# YouTube — 160 „Why Is It So Hard to Bring a Rock Back from Mars?“

Stav: **hotovo a naplánováno** (2026-11-18). Přes API nastavení, popis, náhled, lokalizace 13, ASR smazán, titulky 10/15; zbytek (titulky tr, uk, vi, fi, en-US, playlist `vesmir`, karta S14 → 125, závěrečná obrazovka, US audiostopa) naklikal uživatel ručně.

| | |
|---|---|
| ID videa | `iHV62yZI8MY` (https://youtu.be/iHV62yZI8MY), MP4 nahrál uživatel ručně ve Studiu 2026-11-17 |
| master | `render/final-en-160.mp4` (herní PC, 3× supersampling, 665,84 s, 1920×1080, 77 MB, dekódováno bez chyby) |
| náhled | ✅ `render/thumbnail.jpg` (C1, ChatGPT, 1280×720, 0,39 MB), původ `thumbnail/PUVOD.md` |
| nastavení, popis, tagy | podklady níž |
| lokalizace | `youtube-preklady.md`, 13 jazyků |
| titulky | `subtitles/<kód>.srt`, 14 jazyků + `en-US`, Codex 0.6 ve všech 13 překladech |
| americká stopa | `render/audio-en-US.m4a` (k draftu 3, scénář v0.6), ručně ve Studiu |
| závěrečná obrazovka | S80–S83, **horní polovina** (viz níž) |
| karty | **jedna**, S14 → 125 (`nahraj.py` ji vypíše) |
| playlist | `vesmir` |

**Co musí uživatel naklikat sám:** závěrečnou obrazovku, **kartu**, americkou audiostopu
(`render/audio-en-US.m4a`) a osvědčení o zproštění, pokud ho nevyřídil průvodce nahráním.

Stopáž 11:06 (`work/timing.json` total 665,81 s).

> Kdyby se znovu pouštěl `tts.py`, přepočítej kapitoly a čas karty tady i v `youtube-preklady.md`
> a přegeneruj `en-US` přes `us_stopa.py`.

Pořadí podle CENY (`docs/zverejneni.md`):

```bash
V=videos/160-why-is-it-so-hard-to-bring-a-rock-back-from-mars
python tools/nahraj.py $V --k-videu=iHV62yZI8MY --bez-titulku   # 100
python tools/analytics.py --videa                        #   1  ← nutné
python tools/lokalizace.py $V                            #  50
python tools/titulky.py $V --smaz-asr                    # 150  ← před titulky
python tools/titulky.py $V                               # 400×N
python tools/playlisty.py                                #  50
# úklid, až je MP4 na YouTube:
rm $V/render/draft*.mp4
```

---

## 1. Titul

```
Why Is It So Hard to Bring a Rock Back from Mars?
```

> Wh-otázka, 49 znaků, shodná s `project.json`. Odpověď (řetěz strojů, z nichž každý musí vyjít
> napoprvé, a raketová rovnice) titul neprozrazuje.

---

## 2. Popis

```
On Mars, ten titanium tubes full of rock are lying exactly where NASA's Perseverance rover put them. One sample still on the rover holds a rock with "leopard spots", which scientists described in 2025 as a potential biosignature. To find out what it really is, the rock has to come to Earth. Apollo brought back about twenty-two kilograms of the Moon in 1969. So why did a plan to bring back less than half a kilogram from Mars grow to an estimated eleven billion dollars, and then lose its funding?

This video goes through what Mars's gravity does to the rocket equation, why everything that launches from Mars has to land there first, why meteorites from Mars can't answer the question, how NASA and ESA planned to catch a basketball-sized container in Mars orbit, what a single Starship would need and how far MOXIE's oxygen experiment is from a fuel factory, why the return capsule was designed to fall into the Utah desert without a parachute, and where things stand now, with a new NASA team and China's Tianwen-3.

Sources: NASA/JPL, Perseverance sample tubes and Sample Depot (PIA25738, PIA26643); J. A. Hurowitz et al., Nature (September 2025); NASA Mars Sample Return Independent Review Board reports (2020, 2023) and NASA statement on cost and schedule (April 2024); NASA, Mars Sample Return industry studies (June 2024); NASA, MOXIE results (2023); NASA NTRS, Earth Entry System drop tests (2024); D. S. McKay et al., Search for past life on Mars, Science 273, 924 (1996); CNSA, Tianwen-3 mission plan (April 2026); SpacePolicyOnline, NASA looking for new ways to return Perseverance samples (November 2026).

Subtitles are written for this video, not auto-generated. An American English audio track is available as a second audio track.

Full transcript, sources and translations: https://theresmoretoit-channel.github.io/videos/why-is-it-so-hard-to-bring-a-rock-back-from-mars/

CHAPTERS
00:00 Ten tubes on Mars
01:08 We've done this before
01:32 Mars is not the Moon
02:15 Everything has to land first
03:17 Is it worth it?
03:46 A meteorite has no address
04:29 Why bring them to Earth
05:11 NASA's plan
06:08 Catching a container in orbit
06:40 Eleven billion dollars
07:00 What if one ship did it all?
07:40 Making fuel on Mars
08:41 How do you bring them down?
09:43 Where things stand now
10:04 China's Tianwen-3

IMAGE CREDITS
Archive images: NASA/JPL-Caltech, NASA/JPL-Caltech/MSSS, NASA/JSC, NASA/JSC/Stanford University, NASA/ESA/JPL-Caltech, NASA/GSFC — public domain.
World map: Canuckguy, after the CIA World Factbook — public domain, via Wikimedia Commons.
```

> **Blok se kopíruje CELÝ** (`docs/zverejneni.md`). Kredity ze `sources.json` a `art/PUVOD.md`: všech
> devět archivních snímků je NASA (volné dílo US Government), mapa S32 je public domain. **Povinná
> atribuce CC BY tu není žádná**, jména jsou tam ze slušnosti. S19 je malovaná ilustrace z SDXL,
> 79 scén kresleno kódem.
>
> **Pointa se neprozrazuje:** popis ani kapitoly neříkají, že problém je řetěz předávek, z nichž
> každá musí vyjít napoprvé (S44–S46), ani že MOXIE je od továrny sedm milionů krát daleko (S61).
>
> Kapitoly ze scén S01, S09, S11, S17, S22, S27, S30, S34, S42, S48, S50, S56, S64, S73, S76
> (`work/timing.json`, zaokrouhleno dolů). První na 00:00, všechny ≥ 10 s (nejkratší S48 → S50 20 s
> a S73 → S76 20 s; poslední S76 → konec 61 s). Otázka do komentářů (S83) vlastní kapitolu nemá.
>
> **Zdroje:** primární z `factcheck-zaklad.md` a `factcheck.md`; u Hurowitze a MOXIE schválně bez ročníku
> a stran, protože rešerše je má jen z druhé ruky.

---

## 3. Náhled

**C1** z `thumbnail/ZADANI.md`: titanová trubička na rezavém písku, `MARS ROCK` / `WHY $11 BILLION?`.
Nakreslil ChatGPT, dodávka `render/thumbnail.jpg` (1280×720, 0,39 MB), původ a otisk v `thumbnail/PUVOD.md`.
`thumb_check`: jas 89,2, kontrast 93,7, ve 150 px čitelné. Nahraje ho `nahraj.py`.

---

## 4. Titulky

`subtitles/<kód>.srt` pro 14 jazyků a `en-US`.
Jazyk videa **`en-gb`** (hlas `bf_emma`) nastaví `nahraj.py` dřív, než se nahrají titulkové stopy.

---

## 5. Nastavení

| | |
|---|---|
| kategorie | **Science & Technology** (28), posílá `nahraj.py` napevno |
| jazyk videa | `en-gb` |
| licence | standardní |
| pro děti | **ne** |
| komentáře | zapnuté (S83 je otázka do komentářů) |
| **byla použita AI** | **ne**. 79 z 89 scén je kreslených kódem, devět jsou archivní snímky NASA upravené jen barevně (S01 je montáž NASA, ne naše). S19 (lander v prachové bouři) je malovaná ilustrace z SDXL, ne fotorealismus. Hudba je procedurální, hlas není klon skutečné osoby. |

### Karty

| čas | scéna | cíl |
|---|---|---|
| **~1:54** | S14 *If you've seen our video on getting to orbit* | 125 *Why Is Getting to Orbit So Hard?* (`IxISlshxSc8`) |

> Čas je ze začátku scény + ~2 s; přesný vypíše `nahraj.py` z `work/timing.json`.

### Závěrečná obrazovka

Od **11:06 − 20 s ≈ 10:46** (začátek S80 je 10:37). `zaver_check` hlásí S80, S82 a S83 OK, spodní
rohy jsou pod titulky. **Dlaždici i odběr dej do HORNÍ poloviny.**
Jako dlaždici navrhuju **125 *Why Is Getting to Orbit So Hard?*** (S14 na něj odkazuje a raketová
rovnice je jádro obou videí), druhou nechat na „nejlepší pro diváka“.

---

## 6. Tagy

```
mars sample return, perseverance rover, mars rock, nasa, esa, leopard spots, biosignature,
rocket equation, escape velocity, mars ascent vehicle, mars meteorite, alh84001, moxie,
starship, planetary protection, tianwen-3, space race, apollo samples, there's more to it
```

---

## 7. Playlist

**`vesmir`** (je v něm i 125). Dopsat slug do `playlisty.json`, `analytics.py --videa`,
`playlisty.py --jen vesmir`.
