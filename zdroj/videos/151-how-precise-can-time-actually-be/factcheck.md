# Fact check — 151 How Precise Can Time Actually Be?

Ověřuje **scénář v0.4** (2026-11-09). Číslování scén podle v0.4.
Výpočty: `python3` ze vzorců článku, konstanty ħ = 1,0546e-34 J s, c = 2,998e8 m/s,
G = 6,674e-11, m0 = 1,6605e-27 kg (atomová hmotnostní jednotka), rok = 3,156e7 s,
věk vesmíru 13,8 mld let = 4,35e17 s.

## Zdroje

| zkratka | zdroj |
|---|---|
| [B25] | Bortolotti, Curceanu, Diósi, Manti, Piscicchia: *Fundamental Limits on Clock Precision from Spacetime Uncertainty in Quantum Collapse Models*, Phys. Rev. Research 7, 043166 (listopad 2025), DOI 10.1103/p6tj-lg8l; arXiv:2504.06109 (8. 4. 2025), **přečten celý** |
| [A24] | Aeppli, Kim, Warfield, Safronova, Ye: *A clock with 8 × 10⁻¹⁹ systematic uncertainty*, PRL 133, 023401 (10. 7. 2024), JILA Boulder |
| [C10] | Chou, Hume, Rosenband, Wineland: *Optical Clocks and Relativity*, Science 329, 1630 (24. 9. 2010), NIST Boulder; Physics Today: *„The Al-Mg clock started out 17 cm below the other clock and then was raised by a total of 33 cm."* |
| [Bo22] | Bothwell et al.: *Resolving the gravitational redshift across a millimetre-scale atomic sample*, Nature 602, 420 (16. 2. 2022), JILA |
| [GRW] | Ghirardi, Rimini, Weber, Phys. Rev. D 34, 470 (1986); λ = 1e-16 s⁻¹, σ = 1e-7 m — podle [B25] a sekundární literatury („first consistent collapse model"), originál nečten |
| [D20] | Donadi, Piscicchia, Curceanu, Diósi, Laubenstein, Bassi: *Underground test of gravity-related wave function collapse*, Nature Physics 17, 74 (online **7. 9. 2020**), Gran Sasso |
| [BIPM] | doporučená frekvence ⁸⁷Sr 429 228 004 229 873 Hz (CIPM, sekundární reprezentace sekundy) — z paměti, řád a první tři číslice jisté |

## Tvrzení

### S01 — Boulder, nejistota za věk vesmíru < 1 s
[A24]: celková systematická nejistota 8,1e-19. 8,1e-19 × 4,35e17 s = **0,35 s** < 1 s. ✅
Formulace mluví o **nejistotě frekvence**, ne o tom, že by se hodiny „rozešly" (zpětná vazba k v0.1). JILA sídlí v Boulderu. ✅

### S02 — každá generace hodin lepší než minulá
Obecně platí (cesium → optické mřížkové hodiny, nejistoty klesají o řády). Rétorické. ✅

### S05 — v klasické fyzice čas dokonale ostrý
Newtonův absolutní čas; ani relativita na spojitosti a ostrosti času nic nemění (mění jeho relativnost). ✅

### S06 — 2025, fyzici v Římě a Budapešti
[B25]: afiliace Řím (Centro Fermi, Sapienza), Frascati, Budapešť (Wigner, ELTE), Măgurele. arXiv duben 2025, PRR listopad 2025. ✅

### S07–S08 — „if one particular idea … is right", „in these models … would"
[B25] abstrakt: *these models suggest an induced uncertainty in the flow of time*. Podmíněné. ✅

### S10, S50 — nejvíc trpí nejmenší hodiny
[B25], obr. 1 a rov. (12)–(15): fluktuace maximální pro poloměr hodin R ≲ σ, pro větší klesá (CSL ~ (R/σ)⁻³, DP ~ (R/σ)⁻¹). ✅ „Cheap ones" je rétorický kontrast.

### S14 — Sr, ~429 bilionů vln za sekundu
[BIPM] 429 228 004 229 873 Hz. „Counts the waves of a laser locked to strontium atoms" — hodiny počítají kmity laseru stabilizovaného na přechod Sr. ✅

### S17 — hlouběji v gravitačním poli hodiny jdou pomaleji
Gravitační dilatace času (obecná relativita), ověřeno např. [C10], [Bo22]. ✅

### S18 — 2010, hodiny zvednuté o 33 cm šly rychleji
[C10]: Al-Mg hodiny zvednuty celkem o 33 cm (ze 17 cm pod druhými hodinami). **v0.3 měla *„lifted … thirty-three centimetres above another"*** — to neplatí (skončily ~16 cm nad), opraveno na *raised … by just thirty-three centimetres*. Výše položené hodiny jdou rychleji (gravitační rudý posuv). ✅ po opravě

### S19–S20 — 2022, rozdíl uvnitř jednoho oblaku přes 1 mm, ~1 : 10¹⁹
[Bo22]: lineární gradient frekvence uvnitř jediného milimetrového vzorku ultrachladného Sr, v souladu s gravitačním rudým posuvem, nejistota 7,6e-21. Očekávaný posuv gΔh/c² = 9,81 × 1e-3 / 8,99e16 = **1,09e-19** na mm = jedna ku deseti trilionům (10 mld × mld). Tým Juna Ye, JILA Boulder = „the team in Boulder". ✅

### S21 — „in the way some quantum models predict"
[B25]: kolapsové modely jako náhodná složka Newtonova potenciálu. ✅

### S23–S26 — superpozice, unitární vývoj nevybírá výsledek, problém měření, sto let sporů
Učebnicové. Kvantová mechanika 1925–27, tedy ~100 let. ✅

### S27 — kolapsové modely: příroda volí sama, bez pozorovatele
[B25]: *explain the quantum-to-classical transition without invoking the von Neumann measurement postulate*; *quantum measurements occur continuously and everywhere in nature*. ✅

### S28 — první úplný kolapsový model, 80. léta, jedna částice jednou za ~300 mil. let
[GRW] 1986, λ = 1e-16 s⁻¹ → 1/λ = 1e16 s = **3,17e8 let**. ✅
**v0.3 měla *„the very first collapse model"*** — Pearle navrhoval stochastickou redukci už 1976, GRW je v literatuře „first consistent". Opraveno na *first complete*. ✅ po opravě

### S29 — kočka ~10²⁷ částic, ~10¹¹ lokalizací za sekundu
Kočka 4 kg / 1,66e-27 kg = 2,4e27 nukleonů („roughly a billion billion billion" = 1e27, řádově). Rychlost v GRW = Nλ = 2,4e11 s⁻¹ („around a hundred billion", řádově). Lokalizace jediné složky lokalizuje celek — proto *together*. ✅ (ilustrace GRW, CSL formálně jinak; posudek v0.2 potvrdil)

### S30 — proto atomy ve dvou místech, kočky ne
Vysvětlení **v rámci modelů**; v0.4 doplněno *In these models*. ✅

### S31–S33 — Penrose a Diósi, hmota ve dvou místech = dvě gravitační pole, gravitace vynutí volbu
Diósi 1987/1989, Penrose 1996. [B25]: DP *explicitly relies on the hypothesis of spacetime fluctuations*. ✅

### S34 — Diósi spoluautorem [B25]
✅

### S35–S36 — šum kolapsových modelů lze interpretovat jako fluktuace gravitace, i u nejstudovanějšího (CSL), který s gravitací spojen nebyl
[B25] úvod: *We show that this mechanism could link both models — not just DP — to fundamental uncertainties in Newtonian gravity*; *the stochastic field responsible for irreversibility in CSL has never been connected to gravity*; rov. (2)–(3): φ *plays the role of the Newtonian potential*. „Can be interpreted" odpovídá. CSL a DP jsou podle [B25] *by far the most extensively studied*; CSL je obecně nejstudovanější. ✅

### S38 — rychlost hodin kolísá, kolik — závisí na velikosti
[B25] rov. (6)–(8): δt = (1/c²)∫φ dτ, průměr přes objem hodin. ✅

### S39 — žádné pixely, žádný nejmenší tik
[B25] počítá spojitou náhodnou fluktuaci (bílý šum), žádnou diskretizaci času. ✅

### S40–S42 — náhodná procházka, 4× déle → 2× větší typický drift
[B25]: Δt = √(τt). √4 = 2. ✅

### S43 — stínění ani chladnější laboratoř to neodstraní
Vnitřní vlastnost modelu, nezávisí na prostředí; závisí jen na velikosti hodin (S44). ✅

### S45 — v CSL se fluktuace mění na škále ~1e-7 m, velikost viru
[B25]: σ = 1e-7 m (CSL), korelace D_CSL ~ exp(−x²/4σ²). Viry ~20–400 nm. ✅

### S46–S47 — malé hodiny cítí plnou fluktuaci, větší zprůměrují
[B25], rov. (12), obr. 1. ✅

### S48 — pulzar, ~20 km, skoro imunní
[B25]: *pulsar clocks are expected to be insensitive to noise induced by SCMs, as this would be suppressed by the extremely small ratio σ/R*. Neutronová hvězda ~20–24 km v průměru. ✅

### S49 — u DP škála ~100× menší, princip platí
[B25]: σ_DP = 1e-9 m (referenční) vs 1e-7 m → 100×. Spodní experimentální mez σ_DP > 4,94e-10 m. DP korelace je dalekodosahová (~erf(x/2σ)/x), ale τ_DP ~ (R/σ)⁻¹ → větší hodiny i tak průměrují. ✅

### S52–S53 — ~1e-28 s za rok při standardních parametrech CSL, nejcitlivější velikost; rozsah
τ_CSL^max = ħ²λ/(m0²c⁴) = **4,99e-65 s** (souhlasí s obr. 1, ~5e-65). Za rok √(τt) = **3,97e-29 s**; [B25] rov. (16) uvádí ≃ 1e-28 s → scénář cituje článek (*about*). 1e-28 = desetitisícina bilióntiny bilióntiny ✅.
Rozsah [B25]: povolené 1e-20 < λ < 1e-11 s⁻¹ → článek 1e-31 až 1e-26 s/rok. Přesně: Δt ∝ √λ → 4,0e-31 až 1,3e-26, tedy **~100× menší až ~330× větší**. v0.3 měla *a hundred times larger*, opraveno na *a few hundred times larger, or a hundred times smaller*. ✅ po opravě

### S54 — dnešní optické hodiny ~1e-17 s po jedné sekundě
[B25] s. 4: krátkodobá stabilita ~1e-17/√(t/1 s), *corresponding to time fluctuations of approximately 10⁻¹⁷ s · √(t/1 s) over periods of hours or days*. ✅

### S55 — za den šum ~10¹⁵× větší než předpovězený efekt
Hodiny: 1e-17 × √86400 = 2,9e-15 s. CSL: √(4,99e-65 × 86400) = 2,1e-30 s. Poměr **1,4e15** = „a million billion". ✅ (výpočet, ne číslo z článku)

### S56 — od Velkého třesku jen několik bilióntin bilióntiny sekundy
√(4,99e-65 × 4,35e17) = **4,7e-24 s** = 4,7 bilióntin bilióntiny. ✅
(Posudek v0.2 navrhoval 1e-26 — početní chyba: 1e-28 × √1,38e10 = 1,2e-23, ne 1,2e-26.)

### S57 — DP ještě několiksetkrát menší
τ_DP^max = ħG/(√π c⁴ σ) = **4,92e-70 s** (obr. 1: ~5e-70). Za rok **1,25e-31 s** ([B25]: ≃1e-31). Poměr √(τ_CSL/τ_DP) = **~320×**. ✅

### S58 — pro všechny existující hodiny zanedbatelné
[B25] abstrakt: *remains negligible for all contemporary time-keeping devices, including atomic clocks*; závěr: *entirely negligible compared to the performance of current time-keeping technology*. ✅

### S59–S62 — otázka, zda je kvantová mechanika úplná; když modely neplatí, tento zdroj zmizí; když platí, je tu mez daná přírodou
Interpretace, podmíněně formulováno. [B25]: *an unavoidable uncertainty in any time measurement*, je-li τ nenulové. ✅

### S63 — 2020, pod horou v Itálii vyloučena nejjednodušší verze DP bez nastavitelných parametrů
[D20]: online 7. 9. 2020, Gran Sasso (LNGS), závěr *exclude the parameter-free version of the DP model*. Autoři zčásti titíž jako [B25] (Curceanu, Piscicchia, Diósi) — scénář to neříká, není třeba. ✅

### S64 — jiné verze zůstávají možné
DP s σ ≳ 5e-10 m a CSL v povoleném rozsahu ([B25] citace [26]); [D20]: CSL se falzifikuje hůř. ✅

### S65–S68 — závěr a otázka
Bez faktických tvrzení; *maybe* drží podmíněnost. ✅

## Opravy z fact checku (v0.3 → v0.4)

| scéna | v0.3 | v0.4 | proč |
|---|---|---|---|
| S18 | *lifted one atomic clock just thirty-three centimetres above another, and saw the higher one run faster* | *raised one atomic clock by just thirty-three centimetres, and saw it run faster* | zvednuty **o** 33 cm ze 17 cm pod, ne 33 cm nad [C10] |
| S28 | *the very first collapse model* | *the first complete collapse model* | Pearle 1976 před GRW |
| S30 | *That's why atoms…* | *In these models, that's why atoms…* | vysvětlení platí v modelech |
| S53 | *a hundred times larger* | *a few hundred times larger* | √(1e-11/1e-16) = 316 |

## Obrázky (storyboard, 2026-11-10)

| scéna | co ukazuje | ověření |
|---|---|---|
| S14 | *17jila003 3d strontium atomic clock* (NIST, public domain) | stronciové mřížkové hodiny JILA v Boulderu (3D mřížka, 2017). **Ne nutně** rekordní hodiny z [Aeppli 2024]; hlas říká jen *the clock in Boulder … strontium atoms*, fotka nic dalšího netvrdí. ✅ |
| S63 | *Corno grande da campo imperatore* (Fiat 500e, CC BY 4.0) | Corno Grande, nejvyšší vrchol masivu Gran Sasso d'Italia, pohled z Campo Imperatore. Laboratoř LNGS leží pod tímto masivem (~1 400 m horniny), takže *deep beneath a mountain in Italy* sedí. Dotaz ChatGPT k draftu („ověřit, že jde o Gran Sasso“): ano, je to tentýž masiv, ne konkrétní vstup do laboratoře. ✅ |
| S45–S49 | mřížka pole fluktuací | buňky jsou **prostor** (korelační délka r_C ≈ 1e-7 m), ne kvanta času; od 2026-11-10 v S45 popisek CHANGES FROM PLACE TO PLACE (zpětná vazba ChatGPT: aby se mřížka nečetla jako „pixely času“ po S39). Ve skutečném CSL je šum spojitě vyhlazený gaussovsky, čtverce jsou zjednodušení. ✅ |
| S17, S38 | rozdíl tiků | přehnaný, nese štítek EXAGGERATED. ✅ |
