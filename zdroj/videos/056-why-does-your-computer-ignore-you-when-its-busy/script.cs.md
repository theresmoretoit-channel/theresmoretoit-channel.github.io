<!-- S01 -->
Klikneš na tlačítko.
Nic se nestane.
Klikneš znovu.
Pořád nic.

<!-- S02 -->
Pohneš myší.
Nic.
Na pár sekund
vypadá počítač úplně mrtvý.

<!-- S03 -->
A pak se všechno stane naráz.
Okno se posune.
Nabídka se otevře.
Všechna tvoje kliknutí dorazí
najednou.

<!-- S04 -->
A teď to zvláštní.
Počítač o tom kliknutí věděl.
Věděl to během mikrosekund.

<!-- S05 -->
To není odhad.
Právě teď, když zrovna
nic zvláštního neděláš,
odbavuje tvůj stroj tisíce
hardwarových událostí za sekundu.

<!-- S06 -->
Stisk klávesy.
Příchozí paket.
Tik časovače.
Disk, který dokončil práci.

<!-- S07 -->
Každá z nich je přerušení
a počítače to tak dělají
už od padesátých let,
přesně kvůli tomuhle:

<!-- S08 -->
aby procesor mohl reagovat
na svět kolem sebe.

<!-- S09 -->
Hardware tedy kliknutí ohlásil.
Procesor si ho všiml.
A ty jsi přesto pět sekund
zíral na mrtvou obrazovku.

<!-- S10 -->
Neměl by mít uživatel přednost?

<!-- S11 -->
Existuje na to odpověď
a není to tím,
že by byl počítač pomalý.

<!-- S12 -->
Je to tím, že všimnout si
a obsloužit
jsou dvě úplně různé věci.

<!-- S13 -->
Začněme tím všimnutím.
Představ si počítač bez přerušení.

<!-- S14 -->
Procesor by se musel
pořád dokola ptát:
Přišlo něco z klávesnice?
Dokončil disk práci?

<!-- S15 -->
Dorazil paket?
Pohnula se myš?
A pak se ptát znovu.
A znovu.

<!-- S16 -->
Skoro každá odpověď by byla ne
a samotné ptaní
by ten stroj sežralo zaživa.

<!-- S17 -->
Zařízení proto dostala možnost ozvat se.
Myš se pohne,
hardware vyvolá přerušení

<!-- S18 -->
a procesor pustí z ruky,
co zrovna dělal,
skočí do krátkého kusu kódu,
kterému se říká obsluha,

<!-- S19 -->
a operační systém se dozví,
že se něco stalo.

<!-- S20 -->
Je to skvělý nápad.
A vede k jednomu velmi
rozumnému předpokladu.

<!-- S21 -->
Když se procesor dá vytrhnout
od čehokoli, okamžitě,
tak se přece i moje kliknutí
odbaví okamžitě.

<!-- S22 -->
Jenže obsluha toho nesmí
udělat skoro nic.

<!-- S23 -->
Dokud je procesor uvnitř,
čeká všechno ostatní.
Včetně dalšího přerušení.
A to už je na cestě.

<!-- S24 -->
Pravidlo je tedy přesně opačné,
než bys čekal.
Obsluha udělá tak málo,
jak jen to jde.

<!-- S25 -->
Poznamená si, co se stalo.
Potvrdí zařízení,
že zpráva dorazila.
Odloží událost do fronty.
A zmizí.

<!-- S26 -->
Vývojáři jader tu práci dokonce
dělí na dvě pojmenované půlky:
na to, co se musí stát hned,
a na to, co počká.

<!-- S27 -->
Všechno zajímavé,
všechno, co kdy uvidíš,
je v té druhé půlce.

<!-- S28 -->
A tady máme první odpověď.
Přerušení získá
pozornost počítače.

<!-- S29 -->
Nedostane tvůj program
na procesor.

<!-- S30 -->
Dobře, řekneš. Tak to sprav.
Udělej ze vstupu to nejdůležitější
v celém baráku.

<!-- S31 -->
Myš? Nejvyšší priorita.
Klávesnice? Nejvyšší priorita.
Okno, na které se díváš?
Nejvyšší priorita.

<!-- S32 -->
Všechno ostatní počká.
Zní to naprosto rozumně.

<!-- S33 -->
A nejlepší námitka proti tomu
se odehrála na Marsu.

<!-- S34 -->
V roce 1997 přistál modul
Pathfinder a začal pracovat.
Pak se po pár dnech
začal sám restartovat.

<!-- S35 -->
Ne kosmické záření.
Ne rozbitá součástka.
Chyba v plánování.

<!-- S36 -->
Byla tam úloha s vysokou prioritou,
která rozvážela data
po celé sondě,
a potřebovala sdílený kus paměti.

<!-- S37 -->
Úloha s nízkou prioritou,
která sbírala údaje o počasí,
tam byla dřív
a držela si ji.

<!-- S38 -->
Což by chvíli
vůbec nevadilo.
Jenže pak si procesor vzala
úloha se střední prioritou

<!-- S39 -->
a ta s nízkou prioritou
se nedostala k dokončení.
Takže paměť nikdy nepustila.

<!-- S40 -->
Nejdůležitější úloha
na celé sondě
teď uvízla za tou
úplně nejméně důležitou.

<!-- S41 -->
Má to svoje jméno.
Inverze priorit.

<!-- S42 -->
Hlídací časovač si všiml,
že ta důležitá úloha
už dlouho neproběhla,
usoudil, že je zle,

<!-- S43 -->
a restartoval celou sondu.
Pak se to stalo znovu.
A znovu.

<!-- S44 -->
Inženýři na Zemi na to přišli
a poslali na Mars opravu.

<!-- S45 -->
A poučení si odneseme
úplně zadarmo.
Vysoká priorita neznamená,
že tě někdo obslouží.

<!-- S46 -->
Znamená jen, že se zeptá dřív.
Když to, co potřebuješ,
drží někdo pomalejší,
tvoje důležitost ti nekoupí nic.

<!-- S47 -->
A priorita má druhou mez.
Rozhoduje o pořadí.
Nevyrobí ani jeden
takt navíc.

<!-- S48 -->
Řekněme, že máš všechna jádra
na sto procentech.
Řekl bys, že to znamená zamrznutí.
Obvykle neznamená.

<!-- S49 -->
Plánovač rozdává úseky času
tak rychle,
že ty přechody vůbec necítíš.

<!-- S50 -->
Proto můžeš kompilovat
něco obrovského
a přitom posouvat stránku
v prohlížeči.

<!-- S51 -->
Při zátěži se nemění
ani tak rychlost.
Počítač není pomalý.

<!-- S52 -->
Přichází pozdě.

<!-- S53 -->
Klikneš a odpověď přijde
o půl sekundy později.
Pak o sekundu.
Pak o pět.

<!-- S54 -->
A lidé si toho všímají
neuvěřitelně dobře.
Půl sekundy působí jako stroj,
který přemýšlí.

<!-- S55 -->
Pět sekund působí jako stroj,
který umřel.

<!-- S56 -->
A pak je tu podoba téhle potíže,
která překvapí nejvíc.
Někdy není problém
vůbec v procesoru.

<!-- S57 -->
Otevři toho příliš mnoho naráz
a fyzická paměť se zaplní.
Operační systém začne odsouvat
stránky paměti na disk.

<!-- S58 -->
Když se toho nahromadí dost,
a stroj bude trávit čas
přehazováním paměti
místo aby dělal tvoji práci.

<!-- S59 -->
Taky to má svoje jméno.
Thrashing.

<!-- S60 -->
A tohle je ta matoucí věc,
protože procesor
vůbec nemusí vypadat vytíženě.

<!-- S61 -->
On nepracuje.
On čeká.

<!-- S62 -->
Čekající úloze můžeš dát
nejvyšší prioritu v systému
a bude čekat
úplně stejně dlouho.

<!-- S63 -->
A pak je tu
nejlidštější podoba téhle potíže.
Událost dorazila.
Jádro ji má.

<!-- S64 -->
Leží ve frontě
a je na ní jméno tvého programu.
A ten program
si ji nevyzvedává.

<!-- S65 -->
Možná zrovna počítá něco dlouhého
na tomtéž vlákně,
které má hlídat
jeho vlastní okno.

<!-- S66 -->
Takže myš funguje.
Klávesnice funguje.
Ostatní programy fungují.

<!-- S67 -->
A to jedno okno zešedne
a napíše, že neodpovídá.

<!-- S68 -->
Což není diagnóza.
Windows tenhle nápis zobrazí
zhruba po pěti sekundách,
kdy si nikdo nevyzvedl zprávy.

<!-- S69 -->
Systém je naprosto v pořádku.
Jenom ta aplikace
nepřišla ke dveřím.

<!-- S70 -->
Že počítač kliknutí přijal
a že na něj aplikace odpověděla,
nejsou tytéž události.

<!-- S70b -->
Mimochodem, jestli tě zajímá,
kam nás zavede další otázka,
můžeš se přihlásit k odběru.

Kanálu to opravdu pomůže.
<!-- S71 -->
Zbývá ještě jeden článek řetězu
a je to ten,
na který nikdy nemyslíme.
Nic z toho zatím nedalo
na obrazovku vůbec nic.

<!-- S72 -->
Aplikace změní svůj stav.
Někdo musí složit další snímek.
Grafická karta ho musí vykreslit.
Displej ho musí ukázat.

<!-- S73 -->
Na běžné obrazovce
se nový obraz objeví
zhruba každých šestnáct milisekund.

<!-- S73b -->
Je tedy rozdíl mezi tím,
že počítač tvoje kliknutí odbavil,
a tím, že to vidíš.

<!-- S74 -->
A úplně pod tím vším
leží něco,
co nespraví žádné inženýrství.
Operační systém ví,
že se pohnula myš.
Vůbec netuší proč.

<!-- S75 -->
Možná zrovna míříš na něco
ve hře.
Nebo upravuješ dokument.
Nebo jsi jen vrazil do stolu.

<!-- S76 -->
Pro hardware
jsou to tytéž události.
Systém umí seřadit druhy práce.
Neumí uhodnout, co jsi tím myslel.

<!-- S77 -->
Tak dělá kompromis.
Dost rychle pro tebe,
většinou,
a přitom zbytek nenechá čekat věčně.

<!-- S78 -->
Což nás vrací
k té mrtvé obrazovce.
Kliknutí nikdy nebylo jednou událostí.

<!-- S79 -->
Hardware ho musí ohlásit.
Jádro ho musí uložit.
Fronta se musí dostat k programu.

<!-- S80 -->
Program musí dostat procesor.
Rozhraní se musí změnit.
Někdo musí vykreslit nový obraz
a obrazovka ti ho musí ukázat.

<!-- S81 -->
Každý z těch kroků
je malý a rychlý.

<!-- S82 -->
Stačí zdržet kterýkoli z nich
a nebudeš mít pocit
pomalého okna.

<!-- S83 -->
Budeš mít pocit mrtvého počítače.

<!-- S84 -->
A nejpodivnější na tom celém je,
jak vzácně
se to vlastně stává.

<!-- S85 -->
Čekáme od stroje,
který dělá miliardy operací
za sekundu,
že odpoví na cuknutí ruky.

<!-- S86 -->
A skoro vždycky odpoví.

<!-- S87 -->
Takže až příště klikneš
a nic se nestane,
dej mu chvilku.

<!-- S88 -->
Slyšel tě.

<!-- S89 -->
Jen měl frontu
a ty jsi v ní stál.
