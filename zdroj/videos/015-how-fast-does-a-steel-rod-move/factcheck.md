# Fact check — Nothing Is Really Solid

Ověřeno 2026-09-01 proti `script 0.3.md` (80 scén, 1 228 slov).
Metoda podle CLAUDE.md: vypsat **každé** ověřitelné tvrzení, ne jen ta,
která vypadají rizikově. Čísla se počítají, nevzpomínají.

**Čísla scén platí pro v0.3.** Proti v0.1 se posunula dvakrát — škrty
v0.2 (redundance) a v0.3 (blok „matter looking at matter"), viz `notes.md`.
Tvrzení, která patřila k vyškrtnutému textu, jsou z tohoto dokumentu
odstraněna; zůstávají v `script 0.1.md`, kdyby se blok vracel.

Legenda: ✅ doloženo · ⚠️ platí, ale s výhradou · ❌ neplatí

**Souhrn: nula ❌.** Jedna ⚠️ opravena ve v0.2 („about" → „just over
three seconds"), jedna ⚠️ na podhodnocení („more than twice") ponechána
záměrně, a jedna terminologická past (rychlost zvuku v oceli — tyčová
versus objemová), kterou scénář shodou okolností řeší správně.

---

## S03–S05 — rychlost světla

### „Nothing can move faster than light." ⚠️

Platí pro **přenos informace a fyzikálního vlivu**. Fázová rychlost,
skupinová rychlost v disperzním prostředí, průsečík nůžek nebo světelná
skvrna na Měsíci mohou `c` překročit — nic z toho ale nenese signál.

Scénář si tuhle výhradu **sám doplňuje** v S58 přesnou formulací
*„Physical influences cannot propagate faster than light."* Věta v S03 je
lidový úvod, přesná verze přijde na místě, kde na ní záleží. Nechat.

### „Light would need just over three seconds to travel one million kilometres." ✅

Spočítáno: `c` = 299 792,458 km/s, tedy

    1 000 000 / 299 792,458 = 3,3356 s

> **Opraveno ve v0.2.** Zdrojový scénář říkal *„about three seconds"*,
> což je o **10 % nízko** — jediné číslo v celém scénáři, které nesedělo
> na dvě platné číslice. *„Just over three seconds"* je přesné a v S60
> („even light needs **just over** three seconds") nese pointu i o kus
> dál. Změna je na **obou** místech, S04 i S60.

---

## S06–S11 — mechanická vlna v oceli

### „Even steel isn't perfectly rigid." ✅

Jádro celého videa a v S58–S59 se to dokazuje z relativity.

### „When you push one end, you slightly compress the material." ✅

Hookův zákon; podélná deformace `ε = σ/E`.

### „Those atoms push on their neighbours … the disturbance travels through the material as a wave." ✅

Podélná (kompresní) elastická vlna. Standardní popis.

### „About five kilometres per second. That's roughly the speed of sound in steel." ✅

**Tohle je nejzáludnější číslo videa a scénář ho má správně.** V oceli
existují dvě různé „rychlosti zvuku" a liší se o 15 %:

| | vzorec | ocel (E = 200 GPa, ρ = 7 850 kg/m³, ν = 0,29) |
|---|---|---|
| **tyčová (bar, extensional)** | `√(E/ρ)` | **5 048 m/s** |
| objemová podélná (P-vlna) | `√(M/ρ)` | 5 778 m/s |
| Wikipedia, ocel A36 podélná | | 5 596 m/s |

Rozsah tyčové rychlosti přes běžné oceli (E 190–210 GPa,
ρ 7 750–8 050 kg/m³): **4 858 až 5 205 m/s**.

> **Slovo „roughly" přibylo ve v0.5** na návrh recenzenta. Bez něj věta
> tvrdila jedno číslo tam, kde jich je celé pásmo, a diskuse v komentářích
> by byla oprávněná. Teď je věta pravdivá pro tyčovou i objemovou
> rychlost a pro celý rozsah běžných ocelí.

Pro **dlouhou tenkou tyč**, o které video mluví, platí tyčová rychlost —
materiál se může do stran roztáhnout, takže je efektivně měkčí.
Wikipedia to formuluje jako „for long rods … where their diameter is
shorter than a wavelength". Vychází **5,0 km/s**, tedy přesně to, co
scénář říká.

> **Do komentářů se dá čekat „ale rychlost zvuku v oceli je 5 900!"**
> Odpověď: to je objemová podélná rychlost v neomezeném prostředí. Tyč
> o milionu kilometrů délky a rozumném průměru je učebnicový
> jednorozměrný případ a tam se počítá z Youngova modulu.

---

## S12–S14 — padesát pět hodin

### „At five kilometres per second … roughly fifty-five hours to reach the other end." ✅

    1 000 000 km / 5,000 km/s = 200 000 s = 55,56 h
    1 000 000 km / 5,048 km/s = 198 098 s = 55,03 h

„Roughly fifty-five hours" sedí pro obě hodnoty.

### „You push the rod on Monday morning … the other end doesn't start moving until Wednesday afternoon." ✅

Pondělí 08:00 + 55,0 h = **středa 15:01**.
Pondělí 08:00 + 55,6 h = **středa 15:33**.

Odpoledne v obou případech. Trefa i pro ranní start v 6:00 (středa 13:00)
i v 10:00 (středa 17:00).

---

## S18–S21 — tyč není jedna věc

### „A steel rod is, physically, an enormous collection of atoms interacting with one another." ✅

### „The atoms closest to your hand are pushed first. They move slightly." ✅

Popis mechanismu, který dává číslo z S11. Souhlasí.

### „The rod doesn't respond as one perfectly rigid object. It responds progressively." ✅

---

## S22–S26 — atom

### „atoms are not tiny steel balls." ✅

### „A tiny nucleus sits in the middle, surrounded by electrons." ✅

### „almost all of an atom's volume is not occupied by the nucleus" ✅

Spočítáno pro železo: poloměr jádra ≈ 1,75 fm, poloměr atomu ≈ 126 pm.

    poměr poloměrů  7,2 × 10⁴
    poměr objemů    2,7 × 10⁻¹⁵

Jádro zabírá **řádově biliontinu biliontiny procenta** objemu atomu.
„Almost all" je tedy obrovské podhodnocení, tedy bezpečné.

> **Pozor na obvyklý omyl, do kterého scénář naštěstí nespadl:**
> z toho NEplyne, že je atom „skoro prázdný". Objem atomu je vyplněný
> elektronovou vlnovou funkcí. Scénář to formuluje jako *„not occupied
> by the nucleus"*, což je přesné, a v S25 to sám dovysvětlí
> („you're not looking at … microscopic solid balls"). **Diagram to
> nesmí pokazit** — viz tabulka na konci.

---

## S27–S30 — co to drží pohromadě

### „The answer is mostly electromagnetism." ✅

Se slovem **mostly**, které je nutné — samotný elektromagnetismus
stabilitu hmoty nezaručí, viz S34. Bez toho hedgingu by tvrzení neplatilo.

### „Each positively charged nucleus interacts with negatively charged electrons." ✅

### „depending on the material, these interactions create different kinds of chemical bonding" ✅

Iontová, kovalentní, kovová, van der Waalsova, vodíkové můstky.

### „In metals, electrons can spread out across many atoms." ✅

Model volných elektronů / pásová teorie. Formulace **„is part of what
gives"** u metalické vazby je správně opatrná.

> **Termín „delocalised" se ve v0.5 přesunul do OBRAZU.** Recenzent
> správně namítl, že britsky je to jedno slovo (`delocalised`), jenže
> tak ho Kokoro čte jako „di-LOCK-a-lized" — a `de-localised`, které
> výslovnost opraví, vypadá v titulku jako překlep. Hlas proto říká
> prostý opis *„spread out across many atoms"* a odborný termín nese
> **diagram S30**, kde je napsaný správně. Obojí je tak správně tam,
> kde na tom záleží.

---

## S31–S37 — proč se atomy nesloučí

### „If atoms attract each other … why don't they simply collapse together?" ✅

Správně položená otázka; tohle je přesně **problém stability hmoty**.

### „Move them even closer … the energy rises very rapidly. The electron clouds begin to overlap." ✅

Odpudivá větev Lennard-Jonesova (resp. Born-Mayerova) potenciálu.

### „quantum mechanics prevents identical electrons from occupying the same quantum states." ✅

**Nejsilněji doložené tvrzení videa** a zároveň místo, kde se
popularizace nejčastěji plete. Že stabilita hmoty stojí na vylučovacím
principu, a ne na samotném elektrostatickém odpuzování, je **dokázaná
věta**, ne názor:

| | |
|---|---|
| Dyson & Lenard, 1967–68 | první důkaz stability hmoty |
| Lieb & Thirring, 1975 | kratší důkaz přes Lieb-Thirringovu nerovnost |

Bez vylučovacího principu by energie soustavy `N` elektronů a `K` jader
nebyla zdola omezená úměrně `N + K` a pevná látka by neexistovala.

Scénář drží správnou dělbu: elektromagnetismus **váže** (S27), vylučovací
princip **brání zhroucení** (S34). To je ta věcně správná verze.

> **„prevents" místo „strongly resists" je změna z v0.5** a je to
> zpřesnění, ne zjemnění: vylučovací princip dvěma totožným fermionům
> týž stav skutečně **zakazuje**, není to další odpudivá síla mezi
> mnoha. Původní formulace to svedla číst jako „ještě jedna síla navíc".

### „So matter has an equilibrium … There is a preferred arrangement." ✅

Rovnovážná meziatomová vzdálenost, mřížková konstanta.

---

## S38–S39 — atomy stojí na místě jen zdánlivě

### „The atoms in a solid aren't frozen in place. They're constantly moving." ✅

Tepelné kmity kolem rovnovážných poloh (fonony). Platí **i při absolutní
nule** — zbývají kmity nulového bodu, takže formulace nemá výjimku,
kterou by komentář našel.

---

## S40–S46 — dotek

### „There isn't a microscopic wall made of perfectly touching little balls." ✅

### „quantum mechanics prevents the atoms from simply passing through each other … a force that stops your hand" ✅

Kontaktní (normálová) síla. Táž fyzika jako S34 — a scénář ji správně
vede na Pauliho, ne jen na „elektrostatiku". Viz doklad u S34.

> **Přeformulováno ve v0.5.** Původní *„their quantum states cannot
> simply overlap arbitrarily"* bylo pro divácké video moc abstraktní
> a zároveň to nebyl přesný popis toho, co drží stůl. Nová dvojice vět
> říká totéž srozumitelněji a fyzikálně stejně poctivě.

### „Your hand interacts with the atoms in the material. The material pushes back." ✅

---

## S47–S52 — dá se to zrychlit?

### „Different materials have different sound velocities." ✅

### „Steel is around five kilometres per second." ✅

Viz S11.

### „Diamond can exceed ten kilometres per second." ✅

**Ve v0.5 se z ⚠️ stalo ✅.** Původní *„more than twice as fast"* bylo
pravdivé, ale podhodnocené a záviselo na tom, kterou hodnotu si divák
najde. *„Exceed ten kilometres per second"* platí u **všech** citovaných:

| zdroj | diamant | přesahuje 10 km/s? |
|---|---|---|
| Wikipedia, „speed of sound" | 12 000 m/s | ✅ |
| Trachenko a kol. 2020 | ~18 000 m/s | ✅ |
| `√(E/ρ)`, E = 1 050 GPa, ρ = 3 515 | 17 284 m/s | ✅ |
| podélná v [111] | ~18 600 m/s | ✅ |

Rozptyl 12 az 18,6 km/s zůstává v **diagramu** jako pásmo, protože je
skutečný — ale scénář už netvrdí poměr, který by šlo rozporovat.

> **Věta o dalších materiálech byla ve v0.5 vypuštěna.** Říkala
> *„Some other extremely stiff materials can transmit mechanical
> disturbances even faster."* — doložitelné (grafen v rovině 19,9 az
> 21,3 km/s), ale dramaturgicky generické a po *„Could we make that
> faster?"* to byla už třetí várka čísel. **S vypuštěním mizí i jediné
> místo, kde se video opíralo o dvourozměrný materiál**, takže je fact
> check o jeden zdroj jednodušší. Diagram S51 proto grafen taky
> nekreslí.

### „But none of them are infinitely fast. And that's not just an engineering limitation. It's fundamental." ✅

**Doloženo silněji, než scénář tuší.** Existuje horní mez rychlosti zvuku
v kondenzované látce plynoucí přímo z fundamentálních konstant:

    v_u = α · √(mₑ / 2mₚ) · c ≈ 36 100 m/s

kde `α` je konstanta jemné struktury. Trachenko, Monserrat, Pickard,
Brazhkin, *Speed of sound from fundamental physical constants*,
Science Advances **6** (41), eabc8662 (2020).

Mez je asi **dvojnásobek** diamantu a je to zhruba **0,012 % `c`**.
Tvrzení „it's fundamental" tedy platí dokonce dvakrát: jednou přes
relativitu (S58–S59) a podruhé přes tuhle mez.

> **Do videa se to nedostane** (scénář o tom nemluví a dopisovat autorovi
> věty se nemá), ale **do popisku a do odpovědí v komentářích ano** —
> je to nejlepší dostupná odpověď na „a co kdyby byl materiál ještě
> tužší".

---

## S53–S59 — dokonale tuhé těleso

### „You could use the rod to transmit information. Push the rod. One." ✅

Standardní myšlenkový experiment. Binární kanál.

### „If the other end responded instantly, you would have a way to transmit information instantaneously." ✅

Zákaz nadsvětelného **přenosu signálu**; v jiné inerciální soustavě by
odpověď předcházela příčinu.

### „So a perfectly rigid object cannot exist in our universe." ✅

Standardní důsledek speciální relativity — dokonale tuhé těleso
by muselo mít nekonečnou rychlost zvuku. Souvisí s Bornovou tuhostí:
i „tuhý" pohyb je v SR silně omezený (Herglotz-Nötherova věta).

### „Perfect rigidity would require instantaneous communication between different parts of the object." ✅

---

## S60–S62 — i světlo potřebuje čas

### „Even light needs just over three seconds to cross that distance." ✅

3,3356 s, viz S04. **Obě místa jsou opravená stejně** — kdyby se jedno
vracelo na „about", musí se vrátit obě.

---

## S63–S66 — rekapitulace řetězu

### „Mechanical waves led us to atoms. Atoms led us to electromagnetism." ✅

Odpovídá skutečnému postupu videa. Nic navíc netvrdí.

---

## S67–S71 — co je „solid"

### „‚solid' is really a macroscopic description of how an enormous number of particles behave together" ✅

Emergentní vlastnost. Standardní pohled fyziky kondenzovaných látek.

### „when billions upon billions of these interactions work together" ✅

Podhodnoceno, tedy bezpečné. Dřevěná deska 1,2 × 0,7 × 0,03 m
o hustotě 600 kg/m³ váží 15 kg a má **řádově 10²⁷ atomů**, tedy asi
10¹⁸ krát víc než „miliarda miliard". Idiom, ne číslo.

---

## S72–S75 — týž zákon dělá stůl i ruku

### „The same physical laws that make the table solid also make your hand solid." ✅

### „Your brain receives electrical signals. It processes them." ✅

Mechanoreceptory (Merkelovy disky, Meissnerova a Pacciniho tělíska)
převádějí deformaci kůže na akční potenciály.

---

## Co z fact checku plyne pro DIAGRAMY

Kapitola „Diagram tvrdí i to, co v popisku není" z CLAUDE.md. Čtyři místa,
kde by kresba mohla tvrdit něco, co scénář neříká:

| scéna | past | jak se jí vyhnout |
|---|---|---|
| **S23, S24** | atom nakreslený jako **planetární model** s elektrony na drahách tvrdí zastaralou fyziku, kterou scénář o dvě věty dál vyvrací | elektronový obal jako **rozostřený oblak / hustota pravděpodobnosti**, nikdy jako kuličky na kroužcích. V `sdxl.negative` je proto `orbiting electron shells, solar system atom model` |
| **S24** | „jádro zabírá skoro nic" svádí nakreslit **prázdný** atom | prázdné místo NENÍ prázdné — obal se musí kreslit vyplněný, jinak obraz tvrdí „atom je z 99,9999 % vakuum", což scénář v S25 popírá |
| **S34** | šipka „Pauli → odpuzování" plnou čarou vedle šipky „elektromagnetismus → odpuzování" tenkou tvrdí pořadí důležitosti, které scénář nestanoví | obě stejnou vahou; scénář říká „mostly electromagnetism" o **vazbě** a Pauliho o **odporu proti stlačení** — to jsou dvě různé role, ne soupeři |
| **S50** | sloupcový graf rychlostí svádí nakreslit jednu hodnotu pro diamant | pásmo, ne sloupec — rozptyl 12 až 18,6 km/s je součást tvrzení („depending on the direction and type of wave") |

---

## Zdroje

- Trachenko, Monserrat, Pickard, Brazhkin: *Speed of sound from
  fundamental physical constants*, Science Advances 6(41), eabc8662
  (2020). https://www.science.org/doi/10.1126/sciadv.abc8662
- Wikipedia: *Speed of sound* — tabulka materiálů, vztah tyčové
  a objemové rychlosti. https://en.wikipedia.org/wiki/Speed_of_sound
- Wikipedia: *Stability of matter* — Dyson & Lenard 1967–68,
  Lieb & Thirring 1975. https://en.wikipedia.org/wiki/Stability_of_matter
- Cong et al.: *Probing the acoustic phonon dispersion and sound velocity
  of graphene by Raman spectroscopy*, Carbon 149 (2019) 19
  — podélná rychlost v grafenu.
- Youngův modul a hustota konstrukčních ocelí: E = 190–210 GPa,
  ρ = 7 750–8 050 kg/m³ (standardní materiálové tabulky).
