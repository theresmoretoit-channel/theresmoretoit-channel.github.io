# Fact check — 038 „How Can You Sell Something You Don't Have?"

Verze scénáře: **`script 0.2.md`**, 64 scén.
Ověřeno 2026-09-09, po opravě nálezu B1 znovu 2026-09-09.

Zdroj (`scenar-puvodni.md`) je **skoro nekvantitativní**: 1 341 slov
a jediné konkrétní datum je duben 2020. Většina tvrzení jsou proto
**definice a mechanika**, ne údaje — a právě u definic vznikl jediný
skutečný nález (B1): scénář popisoval mechaniku shortu **akcií**,
zatímco celý zbytek videa mluví o **futures**, kde se nic nepůjčuje.
**Opraveno v 0.2**, viz níž.

---

## A. Aritmetika — dopočítána, ne odhadnuta

Všech osm výpočtů ve scénáři **sedí**. Spočítáno strojově, ne z hlavy:

| scéna | tvrzení | výpočet | |
|---|---|---|---|
| S04 | koupím za 10, prodám za 20 → „made ten dollars" | 20 − 10 = **10** | ✅ |
| S07–S08 | prodej na 80, zpět za 60 → „twenty-dollar difference" | 80 − 60 = **20** | ✅ |
| S10 | short na 80, zpět za 100 → „I lose twenty dollars" | 80 − 100 = **−20** | ✅ |
| S11 | short na 80, cena na 200 → „I lose one hundred and twenty" | 80 − 200 = **−120** | ✅ |
| S14 | koupím za 80, cena na 0 → „I lose eighty" | 0 − 80 = **−80** | ✅ |
| S14 | short na 80, cena na 160 → „I've lost eighty" | 80 − 160 = **−80** | ✅ |
| S15 | short na 80, cena na 800 → „I've lost seven hundred and twenty" | 80 − 800 = **−720** | ✅ |
| S52 | kontrakt za 70 centů → „about a seventy percent chance" | 0,70 → **70 %** | ✅ |

> **S11 obsahuje i nedopočítaný případ a je to v pořádku.** Scénář se
> ptá *„If it goes to five hundred?"* a odpovídá *„Well... you get the
> idea."* Správná hodnota by byla **−420**; scénář ji záměrně neuvádí,
> takže tu není co ověřovat. Nechat tak — beat je funkční.

> **S14 je symetrická dvojice a právě v tom je pointa.** Ztráta 80
> nastane u dlouhé pozice teprve při pádu ceny **na nulu**, kdežto
> u krátké už při **zdvojnásobení**. Obojí ověřeno výš, tvrzení
> o asymetrii tedy stojí na správných číslech.

---

## B. Nálezy

### B1. VYŘEŠENO: u futures se nic nepůjčuje — S07, S08

**Původní znění (0.1):** *„So I borrow an oil contract and sell it for
eighty dollars."* (S07) a *„I return what I borrowed."* (S08)

**Ověření.** Půjčení a vrácení je mechanika krátkého prodeje **akcií**:
prodávající si půjčí cenné papíry od brokera, prodá je, později koupí
zpět a vrátí — a platí za to výpůjční poplatek. **U futures nic
takového neexistuje.** Futures je standardizovaná dohoda, která
*vzniká v okamžiku obchodu*: krátkou pozici lze otevřít kdykoli,
bez půjčky, bez výpůjčního poplatku a bez uptick pravidla, protože
burza zachází s oběma stranami stejně.

❌ **Neplatilo.** A nebyla to drobnost, protože scénář si tím **odporoval
sám se sebou**: S26 o osmnáct scén dál říká *„The traders simply exit
their positions... So I can sell a futures contract for oil... and
later buy the same contract back."* — tedy správně, bez půjčování.

**Kde chyba vznikla:** slovo *short selling* zastřešuje dvě různé
mechaniky a scénář vzal název od té akciové, ale příklad od té
futuresové.

### ✅ Opraveno v `script 0.2.md`

Uživatel zvolil variantu A (vypustit půjčování) a dodal znění
(`zpetna vazba 0.1.txt`):

| | 0.1 | 0.2 |
|---|---|---|
| **S07** | *So I **borrow** an oil contract / **and sell it** for eighty dollars.* | *So I **sell** an oil contract / for eighty dollars.* |
| **S08** | ***I return what I borrowed.*** / *And I keep the twenty-dollar difference.* | *And I keep the twenty-dollar difference.* |

Zbytek obou scén beze změny. Logika je teď **prodám za 80 → cena padá
→ koupím za 60 → +20**, bez tvrzení o půjčce.

**Ověřeno po zásahu:**

- `contract` v nové větě zůstává podstatným jménem: `sˌəʊ aɪ sˈɛl ɐn ˈɔɪl kˈɒntɹakt fɔːɹ ˈeɪti dˈɒləz` ✅
- rozpor se S26 zmizel — slovo *borrow* ani *borrowed* už ve scénáři není ✅
- **čísla scén se neposunula** (S07 a S08 zůstaly), takže odkazy v tomhle
  souboru dál ukazují na správná místa. Ověřeno strojově, viz kapitola E
- délka: −12 slabik, S07 vychází na 6,2 s a S08 na 3,8 s

> **Vedlejší přínos, na který upozornil uživatel:** divák v tuhle chvíli
> pořád ještě neví, *jak* se dá prodat něco, co člověk nemá. Odpověď
> přijde až v S23–S31 (*„we're trading a contract"* → *„does the oil
> actually have to exist?"* → *„we're really trading a promise"*).
> Otázka z titulku tedy zůstává otevřená o čtyři minuty déle, což je
> přesně to, co CLAUDE.md žádá.

### B2. Zjednodušený setup v S01–S02 se NEOPRAVUJE

**Tvrzení:** *„I don't own the oil. In fact, I don't even want the
oil. I just think its price is going down."* (S01) a *„So I sell it
to you today... and I plan to buy it back later, hopefully for
less."* (S02)

Doslova vzato je to *naked short* fyzického barelu, tedy zjednodušení.
**Ponecháno záměrně** (rozhodl uživatel): je to hook a pozdější věta
ze **S23** *„we often aren't trading oil... We're trading a
contract."* ho zpětně správně přerámuje. Není to nepřesnost, kterou by video nechalo stát —
je to nepřesnost, kterou video samo vysvětlí.

---

## C. Duben 2020 — ověřeno proti primárnímu zdroji

### C1. Cena ropných futures spadla pod nulu — S42

**Tvrzení:** *„The price of a major oil futures contract briefly fell
below zero."*

**CFTC**, tisková zpráva k prozatímní zprávě o obchodování kontraktu
NYMEX WTI, doslova:

> The May Contract „fell from **$17.73 per barrel to settle at −$37.63
> per barrel on April 20**, the day before the contract expired."

✅ **Platí.** Kontrakt WTI s dodáním v květnu 2020, vypořádací cena
**−37,63 USD za barel** dne **20. dubna 2020**, den před expirací;
vnitrodenní minimum **−40,32 USD**. Byl to první záporný kurz WTI
od zahájení obchodování v roce 1983. Propad za jediný den činil
**55,36 USD**.

> **Scénář to formuluje opatrně a dobře.** Říká *„a major oil futures
> contract"*, ne „ropa stála mínus třicet sedm dolarů" — což by bylo
> nepravdivé zobecnění, protože Brent týž den stál kolem **26 USD**
> a fyzická ropa se pod nulou neprodávala plošně.

### C2. Příčinou byl nedostatek skladovací kapacity — S40, S41, S45

**Tvrzení:** *„There was too much oil... and not enough storage
space."* a *„you could end up with an obligation to take delivery
of oil. And if you had nowhere to put it... that was a very
expensive problem."*

CFTC uvádí *„concerns about availability of global crude oil storage"*
mezi fundamentálními faktory, které cenu **mohly ovlivnit**, spolu
s převisem nabídky a propadem poptávky kvůli covidu; výslovně dodává,
že zpráva **není analýzou hlavní příčiny**. Doplňkově: zásoby ve
skladovacím uzlu **Cushing v Oklahomě** (místo fyzického dodání WTI)
vzrostly mezi 13. březnem a 1. květnem o 27 milionů barelů na **83 %
provozní kapacity**.

✅ **Platí**, a scénář zachovává i tu opatrnost — neříká „protože",
nýbrž popisuje situaci. Mechanika v S44–S45 je přesně ta, která
zápornou cenu vysvětluje: kdo držel kontrakt do expirace, měl
**povinnost odebrat** 1 000 barelů v Cushingu.

> **Doložitelný dopad, kdyby se hodil jako tvrdé číslo:** při
> −37,63 USD dostal držitel *dlouhé* pozice k tisícovce barelů ještě
> **37 630 USD** navrch. Ve scénáři to není a nemusí být.

**Zdroje:** [CFTC — Interim Report on NYMEX WTI Crude Contract Trading around April 20, 2020](https://www.cftc.gov/PressRoom/PressReleases/8315-20),
[EIA — Crude oil prices briefly traded below $0 in spring 2020](https://www.eia.gov/todayinenergy/detail.php?id=46336),
[Congressional Research Service — Crude Oil Futures Prices Turn Negative](https://www.congress.gov/crs_external_products/IN/PDF/IN11354/IN11354.1.pdf)

### C3. Poptávka po ropě se propadla, výroba nemohla přes noc stát — S39, S40

**Tvrzení:** *„oil demand collapsed. People stopped driving. Airlines
stopped flying. Factories shut down."* a *„But oil production couldn't
simply stop overnight."*

✅ **Platí.** Propad poptávky kvůli pandemii je uveden mezi faktory
i v CFTC zprávě. Setrvačnost těžby je vlastnost ropných polí —
zastavení a opětovné spuštění vrtu je nákladné a u některých ložisek
nevratně poškozuje produktivitu.

---

## D. Mechanika a definice — ověřeno

### D1. Neomezená ztráta u krátké pozice — S12, S13

**Tvrzení:** *„With a short position, there is theoretically no upper
limit to how much you can lose. Because there is no upper limit to
how high the price can go."*

✅ **Platí.** Ztráta krátké pozice je (cena při uzavření − cena při
otevření) a horní mez ceny neexistuje, kdežto dlouhá pozice je
omezená zdola nulou. Scénář správně píše **„theoretically"** —
v praxi pozici uzavře margin call dřív.

### D2. Většina futures nekončí fyzickým dodáním — S25

**Tvrzení:** *„Most futures contracts never result in somebody
receiving a truck full of oil."*

✅ **Platí.** Za běžných podmínek skončí fyzickým dodáním řádově
**1–3 %** nominálu; zbytek se uzavře před prvním oznamovacím dnem.
„Most" je tedy tvrzení **slabší** než skutečnost, což je bezpečný směr.

> **„Truck full of oil" je obraz, ne popis.** WTI se nedodává
> v cisterně, nýbrž převzetím v potrubním a nádržovém uzlu Cushing.
> Scénáři to nevadí — nepopisuje logistiku, kreslí divákovi představu.
> **Do storyboardu ale patří poznámka, aby to nekreslil doslova.**

**Zdroj:** [CME Group — Cash Settlement vs. Physical Delivery](https://www.cmegroup.com/articles/2025/cash-settlement-vs-physical-delivery.html)

### D3. Zajištění aerolinky přes futures — S18, S19

**Tvrzení:** *„Imagine you're an airline. Fuel is one of your biggest
costs."* a *„you can buy futures contracts that effectively lock in
a price for oil."*

✅ **Platí obojí.** Podle IATA je palivo **25,7 az 28,9 %** provozních
nákladů (2024: 28,9 %, 2025: 25,8 %, výhled 2026: 25,7 %) — tedy
skutečně jedna z největších položek. Nákupem futures hedger uzamkne
cenu: vzroste-li cena, dražší palivo vyrovná zisk z pozice.

> **Jedna jemnost, kterou scénář obchází správně:** aerolinky
> se běžně nezajišťují přímo ropnými futures, nýbrž nástroji na
> letecký petrolej nebo crack spreadem, protože cena kerosinu
> a cena ropy se rozcházejí. Scénář ale říká *„effectively lock in
> a price for oil"*, tedy mluví o ropě a o principu — a ten platí.
> Kdyby se doplňovalo číslo, tahle věta **není** místo, kde jmenovat
> konkrétní aerolinku.

**Zdroj:** [IATA — Airline Profitability to Strengthen Slightly in 2025](https://www.iata.org/en/pressroom/2025-releases/2025-06-02-01/)

### D4. Arbitráž jako kotva mezi papírem a fyzickou ropou — S35, S36, S37

**Tvrzení:** *„If the futures price becomes wildly different from the
physical price, traders can exploit the difference. They can buy the
cheap thing and sell the expensive thing. That's called arbitrage."*

✅ **Platí** jako popis principu (cash-and-carry arbitráž). Scénář
navíc sám dodává *„Usually."* — a to je věcně důležité: **v dubnu
2020 arbitráž selhala právě proto, že chyběl sklad**, tedy vazba, na
které cash-and-carry stojí. Existuje k tomu recenzovaná studie
přímo pod názvem *Arbitrage breakdown in WTI crude oil futures*.
Scénář tedy nejen že nepřehání, on tu výhradu **vysloví dřív, než
ji doloží**, což je dobrá stavba.

### D5. Prediction market: cena ≈ pravděpodobnost — S51, S52, S53

**Tvrzení:** *„A contract might pay one dollar if the answer is yes...
and zero dollars if the answer is no. If that contract trades for
seventy cents, the market is roughly saying: we think there's about
a seventy percent chance."*

✅ **Platí.** Přesně takhle jsou binární kontrakty konstruované:
výplata 1 USD při „ano", 0 při „ne", takže cena mezi 0 a 100 centy
se čte jako implikovaná pravděpodobnost.

> **Slovo „roughly" je nutné a scénář ho má.** Cena je
> *diskontovaná* pravděpodobnost — sráží ji vázání kapitálu do
> vypořádání, prodleva výplaty a riziko platformy. Bez toho „roughly"
> by tvrzení bylo příliš silné; s ním je správně.

### D6. Polymarket — S55

**Tvrzení:** *„Platforms such as Polymarket have made this kind of
prediction market highly visible."*

✅ **Platí** a je formulované opatrně — *„such as"* a *„highly
visible"*, tedy žádné tvrzení o velikosti, přesnosti ani legálnosti.
To je dobře: regulační postavení těchto platforem se v posledních
letech měnilo a jakýkoli silnější výrok by rychle zastaral.

### D7. Co všechno se dá vložit do kontraktu — S49

**Tvrzení:** *„Interest rates. Currencies. Stock indexes. Inflation.
Credit risk. Even weather."*

✅ **Platí u všech šesti.** Pro každou položku existuje zavedený trh:
úrokové futures a swapy, měnové futures, indexové futures, inflační
swapy, credit default swapy a **počasnostní deriváty** (CME obchoduje
futures na denostupně HDD/CDD). *„Even weather"* tedy není nadsázka.

---

## E. Co bylo prověřeno a je bez nálezu

| oblast | výsledek |
|---|---|
| **homografy** (seznam z CLAUDE.md) | `contract` 19×, vše podstatné jméno → espeak `kˈɒntɹakt` ✅; `object` ✅; `closes` ✅. **Jediná vada `close` v S26 už opravena na `exit`** |
| **výslovnost** (441 různých slov, fonemizace `en-gb`) | žádný odborný termín espeak neplete; všechny rozdíly proti slabikovači jsou běžná anglická synkopa. **`pronounce` není potřeba** |
| **odborné termíny** | `arbitrage` `ˈɑːbɪtɹɪdʒ` ✅, `futures` `fjˈuːtʃəz` ✅, `counterparties` ✅, `asymmetry` ✅, `Polymarket` `pˌɒlɪmˈɑːkɪt` ✅ |
| **věrnost převodu** | `difflib` nad tokeny zdroje a scénáře: **shoda 99,3 %, 8 rozdílů** — 5 vynucených při převodu, 3 z opravy B1 (viz `notes.md`) |
| **odkazy na scény po zásahu** | fragment z každého nadpisu tohoto souboru dohledán ve scéně, na kterou ukazuje ✅ |

---

## Shrnutí

| | |
|---|---|
| ověřených tvrzení | **21** |
| nálezů | **1** (B1 — půjčování u futures), **opraven v 0.2** |
| tvrzení opřených o primární zdroj | 3 (CFTC, IATA, CME) |
| aritmetických kontrol | 8, všechny sedí |

**B1 je opraven, ostatní tvrzení prošla. Scénář `script 0.2.md` je
věcně v pořádku a připravený na TTS.**
