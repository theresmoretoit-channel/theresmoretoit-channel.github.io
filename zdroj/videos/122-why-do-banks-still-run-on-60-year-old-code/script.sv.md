<!-- S01 -->
Niohundranittionio pund
och nittionio pence.
Lägg till en penny.

<!-- S02 -->
Svaret är noll.

<!-- S03 -->
Inget felmeddelande. Ingen krasch.
Bara noll, tyst inskrivet på kontot.

<!-- S04 -->
I COBOL, när fältet för ett resultat
är för litet för att rymma det,
kan den extra siffran helt enkelt försvinna.
Om inte programmet ber om en varning
fortsätter beräkningen.

<!-- S05 -->
Och det avrundas inte heller.
Två pund och trettiofyra och en halv pence,
sparat på pennyn när,
blir två pund trettiofyra.

<!-- S06 -->
Skriv ett enda extra ord, ROUNDED,
så blir det två pund trettiofem.

<!-- S07 -->
Inget av det här är en bugg.
Det är regler.
Och många av världens banker
fungerar fortfarande enligt sådana regler.

<!-- S08 -->
COBOL är ett programspråk
från 1959.
Inte alla program skrivna i det är så gamla.
Men språket är det,
och dess vanor likaså.

<!-- S09 -->
Så varför har bankerna inte ersatt det?
De har pengarna.
De har ingenjörerna.

<!-- S10 -->
För att ta reda på det tittar vi på tre verkliga fall.
En bank som försökte lämna sitt gamla system,
en som lyckades,
och en kris där alla skyllde på COBOL.

<!-- S11 -->
Men först: den saknade halva pennyn.

<!-- S12 -->
Säg att du skriver om det där bankprogrammet
i ett modernt språk.
Du skulle nog rätta till de reglerna.
Ett för stort tal ger ett fel.
En halv penny avrundas uppåt.

<!-- S13 -->
Renare. Säkrare.
Och nu, varhelst en halv penny dyker upp,
ger ditt program ett annat resultat än det gamla.

<!-- S14 -->
Moderna språk kan räkna exakt med decimaler.
Java har en typ gjord just för det.
Men även där
är avrundningsregeln ett val.

<!-- S15 -->
En vanlig inställning avrundar uppåt vid exakt en halv:
två trettiofem.
En annan avrundar till närmaste jämna siffra:
två trettiofyra.
Båda är rätt. Bara en stämmer överens.

<!-- S16 -->
Och med vanliga flyttal,
den sort som de flesta program använder som standard,
blir det ännu konstigare.
Noll komma ett plus noll komma två
är inte noll komma tre.

<!-- S17 -->
Så att ersätta COBOL är ingen översättning.
Det handlar om att hitta varje sådan regel,
i miljontals rader,
och behålla var och en exakt som den var.

<!-- S18 -->
Hur hamnade det där från början?

<!-- S19 -->
I maj 1959
kallade USA:s försvarsdepartement
till ett möte i Pentagon.
Datortillverkare, myndigheter
och stora företag kom,
alla med samma problem.

<!-- S20 -->
Varje dator hade sitt eget språk.
Ett löneprogram skrivet för en maskin
var oanvändbart på en annan.

<!-- S21 -->
En kommitté utformade ett gemensamt språk
för näringslivet.
Störst inflytande hade FLOW-MATIC,
från Grace Hoppers team på Remington Rand.

<!-- S22 -->
Och i december 1960
kördes i stort sett samma COBOL-program
på två datorer
från konkurrerande tillverkare.
Det var hela poängen.

<!-- S23 -->
Det var gjort för att människor skulle kunna följa det.
ADD PAYMENT TO ACCOUNT-BALANCE.
Du kan nog gissa vad det gör.

<!-- S24 -->
Och det lagrade pengar som folk skriver dem:
som decimalsiffror.
Decimaltecknet
behöver inte ens lagras.
Fältets beskrivning anger var det hör hemma:
de två sista siffrorna är pence.

<!-- S25 -->
1964 lanserade IBM System/360.
Dess konstruktion innehöll instruktioner
för decimal aritmetik.

<!-- S26 -->
Och sedan dess har IBM byggt sina stordatorer
för att förbli kompatibla.
Många äldre program kan fortfarande köras
på dagens maskiner
utan att skrivas om.

<!-- S27 -->
Så det kom sällan ett ögonblick
som tvingade någon att byta.
Varje år fortsatte koden att fungera,
och varje år samlade den på sig fler regler.
Nya produkter, nya skatter, nya regleringar,
nya undantag.

<!-- S28 -->
Ingen har räknat hur mycket COBOL
som fortfarande körs i världen.
Men enligt IBM använder fyrtiofem
av världens femtio största banker
fortfarande IBM:s stordatorer.

<!-- S29 -->
Och en del ägare har faktiskt räknat.
2017 uppgav USA:s socialförsäkringsmyndighet
att dess system innehöll
över sextio miljoner rader COBOL.

<!-- S30 -->
2025 listade den amerikanska statens revisorer
de elva federala system
som mest behövde ersättas.

<!-- S31 -->
De var mellan tjugotre
och sextio år gamla
och kostade omkring sjuhundrafemtio
miljoner dollar om året att driva.

<!-- S32 -->
Så koden är gammal, den finns överallt,
och den är full av regler som ingen skrev ner.
Då måste väl faran ligga i att behålla den.

<!-- S33 -->
Låt oss se vad som händer
när en bank lämnar sitt gamla system.

<!-- S34 -->
2018 hade en brittisk bank vid namn TSB
omkring fem miljoner kunder
och ett problem.

<!-- S35 -->
Dess system var hyrda
från Lloyds Banking Group,
en konkurrent,
och avgifterna skulle stiga kraftigt.

<!-- S36 -->
Så TSB bestämde sig för att flytta allt
till en ny plattform,
byggd av bankens nya ägare,
den spanska banken Sabadell.

<!-- S37 -->
En helg i april.
På söndagskvällen
slogs det nya systemet på.

<!-- S38 -->
På måndagen gjordes omkring
niohundratusen inloggningsförsök.
Bara ungefär en inloggning på internetbanken
av tio lyckades.

<!-- S39 -->
Betalningar misslyckades.
Vissa kunder loggade in
och såg andra personers konton.

<!-- S40 -->
Det värsta varade ungefär en vecka.
TSB var inte tillbaka i normal drift
förrän i december.

<!-- S41 -->
Följderna kostade omkring
trehundratrettio miljoner pund
bara under 2018.
Tillsynsmyndigheterna lade senare till
böter på nästan fyrtionio miljoner.

<!-- S42 -->
Och här kommer det märkliga.
Kunddatan kom fram oskadd.
Det säger båda de officiella rapporterna.

<!-- S43 -->
Det som brast var den nya plattformen runt den.
Två datacenter, olika konfigurerade.
Prestandan testades bara i det ena,
och målen sänktes
när testerna inte gick igenom.

<!-- S44 -->
Och det fanns ingen väg tillbaka.
När datan väl hade flyttats
var en återgång till det gamla systemet,
med tillsynsmyndighetens ord,
”i praktiken omöjlig”.

<!-- S45 -->
TSB flydde inte från ett trasigt system.
Banken lämnade ett som fungerade,
på grund av vem som ägde det
och vad det kostade.
Det farliga var att lämna.

<!-- S46 -->
Så är det alltid en katastrof att lämna?

<!-- S47 -->
2008 gav sig Australiens Commonwealth Bank
i kast med att ersätta kärnsystem
som hade tjänat banken
i mer än fyrtiofem år.

<!-- S48 -->
Planen: omkring femhundraåttio
miljoner australiska dollar
och fyra år.

<!-- S49 -->
Det tog fem.
Pressen uppgav senare att totalen
låg på ungefär en komma en miljard,
i takt med att projektet växte.

<!-- S50 -->
Men banken flyttade inte allt
under en enda helg.
Inlåningskonton kom först, 2010.
Företagskonton följde 2011,
och lån 2012.

<!-- S51 -->
Varje steg var något banken
kunde följa, kontrollera och lära sig av
innan den satsade på nästa.

<!-- S52 -->
Till slut, säger banken,
blev den den första stora australiska banken
med banktjänster i realtid,
dygnet runt.

<!-- S53 -->
Så det går.
Men titta på vad det krävde.
Fem år, en mycket större nota
och tålamod.

<!-- S54 -->
Modernisering är inget köp.
Det är ett projekt,
med egna risker.

<!-- S55 -->
Och nu till krisen
där alla skyllde på COBOL.

<!-- S56 -->
Mars 2020.
När pandemin stängde ner New Jersey
steg antalet nya ansökningar om a-kassa
från under tiotusen på en vecka
till över hundrafemtiofemtusen.

<!-- S57 -->
Sexton gånger så många,
på sju dagar.
Arbetsmarknadsmyndigheten hann inte med.

<!-- S58 -->
I början av april bad guvernören
om frivilliga.
Inte bara vårdpersonal,
utan också folk som kunde COBOL.
Delstatens system, sa han,
var mer än fyrtio år gamla.

<!-- S59 -->
Historien spreds snabbt.
Uråldrig kod hade kollapsat
under pandemin.

<!-- S60 -->
Men när delstatens revisor
senare granskade saken,
hittades inga belägg
för att förseningarna hade orsakats
av datorsystemen.

<!-- S61 -->
Oberoende av det granskade journalister
felmeddelandena som folk fick se
och spårade många till webbplatsen som användarna mötte,
skriven i ett mycket nyare språk, Java.
Den gamla koden bakom fortsatte att gå.

<!-- S62 -->
Så varför behövde delstaten COBOL-programmerare?
För att kongressen ändrade reglerna.
Nya ersättningar, nya belopp,
nya personer som hade rätt till dem,
och varje ändring måste in
i koden, snabbt.

<!-- S63 -->
Problemet var inte att koden var gammal.
Det var att få kunde ändra den,
och att telefonlinjerna och personalen
också var överbelastade.

<!-- S64 -->
Tre fall.
En bank som lämnade ett fungerande system
och vars migrering misslyckades.
En bank som bytte system försiktigt
och lyckades.
Och en kris där den gamla koden fick skulden
och ingen kunde visa att den var orsaken.

<!-- S65 -->
Det betyder inte att gamla system aldrig fallerar.
Det gör de.
De blir dyra,
de som förstår dem går i pension,
och att vänta har också ett pris.

<!-- S66 -->
Men åldern är lätt att se,
och de verkliga riskerna är det inte.
Regler som ingen skrev ner.
Kunskap i några få personers huvuden.
Och ögonblicket när man byter.

<!-- S67 -->
Därför byter många banker inte ut
den gamla kärnan på en gång.
De kapslar in den.
Appen i din telefon är ny,
men den kanske pratar med något
mycket äldre.

<!-- S68 -->
Och de ersätter den bit för bit.
2004 döpte Martin Fowler, som skriver om mjukvara,
det här efter strypfikonet,
en regnskogsväxt som växer runt ett träd
tills den kan stå på egen hand.

<!-- S69 -->
Det gamla systemet fortsätter att arbeta
medan det nya växer runt det,
en uppgift i taget,
tills ingenting längre är beroende av det gamla.

<!-- S70 -->
Vilket för oss tillbaka till den halva pennyn.
Någonstans kan ett program fortfarande tappa den,
för att någon bestämde så,
för flera decennier sedan.
Att ersätta programmet innebär att veta det,
och allt annat av samma slag.

<!-- S71 -->
Det gamla systemet är inte nödvändigtvis
det som fallerar.
Ibland är det ersättaren.

<!-- S72 -->
För att byta ut tekniken
är inte samma sak som att ta bort risken.
Ibland flyttar det bara risken
till en enda helg i april.

<!-- S73 -->
Så här kommer en fråga till dig.
Om ett system har fungerat i fyrtio år,
när är rätt tid att ersätta det?
Och har du själv någon gång behövt ersätta ett?
Berätta i kommentarerna.
