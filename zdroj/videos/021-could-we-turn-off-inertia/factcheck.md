# Fact check — Could We Make Acceleration Impossible to Feel?

Verze scénáře: `script 0.3.md` (= `script.md`), 70 scén.
Datum ověření: 2026-09-02, přečíslováno po škrtání 0.3.

Legenda: ✅ ověřeno · ⚠️ platí s výhradou · ❌ opraveno ve scénáři

---

## S05, S06 — devět G u stíhacího pilota

> „A fighter pilot wears a suit that squeezes the legs and the belly.
> And the pilot strains against the force the whole time." · „Together, that buys
> about nine times gravity. For tens of seconds."

**❌ opraveno.** První draft tvrdil, že oblek sám dá devět G a že to vydrží
„jen pár sekund". Obojí bylo špatně:

| | draft | doloženo |
|---|---|---|
| co dělá oblek | dá devět G | přidá **jen 1 az 2 G** |
| co dělá zbytek | — | **AGSM** (zatínání a dýchání) přidá ~4 G |
| jak dlouho | „pár sekund" | **NATO požaduje 9 G / 15 s**; naměřený průměr 31,6 s (rozsah 20 az 58 s) |

Rozklad, který se v literatuře uvádí: základní tolerance ~4,5 G + oblek ~1 G
+ AGSM ~4 G ≈ **9 G**. Oblek nafukuje vaky přes nohy a břicho, aby krev
nezůstala dole — proto „squeezes the legs and the belly".

Zdroje: [Sci. Reports, AGSM a G tolerance](https://www.nature.com/articles/s41598-020-78687-3),
[Unpredictability of fighter pilots' g duration tolerance (PubMed)](https://pubmed.ncbi.nlm.nih.gov/25945558/)

## S07 — bez obleku stačí pár G

> „Without that, a few times gravity is enough to drain the blood
> from your head. Your vision greys out. Then you black out."

**✅** Uvolněný netrénovaný člověk: **šeda (grey-out) při +3 az +4 Gz**,
**blackout kolem +4 az +4,5 Gz**, G-LOC (ztráta vědomí) kolem **+5 Gz**;
populační průměr pro zdravé jedince 4 az 6 Gz. Pořadí příznaků ve scénáři
(nejdřív šeda, pak mdloba) odpovídá popisu v literatuře.

Zdroje: [+Gz-induced loss of consciousness curve](https://link.springer.com/article/10.1186/2046-7648-2-19),
[SKYbrary: G-induced Impairment and the Risk of G-LOC](https://www.skybrary.aero/index.php/G-induced_Impairment_and_the_Risk_Of_G-LOC)

## S17–S22 — letecký simulátor

> „A flight simulator sits on six moving legs" · „The legs give it
> a metre or so of room" · „the simulator tilts backwards" ·
> „The inner ear cannot tell the difference"

**✅ / ⚠️ s výhradou u čísla.**

- **Šest noh:** Stewartova plošina (hexapod), šest nezávislých válců,
  šest stupňů volnosti. ❌ z draftu vypadlo slovo *hydraulic* — velké
  simulátory jsou dnes i elektrické, takže to bylo tvrzení navíc.
- **Metr místa:** ⚠️ číslo záleží na tom, co se měří. Předpis pro Full
  Flight Simulator žádá **zdvih válce 60 palců (1,52 m)**, ale svislý
  pohyb plošiny bývá jen **±300 mm**. „A metre or so of room" leží uvnitř
  toho rozpětí, ale přesné to není — proto ta vágní formulace.
  **Na pointu scény to nemá vliv**: ať je to půl metru nebo metr a půl,
  plošina nemůže zrychlovat dlouho.
- **Naklonění dozadu:** ✅ je to pojmenovaná a standardní technika,
  **tilt coordination**. Plošina se pomalu nakloní tak, aby složka
  gravitace nahradila trvalé zrychlení, které simulátor uskutečnit nemůže.
- **Vnitřní ucho rozdíl nepozná:** ✅ přímý důsledek toho, že otolity
  měří **měrnou sílu**, ne zrychlení. Tomu se říká **somatogravická
  iluze** a je to táž věc, která u skutečných letadel působí nehody
  při vzletu za tmy.

Zdroj: [Acceleration onset cueing (Wikipedia)](https://en.wikipedia.org/wiki/Acceleration_onset_cueing),
[Pilot Institute: Somatogravic Illusions](https://pilotinstitute.com/somatogravic-illusion/)

## S24 — jedno G je zhruba tíhové zrychlení

> „Suppose the vehicle accelerates at one G for just ten seconds." ·
> „That's roughly the acceleration of gravity."

**✅** Standardní tíhové zrychlení je definičně **9,806 65 m/s²**.

## S25 — po deseti sekundách o ~350 km/h rychleji

> „the vehicle would be moving about three hundred and fifty kilometres
> per hour faster than before."

**✅ přepočítáno, nevzpomínáno.**

    Δv = g · t = 9,80665 × 10 = 98,07 m/s = **353,0 km/h**

„About three hundred and fifty" sedí (chyba 0,8 %).

## S26, S27 — sedačka by ujela skoro pět set metrů

> „your seat would have to move almost five hundred metres" ·
> „a seat rail almost half a kilometre long"

**✅ přepočítáno.**

    s = ½ · g · t² = ½ × 9,80665 × 100 = **490,3 m**

Obě formulace („almost five hundred metres", „almost half a kilometre")
jsou správně a obě jsou správným směrem — skutečnost je **pod** uvedeným
číslem, takže „almost" platí doslova.

## S32, S33 — reakce musí něco přijmout

> „If you push the passenger forward, something else has to receive
> the corresponding reaction."

**✅** Třetí Newtonův zákon. Scéna netvrdí nic silnějšího — správně
uzavírá, že jde o **boj s inercí**, ne o její odstranění.

## S37–S50 — volný pád a princip ekvivalence

> „In free fall, you feel nothing at all." · „Astronauts do not float
> because gravity is gone. They float because they are falling
> continuously." · „It gives every part of you the same acceleration."
> · „Einstein built general relativity on exactly that observation."

**✅ všechny čtyři.**

- Kosmonauti na oběžné dráze ISS jsou stále v tíhovém poli Země
  (ve výšce ~400 km je tíhové zrychlení pořád kolem **89 %** hodnoty
  na povrchu). Neváží nic proto, že padají — nikoli proto, že by
  gravitace zmizela. Beztížný stav je **volný pád**, ne nepřítomnost tíže.
- Pocit „tlaku" je **mechanické napětí uvnitř těla**: sedačka působí
  na styčné ploše a síla se musí přenést kostrou a tkání. Gravitace
  působí na každý element hmoty úměrně jeho hmotnosti, takže vnitřní
  napětí nevznikne a není co snímat.
- Einstein: **1907**, „nejšťastnější myšlenka mého života" — *„pro
  pozorovatele padajícího ze střechy domu gravitační pole neexistuje"*.
  Z toho vyrostl princip ekvivalence a pak obecná relativita.

**⚠️ formulace se ve verzi 0.3 změnila právě kvůli fyzikální
napadnutelnosti.** Recenzent u 0.2 upozornil, že „every atom ... at the
same moment" se dá sestřelit ze dvou stran, a má pravdu v obou:

| námitka | proč sedí |
|---|---|
| **konečná rychlost šíření** | gravitace se šíří rychlostí světla, takže „at the same moment" je tvrzení o **současnosti**, které navíc není invariantní vůči volbě soustavy |
| **slapové síly** | pole není homogenní, takže „every atom" dostane přesně totéž jen v idealizaci |

Nová formulace obojímu uhýbá, a přitom neztrácí pointu:

> **It gives every part of you the same acceleration.**

To je doslova **slabý princip ekvivalence** (setrvačná hmotnost = tíhová),
tedy věta, kterou fyzik podepíše. Neříká nic o čase, takže rychlost šíření
není ve hře; a neříká „exactly", takže slapová odchylka ji neporušuje.

Táž oprava proběhla o dvě scény dál: „act on every atom at once" →
**„accelerate every part of you by the same amount"** (S49).

**Kolik ta slapová odchylka dělá:** v pozemském poli se tíhové zrychlení
mezi hlavou a chodidly liší relativně o **5,7 · 10⁻⁷**, tedy zhruba
o půl miliontiny (2h/R pro h = 1,8 m; absolutně 5,5 · 10⁻⁶ m/s²). Proto „the same acceleration" v měřítku lidského těla
není zaokrouhlení, ale prakticky rovnost. U černé díry by to neplatilo —
scéna o ní ale nemluví.

Zdroj: [Einstein's Happiest Moment: The Equivalence Principle (arXiv 2209.13781)](https://arxiv.org/abs/2209.13781)

## S52 — hmota a energie zakřivují prostoročas

> „In Einstein's general relativity, gravity is not really a force.
> Matter and energy curve spacetime, and things move through that curve."

**✅** Standardní formulace obecné relativity. Důležité je, že scéna říká
**„matter and energy"**, ne jen „matter" — pravá strana Einsteinových
rovnic je tenzor energie a hybnosti, takže energie zakřivuje taky.

## S57 — umíme měřit, neumíme ovládat

> „We can measure gravity with extraordinary precision. We can even
> detect gravitational waves from colliding black holes. But we have
> no technology that can turn it down."

Ve verzi 0.3 jsou původní tři scény (S81–S83) sloučené do jedné,
takže se obě dřívější položky fact checku slévají taky.

**Detekce gravitačních vln: ✅** LIGO, **GW150914**, událost ze
14. září 2015, oznámená v únoru 2016. Splynutí dvou černých děr.
Od té doby řádově stovky událostí.

**Neumíme ji ovládat: ✅** Gravitační pole se dá vytvořit jen hmotou
a energií a nedá se stínit ani obracet. Žádný experiment nedoložil
jinou cestu.

## S58 — graviton

> „We don't even know whether gravity has a quantum particle at all." ·
> „Physicists call it the graviton." · „Nobody has ever detected one."

**✅ platí i k dnešnímu dni**, ale stojí za poznámku, že se ta otázka
zrovna teď hýbe:

- Graviton **nebyl detekován** a kvantová teorie gravitace není potvrzená.
- Dlouho se mělo za to, že detekce jednoho gravitonu je **principiálně
  nemožná**. To se změnilo: práce z roku 2024 (Pikovski a kol.,
  *Nature Communications*) ukázala, že podpis jednotlivých gravitonů
  v gravitační vlně detekovat **lze**, a na Stevens Institute of
  Technology se staví první takový detektor.
- Scénář tím není zasažený — tvrdí „nobody has ever detected", což platí.

> **Zvažováno a ZAMÍTNUTO uživatelem u verze 0.3.** Nabízel jsem přidat
> tu novinku jako beat naděje („a právě teď se staví první detektor").
> Uživatel to odmítl s tím, že oblouk videa je *pocit zrychlení →
> kompenzace → proč je nepraktická → změna setrvačnosti → proč gravitace
> nabízí jinou cestu → časoprostor → sci-fi tlumič → mezihvězdné
> cestování*, a „mimochodem možná už stavíme detektor gravitonu" by ho
> rozbilo. Kdyby se ten výzkum měl někdy zmínit, tak **jednou větou
> v závěru**, ne novým beatem.

Zdroje: [Sci.News: Physicists Begin Building First-Ever Graviton Detector](https://www.sci.news/physics/graviton-detector-14489.html),
[Stevens Institute of Technology](https://www.stevens.edu/news/building-the-worlds-first-graviton-detector)

## S64 — zrychlovat až na zlomek rychlosti světla

> „You could keep accelerating. And accelerating. And accelerating.
> Until the spacecraft reaches a significant fraction of the speed
> of light."

**✅** Scéna žádné číslo neuvádí, takže se dá jen ověřit, že tvrzení
není přehnané. Při vlastním zrychlení jednoho G:

| doba (čas Země) | rychlost |
|---|---|
| 100 dní | **0,27 c** |
| 1 rok | **0,72 c** |

Relativisticky, `v = at / √(1 + (at/c)²)`. „Significant fraction of the
speed of light" je tedy spíš podhodnocené než nadsazené.

**⚠️ co scénář záměrně neřeší:** energii. Tlumič inerce chrání cestující,
ale loď pořád někdo musí roztlačit, a to je samostatná a nevyřešená
překážka. Scénář to nikde netvrdí jinak — S65 mluví o **přežití**
zrychlení, ne o pohonu — takže to není chyba, jen otevřené místo.

---

## Homografy

Seznam z CLAUDE.md (`read, lead, live, wind, tear, close, record, present,
object, subject, contract, conduct, minute, wound, bow, row, use, used,
refuse, separate, moderate, invalid, desert, content, produce`):
**nula výskytů** v celém scénáři. Kontrolováno strojově.

## Číslice a pravopis

- Číslic ve scénáři **nula** — všechno slovy.
- Britský pravopis: opraveno `kilometers → kilometres`, `meters → metres`,
  `kilometer → kilometre`, `behavior → behaviour`. Ověřeno strojově,
  že už žádný americký tvar ze sledovaného seznamu nezbyl.
- Výpustky (`...`) se ve scénáři nevyskytují, takže nehrozí záměna za `…`.
