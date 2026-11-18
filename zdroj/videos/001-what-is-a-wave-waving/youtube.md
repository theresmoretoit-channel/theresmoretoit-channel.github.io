# Podklady pro nahrání na YouTube

Ručně psaný zdroj. Časy kapitol odpovídají renderu z `work/timing.json`
(celkem 10:04) — **po každém přegenerování hlasu je potřeba je znovu odvodit**,
protože se posunou.

---

## Titul

```
What Is a Radio Wave Actually Travelling Through?
```

49 znaků. Limit je 100, mobil ukáže zhruba 60 — vejde se bez oříznutí. Otázka, ne tvrzení — odpovídá
formátu kanálu.

> Sjednoceno na britské `Travelling` (2026-08-24) — v `project.json`,
> `script.md` i `factcheck.md`. Hlas je `bf_emma` / `en-gb` a scénář drží
> britský pravopis (`metre`, `kilometres`), takže titul se mu teď neprotiví.
> Nadpis ve `script.md` se nenamlouvá, takže hlas se přegenerovat nemusí.

Zvažované alternativy:

- `A Radio Signal Crosses Empty Space. What Exactly Is Waving?` — 58 znaků
- `The Question Physics Answered by Deleting the Question` — chytřejší, ale míň hledané

Thumbnail říká „WHAT WAVES?", takže titul to nemá opakovat — nese popisnou
a vyhledatelnou část, thumbnail tu údernou.

---

## Popis

První dva řádky jsou to jediné, co je vidět před „show more". Zbytek je pro ty,
kdo rozkliknou.

```
A radio signal crosses hundreds of millions of kilometres of empty space and still
arrives. Every wave I can picture needs something to wave — so what is this one waving?

The nineteenth century had an answer: the luminiferous ether. This is the story of how
that answer was tested, abandoned, and replaced by something stranger — and why the
replacement still doesn't quite feel like an answer.

Full transcript, sources and translations: https://theresmoretoit-channel.github.io/videos/what-is-a-wave-waving/

Chapters
0:00 The question
0:37 The ether
1:15 Electricity and magnetism turn out to be connected
2:14 Maxwell's missing piece
3:34 The number that gave it away
4:00 Hertz finds the waves
4:46 Why the ether disappeared
5:24 One phenomenon, many names
6:28 Why we don't build antennas for light
7:09 Why the signal survives the journey
8:37 So what is actually waving?

Sources and image credits
All archive images are public domain, CC0, or NASA material used under NASA's
media usage guidelines. Full evidence: sources.json / CREDITS.md in the project.

Juno approaching Jupiter (artist concept) - NASA/JPL-Caltech
  https://images.nasa.gov/details/PIA20702
Michelson-Morley experiment, 1887 - Case Western Reserve University (public domain)
  https://commons.wikimedia.org/wiki/File:Michelson_morley_experiment_1887.jpg
Michael Faraday, portrait by Thomas Phillips, 1841-42 (public domain)
  https://commons.wikimedia.org/wiki/File:Thomas_Phillips_(1770-1845)_-_Michael_Faraday_-_NPG_269_-_National_Portrait_Gallery.jpg
James Clerk Maxwell, gravure after Stodart/Fergus (CC0)
  https://commons.wikimedia.org/wiki/File:James_Clerk_Maxwell_gravure.jpg
Hertzian spark-gap transmitter and receiver, before 1912 (public domain)
  https://commons.wikimedia.org/wiki/File:Hertzian_spark_gap_transmitter_and_receiver.png
Heinrich Hertz, c. 1890 - Robert Krewaldt, Bonn (public domain)
  https://commons.wikimedia.org/wiki/File:HEINRICH_HERTZ.JPG
Albert A. Michelson (Harris & Ewing, 1918) and Edward W. Morley (c. 1880), public domain
  https://commons.wikimedia.org/wiki/File:Albert_Abraham_Michelson_1918.jpg
  https://commons.wikimedia.org/wiki/File:Edward_Williams_Morley2.jpg
Deep Space Network antennas, Madrid - MDSCC/INTA, Francisco "Paco" Moreno
  https://images.nasa.gov/details/PIA26147
Deep Space Network, Goldstone - NASA/JPL-Caltech
  https://images.nasa.gov/details/PIA23214
Deep Space Network antenna - NASA/JPL-Caltech
  https://images.nasa.gov/details/PIA24163

Subtitles are written for this video, not auto-generated. An American English
audio track is available as a second audio track. Music and diagrams: made for
this video.
```

---

## Thumbnail

**Zvolený: `c6b-what-waves`** — triptych AIR / WATER / SPACE, kde táž vlna
pokračuje i třetím panelem, ve kterém není v čem se vlnit. Nadpis `WHAT WAVES?`,
druhé slovo ambrové.

```bash
python tools/thumbnail.py videos/001-what-is-a-wave-waving   # -> render/thumbnail.jpg
```

Volba je zapsaná v `project.json` → `thumbnail`, takže příkaz bez parametrů
vyrobí právě ji. Ostatních šest konceptů zůstává v `thumbnail/` jako varianty
(`c1`–`c6`); vyrobí se předáním `--svg` a `--bg`.

Ověřeno zmenšením na 210 px i 150 px — v obou se nadpis i popisky panelů čtou.
102 kB, tedy hluboko pod limitem YouTube 2 MB.

> Kdybys chtěl porovnat víc variant na skutečném publiku, YouTube umí
> „Test & Compare" až se třemi thumbnaily.

## Tagy

```
radio waves, electromagnetism, Maxwell's equations, luminiferous ether,
Michelson-Morley, Heinrich Hertz, electromagnetic field, speed of light,
electromagnetic spectrum, quantum field theory, physics explained, science
```

---

## Titulky — devět jazyků

| kód | jazyk | zdroj |
|---|---|---|
| `en` | English (United Kingdom) | `script.md` |
| `cs` | čeština | `script.cs.md` |
| `sv` | svenska | `script.sv.md` |
| `es` | español | `script.es.md` |
| `pt-BR` | português (Brasil) | `script.pt-BR.md` |
| `de` | Deutsch | `script.de.md` |
| `fr` | français | `script.fr.md` |
| `it` | italiano | `script.it.md` |
| `pl` | polski | `script.pl.md` |

```bash
for l in cs sv es pt-BR de fr it pl; do
  python tools/subtitles.py videos/001-what-is-a-wave-waving --lang $l
done
```

Video se kvůli tomu nesahá — časy se přebírají z anglického zarovnání, takže
další jazyk je jeden přeložený soubor a jeden příkaz. Žádné namlouvání,
žádný render.

Ověřeno u všech devíti: **žádný řádek přes 42 znaků, žádný třířádkový titulek,
žádný překryv, nic za koncem videa, nejkratší titulek 1,20 s.**

> Překlady jsou strojové (moje). U jazyků, které umím posoudit, jsem hlídala
> odbornou terminologii — `Verschiebungsstrom`, `courant de déplacement`,
> `prąd przesunięcia`, `förskjutningsström`. Past, na kterou pozor u dalších
> videí: **anglické *trillion* je 10¹², tedy německy `Billionen` a španělsky
> `billones`, ne „trillionen"/„trillones"** — jinak je číslo o šest řádů vedle.

## Nastavení při nahrání

Nejsou to soubory, klikají se ve webu:

- jazyk videa: **English (United Kingdom)** — hlas je `en-gb`
- titulky: nahrát ručně, ať se nepoužije automatický přepis
- kategorie: Science & Technology
- „není určeno dětem"
- playlist, koncová obrazovka

---

## Licence — prověřeno 2026-08-24

Všech deset archivních snímků má evidenci v `sources.json` a každý byl
**ověřen bajt po bajtu** proti originálu v `archive-raw/`. Komerční užití
(tedy i monetizace) je u všech možné, ale ze dvou různých důvodů:

**Šest z Wikimedia — bez podmínek.** S06, S10, S21, S22, S24 mají
`Copyrighted: False`, S14 je CC0. Pole `Restrictions` je u všech prázdné.
Uvedení autora není právní povinnost, jen slušnost.

> U S10 (Faraday) jde o fotoreprodukci obrazu z National Portrait Gallery.
> NPG si na reprodukce děl ve volném díle historicky nárokovala vlastní
> autorské právo, ale **článek 14 směrnice EU 2019/790** říká výslovně, že
> rozmnoženiny volných výtvarných děl chráněné nejsou. V EU je to tedy uzavřené.

**Čtyři od NASA — pod jejich pravidly.** Ta znějí:

> „NASA content used in a factual manner that does not imply endorsement may be
> used without needing explicit permission. NASA should be acknowledged as the
> source of the material."

Obě podmínky video splňuje: užití je věcné a popisek NASA uvádí jako zdroj.

**S33 je z těch deseti nejslabší článek.** Credit zní `MDSCC/INTA, Francisco
"Paco" Moreno` — MDSCC je madridská stanice provozovaná španělskou agenturou
INTA, ne NASA, takže to není dílo zaměstnance vlády USA a volným dílem není
automaticky. Proti tomu stojí druhá věta z týchž pravidel NASA:

> „NASA occasionally uses copyright-protected material of third parties with
> permission… Those images will be marked identified as copyright protected
> with the name of the copyright holder."

Stránka PIA26147 **žádné takové označení nemá** — je tam jen `Credits:`, nikde
`©` ani „copyright protected". Podle vlastního pravidla NASA tedy spadá pod
obecné svolení. Je to obhajitelné, ale je to úsudek, ne doklad.

Kdyby to mělo být bez pochybností, existuje náhrada s čistým creditem:
**„70m Antenna at Goldstone, California", NASA/JPL** — ve storyboardu stačí
u S33 změnit `query` na `Goldstone antenna dish` a `pick` na `1`.

**Past, na kterou pozor u thumbnailu:** logo NASA (meatball i worm) volné
**není** a jeho užití vyžaduje souhlas. Do thumbnailu ani do brandingu kanálu
nepatří, i když samotné snímky použít lze.
