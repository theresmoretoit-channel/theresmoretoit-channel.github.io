# Fact check — 049 What Makes a Battery Catch Fire?

**UZAVŘENÝ** (2026-09-16), proti `script.md` verze **0.5**. Všechna
tvrzení scénáře jsou doložená; formulace, které tvrdily víc než zdroj,
jsou opravené — viz „Nálezy z 0.2" a „Co se změnilo v 0.4 a 0.5" dole.

**Odkazy na scény jsou strojově ověřené proti 0.5**: u třinácti nejvíc
zatížených scén (S10, S12, S21, S26, S36, S47, S48, S49, S50, S57, S66,
S68, S69) sedí fragment tvrzení na scénu, na kterou ukazuje.

> **Čísla scén jsou přečíslovaná proti 0.2.** Vypuštění scény o dálnici
> posunulo všechno za ní o jedna dolů; mapa je v `mapa-0.2-0.3.txt`.
> Odkazy níž jsou strojově ověřené proti textu.

Zdrojem čísel je rešerše z 2026-09-16; každé číslo v scénáři má řádek
níž. Tvrzení, která **nejsou** v žádné větě vyslovená, ale ponese je
diagram, se doplní při psaní storyboardu.

---

## 1. Historie a ekonomika (S10–S13)

| tvrzení | ověření | |
|---|---|---|
| „Sony sold the first commercial lithium-ion cell in 1991" | první komerční Li-ion článek uvedla Sony **v roce 1991**, kobalt-oxidová katoda (Goodenough/Mizushima), nasazen nejdřív v kamerách Handycam | ✅ |
| „Lithium is the lightest metal there is" | hustota **0,534 g/cm³**, nejlehčí kov periodické tabulky (a třetí nejlehčí prvek) | ✅ |
| „Between 2010 and 2023, the average price of a battery pack fell by almost ninety percent" | BloombergNEF: **> 1 100 USD/kWh v 2010** → **139 USD/kWh v 2023**, tedy **−88 %** | ✅ |

> **Pozor na jednotku.** BNEF čísla jsou za **pack**, ne za článek.
> Dodaný text mluvil o „battery cells"; ve scénáři je proto „battery
> pack". Kdyby se to při škrtání zkrátilo zpátky na „cell", je to
> nepřesné.

## 2. Co je uvnitř článku (S16–S22)

| tvrzení | ověření | |
|---|---|---|
| kladná elektroda, záporná elektroda, kapalný elektrolyt, separátor | standardní stavba Li-ion článku | ✅ |
| „ionty putují elektrolytem, elektrony jdou oklikou přes telefon" | elektrolyt je iontový vodič a elektronový izolant — proto proud teče vnějším obvodem | ✅ |
| „separator… typically under twenty micrometres" | komerční separátory **7–30 µm**; v testovaných článcích 7, 16, 25 a 30 µm | ✅ „typically under twenty" drží pro moderní články, ne pro všechny |
| „a human hair is around seventy" | lidský vlas **17–180 µm**, běžně uváděný průměr ~70 µm | ✅ |

## 3. Thermal runaway (S26–S41)

| tvrzení | ověření | |
|---|---|---|
| vnitřní zkrat žene energii článku přes malé místo, které se zahřeje | standardní popis iniciace | ✅ |
| „heat it enough and it softens, shrinks away from the hot spot, and gives way" | smrštění a protavení separátoru je popsaný mechanismus rozšíření zkratu. **Konkrétní teplota ve scénáři záměrně není**: polyolefinové separátory mají shutdown zhruba **105–135 °C** podle materiálu a výrobce, keramicky plněné drží podstatně výš | ✅ |
| „heat starts chemical reactions… those reactions give off heat" | exotermní rozklad SEI, elektrolytu a elektrod | ✅ |
| „the electrolyte boils, pressure builds, the cell splits open" | odplynění a protržení pojistného ventilu; uvolněné plyny jsou hořlavé | ✅ |
| **„in some chemistries, the breaking electrode gives off oxygen"** | platí pro **vrstevnaté oxidy** (LCO, NMC), které při rozkladu uvolňují kyslík; **pro LFP to neplatí** | ✅ **jen díky vsuvce „in some chemistries"** — nezkracovat |
| „in those cells, the fire has brought **some of** its own air" | omezeno dvakrát: na „those cells" a na „some of". Uvolněný kyslík požár **živí**, ale článek si nenese celý okysličovadlový rozpočet | ✅ |
| „smothering it does very little… firefighters mostly use water to cool what is around it" | doporučený postup je **chlazení velkým množstvím vody**, ne dušení | ✅ |
| šíření mezi články v packu | thermal runaway propagation je samostatně studovaný jev | ✅ |

> **Tahle pasáž je nejcitlivější místo scénáře.** Věta o kyslíku se
> často přebírá zjednodušeně jako „lithiové baterie si nesou kyslík",
> což u LFP **není pravda** — a LFP je zrovna chemie, kterou video
> o dvacet scén dál chválí. Formulace musí zůstat podmíněná.

## 4. Note 7 jako měřítko „vzácnosti" (S47–S51)

| tvrzení | ověření | |
|---|---|---|
| „In 2016, Samsung recalled two and a half million phones" | staženo **2,5 milionu kusů** v deseti trzích, z toho ~1 milion v USA | ✅ |
| „the number of incidents reported in America was ninety-two, out of roughly a million phones sold there" | CPSC / Samsung: **92 hlášení přehřátí v USA**, 26 popálenin, 55 škod na majetku; ~1 milion kusů v USA | ✅ |
| „that is about one in ten thousand" | 92 / 1 000 000 = **1 : 10 870** | ✅ zaokrouhleno správným směrem |
| „get it banned from aeroplanes" | **US DOT/FAA nouzový příkaz, platný 15. 10. 2016** — zákaz přepravy na palubě, v příručním i odbaveném zavazadle | ✅ |
| „cost more than five billion dollars" | Samsung vyčíslil dopad na **nejméně 5,3 mld. USD** | ✅ |
| „one of the most expensive product failures in the history of consumer electronics" | hodnotící soud, opřený o těch 5,3 mld. | ⚠️ **soud, ne fakt** — ponechat jako řečnickou figuru, nebo nahradit číslem |

> **Past, které se scénář vyhnul:** 92 je počet hlášení **v USA**, ne ve
> světě, a jmenovatel musí být proto taky americký. Poměr „92 ku 2,5
> milionu" by byl **o dva a půl násobku vedle** a vyšel by falešně
> příznivě.

## 5. New York 2023 → 2025 (S65–S70)

| tvrzení | ověření | |
|---|---|---|
| „in 2023 the city recorded two hundred and sixty-eight fires" | FDNY: **268 požárů** od lithiových baterií v roce 2023 | ✅ |
| „eighteen people died" | **18 úmrtí** v 2023 (proti 6 v 2022) | ✅ |
| „**most of it** traced back to one place… cheap replacement packs… often rebuilt from salvaged cells" | FDNY i městské podklady vedou převahu případů k **necertifikovaným, přebaleným nebo repasovaným** packům z šedého trhu („overwhelmingly"). Z „almost all" zmírněno na „most" v 0.3 | ✅ |
| „**from that September**, selling a pack that had not been certified became illegal" | **Local Law 39**, účinnost **16. 9. 2023**: zákaz prodeje, pronájmu a bazarového prodeje necertifikovaných zařízení a baterií (UL 2849 pro kola, UL 2271 pro baterie). Formulace „from that September" je přesnější než „from 2023" a zároveň odlišuje zákon od statistiky za týž rok | ✅ |
| „by 2025, the annual death toll had fallen from eighteen to one" | 2023: **18**, 2025: **1** | ✅ |
| „**the timing is striking.** By 2025 the annual death toll had fallen from eighteen to one" | tvrdí se **souslednost**, ne příčina. Obě čísla doložená | ✅ |
| „the chemistry had not changed. What had changed was which batteries **were reaching the market**" | zákon reguluje certifikaci prodávaného výrobku, ne chemii; věta popisuje, co se změnilo, a příčinu poklesu úmrtí nechává na divákovi | ✅ |

> **Tohle je zároveň pojistka proti oběma vyzněním, která uživatel
> zakázal.** Osmnáct mrtvých vylučuje „média straší"; pokles na jednoho
> po regulaci trhu vylučuje „chemie je nebezpečná sama o sobě".
>
> **Vyřešeno v 0.3.** Pokles 18 → 1 je **korelace**, ne doložená
> kauzalita. Verze 0.2 říkala „what changed was which batteries people
> were **allowed to sell**", což příčinu tvrdilo. Nové znění uvádí
> souslednost („the timing is striking") a fakt o trhu, ale závěr
> nedělá.

## 6. Měřítko energie (S56–S58)

| tvrzení | ověření | |
|---|---|---|
| „a phone battery holds about a dozen watt-hours" | iPhone 13 mini **9,3 Wh**, iPhone 13 Pro Max **16,75 Wh** — pásmo ~9–17 Wh | ✅ „a dozen" sedí doprostřed; dřívější „fifteen" bylo na horním okraji |
| „an electric bike, around five hundred" | běžné pásmo **300–750 Wh**, 500 Wh je de facto standard | ✅ |
| „an electric car carries tens of thousands" | typicky **40–100 kWh**, tedy 40 000–100 000 Wh | ✅ |
| ~~„a car failing can close a motorway for most of a day"~~ | **v 0.3 vypuštěno celé** — nebyl k tomu konkrétní doložený případ a rozdíl 12 Wh proti desítkám kWh nese pointu sám | 🗑 |

## 7. BMS a LFP (S59–S61, S76–S77)

| tvrzení | ověření | |
|---|---|---|
| pack má elektroniku, která hlídá napětí, proud a teplotu a umí odpojit | standardní funkce BMS | ✅ |
| „lithium iron phosphate stores less per kilogram" | LFP má nižší hmotnostní hustotu energie než niklem bohaté chemie | ✅ |
| „much harder to push into runaway" | LFP má vyšší tepelnou stabilitu katody a při rozkladu neuvolňuje kyslík | ✅ |
| solid-state: „swap the flammable liquid for a solid" | principiální popis; scénář si sám bere zpět slovy „in principle" | ✅ |

---

## Nálezy z 0.2 (vyřešené)

Všechny čtyři nahlásil uživatel v `zpetna vazba 0.2.txt` a všechny mají
tentýž tvar: **pěkná formulace tvrdila víc než zdroj.**

| # | co bylo | co je v 0.3 |
|---|---|---|
| 1 | „past roughly a hundred and thirty degrees" | teplota vypuštěna, mechanismus zůstal |
| 2 | „the fire has brought its own air" | „in those cells… **some of** its own air" |
| 3 | „can close a motorway for most of a day" | scéna vypuštěna |
| 4 | „what changed was which batteries people were **allowed to sell**" | souslednost místo příčiny |

## Co se změnilo v 0.4 a 0.5

| verze | scéna | co |
|---|---|---|
| 0.4 | **S48** | hodnotící soud *„one of the most expensive product failures in the history of consumer electronics"* nahrazen samotným číslem: *„The recall cost Samsung more than five billion dollars."* Rozhodl uživatel — číslo je doložené (5,3 mld. USD), soud by se dokládal srovnáním s cizími kauzami |
| 0.4 | S51 | z důsledků vypuštěny peníze (přesunuly se do S48), zůstal konec modelu a zákaz v letadlech |
| 0.5 | **S15** | *„Inside, it is anything but."* → *„Inside, it is not boring at all."* Nebyla to věcná chyba, nýbrž elipsa: *anything but* odkazuje na *boring* ze S14, přes dvě věty a střih scény. Ve čtrnácti překladech navíc past — každý překladatel doplní jiné slovo |

**Fact check tím nemá otevřený bod.**

## Co se kontroluje při každém dalším zásahu

1. Po každém škrtu **strojově ověřit**, že fragment z každého nadpisu
   odpovídá scéně, na kterou ukazuje (past z `CLAUDE.md`: po přečíslování
   ukazuje evidence na cizí tvrzení a vypadá to jako doložený fact check).
2. Věty, které vznikly **slitím nebo zkrácením** dvou zdrojových, patří
   do fact checku stejně jako ty přejaté beze změny.
