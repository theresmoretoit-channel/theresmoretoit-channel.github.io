# 069 — fact check

Podklad: `zpetna vazba 0.1.txt`, tedy kontrola uživatele přes ChatGPT
(zdroje ESA a Novespace) nad `script 0.1.md`, a k tomu vlastní balistický
přepočet (g = 9,81 m/s², bez odporu vzduchu). **Stránky ESA a Novespace
jsem sám neotevíral.** Čísla se z nich přebírají přes tu kontrolu a jsou
označená „ESA/Novespace (přes ChatGPT)".

## Profil paraboly (S14–S18, S44–S47, S55–S60)

| tvrzení | ověření | závěr |
|---|---|---|
| vodorovný let v ~6 km, pull-up při 1,8 g ~20 s | ESA/Novespace (přes ChatGPT) | ✅ |
| volný pád začíná v ~7,6 km | ESA/Novespace uvádí 7,5–7,6 km | ✅ |
| rychlost ~650 km/h při zahájení volného pádu, pořád stoupá | výstup ze 7,6 na 8,5 km vyžaduje svislou rychlost √(2·9,81·900) = 133 m/s; při sklonu 47° to dává 182 m/s = **655 km/h** | ✅ |
| vrchol ~8,5 km | ESA/Novespace (přes ChatGPT) | ✅ |
| mikrogravitace 20–22 s | ESA/Novespace (přes ChatGPT) | ✅ |
| 1,8 g i po parabole, ~20 s | ESA (přes ChatGPT) | ✅. **Ve v0.1 chybně** v S90 (*„a few seconds later, you're back to normal"*), opraveno ve v0.2 |
| „dozens of parabolas" za let | Novespace létá 31 parabol za let | ⚠️ nepřeověřeno, formulace „dozens" to kryje |

## Přechody (S03, S05, S61–S67)

| tvrzení | ověření | závěr |
|---|---|---|
| beztíže přijde „za pár sekund" po nástupu 1,8 g | pull-up trvá ~20 s | ❌ ve v0.1 (S03), opraveno na *„about twenty seconds later"* |
| podlaha „just as suddenly" tlačí zpátky | přechod trvá 3–5 s (ESA, přes ChatGPT) | ❌ ve v0.1 (S05), opraveno na *„gradually"* |
| přechod 0 → 1,8 g je postupný, „after several seconds" | tentýž zdroj | ✅ |

## Proč ne minutu (S48–S54)

| tvrzení | ověření | závěr |
|---|---|---|
| po ~36 s zpátky v 6 km | 13,5 s k vrcholu + √(2·2500/9,81) = 22,6 s dolů | ✅ |
| v tu chvíli přes 900 km/h | svisle 22,6·9,81 = 222 m/s, vodorovně 182·cos 47° = 124 m/s → 254 m/s = **915 km/h** (ChatGPT 908) | ✅ |
| v 60 s pod zemí, nadzvukově | 8 500 − ½·9,81·46,5² = **−2,1 km**; svisle 456 m/s, celkem ~473 m/s ≈ 1 700 km/h | ✅ |
| do země by narazilo dřív | √(2·8500/9,81) = 41,6 s po vrcholu, tedy ~55 s celkem | ✅ („long before" je ve v0.1 i v0.2 řečeno o rychlostních limitech, ne o zemi) |
| vybrání při 1,8 g stojí přes kilometr výšky | pull-out začíná ~7,5 km a končí ~6 km (ESA/Novespace, přes ChatGPT), tedy ~1,5 km | ✅ |

## Ostatní

| tvrzení | ověření | závěr |
|---|---|---|
| 80 kg při 1,8 g „jako 144 kg" | 80·1,8 = 144 | ✅ |
| Měsíc 0,16 g, Mars 0,38 g, fáze delší než při 0 g | Novespace 25 s / 35 s, ESA ~23 / ~30 s (přes ChatGPT), proti 20–22 s | ✅ |
| nevolnost ze smyslového nesouladu, pohyby hlavou horší, léky proti nevolnosti | ESA (přes ChatGPT), Air Zero G doporučuje držet hlavu v klidu | ✅ |
| Airbus A310 Zero G | ESA/Novespace | ✅ |

## Doplněno 2026-09-28 (v0.4, po zpětné vazbě diváka): S13b, S15b, S41b, S80b

| scéna | tvrzení | ověření | závěr |
|---|---|---|---|
| S13b | dnešní A310 dřív vozil německé vládní činitele | bývalý „Konrad Adenauer“, VIP flotila Bundeswehru (reg. 10+21, dnes F-WNOV) — eoPortal, Wikipedia *Konrad Adenauer (aircraft)* | ✅ |
| S13b | nahradil starší A300, který létal skoro 18 let | A300 Zero-G 1997–2014, „more than 13,000 parabolas in nearly 18 years“ — eoPortal, ESA | ✅ |
| S15b | parabolu letí tři piloti naráz; jeden sklon, jeden tah | Air Zero G (*How it works*), eoPortal | ✅ |
| S15b | třetí „drží letadlo stabilně do stran“ | Air Zero G píše **roll**, eoPortal **yaw** — formulace záměrně pokrývá obojí | ✅ |
| S15b | zkušení zkušební piloti z francouzského národního střediska letových zkoušek | DGA Essais en Vol / CEV — Wikipedia *Weightlessness*, ESA; jen sekundární zdroj | ⚠️ |
| S41b | NASA desítky let létala s upraveným KC-135, přezdívka Vomit Comet | KC-135 1973–2004 (program od 1957), přezdívka — Space.com, Wikipedia *Reduced-gravity aircraft* | ✅ |
| S80b | vědci, výcvik astronautů | ESA, CNES, DLR jako zadavatelé; astronaut training — eoPortal | ✅ |
| S80b | mnoho scén beztíže v Apollu 13 natočeno v KC-135 | 13 dní, 612 parabol, necelé 4 h záběrů — Yale Film Notes, SlashFilm | ✅ |
| S80b | veřejnost si může koupit let | Air Zero G od 2013 (Avico), Zero-G Corp. v USA (G-Force One) | ✅ |
