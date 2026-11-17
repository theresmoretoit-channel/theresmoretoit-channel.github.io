<!-- S01 -->
948.
Så många olika sätt hittade en AI
att ta över en Linuxdator inifrån.

<!-- S02 -->
Inget stulet lösenord. Inget intrång utifrån.
Varje fall börjar med en vanlig användare
utan några särskilda rättigheter,
och slutar med root,
kontot som kan göra vad som helst.

<!-- S03 -->
OpenAI publicerade resultatet i november 2026.
Hela körningen kostade
1,2 miljoner dollar i API-krediter.

<!-- S05 -->
Det här är OpenAI:s egna siffror,
publicerade dagen innan
de lanserade modellen som tog fram dem,
och ingen utomstående har bekräftat hela antalet.
Men hundratals rapporter och patchar
har redan skickats ut.

<!-- S06 -->
Därför spelar det här roll bortom Linux.
Linux källkod är offentlig.
Vem som helst kan läsa den.
I årtionden var det argumentet
för att den är säker.

<!-- S07 -->
Så om en maskin kan läsa offentlig kod
och göra om den till fungerande exploits i den här skalan,
borde mjukvara ändå hålla sin kod hemlig?

<!-- S08 -->
Titta på mjukvara som redan gör det.
I april 2026 rättade Microsoft
164 säkerhetsbrister
på sin månatliga patchdag.
I oktober rättade företaget
1 413.

<!-- S09 -->
Under den enda månaden rättade det fler
än under något helt år dessförinnan.
Över 1 000 av rättelserna gällde Windows,
och Microsoft hade varnat för
att dess egna AI-verktyg skulle driva ökningen.

<!-- S10 -->
Du kan inte jämföra de två siffrorna direkt.
Företag räknar olika,
och Microsoft sökte i sin egen privata kod.

<!-- S11 -->
Men det visar en sak.
Att hålla koden privat
hade inte hållit buggarna borta.

<!-- S12 -->
Så vad skyddar dig egentligen?
För att svara på det
måste vi se hur den här maskinen fungerar,
för varje steg i den sållar bort något.

<!-- S13 -->
Linuxkärnan har
mer än 40 miljoner rader kod.
Först gick spaningsagenter igenom den
och valde ut de delar
som en vanlig användare faktiskt kan nå.

<!-- S14 -->
Kvar blev ungefär 7 %.
Det är den del de bedömde värd att angripa,
inte ett slumpmässigt urval,
så du kan inte multiplicera resultatet med 14.

<!-- S15 -->
Sedan gick analysagenter igenom den koden
och listade allt som verkade misstänkt.
2 308 kandidater
på 12 timmar.

<!-- S16 -->
Men en misstanke bevisar ingenting.
Så andra agenter skrev testprogram
och körde dem på isolerade virtuella maskiner.
1 724 buggar
visade sig vara verkliga.

<!-- S17 -->
Sedan kom den dyra delen:
att bygga fungerande exploits,
med standardskydden
i ett vanligt skrivbordssystem påslagna.
1 169
nådde root.

<!-- S18 -->
Gruppera dem efter den underliggande bristen,
så får du de 948.

<!-- S19 -->
Det finns en detalj i rapporten
som är svår att glömma.
I en tidig körning
rapporterade agenterna 200 lyckade försök.
Sedan kontrollerade människor hur de hade kommit dit.

<!-- S20 -->
Tjugo av dem hade nått root
genom en annan, okänd bugg,
inte den de hade fått i uppdrag att använda.
Utskickade för att öppna en dörr
hittade de en annan som ingen kände till.

<!-- S21 -->
I ett urval av sina exploits
identifierade OpenAI tio exploateringstekniker
som externa experter inte hade sett förut.

<!-- S22 -->
I juli hittade en tidigare modell
166 av de här bristerna.
Tre månader av rättelser senare
hittade den nyare modellen 948.
Buggarna hade inte tagit slut.
Den senare körningen hittade betydligt fler.

<!-- S23 -->
Nu finns det en viktig begränsning.
Inget av det här tar sig in i din dator
över internet.
Angriparen måste redan finnas på maskinen,
som en vanlig användare.

<!-- S24 -->
Det är mindre lugnande än det låter,
för verkliga attacker sker ofta i två steg.
Först tar man sig in,
via en brist i webbläsaren eller en skadlig nedladdning.
Sedan behöver man root.
Det här är det andra steget.

<!-- S25 -->
OpenAI:s råd är rakt på sak.
På ett system utan de senaste patcharna:
behandla varje vanligt konto som root,
åtminstone mot en välfinansierad angripare.

<!-- S26 -->
Så vad betyder det
för det gamla argumentet för öppen kod?
I slutet av nittiotalet
gav Eric Raymond det en slogan:
”Med tillräckligt många ögon är alla buggar ytliga.”

<!-- S27 -->
Han kallade det Linus lag.
Det är en fin idé, med ett antagande inbyggt:
att någon faktiskt tittar.

<!-- S28 -->
2014 dök en bugg som kallades Heartbleed upp
i OpenSSL,
koden som skyddade en stor del av webben.
Omkring en halv miljon säkra servrar
ansågs vara exponerade.

<!-- S29 -->
Buggen hade legat i offentlig kod i två år.
Projektet fick
ungefär 2 000 dollar om året i donationer
och hade en enda heltidsanställd utvecklare.

<!-- S30 -->
Vem som helst kunde läsa den.
Nästan ingen gjorde det.

<!-- S31 -->
Det var alltid öppen källkods verkliga svaghet.
Inte för många ögon på koden. För få.

<!-- S32 -->
Och det är den delen som AI förändrar.
En maskin kan fortsätta skanna
och undersöka betydligt fler kandidater
än en mänsklig forskare skulle hinna med ensam.
Det gamla löftet hålls äntligen,
för alla, angripare inräknade.

<!-- S33 -->
Så offentlig kod granskas verkligen nu.
Hjälper det att gömma den?

<!-- S34 -->
Ett slutet program måste ändå köras,
så dess maskinkod finns
på varje dator som använder det.
Verktyg som Ghidra gör om den
till något som liknar källkod.

<!-- S35 -->
Och det finns ett klassiskt knep.
Jämför ett program
före och efter en säkerhetsuppdatering.
Det som ändrats visar dig var hålet fanns.

<!-- S35b -->
Det visar angripare var de ska sikta,
långt innan varje system
har installerat uppdateringen.

<!-- S36 -->
Anthropic testade det här på Windows-kärnan,
med 21 brister
som Microsoft nyligen hade patchat,
och utan källkod.
AI:n framkallade den första kraschen efter 31 minuter.
Inom sex timmar hade den 18.

<!-- S37 -->
Åtta blev fungerande exploits
som kunde ta full kontroll över maskinen,
för ungefär 2 000 dollar styck.

<!-- S38 -->
Men det här var inga okända buggar.
Patcharna pekade redan
på var problemen fanns.
Att hitta en ny brist från grunden är svårare.

<!-- S39 -->
Så hemlighållande kostar fortfarande angriparen något.
Det är ett farthinder, inte en mur.
Hur högt är hindret?
Det finns ingen offentlig siffra.

<!-- S40 -->
Hur är det med den andra sidan?
Vad ger öppenhet dig egentligen?
Svaret finns i en liten detalj
i OpenAI:s rapport.

<!-- S41 -->
Under de tio dagarna av skanning och analys
var över 100 av de här Linuxbristerna
redan rättade, eller på väg att bli det,
av andra människor.
Omkring 300 till
diskuterades redan offentligt.

<!-- S42 -->
Andra hittade samma buggar
samtidigt.

<!-- S43 -->
Linus Torvalds hade beskrivit det redan i maj.
Han sa att AI-rapporter
hade gjort kärnans e-postlista för säkerhet
”nästan helt ohanterlig”,
eftersom olika personer hela tiden hittade
samma saker med samma verktyg.

<!-- S44 -->
Och hans råd var det här:
”Om du hittade en bugg med AI-verktyg
är chansen stor att någon annan också hittade den.”

<!-- S45 -->
Kärnans regler säger det nu rakt ut.
En bugg som hittats med AI ska behandlas som offentlig,
eftersom sådana buggar dyker upp
hos flera forskare,
ofta samma dag.

<!-- S46 -->
Tänk på vad det gör
med idén om en hemlig bugg.
Om den var billig för dig att hitta,
var den billig för alla.

<!-- S47 -->
Med öppen källkod
kan vem som helst granska rapporten,
kontrollera rättelsen och ifrågasätta resultatet.
Med sluten mjukvara
får du oftast lita på leverantören.

<!-- S49 -->
Men öppenhet har ett pris,
och det är inte det du skulle tro.
Det är frestande att säga
att ett litet projekt inte har råd med skanningen.
AI-företag erbjuder redan
underhållare gratis tillgång.

<!-- S50 -->
Det som saknas är människor.
Kärnan brukade registrera
omkring 500 säkerhetsärenden per version.
I år passerade den 1 500.
Många är små,
men någon måste ändå gå igenom dem.

<!-- S51 -->
I januari avslutade curl-projektet
sitt betalda bug bounty-program,
för att sluta belöna en flod av skräprapporter.

<!-- S52 -->
Även bra rapporter flyttar bara arbetet vidare.
AI-genererade patchar behöver fortfarande granskas av människor.
Några tidiga rättelser lade till onödig kod
eller missade andra varianter av samma bugg.

<!-- S53 -->
Du kan köpa mer skanning.
Du kan inte köpa fler människor
som förstår en bit kod så väl.
Här har ett företag med ett betalt säkerhetsteam
verkligen ett försprång.

<!-- S54 -->
Och sedan kommer det sista problemet.
Rättat är inte samma sak som installerat.

<!-- S55 -->
I mars 2017
patchade Microsoft en brist i Windows.
Sluten källkod, en leverantör, ett uppdateringssystem.
Två månader senare
tog sig WannaCry igenom samma hål,
in i omkring 200 000 datorer
i ungefär 150 länder.

<!-- S56 -->
Den patchen hade två månader på sig att spridas,
och det räckte inte.
En angripare ger dig kanske inte längre två månader.
I samma studie från Anthropic
tog AI:n en offentlig rättelse
för Firefox JavaScript-motor
och hade en fungerande exploit på under en timme.

<!-- S57 -->
Den rättade versionen av Firefox
låg fortfarande 18 dagar bort.

<!-- S58 -->
Det här är faran med att publicera en rättelse.
Informationen kan nå angripare
innan uppdateringen når dig.

<!-- S59 -->
En rättelse i Linux har en lång väg att färdas,
från kärnan till en stabil version,
till din distribution, till din enhet.
En telefon kan få vänta i månader, eller för alltid.

<!-- S60 -->
Och sluten mjukvara slipper inte undan.
Vi såg det nyss: Windows-patchen räckte.
Varje uppdatering är nu också en karta.

<!-- S60b -->
Så håll allt uppdaterat,
datorn, telefonen, till och med routern,
och installera uppdateringar så fort de kommer.
I takt med att AI blir bättre på att göra rättelser till attacker
kommer varje dag du väntar att betyda mer.

<!-- S61 -->
Så, är öppen källkod fortfarande säkrare?
Ärligt talat vet ingen det.
Såvitt det är offentligt känt
har ingen kört samma test på båda sidor
under samma regler.

<!-- S62 -->
Det vi kan säga är mer blygsamt.
Att gömma kod ger mindre än det brukade.
Att visa den låter vem som helst kontrollera arbetet
och lägger ännu mer av det arbetet
på dem som underhåller koden.

<!-- S64 -->
Även om AI aldrig hittar varje bugg
har den redan ändrat vad det kostar att hitta dem.

<!-- S65 -->
Det som räknas nu är hur länge ett hål står öppet
mellan ögonblicket då någon hittar det
och ögonblicket då det stängs på din maskin.

<!-- S66 -->
Så här kommer en fråga till dig.
Om vilken bugg som helst kan hittas av vem som helst,
skulle du hellre lita på kod du kan läsa,
eller på ett företag som får betalt för att rätta den?
Skriv gärna i kommentarerna.
