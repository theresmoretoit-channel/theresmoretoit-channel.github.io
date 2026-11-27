# YouTube — 171 „Where Did the First Life Come From?“

Stav: **naplánováno na zveřejnění** (2026-11-27). Přes API nastavení, popis, tagy, lokalizace 13, titulky 15 stop (ASR nebyl). Ručně ve Studiu hotovo: závěrečná obrazovka, americká stopa. Draft schválený, `script 0.6`.

| | |
|---|---|
| ID videa | `x50jk9BuT6E` — https://www.youtube.com/watch?v=x50jk9BuT6E (MP4 nahrál uživatel 2026-11-26) |
| master | `render/final-en-171.mp4`, 644,9 s, 207, dekódování čisté, −14,0 LUFS, 70,4 MB |
| náhled | `render/thumbnail.jpg` — C1 (banán s octomilkami, `LIFE` / `FROM NOTHING?`) přes obrázkový nástroj, viz `thumbnail/PUVOD.md` |
| lokalizace | `youtube-preklady.md`, 13 jazyků |
| titulky | `subtitles/<kód>.srt`, 14 jazyků + `en-US`; překlady 1× Codex |
| americká stopa | `render/audio-en-US.m4a` (`af_heart` 0,9379), ručně ve Studiu |
| závěrečná obrazovka | S77–S78 (od 10:25), **horní polovina** (níž) |
| karty | žádné |
| playlist | **`vesmir`** (zařazeno 2026-11-26, potvrdil uživatel) |
| komentář kanálu | otázka ze S78, zapsaná v `pripnute-komentare.md` |
| shorty | zatím nejsou |

**Ručně ve Studiu:** závěrečná obrazovka, americká audiostopa, osvědčení o zproštění (pokud ho
nevyřídil průvodce) a po zveřejnění připnout komentář.

> Kdyby se znovu pouštěl `tts.py`, přepočítej kapitoly tady i v `youtube-preklady.md` a přegeneruj
> `en-US` přes `us_stopa.py`. Pozor: S70/S70b má u Emmy ruční zvuk (`zvuk/S70.py`).

```bash
V=videos/171-where-did-the-first-life-come-from
python tools/nahraj.py $V --k-videu=x50jk9BuT6E --bez-titulku         # 100
python tools/analytics.py --videa                              #   1  ← nutné
python tools/lokalizace.py $V                                  #  50
python tools/titulky.py $V --smaz-asr                          # 150  ← před titulky
python tools/titulky.py $V                                     # 400×N
python tools/playlisty.py                                      #  50
python tools/komentare.py --jen 171                            #  51  po zveřejnění (vloží i timer)
rm $V/render/draft*.mp4
ssh vrana@192.168.0.207 'rm -rf /home/vrana/temp/render-171-where-did-the-first-life-come-from'
```

---

## 1. Titul

```
Where Did the First Life Come From?
```

---

## 2. Popis

```
Leave a banana on the kitchen counter for a few days, and tiny flies turn up around it. For more than two thousand years, people took that as proof that life could simply start on its own: eels from mud, insects from dew, and even a seventeenth-century recipe for mice. It took sealed jars, gauze and a flask with a neck bent like a swan's to show that life only ever comes from life.

But that answer left a bigger question behind. If every living thing comes from another living thing, the chain has to start somewhere. This video follows how scientists have tried to get from chemistry to life: Darwin's warm little pond, Stanley Miller's sparks in a glass flask, amino acids in a meteorite that fell in Australia, and a molecule that can carry instructions and do work at the same time. And then it asks whether "the first life" is even the right way to put the question.

Sources: Aristotle, History of Animals; J. B. van Helmont, Ortus medicinae (1648; English edition Oriatrike, 1662); F. Redi, Experiments on the Generation of Insects (1668; transl. M. Bigelow, 1909); L. Pasteur, on organised corpuscles in the atmosphere (1861) and his Sorbonne lecture of 7 April 1864; C. Darwin, letter to J. D. Hooker, 1 February 1871 (Darwin Correspondence Project, DCP-LETT-7471); S. L. Miller, Science 117:528 (1953); Johnson et al., Science 322:404 (2008); Koga & Naraoka, Scientific Reports 7:636 (2017); Kruger et al., Cell 31:147 (1982); Gianni et al., Science (2026), on the QT45 ribozyme; NASA Astrobiology, Forming a Definition for Life; Moody et al., Nature Ecology & Evolution (2024), on the last universal common ancestor; Becher et al., Functional Ecology 26:822 (2012), on fruit flies and yeast.

Subtitles are written for this video, not auto-generated. An American English audio track is available as a second audio track.

Full transcript, sources and translations: https://theresmoretoit-channel.github.io/videos/where-did-the-first-life-come-from/

CHAPTERS
00:00 A banana and some flies
01:12 Life out of mud
01:57 Redi's jars
03:01 Pasteur's swan-neck flasks
03:55 So where did the first life come from?
04:57 Why it doesn't happen today
05:27 A warm little pond
06:36 Instructions and copies
07:08 The RNA world
08:21 What counts as alive?
09:39 One genetic code
10:07 Back to the kitchen

IMAGE CREDITS
Leeuwenhoek Microscope — Jeroen Rouwkema, CC BY-SA 3.0
Sainte-Ursule de la Sorbonne, Paris — Dietmar Rabich, CC BY-SA 4.0
Stromatolite, Strelley Pool Formation, Western Australia — James St. John, CC BY 2.0
Murchison meteorite, MNHN — Marie-Lan Taÿ Pamart, CC BY 4.0
Thomas Cech — Douglas A. Lockard, CC BY-SA 3.0
via Wikimedia Commons
Licences: creativecommons.org/licenses/by-sa/3.0, creativecommons.org/licenses/by-sa/4.0, creativecommons.org/licenses/by/2.0, creativecommons.org/licenses/by/4.0
All other archive images are in the public domain (Wikimedia Commons).
```

> **Blok se kopíruje CELÝ.** Povinná atribuce u S21, S29, S35, S49 a S55 (všech pět `CC BY*`
> z `sources.json`); S10, S12, S23, S32 a S44 jsou public domain.
>
> **Řádek s odkazem na web** doplní `python tools/odkaz_web.py --repo --jen 171` (za odstavec
> o titulcích, před kapitoly) — ručně se nepíše.
>
> **Pointa se neprozrazuje:** popis neříká, že žádný „první“ možná nebyl (S63–S71, latina →
> francouzština), ani nic o QT45. Poslední věta jen naznačí, že otázka je položená špatně.
>
> Kapitoly ze scén S01, S09, S15, S23, S31, S39, S43, S51, S55, S62, S72, S75 (`work/timing.json`,
> zaokrouhleno dolů), je jich 12, první na 00:00, nejkratší 30 s (S39 → S43). Zdroje
> z `factcheck.md`.

---

## 3. Náhled

**`render/thumbnail.jpg`**, koncept C1, dodal uživatel 2026-11-26, nahráno. Náhled nesmí prozradit pointu (pozvolný přechod, žádný
„první“); banán s mouchami nese miniatura (rozhodnutí 2026-11-23, viz `notes.md`).

---

## 4. Titulky

`subtitles/<kód>.srt` pro 14 jazyků a `en-US`. Jazyk videa **`en-gb`** nastaví `nahraj.py`.

---

## 5. Nastavení

| | |
|---|---|
| kategorie | **Science & Technology** (28) |
| jazyk videa | `en-gb` |
| licence | standardní |
| pro děti | **ne** |
| komentáře | zapnuté |
| **byla použita AI** | **ne**. 68 z 80 scén je kreslených kódem, 10 jsou archivní snímky upravené jen barevně. S34 a S43 jsou malované ilustrace ze SDXL (žhavá mladá planeta, tůň mezi sopečnými kameny), ne skutečné místo ani událost. Hlas je syntetický Kokoro `bf_emma`, ne klon; hudba procedurální. |

### Závěrečná obrazovka

Od **10:25** (S77 začíná 10:19, S78 10:31). `zaver_check` hlásí S77–S78 OK, spodní rohy jsou pod
titulky → **dlaždice i odběr do horní poloviny**. Dlaždice: návrh **160 *Why Is It So Hard to
Bring a Rock Back from Mars?*** — S74 končí *„find life that started somewhere else“* a 160 je
přesně o tom; druhá „nejlepší pro diváka“.

---

## 6. Tagy

```
where did the first life come from, origin of life, abiogenesis, spontaneous generation, louis pasteur,
swan neck flask, francesco redi, miller urey experiment, stanley miller, rna world, ribozyme, thomas cech,
murchison meteorite, what is life, definition of life, luca, last universal common ancestor, fruit flies,
evolution, there's more to it
```

---

## 7. Playlist

**`vesmir`**, potvrdil uživatel 2026-11-26 (poslední, pozice 18).

---

## 8. Komentář kanálu (otázka ze S78)

```
If a lab one day made something that copies itself and evolves, starting from nothing but simple chemicals, would you call it alive?
```
