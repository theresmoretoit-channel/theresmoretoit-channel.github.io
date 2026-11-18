# YouTube — 118 „Who Really Shot Down MH17?“

Stav: **nahráno 2026-10-19 (`MlYnZ0TfDO0`), zveřejnění naplánované**. Agent nahrál nastavení, popis, tagy, lokalizace (13 jazyků, po Codexu), titulky `en` (en-GB), `cs`, `sv`, `es`, smazal automatický přepis a zařadil video do playlistu; pak došla kvóta. Zbylé titulky, náhled, americkou stopu a závěrečnou obrazovku nahrál uživatel ručně ve Studiu. Stav zveřejnění je v `Témata.fods`.

| | |
|---|---|
| ID videa | `MlYnZ0TfDO0` (MP4 nahrál uživatel 2026-10-19) |
| master | ✅ `render/final-en-118.mp4` (10:55, 1920×1080, 64 MB, render 2026-10-19 na .207 za 556 s, `ffmpeg -v error` čistý) |
| náhled | ✅ `render/thumbnail.jpg` (1280×720, 0,30 MB), MH17 / HOW DO WE KNOW?, koncept A, původ v `thumbnail/PUVOD.md`; nahrál uživatel ručně ve Studiu |
| nastavení, popis, tagy | podklady níž |
| lokalizace | `youtube-preklady.md`, 13 jazyků |
| titulky | `subtitles/*.srt`, 14 jazyků + `en-US`, všechny prošly Codexem |
| americká stopa | `render/audio-en-US.m4a`, ručně ve Studiu |
| závěrečná obrazovka | ručně ve Studiu |
| karty | žádné (video na žádné jiné nenavazuje) |
| playlist | `spolecnost`, na konec, za 117 |

**Co musí uživatel naklikat sám:** závěrečnou obrazovku, americkou
audiostopu (`render/audio-en-US.m4a`) a osvědčení o zproštění, pokud ho
nevyřídil průvodce nahráním.

Stopáž 10:55 (`work/timing.json` total 655,3 s).

> Kdyby se znovu pouštěl `tts.py`, přepočítej kapitoly tady
> i v `youtube-preklady.md` a přegeneruj `en-US` přes `us_stopa.py`.

Pořadí podle CENY (`docs/zverejneni.md`):

```bash
V=videos/118-who-really-shot-down-mh17
python tools/nahraj.py $V --k-videu=MlYnZ0TfDO0 --bez-titulku   # 100
python tools/analytics.py --videa                               #   1  ← nutné
python tools/lokalizace.py $V                                   #  50
python tools/titulky.py $V --smaz-asr                           # 150  ← před titulky
python tools/titulky.py $V                                      # 400×15
python tools/playlisty.py                                       #  50
# úklid, až je MP4 na YouTube:
rm $V/render/draft*.mp4
ssh vrana@192.168.0.207 'rm -rf /home/vrana/temp/render-118-who-really-shot-down-mh17'
```

---

## 1. Titul

```
Who Really Shot Down MH17?
```

> Wh-otázka, 26 znaků, shodná s `project.json`. Odpověď titul neprozrazuje
> a nesvádí k ano/ne.

---

## 2. Popis

```
On 17 July 2014, Malaysia Airlines Flight MH17 broke apart in the sky over eastern Ukraine. All 298 people on board died. Twelve years later, a clip from Russian radio went round the internet. In it, a retired Russian colonel appeared to say: "A Russian officer shot it down, yes."

Was that the confession investigators had been waiting for? To judge it, you first need to know what the evidence says without it. This video follows that evidence: the fragments found in the wreckage, a post that disappeared from social media, intercepted phone calls, photographs of a missile launcher on the move, Russia's changing explanations, and the verdict of a Dutch court. Then it checks the colonel's words the same way.

Sources: Dutch Safety Board, Crash of Malaysia Airlines flight MH17, final report (13 October 2015); OSCE Special Monitoring Mission to Ukraine, reports of 18–21 July 2014; archived VKontakte page "Svodki ot Strelkova" (Wayback Machine, 17 July 2014); Joint Investigation Team MH17, findings of 28 September 2016, 24 May 2018 and 8 February 2023; District Court of The Hague, judgments of 17 November 2022 (ECLI:NL:RBDHA:2022:14036, 14037, 14039 and 14040); ICAO, report on Korean Air Lines Flight 007 (1993); ICAO Council, decision of 12 May 2025; European Court of Human Rights, Grand Chamber, Ukraine and the Netherlands v. Russia (9 July 2025).

Viktor Baranets spoke on Radio Komsomolskaya Pravda on 21 September 2026. That recording has since been taken down and we have not heard the audio ourselves; his words are quoted from the transcript published by Agentstvo (Telegram, @agentstvonews, 11 October 2026).

Subtitles are written for this video, not auto-generated. An American English audio track is available as a second audio track.

Full transcript, sources and translations: https://theresmoretoit-channel.github.io/videos/who-really-shot-down-mh17/

CHAPTERS
00:00 Flight MH17
00:18 A clip from Russian radio
00:54 What destroyed the plane?
01:55 On board
02:31 The crime scene
03:19 Evidence posted online
04:35 The launcher
05:45 Russia's explanations
06:50 Back to the colonel
08:38 What has been proven?
09:50 One more failure
10:20 So who shot it down?

IMAGE CREDITS
Buk-M1, 11th Anti-Aircraft Missile Brigade — Air Command "West" of the Air Forces of the Armed Forces of Ukraine, CC BY 4.0
Malaysia Airlines Boeing 777-200 9M-MRD — Masakatsu Ukon, CC BY-SA 2.0
National Monument MH17, Vijfhuizen — Hay Kranen, CC BY 4.0
via Wikimedia Commons
Licences: creativecommons.org/licenses/by/4.0, creativecommons.org/licenses/by-sa/2.0
```

> **Blok se kopíruje CELÝ** (`docs/zverejneni.md`). Archivní snímky jsou
> tři (S11, S14, S18) a všechny mají povinnou atribuci (`sources.json`).
> Public domain snímek tu není, takže věta „All other archive images…“
> chybí záměrně.
>
> **Zdroj Barancova citátu je v popisu výslovně** (rozhodnuto při fact
> checku): záznam Radia KP na Rutube je skrytý, přepis je jen jeden,
> od Agentstva, a zvuk nikdo z nás neslyšel.
>
> **Pointa se neprozrazuje.** Popis končí tím, že se výrok ověří; že si
> Baranec spletl MH17 s KAL 007 (S57–S61), je výplata. Kapitola
> *„Back to the colonel“* a *„So who shot it down?“* jsou otázky, ne
> odpovědi. Zdroj ICAO ke KAL 007 v seznamu je, ale bez vysvětlení.
>
> Kapitoly ze scén S01, S03, S07, S14, S19, S26, S36, S44, S52, S66, S74,
> S78 (`work/timing.json`, zaokrouhleno dolů). Nejkratší 30 s (S74 → S78),
> první na 00:00, všechny ≥ 10 s. Výzva k odběru S13b (1:47) leží
> v kapitole „What destroyed the plane?“.
>
> 9M-MRD je skutečná registrace letadla MH17 (S14). Čísla a data
> v popisu jsou tatáž jako ve scénáři a ve `factcheck.md`. Zprávy
> (Bellingcat, Meduza) se necitují, citují se primární prameny; Bellingcat
> je ve `factcheck.md` jako ten, kdo první našel shodu značek (S41).

---

## 3. Náhled

`render/thumbnail.jpg`: ocelový úlomek ve tvaru motýlka, MH17 / HOW DO
WE KNOW?. Koncept A ze `ZADANI.md`, obrázek z ChatGPT. Původ, otisk
a thumb_check jsou v `thumbnail/PUVOD.md`.

---

## 4. Titulky

`subtitles/*.srt`, 14 jazyků + `en-US`. Jazyk videa **`en-gb`** (hlas
`bf_emma`) se musí nastavit dřív, než se nahrají titulkové stopy.
Všechny překlady prošly Codexem (nálezy v `notes.md`).

---

## 5. Nastavení

| | |
|---|---|
| kategorie | **Science & Technology** (28) — posílá `nahraj.py` napevno |
| jazyk videa | `en-gb` |
| licence | standardní |
| pro děti | **ne** |
| komentáře | zapnuté |
| **byla použita AI** | **ne**. 77 scén je kreslených kódem, 3 archivní snímky jsou jen barevně upravené. SDXL je ve třech scénách (S15 moře mraků shora, S19 slunečnicové pole pod zataženou oblohou, S36 prázdná silnice mezi slunečnicemi): malované ilustrace a **generická krajina**, ne místo dopadu ani skutečná událost. Hudba je procedurální, hlas není klon. Tváře lidí se nekreslí. |

### Závěrečná obrazovka

Od **10:35** (posledních 20 s), tedy S80–S82. `zaver_check` prošel, oba
horní rohy jsou volné (dole leží titulky). Jako dlaždici doporučuju
**117 *What Would It Take for Russia to Change?*** (nejbližší téma),
druhou nechat na „nejlepší pro diváka“.

---

## 6. Tagy

```
mh17, malaysia airlines mh17, mh17 investigation, buk missile,
dutch safety board, joint investigation team, igor girkin, strelkov,
eastern ukraine 2014, donbas, viktor baranets, kal 007,
korean air lines flight 007, open source investigation, fact checking,
disinformation, russia, there's more to it
```

---

## 7. Playlist

`spolecnost` (*How Society Actually Runs*), na konec, za 117. Zapsáno
v `playlisty.json`. `playlisty.py` ho přeskočí, dokud video není
v `analytics/videa.json`.
