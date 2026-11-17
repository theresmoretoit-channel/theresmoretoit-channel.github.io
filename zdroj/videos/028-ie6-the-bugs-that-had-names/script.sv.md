# Internet Explorer 6 — Buggarna som hade namn

<!-- S01 -->
Det här är del två.

Om du inte har sett del ett
finns länken nedan.

Men du får en kort sammanfattning ändå.

<!-- S02 -->
År 2001
släppte Microsoft
Internet Explorer 6,
och den kom med Windows XP.

Inom ett par år
hade den över nittio procent
av webbläsarmarknaden.

<!-- S03 -->
Microsoft använde det
för att göra webbläsaren
till en applikationsplattform.

Det var en riktig idé.

Webbutvecklarna råkade bara
få betala för den.

<!-- S04 -->
Det var del ett.

Men jag utelämnade något.

Jag utelämnade den delen
där buggarna hade namn.

<!-- S05 -->
En webbläsarbugg är normalt
ett nummer i ett ärendesystem.

Issue 4172.

Ingen minns den.

Ingen pratar om den vid lunchen.

<!-- S06 -->
I Internet Explorer 6
hade buggarna egennamn.

Och det visar sig vara
det mest talande av allt
i hela den epoken.

<!-- S07 -->
Vi börjar med en mild.

Du låter en bild flyta åt vänster
och sätter ett stycke bredvid.

Texten ska ligga
tätt intill bilden.

I stället ligger den
tre pixlar bort.

<!-- S08 -->
Inte fyra.

<!-- S08b -->
Inte två.

<!-- S08c -->
Tre.

<!-- S08d -->
Varje gång.

Den hade ett namn.

The Three Pixel Jog.

<!-- S09 -->
Låt nu bilden flyta åt vänster
och ge den en vänstermarginal
på tio pixlar.

Internet Explorer 6
ger den tjugo.

Den dubblar marginalen,
men bara på den sida
du lät bilden flyta åt.

<!-- S10 -->
The Double Margin Bug.

Och den vedertagna lösningen
var att förklara
ett flytande element som inline.

<!-- S11 -->
Vilket är nonsens.

Ett flytande element är ett block.

Att kalla det inline
betyder ingenting alls.

Det fungerade, så folk skrev det.

<!-- S12 -->
Nästa är bättre.

Du laddar en sida,
och en del av innehållet
finns helt enkelt inte där.

Du skrollar ned.

Du skrollar upp igen.

Och då dyker det upp.

<!-- S13 -->
Ingenting laddades.

Ingenting ändrades.

Det var bara blygt.

Och det hade rätt namn.

The Peekaboo Bug.

<!-- S14 -->
Botemedlet var att tala om
för det saknade elementet
att det var relativt positionerat.

Ingen kunde riktigt förklara
varför det fick tillbaka det.

<!-- S15 -->
Sedan finns den
där du för musen över en länk,
och bakgrunden
på rutan under den
kapas av i en rak linje.

The Guillotine Bug.

<!-- S16 -->
Det fanns en bugg där texten
kröp bort från där du satt den.

Magic Creeping Text.

Det fanns en där ramarna
hamnade på fel plats,
i fel färg,
eller inte alls.

Border Chaos.

<!-- S17 -->
Min favorit är tystare.

Du lägger ut en rad rutor,
och bokstäver från den sista
dyker upp igen under den.

Inte alltid.

Inte förutsägbart.

The Duplicate Character Bug.

<!-- S18 -->
Och det som avgjorde
om det hände dig,
och hur många bokstäver
som kom ut dubblerade,
var antalet HTML-kommentarer
du hade lämnat kvar i koden.

Kommentarer.

Det enda i filen
som webbläsaren
ska kasta bort.

<!-- S19 -->
Det finns en till,
och den är annorlunda,
för den här använde folk
med flit.

Om du sätter en höjd
och innehållet är högre
ska rutan svämma över.

Internet Explorer 6
förstorade rutan i stället.

<!-- S20 -->
Vilket är fel.

Det är också exakt
vad en minsta höjd gör.

Och Internet Explorer 6
hade ingen minsta höjd.

Så utvecklarna slutade
rapportera den buggen
och började förlita sig på den.

<!-- S21 -->
Stanna upp och titta på listan.

The Three Pixel Jog.

The Double Margin Bug.

Peekaboo.

The Guillotine.

Man namnger inte en bugg
man möter en gång.

<!-- S22 -->
De här hade namn
för att alla mötte dem.

Och här kommer det
som gör det värre.

De flesta av dem hade
samma orsak under ytan.

<!-- S23 -->
Inne i Internet Explorer 6
hade varje element antingen
eller inte
något som kallades layout.

<!-- S24 -->
Det avgjorde om elementet
satte sin egen storlek och position,
eller lämnade det till sin förälder.

Och du kunde inte sätta det.

<!-- S25 -->
Det fanns ingen egenskap
som hette layout,
och inget sätt att be om den.

Den stod inte i någon specifikation.

Den var en intern flagga
i renderingsmotorn.

<!-- S26 -->
Men du kunde slå om den
av misstag.

Att sätta en bredd gjorde det.

Att sätta en höjd gjorde det.

Att låta ett element flyta gjorde det.

Så hälften av lösningarna i den här videon
var folk som slog om en strömbrytare
de inte kunde se.

<!-- S27 -->
Därför började de leta
efter det billigaste sättet
att slå om den med flit.

Ett var att sätta en höjd
på en procent.

<!-- S28 -->
Alla andra webbläsare
måste hållas borta från det,
så det hamnade inuti ett hack
som vi kommer till strax.

<!-- S29 -->
Och i Internet Explorer 6
gjorde det ingen skada,
för en höjd som innehållet inte ryms i
är ändå en höjd den växer förbi.

Buggen från två minuter sedan
är det som gör lösningen ofarlig.

<!-- S30 -->
Den hade ett namn.

The Holly Hack.

<!-- S31 -->
Det andra sättet
var en Microsoft-egenskap
som heter zoom, satt till ett.

Zoom ett betyder
zooma inte.

<!-- S32 -->
Det ändrade ingenting du kunde se.

Det var hela poängen.

Det låg i stilmallarna
enbart för att sätta
en osynlig flagga
som fick buggarna att försvinna.

<!-- S33 -->
Vilket för oss till hacken,
och hacken är där
det blir konstigt.

För att fixa en webbläsare
måste du först kunna tala
till bara den.

<!-- S34 -->
Och Internet Explorer 6
betedde sig som om det fanns
ytterligare ett element
ovanför html-elementet.

Ingen annan webbläsare gjorde det.

Det var inte dokumenterat.

Det var bara så den betedde sig.

<!-- S35 -->
Så du skrev en regel
som matchade fantomen,
och bara den webbläsaren
kunde se den.

Stjärna, mellanslag, html.

<!-- S36 -->
Alla andra webbläsare tittade på den,
hittade ingenting som matchade,
och gick vidare.

Det är star hack,
och i åratal låg det
i nästan varje stilmall
på webben.

<!-- S37 -->
Det fanns också
underscore hack.

Du sätter ett understreck
framför ett egenskapsnamn.

<!-- S38 -->
En standardföljande webbläsare
kastar bort raden
som ogiltig.

Internet Explorer 6
struntar i understrecket
och tillämpar den.

<!-- S39 -->
Så du förstörde med flit
din egen stilmall,
och förstörelsen
var instruktionen.

<!-- S40 -->
Och så finns den
som Microsoft byggde med flit.

Du kunde skriva en kommentar
som bara Internet Explorer lydde.

<!-- S41 -->
För alla andra webbläsare
var det en vanlig kommentar,
ignorerad som kommentarer ignoreras.

För Internet Explorer 6
var det en dörr
in till en andra version
av sidan.

<!-- S42 -->
Vilket betyder att tillverkaren
såg på situationen,
höll med om att den här webbläsaren
behövde en egen stilmall,
och levererade en funktion
som gjorde det enklare.

<!-- S43 -->
En del av skadan
krävde ingen bugg alls.

Internet Explorer 6
hade två lägen.

I det moderna
följde den standarden.

<!-- S44 -->
I det gamla
räknades rutans bredd
inklusive dess innerkant
och dess ram,
vilket är ett helt
annat tal.

<!-- S45 -->
Vilket läge du fick
berodde på första raden
i dokumentet.

Och den version av HTML
som alla var på väg mot
sa åt dig att sätta
en XML-deklaration där uppe.

<!-- S46 -->
Den raden knuffade
Internet Explorer 6
in i det gamla läget.

Att följa den nyare standarden
var det som gick sönder.

<!-- S47 -->
Sedan har vi genomskinligheten.

Internet Explorer 6 kunde inte
visa en PNG med mjuka kanter.

Där bilden skulle tona ut
lade den grått.

<!-- S48 -->
Microsofts svar var ett filter
med ett namn som ett serienummer.

Det fungerade.

<!-- S49 -->
Men det ritade utanför
webbläsarens normala
renderingsprocess,
så länkar du lade ovanpå det
slutade ofta fungera.

Du fixade bilden
och förstörde länken.

<!-- S50 -->
Och att tona något annat
var ett andra filter,
med egen syntax,
som låg i stilmallen
precis bredvid den vanliga egenskapen
som alla andra webbläsare förstod.

<!-- S51 -->
En del av det här är äldre
än buggarna själva.

Före allt detta
byggdes layouter
av nästlade tabeller.

<!-- S52 -->
Och för att hålla ett mellanrum öppet
använde du en genomskinlig bild
på en pixel,
utsträckt till vilken storlek
mellanrummet än behövde.

Den hade också ett namn.

The spacer gif.

<!-- S53 -->
Hovring var en annan sak.

I Internet Explorer 6
fungerade hovring på länkar.

Bara på länkar.

<!-- S54 -->
Så en meny som öppnades
när du förde musen
över något annat
behövde ett litet program
kopplat till stilmallen.

<!-- S55 -->
Inte ett skript i sidan.

En separat fil,
refererad från CSS,
med kod vars uppgift
var att lära webbläsaren
en enda selektor.

Den filen skickade folk runt
i åratal.

<!-- S56 -->
Del ett nämnde
att man kunde lägga JavaScript
inuti en stilmall.

Vad den inte nämnde
är hur ofta det skriptet kördes.

<!-- S57 -->
Vid varje musrörelse.

Vid varje tangenttryck.

Vid varje skroll.

Om och om igen,
för att räkna ut en bredd.

<!-- S58 -->
Och webbläsaren hade tak
som ingen annan hade.

En stilmall slutade gälla
någonstans bortom
fyra tusen regler.

Allt efter
den trettioförsta stilmallen
på en sida ignorerades.

<!-- S59 -->
Vilket låter som ett tal
man aldrig når,
tills din sajt är så stor
att någon måste skriva
ett byggsteg vars enda uppgift
är att slå ihop stilmallar
innan webbläsaren ser dem.

<!-- S60 -->
Och en del av det var inte
kosmetiskt alls.

Internet Explorer 6
räknade sina sidobjekt
och sina skriptobjekt
på två olika sätt,
och ingen av sidorna
kunde se hela slingan.

<!-- S61 -->
Så om ett skript pekade
på en del av sidan,
och den delen av sidan
pekade tillbaka på skriptet,
frigjordes ingen av dem.

Låt fönstret stå öppet länge nog
och webbläsaren åt upp maskinen.

<!-- S62 -->
Men den bästa
är ingen layoutbugg alls.

Du skriver en input-tagg.

Du ger den en typ.

Och du glömmer likhetstecknet.

<!-- S63 -->
Det är ett felformat attribut.

Varje parser som någonsin skrivits
har ett svar på det.

Ignorera det.

Gissa vad som menades.

Fortsätt.

<!-- S64 -->
Internet Explorer kraschade.

Inuti ville den veta
om fältet var dolt,
så den jämförde det du hade skrivit
med ordet hidden.

Du hade inte skrivit något.

<!-- S65 -->
Så den gick för att hämta
det du inte hade skrivit
från adress noll.

Vilket vore
en vanlig webbläsarkrasch,
förutom att koden som gjorde det
inte satt i webbläsaren.

<!-- S66 -->
Den satt i ett delat systembibliotek.

Så de tre orden
tog också ned e-postklienten
och förhandsgranskningen
i filhanteraren.

<!-- S67 -->
Ett fönster som listar filer
på din egen maskin,
stängt av en webbsida.

Det är del etts argument
som anländer som en kraschrapport.

Webbläsaren var inte ett program
som kördes på systemet.

Den var en del av systemet.

<!-- S68 -->
Och du kunde inte bara
testa lösningen någon annanstans.

Internet Explorer var svetsad
till operativsystemet,
så en dator
körde exakt en version.

<!-- S69 -->
Därför kom ett frontendjobb
år 2006
med en hylla
reservmaskiner.

<!-- S70 -->
Och senare med en mapp
av virtuella,
där var och en bar ett helt
operativsystem
bara för att en sida
skulle kunna öppnas i det.

<!-- S71 -->
Och så gjorde någon
det uppenbara.

Om du kan lära webbläsaren
en saknad funktion
kan du lära den alla.

<!-- S72 -->
En utvecklare vid namn Dean Edwards
skrev ett bibliotek
vars hela syfte
var att få Internet Explorer 6
att bete sig som en senare
version av sig själv.

Det körde folk skarpt.

I produktion.

<!-- S73 -->
Och där slutar det
vara roligt.

Under större delen av ett decennium
gick en betydande del
av världens frontendarbete
till en webbläsares misstag.

Inte funktioner.

Inte produkter.

Kompensation.

<!-- S74 -->
Och det varade på grund av
det som del ett handlade om.

Företag hade byggt
riktiga applikationer på den,
sådana som bara körde där,
och de applikationerna
måste fortfarande fungera på måndag.

<!-- S75 -->
Så webbläsaren som alla
ville bli av med
var den som ingen
fick ta bort.

<!-- S76 -->
År 2010
meddelade Google att dess egna
appar skulle sluta fungera i den.

Och en designbyrå i Denver
tyckte att det förtjänade en begravning.

<!-- S77 -->
En riktig.

En kista.

Ett griftetal.

Mellan åttio och hundra personer
kom för att se en webbläsare
begravas.

De hade räknat med trettio.

<!-- S78 -->
Och Microsoft skickade blommor.

På kortet stod det:
tack för de goda tiderna,
Internet Explorer 6.

<!-- S79 -->
Exakt ett år senare
lanserade Microsoft en webbplats.

Den följde hur stor del av världen
som fortfarande körde
Internet Explorer 6,
land för land.

<!-- S80 -->
Vid den tidpunkten
var det fortfarande tolv procent.

Målet var att pressa det
under ett.

Företaget som byggde webbläsaren
drev en offentlig nedräkning
till sin egen produkts död.

<!-- S81 -->
Så varför hade buggarna namn?

För att man namnger det
man inte kan gå runt.

<!-- S82 -->
Ingen namnger vädret
i ett land
man bara passerar igenom.

Man namnger det där man bor.

Och i ungefär tio år
var det där webben bodde.

<!-- S83 -->
Men att få bort Internet Explorer 6
från webben är en annan historia.

Och dit går vi härnäst.

Vill du ha den
finns det en prenumerationsknapp,
och del ett är länkad nedan.
