<!-- S01 -->
Du öppnar en terminal.
Någon går förbi.
De ser en svart skärm
täckt av mystisk text.
Och plötsligt...

<!-- S02 -->
"Herregud! Du hackar!"

<!-- S03 -->
Tja...
Kanske.
Eller så försöker du bara ta reda på
varför servern ligger nere.

<!-- S04 -->
I dag ska vi titta på varför
terminaler och hackning har blivit
nästan samma sak i populärkulturen.
Och, ännu viktigare...
hur hackning faktiskt ser ut.

<!-- S05 -->
För de flesta har en dator knappar.
Du klickar på något.
Något händer.
Sedan finns terminalen.
Inga knappar.
Inga vänliga meddelanden.
Bara det här.
Och det är skrämmande.

<!-- S06 -->
Ett grafiskt gränssnitt kan säga:
ta bort användare.
En terminal säger det här i stället.

<!-- S07 -->
För en van Linux-användare
är det fullkomligt vardagligt.
För alla andra ser det ut
som att du ska avfyra en robot.

<!-- S08 -->
Det finns faktiskt ett historiskt skäl
till att det ser ut så.
Tidiga datorer hade inget grafiskt gränssnitt.
Man talade med dem via textterminaler.

<!-- S09 -->
Och de terminalerna hade mörka skärmar
med grön eller bärnstensfärgad fosfor.
Det var inget försök att se häftigt ut.
Det var helt enkelt så tekniken fungerade.

<!-- S10 -->
Men sedan märkte film och television
något användbart.
En svart skärm full av
snabbt växlande text ser teknisk ut.
Och, ännu viktigare...
den ser komplicerad ut.

<!-- S11 -->
Du behöver inte förstå
vad tecknen betyder.
Du ser bara det här.
Och hjärnan bestämmer:
den här personen gör något olagligt.

<!-- S12 -->
Hollywood har utvecklat ett anmärkningsvärt
enhetligt språk för hackning.
Hackaren sitter i ett mörkt rum.
Det finns sex skärmar.

<!-- S13 -->
Rummet lyses upp enbart av skärmarna.
Ingen har tänt lamporna.
Hackaren börjar skriva
i ungefär niohundra ord i minuten.

<!-- S14 -->
Text flyger över skärmen.
En förloppsindikator dyker upp.
Nittiosju procent.
Nittioåtta.
Nittionio.
Och till sist, hundra.
Hackaren lutar sig bakåt.
Och säger...

<!-- S15 -->
"Jag är inne."

<!-- S16 -->
Så fungerar inte de flesta
säkerhetsincidenter.
Låt oss föreställa oss det riktiga samtalet.
"Nu ska jag hacka den här servern."
Och servern svarar:
permission denied.

<!-- S17 -->
"Jaha."
Försöker igen.
Permission denied.
Kontrollerar lösenordet.

<!-- S18 -->
Läser dokumentationen.
Söker på felmeddelandet.
Upptäcker till slut att administratören
stängde av lösenordsinloggning för ett halvår sedan.

<!-- S19 -->
"Just det."

<!-- S20 -->
Datorer är anmärkningsvärt bra på att få dig
att lägga tjugo minuter på att upptäcka att du
glömde ett enda tecken i en konfigurationsfil.

<!-- S21 -->
På ena sidan av skärmen:
systemadministratör.
På den andra:
hackare.
Samma verktyg kan finnas på båda.
Det beror på att terminalen
inte är ett hackningsverktyg.
Den är ett gränssnitt.

<!-- S22 -->
Du kan använda den för att driva en server,
läsa loggar, kopiera filer, installera program,
eller lista ut vad som gick sönder klockan tre på natten.

<!-- S23 -->
Eller, beroende på vad du gör
och om du har tillstånd,
kan du använda den för säkerhetstestning.
Eller för ett angrepp.

<!-- S24 -->
Verktyget självt talar inte om
vilket av det du gör.
En skruvmejsel kan laga en dator.
Den kan också förstöra en.
Skruvmejseln är inte brottslingen.

<!-- S25 -->
Så vad är egentligen en hackare?
Ordet har en mycket äldre historia
än modern it-brottslighet.

<!-- S26 -->
Ursprungligen var en hackare någon
som tyckte om att utforska system
och kunde hitta oväntade lösningar.

<!-- S27 -->
Med tiden fastnade ordet
vid datasäkerhet.
Och i dag, när någon säger
"han är en hackare", kan de mena

<!-- S28 -->
en säkerhetsforskare,
en penetrationstestare,
en verklig angripare,
eller helt enkelt någon som kan
oroväckande mycket om Linux.
Oftast hjälper sammanhanget.

<!-- S29 -->
Låt oss titta på vår bild igen.
Bildtexten säger:
du hackade det.
Och titta på hennes skärmar.

<!-- S29b -->
På den ena, något som liknar nmap.
På den andra, något som ser
ännu mer misstänkt ut.
Snedstreck etc snedstreck passwd.

<!-- S30 -->
För någon som inte kan Linux
bryter hon sig uppenbart in i Pentagon.
För en systemadministratör kontrollerar hon
nätverket och läser en lista över konton.

<!-- S31 -->
Och det är där skämtet kommer ifrån.
Kvinnan kanske inte hackar någonting alls.
Hon kanske bara gör sitt jobb.

<!-- S32 -->
Så vad gör nmap egentligen?
Det är ett verktyg för nätverkskartläggning
och säkerhetsgranskning.

<!-- S33 -->
Mycket förenklat:
du riktar det mot en maskin och frågar
vad den här datorn
exponerar mot nätverket.

<!-- S34 -->
Det kan tala om att vissa portar är öppna.
Och portar motsvarar nätverkstjänster.
Det är inte automatiskt ett angrepp.

<!-- S35 -->
Det liknar mer att titta på en byggnad
och fråga vilka dörrar som står öppna.
Om det är din byggnad
är det vanlig administration.

<!-- S36 -->
Om den är någon annans
och du medvetet
letar efter en väg in...

<!-- S37 -->
ja, då är det en annan sak.

<!-- S38 -->
Och vad gäller den där sökvägen?
Någon kanske tänker:
hon läser lösenordsfilen.
Den innehåller information om konton.

<!-- S39 -->
Men på ett modernt Linux-system
lagras de faktiska lösenordshasharna någon annanstans.
De ligger i snedstreck etc snedstreck shadow,
som är mycket hårdare skyddad.

<!-- S40 -->
Att se den filen är alltså inte samma sak
som att upptäcka allas lösenord.
Hollywood skulle förstås
göra det här mycket mer dramatiskt.

<!-- S41 -->
En Linux-administratör skulle säga:
det är bokstavligen en lista över användare.

<!-- S42 -->
En annan klassisk scen knäcker ett lösenord
på ungefär fjorton sekunder.
Verklig knäckning är tråkigare.
Du har en hash, du har en ordlista,
och du låter datorn pröva kandidater.

<!-- S43 -->
Kanske hittar den ett på en minut.
Kanske på en vecka.
Kanske aldrig.
Och medan den arbetar sitter angriparen
inte där och skriver.
Han kanske äter en smörgås.

<!-- S44 -->
Vilket för mig till min favorit
bland Hollywoods traditioner.
Datorer accepterar tydligen inte kommandon
om du inte skriver dem extremt snabbt.

<!-- S45 -->
Riktiga programmerare och administratörer
skriver inte hela tiden.
De tänker.
De läser.
De stirrar på ett felmeddelande.

<!-- S46 -->
Sedan upptäcker de att någon
löste det för elva år sedan.
Och så kopierar de lösningen.

<!-- S47 -->
Det är datavetenskap.

<!-- S48 -->
Ibland är det farligaste
du kan skriva inte
något mystiskt hackningskommando.
Det är något fullkomligt legitimt.

<!-- S49 -->
Det berömda exemplet är det här.

<!-- S50 -->
Vilket är en underbar historia,
förutom att ett modernt system vägrar.
Det svarar att en rekursiv operation
på snedstreck är farlig,
om du inte lägger till en flagga om att du menar det.

<!-- S51 -->
Kommandona som verkligen förstör saker
är tråkigare.
En radering i fel katalog.
En disk som skrivs över fel disk.

<!-- S52 -->
Om dem varnar terminalen dig inte,
för såvitt den kan se
är ingenting fel.
Den kan bara fråga: är du helt säker?

<!-- S53 -->
Och om du svarar ja...
kan den tro dig.

<!-- S54 -->
Och här är det största problemet
med Hollywood-stereotypen.
Ett verkligt angrepp kanske inte alls
ser ut som hackning.

<!-- S55 -->
Det kan handla om ett stulet lösenord.
Nätfiske.
En opatchad server.
En läckt API-nyckel.
Ett lösenord återanvänt från något annat.

<!-- S56 -->
Angriparen behöver kanske inte ens
en terminal.
Han kanske bara loggar in
i ett webbgränssnitt.
Användarnamn.
Lösenord.
Och nu är han inne.

<!-- S57 -->
Ingen grön text.
Ingen grafik i Matrix-stil.
Ingen dramatisk musik.

<!-- S58 -->
Vilket nog är betydligt läskigare.

<!-- S59 -->
Folk föreställer sig en hackare som en huvtröja,
ett mörkt rum och ett lysande tangentbord.
Inget av det har med hackning att göra.

<!-- S60 -->
Personen bredvid dig på tåget,
med en helt vanlig bärbar dator,
kan kunna betydligt mer
om datasäkerhet.

<!-- S61 -->
Och personen som sitter
framför sex servrar
försöker kanske bara lista ut
varför databasen inte startar.

<!-- S62 -->
Så låt oss återvända till vår ursprungliga bild.
Mannen pekar på kvinnan.
Du hackade det.
Hackade hon?

<!-- S63 -->
Kanske.
Kanske inte.

<!-- S64 -->
Hon har en terminal.
Hon har nmap.
Hon har en lista över konton.
Men inget av det bevisar
att hon har hackat någonting.
Hon kan vara administratören
eller göra en säkerhetsgranskning.

<!-- S65 -->
Eller så hackar hon faktiskt.
Vi vet inte.
Och det är poängen.

<!-- S66 -->
Den verkliga skillnaden mellan
vanlig administration och hackning
är inte färgen på din terminal.
Den är inte hur många skärmar du har.

<!-- S67 -->
Den är inte hur snabbt du skriver.
Och den är definitivt inte
om du har huvtröja på dig.
Den är vad du gör
och om du har tillstånd att göra det.

<!-- S68 -->
Så nästa gång du ser någon
stirra på en svart skärm
full av mystisk text,
anta inte att de hackar.

<!-- S69 -->
De kanske bara lagar servern.

<!-- S70 -->
Fast...
om de skriver niohundra ord
i minuten och samtidigt ropar
"jag är inne"...

<!-- S71 -->
kan det vara värt att fråga
vad de håller på med.
