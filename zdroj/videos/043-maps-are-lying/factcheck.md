# Fact check — 043 „Maps Are Lying"

Ověřeno 2026-09-13 proti `script 0.1.md` po dramaturgickém zamčení;
opravy jsou v `script 0.2.md`, číslování odpovídá 0.3 a letopočty
jsou od 0.5 psané číslicemi (viz „Letopočty" na konci). Prošlo **každé** ověřitelné tvrzení
scénáře, ne jen ta riziková — a hlavně i tvrzení, která
**v dodaném textu nebyla a vznikla až draftem**. Těch je tu většina:
původní text měl dvě čísla, tenhle scénář jich má dvacet.

**Výsledek: 5 oprav zapsáno do scénáře, 2 zjednodušení vědomě ponechána.**
Dvě z těch oprav jsou **věcné chyby, které jsem do scénáře přinesl sám**
(S17 a S18) — obě vznikly tím, že jsem hodnotu spočítal pro kulatou
zeměpisnou šířku a pak ji popsal jako konkrétní místo.

---

## S03, S03b — Afrika je čtrnáctkrát větší než Grónsko

> *„Africa is roughly fourteen times larger than Greenland."* / *„Fourteen."*

| | rozloha |
|---|---|
| Afrika | **30 370 000 km²** |
| Grónsko | **2 166 086 km²** |
| poměr | **14,02** |

✅ **Sedí.** Číslo je v dodaném textu a přežilo přepočet.

## S04 — „Every flat map of the Earth has to lie"

Není to řečnická figura, nýbrž důsledek Gaussovy věty (S08). Koule má
nenulovou Gaussovu křivost, rovina nulovou, a ta je invariantní vůči
izometrii — takže mezi nimi žádná izometrie neexistuje.

✅ **Sedí**, a S08 to ve videu i dokládá.

## S08, S10 — Gauss, 1827, „remarkable theorem"

> *„In 1827, Carl Friedrich Gauss proved that the curvature of
> a surface belongs to the surface itself."* /
> *„Gauss called it his remarkable theorem."*

Práce *Disquisitiones generales circa superficies curvas*, předložená
Královské společnosti v Göttingenu **8. října 1827**. Gauss v ní
výsledek sám nazval **Theorema Egregium**, což je latinsky „pozoruhodná
věta" — pojmenování je tedy skutečně jeho, ne pozdější přezdívka.

✅ **Sedí, včetně toho „called it".**

> **Latinský název ve scénáři záměrně NENÍ.** *Theorema Egregium* by
> Kokoro muselo číst anglickou aproximací a stálo by to `pronounce`
> zápis kvůli jednomu výskytu. Anglické „his remarkable theorem" je
> navíc doslovný překlad, takže se nic neztrácí.

> **Formulace *„belongs to the surface itself"* je zjednodušení, ne
> chyba.** Přesně: Gaussova křivost je vyjádřitelná jen z první
> fundamentální formy, tedy z měření provedených uvnitř plochy.
> „Patří samotné ploše" to říká správně a bez aparátu.

## S09 — válec ano, koule ne ⚠️ OPRAVENO

> **0.1:** *„You can roll a sheet of paper into a tube, because a tube
> isn't really curved."*

❌ **Věcně špatně.** Válec zakřivený **je** — má nenulovou střední
křivost a v prostoru je očividně ohnutý. Nulová je jen jeho **Gaussova**
křivost (jedna hlavní křivost je nulová, takže součin je nula), a právě
proto je rozvinutelný do roviny.

✅ **Opraveno** na formulaci, která tvrdí jen to, co je pravda,
a nepotřebuje zavádět Gaussovu křivost jménem:

> **0.2:** *„You can roll a sheet of paper into a tube, because its
> surface can still be unrolled. But you cannot wrap it round a ball
> without stretching or tearing it."*

## S13 — Mercator, 1569, vlámský

> *„The most famous choice was made in 1569 by a Flemish mapmaker
> called Gerardus Mercator."*

Mapa *Nova et Aucta Orbis Terrae Descriptio ad Usum Navigantium
Emendate* vyšla **1569**, na osmnácti listech, 131 × 208 cm.
Mercator se narodil 1512 v Rupelmonde ve Flandrech.

✅ **Sedí, včetně „Flemish".**

## S14 — loxodroma je na Mercatorově mapě přímka

> *„On his map, a line of constant compass bearing is a straight line."*

To je definiční vlastnost projekce a stojí i v podtitulu té mapy
(*„ad usum navigantium"*, tedy „k užitku plavcům").

✅ **Sedí**, a je to formulované opatrně — *„constant compass bearing"*,
ne „nejkratší cesta". Nejkratší cesta je ortodroma a ta na Mercatoru
přímka **není**; scénář to netvrdí.

## S17 — Oslo, čtyřnásobek plochy

> *„Oslo sits far enough north that it covers four times the area
> it actually has."*

Plošné zkreslení Mercatoru je `sec²φ`. Oslo leží na **59,91° s. š.**:

`1 / cos²(59,91°) = ` **3,98**

✅ **Sedí**, „four times" je zaokrouhlení směrem dolů o 0,5 %.

## S17 — střed Grónska ⚠️ OPRAVENO

> **0.1:** *„The middle of Greenland? Nine times."*

❌ **Moje chyba.** Spočítal jsem `sec²(71°) = 9,43` a pak to popsal jako
„střed Grónska". Grónsko sahá od **59,8°** po **83,65°** s. š., takže
jeho střed je na **71,7°**, a tam vychází:

`1 / cos²(71,7°) = ` **10,14**

✅ **Opraveno na „Ten times"** (`sec²(71,57°) = 10,01`, tedy střed
Grónska s rezervou na obě strany).

## S18 — severní cíp Grónska ⚠️ OPRAVENO, a o hodně

> **0.1:** *„The northern tip of Greenland is stretched thirty-three
> times beyond its real size."*

❌ **Tatáž chyba, ale horší.** 33× je `sec²(80°)`, jenže severní cíp
Grónska je **mys Morris Jesup, 83°39′42″ s. š.** (nejsevernější bod
pevniny na Zemi, 708 km od pólu). Tam vychází:

`1 / cos²(83,66°) = ` **81,7**

✅ **Opraveno na „more than eighty times".** Zajímavé je, že správné
číslo je **dramatičtější** než to špatné — chyba tady video oslabovala.

> **Poučení, které patří do `CLAUDE.md`, kdyby se to zopakovalo:**
> obě chyby mají tentýž tvar — hodnota spočítaná pro **kulatou
> zeměpisnou šířku** a pak popsaná jako **konkrétní místo**. Vypadá to
> jako ověřené číslo, protože výpočet proběhl; jen se počítal jiný bod,
> než o kterém věta mluví. Chytilo to až vypsání skutečných souřadnic.

> **Bude to na běžné mapě vidět?** Ano. Standardní Mercatorova mapa se
> ořezává kolem 82–85° s. š. (Web Mercator přesně na 85,051°), takže
> mys Morris Jesup na ní obvykle je.

## S19 — Grónsko je menší než Kongo i Alžírsko

> *„It is smaller than the Congo. It is smaller than Algeria."*

| | rozloha | poměr ke Grónsku |
|---|---|---|
| Alžírsko | **2 381 741 km²** | 1,10× |
| Konžská demokratická republika | **2 344 858 km²** | 1,08× |
| Grónsko | 2 166 086 km² | — |

✅ **Obojí sedí.**

> **Saúdská Arábie do té dvojice NEPATŘÍ** (2 149 690 km², tedy o 0,8 %
> **menší** než Grónsko), i když se v podobných výčtech objevuje.
> Ve scénáři není.

## S19 — Jižní Amerika je víc než osmkrát větší

> *„South America, which looks about the same on the map, is more than
> eight times bigger."*

17 840 000 / 2 166 086 = **8,24**

✅ **Sedí**, a *„more than eight"* je správně opatrné.

> Druhá půlka věty — *„looks about the same on the map"* — je
> **vizuální tvrzení a musí sedět v obraze.** Na Mercatoru vychází
> Grónsko o něco menší než Jižní Amerika, ne totožné. Storyboard to
> nesmí nakreslit jako shodnou plochu; „přibližně stejně velké" ano.

## S21 — u pólů je roztažení nekonečné a mapa je ořezaná

> *„And at the poles themselves, the stretching becomes infinite.
> That is why a Mercator world map usually cuts the poles off."*

`y = ln(tan(45° + φ/2))` → pro φ → ±90° roste nade všechny meze,
takže pól na mapě neleží v žádné konečné vzdálenosti.

✅ **Sedí**, včetně *„cannot actually reach them"*. Web Mercator
ořezává na **85,051129°**, aby vyšel čtverec.

## S22, S23, S29 — plochojevná mapa a co pokazí

> *„Africa finally looks like Africa."* / *„Africa is stretched tall
> and thin."* / *„It gets the sizes right by getting the shapes wrong."*

✅ **Sedí.** U válcové plochojevné projekce se poblíž rovníku tvary
protahují **na výšku** a poblíž pólů naopak do šířky — Afrika je
převážně rovníková, takže vyjde vysoká a úzká. Odpovídá to i tomu,
co se té projekci vytýká nejčastěji.

> ⚠️ **Opraveno kvůli jinému problému.** 0.1 měla *„Greenland becomes
> the small island it is."* — jenže Grónsko je **největší ostrov
> světa**. Bylo by to nejsnáze napadnutelné tvrzení celého videa,
> a přitom zbytečné: pointa je, že se zmenší, ne že je malé.
> **0.2: *„And Greenland stops pretending."***

## S25–S27 — Boston, 2017

> *„In 2017, the public schools in Boston took the Mercator maps
> off their classroom walls. They replaced them with
> an equal-area map, in the second, seventh and eleventh grades. They
> were the first school district in the country to do it."*

Bostonské veřejné školy zavedly Petersovu projekci v **březnu 2017**,
ve výuce společenských věd ve **druhém, sedmém a jedenáctém ročníku**.
Obvod se označil za **první školní obvod v USA**, který to udělal.

✅ **Sedí, včetně ročníků i prvenství.**

> **Prvenství je opatrně formulované i ve zdrojích** („the district
> said it was the first"). Scénář říká *„they were the first school
> district in the country to do it"*, což je o stupeň silnější než
> „tvrdily, že jsou". Ponecháno: tvrzení nikdo nezpochybnil a je to
> dobově doložené. Kdyby přišel dotaz v komentářích, odpověď je, že
> jde o vlastní vyjádření obvodu.

> **Jméno projekce ve scénáři NENÍ, a je to záměr** (rozhodnuto
> v `zpetna vazba.txt`). Kdyby padlo *Gall–Peters*, video si o tu
> debatu říká samo — a ta debata není jeho pointa. „An equal-area map"
> je věcně správné a dramaturgicky bezpečné.

> **Motiv je podán jednou větou a bez hodnocení:** *„children spend
> years looking at a world where some continents are quietly inflated."*
> To je popis argumentu, ne jeho převzetí. S28 a S29 pak ukazují,
> že nová mapa **taky není pravdivá**.

## S34 — Země se u rovníku vydouvá o dvacet jedna kilometrů

> *„The Earth isn't a sphere. It bulges at the equator by about
> twenty-one kilometres."*

| | poloměr |
|---|---|
| rovníkový (WGS 84) | 6 378,137 km |
| polární | 6 356,752 km |
| **rozdíl** | **21,385 km** |

✅ **Sedí.** Je to rozdíl **poloměrů**, což je obvyklý způsob, jak se
zploštění uvádí (v průměrech by to bylo 42,8 km). Věta mluví o vydutí
na jedné straně, takže poloměr je ta správná veličina.

## S34, S35, S36 — školní globus

Všechna tři čísla počítám pro **globus o průměru 30 cm**, což je běžná
velikost školního i stolního globusu. Průměr Země 12 742 km.

| co | skutečnost | **na 30cm globu** |
|---|---|---|
| zploštění | 21,385 km | **0,503 mm** ✅ „half a millimetre" |
| Mount Everest | 8 848,86 m | **0,208 mm** ✅ „two tenths of a millimetre" |
| měřítko | — | **1 : 42,5 milionu** ✅ „about forty million times smaller" |

✅ **Všechno sedí**, měřítko je zaokrouhlené dolů a *„about"* to kryje.

> ⚠️ **Opraveno kvůli soudržnosti, ne kvůli faktu.** 0.1 měla v S36
> *„A globe on a desk"*, zatímco S34 a S35 mluví o *„a school globe"*.
> Kdyby to byly dva různé globusy, čísla by spolu nesouvisela.
> **0.2: *„A globe like that"***, takže všechna tři čísla platí
> pro tentýž předmět.

> **Výška Everestu je 8 848,86 m** (společné čínsko-nepálské měření
> z roku 2020). Na výsledku to nic nemění — starší 8 848 m dá
> 0,2082 mm místo 0,2083 mm.

## S38 — globus se tiskne na dvanáct pásů

> *„It is printed flat. Usually on twelve tapered strips, which are
> then pasted onto a ball."*

Pásy se jmenují **gores** a bývá jich **dvanáct nebo osmnáct**;
dvanáct po 30° zeměpisné délky je standard a používá se od
šestnáctého století (Johannes Schöner) dodnes.

✅ **Sedí**, a *„usually"* ten rozptyl pokrývá.

> Tohle je tvrzení, na kterém stojí callback S38b–S39, takže stálo za
> to ho ověřit pořádně: ano, opravdu se tiskne **na plocho** a teprve
> pak lepí na kouli. Zkreslení tedy nezmizelo, jen se rozdělilo mezi
> dvanáct dost úzkých kusů, aby ho papír unesl.

## S42 — Harry Beck, 1933

> *„In 1933, London Underground published a diagram by an engineering
> draughtsman called Harry Beck."*

Henry Charles Beck (1902–1974) pracoval jako **engineering draughtsman**
v signalizační kanceláři London Underground. Diagram nakreslil
v roce **1931**, podnik ho nejdřív odmítl a vytiskl až v **lednu 1933**
v 700 000 kapesních výtiscích.

✅ **Sedí přesně tak, jak je to napsané.** Věta říká *„published"*,
ne „drew" ani „designed" — 1933 je rok vydání, 1931 rok vzniku.
Kdyby tam stálo „created", byla by to chyba.

## S44, S45 — Leicester Square a Covent Garden

> *„Leicester Square and Covent Garden are two hundred and sixty metres
> apart. It is the shortest gap on the whole network."* /
> *„The train takes forty-five seconds. Walking takes four minutes."*

Úsek Piccadilly line mezi těmi stanicemi měří **260 m** a je
**nejkratší mezistaniční vzdáleností celého londýnského metra**.
Jízda trvá **45 sekund**, pěší cesta po povrchu **čtyři minuty**.

✅ **Všechno sedí.**

> **Tvrzení *„people still take the train"* je měkčí než ta čísla**
> a je to záměr. Doložit se dá, že ta jízda je populární a že TfL
> na to upozorňuje; přesný počet lidí, kteří ji ročně absolvují
> zbytečně, doložit nejde. Scénář proto netvrdí „tisíce lidí denně",
> nýbrž jen že se to děje.

## S49 — mapa v telefonu je pořád Mercator

> *„Because it is still Mercator. Zoom in on your own street, and you
> are looking at a projection designed for sixteenth century sailors."*

Google Maps, OpenStreetMap, Bing i Mapbox používají **Web Mercator**
(EPSG:3857). Je to Mercator počítaný jako by Země byla koule,
i když souřadnice jsou elipsoidní — pro dlaždicové mapy je to
standard.

✅ **Sedí**, a *„sixteenth century"* sedí taky (1569).

> **Vědomé zjednodušení:** Web Mercator **není totožný** s Mercatorovou
> projekcí z roku 1569 — kulová aproximace posouvá polohy oproti
> elipsoidnímu Mercatoru až o desítky kilometrů a pro navigaci by
> se použít neměla. Scénář říká *„it is still Mercator"*, což je
> pravda v tom smyslu, na kterém stojí pointa (týž typ projekce,
> totéž zkreslení ploch). Rozvádět rozdíl kulové a elipsoidní varianty
> je na tohle video moc.

## S50, S50b — od roku 2018 se při oddálení překlopí na glóbus

> *„Since 2018, if you pull back far enough on a computer, the map
> stops being a map and becomes a globe."*

Google spustil **Globe Mode v srpnu 2018**, tehdy **jen na desktopu**
(přes WebGL); na mobilu zůstal Mercator výchozí.

✅ **Sedí, včetně toho „on a computer".** Ta tři slova tam nejsou
navíc — bez nich by to byla chyba pro každého, kdo si to zkusí
na telefonu.

---

## Co jsme nechali jako vědomé zjednodušení

| | |
|---|---|
| **„the curvature of a surface belongs to the surface itself"** (S08) | přesně jde o **Gaussovu** křivost a o to, že je vyjádřitelná z první fundamentální formy. Formulace je popularizace, ne nepřesnost |
| **„it is still Mercator"** (S49) | Web Mercator je kulová varianta, ne Mercator z roku 1569. Pro tvrzení videa (totéž zkreslení ploch) to platí |

## Co musí ověřit STORYBOARD, ne text

Tři tvrzení tohohle videa nejsou ve větách, nýbrž v obraze — a `CLAUDE.md`
má naměřeno, že takové tvrzení fact check textu nenajde:

1. **S19** — *„South America, which looks about the same on the map"*.
   Na Mercatoru je Grónsko o něco **menší** než Jižní Amerika.
   Kresba je nesmí udělat shodné.
2. **S20** — Grónsko se posouvá k rovníku a zmenšuje. Poměr velikostí
   v každé poloze musí odpovídat `sec²φ`, jinak diagram tvrdí jiné
   číslo než S17 a S18.
3. **S38** — dvanáct pásů, ne šest a ne dvacet. Je to jediné číslo
   scény a v hlasu zazní.


---

## Letopočty se ve scénáři píšou ČÍSLICEMI (od `script 0.5.md`)

Do 0.4 byly vypsané slovy (*„In two thousand and seventeen"*), protože
to tak žádá kapitola „Formát `script.md`" v `CLAUDE.md`. **V titulcích
to ale vypadá jako strojový text** — nahlásil uživatel na S25.

Ta kapitola je starší než funkce `pronounce`. Poslední videa kanálu
(039, 041, 042) mají letopočty ve `script.md` **číslicemi** a Kokorovi
podstrkují slovní tvar až těsně před syntézou. Tím se rozdělí to, co
**divák čte**, od toho, co **hlas říká**:

| scéna | ve scénáři a v titulcích | co řekne Kokoro |
|---|---|---|
| S08 | `1827` | eighteen twenty-seven |
| S13 | `1569` | fifteen sixty-nine |
| S25 | `2017` | twenty seventeen |
| S42 | `1933` | nineteen thirty-three |
| S50 | `2018` | twenty eighteen |

Tvar `20xx` je **„twenty seventeen"**, ne „two thousand and seventeen" —
tak to má i video 042.

> **Množství zůstávají slovy** (*„fourteen times"*, *„more than eighty
> times"*, *„two hundred and sixty metres"*). Konvence kanálu je
> letopočet a označení verze číslicí, počet slovem — 042 má
> *„Fifty-six years earlier"* a zároveň *„In 1966"*.

> **Pozor na odhad stopáže:** naivní slabikovač z `CLAUDE.md` neumí
> číslice vůbec — `2017` nemá v regexu `[aeiouy]` jedinou samohlásku
> a spadne na `max(…, 1)`, ačkoli zazní pět slabik. Je to táž past jako
> `GDP` u videa 036. Do slabikovače pro tohle video patří ručně
> `{'1569': 4, '1827': 5, '1933': 5, '2017': 4, '2018': 4}`.
