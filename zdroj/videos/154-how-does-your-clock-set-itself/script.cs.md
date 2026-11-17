<!-- S01 -->
Někde u tebe doma
možná jsou hodiny,
které nikdy nikdo nenařídil.

<!-- S02 -->
Přežijí výpadek proudu.
Při změně času se přeřídí
samy, uprostřed noci.

<!-- S03 -->
Nemají připojení k internetu.
Žádná Wi-Fi, žádné GPS,
žádná aplikace v telefonu.

<!-- S04 -->
Mají jen malinký rádiový přijímač.
A jednou za sekundu
zachytí jediný impulz.

<!-- S05 -->
Jak tedy hodiny
z jednoho impulzu za sekundu
poznají přesný čas, datum,
a dokonce i den v týdnu?

<!-- S06 -->
V Evropě ty impulzy přicházejí
z vysílače DCF77 u Frankfurtu.
V Americe z WWVB v Coloradu.
Jiné vysílače, stejný princip.

<!-- S07 -->
Vezměme ten německý.
Vysílá stálou rádiovou vlnu,
ve dne i v noci.
A na začátku každé sekundy
ji na chvilku ztlumí.

<!-- S08 -->
Celý trik je v tom, jak dlouho
zůstane ztlumená.

<!-- S09 -->
Pokles na desetinu sekundy
znamená nulu.
Pokles na dvě desetiny znamená jedničku.

<!-- S10 -->
To je celé.
Žádné pakety, žádná síť.
Jen rádiová vlna, která poklesne
nakrátko, nebo na delší dobu.

<!-- S11 -->
Jeden bit za sekundu.
To znamená, že poslat pouhých 60 bitů
by trvalo celou minutu.

<!-- S12 -->
A ve skutečnosti jich vyšle jen 59.

<!-- S13 -->
V poslední sekundě každé minuty
vlna nepoklesne vůbec.
A právě ten chybějící pokles
je nejdůležitější částí
celého signálu.

<!-- S14 -->
Protože když přijde další pokles,
hodiny vědí,
že právě začala nová minuta.

<!-- S15 -->
Mezera funguje jako tečka.
Všechno mezi dvěma mezerami
je jedna celá věta.

<!-- S16 -->
Co se tedy vejde do věty
o 59 bitech?

<!-- S17 -->
Minuta. Hodina.
Den v měsíci, den v týdnu,
měsíc a rok.

<!-- S18 -->
Většina čísel se posílá po číslicích.
47 minut
se neposílá jako 47.
Posílá se jako dvě samostatné číslice,
čtyřka a sedmička.

<!-- S19 -->
Čtyři bity stačí na jakoukoli číslici
od nuly do devíti.
Desítky minut nikdy nepřesáhnou pětku,
takže dostanou jen tři bity.

<!-- S20 -->
A rok dostane jen dvě číslice.
Pro vysílač
je rok 2026 prostě 26.
Století si hodiny doplní samy.

<!-- S21 -->
Jenže rádio není čistý kanál.
Motor, nabíječka telefonu,
levná LED žárovka...
kterákoli z nich může pokles rozmazat.

<!-- S22 -->
Proto za každým blokem čísel
přijde jeden bit navíc, takzvaný paritní bit.

<!-- S23 -->
Volí se tak, aby počet jedniček
v bloku vyšel vždycky sudý.

<!-- S24 -->
Když rušení překlopí jediný bit,
počet vyjde lichý
a hodiny poznají,
že se něco pokazilo.

<!-- S25 -->
Když se ale překlopí dva bity,
počet je zase sudý
a chyba proklouzne.

<!-- S26 -->
Proto mnoho hodin
nevěří jediné minutě.
Počkají na další platnou.

<!-- S27 -->
A proto může nastavení
trvat několik minut,
a ve špatný den mnohem déle.

<!-- S28 -->
Tím vzniká zvláštní problém.

<!-- S29 -->
Hodiny celou minutu
sbírají čas 10:48.
Jenže zatímco tu zprávu sbírají,
je pořád 10:47.

<!-- S30 -->
Kdy se tedy čas doopravdy změní?

<!-- S31 -->
Ta zpráva je totiž oznámení.
Říká, kolik bude hodin,
až začne další minuta.

<!-- S32 -->
Hodiny přečtou celou větu,
přečkají chybějící pokles,
a když přijde další pokles,
právě ten je tím přesným okamžikem.

<!-- S33 -->
Bity hodinám řeknou, kolik je hodin.
Pokles jim řekne, kdy.

<!-- S34 -->
Jenže ve větě je ještě pár slov,
nejen čas.

<!-- S35 -->
Dva bity říkají, jestli má Německo
zimní, nebo letní čas.

<!-- S36 -->
A třetí je varování.
Celou hodinu před změnou času
je nastavený na jedničku.

<!-- S37 -->
Tvoje hodiny tedy nemusejí vědět,
kterou březnovou neděli
se čas posouvá dopředu
ani kterou říjnovou zpátky.
To pravidlo je nikdy nikdo nenaučil.
Prostě se to dozvědí hodinu předem.

<!-- S38 -->
Jestli Evropa jednou přestane čas střídat,
to varování už prostě nikdy nepřijde.

<!-- S39 -->
Další bit dřív varoval před přestupnou sekundou,
sekundou navíc, kterou občas přidávali,
protože se Země
neotáčí úplně pravidelně.
Taková minuta mohla mít 61 sekund.

<!-- S40 -->
Poslední byla přidána
na konci roku 2016.
Ale v říjnu 2026
se světové metrologické autority
rozhodly přestupné sekundy zrušit.
Od 20. května 2027
poběží UTC bez přerušení.

<!-- S41 -->
A prvních 14 bitů
každé minuty
se času vůbec netýká.

<!-- S42 -->
Od roku 2006 se navíc používají
k přenosu šifrovaných předpovědí počasí
pro kompatibilní meteostanice.

<!-- S43 -->
Takže signál, který nařizuje tvůj budík,
mohl zároveň říct
cizí meteostanici,
jestli bude ve čtvrtek pršet.

<!-- S44 -->
A přesto většina těchto hodin
neposlouchá pořád.
Poslouchání stojí baterii,
a tak to mnohé zkoušejí jednou za noc,
v časných ranních hodinách.

<!-- S45 -->
Dlouhé vlny se k hodinám dostanou dvěma cestami:
podél země
a odrazem od horních vrstev atmosféry.
Po setmění se ta horní cesta změní
a signál často dosáhne dál.

<!-- S46 -->
A ve tři ráno
běží v okolí obvykle méně strojů,
nabíječek a světel, které by ho přehlušily.

<!-- S47 -->
Mezi těmi kontrolami
jdou hodiny podle křemenného krystalu,
který se může rozejít zhruba o sekundu denně.

<!-- S48 -->
Při další úspěšné kontrole
rádio tu odchylku opraví.

<!-- S49 -->
Záleží i na tom, kde hodiny poslouchají.
Anténa je malá feritová tyčinka
omotaná drátem.

<!-- S50 -->
Nejlépe slyší, když tyčinka leží napříč
ke směru vysílače,
ne když na něj míří.
Otoč hodiny
a slabý signál může úplně zmizet.

<!-- S51 -->
Proto jedny hodiny na poličce fungují
a tytéž hodiny o dva metry dál,
za železobetonovou zdí, se nenastaví nikdy.

<!-- S52 -->
Odkud ale vysílač
bere čas?

<!-- S53 -->
Z PTB,
německého národního metrologického ústavu,
který provozuje atomové hodiny.

<!-- S54 -->
Samotná sekunda je definovaná
pomocí atomů cesia.
Jedna sekunda je přesně
9 192 631 770 kmitů
záření, které vydávají.

<!-- S55 -->
Takže levný budík na nočním stolku
se doslova
řídí časovým standardem
definovaným atomy cesia.

<!-- S56 -->
Ne ale dokonale.
Signál se šíří rychlostí světla,
a i světlo potřebuje zhruba 3 milisekundy
na každých 1 000 kilometrů.

<!-- S57 -->
Přijímač přidá vlastní zpoždění
a tvoje hodiny neopraví nic z toho.
Nemusejí.
Ukazují jen sekundy.

<!-- S58 -->
Z jediného místa u Frankfurtu
signál dosáhne k hodinám
až zhruba 2 000 kilometrů daleko.
To je většina Evropy.

<!-- S59 -->
Švýcarsko mělo vlastní vysílač
jménem HBG, do konce roku 2011.
Jeho antény by se musely vyměnit,
používalo ho příliš málo lidí
a švýcarské hodiny mohly místo něj
prostě poslouchat Německo.

<!-- S60 -->
Jiní si ty své nechali.
Británie, Francie, Japonsko i Čína
provozují vlastní.

<!-- S61 -->
A v Severní Americe vysílá WWVB
z Fort Collins od roku 1963,
s časovým kódem od roku 1965.

<!-- S62 -->
Stejný princip, jiné nářečí.
Nula je pokles na dvě desetiny sekundy.
Jednička trvá půl sekundy.

<!-- S63 -->
A místo jedné mezery za minutu
přijde každých 10 sekund delší značka,
jako čárky ve větě.
Dvě za sebou znamenají novou minutu.

<!-- S64 -->
Největší rozdíl je v tom,
jaký čas vysílá.
Německo vysílá středoevropský občanský čas,
který sdílí velká část kontinentu.

<!-- S65 -->
Jenže Spojené státy
se táhnou přes několik časových pásem.
WWVB proto vysílá světový čas UTC
a hodinám řekneš, kde jsi.

<!-- S66 -->
Nevysílá dokonce ani měsíc.
Jen den v roce,
od 1 do 366.

<!-- S67 -->
Každá z těch stanic
mluví jiným jazykem.
Hodiny stavěné pro Německo
si s Coloradem neporadí.

<!-- S68 -->
Ale na obou stranách Atlantiku
je to stejná tichá rutina.
Noc co noc se malý přijímač
srovná s atomovým časovým standardem
stovky nebo tisíce kilometrů daleko.

<!-- S69 -->
A teď otázka pro tebe.
Kdyby všechny rádiové časové signály
dnes v noci zmizely,
všiml by sis toho vůbec?
Napiš mi to do komentářů.
