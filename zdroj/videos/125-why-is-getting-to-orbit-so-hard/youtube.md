# YouTube — 125 „Why Is Getting to Orbit So Hard?“

Stav: **MP4 nahráno ručně ve Studiu 2026-10-28, kvóta došla uprostřed titulků.** Stav zveřejnění je v `Témata.fods`.

| | |
|---|---|
| ID videa | `IxISlshxSc8` (MP4 nahraje uživatel ručně ve Studiu) |
| master | ✅ `render/final-en-125.mp4` (8:25, 1920×1080, 505,08 s) |
| náhled | ✅ `render/thumbnail.jpg` (koncept A, Saturn V) |
| nastavení, popis, tagy | podklady níž |
| lokalizace | `youtube-preklady.md`, 13 jazyků |
| titulky | `subtitles/*.srt`, 14 jazyků + `en-US` (Codex hotový) |
| americká stopa | `render/audio-en-US.m4a`, ručně ve Studiu |
| závěrečná obrazovka | od **8:05**, S51–S52, prvky **nahoru** (viz níž) |
| karta | žádná (scénář na starší video neodkazuje) |
| playlist | `vesmir` (*Space — Getting There, and Who Else Is Out There*), na konec |

**Co musí uživatel naklikat sám:** závěrečnou obrazovku, americkou
audiostopu (`render/audio-en-US.m4a`) a osvědčení o zproštění, pokud ho
nevyřídil průvodce nahráním.

Stopáž 8:25 (`work/timing.json` total 505,04 s).

> Kdyby se znovu pouštěl `tts.py`, přepočítej kapitoly tady
> i v `youtube-preklady.md` a přegeneruj `en-US` přes `us_stopa.py`.

Pořadí podle CENY (`docs/zverejneni.md`):

```bash
V=videos/125-why-is-getting-to-orbit-so-hard
python tools/nahraj.py $V --k-videu=IxISlshxSc8 --bez-titulku    # 100
python tools/analytics.py --videa                               #   1  ← nutné
python tools/lokalizace.py $V                                   #  50
python tools/titulky.py $V --smaz-asr                           # 150  ← před titulky
python tools/titulky.py $V                                      # 400×15
python tools/playlisty.py                                       #  50
# úklid, až je MP4 na YouTube:
rm $V/render/draft*.mp4
ssh vrana@192.168.0.207 'rm -rf /home/vrana/temp/render-125-why-is-getting-to-orbit-so-hard'
```

---

## 1. Titul

```
Why Is Getting to Orbit So Hard?
```

> Wh-otázka, 32 znaků, shodná s `project.json`. Odpověď (logaritmus
> v raketové rovnici) titul neprozrazuje.

---

## 2. Popis

```
In July 1969, the rocket that carried the crew of the first Moon landing weighed about 2,900 tonnes on the launch pad. Eight days later, what came back to Earth weighed just under five. About one part in six hundred of that rocket came home. So where did the rest go, and why does reaching space take so much?

This video works through it step by step: why adding fuel to a rocket stops helping at some point, the equation every rocket still has to obey, how fast you actually need to go to stay in orbit, why rockets throw parts of themselves away on the way up, and why we can't simply build a better engine.

Along the way: a schoolteacher from Kaluga, a British mathematician working on military rockets in 1813, a Falcon 9 that delivers about four percent of its launch mass, an ion engine whose push is about the weight of a sheet of paper resting on your hand, and what the same calculation says about a planet ten times heavier than Earth, and about Mars.

Sources: Apollo 11 Mission Report (NASA, 1969); Saturn V Launch Vehicle Flight Evaluation Report AS-506 (Marshall Space Flight Center, 1969); W. Moore, A Treatise on the Motion of Rockets (1813); NASA/JPL, Dawn mission and ion propulsion; M. Rayman, Dawn mission results (AIAA Pickering Lecture, 2019); M. Hippke (2018), Spaceflight from Super-Earths is difficult, International Journal of Astrobiology.

Subtitles are written for this video, not auto-generated. An American English audio track is available as a second audio track.

IMAGE CREDITS
Apollo 11 launch; Saturn V third stage after separation (Apollo 8); Deep Space 1 ion engine test — NASA
Portrait of Konstantin Tsiolkovsky — public domain

Full transcript, sources and translations: https://theresmoretoit-channel.github.io/videos/why-is-getting-to-orbit-so-hard/

CHAPTERS
00:00 One part in six hundred
00:46 Fuel that has to carry fuel
01:13 A century-old equation
01:44 Reading the equation
02:25 More fuel, less speed
03:04 What it takes to reach orbit
04:14 Throwing the rocket away
05:32 Why not a better engine?
06:26 A heavier planet
07:54 The price
```

> **Blok se kopíruje CELÝ** (`docs/zverejneni.md`). Archiv má čtyři
> snímky (`CREDITS.md`): tři NASA (S04, S28, S39), jeden public domain
> (S11). **CC BY žádný**, atribuce tedy není povinná; NASA je uvedená
> jako zdvořilost podle jejích pravidel pro média. S39 je motor Deep
> Space 1, ne Dawn — popisek proto nejmenuje sondu z vyprávění.
>
> **Pointa se neprozrazuje.** Popis položí otázku ze S01–S03 a jmenuje
> témata, ne odpověď (logaritmus, S16–S20; „a rocket that throws away
> almost all of itself“, S51). Kapitola *More fuel, less speed* je
> paradox, ne vysvětlení.
>
> **Nic netvrdí víc než video** (`factcheck.md`): 2,900 t (S01, 2 941 t),
> „just under five“ (S02, 4 932 kg), šestistý díl (S03), Moore 1813 pro
> vojenské rakety (S12), ~4 % u Falconu 9 (S27, 22,8/549), list papíru
> (S40), desetkrát těžší planeta (S45). Mars (S49b) jen jako téma.
>
> Kapitoly ze scén S01, S06, S10, S13, S17, S21, S28, S37, S43, S50
> (`work/timing.json`, zaokrouhleno dolů). Nejkratší má 29 s (S10 → S13),
> poslední 31 s (S50 → konec), všechny ≥ 10 s. Výzvy k odběru (za S12
> a S36) leží uvnitř kapitol.
>
> Zdroje odpovídají `factcheck.md`, sekundární (Wikipedia,
> historyofinformation.com) se neuvádějí.

---

## 3. Náhled

`render/thumbnail.jpg` je koncept A (Saturn V, MOON ROCKET / WHERE DID
99% GO?), obrázek z ChatGPT, původ v `thumbnail/PUVOD.md`. Zálohy pro
Test & Compare: koncepty B a C (`thumbnail/ZADANI.md`).

---

## 4. Titulky

`subtitles/*.srt`, 14 jazyků + `en-US`. Jazyk videa **`en-gb`** (hlas
`bf_emma`) se musí nastavit dřív, než se nahrají titulkové stopy.
Codex proběhl (`notes.md`, 2026-10-26).

---

## 5. Nastavení

| | |
|---|---|
| kategorie | **Science & Technology** (28), posílá `nahraj.py` napevno |
| jazyk videa | `en-gb` |
| licence | standardní |
| pro děti | **ne** |
| komentáře | zapnuté (S52 končí otázkou do komentářů) |
| **byla použita AI** | **ne**. Dvě SDXL scény (S10, S43: raketa na rampě pod zataženou oblohou) jsou malované ilustrace podle kotvy stylu, ne fotorealismus ani konkrétní skutečné místo či událost; S43 je jen ručně retušovaná. Archivní snímky NASA jsou upravené jen barevně. Hudba procedurální, hlas není klon. |

### Závěrečná obrazovka

Od **8:05** (posledních 20 s z 505,0), tedy konec S51 (od 481,4 s)
a S52 (od 493,9 s). `zaver_check` u S51–S52 hlásí volnou **horní
polovinu** (dole je titulek), **dlaždici i kolečko odběru dej nahoru**.
Jako dlaždici doporučuju **035 *Can We Reach Another Star With Today's
Technology?*** (`4waGk1NE9QY`): divák, který právě slyšel cenu za oběžnou
dráhu, dostane otázku o cestě o dva řády dál. Alternativa **002 *Where
Does the Fuel Go When a Plane Dumps It?*** (`ULfrSBJInlc`): táž myšlenka
o hmotnosti paliva, kterou stroj musí nést.

---

## 6. Tagy

```
why is getting to orbit so hard, rocket equation, tsiolkovsky rocket equation,
delta-v, orbital velocity, saturn v, apollo 11, rocket staging, falcon 9,
ion engine, dawn spacecraft, super-earth, escape velocity, rocket science,
spaceflight, explainer, there's more to it
```

---

## 7. Playlist

**`vesmir`** (*Space — Getting There, and Who Else Is Out There*), na
konec za 112. Popis playlistu začíná „What it actually takes to leave
the ground“, což je přesně tohle video.
