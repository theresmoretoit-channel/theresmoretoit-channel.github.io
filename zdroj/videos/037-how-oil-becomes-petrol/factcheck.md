# Fact check — 037 „How Do They Turn Crude Oil Into Petrol?"

Verze scénáře: **`script 0.2.md`**, 85 scén.
Ověřeno 2026-09-09.

Zdroj (`scenar-puvodni.md`) byl **záměrně nekvantitativní** — 1 794 slov
a ani jedno číslo. Čísla do 0.2 přibyla na zadání uživatele a **každé
z nich je ověřené proti primárnímu nebo institucionálnímu zdroji**,
protože přesně tady vzniká riziko populárního, ale zavádějícího údaje
(uživatel to jmenoval: „x litrů benzínu z barelu").

## A. Čísla přidaná v 0.2

### A1. Barel je 159 litrů — S12

**Tvrzení:** *„A barrel of crude oil is a hundred and fifty-nine litres."*

Standardní ropný barel = **42 US gallonů**. 42 × 3,785 411 784 =
**158,987 l**. ✅ **Platí**, zaokrouhleno správně.

### A2. Do rafinerie 159 l, ven ~170 l — S12, S13

**Tvrzení:** *„American refineries pour in a hundred and fifty-nine
litres... and get out about a hundred and seventy. More comes out
than went in."*

EIA, *Refining crude oil — inputs and outputs*, doslova:

> „In 2023, U.S. refineries produced an average of about **45 gallons
> of refined products for every 42-gallon barrel** of crude oil they
> refined."

45 gal = **170,3 l**. ✅ **Platí.** Průměrný „processing gain" 2023 byl
**6,3 %**; 159 × 1,063 = 169,0 l, tedy „about a hundred and seventy"
sedí z obou stran.

> **Omezení, které scénář DODRŽUJE:** je to údaj za **americké**
> rafinerie. Scénář proto říká *„American refineries"*, ne „refineries".
> Zobecnit to na svět nejde — CLAUDE.md má na tenhle tvar chyby
> vlastní řádek („sekundární zdroj použitý na zobecnění").

### A3. Proč vyteče víc, než vteklo — S14

**Tvrzení:** *„Nobody is cheating. The products are simply less dense
than the crude they came from."*

EIA tamtéž, doslova:

> „The total volume of products that refineries produce (output) is
> greater than the volume of crude oil that refineries process (input)
> **because most of the products they make have a lower density** than
> the crude oil they process."

✅ **Platí**, a je to důvod uvedený zdrojem, ne naše interpretace.

### A4. Teplota v peci ~350 °C — S26

**Tvrzení:** *„The crude is heated to around three hundred and fifty
degrees Celsius."*

Wikipedia, *Atmospheric distillation of crude oil*: pec **350–360 °C**.
ScienceDirect (*Atmospheric distillation*): *„heated to 350–380 °C"*.
✅ **Platí**, „around three hundred and fifty" je uvnitř obou rozsahů.

### A5. Body varu frakcí — S27, S28

**Tvrzení:** naphtha do ~190 °C, kerosene ~190–250 °C, nafta
~250–350 °C.

Penn State, kurz FSC 432, *Overall Refinery Flow* (°F):

| frakce | zdroj | převedeno |
|---|---|---|
| full-range naphtha | do 380 °F | do **193 °C** |
| kerosene | 380–480 °F | **193–249 °C** |
| light gas oil | 480–610 °F | **249–321 °C** |
| heavy gas oil | 610–690 °F | **321–366 °C** |

✅ **Platí** pro naphtu a kerosin. U nafty scénář říká *„very roughly
two hundred and fifty to three hundred and fifty"*, což překlenuje
light i část heavy gas oil — proto to výslovné **„very roughly"**.

> **A tohle je ten nález, kvůli kterému má scénář S29–S30.**
> Zdroje se v mezích **liší** — Wikipedia uvádí kerosin 140–270 °C,
> Penn State 193–249 °C. Není to spor, nýbrž vlastnost věci: řezné body
> si rafinerie **volí** podle poptávky a technologie. Scénář to proto
> říká nahlas (*„It's a setting, not a law of nature."*) místo aby
> předstíral přesnost, kterou ta čísla nemají. Uživatel to zadal
> („prezentoval bych je jako přibližné boiling ranges, ne jako ostré
> hranice") — a měření zdrojů mu dalo za pravdu.

### A6. Prostá destilace dá ~20 % benzinu, oktan ~50 — S35, S36, S37, S70

**Tvrzení:** *„Take a good, light crude and simply distil it. About
twenty per cent of the barrel comes off in the petrol range."* a
*„That straight-run petrol has an octane rating of about fifty."*

Penn State, kurz EGEE 439, *Refining of Petroleum into Fuels*, doslova:

> „even high-quality crude oil, we can only produce **from a distillation
> yield of 20% with an octane number of 50**"

✅ **Platí.** Podpůrně (EBSCO, *Petroleum refining and processing*):
katalytický cracking *„increases the yield of gasoline in a refinery to
about 45 percent"* — tedy tentýž směr i tentýž řád.

> **Jistota: střední.** Je to vysokoškolský kurzovní materiál, tedy
> zdroj institucionální, ne primární. Scénář proto říká **„about
> twenty per cent"** a **„about fifty"**, ne přesná čísla, a váže je na
> *„a good, light crude"*, jak to dělá zdroj. Netvrdí se, že to platí
> pro každou ropu — u těžké ropy by výtěžek byl nižší.

### A7. Benzin je skoro polovina toho, co rafinerie prodá — S37

**Tvrzení:** *„petrol is close to half of everything a refinery sells."*

EIA 2023, z 42gallonového barelu: **finished motor gasoline 19,57 gal**.
19,57 / 44,65 gal výstupu = **43,8 %**; vůči vstupu 19,57 / 42 = 46,6 %.
Penn State EGEE 439: *„45-50 barrels per 100 barrels of crude oil
processed are gasoline"*. ✅ **Platí**, „close to half" sedí na obojí.

### A8. Auto chce oktan 95 — S38

**Tvrzení:** *„Your car wants ninety-five."*

95 je v Evropě standardní RON u nejrozšířenějšího benzinu (EN 228
Super 95). ✅ **Platí pro evropský kontext**, který video má —
hlas je `en-gb` a video mluví o „filling station". V USA se pumpy
značí AKI (87/89/93), což je **jiná stupnice**, ne jiný benzin.

> **Nesrovnávat s A6 přes stupnice.** Oktan 50 z A6 je z amerického
> zdroje; RON a AKI se liší zhruba o 4–5 bodů. Scénář tím ale
> neargumentuje kvantitativně — říká jen, že mezera je velká, a ta
> je velká na kterékoli stupnici.

### A9. Oktanová stupnice: heptan 0, isooktan 100 — S49, S50

**Tvrzení:** *„One particular molecule, heptane, was defined as zero.
Another, iso-octane, was defined as a hundred."*

Penn State EGEE 439, doslova: *„heptane - octane number equal to 0, and
**2,2,4-trimethylpentane** - octane number equal to 100"*.
2,2,4-trimethylpentan **je** isooktan. ✅ **Platí.**

> Scénář říká *„was defined as"*, ne „has" — a to je věcně důležité:
> nejde o naměřenou vlastnost, nýbrž o **definici stupnice**. Proto
> je v S49 *„The scale is beautifully arbitrary."*

### A10. Rozpad barelu na produkty — S62, S63

**Tvrzení:** *„roughly seventy-four litres of petrol. Forty-seven of
diesel and heating oil. Seventeen of jet fuel."*

EIA, rozpad 42gallonového barelu (2023):

| produkt | EIA (gal) | × 3,7854 | scénář |
|---|---|---|---|
| finished motor gasoline | 19,57 | 74,1 l | **74** ✅ |
| distillate fuel oil | 12,47 | 47,2 l | **47** ✅ |
| kerosene-type jet fuel | 4,41 | 16,7 l | **17** ✅ |
| petroleum coke | 2,06 | 7,8 l | „the rest" |
| still gas | 1,68 | 6,4 l | „refinery gas" |
| hydrocarbon gas liquids | 1,55 | 5,9 l | „the rest" |
| ostatní (asfalt, maziva, naphty) | 3,91 | 14,8 l | „the rest" |

✅ **Platí.** Scénář správně říká *„In American refineries"* — viz A2.

> **Pozor na jednu past, do které scénář ZÁMĚRNĚ nešlápl:** součet
> 74 + 47 + 17 = 138 l, plus zbytek dá **přes 159 l**. Není to chyba,
> je to týž processing gain z A2 — a proto ta čísla stojí až ZA scénou
> S13, která divákovi předem řekla, že výstup je větší než vstup.

## B. Tvrzení převzatá ze zdroje

| # | tvrzení | scéna | závěr |
|---|---|---|---|
| B1 | ropa je směs tisíců uhlovodíků + síra, dusík, kyslík, kovy | S17, S18 | ✅ standardní popis, shodně ScienceDirect i EIA |
| B2 | lehká ropa = víc malých molekul, těžká = víc velkých | S21 | ✅ definice podle hustoty / API gravity |
| B3 | sweet = málo síry, sour = víc | S22 | ✅ hranice bývá 0,5 % hm. síry |
| B4 | ropa se před destilací odsoluje a zbaví vody | S08 | ✅ desalter je standardní první krok |
| B5 | horká pára stoupá, chladnější kapalina stéká, frakce kondenzují v patrech | S26, S27 | ✅ |
| B6 | cracking = štěpení velkých molekul na menší | S40, S41 | ✅ |
| B7 | hydrocracking používá vodík za vysokého tlaku s katalyzátory | S42 | ✅ |
| B8 | reforming a isomerace zlepšují vlastnosti pro zážehový motor | S46, S47 | ✅ |
| B9 | oktanové číslo měří odolnost proti klepání, ne obsah energie | S48, S51, S52 | ✅ — a je to častý mýtus, takže dobře, že to video říká výslovně |
| B10 | naftu charakterizuje cetanové číslo (kvalita vznícení) | S56 | ✅ |
| B11 | hydrotreating odstraňuje síru reakcí s vodíkem | S58, S59 | ✅ |
| B12 | síra se prodává jako elementární síra | S60, S61 | ✅ Clausův proces; ropné rafinerie jsou dnes hlavní světový zdroj síry |
| B13 | z barelu je benzin, nafta, kerosin, koks, rafinerský plyn, bitumen, maziva, petrochemické suroviny, síra | S62, S63 | ✅ |
| B14 | vlastní destilace nedá komerční benzin (oktan, síra, chování v motoru) | S70, S71, S72 | ✅ a nově je to i **doložené číslem**, viz A6 |

## C. Co bylo v 0.1 a ve 0.2 UŽ NENÍ

Škrtnuto na zadání uživatele, ne kvůli věcné chybě:

- celá sekce o těžké ropě (vakuová destilace, koking) — zbyla jedna
  věta v S42
- opakovaný čtyřdílný výčet v outru
- část specifikací nafty (hustota, chování za nízkých teplot)

> **Žádné z toho nebylo nepravdivé.** Zapsáno proto, aby se při případném
> vracení nemuselo ověřovat znovu.

## D. Věty vzniklé SLITÍM nebo ZKRÁCENÍM

CLAUDE.md varuje, že zkracování vyrábí chyby, které ve zdroji nebyly.
Prověřeny všechny věty, které v 0.1 neexistovaly:

| nová věta | riziko | závěr |
|---|---|---|
| *„This matters most when the refinery is working with heavy crude."* (S42) | nahrazuje celou vyškrtnutou sekci — nesmí tvrdit víc, než tvrdila | ✅ původní sekce říkala totéž (*„Their complexity is partly determined by the crude oil"*) |
| *„Suddenly those enormous molecules aren't something to be sold off cheaply. They're raw material for petrol."* (S43) | „cheaply" je hodnotící soud, ve zdroji nebyl | ✅ zdroj má *„that isn't necessarily the most valuable thing we can do with them"* — táž teze |
| *„The rest is built by the same kind of chemistry."* (S54) | zobecnění o naftě | ✅ zdroj: *„Other refinery processes can produce additional components suitable for diesel"* |
| *„It's a setting, not a law of nature."* (S30) | silné tvrzení o řezných bodech | ✅ doloženo rozporem zdrojů, viz A5 |
| *„Too little petrol. And what there is, is too poor to burn."* (S39) | „too poor to burn" doslova neplatí — straight-run benzin hoří | ⚠️ **viz níž** |

### ⚠️ Jediný nález: „too poor to burn" je nepřesné

Straight-run benzin s oktanem 50 **hoří**. Problém není hoření, ale
**samozápal před jiskrou** — klepání. Věta jak je napsaná tvrdí něco
jiného, než co je pravda, a je to přesně ten typ chyby, který vzniká
zkracováním.

**Navržená oprava (S39):**

> *„Too little petrol. And what there is, would wreck the engine."*

nebo přesněji

> *„Too little petrol. And what there is, would knock itself apart."*

**Neopraveno ve `script.md`** — čeká na tvoje rozhodnutí, protože je to
volba formulace, ne oprava faktu.

## Zdroje

- U.S. EIA, *Refining crude oil — inputs and outputs*
  <https://www.eia.gov/energyexplained/oil-and-petroleum-products/refining-crude-oil-inputs-and-outputs.php>
- U.S. EIA, FAQ 327, *How many gallons of gasoline and diesel fuel are
  made from one barrel of oil?*
  <https://www.eia.gov/tools/faqs/faq.php?id=327&t=9>
- Penn State, Dutton Institute, EGEE 439 — *2.2 Refining of Petroleum
  into Fuels* <https://courses.ems.psu.edu/egee439/node/7>
- Penn State, Dutton Institute, FSC 432 — *Lesson 3: Overall Refinery
  Flow* <https://courses.ems.psu.edu/fsc432/book/export/html/517>
- Wikipedia, *Atmospheric distillation of crude oil*
  <https://en.wikipedia.org/wiki/Atmospheric_distillation_of_crude_oil>
- EBSCO Research Starters, *Petroleum refining and processing*
  <https://www.ebsco.com/research-starters/science/petroleum-refining-and-processing>
