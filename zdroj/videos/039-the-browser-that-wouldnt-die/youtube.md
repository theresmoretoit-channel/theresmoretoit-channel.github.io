# Podklady k nahrání na YouTube

Časy kapitol **ověřené proti `work/timing.json`**, ne odhadnuté.

> **Master render zatím NENÍ.** Draft je `render/draft-en.mp4` (960×540,
> 13:52). Nahrává se až `render/final-en.mp4` — 1920×1080, 25 fps,
> 3× supersampling, CRF 18. A ve videu jsou zatím **dva SDXL
> placeholdery** (S32 a S96), takže master nemá smysl dělat dřív, než
> bude dostupné herní PC.

> **Je to TŘETÍ DÍL trilogie.** V popisu musí být odkazy na oba
> předchozí, jinak divák, který přijde na trojku, nemá kam jít:
> `https://youtu.be/R7Un3IOMvbg` (017 — *The Browser That Became
> a Platform*) a `https://youtu.be/1dIM5UZUEZg` (028 — *The Bugs That
> Had Names*).

> **Archivní snímky žádné.** 95 diagramů, 2 SDXL scény, nula archivu —
> `sources.json` ani `CREDITS.md` proto neexistují a v popisu **není co
> atribuovat**. Není to opomenutí; kdyby archiv přibyl, musí se kredity
> dostat DOVNITŘ bloku „Popis".

---

## Titul

```
Internet Explorer 6 — The Browser That Wouldn't Die
```

---

## Popis

**Kopíruje se CELÝ blok mezi apostrofy a nic jiného.**

```
Microsoft spent years telling people to stop using Internet Explorer 6.
There was a countdown on its own website, percent by percent, country by
country. And in 2010 millions of machines were still running it.

Not because anyone liked it. Because something they needed depended on it.

This is part three, and it asks the harder question: what happens when
obsolete software becomes infrastructure? The answer isn't Windows XP —
Internet Explorer 7 and 8 both ran on XP, so the operating system was
never what held those machines back. It was one internal application
nobody fully understood any more.

Along the way: the attack that broke into Google through a hole in
Internet Explorer, two governments telling their citizens to switch
browsers, the tool Microsoft published to block its own new browser
(four times), the product it sold that ran a hidden copy of Windows XP
inside Windows 7 just to keep the old browser alive, a country whose
banking regulations locked it to one vendor, and five and a half million
pounds paid for one more year of not upgrading.

Part one — how Internet Explorer 6 became a platform:
https://youtu.be/R7Un3IOMvbg

Part two — the bugs that had names:
https://youtu.be/1dIM5UZUEZg

Full transcript, sources and translations: https://theresmoretoit-channel.github.io/videos/the-browser-that-wouldnt-die/

Chapters
00:00 Part three
01:19 January 2010
01:33 Somebody inside Google
02:02 Operation Aurora
02:36 Google stops waiting
03:04 The usual explanation is wrong
04:06 The OS wasn't the reason
04:20 What that application was
05:13 A tool to block its own browser
06:01 When the machine itself dies
06:44 Windows XP inside Windows 7
07:26 Killing it and selling it
07:59 A setting inside the new one
08:39 South Korea
09:40 China and America
10:11 Eight hundred thousand machines
11:22 How it actually ended
12:24 Switched off in 2022
12:53 Browser, platform, dependency
13:39 When the world stopped depending

Subtitles are written for this video, not auto-generated. An American
English audio track is available as a second audio track.
```

---

## Tagy

```
internet explorer 6, ie6, legacy software, technical debt, activex, windows xp, microsoft, browser wars, operation aurora, med-v, enterprise it, software history, dependency, infrastructure, web development history
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
| **závěrečná obrazovka** | **ruční krok ve Studiu** — API na to nemá zdroj. `zaver_check.py` hlásí u S93–S96 volné místo v HORNÍ polovině |

### Prohlášení o AI: odpověď je NE

Rozhoduje fotorealističnost, ne použití AI:

- 95 scén jsou **diagramy kreslené kódem** (Inkscape z SVG)
- 2 scény jsou SDXL, ale kotva stylu z nich dělá **malované ilustrace**,
  ne fotorealismus
- hudba je **procedurální** (numpy), ne z generativního modelu
- hlas je Kokoro `bf_emma`, tedy syntéza, **ne klonovaný hlas skutečné
  osoby**

### Po nahrání

1. `python tools/titulky.py <ID> --smaz-asr` — automatický přepis od
   YouTube konkuruje devíti překladům a je z nich nejhorší
2. závěrečná obrazovka ručně
3. zapsat odkaz a stav do `Témata.ods`
