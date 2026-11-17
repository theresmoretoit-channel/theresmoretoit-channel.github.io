# YouTube — 066 „Why Is Software Still So Full of Bugs?"

Stav: **PŘIPRAVENO K NAHRÁNÍ** (master hotový, náhled vybraný, 14 jazyků + en-US).

| | |
|---|---|
| video | `render/final-en.mp4` (master, 608,9 s) |
| náhled | `render/thumbnail.jpg` — koncept **c1 (brouk, BUGS / WHY SO MANY?)**, vybral uživatel |
| titulky | `subtitles/*.srt`, 14 jazyků + `en-US` |
| americká stopa | `render/audio-en-US.m4a` (nahrát ve Studiu jako druhou stopu) |

Pořadí podle CENY (`docs/zverejneni.md`):

```bash
V=videos/066-why-is-software-still-so-full-of-bugs
python tools/nahraj.py $V --k-videu <ID> --bez-titulku   # 100
python tools/analytics.py --videa                        #   1  ← nutné
python tools/lokalizace.py $V                            #  50
python tools/titulky.py $V --smaz-asr                    # 150  ← před titulky
python tools/titulky.py $V                               # 400×15
python tools/playlisty.py                                # 100
```

**Co musí uživatel naklikat sám:** závěrečnou obrazovku (API na ni nemá
zdroj) a nahrát americkou audiostopu. Prohlášení o AI a osvědčení
o zproštění vyřídí průvodce při ručním nahrání MP4.

---

## 1. Titul

```
Why Is Software Still So Full of Bugs?
```

Wh-otázka (`docs/kanal-metriky.md`: 2,23 % proti 1,63 % u tvrzení).

---

## 2. Popis

```
Every few days, another serious bug makes the news — one that leaks
private data, or hands an attacker a computer. And the reaction is almost
always the same: these are professionals, with code reviews, tests and
audits. So how do the bugs keep coming?

This video is about why, and the answer isn't "bad programmers." It's a
wall built into the mathematics. A program with just a hundred on-or-off
settings already has more combinations than you could ever test — more
than if you had started checking a billion of them every second at the Big
Bang. Real programs have millions of switches. "Just test everything"
isn't expensive. It's impossible.

From there it only goes deeper: memory bugs that let attackers run their
own code, the fact that no program can check every other program (Alan
Turing proved it in 1936, Henry Rice went further in 1953), and the catch
that even a full mathematical proof only shows the code matches a
specification — and the specification is written by people.

So maybe "how do we write software without bugs?" is the wrong question.
The better one is: how do we build systems that stay safe even when the
software has bugs?

Subtitles are written for this video, not auto-generated. An American
English audio track is available as a second audio track.

CHAPTERS
00:00 Another bug in the news
00:44 A hundred switches, and 2^100
01:27 The simplest thing a program does
02:34 C, and control over memory
04:04 Newer languages and the compiler
04:33 Memory-safe, and still wrong
05:04 What a test can and can't prove
05:29 A program that proves programs?
06:33 seL4: proved correct, at a cost
07:15 You don't have to write a bug
07:51 Better tools, more vulnerabilities
08:33 The better question
08:50 How the system guards memory today
09:23 If bugs are inevitable
10:00 "It works" vs "it's safe"

IMAGE CREDITS
Edsger W. Dijkstra — Hamilton Richards, CC BY-SA 3.0
via Wikimedia Commons
Licence: creativecommons.org/licenses/by-sa/3.0/

The photograph of Alan Turing is in the public domain.
```

> **Blok se kopíruje CELÝ.** Atribuce Dijkstry (Hamilton Richards,
> CC BY-SA 3.0) je uvnitř schválně — je to jediný snímek pod CC. Turingova
> fotka je public domain, uvedená jednou větou.
>
> **Kapitolové časy** jsou začátky scén z `work/timing.json`. Po jakékoli
> změně stopáže je přepočítat.

---

## 3. Náhled

`render/thumbnail.jpg` — **koncept c1 (brouk, BUGS / WHY SO MANY?)**,
vybral uživatel 2026-09-26 (menší brouk, ať nezasahuje do nadpisu).
Kreslený kódem (`thumbnail/gen.py`), tedy ilustrace — na otázku „byla
použita AI" to nic nemění. Kontrola `python tools/thumb_check.py $V`.

---

## 4. Titulky

`subtitles/*.srt`, všech 14 jazyků + `en-US`. Jazyk videa **`en-gb`**
(hlas `bf_emma`) se musí nastavit dřív, než se nahrají titulkové stopy.

---

## 5. Nastavení

| | |
|---|---|
| kategorie | Science & Technology |
| jazyk videa | `en-gb` |
| licence | standardní |
| pro děti | **ne** |
| komentáře | zapnuté |

### Prohlášení o AI: **ne**

Rozhoduje fotorealističnost. Dvě SDXL scény (S51 noční pracovna, S63
notebook na stole) jsou malované ilustrace podle kotvy stylu a nezobrazují
žádné skutečné místo ani událost; 63 scén je kreslených kódem, dva archivní
portréty (Dijkstra, Turing) jsou upravené jen barevně, hudba je procedurální.

### Závěrečná obrazovka

Dlaždici i kolečko dej do **horní** poloviny (S64–S67 mají horní polovinu
volnou, dole je titulek). Odkaz na video 019 *„It Still Works. So Why
Upgrade It?"* (zmíněné v závěru).

---

## 6. Tagy

```
software bugs, why software has bugs, computer science, buffer overflow,
memory safety, rust, turing, halting problem, rice's theorem, sel4,
formal verification, cybersecurity, technical debt, programming, explainer,
there's more to it
```

---

## 7. Playlist

Zvaž `technologie` / vývoj softwaru — soused 053 *Why are there so many
bugs in Windows?* a 019 *It Still Works. So Why Upgrade It?*. Dopiš slug
do `playlisty.json`, spusť `analytics.py --videa` a pak `tools/playlisty.py`.
