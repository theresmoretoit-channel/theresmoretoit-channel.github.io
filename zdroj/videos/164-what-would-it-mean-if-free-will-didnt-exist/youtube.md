# YouTube — 164 „What Would It Mean If Free Will Didn't Exist?“

Stav: **nahráno 2026-11-22** (https://youtu.be/54GN11u2RHA). Master `render/final-en-164.mp4`
(9:42, 1080p), náhled `render/thumbnail.jpg` a americká stopa `render/audio-en-US.m4a` jsou hotové.
Překlady prošly Codexem (commit 59034dff), titulky 15 stop jsou v `subtitles/`.

| | |
|---|---|
| ID videa | `54GN11u2RHA` (MP4 ručně 2026-11-22; nastavení, náhled, 13 lokalizací, 15 stop titulků přes API) |
| master | `render/final-en-164.mp4` — 9:42, 1080p, 207, 2026-11-22 |
| náhled | `render/thumbnail.jpg` — ChatGPT podle konceptu C3, `FREE WILL` / `WHAT CHANGES?` (`thumbnail/PUVOD.md`) |
| nastavení, popis, tagy | podklady níž |
| lokalizace | `youtube-preklady.md`, 13 jazyků |
| titulky | `subtitles/<kód>.srt`, 14 jazyků + `en-US`; Codex na všech 13 překladech |
| americká stopa | `render/audio-en-US.m4a` (`af_heart`), ručně ve Studiu |
| závěrečná obrazovka | S60–S61, **horní polovina** (viz níž) |
| karty | **žádné** (storyboard nemá klíč `karta`, scénář na jiné video neodkazuje) |
| playlist | návrh `lide` (viz níž) |

**Co musí uživatel naklikat sám:** závěrečnou obrazovku, americkou audiostopu
(`render/audio-en-US.m4a`) a osvědčení o zproštění, pokud ho nevyřídil průvodce nahráním.

Stopáž 9:42 (`work/timing.json` total 582,55 s, stav po S39b, script 0.5).

> Kdyby se znovu pouštěl `tts.py`, přepočítej kapitoly tady i v `youtube-preklady.md`
> a přegeneruj `en-US` přes `us_stopa.py`.

Pořadí podle CENY (`docs/zverejneni.md`):

```bash
V=videos/164-what-would-it-mean-if-free-will-didnt-exist
python tools/odkaz_web.py --repo --jen 164                # řádek s odkazem na web (už puštěno)
python tools/nahraj.py $V --k-videu=<ID> --bez-titulku   # 100
python tools/analytics.py --videa                        #   1  ← nutné
python tools/lokalizace.py $V                            #  50
python tools/titulky.py $V --smaz-asr                    # 150  ← před titulky
python tools/titulky.py $V                               # 400×N
python tools/playlisty.py                                #  50
# úklid, až je MP4 na YouTube:
rm $V/render/draft*.mp4
ssh vrana@192.168.0.207 'rm -rf /home/vrana/temp/render-164-what-would-it-mean-if-free-will-didnt-exist'
```

---

## 1. Titul

```
What Would It Mean If Free Will Didn't Exist?
```

> Wh-otázka, 45 znaků, shodná s `project.json`. Záměrně ne ano/ne „Do We Have Free Will?“
> (název z `Témata.fods`) — ano/ne otázka má na kanálu nejhorší CTR (`CLAUDE.md`, „Trychtýř").
> Titul navíc nic netvrdí: video neříká, že svobodná vůle neexistuje (S40).

---

## 2. Popis

```
In 2000, a 40-year-old teacher in Virginia suddenly developed urges he had never had before, and began acting on them. He was convicted. He told doctors he knew it was wrong, he just couldn't stop himself. Then a brain scan found a tumour the size of an egg. When surgeons removed it, the urges went away. When it grew back, so did they. Most people would say he wasn't really responsible. But what if every choice you make is shaped by things you never chose, and his case only looks special because we can see the cause on a scan?

This video doesn't ask whether we have free will. It asks what would actually change if we didn't. It looks at Benjamin Libet's famous experiment, where brain activity seemed to start before people felt the urge to move, and at a 2008 study that predicted a choice seconds before people were aware of making it, and why both are less dramatic than they first looked. Then it turns to the harder problem that never depended on those experiments, and asks what it would mean for punishment, guilt, achievement and regret, and whether people really behave worse once they stop believing in free will.

Sources: Burns & Swerdlow, Archives of Neurology (2003); Libet, Gleason, Wright & Pearl, Brain (1983); Soon, Brass, Heinze & Haynes, Nature Neuroscience (2008); Schurger, Sitt & Dehaene, PNAS (2012); Vohs & Schooler, Psychological Science (2008); Open Science Collaboration, Reproducibility Project: Psychology, Science (2015); Buttrick et al., Many Labs 5, Advances in Methods and Practices in Psychological Science (2020); Nadelhoffer et al., Cognition (2020); Genschow et al., Personality and Social Psychology Review (2023).

Subtitles are written for this video, not auto-generated. An American English audio track is available as a second audio track.

Full transcript, sources and translations: https://theresmoretoit-channel.github.io/videos/what-would-it-mean-if-free-will-didnt-exist/

CHAPTERS
00:00 A teacher and a tumour
01:06 Was he responsible?
01:57 Libet's experiment
02:40 Predicting a choice in advance
03:01 A closer look
03:45 The real problem
04:23 Cause or chance?
04:54 What philosophers say
05:40 Punishment
06:51 Guilt
07:06 Achievement
07:36 Regret
07:51 Would people behave worse?
08:32 What would we lose?
09:05 How we see other people
```

> **Blok se kopíruje CELÝ** (`docs/zverejneni.md`). **Žádné `IMAGE CREDITS`:** video nemá
> jediný archivní snímek (`storyboard.json`: 66× `svg`, 3× `sdxl`, 0× `archive`; žádné
> `sources.json` ani `CREDITS.md`), takže atribuční povinnost nevzniká. Ilustrace S29
> z ChatGPT (`art/PUVOD.md`) atribuci nepotřebuje.
>
> **Citlivé místo:** popis záměrně neopakuje *„sexual urges towards children"* ze S02, jen
> *„urges he had never had before"* + *„convicted"*. Je to věcně přesné (nová byla právě
> přitažlivost k dětem, viz `factcheck.md` S02) a popis je text, který YouTube čte při
> posuzování vhodnosti pro inzerenty; ve videu samotném zůstává zdrženlivá formulace scénáře.
> V řádku zdrojů je proto i jen časopis, ne název článku Burns & Swerdlow (obsahuje *pedophilia*).
>
> **Pointa se neprozrazuje:** popis neříká, že kauzální past platí tak jako tak (S29–S37),
> ani výsledek replikace pokusu s podváděním (S54–S55) — jen se ptá. Že Libet a Soon jsou
> „less dramatic than they first looked", je obsah S24–S28 a láká, ne vyzrazuje závěr videa.
>
> Kapitoly ze scén S01, S09, S16, S22, S24, S29, S34, S38, S41, S46, S48, S49, S51, S56, S58
> (`work/timing.json`, zaokrouhleno dolů). První na 00:00, všechny ≥ 10 s (nejkratší
> S46 → S48 a S49 → S51, 15 s; poslední S58 → konec 37 s). S15 (*„a stranger question"*)
> vlastní kapitolu nemá, protože S15 → S16 je jen 9 s; S40 (*„suppose it is"*) totéž
> (S40 → S41 9,5 s), patří do kapitoly 04:54. Otázka do komentářů (S61) kapitolu nemá.
>
> **Zdroje:** primární z `factcheck.md` (PhilPapers Survey tam je jen „pro komentáře", ve videu
> není, takže v popisu ne). Řádek s odkazem na web doplní `tools/odkaz_web.py`.

---

## 3. Náhled

`render/thumbnail.jpg` (1280×720, 0,26 MB): vypínač přepnutý dolů, `FREE WILL` / `WHAT CHANGES?`. Nakreslil ChatGPT
podle konceptu C3 (kódem kreslené koncepty `thumbnail/c1-provazky`, `c2-rozcesti`, `c3-vypinac`); původ v `thumbnail/PUVOD.md`.
Princip a zadání: `docs/thumbnail-styl.md`. Náhled nesmí vyzradit odpověď (titul je otázka).
`nahraj.py --k-videu` jde pustit i bez náhledu (`thumbnails.set` se pak dopustí zvlášť).

---

## 4. Titulky

`subtitles/<kód>.srt` pro 14 jazyků a `en-US`.
Jazyk videa **`en-gb`** (hlas `bf_emma`) nastaví `nahraj.py` dřív, než se nahrají titulkové stopy.

---

## 5. Nastavení

| | |
|---|---|
| kategorie | **Science & Technology** (28), posílá `nahraj.py` napevno |
| jazyk videa | `en-gb` |
| licence | standardní |
| pro děti | **ne** |
| komentáře | zapnuté (S61 je otázka do komentářů: *„who would you judge differently?"*) |
| **byla použita AI** | **ne**. 65 z 69 scén je kreslených kódem. S16 (prázdná laboratoř s osciloskopem), S40 (postava na rozcestí v mlze) a S56 (postava nad údolím) jsou malované ilustrace z SDXL (kotva *painterly editorial illustration*), obecné scény, ne skutečné místo, osoba ani událost. S29 je plochá ilustrace padajícího domina od ChatGPT (`art/PUVOD.md`), stylizovaná, ne fotorealistická. Žádný archivní snímek. Hlas je syntetický Kokoro `bf_emma`, ne klon skutečné osoby; hudba je procedurální. Případ učitele (S01–S08) ukazuje jen schematický profil hlavy, osu příběhu a nádor, žádné zobrazení skutečné osoby. |

### Karty

Žádné. Scénář na jiné video kanálu neodkazuje a `storyboard.json` nemá klíč `karta`.

### Závěrečná obrazovka

Od **9:42 − 20 s ≈ 9:22** (začátek S60 je 9:21, S61 9:30). `zaver_check` hlásí S60–S61 OK,
spodní rohy jsou pod titulky. **Dlaždici i odběr dej do HORNÍ poloviny.**
Jako dlaždici navrhuju **022 *Can AI Have Consciousness?*** (související video podle
`notes.md`), druhou nechat na „nejlepší pro diváka“.

---

## 6. Tagy

```
free will, determinism, neuroscience, philosophy, benjamin libet, libet experiment,
readiness potential, consciousness, moral responsibility, compatibilism, punishment,
criminal justice, brain tumour, decision making, psychology, replication crisis,
philosophy of mind, there's more to it
```

---

## 7. Playlist

Návrh **`lide`** (*Why We Do What We Do*, Psychology & Human Behavior; je v něm 034
*Dunning-Kruger* i 163). Alternativa `mysli` (*Other Minds — Aliens, Telepathy and Machines*,
je v něm 022), ta je ale laděná na mimozemšťany a stroje. Rozhodne uživatel; pak dopsat slug
do `playlisty.json`, `analytics.py --videa`, `playlisty.py --jen <klíč>`.
