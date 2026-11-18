# YouTube — 094 „Why Are Touchscreens in Cars So Dangerous?"

Stav: **připraveno k nahrání** — master `render/final-en-094.mp4` hotový
(2026-10-07, render na 207, 1920×1080, 576,5 s, `ffmpeg -f null` bez chyb).

| | |
|---|---|
| ID videa | `fQ-0rkJf6kQ` (https://www.youtube.com/watch?v=fQ-0rkJf6kQ) |
| nastavení, popis, tagy | ✅ 2026-10-07 (`nahraj.py --k-videu --bez-titulku`) |
| náhled | ✅ C1 (`thumbnail/c1-why-so-dangerous.svg`) → `render/thumbnail.jpg` |
| lokalizace | ✅ 13 jazyků (`lokalizace.py`) |
| automatický přepis | ✅ čisto (žádná asr stopa) |
| titulky | ✅ `en`, `en-US` (API); ⬜ 13 jazyků ručně ve Studiu (uživatel, kvóta) |
| playlist | ⬜ návrh `bezne` |
| závěrečná obrazovka, americká stopa | ⬜ uživatel ve Studiu |

**Co musí uživatel naklikat sám:** nahrát MP4 ve Studiu (průvodce vyřídí
prohlášení o AI a osvědčení o zproštění), závěrečnou obrazovku a americkou
audiostopu (`render/audio-en-US.m4a`).

Soubor k nahrání: `render/final-en-094.mp4` (stopáž 9:36, `work/timing.json`
total 576,5 s).

> **Po masteru:** SDXL scény mění jen obraz, ne zvuk ani časování, takže
> kapitoly, titulky a americká stopa zůstávají platné. Kdyby se ale znovu
> pouštěl `tts.py`, přepočítej kapitoly tady i v `youtube-preklady.md`
> a přegeneruj `en-US` přes `us_stopa.py`.

Pořadí podle CENY (`docs/zverejneni.md`):

```bash
V=videos/094-why-are-touchscreens-in-cars-so-dangerous
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
Why Are Touchscreens in Cars So Dangerous?
```

> Wh-otázka, 42 znaků, totožná s nadpisem `script.md`. Míra jistoty: video
> nedokládá vyšší nehodovost, nýbrž délku pohledů mimo silnici (factcheck);
> titul se ptá „proč", ne „o kolik", a odpověď video dává v mechanismu.

---

## 2. Popis

```
At 50 km/h, every second you look away from the road is fourteen metres. In an old car, you turn the temperature down without looking. In a modern car, you look at a screen, find the right menu, tap, and tap again.

Researchers have measured how long that takes. A Swedish car magazine timed the same simple jobs at 110 km/h: one car needed about ten seconds, another almost forty-five. So if carmakers know all this, why is almost every new car moving its controls onto a screen?

Subtitles are written for this video, not auto-generated. An American English audio track is available as a second audio track.

Full transcript, sources and translations: https://theresmoretoit-channel.github.io/videos/why-are-touchscreens-in-cars-so-dangerous/

CHAPTERS
00:00 A knob and a menu
01:06 It isn't the screen itself
02:13 How long can you look away?
02:49 Thirty cars, forty seconds
03:39 The Swedish test
04:36 Phones and voice control
05:31 Why carmakers do it
06:27 The showroom
07:05 Buttons come back
07:23 Euro NCAP 2026
07:53 What a good interface looks like
08:46 A car isn't a laptop
09:20 The price of a glance

IMAGE CREDITS
Tesla Model 3 interior — Coolomon Tetris (also known as CoolT), CC BY-SA 4.0
VolvoV70Instrumentpanelen — Patrik Nylin, CC BY-SA 4.0
Volkswagen ID.3 interior — Ssu, CC BY-SA 4.0
via Wikimedia Commons
All other archive images are in the public domain.
Licences: creativecommons.org/licenses/by-sa/4.0
```

> **Blok se kopíruje CELÝ** (`docs/zverejneni.md`) — atribuce je UVNITŘ.
> Povinná je u tří položek ze `sources.json` s licencí CC BY*: S10, S39, S71.
> S09 (nárazová zkouška, NHTSA VRTC) je public domain. Všechny čtyři záznamy
> v `sources.json` odpovídají archivním scénám storyboardu.
>
> Kapitoly jsou ze scén S01, S13, S25, S30, S38, S45, S54, S64, S70, S73,
> S78, S87, S93 (`work/timing.json`, časy zaokrouhlené dolů). Nejkratší
> kapitola je 16 s (S93 → konec), všechny ≥ 10 s, první na 00:00. Výzva
> k odběru S12b leží uvnitř první kapitoly.
>
> Popis vynechává odpověď (S44: rozhoduje rozhraní, ne stáří auta; S54–S69:
> proč to výrobci dělají) — jen ji položí jako otázku. Čísla (14 m za
> sekundu při 50 km/h, test Vi Bilägare při 110 km/h, ~10 s proti ~45 s)
> jsou ve `factcheck.md`.

> **Euro NCAP 2026 (S73–S77) je doložen sekundárními zdroji a citací
> Euro NCAP** (newmobility.news, Wapcar), samotný protokol *Safe Driving 2026*
> dohledán nebyl — rozhodnutí uživatele z `zpetna vazba 0.2.txt`. Na dotaz
> v komentářích odpovídat s tímhle zdrojem.

---

## 3. Náhled

✅ **C1** *TOUCHSCREENS / WHY SO DANGEROUS?* (`thumbnail/c1-why-so-dangerous.svg`, kresleno kódem `thumbnail/gen.py`) → `render/thumbnail.jpg`. Ostatní koncepty v `thumbnail/KONCEPTY.md`. Nic převzatého, takže `PUVOD.md` není potřeba.

---

## 4. Titulky

`subtitles/*.srt`, 14 jazyků + `en-US`. Jazyk videa **`en-gb`** (hlas
`bf_emma`) se musí nastavit dřív, než se nahrají titulkové stopy. Titulky
a lokalizace se nahrávají až po zapracování nálezů Codexu.

---

## 5. Nastavení

| | |
|---|---|
| kategorie | Autos & Vehicles (alternativa Science & Technology) |
| jazyk videa | `en-gb` |
| licence | standardní |
| pro děti | **ne** |
| komentáře | zapnuté |
| **byla použita AI** | **ne** (návrh, rozhoduje uživatel). 90 scén kreslených kódem, 4 archivní fotografie jen barevně upravené (*color adjustment* je výslovná výjimka), 4 SDXL scény (S21 stůl s počítačem, S64 autosalon, S66 noční dálnice, S92 silnice za čelním sklem) díky kotvě stylu jako malované ilustrace, ne fotorealismus, a žádná nezobrazuje konkrétní skutečné místo ani událost. Hudba procedurální, hlas není klon |

### Závěrečná obrazovka

`zaver_check.py` na masteru: S93–S96 OK (kresba do 3,4 %, kreslí jen do dolní
poloviny); **S92 (SDXL silnice, 9:15–9:20) má kresbu přes celý obraz** —
závěrečnou obrazovku proto nastav od **9:20** (začátek S93), tedy na posledních
16 s, ne na plných 20. Dlaždici i kolečko odběru dej do **horní poloviny**,
spodní rohy zabírá titulek. Dlaždice: návrh **089** (*Why Can You Still Buy
a Phone With a Keyboard?*) — týž argument hmatem.

---

## 6. Tagy

```
touchscreen, car touchscreen, car infotainment, driver distraction,
physical buttons, touchscreen vs buttons, Euro NCAP 2026, NHTSA,
AAA Foundation, Vi Bilägare, Volkswagen buttons, car interface design,
road safety, eyes off the road, voice control, science explainer,
there's more to it
```

---

## 7. Playlist

Navrženo **`bezne`** (*Ordinary Things, Awkward Questions*): obyčejný ovladač
v autě a nepohodlná otázka, proč ho nahradila obrazovka. Dopiš slug do
`playlisty.json`, spusť `analytics.py --videa` a pak `tools/playlisty.py`.
