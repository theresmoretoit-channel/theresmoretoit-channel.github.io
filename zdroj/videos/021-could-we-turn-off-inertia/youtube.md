# Podklady k nahrání na YouTube

Vyplněno podle `script 0.3.md` (70 scén) a `work/timing.json` (8:19).

---

## Titul

```
Could We Make Acceleration Impossible to Feel?
```

## Popis

```
A fighter pilot in a g-suit, straining against the force the whole time,
can take about nine times gravity — and only for tens of seconds. Without
the suit, a few times gravity is enough to drain the blood from your head.
So every vehicle that carries people is built around a very low limit. Not
the limit of the engine. The limit of the passenger.

What would we actually have to invent to remove it?

Moving your seat backwards while the vehicle accelerates works on paper,
until you do the arithmetic: one G for ten seconds needs a seat rail almost
half a kilometre long. Pushing the passenger directly just moves the
problem — something else has to take the reaction. We haven't eliminated
inertia. We are simply fighting it.

But there is one force you have never felt. Right now gravity is pulling
you towards the centre of the Earth, and you cannot feel a thing. A seat
pushes you in one place, and that push has to travel through your body —
your bones compress, your organs shift, and that is what you actually feel.
Gravity gives every part of you the same acceleration. Nothing is
compressed, so there is nothing to feel.

Which is exactly why a flight simulator tilts backwards instead of
accelerating: it borrows gravity to imitate a force it cannot produce.

With today's physics we cannot build an inertial damper. But if we ever
learn to manipulate inertia, gravity or spacetime, the question stops being
"how do we make the vehicle accelerate more gently?" and becomes "how do we
make the passengers not share that acceleration?" — and the hardest part of
interstellar travel might not be reaching a high speed, but surviving the
acceleration required to get there.

Full transcript, sources and translations: https://theresmoretoit-channel.github.io/videos/could-we-turn-off-inertia/

CHAPTERS
0:00 The question
0:24 Acceleration is a ceiling
1:02 What would we have to invent?
1:18 What you actually feel
1:45 Idea one: move the seat
1:59 What a flight simulator really does
2:39 The half-kilometre problem
3:19 Idea two: push the passenger
3:46 Inertia itself
4:28 A force you have never felt
4:59 Why gravity is different
5:44 Bending spacetime instead
6:25 What we cannot do
6:49 The verdict
7:16 Why it matters for the stars
7:46 The real question

SOURCES AND CREDITS
Archive images, all Wikimedia Commons:
· F-16 pilot in the cockpit, Misawa Air Base — U.S. Air Force photo by
  Airman 1st Class Kenna Jackson, public domain
· CAE CRJ-900 full flight simulator — Headphase, CC BY-SA 4.0
  https://creativecommons.org/licenses/by-sa/4.0
· NASA astronaut Nichole Ayers aboard the ISS — NASA Johnson Space Center,
  public domain

Gravitational waves from colliding black holes were first detected by LIGO
on 14 September 2015 (GW150914).

Subtitles are written for this video, not auto-generated. An American
English audio track is available as a second audio track.
```

> **Popis nesmí slíbit víc než video.** Inerciální tlumič je hypotéza,
> takže věta o něm stojí v podmiňovacím způsobu a graviton se v popisu
> nezmiňuje vůbec — ve videu jsou na něj jen dvě scény a nemá se z něj
> stát téma. Totéž hlídá `factcheck.md`.

## Tagy

```
acceleration, inertia, inertial damper, g-force, gravity, general relativity,
equivalence principle, free fall, spacetime, flight simulator, physics,
interstellar travel, graviton, science fiction, space travel
```

## Nastavení při nahrávání

| položka | hodnota | proč |
|---|---|---|
| soubor | `render/final-en.mp4` | **master, ne draft** |
| náhled | `render/thumbnail.jpg` | do 2 MB, 1280×720 |
| **jazyk videa** | **`en-gb`** | nastavit **jako první**, jinak zůstane dlaždice „Titulky" zašedlá. Hlas je `bf_emma`. |
| titulky | `subtitles/*.srt` | devět jazyků |
| **byla použita AI?** | **NE** | 64 diagramů kreslených kódem, 3 malované SDXL scény (kotva stylu, ne fotorealismus), 3 archivní snímky upravené jen barevně, hudba procedurální. Viz CLAUDE.md, „Označení AI obsahu". |
| kategorie | Science & Technology | |
| publikum | není určeno dětem | |

**Atribuce u S17 je povinná** — simulátor je CC BY-SA 4.0, takže jméno
autora i odkaz na licenci musí v popisu zůstat. Zbylé dva snímky jsou
public domain.

## Před nahráním zkontrolovat

```bash
ffmpeg -v error -i videos/021-could-we-turn-off-inertia/render/final-en.mp4 -f null -
ffprobe -v error -show_entries format=duration -of default=nw=1:nk=1 \
        videos/021-could-we-turn-off-inertia/render/final-en.mp4
ls -la videos/021-could-we-turn-off-inertia/render/thumbnail.jpg
```

**Nahrát jako neveřejné a podívat se na to v přehrávači.** YouTube video
překóduje a jak vyjde tmavá scéna po jejich kompresi, se dopředu posoudit
nedá — je to jediný krok, který nejde udělat na disku.

Kapitoly YouTube uzná: první začíná na `00:00` (S01 startuje na 0,4 s
kvůli `lead_in`, což se zobrazí jako 00:00), je jich šestnáct a nejkratší
trvá **13,7 s** — ověřeno proti `work/timing.json`.
