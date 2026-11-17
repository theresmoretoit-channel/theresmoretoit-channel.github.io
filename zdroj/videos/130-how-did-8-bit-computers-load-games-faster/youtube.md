# YouTube — 130 „How Did 8-Bit Computers Load Games Faster?“

Stav: **nahráno 2026-11-01** (https://youtu.be/40JtV1F2W0c): nastavení, popis, náhled, lokalizace 13 jazyků, titulky 15 stop, ASR smazán, playlist `pocitace`. Ručně zbývá závěrečná obrazovka a americká stopa.
Stav zveřejnění je v `Témata.fods`.

| | |
|---|---|
| ID videa | `40JtV1F2W0c` |
| master | ✅ `render/final-en-130.mp4` (11:12, 1920×1080, 54 MB, render 2026-11-01 na .207 za 573 s, `ffmpeg -v error` čistý) |
| náhled | ✅ `render/thumbnail.jpg`: TURBO / HOW SO FAST?, fotka C60 (Commons, CC BY 2.0) a text kódem, `thumbnail/PUVOD.md` |
| nastavení, popis, tagy | podklady níž |
| lokalizace | ✅ `youtube-preklady.md`, 13 jazyků |
| titulky | ✅ `subtitles/*.srt`, 14 jazyků + `en-US`, po Codexu (`notes.md`) |
| americká stopa | ✅ `render/audio-en-US.m4a` (15 MB, 672,7 s), ručně ve Studiu |
| závěrečná obrazovka | S91, **horní polovina** (viz níž) |
| karty | žádné |
| playlist | ✅ `pocitace` (*Inside Your Computer*), hned za 121 |

**Co musí uživatel naklikat sám:** závěrečnou obrazovku, americkou
audiostopu (`render/audio-en-US.m4a`) a osvědčení o zproštění, pokud ho
nevyřídil průvodce nahráním.

Stopáž 11:12 (`work/timing.json` total 672,7 s).

> Kdyby se znovu pouštěl `tts.py`, přepočítej kapitoly tady
> i v `youtube-preklady.md`, přegeneruj `en-US` přes `us_stopa.py`
> a pusť znovu `anim_s01.py`, `anim_s02.py`, `anim_s39.py` a `anim_s91.py`.

Pořadí podle CENY (`docs/zverejneni.md`):

```bash
V=videos/130-how-did-8-bit-computers-load-games-faster
python tools/nahraj.py $V --k-videu=40JtV1F2W0c --bez-titulku   # 100
python tools/analytics.py --videa                        #   1  ← nutné
python tools/lokalizace.py $V                            #  50
python tools/titulky.py $V --smaz-asr                    # 150  ← před titulky
python tools/titulky.py $V                               # 400×15
python tools/playlisty.py                                #  50
# úklid, až je MP4 na YouTube:
rm $V/render/draft*.mp4
ssh vrana@192.168.0.207 'rm -rf /home/vrana/temp/render-130-how-did-8-bit-computers-load-games-faster'
```

---

## 1. Titul

```
How Did 8-Bit Computers Load Games Faster?
```

> Wh-otázka, 42 znaků, shodná s `project.json`. Odpověď (změnil se
> způsob poslechu, ne páska) titul neprozrazuje.

---

## 2. Popis

```
Same computer. Same kind of cassette. Same program. One version loads in half the time. Nothing in the hardware changed, so what did?

This video looks at turbo loaders on 8-bit home computers: how a ZX Spectrum game could load at twice the normal speed, why the Spectrum didn't do that by itself, and how a computer that only understands the slow format loads the program that teaches it the fast one. Along the way: Speedlock and why speed wasn't its only job, a Commodore 64 cassette beating a floppy disk, Atari owners in Czechoslovakia opening up their tape recorders, and a Sharp MZ-800 program that could load games the computer itself refused.

The loading sounds in this video were generated from the real loading routines, a copy of the Spectrum's ROM loader with the constants Skool Daze used, and checked in an emulator. The whole turbo tape plays at the end.

Sources: ZX Spectrum ROM disassembly (LD-BYTES) and SkoolKit's Skool Daze disassembly; Your Sinclair, May 1986 (Turboloader); CRASH #24 and #44 (David Aubrey-Jones on Speedlock); World of Spectrum and CPCWiki on Speedlock; Compute! #56 and #57, January and February 1985 (TurboTape); Michael Steil, pagetable.com, C64 KERNAL disassembly; Commodore C2N Datassette service manual; ANTIC, February 1983, on the Atari cassette recorder; oldcomp.cz and atari-800.cz on Turbo 2000; Sharp MZ-800 Technical Reference Manual; Sharp MZ-800 emulator archive (Turbo Copy).

Subtitles are written for this video, not auto-generated. An American English audio track is available as a second audio track.

CHAPTERS
00:00 Same tape, half the time
00:37 Make every pulse shorter
01:22 Why the Spectrum didn't do it itself
02:34 The loader that loads the loader
03:26 Speedlock
04:42 Commodore 64: a cassette beats a floppy
05:55 Atari: open the recorder
07:09 The price of speed
07:45 The program that repaired games
08:19 A stopwatch set in advance
09:42 What they all have in common
10:17 A question for you
10:27 The whole turbo tape

IMAGE CREDITS
Commodore 64 with the external power supply and Commodore 1530 (C2N) Datasette — Xavier Caballe, CC BY-SA 2.0
Atari 800 XL home computer with monitor and tape program recorder XC12 — winkelnkemper, CC BY-SA 2.0
Sharp MZ-821 — Superandi73, CC BY-SA 3.0
Compact Cassette C60, Tape, Labelled, Face (thumbnail) — stuart.childs, CC BY 2.0
via Wikimedia Commons
Licences: creativecommons.org/licenses/by-sa/2.0, creativecommons.org/licenses/by-sa/3.0, creativecommons.org/licenses/by/2.0
```

> **Blok se kopíruje CELÝ** (`docs/zverejneni.md`). Archivní snímky
> jsou tři (S41, S53, S70, `CREDITS.md`), všechny CC BY-SA s povinnou
> atribucí; čtvrtý řádek je fotka v náhledu. Obrazovky Spectra (S01,
> S02, S91) jsou z emulátoru, nejsou to cizí snímky.
>
> **Pointa se neprozrazuje:** popis nejmenuje závěr *„It needed a better
> way to listen“* (S89) ani to, jak Turbo Copy hru „opravil“ (S80–S84).
> „Speedlock and why speed wasn't its only job“ naznačuje obrat, ne
> odpověď (ochrana proti kopírování).
>
> Kapitoly ze scén S01, S06, S13, S23, S31, S41, S53, S63, S69, S73,
> S85, S90, S91 (`work/timing.json`, zaokrouhleno dolů). Nejkratší
> 10,2 s (S90 → S91), první na 00:00, všechny ≥ 10 s. Výzvy k odběru
> (za S18 a S64) leží uvnitř kapitol.
>
> Čísla v popisu („half the time“, „twice the normal speed“) jsou tatáž
> jako ve scénáři (S03, S12); výhrada k S03 (polovina platí pro data)
> je ve `factcheck.md`.

---

## 3. Náhled

**TURBO / HOW SO FAST?** nad fotkou kazety C60 s rychlostní stopou
(koncept A ze tří, vybral uživatel 2026-11-01). Táž fotka jako u 121,
takže se dvojice ve výpisu pozná. Původ a atribuce v `thumbnail/PUVOD.md`;
atribuce je v bloku Popis ve všech 14 jazycích.

---

## 4. Titulky

`subtitles/*.srt`, 14 jazyků + `en-US`. Jazyk videa **`en-gb`** (hlas
`bf_emma`) se musí nastavit dřív, než se nahrají titulkové stopy.
Codex hotový a zapracovaný (`notes.md`, sezení 4).

---

## 5. Nastavení

| | |
|---|---|
| kategorie | **Science & Technology** (28) — posílá `nahraj.py` napevno |
| jazyk videa | `en-gb` |
| licence | standardní |
| pro děti | **ne** |
| komentáře | zapnuté (S90 je otázka do komentářů) |
| **byla použita AI** | **ne**. Většina scén je kreslená kódem, 3 archivní snímky jsou jen barevně upravené, obrazovky Spectra jsou z emulátoru. SDXL jsou dvě atmosférické scény (S57, S87): malované ilustrace, ne skutečné místo ani událost. Hudba je procedurální, signály jsou vygenerované z časování loaderů, hlas není klon. |

### Závěrečná obrazovka

Od **10:53** (posledních 20 s), tedy jen S91: film z emulátoru vlevo
a mapa pásky s jezdcem uprostřed, obojí ve **spodní polovině** rámu
(snímek z draftu v 11:02). `zaver_check` četl jen statické PNG a radí
nedávat nic dolů přes titulky. **Dlaždici i odběr dej do HORNÍ poloviny**
(horní polovina je v S91 prázdná). Jako dlaždici doporučuju **121 *How Did
a Music Cassette Store a Computer Game?*** (přímý předchůdce, S06 na něj
odkazuje), druhou nechat na „nejlepší pro diváka“.

---

## 6. Tagy

```
turbo loader, zx spectrum, commodore 64, atari 800, sharp mz-800,
cassette loading, fast loader, speedlock, turbotape, turbo 2000,
retro computing, 8-bit computers, loading games from tape,
copy protection, home computers 1980s, there's more to it
```

---

## 7. Playlist

`pocitace` (*Inside Your Computer — Why It Behaves the Way It Does*),
hned za 121. Zapsat do `playlisty.json` při nahrání; `playlisty.py` ho
přeskočí, dokud video není v `analytics/videa.json`.
