<!-- S01 -->
V roce 1993 běžela hra jménem Doom
na počítači
se 4 megabajty paměti.

<!-- S02 -->
To je zhruba velikost
jedné fotky v tvém telefonu.

<!-- S03 -->
Žádný 3D akcelerátor nebyl.
Veškeré vykreslování
obstarával hlavní procesor.

<!-- S04 -->
Dnes vývojář začíná s enginem,
třeba Unity nebo Unreal,
který se postará o grafiku, zvuk,
paměť a hardware.

<!-- S05 -->
V DOSu bylo tohle všechno
starostí vývojáře.
A dost často i hráče.

<!-- S06 -->
Jak těžké tedy bylo
udělat hru pro DOS?

<!-- S07 -->
Začněme pamětí,
protože s pamětí byl zmatek.

<!-- S08 -->
Původní IBM PC z roku 1981
dokázalo adresovat 1 megabajt paměti.

<!-- S09 -->
Jenže jen prvních
640 kilobajtů
bylo určeno pro programy.

<!-- S10 -->
Zbylých 384 kilobajtů
bylo vyhrazeno pro videopaměť,
rozšiřující karty a BIOS.

<!-- S11 -->
Víc než deset let
DOS běžně spouštěl programy
uvnitř tohoto prostoru.
Cokoli nad ním stálo práci navíc.

<!-- S12 -->
Odtud pochází slavná věta:
640 K by mělo stačit každému.

<!-- S13 -->
Obvykle se připisuje Billu Gatesovi.
Neexistuje záznam, že by ji kdy řekl,
a on to popírá.

<!-- S14 -->
Na začátku devadesátých let
měl počítač 4 megabajty,
nebo 8.

<!-- S15 -->
A hra se přesto mohla zastavit
s hláškou
„nedostatek paměti“.

<!-- S16 -->
Mít paměť
a umět ji využít
byly dvě různé věci.

<!-- S17 -->
Jednou cestou byla expandovaná paměť,
neboli EMS.

<!-- S18 -->
Okno o velikosti 64 kilobajtů
leželo v horní části
toho prvního megabajtu.
Program jím viděl
4 stránky paměti navíc,
každou po 16 kilobajtech,

<!-- S19 -->
a mohl je vyměňovat za jiné,
jako když listuješ knihou
skrz díru v listu papíru.

<!-- S20 -->
Další cestou byla rozšířená paměť,
dostupná přes ovladač jménem HIMEM.

<!-- S21 -->
A tady se
problém vývojáře
stal problémem hráče.

<!-- S22 -->
Ovladače myši, mechaniky CD
nebo zvukové karty
ukusovaly z té vzácné paměti,
pokud se ti je nepovedlo načíst do horní paměti.

<!-- S23 -->
Hráči se tak naučili upravovat dva soubory,
CONFIG.SYS a AUTOEXEC.BAT.

<!-- S24 -->
Jedna hra chtěla EMS.
Jiná ji chtěla vypnutou,
nastavením jménem NOEMS.
A třetí potřebovala každý volný kilobajt.

<!-- S25 -->
V roce 1993 přidal MS-DOS 6
nabídku při startu.

<!-- S26 -->
Vybral sis konfiguraci
pro hru, kterou jsi chtěl hrát,
a počítač nastartoval přesně pro ni.

<!-- S27 -->
Někteří lidé nakonec měli
samostatnou položku
skoro pro každou hru, kterou vlastnili.

<!-- S28 -->
Jenže v té době
už větší hry našly
cestu, jak obejít limity DOSu.

<!-- S29 -->
Od procesoru 386
uměl sám procesor běžet
ve 32bitovém chráněném režimu,
s prostorem až pro 4 gigabajty.

<!-- S30 -->
Chráněný režim jsme probírali
v jednom z dřívějších videí.
DOS ho ale využít neuměl.

<!-- S31 -->
Hry si proto přinesly vlastního pomocníka,
DOS extender.
Nejznámější byl DOS/4GW.

<!-- S32 -->
Dodával se s oblíbeným překladačem
Watcom C.

<!-- S33 -->
Když se hra spustila,
DOS/4GW přepnul procesor
do chráněného režimu
a hra tak dostala přístup
k paměti nad limitem DOSu.

<!-- S34 -->
DOS pod hrou pořád běžel
a poskytoval služby, třeba přístup k souborům.
Jenže hra teď běžela v chráněném režimu,
ne jako klasický program pro DOS.

<!-- S35 -->
Jestli jsi v devadesátkách hrál hry pro DOS,
viděl jsi jeho jméno
mihnout se na obrazovce.

<!-- S37 -->
A teď obraz.
V jednom z nejpoužívanějších režimů VGA,
zvaném Mode 13h,
měla obrazovka 320
na 200 pixelů
a 256 barev.

<!-- S38 -->
Každý pixel byl jeden bajt.
Abys pixel obarvil,
zapsal jsi do paměti číslo.
Žádná grafická knihovna. Jen paměť.

<!-- S39 -->
Celá obrazovka zabrala
64 000 bajtů.

<!-- S40 -->
To je těsně pod 64 kilobajty,
takže se to vešlo do jednoho segmentu,
bloku, který 16bitový program
dokázal adresovat najednou.
Aspoň jednou hrála paměť ve tvůj prospěch.

<!-- S41 -->
Jenže když kreslíš rovnou
na viditelnou obrazovku,
hráč vidí rozpracované obrázky
a obraz bliká.

<!-- S42 -->
Hry proto každý snímek nejdřív kreslily
do skrytého bufferu
a hotový obraz pak zkopírovaly
do videopaměti.

<!-- S43 -->
V roce 1991 Michael Abrash,
programátor a autor,
zveřejnil lepší způsob.
Nazval ho Mode X.

<!-- S44 -->
Využíval část VGA,
na kterou většina programátorů
nikdy nesáhla.

<!-- S45 -->
Dával čtvercové pixely
a místo pro několik obrazovek
ve videopaměti.

<!-- S46 -->
Hra kreslila na obrazovku,
kterou nikdo neviděl,
a pak se na ni prostě přepnula.
Jenže programovalo se to mnohem hůř.

<!-- S47 -->
A pak tu byl zvuk.
A zvuk byla loterie.

<!-- S48 -->
Vestavěný reproduktor PC
byl stavěný na pípání.

<!-- S49 -->
Pak přišly zvukové karty
a další zvukový hardware.
Žádné dva kusy
nefungovaly stejně.

<!-- S50 -->
AdLib s čipem Yamaha,
který syntetizoval hudbu.
Sound Blaster, který uměl přehrát
i nahraný zvuk.

<!-- S51 -->
Roland MT-32,
drahá krabička s bohatšími nástroji.
Gravis UltraSound.

<!-- S52 -->
Podporovat je všechny
znamenalo psát různé ovladače.

<!-- S53 -->
A hra musela vědět,
kde karta je.
Její port, její IRQ
a její kanál DMA.

<!-- S54 -->
Obvyklá odpověď u Sound Blasteru
byla port 220, IRQ 7, DMA 1.
Obvykle.

<!-- S55 -->
Stačilo jedno splést
a hra byla němá.
Nebo zamrzla.

<!-- S56 -->
V roce 1991 programátor jménem John Miles
vydal knihovnu,
která mluvila s mnoha zvukovými kartami
přes jediné rozhraní.

<!-- S57 -->
Hra mohla napsat zvukový kód jednou
a obsluhu karty nechat na knihovně.

<!-- S58 -->
Byla to další vrstva
mezi hrou a hardwarem.
Tohle si zapamatuj.

<!-- S59 -->
A pak tu byla rychlost.
Programátoři počítali
každý krok, který procesor udělal.

<!-- S63 -->
Abys našel pixel na obrazovce,
vynásobíš jeho řádek
číslem 320.

<!-- S63b -->
Na starších procesorech
mohlo být násobení drahé.

<!-- S64 -->
Jenže 320
je 256
plus 64.
Obě jsou mocniny dvojky.

<!-- S65 -->
Násobení tak můžeš nahradit
dvěma bitovými posuny a sčítáním.

<!-- S67 -->
Chris Sawyer šel úplně na dřeň.
Transport Tycoon napsal v roce 1994
skoro celý v assembleru,

<!-- S68 -->
tedy v instrukcích,
kterým rozumí sám procesor,
jedné po druhé.

<!-- S69 -->
A někdy
nestačilo ani tohle všechno.

<!-- S70 -->
V roce 1990 měl Wing Commander chybu,
kterou tým nedokázal najít,
a termín se blížil.

<!-- S71 -->
Když jsi hru ukončil,
správce paměti spadl
s chybovou hláškou.

<!-- S72 -->
Programátor Ken Demarest proto
otevřel správce paměti
v hexeditoru
a text té hlášky změnil.

<!-- S73 -->
Teď v ní stálo:
„Díky, že jsi hrál Wing Commander.“

<!-- S74 -->
Pak tým našel skutečnou chybu
a vtip se do vydané hry nikdy nedostal.

<!-- S74b -->
Někteří hráči jsou dodnes přesvědčení, že ho viděli.
A pozdější hry od Originu
se takhle opravdu loučily.

<!-- S75 -->
Čímž se vracíme k Doomu.

<!-- S76 -->
Doom používal DOS/4GW
a běžel jako 32bitový program.

<!-- S77 -->
Hardware pro výpočty s plovoucí čárkou
neměl zaručeně každý počítač.

<!-- S78 -->
Doom proto počítal v pevné řádové čárce.
Celá čísla,
u kterých spodních 16 bitů
představovalo zlomkovou část.

<!-- S79 -->
A jeho svět nebyl
doopravdy trojrozměrný.

<!-- S80 -->
Každý level je plochý půdorys
s výškou každé podlahy
a každého stropu.

<!-- S81 -->
Jedna místnost nikdy nemůže ležet nad druhou.
A pořádně se nahoru ani dolů podívat nedá.

<!-- S82 -->
Než se dal level hrát,
nástroj rozřezal mapu
do binárního stromu, BSP.

<!-- S83 -->
Engine tím stromem prochází
zepředu dozadu,
počínaje stranou, kde stojí hráč,
a přeskakuje oblasti, které nejsou vidět.

<!-- S84 -->
A Doom se ani nepsal v DOSu.

<!-- S85 -->
id Software ho vyvíjeli
na pracovních stanicích NeXT
a výsledek přeložili pro DOS.

<!-- S86 -->
Doom nebyl obecný 3D engine.
Byl postavený přesně
pro jeden druh světa.
Právě ta specializace
mu pomohla běžet na 386.

<!-- S87 -->
A ostatní studia ten svět chtěla.

<!-- S88 -->
Raven Software si engine Doomu licencovali
pro Heretic v roce 1994
a Hexen v roce 1995.

<!-- S89 -->
Doom pomohl zavést
nový způsob, jak dělat hry.
Studia si mohla licencovat existující engine,
místo aby všechno stavěla od nuly.

<!-- S90 -->
Extender paměti.
Zvuková knihovna.
Licencovaný engine.

<!-- S91 -->
Každý z nich sňal z vývojáře
jeden problém.
A vrstev přibývalo,
až z nich vyrostly enginy,
se kterými vývojáři začínají dnes.

<!-- S92 -->
Bylo tedy dělat hry tehdy těžší?
V mnoha ohledech ano.

<!-- S93 -->
Jenže obtížnost nezmizela.
Přesunula se.

<!-- S94 -->
Dnes vývojáři bojují
s gigabajty dat
a miliony polygonů,
místo pár stovek kilobajtů.

<!-- S95 -->
V DOSu musel i hráč
vědět, kam mu mizí paměť.

<!-- S96 -->
Takže mám pro tebe otázku.
Pamatuješ si, jak sis stavěl
spouštěcí nabídku jen kvůli jedné hře?
A bylo to trápení,
nebo půlka zábavy?
Napiš mi to do komentářů.
