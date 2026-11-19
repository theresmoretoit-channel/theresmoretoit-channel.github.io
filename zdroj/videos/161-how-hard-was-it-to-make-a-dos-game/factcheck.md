# 161 — fact check scénáře v0.3 (2026-11-17)

Podklad: `factcheck-zaklad.md` (zdroje a značky **P / S / M / Pam**).
Tady jen tvrzení scénáře, jejich ověření a závěr. ✅ platí, ⚠️ platí
s formulací, jak stojí, ❌ opraveno.

## Úvod (S01–S07)

| scéna | tvrzení | ověření | |
|---|---|---|---|
| S01 | Doom 1993, 4 MB | README: *386 or better with 4 megs of RAM*; vydání 10. 12. 1993 | ✅ |
| S02 | 4 MB ≈ jedna fotka v telefonu | 12Mpx JPEG ~2–5 MB, HEIC ~1,5–2,5 MB (M) | ⚠️ *about the size* — řádově sedí |
| S03 | bez 3D akcelerátoru, kreslí procesor | 3D karty pro PC až 1996 (3dfx Voodoo); Doom kreslí softwarově | ✅ (v0.1 „no graphics chip“ ❌ opraveno) |
| S04 | Unity, Unreal se starají o grafiku, zvuk, paměť, hardware | obecně | ✅ |

## Paměť (S08–S27)

| scéna | tvrzení | ověření | |
|---|---|---|---|
| S08 | IBM PC 1981, adresuje 1 MB | IBM 5150 (8/1981), 8088 s 20bitovou adresou | ✅ |
| S09–S10 | 640 KB programům, 384 KB vyhrazeno pro video, karty, BIOS | rozdělení adresního prostoru PC | ✅ (*reserved*, ne *taken*) |
| S11 | DOS „normally started programs inside that space“ | program se zavádí do konvenční paměti; víc přes EMS/XMS/extender | ✅ (v0.2 „every program“ zmírněno) |
| S12–S13 | 640K-citát, Gatesovi připisovaný, bez dokladu, popírá | Quote Investigator (verdikt *mixed*), Gates 1996 | ✅ — neříkáme „myth“ |
| S14 | počátek 90. let 4 nebo 8 MB | běžná výbava 486 | ✅ |
| S15 | hlášky „not enough memory“ | běžné u her i DOSu | ✅ |
| S17–S19 | EMS: 64KB okno v horní části 1. MB, 4 stránky po 16 KB, výměna | LIM EMS 3.x, manuál Everex 1985 | ✅ (metafora knihy — přirovnání) |
| S20 | extended memory přes HIMEM | HIMEM.SYS, XMS | ✅ |
| S22 | ovladače ujídají konvenční paměť, pokud je nenahraješ nahoru | LOADHIGH/DEVICEHIGH od MS-DOS 5.0 (1991), na 386+ s EMM386 | ✅ |
| S23–S24 | CONFIG.SYS, AUTOEXEC.BAT; EMS × NOEMS × maximum volné paměti | EMM386 NOEMS = UMB bez EMS | ✅ |
| S25–S26 | MS-DOS 6 (1993) menu při startu, konfigurace podle hry | MultiConfig, `[menu]`, `MENUITEM`; 6.0 vydán 3/1993 | ✅ |
| S27 | někdo měl položku skoro pro každou hru | svědectví uživatele; netvrdíme „většina“ | ✅ |

## DOS/4GW (S28–S35)

| scéna | tvrzení | ověření | |
|---|---|---|---|
| S29 | od 386 32bitový protected mode, prostor až 4 GB | 32bitová lineární adresa | ✅ (v0.2 „all of the memory directly“ zmírněno) |
| S30 | DOS ho nepoužívá | DOS běží v reálném režimu | ✅; callback 156 (S14 tam: 80286 protected mode) |
| S31–S32 | DOS/4GW nejznámější extender, dodávaný s Watcom C | Rational Systems → Watcom run-time (v0.6: „came free“ → „came bundled“; zdarma nebyl samostatný produkt, ale běhové prostředí přibalené k překladači) | ✅ |
| S33 | přepne procesor, dá hře paměť nad limit DOSu | dokumentace DOS/4GW, DPMI | ✅ |
| S34 | DOS dál poskytuje služby (soubory) | extender překládá volání DOSu do reálného režimu přes buffery pod 1 MB (specifikace DPMI) | ✅ |
| S35 | jeho jméno problesklo při startu | banner *DOS/4GW Protected Mode Run-time…* (šel potlačit `DOS4G=quiet`) | ✅ |

## Grafika (S36–S46)

| scéna | tvrzení | ověření | |
|---|---|---|---|
| S37 | Mode 13h, 320 × 200, 256 barev, jeden z nejpoužívanějších | Wikipedia Mode 13h/VGA | ✅ (*one of the most widely used*) |
| S38 | pixel = bajt, zápis čísla do paměti | lineární framebuffer od A000:0000 | ✅ |
| S39–S40 | 64 000 B, pod 64 KB, jeden segment | 64 000 < 65 536 | ✅ M |
| S41–S42 | kreslení přímo → poloviční snímky, blikání; skrytý buffer, kopie do video paměti | double buffering | ✅ (v0.1 „at once“ ❌ opraveno) |
| S43 | Abrash, 1991, Mode X | DDJ 7/1991, název od Abrashe | ✅ |
| S44 | část VGA, na kterou většina nesáhla | planární „unchained“ režim — dokumentovaný, ale málo známý | ⚠️ formulace nesmí říct „undocumented“ — neříká |
| S45–S46 | čtvercové pixely, víc obrazovek, přepnutí; těžší programování | 320 × 240, page flipping; roviny | ✅ |

## Zvuk (S47–S58)

| scéna | tvrzení | ověření | |
|---|---|---|---|
| S48 | reproduktor stavěný na pípání | PC speaker, obdélníkový signál | ✅ |
| S49 | zvukové karty a další zvukový hardware | v0.6 doplněno: MT-32 není karta, ale externí MIDI modul (karta byla LAPC-I); obraz S49/S52/S57 ho kreslí jako skříňku | ✅ |
| S50 | AdLib s čipem Yamaha (FM), Sound Blaster i nahraný zvuk | YM3812/OPL2; SB 1989 s DAC | ✅ |
| S51 | MT-32 drahý, bohatší nástroje; GUS | $550–697 podle zdroje (cenu neříkáme) | ✅ |
| S52 | každá karta vlastní ovladače | | ✅ |
| S53–S54 | port, IRQ, DMA; u Sound Blasteru 220, 7, 1 | tovární nastavení SB; pozdější IRQ 5 → *Usually.* | ✅ |
| S55 | špatně → ticho nebo zamrznutí | běžná zkušenost | ✅ |
| S56–S57 | John Miles 1991, knihovna pro mnoho karet přes jedno rozhraní | AIL (MobyGames, Wikipedia) | ✅ |
| S58 | „another layer“ | netvrdíme první | ✅ |

## Rychlost (S59–S68)

| scéna | tvrzení | ověření | |
|---|---|---|---|
| S63–S63b | adresa = řádek × 320; na starších procesorech násobení drahé | 8088: MUL 16 bit **118–133 taktů**, posun **2**; 386: MUL 9–22 | ✅ |
| S64–S65 | 320 = 256 + 64, mocniny dvou, dva posuny a součet | M | ✅ |
| S67–S68 | Sawyer, Transport Tycoon 1994, téměř celý v assembleru | OpenTTD wiki, Wikipedia | ✅ (bez „99 %“ — to je RCT) |
| S67 (obraz) | snímek OpenTTD, ne Transport Tycoonu | popisek v obraze „SHOWN AS OPENTTD, A FREE REMAKE“; originál volně licencovaný není (v0.6) | ✅ |
| ~~S60–S61~~ | ~~MIPS 1993 × dnes~~ | škrtnuto v v0.2 | — |

## Wing Commander (S69–S74b)

| scéna | tvrzení | ověření | |
|---|---|---|---|
| S70 | 1990, chyba, termín blízko | vydání 26. 9. 1990; Demarest: *„We had to ship ASAP.“* (2009) | ✅ |
| S71–S72 | při ukončení spadl memory manager; Demarest přepsal hlášku hexeditorem | Demarest 2009; *Dirty Coding Tricks II* (Game Developer 2010) | ✅ |
| S73 | *„Thank you for playing Wing Commander.“* | Demarest | ✅ |
| S74 | našli chybu, vtip se do hry nedostal | Demarest: *„once we found the cause … couldn't in good conscience leave the hack in there“*; WC CIC prohledal binárky (9/2023) | ✅ |
| S74b | hráči si ho pamatují; pozdější hry Originu se tak loučily | WC Academy *„Thank you for Playing Wing Commander Academy!“*, Privateer *„Thanks for playing Privateer.“* (WC CIC 2/2024); totéž se uvádí u Ultimy VII | ✅ |

## Doom (S75–S89)

**S75 (obraz, v0.6):** snímek enginu Doomu s grafikami Freedoom (BSD), ne originální Doom; popisek v obraze to říká.

| scéna | tvrzení | ověření | |
|---|---|---|---|
| S76 | DOS/4GW, 32bitový program | Doom Wiki; Watcom | ✅ |
| S77–S78 | FPU nebylo jisté; pevná čárka, dolních 16 bitů zlomek | 386 a 486SX bez FPU; `m_fixed.h` 16.16 | ✅ |
| S80–S81 | plochý půdorys s výškou podlahy a stropu; místnost nad místností ne; nahoru/dolů pořádně ne | Wikipedia Doom engine | ✅ |
| S82 | před hraním nástroj rozřeže mapu do BSP | node builder | ✅ |
| S83 | průchod stromem zepředu dozadu od strany hráče, přeskakuje neviditelné | `R_RenderBSPNode`: nejdřív strana kamery, druhá jen při viditelném bounding boxu | ✅ |
| S85 | vyvíjen na NeXTech, přeložen pro DOS | Wikipedia, Doom Wiki | ✅ |
| S86 | specializace pomohla běhu na 386 | výklad | ✅ |
| S88 | Raven: Heretic 1994, Hexen 1995 | Wikipedia | ✅ |
| S89 | Doom pomohl zavést licencování enginů | Wolfenstein 3D licencován dřív — proto *helped establish*, ne „first“ | ✅ |

## Závěr (S90–S96)

Výklad a otázka do komentářů, žádné nové faktické tvrzení. S94
„gigabytes of assets, millions of polygons“ — obecně platí.

## Otevřené

- S02 fotka: kdyby uživatel chtěl přesnější číslo, *„a few photos“*
  nebo *„one photo“* — obojí řádově správně.
- Výslovnost DOS, MS-DOS, HIMEM, 13h ověřit poslechem po TTS.
