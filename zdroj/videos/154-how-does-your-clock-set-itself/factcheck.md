# Fact check — 154 How Does Your Clock Set Itself?

Ověřeno 2026-11-11 nad scénářem **v0.4** (`script 0.4.md` = `script.md`). Pořadí bodů 1–8 podle
`zpetna vazba 0.4.txt`, pak zbytek scénáře po scénách.
**Primárně** = viděl jsem text dokumentu, **sekundárně** = encyklopedie, tisk, návody, **uživatel** = doložil
uživatel (notes.md), **z paměti** = neověřeno zdrojem v tomto průchodu, **výpočet** = odvozeno.

Zdroje:
- [PTB, DCF77 time code](https://www.ptb.de/cms/en/ptb/fachabteilungen/abt4/fb-44/ag-442/dissemination-of-legal-time/dcf77/dcf77-time-code.html) — primárně (bity, parita, A1/A2, „information for the following minute")
- METAS, *CCTF 2012 report from METAS (CH)*, TAI/12-21, září 2012 (BIPM, working document ID 9465) — primárně (HBG)
- [Meteotime, novinky](https://www.meteotime.com/en/) — primárně (výpadek 30. 6. a 30. 7. 2026)
- [Wikipedia DCF77](https://en.wikipedia.org/wiki/DCF77) — sekundárně (start Meteotime 22. 11. 2006, rozložení bitů, dosah)
- [PTB News 03/2 *PTB time service prolonged*](https://www.ptb.de/cms/en/presseaktuelles/journals-magazines/ptb-news/ptb-news-ausgaben/archivederptb-news/news03-2/ptb-time-service-prolonged.html) — primárně (dosah ~2 000 km)
- BIPM, 28. CGPM, Resolution 5 — uživatel; sekundárně [Euronews 16. 10. 2026](https://www.euronews.com/next/2026/10/16/global-timekeeping-rules-change-leap-second-scrapped-from-2027), [lilting.ch](https://lilting.ch/en/articles/leap-second-abolition-adopted-cgpm); [BIPM CGPM 2022 Resolution 4](https://www.bipm.org/en/cgpm-2022/resolution-4)
- NIST SP 432 / WWVB — uživatel

## Body ze zpětné vazby k v0.4

### 1. S18–S20 — rozložení bitů, BCD, pořadí číslic — **OK**
PTB: minuty, hodiny, den, den v týdnu, měsíc a rok se posílají v **BCD**, rok jen posledními dvěma číslicemi.
P1 kryje **7** bitů minut, P2 **6** bitů hodin, P3 **22** bitů data (primárně). Rozpad (sekundárně, Wikipedia)
a kontrola součtem (výpočet):

| bity | co | |
|---|---|---|
| 21–24 / 25–27 | minuty: jednotky 1-2-4-8 / desítky 10-20-40 | 4 + 3 = **7** ✓ |
| 28 | P1 | |
| 29–32 / 33–34 | hodiny: jednotky / desítky 10-20 | 4 + 2 = **6** ✓ |
| 35 | P2 | |
| 36–41 | den v měsíci 4 + 2 | |
| 42–44 | den v týdnu 1 = pondělí … 7 = neděle | 3 |
| 45–49 | měsíc 4 + 1 | |
| 50–57 | rok 4 + 4 | 6 + 3 + 5 + 8 = **22** ✓ |
| 58 | P3 | |

- *Most numbers are sent digit by digit* — ve skutečnosti **všechna** čísla; den v týdnu je jediná číslice.
  „Most" je tedy opatrnější než nutno, ale nepravdivé není. **Nechat.**
- *Forty-seven … a four and a seven* — BCD ✓. **Pořadí na drátě je od nejnižšího bitu:** jednotky minut
  (bity 21–24, váhy 1-2-4-8) jdou **před** desítkami. Scénář pořadí neříká, takže je to jen pokyn pro
  storyboard: **v diagramu minut je sedmička vlevo (dřív) a čtyřka vpravo**, a bity uvnitř číslice taky od
  váhy 1. Kdyby se kreslilo „čtyřka, pak sedmička" a 8-4-2-1, diagram by tvrdil opak signálu.
- S19 *Four bits … tens of minutes … only three* ✓ (4 bity pokryjí 0–15, desítky minut 0–5 vystačí se 3).
- S20 *year gets just two digits* ✓ (PTB: „the last two digits").

### 2. S22–S25 — parita „po každém bloku" — **OK, s podmínkou pro storyboard**
PTB: P1 za minutami, P2 za hodinami, P3 za **celým datem** (den, den v týdnu, měsíc, rok jako jeden blok
22 bitů). Každý doplňuje skupinu na **sudý** počet jedniček ✓ (S23).
*After each block of numbers* je pravda, jen když „blok" = minuty / hodiny / datum. S17 ale vyjmenuje šest
čísel, takže divák si může představit šest paritních bitů. **Storyboard S22 musí ukázat právě tři bloky
a tři paritní bity** — pak text sedí beze změny.
S24–S25 (jedna chyba se pozná, dvě se vyruší) — vlastnost parity obecně ✓ (výpočet).

### 3. S35–S38 — Z1, Z2 a A1 — **OK**
PTB primárně: bity 17–18 = Z1, Z2; **SEČ: Z1 = 0, Z2 = 1, SELČ obráceně** ✓ (S35 *two bits*).
A1 (bit 16) je jednička **hodinu před změnou**: na jaře 01:00:16 až 01:59:16 SEČ, na podzim 02:00:16 až
02:59:16 SELČ ✓ (S36 *for a whole hour*).
S37: změna v EU poslední neděli v březnu a v říjnu (směrnice 2000/84/ES, z paměti) ✓.
S38 podmíněné budoucí, ✓.
**Ukázka telegramu ve storyboardu:** vysílání v minutě 01:58:00–01:59:00 SEČ v neděli 29. 3. 2026 nese čas
**01:59** (oznámení na příští minutu), A1 = 1, Z1 = 0, Z2 = 1 — leží uvnitř intervalu PTB 01:00:16–01:59:16,
takže je jednoznačná. **Nebrat minutu těsně u změny** (kód pro 03:00 SELČ), tam by se v diagramu muselo
řešit, k čemu patří Z1/Z2.

### 4. S41–S43 — bity 1–14 a Meteotime — **OK, jedna nepřesnost k rozhodnutí**
- PTB primárně: bity 1–14 jsou *primarily … for the purpose of public warning*, *in addition weather data
  … supplied by the Swiss firm Meteo Time GmbH*; dosavadní hodiny tím nejsou rušeny, ale data využít nemohou ✓
  (S42 *also*, *compatible weather stations*).
- **Od 2006** ✓ — sekundárně: Wikipedia, *since 22 November 2006*. Šifrováno, dekódování vyžaduje
  licencovaný čip (HKW, uživatel) ✓.
- S43 *whether it would rain on Thursday* — předpověď na čtyři dny pro 60 regionů z 90 (sekundárně, návod
  Conrad DV216NL) ✓, minulý čas ✓.
- **Výpadek:** Meteotime primárně: *2026-06-30 — since about 30 June 2026 at 18:00 CEST* je přenos přerušen;
  *2026-07-30 — transmission of forecast data still not possible*. **Novější zpráva na webu k 11. 11. 2026
  není**, takže výpadek podle všeho trvá. Obě data v notes.md sedí. **Před vydáním zkontrolovat znovu.**
- **Nepřesnost (S41):** *the first fourteen bits … aren't about time* — doslova bity 0–13 o čase nejsou,
  takže pravda. Jenže S42 říká, že **tytéž** bity nesou počasí, a bit 0 je značka začátku minuty (vždy 0),
  počasí nese **1–14**. Divák si toho nevšimne; technicky zdatný komentátor ano. Možnosti:
  (a) nechat, storyboard vyznačí bity 1–14 a bit 0 nechá zvlášť; (b) *And right after the start of every
  minute, / fourteen bits / aren't about time at all.* **Doporučuju (a)** — v obraze to bude správně a text
  není nepravdivý.

### 5. S45–S46 — fyzika šíření vs. „ve tři ráno méně rušení" — **S45 OK, S46 k rozhodnutí**
- S45: dlouhé vlny jdou **přízemní vlnou** a **prostorovou vlnou** odraženou od ionosféry. Ve dne vrstva D
  prostorovou vlnu tlumí, po setmění zaniká a odraz od vrstvy E (~90 km) zesílí, takže dosah v noci roste
  (z paměti, standardní učebnicová věc; PTB ~2 000 km platí pro obojí). Text je formulovaný opatrně
  (*that upper path changes*, *often carries further*) ✓.
- S46: že je v noci v domácnosti méně rušení, uvádějí návody výrobců jako **důvod** nočního příjmu (Conrad,
  sekundárně), měřený doklad nemám. Je to rozumné, ale kategorické (*fewer … are running*). Možnosti:
  (a) nechat; (b) **přidat jedno slovo**: *fewer machines, chargers and lights / are usually running nearby
  to drown it out.* **Doporučuju (b)** — odliší doložitelnou fyziku (S45) od běžné zkušenosti (S46).

### 6. S50 — osa tyče kolmo ke směru vysílače — **OK, podmínka pro storyboard**
Feritová anténa reaguje na **magnetickou** složku vlny. Ta je u přízemní vlny vodorovná a **kolmá ke směru
šíření**, takže maximum je, když tyč leží **napříč** směrem k vysílači, a nula, když na něj míří ✓
(fyzika, výpočet; Meinberg podle notes.md). *A weak signal can vanish completely* = nula směrové
charakteristiky ✓.
**Storyboard: šipka k vysílači a tyč musí svírat 90°** ve stavu „funguje" a 0° ve stavu „ztratí se".
Diagram, kde tyč míří na vysílač s fajfkou, by tvrdil opak.

### 7. S59 — klesající využití HBG — **OPRAVIT**
METAS primárně (zpráva pro CCTF 2012): *The Swiss government decided in 2009 that HBG would cease its
operation because the estimated costs of refurbishing of the antenna, built in 1932, were too expensive
**in regard to the number of users** of the HBG time service.* Konec provozu na konci 2011 ✓.
Doložený je tedy **malý počet uživatelů vzhledem k ceně**, ne jeho **pokles**. *fewer people used it* tvrdí
trend, který zdroj nemá. Možnosti:
(a) vypustit řádek (původní pokyn); (b) **změnit jedno slovo: *too few people used it*** — to METAS říká
doslova a zachová se trojice důvodů. **Doporučuju (b).**
*Its antennas needed replacing* ✓ (*refurbishing of the antenna, built in 1932*); *Swiss clocks could simply
listen to Germany* ✓ (Wikipedia: *the ease with which all existing users could switch to DCF77*; uživatel
z admin.ch).

### 8. S58 — ~2 000 km a „most of Europe" — **OK**
PTB News: *can be received by normal radio clocks within a radius of approx. 2000 km* ✓.
Vzdálenosti od Mainflingenu (výpočet po ortodromě, zaokrouhleno): Dublin 1 110, Helsinky 1 510, Athény 1 780,
Istanbul 1 840, Lisabon 1 900, Moskva 2 010 km — uvnitř nebo na hraně; mimo je Island (2 400) a sever
Skandinávie (Nordkapp 2 500).
*Most of Europe* sedí ✓. *From one site near Frankfurt* — Mainflingen, ~25 km jihovýchodně ✓.

## Ostatní scény

### S01–S05 — úvod — **OK**
Funkce radiohodin bez internetu, Wi-Fi a GPS ✓; *survives power cuts* — bateriové hodiny, po výpadku se navíc
znovu nastaví ✓. S04 *once every second … a single pulse* — kromě 59. sekundy, ta se vysvětluje v S12–S13 ✓.

### S06–S10 — DCF77, WWVB, modulace — **OK**
DCF77 Mainflingen u Frankfurtu, WWVB u Fort Collins v Coloradu ✓. Na začátku každé sekundy se nosná sníží
(na ~15 % amplitudy, sekundárně; scénář číslo neříká) ✓. **0,1 s = 0, 0,2 s = 1** (PTB primárně) ✓.

### S11–S15 — 59 bitů, chybějící pokles — **OK**
Sekundy 0–58 nesou bity, 59. sekunda pokles nemá a další pokles je začátek minuty (PTB) ✓.
Výjimka: v minutě s přestupnou sekundou je pokles v 59. sekundě a chybí až v 60. — scénář to neřeší a nemusí
(S39 *could have sixty-one seconds*).

### S16–S17 — co se vejde — **OK**
Minuta, hodina, den, den v týdnu, měsíc, rok (PTB) ✓.

### S21 — rušení motorem, nabíječkou, LED — **OK**
Spínané zdroje a LED žárovky jsou známý zdroj rušení na dlouhých vlnách (z paměti; FAQ výrobců) ✓.

### S26–S27 — víc minut, než se nastaví — **OK**
Že kontrolují víc po sobě jdoucích minut, je vlastnost přijímače (notes: *many clocks*) ✓. Několik minut,
při špatném příjmu déle ✓ (návody uvádějí 3–10 min).

### S28–S33 — zpráva je oznámení — **OK**
PTB primárně: *Each code emitted contains the information for the following minute.* Okamžik změny = začátek
sekundy 0 další minuty ✓. Příklad 10:47 → 10:48 ✓.

### S39–S40 — přestupná sekunda — **OK**
A2 (bit 19) je jednička hodinu před přestupnou sekundou; 59. značka se pak vyšle s 0,1 s a minuta má
61 sekund (PTB primárně) ✓. Poslední přestupná sekunda 31. 12. 2016 23:59:60 UTC ✓ (z paměti, IERS;
lilting.ch: 27. a poslední). IERS Bulletin C 72: na konci 2026 nebude (sekundárně) ✓.
28. CGPM 15. 10. 2026, Resolution 5: souvislé UTC od 20. 5. 2027, rozdíl UT1−UTC až 3 600 s (uživatel,
sekundárně Euronews) ✓.
**Pro odpovědi v komentářích:** už 27. CGPM 2022 (Resolution 4) rozhodla, že se tolerance UT1−UTC zvýší
**nejpozději v roce 2035**; rok 2026 stanovil datum a mechanismus. *In October 2026 … decided to end leap
seconds* je tedy zjednodušení (konkrétní rozhodnutí s datem padlo 2026, záměr 2022), ne chyba. **Nechat.**
**Při vydání po 20. 5. 2027:** *will run* → *has run* (notes).

### S44 — jednou za noc — **OK**
Návody radiohodin uvádějí pokusy o příjem v časných ranních hodinách (typicky 1–3 h, někdy víckrát)
(sekundárně, Conrad) ✓, *many of them* ✓.

### S47–S48 — drift křemene — **OK**
Běžný spotřebitelský křemen ±0,5 s/den (≈ ±15 s/měsíc), levné hodiny při kolísání teploty víc (z paměti).
*can drift by a second or so a day* je horní odhad, řádově ✓.

### S49, S51 — feritová tyč, železobeton — **OK**
Anténa = feritová tyč s vinutím ✓. Železobeton stíní (výztuž) ✓.

### S52–S55 — PTB a cesium — **OK**
Čas pro DCF77 dodává PTB (národní metrologický ústav, atomové hodiny), vysílač provozuje Media Broadcast
(PTB, z paměti) ✓. Definice SI sekundy: ΔνCs = **9 192 631 770 Hz**, přechod mezi hladinami hyperjemné struktury
základního stavu cesia 133 ✓. *Radiation they give off* je populární zjednodušení „záření odpovídajícího
přechodu" (v hodinách atomy záření spíš pohlcují) — pro výklad přijatelné. **Nechat.**

### S56–S57 — zpoždění — **OK**
1 000 km / 299 792 km/s = **3,34 ms** → *about three milliseconds* ✓ (výpočet). Spotřebitelské hodiny zpoždění
nekorigují a ukazují sekundy ✓.

### S60 — Británie, Francie, Japonsko, Čína — **OK**
MSF (Anthorn, 60 kHz), ALS162 (Allouis, 162 kHz — uživatel), JJY (dvě stanice, 40 a 60 kHz), BPC
(Šang-čchiou, 68,5 kHz) (z paměti) ✓.

### S61–S63 — WWVB — **OK**
Fort Collins od 5. 7. 1963, časový kód od 1965 (uživatel) ✓. Snížení výkonu **0,2 s = 0, 0,5 s = 1,
0,8 s = značka** (uživatel, NIST) ✓. Značky v sekundách 9, 19, 29, 39, 49, 59 a 0 → **každých deset sekund**,
a 59 + 0 = dvě po sobě na začátku minuty ✓ (z paměti, NIST SP 432).

### S64–S66 — co se posílá — **OK**
DCF77 německý občanský čas SEČ/SELČ (uživatel, PTB Z1/Z2) ✓. WWVB UTC a den v roce 1–366 (uživatel) ✓.
USA má víc časových pásem ✓.

### S67 — „žádné dvě stanice nemluví stejně" — **OK, poznámka**
Formáty DCF77, MSF, WWVB, JJY a BPC se liší (JJY je WWVB podobný, ale s obrácenými pulzy). Dvě japonské
stanice ale vysílají **týž** formát — *none of these stations* je míněno po zemích, divák to tak přečte.
Vícepásmové hodiny umí víc formátů; scénář mluví o hodinách *built for Germany* ✓.

### S68–S69 — **OK**
*hundreds or thousands of kilometres* ✓, otázka bez faktu.

## Mimo scénář: rozpočet FY2019 (kandidát na návrat, rozhoduje uživatel)

NIST v rozpočtovém návrhu na FY 2019 (zveřejněno v srpnu 2018) navrhl *discontinue the dissemination of the
US time and frequency via the NIST radio stations in Hawaii and Fort Collins, Colorado* — tedy WWV, WWVH
i WWVB (sekundárně: [ARRL](https://www.arrl.org/news/nist-fy-2019-budget-would-eliminate-wwv-and-wwvh),
[SWLing Post](https://swling.com/blog/2018/08/nist-official-response-to-closure-questions)).
**~50 milionů hodin** synchronizovaných WWVB uvádí [NPR 25. 8. 2018](https://www.npr.org/2018/08/25/641835302/what-closing-a-government-radio-station-would-mean-for-your-clocks)
s odkazem na NIST — číslo je odhad, nezávislé sčítání neexistuje. Stanice vysílají dál (WWVB v provozu
k 2026, uživatel), návrh neprošel — **výsledek rozpočtu jsem primárně nedohledal**.
Kdyby se scéna vracela: *a budget proposal in 2018 suggested shutting it down* je doložené; *an estimated
fifty million clocks* jen jako odhad NIST. Dramaturgicky by to ale byla nová scéna, a scénář je zmrazený.

## Navržené změny ve scénáři (čekají na schválení)

| scéna | teď | návrh | proč |
|---|---|---|---|
| **S59** | *fewer people used it,* | ***too few people used it,*** | METAS: drahé *in regard to the number of users*; pokles nedoložen |
| S46 | *are running nearby to drown it out.* | *are **usually** running nearby to drown it out.* | oddělit zkušenost od fyziky (bod 5) |
| S41 | *And the first fourteen bits* | nechat (storyboard ukáže 1–14) | bit 0 je značka minuty |

## Pokyny pro storyboard z fact checku

- S18: minuty kreslit v pořadí na drátě — **jednotky (7) před desítkami (4)**, uvnitř číslice od váhy 1.
- S22: **tři** bloky (minuty | hodiny | datum) a **tři** paritní bity, ne šest.
- S35–S37: telegram s časem 01:59 SEČ v neděli 29. 3. 2026, A1 = 1, Z1 = 0, Z2 = 1.
- S41–S42: vyznačit bity **1–14**, bit 0 zvlášť jako značku minuty.
- S50: tyč **napříč** směrem k vysílači = příjem, **podélně** = ztráta.
