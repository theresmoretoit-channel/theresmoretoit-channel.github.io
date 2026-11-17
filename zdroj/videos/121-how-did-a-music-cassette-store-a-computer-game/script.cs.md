<!-- S01 -->
Zmáčkneš play na kazeťáku.
A z reproduktoru vyleze tohle.

<!-- S02 -->
Není to hudba.
A není to ani zvukový doprovod hry.

<!-- S03 -->
Je to ta hra.
Každé zapištění je kus programu
a počítač ho poslouchá.

<!-- S04 -->
Kazeťák nemá ponětí.
Podle něj hraje písničku.

<!-- S05 -->
Jak se tedy z písničky stane hra?
A proč kvůli jedné špatné notě
mohlo přijít vniveč pět minut čekání?

<!-- S06 -->
Tady je ten trik,
na jednom konkrétním stroji:
ZX Spectru,
britském domácím počítači z roku 1982.

<!-- S07 -->
Používá dva druhy pulzů.
Krátká dvojice pulzů znamená nulu.

<!-- S08 -->
Jednička je stejná dvojice,
jen každý pulz trvá dvakrát déle,
takže její tón zní o oktávu níž.

<!-- S09 -->
Pošli zhruba čtrnáct set bitů
za sekundu
a dostaneš přesně ten zvuk, který právě zazněl.

<!-- S09b -->
Znamená to taky, že program plný nul
se nahraje rychleji než program plný jedniček.
Každá jednička se posílá dvakrát déle.

<!-- S10 -->
Kdo vyrůstal v Americe,
ten ho možná nikdy neslyšel.

<!-- S11 -->
Což je zvláštní,
protože samotný nápad byl americký.

<!-- S12 -->
V roce 1975 se na setkání v Kansas City
počítačoví nadšenci dohodli,
jak ukládat data jako zvuk
na obyčejné audiokazety.

<!-- S12b -->
Jedničku tvořilo osm rychlých kmitů
vysokého tónu,
nulu čtyři pomalejší kmity nízkého.
Tři sta bitů za sekundu.

<!-- S13 -->
První stroje jako Apple II
a TRS-80
ukládaly své programy
na úplně běžné magnetofony.

<!-- S14 -->
Jenže americké domácí počítače
se rychle posunuly dál.

<!-- S15 -->
V roce 1983 otiskl jeden časopis průzkum:
devět z deseti nových majitelů Commodore 64
si kupovalo disketovou mechaniku
rovnou spolu s počítačem.

<!-- S16 -->
V Británii se příběh vydal opačným směrem.

<!-- S17 -->
Spectrum stálo sto
dvacet pět liber
a nemělo vůbec žádné úložiště.
Stačil kazeťák,
který už byl doma.

<!-- S18 -->
Takže pro miliony dětí po celé Evropě
byl tenhle zvuk zvukem
hry, která se chystá začít.

<!-- S18b -->
Když se hry nahrávaly dost často,
šlo dokonce poznat, o jakou hru jde,
jen podle toho skřípění.

<!-- S19 -->
Pojďme tedy sledovat jednu hru
z pásky až do počítače.

<!-- S20 -->
Napíšeš LOAD, zmáčkneš enter
a pustíš play.

<!-- S21 -->
Nejdřív přijde stálé hučení,
osm set kmitů za sekundu,
zhruba pět sekund.

<!-- S22 -->
Nenese vůbec žádná data.
Je tam proto, aby počítač
našel signál
a chytil se jeho rytmu.

<!-- S23 -->
Pak dva rychlé pulzy, synchronizace.
Znamenají: odsud jsou to data.

<!-- S24 -->
Jako první dorazí
krátká hlavička.
Devatenáct bajtů:
jméno až o deseti písmenech,
jaký je to druh souboru
a jak bude dlouhý.

<!-- S25 -->
Pak druhé, kratší hučení,
tentokrát dvě sekundy,
a pak samotná hra.

<!-- S26 -->
Každý bajt je osm takových tónů,
jeden za druhým,
a mezi bajty nejsou vůbec žádné mezery.

<!-- S27 -->
A počítač žádné tóny neslyší.
Měří čas mezi jednou hranou
signálu a další.

<!-- S28 -->
Krátká dvojice je nula.
Dlouhá dvojice je jednička.

<!-- S28a -->
To je celý dekodér.

<!-- S28b -->
A ten zvuk na začátku videa
není zvukový efekt.
Vyrobili jsme ho přesně podle těchhle pravidel
a je v něm skutečný program pro Spectrum.

<!-- S28c -->
Celý ho pustíme úplně na konci.
Nahraj si ho a Spectrum ho načte.

<!-- S29 -->
Většina her nejdřív ukázala obrázek
a ten se nahrával v podivném pořadí.

<!-- S30 -->
Objevily se tenké proužky, osm řádků od sebe,
pak se doplňovaly řádek po řádku,
po třetinách obrazovky.
A barvy přišly až nakonec,
přejely shora přes všechno.

<!-- S31 -->
Samotný obrázek
trval zhruba čtyřicet sekund.
Celá hra kolem pěti minut.

<!-- S32 -->
A na konci každého bloku
přijde ještě jeden bajt.

<!-- S33 -->
Při ukládání prožene Spectrum
každý bajt bloku
jednoduchým pravidlem jménem XOR
a výsledek zapíše jako další bajt.

<!-- S34 -->
Při nahrávání ten výpočet zopakuje.
Když výsledky souhlasí,
blok dorazil v pořádku.

<!-- S35 -->
Když ne, Spectrum řekne tohle.

<!-- S36 -->
Pět minut čekání
a jeden bajt rozhodne,
že to bylo celé k ničemu.
Přetočit a znovu od začátku.

<!-- S37 -->
Kupodivu poškozená hlavička
žádnou chybu nevyvolá.
Spectrum ji prostě přejde
a poslouchá dál, jestli nepřijde další.

<!-- S38 -->
Jiné počítače vsadily na jiné karty.

<!-- S39 -->
Commodore 64 nahrával
každý blok dvakrát,
takže poškozené místo v jedné kopii
šlo zachránit z té druhé.

<!-- S40 -->
Bezpečnější, ale pomalé.
S vestavěnou rutinou Commodoru
trval program o čtyřiceti kilobajtech
zhruba dvanáct a půl minuty.

<!-- S41 -->
Vydavatelé her si proto psali
vlastní, rychlejší nahrávací rutiny,
některé až zhruba desetkrát rychlejší.

<!-- S42 -->
A pak tu byl samotný kazeťák.

<!-- S43 -->
Moc potichu
a hrany zapadnou v šumu.
Moc nahlas
a slijí se do sebe.

<!-- S44 -->
Páska, která běží o trochu rychleji nebo pomaleji,
natáhne každý pulz,
a počítač přitom měří čas.

<!-- S45 -->
Nejhorší ze všeho byl azimut,
tedy úhel hlavy.
Páska nahraná na jednom přístroji
nemusela na jiném správně hrát.

<!-- S46 -->
Lidi proto strkali malý šroubovák
do dírky vedle hlavy,
otáčeli jím po kouscích
a poslouchali.

<!-- S47 -->
Vypadalo to jako pověra.
Bylo to ladění signálu.

<!-- S48 -->
Ale všimni si, co kazeťák
nikdy dělat nemusel.

<!-- S49 -->
Nikdy nerozuměl jedinému bitu.
Nahrál zvuk
a zase ho přehrál.

<!-- S50 -->
Což znamená, že program
kazetu vlastně nepotřeboval.
Cokoli, co dokázalo přenášet zvuk,
dokázalo přenášet i software.

<!-- S50b -->
Taky to znamenalo, že zkopírovat hru
bylo stejně snadné jako zkopírovat album.
Dva kazeťáky a kabel.

<!-- S51 -->
Atari využilo obě stereo stopy.
Na jedné program,
na druhé hlas,
který k tobě mluvil z televize,
zatímco se hra nahrávala.

<!-- S52 -->
V Jugoslávii pořad Rádia Bělehrad
vysílal programy éterem.

<!-- S53 -->
Posluchači si je nahrávali na pásku,
zhruba sto padesát programů
mezi lety 1983 a 1986.

<!-- S54 -->
V Československu to byla televize.
Program zněl jako zvuk
pod závěrečnými titulky.

<!-- S55 -->
A v roce 1983 zpěvák Pete Shelley
schoval program pro Spectrum
na konec vinylového alba.

<!-- S56 -->
Zkopíruj ho na pásku, nahraj
a na obrazovce se objeví texty
souběžně s písněmi.

<!-- S57 -->
Jenže to mělo háček.

<!-- S58 -->
Rádio dokázalo dopravit zvuk
ke každému počítači v zemi.
Rozumět mu ale uměl jen ten správný.

<!-- S59 -->
Pusť hru pro Spectrum Commodoru
a Commodore uslyší šum.
Bity něco znamenají jen
pro stroj, který zná formát.

<!-- S60 -->
Nizozemský rozhlas se to proto pokusil vyřešit.
V roce 1982 vytvořil BASICODE:
jeden zvukový formát
a malý překládací program
pro každý druh počítače.

<!-- S61 -->
A ten problém nikdy nezmizel.
Soubor je k užitku jen tehdy,
když ho něco ještě dokáže přečíst.

<!-- S62 -->
Kazety samozřejmě prohrály.
Diskety byly rychlejší,
pak pevné disky, pak flash.

<!-- S63 -->
Až na to, že páska vlastně nikdy neodešla.
Datová centra dodnes ukládají
své archivy na magnetickou pásku.

<!-- S64 -->
Jedna moderní kazeta LTO-9
pojme osmnáct terabajtů.

<!-- S65 -->
Přepočteno na rychlost Spectra
by ta kapacita zaplnila zhruba
dvacet devět milionů kazet
a nahrávala by se
přes tři tisíce let.

<!-- S66 -->
Pořád je to ale tentýž nápad.
Magnetické stopy na pohybující se pásce,
které se zase mění v čísla,
když je potřebuješ.

<!-- S67 -->
Takže až příště uslyšíš to skřípění,
vzpomeň si, co to je.
Žádný šum.
Program, který cestuje jako zvuk.

<!-- S68 -->
A někde v roce 1985
sedí dítě před televizí
a čeká, až to přestane.
Protože až to přestane,
začne hra.

<!-- S69 -->
Takže tady je otázka pro tebe.
Jestli znáš nahrávání her z kazety,
co si z toho pamatuješ nejvíc?
Napiš to do komentářů.

<!-- S70 -->
A jak jsme slíbili, tady je ten program.
Stejně jako tehdy Československá televize
jsme ho dali pod závěrečné titulky.
