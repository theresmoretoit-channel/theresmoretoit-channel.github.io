# YouTube — 095 „How Would Passengers Land an Airliner?"

Stav: **nahráno 2026-10-08** (`dGkGpIkt68M`), zbývá jen ruční práce ve Studiu — master `render/final-en-095.mp4`
hotový (2026-10-08, render na 207, 1920×1080, 592,5 s, `ffmpeg -f null` bez chyb).
Pracovní kopie na 207 smazána po nahrání.

| | |
|---|---|
| ID videa | `dGkGpIkt68M` (https://www.youtube.com/watch?v=dGkGpIkt68M) |
| nastavení, popis, tagy | ✅ 2026-10-08 (`nahraj.py --k-videu --bez-titulku`) |
| náhled | ✅ nahrán; `render/thumbnail.jpg` z `thumbnail/chatgpt-no-pilots.png` (NO PILOTS / WHO LANDS IT?) |
| lokalizace | ✅ 13 jazyků (`lokalizace.py`) |
| automatický přepis | ✅ čisto (žádná asr stopa) |
| titulky | ✅ 15 stop přes API (14 jazyků + `en-US`) |
| playlist | ✅ `bezne`, pozice 20 |
| závěrečná obrazovka, americká stopa | ⬜ uživatel ve Studiu |

**Co musí uživatel naklikat sám:** nahrát MP4 ve Studiu (průvodce vyřídí
prohlášení o AI a osvědčení o zproštění), závěrečnou obrazovku a americkou
audiostopu (`render/audio-en-US.m4a`).

Soubor k nahrání: `render/final-en-095.mp4` (stopáž 9:52, `work/timing.json`
total 592,5 s).

> Kdyby se znovu pouštěl `tts.py`, přepočítej kapitoly tady
> i v `youtube-preklady.md` a přegeneruj `en-US` přes `us_stopa.py`.

Pořadí podle CENY (`docs/zverejneni.md`):

```bash
V=videos/095-how-would-passengers-land-an-airliner
python tools/nahraj.py $V --k-videu=<ID> --bez-titulku    # 100
python tools/analytics.py --videa                         #   1  ← nutné
python tools/lokalizace.py $V                             #  50
python tools/titulky.py $V --smaz-asr                     # 150  ← před titulky
python tools/titulky.py $V                                # 400×15
python tools/playlisty.py                                 #  50
```

---

## 1. Titul

```
How Would Passengers Land an Airliner?
```

> Wh-otázka, 38 znaků, totožná s nadpisem `script.md`. Nepředpokládá
> odpověď „dokázali by" — ptá se „jak", a video odpovídá „ne pilotováním,
> ale automatikou, a jen v nejlepším případě".

---

## 2. Popis

```
In September 2026, the co-pilot of a flydubai Boeing 737 attacked the captain with the cockpit's emergency axe. Passengers rushed in and overpowered him, and two of the airline's own pilots, sitting in the cabin, took over and landed the plane. But they were only on board because of a long detour.

So what if they hadn't been? In a 2023 survey, almost half of American men said they could land a passenger plane with only air traffic control to help. One airline pilot put their chances at almost zero. What would a cabin full of passengers actually have to do to get an airliner down?

Subtitles are written for this video, not auto-generated. An American English audio track is available as a second audio track.

Full transcript, sources and translations: https://theresmoretoit-channel.github.io/videos/how-would-passengers-land-an-airliner/

CHAPTERS
00:00 Dubai to Tel Aviv
00:54 Could you land it?
01:37 The door
02:03 Don't touch anything
02:33 When time runs out
03:08 The radio
03:36 A Cessna over Florida
04:24 Many hands
05:03 The instrument landing system
06:02 The best case
06:32 The simulator test
07:03 Runway or field?
07:58 Why not fly it from the ground?
08:23 Emergency Autoland
09:17 So, could passengers land it?

IMAGE CREDITS
FlyDubai, A6-FMA, Boeing 737-8 MAX — Anna Zvereva, CC BY-SA 2.0
Helios Airways Boeing 737-300 5B-DBY — Mila Daniel, CC BY-SA 4.0
Cessna 208 Caravan D-FNDA at Portimão Airport — Robbie Klinkenberg, CC BY 4.0
London Heathrow Instrument Landing System (ILS) — DaHuzyBru, CC BY-SA 4.0
US Airways Flight 1549 (N106US) on the Hudson River — Greg L, CC BY 2.0
Beechcraft 200 Super King Air — Pedro Aragão, CC BY-SA 3.0
Airbus A350-1000 F-WMIL — New York-air, CC BY-SA 4.0
via Wikimedia Commons
All other archive images are in the public domain.
Licences: creativecommons.org/licenses/by-sa/2.0, /by-sa/3.0, /by-sa/4.0, /by/2.0, /by/4.0
```

> **Blok se kopíruje CELÝ** (`docs/zverejneni.md`) — atribuce je UVNITŘ.
> Povinná u sedmi položek `sources.json` s licencí CC BY*: S06, S24, S32,
> S44, S62, S69, S71. S50 (Trident, Adrian Pingstone) je public domain.
>
> Kapitoly jsou ze scén S01, S09, S15, S19, S24, S28, S32, S38, S43, S55,
> S56d, S57, S64, S67, S73 (`work/timing.json`, zaokrouhleno dolů). Nejkratší
> kapitola je 25 s (S64 → S67), poslední 35 s; všechny ≥ 10 s, první na 00:00.
> Výzva k odběru S63b leží uvnitř kapitoly „Runway or field?".
>
> Popis neprozrazuje odpověď (autopilot, ILS, autoland, Emergency Autoland) —
> kapitoly ano, ale ty jsou až pod otázkou, stejně jako u 094. Fakta (záložní
> piloti flydubai posazení do kabiny kvůli objížďce, průzkum YouGov 2023,
> odhad pilota „almost zero") jsou ve `factcheck.md`.

---

## 3. Náhled

✅ **NO PILOTS / WHO LANDS IT?** — hotový obrázek od uživatele podle konceptu C1
(`thumbnail/chatgpt-no-pilots.png` → `render/thumbnail.jpg`), původ a otisk
v `thumbnail/PUVOD.md`. Kreslené koncepty v `thumbnail/KONCEPTY.md`.

---

## 4. Titulky

`subtitles/*.srt`, 14 jazyků + `en-US`. Jazyk videa **`en-gb`** (hlas
`bf_emma`) se musí nastavit dřív, než se nahrají titulkové stopy. Titulky
a lokalizace se nahrávají až po zapracování nálezů Codexu.

---

## 5. Nastavení

| | |
|---|---|
| kategorie | Science & Technology (alternativa Autos & Vehicles) |
| jazyk videa | `en-gb` |
| licence | standardní |
| pro děti | **ne** |
| komentáře | zapnuté |
| **byla použita AI** | **ne** (návrh, rozhoduje uživatel). 68 scén kreslených kódem, 8 archivních fotografií jen barevně upravených (*color adjustment* je výslovná výjimka), 4 SDXL scény díky kotvě stylu jako malované ilustrace, ne fotorealismus. Hudba procedurální, hlas není klon |

### Závěrečná obrazovka

`zaver_check.py` na masteru: S75–S79 OK (kresba do 2,5 %), takže závěrečná
obrazovka může být plných 20 s, **od 9:32**. Dlaždici i kolečko odběru do
**horní poloviny**, spodní rohy zabírá titulek. Dlaždice: návrh **079**
(*Why Is This 90-Year-Old Airplane Still Flying?*) — totéž letadlo, jiná otázka.

---

## 6. Tagy

```
airliner, passengers land a plane, could a passenger land a plane,
autoland, autopilot, instrument landing system, ILS, Emergency Autoland,
flydubai, Helios 522, Darren Harrison,
mayday, cockpit door, aviation safety, science explainer, there's more to it
```

---

## 7. Playlist

Navrženo **`bezne`** (*Ordinary Things, Awkward Questions*): otázka, kterou si
každý cestující v duchu položil. Alternativa `legacy` (je tam 079 o letadle),
ale tohle video není o starém systému. Dopiš slug do `playlisty.json`, spusť
`analytics.py --videa` a pak `tools/playlisty.py`.
