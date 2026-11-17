# YouTube — 035 Can We Reach Another Star?

Nahrává se `render/final-en.mp4` (master, ne draft), `render/thumbnail.jpg`
a `subtitles/*.srt` v devíti jazycích.

## 1. Titul

```
Can We Reach Another Star With Today's Technology?
```

**Zveřejněno pod tímhle titulem** (49 znaků, dodaný ze zdrojového
podkladu) — rozhodl uživatel 2026-09-09, video je na
<https://www.youtube.com/watch?v=4waGk1NE9QY>. Můj návrh byl kratší
*„Can We Reach Another Star?"*; zapisuju obojí, protože kanál porovnává
CTR podle titulu a bez záznamu by se za půl roku nedalo poznat, která
varianta se měřila.

Zvažované varianty (návrh z doby před zveřejněním):

| varianta | znaků | co dělá |
|---|---|---|
| `Can We Reach Another Star?` | 26 | téma poznat okamžitě, otázka, nejbezpečnější |
| `Can We Reach Another Star With Today's Technology?` | 49 | dodaný titul; druhá půlka nepřidá zvědavost — **a přesto tenhle vyšel** |
| `The Hardest Part Isn't The Distance` | 34 | **slibuje obrat, který video opravdu má** (S86–S88), ale sám o sobě neřekne, o čem to je — nese to celé náhled |
| `We Could Send It. Could It Still Work?` | 37 | oblouk videa ve dvou větách; rizikovější, ale nejblíž tomu, o čem video je |

> **Pozn.:** kanál má CTR mezi videi rozdíl třicetinásobný a titul s náhledem
> stojí podle trychtýře stotřicetkrát víc diváků než úvod videa. Titul jde
> u zveřejněného videa vyměnit bez znovunahrávání, takže zbylé dvě varianty
> zůstávají otevřené jako materiál na spárované měření (viz „Metodika: jak
> se na kanálu měří změna výrobní linky" v CLAUDE.md).

## 2. Popis

```
Proxima Centauri is four and a quarter light-years away. We already know
how to send a spacecraft out of the Solar System and put it on a course
towards it — we have the rockets, the computers and the navigation. So
could we actually do it with today's technology?

Sort of. At Voyager 1's speed the trip takes about seventy-five thousand
years, and the problem stops being the distance. It becomes whether a
machine can still be working when it arrives. Everything humanity has
ever kept running — the Voyagers, at forty-nine years and counting — is
an invisible sliver of that journey. A plutonium-238 generator is down
to less than a thousandth of its output after a thousand years, and a
thousand years is barely one percent of the way.

Go faster and the problems change rather than disappear. A hundred-
gigawatt laser could push a gram-scale sail to a fifth of light speed
and cross the gap in twenty years — but nothing waits at the far end to
slow it down, the biggest dust grain out there arrives with the energy
of a rifle bullet, and the probe has to navigate itself because Earth is
four years away by radio.

Which leaves the question the whole thing is really about: can we build
a machine today that still knows what it's supposed to do when it gets
there?

CHAPTERS
0:00 The nearest star
0:56 How fast can we go?
1:35 Will it still work?
2:43 The computer
3:08 Running out of power
4:00 The laser idea
4:59 You can't slow down
5:50 Dust at a fifth of light speed
6:24 Navigating alone
7:31 Getting the data home
8:26 So can we?
9:08 The real problem is time
9:48 Make it sleep

Subtitles are written for this video, not auto-generated. An American English
audio track is available as a second audio track.

SOURCES
Lingam, M. et al. (2023). Calculations of Particle Bombardment due to
Dust and Charged Particles in the ISM on the Project Starshot Gram-Scale
Interstellar Probe. arXiv:2307.12160
Hoang, T., Lazarian, A., Burkhart, B. & Loeb, A. (2017). The Interaction
of Relativistic Spacecrafts with the Interstellar Medium. arXiv:1608.05284
Breakthrough Initiatives — Starshot: breakthroughinitiatives.org/concept/3
NASA Voyager mission status and power reports: science.nasa.gov/mission/voyager
UK electricity demand 2025: Digest of UK Energy Statistics, chapter 5

IMAGE CREDITS
Voyager 1 entering interstellar space (artist's concept) and the Cassini
radioisotope thermoelectric generator — NASA/JPL-Caltech and NASA/KSC.
Step Pyramid of Djoser — Archivio fotografico Museo Egizio, Turin, CC0.
Computer room — Warren K. Leffler, U.S. News & World Report collection,
public domain.
Licences: creativecommons.org/publicdomain/zero/1.0/
```

## 3. Tagy

```
interstellar travel, Proxima Centauri, Breakthrough Starshot, Voyager,
laser sail, light sail, RTG, plutonium-238, deep space, spacecraft
engineering, autonomous navigation, interstellar dust, space science,
astronomy, engineering
```

## 4. Nastavení

| co | hodnota | kdo to dělá |
|---|---|---|
| jazyk videa | `en-gb` | **napřed**, jinak zůstane dlaždice Titulky zašedlá |
| kategorie | Věda a technika | ručně |
| viditelnost | nejdřív **neveřejné**, podívat se v přehrávači | ručně |
| byla použita AI | **ne** | `nahraj.py` posílá `containsSyntheticMedia=false` |
| osvědčení o zproštění | zaškrtnout | **ručně ve Studiu**, API na to pole nemá |
| závěrečná obrazovka | dlaždice + kolečko odběru | **ručně ve Studiu**, API na to nemá ani zdroj |
| playlist | dopsat slug do `playlisty.json`, pak `analytics.py --videa` a `playlisty.py` | |

**Prohlášení o AI je „ne"** a u tohohle videa stojí na užší půdě než jinde,
protože **žádnou SDXL scénu nemá** — všech 102 scén je kresba kódem (98)
nebo archivní snímek (4). Difuzní model se tedy na obrazu nepodílí vůbec;
archivní snímky jsou upravené jen barevně (výslovná výjimka v pravidlech)
a hudba je procedurální (sinusovky a šum v numpy), ne z generativního
modelu. Náhled je fotorealistický obrázek zvenčí, ale ten do otázky
nespadá — ta se ptá na obsah videa (viz `thumbnail/PUVOD.md`).

## 5. Po nahrání

```bash
python tools/titulky.py --vse --smaz-asr    # automatický přepis konkuruje našim devíti
python tools/lokalizace.py videos/035-can-we-reach-another-star
python tools/playlisty.py
```

## 6. Stav po zveřejnění

Video vyšlo **2026-09-09** jako <https://www.youtube.com/watch?v=4waGk1NE9QY>;
uživatel nahrál MP4 i všechno ostatní ručně ve Studiu, takže `nahraj.py`,
`titulky.py` ani `lokalizace.py` neběžely.

**Zbývá a je to blokované kvótou** — `captions.list` vrátil `quotaExceeded`
(týž den se nahrávala ještě videa 036–038):

| co | příkaz | proč |
|---|---|---|
| smazat automatický přepis | `python tools/titulky.py --vse --smaz-asr` | konkuruje našim devíti překladům a je z nich nejhorší; **smazání ho nezakáže**, takže se to po každém nahrání opakuje |
| ověřit, co na videu doopravdy je | `python tools/titulky.py videos/035-can-we-reach-another-star --zkouska` | 9 titulkových stop a 8 lokalizací je zatím jen podle toho, co uživatel naklikal |
| playlist | `python tools/playlisty.py` | slug je v `playlisty.json` dopsaný do `fyzika` |
