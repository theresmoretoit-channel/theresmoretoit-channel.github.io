# Fact check — 028 IE6: The Bugs That Had Names

Verze scénáře **0.7**. Ověřeno 2026-09-06.
Čísla scén odpovídají `script 0.7.md` (83 scén).

Podnětem byla `zpetna vazba 0.6.md`, která označila za riziková
místa S34, S47–S50 a celý blok S62–S66. Ověřeny ale byly všechny
ověřitelné výroky, ne jen ty tři — riziko se pozná až po ověření.

---

## Opraveno (tvrzení, které ověřením neprošlo)

### 🔴 S17–S18 — Duplicate Character Bug: komentář byl PŘÍČINA, ne oprava

**Původně stálo:** „You write a list, and IE6 draws the last item twice…
the fix that people actually shipped was to put an HTML comment just
before the closing tag."

**Ověření:** Bug se týká **několika plovoucích elementů**, ne seznamu,
a projeví se zdvojením znaků z posledního plovoucího elementu pod ním.
Spouštěčem jsou **HTML komentáře mezi plovoucími elementy**: první dva
komentáře nedělají nic, každý další přidá dva zdvojené znaky. Nejsnazší
oprava je ten komentář **smazat**. (ROPARDO, Impressive Webs, SitePoint;
původní rozbor byl na positioniseverything.net, dnes mrtvém.)

**Závěr:** měl jsem to obráceně. Přepsáno — komentáře jsou příčina
a počet zdvojených písmen závisí na jejich počtu. Pointa je tím silnější:
zdvojení působí to jediné v souboru, co má prohlížeč zahodit.

### 🔴 S61 — „Leave that tab open" u prohlížeče, který neměl panely

**Ověření:** IE6 panely neměl, přišly až v IE7. Scénář si navíc
v S64 sám říká *„Not the tab, because there were no tabs."*

**Závěr:** vnitřní rozpor. Opraveno na *„Leave that window open."*

### 🟡 S34 — „phantom element" je populární výklad, ne doložená architektura

**Ověření:** Formulace „IE6 měl fantomový element nad `<html>`" je
běžný popis star hacku a najde se v desítkách zdrojů, ale je to popis
**chování**: IE6 přijal selektor `* html` jako shodu, tedy se choval,
jako by `<html>` mělo rodiče. Standardní prohlížeč ví, že nad kořenem
nic není, a pravidlo ignoruje.

**Závěr:** obraz zůstává, tvrzení se změkčilo z „měl" na
*„behaved as though there was another element above the html element."*
Chování je doložené, vnitřní struktura ne.

### 🟡 S49 — AlphaImageLoader: „replaced the image" je nepřesné

**Ověření:** Filtr se aplikuje **mimo běžný vykreslovací proces**,
což je popisováno jako příčina toho, že prvky nad ním přestanou být
klikatelné. Nejde o „nahrazení obrázku". Časté řešení bylo dát odkazům
`position: relative` — tedy zase hasLayout.

**Závěr:** přepsáno na *„it painted outside the browser's normal
rendering process, so links you put on top of it would often stop
working."* Přidáno „often", protože to neplatilo vždy.

### 🟡 S57 — „Hundreds of times a second" je nedoložitelná kvantifikace

Že se `expression()` přepočítával při mousemove, scrollu a dalších
událostech, je doložené. Konkrétní frekvence závisí na stroji
a událostech.

**Závěr:** změněno na *„Over and over again, to work out one width."*
Dramaturgicky to nic nestojí. (Návrh recenzenta.)

### 🟡 S60 — „neither one could see the other" oproti zdroji

Microsoft to popisuje jako *„each side couldn't see the entire cycle
of these circular references."* Opraveno na *„neither side could see
the whole loop"* — blíž zdroji a stejně úderné.

### 🟡 S76 — Google nepřestal podporovat IE6 jako celek

**Ověření:** Rajen Sheth (Google Apps) oznámil v **lednu 2010**, že od
**1. března 2010** přestanou Google Docs a Google Sites v IE6 správně
fungovat. Nešlo o vyhlášení konce podpory napříč Googlem.

**Závěr:** upřesněno na *„Google announced that its own apps would stop
working in it."* Souvislost s pohřbem tím sedí ještě líp: pohřeb byl
**tři dny po tom datu**.

### 🟡 S77 — očekávaná účast nebyla „třicet"

**Ověření:** Pořadatel čekal **30 až 50 lidí**; přišlo **80 až 100**
a akce se musela přestěhovat do většího prostoru.

**Závěr:** upraveno na *„They had planned for thirty."* — spodní mez
pořadatelova odhadu, tedy tvrzení, které sedí. Kontrast zůstává.

---

## Ověřeno, beze změny

| scéna | tvrzení | doklad |
|---|---|---|
| S02 | IE6 vydán 2001, přišel s Windows XP | ověřeno v prvním dílu (017) |
| S02 | za pár let přes 90 % trhu | ověřeno v prvním dílu (017) |
| S07–S08 | **Three Pixel Jog** — mezi plovoucím prvkem a textem vedle něj vznikne 3 px mezera; IE/Win dává levému floatu pravý okraj 3 px | Position Is Everything (přes citace), CSS-Tricks |
| S09–S11 | **Double Margin Bug** — okraj na té straně, na kterou je prvek plovoucí, se zdvojí; přijímaná oprava je `display: inline` na floatu | doloženo spolu s opravou Duplicate Character |
| S12–S14 | **Peekaboo** — obsah zmizí a po odscrollování se vrátí; `position: relative` to opraví | mirror „How To Attack An IE/Win Bug" (Holly hack) |
| S15 | **Guillotine** — pravidla `a:hover` u odkazů plus plovoucí prvky ve stejném rodiči useknou pozadí pod posledním floatem | CSS-Tricks, csscreator |
| S16 | **Magic Creeping Text** a **Border Chaos** jsou skutečná jména z téhož katalogu | seznam PIE/quirksmode |
| S19–S20 | **Expanding Box** — IE6 box zvětší místo přetečení; IE6 neumí `min-height` | Holly hack mirror |
| S23–S26 | **hasLayout** — vnitřní příznak vykreslovacího jádra, není v žádné specifikaci, přímo se nastavit nedá; překlopí ho `float`, `position: absolute`, `display: inline-block`, `width`, `height`, `writing-mode` a `zoom` | ISInc, Impressive Webs, alibabacloud |
| S27–S30 | **Holly Hack** = `height: 1%`; funguje **právě proto**, že IE6 box stejně zvětší — tedy díky Expanding Boxu z S19 | Holly hack mirror, doslova: *„IE/Win will just make the box taller anyway"* |
| S31–S32 | `zoom: 1` je proprietární vlastnost Microsoftu, vizuálně nedělá nic a slouží jen k překlopení hasLayout | *„This is why zoom: 1 did nothing visible. It just flipped hasLayout on."* |
| S33–S36 | **star hack** `* html` vidí jen IE6, ostatní prohlížeče nenajdou shodu | viz oprava S34 výš |
| S37–S39 | **underscore hack** — podtržítko před názvem vlastnosti; standardní prohlížeč řádek zahodí jako neplatný, IE6 podtržítko ignoruje a vlastnost použije | maratz.com, modern-css |
| S40–S42 | **podmíněné komentáře** — Microsoftem dodaný mechanismus; pro ostatní prohlížeče obyčejný komentář | dokumentace MSDN, běžná praxe |
| S43–S46 | XML deklarace před doctypem přepne **IE6 do quirks módu**, kde šířka boxu zahrnuje padding a border; XHTML 1.0 autory k XML deklaraci vybízí; IE7 už tím netrpí | 456 Berea Street, MSDN blog IE, quirksmode |
| S47–S49 | IE6 neumí alfa průhlednost PNG; `AlphaImageLoader` to řeší | 24 ways, CSS-Tricks (viz oprava S49) |
| S50 | průhlednost čehokoli jiného je druhý filtr s vlastní syntaxí vedle běžné vlastnosti | `filter: alpha(opacity=…)` vs `opacity` |
| S51–S52 | vnořené tabulky a **spacer gif** — průhledný obrázek 1 px roztažený na potřebnou velikost | dobově doloženo |
| S53–S55 | v IE6 funguje `:hover` **jen na `<a>`**; řešením byl `.htc` soubor připojený z CSS (`behavior: url(csshover.htc)`, „Whatever:hover" Petera Nederlofa) | peterned.home.xs4all.nl, CSS-Tricks |
| S56–S57 | `expression()` se přepočítával při událostech, mimo jiné při pohybu myši a scrollu | modern-css (viz oprava S57) |
| S58–S59 | **4 095 pravidel** na stylesheet a **31 stylesheetů** na dokument, IE6–IE9 | Stack Overflow, dobře zdokumentovaný limit |
| S60–S61 | JScript spravoval životnost skriptových objektů, DOM objekty běžely na počítání referencí; kruhová reference mezi nimi se nerozvázala. **V IE6 se rozvázala teprve ukončením procesu prohlížeče** — tedy zavřením celého prohlížeče, ne stránky | Microsoft KB 830555, MSDN „Circular Memory Leak Mitigation" |
| S66–S68 | IE byl svázaný s operačním systémem, jeden počítač = jedna verze; odtud police náhradních strojů a později virtuály | dobově doloženo |
| S69–S70 | **Dean Edwards, `IE7.js`** — knihovna, jejímž účelem je přimět IE5.5–6 chovat se jako IE7 | code.google.com/p/ie7-js, dnes zrcadla na GitHubu |
| S76–S77 | pohřeb IE6: **Aten Design Group, Denver, 4. března 2010**, rakev s hlavou z loga IE6, smuteční řeč, 80–100 lidí | CNN, Computerworld, PCWorld, fotoalbum Aten Design Group |
| S78 | **IE tým Microsoftu poslal kytici** s kondolencí *„Thanks for the good times, IE6."* | CNN, Computerworld |
| S79–S80 | `ie6countdown.com` spuštěn **4. března 2011**, tedy **přesně rok po pohřbu**; uváděl 12 % celosvětově a cíl pod 1 % | TechSpot (4. 3. 2011), NBC News, Windows Blog |

---

## 🔴 S62–S66 — `<input type crash>`

Recenzent správně žádal nejdůkladnější ověření právě tady, protože
je to nejlepší reveal videa. Ověřeno **před namluvením v0.6**:

| tvrzení ve scénáři | ověření |
|---|---|
| zápis je `<input>` s atributem `type` **bez hodnoty** | ✅ celá stránka je `<html><form><input type crash></form></html>`; slovo „crash" je libovolné a stačí i holé `<input type>` |
| „forget the equals sign" | ✅ přesně to je ten případ — atribut bez hodnoty |
| IE porovnával typ pole se slovem **hidden** | ✅ *„IE tries to compare the type of the input field to 'HIDDEN'"* |
| šel načíst z **adresy nula** | ✅ *„shlwapi.dll#158 does a case-insensitive comparison of two unicode strings: it reads from address 0x0 because of the null-pointer"* |
| kód **nebyl v prohlížeči, ale ve sdílené systémové knihovně** | ✅ `shlwapi.dll` je knihovna Windows Shellu |
| spadl i **poštovní klient** a **náhled ve správci souborů** | ✅ *„any program using the same libraries as IE will crash, specifically Outlook Express, or even the preview feature in Windows Explorer"* |
| není to specifické pro šestku | ✅ původní hlášení mluví o „any IE since version 4.0", diskuse je z **května 2003**; ve scénáři proto zaznívá jen *„Internet Explorer crashed"*, bez čísla verze |

Zdroj: WebmasterWorld, HTML forum, vlákno 4973 (3.–5. května 2003).

**Co scénář NETVRDÍ a tvrdit nesmí:** že spadla „všechna otevřená okna
prohlížeče". Tak to stálo ve v0.5 a doložit se to nepodařilo, takže to
ve v0.6 nahradil doložený a silnější důsledek — pád mimo prohlížeč.

---

## Zdroje

- WebmasterWorld, „HTML-Code crashes Internet Explorer", vlákno 4973 (2003)
- „How To Attack An IE/Win Bug" (Holly hack), zrcadlo na arantius.com
- Microsoft KB 830555; MSDN „Circular Memory Leak Mitigation"
- 456 Berea Street, „Using an XML declaration triggers Quirks mode in IE 6"
- Peter Nederlof, „Whatever:hover" (`csshover.htc`)
- Dean Edwards, `ie7-js`
- CNN, Computerworld, PCWorld — pohřeb IE6, 4. 3. 2010
- TechSpot, NBC News — `ie6countdown.com`, 4. 3. 2011
- CSS-Tricks, modern-css.com, maratz.com — dobové popisy hacků
