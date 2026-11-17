# 125 — fact check (v0.2 → v0.3, 2026-10-25; formulace v0.4)

Čísla scén odpovídají **v0.3** (číslování stejné jako v0.1 a v0.2).
U každé položky je uvedeno, co se doopravdy četlo.

Stav: **potvrzeno** · **částečně** (sedí po úpravě nebo s výhradou) ·
**přepsáno** (v0.2 neodpovídala zdroji) · **spočteno** (odvozeno
z konstant, výpočet níž).

---

## 1. Apollo 11 a Saturn V (S01–S05, S29–S36)

**Primární zdroje, čtené v PDF:**
- *Apollo 11 Mission Report*, MSC-00171 (NASA 1969), tab. A-I „Mass
  properties" (nasa.gov/…/apollo50th/pdf/A11_MissionReport.pdf).
- *Saturn V Launch Vehicle Flight Evaluation Report AS-506 Apollo 11
  Mission*, MPR-SAT-FE-69-9 (MSFC 1969), kap. 1 a tab. 5-2
  (ibiblio.org/apollo/Documents/lvfea-AS506-Apollo11.pdf).

| scéna | tvrzení | co říká zdroj | stav |
|---|---|---|---|
| S01 | v0.2: „On the morning of the first Moon landing" | Start 16. 7. 1969, přistání na Měsíci až 20. 7. Ráno startu (9:32 EDT) není ráno přistání. | **přepsáno**: „In July 1969, the rocket that carried the crew of the first Moon landing" |
| S01 | ~2 900 t na rampě | „Vehicle mass at S-IC ignition is 2,941,221 kilograms" (LVFE, kap. 1). | potvrzeno |
| S02 | „eight days later", tři lidé | Start 16. 7. 13:32 UTC, přistání na moři 24. 7. 16:50 UTC, tedy 8 dní 3 h. | potvrzeno |
| S02 | v0.2: „less than six tonnes" | Tab. A-I: CM při entry 12 095 lb, **landing 10 873 lb = 4 932 kg**. Smithsonianských 5 900 kg je CM při oddělení od SM (12 107 lb = 5 492 kg) nebo zaokrouhlení. | **přepsáno**: „just under five tonnes" |
| S03 | v0.2: „about one part in five hundred" | 2 941 / 4,932 = **596**. | **přepsáno**: „about one part in six hundred" |
| S04 | v0.2: „around two thousand tonnes… first two and a half minutes" | Tab. 5-2 (reconstructed): při uvolnění držáků LOX 1 468,6 t + RP-1 637,8 t, při OECO zbývá 18,0 + 14,0 t → **2 074 t spáleno** od startu do OECO. OECO v 161,66 s (2:42). Při zážehu bylo v S-IC 2 146 t, tedy 73 % startovní hmotnosti. | **přepsáno**: „more than two thousand tonnes… in under three minutes" |
| S04 | *propellant* = palivo + kyslík | S-IC: RP-1 a LOX, viz tab. 5-2. | potvrzeno |
| S05 | velká část nebyla pro loď, ale pro další propelent | Loď (CSM + LM + SLA/LES) při startu 109 667 lb = **49,7 t**, tedy 1,7 % startovní hmotnosti. Nad S-IC je ~650 t, z toho většina propelent S-II a S-IVB. | potvrzeno (kvalitativně) |
| S30 | pět motorů, dopad do Atlantiku | S-IC má pět F-1. LVFE kap. 4: „actual impact locations for the spent S-IC and S-II stages" (Atlantik, ~340 nmi od rampy). | potvrzeno; „two and a half minutes" → „**less than three minutes**" (161 s) |
| S31 | S-II skoro na orbit, S-IVB dokončí a později TLI | S-II ~389 s; S-IVB první zážeh ~144 s → parkovací dráha 183,8 × 186,5 km; druhý zážeh = TLI. | potvrzeno |
| S35 | sestupový stupeň na Měsíci, výstupový odhozen na lunární orbitě | Tab. A-I: „Lunar lift-off" (výstupový stupeň 10 777 lb), „Docking", „After ascent stage jettison". | potvrzeno |
| S35 | (návrh uživatele) Eagle nakonec dopadl na Měsíc | **Nedoloženo.** Osud neznámý. Meador (arXiv 2105.10088, 2021) modeluje stabilní dráhu, Eagle tedy může obíhat dodnes. Záměrně na Měsíc navedené byly výstupové stupně Apolla 12 a 14–17. | nepřevzato, ve scénáři jen „cast off in lunar orbit" |
| S36 | SM odhozen těsně před vstupem | Tab. A-I: „Command & service module separation" těsně před „Entry". | potvrzeno |

Křížová kontrola k S27: na parkovací dráhu se dostalo 135 669 kg
(LVFE kap. 1), tedy **4,6 %** startovní hmotnosti, ve shodě s „~4 %"
u Falconu 9.

## 2. Historie rovnice (S10–S12)

| scéna | tvrzení | zdroj | stav |
|---|---|---|---|
| S10 | „more than a century old" | 1903, příp. 1813. | potvrzeno |
| S11 | 1903, učitel z Kalugy | Článek v *Naučnoje obozrenije*, č. 5, květen 1903 (historyofinformation.com). V Kaluze od 1892, učitel matematiky do 1920 (tsiolkovsky.org). Rukopis podán 1898 (centennialofflight.net). | potvrzeno |
| S12 | Moore 1813, vojenské rakety | William Moore, Royal Military Academy Woolwich, *A Treatise on the Motion of Rockets* (Londýn 1813), předtím články 1810–1812. Wikipedia (Tsiolkovsky rocket equation): Moore „outlined it as early as 1810" a rozvedl v knize 1813. Formulováno opatrně („how a rocket speeds up as it loses mass"), protože nejde o rovnici v dnešním zápisu. | potvrzeno |
| S12 | „Tsiolkovsky turned it into the equation of spaceflight" | Ciolkovskij jako první spojil rovnici s letem do vesmíru (článek 1903 je o letu do kosmu). Interpretace, ne citace. | potvrzeno |

Goddard (1912) a Oberth (~1920) ji odvodili nezávisle taky; ve scénáři
nejsou, a nemusí.

## 3. Rovnice a logaritmus (S13–S20) — spočteno

Δv = vₑ · ln(m₀/m_f).

- S18: ln 4 = 1,386, ln 8 = 2,079 → **+50,0 %**.
- S19: ln 16 = 2,773 → +33,3 % proti ln 8. „About a third more" ✓.
- S20: m₀/m_f = e^(Δv/vₑ), každý přírůstek Δv násobí poměr stejným
  činitelem. „Multiplies it" ✓.
- S14: Δv na kilogram vyhozeného propelentu roste s vₑ (hybnost = m·vₑ).
  Formulace „the more speed it gets out of every kilogram it throws" ✓.

## 4. Cesta na oběžnou dráhu (S21–S28)

| scéna | tvrzení | ověření | stav |
|---|---|---|---|
| S21 | 7,8 km/s na LEO | √(GM/r) při 200 km = **7,79 km/s**. | spočteno |
| S22 | celkem ~9,4 km/s | Gravitační ztráty 1,0–1,5 km/s, odpor vzduchu 0,1–0,15 km/s (arXiv 2009.01664); Wikipedia *Delta-v budget* uvádí 9,3–10 km/s. | potvrzeno |
| S23 | H2/O2 ve vakuu ~4,5 km/s | RS-25 452 s → 4,43 km/s; RL10B-2 465 s → 4,56 km/s; RL10C 453,8 s. „Best chemical engine… as it would in a vacuum" ✓. | potvrzeno |
| S24–S25 | poměr ~8, 100 t → 12 t | e^(9,4/4,5) = **8,08**; 100/8,08 = **12,4 t**. | spočteno |
| S27 | Falcon 9 ~550 t, max. ~23 t na LEO | 549 t, 22,8 t při odhozeném prvním stupni (17,5 t s přistáním na lodi), Wikipedia/SpaceX. 22,8/549 = **4,2 %** → „up to about four percent". | potvrzeno |
| S28 | rakety na orbit odhazují stupně nebo jiný hardware | Žádná jednostupňová raketa na oběžnou dráhu neletěla (Atlas odhazoval motory, Shuttle nádrž a SRB). Změkčeno už ve v0.2. | potvrzeno |

## 5. Motory (S37–S42)

| scéna | tvrzení | zdroj | stav |
|---|---|---|---|
| S38 | chemické rakety brzdí energie paliva | vₑ je omezená chemickou energií na kg; H2/O2 prakticky ~4,5 km/s. | potvrzeno |
| S39 | iontový motor „several times faster" | NSTAR Isp až 3 100 s → **30,4 km/s**, ~7× víc než H2/O2. | potvrzeno |
| S39 | Dawn změnil rychlost o >11 km/s | Rayman, AIAA Pickering Lecture 2019: „total effective velocity change of 11.5 km/s (25,700 mph)", srovnatelné s celým Delta II. | potvrzeno |
| S40 | tah jako váha listu papíru na dlani | NASA/JPL: ~91 mN, „holding a single piece of notebook paper in your hand". | potvrzeno |
| S41 | v0.2: „four days to reach motorway speed" | NASA/JPL: „four days to accelerate from 0 to 60 mph" při plném tahu. (Planetary Society 2013: při tehdejším sníženém výkonu přes pět dní.) | **přepsáno**: „four days to reach sixty miles an hour" |
| S42 | žádný létaný motor neumí obojí | Jaderný termální (NERVA) jen pozemní testy. Interpretace. | potvrzeno |

## 6. Super-Země (S43–S49)

**Zdroj:** Hippke, M. (2018). Spaceflight from Super-Earths is difficult.
*Int. J. Astrobiology*, arXiv 1804.04727. Čten celý text (pdftotext).

| scéna | tvrzení | zdroj | stav |
|---|---|---|---|
| S44 | těžší planeta → vyšší úniková rychlost | v_esc = √(2GM/R). | potvrzeno |
| S45 | 2018, německý výzkumník, 10 M⊕, 1,7× širší | „10 M⊕, 1.7 R⊕ Super-Earth similar to Kepler-20 b". Afiliace Sonneberg Observatory (Německo). v0.2 „astrophysicist" nedoloženo → „German researcher". | přepsáno |
| S46 | 11 vs 27 km/s | „~11.2 km s⁻¹ for Earth, and v_esc ~27.1 km s⁻¹". Přepočet 11,186 · √(10/1,7) = 27,13. | potvrzeno + spočteno |
| S47 | jednostupňová raketa: ~26 → ~2 700 | „single-stage rocket with Isp = 350 s… mass ratio of ~26 on Earth, and ~2,700 on Kepler-20 b". Přepočet e^(11,2/3,43) = 26,1; e^(27,1/3,43) = 2 685. | potvrzeno + spočteno |
| S48 | Apollo ~400 000 t, >100 Saturnů V | „For a classical Apollo moon mission (45 t), the rocket would need to be considerably larger, ~400,000 t." 400 000 / 2 941 = **136**. Hippke sám bere Saturn V 3 050 t → 131. | potvrzeno |
| S48 | (nepoužito) „mass of the Pyramid of Cheops" | Velká pyramida ~6 mil. t, tedy 15× víc. | **nepřebráno** |
| S49 | chemické rakety by ji ještě opustily, na těžších by palivo bylo neúnosné | Abstrakt: „chemical rockets still work for planets up to ~10× Earth mass. More massive rocky worlds… would require a more efficient (nuclear) propulsion." Text: 400 000 t „probably a realistic limit for chemical rockets regarding cost constraints". | potvrzeno |

Hippkeho model je **úniková rychlost, ne oběžná dráha**, a jednostupňová
raketa bez konstrukce („never achievable lower limit"). Scénář mluví
o „escape" a o „simplified single-stage rocket", takže sedí.

## 7. Závěr (S50–S52)

S50–S51 jsou interpretace bez nového čísla. „Throws away almost all of
itself" — domů přišlo 0,17 % (S03). ✓

## Dodatek v0.4 (zpětná vazba 0.3)

Formulace zpřesněny bez nového tvrzení: S05 (fuel jako zjednodušení),
S12 (Ciolkovskij vztah *použil* k úvahám o letu do vesmíru), S14
(vₑ určuje hybnost odnesenou každým kilogramem; Δv rakety závisí i na
okamžité hmotnosti, dv = vₑ·dm/m), S38 (omezení energií chemických
reakcí), S49 (týká se chemických raket, ne úniku jinými prostředky).

## Dodatek v0.5 (2026-10-25, zpětná vazba k draftu 1)

| scéna | tvrzení | ověření | závěr |
|---|---|---|---|
| S13 / S13b | rozdělení „Here it is.“ | beze změny textu | — |
| S49b | Mars ~ desetina hmotnosti Země | 6,417·10²³ / 5,972·10²⁴ kg = **0,107** (NASA Mars Fact Sheet) | potvrzeno |
| S49b | úniková rychlost Marsu ~5 km/s | NASA Mars Fact Sheet: **5,03 km/s** | potvrzeno |
| S49c | ve stejném zjednodušení poměr ~26 → ~4 | Isp 350 s → vₑ = 3,432 km/s; e^(11,186/3,432) = **26,0** (sedí s Hippkem), e^(5,027/3,432) = **4,33**. Náš přepočet, ne Hippkeho číslo — proto „in the same simplified calculation“. | spočteno |
