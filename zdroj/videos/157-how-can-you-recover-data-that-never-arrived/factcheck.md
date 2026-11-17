# 157 — fact check (scénář v0.3 → opravy tímto průchodem = v0.4, 2026-11-14)

Zdroje s odkazy jsou v `factcheck-zaklad.md`; tady je tvrzení po
scénách. **P** primární, **S** sekundární, **M** spočítáno agentem.
Nadpis nese ID scény a doslovný fragment, `grep` ho musí najít v té
scéně. Hlavní sekundární zdroj je Costello & Forney 2007 (C&F),
Voyager je Ludwig & Taylor, DESCANSO 2002 (L&T).

### S01–S06 — „It holds one short line of text"
Tvrzení o **našem** pokusu (načte se celý, po utržení kusu datové
oblasti znovu se stejným textem). **⏳ Ověří až natočení** — uživatel
telefonem; když se poškozený kód nenačte, mění se scéna, ne svět.
Kód: `qrencode -l H`, poziční značky nepoškozovat.
**2026-11-14:** uživatel naskenoval telefonem kresbu z draftu — **celý
i roztržený kód (S04/S05, ~11 % modulů) se načte**. Pokud se natáčet
nebude, tvrzení scén platí pro kresbu, která je ve videu.

### S07/S08 — „so there are eight ways to fill the gaps"
Tři chybějící bity na známých místech → 2³ = 8 doplnění (M). ✅

### S09 — „The answer was sent"
Princip dopředné opravy chyb (FEC): redundance je přidaná předem. ✅

### S11/S12 — „Two votes against one"
Opakovací kód (3,1), dekódování většinou (MacKay kap. 1, P). ✅

### S13 — „less than three times in a hundred"
Nezávislé chyby s p = 0,1: 3p² − 2p³ = **0,028** (M). Předpoklad
nezávislosti je ve scéně („at random and independently"). ✅

### S14 — „and the message slows to a crawl"
Opakováním jde chyba k nule jen při rychlosti 1/N → 0 (MacKay kap. 1, P). ✅

### S16/S17 — „He mostly got time on a relay computer"
Hamming, *The Art of Doing Science and Engineering* (1997), kap. 12:
reléový počítač Bell Labs **Model V** v New Yorku, strojový čas jen
o víkendech (pá 17 h – po 8 h), bez obsluhy; 1947–48 (P). ✅

### S18 — „Two weekends in a row"
Tamtéž: při zjištěné chybě zkusil krok až třikrát, pak úlohu zahodil
a vzal další; stalo se mu to dva víkendy po sobě (P). ✅

### S20 — „why can it not locate where it is?"
Hamming 1997, vlastní slova: *„If the machine can locate there is an
error, why can it not locate where it is, and then fix it by simply
changing the bit to the opposite state?"* — ve scénáři zkráceno na
první půlku věty, nic přidáno. *„The actual language used was perhaps
a bit stronger"* → „probably a bit stronger" (opraveno z „was a bit
stronger", které vypustilo jeho „perhaps"). Verze „Damn it…" (Thompson
1983, rozhovor) nepoužita. ✅

### S22–S24 — „Seven bits in all"
Hamming, BSTJ duben 1950; kód (7,4), tři paritní bity, sudá parita,
každá pozice v jiné kombinaci skupin (P). ✅

### S25–S27 — „In binary, that's six"
Parita na pozicích 1, 2, 4: kontrola 1 hlídá 1, 3, 5, 7 → pozice 6 projde;
kontrola 2 (2, 3, 6, 7) a kontrola 4 (4, 5, 6, 7) neprojdou. Od poslední
k první: 1, 1, 0 = 6 (M). ✅

### S28–S30 — „Nobody had to send anything twice"
Oprava bez zpětného kanálu = FEC. ✅

### S32 — „like the one in our video"
Video 141: Btrfs checksum chybu pozná, opravuje z druhé kopie. Checksum
(CRC, hash) sám pozici chyby neurčí. ✅

### S33/S34 — „That's called an erasure"
Výmaz = chybějící symbol na známém místě; RS opraví 2× víc výmazů než
chyb (2e + f ≤ n − k), tedy „easier" platí (M, C&F). ✅

### S35/S36 — „It has to be two"
4 + 7 + 2 + 9 = 22; 22 − 4 − 7 − 9 = 2 (M). ✅

### S37 — „spread across the drives"
RAID 5: paritní blok (XOR) v každém pruhu, rozprostřený po discích,
přežije výpadek jednoho disku (Patterson, Gibson, Katz 1987, P).
„A similar kind of check" — XOR, ne součet; formulace to nezakrývá. ✅

### S39 — „Two years before Hamming's paper"
Shannon BSTJ červenec a říjen 1948, Hamming BSTJ duben 1950 → 21 měsíců
(P). Oba Bell Labs. Hammingův kód Shannon v článku uvedl („a method due
to R. Hamming"), takže „kolega" sedí. ✅

### S40 — „has a limit"
Kapacita kanálu (Shannon 1948, P). Bez vzorce — Shannon–Hartley platí
jen pro pásmový kanál s bílým šumem. ✅

### S41/S42 — „without slowing down"
Theorem 11: pod kapacitou libovolně malá chybovost při pevné rychlosti;
nad kapacitou ne (P; MacKay kap. 1). ✅

### S43 — „He didn't show how to build one"
Shannon: *„not by exhibiting a coding method… but by showing that such
a code must exist"*, postup *„generally impractical"* (P). „That anybody
could use" — v článku je jediný explicitní kód (Hammingův) pro hračkový
kanál. ✅

### S44 — „more of those"
Náhodný kód je s vysokou pravděpodobností dobrý (důkaz náhodným
kódováním, P). Blok 1 000 bitů při rychlosti 1/2 = 2⁵⁰⁰ ≈ 3,3 × 10¹⁵⁰
zpráv; atomů v pozorovatelném vesmíru ~10⁸⁰ (běžný odhad, S). Platí
pro jakoukoli rychlost od ~0,27 výš (2²⁶⁶ ≈ 10⁸⁰). „Compare with every
possible message" = dekódování maximální věrohodností hrubou silou. ✅

### S46 — „forty-five years"
1948 → turbo kódy 1993 (P). ✅

### S47 — „It fixes one wrong bit in seven"
Hamming (7,4), vzdálenost 3 (M). ✅

### S48 — „takes out hundreds of bits in a row"
CD: škrábanec = výpadek tisíců bitů (S53); obecně shluky chyb. ✅

### S49 — „published a paper five pages long"
Reed & Solomon, *Polynomial Codes over Certain Finite Fields*, J. SIAM
8(2), červen 1960, s. 300–304, MIT Lincoln Laboratory (P). ✅

### S50 — „that's still just one bad byte"
RS pracuje se symboly, typicky bajty (GF(256)) (C&F). ✅

### S51/S52 — „or rebuild thirty-two"
RS(255,223): n − k = 32 → 16 chyb nebo 32 výmazů (M; C&F). ✅

### S53 — „two and a half millimetres of track"
CIRC, dva RS kódy (32,28) a (28,24) (Immink, P); plně opraví ~4 000 bitů
≈ 2,5 mm (Immink píše 1,5 mm, přepočet 15 rámců při 1,2 m/s dává
2,5 mm; Wikipedia 2,5 mm). ✅

### S54 — „thirty percent of its bytes"
Denso Wave: úroveň H **~30 % kódových slov** (P). Kódové slovo QR = 8 bitů,
tedy bajt (ISO/IEC 18004, S přes popisy standardu). 30 % je horní mez
(skutečná závisí na verzi a rozložení poškození), proto „up to about". ✅

### S56 — „Voyager 2 left Earth in 1977"
L&T: *„Voyager carried an experimental Reed-Solomon data encoder,
expressly for… Uranus and Neptune"* (P); na obou sondách od startu
(McEliece & Swanson 1993/94, cit. destevez.net, S cit. P). ✅

### S57 — „by Marcel Golay"
L&T §6.2.2: *„The Golay encoding algorithm used at Jupiter and Saturn
required the transmission of one overhead bit for every information bit
transmitted (100% overhead)"* (P). Golay 1949 < RS 1960 → „older".
Že chránil **snímky**, se netvrdí (zdroje se rozcházejí). ✅

### S58 — „engineers switched Reed-Solomon on"
L&T: později *„upgraded in-flight to concatenated Reed-Solomon and
convolutional coding"* (P). Konvoluční k = 7, r = 1/2 je vnitřní kód,
RS vnější — „on top of" sedí. ✅

### S59 — „about one in a million"
L&T §6.2.2: RS *„reduced the bit-error rate in the output information
from 5 × 10⁻³ to 10⁻⁶"* (P) — tedy chybovost bez RS (za konvolučním
kódem) proti chybovosti s RS. Obě čísla jsou táž veličina. ✅

### S60/S61 — „the bytes of four blocks"
Hloubka prokládání 4 (McEliece & Swanson, S cit. P; zpráva JPL
o Galileu, P ze snippetu). ✅

### S62 — „is in our video about Voyager"
Video 110, S36–S40. ✅

### S63 — „was still short of Shannon's limit"
Zřetězené RS + konvoluční kódy zůstávají znatelně od limitu (C&F, S). ✅

### S65 — „in his doctoral thesis at MIT"
Gallager, Sc.D. MIT **1960** (dspace.mit.edu, P); článek IRE 1962, kniha
1963. Řídká matice: každá kontrola hlídá jen pár bitů (P). ✅

### S66 — „mostly forgotten for thirty years"
*„Much too complex for the technology"* (C&F); znovuobjevení 1995–96.
„Mostly" doplněno, protože Tanner 1981 se k nim vrátil (také zapadl). ✅

### S68 — „at a conference in Geneva"
Berrou, Glavieux, Thitimajshima, ICC '93, Ženeva, květen 1993 (P).
Berrou a Glavieux Francouzi, třetí autor thajský → „a team led by two
French engineers". ✅

### S69 — „somewhere in their calculations"
C&F: *„It can't be true; they must have made a 3 dB error"* bylo
„widespread". 3 dB = dvojnásobek výkonu → „factor of two" (M).
Opraveno z „in the maths" — podezření mířilo na přepočet výkonu
v měření, ne na matematiku kódu. ✅ (S)

### S70 — „other labs had confirmed it"
C&F: laboratoře výsledky během roku potvrdily (S). ✅

### S71/S72 — „David MacKay and Radford Neal"
MacKay & Neal 1995 (IMA) a 1996 (*Electronics Letters*), iterační
dekódování po vzoru turbo kódů (P/S). ✅

### S73/S74 — „four hundredths of a decibel"
Chung, Forney, Richardson, Urbanke, IEEE Comm. Letters, únor 2001:
simulovaný kód **0,04 dB** od limitu při BER 10⁻⁶, blok 10⁷ (P abstrakt,
C&F). 10^0,004 = 1,0093 → **0,93 %** výkonu (M). Teoretický práh
0,0045 dB nepoužit. „The promise had been kept" — hodnocení, ne fakt. ✅

### S75 — „in satellite television"
5G NR: LDPC na datové kanály (3GPP RAN1, 10/2016, Rel-15) (S).
Wi-Fi: LDPC volitelně v 802.11n/ac, povinné v 802.11ax (Wikipedia, S).
Satelitní TV: DVB-S2 (ETSI EN 302 307) LDPC + BCH (S). ✅

### S77–S80 — „only sixteen follow those rules"
Rozšířený Hamming (8,4): 16 slov z 256, vzdálenost 4; `10110100` platné;
při výmazech na pozicích 3, 6, 8 (`10?10?0?`) je z 8 kandidátů platný
jediný; jakékoli 3 výmazy → jednoznačně (56/56) (M). „Hamming's three
checks, and one more check over all eight" = (8,4). ✅

## Opraveno ve scénáři tímto průchodem

| scéna | bylo | je |
|---|---|---|
| S20 | was a bit stronger | was **probably** a bit stronger |
| S66 | put away for thirty years | put away, and **mostly forgotten** for thirty years |
| S69 | somewhere in the maths | somewhere in **their calculations** |

Zbývá: **S01–S06 po natočení pokusu.**

## Zpětná vazba ChatGPT k v0.3 (`zpetna vazba 0.3.txt`) → v0.6, 2026-11-15

Soubor dorazil až po draftu 2; ověřeno proti primárním zdrojům staženým
tentokrát: Hammingova přednáška NPS 21. 4. 1995 (přepis, P), Ludwig &
Taylor DESCANSO 2002 (P), Costello & Forney 2007 (arXiv, S od přímého
účastníka), Rice 2024, *A History of Channel Coding…*, Sensors/PMC11353454
(S, cituje JPL).

| scéna | nález | závěr |
|---|---|---|
| S17 | přednáška 1995: „low man on the totem pole… during the week I didn't get much“, úlohy na páskách přes víkend | **přijato zčásti**: „He **mostly** got time… at weekends“. Kniha 1997 (P) říká víkendy bez obsluhy, takže „nobody was there to watch it“ zůstává |
| S20 | v přednášce zní citát „If a machine can find out if there is an error, why can't I find out where it is?“ | **nepřijato** — scénář cituje knižní znění (1997, P). Jsou to dvě verze téhož výroku od téhož autora; obě dodávají, že skutečná slova byla silnější |
| S32 | Btrfs ví, KTERÝ blok je vadný | **přijato**: „can tell you a block is damaged, but not what the original data were“ (formulace ChatGPT). Dřívější „but not where“ bylo nepřesné |
| S44 | „decoding it means comparing…“ je kategorické | **přijato**: „the obvious way to decode it means comparing…“ |
| S54 | „bytes“ → „eight-bit codewords“ | **nepřijato** — „its bytes“ = bajty celého kódu včetně opravných, kódové slovo QR má 8 bitů (Denso Wave: ~30 % codewords). Slovo *codeword* divák nezná, bajty zavedla S50 |
| S56 | „Both Voyagers… carrying RS“ | **přijato**: „Voyager 2 left Earth in 1977 already carrying a Reed-Solomon encoder“ (L&T: *Voyager carried an experimental RS data encoder*; RS u Uranu a Neptunu jen V2, Rice) |
| S57 | Golay u J/S chránil jen neobrazová data | **přijato** (Rice podle JPL: snímky jen konvoluční kód s chybovostí 5 × 10⁻³, neobrazová data Golay + konvoluční): „it guarded everything but the pictures with an older code“ |
| S58–S59 | upřesnit vrstvy a k čemu se vztahuje 5 × 10⁻³ → 10⁻⁶ | **přijato jinak**: druhý (konvoluční) kód je teď pojmenovaný jako ten, kterým prochází každý bit, a S59 srovnává „with that second code alone“ / „with Reed-Solomon on top“ — to je přesně srovnání L&T. **Tvrzení ChatGPT, že čísla platí pro neobrazová data, nepřevzato**: 5 × 10⁻³ je podle Rice chybovost obrazového spoje, neobrazová data měla požadavek 5 × 10⁻⁵ |
| S69 | faktor dva nedoložený | **nepřijato** — C&F §VI doslova: *„Comments to the effect of 'It can't be true; they must have made a 3 dB error' were widespread.“* 3 dB = 2× výkonu (M). Jen „experts“ → „**many** experts“, ať to sedí s *widespread* |
| S73 | 0,04 dB není od MacKaye a Neala | **přijato**: „a refined version of Gallager's codes came within…“ — C&F: Chung a spol. 2001, neregulární LDPC, *„no extension of Gallager's LDPC codes beyond irregularity“* |
| S75 | ne všechna data v 5G/Wi-Fi | **přijato**: „carry **much of** the data in 5G phones“ |
| S53 | CD přehraje jen určitý typ shluku, jinak interpolace | beze změny — „can fully repair a gap of about four thousand bits“ to už vymezuje |

### Zpětná vazba k v0.6 (`zpetna vazba 0.6.txt`)

ChatGPT v0.6 schválil a námitky k S20, S54 a S69 stáhl. Dva drobné návrhy
**nepřevzaty**:
- **S17 „when the lab was quiet“** místo „when nobody was there to watch it“:
  kniha (P) říká, že stroj o víkendu běžel bez obsluhy, a právě to nese S18
  (úlohu zahodí a nikdo nezasáhne). Lab was quiet by tu vazbu ztratil.
- **S59 „On the image link“**: podle Rice byl CELÝ spoj (od vstupu
  konvolučního kodéru po výstup dekodéru) navržen na 5 × 10⁻³, protože 95 %
  dat tvořily snímky; tuhle chybovost má každý bit. „Image link“ by bylo
  užší, než co zdroj říká — „with that second code alone“ je přesné.
