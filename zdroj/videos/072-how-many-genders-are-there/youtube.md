# YouTube — 072 „How Many Genders Are There?"

Stav: **nahráno** (2026-09-29) — https://youtu.be/By4niuZ7aWI; metadata, náhled, 13 lokalizací, 15 titulkových stop, playlisty `spolecnost` a `bezne`.
Stav zveřejnění se vede v `Témata.ods`.

| | |
|---|---|
| video | `render/final-en-072.mp4` (master, 9:40,8) |
| náhled | `render/thumbnail.jpg` — ✅ C1 formulář (vybral uživatel 2026-09-29) |
| titulky | `subtitles/*.srt`, 14 jazyků + `en-US` |
| americká stopa | `render/audio-en-US.m4a` — nahrát ve Studiu |
| lokalizace | `youtube-preklady.md` |

**Co musí uživatel naklikat sám:** nahrát MP4 ve Studiu (průvodce vyřídí
prohlášení o AI a osvědčení o zproštění), americkou audiostopu
a závěrečnou obrazovku (API na ni nemá zdroj).

Pořadí podle CENY (`docs/zverejneni.md`); `lokalizace.py` a `titulky.py`
**až po zapracování nálezů Codexu**:

```bash
V=videos/072-how-many-genders-are-there
python tools/nahraj.py $V --k-videu <ID> --bez-titulku   # 100
python tools/analytics.py --videa                        #   1  ← nutné
python tools/lokalizace.py $V                            #  50
python tools/titulky.py $V --smaz-asr                    # 150  ← před titulky
python tools/titulky.py $V                               # 400×15
python tools/playlisty.py                                # 100
```

---

## 1. Titul

```
How Many Genders Are There?
```

> wh-otázka („How many…") — podle `docs/kanal-metriky.md` nejlepší CTR.
> Neprozradí odpověď (že číslo závisí na tom, co se počítá).

---

## 2. Popis

```
Two? Fifty-five? Hundreds? Before anyone can give a number, there is an
earlier question: what exactly are we counting?

We separate the things the word "gender" often gets stretched to cover —
reproductive roles, individual sex characteristics, social expectations,
gender identity and gender expression — and look at what can and can't be
counted in each of them. Along the way: Facebook's sixty custom gender
options in 2014, what complete androgen insensitivity syndrome shows about
chromosomes and anatomy, why an infertile man doesn't stop being male, and
why three labels on a form don't automatically mean three genders.

This video isn't trying to settle every argument about sex and gender. It
tries to make sure both sides are answering the same question.

Subtitles are written for this video, not auto-generated. An American
English audio track is available as a second audio track.

Full transcript, sources and translations: https://theresmoretoit-channel.github.io/videos/how-many-genders-are-there/

CHAPTERS
00:00 Two, fifty-five, or hundreds?
01:00 Sixty options on Facebook
01:32 Body, expectations, identity
01:52 Sperm, eggs and reproductive roles
02:46 How bodies develop
03:10 When chromosomes don't tell the whole story
04:14 Gender roles
04:51 Gender identity
05:36 Gender expression
06:04 Counting the labels
06:57 Colours, and the limits of an analogy
07:23 "But people invented these words"
07:47 What makes someone a woman?
08:43 So how many genders are there?
```

> **Blok se kopíruje CELÝ** (`docs/zverejneni.md`). Video nemá žádný
> archivní snímek (50 scén, všechny kreslené kódem), takže kredity nejsou.
>
> Kapitoly: první na 00:00, každá ≥ 10 s, časy z `work/timing.json`
> (začátky scén S01, S06, S09, S10, S15, S17, S22, S25, S28, S30, S34, S36,
> S38, S43).

---

## 3. Náhled

Tři koncepty kreslené kódem (`thumbnail/gen.py`), všechny s nadpisem
**GENDERS** a otázkou; žádný neprozradí pointu („…of what?") ani se
nepostaví za žádné číslo:

| | obraz | otázka |
|---|---|---|
| C1 `render/thumb-c1-formular.jpg` | formulář se zaškrtávacími políčky, pokračuje pod okraj | HOW MANY BOXES? |
| C2 `render/thumb-c2-cisla.jpg` | tři rovnocenná čísla 2 · 55 · ∞ | WHICH ONE? |
| C3 `render/thumb-c3-carky.jpg` | čárky na počítání a otazník | HOW MANY? |

**Vybrán C1** (uživatel 2026-09-29), zapsán v `project.json`; C2 a C3 zůstávají pro případný Test & Compare.

---

## 4. Titulky

`subtitles/*.srt`, 14 jazyků + `en-US`. Jazyk videa **`en-gb`** (hlas
`bf_emma`) se musí nastavit dřív, než se nahrají titulkové stopy.

---

## 5. Nastavení

| | |
|---|---|
| kategorie | Education |
| jazyk videa | `en-gb` |
| licence | standardní |
| pro děti | **ne** |
| komentáře | zapnuté — téma je sporné, počítej s moderováním |

### Prohlášení o AI: **ne**

Rozhoduje fotorealističnost. Video **nemá žádnou SDXL scénu ani archivní
snímek**: všech 50 scén je kresleno kódem, hudba je procedurální, hlas je
syntetický vypravěč, nikoli klon skutečné osoby.

### Závěrečná obrazovka

Posledních 20 s jsou S45–S47; horní rohy jsou volné (`zaver_check.py`),
dole je titulek diagramu. Dlaždici i kolečko dej do **horní** poloviny.

---

## 6. Tagy

```
how many genders are there, gender, sex, gender identity, biological sex,
intersex, non-binary, transgender, cisgender, gender roles, gender
expression, androgen insensitivity syndrome, gametes, facebook gender
options, explainer, there's more to it
```

---

## 7. Playlist

Po zveřejnění dopiš slug do `playlisty.json` — sousední téma 064 je
v `spolecnost` i `bezne`, 072 patří nejspíš do obou — spusť
`analytics.py --videa` a pak `tools/playlisty.py`.
