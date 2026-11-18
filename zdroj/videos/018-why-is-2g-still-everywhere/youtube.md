# Podklady k nahrání na YouTube

Vyplněno podle `script 0.3.md` (85 scén) a `work/timing.json` (13:20).

---

## Titul

```
2G Is Ancient. So Why Are Lifts, Cars and Alarms Still Using It?
```

## Popis

```
Your lift has an emergency phone. Your car has an emergency call system.
Somewhere in your building there is an alarm, and somewhere in your street
there is a meter. A surprising number of them talk to the outside world
over 2G — a mobile network that first went live in 1991.

Operators want to switch it off, and they have good reasons: radio spectrum
is finite and modern networks use it far better. But the machines that
depend on 2G were built to last twenty or thirty years, and nobody replaces
a device that still works.

A study commissioned by the European Commission and published in May 2026
estimates that 64 million vehicles across the EU could lose eCall if the
old networks are switched off without coordination. It recommends that each
Member State keep at least one circuit-switched network alive until at
least 2030.

So maybe the question isn't whether to keep 2G. Maybe it's how little of it
we actually need.

Full transcript, sources and translations: https://theresmoretoit-channel.github.io/videos/why-is-2g-still-everywhere/

CHAPTERS
0:00 Stuck between floors
1:01 2G is ancient
1:38 What a lift actually needs
2:26 Remember GPRS?
3:31 Machines don't get replaced
4:17 The car problem
5:17 Just replace the module?
6:06 Why operators want it gone
6:51 How much 2G do we need?
7:42 EU Legacy
8:08 This isn't hypothetical
9:10 We've done this before
9:51 Why mobile networks are harder
10:21 Legacy isn't bad
11:06 2028 is not far away
11:47 The boring solution
12:01 One tiny message

SOURCES AND CREDITS
European Commission study on eCall and 2G/3G network shutdowns (LS Telcom,
28 May 2026):
https://digital-strategy.ec.europa.eu/en/library/eu-study-informs-ecall-service-gaps-2g3g-networks-shut-down

Regulation (EU) 2015/758 on 112-based eCall:
https://eur-lex.europa.eu/EN/legal-content/summary/ecall-in-vehicle-system-type-approval.html

Archive images, all Wikimedia Commons:
· Berlaymont building — Trougnouf (Benoit Brummer), CC BY 4.0
· ASA-TV 221 television set, 1956 — Museokeskus Vapriikki, CC BY 2.0
· Nokia 5110 — Soltys0, CC BY-SA 2.5

Subtitles are written for this video, not auto-generated. An American
English audio track is available as a second audio track.
```

> **EU Legacy je náš myšlenkový experiment, ne existující projekt.** Popis
> to nesmí naznačit — proto tam ta část není a věta o doporučení Komise
> stojí odděleně. Video si to samo hlídá v S49, S50 a S58.

## Tagy

```
2G, GSM, eCall, mobile networks, network shutdown, legacy technology,
IoT, M2M, telecoms, infrastructure, European Commission, spectrum,
GPRS, lifts, elevators, backward compatibility
```

## Nastavení při nahrávání

| položka | hodnota | proč |
|---|---|---|
| soubor | `render/final-en.mp4` | **master, ne draft** |
| náhled | `render/thumbnail.jpg` | do 2 MB, 1280×720 |
| **jazyk videa** | **`en-gb`** | nastavit **jako první**, jinak zůstane dlaždice „Titulky" zašedlá. Hlas je `bf_emma`. |
| titulky | `subtitles/*.srt` | devět jazyků |
| **byla použita AI?** | **NE** | 74 diagramů kreslených kódem, 8 malovaných SDXL scén (kotva stylu, ne fotorealismus), 3 archivní snímky upravené jen barevně, hudba procedurální. Viz CLAUDE.md, „Označení AI obsahu". |
| kategorie | Science & Technology | |
| publikum | není určeno dětem | |

## Před nahráním zkontrolovat

```bash
ffmpeg -v error -i videos/018-why-is-2g-still-everywhere/render/final-en.mp4 -f null -
ffprobe -v error -show_entries format=duration -of default=nw=1:nk=1 \
        videos/018-why-is-2g-still-everywhere/render/final-en.mp4
ls -la videos/018-why-is-2g-still-everywhere/render/thumbnail.jpg
```

**Nahrát jako neveřejné a podívat se na to v přehrávači.** YouTube video
překóduje a jak vyjde tmavá scéna po jejich kompresi, se dopředu posoudit
nedá — je to jediný krok, který nejde udělat na disku.

Kapitoly YouTube uzná, protože první začíná na `00:00`, je jich sedmnáct
a nejkratší trvá 26 s (ověřeno proti `work/timing.json`).
