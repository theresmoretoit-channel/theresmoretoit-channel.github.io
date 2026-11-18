# YouTube — 132 „We Built Flying Cars. So Why Don't We Use Them?“

Stav: **nahráno 2026-11-02** (MP4 ručně, metadata, náhled, lokalizace a všech 15 titulkových stop přes API; zbytek 2026-11-03). Stav zveřejnění je v `Témata.fods`.

| | |
|---|---|
| ID videa | `uuRcs4HFJHM` — https://www.youtube.com/watch?v=uuRcs4HFJHM |
| master | `render/final-en-132.mp4` (render na .207, 2026-11-02) |
| náhled | ✅ `render/thumbnail.jpg` — koncept C2 (`thumbnail/PUVOD.md`) |
| nastavení, popis, tagy | podklady níž |
| lokalizace | `youtube-preklady.md`, 13 jazyků |
| titulky | ✅ všech 14 jazyků + `en-US` na YouTube (pl, id, tr, uk, vi, fi dobrány 2026-11-03) |
| americká stopa | `render/audio-en-US.m4a`, ručně ve Studiu |
| závěrečná obrazovka | S89–S92, **horní polovina** (viz níž) |
| karty | žádné |
| playlist | `bezne`, hned za 120 (*What If Everyone on Earth Owned a Car?*) |

**Co musí uživatel naklikat sám:** závěrečnou obrazovku, americkou
audiostopu (`render/audio-en-US.m4a`) a osvědčení o zproštění, pokud ho
nevyřídil průvodce nahráním.

Stopáž 8:31 (`work/timing.json` total 511,4 s).

> **Před nahráním přeověřit S06, S50, S79, S83** (konec `factcheck.md`):
> Joby Q3 4. 11., Archer a EHang v listopadu, Alef do konce 2026. Když
> se něco změní, mění se scénář, hlas i titulky — ne jen popis.
>
> Kdyby se znovu pouštěl `tts.py`, přepočítej kapitoly tady
> i v `youtube-preklady.md` a přegeneruj `en-US` přes `us_stopa.py`.

Pořadí podle CENY (`docs/zverejneni.md`):

```bash
V=videos/132-we-built-flying-cars-so-why-dont-we-use-them
python tools/nahraj.py $V --k-videu=<ID> --bez-titulku   # 100
python tools/analytics.py --videa                        #   1  ← nutné
python tools/lokalizace.py $V                            #  50
python tools/titulky.py $V --smaz-asr                    # 150  ← před titulky
python tools/titulky.py $V                               # 400×15
python tools/playlisty.py                                #  50
# úklid, až je MP4 na YouTube:
rm $V/render/draft*.mp4
ssh vrana@192.168.0.207 'rm -rf /home/vrana/temp/render-132-we-built-flying-cars-so-why-dont-we-use-them'
```

---

## 1. Titul

```
We Built Flying Cars. So Why Don't We Use Them?
```

> Tvrzení + wh-otázka, 47 znaků, shodné s `project.json`. Tvrzení je
> paradox (S01–S05), ne pointa; odpověď (měřítko, S73–S75) titul
> neprozrazuje.

---

## 2. Popis

```
This car has a certificate that says it's allowed to fly. In 1956, the American government certified another one, and only six were ever built. We were promised flying cars, and we built them, again and again. So why doesn't anyone use them?

This video starts with just one flying car: why a car and a plane want almost opposite things, the 1947 flying car whose wing you were meant to rent at the airport, how much more power it takes to hover than to drive, why a helicopter gets away with it, what batteries can and can't do, and who would actually fly the thing. Then it puts a few thousand of them over one city, and keeps going.

Sources: HistoryNet / Aviation History (the Aerocar, the ConvAirCar and William Piper's Private Flying: Today and Tomorrow, 1949); San Diego Air & Space Museum archives; General Aviation News on the AirCar certificate (2022); PAL-V Liberty specifications; US EPA test car coefficients; Kasliwal et al., Nature Communications (2019); EASA type certificate data for the Robinson R44; NTSB general aviation accident data (2024); NHTSA and AAA Foundation; FAA airmen statistics and Air Traffic by the Numbers (FY2024); FHWA Highway Statistics; UK Department for Transport, VEH0105; Aerospace America and AIN on the NASA and Wisk simulation (2026); EHang and Joby Aviation filings and announcements; Abraphe on São Paulo's helicopter fleet; AIN on Airbus CityAirbus NextGen (2025).

Subtitles are written for this video, not auto-generated. An American English audio track is available as a second audio track.

Full transcript, sources and translations: https://theresmoretoit-channel.github.io/videos/we-built-flying-cars-so-why-dont-we-use-them/

CHAPTERS
00:00 A car that's allowed to fly
00:44 Start with one
01:36 Rent the wing at the airport
02:13 Straight up, from a street or a roof
02:28 Where physics sends the bill
03:23 Batteries
03:48 Who's flying it?
04:52 A few thousand over one city
05:26 Noise, and somewhere to land
05:58 Make it millions
06:43 The real answer
06:55 A smaller dream
07:42 Where the flying car belongs
08:21 A question for you

IMAGE CREDITS
Aerocar 2024 — Cullen328, CC BY-SA 4.0
EHang 216-S au Salon du Bourget 2025 — Artvill, CC BY 4.0
Helicoptero sobre a prefeitura de São Paulo — Henrique Boney, CC BY-SA 3.0
via Wikimedia Commons
Licences: creativecommons.org/licenses/by-sa/4.0, creativecommons.org/licenses/by/4.0, creativecommons.org/licenses/by-sa/3.0
All other archive images are in the public domain or have no known copyright restrictions.
```

> **Blok se kopíruje CELÝ** (`docs/zverejneni.md`). Povinná atribuce jsou
> tři snímky pod CC BY* (S03, S49, S63); S16, S18, S60 jsou public domain,
> S20 je Flickr Commons „no known copyright restrictions“ (`sources.json`).
>
> **Pointa se neprozrazuje:** popis nejmenuje závěr S73–S75 (*good idea
> for one person, stops working when everyone has one*) ani aerotaxi jako
> odpověď (kapitola 06:55 je proto *A smaller dream* podle S80, ne „Air taxis instead“). „And keeps going“ jen naznačí stupňování.
>
> **Zdroje** jsou hlavní zdroje z `factcheck-zaklad.md`. Konkrétní
> stav aerotaxi (S79–S83) zastará — popis ho proto nepojmenovává.
>
> Kapitoly ze scén S01, S09, S18, S24, S26, S35, S39, S53, S59, S65, S73,
> S76, S84, S91 (`work/timing.json`, zaokrouhleno dolů). Nejkratší
> 10,1 s (S91 → konec), druhá nejkratší 12,4 s (S73 → S76), první na
> 00:00, všechny ≥ 10 s. Výzvy k odběru (za S23 a S75) leží uvnitř kapitol.

---

## 3. Náhled

`render/thumbnail.jpg` (1280×720, 0,36 MB): červené auto z 50. let
s křídly, *PROMISED* / *SO WHERE IS IT?* — koncept C2 z
`thumbnail/ZADANI.md`, původ a otisky v `thumbnail/PUVOD.md`.

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
| komentáře | zapnuté (S91–S92 je otázka do komentářů) |
| **byla použita AI** | **ne**. Většina scén je kreslená kódem (diagramy, animace). Tři SDXL scény (S39, S53, S86) jsou podle kotvy stylu **malované ilustrace** (*painterly editorial illustration*), ne fotorealismus, a nezobrazují konkrétní skutečné místo ani událost. Sedm archivních snímků je jen barevně upravených. Hudba je procedurální, hlas není klon. |

### Závěrečná obrazovka

Od **8:11** (posledních 20 s), tedy S89–S92. `zaver_check` u všech
hlásí volnou **horní** část rámu (~40 %). **Dlaždici i odběr dej do
HORNÍ poloviny.** Jako dlaždici doporučuju **120 *What If Everyone on
Earth Owned a Car?*** (tentýž argument o měřítku na zemi), druhou nechat
na „nejlepší pro diváka“.

---

## 6. Tagy

```
flying car, flying cars, klein vision aircar, pal-v liberty, aerocar,
convaircar, evtol, air taxi, joby aviation, ehang, lilium, volocopter,
urban air mobility, helicopter, future of transport, aviation history,
why don't we have flying cars, there's more to it
```

---

## 7. Playlist

`bezne` (*Ordinary Things, Awkward Questions*), hned za 120 (*What If
Everyone on Earth Owned a Car?*), se kterým sdílí argument o měřítku.
Zapsat do `playlisty.json` při nahrání; `playlisty.py` ho přeskočí,
dokud video není v `analytics/videa.json`.
