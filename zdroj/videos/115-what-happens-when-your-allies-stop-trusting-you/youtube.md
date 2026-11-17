# YouTube — 115 „What Happens When Your Allies Stop Trusting You?“

Stav: **nahráno 2026-10-17, zveřejnění naplánované**; uživatel nahrál a naklikal všechno ručně ve Studiu (titulky, lokalizace, US stopu, kartu, závěrečnou obrazovku). Draft a kopie na .207 smazané. Stav zveřejnění je v `Témata.ods`.

| | |
|---|---|
| ID videa | — |
| master | ✅ `render/final-en-115.mp4` (10:42, 1920×1080, 102 MB, s hudbou, render 2026-10-17 na .207, `ffmpeg -v error` čistý) |
| náhled | ✅ `render/thumbnail.jpg` (1280×720, 0,35 MB), TRUST / WHAT’S IT WORTH?, původ v `thumbnail/PUVOD.md` |
| nastavení, popis, tagy | podklady níž |
| lokalizace | `youtube-preklady.md`, 13 jazyků |
| titulky | `subtitles/*.srt`, 14 jazyků + `en-US`, všechny překlady prošly Codexem |
| americká stopa | `render/audio-en-US.m4a`, ručně ve Studiu |
| závěrečná obrazovka | ručně ve Studiu |
| karta | 052 v 4:48 (viz níž) |
| playlist | `spolecnost`, na konec, za 103 |

**Co musí uživatel naklikat sám:** nahrát MP4 ve Studiu (průvodce vyřídí
prohlášení o AI a osvědčení o zproštění), závěrečnou obrazovku, kartu
na 052 a americkou audiostopu (`render/audio-en-US.m4a`).

Stopáž 10:42 (`work/timing.json` total 642,4 s).

> Kdyby se znovu pouštěl `tts.py`, přepočítej kapitoly tady
> i v `youtube-preklady.md` a přegeneruj `en-US` přes `us_stopa.py`.

> **Těsně před nahráním** (`factcheck.md`, „Před nahráním znovu
> zkontrolovat“): summit EU–Kanada 29.–30. 10. 2026 (S46–S48), GL 135
> (S32–S34), kanadských 72 F-35 (S40). Ověřeno 2026-10-17: summit ještě
> nebyl, GL 135 platí do 7. 4. 2027, o F-35 se nerozhodlo. Když se video
> nahraje až po summitu, ověř S48 znovu.

Pořadí podle CENY (`docs/zverejneni.md`):

```bash
V=videos/115-what-happens-when-your-allies-stop-trusting-you
python tools/nahraj.py $V --k-videu=<ID> --bez-titulku    # 100
python tools/analytics.py --videa                         #   1  ← nutné
python tools/lokalizace.py $V                             #  50
python tools/titulky.py $V --smaz-asr                     # 150  ← před titulky
python tools/titulky.py $V                                # 400×15
python tools/playlisty.py                                 #  50
# úklid, až je MP4 na YouTube:
rm $V/render/draft*.mp4
ssh vrana@192.168.0.207 'rm -rf /home/vrana/temp/render-115-what-happens-when-your-allies-stop-trusting-you'
```

---

## 1. Titul

```
What Happens When Your Allies Stop Trusting You?
```

> Wh-otázka, 48 znaků, shodná s `project.json`. Odpověď (spojenci se
> jistí a USA ztrácí, co dostávaly zadarmo) titul neprozrazuje.

---

## 2. Popis

```
Article 5 of the NATO treaty has been invoked exactly once, and not for anyone in Europe. It was invoked for the United States, after September 11. Over the next twenty years, Britain lost 457 soldiers in Afghanistan, Canada lost 158, and Denmark, a country of six million, lost 44. Twenty-five years later, only 11 per cent of Europeans in a large survey call the United States an ally.

So what happens to the most powerful country on Earth when its allies stop trusting it? Nobody storms out of an alliance. What happens is quieter: a second factory, a second supplier, a backup plan. This video follows that backup plan from Brussels to Madrid, Ottawa and Seoul, and then asks what the United States was getting from trust all along.

Related: Why Would Canada Join the European Union? https://www.youtube.com/watch?v=gEEn2K12lZY

Sources: North Atlantic Treaty (1949), Article 5; NATO, Collective defence and Article 5; UK Ministry of Defence, FOI response (2021); Veterans Affairs Canada; Danish Parliament, resolution B 37 (2001); ECFR, Kobzová & Zerka, Home alone: Europeans are ready to defend themselves (2026); Kiel Institute, Ukraine Support Tracker (2026); US Treasury OFAC, General License 135 (2026); US EIA, distillate fuel oil data (2026); Regulation (EU) 2025/1106 (SAFE); Council of the EU, EU–Canada SAFE agreement (2026); Gallup Korea (August 2026); Nanos Research for The Globe and Mail (April 2026); NATO, The Hague Summit Declaration (2025); IMF, COFER (2026); SIPRI, Trends in International Arms Transfers (2026); IISS (2025); B. Eichengreen, Exorbitant Privilege (2011).

Subtitles are written for this video, not auto-generated. An American English audio track is available as a second audio track.

CHAPTERS
00:00 Article 5, invoked once
00:57 An ally doing the maths
01:17 The question
01:37 Why trust is not soft
02:27 Reasons to wonder
03:51 The backup plan
04:48 And then there is Canada
05:30 The part that should sting
06:20 What trust was buying
08:16 A country with options
08:43 Why it is hard to undo
09:25 Still the strongest
09:43 The first call
10:16 If you are watching in the United States

IMAGE CREDITS
Nuuk, Greenland skyline aerial view — Quintin Soloviev, CC BY 4.0
via Wikimedia Commons
Licence: creativecommons.org/licenses/by/4.0
All other archive images are in the public domain.
```

> **Blok se kopíruje CELÝ** (`docs/zverejneni.md`). Archivních snímků je
> sedm (S05, S12, S14, S15, S16, S30, S40), povinnou atribuci má jen Nuuk
> (S30, CC BY 4.0); ostatních šest je public domain.
>
> **Pointa se neprozrazuje.** Popis končí otázkou, co USA z důvěry
> dostávaly; že to ztrácí a že je to těžko vratné (S55–S62), je výplata.
> Kapitoly *„Why it is hard to undo“* a *„What trust was buying“* říkají
> téma, ne závěr.
>
> Kapitoly ze scén S01, S07, S10, S22, S28, S38, S44, S49, S54c, S55, S58,
> S63, S65, S69b (`work/timing.json`, zaokrouhleno dolů). Nejkratší 18 s
> (S63 → S65), všechny ≥ 10 s, první na 00:00. Výzva k odběru S54b (6:13)
> leží v kapitole „The part that should sting“.
>
> Čísla v popisu (457, 158, 44, šest milionů, 11 %) jsou tatáž jako ve
> scénáři a ve `factcheck.md`. Zdroje podle `factcheck.md`; zprávy
> (Reuters, AP, CNBC, AAA) se necitují, citují se primární prameny.
> Popis říká *„in a large survey“* jako S07, ne „Europeans think“.

---

## 3. Náhled

`render/thumbnail.jpg` — rozbité zrcadlo s vlajkou USA, TRUST /
WHAT’S IT WORTH?. Vlastní nápad uživatele, ne koncept ze `ZADANI.md`;
původ, otisk a thumb_check v `thumbnail/PUVOD.md`.

---

## 4. Titulky

`subtitles/*.srt`, 14 jazyků + `en-US`. Jazyk videa **`en-gb`** (hlas
`bf_emma`) se musí nastavit dřív, než se nahrají titulkové stopy.
Všechny překlady prošly Codexem a čeština uživatelem (oprava S67 *speed
dial* přenesená do es, pl, id, vi).

---

## 5. Nastavení

| | |
|---|---|
| kategorie | **Science & Technology** (28) — posílá `nahraj.py` napevno |
| jazyk videa | `en-gb` |
| licence | standardní |
| pro děti | **ne** |
| komentáře | zapnuté |
| **byla použita AI** | **ne**. Většina scén je kreslená kódem, 7 archivních snímků je jen barevně upravených. SDXL je ve dvou scénách: S22 je malovaná ilustrace, S38 je fotorealističtější, ale **generická tovární hala**, ne skutečné místo ani událost, takže podle pravidel YouTube prohlášení nespouští. Hudba je procedurální, hlas není klon. |

### Závěrečná obrazovka

Od **10:22** (posledních 20 s), tedy S69b–S69d, které mají obraz S67.
Před nahráním `python tools/zaver_check.py $V` a prvky dát tam, kam
ukáže. Jako dlaždici dalšího videa doporučuju **052 *Why Would Canada
Join the European Union?*** — navazuje na blok o Kanadě.

### Karta

**052 v 4:48** (S44 *„And then there is Canada.“*). Je to jediné místo,
kde video samo o 052 mluví, a leží daleko za první půlminutou.

---

## 6. Tagy

```
nato, article 5, allies, alliances, trust, us allies, transatlantic relations,
europe defence, eu safe, rearmament, canada eu, greenland, denmark,
south korea nuclear, f-35, exorbitant privilege, us dollar, export controls,
geopolitics explainer, there's more to it
```

---

## 7. Playlist

`spolecnost` (*How Society Actually Runs*), na konec, za 103.
Zapsáno v `playlisty.json`; `playlisty.py` ho přeskočí, dokud video
není v `analytics/videa.json`.
