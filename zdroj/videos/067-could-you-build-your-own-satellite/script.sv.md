<!-- S01 -->
Tänk dig att du har en galen idé.
Du vill bygga din egen satellit.
Inte någon kommunikationssatellit
för en miljard dollar.
Något litet.

<!-- S02 -->
En låda ungefär lika stor
som en limpa bröd.
Inuti: en dator, solpaneler,
en radio, några sensorer.
Kanske till och med en kamera.

<!-- S03 -->
Du bygger den i ditt garage.
Och sedan, på något sätt...
får du upp den i omloppsbana.
Låter omöjligt.
Men det är det inte.

<!-- S04 -->
Folk har gjort
nästan precis det här i åratal.
De kallas CubeSats.

<!-- S05 -->
Och det förvånande är
att det svåraste
inte är att bygga satelliten.
Det är allt annat.

<!-- S06 -->
Grundenheten kallas 1U —
ungefär en tiocentimeterskub.
Staplar du enheter
får du 2U, 3U, 6U
och större.

<!-- S07 -->
Idén är enkel.
I stället för att konstruera en ny rymdfarkost
från grunden
återanvänder du standardiserade storlekar
och standardiserade gränssnitt.
Och plötsligt är rymden öppen
för universitet, startups
och kanske till och med dig.

<!-- S07b -->
Förresten, om du gillar sådana här
videor, överväg att prenumerera.

Det hjälper kanalen verkligen.

<!-- S08 -->
Så vad skulle vår lilla satellit
egentligen innehålla?
Först behöver den en dator.
Något måste köra mjukvaran,
styra hårdvaran
och bestämma vad som ska göras.

<!-- S09 -->
Sedan strömförsörjningen.
Solpaneler skapar elektricitet.
Batterier lagrar den
till när satelliten
glider in i jordens skugga.

<!-- S10 -->
Sedan kommunikationen.
En radio. En antenn.
Och nere på jorden
en markstation som lyssnar.

<!-- S11 -->
Sedan sensorer.
Temperatur. Spänning. Ström.
Acceleration. Magnetfält.
Och något sätt att avgöra
åt vilket håll satelliten pekar.
För i omloppsbana
är "upp" förvånansvärt svårt att säga.

<!-- S12 -->
Men innan vi bygger en,
kommer en obekväm fråga.
Vad kostar den här lilla lådan?
Svaret är...
mer än man skulle tro.

<!-- S13 -->
En enkel 1U-CubeSat
kan lätt kosta
tiotusentals dollar —
bara i flyghårdvara.
Strömförsörjningen. Solpaneler.
Batterier. Datorn. Radion.
Orienteringskontrollen. Strukturen.
Och nyttolasten.

<!-- S14 -->
Sedan kommer de saker
som inte står på komponentlistan.
Tester. Integration.
Dokumentation.
Drift av markstationen.
Licenser.
Och till slut...
uppskjutningen.

<!-- S15 -->
En samåkning för en pytteliten CubeSat
kan kosta tiotusentals dollar.
Större uppdrag och större CubeSats
kan kosta hundratusentals dollar.
Och det är bara
för att få upp grejen i rymden.

<!-- S16 -->
Och nu
ett ännu löjligare problem.
Minns du alla de där delarna?
Hur i hela världen får man plats
med allt det i en pytteliten låda?

<!-- S17 -->
I rymden finns ingen plats
för en slumpartad hög elektronik.
Varje centimeter räknas.
Varje gram räknas.
Varje watt räknas.
Satelliten är ett tredimensionellt pussel
som måste överleva en raketuppskjutning.

<!-- S18 -->
Så var får du tag i
alla de här delarna?
Du behöver inte konstruera
allt själv.
Det finns en hel industri
som säljer komponenter för små satelliter:
datorer, strömförsörjning,
radioapparater, antenner och solpaneler.
Det finns till och med marknadsplatser
byggda särskilt för CubeSat-delar.

<!-- S18b -->
Och delarna är dessutom standardiserade.
Många delar samma kortformat
och staplas helt enkelt på varandra,
så att delar från olika tillverkare
passar ihop i en enhet.
Företag som EnduroSat
och GomSpace säljer dem,
och ett enda delsystem kan kosta
allt från några tusen
till tiotusentals dollar.

<!-- S19 -->
Och det här är inga
exotiska processorer.
En aktuell CubeSat-dator
använder en ARM Cortex-M7,
med välbekanta gränssnitt —
SPI, I²C, UART och CAN.

<!-- S19b -->
Och det är inget specialbyggt rymdchip.
Det är ett riktigt standardkort
som du skulle kunna hålla i handen.

<!-- S20 -->
En rymdfarkost behöver något
viktigare än ren hastighet:
förutsägbart beteende,
låg förbrukning och tillförlitlighet.
Mer krävande uppdrag
kan använda ARM Cortex-A-processorer —
och till och med Linux.

<!-- S20b -->
Men snabb är den inte.
En typisk CubeSat-dator
kör på ett par hundra megahertz.
Din laptop kör på
fyra eller fem gigahertz,
med många fler kärnor.
Den offrar snabbhet
för att dra så lite ström som möjligt.

<!-- S21 -->
Och om du är programmerare
är det här det blir intressant.
Du skriver inte
något mystiskt "rymdspråk".
Du skriver inbyggd mjukvara.
Ofta i C eller C++.

<!-- S22 -->
Den kan köras direkt
på hårdvaran,
eller på ett realtidsoperativsystem
som FreeRTOS, Zephyr eller RTEMS.
Det finns till och med öppna ramverk
byggda för rymdfarkoster.
NASA:s F Prime, till exempel,
är ett ramverk för flygmjukvara
för inbyggda system och rymdsystem.

<!-- S23 -->
Så din kod kan se ut
ungefär så här.

<!-- S24 -->
Men det finns en enorm skillnad
jämfört med en vanlig dator.
Du kan inte SSH:a in i den.
Du kan inte koppla på en debugger.
Och om din mjukvara kraschar...
är din dator
ett par hundra kilometer upp.

<!-- S25 -->
Så den behöver watchdogtimers,
säkra lägen, feldetektering
och automatisk återhämtning.
Vissa problem måste den lösa
utan att du finns där för att hjälpa.

<!-- S25b -->
Och en stor anledning till allt det
är strålning.
I rymden kan kosmisk strålning
vända en bit i minnet,
eller till och med slå ut ett chip.
Det finns ingen tung avskärmning —
den skulle väga alldeles för mycket.
I stället övervakar datorn sig själv,
rättar fel
och startar om när något går fel.

<!-- S26 -->
Men om du faktiskt
vill skjuta upp den...
blir det allvar.
En del som fungerar på ditt skrivbord
är inte automatiskt redo
för en raket.
Den måste överleva vibrationer,
vakuum, extrema temperaturer
och strålning.

<!-- S27 -->
Nu, tillbaka till problemet
att veta åt vilket håll
satelliten pekar.
Föreställ dig hur den tumlar
genom rymden.
Inget golv. Inget tak.
GPS kan tala om för dig
var du är...
men inte åt vilket håll
du är vänd.

<!-- S28 -->
Så satelliter kombinerar
gyroskop, magnetometrar
och solsensorer
för att räkna ut sin orientering.
Och sedan måste de ändra den.
Ett vanligt knep
är en magnetorquer.

<!-- S29 -->
Den trycker mot
jordens magnetfält
och skapar ett litet vridmoment.
Det är ingen raketmotor.
Den flyttar inte satelliten.
Den bara vrider den.
Och det räcker
för att rikta satelliten
precis dit du vill.

<!-- S30 -->
Men inget av det här
är anledningen till
att vi byggde satelliten.
Vi behöver ett uppdrag.
Det är nyttolasten.
Mäta strålning.
Fotografera jorden.
Studera atmosfären.
Testa en ny sensor.
Eller helt enkelt bevisa
att en ny teknik fungerar.

<!-- S31 -->
Själva satelliten
finns mest till för
att hålla nyttolasten vid liv.
Förse den med ström. Rikta den.
Hålla den varm.
Lagra dess data.
Och skicka hem dem.

<!-- S32 -->
När din dator hänger sig
startar du om den.
När din satellit hänger sig...
har du ett väldigt dyrt föremål
som tyst kretsar kring jorden.

<!-- S33 -->
Låt oss säga att vi byggde den.
Allt fungerar...
Datorn startar...
Radion sänder.
Panelerna skapar ström.
Nyttolasten körs...
Kan vi skjuta upp den?
...Inte än.

<!-- S34 -->
En satellit måste bevisa
att den klarar uppskjutningen.
Det betyder tester.
Massor av tester.

<!-- S35 -->
Först skruvar du fast den
på ett jättelikt skakbord.
Sedan skakar du den, hårt...
Det är vibrationstest.
Raketuppskjutningar är inte skonsamma.
Den måste överleva
buller, vibration och stötar
utan att något
lossnar eller går sönder.
Varje skruv räknas.
Varje kontakt räknas.
Varje kabelbit räknas.

<!-- S36 -->
Sedan kommer vakuumet.
På jorden bär luften bort värme.
I rymden finns ingen luft.
Ena sidan kan bli extremt het,
en annan extremt kall,
och elektroniken
måste ändå hålla sig
inom sina gränser.
Så satelliten behöver
värmeledare, beläggningar,
isolering
och noggrant utvalda material.
Satelliter har ingen
luftkonditionering.
De har fysik.

<!-- S37 -->
Och batteriet
blir intressant.
Ladda det med solljus.
Sedan glider satelliten
in i jordens skugga,
och panelerna skapar nästan ingenting.
Batteriet håller den vid liv.
Sedan tillbaka i solljus.
Ladda. Ladda ur.
Ladda. Ladda ur.
Om och om igen.
I åratal.
Ett enda fel i strömförsörjningen
kan tyst avsluta uppdraget.

<!-- S38 -->
Och hur pratar du nu med den?
Du behöver en radio.
En antenn.
Och en frekvens
som du lagligt får använda.
Och en markstation.
Satelliten
har inget internet.
Den flyger bara över dig
och sänder.

<!-- S39 -->
Din markstation
fångar signalen.
Datorn avkodar den.
Och plötsligt har du data
från din egen rymdfarkost.
Tänk dig att öppna en terminal
och se det här.

Fast maskinen
som skriver ut de där siffrorna...
är hundratals kilometer
ovanför ditt huvud.

<!-- S40 -->
Så hur får vi
egentligen upp den dit?
Du skulle kunna bygga en raket...
Snälla, låt bli...
Du behöver ingen.
CubeSats flyger
som sekundär nyttolast.

<!-- S41 -->
En raket ska ändå upp.
Den har plats över.
Din satellit följer med
i en standardutskjutare.
Ingen egen raket behövs.

<!-- S42 -->
Och nu sitter den
på toppen av en raket.
Du kan inte röra den.
Du kan inte öppna lådan.
Du kan inte koppla in en kabel.
Raketen skjuts upp.
Ungefär nio minuter senare
är du i omloppsbana.

<!-- S43 -->
Utskjutaren
släpper loss din satellit.
Den fjädrar ut
och börjar tumla.

<!-- S43b -->
Men hur vet den att den är ute?
...
Fjäderbelastade brytare, intryckta
medan den satt i utskjutaren,
frigörs i samma stund den skjuts ut,
och datorn startar.
Sedan är den, enligt reglerna,
tyst i ungefär en halvtimme.
Först då slår den på sin radio,
fäller ut sina antenner
och hör äntligen av sig hem.
Och någonstans på jorden...
hör din markstation den.

<!-- S44 -->
Du byggde en maskin.
Och nu kretsar den maskinen
kring planeten.

<!-- S44b -->
Fast, vi är inte klara.
En död satellit kan inte bara
stanna där uppe för evigt.
Lämnad i omloppsbana i århundraden
blir den rymdskrot.

<!-- S45 -->
Det betyder att moderna uppdrag
allt oftare måste planera
för slutet
på rymdfarkostens liv.
Helst drar den tunna övre atmosfären
långsamt ner den.
Dess omloppsbana sjunker.
Den återinträder.
Och den brinner upp.
Slutet på uppdraget...
är en del av uppdraget.

<!-- S46 -->
Så... skulle du kunna bygga
din egen satellit?
Tekniskt sett, ja.
Du behöver inte vara NASA.
Du behöver inte
äga en raket.
Du behöver inte ens nödvändigtvis
ett enormt företag.

<!-- S47 -->
Satelliten måste
överleva uppskjutningen.
Överleva rymden.
Kommunicera lagligt.
Fungera på egen hand.
Och till slut
lämna omloppsbanan.
Allt det där
måste bevisas
innan någon
sätter den på en raket.

<!-- S48 -->
CubeSats gjorde inte rymden enkel.
De gjorde den standardiserad.
I stället för att bygga allt
från grunden
kan du bygga något
som passar en befintlig standard.
Och det är en förvånansvärt stor förändring.

<!-- S49 -->
Så någonstans, just nu,
kretsar pyttesmå maskiner
kring jorden.
Byggda av universitet,
forskarlag,
företag och studenter.

<!-- S50 -->
Vissa bär kameror.
Vissa mäter strålning.
Vissa testar
helt ny teknik.
Och vissa är bara experiment
med en enda fråga:
"kan vi få den här grejen
att fungera i rymden?"

<!-- S51 -->
Och det är därför
det är så fascinerande
att bygga sin egen satellit.
För avståndet
mellan dig och rymden
är inte längre en raket.
Det kan vara...
en tiocentimeterslåda.
Och en väldigt, väldigt
lång checklista.
