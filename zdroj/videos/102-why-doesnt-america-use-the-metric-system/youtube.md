# YouTube — 102 „Why the Hell Doesn't America Use the Metric System?"

Stav: **hotovo, naplánováno na zveřejnění** (2026-10-11). Titulky sv…fi + en-US a playlist doklikal uživatel ve Studiu.

| | |
|---|---|
| ID videa | **`xcOK7VRyQZM`** — https://www.youtube.com/watch?v=xcOK7VRyQZM |
| master | ✅ `render/final-en-102.mp4` (1920×1080, 10:13, dekódování bez chyby) |
| náhled | ✅ C1 „AMERICA / 65 WHAT?" — `render/thumbnail.jpg` (vybral uživatel 2026-10-11) |
| nastavení, popis, tagy | ✅ `nahraj.py --k-videu --bez-titulku` 2026-10-11 |
| lokalizace | ✅ nahráno 2026-10-11, 13 jazyků v `youtube-preklady.md`, Codex 2026-10-11 (23 nálezů přijato, 9 zamítnuto) |
| titulky | ⏳ ASR smazán; nahoře **en, cs**, zbytek spadl na kvótě → po 9:00: `titulky.py $V --jen sv,es,pt-BR,de,fr,it,pl,id,tr,uk,vi,fi,en-US` |
| playlist | ⏳ `legacy` (na konec) zapsán v `playlisty.json`, `playlisty.py` po resetu kvóty |
| závěrečná obrazovka, americká stopa | ⏳ uživatel ve Studiu |

**Co musí uživatel naklikat sám:** nahrát MP4 ve Studiu (průvodce vyřídí
prohlášení o AI a osvědčení o zproštění), závěrečnou obrazovku a americkou
audiostopu (`render/audio-en-US.m4a`).

Soubor k nahrání: `render/final-en-102.mp4` (stopáž 10:13, `work/timing.json`
total 613,1 s).

> Kdyby se znovu pouštěl `tts.py`, přepočítej kapitoly tady
> i v `youtube-preklady.md` a přegeneruj `en-US` přes `us_stopa.py`.

> **I-19 ověřeno 2026-10-11: tabule pořád stojí** (`factcheck.md`). Kdyby se zveřejňovalo o hodně později, ověř znovu
> (S40b říká *„Those signs are still there today."*; USDOT ohlásil
> revizi, viz `factcheck.md`).

Pořadí podle CENY (`docs/zverejneni.md`):

```bash
V=videos/102-why-doesnt-america-use-the-metric-system
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
Why the Hell Doesn't America Use the Metric System?
```

> Wh-otázka, 51 znaků, schválená uživatelem i s „the Hell".
> „America" = USA záměrně: je to ustálené znění, pod kterým se téma hledá,
> a S01 hned říká *„in the United States"*. V překladech titulu se
> používá místní název USA (rozhodl uživatel 2026-10-11).

---

## 2. Popis

```
Sixty-five what? Drive along any road in the United States and the speed limits, the weather forecast and the recipes all use units that almost nobody else on Earth uses. So why hasn't America simply switched to the metric system like nearly every other country?

The strange part is that, in a way, it already has. From Thomas Jefferson's decimal plan and a French scientist captured by privateers to President Ford's Metric Conversion Act, kilometre signs on an Arizona interstate and a Mars probe lost to a mix-up of units, and how Ireland, Australia and Britain went about it.

Sources: NIST (the 1959 definition of the inch and pound); BIPM (the Metre Convention, 1875); Statement on signing the Metric Conversion Act (1975); Congressional Research Service (report 95-875); Mars Climate Orbiter Mishap Investigation Board, Phase I Report (1999); NASA Management Instruction 8010.2A (1991); RTÉ News (20 January 2005).

Subtitles are written for this video, not auto-generated. An American English audio track is available as a second audio track.

Full transcript, sources and translations: https://theresmoretoit-channel.github.io/videos/why-doesnt-america-use-the-metric-system/

CHAPTERS
00:00 Sixty-five what?
00:47 The strange part
01:40 Not imperial at all
02:22 France builds something new
03:05 Did pirates stop it?
03:46 Why units stick
04:35 America finally tries
05:47 Metric where it's useful
06:23 The price of two systems
07:18 Are Americans being stupid?
08:05 How did other countries do it?
08:36 And then there's Britain
09:36 So why doesn't America use metric?

IMAGE CREDITS
I-19 metric: El Paso, Phoenix – 3 km, Ajo Way – 1 km — ossguy, CC BY-SA 2.0, via Flickr (colour-graded, licence plates blurred)
Licence: creativecommons.org/licenses/by-sa/2.0
All other archive images are in the public domain.
```

> **Blok se kopíruje CELÝ** (`docs/zverejneni.md`). Jediný povinný kredit
> je S40 (ossguy, CC BY-SA 2.0, `sources.json`), u BY-SA i s uvedením úprav.
> Ostatní archivní snímky (S11 metr, S23 Jefferson, S37 Ford, S44 Reagan,
> S50 Mars Climate Orbiter) jsou public domain.
>
> **Pointa se neprozrazuje.** Popis ani kapitoly neříkají, že přechod byl
> dobrovolný, že nikdo nestanovil datum, ani že Irsko přešlo za jednu noc —
> jen „how Ireland, Australia and Britain went about it". Věta *„in a way,
> it already has"* je háček z S08, ne odpověď (ta je v S68–S69c).
>
> Kapitoly jsou ze scén S01, S08, S15, S20, S25, S30, S36, S45, S49, S55,
> S61, S64, S70 (`work/timing.json`, zaokrouhleno dolů). Nejkratší kapitola
> je 31 s (S61 → S64), poslední 37 s; všechny ≥ 10 s, první na 00:00.
> Výzva k odběru S14b (1:32) leží v kapitole „The strange part".
>
> Zdroje podle `factcheck.md`: NIST survey foot (S09–S11), BIPM (S28),
> presidency.ucsb.edu (S37), CRS 95-875 (S38–S44), MIB Phase I (S50–S53),
> NMI 8010.2A (S53b), RTÉ 20. 1. 2005 (S62).

---

## 3. Náhled

✅ **C1 „AMERICA / 65 WHAT?"** (vybral uživatel 2026-10-11) — značka
SPEED LIMIT 65, kterou video otevírá. Kresleno kódem (`thumbnail/gen.py`),
klíč `thumbnail` v `project.json`, soubor `render/thumbnail.jpg`.

---

## 4. Titulky

`subtitles/*.srt`, 14 jazyků + `en-US`. Jazyk videa **`en-gb`** (hlas
`bf_emma`) se musí nastavit dřív, než se nahrají titulkové stopy. Titulky
a lokalizace se nahrávají **až po zapracování nálezů Codexu** na všech
překladech scénáře.

---

## 5. Nastavení

| | |
|---|---|
| kategorie | **Science & Technology** (28) — posílá `nahraj.py` napevno |
| jazyk videa | `en-gb` |
| licence | standardní |
| pro děti | **ne** |
| komentáře | zapnuté |
| **byla použita AI** | **ne** (návrh, rozhoduje uživatel). Většina scén kreslená kódem, 6 archivních snímků jen barevně upravených (*color adjustment* je výslovná výjimka; u S40 navíc rozostřené SPZ), 5 SDXL scén (S16, S20, S26, S36, S74) jsou malované ilustrace podle kotvy stylu — nefotorealistické, žádné konkrétní skutečné místo či událost. Hudba procedurální, hlas není klon |

### Závěrečná obrazovka

Může být plných 20 s, **od 9:53** (S72–S74). `zaver_check.py`: S72–S74 OK,
prvky do **horní poloviny**, spodní rohy zabírá titulek. S74 je SDXL obloha
(malba), prvky přes ni nevadí.

---

## 6. Tagy

```
metric system, imperial units, US customary units, why doesn't America use metric,
metrication, Metric Conversion Act, Mars Climate Orbiter, Thomas Jefferson,
Fahrenheit, miles vs kilometres, Interstate 19, Ireland metric, Britain metric,
units of measurement, science explainer, there's more to it
```

---

## 7. Playlist

Navrženo **`legacy`** (*Legacy Tech — The Old Systems Still Running
Everything*): video je přesně o starém standardu, který se nevymění, protože
na něm stojí všechno ostatní (S30–S32 „infrastruktura", S60 cena přechodu).
Alternativa **`spolecnost`** (*How Society Actually Runs*), kdyby uživatel
četl video spíš jako o tom, kdo rozhoduje (datum, které nikdo nestanovil).
Dopiš slug do `playlisty.json`, spusť `analytics.py --videa` a pak
`tools/playlisty.py`.
