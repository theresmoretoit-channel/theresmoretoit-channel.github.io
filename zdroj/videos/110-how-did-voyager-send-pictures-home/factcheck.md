# Fact check — 110 How Did Voyager Send Pictures Home?

Ověřováno na **v0.2**, S22/S26/S39/S45 dořešeny ve **v0.3**, S02/S34/S42/S46/S53 ve **v0.4** podle Codexu a uživatele (2026-10-14). Čísla, která se dají spočítat, jsou spočítaná a výpočet je uvedený.
Závěr: ✅ sedí · ⚠️ sedí s výhradou / zaokrouhleno · ❌ opraveno proti v0.1.

## Hook

| scéna | tvrzení | ověření | závěr |
|---|---|---|---|
| S01 | srpen 1989 Neptun, „more than four billion km" od Země | průlet 25. 8. 1989; Neptun–Země ~30 AU (DESCANSO) → 4,4–4,5·10⁹ km | ✅ |
| S02 | kamera postavená kolem TV elektronky, „designed in the 1970s" (v0.4) | vidicon odvozený od kamer Marinerů (PDS ISS); projekt Voyager (MJS77) 1972, start 1977 → návrh v 70. letech jistě. v0.3 „early 1970s" bylo jen odhadem → zúženo | ⚠️ upraveno |
| S03 | „Thousands" snímků | NASA: od Neptunu přes 9 000 snímků | ✅ |
| S04 | 12 let před startem Voyageru; první snímky jiné planety zblízka | 1965 vs. 1977; Mariner 4 = první snímky jiné planety zblízka | ✅ |

## Mariner 4

| scéna | tvrzení | ověření | závěr |
|---|---|---|---|
| S05 | červenec 1965, 22 snímků | NSSDC: 15. 7. 1965, „21 pictures plus 21 lines of a 22nd" | ⚠️ 22. snímek jen částečný — Caltech píše 22 |
| S06 | kamera = vidicon, signál po řádcích | Wikipedia Mariner 4 (slow-scan vidicon) | ✅ |
| S07 | rádio slabé na živý TV signál; 200 × 200 bodů | NSSDC: 8⅓ / 33⅓ bit/s; 200 × 200 (Wikipedia) | ✅ |
| S08 | jas 0–63, 6 bitů | 2⁶ = 64 úrovní; Caltech/Teledyne: tiskárna vypisovala čísla 0–63 | ✅ |
| S09 | páska; 8⅓ bit/s; ~8 h na snímek | NSSDC: páska 5,24 Mbit, rychlost 8⅓ bit/s. 200 × 200 × 6 = 240 000 bitů / 8,33 = **28 800 s = 8 h**. Kontrola: 22 snímků ≈ 5,2 Mbit = celkový objem podle NSSDC | ✅ |
| S10–S11 | JPL nechtěli čekat na počítač, vytiskli čísla na pásky, vybarvili ručně pastelem podle klíče | Caltech Magazine „A Planet Painted by Hand": telekomunikační tým JPL, „impatient to see the official processed image", proužky papíru, barevný klíč, pastel; NASA obrázek „First TV Image of Mars (Hand Colored)" | ✅ |
| S13 | Mariner 4 nebyl digitální fotoaparát; kamera analogová, digitální vše za ní | analogový vidicon → 6bitový A/D převodník → páska → rádio | ✅ (formulace podle zadání uživatele: předchůdce principu, ne první digitální foťák) |

## Sasson / Kodak

| scéna | tvrzení | ověření | závěr |
|---|---|---|---|
| S14–S15 | Kodak, prosinec 1975, Steven Sasson, CCD | IEEE Spectrum; první snímek prosinec 1975 | ✅ |
| S16 | CCD = mřížka světlocitlivých prvků, ne skenování paprskem | učebnicové. **Pozor:** i CCD dává analogové náboje, které se digitalizují — proto ve scénáři *není* „born as numbers"; rozdíl je mřížka v čipu vs. skenovaný terčík | ✅ |
| S17 | 100 × 100, černobílé, záznam na kazetu 23 s | Wikipedia + Sasson (IEEE): expozice 50 ms, zápis na pásku 23 s | ✅ |
| S18 | Kodak ho nikdy neprodával | IEEE Spectrum: „never put into production" | ✅ |

## Voyager — kamera

| scéna | tvrzení | ověření | závěr |
|---|---|---|---|
| S20 | start 1977, dvě kamery (širokoúhlá, úzkoúhlá) | NASA, PDS ISS | ✅ |
| S21 | slow-scan vidicon, upravené kamery dřívějších Marinerů | PDS: „a modified version of the slow scan vidicon camera designs that were used in the earlier Mariner flights" | ✅ |
| S22 | terčík selen-síra, drží obraz přes 1,5 min | **primárně:** B. A. Smith (vedoucí zobrazovacího týmu), *Voyager Imaging Science Investigations*, NASA 1979 (NTRS 19790008605): „Each camera employs a selenium-sulfur … vidicon"; PDS: „target is selenium sulphur", obraz drží „for over 100 s" | ✅ |
| S23 | 800 řádků × 800 bodů | PDS | ✅ |
| S24 | odečet 48 s, 0–255, 8 bitů | PDS: „One frame requires 48 s for electronic readout", 8bitový A/D | ✅ |
| S25 | 16× víc bodů, 4× víc odstínů než Mariner 4; >5 mil. bitů | 640 000 / 40 000 = 16; 256 / 64 = 4; 800² × 8 = 5 120 000 | ✅ |
| S26 | ~640 kB **surových obrazových dat** (v0.3 doplněno), linka přidává bity na ochranu před šumem | 5 120 000 / 8 = 640 000 B (desítkové kB), nekomprimovaný obraz bez kódování; přenášený objem je větší o režii kódu (Golay u Jupiteru +100 %, DESCANSO 6.2.2). 50Mpx JPEG má jednotky až desítky MB | ✅ |

## Cesta domů

| scéna | tvrzení | ověření | závěr |
|---|---|---|---|
| S28 | Jupiter 1979: 115 200 bit/s; snímek za méně než minutu | DESCANSO (Ludwig & Taylor 2002), tab. 6-1. 5,12 Mbit / 115,2 kbit/s = **44 s**; nezávisle PDS: odečet snímku 48 s v režimu přenosu v reálném čase | ✅ |
| S29 | páska, když Země není vidět; místo na ~100 snímků | Tomayko: data na DSS při zákrytu; NASA (Saturn 1981) 536 Mbit / 5,12 = 105; PDS: 12 snímků na stopu × 8 stop = 96 | ✅ |
| S30 | dvojnásobná vzdálenost → 4× slabší signál | zákon převrácených čtverců; DESCANSO | ✅ |
| S31 | Neptun ~6× dál než Jupiter; bez úprav ~3 000 bit/s | DESCANSO: Jupiter 5,2 AU, Neptun 30 AU (5,8×), očekáváno **~3 200 bit/s** | ✅ |
| S32 | snímek by trval skoro půl hodiny | 5,12 Mbit / 3 200 = 1 600 s = **26,7 min** | ✅ |
| S33 | antény DSN přestavěny z 64 na 70 m | DESCANSO 6.3.1 | ✅ |
| S34 | „for the Neptune flyby" (v0.4; v0.3 „at Neptune" stavělo antény k Neptunu) společný příjem s jinými radioteleskopy, mj. 27 antén VLA v Novém Mexiku | DESCANSO 6.3.3 (VLA 27 × 25 m + Goldstone; Parkes s Canberrou) | ✅ |
| S35 | Voyager 2 už za Saturnem, software změněn | Saturn srpen 1981; nahrání 1984–85 (Tomayko: léto 1984 load trval 4 h) | ✅ |
| S36 | letový datový počítač ~80 000 instrukcí/s | Tomayko, *Computers in Spaceflight*, kap. 6: FDS „instruction execution rate was 80,000 per second" | ✅ |
| S37 | nový program nahrán do záložního počítače | DESCANSO 6.2.1: IDC software nahrán do záložního FDS; Tomayko: dvouprocesorový režim poprvé pro Uran | ✅ |
| S38 | posílají se rozdíly mezi sousedními body | DESCANSO: „counting only the differences between adjacent pixel gray levels" | ✅ |
| S39 | typický snímek −60 %; nový opravný kód ubral ochranné bity (callback na S26) | DESCANSO: −60 %; Reed-Solomon místo Golaye, režie 100 % → 20 % | ✅ |
| S40 | Neptun 1989: >20 000 bit/s, skoro 7× víc; snímek ~1,5 min | DESCANSO: dosaženo **21 600**, faktor ×6,8. 5,12 Mbit × 0,4 / 21 600 = **95 s** | ✅ (95 s je výpočet pro „typický" snímek) |
| S42 | v0.4: digitální je až převod signálu na čísla | v0.3 „everything after the lens" bylo **věcně špatně** — za objektivem je ještě analogová elektronka a analogové obvody, digitalizuje až 8bitový A/D převodník (PDS ISS); odporovalo S13. Našel Codex ve všech třech jazycích | ❌ opraveno |
| S42 | software přepsán „from billions of kilometres away" | 1984–85 byl Voyager 2 mezi 10 a 19 AU = 1,5–2,8·10⁹ km | ✅ |

## Pale Blue Dot

| scéna | tvrzení | ověření | závěr |
|---|---|---|---|
| S44 | 1990 Voyager 1 za Jupiterem a Saturnem, planetární mise hotová | Jupiter 1979, Saturn 1980 | ✅ |
| S45 | v0.3: „Back in 1981 … had proposed one last picture"; Sagan člen zobrazovacího týmu | NASA (Voyager 1's Pale Blue Dot): „He had the original idea in 1981 …", „Sagan also was a member of the Voyager Imaging Team." v0.2 „for years … had argued" — délku a průběh úsilí NASA nedokládá (jen sekundární zdroje: „six requests, eight years"), proto nahrazeno doloženým rokem | ❌ opraveno |
| S46 | 14. 2. 1990, 60 snímků, „from beyond Neptune" (v0.4) | NASA. Voyager 1 ve 40,5 AU, Neptun ~30 AU → za drahou Neptunu, ale uvnitř heliosféry; v0.3 „from the outside" by tvrdilo, že je mimo Sluneční soustavu | ⚠️ upraveno |
| S47 | šest planet: Venuše, Země, Jupiter, Saturn, Uran, Neptun | NASA (Merkur u Slunce, Mars rozptýlené světlo, Pluto malé) | ✅ |
| S48 | ~6 mld. km; Země ~1/8 pixelu | 40,5 AU × 1,496·10⁸ = 6,06·10⁹ km (NASA: 6 mld. km od Slunce; popisek PIA00452: „more than 4 billion miles from Earth" = 6,4 mld. km → „about six billion" sedí na obojí); PIA00452: „a crescent only 0.12 pixels in size" ≈ 1/8 (0,125) | ⚠️ zaokrouhleno, „about" |
| S49 | světelný pruh = rozptýlené sluneční světlo v kameře | PIA00452: „Earth lies right in the center of one of the scattered light rays"; NASA: rozptyl „bouncing around in the camera" | ✅ |
| S50 | barevná verze ze tří expozic přes barevné filtry | PIA00452: „three color filters — violet, blue and green" | ✅ |
| S51 | kamery vypnuty 34 min po snímcích Země, kvůli energii, už nikdy nezapnuty | NASA: snímky Země 04:48 GMT, kamery vypnuty o 34 min později natrvalo | ✅ |
| S52 | poslední data na Zemi 1. 5. 1990, skoro 11 týdnů | NASA: do 1. 5. 1990, čtyři relace DSN; 14. 2. → 1. 5. = 76 dní = 10,9 týdne | ✅ |
| S53 | „A transmitter of about twenty watts" (v0.4; v0.3 „radio") | DESCANSO: X-band TWTA, **vysílaný RF výkon** do antény 12 W (low) / **18 W** (high). Je to výkon VYSÍLANÝ, ne elektrický příkon (ten je vyšší, zesilovač má účinnost pod 100 %) — v obraze i v hlase proto „transmitter", ne „radio" | ✅ |

## Zdroje

- Ludwig & Taylor, *Voyager Telecommunications*, DESCANSO Design and Performance Summary Series, JPL 2002 — tab. 6-1, kap. 6.2–6.3
- PDS Rings Node: Voyager 1 Narrow Angle Camera Description (inst_cat_na1)
- Tomayko, *Computers in Spaceflight: The NASA Experience*, NASA CR-182505, 1988, kap. 6 (nasa.gov/…/computers/Ch6-2.html)
- NSSDC: Mariner 4 (1964-077A)
- Caltech Magazine, *A Planet Painted by Hand*; NASA, *First TV Image of Mars (Hand Colored)*
- IEEE Spectrum, first digital camera history; Wikipedia: Steven Sasson, Mariner 4, Family Portrait (Voyager)
- B. A. Smith, *Voyager Imaging Science Investigations*, NASA 1979 (NTRS 19790008605)
- NASA Photojournal PIA00452 (Pale Blue Dot, původní popisek)
- NASA Science: Voyager 1's Pale Blue Dot; NASA: 30 years ago Voyager 2 explores Neptune
