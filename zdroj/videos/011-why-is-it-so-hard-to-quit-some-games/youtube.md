# Podklady k nahrání na YouTube

Jedenácté video kanálu **There's More To It**. Soubory:

| co | odkud |
|---|---|
| video | `render/final-en.mp4` (10:49, 43,9 MB, −14,0 LUFS / −1,3 dBTP) |
| náhled | `render/thumbnail.jpg` — koncept c3 STILL PLAYING?, 1280×720, 65 kB |
| titulky | `subtitles/*.srt`, **devět jazyků** |

---

## Titul

```
Why Is It So Hard to Quit Some Games?
```

## Popis

```
You come home tired, you start a game you already know, and three hours later
you are not sure you had any fun. This video is about why that happens — and
it is not because you lack willpower.

An unfinished thing does pull you back. That much has been measured: people
return to interrupted tasks about two thirds of the time. But on its own that
pull is weak. You put down a half-read book and the world carries on.

What makes it strong is that a game does not leave it on its own. It puts the
unfinished thing next to a reward, next to a deadline, next to a routine you
already have — and then it shows you a number. At that point you are not
really playing the game any more. You are maintaining it.

The second half is about what to do with that, and it takes the four pulls
apart one at a time. None of it says games are bad. Progress is one of the
reasons games are fun. The line worth watching is different: "I want to finish
something" is fine. "I can't stop even though I don't want to continue" is not.

CHAPTERS
00:00 Three hours, and no fun
01:20 A game that never ends
02:00 Progress is not the problem
02:32 Seventy-three per cent
03:12 Four pulls, not one
04:06 Playing, or maintaining?
04:41 A world that keeps growing
05:13 Why willpower is bad advice
05:47 1. Break the automatic start
06:38 2. Try a real break
07:13 3. Don't let FOMO decide
07:54 4. Leave things unfinished
08:40 5. One uncomfortable question
09:05 Games are not the problem
09:42 Playing differently
10:11 You don't have to

A FEW THINGS WORTH SPELLING OUT

The pull of unfinished things is real, but it is not the famous version of it.
The Zeigarnik effect — the claim that we remember unfinished tasks better —
does not hold up. A 2025 meta-analysis of 59 publications found no memory
advantage at all: interrupted and finished tasks were recalled about equally
(ratio 0.99 across 38 publications). What did hold up is its lesser-known
twin, the Ovsiankina effect: people resume interrupted tasks roughly 67% of
the time. That is what this video is built on, and it is why the video talks
about being pulled back rather than about remembering.

Ghibellini, R. & Meier, B. (2025). Interruption, recall and resumption: a
meta-analysis of the Zeigarnik and Ovsiankina effects. Humanities and Social
Sciences Communications 12, 962. doi:10.1057/s41599-025-05000-w (open access)

No specific game or publisher is named anywhere in this video, and that is
deliberate. Nothing here is a diagnosis either — "gaming disorder" is a real
ICD-11 condition, and an ordinary evening routine is not it.

Subtitles are written for this video, not auto-generated. An American English
audio track is available as a second audio track.
```

## Tagy

```
games, video games, gaming, game design, live service, progress bar,
completionist, daily quests, FOMO, habits, motivation, psychology,
Ovsiankina effect, Zeigarnik effect, why we keep playing, gaming habits,
screen time, quitting games
```

## Nastavení při nahrávání

| pole | hodnota |
|---|---|
| jazyk videa | **`en-gb`** — nastavit PRVNÍ, jinak zůstane dlaždice „Titulky" zašedlá |
| kategorie | Věda a technika (Science & Technology) |
| pro děti | ne |
| byla použita AI | **ne**, viz níž |
| titulky | nahrát všech devět `.srt`; kód souboru = kód jazyka na YouTube |
| náhled | `render/thumbnail.jpg` |
| viditelnost | **nejdřív neveřejné**, podívat se v přehrávači, pak teprve zveřejnit |

### Proč je odpověď na AI „ne"

Rozhoduje fotorealističnost, ne použití AI
([pravidla](https://support.google.com/youtube/answer/14328491)):

- **72 ze 75 scén jsou diagramy kreslené kódem** (`diagrams/gen/`), tedy
  vektorová grafika, ne generovaný obraz.
- **3 scény jsou SDXL** (S01, S37, S49) a všechny jsou díky kotvě stylu
  **malované ilustrace**, ne fotorealismus.
- **Žádné archivní snímky**, takže žádná atribuce a žádné `CREDITS.md`.
- **Hudba je procedurální** (sinusovky a šum v numpy, `tools/music.py`),
  ne z generativního modelu.
- Hlas je Kokoro `bf_emma` — syntetický, ale **není to klon skutečné osoby**.

### Varianty náhledu pro „Test & Compare"

YouTube umí testovat až tři. Kromě vybraného `c3-outside` leží připravené:

- `render/thumb-c1-never.jpg` — pruh postupu bez konce, NEVER ONE HUNDRED
- `render/thumb-c2-turn-it-off.jpg` — monitor se symbolem vypnutí, TURN IT OFF

## Před nahráním zkontrolovat

```bash
# délka a integrita (ffprobe samotné poškození neodhalí)
ffmpeg -v error -i videos/011-why-is-it-so-hard-to-quit-some-games/render/final-en.mp4 -f null -
ffprobe -v error -show_entries format=duration -of default=nw=1:nk=1 \
        videos/011-why-is-it-so-hard-to-quit-some-games/render/final-en.mp4

# titulky nesmí přesáhnout délku videa
python3 -c "
import pathlib,re
for l in ('en','cs','sv','es','pt-BR','de','fr','it','pl'):
    t=pathlib.Path(f'videos/011-why-is-it-so-hard-to-quit-some-games/subtitles/{l}.srt').read_text(encoding='utf-8')
    b=[x.split(chr(10)) for x in t.strip().split(chr(10)*2)]
    print(l, len(b), b[-1][1])"
```

Naměřeno 2026-08-30: **649,8 s**, dekódovací test projde beze slova,
titulky ve všech devíti jazycích končí v **648,5 s**.

## Poznámky k odpovídání v komentářích

Podklad je `factcheck.md`. Dvě věci, na které se nejspíš někdo zeptá:

1. **„To je přece Zeigarnikové efekt."** Není, a je to ve videu schválně.
   Paměťová verze se nereplikuje (metaanalýza 2025, poměr 0,99). Drží
   Ovsiankinové efekt, tedy návrat k přerušené činnosti — 67 %.
2. **„Které hry to dělají?"** Video schválně nejmenuje ani jednu. Obvinění
   konkrétního titulu by chtělo úplně jinou úroveň dokladů, než na jakou
   tenhle scénář stojí.

## Závěrečná obrazovka a karty

Kanál už má deset dalších videí, takže **tady poprvé dává smysl odkázat** —
závěrečná obrazovka jde přidat i po zveřejnění. Poslední scéna je tmavá
(zhasnutý monitor), takže je na prvky dost místa a nic nepřekryjí.
