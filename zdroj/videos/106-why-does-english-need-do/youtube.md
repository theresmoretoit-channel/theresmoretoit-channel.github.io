# YouTube — 106 „Why Does English Need "Do" to Ask a Question?"

Stav: **naplánováno ke zveřejnění** (2026-10-13). Po vyčerpání kvóty uživatel doklikal zbytek ručně ve Studiu.

| | |
|---|---|
| ID videa | **`KVQcvoh7zOY`** — https://www.youtube.com/watch?v=KVQcvoh7zOY |
| master | ✅ `render/final-en-106.mp4` (1920×1080, 7:58, ověřeno `ffmpeg -f null`) |
| náhled | ✅ od 2026-10-14 hotový obrázek od uživatele `ENGLISH / WHAT DOES "DO" DO?` (`thumbnail/PUVOD.md`); 13.–14. 10. běželo pod kresleným C1 `ENGLISH / WHY TWO DOs?` — **při srovnání CTR dělit k tomuto datu** |
| nastavení, popis, tagy | ✅ `nahraj.py --k-videu --bez-titulku` 2026-10-13 (+ náhled) |
| lokalizace | ✅ 13 jazyků nahráno 2026-10-13 |
| titulky | ✅ en, cs, sv, es, pt-BR, de, fr, it přes `titulky.py`; zbytek (pl, id, tr, uk, vi, fi, en-US) doklikal uživatel ve Studiu — přes API neověřeno (kvóta) |
| americká stopa | ✅ uživatel ve Studiu |
| závěrečná obrazovka | ✅ uživatel ve Studiu |
| playlist | `jazyky` v `playlisty.json`; uživatel doklikal ve Studiu (`playlisty.py` je idempotentní, nic nezdvojí) |

**Co musí uživatel naklikat sám:** nahrát MP4 ve Studiu (průvodce vyřídí
prohlášení o AI a osvědčení o zproštění), závěrečnou obrazovku a americkou
audiostopu (`render/audio-en-US.m4a`).

Stopáž 7:58 (`work/timing.json` total 477,8 s).

> Kdyby se znovu pouštěl `tts.py`, přepočítej kapitoly tady
> i v `youtube-preklady.md` a přegeneruj `en-US` přes `us_stopa.py`.

Pořadí podle CENY (`docs/zverejneni.md`):

```bash
V=videos/106-why-does-english-need-do
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
Why Does English Need "Do" to Ask a Question?
```

> Wh-otázka, 45 znaků, pracovní název videa od založení.

---

## 2. Popis

```
"Why do you do that?" One "do" is the thing you're doing. The other one isn't doing anything at all. So why does English insist on it? Shakespeare didn't always bother, and a thousand years ago nobody did.

From a Latin schoolbook glossed in Old English to Chaucer's four negatives in one sentence, from a 13th-century poem that needed a rhyme to the King James Bible's "and he did eat": how an ordinary verb crept into English questions, spread into plain statements, retreated again, and ended up doing a job nobody ever designed.

Sources: Alvar Ellegård, The Auxiliary Do (1953); Anthony Kroch, Reflexes of grammar in patterns of language change (1989); Anthony Warner, Why DO dove (2005); Otto Jespersen, Negation in English and Other Languages (1917); Phillip Wallage (2008) on Middle English negation; David Denison, English Historical Syntax (1993); Johan van der Auwera & Inge Genee (2002) on English do and Celtic; Ælfric's Colloquy (Old English gloss, 11th century); Chaucer, General Prologue; King Horn; Shakespeare, Hamlet and Macbeth (Folger editions); King James Bible (1611); William Tyndale's Pentateuch (1530); Jon Nielson & Royal Skousen (1998) on Tyndale and the King James Bible.

Subtitles are written for this video, not auto-generated. An American English audio track is available as a second audio track.

CHAPTERS
00:00 Two "do"s in one question
00:27 Shakespeare used both
01:25 Questions a thousand years ago
02:31 How "not" started as "nothing"
03:58 Where did "do" come from?
05:04 "Do" in plain statements
06:23 Why it stuck
07:12 Nobody chose it

IMAGE CREDITS
All archive images are in the public domain: the Droeshout portrait of Shakespeare (1623), the King James Bible title page (1611), the Knight from the Ellesmere Chaucer, Matthew Paris's map of Britain (c. 1250) and Pieter Bruegel the Elder's Netherlandish Proverbs (1559), via Wikimedia Commons.
```

> **Blok se kopíruje CELÝ** (`docs/zverejneni.md`). Povinný kredit
> není žádný — všech pět archivních snímků je public domain
> (`sources.json`), vypsané jsou jen kvůli divákovi.
>
> **Pointa se neprozrazuje.** Popis neříká, PROČ *do* zůstalo (ztráta
> pohybu slovesa, S52), jen že „nobody ever designed" — to je tvrzení
> z úvodu i závěru.
>
> Kapitoly ze scén S01, S05, S11, S19, S31, S40, S50, S56
> (`work/timing.json`, zaokrouhleno dolů). Nejkratší 45 s (S56 → konec),
> všechny ≥ 10 s, první na 00:00. Výzva k odběru S10b (1:17) leží
> v kapitole „Shakespeare used both".
>
> Zdroje podle `factcheck.md` a `podklady-historie.md`. Název Warnera
> 2005 ověřen na White Rose eprints: *Why DO dove: Evidence for register
> variation in Early Modern English negatives*.

---

## 3. Náhled

✅ **C1 „ENGLISH / WHY TWO DOs?“** (vybral uživatel 2026-10-13, otázka
bez uvozovek a menší nadpis). Kresleno kódem (`thumbnail/gen.py`), klíč
`thumbnail` v `project.json`, soubor `render/thumbnail.jpg`. Koncepty
v `thumbnail/KONCEPTY.md`.

---

## 4. Titulky

`subtitles/*.srt`, 14 jazyků + `en-US`. Jazyk videa **`en-gb`** (hlas
`bf_emma`) se musí nastavit dřív, než se nahrají titulkové stopy.
Codex na všech 13 překladech proběhl (`work/codex-*.txt`) a nálezy jsou
zapracované (`codex-zapracovano.md`), takže titulky a lokalizace můžou
nahoru hned po `nahraj.py`.

---

## 5. Nastavení

| | |
|---|---|
| kategorie | **Science & Technology** (28) — posílá `nahraj.py` napevno |
| jazyk videa | `en-gb` |
| licence | standardní |
| pro děti | **ne** |
| komentáře | zapnuté |
| **byla použita AI** | **ne** (návrh, rozhoduje uživatel). Všechny scény kromě pěti jsou kreslené kódem, pět archivních snímků je jen barevně upravených (*color adjustment* je výslovná výjimka). **Žádná scéna ze SDXL.** Hudba je procedurální, hlas není klon. |

### Závěrečná obrazovka

Plných 20 s, **od 7:38** (S59–S61). `zaver_check.py`: S59–S61 OK, prvky
patří do **horní poloviny**, spodní rohy zabírá titulek.

---

## 6. Tagy

```
english grammar, do-support, history of english, english language history,
old english, middle english, shakespeare english, king james bible, chaucer,
linguistics, language change, why does english use do, auxiliary verbs,
jespersen cycle, etymology, science explainer, there's more to it
```

---

## 7. Playlist

Navrženo **`jazyky`** („Languages — Why We Speak the Way We Do"), vedle
048 a 087. Dopiš slug do `playlisty.json`, spusť `analytics.py --videa`
a pak `tools/playlisty.py`.
