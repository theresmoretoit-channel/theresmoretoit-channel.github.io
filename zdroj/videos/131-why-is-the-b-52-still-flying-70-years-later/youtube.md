# YouTube — 131 „Why Is the B-52 Still Flying, 70 Years Later?“

Stav: **nahráno 2026-11-02** (https://youtu.be/1cCc77q7jlE): nastavení, popis, náhled, lokalizace 13 jazyků, titulky 15 stop, playlist `legacy`. ASR při mazání ještě nebyl. Ručně zbývá závěrečná obrazovka a americká stopa.
Stav zveřejnění je v `Témata.fods`.

| | |
|---|---|
| ID videa | `1cCc77q7jlE` |
| master | ✅ `render/final-en-131.mp4` (9:03, 1920×1080, 50 MB, render 2026-11-02 na .207 za 582 s, `ffmpeg -v error` čistý) |
| náhled | ✅ `render/thumbnail.jpg`: 1962 / STILL FLYING IN 2050?, koncept B překreslený v ChatGPT, `thumbnail/PUVOD.md` |
| nastavení, popis, tagy | podklady níž |
| lokalizace | `youtube-preklady.md`, 13 jazyků |
| titulky | ✅ `subtitles/*.srt`, 14 jazyků + `en-US`, po Codexu (`notes.md`) |
| americká stopa | ✅ `render/audio-en-US.m4a`, ručně ve Studiu |
| závěrečná obrazovka | S110–S114, **horní polovina** (viz níž) |
| karty | žádné |
| playlist | ✅ `legacy`, hned za 079 (DC-3) |

**Co musí uživatel naklikat sám:** závěrečnou obrazovku, americkou
audiostopu (`render/audio-en-US.m4a`) a osvědčení o zproštění, pokud ho
nevyřídil průvodce nahráním.

Stopáž 9:03 (`work/timing.json` total 543,3 s).

> Kdyby se znovu pouštěl `tts.py`, přepočítej kapitoly tady
> i v `youtube-preklady.md` a přegeneruj `en-US` přes `us_stopa.py`.

Pořadí podle CENY (`docs/zverejneni.md`):

```bash
V=videos/131-why-is-the-b-52-still-flying-70-years-later
python tools/nahraj.py $V --k-videu=1cCc77q7jlE --bez-titulku   # 100
python tools/analytics.py --videa                        #   1  ← nutné
python tools/lokalizace.py $V                            #  50
python tools/titulky.py $V --smaz-asr                    # 150  ← před titulky
python tools/titulky.py $V                               # 400×15
python tools/playlisty.py                                #  50
# úklid, až je MP4 na YouTube:
rm $V/render/draft*.mp4
ssh vrana@192.168.0.207 'rm -rf /home/vrana/temp/render-131-why-is-the-b-52-still-flying-70-years-later'
```

---

## 1. Titul

```
Why Is the B-52 Still Flying, 70 Years Later?
```

> Wh-otázka, 45 znaků, shodná s `project.json`. Odpověď (postavený kolem
> úkolu, ne kolem technologie) titul neprozrazuje.

---

## 2. Popis

```
The last B-52 left the factory in 1962. In some American families, three generations have flown in it, and the US Air Force plans to keep it flying into the 2050s. It has already outlived the bomber that was meant to replace it. So why does the most powerful air force in the world keep flying its oldest bomber?

This video follows the B-52 from a weekend in a Dayton hotel in 1948, where Boeing engineers redesigned it and carved a balsa model, through three completely different jobs: flying high into the Soviet Union, flying low under the radar, and carrying cruise missiles. Along the way: the XB-70 Valkyrie, a test flight that lost most of its tail fin, why a wing wears out by flying rather than by age, a bomber brought back from the Arizona desert, and why the new B-52J keeps eight engines instead of four.

Sources: National Museum of the US Air Force (XB-70 Valkyrie, AGM-86B ALCM, the Powers incident); Boeing, B-52 Design: Dayton Hotel Birthplace of Jet-powered Bomber (2002); AFLCMC History Office, The B-52's First Flight (2026); US Air Force B-52H fact sheet; Barksdale AFB, Ripped Off: The Story of No. 61-023; President Carter's news conference of 30 June 1977; Air & Space Forces Magazine, A Tale of Two Bombers and U-2 Down; US Office of the Historian on the U-2 incident; US Government Accountability Office, GAO-26-109272 (July 2026); Defense Science Board, Task Force on B-52H Re-Engining (2004); Defense News, September 2026.

Subtitles are written for this video, not auto-generated. An American English audio track is available as a second audio track.

CHAPTERS
00:00 Built in 1962, set to fly into the 2050s
00:38 The first part of the answer
01:22 A weekend in a Dayton hotel
02:10 Job one: fly high
02:57 Job two: fly low
03:33 Job three: carry the missiles
04:35 How is it still flying?
05:35 Back from the desert
05:55 Many of them, and cheap to fly
06:26 What's inside it today
06:47 Why still eight engines?
07:42 The newest bomber and the oldest
08:05 So why is it still flying?
08:50 A question for you

IMAGE CREDITS
All archive images are in the public domain (US Air Force, US Navy and others, via Wikimedia Commons).
```

> **Blok se kopíruje CELÝ** (`docs/zverejneni.md`). Všech sedm archivních
> snímků (S18, S31, S34, S63, S70, S72, S96) je public domain
> (`sources.json`), takže povinná atribuce není. **Až vznikne náhled
> s cizí fotkou pod CC BY*, musí sem i do všech 13 lokalizací přibýt
> její řádek TASL.**
>
> **Pointa se neprozrazuje:** popis nejmenuje závěr S105–S107 (*„built
> around a technology / around a job“*) ani odpověď na otázku z S13.
>
> **Zdroje** jsou hlavní zdroje z `factcheck-zaklad.md` (GAO-26-109272
> z 31. 7. 2026 je zpráva, kterou citují scény o počtu a opotřebení;
> DSB 2004 je podklad k S89–S93). Havárie z 15. 6. 2026 se v popisu
> nezmiňuje (rozhodnutí v `notes.md`).
>
> Kapitoly ze scén S01, S08, S18, S28, S37, S43, S57, S69, S74, S79, S84,
> S96, S102, S112 (`work/timing.json`, zaokrouhleno dolů). Nejkratší
> 12,5 s (S112 → konec), první na 00:00, všechny ≥ 10 s. Výzvy k odběru
> (za S20 a S55) leží uvnitř kapitol.

---

## 3. Náhled

**1962 / STILL FLYING IN 2050?** nad B-52 na tmavém pozadí (koncept B
ze tří, vybral uživatel 2026-11-02 a nechal ho překreslit v ChatGPT).
Letadlo vychází z public-domain fotky S72, atribuce se nepřidává.
Původ, otisk a ověření textu v `thumbnail/PUVOD.md`.

---

## 4. Titulky

`subtitles/*.srt`, 14 jazyků + `en-US`. Jazyk videa **`en-gb`** (hlas
`bf_emma`) se musí nastavit dřív, než se nahrají titulkové stopy.
Codex hotový a zapracovaný (`notes.md`, „Překlady“).

---

## 5. Nastavení

| | |
|---|---|
| kategorie | **Science & Technology** (28) — posílá `nahraj.py` napevno |
| jazyk videa | `en-gb` |
| licence | standardní |
| pro děti | **ne** |
| komentáře | zapnuté (S112–S114 je otázka do komentářů) |
| **byla použita AI** | **ne**. Scény jsou kreslené kódem (diagramy, animace), 7 archivních snímků je public domain a jen barevně upravených. SDXL ve videu není. Hudba je procedurální, hlas není klon. |

### Závěrečná obrazovka

Od **8:43** (posledních 20 s), tedy S110–S114. `zaver_check` u všech
pěti hlásí OK s volnou **horní** částí rámu a radí nedávat nic dolů
přes titulky. **Dlaždici i odběr dej do HORNÍ poloviny.** Jako dlaždici
doporučuju **079 *Why Is This 90-Year-Old Airplane Still Flying?*** (DC-3,
táž otázka u dopravního letadla), druhou nechat na „nejlepší pro diváka“.

---

## 6. Tagy

```
b-52, b-52 stratofortress, b-52j, boeing b-52, strategic bomber,
xb-70 valkyrie, b-1 lancer, b-2 spirit, b-21 raider, cruise missile,
cold war aviation, us air force, military aviation history,
amarg boneyard, rolls-royce f130, old planes still flying,
legacy technology, there's more to it
```

---

## 7. Playlist

`legacy` (*Legacy Tech — The Old Systems Still Running Everything*),
hned za 079 (DC-3). Zapsat do `playlisty.json` při nahrání;
`playlisty.py` ho přeskočí, dokud video není v `analytics/videa.json`.
