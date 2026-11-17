<!-- S01 -->
948.
Tolik samostatných způsobů našla AI,
jak převzít počítač s Linuxem zevnitř.

<!-- S02 -->
Žádné ukradené heslo. Žádný průnik po síti.
Každý začíná u běžného uživatele
bez zvláštních práv
a končí u roota,
účtu, který smí všechno.

<!-- S03 -->
OpenAI výsledek zveřejnilo v listopadu 2026.
Celý běh stál
1,2 milionu dolarů v kreditech API.

<!-- S05 -->
Jsou to vlastní čísla OpenAI,
zveřejněná den předtím,
než firma uvedla model, který je vytvořil,
a celkový počet nikdo mimo OpenAI nepotvrdil.
Stovky hlášení a oprav
už ale odešly.

<!-- S06 -->
Tohle se netýká jen Linuxu.
Zdrojový kód Linuxu je veřejný.
Může si ho přečíst kdokoli.
Celá desetiletí to byl argument,
proč je bezpečný.

<!-- S07 -->
Takže když stroj umí veřejný kód přečíst
a v takovém měřítku z něj vyrobit funkční exploity,
neměl by software svůj kód přece jen tajit?

<!-- S08 -->
Podívejme se na software, který to dělá.
V dubnu 2026 opravil Microsoft
164 bezpečnostních chyb
v rámci měsíčních aktualizací.
V říjnu jich opravil
1 413.

<!-- S09 -->
Za ten jediný měsíc jich opravil víc
než za kterýkoli celý rok předtím.
Přes tisíc těch oprav bylo ve Windows
a Microsoft předem varoval,
že nárůst způsobí jeho vlastní nástroje s AI.

<!-- S10 -->
Obě čísla se přímo srovnávat nedají.
Firmy počítají různě
a Microsoft prohledával svůj vlastní neveřejný kód.

<!-- S11 -->
Jedno to ale ukazuje.
Neveřejný kód
chybám nezabránil.

<!-- S12 -->
Co tě tedy doopravdy chrání?
Abychom na to odpověděli,
musíme se podívat, jak ten stroj funguje,
protože každý jeho krok něco vyhodí.

<!-- S13 -->
Linuxové jádro má
přes 40 milionů řádků kódu.
Nejdřív ho prošli průzkumní agenti
a vybrali části,
na které běžný uživatel opravdu dosáhne.

<!-- S14 -->
Zbylo asi sedm procent.
Je to část, na kterou podle nich stálo za to zaútočit,
ne náhodný vzorek,
takže výsledek nemůžeš vynásobit čtrnácti.

<!-- S15 -->
Pak tím kódem prošli analytičtí agenti
a sepsali všechno podezřelé.
2 308 kandidátů,
za dvanáct hodin.

<!-- S16 -->
Jenže podezření nic nedokazuje.
Další agenti proto napsali testovací programy
a spustili je na izolovaných virtuálních strojích.
1 724 chyb
se ukázalo jako skutečných.

<!-- S17 -->
Pak přišla drahá část:
stavba funkčních exploitů,
se zapnutými standardními ochranami
běžného desktopového systému.
1 169 se jich
dostalo na roota.

<!-- S18 -->
Seskup je podle chyby, která za nimi stojí,
a dostaneš těch 948.

<!-- S19 -->
Jeden detail ze zprávy
se jen tak nezapomíná.
V raném běhu
agenti nahlásili 200 úspěchů.
Pak lidé zkontrolovali, jak k nim došli.

<!-- S20 -->
Dvacet se jich dostalo na roota
přes jinou, neznámou chybu,
ne přes tu, kterou měli použít.
Měli otevřít jedny dveře
a našli jiné, o kterých nikdo nevěděl.

<!-- S21 -->
Ve vzorku svých exploitů
OpenAI popsalo deset technik exploitace,
které externí odborníci dosud neviděli.

<!-- S22 -->
V červenci starší model
našel 166 takových chyb.
Po třech měsících oprav
našel novější model 948.
Chyby nedošly.
Pozdější běh našel mnohem víc.

<!-- S23 -->
Má to ale důležitou mez.
Nic z toho se do tvého počítače nedostane
přes internet.
Útočník už musí být na stroji,
jako běžný uživatel.

<!-- S24 -->
To uklidňuje méně, než se zdá,
protože skutečné útoky mívají dva kroky.
Nejdřív se dostaneš dovnitř,
přes chybu v prohlížeči nebo škodlivý soubor.
Pak potřebuješ roota.
Tohle je ten druhý krok.

<!-- S25 -->
Rada OpenAI je přímočará.
Na systému bez nejnovějších oprav
ber každý běžný účet jako roota,
aspoň proti útočníkovi s dostatkem prostředků.

<!-- S26 -->
Kde tedy zůstává
starý argument pro otevřený kód?
Koncem devadesátých let
mu dal Eric Raymond heslo:
„Když se dívá dost očí, žádná chyba se neschová.“

<!-- S27 -->
Nazval to Linusův zákon.
Krásná myšlenka, v níž se skrývá jeden předpoklad:
že se někdo opravdu dívá.

<!-- S28 -->
V roce 2014 se chyba jménem Heartbleed
objevila v OpenSSL,
kódu, který chránil obrovský kus webu.
Ohroženo mělo být asi půl milionu
zabezpečených serverů.

<!-- S29 -->
Chyba ležela ve veřejném kódu dva roky.
Projekt dostával
asi dva tisíce dolarů ročně na darech
a měl jediného vývojáře na plný úvazek.

<!-- S30 -->
Přečíst si to mohl kdokoli.
Skoro nikdo to neudělal.

<!-- S31 -->
To byla vždycky skutečná slabina open source.
Ne moc očí na kódu. Málo.

<!-- S32 -->
A právě to AI mění.
Stroj může skenovat pořád dál
a prověřit mnohem víc kandidátů,
než by sám zvládl lidský výzkumník.
Starý slib se konečně plní,
pro všechny, včetně útočníků.

<!-- S33 -->
Veřejný kód se teď tedy opravdu prohlíží.
Pomůže ho schovat?

<!-- S34 -->
Uzavřený program přece musí běžet,
takže jeho strojový kód leží
na každém počítači, který ho používá.
Nástroje jako Ghidra z něj udělají zpátky
něco jako zdrojový kód.

<!-- S35 -->
A je tu klasický trik.
Porovnej program
před bezpečnostní aktualizací a po ní.
Co se změnilo, ukazuje, kde byla díra.

<!-- S35b -->
Útočníkům to prozradí, kam mířit,
dřív, než si všechny systémy
aktualizaci nainstalují.

<!-- S36 -->
Anthropic to zkusil na jádře Windows,
na 21 chybách,
které Microsoft nedávno opravil,
a bez zdrojového kódu.
První pád AI vyvolala za 31 minut.
Do šesti hodin jich měla 18.

<!-- S37 -->
Osm se jich stalo funkčními exploity,
které dokázaly plně ovládnout počítač,
každý zhruba za dva tisíce dolarů.

<!-- S38 -->
Nebyly to ale neznámé chyby.
Záplaty už ukazovaly,
kde problém je.
Najít novou chybu od nuly je těžší.

<!-- S39 -->
Utajení tedy útočníka pořád něco stojí.
Je to retardér, ne zeď.
Jak vysoký?
Veřejné číslo neexistuje.

<!-- S40 -->
A druhá strana?
Co ti otevřenost vlastně dává?
Odpověď je v malém detailu
zprávy OpenAI.

<!-- S41 -->
Během těch deseti dní skenu a analýzy
přes sto těchto linuxových chyb
opravili, nebo se k tomu chystali,
jiní lidé.
Asi o třech stech dalších
se už veřejně diskutovalo.

<!-- S42 -->
Jiní našli stejné chyby
ve stejnou dobu.

<!-- S43 -->
Linus Torvalds to popsal už v květnu.
Podle něj hlášení z AI
zahltila bezpečnostní e-mailovou konferenci jádra
tak, že je „téměř úplně nezvládnutelná“,
protože různí lidé pořád nacházeli
totéž stejnými nástroji.

<!-- S44 -->
A poradil tohle:
„Pokud jsi chybu našel pomocí nástrojů AI,
je dost možné, že ji našel i někdo jiný.“

<!-- S45 -->
Pravidla jádra to teď říkají na rovinu.
Chyba nalezená s AI se musí brát jako veřejná,
protože se takové chyby objevují
u několika výzkumníků naráz,
často týž den.

<!-- S46 -->
Domysli, co to dělá
s představou tajné chyby.
Když tě její nalezení stálo málo,
stálo to málo každého.

<!-- S47 -->
U open source
si může každý prohlédnout hlášení,
ověřit opravu a výsledek zpochybnit.
U uzavřeného softwaru
musíš většinou věřit výrobci.

<!-- S49 -->
Otevřenost má ale svou cenu,
a není to ta, kterou bys čekal.
Nabízí se říct,
že malý projekt nemá na skenování.
Firmy s AI už ale
nabízejí správcům přístup zdarma.

<!-- S50 -->
Chybí lidé.
Jádro dřív evidovalo
asi 500 bezpečnostních chyb na vydání.
Letos překročilo 1 500.
Spousta jich je drobných,
ale někdo je stejně musí projít.

<!-- S51 -->
V lednu ukončil projekt curl
placené odměny za nalezené chyby,
aby přestal odměňovat záplavu bezcenných hlášení.

<!-- S52 -->
I dobrá hlášení práci jen posunou dál.
Záplaty z AI pořád potřebují lidskou kontrolu.
Některé rané opravy přidávaly zbytečný kód
nebo přehlédly jiné varianty téže chyby.

<!-- S53 -->
Víc skenování si koupit můžeš.
Víc lidí, kteří kus kódu
znají takhle dobře, si nekoupíš.
Tady má firma s placeným bezpečnostním týmem
opravdu náskok.

<!-- S54 -->
A pak přichází poslední problém.
Opraveno neznamená nainstalováno.

<!-- S55 -->
V březnu 2017
opravil Microsoft chybu ve Windows.
Uzavřený kód, jeden výrobce, jeden systém aktualizací.
O dva měsíce později
prošel toutéž dírou WannaCry
do nějakých dvou set tisíc počítačů
asi ve sto padesáti zemích.

<!-- S56 -->
Ta záplata měla dva měsíce na to, aby se rozšířila,
a nestačilo to.
Dva měsíce ti dnes útočník možná nedá.
Ve stejné studii Anthropicu
vzala AI veřejnou opravu
JavaScriptového jádra Firefoxu
a funkční exploit měla za necelou hodinu.

<!-- S57 -->
Do vydání opravené verze Firefoxu
zbývalo ještě osmnáct dní.

<!-- S58 -->
To je nebezpečí zveřejněné opravy.
Informace se k útočníkům může dostat
dřív než aktualizace k tobě.

<!-- S59 -->
Oprava Linuxu má před sebou dlouhou cestu,
z jádra do stabilního vydání,
do tvé distribuce, do tvého zařízení.
Telefon může čekat měsíce, nebo navždy.

<!-- S60 -->
A uzavřený software tomu neunikne.
Právě jsme to viděli: záplata Windows stačila.
Každá aktualizace je teď zároveň mapa.

<!-- S60b -->
Takže měj všechno aktualizované,
počítač, telefon, i router,
a instaluj aktualizace, jakmile vyjdou.
Čím líp AI umí dělat z oprav útoky,
tím víc bude záležet na každém dni čekání.

<!-- S61 -->
Je tedy open source pořád bezpečnější?
Upřímně, nikdo to neví.
Podle toho, co je veřejně známo,
nikdo neudělal stejný test na obou stranách
za stejných pravidel.

<!-- S62 -->
Můžeme ale říct aspoň tohle.
Skrývání kódu přináší méně než dřív.
Když ho ukážeš, může práci kontrolovat kdokoli,
a přidáš větší hromadu té práce
těm, kdo ho udržují.

<!-- S64 -->
I kdyby AI nikdy nenašla každou chybu,
už změnila ekonomiku jejich hledání.

<!-- S65 -->
Teď záleží na tom, jak dlouho zůstane díra otevřená
mezi chvílí, kdy ji někdo najde,
a chvílí, kdy se zavře na tvém stroji.

<!-- S66 -->
Takže otázka pro tebe.
Když může kteroukoli chybu najít kdokoli,
věřil bys radši kódu, který si můžeš přečíst,
nebo firmě, která dostává zaplaceno za opravy?
Napiš to do komentářů.
