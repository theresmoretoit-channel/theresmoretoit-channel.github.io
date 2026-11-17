<!-- S01 -->
Devět set devadesát devět liber
a devadesát devět pencí.
Přičti jednu penci.

<!-- S02 -->
Výsledek je nula.

<!-- S03 -->
Žádné chybové hlášení. Žádný pád.
Jen nula, potichu zapsaná na účet.

<!-- S04 -->
Když je v COBOLu pole pro výsledek
příliš malé, aby se do něj vešel,
přebývající číslice může prostě zmizet.
Pokud si program nevyžádá varování,
výpočet běží dál.

<!-- S05 -->
A ani nezaokrouhluje.
Dvě libry a třicet čtyři a půl pence,
uložené s přesností na penci,
se změní na dvě třicet čtyři.

<!-- S06 -->
Připiš jedno slovo navíc, ROUNDED,
a vyjde dvě třicet pět.

<!-- S07 -->
Ani jedno z toho není chyba.
Jsou to pravidla.
A spousta bank na světě
na takových pravidlech pořád jede.

<!-- S08 -->
COBOL je programovací jazyk
z roku 1959.
Ne každý program v něm napsaný je tak starý.
Ale jazyk ano,
a jeho zvyky taky.

<!-- S09 -->
Proč ho tedy banky nenahradily?
Peníze mají.
Inženýry taky.

<!-- S10 -->
Podíváme se proto na tři skutečné případy.
Na banku, která se pokusila opustit starý systém,
na banku, které se to povedlo,
a na krizi, za kterou všichni vinili COBOL.

<!-- S11 -->
Ale nejdřív k té chybějící půl penci.

<!-- S12 -->
Řekněme, že ten bankovní program přepíšeš
do moderního jazyka.
Ta pravidla bys nejspíš opravil.
Přetečení se stane chybou.
Půl pence se zaokrouhlí nahoru.

<!-- S13 -->
Čistší. Bezpečnější.
A všude, kde se objeví půl pence,
se teď tvůj program se starým neshodne.

<!-- S14 -->
Moderní jazyky umí počítat přesně v desítkové soustavě.
Java má na to vlastní typ.
Ale i tam
je zaokrouhlovací pravidlo věcí volby.

<!-- S15 -->
Jedno běžné nastavení zaokrouhlí polovinu nahoru:
dvě třicet pět.
Jiné zaokrouhlí k nejbližší sudé číslici:
dvě třicet čtyři.
Obojí je správně. Shodne se jen jedno.

<!-- S16 -->
A s obyčejnou plovoucí čárkou,
kterou většina kódu používá ve výchozím stavu,
je to ještě podivnější.
Nula celá jedna plus nula celá dva
není nula celá tři.

<!-- S17 -->
Nahradit COBOL tedy není překlad.
Znamená to najít každé takové pravidlo
v milionech řádků
a každé zachovat přesně tak, jak bylo.

<!-- S18 -->
Jak se tam vůbec dostal?

<!-- S19 -->
V květnu 1959
svolalo ministerstvo obrany USA
schůzku do Pentagonu.
Přišli výrobci počítačů, úřady
a velké firmy,
a všichni měli stejný problém.

<!-- S20 -->
Každý počítač měl svůj vlastní jazyk.
Mzdový program napsaný pro jeden stroj
byl na jiném k ničemu.

<!-- S21 -->
Komise navrhla společný jazyk
pro firmy.
Nejvíc ho ovlivnil FLOW-MATIC
z týmu Grace Hopperové ve firmě Remington Rand.

<!-- S22 -->
A v prosinci 1960
běžel v podstatě tentýž program v COBOLu
na dvou počítačích
od konkurenčních výrobců.
O to přesně šlo.

<!-- S23 -->
Byl navržený tak, aby se v něm lidé vyznali.
ADD PAYMENT TO ACCOUNT-BALANCE.
Co to dělá, nejspíš uhodneš.

<!-- S24 -->
A peníze ukládal tak, jak je píšou lidé:
jako desítkové číslice.
Desetinnou čárku
dokonce není třeba ukládat.
Kam patří, říká popis pole:
poslední dvě číslice jsou pence.

<!-- S25 -->
V roce 1964 uvedla IBM System/360.
Jeho návrh obsahoval instrukce
pro desítkovou aritmetiku.

<!-- S26 -->
A IBM od té doby navrhuje své sálové počítače
tak, aby zůstaly kompatibilní.
Spousta starších programů pořád běží
i na dnešních strojích,
aniž by se musely přepsat.

<!-- S27 -->
Takže málokdy nastala chvíle,
která by někoho donutila přejít.
Každý rok kód dál fungoval
a každý rok nasbíral další pravidla.
Nové produkty, nové daně, nové předpisy,
nové výjimky.

<!-- S28 -->
Kolik COBOLu ve světě pořád běží,
nikdo nespočítal.
IBM ale tvrdí, že čtyřicet pět
z padesáti největších bank světa
pořád používá její sálové počítače.

<!-- S29 -->
A někteří majitelé to spočítali.
V roce 2017 uvedla americká
Správa sociálního zabezpečení, že její systémy obsahují
přes šedesát milionů řádků COBOLu.

<!-- S30 -->
V roce 2025 sepsali auditoři americké vlády
jedenáct federálních systémů,
které nejvíc potřebují nahradit.

<!-- S31 -->
Byly staré dvacet tři
až šedesát let
a jejich provoz stál zhruba sedm set padesát
milionů dolarů ročně.

<!-- S32 -->
Kód je tedy starý, je všude
a je plný pravidel, která nikdo nesepsal.
Nebezpečné je přece si ho nechat.

<!-- S33 -->
Podívejme se, co se stane,
když banka odejde.

<!-- S34 -->
V roce 2018 měla britská banka TSB
zhruba pět milionů zákazníků
a problém.

<!-- S35 -->
Své systémy si pronajímala
od Lloyds Banking Group,
konkurenta,
a poplatky měly prudce stoupnout.

<!-- S36 -->
TSB se proto rozhodla převést všechno
na novou platformu,
kterou postavil její nový majitel,
španělská banka Sabadell.

<!-- S37 -->
Jeden víkend v dubnu.
V neděli večer
se nový systém zapnul.

<!-- S38 -->
V pondělí bylo zhruba
devět set tisíc pokusů o přihlášení.
Do internetového bankovnictví
prošlo jen zhruba jedno přihlášení z deseti.

<!-- S39 -->
Platby selhávaly.
Někteří zákazníci se přihlásili
a viděli cizí účty.

<!-- S40 -->
Nejhorší stav trval asi týden.
K běžnému provozu se TSB vrátila
až v prosinci.

<!-- S41 -->
Následky stály kolem
tří set třiceti milionů liber
jen v roce 2018.
Regulátoři později přidali
pokuty za skoro čtyřicet devět milionů.

<!-- S42 -->
A teď to zvláštní.
Data zákazníků dorazila neporušená.
Shodují se na tom obě oficiální zprávy.

<!-- S43 -->
Selhala nová platforma kolem nich.
Dvě datová centra, každé nastavené jinak.
Výkon otestovaný jen na jednom z nich,
a cíle snížené,
když testy neprošly.

<!-- S44 -->
A cesta zpátky nebyla.
Jakmile se data přesunula,
byl návrat ke starému systému
slovy regulátora
„v podstatě nemožný“.

<!-- S45 -->
TSB neutíkala z rozbitého systému.
Opouštěla systém, který fungoval,
kvůli tomu, komu patřil
a kolik stál.
Nebezpečný byl právě ten odchod.

<!-- S46 -->
Je tedy odchod vždycky katastrofa?

<!-- S47 -->
V roce 2008 se australská Commonwealth Bank
rozhodla nahradit základní systémy,
které jí sloužily
přes čtyřicet pět let.

<!-- S48 -->
Plán: zhruba pět set osmdesát
milionů australských dolarů
a čtyři roky.

<!-- S49 -->
Trvalo to pět.
Podle pozdějších zpráv tisku vyšel celek
zhruba na miliardu sto milionů,
jak se projekt rozrůstal.

<!-- S50 -->
Nepřesunula ale všechno
za jeden víkend.
Nejdřív v roce 2010 vkladové účty.
Firemní účty následovaly v roce 2011
a úvěry v roce 2012.

<!-- S51 -->
Každý krok byl něco, co banka
mohla sledovat, ověřit a poučit se z něj,
než přešla na další.

<!-- S52 -->
Nakonec se podle svých slov
stala první velkou australskou bankou
s bankovnictvím v reálném čase,
nepřetržitě.

<!-- S53 -->
Takže to jde.
Ale podívej se, co to stálo.
Pět let, mnohem vyšší účet
a trpělivost.

<!-- S54 -->
Modernizace není nákup.
Je to projekt
s vlastními riziky.

<!-- S55 -->
A teď krize,
za kterou všichni vinili COBOL.

<!-- S56 -->
Březen 2020.
Když pandemie zavřela New Jersey,
vyskočil počet nových žádostí o podporu v nezaměstnanosti
z necelých deseti tisíc za týden
na přes sto padesát pět tisíc.

<!-- S57 -->
Šestnáctkrát víc,
za sedm dní.
Úřad práce to nestíhal.

<!-- S58 -->
Začátkem dubna guvernér
požádal o dobrovolníky.
Nejen o zdravotníky,
ale i o lidi, kteří umějí COBOL.
Systémy státu jsou podle jeho slov
přes čtyřicet let staré.

<!-- S59 -->
Příběh se rychle rozšířil.
Prastarý kód se pod náporem pandemie
zhroutil.

<!-- S60 -->
Když to ale později
prověřil státní auditor,
nenašel žádný doklad,
že by zpoždění způsobily
počítačové systémy.

<!-- S61 -->
Novináři, kteří nezávisle na tom zkoumali
chybová hlášení, která lidé dostávali,
dohledali mnoho z nich až k webovému rozhraní,
napsanému v mnohem novějším jazyce, Javě.
Starý kód za ním běžel dál.

<!-- S62 -->
Proč tedy stát potřeboval programátory COBOLu?
Protože Kongres měnil pravidla.
Nové dávky, nové částky,
noví lidé, kteří na ně měli nárok,
a každá změna se musela dostat
do kódu, a rychle.

<!-- S63 -->
Problém nebyl v tom, že byl kód starý.
Byl v tom, že ho umělo měnit málo lidí,
a že telefonní linky i personál
byly taky přetížené.

<!-- S64 -->
Tři případy.
Banka, která opustila systém, jenž pořád fungoval,
a jejíž migrace selhala.
Banka, která odcházela opatrně
a uspěla.
A krize, ze které se vinil starý kód,
a nikdo nedoložil, že byl příčinou.

<!-- S65 -->
To neznamená, že staré systémy nikdy neselhávají.
Selhávají.
Prodražují se,
lidé, kteří jim rozumějí, odcházejí do důchodu,
a čekání má taky svou cenu.

<!-- S66 -->
Jenže stáří je vidět snadno
a skutečná rizika ne.
Pravidla, která nikdo nesepsal.
Znalosti v hlavách pár lidí.
A okamžik přepnutí.

<!-- S67 -->
Proto spousta bank nevyměňuje
staré jádro najednou.
Obalí ho.
Aplikace v tvém telefonu je nová,
ale možná mluví s něčím
mnohem starším.

<!-- S68 -->
A nahrazují ho kus po kusu.
V roce 2004 to Martin Fowler, autor knih o softwaru,
pojmenoval podle fíkusu škrtiče,
rostliny deštného pralesa, která obroste strom,
až nakonec obstojí sama.

<!-- S69 -->
Starý systém dál pracuje,
zatímco nový kolem něj roste,
jedna úloha po druhé,
dokud na starém nic nezávisí.

<!-- S70 -->
Tím se vracíme k té půl penci.
Někde ji program možná pořád zahazuje,
protože to tak někdo rozhodl
před desítkami let.
Nahradit ten program znamená vědět o tom,
a o všem podobném.

<!-- S71 -->
Starý systém nemusí být nutně
to, co selže.
Někdy je to to, co ho nahrazuje.

<!-- S72 -->
Protože nahradit technologii
neznamená odstranit riziko.
Někdy ho to jen přesune
do jediného dubnového víkendu.

<!-- S73 -->
Tak tady je otázka pro tebe.
Když systém funguje čtyřicet let,
kdy je ta správná chvíle ho nahradit?
A nahrazoval jsi někdy nějaký sám?
Napiš mi to do komentářů.
