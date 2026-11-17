<!-- S01 -->
19. července 2024
rozeslala bezpečnostní firma CrowdStrike
běžnou aktualizaci.

<!-- S02 -->
Žádný nový program.
Jen malý konfigurační soubor.

<!-- S03 -->
Během pár hodin se 8,5 milionu
počítačů s Windows zastavilo
na modré obrazovce.

<!-- S04 -->
Aerolinky zrušily lety.
Nemocnice rušily operace.
Jedna zpravodajská stanice přestala vysílat.

<!-- S05 -->
A chyba, která za tím stála,
byla úplně obyčejná.
Program čekal 20 údajů.
Aktualizace mu jich dala 21.

<!-- S06 -->
Tvoje hry a aplikace dělají
takové chyby pořád.
Když se to stane, hra se zavře
a ty ji pustíš znovu.

<!-- S07 -->
Stejný druh chyby.
Jedna zavře okno.
Druhá zastaví
8,5 milionu strojů.

<!-- S08 -->
Rozdíl není v chybě.
Je v tom, kde ten kód běžel.

<!-- S09 -->
Tak proč nemůže jeden program
ovládnout tvůj počítač...
a proč tenhle mohl?

<!-- S10 -->
Nebylo to tak vždycky.

<!-- S11 -->
Na PC s DOSem v 80. letech
programu v procesoru nic nebránilo.
Mohl zapisovat kamkoli do paměti
a mluvit přímo s hardwarem.

<!-- S12 -->
Stačilo, aby jeden program
zapsal někam, kam neměl,
a mohl přepsat operační systém.
Celý počítač zamrzl.

<!-- S13 -->
Řešením bylo přestat programům věřit
a nechat nedůvěru
na procesoru.

<!-- S14 -->
V roce 1982 přinesl procesor Intel 80286
chráněný režim
se čtyřmi úrovněmi oprávnění.

<!-- S15 -->
Obvykle se kreslí
jako čtyři prstence, jeden v druhém.

<!-- S16 -->
Ring 0 je uprostřed.
Ring 3 je venku.

<!-- S17 -->
A číslují se pozpátku.
Čím nižší číslo,
tím víc toho kód smí.

<!-- S18 -->
Ring 0 patří kernelu,
jádru operačního systému.
Rozděluje paměť,
rozhoduje, který program poběží dál,
a mluví s hardwarem.

<!-- S19 -->
V ringu 3 běží tvůj prohlížeč,
tvoje hry a textový editor.
Říká se tomu uživatelský režim.

<!-- S19b -->
Windows, macOS i Linux
si práci dělí stejně.
Kernel v ringu 0,
aplikace v ringu 3.

<!-- S19c -->
Telefony a novější Macy od Applu
používají místo toho čipy ARM.
Tam se těm úrovním říká exception levels.
Jiné jméno, stejné rozdělení:
jedna pro kernel, jedna pro aplikace.

<!-- S20 -->
Procesor vždycky ví,
ve kterém ringu právě běží.
A kontroluje to.

<!-- S21 -->
Některé instrukce fungují jen v ringu 0.
Třeba vypnutí přerušení
nebo změna mapování paměti.

<!-- S22 -->
Když to program v ringu 3 zkusí,
procesor odmítne.
Vyvolá výjimku
a předá řízení kernelu,
který program obvykle ukončí.

<!-- S23 -->
S pamětí je to stejné.
Každá stránka paměti je označená
buď jako user, nebo jako supervisor.

<!-- S24 -->
Program v ringu 3,
který sáhne na stránku supervisoru,
data nedostane.
Zastaví se.

<!-- S25 -->
Tvůj prohlížeč i tvoje hra
běží oba v ringu 3.
Od sebe je drží to,
že každý má vlastní mapu paměti.
Paměť toho druhého programu
na ní prostě není.

<!-- S26 -->
Takže když hra spadne,
škoda zůstane uvnitř hry.
Kernel po ní uklidí.
Všechno ostatní běží dál.

<!-- S27 -->
A teď znovu CrowdStrike.
Jeho ovladač běžel v ringu 0,
hned vedle kernelu.

<!-- S28 -->
Nic nad ringem 0
takovou chybu nezachytí.

<!-- S29 -->
Windows tedy udělal jedinou bezpečnou věc, co zbývala.
Zastavil celý počítač, a to schválně,
místo aby pokračoval s pamětí,
které už nemohl věřit.

<!-- S30 -->
Přesně tohle je ta modrá obrazovka.

<!-- S31 -->
A protože se ovladač spouštěl
pokaždé, když startoval Windows,
každý restart přinesl pád znovu.

<!-- S32 -->
Jenže tady vzniká otázka.
Když prohlížeč nesmí sahat na hardware,
jak vůbec uloží soubor
nebo něco pošle po síti?

<!-- S33 -->
Požádá.

<!-- S34 -->
Program vloží svůj požadavek
do registrů procesoru.
Který soubor. Kam mají data jít.
Kolik jich.

<!-- S35 -->
Pak spustí jednu speciální instrukci.
Na moderním PC se jmenuje SYSCALL.

<!-- S36 -->
V tu chvíli se procesor přepne
z ringu 3 do ringu 0...

<!-- S37 -->
ale neskočí tam,
kam chce program.
Skočí do jediného vstupního bodu,
který si kernel předem určil.

<!-- S38 -->
Kernel požadavek zkontroluje,
udělá práci
a vrátí se do ringu 3.
Program se disku sám nikdy nedotkl.

<!-- S39 -->
Tomu se říká systémové volání
a děje se pořád.

<!-- S40 -->
Spočítali jsme je na notebooku.
Program, který nedělá vůbec nic,
jich i tak udělá 30.

<!-- S41 -->
Firefox při startu
a načtení jedné stránky Wikipedie
jich udělal asi 670 000
za 20 sekund...
a to ho naše počítání ještě zpomalovalo.

<!-- S42 -->
Každé z nich
je cesta skrz zeď a zpátky.

<!-- S43 -->
A tady je něco zvláštního.
Čtyři ringy,
a potřebovali jsme jen dva.

<!-- S44 -->
Co se stalo s ringy 1 a 2?

<!-- S45 -->
Myšlenka ringů je starší než PC.
Multics, operační systém
z konce 60. let,
jich měl osm.

<!-- S46 -->
Šlo o vrstvy důvěry.
Jádro systému uprostřed,
méně důvěryhodné služby kolem něj
a programy venku.

<!-- S46b -->
Intel nakreslil stejný obrázek.
Ringy 1 a 2 byly určené
pro vrstvy mezi tím,
třeba ovladače a systémové služby.
Víc důvěry než tvoje aplikace,
míň než kernel.

<!-- S47 -->
V cestě stály dvě věci.

<!-- S48 -->
Zaprvé, systémy jako Unix a Windows NT
měly běžet
na mnoha druzích procesorů.

<!-- S49 -->
A jediné rozdělení,
které nabízel každý procesor,
byly dvě úrovně.
Jedna pro kernel,
jedna pro všechno ostatní.

<!-- S50 -->
Zadruhé, samotný procesor x86.
Když mapuje paměť,
zná každá stránka jen dva stavy.
User, nebo supervisor.

<!-- S51 -->
Ringy 1 a 2 se počítají jako supervisor.
Takže ovladač v ringu 1
by stejně mohl sahat do paměti kernelu.
Ring navíc by toho moc neochránil.

<!-- S51b -->
Pár systémů je přesto využilo.
OS/2 pouštěl některé programy do ringu 2,
jen aby mohly mluvit přímo s hardwarem.

<!-- S51c -->
A než procesory dostaly pomoc
pro běh virtuálních počítačů,
Xen a VirtualBox přesouvaly kernel virtuálního počítače
do ringu 1,
aby systém pod ním
měl ring 0 sám pro sebe.

<!-- S52 -->
V roce 2023 Intel navrhl
ringy 1 a 2 úplně zrušit.

<!-- S53 -->
V prosinci 2024 od plánu upustil.
V tvém procesoru pořád jsou.
Skoro nic je nepoužívá.

<!-- S54 -->
Zatím to zní jako dobrá zpráva.
Pravidla jsou v hardwaru
a hardware kontroluje každý přístup.

<!-- S55 -->
V roce 2017 našly tři týmy výzkumníků,
nezávisle na sobě,
cestu skrz tu zeď.

<!-- S56 -->
Pojmenovali ji Meltdown.
A abys ji pochopil,
potřebuješ znát jeden trik,
který dělají moderní procesory.

<!-- S57 -->
Procesor nečeká,
až jedna instrukce doběhne,
než začne další.
Běží napřed,
na instrukcích, které asi bude potřebovat.

<!-- S58 -->
Když se spletl,
výsledky zahodí,
jako by se nic nestalo.

<!-- S59 -->
A tady je ta chyba.
Na postižených čipech Intel
mohl program v ringu 3 požádat
o bajt z paměti kernelu...

<!-- S60 -->
a procesor ho načetl
a předal dalším instrukcím
dřív, než dokončil kontrolu,
jestli je to povolené.

<!-- S61 -->
Kontrola sice selhala.
Výsledek se zahodil.

<!-- S62 -->
Jenže ty další instrukce
už tajný bajt použily
a natáhly jeden kousek
vlastní paměti programu
do cache procesoru.

<!-- S63 -->
A cache nezapomene jen proto,
že se výsledek zrušil.

<!-- S64 -->
Program tedy měří,
jak rychle odpovídá každý kousek jeho paměti.
Ten, který odpoví rychle,
prozradí tajný bajt.

<!-- S65 -->
Bajt po bajtu
tak mohl obyčejný program číst
paměť kernelu
a jakákoli tajemství, která v ní byla.
Včetně hesel a šifrovacích klíčů.

<!-- S66 -->
Meltdown postihl procesory Intel
vyrobené už od roku 1995.

<!-- S67 -->
Zveřejněný byl
3. ledna 2018.

<!-- S68 -->
Oprava nemohla změnit křemík.
Operační systémy tedy změnily mapu.

<!-- S69 -->
Zatímco tvůj program běží,
je teď paměť kernelu z jeho mapy
skoro úplně odstraněná.
Není tam co načíst.

<!-- S70 -->
Ale vzpomeň si na systémová volání.
Každá cesta skrz zeď
teď musí vyměnit i mapu.

<!-- S71 -->
Red Hat změřil záplaty proti Meltdownu
a příbuzné chybě Spectre.
Pod 1 % u některé práce...
až 19 % u vytížených databází.

<!-- S72 -->
Pravidlo bylo celou dobu správné.
Procesor ho jen kontroloval pozdě.

<!-- S73 -->
A tím jsme zpátky u CrowdStriku
a u těžší otázky.

<!-- S74 -->
Proč byl bezpečnostní program
vůbec v ringu 0?

<!-- S75 -->
Protože odtamtud vidí všechno.
Startuje dřív než ostatní software.
A malware s právy administrátora
ho tam hůř vypne.

<!-- S76 -->
Výčet od samotného Microsoftu
končí varováním.
Ovladače v kernelu to dávají za cenu nižší odolnosti.

<!-- S77 -->
Po výpadku
začal Microsoft budovat způsob,
jak by antiviry mohly
běžet mimo kernel.

<!-- S78 -->
Na podzim 2026
je to pořád jen v testovacích verzích Windows.
A bezpečnostním firmám
kernel zavřený není.

<!-- S79 -->
Tvoje hry řeší stejné dilema.

<!-- S80 -->
Cheaty, které běží v kernelu,
jsou neviditelné pro anti-cheat,
který běží v ringu 3.

<!-- S81 -->
Tak se anti-cheat nastěhoval taky.
Vanguard od Riotu, který používá Valorant,
dává ovladač do ringu 0.
Na většině PC se načte už se startem Windows...
i když hru nikdy neotevřeš.

<!-- S82 -->
To z něj nedělá vadný program.
Ale sedí na stejném místě
jako ovladač CrowdStriku,
kde jedna chyba zastaví celý počítač.

<!-- S83 -->
Tak proč nemůže jeden program
ovládnout tvůj počítač?

<!-- S84 -->
Protože procesor drží
skoro všechny programy mimo střed
a kontroluje je pokaždé, když zaklepou.

<!-- S85 -->
Jenže procesor nemůže rozhodnout,
koho pustí dovnitř.
To rozhodují lidé...
pokaždé, když instalují ovladač.

<!-- S86 -->
Tak tady je otázka do komentářů.
Kdo by měl rozhodovat, které programy
se dostanou do ringu 0:
ty, Microsoft,
nebo firmy, které je vyrábějí?
