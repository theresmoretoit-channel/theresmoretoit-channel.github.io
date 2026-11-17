# Fact check — 054 Why Does the Most Important Player Do Almost Nothing in MMOs?

Ověřeno 2026-09-18 proti `script.md` (v0.3, 109 scén).

**Tohle video je esej o zkušenosti**, takže velká část textu jsou soudy,
ne tvrzení — a právě proto musí být vypsané všechny. Ověřitelné tvrzení
se tu od názoru pozná hůř než u výkladového videa, kde je rozdíl vidět
na první pohled.

Rozděleno proto do tří skupin: **doložitelná tvrzení**, **charakteristiky**
(soud o herním návrhu, ne fakt) a **rétorika** (mimo rozsah kontroly).

---

## A. Doložitelná tvrzení

### S02 — tři role ve třech jmenovaných hrách

> *„In games like World of Warcraft, Final Fantasy XIV or The Elder
> Scrolls Online, groups are built around three basic roles."*

**Ověřeno.** Trojice tank / healer / damage dealer je základ skupinového
obsahu ve všech třech. U ESO to potvrzuje i vlastní výběr role ve
vyhledávači skupin a existence samostatných taunt dovedností (viz S18).

**Závěr: platí.** Formulace *„in games like"* navíc netvrdí, že to platí
ve všech MMO, což by neplatilo.

### S05 — tank je role, kterou nikdo nechce

> *„And of the three, the tank is often the one nobody wants to be."*

**Tohle je nejcitlivější věta videa** a prošla dvěma přeformulacemi.
Původní znění *„the hardest role to find"* je empirické tvrzení o MMO
obecně — tedy přesně takové, které si žádá statistiku front, a tu
video vědomě nemá.

Současné znění mluví o **ochotě hráčů**, ne o počtech, a video ho
**samo dokládá o padesát scén dál** (S51d az S51f) herními systémy,
které existují proto, aby se podplněná role zaplnila.

**Závěr: platí jako popis ochoty**, podložený nepřímo. Kdyby se věta
vrátila k tvrzení o počtech, doklad by neunesla.

### S18 — taunt je mechanika, ne dojem

> *„The tank walks towards the boss. Uses a taunt."*

**Ověřeno ve všech třech hrách.** ESO: `Puncture` (One Hand and Shield)
a `Inner Fire` (Undaunted), obě **15 s**, `Inner Fire` na 28 m. WoW
i FFXIV mají vlastní obdoby.

> **Pozor na zobecnění, které ve scénáři NENÍ a být nemá:** ESO nemá
> klasickou tabulku ohrožení jako WoW, drží se to výhradně na taunt
> dovednosti. Scénář mluví obecně (*„uses a taunt"*), takže rozdíl
> nevadí — ale jakákoli věta o „threat" nebo „aggro table" by ho
> porušila.

### S30 — mrtvého hráče lze vzkřísit

> *„The healer can resurrect them. The group can continue."*

**Ověřeno**, standardní ve všech třech hrách.

> Původní znění mělo navíc *„Another player can resurrect them."*
> Škrtnuto v0.2 jako opakování — věcně to ale platilo taky.

### S33 — co se stane, když tank umře

> *„A dead tank is a completely different situation. Because the boss
> immediately finds somebody who cannot take it."*

**OPRAVENO 2026-09-18 po nálezu uživatele.** Scéna původně tvrdila,
že *„the boss suddenly has nobody to hit"* — a to je **nepravda**.

Boss po smrti tanka nezůstane bez cíle: přepne se na dalšího v pořadí
ohrožení, což je v praxi skoro vždycky damage dealer nebo healer, tedy
někdo, kdo tu ránu nerozdýchá. Přesně proto tank existuje.

**Závěr: původní znění bylo věcně špatně, opravené platí.**

> **Chyba přežila fact check i dvě kola škrtů**, protože zněla
> rozumně — táž rodina jako *„four hundred million kilometres"*
> k Jupiteru z prvního videa. A **kresba ji věrně opakovala**: šipka
> od bosse končila v prázdnu s popiskem NOBODY LEFT TO HIT, takže
> kontrola „co říká voiceover × co tvrdí kresba" ji najít nemohla —
> obojí tvrdilo totéž, jen to nebyla pravda.
>
> Opraveno v obou: text, kresba (útok míří na horní dva pruhy)
> i `UTOK_JINAM` v `_kit.py`, kde je S33 nově povolená jako scéna,
> ve které boss útočí na skupinu.

### S51d — World of Warcraft, Call to Arms

> *„World of Warcraft once added Call to Arms: a bag of extra rewards
> for whichever role the queue was short of."*

**Ověřeno z primárního zdroje** — oficiální poznámky k patchi 4.1
(Blizzard, PTR notes, duben 2011; patch vyšel **26. 4. 2011**,
expanze Cataclysm):

> *„which class role is currently the least represented in the queue"*
> … *„Satchel of Exotic Mysteries (account bound)"* … *„Players must
> queue solo with the currently indicated least represented class
> (by the system) and complete the dungeon up to and including the
> final boss in order to be eligible for the bonus reward."*

**Tři věci, které scénář říká přesně, a je to záměr:**

1. **„once added"** — minulý čas. Jestli systém běží i dnes, se
   nepodařilo doložit; scénář to netvrdí.
2. **„whichever role the queue was short of"** — systém **není
   o tancích**. Odměňuje nejméně zastoupenou roli, ať je to která
   chce. Že to bývá tank, video **netvrdí**, protože na to nemá číslo.
3. **„a bag of extra rewards"** — doslova `Satchel of Exotic
   Mysteries`, tedy pytel. Není to metafora.

### S51e — Final Fantasy XIV, Adventurer in Need

> *„Final Fantasy XIV has its own version, and it even has a name.
> Adventurer in Need."*

**Ověřeno z primárního zdroje** — oficiální Lodestone, poznámky
k patchi 5.4:

> *„Roles subject to the Adventurer in Need bonus under the Duty
> Roulette tab are now indicated by an icon."*

Bonus se týká **Duty Roulette**, dostane ho role, které je v dané
kategorii zrovna potřeba, a platí **navíc** k běžné odměně (gil
a zkušenosti). Přítomný čas *„has"* je v pořádku, systém je živý.

### S74 — swap tanků kvůli stohujícím se debuffům

> *„Swap with the other tank before the debuffs stack up and kill you."*

**Ověřeno.** Je to standardní souboj o dva tanky: na tankovi se
hromadí debuff (nejčastěji stohující zranitelnost nebo damage over
time), který dřív nebo později znemožní pokračovat, takže druhý tank
bosse tauntne a prvnímu debuff mezitím vyprší.

**Závěr: platí**, a je to konkrétní mechanika, ne obecná fráze.

### S85 — Formule 1

> *„You don't learn to drive by entering a Formula One race."*

Přirovnání, ne tvrzení. **Formula One** je správný zápis závodní
série a píše se slovem, ne číslicí — v souladu s pravidlem projektu
(označení verze číslicí, množství slovem; tohle je název).

---

## B. Charakteristiky — soud o herním návrhu, ne fakt

Tohle jsou věty, které **znějí jako doložitelná tvrzení, ale nejsou**.
Nepatří do skupiny A a nesmí se podle ní kontrolovat; zároveň nesmí
zmizet mezi rétoriku, protože se o nich dá věcně přít.

| scéna | věta | jak to stojí |
|---|---|---|
| S51f | *„built to bribe somebody into a role nobody volunteered for"* | **„bribe" je vtip, ne popis.** Systém odměňuje, neuplácí. Charakteristika je obhajitelná (motivace odměnou) a scéna před ní říká, co se doopravdy stalo |
| S61 | *„Lots of health. High resistances. Damage mitigation. Shields. Blocking."* | popis návrhu tankových postav, platí napříč žánrem; žádná konkrétní čísla se netvrdí |
| S63 | *„Because DDs are usually glass cannons."* | **žargon jako žargon** — ustálené označení návrhového kompromisu (přežití vyměněné za poškození). Slovo „usually" to drží |
| S64 | *„built to turn as much of their survivability as possible into damage"* | totéž vysvětlené; je to záměr návrhu, ne měření |
| S21–S22 | facing, blokování, adds | obecné mechaniky; scénář nikde neříká, ve které hře konkrétně |

---

## C. Rétorika — mimo rozsah kontroly

Vypsáno proto, aby bylo vidět, že se na to nezapomnělo:

- **tři úrovně tankování** (S79–S86) — vlastní rámec videa, nikoli
  převzatá klasifikace. Nikde se netvrdí, že to tak hry dělí
- **stroj o deseti součástkách** (S44–S46) — přirovnání
- **„astonishing amount of nothing happening"**, **„a small piano
  recital"** (S23, S26) — obraznost
- závěr (S95–S103) — teze o týmech, ne tvrzení o hrách

---

## Co se opravilo ve scénáři

| verze | scéna | bylo | je |
|---|---|---|---|
| v0.3 | **S05** | *„the tank is usually the hardest role to find"* | *„the tank is often the one nobody wants to be"* |
| v0.3 | **S51d** | — | doplněno tak, aby odměna platila **roli, které se nedostává**, ne tankovi |
| v0.8 | **S33** | *„the boss suddenly has nobody to hit"* | *„the boss immediately finds somebody who cannot take it"* — nález uživatele, viz výš |
| v0.8 | **S65** | *„the same mistake"* | *„the same hit"* — odstraňuje zdánlivý rozpor s S51 |

## Co se vědomě NEDOLOŽILO

**Video nemá jediné číslo o chování hráčů** a je to rozhodnutí
uživatele, ne mezera:

> Statistika typu „X % hráčů nechce tankovat" by si vyžádala
> reprezentativní data a určení hry, režimu i období — a posunula by
> video od paradoxu k „MMO tank shortage explained".

Zvažovaný a **zamítnutý** údaj: podíl tanka ve čtyřčlenné skupině
(jeden tank, tři DPS = 25 %). Je to matematika složení skupiny, tedy
doložitelné — ale bylo by to číslo jen proto, aby video mělo číslo,
a hlavně by otevřelo otázku „tak proč tedy hráči tanky nehrají?",
tedy úplně jiné video. **Uzavřeno uživatelem 2026-09-18, neotvírat.**

Doklad té premisy nese **S51b az S51f** (Call to Arms, Adventurer in
Need) — tvrdý externí důkaz bez předstírání, že známe univerzální
statistiku.

## Zdroje

| | |
|---|---|
| Call to Arms | oficiální poznámky k patchi 4.1, `worldofwarcraft.blizzard.com/en-gb/news/10004620/` |
| Adventurer in Need | oficiální Lodestone, poznámky k patchi 5.4, `na.finalfantasyxiv.com/lodestone/topics/detail/230f6e0af3…` |
| ESO taunt (`Puncture`, `Inner Fire`, 15 s) | UESP, `en.uesp.net/wiki/Online:Puncture`, `Online:Inner_Fire` |
| tank swap | Wowpedia, `wowpedia.fandom.com/wiki/Tank_swap` |

> **Sekundární zdroje jsou použité jen na mechaniky, ne na zobecnění.**
> Obě tvrzení, která video vyslovuje jmenovitě (Call to Arms,
> Adventurer in Need), stojí na **primárních** poznámkách vydavatele.
