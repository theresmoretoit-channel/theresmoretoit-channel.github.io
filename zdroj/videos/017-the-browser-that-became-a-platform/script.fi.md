# Internet Explorer 6 — selain, josta tuli alusta

<!-- S01 -->
Kuvittele olevasi web-kehittäjä
kaksituhattaluvun alussa.

Olet kirjoittanut
täysin järkevän verkkosivun.

<!-- S02 -->
Se toimii Netscapessa.

Se toimii Operassa.

Se toimii uudessa Firefoxissa.

Ja sitten avaat sen
Internet Explorerissa.

Kaikki on rikki.

<!-- S03 -->
Asettelu on väärin.

Painikkeet ovat siirtyneet.

PNG-kuvat näyttävät kamalilta.

Ja jotenkin
yhden rivinvaihdon lisääminen HTML:ään
on luonut kolmen pikselin raon.

<!-- S04 -->
Tervetuloa web-kehitykseen
Internet Explorer kutosen aikakaudella.

Mutta tässä on se kiinnostava osa.

Internet Explorer kutonen
ei ollut vain kamala selain.

<!-- S05 -->
Microsoft yritti ratkaista ongelmia,
joita webillä oikeasti oli.

Heillä oli vain yksi valtava etu
kaikkiin muihin nähden.

Windows.

<!-- S06 -->
Ja lopulta se etu
antoi Microsoftille mahdollisuuden muuttaa selain
joksikin paljon suuremmaksi
kuin pelkkä selain.

<!-- S07 -->
Yhdeksänkymmentäluvun puolivälissä
webiä hallitsi
Netscape Navigator.

Microsoft ei ollut siitä iloinen.

<!-- S08 -->
Niinpä Internet Explorer
niputettiin Windowsin mukaan
ja annettiin ilmaiseksi.

Ostit Windows-koneen.

Internet Explorer oli jo siellä.

Ei ladattavaa.

Ei maksettavaa.

<!-- S09 -->
Ja mikä tärkeintä,
Microsoft hallitsi
käyttöjärjestelmää.

Kaksituhattaluvun alkuun mennessä
Internet Explorerilla oli
yli yhdeksänkymmentä prosenttia
selainmarkkinoista.

<!-- S10 -->
Internet Explorer kutonen saapui
vuonna 2001
yhdessä Windows XP:n kanssa.

Ja hetken näytti siltä,
että Microsoft oli yksinkertaisesti voittanut
selainsodat.

<!-- S11 -->
Microsoftilla oli ongelma.

Web oli äärimmäisen rajoittunut.

HTML osasi näyttää dokumentteja.

CSS osasi tyylitellä niitä.

JavaScript osasi tehdä niistä vuorovaikutteisia.

<!-- S12 -->
Mutta siinä se suunnilleen oli.

Mikä tahansa monimutkaisempi
törmäsi suoraan
selaimen rajoihin.

<!-- S13 -->
Entä jos halusit skannata asiakirjan?

Tai viestiä älykortin kanssa?

Tai puhua jollekin
Windows-laitteelle?

<!-- S14 -->
Selain ei oikeastaan
osannut niitä asioita.

Joten Microsoft keksi ratkaisun.

ActiveX.

<!-- S15 -->
Perusajatus oli yksinkertainen.

Miksi rajoittaa web-sovellus
siihen, mitä selain osaa?

Annetaan sen vain käyttää
natiiveja Windows-komponentteja.

<!-- S16 -->
Ja yhtäkkiä verkkosivu
osasi asioita,
joista tavallinen HTML
ei osannut edes uneksia.

<!-- S17 -->
Nykyään ActiveX kuulostaa kauhistuttavalta.

Ja hyvästä syystä.

ActiveX-komponentti ylsi
tiedostoihin, sovelluksiin,
laitteistoon
ja käyttöjärjestelmään.

<!-- S18 -->
Nykyisestä tietoturvanäkökulmasta
se kuulostaa täysin hullulta.

Mutta kaksituhattaluvun alussa
se oli yritysten sovelluksille
täysin järkevää.

<!-- S19 -->
Yritykset eivät halunneet
nättiä dokumenttikatselinta.

Ne halusivat sovelluksia.

Ne halusivat verkkosivuja,
jotka käyttäytyisivät
melkein kuin työpöytäohjelmat.

<!-- S20 -->
Ja Microsoft antoi niille täsmälleen sen.

Jopa Windows Update itse
nojasi alun perin ActiveXiin
tutkiakseen järjestelmää
ja selvittääkseen, mitä päivityksiä
tarvittiin.

<!-- S21 -->
ActiveX ei siis ollut vain
typerä virhe.

Se oli varhainen yritys
muuttaa selain
sovellusalustaksi.

<!-- S22 -->
Ja siinä mielessä Microsoft
oli itse asiassa aikaansa edellä.

Ongelma oli se, kuinka paljon valtaa
he sille alustalle antoivat.

<!-- S23 -->
ActiveX ei ollut
Microsoftin ainoa laajennus.

Oli VBScript.

Oli DHTML.

Oli jopa CSS expression.

Kyllä.

<!-- S24 -->
Internet Explorer osasi suorittaa
JavaScriptiä suoraan CSS:n sisällä.

Saatoit tehdä jotain tällaista.

<!-- S25 -->
Se oli naurettavaa.

Se oli joskus myös
yllättävän hyödyllistä.

Eikä mikään siitä toiminut
taatusti missään muualla.

<!-- S26 -->
Microsoft ei vain
toteuttanut webiä.

Microsoft laajensi webiä
omaan suuntaansa.

Ja yhdeksänkymmenen prosentin
markkinaosuudella
sillä oli tarpeeksi valtaa
saada se toimimaan.

<!-- S27 -->
Yksi kuuluisimmista esimerkeistä
oli CSS:n laatikkomalli.

Standardimalli sanoi,
että jos elementti
oli kaksisataa pikseliä leveä,
kahdenkymmenen pikselin sisäreunuksella
ja viiden pikselin reunaviivalla,

<!-- S28 -->
niin kokonaisleveys
oli kaksisataaviisikymmentä pikseliä.

<!-- S29 -->
Internet Explorerin vanhemmat versiot
lukivat sen toisin.

Quirks-tilassa ilmoitettu leveys
saattoi sisältää sisäreunuksen
ja reunaviivan.

<!-- S30 -->
Se ei ollut välttämättä
hullu tapa ajatella leveyttä.

Itse asiassa nykyään saamme selaimet usein
toimimaan juuri näin ihan tarkoituksella.

Sitä kutsutaan border box -mitoitukseksi.

<!-- S31 -->
Todellinen ongelma oli,
että eri selaimet
käyttäytyivät eri tavoin.

Ja se tarkoitti,
että kehittäjän piti ottaa erot huomioon.

Ja nähdä paljon vaivaa.

<!-- S32 -->
Oli jokin nimeltä hasLayout.

Se ei ollut tavallinen CSS-ominaisuus.

Se ei ollut osa standardia.

Mutta se ratkaisi,
miten Internet Explorer
latoi elementit.

<!-- S33 -->
Ja joskus rikkinäisen asettelun
saattoi salaperäisesti korjata
lisäämällä yhden rivin.

zoom: 1

Miksi?

Koska zoom: 1 saattoi laukaista
sisäisen hasLayout-mekanismin.

<!-- S34 -->
Oli ongelmia
PNG-läpinäkyvyyden kanssa.

Oli ongelmia select-elementtien kanssa,
jotka ilmestyivät absoluuttisesti
sijoitettujen ponnahdusikkunoiden päälle
riippumatta siitä, kuinka korkealle
z-indexin asetti.

<!-- S35 -->
Web-kehityksessä ei ollut kyse vain
oman suunnitelman toteuttamisesta.

Siinä oli kyse tietyn selainmoottorin
bugien opettelusta.

<!-- S36 -->
Tässä toinen ihana esimerkki.

Tyhjämerkit.

Eikä tämä ollut edes
Internet Explorerin vika.

Saatoit laittaa kaksi kuvaa
aivan vierekkäin
merkkaukseen
ilman mitään tagien välissä
ja saada yhden lopputuloksen.

<!-- S37 -->
Sitten joku muotoili HTML:n siististi
ja laittoi jokaisen tagin omalle rivilleen.

Ja yhtäkkiä kuvien välissä
oli muutaman pikselin rako.

Rivinvaihdosta tuli merkitsevä.

<!-- S38 -->
Koodinmuotoilijasi
saattoi kirjaimellisesti rikkoa verkkosivusi.

Ja jos käytit
vanhaa Visual Studion versiota,
se saattoi iloisesti muotoilla
HTML:si puolestasi.

Kiitos, Microsoft.

<!-- S39 -->
Kehittäjille kertyi
kokonainen työkalupakki kiertoteitä.

Ehdolliset kommentit.

<!-- S40 -->
Ja joskus täysin
omituisen näköistä HTML:ää,
jonka ainoa tarkoitus oli saada
Internet Explorer käyttäytymään.

<!-- S41 -->
Et kirjoittanut rumaa koodia siksi,
että olisit ollut huono ohjelmoija.

Kirjoitit rumaa koodia siksi,
että selain pakotti sinut siihen.

<!-- S42 -->
Internet Explorer myös kaatui
näyttävästi ja vei usein mukanaan
jokaisen avoimen ikkunan.

<!-- S43 -->
Siitä syntyi mainio tapa
pitää hauskaa toimistolla.

Hei, katso tätä linkkiä.

Ja kaksikymmentä Internet Explorer -ikkunaa
katoaa.

<!-- S44 -->
Tämä oli web
ennen kuin selaimet eristettiin.

Nykyselain sanoo näin.

Tämä sivusto ei ole luotettu.

Eristän sen.

<!-- S45 -->
Internet Explorer kutonen
tuntui joskus enemmän tältä.

Olet verkkosivu?

Toki.

Tässä on avaimet rakennukseen.

<!-- S46 -->
Miksi kehittäjät
oikeasti käyttivät näitä kiertoteitä?

Koska heidän oli pakko.

<!-- S47 -->
Kuvittele yritys,
jossa on viisisataa työntekijää.

Joka koneessa on Windows XP.

Joka koneessa on Internet Explorer.

<!-- S48 -->
Kehittäjällä on kaksi vaihtoehtoa.

Vaihtoehto yksi.

Rakenna Internet Explorerille,
joka kaikilla jo on.

<!-- S49 -->
Vaihtoehto kaksi.

Rakenna joka selaimelle,
testaa kaikki kaikkialla
ja selitä IT-osastolle,
miksi kaikki tarvitsevat toisen selaimen.

Vastaus oli yleensä ilmeinen.

<!-- S50 -->
He eivät valinneet
Microsoftin teknologiaa siksi,
että olisivat rakastaneet Microsoftia.

He valitsivat sen, mikä ratkaisi
asiakkaan ongelman.

Ja joskus ActiveX
oli paras saatavilla oleva työkalu.

<!-- S51 -->
Ja lopulta joku sai tarpeekseen.

JavaScript-kirjastot alkoivat
piilottaa selainerot.

Yksi tärkeimmistä
oli jQuery.

<!-- S52 -->
Sen sijaan että olisit kirjoittanut
selainkohtaista tapahtumankäsittelyä,
saatoit kirjoittaa yhden rivin,
joka toimi kaikkialla.

<!-- S53 -->
Sen sijaan että olisit käsitellyt käsin
eri AJAX-toteutuksia,
saatoit käyttää yhteistä abstraktiota.

<!-- S54 -->
jQuery ei saanut
Internet Exploreria katoamaan.

Mutta se teki paljon helpommaksi
teeskennellä, ettei sitä ollut.

Ja sen ajan web-kehittäjille
se oli mahtava juttu.

<!-- S55 -->
Firefox ilmestyi.

Opera jatkoi kehitystään.

Safari saapui.

Ja lopulta Google julkaisi Chromen.

<!-- S56 -->
Selainsodat olivat palanneet,
ja tällä kertaa
kilpailu oli erilaista.

JavaScript-moottoreista
tuli dramaattisesti parempia.

HTML5 saapui.

<!-- S57 -->
Selain itse alkoi oppia
kaiken sen, mihin kehittäjät
olivat aiemmin tarvinneet liitännäisiä.

<!-- S58 -->
Video.

Ääni.

Canvas.

SVG.

WebGL.

WebSocketit.

Ja lopulta WebRTC.

Webistä oli tulossa
sovellusalusta.

<!-- S59 -->
Mikä oli täsmälleen se,
mitä Microsoft oli yrittänyt
saavuttaa ActiveXilla.

Mutta nyt se tapahtui
avoimien standardien kautta.

<!-- S60 -->
Microsoft yritti vielä kerran.

Silverlight antoi kehittäjien rakentaa
rikkaita selainsovelluksia
C#:lla ja .NETillä.

Se pyöritti jopa
Netflixin varhaista suoratoistoa.

<!-- S61 -->
Mutta web ei halunnut liitännäisiä ikuisesti.

Apple kieltäytyi tukemasta Flashia
iPhonessa.

Ja yhtäkkiä tulevaisuus ei ollut tämä.

Selain plus liitännäinen.

Se oli tämä.

Selain itse.

<!-- S62 -->
Silverlight katosi.

Flash katosi.

ActiveX katosi.

Ja Internet Explorer
katosi lopulta myös.

<!-- S63 -->
Ja tässä kohtaa
tarina muuttuu kiinnostavaksi.

Koska Microsoft
ei ollut täysin väärässä.

He olivat ennustaneet oikein,
että selaimesta tulisi
sovellusalusta.

<!-- S64 -->
He vain yrittivät päästä sinne
suljettujen teknologioiden avulla.

Web pääsi samaan määränpäähän
standardien kautta.

<!-- S65 -->
Selain voitti.

Mutta se voitti muuttumalla
joksikin paljon voimakkaammaksi
kuin vuoden 2001
selain.

<!-- S66 -->
Oliko Microsoft siis konna?

Ei oikeastaan.

Ja juuri se tekee
tarinasta kiinnostavamman.

<!-- S67 -->
Microsoftilla oli loistavia insinöörejä.

Sillä oli valtavat resurssit.

Ja se rakensi monia teknologioita,
jotka olivat aidosti aikaansa edellä.

<!-- S68 -->
Mutta Microsoftilla oli myös
ylivoimainen markkina-asema.

Ja se loi
vaarallisen kannustimen.

<!-- S69 -->
Jos melkein kaikki
käyttävät sinun selaintasi,
miksi odottaa standardeja?

Miksi et vain toteuttaisi
omaa ratkaisuasi?

Hetken se toimi.

Kunnes muu web sai Microsoftin kiinni.

<!-- S70 -->
Nykyään Internet Explorer on poissa.

Vanhat selainsodat
tuntuvat muinaishistorialta.

Mutta katso
nykyisiä selainmarkkinoita.

Chrome.

Edge.

Opera.

Brave.

Vivaldi.

<!-- S71 -->
Ja monet muut
perustuvat Chromiumiin.

Eri tuotteita.

Usein sama
taustalla oleva selainmoottori.

<!-- S72 -->
Ehkä olemme siis vaihtaneet tämän.

Yhden selaimen, jota kaikkien oli tuettava.

Tähän.

Yhteen moottoriin, jonka päälle kaikki rakentavat.

Kuulostaako tutulta?

<!-- S73 -->
Koska hallitseva selainmoottori
ei päätä vain siitä,
miten sivustot näytetään.

<!-- S74 -->
Se vaikuttaa siihen, mitä kehittäjät rakentavat.

Mistä teknologioista tulee suosittuja.

Ja viime kädessä siihen,
millaiseksi web itse muuttuu.

<!-- S75 -->
On kuitenkin
yksi hyvin tärkeä ero.

Nykyinen web on rakennettu
avoimien standardien ympärille.

Firefoxilla on yhä oma moottorinsa.

Safarilla on WebKit.

Chromium on avointa lähdekoodia.

<!-- S76 -->
Ja nykyselaimet
päivittyvät automaattisesti.

Emme ole lähelläkään
vuoden 2003
tilannetta.

<!-- S77 -->
Mutta perus kysymys jää.

Kuinka paljon vaikutusvaltaa
yhdellä yrityksellä pitäisi olla
alustaan,
jota melkein kaikki käyttävät?

Se on se kysymys,
joka ei koskaan oikeasti kadonnut.

<!-- S78 -->
Oliko Internet Explorer kutonen siis kamala?

Kyllä.

Joskus näyttävän kamala.

<!-- S79 -->
Mutta se ei ole koko tarina.

Se oli myös aikansa tuote.

<!-- S80 -->
Ongelma oli se,
että Microsoft oli voittanut
selainsodat niin täydellisesti,
että se saattoi määritellä säännöt.

<!-- S81 -->
Ja web-kehittäjät maksoivat hinnan.

He opettelivat
hasLayoutin mysteerit.

He huomasivat, että zoom: 1
saattoi taianomaisesti korjata asioita.

Ja he rukoilivat.

<!-- S82 -->
Ja lopulta Internet Explorerista
tuli se, mitä se oli luonut
kaksikymmentä vuotta.

Legacy-alusta,
jota kukaan ei enää
halunnut tukea.

<!-- S83 -->
Web ei hylännyt
Microsoftin visiota.

Se rakensi siitä vain
paremman version.

Ja jos se aikakausi opettaa
meille yhden asian,
niin tämän.

<!-- S84 -->
Teknologiasta ei tule standardia
vain siksi, että se on hyvä.

<!-- S85 -->
Joskus siitä tulee standardi siksi,
että yhdellä yrityksellä on tarpeeksi valtaa
saada kaikki käyttämään sitä.

<!-- S86 -->
Ja joskus,
kaksikymmentä vuotta myöhemmin...
tajuamme tehneemme sen taas.
