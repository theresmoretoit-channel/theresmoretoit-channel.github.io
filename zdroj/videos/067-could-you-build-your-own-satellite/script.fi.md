<!-- S01 -->
Kuvittele, että sinulla on hullu idea.
Haluat rakentaa oman satelliittisi.
Et miljardin dollarin
viestintäsatelliittia.
Jotain pientä.

<!-- S02 -->
Laatikko, joka on suunnilleen
leipäpötkön kokoinen.
Sisällä: tietokone, aurinkopaneelit,
radio, muutama anturi.
Ehkä jopa kamera.

<!-- S03 -->
Rakennat sen autotallissasi.
Ja sitten jotenkin...
saat sen kiertoradalle.
Kuulostaa mahdottomalta.
Mutta ei se ole.

<!-- S04 -->
Ihmiset ovat tehneet
lähes juuri tätä jo vuosia.
Niitä kutsutaan CubeSateiksi.

<!-- S05 -->
Ja yllättävää on se,
että vaikeinta
ei ole satelliitin rakentaminen.
Vaan kaikki muu.

<!-- S06 -->
Perusyksikköä kutsutaan 1U:ksi —
noin kymmensenttinen kuutio.
Pinoat yksiköitä päällekkäin
ja saat 2U:n, 3U:n, 6U:n
ja isompiakin.

<!-- S07 -->
Idea on yksinkertainen.
Sen sijaan että suunnittelisit uuden
avaruusaluksen alusta,
käytät uudelleen standardikokoja
ja standardirajapintoja.
Ja yhtäkkiä avaruus on avoin
yliopistoille, startupeille,
ja ehkä jopa sinulle.

<!-- S07b -->
Muuten, jos pidät tällaisista
videoista, harkitse tilaamista.

Se auttaa kanavaa todella paljon.

<!-- S08 -->
Mitä pieni satelliittimme
oikeastaan sisältäisi?
Ensinnäkin se tarvitsee tietokoneen.
Jonkin täytyy ajaa ohjelmistoa,
ohjata laitteistoa
ja päättää, mitä tehdä.

<!-- S09 -->
Sitten on virta.
Aurinkopaneelit tuottavat sähköä.
Akut varastoivat sitä
niitä hetkiä varten, kun satelliitti
liukuu Maan varjoon.

<!-- S10 -->
Sitten viestintä.
Radio. Antenni.
Ja alhaalla Maassa,
kuunteleva maa-asema.

<!-- S11 -->
Sitten anturit.
Lämpötila. Jännite. Virta.
Kiihtyvyys. Magneettikenttä.
Ja jokin keino kertoa,
mihin suuntaan satelliitti osoittaa.
Koska kiertoradalla on yllättävän vaikea
sanoa, missä on 'ylös'.

<!-- S12 -->
Mutta ennen kuin rakennamme sellaisen,
on kiusallinen kysymys.
Paljonko tämä pieni laatikko maksaa?
Vastaus on...
enemmän kuin ulkonäöstä voisi päätellä.

<!-- S13 -->
Yksinkertainen 1U CubeSat
voi helposti maksaa
kymmeniä tuhansia dollareita —
pelkkänä lentolaitteistona.
Virtajärjestelmä. Aurinkopaneelit.
Akut. Tietokone. Radio.
Asennonhallinta. Rakenne.
Ja hyötykuorma.

<!-- S14 -->
Sitten tulevat asiat,
joita ei ole osaluettelossa.
Testaus. Integrointi.
Dokumentointi.
Maa-aseman operointi.
Lisensointi.
Ja lopuksi...
laukaisu.

<!-- S15 -->
Kyytiosuus pienelle CubeSatille
voi maksaa kymmeniä tuhansia.
Isommat missiot ja isommat CubeSatit
yltävät satoihin tuhansiin.
Ja se on vain
sen kapistuksen saamista avaruuteen.

<!-- S16 -->
Ja nyt
vielä naurettavampi ongelma.
Muistatko kaikki ne osat?
Miten ihmeessä kaikki tuo
mahtuu yhteen pikkuruiseen laatikkoon?

<!-- S17 -->
Avaruudessa ei ole tilaa
satunnaiselle elektroniikkakasalle.
Jokainen senttimetri merkitsee.
Jokainen gramma merkitsee.
Jokainen watti merkitsee.
Satelliitti on kolmiulotteinen palapeli,
jonka on selvittävä raketin laukaisusta.

<!-- S18 -->
Mistä siis hankit
kaikki nämä osat?
Sinun ei tarvitse suunnitella
kaikkea itse.
On kokonainen teollisuudenala,
joka myy komponentteja piensatelliiteille:
tietokoneita, virtajärjestelmiä,
radioita, antenneja ja aurinkopaneeleja.
On jopa markkinapaikkoja,
jotka on rakennettu varta vasten CubeSat-osille.

<!-- S18b -->
Ja osat ovat lisäksi standardoituja.
Monissa on samankokoiset piirilevyt,
jotka voi helposti pinota päällekkäin,
joten eri valmistajien palaset
sopivat yhteen yksikköön.
EnduroSatin ja GomSpacen
kaltaiset yritykset myyvät niitä,
ja yksittäinen alijärjestelmä voi maksaa
muutamasta tuhannesta
kymmeniin tuhansiin dollareihin.

<!-- S19 -->
Eivätkä nämä ole
eksoottisia prosessoreja.
Eräs nykyinen CubeSat-tietokone
käyttää ARM Cortex-M7:ää,
tutuilla rajapinnoilla —
SPI, I²C, UART ja CAN.

<!-- S19b -->
Eikä se ole räätälöity avaruussiru.
Se on aito, hyllystä saatava kortti,
jota voisit pitää kädessäsi.

<!-- S20 -->
Avaruusalus tarvitsee jotain
tärkeämpää kuin raaka nopeus:
ennustettavaa käytöstä,
pientä virrankulutusta ja luotettavuutta.
Vaativammat missiot
voivat käyttää ARM Cortex-A -prosessoreja —
ja jopa Linuxia.

<!-- S20b -->
Mutta se ei ole nopea.
Tyypillinen CubeSat-tietokone
käy parilla sadalla megahertsillä.
Sinun kannettavasi käy
neljällä tai viidellä gigahertsillä,
ja siinä on paljon enemmän ytimiä.
Satelliitin tietokone tinkii nopeudesta
kuluttaakseen mahdollisimman vähän sähköä.

<!-- S21 -->
Ja jos olet ohjelmoija,
tässä kohtaa se muuttuu kiinnostavaksi.
Et kirjoita
mitään salaperäistä "avaruuskieltä".
Kirjoitat sulautettua ohjelmistoa.
Usein C:llä tai C++:lla.

<!-- S22 -->
Se voi toimia suoraan
laitteistolla,
tai reaaliaikaisessa käyttöjärjestelmässä
kuten FreeRTOS, Zephyr tai RTEMS.
On jopa avoimia ohjelmistokehyksiä,
jotka on rakennettu avaruusaluksille.
Esimerkiksi NASAn F Prime
on lento-ohjelmiston kehys
sulautetuille ja avaruuslennon järjestelmille.

<!-- S23 -->
Koodisi saattaa siis näyttää
jokseenkin tältä.

<!-- S24 -->
Mutta on yksi valtava ero
tavalliseen tietokoneeseen.
Et pääse SSH:lla sisään.
Et voi liittää debuggeria.
Ja jos ohjelmistosi kaatuu...
tietokoneesi on
muutaman sadan kilometrin korkeudessa.

<!-- S25 -->
Siksi se tarvitsee vahtikoiria,
turvatiloja, vikojen tunnistusta
ja automaattista palautumista.
Sen on korjattava jotkin ongelmat
ilman että sinä olet auttamassa.

<!-- S25b -->
Ja yksi iso syy, miksi se tarvitsee kaiken tuon,
on säteily.
Avaruudessa kosmiset säteet
voivat kääntää bitin muistissa,
tai jopa lyödä sirun pois pelistä.
Raskasta suojausta ei ole —
se painaisi aivan liikaa.
Sen sijaan tietokone tarkkailee itseään,
korjaa virheitä
ja nollautuu, kun jokin menee vikaan.

<!-- S26 -->
Mutta jos oikeasti
haluat laukaista sen...
asiat muuttuvat vakaviksi.
Osa, joka toimii pöydälläsi,
ei ole automaattisesti valmis
rakettiin.
Sen on kestettävä tärinää,
tyhjiötä, lämpötilan ääripäitä
ja säteilyä.

<!-- S27 -->
Nyt takaisin siihen ongelmaan,
miten tietää, mihin suuntaan
satelliitti osoittaa.
Kuvittele sen kieppuvan
avaruudessa.
Ei lattiaa. Ei kattoa.
GPS voi kertoa sinulle,
missä olet...
mutta ei sitä, mihin suuntaan
olet kääntynyt.

<!-- S28 -->
Niinpä satelliitit yhdistävät
gyroskoopit, magnetometrit
ja aurinkoanturit
selvittääkseen asentonsa.
Ja sitten niiden on muutettava sitä.
Yksi yleinen kikka
on magnetorqueri.

<!-- S29 -->
Se työntää
Maan magneettikenttää vasten
ja tuottaa pienen vääntömomentin.
Se ei ole rakettimoottori.
Se ei liikuta satelliittia.
Se vain kääntää sitä.
Ja se riittää
kääntämään satelliitin
juuri sinne, minne haluat.

<!-- S30 -->
Mutta mikään tästä
ei ole syy,
miksi rakensimme satelliitin.
Tarvitsemme mission.
Se on hyötykuorma.
Mittaa säteilyä.
Valokuvaa Maata.
Tutki ilmakehää.
Testaa uutta anturia.
Tai vain todista,
että uusi teknologia toimii.

<!-- S31 -->
Satelliitti itsessään
on siellä lähinnä
pitääkseen hyötykuorman hengissä.
Syötä sille virtaa. Suuntaa se.
Pidä se lämpimänä.
Tallenna sen data.
Ja lähetä se kotiin.

<!-- S32 -->
Kun pöytäkoneesi jumittuu,
käynnistät sen uudelleen.
Kun satelliittisi jumittuu...
sinulla on hyvin kallis kappale
kiertämässä Maata hiljaa.

<!-- S33 -->
Sanotaan siis, että rakensimme sen.
Kaikki toimii...
Tietokone käynnistyy...
Radio puhuu.
Paneelit tuottavat virtaa.
Hyötykuorma pyörii...
Voimmeko laukaista sen?
...Emme vielä.

<!-- S34 -->
Satelliitin on todistettava,
että se kestää laukaisun.
Se tarkoittaa testaamista.
Paljon testaamista.

<!-- S35 -->
Ensin pulttaa se
jättimäiseen täristimeen.
Sitten täristä sitä kovaa...
Se on tärinätestausta.
Rakettien laukaisut eivät ole hellävaraisia.
Sen on kestettävä
melu, tärinä ja isku
ilman että mikään
irtoaa tai hajoaa.
Jokainen ruuvi merkitsee.
Jokainen liitin merkitsee.
Jokainen kaapelinpätkä merkitsee.

<!-- S36 -->
Sitten tulee tyhjiö.
Maassa ilma kuljettaa lämmön pois.
Avaruudessa ei ole ilmaa.
Toinen puoli voi kuumeta valtavasti,
toinen taas jäähtyä todella kylmäksi,
ja elektroniikan
on silti pysyttävä
rajojensa sisällä.
Siksi satelliitti tarvitsee
lämpösiltoja, pinnoitteita,
eristystä
ja huolella valittuja materiaaleja.
Satelliiteilla ei ole
ilmastointia.
Niillä on fysiikka.

<!-- S37 -->
Ja akun kanssa
riittää haastetta.
Lataa se auringonvalolla.
Sitten satelliitti
liukuu Maan varjoon,
ja paneelit eivät tuota juuri lainkaan sähköä.
Akku pitää sen hengissä.
Sitten takaisin auringonvaloon.
Lataus. Purku.
Lataus. Purku.
Yhä uudelleen.
Vuosikausia.
Yksi virhe virranhallinnassa
voisi hiljaa lopettaa mission.

<!-- S38 -->
Ja nyt, miten puhut sille?
Tarvitset radion.
Antennin.
Ja taajuuden,
jota sinulla on laillinen lupa käyttää.
Ja maa-aseman.
Satelliitilla
ei ole internetiä.
Se vain lentää yli
ja lähettää.

<!-- S39 -->
Maa-asemasi
nappaa signaalin.
Tietokone purkaa sen.
Ja yhtäkkiä sinulla on dataa
omasta avaruusaluksestasi.
Kuvittele, että avaat terminaalin
ja näet tämän.

Paitsi että kone,
joka tulostaa nuo numerot...
on satojen kilometrien
päässä pääsi yllä.

<!-- S40 -->
Miten me sitten
oikeasti saamme sen sinne ylös?
Voisit rakentaa raketin...
Ole kiltti, älä...
Et tarvitse sellaista.
CubeSatit lentävät
toissijaisena hyötykuormana.

<!-- S41 -->
Raketti on jo lähdössä ylös.
Siinä on ylimääräistä tilaa.
Satelliittisi matkustaa mukana
vakiomallisessa vapauttimessa.
Omaa rakettia ei tarvita.

<!-- S42 -->
Ja nyt se istuu
raketin nokassa.
Et voi koskea siihen.
Et voi avata laatikkoa.
Et voi kytkeä kaapelia.
Raketti laukaistaan.
Noin yhdeksän minuuttia myöhemmin
olet kiertoradalla.

<!-- S43 -->
Vapautin
päästää satelliittisi irti.
Se ponnahtaa vapaaksi
ja alkaa kiepua.

<!-- S43b -->
Mutta mistä se tietää olevansa ulkona?
...
Jousikuormitteiset kytkimet, jotka olivat
painettuina vapauttimen sisällä,
palautuvat ulos heti, kun satelliitti vapautetaan,
ja tietokone käynnistyy.
Sitten, sääntöjen mukaan,
se pysyy hiljaa noin puoli tuntia.
Vasta sitten se käynnistää radionsa,
avaa antenninsa,
ja lopulta soittaa kotiin.
Ja jossain Maan päällä...
maa-asemasi kuulee sen.

<!-- S44 -->
Rakensit koneen.
Ja nyt se kone
kiertää planeettaa.

<!-- S44b -->
Paitsi että emme ole valmiita.
Kuollut satelliitti ei voi vain
jäädä sinne ikuisesti.
Kiertoradalle vuosisadoiksi jätettynä
siitä tulee avaruusromua.

<!-- S45 -->
Se tarkoittaa, että nykyaikaisten missioiden
on yhä useammin suunniteltava
avaruusaluksen elinkaaren
loppu.
Parhaimmillaan ohut yläilmakehä
vetää sitä hitaasti alas.
Sen kiertorata madaltuu.
Se palaa ilmakehään.
Ja palaa poroksi.
Mission loppu...
on osa missiota.

<!-- S46 -->
Niin... voisitko rakentaa
oman satelliittisi?
Teknisesti kyllä.
Sinun ei tarvitse olla NASA.
Sinun ei tarvitse
omistaa rakettia.
Et välttämättä tarvitse edes
suurta yritystä.

<!-- S47 -->
Satelliitin on
kestettävä laukaisu.
Kestettävä avaruus.
Viestittävä laillisesti.
Toimittava omillaan.
Ja lopulta
poistuttava kiertoradalta.
Kaikki tuo
on todistettava,
ennen kuin kukaan
laittaa sen rakettiin.

<!-- S48 -->
CubeSatit eivät tehneet avaruudesta helppoa.
Ne tekivät siitä standardoidun.
Sen sijaan että rakentaisit kaiken
alusta,
voit rakentaa jotain,
joka sopii olemassa olevaan standardiin.
Ja se on yllättävän suuri muutos.

<!-- S49 -->
Jossain juuri nyt
on pieniä koneita
kiertämässä Maata.
Yliopistojen,
tutkimusryhmien,
yritysten ja opiskelijoiden rakentamia.

<!-- S50 -->
Jotkut kantavat kameroita.
Jotkut mittaavat säteilyä.
Jotkut testaavat
upouutta teknologiaa.
Ja jotkut ovat vain kokeita,
joissa etsitään vastausta yhteen kysymykseen:
"saammeko tämän vekottimen
toimimaan avaruudessa?"

<!-- S51 -->
Ja juuri se tekee
oman satelliitin rakentamisesta
niin kiehtovaa.
Koska etäisyys
sinun ja avaruuden välillä
ei ole enää raketti.
Se saattaa olla...
kymmensenttinen laatikko.
Ja hyvin, hyvin
pitkä tarkistuslista.
