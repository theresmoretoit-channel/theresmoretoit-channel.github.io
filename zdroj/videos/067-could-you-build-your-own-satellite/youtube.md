# YouTube — 067 „How Do You Build Your Own Satellite?"

Stav: **NAHRÁNO NEVEŘEJNĚ** (2026-09-28; čeká na ruční kroky + zveřejnění).

| | |
|---|---|
| ID videa | `Id-dThgXgKY` (neveřejné) |
| nastavení, popis, tagy, náhled | ✅ `videos.insert` (private) |
| lokalizace | ✅ 14 jazyků |
| titulky | ✅ 15 stop (en-GB, cs, sv, es, pt-BR, de, fr, it, pl, id, tr, uk, vi, fi, en-US) |
| automatický přepis | ⬜ za pár dní `titulky.py $V --smaz-asr` |
| playlist | ⬜ editorské rozhodnutí (vesmírný playlist zatím není); pak `playlisty.py` |
| závěrečná obrazovka, americká stopa | ⬜ uživatel ve Studiu |
| prohlášení o AI = ne, osvědčení o zproštění | ⬜ **ručně** (insert je nevyřídil) |

**Co musí uživatel naklikat sám:** závěrečnou obrazovku (API na ni nemá zdroj)
a nahrát americkou audiostopu. Prohlášení o AI a osvědčení o zproštění vyřídí
průvodce při ručním nahrání MP4.

Pořadí podle CENY (`docs/zverejneni.md`):

```bash
V=videos/067-could-you-build-your-own-satellite
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
How Do You Build Your Own Satellite?
```

> wh-otázka („How…") — podle `docs/kanal-metriky.md` nejlepší CTR (2,23 %
> proti 1,21 % u ano/ne otázky). Vybráno uživatelem 2026-09-27 z varianty
> „Could You Build Your Own Satellite?" (vnitřní rámování videa i voiceover
> zůstávají „could you", je to jen YouTube titul).

---

## 2. Popis

```
You don't need to be NASA to put a satellite in orbit. Small satellites
called CubeSats — some no bigger than a loaf of bread — are built by
universities, companies and even students, from standardised, off-the-shelf
parts.

But building the box turns out to be the easy part. The hard part is
everything else: what it costs, fitting it all into ten centimetres,
surviving a rocket launch and the vacuum of space, running on its own with
no one there to fix it, talking to the ground legally — and, in the end,
clearing itself out of orbit.

CubeSats didn't make space easy. They made it standardised. And that turns
out to be a surprisingly big change.

Subtitles are written for this video, not auto-generated. An American
English audio track is available as a second audio track.

Full transcript, sources and translations: https://theresmoretoit-channel.github.io/videos/could-you-build-your-own-satellite/

CHAPTERS
00:00 A crazy idea
00:27 Meet the CubeSat
00:41 Standard sizes
01:15 What is inside
01:57 What it costs
02:47 Fitting it all in
03:15 Off-the-shelf parts
04:39 Writing the software
05:56 Surviving space
06:12 Which way is up?
06:55 The mission
07:33 Testing, a lot of testing
09:00 Talking to it
09:34 Getting to orbit
10:37 The end of the mission
11:13 So — could you?

IMAGE CREDITS
CubeSat in hand — Svobodat, CC BY-SA 3.0
SCATSAT-1 vibration test — Indian Space Research Organisation, GODL-India
via Wikimedia Commons
Licences: creativecommons.org/licenses/by-sa/3.0/ · data.gov.in (GODL-India)

All other archive images are in the public domain.
```

> **Blok se kopíruje CELÝ** (`docs/zverejneni.md`). Povinné atribuce jsou
> UVNITŘ: S04 (CubeSat in hand, CC BY-SA 3.0) a S35 (SCATSAT-1, GODL-India).
> Public domain snímky (S19b SpaceCube, S42 Delta II, S43 STMSat) se
> nevypisují. **Pokud se S35 vymění za NASA-PD shaker, smaž řádek SCATSAT-1
> i GODL-India z licencí** — pak stačí „All other archive images…".

---

## 3. Náhled

`render/thumbnail.jpg` — **zatím není hotový.** Princip v `CLAUDE.md`
(„Thumbnail není titulková karta"), zadání v `docs/thumbnail-styl.md`,
kontrola `python tools/thumb_check.py $V`. Vyrobit víc konceptů, výběr na
uživateli.

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

Rozhoduje fotorealističnost. Video **nemá žádnou SDXL scénu** — 52 scén je
kresleno kódem, 5 jsou barevně upravené archivní fotografie (výjimka
„color adjustment"), hudba je procedurální. Žádný fotorealistický
generovaný obsah ani klonovaný hlas.

### Závěrečná obrazovka

`zaver_check.py` po renderu. Dlaždici i kolečko dej do **horní** poloviny
(dole je titulek diagramu). Poslední scény S48–S51 mají horní pruh volný.

---

## 6. Tagy

```
cubesat, how to build a satellite, small satellite, satellite, space,
spacecraft, embedded software, satellite computer, orbit, space debris,
rocket launch, cubesat deployer, arm cortex, diy space, explainer,
there's more to it
```

---

## 7. Playlist

Dopiš slug do `playlisty.json` (soused podle tématu — technika/vesmír),
spusť `analytics.py --videa` a pak `tools/playlisty.py`.
