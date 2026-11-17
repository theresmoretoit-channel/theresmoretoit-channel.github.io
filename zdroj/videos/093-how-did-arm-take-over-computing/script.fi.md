# Miten ARM valtasi tietotekniikan?

<!-- S01 -->
Vuonna 1985 insinöörit Britanniassa
käynnistivät upouuden suorittimen
ensimmäistä kertaa.

<!-- S02 -->
Se toimi.
Jo se oli pieni ihme.

<!-- S03 -->
Mutta sitten he huomasivat jotain outoa.
Sirun virransyöttöä
ei ollut kytketty.

<!-- S04 -->
Ja silti se pyöri.

<!-- S05 -->
Se pärjäsi pienen pienillä virroilla,
jotka vuotivat sisään sen tulonastoista
ympärillä olevien sirujen signaaleista.

<!-- S06 -->
Kun he mittasivat sen kunnolla,
suoritin tarvitsi
noin kymmenesosan watista.

<!-- S07 -->
Kukaan ei ollut tavoitellut sitä.
Insinöörit halusivat vain sirun,
joka olisi halpa valmistaa.

<!-- S08 -->
Se siru oli ensimmäinen ARM-suoritin.

<!-- S09 -->
Neljäkymmentä vuotta myöhemmin
sen jälkeläisiä on lähes jokaisessa älypuhelimessa.
Applen tietokoneissa.
Joissakin maailman suurimmista
datakeskuksista.

<!-- S10 -->
Satoja miljardeja siruja.

<!-- S11 -->
Miten siis brittiläisen
kotitietokoneyhtiön suoritin
valtasi tietotekniikan?

<!-- S12 -->
Vastaus ei ole yksinkertaisesti se,
että se kulutti hyvin vähän virtaa.
Se oli melkein sattumaa.

<!-- S12b -->
Muuten, jos pidät tällaisista
videoista, voit tilata kanavan.

Se auttaa kanavaa todella paljon.

<!-- S13 -->
Jotta ymmärtäisimme, mitä oikeasti tapahtui,
meidän on palattava vuoteen 1983.

<!-- S14 -->
Yhtiö oli Acorn Computers.
Sen BBC Micro oli luokkahuoneissa
kaikkialla Britanniassa.

<!-- S15 -->
BBC Micro käytti vanhempaa,
kahdeksanbittistä 6502-sirua.
Seuraavaa konettaan varten
Acorn tarvitsi jotain paljon nopeampaa.

<!-- S16 -->
Tiimi siis testasi
markkinoiden uudet suorittimet.
Mikään ei tehnyt sitä, mitä Acorn halusi.

<!-- S17 -->
Ne olivat monimutkaisia,
eikä mikään niistä oikein sopinut siihen,
mitä Acorn halusi rakentaa.

<!-- S18 -->
Sitten kaksi Acornin insinööriä,
Sophie Wilson ja Steve Furber,
matkusti Arizonaan
yritykseen, jonka oli perustanut yksi
6502:n alkuperäisistä suunnittelijoista.

<!-- S19 -->
He odottivat suurta siruyhtiötä.
Sen sijaan he löysivät kourallisen ihmisiä,
jotka tekivät töitä omakotitalossa esikaupungissa.

<!-- S20 -->
Ja he palasivat kotiin
mukanaan yksinkertainen johtopäätös.
Jos he pystyvät suunnittelemaan suorittimen...
niin pystymme mekin.

<!-- S22 -->
Siihen aikaan suorittimiin tuli
yhä monimutkaisempia käskyjä.

<!-- S23 -->
Yksi käsky saattoi hakea
luvun muistista,
laskea sillä
ja kirjoittaa tuloksen takaisin.

<!-- S24 -->
Kätevää ohjelmoijalle.
Mutta jokainen tällainen käsky
tekee sirusta vaikeamman rakentaa.

<!-- S25 -->
Siru tarvitsee lisää logiikkaa
jo pelkästään selvittääkseen, mitä kukin käsky tarkoittaa.
Lisää transistoreja.
Lisää suunnitteluaikaa.

<!-- S26 -->
Berkeleyn ja Stanfordin tutkijat
olivat esittäneet radikaalin kysymyksen.

<!-- S27 -->
Entä jos suorittimessa
olisi vain yksinkertaisia käskyjä
ja kääntäjä hoitaisi loput?

<!-- S28 -->
He kutsuivat sitä nimellä RISC.
Supistetun käskykannan tietokone.

<!-- S29 -->
Sophie Wilson suunnitteli
ARMin käskyt samalla periaatteella.

<!-- S30 -->
Laskutoimitukset käyttävät vain
sirun omia rekistereitä,
pieniä, nopeita lokeroita suorittimen sisällä.
Muistin käsittelyyn on omat käskynsä.

<!-- S31 -->
Muistissa olevan luvun lisääminen
vaatii siis kolme vaihetta.
Lataa.
Laske yhteen.
Tallenna.

<!-- S32 -->
Tätä kutsutaan load-store-arkkitehtuuriksi.

<!-- S33 -->
Ohjelmalle enemmän vaiheita.
Mutta jokainen vaihe on säännönmukainen,
ennustettava
ja helppo dekoodata.

<!-- S34 -->
Ja ARMilla oli runsaasti rekistereitä
käytettävissään.
Kuusitoista, kukin 32-bittinen.
6502:ssa oli kolme pientä.

<!-- S35 -->
Tuloksena oli ARM1.

<!-- S36 -->
Siinä oli noin
25 000 transistoria.

<!-- S37 -->
Intelin muutamaa vuotta aiemmin
julkaistussa 286:ssa oli noin 134 000.

<!-- S38 -->
Vähemmän transistoreja tarkoitti pienempää sirua.
Halvempaa sirua.

<!-- S39 -->
Ja ikään kuin sivuvaikutuksena
sirua, joka tuskin kulutti virtaa lainkaan.

<!-- S40 -->
Siitä se kymmenesosa watista
oli peräisin.
Acorn halusi halvan muovikotelon,
mikä tarkoitti, että kulutus piti pitää alle watin.
Siksi he suunnittelivat huolella...
ja päätyivät kymmenesosaan siitä.

<!-- S41 -->
Vuonna 1987 ARMin nopeampi versio
päätyi Acornin uuteen tietokoneeseen,
Archimedesiin.

<!-- S42 -->
Se oli yksi aikansa nopeimmista
henkilökohtaisista tietokoneista.

<!-- S43 -->
Eikä sillä ollut juuri merkitystä.

<!-- S44 -->
Maailma osti IBM-yhteensopivia PC:itä
Intelin suorittimilla.
Ohjelmistot tehtiin niille.
Niitä yritykset ostivat.

<!-- S45 -->
Archimedes jäi
enimmäkseen brittikouluihin.

<!-- S46 -->
Ja Acorn itse oli vaikeuksissa.
Olivetti oli joutunut pelastamaan sen
jo vuonna 1985.

<!-- S48 -->
Sitten apu tuli Applelta.
Apple rakensi kämmentietokonetta
nimeltä Newton.

<!-- S49 -->
Se tarvitsi suorittimen,
joka olisi nopea, halpa
ja toimisi paristoilla.

<!-- S50 -->
ARM sopi täydellisesti.
Mutta Apple ei halunnut olla riippuvainen
sirusta, jonka omisti
kilpaileva tietokonevalmistaja.

<!-- S51 -->
Niinpä vuonna 1990 ARM-tiimi
irrotettiin Acornista
omaksi yhtiökseen.

<!-- S52 -->
Acorn, Apple
ja sirunvalmistaja VLSI
omistivat sen yhdessä.

<!-- S53 -->
Kaksitoista insinööriä.
Vanha lato Cambridgen lähellä.

<!-- S54 -->
Ja liiketoimintamalli,
joka osoittautui menestyksen todelliseksi avaimeksi.

<!-- S55 -->
Intel suunnitteli suorittimensa,
valmisti ne omissa tehtaissaan
ja myi ne.

<!-- S56 -->
ARM ei valmistaisi mitään.
Se myisi suunnitelman.

<!-- S57 -->
Mikä tahansa yritys voisi lisensoida sen,
rakentaa ARM-ytimen omaan siruunsa
ja maksaa pienen maksun
jokaisesta myymästään sirusta.

<!-- S58 -->
Sillä oli merkitystä,
koska sirun ei tarvitse olla
pelkkä suoritin.
ARM-ytimen ympärille
voit laittaa radion,
grafiikkapiirin,
kamerasuorittimen.

<!-- S59 -->
Yksi siru,
jonka suunnittelee se, joka sitä tarvitsee,
ja ARM keskellä.

<!-- S60 -->
ARMin ei tarvinnut voittaa Inteliä
henkilökohtaisissa tietokoneissa.
Se saattoi päätyä minkä tahansa sisään.

<!-- S61 -->
Ja 1990-luvulla
”mikä tahansa” tarkoitti yhä useammin
matkapuhelimia.

<!-- S62 -->
Pöytäkone voi käyttää
sataa wattia ja isoa tuuletinta.
Puhelin toimii akulla
taskussasi.

<!-- S63 -->
Vuosikymmenen lopulla
ARM-ytimiä oli
joissakin myydyimmistä puhelimista,
Nokialla ja muilla.

<!-- S64 -->
Sitten tuli iPod.
Sitten älypuhelin.

<!-- S65 -->
Miljardit ihmiset kantoivat yhtäkkiä
tietokonetta, jonka piti kestää
koko päivä akulla.

<!-- S66 -->
Ja suoritin, joka oli rakennettu
siksi, että se oli halpa,
osoittautui juuri sellaiseksi,
jota se maailma tarvitsi.

<!-- S67 -->
Siinä siis vastauksemme, eikö?
ARM on yksinkertainen,
yksinkertainen tarkoittaa energiatehokasta,
ja energiatehokas voittaa.

<!-- S68 -->
Ei ihan.

<!-- S69 -->
Katso modernin huippuluokan ARM-ytimen sisään.

<!-- S70 -->
Valtavat välimuistit.
Useita käskyjä suorituksessa yhtä aikaa.
Hyppyennustus,
eli arvaus siitä, mihin suuntaan ohjelma menee,
ennen kuin se on siellä.

<!-- S71 -->
Käskyjen suoritus epäjärjestyksessä,
eli käskyt ajetaan
siinä järjestyksessä, joka on nopein.

<!-- S72 -->
Sirulla miljardeja transistoreja.
Mikään siinä ei ole yksinkertaista.

<!-- S73 -->
Minne se yksinkertaisuus sitten katosi?

<!-- S74 -->
Juju on siinä, että suoritin
on oikeastaan kaksi eri asiaa.

<!-- S75 -->
Käskykanta on kieli,
jota ohjelmisto puhuu.
Mitä käskyjä on olemassa
ja mitä ne tarkoittavat.

<!-- S76 -->
Mikroarkkitehtuuri on kone,
joka ne oikeasti suorittaa.

<!-- S77 -->
Kieli voi pysyä yksinkertaisena,
vaikka sen alla oleva kone
muuttuu valtavan monimutkaiseksi.

<!-- S78 -->
Ja sama tapahtui
toisellakin puolella.

<!-- S79 -->
Intelin x86-käskyt
ovat tunnetusti monimutkaisia.

<!-- S80 -->
Mutta 1990-luvun puolivälistä lähtien
Intelin ja AMD:n suorittimet
ovat pilkkoneet ne sisäisesti
pieniksi, yksinkertaisiksi operaatioiksi.

<!-- S81 -->
Ne ajetaan sitten koneistossa,
joka muistuttaa paljon sitä,
joka on modernin ARM-ytimen sisällä.

<!-- S82 -->
Nimilappujen alla
nämä kaksi ovat käyneet yllättävän samanlaisiksi.

<!-- S83 -->
ARMin siistimmät käskyt auttavat yhä.
Ne on helpompi dekoodata,
mikä voi säästää hieman virtaa.

<!-- S84 -->
Mutta ne eivät ole mikään taianomainen etu,
jota x86 ei voisi koskaan saavuttaa.

<!-- S85 -->
ARM ei siis vallannut alaa
siksi, että se oli yksinkertainen.
Eikä sitä suunniteltu vähävirtaiseksi.

<!-- S86 -->
Se voitti, koska kolme asiaa osui kohdalleen.
Energiatehokas rakenne.
Liiketoimintamalli,
joka antoi kenen tahansa rakentaa ARMin varaan.
Ja maailma, joka yhtäkkiä tarvitsi
miljardeja akkukäyttöisiä tietokoneita.

<!-- S87 -->
Ja sitten, vuonna 2020,
tarina palasi Appleen.

<!-- S88 -->
Apple oli myynyt ARM-osuutensa
vuosia aiemmin,
kun se tarvitsi kipeästi rahaa.

<!-- S89 -->
Nyt se laittoi omat ARM-pohjaiset sirunsa
Maciin.

<!-- S90 -->
Samanlaisia ytimiä kuin iPhonessa,
skaalattuina isommiksi tietokonetta varten.
Nopeita ytimiä, energiatehokkaita ytimiä,
grafiikkaa ja paljon muuta
yhdellä sirulla.

<!-- S91 -->
Ne olivat nopeampia
kuin Intelin sirut, jotka ne korvasivat,
ja kannettavat toimivat paljon pidempään
yhdellä latauksella.

<!-- S92 -->
ARM ei ollut enää
pelkkä puhelinsuoritin.

<!-- S93 -->
Eikä ARM jäänyt siihen.
Se siirtyi myös datakeskuksiin,
joissa jokainen watti maksaa.
Amazon suunnittelee nykyään
omia ARM-palvelinsirujaan.

<!-- S95 -->
Ensimmäisessä ARM-sirussa oli noin
25 000 transistoria.
Nykyisissä niitä on miljardeja.

<!-- S96 -->
Lähes kaikki siinä,
miten ne toimivat sisäisesti, on muuttunut.

<!-- S98 -->
Pieni tiimi halusi
suorittimen, jonka se oikeasti pystyisi rakentamaan.

<!-- S99 -->
He eivät rakentaneet sitä puhelimia,
Applea
tai Intelin päihittämistä varten.

<!-- S100 -->
Ja lopulta
tärkein asia, jonka he tekivät,
ei ollut siru.

<!-- S101 -->
Se oli yksinkertainen perusta,
jonka varaan kaikki muut saattoivat rakentaa.
