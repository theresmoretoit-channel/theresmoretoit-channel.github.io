# YouTube — 114 „Why Haven't We Found a Fourth Spatial Dimension?“

Stav: **nahráno 2026-10-17** (https://www.youtube.com/watch?v=FniptDcBhbk). Přes API
nastavení, popis a tagy 10-17; lokalizace (13 jazyků), náhled, titulky (15 stop)
a playlist 2026-10-18. Závěrečná obrazovka a US stopa naklikané, zveřejnění naplánované (10-18). Stav zveřejnění je v `Témata.fods`.

| | |
|---|---|
| ID videa | `FniptDcBhbk` |
| master | ✅ `render/final-en-114.mp4` (6:56, 1920×1080, 31 MB, render 2026-10-17 na .207, `ffmpeg -v error` čistý) |
| náhled | `render/thumbnail.jpg` (4D SPACE / WHY DOES THIS WIN?, lednice) — `thumbnail/PUVOD.md`; na YouTube od 2026-10-18 |
| nastavení, popis, tagy | podklady níž |
| lokalizace | `youtube-preklady.md`, 13 jazyků, prošlo Codexem (42 oprav) |
| titulky | `subtitles/*.srt`, 14 jazyků + `en-US`, všechny překlady prošly Codexem |
| americká stopa | `render/audio-en-US.m4a`, ručně ve Studiu |
| závěrečná obrazovka | ručně ve Studiu |
| karta | žádná (viz níž) |
| playlist | `fyzika`, za 113 |

**Co musí uživatel naklikat sám:** nahrát MP4 ve Studiu (průvodce vyřídí
prohlášení o AI a osvědčení o zproštění), závěrečnou obrazovku
a americkou audiostopu (`render/audio-en-US.m4a`). A **ve 113 vyměnit
dlaždici závěrečné obrazovky** z 008 na tohle video — 113 končí
*„That's where we're going next.“*

Stopáž 6:56 (`work/timing.json` total 416,1 s).

> Kdyby se znovu pouštěl `tts.py`, přepočítej kapitoly tady
> i v `youtube-preklady.md` a přegeneruj `en-US` přes `us_stopa.py`.

Pořadí podle CENY (`docs/zverejneni.md`):

```bash
V=videos/114-why-havent-we-found-a-fourth-dimension
python tools/nahraj.py $V --k-videu=<ID> --bez-titulku    # 100
python tools/analytics.py --videa                         #   1  ← nutné
python tools/lokalizace.py $V                             #  50
python tools/titulky.py $V --smaz-asr                     # 150  ← před titulky
python tools/titulky.py $V                                # 400×15
python tools/playlisty.py                                 #  50
# 2026-10-17 nahraj.py, analytics, --smaz-asr; 2026-10-18 zbytek (vč. náhledu)
# úklid, až je MP4 na YouTube:
rm $V/render/draft*.mp4
ssh vrana@192.168.0.207 'rm -rf /home/vrana/temp/render-114-why-havent-we-found-a-fourth-dimension'
```

---

## 1. Titul

```
Why Haven't We Found a Fourth Spatial Dimension?
```

> Wh-otázka, 48 znaků, shodná s `project.json`. „Spatial“ zůstává,
> protože samotné *fourth dimension* se čte jako čas a 113 začíná
> *„Not time.“* Odpověď (tři testy nic nenašly, zbývá stočený rozměr)
> titul neprozrazuje.

---

## 2. Popis

```
Close the door of your room and the air stays inside. It doesn't seep away in a direction you can't point to. That sounds too obvious to say, until you remember the question from last time: if space had a fourth direction, why isn't everything leaking into it?

The best clue may be hanging on your fridge. A small magnet holding up a sheet of paper beats the gravity of the entire Earth. Physicists call this the hierarchy problem, and in 1998 three of them proposed that gravity only looks weak because part of it spreads into dimensions we can't see. That idea makes predictions, and physicists have checked them three ways: a twisting disc in a lab in Seattle, particle collisions at the Large Hadron Collider, and a ripple in space from two neutron stars that merged 130 million light-years away. Here's what each test looked for, and where a fourth dimension could still be hiding.

Part one: What If Space Had a Fourth Dimension? https://www.youtube.com/watch?v=dXqHZlOilZY

Sources: Arkani-Hamed, Dimopoulos & Dvali, Phys. Lett. B 429, 263 (1998; arXiv hep-ph/9803315); Lee et al., Phys. Rev. Lett. 124, 101101 (2020); Dimopoulos & Landsberg, Phys. Rev. Lett. 87, 161602 (2001); CMS, JHEP 08 (2026) 098 (arXiv:2604.10732); ATLAS, Phys. Rev. D 103, 112006 (2021); LIGO/Virgo, Phys. Rev. Lett. 119, 161101 (2017); LIGO/Virgo, Fermi GBM & INTEGRAL, ApJL 848, L13 (2017); Pardo, Fishbach, Holz & Spergel, JCAP 07 (2018) 048 (arXiv:1801.08160); E. A. Abbott, Flatland (1884).

Subtitles are written for this video, not auto-generated. An American English audio track is available as a second audio track.

Full transcript, sources and translations: https://theresmoretoit-channel.github.io/videos/why-havent-we-found-a-fourth-dimension/

CHAPTERS
00:00 Why doesn't the air leak out?
00:48 A clue on your fridge
01:02 A trillion trillion trillion times
01:18 An idea from 1998
01:57 What it predicts
02:28 Test one: gravity on a lab bench
03:16 Test two: the Large Hadron Collider
04:11 Test three: two neutron stars
05:14 The scorecard
05:32 The oldest hiding place
06:02 String theory
06:18 Footprints, not visitors

IMAGE CREDITS
Views of the LHC tunnel sector 3-4 — Maximilien Brice (CERN), CC BY-SA 3.0
Composite of images of NGC 4993 and kilonova (eso1733r) — ESO/N.R. Tanvir, A.J. Levan and the VIN-ROUGE collaboration, CC BY 4.0
via Wikimedia Commons
Licences: creativecommons.org/licenses/by-sa/3.0, creativecommons.org/licenses/by/4.0
```

> **Blok se kopíruje CELÝ** (`docs/zverejneni.md`). Archivní snímky jsou
> dva (S22, S26) a oba povinně s atribucí (`CREDITS.md`), proto jsou
> uvnitř bloku.
>
> **Pointa se neprozrazuje.** Popis končí na *„what each test looked
> for“*, ne *found*: že ani jeden test únik nenašel, je výplata S25–S32.
> Kapitola *„The scorecard“* výsledek nejmenuje.
>
> Kapitoly ze scén S01, S06, S08, S10, S13, S17, S21, S26, S32, S34,
> S37, S38 (`work/timing.json`, zaokrouhleno dolů). Nejkratší 14 s
> (S06 → S08), všechny ≥ 10 s, první na 00:00. Výzva k odběru S12b
> (1:49) leží v kapitole „An idea from 1998“.
>
> Zdroje podle `factcheck.md` (citace jsou u jednotlivých scén). Čísla
> v popisu (1998, 130 milionů ly) jsou tatáž jako ve scénáři.
> **Seattleský tým se nejmenuje (Eöt-Wash)** ani v popisu — jméno nic
> nenese a ve zdrojích je pod Lee et al.

---

## 3. Náhled

`render/thumbnail.jpg` — 4D SPACE / WHY DOES THIS WIN? (červený magnet na lednici
drží list papíru). Hotový obrázek od uživatele (ChatGPT, zadání A), jen
zmenšený; původ a otisk v `thumbnail/PUVOD.md`, zadání v `thumbnail/ZADANI.md`.

---

## 4. Titulky

`subtitles/*.srt`, 14 jazyků + `en-US`. Jazyk videa **`en-gb`** (hlas
`bf_emma`) se musí nastavit dřív, než se nahrají titulkové stopy.
Nahrávají se až po zapracování nálezů Codexu.

---

## 5. Nastavení

| | |
|---|---|
| kategorie | **Science & Technology** (28) — posílá `nahraj.py` napevno |
| jazyk videa | `en-gb` |
| licence | standardní |
| pro děti | **ne** |
| komentáře | zapnuté |
| **byla použita AI** | **ne**. 40 scén je kreslených kódem, 2 archivní snímky (tunel LHC, NGC 4993 z ESO) jsou jen barevně upravené. SDXL ve videu není vůbec. Hudba je procedurální, hlas není klon. |

### Závěrečná obrazovka

Od **6:36** (posledních 20 s), tedy S39–S41. `zaver_check` u nich hlásí
volnou **horní polovinu** (dole je titulek), prvky patří **nahoru**.
Jako dlaždici dalšího videa doporučuju **113 *What If Space Had
a Fourth Dimension?*** — kdo přišel rovnou na druhý díl, první neviděl.

### Karta

Žádná. Jediné přirozené místo je S02 *„last time“* (0:10), a karta
v první půlminutě by posílala diváky pryč v okně, kde se rozhoduje,
jestli zůstanou. Odkaz na 113 je v popisu a na závěrečné obrazovce.

---

## 6. Tagy

```
fourth dimension, extra dimensions, hidden dimensions, hierarchy problem,
why is gravity so weak, large extra dimensions, inverse square law,
large hadron collider, lhc, micro black holes, missing energy,
gravitational waves, gw170817, neutron star merger, kaluza klein,
string theory, flatland, physics explainer, science explainer,
there's more to it
```

---

## 7. Playlist

`fyzika` (*Physics That Sounds Simple Until You Ask*), na konec, za 113.
Zapsáno v `playlisty.json`; `playlisty.py` ho přeskočí, dokud video
není v `analytics/videa.json`.
