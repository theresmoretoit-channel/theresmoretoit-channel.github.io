# Podklady k nahrání na YouTube

Vše ověřeno proti `work/timing.json` a hotovému `render/final-en.mp4`
(10:30, 1920×1080, 43,7 MB, −14,0 LUFS / −1,2 dBTP).

## Titul

```
Why We May Not Be Able to Live Forever
```

Podtitul *„The Problem With the Brain"* z původního souboru **odříznut**:
v seznamu se za em-dashem stejně ořízne a prozrazuje pointu první třetiny.

## Popis

```
Imagine we could repair the human body — remove damaged cells, repair DNA,
rejuvenate mitochondria, even make some cells biologically young again.

So we would have solved ageing. Could we live forever?

Maybe not. A recent mathematical model asked what would be left if every
reversible cause of ageing were fixed, and landed on a median human lifespan
of about 156 years. The bottleneck it points to is not the body in general.
It is the tissue we cannot replace without replacing what it holds.

A heart is a pump. People have already lived with an artificial one that has
no pulse at all. A brain is the one place where replacing the part means
replacing the information — and that turns a question about biology into a
question about who you are.

Sources and the full fact check for every number in this video are in the
project notes; the key study is linked below.

Full transcript, sources and translations: https://theresmoretoit-channel.github.io/videos/why-we-may-not-live-forever/

— Chapters —
0:00 Could we solve ageing?
0:49 Why we age
1:57 What if we fixed all of it?
2:50 The one part we cannot swap
3:35 Damage that piles up in a neuron
4:10 Where 156 comes from
5:01 A heart is a pump. A brain is not.
5:56 What does repairing a brain even mean?
6:29 Replace every neuron, slowly
7:10 And what about a copy?
7:38 Healthspan, not lifespan
8:16 What age actually gives us
9:26 Where this leaves us

— Main source —
Efimov, Fedotov, Malaev, Khrameeva, Kriukov:
"Somatic mutations impose an entropic upper bound on human lifespan"
npj Aging 12, 116 (2026), open access
https://www.nature.com/articles/s41514-026-00421-6

Neuron count: Azevedo et al., J Comp Neurol (2009) — 86.1 ± 8.1 billion.
Pulseless artificial heart: Texas Heart Institute, March 2011; BiVACOR, 2025.

Subtitles are written for this video, not auto-generated. An American English
audio track is available as a second audio track. There's more to it.
```

## Nastavení

| co | hodnota |
|---|---|
| soubor | `render/final-en.mp4` — **master, ne draft** |
| náhled | `render/thumbnail.jpg` (1280×720, 91 kB) |
| **jazyk videa** | **`en-gb`** — nastavit PRVNÍ, jinak zůstane dlaždice Titulky zašedlá |
| titulky | `subtitles/*.srt`, devět jazyků |
| kategorie | Věda a technika |
| byla použita AI? | **ne** — viz níž |
| pro děti | ne |

## Titulky k nahrání

`en`, `cs`, `sv`, `es`, `pt-BR`, `de`, `fr`, `it`, `pl`

Kód jazyka je zároveň přípona souboru a musí odpovídat kódu, který zná
YouTube. Anglicky je `en-gb`, protože hlas je `bf_emma`.

## Odpověď na dotaz „byla použita AI"

**Ne**, a drží to tři věci:

1. **72 ze 79 scén jsou kreslené diagramy** (SVG generované kódem).
2. **Pět SDXL scén** je díky kotvě stylu **malovaná ilustrace**, ne
   fotorealismus — rozhoduje fotorealističnost, ne použití AI.
3. **Hudba je procedurální** (sinusovky a šum v numpy), ne z generativního
   modelu. Žádný klonovaný hlas skutečné osoby, žádná scéna zobrazující
   konkrétní skutečné místo nebo událost.

**Nula archivních snímků**, takže pro tohle video nevzniká licenční
evidence — `sources.json`, `CREDITS.md` ani `LICENSES.md` nemají obsah
a do popisku nepatří žádná atribuce.

## Tagy

```
ageing, aging, longevity, lifespan, healthspan, brain, neurons, identity,
ship of theseus, personal identity, biology, senescent cells, epigenetics,
artificial heart, science explainer, theres more to it
```

## Kontrola před nahráním

```bash
ffprobe -v error -show_entries format=duration -of default=nw=1:nk=1 \
        videos/010-why-we-may-not-live-forever/render/final-en.mp4      # 629.92
ffmpeg -v error -i .../final-en.mp4 -f null -                       # beze slova
```

Hotovo, obojí prošlo.

## Zbývá po zveřejnění

- **Nahraj jako neveřejné a podívej se na to v přehrávači.** YouTube video
  překóduje a jak vyjde tmavá scéna po jejich kompresi se dopředu posoudit
  nedá — je to jediný krok, který nejde udělat na disku.
- Závěrečná obrazovka a karty jdou přidat i po zveřejnění.
- `c2-all-but-one` a `c3-not-a-limit` leží v `render/thumb-*.jpg` jako
  varianty pro „Test & Compare".
