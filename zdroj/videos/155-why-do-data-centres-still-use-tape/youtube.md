# YouTube — 155 „Why Do Data Centres Still Use Magnetic Tape?“

Stav: **nahráno (MP4 ručně), nastavení + náhled + lokalizace (13 jazyků) + titulky 15 stop přes API 2026-11-15, playlist `pocitace` pozice 8.** Americká stopa a závěrečná obrazovka naklikány, naplánováno (2026-11-15). Zbývá jen karta u S37b, až bude video o samoopravných kódech.

| | |
|---|---|
| ID videa | `2FHhIT9aiww` — https://youtu.be/2FHhIT9aiww |
| master | `render/final-en-155.mp4` (.207, 3× supersampling, 668,70 s, 50 MB, dekódováno bez chyby) |
| náhled | ✅ C2 audiokazeta, `TAPE / IN THE CLOUD?`, `render/thumbnail.jpg` (`thumbnail/PUVOD.md`) |
| nastavení, popis, tagy | podklady níž |
| lokalizace | `youtube-preklady.md`, 13 jazyků |
| titulky | `subtitles/<kód>.srt`, 14 jazyků + `en-US`, Codex zapracován (12 jazyků po draftu; cs čte uživatel) |
| americká stopa | `render/audio-en-US.m4a`, ručně ve Studiu |
| závěrečná obrazovka | S77–S79, **horní polovina** (viz níž) |
| **karta** | **u S37b (4:25) na video o samoopravných kódech** — až bude zveřejněné, jinak dodatečně |
| playlist | ✅ `pocitace`, pozice 8, za 130 (2026-11-15) |

**Co musí uživatel naklikat sám:** závěrečnou obrazovku, americkou audiostopu
(`render/audio-en-US.m4a`), kartu u S37b, titulky, které nejdou přes API, a osvědčení o zproštění, pokud ho nevyřídil průvodce nahráním.

Stopáž 11:09 (`work/timing.json` total 668,688 s).

> Kdyby se znovu pouštěl `tts.py`, přepočítej kapitoly tady i v `youtube-preklady.md`,
> pusť `diagrams/gen/animace.py` a přegeneruj `en-US` přes `us_stopa.py`.

Pořadí podle CENY (`docs/zverejneni.md`):

```bash
V=videos/155-why-do-data-centres-still-use-tape
python tools/nahraj.py $V --k-videu=<ID> --bez-titulku   # 100
python tools/analytics.py --videa                        #   1  ← nutné
python tools/lokalizace.py $V                            #  50
python tools/titulky.py $V --smaz-asr                    # 150  ← před titulky
python tools/titulky.py $V                               # 400×N
python tools/playlisty.py                                #  50
# úklid, až je MP4 na YouTube:
rm $V/render/draft*.mp4
ssh vrana@192.168.0.207 'rm -rf /home/vrana/temp/render-155-why-do-data-centres-still-use-tape'
```

---

## 1. Titul

```
Why Do Data Centres Still Use Magnetic Tape?
```

> Wh-otázka, 44 znaků, shodná s `project.json`. Odpověď (offline kopie, cena, energie, spolehlivost)
> titul neprozrazuje. Britské *Centres* sedí s hlasem `bf_emma`.

---

## 2. Popis

```
You press play. A cassette starts to squeal, and five minutes later, a game appears on the television. That sounds like nostalgia. But the world's data centres still keep their archives on tape. In February 2011, around forty thousand Gmail users opened their inbox and found it empty, and every message came back from tape. So why would the people with the most data still trust a strip of magnetic tape, when we have hard drives, SSDs and the cloud?

This video goes through LTO, the open tape format behind today's data archives, how forty terabytes fit into a cartridge you can hold in one hand, fifteen thousand tracks narrower than a thousandth of a millimetre, the servo patterns that keep the head on track, how the drive checks every block as it writes, why a cartridge on a shelf is safe from bugs and ransomware, what tape costs compared with hard drives, why finding a file can take a minute, the robot libraries at CERN and Lawrence Livermore, why AI is making tape grow again, and the strange problem of tapes that outlive their drives.

Sources: LTO Program, LTO-10 specifications and LTO roadmap; CERN, CERN hits one exabyte of stored experimental data (2025); IEEE Spectrum, on the Gmail restore from tape (2011); Fujifilm, news release on data tape production capacity (2026); IBM Research, 580 TB tape areal density demonstration with Fujifilm (2020); Fujifilm, LTO Ultrium data cartridge specifications.

Subtitles are written for this video, not auto-generated. An American English audio track is available as a second audio track.

Full transcript, sources and translations: https://theresmoretoit-channel.github.io/videos/why-do-data-centres-still-use-tape/

CHAPTERS
00:00 A cassette and a strange claim
00:22 The day Gmail came back from tape
01:02 Why trust tape?
01:14 Older than the hard drive
01:48 Forty terabytes in one hand
02:36 How does it all fit?
03:13 Tape that wanders
03:58 Built to check itself
04:46 The real advantage
05:51 What tape costs
06:20 The big weakness
07:09 Robot libraries
07:47 Then AI arrived
08:56 Tapes that outlive their drives
10:38 Back to the cassette

IMAGE CREDITS
Closeup of robotic arm in StorageTek tape library at NERSC — Derrick Coetzee, CC0
via Wikimedia Commons
All other archive images are in the public domain.
```

> **Blok se kopíruje CELÝ** (`docs/zverejneni.md`). Kredity ze `sources.json`: S13 UNIVAC (U.S. Census Bureau)
> je public domain, S55 robot NERSC je CC0 — atribuci nevyžaduje, ale je jmenovitě, protože CC0 není
> public domain v užším smyslu. Kresba S59 (`art/`, ChatGPT) a zbytek jsou kreslené kódem. SDXL ve videu není.
>
> **Pointa se neprozrazuje:** popis říká, ŽE se kopie uloží offline a že pásky přežijí mechaniky,
> ale ne to, že LTO-10 nečte žádnou starší kazetu (S73) ani že archivy kopírují (S74).
> *Tapes that outlive their drives* je paradox, ne odpověď.
>
> Kapitoly ze scén S01, S05, S11, S13, S17, S22, S29, S35, S40, S48b, S49, S55, S60, S70, S76
> (`work/timing.json`, zaokrouhleno dolů). První na 00:00, všechny ≥ 10 s (nejkratší S11 → S13, 12 s;
> poslední S76 → konec 30 s). Otázka do komentářů (S79) vlastní kapitolu nemá.
>
> **Zdroje:** z `factcheck.md` ty primární. Obchody a agregátory cen (tapebackup.org, magstor, SHI,
> hddhunt), Blocks & Files a heise v popisu nejsou.

---

## 3. Náhled

C2 z `thumbnail/ZADANI.md` (ChatGPT): průhledná audiokazeta na tmavé břidlici, `TAPE` / `IN THE CLOUD?`.
`render/thumbnail.jpg`, původ v `thumbnail/PUVOD.md`.

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
| komentáře | zapnuté (S79 je otázka do komentářů) |
| **byla použita AI** | **ne**. Video nemá jedinou SDXL scénu; 88 z 91 scén je kreslených kódem. S59 (sklep datacentra) je plochá ilustrace z ChatGPT (`art/PUVOD.md`), ne fotorealismus. Dva archivní snímky z Commons (S13 UNIVAC, S55 robot NERSC) jsou upravené jen barevně. Hudba je procedurální, hlas není klon skutečné osoby. |

### Závěrečná obrazovka

Od **11:09 − 20 s = 10:49**, tedy S77–S79. `zaver_check` hlásí všechny tři OK; dole je titulek,
**dlaždici i odběr dej do HORNÍ poloviny.** Jako dlaždici navrhuju **121 *How Did a Music Cassette Store
a Computer Game?*** (S01–S02 i S76 se na něj odvolávají), druhou nechat na „nejlepší pro diváka“.
Alternativa: 130 *How Did 8-Bit Computers Load Games Faster?*

---

## 6. Tagy

```
magnetic tape, lto, lto-10, tape storage, data centre, data center, tape backup, tape library, archive storage,
cold storage, air gap, ransomware protection, cern, gmail 2011, fujifilm, hard drive vs tape, error correction,
servo tracks, there's more to it
```

---

## 7. Playlist

**`pocitace`**, za 121 a 130 (`notes.md`). Vložit hned po `nahraj.py --k-videu` a `analytics.py --videa`.
