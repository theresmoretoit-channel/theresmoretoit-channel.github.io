# Internet Explorer 6 — Prohlížeč, ze kterého se stala platforma

Překlad `script.md`. Stejné značky scén, stejný počet řádků.
Řádek = jedna fráze = jeden titulek.

<!-- S01 -->
Představte si, že jste webový vývojář
na začátku nového tisíciletí.

Napsali jste
naprosto rozumnou webovou stránku.

<!-- S02 -->
Funguje v Netscape.

Funguje v Opeře.

Funguje i v novém Firefoxu.

A pak ji otevřete
v Internet Exploreru.

Všechno je rozbité.

<!-- S03 -->
Rozvržení je špatně.

Tlačítka se posunula.

PNG obrázky vypadají příšerně.

A jaksi záhadně
jedno zalomení řádku ve vašem HTML
udělalo třípixelovou mezeru.

<!-- S04 -->
Vítejte ve vývoji pro web
v éře Internet Exploreru 6.

Jenže tady je ta zajímavá věc.

Internet Explorer 6
nebyl prostě jen mizerný prohlížeč.

<!-- S05 -->
Microsoft se snažil řešit problémy,
které web opravdu měl.

Měl jen jednu obrovskou výhodu
proti všem ostatním.

Windows.

<!-- S06 -->
A ta výhoda mu nakonec
dovolila udělat z prohlížeče
něco mnohem většího
než prohlížeč.

<!-- S07 -->
V polovině devadesátých let
webu vládl
Netscape Navigator.

Microsoftu se to nelíbilo.

<!-- S08 -->
Internet Explorer se proto
přibalil k Windows
a byl zdarma.

Koupili jste počítač s Windows.

Internet Explorer už tam byl.

Nic ke stažení.

Nic k zaplacení.

<!-- S09 -->
A hlavně: Microsoft
ovládal
operační systém.

Krátce po roce 2000
měl Internet Explorer
přes devadesát procent
trhu s prohlížeči.

<!-- S10 -->
Internet Explorer 6 přišel
v roce 2001,
spolu s Windows XP.

A chvíli to vypadalo,
že Microsoft prostě vyhrál
válku prohlížečů.

<!-- S11 -->
Microsoft měl problém.

Web toho uměl velmi málo.

HTML umělo zobrazit dokument.

CSS ho umělo nastylovat.

JavaScript ho uměl oživit.

<!-- S12 -->
A tím to skončilo.

Cokoli složitějšího
narazilo rovnou
na hranice prohlížeče.

<!-- S13 -->
Co když jste chtěli naskenovat dokument?

Nebo komunikovat s čipovou kartou?

Nebo si promluvit s nějakým
hardwarem ve Windows?

<!-- S14 -->
Prohlížeč tohle
pořádně neuměl.

Microsoft proto přišel s řešením.

ActiveX.

<!-- S15 -->
Základní myšlenka byla prostá.

Proč omezovat webovou aplikaci
na to, co umí prohlížeč?

Ať si klidně sáhne
na nativní součásti Windows.

<!-- S16 -->
A webová stránka najednou
uměla věci,
o kterých se obyčejnému HTML
ani nesnilo.

<!-- S17 -->
Dnes zní ActiveX děsivě.

A právem.

Komponenta ActiveX si mohla sáhnout
na soubory, na aplikace,
na hardware
i na operační systém.

<!-- S18 -->
Z dnešního pohledu na bezpečnost
to zní naprosto šíleně.

Krátce po roce 2000
to ale u firemních aplikací
dávalo dokonalý smysl.

<!-- S19 -->
Firmy nechtěly
hezkou prohlížečku dokumentů.

Chtěly aplikace.

Chtěly webové stránky,
které se chovají
skoro jako program na ploše.

<!-- S20 -->
A Microsoft jim to dal.

I samotný Windows Update
původně stál na ActiveX —
prohlédl si systém
a zjistil, které aktualizace
jsou potřeba.

<!-- S21 -->
ActiveX tedy nebyl prostě
hloupý omyl.

Byl to raný pokus
udělat z prohlížeče
aplikační platformu.

<!-- S22 -->
A v tomhle smyslu byl Microsoft
vlastně před svou dobou.

Problém byl v tom, kolik moci
té platformě dal.

<!-- S23 -->
ActiveX nebyl
jediné microsoftí rozšíření.

Byl tu VBScript.

Bylo tu DHTML.

A dokonce i CSS expression.

Ano.

<!-- S24 -->
Internet Explorer uměl vyhodnotit
JavaScript přímo uvnitř CSS.

Šlo napsat něco takového.

<!-- S25 -->
Bylo to absurdní.

A občas taky
překvapivě užitečné.

A nic z toho nemělo zaručeno,
že to bude fungovat jinde.

<!-- S26 -->
Microsoft web
prostě neimplementoval.

Microsoft web rozšiřoval
vlastním směrem.

A s devadesáti procenty
trhu
měl dost moci na to,
aby mu to prošlo.

<!-- S27 -->
Jedním z nejznámějších příkladů
byl box model v CSS.

Standardní model říkal,
že když je prvek
široký 200 pixelů,
má 20 pixelů paddingu
a 5 pixelů rámečku,

<!-- S28 -->
je celková šířka
250 pixelů.

<!-- S29 -->
Starší verze Internet Exploreru
to četly jinak.

V quirks módu mohla deklarovaná šířka
zahrnovat i padding
a rámeček.

<!-- S30 -->
Nebyl to nutně
šílený způsob, jak o šířce přemýšlet.

Dnes si přesně takové chování
často vyžádáme schválně.

Říká se mu border-box.

<!-- S31 -->
Skutečný problém byl v tom,
že se různé prohlížeče
chovaly různě.

A to znamenalo,
že to vývojáře muselo zajímat.

Hodně.

<!-- S32 -->
Existovalo cosi jménem hasLayout.

Nebyla to normální CSS vlastnost.

Nebyla součástí standardu.

Ale rozhodovala o tom,
jak Internet Explorer
rozvrhne prvky.

<!-- S33 -->
A rozbité rozvržení se občas
záhadně spravilo
přidáním jediného řádku.

zoom: 1

Proč?

Protože zoom: 1 uměl spustit
vnitřní mechanismus hasLayout.

<!-- S34 -->
Byly problémy
s průhledností PNG.

Byly problémy s prvky select,
které se kreslily přes
absolutně pozicované rozbalovací panely
bez ohledu na to, jak vysoko
jste nastavili z-index.

<!-- S35 -->
Vývoj pro web nebyl jen o tom
udělat návrh.

Byl o tom naučit se chyby
jednoho konkrétního enginu.

<!-- S36 -->
Další nádherný příklad.

Bílé znaky.

A za tenhle Internet Explorer
ani nemohl.

Šlo dát dva obrázky
těsně vedle sebe
do markupu,
bez čehokoli mezi tagy,
a dostat jeden výsledek.

<!-- S37 -->
Pak někdo HTML hezky zformátoval
a dal každý tag na vlastní řádek.

A najednou byla mezi obrázky
několikapixelová mezera.

Konec řádku začal být významný.

<!-- S38 -->
Formátovač kódu
vám doslova rozbil stránku.

A kdybyste náhodou používali
starou verzi Visual Studia,
ochotně vám to HTML
zformátoval sám.

Díky, Microsofte.

<!-- S39 -->
Vývojáři si nashromáždili
celý kufřík obezliček.

Conditional comments.

<!-- S40 -->
A občas úplně
bizarně vypadající HTML,
jehož jediným účelem bylo
uklidnit Internet Explorer.

<!-- S41 -->
Nepsali jste ošklivý kód proto,
že jste byli špatní programátoři.

Psali jste ošklivý kód proto,
že vás k tomu prohlížeč donutil.

<!-- S42 -->
Internet Explorer taky padal
velkolepě — a často vzal s sebou
všechna otevřená okna.

<!-- S43 -->
Což dalo vzniknout nádherné kategorii
kancelářské zábavy.

Hele, mrkni na tenhle odkaz.

A dvacet oken Internet Exploreru
zmizí.

<!-- S44 -->
Tohle byl web předtím,
než prohlížeče dostaly pískoviště.

Dnešní prohlížeč říká tohle.

Téhle stránce nevěřím.

Zavřu ji zvlášť.

<!-- S45 -->
Internet Explorer 6
působil spíš takhle.

Ty jsi webová stránka?

Jasně.

Tady máš klíče od baráku.

<!-- S46 -->
Proč vlastně vývojáři
tyhle obezličky používali?

Protože museli.

<!-- S47 -->
Představte si firmu
s pěti sty zaměstnanci.

Na každém počítači běží Windows XP.

Na každém je Internet Explorer.

<!-- S48 -->
Vývojář má dvě možnosti.

Možnost jedna.

Udělat to pro Internet Explorer,
který stejně mají všichni.

<!-- S49 -->
Možnost dvě.

Udělat to pro každý prohlížeč,
otestovat všechno všude
a vysvětlit IT oddělení,
proč všichni potřebují ještě druhý.

Odpověď bývala jasná.

<!-- S50 -->
Nevybírali si
microsoftí technologii proto,
že by Microsoft milovali.

Vybírali si to, co řešilo
zákazníkův problém.

A ActiveX byl někdy
nejlepší nástroj, který byl k mání.

<!-- S51 -->
Nakonec toho měl někdo dost.

JavaScriptové knihovny začaly
rozdíly mezi prohlížeči schovávat.

Jednou z nejdůležitějších
byla jQuery.

<!-- S52 -->
Místo psaní
obsluhy událostí pro každý prohlížeč
jste napsali jediný řádek,
který fungoval všude.

<!-- S53 -->
Místo ručního žonglování
s různými implementacemi AJAXu
jste použili jednu společnou abstrakci.

<!-- S54 -->
jQuery Internet Explorer
nezrušila.

Ale bylo díky ní mnohem snazší
předstírat, že neexistuje.

A pro webové vývojáře té doby
to byla nádhera.

<!-- S55 -->
Objevil se Firefox.

Opera se vyvíjela dál.

Přišlo Safari.

A Google nakonec vydal Chrome.

<!-- S56 -->
Válka prohlížečů byla zpátky
a tentokrát
vypadala konkurence jinak.

JavaScriptové enginy
se dramaticky zrychlily.

Přišlo HTML5.

<!-- S57 -->
Prohlížeč sám se začal učit
všechno to, na co vývojáři
dosud potřebovali zásuvné moduly.

<!-- S58 -->
Video.

Zvuk.

Canvas.

SVG.

WebGL.

WebSockets.

A nakonec WebRTC.

Z webu se stávala
aplikační platforma.

<!-- S59 -->
Což bylo přesně to,
o co se Microsoft
snažil s ActiveX.

Jenže teď se to dělo
přes otevřené standardy.

<!-- S60 -->
Microsoft to zkusil ještě jednou.

Silverlight dovolil stavět
bohaté aplikace v prohlížeči
v C# a .NET.

Běžel na něm dokonce
i raný streaming Netflixu.

<!-- S61 -->
Jenže web nechtěl moduly navždy.

Apple odmítl podporovat Flash
na iPhonu.

A budoucnost najednou nebyla tohle.

Prohlížeč plus modul.

Byla tohle.

Prohlížeč sám.

<!-- S62 -->
Silverlight zmizel.

Flash zmizel.

ActiveX zmizel.

A nakonec zmizel
i Internet Explorer.

<!-- S63 -->
A tady začíná být
ten příběh zajímavý.

Protože Microsoft
se nemýlil úplně.

Předpověděl správně,
že se z prohlížeče stane
aplikační platforma.

<!-- S64 -->
Jen se tam snažil dostat
přes uzavřené technologie.

Web došel do stejného cíle
přes standardy.

<!-- S65 -->
Prohlížeč vyhrál.

Ale vyhrál tím, že se stal
něčím mnohem mocnějším
než prohlížeč
z roku 2001.

<!-- S66 -->
Byl tedy Microsoft padouch?

Vlastně ne.

A právě to dělá
ten příběh zajímavějším.

<!-- S67 -->
Microsoft měl skvělé inženýry.

Měl obrovské zdroje.

A postavil spoustu technologií,
které byly opravdu před svou dobou.

<!-- S68 -->
Jenže Microsoft měl taky
drtivé postavení na trhu.

A to vytvořilo
nebezpečné pokušení.

<!-- S69 -->
Když skoro každý
používá váš prohlížeč,
proč čekat na standardy?

Proč prostě nenasadit
vlastní řešení?

Chvíli to fungovalo.

Než zbytek webu dohnal náskok.

<!-- S70 -->
Internet Explorer je dnes pryč.

Stará válka prohlížečů
vypadá jako dávná historie.

Ale podívejte se
na dnešní trh s prohlížeči.

Chrome.

Edge.

Opera.

Brave.

Vivaldi.

<!-- S71 -->
A spousta dalších
stojí na Chromiu.

Různé produkty.

Často tentýž
engine vespod.

<!-- S72 -->
Možná jsme tedy vyměnili tohle.

Jeden prohlížeč, na který museli myslet všichni.

Za tohle.

Jeden engine, na kterém staví všichni.

Nezní vám to povědomě?

<!-- S73 -->
Protože dominantní engine
nerozhoduje jen o tom,
jak se stránky zobrazí.

<!-- S74 -->
Ovlivňuje, co vývojáři staví.

Které technologie zpopulárnějí.

A nakonec i to,
čím se web sám stane.

<!-- S75 -->
Je tu ale
jeden velmi důležitý rozdíl.

Dnešní web stojí
na otevřených standardech.

Firefox má pořád vlastní engine.

Safari má WebKit.

Chromium je otevřený software.

<!-- S76 -->
A moderní prohlížeče
se aktualizují samy.

Zdaleka nejsme
v situaci
roku 2003.

<!-- S77 -->
Základní otázka ale zůstává.

Jak velký vliv
má mít jediná firma
na platformu,
kterou používá skoro každý?

To je otázka,
která nikdy pořádně nezmizela.

<!-- S78 -->
Byl tedy Internet Explorer 6 hrozný?

Ano.

Občas velkolepě hrozný.

<!-- S79 -->
Ale to není celý příběh.

Byl to taky produkt své doby.

<!-- S80 -->
Problém byl v tom,
že Microsoft vyhrál
válku prohlížečů tak dokonale,
že mohl určovat pravidla.

<!-- S81 -->
A zaplatili to weboví vývojáři.

Naučili se záhady
hasLayoutu.

Zjistili, že zoom: 1
umí kouzelně spravovat věci.

A modlili se.

<!-- S82 -->
A z Internet Exploreru se nakonec
stalo to, co dvacet let
sám vytvářel.

Zastaralá platforma,
kterou už nikdo
nechtěl podporovat.

<!-- S83 -->
Web microsoftí vizi
neodmítl.

Jen z ní postavil
lepší verzi.

A jestli nás má ta doba
něco naučit,
tak tohle.

<!-- S84 -->
Technologie se nestane standardem
jen proto, že je dobrá.

<!-- S85 -->
Někdy se stane standardem proto,
že jedna firma má dost moci na to,
aby ji používali všichni.

<!-- S86 -->
A někdy nám
po dvaceti letech
dojde, že jsme to udělali znovu.
