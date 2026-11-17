# Fact check — 075 How Do You Make Microplastics Without Knowing It? (script 0.1)

Ověřeno 2026-09-30. Primární zdroje jsou abstrakty a metadata článků
(Crossref, Europe PMC, OpenAlex, Semantic Scholar); plné texty u Elsevieru
a ACS jsou za paywallem nebo za captchou, takže **detaily, které v abstraktu
nejsou, jsou výslovně označené jako neověřené**. Fraunhofer UMSICHT 2018
přečten celý (PDF → `pdftotext -layout`).

Legenda: ✅ OK · ⚠️ upřesnit · ❌ chyba

## Úvod a odkaz na 012 (S03, S05, S83)

| scéna | tvrzení | ověření | závěr |
|---|---|---|---|
| S03 | „some of that missing material doesn't disappear. It becomes tiny plastic particles." | obecný mechanismus otěru; doloženo všemi studiemi níž (houbička, prkénko, struna, podrážka) | ✅ |
| S05 | „we followed the biggest source of this kind of wear. The tyres on your car." | **pro:** nařízení (EU) 2024/1257 (Euro 7), recitál 20: *„Emissions from tyres are estimated to be the largest source of microplastics released into the environment."* Fraunhofer UMSICHT 2018, tab. 3-1: „Abrieb Reifen" **1 228,5 g/(cap·a)**, 1. místo z 51 zdrojů (celkem 2 880 g/(cap·a) spočítaných). **proti:** EEA, Zero pollution dashboard, indikátor *Microplastic releases to the environment* (data 2022) dává *„paints (43%), tyre abrasion (35%), plastic pellets (9%) and textiles (3%)"* — barvy jsou tam větší. Barvy se ale uvolňují hlavně zvětráváním a údržbou, ne otěrem při používání, a Fraunhofer jim přisuzuje jen 65 g/(cap·a). Pro „this kind of wear" (otěr předmětu při používání) jsou pneumatiky obhajitelně první | ⚠️ obhajitelné, ale **012 samo tvrdilo opatrněji** („one of the major sources", viz `012…/factcheck.md` bod 2). Návrh v tabulce oprav |
| S83 | „With the tyres, we asked where all that missing tread went." | odkaz na 012, obsahové tvrzení žádné | ✅ |

Pro představu o řádech (spočteno, do scénáře se nenavrhuje): pneumatiky
1 228,5 g/(cap·a) ÷ houbička 4,212 g = **292×**, ÷ 0,682 g = **1 801×**.

## Kuchyňská houbička (S07–S12)

**Zdroj:** Hamann L., Galafton C., Rühr P., Blanke A., Thonemann N. (2026):
*From sink to Sea: Microplastic release from kitchen sponges and potential
environmental effects.* **Environmental Advances 23, 100693.**
DOI [10.1016/j.envadv.2026.100693](https://doi.org/10.1016/j.envadv.2026.100693).
Online **24. 2. 2026**, číslo **duben 2026** (Crossref/OpenAlex). Open access.

| scéna | tvrzení | ověření | závěr |
|---|---|---|---|
| S09 | „A 2026 study" | online i tištěné vydání spadá do 2026 — obojí sedí | ✅ |
| S09 | „measured microplastic release from kitchen sponges during normal use" | abstrakt: *„we determined the MP release of kitchen sponges based on a combination of citizen science and laboratory experiments"* (domácnosti v Německu a Severní Americe, houbičky vážené před a po použití; laboratorní „SpongeBot" — phys.org 21. 3. 2026) | ✅ |
| S10 | „roughly zero point seven to four point two grams of microplastics per person per year" | abstrakt: *„The total MP release from different sponges into the wastewater stream ranges between 0.682 ± 0.566 and 4.212 ± 3.039 g of MP per year and person."* Tři typy: EU-con, AM-con, EU-org (phys.org); prostřední hodnota **1,171 g** v abstraktu **není** (je jen v tiskových zprávách / úryvku ScienceDirect) — pro scénář nepotřebná | ✅ |
| S10 | jsou to **mikroplasty**, ne celková hmotnost otěru? | abstrakt uvádí jednotku výslovně „g of MP" a vazbu na podíl plastu: *„If the sponges contain plastics, it is released into the wastewater as microplastics"*; houbička „organic" má **15,9 hm. %** plastu a nejnižší únik, jiná **59,3 hm. %**. Hodnota je tedy **plastový podíl odebrané hmoty**, ne celkový úbytek houbičky. Že se to počítá přesně jako úbytek × podíl plastu, z abstraktu nevyplývá (plný text za captchou) — částice se jednotlivě **nepočítaly ani neidentifikovaly**, je to hmotnostní odhad | ✅ (scénář říká „estimated", což sedí) |
| S10 | „Depending on the type of sponge" | rozdíl vysvětluje podíl plastu v houbičce | ✅ |
| S12 | „going down the drain" | *„into the wastewater stream"* | ✅ |

> **Pozor na rozptyl:** směrodatné odchylky jsou skoro stejně velké jako
> průměry (0,682 ± 0,566). „Roughly" to unese.

## Melaminová houbička (S13–S15)

**Zdroj:** Su Y., Yang C., Wang S., Li H., Wu Y., Xing B., Ji R. (2024):
*Mechanochemical Formation of Poly(melamine-formaldehyde) Microplastic Fibers
During Abrasion of Cleaning Sponges.* **Environmental Science & Technology
58, 10764–10775.** DOI [10.1021/acs.est.4c00846](https://doi.org/10.1021/acs.est.4c00846).

| scéna | tvrzení | ověření | závěr |
|---|---|---|---|
| S14 | melaminové houbičky = „magic erasers" | abstrakt: *„melamine cleaning sponges (also known as „magic erasers")"* | ✅ |
| S14 | „can produce millions of microscopic polymer fibres as they wear down" | abstrakt: *„The sponge wear could release 6.5 million MPFs/g"* — **jednotka je na gram odebrané houbičky**, ne na použití. Vlákna z poly(melamin-formaldehydu), **10–405 µm** dlouhá. Laboratorní abrazér proti kovovým povrchům různé drsnosti; globální odhad 4,9 bilionu vláken ročně | ✅ „millions" odpovídá řádu na gram; zpřesnění volitelné (viz opravy) |
| S15 | houbička „slowly disappearing" | úbytek hmoty = zdroj vláken | ✅ |

## Prkénko (S16–S22)

**Zdroj 1 (S19):** Yadav H., Khan M. R. H., Quadir M., Rusch K. A., Mondal P. P.,
Orr M., Xu E. G., Iskander S. M. (2023): *Cutting Boards: An Overlooked Source
of Microplastics in Human Food?* **Environmental Science & Technology 57,
8225–8235.** DOI [10.1021/acs.est.3c00924](https://doi.org/10.1021/acs.est.3c00924).

**Zdroj 2 (S20):** Čapla J., Zajác P., Fikselová M., Tulipánová A., Imreová Z.
(2026): *Potential contribution of surface-degraded plastic cutting boards to
microplastic contamination in meat processing.* **Food Control 189, 112306.**
DOI [10.1016/j.foodcont.2026.112306](https://doi.org/10.1016/j.foodcont.2026.112306)
(online 15. 5. 2026).

**Zdroj 3 (S20):** Wang Y., Zhao Y., Jiang Y., Xie M., Ma F., Wang G. (2026):
*Polyethylene cutting board-derived microplastics: mechanical abrasion in retail
meat processing…* **Food Research International 231, 118677.**
DOI [10.1016/j.foodres.2026.118677](https://doi.org/10.1016/j.foodres.2026.118677).

Starší: Habib R. Z. a kol. (2022), *Plastic cutting boards as a source of
microplastics in meat*, Food Additives & Contaminants A 39, 609–619,
DOI [10.1080/19440049.2021.2017002](https://doi.org/10.1080/19440049.2021.2017002).

| scéna | tvrzení | ověření | závěr |
|---|---|---|---|
| S17–S18 | nůž dělá rýhy, povrch hrubne, odlupují se kousky polymeru | mechanismus popsán u Yadav 2023 i Habib 2022 (opotřebení, 875 g PE ztracených za život prkénka — Habib) | ✅ |
| S19 | měřeny mikroplasty z **polyethylenových i polypropylenových** prkének při krájení | Yadav 2023: *„The mass and number of microplastics released from polypropylene chopping boards were greater than polyethylene by 5-60% and 14-71%"*; převážně částice < 100 µm | ✅ |
| S20 | „newer experiments have even detected plastic particles transferred from worn cutting boards onto meat" | Čapla 2026: pilotní studie, 5 PE prkének v různém stupni opotřebení, vepřové maso, LDIR, jen částice ≥ 10 µm; *„worn plastic cutting boards may contribute to microplastic contamination during meat preparation"*. Wang 2026: přenos na maso *„occurred inconsistently"*. Nález v mase z řeznictví už Habib 2022 | ✅ „detected" je přesné; neříká se, kolik, a to je správně — přenos je nekonzistentní a Čapla výslovně žádá opatrný výklad (11 typů polymerů, ne všechny z prkénka) |
| S21–S22 | stopy nože = fyzicky odebraný povrch | tamtéž | ✅ |

## Myčka (S23–S28)

**Zdroj:** Okoffo E. D., Tscharke B. J., Thomas K. V. (2025): *Release of
Micro- and Nanosized Particles from Plastic Articles during Mechanical
Dishwashing.* **ACS ES&T Water 5, 2870–2881.**
DOI [10.1021/acsestwater.4c00768](https://doi.org/10.1021/acsestwater.4c00768)
(online 19. 5. 2025).

| scéna | tvrzení | ověření | závěr |
|---|---|---|---|
| S25 | horká voda, detergenty, trysky, mechanické síly | cyklus 70 °C (UQ tisková zpráva 20. 5. 2025) | ✅ |
| S26 | „plastic containers and utensils made from several common polymers in domestic dishwashers" | abstrakt: *„The selected PP, PE, PS, PET, and nylon-6 articles were mechanically washed using **a domestic dishwasher**"* — pět polymerů; myčka jedna (množné „dishwashers" je obecné, nevadí). Testované předměty byly **nové** | ✅ |
| S27 | „mechanical dishwashing can release both microplastics and nanoplastics" | abstrakt: *„micro- and nanoparticles are released"*; frakce 0,01–0,3 / 0,3–1 / 1–2,7 / > 2,7 µm; až ~920 000 částic na plný cyklus, ~33 mil. na domácnost a rok. **Ale:** počty částic jsou z FlowSync (velikost), polymer se určoval hmotnostně pyrolýzní GC-MS, ne u jednotlivých částic — titul studie proto opatrně říká „micro- and nanosized particles". A autoři sami: *„less than 6 mg/year/person… the source contribution from dishwashers is relatively low"* | ✅ se zmírněním — scénář číslo nedává a velikost neslibuje, což je správně. Kdyby se přidávalo 920 000, musí jít spolu s „relatively low" |

## Pračka (S29–S35)

**Zdroje:** Napper I. E., Thompson R. C. (2016): *Release of synthetic
microplastic plastic fibres from domestic washing machines: Effects of fabric
type and washing conditions.* **Marine Pollution Bulletin 112, 39–45.**
DOI [10.1016/j.marpolbul.2016.09.025](https://doi.org/10.1016/j.marpolbul.2016.09.025).
Luzi B. a kol. (2025): *Critical review of microfiber release from textiles…*
**Chemosphere 378, 144394.** DOI [10.1016/j.chemosphere.2025.144394](https://doi.org/10.1016/j.chemosphere.2025.144394).

| scéna | tvrzení | ověření | závěr |
|---|---|---|---|
| S30 | syntetické oblečení uvolňuje mikrovlákna: polyester, nylon, akryl | Napper 2016 testoval polyester, polyester-bavlnu a akryl (*„over 700,000 fibres… from an average 6kg wash load of acrylic"*); polyamid (nylon) jako zdroj u Forster 2023 (LDIR na stezkách) a v přehledu Luzi 2025 | ✅ |
| S31–S32 | natahování, ohyb, tření → vlákna odcházejí s odpadní vodou | Napper 2016 (vlákna v odpadní vodě pračky) | ✅ |
| S33 | „different studies get very different numbers" | Luzi 2025: *„a standardized protocol for measuring MFs release remains absent, leading to inconsistencies… the lack of a unified measurement unit further complicates cross-study comparisons"* | ✅ |
| S34 | záleží na tkanině, pračce, programu a na tom, jak se vlákna počítají | Luzi 2025: *„type of washing machine, washing program, detergent, and softener significantly impact the quantity"*; přímé vs. nepřímé metody dávají různé řády; Napper 2016: tkanina i podmínky praní. Drobnost: část studií vlákna **nepočítá, ale váží** — „count" je zjednodušení | ✅ |
| S35 | „there isn't one magic number… fibres can end up in wastewater" | tamtéž | ✅ |

## Strunová sekačka (S36–S44)

**Zdroj:** Luo Y., Gibson C. T., Chuah C., Tang Y., Naidu R., Fang C. (2022):
*Applying Raman imaging to capture and identify microplastics and nanoplastics
in the garden.* **Journal of Hazardous Materials 426, 127788.**
DOI [10.1016/j.jhazmat.2021.127788](https://doi.org/10.1016/j.jhazmat.2021.127788)
(online 19. 11. 2021, University of Newcastle, Austrálie). Plný text za
paywallem, repozitář Newcastle nedostupný — **ověřeno z abstraktu**.

Abstrakt doslova: *„…plastic fragments or shreds (with diameters / widths of
80 nm – 3 µm) and nanoparticles (with diameters of < 1000 nm) that are released
during the **mimicked mowing process**. Using Raman imaging, **we estimate**
that thousands of microplastics (0.1-5 mm), and billions of nanoplastics
(< 1000 nm), are released per minute when a line trimmer is used to mow lawn."*

| scéna | tvrzení | ověření | závěr |
|---|---|---|---|
| S37 | „spinning nylon line" | struny jsou běžně z nylonu (polyamid); abstrakt polymer neuvádí, plný text nedostupný. Jako obecné tvrzení o struně OK | ✅ |
| S37 | struna je spotřební materiál | struna se při opotřebení a lámání dopouští z hlavy | ✅ |
| S40 | „Researchers actually **measured** what happens… They **found** thousands of microplastic particles being released every minute" | studie sečení **simulovala** („mimicked mowing") a počet za minutu je **odhad** extrapolovaný z Ramanových snímků („we estimate"), ne změřený úhrn. Velikost mikroplastů 0,1–5 mm | ⚠️ upřesnit „measured / found" → „estimated" |
| S42 | „estimated… billions of nanoscale plastic particles per minute under their test conditions" | sedí na abstrakt („we estimate… billions of nanoplastics (< 1000 nm)… per minute"); „under their test conditions" je přesná výhrada | ✅ |
| S42 | je fér říkat „nanoplastics / nanoscale"? | autoři definují nanoplasty jako **< 1000 nm**, což odpovídá ISO/TR 21960:2020 (nano < 1 µm). Část „nano" objektů jsou ale **útržky, u nichž je nanometrová jen šířka** (80 nm – 3 µm), délka může být větší. Identifikace takto malých částic Ramanem je na hranici metody — autorská skupina (C. Fang) ji vyvíjí sama a nezávislé zopakování s trimrem jsem nenašel | ✅ s výhradou; „nanoscale" a „estimated… under their test conditions" to unese |
| — | konkrétní čísla **6 000–11 250 mikro/min** a **13,2 mld. nano/min** | v abstraktu **nejsou**; 13,2 mld. se objevuje jen v sekundárních webech (a jeden píše nesmyslně „11,000 million microplastics"). Plný text nešlo otevřít | ⚠️ **neověřeno** — scénář je nepoužívá, a tak to má zůstat |
| S43 | „Billions." | viz S42 | ✅ |

## Boty (S45–S52)

**Zdroj:** Forster N. A., Wilson S. C., Tighe M. K. (2023): *Trail running
events contribute microplastic pollution to conservation and wilderness areas.*
**Journal of Environmental Management 331, 117304.**
DOI [10.1016/j.jenvman.2023.117304](https://doi.org/10.1016/j.jenvman.2023.117304).
Fraunhofer UMSICHT (Bertling J., Bertling R., Hamann L.) 2018: *Kunststoffe in
der Umwelt: Mikro- und Makroplastik*, Konsortialstudie, Oberhausen, tab. 3-1.

| scéna | tvrzení | ověření | závěr |
|---|---|---|---|
| S47 | podrážky často obsahují syntetické polymery jako polyuretan a syntetický kaučuk | Forster 2023: LDIR — hlavní typy na stezkách *„polyurethane, polyethylene terephthalate and polyamide"*, podrážky z tvrdé a měkké pryže („rubber fragments"); běžné materiály podrážek PU/TPU, EVA, SBR a přírodní kaučuk (Wasser 3.0, sekundárně) | ✅ „often" je správně (ne všechny) |
| S49 | měřeny mikroplastické částice z otěru obuvi | Forster 2023: *„abrasive wear to shoe outsoles produced an average of 0.3 ± 0.1 to 0.9 ± 0.2 MPs/linear metre/runner"*; měkká pryž víc než tvrdá | ✅ |
| S50 | venku nalezeny částice podrážek vedle vláken ze syntetického oblečení | Forster 2023 na stezkách po závodech: *„included fibres and rubber fragments"*; oblečení 0,7–2,0 vláken/m/běžce, vlákna 63–69 % všech MP | ✅ |
| S52 | násobeno kroky, lidmi a lety = environmentální zdroj | Fraunhofer 2018: „Abrieb Schuhsohlen" **109 g/(cap·a)**, **7. místo** z 51 zdrojů v Německu | ✅ |

## Zubní kartáček (S53–S59)

**Zdroj:** Öztürk Aytulun Ç., Akbari Dana P., Gachayzade Z., Gedik K., Balcı N.,
Toygar H. (2025): *Preliminary results on microplastic release from commercial
toothbrushes during simulated brushing.* **Microchemical Journal 216, 114680.**
DOI [10.1016/j.microc.2025.114680](https://doi.org/10.1016/j.microc.2025.114680)
(online 26. 7. 2025). Plný text ani abstrakt z primárního zdroje nešly otevřít
(ScienceDirect 403, ResearchGate 403); **níže je znění abstraktu, jak ho
shodně citují výsledky vyhledávání** — tedy slabší doklad než u ostatních.

| scéna | tvrzení | ověření | závěr |
|---|---|---|---|
| S54 | „twice a day", štětiny se ohýbají, opotřebují | protokol studie: čištění **dvakrát denně po sedm dní** na 3D modelu zubního oblouku ze zirkonie | ✅ |
| S55 | „A 2025 study simulated normal brushing with commercial toothbrushes and found microplastic particles released from their bristles" | tamtéž; *„All toothbrushes released microplastics regardless of brand"*; charakterizace mikroskopií, FTIR a µ-Ramanem | ✅ (studie se sama nazývá „preliminary") |
| S56 | „The exact amount varied between products" | *„the least expensive brand generating the highest number"* | ✅ |
| S56 | „One of the tested brushes released an average of up to about thirty-nine particles per day" | abstrakt: *„An average of up to 39 microplastics per day are released, as confirmed by Raman spectroscopy"* a *„the least expensive brand… averaging 39 particles per day"*. „Up to" v abstraktu znamená **nejvyšší průměr mezi značkami**, ne horní mez u jedné značky — spojení „one of the brushes… an average of up to" je proto zdvojené a trochu matoucí | ⚠️ upřesnit formulaci (viz opravy) |
| S56 | velikostní rozsah, co je „particle" | **neověřeno** — v dostupném znění abstraktu není; částice jsou fragmenty, vlákna, filmy a pelety, polymery PBT a nylon | — scénář velikost neuvádí, v pořádku |
| S57 | „That doesn't mean you are swallowing thirty-nine dangerous particles… The study did not establish that." | studie měřila uvolnění na modelu, ne příjem ani toxicitu | ✅ |

## Umělý trávník (S60–S67)

**Zdroje:** Harusato A., Kato M. (2025): *Mechanisms of Generation and
Ecological Impacts of Nano- and Microplastics from Artificial Turf Systems in
Sports Facilities.* **Environments 12, 109.**
DOI [10.3390/environments12040109](https://doi.org/10.3390/environments12040109) (přehled).
Kittner M., Coesfeld B., Werischak T., Schlau S., Altmann K., Kalbe U. (2025):
*Simultaneous sampling for microplastics and environmental contaminants from
artificial turf…* **Environmental Sciences Europe 37, 178.**
DOI [10.1186/s12302-025-01235-1](https://doi.org/10.1186/s12302-025-01235-1).

| scéna | tvrzení | ověření | závěr |
|---|---|---|---|
| S62 | stébla jsou syntetická vlákna | Kittner 2025: vlákna trávy jako PE | ✅ |
| S63–S64 | mechanická aktivita přispívá k uvolňování a přesunu vláken a dalších plastů | Harusato 2025: *„Combined mechanical stress, ultra-violet radiation, and weathering processes contribute to the breakdown of synthetic grass fibers and infill materials"*; nalezeno v drenážích a okolní půdě. Kittner 2025: stárnutí zvyšuje tvorbu MP *„especially from rubber infill and grass fibres"* | ✅ |
| S65 | „We don't yet have a perfect number" | Harusato 2025: *„field data on emission rates and environmental fate remain limited, and standardized methods for particle characterization and quantification are lacking"* | ✅ |
| S66 | různé systémy, různé výplně, zvětrávání, slunce, údržba mění výsledek | Kittner 2025: systém s pryžovou výplní vs. bez ní 5,4–8,0 vs. 0,2–5,3 mg/m², reálně stárnuté 136,4–252,5 mg/m² za 15 let; UV a stárnutí (Harusato, Kittner); údržba jako mitigační opatření (Harusato) | ✅ |
| S67 | tření o boty, materiál opouští hřiště | mechanismus výš | ✅ |

> **Stojí za vědomí:** u umělých trávníků je největší zdroj obvykle
> **granulát výplně**, ne stébla — Fraunhofer 2018 dává hřištím 96,6 g/(cap·a)
> hlavně kvůli výplni a EU ji nařízením 2023/2055 omezuje (zákaz uvádění na
> trh od října 2031). Scénář to kryje slovy „and other plastic materials"
> a „different infills behave differently", takže chyba to není.

## Vzorec a zdraví (S70–S82)

| scéna | tvrzení | ověření | závěr |
|---|---|---|---|
| S72–S73 | vedle rozpadu odpadu existuje cesta „plast → tření → otěr → částice" | Fraunhofer 2018 řadí otěr (pneumatiky, podrážky, textil…) mezi zdroje **primárního** mikroplastu, odděleně od rozpadu makroplastu | ✅ |
| S78 | nález mikroplastů neříká, co dělají v těle | WHO (2022), *Dietary and inhalation exposure to nano- and microplastic particles and potential implications for human health*, Ženeva: *„the limited data provide little evidence that MNPs have adverse effects in humans"*, velké mezery ve znalostech | ✅ |
| S79 | „we still don't know what level of exposure is harmful" | WHO 2022 tamtéž; WHO 2019, *Microplastics in drinking-water*: riziko hodnoceno jako nízké, ale na omezené evidenci, s výzvou k dalšímu výzkumu. Prahová (bezpečná / škodlivá) dávka stanovená není | ✅ |
| S80 | věda neopravňuje tvrzení, že kartáček nebo prkénko otravuje | Yadav 2023: předběžný test toxicity PE částic na myších fibroblastech *„did not show adverse effects"* za 72 h; kartáček viz S57 | ✅ |
| S81 | materiály jsou extrémně trvanlivé | obecně | ✅ |

## Navržené opravy scénáře

`script.md` nezměněn.

| scéna | současné znění | návrh | důvod |
|---|---|---|---|
| S40 | „Researchers actually measured what happens during this process. / They found thousands of microplastic particles being released every minute." | „Researchers actually tested what happens during this process. / They estimated that thousands of microplastic particles are released every minute." | sečení bylo simulované a počet za minutu je extrapolovaný odhad (*„we estimate"*), ne měřený úhrn. S42 už „estimated" má, S40 by měla ladit |
| S56 | „One of the tested brushes released an average of up to about thirty-nine particles per day." | „The worst one released about thirty-nine particles a day, on average." | „up to" v abstraktu znamená nejvyšší průměr ze všech značek; ve spojení s „one of the brushes" je to zdvojené a v titulku to působí nejistě. Číslo se nemění |
| S05 | „we followed the biggest source of this kind of wear." | „we followed one of the biggest sources of this kind of wear." | Euro 7 a Fraunhofer mají pneumatiky jako největší zdroj, EEA (2022) ale dává barvám 43 % proti 35 %. A **012 samo** tvrdilo opatrněji („one of the major sources") — video, na které odkazujeme, by nemělo říkat míň než odkaz na něj |
| S14 (volitelné) | „can produce millions of microscopic polymer fibres as they wear down." | „can shed millions of microscopic polymer fibres for every gram that wears away." | jednotka studie je 6,5 mil. vláken **na gram** odebrané houbičky; dnešní znění není chybné, jen neurčité |

## Rozhodne uživatel

- **S05 „the biggest source"** — nechat, nebo zmírnit na „one of the
  biggest"? Pro zmírnění mluví EEA a konzistence s 012, proti tomu
  Euro 7 (recitál 20) a Fraunhofer, podle nichž jsou pneumatiky první,
  a u „this kind of wear" (otěr při používání) je to obhajitelné.
- **Číslo u prkénka** (ChatGPT navrhoval přidat 7,4–50,7 g/rok z PE,
  49,5 g/rok z PP, Yadav 2023): doložené, ale je to **odhad expozice
  „based on our assumptions"** a je o řád vyšší než houbička (0,7–4,2 g),
  takže by divák četl prkénko jako desetkrát horší — na to studie nejsou
  srovnatelné metodou. Doporučuju nepřidávat.
- **Číslo u myčky** (~920 000 částic na cyklus): jen spolu se závěrem
  autorů, že hmotnostně je to < 6 mg na osobu a rok a zdroj je „relatively
  low". Samotné by přehánělo. Současné znění bez čísla je bezpečné.
- **Trimmer 6 000–11 250 / 13,2 mld.**: z primárního zdroje neověřeno
  (paywall). Nepoužívat, dokud se nepřečte plný text.
- **Kartáček**: primární abstrakt nešel otevřít, doklad je znění citované
  výsledky hledání (shodné z více zdrojů). Studie je „preliminary". Pokud
  chceš mít jistotu u velikostí částic, je potřeba plný text.

## Zdroje

- Hamann et al. 2026 — https://doi.org/10.1016/j.envadv.2026.100693 ; phys.org 21. 3. 2026 https://phys.org/news/2026-03-dishwashing-side-effects-kitchen-sponges.html
- Su et al. 2024 — https://doi.org/10.1021/acs.est.4c00846
- Yadav et al. 2023 — https://doi.org/10.1021/acs.est.3c00924
- Čapla et al. 2026 — https://doi.org/10.1016/j.foodcont.2026.112306
- Wang et al. 2026 — https://doi.org/10.1016/j.foodres.2026.118677
- Habib et al. 2022 — https://doi.org/10.1080/19440049.2021.2017002
- Okoffo, Tscharke, Thomas 2025 — https://doi.org/10.1021/acsestwater.4c00768 ; https://news.uq.edu.au/2025-05-20-dishwashing-source-microplastic-pollution
- Napper & Thompson 2016 — https://doi.org/10.1016/j.marpolbul.2016.09.025
- Luzi et al. 2025 — https://doi.org/10.1016/j.chemosphere.2025.144394
- Luo et al. 2022 — https://doi.org/10.1016/j.jhazmat.2021.127788
- Forster, Wilson, Tighe 2023 — https://doi.org/10.1016/j.jenvman.2023.117304
- Öztürk Aytulun et al. 2025 — https://doi.org/10.1016/j.microc.2025.114680
- Harusato & Kato 2025 — https://doi.org/10.3390/environments12040109
- Kittner et al. 2025 — https://doi.org/10.1186/s12302-025-01235-1
- Fraunhofer UMSICHT 2018 — https://www.umsicht.fraunhofer.de/content/dam/umsicht/de/dokumente/publikationen/2018/kunststoffe-id-umwelt-konsortialstudie-mikroplastik.pdf
- Nařízení (EU) 2024/1257, recitál 20 — http://data.europa.eu/eli/reg/2024/1257/oj
- EEA, Microplastic releases to the environment — https://www.eea.europa.eu/en/european-zero-pollution-dashboards/indicators/microplastic-releases-to-the-environment
- WHO 2022 — https://iris.who.int/items/3fb893bd-cc75-40d4-aabf-3ed028130bcc
- WHO 2019 — https://www.who.int/news/item/20-08-2019-microplastics-in-drinking-water
