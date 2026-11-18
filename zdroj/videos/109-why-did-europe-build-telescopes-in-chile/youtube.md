# YouTube — 109 „Why Is Europe Building Telescopes in Chile?“

Stav: **nahráno 2026-10-15** (https://www.youtube.com/watch?v=DRVl3lsm0-I). Metadata, 13 lokalizací, 15 titulkových stop a playlist přes API; náhledy (A/B test), americkou stopu a závěrečnou obrazovku dělá uživatel ve Studiu. Stav zveřejnění je v `Témata.ods`.

| | |
|---|---|
| ID videa | `DRVl3lsm0-I` |
| master | ✅ `render/final-en-109.mp4` (9:24, 1920×1080, 107 MB, render 2026-10-15 na .207, `ffmpeg -v error` čistý) |
| náhled | ✅ A/B test ve Studiu: `render/thumbnail.jpg` (B, glóbus, hlavní) + `render/thumbnail-b.jpg` (A, kopule) — `thumbnail/PUVOD.md` |
| nastavení, popis, tagy | podklady níž |
| lokalizace | ✅ `youtube-preklady.md`, 13 jazyků, nahráno |
| titulky | ✅ `subtitles/*.srt`, 14 jazyků + `en-US`, všechny prošly Codexem (`codex-zapracovano.md`), nahráno |
| americká stopa | ✅ `render/audio-en-US.m4a` — nahrává uživatel ve Studiu |
| závěrečná obrazovka | ručně ve Studiu |
| playlist | ✅ `vesmir` |

**Co musí uživatel naklikat sám:** nahrát MP4 ve Studiu (průvodce vyřídí
prohlášení o AI a osvědčení o zproštění), závěrečnou obrazovku a americkou
audiostopu (`render/audio-en-US.m4a`).

Stopáž 9:24 (`work/timing.json` total 563,7 s).

> Kdyby se znovu pouštěl `tts.py`, přepočítej kapitoly tady
> i v `youtube-preklady.md` a přegeneruj `en-US` přes `us_stopa.py`.

Pořadí podle CENY (`docs/zverejneni.md`):

```bash
V=videos/109-why-did-europe-build-telescopes-in-chile
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
Why Is Europe Building Telescopes in Chile?
```

> Wh-otázka, 43 znaků. Rozhodl uživatel (v0.7); průběhový čas sedí na S01
> (*Europe is building*) a na ELT, který se staví. Slug zůstává pracovní.

---

## 2. Popis

```
In a desert in northern Chile, Europe is building the largest optical telescope ever made, with a main mirror thirty-nine metres across. It won't be alone: some of the world's most powerful telescopes already stand there, more than ten thousand kilometres from the countries that paid for them.

Part of the answer is the air. Twinkling stars look lovely, but for an astronomer the atmosphere is the hardest part of the job, and the Atacama Desert has some of the driest, steadiest skies on Earth. But that only explains the desert. It doesn't explain one word in the name of the organisation behind it all: the European Southern Observatory. From a black hole at the centre of our galaxy to a planet around the nearest star, and from ALMA's sixty-six antennas to the Extremely Large Telescope and NASA's new Roman Space Telescope: why Europe looks at the sky from the other side of the world, and why telescopes in space haven't made that pointless.

Sources: ESO, ELT construction timeline (ann25001) and member states; GRAVITY Collaboration, A&A 615 (2018); S. Gillessen et al., ApJ 837 (2017); G. Anglada-Escudé et al., Nature 536 (2016); A. Suárez Mascareño et al., A&A 639 (2020); ALMA (ESO/NAOJ/NRAO), HL Tauri (2014); NASA, Nancy Grace Roman Space Telescope.

Subtitles are written for this video, not auto-generated. An American English audio track is available as a second audio track.

Full transcript, sources and translations: https://theresmoretoit-channel.github.io/videos/why-did-europe-build-telescopes-in-chile/

CHAPTERS
00:00 The largest telescope ever made
00:34 The problem is the air
01:27 The Atacama Desert
02:03 Why "Southern"?
03:45 Why Europe, together?
04:31 Measuring a star's wobble
05:42 ALMA and the cold universe
06:21 Why build an even bigger one?
07:14 Why not just go to space?
08:09 Roman joins the team
08:49 Back in the desert

IMAGE CREDITS
Atacama Desert landscape — L. Honnorat/ESO, CC BY 4.0
Roque de los Muchachos Observatory, La Palma — H. Zell, CC BY-SA 3.0
La Silla aerial view — ESO/C.Madsen, CC BY 4.0
Paranal and the Pacific at sunset — ESO/G. Hüdepohl (atacamaphoto.com), CC BY 4.0
ALMA antennas on the Chajnantor plateau — ALMA (ESO/NAOJ/NRAO)/W. Garnier (ALMA), CC BY 4.0
HL Tau protoplanetary disk — ALMA (ESO/NAOJ/NRAO), CC BY 4.0
ELT dome, 2025 — ESO/G. Vecchia, CC BY 4.0
via Wikimedia Commons
Licences: creativecommons.org/licenses/by/4.0, creativecommons.org/licenses/by-sa/3.0
Hubble and the Roman launch: NASA, public domain.
```

> **Blok se kopíruje CELÝ** (`docs/zverejneni.md`). Atribuce všech sedmi
> CC BY / CC BY-SA snímků je uvnitř (ověřeno proti `sources.json`, viz níž);
> S50 a S55 jsou NASA, public domain. S31 (`art/S31.png`) je ilustrace
> z ChatGPT/SDXL, atribuci nepotřebuje.
>
> **Pointa se neprozrazuje.** Popis řekne, že vysvětlení pouští stačí na
> poušť, ale ne na slovo *Southern* — co znamená (jižní obloha), nechá na
> videu. Kapitola 02:03 je proto otázka.
>
> Kapitoly ze scén S01, S05, S11, S14, S26, S31, S40, S44, S50, S55, S59
> (`work/timing.json`, zaokrouhleno dolů). Nejkratší 34 s (S01 → S05),
> všechny ≥ 10 s, první na 00:00. Výzva k odběru S13b (1:55) leží
> v kapitole „The Atacama Desert“.
>
> Zdroje podle `factcheck.md`, „Zdroje“. Čísla v popisu (39 m, 10 000 km,
> 66 antén) jsou tatáž jako ve scénáři.

---

## 3. Náhled

✅ `render/thumbnail.jpg` — 10,000 KM / WHY THERE? (glóbus, oblouk ze
střední Evropy ke kopuli v severním Chile). Hotový obrázek od uživatele
(ChatGPT, zadání B), jen zmenšený; původ, otisk a zamítnuté varianty A a C
v `thumbnail/PUVOD.md`.

---

## 4. Titulky

`subtitles/*.srt`, 14 jazyků + `en-US`. Jazyk videa **`en-gb`** (hlas
`bf_emma`) se musí nastavit dřív, než se nahrají titulkové stopy.
Nahrávají se až po zapracování nálezů Codexu.

---

## 5. Nastavení

| | |
|---|---|
| kategorie | **Science & Technology** (28) — posílá `nahraj.py` napevno |
| jazyk videa | `en-gb` |
| licence | standardní |
| pro děti | **ne** |
| komentáře | zapnuté |
| **byla použita AI** | **ne** (návrh, rozhoduje uživatel). 52 scén je kreslených kódem, devět archivních snímků (ESO, ALMA, NASA, H. Zell) je jen barevně upravených (*color adjustment* je výslovná výjimka). **Dvě scény jsou malované ilustrace** — S31 (kopule pod Mléčnou dráhou, SDXL upravené v ChatGPT, `art/PUVOD.md`) a S59 (SDXL) — s generickými kopulemi, žádné konkrétní skutečné místo ani událost. Hudba je procedurální, hlas není klon. |

### Závěrečná obrazovka

Od **9:04** (posledních 20 s), tedy S61–S63. `zaver_check.py`: S61–S63 OK,
prvky patří do **horní poloviny** (spodní polovinu zabírá kresba
a titulek).

---

## 6. Tagy

```
european southern observatory, eso, extremely large telescope, elt,
very large telescope, vlt, alma, atacama desert, chile, paranal,
la silla, southern sky, espresso, proxima b, exoplanets,
james webb, roman space telescope, astronomy, telescopes,
science explainer, there's more to it
```

---

## 7. Playlist

`vesmir` (*Space — Getting There, and Who Else Is Out There*), na konec.
Video se ptá, kam se dívat a odkud, takže sedí k 035 (Proxima — tatáž
hvězda jako S35–S38) i k 029/032.
