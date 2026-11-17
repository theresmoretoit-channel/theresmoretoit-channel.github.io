<!-- S01 -->
Kuvittele, että käynnistät Windows-koneen
etkä löydä tehtäväpalkkia, Käynnistä-painiketta
etkä ainuttakaan kuvaketta työpöydältä.

<!-- S02 -->
Sen sijaan ylhäällä on ohut palkki,
valikko, joka aukeaa mihin tahansa napsautatkin,
ja neljä virtuaalista työpöytää rinnakkain.

<!-- S03 -->
Se näyttää Linuxilta.
Mutta ohjelmasi, ajurisi ja tiedostosi
ovat juuri siellä, mihin ne jätit.
Se on yhä Windows.

<!-- S04 -->
Vain työpöytä on vaihtunut.
Ja kytkin, joka sen vaihtaa,
on yksi ainoa asetus.

<!-- S05 -->
Windows pitää sitä rekisterissä,
arvossa nimeltä Shell.
Lähes jokaisessa Windows-koneessa
siinä lukee explorer.exe.

<!-- S06 -->
Kirjoita siihen toisen ohjelman nimi,
kirjaudu ulos ja takaisin sisään,
niin Windows käynnistääkin tuon ohjelman.
Mitä se piirtää, siitä tulee työpöytäsi.

<!-- S07 -->
Eikä tämä ole kenenkään viime vuonna keksimä temppu.
Vuonna 1990 Windows 3.0:ssa oli sama kytkin
tavallisessa tekstitiedostossa nimeltä system.ini.
Yksi rivi: shell=progman.exe.

<!-- S08 -->
Jos sen nimen vaihtoi,
Järjestelmänhallinta, kuvakeryhmiä täynnä oleva ikkuna,
ei tullut näkyviin lainkaan.

<!-- S09 -->
Kysymys ei siis ole, voiko Windowsissa
olla toinen työpöytä.
Aina on voinut.
Kysymys on, miksi lähes kukaan ei ole nähnyt sellaista.

<!-- S10 -->
Aloitetaan siitä, mihin tuo rivi oikeastaan osoittaa.
Tehtäväpalkki, työpöydän kuvakkeet,
pieni ilmoitusalue kellon vieressä:
kaikki se on yksi ohjelma, explorer.exe.

<!-- S11 -->
Kyllä, sama explorer.exe,
jonka avaat Resurssienhallintana tiedostojen selaamista varten.
Se tekee kahta työtä,
ja useimmat huomaavat niistä vain toisen.

<!-- S12 -->
Sillä toisella työllä on nimi: kuori.
Se on kerros, jota kosketat.
Sen alla ovat ydin, ajurit
ja palvelut, jotka pitävät Windowsin käynnissä.

<!-- S13 -->
Mikään niistä ei tarvitse tehtäväpalkkia.
Lopeta explorer.exe Tehtävienhallinnassa,
niin tehtäväpalkki ja kuvakkeet katoavat...
mutta Muistio, selaimesi
ja kaikki muut ikkunat toimivat edelleen.

<!-- S14 -->
Käynnistä se uudelleen, ja työpöytä palaa.
Tuskin on selvempää todistetta siitä,
että työpöytä on vain yksi ohjelma muiden joukossa.

<!-- S14b -->
Jos olet joskus vaihtanut aloitusnäyttösovellusta
Android-puhelimessa,
olet nähnyt samantapaisen idean.
Androidissa se on tavallinen asetus.
Windowsissakin mekanismi on,
mutta tavalliset käyttäjät eivät ole koskaan saaneet
siihen yksinkertaista painiketta.

<!-- S15 -->
Tässä sekoittuu kolme käsitettä.
Kuori on se, mistä käynnistät asioita:
tehtäväpalkki, valikot, työpöytä.
Ikkunamanageri hallitsee, miten ikkunat
sijoittuvat, pinoutuvat ja saavat kohdistuksen.
Työpöytäympäristö
kokoaa koko käyttökokemuksen yhteen.

<!-- S16 -->
Linuxissa näitä osia voi yhdistellä
monella eri tavalla.
Windowsissa kuoren vaihtaminen
ei vaihda järjestelmän ikkunanhallintaa
eikä sitä, miten sovellukset piirtävät ikkunoidensa kehykset.

<!-- S17 -->
Se ei estänyt ihmisiä yrittämästä.
90-luvun alussa saattoi kävellä kauppaan
ja ostaa korvaajan Järjestelmänhallinnalle.

<!-- S18 -->
Norton Desktop for Windows
antoi sinulle oman työpöydän,
omat tiedostotyökalut ja oman käynnistimen,
saman Windowsin päällä kuin ennenkin.

<!-- S19 -->
Jotkut tietokonevalmistajat vaihtoivat sen
jo ennen kuin asiakas edes käynnisti koneen.
Packard Bellin Navigator tervehti ostajia
talolla, jonka läpi saattoi kulkea huone kerrallaan.

<!-- S20 -->
Sitten Windows 95 antoi tehtävän explorer.exelle,
ja system.ini-tiedoston rivi
muuttui yksinkertaisesti muotoon explorer.exe.
Kytkin pysyi täsmälleen paikallaan.

<!-- S21 -->
90-luvun lopulla
tuon kytkimen ympärille kasvoi kokonainen yhteisö.
Tunnetuin projekti oli LiteStep.

<!-- S22 -->
Se lainasi ulkoasunsa AfterStepiltä,
Unix-ikkunamanagerilta, jonka esikuva oli NeXTSTEP.
NeXTSTEPin kehitti Steve Jobsin Applen jälkeen perustama yhtiö.

<!-- S23 -->
LiteStepissä ei ollut Käynnistä-valikkoa, ellet rakentanut sellaista.
Kaikki oli moduuli:
telakka täällä, kello tuolla,
valikko, joka aukesi minne tahansa napsautit hiiren oikealla.

<!-- S24 -->
Teemoja jaettiin kuin taustakuvia.
Jotkut näyttivät futuristisilta.
Jotkut näyttivät Unix-työasemalta.
Jotkut jättivät näytölle tuskin mitään.

<!-- S25 -->
Blackbox for Windows lähti toiseen suuntaan.
Se kopioi Blackboxin, minimalistisen Unix-ikkunamanagerin,
yhtä ainoaa yksinkertaista valikkoa
ja kapeaa työkalupalkkia myöten.

<!-- S26 -->
Sen seuraaja bbLean
piti idean hengissä Windows 2000:ssa ja XP:ssä.

<!-- S27 -->
Emerge Desktop pilkkoi kuoren erillisiin osiin:
käynnistin, ilmoitusalue, tehtäväluettelo,
jokainen pieni ohjelma, jonka saattoi pitää tai jättää pois.

<!-- S28 -->
Miksi nähdä niin paljon vaivaa?
Osittain siksi, että XP:n ulkoasu
oli helppo tunnistaa ja vaikea muuttaa.
Teemat muuttivat värejä ja painikkeita.
Asettelu pysyi.

<!-- S29 -->
Osittain muistin takia.
Koneessa, jossa oli 128 megatavua,
kevyempi kuori lupasi enemmän tilaa
kaikelle muulle.

<!-- S30 -->
Ja osittain Linuxin takia.
Siellä työpöydän valitseminen oli tavallista,
ja jotkut Windows-käyttäjät halusivat
saman valinnanvapauden.

<!-- S31 -->
Useimpia noista projekteista ei enää ole.
LiteStepin viimeinen julkaisu oli esiversio
vuodelta 2014, yhä alfaksi merkitty.
Myös Emerge Desktop ja SharpEnviro loppuivat.

<!-- S32 -->
Osasyy oli pienissä vapaaehtoistiimeissä.
Mutta myös Windows muuttui.
Vuosien mittaan sen työpöydästä tuli paljon enemmän
kuin yksi suoritettava tiedosto.

<!-- S33 -->
Työpöytäkokemus on nykyään hajautettu
useisiin prosesseihin,
järjestelmäkomponentteihin ja paketoituihin sovelluksiin.
Jopa Käynnistä-valikko toimii omana ohjelmanaan.

<!-- S34 -->
explorer.exen korvaaminen ei tarkoita, että korvaisi
kaiken, mistä nykyaikainen Windowsin käyttöliittymä koostuu.
Ja se on yksi syy siihen, miksi
täydellisen vaihtoehtoisen työpöydän rakentaminen
on vaikeampaa kuin ennen.

<!-- S35 -->
Ja silti se toimii yhä.
Cairo Desktop, avoimen lähdekoodin projekti,
toimii nykyään Windows 11:ssä.

<!-- S36 -->
Se tuo oman valikkopalkin yläreunaan,
oman tehtäväpalkin
ja kansioita, jotka voit kiinnittää palkkiin pinoina.

<!-- S37 -->
Se voi toimia explorer.exen rinnalla
tai ottaa kuoren paikan.
Siinä jälkimmäisessä tilassa
osa Windows 11:stä voi temppuilla,
muun muassa Asetukset ja Windowsin suojaus.

<!-- S38 -->
Seelen UI tekee sen toisin.
Se ei korvaa explorer.exeä.
Se piilottaa tehtäväpalkin ja tuo omat osansa:
telakan, palkin, widgetit
ja ikkunamanagerin, joka asettelee ikkunasi vierekkäin.

<!-- S39 -->
Lopputulos voi näyttää aivan muulta kuin Windowsilta.
Mutta pinnan alla explorer.exe on yhä käynnissä.
Se on uudet kasvot, ei uusi kuori.

<!-- S40 -->
Entä Microsoft?
Sillä on itse asiassa tähän virallinen ominaisuus.
Sen nimi on Shell Launcher,
ja se on tarkoitettu esimerkiksi kioskilaitteisiin.

<!-- S41 -->
Olet luultavasti käyttänyt jotain sellaista
tietämättäsi.
Aseman lippuautomaatti.
Itsepalvelukassa. Pankkiautomaatti.

<!-- S42 -->
Moni niistä on Windows-tietokone,
jonka koko kuori on yksi sovellus.
Ylläpitäjä nimeää ohjelman,
ja kirjautumisen jälkeen se ohjelma on koko työpöytä.

<!-- S43 -->
Mutta se on saatavilla vain
Enterprise-, Education-
ja IoT Enterprise -versioissa.

<!-- S44 -->
Ja vanhempi rekisterimekanismi
on yhä osa Windowsia.
Microsoft ei vain koskaan tehnyt siitä
tavallista työpöytäasetusta
tavallisille käyttäjille.

<!-- S45 -->
Miksi Windowsissa siis näyttää olevan vain yksi työpöytä?
Ei siksi, ettei siinä voisi olla toista.
Vaan siksi, että työpöytä on tuote.

<!-- S46 -->
Linuxissa työpöytä on valinta.
Jotkut jakelut pyytävät sinua valitsemaan sellaisen
jo asennuksen aikana.
KDE Plasma, GNOME, Xfce, Cinnamon...

<!-- S47 -->
Windowsissa työpöytä on se, mitä Microsoft näyttää
jokaisessa mainoksessa, jokaisessa kuvakaappauksessa
ja jokaisella tukisivulla.
Yksi työpöytä tarkoittaa yhtä ohjeistusta
yli miljardille koneelle.

<!-- S48 -->
Se on todellinen etu.
Kun jokin hajoaa,
ohjeartikkelin näyttökuva näyttää samalta kuin sinun näyttösi.
Hintana on, että useimmat eivät koskaan saa tietää,
että valinnanvaraa oli.

<!-- S49 -->
Ihmiset vaihtoivat Windowsin työpöytää
jo ennen kuin Windows 95:tä edes oli.
He rakensivat telakoita, riisuttuja valikoita
ja työpöytiä, jotka eivät muistuttaneet mitään muuta.

<!-- S50 -->
Useimmat noista projekteista ovat poissa.
Idea ei ole.
Jokaisen koskaan napsauttamasi tehtäväpalkin alla
on yhä se yksi asetus, odottamassa toista nimeä.

<!-- S51 -->
Työpöytä on vain yksi ohjelmisto muiden joukossa.
Ja ohjelmiston voi vaihtaa.

<!-- S52 -->
Joten tässä sinulle kysymys.
Jos Windows antaisi sinun valita työpöydän
asennuksen aikana, kuten jotkut Linux-jakelut,
vaihtaisitko, vai pitäisitkö sen, jonka tunnet?
Kerro kommenteissa.
