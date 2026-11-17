<!-- S01 -->
Det här är en ZX Spectrum som laddar ett program.

<!-- S02 -->
Och det här är samma program,
på samma dator,
från samma sorts kassett.

<!-- S03 -->
Det är klart på halva tiden.
Ingenting i hårdvaran ändrades.
Inget snabbare band, ingen snabbare bandspelare.

<!-- S04 -->
Det enda som ändrades
var sättet som datorn lyssnade på.

<!-- S05 -->
Så hur lärde sig 8-bitarsdatorerna
att ladda spel snabbare?
Och om det var så enkelt,
varför gjorde de inte så från början?

<!-- S06 -->
I en tidigare video
såg vi hur Spectrum lagrar bitar
som pulser på bandet.

<!-- S07 -->
Ett kort pulspar betyder noll.
Ett dubbelt så långt par betyder ett.

<!-- S08 -->
Det blir ungefär fjortonhundra bitar
varje sekund.
Ett spel som fyller 48K-minnet
tar runt fem minuter.

<!-- S09 -->
Gör nu varje puls hälften så lång.

<!-- S10 -->
Datorn skiljer fortfarande kort från långt.
Men dubbelt så många bitar
passerar tonhuvudet varje sekund.

<!-- S11 -->
Det är hela tricket bakom en turboladdare.
Och det är inte bara ett tankeexperiment.

<!-- S12 -->
1984 laddade spelet Skool Daze
sina data dubbelt så snabbt
som Spectrum normalt gjorde.

<!-- S13 -->
Så varför laddade inte Spectrum
så snabbt av sig självt?

<!-- S14 -->
Den inbyggda laddaren ligger i ROM-minnet,
minneskretsen som datorn startar från.
Den mäter inte en puls i sekunder.

<!-- S15 -->
Den räknar.
Efter varje flank i signalen
väntar den en stund
och räknar sedan hur länge det dröjer till nästa.

<!-- S16 -->
Ett enda tal i ROM-minnet
avgör var nollan slutar
och ettan börjar.

<!-- S17 -->
Och det talet lämnar gott om utrymme.
En nolla kan töjas ut
med mer än fyrtio procent
och ändå läsas som en nolla.

<!-- S18 -->
Den marginalen gör att ett slitet band
på en billig bandspelare
ändå går att ladda.

<!-- S19 -->
Och det var inte datorn som satte gränsen.
Spectrum kollar bandsignalen
ungefär sextiotusen gånger i sekunden.

<!-- S20 -->
Det var kassetten som satte gränsen.
Kortare pulser betyder högre toner.
Vid dubbel hastighet flyttar sig en nolla
från två kilohertz till fyra.

<!-- S21 -->
Och höga toner är precis vad
en billig bandspelare
eller ett lite feljusterat tonhuvud
tappar först.

<!-- S22 -->
En Spectrumtidning bedömde 1986
att de flesta kunde klara
minst dubbla normala hastigheten.
Hur mycket längre man kom
berodde på bandspelaren.

<!-- S23 -->
Men turbo hade ett märkligare problem.

<!-- S24 -->
Om datorn bara kan
det långsamma formatet,
hur laddar den då programmet
som lär den det snabba?

<!-- S25 -->
Svaret finns i början av bandet.
Den första delen är inspelad
i det vanliga, långsamma formatet.

<!-- S26 -->
Den är kort,
och ROM-minnet laddar den som vilket program som helst.

<!-- S27 -->
Sedan tar det lilla programmet över.
I det enklaste fallet
är det en kopia av ROM-minnets egen laddningsrutin,
med några tal ändrade.

<!-- S28 -->
I Skool Daze
sitter ändringarna på tre ställen.
En kortare väntan, ett nytt startvärde för räkningen,
en ny skiljelinje.

<!-- S29 -->
Så ROM-minnet laddar programmet
som gör ROM-minnets jobb, fast snabbare.

<!-- S30 -->
Det är lite som att ladda ner
en snabbare nedladdare.
Det långsamma steget ger dig verktyget.
Verktyget gör resten.

<!-- S31 -->
Kommersiella spel använde samma idé.
Ett välkänt exempel var Speedlock,
som Ocean använde första gången 1984.

<!-- S32 -->
En av upphovsmännen sa att han skrev den
för att han var trött på
hur lång tid standardladdaren tog.

<!-- S33 -->
Men här kommer överraskningen.
Speedlock var bara ungefär en och en halv
gång så snabb.

<!-- S34 -->
Första dagen
i Daley Thompson's Decathlon
tog tre minuter och tjugo sekunder,
medan samma data i normal hastighet
skulle ta fyra minuter och fyrtiosju.

<!-- S35 -->
Senare versioner var bara ungefär
en femtedel snabbare än ROM-minnet.
För det handlade inte bara om hastighet.

<!-- S36 -->
Från 1983 kunde kopieringsprogram
läsa spelets filhuvud
och kopiera hela spelet till ett annat band.

<!-- S37 -->
Ett eget format
gav de programmen ingenting att läsa.

<!-- S38 -->
Tidiga Speedlock hackade till och med upp sin inledningston
i korta stötar,
så att ROM-minnets egen laddare
inte kände igen den alls.

<!-- S39 -->
Och det hördes.
Ett Speedlockband laddade med klickljud
och ryckiga ränder runt skärmen.

<!-- S40 -->
Det hindrade ingen från att kopiera
ett band från ett kassettdäck till ett annat.
Men det gav förlagen
ett skäl att skriva egna laddare.

<!-- S41 -->
På Commodore 64
var skälet att byta mycket större.

<!-- S42 -->
Dess inbyggda rutin
spelade in allt två gånger,
som en säkerhetskopia.
Ett spel på fyrtio kilobyte tog
ungefär tolv och en halv minut.

<!-- S43 -->
Och här gjorde bandspelaren
nästan inget smart.
Den gjorde bara om ljudet
till rena av- och på-pulser.

<!-- S44 -->
Datorn tog tid på varje puls själv,
i mjukvaran.

<!-- S45 -->
Så en snabbare laddare
var bara ett annat program.

<!-- S46 -->
1985 testade tidningen Compute!
en som hette TurboTape.

<!-- S47 -->
När den väl hade hittat programmet på bandet
laddade den tolv kilobyte
på tjugoåtta sekunder.

<!-- S48 -->
Commodores egen diskettstation
behövde trettiofyra sekunder.

<!-- S49 -->
En kassett
som slår en diskett.

<!-- S50 -->
Och eftersom datorn skötte
allt lyssnande själv,
kunde den göra annat emellanåt.

<!-- S51 -->
Laddare som Freeload
gav bandläsningen förtur.
Den processortid som blev över
gick till musik, mjuk scrollning,
till och med små spel.

<!-- S52 -->
Med Mastertronics Invade-a-Load
spelade du en Space Invaders-klon
medan det riktiga spelet laddade.

<!-- S53 -->
Ataris 8-bitarsdatorer
var en annan historia.

<!-- S54 -->
Här var det bandspelaren som lyssnade.
Inuti satt två filter,
ett för varje ton,
och en krets som gav datorn
färdiga ettor och nollor.

<!-- S55 -->
Standarden var sexhundra bitar i sekunden,
och filtren begränsade
hur mycket snabbare det kunde gå.

<!-- S56 -->
Smart mjukvara kunde trycka upp det
lite, i bästa fall till ungefär tolvhundra.
Men för att komma upp i mycket högre fart
fick man öppna bandspelaren.

<!-- S57 -->
Och i Tjeckoslovakien gjorde folk det.

<!-- S58 -->
En diskettstation kostade där
två till tre gånger
så mycket som själva datorn.
Så de flesta Atariägare där höll sig till kassetter.

<!-- S59 -->
1987 konstruerade en student i Prag
från den lokala Atariklubben
Turbo 2000.

<!-- S60 -->
Den gav signalen en ny väg.
En sladd inne i bandspelaren tog ljudet
direkt från förstärkaren,
före filtren,
genom ett litet chip
och vidare ut på ledningen till datorn.

<!-- S61 -->
En omkopplare, som datorn styrde,
valde mellan den gamla vägen och den nya.

<!-- S62 -->
Nu tog datorn tid på pulserna själv.
Runt tvåtusentrehundra bitar
i sekunden.
Nästan fyra gånger så snabbt.

<!-- S63 -->
Turbo var inte ett enda universellt format.

<!-- S64 -->
Ibland bytte man program.
Ibland fick man bygga om själva maskinen.

<!-- S65 -->
Och snabbare var inte gratis.

<!-- S66 -->
Compute! varnade för att en TurboTape-inspelning
ibland vägrade ladda
på en annan bandspelare,
med tonhuvudet lite annorlunda justerat.

<!-- S67 -->
Standardsparningen, skrev tidningen,
var mycket långsammare,
men extremt pålitlig.

<!-- S68 -->
Att spela in allt två gånger
var inte lathet från Commodores sida.
Det var priset för pålitlig laddning.

<!-- S69 -->
Men en annan laddare
kunde också göra något oväntat.
Den kunde läsa ett band
som den inbyggda vägrade.

<!-- S70 -->
På Sharp MZ-800,
en dator som hittade fram
till Tjeckoslovakien i slutet av 1980-talet,
kände ägarna till ett program som hette Turbo Copy.

<!-- S71 -->
Ett spel vägrade ladda,
med ett kontrollsummefel.
Ägarna upptäckte att Turbo Copy
ofta kunde ladda det ändå.

<!-- S72 -->
Sedan sparade man det i normal hastighet
på en ny kassett,
och datorn
laddade det normalt igen.
Det kändes som att laga ett trasigt spel.

<!-- S73 -->
Så hur kunde en laddare läsa
det som den andra inte klarade?

<!-- S74 -->
Sharps ROM spelade in varje block två gånger,
med ungefär tolvhundra bitar i sekunden.

<!-- S75 -->
Och den mätte aldrig en puls.
När en puls hade börjat
väntade den en bestämd tid
och tittade en enda gång.

<!-- S76 -->
Fortfarande hög?

<!-- S76b -->
Då är det en etta.

<!-- S76c -->
Redan låg?

<!-- S76d -->
Då är det en nolla.

<!-- S77 -->
Ett stoppur, inställt i förväg.

<!-- S78 -->
På ett gammalt band eller en annan bandspelare
kom pulserna tillbaka lite rundare.
Då kunde den enda avläsningen
visa fel nivå.

<!-- S79 -->
En enda fel bit förstör kontrollsumman.
Om båda kopiorna misslyckas,
misslyckas laddningen.

<!-- S80 -->
Turbo Copy lyssnade annorlunda.
Den tog tid på varje puls
med datorns timerkrets.

<!-- S81 -->
Och före varje block
lyssnade den på inledningstonen
och satte sin skiljelinje
efter pulserna den faktiskt hörde.

<!-- S82 -->
Dess stoppur var inställt
på just det band som spelades.

<!-- S83 -->
Och lagningen var ingen kopia av ljudet.
Turbo Copy behöll bytena
och skrev en helt ny,
ren signal med exakt timing.

<!-- S84 -->
Datan hade inte gått förlorad.
Det vanliga sättet att läsa den
var helt enkelt inte tillräckligt bra.

<!-- S84b -->
Turbo Copy kunde också spara spelet med turbo,
i två eller tre gånger normal hastighet,
med en egen liten laddare först.

<!-- S85 -->
Och det är vad alla de här knepen
har gemensamt.

<!-- S86 -->
Kassetten förblev densamma.
Det som ändrades var hur den lästes.

<!-- S87 -->
I dag förväntar vi oss att spel laddar direkt.
På 1980-talet var laddningen en del av spelet.
Du lyssnade på bandet.
Du tittade på ränderna.
Du väntade.

<!-- S88 -->
Och ibland fick en annan laddare
samma kassett att bete sig
som om den satt i en helt annan maskin.

<!-- S89 -->
Datorn behövde inget snabbare band.
Den behövde ett bättre sätt att lyssna.

<!-- S90 -->
Så här kommer en fråga till dig.
Använde du turboladdare på den tiden?
Hur minns du dem?
Strulade de oftare?
Berätta i kommentarerna.

<!-- S91 -->
Och till sist hela turbobandet,
från början till slut.
Först delen i normal hastighet,
sedan turbon.
För ett så litet program
lönar sig inte turbo.
Laddaren tar längre tid
än den tid den sparar.
För ett helt spel kunde det spara minuter.
