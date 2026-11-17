# YouTube — 091 „How Could Aliens Actually Look?"

Stav: **připraveno, nenahráno** — master se renderuje na `.207`.

| | |
|---|---|
| ID videa | — |
| nastavení, popis, tagy | ⬜ |
| náhled | ✅ C1 (`thumbnail/c1-what-is-this.svg`) → `render/thumbnail.jpg` |
| lokalizace | ⬜ 13 jazyků (`youtube-preklady.md`) |
| automatický přepis | ⬜ |
| titulky | ⬜ 14 jazyků + `en-US`, překlady prošly Codexem (commit `fb15708b`) |
| playlist | ⬜ návrh `vesmir` |
| závěrečná obrazovka, americká stopa | ⬜ uživatel ve Studiu |

**Co musí uživatel naklikat sám:** nahrát MP4 ve Studiu (průvodce vyřídí
prohlášení o AI a osvědčení o zproštění), závěrečnou obrazovku a americkou
audiostopu (`render/audio-en-US.m4a`).

Soubor k nahrání: `render/final-en-091.mp4` (stopáž 8:18, `work/timing.json`
total 498,5 s).

Pořadí podle CENY (`docs/zverejneni.md`):

```bash
V=videos/091-how-could-aliens-actually-look
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
How Could Aliens Actually Look?
```

> Wh-otázka, 31 znaků, totožná s nadpisem `script.md`. Neprozrazuje
> pointu (S81–S82: jestli bychom mimozemšťana vůbec poznali).

---

## 2. Popis

```
When we imagine aliens, we usually imagine people with a few changes: grey skin, big eyes, maybe an extra finger. But evolution on another world would have no reason to build anything like us.

Earth has already made creatures stranger than most science fiction: fish that talk with electricity, worms with no mouth that never eat, a slime mould with no brain that solves mazes, and a forest in Utah that is one single living thing. So what could life elsewhere actually look like — and would we even recognise it?

Subtitles are written for this video, not auto-generated. An American English audio track is available as a second audio track.

CHAPTERS
00:00 What we imagine
00:39 Senses we don't have
01:45 Black forests
02:14 Life without eyes
02:46 Life without sunlight
03:14 Gravity changes the shape
03:47 Do aliens need a head?
04:41 One creature or many?
05:18 Giant organisms
06:05 Size changes time
06:30 Life without a planet
07:06 Landing on another world
07:44 So what would they look like?

IMAGE CREDITS
Mormyridae Gnathonemus petersii 2 — NasserHalaweh, CC BY-SA 4.0
Epigean and cave-dwelling Mexican tetras Astyanax mexicanus — Richard Borowsky (New York University), CC BY 3.0
Astyanax fasciatus (Mexican blind cavefish) 3 — James St. John, CC BY 2.0
Vers tubicoles géants (Riftia pachyptila) — IFREMER, CC BY 4.0
Pulpo común (Octopus vulgaris), Parque natural de la Arrábida — Diego Delso, CC BY-SA 4.0
Asterias rubens 179263747 — Michel Langeveld, CC BY-SA 4.0
Physarum polycephalum plasmodium — frankenstoen, CC BY 2.5
Physalia physalis.009 - Praia do Ril (Burela) — Fernando Losada Rodríguez, CC BY-SA 4.0
Aerial View of the Pando Tree — Lance Oditt, Friends of Pando, CC BY-SA 4.0
via Wikimedia Commons
All other archive images are in the public domain.
Licences: creativecommons.org/licenses/by-sa/4.0, creativecommons.org/licenses/by/4.0, creativecommons.org/licenses/by/3.0, creativecommons.org/licenses/by/2.5, creativecommons.org/licenses/by/2.0
```

> **Blok se kopíruje CELÝ** (`docs/zverejneni.md`) — atribuce je UVNITŘ.
> Povinná je u devíti položek ze `sources.json` s licencí CC BY*: S12, S22,
> S23, S27+S30 (dva snímky téže série, jeden řádek), S37, S39, S40, S46
> (zároveň předmět náhledu), S52. Všech třináct záznamů v `sources.json`
> odpovídá archivním scénám ve storyboardu, žádný není osiřelý. Bez
> povinné atribuce: S56 (*Pando 4*, Mx. Granger, CC0), S58 (*Armillaria
> ostoyaea*, George Chernilevsky, PD), S65 (*Jupiter*, NASA, PD), takže
> je pokrývá věta o public domain.
>
> **Ifremer (S27, S30):** Commons má u obou souborů `author = null`
> (nahrál bot z Océanothèque). Zdrojová stránka Ifremeru
> (`image.ifremer.fr/data/00568/67973`) uvádí **Auteurs: IFREMER**, licenci
> CC BY 4.0 a citaci *„IFREMER (2010). Vers tubicoles géants (Riftia
> pachyptila). Ifremer."*. Autor je tedy instituce, ne fotograf (snímky
> pořídil ponorný prostředek Nautile). Ověřeno 2026-10-07; v
> `sources.json` zůstává `credit: null` (generovaný soubor, neupravuje se
> ručně).
>
> Kapitoly jsou ze scén S01, S06, S16, S21, S26, S31, S36, S45, S51, S59,
> S64, S69, S76 (`work/timing.json`, časy zaokrouhlené dolů). Nejkratší
> kapitola je 25 s (S59 → S64), všechny ≥ 10 s, první na 00:00. **Po
> každém dalším běhu `tts.py` časy přepočítej** — a stejně tak
> v `youtube-preklady.md`.
>
> Video **nemá scénu s výzvou k odběru** (žádné `cta: true` ve storyboardu),
> takže kapitoly nic neposouvá.
>
> Popis neprozrazuje pointu S81–S82; poslední věta prvního odstavce ji jen
> klade jako otázku. Příklady ve druhém odstavci (S12–S13, S27–S30, S40–S43,
> S52–S54) jsou ověřené ve `factcheck.md`.

---

## 3. Náhled

✅ **C1** (`thumbnail/c1-what-is-this.svg`, kresleno kódem `thumbnail/gen.py`)
→ `render/thumbnail.jpg`, `ALIENS / WHAT IS THIS?` nad výřezem fotky
měchýřovky (S46, Fernando Losada Rodríguez, CC BY-SA 4.0, už v kreditech).
Původ, otisk a licence v `thumbnail/PUVOD.md`, ostatní koncepty
v `thumbnail/KONCEPTY.md`.

---

## 4. Titulky

`subtitles/*.srt`, 14 jazyků + `en-US`. Jazyk videa **`en-gb`** (hlas
`bf_emma`) se musí nastavit dřív, než se nahrají titulkové stopy. Codex
proběhl na všech 13 překladech včetně `cs` a nálezy jsou zapracované
(commit `fb15708b`).

---

## 5. Nastavení

| | |
|---|---|
| kategorie | Science & Technology |
| jazyk videa | `en-gb` |
| licence | standardní |
| pro děti | **ne** |
| komentáře | zapnuté |
| **byla použita AI** | **ne** (návrh, rozhoduje uživatel). 66 scén kreslených kódem, 13 archivních fotografií jen barevně upravených (*color adjustment* je výslovná výjimka), 9 SDXL scén (S20, S24, S66, S70–S75) díky kotvě stylu jako malované ilustrace, ne fotorealismus, a žádná nezobrazuje skutečné místo ani událost. Hudba procedurální, hlas není klon |

### Závěrečná obrazovka

`zaver_check.py`: S79–S82 mají kresbu do 1,5 % plochy, dlaždice i kolečko
odběru se vejdou kamkoli kromě spodních rohů (titulek). Dej je do **horní
poloviny**. Dlaždice: návrh **092** (*Why Might Aliens Look Surprisingly
Human?*), jakmile bude zveřejněné. Je to přímé pokračování opačnou
otázkou. Do té doby **029** (*What If We Detected Aliens?*).

---

## 6. Tagy

```
aliens, what would aliens look like, alien life, extraterrestrial life,
astrobiology, evolution, alien biology, red dwarf plants, tube worms,
slime mould, octopus intelligence, portuguese man o war, pando,
honey fungus, life on other planets, science explainer, there's more to it
```

---

## 7. Playlist

Navrženo **`vesmir`** (*Space — Getting There, and Who Else Is Out
There*). Sousedí s 029 (signál od mimozemšťanů) a 032 (Fermiho paradox),
tedy s druhou půlkou názvu playlistu. **Sesterské video 092** (*Why Might
Aliens Look Surprisingly Human?*) patří do téhož playlistu hned vedle
(091 se ptá, jak jiní by mohli být, 092 proč by mohli být podobní).
Dopiš slug do `playlisty.json`, spusť `analytics.py --videa` a pak
`tools/playlisty.py`.
