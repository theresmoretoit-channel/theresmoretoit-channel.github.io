<!-- S01 -->
Představ si, že máš bláznivý nápad.
Chceš si postavit vlastní družici.
Ne komunikační družici
za miliardu dolarů.
Něco malého.

<!-- S02 -->
Krabičku velkou zhruba
jako bochník chleba.
Uvnitř: počítač, solární panely,
rádio, pár senzorů.
Možná i kameru.

<!-- S03 -->
Postavíš ji v garáži.
A pak nějak...
ji dostaneš na oběžnou dráhu.
Zní to nemožně.
Ale jde to.

<!-- S04 -->
Lidé dělají skoro přesně tohle
už léta.
Říká se jim CubeSaty.

<!-- S05 -->
A překvapivé je,
že to nejtěžší
není postavit tu družici.
Je to všechno ostatní.

<!-- S06 -->
Základní jednotka se jmenuje 1U —
zhruba deseticentimetrová krychle.
Skládáním jednotek
dostaneš 2U, 3U, 6U
i větší.

<!-- S07 -->
Princip je jednoduchý.
Místo navrhování nové družice
od nuly
použiješ standardní rozměry
a standardní rozhraní.
A vesmír je najednou otevřený
univerzitám, startupům
a možná i tobě.

<!-- S07b -->
Mimochodem, jestli se ti takováhle
videa líbí, můžeš se přihlásit k odběru.

Kanálu to opravdu pomůže.

<!-- S08 -->
Co by naše malá družice
vlastně obsahovala?
Nejdřív potřebuje počítač.
Něco musí spouštět software,
řídit hardware
a rozhodovat, co dělat.

<!-- S09 -->
Pak napájení.
Solární panely vyrábějí elektřinu.
Baterie ji ukládají
na chvíli, kdy družice
sklouzne do stínu Země.

<!-- S10 -->
Pak komunikace.
Rádio. Anténa.
A dole na Zemi
naslouchající pozemní stanice.

<!-- S11 -->
Pak senzory.
Teplota. Napětí. Proud.
Zrychlení. Magnetické pole.
A nějak zjistit,
kam družice míří.
Protože na oběžné dráze
je určit "nahoru" překvapivě těžké.

<!-- S12 -->
Ale než ji postavíme,
přijde nepříjemná otázka.
Kolik ta krabička stojí?
Odpověď zní...
víc, než by se zdálo.

<!-- S13 -->
Jednoduchý 1U CubeSat
může snadno stát
desítky tisíc dolarů —
jen za letový hardware.
Napájení. Solární panely.
Baterie. Počítač. Rádio.
Řízení orientace. Konstrukce.
A užitečné zatížení.

<!-- S14 -->
Pak přijdou věci,
které nejsou na seznamu dílů.
Testování. Integrace.
Dokumentace.
Provoz pozemní stanice.
Licence.
A nakonec...
start.

<!-- S15 -->
Svezení pro malý CubeSat
může stát desítky tisíc.
U větších misí a větších CubeSatů
se cena vyšplhá na stovky tisíc.
A to je jen za to,
dostat ho do vesmíru.

<!-- S16 -->
A teď
ještě absurdnější problém.
Vzpomínáš na všechny ty díly?
Jak se to všechno proboha
vejde do jedné malé krabičky?

<!-- S17 -->
Ve vesmíru není místo
na náhodnou hromadu elektroniky.
Záleží na každém centimetru.
Záleží na každém gramu.
Záleží na každém wattu.
Družice je trojrozměrné puzzle,
které musí přežít start rakety.

<!-- S18 -->
Kde tedy vezmeš
všechny ty díly?
Nemusíš navrhovat
všechno sám.
Existuje celý průmysl,
který prodává díly pro malé družice:
počítače, napájení,
rádia, antény a solární panely.
Existují dokonce tržiště
přímo pro díly CubeSatů.

<!-- S18b -->
A díly jsou navíc standardizované.
Mnohé sdílejí jeden formát desky
a prostě se skládají na sebe,
takže kusy od různých výrobců
zapadnou do jednoho celku.
Firmy jako EnduroSat
a GomSpace je prodávají
a jeden subsystém může stát
od pár tisíc
po desítky tisíc dolarů.

<!-- S19 -->
A nejsou to
žádné exotické procesory.
Jeden současný počítač CubeSatu
používá ARM Cortex-M7
se známými rozhraními —
SPI, I²C, UART a CAN.

<!-- S19b -->
A není to žádný speciální vesmírný čip.
Je to skutečná, běžně dostupná deska,
kterou můžeš vzít do ruky.

<!-- S20 -->
Družice potřebuje něco
důležitějšího než hrubý výkon:
předvídatelné chování,
nízký příkon a spolehlivost.
Náročnější mise
můžou použít procesory ARM Cortex-A —
a dokonce Linux.

<!-- S20b -->
Ale není rychlý.
Typický počítač CubeSatu
běží na pár set megahertzech.
Tvůj notebook běží
na čtyřech pěti gigahertzech
a má mnohem víc jader.
Vyměňuje hrubý výkon
za skoro nulovou spotřebu.

<!-- S21 -->
A jestli jsi programátor,
tady to začíná být zajímavé.
Nepíšeš
žádný tajemný "vesmírný jazyk".
Píšeš embedded software.
Často v C nebo C++.

<!-- S22 -->
Může běžet přímo
na hardwaru,
nebo na operačním systému reálného času,
jako FreeRTOS, Zephyr nebo RTEMS.
Existují dokonce otevřené frameworky
stavěné pro družice.
Třeba NASA F Prime
je framework letového softwaru
pro embedded a kosmické systémy.

<!-- S23 -->
Tvůj kód může vypadat
nějak takhle.

<!-- S24 -->
Ale je tu jeden obrovský rozdíl
oproti běžnému počítači.
Nepřipojíš se přes SSH.
Nepřipojíš debugger.
A když ti spadne software...
tvůj počítač je
pár set kilometrů vysoko.

<!-- S25 -->
Potřebuje proto watchdogy,
nouzové režimy, detekci chyb
a automatické zotavení.
Některé problémy musí vyřešit
bez tvojí pomoci.

<!-- S25b -->
A jeden velký důvod, proč to potřebuje,
je radiace.
Ve vesmíru můžou kosmické paprsky
překlopit bit v paměti
nebo i vyřadit čip.
Těžké stínění nemá —
vážilo by moc.
Počítač se místo toho hlídá,
opravuje chyby
a resetuje se, když se něco pokazí.

<!-- S26 -->
Ale jestli ji fakt
chceš vypustit...
začíná to být vážné.
Součástka, co funguje na stole,
není automaticky připravená
na raketu.
Musí přežít vibrace,
vakuum, teplotní extrémy
a radiaci.

<!-- S27 -->
Zpátky k tomu problému
jak poznat,
kam družice míří.
Představ si, jak se převaluje
vesmírem.
Žádná podlaha. Žádný strop.
GPS ti řekne,
kde jsi...
ale ne, kterým směrem
jsi otočený.

<!-- S28 -->
Družice proto kombinují
gyroskopy, magnetometry
a sluneční senzory,
aby zjistily svou orientaci.
A pak ji musí změnit.
Jeden běžný trik
je magnetorquer.

<!-- S29 -->
Opírá se
o magnetické pole Země
a vytvoří malý moment.
Není to raketový motor.
Družicí neposouvá.
Jen ji otáčí.
A to stačí
k natočení družice
přesně tam, kam chceš.

<!-- S30 -->
Nic z toho ale
není důvod,
proč jsme družici postavili.
Potřebujeme misi.
To je užitečné zatížení.
Měřit radiaci.
Fotit Zemi.
Zkoumat atmosféru.
Otestovat nový senzor.
Nebo prostě dokázat,
že nová technologie funguje.

<!-- S31 -->
Samotná družice
je tam hlavně proto,
aby udržela užitečné zatížení naživu.
Napájet ho. Mířit jím.
Udržet ho v teple.
Ukládat jeho data.
A poslat je domů.

<!-- S32 -->
Když ti zamrzne počítač,
restartuješ ho.
Když ti zamrzne družice...
máš velmi drahý objekt,
co tiše obíhá Zemi.

<!-- S33 -->
Řekněme, že jsme ji postavili.
Všechno funguje...
Počítač naběhne...
Rádio komunikuje.
Panely vyrábějí energii.
Přístroje fungují...
Můžeme ji vypustit?
...Zatím ne.

<!-- S34 -->
Družice musí dokázat,
že přežije start.
To znamená testování.
Hodně testování.

<!-- S35 -->
Nejdřív ji přišroubuj
k obřímu vibračnímu stolu.
Pak s ní pořádně zatřes...
To je vibrační test.
Start rakety není nic jemného.
Musí přežít
hluk, vibrace a otřesy,
aniž by se cokoli
uvolnilo nebo prasklo.
Záleží na každém šroubu.
Záleží na každém konektoru.
Záleží na každém kabelu.

<!-- S36 -->
Pak přijde vakuum.
Na Zemi teplo odvádí vzduch.
Ve vesmíru žádný vzduch není.
Jedna strana může být rozpálená,
druhá úplně ledová,
a elektronika
přesto musí zůstat
ve svých provozních mezích.
Družice proto potřebuje
teplovodivé pásky, nátěry,
izolaci
a pečlivě vybrané materiály.
Družice nemají
klimatizaci.
Mají fyziku.

<!-- S37 -->
A baterie
je zajímavá kapitola.
Nabij ji sluncem.
Pak družice
sklouzne do stínu Země
a panely nevyrábějí skoro nic.
Baterie ji drží naživu.
Pak zpátky na slunce.
Nabít. Vybít.
Nabít. Vybít.
Znovu a znovu.
Roky.
Jediná chyba v napájení
může tiše ukončit misi.

<!-- S38 -->
A jak s ní teď mluvit?
Potřebuješ rádio.
Anténu.
A frekvenci,
kterou smíš legálně použít.
A pozemní stanici.
Družice
nemá internet.
Jen přeletí nad hlavou
a vysílá.

<!-- S39 -->
Tvoje pozemní stanice
zachytí signál.
Počítač ho dekóduje.
A najednou máš data
z vlastní družice.
Představ si, že otevřeš terminál
a vidíš tohle.

Jenže stroj,
který ta čísla vypisuje...
je stovky kilometrů
nad tvou hlavou.

<!-- S40 -->
Tak jak ji
vlastně dostaneme nahoru?
Mohl bys postavit raketu...
Radši ne...
Nepotřebuješ ji.
CubeSaty létají
jako druhotný náklad.

<!-- S41 -->
Nějaká raketa už stejně letí.
Má místo navíc.
Tvoje družice se sveze
ve standardním deployeru.
Vlastní raketa není třeba.

<!-- S42 -->
A teď sedí
na špici rakety.
Nemůžeš na ni sáhnout.
Nemůžeš otevřít krabičku.
Nemůžeš připojit kabel.
Raketa startuje.
Asi za devět minut
jsi na oběžné dráze.

<!-- S43 -->
Deployer
uvolní tvoji družici.
Vymrští se
a začne se převalovat.

<!-- S43b -->
Ale jak pozná, že je venku?
...
Odpružené spínače, které byly
stlačené uvnitř deployeru,
při vypuštění povyskočí
a počítač naběhne.
Pak podle pravidel
zůstane asi půl hodiny tichá.
Teprve pak zapne rádio,
rozloží antény
a konečně se ozve domů.
A někde na Zemi...
ji tvoje pozemní stanice slyší.

<!-- S44 -->
Postavil jsi stroj.
A ten stroj teď
obíhá planetu.

<!-- S44b -->
Jenže ještě nekončíme.
Mrtvá družice nemůže
zůstat nahoře navždy.
Když zůstane na orbitě staletí,
stane se z ní vesmírný odpad.

<!-- S45 -->
To znamená, že moderní mise
musí čím dál víc plánovat
konec
života družice.
V ideálu ji řídká horní atmosféra
pomalu stáhne dolů.
Orbita se snižuje.
Vstoupí do atmosféry.
A shoří.
Konec mise...
je součást mise.

<!-- S46 -->
Takže... dokázal by sis
postavit vlastní družici?
Technicky ano.
Nemusíš být NASA.
Nemusíš
vlastnit raketu.
Nemusíš mít nutně ani
velkou firmu.

<!-- S47 -->
Družice musí
přežít start.
Přežít vesmír.
Komunikovat legálně.
Fungovat sama.
A nakonec
uvolnit oběžnou dráhu.
To všechno
musí být prokázané,
než to někdo
posadí na raketu.

<!-- S48 -->
CubeSaty přístup do vesmíru neusnadnily.
Standardizovaly ho.
Místo stavění všeho
od nuly
můžeš postavit něco,
co zapadá do existujícího standardu.
A to je překvapivě velká změna.

<!-- S49 -->
Takže někde právě teď
obíhají Zemi
drobné stroje.
Staví je univerzity,
výzkumné týmy,
firmy a studenti.

<!-- S50 -->
Některé nesou kamery.
Některé měří radiaci.
Některé testují
úplně novou technologii.
A některé jsou jen pokusy
s jedinou otázkou:
"dokážeme to
rozchodit ve vesmíru?"

<!-- S51 -->
A právě to dělá
stavbu vlastní družice
tak fascinující.
Protože vzdálenost
mezi tebou a vesmírem
už není raketa.
Může to být...
deseticentimetrová krabička.
A hodně, hodně
dlouhý checklist.
