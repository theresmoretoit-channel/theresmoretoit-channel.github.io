# YouTube — 111 „What Would It Take to Travel Faster Than Light?“

Stav: **nahráno 2026-10-16** (https://www.youtube.com/watch?v=zGxKaV9OROE). Metadata, náhled, 13 lokalizací a všech 15 titulkových stop přes API, playlist `vesmir` přes `playlisty.py`; americkou stopu, závěrečnou obrazovku, kartu na 035 a naplánované zveřejnění naklikal uživatel ve Studiu (hotovo). Stav zveřejnění je v `Témata.ods`.

| | |
|---|---|
| ID videa | `zGxKaV9OROE` |
| master | ✅ `render/final-en-111.mp4` (9:23, 1920×1080, 51 MB, render 2026-10-16 na .207, `ffmpeg -v error` čistý) |
| náhled | ✅ `render/thumbnail.jpg` (1 KG / HOW MUCH ENERGY?) — `thumbnail/PUVOD.md` |
| nastavení, popis, tagy | podklady níž |
| lokalizace | `youtube-preklady.md`, 13 jazyků, prošlo Codexem (11 oprav), ✅ nahráno |
| titulky | `subtitles/*.srt`, 14 jazyků + `en-US`, překlady prošly Codexem (64 oprav), ✅ všech 15 přes API |
| americká stopa | `render/audio-en-US.m4a` — nahrává uživatel ve Studiu |
| závěrečná obrazovka | ručně ve Studiu |
| **karta** | **na 035 *Can We Reach Another Star?* v čase 1:18 (S09)** — ručně ve Studiu |
| playlist | ✅ `vesmir`, pozice 7 |

**Co musí uživatel naklikat sám:** nahrát MP4 ve Studiu (průvodce vyřídí
prohlášení o AI a osvědčení o zproštění), závěrečnou obrazovku, kartu
na 035 a americkou audiostopu (`render/audio-en-US.m4a`).

Stopáž 9:23 (`work/timing.json` total 563,1 s).

> Kdyby se znovu pouštěl `tts.py`, přepočítej kapitoly tady
> i v `youtube-preklady.md`, čas karty a přegeneruj `en-US` přes `us_stopa.py`.

Pořadí podle CENY (`docs/zverejneni.md`):

```bash
V=videos/111-what-would-it-take-to-travel-faster-than-light
python tools/nahraj.py $V --k-videu=<ID> --bez-titulku    # 100
python tools/analytics.py --videa                         #   1  ← nutné
python tools/lokalizace.py $V                             #  50
python tools/titulky.py $V --smaz-asr                     # 150  ← před titulky
python tools/titulky.py $V                                # 400×15
python tools/playlisty.py                                 #  50
# úklid, až je MP4 na YouTube:
rm $V/render/draft*.mp4
ssh vrana@192.168.0.207 'rm -rf /home/vrana/temp/render-111-what-would-it-take-to-travel-faster-than-light'
```

---

## 1. Titul

```
What Would It Take to Travel Faster Than Light?
```

> Wh-otázka, 47 znaků. Odpověď (motor nestačí; obě cesty chtějí zápornou
> energii; a možná to zakazuje kauzalita) titul neprozrazuje.

---

## 2. Popis

```
Take one kilogram, a bag of sugar, and push it to ninety-nine per cent of the speed of light. The energy you'd need is about a hundred and thirty megatons, more than twice the largest bomb ever detonated. Every extra nine costs more than the last, and at the Large Hadron Collider no amount of energy closes the final gap. So a bigger engine won't do it.

Physics has two stranger ideas. In 1994 Miguel Alcubierre found a solution to Einstein's equations that looks a lot like the warp drive of science fiction: don't move through space, move space instead. And in 1988 Kip Thorne and Michael Morris asked what it would take to hold a wormhole open, a serious physics question that started with Carl Sagan's novel Contact. So what would we actually have to invent?

How fast our real spacecraft are, and how long they'd take to reach another star: Can We Reach Another Star? https://www.youtube.com/watch?v=4waGk1NE9QY

Sources: M. Alcubierre, The warp drive (Class. Quantum Grav., 1994; arXiv gr-qc/0009013); Pfenning & Ford, The unphysical nature of "warp drive" (1997; arXiv gr-qc/9702026); Everett & Roman (1997; arXiv gr-qc/9702049); Bobrick & Martire, Introducing physical warp drives (2021; arXiv 2102.06824); Morris & Thorne, Am. J. Phys. 56, 395 (1988); Morris, Thorne & Yurtsever, Phys. Rev. Lett. 61, 1446 (1988); Davis & Lineweaver on cosmic expansion (arXiv astro-ph/0310808); Visser, Kar & Dadhich (arXiv gr-qc/0301003); K. Thorne, Black Holes and Time Warps (1994).

Subtitles are written for this video, not auto-generated. An American English audio track is available as a second audio track.

CHAPTERS
00:00 One kilogram at 99% of light speed
00:37 The last three metres per second
01:31 Time runs slower on board
02:05 Space itself can stretch
02:36 Alcubierre's warp bubble
03:23 Less energy than nothing
04:23 How much the bubble needs
05:19 Sagan, Thorne and a novel
05:49 Folding the paper: wormholes
06:18 Holding a wormhole open
07:28 Three things we'd have to invent
08:40 A problem deeper than energy

IMAGE CREDITS
LHC tunnel, sector 3-4 — Maximilien Brice (CERN), CC BY-SA 3.0
Miguel Alcubierre — Jpablo.romero at en.wikipedia, CC BY-SA 3.0
Carl Sagan in 1987 — Kenneth C. Zirkel, CC BY-SA 4.0
Kip S. Thorne, 1972 — A. T. Service, CC BY-SA 3.0
via Wikimedia Commons
Licences: creativecommons.org/licenses/by-sa/3.0, creativecommons.org/licenses/by-sa/4.0
All other archive images: NASA, ESA, public domain.
```

> **Blok se kopíruje CELÝ** (`docs/zverejneni.md`). CC BY-SA snímky jsou
> čtyři (S05, S17, S35, S36), všechny atribuce jsou uvnitř. S13 (Hubble
> eXtreme Deep Field) je NASA/ESA, public domain.
>
> **Pointa se neprozrazuje.** Popis jmenuje warp i červí díru (jsou
> v kapitolách stejně), ale ne zápornou energii, její množství ani
> kauzalitu na konci.
>
> Kapitoly ze scén S01, S05, S10, S13, S17, S22, S29, S35, S38, S42, S49,
> S57 (`work/timing.json`, zaokrouhleno dolů). Nejkratší 29 s (S35 → S38),
> všechny ≥ 10 s, první na 00:00. Výzva k odběru S09b (1:23) leží
> v kapitole „The last three metres per second“.
>
> Zdroje podle `factcheck.md`, „Zdroje“. Čísla v popisu (130 megatun,
> 1994, 1988) jsou tatáž jako ve scénáři.

---

## 3. Náhled

✅ `render/thumbnail.jpg` — 1 KG / HOW MUCH ENERGY? (papírový pytlík se
světelnými stopami). Hotový obrázek od uživatele (ChatGPT, zadání B),
jen zmenšený; původ a otisk v `thumbnail/PUVOD.md`, zadání
v `thumbnail/ZADANI.md`.

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
| **byla použita AI** | **ne**. 57 scén je kreslených kódem, 5 archivních snímků (CERN, NASA/ESA, tři portréty) je jen barevně upravených. S47 je obrázek z ChatGPT, ale zobrazuje zjevně smyšlenou mimozemskou stavbu jako představu z románu, ne skutečné místo, osobu ani událost (`art/PUVOD.md`). Žádná SDXL scéna. Hudba je procedurální, hlas není klon. |

### Závěrečná obrazovka

Od **9:03** (posledních 20 s), tedy S59–S62. `zaver_check` u nich hlásí
volnou **horní polovinu**, prvky patří **nahoru**.

### Karta

Na video **035 *Can We Reach Another Star?*** (`4waGk1NE9QY`) v čase
**1:18** — S09 *„Our actual spacecraft are far slower, as we saw in an
earlier video.“* začíná v 78,5 s.

---

## 6. Tagy

```
faster than light, speed of light, warp drive, alcubierre drive, wormhole,
kip thorne, carl sagan, contact, negative energy, casimir effect,
exotic matter, special relativity, general relativity, time dilation,
interstellar travel, physics explainer, science explainer, there's more to it
```

---

## 7. Playlist

`vesmir` (*Space — Getting There, and Who Else Is Out There*), na konec.
