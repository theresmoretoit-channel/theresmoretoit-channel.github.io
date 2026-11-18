# Podklady pro YouTube — 043

Nahrává se `render/final-en.mp4` (master, ne draft), `render/thumbnail.jpg`
a `subtitles/*.srt` v devíti jazycích. Lokalizované názvy a popisy jsou
v `youtube-preklady.md` a nahrává je `tools/lokalizace.py`.

## 1. Titul

```
Why Do Maps Lie To Us?
```

22 znaků. Limit je 100, mobil ukáže zhruba 60 — vejde se bez oříznutí.

**Proč wh-otázka.** Naměřeno na 29 videích kanálu s aspoň sto
zobrazeními: **wh-otázka 2,23 % vážené CTR, tvrzení 1,63 %, ano/ne
otázka 1,21 %.** Pracovní název `Maps Are Lying` je tvrzení a navíc
říká pointu rovnou.

**Proč ne `Why Does Greenland Look So Big?`** (což tu stálo do
2026-09-14). Ten titul byl taky wh-otázka, takže v CTR kategorii se nic
nemění — rozhodly dvě jiné věci, obě na návrh uživatele:

1. **Náhled už Grónsko nese** (GREENLAND / BIGGER THAN AFRICA?). Když
   ho řekne i titul, dvojice se **opakuje místo aby se doplňovala**.
   Takhle dodá náhled konkrétní hook a titul rozsah.
2. **Slibovat Grónsko je nepoctivé vůči obsahu.** Dvě třetiny videa
   jsou o globusu, reprezentaci a mapě metra; Grónsko je návnada,
   která je dopovězená v 0:28.

> **Cena té volby:** `why does greenland look so big` je vyhledávaná
> fráze, kdežto `why do maps lie` míň. **Objem vyhledávání ale změřit
> neumím** — kanál na to nemá data a Analytics API dotazy nerozpadá,
> takže tohle je úvaha, ne měření.

## 2. Popis

**Kopíruje se CELÝ blok mezi apostrofy a nic jiného.**

```
Look at a world map. Greenland sits up there next to Canada, about the
same size as Africa. Except Africa is fourteen times larger, and the map
is not making a mistake — it is doing exactly what it was built to do.

Every flat map of the Earth has to lie. Not by accident, by necessity.
In 1827 Carl Friedrich Gauss proved it: the curvature of a surface
belongs to the surface itself, so you cannot flatten a sphere without
stretching or tearing it. Cartographers stopped trying and started
choosing which lie to tell instead.

Mercator chose navigation, and the price is arithmetic. Oslo covers four
times the area it has. The middle of Greenland, ten times. The northern
tip, more than eighty. Greenland is smaller than the Congo and smaller
than Algeria, and South America — which looks smaller on that map — is
more than eight times bigger.

Fix the areas and the shapes break. Fix the shapes and the areas break.
In 2017 the public schools in Boston took Mercator off their classroom
walls, and the map they hung instead is not the true one either.

Which leaves the globe. No flattening, no stretching, the poles simply
there. Except the Earth is not a sphere, Everest on a school globe would
stand two tenths of a millimetre tall, and a globe is printed flat — on
twelve tapered strips, then pasted onto a ball. It is the orange from the
start of the video, running backwards.

So the globe solves the problem of projection. It does not solve the
problem of representation. And that distinction turns out to be the
whole thing — which is why the best map ever drawn gets the geography
almost entirely wrong, and why Leicester Square and Covent Garden are
two hundred and sixty metres apart while everyone takes the train.

Full transcript, sources and translations: https://theresmoretoit-channel.github.io/videos/maps-are-lying/

Chapters
00:00 A map you have seen a thousand times
00:35 Every flat map has to lie
01:15 Gauss proves it is impossible
02:07 Mercator, 1569
02:36 The price: four times, ten times, eighty
03:42 So let's fix it
04:21 Boston takes Mercator off the wall
05:10 Which photograph is correct?
05:28 A globe
05:56 Not entirely
06:35 How a globe is made
06:58 Projection, and representation
07:17 The best map ever drawn
08:27 The map in your pocket
09:21 What is it trying to get right?

IMAGE CREDITS
All archive images in this video are in the public domain.

Coastline data: Natural Earth (naturalearthdata.com), public domain.

Subtitles are written for this video, not auto-generated. An American English audio track is available as a second audio track.
```

> **Blok je úplný a nic neslibuje mimo sebe.** Obě archivní scény (S08
> Gaussův portrét, S13 Mercatorova mapa z roku 1569) jsou **public
> domain**, takže povinná atribuce podle `sources.json` neexistuje —
> `docs/zverejneni.md` na to má výslovné pravidlo, že se PD snímky
> vypisovat nemusí.
>
> **Natural Earth uvedeno, ačkoli nemusí.** Licence je public domain
> („no permission needed"), ale obrysy pevnin nese 90 % scén videa,
> takže je poctivé říct, odkud jsou.

## 3. Tagy

```
map projection, Mercator, Greenland size, Gauss, Theorema Egregium, cartography, equal area, Gall-Peters, globe, world map, geography, Harry Beck, tube map, Web Mercator, Google Maps, map distortion, why maps lie, true size of Africa
```

## 4. Nastavení

| | |
|---|---|
| viditelnost | nejdřív **neveřejně**, podívat se na to v přehrávači |
| jazyk videa | **en-GB** — nastavit NAPŘED, jinak zůstane dlaždice Titulky zašedlá |
| kategorie | Věda a technika |
| prohlášení o AI | **ne** — viz níž |
| licence | standardní |
| playlist | doplnit do `playlisty.json` a spustit `tools/playlisty.py` |

### Prohlášení o AI: odpověď je NE

Rozhoduje fotorealističnost, ne použití AI:

- obě SDXL scény (S32 globus na stole, S42 nástupiště metra) jsou
  **malované ilustrace**, ne fotorealismus
- archivní snímky jsou upravené jen barevně — *„color adjustment or
  lighting filters"* je výslovná výjimka
- hudba je **procedurální** (sinusovky a šum v numpy), ne z generativního
  modelu
- 90 % scén jsou diagramy kreslené kódem ze skutečných geodat

### Co musí uživatel naklikat sám

| | nahrál MP4 ručně (`--k-videu`) | `videos.insert` |
|---|---|---|
| prohlášení o AI | ✅ vyřídil průvodce | ❌ **ručně** |
| osvědčení o zproštění | ✅ vyřídil průvodce | ❌ **ručně** |
| **závěrečná obrazovka** | ❌ **ručně** | ❌ **ručně** |

Závěrečnou obrazovku API neumí vůbec. Posledních dvacet sekund pokrývá
šest scén (S53b–S54d) a všechny mají **prázdnou horní polovinu** —
hlídá to `zkontroluj_zaver()` už v generátoru, takže se na to nepřijde
až ve Studiu. Ověřit ještě `python tools/zaver_check.py videos/043-maps-are-lying`.

## 5. Po zveřejnění

```bash
python tools/titulky.py videos/043-maps-are-lying --smaz-asr   # NE --vse!
```

**`--vse` čerstvě nahrané video nevidí** (nezná ho `analytics/videa.json`)
a stojí 4 550 jednotek místo 100. V den nahrávání se volá adresářem.

Zapsat odkaz do `Témata.ods`, doplnit slug do `playlisty.json`, spustit
`analytics.py --videa` a pak `tools/playlisty.py`.

### Rozpočet kvóty na den nahrávání

| krok | jednotek |
|---|---|
| `nahraj.py --k-videu` (metadata, náhled, 9 titulků) | 3 750 |
| `lokalizace.py` | 52 |
| `titulky.py <adresář> --smaz-asr` | 100 |
| **celkem** | **3 902 z 10 000** |

Druhé video se ten den ještě vejde. **`titulky.py --vse` si nech na den,
kdy se nenahrává.**

## 6. Americká audiostopa

`render/audio-en-US.m4a` (13,4 MB, `af_heart`) je dorovnaná na Emminu
časovou mřížku, takže jde nasadit na hotové video **bez nového renderu**.
Nahrává se ve Studiu jako druhá zvuková stopa; API na to nemá volání.

> **YouTube nemá titulky per audiostopu.** Divák na americké stopě dostane
> tentýž `en.srt` zarovnaný na Emmu. Medián scény tohohle videa je 7,9 s,
> tedy blízko videu 039, kde bylo 23 % slov posunutých přes 300 ms —
> podrobnosti a měření v `docs/americka-stopa.md`.
