# Fact check — 036 What Is GDP — And Why Doesn't It Tell You Everything?

Ověřováno proti `script 0.3.md` dne 2026-09-09. **Dva nálezy byly
opravené a scénář je od té chvíle `script 0.4.md`** — viz S54 a S73,
u obou je zapsáno „teď" i „bylo". Metoda podle CLAUDE.md:
vypsat **každé** ověřitelné tvrzení, ne jen ta, která vypadají riziková,
**počítat, ne vzpomínat**, a **zobecnění brát jen z primárního zdroje**.

Uživatel si k tomuhle videu vyžádal navíc, ať se nebere jako
samozřejmost ani „bezriziková" definice — a měl pravdu: **dvě z nich
skončily s výhradou**, viz S54 a S58.

## Primární zdroje

| zkratka | co to je | jak získáno |
|---|---|---|
| **SNA2008** | *System of National Accounts 2008*, EC / IMF / OECD / UN / World Bank | plné PDF (9,5 MB), `pdftotext -layout` |
| **KUZ1934** | Kuznets, S.: *National Income, 1929–32*. Senate Document No. 124, 73. Kongres, 2. zasedání, 4. ledna 1934 | plné PDF (10,3 MB) z FRASER, `pdftotext -layout` |
| **BEA55** | BEA FAQ: *How are GDP and related income measures of the national accounts affected by a disaster?* | `WebFetch`, `bea.gov/help/faq/55` a `/1013` |

```
SNA2008   sha256 854883ffc5769747480561c78ba4099ec40257ca8f44d91a85f654b5e715a9b6
          https://unstats.un.org/unsd/nationalaccount/docs/sna2008.pdf
KUZ1934   sha256 f4ce9435d110339bc34ef3d938ef795c4b9c5d7d8097448aac8cfde695992d73
          https://fraser.stlouisfed.org/files/docs/publications/natincome_1934/19340104_nationalinc.pdf
```

> **Jeden citát ze sekundárního zdroje NEPROŠEL a je to varování.**
> Vyhledávač vrátil větu *„GDP … is not directly affected by the loss of
> property …, **except to the extent that it affects production
> capacity**"* jako doslovnou citaci BEA. **V BEA FAQ ta klauzule
> není** — ověřeno stažením obou verzí FAQ (55 i 1013). Věcně je ta
> úvaha správná, ale **nesmí se připsat BEA**; v tomhle dokumentu je
> proto vedená jako moje úvaha, ne jako citace. Je to přesně past
> „sekundární zdroj použitý na zobecnění" z CLAUDE.md.

---

## Souhrn

| | scén |
|---|---|
| ✅ doloženo primárně | 96 |
| ⚠️ doloženo, ale formulace je zjednodušení (ponecháno, vědět o tom) | 3 — S08, S18, S58 |
| ⚠️ nepřesnost, **opravena** ve 0.4 | 1 — S54 |
| ❌ formulace neobstála, **opravena** ve 0.4 | **1 — S73** |

---

## S01–S03, S19–S25 — hurikán zvýší HDP

✅ **Doloženo primárně, a shodou okolností úplně stejným příkladem.**

SNA2008 §1.80 mluví přímo o hurikánech a o rekonstrukci:

> „There may even be a general tendency for production to rise to remedy
> the harmful effects of events that reduce people's welfare in a broad
> sense. For example, production may be expected to increase in order to
> **repair the damage caused by such natural disasters as earthquakes,
> hurricanes and floods**."

A §1.79 dodává závěr, který video dělá v S26:

> „**Total welfare could fall even though GDP could increase in volume
> terms.**"

Účetní mechanismus doplňuje BEA55:

> „GDP is a measure of the nation's *current* production of goods and
> services; as such, it is not directly affected by the loss of property
> (structures and equipment) produced in previous periods."
>
> „**Neither GDP nor the associated income measures are adjusted to take
> account of damage to, or destruction of, assets due to a catastrophic
> event.**"
>
> „Rebuilding activity, which may occur over many months following
> a disaster, will typically be reflected in the regular source data that
> are used to estimate residential and nonresidential investment."

Zničený majetek se zapisuje mimo HDP, do účtu **„other changes in volume
of assets"** (BEA55; SNA2008 §12.46, §3.7).

> **Sloveso „can" je tady nutné a scénář ho má.** Čistý dopad velké
> katastrofy na HDP je krátkodobě často **záporný**, protože zničené
> kapacity přestanou vyrábět. Scénář nikde netvrdí, že HDP po katastrofě
> vzroste — S03 říká *„GDP **can** go up"* a S25 *„So GDP **can**
> increase after a disaster."* ✅ Kdyby se „can" při dalších úpravách
> ztratilo, tvrzení přestane platit.

Dílčí položky S22–S23 (stavební firmy, mzdy, materiál, vládní opravy
infrastruktury) jsou všechno tržní produkce, resp. vládní výdaje —
v HDP ✅.

## S05 — „one of the most important numbers in economics"

✅ SNA2008 §19.12: *„The growth rate in the volume of GDP is **one of the
key economic indicators** provided by the national accounts."*

## S07 — „GDP stands for gross domestic product"

✅ Triviálně.

## S08 — definice HDP

> *„In simple terms, it measures the market value of all final goods and
> services produced within a country's borders, during a certain period
> of time."*

Rozebráno po částech, protože si to uživatel výslovně vyžádal:

| část | doklad | |
|---|---|---|
| *market value* | SNA2008 §A4.24: GDP = součet hrubé přidané hodnoty v základních cenách **plus daně minus dotace na produkty**, tedy v tržních cenách | ✅ |
| *all final goods and services* | SNA2008 §16.47 (výdajová metoda): *„expenditure on final consumption plus gross capital formation plus exports less imports"* — mezispotřeba se odečítá | ✅ |
| *during a certain period of time* | SNA2008 §3.2: *„Flows measure changes in economic value **over a period of time**."* | ✅ |
| *within a country's borders* | SNA2008 §2.19 | ⚠️ **zjednodušení** |

⚠️ **K poslednímu řádku.** Technické kritérium není hranice, nýbrž
**rezidence v ekonomickém území**:

> „It consists of all the institutional units which are **resident** in
> the economic territory of a country. The economic territory of
> a country, **although consisting essentially of the geographical
> territory, does not coincide exactly**; some additions and subtractions
> are made. … An institutional unit is said to be a resident unit of
> a country when it has a centre of predominant economic interest in the
> economic territory of that country."

Standard tedy sám říká, že ekonomické území je *v podstatě* území
zeměpisné. **Ponecháno**: je to obvyklé populární zjednodušení, odchylky
(ambasády, offshore zařízení) by v devítiminutovém videu zabraly víc
místa, než kolik přinesou. Kdyby se na to někdo ptal v komentářích,
tohle je odpověď.

## S09 — „a year or a quarter"

✅ Obvyklá referenční období národních účtů; SNA2008 věnuje čtvrtletním
účtům vlastní pasáže a odkazuje na *Quarterly National Accounts Manual*
(IMF).

## S10–S13 — auta, software, restaurace, stavby

✅ Všechno tržní produkce dodávaná jiným jednotkám, tedy uvnitř hranice
produkce — SNA2008 §6.27(a).

## S15–S18 — k čemu GDP je

✅ SNA2008 §19.12: *„Such growth rates can be compared directly between
countries because they are expressed in common units (percentage
changes) and are not affected by the currency…"*

⚠️ **Drobnost, kterou video samo opravuje o dvě minuty později.**
S18 říká, že můžeme srovnávat *„one country with another"*. Přímo
srovnatelné jsou ale **tempa růstu**, kdežto **úrovně** vyžadují PPP —
SNA2008 §19.15. Scénář to nezamlčuje: přesně tohle je obsah S41.
**Ponecháno**, protože tvrzení v S18 je o srovnávání obecně a S41 ho
upřesňuje.

## S26–S28 — HDP měří aktivitu, ne její dobrost

✅ SNA2008 §1.75, tedy sekce nazvaná *„The SNA and measures of welfare"*:

> „**GDP is often taken as a measure of welfare, but the SNA makes no
> claim that this is so** and indeed there are several conventions in the
> SNA that argue against the welfare interpretation of the accounts."

## S30–S33 — stejná produkce, ceny o deset procent výš

✅ **Spočítáno, ne odhadnuto.** Při identických množstvích a všech
cenách ×1,10 je nominální agregát Σp·q přesně ×1,10, tedy **+10,0 %**,
zatímco objemový agregát v cenách základního roku je **+0,0 %**.

Scénář říká *„by **roughly** ten percent"* — hedge je na místě, protože
v realitě se všechny ceny nepohnou stejně a deflátor pak nevyjde
přesně na deset. ✅

## S34–S37 — nominální versus reálné

✅ SNA2008 kapitola 15 *Price and volume measures*, §15.1: změny hodnot
toků *„can be directly factored into two components, one reflecting
changes in the prices … and the other the changes in their volumes."*

*„Real GDP tries to remove the effect of changing prices"* ✅ — deflace
cenovými indexy, resp. dvojitá deflace (§15.2).

## S38–S40 — GDP per capita

✅ HDP dělené počtem obyvatel; SNA2008 §19.12–19.15 (ICP odhaduje
*„absolute levels of GDP and GDP per capita across countries in order to
try to establish a relative level of prosperity"*).

## S41 — PPP

✅ **Doloženo definicí.** SNA2008 §15.199:

> „A purchasing power parity (PPP) is defined as the number of units of
> B's currency that are needed in B to purchase the same quantity of
> individual good or service as one unit of A's currency will purchase
> in A."

A §1.x k tomu dodává důvod: *„It is well known that, in general, neither
market nor fixed exchange rates reflect the relative internal purchasing
powers of different currencies."*

Formulace scénáře *„a dollar doesn't buy the same amount everywhere"* ✅.

## S42–S43 — je to průměr a průměry skrývají rozdíly

✅ **Doloženo dvakrát, oběma primárními zdroji.**

SNA2008 §1.77:

> „An increase in consumption of food by someone living in extreme
> poverty is likely to lead to a greater increase in welfare than
> a similar increase in consumption by someone already well-fed. The SNA
> however, cannot distinguish this…"

KUZ1934, str. 6:

> „**Economic welfare cannot be adequately measured unless the personal
> distribution of income is known.**"

## S44–S50 — tok versus zásoba

✅ **Doloženo doslova.** SNA2008 §3.2:

> „**Stocks measure economic value at a point in time. Flows measure
> changes in economic value over a period of time.**"

A §2.122: *„The balancing item of a balance sheet is **net worth**, the
difference between assets and liabilities."* — tedy bohatství je stav
v rozvaze, HDP je tok v účtu výroby. *„GDP is not a country's bank
account"* ✅ jako metafora sedí přesně.

## S52–S58 — večeře doma versus v restauraci

Jádro je ✅ **doloženo doslova**, ale dvě formulace jsou zjednodušení.

Vaření doma je na seznamu vyňatých služeb — SNA2008 §6.28:

> „…listing those services for which no entries are recorded in the
> accounts when they are produced by household members and consumed
> within the same household: … **c. The preparation and serving of
> meals**…"

Restaurace naopak spadá pod §6.27(a), *„production of all goods or
services that are supplied to units other than their producers"* ✅.

⚠️ **S54 — OPRAVENO ve 0.4.**

| | |
|---|---|
| bylo | *„But as far as GDP is concerned... **nothing happened**."* |
| teď | *„But as far as GDP is concerned... **that hour didn't happen**."* |

Důvod: přesně vzato se **suroviny do HDP započítaly** (nákup potravin je
výdaj na konečnou spotřebu domácností). Nezapočítala se ta **hodina
práce**, o které mluví S52. Rozdíl mezi domácí a restaurační variantou
tedy není celá večeře, nýbrž **služba** (a marže) — a *„nothing
happened"* to popíralo.

Nová formulace je i dramaturgicky lepší, protože pointa není „domácí
večeře je neviditelná", nýbrž „neplacená práce se nezachytí jako tržní
produkce" — a tím přirozeně naváže Kuznets v S62–S65.

⚠️ **S58 — *„The economic activity simply became easier for the
statistical system to measure."*** Měřitelnost je **jeden ze tří**
uváděných důvodů, ne jediný. SNA2008 §6.30 shrnuje:

> „…a combination of factors, namely the **relative isolation and
> independence of these activities from markets**, the **extreme
> difficulty of making economically meaningful estimates of their
> values**, and the **adverse effects it would have on the usefulness of
> the accounts for policy purposes**…"

Prostřední z těch tří je přesně to, co scéna říká (§6.29(b): *„there are
typically no suitable market prices that can be used to value such
services"*). **Ponecháno** — je to legitimní zkratka a vybraný důvod je
ten, který divákovi dává smysl. Zapsáno, aby se vědělo, že to není celý
obrázek.

## S59–S61 — neplacená práce: čtyři položky, čtyři shody

✅ **Nejsilnější doklad celého videa.** Výčet v S60 je položku po položce
na seznamu vyňatých služeb v SNA2008 §6.28:

| scénář | SNA2008 §6.28 |
|---|---|
| *Childcare.* | d. *The care, training and instruction of children* |
| *Cleaning.* | a. *The cleaning, decoration and maintenance of the dwelling* |
| *Cooking.* | c. *The preparation and serving of meals* |
| *Taking care of relatives.* | e. *The care of sick, infirm or old people* |

A S61 (*„These things can be extremely valuable"*) má oporu v §6.29:

> „In most countries a considerable amount of labour is devoted to the
> production of these services, and **their consumption makes an
> important contribution to economic welfare**."

## S62–S65 — Kuznets

✅ **Doloženo primárně, všechna čtyři tvrzení.**

| co scéna říká | doklad v KUZ1934 |
|---|---|
| *a nineteen thirty-four report to the US Senate* | titulní list: *„LETTER FROM THE ACTING SECRETARY OF COMMERCE TRANSMITTING **IN RESPONSE TO SENATE RESOLUTION NO. 220** (72D CONG.) A REPORT ON NATIONAL INCOME, 1929–32"*, **JANUARY 4, 1934**, Senate Document No. 124 |
| *one of the people who developed national income accounting* | ACKNOWLEDGMENT: *„Dr. Simon Kuznets, was retained by the Bureau of Foreign and Domestic Commerce to plan and supervise this study. **Dr. Kuznets, who was in full charge of the work, was responsible for the preparation of the final estimates, as well as the organization and the text of the report.**"* Zpráva zároveň přiznává předchozí práci NBER, takže *„one of the people"* je přesně správná míra, ne podcenění ani nadsazení |
| *he explicitly noted that the welfare of a nation could not simply be inferred from a measure of national income* | str. 7, kapitola nazvaná **„Uses and Abuses of National Income Measurements"**: *„**The welfare of a nation can, therefore, scarcely be inferred from a measurement of national income as defined above.**"* |
| *unpaid household work was among the things left outside the measurement* | str. 5, bod *(b) Services of housewives and other members of the family*: *„The volume of services rendered by housewives and other members of the household toward the satisfaction of wants must be imposing indeed … and the item is thus **large enough to affect materially any estimate of national income**."* — a přesto se vynechává |
| *almost a century ago* | 1934 → 2026 je **92 let** ✅ |

> **Bonus, který ve scénáři není, ale hodí se do odpovědí v komentářích:**
> Kuznets si na téže straně všiml i toho, co video ukazuje na restauraci —
> že se ten efekt obrací, když se trh smrští a lidé začnou dělat víc doma:
> *„this omission, unavoidable though it is, lowers the value of national
> income measurements as indexes of the nation's productivity in
> conditions of recent years when the contraction of the market economy
> was accompanied by an **expansion of activity within the family**."*

> **Sloveso „explicitly noted" je oprávněné**, protože podle
> ACKNOWLEDGMENT psal text zprávy sám. Kdyby tam stálo „Kuznets
> invented GDP", bylo by to špatně — HDP v dnešní podobě je pozdější
> a zpráva mluví o *national income*. Scénář to má správně: *„national
> income accounting"*, ne „GDP".

## S66–S70 — HDP není štěstí, zdraví, bezpečí ani volný čas

✅ **Doloženo skoro doslova.** SNA2008 §1.83:

> „An individual's state of well-being, or welfare, is not determined by
> economic factors alone. **Personal and family circumstances, quality of
> health, the satisfaction or lack of it derived from employment** are
> just some other factors that affect welfare."

Životní prostředí zvlášť, §1.81–1.82: *„Some production activities cause
a loss in welfare that is not captured in the SNA. A factory, for
example, may generate noise and emit pollutants…"*

S70 (*„GDP simply wasn't designed to answer those questions"*) má oporu
v §1.84:

> „Yet other aspects are likely to remain forever outside the reach of
> **a system not designed with the measurement of welfare as a prime
> consideration**."

S69 (*„Two countries can have very similar GDP per capita… and radically
different quality of life"*) je obecné tvrzení bez čísla a jako takové
platí; §1.84 ho podpírá v principu. ✅

## S72 — válka: zbraně se počítají, bohatství se ničí

✅ **Obě půlky doloženy.**

**Zbraně jsou v HDP.** SNA2008 uvádí mezi změnami proti SNA 1993:
*„Extension of the assets boundary and government gross capital
formation to include **expenditure on weapons systems**"*, a zbraňové
systémy má v klasifikaci aktiv. Před rokem 2008 se počítaly jako vládní
spotřeba — **v obou případech uvnitř HDP**, liší se jen položka.

**Zničení bohatství je mimo HDP.** SNA2008 §12.46:

> „The volume changes recorded as catastrophic losses in the other
> changes in the volume of assets account are the result of large scale,
> discrete and recognizable events that may destroy a significantly large
> number of assets… They include major earthquakes, volcanic eruptions,
> tidal waves, **exceptionally severe hurricanes**, drought and other
> natural disasters; **acts of war**, riots and other political
> events…"

Standard tedy v jediném odstavci jmenuje **obě** situace videa — hurikán
i válku.

## S73 — OPRAVENO ve 0.4

| | |
|---|---|
| bylo | *„All of the production **counts**. None of the destruction **does**."* |
| teď | *„All of the production **is counted**. None of the destruction **is subtracted**."* |

**Co bylo doložené a pravdivé i v původní verzi:** zničení existujícího
aktiva **není zápornou položkou HDP**. Zapisuje se do jiného účtu —
*other changes in the volume of assets* — a promítne se do rozvahy
a čistého jmění, ne do produkce. SNA2008 §3.7: *„Other flows are changes
in the value of assets and liabilities that do not result from
transactions. **Examples are losses due to natural disasters**…"* BEA55:
*„Neither GDP nor the associated income measures are **adjusted** to take
account of damage to, or destruction of, assets."*

**Proč se to přesto muselo změnit:** *„None of the destruction
**counts**"* se četlo jako absolutní tvrzení, že válečné ničení se do
HDP nepromítne **nijak**. To neplatí — zničená továrna v dalších
obdobích nevyrábí, takže ničení **snižuje budoucí HDP**, a ve válce
navíc obvykle klesá civilní výroba. Ta úvaha je moje, ne citace:
**klauzuli o „production capacity" se mi nepodařilo v BEA doložit**
(viz varování nahoře), takže se o ni tenhle závěr neopírá — stačí, že
běžný divák si „nepočítá se" přeloží jako „nemá vliv".

Tři důvody pro zvolenou formulaci:

1. **Je to účetní tvrzení, a tím se stalo jednoznačným.** „Odečítá se"
   nelze číst jako „má vliv".
2. **Kopíruje sloveso primárního zdroje.** BEA mluví o tom, že HDP
   *„is not **adjusted** to take account of"* zničení.
3. **Rýmuje se to se S77**, kde scénář říká *„it doesn't **subtract**
   points for doing bad things"* — callback přes čtyři scény zadarmo.

> **Vedlejší přínos, který se ukázal až po změně:** `lib.sentences()`
> teď scénu dělí na **dvě věty** místo jedné dvojice bez hranice, takže
> punchline dostane `sentence_pause`. Ověřeno.

## S74 — „There's a whole video about that one."

✅ Video **025 — *How Does a War Economy Work?*** je zveřejněné:
`https://www.youtube.com/watch?v=pKPpZWPuOQI`, 8:45, kapitola *„The
strange case of GDP"* ve 03:49. Není to slib, je to odkaz. ✅

## S75 — znečištění, kriminalita, nehody, nemoci

✅ **Doloženo, a jedna položka dokonce týmž příkladem.**

Znečištění: SNA2008 §1.81 — továrna emituje, což *„goes unmeasured"*,
a když pak na snížení emisí vynaloží prostředky, *„costs will rise"*,
tedy vzroste měřená produkce.

Nemoc: SNA2008 §1.79 používá **přesně stejný příklad jako scénář**:

> „Consider the effects of an exceptionally severe winter combined with
> **an influenza epidemic**… the production and consumption of fuels,
> clothing and **medical services will tend to increase**… **Total
> welfare could fall even though GDP could increase in volume terms.**"

Kriminalita (bezpečnostní služby) a nehody (opravy, zdravotní péče) jsou
tržní služby dodávané jiným jednotkám, tedy v HDP podle §6.27(a). ✅

## S76–S77 — HDP není morální skóre

✅ SNA2008 §1.75 (viz S26–S28). Standard sám říká, že si nárok na měření
blahobytu neklade.

## S79–S81 — HDP je užitečné

✅ SNA2008 §19.12 (viz S05). Recese, oživení a růst se sledují právě
objemovým HDP.

## S83 — teploměr

✅ Metafora, ne tvrzení. Není co ověřovat.

## S85, S99 — otázky, na které HDP nebylo stavěné

✅ **Doloženo, a scénář trefil i slovo.** SNA2008 §1.84:

> „It would be foolish to deny this just as it is unrealistic to expect
> a system of economic accounts to **necessarily and automatically**
> yield a wholly satisfactory measure of welfare."

Scénář v S99 říká *„economic growth is not **automatically** the same
thing as human progress"* — táž míra jistoty jako ve standardu. ✅

## S93–S96 — „GDP increased by three percent" ≠ „People are three percent better off"

✅ SNA2008 §1.76:

> „However, **changes in the volume of consumption, for example, are not
> the same as changes in welfare**. … The increase in welfare may not,
> however, be proportionate to the increase in expenditure."

Tři procenta jsou v obou scénách **hypotetické** (*„say, three
percent"* v S37 to zavádí), takže se neověřují jako údaj. ✅

---

## Co ověřitelný údaj neobsahuje — vypsáno, ne jen tvrzeno

Aby bylo pokrytí doložitelné a ne jen slíbené: výše je rozebráno
**81 scén ze 101**. Zbylých dvacet **neobsahuje ověřitelný údaj** a tady
jsou všechny, ať se to dá zkontrolovat strojově:

| druh | scény |
|---|---|
| řečnická otázka | S04, S14, S78 |
| přechod mezi sekcemi | S29, S51, S71 |
| jednoslovná / hodnotící vsuvka | S06, S82, S84 |
| metafora teploměru a její rozvedení | S86, S87, S88, S89, S90, S100, S101 |
| shrnující formulace bez nového tvrzení | S91, S92, S97, S98 |

Tvrzení, které nesou S91–S92 (*„It tells us something important about
the economy. Just not everything that's important about a society."*),
je totéž jako S85 a S99 a je doložené výš (SNA2008 §1.84).

Zbytek scénáře jsou metafory (teploměr, bankovní účet, tok a zásoba)
a hypotetické příklady s vymyšlenými čísly (*ten percent*, *three
percent*, *fifty dollars*). **Jediný skutečný letopočet v celém videu je
*nineteen thirty-four*** a je doložený primárně.

## Rozhodnuto

**S73 i S54 opravené** (uživatel 2026-09-09, `zpetna vazba
factcheck.txt`). Scénář je `script 0.4.md`, **101 scén, 9:10** —
oprava nezměnila počet scén ani řádků a žádný řádek nepřesáhl 42 znaků.
Fonemizace obou nových vět ověřena: `hour` → `aʊə`, `counted` →
`kaʊntɪd`, `subtracted` → `sʌbtɹaktɪd`, `pronounce` zůstává prázdné.

**S08, S18 a S58 zůstávají** jako vědomá zjednodušení — jsou zapsaná
výš i s tím, co přesně se v nich zamlčuje, takže je z čeho odpovídat
v komentářích.

**Scénář je zamčený. Fact check je hotový.** Další krok je
`storyboard.json`.
