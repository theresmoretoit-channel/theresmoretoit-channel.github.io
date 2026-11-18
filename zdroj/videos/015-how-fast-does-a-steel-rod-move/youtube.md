# Podklady k nahrání na YouTube

Scénář, překlady, obrázky i **master render jsou HOTOVÉ**. Časy kapitol
ověřené proti `work/timing.json`. Zbývá jediný krok: nahrát to.

`render/final-en.mp4` — **9:24, 84 scén, −14,0 LUFS / −1,1 dBTP, 38,7 MB**,
1920×1080 při 25 fps. Dekódovací test projde beze slova. Renderováno na
herním PC za **9,2 minuty** (3× supersampling, CRF 18).

---

## Titul

```
Nothing Is Really Solid — What Happens When You Push a Steel Rod?
```

Alternativa, kdyby se ukázala jako lepší v náhledu:
`How Fast Does a Steel Rod Actually Move?`

## Popis

```
Imagine a steel rod one million kilometres long. You push one end on Monday
morning. When does the other end start to move?

Not immediately. Not at the speed of light either. The answer is Wednesday
afternoon — about fifty-five hours later — and the reason takes us all the
way down to what matter is actually made of.

Along the way: why steel is not perfectly rigid, why a perfectly rigid
object cannot exist in this universe at all, why your hand never really
touches the table it is resting on, and why "solid" turns out to be a
description of behaviour rather than a property of the world.

Full transcript, sources and translations: https://theresmoretoit-channel.github.io/videos/how-fast-does-a-steel-rod-move/

Chapters
00:00 Push one end
00:18 The easy answer: light
00:44 A wave in the metal
01:10 Five kilometres a second
01:24 Fifty-five hours
01:40 But steel feels solid
01:59 The rod is not one thing
02:26 Zooming in on an atom
02:59 What holds it together
03:29 Why don't atoms collapse?
03:50 The Pauli exclusion principle
04:33 Your hand on a table
05:11 What touching really means
05:25 Could we make it faster?
06:04 A perfectly rigid rod
06:27 It would be a telegraph
06:53 Even light takes time
07:19 Look what we just did
07:50 What "solid" actually means
08:24 The same laws on both sides
08:55 Next time you touch a table

Subtitles are written for this video, not auto-generated. An American
English audio track is available as a second audio track.

There's more to it.
```

> **Kapitola „Nothing stands still" (S38, 4:16) vypuštěna.** Do další
> kapitoly jí zbývá **9 s** a YouTube uznává jen kapitoly od 10 s. Blok
> o kmitání tak spadá pod „The Pauli exclusion principle", což dává smysl —
> je to jeho pokračování.

## Nastavení

| položka | hodnota |
|---|---|
| soubor | `render/final-en.mp4` — 9:24, 38,7 MB |
| náhled | `render/thumbnail.jpg` — koncept **`c1b-when-will-it-react`**, 1280×720, 86 kB |
| **jazyk videa** | **`en-gb`** — nastavit PRVNÍ, jinak zůstane dlaždice „Titulky" zašedlá |
| titulky | `subtitles/*.srt` — **všech devět jazyků hotových** (159 anglických, 209–212 v překladech) |
| kategorie | Věda a technika |
| byla použita AI | **ne** — viz níž |
| pro děti | ne |

## Odpověď na dotaz „byla použita AI"

**Ne**, a drží to trojí:

- SDXL scény jsou díky kotvě stylu **malované ilustrace**, ne fotorealismus,
  a jsou už jen **dvě z osmdesáti čtyř**, tedy 2 % scén
- **žádný archivní snímek** — video nemá jediný, takže odpadá i otázka
  atribuce a `CREDITS.md` / `LICENSES.md` nevznikají
- hudba je **procedurální** (sinusovky a šum v numpy), ne z generativního modelu

Poměr zdrojů: **82 diagramů / 2 SDXL / 0 archivních.**

> Původně jich mělo být šest SDXL. Čtyři (S01, S40, S53, S76) model
> netrefil ve dvou kolech po sobě a Commons na devět dotazů nevrátil
> použitelnou náhradu, takže se překreslily — viz `notes.md`.

## Tagy

```
physics, speed of sound, steel, rigid body, relativity, quantum mechanics,
Pauli exclusion principle, what is solid, atoms, materials science,
electromagnetism, how it works, science explainer, thought experiment
```

## Před nahráním zkontrolovat

```bash
ffprobe -v error -show_entries format=duration -of default=nw=1:nk=1 \
        videos/015-how-fast-does-a-steel-rod-move/render/final-en.mp4
ffmpeg -v error -i videos/015-how-fast-does-a-steel-rod-move/render/final-en.mp4 -f null -
```

1. Dekódovací test musí projít **beze slova**.
2. Náhled do 2 MB, 1280×720.
3. **Nahrát jako neveřejné a podívat se na to v přehrávači** — YouTube video
   překóduje a jak vyjde tmavá scéna po jejich kompresi se dopředu posoudit
   nedá. Tohle video má tmavé pozadí u všech 82 diagramů, takže je to tady
   důležitější než jinde.
4. **Test & Compare** — YouTube umí porovnat až tři náhledy naráz.
   Připravené varianty leží v `render/thumb-*.jpg`:
   `c1-fifty-five-hours`, `c2-nothing-solid`, `c3-never-touch`.

> **Proč vyhrála otázka, a ne „55 HOURS".** Vybral uživatel: *„55 HOURS
> se mi líbí nejvíc, ale nechci divákovi vyzradit těch padesát pět hodin."*
> Sedí to i se stavbou videa — S02b az S02e drží otázku otevřenou
> (*„yes?" / „Well..." / „No."*) a číslo padne až v 1:24. Thumbnail
> s číslem by odpověděl dřív než scénář.
>
> Otázka má 30 znaků proti osmi, takže na jeden řádek nejde: při
> velikosti, která by se vešla, má v náhledu 210 px jen 11 px.
> Na dva řádky vyjde velikost 200, tedy **16 px v náhledu** proti
> 21 px u „55 HOURS" — menší, ale daleko nad hranicí čitelnosti.

## Do odpovědí v komentářích

Dvě věci z `factcheck.md`, na které se skoro jistě někdo zeptá:

**„Rychlost zvuku v oceli je přece 5 900 m/s, ne 5 000."**
To je *objemová* podélná rychlost v neomezeném prostředí. Pro dlouhou
tenkou tyč platí *tyčová* rychlost `√(E/ρ)` = 5 048 m/s, protože se
materiál může do stran roztáhnout. Video mluví o tyči, takže 5 km/s.

**„A co kdyby byl materiál ještě tužší?"**
Existuje horní mez plynoucí z fundamentálních konstant:
`v_u = α·√(mₑ/2mₚ)·c ≈ 36 100 m/s`, tedy asi dvojnásobek diamantu
a 0,012 % rychlosti světla. Trachenko, Monserrat, Pickard, Brazhkin,
*Speed of sound from fundamental physical constants*, Science Advances
**6**(41), eabc8662 (2020).

---

## Oba kroky na herním PC jsou HOTOVÉ

Obrázky i master render proběhly 2026-09-01 přes reverzní tunel
(`gamepc-tunel`). Zbývá jen nahrání podle tabulky „Nastavení" výš:
**jazyk videa `en-gb` jako první**, teprve potom titulky.

Kontrola před nahráním (musí projít beze slova):

```bash
ffmpeg -v error -i videos/015-how-fast-does-a-steel-rod-move/render/final-en.mp4 -f null -
```

> **Před uspáním herního PC ověř, že na něm nic neběží:**
> `ssh gamepc-tunel 'pgrep -x ffmpeg; pgrep -f render.py'`.
> Nad dvěma videy už běžela sezení paralelně třikrát.
