# Podklady k nahrání na YouTube

Časy kapitol **ověřené proti `work/timing.json`**, ne odhadnuté.
Nejkratší kapitola má 14 s (YouTube chce aspoň 10).

> **Kapitola „What does it mean to exist?" se ZÁMĚRNĚ vynechala.**
> Vycházela na 0:29 a další na 0:36, tedy sedm sekund — YouTube by
> kapitoly nezobrazil vůbec. Sloučena do úvodní.

> **Archivní snímky jsou dva, oba NASA** (S16 Slunce z SDO, S18
> Hubbleovo hluboké pole). Nejsou pod CC BY-SA, takže atribuce není
> právně vynucená, ale podmínky NASA říkají *„NASA should be
> acknowledged as the source"* — proto je kredit **uvnitř** bloku
> „Popis", ne pod ním.

---

## Titul

```
Does the Past Still Exist?
```

---

## Popis

**Kopíruje se CELÝ blok mezi apostrofy a nic jiného.**

```
Yesterday you woke up, had breakfast, talked to someone. None of that is
happening any more. But it happened. So where is yesterday now?

This is not a video about what time is. It is about a much narrower
question: if something is no longer happening, what does it mean to say
that it exists?

Everything we have of the past is a trace. A photograph is not the past —
it is an object sitting in the present that happens to carry information
about it. A fossil is not the dinosaur. Ash is not the tree. And most of
what has ever happened left nothing at all.

Then it gets stranger. You have never once seen anything in the present.
The Sun you see left eight minutes ago. A galaxy a billion light years
away is a billion years out of date. Even the screen in front of you is
a few nanoseconds old. The universe is saturated with information about
its own past — and information about the past still isn't the past.

Relativity makes it worse: there is no single universal "now" that the
whole universe shares. One answer to that is the block universe, where
your childhood is simply a different part of spacetime. But relativity
makes that idea attractive; it does not prove it. Philosophers have three
names for the alternatives — presentism, eternalism and the growing block
— and physics did not settle the argument. It made the argument harder.

And then one question pulls apart two ideas we normally keep glued
together. Imagine every record of yesterday is gone: no photographs, no
documents, no memory in any head, no physical trace down to the last
atom. Would yesterday have stopped existing? Or would it still have
happened?

Full transcript, sources and translations: https://theresmoretoit-channel.github.io/videos/does-the-past-still-exist/

Chapters
00:00 Where is yesterday?
00:36 A photograph is not the past
01:03 Fossils, ash, memory
01:17 Traces are thin
01:58 The Sun, eight minutes ago
02:13 A galaxy, a billion years ago
02:39 Even this room
03:15 There is no universal now
03:57 The block universe
04:40 Your childhood in spacetime
04:56 Relativity does not prove it
05:12 Presentism
05:32 Eternalism
05:52 The growing block
06:13 Physics made it harder
06:35 What are we claiming?
07:15 A question that pulls them apart
07:35 If every trace were gone
07:50 A conversation in the Bronze Age
08:07 Existence and evidence
08:23 So, does it?
08:49 They happened

IMAGE CREDITS
Image of the Sun from NASA's Solar Dynamics Observatory — NASA/GSFC/SDO
Hubble Deep Field — NASA/JPL/STScI Hubble Deep Field Team
Courtesy NASA. NASA does not endorse this video.

Subtitles are written for this video, not auto-generated. An American
English audio track is available as a second audio track.
```

---

## Tagy

```
time, philosophy of time, block universe, eternalism, presentism, growing block, relativity, simultaneity, spacetime, does the past exist, speed of light, astronomy, memory, evidence, metaphysics
```

---

## Nastavení

| položka | hodnota |
|---|---|
| jazyk videa | **`en-gb`** — nastavit PRVNÍ, jinak zůstane dlaždice Titulky zašedlá |
| kategorie | Věda a technika |
| viditelnost | neveřejné, pak podívat se v přehrávači, teprve pak zveřejnit |
| licence | standardní licence YouTube |
| **prohlášení o AI** | **ne** — viz níž |
| pro děti | ne |
| titulky | devět jazyků z `subtitles/*.srt` |
| lokalizace | osm jazyků z `youtube-preklady.md` přes `tools/lokalizace.py` |
| playlist | doplnit do `playlisty.json` a spustit `tools/playlisty.py` |
| **závěrečná obrazovka** | **ruční krok ve Studiu** — API na to nemá zdroj. `zaver_check.py` hlásí u S68–S73 volné místo v HORNÍ polovině, u všech šesti 0,0 % překryvu |

### Prohlášení o AI: odpověď je NE

Rozhoduje fotorealističnost, ne použití AI:

- 66 scén jsou **diagramy kreslené kódem** (Inkscape z SVG)
- 5 scén je SDXL, ale kotva stylu z nich dělá **malované ilustrace**,
  ne fotorealismus
- 2 scény jsou **archivní snímky NASA**, upravené jen barevně —
  *„color adjustment or lighting filters"* je výslovná výjimka pravidel
- hudba je **procedurální** (numpy), ne z generativního modelu
- hlas je Kokoro `bf_emma`, tedy syntéza, **ne klonovaný hlas skutečné
  osoby**

### Po nahrání

1. `python tools/titulky.py <ID> --smaz-asr` — automatický přepis od
   YouTube konkuruje devíti překladům a je z nich nejhorší
2. závěrečná obrazovka ručně
3. zapsat odkaz a stav do `Témata.ods`
