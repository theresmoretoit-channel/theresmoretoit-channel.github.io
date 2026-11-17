<!-- S01 -->
Tady jsou všechny scénáře,
které kdy pro tenhle kanál vznikly.
158 videí,
skoro milion a půl bajtů textu.

<!-- S02 -->
Prožeňte je obyčejným kompresorem
jménem gzip.
Vyjde z toho něco přes půl megabajtu.
Skoro dvě třetiny pryč.

<!-- S03 -->
A nic se neztratilo.
Rozbalte soubor
a každý scénář se vrátí,
písmeno po písmenu.

<!-- S04 -->
Teď ho zkomprimujte znovu.

<!-- S05 -->
Zvětší se.
O 98 bajtů.

<!-- S06 -->
Potřetí.
O 98 bajtů větší.
Počtvrté.
Zase 98.

<!-- S07 -->
První kolo zahodí dvě třetiny.
Druhé nenajde vůbec nic.
Proč tedy nemůžeme komprimovat pořád dál?

<!-- S08 -->
Podívejme se do toho druhého souboru.
gzip nic nezkomprimoval.
Data jen beze změny zkopíroval,
v šestnácti blocích.

<!-- S09 -->
Každý blok dostal pětibajtový štítek.
Přidejte malou hlavičku a patičku
a vyjde přesně 98.

<!-- S10 -->
Když kompresor nenajde nic, co by odstranil,
uloží data tak, jak jsou,
a přidá jen to, co potřebuje k jejich rozbalení.

<!-- S11 -->
Proč tedy druhé kolo nic nenašlo?
A našel by něco chytřejší program?

<!-- S12 -->
Takový text je plný opakování.
Stejná slova, stejná slovní spojení,
tytéž drobné značky
na začátku každé scény.

<!-- S13 -->
V roce 1977 zveřejnili Jacob Ziv a Abraham Lempel
jednoduchý trik.
Opakování nepište znovu.
Odkažte zpátky tam, kde už bylo.

<!-- S14 -->
Vraťte se o 300 znaků
a zkopírujte dalších dvanáct.
Pár bajtů místo dvanácti.

<!-- S15 -->
Druhý trik:
častým písmenům dát krátké kódy
a vzácným dlouhé.

<!-- S16 -->
V roce 1951 si David Huffman,
postgraduální student na MIT,
mohl vybrat: závěrečná zkouška,
nebo místo ní seminární práce.

<!-- S17 -->
Práce, kterou zadal Robert Fano,
měla najít nejúspornější kód
přesně tohoto druhu.

<!-- S18 -->
Huffman se celé měsíce nikam nedostal.
Vzdal to
a začal se učit na zkoušku.
A pak ho to napadlo.

<!-- S19 -->
Vezměte dva nejvzácnější symboly,
spojte je v jeden
a opakujte, dokud nezbude jediný strom.

<!-- S20 -->
Později to nazval
„nejvýjimečnějším okamžikem svého života“.

<!-- S21 -->
Fano studentům neřekl,
že si s tím sám lámal hlavu,
a Claude Shannon taky.

<!-- S22 -->
Huffmanův kód porazil metody obou.
A dá se dokázat,
že žádný kód tohoto druhu není lepší.

<!-- S23 -->
Na začátku 90. let
spojil Phil Katz oba triky
ve formátu ZIP.
gzip používá tutéž metodu.

<!-- S24 -->
První kolo už vyčerpalo
pravidelnosti, které gzip umí najít.

<!-- S25 -->
Ve zbytku nemá s čím pracovat.
Pro gzip to vypadá jako šum.

<!-- S26 -->
Jenže chytřejší program
by mohl vidět pravidelnosti, které gzip přehlédl.
Mohl by jednou nějaký program
zmenšit cokoli, co mu dáte?

<!-- S27 -->
Ne.
A nemusíte vědět, jak funguje,
abyste si tím byli jistí.

<!-- S28 -->
Vezměte všechny soubory
dlouhé přesně tři bity.
Je jich osm.

<!-- S29 -->
Teď spočítejte všechny kratší.
Čtyři soubory po dvou bitech,
dva po jednom bitu
a jeden prázdný soubor.

<!-- S30 -->
Sedm.

<!-- S30b -->
Osm souborů a sedm kratších míst,
kam je dát.

<!-- S31 -->
Kdyby se zkrátil každý z nich,
dva by se musely dělit o jedno místo.
A až ho rozbalíte,
který z nich to měl být?

<!-- S32 -->
Říká se tomu Dirichletův princip
a platí pro jakoukoli délku.
Kratších souborů je vždycky o jeden méně,
než kolik je potřeba.

<!-- S33 -->
Takže každý kompresor, který vezme jakýkoli soubor
a některé zmenší,
musí jiné zvětšit.
Ne proto, že je špatně napsaný.
Prostě nemají kam jinam jít.

<!-- S34 -->
Těch 98 bajtů
je cena, kterou za to platí gzip.

<!-- S35 -->
Vezměte si jakýkoli kompresor.
Ze všech souborů dané velikosti
zmenší o jediný bajt méně než jeden
ze 250.

<!-- S36 -->
Komprese přesto funguje,
protože soubory, které vytváříme, nejsou náhodné.
Jsou to texty, obrázky a programy,
plné pravidelností.

<!-- S37 -->
To lidem nezabránilo
slibovat víc.

<!-- S38 -->
V roce 1992 ohlásila firma WEB Technologies
software, který prý stlačí
skoro jakákoli data pod kilobajt.
I svůj vlastní výstup,
znovu a znovu.

<!-- S39 -->
Její viceprezident prohlásil, že metoda
„nepodléhá zákonům
teorie informace“.
Produkt nikdy nevyšel.

<!-- S40 -->
Jak to tedy, že se fotky a hudba
tolik zmenší?
Tohle pravidlo pro ně vůbec neplatí.

<!-- S41 -->
JPEG se nevrátí stejný.
Vrátí se dost podobný.
Detaily, které oku chybět nebudou,
se zahodí natrvalo.

<!-- S42 -->
Přibližte si to
a uvidíte, kam se poděly.

<!-- S43 -->
To je ztrátová komprese
a to je jiná hra.
Tohle video je o tom druhém druhu.
Každý bit zpátky, beze změny.

<!-- S44 -->
A u souborů, které pravidelnosti mají:
jak malé můžou být?
Existuje nějaké dno?

<!-- S45 -->
Existuje.
Našlo se v roce 1948,
ve stejném článku, o kterém je naše video
o samoopravných kódech.

<!-- S46 -->
Tam Claude Shannon ukázal,
jak přidaná redundance chrání zprávu.
Tady spočítal,
kolik se jí dá ubrat.

<!-- S47 -->
Jeho odpovědí bylo číslo,
kterému říkal entropie:
jak těžké je uhodnout,
co přijde dál.

<!-- S48 -->
Žádný bezeztrátový kód se pod to číslo nedostane,
v průměru.
Ale přiblížit se mu dá
libovolně blízko.

<!-- S49 -->
Jak nepředvídatelná je tedy angličtina?
V roce 1951 to Shannon změřil
hrou.

<!-- S50 -->
Dal člověku úryvek,
který nikdy neviděl,
a nechal ho, ať ho hádá,
písmeno po písmenu.

<!-- S51 -->
Když se spletl,
hádal znovu,
dokud se netrefil.

<!-- S52 -->
Ukázalo se, že lidé jsou v tom velmi dobří.
Se stovkou písmen kontextu
vyšla angličtina zhruba na jeden bit
na písmeno.

<!-- S53 -->
Počítač ukládá každé písmeno
do osmi bitů.
Lidskému čtenáři stačí zhruba jeden.

<!-- S54 -->
Právě v tomhle rozdílu má komprese prostor.
gzip dostal scénáře kanálu
pod tři bity na znak.

<!-- S55 -->
Jak blízko k jednomu bitu
se tedy dostane stroj?

<!-- S56 -->
Přesně na to je vypsaná cena.
Jmenuje se Hutter Prize
a od roku 2020 se soutěží na jediném souboru:
gigabajt anglické Wikipedie.

<!-- S57 -->
gzip ho zmenší na třetinu.
Nejlepší běžné kompresory
zhruba na pětinu.

<!-- S58 -->
Rekord z července 2026
je něco přes sto milionů bajtů.
Desetina.

<!-- S59 -->
A počítá se i dekompresor.
Jeho velikost se přičítá k výsledku,
takže Wikipedii nejde schovat
do programu.

<!-- S60 -->
Fond má 500 000 eur.
Každé procento zlepšení
vynese pět tisíc.

<!-- S61 -->
Marcus Hutter, který cenu financuje, vysvětluje proč:
„umět dobře komprimovat
úzce souvisí
s inteligentním jednáním.“

<!-- S62 -->
Protože programy na špici
nehledají opakování.
Předpovídají.

<!-- S63 -->
Před každým znakem
odhadnou, jak pravděpodobný je
každý možný další znak.
Dobrý odhad stojí zlomek bitu.

<!-- S64 -->
Je to Shannonova hádací hra,
kterou hraje stroj.
Nejlepší hráči dnes používají neuronové sítě,
naučené předpovídat, co přijde dál.

<!-- S65 -->
Funguje to i na už zkomprimovaných souborech.
V roce 2016 začal Dropbox přebalovat
JPEGy svých uživatelů lepším prediktorem.
V průměru o víc než pětinu menší.

<!-- S66 -->
Každý soubor se vrátil bit po bitu
a do roku 2017
to ušetřilo přes 46 petabajtů.
To je přes 46 000 terabajtů.

<!-- S67 -->
A pak jsou tu obři.
V roce 2023 použili vědci z DeepMind
velký jazykový model
jako kompresor.

<!-- S68 -->
Na malých výřezech fotek ve stupních šedi
porazil PNG:
48 % původní velikosti
proti 58.

<!-- S69 -->
Na nahrávkách předčítané řeči
porazil FLAC:
21 % proti 30.

<!-- S70 -->
Jenže to je bez započtení modelu.
Přičtěte jeho velikost
a výsledek vyjde
140krát
větší než data.

<!-- S71 -->
Kompresor větší než jeho data
nic neušetřil.
Program je součástí popisu.

<!-- S72 -->
A tím se dostáváme k nejpodivnější části.
Tady je první milion číslic čísla π.

<!-- S73 -->
Dejte je čtyřem kompresorům.
Nejlepší je dostane zhruba
na 426 000 bajtů.

<!-- S74 -->
Teď dejte týmž kompresorům
milion náhodných číslic.
Stejný výsledek,
s rozdílem do desetiny procenta.

<!-- S75 -->
Jenže π nevzniká náhodou.
Řídí se matematickým pravidlem.
Tady je program, který vypíše
každou z toho milionu číslic.

<!-- S76 -->
362 bajtů.
Víc než dvatisíckrát kratší než ten soubor.

<!-- S77 -->
Kompresory neviděly
matematické pravidlo, ze kterého π vychází.
Viděly jen číslice.

<!-- S78 -->
Jeden způsob, jak změřit informaci
v datech, je zeptat se:
jak krátký může být program,
který je ještě vypíše?

<!-- S79 -->
Té délce se říká
Kolmogorovova složitost,
podle jednoho z těch, kdo ji popsali.

<!-- S80 -->
Většina dat žádný krátký program nemá.
Je to zase Dirichletův princip:
krátkých programů prostě
není dost.

<!-- S81 -->
Milion náhodných číslic
nejspíš nic kratšího nemá.
π ano.

<!-- S82 -->
Proč tedy prostě nenajít
nejkratší program pro jakýkoli soubor?
Protože je dokázané,
že žádný algoritmus to nedokáže
pro každý soubor.

<!-- S83 -->
Každý program vám dá horní mez.
Ale nic vám nedokáže vždycky říct,
jestli existuje kratší.
Nikdy nevíte, že jste dosáhli dna.

<!-- S84 -->
gzip našel ve scénářích opakování
a nic víc.
Vidí bajty,
ne to, co slova znamenají.

<!-- S85 -->
Aby se program dostal dál,
musí je líp předpovídat.
A dobře předpovídat text
začíná vypadat hodně jako porozumění.

<!-- S86 -->
Takže otázka pro vás.
Kdyby program dokázal stlačit Wikipedii
víc než kterýkoli jiný program,
řekli byste, že jí rozumí?
Napište odpověď do komentářů.
