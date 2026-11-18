# YouTube — 158 „Why Can't We Compress Everything?“

Stav: **zveřejněno 2026-11-16 (`CKkeohuyqHU`), všechno nahráno včetně ručních kroků.** Master hotový (207, 2026-11-16), americká stopa hotová.

| | |
|---|---|
| ID videa | `CKkeohuyqHU` |
| master | `render/final-en-158.mp4` (207, 1920×1080, 639,6 s, 46,5 MB, dekódováno bez chyby) |
| náhled | ✅ C1 zip složky, `ZIP` / `FOREVER?`, `render/thumbnail.jpg` (`thumbnail/PUVOD.md`) |
| nastavení, popis, tagy | podklady níž |
| lokalizace | `youtube-preklady.md`, 13 jazyků |
| titulky | `subtitles/<kód>.srt`, 14 jazyků + `en-US` |
| americká stopa | `render/audio-en-US.m4a` (`us_stopa.py`), ručně ve Studiu |
| závěrečná obrazovka | S85–S86, **horní polovina** (viz níž) |
| karty | **jedna**, viz níž |
| playlist | `pocitace` (Computers) |

**Co musí uživatel naklikat sám:** závěrečnou obrazovku, kartu, americkou audiostopu
(`render/audio-en-US.m4a`), titulky, které nejdou přes API, a osvědčení o zproštění, pokud ho
nevyřídil průvodce nahráním.

Stopáž 10:40 (`work/timing.json` total 639,549 s).

> Kdyby se znovu pouštěl `tts.py`, přepočítej kapitoly a čas karty tady i v `youtube-preklady.md`
> a přegeneruj `en-US` přes `us_stopa.py`.

Pořadí podle CENY (`docs/zverejneni.md`):

```bash
V=videos/158-why-cant-we-compress-everything
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
Why Can't We Compress Everything?
```

> Wh-otázka, 33 znaků, shodná s `project.json`. Odpověď (holubník, S28–S33) titul neprozrazuje.

---

## 2. Popis

```
Take every script ever written for this channel, almost one and a half million bytes of text, and run it through gzip. Almost two thirds of it disappears, and nothing is lost. Now compress the result again, and it gets bigger. Ninety-eight bytes bigger, every single time. So why can't we just keep compressing? And could a cleverer program, someday, shrink anything you give it?

This video goes through the two tricks inside ZIP and gzip: Jacob Ziv and Abraham Lempel's pointers back to earlier text, and David Huffman's code from a term paper he had almost given up on. Then a little counting puzzle with three-bit files, a 1992 product that claimed to be exempt from the laws of information theory, why JPEG plays a different game, Claude Shannon's guessing game and the limit no lossless code can beat, the Hutter Prize and its half a million euros for squeezing Wikipedia, how Dropbox saved forty-six petabytes on photos it had already stored, a large language model used as a compressor, and the strange case of a million digits of pi.

Sources: J. Ziv and A. Lempel, A Universal Algorithm for Sequential Data Compression, IEEE Transactions on Information Theory (1977); D. A. Huffman, A Method for the Construction of Minimum-Redundancy Codes, Proceedings of the IRE (1952); G. Stix, Profile: David A. Huffman, Scientific American (1991); P. Deutsch, RFC 1951 and RFC 1952 (1996); C. E. Shannon, A Mathematical Theory of Communication (1948); C. E. Shannon, Prediction and Entropy of Printed English, Bell System Technical Journal (1951); J.-l. Gailly, comp.compression FAQ (1999); D. R. Horn et al., The Design, Implementation, and Deployment of a System to Transparently Compress Hundreds of Petabytes of Image Files for a File-Storage Service, NSDI (2017); M. Hutter, Hutter Prize for Lossless Compression of Human Knowledge (prize.hutter1.net); M. Mahoney, Large Text Compression Benchmark; G. Delétang et al., Language Modeling Is Compression, ICLR (2024); A. N. Kolmogorov, Three Approaches to the Quantitative Definition of Information (1965); G. J. Chaitin, Information-Theoretic Limitations of Formal Systems (1974). The gzip and pi measurements were made for this video.

Subtitles are written for this video, not auto-generated. An American English audio track is available as a second audio track.

Full transcript, sources and translations: https://theresmoretoit-channel.github.io/videos/why-cant-we-compress-everything/

CHAPTERS
00:00 Every script on this channel, compressed
00:24 Compress it again
00:46 Inside the second file
01:17 Pointing back at repeats
01:44 Huffman's term paper
02:38 ZIP and gzip
02:58 Could a cleverer program do it?
04:16 Software that promised too much
04:39 How do photos get so small?
05:08 Is there a bottom?
05:45 Shannon's guessing game
06:28 The Hutter Prize
07:14 Programs that predict
07:59 A language model as a compressor
08:40 A million digits of pi
09:24 The shortest program
10:11 What gzip can't see

IMAGE CREDITS
Robert Fano — 121a0012, CC BY 3.0
Marcus Hutter — Marcus Hutter, CC BY-SA 4.0
Andrey Kolmogorov — Konrad Jacobs, CC BY-SA 2.0 DE
Kingfisher photo — Alexis LOURS, CC BY 2.0 (cropped, recompressed)
via Wikimedia Commons
Licences: creativecommons.org/licenses/by/3.0, creativecommons.org/licenses/by-sa/4.0, creativecommons.org/licenses/by-sa/2.0/de, creativecommons.org/licenses/by/2.0
Claude Shannon portrait — MIT Photo Service, public domain
```

> **Blok se kopíruje CELÝ** (`docs/zverejneni.md`). Kredity: tři snímky ze `sources.json` s CC BY*
> (S17 Fano, S61 Hutter, S79 Kolmogorov) a **fotka ledňáčka S40–S42, která v `sources.json`
> ani v `CREDITS.md` NENÍ** (leží v `art/`, znění z `art/PUVOD.md`). S45 Shannon je public domain.
> S16 a S49 jsou malované ilustrace z ChatGPT (`art/PUVOD.md`), zbytek je kreslený kódem.
>
> **Pointa se neprozrazuje:** popis ani kapitoly neříkají, proč nejde komprimovat všechno
> (holubník S28–S33) ani kde je dno (entropie S47). Kapitola 02:58 je otázka, ne odpověď;
> *a little counting puzzle* jmenuje metodu, ne výsledek.
>
> Kapitoly ze scén S01, S04, S08, S12, S15, S23, S26, S37, S40, S44, S49, S56, S62, S67, S72, S78, S84
> (`work/timing.json`, zaokrouhleno dolů). První na 00:00, všechny ≥ 10 s (nejkratší S23 → S26, 20 s;
> poslední S84 → konec 28 s). Otázka do komentářů (S86) vlastní kapitolu nemá.
>
> **Zdroje:** z `factcheck-zaklad.md` ty, které jsou primární nebo citovatelné. Wikipedie, Corecursive
> (Sloot, ve scénáři není) a rešerše „z paměti agenta“ v popisu nejsou.

---

## 3. Náhled

C1 z `thumbnail/ZADANI.md` (ChatGPT): pět zmenšujících se zip složek, `ZIP` / `FOREVER?`.
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
| komentáře | zapnuté (S86 je otázka do komentářů) |
| **byla použita AI** | **ne**. Většina scén je kreslená kódem. S16 (pracovna 1951) a S49 (Shannonova hádací hra) jsou malované ilustrace z ChatGPT (`art/PUVOD.md`), ne fotorealismus. Fotka ledňáčka (S40–S42) je skutečná fotka, jen zmenšená a překomprimovaná — JPEG artefakty v S42 jsou skutečné. Čtyři archivní portréty (Fano, Shannon, Hutter, Kolmogorov) jsou upravené jen barevně. Hudba je procedurální, hlas není klon skutečné osoby. |

### Karty

| čas | scéna | cíl |
|---|---|---|
| **5:14** | S45 *the same paper behind our video on error-correcting codes* | 157 *How Can You Recover Data That Never Arrived?* (`fcdsXgB1Z60`) |

### Závěrečná obrazovka

Od **10:40 − 20 s = 10:20**, tedy S85–S86. `zaver_check` hlásí obě OK, **dolní rohy NE**
(přes titulek), horní polovina je volná. **Dlaždici i odběr dej do HORNÍ poloviny.**
Jako dlaždici navrhuju **157 *How Can You Recover Data That Never Arrived?*** (S45–S46 na něj přímo
odkazuje, týž Shannonův článek), druhou nechat na „nejlepší pro diváka“.

---

## 6. Tagy

```
data compression, how compression works, why cant you compress a zip file, gzip, zip, huffman coding,
david huffman, lempel ziv, lossless compression, pigeonhole principle, claude shannon, entropy,
information theory, hutter prize, kolmogorov complexity, language models compression, there's more to it
```

---

## 7. Playlist

**`pocitace`** (Computers). Dopsat slug do `playlisty.json`, `analytics.py --videa`, `playlisty.py --jen pocitace`.
