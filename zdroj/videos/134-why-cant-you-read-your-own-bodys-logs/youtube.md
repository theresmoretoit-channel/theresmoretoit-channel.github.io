# YouTube — 134 „Why Can't You Read Your Own Body's Logs?“

Stav: **nahráno a naplánováno** (MP4 ručně 2026-11-05; metadata, náhled a lokalizace přes API týž den, zbylé titulky a plán zveřejnění ručně ve Studiu). **Zbývá playlist, došla kvóta, reset v 9:00.** Stav zveřejnění je v `Témata.fods`.

| | |
|---|---|
| ID videa | `4jsBorKAljc` — https://www.youtube.com/watch?v=4jsBorKAljc |
| master | `render/final-en-134.mp4` (render na .207, 2026-11-05; na YouTube ověřený soubor 35 228 086 B) |
| náhled | ✅ `render/thumbnail.jpg` — koncept C2 (`thumbnail/PUVOD.md`) |
| nastavení, popis, tagy | podklady níž |
| lokalizace | `youtube-preklady.md`, 13 jazyků |
| titulky | `subtitles/*.srt`, 14 jazyků + `en-US`, Codex hotový a zapracovaný |
| americká stopa | `render/audio-en-US.m4a`, ručně ve Studiu |
| závěrečná obrazovka | S54–S55, **horní polovina** (viz níž) |
| karty | žádné |
| playlist | `telo` (*Your Body, and How Long It Lasts*), hned za 030 |

**Co musí uživatel naklikat sám:** závěrečnou obrazovku, americkou audiostopu
(`render/audio-en-US.m4a`) a osvědčení o zproštění, pokud ho nevyřídil průvodce nahráním.

Stopáž 10:10 (`work/timing.json` total 610,0 s).

> **Do popisu jen „BMJ, 1995".** Citace není ověřená v originále (`notes.md`, `factcheck.md`). Přesnou referenci
> ani autory nepsat, dokud ji někdo nedohledá v archivu.
>
> Kdyby se znovu pouštěl `tts.py`, přepočítej kapitoly tady i v `youtube-preklady.md`
> a přegeneruj `en-US` přes `us_stopa.py`.

Pořadí podle CENY (`docs/zverejneni.md`):

```bash
V=videos/134-why-cant-you-read-your-own-bodys-logs
python tools/nahraj.py $V --k-videu=4jsBorKAljc --bez-titulku   # 100
python tools/analytics.py --videa                        #   1  ← nutné
python tools/lokalizace.py $V                            #  50
python tools/titulky.py $V --smaz-asr                    # 150  ← před titulky
python tools/titulky.py $V                               # 400×15
python tools/playlisty.py                                #  50
# úklid, až je MP4 na YouTube:
rm $V/render/draft*.mp4
ssh vrana@192.168.0.207 'rm -rf /home/vrana/temp/render-134-why-cant-you-read-your-own-bodys-logs'
```

---

## 1. Titul

```
Why Can't You Read Your Own Body's Logs?
```

> Wh-otázka, 40 znaků, shodná s `project.json`. Odpověď (S48, S51–S52: logy existují, jen nebyly psané pro tebe,
> a root nikdy nebyl tvůj) titul neprozrazuje.

---

## 2. Popis

```
When your computer crashes, you open the logs. When your body goes wrong, you get a headache, a vague feeling and no explanation. It's your own body, and you can't ask it what happened last night. Why not?

This video follows the evidence: a builder in agony with a completely unharmed foot, a construction worker with a nail in his brain and a toothache, the rule Google's engineers use to decide what may wake them up, the alarm that can watch the wrong number, the alert that carries the wrong address, and the organ that can't feel pain in its own tissue.

Sources: BMJ, 1995; AP and TIME (Colorado, 2005); Google, Site Reliability Engineering; Patrick Wall, Pain, 1979; WHO, Global report on hypertension, 2023; Zhang et al., Circulation, 2016; Randolph Nesse, the smoke detector principle, 2001; AAIASB final report on Helios Flight 522; National Organization for Rare Disorders; Sender & Milo, Nature Medicine, 2021; Zheng & Meister, Neuron, 2024; Xu et al., Science, 2015; Alexandrov et al., Science, 2016; Cleveland Clinic; NHLBI.

This video is not medical advice. New or unexplained chest pain is a reason to get help now.

Subtitles are written for this video, not auto-generated. An American English audio track is available as a second audio track.

Full transcript, sources and translations: https://theresmoretoit-channel.github.io/videos/why-cant-you-read-your-own-bodys-logs/

CHAPTERS
00:00 Your body's error messages
00:57 Two nails
02:10 Is anything being recorded?
03:26 Every page should be actionable
04:50 The smoke detector
05:19 The alarm that watches the wrong number
06:32 The wrong address
07:14 The organ that can't feel pain
07:39 So is there any log at all?
08:32 Who reads the logs?
09:17 Back to where we started
09:57 A question for you

IMAGE CREDITS
Beau's line on left, middle fingernail — Elipongo, public domain
via Wikimedia Commons
```

> **Blok se kopíruje CELÝ** (`docs/zverejneni.md`). Jediný archivní snímek je S47, public domain.
>
> **Pointa se neprozrazuje:** popis nejmenuje závěr S48 ani S51–S52. Kapitola 08:32 je proto otázka, ne odpověď.
>
> Kapitoly ze scén S01, S07, S15, S22, S29, S31, S37, S41, S43, S48, S51, S55 (`work/timing.json`, zaokrouhleno dolů).
> První na 00:00, všechny ≥ 10 s (nejkratší 13 s, S55 → konec). Výzvy k odběru (za S14 a S30) leží uvnitř kapitol.
>
> **Zdravotní věta** je tu proto, že video rozebírá příznaky: S40 ji říká i hlasem.

---

## 3. Náhled

`render/thumbnail.jpg` (1280×720): starý terminál se siluetou těla, *YOUR BODY* / *WHERE ARE THE LOGS?*. Koncept C2 z `thumbnail/ZADANI.md`, původ a otisky v `thumbnail/PUVOD.md`.

---

## 4. Titulky

`subtitles/*.srt`, 14 jazyků + `en-US`. Jazyk videa **`en-gb`** (hlas `bf_emma`) se musí nastavit dřív,
než se nahrají titulkové stopy. Codex hotový a zapracovaný (`notes.md`, „Překlady 14 jazyků").

---

## 5. Nastavení

| | |
|---|---|
| kategorie | **Science & Technology** (28) — posílá `nahraj.py` napevno |
| jazyk videa | `en-gb` |
| licence | standardní |
| pro děti | **ne** |
| komentáře | zapnuté (S55 je otázka do komentářů) |
| **byla použita AI** | **ne**. 55 scén z 56 je kreslených kódem (diagramy, 14 animací), jedna je archivní fotka (S47) upravená jen barevně. SDXL ve videu není, hudba je procedurální, hlas není klon skutečné osoby. |

### Závěrečná obrazovka

Od **9:50** (posledních 20 s), tedy S54–S55. `zaver_check` hlásí v dolních rozích titulek, kresba je jen v dolní polovině.
**Dlaždici i odběr dej do HORNÍ poloviny.** Jako dlaždici **030 *Is Your Body Legacy Code?***
(rozhodnuto při schválení draftu), druhou nechat na „nejlepší pro diváka".

---

## 6. Tagy

```
your body's logs, interoception, vagus nerve, referred pain, why pain can be wrong,
silent heart attack, high blood pressure no symptoms, smoke detector principle,
every page should be actionable, site reliability engineering, helios flight 522,
hypoxia, ondine's curse, brain has no pain receptors, biological records,
body as a computer, there's more to it
```

---

## 7. Playlist

**`telo`** (*Your Body, and How Long It Lasts*), hned za 030 (*Is Your Body Legacy Code?*), se kterým sdílí metaforu těla jako
systému. Na playlistu závisí i nástěnka Pinterestu u shortů: `Health & the Human Body`. Zapsat do `playlisty.json` při
nahrání; `playlisty.py` ho přeskočí, dokud video není v `analytics/videa.json`.
