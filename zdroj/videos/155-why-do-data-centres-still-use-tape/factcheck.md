# 155 — fact check (scénář v0.6, 2026-11-14)

Zdroje s odkazy jsou v `factcheck-zaklad.md`; tady je tvrzení po
scénách. **P** primární (výrobce, konsorcium, instituce), **S** tisk,
**V** výrobce pásek o vlastní věci. Nadpis nese ID scény a doslovný
fragment, `grep` ho musí najít v té scéně.

### S01 — „five minutes later"
48K hra na Spectru ~5 min (121 `factcheck-zaklad.md`: ~1 364 bit/s,
393 216 bitů → 4:48 + úvodní tóny). ✅

### S02/S03 — „still keep their archives on tape"
Doslovně poslední věta 121 (S63). ✅

### S05 — „around forty thousand Gmail users"
Únor 2011 (od 27. 2.), Google: 0,02 % uživatelů; tisk přepočítává na
~40 000 účtů (S). Číslo „40 000" Google sám neuvedl, je to odvozené. ✅
s výhradou — „around".

### S06/S07 — „The bug reached those too"
Ben Treynor (Google): chyba v aktualizaci úložného softwaru; *„in some
rare instances software bugs can affect several copies of the data"*
(P přes DCK). Kopie v různých datacentrech: Google to o Gmailu uvádí
obecně. ✅

### S08 — „hours instead of milliseconds"
Treynor doslova *„it's taken us hours to get the email back instead of
milliseconds"*. Část uživatelů čekala až ~5 dní (S) — „hours" je citát,
ne celá pravda; ponecháno, protože je doslovný. Pošta *„was never lost"*
(P). ✅

### S09/S10 — „an exabyte of data"
CERN 17. 12. 2025: *„One exabyte of experimental data has now been
gathered from the LHC… Most of the data is stored using magnetic tape…
currently takes up 60 thousand tapes"* (P). 1 EB = 10⁶ TB. ✅
(Opraveno z „more than an exabyte": CERN píše „one exabyte".)

### S13 — „In 1951, the UNIVAC I computer"
UNISERVO, páskový pohon UNIVAC I (1951), páska z niklované fosforbronzi
(„Vicalloy"), ½ palce (S, CHM). První pevný disk IBM 350 RAMAC 1956. ✅

### S14/S15 — „HP, IBM and Seagate"
Společná práce od 1997, specifikace 1998 (S); dnes HPE, IBM, Quantum (P
spec. list Fujifilmu: ochranné známky). ✅

### S16 — „The first cartridge, in 2000"
LTO-1, 100 GB nativně, 2000 (S). ✅

### S17 — „holds up to forty terabytes"
LTO-10 30 a 40 TB nativně (P lto.org). 40 TB / 100 GB = 400×. Rozměr
kazety se nemění: 102,0 × 105,4 × 21,5 mm (P Fujifilm). ✅

### S18 — „squeezed two and a half times"
100 TB komprimovaně při 2,5:1 (P lto.org). Foto a video už
komprimované — obecně platí. ✅

### S19 — „eight hundred million games"
40·10¹² / 49 152 B = 813,8 milionu. ✅

### S20 — „takes more than a day"
400 MB/s nativně (P). 40 TB / 400 MB/s = 100 000 s = 27,8 h. ✅

### S21 — „more than three billion"
400 MB/s × 8 = 3,2 Gbit/s; Spectrum ~1 364 bit/s → 2,35 mil.×. ✅

### S23 — „more than a kilometre of tape"
1 035 m (30 TB, P Quantum/HPE), 1 337 m (40 TB, P spec. list Fujifilm
02/2026). ✅

### S24 — „many times thinner"
Šířka 12,65 mm (= ½ palce), tloušťka **4,0 µm** (40 TB, P Fujifilm);
vlas ~50–100 µm → 12–25× tenčí. ✅

### S25/S26 — „more than fifteen thousand"
15 104 stop (P lto.org). 12,65 mm / 15 104 = 0,84 µm je horní mez
(datové pásy nezabírají celou šířku) → < 1/1000 mm. ✅

### S27/S28 — „thirty-two at once"
LTO-10: 32kanálová hlava (P Spectra datasheet, IBM). 15 104 / 32 = 472
průchodů → „hundreds of passes". Serpentinový zápis ✅

### S31 — „servo patterns are written onto it"
Servo stopy se zapisují při výrobě (obecně známé u LTO; LTO-10 má nový
servo vzor, S Blocks & Files). ✅

### S33 — „the head even tilts slightly"
IBM (Kevin Judd, DSA 2026): mechanika sleduje stav pásky a při
nesouladu mění náklon hlavy; kompenzuje natažení a smrštění (TDS) (P).
Teplo a vlhkost jako příčina TDS: obecně známé. ✅

### S34 — „particles\nof barium ferrite" / „iron oxide"
LTO-10: baryum-ferit dopovaný stronciem (P lto.org). Kazety typu I
oxid železa. ✅

### S36 — „Just behind the write head"
Read-while-write: každý zapisovací prvek mezi dvěma čtecími (P IBM),
vadný blok se zapíše znovu dál. ✅

### S37 — „rebuild the data"
Dvouúrovňový Reed-Solomon (C1/C2) — obecně známé. ✅

### S38/S39 — „The LTO-9 specification allows"
Neopravitelná chyba 1 na 10²⁰ bitů = 1,25·10¹⁹ B = 12,5 EB (S
TechTarget podle LTO, V Fujifilm). CERN 1 EB → ~12×. Je to
specifikace, ve scénáři „allows". ✅

### S41/S45 — „taken out\nof the library"
Air gap: vyjmutí z knihovny — obecné. Gmail: *„since the tapes are
offline, they're protected from such software bugs"* (P). ✅

### S46 — „written only once"
WORM (P lto.org); u LTO-10 jen 30TB kazeta (P Fujifilm). „Some" sedí. ✅

### S47 — „uses no power at all"
Kazeta na polici bez napájení — fyzikálně jisté. ✅

### S48 — „around thirty years"
Archivní životnost 30 let (V datasheet HPE), za předepsaných podmínek;
ve scénáři „Makers rate… if they're stored properly". ✅

### S50 — „a few thousandths of a second"
Průměrný přístup HDD ~4–12 ms. ✅

### S52 — „around a minute"
LTO-9 průměr k prvnímu souboru 45 s (FH) / 60 s (HH) (P Oracle);
IBM 45–73 s od začátku pásky. 60 s / 10 ms = 6 000× → „thousands". ✅

### S57 — „nearly twenty thousand slots"
LLNL: 23 racků, 19 620 slotů (computing.llnl.gov) / 19 575 (Spectra),
**294 PB** nekomprimovaně (P). Pásky IBM TS1155, ne LTO — scénář LTO
neříká. ✅

### S64/S66 — „about ten billion yen"
Fujifilm 29. 10. 2026: ~10 mld. jenů, kapacita ~5× proti FY2025,
FY2026–28 (= „within three years"), důvod *„growing data archiving
demand accompanying the spread of generative AI"* (P). „One of the
biggest makers": Fujifilm o sobě tvrdí největší podíl (V). ✅

### S68 — „a hundred times less densely"
LTO-9 ~12 Gb/in² vs HDD 1,02 Tb/in² (2021) = 85×; nejnovější HDD hustší
(S TechRadar, techfinitive). „Roughly a hundred" ✅.

### S69 — „five hundred and eighty"
IBM Research + Fujifilm, prosinec 2020: 317 Gb/in² na prototypu SrFe,
potenciál ~580 TB na kazetu (P IBM blog). Prototyp, ne produkt. ✅

### S72/S73 — „two generations old"
lto.org: do LTO-7 zápis o 1, čtení o 2 zpět; LTO-8 a 9 o 1; LTO-10
nepodporuje zpětnou kompatibilitu (P). Tabulka Fujifilmu totéž. ✅

### S74 — „Every few years"
Migrace archivů na nové médium — obecná praxe; konkrétní interval CERNu
(4–5 let, uvádí ChatGPT) primárně neověřen, proto ve scénáři není. ✅

### S77 — „More than forty years later"
Spectrum 1982 → 2026 = 44 let. ✅

## Doplněno ve v0.5 (připomínky uživatele po prvním draftu)

### S37 — „error-correcting codes"
LTO chrání každý datový blok dvourozměrným Reed-Solomonovým kódem (C1/C2,
P IBM/lto.org); „error-correcting codes" je obecné a přesné. ✅
S37b slibuje samostatné video o samoopravných kódech — plán uživatele,
v YT Studiu karta na to video, až bude zveřejněné.

### S51b — „rewinding a cassette"
Analogie: sekvenční přístup u audiokazety, převíjení k písničce / hře
(121). Nepřesnost žádná. ✅

### S57b — „three hundred million gigabytes"
294 PB (S57) = 294 000 000 GB; scénář říká „about three hundred
petabytes", tedy 300 · 10⁶ GB (desítkové předpony jako u výrobců). ✅

### S73b — „LTO-10 changed their pattern"
LTO-10 má nový formát servo stop (úhel 36° místo dosavadního),
kvůli přesnějšímu polohování hlavy nad víc a užšími stopami; k tomu
hlava s naklápěním (S33) (S Blocks & Files 2025-07-29, citace IBM;
S heise online, IBM). Mechanika je „skoro celá nová: ASIC, hlava,
složení média, zavádění" (S Symply). ✅
https://www.blocksandfiles.com/tape/2025/07/29/why-lto-10-fell-short-on-speed-and-backward-compatibility/1588360
https://heise.de/-10420420

### S73c — „would have cost capacity"
LTO Program: zachování zpětné kompatibility by vyžadovalo zásadní
kompromisy, hlavně v kapacitě LTO-10 (P lto.org, citováno Blocks & Files). ✅
„Older tapes carry the old pattern" plyne ze S31 (servo stopy se píšou
z výroby) a nového formátu. ✅

### S74b — „Archives copy on their own schedule"
Spectra Logic (CTO): migrovat po 5–7 letech, nejvýš po 10, a důvodem
není degradace média, ale změna systémů (V/S, ProVideo Coalition).
IASA TC-03 6.3.10: formáty se mění rychleji, než médium stárne (P).
„Never the reason to move" = při 30leté životnosti a migraci po 5–10
letech médium o termínu nerozhoduje. ✅ (formulace, ne měření)
https://www.provideocoalition.com/tape-vs-drives-your-lto-questions-answered/
https://iasa-web.org/node/556

### S79 — otázka do komentářů
Bez faktického tvrzení. v0.6: *„If you had a tape drive at home, what
would you put on tape?"* (návrh uživatele).

## Doplněno ve v0.6 (ceny, mechaniky)

Ceny jsou ORIENTAČNÍ, USD, stav říjen 2026; mění se po týdnech. Hlavní
zdroj je tracker tapebackup.org (agregátor, ne prodejce), ověřeno proti
nabídce MagStor a britského prodejce.

### S48b — „around two hundred and sixty dollars"
LTO-10 30 TB: 259–300 USD (tapebackup.org 23. 10. 2026; MagStor IBM/HPE
~260 USD, Fujifilm 299,99 USD). 260/30 = 8,67 USD/TB → „under ten
dollars a terabyte". ✅ (orientačně)
https://tapebackup.org/lto-tape-price-trend/lto10-price
https://magstor.com/collections/lto-10

### S48c — „around forty dollars a terabyte"
Nové 24TB enterprise HDD v maloobchodu září 2026: Exos X24 ~45 USD/TB,
WD Gold ~43 USD/TB, Ultrastar ~50 USD/TB; nejlevnější nabídky 25–28 USD/TB.
Ceny disků od 9/2025 vzrostly o ~46–50 % (AI poptávka). 40/8,67 = 4,6 →
„more than four times". ✅ s výhradou: proti nejlevnějším nabídkám
(~25 USD/TB) by to bylo ~3×. Formulace „large new hard drive" + „around".
https://www.maxmybuild.com/storage/hard-drives/seagate-exos-x24/24tb
https://hddhunt.com/blog/hdd-price-per-tb-august-2026/

### S48d — „more than twenty thousand dollars"
Externí mechanika LTO-10 (zatím jen full-height): 23 422–24 950 USD
(tapebackup.org, říjen 2026; v březnu 2026 11–16 tis. USD). ✅
https://tapebackup.org/why-tape/lto-tape-drive

### S73d — „any LTO-10 drive, from any maker"
LTO je otevřený formát licencovaný konsorciem (HPE, IBM, Quantum);
kazety a mechaniky téže generace jsou zaměnitelné napříč výrobci
(lto.org, compliance program). ✅

### S73e — „eighty thousand cartridge loads"
Quantum LTO-9 HH datasheet: životnost 80 000 zavedení/vysunutí,
MSBF 100 000 cyklů, MTBF 250 000 h při 100% zátěži (statistika, ne
životnost — proto ve scénáři není). ✅ Výměna mechaniky v knihovně:
mechaniky jsou výměnné moduly (obecně známé). ✅
https://www.shi.com/product/44196370/Quantum-LTO-9-HH-Tape-drive

### S73f — „LTO-9 drives are still on sale"
Mechaniky LTO-9 v prodeji 10/2026, 8 009–13 329 USD (tapebackup.org);
LTO-9 čte LTO-8 (lto.org). Firmy na záchranu/migraci starých pásek:
Ontrack (Kroll), MagStor, DriveSavers, Tape Ark aj. — LTO-1 až 8. ✅
https://www.ontrack.com/en-gb/services/tape/migration
https://magstor.com/pages/data-migration
