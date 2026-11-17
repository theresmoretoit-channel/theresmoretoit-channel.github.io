# Podklady k nahrání — 026 Does Copyright Hold Back Progress?

> **NAHRÁNO 5. 9. 2026.** Odkaz a číslo patří do `Témata.ods`,
> ne sem — stavové věty v repozitáři zastarávají.

Soubory:

| co | odkud |
|---|---|
| video | `render/final-en.mp4` — 9:25, 1920×1080, 44,2 MB |
| náhled | `render/thumbnail.jpg` — 1280×720, 0,36 MB (limit 2 MB) |
| titulky | `subtitles/*.srt` — devět jazyků |

**Napřed nastav jazyk videa na `en-gb`**, jinak zůstane dlaždice
„Titulky" zašedlá. Hlas je `bf_emma`, tedy britská angličtina.

---

## 1. Titul

```
Does Copyright Hold Back Progress?
```

Alternativy, kdyby se chtělo něco konkrétnějšího do seznamu:

- `The Song That Nobody Can Use`
- `Why a 1928 Cartoon Was Locked Up for 95 Years`

---

## 2. Popis

**Zkopíruj celý blok mezi apostrofy. Nic mimo něj se na YouTube
nedostane — atribuce je uvnitř schválně.**

```
A recording from 1950. Nobody sells it. The label is gone. The musician
died long ago. And you still may not be allowed to use ten seconds of it.

Copyright was built as a trade: a temporary monopoly in exchange for more
creation. This video asks what happens when "temporary" turns out to mean
the life of the author plus seventy years — and what that costs the people
who want to build on what already exists.

Along the way: why a song is not one thing, what the Blurred Lines dissent
actually warned about, why copying a games console's code counted as fair
use in 1992, what Google v. Oracle turned on, and why compulsory licensing
is not a thought experiment — it has been law since 1909.

CHAPTERS
0:00 A recording nobody can use
0:40 Why copyright exists
1:15 How long is "temporary"?
2:00 Progress does not start from zero
2:26 Music: one song, many owners
3:14 Blurred Lines and the dissent
3:50 Software has the same problem
4:02 Reverse engineering
4:30 Google v. Oracle
4:57 Orphan works
5:50 Should we abolish copyright?
6:25 Compulsory licensing, since 1909
7:08 Transformation is not copying
7:33 And then AI arrives
8:20 The trade-off
8:50 What it leaves for tomorrow

Subtitles are written for this video, not auto-generated. An American
English audio track is available as a second audio track.

IMAGE CREDITS
Mickey Mouse in Steamboat Willie (1928) — Walt Disney / Ub Iwerks,
public domain, via Wikimedia Commons.
Elvira Donnarumma at her home (1930) — unknown photographer,
public domain, via Wikimedia Commons.
All other visuals are drawn for this video.
```

> **Proč je atribuce uvnitř bloku:** naměřeno napříč kanálem, že
> u čtyř videí ze šestnácti chyběla, a pokaždé proto, že kredity byly
> jako poznámka **pod** blokem. U videa o autorském právu by to byl
> vlastní protipříklad.

> **Oba snímky jsou public domain**, takže atribuce právně povinná není
> — je tam z poctivosti a protože jde o video o autorském právu.
> `CREDITS.md` se do popisu nevkládá celý: má české popisky polí,
> hvězdičky a rozsypaný `title` z multijazyčné šablony Commons.

---

## 3. Tagy

```
copyright, intellectual property, public domain, orphan works, fair use, compulsory licensing, copyright term, Berne Convention, Steamboat Willie, Blurred Lines, Google v Oracle, Sega v Accolade, reverse engineering, sampling, music copyright, software copyright, AI training copyright, generative AI, copyright reform, remix culture, explainer, video essay, popular science, there's more to it
```

> **Prvních pár tagů váží nejvíc**, takže vpředu stojí obecné téma
> a vzadu formát. Jmenné kotvy (`Steamboat Willie`, `Blurred Lines`,
> `Google v Oracle`) jsou tam schválně: jsou to věci, které lidé hledají
> samy o sobě, a video na ně skutečně odpovídá — tag, který slibuje něco,
> co ve videu není, si kanál zavírá dveře podruhé.

---

## 4. Nastavení

| pole | hodnota |
|---|---|
| jazyk videa | **`en-gb`** |
| kategorie | Věda a technika |
| **byla použita AI?** | **NE** — viz níž |
| titulky | nahrát všech devět `.srt` |
| kapitoly | v popisu, první na `0:00`, šestnáct, všechny ≥ 10 s |

### Odpověď na dotaz „byla použita AI" je NE

Rozhoduje **fotorealističnost, ne použití AI**:

- **69 scén ze 75 jsou diagramy kreslené kódem** (SVG přes Inkscape)
- **4 SDXL scény** jsou malované ilustrace s kotvou stylu, ne fotorealismus
- **2 archivní snímky** jsou upravené jen barevně — *„color adjustment or
  lighting filters"* je výslovná výjimka pravidel
- hudba je **procedurální** (sinusovky a šum v numpy), ne z generativního
  modelu
- hlas je Kokoro, tedy syntéza — **ne klon skutečné osoby**

### Ochranná známka: pozor na S16

Commons hlásí u **všech** snímků ze Steamboat Willie
`restrictions = trademarked`. Autorské právo k filmu z roku 1928 vypršelo
1. 1. 2024, **ochranná známka k postavě ne**. Do videa to smí (redakční
užití, film je jmenován), ale **do náhledu ani do brandingu kanálu ne** —
tatáž hranice jako u loga NASA.

---

## 5. Před nahráním

```bash
ffprobe -v error -show_entries format=duration -of default=nw=1:nk=1 \
        videos/026-does-copyright-hold-back-progress/render/final-en.mp4
```

**Nahraj jako neveřejné a podívej se na to v přehrávači.** YouTube video
překóduje a jak vyjdou tmavé diagramy po jejich kompresi se dopředu
posoudit nedá. Je to jediný krok, který nejde udělat na disku.

### Naměřeno na masteru

| | |
|---|---|
| délka | 565,68 s = **9:25** |
| integrovaná hlasitost | **−14,0 LUFS** |
| true peak | **−1,3 dBTP** |
| dekódovací test `ffmpeg -f null -` | prošel **beze slova** |
| ID scén v obraze | **žádné** (ověřeno porovnáním rohu s draftem) |

---

## 6. Náhled

**Hotový obrázek od uživatele**, druhý takový na kanále (první u 024).
Původ, otisk a rozbor jsou v `thumbnail/PUVOD.md`.

| veličina | tento | pásmo 25 vydaných | |
|---|---|---|---|
| **jas** | **82,2** | 20,3 az 115,7 | druhý nejsvětlejší z 26 |
| **kontrast** | **86,9** | 35,5 az 92,6 | u horní hranice |
| saturace | 40,3 | 39,1 az 62,9 | u dolní hranice |

Ve 150 px se přečte `COPYRIGHT` i otázka. Nápis na zdi a tři cedule
čitelné nejsou — **nesou to texty, obraz je textura**. Přebytečné vrstvy
nic nepopírají, jen nic nepřidávají.

## 7. Zbývá

- [ ] závěrečná obrazovka a karty: **poslední scéna je na ně navržená**
      (S73, klidná deska, žádný text v dolní třetině ani vpravo)
