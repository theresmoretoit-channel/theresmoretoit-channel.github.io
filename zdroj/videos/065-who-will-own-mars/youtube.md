# YouTube — 065 „Who Will Own Mars?"

Stav: **NAPLÁNOVÁNO ZVEŘEJNĚNÍ** (MP4 nahráno ručně 2026-09-25, zbytek dílem přes API, dílem ručně).

| | |
|---|---|
| ID videa | **`pnaB0b0WdiU`** |
| odkaz | https://youtu.be/pnaB0b0WdiU |
| nastavení, popis, tagy, náhled | ✅ `nahraj.py --k-videu --bez-titulku` |
| lokalizace | ✅ 14 jazyků jedním voláním |
| titulky | ✅ 15 stop: en, cs, sv, es, pt-BR, de, fr přes API; **it, pl, id, tr, uk, vi, fi, en-US doklikal uživatel ručně** (kvóta došla na `it`) |
| automatický přepis | při nahrávání ještě nebyl — **vznikne později, za pár dní sebrat** `titulky.py $V --smaz-asr` (150) |
| playlist `spolecnost` | ✅ ručně ve Studiu; zapsáno i do `playlisty.json` |
| závěrečná obrazovka, americká stopa, zbylá nastavení | ✅ uživatel ve Studiu |
| zveřejnění | ✅ naplánováno |

**Co musí uživatel naklikat sám:** závěrečnou obrazovku (API na ni nemá
ani zdroj) a nahrát americkou audiostopu. Prohlášení o AI a osvědčení
o zproštění vyřídí průvodce při ručním nahrání MP4.

Pořadí podle CENY a podle věcí, které na sobě závisí (`docs/zverejneni.md`):

```bash
V=videos/065-who-will-own-mars
python tools/nahraj.py $V --k-videu <ID> --bez-titulku   # 100
python tools/analytics.py --videa                        #   1  ← nutné
python tools/lokalizace.py $V                            #  50
python tools/titulky.py $V --smaz-asr                    # 150  ← před titulky
python tools/titulky.py $V                               # 400×15
python tools/playlisty.py                                # 100
```

---

## 1. Titul

```
Who Will Own Mars?
```

Wh-otázka (`docs/kanal-metriky.md`: 2,23 % proti 1,63 % u tvrzení).

---

## 2. Popis

```
In 1967, the Outer Space Treaty settled one thing: no country can claim
Mars. In 2020, SpaceX put a sentence about Mars into the terms of service
for Starlink: a free planet, where no Earth-based government has authority
or sovereignty over Martian activities.

So who will own Mars? Nobody can own the land. But you can own a city, a
reactor and everything you have built — and once safety zones appear
around them, it starts looking suspiciously like property.

And the bigger question comes later. What happens when millions of people
live on Mars, most of them born there, and a government on Earth still
tells them they are its citizens?

Spoiler warning: from 07:24 the video discusses For All Mankind and The
Expanse. To skip that part, jump to 08:30.

Subtitles are written for this video, not auto-generated. An American
English audio track is available as a second audio track.

Full transcript, sources and translations: https://theresmoretoit-channel.github.io/videos/who-will-own-mars/

CHAPTERS
00:00 A city on another planet
00:49 The Outer Space Treaty
01:22 A sentence buried in Starlink's terms
01:54 Who supervises a company on Mars?
02:30 Islands of civilisation
03:12 You own the city, not the land
04:03 Safety zones
04:40 How colonies become societies
05:35 Now put that on Mars
06:12 What a state really needs
06:56 Could Mars become a country?
07:24 Spoilers: For All Mankind and The Expanse
08:30 Back to Elon
09:04 The paradox
09:24 Two stages of colonisation
09:43 The question that comes next
10:09 Where the history of Mars begins

IMAGE CREDITS
Signing Outer Space Treaty — ITU, CC BY 2.0
via Wikimedia Commons
Licences: creativecommons.org/licenses/by/2.0/

All other archive images are in the public domain.
```

> **Blok se kopíruje CELÝ.** Atribuce S07 (ITU, CC BY 2.0) je uvnitř
> schválně. Public domain snímky (Ortelius, Trumbull, NASA/JPL) se
> nevypisují.
>
> **Časy `07:24` a `08:30` ve větě o spoilerech** jsou začátky S51 a S57
> z `work/timing.json`; `08:30` je zároveň na spoilerové obrazovce S51.
> Po změně stopáže před S57 se musí změnit obojí.

---

## 3. Náhled

`render/thumbnail.jpg` — **koncept c2 (rozparcelovaná planeta)**, vybral uživatel 2026-09-25. Princip je v `CLAUDE.md`
(„Thumbnail není titulková karta"), zadání v `docs/thumbnail-styl.md`,
kontrola `python tools/thumb_check.py videos/065-who-will-own-mars`.

---

## 4. Titulky

`subtitles/*.srt`, všech 14 jazyků + `en-US`. Jazyk videa **`en-gb`**
(hlas `bf_emma`) se musí nastavit dřív, než se nahrají titulkové stopy.

Nápisy na spoilerové obrazovce S51 jsou jen anglicky; v ostatních
jazycích to kryje kapitola a věta o spoilerech v lokalizovaném popisu.

---

## 5. Nastavení

| | |
|---|---|
| kategorie | Education |
| jazyk videa | `en-gb` |
| licence | standardní |
| pro děti | **ne** |
| komentáře | zapnuté |

### Prohlášení o AI: **ne**

Rozhoduje fotorealističnost. Dvě SDXL scény (S40 dítě u okna kopule, S58
město na Marsu) jsou malované ilustrace podle kotvy stylu a nezobrazují
žádné skutečné místo ani událost; 66 scén je kreslených kódem, archivní
snímky jsou upravené jen barevně, hudba je procedurální.

### Závěrečná obrazovka

`zaver_check.py`: S68–S70 OK. Dlaždici i kolečko dej do **horní** poloviny,
dole je titulek diagramu; bod Země uprostřed nahoře nevadí.

---

## 6. Tagy

```
mars, who owns mars, mars colonisation, outer space treaty, space law,
spacex, starlink, elon musk, artemis accords, safety zones, colonies,
independence, for all mankind, the expanse, explainer, there's more to it
```

---

## 7. Playlist

`spolecnost` — „How Society Actually Runs", soused 020 *Who Runs the
Earth?* Dopiš slug do `playlisty.json`, spusť `analytics.py --videa`
a pak `tools/playlisty.py`.
