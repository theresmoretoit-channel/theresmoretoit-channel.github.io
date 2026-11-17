# Fact check — 066 „Why Is Software Still So Full of Bugs?"

Ověřeno 2026-09-25 proti **`script 0.3.md`**, čísla scén podle 0.3 (0.4 mění jen S53).
Závěry: ✅ platí · ✏️ opraveno ve scénáři · ⚠️ platí se zjednodušením (popsaným níž)

## Kombinatorika (S06–S11)

**S08 „Two to the power of a hundred… roughly a million trillion trillion."** ✅
2¹⁰⁰ = 1 267 650 600 228 229 401 496 703 205 376 ≈ 1,27·10³⁰.
Million · trillion · trillion = 10⁶·10¹²·10¹² = 10³⁰. „Roughly" pokrývá faktor 1,27.

**S09–S10 „a billion combinations every second… started at the Big Bang… about one combination in three thousand."** ✅ (spočítáno)
Stáří vesmíru 13,787 mld. let (Planck 2018) = 4,35·10¹⁷ s → 4,35·10²⁶ testů.
2¹⁰⁰ / 4,35·10²⁶ = **2 914**, tedy jedna kombinace ze ~2 900. „About one in three thousand" sedí.

**S11 „A real program has millions of them."** ✅
Jako vypínač se počítá každý bit stavu. Program se stavem pár megabajtů má desítky milionů bitů, takže „miliony" je spíš podhodnocené.

## Přetečení bufferu (S18–S27)

**S19–S20 C a `strcpy` do bufferu na 16 znaků pokračuje za konec.** ✅
`strcpy` kopii nijak neomezuje. Pokračuje, dokud nenarazí na nulový znak ve zdroji. Chování je nedefinované, v praxi to přepíše sousední paměť.

**S22 „In a classic layout, it sits not far past the end of our buffer."** ⚠️
V klasickém zásobníkovém rámci (x86, zásobník roste dolů) leží lokální pole pod uloženým ukazatelem rámce a návratovou adresou. Zápis za konec pole jde směrem k vyšším adresám, tedy právě na ně. Doložený příklad je Morris worm: buffer měl 512 B a útok poslal 536 B, tedy o 24 B víc, než se vešlo.
Formulace „in a classic layout" záměrně neříká, že tak vypadá každý dnešní systém.

**S23–S24 útočník pošle vlastní instrukce a novou návratovou adresu, procesor do nich skočí.** ⚠️
Takhle vypadá klasický stack smashing (Aleph One, *Smashing the Stack for Fun and Profit*, Phrack 49, 1996). Dnes to přímo takhle nefunguje kvůli ochranám z S59 (NX, canary, ASLR). Útoky proto obcházejí zákaz spouštění dat přes ROP. Video to řeší návratem v S59–S60, takže S23–S24 neříkají nic nepravdivého o minulosti a S59 dopovídá současnost.

**S25 „with all the permissions of yours"** ✅ Vložený kód běží v kontextu napadeného procesu.

**S27 „In 1988… the Morris worm spread across the early internet."** ✅
2. 11. 1988. Jedna z cest šíření byla přetečení bufferu ve `fingerd` na 4.3BSD/VAX: `gets()` do 512B bufferu, 536B řetězec přepsal návratovou adresu. Nakazil odhadem ~6 000 strojů, asi 10 % tehdejšího internetu.
Zdroje: [Wikipedia](https://en.wikipedia.org/wiki/Morris_worm), [Rapid7](https://www.rapid7.com/blog/post/2019/01/02/the-ghost-of-exploits-past-a-deep-dive-into-the-morris-worm/).
Worm měl i další cesty (sendmail DEBUG, rsh/rexec). Věta „let the Morris worm spread" netvrdí, že to byla jediná.

**S27 „the same trick has been used in attacks ever since"** ✅ Code Red (2001, IIS), SQL Slammer (2003, SQL Server), oba přetečení bufferu.

## Rust a paměťová bezpečnost (S28–S34)

**S28 „Rust refuses to build many programs that could misuse memory."** ✅
Borrow checker odmítne kód s porušením paměťové bezpečnosti mimo bloky `unsafe`. Slovo „many" nechává místo pro `unsafe` i pro chyby, které kontrola nepokrývá.

**S30 „around seventy percent of their serious security bugs come from memory safety problems."** ✏️ → „Microsoft **and Google's Chrome team**"
- Microsoft: Matt Miller, BlueHat IL, únor 2019. Zhruba 70 % CVE, které Microsoft každý rok opravuje, jsou chyby paměťové bezpečnosti, a to za posledních 12 let. Znovu to zopakoval [MSRC blog, 07/2019](https://msrc.microsoft.com/blog/2019/07/a-proactive-approach-to-more-secure-code/).
- Google: [Chromium, Memory safety](https://www.chromium.org/Home/chromium-security/memory-safety/) (2020). Zhruba 70 % **high a critical** bezpečnostních chyb Chromia jsou paměťové, ze vzorku 912 chyb od roku 2015.
- Populace se liší: u Microsoftu jsou to všechny opravené CVE, u Chromia jen závažné. „Serious" tedy přesně sedí na Chromium. U Microsoftu jde o chyby, které dostaly CVE a bezpečnostní opravu, a za vážné se dají považovat. „Google" se zúžil na tým Chrome, protože číslo je z Chromia, ne za celý Google.

**S31–S33 paměťově bezpečný program ukáže cizí data kvůli chybě v kontrole oprávnění.** ✅
Typický případ je Broken Access Control / IDOR, č. 1 v OWASP Top 10 (2021). Žádný typový systém tomu obecně nezabrání, protože nezná záměr.

## Testování, Turing, Rice (S35–S43)

**S37 „In 1970, Edsger Dijkstra… Testing can show the presence of bugs, but never their absence."** ✅
EWD249, *Notes on Structured Programming* (1970): *„Program testing can be used to show the presence of bugs, but never to show their absence!"* Podobnou myšlenku řekl už na konferenci NATO v Římě 1969. Rok 1970 platí pro publikovanou formulaci. Věta ve scénáři je zkrácená parafráze, nevydává se za doslovnou citaci.

**S39 „before the first real computer was even built. In 1936, Alan Turing proved that a program like that cannot exist."** ✅
- *On Computable Numbers* (1936). První funkční programovatelný počítač je Zuse Z3 z roku 1941, Colossus 1943–44, ENIAC 1945. Mechanický Z1 (1938) spolehlivě nefungoval. „Before the first real computer" tedy platí.
- Logika: „program" z S38 má rozhodnout **pro jakýkoli kód**, jestli dělá, co má. Kdyby existoval, dal by se použít i na specifikaci „program skončí", a tím by rozhodl problém zastavení. Turing ukázal, že to nejde.

**S41 „no program can decide, for every other program, whether it will ever stop running."** ⚠️
Turing v roce 1936 dokázal nerozhodnutelnost ekvivalentní otázky („circle-free", tedy jestli stroj vypisuje nekonečně mnoho číslic). Název *halting problem* a tuhle formulaci zavedl Martin Davis (1952, 1958). Připisovat ji Turingovi je v literatuře standardní. Pro popularizaci ✅.

**S42 „In 1953, Henry Rice went further… almost any question about what a program actually does."** ✅
H. G. Rice, *Classes of recursively enumerable sets and their decision problems*, Trans. AMS 74 (1953). Každá **netriviální sémantická** vlastnost (vlastnost chování programu, ne jeho zápisu) je nerozhodnutelná. „Almost any" = netriviální, tedy všechny kromě „platí pro všechny programy" a „neplatí pro žádný". „What a program actually does" = sémantická, ne syntaktická.

**S43 „Is it secure? Does it leak data? Does it give the right answer? There is no general method that settles that for every program."** ✅
Všechny tři otázky se ptají na chování programu, takže po formalizaci pod Riceovu větu spadají („vypíše tajnou hodnotu na výstup" nebo „vrátí f(x) pro všechna x"). Věta neříká, že to nejde u konkrétního programu, jen že neexistuje **obecná** metoda pro **každý** program. S44–S48 pak ukazují přesně tu výjimku.
Poznámka pro komentáře: nástroje statické analýzy fungují, protože buď přiznají „nevím", nebo občas řeknou něco špatně. Riceově větě to neodporuje.

## seL4 (S44–S48)

**S45 „In 2009, a team in Australia proved that a small operating system kernel, called seL4, does exactly what its specification says."** ✅ ⚠️
Klein et al., *seL4: Formal Verification of an OS Kernel*, SOSP 2009, NICTA (Sydney). Jde o důkaz funkční správnosti: implementace v C zjemňuje abstraktní specifikaci.
Důkaz předpokládá správnost překladače (GCC), asi 600 řádků assembleru, bootovacího kódu, správy cache a hardwaru (§4.3–4.4). Věta „does exactly what its specification says" to zjednodušuje. Předpoklady video nezmiňuje, ale S47–S48 („even that proof has a catch") jdou stejným směrem.

**S46 „It was under ten thousand lines of code."** ✅ 8 700 řádků C + 600 řádků assembleru = 9 300.

**S46 „Building the kernel took about two person-years. Proving it correct took about twenty."** ✏️ (dřív „The proof took about twenty person-years of work.")
Z článku, §5.2: *„in total the C implementation took about 2 pm, for a total cost of 2.2 py including the Haskell effort"* a *„The cost of the proof is higher, in total about 20 py. This includes significant research and about 9 py invested in formal language frameworks, proof tools, proof automation, theorem prover extensions and libraries. The total effort for the seL4-specific proof was 11 py."*
„About twenty" je tedy přesně číslo, které autoři uvádějí jako cenu důkazu. Obsahuje i jednorázový výzkum a nástroje, samotný důkaz seL4 stál 11 py. Změna věty přidává **poměr 1 : 10** mezi napsáním a dokázáním, který je doložený ze stejné tabulky a je silnější než samotné číslo.
Zdroj: [SOSP 2009 PDF](https://www.sigops.org/s/conferences/sosp/2009/papers/klein-sosp09.pdf).

**S46 „A modern web browser has tens of millions of lines."** ✅ Chromium má kolem 35–36 mil. řádků ([Wikipedia](https://en.wikipedia.org/wiki/Chromium_(web_browser))).

**S47–S48 důkaz ukáže shodu se specifikací, ne to, že specifikace odpovídá záměru.** ✅ Autoři to říkají sami: ověřuje se proti specifikaci, kterou píšou lidé.

## Závislosti a víc softwaru (S49–S55)

**S49–S50 frameworky, knihovny, „hundreds of dependencies", chybu jde nainstalovat.** ✅
U typického projektu na npm jsou stovky tranzitivních závislostí běžné. Doložený příklad importované chyby je Log4Shell (CVE-2021-44228) a event-stream (2018).

**S53 „In 2024 alone, around forty thousand got an official number."** ✅ (0.3: „over")
Za rok 2024 bylo publikováno **40 009 CVE** (proti 28 818 v roce 2023, tedy +38 %). Podle metodiky různé datasety uvádějí 39 957–40 009, takže „over forty thousand" je hraniční.
✏️ **Opraveno v 0.4 na „around forty thousand"** (rozhodl uživatel).
Zdroje: [Jerry Gamblin, 2024 CVE Data Review](https://jerrygamblin.com/2025/01/05/2024-cve-data-review/), [FIRST](https://www.first.org/blog/20250106-Vulnerability-Forecast-Year-in-Review).

**S53 „the number of known vulnerabilities keeps growing."** ✅ Roční počty CVE rostou od roku 2017 (~14,6 tis.) každý rok.
Nárůst je zčásti i tím, že víc organizací má právo CVE přidělovat (CNA). Počet CVE proto měří zčásti i to, jak moc se hledá. „Known vulnerabilities" to formuluje správně.

**S54 silnice.** Metafora, ne tvrzení.

## Obrana (S56–S61)

**S59 „the system guards it. It shuffles where things sit in memory. And it refuses to run instructions hidden in data."** ✅
Stack canary (StackGuard 1998, výchozí v GCC a MSVC), ASLR (PaX 2001, Windows Vista 2007), NX/DEP (AMD64 a Windows XP SP2, 2004).

**S60 „The bug in C is still there. It's just much harder to turn into an attack."** ✅ Ochrany chybu neodstraní, jen zdraží její zneužití. Proto dnes útoky potřebují řetězy (ROP, únik adresy).

**S61 sandboxy, oprávnění, izolace, šifrování, zálohy, monitoring.** ✅ Výčet principu defense in depth.

## Aktualizace (S62–S67)

**S63 „may well contain a vulnerability nobody has found yet."** ✏️ (dřív „almost certainly has")
U velkého softwaru je to historicky skoro jisté, dokázat se to ale nedá. Změkčeno na návrh zpětné vazby 0.2.

**S66 odkaz na 019 *It Still Works. So Why Upgrade It?*** ✅ Titul ověřen v `videos/019-why-upgrade-something-that-works/`.


## Verze 0.5: zpřesnění po Codexu (tři jazyky)

Codex dostal cs, de a es a v části D hledal slabá místa v angličtině. Pět míst označil **ve všech třech jazycích**, takže je vada v originálu:

| scéna | 0.4 → 0.5 | důvod |
|---|---|---|
| S30 | „of their serious security bugs" → „of the security bugs **they've studied**" | Microsoft počítá všechna opravená CVE, Chromium jen high/critical. „Serious" sedělo jen na jeden soubor dat |
| S32 | „No memory is overwritten." → „No memory is **corrupted**." | správný program paměť přepisuje běžně, jde o poškození |
| S42 | „almost any question" → „every **non-trivial** question" | přesné vymezení Riceovy věty (netriviální sémantická vlastnost). „About what a program actually does" = sémantická zůstává |
| S44 | „prove it" → „prove it **correct**" | „it" mohlo ukazovat na „bug-free software is impossible" |
| S66 | „that debt can't be postponed forever" → „that debt **has to be paid off**" | odkládá se splácení, ne dluh |

Menší, označené jedním nebo dvěma jazyky, ale levné a přesnější:

| scéna | změna | důvod |
|---|---|---|
| S12 | „asks for their account" → „… **by its number**" | S13 pak dává smysl („text instead of a number") |
| S34 | „No language can catch that" → „… **on its own**" | jazyky s bezpečnostními typy (Jif, F*) to umí, když se jim pravidla zadají |
| S54 | „Because" → „**Partly** because" | růst CVE je zčásti i tím, že přibývá těch, kdo je přidělují (viz S53) |
| S60 | „The bug in C" → „The bug in **our C code**" | nešlo o chybu jazyka C |

**Ponecháno vědomě:**
- S38–S41 „does what it should" bez specifikace a problém zastavení bez „on a given input" (2/3 jazyků). Specifikaci dopovídají S47–S48 a vstup je detail, který pointu nemění.
- S45 předpoklady důkazu seL4 (1/3). Už ⚠️ výš, video je nezmiňuje.
- S46 „twenty" obsahuje i nástroje (1/3). Autoři to číslo sami uvádějí jako cenu důkazu, samotný důkaz seL4 stál 11 py. Poměr by pak byl 1 : 5, pořád silný. **Pokud to někdo v komentářích namítne, je to fér připomínka.**
- S11 „impossible" místo „impossible in practice", S20 nedefinované chování, S59 NX „instructions hidden in data", S54 „millions of times more roads" (každé 1/3). Jsou to popularizační zkratky, ne chyby.
