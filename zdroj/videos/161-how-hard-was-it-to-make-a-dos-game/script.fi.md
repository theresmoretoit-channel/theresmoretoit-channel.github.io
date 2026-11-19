<!-- S01 -->
Vuonna 1993 Doom-niminen peli
pyöri tietokoneella,
jossa oli 4 megatavua muistia.

<!-- S02 -->
Se on suunnilleen
yhden puhelimesi kuvan koko.

<!-- S03 -->
3D-kiihdytintä ei ollut.
Pääprosessori
hoiti kaiken piirtämisen.

<!-- S04 -->
Nykyään kehittäjä aloittaa pelimoottorista,
kuten Unitystä tai Unrealista,
joka huolehtii grafiikasta, äänestä,
muistista ja laitteistosta.

<!-- S05 -->
DOSissa kaikki se
oli kehittäjän ongelma.
Ja melko usein myös pelaajan.

<!-- S06 -->
Kuinka vaikeaa siis oli
tehdä peli DOSille?

<!-- S07 -->
Aloitetaan muistista,
koska muisti oli yhtä sotkua.

<!-- S08 -->
Alkuperäinen IBM PC vuodelta 1981
pystyi osoittamaan 1 megatavun muistia.

<!-- S09 -->
Mutta vain ensimmäiset
640 kilotavua
oli tarkoitettu ohjelmille.

<!-- S10 -->
Loput 384
oli varattu näyttömuistille,
laajennuskorteille ja BIOSille.

<!-- S11 -->
Yli vuosikymmenen ajan
DOS käynnisti ohjelmat tavallisesti
tuon alueen sisällä.
Kaikki sen yli vaati lisätyötä.

<!-- S12 -->
Siitä on peräisin kuuluisa lausahdus:
640K pitäisi riittää kenelle tahansa.

<!-- S13 -->
Sitä pidetään yleensä Bill Gatesin sanomana.
Mitään todistetta siitä, että hän olisi sanonut niin, ei ole,
ja hän kiistää sen.

<!-- S14 -->
1990-luvun alussa
PC:ssä oli 4 megatavua
tai 8.

<!-- S15 -->
Ja silti peli saattoi pysähtyä
sanoihin
"muisti ei riitä".

<!-- S16 -->
Muistin omistaminen
ja sen käyttäminen
olivat kaksi eri asiaa.

<!-- S17 -->
Yksi kiertotie oli niin sanottu expanded memory,
eli EMS.

<!-- S18 -->
64 kilotavun ikkuna
sijaitsi tuon ensimmäisen megatavun
yläosassa.
Sen läpi ohjelma näki
4 sivua lisämuistia,
kukin 16 kilotavua,

<!-- S19 -->
ja pystyi vaihtamaan ne toisiin,
kuin kääntäisit kirjan sivuja
paperiarkin reiän läpi.

<!-- S20 -->
Toinen tapa oli laajennettu muisti,
johon päästiin HIMEM-nimisellä ajurilla.

<!-- S21 -->
Ja juuri tässä
kehittäjän ongelmasta
tuli pelaajan ongelma.

<!-- S22 -->
Hiiren, CD-aseman
tai äänikortin ajurit
haukkasivat palan tuosta arvokkaasta muistista,
ellet onnistunut lataamaan niitä ylämuistiin.

<!-- S23 -->
Niinpä pelaajat oppivat muokkaamaan kahta tiedostoa,
CONFIG.SYS ja AUTOEXEC.BAT.

<!-- S24 -->
Yksi peli halusi EMS:n.
Toinen halusi sen pois päältä,
NOEMS-nimisellä asetuksella.
Ja kolmas tarvitsi jokaisen vapaan kilotavun.

<!-- S25 -->
Vuonna 1993 MS-DOS 6 toi
käynnistysvalikon.

<!-- S26 -->
Valitsit asetukset
sille pelille, jota halusit pelata,
ja tietokone käynnistyi juuri sitä peliä varten.

<!-- S27 -->
Joillekin kertyi lopulta
oma käynnistysvalinta
lähes jokaiselle heidän pelilleen.

<!-- S28 -->
Mutta siihen mennessä
isommat pelit olivat löytäneet
keinon kiertää DOSin rajat.

<!-- S29 -->
386:sta lähtien
prosessori itse pystyi toimimaan
32-bittisessä suojatussa tilassa,
ja tilaa oli jopa 4 gigatavulle.

<!-- S30 -->
Suojattua tilaa käsiteltiin
eräässä aiemmassa videossa.
DOS ei kuitenkaan osannut käyttää sitä.

<!-- S31 -->
Niinpä pelit toivat oman apurinsa,
DOS-laajentimen.
Tunnetuin oli DOS/4GW.

<!-- S32 -->
Se tuli suositun kääntäjän mukana,
Watcom C:n.

<!-- S33 -->
Kun peli käynnistyi,
DOS/4GW vaihtoi prosessorin
suojattuun tilaan,
jolloin peli pääsi käsiksi
muistiin DOSin rajan yli.

<!-- S34 -->
DOS oli yhä taustalla
ja tarjosi palveluja, kuten tiedostojen käsittelyn.
Mutta peli toimi nyt suojatussa tilassa,
ei perinteisenä DOS-ohjelmana.

<!-- S35 -->
Jos pelasit DOS-pelejä 1990-luvulla,
olet nähnyt sen nimen
vilahtavan ruudulla.

<!-- S37 -->
Sitten kuva.
Yhdessä yleisimmin käytetyistä VGA-tiloista,
nimeltään Mode 13h,
ruutu oli 320
kertaa 200 pikseliä,
256 värillä.

<!-- S38 -->
Jokainen pikseli oli yksi tavu.
Värittääksesi pikselin
kirjoitit muistiin luvun.
Ei grafiikkakirjastoa. Pelkkää muistia.

<!-- S39 -->
Koko ruutu vei
64 000 tavua.

<!-- S40 -->
Se on hieman alle 64 kilotavua,
tarpeeksi pieni mahtuakseen yhteen segmenttiin,
lohkoon, jonka 16-bittinen ohjelma
pystyi osoittamaan kerralla.
Kerrankin muisti oli sinun puolellasi.

<!-- S41 -->
Mutta jos piirrät suoraan
näkyvälle ruudulle,
pelaaja näkee puolivalmiita kuvia
ja kuva välkkyy.

<!-- S42 -->
Niinpä pelit piirsivät jokaisen ruudun
ensin piilotettuun puskuriin
ja kopioivat sitten valmiin kuvan
näyttömuistiin.

<!-- S43 -->
Vuonna 1991 Michael Abrash,
ohjelmoija ja kirjoittaja,
julkaisi paremman tavan.
Hän antoi sille nimen Mode X.

<!-- S44 -->
Se käytti VGA:n osaa,
johon useimmat ohjelmoijat
eivät olleet koskaan koskeneet.

<!-- S45 -->
Se antoi neliönmuotoiset pikselit
ja tilaa useammalle ruudulle
näyttömuistissa.

<!-- S46 -->
Peli piirsi kuvan ruutuun,
jota kukaan ei nähnyt,
ja toi sen sitten yksinkertaisesti näkyviin.
Mutta sen ohjelmointi oli paljon vaikeampaa.

<!-- S47 -->
Sitten oli ääni.
Ja ääni oli arpapeliä.

<!-- S48 -->
PC:n oma kaiutin
oli tehty piippaamaan.

<!-- S49 -->
Sitten tulivat äänikortit
ja muut äänilaitteet.
Mitkään kaksi niistä
eivät toimineet samalla tavalla.

<!-- S50 -->
AdLib, jossa oli musiikkia syntetisoiva
Yamahan piiri.
Sound Blaster, joka pystyi soittamaan myös
nauhoitettua ääntä.

<!-- S51 -->
Roland MT-32,
kallis laatikko, jossa oli rikkaammat soittimet.
Gravis UltraSound.

<!-- S52 -->
Niiden kaikkien tukeminen
tarkoitti eri ajurien kirjoittamista.

<!-- S53 -->
Ja pelin piti tietää,
missä kortti oli.
Sen portti, sen keskeytys
ja sen DMA-kanava.

<!-- S54 -->
Tavallinen vastaus Sound Blasterille
oli portti 220, IRQ 7, DMA 1.
Yleensä.

<!-- S55 -->
Jos yksikin oli väärin,
peli oli mykkä.
Tai se jumittui.

<!-- S56 -->
Vuonna 1991 John Miles -niminen ohjelmoija
julkaisi kirjaston,
joka keskusteli monien äänikorttien kanssa
yhden rajapinnan kautta.

<!-- S57 -->
Peli saattoi kirjoittaa äänikoodinsa kerran
ja antaa kirjaston hoitaa kortin.

<!-- S58 -->
Se oli taas yksi kerros
pelin ja laitteiston välissä.
Pidä se mielessä.

<!-- S59 -->
Ja sitten oli nopeus.
Ohjelmoijat laskivat
jokaisen prosessorin askeleen.

<!-- S63 -->
Löytääksesi pikselin ruudulta
kerrot sen rivin
luvulla 320.

<!-- S63b -->
Vanhemmilla prosessoreilla
kertolasku saattoi olla kallis.

<!-- S64 -->
Mutta 320
on 256
plus 64.
Molemmat ovat kahden potensseja.

<!-- S65 -->
Joten voit korvata kertolaskun
kahdella bittisiirrolla ja yhteenlaskulla.

<!-- S67 -->
Chris Sawyer meni aivan konepellin alle.
Hän kirjoitti Transport Tycoonin vuonna 1994
lähes kokonaan assemblyllä,

<!-- S68 -->
eli käskyillä,
joita prosessori itse ymmärtää,
yksi kerrallaan.

<!-- S69 -->
Ja joskus
kaikki tämäkään ei riittänyt.

<!-- S70 -->
Vuonna 1990 Wing Commanderissa oli bugi,
jota tiimi ei löytänyt,
ja takaraja lähestyi.

<!-- S71 -->
Kun lopetit pelin,
muistinhallinta kaatui
virheilmoitukseen.

<!-- S72 -->
Niinpä ohjelmoija Ken Demarest
avasi muistinhallinnan
heksaeditorissa
ja muutti ilmoituksen tekstin.

<!-- S73 -->
Nyt siinä luki:
"Kiitos, että pelasit Wing Commanderia."

<!-- S74 -->
Sitten tiimi löysi oikean bugin,
eikä vitsi koskaan päätynyt julkaistuun peliin.

<!-- S74b -->
Jotkut pelaajat ovat yhä varmoja, että näkivät sen.
Ja myöhemmät Originin pelit
todella hyvästelivät juuri niin.

<!-- S75 -->
Mikä tuo meidät takaisin Doomiin.

<!-- S76 -->
Doom käytti DOS/4GW:tä
ja toimi 32-bittisenä ohjelmana.

<!-- S77 -->
Liukulukulaskentaa tukevaa laitteistoa
ei ollut taattu joka PC:ssä.

<!-- S78 -->
Niinpä Doom käytti kiintolukuaritmetiikkaa.
Kokonaislukuja,
joiden alimmat 16 bittiä
edustivat murto-osaa.

<!-- S79 -->
Eikä sen maailma ollut
oikeasti kolmiulotteinen.

<!-- S80 -->
Jokainen kenttä on litteä pohjapiirros,
jossa on korkeus jokaiselle lattialle
ja jokaiselle katolle.

<!-- S81 -->
Huone ei voi koskaan olla toisen yläpuolella.
Etkä voi kunnolla katsoa ylös tai alas.

<!-- S82 -->
Ennen kuin kenttää pystyi pelaamaan,
työkalu pilkkoi kartan
binääripuuksi, BSP:ksi.

<!-- S83 -->
Moottori käy puun läpi
edestä taaksepäin,
pelaajan puolelta alkaen,
ja ohittaa alueet, joita ei voi nähdä.

<!-- S84 -->
Eikä Doomia edes kirjoitettu DOSilla.

<!-- S85 -->
id Software rakensi sen
NeXT-työasemilla
ja käänsi lopputuloksen DOSille.

<!-- S86 -->
Doom ei ollut yleiskäyttöinen 3D-moottori.
Se oli rakennettu täsmälleen
yhdenlaiselle maailmalle.
Juuri se erikoistuminen
auttoi sitä toimimaan 386:lla.

<!-- S87 -->
Ja muut studiot halusivat sen maailman.

<!-- S88 -->
Raven Software lisensoi Doomin moottorin
Hereticiin vuonna 1994
ja Hexeniin vuonna 1995.

<!-- S89 -->
Doom auttoi vakiinnuttamaan
uuden tavan tehdä pelejä.
Studiot saattoivat lisensoida valmiin moottorin
sen sijaan, että rakentaisivat kaiken alusta.

<!-- S90 -->
Muistilaajennin.
Äänikirjasto.
Lisensoitu moottori.

<!-- S91 -->
Jokainen niistä vei yhden ongelman
kehittäjän harteilta.
Ja kerroksia kertyi lisää,
kunnes niistä tuli ne moottorit,
joista kehittäjät nykyään aloittavat.

<!-- S92 -->
Oliko pelien tekeminen siis ennen vaikeampaa?
Monella tapaa kyllä.

<!-- S93 -->
Mutta vaikeus ei kadonnut.
Se siirtyi.

<!-- S94 -->
Nykyään kehittäjät painivat
gigatavujen resurssien
ja miljoonien polygonien kanssa
muutaman sadan kilotavun sijaan.

<!-- S95 -->
DOSissa jopa pelaajan
piti tietää, minne muisti katosi.

<!-- S96 -->
Tässä sinulle kysymys.
Muistatko, kun rakensit
käynnistysvalikon vain saadaksesi yhden pelin toimimaan?
Oliko se tuskaa,
vai puolet hauskuudesta?
Kerro kommenteissa.
