# Hur tog ARM över datorvärlden?

<!-- S01 -->
År 1985 slog ingenjörer i Storbritannien
på en helt ny processor
för allra första gången.

<!-- S02 -->
Den fungerade.
Vilket redan det var ett litet mirakel.

<!-- S03 -->
Men sedan märkte de något konstigt.
Chippets strömförsörjning
var inte ansluten.

<!-- S04 -->
Och ändå gick den.

<!-- S05 -->
Den klarade sig på små strömmar
som läckte in genom ingångsstiften,
från signalerna i chippen runt omkring.

<!-- S06 -->
När de mätte ordentligt
behövde processorn
ungefär en tiondels watt.

<!-- S07 -->
Det var ingen som hade siktat på det.
Ingenjörerna ville bara ha ett chip
som var billigt att tillverka.

<!-- S08 -->
Det chippet var den första ARM-processorn.

<!-- S09 -->
Fyrtio år senare finns dess ättlingar
i nästan varenda smartphone.
I Apples datorer.
I några av de största datacentren
i världen.

<!-- S10 -->
Hundratals miljarder chip.

<!-- S11 -->
Så hur kunde en processor
från ett brittiskt hemdatorföretag
ta över datorvärlden?

<!-- S12 -->
Svaret är inte bara
att den drog väldigt lite ström.
Den delen var nästan en slump.

<!-- S12b -->
Förresten, om du gillar sådana här
videor, prenumerera gärna.

Det hjälper kanalen på riktigt.

<!-- S13 -->
För att förstå vad som egentligen hände
måste vi gå tillbaka till 1983.

<!-- S14 -->
Företaget hette Acorn Computers.
Deras BBC Micro stod i klassrum
över hela Storbritannien.

<!-- S15 -->
BBC Micro gick på ett äldre
åttabitarschip, 6502.
Till sin nästa maskin
behövde Acorn något mycket snabbare.

<!-- S16 -->
Så teamet testade
de nya processorerna på marknaden.
Ingen av dem gjorde det Acorn ville.

<!-- S17 -->
De var komplicerade,
och ingen av dem passade riktigt
för det Acorn ville bygga.

<!-- S18 -->
Sedan åkte två av Acorns ingenjörer,
Sophie Wilson och Steve Furber,
till Arizona,
till ett företag som grundats av en av
6502:ans ursprungliga konstruktörer.

<!-- S19 -->
De väntade sig ett stort chipföretag.
I stället hittade de en handfull personer
som jobbade i ett hus i en förort.

<!-- S20 -->
Och de kom hem
med en enkel slutsats.
Om de kan konstruera en processor...
så kan vi.

<!-- S22 -->
På den tiden fick processorerna
allt mer avancerade instruktioner.

<!-- S23 -->
En enda instruktion kunde hämta
ett tal från minnet,
räkna med det
och skriva tillbaka resultatet.

<!-- S24 -->
Bekvämt för programmeraren.
Men varje sådan instruktion
gör chippet svårare att bygga.

<!-- S25 -->
Det behövs mer logik
bara för att reda ut vad var och en betyder.
Fler transistorer.
Mer konstruktionstid.

<!-- S26 -->
Forskare vid Berkeley och Stanford
hade ställt en radikal fråga.

<!-- S27 -->
Tänk om en processor
bara hade enkla instruktioner,
och kompilatorn skötte resten?

<!-- S28 -->
De kallade det RISC.
Reduced Instruction Set Computer.

<!-- S29 -->
Sophie Wilson utformade
ARM:s instruktioner enligt samma idé.

<!-- S30 -->
Räkneoperationer görs bara
på chippets egna register,
små, snabba fack inne i processorn.
För minnet finns det egna instruktioner.

<!-- S31 -->
Att addera ett tal från minnet
blir alltså tre steg.
Läs in det.
Addera det.
Spara det.

<!-- S32 -->
Det kallas load-store-arkitektur.

<!-- S33 -->
Fler steg för programmet.
Men varje steg är regelbundet,
förutsägbart
och lätt att avkoda.

<!-- S34 -->
Och ARM hade gott om register
att arbeta med.
Sexton stycken, vart och ett 32 bitar brett.
6502 hade tre små.

<!-- S35 -->
Resultatet blev ARM1.

<!-- S36 -->
Den hade ungefär
25 000 transistorer.

<!-- S37 -->
Intels 286, som kom några år tidigare,
hade ungefär 134 000.

<!-- S38 -->
Färre transistorer betydde ett mindre chip.
Ett billigare chip.

<!-- S39 -->
Och, nästan som en bieffekt,
ett chip som knappt drog någon ström.

<!-- S40 -->
Det var därifrån
tiondelen av en watt kom.
Acorn ville ha en billig plastkapsel,
och då måste de hålla sig under en watt.
Så de konstruerade försiktigt...
och hamnade tio gånger lägre.

<!-- S41 -->
År 1987 hamnade en snabbare version av ARM
i Acorns nya dator,
Archimedes.

<!-- S42 -->
Den var en av sin tids
snabbaste persondatorer.

<!-- S43 -->
Och det spelade knappt någon roll.

<!-- S44 -->
Världen köpte IBM-kompatibla pc
med Intelprocessorer.
Det var där programvaran fanns.
Det var det företagen köpte.

<!-- S45 -->
Archimedes blev kvar
mest i brittiska skolor.

<!-- S46 -->
Och Acorn självt hade det kämpigt.
Företaget hade redan behövt räddas
av Olivetti, så tidigt som 1985.

<!-- S48 -->
Sedan kom hjälp från Apple.
De byggde en handdator
som hette Newton.

<!-- S49 -->
Den behövde en processor
som var snabb, billig
och kunde gå på batterier.

<!-- S50 -->
ARM passade perfekt.
Men Apple ville inte vara beroende
av ett chip som ägdes av
en konkurrerande datortillverkare.

<!-- S51 -->
Så 1990 knoppades ARM-teamet
av från Acorn
till ett eget företag.

<!-- S52 -->
Acorn, Apple
och chiptillverkaren VLSI
ägde det tillsammans.

<!-- S53 -->
Tolv ingenjörer.
En gammal lada utanför Cambridge.

<!-- S54 -->
Och en affärsmodell
som visade sig vara den verkliga hemligheten.

<!-- S55 -->
Intel konstruerade sina processorer,
tillverkade dem i egna fabriker
och sålde dem.

<!-- S56 -->
ARM skulle inte tillverka något alls.
Det skulle sälja konstruktionen.

<!-- S57 -->
Vilket företag som helst kunde licensiera den,
bygga in ARM-kärnan i sitt eget chip
och betala en liten avgift
för varje chip det sålde.

<!-- S58 -->
Det spelade roll,
eftersom ett chip inte behöver vara
bara en processor.
Runt ARM-kärnan
kan man lägga en radio,
en grafikenhet,
en kameraprocessor.

<!-- S59 -->
Ett chip,
konstruerat av den som behöver det,
med ARM i mitten.

<!-- S60 -->
ARM behövde inte slå Intel
på persondatorer.
Det kunde hamna i vad som helst.

<!-- S61 -->
Och på 1990-talet
betydde vad som helst allt oftare
mobiltelefoner.

<!-- S62 -->
En stationär dator kan dra
hundra watt och ha en stor fläkt.
En telefon går på ett batteri
i fickan.

<!-- S63 -->
I slutet av decenniet
satt ARM-kärnor i
några av de mest sålda telefonerna,
från Nokia och andra.

<!-- S64 -->
Sedan kom iPoden.
Sedan smartphonen.

<!-- S65 -->
Miljarder människor bar plötsligt på
en dator som måste klara sig
en hel dag på ett batteri.

<!-- S66 -->
Och processorn som byggdes
för att den var billig
visade sig vara precis
vad den världen behövde.

<!-- S67 -->
Så det är vårt svar, eller hur?
ARM är enkelt,
enkelt betyder effektivt,
och effektivt vinner.

<!-- S68 -->
Inte riktigt.

<!-- S69 -->
Titta in i en modern ARM-kärna i toppklass.

<!-- S70 -->
Enorma cacheminnen.
Flera instruktioner som körs samtidigt.
Hoppförutsägelse,
som gissar åt vilket håll programmet går
innan det kommer dit.

<!-- S71 -->
Out-of-order-exekvering,
där instruktioner körs
i den ordning som går snabbast.

<!-- S72 -->
Miljarder transistorer på chippet.
Inget av det är enkelt.

<!-- S73 -->
Så vart tog enkelheten vägen?

<!-- S74 -->
Tricket är att en processor
egentligen är två olika saker.

<!-- S75 -->
Instruktionsuppsättningen är språket
som programvaran talar.
Vilka instruktioner som finns,
och vad de betyder.

<!-- S76 -->
Mikroarkitekturen är maskinen
som faktiskt utför dem.

<!-- S77 -->
Språket kan förbli enkelt,
medan maskinen därunder
blir enormt komplicerad.

<!-- S78 -->
Och samma sak hände
på andra sidan.

<!-- S79 -->
Intels x86-instruktioner
är ökänt komplicerade.

<!-- S80 -->
Men sedan mitten av 1990-talet
delar processorer från Intel och AMD
internt upp dem
i små, enkla operationer.

<!-- S81 -->
Sedan kör de dem på en motor
som liknar den
i en modern ARM-kärna.

<!-- S82 -->
Bakom de olika namnen
har de två blivit förvånansvärt lika.

<!-- S83 -->
ARM:s renare instruktioner hjälper fortfarande.
De är lättare att avkoda,
vilket kan spara lite ström.

<!-- S84 -->
Men de är ingen magisk fördel
som x86 aldrig skulle kunna matcha.

<!-- S85 -->
Så ARM tog inte över
för att det var enkelt.
Och det konstruerades inte för låg strömförbrukning.

<!-- S86 -->
Det vann för att tre saker föll på plats.
En effektiv konstruktion.
En affärsmodell
som lät vem som helst bygga på ARM.
Och en värld som plötsligt behövde
miljarder batteridrivna datorer.

<!-- S87 -->
Och sedan, år 2020,
återvände historien till Apple.

<!-- S88 -->
Apple hade sålt sin andel i ARM
många år tidigare,
när de desperat behövde pengarna.

<!-- S89 -->
Nu satte de sina egna ARM-baserade chip
i Macen.

<!-- S90 -->
Samma slags kärnor som i iPhonen,
uppskalade för en dator.
Snabba kärnor, effektiva kärnor,
grafik och mycket mer,
i ett enda chip.

<!-- S91 -->
De var snabbare
än Intelchippen de ersatte,
och de bärbara datorerna höll mycket längre
på en laddning.

<!-- S92 -->
ARM var inte längre
bara telefonprocessorn.

<!-- S93 -->
Och ARM stannade inte där.
Det tog sig in i datacenter också,
där varje watt kostar pengar.
Amazon konstruerar nu
sina egna ARM-serverchip.

<!-- S95 -->
Det första ARM-chippet hade ungefär
25 000 transistorer.
Dagens har miljarder.

<!-- S96 -->
Nästan allt i hur de
fungerar inuti har förändrats.

<!-- S98 -->
Ett litet team ville ha
en processor de faktiskt kunde bygga.

<!-- S99 -->
De byggde den inte för telefoner,
för Apple,
eller för att slå Intel.

<!-- S100 -->
Och till slut
var det viktigaste de skapade
inte chippet.

<!-- S101 -->
Det var en enkel grund
som alla andra kunde bygga vidare på.
