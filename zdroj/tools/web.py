#!/usr/bin/env python3
"""Statický web kanálu: stránka ke každému zveřejněnému videu ve všech jazycích.

    python tools/web.py --out <adresář> [--predchozi <adresář>] [--ted 2026-11-17T20:00:00Z]
    python tools/web.py --balik <adresář>     # podklady pro stavbu na GitHubu
    python tools/web.py --vydana              # ID videí, která už mají být venku

Skládá se z věcí, které v repu už leží: titul, stav a čas zveřejnění
z `analytics/videa.json` (na web jde video veřejné, nebo naplánované, jehož
čas už nastal; `zverejneno` u naplánovaného videa lže), popis a kapitoly z `youtube.md`,
lokalizace z `youtube-preklady.md`, text ze `script.md` / `script.<kód>.md`,
časy z `work/timing.json`, obrázky z `images/`, atribuce ze `sources.json`
a odkazy z `factcheck.md`. Témata jsou playlisty z `playlisty.json`.

Ruční soubory webu (`web/`: styl, skript, písmo, stránky pro audit) se
zkopírují beze změny, stránky se vygenerují vedle nich.

`images/` a `work/` jsou mimo git, takže na stroji, kde se video nestavělo,
obrázky chybí. `--predchozi` je pak minulý výstup (zrcadlo GitHub Pages)
a chybějící obrázek se vezme odtamtud, místo aby z webu zmizel.

Web se staví na GitHubu (Actions, každou hodinu), aby naplánované video
přibylo, i když tenhle počítač neběží. `--balik` k tomu vyrobí podklady:
kopii tohohle skriptu, `lib.py`, `web/` a těch souborů videí, které stavba
čte. Skript v balíku si jako kořen vezme balík, takže běží beze změny.

Vystavuje `tools/web_publikuj.sh`. Postup a rozhodnutí: `docs/web.md`.
"""
import argparse
import datetime as dt
import html
import json
import math
import re
import shutil
import sys
import unicodedata
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import lib  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent
SITE = "https://theresmoretoit-channel.github.io"
CHANNEL = "https://www.youtube.com/@theres-more-to-it"
SUBSCRIBE = CHANNEL + "?sub_confirmation=1"
NAME = "There's More To It"
CACHE = Path.home() / ".cache" / "tmti-web-img"

LANGS = ["en", "cs", "de", "es", "fi", "fr", "id", "it", "pl", "pt-BR", "sv", "tr", "uk", "vi"]

T = {
    "en": dict(name="English", tagline="Videos about questions that sound simple until you look closer.",
               newest="Newest video", all="All videos", search="Search videos",
               empty="No video matches that search.", watch="Watch on YouTube", play="Play the video",
               chapters="Chapters", note="The full narration of the video.",
               sources="Sources", links="Pages checked while fact-checking", credits="Image credits",
               related="More on this topic", more="More videos", min="min", topics="Topics",
               subscribe="Subscribe on YouTube", language="Language", videos="videos",
               footer="The videos are published on the There's More To It channel on YouTube.",
               notfound="This page doesn't exist. The videos are all on the home page.",
               home="Home page"),
    "cs": dict(name="Čeština", tagline="Videa o otázkách, které zní jednoduše, dokud se na ně člověk nepodívá zblízka.",
               newest="Nejnovější video", all="Všechna videa", search="Hledat ve videích",
               empty="Žádné video tomuto hledání neodpovídá.", watch="Pustit na YouTube", play="Přehrát video",
               chapters="Kapitoly", note="Celý text videa v překladu. Video je namluvené anglicky a má titulky v tomto jazyce.",
               sources="Zdroje", links="Stránky, podle kterých se ověřovala fakta", credits="Zdroje obrázků",
               related="Další videa na stejné téma", more="Další videa", min="min", topics="Témata",
               subscribe="Odebírat na YouTube", language="Jazyk", videos="videí",
               footer="Videa vycházejí na kanálu There's More To It na YouTube.",
               notfound="Tato stránka neexistuje. Všechna videa jsou na úvodní stránce.",
               home="Úvodní stránka"),
    "de": dict(name="Deutsch", tagline="Videos über Fragen, die einfach klingen, bis man genauer hinsieht.",
               newest="Neuestes Video", all="Alle Videos", search="Videos durchsuchen",
               empty="Zu dieser Suche passt kein Video.", watch="Auf YouTube ansehen", play="Video abspielen",
               chapters="Kapitel", note="Der vollständige Text des Videos in Übersetzung. Das Video selbst ist auf Englisch gesprochen und hat Untertitel in dieser Sprache.",
               sources="Quellen", links="Seiten, mit denen die Fakten geprüft wurden", credits="Bildnachweise",
               related="Mehr zu diesem Thema", more="Weitere Videos", min="Min.", topics="Themen",
               subscribe="Auf YouTube abonnieren", language="Sprache", videos="Videos",
               footer="Die Videos erscheinen auf dem YouTube-Kanal There's More To It.",
               notfound="Diese Seite gibt es nicht. Alle Videos stehen auf der Startseite.",
               home="Startseite"),
    "es": dict(name="Español", tagline="Vídeos sobre preguntas que parecen sencillas hasta que se miran de cerca.",
               newest="Vídeo más reciente", all="Todos los vídeos", search="Buscar vídeos",
               empty="Ningún vídeo coincide con esa búsqueda.", watch="Ver en YouTube", play="Reproducir el vídeo",
               chapters="Capítulos", note="El texto completo del vídeo, traducido. El vídeo está narrado en inglés y tiene subtítulos en este idioma.",
               sources="Fuentes", links="Páginas consultadas para comprobar los datos", credits="Créditos de las imágenes",
               related="Más sobre este tema", more="Más vídeos", min="min", topics="Temas",
               subscribe="Suscribirse en YouTube", language="Idioma", videos="vídeos",
               footer="Los vídeos se publican en el canal There's More To It de YouTube.",
               notfound="Esta página no existe. Todos los vídeos están en la página de inicio.",
               home="Página de inicio"),
    "fi": dict(name="Suomi", tagline="Videoita kysymyksistä, jotka kuulostavat yksinkertaisilta, kunnes niitä katsoo tarkemmin.",
               newest="Uusin video", all="Kaikki videot", search="Hae videoista",
               empty="Yksikään video ei vastaa hakua.", watch="Katso YouTubessa", play="Toista video",
               chapters="Luvut", note="Videon koko teksti käännettynä. Video on englanninkielinen, ja siinä on tämänkieliset tekstitykset.",
               sources="Lähteet", links="Sivut, joilla tiedot tarkistettiin", credits="Kuvien tekijät",
               related="Lisää samasta aiheesta", more="Lisää videoita", min="min", topics="Aiheet",
               subscribe="Tilaa YouTubessa", language="Kieli", videos="videota",
               footer="Videot julkaistaan YouTube-kanavalla There's More To It.",
               notfound="Tätä sivua ei ole. Kaikki videot löytyvät etusivulta.",
               home="Etusivu"),
    "fr": dict(name="Français", tagline="Des vidéos sur des questions qui semblent simples, jusqu'à ce qu'on y regarde de plus près.",
               newest="Vidéo la plus récente", all="Toutes les vidéos", search="Rechercher une vidéo",
               empty="Aucune vidéo ne correspond à cette recherche.", watch="Regarder sur YouTube", play="Lire la vidéo",
               chapters="Chapitres", note="Le texte intégral de la vidéo, traduit. La vidéo elle-même est narrée en anglais, avec des sous-titres dans cette langue.",
               sources="Sources", links="Pages consultées pour vérifier les faits", credits="Crédits des images",
               related="Sur le même sujet", more="Autres vidéos", min="min", topics="Thèmes",
               subscribe="S'abonner sur YouTube", language="Langue", videos="vidéos",
               footer="Les vidéos sont publiées sur la chaîne YouTube There's More To It.",
               notfound="Cette page n'existe pas. Toutes les vidéos sont sur la page d'accueil.",
               home="Page d'accueil"),
    "id": dict(name="Bahasa Indonesia", tagline="Video tentang pertanyaan yang terdengar sederhana sampai kita melihatnya lebih dekat.",
               newest="Video terbaru", all="Semua video", search="Cari video",
               empty="Tidak ada video yang cocok dengan pencarian itu.", watch="Tonton di YouTube", play="Putar video",
               chapters="Bab", note="Teks lengkap video ini dalam terjemahan. Videonya sendiri berbahasa Inggris, dengan subtitel dalam bahasa ini.",
               sources="Sumber", links="Halaman yang dipakai untuk memeriksa fakta", credits="Kredit gambar",
               related="Lebih lanjut tentang topik ini", more="Video lainnya", min="menit", topics="Topik",
               subscribe="Berlangganan di YouTube", language="Bahasa", videos="video",
               footer="Video-video ini diterbitkan di kanal YouTube There's More To It.",
               notfound="Halaman ini tidak ada. Semua video ada di halaman utama.",
               home="Halaman utama"),
    "it": dict(name="Italiano", tagline="Video su domande che sembrano semplici finché non le si guarda da vicino.",
               newest="Video più recente", all="Tutti i video", search="Cerca tra i video",
               empty="Nessun video corrisponde a questa ricerca.", watch="Guarda su YouTube", play="Riproduci il video",
               chapters="Capitoli", note="Il testo completo del video, tradotto. Il video è narrato in inglese, con sottotitoli in questa lingua.",
               sources="Fonti", links="Pagine consultate per verificare i fatti", credits="Crediti delle immagini",
               related="Altro su questo tema", more="Altri video", min="min", topics="Temi",
               subscribe="Iscriviti su YouTube", language="Lingua", videos="video",
               footer="I video sono pubblicati sul canale YouTube There's More To It.",
               notfound="Questa pagina non esiste. Tutti i video sono nella pagina iniziale.",
               home="Pagina iniziale"),
    "pl": dict(name="Polski", tagline="Filmy o pytaniach, które brzmią prosto, dopóki nie przyjrzymy im się bliżej.",
               newest="Najnowszy film", all="Wszystkie filmy", search="Szukaj filmów",
               empty="Żaden film nie pasuje do tego wyszukiwania.", watch="Obejrzyj na YouTube", play="Odtwórz film",
               chapters="Rozdziały", note="Pełny tekst filmu w tłumaczeniu. Sam film jest nagrany po angielsku i ma napisy w tym języku.",
               sources="Źródła", links="Strony, na których sprawdzano fakty", credits="Autorzy zdjęć",
               related="Więcej na ten temat", more="Więcej filmów", min="min", topics="Tematy",
               subscribe="Subskrybuj na YouTube", language="Język", videos="filmów",
               footer="Filmy ukazują się na kanale There's More To It w serwisie YouTube.",
               notfound="Ta strona nie istnieje. Wszystkie filmy są na stronie głównej.",
               home="Strona główna"),
    "pt-BR": dict(name="Português (Brasil)", tagline="Vídeos sobre perguntas que parecem simples até a gente olhar mais de perto.",
               newest="Vídeo mais recente", all="Todos os vídeos", search="Buscar vídeos",
               empty="Nenhum vídeo corresponde a essa busca.", watch="Assistir no YouTube", play="Reproduzir o vídeo",
               chapters="Capítulos", note="O texto completo do vídeo, traduzido. O vídeo é narrado em inglês e tem legendas neste idioma.",
               sources="Fontes", links="Páginas usadas para checar os fatos", credits="Créditos das imagens",
               related="Mais sobre este tema", more="Mais vídeos", min="min", topics="Temas",
               subscribe="Inscrever-se no YouTube", language="Idioma", videos="vídeos",
               footer="Os vídeos são publicados no canal There's More To It no YouTube.",
               notfound="Esta página não existe. Todos os vídeos estão na página inicial.",
               home="Página inicial"),
    "sv": dict(name="Svenska", tagline="Videor om frågor som låter enkla tills man tittar närmare.",
               newest="Senaste videon", all="Alla videor", search="Sök bland videorna",
               empty="Ingen video matchar sökningen.", watch="Titta på YouTube", play="Spela upp videon",
               chapters="Kapitel", note="Videons fullständiga text i översättning. Själva videon är berättad på engelska och har undertexter på det här språket.",
               sources="Källor", links="Sidor som användes för faktakontrollen", credits="Bildkällor",
               related="Mer om samma ämne", more="Fler videor", min="min", topics="Ämnen",
               subscribe="Prenumerera på YouTube", language="Språk", videos="videor",
               footer="Videorna publiceras på YouTube-kanalen There's More To It.",
               notfound="Sidan finns inte. Alla videor finns på startsidan.",
               home="Startsidan"),
    "tr": dict(name="Türkçe", tagline="Yakından bakana kadar basit görünen sorular üzerine videolar.",
               newest="En yeni video", all="Tüm videolar", search="Videolarda ara",
               empty="Bu aramayla eşleşen video yok.", watch="YouTube'da izle", play="Videoyu oynat",
               chapters="Bölümler", note="Videonun tam metninin çevirisi. Video İngilizce anlatılıyor ve bu dilde altyazıları var.",
               sources="Kaynaklar", links="Bilgilerin doğrulandığı sayfalar", credits="Görsellerin kaynakları",
               related="Bu konuda daha fazlası", more="Diğer videolar", min="dk", topics="Konular",
               subscribe="YouTube'da abone ol", language="Dil", videos="video",
               footer="Videolar YouTube'daki There's More To It kanalında yayımlanıyor.",
               notfound="Bu sayfa yok. Tüm videolar ana sayfada.",
               home="Ana sayfa"),
    "uk": dict(name="Українська", tagline="Відео про запитання, які здаються простими, доки не придивишся уважніше.",
               newest="Найновіше відео", all="Усі відео", search="Пошук серед відео",
               empty="За цим запитом відео не знайдено.", watch="Дивитися на YouTube", play="Відтворити відео",
               chapters="Розділи", note="Повний текст відео в перекладі. Саме відео озвучене англійською і має субтитри цією мовою.",
               sources="Джерела", links="Сторінки, за якими перевіряли факти", credits="Автори зображень",
               related="Ще на цю тему", more="Інші відео", min="хв", topics="Теми",
               subscribe="Підписатися на YouTube", language="Мова", videos="відео",
               footer="Відео виходять на YouTube-каналі There's More To It.",
               notfound="Такої сторінки немає. Усі відео — на головній сторінці.",
               home="Головна сторінка"),
    "vi": dict(name="Tiếng Việt", tagline="Video về những câu hỏi nghe có vẻ đơn giản, cho đến khi ta nhìn kỹ hơn.",
               newest="Video mới nhất", all="Tất cả video", search="Tìm video",
               empty="Không có video nào khớp với tìm kiếm này.", watch="Xem trên YouTube", play="Phát video",
               chapters="Chương", note="Toàn bộ lời bình của video, đã dịch. Video được thuyết minh bằng tiếng Anh và có phụ đề bằng ngôn ngữ này.",
               sources="Nguồn", links="Các trang đã dùng để kiểm chứng", credits="Nguồn hình ảnh",
               related="Thêm về chủ đề này", more="Video khác", min="phút", topics="Chủ đề",
               subscribe="Đăng ký trên YouTube", language="Ngôn ngữ", videos="video",
               footer="Các video được đăng trên kênh YouTube There's More To It.",
               notfound="Trang này không tồn tại. Tất cả video đều có ở trang chủ.",
               home="Trang chủ"),
}

TS = re.compile(r"^\s*((?:\d{1,2}:)?\d{1,2}:\d{2})\s+(.+?)\s*$")
URL = re.compile(r"https?://[^\s<>()\[\]`\"'*|]+")


def esc(s):
    return html.escape(s, quote=True)


def prefix(lang):
    return "" if lang == "en" else "/" + lang.lower()


def sekundy(ts):
    n = [int(x) for x in ts.split(":")]
    return n[-1] + 60 * n[-2] + (3600 * n[-3] if len(n) > 2 else 0)


def cas(s):
    s = int(s)
    return f"{s // 3600}:{s % 3600 // 60:02d}:{s % 60:02d}" if s >= 3600 else f"{s // 60}:{s % 60:02d}"


def vycisti(t):
    t = re.sub(r"\s+", " ", t).strip()
    t = t.replace("...", "…")
    return t


def bez_tagu(s):
    return re.sub(r"\s+", " ", html.unescape(re.sub(r"<[^>]+>", "", s or ""))).strip()


# ---------------------------------------------------------------- podklady

def kod_bloky(text):
    return [m.group(1) for m in re.finditer(r"^```[^\n]*\n(.*?)^```", text, re.M | re.S)]


def popis_z_youtube_md(text):
    m = re.search(r"^#+ .*\bPopis\b.*$", text, re.M)
    if not m:
        return None
    b = kod_bloky(text[m.end():])
    return b[0] if b else None


def bloky_popisu(popis):
    return [b.strip("\n").splitlines() for b in re.split(r"\n\s*\n", popis.strip()) if b.strip()]


def druh_bloku(radky):
    t = " ".join(radky)
    if sum(1 for r in radky if TS.match(r)) >= 2:
        return "kapitoly"
    if URL.search(t) or re.search(r"creativecommons|licen|wikimedia|public domain|\bCC[ -]?BY", t, re.I):
        return "kredity"
    if re.match(r"Sources?:", radky[0]):
        return "zdroje"
    if re.search(r"Subtitles are|audio track", t):
        return "titulky"
    return "text"


def rozeber_popis(popis, vzor=None):
    """Vrátí (úvodní odstavce, kapitoly [(s, název)], zdroje [str]).

    `vzor` je rozbor anglického popisu: překlad má tytéž bloky ve stejném
    pořadí, takže se úvod bere podle POČTU anglických úvodních bloků.
    Klasifikovat přeložený text podle anglických slov by nešlo."""
    bloky = bloky_popisu(popis)
    druhy = [druh_bloku(b) for b in bloky]
    if vzor is None:
        n = 0
        while n < len(druhy) and druhy[n] == "text" and n < 3:
            n += 1
    else:
        n = min(vzor["n_uvod"], len(bloky))
        while n and druhy[n - 1] == "kapitoly":
            n -= 1
    uvod = [vycisti(" ".join(b)) for b in bloky[:n]]
    kapitoly = []
    for b, d in zip(bloky, druhy):
        if d == "kapitoly":
            kapitoly = [(sekundy(m.group(1)), m.group(2)) for m in map(TS.match, b) if m]
            break
    zdroje = []
    for b, d in zip(bloky, druhy):
        if d == "zdroje":
            t = vycisti(" ".join(b))
            t = re.sub(r"^Sources?:\s*", "", t).rstrip(".")
            zdroje = [x.strip() for x in t.split(";") if x.strip()]
    return dict(uvod=uvod, kapitoly=kapitoly, zdroje=zdroje, n_uvod=n)


def preklady(text):
    """{kód: (titul, popis)} z youtube-preklady.md."""
    out = {}
    casti = re.split(r"^## .*\(`([A-Za-z-]+)`\)\s*$", text, flags=re.M)
    for i in range(1, len(casti), 2):
        b = kod_bloky(casti[i + 1])
        if len(b) >= 2:
            out[casti[i]] = (b[0].strip(), b[1])
    return out


def odkazy_factcheck(vd):
    p = vd / "factcheck.md"
    if not p.exists():
        return []
    seen, out = set(), []
    for u in URL.findall(p.read_text(encoding="utf-8")):
        u = u.rstrip(".,;:!?")
        if u.endswith(")") and "(" not in u:
            u = u[:-1]
        if u not in seen:
            seen.add(u)
            out.append(u)
    return out


def popisek_odkazu(u):
    m = re.match(r"https?://(?:www\.)?([^/]+)(.*)", u)
    dom, cesta = m.group(1), m.group(2).rstrip("/")
    cesta = re.sub(r"%[0-9A-Fa-f]{2}", lambda x: bytes.fromhex(x.group(0)[1:]).decode("latin-1"), cesta)
    try:
        cesta = cesta.encode("latin-1").decode("utf-8")
    except UnicodeError:
        pass
    t = dom + cesta
    return t if len(t) <= 70 else t[:68] + "…"


# ---------------------------------------------------------------- obrázky

class Obrazky:
    def __init__(self, out, predchozi):
        self.out, self.predchozi = out, predchozi
        self.chybi = []

    def udelej(self, src, rel, sirka, kvalita, fmt="WEBP"):
        """Zmenší `src` do `out/rel` (přes cache). Vrátí (url, w, h) nebo None."""
        from PIL import Image  # až tady: --vydana na GitHubu běží bez Pillow
        dst, c = self.out / rel, CACHE / rel
        dst.parent.mkdir(parents=True, exist_ok=True)
        if src is not None and src.exists():
            if not c.exists() or c.stat().st_mtime < src.stat().st_mtime:
                c.parent.mkdir(parents=True, exist_ok=True)
                im = Image.open(src).convert("RGB")
                if im.width > sirka:
                    im = im.resize((sirka, round(im.height * sirka / im.width)), Image.LANCZOS)
                if fmt == "WEBP":
                    im.save(c, "WEBP", quality=kvalita, method=4)
                else:
                    im.save(c, "JPEG", quality=kvalita, optimize=True, progressive=True)
            shutil.copy2(c, dst)
        elif self.predchozi and (self.predchozi / rel).exists():
            shutil.copy2(self.predchozi / rel, dst)
        else:
            self.chybi.append(rel)
            return None
        with Image.open(dst) as im:
            return "/" + rel, im.width, im.height


# ---------------------------------------------------------------- videa

def ted_utc():
    return dt.datetime.now(dt.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def kdy_vychazi(x):
    """Čas zveřejnění (ISO, UTC), nebo None: video není veřejné ani naplánované."""
    if "stav" not in x:
        sys.exit("CHYBA: analytics/videa.json nemá stav videí — spusť `python tools/analytics.py --videa`")
    if x["stav"] == "public" and x.get("zverejneno"):
        return x["zverejneno"] + "T00:00:00Z"
    if x["stav"] == "private" and x.get("vychazi"):
        return dt.datetime.fromisoformat(x["vychazi"].replace("Z", "+00:00")) \
            .astimezone(dt.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    return None


def seznam_videi(ted=None):
    """Záznamy z videa.json se slugem, které jsou venku (ted=None: i naplánované)."""
    out = []
    for x in json.loads((ROOT / "analytics/videa.json").read_text(encoding="utf-8")):
        k = x.get("slug") and kdy_vychazi(x)
        if k and (ted is None or k <= ted):
            out.append(dict(x, _vychazi=k))
    return out


def nacti_videa(ted):
    zverejnena = {x["slug"]: x for x in seznam_videi(ted)}
    videa = []
    for vd in sorted((ROOT / "videos").iterdir()):
        info = zverejnena.get(vd.name)
        yt = vd / "youtube.md"
        if not info or not yt.exists() or not (vd / "script.md").exists():
            continue
        popis = popis_z_youtube_md(yt.read_text(encoding="utf-8"))
        if not popis:
            print(f"  {vd.name}: v youtube.md není popis, vynechávám", file=sys.stderr)
            continue
        en = rozeber_popis(popis)
        scenar = {"en": lib.parse_script(vd / "script.md")}
        tit = {"en": info["titul"]}
        pop = {"en": en}
        pp = vd / "youtube-preklady.md"
        lok = preklady(pp.read_text(encoding="utf-8")) if pp.exists() else {}
        for l in LANGS[1:]:
            sp = vd / f"script.{l}.md"
            if l not in lok or not sp.exists():
                continue
            s = lib.parse_script(sp)
            if len(set(s) & set(scenar["en"])) < 0.9 * len(scenar["en"]):
                print(f"  {vd.name}: {l} má neúplný scénář, vynechávám", file=sys.stderr)
                continue
            scenar[l] = s
            tit[l] = lok[l][0]
            r = rozeber_popis(lok[l][1], en)
            if len(r["kapitoly"]) != len(en["kapitoly"]):
                r["kapitoly"] = en["kapitoly"]
            if not r["uvod"]:
                r["uvod"] = en["uvod"]
            pop[l] = r
        board = json.loads((vd / "storyboard.json").read_text(encoding="utf-8"))["scenes"] \
            if (vd / "storyboard.json").exists() else []
        proj = json.loads((vd / "project.json").read_text(encoding="utf-8"))
        tp = vd / "work" / "timing.json"
        timing = json.loads(tp.read_text(encoding="utf-8")) if tp.exists() else None
        sources = json.loads((vd / "sources.json").read_text(encoding="utf-8")) \
            if (vd / "sources.json").exists() else {}
        cislo = vd.name.split("-", 1)[0]
        videa.append(dict(
            dir=vd, slug=vd.name, url_slug=vd.name.split("-", 1)[1] if cislo.isdigit() else vd.name,
            cislo=cislo, id=info["id"], datum=info["_vychazi"][:10], titul=tit, popis=pop, scenar=scenar,
            board={s["id"]: s for s in board}, pauza=proj.get("timing", {}).get("scene_pause", 0.8),
            timing=timing, sources=sources, odkazy=odkazy_factcheck(vd)))
    us = [v["url_slug"] for v in videa]
    for v in videa:
        if us.count(v["url_slug"]) > 1:
            v["url_slug"] = v["slug"]
    return videa


def url_videa(v, lang):
    return f"{prefix(lang)}/videos/{v['url_slug']}/"


def srt(v):
    """[(start, konec, text)] z subtitles/en.srt — je v gitu, na rozdíl od work/timing.json."""
    p = v["dir"] / "subtitles" / "en.srt"
    if not p.exists():
        return []
    out = []
    for blok in re.split(r"\n\s*\n", p.read_text(encoding="utf-8").strip()):
        r = blok.splitlines()
        m = re.findall(r"(\d+):(\d+):(\d+)[,.](\d+)", r[1]) if len(r) >= 3 else []
        if len(m) == 2:
            t = [int(h) * 3600 + int(mi) * 60 + int(se) + int(ms) / 1000 for h, mi, se, ms in m]
            out.append((t[0], t[1], " ".join(r[2:])))
    return out


def starty_scen(v):
    """({id scény: začátek}, tolerance). Z timing.json přesně, jinak z en.srt.

    V en.srt se hledají první čtyři slova scény; titulek začíná o lead_in
    dřív než slovo, proto větší tolerance při párování s kapitolou."""
    if v["timing"]:
        return {s["id"]: s["start"] for s in v["timing"]["scenes"]}, 0.01
    slova = [(w, a) for a, _, t in srt(v) for w in re.findall(r"[\w’']+", t.lower())]
    starty, i = {}, 0
    for sid, txt in v["scenar"]["en"].items():
        ws = re.findall(r"[\w’']+", txt.lower())[:4]
        for k in range(i, len(slova) - len(ws) + 1):
            if ws and all(slova[k + j][0] == ws[j] for j in range(len(ws))):
                starty[sid], i = slova[k][1], k + 1
                break
    return starty, 1.2


def delka(v):
    if v["timing"]:
        return v["timing"]["total"]
    s = srt(v)
    return s[-1][1] if s else None


def iso_delka(s):
    s = int(round(s))
    return f"PT{s // 60}M{s % 60}S"


def kapitoly_se_scenami(v):
    """[(sekunda, index kapitoly, [id scén])] podle work/timing.json.

    Kapitola v popisu je začátek scény zaokrouhlený dolů (`youtube.md`),
    takže scéna, která ji otevírá, má floor(start) == čas kapitoly."""
    ids = list(v["scenar"]["en"])
    kap = v["popis"]["en"]["kapitoly"]
    start, tol = starty_scen(v)
    if not start or not kap:
        return [(0, None, ids)]
    hranice = []
    for i, (sec, _) in enumerate(kap):
        j = next((k for k, sid in enumerate(ids) if sid in start and start[sid] >= sec - tol), None)
        if j is None or (hranice and j <= hranice[-1][1]):
            continue
        hranice.append((i, j))
    if not hranice or hranice[0][1] != 0:
        hranice.insert(0, (None, 0))
    out = []
    for n, (i, j) in enumerate(hranice):
        konec = hranice[n + 1][1] if n + 1 < len(hranice) else len(ids)
        out.append((kap[i][0] if i is not None else 0, i, ids[j:konec]))
    return out


def obrazek_sceny(v, sid):
    s = v["board"].get(sid)
    if not s:
        return None
    vis = s.get("visual") or f"images/{sid}.png"
    p = v["dir"] / vis
    return p if p.suffix.lower() in (".png", ".jpg", ".jpeg") else None


def kredit(v, sid):
    s = v["board"].get(sid, {})
    z = v["sources"].get(sid)
    if s.get("source") != "archive" or not z:
        return None
    titul = bez_tagu(z.get("title") or z.get("identifier", ""))
    autor = bez_tagu(z.get("credit", ""))
    lic = bez_tagu(z.get("license", ""))
    return dict(titul=titul, autor=autor, lic=lic, lic_url=z.get("license_url"),
                page=z.get("page") or z.get("source_page"), provider=z.get("provider", ""))


def kredit_html(k):
    t = esc(k["titul"])
    if k["page"]:
        t = f'<a href="{esc(k["page"])}">{t}</a>'
    casti = [t]
    if k["autor"] and k["autor"] not in k["titul"]:
        casti.append(esc(k["autor"]))
    if k["lic"]:
        casti.append(f'<a href="{esc(k["lic_url"])}">{esc(k["lic"])}</a>' if k["lic_url"] else esc(k["lic"]))
    if k["provider"]:
        casti.append(esc(k["provider"]))
    return ", ".join(casti)


# ---------------------------------------------------------------- šablona

def hlavicka(lang, alternativy):
    t = T[lang]
    jazyky = "".join(
        f'<li><a href="{esc(u)}" hreflang="{l}" lang="{l}"{" aria-current=\"page\"" if l == lang else ""}>'
        f'{esc(T[l]["name"])}</a></li>' for l, u in alternativy)
    return f"""<header class="site">
  <a class="brand" href="{prefix(lang)}/">{esc(NAME)}</a>
  <nav>
    <a class="sub" href="{SUBSCRIBE}">{esc(t["subscribe"])}</a>
    <details class="lang"><summary aria-label="{esc(t["language"])}">{esc(t["name"])}</summary><ul>{jazyky}</ul></details>
  </nav>
</header>"""


def paticka(lang, nastroje=False):
    t = T[lang]
    extra = ""
    if nastroje:
        extra = """
  <section class="tools" aria-labelledby="tools-h">
    <h2 id="tools-h">Publishing tools</h2>
    <p>The channel is run with a small set of scripts used only by its owner.</p>
    <ul>
      <li>YouTube publishing toolkit: <a href="/youtube/terms.html">Terms of Service</a>, <a href="/youtube/privacy.html">Privacy policy</a>
        <a class="badge" href="https://www.youtube.com/@theres-more-to-it"><img src="/youtube/developed-with-youtube.png" alt="Developed with YouTube" width="168" height="60"></a></li>
      <li>TikTok uploader: <a href="/tiktok/terms.html">Terms of Service</a>, <a href="/tiktok/privacy.html">Privacy policy</a></li>
    </ul>
  </section>"""
    return f"""<footer class="site">{extra}
  <p>{esc(t["footer"])} <a href="{CHANNEL}">youtube.com/@theres-more-to-it</a></p>
</footer>"""


def stranka(lang, titul, popis, cesta, alternativy, telo, og=None, jsonld=None, nastroje=False, typ="website"):
    alt = "".join(f'\n<link rel="alternate" hreflang="{l}" href="{SITE}{esc(u)}">' for l, u in alternativy)
    if len(alternativy) > 1:
        en = dict(alternativy).get("en")
        if en:
            alt += f'\n<link rel="alternate" hreflang="x-default" href="{SITE}{esc(en)}">'
    og_img = f'\n<meta property="og:image" content="{SITE}{esc(og)}">\n<meta name="twitter:card" content="summary_large_image">' if og else ""
    ld = f'\n<script type="application/ld+json">{json.dumps(jsonld, ensure_ascii=False)}</script>' if jsonld else ""
    plny = titul if titul == NAME else f"{titul} | {NAME}"
    return f"""<!doctype html>
<html lang="{lang}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{esc(plny)}</title>
<meta name="description" content="{esc(popis)}">
<link rel="canonical" href="{SITE}{esc(cesta)}">{alt}
<meta property="og:type" content="{typ}">
<meta property="og:site_name" content="{esc(NAME)}">
<meta property="og:title" content="{esc(titul)}">
<meta property="og:description" content="{esc(popis)}">
<meta property="og:url" content="{SITE}{esc(cesta)}">{og_img}
<meta name="color-scheme" content="dark light">
<link rel="preload" href="/fonts/source-serif-Regular.woff2" as="font" type="font/woff2" crossorigin>
<link rel="stylesheet" href="/style.css">
<link rel="icon" href="/favicon.ico" sizes="16x16 32x32 48x48">
<link rel="icon" href="/favicon.svg" type="image/svg+xml">
<link rel="apple-touch-icon" href="/apple-touch-icon.png">
<link rel="alternate" type="application/atom+xml" title="{esc(NAME)}" href="/feed.xml">{ld}
</head>
<body>
{hlavicka(lang, alternativy)}
<main id="main">
{telo}
</main>
{paticka(lang, nastroje)}
<script src="/site.js" defer></script>
</body>
</html>
"""


def kratky_popis(v, lang, n=158):
    t = v["popis"][lang]["uvod"][0] if v["popis"][lang]["uvod"] else v["titul"][lang]
    if len(t) <= n:
        return t
    t = t[:n].rsplit(" ", 1)[0]
    return t.rstrip(",;:") + "…"


# Datum, jak se píše v dané zemi (CLDR, formát „long“; vygenerováno z Babel 2.18,
# vloženo napevno, ať stavba na GitHubu nepotřebuje knihovnu navíc).
DATUM = {
    "en": ("{d} {m} {y}", ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']),
    "cs": ("{d}. {m} {y}", ['ledna', 'února', 'března', 'dubna', 'května', 'června', 'července', 'srpna', 'září', 'října', 'listopadu', 'prosince']),
    "de": ("{d}. {m} {y}", ['Januar', 'Februar', 'März', 'April', 'Mai', 'Juni', 'Juli', 'August', 'September', 'Oktober', 'November', 'Dezember']),
    "es": ("{d} de {m} de {y}", ['enero', 'febrero', 'marzo', 'abril', 'mayo', 'junio', 'julio', 'agosto', 'septiembre', 'octubre', 'noviembre', 'diciembre']),
    "fi": ("{d}. {m} {y}", ['tammikuuta', 'helmikuuta', 'maaliskuuta', 'huhtikuuta', 'toukokuuta', 'kesäkuuta', 'heinäkuuta', 'elokuuta', 'syyskuuta', 'lokakuuta', 'marraskuuta', 'joulukuuta']),
    "fr": ("{d} {m} {y}", ['janvier', 'février', 'mars', 'avril', 'mai', 'juin', 'juillet', 'août', 'septembre', 'octobre', 'novembre', 'décembre']),
    "id": ("{d} {m} {y}", ['Januari', 'Februari', 'Maret', 'April', 'Mei', 'Juni', 'Juli', 'Agustus', 'September', 'Oktober', 'November', 'Desember']),
    "it": ("{d} {m} {y}", ['gennaio', 'febbraio', 'marzo', 'aprile', 'maggio', 'giugno', 'luglio', 'agosto', 'settembre', 'ottobre', 'novembre', 'dicembre']),
    "pl": ("{d} {m} {y}", ['stycznia', 'lutego', 'marca', 'kwietnia', 'maja', 'czerwca', 'lipca', 'sierpnia', 'września', 'października', 'listopada', 'grudnia']),
    "pt-BR": ("{d} de {m} de {y}", ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho', 'julho', 'agosto', 'setembro', 'outubro', 'novembro', 'dezembro']),
    "sv": ("{d} {m} {y}", ['januari', 'februari', 'mars', 'april', 'maj', 'juni', 'juli', 'augusti', 'september', 'oktober', 'november', 'december']),
    "tr": ("{d} {m} {y}", ['Ocak', 'Şubat', 'Mart', 'Nisan', 'Mayıs', 'Haziran', 'Temmuz', 'Ağustos', 'Eylül', 'Ekim', 'Kasım', 'Aralık']),
    "uk": ("{d} {m} {y} р.", ['січня', 'лютого', 'березня', 'квітня', 'травня', 'червня', 'липня', 'серпня', 'вересня', 'жовтня', 'листопада', 'грудня']),
    "vi": ("{d} {m}, {y}", ['tháng 1', 'tháng 2', 'tháng 3', 'tháng 4', 'tháng 5', 'tháng 6', 'tháng 7', 'tháng 8', 'tháng 9', 'tháng 10', 'tháng 11', 'tháng 12']),
}


def datum_textem(iso, lang):
    vzor, mesice = DATUM[lang]
    y, m, d = (int(x) for x in iso.split("-"))
    # francouzsky je první den v měsíci řadová číslovka (1er mai), CLDR to neumí
    return vzor.format(d="1er" if lang == "fr" and d == 1 else d, m=mesice[m - 1], y=y)


def meta_videa(v, lang):
    t = T[lang]
    d = delka(v)
    casti = []
    if d:
        casti.append(f'<span>{math.ceil(d / 60)} {esc(t["min"])}</span>')
    casti.append(f'<time datetime="{v["datum"]}">{esc(datum_textem(v["datum"], lang))}</time>')
    return f'<p class="meta">{"".join(casti)}</p>'


# Obrázky jdou ve více šířkách a prohlížeč si podle `sizes` vezme nejmenší, která
# pokryje místo na displeji (PageSpeed 2026-11-17: náhledy 640 px zobrazené ve
# ~250 px, úspora 854 KiB). `sizes` odpovídá rozvržení ve style.css: obsah má
# nejvýš 52rem včetně okrajů, seznam má sloupce od 15rem, text 38rem.
SIZES_SEZNAM = "(max-width: 40rem) calc(100vw - 2rem), (max-width: 52rem) calc(50vw - 2rem), 16rem"
SIZES_PLNA = "(max-width: 52rem) calc(100vw - 2rem), 50rem"
SIZES_TEXT = "(max-width: 40rem) calc(100vw - 4rem), 38rem"


def img(ob, src, varianty, kvalita, sizes, attrs):
    """<img> se srcset; `varianty` = [(rel, šířka)] od nejmenší. Chybějící varianta vypadne."""
    hotove = [r for r in (ob.udelej(src, rel, w, kvalita) for rel, w in varianty) if r]
    if not hotove:
        return ""
    url, w, h = hotove[-1]
    ss = (f' srcset="{", ".join(f"{u} {x}w" for u, x, _ in hotove)}" sizes="{sizes}"'
          if len(hotove) > 1 else "")
    return f'<img src="{url}"{ss} width="{w}" height="{h}" {attrs}>'


def img_nahledu(v, ob, sirky, sizes, attrs):
    return img(ob, v["dir"] / "render/thumbnail.jpg",
               [(f"thumbs/{v['cislo']}-{s}.webp", s) for s in sirky], 78, sizes, attrs)


def polozka_seznamu(v, lang, ob):
    img = img_nahledu(v, ob, (320, 640), SIZES_SEZNAM, 'alt="" loading="lazy" decoding="async"')
    return f"""<li><a href="{url_videa(v, lang)}">{img}<span class="vt">{esc(v["titul"][lang])}</span></a>{meta_videa(v, lang)}</li>"""


# ---------------------------------------------------------------- stránky

def stranka_videa(v, lang, ob, tema, souvisejici):
    t = T[lang]
    vid = v["id"]
    titul = v["titul"][lang]
    pop = v["popis"][lang]
    yt = f"https://www.youtube.com/watch?v={vid}"
    og = ob.udelej(v["dir"] / "render/thumbnail.jpg", f"og/{v['cislo']}.jpg", 1280, 84, fmt="JPEG")
    parametry = "" if lang == "en" else f"&cc_load_policy=1&cc_lang_pref={lang}&hl={lang}"
    poster_img = img_nahledu(v, ob, (640, 960, 1280), SIZES_PLNA, 'alt="" fetchpriority="high"')
    hraj = f"""<div class="player" data-id="{vid}" data-params="{esc(parametry)}" data-title="{esc(titul)}">
  <a class="player-box" href="{yt}" aria-label="{esc(t["play"])}: {esc(titul)}">{poster_img}<span class="play" aria-hidden="true"></span></a>
</div>"""

    kap_nazvy = pop["kapitoly"]
    casti = []
    kredity = []
    uz = set()
    for sec, ki, ids in kapitoly_se_scenami(v):
        odst, akt, delka_akt = [], [], 0
        for sid in ids:
            txt = v["scenar"][lang].get(sid)
            # Mluvená výzva k odběru (videa 044–120, `docs/cta.md`) do textu nepatří.
            if not txt or v["board"].get(sid, {}).get("cta"):
                continue
            akt.append(vycisti(txt))
            delka_akt += len(txt)
            pauza = v["board"].get(sid, {}).get("pause", v["pauza"])
            if pauza >= 1.5 or delka_akt > 520:
                odst.append(" ".join(akt))
                akt, delka_akt = [], 0
        if akt:
            odst.append(" ".join(akt))
        if not odst:
            continue
        obr = ""
        for sid in ids:
            src = obrazek_sceny(v, sid)
            if not src:
                continue
            alt = vycisti(v["scenar"][lang].get(sid, ""))[:180]
            tag = img(ob, src, [(f"img/{v['cislo']}/{sid}-640.webp", 640), (f"img/{v['cislo']}/{sid}.webp", 1200)],
                      74, SIZES_TEXT, f'alt="{esc(alt)}" loading="lazy" decoding="async"')
            if not tag:
                continue
            k = kredit(v, sid)
            cap = ""
            if k:
                cap = f"<figcaption>{kredit_html(k)}</figcaption>"
                if sid not in uz:
                    kredity.append(k)
                    uz.add(sid)
            obr = f'<figure>{tag}{cap}</figure>'
            break
        hlava = ""
        if ki is not None:
            nazev = kap_nazvy[ki][1] if ki < len(kap_nazvy) else v["popis"]["en"]["kapitoly"][ki][1]
            hlava = (f'<h2 id="t{sec}"><a class="ts" href="{yt}&amp;t={sec}s" data-t="{sec}">{cas(sec)}</a>'
                     f'<span>{esc(nazev)}</span></h2>')
        p = [f"<p>{esc(x)}</p>" for x in odst]
        if obr:
            p.insert(1, obr)
        casti.append(f'<section class="ch">{hlava}{"".join(p)}</section>')

    zdroje = ""
    if v["popis"]["en"]["zdroje"]:
        zdroje = f'<h2>{esc(t["sources"])}</h2><ul class="src">' + "".join(
            f"<li>{esc(z)}</li>" for z in v["popis"]["en"]["zdroje"]) + "</ul>"
    if v["odkazy"]:
        zdroje += (f'<details class="links"><summary>{esc(t["links"])} ({len(v["odkazy"])})</summary><ul>'
                   + "".join(f'<li><a href="{esc(u)}" rel="nofollow noopener">{esc(popisek_odkazu(u))}</a></li>'
                             for u in v["odkazy"]) + "</ul></details>")
    kred = ""
    if kredity:
        kred = f'<h2>{esc(t["credits"])}</h2><ul class="cred">' + "".join(
            f"<li>{kredit_html(k)}</li>" for k in kredity) + "</ul>"
    dal = ""
    if souvisejici:
        nadpis = t["related"] if tema else t["more"]
        dal = (f'<section class="related"><h2>{esc(nadpis)}</h2><ul class="vlist">'
               + "".join(polozka_seznamu(x, lang, ob) for x in souvisejici) + "</ul></section>")

    tema_odkaz = ""
    if tema and lang == "en":
        tema_odkaz = f'<p class="topic"><a href="/topics/{tema["klic"]}/">{esc(kratky_titul(tema))}</a></p>'

    # První odstavec popisu je skoro doslova první scéna, takže by se nad
    # textem opakoval. Nad text patří shrnutí; samotný úvod jde do meta popisu.
    uvod = "".join(f'<p class="lead">{esc(x)}</p>' for x in (pop["uvod"][1:] or pop["uvod"]))
    telo = f"""<article class="video">
<header class="vh">
{tema_odkaz}<h1>{esc(titul)}</h1>
{meta_videa(v, lang)}
</header>
{hraj}
<div class="intro">{uvod}
<p class="actions"><a class="btn" href="{yt}">{esc(t["watch"])}</a><a href="{SUBSCRIBE}">{esc(t["subscribe"])}</a></p>
</div>
<div class="transcript">
<div class="rail" aria-hidden="true"><div class="rail-fill"></div></div>
<p class="note">{esc(T["en"]["note"] if lang == "en" else t["note"])}</p>
{"".join(casti)}
</div>
<footer class="vf">
{zdroje}{kred}
</footer>
</article>
{dal}"""

    jl = {"@context": "https://schema.org", "@type": "VideoObject", "name": titul,
          "description": " ".join(pop["uvod"]) or titul, "uploadDate": v["datum"],
          "thumbnailUrl": [SITE + og[0]] if og else [],
          "embedUrl": f"https://www.youtube.com/embed/{vid}", "url": SITE + url_videa(v, lang),
          "inLanguage": "en", "transcript": " ".join(vycisti(x) for k, x in v["scenar"][lang].items()
                                if not v["board"].get(k, {}).get("cta"))}
    if lang != "en":
        jl["subtitleLanguage"] = lang
        jl.pop("transcript")
    if delka(v):
        jl["duration"] = iso_delka(delka(v))
    alternativy = [(l, url_videa(v, l)) for l in LANGS if l in v["scenar"]]
    return stranka(lang, titul, kratky_popis(v, lang), url_videa(v, lang), alternativy, telo,
                   og=og[0] if og else None, jsonld=jl, typ="video.other")


def kratky_titul(tema):
    return tema["titul"].split(" — ")[0]


def stranka_domu(lang, videa, temata, ob):
    t = T[lang]
    moje = [v for v in videa if lang in v["scenar"]]
    moje.sort(key=lambda v: (v["datum"], v["cislo"]), reverse=True)
    nej = moje[0]
    obr = img_nahledu(nej, ob, (640, 960, 1280), SIZES_PLNA, 'alt="" fetchpriority="high"')
    uvod = nej["popis"][lang]["uvod"][0] if nej["popis"][lang]["uvod"] else ""
    temata_html = ""
    if lang == "en":
        temata_html = '<section class="topics" aria-labelledby="topics-h"><h2 id="topics-h">Topics</h2><ul>' + "".join(
            f'<li><a href="/topics/{x["klic"]}/">{esc(kratky_titul(x))}</a> <span>{len(x["_videa"])}</span></li>'
            for x in temata if x["_videa"]) + "</ul></section>"
    # Záhlaví po vzoru stránky kanálu na YouTube: banner (výřez 1546×423, který
    # YouTube ukazuje na všech zařízeních), profilovka, název, handle, popis, odběr.
    telo = f"""<section class="hero kanal-hero">
<img class="banner" src="/kanal/banner-1546.webp" srcset="/kanal/banner-800.webp 800w, /kanal/banner-1546.webp 1546w" sizes="{SIZES_PLNA}" width="1546" height="423" alt="">
<div class="kanal">
<img class="profil" src="/kanal/profil-192.webp" width="96" height="96" alt="">
<div class="kanal-text">
<h1>{esc(NAME)}</h1>
<p class="handle"><span>@theres-more-to-it</span><span>{len(moje)} {esc(t["videos"])}</span></p>
<p class="tagline">{esc(t["tagline"])}</p>
<a class="odber" href="{SUBSCRIBE}">{esc(t["subscribe"])}</a>
</div>
</div>
</section>
<section class="newest" aria-labelledby="newest-h">
<h2 id="newest-h" class="quiet">{esc(t["newest"])}</h2>
<a class="feature" href="{url_videa(nej, lang)}">{obr}<span class="ft">{esc(nej["titul"][lang])}</span></a>
<p class="lead">{esc(uvod)}</p>
{meta_videa(nej, lang)}
</section>
{temata_html}
<section class="all" aria-labelledby="all-h">
<div class="all-head"><h2 id="all-h">{esc(t["all"])} <span class="count">{len(moje)}</span></h2>
<label class="search"><span class="vh-only">{esc(t["search"])}</span><input id="q" type="search" placeholder="{esc(t["search"])}" autocomplete="off"></label></div>
<ul class="vlist">{"".join(polozka_seznamu(v, lang, ob) for v in moje)}</ul>
<p class="empty" hidden>{esc(t["empty"])}</p>
</section>"""
    alternativy = [(l, prefix(l) + "/") for l in LANGS]
    return stranka(lang, NAME, t["tagline"], prefix(lang) + "/", alternativy, telo,
                   og=f"/og/{nej['cislo']}.jpg", nastroje=(lang == "en"))


def stranka_tematu(tema, ob):
    vs = tema["_videa"]
    telo = f"""<section class="hero topic-hero">
<p class="crumb"><a href="/">{esc(NAME)}</a></p>
<h1>{esc(tema["titul"])}</h1>
<p class="tagline">{esc(tema.get("popis", ""))}</p>
</section>
<section class="all"><ul class="vlist">{"".join(polozka_seznamu(v, "en", ob) for v in vs)}</ul></section>"""
    cesta = f"/topics/{tema['klic']}/"
    return stranka("en", kratky_titul(tema), tema.get("popis", "")[:158], cesta, [("en", cesta)], telo,
                   og=f"/og/{vs[0]['cislo']}.jpg")


def stranka_404():
    telo = f"""<section class="hero"><h1>404</h1><p class="tagline">{esc(T["en"]["notfound"])}</p>
<p><a class="btn" href="/">{esc(T["en"]["home"])}</a></p></section>"""
    return stranka("en", "Page not found", T["en"]["notfound"], "/404.html", [("en", "/")], telo)


def sitemap(videa, temata):
    radky = []

    def url(cesta, alts, lastmod):
        a = "".join(f'<xhtml:link rel="alternate" hreflang="{l}" href="{SITE}{u}"/>' for l, u in alts)
        radky.append(f"<url><loc>{SITE}{cesta}</loc><lastmod>{lastmod}</lastmod>{a}</url>")

    dnes = dt.date.today().isoformat()
    homes = [(l, prefix(l) + "/") for l in LANGS]
    for l, u in homes:
        url(u, homes, dnes)
    for x in temata:
        if x["_videa"]:
            url(f"/topics/{x['klic']}/", [], dnes)
    for v in videa:
        alts = [(l, url_videa(v, l)) for l in LANGS if l in v["scenar"]]
        for l, u in alts:
            url(u, alts, v["datum"])
    return ('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" '
            'xmlns:xhtml="http://www.w3.org/1999/xhtml">\n' + "\n".join(radky) + "\n</urlset>\n")


def feed(videa):
    vs = sorted(videa, key=lambda v: (v["datum"], v["cislo"]), reverse=True)[:30]
    pol = "".join(f"""
<entry><title>{esc(v["titul"]["en"])}</title><link href="{SITE}{url_videa(v, "en")}"/>
<id>{SITE}{url_videa(v, "en")}</id><updated>{v["datum"]}T12:00:00Z</updated>
<summary>{esc(" ".join(v["popis"]["en"]["uvod"]))}</summary></entry>""" for v in vs)
    return f"""<?xml version="1.0" encoding="utf-8"?>
<feed xmlns="http://www.w3.org/2005/Atom"><title>{esc(NAME)}</title>
<link href="{SITE}/"/><link rel="self" href="{SITE}/feed.xml"/><id>{SITE}/</id>
<updated>{vs[0]["datum"]}T12:00:00Z</updated><author><name>{esc(NAME)}</name></author>{pol}
</feed>
"""


def zapis(out, cesta, obsah):
    p = out / cesta.lstrip("/")
    if cesta.endswith("/"):
        p = p / "index.html"
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(obsah, encoding="utf-8")


# Co stavba čte z adresáře videa (viz nacti_videa, srt, kredit, odkazy_factcheck).
# Obrázky ne: ty jdou do balíku už zmenšené, jako minulý výstup (--predchozi).
SOUBORY_VIDEA = ["youtube.md", "youtube-preklady.md", "script.md", "storyboard.json", "project.json",
                 "sources.json", "factcheck.md", "subtitles/en.srt", "work/timing.json"]


def balik(cil):
    """Podklady pro stavbu na GitHubu: videa veřejná i naplánovaná, nic jiného."""
    if cil.exists():
        shutil.rmtree(cil)
    (cil / "tools").mkdir(parents=True)
    for f in ("tools/web.py", "tools/lib.py"):
        shutil.copy2(ROOT / f, cil / f)
    shutil.copy2(ROOT / "playlisty.json", cil / "playlisty.json")
    shutil.copytree(ROOT / "web", cil / "web")
    vybrana = seznam_videi()
    pole = ("id", "titul", "zverejneno", "slug", "stav", "vychazi")
    (cil / "analytics").mkdir()
    (cil / "analytics/videa.json").write_text(json.dumps(
        [{k: x.get(k, "") for k in pole} for x in vybrana], ensure_ascii=False, indent=1), encoding="utf-8")
    for x in vybrana:
        vd = ROOT / "videos" / x["slug"]
        for rel in SOUBORY_VIDEA + [p.name for p in vd.glob("script.*.md")]:
            if (vd / rel).exists():
                (cil / "videos" / x["slug"] / rel).parent.mkdir(parents=True, exist_ok=True)
                shutil.copy2(vd / rel, cil / "videos" / x["slug"] / rel)
    print(f"web: balík {len(vybrana)} videí -> {cil}")


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--out", type=Path)
    ap.add_argument("--predchozi", type=Path, help="minulý výstup; odtud se vezmou obrázky, které tu chybí")
    ap.add_argument("--ted", default=ted_utc(),
                    help="okamžik, ke kterému se web staví (UTC); 9999 = i všechna naplánovaná videa")
    ap.add_argument("--balik", type=Path, help="vyrobí podklady pro stavbu na GitHubu a skončí")
    ap.add_argument("--vydana", action="store_true", help="vypíše JSON s ID videí, která už mají být venku")
    a = ap.parse_args()

    if a.vydana:
        print(json.dumps(sorted(x["id"] for x in seznam_videi(a.ted))))
        return
    if a.balik:
        balik(a.balik.resolve())
        return
    if not a.out:
        ap.error("chybí --out")

    out = a.out.resolve()
    if out.exists():
        shutil.rmtree(out)
    shutil.copytree(ROOT / "web", out)
    ob = Obrazky(out, a.predchozi.resolve() if a.predchozi else None)

    videa = nacti_videa(a.ted)
    podle_slugu = {v["slug"]: v for v in videa}
    temata = json.loads((ROOT / "playlisty.json").read_text(encoding="utf-8"))["playlisty"]
    for x in temata:
        x["_videa"] = [podle_slugu[s] for s in x.get("videa", []) if s in podle_slugu]

    stran = 0
    for v in videa:
        tema = min((x for x in temata if v in x["_videa"]), key=lambda x: len(x["_videa"]), default=None)
        if tema:
            ostatni = [x for x in tema["_videa"] if x is not v]
        else:
            ostatni = [x for x in videa if x is not v]
        ostatni.sort(key=lambda x: abs(int(x["cislo"]) - int(v["cislo"])) if x["cislo"].isdigit() and v["cislo"].isdigit() else 999)
        for lang in v["scenar"]:
            souv = [x for x in ostatni if lang in x["scenar"]][:4]
            zapis(out, url_videa(v, lang), stranka_videa(v, lang, ob, tema, souv))
            stran += 1
    for lang in LANGS:
        zapis(out, prefix(lang) + "/", stranka_domu(lang, videa, temata, ob))
        stran += 1
    for x in temata:
        if x["_videa"]:
            zapis(out, f"/topics/{x['klic']}/", stranka_tematu(x, ob))
            stran += 1
    zapis(out, "/404.html", stranka_404())
    zapis(out, "/sitemap.xml", sitemap(videa, temata))
    zapis(out, "/feed.xml", feed(videa))
    zapis(out, "/robots.txt", f"User-agent: *\nAllow: /\nSitemap: {SITE}/sitemap.xml\n")
    # Podle tohohle pozná hodinová kontrola na GitHubu, jestli od minula něco vyšlo.
    # Stejná množina jako --vydana (ne `videa`: z těch se vynechává video bez popisu
    # a kontrola by pak stavěla každou hodinu znovu).
    zapis(out, "/stav.json", json.dumps({"vydana": sorted(x["id"] for x in seznam_videi(a.ted)), "sestaveno": a.ted}) + "\n")

    jazyku = sum(len(v["scenar"]) for v in videa)
    print(f"web: {len(videa)} videí, {jazyku} stránek videí, celkem {stran} stránek -> {out}")
    bez = sorted({r.split("/")[1] for r in ob.chybi if r.startswith("img/")})
    if bez:
        print(f"web: videa bez obrázků scén (images/ tu není ani v --predchozi): {', '.join(bez)}",
              file=sys.stderr)


if __name__ == "__main__":
    main()
