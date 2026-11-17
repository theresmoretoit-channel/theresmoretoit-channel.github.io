# Internet Explorer 6 — Webbläsaren som blev en plattform

Översättning av `script.md`. Samma scenmarkeringar, samma antal rader.
En rad = en fras = en undertext.

<!-- S01 -->
Tänk dig att du är webbutvecklare
i början av tvåtusentalet.

Du har skrivit
en fullkomligt rimlig webbsida.

<!-- S02 -->
Den fungerar i Netscape.

Den fungerar i Opera.

Den fungerar i nya Firefox.

Och så öppnar du den
i Internet Explorer.

Allt är trasigt.

<!-- S03 -->
Layouten är fel.

Knapparna har flyttat sig.

PNG-bilderna ser förfärliga ut.

Och på något sätt har
en enda radbrytning i din HTML
skapat ett glapp på tre pixlar.

<!-- S04 -->
Välkommen till webbutveckling
i Internet Explorer 6:s tidsålder.

Men här kommer det intressanta.

Internet Explorer 6
var inte bara en usel webbläsare.

<!-- S05 -->
Microsoft försökte lösa problem
som webben faktiskt hade.

De hade bara en enorm fördel
gentemot alla andra.

Windows.

<!-- S06 -->
Och den fördelen lät till slut
Microsoft förvandla webbläsaren
till något mycket större
än en webbläsare.

<!-- S07 -->
I mitten av nittiotalet
dominerades webben
av Netscape Navigator.

Microsoft gillade inte det.

<!-- S08 -->
Så Internet Explorer
följde med Windows
och gjordes gratis.

Du köpte en Windows-dator.

Internet Explorer fanns redan där.

Inget att ladda ner.

Inget att betala.

<!-- S09 -->
Och framför allt:
Microsoft kontrollerade
operativsystemet.

Strax efter år 2000
hade Internet Explorer
mer än nittio procent
av webbläsarmarknaden.

<!-- S10 -->
Internet Explorer 6 kom
2001,
tillsammans med Windows XP.

Och ett tag såg det ut som om
Microsoft helt enkelt hade vunnit
webbläsarkriget.

<!-- S11 -->
Microsoft hade ett problem.

Webben kunde extremt lite.

HTML kunde visa dokument.

CSS kunde ge dem stil.

JavaScript kunde göra dem interaktiva.

<!-- S12 -->
Och ungefär där tog det slut.

Allt som var mer komplicerat
gick rakt in
i webbläsarens gränser.

<!-- S13 -->
Tänk om du ville skanna ett dokument?

Eller prata med ett smartkort?

Eller med någon bit
Windows-hårdvara?

<!-- S14 -->
Webbläsaren kunde
egentligen inte det.

Så Microsoft kom med en lösning.

ActiveX.

<!-- S15 -->
Grundidén var enkel.

Varför begränsa en webbapplikation
till vad webbläsaren kan?

Låt den använda
inbyggda Windows-komponenter.

<!-- S16 -->
Och plötsligt kunde en webbsida
göra saker
som vanlig HTML
inte ens kunde drömma om.

<!-- S17 -->
I dag låter ActiveX skrämmande.

Och det med rätta.

En ActiveX-komponent kunde nå
filerna, programmen,
hårdvaran
och operativsystemet.

<!-- S18 -->
Ur dagens säkerhetsperspektiv
låter det fullständigt vansinnigt.

Men i början av tvåtusentalet
var det helt logiskt
för företagsapplikationer.

<!-- S19 -->
Företagen ville inte ha
en snygg dokumentvisare.

De ville ha applikationer.

De ville ha webbsidor
som betedde sig
nästan som skrivbordsprogram.

<!-- S20 -->
Och exakt det gav Microsoft dem.

Till och med Windows Update
byggde från början på ActiveX
för att undersöka systemet
och räkna ut vilka uppdateringar
som behövdes.

<!-- S21 -->
ActiveX var alltså inte bara
ett dumt misstag.

Det var ett tidigt försök
att göra webbläsaren
till en applikationsplattform.

<!-- S22 -->
Och i den meningen låg Microsoft
faktiskt före sin tid.

Problemet var hur mycket makt
de gav den plattformen.

<!-- S23 -->
ActiveX var inte
Microsofts enda utvidgning.

Det fanns VBScript.

Det fanns DHTML.

Och till och med CSS expression.

Ja.

<!-- S24 -->
Internet Explorer kunde köra
JavaScript direkt inuti CSS.

Man kunde skriva något sådant här.

<!-- S25 -->
Det var absurt.

Och ibland också
förvånansvärt användbart.

Och inget av det var garanterat
att fungera någon annanstans.

<!-- S26 -->
Microsoft implementerade
inte bara webben.

Microsoft utvidgade webben
i sin egen riktning.

Och med nittio procent
av marknaden
hade de nog med makt
för att det skulle gå.

<!-- S27 -->
Ett av de mest kända exemplen
var CSS-boxmodellen.

Standardmodellen sa
att om ett element
var 200 pixlar brett,
med 20 pixlar innerkant
och 5 pixlar ram,

<!-- S28 -->
så var den totala bredden
250 pixlar.

<!-- S29 -->
Äldre versioner av Internet Explorer
läste det annorlunda.

I quirks-läge kunde den angivna bredden
räkna in innerkanten
och ramen.

<!-- S30 -->
Det var inte nödvändigtvis
ett vansinnigt sätt att tänka på bredd.

I dag ber vi faktiskt ofta
om precis det beteendet med flit.

Det heter border-box.

<!-- S31 -->
Det verkliga problemet var
att olika webbläsare
betedde sig olika.

Och det betydde
att utvecklaren måste bry sig.

Mycket.

<!-- S32 -->
Det fanns något som hette hasLayout.

Det var ingen vanlig CSS-egenskap.

Det ingick inte i standarden.

Men det avgjorde
hur Internet Explorer
placerade ut element.

<!-- S33 -->
Och ibland kunde en trasig layout
mystiskt lagas
genom att lägga till en enda rad.

zoom: 1

Varför?

Därför att zoom: 1 kunde utlösa
den interna hasLayout-mekanismen.

<!-- S34 -->
Det fanns problem
med PNG-genomskinlighet.

Det fanns problem med select-element
som lade sig ovanpå
absolut positionerade menyer,
hur högt du än
satte z-index.

<!-- S35 -->
Webbutveckling handlade inte bara om
att förverkliga sin design.

Den handlade om att lära sig buggarna
i en viss renderingsmotor.

<!-- S36 -->
Här är ett till underbart exempel.

Blanksteg.

Och för det här kunde
Internet Explorer inte ens rå.

Du kunde lägga två bilder
alldeles intill varandra
i koden,
utan något mellan taggarna,
och få ett resultat.

<!-- S37 -->
Sedan formaterade någon HTML-koden snyggt
och gav varje tagg en egen rad.

Och plötsligt fanns det
ett glapp på några pixlar mellan bilderna.

Radbrytningen började betyda något.

<!-- S38 -->
Din kodformaterare
kunde bokstavligen förstöra din sida.

Och om du använde
en gammal version av Visual Studio
formaterade den gladeligen
din HTML åt dig.

Tack, Microsoft.

<!-- S39 -->
Utvecklarna samlade på sig
en hel verktygslåda med kringgåenden.

Villkorliga kommentarer.

<!-- S40 -->
Och ibland fullkomligt
bisarrt utseende HTML
vars enda syfte var
att få Internet Explorer att uppföra sig.

<!-- S41 -->
Du skrev inte ful kod
för att du var en dålig programmerare.

Du skrev ful kod
för att webbläsaren tvingade dig.

<!-- S42 -->
Internet Explorer kraschade också
spektakulärt, och tog ofta
alla öppna fönster med sig.

<!-- S43 -->
Vilket gav upphov till en underbar sorts
kontorsunderhållning.

Du, kolla in den här länken.

Och tjugo Internet Explorer-fönster
försvinner.

<!-- S44 -->
Det här var webben innan
webbläsarna kördes i sandlåda.

Dagens webbläsare säger så här.

Den här webbplatsen litar jag inte på.

Jag isolerar den.

<!-- S45 -->
Internet Explorer 6
lät snarare så här.

Är du en webbsida?

Visst.

Här är nycklarna till huset.

<!-- S46 -->
Varför använde utvecklarna
egentligen de här knepen?

För att de måste.

<!-- S47 -->
Tänk dig ett företag
med femhundra anställda.

På varje dator kör Windows XP.

På varje finns Internet Explorer.

<!-- S48 -->
Utvecklaren har två alternativ.

Alternativ ett.

Bygga för Internet Explorer,
som alla ändå redan har.

<!-- S49 -->
Alternativ två.

Bygga för varje webbläsare,
testa allt överallt
och förklara för IT-avdelningen
varför alla behöver en till.

Svaret var oftast uppenbart.

<!-- S50 -->
De valde inte
Microsofts teknik
för att de älskade Microsoft.

De valde det som löste
kundens problem.

Och ibland var ActiveX
det bästa verktyg som fanns.

<!-- S51 -->
Och till slut fick någon nog.

JavaScript-biblioteken började
dölja skillnaderna mellan webbläsarna.

Ett av de viktigaste
var jQuery.

<!-- S52 -->
I stället för att skriva
händelsehantering per webbläsare
kunde du skriva en enda rad
som fungerade överallt.

<!-- S53 -->
I stället för att för hand brottas
med olika AJAX-implementationer
använde du en gemensam abstraktion.

<!-- S54 -->
jQuery fick inte
Internet Explorer att försvinna.

Men det blev mycket lättare
att låtsas att den inte fanns.

Och för dåtidens webbutvecklare
var det något underbart.

<!-- S55 -->
Firefox dök upp.

Opera fortsatte utvecklas.

Safari kom.

Och till slut släppte Google Chrome.

<!-- S56 -->
Webbläsarkrigen var tillbaka,
och den här gången
såg konkurrensen annorlunda ut.

JavaScript-motorerna
blev dramatiskt bättre.

HTML5 kom.

<!-- S57 -->
Webbläsaren själv började lära sig
allt det som utvecklarna
tidigare behövde insticksprogram för.

<!-- S58 -->
Video.

Ljud.

Canvas.

SVG.

WebGL.

WebSockets.

Och till slut WebRTC.

Webben höll på att bli
en applikationsplattform.

<!-- S59 -->
Vilket var precis det
som Microsoft hade försökt
uppnå med ActiveX.

Fast nu skedde det
genom öppna standarder.

<!-- S60 -->
Microsoft försökte en gång till.

Silverlight lät utvecklare bygga
rika webbläsarapplikationer
i C# och .NET.

Netflix tidiga strömning
kördes till och med på det.

<!-- S61 -->
Men webben ville inte ha insticksprogram för evigt.

Apple vägrade stödja Flash
på iPhone.

Och plötsligt var framtiden inte det här.

Webbläsare plus insticksprogram.

Den var det här.

Webbläsaren själv.

<!-- S62 -->
Silverlight försvann.

Flash försvann.

ActiveX försvann.

Och till slut försvann
även Internet Explorer.

<!-- S63 -->
Och det är här
historien blir intressant.

För Microsoft
hade inte helt fel.

De hade förutsagt korrekt
att webbläsaren skulle bli
en applikationsplattform.

<!-- S64 -->
De försökte bara ta sig dit
genom proprietär teknik.

Webben nådde samma mål
genom standarder.

<!-- S65 -->
Webbläsaren vann.

Men den vann genom att bli
något långt kraftfullare
än webbläsaren
från 2001.

<!-- S66 -->
Var Microsoft alltså skurken?

Egentligen inte.

Och det är just det som gör
historien mer intressant.

<!-- S67 -->
Microsoft hade lysande ingenjörer.

De hade enorma resurser.

Och de byggde många tekniker
som verkligen låg före sin tid.

<!-- S68 -->
Men Microsoft hade också
en överväldigande marknadsställning.

Och det skapade
ett farligt incitament.

<!-- S69 -->
Om nästan alla
använder din webbläsare,
varför vänta på standarder?

Varför inte helt enkelt införa
din egen lösning?

Ett tag fungerade det.

Tills resten av webben kom ikapp.

<!-- S70 -->
I dag är Internet Explorer borta.

De gamla webbläsarkrigen
känns som avlägsen historia.

Men titta på
dagens webbläsarmarknad.

Chrome.

Edge.

Opera.

Brave.

Vivaldi.

<!-- S71 -->
Och många andra
bygger på Chromium.

Olika produkter.

Ofta samma
motor under huven.

<!-- S72 -->
Så kanske har vi bytt bort det här.

En webbläsare som alla måste ta hänsyn till.

Mot det här.

En motor som alla bygger på.

Låter det bekant?

<!-- S73 -->
För en dominerande motor
avgör inte bara
hur webbplatser visas.

<!-- S74 -->
Den påverkar vad utvecklare bygger.

Vilka tekniker som blir populära.

Och i slutänden
vad webben själv blir.

<!-- S75 -->
Det finns dock
en mycket viktig skillnad.

Dagens webb vilar
på öppna standarder.

Firefox har fortfarande en egen motor.

Safari har WebKit.

Chromium är öppen källkod.

<!-- S76 -->
Och moderna webbläsare
uppdaterar sig själva.

Vi är långtifrån
situationen
från 2003.

<!-- S77 -->
Men grundfrågan kvarstår.

Hur mycket inflytande
bör ett enda företag ha
över en plattform
som nästan alla använder?

Det är frågan
som aldrig riktigt försvann.

<!-- S78 -->
Så var Internet Explorer 6 förfärlig?

Ja.

Ibland spektakulärt förfärlig.

<!-- S79 -->
Men det är inte hela historien.

Den var också en produkt av sin tid.

<!-- S80 -->
Problemet var
att Microsoft hade vunnit
webbläsarkrigen så fullständigt
att de kunde bestämma reglerna.

<!-- S81 -->
Och priset betalade webbutvecklarna.

De lärde sig hasLayouts
hemligheter.

De upptäckte att zoom: 1
kunde laga saker som genom magi.

Och de bad.

<!-- S82 -->
Och till slut blev Internet Explorer
det som den hade ägnat
tjugo år åt att skapa.

En förlegad plattform
som ingen längre ville
underhålla.

<!-- S83 -->
Webben förkastade inte
Microsofts vision.

Den byggde helt enkelt
en bättre version av den.

Och om den tiden
ska lära oss en sak,
så är det den här.

<!-- S84 -->
Teknik blir inte en standard
bara för att den är bra.

<!-- S85 -->
Ibland blir den en standard
för att ett företag har nog med makt
för att få alla att använda den.

<!-- S86 -->
Och ibland inser vi
tjugo år senare
att vi har gjort det igen.
