# YouTube — 157 „How Can You Recover Data That Never Arrived?“

Stav: **připraveno k nahrání, nic nenahráno.** Master hotový (207, 2026-11-15), náhled C1 hotový, americká stopa hotová.

| | |
|---|---|
| ID videa | `DOPLNIT-ID` |
| master | `render/final-en-157.mp4` (207, 3× supersampling, 579,6 s, 1920×1080, 35 MB, dekódováno bez chyby) |
| náhled | ✅ C1 roztržený QR kód, `QR CODE` / `TORN. STILL WORKS?`, `render/thumbnail.jpg` (`thumbnail/PUVOD.md`) |
| nastavení, popis, tagy | podklady níž |
| lokalizace | `youtube-preklady.md`, 13 jazyků |
| titulky | `subtitles/<kód>.srt`, 14 jazyků + `en-US`, Codex zapracován ve všech 13 překladech |
| americká stopa | `render/audio-en-US.m4a` (`us_stopa.py`), ručně ve Studiu |
| závěrečná obrazovka | S81–S82, **horní polovina** (viz níž) |
| karty | **dvě**, viz níž (`nahraj.py` je vypíše) |
| playlist | `pocitace` (Computers) |

**Co musí uživatel naklikat sám:** závěrečnou obrazovku, dvě karty, americkou audiostopu
(`render/audio-en-US.m4a`), titulky, které nejdou přes API, a osvědčení o zproštění, pokud ho
nevyřídil průvodce nahráním.

**Voyager 1 překročí jeden světelný den ~19. 11. 2026** (`factcheck-zaklad.md`). Ve scénáři není;
kdyby video vycházelo kolem toho data, jde o to zmínit v připnutém komentáři, ne ve videu.

Stopáž 9:40 (`work/timing.json` total 579,599 s).

> Kdyby se znovu pouštěl `tts.py`, přepočítej kapitoly a časy karet tady i v `youtube-preklady.md`
> a přegeneruj `en-US` přes `us_stopa.py`.

Pořadí podle CENY (`docs/zverejneni.md`):

```bash
V=videos/157-how-can-you-recover-data-that-never-arrived
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
How Can You Recover Data That Never Arrived?
```

> Wh-otázka, 44 znaků, shodná s `project.json` a se zdrojem uživatele. Odpověď (S30: informaci
> přibalil odesílatel předem) titul neprozrazuje.

---

## 2. Popis

```
Tear a piece off a QR code, and your phone still reads it. The same text, down to the last letter. Part of the code isn't hard to read, it is simply gone. So how can a phone read something that is no longer there? The same puzzle in miniature: someone sends you eight bits, three of them vanish on the way, and nothing that arrived tells you which way to fill the gaps.

This video goes through the simplest fix of all, saying everything three times, and why it seemed to be the price of reliability. Then Richard Hamming's lost weekends at Bell Labs and the three checks that point straight at a broken bit, erasures and the parity that keeps servers alive when a disk dies, Claude Shannon's strange promise of a limit for every channel, Reed and Solomon's five-page paper behind CDs, QR codes and Voyager at Uranus and Neptune, and the forty-five-year chase towards Shannon's limit: Robert Gallager's forgotten codes, the turbo codes that experts thought were a mistake, and the codes inside 5G, Wi-Fi and satellite television today.

Sources: R. W. Hamming, The Art of Doing Science and Engineering (1997); R. W. Hamming, Error Detecting and Error Correcting Codes, Bell System Technical Journal (1950); C. E. Shannon, A Mathematical Theory of Communication (1948); I. S. Reed and G. Solomon, Polynomial Codes over Certain Finite Fields, J. SIAM (1960); R. G. Gallager, Low-Density Parity-Check Codes, MIT (1960, 1963); C. Berrou, A. Glavieux, P. Thitimajshima, ICC Geneva (1993); D. J. C. MacKay and R. M. Neal, Electronics Letters (1996); S.-Y. Chung, G. D. Forney, T. J. Richardson, R. Urbanke, IEEE Communications Letters (2001); D. J. Costello and G. D. Forney, Channel Coding: The Road to Channel Capacity, Proceedings of the IEEE (2007); R. Ludwig and J. Taylor, Voyager Telecommunications, NASA JPL DESCANSO (2002); K. A. S. Immink, Shannon, Beethoven, and the Compact Disc; Denso Wave, QR code error correction; D. A. Patterson, G. Gibson, R. H. Katz, A Case for Redundant Arrays of Inexpensive Disks (1987).

Subtitles are written for this video, not auto-generated. An American English audio track is available as a second audio track.

CHAPTERS
00:00 A torn QR code that still scans
00:25 Eight bits, three missing
00:53 Say everything three times
01:35 Hamming's lost weekends
02:11 Three checks that point at a bit
03:05 So where did the answer come from?
03:26 When you know where the gap is
04:04 Shannon's strange promise
04:38 A proof without a recipe
05:13 When damage comes in bursts
05:55 Why a scratched CD still plays
06:19 Voyager at Uranus and Neptune
07:13 The code that already existed
07:46 "They must have made a mistake"
08:16 Gallager's codes come back
08:53 Back to our eight bits

IMAGE CREDITS
Claude Shannon portrait — MIT Photo Service, digitized by the MIT Museum, public domain
Voyager images — NASA/JPL-Caltech, public domain
```

> **Blok se kopíruje CELÝ** (`docs/zverejneni.md`). Kredity ze `sources.json`: všechny tři archivní snímky
> jsou public domain (S39 Shannon, Commons; S56 model Voyageru PIA14111 a S62 Neptun PIA01492, NASA),
> takže povinná atribuce žádná; jména jsou tam ze slušnosti a NASA o kredit žádá. S17 (reléový počítač)
> je ilustrace z ChatGPT (`art/PUVOD.md`), zbytek je kreslený kódem.
>
> **Pointa se neprozrazuje:** popis ani kapitoly neříkají, že odpověď byla přibalena předem (S09–S10, S30).
> Kapitola v 3:05 je otázka, ne odpověď; *checks that point at a bit* je mechanismus, ne odpověď na hlavní otázku.
>
> Kapitoly ze scén S01, S07, S11, S16, S22, S30, S33, S38, S43, S47, S53, S56, S63, S68, S72, S77
> (`work/timing.json`, zaokrouhleno dolů). První na 00:00, všechny ≥ 10 s (nejkratší S30 → S33, 21 s;
> poslední S77 → konec 46 s). Otázka do komentářů (S82) vlastní kapitolu nemá.
>
> **Zdroje:** z `factcheck-zaklad.md` ty, které jsou primární nebo citovatelné. Wikipedie a podklady
> „z paměti agenta“ (CCSDS, 3G/4G, Wi-Fi standardy) v popisu nejsou.

---

## 3. Náhled

C1 z `thumbnail/ZADANI.md` (ChatGPT): papírový QR kód s utrženým kusem, `QR CODE` / `TORN. STILL WORKS?`.
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
| komentáře | zapnuté (S82 je otázka do komentářů) |
| **byla použita AI** | **ne**. 70 ze 74 scén je kreslených kódem. S17 (reléový počítač u Bell Labs) je plochá ilustrace z ChatGPT (`art/PUVOD.md`), ne fotorealismus. Tři archivní snímky (Shannon, model Voyageru, Neptun) jsou upravené jen barevně. Hudba je procedurální, hlas není klon skutečné osoby. |

### Karty

| čas | scéna | cíl |
|---|---|---|
| **3:16** | S32 *like the ones in our video about Btrfs* | 141 *Btrfs checksums: how does it know your data is corrupted?* — **zatím nezveřejněné** (v `analytics/videa.json` nemá ID); kartu přidat, až vyjde |
| **7:08** | S62 *is in our video about Voyager* | 110 *How Did Voyager Send Pictures Home?* (`QUQP72iXJgM`) |

### Závěrečná obrazovka

Od **9:40 − 20 s = 9:20**, tedy S81–S82. `zaver_check` hlásí S80–S82 OK, **horní polovina je volná**
(řada bitů v S81 je posunutá dolů na `ZAVER_Y`). **Dlaždici i odběr dej do HORNÍ poloviny.**
Jako dlaždici navrhuju **110 *How Did Voyager Send Pictures Home?*** (S56–S62 na něj přímo odkazuje),
druhou nechat na „nejlepší pro diváka“. Až vyjde 141 (Btrfs checksums), je to alternativa.

---

## 6. Tagy

```
error correction, error correcting codes, how qr codes work, torn qr code, reed solomon, hamming code,
shannon limit, claude shannon, richard hamming, information theory, ldpc codes, turbo codes, parity bit,
raid parity, how cds play through scratches, voyager, channel capacity, there's more to it
```

---

## 7. Playlist

**`pocitace`** (Computers). Dopsat slug do `playlisty.json`, `analytics.py --videa`, `playlisty.py --jen pocitace`.
