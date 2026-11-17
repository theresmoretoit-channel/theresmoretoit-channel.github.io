# Fact check — 124 Why Does a New Disk Need Formatting?

Ověřováno 2026-10-25 proti `script 0.3.md`, opravy jsou ve `script 0.4.md`
(čísla scén se nemění). Hlavní doklad je **vlastní měření**
`mereni-mkfs.txt`: obraz o přesně 10¹² B, `mkfs.ext4` s výchozím nastavením
(mke2fs 1.47.3, `/etc/mke2fs.conf` openSUSE), `dumpe2fs`, `debugfs`;
Btrfs `mkfs.btrfs` (btrfs-progs 7.1). Reprodukce: příkazy jsou v tom souboru.

Značky: ✅ platí · ✏️ opraveno · ⚠️ platí s výhradou (do komentářů).

## Háček (S01–S06)

**S01 „your computer asks you to format it"** ✏️
Nový interní disk se ve Windows ukáže v Disk Management jako
neinicializovaný, dotaz „You need to format the disk" přijde jen u oddílu
bez filesystemu; Linux se neptá vůbec. A externí disky se často prodávají
předformátované (exFAT/NTFS). → **„it first has to be formatted."**

**S02 ext4 „the standard filesystem on many Linux computers"** ✅
Výchozí v instalátoru Debianu a Ubuntu. Ne všude: Fedora má Btrfs od
verze 33 (2020), openSUSE Btrfs na systémovém oddílu. Proto „many", ne „most".

**S02 „with the default settings… about seventeen gigabytes are gone"** ✅ ⚠️
Naměřeno: 244 140 625 bloků, volných po mkfs 240 026 450 → 4 114 175 bloků
× 4 096 B = **16,85 GB**. Platí pro výchozí `mke2fs.conf` a velikost
10¹² B; jiná distribuce s jiným `mke2fs.conf` dá jiné číslo.
Co uvidí divák, který si to zkontroluje (**spočteno, neměřeno**, mount
potřebuje root): `df` u ext4 hlásí velikost bez režie, tedy
931,3 − 15,7 = **~916 GiB**, takže „zmizení" je vidět. Volné místo
(`Avail`) je ale ještě o **5 % rezervy pro roota** nižší (12 207 031 bloků
= 50 GB, ~869 GiB). **Rezerva ve scénáři není schválně** (odbočka od
otázky „co tam je"); je to nejpravděpodobnější námitka v komentářích.

**S04 „It can read and write billions of bits"** ✏️
1 TB = 8 × 10¹² bitů, tedy **biliony**. „Billions" je pravda, ale o tři
řády slabší. → **„trillions of bits"**.

## Sešit (S07–S17)

Analogie, nic k ověření. S17 ji výslovně ukončuje. Mapování na skutečnost
(stránky = bloky, obsah = složka + inode, seznam prázdných stránek = bitmapa)
drží; nepřesnost, že obsah v sešitu nese jméno i umístění najednou, kdežto
ext4 je rozdělí do složky a inodu, řeší S34.

## Sektory a bloky (S18–S22)

**S18–S19 disk nabízí jen číslované sektory, HDD na plotnách, SSD ve flash** ✅
Rozhraní blokového zařízení (LBA). U SSD převádí logické sektory na stránky
flash řadič (FTL), počítač o tom neví, což věta „the computer only ever asks
for a sector by its number" říká správně.

**S20 sektor 512 B, nebo 4 096 B u novějších disků** ✅
Advanced Format (4K fyzické sektory, u HDD od ~2010, často s emulací 512 B).
„Usually" kryje, že NVMe SSD často hlásí logických 512 B.

**S21 blok ext4 = 4 KB = osm „starých" sektorů** ✅
`/etc/mke2fs.conf`: `blocksize = 4096`; `dumpe2fs`: Block size 4096.
4 096 / 512 = 8.

## Odpověď na háček (S23–S29)

**S24 inode 256 B, jeden na každý soubor a složku, které se tam vejdou naráz** ✅ ✏️
`mke2fs.conf`: `inode_size = 256`, `dumpe2fs`: Inode size 256. Inode
spotřebuje každý objekt (soubor, složka, symlink), proto „file and folder".
**„Linux calls it an inode"** ✏️: inode je pojem z Unixu (70. léta), ne
z Linuxu. → **„It's called an inode."**

**S25 inode nese velikost, čas změny, oprávnění, bloky** ✅
`debugfs stat hello.txt`: Size, ctime/mtime, Mode/User/Group, EXTENTS.
Jméno v inodu není (viz S34).

**S26 ~61 milionů inodů, téměř 16 GB** ✅
Naměřeno 61 038 592 × 256 B = **15,63 GB**.

**S27 jeden inode na 16 KB místa; většina záznamů zůstane nevyužita** ✅
`mke2fs.conf`: `inode_ratio = 16384`; 10¹² / 16 384 = 61 035 156, mkfs
zaokrouhlí na celé skupiny (8 192 inodů) → 61 038 592. **Pozor:** od 4 TiB
použije mke2fs typ `big` (32 768), od 16 TiB `huge` (65 536), takže u větších
disků je poměr jiný — scéna mluví o 1TB disku, sedí.
„Most will never be used": render node .207 (dva ext4 svazky) má využito
**2 % inodů** při 50 % zaplnění (`/`, 219 GB) a **4 %** při 24 % (`/data`,
1,8 TB). Dva svazky nejsou statistika, ale směr je jednoznačný; a „typical"
je na místě, protože výjimky (poštovní servery, cache) existují.

**S28 asi 1 GB žurnál, zbytek ostatní evidence včetně bitmapy bloků** ✅
Naměřeno: „Vytváří se žurnál (262 144 bloků)" = 1 GiB = **1,07 GB**.
Mimo tabulky inodů zbývá 16,85 − 15,63 = 1,22 GB, žurnál z toho tvoří 88 %.
Bitmapa bloků = 1 bit na blok (244 M bitů ≈ 30,5 MB), dále bitmapy inodů,
popisovače skupin, rezerva GDT pro zvětšení (`resize_inode`), superbloky.

**S29 vyčerpané inody → „disk je plný" i s volným místem** ✅
Zápis selže s `ENOSPC` („No space left on device"), `df -i` ukáže 100 %.
Známá provozní past ext2/3/4; počet inodů ext4 po vytvoření nezvětšíš
(jen spolu se zvětšením filesystemu).

## hello.txt (S30–S45)

**S30–S33 vytvoření: inode, blok, záznam ve složce** ✅
Naměřeno přes `debugfs write`: přidělen **inode 13** (S31 ho uvádí jako
příklad, „Let's say"), Size 5, blok 9884, ve `/` řádek `13 … hello.txt`.
Pořadí kroků ve scénáři je výkladové, jádro je dělá v jedné transakci
žurnálu — na tvrzení to nic nemění.

**S34 jméno je ve složce, ne v souboru ani v inodu** ✅
Položka adresáře ext4 = číslo inodu + délka + typ + jméno
(kernel.org, *ext4 Data Structures and Algorithms*, „Directory Entries").
Proto jde mít víc jmen na jeden inode (hard link).

**S35 složka je soubor, jehož obsahem je ten seznam** ✅
Adresář je inode typu adresář s datovými bloky plnými položek
(`ls -l /` v debugfs: `.` má sám inode 2 a velikost 4 096).

**S36 přesun v rámci jednoho filesystemu je okamžitý** ✅
`rename(2)` jen přepíše položky adresářů, data se nehýbou; mezi
filesystémy `mv` kopíruje a maže. Totéž Průzkumník ve Windows v rámci
svazku.

**S37 5 B na disku zabere 4 096 B** ✅ ⚠️
Naměřeno: Blockcount 8 (po 512 B) = 4 096 B. Výjimky do komentářů:
prázdný soubor blok nemá, ext4 s volbou `inline_data` (není výchozí)
a Btrfs drobné soubory ukládají přímo do metadat.

**S38 při růstu další blok, vedle nebo jinde, inode zapíše oba** ✅
Rozsahy (extents) v inodu; alokátor ext4 se snaží o souvislost, nezaručí ji.

**S39 fragmentace: HDD musí skákat, SSD to snáší mnohem líp** ✅
Mechanická hlava × bez pohyblivých částí. Formulace záměrně netvrdí, že
na SSD na fragmentaci nezáleží (má měřitelný, ale menší dopad).

**S40 program o tom neví** ✅ — volá `open`/`write`, alokaci dělá filesystem.

**S41 mazání: jméno pryč, inode volný, blok volný** ✅
Naměřeno: po `debugfs rm` zmizel řádek ze `/` a `testb 9884` hlásí
„Block 9884 not in use".

**S42 na klasickém HDD bajty zůstanou, dokud se nepřepíšou** ✅
Naměřeno: `bd 9884` po smazání ukazuje `hello`.

**S43 „Deleting usually doesn't erase anything"** ✏️
Příliš široké: smazání **maže** jméno a ext4 při něm vynuluje i ukazatele
na bloky v inodu (proto je obnova na ext4 těžší než na FAT a dělá se
vyhledáváním obsahu, např. PhotoRec). Nesmaže **obsah**. →
**„Deleting usually doesn't erase the contents."**

**S44 SSD: TRIM/discard, obnova méně pravděpodobná** ✅
ext4 posílá discard při volbě `discard` nebo přes periodický `fstrim`
(systemd `fstrim.timer`, výchozí např. v Ubuntu). Řadič pak může stránky
zahodit; mnoho SSD po TRIM vrací nuly. Formulace „may" a „much less likely"
to kryje. Mimochodem: `mke2fs` sám dělá discard při formátování SSD, proto
ve scénáři není „quick format nemaže data".

**S45 vytvoření souboru = složka, inode, mapa volných bloků** ✅ (S30–S33)

## Selhání (S46–S52)

**S47 blok označený, inode na něj neukazuje → ztracené místo, neškodné** ✅
**S48 inode ukazuje na blok, který mapa vede jako volný → přepis** ✅
Klasické nekonzistence bez žurnálu; `e2fsck` je hlásí jako „block bitmap
differences" a „multiply-claimed blocks". Scéna je ilustrace, proč je žurnál
potřeba (S49), ne popis chování ext4 se žurnálem.

**S49 žurnál: nejdřív zapsat, co se změní; po pádu přehrát dopsané,
nedopsané zahodit** ✅
jbd2 je redo log: nové verze bloků evidence jdou napřed do žurnálu,
transakce se uzavře záznamem commit; při obnově se přehrají jen uzavřené.
Výchozí režim `data=ordered` žurnáluje **metadata**, ne obsah souborů —
scéna mluví o „bookkeeping", takže sedí (kernel.org, ext4 admin-guide,
„Data Mode").

**S50 disk občas změní bit a nic neohlásí** ✅
Tichá korupce dat je doložená: Bairavasundaram a kol., *An Analysis of Data
Corruption in the Storage Stack* (FAST 2008), přes 400 000 neshod kontrolních
součtů na 1,53 milionu disků za 41 měsíců. Číslo ve scénáři není, slouží
k odpovědím.

**S51 ext4 chrání checksumy svou evidenci, obsahu souborů věří** ✅
`dumpe2fs`: feature `metadata_csum` (výchozí od e2fsprogs 1.43, 2016) —
superblok, popisovače skupin, bitmapy, inody, adresáře, rozsahy, žurnál.
Kontrolní součty dat ext4 nemá.

**S52 některé kontrolují obojí, některé opraví z druhé kopie** ✅
Btrfs a ZFS kontrolují data i metadata; opravit umí jen ze zrcadla/DUP/RAID
(Btrfs: metadata jsou na jednom disku ve výchozím stavu DUP, viz výstup
mkfs „Metadata: DUP"). Scéna výslovně odděluje odhalení od opravy.

## Různé filesystémy (S53–S57)

**S53 každý filesystem: číslované bloky, seznam jmen, mapa volného** ✅
Obecně (FAT má mapu i řetězení v jedné tabulce FAT, ale funkci plní).

**S54 ext4 61 milionů předem; NTFS jedna velká tabulka, která roste** ✅
NTFS: Master File Table je soubor `$MFT`, záznamy (typicky 1 KB) přibývají
s potřebou, MFT se zvětšuje (rezervovaná „MFT zone" je jen přednostní
místo, ne pevná tabulka). Naměřeno pro zajímavost: prázdný NTFS na 1 TB
zapsal 97 MB.

**S55 Btrfs nemá pevnou tabulku inodů, vytváří je průběžně; běžně
nepřepisuje na místě** ✅
Inody jsou položky ve stromu metadat; doklad i z tohoto notebooku:
`df -i` na Btrfs `/` a `/home` hlásí **0 inodů** (žádná pevná zásoba).
Copy-on-write je výchozí, výjimka `nodatacow`/`chattr +C` — proto „normally".

**S56 výchozí checksumy dat** ✅
Výstup mkfs: „Checksum: crc32c"; vypnout jde `nodatasum`/`nodatacow`,
proto „by default".

**S57 díky novým kopiím drží staré verze; mění pád, mazání, kopii** ✅
Snapshoty (staré verze, smazaný soubor dál žije ve snapshotu), konzistence
po pádu přes copy-on-write místo žurnálu, reflink (`cp --reflink`, v
coreutils 9 výchozí `auto`) — kopie bez zkopírování dat. Upoutávka na díl 2,
každé z těch tří slov musí díl 2 zaplatit.

## Opravy ve v0.4

| scéna | v0.3 | v0.4 |
|---|---|---|
| S01 | your computer asks you to format it. | it first has to be formatted. |
| S04 | billions of bits | trillions of bits |
| S24 | Linux calls it an inode. | It's called an inode. |
| S43 | Deleting usually doesn't erase anything. | Deleting usually doesn't erase the contents. |

## Úpravy ve v0.5 (zpětná vazba `zpetna vazba 0.4.txt`)

| scéna | změna | proč |
|---|---|---|
| S19 | „…and the drive works out where that is" | číslo sektoru je logická adresa, kde fyzicky leží, ví jen disk (u SSD řadič) |
| S36 | „usually, the contents don't move" | výjimka existuje: přesun mezi subvolumy Btrfs vrátí `rename(2)` chybu `EXDEV` a `mv` pak data kopíruje |
| S44 | „tell the drive that those blocks are no longer needed" | uvolnit blok ve filesystemu ≠ oznámit to disku (TRIM); věta teď popisuje TRIM |
| S49 | „replays only the changes it had finished writing down, and marked as complete. Anything unfinished is ignored." | přehrávají se jen transakce se záznamem commit |
| S57 | „because the old copy isn't overwritten, a snapshot can keep it alive" | copy-on-write staré verze sám nedrží, drží je snapshot (nebo jiný odkaz) |
| S43 | jen zalomení řádku (44 znaků) | |

**Nepřevzato:**
- S18 „numbered blocks of storage" místo „sectors": slovo *block* má ve
  scénáři od S21 význam bloku filesystemu, dvojí význam by diváka mátl.
  *Logical sector* je standardní název (velikost logického sektoru,
  adresování LBA); nepřesnost „číslo = fyzické místo" řeší oprava S19.
- S24 „inode není záznam pro každý název": scéna mluví o souborech
  a složkách, ne o jménech; že jméno v inodu není, říká výslovně S34.
- S25 „who may open it" → „permissions": *may* znamená právě oprávnění,
  ne kdo soubor otevře.
