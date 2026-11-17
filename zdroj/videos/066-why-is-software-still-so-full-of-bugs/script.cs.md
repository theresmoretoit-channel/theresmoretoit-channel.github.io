<!-- S01 -->
Každých pár dní se ve zprávách
objeví další vážná chyba.
Chyba, díky které jde obejít přihlášení.
Chyba, kvůli které unikají soukromá data.
Chyba, která útočníkovi předá váš počítač.

<!-- S02 -->
Jednou je to Windows. Jindy Linux.
Prohlížeč, databáze, cloudová služba...
nebo malá knihovna,
na které závisejí miliony vývojářů.

<!-- S03 -->
A reakce je skoro pokaždé stejná.
Jak to mohli programátoři přehlédnout?

<!-- S04 -->
Jsou to přece profesionálové.
Mají revize kódu, automatické testy,
bezpečnostní audity, fuzzing...
a chyby stejně přibývají dál.

<!-- S05 -->
Dá se tedy vůbec napsat
složitý software bez chyb?

<!-- S06 -->
Začněme jedním číslem.
Představte si program s pouhými sto nastaveními
a každé je buď zapnuté, nebo vypnuté.

<!-- S07 -->
Sto jednoduchých rozhodnutí ano, nebo ne.
Kolik je to kombinací?

<!-- S08 -->
Dvě na stou.
To je zhruba milion bilionů bilionů.

<!-- S09 -->
Teď si představte, že dokážete otestovat
miliardu kombinací za sekundu.
A že jste začali při velkém třesku.

<!-- S10 -->
Do dneška byste otestovali
zhruba jednu kombinaci ze tří tisíc.

<!-- S11 -->
A sto přepínačů není nic.
Skutečný program jich má miliony.
Takže „prostě otestovat všechno“
není drahé. Je to nemožné.

<!-- S12 -->
A nejsou to nijak exotické přepínače.
Vezměte jednu z nejjednodušších věcí,
jaké program vůbec dělá.
Uživatel si řekne o svůj účet podle jeho čísla.
My ho najdeme v databázi.
A pošleme mu ho.

<!-- S13 -->
Jenže co když ten uživatel neexistuje?
Co když někdo pošle místo čísla text?
Nebo záporné číslo? Nebo obrovské?

<!-- S14 -->
Co když se na to ten člověk nesmí dívat?
Co když někdo smaže účet
přesně ve chvíli, kdy ho načítáme?
Co když stejný požadavek přijde dvakrát?

<!-- S15 -->
Každá z těch otázek je jednoduchá.
Problém je v tom, jak se kombinují.
Každá je další přepínač.

<!-- S15b -->
Mimochodem, jestli se vám takováhle
videa líbí, můžete se přihlásit k odběru.

Kanálu to opravdu pomůže.

<!-- S16 -->
A počítač to za nás nevyřeší.
Udělá přesně to, co mu řekneme.
Ne to, co jsme mysleli.

<!-- S17 -->
Proto jsme vymysleli programovací jazyky.
Díky nim můžeme popsat složité věci
bez přemýšlení o každém detailu.

<!-- S18 -->
Jenže některé z nich hlídají míň,
než byste čekali.
Třeba C. Je rychlé, jednoduché
a dává vám obrovskou kontrolu nad pamětí.

<!-- S19 -->
Takže můžete napsat tohle.
Vyhradíme místo na šestnáct znaků.
A pak řekneme: sem zkopíruj vstup.

<!-- S20 -->
Co když má ten vstup
pět set znaků?
C se nezeptá.
Prostě píše dál za konec.

<!-- S21 -->
A co leží hned za těmi šestnácti znaky?
Často něco hodně důležitého.

<!-- S22 -->
Když program volá funkci,
poznamená si, kam se má vrátit,
až funkce skončí.
Návratovou adresu.
V klasickém uspořádání leží
kousek za koncem našeho bufferu.

<!-- S23 -->
Útočník tedy pošle vstup
přesně té správné délky.
Nejdřív svoje vlastní instrukce.
A pak, úplně na konci, novou návratovou adresu...
která ukazuje zpátky na ty instrukce.

<!-- S24 -->
Funkce skončí.
Procesor se podívá, kam se má vrátit...
a skočí rovnou do útočníkova kódu.

<!-- S25 -->
Teď běží jeho program,
se všemi oprávněními toho vašeho.
Tomu se říká „spuštění libovolného kódu“.

<!-- S26 -->
A procesor přitom nic špatně neudělal.
Řídil se instrukcemi.

<!-- S27 -->
V roce 1988 přesně taková chyba
umožnila Morrisovu červu
rozšířit se po raném internetu.
A stejný trik se od té doby
používá při útocích dodnes.

<!-- S28 -->
Novější jazyky proto část práce předávají
překladači.
Třeba Rust odmítne přeložit
spoustu programů, které by mohly s pamětí zacházet špatně.

<!-- S29 -->
Programátor říká:
ale já přesně vím, co dělám!
A překladač na to:
to říká každý.

<!-- S30 -->
A je správně, že je podezíravý.
Microsoft i tým Chromu v Googlu
shodně uvádějí,
že zhruba sedmdesát procent
bezpečnostních chyb, které zkoumali,
pochází z problémů s paměťovou bezpečností.

<!-- S31 -->
Jenže program může s pamětí pracovat úplně bezpečně
a přesto dělat všechno špatně.

<!-- S32 -->
Představte si, že se uživatel přihlásí.
Heslo se ověří správně.
Nic nespadne. Paměť se nijak nepoškodí.

<!-- S33 -->
A pak mu program ukáže
data někoho jiného.
Protože kontrola oprávnění
byla napsaná trochu špatně.

<!-- S34 -->
Tohle žádný jazyk sám od sebe nezachytí.
Jazyk neví,
co měl program dělat.
To víme jenom my.

<!-- S35 -->
Takže zpátky k testování.
Test vám může říct:
pro tenhle vstup jsem dostal tenhle výsledek.

<!-- S36 -->
Nemůže vám říct:
program funguje správně pro každý vstup.
A už jsme viděli,
proč je nemůžeme vyzkoušet všechny.

<!-- S37 -->
V roce 1970 to informatik
Edsger Dijkstra shrnul jednou větou.
Testování může ukázat přítomnost chyb,
ale nikdy jejich nepřítomnost.

<!-- S38 -->
Dobře. Tak proč místo testování
nenapsat program,
který kontroluje jiné programy
a dokazuje, že fungují správně?
Dáte mu jakýkoli kód a on vám řekne,
jestli ten kód dělá, co má.

<!-- S39 -->
Na tuhle otázku přišla odpověď
dřív, než vznikl první skutečný počítač.
V roce 1936 Alan Turing dokázal,
že takový program existovat nemůže.

<!-- S40 -->
Ne že ho zatím nikdo nepostavil.
Že vůbec existovat nemůže.

<!-- S41 -->
Ukázal, že žádný program nedokáže
u každého jiného programu rozhodnout,
jestli se někdy zastaví.

<!-- S42 -->
A v roce 1953 zašel Henry Rice ještě dál.
Totéž platí pro každou netriviální otázku
o tom, co program doopravdy dělá.

<!-- S43 -->
Je bezpečný? Unikají z něj data?
Dává správnou odpověď?
Neexistuje žádná obecná metoda,
která by to rozhodla pro každý program.

<!-- S44 -->
Je tedy software bez chyb nemožný?
Ne tak docela.
U jednoho konkrétního programu
se někdy dá dokázat, že je správný,
s obrovským úsilím.

<!-- S45 -->
V roce 2009 tým v Austrálii dokázal,
že malé jádro operačního systému
jménem seL4
dělá přesně to, co říká jeho specifikace.

<!-- S46 -->
Mělo necelých deset tisíc řádků kódu.
Napsat to jádro trvalo
zhruba dva člověkoroky.
Dokázat jeho správnost zhruba dvacet.
Moderní webový prohlížeč
má desítky milionů řádků.

<!-- S47 -->
A i ten důkaz má háček.
Ukazuje, že program odpovídá specifikaci.
Nemůže ukázat, že ta specifikace
je to, co jsme doopravdy chtěli.

<!-- S48 -->
A specifikaci píšou lidé.
Takže se ta otázka vrací k nám.

<!-- S49 -->
A nejde jen o náš vlastní kód.
Dnešní programátor staví na frameworcích,
knihovnách a stovkách závislostí.
Každá vrstva nám ušetří obrovské množství práce.
Jenže každá vrstva je něco,
čemu musíme rozumět...
nebo aspoň věřit.

<!-- S50 -->
Takže abyste měli v softwaru chybu,
nemusíte ji napsat.
Stačí si ji nainstalovat.

<!-- S51 -->
K tomu přidejte tlak.
Nikdo nechce dokonalý produkt za deset let.
Chce fungující produkt příští měsíc.
A průnik, ke kterému nikdy nedošlo,
se v prezentaci ukazuje hodně těžko.

<!-- S52 -->
A teď ta nejpodivnější část.
Naše nástroje jsou pořád lepší.
Bezpečnější jazyky, fuzzing, odměny za nalezené chyby...

<!-- S53 -->
A přesto počet známých zranitelností
dál roste.
Jen za rok 2024 jich zhruba čtyřicet tisíc
dostalo oficiální číslo.

<!-- S54 -->
Zčásti proto, že taky píšeme
nesrovnatelně víc softwaru než kdykoli dřív.
Jako bychom dělali každou silnici bezpečnější...
a přitom stavěli milionkrát víc silnic.

<!-- S55 -->
Dělají tedy programátoři svou práci špatně?
Ne.
Chceme po nich něco,
co žádná obecná metoda nedokáže zaručit.

<!-- S56 -->
Takže možná
„jak napsat software bez chyb?“
je špatná otázka.

<!-- S57 -->
Lepší otázka zní:
jak stavět systémy, které zůstanou bezpečné,
i když je v softwaru chyba?

<!-- S58 -->
A přesně tam se bezpečnost ubírá.
Neříká: nikdy neudělej chybu.
Říká: počítej s tím, že už jsi ji udělal.

<!-- S59 -->
Vzpomínáte na tu návratovou adresu?
Dnes ji systém hlídá.
Přehází, kde co v paměti leží.
A odmítne spustit instrukce
schované v datech.

<!-- S60 -->
Chyba v našem kódu v C tam pořád je.
Jenom se z ní mnohem hůř dělá útok.

<!-- S61 -->
A stejná myšlenka je všude.
Sandboxy, omezená oprávnění,
izolované procesy, šifrování,
zálohy, monitoring...
vrstva za vrstvou,
aby se z jedné chyby nestala katastrofa.

<!-- S62 -->
A má to velmi praktický důsledek.
Když jsou chyby nevyhnutelné,
opravovat je prostě musíme.

<!-- S63 -->
Software, který dnes používáte,
klidně může obsahovat zranitelnost,
kterou zatím nikdo nenašel.

<!-- S64 -->
A až ji někdo najde,
závisí na aktualizaci, jestli to bude
„objevili jsme zranitelnost“
nebo „hackli nás“.

<!-- S65 -->
Totéž platí pro systémy, které stavíme.
Staré knihovny a nepodporované platformy
nejsou bezpečnější tím, že je ignorujeme.
Mění se v technický dluh.

<!-- S66 -->
A proč se ten dluh musí splatit,
o tom je moje video
„Vždyť to funguje.
Tak proč to upgradovat?“

<!-- S67 -->
Protože v softwaru
„pořád to funguje“
a „pořád je to bezpečné“
jsou dvě velmi odlišné věci.
