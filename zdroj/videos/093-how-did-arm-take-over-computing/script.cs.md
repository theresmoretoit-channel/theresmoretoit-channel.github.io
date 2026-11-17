# Jak ARM ovládl výpočetní techniku?

<!-- S01 -->
V roce 1985 inženýři v Británii
zapnuli zbrusu nový procesor
úplně poprvé.

<!-- S02 -->
Fungoval.
Což už samo o sobě byl malý zázrak.

<!-- S03 -->
Pak si ale všimli něčeho zvláštního.
Napájení čipu
nebylo zapojené.

<!-- S04 -->
A přesto běžel.

<!-- S05 -->
Vystačil si s nepatrnými proudy,
které do něj prosakovaly vstupními piny
ze signálů okolních čipů.

<!-- S06 -->
Když ho pořádně změřili,
procesor potřeboval
zhruba desetinu wattu.

<!-- S07 -->
O to se přitom nikdo nesnažil.
Inženýři prostě chtěli čip,
jehož výroba bude levná.

<!-- S08 -->
Ten čip byl první procesor ARM.

<!-- S09 -->
O čtyřicet let později jsou jeho potomci
skoro v každém chytrém telefonu.
V počítačích Applu.
V některých z největších datových center
na světě.

<!-- S10 -->
Stovky miliard čipů.

<!-- S11 -->
Jak tedy procesor
od britské firmy na domácí počítače
ovládl výpočetní techniku?

<!-- S12 -->
Odpověď nezní jednoduše tak,
že měl velmi malou spotřebu.
Ta byla skoro náhoda.

<!-- S12b -->
Mimochodem, jestli se ti takováhle
videa líbí, můžeš se přihlásit k odběru.

Kanálu to opravdu pomůže.

<!-- S13 -->
Abychom pochopili, co se doopravdy stalo,
musíme se vrátit do roku 1983.

<!-- S14 -->
Ta firma se jmenovala Acorn Computers.
Její BBC Micro stál ve třídách
po celé Británii.

<!-- S15 -->
BBC Micro běžel na starším
osmibitovém čipu 6502.
Pro svůj další stroj
potřeboval Acorn něco mnohem rychlejšího.

<!-- S16 -->
Tým tedy vyzkoušel
nové procesory na trhu.
Žádný nedělal, co Acorn chtěl.

<!-- S17 -->
Byly složité
a žádný doopravdy neseděl k tomu,
co chtěl Acorn postavit.

<!-- S18 -->
Pak dva inženýři Acornu,
Sophie Wilsonová a Steve Furber,
odjeli do Arizony,
do firmy, kterou založil jeden
z původních konstruktérů čipu 6502.

<!-- S19 -->
Čekali velkou čipovou firmu.
Místo toho našli hrstku lidí,
kteří pracovali z domku na předměstí.

<!-- S20 -->
A domů se vrátili
s prostým závěrem.
Když dokážou navrhnout procesor oni...
dokážeme to i my.

<!-- S22 -->
Procesory tehdy dostávaly
čím dál propracovanější instrukce.

<!-- S23 -->
Jediná instrukce dokázala načíst
číslo z paměti,
provést s ním výpočet
a zapsat výsledek zpátky.

<!-- S24 -->
Pro programátora pohodlné.
Jenže každá taková instrukce
ztěžuje stavbu čipu.

<!-- S25 -->
Čip potřebuje víc logiky
jen na to, aby zjistil, co která znamená.
Víc tranzistorů.
Víc času na návrh.

<!-- S26 -->
Výzkumníci z Berkeley a Stanfordu
si položili radikální otázku.

<!-- S27 -->
Co kdyby procesor
měl jen jednoduché instrukce
a zbytek obstaral překladač?

<!-- S28 -->
Říkali tomu RISC.
Počítač s redukovanou instrukční sadou.

<!-- S29 -->
Sophie Wilsonová navrhla
instrukce ARM v tomhle duchu.

<!-- S30 -->
Aritmetika pracuje jen
s vlastními registry čipu,
malými rychlými přihrádkami uvnitř procesoru.
Pro práci s pamětí má zvláštní instrukce.

<!-- S31 -->
Přičíst číslo z paměti
tak znamená tři kroky.
Načíst.
Sečíst.
Uložit.

<!-- S32 -->
Říká se tomu architektura load-store.

<!-- S33 -->
Pro program víc kroků.
Každý krok má ale stejnou podobu,
předvídatelný
a snadno se dekóduje.

<!-- S34 -->
A ARM měl spoustu registrů,
se kterými mohl pracovat.
Šestnáct, každý široký 32 bitů.
6502 měl tři malé.

<!-- S35 -->
Výsledkem byl ARM1.

<!-- S36 -->
Měl zhruba
25 000 tranzistorů.

<!-- S37 -->
Intel 286, uvedený o pár let dřív,
jich měl zhruba 134 000.

<!-- S38 -->
Méně tranzistorů znamenalo menší čip.
Levnější čip.

<!-- S39 -->
A skoro jako vedlejší účinek
čip, který nespotřeboval skoro nic.

<!-- S40 -->
Odtud se vzala
ta desetina wattu.
Acorn chtěl levné plastové pouzdro,
a to znamenalo zůstat pod jedním wattem.
Navrhovali tedy pečlivě...
a skončili desetkrát níž.

<!-- S41 -->
V roce 1987 se rychlejší verze ARM
dostala do nového počítače Acornu
jménem Archimedes.

<!-- S42 -->
Byl to jeden z nejrychlejších
osobních počítačů své doby.

<!-- S43 -->
A skoro na tom nezáleželo.

<!-- S44 -->
Svět kupoval PC kompatibilní s IBM
s procesory Intel.
Tam byly programy.
To kupovaly firmy.

<!-- S45 -->
Archimedes zůstal
hlavně v britských školách.

<!-- S46 -->
A samotný Acorn měl potíže.
Zachraňovat ho musela
už v roce 1985 firma Olivetti.

<!-- S48 -->
Pak přišla pomoc od Applu.
Ten stavěl kapesní počítač
jménem Newton.

<!-- S49 -->
Potřeboval procesor,
který bude rychlý, levný
a zvládne běžet na baterie.

<!-- S50 -->
ARM se hodil dokonale.
Apple ale nechtěl záviset
na čipu, který patří
konkurenčnímu výrobci počítačů.

<!-- S51 -->
V roce 1990 se proto tým ARM
oddělil od Acornu
do samostatné firmy.

<!-- S52 -->
Acorn, Apple
a výrobce čipů VLSI
ji vlastnili společně.

<!-- S53 -->
Dvanáct inženýrů.
Stará stodola u Cambridge.

<!-- S54 -->
A obchodní model,
který se ukázal jako skutečné tajemství úspěchu.

<!-- S55 -->
Intel své procesory navrhoval,
vyráběl ve vlastních továrnách
a prodával.

<!-- S56 -->
ARM neměl vyrábět vůbec nic.
Měl prodávat návrh.

<!-- S57 -->
Kterákoli firma si ho mohla licencovat,
zabudovat jádro ARM do vlastního čipu
a platit malý poplatek
z každého prodaného čipu.

<!-- S58 -->
To bylo důležité,
protože čip nemusí být
jen procesor.
Kolem jádra ARM
můžeš dát rádio,
grafiku,
procesor pro fotoaparát.

<!-- S59 -->
Jeden čip,
navržený tím, kdo ho potřebuje,
a ARM uprostřed.

<!-- S60 -->
ARM nemusel porazit Intel
v osobních počítačích.
Mohl skončit uvnitř čehokoli.

<!-- S61 -->
A v 90. letech
„cokoli“ čím dál častěji znamenalo
mobilní telefony.

<!-- S62 -->
Stolní počítač si může dovolit
sto wattů a velký větrák.
Telefon běží na baterii
v kapse.

<!-- S63 -->
Koncem desetiletí
byla jádra ARM
v některých z nejprodávanějších telefonů
od Nokie i dalších.

<!-- S64 -->
Pak přišel iPod.
Pak chytrý telefon.

<!-- S65 -->
Miliardy lidí najednou nosily
počítač, který musel vydržet
celý den na baterii.

<!-- S66 -->
A procesor, který vznikl proto,
že byl levný,
se ukázal být přesně tím,
co ten svět potřeboval.

<!-- S67 -->
Takže tohle je naše odpověď, ne?
ARM je jednoduchý,
jednoduchý znamená efektivní
a efektivní vyhrává.

<!-- S68 -->
Tak docela ne.

<!-- S69 -->
Podívej se do moderního výkonného jádra ARM.

<!-- S70 -->
Obrovské cache.
Několik instrukcí najednou.
Predikce větvení,
tedy odhad, kudy se program vydá,
dřív, než tam dojde.

<!-- S71 -->
Provádění mimo pořadí,
kdy instrukce běží
v tom pořadí, které je nejrychlejší.

<!-- S72 -->
Miliardy tranzistorů na čipu.
Nic na tom není jednoduché.

<!-- S73 -->
Kam se tedy poděla ta jednoduchost?

<!-- S74 -->
Háček je v tom, že procesor
jsou ve skutečnosti dvě různé věci.

<!-- S75 -->
Instrukční sada je jazyk,
kterým mluví software.
Které instrukce existují
a co znamenají.

<!-- S76 -->
Mikroarchitektura je stroj,
který je skutečně provádí.

<!-- S77 -->
Jazyk může zůstat jednoduchý,
zatímco stroj pod ním
je nesmírně složitý.

<!-- S78 -->
A totéž se stalo
i na druhé straně.

<!-- S79 -->
Instrukce x86 od Intelu
jsou proslule složité.

<!-- S80 -->
Jenže od poloviny 90. let
je procesory Intel a AMD
uvnitř rozkládají
na malé, jednoduché operace.

<!-- S81 -->
Ty pak provádějí na stroji,
který se hodně podobá tomu
v moderním jádře ARM.

<!-- S82 -->
Navzdory jiným jménům
jsou si uvnitř překvapivě podobné.

<!-- S83 -->
Čistší instrukce ARM pořád pomáhají.
Snáz se dekódují,
což může ušetřit trochu energie.

<!-- S84 -->
Nedávají ale ARM kouzelný náskok,
kterou by x86 nikdy nedohnalo.

<!-- S85 -->
ARM tedy nezvítězil proto,
že byl jednoduchý.
A nebyl navržený pro nízkou spotřebu.

<!-- S86 -->
Vyhrál, protože se sešly tři věci.
Efektivní návrh.
Obchodní model,
který komukoli dovolil na ARM stavět.
A svět, který najednou potřeboval
miliardy počítačů na baterie.

<!-- S87 -->
A pak, v roce 2020,
se příběh vrátil k Applu.

<!-- S88 -->
Apple svůj podíl v ARM prodal
už před lety,
když nutně potřeboval peníze.

<!-- S89 -->
Teď dal vlastní čipy postavené na ARM
do Macu.

<!-- S90 -->
Stejný druh jader jako v iPhonu,
jen ve větším měřítku pro počítač.
Rychlá jádra, úsporná jádra,
grafika a mnohem víc,
v jediném čipu.

<!-- S91 -->
Byly rychlejší
než čipy Intel, které nahradily,
a notebooky vydržely mnohem déle
na jedno nabití.

<!-- S92 -->
ARM už nebyl
jen procesor do telefonů.

<!-- S93 -->
A ARM u toho nezůstal.
Pronikl i do datových center,
kde každý watt stojí peníze.
Amazon dnes navrhuje
vlastní serverové čipy ARM.

<!-- S95 -->
První čip ARM měl zhruba
25 000 tranzistorů.
Dnešní jich mají miliardy.

<!-- S96 -->
Skoro všechno na tom,
jak uvnitř fungují, se změnilo.

<!-- S98 -->
Malý tým chtěl
procesor, který dokáže opravdu postavit.

<!-- S99 -->
Nepostavili ho pro telefony,
pro Apple
ani proto, aby porazili Intel.

<!-- S100 -->
A nakonec
to nejdůležitější, co vytvořili,
nebyl čip.

<!-- S101 -->
Byl to jednoduchý základ,
na kterém mohli stavět všichni ostatní.
