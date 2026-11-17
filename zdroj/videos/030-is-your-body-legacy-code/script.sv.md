<!-- S01 -->
Tänk dig ett datorprogram
med tre miljarder tecken
instruktioner.

<!-- S02 -->
Och varje gång du
startar en ny process
kopierar du in hela programmet.

<!-- S02b -->
Två gånger.

<!-- S03 -->
Inte bara de funktioner
som processen behöver.
Alltihop.
Varje modul.
Varje beroende.
Varje bit uråldrig legacy-kod.

<!-- S04 -->
Och sedan ignorerar processen
helt enkelt nittionio procent.
Det vore fruktansvärd
mjukvaruutveckling.

<!-- S05 -->
Och ändå...

<!-- S06 -->
...är det ungefär det
dina celler gör.

<!-- S07 -->
Nästan varje cell i din kropp
som har en cellkärna
innehåller i princip samma
fullständiga kopia av ditt genom.

<!-- S08 -->
En neuron har den.
En levercell har den.
En hudcell har den.
Och ändå beter de sig
helt olika.

<!-- S09 -->
Koden finns där.
Det mesta av den används bara inte.

<!-- S10 -->
En gen kan man,
mycket grovt,
se som en funktion eller en modul.

<!-- S11 -->
Den bär information
som till slut kan ge upphov
till en viss
funktionell produkt,
ofta ett protein.
Vi kan tänka oss ungefär så här.

<!-- S12 -->
Men att ha funktionen i koden
betyder inte att den körs.
Något måste starta den.
Och det är där biologin
blir intressant.

<!-- S13 -->
För i en dator
skriver jag bara det här.
Eller i maskinkod.

<!-- S14 -->
Processorn vet precis vad den ska göra.
Det finns en instruktion.
Det finns en adress.
Det finns en instruktionspekare.

<!-- S15 -->
Men en cell har ingen processor
som betar av DNA-instruktioner
en i taget.

<!-- S16 -->
Så...

<!-- S17 -->
...hur vet den vad den ska använda?

<!-- S18 -->
Här börjar jämförelsen
med datorn bli konstig.
I en dator kan du hoppa
till en bestämd minnesadress.

<!-- S19 -->
Du kan ha åtkomsträttigheter.
Du kan ha processer.
Du kan ha konfigurationsfiler.
Du kan ha händelser
som utlöser bestämda kodstycken.

<!-- S20 -->
Biologin har saker
som spelar förvånansvärt lika roller.

<!-- S21 -->
Transkriptionsfaktorer binder
till bestämda DNA-sekvenser
och påverkar om en gen
transkriberas eller inte.

<!-- S22 -->
Reglerande DNA-sekvenser påverkar
när och var gener uttrycks.
Kromatinets struktur styr
hur åtkomliga enskilda
DNA-avsnitt är.

<!-- S23 -->
Och celler tar hela tiden emot
signaler från sin omgivning.

<!-- S24 -->
Så i stället för en processor,
en instruktionspekare,
en minnesadress och körning...

<!-- S25 -->
...har du snarare något sådant här.

<!-- S26 -->
Det finns ingen enda instruktionspekare.
Det finns ett enormt nät
av molekylära samspel.

<!-- S27 -->
DNA:t finns där.
Men olika delar av det
är mer eller mindre åtkomliga
för det molekylära maskineri
som läser dem.

<!-- S28 -->
Att ha koden
är alltså inte samma sak
som att ha tillgång till den.
En levercell behöver inte radera
alla neurongener.
Det räcker att den styr
om de används.

<!-- S29 -->
Tillbaka
till vårt mjukvaruprojekt.
Säg att du utvecklar
en enorm applikation.

<!-- S30 -->
Du skapar en modul som heter finger.
Och i stället för att importera
de få funktioner den behöver...

<!-- S31 -->
...kopierar du in hela
repositoriet människa.

<!-- S32 -->
Hjärnan.
Levern.
Hjärtat.
Immunförsvaret.
Fortplantningsorganen.
Allt.

<!-- S33 -->
Och det gör du igen...

<!-- S34 -->
...för varenda cell.

<!-- S35 -->
Som programmerare
skulle du nog fråga...
Vem har designat det här?

<!-- S36 -->
Och svaret är...

<!-- S37 -->
Ingen.

<!-- S38 -->
Nja... Inte riktigt ingen.
Evolutionen.

<!-- S39 -->
Och evolutionen har en helt annan
utvecklingsfilosofi.

<!-- S40 -->
Tänk dig att du öppnar ett repositorium
som heter människa,
vars commit-historik
sträcker sig miljarder år bakåt.

<!-- S41 -->
Ingen arkitekt satte sig ned
och ritade version 1.0.
Det gjordes aldrig någon ren omskrivning.
Det kom aldrig någon människa version två
med ny arkitektur.

<!-- S42 -->
I stället...
Lägg till funktion.
Lappa bugg.
Duplicera modul.
Återanvänd gammal modul.

<!-- S43 -->
Gå runt begränsning.
Lägg till ännu en nödlösning.
Behåll gammalt API,
för något beror på det.

<!-- S44 -->
Igen.
Och igen.
Och igen.
I miljarder år.

<!-- S45 -->
Evolutionen frågar inte
vad den renaste arkitekturen är.
Dess fråga är mycket enklare.
Fortplantar sig den här
organismen framgångsrikt?

<!-- S46 -->
Om svaret är ja
överlever koden.

<!-- S47 -->
Tänk dig att du ärver ett projekt
som har underhållits
av miljontals programmerare,
i miljarder år,
och du har ingen som helst möjlighet
att skriva om alltihop.

<!-- S48 -->
Du stöter på något och frågar...
Varför finns det här?
För att något berodde på det.

<!-- S49 -->
Varför är det här API:et så konstigt?
Legacy.

<!-- S50 -->
Det här är evolutionen.
Det ultimata legacy-systemet.
Den refaktorerar inte.
Den ändrar det som redan finns.

<!-- S51 -->
Och efter miljarder år...

<!-- S52 -->
...blir det vi.

<!-- S53 -->
Modern mjukvaruutveckling
vilar på en ganska förnuftig tanke.
Du gör en ändring.
Sedan testar du den.

<!-- S54 -->
Commit.
Bygge.
Enhetstester.
Integrationstester.
Driftsättning.

<!-- S55 -->
Biologin har något
som ser ungefär likadant ut.
En mutation uppstår.

<!-- S56 -->
Och sedan...
Organismen antingen överlever
och fortplantar sig.
Eller inte.

<!-- S57 -->
Det finns ingen stagingmiljö.
Det finns ingen rollback.

<!-- S58 -->
Och ibland
händer något mycket värre.
En mutation kan göra en cell
bättre på att överleva och föröka sig
inne i organismen.
Det kan bidra till cancer.

<!-- S59 -->
Biologin har alltså en rätt
skräckinjagande continuous integration.
Testerna körs
på produktionssystemet.

<!-- S60 -->
Men det är just här
som jämförelsen med mjukvara
blir ännu mer intressant.
När du tittar på människokroppen
är det frestande att föreställa sig
något sådant här.

<!-- S61 -->
Men så fungerar
systemet inte alls.
Det finns ingen central server
som skickar order till varje cell.

<!-- S62 -->
Dina celler bevakar hela tiden
sin närmaste omgivning.
De tar emot kemiska signaler.
De har kontakt med grannceller.
De reagerar på hormoner.

<!-- S63 -->
En cell får aldrig
ett meddelande som säger...

<!-- S64 -->
...cell nummer sju miljoner
trehundranittiotvå tusen
etthundraåttiofyra.
Uttryck gen X nu, tack.

<!-- S65 -->
Om du programmerar
blir plötsligt ett annat
begrepp användbart.
Distribuerade system.

<!-- S66 -->
Dina celler är i praktiken
ett oerhört antal
enskilda agenter.
Var och en har eget tillstånd.
Egna sensorer.
Egna indata.
Egna svar.

<!-- S67 -->
Det finns ingen jättelik loop
som säger varje cell vad den ska göra.
Närmare ligger ett
multiagentsystem.
Eller en svärm.
Eller en cellulär automat.

<!-- S68 -->
Enkla lokala regler...

<!-- S69 -->
...som ger upphov till häpnadsväckande
komplicerat samlat beteende.

<!-- S70 -->
Och en sak till som vore
oacceptabel i vanlig mjukvara.
Din kropp har kört
oavbrutet i årtionden.

<!-- S71 -->
Ingen omstart.
Inget planerat underhållsfönster.

<!-- S72 -->
Och ändå förändras
systemet hela tiden.
Celler dör.
Nya bildas.
Proteiner byggs upp och bryts ner.

<!-- S73 -->
DNA kopieras.
Skador repareras.
Delar byts ut.

<!-- S74 -->
Systemet stängs inte av
för att underhåll ska hinnas med.
Det underhåller sig
under full drift.

<!-- S75 -->
Nästan som om du hade en server
som byter ut sina egna delar
just i det ögonblick
då den betjänar anrop...

<!-- S76 -->
...och aldrig går offline.

<!-- S77 -->
Celler har eget maskineri.
De kommunicerar.
De svarar.
De reglerar varandra.
De bildar vävnader.
Vävnader bildar organ.
Organ bildar system.
Och system bildar en organism.

<!-- S78 -->
Och det finns ingen enskild del
som håller hela arkitekturen
i huvudet.

<!-- S79 -->
Och på något sätt...

<!-- S80 -->
...fungerar det.

<!-- S81 -->
Inte perfekt.
Långt ifrån perfekt.

<!-- S82 -->
Men tillräckligt bra för ögon.
Hjärtan.
Immunförsvar.
Hjärnor.

<!-- S83 -->
Och för organismer som kan skriva
mjukvara för att klaga på
hur uselt systemet
är designat.

<!-- S84 -->
Vi kallar DNA för kod.
Och jämförelsen är användbar.
Gener liknar lite funktioner.
Mutationer liknar lite
ändringar i källkoden.

<!-- S85 -->
Men det finns
en viktig skillnad.
DNA är nämligen ingen
fullständig ritning över en människa.

<!-- S86 -->
Ingenstans står det en rad...
Skapa en arm.
Skapa ett öga.
Skapa ett hjärta.

<!-- S87 -->
DNA deltar i stället
i ett enormt nät av samspel
med molekyler, celler,
fysikaliska krafter, kemiska gradienter,
tajming och omgivning.

<!-- S87b -->
Organismen uppstår ur alltihop.

<!-- S88 -->
DNA förstås alltså bättre som en
uppsättning instruktioner och regler
inbäddad i ett fysiskt system...

<!-- S89 -->
...än som en fullständig
källkodslistning för en människa.
Och det är faktiskt mycket konstigare.

<!-- S90 -->
Vi kan sekvensera ett genom,
identifiera gener
och mäta proteiner.

<!-- S91 -->
Men vi kan fortfarande inte ta DNA
ur en vanlig mänsklig cell,
lägga in det i en dator,
trycka på kör...

<!-- S92 -->
...och se den människan växa fram.

<!-- S93 -->
Vi har genomet.
Men genomet
är inte hela maskinen.

<!-- S94 -->
Och där hamnar vi.
Vi började med en välbekant idé.
DNA är som datorkod.

<!-- S95 -->
Och jämförelsen visar sig
vara förvånansvärt användbar.
Men ju djupare vi tittar,
desto konstigare blir systemet.

<!-- S96 -->
Det finns ingen processor.
Det finns inget operativsystem.
Det finns ingen central server.

<!-- S97 -->
Det finns ingen programmerare.
Det finns inget GitHub.
Det finns ingen kodgranskning.
Det finns ingen stagingmiljö.
Det finns ingen rollback.
Det finns knappt ens
en ren arkitektur.

<!-- S98 -->
Det finns biljoner små agenter
som var och en följer lokala regler,
stämmer av med grannarna,

<!-- S99 -->
använder ett enormt, uråldrigt,
ständigt ändrat repositorium...
Och på något sätt blir det
en fungerande organism.

<!-- S100 -->
Så om biologi är mjukvara...

<!-- S101 -->
...är den nog det äldsta,
rörigaste och mest överkonstruerade
legacy-system man kan tänka sig.

<!-- S102 -->
Ett system med miljarder år
av commits.
Nästan ingen refaktorering.
Ingen central administratör.
Och absolut ingen omstart.

<!-- S103 -->
Och på något sätt...

<!-- S104 -->
...har det kört i produktion
i miljarder år.
