# 046 — Fact check

Ověřeno 2026-09-14 proti `script 0.2.md`. Projeta **každá** ověřitelná
věta scénáře, ne jen ta, která vypadala riskantně.

**Výsledek: dvě věcné chyby a jedno podstřelené číslo.** Všechny tři
opraveny, scénář postoupil z `0.1` na `0.2`.

**A čtvrtou našel až poslech draftu** — zastaralé tvrzení o Linuxu.
Opraveno v `0.3`, viz poslední kapitola.

---

## ❌ S34 — pořadí Windows 2000 a Windows ME bylo OBRÁCENĚ

**Bylo v 0.1:**

> Windows 95. Windows 98. Windows ME. […]
> **Then came Windows 2000. Then XP.**

**Ověřeno:**

| verze | vydání | základ |
|---|---|---|
| Windows 95 | 24. 8. 1995 | MS-DOS |
| Windows 98 | 25. 6. 1998 | MS-DOS |
| **Windows 2000** | **17. 2. 2000** | **NT** |
| **Windows Me** | **14. 9. 2000** | MS-DOS |
| Windows XP | 25. 10. 2001 | NT |

**Windows 2000 vyšlo o sedm měsíců DŘÍV než Windows ME**, ne po něm.
Nebyl to nástupce — byla to **paralelní řada**. Windows 2000 je NT pro
firmy, ME poslední domácí systém postavený na MS-DOSu. Obě linky spojilo
až XP, které je nástupcem obou.

Věta *„Then came Windows 2000"* tedy tvrdila příčinnou i časovou
posloupnost, která neexistuje. A je to přesně ten druh chyby, kterou
popisuje `CLAUDE.md`: **vznikla zkrácením** — v zadání byl jen výčet
„Windows 2000. XP. A pozdější generace.", ze kterého jsem udělal
časovou osu.

**Opraveno na 0.2:**

> But underneath, Microsoft had a second, sturdier line.
> Windows NT.
> And in 2001, Windows XP finally brought it to ordinary home computers.

Tahle verze je nejen správná, ale i **silnější vyprávění**: vysvětluje,
*proč* se Windows zlepšily, místo aby jen vyjmenovala verze. Zároveň
navazuje na S19 (*„graphical shell running on top of MS-DOS"*) — divák
teď vidí, že se ten základ vyměnil.

Zdroj: [List of Microsoft Windows versions](https://en.wikipedia.org/wiki/List_of_Microsoft_Windows_versions)

---

## ❌ S02 — „hundreds of millions" podstřelilo o řád

**Bylo v 0.1:** *Windows runs on hundreds of millions of computers.*

Microsoft uvádí pro fiskální rok 2026 **1,6 miliardy** měsíčně aktivních
zařízení s Windows (Nadella, duben 2026; v červnu 2025 to bylo 1,4 mld.).
„Stovky milionů" tedy nejsou nepravda, ale **sedmkrát menší číslo**, než
jaké platí — a věta stojí hned v druhé scéně, kde má vybudovat měřítko.

**Opraveno na 0.2:** *Windows runs on more than a billion computers.*
Hedge „more than" drží i kdyby se údaj hýbal.

Zdroj: [Nadella: 1,6 mld. měsíčně aktivních zařízení](https://www.windowslatest.com/2026/04/30/microsofts-satya-nadella-confirms-1-6-billion-monthly-windows-users-bing-crosses-1-billion-for-the-first-time/), [1,4 mld. v r. 2025](https://www.tomshardware.com/software/windows/windows-seemingly-lost-400-million-users-in-the-past-three-years-official-microsoft-statements-show-hints-of-a-shrinking-user-base)

---

## ⚠️ S40 — Netscape vypadl při zkracování, vrácen

Zkrácení sekce 4 z 0.1 nechalo *„the antitrust case around Internet
Explorer"*. Jenže spor **byl** o Netscape: jádrem žaloby bylo, že
Microsoft váže IE na Windows a tím dusí Netscape Navigator. Bez toho
jména věta nedává smysl — „spor kolem Internet Exploreru" zní jako spor
o prohlížeč sám.

Vráceno v 0.2 (*„around Internet Explorer and Netscape"*), stojí to
tři slabiky.

---

## ✅ Co prošlo

| scéna | tvrzení | ověření |
|---|---|---|
| **S09** | *Some programs written in the 1990s still run on Windows today.* | **Platí, a „some" je tam nutné.** 32bitové aplikace běží na 64bitových Windows 11 přes **WOW64** bez zásahu. **16bitové NE** — `NTVDM` na 64bitových Windows není a nejde doplnit, protože long mode x86-64 neumí VM86 režim, na kterém stál. Bez slova „some" by věta byla nepravdivá. |
| **S09** | *Thirty years later, on hardware that didn't exist.* | 1995–2026 je 31 let; „thirty years" je zaokrouhlení dolů, ne nadsázka |
| **S18** | *more than forty years of building* | Windows 1.01 vyšel **20. 11. 1985**, tedy 40 let a 10 měsíců. „More than forty" těsně, ale platí |
| **S19** | *It started as a graphical shell running on top of MS-DOS.* | Windows 1.0 az 3.x běžely nad MS-DOSem; 95/98/ME na něm byly postavené. NT řada ne — proto je ve S34 ta oprava |
| **S30** | *Windows 95. Windows 98. Windows ME.* | výčet bez tvrzení o pořadí — po opravě S34 už není zavádějící |
| **S39** | *Windows became the dominant operating system for personal computers.* | StatCounter 2026: 56–70 % podle metodiky a období. Dominantní ano; **konkrétní procento se ve videu záměrně neříká**, protože se čísla mezi zdroji liší o 14 bodů |
| **S40** | *antitrust case* | *United States v. Microsoft Corp.*, podáno **18. 5. 1998**, skutková zjištění 5. 11. 1999, právní závěry 3. 4. 2000, nařízené rozdělení 7. 6. 2000, dohoda s DOJ 1. 11. 2001, potvrzena 1. 11. 2002, odvolací soud 30. 6. 2004. Scénář žádné z těch dat neuvádí, jen říká „long series of fights" — a to je přesné |
| **S40** | *a long series of fights with its competitors* | vedle US v. Microsoft i evropská řízení; „series" v množném čísle sedí |
| **S53** | *Windows is proprietary software. Closed source.* | ✅ |
| **S58** | *With open source you can read the code… and if the licence allows it, build your own version.* | podmínka *„if the licence allows"* je tam správně — copyleft (GPL) i permisivní licence to dovolují, ale s různými povinnostmi, a ne každá „source available" licence je open source |
| **S59–S60** | *You can watch its network traffic. You can take the binary apart, all the way down to processor instructions.* | disassemblování a analýza provozu; scénář netvrdí, že je to legální všude ani že je to snadné — S62 výslovně říká opak |
| **S66–S69** | distribuce, desktopové prostředí, volba programů | ✅ |
| **S75** | *Apple builds the hardware and the software together.* | ✅ |
| **S87** | *Updates. OneDrive. A Microsoft account. Edge. Notifications.* | všechno jsou skutečné součásti dnešních Windows 11 |

---

## Věty vzniklé SLOUČENÍM nebo ZKRÁCENÍM

`CLAUDE.md` (pravidlo z videa 032) žádá, aby se ověřovaly i věty, které
v zadání takhle nestály. Ve `script 0.2.md` je takových šest — a **dvě
z nich nesly obě nalezené chyby**, takže se to pravidlo znovu zaplatilo.

| scéna | vznik | verdikt |
|---|---|---|
| **S34** | zkrácení výčtu verzí na časovou osu | ❌ **chyba, opraveno** (viz výš) |
| **S40** | zkrácení sekce 4 | ⚠️ **vypadl Netscape, vráceno** |
| **S42** | *„So you can dislike Windows without having any problem with its technology."* — sloučení dvou vět zadání | ✅ tvrzení se nezměnilo |
| **S51** | *„You can complain. You can buy a different car. But you cannot take their software and keep the feature working."* — ze tří vět zadání dvě | ✅ pointa zachována |
| **S61** | *„But that is dismantling the finished car instead of reading the service manual."* — zhuštění dvou vět | ✅ |
| **S65** | *„Because the argument was never really about bugs. It was about who decides."* — **věta, která v zadání není vůbec** | ✅ není to faktické tvrzení, nýbrž teze videa. Shrnuje sekce 5–7 zadání a nic nepřidává |
| **S94–S95** | sloučení sekcí 13 a 14 | ✅ |

---

## Obrázky

Ověřit se musí i vizuál, ne jen text (`CLAUDE.md`). Až vznikne
`storyboard.json`, hlídat u archivních scén:

- **žádné logo ani snímek obrazovky Windows** — ochranná známka i autorské
  právo; scény o konkrétních verzích patří spíš do diagramu než do archivu
- **modrá obrazovka smrti (S31)**: skutečný snímek BSOD z Windows 9x na
  Commons existuje, ale bývá to **fotografie cizí obrazovky** s nejistou
  licencí. Kreslený BSOD kódem je bezpečnější a projekt na to má `_kit.py`
- **portréty nikoho** — video nejmenuje žádnou osobu, takže odpadá pravidlo
  „celá hlava s odstupem"

---

## Co se ve videu ZÁMĚRNĚ netvrdí

Zapsáno, aby to příště nikdo „nedoplnil":

- **konkrétní podíl na trhu** — zdroje se liší o 14 procentních bodů
  (56,6 % az 70 % podle metodiky a měsíce), takže video říká jen „dominant"
- **že Windows dnes padají víc nebo míň než Linux či macOS** — na to kanál
  nemá číslo a srovnatelná data prakticky neexistují
- **že telemetrie Windows dělá konkrétně tohle** — S87 jmenuje jen to, co
  divák vidí na obrazovce (Updates, OneDrive, účet, Edge, oznámení)
- **kdo ze tří táborů má pravdu** — to je pointa videa


---

## ❌ Čtvrtá chyba: „Linux je skládačka, na které je práce"

**Našel ji uživatel při poslechu draftu, ne tenhle fact check.** A je to
poučení o tom, co se má ověřovat.

**Bylo v 0.2** (S69–S72 a S83):

> You choose a distribution. A desktop environment. Your programs.
> You can study the system and change it. […] That is also Linux.
> […] But for some people that freedom matters more than convenience.
> […] Linux says: you want control? Here you go. **But some of the work
> is yours.**

Dohromady to tvrdí, že u Linuxu si člověk musí vybírat a část práce je
na něm. **To u běžné dnešní distribuce neplatí.** Mainstreamová
distribuce se nainstaluje podobně jako Windows a uživatel se nemusí
dotknout terminálu. Ta možnost tam je; povinnost ne.

**Opraveno v 0.3:**

| bylo | je |
|---|---|
| „You can study the system and change it." | „And if you want to, the system itself." + nová scéna **S69b** („Install a mainstream distribution today and you may never open a terminal at all.") |
| „That is also Linux." | „That is Linux too. But it is an option, not the price of entry." |
| „that freedom matters more than convenience" | „For some that freedom is the whole point. For everyone else it simply sits there until they need it." |
| „But some of the work is yours." | „As much or as little as you like." |

### Proč to tenhle fact check propásl

Prošel **čísla, jména, data a fyzikální tvrzení** — a tohle není ani
jedno z toho. Je to **tvrzení o tom, jaké něco JE**, u kterého se
odpověď mění v čase. Takové věty nemají v textu žádný poznávací znak
(nejsou v nich číslice ani vlastní jména), takže je hledání rizikových
míst přeskočí.

> **Pravidlo pro příště:** do seznamu ověřovaných tvrzení patří i věty
> tvaru **„X je takové a takové"** a **„u X musíš Y"**, zvlášť když se
> týkají živé technologie. U nich se neptej „je to pravda?", ale
> **„platilo to naposled kdy?"**.

Ve `script 0.3.md` jsou takových vět ještě tři a všechny obstály:

| scéna | tvrzení | proč platí |
|---|---|---|
| S26 | *„A program written twenty years ago may still expect a particular interface…"* | pořád platí; `may` je správný hedge |
| S75 | *„Apple builds the hardware and the software together."* | platí |
| S87 | *„Updates. OneDrive. A Microsoft account. Edge. Notifications."* | všechno jsou součásti dnešních Windows 11 |
