<!-- S01 -->
Yrität poistaa tiedoston.
Tietokone sanoo, että se on auki
toisessa ohjelmassa.
Muttei kerro, missä.

<!-- S02 -->
Tuo viesti on vain näkyvä osa
paljon oudommasta kysymyksestä.
Mitä tiedoston avaaminen
oikeastaan tarkoittaa?

<!-- S03 -->
Sillä toisella tietokoneella
sama tiedosto, samalla tavalla auki,
poistuu ilman yhtään valitusta.

<!-- S04 -->
Sama tiedosto.
Sama toimenpide.
Kaksi täysin eri vastausta.

<!-- S05 -->
Aloitetaan siitä,
mikä ärsyttää kaikkia.
Mikä ohjelma?

<!-- S06 -->
Windows tietää sen.
Sillä on ytimen olio
tuolle avoimelle tiedostolle,
ja se tietää omistavan prosessin.
Se voisi kertoa nimen.

<!-- S07 -->
Niinpä suljet ohjelmia summamutikassa.
Avaat Tehtävienhallinnan.
Tuijotat prosessilistaa
etkä tunnista niistä juuri mitään.

<!-- S08 -->
Ja vuosikausia
vastaus tosiaan oli
ladata erillinen työkalu.
Unlocker ilmestyi vuonna 2005,
ja Windows XP:ssä se oli vastaus.

<!-- S09 -->
Sitten Windows 7 toi
Resurssienvalvonnan.
Suoritin-välilehden.
Listan nimeltä Liittyvät kahvat.

<!-- S10 -->
Kirjoita tiedoston nimi.
Se antaa sinulle ohjelman
ja prosessin tunnuksen.
Mitään ei tarvitse asentaa.
Se on ollut siellä vuodesta 2009.

<!-- S10b -->
Mutta erilliset työkalut tekivät
enemmän kuin vain kertoivat.
Ne osasivat sulkea kahvan
ja vapauttaa tiedoston.

<!-- S11 -->
Mikä tuo meidät takaisin
kysymykseen.
Mitä se ohjelma sai,
kun se avasi tiedoston?

<!-- S12 -->
Sanotaan, että soitin avaa
tiedoston nimeltä movie.mp4.
Windowsissa tiedoston avaaminen
tarkoittaa kahden asian määrittämistä.

<!-- S13 -->
Ensimmäinen on itsestään selvä.
Mitä minä haluan sillä tehdä?
Lukea sitä. Kirjoittaa siihen.

<!-- S14 -->
Toinen on se kiinnostava.
Mitä kaikki muut saavat tehdä
sillä aikaa kun se on minulla auki?

<!-- S15 -->
Se on oikea asetus.
Sinä kerrot, mitä muut ohjelmat
saavat tehdä sillä aikaa kun pidät sitä.

<!-- S16 -->
Ne saavat lukea sitä.
Ne saavat myös kirjoittaa siihen.
Ne saavat poistaa sen tai nimetä uudelleen.

<!-- S16b -->
Tai sitten ei mitään.
Kukaan ei koske siihen
sillä aikaa kun minä käytän sitä.

<!-- S17 -->
Poistamisen salliva lippu
on nimeltään FILE_SHARE_DELETE.
Ja Microsoftin dokumentaatio
lisää sen alle yhden rivin.

<!-- S18 -->
Poisto-oikeus kattaa
sekä poistamisen että uudelleennimeämisen.

<!-- S19 -->
Eli ohjelma, joka kieltäytyy
jakamasta poisto-oikeutta,
on estänyt myös uudelleennimeämisen.

<!-- S20 -->
Ja jos tiedoston avannut ohjelma
ei myöntänyt sitä,
kukaan muu ei voi sitä ottaa.

<!-- S21 -->
Siksi virheen nimi
ei ole tiedosto varattu.
Sen nimi on jakamisvirhe.

<!-- S22 -->
Vastaus oli koko ajan
itse virheen
nimessä.

<!-- S23 -->
Nyt sama asia
Linux-koneella.
Soitin avaa videon.

<!-- S24 -->
Ja sinä kirjoitat
rm movie.mp4.

<!-- S24b -->
Se toimii.
Video jatkaa soimistaan.

<!-- S25 -->
Mitä se ohjelma siis sai,
jos ei mitään mistä pitää kiinni?

<!-- S26 -->
Tässä on tämän videon
koko idea.
Nimi ei ole tiedosto.

<!-- S27 -->
movie.mp4 on rivi
hakemistossa.
Se rivi osoittaa olioon,
jossa varsinainen data on.

<!-- S28 -->
Kun ohjelma avaa tiedoston,
se saa viittauksen
olioon.
Ei riviin.

<!-- S29 -->
Tiedoston poistaminen
poistaa siis rivin.
Olioon ei kosketa.

<!-- S30 -->
Manuaalisivu sanoo sen
yhdellä lauseella.
Tiedosto on olemassa edelleen,
kunnes viimeinen siihen viittaava
tiedostokuvaaja on suljettu.

<!-- S31 -->
Se kuulostaa abstraktilta,
kunnes sen näkee tapahtuvan.
Tein siis lokitiedoston,
jonka koko oli viisisataa megatavua,
ja jätin yhden prosessin pitämään sitä auki.

<!-- S31b -->
Sitten poistin sen.

<!-- S32 -->
Hakemiston listaus
ei näytä yhtään mitään.
Työkalu, joka mittaa
kansion koon, sanoo nolla.

<!-- S33 -->
Ja työkalu, joka mittaa
levyn vapaan tilan,
sanoo, että viisisataa megatavua
on yhä poissa.

<!-- S33b -->
Tyhjä kansio.
Puoli gigatavua kadonnut.

<!-- S34 -->
Tätä sattuu niin usein,
että tällaisten tiedostojen etsimiseen
on oma komentonsa.
Poistettu, näkymätön, yhä levyllä.

<!-- S35 -->
Ja tila palaa
sillä hetkellä, kun se yksi prosessi
päästää tiedostosta irti.

<!-- S36 -->
Sama logiikka pätee uudelleennimeämiseen.
Siirrä tiedosto sen ollessa auki,
eikä ohjelma huomaa mitään.

<!-- S37 -->
Manuaali on siitäkin suorasukainen.
Vanhan polun avoimet tiedostokuvaajat
eivät muutu miksikään.

<!-- S37b -->
Se ei koskaan käyttänyt nimeä.

<!-- S38 -->
Tällä on yksi rajoitus,
joka kannattaa tietää.
Käynnissä olevaa ohjelmaa
ei voi korvata suoraan.

<!-- S38b -->
Linux kieltäytyy.
Text file busy.

<!-- S39 -->
Se mitä voit tehdä,
on irrottaa nimi
ja luoda tilalle uusi tiedosto.

<!-- S40 -->
Vanha prosessi jatkaa käyntiään
oliosta käsin,
jolla ei enää ole mitään nimeä.
Kaikki myöhemmin käynnistetty saa uuden.

<!-- S41 -->
Ja taas sama ajatus,
joka todistaa itsensä oikeaksi.
Monia asioita voi vaihtaa
koskematta itse olioon.

<!-- S41b -->
Siksi Linux voi päivittää
ohjelman sen ollessa käynnissä.
Uutta versiota et vain saa,
ennen kuin käynnistät sen uudelleen.

<!-- S42 -->
Onko Windows siis
yksinkertaisesti huonommin suunniteltu?

<!-- S42b -->
Ei.
Ja tämä on se osa,
jota tuskin kukaan tuntee.

<!-- S43 -->
Windowsilla on tapa
tehdä täsmälleen sama asia.

<!-- S43b -->
NTFS:llä Windows voi pyytää
POSIX-tyylistä poistoa.

<!-- S44 -->
Microsoft kuvaa,
mitä silloin tapahtuu.
Nimi poistetaan
näkyvästä nimiavaruudesta.

<!-- S45 -->
Ja sovellukset, joilla tiedosto
oli jo auki, voivat yhä käyttää sitä,
vaikka nimeä,
jolla ne avasivat sen, ei enää ole.

<!-- S46 -->
Se on Unixin toimintatapa.
NTFS:llä.
Microsoftin dokumentoimana.

<!-- S47 -->
Kumpikin järjestelmä osaa molemmat.
Ero on oletusasetuksessa.
Siinä mitä saat, kun avaat tiedoston
etkä ajattele asiaa lainkaan.

<!-- S48 -->
Windowsissa saat sopimuksen.
Unixissa saat viittauksen
olioon.

<!-- S49 -->
Mikä kuulostaa kysymykseltä
ohjelmoijille,
kunnes on nähnyt
juuri tämän viestin.

<!-- S50 -->
Käynnistä tietokone uudelleen,
jotta päivitysten asennus valmistuu.

<!-- S51 -->
Oletetaan, että Windowsin pitää vaihtaa
kirjasto, jota käynnissä oleva prosessi
pitää auki tiukan sopimuksen mukaisesti.

<!-- S52 -->
Se ei voi vaihtaa tiedostoa
sen prosessin alta.
Jonkin on siis päästettävä irti.

<!-- S53 -->
Sulje sovellus.
Pysäytä palvelu.
Tai anna koko homma
uudelleenkäynnistyksen hallinnalle.

<!-- S54 -->
Se on oikea järjestelmäkomponentti.
Se sammuttaa asiat järjestyksessä.
Windows-sovellukset,
sitten konsoliohjelmat,

<!-- S55 -->
sitten palvelut,
ja Resurssienhallinta viimeisenä.
Sitten se käynnistää ne taas.

<!-- S56 -->
Ja se on olemassa yhdestä syystä,
jonka Microsoft sanoo suoraan
omassa dokumentaatiossaan.

<!-- S57 -->
Pääsyy siihen,
että ohjelmistojen asennukset
ja päivitykset vaativat
järjestelmän uudelleenkäynnistyksen...

<!-- S58 -->
on se, että osa päivitettävistä
tiedostoista on juuri silloin
käynnissä olevan sovelluksen
tai palvelun käytössä.

<!-- S59 -->
Olisi liian siistiä lopettaa tähän.
Jakamissäännöt eivät ole ainoa syy,
miksi kone pyytää uudelleenkäynnistystä.

<!-- S60 -->
Ytimen päivitys on eri asia.
Ydintä ei voi vaihtaa
sen itsensä alta.

<!-- S61 -->
Linuxissa on sama ongelma,
vaikka live-päivitys
joskus välttääkin uudelleenkäynnistyksen.

<!-- S62 -->
Rehellinen versio väittää
siis vähemmän
kuin tyydyttävä versio.

<!-- S63 -->
Tapa, jolla Windows kohtelee käytössä
olevia tiedostoja, teki joistakin osista
vaikeampia vaihtaa ajon aikana,
ja se vaikutti asiaan.

<!-- S64 -->
Sillä jokaisella suunnitteluvalinnalla
on jossain seurauksensa.

<!-- S65 -->
Windows antaa tiedoston avaavan
ohjelman päättää,
mitä muut saavat sillä tehdä.

<!-- S66 -->
Hintana on se, että joskus
et voi poistaa omaa tiedostoasi,
koska toinen ohjelma
ei sallinut sitä.

<!-- S67 -->
Unix pitää nimen
ja olion erillään,
joten monia asioita voi vaihtaa
järjestelmän ollessa käynnissä.

<!-- S68 -->
Hintana on puoli gigatavua,
joka katosi levyltä
eikä kuulu millekään tiedostolle.

<!-- S69 -->
Ja katso, miten kumpikin
näistä ratkeaa.
Windowsissa yksi ulospääsy on
sulkea ohjelma,
joka pitää tiedostoa.

<!-- S70 -->
Linuxissa yksi tapa
saada se tila takaisin
on käynnistää uudelleen palvelu,
jolla tiedosto on yhä auki.

<!-- S71 -->
Eri syyt.
Joskus sama lääke.

<!-- S71b -->
Muuten, jos haluat nähdä,
minne seuraava kysymys meidät vie,
harkitse tilaamista.
Se auttaa kanavaa paljon.

<!-- S72 -->
Eli. Alun kysymys.
Mitä tiedoston avaaminen
tarkoittaa?

<!-- S73 -->
Se tarkoittaa, että pidät jotakin.
Nämä kaksi järjestelmää vain antavat
käteesi eri asiat.

<!-- S74 -->
Siksi tuo viesti
ei oikeastaan koskaan sanonut,
ettei tätä tiedostoa voi poistaa.

<!-- S75 -->
Se sanoi, ettei sen avannut
ohjelma
antanut sinulle lupaa.

<!-- S75b -->
Ja se tietää, mikä ohjelma se on.
Se vain ei maininnut sitä.
