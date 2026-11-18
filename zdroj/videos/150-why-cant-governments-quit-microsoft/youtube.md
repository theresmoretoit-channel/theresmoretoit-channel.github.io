# YouTube — 150 „Why Can't Governments Quit Microsoft?“

Stav: **nahráno 2026-11-09** (https://youtu.be/L-WU6h0nTvg), zveřejnění naplánované, zbytek doklikán ve Studiu; zbývá `playlisty.py` po zveřejnění.

| | |
|---|---|
| ID videa | `L-WU6h0nTvg` |
| master | `render/final-en-150.mp4` (herní PC přes wifi, 632,6 s, 1920×1080, dekódováno bez chyby) |
| náhled | ✅ C1 `MICROSOFT / WHERE'S THE EXIT?`, `render/thumbnail.jpg` (`thumbnail/PUVOD.md`) |
| nastavení, popis, tagy | podklady níž |
| lokalizace | `youtube-preklady.md`, 13 jazyků, Codex A/B/C zapracován (`codex youtube-preklady.txt`) |
| titulky | `subtitles/<kód>.srt`, 14 jazyků + `en-US`, Codex v0.4 (cs, de) a v0.6 (11 jazyků) zapracován; id S01 *kepala jaksa* opraveno podle Codexu k lokalizacím |
| americká stopa | `render/audio-en-US.m4a`, ručně ve Studiu |
| závěrečná obrazovka | S67–S69, **horní polovina** (viz níž) |
| karty | žádné |
| playlist | `spolecnost` (*How Society Actually Runs*) |

**Co musí uživatel naklikat sám:** závěrečnou obrazovku, americkou audiostopu
(`render/audio-en-US.m4a`), titulky, které nejdou přes API, a osvědčení o zproštění, pokud ho nevyřídil průvodce nahráním.

Stopáž 10:32 (`work/timing.json` total 632,565 s).

> Kdyby se znovu pouštěl `tts.py`, přepočítej kapitoly tady i v `youtube-preklady.md`
> a přegeneruj `en-US` přes `us_stopa.py`.

Pořadí podle CENY (`docs/zverejneni.md`):

```bash
V=videos/150-why-cant-governments-quit-microsoft
python tools/nahraj.py $V --k-videu=<ID> --bez-titulku   # 100
python tools/analytics.py --videa                        #   1  ← nutné
python tools/lokalizace.py $V                            #  50
python tools/titulky.py $V --smaz-asr                    # 150  ← před titulky
python tools/titulky.py $V                               # 400×N
python tools/playlisty.py                                #  50
# úklid, až je MP4 na YouTube:
rm $V/render/draft*.mp4
ssh vrana@192.168.0.207 'rm -rf /home/vrana/temp/render-150-why-cant-governments-quit-microsoft'
```

---

## 1. Titul

```
Why Can't Governments Quit Microsoft?
```

> Wh-otázka, 37 znaků, shodná s `project.json`, schválená uživatelem (`zpetna vazba 0.1.txt`).
> Odpověď (*A government can rent its software. It shouldn't rent its ability to function.*, S68) titul neprozrazuje.

---

## 2. Popis

```
By May 2025, the chief prosecutor of the International Criminal Court had lost access to his email. Not because of a hack. The United States had put him under sanctions, and his email ran on Microsoft, an American company. Now scale that up to a whole country: tax offices, hospitals and police all depend on software from a handful of companies abroad. Governments know this, and they keep signing the contracts anyway. So why can't governments quit Microsoft?

This video goes through the Czech government's framework agreement for Microsoft products, why picking the software everyone already knows was the sensible decision, what vendor lock-in looks like inside a ministry, the British government's surprising advice on lock-in in the cloud, what the CLOUD Act means for data stored in Europe, what Microsoft France told the French Senate under oath, Munich's LiMux, Schleswig-Holstein's move to open source, and a simple test any government can run on itself.

Sources: Czech Ministry of the Interior, Central purchase of Microsoft products (2024); AP, Trump's sanctions on ICC's chief prosecutor have halted tribunal's work (May 2025); Executive Order 14203 (2025); The Register (October 2025, February 2026); European Parliament, European Software and Cyber Dependencies, PE 778.576 (2025); UK Government Digital Service, Managing technical lock-in in the cloud; 18 U.S.C. § 2713 (CLOUD Act); French Senate, commission of inquiry into public procurement, hearing of 10 June 2025; Land Schleswig-Holstein, press releases (December 2025, September 2026); Wikipedia: LiMux.

Subtitles are written for this video, not auto-generated. An American English audio track is available as a second audio track.

Full transcript, sources and translations: https://theresmoretoit-channel.github.io/videos/why-cant-governments-quit-microsoft/

CHAPTERS
00:00 The prosecutor who lost his email
00:43 Now scale that up
01:09 Fourteen billion crowns
01:50 Not just the Czechs
02:04 How did it get like this?
03:03 Why not just switch?
03:33 Vendor lock-in
04:24 The British government's advice
04:55 Back to The Hague
05:36 Buying versus renting
05:50 Where the data is stored
06:19 Under oath in the French Senate
07:01 Just install Linux!
07:38 Schleswig-Holstein
08:10 The court in The Hague, again
08:23 Open source isn't free
08:51 Digital sovereignty
09:20 A simple test
09:51 So what's the mistake?

IMAGE CREDITS
Letná, Ministry of the Interior — Gampe, CC BY-SA 4.0
The Hague International Criminal Court building seen from Maurits Kiekpad — Ymblanter, CC BY-SA 4.0
Le palais du Luxembourg, Paris — Luis Miguel Bugallo Sánchez (Lmbuga), CC BY-SA 4.0
LiMux desktop — Clemens Kleinfeld, GPL
via Wikimedia Commons
Licences: creativecommons.org/licenses/by-sa/4.0, gnu.org/licenses/gpl.html
```

> **Blok se kopíruje CELÝ** (`docs/zverejneni.md`). Kredity: všechny čtyři archivní snímky ze `sources.json`
> (S09, S35, S45 CC BY-SA 4.0, S50 GPL). S25 a S42 jsou SDXL, zbytek kreslený kódem.
>
> **Úvod drží opatrnost scénáře:** *had lost access* a *his email ran on Microsoft*, ne „Microsoft ho odpojil“
> (S04–S05: řetěz rozhodnutí je sporný). Věta o podpisu ve Washingtonu je zkrácená na sankce, aby popis nepřebíral
> pointu S02 doslova.
>
> **Pointa se neprozrazuje:** popis ani kapitoly neříkají S68 (*rent its ability to function*), co odpověděl
> ředitel Microsoft France (S47), ani že ICC přechází na openDesk (S54, kapitola je jen *The court in The Hague, again*).
>
> Kapitoly ze scén S01, S06, S09, S14, S15, S22, S26, S32, S35, S40, S42, S45, S49, S53, S54, S55, S58, S61, S65
> (`work/timing.json`, zaokrouhleno dolů). První na 00:00, všechny ≥ 10 s (nejkratší S54 → S55, 13 s;
> S14 → S15 a S40 → S42 po 14 s; poslední S65 → konec 41 s). Otázka do komentářů (S69) vlastní kapitolu nemá.
> Výzvy k odběru (za S14 a S57) leží uvnitř kapitol.
>
> **Zdroje:** primární a autoritativní z `factcheck.md` ([MV], [AP], [EO], [Reg25], [Reg26], [EP], [GDS], [2713],
> [Senát], [SH], [SH-Linux], [WP-LiMux]). Kurz ČNB je jen přepočet, v popisu není.

---

## 3. Náhled

C1 z `thumbnail/ZADANI.md` (ChatGPT): vládní budova se zazděným vchodem pod cedulí EXIT, `MICROSOFT / WHERE'S THE EXIT?`.
`render/thumbnail.jpg`, původ v `thumbnail/PUVOD.md`.

---

## 4. Titulky

`subtitles/<kód>.srt` pro 14 jazyků a `en-US` (`codex 0.4 <kód>.txt`, `codex 0.6 <kód>.txt`).
Jazyk videa **`en-gb`** (hlas `bf_emma`) nastaví `nahraj.py` dřív, než se nahrají titulkové stopy.

---

## 5. Nastavení

| | |
|---|---|
| kategorie | **Science & Technology** (28), posílá `nahraj.py` napevno |
| jazyk videa | `en-gb` |
| licence | standardní |
| pro děti | **ne** |
| komentáře | zapnuté (S69 je otázka do komentářů) |
| **byla použita AI** | **ne**. 65 ze 71 scén je kreslených kódem. Dvě SDXL scény (S25 úřad, S42 datové centrum) jsou díky kotvě stylu malované ilustrace, ne fotorealismus, a nezobrazují konkrétní skutečné místo ani událost. Čtyři archivní snímky z Commons (S09, S35, S45, S50) jsou upravené jen barevně. Hudba je procedurální, hlas není klon skutečné osoby. |

### Závěrečná obrazovka

Od **10:32 − 20 s = 10:12**, tedy S67–S69. `zaver_check` hlásí v obou dolních rozích titulek.
**Dlaždici i odběr dej do HORNÍ poloviny.** Jako dlaždici navrhuju **077 *What Makes a State a State?***
(stát jako stroj na zpracování informací, S16; tentýž playlist), druhou nechat na „nejlepší pro diváka“.
Alternativa: 033 *Linux — You Probably Use It Already* (navazuje na S49–S56).

---

## 6. Tagy

```
digital sovereignty, vendor lock-in, microsoft government, government it, why governments use microsoft,
international criminal court email, icc microsoft, us sanctions, cloud act, data sovereignty,
europe digital dependency, czech government microsoft contract, munich limux, schleswig-holstein open source,
opendesk, libreoffice, linux in government, open source government, there's more to it
```

---

## 7. Playlist

**`spolecnost`** (*How Society Actually Runs*), za 118, vedle 077 *What Makes a State a State?*
Dopsat slug do `playlisty.json` až po zveřejnění, pak `analytics.py --videa` a `playlisty.py`.
Pinterest shortů: nástěnka playlistu `spolecnost`.
