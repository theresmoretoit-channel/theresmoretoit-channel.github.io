<!-- S01 -->
Med några dagars mellanrum dyker en ny allvarlig bugg
upp i nyheterna.
En bugg som låter någon hoppa över inloggningen.
En bugg som läcker privata data.
En bugg som ger en angripare kontroll över din dator.

<!-- S02 -->
Ibland är det Windows. Ibland Linux.
En webbläsare, en databas, en molntjänst...
eller ett litet bibliotek
som miljoner utvecklare är beroende av.

<!-- S03 -->
Och reaktionen är nästan alltid densamma.
Hur kunde programmerarna missa det här?

<!-- S04 -->
Det här är proffs.
De har kodgranskningar, automatiska tester,
säkerhetsgranskningar, fuzzing...
och ändå fortsätter buggarna att komma.

<!-- S05 -->
Så är det ens möjligt
att skriva komplex programvara utan buggar?

<!-- S06 -->
Låt oss börja med ett tal.
Tänk dig ett program med bara hundra inställningar,
var och en antingen på eller av.

<!-- S07 -->
Hundra enkla ja-eller-nej-beslut.
Hur många kombinationer är det?

<!-- S08 -->
Två upphöjt till hundra.
Det är ungefär en miljon biljoner biljoner.

<!-- S09 -->
Tänk dig nu att du kunde testa
en miljard kombinationer varje sekund.
Och att du började vid Big Bang.

<!-- S10 -->
Fram till idag skulle du ha testat
ungefär en kombination av tretusen.

<!-- S11 -->
Och hundra brytare är ingenting.
Ett riktigt program har miljoner av dem.
Så att "bara testa allt"
är inte dyrt. Det är omöjligt.

<!-- S12 -->
Och de där brytarna är inget exotiskt.
Ta en av de enklaste sakerna
ett program någonsin gör.
En användare ber om sitt konto med dess nummer.
Vi hittar det i databasen.
Vi skickar tillbaka det.

<!-- S13 -->
Men tänk om användaren inte finns?
Tänk om någon skickar text i stället för ett nummer?
Eller ett negativt tal? Eller ett enormt?

<!-- S14 -->
Tänk om den här personen inte får se det?
Tänk om någon raderar kontot
i exakt det ögonblick vi laddar det?
Tänk om samma förfrågan kommer två gånger?

<!-- S15 -->
Var och en av de här frågorna är enkel.
Problemet är hur de kombineras.
Var och en är ännu en brytare.

<!-- S15b -->
Förresten, om du gillar sådana här
videor, prenumerera gärna.

Det hjälper kanalen på riktigt.

<!-- S16 -->
Och en dator reder inte ut det åt oss.
Den gör exakt det vi säger åt den.
Inte det vi menade.

<!-- S17 -->
Det är därför vi uppfann programmeringsspråk.
De låter oss beskriva komplexa saker
utan att tänka på varje detalj.

<!-- S18 -->
Men vissa av dem sköter mindre
än man skulle hoppas.
Ta C. Det är snabbt, det är enkelt,
och det ger dig enorm kontroll över minnet.

<!-- S19 -->
Så du kan skriva det här.
Vi reserverar plats för sexton tecken.
Sedan säger vi: kopiera indatan hit.

<!-- S20 -->
Tänk om indatan är
femhundra tecken lång?
C frågar inte.
Det bara fortsätter skriva förbi slutet.

<!-- S21 -->
Och vad ligger precis efter de där sexton tecknen?
Ofta något mycket viktigt.

<!-- S22 -->
När ett program anropar en funktion
antecknar det vart det ska tillbaka
när funktionen är klar.
En returadress.
Med en klassisk minneslayout ligger den
en bit efter slutet på vår buffert.

<!-- S23 -->
Så en angripare skickar en indata
av exakt rätt längd.
Först sina egna instruktioner.
Sedan, allra sist, en ny returadress...
som pekar tillbaka på de instruktionerna.

<!-- S24 -->
Funktionen avslutas.
Processorn slår upp vart den ska återvända...
och hoppar rakt in i angriparens kod.

<!-- S25 -->
Nu kör den deras program,
med samma behörigheter som ditt program.
Det är vad "köra godtycklig kod" betyder.

<!-- S26 -->
Och processorn gjorde inget fel.
Den följde instruktionerna.

<!-- S27 -->
År 1988 lät ett misstag precis som det här
Morris-masken sprida sig
över det tidiga internet.
Och samma trick har använts
i attacker ända sedan dess.

<!-- S28 -->
Så nyare språk lämnar en del av jobbet
till kompilatorn.
Rust, till exempel, vägrar att bygga
många program som skulle kunna hantera minnet fel.

<!-- S29 -->
Programmeraren säger:
men jag vet precis vad jag gör!
Och kompilatorn säger:
det säger alla.

<!-- S30 -->
Och det är rätt att vara misstänksam.
Microsoft och Googles Chrome-team
har båda rapporterat
att omkring sjuttio procent
av de säkerhetsbuggar de studerat
kommer från problem med minnessäkerhet.

<!-- S31 -->
Men ett program kan vara helt minnessäkert
och ändå fullständigt fel.

<!-- S32 -->
Tänk dig att en användare loggar in.
Lösenordet kontrolleras korrekt.
Inget kraschar. Inget minne blir korrupt.

<!-- S33 -->
Och sedan visar programmet dem
någon annans data.
För att behörighetskontrollen
skrevs lite fel.

<!-- S34 -->
Inget språk kan fånga det på egen hand.
Språket vet inte
vad programmet var tänkt att göra.
Bara vi vet det.

<!-- S35 -->
Så tillbaka till testning.
Ett test kan säga dig:
för den här indatan fick jag det här resultatet.

<!-- S36 -->
Det kan inte säga dig:
programmet är rätt för varje indata.
Och vi har redan sett
varför vi inte kan pröva alla.

<!-- S37 -->
År 1970 sammanfattade datavetaren
Edsger Dijkstra det i en mening.
Testning kan visa att buggar finns,
men aldrig att de saknas.

<!-- S38 -->
Okej. Så i stället för att testa,
varför inte skriva ett program
som kontrollerar andra program
och bevisar att de är korrekta?
Mata in vilken kod som helst, så talar det om
huruvida koden gör det den ska.

<!-- S39 -->
Den frågan besvarades
innan den första riktiga datorn ens var byggd.
År 1936 bevisade Alan Turing
att ett sådant program inte kan finnas.

<!-- S40 -->
Inte att ingen har byggt det ännu.
Att det inte kan finnas alls.

<!-- S41 -->
Han visade att inget program kan avgöra,
för varje annat program,
om det någonsin kommer att stanna.

<!-- S42 -->
Och 1953 gick Henry Rice ännu längre.
Detsamma gäller varje icke-trivial fråga
om vad ett program faktiskt gör.

<!-- S43 -->
Är det säkert? Läcker det data?
Ger det rätt svar?
Det finns ingen allmän metod
som avgör det för varje program.

<!-- S44 -->
Så är buggfri programvara omöjlig?
Inte riktigt.
För ett enda specifikt program
kan man ibland bevisa att det är korrekt,
med enorm möda.

<!-- S45 -->
År 2009 bevisade ett team i Australien
att en liten operativsystemskärna,
kallad seL4,
gör exakt vad dess specifikation säger.

<!-- S46 -->
Den hade under tiotusen rader kod.
Att bygga kärnan tog
ungefär två personår.
Att bevisa att den var korrekt tog ungefär tjugo.
En modern webbläsare
har tiotals miljoner rader.

<!-- S47 -->
Och även det beviset har en hake.
Det visar att programmet matchar sin specifikation.
Det kan inte visa att specifikationen
är det vi faktiskt ville ha.

<!-- S48 -->
Och specifikationen skrivs av människor.
Så frågan kommer tillbaka till oss.

<!-- S49 -->
Och det är inte bara vår egen kod.
En programmerare bygger idag på ramverk,
bibliotek och hundratals beroenden.
Varje lager sparar oss enorma mängder arbete.
Men varje lager är något
vi måste förstå...
eller åtminstone lita på.

<!-- S50 -->
Vilket betyder att du inte behöver skriva en bugg
för att ha en i din programvara.
Du kan helt enkelt installera den.

<!-- S51 -->
Lägg sedan till pressen.
Ingen vill ha en perfekt produkt om tio år.
De vill ha en som fungerar nästa månad.
Och ett intrång som aldrig hände
är väldigt svårt att visa i en presentation.

<!-- S52 -->
Och här kommer det märkligaste.
Våra verktyg blir hela tiden bättre.
Säkrare språk, fuzzing, bug bounties...

<!-- S53 -->
Och ändå fortsätter antalet kända sårbarheter
att växa.
Bara under 2024 fick omkring fyrtiotusen
ett officiellt nummer.

<!-- S54 -->
Delvis för att vi också skriver
långt mer programvara än någonsin.
Det är som att göra varje väg säkrare...
samtidigt som vi bygger miljontals gånger fler vägar.

<!-- S55 -->
Så är programmerare dåliga på sitt jobb?
Nej.
Vi har bett dem om något
som ingen allmän metod kan garantera.

<!-- S56 -->
Så kanske
"hur skriver vi programvara utan buggar?"
är fel fråga.

<!-- S57 -->
Den bättre frågan är:
hur bygger vi system som förblir säkra
även när programvaran har buggar?

<!-- S58 -->
Och det är precis dit säkerheten är på väg.
Den säger inte: gör aldrig ett misstag.
Den säger: utgå från att du redan gjort det.

<!-- S59 -->
Minns du den där returadressen?
Idag vaktar systemet den.
Det blandar om var saker ligger i minnet.
Och det vägrar köra instruktioner
gömda i data.

<!-- S60 -->
Buggen i vår C-kod finns fortfarande kvar.
Den är bara mycket svårare att utnyttja för en attack.

<!-- S61 -->
Och samma idé finns överallt.
Sandlådor, begränsade behörigheter,
isolerade processer, kryptering,
säkerhetskopior, övervakning...
lager på lager,
så att en bugg inte blir en katastrof.

<!-- S62 -->
Och det har en mycket praktisk följd.
Om buggar är oundvikliga
är det inte valfritt att åtgärda dem.

<!-- S63 -->
Programvaran du använder idag
innehåller mycket möjligt en sårbarhet
som ingen ännu har hittat.

<!-- S64 -->
Och när någon gör det
är uppdateringen skillnaden mellan
"en sårbarhet upptäcktes"
och "vi blev hackade".

<!-- S65 -->
Detsamma gäller de system vi bygger.
Gamla bibliotek och plattformar utan stöd
blir inte säkrare av att ignoreras.
De blir teknisk skuld.

<!-- S66 -->
Och varför den skulden måste betalas av
handlar min video
"Det funkar ju än. Så varför uppgradera?"
om.

<!-- S67 -->
För i programvara
är "det funkar fortfarande"
och "det är fortfarande säkert"
två väldigt olika saker.
