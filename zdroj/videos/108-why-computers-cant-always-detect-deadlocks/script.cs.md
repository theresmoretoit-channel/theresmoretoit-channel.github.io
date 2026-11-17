<!-- S01 -->
Ke křižovatce přijedou čtyři auta
přesně ve stejnou chvíli.
Žádné semafory. Žádné značky.
Jen pravidlo, které platí v mnoha zemích:
dej přednost autu zprava.

<!-- S02 -->
Každý řidič se podívá doprava
a vidí auto, kterému musí dát přednost.
Takže každý řidič čeká.

<!-- S03 -->
Nikdo neporušuje pravidla.
Všichni je dodržují dokonale.
A nikdo se nikdy nepohne.

<!-- S04 -->
Informatici tomu říkají deadlock, neboli uváznutí.
A neděje se to jen na silnicích.
Děje se to v databázích,
operačních systémech i v běžném softwaru.

<!-- S05 -->
Počítače často umějí deadlock dobře poznat,
když už nastal.
Dokáže ale program přečíst jiný program
a říct ti s jistotou,
jestli někdy uvázne?

<!-- S06 -->
U mnoha programů ano.
Ale metoda, která funguje
pro každý možný program,
existovat nemůže.
A ne proto, že by počítače
ještě nebyly dost rychlé.
Žádný rychlejší počítač na tom nic nezmění.

<!-- S07 -->
Takhle program uvázne.
Představ si e-shop,
ve kterém běží dvě úlohy současně.

<!-- S08 -->
Než úloha cokoli změní,
vezme si na to zámek,
aby na to nikdo jiný nemohl sáhnout.
Jako když si vezmeš jediný klíč od místnosti.

<!-- S09 -->
První úloha zamkne zákazníkův účet
a pak sáhne po jeho objednávce.
Druhá zamkne objednávku
a pak sáhne po účtu.

<!-- S10 -->
Jedna drží účet
a čeká na objednávku.
Druhá drží objednávku
a čeká na účet.
Ani jedna nepustí, co drží.

<!-- S11 -->
A zvláštní je,
že tenhle kód může proběhnout milionkrát
bez jediného problému.
Jen když se ty dvě úlohy překryjí
přesně v tom špatném pořadí,
všechno se zastaví.

<!-- S12 -->
Chyba tam byla celou dobu.
Načasování ji jen odhalilo.

<!-- S12b -->
Mimochodem, jestli se ti takováhle
videa líbí, můžeš se přihlásit k odběru.

Kanálu to opravdu pomůže.

<!-- S13 -->
Databáze na tohle narážejí pořád,
a tak hlídají.
Kreslí si mapu, kdo na koho čeká.

<!-- S14 -->
První čeká na druhou.
Druhá čeká na první.
Když se šipky uzavřou do smyčky,
je to deadlock.
Žádné hádání. Smyčka je přímo tam.

<!-- S15 -->
Pak databáze udělá něco brutálního.
Vybere jednu z úloh
a její práci zahodí.

<!-- S16 -->
SQL Server od Microsoftu dokonce oznámí
poraženému, že byl vybrán
jako oběť deadlocku
a má to zkusit znovu.

<!-- S17 -->
Druhá úloha pokračuje
a oběť to prostě může zkusit znovu.

<!-- S18 -->
Všimni si, co to opraví a co ne.
Uváznutí je vyřešené.
Ale kód, který ho způsobil, tam pořád je
a čeká na další nešťastnou chvíli.

<!-- S19 -->
Poznat deadlock,
který už nastal,
je tedy ta snadná část.
Ta těžká otázka je jiná.

<!-- S20 -->
Ne: uvázl ten program právě teď?
Ale: dej mu tenhle vstup.
Může někdy uváznout?

<!-- S21 -->
To první je fotka přítomnosti.
Stačí se na ni podívat.
To druhé je předpověď
každé možné budoucnosti.

<!-- S22 -->
A programy to hodně ztěžují.
Rozhodují se. Opakují věci.
Můžou spouštět výpočty, které trvají
sekundu, nebo tisíc let.

<!-- S23 -->
Program může uváznout hned,
po milionu kroků,
kvůli jednomu vzácnému vstupu,
nebo vůbec nikdy.

<!-- S24 -->
Mohl bys ho prostě spustit a sledovat.
Ale když za hodinu pořád neuvázl,
co ti to řekne?

<!-- S25 -->
Nic.
Může uváznout v příští sekundě,
nebo nikdy.

<!-- S26 -->
V roce 1936 mladý matematik
jménem Alan Turing ukázal,
že na některé otázky o programech
nedokáže odpovědět žádný program.
Ta nejslavnější zní ještě jednodušeji.

<!-- S27 -->
Vezmi libovolný program a jeho vstup.
Zastaví se nakonec?
Nebo poběží navždy?

<!-- S28 -->
Dnes se tomu říká problém zastavení.
A žádný program ho nedokáže vyřešit
správně ve všech případech.

<!-- S29 -->
Myšlenka důkazu
je překvapivě krátká.
Představ si, že ti někdo dá
dokonalý kontrolor zastavení.

<!-- S30 -->
Teď napíšeš malý vzdorovitý program.
Zeptá se kontroloru sám na sebe
a pak udělá pravý opak.

<!-- S31 -->
Když kontrolor řekne, že se zastaví,
program se zacyklí navždy.
Když kontrolor řekne, že poběží navždy,
program se okamžitě zastaví.

<!-- S32 -->
Ať kontrolor o tomhle programu řekne cokoli,
mýlí se.
Takže dokonalý kontrolor existovat nemůže.

<!-- S33 -->
Co to má tedy společného s deadlocky?
Všechno.

<!-- S34 -->
Představ si, že někdo tvrdí, že sestrojil
dokonalý předpovídač deadlocků.
Dáš mu libovolný program a jeho vstup
a on ti vždycky správně řekne,
jestli ten program někdy uvázne.

<!-- S35 -->
Použijme ho
k vyřešení problému zastavení.

<!-- S36 -->
Vezmi libovolný program
a zabal ho do nového programu.

<!-- S37 -->
Nový program nejdřív
prostě spustí ten starý,
krok za krokem, v jediném vlákně.
Žádné zámky. Nic sdíleného.
Nic, co by vůbec mohlo uváznout.

<!-- S38 -->
Pak, pokud starý program někdy skončí,
spustí nový program dvě úlohy.
Každá si vezme jeden zámek,
počká, až ta druhá vezme ten svůj,
a pak sáhne po tom cizím.
Deadlock, schválně, pokaždé.

<!-- S39 -->
Když starý program nikdy neskončí,
nový se tam nikdy nedostane.
Žádný deadlock. Nikdy.

<!-- S40 -->
Nový program tedy uvázne
právě tehdy, když se ten starý zastaví.

<!-- S41 -->
Teď se zeptej předpovídače
na ten nový program.
„Ano, uvázne“
znamená, že se starý program zastaví.
„Ne“ znamená, že poběží navždy.

<!-- S42 -->
Právě jsme vyřešili problém zastavení.
A to je přesně to, co nejde.

<!-- S43 -->
Takže ani dokonalý předpovídač deadlocků
nemůže existovat.

<!-- S44 -->
Potíž není v zámcích,
v databázích ani ve špatných programátorech.
Program může deadlock schovat
za libovolný výpočet.
Abys předpověděl ten deadlock,
musel bys předpovědět, jestli ten výpočet skončí.

<!-- S45 -->
Ale moment.
Skutečný počítač není nekonečný.
Jeho paměť má omezený počet stavů.
Nešlo by je prostě všechny zkontrolovat?

<!-- S46 -->
U stroje s pevně danou
pamětí v principu ano.
V praxi je zkus spočítat.

<!-- S47 -->
Paměť notebooku
s osmi gigabajty
se dá uspořádat tolika způsoby,
že jen zapsat to číslo
zabere asi dvacet miliard číslic.

<!-- S48 -->
Počet atomů
v pozorovatelném vesmíru
jich má asi osmdesát.

<!-- S49 -->
Na skutečném stroji je tedy zkontrolovat
všechno v teorii možné
a v praxi beznadějné.

<!-- S50 -->
To je ale jiná zeď.
Turingova mez není o tom, že je stavů moc.
Platí pro programy,
které si můžou vždycky říct o další paměť.
Pro ty žádný dokonalý předpovídač existovat nemůže,
ať je počítač jakkoli velký.

<!-- S51 -->
Takže s deadlocky nic nenaděláme?
Ne.
Znamená to jen, že neexistuje dokonalý kontrolor.
A tak programátoři píšou programy,
které se kontrolují snáz.

<!-- S52 -->
Nejjednodušší trik je pořadí.
Každá úloha musí zamknout účet
dřív než objednávku.
Nikdy naopak.

<!-- S53 -->
Když se toho pořadí opravdu drží každá úloha,
smyčka nevznikne
a tenhle druh deadlocku nastat nemůže.

<!-- S54 -->
Jiné systémy to po časovém limitu vzdají,
vezmou si všechny zámky naráz,
nebo nechají databázi vybrat oběť
a prostě to zkusí znovu.

<!-- S55 -->
A u malých, pečlivě popsaných návrhů
dokážou nástroje projít každý možný stav.
Inženýři v Amazonu jeden takový použili
a našli chybu, která potřebovala pětatřicet kroků
přesně ve správném pořadí, aby se projevila.

<!-- S56 -->
Tyhle nástroje fungují,
protože se problém zmenšil.
Kontrolují model systému,
ne každý program, který by kdy mohl existovat.

<!-- S57 -->
U skutečného kódu ale
kontrolor, který vezme jakýkoli program,
musí něco obětovat.
Může varovat před deadlocky,
které nastat nemůžou,
přehlédnout některé, které nastat můžou,
nebo občas neodpovědět vůbec.

<!-- S58 -->
Kontrolor, který nikdy nevyhlásí planý poplach,
nikdy žádný deadlock nepřehlédne
a vždycky odpoví,
a to u každého programu,
je přesně to, co Turing vyloučil.

<!-- S59 -->
Zpátky na křižovatce:
ti čtyři řidiči tam nebudou stát navždy.

<!-- S60 -->
Někdo zamává.
Jeden řidič se vzdá přednosti
a za pár vteřin je po všem.

<!-- S61 -->
Přesně tohle dělá i databáze.
Uváznutí nepředpovídá.
Všimne si ho
a přiměje někoho dát přednost.

<!-- S62 -->
Některé problémy potřebují rychlejší počítač.
Některé lepší nápad.

<!-- S63 -->
A některé, jako tenhle,
nemají dokonalé řešení vůbec.
Jen dobrá pravidla
a někoho, kdo je připravený zamávat.
