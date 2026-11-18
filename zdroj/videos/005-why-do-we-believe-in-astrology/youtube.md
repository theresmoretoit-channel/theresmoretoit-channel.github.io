# Podklady pro nahrání na YouTube

Ručně psaný zdroj. Časy kapitol odpovídají `work/timing.json` (celkem 12:52), ověřeno 2026-08-27.
**Po každém přegenerování hlasu je odvoď znovu** — po každém
přegenerování hlasu je odvoď znovu, protože se posunou.

---

## Titul

```
Why Do We Believe in Astrology?
```

30 znaků. Limit je 100, mobil ukáže zhruba 60 — vejde se celý. Otázka, ne
tvrzení, tedy formát kanálu.

Titul vybral uživatel a **opravil tím oblouk videa**. Pracovní název zněl
*„Why Astrology Is Complete Bullshit"*; ten slibuje devět sekcí vyvracení
a závěr o mozku je pak přívěsek. Tenhle slibuje přesně to, čím video končí.
Sprosté slovo v titulku navíc omezuje dosah i monetizaci.

Zvažované alternativy:

- `Why Can't Astrologers Agree On Your Sign?` — 41 znaků, konkrétnější,
  ale slibuje jen první polovinu videa
- `What Is Your Star Sign Actually?` — 31 znaků, slabší, nenese pointu

---

## Popis

První dva řádky jsou jediné, co je vidět před „show more".

```
Your horoscope says you are a Leo. Indian astrology says you are a Cancer. Both
systems are practised today, and they disagree about four people out of every five.

That is not the strange part. The strange part is that a description written for
everybody can still feel like it was written for you. This video starts with a
thirteenth constellation the zodiac quietly leaves out, works through what a sign
actually is once you notice it is not a constellation, and ends up somewhere more
interesting than astrology: the machinery in your head that finds meaning in noise.

Along the way: a psychologist who handed thirty-nine students the same personality
profile and got an average score of 4.26 out of 5, a double-blind test in Nature
that the astrologers themselves helped design, and why one experiment is never the
last word — including that one.

Full transcript, sources and translations: https://theresmoretoit-channel.github.io/videos/why-do-we-believe-in-astrology/

Chapters
0:00 A question about your star sign
0:29 The thirteenth constellation
1:41 Signs are not constellations
2:05 So what is a sign?
2:47 Two schools, two answers
3:43 How a horoscope is calculated
4:55 Gravity carries no message
5:21 Why the exact moment of birth?
6:04 Your horoscope is always accurate
7:29 Being fair to astrologers
8:29 Putting it to the test
9:07 One experiment is never the last word
10:26 Why we are so good at this
11:09 What we found
11:59 The fascinating part

Main sources
Carlson, S. (1985). A double-blind test of astrology. Nature 318, 419-425.
  https://doi.org/10.1038/318419a0
Forer, B. R. (1949). The fallacy of personal validation: A classroom demonstration
  of gullibility. Journal of Abnormal and Social Psychology 44(1), 118-123.
Dean, G., Kelly, I. W. (2003). Is astrology relevant to consciousness and psi?
  Journal of Consciousness Studies 10(6-7), 175-198.
Ertel, S. (2009). Appraisal of Shawn Carlson's renowned astrology tests.
  Journal of Scientific Exploration 23(2), 125-137.
IAU constellation boundaries (Delporte, 1930) for the thirteen constellations
  the ecliptic crosses.
Lahiri (Chitrapaksha) ayanamsa, the standard adopted by the Indian Astronomical
  Ephemeris: 24 degrees 13 minutes for 2026.

Image credits
All archive images are in the public domain or CC BY-SA, via Wikimedia Commons.
Full evidence with SHA-256 fingerprints: sources.json / LICENSES.md in the project.

Urania's Mirror: Taurus Poniatowski, Serpentarius, Scutum Sobiesky and Serpens,
  Sidney Hall, 1824, restored by Adam Cuerden (public domain)
  https://commons.wikimedia.org/wiki/File:Sidney_Hall_-_Urania%27s_Mirror_-_Taurus_Poniatowski,_Serpentarius,_Scutum_Sobiesky,_and_Serpens.jpg
Iranian astrolabe - photograph by Masoud Saf, uploaded by Jacopo Koushan
  (CC BY-SA 3.0)
  https://commons.wikimedia.org/wiki/File:Iranian_Astrolabe_14.jpg
Alfonsine table in BnF lat. 7432, Conrad Heingartner (public domain)
Horoscope of James King, born 6 December 1764, printed 1792, C. Heydon
  (public domain)

Subtitles are written for this video, not auto-generated. An American English
audio track is available as a second audio track. Music, diagrams and
illustrations: made for this video.
```

> **Serpentarius je historické jméno Hadonoše** a v atribuci se musí nechat
> tak, jak stojí na stránce Commons — jinak otisk SHA-256 nesedí na název.

---

## Označení AI obsahu — odpověď je NE

Drží ji tři věci, stejně jako u předchozích videí:

- **5 SDXL scén ze 76** a všechny jsou malované ilustrace, ne fotorealismus.
  `sdxl.negative` má `photorealistic, photograph, photo, 3d render` právě proto.
- **4 archivní snímky** upravené jen barevně — *„color adjustment or lighting
  filters"* je v pravidlech YouTube výslovná výjimka.
- **Hudba je procedurální** (`tools/music.py`, sinusovky a šum v numpy),
  ne z generativního modelu.

Vypravěčka je Kokoro `bf_emma`, tedy **ne klon skutečné osoby**.

---

## Tagy

```
astrology, horoscope, zodiac, Ophiuchus, star signs, Barnum effect, Forer effect,
precession, sidereal astrology, tropical zodiac, science, skepticism,
cognitive bias, pattern recognition, does astrology work
```

---

## Nastavení při nahrávání

1. **Napřed jazyk videa** — `en-gb`, protože hlas je `bf_emma`. Bez toho
   zůstane dlaždice „Titulky" zašedlá.
2. **Kapitoly** uzná YouTube, jen když první začíná na `00:00`, jsou aspoň
   tři a každá trvá ≥ 10 s. Časy ber z `work/timing.json`.
3. **Nahrát jako neveřejné a podívat se na to v přehrávači.** Tohle video má
   hodně tmavých diagramů s tenkými čárami — jak je YouTube překóduje, se
   dopředu posoudit nedá. Je to jediný krok, který nejde udělat na disku.

Kontrola před nahráním:

```bash
ffprobe -v error -show_entries format=duration -of default=nw=1:nk=1 \
        videos/005-why-do-we-believe-in-astrology/render/final-en.mp4
ffmpeg -v error -i videos/005-why-do-we-believe-in-astrology/render/final-en.mp4 -f null -
```

Druhý příkaz musí projít **beze slova** — `ffprobe` přečte délku z kontejneru
i u rozsypaného streamu.

---

## Thumbnail — tři koncepty, čeká na výběr

Všechny tři jsou kreslené kódem (`thumbnail/gen.py` nad `tools/svgkit.py`)
a ověřené zmenšením na **210 px i 150 px** — v obou se hlavní slova čtou.

| koncept | objekt | slova | paradox |
|---|---|---|---|
| `c1-two-signs` | dvě šipky z jednoho data | `LEO` / `CANCER` | dva živé systémy, dvě různá znamení téhož člověka — obraz, který ve videu padne třikrát (S03, S18, S57) |
| `c2-thirteenth` | dvanáctidílný kruh a jeden díl navíc | `13` | třináctý znak, který se do úhledného kruhu nevejde |
| `c3-not-the-stars` | otazník složený z hvězd | `IT IS NOT THE STARS` | odpověď na titul: příčina není na obloze |

```bash
python videos/005-why-do-we-believe-in-astrology/thumbnail/gen.py
python tools/thumbnail.py videos/005-why-do-we-believe-in-astrology \
       --svg thumbnail/c1-two-signs.svg --bg none --out render/thumb-c1-two-signs.jpg
```

Leží vyrobené v `render/thumb-*.jpg` (49–72 kB, hluboko pod limitem 2 MB).
YouTube umí „Test & Compare" až se třemi, takže jde nasadit všechny.

> **c3 se kreslil dvakrát.** První verze měla pod otazníkem ještě siluetu
> hlavy; ve 150 px z ní byla šmouha a text zmizel úplně. Objekt musí být
> **jeden a velký**, jinak thumbnail nese text a ne obraz.

**Až bude vybráno**, zapsat do `project.json` → `thumbnail`.

---

## Titulky — devět jazyků

| kód | jazyk | zdroj | titulků | útržky |
|---|---|---|---|---|
| `en` | English (United Kingdom) | `script.md` | 214 | 1 % |
| `cs` | čeština | `script.cs.md` | 308 | 3 % |
| `sv` | svenska | `script.sv.md` | 309 | 2 % |
| `es` | español | `script.es.md` | 311 | 1 % |
| `pt-BR` | português (Brasil) | `script.pt-BR.md` | 310 | 2 % |
| `de` | Deutsch | `script.de.md` | 311 | 0 % |
| `fr` | français | `script.fr.md` | 310 | 1 % |
| `it` | italiano | `script.it.md` | 310 | 1 % |
| `pl` | polski | `script.pl.md` | 308 | 3 % |

U všech nula řádků přes 42 znaků a nula třířádkových titulků.

> **Past s číslovkami ohlídána.** Britská *billion* je 10⁹, takže
> `mil millones` (ne *billones*), `bilhão`, `Milliarde`, `miljard`,
> `milliard`, `miliardo`, `miliard`. Ověřeno ve všech osmi.

> **Záměrné opakování ohlídáno.** Anglicky padne dvakrát *„It does not"*
> a to opakování je záměr. V polštině a brazilské portugalštině se ztratilo
> (dvě různá slovesa) — opraveno na dvakrát totéž.

## Zbývá doplnit

- **Thumbnail** — vybrán `c2-thirteenth`, zapsán v `project.json`
- ~~Titulky~~ — **hotovo, devět jazyků**
- **Odkaz na video** po zveřejnění
