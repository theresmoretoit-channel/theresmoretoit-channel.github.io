<!-- S01 -->
Den 19 juli 2024
skickade säkerhetsföretaget CrowdStrike
ut en rutinuppdatering.

<!-- S02 -->
Inte ett nytt program.
Bara en liten konfigurationsfil.

<!-- S03 -->
Inom några timmar hade 8,5 miljoner
Windowsdatorer stannat
på en blå skärm.

<!-- S04 -->
Flygbolag ställde in flyg.
Sjukhus ställde in operationer.
En nyhetskanal slutade sända.

<!-- S05 -->
Och misstaget bakom det
var helt vanligt.
Programmet väntade sig 20 värden.
Uppdateringen gav det 21.

<!-- S06 -->
Dina spel och appar gör
sådana misstag hela tiden.
När det händer stängs spelet,
och du startar det igen.

<!-- S07 -->
Samma sorts bugg.
Den ena stänger ett fönster.
Den andra stoppar
8,5 miljoner maskiner.

<!-- S08 -->
Skillnaden ligger inte i misstaget.
Utan i var koden kördes.

<!-- S09 -->
Så varför kan inte ett program
ta över din dator...
och varför kunde det här?

<!-- S10 -->
Det har inte alltid varit så här.

<!-- S11 -->
På en PC med DOS på 1980-talet
fanns det inget i processorn som stoppade ett program.
Det kunde skriva var som helst i minnet
och prata direkt med hårdvaran.

<!-- S12 -->
Ett enda program som skrev
någonstans där det inte borde
kunde skriva över operativsystemet,
och hela maskinen frös.

<!-- S13 -->
Lösningen var att sluta lita på program
och låta processorn
stå för misstron.

<!-- S14 -->
1982 införde Intels processor 80286
skyddat läge, protected mode,
med fyra behörighetsnivåer.

<!-- S15 -->
De brukar ritas
som fyra ringar, den ena inuti den andra.

<!-- S16 -->
Ring 0 är i mitten.
Ring 3 är ytterst.

<!-- S17 -->
Och numreringen går baklänges.
Ju lägre nummer,
desto mer får koden göra.

<!-- S18 -->
Ring 0 tillhör kärnan,
den innersta delen av operativsystemet.
Den delar ut minne,
bestämmer vilket program som körs härnäst
och pratar med hårdvaran.

<!-- S19 -->
I ring 3 körs din webbläsare,
dina spel och din textredigerare.
Det kallas användarläge.

<!-- S19b -->
Windows, macOS och Linux
delar alla upp arbetet så här.
Kärnan i ring 0,
dina appar i ring 3.

<!-- S19c -->
Mobiler och Apples nyare Mac-datorer
använder ARM-kretsar i stället.
Där kallas nivåerna exception levels.
Annat namn, samma uppdelning:
en för kärnan, en för dina appar.

<!-- S20 -->
Processorn vet alltid
vilken ring den kör i.
Och den kontrollerar.

<!-- S21 -->
Vissa instruktioner fungerar bara i ring 0.
Att stänga av avbrott, till exempel,
eller att ändra hur minnet mappas.

<!-- S22 -->
När ett program i ring 3 försöker med en sådan,
vägrar processorn.
Den utlöser ett undantag
och lämnar över kontrollen till kärnan,
som oftast avslutar programmet.

<!-- S23 -->
Minnet behandlas likadant.
Varje minnessida är märkt
som antingen user eller supervisor.

<!-- S24 -->
Ett program i ring 3
som försöker läsa en supervisor-sida
får inte datan.
Det blir stoppat.

<!-- S25 -->
Din webbläsare och ditt spel
körs båda i ring 3.
Det som håller isär dem
är att vart och ett får sin egen minneskarta.
Det andra programmets minne
finns helt enkelt inte på den.

<!-- S26 -->
Så när ett spel kraschar
stannar skadan inne i spelet.
Kärnan städar upp.
Allt annat fortsätter.

<!-- S27 -->
Titta nu på CrowdStrike igen.
Dess drivrutin kördes i ring 0,
precis bredvid kärnan.

<!-- S28 -->
Ingenting ovanför ring 0
kan fånga ett sådant misstag.

<!-- S29 -->
Så Windows gjorde det enda säkra som återstod.
Det stoppade hela maskinen, med flit,
i stället för att fortsätta med minne
det inte längre kunde lita på.

<!-- S30 -->
Det är det som den blå skärmen är.

<!-- S31 -->
Och eftersom drivrutinen startade
varje gång Windows gjorde det,
kom kraschen tillbaka vid varje omstart.

<!-- S32 -->
Men det väcker en fråga.
Om din webbläsare inte får röra hårdvaran,
hur sparar den då någonsin en fil
eller skickar något över nätverket?

<!-- S33 -->
Den ber om det.

<!-- S34 -->
Programmet lägger sin begäran
i processorns register.
Vilken fil. Vart datan ska.
Hur mycket.

<!-- S35 -->
Sedan kör det en speciell instruktion.
På en modern PC heter den SYSCALL.

<!-- S36 -->
I det ögonblicket växlar processorn
från ring 3 till ring 0...

<!-- S37 -->
men den hoppar inte
vart programmet vill.
Den hoppar till en enda ingång
som kärnan har valt i förväg.

<!-- S38 -->
Kärnan kontrollerar begäran,
gör jobbet
och går tillbaka till ring 3.
Programmet rörde aldrig disken självt.

<!-- S39 -->
Det här är ett systemanrop,
och det händer hela tiden.

<!-- S40 -->
Vi räknade dem på en laptop.
Ett program som inte gör någonting alls
gör ändå 30.

<!-- S41 -->
Firefox, när det startade
och laddade en enda Wikipediasida,
gjorde ungefär 670 000
på 20 sekunder...
trots att vår räkning saktade ner det.

<!-- S42 -->
Vart och ett av dem
är en resa genom väggen och tillbaka.

<!-- S43 -->
Då återstår något konstigt.
Fyra ringar,
och vi har bara behövt två.

<!-- S44 -->
Vad hände med ring 1 och 2?

<!-- S45 -->
Idén med ringar är äldre än PC:n.
Multics, ett operativsystem
från slutet av 1960-talet,
hade åtta.

<!-- S46 -->
Tanken var lager av förtroende.
Systemets kärna i mitten,
mindre betrodda tjänster runt den
och programmen ytterst.

<!-- S46b -->
Intel ritade samma bild.
Ring 1 och 2 var tänkta
för lagren däremellan,
som drivrutiner och systemtjänster.
Mer betrodda än dina appar,
mindre än kärnan.

<!-- S47 -->
Två saker kom i vägen.

<!-- S48 -->
För det första var system som Unix och Windows NT
byggda för att köras
på många sorters processorer.

<!-- S49 -->
Och den enda uppdelning
som varje processor erbjöd
var två nivåer.
En för kärnan,
en för allt annat.

<!-- S50 -->
För det andra själva x86-processorn.
När den mappar minne
känner varje sida bara till två lägen.
User eller supervisor.

<!-- S51 -->
Ring 1 och 2 räknas som supervisor.
Så en drivrutin i ring 1
kunde ändå röra kärnans minne.
Den extra ringen skulle inte skydda mycket.

<!-- S51b -->
Några system använde dem ändå.
OS/2 lät vissa program kliva in i ring 2,
bara för att prata direkt med hårdvaran.

<!-- S51c -->
Och innan processorerna fick stöd
för att köra virtuella maskiner
flyttade Xen och VirtualBox gästsystemets kärna
till ring 1,
så att systemet under
kunde behålla ring 0 för sig självt.

<!-- S52 -->
2023 föreslog Intel
att ta bort ring 1 och 2 helt.

<!-- S53 -->
I december 2024 släppte Intel planen.
De finns kvar i din processor.
Nästan ingenting använder dem.

<!-- S54 -->
Hittills låter det lugnande.
Reglerna sitter i hårdvaran,
och hårdvaran kontrollerar varje åtkomst.

<!-- S55 -->
2017 hittade tre forskarlag,
oberoende av varandra,
en väg genom den väggen.

<!-- S56 -->
De kallade den Meltdown.
Och för att hänga med
behöver du känna till ett trick
som moderna processorer använder.

<!-- S57 -->
En processor väntar inte
på att en instruktion ska bli klar
innan den börjar på nästa.
Den kör i förväg
med instruktioner den troligen kommer att behöva.

<!-- S58 -->
Om den gissade fel
kastar den resultaten,
som om ingenting hade hänt.

<!-- S59 -->
Här är felet.
På drabbade Intel-kretsar
kunde ett program i ring 3 be
om en byte ur kärnans minne...

<!-- S60 -->
och processorn hämtade den
och skickade den vidare till de följande instruktionerna
innan den hade kontrollerat klart
om det var tillåtet.

<!-- S61 -->
Kontrollen misslyckades mycket riktigt.
Resultatet kastades.

<!-- S62 -->
Men de följande instruktionerna
hade redan använt den hemliga byten
för att dra in en bit
av programmets eget minne
i processorns cache.

<!-- S63 -->
Och cachen glömmer inte
bara för att resultatet annullerades.

<!-- S64 -->
Så programmet mäter
hur snabbt varje del av dess minne svarar.
Den del som svarar snabbt
avslöjar den hemliga byten.

<!-- S65 -->
En byte i taget
kunde ett vanligt program läsa
kärnans minne,
och alla hemligheter som låg där.
Lösenord och krypteringsnycklar inräknade.

<!-- S66 -->
Meltdown drabbade Intel-processorer
ända tillbaka till 1995.

<!-- S67 -->
Den offentliggjordes
den 3 januari 2018.

<!-- S68 -->
Lösningen kunde inte ändra kislet.
Så operativsystemen ändrade kartan.

<!-- S69 -->
Medan ditt program körs
är kärnans minne nu nästan helt
borttaget från dess karta.
Det finns inget där att hämta.

<!-- S70 -->
Men kom ihåg systemanropen.
Varje resa genom väggen
måste nu byta karta också.

<!-- S71 -->
Red Hat mätte patcharna mot Meltdown
och en besläktad brist, Spectre.
Under 1 % för vissa arbetsbelastningar...
upp till 19 % för hårt belastade databaser.

<!-- S72 -->
Regeln var rätt hela tiden.
Processorn kontrollerade den bara för sent.

<!-- S73 -->
Vilket för oss tillbaka till CrowdStrike,
och till en svårare fråga.

<!-- S74 -->
Varför låg ett säkerhetsprogram
i ring 0 från första början?

<!-- S75 -->
För därifrån ser det allt.
Det startar före annan programvara.
Och skadlig kod med administratörsrättigheter
har svårare att stänga av det.

<!-- S76 -->
Microsofts egen lista
slutar med en varning.
Drivrutiner i kärnan ger det på bekostnad av driftsäkerheten.

<!-- S77 -->
Efter avbrottet
började Microsoft bygga ett sätt
för antivirusprogram
att köras utanför kärnan.

<!-- S78 -->
Hösten 2026
finns det fortfarande bara i testversioner av Windows.
Och kärnan har inte stängts
för säkerhetsföretagen.

<!-- S79 -->
Dina spel står inför samma dilemma.

<!-- S80 -->
Fusk som körs i kärnan
är osynligt för ett anti-cheat
som körs i ring 3.

<!-- S81 -->
Så anti-cheatet flyttade in också.
Riots Vanguard, som Valorant använder,
lägger en drivrutin i ring 0.
På de flesta datorer laddas den när Windows startar...
även om du aldrig öppnar spelet.

<!-- S82 -->
Det betyder inte att den är felaktig.
Men den sitter på samma plats
som CrowdStrikes drivrutin gjorde,
där ett enda misstag stoppar hela maskinen.

<!-- S83 -->
Så varför kan inte ett program
ta över din dator?

<!-- S84 -->
För att processorn håller
nästan alla program borta från mitten
och kontrollerar dem varje gång de knackar på.

<!-- S85 -->
Men processorn kan inte bestämma
vem som släpps in.
Det bestämmer människor...
varje gång de installerar en drivrutin.

<!-- S86 -->
Så här är en fråga till kommentarerna.
Vem ska bestämma vilka program
som får komma in i ring 0:
du, Microsoft,
eller företagen som gör dem?
