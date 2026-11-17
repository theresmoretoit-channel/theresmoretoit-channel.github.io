<!-- S01 -->
Otevřeš si terminál.
Někdo jde kolem.
Uvidí černou obrazovku
plnou záhadného textu.
A najednou...

<!-- S02 -->
„Ty jo! Ty hackuješ!"

<!-- S03 -->
No...
Možná.
Nebo možná jen zjišťuješ,
proč neběží server.

<!-- S04 -->
Dnes se podíváme, proč se z terminálu
a hackování stalo v populární kultuře
skoro totéž.
A hlavně...
jak hackování vypadá doopravdy.

<!-- S05 -->
Většina lidí má počítač s tlačítky.
Na něco klikneš.
Něco se stane.
A pak je tu terminál.
Žádná tlačítka.
Žádné vlídné hlášky.
Jenom tohle.
A to je děsivé.

<!-- S06 -->
Grafické rozhraní řekne:
smazat uživatele.
Terminál na to řekne tohle.

<!-- S07 -->
Pro zkušeného linuxáka
je to úplně běžná věc.
Pro všechny ostatní to vypadá,
že se chystáš odpálit raketu.

<!-- S08 -->
Ono to má svůj historický důvod,
proč to tak vypadá.
Rané počítače neměly grafické rozhraní.
Lidé s nimi mluvili přes textové terminály.

<!-- S09 -->
A ty terminály měly tmavé obrazovky
se zeleným nebo ambrovým fosforem.
Nebyl to pokus vypadat cool.
Prostě tak ta technika fungovala.

<!-- S10 -->
Jenže pak si film a televize
všimly něčeho užitečného.
Černá obrazovka plná rychle
běžícího textu vypadá technicky.
A hlavně...
vypadá složitě.

<!-- S11 -->
Nemusíš rozumět tomu,
co ty znaky znamenají.
Prostě to vidíš.
A mozek si řekne:
tenhle člověk dělá něco nelegálního.

<!-- S12 -->
Hollywood si vytvořil pozoruhodně
jednotný jazyk pro hackování.
Hacker sedí v tmavé místnosti.
Má šest monitorů.

<!-- S13 -->
Místnost svítí jen od těch monitorů.
Nikdo nerozsvítil.
Hacker začne psát rychlostí
zhruba devět set slov za minutu.

<!-- S14 -->
Po obrazovce lítá text.
Objeví se ukazatel průběhu.
Devadesát sedm procent.
Devadesát osm.
Devadesát devět.
A konečně sto.
Hacker se opře.
A řekne...

<!-- S15 -->
„Jsem uvnitř."

<!-- S16 -->
Takhle většina bezpečnostních
incidentů nevypadá.
Zkusme si ten skutečný rozhovor.
„Teď zahackuju tenhle server."
A server odpoví:
permission denied.

<!-- S17 -->
„Aha."
Zkusí to znovu.
Permission denied.
Zkontroluje heslo.

<!-- S18 -->
Přečte dokumentaci.
Vyhledá si chybovou hlášku.
Nakonec zjistí, že správce před půl rokem
vypnul přihlašování heslem.

<!-- S19 -->
„No jasně."

<!-- S20 -->
Počítače jsou pozoruhodně dobré v tom,
nechat tě dvacet minut hledat, že jsi
v konfiguráku zapomněl jediný znak.

<!-- S21 -->
Na jedné straně obrazovky:
správce systému.
Na druhé:
hacker.
Na obou se objeví tytéž nástroje.
Je to tím, že terminál
není nástroj na hackování.
Je to rozhraní.

<!-- S22 -->
Můžeš na něm provozovat server,
číst logy, kopírovat soubory, instalovat,
nebo ve tři ráno zjišťovat, co se rozbilo.

<!-- S23 -->
Nebo, podle toho, co zrovna děláš
a jestli k tomu máš oprávnění,
na něm můžeš testovat bezpečnost.
Nebo útočit.

<!-- S24 -->
Sám nástroj ti neřekne,
které z toho zrovna děláš.
Šroubovákem se dá počítač opravit.
Dá se jím taky zničit.
Šroubovák za to nemůže.

<!-- S25 -->
Tak co je vlastně hacker?
To slovo má mnohem starší historii
než dnešní kyberkriminalita.

<!-- S26 -->
Původně to byl někdo,
kdo rád zkoumal systémy
a uměl najít nečekaná řešení.

<!-- S27 -->
Časem se to slovo přilepilo
k počítačové bezpečnosti.
A dneska, když někdo řekne
„to je hacker", může myslet

<!-- S28 -->
bezpečnostního výzkumníka,
penetračního testera,
skutečného útočníka,
nebo prostě někoho, kdo ví
znepokojivě moc o Linuxu.
Většinou pomůže kontext.

<!-- S29 -->
Podívejme se znovu na náš obrázek.
Nápis říká:
tys to zahackovala.
A koukněte na ty monitory.

<!-- S29b -->
Na jednom je něco jako nmap.
Na druhém něco, co vypadá
ještě podezřeleji.
Lomítko etc lomítko passwd.

<!-- S30 -->
Pro někoho, kdo nezná Linux,
se zjevně nabourává do Pentagonu.
Pro správce systému kontroluje síť
a dívá se na seznam uživatelských účtů.

<!-- S31 -->
A přesně odtud pochází ten vtip.
Ta žena možná nehackuje vůbec nic.
Možná jen dělá svou práci.

<!-- S32 -->
Tak co ten nmap vlastně dělá?
Je to nástroj na mapování sítě
a bezpečnostní audit.

<!-- S33 -->
Hodně zjednodušeně:
namíříš ho na stroj a ptáš se,
co ten počítač
vystavuje do sítě.

<!-- S34 -->
Může ti říct, že některé porty jsou otevřené.
A porty odpovídají síťovým službám.
Není to automaticky útok.

<!-- S35 -->
Je to spíš jako dívat se na budovu
a ptát se, které dveře jsou otevřené.
Když je to tvoje budova,
je to běžná správa.

<!-- S36 -->
Když je cizí
a ty záměrně
hledáš, kudy dovnitř...

<!-- S37 -->
no, to už je jiná.

<!-- S38 -->
A co ta cesta k souboru?
Někdo si řekne:
čte soubor s hesly.
Jsou v něm informace o účtech.

<!-- S39 -->
Jenže na moderním Linuxu
jsou samotné otisky hesel uložené jinde.
Jsou v lomítko etc lomítko shadow,
který je mnohem přísněji chráněný.

<!-- S40 -->
Vidět ten soubor tedy není totéž
jako objevit hesla všech uživatelů.
Hollywood by z toho samozřejmě
udělal mnohem větší drama.

<!-- S41 -->
Správce Linuxu by řekl:
je to doslova seznam uživatelů.

<!-- S42 -->
Další klasická scéna prolomí heslo
zhruba za čtrnáct sekund.
Skutečné lámání je nudnější.
Máš otisk, máš slovník
a necháš počítač zkoušet kandidáty.

<!-- S43 -->
Možná ho najde za minutu.
Možná za týden.
Možná nikdy.
A zatímco počítač pracuje, útočník
u toho nesedí a nepíše.
Klidně si dává svačinu.

<!-- S44 -->
Čímž se dostávám ke své nejoblíbenější
hollywoodské tradici.
Počítače prý nepřijmou příkaz,
dokud ho nenapíšeš strašně rychle.

<!-- S45 -->
Skuteční programátoři a správci
nepíšou pořád.
Přemýšlejí.
Čtou.
Zírají na chybovou hlášku.

<!-- S46 -->
Pak zjistí, že to někdo
vyřešil před jedenácti lety.
A to řešení zkopírují.

<!-- S47 -->
To je informatika.

<!-- S48 -->
Někdy není to nejnebezpečnější,
co můžeš napsat,
žádný záhadný hackerský příkaz.
Je to něco naprosto legitimního.

<!-- S49 -->
Slavný příklad je tenhle.

<!-- S50 -->
Což je krásná historka,
až na to, že moderní systém odmítne.
Odpoví, že rekurzivní operace
na lomítku je nebezpečná,
dokud nepřidáš přepínač, že to fakt chceš.

<!-- S51 -->
Příkazy, které opravdu něco zničí,
jsou nudnější.
Smazání ve špatném adresáři.
Přepsání špatného disku.

<!-- S52 -->
Před těmi tě terminál nevaruje,
protože jak on to vidí,
není nic v nepořádku.
Umí se jen zeptat: opravdu to chceš?

<!-- S53 -->
A když odpovíš ano...
klidně ti to uvěří.

<!-- S54 -->
A tady je největší problém
toho hollywoodského stereotypu.
Skutečný útok nemusí jako
hackování vypadat vůbec.

<!-- S55 -->
Může to být ukradené heslo.
Phishing.
Nezáplatovaný server.
Uniklý API klíč.
Heslo použité znovu odjinud.

<!-- S56 -->
Útočník nemusí potřebovat
ani terminál.
Klidně se jen přihlásí
do webového rozhraní.
Jméno.
Heslo.
A je uvnitř.

<!-- S57 -->
Žádný zelený text.
Žádná grafika jako z Matrixu.
Žádná dramatická hudba.

<!-- S58 -->
Což je dost možná mnohem děsivější.

<!-- S59 -->
Lidé si hackera představují jako mikinu,
tmavou místnost a svítící klávesnici.
Nic z toho s hackováním nesouvisí.

<!-- S60 -->
Ten člověk vedle tebe ve vlaku
s úplně obyčejným notebookem
toho může o počítačové bezpečnosti
vědět podstatně víc.

<!-- S61 -->
A ten, co sedí
před šesti servery,
možná jen řeší,
proč nenaběhla databáze.

<!-- S62 -->
Vraťme se k našemu původnímu obrázku.
Muž ukazuje na ženu.
Tys to zahackovala.
Hackovala?

<!-- S63 -->
Možná.
Možná ne.

<!-- S64 -->
Má terminál.
Má nmap.
Má seznam účtů.
Jenže nic z toho nedokazuje,
že něco zahackovala.
Může být správkyně
nebo dělat bezpečnostní audit.

<!-- S65 -->
Nebo taky může hackovat.
My to nevíme.
A v tom je ten vtip.

<!-- S66 -->
Skutečný rozdíl mezi
běžnou správou a hackováním
není v barvě tvého terminálu.
Není v tom, kolik máš monitorů.

<!-- S67 -->
Není v tom, jak rychle píšeš.
A rozhodně není v tom,
jestli máš na sobě mikinu.
Je v tom, co děláš
a jestli k tomu máš oprávnění.

<!-- S68 -->
Takže až příště uvidíš někoho
zírat na černou obrazovku
plnou záhadného textu,
nepředpokládej, že hackuje.

<!-- S69 -->
Možná jen opravuje server.

<!-- S70 -->
I když...
jestli píše devět set slov
za minutu a přitom křičí
„jsem uvnitř"...

<!-- S71 -->
možná stojí za to zeptat se,
co to dělá.
