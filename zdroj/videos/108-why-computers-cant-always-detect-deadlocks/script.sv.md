<!-- S01 -->
Fyra bilar kommer fram till en korsning
i exakt samma ögonblick.
Inga trafikljus. Inga skyltar.
Bara regeln som gäller i många länder:
lämna företräde åt bilen från höger.

<!-- S02 -->
Varje förare tittar åt höger
och ser en bil som hen måste vänta på.
Så varje förare väntar.

<!-- S03 -->
Ingen bryter mot regeln.
Alla följer den perfekt.
Och ingen kommer någonsin att röra sig.

<!-- S04 -->
Datavetare kallar det här ett baklås, på engelska deadlock.
Och det händer inte bara på vägarna.
Det händer i databaser,
operativsystem och helt vanlig mjukvara.

<!-- S05 -->
Datorer är ofta bra på att upptäcka
ett baklås när det väl har uppstått.
Men skulle ett program kunna läsa ett annat program
och tala om för dig, med säkerhet,
om det någonsin kommer att fastna?

<!-- S06 -->
För många program, ja.
Men en metod som fungerar
för alla tänkbara program
kan inte finnas.
Och inte för att datorer
inte är tillräckligt snabba än.
Ingen snabbare dator kommer någonsin att ändra på det.

<!-- S07 -->
Så här fastnar ett program.
Tänk dig en webbutik
där två processer körs samtidigt.

<!-- S08 -->
Innan en process ändrar något
lägger den ett lås på det,
så att ingen annan kan röra det.
Som att ta den enda nyckeln till ett rum.

<!-- S09 -->
Den första processen låser en kunds konto
och vill sedan låsa kundens beställning.
Den andra låser beställningen
och vill sedan låsa kontot.

<!-- S10 -->
Den ena håller kontot
och väntar på beställningen.
Den andra håller beställningen
och väntar på kontot.
Ingen av dem släpper det den håller.

<!-- S11 -->
Och det märkliga är
att den här koden kan köras en miljon gånger
utan minsta problem.
Bara när de två processerna överlappar
i precis fel ordning
stannar allt.

<!-- S12 -->
Felet fanns där hela tiden.
Det var bara den olyckliga tajmingen som avslöjade det.

<!-- S12b -->
Förresten, om du gillar sådana här
videor, prenumerera gärna.

Det hjälper kanalen på riktigt.

<!-- S13 -->
Databaser råkar ut för det här hela tiden,
så de håller vakt.
De ritar en karta över vem som väntar på vem.

<!-- S14 -->
Den första väntar på den andra.
Den andra väntar på den första.
När pilarna sluter sig till en slinga
är det ett baklås.
Inget gissande. Slingan syns direkt.

<!-- S15 -->
Sedan gör databasen något brutalt.
Den väljer ut en av processerna
och kastar bort dess arbete.

<!-- S16 -->
Microsofts SQL Server talar till och med om för förloraren
att den har valts ut
som offer för baklåset
och ska försöka igen.

<!-- S17 -->
Den andra processen fortsätter,
och offret kan helt enkelt försöka igen.

<!-- S18 -->
Lägg märke till vad det löser och inte löser.
Baklåset är upplöst.
Men koden som orsakade det finns kvar
och väntar på nästa olyckliga ögonblick.

<!-- S19 -->
Att upptäcka ett baklås
som redan har uppstått
är alltså den lätta delen.
Den svåra frågan är en annan.

<!-- S20 -->
Inte: har det här programmet fastnat just nu?
Utan: om det får den här indatan,
kan det någonsin fastna?

<!-- S21 -->
Den första är ett foto av nuet.
Du kan bara titta på det.
Den andra är en förutsägelse
om varje tänkbar framtid.

<!-- S22 -->
Och program gör det väldigt svårt.
De fattar beslut. De upprepar saker.
De kan köra beräkningar som tar
en sekund, eller tusen år.

<!-- S23 -->
Ett program kan fastna direkt,
efter en miljon steg,
för ett enda ovanligt indatavärde,
eller aldrig någonsin.

<!-- S24 -->
Du skulle kunna köra det och se vad som händer.
Men om det inte har fastnat efter en timme,
vad säger det dig?

<!-- S25 -->
Ingenting.
Det kan fastna i nästa sekund,
eller aldrig.

<!-- S26 -->
År 1936 visade en ung matematiker
som hette Alan Turing
att vissa frågor om program
inte kan besvaras av något program.
Den mest berömda låter ännu enklare.

<!-- S27 -->
Ta vilket program som helst, och dess indata.
Kommer det till slut att stanna?
Eller kommer det att köra för evigt?

<!-- S28 -->
I dag kallas det stopproblemet.
Och inget program kan besvara det
korrekt i alla fall.

<!-- S29 -->
Idén bakom beviset
är förvånansvärt kort.
Anta att någon ger dig
en perfekt stoppkontrollant.

<!-- S30 -->
Nu skriver du ett litet, motsträvigt program.
Det frågar kontrollanten om sig självt
och gör sedan tvärtom.

<!-- S31 -->
Om kontrollanten säger att det stannar,
hamnar det i en oändlig loop.
Om kontrollanten säger att det kör för evigt,
stannar det direkt.

<!-- S32 -->
Vad kontrollanten än säger om det,
har kontrollanten fel.
Så en perfekt kontrollant kan inte finnas.

<!-- S33 -->
Så vad har det här med baklås att göra?
Väldigt mycket.

<!-- S34 -->
Tänk dig att någon påstår sig ha byggt
ett perfekt verktyg som förutsäger baklås.
Ge det vilket program som helst och dess indata,
så säger det dig alltid, korrekt,
om programmet någonsin kommer att fastna.

<!-- S35 -->
Låt oss använda det
för att lösa stopproblemet.

<!-- S36 -->
Ta vilket program du vill
och bädda in det i ett nytt program.

<!-- S37 -->
Först kör det nya programmet
helt enkelt det gamla,
steg för steg, i en enda tråd.
Inga lås. Inget delat.
Inget som någonsin skulle kunna fastna.

<!-- S38 -->
Sedan, om det gamla programmet någonsin blir klart,
startar det nya två processer.
Var och en tar ett lås,
väntar tills den andra har tagit sitt,
och försöker sedan ta den andras.
Ett baklås, med flit, varje gång.

<!-- S39 -->
Om det gamla programmet aldrig blir klart,
kommer det nya aldrig så långt.
Inget baklås. Aldrig.

<!-- S40 -->
Så det nya programmet fastnar
om, och endast om, det gamla stannar.

<!-- S41 -->
Fråga nu verktyget
om det nya programmet.
”Ja, det blir baklås”
betyder att det gamla programmet stannar.
”Nej” betyder att det kör för evigt.

<!-- S42 -->
Vi har just löst stopproblemet.
Och det är precis det som inte går.

<!-- S43 -->
Så ett perfekt verktyg som förutsäger baklås
kan inte heller finnas.

<!-- S44 -->
Problemet är inte låsen,
eller databaserna, eller dåliga programmerare.
Ett program kan gömma vilken beräkning som helst
på vägen till ett baklås.
För att förutsäga baklåset
skulle du behöva förutsäga om beräkningen tar slut.

<!-- S45 -->
Men vänta lite.
En riktig dator är inte oändlig.
Dess minne har ett begränsat antal tillstånd.
Kan du inte bara kontrollera alla, då?

<!-- S46 -->
För en maskin med en fast mängd
minne är svaret i princip ja.
I praktiken: försök räkna dem.

<!-- S47 -->
Minnet i en bärbar dator
med åtta gigabyte
kan ordnas på så många sätt
att det behövs ungefär tjugo miljarder siffror
bara för att skriva ner det talet.

<!-- S48 -->
Antalet atomer
i det observerbara universumet
har ungefär åttio.

<!-- S49 -->
Att kontrollera allt på en riktig maskin
är alltså möjligt i teorin
och hopplöst i praktiken.

<!-- S50 -->
Men det är en helt annan mur.
Turings gräns handlar inte om för många tillstånd.
Den gäller program
som alltid kan be om mer minne.
För dem kan det inte finnas något perfekt verktyg,
hur stor datorn än är.

<!-- S51 -->
Betyder det att baklås är hopplösa?
Nej.
Det betyder att det inte finns någon perfekt kontrollant.
Så programmerare skriver program
som är lättare att kontrollera.

<!-- S52 -->
Det enklaste tricket är en fast ordning.
Varje process måste låsa kontot
före beställningen.
Aldrig tvärtom.

<!-- S53 -->
Om varje process verkligen håller sig till den ordningen
kan slingan inte bildas,
och den här sortens baklås kan inte uppstå.

<!-- S54 -->
Andra system ger upp efter en timeout,
tar alla sina lås på en gång
eller låter databasen välja ett offer
och försöker helt enkelt igen.

<!-- S55 -->
Och för små, noggrant beskrivna konstruktioner
kan verktyg kontrollera varje möjligt tillstånd.
Ingenjörer på Amazon använde ett sådant
för att hitta en bugg som krävde trettiofem steg,
i exakt rätt ordning, för att visa sig.

<!-- S56 -->
De här verktygen fungerar
eftersom problemet har gjorts mindre.
De kontrollerar en modell av systemet,
inte varje program som någonsin skulle kunna finnas.

<!-- S57 -->
För riktig kod däremot
måste en kontrollant som tar emot vilket program som helst
ge upp något.
Den kan varna för baklås
som inte kan uppstå,
missa några som kan,
eller ibland inte ge något svar alls.

<!-- S58 -->
En kontrollant som aldrig slår falskt larm,
aldrig missar ett enda baklås
och alltid ger ett svar,
för varje program,
är precis det som Turing uteslöt.

<!-- S59 -->
Tillbaka i korsningen:
de fyra förarna sitter inte där för evigt.

<!-- S60 -->
Någon vinkar.
En förare avstår från sin tur,
och baklåset är löst på några sekunder.

<!-- S61 -->
Det är precis vad databasen också gör.
Den förutsäger inte baklåset.
Den märker det
och får någon att lämna företräde.

<!-- S62 -->
Vissa problem behöver en snabbare dator.
Vissa en bättre idé.

<!-- S63 -->
Och vissa, som det här,
har ingen perfekt lösning alls.
Bara bra regler
och någon som är redo att vinka.
