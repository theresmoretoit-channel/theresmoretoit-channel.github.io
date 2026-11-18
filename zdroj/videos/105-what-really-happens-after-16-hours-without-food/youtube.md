# YouTube — 105 „What Really Happens After 16 Hours Without Food?"

Stav: **hotovo** (2026-10-13). Americkou stopu, závěrečnou obrazovku a zveřejnění naklikal uživatel ve Studiu.

| | |
|---|---|
| ID videa | **`cF8naUcI_NQ`** — https://www.youtube.com/watch?v=cF8naUcI_NQ |
| master | ✅ `render/final-en-105.mp4` (1920×1080, 8:17) |
| náhled | ✅ od 2026-10-14 hotový obrázek od uživatele `16 HOURS / REPAIR MODE ON?`, talíř jako hodiny (`thumbnail/PUVOD.md`); 13.–14. 10. běželo pod kresleným C3 `16 HOURS / SELF-CLEANING?` — **při srovnání CTR dělit k tomuto datu** |
| nastavení, popis, tagy | ✅ `nahraj.py --k-videu --bez-titulku` 2026-10-13; ověřeno `videos.list`: 17 tagů, jazyk en-GB, vkládání zapnuté |
| lokalizace | ✅ 13 jazyků nahráno 2026-10-13 |
| titulky | ✅ všech 15 stop (14 jazyků + `en-US`) 2026-10-13; ASR v té chvíli ještě nebyl — kdyby se objevil, `titulky.py $V --smaz-asr` |
| americká stopa | ✅ uživatel ve Studiu |
| závěrečná obrazovka | ✅ uživatel ve Studiu |
| playlist | ✅ `telo`, pozice 5 (`playlisty.py`) |

**Co musí uživatel naklikat sám:** nahrát MP4 ve Studiu (průvodce vyřídí
prohlášení o AI a osvědčení o zproštění), závěrečnou obrazovku a americkou
audiostopu (`render/audio-en-US.m4a`).

Stopáž 8:17 (`work/timing.json` total 496,9 s, `ffprobe` 496,9 s).

> Kdyby se znovu pouštěl `tts.py`, přepočítej kapitoly tady
> i v `youtube-preklady.md` a přegeneruj `en-US` přes `us_stopa.py`.

Pořadí podle CENY (`docs/zverejneni.md`):

```bash
V=videos/105-what-really-happens-after-16-hours-without-food
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
What Really Happens After 16 Hours Without Food?
```

> Wh-otázka, 48 znaků, pracovní název videa od založení. Číslice 16
> v titulu sedí s náhledem („16 HOURS").

---

## 2. Popis

```
Stop eating for sixteen hours, says the internet, and your cells switch into a built-in repair mode called autophagy, the process behind the 2016 Nobel Prize. But where does that sixteen actually come from? And has anyone ever measured it in a human being?

From a 16:8 meal schedule and a fasting guide that cites a study on mice, to Christian de Duve's lysosome, Yoshinori Ohsumi's starving yeast, mice that went two days without food and the first attempts to measure autophagy in human blood: what the evidence behind the sixteen-hour number actually shows.

Sources: Nobel Prize in Physiology or Medicine 2016 (press release and scientific background); Martin Berkhan, The Leangains Guide (2010); Lasta, fasting timeline (2024); Takeshige et al. 1992 and Tsukada & Ohsumi 1993 (yeast); Kuma et al. 2004 and Komatsu et al. 2005 (newborn mice); Mizushima et al. 2004 and Alirezaei et al. 2010 (fasting mice); Perlman 2016 and Carper et al. 2020 (mouse metabolism); Klionsky et al. 2021 (autophagy guidelines); Jamshed et al. 2019, Singh et al. 2025 and Bensalem et al. 2025 (human studies); Guido Kroemer interviewed by Rhonda Patrick, FoundMyFitness (2019); Hara et al. 2006, Komatsu et al. 2006 and Pyo et al. 2013 (brain and lifespan); Qu et al. 2003, Yue et al. 2003 and Yang et al. 2011 (cancer); Anton et al. 2018 (metabolic switch).

Subtitles are written for this video, not auto-generated. An American English audio track is available as a second audio track.

Full transcript, sources and translations: https://theresmoretoit-channel.github.io/videos/what-really-happens-after-16-hours-without-food/

CHAPTERS
00:00 The sixteen-hour promise
00:33 Following the number back
01:39 How a cell takes out the trash
02:38 A body that can't do without it
03:05 Ohsumi's starving yeast
03:49 Two days without food, for a mouse
04:50 Looking inside a human
05:27 What the human studies found
06:10 Asking an expert directly
06:31 Longer life, and cancer
07:30 So what really happens?

IMAGE CREDITS
Nobel Laureates 7428 (30679389523) (cropped) — Bengt Nyman from Vaxholm, Sweden, CC BY 2.0, via Wikimedia Commons (colour adjusted)
Licence: creativecommons.org/licenses/by/2.0
All other archive images are in the public domain.
```

> **Blok se kopíruje CELÝ** (`docs/zverejneni.md`). Povinný kredit je
> jediný: S04 (Ósumi, CC BY 2.0). S21 (de Duve) je CC0 a S30 (myš)
> public domain — S30 navíc vyretušovaná, což u PD atribuci nevyžaduje
> (popis retuše je v `LICENSES.md`).
>
> **Pointa se neprozrazuje.** Popis klade obě otázky z S05 a končí
> „what the evidence… actually shows", ne odpovědí. Kapitola u S46 se
> proto jmenuje „Asking an expert directly", ne „We don't know".
>
> Kapitoly jsou ze scén S01, S06, S14, S22, S25, S30, S37, S42, S46,
> S49, S57 (`work/timing.json`, zaokrouhleno dolů). Nejkratší je 21 s
> (S46 → S49), poslední 46 s; všechny ≥ 10 s, první na 00:00. Výzva
> k odběru S13b (1:31) leží v kapitole „Following the number back".
>
> Zdroje podle `factcheck.md` (podrobnosti v `podklady-pust.md`
> a `podklady-biologie.md`). **Leangains a Lasta jsou ve videu
> anonymní** („one guide", „one popular fasting guide") — v popisu
> jmenované, aby šlo tvrzení S08–S10 ověřit. Kdybys je jmenovat nechtěl,
> stačí škrtnout dvě položky tady i ve 13 překladech.

---

## 3. Náhled

✅ **C3 „16 HOURS / SELF-CLEANING?"** (vybral uživatel 2026-10-13;
agent doporučoval C2 talíř). Kresleno kódem (`thumbnail/gen.py`), klíč
`thumbnail` v `project.json`, soubor `render/thumbnail.jpg`. Koncepty
v `thumbnail/KONCEPTY.md`. C3 je ve 150 px nejabstraktnější ze tří —
až přijde CTR, porovnat.

---

## 4. Titulky

`subtitles/*.srt`, 14 jazyků + `en-US`. Jazyk videa **`en-gb`** (hlas
`bf_emma`) se musí nastavit dřív, než se nahrají titulkové stopy.
Codex na všech 13 překladech proběhl (`work/codex-*.txt`) a nálezy jsou
zapracované, takže titulky a lokalizace můžou nahoru hned po `nahraj.py`.

---

## 5. Nastavení

| | |
|---|---|
| kategorie | **Science & Technology** (28) — posílá `nahraj.py` napevno |
| jazyk videa | `en-gb` |
| licence | standardní |
| pro děti | **ne** |
| komentáře | zapnuté |
| **byla použita AI** | **ne** (návrh, rozhoduje uživatel). 62 scén je kreslených kódem, tři archivní snímky jsou barevně upravené (*color adjustment* je výslovná výjimka), u S30 navíc retuš drobků klonem z téže fotky. Žádná scéna ze SDXL. Hudba je procedurální, hlas není klon. |

### Závěrečná obrazovka

Plných 20 s, **od 7:57** (S60–S63). `zaver_check.py`: S60–S63 OK, prvky
patří do **horní poloviny**, spodní rohy zabírá titulek.

---

## 6. Tagy

```
autophagy, intermittent fasting, 16:8 fasting, 16 hour fast, time-restricted eating,
fasting autophagy, Yoshinori Ohsumi, Nobel Prize 2016, Christian de Duve, lysosome,
autophagosome, cell biology, fasting myths, Guido Kroemer, nutrition science,
science explainer, there's more to it
```

---

## 7. Playlist

Navrženo **`telo`** („Your Body, and How Long It Lasts"): buněčná údržba,
stárnutí a rakovina sedí přesně na popis playlistu (sloni a rakovina,
stárnutí, tělo jako kód). Dopiš slug do `playlisty.json`, spusť
`analytics.py --videa` a pak `tools/playlisty.py`.
