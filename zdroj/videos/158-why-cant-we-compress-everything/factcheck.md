# 158 — fact check (scénář v0.3 → opravy tímto průchodem = v0.4, 2026-11-15)

Zdroje s odkazy jsou v `factcheck-zaklad.md`; tady je tvrzení po scénách.
**P** primární, **S** sekundární, **M** spočítáno / změřeno agentem.
Nadpis nese ID scény a doslovný fragment, `grep` ho musí najít v té scéně.

**Měření jsou verzovaná** v `mereni/` (`mer.sh`, `bloky.py`, `pi.py`,
výstup `vysledky.txt`); dřív ležela jen ve scratchpadu a `pi.py` se s ním
ztratil. `bash videos/158-*/mereni/mer.sh <pracovní adresář>` z kořene repa.

Tímto průchodem ověřeno nově ze zdrojů čtených celých: Shannon 1951
(BSTJ, pdftotext), Horn et al. NSDI ’17 (Lepton, arXiv 1704.06192),
Delétang et al. ICLR 2024 (arXiv 2309.10668v2, tab. 1), prize.hutter1.net.

## Opravy ve scénáři (v0.3 → v0.4)

| scéna | bylo | je | proč |
|---|---|---|---|
| S01 | *A hundred and fifty-seven videos* | *A hundred and fifty-eight* | na commitu `e6e3027d` je **158** souborů `script.md` (000–157, včetně 000) — M |
| S51 | *After each wrong guess, they were told the right letter, and carried on.* | *If a guess was wrong, they guessed again, until they got it right.* | to byl Shannonův **první** pokus; odhad 0,6–1,3 bitu při 100 písmenech (S52) je z **druhého**, kde se hádá do správné odpovědi — P |
| S65 | *a fifth smaller* | *over a fifth smaller* | 23 % (NSDI) / 22 % (blog); „pětina“ podstřelovala — P |
| S76 | *Four hundred and forty-five bytes. Two thousand times…* | *Three hundred and sixty-two bytes. Over two thousand times…* | program 445 B se ztratil, nový `mereni/pi.py` má 362 B (1 000 000 / 362 = 2 762×) — M |

Po opravách 86 scén, 2 128 slabik.

## Po scénách

### S01 — „A hundred and fifty-eight videos"
158 souborů `script.md` na `e6e3027d`, 1 490 115 B (M). „Almost one and
a half million“ ✅. Scénáře psal uživatel s agenty; „I've written“ je hlas
kanálu.

### S02 — „They came out at just over half a megabyte"
gzip 1.14, `-9 -n`: 508 111 B = 0,508 MB (SI; v MiB by to bylo 0,485,
proto se drží desítkových jednotek). Úbytek 65,9 % → „almost two thirds“ ✅ (M).

### S03 — „every script comes back"
`gzip -dc` kola 1 je s originálem shodné bajt po bajtu (`cmp`, M). ✅

### S05/S06 — „Ninety-eight bytes bigger."
Kola 2, 3, 4: +98, +98, +98 (M). Scénář ukazuje jen tato tři kola
a nikde neříká „every time“ — 7. kolo je +93 (viz S08). ✅

### S07 — „The second found nothing at all."
Kolo 2 obsahuje **jen stored bloky** (data uložená doslova), `bloky.py` (M). ✅

### S08 — „in sixteen blocks"
`bloky.py` na kole 2: **16 stored bloků**, dohromady přesně 508 111 B dat
(= celé kolo 1). Délky bloků 16 272 až 32 808 B (M). ✅
**Oprava číselného základu:** 7. kolo (+93) nemá „o blok méně“, nýbrž
začíná komprimovaným blokem (typ 2) — gzip tam drobek našel. Scénáře se
to netýká, ukazuje jen kola 2–4.

### S09 — „you get exactly ninety-eight"
Hlavička 10 B + 16 × 5 B (bajt s typem bloku a délka + její doplněk,
RFC 1951 §3.2.4) + patička 8 B (CRC-32 a délka, RFC 1952) = 98 (M). ✅
„Label“ je zjednodušení pro hlavičku bloku.

### S10 — „adds only what it needs to undo it"
DEFLATE má režim stored právě pro data, která nejdou zmenšit (RFC 1951,
P). Zjednodušení: patička (CRC) slouží ke **kontrole**, ne k rozbalení.
Ponecháno — rozdíl není pro diváka podstatný a věta netvrdí nic, co by
šlo vyvrátit číslem.

### S12 — „the same little scene markers"
Každá scéna začíná `<!-- Sxx -->` ✅.

### S13 — „In 1977, Jacob Ziv and Abraham Lempel"
IEEE Trans. IT-23(3), květen 1977, pořadí autorů Ziv, Lempel (P).
„Point back to where it was“ = LZ77 (kopie z nedávno viděného textu),
ne slovník LZ78 ✅.

### S14 — „A few bytes instead of twelve."
**Opraveno při kreslení diagramů (2026-11-15), v0.4 → v0.5.** Obraz ukazuje
SKUTEČNÝ odkaz z korpusu (`diagrams/gen/data.py`, `assert`): ` perhaps the`
ve scénáři 032 (S106b → S110), přesně **300** znaků (i bajtů) zpět, délka
**12**, maximální shoda a jediný výskyt v okně 32 KB, takže by ho deflate
opravdu použil. Délka 11 na vzdálenost 300 jednoznačně v korpusu není (dva
kandidáti mají bližší nebo delší shodu), proto scénář *eleven* → *twelve* (M).
DEFLATE, pevné Huffmanovy kódy: délka 12 = kód 266 (7 bitů) + 1 extra bit,
vzdálenost 300 = kód 16 (5 bitů) + 7 extra bitů → **20 bitů, 2,5 bajtu**
(RFC 1951 §3.2.5–6, M). Délka ≤ 258, okno 32 KB — obojí sedí. ✅

### S16 — „could sit the final exam"
Stix, Scientific American 1991: *„given the choice of a term paper or
a final exam“*; postgraduální kurz na MIT 1951 (S, rozhovor s Huffmanem). ✅

### S17 — „The paper, set by Robert Fano"
Stix: Fano zadal najít nejúspornější binární kód (S). ✅

### S18 — „For months, Huffman got nowhere."
Stix: měsíce bez výsledku, vzdal to a začal se učit na zkoušku (S). Koš
s poznámkami (Stixova parafráze) ve scénáři **není** ✅.

### S19 — „Take the two rarest symbols"
Huffman, Proc. IRE 40(9), 1952 — slučování dvou nejméně pravděpodobných (P). ✅

### S20 — „the most singular moment of my life."
Doslovný citát u Stixe (P zprostředkovaně). ✅

### S21 — „and so had Claude Shannon"
Huffman u Stixe: profesor ho neodradil tím, že by řekl, že *„other good
people had struggled with this problem“*; Stix uvádí Fana a Shannona (S). ✅

### S22 — „Huffman's code beat both their methods."
Huffman 1952: metody Shannona a Fana *„are not optimum“*; jeho kód je
optimální mezi prefixovými kódy symbol po symbolu (P). „Beat“ = nikdy
horší, někdy lepší ✅. Nezveličuje vztah k Fanovi (pokyn uživatele) ✅.

### S23 — „Phil Katz put both tricks together"
RFC 1951: *„Phil Katz designed the deflate format“*; DEFLATE = LZ77 + Huffman;
PKZIP 2 1991–93 (P/S). gzip = DEFLATE (RFC 1952) ✅.
Pozn.: spojení LZ + kódu proměnné délky Katz **nevymyslel první** (LHarc
1988, jeho vlastní „implode“ 1989 se Shannon–Fanem). Scéna to netvrdí —
říká „for ZIP files“. ✅

### S24/S25 — „To gzip, it looks like noise."
Kolo 2 = jen stored bloky (M). Věta je formulovaná z pohledu gzipu
(recenze v0.2). **Pro storyboard:** obraz **nesmí tvrdit**, že výstup gzipu
je náhodný — žádný „šum“ jako vlastnost dat, nanejvýš „gzip nevidí vzor“.

### S28–S30 — „There are eight of them."
3 bity: 2³ = 8; kratší: 4 + 2 + 1 (prázdný) = 7 (M). ✅

### S32 — „one fewer shorter file"
Kratších než n bitů je 2ⁿ − 1 (M). ✅

### S33 — „any compressor that takes every file"
Platí pro bezeztrátový kompresor definovaný na všech souborech; důkaz
v `notes.md` (zpětná vazba k v0.1) a ve `factcheck-zaklad.md`, recenze
v0.2 ho uznala (M). ✅

### S34 — „how gzip pays that price"
Režie stored bloků je přesně ta cena: soubor, který gzip nezmenší,
prodlouží o 18 B + 5 B na blok (M). ✅

### S35 — „in two hundred and fifty by a single byte"
Souborů kratších než n bajtů je (256ⁿ − 1)/255, tedy < 1/255 počtu
n-bajtových (M). Platí pro „aspoň o bajt“ i „přesně o bajt“ (1/256). ✅
Mahoney: *„less than 0.4 % of strings can be compressed by one byte“* (S).

### S36 — „because the files we make aren't random"
Obecné, ✅.

### S38 — „In 1992, WEB Technologies"
comp.compression FAQ (Gailly), položka 9, cituje Byte Week 20. 4. 1992:
*„virtually any amount of data can be squeezed to under 1024 bytes“*,
opakovaně i vlastní výstup (S). „Almost any data“ je volnější než
„any amount of data“, smysl drží. ✅

### S39 — „not subject to the laws"
Citát viceprezidenta podle FAQ (Byte 6/1992); produkt nikdy nevyšel (S). ✅

### S41 — „A JPEG doesn't come back identical."
Ztrátová komprese, obecné ✅. **Pro storyboard:** S42 (*„Zoom in, and you
can see where it went“*) potřebuje **skutečné** artefakty — vyrobit vlastní
JPEG v nízké kvalitě (`magick -quality 10`) a ukázat výřez, ne kreslit
„kostičky“ od ruky.

### S45 — „in the same paper behind our video"
BSTJ 27, 1948 — týž článek jako u 157 (157 S-blok o Shannonovi, *„The
promise of 1948“*) ✅. **Platí jen, když 157 vyjde dřív než 158** — ověřit
při nahrání.

### S46 — „how much of it you can take away"
Tentýž článek: kódování kanálu (157) i zdroje (Theorem 9) (P). ✅

### S47/S48 — „No lossless code can beat that number"
Theorem 9 (P). **Výhrada recenze:** entropie je vlastnost **modelu
zdroje** (rozdělení pravděpodobností), ne jednoho souboru. Scénář ji
definuje jako „how hard it is to guess what comes next“ a mez jako
„on average“, tedy nad zdrojem, ne nad konkrétním souborem ✅.
„As close as you like“ — při kódování dlouhých bloků / aritmetickém
kódování ✅.

### S49 — „In 1951, Shannon measured it"
*Prediction and Entropy of Printed English*, BSTJ 30, leden 1951 (P).
„Measured“ = experimentální odhad, viz S52.

### S50 — „letter by letter"
Neznámý úryvek, hádá se písmeno po písmenu (P). ✅

### S51 — „they guessed again"
**Opraveno.** Shannon 1951, s. 56: *„If he is wrong, he is told so and
asked to guess again. This is continued until he finds the correct
letter.“* Tohle je druhý pokus a z něj je tabulka do 100 písmen (P).

### S52 — „English came out at about one bit"
Abstrakt: *„the long range statistical effects (up to 100 letters) reduce
the entropy to something of the order of one bit per letter“*; tabulka
dává meze 0,6–1,3 (P). **Výhrada recenze:** je to odhad z lidského
předvídání, ne dokázaná mez angličtiny — scénář říká „came out at
about“ ✅.

### S53 — „A computer stores each letter"
ASCII / UTF-8 pro anglická písmena 8 bitů ✅.

### S54 — „under three bits a character"
Po 1. kole 2,728 bitu na znak (1 489 851 znaků; bajtů je o 264 víc kvůli
několika vícebajtovým znakům UTF-8) (M). ✅

### S56 — „since 2020, the task is one file"
Od 2020 `enwik9`, prvních 10⁹ bajtů výpisu anglické Wikipedie (XML se
značkami) (P). ✅

### S57 — „gzip shrinks it to a third."
LTCB: gzip -9 32,3 %, xz 19,7 % (P). ✅

### S58 — „The record, set in July 2026"
Vladimir Ivanov, 24. 7. 2026, 100 424 672 B (P) → „just over a hundred
million… A tenth“ ✅.

### S59 — „the decompressor counts too"
Pravidla: kompresor + samorozbalovací archiv (P). ✅

### S60 — „five hundred thousand euros"
Fond 500 000 €, 1 % zlepšení = 5 000 € (P). ✅

### S61 — „Marcus Hutter, who funds it"
prize.hutter1.net: *„Marcus Hutter: arbiter, current sponsor, and manager
of prize fund“* (P). Citát doslovně z hlavní stránky (P). ✅

### S62 — „They predict."
Špička LTCB = kontextové míchání (cmix) s transformerem (P).
Zjednodušení: cmix má mezi modely i „match model“ (hledá opakování),
ale i ten jen dodává **předpověď** do míchání — věta je pravdivá v tom,
co dělá výstup. ✅

### S63 — „A good guess costs a fraction of a bit."
Aritmetické kódování: symbol s pravděpodobností p stojí −log₂ p bitů,
při p > 0,5 méně než bit (M). ✅

### S64 — „The best players now use neural networks"
fx2-cmix-T: transformer 6 mil. parametrů; nncp (P). ✅

### S65 — „In 2016, Dropbox began re-packing"
NSDI ’17: *„We deployed Lepton in April 2016“*; JPEG na 77 % průměrně (P).
„Better predictor“: nahrazuje Huffmanovu vrstvu aritmetickým kódováním
s lepší předpovědí koeficientů (P). „Over a fifth“ **opraveno** ✅.

### S66 — „over forty-six petabytes"
NSDI ’17: *„As of Feb. 16, 2017, Lepton has encoded 203 PiB of images,
reducing the size of those images by 46 PiB“* (P). 46 PiB = 51,8 PB,
„over forty-six petabytes“ platí v obou jednotkách ✅. Přidáno 2026-11-16 na přání
uživatele „over forty-six thousand terabytes“: 46 PiB = 47 104 TiB = 51 800 TB,
takže platí taky v obou jednotkách ✅. Bit po bitu:
každý soubor se před uložením rozbalí a porovná; co neprojde (~6 %),
zůstane v původní podobě (P) ✅.

### S67 — „In 2023, researchers at DeepMind"
arXiv září 2023, ICLR 2024; Chinchilla 70B (P). ✅

### S68 — „forty-eight percent of the original size"
Tab. 1: ImageNet, záplaty 32 × 64 px převedené na odstíny šedi (P) →
„small greyscale patches“ ✅. Chinchilla 70B 48,0 %, PNG **58,5 %**
(PNG na celém souboru; na stejně dlouhých kusech jako model je 61,7 %).
Scénář bere pro PNG tu **výhodnější** hodnotu ✅.

### S69 — „twenty-one percent against thirty"
LibriSpeech (předčítané audioknihy, 16 kHz) 21,0 %, FLAC 30,3 % (nejlepší
z obou variant, 30,9 na celém souboru) (P). ✅

### S70 — „a hundred and forty times"
Tab. 1, upravená míra se započtenou velikostí modelu: 14 008–14 101 %,
tedy ~140× (P). ✅

### S73 — „four hundred and twenty-six thousand bytes"
Milion číslic π (bez úvodní trojky) — zstd --ultra -22: **426 124 B**,
gzip 470 431, bzip2 431 446, xz 436 088 (M). ✅
Kontrola číslic: prvních 20 000 se shoduje s Machinovým vzorcem,
„Feynmanův bod“ 999999 začíná na 762. místě (známá hodnota) (M).

### S74 — „within a tenth of a percent"
Náhodné číslice ze `secrets` (CSPRNG systému, ne Mersenne Twister —
u `random` by existoval krátký program se semínkem a podrazilo by to
S81): gzip 470 461, bzip2 431 187, xz 436 248, zstd 425 902. Největší
rozdíl proti π 259 B = **0,06 %** (M). ✅
Teoretické minimum pro náhodné číslice 415 241 B — pod něj se nedostal
nikdo, ani u π.

### S75 — „It follows a mathematical rule."
Formulace recenze v0.2: normalita π není dokázaná, deterministická ≠
statisticky nenáhodná ✅. Program = `mereni/pi.py` (Chudnovského řada,
binární dělení, celá čísla). **Pro storyboard:** ukázat **přesně tento
soubor**, jinak nesedí počet bajtů.

### S76 — „Three hundred and sixty-two bytes."
`wc -c mereni/pi.py` = 362, výstup 1 000 000 číslic za 7,7 s (M).
1 000 000 / 362 = 2 762 → „over two thousand times“ ✅.
Výhrada (viz S78): k programu patří interpret Pythonu; Kolmogorovova
složitost se definuje vůči pevnému jazyku a liší se o konstantu.

### S77 — „They could only see the digits."
Obecné kompresory modelují četnosti a opakování; π je jimi
nerozeznatelná od náhody (S73/S74, M). ✅

### S78 — „One way to measure the information"
K(x) = délka nejkratšího programu, který vypíše x (S, Scholarpedia).
„One way“ — závislost na jazyce (recenze v0.1) ✅.

### S79 — „after one of the men who described it"
Solomonoff 1964, Kolmogorov 1965, Chaitin 1966/69 (P/S). ✅

### S80 — „there aren't enough short programs"
Programů kratších než n − c bitů je < 2ⁿ⁻ᶜ, tedy nejvýš podíl 2⁻ᶜ řetězců
délky n (M). ✅

### S81 — „very likely has nothing shorter"
Pro skutečně náhodný řetězec platí K(x) ≥ n − c s pravděpodobností
≥ 1 − 2⁻ᶜ (M). „Nothing shorter“ = žádný podstatně kratší popis ✅.

### S82 — „no algorithm can do that"
K je nevyčíslitelná (Scholarpedia; Chaitin 1974) (S/P). ✅

### S83 — „Every program gives you an upper limit."
Shora aproximovatelná, ne vyčíslitelná; dolní mez jde dokázat jen
výjimečně (Chaitin 1974, recenze v0.2) ✅.

### S84–S86
Závěr a otázka do komentářů — názor, ne tvrzení. „Predicting text well
starts to look a lot like understanding it“ odpovídá Hutterově tezi (S61)
a je formulované jako dojem ✅.

## Pro storyboard (z fact checku)

- S08–S09: čísla bloků ber z `mereni/vysledky.txt`, ne z hlavy (16 bloků,
  10 + 80 + 8).
- S24/S25: výstup gzipu nekreslit jako „náhodný šum“.
- S42: skutečný JPEG artefakt, vlastní soubor.
- S68–S70: uvést dataset (ImageNet záplaty, LibriSpeech) a že 140× je se
  započtenou velikostí modelu.
- S75/S76: kód z `mereni/pi.py`, 362 B.
- S45: callback na 157 jen pokud 157 vyjde dřív.

## Data v diagramech (2026-11-15)

Co obraz ukazuje navíc proti hlasu, a odkud to je. Všechno spočítá
`diagrams/gen/data.py` z korpusu e6e3027d do verzovaného `data.json`,
nebo `art/vyrob.sh` z fotky.

| scéna | v obraze | původ |
|---|---|---|
| S08 | 16 bloků v šířkách podle skutečných délek (32 797 … 16 272 B) | `data.json` z `gzip -9 -n` kola 2 (M) |
| S15 | E 000, T 001, S 1010, A 0100 · X, J, Q, Z 8–10 bitů | četnosti A–Z ve 158 scénářích, Huffman, kanonické kódy (M); S je třetí díky značkám `<!-- Sxx -->` |
| S19/S22 | abeceda A20 B7 C7 D7 E4 F3: Shannon–Fano 2,44, Huffman 2,31 bitu | Fanova metoda vs. Huffman (M). Vybráno hrubou silou jako případ s největším rozdílem — na malé abecedě je Fano blízko optima, obraz to netvrdí jinak |
| S25 | 48 hex bajtů | skutečné bajty kola 1 od offsetu 200 000 (M) |
| S40 | text 34 %, fotka 1,8 %, hudba 9,1 % | text = náš gzip; fotka = JPEG q75 / nekomprimované RGB pixely naší fotky (42 482 / 2 418 900); hudba = 128 / 1 411,2 kbit/s (CD: 44 100 × 16 × 2) (M) |
| S41/S42 | ledňáček, JPEG q20, výřez 5× | vlastní soubor z fotky CC BY 2.0 (`art/PUVOD.md`) — artefakty skutečné |
| S47 | po „th“: E 69 %, A 17 %, I 8 %, O 3 %, R 3 % | korpus, „th“ na začátku slova (M) |
| S63 | po „fro“: M 91 % (0,14 bitu), N 7 % (3,8), Z 2 % (5,7) | korpus, začátek slova; cena −log₂ p (M) |
| S76 | 2 762× | 1 000 000 / 362 (M) |
