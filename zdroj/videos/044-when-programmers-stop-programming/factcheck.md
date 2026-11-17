# Fact check — 044 When Programmers Stop Programming

Ověřeno proti `script 0.2.md`, opravy jsou ve `script 0.3.md`.
ID scén jsou v číslování **0.3**.

**Výsledek: 21 tvrzení, z toho 2 věcné chyby, 1 nedoložitelné tvrzení
a 1 nepoužitelné srovnání.** Všechno opraveno; co zbylo, je níž
i s tím, co ho drží.

---

## ❌ CHYBA 1 — „FORTRAN arrived three years later" (S14)

| | |
|---|---|
| **tvrzeno** | tři roky po zprávě z 10. 11. 1954 |
| **naměřeno** | první překladač dodán zákazníkům **v dubnu 1957**, tedy za **2 roky 5 měsíců** |
| **opraveno na** | *„FORTRAN arrived two and a half years later."* |

Vyšlo to i líp: přesnější číslo je působivější než zaokrouhlené nahoru.

## ❌ CHYBA 2 — cíl COBOLu (S15, S16)

| | |
|---|---|
| **tvrzeno** | *„so that people who were not programmers could read the programs"* a *„the whole point of COBOL was that a human could read it"* |
| **doloženo** | z jednání v Pentagonu 28.–29. 5. 1959: účastníci se shodli, že **programovat by mělo umět víc lidí** a že jazyk má **maximálně využít angličtinu**. Deklarované cíle: efektivní přenositelné programy, snadný přechod na nový systém, **vhodnost pro nezkušené programátory** |
| **co v záznamu NENÍ** | že cílem byla čitelnost pro **neprogramátory** nebo pro management. To je rozšířené, ale silnější tvrzení, než co je doložené |
| **opraveno na** | *„They agreed on two things. That more people should be able to program at all… and that the language should use as much plain English as possible."* a *„COBOL was shaped around what a human could read."* |

**Payoff videa to nebourá** — S58 a S67–S69 potřebují jen to, že jazyky
jsou tvarované kolem lidského čtenáře, a to doložené je.

Při té příležitosti opraveno i *„Five years after that"* (S15). Vázalo se
to na scénu o roce **1957**, takže by to ukazovalo na rok 1962. Teď je
tam **1959** natvrdo.

## ❌ NEDOLOŽITELNÉ — „And it sold" (S18)

O prodejích Martinovy knihy jsem nenašel žádný údaj. Škrtnuto; věta teď
začíná *„And the promise was exactly the one you have been hearing
this year."* Nic to nestálo.

## ⚠️ NEPOUŽITELNÉ SROVNÁNÍ — a tohle je nejdůležitější nález

Ve verzi 0.2 stálo: **„About a hundred and ten thousand people in America
have that title now. Fewer than in 1980."**

Obě čísla jsou pravdivá. **Dohromady je dát nejde.**

| číslo | odkud |
|---|---|
| 1980: „more than 300,000" | **Current Population Survey** (analýza Washington Post) |
| dnes: 110 800 | **Occupational Outlook Handbook / OES**, jiné šetření, jiná metodika |

A i kdyby se zůstalo u jednoho šetření, je v něm díra: **CPS přešel
v lednu 2003 na klasifikaci povolání z roku 2002 a BLS sám to popisuje
jako „a complete break in comparability at all levels of industry and
occupation aggregation".** Srovnání roku 1980 s dneškem přes ten zlom
tedy neobstojí — a přitom je to přesně ten titulek, který koluje
médii („lowest level since 1980").

> Reconciliovaná řada, kterou BLS pro roky 1983–99 vydal, **jde jen po
> hlavní skupiny povolání**, ne po jednotlivá. Pro „computer programmers"
> tedy čistá dlouhá řada neexistuje.

**Jak je to ve 0.3 vyřešené** — nikde se přes rok 2003 nesrovnává:

| scéna | tvrzení | zdroj |
|---|---|---|
| S20 | 1980 přes 300 000 → počátek 2000s přes 700 000 | **obojí PŘED zlomem**, tedy uvnitř jedné klasifikace |
| S21–S22 | v roce 2003 přibyl vedle „computer programmer" nový kód pro „computer software engineer" | klasifikace 2002 Census: 1010 vs 1020 |
| S22b | dnes 380 tis. programátorů a 2,25 mil. vývojářů | **CPS, tabulka 11, rok 2025** — jedno šetření, jeden rok |
| S23 | šest vývojářů na jednoho programátora | podíl z týchž dvou čísel |

**Pointa se tím nezeslabila, naopak.** Ve 0.2 to bylo „titulu ubylo".
Ve 0.3 je to doložený úřední akt: v roce **2003 statistický úřad tu
profesi rozdělil na dvě** a dnes je šest ze sedmi lidí na té druhé
straně. Přejmenování není metafora, má datum.

---

## ✅ Co prošlo

| scéna | tvrzení | doklad |
|---|---|---|
| S11 | první programátoři pracovali přímo ve strojových instrukcích, pak assembler, pak vyšší jazyky | pořadí je nesporné |
| S12 | **10. 11. 1954**, skupina v IBM, zpráva o systému jménem FORTRAN | naskenovaný originál, titulní strana: *Programming Research Group, Applied Science Division, IBM, November 10, 1954*, název *Specifications for The IBM Mathematical FORmula TRANSlating System* |
| S13 | **„strana dvě"** | ve skenu je citát na 3. listu; 1. list je titulní, takže tělo začíná na 2. listu a citát je na **tištěné straně 2** ✅ |
| S13 | *„Since FORTRAN should virtually eliminate coding and debugging…"* | **doslovný přepis** z téhož skenu |
| S13 | pokračování slibuje méně než poloviční náklad | celá věta: *„…it should be possible to solve problems for less than half the cost that would be required without such a system."* Ve scénáři je citát **useknutý na doslovnou část** a zbytek převyprávěný, aby se necitovalo nepřesně |
| S15 | 1959, výbor, jazyk pro byznys | CODASYL pojmenován 4. 6. 1959, specifikace COBOL 60 schválena 8. 1. 1960 |
| S17 | **1982**, James Martin, kniha *Application Development Without Programmers* | Prentice-Hall 1982, ISBN 0-13-038943-9 |
| S18 | šlo o generátory sestav a generátory aplikací, ne o roboty | obsah knihy: dotazovací jazyky nad databází, generátory aplikací a sestav, grafické nástroje |
| S22b | 380 tis. / 2,25 mil. | CPS tab. 11 (2025): computer programmers **381**, software developers **2 254** (v tisících) |
| S26–S27 | AI umí z popisu chování vyrobit databázi, backend, API, frontend, testy a dokumentaci | popis dnešní schopnosti, ověřitelný přímo |
| S49 | cedule „437 people" | **záměrná fikce**, ne tvrzení o skutečné lodi |
| S58 | Python, C#, PHP navrženy pro lidského čtenáře a pisatele | vlastnost vyšších jazyků, nesporná |
| S61 | 37 souborů, 4 821 / 1 734 řádků | **ilustrace**, převzatá z dodaného textu; netvrdí se, že jde o konkrétní commit |

---

## Co NEJDE ověřit a je to tak napsané

**S52: *„For decades that looked like the part the writers had not
thought about. It may turn out to be the part they got right."***
Je to čtení, ne tvrzení, a formulace to přiznává (*„may turn out"*).

**S50** — *„transporter"* nahrazen **life support**. Nebyla to věcná
chyba, ale slovo je značkově vázané na jeden konkrétní seriál, a to
je proti rozhodnutí nejmenovat konkrétní dílo.

---

## Jediná měkká noha, která zbyla

**S20: „In 1980… more than three hundred thousand" a „by the early 2000s,
more than seven hundred thousand."** Obě čísla mám ze **sekundárního
zdroje** (Fortune přebírající analýzu Washington Postu nad daty CPS).
Primární tabulku pro rok 1980 se mi najít nepodařilo — CPS podrobná
povolání v dostupných tabulkách začínají rokem 1983.

Proč to ve scénáři zůstalo: obě čísla jsou **ze stejného šetření a ze
stejné klasifikační éry**, takže to srovnání neporušuje nic z toho, co
padlo výš, a scénář je uvádí opatrně (*„more than"*). Kdyby se našel
primární zdroj, je to jednořádková oprava; kdyby se ukázal jako mylný,
scéna jde nahradit poměrem z roku 2025, který stojí sám.

## Zdroje

- Preliminary Report, IBM Programming Research Group, 10. 11. 1954 —
  sken Computer History Museum, `archive.computerhistory.org/resources/text/Fortran/102679231.05.01.acc.pdf`
- Backus et al., *The FORTRAN Automatic Coding System*, 1957
- BLS, *Occupational Outlook Handbook* — Computer Programmers; Software Developers, QA Analysts and Testers
- BLS, *Current Population Survey*, tabulka 11 (2025), `bls.gov/cps/cpsaat11.htm`
- BLS, *Historical comparability of occupation and industry data from the CPS*, `bls.gov/cps/cpsoccind.htm`
- Census 2002 Occupation Codes (1010 Computer programmers, 1020 Computer software engineers)
- Fortune, 17. 3. 2025, přebírá analýzu Washington Postu nad CPS
- James Martin, *Application Development Without Programmers*, Prentice-Hall 1982
