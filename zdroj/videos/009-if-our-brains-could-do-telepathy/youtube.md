# Podklady k nahrání na YouTube

Deváté video kanálu **There's More To It**. Soubory:

| co | odkud |
|---|---|
| video | `render/final-en.mp4` (15:44, 69,8 MB, −14,0 LUFS / −1,1 dBTP) |
| náhled | `render/thumbnail.jpg` — koncept c1 NO RECEIVER, 1280×720, 78 kB |
| titulky | `subtitles/*.srt`, **devět jazyků** |

---

## Titul

```
If Our Brains Could Do Telepathy
```

## Popis

```
Nobody has ever reliably shown that a human brain can read another one. So
this video does not ask whether telepathy is real. It asks something more
useful: what would actually have to be different for it to work at all?

The answer turns out to be much bigger than "stronger brain waves". Your
brain really does produce electromagnetic activity — we can measure it with
electrodes on the scalp. But a transmitter with nobody able to receive it is
just a rock next to a radio. And even a perfect receiver would not help,
because a thought is not a signal: there is no single neuron in your head
that says "apple".

Work through it properly and telepathy stops being one ability and becomes an
entire communication system — a transmitter, a receiver, structure, a decoder,
a filter, and an address. That is not a change to one gene. That is a whole
new sense.

CHAPTERS
00:00 Two people, one thought
00:58 The brain already transmits
01:48 A transmitter with no receiver
02:27 A signal is not a thought
03:24 What a telepathic language needs
04:49 What if a brain had an aerial
05:38 Why would it ever evolve?
06:23 What water does to the idea
07:03 A million minds at once
07:46 Where do you even send a thought?
08:34 Telepathic privacy
09:18 The Trisolarans
10:05 Would an implant count?
11:21 It has already been done
12:27 A planet built on it
13:07 No such thing as a secret
13:47 Six things we would need
14:35 Would we still be individuals?

A FEW THINGS WORTH SPELLING OUT

Telepathy has not been demonstrated. Early meta-analyses of ganzfeld
experiments looked positive, but Milton and Wiseman (1999) failed to
replicate the effect across thirty later studies, and the field has a
documented sensitivity to questionable research practices.

Single neurons can be remarkably picky. Quian Quiroga and colleagues (2005)
found cells in the human medial temporal lobe that respond to one particular
person or place — the famous "Jennifer Aniston neuron". That is real, and it
does not contradict the video: the coding is sparse rather than
single-celled, and no one cell carries the whole concept.

Brain-to-brain communication has already been done, crudely and without
implants. Grau et al. (2014) sent the words "hola" and "ciao" from India to
France using EEG on one end and transcranial magnetic stimulation on the
other; the receiver only reported flashes of light and the word was
reconstructed afterwards by computer. Rao et al. (2014) built a direct
brain-to-brain interface, and BrainNet (Jiang et al. 2019) linked three
people over a Tetris-like task at one bit per turn.

Nature has an electromagnetic sense, but not a radio. Migratory birds
navigate by the Earth's magnetic field, most likely via a radical-pair
mechanism in cryptochrome. That is a sense for a static field, not for a
modulated signal — and no known organism communicates by radio.

The Trisolarans are used as a thought experiment about consequences, not as
a model of how telepathy would work. They come from Liu Cixin's trilogy
Remembrance of Earth's Past.

SOURCES AND CREDITS

EEG Recording Cap — Chris Hope, CC BY 2.0, via Wikimedia Commons
https://commons.wikimedia.org/wiki/File:EEG_Recording_Cap.jpg

Vintage Realtone Two-Band (AM-FM) 10-Transistor Radio — Joe Haupt,
CC BY-SA 2.0, via Wikimedia Commons

Vervet monkey (Chlorocebus pygerythrus), Lake Nakuru National Park —
Diego Delso, CC BY-SA 4.0, via Wikimedia Commons

Biofilms Found Near Underwater Fresh Water Springs in the Dead Sea (2012) —
Ionescu et al., CC BY 2.5, via Wikimedia Commons

Music is generated procedurally. Diagrams are drawn in code.

Subtitles are written for this video, not auto-generated. An American English
audio track is available as a second audio track.
```

---

## Tagy

```
telepathy, neuroscience, brain, evolution, communication, EEG, brain-computer
interface, BrainNet, science communication, thought experiment, speculative
biology, electromagnetism, Liu Cixin, Three-Body Problem, sensory systems
```

## Nastavení při nahrávání

| položka | hodnota |
|---|---|
| jazyk videa | **`en-gb`** — nastavit PRVNÍ, jinak zůstane dlaždice Titulky zašedlá |
| titulky | devět souborů, kód jazyka = přípona souboru: `en.srt` jako **`en-GB`**, dál `cs`, `sv`, `es`, `pt-BR`, `de`, `fr`, `it`, `pl` |
| kategorie | Science & Technology |
| náhled | `render/thumbnail.jpg` |
| **byla použita AI?** | **NE** — viz níž |
| pro děti | ne |

### Proč je odpověď na AI „ne"

Rozhoduje fotorealističnost, ne použití nástroje:

- **98 ze 107 scén jsou diagramy kreslené kódem** (SVG přes `tools/svgkit.py`).
- **5 scén je SDXL** a všechny jsou malované ilustrace v kotvě stylu, ne
  fotorealismus: místnost (S01), lovci (S40), město (S47), cizí planeta (S82),
  závěrečná krajina (S107). Žádná nezobrazuje konkrétní skutečné místo ani
  událost.
- **4 archivní snímky** jsou upravené jen barevně — *„color adjustment or
  lighting filters"* je výslovná výjimka v pravidlech YouTube.
- **Hudba je procedurální** (`tools/music.py`, sinusovky a šum v numpy),
  ne z generativního modelu.
- Hlas je Kokoro `bf_emma`, tedy **syntetický vypravěč, ne klon skutečné
  osoby**.

## Před nahráním zkontrolovat

```bash
ffprobe -v error -show_entries format=duration -of default=nw=1:nk=1 \
        videos/009-if-our-brains-could-do-telepathy/render/final-en.mp4
ffmpeg -v error -i videos/009-if-our-brains-could-do-telepathy/render/final-en.mp4 -f null -
```

- délka **943,96 s = 15:44**, dekódovací test projde beze slova ✅
- náhled do 2 MB, 1280×720 ✅ (78 kB)
- kapitol je osmnáct, první začíná na `00:00` a všechny jsou delší než 10 s ✅
- **nahrát jako neveřejné a podívat se na to v přehrávači** — YouTube video
  překóduje a jak vyjdou tmavé scény po jejich kompresi se dopředu posoudit nedá
