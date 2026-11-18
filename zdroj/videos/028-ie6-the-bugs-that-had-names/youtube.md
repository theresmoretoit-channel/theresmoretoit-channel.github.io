# Podklady k nahrání na YouTube

Časy kapitol **ověřené proti `work/timing.json`**, ne odhadnuté.
Master render je HOTOV.

`render/final-en.mp4` — **13:42, 86 scén, −14,1 LUFS / −1,2 dBTP, 51 MB**,
1920×1080 při 25 fps, 3× supersampling, CRF 18. Dekódovací test projde
beze slova.

> **Je to DRUHÝ DÍL.** V popisu i v prvních vteřinách videa je odkaz na
> `https://youtu.be/R7Un3IOMvbg` (017 — *The Browser That Became a
> Platform*). Ten odkaz musí v popisu být, jinak divák, který přijde
> na dvojku, nemá kam jít.

---

## Titul

```
Internet Explorer 6 — The Bugs That Had Names
```

---

## Popis

**Kopíruje se CELÝ blok mezi apostrofy a nic jiného.**

```
Normally a browser bug is a number in a tracker. Issue 4172. Nobody
remembers it, nobody talks about it at lunch.

In Internet Explorer 6 the bugs had proper nouns. Peekaboo. The Guillotine.
The Three Pixel Jog. The Duplicate Character Bug. And that turns out to be
the most telling thing about the whole era: you don't name a bug you meet
once.

This is part two. It's about what living inside that platform actually
meant — the named bugs, the invisible flag underneath most of them, the
hacks written to reach one browser, the fix that was a typo on purpose,
and the three words of HTML that could close a window on your own machine.

Part one, on how Internet Explorer 6 became a platform in the first place:
https://youtu.be/R7Un3IOMvbg

Full transcript, sources and translations: https://theresmoretoit-channel.github.io/videos/ie6-the-bugs-that-had-names/

Chapters
00:00 Part two
00:36 A bug with a number
00:57 The Three Pixel Jog
01:17 The Double Margin Bug
01:44 Peekaboo
02:10 The Guillotine
02:32 The Duplicate Character Bug
03:00 The Expanding Box
03:27 You don't name a bug you meet once
03:48 hasLayout
04:27 The Holly Hack
04:54 zoom: 1
05:14 Talking to one browser
05:54 The underscore hack
06:15 Conditional comments
06:45 Quirks mode
07:21 Transparency
07:59 Tables and the spacer gif
08:19 Hover, and a file next to the page
08:47 JavaScript in a stylesheet
09:04 Ceilings nobody else had
09:30 The memory leak
09:55 The missing equals sign
10:34 Out of the browser
11:12 One machine, one version
11:34 A library to patch the browser
11:48 What it cost
12:31 The funeral
12:48 One year later
13:12 Why the bugs had names

Every image in this video is drawn from code or painted; there are no
archive photographs, so there is nothing to attribute.

Subtitles are written for this video, not auto-generated. An American
English audio track is available as a second audio track.

There's More To It
```

---

## Tagy

```
internet explorer, ie6, web development, css hacks, haslayout, peekaboo bug,
quirks mode, front end, browser history, retrocomputing, css, windows xp,
star hack, conditional comments, legacy browsers
```

---

## Nastavení při nahrávání

| pole | hodnota |
|---|---|
| jazyk videa | **`en-gb`** — nastavit NAPŘED, jinak zůstane dlaždice Titulky zašedlá |
| titulky | `subtitles/*.srt`, devět jazyků |
| náhled | `render/thumbnail.jpg` (93 kB, 1280×720) |
| kategorie | Věda a technika |
| pro děti | ne |
| lokalizované názvy a popisy | `youtube-preklady.md` |

### Odpověď „byla použita AI" je NE

- **84 z 86 scén jsou diagramy kreslené kódem**, ne modelem
- zbylé dvě jsou SDXL, ale díky kotvě stylu **malované ilustrace**,
  ne fotorealismus — pravidla YouTube se ptají na fotorealističnost
- **žádný archivní snímek**
- hudba je **procedurální** (`tools/music.py`), ne z generativního modelu

### Atribuce

**Není co atribuovat.** `sources.json` neexistuje, protože video nemá ani
jeden archivní snímek. Věta v popisu to říká nahlas, ať se nikdo neptá.

---

## Před nahráním zkontrolovat

```bash
V=videos/028-ie6-the-bugs-that-had-names

# 1) master není rozsypaný — musí projít BEZE SLOVA
ffmpeg -v error -i $V/render/final-en.mp4 -f null -

# 2) délka
ffprobe -v error -show_entries format=duration -of default=nw=1:nk=1 \
        $V/render/final-en.mp4

# 3) titulky nepřesahují délku videa
tail -4 $V/subtitles/en.srt

# 4) náhled do 2 MB
ls -l $V/render/thumbnail.jpg
```

---

## Thumbnail

**Hotový obrázek dodaný uživatelem**, ne kreslený koncept — rozbité okno
Internet Exploreru polepené lepíky se jmény chyb, vpravo
`THE BUGS THAT HAD NAMES`. Původ, otisk a rozbor jsou
v `thumbnail/PUVOD.md`; originál je verzovaný v `thumbnail/`.

| | dodaný | pásmo 28 vydaných |
|---|---|---|
| jas | **101,8** | 20,3 az 115,7 |
| kontrast | 89,2 | 35,5 az 92,6 |
| saturace | 46,5 | 14,7 az 62,9 |

Rozhodlo **„téma poznat okamžitě"**: logo IE a chrome z éry Windows XP
to řeknou na jeden pohled, kdežto kreslený koncept `c1-peekaboo` sázel
na slovo, které samo o sobě Internet Explorer nepojmenuje. Lepíky se
ve 150 px nepřečtou a nemají — nesou tvrzení „je jich tolik, že jsou
polepené všude", ne informaci.

> **Dvě věci k rozhodnutí uživatele**, obě rozepsané v `thumbnail/PUVOD.md`:
> nápis je **tvrzení, ne otázka** (pravidlo šablony je tu splněné obrazem,
> ne textem), a jsou v něm **ochranné známky Microsoftu** — u videa o tom
> produktu je to běžné redakční užití, ale kanál má precedens, že logo NASA
> do náhledu nepatří.

**Kreslené koncepty zůstávají pro „Test & Compare":**
`render/thumb-c1-peekaboo.jpg`, `render/thumb-c2-ie6.jpg`,
`render/thumb-c3-guillotine.jpg`.
