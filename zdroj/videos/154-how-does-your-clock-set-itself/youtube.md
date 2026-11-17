# YouTube — 154 „How Does Your Clock Set Itself?“

Stav: **nahráno (MP4 ručně), nastavení + náhled + lokalizace přes API; titulky 15 stop nahrány 2026-11-12, americká stopa a závěrečná obrazovka naklikány, naplánováno na 16. 11. 2026 21:00 Praha.** Master hotový (2026-11-11), náhled C2 hotový.

| | |
|---|---|
| ID videa | `d3kigrY3pao` — https://youtu.be/d3kigrY3pao |
| master | `render/final-en-154.mp4` (herní PC, 3× supersampling, 541,68 s, 1920×1080, 51 MB, dekódováno bez chyby; opravené podklady popisků v S06/S58/S59/S64) |
| náhled | ✅ C2 radiobudík a rádiové oblouky, `HOW DOES IT KNOW?`, `render/thumbnail.jpg` (`thumbnail/PUVOD.md`) |
| nastavení, popis, tagy | podklady níž |
| lokalizace | `youtube-preklady.md`, 13 jazyků |
| titulky | `subtitles/<kód>.srt`, 14 jazyků + `en-US`, Codex zapracován (cs/de/es před draftem, zbylých 10 po něm) |
| americká stopa | `render/audio-en-US.m4a`, ručně ve Studiu |
| závěrečná obrazovka | S68–S69, **horní polovina** (viz níž) |
| karty | žádné |
| playlist | ✅ `fyzika`, pozice 12 (2026-11-12) |

**Co musí uživatel naklikat sám:** závěrečnou obrazovku, americkou audiostopu
(`render/audio-en-US.m4a`), titulky, které nejdou přes API, a osvědčení o zproštění, pokud ho nevyřídil průvodce nahráním.

**Před zveřejněním zkontroluj stav Meteotime** (S42–S43, `notes.md`): k 11. 11. 2026 je přenos předpovědí
přerušený od 30. 6. 2026. Scénář o tom mluví v minulém čase (*could also tell*); kdyby se služba obnovila nebo
oficiálně skončila, rozhodne uživatel o dovětku. **Při vydání po 20. 5. 2027** změnit S40 *will run* → *has run*.

Stopáž 9:01 (`work/timing.json` total 541,657 s).

> Kdyby se znovu pouštěl `tts.py`, přepočítej kapitoly tady i v `youtube-preklady.md`
> a přegeneruj `en-US` přes `us_stopa.py`. **S17 má hotový zvuk** (`zvuk/S17.py`), `tts.py` ho převezme sám.

Pořadí podle CENY (`docs/zverejneni.md`):

```bash
V=videos/154-how-does-your-clock-set-itself
python tools/nahraj.py $V --k-videu=<ID> --bez-titulku   # 100
python tools/analytics.py --videa                        #   1  ← nutné
python tools/lokalizace.py $V                            #  50
python tools/titulky.py $V --smaz-asr                    # 150  ← před titulky
python tools/titulky.py $V                               # 400×N
python tools/playlisty.py                                #  50
# úklid, až je MP4 na YouTube:
rm $V/render/draft*.mp4
```

---

## 1. Titul

```
How Does Your Clock Set Itself?
```

> Wh-otázka, 31 znaků, shodná s `project.json`. Odpověď (S29–S33: zpráva ohlašuje příští minutu, pokles po mezeře
> je okamžik) titul neprozrazuje. *Your clock* místo zdrojového *…Listen to Germany?* — 70 % publika je americké (notes).

---

## 2. Popis

```
Somewhere in your home, there might be a clock that nobody has ever set. It survives power cuts. It changes for daylight saving time on its own, in the middle of the night. It has no internet connection. No Wi-Fi, no GPS, no app on your phone. All it has is a tiny radio receiver, and once every second, it hears a single pulse. So how does a clock turn one pulse per second into the exact time, the date, and even the day of the week?

This video goes through DCF77 near Frankfurt and WWVB in Colorado, how a radio wave carries zeros and ones, why a whole minute carries only fifty-nine bits, the parity bits that catch interference, the strange problem of when the time actually changes, daylight saving time and leap seconds, the weather forecasts hidden in the same signal, why many clocks only listen at night, which way the antenna should point, the atomic clocks behind the transmitter, and why a clock built for Germany can't make sense of Colorado.

Sources: PTB, DCF77 time code; PTB News 03/2, PTB time service prolonged; METAS, CCTF 2012 report from METAS (CH), BIPM working document TAI/12-21 (2012); BIPM, 28th CGPM (2026), Resolution 5; BIPM, 27th CGPM (2022), Resolution 4; NIST, Special Publication 432, NIST Time and Frequency Services; Meteotime, service notices (2026).

Subtitles are written for this video, not auto-generated. An American English audio track is available as a second audio track.

CHAPTERS
00:00 A clock nobody ever set
00:45 Short dip, long dip
01:13 The missing dip
01:44 What fits into fifty-nine bits
02:24 When radio isn't clean
03:05 When does the time actually change?
03:41 Summer time and leap seconds
04:44 Weather in the time signal
05:04 Why at night?
05:44 Which way the antenna points
06:11 Where the transmitter gets its time
07:06 Other countries, other transmitters
07:34 WWVB in Colorado
08:27 Different languages

IMAGE CREDITS
Atomuhr-CS2 part2 — Jörg Behrens, CC BY-SA 3.0
via Wikimedia Commons
Licences: creativecommons.org/licenses/by-sa/3.0
All other archive images are in the public domain.
```

> **Blok se kopíruje CELÝ** (`docs/zverejneni.md`). Kredity ze `sources.json`: jediný snímek s CC BY-SA
> (S53 laboratoř PTB) jmenovitě, zbylé dva (S49 přijímač DCF77, S61 stožáry WWVB, NIST) jsou public domain.
> SDXL scény S44, S46, S52 jsou generované, kreslené kódem je zbytek.
>
> **Pointa se neprozrazuje:** popis ani kapitoly neříkají, že zpráva ohlašuje PŘÍŠTÍ minutu a že okamžik nese
> pokles po mezeře (S31–S33). Kapitola *When does the time actually change?* je otázka, ne odpověď.
>
> Kapitoly ze scén S01, S07, S11, S16, S21, S28, S34, S41, S44, S49, S52, S58, S61, S67
> (`work/timing.json`, zaokrouhleno dolů). První na 00:00, všechny ≥ 10 s (nejkratší S41 → S44, 20 s;
> poslední S67 → konec 34 s). Otázka do komentářů (S69) vlastní kapitolu nemá.
>
> **Zdroje:** z `factcheck.md` ty, které jsou primární nebo citovatelné. Wikipedie a tisk (Euronews) v popisu nejsou.

---

## 3. Náhled

C2 z `thumbnail/ZADANI.md` (ChatGPT): radiobudík s ambrovým displejem, zleva rádiové oblouky, `CLOCK` / `HOW DOES IT KNOW?`.
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
| komentáře | zapnuté (S69 je otázka do komentářů) |
| **byla použita AI** | **ne**. 63 z 69 scén je kreslených kódem. Tři SDXL scény (S44 noční ložnice, S46 noční dvůr se stožárem, S52 stožáry v krajině) jsou díky kotvě stylu malované ilustrace, ne fotorealismus, a nezobrazují konkrétní skutečné místo jako dokument. Tři archivní snímky z Commons jsou upravené jen barevně (S53 navíc ořez okraje skenu). Hudba je procedurální, hlas není klon skutečné osoby. |

### Závěrečná obrazovka

Od **9:01 − 20 s = 8:41**, tedy S68–S69. `zaver_check` hlásí S68 i S69 OK, **horní polovina je volná**.
**Dlaždici i odběr dej do HORNÍ poloviny.** Jako dlaždici navrhuju **151 *How Precise Can Time Actually Be?***
(atomové hodiny, rodič S53–S55 na něj navazuje), druhou nechat na „nejlepší pro diváka“.
Alternativa: 119 *Why Do We Still Change the Clocks?* (navazuje S38).

---

## 6. Tagy

```
radio clock, how does a radio clock work, atomic clock, dcf77, wwvb, time signal, radio controlled clock,
daylight saving time, leap second, utc, parity bit, longwave radio, ptb, nist, time code, how clocks set themselves,
there's more to it
```

---

## 7. Playlist

**`fyzika`** (Science & Physics). 151 zatím v žádném playlistu není; až bude, zvážit vedle něj.
Vloženo 2026-11-12 (`playlisty.json` + `playlisty.py --jen fyzika`), ještě před zveřejněním.
