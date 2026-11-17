<!-- S01 -->
Tänk dig att du startar en Windows-dator
och inte hittar något aktivitetsfält, ingen Start-knapp
och inte en enda ikon på skrivbordet.

<!-- S02 -->
I stället finns en smal list längst upp,
en meny som dyker upp var du än klickar,
och fyra virtuella skrivbord bredvid varandra.

<!-- S03 -->
Det ser ut som Linux.
Men dina program, drivrutiner och filer
ligger precis där du lämnade dem.
Det är fortfarande Windows.

<!-- S04 -->
Det är bara skrivbordet som har ändrats.
Och reglaget som ändrar det
är en enda inställning.

<!-- S05 -->
Windows har den i registret,
i ett värde som heter Shell.
På nästan varje Windows-dator
står det explorer.exe där.

<!-- S06 -->
Skriv in namnet på ett annat program,
logga ut och logga in igen,
så startar Windows det programmet i stället.
Vad det än ritar blir ditt skrivbord.

<!-- S07 -->
Och det är inget trick som någon hittade i fjol.
Redan 1990 hade Windows 3.0 samma reglage
i en vanlig textfil som hette system.ini.
En rad: shell=progman.exe.

<!-- S08 -->
Ändrade man det namnet
dök Programhanteraren, fönstret fullt av ikongrupper,
aldrig upp alls.

<!-- S09 -->
Frågan är alltså inte om Windows
kan ha ett annat skrivbord.
Det har det alltid kunnat.
Frågan är varför nästan ingen har sett ett.

<!-- S10 -->
Börja med vad den raden faktiskt pekar på.
Aktivitetsfältet, ikonerna på skrivbordet,
det lilla meddelandefältet vid klockan:
allt det är ett enda program, explorer.exe.

<!-- S11 -->
Ja, samma explorer.exe
som du öppnar som Utforskaren för att titta på dina filer.
Det gör två jobb,
och de flesta lägger bara märke till det ena.

<!-- S12 -->
Det andra jobbet har ett namn: skalet.
Det är lagret du rör vid.
Under det finns kärnan, drivrutinerna
och tjänsterna som håller Windows igång.

<!-- S13 -->
Ingen av dem behöver ett aktivitetsfält.
Avsluta explorer.exe i Aktivitetshanteraren,
så försvinner aktivitetsfältet och ikonerna...
men Anteckningar, din webbläsare
och alla andra fönster fortsätter att fungera.

<!-- S14 -->
Starta det igen, så kommer skrivbordet tillbaka.
Det är nog det tydligaste beviset som finns
på att skrivbordet bara är ett program till.

<!-- S14b -->
Om du någon gång har bytt startskärmsapp
på en Android-telefon
har du sett en liknande idé.
Android gör det till en vanlig inställning.
Windows har också mekanismen,
men har aldrig gett vanliga användare
en enkel knapp för det.

<!-- S15 -->
Tre ord blandas ihop här.
Skalet är det du startar saker från:
aktivitetsfältet, menyerna, skrivbordet.
En fönsterhanterare styr hur fönster
placeras, staplas och får fokus.
En skrivbordsmiljö
får hela upplevelsen att hänga ihop.

<!-- S16 -->
På Linux kan de här delarna kombineras
på många olika sätt.
På Windows ersätter ett nytt skal
inte systemets fönsterhantering
eller sättet som program ritar sina fönsterramar på.

<!-- S17 -->
Det hindrade inte folk från att försöka.
I början av 90-talet kunde du gå in i en butik
och köpa en ersättare för Programhanteraren.

<!-- S18 -->
Norton Desktop for Windows
gav dig ett eget skrivbord,
egna filverktyg och en egen programstartare,
ovanpå samma Windows som förut.

<!-- S19 -->
Vissa datortillverkare bytte ut den
innan kunden ens hade startat datorn.
Packard Bells Navigator tog emot köparna
med ett hus man kunde gå igenom, rum för rum.

<!-- S20 -->
Sedan lämnade Windows 95 över jobbet till explorer.exe,
och raden i system.ini
ändrades helt enkelt till explorer.exe.
Reglaget satt kvar precis där det var.

<!-- S21 -->
I slutet av 90-talet
växte en hel gemenskap fram kring det reglaget.
Det mest kända projektet var LiteStep.

<!-- S22 -->
Det lånade sitt utseende från AfterStep,
en fönsterhanterare för Unix med NeXTSTEP som förebild,
från företaget Steve Jobs grundade efter att ha lämnat Apple.

<!-- S23 -->
LiteStep hade ingen Start-meny om du inte byggde en.
Allt var en modul:
en docka här, en klocka där,
en meny som öppnades var du än högerklickade.

<!-- S24 -->
Teman delades som bakgrundsbilder.
Vissa såg futuristiska ut.
Vissa såg ut som en Unix-arbetsstation.
Vissa lämnade nästan ingenting kvar på skärmen.

<!-- S25 -->
Blackbox for Windows gick åt andra hållet.
Det kopierade Blackbox, en minimalistisk fönsterhanterare för Unix,
ända ner till en enda enkel meny
och ett smalt verktygsfält.

<!-- S26 -->
Efterföljaren bbLean
höll den idén vid liv på Windows 2000 och XP.

<!-- S27 -->
Emerge Desktop delade upp skalet i separata delar:
en programstartare, ett meddelandefält, en lista över öppna fönster,
var och en ett litet program som du kunde behålla eller slänga.

<!-- S28 -->
Varför göra sig så mycket besvär?
Delvis för att XP:s utseende
var lätt att känna igen och svårt att ändra.
Teman ändrade färgerna och knapparna.
Layouten var densamma.

<!-- S29 -->
Delvis minnet.
På en dator med 128 megabyte
lovade ett lättare skal mer utrymme
för allt annat.

<!-- S30 -->
Och delvis Linux.
Där var det normalt att välja skrivbord,
och vissa Windows-användare ville ha
samma val.

<!-- S31 -->
De flesta av de projekten finns inte längre.
LiteSteps sista version var en förhandsversion
från 2014, fortfarande märkt alfa.
Emerge Desktop och SharpEnviro lades också ner.

<!-- S32 -->
Små team av ideella utvecklare var en del av förklaringen.
Men Windows förändrades också.
Med åren blev skrivbordet mycket mer
än en enda körbar fil.

<!-- S33 -->
Skrivbordsupplevelsen är i dag utspridd
över flera processer,
systemkomponenter och paketerade appar.
Till och med Start-menyn körs som ett eget program.

<!-- S34 -->
Att ersätta explorer.exe betyder inte att man ersätter
allt som utgör dagens Windows-gränssnitt.
Och det är ett av skälen till att det
är svårare än förr att bygga
ett komplett alternativt skrivbord.

<!-- S35 -->
Och ändå fungerar det fortfarande.
Cairo Desktop, ett projekt med öppen källkod,
körs på Windows 11 i dag.

<!-- S36 -->
Det har en egen menyrad längst upp,
ett eget aktivitetsfält
och mappar som du kan fästa på raden som staplar.

<!-- S37 -->
Det kan köras sida vid sida med explorer.exe
eller ta över som skal.
I det andra läget
kan delar av Windows 11 krångla,
bland annat Inställningar och Windows-säkerhet.

<!-- S38 -->
Seelen UI gör det på ett annat sätt.
Det ersätter inte explorer.exe.
Det döljer aktivitetsfältet och har egna delar:
en docka, en list, widgetar
och en fönsterhanterare som lägger dina fönster sida vid sida.

<!-- S39 -->
Resultatet kan se ut som allt annat än Windows.
Men under ytan körs explorer.exe fortfarande.
Det är ett nytt ansikte, inte ett nytt skal.

<!-- S40 -->
Och Microsoft?
De har faktiskt en officiell funktion för det här.
Den heter Shell Launcher
och är gjord för enheter som kiosker.

<!-- S41 -->
Du har förmodligen använt något liknande
utan att veta om det.
Biljettautomaten på stationen.
En självbetjäningskassa. En bankomat.

<!-- S42 -->
Många av dem är Windows-datorer
där hela skalet är ett enda program.
En administratör anger programmet,
och efter inloggningen är det programmet hela skrivbordet.

<!-- S43 -->
Men den finns bara
i utgåvorna Enterprise, Education
och IoT Enterprise.

<!-- S44 -->
Och den äldre mekanismen i registret
är fortfarande en del av Windows.
Microsoft gjorde den bara aldrig
till en vanlig skrivbordsinställning
för vanliga användare.

<!-- S45 -->
Så varför verkar Windows bara ha ett skrivbord?
Inte för att det inte kan ha ett annat.
Utan för att skrivbordet är produkten.

<!-- S46 -->
På Linux är skrivbordet ett val.
Vissa distributioner ber dig välja ett
medan du fortfarande installerar.
KDE Plasma, GNOME, Xfce, Cinnamon...

<!-- S47 -->
På Windows är skrivbordet det som Microsoft visar
i varje annons, på varje skärmbild
och på varje supportsida.
Ett skrivbord betyder en uppsättning instruktioner
för mer än en miljard datorer.

<!-- S48 -->
Det är en verklig fördel.
När något går sönder
ser skärmen i hjälpartikeln ut som din.
Priset är att de flesta aldrig får veta
att det fanns ett val.

<!-- S49 -->
Folk bytte ut Windows-skrivbordet
redan innan Windows 95 ens fanns.
De byggde dockor, avskalade menyer
och skrivbord som inte liknade något annat.

<!-- S50 -->
De flesta av de projekten är borta.
Idén är det inte.
Under varje aktivitetsfält du någonsin har klickat på
finns den där enda inställningen kvar och väntar på ett annat namn.

<!-- S51 -->
Skrivbordet är bara ännu en programvara.
Och programvara går att byta ut.

<!-- S52 -->
Så här kommer en fråga till dig.
Om Windows lät dig välja skrivbord
vid installationen, som vissa Linuxdistributioner gör,
skulle du byta, eller behålla det du känner till?
Skriv det i kommentarerna.
