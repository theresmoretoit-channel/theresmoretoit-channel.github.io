# YouTube — 033 Linux: You Probably Use It Already

Nahrává se `render/final-en.mp4` (master, ne draft), `render/thumbnail.jpg`
a `subtitles/*.srt` v devíti jazycích.

## 1. Titul

```
Linux — You Probably Use It Already
```

**Alternativy k rozhodnutí.** Titul a náhled rozhodují o stotřicetkrát
víc divácích než úvod videa, takže tohle není kosmetika:

| varianta | co dělá |
|---|---|
| `Linux — You Probably Use It Already` | dodal uživatel; tvrzení o divákovi, ne o Linuxu |
| `You've Already Used Linux Today` | ostřejší, osobnější, kratší |
| `Linux Has Run On Two Planets` | vede pointou videa; nejsilnější zvědavost, ale prozrazuje závěr |

## 2. Popis

```
If you're not a programmer, you probably think Linux is a black terminal
full of text. So here's a better question: where does Linux actually run?

It started in 1991 as one student's hobby project. Today it's in your
phone, your router, your television, the servers behind most of the web,
all five hundred of the world's most powerful supercomputers — and on
the flight computer of a helicopter that flew on Mars.

Linux isn't really one operating system. It's a kernel: a building block
you can wrap almost anything around. That's why it turns up in places
that seem completely unrelated — and why you've almost certainly used it
without ever choosing to.

CHAPTERS
0:00 The stereotype
0:48 1991: a hobby project
2:00 What Linux actually is
2:54 Your phone
3:28 Your router
3:59 Your television
4:26 The internet
5:11 Supercomputers
6:03 Things that move
6:49 Space — and Mars
7:55 So what is Linux?
8:24 Do you use Linux?

Subtitles are written for this video, not auto-generated. An American
English audio track is available as a second audio track.

SOURCES FOR THE NUMBERS
Kernel 7.2 development statistics — LWN.net
TOP500 operating system family statistics — top500.org
Android active devices — Google, The Android Show: I/O Edition, May 2025
Ingenuity flight count and Linux flight software — NASA / JPL
ISS laptops moved to Debian in 2013 — United Space Alliance

IMAGE CREDITS
LinuxCon Europe Linus Torvalds 03 (cropped) — Krd (photo), Von Sprat
(crop), CC BY-SA 4.0
via Wikimedia Commons
Licence: creativecommons.org/licenses/by-sa/4.0

Earth limb seen from STS-32 courtesy NASA/JSC.
Mars surface and Ingenuity images courtesy NASA/JPL-Caltech/ASU/MSSS.
All other archive images are in the public domain.

Music, diagrams and animation made for this video.
```

## 3. Tagy

```
linux, linux kernel, open source, android, torvalds, supercomputer,
top500, embedded linux, ingenuity, mars helicopter, iss, operating system,
how linux works, where linux runs, tech explainer
```

## 4. Nastavení

| pole | hodnota |
|---|---|
| jazyk videa | **`en-gb`** — nastavit NAPŘED, jinak zůstane dlaždice Titulky zašedlá |
| kategorie | Science & Technology |
| pro děti | ne |
| **byla použita AI** | **ne** — posílá `nahraj.py` jako `containsSyntheticMedia: false` |
| **osvědčení o zproštění** | ✅ **ručně ve Studiu**, API na to pole nemá |
| **závěrečná obrazovka** | ✅ **ručně ve Studiu**, API na to nemá ani zdroj |
| playlist | `legacy` (video už je v `playlisty.json`) |

## Proč je odpověď na „byla použita AI" NE

- **SDXL scény jsou 4 z 95** a díky kotvě stylu jsou to malované
  ilustrace, ne fotorealismus.
- **Archivní snímky jsou 4** a upravené jen barevně — „color adjustment
  or lighting filters" je výslovná výjimka v pravidlech YouTube.
- **Hudba je procedurální** (sinusovky a šum v numpy), ne z generativního
  modelu.
- Zbylých **86 scén je kreslených kódem**.

## Postup nahrání

Výchozí cesta je **ruční nahrání MP4 ve Studiu + `--k-videu`**, ne
`videos.insert` — ušetří 1 600 jednotek kvóty a průvodce ve Studiu se
sám zeptá na prohlášení o AI i na osvědčení o zproštění.

```bash
# 1) MP4 přetáhnout do Studia, zjistit ID
python tools/nahraj.py videos/033-you-probably-use-linux-already --k-videu <ID>
python tools/lokalizace.py videos/033-you-probably-use-linux-already
python tools/titulky.py --vse --smaz-asr      # automatický přepis konkuruje našim devíti
```

Po zveřejnění: doplnit číslo **33** a odkaz do `Témata.ods`, pustit
`tools/analytics.py --videa` a `tools/playlisty.py`.

> **Nahrát napřed neveřejně a podívat se na to v přehrávači.** YouTube
> video překóduje a jak po jejich kompresi vyjdou tmavé scény, se
> na disku posoudit nedá — a tohle video je tmavé skoro celé.
