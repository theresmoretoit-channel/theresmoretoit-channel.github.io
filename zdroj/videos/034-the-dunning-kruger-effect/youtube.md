# YouTube — 034 The Dunning–Kruger Effect

Nahrává se `render/final-en.mp4` (master, ne draft), `render/thumbnail.jpg`
a `subtitles/*.srt` v devíti jazycích.

## 1. Titul

```
How Do You Know You're Not Wrong?
```

**Vybráno 2026-09-09.** Dodaný titul měl 82 znaků a jméno efektu vepředu;
YouTube jich v seznamu ukáže zhruba 60, takže by se utnul za „Dangerous".
Uživatel rozhodl, že jméno efektu v titulu neprodává. Zvolená varianta je
**doslova klimax videa** — storyboard na tu větu staví dvě identické desky,
S65 a S73 — a odpovídá zvyku kanálu: **24 z 32 titulů je otázka**, medián
délky **37 znaků**, a jediný dosavadní titul s odborným názvem je
„Fermi paradox might not be real".

Zvažované varianty:

| varianta | znaků | co dělá |
|---|---|---|
| `The Dunning–Kruger Effect — The Most Dangerous Thing You Don't Know You Don't Know` | 81 | dodal uživatel; v seznamu se utne za „Dangerous" |
| `You Don't Know What You Don't Know` | 34 | vede pointou, ne jménem efektu; funguje i bez toho, aby divák efekt znal |
| `The Dunning–Kruger Effect Isn't What You Think` | 46 | slibuje obrat, který video opravdu má (S55–S65), a jméno drží vepředu |
| `What If The Famous Graph Is Wrong?` | 34 | nejsilnější zvědavost, ale prozrazuje druhou polovinu |

## 2. Popis

```
You learn something new, and suddenly it seems simple. But what if the
thing you're missing is precisely the thing that would tell you that
you're missing something?

In 1999, Justin Kruger and David Dunning gave students tests of humour,
grammar and logic, then asked them how well they thought they had done.
Across four studies, the people in the bottom quarter scored around the
12th percentile — and estimated themselves at the 62nd. They weren't
just wrong. They were wrong about how wrong they were.

But the popular internet version gets it backwards, and there's a second
problem that almost nobody mentions: several researchers have argued
that the characteristic graph can appear partly for statistical reasons.
Take simulated data with no such effect in it at all, plot it the same
way, and you can still get a picture that looks much like the original.
The debate isn't settled — which brings us straight back to the
uncomfortable question the whole thing is about.

Full transcript, sources and translations: https://theresmoretoit-channel.github.io/videos/the-dunning-kruger-effect/

CHAPTERS
0:00 The feeling of getting it
0:35 Learning to program
1:19 The 1999 study
1:50 12th versus 62nd
2:18 Why it happens
3:17 Grading your own exam
4:39 What it does not mean
4:55 The graph itself
5:57 What they actually claimed
6:37 Are you doing it right now?
7:14 Feedback from reality
8:30 How would you find out?

Subtitles are written for this video, not auto-generated. An American
English audio track is available as a second audio track.

SOURCES
Kruger, J. & Dunning, D. (1999). Unskilled and Unaware of It. Journal of
Personality and Social Psychology 77(6), 1121-1134
Kruger & Dunning (2002). Unskilled and Unaware - But Why? A Reply to
Krueger and Mueller. JPSP 82(2), 189-192
Nuhfer et al. (2016, 2017). Numeracy 9(1) art. 4 and 10(1) art. 4
Gignac & Zajenkowski (2020). The Dunning-Kruger effect is (mostly) a
statistical artefact. Intelligence 80, 101449
Magnus & Peresetsky (2022). A Statistical Explanation of the
Dunning-Kruger Effect. Frontiers in Psychology

IMAGE CREDITS
Uris Hall Auditorium, Cornell University - Kenneth C. Zirkel, CC BY-SA 4.0
via Wikimedia Commons
Licence: creativecommons.org/licenses/by-sa/4.0

All other archive images are in the public domain.

Music, diagrams and animation made for this video.
```

## 3. Tagy

```
dunning kruger, dunning kruger effect, cognitive bias, metacognition,
overconfidence, self assessment, psychology, statistical artefact,
regression to the mean, kruger and dunning 1999, epistemic humility,
critical thinking, why experts sound unsure, science explainer
```

## 4. Nastavení

| pole | hodnota |
|---|---|
| jazyk videa | **`en-gb`** — nastavit NAPŘED, jinak zůstane dlaždice Titulky zašedlá |
| kategorie | **Science & Technology** (28) — posílá `nahraj.py`; kanál ji má u 11 z 12 ověřených videí |
| pro děti | ne |
| **byla použita AI** | **ne** — posílá `nahraj.py` jako `containsSyntheticMedia: false` |
| **osvědčení o zproštění** | ✅ **ručně ve Studiu**, API na to pole nemá |
| **závěrečná obrazovka** | ✅ **ručně ve Studiu**, API na to nemá ani zdroj |
| playlist | dopsat do `playlisty.json` před `tools/playlisty.py` |

## Proč je odpověď na „byla použita AI" NE

- **SDXL scény jsou 3 ze 101** a díky kotvě stylu jsou to malované
  ilustrace, ne fotorealismus.
- **Archivní snímky jsou 2** a upravené jen barevně — „color adjustment
  or lighting filters" je výslovná výjimka v pravidlech YouTube.
- **Hudba je procedurální** (sinusovky a šum v numpy), ne z generativního
  modelu.
- Zbylých **96 scén je kreslených kódem**.

## Postup nahrání

Výchozí cesta je **ruční nahrání MP4 ve Studiu + `--k-videu`**, ne
`videos.insert` — ušetří 1 600 jednotek kvóty a průvodce ve Studiu se
sám zeptá na prohlášení o AI i na osvědčení o zproštění.

```bash
# 1) MP4 přetáhnout do Studia, zjistit ID
python tools/nahraj.py videos/034-the-dunning-kruger-effect --k-videu <ID>
python tools/lokalizace.py videos/034-the-dunning-kruger-effect --id <ID>
python tools/titulky.py videos/034-the-dunning-kruger-effect --smaz-asr
```

> **Pořadí není libovolné.** `lokalizace.py` potřebuje `defaultLanguage`,
> a to pole Studio pod „jazykem videa" NENASTAVUJE — Studio nastaví jen
> `defaultAudioLanguage`. `defaultLanguage` posílá až `nahraj.py`, takže
> musí běžet první. Jinak lokalizace skončí na „video nemá nastavený
> jazyk" a hláška pošle člověka klikat do Studia, kde už to nastavené je.

> **A automatický přepis se vrátí.** Po nahrání ho YouTube vyrobí znovu
> během minut, takže `--smaz-asr` hned po nahrání nestačí — pusť ho ještě
> jednou s odstupem, nejlíp až po zveřejnění. Na jedno video se `--vse`
> nepoužívá: projde všech 32 videí a při plném běhu to spolu s nahráním
> vyčerpá denní kvótu (ověřeno 2026-09-09).

Po zveřejnění: doplnit číslo **34** a odkaz do `Témata.ods`, pustit
`tools/analytics.py --videa` a `tools/playlisty.py`.

> **Nahrát napřed neveřejně a podívat se na to v přehrávači.** YouTube
> video překóduje a jak po jejich kompresi vyjdou tmavé scény, se
> na disku posoudit nedá.
