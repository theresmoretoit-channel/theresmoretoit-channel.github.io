# Factcheck — 067 Could You Build Your Own Satellite?

Ověřováno na `script 0.3.md` (2026-09-26). Empirická tvrzení dohledal
rešeršní průchod s primárními/autoritativními zdroji, fyziku a spočitatelné
věci ověřeno rozborem. **Dvě tvrzení vyšla jen ČÁSTEČNĚ a jedno se zjemnilo
— vedlo to k opravě scénáře (→ `script 0.4.md`).** Slouží i jako podklad
pro odpovědi divákům.

## Tvrzení, která vedla k opravě scénáře

### S06 — „1U, ten centimetres on every side" → ČÁSTEČNĚ, OPRAVENO
- **Ověření:** Cal Poly CubeSat Design Specification: 1U = 100 × 100 ×
  **113,5** mm. Průřez 10×10 cm, ale výška 11,35 cm — **není to krychle.**
  Hmotnost ≤ 1,33 kg (CDS ≤ rev 13), ≤ 2 kg (rev 14+, 2020).
- **Zdroj:** CDS Rev 14.1 (2022), en.wikipedia.org/wiki/CubeSat
- **Závěr:** „ten centimetres on every side" je věcně špatně na výšce.
  **Opraveno na „roughly a ten-centimetre cube"** — poctivé zjednodušení.
  (Závěrečné „a ten-centimetre box" v S51 zůstává, „box" je přibližný.)

### S42 — „Eight minutes later, you're in space" → ČÁSTEČNĚ, OPRAVENO
- **Ověření:** Falcon 9 na LEO — MECO ~2:45, orbitální inzerce (SECO-1)
  ~8:30–9:14. Překročení Kármánovy hranice (~100 km, „in space") nastává
  už kolem 2–3 min. **~8–9 min je čas do ORBITU, ne „do vesmíru".**
  Číslo je navíc závislé na nosiči (údaj platí pro Falcon 9 / rideshare).
- **Zdroj:** spaceflightnow.com (F9 timeline), en.wikipedia.org/wiki/Falcon_9
- **Závěr:** **Opraveno na „About nine minutes later, you're in orbit."**
  — zachovává konkrétní beat, ale rozlišuje vesmír od orbity.

### S47 — „dispose of itself" → ZJEMNĚNO
- **Ověření:** End-of-life je požadavek na **opuštění chráněné oblasti**
  v daném limitu, ne nutně aktivní sebelikvidace. Pod ~500–550 km stačí
  pasivní pokles atmosférou; nad tím je potřeba aktivní/asistovaný deorbit.
  „Dispose of itself" implikuje aktivní likvidaci u každé družice — moc
  kategorické.
- **Závěr:** **Opraveno na „clear out of orbit"** — pokrývá pasivní i
  aktivní cestu.

## Empirická tvrzení — DOLOŽENA

### S13–S15 — ceny (nejcitlivější, drženo ODDĚLENĚ hardware / launch / mission)
- **Hardware 1U (S13):** flight-grade hardware 1U reálně **desítky tisíc
  dolarů** (jen jeden GaAs panel ~€12,8 tis.; 1U jich chce 5–6 + EPS + OBC
  + rádio + ADCS). Levný studentský kit může být pár tisíc — proto ve
  scénáři „**flight hardware**" a „can easily cost".
- **Launch (S15):** rideshare (SpaceX ~$6–7 tis./kg 2026, přes brokery
  vč. deploreru): **1U ≈ nižší desítky tisíc**, 3U ≈ ~$80–240 tis.,
  6U ≈ ~$160–480 tis. „tens of thousands… hundreds of thousands" sedí.
- **Pozn.:** celkový **mission cost** (hardware + launch + licence +
  ground + práce) jde do stovek tisíc až nižších milionů; scénář ho
  netvrdí a nemíchá — S13 hardware, S14 „things not on the parts list",
  S15 launch. **Ceny jsou indikativní a tržně proměnlivé.**
- **Zdroj:** nanoavionics.com (panel), cubesatshop.com, satbase.com
  (F9 2026), blackwingspace.com, medium (rideshare economics).
- **Závěr:** SUPPORTED, formulace ve scénáři už tři složky rozlišuje.

### S18 — marketplace komponent → SUPPORTED
- **Ověření:** CubeSatShop.com (od 2009, ISIS) = katalog/webshop 100+
  standardizovaných produktů od 25+ dodavatelů; existuje i CubeSat.Market.
  **Nuance:** spíš katalog/„request a quote", ne klik-a-kup e-shop.
- **Zdroj:** cubesatshop.com/about, cubesat.market
- **Závěr:** „marketplaces built specifically for CubeSat parts" je přesné.
  Scénář netvrdí klik-a-kup, netřeba měnit.

### S19 — EnduroSat OBC = ARM Cortex-M7 + SPI/I²C/UART/CAN → SUPPORTED
- **Ověření:** EnduroSat Onboard Computer: **ARM Cortex-M7** (do 216 MHz),
  2 MB flash + 2×2 MB FRAM + 2×16 GB SD-NAND, rozhraní **CAN/CAN-FD, SPI,
  I²C, UART**, navíc RS-422/485 a Ethernet; běží FreeRTOS.
- **Zdroj:** endurosat.com/products/onboard-computer, SatCatalog datasheet
- **Závěr:** Cortex-M7 i výčet rozhraní sedí. Scénář neuvádí konkrétní
  číslo paměti (dobře — vyhnul se pasti „2 MB vs 32 GB"), netřeba měnit.

### S20 — Cortex-A + Linux u náročnějších → SUPPORTED
- **Ověření:** konkrétně **Xiphos Q8** (Zynq UltraScale+, quad Cortex-A53,
  Linux, flight-proven); též Xiphos Q7 (Cortex-A9), Unibap iX10.
- **Zdroj:** xiphos.com, satsearch.co (payload processors), unibap.com
- **Závěr:** SUPPORTED.

### S22 — NASA F Prime → SUPPORTED (silný primární zdroj)
- **Ověření:** F´ (F Prime) = komponentový C++ letový framework z JPL,
  open-source (github.com/nasa/fprime), určený i pro CubeSaty/SmallSaty.
  Heritage: ASTERIA, Lunar Flashlight, NEA Scout (CubeSaty), Ingenuity.
- **Zdroj:** github.com/nasa/fprime, fprime.jpl.nasa.gov, jpl.nasa.gov
- **Závěr:** SUPPORTED. (RTEMS/Zephyr/FreeRTOS z téže scény jsou reálné
  RTOSy používané v kosmu — RTEMS notoricky NASA/ESA.)

### S28–S29 — magnetorquer → SUPPORTED
- **Ověření:** cívka vytvoří dipól m, v poli Země moment τ = m × B; slouží
  k řízení orientace a odčerpávání momentu setrvačníků. Není pohon.
  Dipól v **homogenním** poli necítí sílu, jen moment; gradient pole Země
  dá zanedbatelnou sílu → „doesn't move the satellite" je na úrovni
  populárního výkladu přesné (orbitu to nemění).
- **Zdroj:** en.wikipedia.org/wiki/Magnetorquer, satsearch.co, tensortech.co
- **Závěr:** SUPPORTED, „It just turns it" ponecháno.

### S44b–S45 — debris, deorbit, „burns up" → SUPPORTED (rámováno opatrně)
- **Ověření:** (a) pravidla: **IADC/UN 25 let** (nezávazná směrnice) +
  **FCC „5-year rule"** (FCC 22-74, 2022, závazné pro US licence v/přes
  LEO <2000 km). (b) demise: malé CubeSaty **většinou shoří**, ale ne
  zaručeně vše — setrvačníky, magnetorquery, optika, baterie, nádrže mohou
  přežít („Design for Demise"). (c) závislost na výšce: pod ~500–550 km
  pasivní pokles v limitu; nad ~600 km přirozený rozpad **staletí** — přesně
  případ „left in orbit for centuries → debris".
- **Zdroj:** fcc.gov (5-year rule), FCC-22-74A1, NTRS (Ostrom, CubeSats),
  esa.int (feel the burn)
- **Závěr:** SUPPORTED. Scénář to rámuje správně: S44b = „nech to být /
  vysoká orbita → debris", S45 slovem **„Ideally"** hedguje pasivní pokles.
  „Burns up" je pro malý CubeSat v nízké orbitě férové zjednodušení —
  neměněno (hedging každé věty by scénář jen zředil).

## Rutinní tvrzení — ověřeno rozborem, bez nálezu

Fyzika a obecně známé: eklipsa/nabíjení baterií (S09, S37), vakuum bez
konvekce a teplotní design (S36), senzory orientace gyro/magnetometr/sun
sensor (S28), GPS dává polohu ne orientaci (S27), radiace překlápí bity
(S26/S32), embedded C/C++ + RTOS (S21–S22), watchdogy/safe mode (S25),
vibrační/prostředí­ové testy před startem (S33–S35), spektrum se licencuje
(S38), sekundární payload + standardní deployer (S40–S41), typické mise
CubeSatů: radiace, snímky Země, atmosféra, tech demo (S30). CubeSaty
existují od ~1999, první starty 2003 (S04). Vše v pořádku, bez zásahu.

## Doplňky po poslechu (verze 0.5)

Ověřeno 2026-09-27 (web) pro nové scény S18b, S19b, S20b, S25b, S43b:

- **S20b — takt.** Tvrzení „CubeSat počítač běží na pár set MHz, notebook na
  4–5 GHz". Doloženo: EnduroSat OBC = ARM Cortex-M7 **do 216 MHz** (satsearch,
  endurosat.com). Cortex-M7 (STM32H7) max ~480–550 MHz, CubeSat OBC běžně
  níž kvůli příkonu. Desktop/notebook ~3–5 GHz + víc jader. Poměr ~21× je ve
  scéně odvozen z čísel (assert). Voiceover má „a couple of hundred megahertz"
  a „four or five gigahertz" — záměrně zaokrouhleno, ne přesné číslo.
- **S18b — standard + prodej + cena.** „Standardizované, stohovatelné,
  prodejné." Doloženo: **PC/104** = stohovatelný modulární standard desek od
  různých výrobců (Wikipedia PC/104). Prodejci: EnduroSat, GomSpace, ISISPACE;
  agregátor CubeSatShop.com. **Ceny záměrně jen orientačně** („tisíce až
  desítky tisíc $ za subsystém") — konkrétní ceny se veřejně neuvádějí
  (na dotaz), proto rozpětí, ne číslo.
- **S25b — radiace/stínění.** „Není těžké stínění, počítač se hlídá, opravuje
  a resetuje." Doloženo: CubeSaty používají COTS díly + **watchdog timery**
  (reset při chybě) + **latch-up ochranu** (odpojení při nadproudu) + **ECC/
  scrubbing** paměti; těžké stínění se nepoužívá (hmotnost), spoléhá se na
  fault-tolerant design + krátké mise na LEO (ScienceDirect „Radiation tests
  of a CubeSat OBC", Military Embedded Systems). Kosmické záření: SEU (překlopení
  bitu) a latch-up jsou reálné mechanismy.
- **S43b — detekce vypuštění + inhibice.** „Deployment switches sepnou při
  vysunutí, pak ~30 min ticho." Doloženo **CubeSat Design Specification (CDS)**:
  min. jeden deployment switch na rohové kolejnici, stlačený v deployeru;
  **žádný provoz (RF, rozložení, hlavní napájení) min. 30 minut po vypuštění**;
  deployables (antény, panely) čekají ≥30 min. Tři nezávislé HW inhibitory.
  Proto se „ground station hears it" přesunulo z S43 do S43b (za těch 30 min).
- **S19b — reálná deska.** Fotka je archiv (Wikimedia), evidence přes
  `sources.json` + otisk jako u ostatních archivních scén; tvrzení „reálná
  off-the-shelf deska" je popisné, ne konkrétní produkt.
