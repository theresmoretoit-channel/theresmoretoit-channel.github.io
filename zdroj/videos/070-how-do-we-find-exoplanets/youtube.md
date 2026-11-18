# YouTube — 070 „How Do We Find Exoplanets?"

Stav: **připraveno k nahrání** (2026-09-28): master, náhled, titulky
15 jazyků. Titulky a lokalizace až po Codexu. Stav zveřejnění se vede v `Témata.ods`.

| | |
|---|---|
| video | `render/final-en-070.mp4` (master 1920×1080, 10:46, −14,0 LUFS) |
| náhled | `render/thumbnail.jpg` — koncept **C3** „EXOPLANETS / WHAT MADE THIS DIP?“ |
| titulky | `subtitles/*.srt`, 14 jazyků + `en-US`  |
| americká stopa | `render/audio-en-US.m4a` — nahrát ve Studiu |
| lokalizace | `youtube-preklady.md` |

**Co musí uživatel naklikat sám:** nahrát MP4 ve Studiu (průvodce vyřídí
prohlášení o AI a osvědčení o zproštění), americkou audiostopu
a závěrečnou obrazovku (API na ni nemá zdroj).

Pořadí podle CENY (`docs/zverejneni.md`); `lokalizace.py` a `titulky.py`
až po zapracování nálezů Codexu k překladům:

```bash
V=videos/070-how-do-we-find-exoplanets
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
How Do We Find Exoplanets?
```

> wh-otázka („How…") — podle `docs/kanal-metriky.md` nejlepší CTR
> (2,23 % proti 1,21 % u ano/ne otázky). Titul je zároveň název projektu
> a nadpis `script.md`. Odpověď (měří se účinky, ne planeta) nevyzrazuje.

---

## 2. Popis

```
Planets outside our Solar System are everywhere. And yet we can barely
see them. A planet is incredibly faint next to its star, and from dozens
or hundreds of light-years away the two blur into almost a single point
of light.

So how do astronomers find planets they usually cannot see? Mostly, they
don't look for the planet itself. They look for what it does to
everything around it.

A planet crossing in front of its star makes it slightly dimmer — for an
Earth-sized planet and a Sun-like star, by about one part in twelve
thousand. A planet makes its star move and shifts the lines in its
spectrum. It can distort the light of a distant background star. And its
atmosphere can leave a fingerprint in starlight. We go through the
methods one by one, and look at what happens when two of them see the
same planet.

Subtitles are written for this video, not auto-generated. An American
English audio track is available as a second audio track.

Full transcript, sources and translations: https://theresmoretoit-channel.github.io/videos/how-do-we-find-exoplanets/

CHAPTERS
00:00 A strange problem
00:53 Direct imaging
01:50 A single point of light
02:21 Waiting for a transit
04:13 Without waiting for a transit
04:49 Starlight and the Doppler effect
05:47 Combining two methods
06:17 What is it made of?
06:55 Gravitational microlensing
08:11 Reading an atmosphere
09:16 Back to the original question
09:50 What "discovered" really means

IMAGE CREDITS
Webb Takes Its First Exoplanet Image (HIP-65426b) — NASA/ESA/CSA, A Carter (UCSC), the ERS 1386 team, and A. Pagan (STScI), CC BY 4.0
via Wikimedia Commons
Licence: creativecommons.org/licenses/by/4.0

All other images are diagrams drawn for this video.
```

> **Blok se kopíruje CELÝ** (`docs/zverejneni.md`). Jediná povinná
> atribuce je UVNITŘ: S10 (snímek HIP 65426 b z JWST, CC BY 4.0), TASL
> podle `sources.json`. Jiný archivní snímek video nemá (storyboard:
> 55 × `svg`, 1 × `archive`, žádné SDXL), proto místo věty o volném díle
> věta o diagramech.
>
> Kapitoly: první na 00:00, dvanáct, nejkratší 30 s (S27→S32 je 58 s,
> S10→S13 31 s, S34→S37 38 s), časy = začátky scén z `work/timing.json`
> zaokrouhlené dolů: S01, S06, S10, S13, S23, S27, S32, S34, S37, S44,
> S49, S52. Poslední kapitola do konce trvá 55 s.
>
> Čísla v popisu: „one part in twelve thousand" je S17 (1 / 0,00008386
> = 11 924, viz `factcheck.md`), „dozens or hundreds of light-years" S03.

---

## 3. Náhled

Vybrán koncept **C3** (uživatel 2026-09-28): světelná křivka s poklesem
a otazníkem, „EXOPLANETS / WHAT MADE THIS DIP?“. Kreslený kódem
(`thumbnail/c3-krivka.svg`, `--bg none`), varianta zapsaná v `project.json`.
Zamítnuté C1 (záře hvězdy) a C2 (otazník na dráze), kontaktní list
`thumbnail/kontakt-150-210.png`. Jas 39,6, kontrast 62,8 (pásmo kanálu).

---

## 4. Titulky

`subtitles/*.srt`, 14 jazyků + `en-US`. Jazyk videa **`en-gb`** (hlas
`bf_emma`) se musí nastavit dřív, než se nahrají titulkové stopy.

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

Rozhoduje fotorealističnost. Video **nemá žádnou SDXL scénu** (dva
pokusy u S08 zamítnuty, viz `notes.md`): 55 scén je kreslených kódem,
jediná archivní fotografie S10 (JWST) je jen vsazená do rámu bez retuše,
hudba je procedurální. Žádný fotorealistický generovaný obsah ani
klonovaný hlas.

### Závěrečná obrazovka

Storyboard rezervuje v S52–S55 horní polovinu pro karty (video vlevo
nahoře, odběr vpravo nahoře); dole je titulek. `zaver_check.py` se
skutečným timingem ověřit na masteru.

---

## 6. Tagy

```
exoplanets, how do we find exoplanets, exoplanet detection, transit method,
radial velocity method, doppler spectroscopy, gravitational microlensing,
direct imaging, coronagraph, james webb space telescope, HIP 65426 b,
kepler, tess, transmission spectroscopy, astronomy, space, explainer,
there's more to it
```

---

## 7. Playlist

Patří do `vesmir` („Space — Getting There, and Who Else Is Out There").
Dopiš slug `070-how-do-we-find-exoplanets` do `playlisty.json`, spusť
`analytics.py --videa` a pak `tools/playlisty.py`.
