# Fact check — It Still Works. So Why Upgrade It?

Verze `script 0.2.md`, 63 scén. Ověřeno 2. 9. 2026.

Video je **z velké části záměrná fikce** (Water 2.0, Chair 6, Enterprise
Extended Chair Support) a scénář to sám říká — *„Now let's make this
ridiculous."*, *„Completely absurd."* Ověřitelných tvrzení je proto málo,
zato je na nich postavená pointa: **vtip o Enterprise Extended Chair
Support se v S24–S28 překlopí ve skutečnost.** Kdyby ta část neseděla,
padá s ní celý střed videa.

Přehled:

| | scény | závěr |
|---|---|---|
| 1. Konec podpory Windows XP | S24 | ✅ 8. 4. 2014 |
| 2. Cena Custom Support | S25 | ✅ 200 → 400 dolarů za stroj |
| 3. Smlouva britského veřejného sektoru | S26 | ✅ 5,548 mil. £ na 12 měsíců |
| 4. Neprodloužení a stroje na místě | S27 | ✅ doloženo primárně |
| 5. Vypínání 2G | S09 | ✅ viz osmnácté video |
| 6. Telefon z roku 2008 funguje | S05 | ⚠️ jako přístroj ano, v síti hůř |
| 7. Přísloví o kovářově kobyle | S41–S43 | ✅ obojí doloženo |
| 8. Audit najde nepodporovanou technologii | S32 | ✅ PCI DSS 4.0, 12.3.4 |
| 9. Výměna oleje auto nezrychlí | S35 | ✅ triviálně |
| 10. Fikce, která se za fakt nevydává | S11–S23, S39 | ✅ označená ve scénáři |

---

## 1. Windows XP skončil v podpoře 8. dubna 2014 — S24

> „When Windows XP ran out of support in 2014, Microsoft sold exactly
> that deal."

**Ověřeno primárním zdrojem.** Dopis Department of Health a Crown
Commercial Services NHS organizacím z **8. dubna 2014** mluví o přístupu
k aktualizacím *„beyond 8 April 2014 for XP, Office 2003 and Exchange
2003"*.

Zdroj: [DH and Cabinet Office Microsoft XP update, 8. 4. 2014](https://assets.publishing.service.gov.uk/government/uploads/system/uploads/attachment_data/file/314721/DHandCabinetOfficeMicrosoftXPupdate8April14.pdf) (PDF, gov.uk)

## 2. Custom Support: dvě stě dolarů za stroj, druhý rok dvojnásobek — S25

> „Custom support. Around two hundred dollars per machine for the first
> year. Double that for the second."

**Ověřeno.** Microsoft cenu Custom Support Agreement těsně před koncem
podpory srazil na **200 dolarů za zařízení se stropem 250 000 dolarů**;
při obnově v dubnu 2015 stoupla na **400 dolarů za zařízení**.

| | první rok | druhý rok |
|---|---|---|
| cena za zařízení | **200 $** | **400 $** |
| strop | 250 000 $ | — |

> **Pozor na dvě věci, které do scénáře nepatří a do obrazu už vůbec ne.**
>
> **a) Těch 200 dolarů je SNÍŽENÁ cena.** Do března 2014 byly CSA
> podstatně dražší; Microsoft je zlevnil pár dní před vypnutím podpory.
> Scénář říká „around two hundred dollars", což platí pro stav v dubnu
> 2014 — ne pro celou historii programu.
>
> **b) Cenu za stroj NESMÍ diagram vynásobit britskou smlouvou.**
> To jsou dva různé ceníky: 200 $/stroj je katalogová cena CSA, kdežto
> 5,548 mil. £ je hromadná smlouva vyjednaná pro celý veřejný sektor
> (CCS uvádí úsporu **přes 20 mil. £ proti standardnímu ceníku**).
> Vydělením by vyšel nesmyslný počet strojů. Scénář ta dvě čísla
> nespojuje a **obraz je nesmí spojit taky** — viz pravidlo „diagram
> tvrdí i to, co v popisku není".

Zdroj: [Microsoft to double price of XP's post-retirement support](https://www.computerworld.com/article/1640632/microsoft-to-double-price-of-xps-post-retirement-support.html) (Computerworld)

## 3. Britský veřejný sektor: 5,5 mil. liber na jeden rok — S26

> „The British public sector signed it. Five and a half million pounds
> for one more year of security updates."

**Ověřeno.** Smlouvu vyjednala **Crown Commercial Service** (obchodní
agentura Cabinet Office) pro **centrální státní správu i širší veřejný
sektor**, na **dvanáct měsíců** do 14. 4. 2015, a kryla **Windows XP SP3,
Office 2003 SP3 a Exchange 2003 SP2**.

| | |
|---|---|
| hodnota | **5,548 mil. £** |
| doba | 12 měsíců, do 14. 4. 2015 |
| kryje | XP SP3, Office 2003 SP3, Exchange 2003 SP2 |
| vyjednal | Crown Commercial Service |
| pro koho | státní správa, samospráva, školy, NHS |

> **Prameny se rozcházejí v jedné číslici:** Computer Weekly, Silicon
> i shrnutí CCS uvádějí **5,548 mil. £**, The Register **5,584 mil. £**.
> Je to zjevná záměna dvou číslic a **na scénář to nemá vliv** — obě se
> zaokrouhlují na „five and a half million pounds". Do obrazu se přesné
> číslo psát nemá; když ano, tak 5,548 (převažující údaj).

Scénář říká „the British public sector", ne „the government" — to je
přesnější, protože účast byla dobrovolná a smlouva byla k dispozici celému
veřejnému sektoru, ne uložená shora.

Zdroje: [Government signs £5.5m Microsoft deal](https://www.computerweekly.com/news/2240217389/Government-signs-55m-Microsoft-deal-to-extend-Windows-XP-support) (Computer Weekly), [Microsoft in 1-year Windows XP survival deal with UK govt](https://www.theregister.com/2014/04/03/whitehall_microsoft_winxp_security_lifeline/) (The Register)

## 4. O rok později neprodloužili a stroje tam pořád byly — S27

> „A year later they decided not to renew. And the old machines were
> still there."

**Ověřeno primárním zdrojem** — blog Government Technology (gov.uk),
22. 5. 2015:

> „The Technology Leaders met last month and took a collective decision
> to **not extend the support arrangement for 2015**."

> „We expect **most remaining government devices using Windows XP** will
> be able to mitigate any risks, using the CESG guidance."

Druhá věta dokládá obojí naráz: neprodloužili **a** stroje tam pořád byly.
Že to byl od začátku záměr, potvrzuje i dopis z dubna 2014 — *„there are
no plans to negotiate a further national extension of XP support beyond
April 2015"*.

Zdroj: [Update on the customer support agreement for Windows XP](https://governmenttechnology.blog.gov.uk/2015/05/22/update-on-the-customer-support-agreement-for-windows-xp/) (gov.uk)

### ⚠️ WannaCry do tohoto bloku ZÁMĚRNĚ nepatří

Nabízí se dopsat, že v roce 2017 zasáhl NHS ransomware — příběh by se tím
uzavřel. **Je to ale rozšířený omyl.** Nákaza se šířila drtivou většinou
přes neaktualizované **Windows 7**, ne přes XP; na XP se útok obvykle
zhroutil místo šíření. Scénář proto končí u „neprodloužili a stroje tam
pořád byly" a **žádnou příčinnou souvislost s WannaCry netvrdí**.

Platí to i pro obraz: **žádná časová osa nesmí vést od roku 2015 k roku
2017**, protože šipka je tvrzení o příčině.

## 5. „2G is going away" — S09

> „Imagine a device that uses a 2G mobile network. (…) Then the operator
> announces: 2G is going away."

**Ověřeno** a doloženo podrobně ve `factcheck.md` osmnáctého videa
(`why-is-2g-still-everywhere`, kapitola 8): Deutsche Telekom **červen
2028**, Vodafone Německo **září 2028**, O2/Telefónica **druhá polovina
2028**; GSMA eviduje 131 sítí naplánovaných k vypnutí do roku 2030.

Scénář žádné datum ani operátora nejmenuje, takže tvrdí jen to, co je
doložené s velkou rezervou.

## 6. „A phone from 2008 can still work." — S05

> ⚠️ **Platí jako přístroj, ne nutně jako telefon.**

Zapnout se dá; volat už ne vždy — v zemích, kde je 2G i 3G vypnuté,
telefon z roku 2008 bez VoLTE hovor nesestaví. Scénář říká *„can still
work"* v řadě s Windows XP a dvacetiletým autem, tedy o **funkčnosti
přístroje**, a hned v S07 to sám vyvrací (*„it's a property of your
software and everything around it"*). **Není to chyba, je to setup** —
S09 na tomtéž telefonu ukazuje, že mu chybí svět kolem.

Kdyby to mělo v obraze být explicitní, musí být vidět, že přístroj se
rozsvítí, ale síť chybí — ne že telefon „funguje".

## 7. Přísloví: kovářova kobyla i ševcovy děti — S41 az S43

> „The blacksmith's horse goes barefoot." (…) „English usually tells it
> about the cobbler's children, who have nothing on their feet."

**Obojí ověřeno.** Jde o mezinárodní přísloví, které si každý jazyk
obsadil jiným řemeslem:

| jazyk | podoba |
|---|---|
| angličtina (základní) | *the shoemaker's children go barefoot*, *the cobbler's children are the worst shod* |
| **čeština** | **kovářova kobyla chodí bosa** |
| španělština | *en casa de herrero, cuchillo de palo* (kovář, dřevěný nůž) |
| portugalština, galicijština | rovněž kovář |

Wiktionary uvádí českou variantu **jmenovitě** v seznamu ekvivalentů.
Scénář tedy nic nepřekrucuje: *blacksmith's horse* je doslovný převod
české podoby a S43 poctivě dodává, jak to říká angličtina.

Zdroj: [the shoemaker's children go barefoot](https://en.wiktionary.org/wiki/the_shoemaker's_children_go_barefoot) (Wiktionary)

## 8. „It fails when the security audit comes back with a finding." — S32

**Ověřeno na konkrétní normě.** PCI DSS v4.0, požadavek **12.3.4**, žádá
revizi hardwaru a softwaru **aspoň jednou za dvanáct měsíců** včetně
analýzy, že technologie *„continue to receive security fixes from vendors
promptly"*, evidence oznámení o konci životnosti a **plánu na nápravu
schváleného vedením**.

Nepodporovaná technologie tedy není jen riziko — je to **nález v auditu**
u každého, kdo zpracovává platební karty. Scénář normu nejmenuje a nemá
proč; tvrzení je ale doložitelné, ne dojmové.

Zbylé tři způsoby selhání v S32–S33 (rozhraní partnera, obraz u hostingu,
nábor) jsou **obecná pozorování z praxe**, ne statistika, a scénář je tak
i formuluje — výčtem „it fails when…", ne číslem. Do obrazu proto nesmí
přijít graf ani procento.

## 9. „Changing the oil… the car doesn't get faster." — S35

Triviálně pravdivé a scénář z toho nedělá technické tvrzení; je to
metafora údržby.

## 10. Co je fikce a scénář to říká sám

| prvek | scény | jak je označený |
|---|---|---|
| Water 2.0 / Water 1.0 | S11–S13 | *„Now let's make this ridiculous."* |
| Chair 6, Chair 8, výrobce židlí | S16–S20 | *„Let's make it even more ridiculous."* |
| Enterprise Extended Chair Support | S21–S22 | *„Completely absurd."* |
| „dependency from 2014" v dialogu | S39 | scénka, ne případ |
| dvacetiletá firma z S01 | S01 | *„Imagine a company…"* |

**Žádný z nich se nevydává za skutečnost** a scénář u každého bloku sám
říká, že si vymýšlí. Jediné místo, kde se fikce a skutečnost potkávají,
je S23 → S24 (*„But replace 'chair' with 'software'… Except this part is
not a joke."*) — a právě tam navazuje doložený blok o XP.

> Mimochodem, řádová kalibrace vtipu sedí: fiktivní „several million
> a year" za náhradní kolečka a skutečných 5,5 mil. £ za rok záplat jsou
> **totéž číslo**. Nadsazené to není.

---

## Co se ve v0.2 nezměnilo kvůli fact checku

Nic. Blok S24–S28 vznikl už ve v0.1 rovnou z ověřených údajů (dohledáno
před zapsáním, ne po něm), takže fact check jen doplnil primární zdroje
a dvě varování pro obraz:

1. **nenásobit** 200 $/stroj britskou smlouvou (kap. 2),
2. **nekreslit šipku** z roku 2015 na WannaCry 2017 (kap. 4).
