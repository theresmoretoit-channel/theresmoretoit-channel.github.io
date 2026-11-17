<!-- S01 -->
To je QR kód.
Nese jeden krátký řádek textu.

<!-- S02 -->
Telefon ho přečte hned.

<!-- S03 -->
Teď z něj kus utrhneme.

<!-- S04 -->
A naskenujeme ho znovu.
Stejný text.
Do posledního písmene.

<!-- S05 -->
Část kódu chybí.
Není špatně čitelná.
Chybí.

<!-- S06 -->
Jak tedy může telefon přečíst něco,
co už tam není?

<!-- S07 -->
Tady je tentýž problém, jen menší.
Někdo vám pošle osm bitů.
Cestou se tři z nich ztratí.

<!-- S08 -->
Každý chybějící bit je nula, nebo jednička,
takže mezery jde doplnit osmi způsoby.
A nic z toho, co dorazilo,
vám neřekne, který je správný.

<!-- S09 -->
A přesto to telefon právě udělal.
Nehádal.
Odpověď byla odeslána
dřív, než se cokoli ztratilo.

<!-- S10 -->
Trik je poslat víc
než samotnou zprávu.

<!-- S11 -->
Nejjednodušší způsob
je říct všechno třikrát.
Nula se pošle jako tři nuly,
jednička jako tři jedničky.

<!-- S12 -->
Šum jednu z nich překlopí
a vy dostanete jedna, nula, jedna.
Dva hlasy proti jednomu.
Skoro jistě to byla jednička.

<!-- S13 -->
Když šum překlopí jeden bit z deseti,
náhodně a nezávisle,
většina ze tří se splete
méně než třikrát ze sta.

<!-- S14 -->
Jenže jste ztrojnásobili
všechno, co posíláte.
Abyste se přiblížili dokonalosti,
opakovali byste pětkrát, pak devětkrát,
pak stokrát...
a zpráva by se jen plazila.

<!-- S15 -->
Dlouho
to vypadalo jako nevyhnutelná cena.
Méně chyb, pomalejší zprávy.
Zapamatujte si to.

<!-- S16 -->
Na konci 40. let
měl Richard Hamming v Bellových laboratořích
vlastní problém.

<!-- S17 -->
Reléový počítač
měl k dispozici hlavně o víkendech,
kdy na něj nikdo nedohlížel.

<!-- S18 -->
Stroj poznal,
když udělal chybu.
Zkusil krok znovu,
třikrát...
a pak jeho úlohu zahodil.
Dva víkendy po sobě
přišel o svou práci.

<!-- S20 -->
Jeho otázka, jeho vlastními slovy:
„Když stroj dokáže zjistit,
že je tam chyba,
proč nedokáže zjistit, kde je?“
Jak sám přiznal, ve skutečnosti
použil nejspíš ostřejší slova.

<!-- S22 -->
Jeho odpověď vezme čtyři bity zprávy
a přidá tři kontrolní bity.
Celkem sedm bitů.

<!-- S23 -->
Každý kontrolní bit hlídá
jinou skupinu pozic
a zajistí, aby ta skupina
měla sudý počet jedniček.

<!-- S24 -->
Skupiny se překrývají podle promyšleného vzoru.
Každá pozice patří
do vlastní kombinace skupin.

<!-- S25 -->
Teď překlopme jeden bit.
Třeba ten na pozici šest.

<!-- S26 -->
Příjemce znovu provede tři kontroly.
První projde.
Druhá neprojde.
Třetí neprojde.

<!-- S27 -->
Zapište neúspěšnou kontrolu jako jedničku,
úspěšnou jako nulu
a čtěte je od poslední k první.
Jedna, jedna, nula.
Ve dvojkové soustavě je to šest.

<!-- S28 -->
Kontroly neřeknou jen to,
že se něco pokazilo.
Ukážou přesně na ten bit.

<!-- S29 -->
Překlopte ho zpátky
a zpráva je zase celá.
Nikdo nemusel nic posílat dvakrát.

<!-- S30 -->
Tak tohle je odpověď.
Příjemce neobnovuje
ztracenou informaci z ničeho.
Odesílatel ji tam přibalil
předem.

<!-- S32 -->
Tohle nedokáže každá kontrola.
Kontrolní součet, jako ten z našeho videa
o Btrfs,
vám řekne, který blok je poškozený,
ale ne, jaká v něm byla původní data.

<!-- S33 -->
A existuje i druhý druh poškození.
Někdy bit není špatně.
Prostě chybí
a vy přesně víte, kde je mezera.

<!-- S34 -->
Tomu se říká výmaz
a výmazy jsou snazší.

<!-- S35 -->
Pošlete čtyři čísla,
4, 7, 2 a 9,
a k nim páté:
jejich součet, 22.

<!-- S36 -->
Když kterékoli z nich chybí,
ostatní vám řeknou, jaké bylo.
4, 7, něco, 9,
22.
Musí to být dvojka.

<!-- S37 -->
Servery chrání své disky
podobným druhem kontroly,
rozprostřeným po všech discích.
Když jeden disk odejde,
jeho obsah se dopočítá ze zbytku.

<!-- S38 -->
Kolik toho tedy musíte přidat?
Opakování říká:
chcete-li chyby srazit na nulu,
musíte zpomalit na nulu.

<!-- S39 -->
Dva roky předtím, než Hammingův článek
vyšel,
publikoval jeho kolega Claude Shannon
podivnější odpověď.

<!-- S40 -->
Každý kanál,
rádiové spojení, kabel, disk,
má svůj limit.
Nejvyšší rychlost přenosu informace.

<!-- S41 -->
Pod tím limitem
můžou být chyby tak vzácné, jak chcete,
aniž byste zpomalili.
Ne tím, že budete víc opakovat.
Ale chytřejším kódováním.

<!-- S42 -->
Nad ním
nepomůže žádný kód na světě.

<!-- S43 -->
Mělo to ale háček.
Shannon dokázal, že takové kódy existují.
Neukázal ale, jak sestrojit takový,
který by kdokoli mohl použít.

<!-- S44 -->
Podle jeho důkazu by náhodně zvolený kód
byl skoro jistě dobrý.
Jenže přímočaré dekódování
znamená porovnat to, co dorazilo,
s každou možnou zprávou...
a pro blok o 1 000 bitech
je jich víc
než atomů ve vesmíru.

<!-- S46 -->
Shannonův článek tedy nebyl řešení.
Byl to slib.
A inženýři pak strávili dalších
45 let snahou ho splnit.

<!-- S47 -->
Hammingův kód byl první krok.
Opraví jeden špatný bit ze sedmi.

<!-- S48 -->
Jenže skutečné poškození přichází ve shlucích.
Škrábanec nebo náhlé zapraskání
vyřadí stovky bitů za sebou.

<!-- S49 -->
V roce 1960 Irving Reed a Gustave Solomon
z Lincolnovy laboratoře MIT
publikovali článek dlouhý pět stran.

<!-- S50 -->
Jejich kódy pracují s celými bajty,
ne s jednotlivými bity.
Když shluk zničí všech osm bitů
jednoho bajtu,
je to pořád jen jeden špatný bajt.

<!-- S51 -->
Jedna běžná verze přidá
32 kontrolních bajtů
ke 223
bajtům dat.

<!-- S52 -->
Dokáže opravit libovolných 16 bajtů,
které dorazí špatně...
nebo obnovit 32,
které nedorazí vůbec.

<!-- S53 -->
Proto CD hraje i přes škrábanec.
Jeho dva Reedovy-Solomonovy kódy
dokážou úplně zacelit výpadek
o délce zhruba 4 000 bitů,
tedy 2,5 milimetru stopy.

<!-- S54 -->
A proto roztržený QR kód
pořád fungoval.
V nejsilnějším nastavení
dokáže QR kód obnovit
až zhruba 30 % svých bajtů
a přesto vrátit každé písmeno.

<!-- S56 -->
Voyager 2 opustil Zemi v roce 1977
s Reedovým-Solomonovým kodérem na palubě.

<!-- S57 -->
U Jupiteru a Saturnu
ale chránil všechno kromě snímků
starším kódem od Marcela Golaye,
který posílal jeden bit navíc
za každý bit dat.

<!-- S58 -->
Pro Uran a Neptun,
kde signál slábl,
inženýři zapnuli Reedův-Solomonův kód,
jako vrstvu nad druhým kódem,
kterým už procházel každý bit.

<!-- S59 -->
Se samotným druhým kódem
bylo pořád špatně
asi pět bitů z tisíce.
S Reedovým-Solomonovým kódem navrch
asi jeden z milionu.

<!-- S60 -->
I šum přichází ve shlucích,
takže Voyager promíchal
bajty čtyř bloků dohromady,
než je odeslal.

<!-- S61 -->
Shluk, který by zničil jeden blok,
teď vezme pár bajtů z každého...
tak málo, že každý blok
se dokáže opravit sám.

<!-- S62 -->
Zbytek cesty snímků Neptunu
domů
najdete v našem videu o Voyageru.

<!-- S63 -->
Ale ani tohle
pořád nedosahovalo Shannonova limitu...
a kód, který se mohl dostat mnohem blíž,
už existoval.

<!-- S65 -->
V roce 1960 popsal ve své disertaci na MIT
Robert Gallager kódy
složené z mnoha jednoduchých kontrol,
z nichž každá hlídá jen pár bitů.

<!-- S66 -->
Dekódování znamenalo, že si kontroly
předávají odhady tam a zpět,
kolo za kolem...
což bylo příliš
na počítače 60. let.
Nápad tedy skončil v šuplíku
a na 30 let se na něj skoro zapomnělo.

<!-- S68 -->
V roce 1993
představil tým vedený dvěma francouzskými inženýry,
Claudem Berrouem a Alainem Glavieuxem,
turbo kódy
na konferenci v Ženevě.

<!-- S69 -->
Jejich výsledky byly tak blízko
Shannonovu limitu,
že mnoho odborníků předpokládalo,
že se spletli.
Nejspíš o dvojnásobek,
někde ve výpočtech.

<!-- S70 -->
Do roka
to potvrdily další laboratoře.

<!-- S71 -->
I turbo kódy fungovaly
předáváním odhadů tam a zpět
a to lidi přivedlo zpátky ke Gallagerovi.

<!-- S72 -->
V letech 1995 a 1996
David MacKay a Radford Neal
jeho kódy znovu objevili
a ukázali, že se dokážou dostat
stejně blízko.

<!-- S73 -->
V roce 2001
se vylepšená verze Gallagerových kódů
dostala na 0,04 decibelu
od Shannonova limitu.

<!-- S74 -->
To je o méně než 1 %
vyšší výkon signálu
než teoretické minimum.
Slib z roku 1948 byl splněn.

<!-- S75 -->
Dnes Gallagerovy kódy přenášejí
velkou část dat v telefonech 5G,
v moderní Wi-Fi
a v satelitní televizi.

<!-- S77 -->
A teď zpátky k našim osmi bitům.
Tři se ztratily
a mezery jde doplnit
osmi způsoby.

<!-- S78 -->
Jenže těch osm bitů
nikdy nebylo jen zpráva.
Neslo čtyři bity dat,
tři Hammingovy kontroly
a ještě jednu kontrolu přes všech osm.

<!-- S79 -->
Ze všech 256
možných kombinací osmi bitů
dodržuje tahle pravidla jen 16.

<!-- S80 -->
Vyzkoušejte osm kandidátů.
Jeden po druhém neprojdou.
Zbude jediný.

<!-- S81 -->
Chybějící bity nikdy doopravdy nezmizely.
Jejich informace tam pořád byla,
v bitech, které přežily.

<!-- S82 -->
A teď otázka pro vás.
Všimli jste si někdy opravy chyb
u něčeho, co používáte každý den?
Napište mi to do komentářů.
