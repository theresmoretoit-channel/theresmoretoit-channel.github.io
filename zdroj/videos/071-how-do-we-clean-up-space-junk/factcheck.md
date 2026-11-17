# Fact check — 071 — How Do We Clean Up Space Junk?

Ověřeno 2026-09-28. Výchozí text: `zdroj.txt` (z `/data/temp/Space Junk: How Do We Clean Up Earth's Orbit?.txt`),
výsledek: `script 0.1.md` a shodný `script.md`.

**Výsledek:** Všechna základní fyzikální tvrzení, řádové hodnoty rychlostí, orbitální mechanika,
koncept Kesslerova syndromu i technologie laserové ablace a odchytu jsou věcně správné.
Do scénáře byly doplněny standardní britské tvary (`kilometres`, `tonnes`, `travelling`, `vaporises`),
slovní vypsání veličin pro syntézu hlasu a standardní 3řádková výzva k odběru (S18b).

Níže je detailní rozbor jednotlivých scén, faktické zdroje a pokyny pro budoucí storyboard a diagramy.

---

## S01–S05 — Úvod a podstata problému

- **„Thousands of tonnes of junk flying around Earth“**: Podle zprávy ESA Space Debris Report (2024)
  je celková hmotnost lidmi vyrobených objektů na oběžné dráze Země odhadována na více než 11 500 až 13 000 tun.
  Formulace „thousands of tonnes“ je plně podložená.
- **Složení smetí**: Nefunkční družice (dead satellites), vyhořelé stupně nosných raket (spent rocket stages),
  úlomky po explozích zbytkového paliva/baterií a po historických kolizích (např. Iridium-33 / Kosmos-2251 v roce 2009).
- **Nebezpečí malých úlomků**: Většina sledovatelných objektů je katalogizována od velikosti ~10 cm (radar a optika ze Země).
  Objekty mezi 1 cm a 10 cm (odhadem přes 1 000 000 kusů) a pod 1 cm (přes 130 milionů kusů) jsou téměř
  nesledovatelné, ale při orbitálních rychlostech mají kinetickou energii ekvivalentní projektilu nebo granátu.
- **Absurdní otázka**: Přirovnání „no floor, no broom, no garbage truck“ funguje jako rétorická kotva. **Věcně OK.**

## S06–S09 — Fyzika oběžné dráhy a rychlosti

- **Rychlost 7 až 8 km/s (přes 25 000 km/h)**:
  Kruhová rychlost na nízké oběžné dráze (LEO, 200–1000 km):
  $$v = \sqrt{\frac{GM}{r}}$$
  Pro výšku 200 km: $v \approx 7,78\text{ km/s}$ ($28\,000\text{ km/h}$).
  Pro výšku 800 km: $v \approx 7,45\text{ km/s}$ ($26\,800\text{ km/h}$).
  Údaj „roughly seven to eight kilometres per second... more than twenty-five thousand kilometres per hour“ sedí přesně.
- **Relativní rychlost srážky**: Družice nelétají jen týmž směrem (např. polární vs. ekvatoriální dráhy, retrográdní sklony).
  Vzájemná relativní rychlost může dosáhnout 10 až 15 km/s.
- **Doba setrvání na dráze**:
  Ve výškách pod 400 km (kde létá ISS) zbytková atmosféra způsobuje zánik v řádu měsíců až jednotek let.
  V 600–800 km jsou to dekády až století. Nad 1 000 km tisíce let. Text správně uvádí závislost na výšce a odporu atmosféry. **Věcně OK.**

## S10–S14 — Aktivní odklízení velkých kusů (ADR) a mise ClearSpace-1

- **Nekooperativní cíle**: Staré družice a stupně raket nemají dokovací uzly, vizuální navigační terče,
  ani aktivní stabilizaci. Většina z nich nekontrolovaně rotuje (tumbling) vlivem gradientu gravitace a tlaku záření.
- **ClearSpace-1**: První plánovaná mise ESA pro aktivní odstranění trosek (Active Debris Removal).
  Původním cílem byl adaptér Vespa (112 kg) z rakety Vega (vypuštěné 2013).
  I když byl adaptér v roce 2023 pravděpodobně zasažen malým úlomkem a mise čelí úpravám profilu,
  ClearSpace-1 je v literatuře standardní příklad robotického zachycení 4 chapadly. **Věcně OK.**

## S15–S18 — Proč nestačí trosky rozstřílet (Kesslerův syndrom)

- **Kesslerův syndrom**: Popsán Donaldem J. Kesslerem a Burtonem Cour-Palaisem v roce 1978
  (*„Collision Frequency of Artificial Satellites: The Creation of a Debris Belt“*).
  Jde o domino efekt, kdy hustota objektů v LEO překročí kritickou mez a kolize začnou generovat
  více nových úlomků, než kolik jich atmosféra stíhá brzdit a čistit.
- **Důkazy z praxe**:
  - Test čínské protidružicové zbraně (ASAT) na Fengyun-1C (2007) vytvořil přes 3 500 katalogizovaných trosek.
  - Kolize Iridium 33 a Kosmos-2251 (2009) vytvořila přes 2 000 velkých trosek.
- Text výslovně a správně vysvětluje, že pouhá destrukce problém zhoršuje. **Věcně OK.**

## S18b — CTA (Výzva k odběru)

- Standardní 3řádkový formát z `docs/cta.md`.
- Umístěno po dramatickém vrcholu (Kesslerův syndrom) a před obratem k fyzikálním řešením.

## S19–S21 — Orbitální mechanika brzdění

- **Snížení perigea**: Pro deorbitaci není nutné snížit celou dráhu ani těleso zastavit (což by vyžadovalo $\Delta v \approx 7,5\text{ km/s}$).
  Stačí zpomalit v apogeu o desítky až stovky metrů za sekundu, čímž perigeum klesne do hustších vrstev atmosféry (pod ~120 km).
  Zbytek práce vykoná atmosférický odpor (aerodynamický brzdný účinek a aerotermodynamický zánik).
- Text toto vysvětluje velmi názorně a věcně přesně („We just have to change its orbit... give it a tiny push“). **Věcně OK.**

## S22–S27 — Robotické rameno a síť

- **Robotická ramena**: Používají se pro plánované mise (ClearSpace, Astroscale ADRAS-J). Nevýhoda: vysoká cena na jednotlivý kus,
  složitá navigace a rendezvous.
- **Síť (Net capture)**: Testováno na orbitě v rámci experimentu *RemoveDEBRIS* (Surrey Space Centre, 2018),
  kde byla úspěšně vystřelena síť na testovací cubesat.
  Výhoda: nevyžaduje specifický úchopový bod.
  Riziko: možnost zamotání, dynamické síly lana. **Věcně OK.**

## S28–S35 — Odstranění trosek laserem (Radiační tlak a laserová ablace)

- **Radiační tlak (Radiation pressure)**: Foton nese hybnost $p = E/c$. Odrazem fotonu od povrchu tělesa vzniká tlak.
  Jde o nepatrnou sílu (řádově mikronewtony na kilowatt výkonu), ale působící bezkontaktně.
- **Laserová ablace (Laser ablation / Laser propulsion)**:
  Koncepce LODR (Laser Orbital Debris Removal), kterou poprvé detailně popsal Claude Phipps (1996, *Project Orion*).
  Pulzní laser vysoké intenzity zasáhne povrch úlomku; tenká vrstva kovu/plastu se bleskově odpaří na horké plazma.
  Expandující plazma tryská směrem od povrchu a podle zákona zachování hybnosti udělí úlomku reaktivní impuls v opačném směru:
  $$I = C_m \cdot E_{laser}$$
  kde $C_m$ je koeficient vazby hybnosti (obvykle $10\text{ až }100\text{ }\mu\text{N}\cdot\text{s/J}$).
  Objekt funguje jako vlastní mikroraketový motor.
- **Požadovaný impuls**: K vychýlení dráhy o několik metrů za sekundu postačí série pulzů během několika průletů nad stanicí.
  To stačí k vyhnutí se kolizi (collision avoidance) i k postupnému snížení perigea. **Věcně OK.**

## S36–S39 — Problémy laserového řešení

- **Přesnost sledování**: Pro fokusaci laseru na 1–10 cm cíl ve vzdálenosti 800 km je potřeba sub-oblouková vteřinová přesnost (astrometrie a laser ranging).
- **Atmosférické zkreslení**: Pozemní laser musí překonat atmosférickou turbulenci (vyžaduje adaptivní optiku).
- **Riziko špatného směru impulsu**: Pokud úlomek rotuje a impuls je aplikován ve směru letu místo proti němu, dojde ke zvýšení dráhy
  nebo nechtěné změně sklonu. **Věcně OK.**

## S40–S45 — Velké objekty, prevence a pravidla

- **Těžké družice**: Pro několikatunovou družici je energie potřebná k ablaci příliš vysoká; laser je určen primárně pro malé úlomky (1–10 cm).
- **Prevence a konstrukce**: Pravidlo 25 let pro opuštění LEO (FCC v USA v roce 2022 zpřísnila na 5 let; ESA Zero Debris Charter cílí na nulový odpad do roku 2030).
  Pasivace nádrží a baterií (aby nedocházelo k explozím po skončení mise).
- Přirovnání k vysavači a házení odpadků na zem: Přesná metafora. **Věcně OK.**

## S46–S50 — Závěr a cliffhanger pro Part 2

- Rekapitulace: Žádný zázračný vysavač, ale kombinace technologií.
- Zmínka o dalších metodách pro Part 2: Harpuny (testováno rovněž na RemoveDEBRIS), plachty (drag sails, např. NanoSail-D2),
  elektrodynamické tethers, magnetické dokování. **Věcně OK.**

---

## Revize 2026-09-28 (druhý průchod, přepočtem a proti zdrojům)

Původní fact check výš vznikl slabším modelem a část tvrzení jen převyprávěl. Přepočteno
(`mu = 398 600,4 km³/s²`, `R = 6 371 km`) a dohledáno:

| scéna | tvrzení | ověření | závěr |
|---|---|---|---|
| S01 | *thousands of tonnes* | ESA Space Environment Report 2025: ~13 600 t | ✅ |
| S07 | 7–8 km/s, *more than 25,000 km/h* | 400 km: 7,67 km/s = 27 600 km/h; 1 000 km: 7,35 km/s | ✅ |
| S50 | *28,000 km/h* | 7,79 km/s ve 200 km = 28 040 km/h; ve 400 km 27 600 | ✅ (horní hrana LEO rychlostí) |
| S14 | ClearSpace-1 chytí nefunkční objekt a sestoupí s ním | cíl od dubna 2024 **PROBA-1** (95 kg, 2001), ne adaptér Vespa — ten zasáhl úlomek 2023; stack shoří v atmosféře | ✅ text sedí, **výš uvedený cíl Vespa je zastaralý** |
| S29 | fotony nesou hybnost | F = P/c: 3,3 µN na kW pohlceného, 6,7 µN odraženého | ✅ |
| S19–S21 | stačí snížit perigeum | Δv v apogeu na perigeum 200 km: **58 m/s** ze 400 km, **113** z 600, **165** z 800, **214** z 1 000 km | ✅ |
| **S48** | ***„Maybe by a few metres per second. Or even much less."*** | 1 m/s sníží protější bod dráhy jen o ~3,8 km. Na návrat do atmosféry je potřeba **desítky až ~200 m/s**; Phipps (LODR) počítá 100–150 m/s. Pár m/s stačí na **vyhnutí se srážce**, ne na odklizení | ❌ **nepravdivé** |
| S33 | *„only need to change it by a tiny amount"* | 100–150 m/s je 1–2 % z 7 500 m/s | ✅ relativně |

**Oprava S48 čeká na rozhodnutí uživatele** (mění text, tedy TTS). Návrh:
*„Maybe by a hundred metres per second. / Barely more than one percent of its speed."*
Diagram S48 (`zaver.py`) má zatím popisek podle chybné věty a po opravě se musí změnit.

**Obraz S08** (`File:Space debris impact on Space Shuttle window.jpg`, NASA, public domain): důlek
v okně raketoplánu po misi STS-7 (1983), podle NASA po zlomku barvy o velikosti řádově 0,2 mm; měřítko
1 mm je přímo ve snímku. Sedí na větu *„a tiny screw… is a projectile"* — ukazuje, co udělá i menší kus.
