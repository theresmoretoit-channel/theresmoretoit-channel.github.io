# YouTube — 069 „What Does Zero Gravity Actually Feel Like?"

Stav: **NAHRÁNO** (2026-09-28), ID `Zo2R8_3bbXU`. Metadata, náhled a
lokalizace přes API; zbylé titulky, americkou stopu a závěrečnou obrazovku
doklikal uživatel ručně ve Studiu. Stav zveřejnění se vede v `Témata.ods`.

| | |
|---|---|
| video | `render/final-en-069.mp4` (master, 13:20,6) |
| náhled | `render/thumbnail.jpg` — ✅ koncept C3 (fotka NASA) |
| titulky | `subtitles/*.srt`, 14 jazyků + `en-US` — ✅ všechny prošly Codexem, nálezy zapracované |
| americká stopa | `render/audio-en-US.m4a` — nahrát ve Studiu |
| lokalizace | `youtube-preklady.md` — ✅ 13 jazyků, prošlo Codexem |

**Co musí uživatel naklikat sám:** nahrát MP4 ve Studiu (průvodce vyřídí
prohlášení o AI a osvědčení o zproštění), americkou audiostopu
a závěrečnou obrazovku (API na ni nemá zdroj).

Pořadí podle CENY (`docs/zverejneni.md`):

```bash
V=videos/069-what-does-zero-gravity-actually-feel-like
python tools/nahraj.py $V --k-videu <ID> --bez-titulku   # 100
python tools/analytics.py --videa                        #   1  ← nutné
python tools/lokalizace.py $V                            #  50
python tools/titulky.py $V --smaz-asr                    # 150  ← před titulky
python tools/titulky.py $V                               # 400×15
python tools/playlisty.py                                # 100
```

---

## 1. Titul

```
What Does Zero Gravity Actually Feel Like?
```

> wh-otázka („What…") — podle `docs/kanal-metriky.md` nejlepší CTR
> (2,23 % proti 1,21 % u ano/ne otázky). Titul je zároveň název projektu.

---

## 2. Popis

```
Imagine lying on the floor of an airplane and suddenly weighing almost
twice as much. Twenty seconds later, you're floating. This is how people
experience weightlessness without ever leaving Earth — on board a
parabolic flight.

What does it actually feel like? Why can it make you sick? Why does it
last only about twenty seconds, when gravity isn't going anywhere? And is
it really "zero gravity" at all?

We follow one parabola from start to finish — the pull-up at 1.8 g, the
free fall, the way the floor slowly comes back — and look at the aircraft,
the pilots who fly it, and the people who use these flights, from
scientists and astronauts to film crews and anyone who buys a seat.

Subtitles are written for this video, not auto-generated. An American
English audio track is available as a second audio track.

CHAPTERS
00:00 Floating inside an airplane
00:47 How do you make someone weightless?
01:10 Parabolic flight
01:35 The phases of a parabola
02:37 What 1.8 g feels like
03:20 Free fall
04:00 Why it can make you sick
06:01 Why only twenty seconds?
06:59 What if they didn't pull out?
08:09 The whole arc
08:57 Zero to 1.8 g, gradually
09:54 Again and again
10:37 The Moon and Mars
11:41 Is it really zero gravity?
12:21 Things fall down

IMAGE CREDITS
Airbus A310 - F-WNOV AirZeroG at LFBT airport — Hugo LUC, CC BY-SA 4.0
Airbus A-300 ZERO-G — Neuwieser, CC BY-SA 2.0
Boeing KC-135A Stratotanker 'N930NA' — Alan Wilson, CC BY-SA 2.0
via Wikimedia Commons
Licences: creativecommons.org/licenses/by-sa/4.0 · creativecommons.org/licenses/by-sa/2.0

All other archive images are courtesy of NASA and are in the public domain.
```

> **Blok se kopíruje CELÝ** (`docs/zverejneni.md`). Povinné atribuce jsou
> UVNITŘ: S13 (A310, CC BY-SA 4.0), S13b (A300, CC BY-SA 2.0) a S41b
> (KC-135A, CC BY-SA 2.0). Snímky NASA (S06, S23, S27, S80) jsou volné
> dílo; podmínky NASA žádají uvést NASA jako zdroj, proto věta „courtesy
> of NASA".
>
> Kapitoly: první na 00:00, každá ≥ 10 s, časy z `work/timing.json`
> (začátky scén S01, S09, S12, S14, S19, S23, S28, S42, S48, S55, S61,
> S68, S75, S81, S86).

---

## 3. Náhled

`render/thumbnail.jpg` — **vybrán koncept C3** (uživatel 2026-09-28):
fotka NASA s84-37522 (člověk ve vznosu v kabině KC-135, volné dílo),
nahoře **ZERO G**, dole **HOW DOES IT FEEL?**. Pozadí `thumbnail/bg-c3.jpg`,
vrstva `thumbnail/c3-foto.svg`, volba zapsaná v `project.json`.
`thumb_check.py`: jas 125,9 (68/69, skoro nejjasnější v kanálu), 0,27 MB,
1280×720.

---

## 4. Titulky

`subtitles/*.srt`, 14 jazyků + `en-US`. Jazyk videa **`en-gb`** (hlas
`bf_emma`) se musí nastavit dřív, než se nahrají titulkové stopy.

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

Rozhoduje fotorealističnost. Video **nemá žádnou SDXL scénu**: 90 scén je
kresleno kódem, 7 jsou barevně upravené archivní fotografie (výjimka
„color adjustment"), hudba je procedurální. Žádný fotorealistický
generovaný obsah ani klonovaný hlas.

### Závěrečná obrazovka

`zaver_check.py` hlásí volné místo nahoře ve všech scénách ocasu
(S91–S93). Dlaždici i kolečko dej do **horní** poloviny, dole je titulek.

---

## 6. Tagy

```
zero gravity, weightlessness, parabolic flight, vomit comet, microgravity,
free fall, airbus zero g, zero g flight, astronaut training, g-force,
how does zero gravity work, physics, space, explainer, there's more to it
```

---

## 7. Playlist

Dopiš slug do `playlisty.json` (vesmír / fyzika), spusť
`analytics.py --videa` a pak `tools/playlisty.py`.
