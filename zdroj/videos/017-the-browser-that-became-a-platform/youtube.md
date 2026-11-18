# Podklady k nahrání na YouTube

Časy kapitol **ověřené proti `work/timing.json`**, ne odhadnuté.
Master render je HOTOV.

`render/final-en.mp4` — **14:07, 86 scén, −14,1 LUFS / −1,3 dBTP, 56,4 MB**,
1920×1080 při 25 fps, 3× supersampling, CRF 18. Dekódovací test projde
beze slova. Renderováno na herním PC za **12,4 minuty**.

> **Pozor: `render/draft-en.mp4` je ZASTARALÝ.** `render_remote.py` stahuje
> zpátky celý adresář `render/`, takže při běhu masteru přepsal lokálně
> vyrobený opravený draft starší kopií z herního PC. Master je správný
> a novější; draft se dá ignorovat, nebo smazat.

---

## Titul

```
Internet Explorer 6 — The Browser That Became a Platform
```

Alternativy, kdyby se v náhledu ukázaly jako lepší:

- `IE6 Was Right (And That's the Problem)`
- `The Browser Everyone Hated Was Trying to Tell Us Something`

## Popis

```
Open a perfectly reasonable web page in Netscape, in Opera, in the new
Firefox — fine. Open it in Internet Explorer 6 and the layout is wrong,
the buttons have moved, the PNGs look terrible, and somehow a single line
break has created a three pixel gap.

But IE6 wasn't simply a terrible browser. Microsoft was trying to solve
a real problem: in 2001 the web could display documents and not much else,
while companies wanted actual applications. ActiveX was an early, reckless,
and genuinely visionary answer — turn the browser into an application
platform. They were right about the destination and wrong about the route.

This is the story of how a browser became a platform, what it cost the
people who had to build for it, and why the ending should feel a little
too familiar: today almost every browser you can name runs on the same
engine.

Full transcript, sources and translations: https://theresmoretoit-channel.github.io/videos/the-browser-that-became-a-platform/

Chapters
00:00 Everything is broken
01:01 How Internet Explorer won
01:47 The web could barely do anything
02:15 So Microsoft invented ActiveX
03:02 Terrifying today, obvious then
03:42 Extending the web sideways
04:26 The box model
05:12 hasLayout and zoom: 1
05:59 Whitespace — and it wasn't IE's fault
06:39 The era of HTML hacks
07:04 When the browser simply died
07:40 Why developers used the hacks
08:29 Then came jQuery
09:06 The browser started learning
09:52 And then came Silverlight
10:29 The browser became the platform
10:57 So was Microsoft the villain?
11:35 History starts repeating itself
12:22 The difference between then and now
12:56 Was IE6 terrible? Yes. And?

Subtitles are written for this video, not auto-generated. An American
English audio track is available as a second audio track.

There's More To It
```

## Tagy

```
internet explorer, ie6, activex, web development, browser wars, css,
haslayout, quirks mode, box model, jquery, silverlight, chromium,
web standards, microsoft, netscape, web history, frontend, retro computing
```

## Nastavení při nahrávání

| položka | hodnota |
|---|---|
| jazyk videa | **`en-gb`** — hlas je `bf_emma`. Nastavit **DŘÍV** než titulky, jinak zůstane dlaždice „Titulky" zašedlá |
| titulky | `subtitles/*.srt` — **devět jazyků, hotové** |
| náhled | `render/thumbnail.jpg` (do 2 MB, 1280×720) |
| **byla použita AI** | **NE** — viz níž |
| kategorie | Věda a technika |
| publikum | není určeno dětem |

### Odpověď „byla použita AI" je NE a drží ji tři věci

1. **82 z 86 scén jsou diagramy kreslené kódem** (SVG přes Inkscape),
   ne generovaný obraz.
2. **Čtyři SDXL scény jsou malované ilustrace**, ne fotorealismus —
   drží to kotva stylu v `project.json`. Rozhoduje fotorealističnost,
   ne použití modelu ([pravidla YouTube](https://support.google.com/youtube/answer/14328491)).
3. **Hudba je procedurální** (sinusovky a šum v numpy, `tools/music.py`),
   ne z generativního modelu.

Žádná scéna nezobrazuje konkrétní skutečné místo ani událost a nikde není
klonovaný hlas skutečné osoby.

### Atribuce

**Žádná není potřeba** — video nemá jediný archivní snímek
(`sources.json`, `CREDITS.md` ani `LICENSES.md` proto neexistují).
Hudba je vlastní generovaná, bez licenčních vazeb.

Loga a značky se ve videu nekreslí. Okna prohlížečů mají obecnou ikonku
aplikace, ne cizí logo — záměrně, viz `diagrams/gen/_kit.py`.

---

## Před nahráním zkontrolovat

```bash
V=videos/017-the-browser-that-became-a-platform
# 1) master není rozsypaný — musí projít BEZE SLOVA
ffmpeg -v error -i $V/render/final-en.mp4 -f null -
# 2) délka
ffprobe -v error -show_entries format=duration -of default=nw=1:nk=1 \
        $V/render/final-en.mp4
# 3) titulky nepřesahují délku videa
for f in $V/subtitles/*.srt; do echo "$f $(tail -4 $f | head -1)"; done
# 4) náhled do 2 MB
ls -la $V/render/thumbnail.jpg
```

**Nahrát jako neveřejné a podívat se na to v přehrávači.** YouTube video
překóduje a jak vyjde tmavá scéna po jejich kompresi se dopředu posoudit
nedá — a tohle video je tmavé celé. Je to jediný krok, který nejde
udělat na disku.

## Thumbnail

Tři koncepty leží v `render/thumb-*.jpg`, porovnání v
`work/kontakt-thumbnaily.png`:

| koncept | objekt | text | paradox |
|---|---|---|---|
| `c1-ie6-was-right` | okno prohlížeče přerůstající stroj pod sebou | IE6 WAS RIGHT | jde proti tomu, co si divák myslí |
| `c2-zoom-one` | `zoom: 1;` a za ním rozvržení, které se srovná | IT FIXED EVERYTHING | řádek, který nic neznamená, spravil všechno |
| `c3-did-it-again` | jedno okno vlevo, pět vpravo — všechna na jedné liště | WE DID IT AGAIN | „pět" a „jedno" je totéž |

**Uživatel vybral `c1`** (s textem `IE6 WAS TERRIBLE` místo původního
`IE6 WAS RIGHT`). Volba je zapsaná v `project.json` a hotový soubor je
`render/thumbnail.jpg` — **1280×720, 66 kB**, tedy hluboko pod limitem 2 MB.
`c2` a `c3` zůstávají v `render/thumb-*.jpg` jako varianty pro
„Test & Compare".
