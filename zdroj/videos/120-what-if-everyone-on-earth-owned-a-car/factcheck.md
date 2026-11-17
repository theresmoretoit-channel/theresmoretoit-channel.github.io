# Fact check — 120 What If Everyone on Earth Owned a Car?

**Stav: ověřený číselný základ (2026-10-21), ještě ne plný průchod
scénářem.** Čísla dohledal agent z primárních zdrojů dřív, než vznikla
v0.1, a v0.1 je postavená na nich. Po škrtání uživatele se projde každé
tvrzení scénu po scéně (včetně vět, které vzniknou slitím).

Stažené PDF a výtahy jsou ve scratchpadu sezení (mimo git); doklad je
odkaz + citace tady.

## Ověřená čísla

| scéna | tvrzení | ověřeno | zdroj |
|---|---|---|---|
| S05 | *roughly eight vehicles for every ten people* | FHWA 2024: **271 085 742 lehkých vozidel** (osobní, SUV, dodávky, pickupy) / 339 058 370 obyvatel = **0,80**. Všechna motorová vozidla (vč. nákladních, autobusů, motocyklů) 297,5 mil. = 0,88. Formulace uživatele sedí na lehká vozidla | FHWA Highway Statistics 2024, MV-1, VM-1 (fhwa.dot.gov/policyinformation/statistics/2024/) |
| S06 | víc aut, SUV a pickupů než řidičů | lehká vozidla 271,1 mil. > **239 824 944 řidičských oprávnění** (DL-1C 2024). Tentýž zdroj, tentýž rok, takže srovnatelné, jak chtěl uživatel | FHWA 2024, DL-1C |
| S07 | *more than one and a half billion vehicles, one for every five people* | OICA 2020: **1 590 276 tis.**, 209 na 1 000 obyvatel. Novější číslo OICA nevydala | OICA, Total World vehicles in use 2020 |
| S08 | *the American level of motorization … about six and a half billion* (v0.3: dřív *that level*, divák to četl jako světovou úroveň 1 : 5) | 0,80 × 8,266 mld (UN WPP 2024, 1. 1. 2026) = **6,6 mld** | výpočet |
| S11–S12 | 2,5 × 5 m = 12,5 m², × 8 mld = 100 000 km², Jižní Korea | Jižní Korea **97 600 km²** (Světová banka 2024), tedy 1,02× | World Bank AG.LND.TOTL.K2 |
| S14 | 25–33 m² na stání s uličkami, dvě až tři Jižní Koreje, zhruba UK | **23–33 m²** (250–350 sq ft) na stání včetně příjezdů. 25 m² → 200 000 km² (2,0× Korea, 0,83× UK), 33 m² → 264 000 km² (1,09× UK 241 930 km²) | Litman, VTPI *Transportation Cost Analysis* 5.4 |
| S16 | parkuje ~95 % času | Shoup, *The High Cost of Free Parking* (2005), příl. B, z NPTS 1995; Barter přepočítal na 95–96,5 % | Shoup 2005 (z druhé ruky, stránka knihy neviděna) |
| S20–S21 | pruh: auta 600–1 600 lidí/h, autobusy do 8 000, tramvaje do 25 000 | NACTO: soukromá auta 600–1 600, **vyhrazený** pruh pro autobusy do 8 000, transitway do 25 000. Číslo pro autobus ve smíšeném provozu **neověřeno, nepoužívat** | NACTO Transit Street Design Guide (2016), přes výtah Strong Towns |
| S24 | Katy Freeway, přes 20 pruhů včetně postranních silnic, 2008, skoro 3 mld USD | dokončeno **říjen 2008**, **2,79 mld USD**; FHWA: 6+6 pruhů + 2 mýtné uprostřed + postranní silnice; Cortright „23 lanes", „26" jen v tisku. Proto *more than twenty* | FHWA project profile; City Observatory |
| S25 | 2011–2014 ráno +30 %, večer +55 % | TranStar přes Cortrighta: ráno +25 min (+30 %), odpoledne +23 min (+55 %). **Až po rozšíření, ne před/po**, a nejspíš různé trasy, proto *the morning commute… the evening one* bez tvrzení o téže trase | cityobservatory.org/reducing-congestion-katy-didnt-2/ |
| S29 | ~1,2 mil. mrtvých ročně | WHO: **1,19 mil.** (data 2021) | WHO Global status report on road safety 2023 |
| S31 | pětkrát víc aut | 8 / 1,59 = 5,0 | výpočet |
| S33 | 2024 ~93 mil. vozidel všech druhů | OICA **92 723 280** (osobní 67,7 mil.) | OICA, tabulka revidovaná 4/2026 |
| S34 | v Americe auto vydrží ~17 let | medián očekávané životnosti osobních aut v USA 2020 **~17 let** (SUV a dodávky 20, pickupy 25). Globálně spíš kratší, proto *In America* | Greene & Leard, *Transp. Res. A* 180 (2024) 103982 |
| S34–S35 | 93 mil. × 17 ≈ 1,5 mld ≈ dnešní park; *the fleet is still growing* | 1,58 mld vs. 1,59 mld, tedy **řádová shoda, ne ustálený stav**. Park roste: OICA 2015 **1 282 mil.** (947 osobních + 335 užitkových, přes Statista) → 2020 **1 590 mil.** = **+4,4 %/rok, ~62 mil. ročně**. Proto v v0.3 škrtnuto *Our factories mostly replace the cars that wear out* (při 93 mil. výroby a 62 mil. přírůstku se šrotuje jen ~30 mil.) | výpočet; OICA přes statista.com/statistics/281134 |
| S36 | pětkrát víc ročně | 8 mld / 17 = 470 mil./rok = **5,1×** | výpočet |
| S37–S38 | 10 000 km, 7 l/100 km → ~96 mil. barelů **benzínu** denně (v0.3: dřív *of oil*) | 8e9 × 10 000 × 0,07 = 5,6e12 l/rok = **96,4 mb/d**. USA 17 360 km/auto (VM-1), EU **10 800 km** (2023, Odyssee-Mure: *„on average 10,800 km/year for the EU"*, rozpětí 6 000 Litva až 17 000 Irsko; S37 v obraze opraveno z ≈ 11 000); 7,1 l/100 km je norma **nových** aut (GFEI 2019), park v USA jezdí za 10 l. **Oba předpoklady jsou konzervativní** | FHWA VM-1 2024; GFEI 2021; odyssee-mure.eu/publications/efficiency-by-sector/transport/distance-travelled-by-car.html (staženo 2026-10-21) |
| S39 | svět ~103 mil. barelů denně | IEA: **102,9 mb/d** v roce 2024. IEA měří poptávku po ropě jako dodané **produkty** (barely produktu), takže barely benzínu jsou s ní srovnatelné objemem. Výhrada: rafinerie nevyrobí z barelu jen benzín, takže skutečná potřeba ropy je vyšší → formulace drží | IEA Oil Market Report 2/2025 |
| S55 | *almost as much fuel as the whole world uses today* (v0.3: dřív *nearly all of today's oil*) | 96 / 103 = 94 % objemu všech dnešních ropných produktů; *almost* drží, *all of today's oil* by tvrdilo surovou ropu | výpočet z S38–S39 |
| S41 | 2 000 kWh/rok, polovina světové elektřiny | 0,2 kWh/km včetně ztrát při nabíjení (EPA 0,19–0,22) × 10 000 km; × 8 mld = **16 000 TWh = 52 %** z **30 856 TWh** (Ember 2024). Údaj IEA 30 664 TWh agent nedohledal, použito Ember | Ember Global Electricity Review 2025; fueleconomy.gov |
| S42 | jen na výměnu baterií ~30× dnešní produkce | 8 mld × 65 kWh (průměr IEA) / 17 let = 30,6 TWh/rok vs. **950 GWh** baterií do aut v roce 2024 = **32×** | IEA Global EV Outlook 2025 |
| S47 | skoro tři z deseti jsou děti, ~2,4 mld | UN WPP 2024: **2,407 mld pod 18 let z 8,266 mld = 29,1 %** (1. 1. 2026). „Nearly a third" by nadsazovalo | UN WPP 2024 |
| S49 | v USA skoro tři z deseti nemají řidičák | 1 − 239,8 / 339,1 = **29,3 %** (většinou děti) | FHWA 2024 DL-1C, VM-1 |

## Zbývá ověřit

- S26 indukovaná poptávka (definice), S27, S30 (faktory nehodovosti),
  S43 (noční nabíjení), S52 (venkov).
- Po škrtání: přečíslování a kontrola, že fragment každého řádku
  tabulky je opravdu v uvedené scéně.

## Nepoužito

- **Ocel (v0.1 S37), vyřazeno v v0.2 podle pravidla uživatele: číslo jen výslovně ověřené.** 2024 bylo 1 882,6 Mt surové oceli (worldsteel, primárně). „~900 kg na auto" se ale přisuzuje worldsteel jen v druhé ruce (S&P, AMS), stránky worldsteel se nenačtou (vykresluje je JavaScript) a archiv nejde stáhnout. Navíc se srovnávala hotová ocel v autě s výrobou surové oceli. Vychází 7,2 / 1,88 = 3,8 roku.

- AAA 2026: nové auto stojí **12 863 USD ročně** (blok o ceně vypadl).
- Baterie: 480–520 TWh na celý park = ~500 let dnešní produkce
  (~145 let při plné kapacitě továren 3,3 TWh). Použita varianta
  „výměna", protože sedí s výrobou aut (S36).
