# Podklady k nahrání na YouTube

Soubor je ruční. Čísla v něm jsou z `work/timing.json` a `CREDITS.md`,
ne z odhadu.

| co | odkud |
|---|---|
| video | `render/final-en.mp4` — 11:45, 81 MB, −14,0 LUFS / −1,3 dBTP |
| náhled | `render/thumbnail.jpg` — **c4 WHY PICK MUSHROOMS**, 76 kB |
| titulky | `subtitles/*.srt`, devět jazyků |
| atribuce | `CREDITS.md` |

---

## Titul

**Why Do People Go Mushroom Hunting?**

Záložní varianty, kdyby se testovalo:

- The Food You Cannot Buy
- Why Mushrooms Can't Be Farmed

## Popis

```
A stranger watches someone pull a brown lump out of the forest floor,
brush the dirt off it, and plan to eat it for dinner. In some countries
that is a completely ordinary afternoon. In others it looks insane.

This is about why the difference exists — and why mushroom hunting turns
out to be the last everyday survivor of something humans did for almost
all of our history.

Along the way: why a mushroom is closer to you than to the tree it grows
under, why most wild mushrooms cannot be farmed at all, why the deadliest
one in Europe kills by waiting, and why drying a mushroom does not weaken
it but makes it into a stronger ingredient than it ever was.

Full transcript, sources and translations: https://theresmoretoit-channel.github.io/videos/why-do-people-go-mushroom-hunting/

CHAPTERS
00:00 What on earth are they doing?
00:54 Not a plant, not an animal
01:30 What you see is not the whole organism
01:47 The largest living thing ever found
02:12 Why eat them at all?
02:42 Why most of them cannot be farmed
03:35 What is actually on the shelf
04:08 The dangerous ones
04:34 Why the death cap kills
05:08 The rules that do not work
05:49 Not mushrooms — species
06:30 How the knowledge travels
07:09 The honeymoon that named it
07:45 Food is mostly an agreement
08:14 Why drying changes everything
09:22 The part that is free
09:46 One thing that matters
10:20 So is it ridiculous?

A NOTE ON TWO NUMBERS
The thirtyfold figure for savoury intensity comes from tests on the pure
compounds — glutamate and guanylate mixed in equal amounts in solution.
It is not a measurement of dried mushrooms in a soup.
The Czech participation figure (73.1% of adults) is from harmonised survey
data collected 2020–2024.

Subtitles are written for this video, not auto-generated. An American
English audio track is available as a second audio track.

This video does not tell you how to identify a mushroom, and it is not a
substitute for someone who can. If you want to pick, learn from a person
who already knows, or use a reliable identification resource.

IMAGE CREDITS
Mushrooming — Erkki Voutilainen, CC BY 4.0
Boletus edulis — Holger Krisp, CC BY 3.0
Armillaria ostoyae — Holger Krisp, CC BY 3.0
Amanita phalloides — George Chernilevsky, public domain
Dried mushrooms — André Karwath aka Aka, CC BY-SA 2.5
Boletus edulis in situ — Bernie, public domain
All via Wikimedia Commons.

Music generated procedurally for this video.

There's more to it.
```

## Tagy

```
mushroom hunting, mushroom foraging, mycorrhiza, why mushrooms can't be farmed,
death cap, amanita phalloides, umami, dried mushrooms, mycophilia, mycophobia,
wasson, foraging, fungi, mycelium, porcini, chanterelle, food culture,
popular science, theres more to it
```

## Nastavení při nahrávání

| položka | hodnota | proč |
|---|---|---|
| **jazyk videa** | **`en-GB`** | **nastavit PRVNÍ**, jinak zůstane dlaždice Titulky zašedlá. Hlas je `bf_emma`, tedy britská angličtina |
| kategorie | Education | |
| **byla použita AI?** | **NE** | viz níž |
| pro děti | ne | |
| viditelnost | **nejdřív neveřejné** | YouTube video překóduje a jak vyjdou tmavé lesní scény po jejich kompresi se na disku posoudit nedá |

### Odpověď „byla použita AI" je NE — a proč

Rozhoduje **fotorealističnost**, ne použití nástroje
([pravidla](https://support.google.com/youtube/answer/14328491)).

- **50 z 63 scén jsou diagramy kreslené kódem** (SVG přes `diagrams/gen/`).
- **6 scén jsou archivní snímky** z Wikimedia, upravené jen barevně —
  *„color adjustment or lighting filters"* je výslovná výjimka.
- **7 scén je SDXL, a všechny jsou malované.** Tři z nich (S46, S51, S60)
  se musely přegenerovat, protože první pokus vyšel fotorealisticky —
  což by odpověď překlopilo na ANO. Po opravě jsou to zjevně olejové skici.
- **Hudba je procedurální** (`tools/music.py`, sinusovky a šum v numpy),
  ne z generativního modelu. Pravidla YouTube jmenují „AI-generated music"
  výslovně.

> Kdyby se cokoli z toho v budoucnu změnilo — jiný checkpoint, hudba ze
> Suno, klonovaný hlas — odpověď se překlápí a musí se u nahrávání změnit.

## Titulky

Nahrát všech devět. Kód jazyka musí odpovídat tomu, co zná YouTube:

| soubor | jazyk na YouTube |
|---|---|
| `en.srt` | English (United Kingdom) |
| `cs.srt` | čeština |
| `sv.srt` | svenska |
| `es.srt` | español |
| `pt-BR.srt` | português (Brasil) |
| `de.srt` | Deutsch |
| `fr.srt` | français |
| `it.srt` | italiano |
| `pl.srt` | polski |

## Thumbnail — na výběr jsou tři

**Vybráno uživatelem: `c4-why-pick-mushrooms`**, zapsáno v `project.json`
a vyrobeno do `render/thumbnail.jpg`. Zbylé tři zůstávají jako varianty
pro „Test & Compare".

Vybírá uživatel; je to jediné místo pipeline, kde měření nerozhodne.
YouTube umí „Test & Compare" až se třemi, takže se z těchhle čtyř
vybírají nejvýš tři.

| soubor | obraz | kterou pointu videa nese |
|---|---|---|
| `render/thumb-c4-why-pick-mushrooms.jpg` | tři druhy — liška, hřib, muchomůrka — **WHY PICK MUSHROOMS** | námět uživatele; nese otázku videa a zároveň to, že houbař rozlišuje **druhy**, ne „houby“ |
| `render/thumb-c1-not-for-sale.jpg` | houba a prázdná cenovka, **NOT FOR SALE** | nedá se to koupit, protože to neroste bez stromu |
| `render/thumb-c2-underground.jpg` | malý klobouk nad zemí, obrovská síť pod ní, **MOSTLY UNDERGROUND** | co vidíš, není celý organismus |
| `render/thumb-c3-one-of-these.jpg` | dvě nerozeznatelné houby, jedna označená, **ONE OF THESE KILLS** | bez znalosti druhu to nejde |

Všechny čtyři ověřené ve 210 px i ve 120 px. Po výběru zapsat do
`project.json` a vyrobit do `render/thumbnail.jpg`.

> **U c4 nese barva význam, ne pestrost.** Tři houby se liší barvou
> **i tvarem** — nálevka lišky, tlustý hřib, štíhlá muchomůrka s pochvou
> u báze. Kdyby se lišily jen barvou, první otázka diváka by byla „proč
> jsou různě barevné?“ a odpověď „pro pestrost“ je špatná (zpětná vazba
> ke třetímu videu).
>
> **c3 je nejsilnější hák a zároveň nejblíž hranici.** Není to clickbait —
> video přesně tohle tvrdí a dokládá — ale je to jediná varianta, která
> láká na nebezpečí místo na paradox. Kdyby se kanál měl držet dál od
> senzace, je c1 věcně stejně silná a klidnější.

## Před nahráním

```bash
# délka a integrita (ffprobe na kontejner NESTAČÍ — délku přečte
# i z rozsypaného streamu, proto dekódovací test)
ffmpeg -v error -i videos/007-why-do-people-go-mushroom-hunting/render/final-en.mp4 -f null -
ffprobe -v error -show_entries format=duration -of default=nw=1:nk=1 \
        videos/007-why-do-people-go-mushroom-hunting/render/final-en.mp4

# náhled do 2 MB
ls -l videos/007-why-do-people-go-mushroom-hunting/render/thumbnail.jpg
```

Ověřeno 2026-08-28: dekódovací test prochází beze slova, 705,12 s,
otisk MD5 shodný s tím, co vyrobilo herní PC.

## Po zveřejnění

Závěrečná obrazovka a karty jdou doplnit kdykoli. Odkazovat se dá na
**první video** (`what-is-a-wave-waving`), případně na třetí a čtvrté,
až budou nahraná.

Podklad pro odpovědi v komentářích je `factcheck.md` — hlavně kapitola
„Co se ve scénáři NETVRDÍ, ač by to bylo lákavé".
