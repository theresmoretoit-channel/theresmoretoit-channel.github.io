# YouTube — 122 „Why Do Banks Still Run on 60-Year-Old Code?“

Stav: **nahráno (`BpEbqJGJitI`) a naplánováno 2026-10-25: nastavení, náhled, 13 lokalizací a titulky `en`, `en-US` přes API; zbylých 13 titulkových stop, americká stopa a závěrečná obrazovka naklikány ručně.**
Stav zveřejnění je v `Témata.fods`.

| | |
|---|---|
| ID videa | `BpEbqJGJitI` |
| master | ✅ `render/final-en-122.mp4` (10:54, renderováno na .207) |
| náhled | ✅ `render/thumbnail.jpg`: karta z děrného štítku (ChatGPT, koncept A) a text kódem, `thumbnail/PUVOD.md` |
| nastavení, popis, tagy | podklady níž |
| lokalizace | `youtube-preklady.md`, 13 jazyků |
| titulky | `subtitles/*.srt`, 14 jazyků + `en-US`, všechny prošly Codexem (2026-10-25) |
| americká stopa | `render/audio-en-US.m4a`, ručně ve Studiu |
| závěrečná obrazovka | ručně, **horní polovina** (viz níž) |
| karty | žádné |
| playlist | `legacy` (*Legacy Tech*), na konec |

**Co musí uživatel naklikat sám:** závěrečnou obrazovku, americkou
audiostopu (`render/audio-en-US.m4a`) a osvědčení o zproštění, pokud ho
nevyřídil průvodce nahráním.

Stopáž 10:54 (`work/timing.json` total 653,7 s).

> Kdyby se znovu pouštěl `tts.py`, přepočítej kapitoly tady
> i v `youtube-preklady.md` a přegeneruj `en-US` přes `us_stopa.py`.

Pořadí podle CENY (`docs/zverejneni.md`):

```bash
V=videos/122-why-do-banks-still-run-on-60-year-old-code
python tools/nahraj.py $V --k-videu=<ID> --bez-titulku   # 100
python tools/analytics.py --videa                        #   1  ← nutné
python tools/lokalizace.py $V                            #  50
python tools/titulky.py $V --smaz-asr                    # 150  ← před titulky
python tools/titulky.py $V                               # 400×15
python tools/playlisty.py                                #  50
# úklid, až je MP4 na YouTube:
rm $V/render/draft*.mp4
ssh vrana@192.168.0.207 'rm -rf /home/vrana/temp/render-122-why-do-banks-still-run-on-60-year-old-code'
```

---

## 1. Titul

```
Why Do Banks Still Run on 60-Year-Old Code?
```

> Wh-otázka, 43 znaků, shodná s `project.json`. „60-year-old“ je jazyk
> (1959), ne každý program; úvod to upřesní v S08 (rozhodnutí uživatele,
> `notes.md`). Odpověď titul neprozrazuje.

---

## 2. Popis

```
Add one penny to £999.99 in the wrong COBOL field and the answer is zero. No error message, no crash. That isn't a bug. It's a rule, and many of the world's banks still run on rules like these.

COBOL is a programming language from 1959. So why haven't banks replaced it, when they have the money and the engineers? This video looks at why a rewrite is not a translation, how a meeting at the Pentagon gave business its common language, and three real cases: a British bank that tried to leave its old system, an Australian bank that managed it, and a pandemic crisis in New Jersey where everyone blamed COBOL.

Sources: IBM Enterprise COBOL for z/OS 6.4 Language Reference (ROUNDED, SIZE ERROR, assumed decimal point), with the examples run in GnuCOBOL 3.2; Java BigDecimal documentation; COBOL initial specifications, US Department of Defense, April 1960; IBM System/360 Principles of Operation; IBM z/Architecture Principles of Operation; IBM 10-K, fiscal 2022; SSA IT Modernization Plan, 2017; GAO-25-107795 (2025); FCA Final Notice to TSB Bank plc (2022); Slaughter and May, TSB Review (2019); TSB 2018 full-year results; Commonwealth Bank of Australia, Recent Developments (2008) and 2013 Shareholder Review; iTWire and Delimiter, February 2011; New Jersey Department of Labor, March 2020; New Jersey Office of the State Auditor (2022); WIRED, "Can't File for Unemployment? Don't Blame Cobol" (2020); Mar Hicks, "Built to Last", Logic (2020); Martin Fowler, "StranglerApplication" (2004).

Subtitles are written for this video, not auto-generated. An American English audio track is available as a second audio track.

Full transcript, sources and translations: https://theresmoretoit-channel.github.io/videos/why-do-banks-still-run-on-60-year-old-code/

CHAPTERS
00:00 Add one penny
00:46 A language from 1959
01:17 Why not just rewrite it?
02:22 How COBOL got there
03:56 How much is still running
04:41 TSB: a bank leaves
06:28 Commonwealth Bank: leaving slowly
07:32 New Jersey: everyone blamed COBOL
08:57 Three cases
09:34 Wrap it, replace it piece by piece
10:07 Back to the half penny

IMAGE CREDITS
Grace Hopper and UNIVAC — unknown author, CC BY 2.0
IBM System/360 Model 30 — ArnoldReinhold, CC BY-SA 3.0
TSB Newcastle — TubularWorld, CC BY-SA 3.0
Commonwealth Bank branch office — Maksym Kozlenko, CC BY-SA 4.0
via Wikimedia Commons
Licences: creativecommons.org/licenses/by/2.0, creativecommons.org/licenses/by-sa/3.0, creativecommons.org/licenses/by-sa/4.0
All other archive images are in the public domain.
```

> **Blok se kopíruje CELÝ** (`docs/zverejneni.md`). Archivní snímky jsou
> pět (S19, S21, S25, S34, S47); povinnou atribuci mají čtyři, pohlednice
> Pentagonu (S19) je volné dílo. Náhled není cizí fotka, atribuci nemá.
>
> **Pointa se neprozrazuje.** Popis nejmenuje závěr (S71–S72: riziko není
> jen starý systém, ale i jeho náhrada; odchod byl ta nebezpečná část)
> ani výsledek auditu v New Jersey (S60). Případy jsou popsané tak jako
> v S10 (*„a bank that tried to leave… one that managed it… a crisis
> where everyone blamed COBOL“*).
>
> „In the wrong COBOL field“ místo holého tvrzení: nula vyjde jen v poli
> na tři celé číslice (`PIC 9(3)V99`, fc S01–S04).
>
> Kapitoly ze scén S01, S08, S12, S19, S28, S33, S46, S55, S64, S67, S70
> (`work/timing.json`, zaokrouhleno dolů). Nejkratší 31 s (S08 → S12),
> první na 00:00, všechny ≥ 10 s. Výzvy k odběru (za S17 a S45) leží
> uvnitř kapitol.

---

## 3. Náhled

**YOUR BANK / WHY 1959?** nad platební kartou z děrného štítku (koncept A
ze `thumbnail/ZADANI.md`). Obrázek z ChatGPT bez textu, text vysázený kódem
(`thumbnail/gen.py`). Původ v `thumbnail/PUVOD.md`; cizí fotka to není,
takže do popisu žádná atribuce nepřibývá.

---

## 4. Titulky

`subtitles/*.srt`, 14 jazyků + `en-US`. Jazyk videa **`en-gb`** (hlas
`bf_emma`) se musí nastavit dřív, než se nahrají titulkové stopy.
Všech 12 nových překladů prošlo Codexem 2026-10-25 a nálezy jsou
zapracované (`git log`, commit „12 překladů s Codexem“).

---

## 5. Nastavení

| | |
|---|---|
| kategorie | **Science & Technology** (28) — posílá `nahraj.py` napevno |
| jazyk videa | `en-gb` |
| licence | standardní |
| pro děti | **ne** |
| komentáře | zapnuté (S73 končí otázkou do komentářů) |
| **byla použita AI** | **ne**. Většina scén je kreslená kódem, 5 archivních snímků je jen barevně upravených. Dvě SDXL scény (S07, S18) jsou malované ilustrace bez skutečného místa či události. Hudba je procedurální, hlas není klon. |

### Závěrečná obrazovka

Od **10:34** (posledních 20 s), tedy scény S72 a S73. **Dlaždici i odběr
dej do HORNÍ poloviny** (`zaver_check`: dole by šly přes titulky; závěr
S71–S73 je kreslený jen dole). Dlaždici doporučuju jako **playlist
*Legacy Tech*** (video tam patří), nebo jedno video z něj; druhou
nechat na „nejlepší pro diváka“.

---

## 6. Tagy

```
cobol, legacy systems, banking software, mainframe, tsb it failure,
tsb migration 2018, commonwealth bank core banking, new jersey cobol,
technical debt, software modernization, strangler fig pattern,
decimal arithmetic, rounding errors, grace hopper, ibm system 360,
there's more to it
```

---

## 7. Playlist

`legacy` (*Legacy Tech — The Old Systems Still Running Everything*), na
konec. Zapsat do `playlisty.json` při nahrání; `playlisty.py` ho
přeskočí, dokud video není v `analytics/videa.json`.
