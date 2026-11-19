# YouTube — 161 „How Hard Was It to Make a DOS Game?“

Stav: **nahráno 2026-11-19** (`mUOVu8aofSk`) — nastavení, náhled, lokalizace 13, titulky 15, playlist `pocitace`. Ručně zbývá závěrečná obrazovka, karta S30 a US audiostopa.

| | |
|---|---|
| ID videa | `mUOVu8aofSk` — https://youtu.be/mUOVu8aofSk |
| master | ✅ `render/final-en-161.mp4` (.207, 2026-11-19, 1920×1080, 9:59,92, 69,6 MB, dekóduje čistě) |
| náhled | ✅ `render/thumbnail.jpg` (C1 `DOS / STRUGGLE OR FUN?`, `thumbnail/PUVOD.md`) |
| nastavení, popis, tagy | ✅ `nahraj.py --k-videu --bez-titulku` |
| lokalizace | ✅ `youtube-preklady.md`, 13 jazyků |
| titulky | ✅ `subtitles/<kód>.srt`, 14 jazyků + `en-US` (ASR nebylo) |
| americká stopa | `render/audio-en-US.m4a` (k draftu 4, scénář v0.6), ručně ve Studiu |
| závěrečná obrazovka | S92–S96 (viz níž) |
| karty | **jedna**, S30 → 156 (`nahraj.py` ji vypíše) |
| playlist | `pocitace` |

**Co musí uživatel naklikat sám:** závěrečnou obrazovku, **kartu**, americkou audiostopu
(`render/audio-en-US.m4a`) a osvědčení o zproštění, pokud ho nevyřídil průvodce nahráním.

Stopáž 10:00 (`work/timing.json` total 599,91 s).

> Kdyby se znovu pouštěl `tts.py`, přepočítej kapitoly a čas karty tady i v `youtube-preklady.md`
> a přegeneruj `en-US` přes `us_stopa.py`.

Pořadí podle CENY (`docs/zverejneni.md`):

```bash
V=videos/161-how-hard-was-it-to-make-a-dos-game
python tools/nahraj.py $V --k-videu=<ID> --bez-titulku   # 100
python tools/analytics.py --videa                        #   1  ← nutné
python tools/lokalizace.py $V                            #  50
python tools/titulky.py $V --smaz-asr                    # 150  ← před titulky
python tools/titulky.py $V                               # 400×N
python tools/playlisty.py                                #  50
# úklid, až je MP4 na YouTube:
rm $V/render/draft*.mp4
ssh vrana@192.168.0.207 'rm -rf /home/vrana/temp/render-161-how-hard-was-it-to-make-a-dos-game'
```

---

## 1. Titul

```
How Hard Was It to Make a DOS Game?
```

> Wh-otázka, 35 znaků, shodná s `project.json` a s titulem zdroje. Odpověď (obtížnost se
> nezmenšila, přesunula se do vrstev, ze kterých vyrostly dnešní enginy) titul neprozrazuje.

---

## 2. Popis

```
In 1993, Doom ran on a computer with four megabytes of memory and no 3D accelerator. Today, a game starts with an engine that takes care of graphics, sound, memory and the hardware. On DOS, all of that was the developer's problem, and quite often the player's too. So how hard was it to make a game for DOS?

This video goes through the 640-kilobyte limit and the line usually credited to Bill Gates, expanded and extended memory, why players ended up editing CONFIG.SYS and AUTOEXEC.BAT and building boot menus in MS-DOS 6, what DOS/4GW did when its name flashed past on the screen, how Mode 13h and Michael Abrash's Mode X put pixels on the screen, why sound cards were a lottery of ports, IRQs and DMA channels, how programmers replaced multiplication with bit shifts, the joke error message in Wing Commander, and what happened when other studios wanted Doom's engine.

Sources: id Software, Doom README (1993) and Doom source code (GPL release, 1999); Microsoft, MS-DOS 6 online help and Knowledge Base Q91202 (MultiConfig); Quote Investigator, "640K of computer memory ought to be enough for anybody" (2011); M. Abrash, Dr. Dobb's Journal (July 1991); B. Sheffield, Dirty Coding Tricks II, Game Developer (March 2010); B. Lesnick, Mythbusters: Wing Commander I Edition, Wing Commander CIC (September 2023).

Subtitles are written for this video, not auto-generated. An American English audio track is available as a second audio track.

Full transcript, sources and translations: https://theresmoretoit-channel.github.io/videos/how-hard-was-it-to-make-a-dos-game/

CHAPTERS
00:00 Doom on four megabytes
00:35 The 640-kilobyte limit
01:33 Expanded and extended memory
02:00 When it became the player's problem
02:47 DOS extenders and DOS/4GW
03:45 One byte per pixel
04:38 Mode X
05:04 The sound card lottery
06:18 Counting every step
07:01 Thank you for playing Wing Commander
07:40 Back to Doom
08:48 Licensing the engine
09:25 Was it harder back then?

IMAGE CREDITS
Michael Abrash at Facebook's F8 2015 — Maurizio Pesce, CC BY 2.0
NeXTcube — Simon Claessen, CC BY-SA 2.0
Freedoom screenshot (Freedoom 2018) — Freedoom developers, BSD licence
OpenTTD screenshot (Farhill Transport, 14th Mar 1939) — OpenTTD authors, OpenGFX authors, Derpy Hooves; GPL
via Wikimedia Commons. Licences: creativecommons.org/licenses/by/2.0, creativecommons.org/licenses/by-sa/2.0
The photos of the IBM PC 5150 and the Roland MT-32 are in the public domain.
```

> **Blok se kopíruje CELÝ** (`docs/zverejneni.md`). Kredity ze `sources.json`: povinná atribuce je
> u **S43** (Pesce, CC BY 2.0) a **S85** (Claessen, CC BY-SA 2.0); **S67** OpenTTD (GPL) a **S75**
> Freedoom (BSD) jsou snímky volných her, ve videu s popiskem, že nejde o originál. S08 a S51
> public domain.
>
> **Pointa se neprozrazuje:** popis neříká, že obtížnost nezmizela, nýbrž se přesunula (S93), ani že
> se Doom na DOSu nevyvíjel (S84–S85), ani jak dopadl vtip ve Wing Commanderu (S74).
>
> Kapitoly ze scén S01, S07, S17, S21, S28, S37, S43, S47, S59, S69, S75, S87, S92
> (`work/timing.json`, zaokrouhleno dolů). První na 00:00, všechny ≥ 10 s (nejkratší S17 → S21
> 27 s a S43 → S47 26 s; poslední S92 → konec 34 s).
>
> **Zdroje:** primární a nejsilnější sekundární z `factcheck-zaklad.md`.

---

## 3. Náhled

**Zatím není.** Další krok podle `docs/thumbnail-styl.md`.

---

## 4. Titulky

`subtitles/<kód>.srt` pro 14 jazyků a `en-US`.
Jazyk videa **`en-gb`** (hlas `bf_emma`) nastaví `nahraj.py` dřív, než se nahrají titulkové stopy.

---

## 5. Nastavení

| | |
|---|---|
| kategorie | **Science & Technology** (28), posílá `nahraj.py` napevno |
| jazyk videa | `en-gb` |
| licence | standardní |
| pro děti | **ne** |
| komentáře | zapnuté (S96 je otázka do komentářů) |
| **byla použita AI** | **ne**. Většina scén je kreslená kódem. Archivní snímky (S08, S43, S51, S85) jsou upravené jen barevně, S67 a S75 jsou skutečné snímky volných her. S21, S69 a S92 jsou malované ilustrace z SDXL, ne fotorealismus. Hudba je procedurální, hlas není klon skutečné osoby. |

### Karty

| čas | scéna | cíl |
|---|---|---|
| **~3:02** | S30 *We've looked at protected mode in an earlier video* | 156 *Why Can't One Program Take Over Your Computer?* (`qZdKjlQFpVY`) |

> Čas je ze začátku scény (3:00) + ~2 s; přesný vypíše `nahraj.py` z `work/timing.json`.

### Závěrečná obrazovka

Od **10:00 − 20 s ≈ 9:40** (začátek S95 je 9:42, S94 9:35). `zaver_check` hlásí S94, S95
a S96 OK, spodní rohy jsou pod titulky. **Dlaždici i odběr dej do HORNÍ poloviny.** Jako dlaždici navrhuju **156** (protected mode
a DOS extender jsou jádro obou videí), případně **130** *How did 8-bit computers load games
faster*; druhou nechat na „nejlepší pro diváka“.

---

## 6. Tagy

```
dos games, ms-dos, doom, retro gaming, game development, 640k, conventional memory,
expanded memory, ems, himem, config.sys, autoexec.bat, dos/4gw, protected mode, vga,
mode 13h, mode x, michael abrash, sound blaster, adlib, roland mt-32, transport tycoon,
wing commander, id software, game engine, there's more to it
```

---

## 7. Playlist

**`pocitace`** (je v něm i 156 a 130). Dopsat slug do `playlisty.json`, `analytics.py --videa`,
`playlisty.py --jen pocitace`.
