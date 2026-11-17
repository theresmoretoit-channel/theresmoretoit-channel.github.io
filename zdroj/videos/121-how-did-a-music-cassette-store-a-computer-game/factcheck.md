# 121 — fact check scénáře v0.1

Zdroje a výpočty k číslům jsou v `factcheck-zaklad.md` (odkazy v tabulce
jsou na jeho položky, `#4` = řádek 4 tamní tabulky). Tady je jen
přiřazení ke scénám a závěr.

| scéna | tvrzení | ověření | závěr |
|---|---|---|---|
| S06 | ZX Spectrum, britský, 1982 | #8a: 23. 4. 1982 | ✅ |
| S07–S08 | dva druhy pulzu; jednička = týž pár, každý pulz dvakrát delší, tón o oktávu níž (v0.2: pulzy, ne „dva tóny“) | #4, ROM SA-BYTES: 855 / 1 710 T, 2 047 / 1 023 Hz | ✅ |
| S09 | „around fourteen hundred" za sekundu | #4, #7b: 1 364 (smíšená data) až 1 535; dobové „1 500" | ✅ |
| S09b | program z nul se nahraje rychleji | plyne z #4 | ✅ |
| S12 | 1975, setkání v Kansas City, data jako zvuk na běžné kazety | #12: sympozium BYTE 7.–8. 11. 1975 | ✅ |
| S12b | 1 = 8 cyklů vysokého tónu, 0 = 4 cykly nízkého, 300 bit/s | #12: 2 400 / 1 200 Hz, BYTE 2/1976 | ✅ |
| S13 | Apple II a TRS-80 na běžný magnetofon | 5B | ✅ |
| S15 | 1983, časopis, průzkum, 9 z 10 nových majitelů C64 kupuje mechaniku | **ověřeno agentem přímo ve skenu**: Compute!'s Gazette 12/1983 s. 6, úvodník: *„A recent survey showed that 90 percent of new Commodore 64 owners bought a disk drive with their computer"*. Kdo průzkum dělal, neuvádí, proto „one magazine reported a survey". 97 % (CGW 1986) jen z druhé ruky, nepoužito | ✅ |
| S17 | £125, bez úložiště, jakýkoli magnetofon | #8b (16K), #9a (EAR/MIC, žádná vlastní jednotka) | ✅ |
| S18 | „millions of kids across Europe" | ~5 mil. Spectrer (#8c), k tomu C64 na kazetách (5A) | ✅ |
| S18b | po mnoha nahráváních šlo poznat hru podle zvuku | vzpomínka uživatele a běžná zkušenost pamětníků; formulace *you could even tell*, ne tvrzení o všech hrách. Fyzikálně podložené: délka hry, pauzy mezi bloky a vlastní nahrávací rutiny dávají každé hře jiný rytmus | ✅ (zkušenost, ne měření) |
| S21 | hučení ~800 Hz, asi 5 s | #2a, #2b: 807 Hz, 4,99 s | ✅ |
| S22 | pilot nenese data, slouží k zachycení signálu | ROM LD-BYTES | ✅ |
| S23 | dva rychlé pulzy, synchronizace | #3: 667 + 735 T | ✅ |
| S24 | hlavička 19 bajtů: jméno do 10 znaků, typ, délka | #5 | ✅ |
| S25 | druhé hučení 2 s, pak data | #2b: 2,00 s; mezi bloky 1 s ticha | ✅ |
| S26 | bajt = 8 not, mezi bajty žádné mezery | #4 (ROM: *„no gaps… between bytes"*) | ✅ |
| S27–S28 | měří se čas mezi hranami, krátký pár 0, dlouhý 1 | #4 (práh ~2 400 T na pár) | ✅ |
| S28b–c | zvuk na začátku je skutečný program podle těchto pravidel; Spectrum ho nahraje | `zvuk/spectrum.py`, cizí dekodér tzxtools přečetl bajt po bajtu | ✅ **ověřeno v emulátoru 2026-10-22** (`zvuk/spectrum_test.py`, emulátor `zx` 48K: napíše `LOAD ""`, pulzy jdou skutečnou rutinou ROM, bez pasti na rychlé nahrávání). Program naběhl a vypsal *THERE'S MORE TO IT* (`0 OK, 20:1`) **ve všech třech variantách**. **Znovu 2026-10-23 po prodloužení programu o kresbu kazety** (790 B dat): kazeta + nápis, `0 OK, 80:2`, md5 obrazovky `ae779f94…` shodné pro čistý signál, Opus i AAC; negativní kontrola dál *R Tape loading error, 0:1*. Původní znění: čistý signál, render (AAC 192k/48 kHz) → Opus 128k, render → AAC 128k/44,1 kHz; obrazovky bajtově shodné. **Negativní kontrola:** 20 ms ticha uprostřed dat → *R Tape loading error, 0:1*, hlavička přitom prošla. Neověřeno na skutečném hardwaru a na zvuku staženém přímo z YouTube (až po nahrání) |
| S29–S30 | obrázek se nahrává v pruzích po osmi řádcích, po třetinách, barvy nakonec shora dolů | rozložení paměti obrazu Spectra: 6 144 B bitmapy ve třech třetinách prokládaně, pak 768 B atributů | ✅ **ověřeno simulací 2026-10-23** (`diagrams/gen/obrazek.py`): bajty se plní v pořadí adres obrazové paměti; assert, že po 512 B jsou v horní třetině jen řádky 0 a 1 každého znaku (tedy proužky po osmi řádcích) a po 2 048 B je hotová celá horní třetina; atributy (barvy) až za bitmapou, po řádcích znaků shora dolů |
| S31 | obrázek ~40 s, hra ~5 min | #7a: 6 912 B / 170,6 B/s = 40,5 s; 48K hra ≈ 5:00 | ✅ |
| S32–S34 | na konci každého bloku jeden bajt, všechny bajty bloku přes XOR (v0.2: jmenovitě XOR, ne „součet“) | #6 | ✅ |
| S35 | hláška *R Tape loading error* (v obraze) | #6, ROM tabulka hlášek | ✅ |
| S37 | poškozená hlavička chybu nedá, Spectrum poslouchá dál | #6 (LD_LOOK_H) | ✅ |
| S39 | C64 nahrává každý blok dvakrát, druhá kopie zachraňuje první | #10a | ✅ |
| S40 | vestavěnou rutinou 40 kB ≈ 12,5 min | #10b (NTSC; PAL 13 min) | ✅ |
| S41 | vlastní loadery až zhruba 10× rychlejší | #10d: TurboTape ~8× (Compute! 1/1985), proto „up to about" | ✅ |
| S43–S44 | hlasitost, rychlost pásky | obecný princip, plyne z měření délky pulzů | ✅ |
| S45–S46 | azimut, šroubováček do dírky u hlavy | #9b: Sinclair User #43 (1985), #86 (1989) | ✅ |
| S50b | kopírování hry jako kopírování alba, dva magnetofony a kabel | obecně známé, hra je zvuk | ✅ (bez čísla) |
| S51 | Atari: program na jedné stopě, hlas na druhé, přes televizi při nahrávání | 5D: ANTIC 10/1982 | ✅ |
| S52–S53 | Rádio Bělehrad vysílalo programy, posluchači nahrávali, ~150 v letech 1983–86 | #14 (Ventilator 202, druhotné zdroje se shodují) | ✅ |
| S54 | ČSSR: televize, program jako zvuk pod závěrečnými titulky | #16b (Gruber, ČST Ostrava 1986, 1988). Rozhlas nedoložen, neříká se | ✅ |
| S55–S56 | 1983, Pete Shelley, program pro Spectrum na konci vinylu; přes kazetu; text v rytmu písní | #17a (*XL1*, za zamčenou drážkou) | ✅ |
| S58–S59 | program pro jeden stroj je pro jiný šum | formát: Spectrum (#4) a C64 (#10b) se kódují jinak | ✅ |
| S60 | 1982, nizozemský rozhlas, BASICODE, jeden formát + překladač pro každý počítač | #15 (NOS Hobbyscoop, „Bascoder") | ✅ |
| S63 | datacentra archivují na pásky | #18 | ✅ |
| S64 | LTO-9 18 TB | #18a | ✅ |
| S65 | přepočet kapacity: ~29 mil. kazet, přes 3 000 let nahrávání (v0.2: „converted…, that capacity would…“, tedy přepočet, ne způsob ukládání) | výpočet: 18 TB / (1 800 s × 170,6 B/s × 2 strany) = 29,3 mil. C60; 18 TB / 170,6 B/s = 3 343 let | ✅ |
| S70 | program pod závěrečnými titulky „jako ČST" | viz S54, S28b | ✅ (jako S28b) |

**Pravidla z rešerše, co neříkat** (konec `factcheck-zaklad.md`):
„1 500 bit/s" jako přesné číslo, Shakin' Stevens „na desce", „americké C64
z kazet", „Československý rozhlas", 17 mil. C64.
