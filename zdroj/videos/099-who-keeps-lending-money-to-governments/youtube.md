# YouTube — 099 „Who Keeps Lending Money to Governments?"

Stav: **nahráno a naplánované ke zveřejnění** (`ellqMJuppKc`, 2026-10-10). Hotovo. Titulky 14 jazyků
+ `en-US` prošly Codexem (2026-10-10), čeština schválena uživatelem.

| | |
|---|---|
| ID videa | `ellqMJuppKc` (https://www.youtube.com/watch?v=ellqMJuppKc), MP4 nahrál uživatel 2026-10-10 |
| master | ✅ `render/final-en-099.mp4` (2026-10-10, render na .207, 1920×1080, 582,3 s, `ffmpeg -f null` bez chyb) |
| náhled | ✅ C1 DEBT / WHO'S LENDING? (`render/thumbnail.jpg`) |
| nastavení, popis, tagy | ✅ 2026-10-10 (`nahraj.py --k-videu --bez-titulku`) |
| lokalizace | ✅ 13 jazyků + en (`lokalizace.py`) |
| automatický přepis | ✅ při nahrávání titulků nebyl, objevil se později, uživatel smazal ve Studiu |
| titulky | ✅ 15 stop (`titulky.py`, 6 000 jednotek) |
| tagy | ✅ 18 — `lokalizace.py` je smazal (snippet zpátky), obnoveny a nástroj opraven (`d18f698d`) |
| playlist | ✅ `spolecnost` (*How Society Actually Runs*, `playlisty.py`) |
| závěrečná obrazovka, americká stopa | ✅ uživatel ve Studiu, video naplánované |

**Co musí uživatel naklikat sám:** nahrát MP4 ve Studiu (průvodce vyřídí
prohlášení o AI a osvědčení o zproštění), závěrečnou obrazovku a americkou
audiostopu (`render/audio-en-US.m4a`).

Soubor k nahrání: `render/final-en-099.mp4` (stopáž 9:42, `work/timing.json`
total 582,2 s).

> Kdyby se znovu pouštěl `tts.py`, přepočítej kapitoly tady
> i v `youtube-preklady.md` a přegeneruj `en-US` přes `us_stopa.py`.

Pořadí podle CENY (`docs/zverejneni.md`):

```bash
V=videos/099-who-keeps-lending-money-to-governments
python tools/nahraj.py $V --k-videu=<ID> --bez-titulku    # 100
python tools/analytics.py --videa                         #   1  ← nutné
python tools/lokalizace.py $V                             #  50
python tools/titulky.py $V --smaz-asr                     # 150  ← před titulky
python tools/titulky.py $V                                # 400×15
python tools/playlisty.py                                 #  50
```

---

## 1. Titul

```
Who Keeps Lending Money to Governments?
```

> Wh-otázka, 39 znaků, totožná s nadpisem `script.md`. Neprozrazuje
> odpověď (z velké části my sami přes penzijní fondy, a refinancování).

---

## 2. Popis

```
Greece owes about 146% of its GDP, more than any other country in the European Union. And yet for most of the past year, it has borrowed more cheaply than France.

Governments spend more than they collect, year after year, and the old loans never seem to go away. So who keeps lending them the money? Who actually buys government bonds, how can Japan owe more than twice its entire economy, and does any of it ever get paid back?

Debt and deficit figures: Eurostat (April 2026 notification) and the IMF World Economic Outlook (April 2026). Ten-year government bond yields on 2 October 2026: Greece 4.52%, France 4.91%.

Subtitles are written for this video, not auto-generated. An American English audio track is available as a second audio track.

CHAPTERS
00:00 Borrowing every year
00:34 Where it stopped working
01:30 Deficit and debt
02:07 Two real countries
03:38 Across Europe
04:07 Who buys government bonds?
05:13 Japan
06:11 When does it get paid back?
07:11 The catch
08:13 Why not pay it all off?
09:01 So who keeps lending?

IMAGE CREDITS
2011 Greece Uprising — Kotsolis at English Wikipedia, CC BY-SA 3.0
United States Treasury Building — Rchuon24, CC BY-SA 3.0
Bank of Japan Head Office, Tokyo - Aug 29, 2011 — yt_siden, CC BY-SA 2.0
via Wikimedia Commons
All other archive images are in the public domain.
Licences: creativecommons.org/licenses/by-sa/3.0, creativecommons.org/licenses/by-sa/2.0
```

> **Blok se kopíruje CELÝ** (`docs/zverejneni.md`). Povinná atribuce:
> S07 (Kotsolis), S30 (Rchuon24), S47 (yt_siden), všechny CC BY-SA.
> S39 (dluhopis z roku 1825) je public domain.
>
> Kapitoly jsou ze scén S01, S07, S16, S22, S33, S37, S47, S56, S66, S76,
> S82 (`work/timing.json`, zaokrouhleno dolů). Nejkratší kapitola je 29 s
> (S33 → S37), poslední 41 s; všechny ≥ 10 s, první na 00:00. Výzva
> k odběru S15b leží v kapitole „Where it stopped working".
>
> **Datum výnosů a ročník dat jsou v popisu podle rozhodnutí uživatele**
> (2026-10-10): na IMF WEO 13. 10. ani na říjnovou notifikaci Eurostatu
> se nečeká. 146 % je Eurostat 2025 (146,1, nejvyšší v EU; Itálie 137);
> výnosy 4,523 / 4,910 % z dnews.gr 3. 10. 2026 (`factcheck.md`, S12).
> „Twice its entire economy" = S48 (IMF 206,5 %).

---

## 3. Náhled

✅ **DEBT / WHO'S LENDING?** — C1 kreslený kódem (`thumbnail/c1-stoh.svg` →
`render/thumbnail.jpg`), vybral uživatel 2026-10-10, koncepty v `thumbnail/KONCEPTY.md`.

---

## 4. Titulky

`subtitles/*.srt`, 14 jazyků + `en-US`. Jazyk videa **`en-gb`** (hlas
`bf_emma`) se musí nastavit dřív, než se nahrají titulkové stopy. Titulky
a lokalizace se nahrávají až po zapracování nálezů Codexu — **to je hotové**
(2026-10-10, všech 13 jazyků).

---

## 5. Nastavení

| | |
|---|---|
| kategorie | **Science & Technology** (28) — posílá `nahraj.py` napevno |
| jazyk videa | `en-gb` |
| licence | standardní |
| pro děti | **ne** |
| komentáře | zapnuté |
| **byla použita AI** | **ne** (návrh, rozhoduje uživatel). 86 scén kreslených kódem, 4 archivní fotografie jen barevně upravené (*color adjustment* je výslovná výjimka), S37, S56 a S76 jsou ploché malované ilustrace z ChatGPT (`art/PUVOD.md`) — žádná není fotorealistická ani nezobrazuje konkrétní skutečné místo či událost. Hudba procedurální, hlas není klon |

### Závěrečná obrazovka

`zaver_check.py`: S85–S88 OK (kresba do 2,9 %), takže závěrečná obrazovka
může být plných 20 s, **od 9:22**. Dlaždici i kolečko odběru do **horní
poloviny**, spodní rohy zabírá titulek.

---

## 6. Tagy

```
government debt, national debt, sovereign debt, government bonds, bonds explained,
deficit vs debt, debt to GDP, Greece debt crisis, Japan debt, Bank of Japan,
pension funds, refinancing, bond yields, Eurozone, economics explained,
public finance, science explainer, there's more to it
```

---

## 7. Playlist

Navrženo **`spolecnost`**: státní finance a to, kdo je drží, patří k tématům
o fungování společnosti. Dopiš slug do `playlisty.json`, spusť
`analytics.py --videa` a pak `tools/playlisty.py`.
