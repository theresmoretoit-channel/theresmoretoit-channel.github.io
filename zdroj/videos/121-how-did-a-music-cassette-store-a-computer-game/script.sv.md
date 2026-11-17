<!-- S01 -->
Du trycker på play på en kassettbandspelare.
Och det här kommer ut ur högtalaren.

<!-- S02 -->
Det är inte musik.
Och det är inte heller spelets soundtrack.

<!-- S03 -->
Det är själva spelet.
Varje tjut är en del av ett program,
och datorn lyssnar på det.

<!-- S04 -->
Kassettspelaren har ingen aning.
Så vitt den vet spelar den en låt.

<!-- S05 -->
Så hur blir en låt ett spel?
Och varför kunde en enda fel ton
göra fem minuters väntan förgäves?

<!-- S06 -->
Så här går tricket till,
på en bestämd maskin:
ZX Spectrum,
en brittisk hemdator från 1982.

<!-- S07 -->
Den använder två sorters pulser.
Ett kort pulspar betyder noll.

<!-- S08 -->
En etta är samma par,
men varje puls är dubbelt så lång,
så tonen ligger en oktav lägre.

<!-- S09 -->
Skicka ungefär fjortonhundra bitar
i sekunden,
så får du ljudet du just hörde.

<!-- S09b -->
Det betyder också att ett program fullt av nollor
laddas snabbare än ett fullt av ettor.
Varje etta tar dubbelt så lång tid att skicka.

<!-- S10 -->
Om du växte upp i USA
har du kanske aldrig hört det alls.

<!-- S11 -->
Vilket är märkligt,
för själva idén var amerikansk.

<!-- S12 -->
1975, på ett möte i Kansas City,
kom datorentusiaster överens om ett sätt
att lagra data som ljud
på vanliga ljudkassetter.

<!-- S12b -->
En etta var åtta snabba svängningar
i en hög ton,
en nolla fyra långsammare i en låg.
Trehundra bitar i sekunden.

<!-- S13 -->
Tidiga maskiner som Apple II
och TRS-80
sparade sina program
på helt vanliga bandspelare.

<!-- S14 -->
Men i USA gick man snart över
till andra lagringsmedier.

<!-- S15 -->
1983 rapporterade en tidning om en enkät:
nio av tio nya ägare av Commodore 64
köpte en diskettstation
samtidigt med datorn.

<!-- S16 -->
I Storbritannien gick historien åt andra hållet.

<!-- S17 -->
Spectrum kostade
hundratjugofem pund,
och den kom helt utan lagringsenhet.
Du använde den kassettspelare
du redan hade.

<!-- S18 -->
Så för miljontals barn runt om i Europa
betydde det här ljudet
att ett spel snart skulle börja.

<!-- S18b -->
Efter tillräckligt många laddningar
kunde du till och med höra vilket spel det var
bara på tjutet.

<!-- S19 -->
Så låt oss följa ett spel
från bandet in i datorn.

<!-- S20 -->
Du skriver LOAD, trycker på enter
och trycker på play.

<!-- S21 -->
Först kommer ett jämnt brummande,
åttahundra svängningar i sekunden,
i ungefär fem sekunder.

<!-- S22 -->
Det bär ingen data alls.
Det finns där för att datorn
ska hitta signalen
och låsa sig på dess rytm.

<!-- S23 -->
Sedan två snabba pulser, synken.
De betyder: härifrån är det data.

<!-- S24 -->
Det första som kommer fram
är ett kort huvud.
Nitton byte:
ett namn på upp till tio bokstäver,
vilken sorts fil det är
och hur lång den kommer att bli.

<!-- S25 -->
Sedan ett andra, kortare brummande,
två sekunder den här gången,
och sedan själva spelet.

<!-- S26 -->
Varje byte är åtta sådana toner,
den ena efter den andra,
helt utan mellanrum mellan byten.

<!-- S27 -->
Och datorn hör inga toner.
Den mäter tiden mellan en flank
i signalen och nästa.

<!-- S28 -->
Ett kort par är en nolla.
Ett långt par är en etta.

<!-- S28a -->
Det är hela avkodaren.

<!-- S28b -->
Och ljudet i början av den här videon
är ingen ljudeffekt.
Vi skapade det exakt enligt de här reglerna,
och i det finns ett riktigt Spectrum-program.

<!-- S28c -->
Vi spelar upp det hela alldeles i slutet.
Spela in det, så laddar en Spectrum det.

<!-- S29 -->
De flesta spel visade först en bild,
och den laddades i en märklig ordning.

<!-- S30 -->
Tunna ränder dök upp med åtta raders mellanrum,
och fylldes sedan i, linje för linje,
en tredjedel av skärmen i taget.
Och färgerna kom sist
och svepte nedåt över allt.

<!-- S31 -->
Bara bilden
tog ungefär fyrtio sekunder.
Hela spelet runt fem minuter.

<!-- S32 -->
Och i slutet av varje block
kommer en byte till.

<!-- S33 -->
När Spectrum sparar kör den
varje byte i blocket
genom en enkel regel som heter XOR
och spelar in resultatet som en byte till.

<!-- S34 -->
Vid laddningen gör den om beräkningen.
Om resultaten stämmer
kom blocket fram helt.

<!-- S35 -->
Om de inte stämmer säger Spectrum det här.

<!-- S36 -->
Fem minuters väntan,
och en enda byte avgör
att allt var förgäves.
Spola tillbaka och börja om.

<!-- S37 -->
Märkligt nog ger ett trasigt huvud
inget felmeddelande alls.
Spectrum bara ignorerar det
och fortsätter lyssna efter nästa.

<!-- S38 -->
Andra datorer satsade på annat.

<!-- S39 -->
Commodore 64 spelade in
varje block två gånger,
så att ett skadat ställe i ena kopian
kunde räddas från den andra.

<!-- S40 -->
Säkrare, men långsamt.
Med Commodores inbyggda rutin
tog ett program på fyrtio kilobyte
ungefär tolv och en halv minut.

<!-- S41 -->
Så spelförlagen skrev
egna, snabbare laddare,
en del upp till ungefär tio gånger snabbare.

<!-- S42 -->
Och så var det kassettspelaren.

<!-- S43 -->
För tyst,
och flankerna sjunker ner i bruset.
För högt,
och de smetas ut i varandra.

<!-- S44 -->
Ett band som går lite för fort eller för sakta
töjer ut varje puls,
och datorn mäter ju tid.

<!-- S45 -->
Värst av allt var azimuten,
tonhuvudets vinkel.
Ett band inspelat på en maskin
passade kanske inte en annan.

<!-- S46 -->
Så folk stack in en pytteliten skruvmejsel
i ett hål bredvid tonhuvudet,
vred den en liten bit i taget
och lyssnade.

<!-- S47 -->
Det såg ut som vidskepelse.
Det var signaljustering.

<!-- S48 -->
Men lägg märke till vad kassettspelaren
aldrig behövde göra.

<!-- S49 -->
Den förstod aldrig en enda bit.
Den spelade in ljud
och spelade upp det igen.

<!-- S50 -->
Vilket betyder att ett program
egentligen inte behövde en kassett.
Allt som kunde bära ljud
kunde bära mjukvara.

<!-- S50b -->
Det betydde också att kopiera ett spel
var lika lätt som att kopiera ett album.
Två kassettdäck och en kabel.

<!-- S51 -->
Atari använde båda stereospåren.
Programmet på det ena
och en röst på det andra,
som pratade med dig genom tv:n
medan spelet laddades.

<!-- S52 -->
I Jugoslavien sände ett program på Radio Belgrad
datorprogram i etern.

<!-- S53 -->
Lyssnarna spelade in dem på band,
ungefär hundrafemtio program
mellan 1983 och 1986.

<!-- S54 -->
I Tjeckoslovakien var det tv:n.
Ett program spelades som ljud
under eftertexterna.

<!-- S55 -->
Och 1983 gömde sångaren Pete Shelley
ett Spectrum-program
i slutet av ett vinylalbum.

<!-- S56 -->
Kopiera det till band, ladda det,
så visades sångtexterna på skärmen
i takt med låtarna.

<!-- S57 -->
Men det fanns en hake.

<!-- S58 -->
Radion kunde bära ljudet
till varenda dator i landet.
Bara den rätta kunde förstå det.

<!-- S59 -->
Spela ett Spectrum-spel för en Commodore,
och Commodoren hör brus.
Bitarna betyder bara något
för en maskin som känner till formatet.

<!-- S60 -->
Så nederländsk radio försökte lösa det.
1982 skapade den BASICODE:
ett enda ljudformat,
med ett litet översättningsprogram
för varje sorts dator.

<!-- S61 -->
Och det problemet försvann aldrig.
En fil är bara användbar
om något fortfarande kan läsa den.

<!-- S62 -->
Kassetterna förlorade förstås.
Disketter var snabbare,
sedan hårddiskar, sedan flashminnen.

<!-- S63 -->
Fast bandet försvann faktiskt aldrig.
Datacenter förvarar fortfarande
sina arkiv på magnetband.

<!-- S64 -->
En modern LTO-9-kassett
rymmer arton terabyte.

<!-- S65 -->
Omräknat till Spectrums hastighet
skulle den kapaciteten fylla ungefär
tjugonio miljoner kassetter
och ta mer än tretusen
år att ladda.

<!-- S66 -->
Men det är fortfarande samma idé.
Mönster på en remsa band i rörelse,
som blir till siffror igen
när du behöver dem.

<!-- S67 -->
Så nästa gång du hör det där tjutet,
kom ihåg vad det är.
Inget brus.
Ett program som färdas som ljud.

<!-- S68 -->
Och någonstans år 1985
sitter ett barn framför en tv
och väntar på att det ska sluta.
För när det gör det,
börjar spelet.

<!-- S69 -->
Så här kommer en fråga till dig.
Om du någon gång laddade ett spel från kassett,
vad minns du mest av det?
Skriv det i kommentarerna.

<!-- S70 -->
Och som utlovat, här är programmet.
Precis som tjeckoslovakisk tv
har vi lagt det under eftertexterna.
