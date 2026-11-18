# YouTube — 104 „How Can a Floating Bridge Carry a Tank?"

Stav: **hotovo, naplánováno na zveřejnění** (2026-10-13). Zbylé titulky, americkou stopu, závěrečnou obrazovku a playlist `fyzika` naklikal uživatel ve Studiu.

| | |
|---|---|
| ID videa | **`BOYO3PVRt5c`** — https://www.youtube.com/watch?v=BOYO3PVRt5c |
| master | ✅ `render/final-en-104.mp4` (207, 1920×1080, 6:53, bez chyb) |
| náhled | ✅ od 2026-10-14 hotový obrázek od uživatele `60 TONNES / ON FLOATING BOXES?`, fotka tanku na pontonech (`thumbnail/PUVOD.md`); 13.–14. 10. běželo pod kresleným C1 se stejnými texty — **při srovnání CTR dělit k tomuto datu** |
| nastavení, popis, tagy | ✅ `nahraj.py --k-videu --bez-titulku` 2026-10-13 |
| lokalizace | ✅ 13 jazyků nahráno 2026-10-13 |
| titulky | ✅ ASR smazán; nahráno **en, en-US, cs, de, es, fr, pt-BR, it**. zbylé pl, sv, uk, tr, id, vi, fi nahrál uživatel ručně (kvóta došla u `pl`) |
| americká stopa | ✅ uživatel ve Studiu |
| závěrečná obrazovka | ✅ uživatel ve Studiu |
| playlist | ✅ `fyzika` (uživatel ve Studiu, zapsáno v `playlisty.json`) |

**Co musí uživatel naklikat sám:** nahrát MP4 ve Studiu (průvodce vyřídí
prohlášení o AI a osvědčení o zproštění), závěrečnou obrazovku a americkou
audiostopu (`render/audio-en-US.m4a`).

Stopáž 6:53 (`work/timing.json` total 413,0 s).

> Kdyby se znovu pouštěl `tts.py`, přepočítej kapitoly tady
> i v `youtube-preklady.md` a přegeneruj `en-US` přes `us_stopa.py`.

Pořadí podle CENY (`docs/zverejneni.md`):

```bash
V=videos/104-how-can-a-floating-bridge-carry-a-tank
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
How Can a Floating Bridge Carry a Tank?
```

> Wh-otázka, 39 znaků, pracovní název videa od založení.

---

## 2. Popis

```
A main battle tank weighs more than sixty tonnes, and an army can lay a bridge of floating metal boxes across a river in about thirty minutes. So how does floating metal carry that much weight? And if a bridge goes up that fast, why can't the enemy simply destroy it?

From Archimedes and a block of displaced water to ribbon bridges, amphibious rigs, the floating motorway near Seattle and the failed Russian crossing of the Siverskyi Donets at Bilohorivka in May 2022: why buoyancy is the easy part of a military bridge.

Sources: British Army (M3 Amphibious Bridging Vehicle); General Dynamics European Land Systems (M3, Exercise Anakonda 2016); WSDOT and Guinness World Records (SR 520 Evergreen Point Floating Bridge); FAS / US Army weapon systems handbook (Improved Ribbon Bridge); Conflict and Environment Observatory (Bilohorivka river crossing damage map); US Army, army.mil (Kindy, 2025); Fort Leonard Wood, Engineer Professional Bulletin (Witcomb, 2025); UK Defence Intelligence update of 13 May 2022, as reported by the press.

Subtitles are written for this video, not auto-generated. An American English audio track is available as a second audio track.

Full transcript, sources and translations: https://theresmoretoit-channel.github.io/videos/how-can-a-floating-bridge-carry-a-tank/

CHAPTERS
00:00 Sixty tonnes on floating boxes
00:26 Sixty cubic metres of water
01:26 The hard part
01:53 Surviving the tank itself
03:05 The river pushes back
03:22 Why armies rely on it
04:06 Thirty minutes is not the operation
04:24 Bilohorivka, May 2022
05:11 What actually failed
05:39 Destroyed is not stopped
06:29 Staying alive long enough

IMAGE CREDITS
Evergreen Point Floating Bridge eastbound from HOV lane — SounderBruce, CC BY-SA 4.0, via Wikimedia Commons (colour adjusted)
Exercise Hwang So-06 — UNC - CFC - USFK, CC BY 2.0, via Wikimedia Commons (colour adjusted)
Two M3 Amphibious Rigs during AOH 2022 300522 — Seloloving, CC BY-SA 4.0, via Wikimedia Commons (colour adjusted)
Форсування Сіверського Донця — armyinform.com.ua, CC BY 4.0, via Wikimedia Commons (colour adjusted)
Licences: creativecommons.org/licenses/by-sa/4.0 · creativecommons.org/licenses/by/2.0 · creativecommons.org/licenses/by/4.0
All other archive images are in the public domain.
```

> **Blok se kopíruje CELÝ** (`docs/zverejneni.md`). Povinné kredity jsou
> čtyři CC BY / BY-SA ze `sources.json`: S12, S29, S30, S39, u všech
> s vyznačením úprav („colour adjusted"). Zbylých pět (S01, S11, S20,
> S31, S46) je public domain.
>
> **Pointa se neprozrazuje.** Popis klade obě otázky videa (vztlak,
> zničení) a „buoyancy is the easy part" je jen úhel, ne odpověď.
> Čísla v popisu jsou z `factcheck.md` (60 t, ~30 min).
>
> Kapitoly jsou ze scén S01, S05, S13, S16, S24, S26, S32, S35, S41, S44,
> S50 (`work/timing.json`, zaokrouhleno dolů). Nejkratší je 17 s (S24 → S26),
> poslední 44 s; všechny ≥ 10 s, první na 00:00. Výzva k odběru S15b
> (1:45) leží v kapitole „The hard part".
>
> Zdroje podle `factcheck.md`. Bulletin britské rozvědky je citovaný
> z tiskových zpráv (primární text nedohledán), proto „as reported by
> the press".

---

## 3. Náhled

✅ **C1 „60 TONNES / ON FLOATING BOXES?"** (vybral uživatel 2026-10-13):
tank na pontonech z páteře A. Kresleno kódem (`thumbnail/gen.py`), klíč
`thumbnail` v `project.json`, soubor `render/thumbnail.jpg`. Koncepty
v `thumbnail/KONCEPTY.md`.

---

## 4. Titulky

`subtitles/*.srt`, 14 jazyků + `en-US`. Jazyk videa **`en-gb`** (hlas
`bf_emma`) se musí nastavit dřív, než se nahrají titulkové stopy.
Codex na všech 13 překladech proběhl a nálezy jsou zapracované,
takže titulky a lokalizace můžou nahoru hned po `nahraj.py`.

---

## 5. Nastavení

| | |
|---|---|
| kategorie | **Science & Technology** (28) — posílá `nahraj.py` napevno |
| jazyk videa | `en-gb` |
| licence | standardní |
| pro děti | **ne** |
| komentáře | zapnuté |
| **byla použita AI** | **ne** (návrh, rozhoduje uživatel). 44 scén je kreslených kódem, devět archivních snímků je jen barevně upravených (*color adjustment* je výslovná výjimka). Žádná scéna ze SDXL. Hudba je procedurální, hlas není klon. |

### Závěrečná obrazovka

Může být plných 20 s, **od 6:33** (S50–S52). Závěr je kreslený jen
v dolní polovině. Prvky patří do **horní poloviny**, protože spodní rohy
zabírá titulek (`zaver_check.py`: S50–S52 OK).

---

## 6. Tagy

```
pontoon bridge, floating bridge, military bridge, buoyancy, Archimedes principle,
ribbon bridge, Improved Ribbon Bridge, M3 amphibious rig, military engineering,
river crossing, Bilohorivka, Siverskyi Donets, war in Ukraine, Military Load Classification,
Evergreen Point Floating Bridge, physics explained, science explainer, there's more to it
```

---

## 7. Playlist

Navrženo **`fyzika`**: první polovina videa je vztlak a stabilita, otázka
v titulu je fyzikální. Alternativa je **`legacy`**, kde už leží 098
(drony na drátě), kdyby uživatel četl video spíš jako vojenskou techniku.
Dopiš slug do `playlisty.json`, spusť `analytics.py --videa` a pak
`tools/playlisty.py`.
