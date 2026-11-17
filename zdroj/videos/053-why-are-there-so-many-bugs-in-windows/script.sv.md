<!-- S01 -->
I september 2026 slog
en enda omgång Windows-uppdateringar
sönder fyra saker på en gång.

<!-- S02 -->
Ljudet slutade fungera.
Remote Desktop slutade fungera.
Delade mappar i virtuella maskiner
slutade fungera.

<!-- S03 -->
Och vissa datorer slutade lita på
företagsnätverket
de tillhörde,
så folk kunde inte logga in alls.

<!-- S04 -->
En omgång.
En tisdag.

<!-- S05 -->
Och om du tänker
att det här bara är ännu en
dålig Windows-uppdatering...

<!-- S06 -->
är det inte det.

<!-- S07 -->
För det här har hänt
om och om och om igen.

<!-- S08 -->
Så vad gör deras QA egentligen?

<!-- S09 -->
Hur kan ett så enormt företag
släppa en systemuppdatering
och missa något så uppenbart?

<!-- S10 -->
Vi börjar med den minsta saken.

<!-- S11 -->
Microsoft släppte en uppdatering
som ändrade ett par saker
i aktivitetsfältet.
Och strax därefter medgav de
att det fanns ett problem
med muspekarens inställningar.

<!-- S12 -->
För vissa gick en egen muspekare
tillbaka till en stor vit pil.
En sådan pil som får dig att kolla
om du råkat starta
en dator från 1998.

<!-- S13 -->
Din noga valda muspekare?
Borta.
Och att sätta tillbaka den
fungerade tydligen inte heller.

<!-- S14 -->
Nu tänker du kanske:
all mjukvara har buggar.
Precis.

<!-- S15 -->
Men det är skillnad på:
”Vi hittade ett sällsynt fel
under en ovanlig
hårdvarukonfiguration.”

<!-- S16 -->
Och:
”Efter vår uppdatering
ser muspekaren inte ut som
den muspekare du valde.”

<!-- S17 -->
För någon måste installera den.
Någon måste logga in.
Någon måste röra musen.
Och tydligen räckte inte det.

<!-- S18 -->
Sedan har vi ljudet.
Installera en uppdatering.
Starta om.
Inget ljud.

<!-- S19 -->
Vissa USB-ljudenheter slutar bara,
och Windows meddelar
att enheten inte kan startas.

<!-- S20 -->
Och ljud är knappast
en exotisk funktion.
Man skulle tro att ett av grundtesterna
för ett operativsystem vore:

<!-- S21 -->
får datorn fortfarande fram ett ljud?

<!-- S22 -->
Tydligen är det mer komplicerat
än det låter.
Bokstavligen.

<!-- S23 -->
Hemma är allt det här irriterande.
Muspekaren ser fånig ut.
Högtalarna är tysta.
Men du överlever.

<!-- S24 -->
Men en server som slutar lita på
nätverket den tillhör
betyder att ingen kan logga in,
och någon på IT-avdelningen
har en riktigt dålig morgon.

<!-- S25 -->
Och här slutar det vara
en samling roliga historier.

<!-- S26 -->
För vi kan titta i
Microsofts egen uppdateringshistorik.
Microsoft publicerar den.
Varje månad listar de
vad deras uppdateringar slog sönder.

<!-- S27 -->
Och om du radar upp
ett enda år av den listan
upprepas samma mönster
om och om igen.

<!-- S28 -->
Januari slog sönder ljudenheter
och webbkameror.
Februari fick muspekaren att snurra
så datorn såg ut att ha hängt sig.

<!-- S29 -->
Mars gav blåskärmar
och installationer
som fastnade halvvägs.
April slog sönder inloggning
med ansiktet.

<!-- S30 -->
I maj slutade Utforskaren
reagera på musen.
Och oktober slog sönder anslutningar
till din egen dator.

<!-- S31 -->
Inte internet.
Adressen som betyder ”den här datorn”.

<!-- S32 -->
Och två av dem
är verkligen anmärkningsvärda.

<!-- S33 -->
En uppdatering slog sönder knappen
som återställer datorn.
En annan tog återställningsskärmen,
där USB-möss och tangentbord
slutade svara.

<!-- S34 -->
Läs det en gång till.

<!-- S35 -->
Två gånger på tre månader
slog en uppdatering sönder verktyget
man lagar en trasig dator med.

<!-- S36 -->
Och en detalj till,
kanske den viktigaste.
Den där ljudbuggen, där Windows
säger att enheten inte kan startas?

<!-- S37 -->
Den dök upp i januari.
Och sedan dök den upp igen
tjugo månader senare.

<!-- S38 -->
Samma symtom.
Samma sorts enhet.
Samma meddelande.

<!-- S39 -->
Det är ingen historia
om att skriva dålig kod.
Det är en historia om testning.

<!-- S40 -->
Och inget av det här är nytt.

<!-- S41 -->
År 2024 kom en uppdatering
som gjorde att Linux slutade starta
på datorer med två system.
Felmeddelandet löd ordagrant:

<!-- S42 -->
”Något har gått
riktigt allvarligt fel.”

<!-- S43 -->
Vilket ärligt talat är det mest träffsäkra
felmeddelande Windows någonsin visat.

<!-- S44 -->
Och 2018 fanns en version
som måste dras tillbaka helt,
efter att folk rapporterat
att deras filer var borta.

<!-- S45 -->
Så vid det här laget
kan du rimligen dra slutsatsen:
Microsoft är helt enkelt inte bra
på att skriva mjukvara.

<!-- S46 -->
Och det skulle förklara allt.
Buggarna.
Regressionerna.
Uppdateringarna som lagar en sak
och slår sönder en annan.

<!-- S47 -->
Men det finns ett problem
med den förklaringen.
Microsoft gör inte bara Windows.

<!-- S48 -->
De gör Office.
Visual Studio.
Exchange.
Teams.
Och ett väldigt stort moln.

<!-- S49 -->
Och allt det har haft
egna buggar, egna regressioner
och egna spektakulära avbrott.

<!-- S50 -->
Och det spelar roll.
För den vanliga förklaringen till
Windows är att det bär på
trettio år av gammal kod.

<!-- S51 -->
En modern molntjänst
bär inte på trettio år
av någonting alls.
Den byggdes nyligen,
av folk som visste
vad de byggde.

<!-- S52 -->
Och den går sönder ändå.

<!-- S53 -->
Så problemet var aldrig
bara gammal kod.
Problemet är komplexitet
i Microsofts skala.

<!-- S54 -->
Och Windows är stället
där den komplexiteten
syns allra bäst.

<!-- S55 -->
För Windows är egentligen inte
ett operativsystem.
Längst ner finns en arkitektur
som går tillbaka till tidigt nittiotal.

<!-- S56 -->
Sedan årtionden av gränssnitt.
Sedan kompatibilitetslager.
Sedan drivrutiner.
Sedan tjänster.

<!-- S57 -->
Sedan nyare ramverk,
byggda ovanpå äldre ramverk.
Sedan ett nytt utseende.
Sedan ännu ett nytt utseende.

<!-- S58 -->
Det är mindre ett operativsystem
och mer en arkeologisk utgrävning
som på något sätt fortfarande går.

<!-- S59 -->
Och Microsoft får inte
röja platsen,
för företag är beroende
av det som ligger under.
Det finns en hel video om just det.

<!-- S60 -->
Det som spelar roll här
är vad det gör med buggar.
Varje lager måste fortsätta fungera
med varje lager under sig.

<!-- S61 -->
Så en ändring här uppe
kan slå sönder något
ingen har tittat på på flera år.

<!-- S62 -->
Och det finns en ledtråd till
om hur det går till,
och den handlar inte om buggar alls.

<!-- S63 -->
Det är ett mönster.
Microsoft tar bort något.
Användarna klagar.
Microsoft tar flera år
på sig att ompröva det.

<!-- S64 -->
Och under tiden
bygger någon annan ett verktyg
som sätter tillbaka det.

<!-- S65 -->
Och det roliga är
att det inte handlar om
några obskyra hobbyprojekt.

<!-- S66 -->
Det finns hela program
vars enda uppgift är att få Windows
att bete sig mer som...

<!-- S67 -->
ja...
Windows.

<!-- S68 -->
De tar tillbaka en äldre Startmeny.
De återställer aktivitetsfältet.
De ändrar hur Utforskaren beter sig.

<!-- S69 -->
Och vissa ger dig mer kontroll
över Windows än Windows själv gör.

<!-- S70 -->
Microsoft har ett enormt antal
ingenjörer som jobbar med systemet.
Och så säger någon utanför företaget:
okej.
Jag sätter tillbaka fältet själv.

<!-- S71 -->
Och nu har något annat ändrats.
Microsoft använder alltmer AI
i hur deras mjukvara skrivs.

<!-- S72 -->
Deras egen vd har sagt
att tjugo till trettio procent
av koden i deras källkodsarkiv
numera skrivs av mjukvara.

<!-- S73 -->
Och det borde betyda
högre produktivitet.
Fler buggfixar.
Snabbare utveckling.

<!-- S74 -->
Men det finns en uppenbar flaskhals.
Att skriva kod kan bli snabbare.

<!-- S75 -->
Att testa ett enormt gammalt system
blir inte nödvändigtvis snabbare.

<!-- S76 -->
Och om du kan producera ändringar
snabbare än du hinner testa
hur de samverkar
med årtionden av befintlig kod...

<!-- S77 -->
blir resultatet kanske bara att du
producerar regressioner snabbare.

<!-- S78 -->
Och här gäller det att vara försiktig.
Den siffran gäller hela Microsoft,
inte Windows i synnerhet.
Och ingen har visat
att AI orsakat någon av buggarna.

<!-- S79 -->
Kanske gjorde AI inte Microsoft
sämre på att testa.

<!-- S80 -->
Kanske gjorde den bara
det befintliga problemet snabbare.

<!-- S80b -->
Förresten, om du vill se
vart resten av det här leder,
överväg att prenumerera.

Det hjälper kanalen på riktigt.

<!-- S81 -->
Det mesta av videon har hävdat
att Microsoft har
ett verkligt kvalitetsproblem.
Och det argumentet håller.

<!-- S82 -->
Men här kommer den delen
som överraskar folk.
Varför skulle kärnan
ändå vara annorlunda?

<!-- S83 -->
För nästan allt
som beskrivits hittills
är inte kärnan.

<!-- S84 -->
Muspekaren.
Aktivitetsfältet.
Startmenyn.
Inställningarna.
Återställningsskärmen.

<!-- S85 -->
Allt det ligger ovanpå.

<!-- S86 -->
Kärnan är delen under.
Den avgör vilket program
som körs på vilken processorkärna.
Den delar ut minne.
Den pratar med hårdvaran.

<!-- S87 -->
Och om den delen gick riktigt fel,
är symtomet inte
en fånig muspekare.

<!-- S88 -->
Symtomet är en maskin
som stannar, förstör dina data
eller tyst släpper in någon.

<!-- S88b -->
Och kärnan har något
som resten av Windows inte har.
Hårda begränsningar.

<!-- S88c -->
En schemaläggare kan inte bestämma
sig för att bete sig annorlunda
för att någon ritat om
Startmenyn.

<!-- S88d -->
Minneshantering kan inte moderniseras
genom att flytta en knapp.
Och en drivrutin får inte anta
att hårdvaran uppför sig snällt.

<!-- S88e -->
Och framför allt: kärnan har ingenstans
att gömma ett misstag bakom
en lite förvirrande inställningssida.

<!-- S88f -->
Vilket är ett skäl att misstänka
att det är en helt annan
teknisk historia
än resten av Windows.

<!-- S89 -->
Men misstanke är inte bevis.
Så titta på vad den här saken
faktiskt har fått stå ut med.

<!-- S90 -->
Arkitekturen längst ner är gammal.
Väldigt gammal.
Och den överlevde.

<!-- S91 -->
Den blev Windows 2000.
Sedan XP.
Sedan Vista.
Sedan 7, 8, 10 och 11.

<!-- S92 -->
Processorerna ändrades.
Antalet kärnor exploderade.
Minnesstorlekarna exploderade.
Virtuella maskiner gick från exotiska
till helt normala.

<!-- S93 -->
Och samma familj av kod
hamnade på servrar
över hela världen.

<!-- S94 -->
Filservrar.
Företagsinloggningar.
Virtuella maskiner.
Arbetsbelastningar ingen tänkte på
när det konstruerades.

<!-- S95 -->
Om delen som avgör
vad som körs när,
och som delar ut minnet,
vore hopplöst trasig...
vore notan omöjlig att dölja.

<!-- S96 -->
Nu ett ärligt medgivande.
Ingen utanför Microsoft kan läsa
källkoden till dagens kärna,
så ingen kan kalla den vacker.

<!-- S96b -->
Men en äldre version
tittade faktiskt någon på.

<!-- S96c -->
Delar av källkoden till Windows 2000
läckte 2004,
och förra året gick en forskare
igenom den.

<!-- S96d -->
Fynden var inte smickrande.
Buggar som satt i den koden
i sexton år
innan någon lappade dem.

<!-- S96e -->
Men det är farfar
till dagens kärna,
och bara en bråkdel läckte.
Det säger något om 2000,
inte om nu.

<!-- S97 -->
Och att överleva är inte samma sak
som att vara utmärkt.

<!-- S98 -->
Så det här är inget påstående
om att Windows kärna är genial.
Det vet ingen.

<!-- S99 -->
Men vi har årtionden av belägg
för att den klarar sitt jobb.

<!-- S100 -->
Och det är en mycket märkligare slutsats
än ”Windows är dåligt”.

<!-- S101 -->
För det betyder att svaret
på ”vad gör deras QA”
antagligen inte är
”Microsoft kan inte skriva mjukvara”.

<!-- S102 -->
Det är att de i årtionden
byggt nytt ovanpå gammalt,
utan att någonsin få
kasta bort det gamla.

<!-- S103 -->
Resultatet är enormt.
Kraftfullt.
Kompatibelt.
Och emellanåt löjligt.

<!-- S104 -->
Du installerar en uppdatering.
Ljudet försvinner.
Muspekaren ser ut som Windows 98.

<!-- S105 -->
Och under alltihop
avgör något i tysthet
vilket program som körs härnäst.
Delar ut minne.
Pratar med hårdvaran.

<!-- S106 -->
Gör precis det
den ska göra.

<!-- S107 -->
Åtminstone...
tror vi det.

<!-- S108 -->
För till skillnad från aktivitetsfältet...
ser vi den inte.
