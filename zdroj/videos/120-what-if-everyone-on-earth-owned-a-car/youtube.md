# YouTube — 120 „What If Everyone on Earth Owned a Car?“

Stav: **nahráno (`NuLh-NGHd9g`), zveřejnění naplánované; zbytek doklikal uživatel ručně ve Studiu.**
Stav zveřejnění je v `Témata.fods`.

| | |
|---|---|
| ID videa | `NuLh-NGHd9g` |
| master | ✅ `render/final-en-120.mp4` (8:39, 1920×1080, 66 MB, render 2026-10-21 na .207 za 436 s, `ffmpeg -v error` čistý) |
| náhled | ✅ koncept C, `render/thumbnail.jpg` (`thumbnail/PUVOD.md`) |
| nastavení, popis, tagy | podklady níž |
| lokalizace | `youtube-preklady.md`, 13 jazyků |
| titulky | `subtitles/*.srt`, 14 jazyků + `en-US`, až po Codexu |
| americká stopa | `render/audio-en-US.m4a`, ručně ve Studiu |
| závěrečná obrazovka | ručně ve Studiu |
| karty | žádné |
| playlist | `bezne` (*Ordinary Things, Awkward Questions*), na konec |

**Co musí uživatel naklikat sám:** závěrečnou obrazovku, americkou
audiostopu (`render/audio-en-US.m4a`) a osvědčení o zproštění, pokud ho
nevyřídil průvodce nahráním.

Stopáž 8:39 (`work/timing.json` total 518,7 s).

> Kdyby se znovu pouštěl `tts.py`, přepočítej kapitoly tady
> i v `youtube-preklady.md` a přegeneruj `en-US` přes `us_stopa.py`.

Pořadí podle CENY (`docs/zverejneni.md`):

```bash
V=videos/120-what-if-everyone-on-earth-owned-a-car
python tools/nahraj.py $V --k-videu=<ID> --bez-titulku   # 100
python tools/analytics.py --videa                        #   1  ← nutné
python tools/lokalizace.py $V                            #  50
python tools/titulky.py $V --smaz-asr                    # 150  ← před titulky
python tools/titulky.py $V                               # 400×15
python tools/playlisty.py                                #  50
# úklid, až je MP4 na YouTube:
rm $V/render/draft*.mp4
ssh vrana@192.168.0.207 'rm -rf /home/vrana/temp/render-120-what-if-everyone-on-earth-owned-a-car'
```

---

## 1. Titul

```
What If Everyone on Earth Owned a Car?
```

> Wh-otázka, 38 znaků, shodná s `project.json`. Odpověď titul
> neprozrazuje.

---

## 2. Popis

```
Imagine a world where every person on Earth owns a car. Not every family, every person. Eight billion people, eight billion cars. It sounds like the ultimate freedom, and it isn't as absurd as it sounds: in the United States there are already roughly eight vehicles for every ten people.

So what would happen if every country reached the American level? This video works it out step by step: where eight billion cars would park, how many people one lane of a city street can actually move, what happened after Houston widened the Katy Freeway to more than twenty lanes, how many cars the world's factories would have to build every year, and how much petrol, or electricity, it would take to keep them all moving.

Sources: FHWA, Highway Statistics 2024 (MV-1, DL-1C, VM-1); OICA, world vehicles in use (2020) and world motor vehicle production (2024); UN World Population Prospects 2024; World Bank, land area; Litman, Victoria Transport Policy Institute, Transportation Cost and Benefit Analysis; Shoup, The High Cost of Free Parking (2005); NACTO, Transit Street Design Guide (2016); FHWA, Katy Freeway project profile; City Observatory (Cortright), Houston TranStar travel times; WHO, Global Status Report on Road Safety 2023; Greene & Leard, Transportation Research Part A (2024); Odyssee-Mure, distance travelled by car; GFEI; IEA, Oil Market Report (2025); Ember, Global Electricity Review 2025; IEA, Global EV Outlook 2025. The fuel, electricity and battery figures assume 10,000 km per car per year, 7 litres of petrol or 20 kWh of electricity per 100 km.

Subtitles are written for this video, not auto-generated. An American English audio track is available as a second audio track.

CHAPTERS
00:00 Eight billion cars
00:28 Not as absurd as it sounds
01:06 The first problem: parking
02:32 Monday morning
03:05 So we build more roads
03:50 Not the only cost
04:20 Someone has to build them
05:03 Fuelling eight billion cars
05:31 What if they were all electric?
06:31 Who's going to drive them?
07:09 Where the experiment falls apart
07:45 Back to our world

IMAGE CREDITS
Run, Forest, Run! U.S. Route 163 in Monument Valley — m01229 from USA, CC BY-SA 2.0
Production line, car assembly line in General Motors Manufacturing Poland, Gliwice — Marek Ślusarczyk (Tupungato), CC BY 3.0
via Wikimedia Commons
Licences: creativecommons.org/licenses/by-sa/2.0, creativecommons.org/licenses/by/3.0
All other archive images are in the public domain.
```

> **Blok se kopíruje CELÝ** (`docs/zverejneni.md`). Archivní snímky
> jsou tři: S03 (CC BY-SA 2.0) a S32 (CC BY 3.0) mají povinnou atribuci,
> S24 (Katy Freeway, Carol M. Highsmith) je public domain.
>
> **Pointa se neprozrazuje.** Popis vyjmenuje kroky experimentu, ale
> ne závěr *svoboda pohybu ≠ vlastnictví stroje* (S51) ani *a strange
> answer for eight billion* (S57).
>
> Kapitoly ze scén S01, S05, S10, S19, S23, S28, S32, S37, S40, S46,
> S51, S54 (`work/timing.json`, zaokrouhleno dolů). Nejkratší 28 s
> (S05 → S10 38 s, S37 → S40 28 s), první na 00:00, všechny ≥ 10 s.
> Výzva k odběru S18b (2:24) leží v kapitole „The first problem: parking“.
>
> Čísla v popisu jsou tatáž jako ve scénáři a ve `factcheck.md`
> (S05, S08, S24, S37–S41).

---

## 3. Náhled

Tři koncepty v `thumbnail/ZADANI.md`, vybírá uživatel. Podle
`docs/thumbnail-styl.md`: jeden koncept, otázka bez odpovědi, čitelné
ve 150 px.

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
| komentáře | zapnuté (S58 končí otázkou do komentářů) |
| **byla použita AI** | **ne**. 52 scén je kreslených kódem, 3 archivní snímky jsou jen barevně upravené. SDXL jsou čtyři scény (S10 parkoviště, S19 ranní dálnice, S40 město s elektromobily, S52 venkovská silnice): malované ilustrace a generické scény, ne skutečné místo ani událost. Hudba je procedurální, hlas není klon. |

### Závěrečná obrazovka

Od **8:18** (posledních 20 s), tedy S57 a S58; páteř `jeden_a_vsichni()`
kreslí v závěru jen do dolní poloviny. `zaver_check` prošel, horní
polovina je volná. Jako dlaždici doporučuju **037 *How Oil Becomes
Petrol*** (navazuje na barely benzínu z S38–S39), druhou nechat
na „nejlepší pro diváka“.

---

## 6. Tagy

```
what if everyone owned a car, car ownership, cars, traffic, parking,
induced demand, katy freeway, road capacity, public transport,
electric cars, motorization, car dependency, urban planning,
road safety, oil demand, there's more to it
```

---

## 7. Playlist

`bezne` (*Ordinary Things, Awkward Questions*), na konec. Auto je
všední věc s nečekanou odpovědí za ní, což je přesně popis toho
playlistu. Alternativa je `energie` (blok S37–S42). Zapsat do
`playlisty.json` při nahrání; `playlisty.py` ho přeskočí, dokud video
není v `analytics/videa.json`.
