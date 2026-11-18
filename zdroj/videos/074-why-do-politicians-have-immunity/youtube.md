# YouTube — 074 „Why Do Politicians Have Immunity?"

Stav: **NAHRÁNO VČETNĚ METADAT A LOKALIZACÍ; TITULKY 7 z 15** (došla kvóta); zbývá ruční část ve Studiu.

| | |
|---|---|
| ID videa | `sfxGpbJriUw` (https://www.youtube.com/watch?v=sfxGpbJriUw) |
| nastavení, popis, tagy, náhled | ✅ 2026-09-30 `nahraj.py --k-videu sfxGpbJriUw --bez-titulku` |
| lokalizace | ✅ 2026-09-30 13 jazyků jedním voláním (`lokalizace.py`) |
| titulky | ⚠️ 2026-09-30 podle logu vloženo en, cs, sv, es, pt-BR, de, fr; na `it` došla kvóta. **zbytek nahrává uživatel ručně ve Studiu** |
| automatický přepis | ⬜ zatím nevznikl (smazáno 0); za pár dní znovu `titulky.py $V --smaz-asr` |
| playlist | ⬜ `spolecnost` — nastaví uživatel ručně (slug je i v `playlisty.json`) |
| závěrečná obrazovka, americká stopa | ⬜ uživatel ve Studiu |

**Co musí uživatel naklikat sám:** závěrečnou obrazovku (API na ni nemá zdroj)
a nahrát americkou audiostopu (`render/audio-en-US.m4a`). Prohlášení o AI
a osvědčení o zproštění vyřídí průvodce při ručním nahrání MP4.

Soubor k nahrání: `render/final-en-074.mp4`.

Pořadí podle CENY (`docs/zverejneni.md`):

```bash
V=videos/074-why-do-politicians-have-immunity
python tools/nahraj.py $V --k-videu sfxGpbJriUw --bez-titulku   # 100
python tools/analytics.py --videa                         #   1  ← nutné
python tools/lokalizace.py $V                             #  50
python tools/titulky.py $V --smaz-asr                     # 150  ← před titulky
python tools/titulky.py $V                                # 400×15
python tools/playlisty.py                                 # 100
```

---

## 1. Titul

```
Why Do Politicians Have Immunity?
```

> wh-otázka („Why…") — podle `docs/kanal-metriky.md` nejlepší CTR. Náhled
> „IMMUNITY / WHO IS IT FOR?" se ptá, odpověď neprozrazuje.

---

## 2. Popis

```
In January 1642, King Charles the First walked into the House of Commons
to arrest five members of Parliament. They were gone. The Speaker knelt
and refused to tell him where they were.

That day shows why parliaments need protection from those in power. But
how do you protect politicians from persecution without putting them
above the law?

This video separates two very different kinds of immunity: protection for
how politicians vote and what they say in parliament, and protection for
the politician personally, even from charges that have nothing to do with
the job. It follows the wording from the English Bill of Rights of 1689 to
the US Constitution, compares the United States, Britain and the Czech
Republic, and looks at one case that ended up before two parliaments: the
Stork's Nest case of Andrej Babiš and Jana Nagyová.

Babiš denies any wrongdoing. The Czech parliament's vote in 2026 was not a
verdict; it paused the case for the rest of his term.

Subtitles are written for this video, not auto-generated. An American
English audio track is available as a second audio track.

Full transcript, sources and translations: https://theresmoretoit-channel.github.io/videos/why-do-politicians-have-immunity/

CHAPTERS
00:00 January 1642
01:00 Why parliaments need protection
01:33 The Bill of Rights
01:51 Voting without fear
02:35 Two very different immunities
03:11 The United States
03:51 Britain and Europe
04:09 The Czech Republic
05:01 Andrej Babiš and the Stork's Nest case
06:12 A vote, not a verdict
06:37 Same case, two parliaments
07:32 So why do politicians have immunity?

IMAGE CREDITS
Čapí hnízdo, Olbramovice — Richenza, CC BY-SA 3.0, via Wikimedia Commons
Andrej Babiš (2025) — Vox España, CC0, via Wikimedia Commons
All other archive images are in the public domain.
Licences: creativecommons.org/licenses/by-sa/3.0
```

> **Blok se kopíruje CELÝ** (`docs/zverejneni.md`) — atribuce jsou UVNITŘ.
> Povinná je jen S41 (Richenza, CC BY-SA 3.0); S40 je CC0, uvádí se
> z korektnosti. S04 (Copley), S13 (Fairburn 1799) a S27 (NARA) jsou volné dílo.
>
> Kapitoly jsou ze scén S01, S09, S13, S16, S22, S27, S32, S34, S40, S47,
> S50, S57 (`work/timing.json`). Všechny ≥ 10 s.
>
> **Popis netvrdí vinu.** Obžaloba ani rozsudek nad Nagyovou v něm nejsou,
> je tam Babišovo popření a to, že hlasování nebylo rozsudkem, tedy stejná
> míra jistoty jako ve scénáři.

---

## 3. Náhled

`render/thumbnail.jpg`: **hotový**, koncept K1 (rozevřená pouta se zlatým
štítem na červené lavici, „IMMUNITY / WHO IS IT FOR?", ChatGPT, přijal
uživatel 2026-09-30). Původ v `thumbnail/PUVOD.md`; `thumb_check.py`: jas
75,6, kontrast 88,1, uvnitř pásma kanálu.

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

### Prohlášení o AI: **ne**

Rozhoduje fotorealističnost, ne použití AI. Video nemá žádnou SDXL scénu:
60 scén je kreslených kódem, 5 jsou barevně upravené archivní snímky (výjimka
„color adjustment"). Prázdná sněmovna v S57 je plochá ilustrace z ChatGPT
(`art/PUVOD.md`); první, fotorealistická verze byla zamítnuta. Hudba je
procedurální, hlas není klon skutečné osoby.

### Závěrečná obrazovka

S64–S67 mají **horní polovinu volnou** (kresba jen dole) — dlaždici dalšího
videa i kolečko odběru dej do **horní** poloviny (`zaver_check.py` ověřeno).

---

## 6. Tagy

```
why do politicians have immunity, parliamentary immunity, immunity from
prosecution, bill of rights 1689, speech or debate clause, charles i five
members, rule of law, separation of powers, czech republic, andrej babis,
storks nest case, european parliament, politics explained, explainer,
there's more to it
```

---

## 7. Playlist

Playlist `spolecnost` (spolu s 020, 050 a 063). Dopiš slug do
`playlisty.json`, spusť `analytics.py --videa` a pak `tools/playlisty.py`.
