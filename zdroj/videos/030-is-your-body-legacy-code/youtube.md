# Podklady pro nahrání na YouTube

Ručně psaný zdroj. Časy kapitol odpovídají renderu z `work/timing.json`
(celkem 11:31) — **po každém přegenerování hlasu je potřeba je znovu
odvodit**, protože se posunou.

---

## 1. Titul

```
Is Your Body Legacy Code?
```

25 znaků. Limit je 100, mobil ukáže zhruba 60 — vejde se bez oříznutí.

Vybral uživatel ze čtyř variant. Zvažované alternativy:

- `Why Is DNA Such Bad Code?` — 25 znaků, pojmenuje téma i úhel naráz,
  ale „bad code" svádí k tomu, že video kritizuje
- `Biology Is The Worst Software Project` — titul zdrojového textu,
  37 znaků. Tvrzení místo otázky, tedy proti zvyklosti kanálu
- `Who Wrote The Code In Your Cells?` — 32 znaků, otázka s překvapivou
  odpovědí („nikdo"), ale delší a hůř čitelná v malém

„Legacy code" je pro programátorské publikum okamžitě čitelné a nese
celou pointu; biologii dodá náhled, takže ji titul nést nemusí.

---

## 2. Popis

První dva řádky jsou to jediné, co je vidět před „show more". Zbytek
je pro ty, kdo rozkliknou.

```
Imagine a program with three billion characters of instructions, copied whole into every new
process — which then ignores ninety-nine percent of it. That is roughly what your cells do.

Almost every cell in your body that has a nucleus carries the same complete copy of your
genome. A neuron has it. A liver cell has it. They behave nothing alike. So a gene starts to
look a bit like a function — except there is no CPU, no instruction pointer and nothing that
executes DNA line by line. What decides which parts get used is a network of molecular
interactions, and having the code turns out to be very different from having access to it.

From there the software analogy gets stranger rather than weaker. A repository with a commit
history four billion years deep, maintained by patches and workarounds because nothing can
ever be rewritten. A continuous integration pipeline whose tests run on the production system.
Trillions of tiny agents with no central server and no one holding the architecture in their
head. And a machine that has been running for decades without a single reboot, replacing its
own parts while it serves.

Then the analogy breaks, and that is the most interesting part. DNA is not a blueprint. There
is no line that says create arm. We can sequence a genome, identify genes and measure
proteins — and we still cannot put the DNA of one ordinary cell into a computer, press run and
watch a human develop. We have the genome. The genome is not the whole machine.

Full transcript, sources and translations: https://theresmoretoit-channel.github.io/videos/is-your-body-legacy-code/

Chapters
0:00 The program nobody would write
0:37 Every cell has the whole thing
0:57 Genes look like functions
1:35 But there is no CPU
1:47 What plays the role of a pointer
2:49 Having the code isn't having access
3:10 The module called finger
3:42 Who designed this?
3:56 Four billion years of commits
4:48 It doesn't refactor
5:26 Where are the unit tests?
5:54 When a cell wins and you lose
6:16 There is no central server
6:57 Your body is a distributed system
7:36 Nobody ever restarts it
8:39 And somehow it works
9:00 Where the analogy breaks
9:53 We don't have the source code
10:15 The final paradox

Every visual in this video was drawn or generated for it — there are no archive photographs,
so there is nothing to attribute. The music is procedural, generated with numpy.

Subtitles are written for this video, not auto-generated. An American English
audio track is available as a second audio track.
```

**Blok výš se kopíruje CELÝ a nic pod ním se na YouTube nedostane.**
U tohohle videa v něm žádná atribuce být nemusí — `storyboard.json`
nemá jedinou scénu se `source: "archive"`, takže neexistuje
`sources.json` ani `CREDITS.md`. Věta o původu vizuálů je uvnitř bloku
schválně: mlčení by u kanálu, který jinak kredituje, vypadalo jako
opomenutí.

---

## 3. Kapitoly

Devatenáct kapitol, první na `00:00`, nejkratší úsek **12 s**
(`3:42` → `3:56`). YouTube žádá aspoň tři a každou nejméně 10 s —
splněno. Časy jsou ze `work/timing.json`, ne odhad.

---

## 4. Tagy

```
biology, DNA, genetics, gene expression, software engineering, legacy code, programming,
computer science, distributed systems, evolution, cells, genome, technical debt, refactoring,
continuous integration, science explained, popular science, analogy, systems thinking
```

---

## 5. Nastavení

| pole | hodnota | kdo to dělá |
|---|---|---|
| jazyk videa | **`en-gb`** — nastavit PRVNÍ, jinak zůstane dlaždice Titulky zašedlá | `nahraj.py` |
| kategorie | Věda a technika | `nahraj.py` |
| pro děti | ne | `nahraj.py` |
| **byla použita AI** | **ne** (`status.containsSyntheticMedia: false`) | `nahraj.py` |
| **Osvědčení o zproštění** | zaškrtnout „nikdy se nevysílalo v TV v USA" | **ručně ve Studiu**, API na to pole nemá |
| viditelnost | nejdřív **neveřejné** a podívat se na to v přehrávači | ručně |
| titulky | devět jazyků z `subtitles/` | `nahraj.py` |
| lokalizace | `youtube-preklady.md` přes `lokalizace.py` | zvlášť |

### Proč „byla použita AI" = ne

Tři důvody, tytéž jako u ostatních videí kanálu:

- **94 % scén jsou diagramy kreslené kódem** (100 ze 106) — SVG
  v repozitáři, žádný model
- šest SDXL scén drží kotva stylu *painterly conceptual illustration*,
  tedy **malovaná ilustrace, ne fotorealismus**; pravidla YouTube se
  ptají na fotorealističnost, ne na původ
- hudba je **procedurální** (sinusovky a šum v numpy), ne z generativního
  modelu

Rozhodne se to znovu, jakmile by přišel fotorealistický checkpoint nebo
scéna zobrazující konkrétní skutečné místo či událost. Ani jedno tu není.

---

## 6. Kvóta

Celý postup stojí **5 301 jednotek** z denního stropu 10 000
(video 1 600 + náhled 50 + devět titulků 3 600 + lokalizace 51),
takže **v ten den se nedá nahrát druhé video**. Pozor na paralelní
sezení — u videa 029 sebralo kvótu a titulky nedojely.

---

## 7. Náhled

`render/thumbnail.jpg` (1280×720, 244 kB) je **hotový obrázek od
uživatele**, ne kreslený kódem — provedení konceptu `c3-zaplata` jako
3D render. Původ, otisk a rozbor jsou v `thumbnail/PUVOD.md`.

Na prohlášení „byla použita AI" to nic nemění: ta otázka se ptá na
**obsah videa**, ne na náhled.

## 8. Stav

| | |
|---|---|
| master `render/final-en.mp4` | ✅ 1920×1080, supersample 3 |
| šest SDXL scén | ✅ vygenerováno na herním PC |
| náhled | ✅ |
| devět jazyků titulků | ✅ |
| lokalizace | ✅ `youtube-preklady.md` |
