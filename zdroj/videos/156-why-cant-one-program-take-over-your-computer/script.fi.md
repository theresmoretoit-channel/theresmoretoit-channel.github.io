<!-- S01 -->
19. heinäkuuta 2024
tietoturvayhtiö CrowdStrike
lähetti tavallisen päivityksen.

<!-- S02 -->
Ei uusi ohjelma.
Vain pieni asetustiedosto.

<!-- S03 -->
Muutamassa tunnissa 8,5 miljoonaa
Windows-tietokonetta oli pysähtynyt
siniseen ruutuun.

<!-- S04 -->
Lentoyhtiöt peruivat lentoja.
Sairaalat peruivat leikkauksia.
Yksi uutiskanava katosi lähetyksestä.

<!-- S05 -->
Ja virhe kaiken takana
oli ihan tavallinen.
Ohjelma odotti 20 tietokenttää.
Päivitys antoi sille 21.

<!-- S06 -->
Pelisi ja sovelluksesi tekevät
tuollaisia virheitä koko ajan.
Kun niin käy, peli sulkeutuu,
ja sinä käynnistät sen uudelleen.

<!-- S07 -->
Samanlainen bugi.
Yksi sulkee ikkunan.
Toinen pysäyttää
8,5 miljoonaa konetta.

<!-- S08 -->
Ero ei ole virheessä.
Vaan siinä, missä koodi oli käynnissä.

<!-- S09 -->
Miksi siis yksi ohjelma ei voi
kaapata tietokonettasi...
ja miksi tämä pystyi?

<!-- S10 -->
Aina ei ole ollut näin.

<!-- S11 -->
1980-luvun DOS-PC:ssä
mikään suorittimessa ei pysäyttänyt ohjelmaa.
Se pystyi kirjoittamaan mihin tahansa muistiin
ja puhumaan suoraan laitteistolle.

<!-- S12 -->
Riitti, että yksi ohjelma kirjoitti
jonnekin, minne ei pitänyt,
ja se saattoi kirjoittaa käyttöjärjestelmän yli,
ja koko kone jumiutui.

<!-- S13 -->
Ratkaisu oli lakata luottamasta ohjelmiin
ja siirtää epäluulo
suorittimen tehtäväksi.

<!-- S14 -->
Vuonna 1982 Intelin 80286-suoritin
toi suojatun tilan,
jossa oli neljä käyttöoikeustasoa.

<!-- S15 -->
Ne piirretään yleensä
neljäksi renkaaksi, sisäkkäin.

<!-- S16 -->
Rengas 0 on keskellä.
Rengas 3 on uloimpana.

<!-- S17 -->
Ja numerointi kulkee takaperin.
Mitä pienempi numero,
sitä enemmän koodi saa tehdä.

<!-- S18 -->
Rengas 0 kuuluu ytimelle,
käyttöjärjestelmän sydämelle.
Se jakaa muistia,
päättää, mikä ohjelma ajetaan seuraavaksi,
ja puhuu laitteistolle.

<!-- S19 -->
Renkaassa 3 toimivat selaimesi,
pelisi ja tekstieditorisi.
Tätä kutsutaan käyttäjätilaksi.

<!-- S19b -->
Windows, macOS ja Linux
jakavat työn kaikki näin.
Ydin renkaassa 0,
sovelluksesi renkaassa 3.

<!-- S19c -->
Puhelimet ja Applen uudemmat Macit
käyttävät sen sijaan ARM-siruja.
Siellä tasoja kutsutaan nimellä exception level.
Eri nimi, sama jako:
yksi ytimelle, yksi sovelluksillesi.

<!-- S20 -->
Suoritin tietää aina,
missä renkaassa se on käynnissä.
Ja se tarkistaa.

<!-- S21 -->
Jotkin käskyt toimivat vain renkaassa 0.
Esimerkiksi keskeytysten poistaminen käytöstä
tai sen muuttaminen, miten muisti kartoitetaan.

<!-- S22 -->
Kun renkaan 3 ohjelma yrittää sellaista,
suoritin kieltäytyy.
Se nostaa poikkeuksen
ja antaa ohjat ytimelle,
joka yleensä lopettaa ohjelman.

<!-- S23 -->
Muistia kohdellaan samoin.
Jokainen muistisivu on merkitty
joko user- tai supervisor-sivuksi.

<!-- S24 -->
Renkaan 3 ohjelma,
joka koskee supervisor-sivuun,
ei saa dataa.
Se pysäytetään.

<!-- S25 -->
Selaimesi ja pelisi
toimivat molemmat renkaassa 3.
Ne pitää erillään se,
että kumpikin saa oman muistikarttansa.
Toisen ohjelman muistia
ei yksinkertaisesti ole siinä.

<!-- S26 -->
Kun peli siis kaatuu,
vahinko jää pelin sisälle.
Ydin siivoaa jäljet.
Kaikki muu jatkaa toimintaansa.

<!-- S27 -->
Katso nyt taas CrowdStrikea.
Sen ajuri toimi renkaassa 0,
aivan ytimen vieressä.

<!-- S28 -->
Mikään renkaan 0 yläpuolella
ei pysty nappaamaan sellaista virhettä.

<!-- S29 -->
Joten Windows teki ainoan turvallisen asian, mitä oli jäljellä.
Se pysäytti koko koneen, tarkoituksella,
sen sijaan että olisi jatkanut muistilla,
johon se ei enää voinut luottaa.

<!-- S30 -->
Sitä sininen ruutu on.

<!-- S31 -->
Ja koska ajuri käynnistyi
joka kerta, kun Windows käynnistyi,
jokainen uudelleenkäynnistys toi kaatumisen takaisin.

<!-- S32 -->
Mutta tästä herää kysymys.
Jos selaimesi ei saa koskea laitteistoon,
miten se ylipäätään tallentaa tiedoston
tai lähettää mitään verkon yli?

<!-- S33 -->
Se pyytää.

<!-- S34 -->
Ohjelma laittaa pyyntönsä
suorittimen rekistereihin.
Mikä tiedosto. Minne datan pitää mennä.
Kuinka paljon.

<!-- S35 -->
Sitten se suorittaa yhden erityisen käskyn.
Nykyaikaisessa PC:ssä sen nimi on SYSCALL.

<!-- S36 -->
Sillä hetkellä suoritin vaihtaa
renkaasta 3 renkaaseen 0...

<!-- S37 -->
mutta se ei hyppää
minne ohjelma haluaa.
Se hyppää yhteen sisääntulokohtaan,
jonka ydin on valinnut etukäteen.

<!-- S38 -->
Ydin tarkistaa pyynnön,
tekee työn
ja palaa renkaaseen 3.
Ohjelma ei koskaan itse koskenut levyyn.

<!-- S39 -->
Tämä on järjestelmäkutsu,
ja niitä tapahtuu koko ajan.

<!-- S40 -->
Laskimme ne kannettavalla.
Ohjelma, joka ei tee yhtään mitään,
tekee silti 30.

<!-- S41 -->
Firefox teki käynnistyessään
ja ladatessaan yhden Wikipedia-sivun
noin 670 000
20 sekunnissa...
vaikka laskentamme vielä hidasti sitä.

<!-- S42 -->
Jokainen niistä
on matka muurin läpi ja takaisin.

<!-- S43 -->
Jäljelle jää jotain kummallista.
Neljä rengasta,
ja tarvitsimme vain kaksi.

<!-- S44 -->
Mitä tapahtui renkaille 1 ja 2?

<!-- S45 -->
Renkaiden idea on vanhempi kuin PC.
Multicsissa, käyttöjärjestelmässä
1960-luvun lopulta,
niitä oli kahdeksan.

<!-- S46 -->
Ajatuksena olivat luottamuksen kerrokset.
Järjestelmän sydän keskellä,
vähemmän luotetut palvelut sen ympärillä
ja ohjelmat uloimpana.

<!-- S46b -->
Intel piirsi saman kuvan.
Renkaat 1 ja 2 oli tarkoitettu
välissä oleville kerroksille,
kuten ajureille ja järjestelmäpalveluille.
Luotetumpia kuin sovelluksesi,
vähemmän kuin ydin.

<!-- S47 -->
Kaksi asiaa tuli tielle.

<!-- S48 -->
Ensinnäkin Unixin ja Windows NT:n kaltaiset järjestelmät
suunniteltiin toimimaan
monenlaisilla suorittimilla.

<!-- S49 -->
Ja ainoa jako,
jonka jokainen suoritin tarjosi,
oli kaksi tasoa.
Yksi ytimelle,
yksi kaikelle muulle.

<!-- S50 -->
Toiseksi itse x86-suoritin.
Kun se kartoittaa muistia,
jokainen sivu tuntee vain kaksi tilaa.
User tai supervisor.

<!-- S51 -->
Renkaat 1 ja 2 lasketaan supervisor-tasoksi.
Joten renkaan 1 ajuri
pystyisi silti koskemaan ytimen muistiin.
Ylimääräinen rengas ei suojaisi paljon.

<!-- S51b -->
Muutama järjestelmä käytti niitä silti.
OS/2 päästi jotkin ohjelmat renkaaseen 2,
jotta ne voisivat puhua suoraan laitteistolle.

<!-- S51c -->
Ja ennen kuin suorittimissa oli tukea
virtuaalikoneiden ajamiseen,
Xen ja VirtualBox siirsivät vierasjärjestelmän ytimen
renkaaseen 1,
jotta alla oleva järjestelmä
sai pitää renkaan 0 itsellään.

<!-- S52 -->
Vuonna 2023 Intel ehdotti,
että renkaat 1 ja 2 poistettaisiin kokonaan.

<!-- S53 -->
Joulukuussa 2024 Intel luopui suunnitelmasta.
Ne ovat yhä suorittimessasi.
Lähes mikään ei käytä niitä.

<!-- S54 -->
Tähän asti tämä kuulostaa rauhoittavalta.
Säännöt ovat laitteistossa,
ja laitteisto tarkistaa jokaisen käytön.

<!-- S55 -->
Vuonna 2017 kolme tutkijaryhmää,
toisistaan riippumatta,
löysi reitin tuon muurin läpi.

<!-- S56 -->
He nimesivät sen Meltdowniksi.
Ja jotta pysyt mukana,
sinun pitää tuntea yksi temppu,
jota nykyaikaiset suorittimet käyttävät.

<!-- S57 -->
Suoritin ei odota,
että yksi käsky on valmis,
ennen kuin aloittaa seuraavan.
Se juoksee edelle,
käskyihin, joita se luultavasti tarvitsee.

<!-- S58 -->
Jos se arvasi väärin,
se heittää tulokset pois,
kuin mitään ei olisi tapahtunut.

<!-- S59 -->
Tässä on vika.
Haavoittuvilla Intelin siruilla
renkaan 3 ohjelma saattoi pyytää
tavun ytimen muistista...

<!-- S60 -->
ja suoritin haki sen
ja välitti sen seuraaville käskyille
ennen kuin oli tarkistanut loppuun,
oliko se sallittua.

<!-- S61 -->
Tarkistus kyllä epäonnistui.
Tulos heitettiin pois.

<!-- S62 -->
Mutta ne seuraavat käskyt
olivat jo käyttäneet salaista tavua
vetääkseen yhden palan
ohjelman omasta muistista
suorittimen välimuistiin.

<!-- S63 -->
Eikä välimuisti unohda
vain siksi, että tulos peruttiin.

<!-- S64 -->
Joten ohjelma mittaa,
kuinka nopeasti kukin pala sen muistista vastaa.
Se, joka vastaa nopeasti,
paljastaa salaisen tavun.

<!-- S65 -->
Tavu kerrallaan
tavallinen ohjelma pystyi lukemaan
ytimen muistia
ja mitä tahansa salaisuuksia siellä oli.
Salasanat ja salausavaimet mukaan lukien.

<!-- S66 -->
Meltdown koski Intelin suorittimia
vuodesta 1995 alkaen.

<!-- S67 -->
Se julkistettiin
3. tammikuuta 2018.

<!-- S68 -->
Korjaus ei voinut muuttaa piitä.
Joten käyttöjärjestelmät muuttivat kartan.

<!-- S69 -->
Kun ohjelmasi on käynnissä,
ytimen muisti on nyt poistettu
sen kartalta lähes kokonaan.
Siellä ei ole mitään haettavaa.

<!-- S70 -->
Mutta muista järjestelmäkutsut.
Jokaisella matkalla muurin läpi
pitää nyt myös vaihtaa karttaa.

<!-- S71 -->
Red Hat mittasi Meltdownin
ja siihen liittyvän Spectre-haavoittuvuuden korjaukset.
Alle 1 % joissakin töissä...
jopa 19 % kuormitetuissa tietokannoissa.

<!-- S72 -->
Sääntö oli oikea koko ajan.
Suoritin vain tarkisti sen liian myöhään.

<!-- S73 -->
Mikä tuo meidät takaisin CrowdStrikeen
ja vaikeampaan kysymykseen.

<!-- S74 -->
Miksi tietoturvaohjelma
ylipäätään oli renkaassa 0?

<!-- S75 -->
Koska sieltä se näkee kaiken.
Se käynnistyy ennen muita ohjelmia.
Ja järjestelmänvalvojan oikeuksilla toimivan haittaohjelman
on vaikeampi sammuttaa se.

<!-- S76 -->
Microsoftin oma lista
päättyy varoitukseen.
Ytimen ajurit tarjoavat tämän vikasietoisuuden kustannuksella.

<!-- S77 -->
Katkon jälkeen
Microsoft alkoi rakentaa tapaa,
jolla virustorjuntaohjelmat
voisivat toimia ytimen ulkopuolella.

<!-- S78 -->
Syksyllä 2026
se on yhä vain Windowsin testiversioissa.
Eikä ydintä ole suljettu
tietoturvayhtiöiltä.

<!-- S79 -->
Pelisi ovat saman dilemman edessä.

<!-- S80 -->
Huijausohjelmat, jotka toimivat ytimessä,
ovat näkymättömiä huijauksenestolle,
joka toimii renkaassa 3.

<!-- S81 -->
Joten huijauksenestokin muutti sinne.
Riotin Vanguard, jota Valorant käyttää,
asentaa ajurin renkaaseen 0.
Useimmissa PC:issä se latautuu jo Windowsin käynnistyessä...
vaikka et koskaan avaisi peliä.

<!-- S82 -->
Se ei tee siitä viallista.
Mutta se on samassa paikassa
kuin CrowdStriken ajuri oli,
jossa yksi virhe pysäyttää koko koneen.

<!-- S83 -->
Miksi siis yksi ohjelma ei voi
kaapata tietokonettasi?

<!-- S84 -->
Koska suoritin pitää
lähes jokaisen ohjelman poissa keskeltä
ja tarkistaa ne joka kerta, kun ne koputtavat.

<!-- S85 -->
Mutta suoritin ei voi päättää,
kuka päästetään sisään.
Sen päättävät ihmiset...
joka kerta, kun he asentavat ajurin.

<!-- S86 -->
Joten tässä kysymys kommentteihin.
Kenen pitäisi päättää, mitkä ohjelmat
pääsevät renkaaseen 0:
sinun, Microsoftin
vai niiden yritysten, jotka niitä tekevät?
