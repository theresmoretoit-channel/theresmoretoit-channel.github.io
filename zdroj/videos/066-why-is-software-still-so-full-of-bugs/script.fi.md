<!-- S01 -->
Muutaman päivän välein taas yksi vakava bugi
nousee uutisiin.
Bugi, jonka avulla joku ohittaa kirjautumisen.
Bugi, joka vuotaa yksityisiä tietoja.
Bugi, joka luovuttaa tietokoneesi hyökkääjälle.

<!-- S02 -->
Joskus se on Windows. Joskus Linux.
Selain, tietokanta, pilvipalvelu...
tai pieni kirjasto,
josta miljoonat kehittäjät ovat riippuvaisia.

<!-- S03 -->
Ja reaktio on lähes aina sama.
Miten ohjelmoijat missasivat tämän?

<!-- S04 -->
He ovat ammattilaisia.
Heillä on koodikatselmoinnit, automaattiset testit,
tietoturva-auditoinnit, fuzzausta...
ja silti bugeja tulee koko ajan lisää.

<!-- S05 -->
Onko siis edes mahdollista
kirjoittaa monimutkaista ohjelmistoa ilman bugeja?

<!-- S06 -->
Aloitetaan luvusta.
Kuvittele ohjelma, jossa on vain sata asetusta,
kukin joko päällä tai pois.

<!-- S07 -->
Sata yksinkertaista kyllä-tai-ei-päätöstä.
Montako yhdistelmää se on?

<!-- S08 -->
Kaksi potenssiin sata.
Se on suunnilleen miljoona biljoonaa biljoonaa.

<!-- S09 -->
Kuvittele nyt, että voisit testata
miljardi yhdistelmää joka sekunti.
Ja että aloitit alkuräjähdyksestä.

<!-- S10 -->
Tähän päivään mennessä olisit testannut
noin yhden yhdistelmän kolmesta tuhannesta.

<!-- S11 -->
Ja sata kytkintä ei ole mitään.
Oikeassa ohjelmassa niitä on miljoonia.
Joten "testataan vain kaikki"
ei ole kallista. Se on mahdotonta.

<!-- S12 -->
Eivätkä nuo kytkimet ole mitään eksoottista.
Ota yksi yksinkertaisimmista asioista,
joita ohjelma koskaan tekee.
Käyttäjä pyytää omaa tiliään sen numerolla.
Me löydämme sen tietokannasta.
Ja lähetämme sen takaisin.

<!-- S13 -->
Mutta entä jos käyttäjää ei ole olemassa?
Entä jos joku lähettää tekstiä numeron sijaan?
Tai negatiivisen luvun? Tai valtavan?

<!-- S14 -->
Entä jos tällä henkilöllä ei ole lupaa nähdä sitä?
Entä jos joku poistaa tilin
juuri sillä hetkellä, kun lataamme sitä?
Entä jos sama pyyntö saapuu kahdesti?

<!-- S15 -->
Jokainen näistä kysymyksistä on yksinkertainen.
Ongelma on se, miten ne yhdistyvät.
Jokainen on taas yksi kytkin.

<!-- S15b -->
Muuten, jos pidät tällaisista
videoista, voit tilata kanavan.

Se auttaa kanavaa todella paljon.

<!-- S16 -->
Eikä tietokone selvitä niitä puolestamme.
Se tekee täsmälleen niin kuin käskemme.
Ei sitä, mitä tarkoitimme.

<!-- S17 -->
Siksi keksimme ohjelmointikielet.
Niiden avulla voimme kuvata monimutkaisia asioita
ajattelematta jokaista yksityiskohtaa.

<!-- S18 -->
Mutta jotkin niistä huolehtivat vähemmästä
kuin toivoisit.
Ota C. Se on nopea, se on yksinkertainen,
ja se antaa sinulle valtavan hallinnan muistiin.

<!-- S19 -->
Joten voit kirjoittaa tämän.
Varaamme tilaa kuudelletoista merkille.
Sitten sanomme: kopioi syöte tähän.

<!-- S20 -->
Entä jos syöte on
viisisataa merkkiä pitkä?
C ei kysy.
Se vain jatkaa kirjoittamista lopun ohi.

<!-- S21 -->
Ja mitä on heti näiden kuudentoista merkin jälkeen?
Usein jotain hyvin tärkeää.

<!-- S22 -->
Kun ohjelma kutsuu funktiota,
se merkitsee muistiin, minne palata,
kun funktio on valmis.
Paluuosoitteen.
Klassisessa asettelussa se sijaitsee
vähän puskurimme lopun jälkeen.

<!-- S23 -->
Niinpä hyökkääjä lähettää syötteen,
joka on juuri oikean pituinen.
Ensin omat käskynsä.
Sitten aivan lopussa uuden paluuosoitteen...
joka osoittaa takaisin noihin käskyihin.

<!-- S24 -->
Funktio päättyy.
Suoritin katsoo, minne palata...
ja hyppää suoraan hyökkääjän koodiin.

<!-- S25 -->
Nyt se suorittaa hänen ohjelmaansa,
kaikilla sinun ohjelmasi oikeuksilla.
Sitä "mielivaltaisen koodin suorittaminen" tarkoittaa.

<!-- S26 -->
Eikä suoritin tehnyt mitään väärää.
Se noudatti käskyjä.

<!-- S27 -->
Vuonna 1988 juuri tällainen virhe
päästi Morris-madon leviämään
varhaiseen internetiin.
Ja samaa temppua on käytetty
hyökkäyksissä siitä lähtien.

<!-- S28 -->
Niinpä uudemmat kielet antavat osan työstä
kääntäjälle.
Rust esimerkiksi kieltäytyy kääntämästä
monia ohjelmia, jotka voisivat käyttää muistia väärin.

<!-- S29 -->
Ohjelmoija sanoo:
mutta minä tiedän tasan, mitä teen!
Ja kääntäjä sanoo:
niin kaikki sanovat.

<!-- S30 -->
Ja on oikein olla epäluuloinen.
Microsoft ja Googlen Chrome-tiimi
ovat molemmat raportoineet,
että noin seitsemänkymmentä prosenttia
tutkimistaan tietoturvabugeista
johtuu muistiturvallisuusongelmista.

<!-- S31 -->
Mutta ohjelma voi olla täysin muistiturvallinen
ja silti täysin väärä.

<!-- S32 -->
Kuvittele, että käyttäjä kirjautuu sisään.
Hänen salasanansa tarkistetaan oikein.
Mikään ei kaadu. Muisti ei mene rikki.

<!-- S33 -->
Ja sitten ohjelma näyttää hänelle
jonkun toisen tiedot.
Koska oikeuksien tarkistus
kirjoitettiin hieman väärin.

<!-- S34 -->
Mikään kieli ei nappaa sitä itsestään.
Kieli ei tiedä,
mitä ohjelman oli tarkoitus tehdä.
Vain me tiedämme sen.

<!-- S35 -->
Palataan siis testaamiseen.
Testi voi kertoa sinulle:
tällä syötteellä sain tämän tuloksen.

<!-- S36 -->
Se ei voi kertoa sinulle:
ohjelma on oikein jokaisella syötteellä.
Ja olemme jo nähneet,
miksi emme voi kokeilla niitä kaikkia.

<!-- S37 -->
Vuonna 1970 tietojenkäsittelytieteilijä
Edsger Dijkstra tiivisti sen yhteen lauseeseen.
Testaus voi osoittaa bugien läsnäolon,
mutta ei koskaan niiden poissaoloa.

<!-- S38 -->
Hyvä on. Testaamisen sijaan siis:
miksei kirjoitettaisi ohjelmaa,
joka tarkistaa muita ohjelmia
ja todistaa, että ne ovat oikein?
Syötä sille mikä tahansa koodi, ja se kertoo,
tekeekö tuo koodi sen, mitä pitäisi.

<!-- S39 -->
Siihen kysymykseen vastattiin
jo ennen kuin ensimmäistä oikeaa tietokonetta oli rakennettu.
Vuonna 1936 Alan Turing todisti,
ettei sellaista ohjelmaa voi olla olemassa.

<!-- S40 -->
Ei niin, ettei kukaan ole vielä rakentanut sitä.
Vaan ettei sitä voi olla olemassa lainkaan.

<!-- S41 -->
Hän osoitti, ettei mikään ohjelma voi ratkaista,
jokaisen toisen ohjelman kohdalla,
pysähtyykö se koskaan.

<!-- S42 -->
Ja vuonna 1953 Henry Rice meni pidemmälle.
Sama pätee jokaiseen ei-triviaaliin kysymykseen
siitä, mitä ohjelma oikeasti tekee.

<!-- S43 -->
Onko se turvallinen? Vuotaako se tietoja?
Antaako se oikean vastauksen?
Ei ole olemassa yleistä menetelmää,
joka ratkaisisi sen jokaiselle ohjelmalle.

<!-- S44 -->
Onko bugiton ohjelmisto siis mahdotonta?
Ei aivan.
Yhden tietyn ohjelman kohdalla
voit joskus todistaa sen oikeaksi,
valtavalla vaivalla.

<!-- S45 -->
Vuonna 2009 australialainen ryhmä todisti,
että pieni käyttöjärjestelmän ydin,
nimeltään seL4,
tekee tasan sen, mitä sen määrittely sanoo.

<!-- S46 -->
Siinä oli alle kymmenentuhatta riviä koodia.
Ytimen rakentaminen kesti
noin kaksi henkilötyövuotta.
Sen oikeaksi todistaminen kesti noin kaksikymmentä.
Nykyaikaisessa verkkoselaimessa
on kymmeniä miljoonia rivejä.

<!-- S47 -->
Ja jopa siinä todistuksessa on koukku.
Se osoittaa, että ohjelma vastaa määrittelyään.
Se ei voi osoittaa, että määrittely
on se, mitä oikeasti halusimme.

<!-- S48 -->
Ja määrittelyn kirjoittavat ihmiset.
Joten kysymys palaa meille.

<!-- S49 -->
Eikä kyse ole vain omasta koodistamme.
Ohjelmoija rakentaa nykyään ohjelmistokehysten,
kirjastojen ja satojen riippuvuuksien varaan.
Jokainen kerros säästää meiltä valtavasti työtä.
Mutta jokainen kerros on jotain,
joka meidän on ymmärrettävä...
tai ainakin luotettava siihen.

<!-- S50 -->
Mikä tarkoittaa, ettei sinun tarvitse kirjoittaa bugia
saadaksesi sellaisen ohjelmistoosi.
Voit yksinkertaisesti asentaa sen.

<!-- S51 -->
Lisää sitten paine.
Kukaan ei halua täydellistä tuotetta kymmenen vuoden päästä.
He haluavat toimivan ensi kuussa.
Ja murto, jota ei koskaan tapahtunut,
on hyvin vaikea näyttää esityksessä.

<!-- S52 -->
Ja tässä on outoin osa.
Työkalumme paranevat jatkuvasti.
Turvallisemmat kielet, fuzzaus, bugipalkkiot...

<!-- S53 -->
Ja silti tunnettujen haavoittuvuuksien määrä
kasvaa yhä.
Pelkästään vuonna 2024 noin neljäkymmentätuhatta
sai virallisen numeron.

<!-- S54 -->
Osittain siksi, että kirjoitamme myös
valtavasti enemmän ohjelmistoa kuin koskaan.
Se on kuin tekisi jokaisen tien turvallisemmaksi...
samalla kun rakentaa miljoonia kertoja enemmän teitä.

<!-- S55 -->
Ovatko ohjelmoijat siis huonoja työssään?
Eivät.
Olemme pyytäneet heiltä koko ajan jotain,
mitä mikään yleinen menetelmä ei voi taata.

<!-- S56 -->
Joten ehkä
"miten kirjoitamme ohjelmistoa ilman bugeja?"
on väärä kysymys.

<!-- S57 -->
Parempi kysymys on:
miten rakennamme järjestelmiä, jotka pysyvät turvassa,
vaikka ohjelmistossa on bugeja?

<!-- S58 -->
Ja juuri sinne tietoturva on menossa.
Se ei sano: älä koskaan tee virhettä.
Se sanoo: oleta, että olet jo tehnyt.

<!-- S59 -->
Muistatko sen paluuosoitteen?
Nykyään järjestelmä vartioi sitä.
Se sekoittaa, missä asiat sijaitsevat muistissa.
Ja se kieltäytyy suorittamasta käskyjä,
jotka on piilotettu dataan.

<!-- S60 -->
Bugi C-koodissamme on yhä siellä.
Sitä on vain paljon vaikeampi muuttaa hyökkäykseksi.

<!-- S61 -->
Ja sama ajatus on kaikkialla.
Hiekkalaatikot, rajatut oikeudet,
eristetyt prosessit, salaus,
varmuuskopiot, valvonta...
kerros kerroksen päälle,
jottei yksi bugi muutu katastrofiksi.

<!-- S62 -->
Ja sillä on hyvin käytännöllinen seuraus.
Jos bugit ovat väistämättömiä,
niiden korjaaminen ei ole valinnaista.

<!-- S63 -->
Ohjelmisto, jota käytät tänään,
sisältää hyvinkin mahdollisesti haavoittuvuuden,
jota kukaan ei ole vielä löytänyt.

<!-- S64 -->
Ja kun joku löytää sen,
päivitys on ero näiden välillä:
"haavoittuvuus löydettiin"
ja "meidät hakkeroitiin".

<!-- S65 -->
Sama pätee järjestelmiin, joita rakennamme.
Vanhat kirjastot ja tukemattomat alustat
eivät muutu turvallisemmiksi jäämällä huomiotta.
Niistä tulee teknistä velkaa.

<!-- S66 -->
Ja miksi se velka on maksettava pois —
videoni
"Toimiihan se yhä. Miksi siis päivittää?"
kertoo juuri siitä.

<!-- S67 -->
Sillä ohjelmistoissa
"se toimii yhä"
ja "se on yhä turvallinen"
ovat kaksi hyvin eri asiaa.
