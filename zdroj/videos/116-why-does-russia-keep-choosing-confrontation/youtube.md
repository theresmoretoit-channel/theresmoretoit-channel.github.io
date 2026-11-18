# YouTube — 116 „Why Does Russia Keep Choosing Confrontation?“

Stav: **nahráno 2026-10-19** (MP4 ručně ve Studiu; nastavení, náhled,
lokalizace 13 jazyků, 15 titulkových stop a playlist přes API). Draft smazaný.
Uživatel ve Studiu naklikal americkou stopu, kartu na 100 (3:05), závěrečnou
obrazovku (dlaždice 050) a **naplánoval zveřejnění**. Po vydání 117 vyměnit
dlaždici a přidat kartu na 117 do S78 (10:00).
Stav zveřejnění je v `Témata.fods`.

| | |
|---|---|
| ID videa | `BC9fxi97ARQ` — https://www.youtube.com/watch?v=BC9fxi97ARQ |
| master | ✅ `render/final-en-116.mp4` (10:20, 58 MB, render 2026-10-18 na herním PC, `ffmpeg -v error` čistý) |
| náhled | ✅ `render/thumbnail.jpg` (1280×720, 0,35 MB), RUSSIA / WHY PRESS IT AGAIN?, původ v `thumbnail/PUVOD.md` |
| nastavení, popis, tagy | podklady níž |
| lokalizace | `youtube-preklady.md`, 13 jazyků |
| titulky | `subtitles/*.srt`, 14 jazyků + `en-US` |
| americká stopa | `render/audio-en-US.m4a`, ručně ve Studiu |
| závěrečná obrazovka | ručně ve Studiu |
| karta | 100 v 3:05 (viz níž) |
| playlist | `spolecnost`, na konec, za 115 |

**Co musí uživatel naklikat sám:** nahrát MP4 ve Studiu (průvodce vyřídí
prohlášení o AI a osvědčení o zproštění), závěrečnou obrazovku, kartu
na 100 a americkou audiostopu (`render/audio-en-US.m4a`).

Stopáž 10:20 (`work/timing.json` total 620,0 s).

> Kdyby se znovu pouštěl `tts.py`, přepočítej kapitoly tady
> i v `youtube-preklady.md` a přegeneruj `en-US` přes `us_stopa.py`.

> **Platnost:** S56 říká *„is now in its fifth year“*. To platí do
> **24. 2. 2027**; kdyby se video zveřejňovalo později, musí se S56 změnit
> (`factcheck.md`). Válka k 18. 10. 2026 trvá.

> **Až vyjde 117** (*What Would It Take for Russia to Change?*), dát na
> něj dlaždici závěrečné obrazovky a kartu do S78 (10:00). S78–S79 na
> něj odkazují (*„that is where we go next“*).

Pořadí podle CENY (`docs/zverejneni.md`):

```bash
V=videos/116-why-does-russia-keep-choosing-confrontation
python tools/nahraj.py $V --k-videu=<ID> --bez-titulku    # 100
python tools/analytics.py --videa                         #   1  ← nutné
python tools/lokalizace.py $V                             #  50
python tools/titulky.py $V --smaz-asr                     # 150  ← před titulky
python tools/titulky.py $V                                # 400×15
python tools/playlisty.py                                 #  50
# úklid, až je MP4 na YouTube:
rm $V/render/draft*.mp4
```

---

## 1. Titul

```
Why Does Russia Keep Choosing Confrontation?
```

> Wh-otázka, 44 znaků, shodná s `project.json`. Odpověď (vzorec slouží
> systému, který potřebuje nepřítele) titul neprozrazuje.

---

## 2. Popis

```
In 2022, one of the reasons Moscow gave for invading Ukraine was NATO creeping towards its borders. Just over a year later, Finland joined NATO, and the land border between Russia and NATO roughly doubled. Then Sweden joined too, a country that had not fought a war since 1814.

Russia is the largest country on Earth, rich in oil, gas, forests, farmland and minerals. Yet its economy is roughly the size of Italy's. So why does a country with so much keep choosing confrontation with neighbours it could trade with, even when Russia itself pays the price? The easy answer is one man. But the pattern is older than any one president. This video follows it from five centuries of expansion and an open plain with no natural defences, through the collapse of the Soviet Union and the chaotic 1990s, to the way decisions are made in Moscow today, and asks who the pattern really serves.

Sources: Address by the President of the Russian Federation, 24 February 2022 (kremlin.ru); NATO, Relations with Finland and Sweden; IMF, World Economic Outlook (2026); World Bank, World Development Indicators; MTS and EVA surveys on NATO membership; Yle / Taloustutkimus (May 2022); J. H. Herz, Idealist Internationalism and the Security Dilemma, World Politics (1950); G. F. Krivosheev, Soviet Casualties and Combat Losses (1993); Rosstat; V. Putin, Russia at the Turn of the Millennium (1999); V. Putin, Address to the Federal Assembly (2005); V. Putin, On the Historical Unity of Russians and Ukrainians (2021); Kremlin, Security Council meeting transcript (21 February 2022); RUSI, Preliminary Lessons in Conventional Warfighting from Russia's Invasion of Ukraine (2022); Federal Law No. 121-FZ (2012); EUAA, Russia: Foreign agents (2025); Ministry of Finance of the Russian Federation; Gaidar Institute, Monitoring (2026); European Commission, REPowerEU Roadmap (2025) and Quarterly Report on European Gas Markets (2025); The Bell (2023); MERICS, China–Russia Dashboard (2026).

Subtitles are written for this video, not auto-generated. An American English audio track is available as a second audio track.

Full transcript, sources and translations: https://theresmoretoit-channel.github.io/videos/why-does-russia-keep-choosing-confrontation/

CHAPTERS
00:00 Finland joins NATO
00:38 So much land, so small an economy
01:13 Is it just one man?
01:39 Five centuries of growth
02:37 The security dilemma
03:14 Finland changes its mind
03:33 The Soviet Union
03:55 Collapse and the 1990s
04:51 Order and a strong state
05:33 A lost sphere of influence
06:23 How decisions get made
07:25 The third mechanism
08:06 Who does the pattern serve?
08:43 The bill
09:34 Is it simply fate?
10:00 What would it take to change it?

IMAGE CREDITS
Full-size mock-up of the Vostok 1 capsule, Musée de l'air et de l'espace, Le Bourget — Alan Wilson, CC BY-SA 2.0
Kremlin wall in winter, Moscow — Vyacheslav Argenberg, CC BY 4.0
via Wikimedia Commons
Licences: creativecommons.org/licenses/by-sa/2.0 · creativecommons.org/licenses/by/4.0
```

> **Blok se kopíruje CELÝ** (`docs/zverejneni.md`). Archivní snímky
> jsou dva (S29, S40) a oba mají povinnou atribuci, jiné archivní snímky
> ve videu nejsou, proto chybí věta o public domain.
>
> **Pointa se neprozrazuje.** Popis končí otázkou, komu vzorec slouží;
> že slouží systému, který potřebuje nepřítele (S57–S62, S77), je
> výplata. Kapitoly *„The third mechanism“* a *„Who does the pattern
> serve?“* říkají téma, ne závěr. *„Is it simply fate?“* je otázka
> z S75, odpověď z S76 v kapitolách není.
>
> Kapitoly ze scén S01, S06, S10, S13, S20, S26, S29, S32, S40, S44, S49,
> S57, S63, S68, S75, S78 (`work/timing.json`, zaokrouhleno dolů).
> Nejkratší 19 s (S26 → S29), poslední 20 s (S78 → konec), všechny ≥ 10 s,
> první na 00:00. Výzva k odběru S12b (1:31) leží v kapitole *„Is it just
> one man?“*.
>
> Čísla v popisu (1814, „roughly doubled“, „roughly the size of Italy's“)
> jsou tatáž jako ve scénáři a ve `factcheck.md`. Zdroje podle
> `factcheck.md`; zprávy (AP, CNBC, Al Jazeera, NPR, Meduza) se necitují,
> citují se primární prameny a studie.

---

## 3. Náhled

`render/thumbnail.jpg` — ošoupaný rudý knoflík, RUSSIA / WHY PRESS IT
AGAIN? (koncept A ze `thumbnail/ZADANI.md`); původ, otisk a thumb_check
v `thumbnail/PUVOD.md`.

---

## 4. Titulky

`subtitles/*.srt`, 14 jazyků + `en-US`. Jazyk videa **`en-gb`** (hlas
`bf_emma`) se musí nastavit dřív, než se nahrají titulkové stopy.
Všechny překlady prošly Codexem, čeština i uživatelem.

---

## 5. Nastavení

| | |
|---|---|
| kategorie | **Science & Technology** (28) — posílá `nahraj.py` napevno |
| jazyk videa | `en-gb` |
| licence | standardní |
| pro děti | **ne** |
| komentáře | zapnuté |
| **byla použita AI** | **ne**. Většina scén je kreslená kódem, 2 archivní snímky jsou jen barevně upravené. SDXL je ve dvou scénách: S15 (pláň) a S38 (ulice) jsou malované ilustrace bez konkrétního místa nebo události. Hudba je procedurální, hlas není klon. |

### Závěrečná obrazovka

Od **10:00** (posledních 20 s), tedy S78–S79, které kreslí jen do dolní
poloviny. `zaver_check.py` (2026-10-18): obě scény OK, prvky patří
**nahoru** (horní rohy 0 % kresby), dolní rohy kryje ambrový titulek. Dokud 117 nevyjde, dlaždice **050 *How Does a Dictatorship Become a
Democracy?*** — S78 se ptá *„what would it take to change it?“*, což je
otázka 050; po vydání 117 ji vyměnit za 117.

### Karta

**100 *Why Would Preparing for War Keep the Peace?* v 3:05** (S25
*„Political scientists call it the security dilemma“*). 100 vykládá
přesně tenhle pojem včetně Herze 1950 (S16–S17). Původní návrh (115
v 3:14) neměl oporu: 115 je o důvěře spojenců v USA, video 116 o tom
nemluví.

---

## 6. Tagy

```
russia, putin, russia ukraine war, nato expansion, finland nato,
sweden nato, security dilemma, soviet union, collapse of the soviet union,
russia 1990s, foreign agents law, russia china, russian gas, europe gas,
geopolitics explainer, history explainer, there's more to it
```

---

## 7. Playlist

`spolecnost` (*How Society Actually Runs*), na konec, za 115.
Zapsáno v `playlisty.json`; `playlisty.py` ho přeskočí, dokud video
není v `analytics/videa.json`.
