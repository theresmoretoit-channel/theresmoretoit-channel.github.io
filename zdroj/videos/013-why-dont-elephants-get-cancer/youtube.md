# Podklady k nahrání na YouTube

Třinácté video kanálu **There's More To It**.
**Master `render/final-en.mp4` je hotový:** 15:36, 1920×1080, 69,2 MB,
−14,1 LUFS / −1,1 dBTP, dekódovací test prošel beze slova.
Náhled `render/thumbnail.jpg` (1280×720, 58 kB) je vybraný koncept
`c1-two-or-twenty`.

---

## Titul

```
Why Don't Elephants Get Cancer?
```

Alternativy, kdyby se testovalo A/B:

```
Elephants Should Get More Cancer Than Us. They Don't.
The Elephant Paradox: 20 Copies of One Gene
```

## Popis

```
An elephant has vastly more cells than you do, and lives for decades.
Every one of those cells is another chance for cancer to start. So why
don't elephants get far more of it than we do?

That question is called Peto's paradox, and the most famous answer —
"elephants have twenty copies of TP53" — is true, popular, and not quite
what it sounds like. This video works through what a gene actually is,
what p53 does, why apoptosis matters, and what the evidence does and
doesn't show about those twenty copies.

Along the way: the zombie gene, why we can't simply turn our own p53 up
to maximum, and what elephant MDM2 is doing in human cells.

CHAPTERS
00:00 Thirty trillion chances to go wrong
00:46 The elephant problem
01:43 What a gene actually is
02:53 Meet p53
03:58 What happens when it fails
04:55 How many copies do we have?
05:27 About twenty, in the elephant
06:20 But there's a catch
07:00 Drift, not selection
07:51 The zombie gene
08:44 Elephants do get cancer
09:53 Why not just copy the elephant?
10:18 The balancing act
11:09 What people are already trying
12:12 Not only elephants
12:53 Cancer is evolution inside you
13:58 Could we become more like elephants?
14:38 The elephant changed the question

SOURCES
Abegglen et al., JAMA 314(17):1850-1860 (2015)
Sulak et al., eLife 5:e11994 (2016)
Vazquez et al., Cell Reports 24(7):1765-1776 (2018)
Nunney, Evolutionary Applications 15(6):891-901 (2022)
Preston et al., Cell Death Discovery (2023)
Palefsky et al., FASEB Journal 39(19) (2025)
Vincze et al., Nature 601:263-267 (2022)
Hatton et al., PNAS 120(39):e2303077120 (2023)

IMAGE CREDITS
African Bush Elephant, Amboseli NP - Ray in Manila, CC BY 2.0
African elephant side view portrait - Timothy Akolamazima, CC BY-SA 4.0
African Elephants herd crossing the road - Bernard DUPONT, CC BY-SA 2.0
Elephants at Amboseli against Mount Kilimanjaro - Amoghavarsha JS, CC BY-SA 3.0
Nacktmull (naked mole-rat) - Roman Klementschitz, CC BY-SA 3.0
via Wikimedia Commons

Subtitles are written for this video, not auto-generated. An American English
audio track is available as a second audio track.
```

## Nastavení při nahrávání

| pole | hodnota | pozn. |
|---|---|---|
| **jazyk videa** | `en-GB` | **nastavit PRVNÍ**, jinak zůstane dlaždice „Titulky" zašedlá |
| kategorie | Education | |
| **byla použita AI?** | **NE** | viz níž |
| pro děti | ne | |
| viditelnost | nejdřív **neveřejné** a přehrát si to | YouTube překóduje a tmavé scény se dopředu posoudit nedají |

### Proč „byla použita AI" = ne

Rozhoduje **fotorealističnost, ne použití AI**
([pravidla](https://support.google.com/youtube/answer/14328491)).

- **97 ze 105 scén jsou diagramy kreslené kódem** (SVG přes `diagrams/gen/`)
- 5 archivních fotografií, upravených jen barevně — *„color adjustment or
  lighting filters"* je výslovná výjimka
- 3 SDXL scény jsou díky kotvě stylu **malované ilustrace**, ne fotorealismus
- kreslený slon a postava v `art/` jsou ploché ilustrace, ne fotorealismus
  (podrobně `art/PUVOD.md`)
- hudba je **procedurální** (`tools/music.py`), ne z generativního modelu
- hlas je Kokoro `bf_emma`, tedy **nikoli klonovaný hlas skutečné osoby**

## Tagy

```
cancer, elephants, Peto's paradox, TP53, p53, LIF6, apoptosis, tumour
suppressor, evolution, genetics, biology, cancer research, MDM2,
naked mole rat, comparative oncology, science explained
```

## Soubory

| co | odkud |
|---|---|
| video | `render/final-en.mp4` — 15:36, 69,2 MB |
| náhled | `render/thumbnail.jpg` — 1280×720, 58 kB |
| titulky | `subtitles/*.srt`, devět jazyků |
| atribuce | `CREDITS.md` |

## Kontrola před nahráním

```bash
ffprobe -v error -show_entries format=duration -of default=nw=1:nk=1 \
        videos/013-why-dont-elephants-get-cancer/render/final-en.mp4
ffmpeg -v error -i videos/013-why-dont-elephants-get-cancer/render/final-en.mp4 \
       -f null -            # musí projít BEZE SLOVA
```

Náhled musí být do 2 MB a 1280×720.

---

## Co ještě chybí

**Nic.** Video je připravené k nahrání.

`c2-cells` a `c3-below-the-line` zůstávají v `render/thumb-*.jpg` jako
varianty pro „Test & Compare" — YouTube umí testovat až tři.

Závěrečná obrazovka a karty jdou přidat až po zveřejnění.
