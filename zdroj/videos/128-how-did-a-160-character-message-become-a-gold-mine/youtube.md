# YouTube — 128 „How Did a 160-Character Message Become a Gold Mine?“

Stav: **MP4 nahráno ručně ve Studiu 2026-10-31; metadata, náhled, 13 lokalizací, 15 titulkových stop a playlist nahrané.** Stav zveřejnění je v `Témata.fods`. Stav zveřejnění je v `Témata.fods`.

| | |
|---|---|
| ID videa | `CzaE8TpZQTg` |
| master | ✅ `render/final-en-128.mp4` (9:23, 1920×1080, 563,1 s), herní PC 2026-10-31 |
| náhled | ✅ `render/thumbnail.jpg` z konceptu B (`thumbnail/PUVOD.md`) |
| nastavení, popis, tagy | podklady níž |
| lokalizace | `youtube-preklady.md`, 13 jazyků |
| titulky | `subtitles/*.srt`, 14 jazyků + `en-US` (Codex hotový na všech 13) |
| americká stopa | `render/audio-en-US.m4a`, ručně ve Studiu |
| závěrečná obrazovka | od **9:03**, S107–S110, prvky **nahoru** (viz níž) |
| karta | žádná |
| playlist | `legacy` (*Legacy Tech — The Old Systems Still Running Everything*), na konec |

**Co musí uživatel naklikat sám:** závěrečnou obrazovku, americkou
audiostopu (`render/audio-en-US.m4a`) a osvědčení o zproštění, pokud ho
nevyřídil průvodce nahráním.

Stopáž 9:23 (`work/timing.json` total 563,03 s).

> Kdyby se znovu pouštěl `tts.py`, přepočítej kapitoly tady
> i v `youtube-preklady.md` a přegeneruj `en-US` přes `us_stopa.py`.

Pořadí podle CENY (`docs/zverejneni.md`):

```bash
V=videos/128-how-did-a-160-character-message-become-a-gold-mine
python tools/nahraj.py $V --k-videu=CzaE8TpZQTg --bez-titulku          # 100
python tools/analytics.py --videa                               #   1  ← nutné
python tools/lokalizace.py $V                                   #  50
python tools/titulky.py $V --smaz-asr                           # 150  ← před titulky
python tools/titulky.py $V                                      # 400×15
python tools/playlisty.py                                       #  50
# úklid, až je MP4 na YouTube:
rm $V/render/draft*.mp4
```

---

## 1. Titul

```
How Did a 160-Character Message Become a Gold Mine?
```

> Wh-otázka, 51 znaků, shodná s `project.json`. Neprozrazuje ani původ
> čísla 160 (S08–S24), ani proč byl důl tak výnosný (S53–S64).

---

## 2. Popis

```
In the early 2000s, mobile operators were selling data at a price that sounds absurd today: more than seven hundred dollars a megabyte. Not mobile internet. Text messages. So how did a tiny side feature of the mobile network become a gold mine? And why was every message limited to exactly 160 characters?

This video follows the text message from a typewriter in 1985 to the phone in your pocket: where the number 160 really came from, why a single accented letter could cut your message by more than half, what the very first text said, and how a message could wait for a phone that was switched off.

Along the way: free texting from operators' own websites, why MMS was the awkward teenager of messaging, how internet messaging apps bypassed the gold mine, and why SMS still carries your login codes when nothing else works.

Sources: 3GPP TS 23.038, Alphabets and language-specific information (ETSI TS 123 038, V18.0.0); 3GPP TS 23.040, Technical realization of the Short Message Service (ETSI TS 123 040, V18.0.0); Open Mobile Alliance, MMS Conformance Document 1.3 (2011); M. Milian, interview with Friedhelm Hillebrand, Los Angeles Times (May 2009); F. Hillebrand (ed.), Short Message Service (SMS): The Creation of Personal Global Text Messaging, Wiley (2010); ITU, The World in 2010: ICT Facts and Figures; GSMA, RCS Universal Profile.

Subtitles are written for this video, not auto-generated. An American English audio track is available as a second audio track.

IMAGE CREDITS
Nokia 1011 — Jkbw, CC BY 3.0
via Wikimedia Commons
Licences: creativecommons.org/licenses/by/3.0
All other archive images are in the public domain.

Full transcript, sources and translations: https://theresmoretoit-channel.github.io/videos/how-did-a-160-character-message-become-a-gold-mine/

CHAPTERS
00:00 Data at an absurd price
00:36 Where 160 came from
01:12 The network's spare capacity
01:46 140 bytes, 160 characters
02:22 One letter can halve a message
03:00 The first text message
03:38 Store and forward
04:06 Texting takes off
04:40 The gold mine
05:37 Free texting, one window away
06:06 MMS
06:59 Messaging over the internet
07:38 Why SMS never went away
08:05 RCS
08:39 Back to 160 characters
```

> **Blok se kopíruje CELÝ** (`docs/zverejneni.md`). Archiv má dva snímky
> (`CREDITS.md`): S15 Nokia 1011 (Jkbw, **CC BY 3.0**) v TASL uvnitř
> bloku, S12 dálnopis (GPO photographer) je public domain.
>
> **Pointa se neprozrazuje.** Popis položí obě otázky ze S06–S07; že 160
> vyšlo z 1120 bitů / 7 a že rám natáhli ze 146 (S21–S24), neříká.
> „A single accented letter could cut your message by more than half“
> je S30 jako téma, ne vysvětlení. „What the very first text said“ je
> otázka (S36), ne citace.
>
> **Nic netvrdí víc než video** (`factcheck.md`): přes 700 USD za MB při
> 10 c a desítkovém MB (S04), 1985 a psací stroj (S09), MMS jako
> „awkward teenager“ (S81), obejití dolu (S89), přihlašovací kódy (S95).
>
> Kapitoly ze scén S01, S08, S14, S20, S25, S32, S39, S45, S52, S65, S70,
> S82, S90, S97, S103 (`work/timing.json`, zaokrouhleno dolů). Nejkratší
> má 28 s (S39 → S45), všechny ≥ 10 s. Výzvy k odběru (za S24 a S64)
> leží uvnitř kapitol.
>
> Zdroje jsou z `factcheck.md`: primární specifikace a Hillebrandův
> rozhovor; ceny (Kohl 2008) a novinové zdroje k RCS se neuvádějí,
> ITU je u počtu zpráv za den (S05).

---

## 3. Náhled

Koncept **B** z `thumbnail/ZADANI.md` (displej starého telefonu
s počítadlem 160, SMS / WHY ONLY 160?), obrázek z ChatGPT. Původ, otisk
a `thumb_check` v `thumbnail/PUVOD.md`.

---

## 4. Titulky

`subtitles/*.srt`, 14 jazyků + `en-US`. Jazyk videa **`en-gb`** (hlas
`bf_emma`) se musí nastavit dřív, než se nahrají titulkové stopy.
Nahrávají se **až po zapracování nálezů Codexu** (hotovo).

---

## 5. Nastavení

| | |
|---|---|
| kategorie | **Science & Technology** (28), posílá `nahraj.py` napevno |
| jazyk videa | `en-gb` |
| licence | standardní |
| pro děti | **ne** |
| komentáře | zapnuté (S110 končí otázkou do komentářů) |
| **byla použita AI** | **ne**. Čtyři SDXL scény (S33 ulice, S45 zastávka v dešti, S52 stožár nad městem, S90 stožár s chalupou) jsou malované ilustrace podle kotvy stylu, žádné skutečné místo ani událost. Archivní snímky (S12, S15) jsou upravené jen barevně, ostatní scény jsou kresba kódem (30 animovaných). Hudba procedurální, hlas není klon. |

### Závěrečná obrazovka

Od **9:03** (posledních 20 s z 563,0), tedy S107 (od 540,4 s) až S110.
`zaver_check` u všech čtyř hlásí volnou horní polovinu (dole je titulek),
**dlaždici i kolečko odběru dej nahoru**. Jako dlaždici jednoznačně
**129 *Why Are iPhone Texts to Android Still Green?*** — S107–S109
na ni přímo odkazují („the best-known phone in the world simply didn't
speak it … a story for another video“). Pokud 129 ještě nevyjde,
**089 *Why Can You Still Buy a Phone With a Keyboard?***, a 129 doplnit
po jejím zveřejnění.

---

## 6. Tagy

```
how did a 160 character message become a gold mine, sms, text message,
160 characters, why are texts 160 characters, friedhelm hillebrand, gsm,
gsm 7-bit alphabet, short message service, first text message, mms,
rcs, rich communication services, signaling channel, store and forward,
history of texting, mobile operators, tech history explainer,
there's more to it
```

---

## 7. Playlist

**`legacy`** (*Legacy Tech — The Old Systems Still Running Everything*),
na konec za 122. SMS je přesně ten případ: systém z osmdesátých let,
který pořád nese přihlašovací kódy.
