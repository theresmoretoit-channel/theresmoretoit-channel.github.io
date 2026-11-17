# 132 — fact check scénáře v0.4 (2026-11-02)

Zdroje, citace a výpočty jsou v `factcheck-zaklad.md`; tady je přiřazení ke
scénám a závěr. **A** = rešerše A (létající auta, historie), **B** = rešerše B
(eVTOL, hluk), **C** = rešerše C (fyzika, bezpečnost, pilot, provoz),
**V** = výpočet vznášení nahoře v základu. Výpočty jsou přepočítané, ne opsané.
Stav k 2. 11. 2026 — **řádky označené 🔁 přeověřit těsně před nahráním.**

| scéna | tvrzení | ověření | závěr |
|---|---|---|---|
| S01 | auto má osvědčení, že smí létat | A §5 AirCar: Certificate of Airworthiness, Dopravný úrad SR. Je to individuální osvědčení na **jeden prototyp**, ne typové osvědčení EASA; „this car" ukazuje na ten jeden kus, takže sedí | ✅ |
| S02 | slovenský úřad, 2022, 70 h ve vzduchu, víc než 200 vzletů | A §5: GA News 25. 1. 2022 „70 hours of flight testing … more than 200 takeoffs and landings". Úřad je Dopravný úrad (divize civilního letectví) → „aviation authorities" je volný, ale věcně správný popis. Tisková zpráva KV z 9/2026 uvádí rok 2023 — všechna dobová média 2022, držíme 2022 | ✅ |
| S03 | „not the first"; 1956 vláda USA certifikovala auto, které umělo létat | A §3: Aerocar, CAA prosinec 1956 (CAA = federální úřad, předchůdce FAA; scénář správně neříká „FAA"). Prvním certifikovaným byl Airphibian 1950 — scénář netvrdí, že Aerocar byl první | ✅ |
| S04 | postavilo se šest; zájemců málo, do výroby se nedostal | A §3: HistoryNet „too few buyers signed on and only six Aerocars were built" (HistoryLink 5–7 podle počítání) | ✅ |
| S05 | postavili jsme je znovu a znovu | A: Airphibian, ConvAirCar, Aerocar, Transition, AirCar, PAL-V, Switchblade, Alef | ✅ |
| S06 | proč je nikdo nepoužívá | A §5 souhrn: **žádný zákazník nemá moderní létající auto** (absence dokladu). Alef slibuje první dodávky „do konce 2026" pár testovacím zákazníkům | ✅ 🔁 Alef |
| S11 | auto musí být pevné a dost těžké, letadlo co nejlehčí | Piper 1949 (A §4): „the light weight essential for flying works against its performance as an automobile, making it frail and flimsy" | ✅ |
| S12 | auto se vejde do pruhu, letadlo potřebuje křídla širší než silnice | pruh ~3,5 m, dvoupruhová silnice ~7 m; Curtiss Autoplane 12,34 m (A §1), lehká letadla ~10–11 m. Platí pro letadlo, ne pro všechna létající auta (ta křídla skládají — S13) | ✅ |
| S13 | křídla se skládají, odnímají, nebo zůstanou | skládá AirCar, Switchblade, PAL-V (rotor); odnímá Aerocar (tahá je jako přívěs); ConvAirCar si křídlo půjčoval na letišti (A §2, §3, §7) | ✅ |
| S14 | nizozemské létající auto s povolením na silnici potřebuje 180 m dráhy jen ke vzletu | A §5 PAL-V: homologace RDW 2020; pal-v.com „vzletový rozjezd 180 m (MTOW, hladina moře)". Je to vírník — „flying car" se o něm běžně říká, výrobce sám „flying car" | ✅ |
| S16–S17 | Piper 1949: „neither a good plane nor a good automobile" | A §4: *Private Flying: Today and Tomorrow* (1949), cit. HistoryNet doslova; „aircraft maker" = zakladatel Piper Aircraft | ✅ |
| S18 | o dva roky dřív to americká firma zkusila obejít | Convair, 1947 (A §2). „Obejít" je výklad obchodního modelu, ne citace | ✅ |
| S19 | auto koupit, křídlo si pronajmout na letišti | A §2: San Diego Union 16. 11. 1947 „sell the automobile part … and rent him the flying part". Byl to **návrh**, ne zavedený prodej — anglické *you'd* to nese, překlady opraveny (v0.3) | ✅ |
| S20 | poprvé vzlétlo v listopadu 1947 | A §2: 15. 11. 1947, Lindbergh Field, 1 h 18 min (infobox Wikipedie „1. 11." je chyba) | ✅ |
| S21 | o tři dny později mu docházelo palivo, nouzově přistál na bahnitých pláních u San Diega | A §2: SDASM „On November 18, 1947 … low fuel forced landing near San Diego"; NYT 19. 11. 1947 „Lands in California Mud Flats". 15. → 18. = tři dny | ✅ |
| S22 | traduje se, že pilot zkontroloval špatný ukazatel paliva, ten pro auto | A §2: v primárních zdrojích **není**; Wikipedie „reportedly", sloupek 2026. Scénář to uvádí jako „the story goes" a S23 „whether or not that's true" — tak je to v pořádku | ✅ (s výhradou v textu) |
| S24–S25 | dnešní „létající auta" jsou většinou malá letadla se svislým vzletem | B §1: hlavní projekty (Joby, Archer, EHang, Wisk, Vertical, Alef, ASKA) jsou VTOL; silniční letadla s dráhou jsou hrstka (AirCar, PAL-V, Switchblade). S77 je pak odliší jako „air taxis, not flying cars" — S25 mluví o tom, čemu se tak běžně říká, takže si to neodporuje | ✅ |
| S27 | auto při 100 km/h potřebuje asi 13 kW | C §6a: koeficienty EPA, Corolla 13,3 kW, Camry a Civic 12,5, Model 3 14,0 | ✅ |
| S28 | váhu nese silnice, motor ho jen protlačuje vzduchem | C §6a Corolla při 100 km/h: A + B·v = 25,0 + 11,8 = 36,8 lbf (valivý odpor a ztráty), C·v² = 70,7 lbf (vzduch). **Vzduch je ~2/3, třetina je valivý odpor**, který s hmotností roste. Pointa (silnice nese váhu, motor ji nemusí držet) platí, v0.4 proto *„only has to keep it moving"* | ✅ (v0.4) |
| S29 | vznášející se stroj nese celou váhu sám tím, že vrhá vzduch dolů | teorie hybnosti (V) | ✅ |
| S30 | u stroje velikosti auta 20–40× víc výkonu | V: Kasliwal 2019 (1 188 kg) 250,6 kW = **19×**; Joby S4 na hřídeli 350–525 kW = **26–39×**; 1,5 t s rotory v půdorysu auta ~570 kW = **43×**. „Size of a car" čteme jako hmotnost auta; rotory těch strojů se do půdorysu auta nevejdou, s nimi by vyšlo víc — tvrzení je tedy **při spodní hraně**, ne přehnané | ✅ |
| S31 | čím menší rotory, tím hůř | P ∝ 1/√A (V) | ✅ |
| S32 | vrtulník zvládne totéž asi s desetinásobkem výkonu auta | V: R44 ~120 kW na hlavní rotor = **9×**, trvalý výkon motoru 153 kW = 11,5× | ✅ |
| S33 | ale jen proto, že má rotor deset metrů | EASA TCDS R44: 10,06 m. „Only because" je zkratka: R44 je i lehčí (1 134 kg); při 1 500 kg by vyšel ~14×, pořád pod pásmem 20–40 | ✅ |
| S34 | úsporný právě proto, že by se na silnici nevešel | rotor 10 m proti silnici ~7 m | ✅ |
| S34b | levné držení ve vzduchu by chtělo něco úplně nového, třeba antigravitaci, a to je daleko za tím, co umíme postavit (v0.5) | Žádný známý mechanismus antigravitace neexistuje; obecná relativita ani experimenty nedávají způsob, jak gravitaci stínit nebo obrátit (antihmota padá dolů, ALPHA-g 2023). „Far beyond anything we know how to build“ je proto spíš mírné — tvrzení nepřehání | ✅ |
| S36 | kilogram benzínu má asi 50× víc energie než kilogram dnešní bateriové sady | C §5: benzín 12 060 Wh/kg (LHV), sada Joby 235 Wh/kg → **51×** | ✅ |
| S37 | elektromotory plýtvají mnohem méně, baterie i tak dodá jen asi patnáctinu | C §5: benzínový motor 25–30 %, elektrický pohon ~90 % → 3,0–3,6 vs 0,21 kWh/kg užitečné práce = **14–17×** | ✅ |
| S38 | nádrž s ubývajícím palivem lehne, baterie ne | Li-ion článek při vybití hmotnost nemění | ✅ |
| S41 | soukromá pilotní licence: v Evropě nejméně 45 h, v praxi obvykle víc | C §3a: EASA FCL.210.A 45 h ✅; „usually more": AOPA 50–70 h (USA), britské rozpočty ~55 h. **Ale UK má od 10/2025 40 h** (C §3a, past 1) — v0.4 proto *„at least forty hours"*, což platí všude (ICAO, FAA, UK 40 h; EASA 45 h) | ✅ (v0.4) |
| S42 | v USA asi 1 400 řidičů na soukromého pilota | C §3d: FHWA 2023 237,7 mil. řidičů / FAA 2024 172 012 aktivních soukromých pilotů letounů = **1 382** | ✅ |
| S47 | v simulaci NASA zvládl jeden člověk na zemi bezpečně dohlížet na tři letadla | Aerospace America 15. 7. 2026: „Four days of flight simulations conducted by NASA and … Wisk", „conducted at the agency's Ames Research Center", řídící dodala NASA; AIN 30. 7. 2026 „Wisk Aero and NASA have simulated a single ground-based supervisor managing three autonomous aircraft". Společná simulace NASA–Wisk v NASA Ames → „a NASA simulation" drží; je vázaná na **jednu** simulaci, jak uživatel chtěl | ✅ |
| S49 | v Číně má bezpilotní aerotaxi osvědčení od 2023 | B §1: EH216-S, typové osvědčení CAAC říjen 2023 (Aviation Week) | ✅ |
| S50 | ještě nevezlo platícího cestujícího | B §1: EHang 6-K 9. 6. 2026 „ahead of the launch of public ticketed flight services", jen „internal trial commercial operations"; 8/2026 stažený výhled kvůli opatrnosti regulátora | ✅ 🔁 EHang Q3 (konec listopadu) |
| S55b–S55c | antigravitace by dovolila zastavit na „krajnici na nebi“, jen by se nedalo vystoupit a dojít pěšky (v0.5) | nadsázka navazující na S34b, nic netvrdí | ✅ |
| S56 | na hodinu cesty je soukromé létání asi 50× smrtelnější než jízda autem | C §1: NTSB 2024 personal flying 199 mrtvých / 8,457 mil. h = 2,35 / 100 tis. h; auto NHTSA 2023 40 901 / AAA 95 mld. h = 0,043 / 100 tis. h → **55×**. **Na hodinu**, ne na míli (NTSB nemá nalétané míle). Silniční mrtví zahrnují chodce a cyklisty, takže pro posádky aut by násobek vyšel ještě vyšší — „about fifty" je konzervativní | ✅ |
| S57–S58 | nad městem nejsou v ohrožení jen lidé na palubě | NTSB 2024: 300 z 305 mrtvých GA na palubě — dnes je to malé číslo, scénář mluví o tisících strojů nad městem. Logická úvaha, ne statistika | ✅ |
| S60 | nejnovější aerotaxi jsou opravdu mnohem tišší než vrtulníky | B §4: Joby < 65 dBA na 100 m při vzletu a přistání; vrtulníky SEL 81–85 dB(A) na 150 m (EASA TCDS). Různé metriky, rozdíl ~15–20 dB → „much quieter" kvalitativně sedí; číslo záměrně nepoužito | ✅ |
| S63 | São Paulo: jedna z největších vrtulníkových flotil, ~400 vrtulníků, ~260 heliportů | B §5: Abraphe ~410 vrtulníků, ~260 heliportů; „capital mundial do helicóptero" je tvrzení Abraphe, scénář říká opatrněji „one of the biggest". Všechna čísla z jednoho zdroje | ✅ (⚠ jediný zdroj) |
| S66 | Londýn má víc než 2,5 mil. aut | C §4c: DfT VEH0105, London Cars 2 663 653 (2026 Q2) | ✅ |
| S67 | jedno auto ze sta → přes 26 tisíc letadel | 2 663 653 / 100 = **26 637** | ✅ |
| S68 | to je víc, než kolik jich je naráz ve vzduchu nad celou planetou | C §4b: FR24 > 22 000 (5/2023), AirNav 24 115 (6/2025), oba sekundární. 26 637 / 24 115 = **1,10** — rezerva jen 10 % a trackery vidí jen letadla s transpondérem ADS-B; neviditelné všeobecné letectví by ji mohlo smazat → v0.4 *„about as many as"* | ✅ (v0.4) |
| S69 | ve špičce USA zvládají ~5 500 letů ve vzduchu naráz | C §4a: FAA FY2024, peak day 25. 7. 2024 „an average of 5,500 IFR flights enroute … maximum of 5,700". Jen lety IFR (bez VFR) — o řízených letech scénář mluví, sedí | ✅ |
| S70 | potřebují na to 14 tisíc řídících | C §4a: FAA „Controllers 14,264" — celý stav, na všechny směny a 44 tis. letů denně; „it takes … to do it" čteme jako celý systém | ✅ |
| S71 | každý let má přidělenou trasu, výšku a předem podaný letový plán | definice letu IFR | ✅ |
| S76–S77 | firmy, které je dnes stavějí, potichu změnily plán: neprodávají létající auta, stavějí aerotaxi | B §1, §3: Joby, Archer, EHang, Wisk, Vertical — aerotaxi s operátorem ✅. **Ale** Klein Vision, PAL-V, Alef, Samson a ASKA pořád prodávají (předobjednávky) soukromníkům (A §5) → v0.4 *„the biggest companies"* | ✅ (v0.4) |
| S78 | málo letadel, profesionální piloti, pár tras | B §3: Joby a Archer s pilotem (FAA JAS4-1 „single pilot onboard"), trasy letiště ↔ město | ✅ |
| S79 | Joby v Dubaji: čtyři přistávací místa, jedno na letišti | B §1: vertiporty DXB, American University of Dubai, Atlantis The Royal, Dubai Mall (Joby 17. 11. 2025); provoz zatím nezačal (Motley Fool 30. 10. 2026) | ✅ 🔁 Joby Q3 4. 11. |
| S81 | Lilium a Volocopter podaly insolvenční návrh do dvou měsíců od sebe | B §2: Lilium 28. 10. 2024 (Weilheim), Volocopter 26. 12. 2024 (Karlsruhe) → **59 dní**. Lilium podruhé a definitivně 21. 2. 2025 | ✅ |
| S82 | Airbus pozastavil projekt, baterie prý nejsou připravené | B §2: CityAirbus NextGen pozastaven 27. 1. 2025, „battery technology not mature" (AIN) | ✅ |
| S83 | zatím nikde na světě takové aerotaxi nevozí platící cestující | B: žádný eVTOL nevozí platící (ani EHang, ani Joby v Dubaji). Vrtulníky (Blade) vozí — „like this" je proto nutné a je tam | ✅ 🔁 Joby, Archer, EHang |
| S85 | vrtulníková doprava, jen tišší a možná levnější | Blade Manhattan–JFK od 195 $ (B §5 ⚠); RTA Dubaj: levnější než vrtulník (B §3 ⚠); „maybe" | ✅ |

## Změny angličtiny v0.4 (schválil uživatel 2026-11-02)

| scéna | proč | v0.3 | návrh |
|---|---|---|---|
| S41 | UK má od 10/2025 40 h; „in Europe" zahrnuje Británii, a publikum je anglické. ICAO, FAA i UK mají 40 h, EASA 45 → „at least forty" platí všude | *at least forty-five hours in the air / in Europe, / and in practice usually more.* | *at least forty hours in the air, / and in practice usually more.* (o řádek míň, překlady se upraví) |
| S68 | rezerva 10 % proti sekundárnímu číslu z trackerů | *That's more than are in the air* | *That's about as many as are in the air* |
| S76 | AirCar, PAL-V, Alef, Samson pořád prodávají soukromníkům | *Which is why the companies* | *Which is why the biggest companies* |
| S28 | třetina výkonu je valivý odpor (volitelné, pointa platí i tak) | *The engine only has to push it / through the air.* | *The engine only has to keep it moving.* (o řádek míň) |

## Přeověřit před nahráním 🔁

- Joby Q3 (4. 11. 2026): Dubaj, první platící cestující? → S79, S83
- Archer Q3 (polovina listopadu): Abú Dhabí → S83
- EHang Q3 (konec listopadu): veřejné lety s jízdenkou? → S50, S83
- Alef: dodávka prvním zákazníkům „do konce 2026"? → S06

### Přeověřeno 2026-11-02 večer (webové vyhledávání)

| scéna | stav | zdroj |
|---|---|---|
| S06 Alef | **platí** — dodávky zatím nezačaly; „první várka do konce 2026“, nejvýš ~10 kusů (Kalifornie, Hongkong) | Electrek 19. 5. 2026; Flying |
| S50, S83 EHang | **platí** — v Q2 (25. 8. 2026) stažený výhled kvůli zdržení schvalování placených letů, jen zkušební provoz; AllFlyingCars k 17. 10. totéž. Blog evtol.travel (5/2026) tvrdí spuštění v březnu — proti pozdějšímu oficiálnímu 6-K neplatí | Venture Atlas; allflyingcars.com |
| S79, S83 Joby | **platí** — první cestující „před koncem 2026“, chybí vertiporty a povolení GCAA | Motley Fool 2. 10. a 30. 10. 2026 |
| S83 Archer | **platí** — Abú Dhabí v certifikaci (GCAA RTC od 7. 5. 2026), start konec 2026 / začátek 2027 | Gulf News; Arabian Business |

**Riziko:** Joby i Alef míří na „konec 2026“. Pokud video vyjde až v prosinci,
přeověřit znovu (Joby Q3 4. 11. 2026).
