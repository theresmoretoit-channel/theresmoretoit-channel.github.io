<!-- S01 -->
1993 kördes ett spel som hette Doom
på en dator
med 4 megabyte minne.

<!-- S02 -->
Det är ungefär storleken
på ett enda foto i din mobil.

<!-- S03 -->
Det fanns ingen 3D-accelerator.
Huvudprocessorn
skötte all rendering.

<!-- S04 -->
I dag börjar en utvecklare med en spelmotor,
som Unity eller Unreal,
som tar hand om grafik, ljud,
minne och hårdvara.

<!-- S05 -->
Under DOS var allt det där
utvecklarens problem.
Och ganska ofta spelarens också.

<!-- S06 -->
Så hur svårt var det
att göra ett spel för DOS?

<!-- S07 -->
Vi börjar med minnet,
för minnet var en enda röra.

<!-- S08 -->
Den ursprungliga IBM PC från 1981
kunde adressera 1 megabyte minne.

<!-- S09 -->
Men bara de första
640 kilobyten
var tänkta för program.

<!-- S10 -->
De övriga 384
var reserverade för videominne,
expansionskort och BIOS.

<!-- S11 -->
I mer än tio år
startade DOS normalt program
inom det utrymmet.
Allt utanför krävde extra arbete.

<!-- S12 -->
Det är därifrån det berömda citatet kommer.
640K borde räcka för alla.

<!-- S13 -->
Det brukar tillskrivas Bill Gates.
Det finns inget belägg för att han någonsin sa det,
och han förnekar det.

<!-- S14 -->
I början av nittiotalet
kom en PC med 4 megabyte,
eller 8.

<!-- S15 -->
Och ett spel kunde ändå stanna
med orden
"inte tillräckligt med minne".

<!-- S16 -->
Att ha minnet
och att kunna använda det
var två olika saker.

<!-- S17 -->
Ett sätt att komma runt det var expanderat minne,
eller EMS.

<!-- S18 -->
Ett fönster på 64 kilobyte
satt i den övre delen
av den första megabyten.
Genom det kunde ett program se
4 sidor extra minne,
på 16 kilobyte vardera,

<!-- S19 -->
och byta ut dem mot andra,
som att bläddra i en bok
genom ett hål i ett papper.

<!-- S20 -->
Ett annat sätt var utökat minne,
som nåddes via en drivrutin som hette HIMEM.

<!-- S21 -->
Och det är här
utvecklarens problem
blev spelarens.

<!-- S22 -->
Drivrutiner för musen, cd-enheten
eller ljudkortet
tog en tugga av det dyrbara minnet,
om du inte lyckades ladda dem i det övre minnet.

<!-- S23 -->
Så spelarna lärde sig redigera två filer,
CONFIG.SYS och AUTOEXEC.BAT.

<!-- S24 -->
Ett spel ville ha EMS.
Ett annat ville ha det avstängt,
med en inställning som hette NOEMS.
Och ett tredje behövde varenda ledig kilobyte.

<!-- S25 -->
1993 lade MS-DOS 6 till
en meny vid uppstart.

<!-- S26 -->
Du valde konfigurationen
för spelet du ville spela,
och datorn startade för just det spelet.

<!-- S27 -->
Vissa fick till slut
ett eget menyval
för nästan varje spel de ägde.

<!-- S28 -->
Men vid det laget
hade de större spelen hittat
ett sätt att ta sig runt DOS begränsningar.

<!-- S29 -->
Sedan 386:an
kunde processorn själv köras
i 32-bitars skyddat läge,
med plats för upp till 4 gigabyte.

<!-- S30 -->
Vi har tittat på skyddat läge
i en tidigare video.
Men DOS kunde inte använda det.

<!-- S31 -->
Så spelen tog med sig en egen hjälpreda,
en DOS-extender.
Den mest kända var DOS/4GW.

<!-- S32 -->
Den följde med en populär kompilator,
Watcom C.

<!-- S33 -->
När ett spel startade
växlade DOS/4GW processorn
till skyddat läge
och gav spelet tillgång
till minne bortom DOS-gränsen.

<!-- S34 -->
DOS fanns fortfarande kvar därunder
och skötte tjänster som filåtkomst.
Men spelet körde nu i skyddat läge,
inte som ett traditionellt DOS-program.

<!-- S35 -->
Om du spelade DOS-spel på nittiotalet
har du sett dess namn
blinka förbi på skärmen.

<!-- S37 -->
Nu till bilden.
I ett av de mest använda VGA-lägena,
kallat Mode 13h,
var skärmen 320
gånger 200 pixlar,
med 256 färger.

<!-- S38 -->
Varje pixel var en byte.
För att färga en pixel
skrev du ett tal i minnet.
Inget grafikbibliotek. Bara minne.

<!-- S39 -->
Hela skärmen tog
64 000 byte.

<!-- S40 -->
Det är strax under 64 kilobyte,
tillräckligt lite för att rymmas i ett segment,
det block som ett 16-bitarsprogram
kunde adressera på en gång.
För en gångs skull var minnet på din sida.

<!-- S41 -->
Men om du ritar direkt
på den synliga skärmen
ser spelaren halvfärdiga bilder,
och bilden flimrar.

<!-- S42 -->
Så spelen ritade varje bildruta
i en dold buffert först
och kopierade sedan den färdiga bilden
till videominnet.

<!-- S43 -->
1991 publicerade Michael Abrash,
programmerare och skribent,
ett bättre sätt.
Han kallade det Mode X.

<!-- S44 -->
Det använde en del av VGA
som de flesta programmerare
aldrig hade rört.

<!-- S45 -->
Det gav kvadratiska pixlar
och plats för flera skärmar
i videominnet.

<!-- S46 -->
Spelet ritade på en skärm
som ingen kunde se
och växlade sedan helt enkelt till den.
Men det var mycket svårare att programmera.

<!-- S47 -->
Sedan var det ljudet.
Och ljud var ett lotteri.

<!-- S48 -->
Datorns egen högtalare
var byggd för att pipa.

<!-- S49 -->
Sedan kom ljudkort
och annan ljudhårdvara.
Inga två av dem
fungerade på samma sätt.

<!-- S50 -->
AdLib, med ett Yamaha-chip
som syntetiserade musik.
Sound Blaster, som också kunde spela
inspelat ljud.

<!-- S51 -->
Roland MT-32,
en dyr låda med rikare instrument.
Gravis UltraSound.

<!-- S52 -->
Att stödja alla ljudkort
innebar att skriva olika drivrutiner.

<!-- S53 -->
Och spelet måste veta
var kortet satt.
Dess port, dess avbrott
och dess DMA-kanal.

<!-- S54 -->
Det vanliga svaret, för ett Sound Blaster,
var port 220, IRQ 7, DMA 1.
Oftast.

<!-- S55 -->
Fick du en av dem fel
blev spelet tyst.
Eller så frös det.

<!-- S56 -->
1991 släppte en programmerare vid namn John Miles
ett bibliotek
som pratade med många ljudkort
genom ett enda gränssnitt.

<!-- S57 -->
Ett spel kunde skriva sin ljudkod en gång
och låta biblioteket sköta kortet.

<!-- S58 -->
Det var ännu ett lager
mellan spelet och hårdvaran.
Kom ihåg det.

<!-- S59 -->
Och sedan var det hastigheten.
Programmerare räknade
varje steg processorn tog.

<!-- S63 -->
För att hitta en pixel på skärmen
multiplicerar du dess rad
med 320.

<!-- S63b -->
På äldre processorer
kunde multiplikation vara dyr.

<!-- S64 -->
Men 320
är 256
plus 64.
Båda är potenser av två.

<!-- S65 -->
Så du kan ersätta multiplikationen
med två bitskift och en addition.

<!-- S67 -->
Chris Sawyer gick ända ner till hårdvaran.
Han skrev Transport Tycoon 1994
nästan helt i assembler,

<!-- S68 -->
de instruktioner
som processorn själv förstår,
en i taget.

<!-- S69 -->
Och ibland
räckte inte ens allt det där.

<!-- S70 -->
1990 hade Wing Commander en bugg
som teamet inte kunde hitta,
och deadline närmade sig.

<!-- S71 -->
När du avslutade spelet
kraschade minneshanteraren
med ett felmeddelande.

<!-- S72 -->
Så en programmerare, Ken Demarest,
öppnade minneshanteraren
i en hexeditor
och ändrade texten i meddelandet.

<!-- S73 -->
Nu stod det:
"Tack för att du spelade Wing Commander."

<!-- S74 -->
Sedan hittade teamet den riktiga buggen,
och skämtet kom aldrig med i det släppta spelet.

<!-- S74b -->
Vissa spelare är fortfarande säkra på att de såg det.
Och senare spel från Origin
tog faktiskt farväl just så.

<!-- S75 -->
Vilket för oss tillbaka till Doom.

<!-- S76 -->
Doom använde DOS/4GW
och kördes som ett 32-bitarsprogram.

<!-- S77 -->
Hårdvara för flyttal
fanns inte garanterat i varje PC.

<!-- S78 -->
Så Doom använde fixpunktsaritmetik.
Heltal
där de lägsta 16 bitarna
stod för bråkdelen.

<!-- S79 -->
Och dess värld var inte
riktigt tredimensionell.

<!-- S80 -->
Varje bana är en platt planritning,
med en höjd för varje golv
och varje tak.

<!-- S81 -->
Ett rum kan aldrig ligga ovanför ett annat.
Och du kan inte riktigt titta upp eller ner.

<!-- S82 -->
Innan en bana kunde spelas
delade ett verktyg upp kartan
i ett binärt träd, ett BSP.

<!-- S83 -->
Motorn går igenom trädet
framifrån och bakåt,
med början på spelarens sida,
och hoppar över områden som inte syns.

<!-- S84 -->
Och Doom skrevs inte ens på DOS.

<!-- S85 -->
id Software byggde det
på NeXT-arbetsstationer
och kompilerade resultatet för DOS.

<!-- S86 -->
Doom var ingen allmän 3D-motor.
Den var byggd för exakt
en sorts värld.
Den specialiseringen
hjälpte den att köras på en 386:a.

<!-- S87 -->
Och andra studior ville ha den världen.

<!-- S88 -->
Raven Software licensierade Dooms motor
för Heretic 1994
och Hexen 1995.

<!-- S89 -->
Doom bidrog till att etablera
ett nytt sätt att göra spel.
Studior kunde licensiera en befintlig motor
i stället för att bygga allt från grunden.

<!-- S90 -->
En minnesextender.
Ett ljudbibliotek.
En licensierad motor.

<!-- S91 -->
Var och en lyfte ett problem
från utvecklarens axlar.
Och lagren fortsatte att växa,
till de motorer
som utvecklare börjar med i dag.

<!-- S92 -->
Så var det svårare att göra spel förr?
På många sätt, ja.

<!-- S93 -->
Men svårigheten försvann inte.
Den flyttade.

<!-- S94 -->
I dag kämpar utvecklare
med gigabyte av grafik och ljud
och miljontals polygoner,
i stället för några hundra kilobyte.

<!-- S95 -->
Under DOS behövde till och med spelaren
veta vart minnet tog vägen.

<!-- S96 -->
Så här är en fråga till dig.
Minns du när du byggde
en startmeny bara för att få igång ett spel?
Och var det ett slit,
eller halva nöjet?
Skriv det i kommentarerna.
