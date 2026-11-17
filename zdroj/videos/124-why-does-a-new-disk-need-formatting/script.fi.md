<!-- S01 -->
Ostat upouuden levyn.
Yksi teratavu, täysin tyhjä.
Ennen kuin sille voi tallentaa yhtäkään tiedostoa,
se täytyy ensin alustaa.

<!-- S02 -->
Alustat sen siis ext4:ksi,
joka on vakiotiedostojärjestelmä
monissa Linux-tietokoneissa.
Oletusasetuksilla,
ennen kuin olet tallentanut yhtään mitään,
noin seitsemäntoista gigatavua on poissa.

<!-- S03 -->
Mitään ei ole vielä tallennettu.
Ei kuvia, ei asiakirjoja.
Mikä siis vie kaiken sen tilan?

<!-- S04 -->
Ja miksi levy ylipäätään
pitää alustaa?
Se osaa jo tallentaa dataa.
Se osaa lukea ja kirjoittaa biljoonia bittejä.

<!-- S05 -->
Miksei tietokone voi vain alkaa kirjoittaa
mihin tahansa, missä on tilaa?

<!-- S06 -->
Koska datan tallentaminen
ja sen löytäminen uudelleen
ovat kaksi hyvin eri ongelmaa.

<!-- S07 -->
Kuvittele virasto, joka jakaa
tyhjää paperia lomakkeiden sijaan.
Kaikki kirjoitetaan jonnekin...
eikä kukaan löydä mitään.

<!-- S08 -->
Levy ilman tiedostojärjestelmää
on se paperikasa.
Parempi vertaus
on kuitenkin muistivihko.

<!-- S09 -->
Kuvittele muistivihko,
jossa on tuhat sivua
ja muutama sääntö sen käyttöön.

<!-- S10 -->
Ensinnäkin jokaisella sivulla on numero.
Nyt jokaisella kohdalla vihossa
on osoite.
Sivu neljäsataakaksitoista
tarkoittaa täsmälleen yhtä paikkaa.

<!-- S11 -->
Toiseksi ensimmäiset sivut
ovat sisällysluettelo.
Jokaisessa merkinnässä on nimi
ja sivu, jolla se on.
Letut: sivu kaksitoista.

<!-- S12 -->
Kolmanneksi aivan lopussa
on luettelo sivuista,
jotka ovat vielä tyhjiä.

<!-- S13 -->
Lisää nyt resepti.
Etsit lopusta tyhjän sivun.
Kirjoitat reseptin sille.
Lisäät rivin sisällysluetteloon.
Ja yliviivaat sen sivun
tyhjien luettelosta.

<!-- S14 -->
Yksi resepti, kolme paikkaa.
Ja kaikkien kolmen on täsmättävä.

<!-- S15 -->
Sitten letturesepti kasvaa.
Sivu kaksitoista on täynnä,
ja sivu kolmetoista on jo varattu.
Joten se jatkuu sivulla kahdeksankymmentäseitsemän,
ja sisällysluettelon on kerrottava se.

<!-- S16 -->
Ja tässä on juju.
Jos haluat tilaa tuhannelle merkinnälle
sisällysluettelossa,
sinun on varattava ne sivut
ennen kuin kirjoitat yhtäkään reseptiä.

<!-- S17 -->
Siinä vertaus.
Nyt siihen, mitä levyllä oikeasti on.

<!-- S18 -->
Levy ei tiedä mitään tiedostoista,
kansioista tai nimistä.
Se tarjoaa vain pitkän rivin
numeroituja paikkoja, joita kutsutaan sektoreiksi.

<!-- S19 -->
Kiintolevyllä
data on pyörivillä kiekoilla.
SSD säilyttää sen flash-muistissa.
Kummassakin tapauksessa tietokone pyytää aina vain
sektoria sen numeron perusteella,
ja levy selvittää itse, missä se on.

<!-- S20 -->
Sektori on pieni.
Yleensä 512 tavua,
tai 4 096
uudemmissa levyissä.

<!-- S21 -->
Tiedostojärjestelmät käsittelevät yleensä
isompia paloja, joita kutsutaan lohkoiksi.
Ext4:ssä lohko on neljä kilotavua,
eli kahdeksan vanhanmallisen sektorin kokoinen.

<!-- S22 -->
Nuo numeroidut lohkot
ovat vihon sivut.
Tiedostojärjestelmä tarvitsee vielä
kaksi muuta osaa:
sisällysluettelon
ja luettelon siitä, mikä on vapaana.

<!-- S23 -->
Juuri ne alustus rakentaa.
Ja juuri sinne
ne seitsemäntoista gigatavua menivät.

<!-- S24 -->
Ext4 varaa tietueen
jokaiselle tiedostolle ja kansiolle,
joita levyllä voi olla yhtä aikaa.
Jokainen tietue on
256 tavua.
Sitä kutsutaan i-solmuksi.

<!-- S25 -->
Joskus jokainen i-solmu kertoo,
kuinka suuri tiedosto on,
milloin sitä muutettiin,
kuka saa avata sen
ja missä lohkoissa sen sisältö on.

<!-- S26 -->
Yhden teratavun levylle
ext4 valmistelee niitä noin
kuusikymmentäyksi miljoonaa.
Kaikki tyhjiä, kaikki odottavat.
Se on lähes kuusitoista gigatavua
tyhjiä tietueita.

<!-- S27 -->
Miksi kuusikymmentäyksi miljoonaa?
Ext4 tekee yksinkertaisen arvauksen:
yksi i-solmu jokaista kuuttatoista kilotavua
levytilaa kohden.
Tavallisessa tietokoneessa
suurinta osaa niistä tietueista
ei koskaan käytetä.

<!-- S28 -->
Noin yksi gigatavu lisää
menee journaaliin,
johon palaamme myöhemmin.
Loput on muuta kirjanpitoa,
muun muassa kartta, jossa on bitti lohkoa kohden
ja joka kertoo, onko lohko käytössä vai vapaana.

<!-- S29 -->
Myös se määrä on kiinteä.
Käytä kaikki tietueet
miljoonilla pikkutiedostoilla,
niin levy ilmoittaa olevansa täynnä...
vaikka tilaa on vielä gigatavuja.

<!-- S30 -->
Katsotaan siis, miten se toimii.
Luomme tiedoston nimeltä hello.txt.
Sisällä vain yksi sana: hello.
Viisi kirjainta. Viisi tavua.

<!-- S31 -->
Tiedostojärjestelmä valitsee tyhjän i-solmun.
Vaikkapa numero kolmetoista.
Sitten se etsii kartasta vapaan lohkon
ja merkitsee sen käytetyksi.

<!-- S32 -->
Se kirjoittaa viisi tavua siihen lohkoon.
Sitten se täyttää i-solmun:
pituus viisi tavua, luotu juuri nyt
ja tallennettu siihen yhteen lohkoon.

<!-- S33 -->
Ja lopuksi se lisää kansioon
yhden rivin:
nimen hello.txt
ja numeron kolmetoista.

<!-- S34 -->
Huomaa, mihin nimi päätyi.
Ei tiedostoon.
Ei i-solmuun.
Nimi on kansiossa,
joka on oikeastaan vain luettelo
nimistä ja numeroista.

<!-- S35 -->
Ja kansio on vain yksi tiedosto lisää.
Sen sisältönä
sattuu olemaan se luettelo.

<!-- S36 -->
Siksi tiedoston siirtäminen
toiseen kansioon samassa tiedostojärjestelmässä
käy hetkessä, oli se kuinka iso tahansa.
Yhdestä kansiosta lähtee rivi,
toiseen tulee yksi lisää,
ja yleensä itse sisältö
ei liiku lainkaan.

<!-- S37 -->
Viisi tavua tekstiä...
ja levyllä se vie
4 096.
Lohko on pienin pala,
jonka tiedostojärjestelmä antaa,
joten pienikin tiedosto vie kokonaisen lohkon.

<!-- S38 -->
Kun tiedosto kasvaa lohkoaan isommaksi,
tiedostojärjestelmä etsii toisen vapaan.
Ehkä ihan vierestä.
Ehkä jostain aivan muualta.
Ja i-solmu pitää kirjaa molemmista.

<!-- S39 -->
Ajan mittaan iso tiedosto voi päätyä
paloina ympäri levyä.
Kiintolevyn on hypittävä niiden välillä.
SSD selviää siitä paljon paremmin.

<!-- S40 -->
Ohjelma, joka tallensi tiedoston,
ei tiedä tästä mitään.
Se sanoi ”tallenna hello.txt”,
ja kaikki muu tapahtui pinnan alla.

<!-- S41 -->
Poista se nyt.
Nimi poistetaan kansiosta.
I-solmu merkitään vapaaksi.
Lohko palaa vapaiden luetteloon.

<!-- S42 -->
Perinteisellä kiintolevyllä
itse viisi tavua pysyvät paikallaan.
Kukaan ei koskenut niihin.
Ne säilyvät, kunnes jotain uutta
kirjoitetaan niiden päälle.

<!-- S43 -->
Siksi poistetun tiedoston
voi joskus palauttaa.
Poistaminen ei yleensä pyyhi
itse sisältöä.
Se vain merkitsee tilan vapaaksi.

<!-- S44 -->
SSD:llä asia on epävarmempi.
Tiedostojärjestelmä voi kertoa levylle,
ettei niitä lohkoja enää tarvita,
ja levy voi hävittää niiden sisällön.
Sen jälkeen tiedoston saaminen takaisin
on paljon epätodennäköisempää.

<!-- S45 -->
Tiedostojärjestelmä on siis oikeastaan kirjanpitäjä.
Tämän yhden tiedoston luominen
tarkoitti kolmen asian päivittämistä:
kansion, i-solmun
ja vapaiden lohkojen kartan.

<!-- S46 -->
Katkaise nyt virta
kesken tiedoston tallentamisen.

<!-- S47 -->
Ehkä lohko merkittiin käytetyksi,
mutta mikään i-solmu ei vielä osoita siihen.
Se tila on yksinkertaisesti hukassa.
Ärsyttävää, mutta vaaratonta.

<!-- S48 -->
Tai ehkä i-solmu osoittaa lohkoon,
jota kartta pitää yhä vapaana.
Seuraava tiedosto voidaan kirjoittaa
suoraan sen päälle.
Ja ensimmäinen tuhoutuu hiljaa.

<!-- S49 -->
Siksi ext4 pitää journaalia.
Ennen kuin se muuttaa kirjanpitoaan,
se kirjoittaa ylös, mitä aikoo tehdä.
Kaatumisen jälkeen se toistaa vain ne muutokset,
jotka se ehti kirjoittaa ylös loppuun
ja merkitä valmiiksi.
Kaikki keskeneräinen jätetään huomiotta.

<!-- S50 -->
Ja sitten on hiljaisempi ongelma.
Joskus levy muuttaa bitin
eikä kerro siitä kenellekään.

<!-- S51 -->
Ext4 suojaa omat tietueensa
tarkistussummilla,
joten se huomaa niissä olevat vauriot.
Mutta tiedostojesi sisältö?
Siihen se yksinkertaisesti luottaa.

<!-- S52 -->
Jotkin tiedostojärjestelmät tarkistavat molemmat.
Ja jotkin pitävät toista kopiota,
joten kun yksi kopio vaurioituu,
ne voivat korjata sen toisesta.
Ongelman huomaaminen ja sen korjaaminen
eivät ole sama asia.

<!-- S53 -->
Jokainen tiedostojärjestelmä tekee siis saman työn:
numeroidut lohkot, nimiluettelo
ja kartta siitä, mikä on vapaana.

<!-- S54 -->
Mutta valinnat eroavat.
Ext4 valmistelee kuusikymmentäyksi miljoonaa tietuetta
ennen kuin tallennat mitään.
Windowsin NTFS pitää tietueensa
yhdessä isossa taulukossa, joka kasvaa käytön mukana.

<!-- S55 -->
Ja Btrfs ei valmistele
kiinteää i-solmutaulukkoa etukäteen.
Se luo niitä sitä mukaa kuin tiedostoja tulee.
Ja tavallisesti se ei ylikirjoita
dataa sen alkuperäisessä paikassa.
Se kirjoittaa uuden kopion
ja vasta sitten luopuu vanhasta.

<!-- S56 -->
Oletuksena se laskee tarkistussummat myös tiedostoillesi,
joten se huomaa, jos ne ovat vaurioituneet.

<!-- S57 -->
Ja koska vanhaa kopiota
ei kirjoiteta yli,
tilannevedos voi pitää sen elossa.
Se muuttaa vastauksen
lähes jokaiseen tämän videon kysymykseen:
mitä kaatuminen tekee,
mitä poistaminen tarkoittaa
ja jopa mikä kopio on.

<!-- S58 -->
Siitä seuraava video alkaa.

<!-- S59 -->
Joten tässä sinulle kysymys.
Pitäisikö tiedostojärjestelmän vain tallentaa tiedostosi,
vai pitäisikö sen myös suojata niitä?
Kerro kommenteissa.
