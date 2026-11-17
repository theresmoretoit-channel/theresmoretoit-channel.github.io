# YouTube — 071 „How Do We Clean Up Space Junk?"

Stav: **připravuje se** (2026-09-28) — čeká na Codex (překlady).
Stav zveřejnění se vede v `Témata.ods`.

| | |
|---|---|
| video | `render/final-en-071.mp4` (master, 11:10,4) |
| náhled | `render/thumbnail.jpg` — ✅ dodaný obrázek, viz `thumbnail/PUVOD.md` |
| titulky | `subtitles/*.srt`, 14 jazyků + `en-US` |
| americká stopa | `render/audio-en-US.m4a` — nahrát ve Studiu |
| lokalizace | `youtube-preklady.md` |

**Co musí uživatel naklikat sám:** nahrát MP4 ve Studiu (průvodce vyřídí
prohlášení o AI a osvědčení o zproštění), americkou audiostopu
a závěrečnou obrazovku (API na ni nemá zdroj).

Pořadí podle CENY (`docs/zverejneni.md`); `lokalizace.py` a `titulky.py`
**až po zapracování nálezů Codexu**:

```bash
V=videos/071-how-do-we-clean-up-space-junk
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
How Do We Clean Up Space Junk?
```

> wh-otázka („How…") — podle `docs/kanal-metriky.md` nejlepší CTR.
> Neprozradí odpověď (že se to nemusí odtáhnout, stačí postrčit).

---

## 2. Popis

```
Thousands of tonnes of dead satellites, spent rocket stages and fragments
are circling Earth at several kilometres per second. Even a piece of
metal the size of a screw is a projectile. So how do you clean a place
with no floor, no broom and no garbage truck?

Why can't we simply catch the junk, or blow it up? What is the Kessler
syndrome? And why might the most useful trick be not to remove an object
at all, but to give it a small push?

We look at robotic spacecraft, nets and lasers — radiation pressure and
laser ablation — at what each of them is good for and where it runs into
trouble, and at why the cheapest piece of space junk is the one that
never becomes space junk.

Subtitles are written for this video, not auto-generated. An American
English audio track is available as a second audio track.

CHAPTERS
00:00 Thousands of tonnes of junk
00:47 Why it doesn't just fall down
01:36 Why not just catch it?
02:48 Why not just destroy it?
03:40 The first trick: change the orbit
04:26 Method 1: a robot
05:03 Method 2: a net
05:45 Method 3: a laser
07:38 Why we don't have space lasers yet
08:30 Which tool for which junk
09:08 Prevention
09:50 Can we actually clean up space?

IMAGE CREDITS
Space debris impact on Space Shuttle window — NASA, public domain,
via Wikimedia Commons
```

> **Blok se kopíruje CELÝ** (`docs/zverejneni.md`). Video má jediný
> archivní snímek (S08, NASA, volné dílo); povinná atribuce CC BY žádná
> není, NASA je uvedená jako zdroj podle jejích podmínek.
>
> Kapitoly: první na 00:00, každá ≥ 10 s, časy z `work/timing.json`
> (začátky scén S01, S06, S10, S15, S19, S22, S25, S28, S36, S40, S43, S46).

---

## 3. Náhled

`render/thumbnail.jpg` — **dodaný obrázek** (uživatel 2026-09-28): Země
s řídkými úlomky, nahoře **SPACE JUNK**, dole **HOW DO WE CLEAN IT?**.
Zdroj a otisky v `thumbnail/PUVOD.md`; varianta B (hustý prstenec) leží
v `thumbnail/varianta-b-prstenec.png` pro případný Test & Compare.
`thumb_check.py`: jas 56,3, 0,30 MB, 1280×720.

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
| komentáře | zapnuté |

### Prohlášení o AI: **ne**

Rozhoduje fotorealističnost. Video **nemá žádnou SDXL scénu** (S12 se
z SDXL překreslila kódem): 50 scén je kresleno kódem, 1 je barevně
upravená archivní fotografie NASA (výjimka „color adjustment"), hudba je
procedurální. Žádný fotorealistický generovaný obsah ani klonovaný hlas.

### Závěrečná obrazovka

Posledních 20 s je celá S50, která kreslí jen do spodní poloviny.
Dlaždici i kolečko dej do **horní** poloviny, dole je titulek.

---

## 6. Tagy

```
space junk, space debris, orbital debris, kessler syndrome, clearspace-1,
active debris removal, laser ablation, radiation pressure, low earth orbit,
satellites, deorbit, removedebris, space, explainer, there's more to it
```

---

## 7. Playlist

Po zveřejnění dopiš slug do `playlisty.json` (playlist `vesmir`), spusť
`analytics.py --videa` a pak `tools/playlisty.py`.
