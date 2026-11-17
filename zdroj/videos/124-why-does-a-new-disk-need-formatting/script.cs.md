<!-- S01 -->
Koupíš si úplně nový disk.
Jeden terabajt, úplně prázdný.
Než na něj uložíš jediný soubor,
musí se nejdřív naformátovat.

<!-- S02 -->
Tak ho naformátuješ na ext4,
standardní souborový systém
mnoha linuxových počítačů.
S výchozím nastavením,
ještě než vůbec něco uložíš,
zmizí zhruba sedmnáct gigabajtů.

<!-- S03 -->
Ještě tam nic není.
Žádné fotky, žádné dokumenty.
Tak co zabírá všechno to místo?

<!-- S04 -->
A proč vlastně disk potřebuje
nějaké formátování?
Data přece ukládat umí.
Umí číst a zapisovat biliony bitů.

<!-- S05 -->
Proč počítač prostě nezačne zapisovat
tam, kde je zrovna místo?

<!-- S06 -->
Protože data uložit
a pak je znovu najít
jsou dva úplně jiné problémy.

<!-- S07 -->
Představ si úřad, který místo formulářů
rozdává prázdné papíry.
Všechno je někde zapsané...
a nikdo nic nenajde.

<!-- S08 -->
Disk bez souborového systému
je ta hromada papíru.
Lepší přirovnání
je ale sešit.

<!-- S09 -->
Představ si sešit
s tisíci stranami
a s několika pravidly, jak ho používat.

<!-- S10 -->
Zaprvé: každá strana má číslo.
Takže každé místo v sešitu
má adresu.
Strana čtyři sta dvanáct
znamená právě jedno místo.

<!-- S11 -->
Zadruhé: na prvních pár stranách
je obsah sešitu.
Každá položka má název
a stranu, na které je.
Palačinky: strana dvanáct.

<!-- S12 -->
Zatřetí: úplně vzadu
je seznam stran,
které jsou ještě prázdné.

<!-- S13 -->
Teď přidej recept.
Vzadu najdeš prázdnou stranu.
Napíšeš na ni recept.
Přidáš řádek do obsahu.
A tu stranu škrtneš
v seznamu prázdných.

<!-- S14 -->
Jeden recept, tři místa.
A všechna tři se musí shodovat.

<!-- S15 -->
Pak se recept na palačinky rozroste.
Strana dvanáct je plná
a třináctka už je obsazená.
Pokračuje tedy na straně osmdesát sedm
a obsah to musí uvádět.

<!-- S16 -->
A teď ten háček.
Když chceš v obsahu místo
pro tisíc položek,
musíš si ty strany vyhradit
dřív, než napíšeš jediný recept.

<!-- S17 -->
Tolik přirovnání.
A teď, co je doopravdy na disku.

<!-- S18 -->
Disk neví nic o souborech,
složkách ani názvech.
Nabízí jen dlouhou řadu
očíslovaných políček, takzvaných sektorů.

<!-- S19 -->
Na pevném disku
leží data na rotujících plotnách.
SSD je drží ve flash paměti.
Počítač si ale v obou případech říká
jen o sektor podle jeho čísla
a disk sám zjistí, kde ten sektor je.

<!-- S20 -->
Sektor je malý.
Obvykle 512 bajtů,
nebo 4 096
u novějších disků.

<!-- S21 -->
Souborové systémy obvykle pracují
s většími kusy, takzvanými bloky.
U ext4 má blok čtyři kilobajty,
tedy velikost osmi sektorů starého typu.

<!-- S22 -->
Tyhle očíslované bloky
jsou strany sešitu.
Souborovému systému ještě chybí
zbylé dvě části:
obsah
a seznam toho, co je volné.

<!-- S23 -->
Právě ty formátování vytváří.
A právě tam
zmizelo těch sedmnáct gigabajtů.

<!-- S24 -->
Ext4 vyhradí záznam
pro každý soubor a složku,
které na disku budou moct být najednou.
Každý záznam má
256 bajtů.
Říká se mu inode.

<!-- S25 -->
Jednou bude každý inode říkat,
jak velký je soubor,
kdy se změnil,
kdo ho smí otevřít
a ve kterých blocích je jeho obsah.

<!-- S26 -->
Na terabajtovém disku
jich ext4 připraví zhruba
jednašedesát milionů.
Všechny prázdné, všechny čekají.
To je skoro šestnáct gigabajtů
prázdných záznamů.

<!-- S27 -->
Proč zrovna jednašedesát milionů?
Ext4 jednoduše odhadne:
jeden inode na každých šestnáct kilobajtů
místa na disku.
Na běžném počítači
většina těch záznamů
nikdy použita nebude.

<!-- S28 -->
Zhruba další gigabajt
připadne na žurnál,
ke kterému se ještě vrátíme.
Zbytek je další evidence,
včetně mapy s jedním bitem na blok,
který říká, jestli je obsazený, nebo volný.

<!-- S29 -->
A ten počet je navíc pevný.
Spotřebuj všechny záznamy
miliony drobných souborů
a disk ti oznámí, že je plný...
i když na něm zbývají gigabajty místa.

<!-- S30 -->
Tak se podívejme, jak to funguje.
Vytvoříme soubor hello.txt.
Uvnitř je jediné slovo: hello.
Pět písmen. Pět bajtů.

<!-- S31 -->
Souborový systém vybere prázdný inode.
Třeba číslo třináct.
Pak v mapě najde volný blok
a označí ho jako obsazený.

<!-- S32 -->
Do toho bloku zapíše těch pět bajtů.
Pak vyplní inode:
délka pět bajtů, vytvořen právě teď,
uložen v tom jednom bloku.

<!-- S33 -->
A nakonec do složky
přidá jeden řádek:
název hello.txt
a číslo třináct.

<!-- S34 -->
Všimni si, kde skončil název.
Ne v souboru.
Ne v inodu.
Název je uložený ve složce,
která je vlastně jen
seznamem názvů a čísel.

<!-- S35 -->
A složka je jen další soubor.
Jejím obsahem
je prostě ten seznam.

<!-- S36 -->
Proto je taky přesun souboru
do jiné složky na stejném souborovém systému
okamžitý, ať je soubor jakkoli velký.
Jedné složce řádek ubude,
druhé přibude
a samotný obsah
se obvykle vůbec nepohne.

<!-- S37 -->
Pět bajtů textu...
a na disku zabírá
4 096.
Blok je nejmenší kus,
který souborový systém přidělí,
takže i drobný soubor stojí celý blok.

<!-- S38 -->
Když soubor svůj blok přeroste,
souborový systém najde další volný.
Možná hned vedle.
Možná úplně jinde.
A inode si zapíše oba.

<!-- S39 -->
Velký soubor může časem skončit
rozházený po celém disku.
Pevný disk mezi kusy musí přeskakovat.
SSD si s tím poradí mnohem líp.

<!-- S40 -->
Program, který soubor uložil,
o ničem z toho neví.
Řekl „ulož hello.txt“
a všechno ostatní proběhlo na pozadí.

<!-- S41 -->
Teď ho smaž.
Název zmizí ze složky.
Inode se označí jako volný.
Blok se vrátí mezi volné.

<!-- S42 -->
Na klasickém pevném disku
zůstane samotných pět bajtů na místě.
Nikdo na ně nesáhl.
Zůstanou tam, dokud přes ně
někdo nezapíše něco nového.

<!-- S43 -->
Proto jde smazaný soubor
někdy obnovit.
Smazání obvykle neodstraní
samotný obsah.
Jen označí místo jako volné.

<!-- S44 -->
U SSD je to méně jisté.
Souborový systém může disku oznámit,
že ty bloky už nepotřebuje,
a disk pak jejich obsah může zahodit.
Pak už je šance
na obnovení souboru mnohem menší.

<!-- S45 -->
Souborový systém je vlastně takový účetní.
Vytvoření jednoho souboru
znamenalo upravit tři věci:
složku, inode
a mapu volných bloků.

<!-- S46 -->
Teď vypni proud
uprostřed ukládání souboru.

<!-- S47 -->
Možná už byl blok označený jako obsazený,
ale ještě na něj neukazuje žádný inode.
To místo je prostě ztracené.
Otravné, ale neškodné.

<!-- S48 -->
Nebo inode ukazuje na blok,
který mapa pořád vede jako volný.
Další soubor se pak může zapsat
přímo přes něj.
A ten první je potichu zničený.

<!-- S49 -->
Proto si ext4 vede žurnál.
Než změní svou evidenci,
zapíše si, co se chystá udělat.
Po pádu zopakuje jen ty změny,
které stihl celé zapsat
a označit jako dokončené.
Nedokončené ignoruje.

<!-- S50 -->
A pak je tu tišší problém.
Disk občas změní bit
a nikomu to neřekne.

<!-- S51 -->
Ext4 chrání své vlastní záznamy
kontrolními součty,
takže u nich poškození pozná.
Ale obsah tvých souborů?
Tomu prostě věří.

<!-- S52 -->
Některé souborové systémy kontrolují obojí.
A některé si drží druhou kopii,
takže když se jedna kopie poškodí,
opraví ji z té druhé.
Problém odhalit a problém opravit
není totéž.

<!-- S53 -->
Každý souborový systém tedy dělá totéž:
očíslované bloky, seznam názvů
a mapa toho, co je volné.

<!-- S54 -->
Liší se ale v tom, jak to dělá.
Ext4 připraví jednašedesát milionů záznamů
dřív, než cokoli uložíš.
NTFS ve Windows drží své záznamy
v jedné velké tabulce, která průběžně roste.

<!-- S55 -->
A Btrfs nepřipravuje
pevnou tabulku inodů předem.
Vytváří je, jak přibývají soubory.
A běžně nepřepisuje
data na místě.
Zapíše novou kopii
a teprve pak pustí tu starou.

<!-- S56 -->
Ve výchozím nastavení počítá kontrolní součty
i tvých souborů, takže pozná jejich poškození.

<!-- S57 -->
A protože se stará kopie
nepřepíše,
může ji zachovat snapshot.
To mění odpověď
skoro na každou otázku z tohohle videa:
co udělá pád,
co znamená smazání
a dokonce i co je kopie.

<!-- S58 -->
Tím začne další video.

<!-- S59 -->
Tak mám pro tebe otázku.
Má souborový systém soubory jen ukládat,
nebo je má i chránit?
Napiš mi to do komentářů.
