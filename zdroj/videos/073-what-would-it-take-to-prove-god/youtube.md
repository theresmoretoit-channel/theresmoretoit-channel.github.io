# YouTube — 073 „What Would It Take to Prove God?"

Stav: **NAHRÁNO VČETNĚ METADAT, LOKALIZACÍ A TITULKŮ**; zbývá ruční část ve Studiu.

| | |
|---|---|
| ID videa | `6IuuXCygHY0` (https://www.youtube.com/watch?v=6IuuXCygHY0) |
| nastavení, popis, tagy, náhled | ✅ 2026-09-30 `nahraj.py --k-videu 6IuuXCygHY0 --bez-titulku` |
| lokalizace | ✅ 2026-09-30 13 jazyků jedním voláním (`lokalizace.py`) |
| titulky | ✅ 2026-09-30 15 stop (en, cs, sv, es, pt-BR, de, fr, it, pl, id, tr, uk, vi, fi, en-US) |
| automatický přepis | ⬜ zatím nevznikl (smazáno 0); za pár dní znovu `titulky.py $V --smaz-asr` |
| playlist | ✅ `lide` (2026-09-30) |
| závěrečná obrazovka, americká stopa | ⬜ uživatel ve Studiu |

**Co musí uživatel naklikat sám:** závěrečnou obrazovku (API na ni nemá zdroj)
a nahrát americkou audiostopu (`render/audio-en-US.m4a`). Prohlášení o AI
a osvědčení o zproštění vyřídí průvodce při ručním nahrání MP4.

Soubor k nahrání: `render/final-en-073.mp4`.

Pořadí podle CENY (`docs/zverejneni.md`):

```bash
V=videos/073-what-would-it-take-to-prove-god
python tools/nahraj.py $V --k-videu 6IuuXCygHY0 --bez-titulku   # 100
python tools/analytics.py --videa                         #   1  ← nutné
python tools/lokalizace.py $V                             #  50
python tools/titulky.py $V --smaz-asr                     # 150  ← před titulky
python tools/titulky.py $V                                # 400×15
python tools/playlisty.py                                 # 100
```

---

## 1. Titul

```
What Would It Take to Prove God?
```

> wh-otázka („What…") — podle `docs/kanal-metriky.md` nejlepší CTR. Náhled
> se ptá na metodu („WHAT WOULD PROVE IT?"), odpověď neprozrazuje.

---

## 2. Popis

```
Someone tells you God exists. You ask how they know. "Because I have
proof." But what would that proof actually have to prove? And could anyone
prove the opposite?

This video looks at what "proof" even means — an apple in a box, a
mathematical proof and a scientific theory are three very different things.
Then it goes through the ways people have tried to settle the question of
God: the cosmological argument and fine-tuning, claimed miracles, the problem of evil, divine
hiddenness, a God defined to be beyond any observation, and Carl Sagan's
invisible dragon in the garage.

Along the way: why "there's a natural explanation" is not the same as "God
doesn't exist", why the inability to disprove a claim is not evidence that
it's true, and the same kind of mistake that atheists and believers
sometimes make from opposite sides.

Sometimes the hardest part isn't finding the answer. It's figuring out
whether the question can have an answer at all.

Subtitles are written for this video, not auto-generated. An American
English audio track is available as a second audio track.

Full transcript, sources and translations: https://theresmoretoit-channel.github.io/videos/what-would-it-take-to-prove-god/

CHAPTERS
00:00 "Because I have proof"
00:35 What counts as proof?
01:18 Which God?
02:01 The cosmological argument
02:40 Fine-tuning
03:35 Miracles and what we can test
04:28 Can we disprove God?
05:39 Divine hiddenness
06:25 A God beyond any observation
06:59 The invisible dragon
07:38 Three different questions
08:38 A mistake on both sides
09:44 Does God exist? Yes or no

IMAGE CREDITS
Cosmic Cliffs in the Carina Nebula — NASA, ESA, CSA, STScI
All other archive images are in the public domain.
```

> **Blok se kopíruje CELÝ** (`docs/zverejneni.md`) — atribuce jsou UVNITŘ.
> Všech šest archivních snímků je volné dílo (S19 Crivelli, S38 Currier & Ives,
> S43 Le Bas, S52 Redman, S64 NASA/JPL; S26 NASA/ESA/CSA/STScI jako dílo
> US Government). Uvedení u S26 není povinné, uvádí se z korektnosti (TASL).
>
> Kapitoly jsou ze scén S01, S08, S14, S19, S25, S33, S41, S51, S59, S64,
> S71, S81, S91 (`work/timing.json`). S43 (problém zla, 04:37) samostatnou
> kapitolou není — od S41 ji dělí 9 s a YouTube chce kapitolu aspoň 10 s.

---

## 3. Náhled

`render/thumbnail.jpg` — **hotový** (koncept C1, zavřená krabice se světlem
pod víkem, „GOD / WHAT WOULD PROVE IT?"; vybral uživatel 2026-09-30). Zdroj
`thumbnail/c1-krabice.svg` přes `thumbnail/gen.py`; `thumb_check.py` — jas 50,
kontrast 77, uprostřed pásma kanálu. Nevybrané koncepty: C2 baňka, C3 lupa.

---

## 4. Titulky

`subtitles/*.srt`, 14 jazyků + `en-US`. Jazyk videa **`en-gb`** (hlas
`bf_emma`) se musí nastavit dřív, než se nahrají titulkové stopy, jinak
zůstane dlaždice Titulky zašedlá.

---

## 5. Nastavení

| | |
|---|---|
| kategorie | Education |
| jazyk videa | `en-gb` |
| licence | standardní |
| pro děti | **ne** |
| komentáře | zapnuté |

### Prohlášení o AI: **ne**

Rozhoduje fotorealističnost, ne použití AI. Video nemá žádnou SDXL scénu:
96 scén je kreslených kódem, 6 jsou barevně upravené archivní snímky (výjimka
„color adjustment"). Garáž v S65 je plochá malovaná ilustrace z ChatGPT
(`art/PUVOD.md`), ne fotorealismus. Hudba je procedurální, hlas není klon
skutečné osoby.

### Závěrečná obrazovka

S98–S101 mají **horní polovinu volnou** (kresba jen dole) — dlaždici dalšího
videa i kolečko odběru dej do **horní** poloviny (`zaver_check.py` ověřeno).

---

## 6. Tagy

```
what would it take to prove god, can you prove god exists, existence of
god, proof of god, philosophy of religion, cosmological argument,
fine-tuning argument, problem of evil, divine hiddenness, invisible dragon,
carl sagan, burden of proof, falsifiability, atheism, epistemology,
explainer, there's more to it
```

---

## 7. Playlist

Playlist `lide` (spolu se sesterským 068, viz `notes.md`). Dopiš slug do
`playlisty.json`, spusť `analytics.py --videa` a pak `tools/playlisty.py`.
