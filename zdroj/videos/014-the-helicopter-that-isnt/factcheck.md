# Fact check — The Gyroplane: The Helicopter That Isn't

Ověřeno 2026-08-31 proti scénáři `script 0.3.md` (67 scén, 1 348 slov).
Scénář se od v0.3 nemění; storyboard ano — viz „Co z fact checku plyne
pro DIAGRAMY" a poznámku o Cierva C.4 níž.
Čísla scén odpovídají v0.2 — proti v0.1 se posunula, viz `notes.md`.
Metoda podle CLAUDE.md: vypsat **každé** ověřitelné tvrzení, ne jen ta,
která vypadají rizikově.

Legenda: ✅ doloženo · ⚠️ platí, ale s výhradou · ❌ neplatí

---

## S01–S04 — úvodní charakteristika

### „looks almost exactly like a helicopter … big rotor on top" ✅

Gyroplán má nepoháněný nosný rotor nad trupem a k tomu tlačnou (výjimečně
tažnou) vrtuli. Vizuální podobnost s vrtulníkem je právě to, na čem stojí
celý oblouk videa.

### „It can take off and land in a surprisingly small space." ✅

Přistání je u gyroplánu prakticky bez dojezdu — pilot vybere klesání
a dosedne při téměř nulové pozemní rychlosti. Vzlet vyžaduje rozjezd
(viz S31–S33), ale s předroztočením rotoru je krátký a se skokovým
vzletem (S34–S37) může být nulový. Tvrzení je v úvodu záměrně
**nastavená past**, kterou scénář sám v kapitole „But there's a catch"
rozebere.

> **`surprisingly` místo `very` je změna z v0.3.** Uživatel namítl, že
> `very small space` je proti pozdějšímu *„You need space for takeoff
> and landing"* moc absolutní. `surprisingly` hook udrží a tvrzení
> zmírní na to, co je doložitelné.

### „if its engine stops in mid-air, it can still land safely" ✅

Rozvedeno v S28–S34, tam i výhrady. Viz níž.

### „also called an autogyro" ✅

Synonyma: gyroplane (ICAO/EASA/FAA úřední termín), autogyro, gyrocopter,
gyrokoptéra. *Autogiro* s „i" je **ochranná známka Cierva Autogiro Company**,
proto se ve scénáři nepoužívá.

### „The engine doesn't power the rotor." ✅

Jádro definice. Motor pohání vrtuli; nosný rotor je v **autorotaci**,
poháněný nabíhajícím vzduchem. Předroztočení před vzletem je jediná
výjimka a je pozemní (S26).

---

## S05–S07 — jak to má vrtulník

### „In a helicopter, the engine spins the main rotor." ✅

### „by tilting the rotor, the helicopter can also move in different directions" ✅

Naklonění vektoru tahu rotoru cyklikou. Standardní popis.

### „If you spin a rotor one way, physics wants to spin the rest of the helicopter the other way." ✅

Reakční moment (3. Newtonův zákon / zachování momentu hybnosti).

### „conventional helicopters need a way to counteract that torque — usually a tail rotor" ✅

Slovo **„usually"** je důležité a ve scénáři je: existují koaxiální
(Kamov), tandemové (Chinook), příčné, NOTAR i systémy se vzájemně
zabírajícími rotory (Kaman). Bez toho hedgingu by tvrzení neplatilo.

---

## S08–S10 — jak to má gyroplán

### „Its engine powers a completely separate propeller." ✅

### „the airflow through the big rotor on top makes it spin — this is called autorotation" ✅ a od v0.2 je to i vysvětlené

Ve v0.1 tu byla jediná ⚠️ celého fact checku: jev byl pojmenovaný, ale
nevysvětlený. **Uživatel si rozšíření vyžádal a v0.2 ho má** — nový blok
S11–S17, ověřený níž.

### „engine → propeller → forward motion → airflow → spinning rotor → lift" ✅

Řetěz je správný. Ve scénáři je vyslovený jako výčet (`Engine, propeller,
forward motion, airflow, spinning rotor, lift.`), šipky patří do diagramu.

## S11–S17 — mechanismus autorotace (nové ve v0.2)

Sedm scén doplněných na vyžádání uživatele. **Ověřeno proti americké
armádní příručce aerodynamiky autorotace a proti FAA Helicopter Flying
Handbook**, kde je to standardní učebnicový výklad.

### „The rotor disc isn't flat. It's tilted back." ✅

Rotorový disk gyroplánu je za letu nakloněný dozadu vůči nabíhajícímu
proudu. Bez toho by autorotace nenastala.

### „So the air isn't pushed down through it, the way it is under a helicopter. It comes up through it instead." ✅

Klíčový rozdíl. Poháněný rotor vrtulníku žene vzduch **dolů** diskem
(indukované proudění dolů). Rotor v autorotaci má diskem složku proudění
**vzhůru**. Vrtulník v autorotaci se chová stejně jako gyroplán — proto
je to tentýž jev pod týmž jménem.

### „It's slicing forward through the air, and at the same time, air is arriving from below." / „The flow it meets is the sum of both." ✅

Popis výsledného (relativního) proudu jako vektorového součtu obvodové
rychlosti listu a nabíhajícího proudu. Standardní postup.

### „That tips the lift of the blade slightly forward … in the direction the blade is already moving." ✅

Naklonění výsledného proudu vzhůru nakloní i výslednou aerodynamickou sílu
**dopředu před osu otáčení**, takže má složku ve směru otáčení. Ta rotor
pohání. Formulace „tips the lift forward" je zjednodušení (přesně jde
o výslednou aerodynamickou sílu, ne o vztlak samotný), ale je to
zjednodušení **ve správném směru** a v učebnicích se používá taky.

### „Where the flow arrives steeply, the blade is driven. Where it arrives shallowly, it drags." ✅ ale pozor na diagram

Úhel náběhu proudu je `atan(V_vzhůru / Ωr)`. Složka vzhůru je po rozpětí
zhruba stálá, kdežto obvodová rychlost `Ωr` roste s poloměrem — proto je
proud **strmý u kořene** a **plochý u konce listu**. Strmý proud naklání
výslednou sílu dopředu (hnací oblast), plochý dozadu (brzdná).

> **Scénář to říká podmínkou, ne poloměrem, a to je záměr.** Učebnicové
> dělení disku je **trojí**, ne dvojí:
>
> | oblast | poloměr | co dělá |
> |---|---|---|
> | ztrátová (stall) | vnitřních **25 %** | nad kritickým úhlem, **brzdí** |
> | hnací (driving) | **25–70 %** | pohání |
> | brzdná (driven, „propeller") | vnějších **30 %** | brzdí |
>
> Kdyby scéna říkala „u náboje to pohání", **bylo by to špatně** —
> u samotného náboje je ztrátová oblast, která brzdí. Proto je ve
> scénáři podmínka *„where the flow arrives steeply"*, ne poloha.
>
> **Pro diagram z toho plyne tvrdý požadavek:** hnací pás se kreslí
> **doprostřed listu**, ne ke kořeni, a procenta se do obrázku
> **nepíšou** — čísla výš platí pro vrtulník v autorotaci, kdežto
> gyroplán v dopředném letu má navíc asymetrii postupujícího
> a ustupujícího listu, takže by obraz tvrdil přesnost, kterou nemáme.
> Platí „diagram tvrdí i to, co v popisku není".

### „It settles where those two balance, and holds there by itself." ✅

Ustálené otáčky jsou tam, kde se hnací a brzdný moment vyrovnají.
Je to samočinná zpětná vazba: klesnou-li otáčky, zvětší se úhel náběhu
proudu, hnací oblast se zvětší a otáčky se vrátí.

---

## S18–S19 — co ten rotor „zadarmo" stojí

### „You are exchanging some forward speed for the energy needed to keep the rotor spinning." ✅

Přesnější formulace by byla „platíš odporem, tedy výkonem", ale směr je
správný: energie na roztočení rotoru pochází z nabíhajícího proudu a musí
ji dodat vrtule. Gyroplán má proto vyšší indukovaný odpor než letoun
srovnatelného výkonu a nižší klouzavost.

### „there is no engine-driven rotor shaft" ✅

---

## S20–S27 — proč se trup netočí

### „In a helicopter, the engine continuously supplies torque to overcome the aerodynamic drag of the rotor." ✅

### „In a gyroplane, the rotor is free-spinning … no large engine torque … into the aircraft" ✅

V ustálené autorotaci je **výsledný aerodynamický moment na rotoru nulový**
(hnací a brzdná oblast se vyrovnají) a hřídelí se přenáší jen tření
v ložisku, tedy řádově nic. Proto gyroplán **nepotřebuje vyrovnávací rotor**.

> **Co scénář správně NEtvrdí:** že gyroplán nemá ocasní plochy. Má
> svislou ocasní plochu s kormidlem — ale na **řízení směru** a na
> vyrovnání momentu **vrtule**, ne rotoru. Věta ve scénáři je
> `you don't need a tail rotor just to keep the fuselage from spinning`,
> tedy přesně to. Formulace `just to` nese celé břemeno; **při škrtání
> ji nezkracuj.**

### „And yes — there can be aerodynamic torques." ✅

Poctivé. Nulový je výsledný moment v ustáleném stavu, ne okamžité síly.

---

## S28–S33 — gyroplán nevisí

### „It can't hover." ⚠️ platí v bezvětří, ne absolutně

Gyroplán potřebuje **vzduch protékající rotorem**, ne nutně pohyb vůči zemi.
V protivětru zhruba na úrovni jeho minimální rychlosti (u lehkých typů
řádově 40–50 km/h) může **stát nad jedním místem terénu**. Je to vis vůči
zemi, ne vůči vzduchu.

Scénář se tomu vyhýbá správně: hned následující věta je
`A gyroplane needs airflow through its rotor`, tedy definice přes vzduch,
a `That means it normally has to move forward` s hedgingem **„normally"**.
**Ponechat obojí.** Samotné `It can't hover.` bez těch dvou vět by bylo
zjednodušení, které se dá vyvrátit videem z YouTube.

### „you can't simply point it upward and take off vertically" ⚠️ hedging `simply` je nutný

Existuje **jump takeoff** (skokový vzlet): rotor se předroztočí nad letovou
frekvenci při nulovém úhlu nastavení listů, pak se skokem nasadí kolektivní
úhel a stroj se vymrští z uložené kinetické energie vzhůru. Cierva C.30
a C.40 s „autodynamickou" hlavou zvládly **asi 6 metrů**; dělají to
i některé moderní stroje.

Není to vrtulníkový vertikální vzlet — je to jeden skok z energie
uskladněné v rotoru, po němž musí okamžitě následovat rozlet. Slovo
**`simply`** ve větě to celé drží. Bez něj by věta byla nepravdivá.

> **Od v0.2 to video říká samo** — blok S34–S37 níž. Slovo `simply`
> v S31 tím dostalo ještě větší váhu: je to teď nastavené očekávání,
> které se o čtyři scény později opraví.

### „Some gyroplanes can pre-spin their rotors before takeoff, allowing a very short takeoff run." ✅

Předroztáčeč (prerotator) je běžná výbava. Je to slabší varianta téhož,
co dělá jump takeoff.


---

## S34–S38 — skokový vzlet (nové ve v0.2)

Čtyři scény doplněné na vyžádání uživatele, s jeho podmínkou:
*„Nechci, aby divák odnesl, že gyroplán umí normálně kolmý vzlet."*

### „a few gyroplanes can leave the ground without any run at all" ✅

### „The rotor is spun up on the ground past its normal flying speed, with the blades set almost flat, so they make hardly any lift." ✅

Přesný popis. Předroztočení **nad** letové otáčky je možné právě proto,
že listy jsou na malém (nulovém až záporném) úhlu nastavení a nekladou
odpor ani nedělají vztlak.

### „Then the pilot changes the blade angle all at once. The stored spin turns into lift, and the machine hops off the ground." ✅

Skokové nasazení kolektivního úhlu. Cierva tomu říkal **autodynamická
hlava** — u C.30 a C.40 to nasazení proběhlo automaticky ve chvíli, kdy
se roztáčení zastavilo.

### „Cierva's machines could clear about six metres." ✅

Doloženo: *„jump some 20 ft (6 m) upwards"*. Zdroj je NASA/TP-2015-218714
(J.-P. Harrison, *The Cierva Autodynamic Rotor*) a popisy typů C.30 a C.40.

> **Šest metrů je výška skoku, ne dostup.** Kdyby to diagram nakreslil
> jako stoupání, tvrdil by něco jiného.

### „But it's one jump, out of energy the rotor already had … It doesn't hover at the top." ✅ a je to ta nutná pojistka

Tohle je věcně nejdůležitější věta bloku. Energie na skok je **uložená
v setrvačnosti rotoru** a je jednorázová; po vyčerpání musí okamžitě
následovat dopředný let, jinak otáčky klesnou a vztlak zmizí. Skokový
vzlet **není vis** a není to ani vrtulníkový svislý vzlet.

Bez téhle věty by blok popíral S28 (*It can't hover*) a S31
(*you can't simply point it upward*). S ní je opravuje jen o to, o co má.

### „much closer to a strange hybrid between an aeroplane and a helicopter" ✅

Hodnotící, ne faktické. Po vloženém bloku sedí ještě líp než ve v0.1.

---

## S39–S47 — vysazení motoru

### „In an aeroplane, you now have a glider." ✅

### „In a helicopter, the pilot enters autorotation and uses the airflow to keep the rotor spinning." ✅

Snížit kolektiv, přejít do klesání, u země vybrat z energie rotoru.

### „In a gyroplane you're already in autorotation." ✅

Nejsilnější tvrzení videa a je pravdivé. Gyroplán nemá co „zahajovat" —
letí v autorotaci pořád. Odpadá reakční doba pilota, která je u vrtulníku
kritická.

### „The pilot can control the descent and make an emergency landing." ✅

### „You still need altitude, speed, a suitable landing area and a competent pilot." ✅

Poctivá výhrada a patří tam. Gyroplán má strmější klesání (menší
klouzavost) než letoun, takže „doletíš dál" neplatí — výhoda je v tom,
že **neztratí schopnost vyrábět vztlak**, ne v doletu.

### S45–S46 (nové ve v0.2) — „And it isn't crash-proof." ✅

Doplněno na vyžádání uživatele jako brzda proti „AKSHUALLY" komentáři.
Ověřeno, protože **první formulace byla vedle** a stojí za zaznamenání
proč — viz `notes.md`.

### „The rotor turns because the air is pushing up through it. Unload it, and it slows down." ✅

Vazba na nový blok S11–S17 a je to fyzikálně tentýž jev z druhé strany:
rotor se točí, protože je **zatížený** proudem. Při manévru pod jedno G
indukovaný odpor rotoru téměř zmizí a **otáčky rychle klesají**. To je
doložené a je to hlavní mechanismus nehod gyroplánů.

### „Older designs carried the propeller high above the centre of gravity, and could pitch down into it." ✅ ale pozor na formulaci

Jde o **power push-over** (bunt-over). Tah vrtule vedený nad těžištěm
dává klopivý moment na nos dolů; chybí-li dostatečná vodorovná ocasní
plocha, může se to při odlehčeném rotoru **samo posilovat** a stát se
nevratným.

> **Původní návrh zněl „pitch-down po vysazení motoru" a to je vedle.**
> Tah nad těžištěm dává moment na nos **dolů**, takže ubrání výkonu nos
> naopak zvedne. Nebezpečné je **přidání výkonu** a hlavně **odlehčení
> rotoru** — proto je ve scénáři formulace *„could pitch down into it"*,
> tedy do toho odlehčení, ne po vysazení motoru.
>
> Scéna proto **nesmí** být nakreslená jako „motor zhasl → nos dolů".
> Kreslí se odlehčený rotor a tahová osa nad těžištěm.

### „Modern machines are built against it, and pilots are taught never to unload the rotor." ✅

Novější konstrukce řeší polohu tahové osy vůči těžišti a velikost
vodorovné ocasní plochy; výskyt PPO tím výrazně klesl. Vyšetřovala to
v devadesátých letech britská **CAA** s **Glasgowskou univerzitou** na přístrojově vybaveném dvoumístném stroji.

### „an engine failure doesn't automatically mean that the aircraft has lost its ability to generate lift" ✅

---

## S48–S53 — historie

### „The first successful practical gyroplane was developed by Spanish engineer Juan de la Cierva." ✅

Juan de la Cierva y Codorníu (1895–1936), španělský letecký inženýr.
Typy C.1 až C.3 selhaly, C.4 uspěl.

### „His C four made its first successful flight in nineteen twenty-three." ✅ rok je bezpečný, den ne

Prameny se liší v datu, **ne v roce**:

| verze | datum | co to bylo |
|---|---|---|
| Ciervovo vlastní tvrzení | **9. ledna 1923**, Getafe u Madridu | při pojezdových zkouškách se stroj odlepil (pilot por. Alejandro Gómez Spencer) |
| většina historiků | **17. ledna 1923**, tamtéž | první **pozorovaný a natočený** let: asi 180 m v ustálené výšce ~4 m |

**Scénář uvádí jen rok, takže je to v pořádku.** Kdyby se do scénáře nebo
do titulků dostalo přesné datum, patří tam 17. leden s poznámkou o sporu.

> **A jedna věc, která se ukázala až u storyboardu: FOTKA C.4 NEEXISTUJE.**
> Wikimedia Commons na `Cierva C.4` vrací jen pozdější typy — C.7 (1927),
> C-8L (1928) a C.30. Kdyby některý z nich stál pod větou *„His C four made
> its first successful flight"*, divák by ho četl jako C.4 a byla by to
> **falešná atribuce** — přesně ta vada, kterou má projekt v pastech
> („evidence doplněná dohledáním").
>
> S50 je proto **kresba**, ne archiv. Tvrdí jen to, co scénář říká: rok,
> místo a stroj té třídy. Archivní snímky zůstaly čtyři a u všech čtyř
> je jasné, co na nich je: moderní gyroplán (S01), gyroplán na trávě (S33),
> portrét Ciervy (S49) a Cierva C.30 (S53).

### „That's more than a century ago." ✅

1923 → 2026 je **103 let**.

### „Cierva's work on rotor systems also contributed ideas that later became important in helicopter development." ✅ a je to podhodnocené

Není to zdvořilostní věta, je to jeden z pilířů oboru. Cierva identifikoval
**nesymetrii vztlaku** (postupující list má vyšší náběžnou rychlost než
ustupující, což stroj překlápí) a vyřešil ji **mávacím kloubem**; k němu
přidal **kmitavý kloub** a vznikl **plně kloubový rotor**, který je dodnes
základ konstrukce rotorových hlav vrtulníků. Vazba **delta-3** (mávnutí
listu vzhůru samo zmenší jeho úhel nastavení) je také jeho.

### „the gyroplane wasn't invented as a cheap alternative to modern helicopters … one of the stepping stones toward rotary-wing flight" ✅

Chronologie sedí: C.4 letěl **1923**, první prakticky použitelný vrtulník
(Focke-Wulf Fw 61) až **1936**, Sikorsky VS-300 **1939**. Gyroplán je
o třináct let starší než vrtulník, ne jeho levná odnož.

---

## S54–S59 — cena a spotřeba

> **Všechna čísla platí k srpnu 2026 a jsou to katalogové ceny bez daně.**
> Kurz použitý pro přepočet: 1 EUR ≈ 1,09 USD.

### „a modern two-seat gyroplane can cost only a fraction of the price of a comparable small helicopter" ✅

### „for roughly twenty to forty per cent of the purchase price of a comparable helicopter" ⚠️ platí, ale horní hranice je natěsno

Spočítáno, ne odhadnuto:

| dvojice | gyroplán | vrtulník | poměr |
|---|---|---|---|
| Cavalon (Rotax 915 iS) 127 000 € ≈ 138 000 $ vs. **R22 Beta II** základ 375 000 $ | 138 k$ | 375 k$ | **36,8 %** |
| Cavalon (Rotax 916 iS) 141 210 € ≈ 154 000 $ vs. R22 základ | 154 k$ | 375 k$ | **41,1 %** |
| Cavalon 915 iS vs. **konfigurovaný R22** 428 300 $ | 138 k$ | 428 k$ | **32,2 %** |
| Cavalon 915 iS vs. **R44** (čtyřmístný, ~620 k$) | 138 k$ | 620 k$ | **22,3 %** |

Rozpětí vychází **22 až 41 %**. Deklarované „roughly twenty to forty per
cent" tedy sedí — ale horní okraj je o desetinu procenta venku a drží ho
jen slovo **`roughly`** a **`depending on the model`**. Obojí ve scénáři je.

**Nepřepisuj to na „a fifth to a third"** — to by bylo 20–33 % a nejdražší
kombinace by z toho vypadla ven doopravdy.

### „A small gyroplane might burn roughly ten to twenty litres of fuel per hour" ⚠️ platí pro slabší motory, ne pro celou třídu

| motor / stroj | spotřeba v cestovním režimu |
|---|---|
| Rotax 912 iS | **13,6–14,1 l/h** |
| Rotax 912 iS, běžné cestovní nastavení | ~15 l/h |
| AutoGyro Cavalon s Rotaxem 915 iS (údaj výrobce) | **13,2–26,5 l/h** (3,5–7 gal/h) |
| hrubé pravidlo Rotax | ≈ 0,3 × výkon [hp] litru za hodinu |

Deset až dvacet litrů odpovídá strojům s Rotaxem 912 (80–100 hp). Silnější
915/916 iS jdou nad dvacet. Scénář to má ošetřené třikrát: **„A small
gyroplane"**, **„roughly"** a **„depending on the engine, the aircraft and
the conditions"**. **Žádný z těch tří hedgingů se nesmí vyškrtnout.**

### „At a cruising speed around one hundred and forty kilometres per hour, that can work out to roughly seven to fourteen litres per hundred kilometres." ✅ aritmetika sedí

- 10 l/h ÷ 140 km/h × 100 = **7,14 l/100 km**
- 20 l/h ÷ 140 km/h × 100 = **14,29 l/100 km**

Cestovní rychlost je realistická: Cavalon 120–177 km/h, Calidus 160 km/h.
Sto čtyřicet je uprostřed.

### „That's not exactly economical transport" ✅

Hodnotící, a poctivé — sedm až čtrnáct litrů na sto kilometrů je spotřeba
velkého SUV.

---

## S60–S67 — závěr

### „The gyroplane is relatively simple." / „It doesn't need a powered main rotor." ✅

Odpadá převodovka hlavního rotoru, vyrovnávací rotor s jeho hřídelí
a převodovkou, a kolektivní řízení (u strojů bez skokového vzletu).

### „It can survive an engine failure remarkably well." ✅

Viz S28–S34.

### „It can fly at respectable speeds." ✅

Calidus: cestovní 160 km/h, maximální 225 km/h.

### „it can be much cheaper to buy and to operate" ✅

Viz S41–S45.

### „You need space for takeoff and landing. And you can't simply land vertically in your back garden." ✅

Přistání je krátké, ale ne svislé, a hlavně: nad zástavbou by na to nebyl
prostor pro přiblížení. Věta je o prostoru, ne jen o délce dojezdu.

### „this strange combination has been flying for more than a hundred years" ✅

1923 → 2026, viz výš.

---

## Souhrn

| | v0.1 | **v0.2** |
|---|---|---|
| ověřených tvrzení | 44 | **57** |
| ✅ platí beze změny | 32 | **45** |
| ⚠️ platí, ale drží to hedging ve scénáři | 6 | **5** |
| ❌ neplatí | 0 | **0** |

Ubyla jedna ⚠️: díra „autorotace je pojmenovaná, ale nevysvětlená" je
rozšířením S11–S17 zaceleá. Třináct nových tvrzení prošlo bez výhrady.

**Do scénáře nezasahuje nic.** Pět výhrad není pět chyb — je to pět míst,
kde je tvrzení pravdivé **jen se slovem, které tam autor napsal**.

> **To je pro tohle video hlavní riziko škrtání.** Při zkracování se
> první ruší právě taková slova, protože vypadají jako vata. Nejsou.
> Seznam k ochraně:
>
> | scéna | slovo | bez něj tvrzení |
> |---|---|---|
> | S07 | `usually` a tail rotor | vylučuje Kamov, Chinook, NOTAR |
> | S27 | `just to` keep the fuselage from spinning | popírá, že gyroplán má kormidlo |
> | S31 | `normally` has to move forward | vylučuje vis v protivětru |
> | S31 | `simply` point it upward | popírá skokový vzlet — a od v0.2 si to video **samo opravuje** o čtyři scény dál |
> | S55 | `roughly` twenty to forty per cent | horní okraj vychází měřením 41,1 % |
> | S56 | `small`, `roughly`, `depending on…` | Rotax 915/916 jde nad 20 l/h |
> | S45 | `Older designs`, `could` | bez nich by video tvrdilo, že gyroplány padají dodnes |

---

## Co z fact checku plyne pro DIAGRAMY

Tři místa, kde by obraz mohl tvrdit víc než scénář:

| scéna | past | jak ne |
|---|---|---|
| **S16** | hnací pás nakreslený **u náboje** | u náboje je ztrátová oblast, která brzdí. Hnací pás patří **doprostřed listu** |
| **S16** | procenta poloměru v obrázku | čísla 25 / 25–70 / 30 % platí pro vrtulník v autorotaci, ne pro gyroplán v dopředném letu |
| **S35** | šest metrů nakreslených jako **stoupání** | je to výška jednoho skoku, ne dostup |
| **S45** | „motor zhasl → nos dolů" | příčinou je **odlehčení rotoru** a tahová osa nad těžištěm, ne vysazení motoru |

A obecně: **čárkovaná čára nemá v tomhle videu co dělat.** Všechno je
doložené, takže konvence „plná = doloženo, čárkovaná = hypotéza"
z devátého videa by tu vyráběla pochybnost, kterou scénář nemá.

---

## Zdroje

- Cierva C.4, datum a okolnosti prvního letu — Wikipedia „Cierva C.4",
  Vintage Aviation News (replika k stému výročí), all-aero.com
- Nesymetrie vztlaku, mávací a kmitavý kloub, delta-3 — Embry-Riddle,
  *Introduction to Aerospace Flight Vehicles*, kapitola „Helicopters";
  Wikipedia „Juan de la Cierva"; HistoryNet, „Juan de la Cierva: Autogiro Genius"
- Skokový vzlet a autodynamická hlava — NASA/TP-2015-218714, J.-P. Harrison,
  *The Cierva Autodynamic Rotor*; Wikipedia „Cierva C.30", „Cierva C.40"
- Ceny gyroplánů — AutoGyro GmbH / aeroexpo.online (Cavalon, katalog 2026)
- Ceny vrtulníků — Robinson Helicopter Company, ceníkové údaje R22 Beta II
  přes Quantum Helicopters a Aircraft.com (modelový rok 2026)
- Spotřeba — rotax-owner.com (912 iS, 912 ULS), AutoGyro USA / Gyro Revolution
  (Cavalon 915 iS), Wikipedia „AutoGyro Calidus"
- **Aerodynamika autorotace** (hnací, brzdná a ztrátová oblast; naklonění
  výsledné síly) — US Army, *Aerodynamics of Autorotation* (výtah v dokumentaci
  NTSB); FAA *Helicopter Flying Handbook*, kap. autorotace; copters.com
- **Power push-over, odlehčení rotoru, výzkum CAA** — Wikipedia „Power push-over";
  KitPlanes, *Gyroplane Safety*; měření Glasgowské univerzity na tahové ose
  vůči těžišti, financovaná britskou CAA
