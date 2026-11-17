# YouTube — 100 „Why Would Preparing for War Keep the Peace?"

Stav: **nahráno, hotovo** (`J4MX-4FZnHI`, 2026-10-10). Titulky 14 jazyků + `en-US` prošly Codexem
(2026-10-10), čeština schválena uživatelem.

| | |
|---|---|
| ID videa | `J4MX-4FZnHI` (https://www.youtube.com/watch?v=J4MX-4FZnHI), MP4 nahrál uživatel 2026-10-10 |
| master | ✅ `render/final-en-100.mp4` (2026-10-10, render na .207, 1920×1080, 453,5 s, dekóduje se čistě) |
| náhled | ✅ C3 WANT PEACE? / PREPARE FOR WAR? (`render/thumbnail.jpg`) |
| nastavení, popis, tagy | ✅ 2026-10-10 (`nahraj.py --k-videu --bez-titulku`), ověřeno: 18 tagů, en-GB |
| lokalizace | ✅ 13 jazyků + en (`lokalizace.py`, ověřeno 14) |
| automatický přepis | ✅ při nahrávání titulků nebyl (zkontrolovat znovu, YouTube ho vyrábí dodatečně) |
| titulky | ✅ 15 stop — en-GB, en-US, cs, es, pt-BR, de, fr, it přes `titulky.py`, zbylých 7 uživatel ručně ve Studiu (2026-10-10) |
| playlist | ✅ `spolecnost`, pozice 21 (`playlisty.py`) |
| závěrečná obrazovka, americká stopa | ✅ uživatel ve Studiu |

**Co musí uživatel naklikat sám:** nahrát MP4 ve Studiu (průvodce vyřídí
prohlášení o AI a osvědčení o zproštění), závěrečnou obrazovku a americkou
audiostopu (`render/audio-en-US.m4a`).

Soubor k nahrání: `render/final-en-100.mp4` (stopáž 7:33, `work/timing.json`
total 453,5 s).

> Kdyby se znovu pouštěl `tts.py`, přepočítej kapitoly tady
> i v `youtube-preklady.md` a přegeneruj `en-US` přes `us_stopa.py`.

Pořadí podle CENY (`docs/zverejneni.md`):

```bash
V=videos/100-why-would-preparing-for-war-keep-the-peace
python tools/nahraj.py $V --k-videu=<ID> --bez-titulku    # 100
python tools/analytics.py --videa                         #   1  ← nutné
python tools/lokalizace.py $V                             #  50
python tools/titulky.py $V --smaz-asr                     # 150  ← před titulky
python tools/titulky.py $V                                # 400×15
python tools/playlisty.py                                 #  50
```

Render node .207: kopie v `/home/vrana/temp/` smazána 2026-10-10.

---

## 1. Titul

```
Why Would Preparing for War Keep the Peace?
```

> Wh-otázka, 43 znaků, totožná s nadpisem `script.md`. Neprozrazuje
> odpověď (odstrašení — a že funguje jen tehdy, když druhá strana hrozbě
> věří, rozumí jí a nepanikaří).

---

## 2. Popis

```
Do you want peace? Then prepare for war. The advice is around sixteen hundred years old, and in 2025 the world spent nearly 2.9 trillion dollars on the military, the most ever recorded.

But if the goal is never to fight, why build tanks, missiles and warships? Can weapons actually keep the peace, or do they just make everyone more afraid of each other? From a Roman writer's complaint about a neglected army to the Dreadnought race, seventy thousand nuclear warheads, the Falklands and one night in 1983 when a Soviet warning system reported incoming missiles.

Military spending: SIPRI (April 2026). Nuclear warheads: Federation of American Scientists. Falklands: the Franks Report (1983).

Subtitles are written for this video, not auto-generated. An American English audio track is available as a second audio track.

CHAPTERS
00:00 Want peace? Prepare for war
00:35 Deterrence in its simplest form
01:11 An old Roman idea
01:52 The security dilemma
02:37 The Dreadnought race
03:09 Nuclear weapons and MAD
03:59 When it works, nothing happens
04:28 When deterrence fails
05:26 September 1983
05:59 A narrow line
06:18 The hotline
06:49 So, does it keep the peace?

IMAGE CREDITS
Stanislav Petrov, 2016 — Queery-54, CC BY-SA 4.0
via Wikimedia Commons
All other archive images are in the public domain.
Licences: creativecommons.org/licenses/by-sa/4.0
```

> **Blok se kopíruje CELÝ** (`docs/zverejneni.md`). Povinná atribuce je
> jediná: S37 Petrov (Queery-54, CC BY-SA 4.0). S10, S18, S31, S44 jsou
> public domain.
>
> Kapitoly jsou ze scén S01, S06, S09, S13, S18, S21, S27, S30, S36, S40,
> S42, S45 (`work/timing.json`, zaokrouhleno dolů). Nejkratší kapitola je
> 19 s (S40 → S42), poslední 44 s; všechny ≥ 10 s, první na 00:00. Výzva
> k odběru S12b leží v kapitole „An old Roman idea".
>
> Čísla: 2,9 bilionu = SIPRI 2025, 2 887 mld. (S03); 70 000 hlavic = FAS
> vrchol 1986 (S21); Franks Report Cmnd 8787 (S31–S32b). Popis ani kapitola
> neprozrazují, že poplach byl planý (S38) — rozuzlení zůstává videu.
> „Sixteen hundred years" = Vegetius (S10).

---

## 3. Náhled

✅ **WANT PEACE? / PREPARE FOR WAR?** — C3 kreslený kódem
(`thumbnail/c3-proti.svg` → `render/thumbnail.jpg`), vybral uživatel
2026-10-10, koncepty v `thumbnail/KONCEPTY.md`.

---

## 4. Titulky

`subtitles/*.srt`, 14 jazyků + `en-US`. Jazyk videa **`en-gb`** (hlas
`bf_emma`) se musí nastavit dřív, než se nahrají titulkové stopy. Titulky
a lokalizace se nahrávají až po zapracování nálezů Codexu — u titulků
**hotové** (2026-10-10, 12 jazyků, 63 oprav, `notes.md`).

---

## 5. Nastavení

| | |
|---|---|
| kategorie | **Science & Technology** (28) — posílá `nahraj.py` napevno |
| jazyk videa | `en-gb` |
| licence | standardní |
| pro děti | **ne** |
| komentáře | zapnuté |
| **byla použita AI** | **ne** (návrh, rozhoduje uživatel). Většina scén kreslená kódem, 5 archivních snímků jen barevně upravených (*color adjustment* je výslovná výjimka), S23 a S45 jsou malované ilustrace z ChatGPT (`art/PUVOD.md`) — nefotorealistické, anonymní bunkr a anonymní přístav, žádné konkrétní skutečné místo či událost. Hudba procedurální, hlas není klon |

### Závěrečná obrazovka

`zaver_check.py`: S48–S51 OK, prvky do horní poloviny. Závěrečná obrazovka
může být plných 20 s, **od 7:13**. Dlaždici i kolečko odběru do **horní
poloviny**, spodní rohy zabírá titulek.

---

## 6. Tagy

```
deterrence, si vis pacem para bellum, security dilemma, arms race,
mutually assured destruction, nuclear deterrence, Cold War, military spending,
SIPRI, Vegetius, HMS Dreadnought, Falklands War, Stanislav Petrov,
Moscow Washington hotline, history explained, war and peace,
science explainer, there's more to it
```

---

## 7. Playlist

Navrženo **`spolecnost`** (*How Society Actually Runs*): kdo rozhoduje
o válce a míru a proč státy zbrojí, patří k tématům o fungování
společnosti. Dopiš slug do `playlisty.json`, spusť `analytics.py --videa`
a pak `tools/playlisty.py`.
