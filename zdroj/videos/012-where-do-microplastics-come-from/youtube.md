# Podklady k nahrání na YouTube

Dvanácté video kanálu **There's More To It**. Soubory:

| co | odkud |
|---|---|
| video | `render/final-en.mp4` (10:27, 69,4 MB, −14,05 LUFS / −1,35 dBTP) |
| náhled | `render/thumbnail.jpg` — koncept c2 NOT THE BOTTLE, 1280×720, 87 kB |
| titulky | `subtitles/*.srt`, **devět jazyků** |
| atribuce do popisu | `CREDITS.md` |

---

## Titul

```
Where Do Microplastics Come From?
```

## Popis

```
Ask most people where microplastics come from and they will say bottles,
bags, packaging, synthetic clothes. All of that is real. But one of the
largest sources of tiny plastic particles is something almost nobody
pictures: the tyres on your car.

Tyres wear out. We can literally watch the tread disappear. What we rarely
ask is where that missing material actually goes — because it does not
simply vanish. A car tyre is thought to lose something like a tenth to a
fifth of its own weight while it is used, which is roughly a kilogram per
tyre, scattered invisibly along every road you have ever driven. And there
are well over a billion vehicles on this planet.

This video follows that material: what a tyre is actually made of, why
scientists call the result "tyre and road wear particles" rather than
microplastics, what 6PPD-quinone has to do with dead salmon, where the
particles end up, and what Europe's Euro 7 rules really say — including the
table of tyre limits that is printed with every single value left blank.

Along the way: brake dust, non-exhaust emissions, a French system that
literally vacuums your brakes, and why electric cars fix part of this
problem but not the part that matters most.

CHAPTERS
0:00 What we picture when we hear microplastics
0:43 Tyres wear out — so where does it go?
1:26 What a tyre is actually made of
2:30 6PPD: the chemistry a tyre leaves behind
3:19 How much material is that, really?
4:24 Where the particles end up
4:52 Brakes, roads and non-exhaust emissions
5:37 Euro 7 and a vacuum cleaner for your brakes
7:07 Electric cars do not make it disappear
8:00 What can actually be done
8:48 What does it do to us?
9:32 Where did the missing material go?

There's more to it.

--- Sources and further reading ---

Regulation (EU) 2024/1257 (Euro 7), full text:
https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32024R1257

Kole et al. (2017), Wear and Tear of Tyres: A Stealthy Source of
Microplastics in the Environment, Int. J. Environ. Res. Public Health
14(10):1265 — https://doi.org/10.3390/ijerph14101265

Tian et al. (2021), A ubiquitous tire rubber-derived chemical induces
acute mortality in coho salmon, Science 371(6525):185-189 —
https://doi.org/10.1126/science.abd6951

OECD (2020), Workshop on Microplastics from Tyre Wear: Knowledge,
Mitigation Measures, and Policy Options

--- Image credits ---

Tyre tread — National Rural Knowledge Exchange (CC BY 2.0)
Coho salmon — USFWS (public domain)
Miami rush hour traffic, I-95 — B137 (CC0)
Front brakes — simonov (CC BY-SA 2.0)
Regulation (EU) 2024/1257, page 30 — European Union, eur-lex.europa.eu
  (reuse authorised, Commission Decision 2011/833/EU)
Road gully — Alan Stanton (CC BY-SA 2.0)
Central Square, Keene NH, 1920s — Keene Public Library and the Historical
  Society of Cheshire County (no known restrictions)
Bald tyre — PookieFugglestein (CC0)

All images via Wikimedia Commons except the regulation page, which is from
EUR-Lex. Colour grading applied; otherwise unmodified.

Subtitles are written for this video, not auto-generated. An American English
audio track is available as a second audio track.
```

## Kapitoly

**Jsou už uvnitř bloku popisu** (doplněno 2026-09-05 — do té doby
ležely jen tady, tedy MIMO blok, a na YouTube se proto nikdy nedostaly).
Ověřeno proti `work/timing.json`: první na `00:00`, dvanáct kapitol,
nejkratší 28 s (YouTube žádá aspoň tři a každou aspoň 10 s).

```
0:00 What we picture when we hear microplastics
0:43 Tyres wear out — so where does it go?
1:26 What a tyre is actually made of
2:30 6PPD: the chemistry a tyre leaves behind
3:19 How much material is that, really?
4:24 Where the particles end up
4:52 Brakes, roads and non-exhaust emissions
5:37 Euro 7 and a vacuum cleaner for your brakes
7:07 Electric cars do not make it disappear
8:00 What can actually be done
8:48 What does it do to us?
9:32 Where did the missing material go?
```

## Tagy

```
microplastics, tyre wear, tire wear particles, TRWP, 6PPD, 6PPD-quinone,
brake dust, non-exhaust emissions, Euro 7, road runoff, electric cars,
air pollution, environment, science explainer, pollution
```

## Nastavení při nahrávání

| položka | hodnota |
|---|---|
| **jazyk videa** | **`en-gb`** — nastavit PRVNÍ, jinak zůstane dlaždice Titulky zašedlá |
| kategorie | Věda a technika |
| **byla použita AI** | **NE** — viz níž |
| pro děti | ne |
| titulky | nahrát všech devět `.srt` |
| náhled | `render/thumbnail.jpg` |

### Proč je odpověď na AI „ne"

Rozhoduje fotorealističnost, ne použití AI. Ze 73 scén dělá model
**čtyři** (S01, S48, S60, S70) a všechny jsou malované, zamlžené
a bez konkrétního skutečného místa. Zbytek je **61 diagramů kreslených
kódem** a **8 archivních snímků** upravených jen barevně, což je
výslovná výjimka. Hudba je procedurální (`tools/music.py`), ne
z generativního modelu.

## Před nahráním zkontrolovat

```bash
ffmpeg -v error -i render/final-en.mp4 -f null -     # musí projít BEZE SLOVA
ffprobe -v error -show_entries format=duration -of default=nw=1:nk=1 \
        render/final-en.mp4
```

Naměřeno: dekódovací test projde beze slova, délka 627,32 s sedí
s `work/timing.json` (627,30 s) na 0,02 s, master renderován na herním
PC s 3× supersamplingem a bez značek scén.

**Nahraj jako neveřejné a podívej se na to v přehrávači.** YouTube video
překóduje a jak vyjdou tmavé diagramy po jejich kompresi se dopředu
posoudit nedá — je to jediný krok, který nejde udělat na disku.
