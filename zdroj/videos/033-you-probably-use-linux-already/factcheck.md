# Fact check — 033 Linux — You Probably Use It Already

Ověřováno proti `script.md` (= `script 0.4.md`, 94 scén, **přečíslováno**
S01–S94). Ověřeno původně na 0.2, po škrtání 0.3 a po přečíslování 0.4
pokaždé znovu strojově překontrolováno. Postup podle CLAUDE.md:
vypsáno **každé** ověřitelné tvrzení, ne jen ta riziková. Čísla se
počítají, ne vzpomínají; zobecnění jen z primárního zdroje.

**Výsledek: 22 tvrzení, 20 prošlo beze změny, 1 opraveno ve scénáři
(pointa o planetách), 1 má omezenou trvanlivost.**

> **Čísla scén níž jsou z PŘEČÍSLOVANÉ 0.4** (S01–S94), ne z 0.2/0.3,
> ve kterých se ověřovalo. Převodní tabulka je v `precislovani.json`.
> Jediná dvě čísla v historickém významu jsou označená *(číslování 0.3)*.

> **Pozor na to, co vzniklo PŘI ÚPRAVĚ, ne ve zdroji.** Čtyři číselné
> kotvy (S17, S32, S55–S57, S70–S71) ve zdrojovém textu **nebyly** —
> dopsaly se 2026-09-08 na žádost uživatele. Ověřovaly se proto stejně
> přísně jako přejatá tvrzení, ne mírněji.

---

## S03 — „Maybe you have an iPhone" (implicitně: iPhone není Linux)

**Ověření.** iOS stojí na jádře **XNU** (Darwin), hybridu Mach + BSD.
S Linuxem nesdílí jádro. Protiklad ve větě je tedy věcně správný.

**Závěr: ✅ prošlo.**

---

## S11 — „In nineteen ninety-one, a twenty-one-year-old Finnish student named Linus Torvalds"

**Ověření.** Torvalds se narodil **28. 12. 1969** v Helsinkách, oznámení
poslal do `comp.os.minix` **25. 8. 1991**. Spočítáno: k tomu dni mu bylo
**21 let a 240 dní**. Student **Helsinské univerzity**, tedy „Finnish
student" sedí.

**Závěr: ✅ prošlo.** Věk je správný pro srpnové oznámení i pro celý
zbytek roku 1991 až do 28. 12.

---

## S12 — „It was basically a hobby project."

**Ověření.** Doslova Torvaldsova vlastní formulace z oznámení
25. 8. 1991: *„I'm doing a (free) operating system (just a hobby, won't
be big and professional like gnu)."*

**Závěr: ✅ prošlo.** Není to interpretace, je to citát.

---

## S13 — „a Unix-like system", „he released the source code"

**Ověření.** Linux je unixového typu (POSIX-like rozhraní), vyvíjen
původně proti Minixu. Zdrojový kód zveřejněn od verze 0.01 (září 1991);
licence GPLv2 od verze 0.12 (únor 1992). Věta říká jen „released the
source code", ne „pod GPL", takže platí i pro nejstarší verze.

**Závěr: ✅ prošlo.**

---

## S16 — „developed by thousands of people, and supported by companies, universities, independent developers and volunteers"

**Ověření.** Viz S17. Přispěvatelé jsou zaměstnanci firem i nezávislí;
LWN u posledního cyklu identifikovala **249 zaměstnavatelů**.

**Závěr: ✅ prošlo.**

---

## S17 — „The most recent release … took about nine weeks, and it brought in the work of two thousand six hundred and fifty-two developers."

**KOTVA DOPSANÁ AGENTEM.**

**Ověření.** LWN.net, vývojová statistika jádra **7.2** (vydáno
17. 8. 2026), počítaná přímo z gitového repozitáře:

| | |
|---|---|
| vývojářů | **2 652** (rekord, předchozí 2 479 u 7.1) |
| changesetů (bez merge) | 16 418 (druhý nejrušnější cyklus v historii) |
| identifikovaných zaměstnavatelů | 249 |
| prvních příspěvků | 613 (rekord, předchozí 530 u 7.1) |

Délka cyklu: 7.1 vyšlo **14. 6. 2026**, 7.2 **17. 8. 2026**, tedy
**64 dní = 9,1 týdne**. Proto „about nine weeks", ne deset — kadence
jádra je 9–10 týdnů (dva týdny merge window + sedm release candidates)
a tenhle konkrétní cyklus vyšel na spodní hranu.

**Závěr: ✅ prošlo, ale ⏳ MÁ OMEZENOU TRVANLIVOST.**

> **Aktualizováno 2026-09-08 před renderem masteru.** Původní znění
> mluvilo o 7.1 (2 479 vývojářů, „about ten weeks") a mezitím vyšlo
> **7.2**, takže tvrzení „the most recent release" přestalo platit.
> Přepsáno ve `script.md` i v osmi překladech; scéna se přemluvila.
> Je to přesně ten případ, na který upozorňovala předchozí verze
> téhle položky.
>
> Číslo **roste** (6.18: 2 134 → 6.19: 2 141 → 7.0: 2 362 → 7.1: 2 479
> → 7.2: 2 652), takže zastarává směrem dolů. Vyjde-li do zveřejnění
> jádro 7.3, ověř statistiku na LWN znovu — je to jediné číslo ve videu,
> které stárne.

---

## S18 — „one of the largest collaborative software projects humanity has ever created"

**Ověření.** Hedge „one of" tvrzení drží. Jádro má přes 40 milionů
řádků a přes 20 tisíc přispěvatelů od zavedení gitu (2005); srovnatelné
projekty (Chromium, LibreOffice) jsou menší v počtu přispěvatelů.
Superlativ *„the largest"* by doložit nešel, *„one of the largest"* ano.

**Závěr: ✅ prošlo.** Hedge je nutný a ve scénáři je.

---

## S22, S23 — „Linux isn't really one operating system. Linux is a kernel."

**Ověření.** `torvalds/linux` je jádro. Uživatelský prostor (GNU
coreutils, libc, init, desktop) dodává distribuce. Je to standardní
a nesporné rozlišení — právě o něj se vede spor „GNU/Linux".

**Závěr: ✅ prošlo.**

---

## S24 — „the part of the system that sits between software and hardware … It manages the processors, the memory and the devices"

**Ověření.** Odpovídá funkcím jádra: plánovač procesů, správa paměti,
ovladače zařízení, systémová volání. Zjednodušené, ale ne nepřesné.

**Závěr: ✅ prošlo.**

---

## S31 — „If you're using Android, you're already using the Linux kernel."

**Ověření.** Android staví na jádře Linuxu (dnes větev **Android Common
Kernel** odvozená z LTS jader). Google to uvádí ve vlastní dokumentaci
architektury Androidu.

**Závěr: ✅ prošlo.**

---

## S32 — „more than three billion active Android devices, in over a hundred and ninety countries"

**KOTVA DOPSANÁ AGENTEM.**

**Ověření.** Primární zdroj, Googlův vlastní blog, *„The Android Show:
I/O Edition"*, **13. 5. 2025**, doslova: *„As the world's most popular
OS with more than 3 billion active devices in over 190 countries."*

Formulace ve scénáři je **převzatá včetně obou hedge slov**
(„more than", „over"), takže se s časem nemůže pokazit směrem dolů.

> **Past pro překlad:** *billion* je britská miliarda, tedy 10⁹ —
> německy `Milliarden`, švédsky `miljarder`, polsky `miliardów`,
> italsky `miliardi`, španělsky `mil millones`, portugalsky
> `bilhões` (v pt-BR je `bilhão` = 10⁹, tedy sedí), francouzsky
> `milliards`. **Ne** `Billionen` / `billones`, to je o tři řády vedle.

**Závěr: ✅ prošlo.**

---

## S33 — „Android isn't simply Linux in the same sense as Ubuntu or Fedora."

**Ověření.** Android nepoužívá GNU libc (má Bionic), nemá klasický
`init` z distribucí, jinak řeší uživatelský prostor i balíčky.
Ubuntu i Fedora jsou naproti tomu klasické GNU/Linux distribuce.

**Závěr: ✅ prošlo.**

---

## S39 — „many routers run Linux"

**Ověření.** Většina firmwaru domácích routerů je odvozená z Linuxu
(OpenWrt a od něj odvozené vendorské firmwary, DD-WRT). Právě routery
byly předmětem vymáhání GPL, protože vendoři jádro použili — což je
nezávislý doklad, že tam Linux je.

**Závěr: ✅ prošlo.** Hedge „many" je namístě, jsou i routery na
BSD nebo VxWorks.

---

## S43 — „Linux is used in many smart televisions and other consumer electronics"

**Ověření.** Tři největší platformy chytrých televizí stojí na Linuxu:
**Tizen** (Samsung, přes 200 mil. přístrojů), **webOS** (LG, přes
130 mil.) a **Android TV / Google TV** (jádro Linuxu). Dohromady jsou
to podle různých metodik 60–80 % trhu. Roku je výjimka (vlastní systém).

**Závěr: ✅ prošlo.** Hedge „many" opět namístě.

---

## S48 — „Linux has become enormously important in server infrastructure"

**Ověření.** Doložitelné z jiné strany, než jsou odhady podílu:
Google, Meta, Amazon a Microsoft jsou samy mezi největšími přispěvateli
do jádra a provozují na Linuxu vlastní infrastrukturu (Google veřejně
popisuje interní distribuci odvozenou z Debianu). Věta je navíc
formulovaná kvalitativně („enormously important"), ne procentem —
na procento by byl potřeba primární zdroj a ten spolehlivý není.

> **Druhá věta téhož tvrzení ve scénáři už NENÍ.** V 0.2 stála
> v S54 *(číslování 0.3)* (*„Companies operating some of the biggest Internet services
> in the world rely heavily on Linux."*) a při škrtání 0.3 se
> vypustila jako opakování tehdejších S53 a S55. Ověření výš platilo pro obě.

**Závěr: ✅ prošlo.** A **záměrně tam žádné procento nedávej** —
běžně citovaná čísla o podílu Linuxu na serverech pocházejí ze
sekundárních přehledů s nejasnou metodikou.

---

## S55, S56, S57 — „a list of the five hundred most powerful supercomputers … All five hundred of them run Linux … on every single list since two thousand and seventeen"

**KOTVA DOPSANÁ AGENTEM. Nejsilnější číslo videa.**

**Ověření z primárního zdroje.** Vlastní statistika TOP500
(*Operating system Family / Linux*) — počet systémů s Linuxem
podle seznamů, čteno přímo z dat stránky:

| seznam | systémů s Linuxem |
|---|---|
| **6/2026** (nejnovější) | **500** |
| 11/2025 az 11/2017 | **500** (17 dalších seznamů v řadě) |
| 6/2017 | 498 |
| 11/2016 | 498 |

Tedy **500 z 500 na osmnácti po sobě jdoucích seznamech**, počínaje
listopadem 2017. Sedí to s nezávisle uváděným „poslední dva
neliunuxové systémy vypadly v listopadu 2017".

> **Formulace je vybraná tak, aby nepřestřelila.** Scénář říká
> *„Twice a year, someone publishes a list of the five hundred most
> powerful supercomputers"* — tedy popisuje **žebříček**, ne skutečnost.
> TOP500 je totiž **sebedeklarační**: stroj se do něj dostane, jen když
> ho provozovatel přihlásí a proběhne LINPACK. Utajené vojenské stroje
> v něm nejsou. Věta *„the world's five hundred most powerful
> supercomputers all run Linux"* by proto byla zobecnění za hranici
> zdroje; věta o seznamu je přesně to, co seznam dokládá.

**Závěr: ✅ prošlo.**

---

## S58 — „The same kernel that can be running inside a tiny embedded computer can also be running on machines containing enormous numbers of processors"

**⚠️ NAHLÁSIL UŽIVATEL 2026-09-08. Tvrzení v prvním průchodu vypsané
nebylo — je to díra ve fact checku, ne jen stylistika.**

**Ověření.** Doslova týž **binární** kernel to není a být nemůže.
Rozdíly jsou tři a všechny doložitelné:

| | |
|---|---|
| **konfigurace** | jedno mainline dřevo, ale jiný `.config` — embedded vypíná subsystémy, které superpočítač potřebuje, a naopak |
| **vendorské patche** | Android jede na **Android Common Kernel** (odvozeném z LTS mainline s androidími patchi), embedded často na BSP stromu výrobce, superpočítače na distribučním jádře (RHEL/SUSE) |
| **verze** | v jednu chvíli běží v provozu desítky různých LTS řad |

Co ale platí a je celé tvrzení scény: **je to týž kernel jako projekt,
tedy tentýž zdrojový strom.** Ovladač, plánovač i správa paměti mají
společný původ a patche se vracejí do mainline. Přesně proto se dá týž
kód použít v obou krajnostech měřítka.

**Závěr: ✅ prošlo, ale ⚠️ VYŽADUJE UPŘESNĚNÍ V OBRAZE — doplněno.**

Věta ve scénáři zůstává (říká *„the same kernel that can be running…"*,
tedy o kernelu jako o věci, ne o souboru). Diagram S58 ale sám o sobě
tvrdil víc jistoty, než scénář unese, takže do něj přibyl tlumený
popisek **`ONE CODEBASE, DIFFERENT BUILDS`**. Tři nezávislá čtení scény
— voiceover, text v obraze, kresba — se tím srovnala.

> **Kdyby to někdo v komentářích zvedl**, tohle je odpověď: stejný
> projekt a stejný zdrojový strom, jiná konfigurace a jiný build.
> Není to vytáčka — je to přesně ten důvod, proč Linux v obou
> krajnostech vůbec být může.

---

## S61 — „Cars run Linux in various systems, particularly infotainment and connected-car platforms"

**Ověření.** **Automotive Grade Linux** (projekt Linux Foundation,
nasazeno v Toyotě a Subaru) a **Android Automotive OS** (Volvo, Polestar,
GM, Renault) jsou obojí na jádře Linuxu. Hedge *„particularly
infotainment"* je **věcně nutný**: bezpečnostně kritické řídicí
jednotky (brzdy, airbagy, motor) na Linuxu neběží — tam jsou
certifikované RTOS podle ISO 26262. Věta to neříká a říkat nesmí.

**Závěr: ✅ prošlo — a hedge je nutná součást tvrzení, neškrtat.**

---

## S62 — „industrial equipment, robotics, drones, cameras, storage devices, network equipment"

**Ověření.** Doložitelné po položkách: ROS (Robot Operating System)
běží na Linuxu; PX4 a ArduPilot mají linuxové cíle; síťové OS
(Cumulus, SONiC, Junos, Arista EOS) stojí na Linuxu; NAS (Synology,
QNAP) taky; průmyslové PLC a HMI často embedded Linux.

**Závěr: ✅ prošlo.**

---

## S67 — „Linux has even made it into space. It has been used on spacecraft and space-related systems."

**Ověření.** SpaceX používá Linux (s real-time patchi) na primárních
letových počítačích Falconu 9 i Dragonu — trojitá redundance, tři
dvoujádrové x86. Na ISS byly navíc v roce 2013 uživatelské notebooky
převedeny z Windows na Debian.

**Závěr: ✅ prošlo.**

---

## S67b — „On the International Space Station, the laptops the crew works on were moved to Linux back in twenty thirteen."

**SCÉNA DOPLNĚNÁ 2026-09-08 na návrh uživatele — a ověřená dřív, než se
napsala.**

**Ověření.** V roce 2013 převedla United Space Alliance notebooky sítě
**OpsLAN** na ISS z Windows XP na **Debian 6**. Keith Chuvala (United
Space Alliance) k tomu: *„We migrated key functions from Windows to
Linux because we needed an operating system that was stable and
reliable — one that would give us in-house control."* Stanice má kolem
**140 notebooků**, z toho zhruba 80 v provozu naráz.

**Závěr: ✅ prošlo — ale JEN v tomhle rozsahu.**

> **Rozsah je tady celé tvrzení.** Doložené jsou **notebooky posádky**,
> ne řídicí počítače stanice. Věta ve scénáři proto říká *„the laptops
> the crew works on"*, ne „the space station runs Linux", a diagram
> ukazuje notebook s popiskem `CREW LAPTOPS`, kdežto silueta stanice je
> záměrně tlumená kulisa. Kdyby obraz naznačil, že na Linuxu běží řízení
> ISS, tvrdil by víc než scénář i než zdroj.

## Měsíc: NEDOLOŽENO, do scénáře nešel

Uživatel se ptal, jestli Linux nebyl i na Měsíci. **Doložit se to
nepodařilo** a proto ve videu není. Prošlé mise: Odysseus (IM-1,
2024), Blue Ghost (2025, letový software Rocket Lab **MAX**, ne Linux),
Peregrine (2024, na Měsíc nedoletěl), Chandrayaan-3. U žádné není
použití Linuxu veřejně doložené.

> **Pointa videa tím není ohrožena:** Měsíc není planeta, takže
> *„Two. Earth and Mars."* by platilo, i kdyby se Linux na Měsíci
> jednou objevil.

---

## S69 — „NASA's Ingenuity helicopter, which operated on Mars, used a Linux-based flight computer."

**Ověření z primárního zdroje.** JPL/NASA, *„Meet the Open-Source
Software Powering NASA's Ingenuity Mars Helicopter"*: vrtulník běžel
na **Linuxu** nad rámcem **F Prime** (open source, vyvinutý v JPL),
na běžném **Qualcomm Snapdragon 801**. Citát pracovníka JPL:
*„we're flying an open-source operating system and an open-source
flight software framework."*

**Závěr: ✅ prošlo.** Doloženo přímo NASA/JPL, ne z druhé ruky.

---

## S70, S71 — „It was designed to make five test flights. It made seventy-two."

**KOTVA DOPSANÁ AGENTEM.**

**Ověření.** NASA: Ingenuity byla technologická demonstrace navržená
na **nejvýš pět zkušebních letů během třiceti dnů**. Ve skutečnosti
zvládla **72 letů** za téměř tři roky, celkem 128,8 minuty ve vzduchu.
První let 19. 4. 2021, poškození listů rotoru při přistání 18. 1. 2024,
konec mise oznámen 25. 1. 2024.

**Závěr: ✅ prošlo.** Poměr pět ku sedmdesáti dvěma je doložený, ne
zaokrouhlený.

---

## S77 — „the operating-system kernel that has run on the greatest number of planets" — ❌ OPRAVENO

**Tvrzení ve zdroji bylo NEPRAVDIVÉ.** Původní znění:

> *As far as we know, it is the operating-system kernel that has run
> on the greatest number of planets.*

**Ověření.** Protipříklad existuje a je snadný: **VxWorks** (Wind River)
běžel na Marsu na **Sojourneru** (1997), **Spiritu a Opportunity**,
**Curiosity** i **Perseverance** — a samozřejmě i na Zemi. To je
rovněž **dvě planety**. Linux tedy není v čele, je nanejvýš **na
děleném prvním místě**, a proti VxWorks má na Marsu jediný stroj proti
pěti misím.

Hedge *„As far as we know"* to nezachrání — protipříklad je veřejně
známý a doložený výrobcem, takže „pokud víme" je právě to, co víme
špatně.

**Oprava ve scénáři** (2026-09-08). Superlativ vypuštěn, beat
*„Two. / Earth and Mars."* i pointa *„Not bad for a hobby project."*
zůstávají netknuté:

> *Which gives Linux a rather unusual statistic.
> **The number of planets it has run on.***

Nová formulace nic netvrdí o pořadí — jen otevře otázku, na kterou
odpoví další scéna. Vtip stojí na tom, že se u softwaru taková
statistika vůbec vede, ne na rekordu.

**Závěr: ❌ neprošlo → ✅ opraveno.** Je to přesně případ z CLAUDE.md
*„do fact checku patří i věty, které vznikly slitím nebo zkrácením"* —
jen o krok dál: tady byla vada už ve zdrojovém textu a zněla věrohodně.

---

## S88 — „It started as a small project by a university student in Finland."

**Ověření.** Viz S11. Helsinská univerzita, Finsko.

**Závěr: ✅ prošlo.**

---

## Co se NEOVĚŘOVALO a proč

- **S06** („Linux má pověst složitého") — tvrzení o pověsti, ne o faktu.
- **S42** („chytré televize nejsou televize, jsou to počítače s
  obrazovkou") — řečnická figura.
- **S44** (Netflix a dálkové ovládání) — hedge *„may be involved"*
  je ve větě záměrně; tvrdí jen možnost.
- **S84** („dozens of devices around you") — odhad formulovaný jako
  odhad („probably").

## Zdroje

| tvrzení | zdroj | typ |
|---|---|---|
| jádro 7.2, 2 652 vývojářů | LWN.net, *Development statistics for the 7.2 kernel*, `lwn.net/Articles/1088776/` | primární (počítáno z gitu) |
| TOP500, 500 z 500 | `top500.org/statistics/details/osfam/1/`, data seznamu 6/2026 | primární |
| 3 miliardy Androidů | `blog.google/products/android/the-android-show-io-2025/`, 13. 5. 2025 | primární (Google) |
| Ingenuity na Linuxu | JPL, *Meet the Open-Source Software Powering NASA's Ingenuity Mars Helicopter* | primární (NASA/JPL) |
| Ingenuity 5 → 72 letů | NASA Science, stránka mise Ingenuity | primární (NASA) |
| VxWorks na Marsu | Wind River, tisková zpráva k MSL Curiosity | primární (výrobce) |
| Torvalds 1991 | oznámení v `comp.os.minix`, 25. 8. 1991 | primární |
