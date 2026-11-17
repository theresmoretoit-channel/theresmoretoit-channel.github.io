# Fact check — Why We May Not Be Able to Live Forever

Ověřeno 2026-08-29 proti `script.md` v0.1 (78 scén). Metoda podle CLAUDE.md:
vypsáno **každé** ověřitelné tvrzení, ne jen ta, která vypadala riziková.

Legenda: ✅ ověřeno · ⚠️ platí s výhradou · ❌ opraveno ve scénáři

---

## Páteřní číslo videa: 156 let

**Zdroj (primární):** Efimov E., Fedotov V., Malaev L., Khrameeva E. E.,
Kriukov D.: *Somatic mutations impose an entropic upper bound on human
lifespan.* **npj Aging 12, článek 116 (2026), publikováno 25. června 2026**,
open access. https://www.nature.com/articles/s41514-026-00421-6
Pracoviště: Skolkovo Institute of Science and Technology a AIRI, Moskva.

Doslovně z abstraktu:

> „post-mitotic cells such as neurons and cardiomyocytes act as critical
> longevity bottlenecks, with somatic mutations reducing **median lifespan**
> from a theoretical non-aging baseline of 1759 years to **156 years**. In
> contrast, proliferating tissues like liver maintain functionality for
> thousands of years through cellular replacement (…) Multi-organ integration
> predicts median lifespans of **146–194 years**."

### S32 „a median human lifespan of roughly a hundred and fifty-six years"

❌ **Opraveno.** Původní scénář psal *„The model estimated a **maximum**
human lifespan of roughly 156 years."* Paper mluví o **mediánu**, ne o maximu
— což je věcně jiné tvrzení a zároveň silnější. Přidána scéna S33, protože
bez ní by divák slovo „median" přeslechl a rozdíl by zmizel.

**Formulaci S33 přepsal uživatel 2026-08-29 a je to důležitá oprava.** První
znění bylo *„Median, not maximum. Half of us would still be alive at a
hundred and fifty-six."* — to se ale dá číst jako **predikce o skutečné
populaci**, tedy že polovina lidí se opravdu dožije sto padesáti šesti let.
Model přitom počítá hypotetický svět, ve kterém jsou všechny ostatní
mechanismy stárnutí odstraněné. Platné znění:

> Median, not maximum.
> In the model, half of the population
> would reach beyond a hundred
> and fifty-six years.

„In the model" nese tu výhradu přesně tam, kde vzniká, a *„reach beyond"*
je zároveň korektní definice mediánu. Cena je jedna slabika navíc a mírně
menší úderovost.

Stojí za zapamatování, **čím ta chyba byla**: statisticky bylo první znění
v pořádku (medián je opravdu hodnota, pod kterou je polovina), takže by
prošlo každou kontrolou čísla. Vadná byla **modalita**, ne aritmetika —
věta o výstupu modelu se tvářila jako věta o světě.

Poznámka: **novinové články to popletly taky** (Newsweek, WION i IBTimes
píší „maximum age of 156"), takže tahle chyba je v původním scénáři
pochopitelná — přišla ze sekundárních zdrojů. Tím spíš patří do evidence:
CLAUDE.md má „sekundární zdroj neunese zobecnění" mezi pastmi.

### S05 „a limit somewhere around a hundred and fifty years"

✅ **Ponecháno záměrně — rozhodl uživatel 2026-08-29.** Vypadá to jako
nesrovnalost (v úvodu „around 150", v odhalení „156"), ale není:

- 150 je zaokrouhlení mediánu 156 a **tiskové zprávy k té studii samy mluví
  o 150** (Skoltech press, The Print: „150 years might be the limit").
- Vícetkáňový model dává **146–194**, takže „kolem sto padesáti" sedí i tam.

- 156 **je** přibližně 150, takže o faktickou chybu nejde v žádném čtení.

A hlavně je to **dramaturgicky lepší než sjednotit**: divák dostane v úvodu
číslo, které čeká, a v S32–S33 zjistí, že jeho první interpretace byla
špatná — nejdřív se zpřesní na 156, hned nato se převrátí význam
(*„Median, not maximum."*). Kdyby v úvodu stálo rovnou 156, ten dvojitý
obrat by zmizel a zbylo by opakování téhož čísla.

### S38–S40 „a heart is a pump… the brain is the one place…"

❌ **Doplněno, protože scénář studii nepřesně přisuzoval.** Původní text
odvozoval limit **jen z mozku**. Paper jmenuje **dvě** post-mitotické tkáně:
neurony **a kardiomyocyty**. Vynechat srdce by znamenalo tvrdit o studii něco,
co v ní není.

Přidané scény ten problém zároveň řeší ve prospěch oblouku videa: srdce je
pumpa a transplantuje se dnes běžně, kdežto mozek je jediné místo, kde
výměna součástky znamená výměnu informace. Tím se úhel „problém je mozek"
neztrácí, jen se stává doloženým.

Podpůrné číslo (ve scénáři není, je jen pro komentáře): obnova kardiomyocytů
je podle 14C datování **~1 % ročně u mladých a pod 0,5 % ve stáří**
(Bergmann et al., Science 2009), tedy „skoro post-mitotická" — kdežto
kortikální neurony jsou podle téže metody **staré jako sám člověk**
(Spalding et al., Cell 2005; citlivost metody je 1 %).

### S34 „does not mean there is a biological timer"

✅ **Odpovídá primárnímu zdroji, a to doslova.** Abstrakt sám říká:
*„This substantial yet incomplete reduction indicates that somatic mutations
significantly drive aging but **cannot alone account for observed
mortality**."* Scénář tuhle výhradu měl už od uživatele — je to jeho
nejsilnější místo a je správně.

---

## Biologie stárnutí

| # | Tvrzení (scéna) | Ověření | |
|---|---|---|---|
| 1 | mozek má „roughly eighty-six billion neurons" (S22) | Azevedo et al., J Comp Neurol 2009: **86,1 ± 8,1 mld.** neuronů a 84,6 ± 9,8 mld. neneuronálních buněk, isotropní frakcionátor, **n = 4** mužské mozky (50, 51, 54, 71 let). Číslo bylo v Brain 2025 zpochybněno a v témže časopise obhájeno („Yes, the human brain has around 86 billion neurons") | ✅ |
| 2 | „the lining of our intestines can renew itself incredibly quickly" (S08) | životnost střevní epitelové buňky **3–5 dní** | ✅ |
| 3 | „our skin renews itself" (S08) | obnova epidermis řádově **28–45 dní** | ✅ |
| 4 | „our blood cells are constantly replaced" (S08) | erytrocyt **~120 dní** | ✅ |
| 5 | „most neurons stay with us for decades" (S27) | 14C datování: kortikální neurony jsou staré jako člověk sám (Spalding 2005). Výhrada: **hipokampální neurogeneze u dospělých je sporná** — scénář ji ale netvrdí ani nepopírá, píše „most" | ⚠️ |
| 6 | senescentní buňky = „stop working properly, but don't die" (S11) | odpovídá definici buněčné senescence; jeden z hallmarks of aging | ✅ |
| 7 | epigenetické změny = „change the way they switch genes on and off" (S12) | odpovídá; *epigenetic alterations* je hallmark (López-Otín et al. 2013, rozšířeno 2023) | ✅ |
| 8 | výčet příčin stárnutí: poškození DNA, mitochondrie, odpad v buňkách, senescence, epigenetika, kmenové buňky (S10–S12, S16–S17) | všech šest je mezi **hallmarks of aging**; scénář nic nevymýšlí ani nepřidává | ✅ |
| 9 | „we could even make some cells biologically young again" (S02) a „reset some of the epigenetic changes" (S17) | **částečné přeprogramování Yamanakovými faktory je skutečné, ale na zvířatech**: Ocampo et al., Cell 2016 (cyklické 4F u progeroidních myší); Lu et al. — OSK přes AAV u 124týdenních myší prodloužilo zbylý medián o 109 %; cyklické OSK u neuronů zlepšilo paměť (Commun Biol 2024). U člověka terapie **není** | ⚠️ |

Výhrada u bodů 9 je **v pořádku i tak**, protože scénář je uvádí v podmiňovacím
způsobu („imagine that science gets really good at this"). Kdyby se kdy
přeformulovaly na oznamovací větu, přestanou platit.

---

## Umělé srdce bez tepu (S39b, S39c) — doplněno 2026-08-30

Uživatel navrhl doplnit, že člověk už žil s umělým srdcem bez tepu a
s ovládáním zvenčí, a výslovně požádal o ověření a zpřesnění. Ověřeno:

| tvrzení ve scénáři | doklad | |
|---|---|---|
| „People have lived with an artificial heart that has no pulse at all" | **Craig Lewis**, 55 let, Texas Heart Institute, **10. 3. 2011**. Billy Cohn a Bud Frazier mu vyňali srdce a nahradili je dvěma spojenými **kontinuálními** čerpadly. Bez tepu, bez křivky na EKG. Novější případ: **BiVACOR** (titanové srdce s magneticky levitovaným rotorem, jedna pohyblivá součást) | ✅ |
| „its speed set from outside the body" | otáčky se nastavují na **externí řídicí jednotce** — obsluhou nebo lékařem. U SynCardie umí jednotka i pulzní režim, kterým se dá „digitální tep" vyrobit schválně, aby fungoval tlakoměr a pulzní oxymetr | ✅ |
| „Not for long. Weeks, sometimes months." | Lewis přežil **asi pět až šest týdnů**; zemřel na selhání ledvin a jater, protože **amyloidóza postihla i ostatní orgány** — ne kvůli selhání čerpadla. BiVACOR: Australan ve čtyřicátých letech vydržel **105 dní** mezi implantací a transplantací a byl **první na světě propuštěn s ním z nemocnice** (únor 2025). SynCardia: medián podpory **96 dní** u 196 pacientů za dvacet let | ✅ |
| „And not without complications." | ano; všechny tyhle případy jsou **most k transplantaci**, ne trvalé řešení | ✅ |
| „But the principle held. Their blood kept moving, and they were still themselves." | tohle je **interpretace, ne měřený údaj**, a je záměrně opatrná: netvrdí, že to funguje dlouhodobě, jen že oběh šel udržet bez tepu a že to člověka nezměnilo. To je přesně ten rozdíl, na kterém stojí S40 | ⚠️ |

### Čemu se scénář vyhnul

Uživatel mluvil o „dálkovém ovládání". **Rozhlasové dálkové ovládání to
není** — je to externí jednotka spojená kabelem přes kůži. Scénář proto
říká *„its speed set from outside the body"*, což je doložitelné, a ne
„remote control", což by bylo přehnané.

Zdroje: Texas Heart Institute / NPR a ABC News k případu Craig Lewis 2011;
CNN a Jerusalem Post k BiVACOR 2025; PMC (20letá série 196 pacientů)
a FDA P030011 k SynCardii.

## Aritmetika

### S47 „replacing one percent of your neurons every year"

❌ **Opraveno na „a different one percent".** Původní věta plus závěr
*„After one hundred years, none of your original neurons would remain"*
platí jen při **systematickém** postupu, kdy se každý rok bere jiné procento.
Při náhodném výběru zbyde 0,99¹⁰⁰ = **36,6 %** původních neuronů, tedy víc
než třetina — a tvrzení „none would remain" by bylo nepravdivé.

Loď Théseus se takhle myslí vždycky, takže šlo o formulaci, ne o myšlenku;
jedno slovo díru zavírá. Je to přesně ten typ chyby, který komentář najde.

### S63 „At forty, twenty years of experience. At sixty, perhaps forty."

✅ Konzistentní — implikuje start ve dvaceti, což scénář o dvě věty dřív
sám zavádí („something we don't have at twenty").

### S03 „an eighty-year-old could have the body of a forty-year-old"

✅ Hypotéza, ne tvrzení o světě. Nic k ověření.

---

## Co ověřovat nešlo

- **„How long can we keep a human being human?"** (S76) a celá pasáž
  o osobní identitě je filozofie, ne fakt. Scénář to sám přiznává
  (*„we're no longer talking only about biology"*), takže nehrozí, že by
  se to četlo jako doložené tvrzení.
- **Analogie s operačním systémem** (S13–S15) je výslovně označená za
  analogii a scénář ji sám relativizuje (*„our bodies aren't computers"*).

---

## Obrázky

`storyboard.json` hotov (77 scén, 71 diagramů / 6 SDXL / **0 archivních**).
Nulový archiv znamená, že **licenční evidence pro tohle video nevzniká** —
`sources.json`, `CREDITS.md` ani `LICENSES.md` nemají co obsahovat.

Tři tvrzení v obrazech, která musí sedět stejně jako text:

| scéna | co obraz tvrdí | doklad |
|---|---|---|
| S05, S32, S33, S34, S72 | křivka přežití s mediánem v 156 | výstup modelu, ne data — proto je v obraze **povinná cedulka MODEL** a v S33 nápis IN THE MODEL. Poučení z S39 třetího videa: vypadalo to jako graf, a nebyl |
| S05 | křivka u 156 **neklesá k nule** | 156 je medián, takže tam křivka protíná **padesát procent**. Původní návrh storyboardu měl „klesá k nule kolem 156" a tvrdil by pravý opak toho, co S33 opravuje |
| S33 | medián nakreslený jako **dělení osy Y**, ne plochy | spočítáno: plochy pod křivkou přežití vlevo a vpravo od mediánu jsou v poměru **18,4 : 1**, ne 1 : 1. „Dvě stejné plochy" by byla věcná chyba v obraze |
| S08, S21, S27, S38 | doby obnovy tkání a to, že neurony mezi ně nepatří | řádky 2–5 tabulky výš (střevo 3–5 dní, kůže ~28–45, erytrocyt ~120) a Spalding 2005 pro neurony |
| S38 | post-mitotické jsou **dvě** tkáně, srdce i mozek | abstrakt npj Aging doslova („neurons and cardiomyocytes") |
| S22 | číslo 86 000 000 000 | Azevedo 2009. **Nekreslit 86 miliard bodů** — bylo by to nečitelné i nepravdivé |
| S72 | křivka pokračuje za 156 | přerušovaně, protože je to hypotéza scénáře, ne výstup modelu |

### ✅ S74: vyřešeno bez rozšíření fact checku

Diagram měl původně ukázat tři historické „nepřekonatelné meze", které
někdo překonal. Scénář ale žádnou nejmenuje (*„technology has a strange
habit…"*), takže by je **přidal obraz** a začal dělat faktickou práci,
kterou text nedělá — tatáž vada jako u S39 třetího videa.

**Uživatel zvolil abstraktní variantu** (2026-08-29): řetěz
`LIMIT → prasklina → LIMIT posunutý dál → …`, bez jmen, roků, ikon
technologií a postav. Tím obraz ilustruje přesně to, co text říká, a
**fact check se kvůli němu nemusí rozšiřovat o nic, co pro argument není
potřeba**.

Zásada, kterou to zavádí a která platí pro celý storyboard:

> Divák má z obrazu pochopit myšlenku, ale nemá z něj získat **fakta navíc**.
