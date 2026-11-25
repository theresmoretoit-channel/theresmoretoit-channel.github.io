# 167 — fact check scénáře (v0.2 → v0.3, 2026-11-21)

Ověřuje **každé** tvrzení `script.md`, scénu po scéně. Čísla, která už
dokládá `factcheck-zaklad.md`, se tu jen odkazují (§ = jeho sekce).
Značky jako tam: **P** primární, **S** sekundární, **M** spočítáno,
**Pam** z paměti (nedohledáno, riziko nízké).

Primární zdroje, plné texty přečtené (`pdftotext`):
- **HAVOC PoC** — Jones, Arney a kol., *HAVOC: Proofs of Concept*, NTRS 20160006580.
- **HAVOC 2015** — Arney a Jones, prezentace *HAVOC: An Exploration Strategy
  for Venus*, AIAA Space 2015, NTRS 20160006329.
- **Landis 2003** — *Colonization of Venus*, STAIF 2003, NTRS 20030022668.
- **Landis 2020** — *Settling Venus: A City in the Clouds?*, AIAA-2020-4152, NTRS 20205008515.

Výsledek: **10 oprav** (sloupec „verdikt“ ✏️), z toho 6 z tvého seznamu
k v0.2 a 4 nové. Dramaturgie beze změny. v0.3: 93 scén, ~2 261 slabik,
~9:15 řeči, ~10:45 s pauzami.

## Háček (S01–S08)

| scéna | tvrzení | ověření | verdikt |
|---|---|---|---|
| S01 | povrch ~465 °C | § 1 (NASA; Venera 13 naměřila 457 °C) | ✅ |
| S02 | taví olovo | olovo taje při 327 °C; i nejchladnější místo, vrchol Maxwell Montes (~380 °C), je nad tím | ✅ Pam |
| S02 | stejně ve dne v noci, na pólech i na rovníku | husté CO₂ teplotu vyrovnává na pár stupňů; rozdíly dělá **nadmořská výška**, ne šířka ani denní doba | ✅ S |
| S03 | 90× zemský tlak, skoro kilometr pod mořem | 92 bar; (92 − 1) bar / (1 025 · 9,81) = **905 m** | ✅ M |
| S04 | 1982, Venera 13, sovětská | přistála 1. 3. 1982 | ✅ S |
| S05 | navržena na půl hodiny, vydržela přes dvě hodiny | navržena na **32 min**, vysílala **127 min** (Wikipedie, Guinness) | ✅ S. **Pozor:** HAVOC PoC píše „157 minutes“, je to chyba studie, ne naše |
| S06 | „some engineers at NASA argue“ … nejpodobnější Zemi mimo Zemi | Landis 2020: *„the most earthlike environment (other than Earth itself) in the solar system“*; stránka NASA o HAVOC: *„the most Earth surface-like conditions within the Solar System“* | ✅ P |
| S07 | 50 km nad povrchem | totéž, Landis i HAVOC | ✅ P |
| S08 | většina plánů na život jinde míří na Mars | obecně známé | ✅ |

## Výškové pásmo (S09–S15)

| scéna | tvrzení | ověření | verdikt |
|---|---|---|---|
| S10 | 50 km: tlak skoro přesně jako u moře, ~75 °C | VIRA 1,07 bar a 350 K (77 °C) — § 2. Landis: 1 bar *„slightly above fifty km“* | ✅ |
| S11 | o 5 km výš pokojová teplota | VIRA 55 km = **27–29 °C**, Landis 20 °C až v 56 km. Holé „room temperature“ je o kus teplejší | ✏️ → *„drops to about room temperature“* |
| S12 | půl zemského tlaku, jako v základním táboře pod Everestem | 0,53 bar; EBC 5 364 m → 0,51 bar ze standardní atmosféry, naměřeno ~0,53 | ✅ M |
| S13 | pásmo pár kilometrů silné | 50–56 km, Landis: města v 50–60 km | ✅ P |
| S14 | žádný skafandr, nezmrznete ani se nevaříte | tlak 0,5–1 bar, tedy nad Armstrongovou hranicí (0,063 bar), takže krev se nevaří. Landis 2003: *„will not require a high-strength pressure vessel“* | ✅ P |
| S15 | „oxygen mask“ | **Tvoje výhrada platí.** Obyčejná kyslíková maska (letadlová) přisává okolní vzduch, tady by to byl CO₂. Je potřeba **utěsněná maska s vlastním přívodem**. Landis 2003: *„would still require provision of oxygen … sufficient clothing to avoid direct skin exposure to aerosol droplets“* | ✏️ → *„a sealed mask / with your own air supply“* |

## Skóre 1, gravitace (S16–S19)

| scéna | tvrzení | ověření | verdikt |
|---|---|---|---|
| S16 | Venuše skoro velká jako Země, gravitace ~90 % | poloměr 95 %, **0,904 g** | ✅ S |
| S17 | Mars 38 % | 0,38 g | ✅ S |
| S18 | „Nobody has ever lived **for years** in gravity that low“ | **Neplatí doslova.** Na ISS se žije přes rok v beztíži, tedy v gravitaci *nižší*: Poljakov 437 dní v kuse, Kononěnko přes 1 000 dní celkem. Pravda je, že **v částečné gravitaci** (třetina g) nežil nikdo; Apollo strávilo na Měsíci nejvýš tři dny | ✏️ → *„Nobody has ever lived / in gravity like that. / We don't know what years of it would do“* |
| S19 | „almost exactly what you weigh“ | 90 % znamená, že 70 kg váží 63 kg. „Almost exactly“ je přehnané | ✏️ → *„you'd weigh nearly / as much as you do at home“* |

## Skóre 2, radiace (S20–S24)

| scéna | tvrzení | ověření | verdikt |
|---|---|---|---|
| S20 | Venuše ani Mars nemají magnetické pole | Venuše jen indukovanou magnetosféru; Mars jen zbytky magnetizace v kůře, globální pole ne | ✅ S |
| S21 | v 50 km víc vzduchu nad hlavou než nad pláží | sloupec = p/g: 106 600 Pa / 8,73 m/s² (g ve 50 km) = **1,22 kg/cm²**; Země u moře 101 325 / 9,81 = **1,03 kg/cm²** | ✅ M |
| S22 | „about a kilogram of air on every square centimetre“ | 1,22 ≈ „about a kilogram“; doslova Landis 2003 i 2020 (*„about one kilogram per square centimeter of mass shielding“*). Pozor, platí **pro 50 km**; v 55 km je to 0,61 kg/cm², jako na Zemi v ~5 km | ✅ P + M |
| S22 | „much of the radiation“ | Landis: *„most radiation“*, *„galactic cosmic radiation and … solar particle event radiation“*. Studie dávek (§ 5) dávají v 51–62 km hodnoty řádově jako na povrchu Země; výhrada o slunečních bouřích v horní části pásma platí. „Much of“ je opatrnější než zdroj | ✅ P |
| S23 | Mars méně než 2 % toho | 610 Pa / 3,72 m/s² = **16,4 g/cm²**, tedy **1,3 %** z 1,22 kg/cm² | ✅ M |
| S23 | mnoho plánů zahrabává habitaty pod regolit | běžné v návrzích (NASA, Mars Society, studie stínění regolitem) | ✅ S |

## Skóre 3, vztlak a díra v obalu (S25–S36)

| scéna | tvrzení | ověření | verdikt |
|---|---|---|---|
| S26 | balon na Zemi: helium nebo vodík | ✅ | ✅ |
| S27 | vzduch na Venuši skoro celý CO₂ | 96,5 % | ✅ S |
| S28 | CO₂ je „about half as heavy again“ | 44 / 29 = **1,52** | ✅ M |
| S29 | dýchatelný vzduch je nosný plyn | doslova HAVOC PoC i Landis 2003 | ✅ P |
| S31 | 50 km: ~0,5 kg/m³, polovina helia na Zemi; výš ~čtvrtina | ρ(CO₂, 1,066 bar, 350 K) = 1,59, ρ(vzduch) = 1,06 → **0,53 kg/m³**; helium u moře 1,225 − 0,169 = **1,06** → 50 %. Landis 2020: 0,28 kg/m³ v 56 km = **26 %**. Landis 2003 uvádí *„about half kg per cubic meter“* | ✅ M + P |
| S32b | lidé můžou bydlet přímo v nosném plynu | Landis 2003: *„the full volume of the aerostat to be habitable volume“* | ✅ P |
| S33 | tlak uvnitř stejný jako venku | Landis 2003 i 2020 | ✅ P |
| S33b | výš jen půl zemského tlaku, směs s víc kyslíkem, každý nádech jako u moře | Landis 2020: 0,56 bar a **37 % O₂** → parciální tlak 0,207 bar = mořských 0,21 | ✅ P + M |
| S33c | obal nemusí nic držet | Landis: *„would not require a high-strength pressure vessel, and could be extremely lightweight“* | ✅ P |
| S34 | „nothing rushes out … just mixes“ | **Tvoje výhrada platí a je i fyzikální.** Úplně nulový rozdíl tlaků to není: lehčí vzduch uvnitř vysokého obalu tlačí nahoře o Δρ·g·h víc než CO₂ venku. U koule 1 km je to 0,5 × 8,7 × 1 000 ≈ **4 kPa** (4 % atmosféry). Výbušná dekomprese tedy odpadá, **pomalý únik nahoře a průnik CO₂ dole** ne | ✏️ → *„there's no explosive decompression. / The air just seeps out, slowly, / and carbon dioxide seeps in.“* |
| S35 | „One NASA study estimated … large rip … thousands of hours“ | Landis 2003 a 2020 doslova: *„even a rather large tear in the envelope would take thousands of hours to leak significant amounts of gas, allowing ample time for repair“*. **Velikost trhliny ani „významný únik“ nedefinuje a výpočet neuvádí** (k tvé otázce). Je to odhad jednoho inženýra, ne studie. Kontrolní řádový výpočet: díra 1 m² nahoře, Δp 4 kPa → v = √(2Δp/ρ) ≈ 90 m/s, se součinitelem výtoku ~0,6 asi 55 m³/s; koule 1 km má 5,2·10⁸ m³ → **~2 600 h na celý objem**. „Thousands of hours“ řádově sedí | ✏️ → *„One NASA engineer estimated“* |
| S36 | Mars: venku méně než 1 % zemského tlaku | 6,1 mbar / 1 013 = **0,6 %** | ✅ M |

## Vega (S37–S42)

| scéna | tvrzení | ověření | verdikt |
|---|---|---|---|
| S37 | 1985, Vega 1 a 2, sovětské, kolem Venuše k Halleyově kometě | u Venuše 11. a 15. 6. 1985, u Halleyovy komety v březnu 1986 | ✅ S |
| S38 | každá shodila do mraků balon | sestupný modul každé sondy vypustil balon | ✅ S |
| S39 | ~54 km, zhruba dva dny, data na Zemi | ~54 km, **přes 46 h**; vysílaly přímo na Zemi (síť ~20 radioteleskopů, VLBI) | ✅ S |
| S40 | skoro 250 km/h | 66,0 a 69,4 m/s = **238 a 250 km/h** | ✅ S + M |
| S40 | třetina cesty kolem planety | NASA NTRS: *„one-third of the way around“*; kontrola: 46 h × 67 m/s = 11 100 km, obvod ve 54 km 38 400 km → 29 % | ✅ S + M |
| S41 | malé, s heliem | koule **3,4–3,54 m** (prameny se liší), **helium**, superpressure, gondola 6,9 kg na laně 13 m | ✅ S |
| S42 | balony na Venuši už letěly, lidi ne | ✅ | ✅ |

## HAVOC (S43–S45)

| scéna | tvrzení | ověření | verdikt |
|---|---|---|---|
| S43 | studie HAVOC, vzducholoď s posádkou 129 m | Landis 2020 | ✅ P |
| S44 | dva astronauti, měsíc, 50 km | HAVOC 2015: *„2 crew, 30 days“*, 50 km | ✅ P |
| S44b | rozbalí se a nafoukne ještě za pádu | HAVOC PoC: *„inserting and inflating the airship … during the entry sequence“*, *„pressurized during parachute descent“*; HAVOC 2015: nafukování začne při 100 m/s | ✅ P |
| S45 | studie, nikdy schválená mise | interní studie NASA Langley; Wikipedie: NASA ji nikdy vážně nezamýšlela. Pozn.: HAVOC **počítal s heliem** (HAVOC 2015), ne se vzduchem. Scénář vzduch s HAVOC nespojuje, takže v pořádku | ✅ P + S |

## Kyselina (S49–S56)

| scéna | tvrzení | ověření | verdikt |
|---|---|---|---|
| S49 | mraky z kapek koncentrované kyseliny sírové | 75–98 % H₂SO₄ | ✅ S |
| S50 | naše pásmo leží mezi nimi | mraky ~47–70 km | ✅ S |
| S51 | kov koroduje, těsnění selhávají | obecně; výjimky (zlato, platina, tantal, sklo, PTFE) existují, a proto S52 | ✅ |
| S52 | materiály odolné kyselině známe, kyselina se v skle drží po staletí | Landis 2020: *„materials to avoid acid corrosion have been known for centuries“*; kyselina sírová se vyrábí a skladuje ve skle nejméně od 16. století (sklo napadá jen HF) | ✅ P + Pam |
| S53 | teflon měsíc v koncentrované kyselině, propouští ~90 % světla jako první den | HAVOC PoC: FEP v **75 a 85 %** H₂SO₄ na 1, 7 a 30 dní, *„negligible decay (within the 2% accuracy)“*, abstrakt *„90% transmittance … after 30 days“*. Test proběhl **v laboratoři, ne při 75 °C** — to pokrývá S55 | ✅ P |
| S54 | PVC začalo hnědnout do hodiny | *„began to turn brown an hour after immersion“* (75 %) | ✅ P |
| S55 | fólie v laboratoři není město v bouři | názor, podložený výhradou výš | ✅ |

## Energie a noc (S57–S63)

| scéna | tvrzení | ověření | verdikt |
|---|---|---|---|
| S57 | sluneční svit skoro 2× silnější | 1/0,723² = **1,91×** — ale **nad atmosférou**. Uvnitř mraků slábne: u spodku mraků 20–50 %, v 65 km ~95 % (Landis, studie solárních letadel) | ✏️ → *„so above the clouds, / sunlight is almost twice…“* |
| S58 | panel mířící dolů skoro stejně dobrý | **K tvé otázce:** Landis 2020 to tvrdí *„above the thick middle cloud layer“*; ze studií solárních letadel (Landis, NTRS) je konkrétní číslo pro **60 km**: odražené světlo = **90 %** dopadajícího. Je to výpočet z naměřených toků (Pioneer Venus), ne naměřený výkon panelu. Po opravě S57 scéna mluví o prostoru nad mraky, takže sedí | ✅ P (podmíněně) |
| S59 | planeta se otočí jednou za 243 dní, vzduch ne | 243,0 dne (siderická) | ✅ S |
| S60 | ve výšce města oběhne atmosféra za 6–7 dní | vítr 66–69 m/s ve 54 km (Vega) → 38 400 km / 67,7 m/s = **6,6 dne**; ve 50 km je vítr slabší (~60 m/s) → ~7 dní | ✅ M |
| S61 | noc ~3 dny | polovina oběhu = **3,3 dne**. **Pozor:** Landis 2003 píše *„roughly fifty hours“*, protože počítá se čtyřdenní rotací — ta ale platí pro **vršky mraků** (65–70 km), ne pro 50–55 km. Naše číslo je pro výšku města správné; kdyby se divák ohradil Landisem, tady je odpověď | ✅ M |
| S62 | marťanský den 24 h 40 min | sol = **24 h 39 min 35 s** | ✅ S |

## Voda a kyslík (S64–S70)

| scéna | tvrzení | ověření | verdikt |
|---|---|---|---|
| S64 | jedno z nejsušších míst, ~20 ppm vodní páry | ~20–30 ppm (§ 8); pro srovnání Mars má ve vzduchu ~200 ppm | ✅ S |
| S65 | kapky nejsou čistá kyselina, je v nich i voda | 75–85 % H₂SO₄ → **15–25 % vody** | ✅ M |
| S66 | v principu jde voda z kyseliny získat | Landis 2003: *„hydrogen reaped from condensing atmospheric sulfuric acid droplets“*; tepelný rozklad H₂SO₄ → H₂O + SO₃ | ✅ P |
| S67 | energeticky náročné, stroj nikdo nepostavil | ✅ | ✅ |
| S68 | Mars má led v zemi, dá se vykopat | Phoenix 2008 led vyhrabal; radar SHARAD našel ledové vrstvy ve středních šířkách | ✅ S |
| S69 | 2021 MOXIE vyrobil kyslík z CO₂ na Marsu | první běh 20. 4. 2021, celkem 122 g v 16 bězích | ✅ S |
| S70 | totéž by šlo na Venuši | Landis 2003: kyslík *„by zirconia electrolysis“* z CO₂, tedy princip MOXIE | ✅ P |

## Pevná zem (S71–S74)

| scéna | tvrzení | ověření | verdikt |
|---|---|---|---|
| S71–S72 | na Marsu skála a těžba, na Venuši vše ze vzduchu nebo ze Země | ✅ obecně. Landis 2003 navrhuje těžbu z povrchu robotem nebo lanem — je to vize, ne technika, takže „everything has to come from the air or from Earth“ platí pro dohlednou dobu | ✅ |
| S73 | nic nepřežilo na povrchu déle než ~2 hodiny | Venera 13, 127 min | ✅ S |
| S73b | balony asi dva dny; rovery na Marsu jezdí desítky let | Vega 46 h; Sojourner 1997, od roku 2004 nepřetržitě některý rover (Spirit, Opportunity, Curiosity, Perseverance), tedy 22 let | ✅ S |

## Cesta tam (S75–S77)

| scéna | tvrzení | ověření | verdikt |
|---|---|---|---|
| S76 | startovní okna každý rok a půl, k Marsu zhruba každé dva roky | synodická perioda 584 d (**19,2 měsíce**), Mars 780 d (**25,6 měsíce**); HAVOC PoC totéž slovy | ✅ P + M |
| S77 | zpáteční cesta i jen 14 měsíců | **K tvé otázce:** HAVOC 2015: **110 dní tam, 30 dní na místě, 300 dní zpět = 440 dní = 14,5 měsíce**, chemický pohon, aerocapture u Venuše i Země, setkání na oběžné dráze | ✅ P |
| S77 | k Marsu a zpět „well over two years“ | **Nesrovnává stejné se stejným.** 26+ měsíců (HAVOC PoC) je mise s dlouhým pobytem (konjunkční, ~900 dní, pobyt ~500 dní). Krátký pobyt na Marsu, 30 dní jako u Venuše, vyjde na **500–660 dní** (opoziční mise; Britannica, NASA), tedy 16–22 měsíců | ✏️ → *„And a round trip, / with a month spent at Venus, / could take as little as fourteen months. / The same short visit to Mars / takes a year and a half or more.“* Venuše vyhrává i tak |

## Cesta domů (S78–S82)

| scéna | tvrzení | ověření | verdikt |
|---|---|---|---|
| S79 | z Marsu start ze země, slabá gravitace | ✅ | ✅ |
| S80 | z Venuše raketa visící pod balonem | **K tvé otázce: ano.** HAVOC 2015 má **Venus Ascent Vehicle** pod vzducholodí vedle gondoly (výkres i model v PoC: *„gondola containing habitat and ascent vehicle“*); **dvoustupňová, LOX/RP-1, 63 t**, *„ascend from 50 km to orbit to rendezvous with TEI stage“*. Je to vzducholoď, ne balon, ale princip stejný | ✅ P |
| S81 | na oběžnou dráhu zhruba 2× rychleji než u Marsu | orbitální rychlost √(GM/r) ve 250 km: Venuše 324 859 / 6 302 → **7,18 km/s**, Mars 42 828 / 3 640 → **3,43 km/s**, poměr **2,09**. HAVOC 2015 navíc počítá s **9 km/s celkového Δv**, kdežto výstupní raketa z Marsu potřebuje ~4–4,5 km/s (Pam), takže poměr sedí i pro Δv | ✅ M + P |
| S82 | „haven't even launched anything from Mars“ | **Ingenuity** z Marsu vzlétla 72×, takže „anything“ neplatí. Platí, že **z Marsu nikdy nestartovala raketa** (výstupní raketa pro návrat vzorků se nikdy nepostavila) | ✏️ → *„We've never even launched a rocket / from Mars.“* |

## Závěr (S83–S88)

| scéna | tvrzení | ověření | verdikt |
|---|---|---|---|
| S83–S85 | „Mars isn't more Earth-like. In many ways, Venus is.“ | závěr z bodů výš, formulovaný jako názor | ✅ |
| S86 | z okna moře žlutých mraků | ve 55–56 km je člověk u horní hranice střední vrstvy mraků (50,5–56,5 km), takže dolů vidí mraky. Ve 50 km by byl v oparu. Básnický obraz drží pro výšku, kterou scénář jmenuje „higher up“ | ✅ |
| S87 | „ordinary air, at ordinary pressure“ | **Rozpor s S33b:** tam, kde je teplota pokojová a pod člověkem moře mraků (S86), je venku **půl atmosféry** a směs s víc kyslíkem. Obyčejný tlak je jen ve 50 km při 75 °C venku | ✏️ → *„at room temperature“* (zároveň odkaz na S11) |
| S87 | pec 50 km pod nohama | 50–56 km, „fifty“ je zaokrouhlení | ✅ |
| S88 | otázka do komentářů | podle `docs/cta.md` | ✅ |

## Co se změnilo ve v0.3 (souhrn)

S11, S15, S18, S19, S34, S35, S57, S77, S82, S87. Archiv `script 0.3.md`.
Kontrola délky řádků prošla (všechny ≤ 42 znaků). Homografy v nových
řádcích: žádné (*seeps*, *sealed*, *decompression* jsou bez rizika).

## Pro odpovědi v komentářích

- **„Landis říká noc 50 hodin“** → to je pro vršky mraků (rotace 4 dny);
  ve výšce města fouká 66–69 m/s, oběh 6–7 dní, noc ~3 dny (S61).
- **„Wikipedie: koule 1 km unese 700 000 t“** → pochází z Landise 2003, ale
  z jeho vlastního čísla 0,5 kg/m³ vychází 5,2·10⁸ m³ × 0,5 = **262 000 t**.
  Video číslo nepoužívá.
- **„HAVOC počítal s heliem“** → ano; video vzduch jako nosný plyn
  připisuje Landisovi a fyzice, ne HAVOC.
- **„Venera 13 vydržela 157 minut“** (HAVOC PoC) → správně 127 min.
- **„Ingenuity z Marsu vzlétla“** → proto S82 mluví o raketě.
