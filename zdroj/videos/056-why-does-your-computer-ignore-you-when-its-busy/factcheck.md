# Fact check — 056

> **Tenhle soubor je vázaný na `script 0.2.md`** (přečíslováno
> 2026-09-19 po tvém škrtání, ověřeno proti textu scén). Po každém dalším
> škrtu se musí přečíslovat znovu a strojově ověřit, že fragment z každého
> nadpisu v té scéně opravdu je — jinak evidence ukazuje na cizí tvrzení.

Ověřeno 2026-09-19. Zadání (`scenar-puvodni.md`) neobsahovalo **jediné
ověřitelné tvrzení** — všechno níž jsou kotvy dopsané do draftu, tedy
přesně ta místa, kde se dá udělat chyba.

---

## S05 — „your machine is dealing with thousands of hardware events every second"

**Ověřeno měřením na tomhle notebooku**, ne z literatury:

```
přerušení za 5 s: 31 628  =>  6 325 / s
průměrná zátěž: 0,17 (tedy prakticky nečinný stroj)
```

Zdroj: součet všech čítačů v `/proc/interrupts` ve dvou odběrech po pěti
sekundách. **Závěr: „thousands" je pravdivé a spíš konzervativní.**

> Slovo *thousands* je schválně neurčité. Konkrétní číslo by platilo
> pro tenhle stroj a tuhle chvíli, ne pro divákův počítač.

## S07 — „computers have worked this way since the 1950s"

Ve verzi 0.1 tu stálo *„the whole mechanism was invented in the 1950s"*.
**Sporné na tom není desetiletí, nýbrž prvenství** — všichni kandidáti
padnou do 50. let:

| | |
|---|---|
| UNIVAC 1103 / 1103A | bývá uváděn jako první s přerušením, ale **manuál z roku 1953 přerušení nepopisuje**; jiné prameny dávají 1103A, tedy 1956 |
| DYSEAC (NBS) | **1954**, bývá uveden jako první s přerušením od vstupu a výstupu |
| UNIVAC I (1951) | přetečení skočilo na opravnou rutinu — předchůdce, ne přerušení |

Souhrn: [Mark Smotherman, Clemson — History and Overview of Interrupt
Systems](https://people.computing.clemson.edu/~mark/interrupts.html),
[Wikipedia: Interrupt](https://en.wikipedia.org/wiki/Interrupt),
[Wikipedia: DYSEAC](https://en.wikipedia.org/wiki/DYSEAC).

**Závěr: desetiletí doložené je, slovo *invented* ne.** Proto je ve verzi
0.2 formulace *„computers have worked this way since the 1950s"* — drží
kotvu, ale netvrdí, kdo byl první. Konkrétní rok se uvést nesmí.

## S34–S44 — Mars Pathfinder, 1997  *(čísla scén beze změny)*

Nejsilnější kotva videa a jediné místo s vlastními jmény. Ověřeno proti
dobovému výkladu vedoucího softwarového týmu (Glenn Reeves, JPL):

| tvrzení ve scénáři | doklad |
|---|---|
| „In 1997, the Pathfinder lander touched down and started working" | přistání 1997, mise běžela |
| „Then, days later, it began resetting itself" | *„a few days into the mission, not long after Pathfinder started gathering meteorological data, the spacecraft began experiencing total system resets"* |
| vysoce prioritní úloha „moved data around the spacecraft" | **information bus task** — vysoká priorita, běhala často |
| „it needed a shared piece of memory" | *„an 'information bus'… a shared memory area used for passing information between different components"*, chráněná mutexem |
| nízkoprioritní úloha „collecting weather data" | **meteorologická úloha (ASI/MET)**, nízká priorita, běhala zřídka |
| „a medium priority task then took the processor" | **komunikační úloha**, střední priorita, dlouhoběžící |
| „A watchdog timer noticed… and reset the entire spacecraft" | *„a watchdog timer would go off, notice that the data bus task had not been executed for some time, conclude that something had gone drastically wrong, and initiate a total system reset"* |
| „It has a name. Priority inversion." | ano, učebnicový případ |
| „Engineers on Earth worked out why, and sent a fix up to Mars" | nahrán program v C, který přepnul proměnné z FALSE na TRUE a **zapnul dědění priority** u dotčených mutexů |

Zdroje: [Glenn Reeves — What really happened on
Mars?](https://www.cs.unc.edu/~anderson/teach/comp790/papers/mars_pathfinder_short_version.html),
[delší verze](https://www.cs.ccsu.edu/~pelletie/local/risks/programming-software/pathfinder.html),
[Wikipedia: Priority
inversion](https://en.wikipedia.org/wiki/Priority_inversion).

> **Co se do scénáře záměrně NEDALO:** vzdálenost Země–Mars ani doba
> přenosu. Je to táž past jako „four hundred million kilometres"
> k Jupiteru u prvního videa — číslo, které zní rozumně a nikdo ho
> nepřepočítá. „Sent a fix up to Mars" žádné číslo nepotřebuje.
>
> A **nepíše se, že šlo o první chybu na Marsu** ani o první inverzi
> priorit v dějinách. Obojí se po internetu opisuje a doložit se to nedá.

## S68 — „Windows puts that label on a window after about five seconds"  *(v 0.1 to byla S69)*

Doloženo **primárním zdrojem**, ne fórem:

> *„The operating system detects this state by attaching a timer to pending
> messages in the message queue. If a message has not been retrieved within
> 5 seconds, the DWM declares the window to be hung."*
>
> *„The operating system defines an application hang as a UI thread that has
> not processed messages for at least 5 seconds."*

Tamtéž je i doklad pro popis v S67 a S69: DWM původní okno schová
a nahradí je **duchem** — bitmapou posledního obsahu s dopsaným
*„Not Responding"* v záhlaví, se kterým jde jen hýbat, minimalizovat
a zavřít.

Zdroj: [Microsoft Learn — Preventing Hangs in Windows
Applications](https://learn.microsoft.com/en-us/previous-versions/windows/win32/win7appqual/preventing-hangs-in-windows-applications).

> Pět sekund v S68 je **totéž číslo** jako pět sekund v S09 („you still sat
> there for five seconds"). To je náhoda, ne souvislost — v S09 je to
> vymyšlená scéna, v S68 doložený práh. Kdyby to při poslechu vypadalo
> jako pointa, změň číslo v S09.

## S73 — „a new picture appears about every sixteen milliseconds"  *(v 0.1 to byla S75)*

Odvozeno, ne opsáno: 1 000 / 60 = **16,67 ms**. Platí pro obvyklých
60 Hz; proto *„on an ordinary screen"* a *„about"*. U 120 a 144 Hz
panelů je to 8,3 a 6,9 ms.

---

## Co ověřené NENÍ a čeká na finální scénář

Zbytek videa je popis mechanismu (přerušení, obslužná rutina, plánovač,
stránkování, fronta zpráv). Není v něm číslo ani jméno, takže se ověřuje
**jinak než tabulkou** — čte se, jestli tvrzení nezobecňuje přes rámec:

- **S26 „two named halves"** — horní a dolní polovina je linuxový pojem.
  Scénář ta jména schválně neříká, takže tvrdí jen tolik, že se práce
  dělí. Kdyby ses rozhodl jména dát do obrazu, platí to pro Linux, ne
  pro každý systém.
- **S48–S50** — „sto procent neznamená zamrzlé" platí pro běžný
  preemptivní plánovač. Nepíše se, který.
- **S59 Thrashing** — pojem je zavedený; kdyby padlo datum nebo jméno,
  musí se doložit.
- **S76 „It cannot guess what you meant"** — formulace vznikla obcházením
  homografu *read* (*„cannot read your mind"*); Kokoro čte `read`
  nespolehlivě, viz `CLAUDE.md`.

**A hlavně:** věty, které vznikly slitím nebo zkrácením dvou zdrojových,
patří do fact checku stejně jako věty přejaté — to je poučení z videa 032
(Great Filter zkrácený na sebezničení). Po tvém škrtání projdi i je.
