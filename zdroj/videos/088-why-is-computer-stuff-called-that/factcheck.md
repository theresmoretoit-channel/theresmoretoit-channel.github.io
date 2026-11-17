# Fact check — 088 Why Is Computer Stuff Called That?

Ověřeno 2026-10-04 nad `script 0.1.md` (S01–S87), opravy zapracované
do `script 0.2.md`. Tři nezávislé průchody webovými zdroji; čísla u paketů
a rakety **spočítaná**, ne převzatá.

**Hlavní zdroje:**

- Computer History Museum, *The mouse*: <https://www.computerhistory.org/revolution/input-output/14/350>
- SRI, *75 years of innovation: the computer mouse*: <https://www.sri.com/75-years-of-innovation/75-years-of-innovation-the-computer-mouse/>
- Johnson et al. 1989, *The Xerox Star: A Retrospective*, IEEE Computer:
  <https://www.lri.fr/~mbl/ENS/FundHCI/2013/papers/XeroxStar-Computer89.pdf>
- Wikipedia *Trash (computing)*; MIT Technology Review 2011, *Who coined “cloud computing”?*
- Berners-Lee, FAQ: <https://www.w3.org/People/Berners-Lee/FAQ.html>
- Internet Hall of Fame, Donald Davies; Wikipedia *Donald Davies* (ref. 16)
- Etymonline: *payload*, *buffer*, *pipeline*, *margin*, *log*, *boot*, *demon*
- TUHS, *Pipes* (McIlroy 1964): <https://wiki.tuhs.org/doku.php?id=features%3Apipes>
- MDN, *The box model*
- Royal Museums Greenwich, chip log: <https://www.rmg.co.uk/collections/objects/rmgc-object-42932>; Wikipedia *Chip log*, *Logbook (nautical)*
- Barry Popik, *pull yourself up by your bootstraps* (1834)
- Smithsonian NMAH, *Log Book With Computer Bug*: <https://americanhistory.si.edu/collections/object/nmah_334663>
- JSTOR Daily, *The Bug in the Computer Bug Story*
- Edison → Puskás, 13. 11. 1878 (citováno přes Wikipedia *Bug (engineering)*, Edison Papers neotevřeny)
- Corbató, e-mail v *Take Our Word For It* 146 (2002): <https://www.takeourword.com/TOW146/page4.html>
- Maxwell, *Theory of Heat* (1871); dopis Taitovi 11. 12. 1867; Kelvin, Nature 1874
- Shoch & Hupp, *The “Worm” Programs*, CACM 25(3), 1982

---

## S01–S06 — háček
Neověřitelná tvrzení nejsou; řetěz logu viz S48–S55. **OK.**

## S08–S10 — myš
Kabel vycházel na prvním prototypu **vzadu**, pod zápěstím (CHM). Postavil ho
Bill English podle návrhu Douga Engelbarta, SRI, 1963 (CHM) / 1964 (SRI) —
„1960s“ kryje obojí. K jménu Engelbart: *„No one can remember. It just looked
like a mouse with a tail, and we all called it that.“*
**Upřesněno:** jméno se nepřipisuje inženýrům jako rozhodnutí — *„the team
that built it… Nobody remembers who said it first.“* (připomínka uživatele).

## S11–S14 — desktop
Star: koncipován 1975, vydán 1981; plocha s *„documents, folders, file drawers,
in-baskets“*, záměrně *„an analogy with real offices to make the system easy
to learn“* (Johnson 1989). Alto 1973. **Koš Star neměl** (mazalo se klávesou
Delete); Wastebasket přišel s Apple Lisa 1983, Trash s Macintoshem 1984.
**Opraveno:** *„Apple later added the bin.“*

## S17–S20 — cloud
Mrak jako symbol sítě, do které se nekreslí: telefonní schémata, ARPANET 1977,
CSNET 1981. „Cloud computing“ poprvé 1996 (interní dokument Compaqu). **OK.**

## S21–S22 — web
Berners-Lee: *„its decentralized form allowing anything to link to anything.
This form is mathematically a graph, or web.“* Jméno ustaveno 1990.
„No edge“ je básnická licence. **OK.**

## S24–S25 — packet
Idea Davies 1965, slovo *packet* písemně červen 1966, první přednáška 16. 3. 1966.
Překladatelnost: *„after consulting with a linguist because it was capable of
being translated into languages other than English“* — široce citováno,
**vlastními slovy Daviese nedohledáno**; „partly because“ je přiměřené.
**Opraveno:** *„In 1965“* → *„In the mid-1960s“*.

## S26 — kolik paketů má video
Spočítáno: 10 min × 5 Mbit/s (1080p) = 375 MB ÷ ~1 460 B ≈ **257 000 paketů**;
720p ≈ 130 000, 480p ≈ 50 000. **Chyba:** *„thousands“* →
*„hundreds of thousands“*.

## S28–S31 — load, payload
Etymonline: *„1914, from pay + load. Originally ‘the part of a truck's (later
an aircraft's) load from which revenue is derived’“* — nákladní auta opravdu
první. Raketa: Falcon 9 vzletová hmotnost 549 t, palivo 488,4 t = **89 %**,
náklad na LEO 22,8 t = 4,2 %. Header/payload je standardní terminologie. **OK.**

## S33–S37 — stream, buffer
Buffer: *„apparatus for deadening the concussion between a moving body and
that against which it strikes,“ 1835*; železniční 1839; počítačový smysl od
40. let 20. stol. z obecného „tlumič nárazu“. Scénář vagon dává jako obraz,
netvrdí přímé odvození. **OK.**

## S38–S40 — pipeline
McIlroy, Bell Labs, memo 11. 10. 1964: *„We should have some ways of coupling
programs like garden hose“*. Slovo *pipeline* ale McIlroy nepoužil; v počítačích
dřív u řetězení instrukcí (IBM Stretch ~1959–61), samo slovo z ropovodů (1859).
„Plumbing from the start“ platí pro slovo. Unixové roury 1972/73.
**Upřesněno:** jmenován McIlroy, *„like lengths of garden hose“*; scéna netvrdí,
že slovo vymyslel.

## S42–S44 — padding, margin
MDN: padding mezi rámečkem a obsahem, margin vně. *Margin* = okraj listu,
14. stol., tedy starší než tisk. **Upřesněno:** *„printed page“* → *„page“*.

## S48–S55 — lodní log
Chip log poprvé popsal William Bourne **1574** (RMG). Původní *„Four hundred
years ago… no instrument“* = rok 1626, kdy už existoval. **Chyba**, opraveno na
*„Five hundred years ago, a ship had no speedometer.“* (1526, před Bournem).
Lano zpočátku **uzly nemělo**, ustálily se v 17. stol. → *„Later, knots were
tied…“*. Přesýpací hodiny 28 s (RMG). Jednotka *knot* odsud pochází.
Údaje se psaly nejdřív křídou na desku, pak do knihy → *„first on a board, then
in a book“*. Log-book 1670s; počítačové *log in/on* 1963, význam „záznam“ přímo
z lodního deníku. **OK po opravách.**

## S57–S62 — bootstrap
1834, sarkasmus na vynálezce perpetua mobile: *„hand himself over the
Cumberland river or a barn yard fence by the straps of his boots“* — příklad
nemožného úkolu. Poutka jsou **nahoře**, ne vzadu. Počítačový *bootstrap* 1953
výslovně z rčení, *boot* 1975. **Upřesněno:** *„at the top of a boot“*,
*„your own boots“*; S62 *„when it wakes up“* → *„when you switch it on“*
(probuzení ze spánku zavaděč nespouští).

## S64–S69 — bug
9. 9. 1947, Harvard Mark II, *„Relay #70 Panel F (moth) in relay“*,
poznámka *„First actual case of bug being found.“* Smithsonian předmět sám
nazývá **„Log Book“** — callback S66 sedí. Hopperová ji nenašla (*„This log
book was probably not Hopper's“*), scénář ji nejmenuje. Výklad jako vtipu
podporuje JSTOR Daily; *bug* jako vada přístroje už ve Websterovi 1934.
Edison 1878: *„‘Bugs’—as such little faults and difficulties are called“*. **OK.**

## S70–S76 — daemon
Corbató, Project MAC 1963: *„Our use of the word daemon was inspired by the
Maxwell's daemon of physics… background processes which worked tirelessly“*.
Maxwell: jedna nádoba rozdělená přepážkou s otvorem, bytost pouští rychlé
z A do B a pomalé z B do A; slovo *demon* až Kelvin 1874. Původní znění
(*„two boxes“*, *„opened the door only for the fast ones“*) **chybné**, opraveno.
Daimon = *„guiding spirit, tutelary deity“*. Pošta/tiskárna/hodiny ≈ sendmail,
lpd, cron/ntpd. **OK po opravě.**
V 0.4 doplněno *„later called Maxwell's demon“* — slovo *demon* až Kelvin 1874, tedy „later“ sedí.

## S78–S81 — worm
Brunner 1975, „tapeworm“. Shoch & Hupp: pokusy ~1979, workshop 1980, článek
1982 → *„Seven years later“* **chybné**, opraveno na *„A few years later“*.
Článek otevírá motto z románu a cituje Brunnera, výslovné „pojmenovali jsme
podle“ tam není → *„borrowed the name from the book“*. *„Didn't come from
biology“* zavádějící (tasemnice je biologie) → vypuštěno. Worm běžel na
*„over 100 Alto computers“* v PARC → *„same lab… desktop“* **OK**.

## S82–S87 — závěr
Shrnuje výše ověřené. **OK.**
