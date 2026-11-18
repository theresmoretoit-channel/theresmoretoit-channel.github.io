# Podklady k nahrání na YouTube

**Video:** `render/final-en.mp4` (master, ne draft)
**Náhled:** `render/thumbnail.jpg` — 1280×720, do 2 MB
**Titulky:** `subtitles/*.srt`, devět jazyků

> **Nejdřív nastav jazyk videa na `en-gb`**, jinak zůstane dlaždice
> „Titulky" zašedlá. Hlas je `bf_emma`, tedy britská angličtina.

---

## Titul

**Where Did Health Insurance Come From?**

Varianty, kdyby první nefungoval:

- Health Insurance Is Only 150 Years Old
- The Accident That Tied American Healthcare to Your Job

---

## Popis

```
For most of human history, if you got sick, you were basically on your own.

Public health insurance feels like something that must have always existed.
It hasn't. It is largely a product of the last hundred and fifty years, and
it was invented for a reason: industrial society created a new kind of
problem, where a person could be perfectly able to work and still have one
illness destroy their family's finances.

This is the story of how we got from Roman burial societies and medieval
guilds to Bismarck, Beveridge, and the strangest healthcare system in the
developed world.

Full transcript, sources and translations: https://theresmoretoit-channel.github.io/videos/where-did-health-insurance-come-from/

00:00 Why this feels normal
00:29 Europe around 1800
01:08 Rome, guilds and the common fund
01:56 The Industrial Revolution
02:48 Bismarck and the first compulsory system
04:10 How it spread across Europe
04:38 Beveridge and the National Health Service
05:33 And then there was America
06:42 Why American insurance is tied to your job
06:58 How that happened by accident
07:42 Six questions instead of one
08:16 Why the paths diverged
08:46 What insurance actually is

--

A few things the video says carefully, and the sources behind them:

Germany introduced compulsory sickness insurance in 1883 — five years after
the Anti-Socialist Law of 1878 banned socialist organisations. Workers paid
two thirds of the contribution, employers one third.

Austria followed in 1888 and Hungary in 1891; Britain's National Insurance
Act came in 1911. After the First World War Czechoslovakia inherited both
the Austrian and the Hungarian systems and unified them by the Act of
9 October 1924.

The Beveridge Report was published on 2 December 1942; the National Health
Service began on 5 July 1948.

American employer-sponsored insurance was largely an accident of wartime
wage controls: the War Labor Board ruled in 1943 that contributions to
insurance funds did not count as wages, and by the end of the war health
coverage had tripled. The tax treatment was codified in 1954.

Medicare covers mainly older Americans; Medicaid covers eligible low-income
people, with rules that vary by state. In 2025, 8.3 percent of Americans —
about 28 million people — had no health insurance at all (CDC/NHIS).

Full working notes and every claim checked one by one: see the pinned comment.

--

Subtitles are written for this video, not auto-generated. An American English
audio track is available as a second audio track.

Music is generated procedurally.

IMAGE CREDITS
Inscription collegium tibicinum, Musei Capitolini — Marie-Lan Nguyen, CC BY 2.5
via Wikimedia Commons
Licences: creativecommons.org/licenses/by/2.5
All other archive images are in the public domain.
```

---

## Kapitoly

Ověřené proti `work/timing.json`, ne odhadnuté. První začíná na `00:00`,
je jich třináct a nejkratší trvá 16 s — YouTube žádá aspoň tři a každou
nejméně 10 s.

| čas | scéna | kapitola |
|---|---|---|
| 00:00 | S01 | Why this feels normal |
| 00:29 | S06 | Europe around 1800 |
| 01:08 | S11 | Rome, guilds and the common fund |
| 01:56 | S16 | The Industrial Revolution |
| 02:48 | S22 | Bismarck and the first compulsory system |
| 04:10 | S33 | How it spread across Europe |
| 04:38 | S37 | Beveridge and the National Health Service |
| 05:33 | S45 | And then there was America |
| 06:42 | S54 | Why American insurance is tied to your job |
| 06:58 | S56 | How that happened by accident |
| 07:42 | S62 | Six questions instead of one |
| 08:16 | S66 | Why the paths diverged |
| 08:46 | S69 | What insurance actually is |

---

## Tagy

```
health insurance, history of healthcare, Bismarck, Beveridge, NHS,
National Health Service, Medicare, Medicaid, social insurance,
sickness funds, industrial revolution, welfare state, public health,
history explained, why healthcare is expensive, employer sponsored insurance
```

---

## Nastavení

| položka | hodnota |
|---|---|
| jazyk videa | **`en-gb`** — nastavit PRVNÍ, jinak jsou titulky zašedlé |
| kategorie | Education |
| pro děti | ne |
| **byla použita AI?** | **NE** — viz níž |
| viditelnost | nejdřív **neveřejné** a podívat se v přehrávači |

### Proč je odpověď na dotaz „byla použita AI" ne

Rozhoduje **fotorealističnost, ne použití AI**
([pravidla](https://support.google.com/youtube/answer/14328491)). U tohohle
videa to drží trojnásobně:

- **69 ze 79 scén jsou diagramy kreslené kódem** (SVG přes `diagrams/gen/`),
  tedy ne generovaný obraz vůbec
- **7 scén jsou archivní snímky**, upravené jen barevně a oříznuté —
  *„color adjustment or lighting filters"* je výslovná výjimka
- **3 scény jsou SDXL**, ale `sdxl.style` je kotvený na *painterly
  documentary illustration*, tedy malovanou ilustraci, ne fotorealismus
- **hudba je procedurální** (sinusovky a šum v numpy), ne z generativního
  modelu

Odpověď by se překlopila na ano, kdyby se přidal fotorealistický checkpoint,
hudba ze Suno/Udio nebo klonovaný hlas.

---

## Před nahráním zkontrolovat

```bash
# délka
ffprobe -v error -show_entries format=duration -of default=nw=1:nk=1 \
        videos/016-where-did-health-insurance-come-from/render/final-en.mp4

# dekódovací test — musí projít BEZE SLOVA
ffmpeg -v error -i videos/016-where-did-health-insurance-come-from/render/final-en.mp4 -f null -

# titulky proti délce videa
for f in videos/016-where-did-health-insurance-come-from/subtitles/*.srt; do
  echo -n "$(basename $f): "; tail -4 "$f" | head -1
done

# náhled do 2 MB
ls -la videos/016-where-did-health-insurance-come-from/render/thumbnail.jpg
```

**Nahrát jako neveřejné a podívat se na to v přehrávači.** Video je tmavé
(diagramy mají průměrný jas 17 z 255) a jak vyjde po překódování YouTube
se dopředu posoudit nedá. Je to jediný krok, který nejde udělat na disku.

Závěrečná obrazovka a karty jdou přidat i po zveřejnění.

---

## Připnutý komentář

```
A note on how this was made and checked.

Every number and date in this video was verified against a primary or
near-primary source before recording — 33 claims in all. Two of them
changed the script: Czechoslovakia inherited the Austro-Hungarian system,
not just the Austrian one, and the United States never *completely*
rejected public healthcare rather than never rejecting it.

Two things the video deliberately does NOT claim. It does not say the
anti-socialist law failed, although the socialist vote grew while it was in
force — that is an interpretation, and the video simply puts 1878 and 1883
side by side. And it does not put a number on how many Americans are
uninsured, because that figure moves every year and this video is meant to
last.

Bismarck defended his own law in the Reichstag on 9 May 1884: "Give the
worker the right to work as long as he is healthy, give him care when he is
sick, give him care when he is old... then I believe that the gentlemen of
the socialist party will blow their whistle in vain." It is a defence given
a year after the law, not a motive recorded before it — which is why it is
here and not in the video.
```
