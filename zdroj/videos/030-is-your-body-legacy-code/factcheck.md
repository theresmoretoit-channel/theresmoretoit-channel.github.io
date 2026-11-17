# Fact check — 030 Is Your Body Legacy Code?

Proti `script 0.2.md` (105 scén). Ověřováno 2026-09-07, před storyboardem
na výslovnou žádost uživatele (`zpetna vazba 0.2.txt`).

Scénář je z velké části analogie, takže ověřitelných tvrzení je málo —
o to víc na nich stojí. **Dvě opravy, obě čísla, obě v exponovaném místě.**

| | scén s ověřitelným tvrzením | oprav |
|---|---|---|
| | 24 | **2** |

---

## ❌ 1. „Almost every cell" — v tomhle znění je to nepravda

**S07:** *„Almost every cell in your body contains essentially the same
complete copy of your genome."*

**Ověření.** Sender, Fuchs & Milo 2016 (PLoS Biology, referenční
sedmdesátikilový člověk) rozpočítává **3,0 · 10¹³ lidských buněk**:

| | buněk | podíl |
|---|---|---|
| červené krvinky | 2,5 · 10¹³ | **84 %** |
| krevní destičky | ~1,2 · 10¹² | ~4 % |
| **bez jádra celkem** | **2,6 · 10¹³** | **≈ 90 %** |
| **s jádrem** | **~3 · 10¹²** | **≈ 10 %** |

**Závěr: devět buněk z deseti v lidském těle nemá jádro, a tedy ani
genom.** Zralá červená krvinka jádro při dozrávání vypudí, destička
žádné nikdy neměla. „Almost every cell" je tedy doslova obrácené —
platí to pro **menšinu** buněk.

**Oprava (0.3):** doplnit jednu podmínku, ne novou sekci.

> Almost every cell in your body **that has a nucleus**
> contains essentially the same complete copy of your genome.

Pro **jaderné** buňky tvrzení platí; výjimky (gamety jsou haploidní,
lymfocyty si DNA přeskupují, somatická mozaika) pokrývá slovo
*essentially* a *almost*.

> **Kdyby se někdy chtělo víc, tady je ta munice** — nedávat do 0.3,
> uživatel řekl „žádná nová sekce": nejpočetnější buňka lidského těla
> **zahodila vlastní zdroják**, aby se do ní vešel náklad. To je přesně
> to WTF, na kterém stojí celé video, jen z opačné strany.

---

## ❌ 2. „billions of tiny agents" — o tři řády vedle

**S98:** *„There are billions of tiny agents"*

**Ověření.** Táž práce: **3,0 · 10¹³ = 30 bilionů** lidských buněk.
I kdyby se počítaly jen jaderné, je to **3 · 10¹² = 3 biliony**.
V obou případech **trillions**, ne *billions*.

**Oprava (0.3):** `billions` → **`trillions`**. Nahlásil uživatel
sám, měření to potvrzuje z obou stran.

> **Past pro překlad, ne pro scénář.** Anglické *trillion* je 10¹²,
> tedy česky **bilion**, německy `Billionen`, španělsky `billones`,
> polsky `bilion`, švédsky `biljon`. Nikoli „trillionů". Ve francouzštině
> a italštině je bezpečnější opis (*milliers de milliards*, *migliaia
> di miliardi*). Zapsáno, protože CLAUDE.md tuhle past eviduje
> a tohle je první video kanálu, kde na ni dojde.

---

## ⚠️ 3. „three billion characters" — platí, ale ne o buňce

**S01:** *„a computer program containing three billion characters
of instructions"*

**Ověření.** Kompletní haploidní sestava **T2T-CHM13 má 3,055 · 10⁹
párů bází** (bez chromozomu Y); GRCh38 ~3,1 · 10⁹. Tři miliardy tedy
sedí — **na jednu sadu**.

Somatická buňka je ale **diploidní**, takže nese **dvě** sady,
tj. ~6,2 · 10⁹ párů bází. (Plus mitochondriální DNA, 16 569 bp
v mnoha kopiích — proti jaderné zanedbatelné.)

**Závěr: beze změny.** Scénář říká, že *program* má tři miliardy znaků,
a pak že se *program* kopíruje do každého procesu. Obojí je správně;
nikde netvrdí, že buňka obsahuje tři miliardy znaků.

> **Volitelná jednoslovná úprava, kterou uživatel neschválil a já ji
> do 0.3 nedávám:** `S02` *„you copied the entire program into it."*
> → dopsat **`Twice.`** Je to fakticky přesnější (diploidie) a zároveň
> lepší vtip. Cena je jedno slovo v hooku, který má zůstat nedotčený —
> proto rozhodne uživatel.

Játra mimochodem tuhle přesnost ještě komplikují: **30–40 % lidských
hepatocytů je polyploidních** (binukleární 2 × 2n nebo mononukleární 4n)
a podíl s věkem roste. `S08` jmenuje *„A liver cell has it."* — obsah
kopie je týž, počet kopií ne. Slovo *essentially* to unese.

---

## ⚠️ 4. „ignored ninety-nine percent of it" — pravda jen v jednom čtení

**S04:** *„And then the process simply ignored ninety-nine percent of it."*

Tohle je nejzranitelnější místo scénáře, protože **dvě čtení dávají
opačný verdikt**:

| čtení | čísla | verdikt |
|---|---|---|
| **99 % ZNAKŮ genomu nekóduje bílkovinu** | kódující exony jsou **1–1,5 %** genomu | ✅ **pravda** |
| 99 % GENŮ buňka nepoužívá | z ~20 000 genů kódujících bílkovinu je „elevated" v aspoň jednom buněčném typu **76 %**; skutečných housekeeping genů ve všech 154 typech je **2 425** | ❌ **nepravda** |

**Závěr: beze změny**, protože scénář mluví o **znacích**, ne o genech —
`S01` zavádí *„three billion characters"* a `S04` říká *„ninety-nine
percent of **it**"*, tedy těch znaků. V tom čtení je to doložené.

Kolik genomu je *funkčních* je zvlášť spor: ENCODE 2012 tvrdil
**80 %** „biochemicky funkčních", Graur oponuje **~9 %** podle
evoluční konzervace. Ani jedno číslo scénář netvrdí a je dobře.

> **Připraveno na komentáře.** Pokud někdo napíše „to je nesmysl, buňka
> používá většinu svých genů", má pravdu **o genech** a scénář mluví
> **o znacích**. Odpověď je v téhle tabulce, ne v dohadování.

---

## ✅ Ověřeno bez výhrad

| tvrzení | scéna | doklad |
|---|---|---|
| gen nese informaci pro *„functional product, often a protein"* | S10, S11 | formulace je záměrně opatrná (*often*) a pokrývá i geny pro RNA, které bílkovinu nekódují |
| transkripční faktory se vážou na konkrétní sekvence DNA a ovlivňují, zda se gen přepíše | S21 | učebnicová molekulární biologie |
| regulační sekvence ovlivňují **kdy a kde** se geny exprimují | S22 | promotory, zesilovače |
| struktura chromatinu ovlivňuje **přístupnost** oblastí DNA | S22, S27 | euchromatin/heterochromatin; měří se ATAC-seq |
| buňky trvale přijímají signály z okolí | S23, S62 | chemické signály, hormony, mechanické síly, kontakt se sousedy |
| jaterní buňka nemusí neuronové geny mazat, stačí je regulovat | S28 | přesně tak; regulace exprese, ne delece |
| mutace, která buňce zlepší přežívání a množení **uvnitř organismu**, může přispět k rakovině | S58 | somatická klonální evoluce (Nowell 1976); je to doslova výběr na úrovni buněk proti zájmu organismu |
| commit history *„stretching back billions of years"* | S40, S44, S51, S102, S104 | nejstarší nesporné doklady života ~3,48 mld. let (Pilbara), sporné 3,7 mld. (Isua). „Billions" sedí |
| tělo běží nepřetržitě **desítky let** | S70 | triviálně |
| buňky umírají a vznikají, bílkoviny se tvoří a odbourávají, DNA se kopíruje, poškození se opravuje | S72, S73 | proteinový a buněčný obrat, systémy oprav DNA |
| tkáně → orgány → soustavy → organismus | S77 | standardní hierarchie |
| *„well enough to build eyes, hearts, immune systems, brains"* | S82 | ano |
| umíme sekvenovat genom, identifikovat geny, měřit bílkoviny | S90 | ano |
| **neumíme** vzít DNA z buňky, nahrát ji do počítače a spustit vývoj člověka | S91, S92 | ano — chybí úplný model vývoje, ne výpočetní výkon |

---

## Co scénář moudře NETVRDÍ

Zapsáno proto, aby se to při dalších úpravách omylem nedopsalo:

- **že gen = funkce jedna ku jedné.** `S10` říká *„very roughly"*
  a *„a function or a module"*. Alternativní sestřih, jeden gen → víc
  bílkovin, tím zůstává mimo.
- **že DNA je plán organismu.** `S85`–`S87` to naopak výslovně vyvrací.
- **kolik procent genomu je „junk".** Viz spor ENCODE vs. Graur výš.

## Jediná biologická výjimka, která analogii potvrzuje doslova

`S50` říká *„It doesn't refactor."* — a to je pravda **skoro** vždycky.
Vyvíjející se B a T lymfocyty ale **V(D)J rekombinací fyzicky přeskupí
vlastní genomovou DNA** a zralé B buňky ji pak somatickou hypermutací
dál mutují. Jsou to jediné lidské buňky, které **opravdu editují svůj
zdroják za běhu** — a dělají to proto, aby vyrobily rozmanitost, kterou
by dopředu naplánovat nešlo.

Do scénáře to **nepatří** (rozhodl uživatel: žádná nová sekce), ale je
to nejlepší odpověď na komentář typu *„a co imunitní systém?"*.

---

## Zdroje

- Sender R., Fuchs S., Milo R. (2016). *Revised Estimates for the Number
  of Human and Bacteria Cells in the Body.* PLoS Biology 14(8):e1002533.
  https://journals.plos.org/plosbiology/article?id=10.1371/journal.pbio.1002533
- Nurk S. et al. (2022). *The complete sequence of a human genome.*
  Science 376:44–53. https://www.science.org/doi/10.1126/science.abj6987
- Human Protein Atlas — housekeeping proteome.
  https://www.proteinatlas.org/humanproteome/tissue/housekeeping
- Nutman A. P. et al. (2016). *Rapid emergence of life shown by discovery
  of 3,700-million-year-old microbial structures.* Nature 537:535–538.
  https://www.nature.com/articles/nature19355
- ENCODE vs. Graur — spor o podíl funkčního genomu.
  https://plato.stanford.edu/archives/fall2023/entries/genomics/encode-project.html
- Chi X. et al. (2020). *V(D)J recombination, somatic hypermutation and
  class switch recombination of immunoglobulins.* Immunology 160:233–247.
  https://onlinelibrary.wiley.com/doi/full/10.1111/imm.13176
- Přehled polyploidie hepatocytů:
  https://pmc.ncbi.nlm.nih.gov/articles/PMC6592246/
