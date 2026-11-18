# Podklady k nahrání na YouTube

Vygenerováno k `render/final-en.mp4` (9:20). Časy kapitol ověřené proti
`work/timing.json`.

---

## Titul

```
The Gyroplane — The Helicopter That Isn't
```

## Popis

```
It has a big rotor on top. It takes off and lands in a surprisingly small
space. And if the engine quits in mid-air, it can still put itself down.

Sounds like a helicopter. It isn't — because the engine doesn't power the
rotor at all. The air does.

This video takes that apart: why a rotor spins when nothing drives it, why
the fuselage doesn't spin with it, why the machine can't hover, and why a
few of them can still leap off the ground without any run at all. Plus the
part most people get wrong — the gyroplane is thirteen years OLDER than the
practical helicopter, and it costs a fraction of one.

Full transcript, sources and translations: https://theresmoretoit-channel.github.io/videos/the-helicopter-that-isnt/

Chapters
00:00 The machine that looks like a helicopter
00:31 How a helicopter does it
00:57 A completely separate propeller
01:20 Why does the air spin the rotor?
02:26 What the free rotor costs
02:45 Why the fuselage doesn't spin
03:45 It can't hover
04:28 The jump takeoff
05:20 When the engine stops
06:07 But it isn't crash-proof
06:37 Older than the helicopter
07:21 Surprisingly affordable
08:18 So why doesn't everyone fly one?
08:56 Not a cheap helicopter — something else

Subtitles are written for this video, not auto-generated. An American English
audio track is available as a second audio track.


There's more to it.

IMAGE CREDITS
Autogyro МТО-Sport and photographer in flight — Aleksandr Markin, CC BY-SA 2.0
Gyrocopter 2010 — Felix König, CC BY 3.0
Cierva C.30 — Hugh Llewelyn, CC BY-SA 2.0
via Wikimedia Commons
Licences: creativecommons.org/licenses/by-sa/2.0 · creativecommons.org/licenses/by/3.0
All other archive images are in the public domain.
```


## Nastavení při nahrávání

| položka | hodnota |
|---|---|
| soubor | `render/final-en.mp4` |
| náhled | `render/thumbnail.jpg` — koncept **`c3-not-a-helicopter`**, 1280×720, 60 kB |
| **jazyk videa** | **`en-gb`** — nastavit PRVNÍ, jinak zůstane dlaždice „Titulky" zašedlá |
| titulky | `subtitles/*.srt`, devět jazyků |
| kategorie | Věda a technika |
| byla použita AI | **ne** — viz níž |
| pro děti | ne |

## Odpověď na dotaz „byla použita AI"

**Ne**, a drží to trojí:

- SDXL scény jsou díky kotvě stylu **malované ilustrace**, ne fotorealismus,
  a **žádná z nich nezobrazuje stroj** — jsou to krajiny a obloha
- archivní snímky jsou upravené jen barevně; *„color adjustment or lighting
  filters"* je výslovná výjimka pravidel
- hudba je **procedurální** (sinusovky a šum v numpy), ne z generativního modelu

Poměr zdrojů: **59 diagramů / 4 archivní / 4 SDXL**, tedy model dělá 6 % scén.

## Tagy

```
gyroplane, autogyro, gyrocopter, autorotation, rotorcraft, aviation,
how it works, helicopter, Juan de la Cierva, aerodynamics, flight,
engineering, science, explainer
```

## Před nahráním zkontrolovat

```bash
ffprobe -v error -show_entries format=duration -of default=nw=1:nk=1 \
        videos/014-the-helicopter-that-isnt/render/final-en.mp4
ffmpeg -v error -i videos/014-the-helicopter-that-isnt/render/final-en.mp4 -f null -
```

1. Dekódovací test musí projít **beze slova**.
2. Náhled do 2 MB, 1280×720.
3. **Nahrát jako neveřejné a podívat se na to v přehrávači** — YouTube video
   překóduje a jak vyjde tmavá scéna po jejich kompresi se dopředu posoudit
   nedá. Tohle video má tmavé pozadí u všech 59 diagramů, takže je to tady
   důležitější než jinde.

4. **Test & Compare** — YouTube umí porovnat až tři náhledy naráz.
   Připravené varianty leží v `render/thumb-c1-no-engine.jpg`
   a `render/thumb-c2-air-spins-it.jpg`.

Závěrečná obrazovka a karty jdou přidat i po zveřejnění.
