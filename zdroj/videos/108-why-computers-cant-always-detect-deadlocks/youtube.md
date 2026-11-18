# YouTube — 108 „Why Can't Computers Predict Every Deadlock?“

Stav: **nahráno 2026-10-14 a naplánované** (https://www.youtube.com/watch?v=iaznfrY3DXw). Titulky 13 jazyků, americkou stopu a závěrečnou obrazovku doplnil uživatel ručně ve Studiu.

| | |
|---|---|
| ID videa | `iaznfrY3DXw` |
| master | ✅ `render/final-en-108.mp4` (8:59, 1920×1080, render 2026-10-14 na 207) |
| náhled | ✅ `render/thumbnail.jpg` — DEADLOCK / BEFORE IT HAPPENS?, obrázek od uživatele (`thumbnail/PUVOD.md`) |
| nastavení, popis, tagy | podklady níž |
| lokalizace | `youtube-preklady.md`, 13 jazyků |
| titulky | ✅ `subtitles/*.srt`, 14 jazyků + `en-US`, všechny prošly Codexem (`codex-zapracovano.md`) |
| americká stopa | ✅ `render/audio-en-US.m4a` — nahrává uživatel ve Studiu |
| závěrečná obrazovka | ručně ve Studiu |
| playlist | ✅ nový `pocitace` v `playlisty.json` |

**Co musí uživatel naklikat sám:** nahrát MP4 ve Studiu (průvodce vyřídí
prohlášení o AI a osvědčení o zproštění), závěrečnou obrazovku a americkou
audiostopu (`render/audio-en-US.m4a`).

Stopáž 8:59 (`work/timing.json` total 539,4 s).

> Kdyby se znovu pouštěl `tts.py`, přepočítej kapitoly tady
> i v `youtube-preklady.md` a přegeneruj `en-US` přes `us_stopa.py`.

Pořadí podle CENY (`docs/zverejneni.md`):

```bash
V=videos/108-why-computers-cant-always-detect-deadlocks
python tools/nahraj.py $V --k-videu=<ID> --bez-titulku    # 100
python tools/analytics.py --videa                         #   1  ← nutné
python tools/lokalizace.py $V                             #  50
python tools/titulky.py $V --smaz-asr                     # 150  ← před titulky
python tools/titulky.py $V                                # 400×15
python tools/playlisty.py                                 #  50
```

---

## 1. Titul

```
Why Can't Computers Predict Every Deadlock?
```

> Wh-otázka, 43 znaků. Rozhodl uživatel (pracovní název byl
> *Why Computers Can't Always Detect Deadlocks*): video tvrdí, že
> **poznat** deadlock jde, nejde ho obecně **předpovědět**.

---

## 2. Popis

```
Four cars arrive at a crossroads at exactly the same moment. Every driver gives way to the car on their right, so every driver waits, and nobody ever moves. Programs get stuck the same way. Two tasks each hold a lock the other one needs, and the code can run a million times without trouble before the timing goes wrong.

Databases are good at catching a deadlock once it has happened. Microsoft's SQL Server even picks a "deadlock victim" and tells it to try again. But could a program read another program and tell you, for certain, whether it will ever get stuck? From Alan Turing's halting problem to a laptop with more possible memory states than anyone could ever check, and to the bug Amazon's engineers found 35 steps deep: why no faster computer will fix this, and what programmers do instead.

Sources: A. M. Turing, "On Computable Numbers, with an Application to the Entscheidungsproblem", Proceedings of the London Mathematical Society (1936); M. Davis, Computability and Unsolvability (1958); C. Strachey, "An impossible program", The Computer Journal (1965); J. W. Havender, "Avoiding deadlock in multitasking systems", IBM Systems Journal (1968); E. G. Coffman, M. J. Elphick and A. Shoshani, "System Deadlocks", ACM Computing Surveys (1971); C. Newcombe et al., "How Amazon Web Services Uses Formal Methods", Communications of the ACM 58(4) (2015); Microsoft Learn, SQL Server deadlocks guide and error 1205; Vienna Convention on Road Traffic (1968), article 18.

Subtitles are written for this video, not auto-generated. An American English audio track is available as a second audio track.

Full transcript, sources and translations: https://theresmoretoit-channel.github.io/videos/why-computers-cant-always-detect-deadlocks/

CHAPTERS
00:00 Four cars, and nobody moves
01:03 How a program gets stuck
02:02 How databases catch a deadlock
02:49 The hard question
03:41 Turing and the halting problem
04:07 A program that does the opposite
04:37 What this has to do with deadlocks
06:12 But computers are finite
07:05 What programmers do instead
08:24 Back at the crossroads

IMAGE CREDITS
The portrait of Alan Turing in the 1930s is in the public domain, via Wikimedia Commons.
```

> **Blok se kopíruje CELÝ** (`docs/zverejneni.md`). Jediný archivní snímek
> (S26, Turing) je public domain, povinná atribuce tedy žádná; je vypsaný
> kvůli divákovi.
>
> **Zdroj Amazonu (S55) je tady, ne v `CREDITS.md`/`LICENSES.md`**
> (uživatel 2026-10-14): z článku se nepřebírá obraz ani text, jen fakt.
> V obraze S55 je citovaný drobně.
>
> **Pointa se neprozrazuje.** Popis neříká, že dokonalý předpovídač
> deadlocků existovat nemůže ani proč (převod z problému zastavení) —
> jen „why no faster computer will fix this“. Kapitola 04:37 je proto
> otázka z S33, ne „Deadlocks are undecidable“.
>
> Kapitoly ze scén S01, S07, S13, S19, S26, S29, S33, S45, S51, S59
> (`work/timing.json`, zaokrouhleno dolů). Nejkratší 26 s (S26 → S29),
> všechny ≥ 10 s, první na 00:00. Výzva k odběru S12b (1:54) leží
> v kapitole „How a program gets stuck“.
>
> Zdroje podle `factcheck.md`. Čísla v popisu (35 kroků, 1936) jsou
> tatáž jako ve scénáři.

---

## 3. Náhled

✅ `render/thumbnail.jpg` — DEADLOCK / BEFORE IT HAPPENS? (notebook
s kódem a otazníkem → smyčka dvou úloh a dvou zámků). Hotový obrázek
od uživatele, jen zmenšený; původ a otisk v `thumbnail/PUVOD.md`.
Kreslené koncepty C1–C3 (`thumbnail/KONCEPTY.md`) se nepoužily.

---

## 4. Titulky

`subtitles/*.srt`, 14 jazyků + `en-US`. Jazyk videa **`en-gb`** (hlas
`bf_emma`) se musí nastavit dřív, než se nahrají titulkové stopy.
Codex na všech 13 překladech proběhl a nálezy jsou zapracované
(`codex-zapracovano.md`).

---

## 5. Nastavení

| | |
|---|---|
| kategorie | **Science & Technology** (28) — posílá `nahraj.py` napevno |
| jazyk videa | `en-gb` |
| licence | standardní |
| pro děti | **ne** |
| komentáře | zapnuté |
| **byla použita AI** | **ne** (návrh, rozhoduje uživatel). 60 scén je kreslených kódem, jeden archivní snímek (Turing, PD) je jen barevně upravený (*color adjustment* je výslovná výjimka). **Tři scény ze SDXL** (S07 serverovna, S45 detail čipu, S51 noční kancelář) — obecné ilustrační záběry, žádná skutečná osoba, místo ani událost. S45 je z nich nejblíž fotografii, ale zobrazuje anonymní součástku, takže diváka o ničem skutečném neklame. Hudba je procedurální, hlas není klon. |

### Závěrečná obrazovka

Od **8:39** (posledních 20 s), tedy S61–S63. `zaver_check.py`: S61–S63 OK,
prvky patří do **horní poloviny** (spodní polovinu zabírá kresba
a titulek).

---

## 6. Tagy

```
deadlock, deadlocks, halting problem, alan turing, computer science,
undecidability, databases, sql server, deadlock victim, concurrency,
locks, multithreading, formal methods, tla+, model checking,
science explainer, there's more to it
```

---

## 7. Playlist

**Nový playlist `pocitace`** (uživatel 2026-10-14: „playlist klidně
nový“): *Inside Your Computer — Why It Behaves the Way It Does*, s videi
056, 059, 066, 093, 088 a 108 (všechna kromě 108 zůstávají i ve svých
dosavadních playlistech). První je 056, takže dává miniaturu playlistu;
pořadí jde změnit jen ve Studiu.
