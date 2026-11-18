# Podklady pro nahrání na YouTube

Ručně psaný zdroj. Časy kapitol odpovídají masteru z `work/timing.json`
(celkem 9:43) — **po každém přegenerování hlasu je odvoď znovu**, protože
se posunou. Naposledy ověřeno 2026-08-28 proti `render/final-en.mp4`.

---

## Titul

```
Which Is Better: Red Car or Car Red?
```

36 znaků. Limit je 100, mobil ukáže zhruba 60 — vejde se celý. Otázka,
ne tvrzení, tedy formát kanálu. Titul i thumbnail nesou tatáž dvě slova,
což je tady výjimečně v pořádku: pointa videa JE to prohození, takže
opakování není plýtvání, ale zdvojený signál.

Zvažované alternativy:

- `Most Languages Say Car Red. Why Doesn't English?` — 47 znaků, silné
  číslo v pozadí (879 : 373), ale slibuje video o angličtině, kdežto
  závěr je „ani jedno pořadí nevyhrává"
- `The Word Order Question Nobody Can Win` — 37 znaků, vystihuje závěr,
  ale nedá se vyhledat: nikdo takhle neformuluje dotaz

---

## Popis

```
"Take the red car." Most of the world would say "take the car red" — and
by a clear margin. Out of more than 1,300 languages surveyed, 879 put the
noun first and only 373 put the adjective first. So the order English uses
is the rarer one.

Which raises an awkward question: is one of them actually better?

There are good arguments both ways. Noun first tells you what we are
talking about straight away, and everything after it is just detail. But
if you are standing next to two hundred cars, "car" tells you nothing at
all — the colour is the only part that helps. And that turns the grammar
question into an information question: what does the listener already
know?

Along the way: Polish, which cheerfully does both at once and has a rule
for which adjective goes where; Norwegian, which moves a different word
entirely; and French, where moving the adjective quietly changes what the
sentence means.

Full transcript, sources and translations: https://theresmoretoit-channel.github.io/videos/which-is-better-red-car-or-car-red/

Chapters:
0:00 Take the red car
0:28 Adjective first: English, German, Swedish
0:58 Car red is the majority
1:21 Polish does both — and why
1:53 The case for the noun first
2:47 Two hundred cars
3:34 The real question
4:07 Language does not happen in isolation
4:48 The very long noun phrase
5:39 Back to Polish and Norwegian
6:21 French changes the meaning
7:36 So what is the verdict?
8:02 Nobody designed this
8:51 It depends
9:26 Two hundred of them

Subtitles are written for this video, not auto-generated. An American
English audio track is available as a second audio track.

There's more to it.
```

**Kapitoly**: patnáct, první na `00:00`, nejkratší 17 s (ta poslední) — YouTube žádá
aspoň tři a každou minimálně 10 s, takže projdou. Časy odvozené strojově
z `work/timing.json`, ne odhadem.

**Čísla v popisu**: 1 300 / 879 / 373 odpovídají `factcheck.md`. V popisu
jsou číslicemi schválně — ve scénáři jsou slovy jen kvůli TTS.

---

## Tagy

```
word order, adjective placement, linguistics, language typology, grammar explained, comparative linguistics, English grammar, French grammar, Polish grammar, Norwegian language, syntax, information theory, why languages differ, language explained
```

246 znaků. YouTube počítá **všechny tagy dohromady** proti limitu
500, takže je místo i na víc — seznam je krátký záměrně, ne z nouze.

Tři pravidla, podle kterých je vybraný:

- **jazyky, které ve videu opravdu zaznějí** (`English`, `French`,
  `Polish`, `Norwegian`) — ne všech devět jazyků titulků, ty se hledají
  jinak a jen by seznam naředily
- **oborové názvy** (`language typology`, `syntax`, `information theory`),
  protože podle nich hledají lidé, kteří o tématu něco vědí
- **nic o červeném autu.** `red car` je pointa titulu a thumbnailu, ale
  jako vyhledávací dotaz vede k prodeji ojetin, ne k lingvistice.

---

## Nastavení při nahrávání

| položka | hodnota |
|---|---|
| soubor | `render/final-en.mp4` (**master**, ne draft) |
| náhled | `render/thumbnail.jpg` — 1280×720, 47 kB |
| **jazyk videa** | **`en-GB`** — nastavit PRVNÍ, jinak zůstane dlaždice „Titulky" zašedlá |
| titulky | `subtitles/*.srt`, devět jazyků |
| kategorie | Vzdělávání |
| publikum | není určeno pro děti |
| **byla použita AI** | **ne** — viz níž |

### Titulky, které se nahrávají

`en` (en-GB), `cs`, `sv`, `es`, `pt-BR`, `de`, `fr`, `it`, `pl`.

Kód jazyka je zároveň přípona souboru a musí odpovídat kódu, který zná
YouTube.

### Označení AI obsahu

Odpověď je **ne** a drží ji tři věci:

- **59 z 68 scén jsou SVG diagramy** kreslené kódem, tedy vlastní dílo
- zbylých **7 je SDXL**, ale kotva stylu z nich dělá malované ilustrace,
  ne fotorealismus (výjimka v pravidlech YouTube)
- **archivní snímek žádný** a hudba je procedurální (`tools/music.py`),
  ne z generativního modelu

Kdyby se cokoli z toho změnilo, odpověď se překlápí — pravidla jsou
[tady](https://support.google.com/youtube/answer/14328491).

### Atribuce

`CREDITS.md` je prázdný — video nepoužívá ani jeden cizí snímek, takže do
popisu nepatří žádná atribuce. Cizojazyčné fráze říkají hlasy Piperu
(`de`, `sv`, `no`, `pl`, `fr`, `es`), všechny **CC0**, tedy taky bez
povinné atribuce.

---

## Thumbnail

Vybraný: **`c1-swap`** (`RED CAR` nad autem, `CAR RED` pod ním).

Zbylé dva leží připravené v `render/thumb-*.jpg` pro „Test & Compare",
kde jdou nahrát až tři:

| | co to je | jak čte ve 150 px |
|---|---|---|
| `c1-swap` | prohození kolem auta | ✅ nejjasnější, červená se přesune zleva doprava |
| `c2-question` | `RED ? CAR` | ✅ čte, ale podtitulek už ne |
| `c3-surrounded` | auto obklopené dvěma `RED` | ✅ čte, popiska na hraně |

---

## Kontrola před nahráním

```bash
ffprobe -v error -show_entries format=duration -of default=nw=1:nk=1 \
        videos/006-which-is-better-red-car-or-car-red/render/final-en.mp4
ffmpeg -v error -i videos/006-which-is-better-red-car-or-car-red/render/final-en.mp4 \
       -f null -                       # musí projít BEZE SLOVA
```

Naměřeno na masteru 2026-08-28: **583,04 s** (9:43), 1920×1080, h264,
25 fps, **−14,0 LUFS / −1,0 dBTP**, 50 MB. Dekódovací test prošel.

**Nahraj jako neveřejné a podívej se na to v přehrávači.** YouTube video
překóduje a jak po jejich kompresi vyjdou tmavé scény, se dopředu
posoudit nedá. Je to jediný krok, který nejde udělat na disku.

Závěrečná obrazovka a karty jdou přidat i po zveřejnění — tady je na co
odkazovat, protože kanál už má pět zveřejněných videí.
