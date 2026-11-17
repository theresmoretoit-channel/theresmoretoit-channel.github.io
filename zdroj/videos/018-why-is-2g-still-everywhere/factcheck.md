# Fact check — 2G Is Ancient. So Why Are Lifts, Cars and Alarms Still Using It?

Ověřeno 2026-09-01. **Čísla scén platí pro `script 0.3.md` (85 scén)** —
přečíslováno podruhé, po dramaturgickém cutu, který zrušil osm scén
opakujících už řečené (viz `notes.md`, „Cut 0.3"). Verze 0.1 a 0.2 měly
jiné číslování; kdo cituje starší čísla, musí je přemapovat.

Dvě tvrzení tím ztratila druhý výskyt ve scénáři: rozepsání provozu
(*„An eCall system makes an emergency call…"*) a sdílení mezi operátory
(*„Vodafone could provide some sites…"*). **Doklady se nemění** — jen se
o ně opírá méně scén.

Souhrn: **žádné tvrzení scénáře neprošlo jako nepravdivé.** Dvě čísla, která
v 0.1 vycházela z ověření silnější než text, jsou v 0.2 zapracovaná —
kapitola 7.

---

## 1. GSM je z počátku devadesátých let — S08

> „GSM first appeared commercially in the early 1990s."

**Ověřeno.** První komerční GSM síť na světě spustila **Radiolinja ve Finsku
1. července 1991**. Scénář říká „early 1990s", což sedí přesně.

Doplňkově: standardizace GSM začala v CEPT už 1982, první specifikace 1987
(podpis GSM MoU), takže „ancient" je obhajitelné i tou delší historií.

Zdroj: [Radiolinja, Wikipedia](https://en.wikipedia.org/wiki/Radiolinja)

**Závěr: ✅ beze změny.**

---

## 2. GPRS má desítky kilobitů za sekundu — S16, S17

> „We are talking about tens of kilobits per second."

**Ověřeno.** GPRS dává v praxi **9 az 114 kbit/s** podle počtu přidělených
timeslotů a kódovacího schématu; teoretické maximum standardu je
171,2 kbit/s (8 timeslotů, CS-4), v provozu prakticky nedosažitelné.
Typický reálný provoz jednoho zařízení je 20 az 60 kbit/s.

„Tens of kilobits per second" je tedy **správný řád** a scénář se
nedopouští ani nadsázky, ani podcenění.

Zdroj: [Nokia/Radiolinja GPRS, tisková zpráva 2000](https://www.globenewswire.com/en/news-release/2000/01/24/1844727/0/en/Nokia-delivers-first-phase-GPRS-core-network-solution-to-Radiolinja-Finland.html)

**Závěr: ✅ beze změny.**

---

## 3. Pár set bajtů stačí — S20, S21

> „A device might only need to send a few hundred bytes."
> „Temperature, 21.4. Pressure, 1012. Status, OK."

**Ověřeno výpočtem, ne odhadem.** Ta tři pole zabírají v čitelném textovém
tvaru **41 bajtů** i s oddělovači. I se záhlavím protokolu, identifikací
zařízení a časovým razítkem je to řádově **stovky bajtů**, ne kilobajty.

Hodnoty samy jsou fyzikálně příčetné: **1012 hPa** je běžný atmosférický
tlak (normál 1013,25 hPa) a **21,4 °C** pokojová teplota. Scénář je nikde
neoznačuje jednotkou, takže netvrdí ani °C, ani hPa — je to ukázka tvaru
zprávy, ne měření.

**Závěr: ✅ beze změny.**

---

## 4. Výtah vydrží dvacet až třicet let — S24, S72

> „A lift can stay in service for twenty or thirty years."
> „But a lift from 2011? That's barely middle-aged."

**Ověřeno.** Životnost výtahu se v oboru běžně uvádí jako **20 az 30 let**,
modernizace se doporučuje po dvaceti letech a prodlouží životnost o dalších
10 az 20 let. Scénářové „twenty or thirty years" je tedy střed rozpětí,
ne horní hranice.

Z toho plyne i to, že **výtah z roku 2011 je v roce 2026 patnáctiletý**,
tedy zhruba v polovině životnosti — scénářové „barely middle-aged" sedí
doslova.

Zdroj: [Elevator Life Expectancy](https://www.elevatorconsultantsolutions.com/elevator-life-expectancy)

**Závěr: ✅ beze změny.**

---

## 5. eCall volá 112 a posílá data o vozidle — S29

> „The European emergency call system can automatically contact 112 after
> a serious accident and transmit information about the vehicle."

**Ověřeno proti nařízení.** Nařízení **(EU) 2015/758** ukládá vybavit
palubním systémem eCall na bázi 112 všechny **nové typy** vozidel kategorií
**M1 a N1 od 31. března 2018**. Při detekci vážné nehody systém
automaticky volá 112 a odesílá **minimální soubor dat (MSD)**: přesnou
polohu, čas nehody, směr jízdy a identifikační číslo vozidla (VIN).

Technické požadavky doplňuje nařízení v přenesené pravomoci **(EU) 2017/79**.

Scénářová formulace „transmit information about the vehicle" je tedy
**přesná a záměrně obecná** — MSD skutečně nese údaje o vozidle i o nehodě.

Zdroj: [eCall in-vehicle system — type-approval, EUR-Lex](https://eur-lex.europa.eu/EN/legal-content/summary/ecall-in-vehicle-system-type-approval.html)

**Závěr: ✅ beze změny.**

---

## 6. Starší eCall jede po 2G a 3G — S28

> „And some older cars have emergency communication systems based on 2G
> or 3G. This includes older versions of eCall."

**Ověřeno.** První generace palubních jednotek eCall pracuje výhradně
v **okruhově spínaném režimu (circuit-switched)**, tedy po 2G nebo 3G;
přenos MSD se děje in-band modemem uvnitř hlasového hovoru. Sítě LTE/5G
jsou paketové a starší jednotka se do nich nepřihlásí.

Právě proto studie Komise doporučuje zachovat **aspoň jednu okruhově
spínanou síť**, ne „nějaké 2G" — viz kapitola 7.

**Závěr: ✅ beze změny.**

---

## 7. Studie Evropské komise — S53, S54, S55, S57

Tohle je nejsilněji doložená část videa a v revizi 0.2 se z ní stal
**reveal**: nápad „EU Legacy" (S48–S50) se ukáže jako věc, kterou nezávisle
na nás doporučuje studie zadaná Komisí.

Primární zdroj: [EU study informs of eCall service gaps as 2G/3G networks shut down](https://digital-strategy.ec.europa.eu/en/library/eu-study-informs-ecall-service-gaps-2g3g-networks-shut-down)

| tvrzení scénáře | scéna | doloženo |
|---|---|---|
| „In May 2026, the European Commission published a study on exactly this." | S53 | studie zveřejněná **28. 5. 2026**, zadala **Evropská komise**, zpracoval **LS Telcom** |
| „…64 million vehicles across the EU could lose eCall." | S54 | „an estimated **64 million vehicles** could lose eCall functionality due to uncoordinated network shutdowns across the EU" |
| „If the networks are switched off without coordination…" | S54 | tatáž věta: **„due to uncoordinated network shutdowns"** |
| „Keep at least one circuit-switched network alive until at least 2030." | S57 | studie doporučuje Komisi „issue formal guidance, urging Member States to **preserve at least one circuit-switched network until at least 2030**" |

> **Jedno zjednodušení, které je vědomé.** Doporučení má ve skutečnosti
> mezikrok: studie doporučuje **Komisi**, aby vydala pokyn **členským
> státům**, aby síť zachovaly. Scénář ten řetězec zkracuje na „the study
> recommends: keep at least one circuit-switched network alive". Obsah
> doporučení tím zůstává nedotčený — mění se jen adresát, kterého by
> jmenování ve videu jen zatížilo. **Nesmí se ale posunout na
> „EU rozhodla"**: studie doporučuje, nerozhoduje, a S57 to drží slovem
> *recommend*.

**Bonus, který revizi posiluje:** studie podle téže stránky hodnotí jako
možná řešení mimo jiné **network sharing** a **úpravy spektrových licencí**
(„spectrum licence adjustments, network sharing, and financial incentives").
To je přesně to, co scénář navrhuje o pět scén dřív v S48 (nemuselo by to
patřit jednomu operátorovi). Video tu shodu nepojmenovává a nemusí —
podstatné je, že **není v rozporu se zdrojem, nýbrž s ním souhlasí**.

Studie zároveň uvádí, že **náhradní řešení pro dovybavení se nečekají před
rokem 2030**, což je důvod, proč je doporučená hranice zrovna tam.

**Závěr: ✅ všechna čtyři tvrzení doložena primárním zdrojem.**

### A ověření opačným směrem: žádná „EU Legacy" se nechystá

Vyžádal si ho uživatel 2026-09-01 otázkou, jestli je pravda, že EU žádnou
takovou síť nestaví. **Je.** Ověřeno hledáním na pan-evropskou sdílenou
legacy síť: nic takového neexistuje ani se nepřipravuje. Přístup EU je
**doporučení na národní úrovni**, ne jednotná síť.

To je pro video důležitější, než vypadá, protože **doporučení studie
a náš návrh nejsou totéž**:

| | studie Komise | „EU Legacy" ve videu |
|---|---|---|
| kdo | **každý členský stát** aspoň jednu síť | **jedna sdílená** evropská |
| co to je | doporučení, ne závazné pravidlo | myšlenkový experiment autora |
| staví to někdo | — | **nikdo** |

Rozdíl „v každé zemi" versus „jedna sdílená" byl v první verzi diagramu
S57 zamlžený: stálo tam jen *„keep at least one circuit-switched network"*
bez adresáta, takže se to četlo jako jedna síť pro celou EU — tedy náhodou
přesně to, co navrhuje video. Opraveno na *„each Member State should
keep…"* a doplněno *„a recommendation, not a binding rule"*.

**S58 proto ukazuje obě věci vedle sebe** a pojmenovává, která je která:
vlevo plnou čarou, co žádá studie, vpravo čárkovaně *„WHAT WE JUST MADE
UP"* a *„nobody is building this"*.

---

## 8. Operátoři vypínají 2G ke konci dekády — S71

> „Some European operators are planning to retire 2G around the end of
> this decade."

**Ověřeno.** Ohlášené termíny v Německu, tedy na největším trhu EU:

| operátor | termín vypnutí 2G |
|---|---|
| Deutsche Telekom | **červen 2028** (ohlášeno jako první na trhu) |
| Vodafone Německo | **září 2028** pro zákazníky; síť běží pro část IoT do konce **2030** |
| O2 / Telefónica Německo | **druhá polovina 2028** |
| Vodafone (celá Evropa) | postupné ukončení do **2030** |

GSMA eviduje **131 sítí naplánovaných k vypnutí do roku 2030**, z toho
zhruba polovinu 2G.

Scénářové „around the end of this decade" tedy sedí; nadpis původního
zdroje „2028 is not very far away" je doložený doslova. Nadpisy se
nemluví, ale číslo 2028 se dá bez obav použít **v obraze**.

Zdroj: [Vodafone prepares to pull plug on German 2G](https://www.mobileworldlive.com/europe/vodafone-prepares-to-pull-plug-on-german-2g/)

**Závěr: ✅ beze změny.**

---

## 9. Barevná televize je příklad zpětné kompatibility — S59, S60, S61

> „The colour television standards were designed so that older
> black-and-white receivers could still display the original image.
> New televisions could extract the additional colour information."

**Ověřeno.** FCC schválila barevný standard NTSC v **prosinci 1953**
právě s podmínkou **plné zpětné kompatibility** s tehdejšími
černobílými přijímači.

Mechanismus je přesně ten, který scénář popisuje: jas (luminance) se
vysílá stejně jako dřív, barva se přidá na **barvonosné subnosné
3,579545 MHz**. Frekvence byla zvolena tak, aby složky chrominance padly
**přesně mezi** složky luminance, takže barevný přijímač je umí oddělit
a černobílý je prakticky nevidí — chroma signál jednoduše ignoruje.

Scénář neuvádí NTSC ani PAL jménem, takže tvrzení platí pro obojí
(PAL i SECAM byly navrženy na témže principu kompatibilního přidání
barvy k monochromnímu signálu).

Zdroj: [NTSC, Wikipedia](https://www.wikiwand.com/en/NTSC)

**Závěr: ✅ beze změny.**

> **Hlídané místo — upozornil na ně uživatel u v0.1.** Z analogie nesmí
> vyplynout, že GSM a LTE mohly být zpětně kompatibilní podobným trikem.
> Scénář si to sám vyvrací hned v následujícím bloku (S63, S64) a dělá to
> **dřív, než divák stihne vyvodit špatný závěr** — mezi „that is what
> good backward compatibility looks like" (S62) a „mobile networks are
> much more complicated" (S63) není žádná scéna. Ověřeno po revizi 0.2:
> přesun bloku o Komisi to pořadí nerozbil.

---

## 10. GSM a LTE nejdou složit dohromady — S63, S64

> „GSM and LTE are not simply two versions of the same technology."
> „You can't just add a little bit of LTE to a GSM signal and expect
> a 1998 Nokia to understand it. It won't."

**Ověřeno technicky.** Nejde o rozdíl verzí, ale o jinou fyzickou vrstvu:

| | GSM | LTE |
|---|---|---|
| přístup | TDMA / FDMA | OFDMA (dolů), SC-FDMA (nahoru) |
| šířka nosné | 200 kHz | 1,4 az 20 MHz |
| jádro sítě | okruhově spínané | plně paketové (EPC) |
| modulace | GMSK, 8-PSK | QPSK az 256-QAM |

Barevná televize šla přidat proto, že šlo o **doplněk k témuž signálu**;
LTE není doplněk GSM, je to jiný signál. Analogie ve scénáři je proto
podána správně — jako **protipól**, ne jako návod.

**Závěr: ✅ beze změny.** Scénář si sám v S63 říká „to be fair, mobile
networks are much more complicated", takže analogii nepřepíná.

---

## 11. Moderní sítě využijí spektrum lépe — S39, S40, S47

> „Modern networks can use that spectrum much more efficiently. LTE and
> 5G can provide vastly more capacity and much better performance."

**Ověřeno řádově.** Spektrální účinnost GSM je zhruba **0,2 bit/s/Hz**,
u LTE **1,5 az 3 bit/s/Hz** podle konfigurace MIMO. Rozdíl je tedy
**téměř řádový**, což „vastly more" unese.

Scénář nikde neuvádí konkrétní násobek, takže není co upřesňovat.

**Závěr: ✅ beze změny.**

---

## 12. Jmenovaní operátoři — S48

> „It doesn't necessarily have to be Vodafone. Or O2. Or Deutsche Telekom."
> „Vodafone could provide some sites. O2 could provide others."

**Ověřeno.** Všichni tři jsou skuteční evropští mobilní operátoři a
scénář je jmenuje **neutrálně**, jako příklady kategorie „conventional
mobile operator". Nepřipisuje jim žádné jednání ani názor; věta „Vodafone
could provide some sites" je výslovně **hypotéza** („could"), ne popis
skutečnosti.

Vodafone a O2/Telefónica navíc v Německu **sdílení sítí už provozují**,
a studie Komise (kapitola 7) network sharing výslovně hodnotí jako jedno
z možných řešení — hypotéza tedy není technicky ani regulačně nemožná.

**Závěr: ✅ beze změny.** Právně ani věcně to není tvrzení o firmách.

---

## Co se nekontrolovalo, protože to není tvrzení

Řečnické a hodnotící věty, u kterých není co ověřit:
„It is practically a fossil" (S08), „Today, a teenager would probably
describe that as a network outage" (S17), „Some of us knew no better"
(S18), „That's rather useful" (S29), „A smartphone from 2021 is already
old by 2026 standards" (S72 — subjektivní hodnocení, ne údaj),
„machines have a very annoying habit" (S23), „And here's where it gets
strange" (S52).

**Vizuály se ověří zvlášť**, až vznikne storyboard — CLAUDE.md žádá fact
check i na obrázky. U tohohle videa jsou riziková tři místa:

1. **eCall (S28, S29)** — nesmí ukazovat konkrétní značku vozu.
2. **Operátoři (S48)** — nesmí použít jejich loga; „EU LEGACY" na
   displeji modemu je fiktivní název a musí být vidět, že je to návrh.
   **Vyřešeno:** S49 zavádí legendu čárkování (*„dashed = a proposal, not
   a service you can buy"*) a říká *„OUR NAME FOR A THING THAT DOESN'T
   EXIST"*; S50 nese pohled zařízení a S58 *„nobody is building this"*.
3. **Studie Komise (S53, S54, S57)** — pokud se ukáže dokument, musí to
   být ten skutečný, ne naše překreslení vydávané za něj (CLAUDE.md,
   provider `eurlex`). Číslo **64 milionů** patří do obrazu jen v té
   podobě, v jaké ho uvádí zdroj.
