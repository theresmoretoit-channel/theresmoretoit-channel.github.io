# Fact check — Where Does the Fuel Go When a Plane Dumps It?

Každé ověřitelné tvrzení ze `script.md`. Stav k **24. 8. 2026**, scénář **v0.3** (51 scén, 1 153 slov, 8:25).

> Scénář byl 24. 8. zkrácen z 58 scén / 10:41 na cílovou stopáž. **Škrt
> nezrušil žádné ověřené tvrzení** — všech šestnáct je ve v0.3 pořád, jen
> pod jinými čísly scén. Odkazy níž už jsou přečíslované; předchozí verze
> je `script 0.2.md`.

**Fact check je uzavřený — scénář smí do TTS.** Čtyři dříve nedotažené položky
jsou vyřešené (dvě změkčením textu, jedna doložením z primárního zdroje, jedna
ponechána s uvedeným stupněm doložení) — viz oddíl „Vyřešeno" na konci.

> Pozor: dvě položky se řešily **opravou dřívější evidence, ne doplněním**.
> U MLW 747-400 přebil primární zdroj sekundární a zároveň vyvrátil zobecnění,
> které tu dřív stálo u S08. Detaily jsou u obou scén.

---

## S07 — „A seven four seven may take off at three hundred and ninety-seven tonnes. It may land at two hundred and eighty-six."

**Ověřeno z primárního zdroje** — Boeing *747-400 Airplane Characteristics for
Airport Planning*, D6-58326-1 **Rev F, prosinec 2024**, oddíl 2.1.1
(motory GE CF6-80C2B1). Návrhové hmotnosti jsou nabízené ve variantách:

| | | | | | |
|---|---|---|---|---|---|
| **MTOW** (lb) | 800 000 | 833 000 | 850 000 | 870 000 | **875 000** |
| MTOW (kg) | 362 873 | 377 842 | 385 553 | 394 625 | **396 893** |
| **MLW** (lb) | 574 000 | 574 000 | 630 000 | 630 000 | **630 000** |
| MLW (kg) | 260 362 | 260 362 | 285 763 | 285 763 | **285 763** |

Poznámka 1 v dokumentu: *„630,000 LB LANDING WEIGHT IS OPTIONAL"* — základní
MLW je 574 000 lb, vyšší se dokupuje.

**Závěr:** ✅ Dvojice ve scénáři (396 893 kg → „three hundred and ninety-seven",
285 763 kg → „two hundred and eighty-six") je **přesně poslední sloupec
tabulky**, tedy konzistentní pár jedné skutečné konfigurace, ne dvě čísla
z různých strojů.

> **Opravena dřívější evidence.** Do 22. 8. tu stálo MLW 652 000 lb
> (295 743 kg) ze sekundárního zdroje (flugzeuginfo.net). V ACAP pro
> osobní 747-400 **taková hodnota není** — patrně jde o -400ER nebo
> nákladní verzi. Primární zdroj tedy sekundární přebil.

---

## S08 — „That gap is over a hundred tonnes."

**Rozdíly MTOW − MLW po sloupcích** (z tabulky výše):

| MTOW (lb) | MLW (lb) | rozdíl |
|---|---|---|
| 800 000 | 574 000 | 102,5 t |
| 833 000 | 574 000 | 117,5 t |
| 850 000 | 630 000 | **99,8 t** ← jediný pod stovkou |
| 870 000 | 630 000 | 108,9 t |
| **875 000** | **630 000** | **111,1 t** ← dvojice ve scénáři |

**Závěr:** ✅ Pro dvojici, kterou scénář právě vyslovil, je rozdíl 111,1 t.
Věta „that gap is over a hundred tonnes" navazuje na ta dvě čísla, takže
platí přesně tak, jak je řečená.

> ⚠️ **Opravena dřívější evidence — dříve tu stálo, že tvrzení platí
> „za jakékoli kombinace variant". To neplatí.** Ten závěr stál na chybném
> MLW 652 000 lb. Podle ACAP existuje konfigurace (850 000 lb / 630 000 lb),
> kde rozdíl vyjde **99,8 t**, tedy těsně pod stovkou.
>
> Na scénář to nemá vliv, protože ten mluví o konkrétní dvojici. Kdyby ale
> někdo chtěl větu zobecnit na „a seven four seven can always take off
> a hundred tonnes heavier than it can land", **bylo by to nepravdivé.**
>
> Poučení: zobecnění „platí vždy" se musí ověřit proti **úplnému** seznamu
> variant z primárního zdroje. Se sekundárním zdrojem vyšel opačný závěr.

---

## S20 / S21 / S22 — vypouštěcí výška a odpar

| Tvrzení | Ověření | Závěr |
|---|---|---|
| „no lower than about eighteen hundred metres" | Zdroj uvádí **6 000 ft AGL = 1 829 m**; video to říká metricky jako „asi 1 800 m", což je zaokrouhlení dolů, tedy konzervativní | ✅ |
| „above roughly fifteen hundred metres, more than ninety-eight percent evaporates" | Model ATSDR (US Agency for Toxic Substances and Disease Registry): >98 % paliva vypuštěného nad 1 500 m se odpaří dřív, než dosáhne země | ✅ |
| „ground sampling found no liquid fuel at all" | Vzorkování pod reálnými dumpy (studie na KC-135) nenašlo kapalné palivo ani při vypuštění z 750 m | ✅ |
| „that number is not arbitrary" | 1 800 m leží **nad** prahem 1 500 m ze studie | ✅ Metricky je ta souvislost vidět rovnou, bez převodu ze stop |

**Poznámka k poctivosti:** studie ATSDR i KC-135 pracují hlavně s **JP-4**,
což je těkavější palivo než dnešní civilní Jet A-1 / JP-8. Literatura sama
uvádí, že chování méně těkavého JP-8 není tak dobře zmapované. Scénář proto
neříká „palivo zmizí", ale výslovně dodává, že kerosin **nezmizí, zůstává
v atmosféře a je to reálná ekologická zátěž** (S22). To je věcně přesnější
než formulace v původním námětu („významná část se odpaří").

---

## S24 / S25 — „ten to eleven tonnes an hour" → „about ten hours"

**Ověření spotřeby:** 747-400 v cestovním režimu spálí ~10–11 t/h
(shoda víc zdrojů; závisí na hmotnosti, výšce a rychlosti).

**Přepočet:** 111,1 t ÷ 11 t/h = **10,1 h**; ÷ 10 t/h = **11,1 h**.

**Závěr:** ✅ „about ten hours" je spodní hranice rozsahu, takže tvrzení
nepřehání. Při pomalejším spalování je to ještě déle.

---

## S26–S34 — létající plamenomet a F-111

| Tvrzení | Ověření | Závěr |
|---|---|---|
| „Somebody did" | F-111 Aardvark uměl *dump and burn* | ✅ |
| „fuel dump outlet happened to sit between the two engines" | Výpustný otvor byl mezi motory; efekt byl **vedlejší produkt umístění trubky**, ne záměr | ✅ |
| „lit the afterburners... the fuel ignited" | Palivo se vzňalo od horkých výtokových plynů při zapnutém přídavném spalování | ✅ |
| „Australian air force turned it into a signature airshow display" | RAAF to předváděla na airshow, byla to jejich poznávací figura | ✅ |
| „no operational purpose" | Sloužilo výhradně k efektu | ✅ |
| ~~„the US Air Force banned the practice"~~ → **„And nobody else ever took it up."** | Doložitelné je jen to, že *dump and burn* předváděla na airshow **výhradně RAAF**. Tvrzení o formálním zákazu USAF stojí jen na diskusních fórech (PPRuNe, Quora, Airliners.net) — žádný rozkaz ani směrnice. **Změněno ve scénáři 24. 8.** | ✅ po opravě |
| „On an airliner, the nozzles are at the wingtips, deliberately" | Jettison trysky jsou na odtokové hraně křídla u konců, aby palivo minulo letadlo; jsou konstruované na rozprášení | ✅ |

> **Tohle je největší zásah do námětu.** Původní text bral plamenomet jako
> čistě absurdní nápad. Ve skutečnosti *existoval* — a tím se z vtipu stává
> mechanismus: rozdíl mezi F-111 a dopravním letadlem je doslova umístění
> jedné trubky. Zároveň to odpovídá na námitku „plamen by se mohl vrátit
> k letadlu" konkrétněji než původní formulace.

---

## S35 / S36 — kufry

**Přepočet:** 200 × 20 kg = **4 000 kg = 4 t**. Podíl na stotunovém
problému: 4/100 = **4 %**.

**Závěr:** ✅ Aritmetika sedí a scénář správně říká „four percent of the problem".

---

## S38 / S39 — 150 cestujících

**Přepočet:** 12 000 kg ÷ 80 kg = **150** přesně.

**Závěr:** ✅ Vnitřně konzistentní. 80 kg je **záměrně kulaté číslo**
a scénář to přiznává („assumes eighty kilograms each"), takže netvrdí,
že jde o certifikační hodnotu. (Standardní hmotnosti podle EASA jsou vyšší
a dělily by se nehezky; pro vtip je 150 lepší a nic tím nelže.)

---

## S42 / S43 / S44 / S45 / S46 — většina letadel palivo vypouštět neumí

| Tvrzení | Ověření | Závěr |
|---|---|---|
| „Most airliners cannot dump fuel at all" | Jettison mají hlavně velké širokotrupé stroje: 747, 777, 787, A330, A340, A350, A380, DC-10/MD-11, L-1011 (u A300/A310/A330 jako opce) | ✅ |
| „The seven three seven cannot. The A three twenty cannot." | 737 (všechny verze) ani rodina A320 jettison nemají | ✅ |
| „Neither can the seven five seven, the A two twenty…" | 757, A220, DC-9/MD-80/717 a regionální proudové stroje jettison nemají | ⚠️ A220 viz Nedotažené |
| „written into the certification rules" | FAR 25.1001 / CS-25 | ✅ |
| „needs a jettison system only if it cannot meet its climb requirements after a fifteen minute flight at maximum weight" | Systém není požadován, pokud stroj splní stoupavost podle FAR 25.119 (landing climb) a 25.121 (approach climb) při předpokladu 15minutového letu | ✅ Formulace ve scénáři to shrnuje věrně |
| „So the rule does not require it, and nobody fits it" | Úzkotrupé stroje stoupavost splní i při plné hmotnosti | ✅ |

**Historická poznámka (do videa nejde, ale ať je zapsaná):** dřívější
kritérium bylo poměr MTOW/MLW > 1,05. Dnešní znění je založené na stoupavosti.

**Závěr:** ✅ Toto je věcná díra, kterou původní námět měl — mlčky
předpokládal, že jettison umí každé letadlo. Doplněno jako S42–S49.

---

## S48 — „circles until it has burned enough off. Or it lands overweight"

**Ověření:** obojí je standardní postup. Overweight landing je certifikovaný
úkon s vlastním checklistem a následnou prohlídkou.

**Závěr:** ✅

---

## Vyřešeno 24. 8. 2026 (dříve „Nedotažené")

Všechny čtyři blokující položky jsou uzavřené. **Scénář je z hlediska
fact checku připravený do TTS.**

| # | Položka | Jak vyřešeno |
|---|---|---|
| 1 | „the US Air Force banned the practice" (S32) | **Změkčeno ve scénáři** na „And nobody else ever took it up." Zákaz se nepodařilo doložit ničím než diskusními fóry; to, že to předváděla jen RAAF, doložitelné je. |
| 2 | A220 v seznamu strojů bez jettisonu (S43) | **Ponecháno.** Potvrzeno víc nezávislými sekundárními zdroji (Fly Away Simulation, Aeropeep, eplaneAI). Pořád ne certifikační dokument — kdyby se seznam zkracoval, tohle je první na odstřel. |
| 3 | „for twenty-five years" (S13) | **Změněno ve scénáři na „for decades".** Konkrétní číslo bylo nepodložené, řádově správné. |
| 4 | MLW 747-400 z Boeing ACAP (S07) | **Doloženo z primárního zdroje** — D6-58326-1 Rev F. Zároveň tím vyšlo najevo, že dřívější sekundární hodnota byla chybná, viz S07 a S08. |

**Zbývá jediná slabina, a je vědomá:** seznam strojů bez jettisonu (S43) stojí
na sekundárních zdrojích. Nic v něm neodporuje ostatním zdrojům, ale
certifikační doklad to není.

---

## Zdroje

- [Fuel dumping — Wikipedia](https://en.wikipedia.org/wiki/Fuel_dumping) — FAR 25.1001/CS-25, 25.119, 25.121, 6 000 ft AGL, seznam strojů, rychlosti vypouštění
- [Boeing 747-400 — Wikipedia](https://en.wikipedia.org/wiki/Boeing_747-400) — MTOW 875 000 lb (396 890 kg)
- [Boeing 747-400 — flugzeuginfo.net](https://www.flugzeuginfo.net/acdata_php/acdata_7474_en.php) — ⚠️ uvádí MLW 652 000 lb, což pro osobní -400 **odporuje ACAP**; nepoužívat
- **[Boeing 747-400 Airplane Characteristics for Airport Planning, D6-58326-1 Rev F (prosinec 2024)](https://www.boeing.com/content/dam/boeing/v2/airports/acaps/747-400_Rev_F.pdf)** — primární zdroj návrhových hmotností, oddíl 2.1.1. Ověřeno 24. 8. 2026 (PDF má 16 MB, `WebFetch` na něj nestačí — stáhnout `curl` a číst `pdftotext -layout`)
- [Evaporation and Groundfall of JP-4 Jet Fuel Jettisoned by USAF Aircraft (DTIC)](https://apps.dtic.mil/sti/tr/pdf/ADA109307.pdf) — odpar a groundfall
- [Fuel Jettisoning by U.S. Air Force Aircraft, Vol. I (DTIC)](https://apps.dtic.mil/sti/tr/pdf/ADA089010.pdf)
- [Fuel Dumping: Guidance for Flight Crews — SKYbrary](https://skybrary.aero/articles/fuel-dumping-guidance-flight-crews)
- [Is It True That The Boeing 737 Can't Dump Fuel? — Simple Flying](https://simpleflying.com/true-boeing-737-cant-dump-fuel/) — úzkotrupé stroje bez jettisonu
- [Boeing 777 Fuel Jettison System — TransGlobal Training](https://www.transglobaltraining.com/boeing-777-fuel-jettison/) — trysky na koncích křídel, rozprašování
- [Fuel dump: which aircraft can dump fuel — Aerospace Global News](https://aerospaceglobalnews.com/news/fuel-dump)
- [How much fuel does a Boeing 747-400 burn — FlightDeckFriend](https://www.flightdeckfriend.com/ask-a-pilot/how-much-fuel-does-a-jumbo-jet-burn/) — 10–11 t/h
- [Airbus A380 Aircraft Characteristics (Airbus)](https://www.airbus.com/sites/g/files/jlcbta136/files/2021-11/Airbus-Aircraft-AC-A380.pdf) — MTOW 575 t / MLW 394 t (ve scénáři nakonec nepoužito)
