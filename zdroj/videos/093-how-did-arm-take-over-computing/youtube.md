# YouTube — 093 „How Did ARM Take Over Computing?"

Stav: **zveřejněno** (`DEZvBz32pnE`), hotovo 2026-10-07.

| | |
|---|---|
| ID videa | `DEZvBz32pnE` (https://www.youtube.com/watch?v=DEZvBz32pnE) |
| nastavení, popis, tagy | ✅ `nahraj.py --k-videu` 2026-10-07 |
| náhled | ✅ C1 (`thumbnail/c1-unplugged.svg`) → `render/thumbnail.jpg` |
| lokalizace | ✅ 13 jazyků + `en-GB` (`lokalizace.py` 2026-10-07) |
| automatický přepis | ✅ čistý (nic ke smazání) |
| titulky | ✅ `en`, `en-US` (API) + 13 jazyků ručně uživatelem |
| playlist | ⬜ návrh `legacy` |
| závěrečná obrazovka, americká stopa | ✅ uživatel ve Studiu |

**Co musí uživatel naklikat sám:** nahrát MP4 ve Studiu (průvodce vyřídí
prohlášení o AI a osvědčení o zproštění), závěrečnou obrazovku a americkou
audiostopu (`render/audio-en-US.m4a`).

Soubor k nahrání: `render/final-en-093.mp4` (stopáž 9:50, `work/timing.json`
total 590,3 s).

Pořadí podle CENY (`docs/zverejneni.md`):

```bash
V=videos/093-how-did-arm-take-over-computing
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
How Did ARM Take Over Computing?
```

> Wh-otázka, 32 znaků, totožná s nadpisem `script.md`. Neprozrazuje pointu
> (S85–S86: nevyhrála jednoduchost ani nízká spotřeba, ale návrh, obchodní
> model a svět na baterie).

---

## 2. Popis

```
In 1985, the first ARM processor was switched on for the first time, and it kept running even though its power supply wasn't connected. Forty years later, its descendants are in almost every smartphone, in Apple's computers and in some of the largest data centres in the world.

The usual explanation is that ARM is simple and efficient, and efficient wins. But a modern ARM core is anything but simple, and since the mid-1990s Intel's chips have looked surprisingly similar inside. So how did a chip from a British home-computer company end up everywhere?

Subtitles are written for this video, not auto-generated. An American English audio track is available as a second audio track.

CHAPTERS
00:00 The chip that ran without power
01:10 Acorn, 1983
02:11 The RISC idea
03:34 The ARM1
04:09 The Archimedes
04:46 Apple and a new company
05:17 Selling the design
06:00 Phones
06:35 Is simple the answer?
07:13 Two different things
07:36 What happened to x86
08:34 Back to Apple
09:07 Data centres
09:30 What they really built

IMAGE CREDITS
Acorn Archimedes A310 with mouse and keyboard — mikkohoo, CC BY-SA 4.0
Apple Newton MessagePad 100 — Felix Winkelnkemper, CC BY-SA 4.0
Nokia 6110 blue-92111 — Raimond Spekking, CC BY-SA 4.0
via Wikimedia Commons
All other archive images are in the public domain or CC0.
Licences: creativecommons.org/licenses/by-sa/4.0
```

> **Blok se kopíruje CELÝ** (`docs/zverejneni.md`) — atribuce je UVNITŘ.
> Povinná je u tří položek ze `sources.json` s licencí CC BY*: S41, S48,
> S63. Bez povinné atribuce: S14 (*BBC Micro Front Restored*, public domain)
> a S89 (*Apple M1*, Henriok, CC0), proto „public domain or CC0“. Všech pět
> záznamů v `sources.json` odpovídá archivním scénám storyboardu.
>
> Kapitoly jsou ze scén S01, S13, S22, S35, S41, S48, S54, S61, S67, S74, S78,
> S87, S93, S98 (`work/timing.json`, časy zaokrouhlené dolů). Nejkratší
> kapitola je 20 s (S98 → konec), všechny ≥ 10 s, první na 00:00. **Po
> každém dalším běhu `tts.py` časy přepočítej** — a stejně tak
> v `youtube-preklady.md`. Výzva k odběru S12b leží uvnitř první kapitoly.
>
> Popis vynechává odpověď (S85–S86) a nabízí jen „obvyklé vysvětlení“, které
> video v S67–S68 přebije. Fakta (1985, napájení přes vstupy, Intel od pol.
> 90. let mikrooperace) jsou ve `factcheck.md`. „Small“ v popisu není:
> Acorn po BBC Micro malý nebyl (factcheck), stejně jako ve scénáři S11.

---

## 3. Náhled

✅ **C1** `ARM / UNPLUGGED?` (`thumbnail/c1-unplugged.svg`, kresleno kódem `thumbnail/gen.py`) → `render/thumbnail.jpg`. Ostatní koncepty v `thumbnail/KONCEPTY.md`. Nic převzatého, takže `PUVOD.md` není potřeba.

---

## 4. Titulky

`subtitles/*.srt`, 14 jazyků + `en-US`. Jazyk videa **`en-gb`** (hlas
`bf_emma`) se musí nastavit dřív, než se nahrají titulkové stopy. Codex
proběhl na všech 13 překladech včetně `cs`; titulky se nahrávají až po
zapracování nálezů.

---

## 5. Nastavení

| | |
|---|---|
| kategorie | Science & Technology |
| jazyk videa | `en-gb` |
| licence | standardní |
| pro děti | **ne** |
| komentáře | zapnuté |
| **byla použita AI** | **ne** (návrh, rozhoduje uživatel). 90 scén kreslených kódem, 5 archivních fotografií jen barevně upravených (*color adjustment* je výslovná výjimka), 3 SDXL scény (S19, S53, S93) díky kotvě stylu jako malované ilustrace, ne fotorealismus; S19 a S53 zobrazují obecný dům a stodolu, ne konkrétní skutečné místo. Hudba procedurální, hlas není klon |

### Závěrečná obrazovka

`zaver_check.py`: S96–S101 mají kresbu do 7 % plochy a horní polovina je
v závěru (S98–S101) prázdná schválně. Dlaždici i kolečko odběru dej do
**horní poloviny**, spodní rohy zabírá titulek. Dlaždice: návrh **088**
(*Why Is Computer Stuff Called That?*) — taky o dějinách počítačů.

---

## 6. Tagy

```
ARM, ARM processor, how did ARM take over, ARM vs x86, RISC, Acorn,
BBC Micro, Sophie Wilson, Steve Furber, ARM1, Apple Silicon, Apple M1,
instruction set, microarchitecture, history of computing, CPU,
smartphone processor, science explainer, there's more to it
```

---

## 7. Playlist

Navrženo **`legacy`** (*Legacy Tech — The Old Systems Still Running
Everything*): rozhraní navržené v roce 1985 dnes nese telefony, Macy i
datová centra. Dopiš slug do `playlisty.json`, spusť `analytics.py --videa`
a pak `tools/playlisty.py`.
