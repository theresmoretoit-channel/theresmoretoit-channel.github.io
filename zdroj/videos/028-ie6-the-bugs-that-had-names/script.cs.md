# Internet Explorer 6 — Chyby, které měly jména

<!-- S01 -->
Tohle je druhý díl.

Jestli jsi neviděl první,
je odkaz pod videem.

Krátké shrnutí ale dostaneš tak jako tak.

<!-- S02 -->
V roce 2001
vydal Microsoft
Internet Explorer 6
a přišel s Windows XP.

Během pár let
měl přes devadesát procent
trhu prohlížečů.

<!-- S03 -->
Microsoft toho využil
a udělal z prohlížeče
aplikační platformu.

Byl to skutečný nápad.

Jen ho shodou okolností
zaplatili weboví vývojáři.

<!-- S04 -->
To byl první díl.

Něco jsem ale vynechal.

Vynechal jsem tu část,
kde chyby měly jména.

<!-- S05 -->
Chyba v prohlížeči
je normálně číslo v trackeru.

Issue 4172.

Nikdo si ji nepamatuje.

Nikdo o ní nemluví u oběda.

<!-- S06 -->
V Internet Exploreru 6
měly chyby vlastní jména.

A ukazuje se,
že je to ta nejvýmluvnější věc
na celé té době.

<!-- S07 -->
Začneme něčím mírným.

Necháš obrázek plavat vlevo
a vedle něj dáš odstavec.

Text má sedět
těsně u obrázku.

Místo toho sedí
o tři pixely dál.

<!-- S08 -->
Ne o čtyři.

<!-- S08b -->
Ne o dva.

<!-- S08c -->
O tři.

<!-- S08d -->
Pokaždé.

Mělo to jméno.

The Three Pixel Jog.

<!-- S09 -->
Teď nech ten obrázek plavat vlevo
a dej mu levý okraj
deset pixelů.

Internet Explorer 6
mu jich dá dvacet.

Zdvojnásobí ten okraj,
ale jen na té straně,
na kterou obrázek plave.

<!-- S10 -->
The Double Margin Bug.

A přijímaná oprava byla
prohlásit plovoucí prvek
za řádkový.

<!-- S11 -->
Což je nesmysl.

Plovoucí prvek je blok.

Nazvat ho řádkovým
neznamená vůbec nic.

Fungovalo to, tak to lidi psali.

<!-- S12 -->
Tahle další je lepší.

Načteš stránku
a část obsahu
tam prostě není.

Odscrolluješ dolů.

Odscrolluješ zpátky nahoru.

A ono se to objeví.

<!-- S13 -->
Nic se nenačetlo.

Nic se nezměnilo.

Jenom se to stydělo.

A mělo to správné jméno.

The Peekaboo Bug.

<!-- S14 -->
Lék byl říct
tomu chybějícímu prvku,
že je pozicovaný relativně.

Nikdo nedokázal úplně vysvětlit,
proč ho to vrátilo zpátky.

<!-- S15 -->
Pak je tu ta,
kde najedeš myší na odkaz
a pozadí
rámečku pod ním
se usekne rovnou čarou.

The Guillotine Bug.

<!-- S16 -->
Byla chyba, při které se text
odplížil z místa, kam jsi ho dal.

Magic Creeping Text.

Byla i taková, kde rámečky
vyšly na špatném místě,
ve špatné barvě,
nebo vůbec.

Border Chaos.

<!-- S17 -->
Moje oblíbená je tišší.

Poskládáš vedle sebe řadu bloků
a písmena z toho posledního
se objeví znovu pod ním.

Ne vždycky.

Ne předvídatelně.

The Duplicate Character Bug.

<!-- S18 -->
A o tom, jestli to
potká zrovna tebe,
a kolik písmen
vyjde zdvojených,
rozhodoval počet HTML komentářů,
které jsi nechal ve zdroji.

Komentářů.

Té jediné věci v souboru,
kterou má prohlížeč
zahodit.

<!-- S19 -->
Je tu ještě jedna
a je jiná,
protože tuhle lidi používali
schválně.

Když nastavíš výšku
a obsah je vyšší,
má rámeček přetéct.

Internet Explorer 6
ho místo toho zvětšil.

<!-- S20 -->
Což je špatně.

A zároveň je to přesně to,
co dělá minimální výška.

A Internet Explorer 6
žádnou minimální výšku neměl.

Takže vývojáři přestali
tuhle chybu hlásit
a začali na ní stavět.

<!-- S21 -->
Zastav se a podívej se na ten seznam.

The Three Pixel Jog.

The Double Margin Bug.

Peekaboo.

The Guillotine.

Chybu, kterou potkáš jednou,
nepojmenováváš.

<!-- S22 -->
Tyhle jména měly proto,
že je potkal každý.

A teď to,
co je na tom horší.

Většina z nich měla
pod sebou tutéž příčinu.

<!-- S23 -->
Uvnitř Internet Exploreru 6
každý prvek buď měl,
nebo neměl
něco, čemu se říkalo layout.

<!-- S24 -->
Rozhodovalo to, jestli si prvek
sám určí velikost a pozici,
nebo to nechá na rodiči.

A nastavit se to nedalo.

<!-- S25 -->
Neexistovala žádná vlastnost,
která by se jmenovala layout,
a nešlo si o něj říct.

Nebyl v žádné specifikaci.

Byl to vnitřní příznak
vykreslovacího jádra.

<!-- S26 -->
Šlo ho ale překlopit
omylem.

Stačilo nastavit šířku.

Stačilo nastavit výšku.

Stačilo nechat prvek plavat.

Takže půlka oprav v tomhle videu
byli lidé přepínající vypínač,
na který neviděli.

<!-- S27 -->
Proto začali hledat
nejlevnější způsob,
jak ho překlopit schválně.

Jedním bylo nastavit výšku
na jedno procento.

<!-- S28 -->
Všechny ostatní prohlížeče
se od toho musely držet dál,
takže to šlo dovnitř hacku,
ke kterému se za chvíli dostaneme.

<!-- S29 -->
A v Internet Exploreru 6
to neškodilo,
protože výška, do které se obsah nevejde,
je stejně výška, kterou přeroste.

Chyba z doby před dvěma minutami
je to, co dělá tu opravu bezpečnou.

<!-- S30 -->
Mělo to jméno.

The Holly Hack.

<!-- S31 -->
Ta druhá cesta
byla vlastnost od Microsoftu,
která se jmenuje zoom, nastavená na jedna.

Zoom jedna znamená
nepřibližovat.

<!-- S32 -->
Nezměnilo to nic, co bys viděl.

O to přesně šlo.

Sedělo to ve stylech
čistě proto,
aby to nastavilo neviditelný příznak,
po kterém ty chyby zmizely.

<!-- S33 -->
Čímž se dostáváme k hackům,
a hacky jsou to,
kde to začíná být divné.

Abys opravil jeden prohlížeč,
musíš napřed umět mluvit
jenom na něj.

<!-- S34 -->
A Internet Explorer 6
se choval, jako by byl
ještě jeden prvek
nad prvkem html.

Žádný jiný prohlížeč ne.

Nebylo to nikde popsané.

Prostě se tak choval.

<!-- S35 -->
Tak jsi napsal pravidlo,
které na ten přízrak sedlo,
a vidět ho mohl
jenom ten prohlížeč.

Hvězdička, mezera, html.

<!-- S36 -->
Všechny ostatní prohlížeče se na to podívaly,
nenašly nic, co by sedělo,
a jely dál.

To je star hack
a roky seděl
skoro v každém stylopisu
na webu.

<!-- S37 -->
Byl tu taky
underscore hack.

Napíšeš podtržítko
před název vlastnosti.

<!-- S38 -->
Prohlížeč dodržující standardy
ten řádek zahodí
jako neplatný.

Internet Explorer 6
podtržítko ignoruje
a vlastnost použije.

<!-- S39 -->
Takže jsi schválně rozbil
vlastní stylopis
a to rozbití
byl ten pokyn.

<!-- S40 -->
A pak je tu ten,
který Microsoft postavil schválně.

Šlo napsat komentář,
který poslechl jenom Internet Explorer.

<!-- S41 -->
Pro všechny ostatní prohlížeče
to byl obyčejný komentář,
ignorovaný tak, jak se komentáře ignorují.

Pro Internet Explorer 6
to byly dveře
do druhé verze
té stránky.

<!-- S42 -->
Což znamená, že se výrobce
podíval na tu situaci,
souhlasil, že tenhle prohlížeč
potřebuje vlastní stylopis,
a dodal funkci,
která to má usnadnit.

<!-- S43 -->
Část těch škod
nepotřebovala chybu vůbec.

Internet Explorer 6
měl dva režimy.

V tom modernějším
dodržoval standard.

<!-- S44 -->
V tom starém
zahrnovala šířka rámečku
i jeho vnitřní okraj
a jeho rámování,
což je úplně
jiné číslo.

<!-- S45 -->
Který režim jsi dostal,
záviselo na prvním řádku
dokumentu.

A ta verze HTML,
ke které se všichni přesouvali,
ti říkala, ať tam nahoru dáš
XML deklaraci.

<!-- S46 -->
Ten řádek Internet Explorer 6
přepnul
do toho starého režimu.

Rozbilo ho to,
že jsi dodržel novější standard.

<!-- S47 -->
Pak je tu průhlednost.

Internet Explorer 6 neuměl
zobrazit PNG s měkkými okraji.

Tam, kde měl obrázek přecházet,
dal šedou.

<!-- S48 -->
Odpověď Microsoftu byl filtr
se jménem jako sériové číslo.

Fungoval.

<!-- S49 -->
Jenže kreslil mimo
běžný vykreslovací
proces prohlížeče,
takže odkazy, které jsi dal na něj,
často přestaly fungovat.

Spravil jsi obrázek
a rozbil odkaz.

<!-- S50 -->
A prolnout cokoli jiného
byl druhý filtr,
s vlastní syntaxí,
sedící ve stylopisu
hned vedle běžné vlastnosti,
které rozuměl každý jiný prohlížeč.

<!-- S51 -->
Něco z toho je starší
než ty chyby samotné.

Ještě předtím
se rozvržení stavěla
z vnořených tabulek.

<!-- S52 -->
A abys udržel mezeru otevřenou,
použil jsi průhledný obrázek
o rozměru jednoho pixelu,
roztažený na jakoukoli velikost,
kterou ta mezera potřebovala.

Taky to mělo jméno.

Spacer gif.

<!-- S53 -->
Najetí myší byla další věc.

V Internet Exploreru 6
fungovalo najetí na odkazech.

Jenom na odkazech.

<!-- S54 -->
Takže menu, které se rozbalilo,
když jsi najel myší
na cokoli jiného,
potřebovalo malý program
připojený ke stylopisu.

<!-- S55 -->
Ne skript ve stránce.

Samostatný soubor,
odkazovaný z CSS,
nesoucí kód, jehož úkolem
bylo naučit prohlížeč
jeden selektor.

Ten soubor si lidi
předávali roky.

<!-- S56 -->
První díl zmínil,
že se dal JavaScript
dát dovnitř stylopisu.

Co nezmínil,
je jak často se ten JavaScript spouštěl.

<!-- S57 -->
Při každém pohybu myši.

Při každém stisku klávesy.

Při každém scrollu.

Pořád dokola,
kvůli jedné šířce.

<!-- S58 -->
A ten prohlížeč měl stropy,
které neměl nikdo jiný.

Stylopis se přestal používat
někde za
čtyřmi tisíci pravidly.

Cokoli po
jedenatřicátém stylopisu
na stránce se ignorovalo.

<!-- S59 -->
Což zní jako číslo,
na které nikdy nedosáhneš,
dokud není tvůj web tak velký,
že někdo musí napsat
krok buildu, jehož jediná práce
je slepit stylopisy dohromady,
než je prohlížeč uvidí.

<!-- S60 -->
A něco z toho nebylo
vůbec kosmetické.

Internet Explorer 6
počítal objekty stránky
a objekty skriptu
dvěma různými způsoby
a ani jedna strana
neviděla celou smyčku.

<!-- S61 -->
Takže když skript ukazoval
na část stránky
a ta část stránky
ukazovala zpátky na skript,
neuvolnil se ani jeden.

Nech to okno otevřené dost dlouho
a prohlížeč sežral celý stroj.

<!-- S62 -->
Ta nejlepší z nich
ale není chyba rozvržení.

Napíšeš značku input.

Dáš jí typ.

A zapomeneš rovnítko.

<!-- S63 -->
To je vadný atribut.

Každý parser, co kdy vznikl,
na to má odpověď.

Ignoruj ho.

Hádej, co tam mělo být.

Jeď dál.

<!-- S64 -->
Internet Explorer spadl.

Uvnitř chtěl vědět,
jestli je to pole skryté,
takže porovnal to, cos napsal,
se slovem hidden.

Ty jsi nenapsal nic.

<!-- S65 -->
Tak si to,
cos nenapsal, šel načíst
z adresy nula.

Což by byl
obyčejný pád prohlížeče,
kdyby ten kód, co to dělal,
nebyl mimo prohlížeč.

<!-- S66 -->
Byl ve sdílené systémové knihovně.

Takže ta tři slova
shodila i poštovního klienta
a náhled
ve správci souborů.

<!-- S67 -->
Okno se seznamem souborů
na tvém vlastním počítači,
zavřené webovou stránkou.

To je teze prvního dílu,
která dorazila jako hlášení o pádu.

Prohlížeč nebyl program,
který běží na systému.

Byl částí systému.

<!-- S68 -->
A nešlo si tu opravu
prostě otestovat jinde.

Internet Explorer byl přivařený
k operačnímu systému,
takže jeden počítač
provozoval přesně jednu verzi.

<!-- S69 -->
Proto k práci na frontendu
v roce 2006
patřila police
náhradních strojů.

<!-- S70 -->
A později složka
těch virtuálních,
z nichž každý nesl celý
operační systém,
aby se v něm dala
otevřít jedna stránka.

<!-- S71 -->
A pak někoho napadla
ta zjevná věc.

Když umíš prohlížeč naučit
jednu chybějící vlastnost,
můžeš ho naučit všechny.

<!-- S72 -->
Vývojář jménem Dean Edwards
napsal knihovnu,
jejímž jediným účelem
bylo přimět Internet Explorer 6
chovat se jako jeho
pozdější verze.

Tohle lidi nasazovali.

Do produkce.

<!-- S73 -->
A tady to přestává
být vtipné.

Většinu jedné dekády
šel vážný podíl
světové práce na frontendu
do chyb jednoho prohlížeče.

Ne do funkcí.

Ne do produktů.

Do kompenzace.

<!-- S74 -->
A vydrželo to kvůli tomu,
o čem byl první díl.

Firmy na tom postavily
skutečné aplikace,
takové, co běžely jenom tam,
a ty aplikace
musely v pondělí pořád fungovat.

<!-- S75 -->
Takže prohlížeč, kterého se všichni
chtěli zbavit,
byl ten, který nikdo
nesměl odstranit.

<!-- S76 -->
V roce 2010
Google oznámil, že jeho vlastní
aplikace v něm přestanou fungovat.

A jedno designové studio v Denveru
usoudilo, že si to zaslouží pohřeb.

<!-- S77 -->
Skutečný.

Rakev.

Smuteční řeč.

Osmdesát až sto lidí
se přišlo podívat, jak se pohřbívá
prohlížeč.

Počítali s třiceti.

<!-- S78 -->
A Microsoft poslal květiny.

Na kartičce stálo:
díky za pěkné časy,
Internet Exploreru 6.

<!-- S79 -->
Přesně o rok později
spustil Microsoft web.

Sledoval, kolik světa
pořád běží
na Internet Exploreru 6,
zemi po zemi.

<!-- S80 -->
V tu chvíli
to bylo pořád dvanáct procent.

Cílem bylo dostat to
pod jedno.

Firma, která ten prohlížeč postavila,
provozovala veřejný odpočet
do smrti vlastního produktu.

<!-- S81 -->
Tak proč měly ty chyby jména?

Protože pojmenováváš to,
co nejde obejít.

<!-- S82 -->
Nikdo nepojmenovává počasí
v zemi,
kterou jenom projíždí.

Pojmenováváš ho tam, kde bydlíš.

A zhruba deset let
tam web bydlel.

<!-- S83 -->
Ale dostat Internet Explorer 6
pryč z webu, to je jiný příběh.

A tam se podíváme příště.

Jestli o něj stojíš,
je tu tlačítko odebírat
a odkaz na první díl je pod videem.
