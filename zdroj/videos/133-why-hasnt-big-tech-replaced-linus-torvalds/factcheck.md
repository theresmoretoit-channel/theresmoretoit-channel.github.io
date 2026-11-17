# 133 — fact check scénáře (v0.2 → v0.3, 2026-11-02)

Každé ověřitelné tvrzení `script.md` (ID scén podle v0.3, shodná s v0.2).
Podklady a plné citace jsou v `factcheck-zaklad.md` (dál jen „základ").
✅ = doloženo přečteným primárním zdrojem, ⚠ = zjednodušení nebo
sekundární zdroj (zdůvodněno), ❌ = neprošlo → opraveno ve v0.3.

## Opravy ve v0.3

| scéna | v0.2 | v0.3 | proč |
|---|---|---|---|
| S31 | *since Android 12, new phones have to use one common kernel from Google* | *since Android 12, phones that launch on a newer kernel must use one common kernel from Google, the Generic Kernel Image* | source.android.com: *„Beginning with Android 12, devices shipping with kernel version 5.10 or higher must ship with the GKI kernel.“* Povinnost neplatí pro každý nový telefon. GKI pojmenováno (požadavek uživatele) |
| S42 | *about a hundred and forty of them send their collections to Linus* | *more than a hundred of them* | 139 bylo počítáno v **repozitářích**, ne v lidech. `conclave.rst`: *„over 100 maintainers each working to keep changes moving through their own repositories“* |
| S55 | *about three percent of its **spending*** | *of its **budget*** | 8 410 114 $ / 284 795 682 $ = 2,95 % je **prognóza výdajů na 2025** z výroční zprávy LF (str. 58), řádek „Linux Kernel Project". Ne Form 990 (ten má celkem 204 369 300 $ a řádek pro jádro nemá); opraveno i v základu. Jádru slouží zčásti i jiné řádky (infrastruktura, akce) |

## Tvrzení po scénách

| scéna | tvrzení | | ověření |
|---|---|---|---|
| S03–S05 | firma, jejíž infrastrukturu „ovládá“ člověk, který pro ni nepracuje; inženýři mu pošlou práci a čekají | ⚠ | háček zjednodušuje: práce jde napřed ke správcům a teprve přes ně k Linusovi. Vysvětleno v S36–S43, takže to nezůstane viset |
| S04 | *You can't fire him. You can't overrule him.* | ⚠ | platí z pohledu **jedné** firmy („you“). Firmy dohromady jmenují radu LF, která ho zaměstnává — S51–S54 to říkají otevřeně |
| S07 | Google, Microsoft, Intel, Amazon a Meta posílají kód do jádra | ✅ | změny ve verzi 7.3 podle e-mailové domény autora (`git log --no-merges v7.2..v7.3`, agent): Intel 849, Google 670, Meta 66 (meta.com + fb.com), **Amazon 49, Microsoft 10**. LWN 7.3 podle zaměstnavatele: Intel 1 179, Google 1 138, Meta 524. Amazon a Microsoft přispívají málo, ale přispívají |
| S09 | 1991, studentský koníček, Helsinky | ✅ | comp.os.minix 25. 8. 1991, *„Organization: University of Helsinki“*, *„just a hobby“* (základ C7) |
| S09 | běží na telefonech s Androidem, cloudových serverech a všech 500 nejrychlejších superpočítačích | ✅ | TOP500 `['Linux', 500]` od listopadu 2017 po červen 2026 (základ C1); Android = jádro Linux (základ A4) |
| S10 | poslední vydání: skoro 19 000 změn, asi 3 000 vývojářů, přes 200 firem | ✅ | Linux 7.3 (18. 10. 2026): 18 765 neslučovacích commitů, 3 021 vývojářů, 232 zaměstnavatelů (LWN 1100241). **Při zveřejnění přeověřit** — 7.4 vyjde kolem začátku ledna 2027 |
| S11–S13 | Linus sám napsal devět, osm jen změnilo číslo verze | ✅ | git, autor torvalds@linux-foundation.org, 9 commitů ve 7.3, z toho 8 „Linux 7.3-rcN“ / „Linux 7.3“ (základ C2) |
| S14 | za dva týdny sloučil asi 240 dávek změn | ✅ | merge window 7.3: 236 sloučení, 7.4: 258 (git, základ C2); okno trvá ~2 týdny (docs.kernel.org). *„each one sent to him by someone he trusts“* je výklad, ne číslo |
| S17–S18 | kód si může vzít kdokoli a udělat vlastní verzi (fork), bez Linusova svolení | ✅ | licence GPLv2 to dovoluje; obecně známé |
| S19–S20 | Google neudělal nový Linux, vedl vlastní větev jádra pro Android | ✅ | Greg Kroah-Hartman: *„Effectively creating a kernel branch“* (základ A1) |
| S20 | jádro = část, která mluví s hardwarem | ⚠ | zjednodušení pro diváka, věcně správné |
| S21 | v prosinci 2009 byl kód Androidu z hlavního jádra odstraněn | ✅ | commit `b0a0ccfad85b`, 11. 12. 2009, 2.6.33-rc1 (základ A1) |
| S22 | Greg: *no one cared about the code, so it was removed* | ✅ | blog Grega Kroah-Hartmana, doslova *„In short, no one cared about the code, so it was removed.“* (datum blogu ⚠ únor 2010 — ve scénáři není) |
| S24 | výrobci čipů a telefonů přidávali vlastní změny navrch | ✅ | GKI: *„device-specific changes made by system on chip (SoC) vendors and OEMs“* |
| S25 | podle Googlu mohla být až polovina kódu jádra telefonu mimo hlavní jádro | ✅ | GKI: *„as much as 50% of kernel code being out-of-tree code“* |
| S26–S27 | každou bezpečnostní opravu bylo nutné přenést do každé verze; *„prohibitively expensive“* | ✅ | GKI: *„Security patches … must be backported into each of the device kernels. However, due to kernel fragmentation, it's prohibitively expensive to propagate security fixes to Android devices in the field.“* |
| S28 | nové vydání jádra mohlo do telefonu dorazit až za 18 měsíců | ⚠ | GKI: *„a delay of up to 18 months from the point where an LTS release was available upstream, to when it was in a device“*. Jde o **LTS** vydání (dlouhodobě podporované) a dokumentace to uvádí pod nadpisem *„Difficult to contribute kernel changes back to upstream Linux“*, ne u bezpečnosti. Věta „a new kernel release“ je obecnější, ale nepřehání; navazuje-li ve scénáři na bezpečnost, nevadí to, protože LTS vydání jsou právě nositelem oprav |
| S29–S30 | o dva roky později Greg kód vrátil: *„Turns out I was wrong, we want these in the tree.“* | ✅ | commit `355b0502f6ef`, autor Greg Kroah-Hartman, 30. 11. 2011 (o necelé dva roky), doslova (základ A2) |
| S31 | od Androidu 12 musí telefony s novějším jádrem používat GKI od Googlu | ✅ (v0.3) | viz opravy výš |
| S32 | pořád Linux s vlastními změnami Androidu | ✅ | *„a superset of the upstream Linux kernel, with additional Android-specific patches“* (Kernel overview); 2020: 485 patchů, 260 bez cesty upstream (LWN 830979) |
| S32 | drží se blízko hlavní verze, protože tam jsou opravy | ✅ | GKI: *„with all of the custom modifications in the device kernels, it's difficult to just merge the LTS fixes“*; GKI *„updated regularly with LTS and critical bug fixes“* |
| S35 | jakmile je kód v jádře, starají se o něj i ostatní | ⚠ | výklad (síťový efekt), Greg 2010: *„so that they can take advantage of the security fixes, and handle the rapid API churn automatically“* |
| S37–S38 | jádro je rozdělené na oblasti s vlastními správci; seznam má asi 3 500 položek | ✅ | `MAINTAINERS` k 2. 11. 2026: ~3 400 záznamů, ~2 100 jmen (základ C2) |
| S42 | nahoře posílá Linusovi své sbírky víc než sto správců | ✅ (v0.3) | viz opravy výš |
| S47 | Linus nepracuje pro žádnou z firem | ✅ | zaměstnanec LF, titul Fellow (Form 990 FY2024, Part VII) |
| S49 | platí ho Linux Foundation | ✅ | tamtéž; **částka záměrně neuvedena** (rozhodnutí uživatele) |
| S50–S51 | LF není charita, je to sdružení firem | ✅ | Form 990: `501(c)(6)` — obchodní / profesní sdružení, ne charita |
| S52 | Google, Microsoft, Intel, Meta, Amazon a další platí nejvyšší členství a každý má křeslo v radě | ✅ | platinoví členové: tisková zpráva LF 24. 2. 2026 (Google + Intel, Meta, Microsoft…), AWS od 7. 10. 2026 (*„AWS will have representation on the Linux Foundation Board of Directors“*). Form 990, Schedule O: *„EACH PLATINUM MEMBER, UP TO A MAXIMUM OF 20, IS ENTITLED TO APPOINT A DIRECTOR.“* (platinových je dnes 14, tedy pod stropem) |
| S53 | LF říká, že ho platí, aby mohl zůstat nezávislý | ✅ | text LF: *„sponsors Linus Torvalds so he can remain independent while working full-time on the Linux kernel“* (základ B6) |
| S54 | deklarovaný účel, ne zveřejněná záruka | ⚠ | smluvní ani jiná zveřejněná záruka nezávislosti **nenalezena** (základ B6, ❌). „Not a published guarantee“ tvrdí jen to, co jsme hledali a nenašli |
| S55 | LF hostí přes tisíc projektů | ✅ | Form 990 FY2024: *„WE SURPASSED 1,000 ACTIVE OPEN SOURCE SOFTWARE AND STANDARDS PROJECTS IN 2024“* |
| S55 | jádro dostává asi 3 % rozpočtu | ✅ (v0.3) | viz opravy výš |
| S60 | v roce 2024 dostal Linux souborový systém bcachefs | ✅ | sloučen v okně 6.7, 6.7 vyšlo 7. 1. 2024 (základ C4) |
| S61 | nové funkce jen v prvních dvou týdnech, pak jen opravy | ✅ | docs.kernel.org, 2.Process: merge window ~2 týdny, poté jen opravy |
| S62 | vývojář posílal velké změny po těch dvou týdnech | ✅ | srpen 2024, 6.11-rc5 (LKML); červen 2025, 6.16-rc (⚠ jen Phoronix) |
| S63–S64 | srpen 2024: *„At some point, fix something just turns into development. And this is that point.“* | ✅ | LKML archiv 2408.2/10955; originál: *„At some point "fix something" just turns into development, and this is that point.“* — zkrácen začátek (*„Yeah, no, enough is enough…“*), smysl beze změny |
| S65 | spory trvaly ještě rok | ✅ | srpen 2024 → srpen 2025 (commit *externally maintained* 28. 8. 2025) |
| S66 | v roce 2025 Linus bcachefs z jádra vyjmul | ✅ | 28. 8. 2025 *externally maintained* (6.17), 29. 9. 2025 *„Remove bcachefs core code“*, autor Linus (6.18) |
| S67 | dál existuje jako samostatný doplněk | ✅ | commit: *„It's now a DKMS module“* |
| S71 | v září 2018 Linus odstoupil | ✅ | 16. 9. 2018 (LWN 765108) |
| S72 | omluvil se za útoky na lidi v e-mailech a potřebuje čas změnit chování | ✅ | *„My flippant attacks in emails have been both unprofessional and uncalled for.“*; *„taking a break … to focus on improving his own behavior“* (LWN; originál na lore nečten) |
| S73 | Greg Kroah-Hartman převzal a dokončil 4.19 | ✅ | tag `v4.19` podepsal Greg 22. 10. 2018; `conclave.rst`: *„as was demonstrated by the 4.19 release in 2018“*. (Uživatel původně psal 4.18 — vyvráceno, základ C3) |
| S74 | za pár týdnů se Linus vrátil | ✅ | LWN 26. 10. 2018, *„has returned as the keeper of the mainline kernel repository“* (~6 týdnů) |
| S75–S77 | od roku 2026 psaný plán: do 72 hodin začnou správci jednat, kdo převezme; nástupce nejmenuje | ✅ | `Documentation/process/conclave.rst`, zařazen 25. 1. 2026 (v6.19): organizátor posledního Maintainers Summitu *„Within 72 hours … will open a discussion with the invitees of the most recently concluded Maintainers Summit“*; nástupce nejmenován |
| S83 | metafora krále a strážce | — | ze zdroje uživatele, není faktické tvrzení |

## Výslovnost (`project.json` → `pronounce`)

`Linus` → `Leenus` (Linus pro BCS 2007: *„in Finland it's pronounced
Lee-nus“*), `bcachefs` → `B cache F S`, letopočty slovy, `4.19` → *four
nineteen*. *Kroah-Hartman* a *Torvalds* bez zásahu (fonémy ověřeny).

## Co přeověřit před zveřejněním

- S10: jestli je 7.3 pořád poslední vydání (7.4 kolem začátku ledna 2027);
  při nové verzi přepsat čísla podle statistik LWN.
- S52: seznam platinových členů (mění se).
