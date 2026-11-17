# 156 — fact check (scénář v0.3, 2026-11-14)

Zdroje s odkazy jsou v `factcheck-zaklad.md`; tady je tvrzení po
scénách. **P** primární (výrobce, instituce, dokumentace), **S** tisk,
**M** změřeno agentem. Nadpis nese ID scény a doslovný fragment, `grep`
ho musí najít v té scéně.

### S01/S02 — „nineteenth of July, 2024"
CrowdStrike RCA (2024-08-06): 19. 7. 2024 *„content configuration update
(via channel files) for the Windows sensor that resulted in a system
crash"* (P). „Configuration file" = channel file 291, ne nový program. ✅

### S03 — „eight and a half million"
Microsoft, D. Weston, 2024-07-20: *„affected 8.5 million Windows devices,
or less than one percent of all Windows machines"* (P). „Within hours":
vadná verze vyšla 04:09 UTC, opravená 05:27 UTC; stroje padaly od rána
(S). ✅

### S04 — „Airlines grounded flights"
Delta, United a American Airlines zastavily lety (NPR, Engadget, S);
v Německu nemocnice rušily neakutní operace (S); Sky News byla ráno mimo
vysílání (S). ✅ („Hospitals cancelled operations" — opraveno
z „appointments": rušení objednávek bylo u britských praktiků, operace
v nemocnicích.)

### S05 — „twenty pieces of data"
RCA: *„The sensor expected 20 input fields, while the update provided 21
input fields… resulted in an out-of-bounds memory read"* (P). ✅

### S06/S07 — „Same kind of bug"
Čtení mimo meze pole je běžná třída chyb v aplikacích; v ringu 3 končí
pádem procesu. Rétorické zobecnění, ne číslo. ✅

### S11/S12 — „nothing in the processor stopped a program"
DOS běží v reálném režimu, který nemá ochranu paměti ani úrovně
oprávnění; program může zapisovat kamkoli včetně paměti DOSu a přímo
na porty (Intel; Wikipedia *Real mode*). Formulace změkčena podle
zpětné vazby 0.1 („every program could do anything" byla absolutní). ✅

### S14 — „In 1982, Intel's 80286"
80286 uveden 1982, přinesl chráněný režim; Intel jej popisuje jako
*„four-level, ringed-type, increasingly-privileged protection
mechanism"* (P). ✅

### S17 — „The lower the number"
CPL 0 nejvíc privilegovaný, 3 nejméně (Intel SDM sv. 3, 5.5). ✅

### S19b — „Windows, macOS and Linux"
Na x86 všechny tři používají jen CPL 0 (kernel) a CPL 3 (aplikace);
ringy 1 a 2 nevyužívá žádný (Intel SDM 5.5: systémy se dvěma úrovněmi
mají použít 0 a 3). Zjednodušení: macOS na Apple Silicon je ARM, viz S19c. ✅

### S19c — „exception levels"
ARMv8-A: EL0 aplikace, EL1 kernel OS, EL2 hypervisor, EL3 secure monitor;
EL0 a EL1 povinné (Arm ARM, S: Arm community, WikiChip). Apple M1+
a telefony jsou ARMv8/9. Číslování je opačné než u x86 (vyšší = víc
moci) — scénář to neříká, kresba ano. ✅

### S21/S22 — „Switching off interrupts"
`CLI` při CPL > IOPL a `MOV CR3` mimo CPL 0 vyvolají #GP (Intel SDM);
Linux pošle procesu SIGSEGV/SIGILL a ukončí ho, Windows obdobně. ✅

### S23/S24 — „either user or supervisor"
Bit U/S v položce stránkové tabulky; přístup z CPL 3 na supervisor
stránku = page fault (Intel 80386 manual, SDM 4.6) (P). ✅

### S25 — „its own map of memory"
Každý proces má vlastní stránkové tabulky (adresní prostor); izolace
mezi procesy v ringu 3 je věc stránkování, ne ringů. ✅

### S27 — „Its driver ran in ring zero"
Microsoft Security blog 2024-07-27: chyba čtení mimo meze v ovladači
`CSagent.sys`, výpis ukazuje stránkovou chybu v kernelu (P). ✅

### S29/S30 — „It stopped the whole machine, on purpose"
Microsoft Learn, *Bug Checks (Blue Screens)*: *„When Microsoft Windows
encounters a condition that compromises safe system operation, the
system halts"*; běh dál by mohl poškodit data (P). ✅

### S31 — „every restart brought the crash back"
Stroje uvízly ve smyčce bootu; náprava = nouzový režim a ruční smazání
souboru z `System32\drivers\CrowdStrike` (S, CrowdStrike pokyny). ✅

### S35 — „it's called SYSCALL"
Na x86-64 používají Linux i Windows instrukci `SYSCALL` (Intel SDM,
AMD64). „On a modern PC" — 32bitové systémy měly `int 0x80`/`SYSENTER`. ✅

### S37 — „the kernel chose in advance"
`SYSCALL` skočí na adresu z MSR `IA32_LSTAR`, kterou nastaví kernel (P). ✅

### S40 — „still makes thirty"
`strace -f -c true`: 30 volání (M, 2026-11-14). ✅

### S41 — „six hundred and seventy thousand"
`strace -f -c timeout 20 firefox --headless … Wikipedia`: 669 861 (M).
Zahrnuje start prohlížeče („starting up and loading"). `strace` program
zpomaluje, proto dodáno *„even with our counting slowing it down"*. ✅

### S45 — „had eight of them"
Schroeder & Saltzer, CACM 3/1972: *„In Multics, eight was chosen as the
appropriate number of rings"*; na 645 softwarově (P). Multics v provozu
od 1969. ✅

### S46 — „layers of trust"
Smysl ringů v Multicsu: vrstvy supervisoru a uživatelských podsystémů
s klesající důvěrou (P, tamtéž). Obecný popis, bez čísel. ✅

### S46b — „Rings one and two were meant for…"
Intel SDM sv. 3A, obr. 5-3 *Protection Rings*: Operating System Kernel
(0), Operating System Services (vnitřní ringy kolem jádra), Applications
(3); text: vnější ringy *„for less critical software"* (S: zrcadla SDM).
„Drivers" je příklad služby systému, ne citát. ✅ jako zjednodušení

### S48/S49 — „many kinds of processor"
Windows NT původně IA-32, MIPS, Alpha (S); Unix portovaný od 1973.
**Úmyslně NEtvrdí**, že ty procesory měly jen dva režimy (Alpha i VAX
měly čtyři, MIPS R4000 tři) — jen že dvě úrovně jsou společné všem. ✅

### S50/S51 — „each page knows only two states"
Stránkování x86 má jen bit U/S; CPL 0–2 = supervisor (P). Zjednodušení:
ve 32bitovém režimu šlo ring 0 od ringu 1 chránit ještě segmentací, ale
systémy používají plochý model a v 64bitovém režimu se meze segmentů
nekontrolují. ✅ jako zjednodušení

### S51b — „OS/2 let some programs step into ring two"
OS/2 nastavuje IOPL 2; ring 2 používá jen pro IOPL segmenty aplikací,
které přistupují přímo na I/O porty (Dr. Dobb's 12/1988; EDM2 Device
Driver FAQ: ring 1 nepoužit, ring 2 = IOPL, drivery v ringu 0) (S).
Proto „programs", ne „drivers". ✅

### S51c — „Xen and VirtualBox moved the guest's kernel into ring one"
Xen PV na 32bit x86: Xen v ringu 0, kernel hosta v ringu 1, aplikace
v ringu 3 (Barham et al., SOSP 2003; xen-users) (P/S). VirtualBox raw
mode pouštěl kód kernelu hosta v ringu 1 (odstraněn ve 6.1, viz S52/S53).
Obojí před VT-x/AMD-V („before processors had help"). ✅

### S52/S53 — „In 2023, Intel proposed"
X86S (bílá kniha 5/2023) mimo jiné ruší ringy 1 a 2; 20. 12. 2024 Intel
oznámil, že v X86S nepokračuje (TechPowerUp, Hackaday, S). „Almost
nothing uses them": VirtualBox raw mode (ring 1) odstraněn ve verzi 6.1. ✅

### S55 — „three teams of researchers"
Jann Horn (Google Project Zero), Cyberus Technology, TU Graz — nezávisle
(meltdownattack.com, P). Nahlášeno výrobcům 1. 6. 2017 (Project Zero). ✅

### S57/S58 — „It runs ahead"
Spekulativní a out-of-order vykonávání; chybně odhadnuté výsledky se
zahodí (architektonicky se neprojeví). ✅

### S59–S61 — „before it had finished checking"
Project Zero: výsledek čtení se předá dalším instrukcím dřív, než
doběhne kontrola oprávnění; CERT VU#584653 *„permission check performed
after kernel memory read"* (P). ✅

### S62–S64 — „into the processor's cache"
Závislé čtení podle tajného bajtu načte jeden řádek pole útočníka do
cache; měření času přístupu (Flush+Reload) bajt prozradí (P, článek
Meltdown). ✅

### S65 — „Passwords and encryption keys included"
meltdownattack.com: *„read the memory of other programs and the
operating system… passwords"* (P). Na Linuxu kernel mapoval celou
fyzickou paměť. Formulace podle zpětné vazby 0.1: „whatever secrets were
sitting in it", ne „Anything". ✅

### S66 — „Intel processors going back to 1995"
meltdownattack.com: prakticky každý procesor Intel s out-of-order od
1995, kromě Itanium a Atom před 2013 (P) — proto jen „Intel processors going back to 1995", ne „every". ✅

### S67 — „third of January, 2018"
Project Zero blog 2018-01-03 (P). ✅

### S69 — „almost entirely"
Dokumentace jádra (PTI): v uživatelských tabulkách zůstává jen
minimum — vstupní/výstupní kód a IDT v `cpu_entry_area` (P). ✅

### S70 — „swap the map as well"
PTI: *„Moves to CR3… are required at every entry and exit"* (P). ✅

### S71 — „up to nineteen on busy databases"
Red Hat (článek 3307751): kategorie *Measurable* původně 8–19 % —
OLTP databáze a *„benchmarks with high kernel-to-user space
transitions"*; *Minimal* pod 1 % (P). **Čísla jsou pro záplaty všech
tří variant (Meltdown + Spectre) dohromady**, proto „patches for
Meltdown and a related flaw, Spectre". Opraveno z „between one and
twenty percent" (to bylo z druhé ruky a nepřesně). ✅

### S75 — „from there, it sees everything"
Microsoft 2024-07-27: viditelnost celého systému, start brzy při bootu,
odolnost proti útočníkovi s právy administrátora (P). ✅

### S76 — „at the cost of resilience"
Tamtéž doslova *„Kernel drivers provide the above properties at the cost
of resilience"* (P). ✅

### S77/S78 — „still in test versions of Windows"
Windows blog 2025-06-26: platforma pro antiviry mimo kernel, private
preview pro partnery MVI (P); Elastic 2026-10-26: *„in its early
stages… Windows Insider builds"* (S). Kernel bezpečnostním firmám
zavřený není. ✅

### S80 — „invisible to an anti-cheat"
Riot (2020-02-03): kód v kernelu může hooknout právě ta systémová volání,
na která by se anti-cheat v user mode spoléhal (P). ✅

### S81 — „On most PCs, it loads as Windows starts"
Vanguard: ovladač `vgk.sys` v ringu 0, standardně startuje s Windows (P/S).
**Od 24. 6. 2026 režim On-Demand** — ovladač jen při spuštění hry, ale
volitelně a jen na Windows 11 25H2 se Secure Boot, TPM 2.0, VBS, HVCI
a IOMMU; podle Riotu splňuje podmínky ~35 % hráčů (S). Proto „On most
PCs", ne absolutně. ✅

### S82 — „That doesn't make it faulty"
Podle zpětné vazby 0.1: netvrdit, že je Vanguard rizikový jako vadný
ovladač CrowdStriku — jen že sedí na stejné úrovni, kde chyba shodí celý
stroj (pády `vgk.sys` s modrou obrazovkou se vyskytují, S). ✅
