<!-- S01 -->
Du köper en helt ny disk.
En terabyte, helt tom.
Innan den kan rymma en enda fil
måste den först formateras.

<!-- S02 -->
Så du formaterar den med ext4,
standardfilsystemet
på många Linuxdatorer.
Med standardinställningarna,
innan du ens har sparat något,
är ungefär sjutton gigabyte borta.

<!-- S03 -->
Ingenting har sparats än.
Inga foton, inga dokument.
Så vad är det som tar upp all den platsen?

<!-- S04 -->
Och varför behöver en disk formateras
över huvud taget?
Den kan ju redan lagra data.
Den kan läsa och skriva biljoner bitar.

<!-- S05 -->
Varför kan datorn inte bara börja skriva
där det finns plats?

<!-- S06 -->
För att lagra data
och att hitta den igen
är två helt olika problem.

<!-- S07 -->
Tänk dig ett kontor som delar ut
tomma papper i stället för blanketter.
Allt skrivs ner någonstans...
och ingen hittar någonting.

<!-- S08 -->
En disk utan filsystem
är den där pappershögen.
En bättre bild
är ändå en anteckningsbok.

<!-- S09 -->
Tänk dig en anteckningsbok
med tusen sidor
och några regler för hur den ska användas.

<!-- S10 -->
För det första har varje sida ett nummer.
Nu har varje ställe i boken
en adress.
Sidan fyrahundratolv
betyder exakt ett ställe.

<!-- S11 -->
För det andra är de första sidorna
en innehållsförteckning.
Varje rad anger ett namn
och sidan där det står.
Pannkakor: sidan tolv.

<!-- S12 -->
För det tredje finns det längst bak
en lista över de sidor
som fortfarande är tomma.

<!-- S13 -->
Lägg nu till ett recept.
Du letar längst bak efter en tom sida.
Du skriver receptet där.
Du lägger till en rad i innehållsförteckningen.
Och du stryker den sidan
från listan över tomma sidor.

<!-- S14 -->
Ett recept, tre ställen.
Och alla tre måste stämma överens.

<!-- S15 -->
Sedan växer pannkaksreceptet.
Sidan tolv är full,
och sidan tretton är redan upptagen.
Så det fortsätter på sidan åttiosju,
och innehållsförteckningen måste ange det.

<!-- S16 -->
Och här är haken.
Om du vill ha plats för tusen rader
i innehållsförteckningen
måste du avsätta de sidorna
innan du skriver ett enda recept.

<!-- S17 -->
Det var liknelsen.
Så här ser det faktiskt ut på disken.

<!-- S18 -->
En disk vet ingenting om filer,
mappar eller namn.
Allt den erbjuder är en lång rad
numrerade platser, så kallade sektorer.

<!-- S19 -->
På en hårddisk
ligger datan på snurrande skivor.
En SSD lagrar den i flashminne.
Hur som helst ber datorn bara
om en sektor med dess nummer,
och disken räknar själv ut var den finns.

<!-- S20 -->
En sektor är liten.
Oftast 512 byte,
eller 4 096
på nyare diskar.

<!-- S21 -->
Filsystem arbetar oftast
med större bitar, så kallade block.
I ext4 är ett block fyra kilobyte,
lika stort som åtta sektorer av den gamla sorten.

<!-- S22 -->
De numrerade blocken
är bokens sidor.
Det filsystemet fortfarande behöver
är de två andra delarna:
en innehållsförteckning
och en lista över vad som är ledigt.

<!-- S23 -->
Det är det formateringen bygger.
Och det är dit
de sjutton gigabyten tog vägen.

<!-- S24 -->
Ext4 avsätter en post
för varje fil och mapp
som disken ska kunna rymma samtidigt.
Varje post är
256 byte.
Den kallas inod.

<!-- S25 -->
En dag kommer varje inod att ange
hur stor en fil är,
när den ändrades,
vem som får öppna den
och vilka block som rymmer dess innehåll.

<!-- S26 -->
På en disk på en terabyte
förbereder ext4 ungefär
sextioen miljoner sådana.
Alla tomma, alla väntande.
Det är nästan sexton gigabyte
tomma poster.

<!-- S27 -->
Varför sextioen miljoner?
Ext4 gör en enkel gissning:
en inod per sexton kilobyte
utrymme på disken.
På en vanlig dator
kommer de flesta av de posterna
aldrig att användas.

<!-- S28 -->
Ungefär en gigabyte till
går till en journal,
som vi återkommer till.
Resten är annan bokföring,
bland annat en karta med en bit per block
som anger om blocket är använt eller ledigt.

<!-- S29 -->
Det antalet är också fast.
Gör slut på alla poster
med miljontals små filer,
så säger disken att den är full...
fast det finns gigabyte kvar.

<!-- S30 -->
Så låt oss se hur det fungerar.
Vi skapar en fil som heter hello.txt.
Inuti bara ett ord: hello.
Fem bokstäver. Fem byte.

<!-- S31 -->
Filsystemet väljer en tom inod.
Säg nummer tretton.
Sedan hittar det ett ledigt block i kartan
och markerar det som använt.

<!-- S32 -->
Det skriver de fem byten i blocket.
Sedan fyller det i inoden:
fem byte lång, skapad alldeles nyss
och lagrad i det enda blocket.

<!-- S33 -->
Och till sist lägger det till
en rad i mappen:
namnet hello.txt
och numret tretton.

<!-- S34 -->
Lägg märke till var namnet hamnade.
Inte i filen.
Inte i inoden.
Namnet finns i mappen,
som egentligen bara är en lista
med namn och nummer.

<!-- S35 -->
Och en mapp är bara ännu en fil.
Det den råkar innehålla
är den listan.

<!-- S36 -->
Det är också därför en flytt av en fil
till en annan mapp i samma filsystem
går på ett ögonblick, hur stor filen än är.
Den ena mappen förlorar en rad,
den andra får en,
och oftast flyttas
innehållet inte alls.

<!-- S37 -->
Fem byte text...
och på disken tar det upp
4 096.
Ett block är den minsta bit
som filsystemet delar ut,
så även en pytteliten fil kostar ett helt block.

<!-- S38 -->
När filen växer ur sitt block
hittar filsystemet ett annat ledigt.
Kanske precis bredvid.
Kanske någon helt annanstans.
Och inoden håller reda på båda.

<!-- S39 -->
Med tiden kan en stor fil hamna
i bitar över hela disken.
En hårddisk måste hoppa mellan dem.
En SSD klarar det mycket bättre.

<!-- S40 -->
Programmet som sparade filen
vet ingenting om det här.
Det sa ”spara hello.txt”,
och allt annat hände under ytan.

<!-- S41 -->
Radera den nu.
Namnet tas bort från mappen.
Inoden markeras som ledig.
Blocket hamnar på listan över lediga igen.

<!-- S42 -->
På en traditionell hårddisk
ligger själva de fem byten kvar.
Ingen har rört dem.
De finns kvar tills något nytt
skrivs ovanpå.

<!-- S43 -->
Det är därför en raderad fil
ibland kan återställas.
Att radera suddar oftast inte ut
själva innehållet.
Det markerar bara utrymmet som tillgängligt.

<!-- S44 -->
På en SSD är det mer osäkert.
Filsystemet kan tala om för disken
att de blocken inte behövs längre,
och disken kan kasta det som finns i dem.
Efter det är chansen att få tillbaka filen
mycket mindre.

<!-- S45 -->
Så ett filsystem är egentligen en bokförare.
Att skapa den här enda filen
innebar att uppdatera tre saker:
mappen, inoden
och kartan över lediga block.

<!-- S46 -->
Bryt nu strömmen
mitt under sparandet av en fil.

<!-- S47 -->
Kanske markerades blocket som använt,
men ingen inod pekar på det än.
Det utrymmet är helt enkelt förlorat.
Irriterande, men ofarligt.

<!-- S48 -->
Eller så pekar inoden på ett block
som kartan fortfarande anger som ledigt.
Nästa fil kan skrivas
rakt ovanpå det.
Och den första förstörs i det tysta.

<!-- S49 -->
Därför för ext4 en journal.
Innan det ändrar sin bokföring
skriver det ner vad det tänker göra.
Efter en krasch utför det på nytt bara de ändringar
som det hann skriva ner färdigt
och markera som klara.
Allt ofärdigt ignoreras.

<!-- S50 -->
Och så finns det ett tystare problem.
Ibland ändrar en disk en bit
utan att säga det till någon.

<!-- S51 -->
Ext4 skyddar sina egna poster
med kontrollsummor,
så att det kan upptäcka skador där.
Men innehållet i dina filer?
Det litar det helt enkelt på.

<!-- S52 -->
Vissa filsystem kontrollerar båda.
Och vissa har en andra kopia,
så att när den ena kopian skadas
kan de reparera den från den andra.
Att upptäcka ett problem och att åtgärda det
är inte samma sak.

<!-- S53 -->
Så alla filsystem gör samma jobb:
numrerade block, en lista med namn
och en karta över vad som är ledigt.

<!-- S54 -->
Men valen skiljer sig åt.
Ext4 förbereder sextioen miljoner poster
innan du har sparat någonting.
NTFS, i Windows, håller sina poster
i en enda stor tabell som växer efter hand.

<!-- S55 -->
Och Btrfs förbereder inte
en fast tabell med inoder i förväg.
Det skapar dem allteftersom filer kommer till.
Och normalt skriver det inte över
data på plats.
Det skriver en ny kopia
och släpper först därefter den gamla.

<!-- S56 -->
Som standard beräknar det också kontrollsummor för dina filer,
så att det märker när de har skadats.

<!-- S57 -->
Och eftersom den gamla kopian
inte skrivs över
kan en ögonblicksbild hålla den vid liv.
Det ändrar svaret
på nästan varje fråga i den här videon:
vad en krasch gör,
vad radering betyder
och till och med vad en kopia är.

<!-- S58 -->
Det är där nästa video börjar.

<!-- S59 -->
Så här kommer en fråga till dig.
Ska ett filsystem bara lagra dina filer,
eller ska det skydda dem också?
Skriv i kommentarerna.
