# Podklady pro nahrání na YouTube

Ručně psaný zdroj. Časy kapitol odpovídají masteru z `work/timing.json`
(celkem 9:10) — **po každém přegenerování hlasu je odvoď znovu**, protože
se posunou. Naposledy ověřeno 2026-08-26 proti `render/final-en.mp4`.

---

## Titul

```
Was There More Nonsense Before the Internet?
```

43 znaků. Limit je 100, mobil ukáže zhruba 60 — vejde se celý. Otázka, ne
tvrzení, tedy formát kanálu. Thumbnail nese údernou část (`TRUTH × LIES`),
titul tu vyhledatelnou, takže se neopakují.

Zvažované alternativy:

- `Were People in the Middle Ages Easier to Fool?` — 46 znaků, osobnější,
  ale svádí k odpovědi „ano", kterou video vyvrací
- `The Most Famous Mass Panic in History Never Happened` — 52 znaků, silné,
  ale slibuje celé video o Wellesovi, což je jen jeden blok ze šesti;
  navíc doslova opakuje thumbnail `c3`

---

## Popis

První dva řádky jsou jediné, co je vidět před „show more".

```
In the fourteenth century a traveller could tell you there was a monster in the
north, and you had no way to check. Today you can check anything in seconds — and
nonsense still travels further than the truth.

So were people back then more gullible than we are? This is the story of six
technologies that each made it faster to spread knowledge, and exactly as much
faster to spread nonsense: the spoken rumour, the printing press, the newspaper,
radio, the internet, and now AI. Along the way: a massacre justified by a lie the
Pope had already refuted, the most famous mass panic in history that never actually
happened, and a study of 126,000 stories that found the problem is not the bots.

Chapters
0:00 A monster in the north
0:36 Were people back then more stupid?
1:24 Lies with a purpose - Strasbourg, 1349
2:23 Print, newspapers, radio: the multiplier
3:12 The panic that never happened
4:20 The internet: the library and the pub
5:00 Why nonsense travels further
6:08 Too much information
6:22 What AI changes
7:26 So, were they more gullible?
8:25 The skill that actually matters

Main sources
Vosoughi, S., Roy, D., Aral, S. (2018). The spread of true and false news online.
  Science 359(6380), 1146-1151. https://doi.org/10.1126/science.aap9559
Pooley, J., Socolow, M. J. (2013). The Myth of the War of the Worlds Panic. Slate.
Dondi, C. (ed.) (2020). Printing R-Evolution and Society 1450-1500. Ca' Foscari.
Clement VI, bull Quamvis perfidiam, 26 September 1348.
Jakob Twinger von Koenigshofen, Strasbourg chronicle, on the massacre of 14 Feb 1349.
The Report of the Paris Medical Faculty, October 1348 (Compendium de epidemia).

Image credits
All archive images are in the public domain, via Wikimedia Commons. Full evidence
with SHA-256 fingerprints: sources.json / LICENSES.md in the project.

Marvels of the East: a man without knowledge of fire, a centaur (public domain)
  https://commons.wikimedia.org/wiki/File:A_Man_Without_Knowledge_of_Fire;_A_Man_Riding_a_Crocodile;_A_Centaur;_Sanrus_-_Google_Art_Project.jpg
Bayeux Tapestry, Halley's comet, scenes 32-33 - photo Myrabella (public domain)
  https://commons.wikimedia.org/wiki/File:Bayeux_Tapestry_32-33_comet_Halley_Harold.jpg
Burying plague victims of Tournai, Pierart dou Tielt, c. 1353 (public domain)
  https://commons.wikimedia.org/wiki/File:Doutielt1.jpg
Jews burned at the stake, medieval manuscript (public domain)
  https://commons.wikimedia.org/wiki/File:Jews_burned_at_stake,_manuscript.jpg
Early printing press, engraving by John Farey (public domain)
  https://commons.wikimedia.org/wiki/File:Printing_press.jpg
Orson Welles, 1938 - Regal Press, Inc. (public domain)
  https://commons.wikimedia.org/wiki/File:Orson-Welles-1938.jpg
Orson Welles press conference, Universal Newsreel, 31 October 1938 (public domain)
  https://commons.wikimedia.org/wiki/File:Universal_Newsreel_October_31,_1938_WOTW_Welles.jpg
Marvels of the East: Praesillus, a hairy woman of Gorgade (public domain)
  https://commons.wikimedia.org/wiki/File:Praesillus;_A_Hairy_Woman_of_the_Island_of_Gorgade;_A_Scorpion_-_Google_Art_Project.jpg

Subtitles are written for this video, not auto-generated. An American English
audio track is available as a second audio track. Music, diagrams and
illustrations: made for this video.
```

---

## Thumbnail — vybrán `c1-multiplier`

Všechny tři jsou kreslené kódem (`thumbnail/gen.py` nad `tools/svgkit.py`)
a ověřené zmenšením na **210 px i 150 px** — v obou se hlavní slova čtou.

| koncept | objekt | slova | paradox |
|---|---|---|---|
| **`c1-multiplier`** | velké ambrové × | `TRUTH × LIES` | technologie násobí obojí stejně — klíčový obraz videa (S21, vrací se v S57) |
| `c2-same-monster` | psí hlava z profilu v displeji telefonu | `SAME MONSTER / NEW PIPE` | středověká příšera v moderní trubce |
| `c3-never-happened` | rádio z roku 1938 | přeškrtnuté `PANIC`, `IT NEVER HAPPENED` | nejslavnější masová panika se nestala |

```bash
python videos/004-disinformation-then-and-now/thumbnail/gen.py     # SVG
python tools/thumbnail.py videos/004-disinformation-then-and-now \
       --svg thumbnail/c1-multiplier.svg --bg none --out render/thumb-c1-multiplier.jpg
```

**Uživatel vybral `c1`** (2026-08-26). Volba je zapsaná v `project.json` →
`thumbnail`, takže `python tools/thumbnail.py videos/004-disinformation-then-and-now`
bez dalších parametrů vyrobí právě ji do `render/thumbnail.jpg`
(1280×720, 67 kB, tedy hluboko pod limitem YouTube 2 MB).

Důvod volby: ve 150 px se čte nejlíp ze všech tří, drží se obrazu, který ve
videu dvakrát padne, a nekonkuruje titulu. `c2` má slabinu v tom, že popiska
`IN THE NORTH` je v náhledu jen šmouha; `c3` je nejpřesnější, ale nejužší —
slibuje video o Wellesovi.

`c2` a `c3` zůstávají v `thumbnail/` jako varianty a leží vyrobené
v `render/thumb-c2-same-monster.jpg` a `render/thumb-c3-never-happened.jpg`.
YouTube umí „Test & Compare" až se třemi, takže jde nasadit všechny.

## Tagy

```
disinformation, misinformation, media history, fake news, Orson Welles,
War of the Worlds panic, printing press, Black Death, Strasbourg 1349,
artificial intelligence, fact checking, information literacy, history explained
```

---

## Titulky — devět jazyků

| kód | jazyk | zdroj | titulků |
|---|---|---|---|
| `en` | English (United Kingdom) | `script.md` | 145 |
| `cs` | čeština | `script.cs.md` | 208 |
| `sv` | svenska | `script.sv.md` | 210 |
| `es` | español | `script.es.md` | 210 |
| `pt-BR` | português (Brasil) | `script.pt-BR.md` | 210 |
| `de` | Deutsch | `script.de.md` | 210 |
| `fr` | français | `script.fr.md` | 210 |
| `it` | italiano | `script.it.md` | 210 |
| `pl` | polski | `script.pl.md` | 209 |

```bash
for l in cs sv es pt-BR de fr it pl; do
  python tools/subtitles.py videos/004-disinformation-then-and-now --lang $l
done
```

Ověřeno u všech devíti: **žádný řádek přes 42 znaků, žádný třířádkový
titulek, útržků 0–3 %, nejkratší titulek 0,96 s.**

> Překlady jsou strojové (moje) a čtené řádek po řádku proti originálu.
> Hlídaná místa u tohohle videa jsou **čísla**: 28 000 vydání, 5 000
> domácností, 2 %, 126 000 zpráv, 70 %, 1 500 lidí, 100 000, rok 1349 a 1938.
> Ověřeno ve všech osmi jazycích vedle sebe.
>
> Při čtení se našly a opravily čtyři vlastní chyby: švédština psala
> číslovky zvlášť (`tjugoåtta tusen` → `tjugoåttatusen`), polština měla
> u `około` špatný pád (`dwadzieścia osiem tysięcy` → `dwudziestu ośmiu
> tysięcy`). **Strukturální kontrola ani jednu z nich nechytí** — je to
> přesně ta past z CLAUDE.md, že počty řádků nedokazují nic o obsahu.

## Nastavení při nahrání

Nejsou to soubory, klikají se ve webu:

- **jazyk videa: English (United Kingdom)** — hlas je `bf_emma` / `en-gb`.
  Nastavit **dřív** než titulky, jinak zůstane dlaždice „Titulky" zašedlá.
- titulky: nahrát ručně všech devět `.srt`, ať se nepoužije automatický přepis
- kategorie: Education (u předchozích videí Science & Technology — tohle je
  spíš mediální gramotnost než technika)
- „není určeno dětem"
- nahrát jako **neveřejné a přehrát si to v přehrávači** — YouTube video
  překóduje a jak vyjdou tmavé scény po jejich kompresi, se na disku posoudit
  nedá. Je to jediný krok, který nejde udělat lokálně.

| co | odkud |
|---|---|
| video | `render/final-en.mp4` — 9:10, 74 MB, −14,0 LUFS / −1,3 dBTP |
| náhled | `render/thumbnail.jpg` — 1280×720, 67 kB, limit YouTube je 2 MB |
| titulky | `subtitles/*.srt`, devět jazyků |
| atribuce | `CREDITS.md` (generuje `archive.py`) |

---

## Označení AI obsahu — odpověď zní NE

Rozhoduje fotorealističnost, ne použití AI
([pravidla](https://support.google.com/youtube/answer/14328491)). U tohohle
videa drží odpověď „ne" tři věci:

- **SDXL scény jsou malované ilustrace**, ne fotorealismus — kotva stylu zní
  *painterly documentary illustration, muted desaturated palette*. Je jich
  pět z 62 (S01, S30, S36, S48, S53) a všechny jsou atmosférické.
- **S48 je záměrně rozpadající se malba.** Scéna mluví o svědkovi, který
  neexistuje; fotorealistický obličej by odpověď překlopil na „ano".
- **archivních snímků je osm a jsou upravené jen barevně** — *„color
  adjustment or lighting filters"* je výslovná výjimka v pravidlech.
- **hudba je procedurální** (sinusovky a šum v numpy), ne z generativního
  modelu. Suno/Udio by odpověď překlopilo, protože pravidla jmenují
  „AI-generated music" přímo.

---

## Licence — prověřeno 2026-08-26

Všech osm archivních snímků je **public domain z Wikimedia Commons**, každý
má záznam v `sources.json` a otisk SHA-256 originálu v `LICENSES.md`.
Komerční užití včetně monetizace je bez podmínek; uvedení autora u těch,
kde je znám (Myrabella, Pierart dou Tielt, John Farey, Universal Newsreel,
Regal Press), je slušnost, ne povinnost.

```bash
python tools/archive.py videos/004-disinformation-then-and-now --evidence
```

Žádný snímek od NASA tu není, takže odpadá i výhrada, která visela nad
prvním videem. Logo NASA do thumbnailu stejně nepatří — volné není.
