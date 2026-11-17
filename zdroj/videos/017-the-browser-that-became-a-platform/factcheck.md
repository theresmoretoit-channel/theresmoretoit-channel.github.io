# Fact check — Internet Explorer 6: The Browser That Became a Platform

Ověřeno 1. 9. 2026 proti `script 0.4.md` (86 scén). Čísla scén platí pro v0.4.
Prošlo se **každé ověřitelné tvrzení**, ne jen ta, která vypadala riziková —
a dvě ze tří oprav jsou právě z těch, které rizikově nevypadaly.

**Výsledek: 3 opravy, 4 poznámky pro storyboard, zbytek prošel.**

---

## ❌ Opraveno

### 1. S03 + S36 — mezera mezi obrázky NENÍ vada Internet Exploreru

**Tvrzení (hook S02–S03):** *„It works in Netscape. It works in Opera. It works
in the new Firefox. And then you open it in Internet Explorer. Everything is
broken. … And somehow, adding one line break to your HTML has created a three
pixel gap."*

**Ověření:** Mezera mezi dvěma `<img>` na samostatných řádcích je **standardní
chování CSS ve všech prohlížečích**, ne chyba Trident. Řádkové (inline) elementy
berou zalomení řádku ve zdroji jako mezeru mezi slovy; CSS-Tricks to shrnuje
větou *„It's not a bug. It's how the browser renders inline content by default."*
Netscape, Opera i Firefox tu mezeru udělají také.

**Proč to prošlo autorovi i mně:** věta je *doslova pravdivá* — v IE ta mezera
opravdu je. Nepravdivá je až **implikace z rámování hooku**, že to dělá IE
a ostatní prohlížeče ne. To žádná kontrola jednotlivé věty nechytí.

**Oprava:** věta v S03 zůstala (je to nejlepší vtip hooku a je autorova),
ale kapitola, která ji vysvětluje, ji teď **výslovně nepřipisuje IE**:

> S36: Here's another wonderful example. Whitespace.
> **And this one wasn't even Internet Explorer's fault.**

Je to zároveň lepší video: teze celého dílu je „je to složitější než IE bad",
takže přiznat, že jedna z ikonických otravností za IE nemohla, hraje pro ni.

### 2. S29 — chybělo „in quirks mode", a bez toho to tvrdí nepravdu o IE6

**Tvrzení:** *„Older versions of Internet Explorer read it differently.
The declared width could include the padding and the border."*

**Ověření:** IE 4 a IE 5.x počítaly šířku od okraje k okraji **vždy**. Ale
**IE6 v standards mode počítá box model SPRÁVNĚ** podle W3C; starý model
používá jen v quirks mode (Wikipedia, *Internet Explorer box model bug*:
*„As of Internet Explorer 6, the browser supports an alternative rendering mode
… which solves this discrepancy"*, a *„Internet Explorer in 'quirks mode'
includes the content, padding and borders within a specified width or height"*).

Ve videu o IE6 si divák „older versions" přečte jako „IE6 a starší" a odnese
si, že IE6 měl box model rozbitý. Neměl — když se poslal správný doctype.

**Kde se to pokazilo:** zdroj autora **„in quirks mode" MĚL**. Vypadlo to při
mém škrtání v0.2 jako výplňové sousloví. Nebyla to výplň, byla to nosná
přesnost.

**Oprava:** vráceno zpátky. *„In quirks mode, the declared width could include
the padding and the border."*

> **Poučení do dalších škrtů:** kvalifikátor typu „in quirks mode", „older",
> „originally", „almost" vypadá při krácení jako vata, protože nenese děj.
> Nese ale **rozsah platnosti tvrzení**, a to je to jediné, co dělá rozdíl
> mezi pravdou a nepravdou. Při škrtání je proto **kontroluj proti zdroji,
> ne proti rytmu věty.**

### 3. S07 — Netscape dominoval v POLOVINĚ devadesátek, ne na konci

**Tvrzení:** *„In the late nineteen nineties, the web was dominated by
Netscape Navigator."*

**Ověření (měřeno, ne vzpomínáno):**

| rok | Netscape | Internet Explorer |
|---|---|---|
| konec 1995 | ~80 % | pod 10 % |
| 1996 | **~86 %** | pod 10 % |
| konec 1997 | **51 %** | ~40 % |
| 1998 | menšina | **vede** |

„Late nineteen nineties" znamená 1997–1999, a v té době už Netscape
dominantní nebyl — v roce 1998 vedlo IE. Dominance byla **1995–1996**.

**Oprava:** *„In the **mid** nineteen nineties…"*. Vedlejší přínos: navazující
beat (bundling s Windows) tím sedí i chronologicky — IE 1.0 přišlo s Windows 95
v srpnu 1995 a IE4 v roce 1997.

---

## ⚠️ Poznámky pro storyboard — text je v pořádku, obraz může lhát

### 4. S55 — seznam prohlížečů NENÍ chronologický

**Text:** *„Firefox appeared. Opera continued developing. Safari arrived.
And eventually Google released Chrome."*

| | datum |
|---|---|
| Safari 1.0 (public beta) | **7. 1. 2003** |
| Firefox 1.0 | **9. 11. 2004** |
| Google Chrome | **2. 9. 2008** |

**Safari je o rok a deset měsíců starší než Firefox 1.0**, takže pořadí ve
větě chronologické není. Věta to netvrdí (`and eventually` označuje jen
Chrome jako poslední) a text zůstává beze změny.

> **Ale diagram to tvrdit umí.** Kdyby se ten seznam nakreslil jako časová
> osa nebo jako svislý sled shora dolů, obraz řekne „Safari přišlo po
> Firefoxu", což je nepravda. Je to přesně případ z CLAUDE.md
> („diagram tvrdí i to, co v popisku není"). **Kreslit jako množinu, ne
> jako osu** — čtyři loga vedle sebe, žádné pořadí. Kdyby uživatel osu
> chtěl, musí se přeskládat text.

### 5. S60 — Netflix na Silverlightu ano, ale nebyl to jeho PRVNÍ přehrávač

**Text:** *„Silverlight let developers build rich browser applications using
C sharp and dot NET. It even powered Netflix's early streaming."*

| | |
|---|---|
| Netflix „Watch Instantly" spuštěno | **leden 2007** — přehrávač Windows Media, jen Windows + IE |
| přechod na Silverlight | **27. 10. 2008** (přineslo podporu Maců) |
| oznámení přechodu na HTML5 | **2013** (Netflix Tech Blog, po oznámení konce Silverlightu) |
| Silverlight u Netflixu dojel | **13. 9. 2023** |

„Early streaming" je tedy **v pořádku** (2008–2013 je raná éra Netflixu),
ale první přehrávač Silverlight nebyl.

> **Bonus, který hraje pro tezi videa:** oba první přehrávače Netflixu byly
> proprietární microsoftí platformy v prohlížeči — nejdřív **ActiveX**
> (Windows Media), potom **Silverlight**. Teprve třetí byl HTML5. Kdyby se
> scéna někdy rozšiřovala, tohle je materiál. Do v0.4 se nepřidávalo,
> protože scénář je schválený.

### 6. S86 — „twenty years later" je řečnická figura, ne datum

IE6 vyšlo **2001**, dnes je **2026**, tedy **dvacet pět let**. Táž věc v S82
(*„what it had spent twenty years creating"*): IE žilo 1995–2022, tedy
dvacet sedm let. Obojí je idiom, ne měření, a **nemění se** — ale kdyby to
někdo v komentářích počítal, tohle je odpověď.

### 7. S20 — Windows Update a ActiveX: pravda, ale ve dvou verzích jinak

**Text:** *„Even Windows Update itself originally relied on ActiveX to inspect
the system and work out which updates were required."*

**Ověření:** Webová aplikace Windows Update **vyžadovala ActiveX** (a tedy IE
nebo prohlížeč s podporou ActiveX). Rozdělení podle verzí:

| verze | co dělala |
|---|---|
| **v3** (nejstarší) | stáhla úplný seznam všech dostupných aktualizací a **vybrala si sama na klientu**, co stáhnout a nainstalovat |
| **v4** (2001, s Windows XP) | udělá **inventuru hardwaru a softwaru** a pošle ji službě — rozhodování se přesune na servery Microsoftu |

Slovo *„originally"* míří na v3 a tam sedí doslova. U v4 (tedy zrovna v éře
IE6) se „work out which updates were required" děje na serveru. Tvrzení
**platí**, protože je omezené slovem *originally*; kdyby se rozšířilo na
éru XP, přestalo by platit.

### 8. S01–S02 — „early two thousands" a „the new Firefox" se potkávají jen těsně

**Text:** *„Imagine being a web developer in the early two thousands. …
It works in the new Firefox."*

Firefox 1.0 vyšel **9. 11. 2004** (pod jménem Firefox od února 2004, předtím
Phoenix 2002 a Firebird 2003). „The new Firefox" tedy ukazuje na **konec roku
2004 a rok 2005**, což je spíš polovina dekády než „early two thousands".

Drží to pohromadě jen proto, že éra IE6 trvala 2001–2006 a Netscape 7 se
tou dobou ještě používal, takže všechny tři prohlížeče z hooku spolu
opravdu existovaly. **Nemění se** — je to nálada, ne datum. Kdyby to
někdo v komentářích počítal, tohle je odpověď.

---

## ✅ Ověřeno beze změny

| scéna | tvrzení | doklad |
|---|---|---|
| S08 | IE se přibalovalo k Windows a bylo zdarma | doloženo napříč zdroji k browser wars; strategie od Windows 95 / IE 1.0 (1995) |
| S09, S26 | v raných dvoutisících měl IE **přes devadesát procent** trhu | vrchol **95,4 %** v červenci 2003; samotné IE6 „high 80s" v letech 2002–03, ~90 % v polovině 2004 |
| S10 | IE6 přišlo **v roce 2001 spolu s Windows XP** | IE6 vydáno **24. 8. 2001**, Windows XP **25. 10. 2001**, IE6 je součástí XP RTM |
| S17 | ActiveX komponenta mohla sáhnout na soubory, aplikace, hardware i OS | podstata ActiveX (COM v prohlížeči); doloženo bezpečnostní literaturou k IE6 |
| S23 | VBScript, DHTML, CSS `expression()` jsou microsoftí rozšíření | ✅ |
| S24 | IE uměl vyhodnotit **JavaScript přímo v CSS** | „dynamic properties" / `expression()`; **zavrženo v IE8**, v IE11 už se v internetové zóně nevyhodnocuje |
| S27, S28 | šířka 200 + padding 2× 20 + rámeček 2× 5 = **250 px** | 200 + 40 + 10 = 250 ✅ (spočítáno, ne převzato) |
| S30 | dnes se totéž chování žádá schválně a jmenuje se **border box sizing** | `box-sizing: border-box` ✅ |
| S32 | `hasLayout` **není normální CSS vlastnost ani součást standardu**, ale rozhodoval o rozvržení v IE | interní příznak Tridentu, autor stylu ho nemůže nastavit přímo |
| S33 | **`zoom` spouští `hasLayout`** | **primární zdroj: Microsoft, [MS-CSS21] „The hasLayout Property Triggers and Resets"** — tabulka uvádí `zoom`, trigger `any`, reset `normal` |
| S34 | IE6 neuměl **alfa průhlednost PNG** | Wikipedia IE6: *„IE6 lacks support for alpha transparency in PNG images, replacing transparent pixels with a solid colour background"* |
| S34 | `select` se kreslil nad absolutně pozicovanými prvky **bez ohledu na `z-index`** | `select` je **windowed control** z operačního systému a kreslí se do jiné roviny než windowless elementy; `z-index` roviny nepropojí. Obcházelo se to iframe shimem |
| S37 | zalomení řádku v markupu udělá mezeru mezi obrázky | ✅ (ale není to vada IE — viz oprava 1) |
| S39 | conditional comments | microsoftí rozšíření; **odstraněno v IE10** |
| S42, S44 | jeden pád shodil celý prohlížeč se všemi okny | v IE7 a starších *„a single access violation … will cause your entire browser, and all its tabs, to crash"*; izolaci záložek přinesl až **IE8 s LCIE (beta 5. 3. 2008)** |
| S51 | jQuery byla jedna z nejdůležitějších knihoven schovávajících rozdíly | vytvořil **John Resig, leden 2006**; v roce 2019 na **80 % z milionu nejnavštěvovanějších webů** |
| S53 | jQuery schovala různé implementace AJAXu | v IE6 se XHR dělalo přes `ActiveXObject("Microsoft.XMLHTTP")`, jinde nativním `XMLHttpRequest` |
| S58 | Video, Audio, Canvas, SVG, WebGL, WebSockets, WebRTC v prohlížeči | ✅ WebRTC je z roku 2011+, proto ve scénáři *„and eventually"* |
| S60 | Silverlight = **C#, .NET, XAML** | rozhraní se deklaruje v XAML a programuje podmnožinou .NET; od verze 2 v libovolném .NET jazyce |
| S61 | **Apple odmítl Flash na iPhonu** | iPhone (2007) Flash nikdy neměl; Steve Jobs to veřejně zdůvodnil v *Thoughts on Flash*, **29. 4. 2010** |
| S62 | Silverlight, Flash, ActiveX i IE zmizely | Silverlight: podpora ukončena **12. 10. 2021**; Flash: konec **31. 12. 2020**; IE11 desktop **15. 6. 2022** |
| S70, S71 | Chrome, Edge, Opera, Brave, Vivaldi — mnoho z nich na Chromiu | ✅ všech pět je na Chromiu |
| S75 | Firefox má vlastní engine, Safari WebKit, Chromium je open source | Gecko / WebKit ✅; Chromium je svobodný software (BSD-3 pro kód Googlu, k tomu LGPL, MIT, Ms-PL, MPL po WebKitu) |
| S76 | moderní prohlížeče se aktualizují samy | ✅ |

---

## Co se NEDÁ ověřit a je to v pořádku

Video má několik míst, která nejsou tvrzení o světě, nýbrž **hodnocení nebo
scénka**, a fact check na ně nepatří:

- S43 — kancelářský vtip s odkazem („a dvacet oken zmizí"). Ilustrace, ne
  statistika. Že jeden pád shodil všechna okna, doloženo je (S42).
- S45 — *„Here's the keys to the building."* Metafora.
- S47–S49 — firma s pěti sty zaměstnanci. Modelový příklad, ne případová studie.
- S66–S69 — *„So was Microsoft the villain? Not really."* Autorský soud, a je
  jako soud i formulovaný.
- S72 — *„One engine everyone builds on."* Chromium **nemá** monopol jako
  kdysi IE: Firefox i Safari mají vlastní engine a scénář to sám vzápětí
  přiznává v S75. Věta je tedy položená jako otázka (*„Does that sound
  familiar?"*), ne jako tvrzení o podílech — **a tak musí zůstat i v obraze.**

---

## Nepoužité, ale doložené — materiál pro komentáře

- **XMLHttpRequest vynalezl Microsoft.** V IE5 (1999) jako ActiveX komponentu
  `Microsoft.XMLHTTP`; ostatní prohlížeče ho převzaly. Je to nejsilnější
  jednotlivý doklad teze videa („některé jeho nápady byly vlastně dobré")
  a ve v0.3 se to škrtlo se závěrečným výčtem.
- **IE Mode žije dál.** Internet Explorer jako aplikace skončil 15. 6. 2022,
  ale režim IE v Edge je podporovaný **nejméně do roku 2029**. Na větu
  *„Internet Explorer eventually disappeared too"* to nemá vliv (zmizela
  aplikace), ale v komentářích to někdo zmíní.
- **Blink se oddělil od WebKitu v roce 2013**, takže „Chromium engine" a
  „WebKit" dnes nejsou totéž — což je zrovna ta věc, která dělá S75 pravdivým.
