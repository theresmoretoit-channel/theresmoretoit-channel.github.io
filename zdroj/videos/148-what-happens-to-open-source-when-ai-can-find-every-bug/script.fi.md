<!-- S01 -->
948.
Niin monta eri tapaa tekoäly löysi
Linux-tietokoneen kaappaamiseen sisältäpäin.

<!-- S02 -->
Ei varastettua salasanaa. Ei etämurtoa.
Jokainen alkaa tavallisesta käyttäjästä,
jolla ei ole mitään erityisoikeuksia,
ja päättyy rootiin,
tiliin, joka voi tehdä mitä tahansa.

<!-- S03 -->
OpenAI julkaisi tuloksen marraskuussa 2026.
Koko ajo maksoi
1,2 miljoonaa dollaria API-krediitteinä.

<!-- S05 -->
Nämä ovat OpenAI:n omia lukuja,
jotka julkaistiin päivää ennen
kuin yhtiö toi markkinoille ne tuottaneen mallin,
eikä kukaan ulkopuolinen ole vahvistanut koko määrää.
Mutta satoja raportteja ja korjauksia
on jo lähetetty.

<!-- S06 -->
Tästä syystä asia koskee muutakin kuin Linuxia.
Linuxin lähdekoodi on julkinen.
Kuka tahansa voi lukea sen.
Vuosikymmeniä se oli perustelu
sille, miksi Linux on turvallinen.

<!-- S07 -->
Jos siis kone pystyy lukemaan julkista koodia
ja tekemään siitä toimivia hyökkäyskoodeja tässä mittakaavassa,
pitäisikö ohjelmistojen sittenkin pitää koodinsa salassa?

<!-- S08 -->
Katsotaan ohjelmistoa, joka jo tekee niin.
Huhtikuussa 2026 Microsoft korjasi
164 tietoturva-aukkoa
kuukausittaisena päivityspäivänään.
Lokakuussa se korjasi
1 413.

<!-- S09 -->
Pelkästään sinä kuukautena se korjasi enemmän
kuin minään kokonaisena vuonna aiemmin.
Yli 1 000 korjauksista koski Windowsia,
ja Microsoft oli varoittanut,
että sen omat tekoälytyökalut kasvattaisivat määrää.

<!-- S10 -->
Näitä kahta lukua et voi verrata suoraan.
Yhtiöt laskevat eri tavoin,
ja Microsoft etsi omasta suljetusta koodistaan.

<!-- S11 -->
Mutta yhden asian se osoittaa.
Koodin pitäminen salassa
ei ollut pitänyt bugeja poissa.

<!-- S12 -->
Mikä sitten oikeasti suojaa sinua?
Vastataksemme siihen
meidän täytyy nähdä, miten tämä kone toimii,
koska sen jokainen vaihe karsii jotain pois.

<!-- S13 -->
Linuxin ytimessä on
yli 40 miljoonaa riviä koodia.
Ensin tiedusteluagentit kävivät sen läpi
ja valitsivat ne osat,
joihin tavallinen käyttäjä oikeasti ylettyy.

<!-- S14 -->
Jäljelle jäi noin 7 %.
Se on osa, jonka ne arvioivat hyökkäämisen arvoiseksi,
ei satunnainen otos,
joten tulosta et voi kertoa 14:llä.

<!-- S15 -->
Seuraavaksi analyytikkoagentit kävivät koodin läpi
ja listasivat kaiken epäilyttävän.
2 308 ehdokasta
12 tunnissa.

<!-- S16 -->
Mutta epäily ei todista mitään.
Siksi toiset agentit kirjoittivat testiohjelmia
ja ajoivat niitä eristetyissä virtuaalikoneissa.
1 724 bugia
osoittautui todellisiksi.

<!-- S17 -->
Sitten tuli kallis osuus:
toimivien hyökkäyskoodien rakentaminen
niin, että tavallisen työpöytäjärjestelmän
vakiosuojaukset olivat päällä.
1 169
pääsi rootiin asti.

<!-- S18 -->
Ryhmittele ne taustalla olevan virheen mukaan,
niin saat ne 948.

<!-- S19 -->
Raportissa on yksi yksityiskohta,
jota on vaikea unohtaa.
Eräässä varhaisessa ajossa
agentit ilmoittivat 200 onnistumista.
Sitten ihmiset tarkistivat, miten ne olivat päässeet sinne.

<!-- S20 -->
Kaksikymmentä niistä oli päässyt rootiin
toisen, tuntemattoman bugin kautta,
ei sen, jota niitä oli käsketty käyttämään.
Kun ne lähetettiin avaamaan yksi ovi,
ne löysivät toisen, josta kukaan ei tiennyt.

<!-- S21 -->
Otoksessa hyökkäyskoodeistaan
OpenAI tunnisti kymmenen hyökkäystekniikkaa,
joita ulkopuoliset asiantuntijat eivät olleet nähneet.

<!-- S22 -->
Heinäkuussa aiempi malli
löysi 166 tällaista aukkoa.
Kolmen kuukauden korjausten jälkeen
uudempi malli löysi 948.
Bugit eivät olleet loppuneet.
Myöhempi ajo löysi niitä paljon enemmän.

<!-- S23 -->
Tässä on kuitenkin tärkeä rajoitus.
Mikään tästä ei murtaudu tietokoneeseesi
internetin kautta.
Hyökkääjän täytyy olla jo koneella
tavallisena käyttäjänä.

<!-- S24 -->
Se on vähemmän lohdullista kuin kuulostaa,
koska oikeat hyökkäykset tulevat usein kahdessa vaiheessa.
Ensin päästään sisään
selaimen aukon tai haitallisen latauksen kautta.
Sitten tarvitaan root.
Tämä on se toinen vaihe.

<!-- S25 -->
OpenAI:n neuvo on suorasukainen.
Järjestelmässä, josta puuttuvat uusimmat korjaukset,
pidä mitä tahansa tavallista tiliä rootina,
ainakin hyvin rahoitettua hyökkääjää vastaan.

<!-- S26 -->
Mitä tämä sitten tarkoittaa
avoimen koodin vanhalle perustelulle?
1990-luvun lopulla
Eric Raymond antoi sille iskulauseen:
”Kun silmäpareja on tarpeeksi, kaikki bugit löytyvät helposti.”

<!-- S27 -->
Hän kutsui sitä Linuksen laiksi.
Se on kaunis ajatus, mutta sen sisällä on oletus:
että joku oikeasti katsoo.

<!-- S28 -->
Vuonna 2014 Heartbleed-niminen bugi
paljastui OpenSSL:stä,
koodista, joka suojasi valtavaa osaa verkosta.
Noin puolen miljoonan suojatun palvelimen
arveltiin olevan alttiina.

<!-- S29 -->
Bugi oli maannut julkisessa koodissa kaksi vuotta.
Projekti sai
noin 2 000 dollaria lahjoituksia vuodessa,
ja sillä oli yksi kokoaikainen kehittäjä.

<!-- S30 -->
Kuka tahansa olisi voinut lukea sen.
Tuskin kukaan luki.

<!-- S31 -->
Se oli aina avoimen lähdekoodin todellinen heikkous.
Koodia ei katsonut liian moni. Vaan liian harva.

<!-- S32 -->
Ja juuri sen tekoäly muuttaa.
Kone voi jatkaa skannaamista
ja tutkia paljon useampia ehdokkaita
kuin ihmistutkija ehtisi yksinään.
Vanha lupaus vihdoin lunastetaan,
kaikille, myös hyökkääjille.

<!-- S33 -->
Julkista koodia siis todella tutkitaan nyt.
Auttaako sen piilottaminen?

<!-- S34 -->
Suljetun ohjelman täytyy silti toimia,
joten sen konekoodi on
jokaisella tietokoneella, joka sitä käyttää.
Ghidran kaltaiset työkalut muuttavat sen takaisin
joksikin lähdekoodin kaltaiseksi.

<!-- S35 -->
Ja on olemassa klassinen temppu.
Vertaa ohjelmaa
ennen tietoturvapäivitystä ja sen jälkeen.
Se, mikä muuttui, näyttää sinulle, missä aukko oli.

<!-- S35b -->
Se kertoo hyökkääjille, mihin tähdätä,
kauan ennen kuin jokainen järjestelmä
on asentanut päivityksen.

<!-- S36 -->
Anthropic kokeili tätä Windowsin ytimellä:
21 aukkoa,
jotka Microsoft oli hiljattain korjannut,
eikä lähdekoodia.
Tekoäly sai järjestelmän kaatumaan ensi kerran 31 minuutissa.
Kuudessa tunnissa niitä oli 18.

<!-- S37 -->
Kahdeksasta tuli toimivia hyökkäyskoodeja,
jotka pystyivät ottamaan koneen täysin hallintaansa,
noin 2 000 dollarilla kappale.

<!-- S38 -->
Mutta nämä eivät olleet tuntemattomia bugeja.
Korjaukset osoittivat jo,
missä ongelmat olivat.
Uuden aukon löytäminen tyhjästä on vaikeampaa.

<!-- S39 -->
Salailu siis maksaa hyökkääjälle yhä jotain.
Se on hidaste, ei muuri.
Kuinka korkea hidaste on?
Siitä ei ole julkista lukua.

<!-- S40 -->
Entä toinen puoli?
Mitä avoimuus oikeasti antaa sinulle?
Vastaus on pienessä yksityiskohdassa
OpenAI:n raportissa.

<!-- S41 -->
Skannauksen ja analyysin kymmenen päivän aikana
yli 100 näistä Linux-aukoista
oli muiden ihmisten korjaamia
tai korjauksen alla.
Noin 300 muusta
keskusteltiin jo julkisesti.

<!-- S42 -->
Muut löysivät samoja bugeja
samaan aikaan.

<!-- S43 -->
Linus Torvalds oli kuvannut tämän jo toukokuussa.
Hänen mukaansa tekoälyraportit
olivat tehneet ytimen tietoturvan postituslistasta
”lähes täysin hallitsemattoman”,
koska eri ihmiset löysivät yhä uudelleen
samat asiat samoilla työkaluilla.

<!-- S44 -->
Ja hänen neuvonsa oli tämä:
”Jos löysit bugin tekoälytyökaluilla,
on todennäköistä, että joku muukin löysi sen.”

<!-- S45 -->
Ytimen säännöt sanovat sen nyt suoraan.
Tekoälyllä löydettyä bugia on pidettävä julkisena,
koska tällaiset bugit tulevat esiin
usealla tutkijalla,
usein samana päivänä.

<!-- S46 -->
Mieti, mitä se tekee
ajatukselle salaisesta bugista.
Jos sen löytäminen oli sinulle halpaa,
se oli halpaa kaikille.

<!-- S47 -->
Avoimessa lähdekoodissa
kuka tahansa voi tarkastella raporttia,
varmistaa korjauksen ja kyseenalaistaa tuloksen.
Suljetussa ohjelmistossa
joudut enimmäkseen luottamaan toimittajaan.

<!-- S49 -->
Mutta avoimuudella on laskunsa,
eikä se ole se, jota odottaisit.
On houkuttelevaa sanoa,
ettei pienellä projektilla ole varaa skannaukseen.
Tekoäly-yhtiöt tarjoavat jo
ylläpitäjille ilmaista käyttöä.

<!-- S50 -->
Pulaa on ihmisistä.
Ytimeen kirjattiin ennen
noin 500 tietoturvaongelmaa julkaisua kohden.
Tänä vuonna määrä ylitti 1 500.
Monet ovat pieniä,
mutta jonkun täytyy silti käydä ne läpi.

<!-- S51 -->
Tammikuussa curl-projekti
lopetti rahalliset bugipalkkionsa,
jotta se ei enää palkitsisi roskaraporttien tulvaa.

<!-- S52 -->
Hyvätkin raportit vain siirtävät työtä eteenpäin.
Tekoälyn tuottamat korjaukset tarvitsevat yhä ihmisen tarkistuksen.
Osa varhaisista korjauksista lisäsi turhaa koodia
tai ohitti saman bugin muita muunnelmia.

<!-- S53 -->
Lisää skannausta voit ostaa.
Et voi ostaa lisää ihmisiä,
jotka ymmärtävät jonkin koodinpätkän yhtä hyvin.
Tässä yrityksellä, jolla on palkattu tietoturvatiimi,
on todella etulyöntiasema.

<!-- S54 -->
Ja sitten tulee viimeinen ongelma.
Korjattu ei ole sama asia kuin asennettu.

<!-- S55 -->
Maaliskuussa 2017
Microsoft korjasi Windowsin aukon.
Suljettu koodi, yksi toimittaja, yksi päivitysjärjestelmä.
Kaksi kuukautta myöhemmin
WannaCry pääsi saman aukon kautta
noin 200 000 tietokoneeseen
noin 150 maassa.

<!-- S56 -->
Sillä korjauksella oli kaksi kuukautta aikaa levitä,
eikä se riittänyt.
Hyökkääjä ei ehkä enää anna sinulle kahta kuukautta.
Samassa Anthropicin tutkimuksessa
tekoäly otti julkisen korjauksen
Firefoxin JavaScript-moottoriin
ja sai toimivan hyökkäyskoodin alle tunnissa.

<!-- S57 -->
Firefoxin korjattuun versioon
oli vielä 18 päivää.

<!-- S58 -->
Tämä on korjauksen julkaisemisen vaara.
Tieto voi päätyä hyökkääjille
ennen kuin päivitys päätyy sinulle.

<!-- S59 -->
Linux-korjauksella on pitkä matka kuljettavana,
ytimestä vakaaseen julkaisuun,
jakeluusi ja laitteellesi.
Puhelin voi joutua odottamaan kuukausia tai ikuisesti.

<!-- S60 -->
Eikä suljettu ohjelmisto välty tältä.
Näimme sen juuri: Windowsin korjaus riitti.
Jokainen päivitys on nyt myös kartta.

<!-- S60b -->
Pidä siis kaikki ajan tasalla,
tietokone, puhelin ja jopa reititin,
ja asenna päivitykset heti, kun ne tulevat.
Kun tekoäly paranee korjausten muuttamisessa hyökkäyksiksi,
jokainen odotettu päivä painaa yhä enemmän.

<!-- S61 -->
Onko avoin lähdekoodi siis yhä turvallisempi?
Rehellisesti sanottuna kukaan ei tiedä.
Sikäli kuin julkisesti tiedetään,
kukaan ei ole testannut molempia puolia samalla tavalla
samoilla säännöillä.

<!-- S62 -->
Se, mitä voimme sanoa, on vaatimattomampaa.
Koodin piilottaminen hyödyttää vähemmän kuin ennen.
Sen näyttäminen antaa kenen tahansa tarkistaa työn
ja kasaa entistä enemmän työtä
niille, jotka koodia ylläpitävät.

<!-- S64 -->
Vaikka tekoäly ei koskaan löytäisi jokaista bugia,
se on jo muuttanut sen, mitä niiden löytäminen maksaa.

<!-- S65 -->
Nyt ratkaisee se, kuinka kauan aukko pysyy auki
siitä hetkestä, kun joku löytää sen,
siihen hetkeen, kun se suljetaan sinun koneellasi.

<!-- S66 -->
Joten tässä kysymys sinulle.
Jos kuka tahansa voi löytää minkä tahansa bugin,
luottaisitko mieluummin koodiin, jonka voit lukea,
vai yritykseen, jolle maksetaan sen korjaamisesta?
Kerro kommenteissa.
