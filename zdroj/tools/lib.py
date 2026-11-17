"""Sdílené utility pro video pipeline."""
import json, re, subprocess, sys, unicodedata
from pathlib import Path

sys.stdout.reconfigure(line_buffering=True)  # ať je vidět postup i při přesměrování

ROOT = Path(__file__).resolve().parent.parent
MODELS = ROOT / "models"


def cislo_videa(video_dir):
    """Číslo videa z názvu adresáře (`068-why-...` -> `068`), nebo prázdný
    řetězec, když adresář číslem nezačíná (hudební větev `lin-audio-049`,
    testovací adresáře)."""
    m = re.match(r"(\d+)", Path(video_dir).name)
    return m.group(1) if m else ""


def master_mp4(video_dir, zaklad="final-en"):
    """Cesta k finálnímu MP4 s číslem videa v názvu
    (`render/final-en-068.mp4`). Číslo tam je proto, aby se ukázalo v poli
    Název souboru na YouTube. Adresář bez čísla (hudební video) dostane
    jméno bez čísla."""
    n = cislo_videa(video_dir)
    jm = f"{zaklad}-{n}.mp4" if n else f"{zaklad}.mp4"
    return Path(video_dir) / "render" / jm


def najdi_master(video_dir, zaklad="final-en"):
    """Najde existující finální MP4: nejdřív s číslem (nová konvence od
    2026-09-28), pak bez čísla (starší videa). Vrátí None, když ani jedno
    neexistuje."""
    p = master_mp4(video_dir, zaklad)
    if p.exists():
        return p
    stary = Path(video_dir) / "render" / f"{zaklad}.mp4"
    return stary if stary.exists() else None


def load(video_dir: Path, scenar: str = "script.md"):
    """`scenar` je jméno souboru se scénářem, ne cesta.

    Americká stopa videa 000 potřebuje JINÝ TEXT dvou scén než britská —
    video mluví o vlastním hlasu, takže „the British voice" musí v americké
    stopě znít „the American voice". Je to tentýž mechanismus jako u devíti
    překladů (tytéž značky scén, tentýž počet řádků), jen desátý jazyk;
    `script.en-US.md` proto čte i tts.py, ne jen subtitles.py.

    Bez argumentu se chová přesně jako dřív.
    """
    proj = json.loads((video_dir / "project.json").read_text(encoding="utf-8"))
    board = json.loads((video_dir / "storyboard.json").read_text(encoding="utf-8"))

    # Hudební video nemá scénář — scény určuje hudba, ne řeč. Dělí se podle
    # `kind` v datech, ne podle adresáře: `videos/` zůstává plochý a nástroje
    # sdílené. Storyboard je tu jediný zdroj scén, takže se vrátí, jak je.
    if proj.get("kind") == "music":
        return proj, [dict(s) for s in board["scenes"]]

    sc_path = video_dir / scenar
    if not sc_path.exists():
        sys.exit(f"CHYBA: chybí {sc_path}")
    scenes = parse_script(sc_path)
    segments = parse_script_segments(sc_path)

    by_id = {s["id"]: s for s in board["scenes"]}
    missing = [sid for sid in scenes if sid not in by_id]
    if missing:
        sys.exit(f"CHYBA: scény {missing} jsou ve {scenar}, ale chybí ve storyboard.json")

    ordered = []
    for sid, text in scenes.items():
        sc = dict(by_id[sid])
        sc["text"] = text
        sc["segments"] = segments.get(sid, [(text, None)])
        ordered.append(sc)
    return proj, ordered


#: Cizí fráze na začátku řádku: `{de} Ein rotes Auto.`
#: Pro titulky a zarovnání je to obyčejný text, pro tts.py je to pokyn
#: „tohle řekni nativním hlasem jako samostatnou promluvu".
FOREIGN_TAG = re.compile(r"\{([a-z]{2})\}\s*")


def strip_markdown(t: str) -> str:
    """Odstraní markdown značky, které by TTS přečetlo doslova.

    `*is*` Kokoro vyslovilo jako „asterisk is asterisk". Zvýraznění je
    ve scénáři pokyn pro přednes, jenže Kokoro důraz neumí — takže se
    značka jen odstraní a důraz se dělá tempem a pauzou (viz CLAUDE.md).
    """
    t = re.sub(r"\*\*(.+?)\*\*", r"\1", t)
    t = re.sub(r"(?<!\w)\*(.+?)\*(?!\w)", r"\1", t)
    t = re.sub(r"(?<!\w)_(.+?)_(?!\w)", r"\1", t)
    t = re.sub(r"`(.+?)`", r"\1", t)
    t = FOREIGN_TAG.sub("", t)
    return t


def cti_scenar(path: Path):
    """Načte scénář a NORMALIZUJE ho na NFC.

    Písmeno s diakritikou lze v Unicode zapsat dvěma způsoby: jako jeden
    znak (NFC, `ế` = U+1EBF), nebo jako základ plus skládající se značky
    (NFD, `e` + U+0302 + U+0301). Na obrazovce jsou k nerozeznání,
    ale `len()` je spočítá různě — a `subtitles.py` podle délky zalamuje
    řádky proti `subtitles.max_chars`.

    U vietnamštiny, která skládá na jedno písmeno DVĚ diakritiky (znak
    a tón), je ten rozdíl **+33 %** (naměřeno 2026-09-15 na větě o 48
    znacích: NFD jich má 64). Překlad v NFD by se tedy zalamoval mnohem
    dřív a titulky by vyšly zbytečně roztrhané — vada, kterou jinak řeší
    `balanced_bounds()` a `merge_short()`.

    NFD nevzniká náhodou, přichází zvenčí: dává ho část editorů
    a překladačů a přežije schránku. Okem se nepozná, jen měřením.
    Všech devět překladů z doby zavedení v NFC už bylo, takže je to
    pojistka pro nové jazyky (vi, fi, uk, tr, id), ne změna chování.
    """
    return unicodedata.normalize("NFC", path.read_text(encoding="utf-8"))


def parse_script(path: Path):
    """Rozdělí script.md podle značek <!-- Sxx --> na {id: text}."""
    raw = cti_scenar(path)
    parts = re.split(r"<!--\s*(S\d+[a-z]?)\s*-->", raw)
    out = {}
    for i in range(1, len(parts), 2):
        text = strip_markdown(re.sub(r"\s*\n\s*", " ", parts[i + 1])).strip()
        if text:
            out[parts[i]] = text
    if not out:
        sys.exit(f"CHYBA: ve {path} nejsou žádné značky <!-- Sxx -->")
    return out


def parse_script_lines(path: Path):
    """Jako parse_script, ale zachová členění na řádky: {id: [řádek, ...]}.

    Řádek je přirozená jednotka scénáře (jedna fráze) a zároveň jednotka,
    ve které se překládá. Slova řádku odpovídají slovům ve work/words.json,
    takže z nich jde odvodit čas každého řádku bez dalšího zarovnávání.
    """
    raw = cti_scenar(path)
    parts = re.split(r"<!--\s*(S\d+[a-z]?)\s*-->", raw)
    out = {}
    for i in range(1, len(parts), 2):
        lines = [strip_markdown(l).strip() for l in parts[i + 1].splitlines() if l.strip()]
        if lines:
            out[parts[i]] = lines
    return out


def parse_script_segments(path: Path):
    """{id: [(text, jazyk|None), ...]} — cizí fráze jako samostatný úsek.

    Cizí fráze MUSÍ být vlastní promluva nativním hlasem. Ve společné
    promluvě s angličtinou se vsákne do věty a ztratí vlastní intonaci —
    „…appears in German ein rotes Auto" se slije v jedno. Naměřeno
    2026-08-27: uživatel slyšel rozdíl i tam, kde byly FONÉMY TOTOŽNÉ
    a lišilo se jen to, že šlo o samostatné promluvy.

    Úsek je vždycky celý řádek, protože řádek je jednotka scénáře
    i překladu. Sousední anglické řádky se slévají do jednoho úseku,
    aby uvnitř nevznikaly zbytečné hranice promluv.
    """
    raw = cti_scenar(path)
    parts = re.split(r"<!--\s*(S\d+[a-z]?)\s*-->", raw)
    out = {}
    for i in range(1, len(parts), 2):
        segs, buf = [], []
        for line in parts[i + 1].splitlines():
            line = line.strip()
            if not line:
                continue
            m = FOREIGN_TAG.match(line)
            if m:
                if buf:
                    segs.append((strip_markdown(" ".join(buf)).strip(), None))
                    buf = []
                segs.append((strip_markdown(line[m.end():]).strip(), m.group(1)))
            else:
                buf.append(line)
        if buf:
            segs.append((strip_markdown(" ".join(buf)).strip(), None))
        if segs:
            out[parts[i]] = segs
    return out


def sentences(text: str, min_words: int = 4):
    """Rozdělí text scény na věty pro samostatná volání TTS.

    Dvě pravidla, obě zaplacené poslechem:

    1. **Nedělit na výpustce.** `(?<=[.?!])` by rozseklo i „underneath... they",
       protože výpustka končí tečkou. Vznikl by útržek bez podmětu a Kokoro
       ho vysloví špatně. Proto se koukáme dva znaky zpět.
    2. **Krátké věty přilepit k předchozí.** Jednoslovné věty („Infrared.",
       „That Hertz.") samostatně znějí uříznutě; ve výčtu spektra by se
       sedm názvů rozpadlo na sedm útržků.
    2b. **Ale ne, když je v nich VÝPUSTKA.** Věta s „..." je autorský pokyn
       k přednesu, ne útržek — autor si o tu pauzu řekl sám. Bez téhle
       výjimky spadla celá S16 šestého videa („The car... red. The car...
       old. The car... enormous.") do JEDNÉ věty a nedostala ani jednu
       větnou pauzu: divák slyšel „red. The car" slitě, jako by tam tečka
       nebyla. Výpustkové pauzy to nezachrání — ty sedí UVNITŘ vět, ne mezi
       nimi. Naměřeno: dotýká se to 2 scén ze 457 napříč všemi videi,
       obou v šestém, takže starší videa se nemění.
    3. **Uvozovka za tečkou větu neruší.** `simple?"` končí uvozovkou, takže
       se pohled na dva znaky zpět netrefil a celá S79 třetího videa platila
       za JEDNU větu — nedostala pauzy a scene_audio se kvůli tomu vrátila
       dřív, než stihla uříznout obětovaný dovětek. Ten pak zůstal
       v nahrávce. Zavírací uvozovka i závorka se proto přeskakují.
    """
    out = []
    for p in re.split(r"""(?<=[^.?!][.?!])['"\u201d\u2019)\]]?\s+""", text.strip()):
        if not p:
            continue
        vypustka = "..." in p or "\u2026" in p
        if out and len(p.split()) < min_words and not vypustka:
            out[-1] = out[-1] + " " + p
        else:
            out.append(p)
    return out


def run(cmd, **kw):
    r = subprocess.run(cmd, capture_output=True, text=True, **kw)
    if r.returncode != 0:
        print(" ".join(str(c) for c in cmd[:12]) + " ...", file=sys.stderr)
        print(r.stderr[-2500:], file=sys.stderr)
        sys.exit(f"CHYBA: příkaz selhal ({cmd[0]})")
    return r.stdout


def duration(path: Path) -> float:
    return float(run(["ffprobe", "-v", "error", "-show_entries", "format=duration",
                      "-of", "csv=p=0", str(path)]).strip())


def video_dir(argv):
    if len(argv) > 1:
        return Path(argv[1]).resolve()
    vids = sorted((ROOT / "videos").iterdir())
    if len(vids) != 1:
        sys.exit("Zadej adresář videa: tools/<skript>.py videos/<slug>")
    return vids[0]


def timing_path(vd: Path, pripona: str = ""):
    """Kde leží rozpis „od kdy do kdy který vizuál".

    Mluvené video ho dostane z `tts.py` (work/timing.json), hudební
    z `analyze.py` (work/audio.json). Tvar je schválně TENTÝŽ, takže
    `render.py` nemusí vědět, odkud řezy přišly — z řeči, nebo z harmonie.

    `pripona` je přípona adresáře pro DRUHOU audiostopu (`-us` -> `work-us`), aby
    americká stopa nepřepsala tu, ze které vznikl nahraný master.
    Výchozí prázdná hodnota nechává chování beze změny.
    """
    proj = vd / "project.json"
    if proj.exists():
        kind = json.loads(proj.read_text(encoding="utf-8")).get("kind")
        if kind == "music":
            return vd / f"work{pripona}" / "audio.json"
    return vd / f"work{pripona}" / "timing.json"


def zvuk(p: Path) -> Path:
    """Zvukový soubor bez ohledu na příponu: nejdřív `.flac`, pak `.wav`.

    Pipeline od 2026-09-16 zapisuje FLAC. Je to TOTÉŽ PCM 16 bit — všech
    12 110 wavů v repu bylo `pcm_s16le`, takže se nic nepřevzorkovává
    a převod je bit po bitu shodný (ověřeno round-tripem přes soundfile
    i ffmpegem). Velikost klesne na ~55 % u řeči a na 29 % u podkresu,
    protože ten je ze sinusovek a lineární predikce si s ním poradí.

    Starší videa mají na disku `.wav` a přegenerovávat je není proč —
    proto ten fallback. Vzor je převzatý z `analyze.py` a `visualizer.py`,
    kde takhle od začátku funguje `track.flac` / `track.wav`.

    Vrací `.flac` i tehdy, když nic neexistuje: je to cesta pro ZÁPIS.
    Volající, kterému jde o čtení, si existenci ověří sám — chybějící
    soubor má každý nástroj hlásit vlastní hláškou, ne přes `FileNotFound`.
    """
    for pripona in (".flac", ".wav"):
        kandidat = p.with_suffix(pripona)
        if kandidat.exists():
            return kandidat
    return p.with_suffix(".flac")


def zvuk_pro_zapis(p: Path) -> Path:
    """Kam zapsat zvuk: vždy `.flac` — a starý `.wav` u toho uklidí.

    Bez toho úklidu by po přegenerování ležely na disku oba soubory.
    `zvuk()` sice dá přednost flacu, takže by se použil ten správný, jenže
    wav by tiše zabíral místo a při pohledu do adresáře by nebylo poznat,
    který z nich je ten platný.
    """
    novy = p.with_suffix(".flac")
    stary = p.with_suffix(".wav")
    if stary.exists() and stary != novy:
        stary.unlink()
    return novy
