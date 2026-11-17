<!-- S01 -->
Här är alla manus
som någonsin skrivits för den här kanalen.
158 videor,
nästan en och en halv miljon byte text.

<!-- S02 -->
Kör dem genom ett vanligt komprimeringsprogram
som heter gzip.
Ut kommer drygt en halv megabyte.
Nästan två tredjedelar borta.

<!-- S03 -->
Och ingenting går förlorat.
Packa upp filen,
så kommer vartenda manus tillbaka,
bokstav för bokstav.

<!-- S04 -->
Komprimera den nu igen.

<!-- S05 -->
Den blir större.
98 byte större.

<!-- S06 -->
En tredje gång.
98 byte större.
En fjärde.
98 igen.

<!-- S07 -->
Första rundan slänger två tredjedelar.
Den andra hittar ingenting alls.
Så varför kan vi inte bara fortsätta komprimera?

<!-- S08 -->
Låt oss titta in i den andra filen.
gzip komprimerade ingenting.
Den kopierade över datan oförändrad,
i sexton block.

<!-- S09 -->
Varje block fick en etikett på fem byte.
Lägg till ett litet huvud och en avslutning,
så blir det exakt 98.

<!-- S10 -->
När ett komprimeringsprogram inte hittar något att ta bort
sparar det datan som den är
och lägger bara till det som behövs för att packa upp den.

<!-- S11 -->
Så varför hittade andra rundan ingenting?
Och skulle ett smartare program göra det?

<!-- S12 -->
Sådan här text är full av upprepningar.
Samma ord, samma fraser,
samma små scenmarkeringar
i början av varje scen.

<!-- S13 -->
1977 publicerade Jacob Ziv och Abraham Lempel
ett enkelt knep.
Skriv inte en upprepning en gång till.
Peka tillbaka dit där den stod.

<!-- S14 -->
Gå tillbaka 300 tecken
och kopiera de tolv som följer.
Några få byte i stället för tolv.

<!-- S15 -->
Det andra knepet:
ge vanliga bokstäver korta koder
och ovanliga långa.

<!-- S16 -->
1951 kunde David Huffman,
doktorand vid MIT,
antingen skriva slutprovet
eller skriva en uppsats i stället.

<!-- S17 -->
Uppgiften, som Robert Fano hade gett,
gick ut på att hitta den effektivaste koden
av just det här slaget.

<!-- S18 -->
I månader kom Huffman ingenstans.
Han gav upp
och började plugga till provet.
Då kom han på det.

<!-- S19 -->
Ta de två ovanligaste symbolerna,
slå ihop dem till en
och upprepa tills det bara finns ett enda träd kvar.

<!-- S20 -->
Han kallade det senare
”det mest unika ögonblicket i mitt liv”.

<!-- S21 -->
Fano hade inte berättat för klassen
att han själv hade kämpat med det,
och det hade Claude Shannon också.

<!-- S22 -->
Huffmans kod slog bådas metoder.
Och det går att bevisa
att ingen kod av det slaget gör det bättre.

<!-- S23 -->
I början av 1990-talet
kombinerade Phil Katz båda knepen
för ZIP-filer.
gzip använder samma metod.

<!-- S24 -->
Första rundan har redan förbrukat
de mönster som gzip kan hitta.

<!-- S25 -->
Det som är kvar ger den inget att arbeta med.
För gzip ser det ut som brus.

<!-- S26 -->
Men ett smartare program
kanske ser mönster som gzip missade.
Skulle något program en dag kunna
krympa allt du ger det?

<!-- S27 -->
Nej.
Och du behöver inte veta hur det fungerar
för att vara säker på det.

<!-- S28 -->
Ta alla filer
som är exakt tre bitar långa.
Det finns åtta stycken.

<!-- S29 -->
Räkna nu alla som är kortare.
Fyra filer på två bitar,
två på en bit
och en tom fil.

<!-- S30 -->
Sju.

<!-- S30b -->
Åtta filer och sju kortare platser
att lägga dem på.

<!-- S31 -->
Om varenda en blev kortare
skulle två behöva dela på en plats.
Och när du packar upp den,
vilken menade du då?

<!-- S32 -->
Det kallas lådprincipen,
och den gäller för vilken längd som helst.
Det finns alltid en kortare fil för lite
för att räcka till alla.

<!-- S33 -->
Så ett komprimeringsprogram som tar emot alla filer
och krymper några av dem
måste göra andra större.
Inte för att det är dåligt skrivet.
De har ingen annanstans att ta vägen.

<!-- S34 -->
De där 98 byten
är priset som gzip betalar för det.

<!-- S35 -->
Välj vilket komprimeringsprogram du vill.
Av alla filer av en viss storlek
kan det krympa färre än en
av 250 med så mycket som en enda byte.

<!-- S36 -->
Komprimering fungerar ändå,
eftersom filerna vi skapar inte är slumpmässiga.
De är text, bilder och program,
fulla av mönster.

<!-- S37 -->
Det har inte hindrat folk
från att lova mer.

<!-- S38 -->
1992 tillkännagav WEB Technologies
programvara som påstods kunna pressa
nästan vilka data som helst under en kilobyte.
Till och med sin egen utdata,
om och om igen.

<!-- S39 -->
Företagets vice vd sa att metoden
”inte omfattades av
informationsteorins lagar”.
Produkten kom aldrig ut.

<!-- S40 -->
Så hur blir foton och musik
så mycket mindre?
De följer inte den här regeln alls.

<!-- S41 -->
En JPEG kommer inte tillbaka identisk.
Den kommer tillbaka tillräckligt lik.
Detaljer som ögat inte saknar
kastas bort för gott.

<!-- S42 -->
Zooma in,
så ser du vart de tog vägen.

<!-- S43 -->
Det är förstörande komprimering,
och det är en helt annan sak.
Den här videon handlar om den andra sorten.
Varenda bit tillbaka, exakt.

<!-- S44 -->
Så för filer som faktiskt har mönster:
hur små kan de bli?
Finns det en botten?

<!-- S45 -->
Ja, det gör det.
Den hittades 1948,
i samma artikel som ligger bakom vår video
om felrättande koder.

<!-- S46 -->
Där visade Claude Shannon
hur tillagd redundans skyddar ett meddelande.
Här räknade han ut
hur mycket av den man kan ta bort.

<!-- S47 -->
Hans svar var ett tal
som han kallade entropi:
hur svårt det är att gissa
vad som kommer härnäst.

<!-- S48 -->
Ingen förlustfri kod kan komma under det talet
i genomsnitt.
Men man kan komma det
hur nära som helst.

<!-- S49 -->
Så hur oförutsägbar är engelska?
1951 mätte Shannon det
med en lek.

<!-- S50 -->
Han gav någon ett textstycke
som personen aldrig hade sett
och bad hen gissa det,
bokstav för bokstav.

<!-- S51 -->
Om en gissning var fel
gissade hen igen,
tills det blev rätt.

<!-- S52 -->
Människor visade sig vara väldigt bra på det.
Med hundra bokstäver som sammanhang
landade engelska på ungefär en bit
per bokstav.

<!-- S53 -->
En dator lagrar varje bokstav
i åtta bitar.
En mänsklig läsare behöver ungefär en.

<!-- S54 -->
Den skillnaden ger utrymme för komprimering.
gzip fick ner kanalens manus
till under tre bitar per tecken.

<!-- S55 -->
Så hur nära en bit
kan en maskin komma?

<!-- S56 -->
Det finns ett pris för just det.
Det heter Hutter Prize,
och sedan 2020 gäller uppgiften en enda fil:
en gigabyte av engelska Wikipedia.

<!-- S57 -->
gzip krymper den till en tredjedel.
De bästa vanliga komprimeringsprogrammen
till ungefär en femtedel.

<!-- S58 -->
Rekordet, satt i juli 2026,
är drygt hundra miljoner byte.
En tiondel.

<!-- S59 -->
Och dekomprimeraren räknas också.
Dess storlek ingår i totalen,
så du kan inte gömma Wikipedia
inne i programmet.

<!-- S60 -->
Prispotten är 500 000 euro.
Varje procents förbättring
ger 5 000.

<!-- S61 -->
Marcus Hutter, som finansierar priset, förklarar varför:
”Att kunna komprimera väl
hänger nära ihop
med att handla intelligent.”

<!-- S62 -->
För programmen i toppen
letar inte efter upprepningar.
De förutsäger.

<!-- S63 -->
Före varje tecken
uppskattar de hur sannolikt
varje möjligt nästa tecken är.
En bra gissning kostar en bråkdel av en bit.

<!-- S64 -->
Det är Shannons gissningslek,
spelad av en maskin.
De bästa spelarna använder i dag neurala nätverk,
tränade att förutsäga vad som kommer härnäst.

<!-- S65 -->
Det fungerar till och med på redan komprimerade filer.
2016 började Dropbox packa om
användarnas JPEG-bilder med en bättre prediktor.
I snitt mer än en femtedel mindre.

<!-- S66 -->
Varje fil kom tillbaka bit för bit,
och fram till 2017
hade det sparat över 46 petabyte.
Det är över 46 000 terabyte.

<!-- S67 -->
Sedan har vi jättarna.
2023 använde forskare på DeepMind
en stor språkmodell
som komprimeringsprogram.

<!-- S68 -->
På små gråskaleutsnitt ur foton
slog den PNG:
48 procent av originalstorleken
mot 58.

<!-- S69 -->
På inspelningar av uppläst tal
slog den FLAC:
21 procent mot 30.

<!-- S70 -->
Men då är modellen inte medräknad.
Lägg till dess storlek,
så blir resultatet
140 gånger
större än datan.

<!-- S71 -->
Ett komprimeringsprogram som är större än sin data
har inte sparat något.
Programmet är en del av beskrivningen.

<!-- S72 -->
Och det leder oss till den märkligaste delen.
Här är den första miljonen siffror i π.

<!-- S73 -->
Mata in dem i fyra komprimeringsprogram.
Det bästa får ner dem till ungefär
426 000 byte.

<!-- S74 -->
Ge nu samma program
en miljon slumpmässiga siffror.
Samma resultat,
med en tiondels procents marginal.

<!-- S75 -->
Men π är inte slumpmässigt.
Det följer en matematisk regel.
Här är ett program som skriver ut
varenda siffra i den där miljonen.

<!-- S76 -->
362 byte.
Över 2 000 gånger kortare än filen.

<!-- S77 -->
Komprimeringsprogrammen kunde inte se
den matematiska regeln bakom π.
De såg bara siffrorna.

<!-- S78 -->
Ett sätt att mäta informationen
i data är att fråga:
hur kort kan ett program vara
och ändå skriva ut den?

<!-- S79 -->
Den längden kallas
Kolmogorovkomplexitet,
efter en av männen som beskrev den.

<!-- S80 -->
Det mesta data har inget kort program.
Det är lådprincipen igen:
det finns inte tillräckligt många korta program
för att räcka till alla.

<!-- S81 -->
En miljon slumpmässiga siffror
har med stor sannolikhet inget kortare.
π har det.

<!-- S82 -->
Så varför inte bara hitta
det kortaste programmet för vilken fil som helst?
För att det är bevisat
att ingen algoritm kan göra det
för varje fil.

<!-- S83 -->
Varje program ger dig en övre gräns.
Men inget kan alltid tala om för dig
om det finns ett kortare.
Du vet aldrig om du har nått botten.

<!-- S84 -->
gzip hittade upprepningarna i manusen
och inget mer.
Den ser byte,
inte vad orden betyder.

<!-- S85 -->
För att komma längre måste ett program
förutsäga dem bättre.
Och att förutsäga text bra
börjar likna att förstå den rätt mycket.

<!-- S86 -->
Så här är en fråga till dig.
Om ett program kunde komprimera Wikipedia
mer än något annat program,
skulle du säga att det förstår den?
Skriv ditt svar i kommentarerna.
