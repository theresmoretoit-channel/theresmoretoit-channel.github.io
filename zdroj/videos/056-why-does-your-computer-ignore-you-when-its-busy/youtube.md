# Podklady k nahrání — 056

Video nahrál uživatel ručně ve Studiu; zbytek doplňuje
`nahraj.py --k-videu <ID>`. Postup a všechna pravidla jsou
v `docs/zverejneni.md` — **uživatel kopíruje jen text mezi trojicí
zpětných apostrofů pod nadpisem „Popis" a nic jiného**, takže co má být
na YouTube, musí být uvnitř toho bloku.

| | |
|---|---|
| ID videa | `RgqzoNF9OwU` |
| soubor | `render/final-en.mp4`, 9:37, 44,6 MB |
| náhled | `render/thumbnail.jpg`, 1280×720, 0,29 MB |

## Titul

```
Why Does Your Computer Ignore You When It's Busy?
```

> Wh-otázka schválně. Naměřeno na kanálu (29 videí, vážené impresemi):
> wh-otázka **2,23 %**, tvrzení 1,63 %, ano/ne otázka 1,21 %.

## Popis

```
You click a button. Nothing happens. You click again. Still nothing. And
then, five seconds later, everything arrives at once.

Here is the strange part: your computer knew. It knew within
microseconds. Right now, doing nothing in particular, your machine is
dealing with thousands of hardware events every second, and the mechanism
that makes that possible has been there since the 1950s.

So why does the click sit there?

This video is about the gap between being noticed and being served. It
turns out an interrupt gets the computer's attention, but it does not get
your program onto a processor — and the obvious fix, giving input the
highest priority, fails in a way that once reset a spacecraft on Mars.

Along the way: why a processor at one hundred percent does not mean
frozen, why the machine is often not slow but late, why the bottleneck is
sometimes memory rather than the processor, and why an application can go
pale and stop answering while the system around it is perfectly alive.

Chapters:
0:00 Click. Nothing happens.
1:18 What an interrupt actually is
2:11 The handler does as little as possible
2:52 First answer: attention is not a processor
3:04 So give input the highest priority
3:26 Mars, 1997
4:15 Priority inversion
4:37 High priority does not mean you get served
4:53 Priority does not create cycles
5:28 Not slow. Late.
5:50 When the processor is not the problem
6:33 The application that will not answer
7:31 And nothing has reached the screen yet
8:03 It has no idea why you moved the mouse
8:37 Your click was never one event

Subtitles are written for this video, not auto-generated. An American
English audio track is available as a second audio track.

IMAGE CREDITS
Mars Pathfinder Presidential Panorama — NASA, public domain
Pathfinder on Mars (PIA01120) — NASA/JPL, public domain
Mars Pathfinder Rover Team — NASA/JPL-Caltech, public domain

All other visuals are drawn from the project's own source files.
```

> **Věta o americké audiostopě tam JE od 2026-09-19**, kdy uživatel
> stopu nahrál ve Studiu. Do té doby chyběla schválně: z API ani ze
> souborů na disku se nepozná, jestli je stopa na videu — `render/
> audio-en-US.m4a` dokládá jen to, že se vyrobila. Znění se **nepřekládá
> znovu**, kopíruje se z posledního videa (tady 054), stejně jako CTA.

## Nastavení při nahrávání

| pole | hodnota |
|---|---|
| jazyk videa | **`en-GB`** — nastavit **NEJDŘÍV**, jinak zůstane dlaždice Titulky zašedlá |
| kategorie | Věda a technika |
| publikum | není určeno pro děti |
| prohlášení o AI | **ne** — SDXL scény jsou malované ilustrace (jen dvě z 91), archivní snímky jen barevně sjednocené, hudba procedurální |
| viditelnost | nejdřív **neveřejně**, podívat se na to v přehrávači, teprve pak zveřejnit |

## Tagy

```
computer, operating system, interrupt, scheduler, latency, cpu,
priority inversion, mars pathfinder, not responding, thrashing,
memory, responsiveness, kernel, explainer, how computers work
```

## Co musí uživatel naklikat sám

| | |
|---|---|
| prohlášení o AI | ✅ vyřídil průvodce při ručním nahrání |
| osvědčení o zproštění | ✅ vyřídil průvodce |
| **závěrečná obrazovka** | ❌ **ručně** — Data API na ni nemá ani zdroj |
| **americká audiostopa** | ✅ nahráno ve Studiu 2026-09-19 |

`zaver_check.py` hlásí u všech pěti scén v posledních dvaceti sekundách
(S85–S89) umístění s **nulovým** překryvem, takže dlaždice i kolečko se
vejdou kamkoli do horní poloviny.

## Nahráno 2026-09-19

| | |
|---|---|
| nastavení, popis, tagy, jazyk `en-GB` | ✅ |
| náhled | ✅ |
| **lokalizace — 13 jazyků + `en-GB`** | ✅ `lokalizace.py --id RgqzoNF9OwU` |
| **titulky — 15 stop** | ✅ `cs de en-GB en-US es fi fr id it pl pt-BR sv tr uk vi` |
| automatický přepis (asr) | ✅ smazán — po zveřejnění ho YouTube vyrobí znovu |
| **americká audiostopa + věta v popisu** | ✅ 2026-09-19, popis a 13 překladů přepsány |

Video je zatím **private**, takže `titulky.py` ani `analytics.py --videa`
na ně nedosáhnou (berou seznam z `analytics/videa.json`, kde jsou jen
zveřejněná videa). Titulky proto nahrál `nahraj.py --k-videu`.

## Po zveřejnění

Zveřejněno **2026-09-20 00:00 UTC**.

1. ✅ `analytics.py --videa` — 56 videí, 056 spárováno
2. ✅ `playlisty.py --jen bezne` — vloženo na pozici 11 playlistu
   *Ordinary Things, Awkward Questions* (50 jednotek)
3. ⏳ automatický přepis — uživatel ho smazal ručně ve Studiu a
   `captions.list` **potvrdil 15 stop `standard` a nula `asr`**
   (2026-09-20). Smazání ho ale **nezakáže**, takže si ho YouTube po
   zpracování vyrobí znovu: za pár hodin pusť
   `python tools/titulky.py videos/056-… --smaz-asr` (150 jednotek).
   `--vse` na to nepoužívej, to je 2 600 jednotek jen za čtení
4. řádek 56 do `Témata.ods`
