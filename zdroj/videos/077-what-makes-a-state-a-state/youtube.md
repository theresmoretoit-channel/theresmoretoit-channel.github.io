# YouTube — 077 „What Makes a State a State?"

Stav: **HOTOVO** — zbytek titulků, playlist, závěrečnou obrazovku a americkou stopu naklikal uživatel ve Studiu a video naplánoval ke zveřejnění (2026-10-01).

| | |
|---|---|
| ID videa | `-Fg27tDnuXc` (https://www.youtube.com/watch?v=-Fg27tDnuXc) |
| nastavení, popis, tagy | ✅ 2026-10-01 `nahraj.py --k-videu=-Fg27tDnuXc --bez-titulku` |
| náhled | ✅ 2026-10-01 (týž běh) |
| lokalizace | ✅ 2026-10-01 13 jazyků jedním voláním |
| automatický přepis | ✅ 2026-10-01 čisté (`--smaz-asr`, nic k smazání); za pár dní zopakovat |
| titulky | ⏳ 2026-10-01 vloženo en, cs, sv, es, pt-BR, pak kvóta. **Zbývá:** `titulky.py $V --jen de,fr,it,pl,id,tr,uk,vi,fi,en-US` (4 000) a ověřit `captions.list` |
| playlist | ⏳ slug v `playlisty.json` za 020; zbývá `playlisty.py` (50) |
| závěrečná obrazovka, americká stopa | — |

**Co musí uživatel naklikat sám:** závěrečnou obrazovku (API na ni nemá zdroj)
a nahrát americkou audiostopu (`render/audio-en-US.m4a`). Prohlášení o AI
a osvědčení o zproštění vyřídí průvodce při ručním nahrání MP4.

Soubor k nahrání: `render/final-en-077.mp4`.

Pořadí podle CENY (`docs/zverejneni.md`):

```bash
V=videos/077-what-makes-a-state-a-state
python tools/nahraj.py $V --k-videu=-Fg27tDnuXc --bez-titulku   # 100
python tools/analytics.py --videa                         #   1  ← nutné
python tools/lokalizace.py $V                             #  50
python tools/titulky.py $V --smaz-asr                     # 150  ← před titulky
python tools/titulky.py $V                                # 400×15
python tools/playlisty.py                                 # 100
```

---

## 1. Titul

```
What Makes a State a State?
```

> wh-otázka („What…") — podle `docs/kanal-metriky.md` nejlepší CTR. Titul
> neprozrazuje odpověď (schopnost vymáhat pravidla na svém území).

---

## 2. Popis

```
Imagine the police in your neighbourhood stopped taking orders from the government. The laws, the courts and the parliament would all still exist. So who would actually be in charge?

A state has borders, a flag and a constitution. But the sociologist Max Weber pointed to something less visible: a claim to the legitimate use of force within a territory. This video follows that idea through what happens when a government can no longer enforce its own rules, through Lebanon and Hezbollah, often called "a state within a state", and through the Islamic State, which for a few years performed many of the functions of a state without ever being recognised as one.

And it ends with a paradox: the more successful a state is, the less we notice its monopoly on force.

The question of who has the final say over the states themselves is the subject of an earlier video: https://youtu.be/qCmRqFm-Vtk

Subtitles are written for this video, not auto-generated. An American English audio track is available as a second audio track.

Full transcript, sources and translations: https://theresmoretoit-channel.github.io/videos/what-makes-a-state-a-state/

CHAPTERS
00:00 Who is in charge?
00:31 Max Weber's answer
01:44 When rules can't be enforced
02:40 Other centres of power
03:18 Lebanon: a state within a state
04:18 The Islamic State
05:04 If the government disappeared
05:57 The paradox of a successful state
06:40 So what makes a state a state?
07:26 Back to the beginning

IMAGE CREDITS
Beirut skyline from O Monot hotel — Laura C Ellis, CC BY-SA 4.0, via Wikimedia Commons
Licences: creativecommons.org/licenses/by-sa/4.0
```

> **Blok se kopíruje CELÝ** (`docs/zverejneni.md`) — atribuce je UVNITŘ.
> Jediný archivní snímek (S24) je CC BY-SA, tedy povinný; jiné archivní
> snímky video nemá, proto chybí řádek o public domain. SDXL scény
> (S38, S40, S48) atribuci nepotřebují.
>
> Kapitoly jsou ze scén S01, S04, S12, S19, S24, S30, S37, S46, S52, S58
> (`work/timing.json`, celkem 483,8 s). Všechny ≥ 10 s. **Po každém dalším
> běhu `tts.py` časy přepočítej** — a stejně tak v `youtube-preklady.md`.
>
> Odkaz na 020 „Who Runs the Earth?" (`https://youtu.be/qCmRqFm-Vtk`,
> z `Témata.ods`) — video na něj v S62 odkazuje slovy „You'll find it right here".
>
> Popis drží míru jistoty scénáře: Hizballáh „often called" (S27 „described
> as"), ISIS „performed many of the functions" (S35), neuznaný (S34).

---

## 3. Náhled

`render/thumbnail.jpg`: **hotový**, koncept C1 (ošuntělá vlajka bez znaku,
„STATE / WHAT MAKES ONE?", ChatGPT, dodal uživatel 2026-10-01). Původ
v `thumbnail/PUVOD.md`; `thumb_check.py`: jas 71,6, kontrast 90,3, uvnitř
pásma kanálu.

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
| **byla použita AI** | **ne** — 65 scén kreslených kódem, 3 SDXL scény jako malované ilustrace, archivní snímek Bejrútu jen barevně upravený, hudba procedurální, hlas není klon skutečné osoby |

### Závěrečná obrazovka

S59–S62 mají **horní polovinu volnou** — dlaždici i kolečko odběru dej
do **horní** poloviny. **Dlaždice MUSÍ být 020** („Who Runs the Earth?"),
protože S62 říká „You'll find it right here".

---

## 6. Tagy

```
what makes a state a state, what is a state, max weber, monopoly on violence,
monopoly of force, state within a state, hezbollah, lebanon, islamic state,
failed state, sovereignty, political science explained, explainer,
there's more to it
```

---

## 7. Playlist

Playlist `spolecnost` („How Society Actually Runs"). Dopiš slug do
`playlisty.json` hned za `020-who-runs-the-earth`, spusť `analytics.py --videa`
a pak `tools/playlisty.py`.
