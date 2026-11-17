# YouTube — 146 „What Can a Hypnotist Actually Make You Do?“

Stav: **MP4 nahrané ručně 2026-11-07**; metadata, lokalizace (13 jazyků, po Codexu), 15 titulků (ASR smazán), playlist a náhled přes API týž den.
Plán zveřejnění, americká stopa a závěrečná obrazovka naklikané ve Studiu 2026-11-07. Stav zveřejnění je v `Témata.fods`.

| | |
|---|---|
| ID videa | `a4j9XH0tPmM` — https://www.youtube.com/watch?v=a4j9XH0tPmM |
| master | `render/final-en-146.mp4` (herní PC přes wifi, 739,3 s) |
| náhled | ✅ C2 `HYPNOSIS / WHO WOULD REACH IN?`, `render/thumbnail.jpg`, nahráno (`thumbnail/PUVOD.md`) |
| nastavení, popis, tagy | podklady níž |
| lokalizace | `youtube-preklady.md`, 13 jazyků, Codex zapracován, nahráno |
| titulky | `subtitles/*.srt`, 14 jazyků + `en-US`, Codex zapracován, nahráno |
| americká stopa | `render/audio-en-US.m4a`, ručně ve Studiu |
| závěrečná obrazovka | S74–S75, **horní polovina** (viz níž) |
| karty | žádné |
| playlist | `lide` (*Why We Do What We Do*), za 135, zařazeno |

**Co musí uživatel naklikat sám:** závěrečnou obrazovku, americkou audiostopu
(`render/audio-en-US.m4a`) a osvědčení o zproštění, pokud ho nevyřídil průvodce nahráním.

Stopáž 12:19 (`work/timing.json` total 739,255 s).

> Kdyby se znovu pouštěl `tts.py`, přepočítej kapitoly tady i v `youtube-preklady.md`
> a přegeneruj `en-US` přes `us_stopa.py`.

Pořadí podle CENY (`docs/zverejneni.md`):

```bash
V=videos/146-what-can-a-hypnotist-actually-make-you-do
python tools/nahraj.py $V --k-videu=a4j9XH0tPmM --bez-titulku   # 100
python tools/analytics.py --videa                        #   1  ← nutné
python tools/lokalizace.py $V                            #  50
python tools/titulky.py $V --smaz-asr                    # 150  ← před titulky
python tools/titulky.py $V                               # 400×15
python tools/playlisty.py                                #  50
# úklid, až je MP4 na YouTube:
rm $V/render/draft*.mp4
ssh vrana@192.168.0.207 'rm -rf /home/vrana/temp/render-146-what-can-a-hypnotist-actually-make-you-do'
```

---

## 1. Titul

```
What Can a Hypnotist Actually Make You Do?
```

> Wh-otázka, 42 znaků, shodná s `project.json`. Odpověď (S28, S74) titul neprozrazuje.

---

## 2. Popis

```
A researcher tells you that the number six no longer exists. Asked to count to ten, some people simply skipped it. That was real research. So what can a hypnotist actually make you do?

Films say a hypnotist can send you out to kill, wipe a memory or plant a command for later. All of that has been tested in a lab, and the best experiments added people who were told to fake hypnosis. This video goes through a rattlesnake behind glass, a beaker of real nitric acid, a secretary in a waiting room, a test where reading stops, a bus driver in Chowchilla and a night that never happened. And it ends where hypnosis clearly does help.

Sources: Orne & Evans 1965, Journal of Personality and Social Psychology; Orne, Sheehan & Evans 1968, Journal of Personality and Social Psychology; Evans & Orne 1971, International Journal of Clinical and Experimental Hypnosis; Laurence & Perry 1983, Science; AMA Council on Scientific Affairs 1985, JAMA; Raz et al. 2002, Archives of General Psychiatry; Raz, Fan & Posner 2005, PNAS; Raz et al. 2006, Psychological Science; Montgomery et al. 2007, Journal of the National Cancer Institute; Kihlstrom 2008, The Oxford Handbook of Hypnosis; Terhune et al. 2017, Neuroscience & Biobehavioral Reviews; Thompson et al. 2019, Neuroscience & Biobehavioral Reviews.

Subtitles are written for this video, not auto-generated. An American English audio track is available as a second audio track.

CHAPTERS
00:00 The number six is gone
00:52 What can a hypnotist do?
01:10 Hypnosis in films
01:32 It isn't sleep
02:28 Stuck in a trance?
03:18 One person in eight
03:46 A rattlesnake behind glass
04:17 Sydney, 1960
05:48 Stage shows
06:09 A command for later
07:29 Try this
08:34 Memory
09:00 Chowchilla, 1976
09:36 A night that never happened
10:32 Is hypnosis any use?
11:42 Can someone program your mind?
12:08 A question for you

IMAGE CREDITS
Main Quadrangle, University of Sydney (cropped) — Jason Tong, CC BY 2.0
via Wikimedia Commons
Licence: creativecommons.org/licenses/by/2.0
All other archive images are in the public domain.
```

> **Blok se kopíruje CELÝ** (`docs/zverejneni.md`). CC BY* ze `sources.json`: jen S19 (Jason Tong). S10b, S15 a S30 jsou PD.
>
> **Pointa se neprozrazuje:** popis neříká *it only took the setting* (S28) ani *it feels like you* (S74).
> Kapitola 04:17 je proto jen místo a rok, ne výsledek.
>
> Kapitoly ze scén S01, S09, S10b, S11, S12e, S13, S15, S19, S30, S32, S43, S50, S53, S57, S64, S71, S75
> (`work/timing.json`, zaokrouhleno dolů). První na 00:00, všechny ≥ 10 s (nejkratší S75 → konec, 10,8 s;
> S10b → S11 22 s). Výzvy k odběru (za S12b a S42) leží uvnitř kapitol.
>
> **Zdroje:** jen to, co jsem četl (plný text nebo abstrakt podle `factcheck.md`). Rowland 1939 a přednáška
> Evans 1972 jsou ve `factcheck.md` přes druhou ruku, proto tu nejsou. Wikipedia a nekrology taky ne.

---

## 3. Náhled

C2 z `thumbnail/ZADANI.md` (ChatGPT): kádinka s kyselinou a ruka, `HYPNOSIS / WHO WOULD REACH IN?`.
`render/thumbnail.jpg`, nahráno přes `thumbnails.set` 2026-11-07. Původ v `thumbnail/PUVOD.md`.

---

## 4. Titulky

`subtitles/*.srt`, 14 jazyků + `en-US`. Jazyk videa **`en-gb`** (hlas `bf_emma`) se musí nastavit dřív,
než se nahrají titulkové stopy.

---

## 5. Nastavení

| | |
|---|---|
| kategorie | **Science & Technology** (28), posílá `nahraj.py` napevno |
| jazyk videa | `en-gb` |
| licence | standardní |
| pro děti | **ne** |
| komentáře | zapnuté (S75 je otázka do komentářů) |
| **byla použita AI** | **ne**. 79 z 85 scén je kreslených kódem, čtyři archivní snímky jsou upravené jen barevně a ořezem, S50 a S70 ze SDXL jsou malované ilustrace (kotva *painterly editorial illustration*), ne fotorealismus. Hudba je procedurální, hlas není klon skutečné osoby. |

### Závěrečná obrazovka

Od **11:59** (posledních 20 s), tedy S74–S75. `zaver_check` hlásí v obou dolních rozích titulek.
**Dlaždici i odběr dej do HORNÍ poloviny.** Jako dlaždici navrhuju **009 *If Our Brains Could Do Telepathy***
(téma mysli a sugesce), druhou nechat na „nejlepší pro diváka".

---

## 6. Tagy

```
hypnosis, what can hypnosis do, can a hypnotist control you, hypnotist, stage hypnosis,
posthypnotic suggestion, martin orne, hypnosis experiment, hypnosis and memory, false memory,
stroop effect, amir raz, hypnosis for pain, chowchilla kidnapping, psychology experiments,
mind control, there's more to it
```

---

## 7. Playlist

**`lide`** (*Why We Do What We Do*), za 135. Pinterest shortů: `Psychology & Human Behavior`.
Zapsat do `playlisty.json` při nahrání; `playlisty.py` ho přeskočí, dokud video není v `analytics/videa.json`.
