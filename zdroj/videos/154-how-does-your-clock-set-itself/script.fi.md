<!-- S01 -->
Jossain kotonasi
saattaa olla kello,
jota kukaan ei ole koskaan asettanut.

<!-- S02 -->
Se selviää sähkökatkoista.
Se siirtyy kesäaikaan ja takaisin
itsestään, keskellä yötä.

<!-- S03 -->
Sillä ei ole internetyhteyttä.
Ei wifiä, ei GPS:ää,
ei sovellusta puhelimessa.

<!-- S04 -->
Sillä on vain pikkuruinen radiovastaanotin.
Ja kerran sekunnissa
se kuulee yhden ainoan pulssin.

<!-- S05 -->
Miten kello siis muuttaa
yhden pulssin sekunnissa
tarkaksi kellonajaksi, päivämääräksi
ja jopa viikonpäiväksi?

<!-- S06 -->
Euroopassa pulssit tulevat
DCF77-asemalta Frankfurtin läheltä.
Amerikassa WWVB-asemalta Coloradosta.
Eri lähettimet, sama idea.

<!-- S07 -->
Otetaan esimerkiksi saksalainen.
Se lähettää tasaista radioaaltoa
päivin ja öin.
Ja jokaisen sekunnin alussa
se heikentää aaltoa hetkeksi.

<!-- S08 -->
Juju on siinä, kuinka pitkään
aalto pysyy heikennettynä.

<!-- S09 -->
Sekunnin kymmenyksen notkahdus
tarkoittaa nollaa.
Kahden kymmenyksen notkahdus tarkoittaa ykköstä.

<!-- S10 -->
Siinä koko idea.
Ei paketteja, ei verkkoa.
Vain radioaalto, joka notkahtaa
lyhyeksi aikaa tai vähän pidemmäksi.

<!-- S11 -->
Yksi bitti sekunnissa.
Eli pelkkien 60 bitin lähettämiseen
menisi kokonainen minuutti.

<!-- S12 -->
Ja itse asiassa se lähettää vain 59.

<!-- S13 -->
Jokaisen minuutin viimeisellä sekunnilla
aalto ei notkahda lainkaan.
Ja juuri se puuttuva notkahdus
on koko signaalin
tärkein osa.

<!-- S14 -->
Kun seuraava notkahdus tulee,
kello nimittäin tietää,
että uusi minuutti on juuri alkanut.

<!-- S15 -->
Aukko toimii kuin piste.
Kaikki kahden aukon välissä
on yksi kokonainen lause.

<!-- S16 -->
Mitä kaikkea mahtuu siis
59 bitin lauseeseen?

<!-- S17 -->
Minuutti. Tunti.
Kuukaudenpäivä, viikonpäivä,
kuukausi ja vuosi.

<!-- S18 -->
Useimmat luvut lähetetään numero kerrallaan.
47 minuuttia
ei lähde lukuna 47.
Se lähetetään kahtena erillisenä numerona,
nelosena ja seitsemänä.

<!-- S19 -->
4 bittiä riittää mille tahansa numerolle
nollasta yhdeksään.
Minuuttien kymmenet eivät koskaan ylitä viittä,
joten ne saavat vain 3.

<!-- S20 -->
Ja vuosi saa vain kaksi numeroa.
Lähettimen kannalta
2026 on yksinkertaisesti 26.
Vuosisadan kello lisää itse.

<!-- S21 -->
Mutta radio ei ole puhdas kanava.
Moottori, puhelimen laturi,
halpa LED-lamppu...
mikä tahansa niistä voi sotkea notkahduksen.

<!-- S22 -->
Siksi jokaisen numerolohkon perään
tulee yksi ylimääräinen bitti, pariteettibitti.

<!-- S23 -->
Se valitaan niin, että ykkösten määrä
lohkossa on aina parillinen.

<!-- S24 -->
Jos häiriö kääntää yhden bitin,
määrästä tulee pariton,
ja kello tietää,
että jokin meni vikaan.

<!-- S25 -->
Mutta jos kaksi bittiä kääntyy,
määrä on taas parillinen,
ja virhe lipsahtaa läpi.

<!-- S26 -->
Siksi moni kello
ei luota yhteen minuuttiin.
Se odottaa vielä toisen kelvollisen.

<!-- S27 -->
Ja siksi itsensä asettaminen
voi kestää useita minuutteja,
ja huonona päivänä paljon kauemmin.

<!-- S28 -->
Siitä syntyy kummallinen ongelma.

<!-- S29 -->
Kello käyttää kokonaisen minuutin
kellonajan 10.48 keräämiseen.
Mutta sillä aikaa kun se kerää viestiä,
kello on vasta 10.47.

<!-- S30 -->
Milloin aika sitten oikeasti vaihtuu?

<!-- S31 -->
Viesti on nimittäin ilmoitus.
Se kertoo, paljonko kello on,
kun seuraava minuutti alkaa.

<!-- S32 -->
Kello lukee koko lauseen,
odottaa puuttuvan notkahduksen yli,
ja kun seuraava notkahdus tulee,
juuri se on täsmällinen hetki.

<!-- S33 -->
Bitit kertovat kellolle, mitä kello on.
Notkahdus kertoo milloin.

<!-- S34 -->
Mutta lauseessa on muutama sana enemmän
kuin pelkkä kellonaika.

<!-- S35 -->
Kaksi bittiä kertoo, onko Saksassa
talviaika vai kesäaika.

<!-- S36 -->
Ja kolmas on varoitus.
Koko tunnin ennen kellojen siirtoa
sen arvo on yksi.

<!-- S37 -->
Kellosi ei siis tarvitse tietää,
minä maaliskuun sunnuntaina
kelloja siirretään eteenpäin
tai minä lokakuun sunnuntaina taaksepäin.
Kukaan ei ole koskaan opettanut sille sääntöä.
Sille vain kerrotaan, tuntia etukäteen.

<!-- S38 -->
Jos Eurooppa joskus lopettaa kellojen siirtelyn,
varoitusta ei yksinkertaisesti enää koskaan tule.

<!-- S39 -->
Toinen bitti varoitti ennen karkaussekunnista,
ylimääräisestä sekunnista, joka lisättiin silloin tällöin,
koska Maan pyöriminen
ei pidä aikaa täydellisesti.
Siinä minuutissa saattoi olla 61 sekuntia.

<!-- S40 -->
Viimeinen lisättiin
vuoden 2016 lopussa.
Mutta lokakuussa 2026
maailman metrologiaviranomaiset
päättivät luopua karkaussekunneista.
20. toukokuuta 2027 alkaen
UTC kulkee keskeytyksettä.

<!-- S41 -->
Ja jokaisen minuutin
ensimmäiset 14 bittiä
eivät koske aikaa lainkaan.

<!-- S42 -->
Vuodesta 2006 niitä on käytetty myös
salattujen sääennusteiden välittämiseen
yhteensopiville sääasemille.

<!-- S43 -->
Eli signaali, joka asettaa herätyskellosi,
saattoi myös kertoa
jonkun toisen sääasemalle,
sataako torstaina.

<!-- S44 -->
Silti useimmat näistä kelloista
eivät kuuntele koko ajan.
Kuunteleminen kuluttaa paristoa,
joten moni yrittää kerran yössä,
aikaisin aamuyöstä.

<!-- S45 -->
Pitkät aallot tavoittavat kellon kahta reittiä:
maata pitkin
ja ylemmästä ilmakehästä heijastuen.
Pimeän tultua ylempi reitti muuttuu,
ja signaali kantaa usein pidemmälle.

<!-- S46 -->
Ja kello kolmelta yöllä
lähistöllä on yleensä vähemmän koneita, latureita ja valoja
peittämässä sitä.

<!-- S47 -->
Tarkistusten välillä
kello käy kvartsikiteen varassa,
joka voi heittää noin sekunnin päivässä.

<!-- S48 -->
Seuraavassa onnistuneessa tarkistuksessa
radio korjaa heiton.

<!-- S49 -->
Jopa kuuntelupaikalla on väliä.
Antenni on pieni ferriittisauva,
jonka ympärille on kierretty lankaa.

<!-- S50 -->
Se kuulee parhaiten, kun sauva on poikittain
lähettimen suuntaan nähden,
ei osoittaen sitä kohti.
Käännä kelloa,
ja heikko signaali voi kadota kokonaan.

<!-- S51 -->
Siksi yksi kello toimii hyllyllä,
mutta sama kello kahden metrin päässä
teräsbetoniseinän takana ei asetu koskaan.

<!-- S52 -->
Mistä lähetin sitten
saa aikansa?

<!-- S53 -->
PTB:ltä,
Saksan kansalliselta metrologialaitokselta,
joka ylläpitää atomikelloja.

<!-- S54 -->
Itse sekunti on määritelty
cesiumatomien avulla.
Yksi sekunti on tasan
9 192 631 770 värähdystä
niiden lähettämässä säteilyssä.

<!-- S55 -->
Yöpöydällä oleva halpa herätyskello
seuraa siis kirjaimellisesti
aikastandardia,
joka on määritelty cesiumatomien avulla.

<!-- S56 -->
Ei tosin täydellisesti.
Signaali kulkee valon nopeudella,
ja valoltakin kuluu noin 3 millisekuntia
jokaista 1 000:ta kilometriä kohden.

<!-- S57 -->
Vastaanotin lisää oman viiveensä,
eikä kellosi korjaa mitään niistä.
Sen ei tarvitsekaan.
Se näyttää vain sekunnit.

<!-- S58 -->
Yhdestä paikasta Frankfurtin läheltä
signaali tavoittaa kellot
jopa noin 2 000 kilometrin päässä.
Se on suurin osa Eurooppaa.

<!-- S59 -->
Sveitsillä oli oma lähettimensä,
nimeltään HBG, vuoden 2011 loppuun asti.
Sen antennit olisi pitänyt uusia,
liian harva käytti sitä,
ja sveitsiläiset kellot pystyivät yksinkertaisesti
kuuntelemaan sen sijaan Saksaa.

<!-- S60 -->
Muut pitivät omansa.
Britannialla, Ranskalla, Japanilla ja Kiinalla
on kaikilla omansa.

<!-- S61 -->
Ja Pohjois-Amerikassa WWVB
on lähettänyt Fort Collinsista vuodesta 1963,
ja aikakoodia vuodesta 1965.

<!-- S62 -->
Sama periaate, eri murre.
Nolla on kahden sekunnin kymmenesosan notkahdus.
Ykkönen kestää puoli sekuntia.

<!-- S63 -->
Ja yhden minuuttikohtaisen aukon sijaan
joka 10. sekunti tulee pidempi merkki,
kuin pilkut lauseessa.
Kaksi peräkkäin tarkoittaa uutta minuuttia.

<!-- S64 -->
Suurin ero on siinä,
mitä aikaa se lähettää.
Saksa lähettää Keski-Euroopan virallista aikaa,
jota suuri osa mantereesta käyttää.

<!-- S65 -->
Mutta Yhdysvallat
ulottuu usealle aikavyöhykkeelle.
Siksi WWVB lähettää yleisaikaa, UTC:tä,
ja sinä kerrot kellolle, missä olet.

<!-- S66 -->
Se ei lähetä edes kuukautta.
Vain päivän järjestysnumeron vuodessa,
1:stä 366:een.

<!-- S67 -->
Mikään näistä asemista
ei puhu samaa kieltä.
Saksaa varten tehty kello
ei saa Coloradosta mitään selvää.

<!-- S68 -->
Mutta Atlantin molemmin puolin
toistuu sama hiljainen rutiini.
Yö yön jälkeen pieni vastaanotin
tahdistaa itsensä atomiaikastandardiin
satojen tai tuhansien kilometrien päässä.

<!-- S69 -->
Joten tässä kysymys sinulle.
Jos kaikki radioaikamerkit
katoaisivat tänä yönä,
huomaisitko sitä edes?
Kerro kommenteissa.
