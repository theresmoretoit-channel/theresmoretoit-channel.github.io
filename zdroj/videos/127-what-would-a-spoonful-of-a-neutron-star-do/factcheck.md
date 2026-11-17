# 127 — fact check (scénář 0.4 → 0.5, 2026-10-29)

Scény podle `script 0.5.md` (= `script.md`; od 0.4 se liší jen S27 a S42).
Závěr: ✅ doloženo, ✏️ opraveno ve scénáři, 💬 úvaha / zjednodušení
(není faktické tvrzení, jen nesmí lhát).

Konstanty pro výpočty: CODATA 2022 (m_n = 939,565 42 MeV, m_p = 938,272 09 MeV,
m_e = 0,510 999 MeV, m(¹H) = 1,007 825 03 u, u = 931,494 10 MeV),
hmotnosti nuklidů AME2020. Výpočty jsou počítané, ne opsané.

## Lžička: hustota a hmotnost

| | tvrzení | ověření | |
|---|---|---|---|
| S01–S02, S54, S69 | lžička hmoty neutronové hvězdy by na Zemi vážila *billions of tonnes* | 5 ml × saturační hustota 2,7×10¹⁷ kg/m³ (Janka 2012: „nuclear densities (ρ ≳ 2.7 × 10¹⁴ g/cm³)", [arXiv:1206.2503](https://arxiv.org/abs/1206.2503)) = **1,35 mld. t**; s průměrnou hustotou hvězdy (1,4 M☉, R 11–13 km → 3,0–5,0×10¹⁷ kg/m³) **1,5–2,5 mld. t**; střed 5–10× n₀ (Lattimer & Prakash 2004, [astro-ph/0405262](https://arxiv.org/abs/astro-ph/0405262)). NASA Goddard: „one teaspoon of neutron star matter would weigh a billion tons" ([NASA](https://www.nasa.gov/centers-and-facilities/goddard/new-nasa-mission-to-study-mysterious-neutron-stars-aid-in-deep-space-navigation/)). Údaj DOE „10 milionů tun" by odpovídal hustotě ~100× pod jadernou; scénář ho nepřebírá | ✅ |
| S03 | to je několikanásobek hmotnosti všech žijících lidí | populace 8,2 mld. v polovině 2024 ([UN News, 11. 7. 2024](https://news.un.org/en/story/2024/07/1151971)) × 50–62 kg (průměr dospělého 62 kg; dospělí v roce 2005 dohromady 287 mil. t, Walpole a kol. 2012, [BMC Public Health 12:439](https://bmcpublichealth.biomedcentral.com/articles/10.1186/1471-2458-12-439)) = **0,41–0,51 mld. t**. Lžička 1,35–2,5 mld. t → **2,6× až 6×**. „Several" drží; při nejmenší lžičce je to na spodní hraně | ✅ |

## S06–S13 Prázdný atom

| | tvrzení | ověření | |
|---|---|---|---|
| S08 | malé jádro ve středu, kolem elektrony, mezi nimi „almost nothing" | popularizační zjednodušení (elektrony jsou rozprostřená vlnová funkce, ne kuličky na dráze); „almost" drží míru | 💬 |
| S09 | atom jako stadion → jádro hrášek uprostřed hřiště | poměr průměru atomu a jádra: H ≈ 62 000 (1,06×10⁻¹⁰ m / 1,7 fm), C ≈ 28 000, O ≈ 22 000. Stadion 200–300 m → jádro **3–14 mm**, hrášek 7–9 mm | ✅ |
| S10 | v jádře je přes 99,9 % hmoty atomu | ¹H: m_p/(m_p+m_e) = **99,95 %**; ¹²C: 99,97 % | ✅ |
| S11 | lidstvo bez prázdného prostoru by se vešlo do kostky cukru | 0,41–0,51 mld. t / 2,7×10¹⁷ kg/m³ = **1,5–1,9 cm³**; kostka cukru má 2–4 cm³. Podmíněně („If you could squeeze") | ✅ |
| S12 | neutronová hvězda je hmota v takovém stavu, kde běžné atomy nemohou existovat | viz S26–S30: v jádru hvězdy pár % protonů, žádné atomy s elektronovým obalem | ✅ |

## S14–S19 Jádro a silná interakce

| | tvrzení | ověření | |
|---|---|---|---|
| S14–S16 | jádro z protonů a neutronů, protony se elektricky odpuzují, přesto jádra existují | učebnicové | ✅ |
| S17 | drží je silná interakce mezi protony a neutrony, na krátkou vzdálenost přebije elektrické odpuzování | jaderná (reziduální silná) síla mezi nukleony; formulace z recenze 0.1 záměrně nemluví o kvarcích | ✅ |
| S18 | dosah malý, za šířkou několika protonů rychle slábne | dosah ~ Comptonova vlnová délka pionu ≈ **1,4 fm** (Weise 2007, [arXiv:0704.1992](https://arxiv.org/abs/0704.1992)); poloměr protonu 0,84 fm (CODATA 2022), tedy průměr ~1,7 fm. Yukawův potenciál klesá jako e^(−r/1,4 fm)/r — „fades away very quickly", ne ostrá hrana | ✅ |

## S20–S25 Kolaps a supernova

| | tvrzení | ověření | |
|---|---|---|---|
| S20 | hvězda mnohokrát těžší než Slunce, miliony let fúze | „a star heavier than about 8 solar masses" (Woosley & Janka 2005, [astro-ph/0601261](https://arxiv.org/abs/astro-ph/0601261)); životnost takových hvězd jsou jednotky až desítky milionů let | ✅ |
| S21 | železné jádro těžší než Slunce, zhruba velikosti Země | „the iron core, which itself typically has a mass in the range 1.4 to 2.0 M⊙" (Sukhbold & Woosley 2014, [arXiv:1311.6546](https://arxiv.org/abs/1311.6546)); „Starting from the size of the Earth, the core collapses…" (Woosley & Janka 2005) | ✅ |
| S22 | fúze železa neuvolňuje energii; když je jádro dost těžké, gravitaci neudrží | vrchol vazebné energie na nukleon u ⁵⁶Fe/⁶²Ni. Spouštěčem kolapsu je ve skutečnosti ztráta tlaku elektronů (záchyt, fotodisintegrace) u jádra blízko Chandrasekharovy meze — „heavy enough" je zjednodušení, ale nelže | ✅ 💬 |
| S23 | za méně než sekundu se něco velikosti planety zmenší na velikost města | „the dense core of this star implodes within less than a second to neutron-star densities" (Burrows & Vartanyan 2021, [arXiv:2009.14157](https://arxiv.org/abs/2009.14157)); z velikosti Země na „neutron-rich sphere about 30 km in radius" (Woosley & Janka 2005) | ✅ |
| S24 | pod tím tlakem protony zachytávají elektrony, z protonu neutron a neutrino | „electrons are squeezed into iron-group nuclei, raising their neutron number" (Woosley & Janka 2005); „e-captures on nuclei (and some free protons) speed up and accelerate the implosion" (Janka 2012). **Pozor na pořadí:** záchyt začíná už před kolapsem a je jednou z jeho příčin — „start" je tedy zjednodušení. Protony uvnitř jader jsou pořád protony, takže věta platí | ✅ 💬 |
| S25 | záplava neutrin odnese většinu energie a pomůže odhodit vnější vrstvy | neutrina „carrying away about 99% of the gravitational binding energy" (Janka 2004, [astro-ph/0401461](https://arxiv.org/abs/astro-ph/0401461)); vazebná energie ~3×10⁴⁶ J (Lattimer & Prakash 2004). Ohřev neutriny „drives explosions" (Janka 2012) — vedoucí model, ne uzavřený; „helping" to drží | ✅ |

## S26–S33 Co zbyde a co to drží

| | tvrzení | ověření | |
|---|---|---|---|
| S26 | už to není z běžných atomů, elektrony jsou z velké části pryč | „neutron star matter has only a few percent protons" (Lattimer & Prakash 2004); elektronů je tolik co protonů. Podíl protonů při n₀ x = 0,040–0,053 (Hebeler a kol. 2013, [arXiv:1303.4662](https://arxiv.org/abs/1303.4662), tab. 2) | ✅ |
| S27 | objekt asi dvacet kilometrů napříč, převážně neutrony, zhruba hustota jádra | NASA: „about 12 miles (20 kilometers) across" (odkaz výš). **Změřené poloměry jsou ale 12,4–13 km**, tedy průměr ~25 km: J0030 1,34 M☉ / 12,71 km (Riley a kol. 2019, [arXiv:1912.05702](https://arxiv.org/abs/1912.05702)), 1,44 M☉ / 13,02 km (Miller a kol. 2019, [arXiv:1912.05705](https://arxiv.org/abs/1912.05705)); R(1,4 M☉) = 12,45 ± 0,65 km (Miller a kol. 2021, [arXiv:2105.06979](https://arxiv.org/abs/2105.06979)). → v0.5 *typically about twenty-five kilometres across* (typický průměr, ne univerzální) | ✏️ ✅ |
| S28 | láká to nazvat ji jedním obřím jádrem, ale není | drží ji gravitace, ne silná interakce, a stavba se mění s hloubkou (S29–S30) — požadavek uživatele z rozhodnutí o variantě A | ✅ |
| S29 | kůra je mřížka podivných jader bohatých na neutrony; hlouběji splývají do tvarů zvaných jaderné těstoviny | „body-centered cubic lattice… the composition of the nuclei becomes more neutron rich as a result of electron captures" (Chamel & Haensel 2008, [arXiv:0812.3955](https://arxiv.org/abs/0812.3955)); „meatballs… spaghetti… lasagna… known as the nuclear pasta", od ~0,1 n₀ (Lattimer & Prakash 2004) | ✅ |
| S30 | pod tím neutronová kapalina, ve středu to nikdo neví | „The outer core consists of a soup of nucleons, electrons and muons. The neutrons could form a ³P₂ superfluid… In the inner core exotic particles such as… hyperons… a transition to… deconfined quark matter" (Lattimer & Prakash 2004) | ✅ |
| S31 | drží ji tlak té hmoty: zčásti kvantový jev, zčásti odpudivá silná interakce na krátkou vzdálenost | Oppenheimer–Volkoff: hvězda jen z neutronového degeneračního tlaku se zhroutí nad **0,7 M☉** — „This underscores the critical role that strong interactions play" (Ruiz Lopez a kol. 2022, [arXiv:2209.14877](https://arxiv.org/abs/2209.14877)); „repulsive short-range forces between nucleons" (Janka 2012) | ✅ |
| S32 | nad určitou hmotností žádný známý tlak kolaps nezastaví, vznikne černá díra | M_TOV mezi 2,01 a ~2,16 (+0,17) M☉ (Rezzolla a kol. 2018, [arXiv:1711.00314](https://arxiv.org/abs/1711.00314)); nejtěžší spolehlivě změřená 2,08 ± 0,07 M☉ (Fonseca a kol. 2021, [arXiv:2104.00880](https://arxiv.org/abs/2104.00880)). Přesná mez závisí na stavové rovnici, proto „a certain mass" a „no known pressure" | ✅ |
| S33 | shrnutí: gravitace stlačí hmotu do stavu bez atomů a na hustotu jádra | shrnuje S23–S31 | ✅ |

## S34–S37 Lžička na Zemi

| | tvrzení | ověření | |
|---|---|---|---|
| S34 | „Suppose you could scoop out…" | myšlenkový pokus, rámec pro S35–S37 | 💬 |
| S35–S36 | (po poslechu draftu 2026-10-30) hmotu nedrží pohromadě silná interakce, samotné neutrony k sobě „nelnou“, stlačenou ji drží gravitace celé hvězdy; mimo hvězdu převládne její vlastní tlak a násilně se dekomprimuje | Dineutron ani čistě neutronové jádro vázané nejsou (energie na neutron v čisté neutronové hmotě je kladná při všech hustotách, např. Gandolfi a kol. 2015, Annu. Rev. Nucl. Part. Sci. 65, 303); hvězdu drží gravitace proti degeneračnímu tlaku a krátkodosahovému odpuzování (S31). Tlak hmoty při n₀ je řádově 10³² Pa; nic na Zemi ho nevyváží. Dekompresi chladné hmoty neutronové hvězdy rozebírají Lattimer, Mackie, Ravenhall & Schramm 1977, ApJ 213, 225 ([NTRS 19770045172](https://ntrs.nasa.gov/citations/19770045172)) | ✅ |
| S37 | při dekompresi se musí přeměnit na běžnou hmotu; už rozdíl energie neutronu a atomu vodíku dává víc než asteroid, který vyhubil dinosaury | **rozepsáno ve třech vrstvách níž** | ✅ |

### S37 ve třech vrstvách (požadavek zpětné vazby 0.3 a 0.4)

**1. Výpočet.** m_n − m(¹H) = 939,565 42 − 938,783 08 = **0,782 35 MeV**
(totéž jako m_n − m_p − m_e, vazba elektronu 13,6 eV je zanedbatelná).
Počet baryonů v lžičce = hmotnost / u:

| lžička | baryonů | × 0,782 MeV |
|---|---|---|
| 1,35 mld. t (saturační hustota) | 8,1×10³⁸ | **1,0×10²⁶ J** |
| 1,9 mld. t (průměr hvězdy 1,4 M☉ / 12 km) | 1,1×10³⁹ | 1,4×10²⁶ J |

Chicxulub: recenzovaný přehled Morgan, Bralower, Brugger a kol. 2022
(*Nature Reviews Earth & Environment* 3, 338): „an impact energy of about
10²³ joules" ([PSU](https://pure.psu.edu/en/publications/the-chicxulub-impact-and-its-environmental-consequences/)).
→ **asi 1 000×**. Nejvyšší nalezený odhad je preprint Durand-Manterola &
Cordero-Tercero 2014, 1,3×10²⁴–5,8×10²⁵ J ([arXiv:1403.6391](https://arxiv.org/abs/1403.6391),
v časopise jsme ho nenašli; počítá s kometou až 80 km). I proti jeho horní
mezi vychází 1,7–2,4×. *(V `notes.md` u v0.3 je tenhle rozsah omylem
o dva řády nižší, 1,3–5,8×10²³ J; závěr to neobrací.)*

**2. Fyzikální předpoklad: proč je to DOLNÍ mez celého procesu.**
Uvolněná energie = (energie na baryon na začátku − na konci) × počet baryonů.

- **Konec:** každý stabilní i dlouhožijící nuklid má hmotnost na nukleon
  **nižší** než ¹H, protože vodík jako jediný nemá jadernou vazbu (AME2020:
  ²H 1,007 051 u, ³He 1,005 343 u, ⁴He 1,000 651 u, ⁵⁶Fe 0,998 838 u,
  ²³⁸U 1,000 213 u; ¹H 1,007 825 u). Volný neutron stabilní není (rozpadá
  se za ~15 min). Jakýkoli konečný stav tedy dá rozdíl **≥ 0,782 MeV** na
  baryon. Skutečně vzniknou těžká jádra r-procesu, tedy rozdíl blíž
  **8–9 MeV** (⁵⁶Fe: 9,15 MeV).
- **Začátek:** hmota v beta-rovnováze při saturační hustotě má energii na
  baryon **o 13,2–16,9 MeV nad klidovou hmotností neutronu** (Hebeler,
  Lattimer, Pethick & Schwenk 2013, ApJ 773, 11, tab. 5, při n/n₀ = 1,037;
  ověřeno, že tabulka počítá od 939,6 MeV). Čistá neutronová hmota při n₀:
  14,1–21,0 MeV na částici (Tews a kol. 2013, [arXiv:1206.0025](https://arxiv.org/abs/1206.0025)).
  Volný neutron je tedy **spodní hranice** výchozího stavu. Platí to pro
  hmotu o jaderné hustotě, kterou S27 popisuje. **Neplatí to pro kůru**
  (vnější kůra jsou jádra železa a je pod m_n), ale lžička ve scénáři
  z kůry není.
- **„Would have to turn into ordinary matter":** Lattimer a kol. 1977:
  „neutrons can be captured only after beta decay increases the atomic
  numbers of nuclei… no free neutrons can escape… neutron-star ejecta can
  produce heavy neutron-rich nuclei". Moderní kilonovy: „Neutron-rich
  matter… undergo rapid neutron capture (r-process) nucleosynthesis as it
  decompresses" a rozpad volných neutronů ve vnějších vrstvách výronu
  (Metzger, [arXiv:1910.01617](https://arxiv.org/abs/1910.01617)).
  Neutronově bohatá jádra se pak beta rozpady dostanou ke stabilitě.

Rozdíl m_n − m_H je tedy dolní mez energetické bilance **celého** procesu,
ne odhad. Skutečná bilance je ~(13 + 8) ≈ **20 MeV na baryon**, tedy asi
25× víc. Podmínka uživatele ze zpětné vazby 0.4 je splněná.

**3. Omezení.**

- Je to **celková** energetická bilance z rozdílu hmotností, ne simulace
  dekomprese a ne energie okamžitého výbuchu. Část se uvolní až rozpady
  (sekundy až roky). Věta mluví o rozdílu energie, který „adds up to",
  takže výbuch netvrdí.
- **Antineutrina:** u rozpadu volného neutronu odnesou v průměru **61 %**
  z 0,782 MeV (spočteno z povoleného beta spektra: elektron v průměru
  0,303 MeV, antineutrino 0,480 MeV). Na Zemi by v nejhorším případě
  (konec jako vodík) zůstalo ~4×10²⁵ J, tedy **~400×** odhad 10²³ J.
  Pod horní mezí preprintu by to bylo; v realistické bilanci (~20 MeV
  na baryon) ne.
- „As the matter decompressed" je časově volné: přeměna začne při
  dekompresi a beta rozpady ji dokončí po ní.

## S38–S43 GW170817

| | tvrzení | ověření | |
|---|---|---|---|
| S38 | v roce 2017 jsme viděli „something like it" | výron ze srážky je dekomprimovaná hmota neutronových hvězd (Metzger, výš); „something like it", protože srážka není lžička | ✅ |
| S39 | dvě neutronové hvězdy asi 130 milionů světelných let daleko se spirálovitě přiblížily a srazily | 17. 8. 2017, NGC 4993, 40 ± 8 Mpc (Abbott a kol. 2017, ApJL 848, L12, [arXiv:1710.05833](https://arxiv.org/abs/1710.05833)); „about 130 million light-years from Earth" ([LIGO](https://www.ligo.caltech.edu/page/press-release-gw170817)) | ✅ |
| S40 | srážku zachytily detektory gravitačních vln, pak se podívaly dalekohledy po celém světě | Advanced LIGO a Virgo; GRB 170817A o 1,74 ± 0,05 s později ([arXiv:1710.05834](https://arxiv.org/abs/1710.05834)); „about 70 observatories on the ground and in space" (LIGO). Část z nich byla ve vesmíru, „all over the world" je volné | ✅ 💬 |
| S41 | viděly trosky rozpínající se do prostoru a zářící | kilonova AT 2017gfo: „material that is left over from the neutron star collision, which glows with light, is blown… far out into space" (LIGO) | ✅ |
| S42 | při dekompresi neutronově bohaté hmoty vznikly těžké atomy; identifikováno stroncium, modely naznačují zlato a platinu | stroncium: Watson a kol. 2019, Nature 574, 497 ([arXiv:1910.10510](https://arxiv.org/abs/1910.10510)). **Identifikace je od roku 2022 sporná:** tutéž čáru může dát helium 1083 nm (Perego a kol. 2022, [arXiv:2009.08988](https://arxiv.org/abs/2009.08988); Tarumi a kol. 2023, [arXiv:2302.13061](https://arxiv.org/abs/2302.13061)). → v0.5 *Astronomers identified what is most likely strontium*. Zlato a platina: složka těžkých prvků r-procesu (A > 140) odvozená z opacity (Kasen a kol. 2017, [arXiv:1710.05463](https://arxiv.org/abs/1710.05463)); „models suggest" drží | ✏️ ✅ |
| S43 | část zlata na Zemi možná vznikla při takových srážkách | podíl srážek je sporný, kolapsary podle Siegel a kol. 2019 („may supply more than 80 per cent of the r-process content", [arXiv:1810.00098](https://arxiv.org/abs/1810.00098)). „Some… may" drží obojí | ✅ |

## S44–S55 Proč to vůbec něco váží

| | tvrzení | ověření | |
|---|---|---|---|
| S46 | každý neutron a proton je ze tří menších částic, kvarků | tři valenční kvarky; moře kvarkových párů a gluony scénář řeší v S50. Zjednodušení | ✅ 💬 |
| S47–S48 | kvarky dají zhruba jedno procento protonu | PDG 2024: m_u = 2,16 ± 0,07 MeV, m_d = 4,70 ± 0,07 MeV (MS-bar, 2 GeV) ([PDG](https://pdg.lbl.gov/2024/tables/rpp2024-sum-quarks.pdf)); (2·2,16 + 4,70) / 938,27 = **0,96 %** (neutron 1,23 %). Pozor: příspěvek členů s hmotností kvarků k hmotnosti protonu (sigma člen, včetně s-kvarku) je ~9 % (Yang a kol. 2018, [arXiv:1808.08677](https://arxiv.org/abs/1808.08677)); scénář mluví o klidové hmotnosti kvarků, kde 1 % platí | ✅ |
| S49–S50 | zbytek je energie kvarků pohybujících se téměř rychlostí světla a gluonových polí | Yang a kol. 2018: „quark energy and glue field energy contribute 33(4)(4)% and 37(5)(4)%", stopová anomálie 23 % | ✅ |
| S51 | Einstein ukázal, že energie má hmotnost | Einstein 1905, *Ist die Trägheit eines Körpers von seinem Energieinhalt abhängig?* | ✅ |
| S52 | Higgsovo pole dává hmotnost kvarkům, ta je ale jen ~1 % protonu | Yukawovy vazby na Higgsovo pole dávají klidovou hmotnost kvarkům (a leptonům) | ✅ |
| S53 | hmota v těle je hmotná hlavně kvůli energii polí, která ji drží pohromadě | věta uživatele; plyne z S48–S50 (nukleony jsou >99,9 % hmoty atomu, S10) | ✅ |
| S54 | totéž u lžičky: miliardy tun a skoro všechno je energie silné interakce | nukleony jako výš; navíc ~13–17 MeV/baryon jaderné energie (S37), taky silná interakce | ✅ |
| S55 | na superpočítačích lze hmotnost protonu spočítat z QCD a souhlasí s experimentem | Dürr a kol. 2008, Science 322, 1224: „a full ab-initio calculation of the masses of protons, neutrons and other light hadrons, using lattice quantum chromodynamics… Our results completely agree with experimental observations" ([arXiv:0906.3599](https://arxiv.org/abs/0906.3599)) | ✅ |

## S56–S68 Čísla, která teorie nepředpovídá

| | tvrzení | ověření | |
|---|---|---|---|
| S56–S57 | výpočet začíná od čísel, která teorie sama nepředpovídá: síla silné interakce, hmotnosti kvarků; ty se měří a dosazují ručně | jsou to volné parametry QCD. V praxi mřížky se nastavují přes naměřené hmotnosti hadronů (u Dürra pion, kaon a Ξ) — tedy právě „measured and put in" | ✅ |
| S58 | Standardní model má kolem dvaceti takových čísel | „In the absence of neutrino masses… 19 parameters, and the inclusion of neutrinos raises the number to 26" (Adams 2019, Physics Reports, [arXiv:1902.03928](https://arxiv.org/abs/1902.03928)) | ✅ |
| S59 | rychlost světla přesně 299 792 458 m/s | přesná hodnota z definice | ✅ |
| S60 | od roku 1983 je metr definován pomocí rychlosti světla | 17. CGPM 1983, rezoluce 1: „The metre is the length of the path travelled by light in vacuum during a time interval of 1/299 792 458 of a second" ([BIPM](https://www.bipm.org/en/committees/cg/cgpm/17-1983/resolution-1)). Od 2019 se metr definuje stanovením číselné hodnoty c; hodnota je pořád přesná | ✅ |
| S61 | ve stopách se číslo úplně změní | 983 571 056 ft/s. „The speed itself matters enormously" (recenze 0.1) | ✅ |
| S62–S63 | některá čísla nemají jednotky; nejslavnější je konstanta jemné struktury, určuje, jak silně elektrické náboje interagují se světlem | α je bezrozměrná vazbová konstanta elektromagnetické interakce (náboje s fotony) | ✅ |
| S64 | pomáhá určovat velikost atomů („all that empty space from the beginning“, odkaz na S08–S11) a sílu chemických vazeb | Bohrův poloměr = ħ/(m_e c α), tedy velikost atomu ∝ 1/α (spolu s m_e, proto „helps set“); energie hladin ∝ α² m_e c², tedy i vazebné energie. Změněno po poslechu draftu 2026-10-30: uživatel nepochopil, co má α společného s tématem | ✅ |
| S65 | asi jedna lomeno 137, v každých jednotkách stejně | CODATA 2022: α⁻¹ = 137,035 999 177(21) ([NIST](https://physics.nist.gov/cgi-bin/cuu/Value?alphinv)). Při vysokých energiích „běží" (~1/128 u hmotnosti Z) — 1/137 je nízkoenergetická hodnota, jak ji zná každý | ✅ 💬 |
| S66 | měříme ji s mimořádnou přesností, ale nevíme, proč má tuhle hodnotu | relativní nejistota 1,6×10⁻¹⁰; měření přes Rb (Morel a kol. 2020, Nature 588, 61, 81 ppt) se od Cs liší o víc než 5σ — přesnost je mimořádná i tak | ✅ |
| S67 | některé výpočty naznačují, že změna určitých konstant by mohla vést k vesmíru bez stabilních hvězd nebo bez složité chemie | Tegmark 1998: „the fact that α, β ≪ 1 is crucial for chemistry as we know it"; „it is doubtful if stable, long-lived stars could exist at all" ([gr-qc/9704009](https://arxiv.org/abs/gr-qc/9704009)). Protiváha: Adams 2019 — „Stable hydrogen burning stars can exist over a wide range of parameter space". Proto „some calculations", „certain constants", „could"; **nepřidávat „slightly" ani „tiny"** | ✅ |
| S68 | štěstí, hlubší teorie, nebo jeden z mnoha vesmírů? Nikdo neví | otevřená otázka (073 S25–S30) | 💬 |

## S69–S74 Závěr

| | tvrzení | ověření | |
|---|---|---|---|
| S69–S70 | rekapitulace | shrnuje S01–S50 | ✅ |
| S71 | na dně je hrstka čísel, která teorie berou jako daná | 19–26 (S58); „handful" je volnější než „around twenty" | 💬 |
| S72–S74 | i hlubší teorie otevře otázku „proč tahle"; otázka do komentářů | úvaha; odvození 1/137 z něčeho hlubšího je otevřený problém | 💬 |

## Rozhodnutí po fact checku (uživatel, 2026-10-29)

- S42 a S27 upraveny (v0.5), viz tabulky výš.
- S24 „start capturing" zůstává: přiměřené zjednodušení děje během kolapsu.
- **S37 zůstává ve znění 0.4**, nezměkčuje se. Uživatel bere zpět výhradu,
  že m_n − m_H není dolní mez: předpoklady (výchozí stav z jádra hvězdy,
  ne z kůry; konečný stav stabilní nebo dlouhožijící hmota) jsou vymezené.
  Pro odpovědi v komentářích: věta mluví o celkové bilanci, ničivý účinek
  na Zemi je menší o energii antineutrin (S37, vrstva 3).
- Dál scénář neměnit, další kolo přepisování ne.
- **Obraz S37 ukazuje ≈ 1,000×** (storyboard, rozhodl uživatel), vztažené
  k referenčnímu odhadu ~10²³ J, a to i v obraze. Proti horní mezi preprintu
  by platilo jen „more than“ (1,7–2,4×).
