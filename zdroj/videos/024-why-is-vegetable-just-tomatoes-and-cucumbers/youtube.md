# Podklady k nahrání — Why Is Vegetable Basically Just Tomatoes and Cucumbers?

Soubor: `render/final-en.mp4` (9:58, 1920×1080, 25 fps, −14,05 LUFS / −1,29 dBTP, 77,5 MB)
Náhled: `render/thumbnail.jpg` (1280×720, 274 kB) — **hotový obrázek, ne kreslený
kódem**, viz `thumbnail/PUVOD.md`
Titulky: `subtitles/*.srt` — devět jazyků

## 1. Nastavení PŘED nahráním

**Jazyk videa nastav jako první**, jinak zůstane dlaždice „Titulky" zašedlá.
Je to **`en-gb`**, protože hlas je `bf_emma`.

| položka | hodnota |
|---|---|
| jazyk videa | angličtina (Spojené království) |
| kategorie | Věda a technika |
| pro děti | ne |
| **byla použita AI** | **ne** — viz níž |
| viditelnost | nejdřív **neveřejné**, po kontrole v přehrávači veřejné |

**Proč „ne" u otázky na AI:** rozhoduje fotorealističnost, ne použití
nástroje. Video má 63 diagramů kreslených kódem, 4 malované SDXL scény
(kotva stylu je malovaná ilustrace, ne fotorealismus), 2 skutečné archivní
fotografie upravené jen barevně (*„color adjustment or lighting filters"*
je výslovná výjimka pravidel) a procedurálně generovanou hudbu.

## 2. Popis

```
A supermarket tomato can taste like someone described a tomato to water.
That is not just a feeling — somebody measured it.

Researchers took three hundred and ninety-eight tomato varieties, analysed
what is in them and had people taste a selection. Modern commercial
varieties really do contain significantly less of the compounds that make
a tomato taste of tomato.

And one of those losses was not a trade-off at all. It was an accident:
growers wanted fruit that ripens evenly, so breeders selected a variety
without the dark green shoulder around the stem. That trait turned out to
be one gene — and the same gene builds the chloroplasts inside the fruit.
An unripe tomato quietly photosynthesises and makes part of its own sugar.
Switch the gene off and you get exactly what was ordered: even ripening,
less sugar, less red pigment. Nobody chose the last two.

Then we finish the job at home, because the aroma compounds are damaged
below twelve degrees and some of the genes that make them never properly
switch back on.

The cucumber has its own version of the story: wild cucumbers are bitter,
and domestication switched that off in the fruit on purpose.

So we asked agriculture for vegetables that are firm, even, cheap and that
do not fight back. We got exactly that.

But tomato and cucumber are not the definition of vegetable. They are
barely the tutorial.

SOURCES
Tieman et al., A chemical genetic roadmap to improved tomato flavor.
Science 355, 391 (2017). doi:10.1126/science.aal1556
Powell et al., Uniform ripening encodes a Golden 2-like transcription
factor regulating tomato fruit chloroplast development.
Science 336, 1711 (2012). doi:10.1126/science.1222218
Zhang et al., Chilling-induced tomato flavor loss is associated with
altered volatile synthesis and transient changes in DNA methylation.
PNAS 113, 12580 (2016). doi:10.1073/pnas.1613910113
Shang et al., Biosynthesis, regulation, and domestication of bitterness
in cucumber. Science 346, 1084 (2014). doi:10.1126/science.1259215

IMAGE CREDITS
Outdoor market fruit and vegetable stall, Market Place, Romford, London
— Acabashi, CC BY-SA 4.0
via Wikimedia Commons
Roasted Vegetables (2897937502) — Mack Male, CC BY-SA 2.0
via Wikimedia Commons
Licences: creativecommons.org/licenses/by-sa/4.0
and creativecommons.org/licenses/by-sa/2.0

Subtitles are written for this video, not auto-generated. An American
English audio track is available as a second audio track.

Full transcript, sources and translations: https://theresmoretoit-channel.github.io/videos/why-is-vegetable-just-tomatoes-and-cucumbers/

CHAPTERS
0:00 Intro
1:01 Somebody actually measured it
1:38 Why these two are everywhere
2:21 What a good tomato can be
2:35 What a supermarket tomato has to survive
2:54 The loss nobody ordered
3:20 The gene that builds the green machinery
3:38 Switch it off
3:58 And then the fridge
4:21 The cucumber did the same thing
4:38 Exactly what we asked for
4:57 Vegetables are not one thing
5:18 Carrots, broccoli and cabbage
5:56 Vegetables with an opinion
6:34 Cooking changes everything
7:08 Maybe it was how they were served
7:51 You can actually choose
8:29 In defence of tomatoes and cucumbers
8:59 What do I actually like?
9:28 Barely the tutorial
```

> **Zkopíruj CELÝ blok mezi trojicí zpětných apostrofů, nic jiného.**
> Atribuce je uvnitř schválně: u čtyř z šestnácti starších videí chyběla
> v popisu právě proto, že kredity ležely jako poznámka POD blokem.
> Obě fotky jsou **CC BY-SA**, takže uvedení autora je povinné.

## 3. Titulky

Nahraj všech devět souborů z `subtitles/`. Kód jazyka je zároveň přípona:

| soubor | jazyk | | soubor | jazyk |
|---|---|---|---|---|
| `en.srt` | English (United Kingdom) | | `de.srt` | Deutsch |
| `cs.srt` | čeština | | `fr.srt` | français |
| `sv.srt` | svenska | | `it.srt` | italiano |
| `es.srt` | español | | `pl.srt` | polski |
| `pt-BR.srt` | português (Brasil) | | | |

Naměřeno: 163 anglických titulků, 225 az 230 v překladech, u všech devíti
**nula řádků přes 42 znaků a nula třířádkových**.

## 4. Kapitoly

Kapitoly jsou už v bloku popisu. Ověřeno proti `work/timing.json`:
**dvacet kapitol, první na 0:00, každá trvá aspoň deset sekund** —
to jsou tři podmínky, bez kterých je YouTube neuzná. Dvě původně
navržené (Bred to ripen evenly, Cabbage) se musely sloučit, protože
od předchozí dělily jen 8 a 10 sekund.

## 5. Tagy

```
vegetables, tomato, cucumber, food science, why do supermarket tomatoes
taste bad, tomato flavour, uniform ripening, tomato genetics, plant
breeding, kohlrabi, celeriac, why vegetables taste bland, cooking
vegetables, food myths, popular science, there's more to it
```

## 6. Náhled je vědomý pokus — sleduj u něj CTR

Tenhle náhled je **třikrát světlejší než cokoli, co kanál kdy vydal**
(jas 100,8 proti pásmu 23 az 37). CLAUDE.md u jasu píše, že je to
proměnná bez rozptylu, tedy že se z dosavadních dat nedá zjistit nic —
tohle je první video, které tu otázku klade.

Až přijdou data, porovnávej **míru prokliku miniatur**, ne zhlédnutí:
je to jediná metrika, která měří náhled a ne obsah. Pásmo kanálu je
0,36 az 2,26 %.

## 7. Po nahrání

1. **Podívej se na to v přehrávači jako neveřejné.** YouTube video
   překóduje a jak vyjdou tmavé scény po jejich kompresi se dopředu
   posoudit nedá. Je to jediný krok, který nejde udělat na disku.
2. Závěrečná obrazovka a karty jdou přidat i po zveřejnění. **S66 je pro
   ně navržená** — klidná deska, prázdná dolní třetina i pravá polovina.
3. Doplnit odkaz do `Témata.ods`.

> **Vodoznak odběru** se nastavuje jednou na úrovni kanálu (Přizpůsobení →
> Branding) a projeví se **zpětně na všech videích**. Podle měření z
> 2026-09-02 je to jediný prvek, který není za úzkým hrdlem — vidí ho
> i divák, který odejde po dvaceti vteřinách.
