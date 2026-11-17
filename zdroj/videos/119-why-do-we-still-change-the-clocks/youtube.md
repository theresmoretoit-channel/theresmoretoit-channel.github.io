# YouTube — 119 „Why Do We Still Change the Clocks?“

Stav: **draft 2 schválený 2026-10-20, překlady a Codex rozpracované**.
Stav zveřejnění je v `Témata.fods`.

| | |
|---|---|
| ID videa | — (MP4 nahraje uživatel ručně ve Studiu) |
| master | ✅ `render/final-en-119.mp4` (9:37, 1920×1080, 44 MB, render 2026-10-20 na .207 za 498 s, `ffmpeg -v error` čistý) |
| náhled | ❌ ještě není |
| nastavení, popis, tagy | podklady níž |
| lokalizace | `youtube-preklady.md`, 13 jazyků |
| titulky | `subtitles/*.srt`, 14 jazyků + `en-US`, až po Codexu |
| americká stopa | `render/audio-en-US.m4a`, ručně ve Studiu |
| závěrečná obrazovka | ručně ve Studiu |
| karty | žádné |
| playlist | `legacy` (*Legacy Tech — The Old Systems Still Running Everything*), na konec |

**Co musí uživatel naklikat sám:** závěrečnou obrazovku, americkou
audiostopu (`render/audio-en-US.m4a`) a osvědčení o zproštění, pokud ho
nevyřídil průvodce nahráním.

Stopáž 9:37 (`work/timing.json` total 577,9 s).

> Kdyby se znovu pouštěl `tts.py`, přepočítej kapitoly tady
> i v `youtube-preklady.md` a přegeneruj `en-US` přes `us_stopa.py`.

> **Před nahráním znovu ověř, že Senát o H.R. 139 nehlasoval**
> (`factcheck.md`, S05): S05 říká *„It's now stuck in the Senate."*
> BILLSTATUS: https://www.govinfo.gov/bulkdata/BILLSTATUS/119/hr/BILLSTATUS-119hr139.xml

Pořadí podle CENY (`docs/zverejneni.md`):

```bash
V=videos/119-why-do-we-still-change-the-clocks
python tools/nahraj.py $V --k-videu=<ID> --bez-titulku   # 100
python tools/analytics.py --videa                        #   1  ← nutné
python tools/lokalizace.py $V                            #  50
python tools/titulky.py $V --smaz-asr                    # 150  ← před titulky
python tools/titulky.py $V                               # 400×15
python tools/playlisty.py                                #  50
# úklid, až je MP4 na YouTube:
rm $V/render/draft*.mp4
ssh vrana@192.168.0.207 'rm -rf /home/vrana/temp/render-119-why-do-we-still-change-the-clocks'
```

---

## 1. Titul

```
Why Do We Still Change the Clocks?
```

> Wh-otázka, 34 znaků, shodná s `project.json`. Odpověď titul
> neprozrazuje.

---

## 2. Popis

```
Twice a year, most of America moves its clocks by one hour, and every time the same argument starts: it's bad for our health, it's pointless, just pick one time and keep it. In 2022 the US Senate passed a bill to stop the switch without a single objection. In 2026 the House passed another one. The clocks are still changing.

So if changing the clocks is such a bad idea, why is it so hard to stop? This video looks at the problem the clocks were meant to solve, how a wartime measure became part of everyday life, what happened when America tried daylight saving time all year in 1974, why Russia and the European Union got stuck too, how Spain lives with its clocks an hour off the Sun, and why simply changing our schedules instead is harder than it sounds.

Sources: 15 U.S.C. 260a (Uniform Time Act); Congressional Research Service, Daylight Saving Time (R44411); Congress.gov, S.623 (117th Congress) and H.R. 139 (119th Congress); Public Laws 93-182 and 93-434 (1973, 1974); Office of the House Historian, Daylight Saving Time (2019); IANA Time Zone Database, NEWS; European Commission, public consultation on summertime arrangements (2018); European Parliament, vote of 26 March 2019; Planesas, Anuario del Observatorio Astronómico de Madrid (2013); Martín-Olalla, Scientific Reports (2018); Fritz et al., Current Biology (2020); Janszky & Ljung, New England Journal of Medicine (2008); Sandhu et al., Open Heart (2014). Sunrise and sunset times are calculated with the NOAA solar algorithm.

Subtitles are written for this video, not auto-generated. An American English audio track is available as a second audio track.

CHAPTERS
00:00 The same argument every year
00:56 Daylight changes, schedules don't
02:11 A war measure
03:11 What it costs our bodies
03:36 Which time would we keep?
04:14 America tried it in 1974
04:54 The odd part of the law
05:20 Russia and Europe
06:24 Move the day, not the clock
07:29 Why not just change schedules?
08:08 Ask a programmer
08:44 So why do we still change the clocks?

IMAGE CREDITS
Postkarte zur Einführung der Sommerzeit in Deutschland am 30. April 1916 — Grafj, CC BY-SA 4.0
via Wikimedia Commons
Licences: creativecommons.org/licenses/by-sa/4.0
All other archive images are in the public domain.
```

> **Blok se kopíruje CELÝ** (`docs/zverejneni.md`). Archivní snímky
> jsou tři (S16, S18, S32); povinnou atribuci má jen S16 (CC BY-SA 4.0),
> S18 (United Cigar Stores, 1918) a S32 (NARA 555489) jsou public domain.
>
> **Pointa se neprozrazuje.** Popis končí otázkou, proč je změna
> rozvrhů těžší, než se zdá; „least bad“ (S69b) v něm není.
>
> Kapitoly ze scén S01, S08, S16, S23, S26, S31, S36, S39, S46, S54,
> S60, S64 (`work/timing.json`, zaokrouhleno dolů). Nejkratší 23 s
> (S31 → S36 je 40 s, S36 → S39 26 s, S23 → S26 25 s), první na 00:00,
> všechny ≥ 10 s. Výzva k odběru S15b (2:03) leží v kapitole
> „Daylight changes, schedules don't“.
>
> Čísla a data v popisu jsou tatáž jako ve scénáři a ve `factcheck.md`.

---

## 3. Náhled

Ještě není. Podle `docs/thumbnail-styl.md`: jeden koncept, otázka
bez odpovědi, čitelné ve 150 px.

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
| komentáře | zapnuté |
| **byla použita AI** | **ne**. 70 scén je kreslených kódem, 3 archivní snímky jsou jen barevně upravené. SDXL je v jediné scéně (S33, děti jdou po předměstské silnici před svítáním): malovaná ilustrace a generická scéna, ne skutečné místo ani událost. Hudba je procedurální, hlas není klon. |

### Závěrečná obrazovka

Od **9:18** (posledních 20 s), tedy S69, S69b a S70; S67 a S68 kreslí
taky jen do dolní poloviny. `zaver_check` prošel, horní polovina je
volná. Jako dlaždici doporučuju **102 *Why Doesn't America Use the
Metric System?*** (týž typ otázky „proč pořád to staré“), druhou nechat
na „nejlepší pro diváka“.

---

## 6. Tagy

```
daylight saving time, dst, changing the clocks, clocks go forward,
clocks go back, permanent daylight saving time, permanent standard time,
sunshine protection act, standard time, time zones, 1974 daylight saving,
uniform time act, spain time zone, circadian rhythm, eu clock change,
time zone database, there's more to it
```

---

## 7. Playlist

`legacy` (*Legacy Tech — The Old Systems Still Running Everything*), na
konec, za 102. Zapsat do `playlisty.json` při nahrání; `playlisty.py`
ho přeskočí, dokud video není v `analytics/videa.json`.
