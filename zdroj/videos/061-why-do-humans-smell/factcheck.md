# Fact check — 061 „Why Do Humans Smell?"

Proti `script.md` verze **0.4** (110 scén + CTA). Ověřováno 2026-09-20
a 2026-09-21. Tři tvrzení neprošla a jsou ze scénáře **vyškrtnutá**,
viz kapitola „Co neprošlo" dole.

Legenda: ✅ doloženo primárním nebo odborným zdrojem · ⚠️ doloženo, ale
jen sekundárně nebo se sebevykazujícím zdrojem · ❌ neprošlo.

---

## S01–S04 — „Your sweat does not smell"

| | |
|---|---|
| tvrzení | Čerstvý sekret nepáchne; pach vzniká až potom a nedělá ho tělo |
| ověření | Apokrinní žlázy vylučují **bezpachý** prekurzor; pachovou molekulu uvolní až kožní bakterie. eLife 2018 ho jmenuje doslova *„odourless dipeptide-containing malodour precursor molecule, S-Cys-Gly-3M3SH"* |
| závěr | ✅ |

**S04 „And your body does not make it."** — myšleno *pach*, ne prekurzor.
Doslova pravdivé: 3M3SH vzniká enzymatickým štěpením **uvnitř bakterie**,
ne v lidské tkáni. Scénář si to sám upřesňuje v S15 (*„your body makes
a component"*).

## S05–S06 — ekrinní žlázy

| | |
|---|---|
| tvrzení | Druhá třída žláz je po celém těle, chladí, a ten pot je „almost entirely water" |
| ověření | Ekrinní pot je **~99 % voda**, zbytek hlavně sodík a chlorid; funkce je termoregulace odparem |
| závěr | ✅ |

> Zadání uživatele mělo ekrinní žlázy jako **jediné** zmíněné a přitom
> pachová linka jde přes apokrinní. Opraveno už ve verzi 0.1.

## S07 — apokrinní žlázy

| | |
|---|---|
| tvrzení | Sedí v podpaží a tříslech, naskočí v pubertě |
| ověření | Apokrinní žlázy jsou v axile, tříslech a dvorci bradavky, ústí do vlasového folikulu; existují od narození, ale **výrazná aktivita začíná pubertou** vlivem hormonů |
| závěr | ✅ — „switch on at puberty" je zkratka za „stanou se aktivními", ne za „vzniknou" |

## S08–S09 — „a large, heavy molecule" / „a sulphur atom, wrapped up"

Tohle je nejexponovanější místo scénáře, proto rozepsané.

| | |
|---|---|
| molekula | **Cys-Gly-3M3SH**, plným jménem *S-[1-(2-hydroxyethyl)-1-methylbutyl]-L-cysteinylglycin* |
| souhrnný vzorec | **C₁₂H₂₄N₂O₄S** |
| hmotnost (spočítáno z atomových hmotností, ne opsáno) | **292,4 g/mol** |
| pachová molekula, která z ní vznikne | **3M3SH**, C₇H₁₆OS, **148,3 g/mol** |
| poměr | prekurzor je **1,97× těžší** než výsledný odorant |

Takže **„large, heavy" obstojí** — prekurzor je doslova zhruba dvojnásobek
hmotnosti toho, co nakonec letí vzduchem.

> **Ale příčina netěkavosti NENÍ hmotnost, nýbrž ta „wrapping".**
> 292 g/mol je na těkavou látku běžná hmotnost; netěkavý je prekurzor
> proto, že je to **polární dipeptidový konjugát** (volná aminoskupina,
> karboxyl, peptidová vazba), který drží vodíkovými můstky. Scénář to
> naštěstí přisuzuje správně — S09 říká *„wrapped up so that it cannot
> fly"*, ne „too heavy to fly". **Kdyby se S08 a S09 někdy přeformulovaly,
> tohle rozlišení se musí udržet.**

## S10 — pach musí cestovat

Triviálně pravdivé: čichový vjem vyžaduje molekulu v plynné fázi, která
dorazí k čichovému epitelu. ✅

## S11–S14 — bakterie a dva enzymy

| krok scénáře | co se doopravdy děje |
|---|---|
| *„Then a bacterium finds it."* | ***Staphylococcus hominis***, dál *S. haemolyticus* a *S. lugdunensis* |
| *„It carries the right tools."* | prekurzor si vtáhne dovnitř peptidovým transportérem (**PepTSh / DtpT**, rodina POT) |
| *„One enzyme trims the wrapping."* | **dipeptidáza PepV** odštěpí koncový glycin → Cys-3M3SH |
| *„A second enzyme cuts the bond holding the sulphur in place."* | **cystein-S-konjugát β-lyáza (PatB)** rozetne vazbu C–S a uvolní thiol, k tomu amoniak a pyruvát |
| *„the thing that floats away is the smell"* | **3M3SH**, popisovaný jako „highly pungent" |

**✅ Pořadí i počet enzymů sedí.** Zdroje: eLife 2018 (*Structural basis
of malodour precursor transport in the human axilla*), J Biol Chem /
PMC11742315 (*Identification of a staphylococcal dipeptidase involved in
the production of human body odor*), Sci Rep 2020 (*The molecular basis of
thioalcohol production in human body odour*).

> Pozn.: „cuts the bond holding the sulphur in place" je přesné —
> β-lyáza štěpí vazbu **C–S**, takže síra odchází **s** uvolněným
> thiolem, ne od něj.

## S18–S19 — „a few parts per billion"

| | |
|---|---|
| ověření | Naměřené prahy detekce pro aldehydy: propanal 2,0 ppb, dále 0,46 / 0,33 / 0,17 ppb, nonanal 0,53 ppb; **oktanal a helional 0,14 ppb** |
| závěr | ✅ **konzervativní** — „jednotky miliardtin" je spíš horní odhad, u nejsilnějších odorantů je práh ještě o řád níž |

> **S19 je opravená verze.** Do 0.2 tam stálo *„One molecule in a billion
> others"*, což tvrdí víc než S18. Nález ze zpětné vazby k 0.2, přijat.
>
> A ve zdrojovém textu uživatele stálo *„There can be billions of
> molecules of air"* — to je **o deset řádů vedle** (v cm³ vzduchu je
> ~2,5 × 10¹⁹ molekul). Proto scénář mluví o **poměru**, ne o počtu.

## S23 — „older than soap, older than cities, older than words"

| | |
|---|---|
| chemorecepce | základní smysl přítomný už u bakterií (chemotaxe); obratlovčí rodiny čichových receptorových genů jsou staré **stovky milionů let** |
| mýdlo | doloženo v Mezopotámii kolem 2800 př. n. l. |
| města | Uruk a spol., 4. tisíciletí př. n. l. |
| jazyk | horní odhad **statisíce až jednotky milionů let** |
| závěr | ✅ u všech tří, a u „words" **s největší rezervou ze všech** |

> Zpětná vazba k 0.2 navrhovala *„older than words"* nahradit
> *„older than civilization"*, protože prý neznáme dobu vzniku jazyka.
> **Nepřijato:** přesné datum není potřeba, stačí horní mez — a ta je
> o řády mladší než čich. Navrhovaná náhrada je navíc slabší, protože
> jen opakuje „cities".

## S29–S39 — Joy Milne

| tvrzení scénáře | ověření |
|---|---|
| skotská zdravotní sestra | ✅ zdravotní sestra ve výslužbě, Skotsko |
| pach „woody, musky" | ✅ doslovný popis z jejích vlastních výpovědí |
| **dvanáct let** před diagnózou | ✅ |
| souvislost jí došla na setkání pacientů | ✅ *„ti lidé v té místnosti voní stejně jako ty"* |
| **dvanáct triček, šest a šest** | ✅ pilotní test, Tilo Kunath, Univerzita v Edinburghu, po setkání v roce 2012 |
| určila **všech šest** | ✅ |
| označila i sedmé, „zdravé" | ✅ |
| ten člověk byl diagnostikován **za devět měsíců** | ✅ |
| pach dohledán do **kožního mazu na horní části zad** | ✅ Perdita Barran, Manchester |

> **Tady fact check našel chybu.** Do verze 0.2 stálo *„less than a year
> later"*, což je to, co píše většina sekundárních převyprávění.
> Konkrétnější zdroje uvádějí **devět měsíců**. Opraveno.
>
> A druhá věc: pohlaví té kontrolní osoby **žádný zdroj neuvádí**,
> takže scénář říká *„That person… They were diagnosed"*, ne „that man".

## S41–S44 — chemický podpis

| | |
|---|---|
| tvrzení | Každý člověk nese trochu jinou směs; podíl má vlastní chemie, konkrétní kožní bakterie, strava, prostředí, oblečení |
| ověření | Individuální kožní „volatilom" je doložený; složení určuje jak hostitel, tak kožní mikrobiom, a moduluje ho strava i prostředí |
| závěr | ✅ — ale **záměrně jako „slightly different", ne „unique"**. Tvrzení o jednoznačné identifikovatelnosti by bylo silnější, než co zdroje unesou |

## S44b–S44i — feromony a psi

| | |
|---|---|
| tvrzení | *„People reach for the word pheromone. In humans, not one has ever been found."* |
| ověření | Wyatt, *Proc R Soc B* 282:20142994 (2015): pro žádnou ze čtyř nejčastěji uváděných molekul (androstenon, androstenol, androstadienon, estratetraenol) neexistuje pořádný důkaz vedený bioesejí. Doslova *„We do not yet know if humans have pheromones."* |
| závěr | ✅ — a scénář to **tvrdí právě v té opatrné podobě**: neříká „feromony neexistují", nýbrž že se žádný nenašel |

| | |
|---|---|
| tvrzení | *„Four dogs in Belfast were given breath and sweat from one person, calm, and then under pressure. They found the stressed sample in ninety-four per cent of seven hundred and twenty trials."* |
| ověření | Wilson et al., *PLOS ONE* 2022 (Queen's University Belfast). Dvojitě zaslepený tříalternativní výběr, vzorky dechu a potu od **36 lidí** před stresovou úlohou a po ní (počítání zpaměti), **4 psi**, **720 pokusů**. Úspěšnost **93,75 %** (rozpětí 90,00 az 96,88 %), binomický test p < 0,001 |
| závěr | ✅ — „ninety-four per cent" je 93,75 zaokrouhlených nahoru. **Klíčové je „from one person"**: psi rozlišovali klidný a stresový vzorek TÉHOŽ člověka, ne dva různé lidi. Bez toho by tvrzení nedokládalo nic |

| | |
|---|---|
| tvrzení | *„Human fear sweat raises a dog's heart rate and sends it looking for its owner."* |
| ověření | D'Aniello et al., *Animal Cognition* 21:67–78 (2018). Psi vystavení lidskému potu strachu vykazovali víc chování směrem k majiteli, **vyšší tepovou frekvenci** a víc známek stresu; u potu z radosti naopak víc chování k *cizímu* člověku |
| závěr | ✅ — a je to jiné tvrzení než to předchozí: Belfast dokládá ROZPOZNÁNÍ, tohle PŘENOS. Scénář je proto odděluje větou *„And it goes further than detection."* |

| | |
|---|---|
| tvrzení | *„It never saw a face."* |
| ověření | V belfastské studii dostával pes vzorek v nádobě, bez přítomnosti dárce; u D'Aniella šel pach z dávkovače a dárci vzorků se pokusu neúčastnili |
| závěr | ✅ — obě uspořádání zrakový vjem dárce vylučují. **Neříká se, že pes pozná emoci „dřív, než ji uvidí"** — to by byl závod dvou smyslů, který ani jedna studie neměřila |

## S45–S50 — pelyněk a tabák

| tvrzení scénáře | ověření |
|---|---|
| přistřižený pelyněk uvolní těkavé látky | ✅ Karban a spol., damage-induced volatiles |
| sousední **tabák divoký** utrpí prokazatelně menší škody | ✅ přes tři polní sezóny, menší poškození listů |
| **od kobylek a housenek** | ✅ grasshoppers a cutworms; cutworm je housenka, ne červ |
| dosah **pod patnáct centimetrů** | ✅ mezidruhově pelyněk↔tabák **<10–15 cm**; vnitrodruhově u pelyňku <60 cm |

> **Tohle číslo se opravovalo.** Verze 0.1 měla „under sixty centimetres",
> jenže šedesát platí pro **vnitrodruhovou** komunikaci pelyňku s pelyňkem.
> Scéna mluví o dvojici pelyněk→tabák, tedy o **mezidruhovém** případu,
> kde platí patnáct. Opraveno, a je to i působivější.

## S53–S56 — znechucení

Filozofické tvrzení („molekula nenese názor") plus obecně přijímaná
funkce znechucení jako ochrany před patogeny a zkaženou potravou.
Není to číselné tvrzení a scénář z něj nic kvantitativního nevyvozuje. ✅

## S60–S67 — rok 1919 a Odorono

| tvrzení scénáře | ověření |
|---|---|
| rok **1919** | ✅ |
| agentura **J. Walter Thompson** | ✅ |
| textař **James Webb Young** | ✅ — **jméno opraveno**, scénář do 0.3 psal jen „James Young" |
| přípravek **Odorono** (aluminium-chloridový roztok) | ✅ |
| prodeje stály; **dvě ženy ze tří** si nemyslely, že jde o ně | ✅ Youngův vlastní průzkum. **Dvě opravy najednou:** scénář do 0.8 psal *„Nobody felt they needed it"*, což (a) přestřelovalo — byly to dvě třetiny, ne všichni — a (b) odporovalo S68 *„People had minded the smell for centuries."* Rozpor našel uživatel. Rozpouští se tím, že lidem pach vadil obecně, jen si nemysleli, že zdrojem jsou ONI — a přesně na tom stál inzerát: žena může obtěžovat a dozví se to poslední |
| inzerát v **Ladies' Home Journal** | ✅ |
| titulek **„Within the Curve of a Woman's Arm"** | ✅ |
| podtitul **„A frank discussion of a subject too often avoided"** | ✅ |
| **dvě stě** čtenářek zrušilo předplatné | ⚠️ ✅ v tom smyslu, že to **říká sám Young** ve vzpomínkách („some 200 … and publishers begged us to stop the copy"). Je to tedy **sebevykazující zdroj**; nezávisle to potvrzené není |
| kolegyně s ním přestaly mluvit | ⚠️ táž pasáž, týž zdroj |
| **+112 % za rok** | ✅ a upřesněno: na **417 000 dolarů v roce 1920** |

> Dvě položky ⚠️ nesou tutéž vadu: pocházejí z memoárů člověka, jehož
> historku dělají působivější. **Do videa jsou ponechané**, protože
> nejde o fyzikální fakt, nýbrž o dobově doloženou anekdotu, a scénář
> je nepoužívá jako důkaz — nese ho těch +112 %. Kdyby se na to ptal
> divák, tahle věta je odpověď.

## S68–S69 — „None of which invented the shame"

| | |
|---|---|
| tvrzení | Lidé pach řešili staletí předtím — lázně, parfém, mýdlo |
| ověření | Mýdlo doloženo ~2800 př. n. l., parfumerie ve starém Egyptě, římské lázně jako společenská instituce |
| závěr | ✅ |

> **Tahle dvojice scén ve verzi 0.1 vůbec nebyla a byla to věcná chyba.**
> Stálo tam *„Before it, bodies smelled. After it, people smelled bad."*,
> což dělá z roku 1919 okamžik vzniku studu. Nález ze zpětné vazby
> k 0.1, přijat: 1919 vysvětluje vznik **obchodu**, ne vznik studu.

## S74 — „antibacterial metals into socks"

| | |
|---|---|
| ověření | Stříbrné nanočástice se do textilu zavádějí právě proto, že potlačují růst bakterií tvořících pach; testováno mj. proti *Staphylococcus aureus* a *S. epidermidis* |
| závěr | ✅ (a jako bonus: praním se uvolní 1,3 az 35 % obsaženého stříbra, což je vlastní ekologické téma — do videa nepatří) |

## S77–S81 — pumpa, dědičnost, východní Asie

**Scénář vědomě NEJMENUJE gen** (viz `notes.md`, rozhodnutí o `ABCC11`).
Ověřeno je ale celé, aby se dalo odpovědět v komentářích:

| tvrzení scénáře | ověření |
|---|---|
| prekurzor musí ze žlázy vytlačit **pumpa** | ✅ transportér **ABCC11** přenáší SG-3M3SH do apokrinních sekrečních váčků |
| u některých lidí **skoro nefunguje** | ✅ záměna **538G→A**; homozygotům `A/A` se charakteristické pachové složky v axilárním potu prakticky netvoří |
| **dědí se** | ✅ jednonukleotidový polymorfismus |
| **není to vzácné** a ve východní Asii je to **většina** | ✅ podíl genotypu `A/A`: **Tokio ~79 %** (frekvence alely G 0,111), Evropa **~1,6 %** (G 0,875), Yorubové **~0 %** (G 1,000). Jiné práce uvádějí pro východní Asii 80–95 % |
| doklad z opačné strany | ✅ ze 79 pacientů léčených pro axilární osmidrózu neslo alelu G **78, tedy 98,7 %**, proti 35,4 % v populaci |

> Táž záměna určuje i **typ ušního mazu** (suchý u `A/A`). Ve videu to
> není — patří dalšímu videu.

## S84–S85 — Japonsko

| tvrzení scénáře | ověření |
|---|---|
| Japonsko má deodorantový průmysl i tak | ✅ P&G Japan, Mandom, Rohto, Kao; preferovaná „vůně" je **bez vůně** |
| **„sumehara"**, スメハラ, pachové obtěžování | ✅ zavedený japonský výraz pro obtěžování druhých tělesným pachem |

## S92 — oxid uhelnatý

Bez barvy, bez zápachu, bez chuti; otrava probíhá nenápadně a k úmrtím
dochází typicky ve spánku. ✅

## S99–S103 — návrat k molekulám

*„Enough to put you in a kitchen you have not stood in for twenty years"*
je odkaz na **pachem vyvolanou autobiografickou paměť** (Proustův jev),
což je studovaný a doložený efekt. Scénář z něj nevyvozuje žádné číslo. ✅

*„a system that is older than language"* — viz S23. ✅

---

## Co NEPROŠLO a je ze scénáře pryč

### ❌ „B.O." pochází z kampaně Odorono 1919

Verze 0.3 měla scénu:

> *And the same campaign / handed the English language / the abbreviation B.O.*

**Zdroje si odporují a ten nejsilnější tvrdí něco jiného:**

| zdroj | co říká |
|---|---|
| **etymonline** (lexikografie) | *„by c. 1950, an abbreviation of body odor; an advertisers' invention"* — **žádný rok 1919 a žádné Odorono** |
| cosmeticsandskin (dějiny kosmetiky) | zkratku spojuje s **Lifebuoy**, kampaň datuje do roku **1935** |
| populární převyprávění | „Odo-Ro-No vymyslelo, Lifebuoy zpopularizovalo" (1919 / 1933) |

Tři různá datování (1919 / 1935 / kolem 1950) a odborný zdroj nejmladší
z nich. **Scéna vyškrtnuta celá.** Argument videa ji nepotřebuje a platí
pravidlo z `CLAUDE.md`: *„Slabé ověření je horší než žádné, protože
vypadá jako doklad."*

### ❌ „Japonský trh s deodoranty vzrostl o pětinu za čtyři roky"

Verze 0.3 měla u S85 číslo (růst na 1,2násobek mezi roky 2013 a 2017).
**Stopa vede k jedinému zdroji: vlastnímu průzkumu firmy Mandom**, tedy
**výrobce deodorantů**, a k tomu jen přes konzultantský blog. Je to
strana, která má zájem na tvrzení „trh roste".

Číslo vyškrtnuto, věta zkrácena na *„Japan has a deodorant industry
anyway."* **Argument tím neztratí nic**, protože stojí na rozporu
(skoro žádný pach, a přesto průmysl a vlastní slovo pro pachové
obtěžování), ne na velikosti růstu.

### ❌ „Every human being produces body odors"

Hlavní teze **zdrojového textu uživatele**, ne scénáře — do žádné verze
scénáře se nedostala. Neplatí kvůli `ABCC11`; rozbor je v `notes.md`.

---

## Co scénář ZÁMĚRNĚ netvrdí

Zvažováno a nedáno tam, protože by to neuneslo fact check:

| | proč ne |
|---|---|
| **MHC a „potní trička"** (Wedekind 1995) | replikace je sporná |
| ~~**lidské feromony**~~ | **Od verze 0.8 ve scénáři JSOU**, ale jen jako „žádný se nenašel" (S44c). Wyatt (2015) nedokládá neexistenci, nýbrž absenci důkazu — a přesně tak to scénář říká |
| **„lidé rozliší bilion pachů"** (Bushdid 2014) | Gerkin & Castro (2015) to metodicky vyvrátili |
| **merkaptan v plynu a New London 1937** | doložitelné, ale je to odbočka — viz `notes.md` |

---

## Zdroje

- eLife 2018, *Structural basis of malodour precursor transport in the human axilla* — https://elifesciences.org/articles/34995
- J Biol Chem 2025 / PMC11742315, *Identification of a staphylococcal dipeptidase involved in the production of human body odor* — https://pmc.ncbi.nlm.nih.gov/articles/PMC11742315/
- Sci Rep 2020, *The molecular basis of thioalcohol production in human body odour* — https://www.nature.com/articles/s41598-020-68860-z
- PMC2731057, *A strong association of axillary osmidrosis with the wet earwax type determined by genotyping of the ABCC11 gene*
- J Invest Dermatol 2009, *A functional ABCC11 allele is essential in the biochemical formation of human axillary odor* — https://pubmed.ncbi.nlm.nih.gov/19710689/
- Karban & Baldwin a navazující práce k pelyňku a tabáku — https://esajournals.onlinelibrary.wiley.com/doi/10.1890/0012-9658(2006)87%5B922:DRISVA%5D2.0.CO;2
- Edinburgh Impact, *Discovering the smell of Parkinson's* — https://impact.ed.ac.uk/research/future-health-and-care/discovering-the-smell-of-parkinsons/
- Science History Institute, *The Smell of Shame* — https://www.sciencehistory.org/stories/distillations-pod/the-smell-of-shame/
- Cosmetics and Skin, *Odorono* — https://www.cosmeticsandskin.com/companies/odorono.php
- etymonline, *b.o.* — https://www.etymonline.com/word/b.o.
- Tokyoesque, *Smell harassment and the Japanese personal care industry* — https://tokyoesque.com/smell-harassment-japanese-personal-care-industry/
- PLOS ONE 2022, *Dogs can discriminate between human baseline and psychological stress condition odours* — https://journals.plos.org/plosone/article?id=10.1371%2Fjournal.pone.0274143
- Animal Cognition 21:67–78 (2018), *Interspecies transmission of emotional information via chemosignals: from humans to dogs* — https://link.springer.com/article/10.1007/s10071-017-1139-x
- Proc R Soc B 282:20142994 (2015), Wyatt, *The search for human pheromones: the lost decades and the necessity of returning to first principles* — https://royalsocietypublishing.org/doi/10.1098/rspb.2014.2994
