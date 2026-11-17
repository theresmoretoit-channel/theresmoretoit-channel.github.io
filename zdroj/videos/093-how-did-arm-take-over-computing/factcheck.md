# Fact check — 093 How Did ARM Take Over Computing?

Ověřeno 2026-10-07 nad `script.md` (číslování scén podle aktuálního `script.md`,
po `script 0.2.md`). `script.md` se tímhle průchodem neměnil — návrhy oprav jsou
u každého ⚠️.

Shrnutí: **⚠️ 2** (S18, S90) + **⚠️ drobné 3** (S55, S72, S83), ❌ žádné,
zbytek ✅. Všech šest prioritních bodů autora (háček S01–S08, S40, S10, S36/S37,
S63, S83) je doloženo; S40 přímo Furberem, záložní formulace není potřeba.

Hlavní primární zdroj: **Oral History of Steve Furber**, Computer History Museum,
rozhovor vedl Doug Fairbairn 3. 2. 2012, ref. 102746196
(https://archive.computerhistory.org/resources/access/text/2012/05/102746196-05-01-acc.pdf,
dále „CHM Furber“). Stažený text je ve scratchpadu, citace níž jsou doslovné.

Homografy ze seznamu (read, lead, live, close, record, present, object, minute,
separate, produce, content, wind, tear) ve scénáři **nejsou** (`grep -w`). `used`
(S12, S39) a `use` (S62) jsou slovesa, výslovnost jednoznačná. K poslechu:
**„ARM“ velkými písmeny** — ověřit, že Emma čte „arm“, ne „A-R-M“; **„RISC“** má
znít „risk“; **„mid-1990s“** — ověřit, že `pronounce` klíč `1990s` sedne i uvnitř
složeniny s pomlčkou.

---

## S01 — „In 1985, engineers in Britain switched on a brand-new processor for the very first time.“ ✅

- CHM Furber: návrh šel do VLSI Technology (finální kontroly v Mnichově, leden 1985);
  *„The chips came back on April 26, 1985 and they arrived in the morning, and by
  the afternoon they were running BBC BASIC.“* Oživení proběhlo v Acornu
  (Cambridge) → „in Britain“ sedí.
- „for the very first time“ — ano, 26. 4. 1985 je první křemík (vývojová deska
  ARM Evaluation System na druhém procesoru BBC Micro).

## S02 — „It worked. Which was already a small miracle.“ ✅

- CHM Furber: *„once those were fixed the chips just ran as expected and we had our
  own microprocessor, much to our surprise!“* a dál: *„until we had working silicon
  in our hands we always expected to discover why it wasn't a good idea.“*
  „Small miracle“ je nadsázka, kterou autor sám podkládá. (Drobnost: musely se
  opravit chyby na desce plošných spojů, čip sám fungoval napoprvé.)

## S03–S05 — napájení nezapojené, čip běžel z proudu přes vstupní piny ✅

> *„But then they noticed something strange. The chip's power supply wasn't
> connected. And yet it was running. It was getting by on tiny currents leaking in
> through its input pins, from the signals of the chips around it.“*

- Furber pro The Register (Unsung heroes of tech, 3. 5. 2012,
  https://www.theregister.com/2012/05/03/unsung_heroes_of_tech_arm_creators_sophie_wilson_and_steve_furber/?page=3):
  první čip zapojil do vývojové desky, multimetr v sérii s napájením ukazoval
  *„The needle was at zero: the processor seemed to be consuming no power
  whatsoever.“* Příčina: závada desky, napájecí vedení nebylo připojené.
  Wilson: *„The processor was actually running on leakage from the logic circuits.“*
- Verze Sophie Wilson (citovaná např. https://gunkies.org/wiki/ARM,
  https://archivesit.org.uk/blog/arm/): *„When Stephen tried to measure the power
  consumption of the first ARM, he realized that the power pins were actually not
  connected … the leakage currents through all the other pins was enough to power
  up the chip.“*
- **Mechanismus:** vstupy CMOS mají ochranné diody proti napájecí sběrnici; když je
  na vstupu logická jednička a napájení „visí“, proud teče přes diodu do napájecí
  sítě čipu. Formulace „tiny currents leaking in through its input pins, from the
  signals of the chips around it“ to vystihuje přesně a **netvrdí, že čip běžel bez
  energie** — říká, odkud ji bral. ✅
- **Kdy se to zjistilo:** obě verze říkají, že se na to přišlo **při měření
  spotřeby** prvního čipu, The Register to klade přímo k prvnímu zapojení na desku.
  Přesné pořadí (hned při zapnutí / až při měření týž den) se z pramenů jednoznačně
  nevyčte. Scénář je formulovaný bezpečně: S01 „switched on … for the very first
  time“ → S02 „It worked“ → S03 „**But then** they noticed“ — netvrdí, že si toho
  všimli v okamžiku zapnutí. Nic neměnit.
- „The chip's power supply wasn't connected“: přesněji nebylo připojené napájecí
  vedení **desky** k čipu (Wilson: „power pins not connected“). Pro diváka totéž. ✅

## S06 — „When they measured it properly, the processor needed about a tenth of a watt.“ ✅

- CHM Furber: *„we actually produced a design which came in under a tenth of a
  watt“*. Obecně citovaná hodnota ARM1 je **0,1 W** (The Register 2012: *„consumed
  no more than a tenth of a Watt“*).
- „about a tenth“ vs „under a tenth“ — v rámci zaokrouhlení OK. Kdo chce být
  doslova u Furbera: *„less than a tenth of a watt.“* (Pak sjednotit i S40.)

## S07 — „Nobody had aimed for that. The engineers just wanted a chip that was cheap to make.“ ✅

- CHM Furber: *„The goal for the ARM processor was to go in Acorn's desktop product,
  and that was quite a cost sensitive application, so our goal was to get the ARM
  processor into a plastic package …“* Cíl byl **< 1 W kvůli ceně pouzdra**,
  ne 0,1 W. „Nobody had aimed for that“ (tj. za desetinu wattu) sedí.
- Nuance pro komentáře: Furber sám říká *„the low power properties were to some
  degree serendipitous but they were not accidental“* — tj. strop 1 W byl záměr,
  desetinásobná rezerva ne. Scénář to v S40 vysvětluje správně.

## S08 — „That chip was the first ARM processor.“ ✅

- ARM1 (Acorn RISC Machine), první křemík 26. 4. 1985.

## S09 — „Forty years later … almost every smartphone. In Apple's computers. In some of the largest data centres in the world.“ ✅

- 1985 → 2025/26 = 40–41 let. ✅
- Smartphony: Arm uvádí podíl **přes 99 %** (Arm, výroční zpráva / prezentace pro
  investory; Arm Official History https://newsroom.arm.com/arm-official-history).
- Apple: všechny Macy od dokončení přechodu (Mac Pro, červen 2023) jsou na Apple
  silicon (ARM). ✅
- Datová centra: AWS Graviton, Microsoft Cobalt, Google Axion, NVIDIA Grace;
  Arm za FY26 uvádí, že jeho podíl na CPU výkonu dodaném největším hyperscalerům
  dosáhl ~50 % (DCD, https://www.datacenterdynamics.com/en/news/arm-posts-recording-breaking-revenue-for-full-year-and-q4-26-with-its-share-of-hyperscaler-cpu-compute-hitting-50/).
  „Some of the largest“ je naopak opatrné. ✅

## S10 — „Hundreds of billions of chips.“ ✅

- Arm Holdings, Form 20-F FY2025 (https://www.sec.gov/Archives/edgar/data/1973239/000197323925000016/arm-20250331.htm):
  za čtvrtletí do 31. 3. 2025 ~7,9 mld. čipů, **kumulativně přes 310 mld.**
  Arm Official History (2026): *„shipped in more than 350 billion chips“*
  (stav k březnu 2026). „Hundreds of billions“ sedí s rezervou.
- Pozor, počítají se **čipy s jádrem Arm**, ne jádra (těch je víc).

## S11 — „a processor from a British home-computer company“ ✅

- Acorn Computers, Cambridge; BBC Micro, Electron, Archimedes. ✅

## S12 — „The answer isn't simply that it used very little power. That part was almost an accident.“ ✅

- Wilson (The Register 2012): *„a complete accident“*; Furber (CHM):
  *„serendipitous but … not accidental“*. „Almost an accident“ leží přesně mezi
  oběma výroky. ✅

## S13 — „we have to go back to 1983“ ✅

- CHM Furber: RISC články od Hermanna Hausera *„early in 1983“*, návštěva Phoenixu
  *„October 1983“*. Návrh ARM začal 1983.

## S14 — „Its BBC Micro was in classrooms all over Britain.“ ✅

- BBC Micro (1981) v rámci BBC Computer Literacy Project; vládní program Micros in
  Schools dotoval nákup do škol, BBC Micro byl dominantní školní počítač v UK.
  CHM Furber: *„The BBC Micro was selling in huge numbers.“* ✅

## S15 — „older, eight-bit chip, the 6502 … Acorn needed something much faster“ ✅

- CHM Furber: *„The BBC Micro was based around the 6502.“* MOS 6502 (1975), 8bitový,
  v BBC Micro na 2 MHz. „Older“ OK (1975 vs. 1983).

## S16–S17 — testovali nové procesory na trhu, žádný nevyhovoval, byly složité ✅

- CHM Furber: *„we spent quite a lot of time looking at the 16-bit microprocessors
  that we could go out and buy … Each one we looked at didn't really meet our
  expectations … the Motorola 68,000 and the National Semiconductor 32016, both of
  which had very rich complex instruction sets.“*
- Furberovy dva konkrétní důvody byly **pomalá obsluha přerušení** (horší než
  6502) a **nevyužití šířky pásma paměti**. Scénář říká „complicated … none of them
  really fit“ — obecnější, ale ne v rozporu (složitá sada je u Furbera uvedena jako
  společná vlastnost obou). ✅

## S18 — „went to Arizona, to the company that designed the 6502.“ ⚠️ upřesnit

- CHM Furber: *„In October 1983. Sophie and I went to Phoenix, Arizona to visit the
  team that was developing a successor to the 6502 … the 65C816.“* Firma byla
  **Western Design Center** (Mesa, předměstí Phoenixu).
- **Původní 6502 ale navrhla MOS Technology** (Norristown, Pensylvánie, 1975, tým
  Chucka Peddla). WDC založil 1978 **Bill Mensch**, který byl v tom týmu jedním
  z návrhářů, a WDC navrhl CMOS verzi 65C02 a 16bitový 65C816
  (https://en.wikipedia.org/wiki/Bill_Mensch, https://en.wikipedia.org/wiki/Western_Design_Center).
  „The company that designed the 6502“ je tedy nepřesné — znalec 6502 se ozve.
- (Tazatel CHM to v otázce sám zkrátil na „the team … that had designed the 6502“
  a Furber přitakal — je to rozšířené zjednodušení, ne doklad.)
- **Návrh** (řádky 16, 27, 26 znaků):
  ```
  went to Arizona,
  to the small firm designing
  the successor to the 6502.
  ```
  Alternativa, pokud má zůstat vazba na samotný 6502:
  ```
  to a firm started by one of
  the 6502's original designers.
  ```
  Pozor: první varianta trochu předbíhá S19 („small“) — případně vypustit „small“.

## S19 — „They expected a big chip company. Instead, they found a handful of people working out of a suburban house.“ ✅

- CHM Furber: *„expecting to find our image of an American company in large shiny
  office blocks, and what we found was the 65C816 design was being done in a fairly
  modest bungalow in the suburbs of Phoenix … a small team with local school kids
  contributing to some of the physical cell design in their summer holidays.“* ✅

## S20 — „If they can design a processor... so can we.“ ✅

- CHM Furber: *„I distinctly remember returning from Phoenix talking to Sophie and
  saying, well, if they can design the microprocessor then maybe we can too.“*
  Scénář zesiluje „maybe we can too“ na „so can we“ — přijatelná parafráze.

## S22–S25 — složité instrukce (CISC), víc logiky na dekódování, víc tranzistorů ✅

- Instrukce typu paměť–operace–paměť existovaly (VAX `ADDL3` s paměťovými operandy,
  68000 `ADD Dn,<ea>` do paměti, x86 `ADD [mem],reg`). Teze, že bohatá sada stojí
  plochu dekodéru/mikrokódu a čas návrhu, je jádro RISC argumentu
  (Patterson & Ditzel, *The Case for the Reduced Instruction Set Computer*,
  ACM SIGARCH CAN 8(6), 1980). ✅

## S26–S28 — Berkeley a Stanford, „They called it RISC“ ✅

- CHM Furber: Hauser přinesl *„papers describing the Berkeley RISC and the Stanford
  MIPS processors … The Berkeley paper used the term reduced instruction set
  computer“*.
- Drobnost: název **RISC** je berkeleyský (Patterson); Stanford svůj projekt nazval
  MIPS. „They called it RISC“ po větě o obou univerzitách je běžná zkratka, obecný
  pojem RISC dnes zahrnuje oba. Nechat.
- S27 „the compiler did the rest“ — přesně teze RISC (přesun složitosti do
  kompilátoru). ✅

## S29 — „Sophie Wilson designed ARM's instructions along those lines.“ ✅

- CHM Furber: *„Sophie started doodling with these ideas and producing draft
  instruction sets … a very strong flavor of the Stanford and Berkeley RISC ideas“*
  (s vlastními prvky — podmíněné vykonávání, barrel shifter). ✅

## S30–S32 — aritmetika jen nad registry, paměť má vlastní instrukce, load-store ✅

- ARM: datové instrukce pracují s registry a přímou hodnotou (immediate) v instrukci;
  přístup do paměti jen `LDR`/`STR`/`LDM`/`STM`. „Arithmetic only works on the
  chip's own registers“ je správně (immediate je součást instrukce, ne paměť).
- S31: přičíst číslo z paměti a výsledek uložit zpět = load, add, store. ✅

## S33 — „each step is regular, predictable, and easy to decode“ ✅

- Pevná délka instrukce 32 bitů, jednotný formát. CHM Furber navíc: *„it had no
  complicated instructions, and therefore we knew exactly … the maximum time it
  would run before it would take an interrupt“* (předvídatelnost). ✅

## S34 — „Sixteen, each thirty-two bits wide. The 6502 had three small ones.“ ✅

- ARM1: 16 viditelných 32bitových registrů (R0–R15, R15 = PC + stavové bity);
  fyzicky 25 včetně bankovaných pro režimy přerušení. „Sixteen“ = viditelné, správně.
- 6502: akumulátor A a indexové X, Y — tři 8bitové „pracovní“ registry (+ ukazatel
  zásobníku, PC, stavový registr). „Three small ones“ odpovídá běžnému popisu. ✅

## S35–S36, S95 — ARM1, „about twenty-five thousand transistors“ ✅

- CHM Furber: *„[the first ARM] chip had 25,000 transistors“*. Ken Shirriff
  (rekonstrukce layoutu, 2016; The Register
  https://www.theregister.com/2016/02/09/arm1_reverse_engineered/): ~25 000. ✅
- S95 „Today's have billions“ — Apple M1 16 mld., M3 Max 92 mld., telefonní SoC
  ~15–20 mld. ✅ (pozor, jde o čipy, ne jádra — viz S72).

## S37 — „Intel's 286, launched a few years earlier, had about a hundred and thirty-four thousand.“ ✅

- Intel 80286 představen **1. 2. 1982**, **134 000 tranzistorů** (Intel; 
  https://en.wikipedia.org/wiki/Intel_80286). ARM1 duben 1985 → 3 roky dřív,
  „a few years earlier“ sedí. Poměr 134 000 / 25 000 = **5,4×**.

## S38–S39 — méně tranzistorů → menší, levnější čip, „almost as a side effect“ nízká spotřeba ✅

- Menší plocha = víc čipů na waferu = nižší cena; méně spínajících tranzistorů =
  nižší dynamická spotřeba. Odpovídá CHM Furber (cíl byla cena, spotřeba vedlejší).

## S40 — „Acorn wanted a cheap plastic package, which meant staying under one watt. So they designed carefully... and landed ten times below.“ ✅ (doloženo primárně)

- CHM Furber doslova: *„our goal was to get the ARM processor into a plastic package
  because plastic packages were much cheaper than ceramic packages. And the plastic
  package had a power limit of around a watt. If you went above a watt you'd have
  to go to a ceramic package and that brought the cost up a lot … the tools … didn't
  really give the kind of accuracy of power prediction … So the way we made sure that
  we came in under a watt was to use the tools conservatively. Effectively, we used
  Victorian engineering margins … in being very careful to make sure it came in under
  a watt, we actually produced a design which came in under a tenth of a watt.“*
- Kauzální příběh (levné pouzdro → strop 1 W → konzervativní návrh → pod 0,1 W) je
  **přímo od Furbera**, v jeho vlastní interpretaci. Záložní formulace není potřeba.
- „ten times below“: pod 0,1 W proti 1 W = **≥ 10×**. ✅
- Nuance: k nízké spotřebě přispěl i malý počet tranzistorů (S38–39), Furber
  konzervativní návrh uvádí jako „some of that“. Scénář obojí má. ✅

## S41 — „In 1987, a faster version of the ARM went into Acorn's new computer, the Archimedes.“ ✅

- CHM Furber: *„the four chip set got into product first in the Archimedes in
  1987“*, *„the chip set that went out in the Archimedes had ARM2 in it with MEMC,
  VIDC and IOC“*; ARM2 ~8 MHz. ✅

## S42 — „one of the fastest personal computers of its day“ ✅

- CHM Furber: *„when that machine came out it was the fastest computer around for
  quite some time“*. Archimedes A310 ~4 MIPS proti ~1–2 MIPS u současných PC/AT
  a 68000 strojů. „One of the fastest“ je opatrnější než Furber. ✅

## S43–S44 — svět kupoval IBM-kompatibilní PC s Intelem ✅

- Konec 80. let: PC kompatibilní (8088/286/386 + MS-DOS) dominují kancelářím. ✅

## S45 — „The Archimedes stayed mostly in British schools.“ ✅

- CHM Furber: *„Acorn's business was getting pretty flat because they principally
  sold into U.K. education“*. (Furber v přepisu říká „end of the 1990s“, z kontextu
  jde o konec 80. let — jeho odchod 1990.) ✅

## S46 — „It had already needed rescuing by Olivetti, back in 1985.“ ✅

- 20. 2. 1985 Olivetti koupilo 49 % Acornu za 12 mil. £, později v roce podíl
  navýšilo na ~80 % (https://computinghistory.org.uk/det/5852/, Centre for Computing
  History). ✅

## S48–S50 — Apple, Newton, nechtěl záviset na čipu konkurenta ✅

- CHM Furber: *„Apple came knocking on the door at Acorn and said they wanted to use
  the ARM in their Newton product, but they were a little uncomfortable with ARM
  being owned by a competitor. So they came to Acorn with the proposal to set up a
  joint venture, and Acorn had been trying to offload the overhead of maintaining
  ARM for a couple of years.“* ✅
- S49 „fast, cheap, and could run on batteries“ — požadavky Newtonu (kapesní,
  bateriový). Newton vyšel 1993 s ARM610 (Arm Official History). ✅

## S51–S52 — 1990 vyčleněno, vlastníci Acorn, Apple, VLSI ✅

- Arm Official History: *„officially founded as a company in November 1990 as
  Advanced RISC Machines Ltd“*, joint venture Acorn, Apple, VLSI Technology.
  Apple vložil ~1,5 mil. £ (43 %), Acorn inženýry, VLSI nástroje. ✅
- (The Register 2012 píše „1991“ — chyba článku, firma založena 27. 11. 1990.)

## S53 — „Twelve engineers. An old barn near Cambridge.“ ✅

- Arm Official History: *„founded by 12 Arm architecture designers“* … *„an old
  turkey barn in Cambridgeshire“* (Swaffham Bulbeck, ~13 km od Cambridge). ✅

## S54–S57 — licence designu, poplatek z každého čipu, ARM nic nevyrábí ✅

- CHM Furber: *„The business model was to license this design and get royalties“*;
  Robin Saxby přidal *„upfront payment for a license followed by royalties“*. ✅
- S56 „ARM would make nothing at all“ — pro 1990 (a dalších 35 let) správně.
  **Pro komentáře:** v březnu 2026 Arm oznámil první vlastní čip (Arm AGI CPU,
  serverový, první zákazník Meta; vyrábí TSMC). Scéna je v minulém čase
  budoucnosti („would“) a popisuje model z roku 1990, takže platí. Nic neměnit.

## S55 — „Intel designs processors, makes them in its own factories, and sells them.“ ⚠️ drobné

- Pro 1990 přesné. V přítomném čase dnes už ne úplně: Lunar Lake (2024) a výpočetní
  dlaždice Arrow Lake vyrábí **TSMC**. Kontext scény je 1990, takže stačí minulý čas.
- **Návrh:**
  ```
  Intel designed its processors,
  made them in its own factories,
  and sold them.
  ```

## S58–S59 — kolem jádra ARM rádio, grafika, procesor kamery v jednom čipu ✅

- System-on-chip s licencovaným jádrem — přesně model ARM (např. TI OMAP, Qualcomm
  Snapdragon). ✅

## S61–S62 — 90. léta, telefony; desktop „a hundred watts and a big fan“ ✅

- Desktopová skříň 90. let a později běžně kolem 100 W i víc (samotný procesor
  10–30 W v 90. letech, dnes až přes 100 W). Řádová ilustrace, OK.

## S63 — „By the end of the decade, ARM cores were inside some of the best-selling phones, from Nokia and others.“ ✅

- Nokia 6110 (oznámen 12/1997): první GSM telefon s ARM — ARM7TDMI v čipu Texas
  Instruments (Arm Official History; https://en.wikipedia.org/wiki/Nokia_6110).
  Totéž jádro v Nokia 3210 (1999, ~160 mil. kusů) a 3310 (2000).
- „and others“: Ericsson (ARM7TDMI v čipech VLSI/Ericsson, mj. Bluetooth baseband)
  a další výrobci s TI basebandem. ✅

## S64 — „Then came the iPod. Then the smartphone.“ ✅

- iPod (2001): PortalPlayer PP5002, dvě jádra ARM7TDMI. iPhone (2007): Samsung
  s ARM11. ✅ (Chytré telefony existovaly dřív, ale „the smartphone“ jako masový
  fenomén = po 2007, OK.)

## S65 — „Billions of people suddenly carried a computer …“ ✅

- Počet uživatelů smartphonů přes 3 mld. kolem 2020 (GSMA, Statista). ✅

## S69–S71 — moderní high-end ARM jádro: velké cache, superskalár, predikce skoků, out-of-order ✅

- Např. Apple Firestorm (8 dekódovaných instrukcí za takt, ROB ~630), Arm
  Cortex-X/Neoverse V — všechno out-of-order se sofistikovanou predikcí skoků. ✅

## S72 — „Billions of transistors. Nothing about it is simple.“ ⚠️ drobné

- Podmětem je od S69 **jádro** („a modern high-end ARM core“). Jedno jádro má řádově
  **stovky milionů** tranzistorů (Firestorm ~2,3 mm² na N5 při ~130 MTr/mm² ≈
  300 mil. vč. L1), miliardy má až **celý čip**.
- **Návrh:**
  ```
  Billions of transistors on the chip.
  Nothing about it is simple.
  ```
  nebo přesněji k jádru: `Hundreds of millions of transistors.`

## S74–S77 — instrukční sada vs. mikroarchitektura ✅

- Standardní rozlišení ISA / mikroarchitektura (Hennessy & Patterson). ✅

## S79–S81 — x86 od poloviny 90. let rozkládá instrukce na mikrooperace ✅

- NexGen Nx586 (1994), **Intel Pentium Pro / P6 (1995)**, AMD K5 (1996, „RISC86“)
  → „since the mid-1990s, Intel and AMD“ sedí. Následné out-of-order jádro je
  koncepčně podobné jako u high-end ARM (která navíc také některé instrukce
  rozkládají na mikrooperace). ✅

## S82 — „the two have grown surprisingly alike“ ✅

- Blem, Menon, Sankaralingam, *Power Struggles: Revisiting the RISC vs. CISC Debate
  on Contemporary ARM and x86 Architectures*, HPCA 2013
  (https://research.cs.wisc.edu/vertical/wiki/index.php/Isa-power-struggles):
  *„Modern microarchitectural techniques mitigate traditional ISA overheads, leading
  to similar energy efficiency across architectures.“* ✅

## S83 — „ARM's cleaner instructions still help. They're easier to decode, and that saves some power.“ ⚠️ drobné (zmírnit)

- Blem 2013: rozdíl ve spotřebě vysvětluje mikroarchitektura a návrhový cíl, ne ISA
  („ISA being RISC or CISC is largely irrelevant“).
- Hirki, Ou, Nurminen, Niemi, *Empirical Study of the Power Consumption of the
  x86-64 Instruction Decoder*, USENIX CoolDC 2016
  (https://www.usenix.org/conference/cooldc16/workshop-program/presentation/hirki):
  dekodéry x86 berou **3–10 % příkonu pouzdra**, a to jen když se kód nevejde do
  cache dekódovaných mikrooperací; jinak méně.
- Tvrzení „easier to decode“ je pravda (pevná délka instrukce), „saves some power“
  je obhajitelné, ale úspora je **malá a v literatuře sporná**. Hned následující
  S84 to sice relativizuje, přesto bych slovo zmírnil:
- **Návrh:**
  ```
  ARM's cleaner instructions still help.
  They're easier to decode,
  which can save a little power.
  ```

## S85 — „ARM didn't take over because it was simple. And it wasn't designed for low power.“ ✅

- Druhá věta: CHM Furber — nízká spotřeba nebyla cílem (cílem byl levný čip pod
  1 W kvůli pouzdru). Viz S07/S40. ✅

## S86 — tři faktory ✅ (interpretace, ne faktické tvrzení)

## S87–S89 — 2020, Apple dal vlastní ARM čipy do Macu ✅

- Apple M1, představen 10. 11. 2020 (MacBook Air, MacBook Pro 13", Mac mini). ✅

## S88 — „Apple had sold its stake in ARM years earlier, when it badly needed the money.“ ✅

- Apple prodával podíl postupně od 1998 (po IPO ARM Holdings v dubnu 1998) do
  ~2003; do února 1999 klesl na 14,8 % a utržil kolem 1,1 mld. USD — v době, kdy
  byl Apple po krizi 1996–97 na hraně
  (https://appleinsider.com/articles/20/06/09/how-arm-has-already-saved-apple---twice,
  https://www.cultofmac.com/97055/). ✅

## S90 — „Not phone chips stretched to fit. Fast cores, efficient cores, graphics and much more, in a single chip.“ ⚠️

- M1 používá **stejná jádra jako iPhonový A14** (Firestorm / Icestorm), jen jich je
  víc (4+4 místo 2+4), větší GPU a sjednocená paměť; v recenzích se o něm běžně
  psalo jako o zvětšeném A14 (např. AnandTech, *Apple Announces The Apple Silicon
  M1*, 10. 11. 2020, srovnává mikroarchitekturu přímo s A14).
  Věta „Not phone chips stretched to fit“ se tím dá vyvrátit — přesně to se o M1
  v komentářích tvrdí. Druhá část (velká i úsporná jádra, grafika, vše v jednom
  čipu) je správně.
- **Návrh** (vypustit první větu, nebo ji obrátit na fakt):
  ```
  The same kind of cores as the iPhone,
  scaled up for a computer.
  Fast cores, efficient cores,
  graphics and much more,
  in a single chip.
  ```
  (řádky 37, 25, 28, 22, 16 znaků)

## S91 — „faster than the Intel chips they replaced, and the laptops ran far longer on a charge“ ✅

- Výkon: M1 MacBook Air překonal v jednovláknových i vícevláknových testech
  (Geekbench 5, Cinebench R23) Intel MacBook Air i Intel MacBook Pro 13" z roku 2020.
- Výdrž (Apple, specifikace 2020): MacBook Air **18 h** přehrávání videa vs. 12 h
  u Intel modelu; MacBook Pro 13" **20 h** vs. 10 h. „Far longer“ ✅

## S92–S93 — datová centra, „Amazon now designs its own ARM server chips“ ✅

- AWS Graviton (2018), Graviton2–4; navrhuje Annapurna Labs (koupena Amazonem 2015).
  ✅ „every watt costs money“ — obecné, OK.

## S96, S98–S101 — závěr ✅

- Interpretační věty, bez ověřitelného údaje navíc. S99 „didn't build it for
  phones, for Apple, or to beat Intel“ — ARM1 byl pro desktop Acornu (CHM Furber). ✅
