# YouTube — 153 „Why Is Flying So Safe Now?“

Stav: **nahráno 2026-11-11** (https://youtu.be/0hNIAERbWIE, MP4 ručně uživatel). `nahraj.py --bez-titulku` (nastavení, popis, tagy, náhled C1), `lokalizace.py` (13 jazyků + en-GB), ASR přepis nebyl, titulky všech 15 stop (ověřeno `--zkouska`: všude „aktualizace“). Ve Studiu americká stopa, závěrečná obrazovka a naplánované zveřejnění hotové. **Zbývá:** po zveřejnění `playlisty.json` → `bezne` a `playlisty.py`.

| | |
|---|---|
| ID videa | `0hNIAERbWIE` |
| master | `render/final-en-153.mp4` (herní PC, 3× supersampling, 701,96 s, 1920×1080, 80 MB, dekódováno bez chyby) |
| náhled | ✅ C1 letadlo v ementálu, `WHY SO FEW CRASHES?`, `render/thumbnail.jpg` (`thumbnail/PUVOD.md`) |
| nastavení, popis, tagy | podklady níž |
| lokalizace | `youtube-preklady.md`, 13 jazyků |
| titulky | `subtitles/<kód>.srt`, 14 jazyků + `en-US`, Codex v0.3 na 13 jazyků zapracován |
| americká stopa | `render/audio-en-US.m4a`, ručně ve Studiu |
| závěrečná obrazovka | S81–S82, **horní polovina** (viz níž) |
| karty | žádné |
| playlist | `bezne` |

**Co musí uživatel naklikat sám:** závěrečnou obrazovku, americkou audiostopu
(`render/audio-en-US.m4a`), titulky, které nejdou přes API, a osvědčení o zproštění, pokud ho nevyřídil průvodce nahráním.

Stopáž 11:41 (`work/timing.json` total 701,903 s).

> Kdyby se znovu pouštěl `tts.py`, přepočítej kapitoly tady i v `youtube-preklady.md`
> a přegeneruj `en-US` přes `us_stopa.py`.

Pořadí podle CENY (`docs/zverejneni.md`):

```bash
V=videos/153-why-is-flying-so-safe-now
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
Why Is Flying So Safe Now?
```

> Wh-otázka, 26 znaků, shodná s `project.json` a s S78. Odpověď (S58: většina lekcí nestojí životy;
> S62–S66: hlášení vlastních chyb bez trestu, vyšetřování bez hledání viníka) titul neprozrazuje.

---

## 2. Popis

```
In the early 1970s, every time you boarded a passenger plane, your chance of dying on that flight was about one in three hundred and fifty thousand. Today, it's about one in fourteen million. In a single lifetime, flying has become roughly forty times safer, and not because planes stopped breaking. Engines still fail. Sensors still freeze. Pilots still make mistakes. Almost every rule on a modern flight exists because somebody, somewhere, died. But people die on roads too, and roads haven't become anything like forty times safer. So how does aviation manage to learn so well?

This video goes through the Boeing bomber that crashed because of a forgotten lock, the de Havilland Comets that broke apart in mid-air and a fuselage tested in a tank of water, the young Australian scientist behind the black box, the radio call that was lost at Tenerife and the single word that changed after it, the DC-10 that lost all three hydraulic systems over Iowa, Air France 447 and what happens when the autopilot switches off, a warning that never reached TWA, Swiss cheese, and the Boeing 737 MAX.

Sources: Barnett & Reig Torra, Airline safety: Still getting better?, Journal of Air Transport Management (2024); Gawande, The Checklist Manifesto (2009); FAA, Lessons Learned from Civil Aviation Accidents (de Havilland Comet; KLM and Pan Am at Tenerife); NTSB, Aircraft Accident Report AAR-90/06 (United 232); Haynes, The Crash of United Flight 232, lecture at NASA Ames (1991); BEA, Final Report on Air France 447 (2012); NASA, Aviation Safety Reporting System Program Briefing; ICAO, Annex 13; Reason, Human Error (1990); KNKT, Final Report on Lion Air 610 (2019); US House Committee on Transportation and Infrastructure, Final Committee Report on the Boeing 737 MAX (2020).

Subtitles are written for this video, not auto-generated. An American English audio track is available as a second audio track.

Full transcript, sources and translations: https://theresmoretoit-channel.github.io/videos/why-is-flying-so-safe-now/

CHAPTERS
00:00 Forty times safer
00:55 "Too much airplane"
02:02 Why did the Comets break apart?
03:00 The black box
03:39 Tenerife
04:33 A single word
04:47 Speaking up in the cockpit
05:22 United 232: no controls left
06:28 Air France 447
07:34 Lessons that cost lives
07:45 A warning that never arrived
08:12 A system run by NASA
09:01 Swiss cheese
09:22 The Boeing 737 MAX
10:39 Is flying getting more dangerous?
10:54 So why?

IMAGE CREDITS
Boeing B-17G Flying Fortress, Duxford Flying Evening 2024 — Julian Herzog, CC BY 4.0
de Havilland Comet 1, BOAC, Heathrow 1953 — RuthAS, derivative work Altair78, CC BY 3.0
Icelandair Boeing 737-8 MAX TF-ICY, Berlin Brandenburg Airport — MarcelX42, CC BY-SA 4.0
via Wikimedia Commons
Licences: creativecommons.org/licenses/by/4.0, creativecommons.org/licenses/by/3.0, creativecommons.org/licenses/by-sa/4.0
All other archive images are in the public domain.
```

> **Blok se kopíruje CELÝ** (`docs/zverejneni.md`). Kredity ze `sources.json`: tři snímky s CC BY / BY-SA
> (S16, S19, S70) jmenovitě, zbylé čtyři (S10, S11 Model 299, S25 Warren, S28 zapisovač NTSB) jsou public domain.
> SDXL scény S30, S41, S51 jsou generované, kreslené kódem je zbytek.
>
> **Pointa se neprozrazuje:** popis ani kapitoly neříkají, že většina lekcí nestojí životy (S58), ani že hlášení
> nesmí sloužit k trestu (S63, S65–S66). Kapitola *Lessons that cost lives* (S57) je obrat, odpověď až za ní.
> *A system run by NASA* (S62) jmenuje instituci, ne mechanismus.
>
> Kapitoly ze scén S01, S10, S19, S25, S30, S36, S38, S42, S50, S57, S59, S62, S67, S69, S77, S78
> (`work/timing.json`, zaokrouhleno dolů). První na 00:00, všechny ≥ 10 s (nejkratší S57 → S59, 11 s, a S36 → S38,
> 14 s; poslední S78 → konec 47 s). S50 (*computers could fly a plane*) samostatně jen 10 s, proto je začátkem AF447. *The Boeing 737 MAX* začíná S69 (*that system is run by people too*), aby
> S67–S68 zůstal celý Swiss cheese. Otázka do komentářů (S82) vlastní kapitolu nemá.
>
> **Zdroje:** z `factcheck.md` ty, které jsou primární nebo citovatelné. Tisk a encyklopedie (MIT News, Air & Space
> Forces, Wikipedia, IEEE Spectrum, Museums Victoria) v popisu nejsou.

---

## 3. Náhled

C1 z `thumbnail/ZADANI.md` (ChatGPT): dopravní letadlo prolétá řadou plátů ementálu, `WHY SO FEW CRASHES?`.
`render/thumbnail.jpg`, původ v `thumbnail/PUVOD.md`.

---

## 4. Titulky

`subtitles/<kód>.srt` pro 14 jazyků a `en-US` (`codex 0.3 <kód>.txt`).
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
| **byla použita AI** | **ne**. 73 z 82 scén je kreslených kódem. Tři SDXL scény (S30 mlha, S41 kokpit, S51 nebe nad mraky) jsou díky kotvě stylu malované ilustrace, ne fotorealismus, a nezobrazují konkrétní skutečnou událost jako dokument. Šest archivních snímků z Commons je upravených jen barevně. Hudba je procedurální, hlas není klon skutečné osoby. |

> **Letecké nehody a vhodnost pro inzerenty:** video je výkladové, neukazuje zraněné, oběti ani záběry
> z nehod (trosky jen jako kresba). V dotazníku vhodnosti **„Tragic events“** = vzdělávací kontext, bez
> naturalistických záběrů.

### Závěrečná obrazovka

Od **11:41 − 20 s = 11:21**, tedy S81–S82. `zaver_check` hlásí S81 i S82 OK, **horní polovina je volná**.
**Dlaždici i odběr dej do HORNÍ poloviny.** Jako dlaždici navrhuju **095 *How Would Passengers Land an Airliner?***
(tentýž playlist, letectví), druhou nechat na „nejlepší pro diváka“.
Alternativa: 079 *Why Is This 90-Year-Old Airplane Still Flying?* (DC-3, playlist `legacy`).

---

## 6. Tagy

```
why is flying so safe, aviation safety, plane crash, air crash investigation, black box, flight recorder,
checklist, boeing model 299, b-17, de havilland comet, metal fatigue, tenerife disaster, crew resource management,
united 232, sioux city, air france 447, aviation safety reporting system, swiss cheese model, boeing 737 max,
is flying getting more dangerous, there's more to it
```

---

## 7. Playlist

**`bezne`**, za 095 *How Would Passengers Land an Airliner?* (letectví, každodenní otázka).
Dopsat slug do `playlisty.json` až po zveřejnění, pak `analytics.py --videa` a `playlisty.py`.
