# Podklady k nahrání na YouTube

Dvacáté video kanálu **There's More To It**.

| co | odkud |
|---|---|
| video | `render/final-en.mp4` (master, ne draft) |
| náhled | `render/thumbnail.jpg` — **c1-nobody**, 1280×720, 87 kB |
| titulky | `subtitles/*.srt`, devět jazyků |
| atribuce do popisu | `CREDITS.md` |

> **Napřed nastav jazyk videa na `en-gb`**, jinak zůstane dlaždice
> „Titulky" zašedlá. Hlas je `bf_emma`, tedy britská angličtina.

---

## Titul

**Who Runs the Earth?**

Varianty, kdyby byl potřeba delší:

- Who Runs the Earth? Nobody — And That's the Problem
- Who Runs the Earth? Why There Is No Government Above Governments

## Popis

```
There is the United Nations. There are international courts, treaties and
countless international organisations. But there is no world government
with its own police and military that can simply say: "This country has
broken the rules. And now we are going to stop it."

So who is actually above the countries? Nobody.

This video is about what that absence actually means — why international
politics is anarchic in the technical sense (no higher authority), why
even a hegemon is not a world government, what a Federation of Earth
would really need, and why the thing most likely to force our hand isn't
an agreement but a problem bigger than the units trying to solve it.

An asteroid. A pandemic. Or a signal from another star system, and the
question nobody on this planet can currently answer: who represents Earth?

Chapters below. Subtitles are written for this video, not auto-generated.
An American English audio track is available as a second audio track.

---

Full transcript, sources and translations: https://theresmoretoit-channel.github.io/videos/who-runs-the-earth/

00:00 Nobody is above the countries
01:01 How it works inside a country
01:39 The same question, one level up
02:37 So why not just build one?
03:37 The United States was not a world government
04:40 What a Federation of Earth would need
05:29 Forty-eight hours instead of sanctions
06:11 And what if it goes wrong?
06:51 A thin layer, not a ceiling
07:32 What would actually force us
07:54 An artificial signal
08:39 Who speaks for Earth?
09:12 It doesn't have to be aliens
09:55 Add another layer
10:29 But would it really be better?
11:10 Nobody to say enough

---

Sources and image credits:

S45 — United Nations Security Council chamber, photo by Patrick Gruban,
CC BY-SA 3.0, via Wikimedia Commons
https://commons.wikimedia.org/wiki/File:United_Nations_Security_Council_4-3-crop.jpeg

S89 — Blue Marble 2012, NASA/GSFC
https://images.nasa.gov/details/GSFC_20171208_Archive_e001386

All diagrams are drawn in code (SVG). Music is generated procedurally.
```

## Thumbnail

Vybraný: **`c1-nobody`** — Země a nad ní prázdný čárkovaný rámeček
s otazníkem, pod tím jediné slovo **NOBODY**.

`c2-no-one-above` a `c3-who-speaks` zůstávají v `render/thumb-*.jpg`
jako varianty pro „Test & Compare" (YouTube umí až tři).

## Tagy

```
world government, international relations, political theory, sovereignty,
anarchy, Max Weber, monopoly on violence, United Nations, Security Council,
hegemony, unipolar moment, federation of earth, first contact, SETI,
global governance, geopolitics, explainer, video essay
```

## Nastavení

| pole | hodnota |
|---|---|
| jazyk videa | **`en-gb`** (nastavit PRVNÍ) |
| kategorie | Education |
| licence | Standardní licence YouTube |
| pro děti | ne |
| **byla použita AI** | **ne** — viz níž |
| komentáře | zapnuté |

### Proč „ne" u otázky na AI

Rozhoduje **fotorealističnost, ne použití AI**
([pravidla](https://support.google.com/youtube/answer/14328491)).

| zdroj | scén | proč to odpověď nepřeklápí |
|---|---|---|
| kreslené diagramy (SVG) | **85** | kód, ne model |
| SDXL | **3** | malované ilustrace díky kotvě stylu, ne fotorealismus |
| archivní snímky | **2** | upravené jen barevně — výslovná výjimka pravidel |
| hudba | — | procedurální (sinusovky a šum v numpy), ne generativní model |

Model tedy dělá **tři scény z devadesáti jedna** a žádná z nich
nezobrazuje konkrétní skutečné místo ani událost.

## Titulky

Devět jazyků, u všech nula řádků přes 42 znaků a nula třířádkových:

| kód | jazyk | titulků |
|---|---|---|
| `en-gb` | English (United Kingdom) | 198 |
| `cs` | čeština | 276 |
| `sv` | svenska | 276 |
| `es` | español | 277 |
| `pt-BR` | português (Brasil) | 274 |
| `de` | Deutsch | 277 |
| `fr` | français | 276 |
| `it` | italiano | 276 |
| `pl` | polski | 275 |

## Před nahráním

```bash
# délka a celistvost masteru
ffprobe -v error -show_entries format=duration -of default=nw=1:nk=1 \
        videos/020-who-runs-the-earth/render/final-en.mp4
ffmpeg -v error -i videos/020-who-runs-the-earth/render/final-en.mp4 -f null -
```

**Nahraj jako neveřejné a podívej se na to v přehrávači.** YouTube video
překóduje a jak vyjdou tmavé scény po jejich kompresi se dopředu posoudit
nedá — u tohohle videa je pozadí `#0c1220`, tedy skoro černá, a je toho
hodně. Je to jediný krok, který nejde udělat na disku.

## Odpovědi na pravděpodobné komentáře

Podklady jsou ve `factcheck.md`. Čtyři nejpravděpodobnější námitky:

| námitka | odpověď |
|---|---|
| „ICC přece vydal zatykač na hlavu státu" | ano — a na vlastních stránkách píše, že **nemá policii** a při zatýkání je odkázaný na spolupráci států. Zatykač vydat umí, zatknout ne |
| „Federation of Earth existuje" | existuje ústava přijatá 1977 v Innsbrucku nevládní organizací WCPA. Nikdy neplatila |
| „protokol pro první kontakt máme" | IAA/SETI Declaration (1989, revize 2010) říká, komu se to **oznámí** (generálnímu tajemníkovi OSN), a že se **neodpovídá**, dokud neproběhnou konzultace — jejichž postup je „předmětem samostatné dohody", která neexistuje. A je nezávazná |
| „na asteroid a pandemii koordinace je" | IAWN a SMPAG (2014) i WHO IHR (2005) jsou poradní a doporučující. Přesně ty koordinační mechanismy bez pravomoci, o kterých mluví kapitola 2 |
