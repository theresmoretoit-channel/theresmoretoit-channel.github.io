<!-- S01 -->
Neljä autoa saapuu risteykseen
täsmälleen samalla hetkellä.
Ei liikennevaloja. Ei merkkejä.
Vain sääntö, jota monissa maissa noudatetaan:
väistä oikealta tulevaa autoa.

<!-- S02 -->
Jokainen kuljettaja katsoo oikealle
ja näkee auton, jota hänen on väistettävä.
Joten jokainen kuljettaja odottaa.

<!-- S03 -->
Kukaan ei riko sääntöä.
Kaikki noudattavat sitä täydellisesti.
Eikä kukaan pääse koskaan liikkeelle.

<!-- S04 -->
Tietojenkäsittelytieteessä tätä kutsutaan lukkiutumiseksi (deadlock).
Eikä sitä tapahdu vain teillä.
Sitä tapahtuu tietokannoissa,
käyttöjärjestelmissä ja tavallisissa ohjelmissa.

<!-- S05 -->
Tietokoneet ovat usein hyviä havaitsemaan
lukkiutumisen, kun se on jo tapahtunut.
Mutta voisiko ohjelma lukea toisen ohjelman
ja kertoa sinulle varmasti,
jääkö se koskaan jumiin?

<!-- S06 -->
Monien ohjelmien kohdalla kyllä.
Mutta menetelmää, joka toimii
jokaiselle mahdolliselle ohjelmalle,
ei voi olla olemassa.
Eikä siksi, että tietokoneet
eivät vielä olisi tarpeeksi nopeita.
Mikään nopeampi tietokone ei muuta sitä koskaan.

<!-- S07 -->
Näin ohjelma jää jumiin.
Kuvittele verkkokauppa,
jossa kaksi tehtävää on käynnissä yhtä aikaa.

<!-- S08 -->
Ennen kuin tehtävä muuttaa mitään,
se ottaa siihen lukon,
jotta kukaan muu ei voi koskea siihen.
Vähän kuin ottaisit huoneen ainoan avaimen.

<!-- S09 -->
Ensimmäinen tehtävä lukitsee asiakkaan tilin
ja yrittää sitten lukita hänen tilauksensa.
Toinen lukitsee tilauksen
ja yrittää sitten lukita tilin.

<!-- S10 -->
Yksi pitää tiliä hallussaan
ja odottaa tilausta.
Toinen pitää tilausta hallussaan
ja odottaa tiliä.
Kumpikaan ei luovu siitä, mitä pitää hallussaan.

<!-- S11 -->
Ja oudointa on,
että tämä koodi voi toimia miljoona kertaa
ilman ongelmia.
Vasta kun kaksi tehtävää osuu päällekkäin
juuri väärässä järjestyksessä,
kaikki pysähtyy.

<!-- S12 -->
Vika oli siellä koko ajan.
Ajoitus vain paljasti sen.

<!-- S12b -->
Muuten, jos pidät tällaisista
videoista, voit tilata kanavan.

Se auttaa kanavaa todella paljon.

<!-- S13 -->
Tietokannat törmäävät tähän jatkuvasti,
joten ne pitävät vahtia.
Ne piirtävät kartan siitä, kuka odottaa ketäkin.

<!-- S14 -->
Ensimmäinen odottaa toista.
Toinen odottaa ensimmäistä.
Kun nuolet sulkeutuvat silmukaksi,
kyseessä on lukkiutuminen.
Ei arvailua. Silmukka näkyy selvästi.

<!-- S15 -->
Sitten tietokanta tekee jotain brutaalia.
Se valitsee yhden tehtävistä
ja heittää sen työn roskiin.

<!-- S16 -->
Microsoftin SQL Server jopa ilmoittaa häviäjälle,
että se on valittu
lukkiutumisen uhriksi
ja että sen pitäisi yrittää uudelleen.

<!-- S17 -->
Toinen tehtävä jatkaa,
ja uhri voi yksinkertaisesti yrittää uudelleen.

<!-- S18 -->
Huomaa, mitä tämä korjaa ja mitä ei.
Lukkiutuminen on purettu.
Mutta sen aiheuttanut koodi on yhä paikallaan
odottamassa seuraavaa huonoa hetkeä.

<!-- S19 -->
Lukkiutumisen huomaaminen
sen jo tapahduttua
on siis se helppo osa.
Vaikea kysymys on toinen.

<!-- S20 -->
Ei: onko tämä ohjelma jumissa juuri nyt?
Vaan: anna sille tämä syöte.
Voiko se koskaan jäädä jumiin?

<!-- S21 -->
Ensimmäinen on valokuva nykyhetkestä.
Sitä voi vain katsoa.
Toinen on ennuste
jokaisesta mahdollisesta tulevaisuudesta.

<!-- S22 -->
Ja ohjelmat tekevät siitä hyvin vaikeaa.
Ne tekevät päätöksiä. Ne toistavat asioita.
Ne voivat ajaa laskutoimituksia, jotka kestävät
sekunnin tai tuhat vuotta.

<!-- S23 -->
Ohjelma voi jäädä jumiin heti,
miljoonan askeleen jälkeen,
yhdellä harvinaisella syötteellä
tai ei koskaan.

<!-- S24 -->
Voisit vain ajaa sen ja katsoa.
Mutta jos se ei ole jäänyt jumiin tunnin jälkeen,
mitä se kertoo sinulle?

<!-- S25 -->
Ei mitään.
Se voi jäädä jumiin seuraavalla sekunnilla
tai ei koskaan.

<!-- S26 -->
Vuonna 1936 nuori matemaatikko
nimeltä Alan Turing osoitti,
että joihinkin ohjelmia koskeviin kysymyksiin
ei mikään ohjelma pysty vastaamaan.
Kuuluisin niistä kuulostaa vielä yksinkertaisemmalta.

<!-- S27 -->
Ota mikä tahansa ohjelma ja sen syöte.
Pysähtyykö se lopulta?
Vai jatkuuko se ikuisesti?

<!-- S28 -->
Nykyään sitä kutsutaan pysähtymisongelmaksi.
Eikä mikään ohjelma pysty ratkaisemaan sitä
oikein kaikissa tapauksissa.

<!-- S29 -->
Todistuksen idea
on yllättävän lyhyt.
Oletetaan, että joku antaa sinulle
täydellisen pysähtymistarkistimen.

<!-- S30 -->
Nyt kirjoitat pienen, uppiniskaisen ohjelman.
Se kysyy tarkistimelta itsestään
ja tekee sitten päinvastoin.

<!-- S31 -->
Jos tarkistin sanoo, että se pysähtyy,
se jää ikuiseen silmukkaan.
Jos tarkistin sanoo, että se jatkuu ikuisesti,
se pysähtyy heti.

<!-- S32 -->
Sanoi tarkistin siitä mitä tahansa,
tarkistin on väärässä.
Joten täydellistä tarkistinta ei voi olla olemassa.

<!-- S33 -->
Miten tämä sitten liittyy lukkiutumisiin?
Hyvin suoraan.

<!-- S34 -->
Kuvittele, että joku väittää rakentaneensa
täydellisen lukkiutumisennustimen.
Annat sille minkä tahansa ohjelman ja sen syötteen,
ja se kertoo sinulle aina oikein,
jääkö ohjelma koskaan jumiin.

<!-- S35 -->
Käytetään sitä
pysähtymisongelman ratkaisemiseen.

<!-- S36 -->
Ota mikä tahansa ohjelma
ja sijoita se uuden ohjelman sisään.

<!-- S37 -->
Ensin uusi ohjelma
yksinkertaisesti ajaa vanhan,
askel kerrallaan, yhdessä säikeessä.
Ei lukkoja. Ei mitään jaettua.
Ei mitään, mikä voisi koskaan jäädä jumiin.

<!-- S38 -->
Sitten, jos vanha ohjelma joskus päättyy,
uusi käynnistää kaksi tehtävää.
Kumpikin ottaa yhden lukon,
odottaa, kunnes toinen on ottanut omansa,
ja yrittää sitten ottaa toisen lukon.
Lukkiutuminen, tahallaan, joka kerta.

<!-- S39 -->
Jos vanha ohjelma ei koskaan pääty,
uusi ei koskaan pääse niin pitkälle.
Ei lukkiutumista. Ei koskaan.

<!-- S40 -->
Uusi ohjelma siis jää jumiin
jos ja vain jos vanha pysähtyy.

<!-- S41 -->
Kysy nyt ennustimelta
uudesta ohjelmasta.
”Kyllä, se lukkiutuu”
tarkoittaa, että vanha ohjelma pysähtyy.
”Ei” tarkoittaa, että se jatkuu ikuisesti.

<!-- S42 -->
Ratkaisimme juuri pysähtymisongelman.
Ja juuri sitä ei voi tehdä.

<!-- S43 -->
Täydellistä lukkiutumisennustinta
ei siis myöskään voi olla olemassa.

<!-- S44 -->
Ongelma ei ole lukoissa,
tietokannoissa eikä huonoissa ohjelmoijissa.
Ohjelma voi kätkeä minkä tahansa laskennan
juuri ennen lukkiutumista.
Jotta voisit ennustaa lukkiutumisen,
sinun pitäisi ennustaa, päättyykö laskenta.

<!-- S45 -->
Mutta hetkinen.
Oikea tietokone ei ole ääretön.
Sen muistilla on rajallinen määrä tiloja.
Eikö ne kaikki voisi vain tarkistaa?

<!-- S46 -->
Koneelle, jolla on kiinteä määrä
muistia, periaatteessa kyllä.
Käytännössä yritäpä laskea ne.

<!-- S47 -->
Kahdeksan gigatavun
kannettavan muisti
voidaan järjestää niin monella tavalla,
että pelkästään sen luvun kirjoittamiseen
tarvitaan noin kaksikymmentä miljardia numeroa.

<!-- S48 -->
Havaittavan maailmankaikkeuden
atomien lukumäärässä
on noin kahdeksankymmentä numeroa.

<!-- S49 -->
Oikealla koneella kaiken tarkistaminen
on siis mahdollista teoriassa
ja toivotonta käytännössä.

<!-- S50 -->
Mutta se on eri muuri.
Turingin raja ei johdu siitä, että tiloja on liikaa.
Se koskee ohjelmia,
jotka voivat aina pyytää lisää muistia.
Niille ei voi olla täydellistä ennustinta,
olipa tietokone kuinka suuri tahansa.

<!-- S51 -->
Ovatko lukkiutumiset siis toivoton tapaus?
Eivät.
Se tarkoittaa vain, ettei täydellistä tarkistinta ole.
Joten ohjelmoijat kirjoittavat ohjelmia,
joita on helpompi tarkistaa.

<!-- S52 -->
Yksinkertaisin keino on järjestys.
Jokaisen tehtävän on lukittava tili
ennen tilausta.
Ei koskaan toisin päin.

<!-- S53 -->
Jos jokainen tehtävä todella pysyy siinä järjestyksessä,
silmukkaa ei voi syntyä,
eikä tällaista lukkiutumista voi tapahtua.

<!-- S54 -->
Toiset järjestelmät luovuttavat aikakatkaisun jälkeen,
ottavat kaikki lukkonsa kerralla
tai antavat tietokannan valita uhrin
ja yrittävät yksinkertaisesti uudelleen.

<!-- S55 -->
Ja pienistä, huolellisesti kuvatuista suunnitelmista
työkalut voivat tarkistaa jokaisen mahdollisen tilan.
Amazonin insinöörit käyttivät yhtä sellaista
ja löysivät vian, joka vaati kolmekymmentäviisi askelta
juuri oikeassa järjestyksessä ilmetäkseen.

<!-- S56 -->
Nämä työkalut toimivat,
koska ongelma on tehty pienemmäksi.
Ne tarkistavat järjestelmän mallin,
eivät jokaista ohjelmaa, joka voisi koskaan olla olemassa.

<!-- S57 -->
Oikean koodin kohdalla
tarkistimen, joka ottaa minkä tahansa ohjelman,
on kuitenkin luovuttava jostakin.
Se voi varoittaa lukkiutumisista,
joita ei voi tapahtua,
ohittaa joitakin, joita voi,
tai joskus jättää vastaamatta kokonaan.

<!-- S58 -->
Tarkistin, joka ei koskaan anna väärää hälytystä,
ei koskaan jätä yhtäkään lukkiutumista huomaamatta
ja antaa aina vastauksen,
jokaiselle ohjelmalle,
on juuri se, minkä Turing sulki pois.

<!-- S59 -->
Takaisin risteykseen:
ne neljä kuljettajaa eivät istu siellä ikuisesti.

<!-- S60 -->
Joku viittaa kädellään.
Yksi kuljettaja luopuu vuorostaan,
ja sekunneissa kaikki on ohi.

<!-- S61 -->
Juuri niin tekee tietokantakin.
Se ei ennusta lukkiutumista.
Se huomaa sen
ja pakottaa jonkun väistämään.

<!-- S62 -->
Jotkin ongelmat vaativat nopeamman tietokoneen.
Jotkin paremman idean.

<!-- S63 -->
Ja joillakin, kuten tällä,
ei ole lainkaan täydellistä ratkaisua.
Vain hyvät säännöt
ja joku, joka on valmis viittaamaan.
