# YouTube — 037 How Do They Turn Crude Oil Into Petrol?

Nahrává se `render/final-en.mp4` (master, ne draft), `render/thumbnail.jpg`
a `subtitles/*.srt` v devíti jazycích.

| co | stav |
|---|---|
| titulky | ✅ devět jazyků, 183 en / 257 ostatní |
| lokalizace | ✅ `youtube-preklady.md`, osm jazyků |
| náhled | ✅ `render/thumbnail.jpg` — varianta **`e-molekula-3d`** dodaná uživatelem (druhé kolo), 1280×720, 0,20 MB |
| **master** | ❌ čeká na SDXL scény a render na herním PC |

## 1. Titul

```
How Do They Turn Crude Oil Into Petrol?
```

Dodaný titul, 38 znaků — nad mediánem kanálu (33), hluboko pod hranicí,
za kterou YouTube titul v seznamu utne (~60).

**Ponechán, protože náhled nese paradox a titul má nést otázku.** Kdyby
se titul ptal na totéž co náhled, dvojice řekne jednu věc dvakrát — táž
úvaha jako u videa 036.

| varianta | znaků | poznámka |
|---|---|---|
| **`How Do They Turn Crude Oil Into Petrol?`** | **38** | ✅ dodaný uživatelem |
| `159 Litres In, 170 Litres Out` | 29 | nejsilnější číslo videa, ale bez kontextu nedává smysl |
| `A Refinery Doesn't Extract Petrol. It Makes It.` | 47 | je to **závěr videa**, ne otázka |
| `Could You Make Petrol At Home?` | 30 | slibuje kutilský návod, který video nedá |

> **Pozor na `petrol` versus `gasoline`.** Video je britské (`bf_emma`,
> `en-gb`), takže titul i popis mluví o *petrol*. Americké hledání to
> nenajde — proto je `gasoline` mezi **tagy**, kde nevadí.

## 2. Popis

```
You put a nozzle into your car, press a button, and a few seconds later
you have petrol. But where did it come from? Was it already sitting
inside the crude oil, waiting to be poured out?

It was not. Here is the number that gives it away: American refineries
put a hundred and fifty-nine litres of crude into the process and take
about a hundred and seventy litres of product out. More comes out than
went in. Nobody is cheating — the products are simply less dense than
the crude they came from. A refinery is not a machine that extracts
petrol from oil. It is a machine that makes new things out of it.

This video follows one barrel. What crude oil actually is (a soup of
thousands of different hydrocarbons, plus sulphur, nitrogen, oxygen and
metals). How the distillation column sorts them by boiling behaviour —
and why the boundaries between fractions are a setting the refinery
chooses, not a law of nature.

Then the part that makes the whole industry necessary. Distil a good
light crude and only about twenty per cent of the barrel comes off in
the petrol range, at an octane rating of around fifty. Petrol is close
to half of what a refinery sells, and your car wants ninety-five. Too
little, and what there is knocks too easily. Cracking closes the first
gap. Reforming, isomerisation and careful blending close the second.

And the octane scale itself turns out to be beautifully arbitrary: one
molecule, heptane, was defined as zero, another, iso-octane, as a
hundred, and everything else is measured between them.

Finally, the question we started with. Could you make petrol at home?
In principle yes — nothing about it violates the laws of physics. In
practice you would build a still, get a fifth of a barrel at octane
fifty, and then start adding cracking, hydrotreating, hydrogen
production, high-pressure equipment, control systems and laboratories.
Congratulations. You have just started building a refinery.

Full transcript, sources and translations: https://theresmoretoit-channel.github.io/videos/how-oil-becomes-petrol/

CHAPTERS
0:00 How petrol appears
0:35 What a refinery does first
1:04 159 litres in, 170 out
1:36 What is inside the barrel
2:10 Light, heavy, sweet, sour
2:45 Inside the column
3:50 Why distillation is not enough
4:44 Cracking
5:30 Octane, and what it means
6:35 Diesel
7:00 Where the sulphur goes
7:33 One barrel, many products
8:11 Could you do it at home?
9:04 Building a real refinery
9:55 What is really in your tank

Subtitles are written for this video, not auto-generated. An American
English audio track is available as a second audio track.

SOURCES
US Energy Information Administration - Refining crude oil: inputs and
outputs (2023 yields, processing gain)
Penn State, EGEE 439 - Refining of Petroleum into Fuels (straight-run
yield and octane, octane scale definition)
Penn State, FSC 432 - Overall Refinery Flow (cut points)

IMAGE CREDITS
Distillation Towers Tulap1 - Carlos Valenzuela, CC BY-SA 4.0
Fawley Oil Refinery, aerial 2017 - Chris, CC BY-SA 2.0
Both via Wikimedia Commons.
Licences: creativecommons.org/licenses/by-sa/4.0 and /by-sa/2.0
All other archive images are in the public domain.

If you want the next one, there is a subscribe button.
```

> **Atribuce je UVNITŘ bloku**, ne pod ním. Podle `docs/zverejneni.md`
> chyběla u čtyř videí ze šestnácti přesně proto, že kredity visely jako
> poznámka pod ním — uživatel kopíruje jen text mezi apostrofy.
>
> Vypsané jsou **dvě položky z `sources.json`, obě `CC BY-SA`**.
> Třetí (síra, Gene Daniels) je public domain, takže povinnou atribuci
> nemá a kryje ji poslední řádek.

## 3. Tagy

```
crude oil, petrol, gasoline, oil refinery, refining, distillation,
fractional distillation, catalytic cracking, octane rating, diesel,
petrochemicals, chemistry, how it's made, explainer
```

`gasoline` je tam schválně — video mluví britsky, ale hledá se americky.

## 4. Nastavení

| pole | hodnota |
|---|---|
| jazyk videa | **`en-gb`** — nastavit NAPŘED, jinak zůstane dlaždice Titulky zašedlá |
| kategorie | **Science & Technology** (28) — posílá `nahraj.py` |
| pro děti | ne |
| **byla použita AI** | **ne** — posílá `nahraj.py` jako `containsSyntheticMedia: false` |
| **osvědčení o zproštění** | ✅ vyřídí průvodce ve Studiu při ručním nahrání |
| **závěrečná obrazovka** | ❌ **ručně ve Studiu**, API na to nemá ani zdroj |
| playlist | dopsat do `playlisty.json` před `tools/playlisty.py` |

## Proč je odpověď na „byla použita AI" NE

- **SDXL scény jsou 4 z 85** a díky kotvě stylu jsou to malované
  ilustrace, ne fotorealismus.
- **Archivní snímky jsou upravené jen barevně** — *„color adjustment or
  lighting filters"* je ve výjimkách pravidel výslovně.
- **Hudba je procedurální** (sinusovky a šum v numpy), ne z generativního
  modelu.

## 5. Postup nahrání

```bash
# 1. MP4 ručně do Studia (průvodce vyřídí AI prohlášení i zproštění)
# 2. zbytek doplní skript:
python tools/nahraj.py videos/037-how-oil-becomes-petrol --k-videu <ID>
python tools/lokalizace.py videos/037-how-oil-becomes-petrol
python tools/titulky.py videos/037-how-oil-becomes-petrol --smaz-asr
```

> **`titulky.py --vse` v den nahrání NE.** Stojí 4 550 jednotek proti 100
> a čerstvě nahrané video stejně nevidí — nechodí přes kanál, nýbrž přes
> `analytics/videa.json`. Na nové video se volá **adresářem**.

> Rozpočet dne: `nahraj.py --k-videu` 3 750 + `lokalizace.py` 52 +
> `titulky.py` na jedno video 100 = **3 902 jednotek** z 10 000.

## Co musí uživatel naklikat sám

| | |
|---|---|
| prohlášení o AI | ✅ vyřídí průvodce nahráním |
| osvědčení o zproštění | ✅ vyřídí průvodce nahráním |
| **závěrečná obrazovka** | ❌ **ručně** — API na ni nemá ani zdroj |

`zaver_check.py` prošel: v posledních 20 s jsou scény **S83, S84 a S85**
a u všech tří je vlevo nahoře 0 % překryv, takže dlaždice i kolečko mají
kam. **Dole to nejde** — přes celou šířku tam leží ambrový titulek.
