# Podklady k nahrání na YouTube

Časy kapitol **ověřené proti `work/timing.json`**, ne odhadnuté.
Každá kapitola je od předchozí aspoň 10 s, první je `0:00` a je jich
17 — YouTube uzná kapitoly, jen když platí všechny tři podmínky.

| co | odkud |
|---|---|
| video | `render/final-en.mp4` — 1920×1080, **11:07**, 53,5 MB |
| náhled | `render/thumbnail.jpg` — 1280×720, 0,26 MB |
| titulky | `subtitles/*.srt` — **deset stop**: devět jazyků + `en-US` |
| americká stopa | `render/audio-en-US.m4a` — 15,1 MB, sedí na obraz na tisícinu |
| lokalizované názvy a popisy | `youtube-preklady.md` |

**Archivní snímek je jeden** (S32, ISA karta s disketami) a je pod
**CC BY-SA 4.0**, takže atribuce je POVINNÁ a musí být **uvnitř bloku
„Popis"** — ne pod ním. Napříč kanálem u čtyř videí ze šestnácti chyběla
přesně proto, že kredity visely jako poznámka vedle.

---

## Titul

```
Why Do Some People Hate Windows?
```

> Wh-otázka schválně. Naměřeno na kanálu (29 videí, vážené impresemi):
> wh-otázka **2,23 %**, tvrzení 1,63 %, ano/ne otázka 1,21 %.

## Popis

```
Windows runs on more than a billion computers. For most of the people
using it, it is simply the thing that starts when they press the button.

And then there are people who can talk for an hour about why it is
terrible.

This video is about what those people are actually objecting to — and why
it might make no sense to you at all.

Some of it is history: today's Windows was never designed as one system,
and backward compatibility is both its greatest strength and the reason
it feels like a technological patchwork. Some of it is reputation earned
in the nineties and never quite lost. Some of it is about Microsoft the
company rather than Windows the system.

But underneath all of that is a question that has nothing to do with bugs
at all. It is about who decides what you may do with something you bought.

Chapters:
0:00 Most people never think about it
0:42 The paradox: thirty-year-old programs
1:12 The washing machine
1:39 Forty years of building on top
2:07 The building nobody can demolish
3:06 Windows 95, 98, ME — and the reputation
3:32 Windows NT and XP
4:04 Microsoft the company
4:42 "But the computer is mine"
5:33 Closed source
6:47 It was about who decides
7:04 Linux is a different philosophy
7:56 And what about Apple?
8:59 Three approaches
9:22 Modern Windows
10:05 So who is actually right?
10:43 What do you actually want?

Subtitles are available in English (UK), English (US), Czech, Swedish,
Spanish, Portuguese (Brazil), German, French, Italian and Polish.
An American audio track is available in the audio track selector.

IMAGE CREDITS
Tekram DC-300B Fast SCSI ISA controller — Dmitry Nosachev, CC BY-SA 4.0
via Wikimedia Commons
Licences: creativecommons.org/licenses/by-sa/4.0

All other visuals are drawn from the project's own source files.
```

---

## Nastavení při nahrávání

| pole | hodnota |
|---|---|
| jazyk videa | **`en-GB`** — nastavit **NEJDŘÍV**, jinak zůstane dlaždice Titulky zašedlá |
| kategorie | Věda a technika |
| publikum | není určeno pro děti |
| prohlášení o AI | **ne** — SDXL scény jsou malované ilustrace, archivní snímek jen barevně upravený, hudba procedurální |
| viditelnost | nejdřív **neveřejně**, podívat se na to v přehrávači, teprve pak zveřejnit |

## Tagy

```
windows, microsoft, operating system, linux, apple, open source,
closed source, proprietary software, backward compatibility, windows xp,
windows me, internet explorer, antitrust, free software, explainer
```

## Co musí uživatel naklikat sám

Podle `docs/zverejneni.md` se to liší podle způsobu nahrání:

| | nahrál MP4 ručně (`--k-videu`) | `videos.insert` |
|---|---|---|
| prohlášení o AI | ✅ vyřídí průvodce | ❌ **ručně** |
| osvědčení o zproštění | ✅ vyřídí průvodce | ❌ **ručně** |
| **závěrečná obrazovka** | ❌ **ručně** | ❌ **ručně** |

Závěrečná obrazovka je ruční vždycky — Data API na ni nemá ani zdroj.
Místo pro ni je ověřené: `zaver_check.py` hlásí u všech šesti scén
posledních dvaceti sekund (S96–S101) překryv **0,0 %**, prvky patří do
**horní poloviny** obrazu.

## Po zveřejnění

1. Dopsat slug do `playlisty.json`, spustit `analytics.py --videa`
   a pak `tools/playlisty.py`.
2. `python tools/titulky.py --vse --smaz-asr` — automatický přepis od
   YouTube se na kanálu maže, konkuruje našim deseti stopám.
3. Doplnit řádek 46 do `Témata.ods` (a 45, pokud tam ještě není).
