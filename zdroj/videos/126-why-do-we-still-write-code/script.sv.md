<!-- S01 -->
Här är ett komplett krav
på ett affärssystem.
En användare kan avbryta en beställning.

<!-- S02 -->
Sex ord.
Varje utvecklare skulle nicka.
Varje kund skulle skriva under.

<!-- S03 -->
Kan en användare alltså avbryta en beställning
efter att fakturan har gått iväg?
Efter att den har skickats?

<!-- S04 -->
Avbryts då också
reservationen hos leverantören?
Och om en person avbryter
och en annan godkänner samma beställning
i samma sekund?

<!-- S05 -->
Meningen svarar inte på något av det.
Koden måste svara på allt.
Och det glappet, mellan meningen
och koden, är vad programmerare
egentligen får betalt för.
I alla fall förr.

<!-- S06 -->
I dag finns det en lockande idé.
Skriv bara meningarna.
Spara dem i dokument,
granska dem, versionshantera dem.
Och låt en AI skriva koden.

<!-- S07 -->
Specifikationen blir
källkoden.
Koden blir det som assembler
är i dag: något som körs,
och som ingen läser.

<!-- S08 -->
Det är en bra idé.
Men den är inte ny.

<!-- S09 -->
I nästan sjuttio år har människor försökt
höja den nivå
där vi talar om för datorer vad de ska göra.
Verktygen var olika,
och det var deras mål också.
Men vart och ett flyttade mer av arbetet
från människor till maskiner.

<!-- S10 -->
År 1957 publicerade ett team på IBM
en artikel om FORTRAN.
I titeln kallades det
ett automatiskt kodningssystem.

<!-- S11 -->
På den tiden var det en träffande benämning.
Man skrev formler,
och maskininstruktionerna,
den del som människor hade skrivit för hand,
producerades nu av maskinen.

<!-- S12 -->
I dag kallar vi FORTRAN för kod.

<!-- S13 -->
På 1980-talet gick CASE-verktyg
och fjärde generationens språk
en nivå högre.
Rita diagrammen, fyll i formulären,
så genereras en stor del
av applikationen åt dig.

<!-- S14 -->
År 2001 lanserade Object Management Group,
organisationen bakom UML,
Model Driven Architecture.

<!-- S15 -->
Löftet kommer att låta bekant.
Du beskriver systemet en gång,
som en modell, oberoende av all teknik.
Sedan genererar verktyg implementationen
för vilken plattform du än behöver.

<!-- S16 -->
Samma affärsregler.
Utbytbar teknik.

<!-- S17 -->
Och 2014 gav analytikerna på Forrester
ett namn åt plattformar
för att bygga affärsapplikationer
med så lite handskriven kod
som möjligt.
De kallade det low-code.

<!-- S18 -->
Fungerade något av det, då?

<!-- S19 -->
Delvis.
År 2014 publicerade forskare vid Lancaster University
en enkätstudie
bland 450 personer
som faktiskt använde
modelldriven utveckling.

<!-- S20 -->
Det fungerade,
och i större utsträckning än många trodde.
Men sällan för ett helt system.
Man använde det för centrala delar
och byggde resten på andra sätt.

<!-- S21 -->
De största hindren de fann
var människor och organisationer,
inte verktyg.
Men det finns också en teknisk gräns,
och programmerare har ett skämt om den.

<!-- S22 -->
En specifikation som är exakt nog
för att generera hela programmet ur...
har redan ett namn.
Den kallas kod.

<!-- S23 -->
För att generera allt
var modellen tvungen att säga allt.
Varje tillstånd, varje undantag,
varje ”tänk om två personer gör det samtidigt”.

<!-- S24 -->
Då har du
inte kommit undan programmeringen.
Du har bara flyttat in den i ett diagram,
som ofta är svårare att läsa,
att jämföra och att granska.

<!-- S25 -->
Redan i slutet av 1970-talet
sammanfattade Edsger Dijkstra den andra halvan
i en kort text med en rättfram titel.
Om dårskapen
i att programmera på naturligt språk.

<!-- S26 -->
Hans poäng var att formell notation
inte är en börda som vi får stå ut med.
Han kallade den ett otroligt effektivt verktyg
för att utesluta allt möjligt nonsens.

<!-- S27 -->
Vanligt språk utesluter det inte.
Det döljer det.
En användare kan avbryta en beställning.

<!-- S28 -->
Så om inget av det ersatte kod,
varför försöka igen?

<!-- S29 -->
För att en sak verkligen är annorlunda.

<!-- S30 -->
Äldre generatorer kunde inte fylla ett glapp
på egen hand.
Om modellen inte sa vad som händer
med en skickad beställning,
fick någon lägga till den regeln uttryckligen.
Tills dess fanns glappet kvar,
och det gick att hitta.

<!-- S31 -->
En AI stannar inte.
Ge den kravet på sex ord,
så svarar den på varje fråga
som vi ställde i början.

<!-- S32 -->
Den bestämmer att en skickad beställning
kan avbrytas. Eller att den inte kan det.
Den bestämmer om fakturan
och om leverantören.
Den skriver kod som körs,
ser rimlig ut
och klarar de tester den själv har skrivit.

<!-- S33 -->
Det är precis det som gör den användbar.
Och precis det som gör den farlig.
För en trovärdig gissning
är inte ett affärsbeslut.

<!-- S34 -->
Förr var glappen fel.

<!-- S35 -->
Nu är de beslut
som ingen märkte att någon fattade.

<!-- S36 -->
Så om specifikationen verkligen
ska bli källkoden,
kan den inte vara några löst skrivna stycken.

<!-- S37 -->
Föreställ dig repot.
Ett dokument beskriver beställningar
och alla tillstånd de kan befinna sig i.
Ett annat säger vem som får godkänna dem,
och vem som får avbryta dem.

<!-- S38 -->
Ett tredje säger när en faktura utfärdas,
och när den måste krediteras.
Ett annat beskriver bokföringssystemet,
inklusive vad som händer när det ligger nere.

<!-- S39 -->
En del är vanlig löptext.
Men överallt där texten skulle bli tvetydig
finns något striktare:
en lista över tillstånd och övergångarna mellan dem,
ett schema, en regel som en maskin kan kontrollera.

<!-- S40 -->
Och bredvid det acceptanstester
som säger exakt vad som måste hända.

<!-- S41 -->
Allt ligger i Git.
Ändringar granskas.
Varje krav kan spåras
till testet som kontrollerar det.

<!-- S42 -->
Hur ser då en ändring ut?
Säg att kunden bestämmer
att en skickad beställning ändå kan avbrytas,
så länge den inte har levererats.
Och då måste fakturan krediteras.

<!-- S43 -->
Ingen öppnar backenden.
En utvecklare ändrar en enda regel
i dokumentet om beställningar.

<!-- S44 -->
Sedan letar systemet upp
allt som regeln berör.
Beställningens tillstånd.
Fakturareglerna.
Testerna för avbeställning.
Reservationen hos leverantören.

<!-- S45 -->
Och där borde det stanna och fråga.
Specifikationen sa aldrig
vad som händer med en reservation hos leverantören
när varorna väl är på väg.
Det är ett beslut,
så det går tillbaka till en människa.

<!-- S46 -->
Först då genereras
den nya implementationen.
Och den kontrolleras åt båda hållen.
Testerna för den nya regeln ska gå igenom.
Och alla andra tester ska fortfarande gå igenom,
oförändrade.

<!-- S47 -->
För en ändring av hur man avbryter
får inte i tysthet ändra något annat.
Fast godkända tester visar bara
det som testerna kontrollerar.

<!-- S48 -->
Och eftersom reglerna
inte är knutna till tekniken,
skulle samma specifikation kunna ge
en PHP-applikation i dag
och något helt annat i morgon.

<!-- S49 -->
Vilket är precis vad
Model Driven Architecture lovade
för tjugofem år sedan.
Skillnaden är att den här gången
kan generatorn vara bra nog.

<!-- S50 -->
Då återstår den svåraste frågan.
Hur vet du att AI:n
faktiskt följde specifikationen?

<!-- S51 -->
Kod som fungerar i vanliga situationer
kan ändå fallera i ovanliga.
Och de ovanliga är precis
de fall som ingen kommer på att testa.

<!-- S52 -->
Amazon stötte på det här
i sina egna molnsystem.
År 2014 beskrev företagets ingenjörer
hur de hade börjat skriva
exakta, matematiska beskrivningar
av sina designer,
i ett språk som heter TLA+.

<!-- S53 -->
Inte av koden. Av själva designen.
Ett verktyg tog sedan en modell av systemet,
begränsad till en fast storlek,
och provade alla möjliga ordningsföljder
för haverier och återställningar.

<!-- S54 -->
I DynamoDB, Amazons databastjänst,
hittade det en bugg som kunde leda till dataförlust.

<!-- S55 -->
Det kortaste sättet att utlösa den
krävde 35 steg,
i exakt rätt ordning.
Buggen hade klarat designgranskningar,
kodgranskningar och tester.

<!-- S56 -->
Så den ärliga versionen av idén
är inte att AI skriver koden
och vi litar på den.
Den är att AI skriver koden
och något oberoende kontrollerar den.

<!-- S57 -->
Titta nu på vad vi har byggt.

<!-- S58 -->
Exakta tillstånd.
Formella regler.
Kontrollerbara tester.
Versionshanterat, granskat, sparat i ett repo.

<!-- S59 -->
Det ser inte ut som
slutet på programmering.
Det ser ut som programmering,
i ett nytt språk.

<!-- S60 -->
Och det är vad som hände varje gång.
FORTRAN var automatisk kodning,
tills det blev koden.
Varje gång maskinen tog över
”hur”, flyttade människor upp till ”vad”.

<!-- S61 -->
Och ”vad” var alltid det svåra.
Inte att skriva, utan att bestämma.
Vad som händer med en skickad beställning.
Vem som får röra vilka data.
Vad systemet aldrig får göra.

<!-- S62 -->
Kanske kommer framtidens programmerare
inte att skriva tusentals rader kod.

<!-- S63 -->
Men någon kommer fortfarande att behöva förstå
ett problem tillräckligt väl för att kunna säga
exakt vad en dator måste göra,
och kontrollera att den gjorde det.

<!-- S64 -->
Och om specifikationen
blir källkoden,
kanske den viktigaste färdigheten
inte längre är att veta
hur man skriver ett program.

<!-- S65 -->
Den kanske är att veta
hur man beskriver ett.

<!-- S66 -->
Så här kommer frågan
som jag gärna vill höra ditt svar på.
Om du skriver en specifikation
så exakt
att en maskin kan bygga utifrån den...
programmerar du då fortfarande?
