# YouTube — 068 „Why Do People Still Believe in God?"

Stav: **VIDEO NAHRÁNO** (ID níže); zbývá metadata, lokalizace, titulky —
**až po Codexu**.

| | |
|---|---|
| ID videa | `MeOQtxC7FY4` (https://www.youtube.com/watch?v=MeOQtxC7FY4) |
| nastavení, popis, tagy, náhled | ⬜ `nahraj.py --k-videu MeOQtxC7FY4 --bez-titulku` |
| lokalizace | ⬜ 14 jazyků jedním voláním (`lokalizace.py`) |
| titulky | ⬜ 15 stop (en, cs, sv, es, pt-BR, de, fr, it, pl, id, tr, uk, vi, fi, en-US) |
| automatický přepis | ⬜ za pár dní `titulky.py $V --smaz-asr` |
| playlist | ⬜ dopsat slug do `playlisty.json`, `analytics.py --videa`, `playlisty.py` |
| závěrečná obrazovka, americká stopa | ⬜ uživatel ve Studiu |

**Co musí uživatel naklikat sám:** závěrečnou obrazovku (API na ni nemá zdroj)
a nahrát americkou audiostopu (`render/audio-en-US.m4a`). Prohlášení o AI
a osvědčení o zproštění vyřídil průvodce při ručním nahrání MP4.

Pořadí podle CENY (`docs/zverejneni.md`) — **až po zapracování Codexu:**

```bash
V=videos/068-why-do-people-still-believe-in-god
python tools/nahraj.py $V --k-videu MeOQtxC7FY4 --bez-titulku   # 100
python tools/analytics.py --videa                              #   1  ← nutné
python tools/lokalizace.py $V                                  #  50
python tools/titulky.py $V --smaz-asr                          # 150  ← před titulky
python tools/titulky.py $V                                     # 400×15
python tools/playlisty.py                                      # 100
```

---

## 1. Titul

```
Why Do People Still Believe in God?
```

> wh-otázka („Why…") — podle `docs/kanal-metriky.md` nejlepší CTR (2,23 %
> proti 1,21 % u ano/ne otázky). Titul je zároveň hlavní otázka videa a
> náhled ji NEodpovídá.

---

## 2. Popis

```
We can see galaxies billions of light-years away. We can edit DNA. We can
explain lightning, disease, evolution and the history of the universe.

And yet billions of people still believe in God. Why?

Maybe science didn't simply fail to replace religion. Maybe we were
expecting it to answer a question it was never designed to answer. This
video looks at why belief persists even in an age of science: the
difference between explaining HOW something happens and WHY it exists, a
pattern-seeking brain that keeps asking "who caused this?", a strange
experiment where atheists' bodies reacted to daring God, death and the
search for meaning, religion as a social system, what scientists actually
believe — and where science and religion do, and don't, overlap.

Science can tell us how the universe works. Whether it has a purpose is a
different kind of question — and that one is still open.

Subtitles are written for this video, not auto-generated. An American
English audio track is available as a second audio track.

Full transcript, sources and translations: https://theresmoretoit-channel.github.io/videos/why-do-people-still-believe-in-god/

CHAPTERS
00:00 Science explains almost everything
00:33 A world full of mysteries
00:56 Science takes the mysteries apart
01:26 Explaining how, not why
02:05 Brains that see patterns
02:42 Belief you might not notice
03:24 And then there is death
04:16 Religion as a social system
05:05 Even in how we imagine the future
06:03 A march away from superstition?
06:29 What scientists actually believe
07:23 When claims can be tested
07:58 We want stories
09:14 What did we expect science to replace?

IMAGE CREDITS
Galaxy cluster Abell 1689 — NASA/GSFC (public domain)
Mass at Puerto Princesa Cathedral — Joshua T. Garcia (CC0)
Licence: creativecommons.org/publicdomain/zero/1.0/
```

> **Blok se kopíruje CELÝ** (`docs/zverejneni.md`) — atribuce jsou UVNITŘ.
> S10 (NASA/GSFC) je volné dílo US Government, S41 je CC0 — ani jedno
> nevyžaduje uvedení autora, uvádí se z korektnosti (TASL). Žádný jiný
> archivní snímek ve videu není.

---

## 3. Náhled

`render/thumbnail.jpg` — **hotový** (koncept C1, sepjaté ruce + teplá zář,
„GOD / WHY STILL BELIEVE?"). Zdroj `thumbnail/c1-amber.svg` přes
`thumbnail/gen.py`; kontrola `thumb_check.py` — leží uprostřed pásma kanálu.

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

Rozhoduje fotorealističnost, ne použití AI. Video má 3 SDXL scény (S05
bouře, S37 dveře světla, S51 lodě) v **malovaném** stylu (kotva stylu,
ne fotorealismus), 2 barevně upravené archivní fotografie (výjimka „color
adjustment") a zbytek kreslený kódem; hudba je procedurální. Žádný
fotorealistický generovaný obsah, žádné konkrétní skutečné místo/událost
v generované scéně, žádný klonovaný hlas.

### Závěrečná obrazovka

Poslední scény (S93/S94/S95) mají horní část volnou — dlaždici dalšího
videa i kolečko odběru dej do **horní** poloviny (`zaver_check.py` ověřeno).

---

## 6. Tagy

```
why do people believe in god, science and religion, belief in god,
religion, atheism, meaning of life, death and meaning, philosophy of
religion, secularization, cognitive science of religion, does science
disprove god, faith, battlestar galactica, existential questions,
explainer, there's more to it
```

---

## 7. Playlist

Dopiš slug do `playlisty.json` (soused podle tématu — věda a společnost /
velké otázky), spusť `analytics.py --videa` a pak `tools/playlisty.py`.
