# 160 — fact check scénáře v0.2 (2026-11-17)

Nad `script 0.2.md` (88 scén). Navazuje na `factcheck-zaklad.md`
(rešerše před scénářem); co je tam doložené, se tu jen odkazuje.
Zahrnuje deset bodů z `zpetna vazba 0.2.txt` (značeno **ZV n**).

Značky: ✅ sedí · ⚠️ sedí, ale formulace je volnější než zdroj · ❌ nesedí ·
**P** primární zdroj (NASA, JPL, ESA, CNSA, odborný článek) · **S**
sekundární · **M** spočítáno.

**Scénář se v tomhle kroku NEMĚNIL** (uživatel: *„nejdřív ověřit, teprve
potom případně upravovat“*). Navržená znění jsou v posledním sloupci
a souhrnně na konci.

## Úvod (S01–S10)

| scéna | tvrzení | ověření | závěr |
|---|---|---|---|
| S01 | *This is a photograph from Mars. Ten small titanium tubes, lying on the ground* | Depo Three Forks, 10 trubiček (12/2022–1/2023) — zaklad §1. Snímky: **PIA25738** je fotomontáž deseti záběrů WATSON (každá trubička zvlášť), **PIA25736** jeden pohled Mastcam-Z na celé depo s 10 trubičkami (31. 1. 2023). Trubičky jsou z titanu (JPL *Martian Roundtrip*) — P | ⚠️ **„a photograph“ platí jen pro PIA25736.** Při storyboardu buď PIA25736, nebo u montáže *„These are photographs from Mars.“* |
| S02 | jádra horniny, vrtaná a zapečetěná Perseverance | P (JPL) | ✅ |
| S03 | *one of the tubes still on the rover* — Sapphire Canyon | Vzorek 25, jádro z Cheyava Falls, zapečetěn 21. 7. 2024 (NASA *Mars Rock Samples*, *Meet the Mars Samples: Sapphire Canyon*) — P. Depo vzniklo 12/2022–1/2023, tedy **před** odběrem, takže vzorek v depu být nemůže — M | ✅ |
| S03 | *tiny dark spots, like the coat of a leopard* | „leopard spots“ — NASA, Hurowitz et al. 2025 — zaklad §2 | ✅ |
| S03b | dva minerály, na Zemi často vznikají tam, kde mikrobi rozkládají organickou hmotu | vivianit a greigit; na Zemi spojené s mikrobiální redukcí a rozkladem organiky — zaklad §2 | ✅ |
| S04 | *In 2025… a potential biosignature. Not proof of life.* | Nature, 10. 9. 2025 — zaklad §2 | ✅ |
| S04 **ZV 1** | *But the rover's instruments can't tell us.* | Rover minerály **určil** (PIXL, SHERLOC); co neumí, je rozhodnout, jestli vznikly biologicky, nebo třeba ohřevem — S (NASA citace Hurowitz) | ⚠️ zní, jako by rover nezjistil nic. **Návrh:** *„The rover can tell what they're made of. Not how they formed.“* |
| S06 | NASA měla plán; méně než půl kila; odhad 11 mld. $ | strop 30 × 15 g = 450 g (M); 11 mld. — NASA 4/2024 (P) | ✅ |
| S07 | přes 20 mil. $ za gram | 11 mld. / 450 g = 24 mil. (M) | ✅ |
| S08 | *in January 2026, the original programme lost its funding* | 6. 1. 2026, Kongres FY2026: *does not support the existing MSR program*; 110 mil. $ na Mars Future Missions — S (Register, Planetary Society, SpacePolicyOnline 12. 11. 2026) | ✅ |
| S09 | Apollo 11 (1969), asi 22 kg | **21,5 kg, 58 vzorků** (NASA NTRS 20090011852 — P); Smithsonian 21,8 kg | ✅ „about twenty-two“ |
| S09b | 2024 čínský robot přivezl vzorky z odvrácené strany | Chang'e 6, **1 935,3 g**, přistání pouzdra 25. 6. 2024 — P (CNSA přes CAS, Planetary Society) | ✅ |
| S10 | *not half a kilogram from Mars* | | ✅ (rétorické, sedí na 450 g) |

## Proč je Mars těžší (S11–S21)

| scéna | tvrzení | ověření | závěr |
|---|---|---|---|
| S11 | gravitace Marsu víc než dvojnásobná | 3,71 / 1,62 = **2,3×** (M) | ✅ |
| S12 | úniková rychlost 2,4 vs. asi 5 km/s | 2,38 vs. 5,03 km/s (M, P konstanty) | ✅ |
| S13 | *It's much worse.* | viz S15–S16 | ✅ |
| S14 | callback na video o orbitě (125) | | ✅ |
| S15 | palivo neroste úměrně rychlosti, ale exponenciálně | raketová rovnice | ✅ |
| S16 **ZV 2** | z Měsíce ~polovina paliva, z Marsu ~tři čtvrtiny, stejný motor | Isp 290 s: Δv ~1,85 km/s → 48 %, Δv ~4,1 km/s → 76 % (M). Kontrola z reality: výstupní stupeň LM měl 2 353 kg paliva z ~4 700 kg, tedy **50 %** — Pam, sedí | ⚠️ čísla sedí, ale jde o **příklad, ne vlastnost všech raket**. **Návrh:** začít *„In a simple example,“* |
| S17 | co startuje z Marsu, musí na Mars přistát | | ✅ |
| S17b | Měsíc bez vzduchu; Mars dost atmosféry na ohřev a málo na to, aby padáky stačily | tlak na povrchu ~0,6 kPa, ~0,6 % pozemského; každé přistání na Marsu kombinovalo padák s motory, airbagy nebo sky crane — P (NASA EDL) | ✅ |
| S18 | lander asi 2 300 kg | **2 275 kg**, *„would be the heaviest spacecraft ever to land on the Red Planet“* — P (JPL 2023, nohy landeru) | ✅ s *„would have been“* |
| S18 | **Nearly twice Perseverance** | Allen Chen (JPL): *„almost twice the mass of what we put down with the Perseverance rover“* — jenže to řekl o landeru *„a little over two metric tons“*. Perseverance má **1 025 kg** (P), takže 2 275 / 1 025 = **2,2×** (M) | ❌ s číslem 2 300 ve **stejné** scéně nesedí. **Návrh:** *„More than twice Perseverance.“* |
| S19 | noci minus osmdesát stupňů | MEDA, Jezero: minimum **−83 °C** (soly 43–44, jaro 2021); v zimě níž — S (Universe Today podle JPL), Nature Geoscience 2022 | ✅ |
| S19b | nejlepší startovní okna zhruba každých 26 měsíců | synodická perioda 780 dní = 25,6 měsíce (M) | ✅ |
| S20 | signál ze Země 3 až 22 minut | 54,6 a 401 mil. km / c (M) | ✅ |
| S21 | z povrchu jiné planety ještě žádná raketa nestartovala; Měsíc není planeta | | ✅ |

## Meteority (S22–S33b)

| scéna | tvrzení | ověření | závěr |
|---|---|---|---|
| S24 | 2025, největší kus Marsu na Zemi, aukce v New Yorku, 24,5 kg | NWA 16788, Sotheby's New York, 16. 7. 2025 — S (Space.com, Sky at Night) | ✅ |
| S25 | 5,3 mil. $, asi 200 $ za gram | 4,3 mil. $ v kladívku, 5,3 mil. s poplatky; 5,3 mil. / 24 500 g = **216 $/g** (M) | ✅ |
| S26 | stotisíckrát levněji | 24 mil. / 216 = **111 000×**; při 22 mil. $/g 102 000× (M) | ✅ |
| S27 | *a meteorite has no address* | | ✅ (obraz, ne tvrzení) |
| S28 | vymrštěn nárazem, miliony let ve vesmíru, průlet atmosférou | ALH84001: vymrštěn před 16 mil. let (expoziční stáří) — P (NASA 1996) | ✅ |
| S29 | ležel v poušti; nevíme odkud, co s ním udělal náraz a co přidala Země | | ✅ |
| S29b | 1996, možné zkamenělé mikroby v marťanském meteoritu z Antarktidy | McKay et al., *Science*, oznámení NASA 7. 8. 1996 — P | ✅ |
| S29c | spor trval desetiletí | stále otevřené, převážně odmítnuto — S | ✅ |
| S29c **ZV 3** | *thirteen thousand years on Earth* | **NASA 7. 8. 1996:** *„It encountered Earth's atmosphere 13,000 years ago and fell in Antarctica as a meteorite.“* — **P** (NSSDC). A že Země do kamene něco přidala, je **doložené, ne domněnka**: Jull et al., *Science* 1998 — větší část organického uhlíku v ALH84001 je **pozemská kontaminace** — P | ✅ číslo je **potvrzené primárně**. Hlavní spor byl ale o výklad struktur, ne o kontaminaci. **Návrh**, aby to neznělo jako vysvětlení celého sporu: *„And it had spent thirteen thousand years in Antarctic ice — long enough for Earth to leave traces of its own.“* |
| S30 | u vzorků z Perseverance známe vrstvu | každý vzorek má zdokumentovanou polohu a kontext — P (NASA sample table) | ✅ |
| S31 | přístroje se musely vejít na robota velikosti auta a přežít start | | ✅ |
| S32 | na Zemi jakákoli laboratoř, i přístroje, které ještě nejsou | | ✅ (logika, ne fakt) |
| S33 | vzorky z Apolla se studují přes 50 let | ANGSA — P | ✅ |
| S33b | 2022 NASA otevřela trubičku, kterou astronauti uzavřeli na Měsíci v roce 1972 a nechali pro lepší přístroje | **73001**, Apollo 17, uzavřen ve vakuové nádobě **na Měsíci**, otevřen **v březnu 2022** (NASA: 23. 3.), program ANGSA — P (NASA) | ✅ |

## Plán NASA (S34–S49)

| scéna | tvrzení | ověření | závěr |
|---|---|---|---|
| S35 | rover přiveze trubičky k landeru; raketa je vynese v kontejneru velikosti basketbalového míče | rover (Perseverance, dřív Sample Fetch Rover) — P; OS „basketball-sized“ — P | ✅ |
| S36 | raketa několik set kilo; náklad méně než půl kila horniny | MAV 400 → 525 → 450 → 350 kg — S (Wikipedia); hornina ≤ 450 g (M) | ⚠️ náklad je kontejner s trubičkami, ne holá hornina; rétoricky obhajitelné. **Volitelně:** *„The rock inside, less than half a kilogram.“* |
| S37 | jen na oběžnou dráhu Marsu | P | ✅ |
| S38 | druhou sondu měla postavit ESA, najít kontejner, chytit ho a odvézt | Earth Return Orbiter, ESA (Airbus) — P | ✅ |
| S40 **ZV 4** | přímý návrat = mnohem větší raketa; *all of it would have to land first* | logika raketové rovnice | ⚠️ *all of it* je nejasné. **Návrh:** *„…and head towards Earth. And that whole rocket, fuel and all, would have to land on Mars first.“* |
| S41 | Apollo nechalo zpáteční motor na oběžné dráze Měsíce a dolů poslalo jen malý modul | lunar orbit rendezvous; SPS motor zůstal na CSM — P (NASA) | ✅ |
| S42 **ZV 5** | nejde o chytání kulky; obě sondy krouží spolu a vůči sobě se skoro nehýbou | NASA (NTRS 2022): ERO sesouhlasí dráhu kontejneru s osou záchytného kužele a přiblíží se *„with a large enough closing velocity to overtake it“*; záchyt trvá **sekundy**. **Konkrétní číslo vzájemné rychlosti jsem v dostupných zdrojích NENAŠEL.** Oběžná rychlost je ~3,4 km/s, setkání se dorovnává na dráze → vzájemná rychlost je o řády menší (M, kvalitativně). Populární *„catch… while traveling four miles per second“* (factsaday) je ten mýtus | ✅ kvalitativně, **číslo do scénáře nedávat** |
| S44 | kontejner neřídí; orbiter ho musí najít sám | kontejner je pasivní a *„fully uncooperative“*, velmi slabý; čistě optická navigace kamerami NAC a WAC (GLEX 2020); detekce **až na 3 000 km**, magnituda 12,6 (Sodern, ESA 2022) — P | ✅ |
| S45 | přiblížit a chytit bez možnosti zásahu ze Země | autonomní detekce (Capture Sensor Suite, Aerospace 2024) — P; zpoždění signálu S20 | ✅ |
| S46 | lander, rover, raketa, orbiter, záchytný systém; vše musí fungovat napoprvé | | ✅ (vrtulníky jako záloha nejsou, ale tvrzení to nevyvrací) |
| S48 **ZV 6** | odhady rostly: ~4 mld. (2020), pak 7, pak 11 a návrat nejdřív 2040 | IRB-1 2020: 3,8–4,4 mld. (S); NASA 4/2024: dřívější 7 mld. → 11 mld., *no sooner than 2040* (P) | ⚠️ čísla sedí, ale **jsou z různých revizí a variant plánu**, ne tři přecenění téhož projektu. **Návrh:** *„So the estimates kept climbing, review after review.“* |
| S49 | levnější varianty se navrhly, žádná se nefinancovala | 1/2025: 5,8–7,7 mld. — S (CBS); FY2026 — S | ✅ |

## Starship a MOXIE (S50–S63)

| scéna | tvrzení | ověření | závěr |
|---|---|---|---|
| S51 | 2024 NASA oslovila firmy, sedm placených studií, jedna od SpaceX | 6/2024, 7 studií po ≤ 1,5 mil. $ ze 48 nabídek — S (TechCrunch, SpaceNews) | ✅ |
| S52 | název *Enabling Mars Sample Return With Starship* | S (SpaceNews) | ✅ |
| S53 | SpaceX zveřejnila málo | S | ✅ |
| S54 | *Imagine a ship…* | výslovná hypotéza | ✅ |
| S56 | vzduch hlavně CO₂; s vodíkem z ledu jde vyrobit metan | atmosféra ~95 % CO₂ — P; Sabatier — S | ✅ |
| S56b | kyslík jde získat z CO₂ | MOXIE (pevný oxid, elektrolýza) — P | ✅ |
| S57 | MOXIE vyrobil kyslík na Marsu | P (NASA) | ✅ |
| S58 | dva roky, 16 běhů, 122 g, malý pes za 10 hodin | 4/2021 – 8/2023 (2,3 roku), 16 běhů, 122 g, citace NASA — S (ScienceAlert podle NASA) | ✅ |
| S59 | Starship s asi 1 200 t pohonných látek, *the figure usually quoted* | V1/V2 ~1 200 t; novější verze 1 500–1 600 t — S, neoficiální | ✅ (se slovy „usually quoted“) |
| S60 | většina je kyslík, přes 900 t | methalox O/F ≈ 3,6 → 1 200 × 3,6 / 4,6 = **939 t** (M) | ✅ |
| S61 **ZV 7** | přes sedm milionů krát víc, než vyrobil MOXIE | **Srovnávají se dvě stejné veličiny:** hmotnost kyslíku ve 1 200 t pohonných látek (939 t) a **celková** hmotnost kyslíku z MOXIE (122 g). 939 000 kg / 0,122 kg = **7,7 milionu** (M). U verze s 1 600 t vyjde 10 milionů, takže „more than seven million“ je spodní mez a drží pro všechny verze | ✅ |
| S62–S63 | MOXIE nebyl palivo pro nic; ukázal, že chemie funguje; továrnu nikdo nepostavil | NASA: demonstrace technologie — P | ✅ |

## Planetární ochrana (S64–S72)

| scéna | tvrzení | ověření | závěr |
|---|---|---|---|
| S66 | vědci nečekají v trubičkách nic živého, ale nikdo nemůže dokázat opak | proto kategorie V *restricted* — P (viz S67) | ✅ |
| S67 | pravidla jsou přísná: nic z Marsu ven mimo uzavřenou nádobu, nic ze Země dovnitř | **COSPAR / NASA kategorie V, Restricted Earth Return** — P (NTRS 20220003049, 20240001902). Přijímací laboratoř musí mít ochranu na úrovni **BSL-4** a zároveň chránit vzorky před pozemskou kontaminací — P (NTRS 20210026720, MSAS) | ✅ |
| S68 **ZV 8** | *One fingerprint of Earth bacteria could ruin the very question* | Kontaminace je skutečné riziko pro výklad (proto „pristine environment“ — P), ale *ruin* a *one fingerprint* jsou absolutní | ⚠️ **Návrh:** *„Even a trace of Earth life could cloud the very question the mission was built to answer.“* |
| S69 **ZV 9** | v původním návrhu NASA neměla kapsle padák | Earth Entry System bez padáku, aby ubylo míst selhání — P (NASA, stránka o UTTR). Architektura z 12/2023, ne obecná varianta | ✅ |
| S70 | padák je další věc, která může selhat; kapsle spadne do měkké půdy v utažské poušti | Utah Test and Training Range, cílová plocha s měkkou jílovitou půdou — P | ✅ |
| S71 | asi 145 km/h; postaveno tak, aby kontejner náraz přežil | ~40 m/s = 144 km/h (90 mph); technická zpráva až 45 m/s; shozy z vrtulníku 10/2023 — P (NASA, NTRS 2024) | ✅ |
| S72 | pak do laboratoře s vysokou úrovní ochrany, prověřit dřív, než na vzorky sáhne kdokoli jiný | SRF provede *„safety assessments … prior to any reduction in biosafety level and distribution“* — P (NTRS 20210026720) | ✅ |

## Současnost a Čína (S73–S83)

| scéna | tvrzení | ověření | závěr |
|---|---|---|---|
| S74 **ZV 10** | v listopadu 2026 NASA začala znovu, s týmem, ne misí | PSRA: MEPAG 9. 11. 2026 (Tiffany Morgan), Town Hall 12. 11. 2026 (George Tahu) — S (SpacePolicyOnline 12. 11. 2026, Leonard David) | ✅ |
| S75 **ZV 10** | začíná v lednu; doporučení kolem konce 2027 | Tahu: tým začne **v lednu** a stráví na tom rok; *„high-level architecture approach and recommendations by the end of next year“*; MEPAG: „winter 2027–28“; tým jsou **tři roční stáže** stávajících zaměstnanců NASA — S | ✅ |
| S75 **ZV 10** | *There's no launch date, and no budget.* | Termín žádný — S. Rozpočet: Kongres dal **110 mil. $ na Mars Future Missions, ne výslovně na návrat vzorků**; financování navazující mise neoznámeno — S | ⚠️ *no budget* by šlo číst i tak, že tým nemá peníze. **Návrh:** *„There's no launch date, and no mission budget.“* |
| S76 | Čína staví vlastní misi, Tianwen-3 | P (CNSA 4/2026) | ✅ |
| S77 | dvě rakety kolem 2028; lander s malou výstupní raketou; orbiter nad ním; předání na oběžné dráze Marsu | 2× Long March 5 z Wenchangu; okno **12/2028–1/2029**; plán představen CNSA 24. 4. 2026 — S (cislunarspace, Space.com) | ✅ |
| S78 | NASA plánovala podobný řetěz, celá mise se stala moc složitou a drahou | IRB-2 2023, NASA 4/2024 — P | ✅ |
| S79 | Čína plánuje přivézt asi půl kila Marsu v roce 2031 | ~500 g, návrat ~2031 — S; *plans to* | ✅ |
| S80 | přistát, jezdit, vrtat, i létat | Ingenuity 2021–2024 — P | ✅ |
| S82–S83 | závěr, otázka | | ✅ (nejsou to tvrzení) |

## Souhrn

**Chyba jedna:** S18 *„Nearly twice Perseverance“* vedle *„about two
thousand three hundred kilograms“* — 2 275 / 1 025 = 2,2×. JPL citát
*almost twice* patřil starší hmotnosti („a little over two tonnes“).

**Navržené úpravy formulací** (všechny z bodů zpětné vazby, žádná nová
dramaturgie):

| scéna | dnes | návrh |
|---|---|---|
| S04 | But the rover's instruments can't tell us. | The rover can tell what they're made of. / Not how they formed. |
| S16 | A small rocket leaving the Moon… | In a simple example, / a small rocket leaving the Moon… |
| S18 | Nearly twice Perseverance. | More than twice Perseverance. |
| S29c | And the rock had already spent / thirteen thousand years on Earth. | And it had spent thirteen thousand years / in Antarctic ice, / long enough for Earth / to leave traces of its own. |
| S40 | And all of it would have to land first. | And that whole rocket, fuel and all, / would have to land on Mars first. |
| S48 | So the estimates kept climbing. | So the estimates kept climbing, / review after review. |
| S68 | One fingerprint of Earth bacteria / could ruin the very question | Even a trace of Earth life / could cloud the very question |
| S75 | There's no launch date, and no budget. | There's no launch date, / and no mission budget. |
| S01 (storyboard) | This is a photograph from Mars. | nechat a použít **PIA25736**, nebo u montáže PIA25738 *These are photographs from Mars.* |
| S36 (volitelné) | Its cargo, / less than half a kilogram of rock. | The rock inside, / less than half a kilogram. |

**Co zůstává bez čísla záměrně:** vzájemná rychlost při zachycení (S42).
Zdroje NASA popisují jen princip (dorovnat dráhu, přiblížit se pomalu,
záchyt trvá sekundy), konkrétní hodnota v dostupných pramenech není.

## Zdroje (nad rámec `factcheck-zaklad.md`)

- NASA 1996, *Meteorite yields evidence of primitive life on early Mars* — https://nssdc.gsfc.nasa.gov/planetary/text/mars_life.txt
- Jull et al. 1998, *Science*: pozemský původ části organiky v ALH84001 — https://experts.arizona.edu/en/publications/isotopic-evidence-for-a-terrestrial-source-of-organic-compounds-f/
- NASA, Apollo 73001 (2022) — https://www.nasa.gov/general/fifty-years-later-curators-unveil-one-of-last-sealed-apollo-samples
- NASA NTRS, lunární vzorky Apolla (21,5 kg Apollo 11) — https://ntrs.nasa.gov/citations/20090011852
- Chang'e 6, 1 935,3 g — https://english.cas.cn/newsroom/news--archives/2024/research-news/202409/t20240924_1130050.shtml
- JPL, nohy Sample Retrieval Landeru (2 275 kg) — https://www.jpl.nasa.gov/news/watch-nasa-engineers-put-a-mars-landers-legs-to-the-test/
- Space.com, citace A. Chena (*almost twice*) — https://www.space.com/landing-on-mars-challenges-entry-descent
- MEDA, teploty v Jezeru — https://universetoday.com/150836/hows-the-weather-in-jezero-crater-according-to-perseverance-cold
- NASA, *Mars Rock Samples* (vzorek 25) — https://science.nasa.gov/mission/mars-2020-perseverance/mars-rock-samples
- JPL PIA25738 (fotomontáž depa) — https://photojournal.jpl.nasa.gov/catalog/PIA25738
- NASA NTRS, Capture and Orient Module — https://ntrs.nasa.gov/citations/20220000770
- GLEX 2020, optická navigace setkání — https://iafastro.directory/iac/paper/id/55947/abstract-pdf/GLEX-2020,3,3,4,x55947.brief.pdf
- Sodern/ESA 2022, kamera NAC (3 000 km) — https://indico.esa.int/event/417/contributions/7673/attachments/4992/7770/NAC%20ERO%20presentation%20-%20Moving%20to%20Mars%202022_SODERN_v2.pdf
- MDPI Aerospace 2024, Capture Sensor Suite — https://mdpi.com/2226-4310/11/10/789
- NASA NTRS, kategorie V — https://ntrs.nasa.gov/citations/20220003049
- NASA NTRS, Sample Receiving Facility (BSL-4) — https://ntrs.nasa.gov/api/citations/20210026720/downloads/ADHarrington_MSAS_LPSC%202022.pdf
- SpacePolicyOnline 12. 11. 2026, PSRA — https://spacepolicyonline.com/news/nasa-looking-for-new-ways-to-return-perseverance-samples-from-mars/
- Tianwen-3, plán CNSA 4/2026 — https://cislunarspace.cn/en/space-news/2026/04/2026-04-24-tianwen-3-mars-sample-return/

## Dodatek 2026-11-17 (storyboard): S01 → v0.5

PIA25736 ukázal po stažení zřetelně jen jednu trubičku z deseti, takže
obraz neodpovídal hlasu (*„Ten small titanium tubes“*). Uživatel zvolil
montáž **PIA25738** (WATSON, deset záběrů, každá trubička zvlášť) a text
*„These are photographs from Mars.“* — tedy přesně variantu, kterou fact
check výš připravil. cs/de/es upraveny stejně. Scénář v0.5 (`script 0.5.md`).

## Dodatek 2026-11-17 (2. draft): scénář v0.6

- **S17b, S56:** *air* → *atmosphere* (připomínka uživatele: „vzduch“ zní jako
  dýchatelný, a ten nemá ani Mars). Věcně beze změny: atmosféra Marsu má u povrchu
  ~0,6 % tlaku zemské, ~95 % CO₂ — *thin* i *mostly carbon dioxide* platí.
- **S79b** *„Is another space race coming?“* — otázka, ne tvrzení; „another“
  odkazuje na závod o Měsíc v 60. letech. Nic k ověření.
