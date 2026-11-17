<!-- S01 -->
Du försöker radera en fil.
Datorn säger att den är öppen
i ett annat program.
Men inte vilket.

<!-- S02 -->
Det meddelandet är den synliga änden
på en mycket märkligare fråga.
Vad betyder det egentligen
att öppna en fil?

<!-- S03 -->
För på en annan dator
kan samma fil, öppnad på samma sätt,
raderas utan protester.

<!-- S04 -->
Samma fil.
Samma handling.
Två helt olika svar.

<!-- S05 -->
Börja med det
som irriterar alla.
Vilket program?

<!-- S06 -->
Windows vet det.
Det har ett kärnobjekt
för den öppna filen
och vet vilken process som äger det.
Det skulle kunna säga namnet.

<!-- S07 -->
Så du stänger saker på måfå.
Du öppnar Aktivitetshanteraren.
Du stirrar på en lista med processer
och känner knappt igen någon.

<!-- S08 -->
Och i flera år
var svaret faktiskt
att ladda ner ett separat verktyg.
Unlocker kom 2005,
och på Windows XP var det svaret.

<!-- S09 -->
Sedan kom Windows 7
med Resursövervakaren.
Fliken Processor.
En lista som heter Associerade handtag.

<!-- S10 -->
Skriv filens namn.
Då ser du programmet
och process-ID:t.
Inget att installera.
Det har funnits där sedan 2009.

<!-- S10b -->
Men de separata verktygen
gjorde mer än att bara berätta.
De kunde stänga handtaget
och släppa filen fri.

<!-- S11 -->
Vilket för oss tillbaka
till frågan.
Vad fick programmet
när det öppnade filen?

<!-- S12 -->
Säg att en videospelare öppnar
en fil som heter movie.mp4.
I Windows betyder det att öppna en fil
att fylla i två saker.

<!-- S13 -->
Den första är självklar.
Vad vill jag göra med den?
Läsa den. Skriva till den.

<!-- S14 -->
Den andra är den intressanta.
Vad får alla andra göra
medan jag har den öppen?

<!-- S15 -->
Det är en riktig inställning.
Du anger vad andra program
får göra medan du har den öppen.

<!-- S16 -->
De får läsa den.
De får också skriva till den.
De får radera eller byta namn på den.

<!-- S16b -->
Eller ingenting alls.
Ingen rör den här
medan jag använder den.

<!-- S17 -->
Flaggan som tillåter radering
heter FILE_SHARE_DELETE.
Och Microsofts dokumentation
lägger till en rad under den.

<!-- S18 -->
Raderingsåtkomst omfattar
både radering och namnbyte.

<!-- S19 -->
Så ett program som vägrar
raderingsdelning
har blockerat namnbytet också.

<!-- S20 -->
Och om programmet som öppnade filen
inte gav den rätten,
kan ingen annan ta den.

<!-- S21 -->
Det är därför felet
inte heter Filen används.
Det heter delningsöverträdelse.

<!-- S22 -->
Svaret låg hela tiden
i namnet
på själva felet.

<!-- S23 -->
Nu samma sak
på en Linuxmaskin.
En spelare öppnar videon.

<!-- S24 -->
Och du skriver
rm movie.mp4.

<!-- S24b -->
Det fungerar.
Videon fortsätter spela.

<!-- S25 -->
Så vad fick programmet,
om inte ett grepp om filen?

<!-- S26 -->
Det här är hela idén
med videon.
Namnet är inte filen.

<!-- S27 -->
movie.mp4 är en rad
i en katalog.
Den raden pekar på ett objekt
som rymmer de faktiska data.

<!-- S28 -->
När ett program öppnar filen
får det en referens
till objektet.
Inte till raden.

<!-- S29 -->
Att radera filen
raderar alltså raden.
Objektet är orört.

<!-- S30 -->
Manualsidan säger det
i en enda mening.
Filen fortsätter att finnas
tills den sista filbeskrivaren
som pekar på den stängs.

<!-- S31 -->
Det låter abstrakt
tills man ser det hända.
Så jag gjorde en loggfil
på fem hundra megabyte
och lät en process hålla den öppen.

<!-- S31b -->
Sedan raderade jag den.

<!-- S32 -->
En listning av katalogen
visar ingenting alls.
Verktyget som mäter
mappens storlek säger noll.

<!-- S33 -->
Och verktyget som mäter
ledigt utrymme på disken
säger att fem hundra megabyte
fortfarande saknas.

<!-- S33b -->
En tom mapp.
En halv gigabyte borta.

<!-- S34 -->
Det händer så ofta
att det finns ett kommando
bara för att hitta sådana filer.
Raderade, osynliga, kvar på disken.

<!-- S35 -->
Och utrymmet kommer tillbaka
i samma stund som den processen
släpper filen.

<!-- S36 -->
Samma logik gäller namnbyte.
Flytta filen medan den är öppen,
och programmet märker ingenting.

<!-- S37 -->
Manualen är lika rakt på sak där.
Filbeskrivare som öppnats
via den gamla sökvägen påverkas inte.

<!-- S37b -->
Det använde aldrig namnet.

<!-- S38 -->
Vilket har en gräns
som är värd att känna till.
Ett program som körs
går inte att skriva över på plats.

<!-- S38b -->
Linux vägrar.
Text file busy.

<!-- S39 -->
Det du kan göra
är att ta bort namnet
och lägga dit en ny fil.

<!-- S40 -->
Den gamla processen fortsätter
från ett objekt
som inte längre har något namn.
Allt som startas senare får det nya.

<!-- S41 -->
Det är samma idé igen,
och den bevisar sig i praktiken.
Mycket går att byta ut
utan att röra objektet på plats.

<!-- S41b -->
Därför kan Linux uppdatera
ett program medan det körs.
Du får bara inte den nya versionen
förrän du startar om det.

<!-- S42 -->
Så är Windows
helt enkelt sämre konstruerat?

<!-- S42b -->
Nej.
Och det här är den delen
som nästan ingen känner till.

<!-- S43 -->
Windows har ett sätt
att göra precis samma sak.

<!-- S43b -->
På NTFS kan Windows be
om en radering i POSIX-stil.

<!-- S44 -->
Microsoft beskriver
vad som händer då.
Namnet tas bort
från den synliga namnrymden.

<!-- S45 -->
Och program som redan hade
filen öppen kan fortsätta använda den,
trots att namnet
de öppnade den med är borta.

<!-- S46 -->
Det är Unix-beteende.
På NTFS.
Dokumenterat av Microsoft.

<!-- S47 -->
Båda systemen klarar båda sakerna.
Det som skiljer är standardläget.
Det du får när du öppnar en fil
utan att tänka på det.

<!-- S48 -->
I Windows får du ett kontrakt.
I Unix får du en referens
till ett objekt.

<!-- S49 -->
Vilket låter som en fråga
för programmerare,
ända tills man har sett
just det här meddelandet.

<!-- S50 -->
Starta om datorn
för att slutföra installationen av uppdateringarna.

<!-- S51 -->
Anta att Windows måste byta ut
ett bibliotek som en process
har öppet enligt det strikta kontraktet.

<!-- S52 -->
Det går inte att byta ut filen
medan processen körs.
Så något måste släppa taget.

<!-- S53 -->
Avsluta programmet.
Stoppa tjänsten.
Eller lämna hela jobbet
till Omstartshanteraren.

<!-- S54 -->
Det är en faktisk systemkomponent.
Den stänger ner saker i ordning.
Windowsprogram,
sedan konsolprogram,

<!-- S55 -->
sedan tjänster,
och Utforskaren sist.
Sedan startar den dem igen.

<!-- S56 -->
Och den finns av ett enda skäl,
som Microsoft säger rakt ut
i sin egen dokumentation.

<!-- S57 -->
Det främsta skälet
till att programinstallationer
och uppdateringar kräver
en omstart av systemet...

<!-- S58 -->
är att några av filerna
som håller på att uppdateras används just nu
av ett program
eller en tjänst som körs.

<!-- S59 -->
Det vore för snyggt om det slutade där.
Delningsreglerna är inte enda skälet
till att en dator ber om omstart.

<!-- S60 -->
En kärnuppdatering är något annat.
Kärnan går inte att byta ut
medan den själv körs.

<!-- S61 -->
Linux har samma problem,
även om live-patchning
ibland kan undvika en omstart.

<!-- S62 -->
Så den ärliga versionen
lovar mindre än
den tillfredsställande.

<!-- S63 -->
Sättet Windows hanterar filer
som används gjorde vissa delar
svårare att byta i drift,
och det bidrog.

<!-- S64 -->
För varje designval
har en konsekvens någonstans.

<!-- S65 -->
Windows låter programmet
som öppnar filen bestämma
vad andra får göra med den.

<!-- S66 -->
Priset är att du ibland
inte kan radera din egen fil,
eftersom ett annat program
inte har tillåtit det.

<!-- S67 -->
Unix håller namnet
och objektet isär,
så många saker går att byta ut
medan systemet körs.

<!-- S68 -->
Priset är en halv gigabyte
som försvann från disken
och inte tillhör någon fil alls.

<!-- S69 -->
Och se på hur vart och ett
av dem löses.
I Windows är en väg ut
att stänga programmet
som håller filen.

<!-- S70 -->
I Linux är ett sätt
att få tillbaka utrymmet
att starta om tjänsten
som fortfarande har filen öppen.

<!-- S71 -->
Olika orsaker.
Ibland samma åtgärd.

<!-- S71b -->
Förresten, om du vill se
vart nästa fråga tar oss,
prenumerera gärna.
Det hjälper kanalen mycket.

<!-- S72 -->
Så. Frågan från början.
Vad betyder det
att öppna en fil?

<!-- S73 -->
Det betyder att du håller i något.
De två systemen ger dig
helt enkelt olika saker att hålla i.

<!-- S74 -->
Det är därför meddelandet
aldrig egentligen sa
att filen inte går att radera.

<!-- S75 -->
Det sa att programmet
som öppnade den
inte gav dig tillåtelse.

<!-- S75b -->
Och det vet vilket program.
Det nämnde det bara inte.
