# Podklady k nahrání na YouTube

Video: `render/final-en.mp4` (**11:22, 1920×1080, −14,1 LUFS / −1,3 dBTP, 55,4 MB**)
Náhled: `render/thumbnail.jpg` — **hotový obrázek** podle
`docs/thumbnail-styl.md` (2026-09-04), 1280×720, 176 kB.
Zdroj a rozbor: `thumbnail/PUVOD.md`
Titulky: `subtitles/*.srt` — devět jazyků

---

## Titul

> **If An AI Said It Was Afraid, How Would We Know?**

Alternativy, kdyby se testovaly:

- Can AI Be Conscious? The Honest Answer Is: We Don't Know
- Intelligence Without Anyone Home

> **Titul nesmí tvrdit, že dnešní AI vědomí má.** Odpověď videa je
> „probably not" a celá druhá polovina rozebírá to slovo (viz
> `factcheck.md`, kapitola 11). Zvolený titul je otázka, ne tvrzení.

---

## Popis

```
Not whether AI can be intelligent — we already know it can.
Whether there is anything it is like to be one.

This video takes the question seriously and refuses to answer it
dishonestly. It starts with our own consciousness: what it is, why
nobody can locate it in the brain, and what general anaesthesia
tells us about it. Then it asks the harder question — if
consciousness is a property of how a system is organised, why would
that system have to be biological?

And then the part that actually matters: even if we built one,
how would we ever tell?

Today's language models are probably not conscious. This video
explains why "probably" is doing a lot of work in that sentence.

CHAPTERS
0:00 The question nobody can answer
0:41 What is consciousness anyway?
1:31 Where is it in the brain?
2:14 The orchestra
2:48 Switching consciousness off
3:33 Why would it have to be biological?
4:12 How would we ever know?
4:59 What if it lies?
5:36 And what are we made of?
6:20 Emergence
7:00 But today's models are different
7:56 Intelligence is not consciousness
8:44 So is today's AI conscious?
8:59 Now imagine a future system
9:39 And now the opposite
10:24 What we know and what we don't

Subtitles are written for this video, not auto-generated. An
American English audio track is available as a second audio track.

SOURCES AND CREDITS
Orchestra photograph: "Columbus Symphony Orchestra concert in the
Ohio Theater" by Cbusram, CC BY 4.0, via Wikimedia Commons.
https://commons.wikimedia.org/wiki/File:Columbus_Symphony_Orchestra_concert_in_the_Ohio_Theater.jpg

Key references: Butlin, Long et al., "Consciousness in Artificial
Intelligence: Insights from the Science of Consciousness" (2023),
arXiv:2308.08708 — and the Cogitate Consortium's adversarial test of
global neuronal workspace and integrated information theories,
Nature (2025).

Music is generated procedurally. Illustrations and diagrams are
drawn as code; the atmospheric scenes are painted, not photographic.
```

---

## Nastavení při nahrávání

| co | hodnota |
|---|---|
| **Jazyk videa** | `en-gb` — **nastavit PRVNÍ**, jinak zůstane dlaždice „Titulky" zašedlá |
| Byla použita AI? | **NE** |
| Kategorie | Věda a technika |
| Komentáře | povolené |

> **Proč „ne" u dotazu na AI.** Rozhoduje fotorealističnost, ne použití
> nástroje. Video má **82 diagramů kreslených kódem, 4 malované SDXL
> scény a 1 skutečnou archivní fotku**. SDXL scény jsou díky kotvě stylu
> malované ilustrace, archivní snímek je upravený jen barevně
> (výslovná výjimka pravidel) a hudba je procedurální, ne z generativního
> modelu.

## Tagy

```
consciousness, artificial intelligence, AI, philosophy of mind,
hard problem of consciousness, neuroscience, anaesthesia,
integrated information theory, global workspace theory,
emergence, large language models, machine consciousness,
qualia, subjective experience, can AI think
```

---

## Kontrola před nahráním

```bash
ffprobe -v error -show_entries format=duration -of default=nw=1:nk=1 \
        videos/022-can-ai-have-consciousness/render/final-en.mp4     # 682.0
ffmpeg -v error -i videos/022-can-ai-have-consciousness/render/final-en.mp4 -f null -   # beze slova
ls -la videos/022-can-ai-have-consciousness/render/thumbnail.jpg     # 176 kB, do 2 MB
python3 tools/thumb_check.py videos/022-can-ai-have-consciousness  # jas/kontrast + náhledy
```

**Náhled se vyměňuje u už zveřejněného videa.** YouTube to umožňuje bez
smazání a nahrání znovu — Obsah → video → Miniatura → Nahrát. Video se
nesahá, takže zhlédnutí ani titulky zůstávají.

> **Poznamenej si datum výměny.** CTR před ní a po ní se v exportu sečte
> do jednoho čísla, takže bez toho data se kreslený náhled od generovaného
> u tohohle videa zpětně neoddělí. Podrobněji v `thumbnail/PUVOD.md`.

Kreslené koncepty `c1` az `c3` zůstávají v `render/thumb-*.jpg`, kdyby se
chtěly otestovat proti tomuhle.

**Nahraj jako neveřejné a podívej se na to v přehrávači.** Video má
hodně tmavých scén a jak vyjdou po překódování YouTube se dopředu
posoudit nedá — je to jediný krok, který nejde udělat na disku.

Závěrečná obrazovka a karty jdou přidat i po zveřejnění.
