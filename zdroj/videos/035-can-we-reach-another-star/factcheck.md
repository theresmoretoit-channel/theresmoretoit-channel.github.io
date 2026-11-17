# Fact check — 035 Can We Reach Another Star With Today's Technology?

Ověřeno 2026-09-09 proti `script 0.2.md` (102 scén). Postup podle CLAUDE.md,
kapitola „Fact check je povinný krok": vypsáno **každé** ověřitelné tvrzení,
čísla **spočítána**, ne vzpomenuta.

**Sedm tvrzení neprošlo** a jsou opravena ve `script 0.3.md`; jedno z nich
(prach) bylo mimo o šest řádů.

---

## NEPROŠLO

### 1. S61 — miligramové zrnko prachu. Mimo o ŠEST ŘÁDŮ.

**Tvrzení 0.2:** *„At a fifth of the speed of light, a single grain weighing
one milligram arrives with the energy of nearly half a tonne of TNT."*

Aritmetika sedí — (γ−1)mc² při 0,2 c pro 10⁻⁶ kg dá 1,85 × 10⁹ J = 443 kg
TNT. **Vadná je ta částice.** Primární rozbor rizika prachu pro Starshot
(Lingam a spol., arXiv:2307.12160, *Calculations of Particle Bombardment due
to Dust and Charged Particles in the ISM on the Project Starshot Gram-Scale
Interstellar Probe*) pracuje s těmito hmotnostmi:

| | hmotnost | kinetická energie při 0,2 c (paper) | moje kontrola |
|---|---|---|---|
| typické zrnko | 3 × 10⁻¹³ g | 0,5 J | 0,55 J ✅ |
| střední zrnko | 2 × 10⁻¹² g | 3,6 J | 3,7 J ✅ |
| **největší zrnko** | **1 × 10⁻⁹ g** | **1 800 J** | 1 853 J ✅ |

Shoda mého výpočtu s paperem potvrzuje metodu. Ale **jeden miligram je
10⁶× víc, než je největší zrnko v tom rozboru**, a 2 × 10⁵× víc než
absolutní horní mez, kterou paper zmiňuje (5 × 10⁻⁹ g). Takové zrnko
v mezihvězdném prostoru není prach, nýbrž kamínek — a sonda o čelní ploše
1 m² nabere za **celou cestu** k Proximě jen ~0,67 mg prachu **dohromady**
(z hustoty ISM 1 atom H/cm³ a poměru prach:plyn 1 %).

**Oprava:** použít číslo z primárního zdroje.

> *The biggest specks out there weigh about a billionth of a gram.
> At a fifth of the speed of light, one of those arrives with the energy
> of a rifle bullet.*

1 800 J odpovídá náboji 5,56 × 45 mm NATO (1 767 J). Pro gramovou sondu
je to zásah, který ji zničí — obraz drží a číslo je doložené.

> **Zbytek sekce prochází.** Že prach při 0,2 c vyžaduje uvažovat o stínění,
> potvrzuje druhá strana literatury: Hoang, Lazarian, Burkhart & Loeb 2017
> (arXiv:1608.05284) naměřili erozi povrchové vrstvy **~0,5 mm** při 0,2 c
> a výslovně doporučují stínicí strategie. Formulace *„So it may need
> shielding"* je tedy podložená; opatrné „may" je na místě, protože tentýž
> rozbor 2307.12160 uzavírá, že počet zásahů *„may be manageable"*
> a eroze stojí 1–5 % hmotnosti gramové sondy.

### 2. S06 — „know how to build" versus S85

**Tvrzení 0.2:** *„We actually know how to build a spacecraft that could
leave the Solar System and head towards Proxima Centauri."*
**Proti tomu S85:** *„Then we're no longer talking about something we know
how to build."*

Rozpor to není — S81/S82 rozdíl vysvětluje (*„send a piece of hardware onto
a trajectory… probably yes"*). Ale S06 je **formulovaná dost volně na to,
aby ji divák četl jako „umíme postavit mezihvězdnou sondu"**, což je přesně
to, co video 9 minut vyvrací.

**Oprava:** říct, co se tím doopravdy myslí — akci, ne stroj.

> *We actually know how to send a spacecraft out of the Solar System
> and put it on a course for Proxima Centauri.*

S07 (*„We have the rockets. We have the computers. We have the navigation
technology."*) to podepře a S85 pak jednoznačně mluví o funkční sondě.

### 3. S14 — Voyager 1 není nejrychlejší sonda

**Tvrzení 0.2:** *„Our fastest spacecraft aren't even remotely close to the
speed of light. Voyager one, for example, is travelling at roughly seventeen
kilometres per second."*

„For example" implikuje, že Voyager patří mezi nejrychlejší. **Nepatří:**
Parker Solar Probe dosahuje v perihelu ~192 km/s, tedy 11× víc.

| sonda | rychlost |
|---|---|
| Parker Solar Probe (perihel) | ~192 km/s |
| **Voyager 1** | **17,0 km/s** |
| Voyager 2 | 15,4 km/s |
| New Horizons | ~13 km/s |
| Pioneer 10 / 11 | ~11–12 km/s |

Voyager 1 **je** nejrychlejší věc, která opouští Sluneční soustavu — a to
je silnější tvrzení než dnešní vágní „for example".

**Oprava:** *„Voyager one, the fastest thing we have ever sent out of the
Solar System, is travelling at roughly seventeen kilometres per second."*

### 4. S46 — „roughly three times" spotřeby Británie je 2,7×

Spotřeba elektřiny Spojeného království **323,0 TWh za rok 2025**
(DUKES 2025 / NESO), tedy průměrný příkon **36,9 GW**.

100 GW / 36,9 GW = **2,71×**. „Roughly three times" je na horní hranici
zaokrouhlení.

**Oprava:** *„nearly three times"*.

### 5. S01 — „four hundred billion stars" je horní okraj odhadu

NASA i ESA uvádějí rozpětí **100 az 400 miliard**; přesně spočítat to nejde,
odhad závisí na modelu hmotnosti galaxie a průměrné hvězdy. Scénář bere
**nejvyšší možnou hodnotu a tvrdí ji jako fakt**.

**Oprava:** *„a few hundred billion stars"* — stejně údernÉ, a neprůstřelné.

### 6. S54 — „just as much energy" chce zpřesnit

**Tvrzení 0.2:** *„Slowing it down takes just as much energy as speeding
it up."*

Fyzikálně platí: kinetická energie při 0,2 c je (γ−1)mc² a při zabrzdění
se jí musíš zbavit přesně tolik, kolik jsi jí dodal. γ = 1,020621.

**Ale „energy" je dvojznačné.** Není to totéž jako *„potřebuješ stejnou
energii ze svého zdroje"* — účinnost pohonu je jiná v obou směrech
(laserová plachta předá plachtě jen zlomek energie svazku) a brzdit by se
muselo úplně jinak (magnetická plachta, laser v cíli).

**Oprava:** říct to o energii **sondy**, ne o zdroji:

> *Slowing it down means getting rid of every bit of that energy again.*

### 7. S43 — Starshotův laser je POZEMNÍ, ne „near Earth"

*„we could put a huge laser array near Earth"* svádí ke čtení „na oběžné
dráze". Baseline Breakthrough Starshot je **pozemní fázované pole**
(*terrestrial-based 100 GW laser*).

**Oprava:** *„somewhere on Earth"*.

---

## PROŠLO

### Vzdálenost a čas

| tvrzení | ověření | |
|---|---|---|
| Proxima Centauri je nejbližší hvězda | ze tří hvězd systému je nejslabší Proxima nejblíž Slunci (NASA) | ✅ |
| *„about four and a quarter light-years"* (S02) | 4,2465 ly | ✅ |
| *„Four point two four light-years"* (S12) | 4,2465 ly | ✅ |
| *„roughly forty trillion kilometres"* (S12) | 4,2465 × 9,4607 × 10¹² = **4,017 × 10¹³ km** | ✅ |
| *„seventeen kilometres per second"* (S14) | NASA, 21. 8. 2024: **17,0 km/s** vůči Slunci | ✅ |
| *„roughly seventy-five thousand years"* (S16) | 4,017 × 10¹³ / 17,0 = **74 886 let** | ✅ |
| *„the first pyramids… about five thousand years ago"* (S17) | Džoserova stupňovitá pyramida ~2667–2648 př. n. l. = **~4 700 let** | ✅ |
| *„twenty percent of the speed of light"* → *„roughly twenty years"* (S45, S47) | 4,2465 / 0,2 = **21,2 roku** | ✅ |
| *„the signal takes more than four years"* (S66) | 4,2465 roku | ✅ |
| *„a complete conversation… more than eight years"* (S76) | 2 × 4,2465 = **8,49 roku** | ✅ |
| *„millions or billions of kilometres away"* (S67) | chyba 1 úhlové vteřiny přes 4,24 ly = **195 mil. km** | ✅ |

**Pozor u překladů:** *trillion* je tady 10¹², tedy německy `Billionen`,
španělsky `billones`, česky **bilionů** (CLAUDE.md, „Past s číslovkami").

### Voyager

| tvrzení | ověření | |
|---|---|---|
| *„spacecraft already flying through interstellar space"* (S07) | Voyager 1 překročil heliopauzu 2012, Voyager 2 v 2018 | ✅ |
| *„among the longest-lived machines we have ever built"* (S24) | start 1977, tedy **49 let** nepřetržitého provozu | ✅ |
| *„already having systems switched off to conserve their remaining power"* (S25) | NASA vypnula Voyageru 1 přístroj *Low-energy Charged Particles* **17. 4. 2026**, předtím *cosmic ray subsystem* (25. 2. 2025) a Voyageru 2 *LECP* (24. 3. 2025). **Sedm z deseti** sad přístrojů je vypnutých, sondy ztrácejí **~4 W ročně** | ✅ velmi aktuální |

### Energie

| tvrzení | ověření | |
|---|---|---|
| *„radioisotope generators… for deep-space missions"* (S34) | RTG na Pu-238: Voyager, Cassini, New Horizons, Curiosity | ✅ |
| *„plutonium two three eight, which loses half its output every eighty-eight years"* (S35) | poločas Pu-238 = **87,7 roku** | ✅ |
| *„after a thousand years… less than a thousandth of what it started with"* (S36) | 1 000 / 87,7 = 11,40 poločasu → 2⁻¹¹·⁴⁰ = **1/2 707** | ✅ a **konzervativní**: skutečný RTG klesá rychleji než izotop, protože degradují termočlánky (Voyager ztrácí ~4 W/rok) |
| *„a thousand years is just over one percent of the journey"* (S37) | 1 000 / 74 886 = **1,34 %** | ✅ |

### Laser a Starshot

| tvrzení | ověření | |
|---|---|---|
| *„Breakthrough Starshot… extremely small spacecraft"* (S45) | gramové „nanocraft", plachta v řádu metrů | ✅ |
| *„twenty percent of the speed of light"* (S45) | deklarovaný cíl programu | ✅ |
| *„a hundred gigawatts"* (S46) | 100 GW fázované pole | ✅ |
| *„there is no giant laser waiting for you at Proxima"* (S54) | z definice mise | ✅ |

### Prach a navigace

| tvrzení | ověření | |
|---|---|---|
| *„space stops being empty… There is dust. There are tiny particles."* (S59) | mezihvězdné prostředí | ✅ |
| *„it may need shielding"* (S62) | Hoang a spol. 2017: eroze ~0,5 mm při 0,2 c, doporučují stínění | ✅ |
| *„every extra gram makes acceleration harder"* (S62) | u laserové plachty je hmotnost přímo v rovnici zrychlení | ✅ |
| *„Proxima is moving. So is the Sun."* (S64) | vlastní pohyb Proximy 3,85″/rok, radiální rychlost −22,2 km/s | ✅ |
| *„Astronomers are very good at predicting stellar motion"* (S64) | Gaia dává paralaxy i vlastní pohyby s přesností na mikrovteřiny | ✅ |
| *„Proxima's planets"* (S78) | Proxima má **dvě potvrzené planety** (b, d) — množné číslo sedí | ✅ |

### Kvalitativní tvrzení bez čísel

*„there is no maintenance mission"*, *„no engineer who can travel there"*,
*„the processor in your phone is unimaginably more powerful than computers
from a few decades ago"*, *„we know how to build machines that work for
years… decades"*, *„Earth is not mission control"* — všechno v mezích
běžného úzu, nic k ověření.

---

## Zdroje

- NASA Voyager — rychlost, mezihvězdný prostor, vypínání přístrojů:
  <https://science.nasa.gov/mission/voyager/frequently-asked-questions/>,
  <https://science.nasa.gov/blogs/voyager/2026/04/17/nasa-shuts-off-instrument-on-voyager-1-to-keep-spacecraft-operating/>,
  <https://www.jpl.nasa.gov/news/nasa-turns-off-two-voyager-science-instruments-to-extend-mission/>
- Lingam a spol., *Calculations of Particle Bombardment… Project Starshot*:
  <https://arxiv.org/pdf/2307.12160>
- Hoang, Lazarian, Burkhart & Loeb 2017, *The interaction of relativistic
  spacecrafts with the interstellar medium*: <https://arxiv.org/abs/1608.05284>
- Breakthrough Initiatives — Starshot: <https://breakthroughinitiatives.org/concept/3>
- Počet hvězd Galaxie: <https://asd.gsfc.nasa.gov/blueshift/index.php/2015/07/22/how-many-stars-in-the-milky-way/>
- Proxima Centauri a její planety:
  <https://science.nasa.gov/exoplanets/other-stars-other-worlds/our-nearest-celestial-neighbor-an-exotic-3-star-system/>
- Spotřeba elektřiny UK 2025 (323,0 TWh): DUKES 2025, kap. 5
  <https://assets.publishing.service.gov.uk/media/688a28656478525675739051/DUKES_2025_Chapter_5.pdf>,
  NESO <https://www.neso.energy/news/britains-energy-explained-2025-review>
- Džoserova pyramida: <https://www.britannica.com/topic/Step-Pyramid-of-Djoser>
