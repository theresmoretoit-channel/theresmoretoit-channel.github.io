# Podklady k nahrání na YouTube

Osmé video kanálu **There's More To It**. Soubory:

| co | odkud |
|---|---|
| video | `render/final-en.mp4` (13:02, 85,4 MB, −14,0 LUFS / −0,8 dBTP) |
| náhled | `render/thumbnail.jpg` — koncept c1 IS NOW REAL?, 1280×720, 72 kB |
| titulky | `subtitles/*.srt`, devět jazyků |

---

## Titul

```
What Is Time, Actually?
```

## Popis

```
We have clocks. We have calendars. We know what time it is. So why does the
question "what is time?" fall apart the moment you look at it properly?

This video is about telling two things apart: time itself, and our feeling
that time flows. That one distinction runs from ordinary clocks to Einstein,
to entropy, to the brain — and to the question of whether there is any
objective "now" at all.

Along the way we run into something the second law does not actually solve.
Entropy explains why disorder keeps increasing. It does not explain why the
universe started out so extraordinarily ordered in the first place. That is
still open.

Full transcript, sources and translations: https://theresmoretoit-channel.github.io/videos/what-is-time-actually/

CHAPTERS
00:00 Two different things
00:43 What a clock actually measures
01:31 Newton's universal clock
01:59 Einstein and the speed of light
02:52 Spacetime and the end of 'now'
03:57 The block universe
04:37 The broken egg and entropy
05:23 But entropy does not rise everywhere
06:14 The laws do not know which way time runs
06:47 Why did the universe start so ordered?
07:47 Memory, and why the past feels different
08:43 Your 'now' is not a point
09:25 Why time flies and drags
10:09 So is time an illusion?
10:48 A whole life in spacetime
11:35 What is time, then?

A FEW THINGS WORTH SPELLING OUT

The block universe is an interpretation, not a result. Relativity makes it a
very natural reading of spacetime, but it does not prove it — Rietdijk and
Putnam argued for it, and Stein and others pushed back on the grounds that
"the present" in relativity is local, not a global slice.

Time-reversal symmetry is not exact. Most fundamental laws work almost the
same run backwards, and that "almost" is doing real work: CP violation showed
up in neutral kaons in 1964, and BaBar made the first direct observation of
T violation in the B-meson system in 2012.

The low-entropy beginning is a hypothesis, not a derivation. It is usually
called the Past Hypothesis, and it is contested — Carroll and Chen, and
Barbour and colleagues, have argued the arrow can come out of the dynamics
without postulating it.

And a subtlety about that beginning: the early universe was a hot, nearly
uniform plasma, and an equilibrium plasma has high entropy. What was low was
gravitational entropy — Penrose's Weyl curvature hypothesis. Smooth, not
tidy.

The satellite navigation figures: for a GPS orbit, special relativity slows
the onboard clock by about 7.2 microseconds a day and the weaker gravitational
potential speeds it up by about 45.7, for a net gain of about 38.4. Left
uncorrected, that is roughly eleven kilometres of position error per day.

IMAGE CREDITS
Isaac Newton — John Vanderbank, formerly attributed to Godfrey Kneller,
public domain, via Wikimedia Commons.
Albert Einstein — possibly Herman Mishkin, public domain, via Wikimedia
Commons.
Messier 17, the Omega Nebula — ESO/INAF-VST/OmegaCAM, acknowledgement
OmegaCen/Astro-WISE/Kapteyn Institute, CC BY 4.0.
Cosmic microwave background — NASA / WMAP Science Team, public domain.
Caesium atomic clock — ESO, CC BY 4.0.

Music is generated procedurally. Diagrams are drawn in code.

Subtitles are written for this video, not auto-generated. An American English
audio track is available as a second audio track.
```

## Tagy

```
time, what is time, physics of time, arrow of time, entropy, second law of
thermodynamics, special relativity, spacetime, block universe, relativity of
simultaneity, presentism, eternalism, past hypothesis, low entropy, time
perception, memory, predictive processing, philosophy of physics, popular
science, theres more to it
```

---

## Nastavení při nahrávání

| položka | hodnota |
|---|---|
| **jazyk videa** | **`en-gb`** — nastavit **jako první**, jinak zůstane dlaždice Titulky zašedlá |
| titulky | nahrát devět souborů ze `subtitles/` |
| kategorie | Věda a technika |
| **byla použita AI?** | **NE** — viz níž |
| pro děti | ne |
| viditelnost | **nejdřív neveřejné** a podívat se v přehrávači |

### Proč je odpověď na AI dotaz „ne"

Rozhoduje fotorealističnost, ne použití AI
([pravidla](https://support.google.com/youtube/answer/14328491)).

- **77 scén z 90 jsou diagramy kreslené kódem** — SVG, žádný model.
- **5 archivních snímků** je upraveno jen barevně, což je výslovná výjimka.
- **8 SDXL scén** je díky kotvě stylu malovaných, ne fotorealistických,
  a žádná nezobrazuje konkrétní skutečné místo ani událost.
- **Hudba je procedurální** (sinusovky a šum v numpy), ne z generativního
  modelu.
- Hlas je syntetický, ale **není to klon skutečné osoby**.

---

## Kontrola před nahráním

```bash
ffprobe -v error -show_entries format=duration -of default=nw=1:nk=1 \
        videos/008-what-is-time-actually/render/final-en.mp4      # 781.68
ffmpeg -v error -i videos/008-what-is-time-actually/render/final-en.mp4 -f null -
```

Druhý příkaz musí projít **beze slova**. Ověřeno 2026-08-29.

Poslední titulek končí v **780,43 s**, tedy 1,25 s před koncem videa —
u všech devíti jazyků.

## Thumbnail

Vybraný uživatelem: **`c1-is-now-real`** — ciferník rozříznutý svisle, obě
půlky posunuté proti sobě, každá s vlastní ručičkou a vlastní barvou. Je to
přímo obraz z S25 a S28: neexistuje univerzální teď. Text **IS NOW REAL?**

Zapsaný v `project.json` jako `thumbnail.overlay`, vyrobený do
`render/thumbnail.jpg` (1280×720, 72 kB; limit YouTube je 2 MB).

Na „Test & Compare" (YouTube umí až tři) zůstávají připravené
`render/thumb-c2-does-it-flow.jpg` a `render/thumb-c3-what-is-time.jpg`.

## Co ještě není

- **Závěrečná obrazovka a karty** jdou doplnit i po zveřejnění; teď už mají
  na co odkazovat, protože kanál má sedm starších videí.
