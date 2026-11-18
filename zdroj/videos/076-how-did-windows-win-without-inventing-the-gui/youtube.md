# YouTube — 076 „How Did Windows Win Without Inventing the GUI?"

Stav: **HOTOVO, naplánováno na zveřejnění** (2026-10-01). Přes API metadata, náhled,
lokalizace a playlist; titulky, americkou stopu a závěrečnou obrazovku naklikal uživatel ve Studiu.

| | |
|---|---|
| ID videa | `crb68Ur-OTI` (https://www.youtube.com/watch?v=crb68Ur-OTI) |
| nastavení, popis, tagy | ✅ 2026-10-01 `nahraj.py --k-videu crb68Ur-OTI --bez-titulku` |
| náhled | ✅ 2026-10-01 (týž běh) |
| lokalizace | ✅ 2026-10-01 13 jazyků jedním voláním (`lokalizace.py --id`) |
| automatický přepis | ✅ uživatel ve Studiu 2026-10-01 (může se po zpracování vrátit — za pár dní `titulky.py $V --smaz-asr`) |
| titulky | ✅ uživatel ručně ve Studiu 2026-10-01 (14 jazyků + `en-US`) |
| playlist | ✅ `legacy`, pozice 11 za 062 (`playlisty.py --jen legacy`) |
| závěrečná obrazovka, americká stopa | ✅ uživatel ve Studiu 2026-10-01 |

**Co musí uživatel naklikat sám:** závěrečnou obrazovku (API na ni nemá zdroj)
a nahrát americkou audiostopu (`render/audio-en-US.m4a`). Prohlášení o AI
a osvědčení o zproštění vyřídí průvodce při ručním nahrání MP4.

Soubor k nahrání: `render/final-en-076.mp4` (592,7 s, 1920×1080, ověřeno
`ffmpeg -f null` beze slova).

Pořadí podle CENY (`docs/zverejneni.md`):

```bash
V=videos/076-how-did-windows-win-without-inventing-the-gui
python tools/nahraj.py $V --k-videu <ID> --bez-titulku    # 100
python tools/analytics.py --videa                         #   1  ← nutné
python tools/lokalizace.py $V                             #  50
python tools/titulky.py $V --smaz-asr                     # 150  ← před titulky
python tools/titulky.py $V                                # 400×15
python tools/playlisty.py                                 # 100
```

---

## 1. Titul

```
How Did Windows Win Without Inventing the GUI?
```

> wh-otázka („How…") — podle `docs/kanal-metriky.md` nejlepší CTR. Titul
> neprozrazuje odpověď (licence DOS a klony IBM PC).

---

## 2. Popis

```
Windows, icons, menus, a mouse. For most people, that is simply what a computer looks like, and most of them met it through Microsoft. But when the first Windows appeared in 1985, almost none of that was new.

Douglas Engelbart demonstrated a computer controlled with a mouse in 1968. Xerox PARC built the Alto in the 1970s and sold the Star in 1981. Apple launched the Lisa and then the Macintosh. All of them got there before Microsoft, and none of their machines ended up on most of the world's desks.

This video follows what happened in between: a contract with IBM, a wave of compatible PCs, a six-year lawsuit, and a loop that is very hard to break once it gets going.

Subtitles are written for this video, not auto-generated. An American English audio track is available as a second audio track.

Full transcript, sources and translations: https://theresmoretoit-channel.github.io/videos/how-did-windows-win-without-inventing-the-gui/

CHAPTERS
00:00 What Windows didn't invent
00:36 Engelbart's demo
01:12 Xerox Alto
02:14 Xerox Star
03:03 Apple: the Lisa and the Mac
04:01 The catch
04:22 IBM needs an operating system
04:56 The detail in the contract
05:17 The clones
06:21 Windows 1.0 and 2.0
06:50 Apple v. Microsoft
07:25 Windows 3.0
08:08 The loop
08:35 Windows 95
08:57 How Windows won

IMAGE CREDITS
Douglas Engelbart, 1968 — SRI International, CC BY-SA 3.0, via Wikimedia Commons
Douglas Engelbart's prototype mouse, Computer History Museum — Michael Hicks, CC BY 2.0, via Wikimedia Commons
Xerox Alto I, 1973, Computer History Museum — The wub, CC BY-SA 4.0, via Wikimedia Commons
Xerox Star 8010 — Al Lemos, derivative of a photo by Marcin Wichary, CC BY 2.0, via Wikimedia Commons
Apple Lisa — Timothy Colegrove, CC BY-SA 4.0, via Wikimedia Commons
Macintosh 128K, 1984 (All About Apple museum) — Sailko, CC BY 3.0, via Wikimedia Commons
All other archive images are in the public domain.
Licences: creativecommons.org/licenses/by/2.0, /by/3.0, /by-sa/3.0, /by-sa/4.0

WINDOWS SCREENSHOTS
Windows 1.01, Windows/386 2.01, Windows 3.0 and Windows 95, captured in the PCjs emulator (pcjs.org).
Used with permission from Microsoft.
```

> **Blok se kopíruje CELÝ** (`docs/zverejneni.md`) — atribuce jsou UVNITŘ.
> Povinné jsou všechny CC BY* snímky z `sources.json`: S06, S07, S13, S19,
> S30, S32. S48 (IBM PC) a S50 (Compaq) jsou public domain, proto souhrnná
> věta. S39 (SDXL) atribuci nepotřebuje.
>
> **„Used with permission from Microsoft." je podmínka Microsoftu** pro
> screenshoty (S57, S61, S69, S81, S82) — `art/PUVOD.md`. Je doslova
> i ve všech 13 jazycích v `youtube-preklady.md` (lokalizovaný popis
> nahrazuje anglický, takže by jinak divákovi v jiném jazyce chyběla).
> Prohlášení o splnění podmínek se nepíše (rozhodl uživatel).
>
> Kapitoly jsou ze scén S01, S06, S12, S19, S26, S35, S39, S44, S48, S57,
> S62, S69, S76, S81, S86 (`work/timing.json`, celkem 592,7 s = master).
> Všechny ≥ 10 s. **Po každém dalším běhu `tts.py` časy přepočítej** —
> a stejně tak v `youtube-preklady.md`.
>
> Fakta popisu proti scénáři: Engelbart 1968 (S06), Alto 70. léta (S13
> „first ones ran in 1973"), Star 1981 (S19), Lisa → Macintosh (S30, S32),
> Windows 1985 (S02), spor šest let (S68).

---

## 3. Náhled

`render/thumbnail.jpg`: **hotový** — trofej s klasickým oknem (styl Win95,
ne logo Windows), „WINDOWS / HOW DID IT WIN?", ChatGPT. Původ a zamítnuté
verze v `thumbnail/PUVOD.md`. Screenshoty Windows v náhledu **nejsou**
(povolení se ověřovalo pro video, ne pro propagaci).

---

## 4. Titulky

`subtitles/*.srt`, 14 jazyků + `en-US`. Jazyk videa **`en-gb`** (hlas
`bf_emma`) se musí nastavit dřív, než se nahrají titulkové stopy, jinak
zůstane dlaždice Titulky zašedlá. Všechny překlady prošly Codexem
(2026-10-01) a nálezy jsou zapracované.

---

## 5. Nastavení

| | |
|---|---|
| kategorie | Education |
| jazyk videa | `en-gb` |
| licence | standardní |
| pro děti | **ne** |
| komentáře | zapnuté |
| **byla použita AI** | **ne** |

Prohlášení o AI **ne**: 79 scén kreslených kódem, 8 archivních snímků
upravených jen barevně (výjimka „color adjustment"), 5 screenshotů
skutečného softwaru, jediná SDXL scéna (S39) je malovaná kancelář —
ne fotorealismus. Hudba procedurální, hlas není klon skutečné osoby.

### Závěrečná obrazovka

`zaver_check.py`: v posledních scénách (S90–S92) je místo v **horní
polovině** — dole je titulek. Jako dlaždici doporučuju **046** („Why Do
Some People Hate Windows?"), nejbližší téma.

---

## 6. Tagy

```
how did windows win, windows history, history of the gui, graphical user interface,
microsoft history, windows 1.0, windows 3.0, windows 95, ms-dos, ibm pc,
ibm compatible, compaq, xerox parc, xerox alto, xerox star, douglas engelbart,
mother of all demos, apple lisa, macintosh, apple vs microsoft, network effect,
computer history, tech history, explainer, there's more to it
```

---

## 7. Playlist

Playlist `legacy` („Legacy Tech — The Old Systems Still Running Everything"),
spolu s ostatními videi o Windows. Dopiš slug do `playlisty.json` hned za
`062-why-doesnt-windows-have-proper-tools`, spusť `analytics.py --videa`
a pak `tools/playlisty.py`.
