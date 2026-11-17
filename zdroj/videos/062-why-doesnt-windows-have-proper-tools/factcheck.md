# Fact check — 062 „Why Doesn't Windows Have Proper Tools?"

Verze scénáře **0.2**, ověřeno 2026-09-21.

Podnětem byla tvoje zpětná vazba k 0.1: nechat projít tvrdým ověřením
právě ta nejsebevědoměji formulovaná tvrzení. **Tři z pěti vytipovaných
byla skutečně vadná** a jedno se muselo přeformulovat jako interpretace.

---

## A. Co bylo ŠPATNĚ a je opraveno

### A1. „They hired the two people who wrote it. One of them runs Microsoft's cloud division today." — DVĚ chyby

| | |
|---|---|
| **autorství** | Process Explorer napsal **Mark Russinovich sám**. Bryce Cogswell spoluzaložil Winternals Software a web sysinternals.com, ale u Process Exploreru je uváděný jako autor Russinovich. „Ti dva, co to napsali" je nepřesné |
| **role** | Russinovich je **Chief Technology Officer a Technical Fellow pro Microsoft Azure**, k tomu Deputy CISO. **Cloudovou divizi neřídí** — to je obchodní jednotka pod jiným vedením. „Runs Microsoft's cloud division" je povýšení, které neexistuje |

**Opraveno na:** *„And they got the man who wrote it. / He is the chief
technology officer of Microsoft's cloud business today."*

### A2. „In 2017, an antivirus company filed complaints in three countries" — datum i počet

Skutečný průběh:

| kdy | kde |
|---|---|
| **konec 2016** | Kaspersky podává stížnost u ruského antimonopolního úřadu (FAS) |
| **červen 2017** | dvě další stížnosti — Evropská komise a německý Bundeskartellamt |
| **srpen 2017** | Kaspersky stížnosti v Berlíně a Bruselu **stahuje**, protože Microsoft přislíbil změnit chování Windows vůči antivirům třetích stran |

Dvě vady: začalo to **2016**, ne 2017. A „tři země" nesedí — Evropská
komise není země, jsou to **tři úřady ve třech jurisdikcích**.

**A vypadl závěr.** Původní znění nechalo diváka v domnění, že spor
běží nebo že Microsoft prohrál. Skutečnost je zajímavější a tezi videa
posiluje: **Microsoft chování změnil a stížnosti tím zmizely.**

**Opraveno na:** *„Starting in 2016 … regulators in Russia, then in
Germany, then in Brussels"* + nová scéna S93b se stažením stížností.

### A3. „The case ran for three years. For a while, breaking the company up was on the table." — pravdivé, ale zamlčuje to podstatné

Co se skutečně stalo:

| | |
|---|---|
| **18. 5. 1998** | DOJ a dvacet států podávají žalobu; jedním ze čtyř bodů je **nezákonné svázání IE s Windows** |
| **červen 2000** | soud prvního stupně nařizuje **rozdělení firmy na dvě** |
| **28. 6. 2001** | odvolací soud (D.C. Circuit) rozdělení **ruší**. Udržování monopolu na OS **potvrzuje**, pokus o monopolizaci trhu prohlížečů **ruší**, a bod o svázání **vrací nižšímu soudu** s pokynem posuzovat ho podle „rule of reason", ne jako zakázané samo o sobě |
| **2. 11. 2001** | smír. Vrácený bod o svázání se tím **už nikdy nedoprojednal** |

Formulace 0.1 byla obhajitelná, ale **nejsilnější fakt zahodila**:
otázka, jestli je přibalení prohlížeče do Windows legální, **nebyla
nikdy zodpovězená**. Pro tezi videa je to lepší než prohra i výhra —
firma, která plánuje, co dát do krabice, čelí **nevyřešenému právu**,
a to je přesně ten mrazivý účinek, o kterém video mluví.

**Opraveno na** tři scény (S86, S86b, S86c) včetně věty *„was never
actually answered."*

---

## B. Co bylo formulované jako fakt a je to INTERPRETACE

### B1. „There are three reasons"

Zpětná vazba to trefila. Tři vysvětlení jsou **naše skladba**, ne
zjištění. Doložitelnost se navíc liší kus od kusu:

| vysvětlení | co ho drží |
|---|---|
| **platforma** | deklarovaná strategie Microsoftu, doložitelná z jeho vlastní komunikace k vývojářům — ale že způsobila *tenhle* konkrétní následek, je úsudek |
| **antimonopol** | **soudní spisy, rozhodnutí a pokuty.** Jediné z trojice, co má tvrdý doklad |
| **v krabici = navždy** | doložitelný je jen **projev** (PowerToys vydané ven a nepodporované), ne vnitřní důvod |

**Opraveno na:** *„There are three explanations. / Only one of them
has court records. / Keep an eye on which."*

Tím se divákovi přizná míra jistoty rovnou v hlase, a přitom to
funguje jako režijní pokyn dopředu — je to silnější, ne slabší.

### B2. „The desktop stopped being the thing worth defending."

Ryzí interpretace. **Podloženo číslem** z uzávěrky Microsoftu za
fiskální rok 2025:

| divize | tržby | podíl |
|---|---|---|
| Productivity and Business Processes | 120,8 mld. $ | 42,9 % |
| Intelligent Cloud | 106,3 mld. $ | 37,7 % |
| **More Personal Computing** (obsahuje Windows) | **54,6 mld. $** | **19,4 %** |
| celkem | 281,7 mld. $ | |

Windows tedy sedí v **nejmenší ze tří divizí**, ta dělá **necelou
pětinu** tržeb — a Windows je jen její část, protože do téže divize
patří **Xbox**, Surface a reklama ve vyhledávání. Samostatné číslo za
Windows Microsoft nezveřejňuje.

**Opraveno na** tři scény (S123, S123b, S123c), které říkají přesně
tohle, a S126 zmírněno na *„The desktop is no longer the thing being
defended."*

### B3. Závěrečná pointa „was not allowed to be good at"

Máš pravdu, že doslova to Windows nikdo nezakázal. Mechanismus, který
za tím stojí, není zákaz, ale **cena**: přibalit nejlepší nástroj zdarma
na miliardu strojů znamená zlikvidovat existující trh, a to je přesně
ten krok, kvůli kterému firma tři roky stála před soudem a zaplatila
v Evropě půl miliardy eur.

**Opraveno na:** *„It's that for twenty years, being brilliant at this
was the one thing Windows could not afford to be."*

„Could not afford" je doložitelné a přitom to punchline neubírá —
naopak pojmenovává mechanismus, kdežto „not allowed" ho jen naznačoval.

### B4. Jedna interpretace, kterou hlásím SÁM, protože ji nikdo nevytipoval

Celá **odpověď 2 je kauzální domněnka**. Neexistuje dokument, ve kterém
by Microsoft napsal „správce souborů jsme nedodali kvůli antimonopolu".
Doložené je čtvero: (a) žalovali je za přibalení, (b) pokutovali je za
přibalení, (c) stěžovali si na ně za přibalení, (d) své nejlepší
nástroje prokazatelně drží mimo krabici. Spojnice mezi tím je úsudek.

**A je tu doklad, který tu domněnku sám omezuje:** PowerToys vyšly
**1996**, tedy **dva roky před žalobou**. Antimonopolem je vysvětlit
nelze. Právě proto jsou ve scénáři zařazené pod vysvětlení 3, ne 2 —
kdyby se použily jako doklad antimonopolu, byl by to anachronismus.

Scénář to nikde netvrdí jako prokázané a S76b diváka varuje předem.
Pokud ti to pořád přijde silné, nejlacinější pojistka je jedna věta
typu *„Nobody at Microsoft ever wrote this down."* — ale podle mě to
S76b už pokrývá.

---

## C. Ověřená tvrzení, která prošla beze změny

| scéna | tvrzení | doklad |
|---|---|---|
| S12 | dvoupanelový správce funguje od **1993** | Windows Commander vydán **25. 9. 1993** pro Windows 3.1x |
| S14 | jeden vývojář, Švýcarsko, **Christian Ghisler** | autorova vlastní stránka |
| S16 | prvních **devět let** se jmenoval jinak | 1993 az 2002 |
| S18–S19 | léto **2002**, dopis od právníků zastupujících **majitele ochranné známky Windows** | `ghisler.com/name.htm`: *„In Summer 2002, we received a letter from attorneys representing the owner of the trademark 'Windows'… we didn't want to risk a lawsuit, and decided to change the name."* Ghisler Microsoft **sám nejmenuje**; scénář ho jmenuje až ve vlastní větě (S20), což je bezpečné — známku vlastní Microsoft |
| S23 | **DOS Shell, 1988**, levý a pravý panel, v krabici | MS-DOS a PC DOS **4.0, červen 1988**, dvojitý seznam adresářů a souborů |
| S24 | Microsoft ho **odstranil** | zrušen v MS-DOS 6.0; na doplňkové disketě přežil do 6.22 |
| S32–S34 | `Everything` čte **MFT** a pak **change journal** | MFT se čte jednorázově při prvním indexování, pak už jen USN journal, který vede sám ovladač NTFS |
| S35–S36 | Windows Search je pomalejší, protože čte **obsah** a řeší **oprávnění** | dokumentované chování indexeru |
| S65 | Process Explorer ukazuje vlákna, handly, čekání na soubor, rodičovský proces | dokumentace nástroje |
| S67–S68 | Microsoft je koupil **v roce 2006** | Winternals Software (zal. 1996), akvizice **18. 7. 2006** |
| S70 | vlastní to **dvacet let** | 2006 az 2026 |
| S71–S72 | Microsoft to **sám distribuuje** a **pořád to není ve Windows** | nástroje běží na `learn.microsoft.com/sysinternals`; Process Explorer není součástí instalace Windows |
| S81 | **Apple dodává nástroj na snímky obrazovky** | ano, vestavěný |
| S83–S85 | **1998**, americká vláda, a žalobním bodem bylo **přibalení**, ne kvalita prohlížeče | žaloba 18. 5. 1998; svázání IE s Windows je jeden ze čtyř bodů |
| S87–S88 | **2004**, téměř **půl miliardy eur**, a příkaz dodat Windows **bez přehrávače** | rozhodnutí Evropské komise z **března 2004**, pokuta **497 mil. €**, vznikají edice Windows XP N. *(Rozhodnutí řešilo i interoperabilitu serverů — scénář to vynechává, protože to není zjednodušení ve prospěch teze, jen zkrácení)* |
| S95 | „miliarda strojů" | Microsoft sám uvádí řádově 1,4 mld. aktivních zařízení; „a billion" je bezpečné |
| S101–S103 | **PowerToys 1996**, od inženýrů Microsoftu, samostatné stažení, **oficiálně nepodporované** | první sada pro Windows 95 vydána **17. 11. 1996**; Tweak UI se v dobových materiálech popisuje jako jeden z „non-supported PowerToys" a KB článek u nich výslovně uvádí konfiguraci nepodporovanou technickou podporou Microsoftu |
| S108, S111 | Linux to řeší jedním příkazem, protože distribuce software **sama sestavuje a balí** | podstata systému balíčků |
| S119 | balíčkovač přišel v **2021** | winget **1.0 vydán 27. 5. 2021**, ohlášen 2020, ~1 400 balíčků při vydání |
| S120 | pořádný terminál, **běží na tom Linux**, PowerToys se vrátily **2019** jako open source | Windows Terminal, WSL, PowerToys znovu na GitHubu od **září 2019** |
| S123b–S123c | nejmenší ze tří divizí, **necelá pětina** tržeb, **obsahuje Xbox** | viz tabulka v B2 |
| S128 | PowerToys, Process Explorer i Sysinternals **si stahuješ sám** | ani jedno není součástí instalace Windows |

---

## D. Dvě místa, která nejsou chyba, ale vědomé zjednodušení

1. **„thirty years"** (S02). Windows 1.0 je 1985, tedy jedenačtyřicet let;
   od Windows 95 jedenatřicet. Ve větě to funguje jako řádová veličina,
   ne jako datum. Kdyby ti to vadilo, *„three decades"* nebo *„forty years"*
   sedí obojí.
2. **„nine hundred gigabytes"** (S40). Ilustrativní číslo, ne tvrzení.

---

## E. Co tenhle fact check NEOVĚŘUJE

Podle pravidla z `CLAUDE.md` ověřuje tenhle dokument **pravdivost, ne
potřebnost**. Otázka „na co se divák ptá PO té scéně" je na tobě při
škrtání — a týká se hlavně prohlídky nástrojů S39 az S60, kde čtyři
ze sedmi nástrojů jen dokládají opakování a pointu nenesou.

A neověřuje **obraz**. Až bude storyboard, platí, že diagram tvrdí i to,
co v popisku není — zvlášť u scén, kde něco míří na někoho (S83 az S93
je blok, kde žaluje jeden druhého, a je to přesně ten tvar, u kterého se
šipka snadno otočí na špatnou stranu).
