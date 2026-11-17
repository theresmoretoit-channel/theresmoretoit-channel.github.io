<!-- S01 -->
Det här är en QR-kod.
Den innehåller en kort rad text.

<!-- S02 -->
Mobilen läser den direkt.

<!-- S03 -->
Nu river vi bort en bit av den.

<!-- S04 -->
Och skannar den igen.
Samma text.
Varenda bokstav.

<!-- S05 -->
En del av koden är borta.
Inte svår att läsa.
Borta.

<!-- S06 -->
Så hur kan en mobil läsa något
som inte längre finns där?

<!-- S07 -->
Här är samma problem, fast mindre.
Någon skickar åtta bitar till dig.
På vägen försvinner tre av dem.

<!-- S08 -->
Varje saknad bit är en nolla eller en etta,
så det finns åtta sätt att fylla luckorna.
Och ingenting i det som kom fram
säger dig vilket som är rätt.

<!-- S09 -->
Och ändå gjorde mobilen precis det.
Den gissade inte.
Svaret skickades
innan något gick förlorat.

<!-- S10 -->
Tricket är att skicka mer
än bara själva meddelandet.

<!-- S11 -->
Det enklaste sättet
är att säga allt tre gånger.
En nolla skickas som tre nollor,
en etta som tre ettor.

<!-- S12 -->
Brus vänder på en av dem,
och du tar emot ett, noll, ett.
Två röster mot en.
Det var nästan säkert en etta.

<!-- S13 -->
Om bruset vänder på var tionde bit,
slumpmässigt och oberoende,
slår en omröstning bland tre fel
i färre än tre fall av hundra.

<!-- S14 -->
Men du har tredubblat
allt du skickar.
För att komma närmare perfektion
skulle du upprepa fem gånger, sedan nio,
sedan hundra...
och meddelandet kryper fram i snigelfart.

<!-- S15 -->
Länge
såg det ut att vara priset.
Färre fel, långsammare meddelanden.
Kom ihåg det.

<!-- S16 -->
I slutet av 1940-talet
hade Richard Hamming på Bell Labs
ett eget problem.

<!-- S17 -->
Han fick oftast tid på en relädator
på helgerna,
när ingen var där och övervakade den.

<!-- S18 -->
Maskinen kunde märka
när den hade gjort ett fel.
Då försökte den med steget igen,
tre gånger...
och avbröt sedan hans körning.
Två helger i rad
förlorade han sitt arbete.

<!-- S20 -->
Hans fråga, med hans egna ord:
”Om maskinen kan avgöra
att det finns ett fel,
varför kan den inte avgöra var det sitter?”
Ordvalet, medgav han,
var nog något kraftigare.

<!-- S22 -->
Hans lösning tar fyra meddelandebitar
och lägger till tre kontrollbitar.
Sju bitar totalt.

<!-- S23 -->
Varje kontrollbit vakar över
en egen grupp av positioner
och ser till att den gruppen
innehåller ett jämnt antal ettor.

<!-- S24 -->
Grupperna överlappar varandra i ett noga uttänkt mönster.
Varje position hör till
sin egen kombination av grupper.

<!-- S25 -->
Vänd nu på en bit.
Säg den på position sex.

<!-- S26 -->
Mottagaren gör om de tre kontrollerna.
Den första går igenom.
Den andra misslyckas.
Den tredje misslyckas.

<!-- S27 -->
Skriv en misslyckad kontroll som ett,
en godkänd kontroll som noll,
och läs dem från den sista till den första.
Ett, ett, noll.
Binärt är det sex.

<!-- S28 -->
Kontrollerna säger inte bara
att något gick fel.
De pekar ut exakt vilken bit.

<!-- S29 -->
Vänd tillbaka den,
och meddelandet är helt igen.
Ingen behövde skicka något två gånger.

<!-- S30 -->
Så det är svaret.
Mottagaren bygger inte upp
förlorad information ur ingenting.
Avsändaren packade in den,
i förväg.

<!-- S32 -->
Alla kontroller klarar inte det.
En kontrollsumma, som den i vår video
om Btrfs,
kan säga att ett block är skadat,
men inte hur originaldatan såg ut.

<!-- S33 -->
Och det finns en andra sorts skada.
Ibland är en bit inte fel.
Den saknas bara,
och du vet exakt var luckan är.

<!-- S34 -->
Det kallas en radering,
och raderingar är lättare.

<!-- S35 -->
Skicka fyra tal,
4, 7, 2 och 9,
och ett femte:
deras summa, 22.

<!-- S36 -->
Om något av dem försvinner,
säger de andra vad det var.
4, 7, något, 9,
22.
Det måste vara en tvåa.

<!-- S37 -->
Servrar skyddar sina diskar
med en liknande sorts kontroll,
utspridd över enheterna.
När en enhet dör,
räknas dess innehåll fram ur resten.

<!-- S38 -->
Så hur mycket extra behöver man?
Upprepning säger:
för att få ner felen till noll
måste man sakta ner till noll.

<!-- S39 -->
Två år innan Hammings artikel
kom ut
hade hans kollega Claude Shannon
publicerat ett märkligare svar.

<!-- S40 -->
Varje kanal,
en radiolänk, en kabel, en skiva,
har en gräns.
En högsta hastighet för information.

<!-- S41 -->
Under den gränsen
kan fel bli hur sällsynta som helst,
utan att det går långsammare.
Inte genom att upprepa mer.
Genom smartare kodning.

<!-- S42 -->
Över den
hjälper ingen kod i världen.

<!-- S43 -->
Men det fanns en hake.
Shannon bevisade att sådana koder finns.
Han visade inte hur man bygger en
som någon faktiskt kan använda.

<!-- S44 -->
Enligt hans bevis skulle en slumpvis vald kod
nästan säkert vara bra.
Men det självklara sättet att avkoda den
innebär att jämföra det som kom fram
med varje möjligt meddelande...
och för ett block på 1 000 bitar
finns det fler sådana
än atomer i universum.

<!-- S46 -->
Shannons artikel var alltså ingen lösning.
Det var ett löfte.
Och ingenjörer ägnade de följande
45 åren åt att försöka hålla det.

<!-- S47 -->
Hammings kod var ett första steg.
Den rättar en felaktig bit av sju.

<!-- S48 -->
Men verkliga skador kommer i felskurar.
En repa eller ett brusknaster
slår ut hundratals bitar i rad.

<!-- S49 -->
1960 gav Irving Reed och Gustave Solomon,
vid MIT:s Lincoln Laboratory,
ut en artikel på fem sidor.

<!-- S50 -->
Deras koder arbetar med hela byte,
inte med enskilda bitar.
Om en felskur förstör alla åtta bitar
i en byte,
är det ändå bara en felaktig byte.

<!-- S51 -->
En vanlig variant fogar
32 kontrollbyte
till 223
databyte.

<!-- S52 -->
Den kan rätta vilka 16 byte som helst
som kommer fram fel...
eller återskapa 32
som aldrig kommer fram alls.

<!-- S53 -->
Det är därför en cd kan spelas trots en repa.
Dess två Reed-Solomon-koder
kan helt laga en lucka
på ungefär 4 000 bitar,
alltså 2,5 millimeter spår.

<!-- S54 -->
Och det är därför den sönderrivna QR-koden
ändå fungerade.
På den högsta felkorrigeringsnivån
kan en QR-kod återskapa
upp till ungefär 30 % av sina byte
och ändå ge tillbaka varenda bokstav.

<!-- S56 -->
Voyager 2 lämnade jorden 1977
med en Reed-Solomon-kodare redan ombord.

<!-- S57 -->
Men vid Jupiter och Saturnus
skyddade den allt utom bilderna
med en äldre kod av Marcel Golay,
som skickade en extra bit
för varje databit.

<!-- S58 -->
För Uranus och Neptunus,
när signalen blev allt svagare,
slog ingenjörerna på Reed-Solomon,
ovanpå en andra kod
som varje bit redan gick igenom.

<!-- S59 -->
Med bara den andra koden
var ungefär fem bitar av tusen
fortfarande fel.
Med Reed-Solomon ovanpå
ungefär en på miljonen.

<!-- S60 -->
Även brus kommer i korta skurar,
så Voyager blandade ihop
bytena från fyra block
innan de skickades.

<!-- S61 -->
En felskur som skulle ha förstört ett block
tar nu några byte från vart och ett...
så få att varje block
kan laga sig självt.

<!-- S62 -->
Resten av historien om hur Neptunus bilder
kom hem
finns i vår video om Voyager.

<!-- S63 -->
Men inte ens det här
räckte ända fram till Shannons gräns...
och en kod som kunde komma mycket närmare
fanns redan.

<!-- S65 -->
1960, i sin doktorsavhandling vid MIT,
beskrev Robert Gallager koder
uppbyggda av många enkla kontroller,
där var och en bara tittar på några få bitar.

<!-- S66 -->
Att avkoda dem innebar att kontrollerna
skickade gissningar fram och tillbaka,
varv efter varv...
alldeles för mycket
för 1960-talets datorer.
Så idén lades undan
och glömdes i stort sett bort i 30 år.

<!-- S68 -->
1993
presenterade ett team lett av två franska ingenjörer,
Claude Berrou och Alain Glavieux,
turbokoder
vid en konferens i Genève.

<!-- S69 -->
Deras resultat låg så nära
Shannons gräns
att många experter trodde
att de hade gjort ett misstag.
Förmodligen en faktor två,
någonstans i deras beräkningar.

<!-- S70 -->
Inom ett år
hade andra labb bekräftat det.

<!-- S71 -->
Turbokoder fungerade också
genom att skicka gissningar fram och tillbaka,
och det fick folk att gå tillbaka till Gallager.

<!-- S72 -->
1995 och 1996
återupptäckte David MacKay och Radford Neal
hans koder
och visade att de kunde komma
lika nära.

<!-- S73 -->
År 2001
kom en förfinad version av Gallagers koder
inom 0,04 decibel
från Shannons gräns.

<!-- S74 -->
Det är mindre än en procent
mer signaleffekt
än det teoretiska minimet.
Löftet från 1948 hade infriats.

<!-- S75 -->
I dag bär Gallagers koder
mycket av datan i 5G-telefoner,
i modernt wifi
och i satellit-tv.

<!-- S77 -->
Nu tillbaka till våra åtta bitar.
Tre gick förlorade,
och det finns åtta sätt
att fylla luckorna.

<!-- S78 -->
Men de här åtta bitarna
var aldrig bara ett meddelande.
De bar fyra databitar,
Hammings tre kontroller
och ytterligare en kontroll över alla åtta.

<!-- S79 -->
Av alla 256
möjliga mönster med åtta bitar
följer bara 16 de reglerna.

<!-- S80 -->
Testa de åtta kandidaterna.
En efter en faller de bort.
Bara en blir kvar.

<!-- S81 -->
De saknade bitarna var aldrig riktigt borta.
Deras information fanns kvar,
i bitarna som överlevde.

<!-- S82 -->
Så här kommer en fråga till dig.
Har du någon gång märkt hur felkorrigering
fungerar i något du använder varje dag?
Berätta i kommentarerna.
