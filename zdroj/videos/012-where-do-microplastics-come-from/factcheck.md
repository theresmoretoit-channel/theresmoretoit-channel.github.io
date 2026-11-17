# Fact check — Where Do Microplastics Come From?

Stav k 30. 8. 2026, scénář v0.2. Ověřováno **z primárních zdrojů**;
kde primární zdroj není, je to u tvrzení výslovně napsáno.

---

## 1. Euro 7: co nařízení skutečně požaduje

**Primární zdroj:** nařízení Evropského parlamentu a Rady **(EU) 2024/1257**
ze dne 24. 4. 2024, Úř. věst. L, 8. 5. 2024.
ELI: http://data.europa.eu/eli/reg/2024/1257/oj
Staženo jako PDF (49 stran) a čteno v plném znění, ne z novinových článků.

### 1a. Limity na částice z brzd — ANO, s čísly

Tabulka 4 přílohy I, „Emission limits in mg/km per vehicle",
vozidla kategorie M1 a N1 (osobní auta a dodávky), platí **do 31. 12. 2029**:

| pohon | limit PM10 z brzd |
|---|---|
| PEV (čistě bateriové) | **3 mg/km** |
| OVC-HEV, NOVC-HEV, FCV/FCHV, ICEV (ostatní) | **7 mg/km** |

Pro N1 třídy III je to 5 a 11 mg/km. Tabulka 8: **od 1. 1. 2035**
platí **3 mg/km pro všechny pohony** a všechny kategorie.

✅ **Scénář to říká správně** — a rozdíl 3 versus 7 je zároveň doklad
pro tvrzení o rekuperaci (bod 4 níž): zákonodárce po elektromobilu chce
**méně než polovinu** brzdných částic, protože ví, že na to má.

### 1b. Limity na otěr pneumatik — NE, zatím NEEXISTUJÍ

Tohle je to místo, kde by se dalo snadno lhát.

**Tabulka 9 „Euro 7 tyre abrasion limits" nemá v nařízení JEDINÉ ČÍSLO.**

Ověřeno **měřením na vyrenderované stránce**, ne odečtem z textové vrstvy
(ta by mohla čísla minout, kdyby byla v grafice). Mřížka tabulky se našla
podle vodorovných a svislých linek a v každé buňce se spočítaly tmavé
pixely:

| | popis | C1 tyres | C2 tyres | C3 tyres |
|---|---|---|---|---|
| **záhlaví** | 2016 | 661 | 667 | 663 |
| Normal tyres | 1322 | **0** | **0** | **0** |
| Snow tyres | 1054 | **0** | **0** | **0** |
| Special use tyres | 1610 | **0** | **0** | **0** |

**Devět datových buněk, ve všech devíti nula tisku.** Text v tabulce je
výhradně v záhlaví (názvy tříd a názvy řádků).

> **Proto scénář neříká „leaves it empty".** Tabulka prázdná není — má
> hlavičku, a divák to na obraze vidí. Přesná a zároveň silnější
> formulace je **„prints the headings, leaves every single limit blank"**,
> a tu měření dokládá do posledního políčka. Opraveno ve v0.5 poté, co
> si uživatel všiml, že „většina buněk je prázdná" ≠ „tabulka je prázdná".

Článek 15 zmocňuje Komisi limity doplnit aktem v přenesené pravomoci
„**referring to the work of the UN WP.29**". Recitál 20 dává lhůty:
pokud UN WP.29 nepřijme jednotná ustanovení do **1. 7. 2026** (třída C1,
tedy osobní pneumatiky), **1. 4. 2028** (C2) nebo **1. 4. 2030** (C3),
Komise limity přijme sama.

✅ **Scénář v0.2 to říká výslovně** („the abrasion limits have not been
written yet"). Verze v0.1 tvrdila, že nařízení limity na otěr zavádí —
**to byla nepřesnost a je opravená**.

### 1c. Nařízení NEPŘEDEPISUJE technologii

Nikde v textu není zmíněn odsávací systém, filtr ani jiné konkrétní
řešení. Nařízení stanoví **limit a metodu měření** (brzdy podle
UN Global Technical Regulation No 24), cesta je na výrobci.

✅ **Scénář v0.2 to říká explicitně** („The rules set a limit. They do
not say how to meet it.") — přesně proto, aby video netvrdilo
„EU nařizuje vysavače".

### 1e. „For the first time" — ANO, ale jen o Evropě

**Prověřeno na výslovnou námitku uživatele.** Verze v0.3 říkala
*„For the first time **anywhere**"*. To se doložit nepodařilo:

| kde jsem hledal | co tam je |
|---|---|
| nařízení (EU) 2024/1257, plný text | „for the first time" je v něm **jednou**, a je to o **PN10 výfukových** částicích (recitál 14), ne o brzdách |
| tisková zpráva Rady EU 293/24 (12. 4. 2024) | mluví o zavedení limitů pro nevýfukové emise, **netvrdí prvenství ve světě** |
| oborový tisk | „world's first" tvrdí, ale je to sekundární zdroj |
| ostatní jurisdikce | Čína 7 se podobné požadavky teprve chystá; Kalifornie omezuje **měď v destičkách**, což je omezení materiálu, ne limit emise částic |

Prvenství ve světě tedy tvrdí jen sekundární zdroje a **absence
protipříkladu ve vyhledávání není důkaz**. CLAUDE.md to má jako past
(„sekundární zdroj neunese zobecnění").

✅ **Opraveno ve v0.4 na „For the first time, Europe puts a number…"**
Doložitelné je to bez potíží: v EU limity na částice z brzd dosud
neexistovaly, což je celý smysl recitálu 20. Rétoricky se tím
neztrácí skoro nic.

### 1d. Data účinnosti

Článek 21: pro nové typy vozidel M1 a N1 platí od **29. 11. 2026**,
pro nová vozidla těchto kategorií od **29. 11. 2027**.
Pro nové typy pneumatik třídy C1 od **1. 7. 2028**.

Scénář data neuvádí — bezpečné, nic se tím netvrdí.

---

## 2. „Pneumatiky jsou jeden z hlavních zdrojů mikroplastů"

**Primární zdroj: totéž nařízení, recitál 20**, doslova:

> „Emissions from tyres are estimated to be the largest source of
> microplastics released into the environment."

A dál tamtéž:

> „it is expected that by 2050 non-exhaust emissions will constitute
> up to 90 % of all particles emitted by road transport, because exhaust
> particles will diminish due to vehicle electrification"

a cíl Unie „**to reduce microplastics released into the environment
by 30 % by 2030**".

✅ Scénář je opatrnější než jeho zdroj (říká „one of the major sources",
zatímco nařízení říká „the largest source"). To je v pořádku — opatrnější
tvrzení se doložit dá vždycky.

⚠️ **Pozor na formulaci.** Nařízení mluví o mikroplastech **uvolňovaných
do prostředí** (primární emise), ne o veškerých mikroplastech v prostředí.
Rozpad odhozeného plastového odpadu je jiná kategorie a bývá odhadován
jako větší. Scénář proto nikde neříká „největší zdroj mikroplastů", jen
„jeden z hlavních".

---

## 3. Kolik pneumatika za život ztratí

**Zdroj:** Kole P. J., Löhr A. J., Van Belleghem F., Ragas A. (2017),
*Wear and Tear of Tyres: A Stealthy Source of Microplastics in the
Environment*, Int. J. Environ. Res. Public Health 14(10):1265,
doi:10.3390/ijerph14101265. Otevřený přístup, PMC5664766.

Shromážděné odhady úbytku hmotnosti pneumatiky za dobu používání:

| zdroj v článku | úbytek |
|---|---|
| UK Environment Agency | **10–20 %** hmotnosti |
| Norsko (výpočet) | 12,5 % |
| Švédský KemI | 17 % |
| italská studie | **1,5 kg** z desetikilové osobní pneumatiky za 50 000 km |

✅ Scénář v0.2 říká „**ten to twenty per cent of its weight**" a „on the
order of a kilogram per tyre, several kilograms for a full set".
Obojí sedí a je formulované jako rozpětí, ne jako jedno číslo.

Emisní faktor na kilometr se v literatuře pohybuje zhruba
**50–150 mg/km na vozidlo** (v jednotlivých experimentech 55–214 mg/km).
Scénář žádné číslo na kilometr netvrdí, takže se o tenhle rozptyl neopírá.

Per capita emise podle téhož článku: globální průměr **0,81 kg/rok**,
rozpětí 0,23 (Indie) až 4,7 kg/rok (USA). OECD uvádí 0,5–1,5 kg/rok.
Ve scénáři nepoužito — je to hezké číslo, ale těžko uchopitelné bez
vysvětlování, čí to je „hlava".

---

## 4. Elektromobily a rekuperace

**Zdroj (nepřímý, ale silný): nařízení samo** — limit 3 mg/km pro PEV
proti 7 mg/km pro ostatní, viz bod 1a. Zákonodárce po bateriovém vozidle
požaduje méně než polovinu, což bez rekuperace není splnitelné.

**Zdroj (přímý, sekundární):** měření udávají snížení brzdných částic
rekuperací v rozpětí zhruba **64–95 %** podle síly rekuperace a cyklu;
v městském provozu průměrně kolem **68 %**.
(Např. *Quantifying the change of brake wear particulate matter emissions
through powertrain electrification in passenger vehicles*, Environmental
Pollution 2023, PMID 37595730; a *Regenerative braking system effectively
reduces the formation of brake wear particles*, J. Hazard. Mater. 2024.)

✅ Scénář v0.2 říká „**well over half**", což leží bezpečně uvnitř
rozpětí všech uvedených měření, a hned vedle uvádí evropský limit
jako doklad.

⚠️ Scénář **netvrdí**, že elektromobily jsou celkově čistší co do
částic — právě naopak pokračuje tím, že s pneumatikami motor nepomůže.
Ta rovnováha je záměrná; jednostranné tvrzení oběma směry by bylo
doložitelně nepřesné.

---

## 5. „Tire wear particles" ≠ automaticky mikroplasty

**Zdroje:**
- OECD (2020), *Workshop on Microplastics from Tyre Wear: Knowledge,
  Mitigation Measures, and Policy Options*, souhrnná zpráva
  (workshop 18.–20. 5. 2020, podpořeno WBCSD).
- Kole et al. 2017, viz výš.
- Baensch-Baltruschat B. et al., *Tyre and road wear particles (TRWP) —
  A review*, Science of the Total Environment 733 (2020) 137823.

Doložená fakta:

1. **Částice není čistá pneumatika.** OECD doslova: „at the point of
   emission TRWP may be composed of tyre tread material and road wear
   components **in equal parts**", a podíl polymeru s časem dál klesá,
   jak se do částice zapékají další materiály.
   ✅ Scénář: „tyre rubber with road surface ground into it,
   in roughly equal parts."
2. **Běh je proto jiný název.** V literatuře se používá **TRWP**,
   tyre and road wear particles, ne „tyre microplastics".
3. **Směs materiálů.** Běhoun je směs přírodního kaučuku (produkt
   rostliny *Hevea brasiliensis*, tedy biopolymer) a syntetických
   kaučuků, plus silika, saze, oleje, sirné sloučeniny, oxid zinečnatý.
4. **Zařazení je věc definice.** OECD v poznámce pod čarou: „As tyre
   particles have a synthetic rubber component and are generally way
   smaller than 5 mm, they are **often classed as** microplastics in
   the literature." Kole et al. dodávají, že elastomerové částice se
   fyzikálně-chemicky liší od částečně krystalických termoplastů.
   ✅ Scénář: „whether they count as microplastics depends on the
   definition you use."
5. **Kole et al. varují**, že žádná z environmentálních studií doposud
   částice otěru pneumatik v prostředí skutečně neidentifikovala,
   natož kvantifikovala jejich podíl na mikroplastech.
   ✅ Scénář: „that difference is exactly what makes them so hard
   to study."

⚠️ **Tvar částice** (doutníkový, 70–100 µm, hustota 1,8) je doložený
a **kreslí ho S15**.

**Velikost proti lidskému vlasu — pozor na intuici.** Lidský vlas má
v průměru zhruba **70 µm**, tedy skoro totéž co typická částice otěru;
nejsou to řády vedle sebe. Mez rozlišení pouhým okem je kolem
**50–100 µm**, takže typická částice leží přesně na ní. Hluboko pod ní
je až jemný podíl (PM10, tedy pod 10 µm) — a ten nese větu „so small
that you can't see them at all". Diagramy S10, S63 a S71 to takhle
kreslí; první verze S10 měla částici mylně o řád níž.

---

## 6. Kam částice putují

**Zdroje:** OECD 2020 (viz výš) a Kole et al. 2017.

Dva modely, dvě různá čísla — a to je důvod, proč scénář **žádné
konkrétní procento neuvádí**:

| | OECD 2020 (globální modely) | Kole et al. 2017 (Nizozemsko) |
|---|---|---|
| zůstane u silnice / v asfaltu | **45 %** | půda **67 %** |
| odnese dešťová voda | **45 %** | povrchová voda ~12 % |
| do ovzduší | **do 10 %** | **12 %** |

Shodují se v tom, co scénář tvrdí: **většina zůstane blízko silnice,
velká část odejde s deštěm, menší část, řádově desetina, jde do vzduchu.**

✅ Scénář v0.2 to říká přesně takhle a **výslovně přiznává**, že se
modely v detailech neshodují („Modelling studies disagree on the
details, but they agree on the shape of it"). Uvést jedno číslo jako
fakt by tady bylo nepoctivé.

Doplňkově doloženo: 2–5 % TRWP se podle modelů dostane řekami až
do ústí (estuárií); podle Kole et al. tvoří otěr pneumatik
3–7 % hmotnosti jemného polétavého prachu PM2,5.

---

## 7. Kolik je na světě vozidel

Odhady se liší podle metodiky (co se počítá jako vozidlo, co jako
„v provozu"):

| zdroj | číslo |
|---|---|
| OICA, poslední zveřejněná statistika „vehicles in use" (2015) | 1,28 mld. celkem, z toho 947 mil. osobních |
| novější komerční odhady (2024–2026) | 1,4–1,7 mld. |

⚠️ **Primární zdroj s aktuálním číslem se nepodařilo dohledat** —
OICA novější „vehicles in use" nezveřejňuje a ostatní jsou komerční
agregátory. Scénář proto říká „**well over a billion**", což je pravda
podle úplně každého z těch odhadů včetně toho nejstaršího a nejnižšího.

Verze v0.1 říkala „hundreds of millions", což bylo o řád opatrnější,
než je potřeba. Opraveno.

---

## 8. „Vysavač na brzdy"

**Zdroje:**
- Tallano Technologies, systém **TAMIC** — popis výrobce a nezávislý
  rozbor v *At source brake dust collection system*,
  Transportation Engineering (2019), doi:10.1016/j.treng.2019.100004.
- MANN+HUMMEL, brzdový prachový filtr — tiskové materiály výrobce.
- UK DfT/DEFRA, *Review of PM2.5 reduction technologies for on road
  transport*.

Doloženo:

1. **Je to doslova odsávání.** TAMIC vede drážku v brzdové destičce,
   kanálky v třmenu a podtlakem odsává částice **přímo z místa styku
   destičky a kotouče** do filtru. Není to metafora.
   ✅ Scénář: „cuts a groove in the brake pad and sucks the dust out
   through the caliper".
2. **Účinnost na zkušebně:** hmotnostní přes **85 %**, početní až 90 %;
   systém je navržen na záchyt aspoň 80 % částic.
   ✅ Scénář: „on test rigs it captures most of it" — záměrně slovy,
   ne číslem, protože je to zkušebna, ne provoz.
3. **Je to jedna z cest, ne ta cesta.** MANN+HUMMEL jde pasivním filtrem
   s účinností řádově 15–40 %. Obojí je ve fázi pilotů.
   ✅ Scénář: „one of the routes they are trying".

⚠️ **Nikde netvrdit, že to EU nařizuje.** Viz bod 1c.

---

## 9. Mikroplasty v lidských tkáních

Doloženo: částice byly popsány v **krvi, placentě, plicní tkáni,
mateřském mléce, varlatech, mozku a v aterosklerotickém plátu**.

- Nature Medicine (2025), měření v mozku, játrech a ledvinách zemřelých
  v letech 2016 a 2024; koncentrace v mozcích z roku 2024 asi o 50 %
  vyšší než z roku 2016.
- New England Journal of Medicine (2024), nález mikroplastů
  v karotidovém plátu spojený s vyšším rizikem infarktu, mrtvice
  nebo úmrtí během tří let sledování.

✅ Scénář tvrdí **jen nález**, ne účinek: „Microplastics have been
detected in water, food, air and human tissues" a hned dodává
„finding particles in the human body doesn't automatically mean
that they are causing disease".

⚠️ To je správně opatrné a **záměrně se tím nepoužívá** studie z NEJM
jako důkaz škodlivosti — je to asociace u konkrétní skupiny pacientů,
ne prokázaná příčinnost, a video by z toho nemělo dělat víc.

---

## 10. 6PPD a losos kisutč (nově ve v0.3, scény S18–S22)

**Primární zdroj:** Tian Z. et al. (2021), *A ubiquitous tire
rubber–derived chemical induces acute mortality in coho salmon*,
Science 371(6525):185–189, doi:10.1126/science.abd6951.
K tomu erratum doi:10.1126/science.abo5785.

| tvrzení ve scénáři | doklad |
|---|---|
| „A tyre contains hundreds of different chemicals." | konzervativní. V pneumatikovém kaučuku bylo popsáno **přes 400** sloučenin; jedna studie Leibnizova institutu identifikovala 2 456 látek, z nichž 144 se vyluhuje |
| „One of them is called 6PPD. It is there to protect the rubber from ozone." | 6PPD je antiozonant, N-(1,3-dimethylbutyl)-N'-fenyl-p-fenylendiamin; brání ozonovému praskání běhounu |
| „It does that by reacting with ozone before the rubber can." | ✅ obětní reakce je principem antiozonantu, ne vedlejším efektem |
| „one of the things that reaction leaves behind is 6PPD-quinone" | 6PPD-chinon je oxidační produkt reakce 6PPD s ozonem |
| „extremely toxic **to some fish**" | LC50 pro mladé kisutče **0,79 ± 0,16 µg/l**, po přeměření s komerčním standardem **95 ng/l** |
| „linked to mass deaths of coho salmon in streams near busy roads, after heavy rain" | v dešťovém odtoku ze silnic v okolí Seattlu naměřeno **0,8–19 µg/l**, při srážkových epizodách 0,3–3,2 µg/l — tedy nad LC50. Tím je vysvětlen *urban runoff mortality syndrome* |

⚠️ **„Some fish" tam musí zůstat.** Citlivost je druhově velmi rozdílná:
losos atlantský (*Salmo salar*) a pstruh obecný (*Salmo trutta*) jsou
podstatně odolnější (Environ. Toxicol. Chem., PMC9828523). Zobecnit to
na „toxic to fish" by bylo doložitelně nepřesné.

⚠️ Scénář **netvrdí nic o účinku na člověka** — a nemá. To je oblast,
kde zatím data nejsou.

✅ Blok zároveň dělá přesně to, co má: dokládá, že problém nemusí být
polymer sám, ale chemie, kterou částice nese. Tím se váže na kapitolu 5
a na větu „simply calling all of this microplastics can be misleading".

---

## Co se do scénáře NEDOSTALO, ale je doložené

**Tvar a velikost částice** (doutníkový, typicky 70–100 µm, hustota 1,8;
OECD 2020). Byl by to hezký diagram, ale ve scénáři pro to není místo —
**nabízí se pro storyboard**, ne pro text.

**Per capita emise** 0,81 kg/rok globálně (Kole et al. 2017), 0,5–1,5 kg
podle OECD. Hezké číslo, ale bez vysvětlování, čí to je „hlava",
špatně uchopitelné.
