# 169 — fact check (`script 0.5.md`)

2026-11-22. Podklad: externí kontrola uživatele (`zpetna vazba 0.3.txt`)
a vlastní rešerše agenta. Sloupec **ověřil** rozlišuje, kdo zdroj viděl:
**A** = agent dohledal sám, **U** = převzato z kontroly uživatele (zdroj
pojmenovaný tam, agent ho neotvíral). Kde se obojí rozešlo, je to
v poznámce.

Závěr: ✅ potvrzeno · ✏️ zpřesněno ve 0.4 · ⚠️ slabší opora, formulace
zvolená tak, aby ji unesla.

## S01–S14 Paradox a zeď

| scéna | tvrzení | ověření | ověřil | závěr |
|---|---|---|---|---|
| S01 | 1977 Londýn–NY za ~3,5 h | BA zahájila provoz 21. 1. 1976 do Bahrajnu; Londýn–New York (JFK) až **22. 11. 1977**, let pod 3,5 h. **0.3 mělo 1976 — chyba.** | U (British Airways, *Celebrating Concorde*) | ✏️ |
| S02 | dnes 7–8 h | běžný jízdní řád LHR–JFK ~8 h, JFK–LHR ~7 h | U | ✅ |
| S04 | 747 v provozu 1970, ~M0,85 | Pan Am leden 1970 | U | ✅ |
| S05 | dnešní letadla ~M0,85 | 787 / A350 typická cestovní M0,85 | U | ✅ |
| S09–S12 | vzduch nad křídlem rychlejší, lokálně nadzvukový, rázová vlna, prudký nárůst odporu | standardní transonická aerodynamika; NASA o rázových vlnách | U (NASA) | ✅ zjednodušení |
| S13 | „for many airliners… 80–85 %" | rozsah, ne pevná mez — formulace to říká | U | ✅ |

## S15–S24 Palivo a Whitcomb

| scéna | tvrzení | ověření | ověřil | závěr |
|---|---|---|---|---|
| S15–S16 | víc odporu → víc tahu → víc paliva na km | fyzika | — | ✅ |
| S17 | palivo „a quarter to a third" nákladů | IATA: 2024 **31 %** provozních nákladů; v jiných letech kolem čtvrtiny | U (IATA, *Airline Profitability Outlook* 2024) | ✏️ |
| S18–S20 | volba rychlosti = kompromis palivo × čas | princip cost indexu; formulace bez tvrzení, že optimum leží u zdi | — | ✅ |
| S21 | některé verze 707 (60. léta) až M0,90, běžně ~0,82 | 707-320B (1962): max. cestovní M0,90 / MMO 0,90–0,91, ekonomická M0,82; IPCC: první jety typicky M0,82–0,84 | A ([707-320B data](https://aircraftinvestigation.info/airplanes\707-320B.html)), U (IPCC) | ✏️ „some versions", rok 1958 nahrazen „1960s" (−320B je z 1962) |
| S22–S24 | Whitcomb, NASA, superkritické křídlo; využito spíš na úsporu | NASA, *How a NASA Engineer Created the Modern Airplane Wing* | U | ✅ |

## S25–S28 Convair 990

| scéna | tvrzení | ověření | ověřil | závěr |
|---|---|---|---|---|
| S25 | 1962 v provozu, nejrychlejší dopravní letadlo | certifikace 1961/62, 621 mph | A ([Wikipedia](https://en.wikipedia.org/wiki/Convair_990_Coronado), [SlashGear](https://www.slashgear.com/1803289/convair-990-coronado-jet-about-passenger-plane-why-failure-considered-flop)) | ✅ |
| S26 | nedosáhl slíbené rychlosti; víc paliva než 707 | v horizontálním letu max. **M0,84 proti garantovaným 0,89** pro American; vysoká spotřeba, nesplnil garance rychlosti a spotřeby | A ([Wikipedia](https://en.wikipedia.org/wiki/Convair_990_Coronado), [HistoryNet](https://historynet.com/why-convairs-speedy-990-lost-out-to-the-boeing-707/)) | ⚠️ viz pozn. |
| S27 | 37 kusů | | A, U (Verkehrshaus) | ✅ |

**Pozn. k S26:** kontrola uživatele navrhla *„barely beat the 707's
scheduled times"*. Agent to **nepoužil**: srovnání jízdních řádů stojí jen
na Wikipedii (tvrzení označené *original research?*) a na příspěvku
z fóra PPRuNe. Doložené je, že 990 **nesplnil slíbenou rychlost**, a to
nese tentýž argument. Původní „less than an hour" (0.3) bylo z populárního
tisku a vypadlo. „More fuel than the 707" je ze sekundárních zdrojů
(nesplněná garance spotřeby); kdyby se našel tvrdý údaj na sedadlo, doplnit.

## S29–S40 Concorde

| scéna | tvrzení | ověření | ověřil | závěr |
|---|---|---|---|---|
| S29 | 2× rychlost zvuku, > 2 000 km/h | M2,02, ~2 140 km/h | U | ✅ |
| S31 | ~100 lidí, na cestujícího ~3× palivo proti 747 | NOVA/PBS: 15,8 vs 46,4 pax-mil/galon (2,9×); trasa LON–NYC 157,6 vs 57,7 galonu/cestujícího (2,73×). **Modelový výpočet** s pevnou obsazeností. | A ([NOVA/PBS](https://dipsy.pbs.org/wgbh/nova/teachers/activities/3203_concorde_02.html)), U | ✅ „roughly" |
| S33 | třesk po celé trase, pás „dozens of km" | USAF: z 30 000 stop pás ~30 mil (48 km) | U (af.mil) | ✅ |
| S34 | 1973 zákaz civilního nadzvukového letu nad USA | FAA, účinné **27. 4. 1973**; nad pevninou a teritoriálními vodami USA. **Vizuál nesmí ukazovat zákaz nad celým světem.** | U (FAA *Historical Chronology*), A ([Federal Register 2026](https://www.federalregister.gov/documents/2026/07/02/2026-13440/enabling-supersonic-overland-flight) cituje 14 CFR 91.817) | ✅ |
| S35 | 20 postaveno; trasy hlavně Londýn/Paříž–NY | | U | ✅ |
| S36 | navržen v 60. letech, levné palivo | | U | ✅ |
| S37 | začátek 1973 odstoupily americké aerolinky (opce), říjen 1973 ropná krize | Pan Am a TWA leden/únor 1973 — **opce, ne pevné objednávky**; embargo říjen 1973; scénář výslovně „two separate blows" | U (heritage-concorde) | ✏️ „held options on it" |
| S38 | 1997 zpáteční NY–Londýn „over eight thousand dollars" | Britannica $7 995; Travel Weekly 8/1997 **$8 226**; Washington Post 10/1997 $8 547 | A ([Britannica](https://www.britannica.com:443/question/How-much-was-a-ticket-on-the-Concorde)), U ([Travel Weekly 20. 8. 1997](https://www.travelweekly.com/Travel-News/Airline-News/Concorde-Fares-Cut-Through-97), [Washington Post 26. 10. 1997](https://www.washingtonpost.com/archive/lifestyle/travel/1997/10/26/worldwise/2fabcb5d-4308-4b4d-9036-9adefce553b0/)) | ✏️ |
| S39–S40 | drahý provoz a údržba; havárie 2000, propad po 9/2001, konec 2003 | BA v oznámení: klesající příjmy, rostoucí náklady na údržbu | U (BA retirement) | ✅ |

**Pozn. k S38:** tři zdroje dávají $7 995–8 547. Rozhodl uživatel 2026-11-22: **„over eight thousand"** — dobové zdroje (dva ze tří) mají přednost před pozdější encyklopedií; rozdíl je nejspíš tarif a dopravce.

## S41–S48 Sonic Cruiser

| scéna | tvrzení | ověření | ověřil | závěr |
|---|---|---|---|---|
| S42 | volba „in the early 2000s" | představen **březen 2001**, rozhodování 2002. **0.3 mělo „in 2001… that year" — nepřesné.** | U (AP 11/2002), A | ✏️ |
| S43 | 2001, až M0,98, o 15–20 % rychlejší | | A ([Wikipedia](https://en.wikipedia.org/wiki/Boeing_Sonic_Cruiser), [Flight International](https://www.flightglobal.com/sonic-cruiser-a-different-boeing/74989.article)), U (Boeing 7/2001) | ✅ |
| S44 | 2002 Boeing s aerolinkami probíral druhou variantu, o 17–20 % nižší spotřeba než 767 | AP 11/2002: Boeing jednal s ~dvěma desítkami aerolinek; 17–20 % lepší spotřeba proti 767. **0.3 mělo „15–20 % nižší provozní náklady" — to je jiná veličina.** | U (AP přes Vindy Archives) | ✏️ |
| S46 | 2002 zrušen, přechod k efektivitě → 787 | prosinec 2002 | A ([NPR](https://www.npr.org/2002/12/21/887162/boeing-drops-plans-for-high-speed-jet)), U | ✅ |
| S47 | „trade-off that hurt the Convair" | Convair měl i vlastní problémy (nesplněné garance, konkurence) → „hurt", ne „sank" | U | ✏️ |
| S48 | „Again and again, airlines chose efficiency over speed" | zobecnění tří doložených případů místo „every time" | U | ✏️ |

## S49–S57 Co se zlepšilo

| scéna | tvrzení | ověření | ověřil | závěr |
|---|---|---|---|---|
| S51 | nové letadlo dnes ~poloviční spotřeba na sedadlo proti novému z 60. let | ICCT 2009: nová letadla 1960→2008 ~2× efektivnější na sedadlo-km; ICCT 2015: −45 % 1968→2014 | A ([ICCT](https://theicct.org/publications/efficiency-trends-new-commercial-jet-aircraft-1960-2008)), U | ✅ |
| S53 | USA, medián domácí zpáteční letenky, reálně, „almost forty percent" 1980→2005 | GAO-06-630 (2006): *„the median fare has declined almost 40 percent since 1980 as measured in 2005 dollars"*. **Kontrola uživatele uvádí 38 % — v textu GAO agent našel „almost 40".** Nahrazuje údaj A4A 1979–2016 (oborová skupina). | A ([GAO-06-630](https://www.gao.gov/products/GAO-06-630)) | ✏️ |
| S54 | „air travel exploded"; 1970 „a few hundred million", 2019 4,5 mld. (do v0.6 „the number of people flying exploded", změněno 2026-11-23: ICAO počítá přepravené cestující, ne unikátní osoby) | ICAO: ~310 mil. (1970), ~4,5 mld. (2019), ~14,7× | U (ICAO / World Bank *Air transport, passengers carried*) | ✅ |
| S56 | 1970 létání mimo rozpočet mnoha rodin; dostupné „far more people" | historická interpretace; kvantifikace „hundreds of millions more people" **vypadla**, protože počet cestujících ≠ počet unikátních lidí | U | ⚠️ interpretace, bez čísla |
| S66 | „more than ten times as many passengers a year" (do v0.6 „as many of us", tedy osoby; změněno 2026-11-23, viz S54) | 14,7× přepravených cestujících za rok (z S54) | U | ✅ |

## S58–S67 Epilog

| scéna | tvrzení | ověření | ověřil | závěr |
|---|---|---|---|---|
| S59 | X-59 má udělat výrazně tišší třesk, tvar rozloží rázové vlny | NASA Quesst; jde o **celkový tvar**, ne jen nos | U (NASA) | ✏️ |
| S60 | 2026 poprvé nadzvukově | **5. 6. 2026**, ~M1,1, 43 400 ft. (První let vůbec 28. 10. 2025 — nezaměnit.) | A ([NASA](https://www.nasa.gov/aeronautics/x-59-first-supersonic-flight/)), U | ✅ |
| S61 | 2026 návrh nahradit zákaz limitem na třesk; jen návrh | FR 2026-13440, 2. 7. 2026, 0,11 psf na povrchu; připomínky do 17. 8. 2026; finál cílen pol. 2027. K 22. 11. 2026 **návrh**. | A ([Federal Register](https://www.federalregister.gov/documents/2026/07/02/2026-13440/enabling-supersonic-overland-flight)), U | ✅ |
| S62 | Boom Overture, první let „late 2020s" | zdroje se rozcházejí: Wikipedia infobox 2027 / text 2028, aerocorner (2026) 2027, Forecast International pochybuje. **Konkrétní rok vypuštěn.** | A ([Wikipedia](https://en.wikipedia.org/wiki/Boom_Overture), [aerocorner](https://aerocorner.com/aircraft/boom-overture/), [Forecast Intl.](https://flightplan.forecastinternational.com/2025/08/25/boom-supersonic-overture-airliner-program-outlook/)) | ✏️ firemní harmonogram |
| S64 | „We could in the 1970s" | Concorde v provozu od 1976 | — | ✅ (místo „1976", ať nekoliduje s S01 = 1977) |

## Co zbývá

- **S26** „more fuel than the 707" — jen sekundární zdroje.
- Zdroje označené **U** agent sám neotvíral; kdyby na nějakém z nich
  visela otázka diváka, dohledat primární text.
