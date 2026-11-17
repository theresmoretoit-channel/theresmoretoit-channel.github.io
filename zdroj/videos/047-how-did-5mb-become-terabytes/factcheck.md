# Fact check — 047 How Did 5 MB Become Terabytes?

**Fact check je UZAVŘENÝ** (2026-09-15), proti `script.md` **0.3**
(metrická verze). Všechna tvrzení scénáře jsou doložená; rozbor
posledních pěti bodů je v kapitole „Uzavřeno" dole.

> **Čísla scén jsou přečíslovaná proti 0.1.** Škrt S27–S30 posunul
> všechno za ním o čtyři dolů (mapa v `mapa-0.1-0.2.txt`). Je to přesně
> ta past z `CLAUDE.md`, kvůli které evidence po škrtu ukazuje na cizí
> tvrzení — proto se tenhle soubor upravil zároveň se scénářem, ne potom,
> a 28 odkazů na scény se pak strojově ověřilo proti textu.

**Čtyři nálezy opravily podklady nebo draft**, viz kapitoly „Nálezy"
a „Nález, který málem prošel" dole.

---

## 1. RAMAC 350 — základní údaje (S01, S02, S12, S13, S16, S17)

| tvrzení ve scénáři | ověření | |
|---|---|---|
| IBM dodalo první pevný disk v roce 1956 | oznámeno na tiskové konferenci **14. 9. 1956** (interně 4. 9.), dodávky od června 1956 | ✅ |
| „held about five megabytes" | **5 milionů znaků**, marketingové číslo; viz bod 2 | ✅ s výhradou |
| padesát kovových plotem, dvě stopy napříč | **50 plotem, 24 palců** = 61 cm | ✅ |
| „spinning twenty times a second" | **1 200 ot/min** = přesně 20 otáček za sekundu | ✅ |
| „find any piece of data in under a second" | průměrná doba vyhledání **600 ms** | ✅ |
| hlava plave na tlakovém vzduchu, 20 µm | **800 mikropalců** = 20,3 µm, **hydrostatické** ložisko z vnějšího kompresoru | ✅ |
| „sixty centimetres across" (S12) | 24 palců = **61 cm** ✅ |  |
| „two hundred kilograms of that ton was a pump" | jednotka **1 730 lb = 785 kg**, kompresor **441 lb = 200 kg** | ✅ |
| „weighed more than a ton" (S02) | jen **s kompresorem**: 1 730 + 441 = 2 171 lb > 2 000 lb (krátká tuna) | ✅ **jen díky formulaci** |

> **Formulace v S02 je zamčená.** Věta zní *„with the compressor that
> kept it running, it weighed more than a ton"*. Bez té vsuvky je to
> **nepravda** — samotná jednotka tunu nemá (785 kg). Nezkracovat.

## 2. „Pět megabajtů" není pět megabajtů (S18, S19)

5 000 000 znaků × 6 datových bitů = 30 Mbit = **3,75 MB** formátovaných
(neformátovaně 6,09 MB). Osmibitový kód s šesti datovými bity.

**Proto je ve scénáři scéna navíc (S18–S19), která to přizná.** Číslo
„5 MB" je zároveň v titulu videa — to je v pořádku, je to číslo, pod
kterým RAMAC zná internet, a video ho **zpřesní, ne popře**. Kdyby
zpřesnění vypadlo při škrtání, kanál tvrdí doložitelnou nepravdu.

Navazující čísla se počítají z **3,75 MB**:

| | |
|---|---|
| „nearly ten million times more" (S03) | 36 TB / 3,75 MB = **9,6 milionu×** ✅ |
| „a thousand times lighter" (S06) | 785 kg / ~0,65 kg = **1 200×** ✅ |

✅ Hmotnost dnešního 3,5" disku: **680 g** (Seagate Exos X20, 20 TB),
takže poměr vychází na 1 150×.

## 3. Plošná hustota — nosné číslo celého videa (S21, S22, S39, S40)

**Zdroje uvádějí hustotu v bitech na ČTVEREČNÍ PALEC, video mluví
METRICKY** (rozhodl uživatel 2026-09-15). Obě soustavy proto vedle sebe;
převodem se poměr nemění, takže „miliardakrát" platí v obou.

| | bitů/palec² *(zdroj)* | bitů/cm² *(video)* |
|---|---|---|
| RAMAC | **2 000** = 100 bitů na palec stopy × 20 stop na palec | **310** |
| IBM 1301 | 26 000 | 4 030 |
| dnes | **~1,8 bilionu** (Seagate Mozaic, 36TB, ~3,6 TB na plotnu) | **~279 miliard** |
| poměr | **~900 milionů×**, tedy „roughly a billion" ✅ | **týž** |

> **Převod je v kódu na JEDNOM místě** (`_kit.na_cm2()`), ne rozepsaný
> v pěti scénách, a **zaokrouhluje na tři platné číslice**. Surový
> převod 1,8 bilionu dá `279 000 558 001`, tedy číslo předstírající
> přesnost na jednotky bitů — zdroj má číslice dvě. Falešná přesnost
> je táž vada jako tvrdit víc, než co je doloženo.

> **Ostatní jednotky videa byly metrické už předtím** (kilogramy,
> mikrometry, nanometry, 450 °C), takže palce byly nekonzistence, ne
> volba. Nejhůř to bylo vidět u výšky letu: **S16 říkala „twenty
> micrometres", ale S25 kreslila kóty „800" a „250 MICROINCHES"** —
> táž veličina dvěma soustavami ve dvou sousedních scénách.

**Kontrast miliarda proti tisícovce** (hustota proti hmotnosti) je teze
videa a obě čísla jsou z nezávislých zdrojů.

## 4. IBM 1301, 1961 — konec kompresoru (S23, S24, S25)

| tvrzení | ověření |
|---|---|
| hlava tvarovaná tak, aby si vzduchový polštář vyrobila sama | **samočinné (hydrodynamické) vzduchové ložisko**, slider ✅ |
| „three times nearer the surface" | 800 → **250 mikropalců** = 20,3 → 6,4 µm = 3,2× ✅ |
| „thirteen times the density" | 2 000 → **26 000 bitů/palec²** = 13× ✅ |

## 5. Winchester 3340, 1973 (S26)

Uzavřená sestava plotem a hlav v jednom modulu, lehká hlava, která na
plotně startuje a přistává. ✅ Kapacita 30 MB se ve scénáři **neříká**
— kdyby se doplňovala, ověřit (model 3340 měl 35 a 70 MB varianty).

## 6. Seagate ST-506, 1980 — ~~ve scénáři~~ ŠKRTNUTO v 0.2

Blok o formátech a o ST-506 (8", 5,25", 3,5" → Seagate 1980 → 1,5 kg →
pětsetkrát lehčí) **z videa vypadl celý**, protože týž argument dokazují
S06–S07 (tisíc proti miliardě) a S23–S25 (kompresor, hustota 13×).

**Nic z toho už se ve videu netvrdí**, takže tenhle oddíl nic nehlídá.
Zůstává tu jen proto, že to byl jediný bod, který stál na nedoloženém
čísle (hmotnost ST-506 „přes 3 libry" ze sekundárního zdroje) — a tím,
že scéna vypadla, **ten dluh zmizel**.

## 7. Obří magnetorezistence (S33, S34, S35, S36, S37, S38)

| | |
|---|---|
| **1988** | Albert Fert a Peter Grünberg, **nezávisle na sobě** ✅ |
| **1997** | IBM dodá první čtecí hlavu na tom jevu ✅ |
| **2007** | Nobelova cena za fyziku ✅ |
| „inside ordinary computers for a decade" | 1997 → 2007 = deset let ✅ |

**Formulace ve scénáři nikde neříká konkrétní počet disků** — původní
nápad „stovky milionů počítačů" se **neověřil, a proto ve scénáři není**.
Věta říká jen „inside ordinary computers for a decade", což z těch tří
dat plyne.

✅ *„By the late eighties, it was getting thin."* (S31) je zjednodušení,
které obstojí — rozbor s daty MR hlavy je v kapitole „Uzavřeno":
mezi indukční hlavou a GMR byla ještě **magnetorezistivní hlava (MR,
IBM 1991)**. Scénář netvrdí, že GMR byl jediný krok, ale při škrtání
tam nesmí vzniknout věta, která by to tvrdila.

## 8. Superparamagnetický limit (S42 az S47)

| | |
|---|---|
| zrno drží směr, protože překlopení stojí energii; menší zrno = nižší bariéra | ✅ standardní výklad (KuV proti kT) |
| „somewhere near fifteen billion bits per square centimetre" | podélný zápis narazil kolem **100–200 Gbitů/palec²**, tedy **15,5–31 Gbitů/cm²** ✅ |
| „around the turn of the century" | sedí s nasazením PMR v 2005 ✅ |

## 9. Kolmý zápis (S49 az S54)

| | |
|---|---|
| magnetizace otočená o 90°, míří do hloubky plotny | ✅ |
| „a standing bit can be narrow and still be deep" | ✅ svislá geometrie + měkká podkladová vrstva dovolí silnější zápisové pole a lepší tepelnou stabilitu |
| „drives started shipping that way in 2005" | **květen 2005, Toshiba** (1,8" disk v přehrávači); Seagate a HGST 2005–2006 ✅ |
| „every hard drive you have bought since works like this" | ✅ — i disky s ohřevem laserem jsou kolmé |

## 10. Zápis s ohřevem (S55 az S59)

| | |
|---|---|
| ~~materiál odolný tepelnému šumu: železo-platina~~ | ✅ FePt — ale **v 0.2 se to ve videu už neříká**, viz níž |
| „if the material is too stable to write, heat it first" | ✅ přesně to je důvod ohřevu |
| laser v hlavě, **~450 °C**, **~1 ns**, pak zamrzne | ✅ |
| „this is not a laboratory, you can buy it" | ✅ Seagate Mozaic 3+, 36TB, dodávky 2025 |

> **Zkratka HAMR se ve voiceoveru záměrně neříká** (viz `notes.md`,
> kapitola o výslovnosti). Do diagramu patří.

> **Zkráceno v 0.2.** Původní S59 jmenovala železo a platinu a vysvětlovala,
> že zápisová hlava materiál sama nepřeklopí. Recenzent to označil za
> nepotřebné k pochopení principu; zůstalo *„If the material is too stable
> to write, heat it first."* **Ubyla tím jedna doložená položka, ne žádné
> tvrzení** — a konkrétní slitina je pořád ověřená pro případ, že by se
> vracela do diagramu.

> **Opraveno proti prvnímu draftu:** stálo tam *„firing billions of
> times an hour"*. Laser se **nepulzuje po bitech** — svítí po dobu
> zápisu. Věta je přepsaná.

## 11. Flash (S60 az S70)

| | |
|---|---|
| bit = zachycený náboj za izolantem v buňce | ✅ |
| náboj zvedne napětí, při kterém buňka sepne; měří se to napětí | ✅ prahové napětí |
| „it is a number of electrons" a ztráta hrstky elektronů rozhodne | ✅ citlivost na ztrátu **jediného elektronu** je uváděný důvod konce plošného škálování |
| „four bits means sixteen different charge levels" | ✅ QLC = 16 hladin |
| **mapování bitů na ose napětí (S63)** | ✅ NAND čte **vymazanou** buňku jako **1** a naprogramovanou jako **0**. Scénář mapování neuvádí, takže by obraz mohl mlčet — jenže když už čísla ukazuje, musí je ukázat správně. První verze měla 0 vlevo a 1 vpravo, tedy obráceně |
| „a few hundred millivolts" mezi hladinami | ✅ |

## 12. Tři rozměry místo dvou (S71, S72, S73)

| | |
|---|---|
| **2013, Samsung**, první sériová 3D NAND (V-NAND) | ✅ |
| **24 vrstev** v první generaci | ✅ |
| „today the count is in the hundreds" | ✅ 286 vrstev v sérii (2025), ohlášeno 400+ |
| „the roadmaps talk about a thousand" | ✅ tisícivrstvá 3D NAND je předmětem publikované literatury a plánů |

## 13. Disk neumřel (S76)

| | |
|---|---|
| „more than nine tenths of the storage in cloud data centres is still spinning disks" | ✅ **přes 90 % exabajtů** v cloudových datacentrech (IDC); v Q4 2025 tvořily nearline disky 86,8 % dodané kapacity |
| „per byte it is still far cheaper" | ✅ ~**15 USD/TB** u disků proti zhruba 2,5× vyšší ceně podnikových flash disků |

> **Pozor na zobecnění, které tam NENÍ.** Draft říkal *„most of the
> world's data… because per byte nothing is cheaper"*. Obojí bylo moc
> silné: doložená je **cloudová datacentra**, ne „svět", a **levnější
> než flash**, ne „nejlevnější" — páska je levnější. Přepsáno.

---

## Nálezy: tři věci, které se opravily dřív, než se natočí

### A. Nobelova cena za GMR je 2007, ne 1997 *(chyba v zadání)*

`/mnt/sandisk128/poznamky.txt` navrhoval větu *„In 1997, two physicists
received the Nobel Prize…"*. Správně jsou **tři data**: objev 1988,
první hlava 1997, cena 2007. Oprava je zároveň lepší příběh a scénář
ji používá tak (S37, S38).

### B. SMR nejsou „bity na výšku" *(chyba v zadání)*

Zadání psalo *„PMR → SMR / perpendicular recording"* a vykládalo obojí
jako využití svislého prostoru. **Svislé je jen PMR.** SMR překrývá
stopy vodorovně jako tašky na střeše. **SMR se do videa nedostalo
vůbec** a formulace *„we started standing the bits upright"* patří
výhradně k PMR (S52).

### C. Kompresor nezrušil Winchester v roce 1973, ale IBM 1301 v roce 1961 *(chyba v mém draftu)*

První draft přisuzoval samonosnou hlavu Winchesteru. Ve skutečnosti
zmizel vnější tlakový vzduch už u **IBM 1301 (1961)** a hned to
**třináctinásobně zvedlo hustotu** — což je přesně teze videa
předvedená na jednom stroji. Draft byl přepsán (S23 az S26) a beat je
tím lepší, ne slabší.

---

## Uzavřeno (2026-09-15)

Všech pět zbývajících bodů dořešeno; fact check je **uzavřený**.

### 1. Hmotnost dnešního 3,5" disku ✅

Seagate Exos X20, 20 TB: **680 g**. Poměr 785 kg / 0,68 kg = **1 150×**,
tedy „about a thousand times lighter" (S06) sedí.

### 2. ~~Hmotnost ST-506~~ — odpadlo, scéna je v 0.2 škrtnutá.

### 3. Primární zdroje k RAMACu ✅

**Computer History Museum** potvrzuje celý oddíl 1 najednou a doslova:
*„5 million, 6-bit characters"* / *„3.75 Megabytes"*, *„fifty 24-inch
diameter disks"*, *„1200 rpm"*, *„average access time of under 1
second"*, **„2,000 bits/sq. in"** a *„weighed over one ton (including
a separate air compressor required for operation)"*.

> Ta poslední citace je důležitá: potvrzuje **zamčenou formulaci S02**
> slovo od slova — tunu má RAMAC jen s kompresorem.

**ASME landmark** nezávisle potvrzuje 50 plotem, 5 milionů znaků,
sto stop na každé straně každé plotny a datum **4. 9. 1956** (tedy
interní oznámení; veřejná tisková konference byla 14. 9.).

### 4. Zjednodušení kolem „late eighties" ✅ obstojí

Doplněná časová osa čtecích hlav:

| | |
|---|---|
| **1990** | první magnetorezistivní (MR) hlava, IBM 9345 „Sawmill" |
| **1991** | IBM 0663 „Corsair", první 3,5" disk s MR hlavou, 132 Mbitů/palec² |
| **1997** | GMR „spin valve", 1 Gbit/palec², Deskstar 16GP |

Mezi slábnoucím signálem konce osmdesátých let a GMR tedy **ležela ještě
MR hlava**. Scénář ji nezmiňuje, ale nikde netvrdí, že GMR byl jediný
nebo první krok — S32 říká jen *„Then physics handed the industry
something it had not asked for"*, a objev GMR (1988) do konce
osmdesátých let opravdu spadá. **Zjednodušení, ne chyba**; kdyby se
scénář někdy rozšiřoval, tohle je místo na půl věty.

### 5. Čísla scén ✅ přečíslována a strojově ověřena

Po škrtu S27–S30 se celý soubor přečísloval zároveň se scénářem a
28 odkazů se ověřilo proti textu scén.

---

## Nález, který málem prošel: výška RAMACu

**S02 tvrdí *„taller than the person operating it"*.** Při dohledávání
primárních zdrojů se ukázalo, že to není tak jisté, jak vypadalo:

| zdroj | co čte jako VÝŠKU |
|---|---|
| Computer History Museum | „5 ft high by 6 ft wide" → **152 cm** |
| IBM archiv / heise | „60 in long, **68 in high**, 29 in deep" → **172 cm** |
| IBM soupis komponent (305 RAMAC) | 350 Disk Storage **72 in** → **183 cm** |

**Všechny tři uvádějí TYTÉŽ tři rozměry (60 × 68 × 29 palců) a každý je
přiřazuje jinak.** Dva ze tří dávají výšku 172 az 183 cm, tedy nad
průměrnou postavou; CHM podle všeho prohodilo výšku se šířkou, protože
60 palců ≈ 5 stop a 68 ≈ 6 stop přesně sedí na jeho formulaci.

**Závěr: tvrzení se drží**, ale je to nejtěsnější tvrzení videa a stojí
na čtení rozměrů. Kdyby se někdy měnilo, bezpečná náhrada je velikost
místo výšky (*„the size of two fridges side by side"*), kterou uvádějí
sekundární zdroje shodně.

> **Poučení:** u čísla, které opisují všichni od všech, se vyplatí
> podívat se, jestli se neliší jen **přiřazením**. Tady by z „taller
> than the person" byla doložitelná nepravda, kdyby se vzalo první
> vyhledané číslo.
