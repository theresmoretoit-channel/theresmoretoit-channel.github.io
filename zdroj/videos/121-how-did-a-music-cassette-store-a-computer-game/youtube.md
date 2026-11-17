# YouTube — 121 „How Did a Music Cassette Store a Computer Game?“

Stav: **nahráno (`YmUJgDi4vR0`), zveřejnění naplánované; zbytek doklikal uživatel ručně ve Studiu (2026-10-24).**
Stav zveřejnění je v `Témata.fods`.

| | |
|---|---|
| ID videa | `YmUJgDi4vR0` |
| master | ✅ `render/final-en-121.mp4` (9:06, 1920×1080, 51 MB, render 2026-10-24 na .207 za 490 s, `ffmpeg -v error` čistý; program z S70 se z jeho zvuku načte i po Opus 128k, md5 sedí) |
| náhled | ✅ `render/thumbnail.jpg`: fotka kazety C60 (Commons, CC BY 2.0) a text kódem, `thumbnail/PUVOD.md` |
| nastavení, popis, tagy | podklady níž |
| lokalizace | `youtube-preklady.md`, 13 jazyků |
| titulky | `subtitles/*.srt`, 14 jazyků + `en-US`, až po Codexu |
| americká stopa | `render/audio-en-US.m4a`, ručně ve Studiu |
| závěrečná obrazovka | **žádná** — nešla umístit (viz níž) |
| karty | žádné |
| playlist | `pocitace` (*Inside Your Computer*), na konec |

**Co musí uživatel naklikat sám:** závěrečnou obrazovku, americkou
audiostopu (`render/audio-en-US.m4a`) a osvědčení o zproštění, pokud ho
nevyřídil průvodce nahráním.

Stopáž 9:06 (`work/timing.json` total 545,5 s).

> **Před zveřejněním otestovat signál na zvuku staženém z YouTube**
> (`notes.md`): program z S70 se musí v emulátoru načíst a dát md5
> obrazovky `ae779f948d9a634eaf5077a00bb4ea01`. Video to divákům slibuje
> (S28c *„Record it, and a Spectrum will load it.“*).

> Kdyby se znovu pouštěl `tts.py`, přepočítej kapitoly tady
> i v `youtube-preklady.md`, přegeneruj `en-US` přes `us_stopa.py`
> a pusť znovu `anim_s01.py`, `anim_s18.py` a `anim_s70.py`.

Pořadí podle CENY (`docs/zverejneni.md`):

```bash
V=videos/121-how-did-a-music-cassette-store-a-computer-game
python tools/nahraj.py $V --k-videu=<ID> --bez-titulku   # 100
python tools/analytics.py --videa                        #   1  ← nutné
python tools/lokalizace.py $V                            #  50
python tools/titulky.py $V --smaz-asr                    # 150  ← před titulky
python tools/titulky.py $V                               # 400×15
python tools/playlisty.py                                #  50
# úklid, až je MP4 na YouTube:
rm $V/render/draft*.mp4
ssh vrana@192.168.0.207 'rm -rf /home/vrana/temp/render-121-how-did-a-music-cassette-store-a-computer-game'
```

---

## 1. Titul

```
How Did a Music Cassette Store a Computer Game?
```

> Wh-otázka, 47 znaků, shodná s `project.json`. Odpověď titul
> neprozrazuje. Záložní titul na případný test: *Why Did Computer Games
> Sound Like Screaming?* (`notes.md`).

---

## 2. Popis

```
In the 1980s, millions of kids pressed play on an ordinary cassette recorder and listened to a screech. It wasn't music, and it wasn't a sound effect. It was the game itself, travelling as sound.

This video follows one program from the tape into a ZX Spectrum: how a zero and a one became two notes an octave apart, what the steady hum before every game was for, why loading screens appeared in such a strange order, and how a single byte at the end could throw away five minutes of waiting. Along the way: why American kids mostly never heard the noise, how the Commodore 64 and Atari did it differently, the tiny screwdriver everyone used on their tape head, and the radio and TV stations that broadcast software over the air.

The loading signal in this video was generated from the Spectrum's own ROM timing, and a real Spectrum program is inside. It plays in full under the closing credits. Record it, and a Spectrum (or an emulator) will load it.

Sources: ZX Spectrum ROM disassembly (SA-BYTES, LD-BYTES); ZX Spectrum BASIC manual, chapter 20; BYTE, February 1976 (Kansas City Standard symposium); Compute!'s Gazette, December 1983; Michael Steil, pagetable.com, and C64-Wiki on Commodore Datassette encoding; Compute! no. 56 (TurboTape); ANTIC vol. 1 no. 4 (Atari cassette); Ventilator 202 (Radio Belgrade); Hobbyscoop / NOS (BASICODE); Electronic Soundmaker & Computer Music, September 1983 (Pete Shelley, XL1); Fujifilm LTO Ultrium specifications. The cassette comparison assumes about 300 KB per side of a C60 tape at Spectrum speed.

Subtitles are written for this video, not auto-generated. An American English audio track is available as a second audio track.

CHAPTERS
00:00 Not music, a program
00:33 Zero and one as two notes
01:11 An American idea
02:00 Why Britain stayed on tape
02:27 Following one game into the computer
03:43 The strange loading screen
04:06 One byte decides
04:45 Other computers, other bets
05:12 The cassette player problem
05:49 Anything that carries sound
06:56 The catch
07:34 Tape never left
08:40 The program, as promised

IMAGE CREDITS
Sinclair ZX Spectrum 48k — Nico Kaiser from München, Germany, CC BY 2.0
Apple II, TRS-80 Model I (edited image) — Pittigrilli, edited from an upload by Springsgrace, CC BY 4.0
Tensai CRE-113 cassette recorder — Kecko, CC BY 4.0
The architecture of memory: inside the StorageTek tape library — Jorge Franganillo, CC BY 4.0
Compact Cassette C60, Tape, Labelled, Face (thumbnail) — stuart.childs, CC BY 2.0
via Wikimedia Commons
Licences: creativecommons.org/licenses/by/2.0, creativecommons.org/licenses/by/4.0
```

> **Blok se kopíruje CELÝ** (`docs/zverejneni.md`). Archivní snímky
> jsou čtyři (S06, S13, S42, S63) a všechny mají povinnou atribuci, takže
> věta o volném díle tu není. Pátý řádek je fotka v náhledu (CC BY 2.0). Obrazovky Spectra (S35, S70) jsou
> z emulátoru, nejsou to cizí snímky.
>
> **Pointa se neprozrazuje.** Popis nejmenuje závěr *„Anything that
> could carry sound could carry software“* (S50) ani návrat pásky
> v datových centrech (S63–S66), jen kapitolu „Tape never left“.
>
> Kapitoly ze scén S01, S06, S10, S16, S19, S29, S32, S38, S42, S48,
> S57, S62, S70 (`work/timing.json`, zaokrouhleno dolů). Nejkratší
> 23 s (S29 → S32), první na 00:00, všechny ≥ 10 s. Výzvy k odběru
> (S18b, S37) leží uvnitř kapitol.
>
> Čísla v popisu jsou tatáž jako ve scénáři a ve `factcheck.md`
> (S09, S31, S36, S65).

---

## 3. Náhled

**CASSETTE / WHERE’S THE GAME?** nad skutečnou fotkou kazety C60 (koncept A
ze `thumbnail/ZADANI.md`). ChatGPT dvakrát nezvládl text (*CASSETE*)
ani kazetu, takže je to fotka z Commons a text vysázený kódem
(`thumbnail/gen.py`). Původ a atribuce v `thumbnail/PUVOD.md`; atribuce
je v bloku Popis ve všech 14 jazycích.

---

## 4. Titulky

`subtitles/*.srt`, 14 jazyků + `en-US`. Jazyk videa **`en-gb`** (hlas
`bf_emma`) se musí nastavit dřív, než se nahrají titulkové stopy.
Nahrávají se až po Codexu (nálezy v `notes.md`).

---

## 5. Nastavení

| | |
|---|---|
| kategorie | **Science & Technology** (28) — posílá `nahraj.py` napevno |
| jazyk videa | `en-gb` |
| licence | standardní |
| pro děti | **ne** |
| komentáře | zapnuté (S69 končí otázkou do komentářů) |
| **byla použita AI** | **ne**. 70 scén je kreslených kódem, 4 archivní snímky jsou jen barevně upravené. SDXL je jediná scéna (S68, dítě u televize zezadu, bez obličeje): malovaná ilustrace, ne skutečné místo ani událost. Hudba je procedurální, signál Spectra je vygenerovaný z časování ROM, hlas není klon. |

### Závěrečná obrazovka

**NENÍ — uživatel ji 2026-10-24 vynechal.** Pruhy nahrávání v S70 běží
přes celý rám a prvky Studia (nejdou zmenšit, logo samo nejde) by všude
něco zakryly; `zaver_check` četl jen statické PNG. Snímek ze Studia:
`zaverecna-obrazovka-studio.png`, rozbor v `docs/storyboard-a-diagramy.md`.
Původní návrh, který nevyšel:


Od **8:46** (posledních 20 s), tedy jen S70. **Dlaždici i odběr dej do
HORNÍ poloviny** (`zaver_check`: dlaždice @ 0,47 / 0,02, odběr @ 0,02 /
0,02); dolní polovinu zabírají titulky a obrazovka Spectra, na které
program právě kreslí kazetu. Jako dlaždici doporučuju **047 *How Did 5 MB
Become Terabytes?*** (navazuje na LTO-9 z S64–S65), druhou nechat na
„nejlepší pro diváka“.

---

## 6. Tagy

```
zx spectrum, cassette loading, loading screen, tape loading, retro computing,
8-bit computers, commodore 64, kansas city standard, data on cassette,
r tape loading error, basicode, home computers 1980s, magnetic tape,
lto tape, how computers store data, there's more to it
```

---

## 7. Playlist

`pocitace` (*Inside Your Computer — Why It Behaves the Way It Does*), na
konec. Video vysvětluje, jak počítač dekóduje data ze zvuku. Alternativa je
`legacy` (páska, která v datových centrech nikdy neodešla, S63–S66).
Zapsat do `playlisty.json` při nahrání; `playlisty.py` ho přeskočí,
dokud video není v `analytics/videa.json`.
