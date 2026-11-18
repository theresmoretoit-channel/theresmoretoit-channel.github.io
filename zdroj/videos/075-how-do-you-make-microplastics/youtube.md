# YouTube — 075 „How Do You Make Microplastics Without Knowing It?"

Stav: **NAHRÁNO VŠE PŘES API** (1. 10.): metadata, náhled, lokalizace, 15 titulkových stop. Ruční část ve Studiu hotová (uživatel 2026-10-01). **HOTOVO.**

| | |
|---|---|
| ID videa | `nLwF9bOnTfQ` (https://www.youtube.com/watch?v=nLwF9bOnTfQ) |
| nastavení, popis, tagy | ✅ 2026-09-30 `nahraj.py --k-videu nLwF9bOnTfQ --bez-titulku` (jazyk en-GB potvrzen čtením); AI prohlášení NE (uživatel) |
| náhled | ✅ 2026-10-01 (druhý běh `nahraj.py --k-videu nLwF9bOnTfQ --bez-titulku`) |
| lokalizace | ✅ 2026-10-01 13 jazyků jedním voláním (`lokalizace.py --id`) |
| automatický přepis | ✅ smazán 2026-10-01 (může se po zpracování vrátit — za pár dní `titulky.py $V --smaz-asr`) |
| titulky | ✅ 2026-10-01 15 stop, ověřeno `captions.list`: cs, de, en-GB, en-US, es, fi, fr, id, it, pl, pt-BR, sv, tr, uk, vi (vše `standard`) |
| playlist | ✅ `bezne` (ručně ve Studiu, slug v `playlisty.json` za 012) |
| závěrečná obrazovka, americká stopa | ✅ uživatel ve Studiu 2026-10-01 |

**Co musí uživatel naklikat sám:** závěrečnou obrazovku (API na ni nemá zdroj)
a nahrát americkou audiostopu (`render/audio-en-US.m4a`). Prohlášení o AI
a osvědčení o zproštění vyřídí průvodce při ručním nahrání MP4 — **u AI ale
tentokrát rozhodni vědomě**, viz kapitola 5.

Soubor k nahrání: `render/final-en-075.mp4` (686,4 s, ověřeno).

Pořadí podle CENY (`docs/zverejneni.md`):

```bash
V=videos/075-how-do-you-make-microplastics
python tools/nahraj.py $V --k-videu nLwF9bOnTfQ --bez-titulku   # 100
python tools/analytics.py --videa                         #   1  ← nutné
python tools/lokalizace.py $V                             #  50
python tools/titulky.py $V --smaz-asr                     # 150  ← před titulky
python tools/titulky.py $V                                # 400×15
python tools/playlisty.py                                 # 100
```

---

## 1. Titul

```
How Do You Make Microplastics Without Knowing It?
```

> wh-otázka („How…") — podle `docs/kanal-metriky.md` nejlepší CTR. Titul
> neprozrazuje odpověď (otěr při běžném používání).

---

## 2. Popis

```
We usually think of plastic pollution as something we throw away. But some microplastics come from things that are working exactly as intended.

A kitchen sponge. A cutting board. Containers in a dishwasher. Clothes in a washing machine. A string trimmer. The soles of your shoes. A toothbrush. An artificial football pitch. They don't look like the same problem, but they all involve plastic being worn away simply by being used.

This video goes through the research behind each of them: what the studies measured, what they only estimated, and what we still don't know about what these particles do to our bodies.

It follows an earlier video about one of the biggest sources of microplastic pollution, the tyres on your car: https://youtu.be/9Xo3Ci3WFaA

Subtitles are written for this video, not auto-generated. An American English audio track is available as a second audio track.

Full transcript, sources and translations: https://theresmoretoit-channel.github.io/videos/how-do-you-make-microplastics/

CHAPTERS
00:00 The plastic you never throw away
00:47 Kitchen sponges
01:27 Magic erasers
02:02 Cutting boards
02:56 The dishwasher
03:34 The washing machine
04:30 The string trimmer
05:31 Shoes
06:30 Toothbrushes
07:30 Artificial turf
08:41 The pattern
09:06 Plastic, friction, wear, particles
09:55 What we don't know
10:21 A world of durable materials

IMAGE CREDITS
Magic eraser — Whoisjohngalt at English Wikipedia, CC BY-SA 3.0, via Wikimedia Commons
String trimmer head — StrangeApparition2011, CC BY-SA 4.0, via Wikimedia Commons
Artificial turf football field, Regent's International School Bangkok — TheRegentsInternationalSchoolBangkok, CC BY-SA 4.0, via Wikimedia Commons
Licences: creativecommons.org/licenses/by-sa/3.0, /by-sa/4.0
```

> **Blok se kopíruje CELÝ** (`docs/zverejneni.md`) — atribuce jsou UVNITŘ.
> Všechny tři archivní snímky (S13, S37, S61) jsou CC BY-SA, tedy povinné;
> jiné archivní snímky video nemá, proto chybí řádek o public domain.
> S36 (ChatGPT) a S71 (SDXL) atribuci nepotřebují.
>
> Kapitoly jsou ze scén S01, S07, S13, S16, S23, S29, S36, S45, S53, S60,
> S68, S72, S78, S81 (`work/timing.json` draftu 2, celkem 686,3 s). Všechny
> ≥ 10 s. **Po každém dalším běhu `tts.py` časy přepočítej** — a stejně
> tak v `youtube-preklady.md`.
>
> **Popis netvrdí škodlivost.** Že nevíme, co částice dělají v těle, je
> ve scénáři S78–S80; popis to drží ve stejné míře jistoty. „Measured /
> estimated" odpovídá fact checku (houbičky, sekačka odhad, kartáčky
> simulace).
>
> Odkaz na 012 (`https://youtu.be/9Xo3Ci3WFaA`, z `Témata.ods`) — video
> na něj v S05 odkazuje slovy „In another video". Hodí se i jako dlaždice
> závěrečné obrazovky.

---

## 3. Náhled

`render/thumbnail.jpg`: **hotový**, koncept K1 (ojetá houbička,
„MICROPLASTICS / MADE BY YOU?", ChatGPT, dodal uživatel 2026-09-30). Původ
v `thumbnail/PUVOD.md`; `thumb_check.py`: jas 93,2, kontrast 93,5, uvnitř
pásma kanálu. Ve 150 px se nepere s náhledem 012.

---

## 4. Titulky

`subtitles/*.srt`, 14 jazyků + `en-US`. Jazyk videa **`en-gb`** (hlas
`bf_emma`) se musí nastavit dřív, než se nahrají titulkové stopy, jinak
zůstane dlaždice Titulky zašedlá.

---

## 5. Nastavení

| | |
|---|---|
| kategorie | Education |
| jazyk videa | `en-gb` |
| licence | standardní |
| pro děti | **ne** |
| komentáře | zapnuté |

### Prohlášení o AI: **rozhodne uživatel**

Rozhoduje fotorealističnost, ne použití AI. Většina videa je v pořádku:
84 scén kreslených kódem, 3 barevně upravené archivní snímky (výjimka
„color adjustment"), hudba procedurální, hlas není klon skutečné osoby.

**Dvě scény jsou ale jiné:**

- **S36 zahrada** — obrázek z ChatGPT (`art/PUVOD.md`), **skoro
  fotorealistický**. Zobrazuje obecnou zahradu, ne konkrétní skutečné
  místo ani událost.
- **S71 kuchyně** — SDXL, spíš malovaná než fotografická.

Pravidla žádají označení u realistického obsahu, který by si divák mohl
splést se skutečným záběrem. Obecná zahrada na čtyři sekundy jako předěl
je hraniční případ — proto to tu není předvyplněné.

### Závěrečná obrazovka

S86, S86b a S86c mají **horní polovinu volnou** (kresba jen dole) — dlaždici
dalšího videa i kolečko odběru dej do **horní** poloviny (`zaver_check.py`
ověřeno na draftu 2). Jako dlaždici doporučuju **012** (pneumatiky), na které
video v S05 i S83 navazuje.

> Epilog slibuje navazující video („what can we actually do about it?").
> Až vznikne, patří na dlaždici místo 012.

---

## 6. Tagy

```
how do you make microplastics, microplastics, microplastic pollution,
where do microplastics come from, nanoplastics, kitchen sponge microplastics,
melamine sponge, cutting board microplastics, dishwasher microplastics,
washing machine microfibres, string trimmer, shoe sole abrasion,
toothbrush microplastics, artificial turf, science explained, explainer,
there's more to it
```

---

## 7. Playlist

Playlist `bezne` („Ordinary Things, Awkward Questions", spolu s 012).
Dopiš slug do `playlisty.json` hned za 012, spusť `analytics.py --videa`
a pak `tools/playlisty.py`.
