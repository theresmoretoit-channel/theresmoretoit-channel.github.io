# YouTube — 098 „Why Do Drones Fly on a Wire?"

Stav: **nahráno a naplánované ke zveřejnění** (`pj-1A4Bn9xM`, 2026-10-09). Hotovo. Master `render/final-en-098.mp4` hotový
(2026-10-09, render na 207, 1920×1080, 442,1 s, `ffmpeg -f null` bez chyb), náhled C2 hotový (`render/thumbnail.jpg`), titulky 14 jazyků + `en-US`
prošly Codexem.

| | |
|---|---|
| ID videa | `pj-1A4Bn9xM` (https://www.youtube.com/watch?v=pj-1A4Bn9xM), MP4 nahrál uživatel 2026-10-09 |
| nastavení, popis, tagy | ✅ 2026-10-09 (`nahraj.py --k-videu --bez-titulku`) |
| náhled | ✅ C2 20 KM / WHY A WIRE? |
| lokalizace | ✅ 13 jazyků + en (`lokalizace.py`) |
| automatický přepis | ✅ čisto (asr nebyl) |
| titulky | ✅ 15 stop — uživatel ručně ve Studiu (kvóta API došla) |
| playlist | ✅ `legacy` (uživatel ve Studiu) |
| závěrečná obrazovka, americká stopa | ✅ uživatel ve Studiu, video naplánované |

**Co musí uživatel naklikat sám:** nahrát MP4 ve Studiu (průvodce vyřídí
prohlášení o AI a osvědčení o zproštění), závěrečnou obrazovku a americkou
audiostopu (`render/audio-en-US.m4a`).

Soubor k nahrání: `render/final-en-098.mp4` (stopáž 7:22, `work/timing.json`
total 442,0 s).

> Kdyby se znovu pouštěl `tts.py`, přepočítej kapitoly tady
> i v `youtube-preklady.md` a přegeneruj `en-US` přes `us_stopa.py`.

Pořadí podle CENY (`docs/zverejneni.md`):

```bash
V=videos/098-why-do-drones-fly-on-a-wire
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
Why Do Drones Fly on a Wire?
```

> Wh-otázka, 28 znaků, totožná s nadpisem `script.md` (rozhodl uživatel
> u v0.1). Neprozrazuje odpověď (rušení). *Drag a 20 km Cable* by lhal —
> S20 říká, že se netáhne.

---

## 2. Popis

```
Some drones over Ukraine don't talk to their pilot by radio at all. Behind them, a strand of glass about as thin as a guitar string unwinds as they fly, and it can be 20 km long.

In the age of satellites and wireless everything, why would anyone fly a drone on a wire? How does a drone weighing a few kilograms manage kilometres of cable, what does a 1980s US Army missile have to do with it, and what happens to all the fiber left lying in the fields?

Subtitles are written for this video, not auto-generated. An American English audio track is available as a second audio track.

CHAPTERS
00:00 A drone on a thread
00:34 Ten thousand drones a month
01:15 Light instead of radio
01:43 Twenty kilometres of cable?
02:22 An old idea
02:57 What changed
03:27 More than one advantage
04:08 Why isn't every drone on a wire?
05:09 The thread points back
05:44 The problem moved
05:57 Fiber on the ground
06:27 A nest
06:57 A wire again

IMAGE CREDITS
UA fiber-optic FPV drone 01 and 02 — ArmyInform (АрміяІнформ), CC BY 4.0
via Wikimedia Commons
A Bird’s Nest Made of Fibre Optic Cable — National Museum of the History of Ukraine in the Second World War (War Museum, Kyiv), CC BY-NC-SA 4.0
via warmuseum.kyiv.ua
All other archive images are in the public domain.
Licences: creativecommons.org/licenses/by/4.0, creativecommons.org/licenses/by-nc-sa/4.0
```

> **Blok se kopíruje CELÝ** (`docs/zverejneni.md`). Povinná atribuce:
> S01 a S33 (АрміяІнформ, CC BY 4.0) a S69 (War Museum, CC BY-NC-SA 4.0,
> první NC snímek kanálu). S25 (TOW) je public domain.
>
> Kapitoly jsou ze scén S01, S08, S14, S18, S24, S29, S34, S41, S53, S60,
> S62, S67, S71 (`work/timing.json`, zaokrouhleno dolů). Nejkratší kapitola
> je 13 s (S60 → S62), poslední 25 s; všechny ≥ 10 s, první na 00:00.
> Výzva k odběru S23b leží v kapitole „Twenty kilometres of cable?".
>
> Popis ani kapitoly neříkají slovo *jamming* — to je odpověď na titul.
> `fiber` v metadatech podle rozhodnutí uživatele k v0.1, scénář a titulky
> zůstávají `fibre`. Fakta (20 km, tloušťka struny, armáda USA v 80. letech
> = FOG-M) jsou ve `factcheck.md`.

---

## 3. Náhled

✅ **20 KM / WHY A WIRE?** — C2 kreslený kódem (`thumbnail/c2-20-km.svg` →
`render/thumbnail.jpg`), koncepty v `thumbnail/KONCEPTY.md`.

---

## 4. Titulky

`subtitles/*.srt`, 14 jazyků + `en-US`. Jazyk videa **`en-gb`** (hlas
`bf_emma`) se musí nastavit dřív, než se nahrají titulkové stopy. Titulky
a lokalizace se nahrávají až po zapracování nálezů Codexu — **to je hotové**
(2026-10-09, všech 13 jazyků).

---

## 5. Nastavení

| | |
|---|---|
| kategorie | Science & Technology |
| jazyk videa | `en-gb` |
| licence | standardní |
| pro děti | **ne** |
| komentáře | zapnuté |
| **byla použita AI** | **ne** (návrh, rozhoduje uživatel). 68 scén kreslených kódem, 4 archivní fotografie jen barevně upravené (*color adjustment* je výslovná výjimka), S70 (sova) z SDXL malovaná, S55 a S65 hybrid SDXL pozadí + vlákna kódem — žádná nezobrazuje konkrétní skutečné místo ani událost. Hudba procedurální, hlas není klon |

> **S69 je CC BY-NC-SA** (neobchodní). Bez monetizace bez problému;
> kdyby se kanál monetizoval, stačí u tohoto videa monetizaci vypnout,
> nebo požádat muzeum o svolení (`info@warmuseum.kyiv.ua`). Reálné
> riziko je malé — vymáhat by to muselo muzeum samo.

### Závěrečná obrazovka

`zaver_check.py`: S71–S74 OK (kresba do 2,4 %), takže závěrečná obrazovka
může být plných 20 s, **od 7:02**. Dlaždici i kolečko odběru do **horní
poloviny**, spodní rohy zabírá titulek.

---

## 6. Tagy

```
drones, FPV drone, fiber-optic drone, fibre optic, optical fiber,
electronic warfare, jamming, drone jamming, Ukraine, war in Ukraine,
drone warfare, TOW missile, FOG-M, wire-guided missile, military technology,
birds nests, science explainer, there's more to it
```

---

## 7. Playlist

Navrženo **`legacy`** (*Legacy Tech — The Old Systems Still Running
Everything*): drát je technologie, kterou rádio mělo nahradit, a vrátila
se. Dopiš slug do `playlisty.json`, spusť `analytics.py --videa` a pak
`tools/playlisty.py`.
