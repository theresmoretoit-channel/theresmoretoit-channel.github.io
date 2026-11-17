# Fact check — 039 IE6: The Browser That Wouldn't Die

Návrh 0.1 (`script 0.1.md`), **126 scén**. Ověřeno 2026-09-10.
Ověřeny všechny ověřitelné výroky, ne jen ta pět míst, která zadání
označilo za riziková — riziko se pozná až po ověření.

Kde se dá, přebírá se ověření z `028/factcheck.md` a `017/factcheck.md`,
aby se totéž nedokládalo dvakrát.

---

## 🔴 0. Není to fakt, ale největší nález: dvacet scén už je v díle 2

Tohle nenajde žádné ověřování faktů, protože všechna ta fakta jsou
**správná** — jen už jednou zazněla. A nejsou to okrajové scény, je to
**finále dílu 2** (jeho S74–S80 ze 83).

| návrh | co v něm je | kde už to je v 028 |
|---|---|---|
| S51–S53 | Google 2010 přestává podporovat IE6 | **S76** |
| S55–S58 | pohřeb v Denveru, rakev, eulogie, 80–100 lidí místo třiceti | **S76–S77** |
| S63–S67 | countdown, 12 %, cíl pod 1 %, „death clock for its own product" | **S79–S80** |
| S21–S27, S72–S77 | firemní aplikace, kterou nikdo nenapsal, a v pondělí musí fungovat | **S74–S75** |

Doslovnost je místy úplná: 028 má *„Between eighty and a hundred people
came… They had planned for thirty."*, návrh má *„The organisers had
expected about thirty. Between eighty and a hundred showed up."*
A 028 S80 má *„The company that built the browser was running a public
countdown to its own product's death."*, návrh S67 *„Microsoft was running
a death clock for its own product."*

Novinka v tom bloku je **jedna**: květiny od Microsoftu (S59–S60).
Ty v díle 2 nejsou.

**Dopad na stopáž:** těch 16 scén (S51–S67 bez S54) je **1:23**.
Bez nich má návrh 110 scén a **13:12** místo 14:35.

**Dopad na oblouk je ale větší než na stopáž.** Pohřeb a countdown jsou
v díle 2 *výplata* — přijdou po tezi „bugy měly jména, protože jsi kolem
nich žil". Tady by přišly podruhé jako kulisa, uprostřed videa, a divák,
který díl 2 viděl, na nich pozná, že se vypráví to samé. Divák, který ho
neviděl, zase nedostane nic, o co by přišel.

---

## 🔴 1. Jádro narativu — „XP = IE6" — je věcně špatně, a podráží to pointu

Návrh to tvrdí na třech místech:

- S28 *„Windows XP kept shipping. IE6 stayed there."*
- S73–S74 *„that machine was still running Windows XP. Still running IE6."*
- S86 *„when Microsoft finally ended support for Windows XP in two thousand
  and fourteen, one of the biggest reasons for keeping IE6 alive
  disappeared with it."*

**Ověření:**

| verze | vyšla | běžela na XP? |
|---|---|---|
| IE6 | 24. 8. 2001 | ✅ součást XP RTM |
| **IE7** | **18. 10. 2006** | ✅ **ano**, XP SP2 a výš |
| **IE8** | **19. 3. 2009** | ✅ **ano**, poslední verze pro XP |
| IE9 | 14. 3. 2011 | ❌ vyžaduje Vista SP2 a výš |

Windows XP tedy **nikdy nebyl důvod držet IE6**. Od října 2006 šlo mít
XP a IE7, od března 2009 XP a IE8 — a od ledna 2012 to Microsoft dělal
strojům sám (viz bod 5). Stroj na XP zaseknutý na IE6 tam nebyl kvůli
operačnímu systému, ale kvůli **té aplikaci**.

**A to je přesně teze videa.** Věta S86 dává příčinu operačnímu systému,
zatímco celé video chce ukázat, že příčinou byla závislost. Je to
ojedinělý případ, kdy věcná chyba a slabé místo scénáře jsou totéž místo:
opravou tvrzení oblouk **zesílí**.

Doložený tvar toho konce je jiný a lepší: **v USA byl IE6 pod jedním
procentem už v lednu 2012**, tedy **dva roky před koncem podpory XP.**
Deadline z S86 přišel, když už bylo rozhodnuto.

---

## 🔴 2. S07 — „more than ninety percent of the market" je o IE, ne o IE6

**Ověření** (přebírá se z `017/factcheck.md`, S09 a S26): vrchol **95,4 %
v červenci 2003** patří **všem verzím IE**. Samotné IE6 bylo v letech
2002–03 „high 80s" a **~90 % dosáhlo v polovině 2004**.

Ve scéně to číslo stojí u věty *„a pak v podstatě přestal"*, tedy v roce
2001–2002, kdy IE6 devadesát procent ještě neměl — teprve rostl.

**Závěr:** nechat to o Internet Exploreru jako celku (*„Internet Explorer
had more than ninety percent"*), ne o šestce. Jinak je číslo o dva roky
předsazené.

---

## 🟡 3. S32–S33 — „part of Windows" je pravda, ale nevysvětluje, co má

*„It was part of Windows… You were replacing part of the operating
system."* — jako popis **odinstalace** to platí (Trident používal shell,
HTML Help, Outlook). Jako vysvětlení, proč se nešlo posunout, to neplatí:
upgrade na IE7/IE8 byl normální podporovaná cesta přes Windows Update.

**Doložený mechanismus, který tam patří místo toho, je ostřejší:**
Microsoft vydal **IE7 Blocker Toolkit** — oficiální nástroj, kterým firma
zablokovala doručení IE7 přes Automatic Updates (klíč
`HKLM\…\Internet Explorer\Setup\7.0`, hodnota `DoNotAllowIE70`).
Bez data expirace. Totéž pak pro IE8, IE9 a IE11.

To je doklad věty S28 *„And Microsoft made that surprisingly easy"*,
zatímco „XP kept shipping" doklad není. Microsoft nejen že upgrade
nevynucoval — **dodal nástroj, jak ho nedostat.**

---

## 🟡 4. S59–S60 — citace na kartičce je „IE6", ne „Internet Explorer six"

**Ověření:** Microsoft poslal na pohřeb kytici s kartou
**„Thanks for the good times, IE6."** (Aten Design Group, Denver,
4. 3. 2010; CNN, Computerworld.)

Návrh cituje *„Thanks for the good times, Internet Explorer six."*
V citaci se text měnit nesmí. Kanál přitom vypisuje čísla slovy kvůli
TTS, takže to má jediné čisté řešení: napsat **„I E six"** a nechat to
citací, nebo scénu přeformulovat tak, aby to citace nebyla.

---

## 🟡 5. S48 — „started pushing users" má datum a je to konkrétní krok

**Ověření:** **15. 12. 2011** Microsoft oznámil, že bude Internet Explorer
**automaticky** upgradovat na nejvyšší verzi dostupnou pro daný systém.
Od ledna 2012: XP s IE6 nebo IE7 → **IE8**. Opt-out zůstal (komu se IE8
či IE9 dřív odmítl, ten ho nedostal) a šlo to odinstalovat.

Ve spojení s bodem 1 to dává skutečný konec IE6: **auto-upgrade 2012**,
ne konec XP 2014.

---

## 🟡 6. S51 — Google 2010 platí, ale chybí mu příčina, a ta je doložená

Ověření z `028/factcheck.md` (S76) platí dál: Rajen Sheth oznámil
v **lednu 2010**, že od **1. 3. 2010** přestanou **Google Docs a Google
Sites** v IE6 správně fungovat. Nešlo o konec podpory napříč Googlem —
návrh to formuluje správně (*„some of its applications"*).

Co v návrhu není: **proč zrovna tehdy.**

- **14. 1. 2010** — McAfee pojmenuje **Operation Aurora**: útok na Google
  a nejméně dvacet dalších firem vstupní branou přes **zero-day v Internet
  Exploreru**, exploit použitý při útoku míří na **IE6**.
- **Leden 2010** — německý **BSI** a francouzský **CERTA** doporučí
  občanům Internet Explorer nepoužívat a přejít na jiný prohlížeč.
  V Německu si za víkend po tom lidé stáhli přes **300 000** Firefoxů.
- **1. 3. 2010** — Google vypíná IE6 v Docs a Sites.
- **4. 3. 2010** — pohřeb v Denveru.

Ta zranitelnost byla ve IE6, 7 i 8; útok šel přes IE6. **Tohle je jediné
místo celého příběhu, kde má „zbavit se IE6" tvrdou příčinu, a ne jen
únavu vývojářů** — a rok 2010 přestane vypadat jako náhoda.

---

## 🟡 7. S86 — „konec podpory XP" je konec ZÁPLAT, ne konec stroje

**Ověření:** 8. 4. 2014 přestal Microsoft vydávat bezpečnostní záplaty
pro Windows XP (a tím i pro IE6 a IE8 na XP). Stroje fungovaly dál,
nic se nevypnulo.

A Microsoft si tu čáru sám hned porušil: **1. 5. 2014** vydal
mimořádnou záplatu na **CVE-2014-1776** (IE6 až IE11) **včetně Windows XP**,
s odůvodněním „based on the proximity to the end of support".

Návrh to naštěstí říká opatrně (*„Not all at once. Not everywhere."*).
Ta opatrnost je správná a má zůstat.

**Doložené dva doklady, které z konce XP dělají scénu, a nejsou v návrhu:**

- **Britská vláda zaplatila Microsoftu £5,584 mil.** za dvanáct měsíců
  prodloužené podpory XP pro celý veřejný sektor. V září 2013 běželo na XP
  **85 % z přibližně 800 000 počítačů NHS**.
- **Jižní Korea**: zákon vynucoval na bankovních a státních webech
  ActiveX, tedy Internet Explorer. Povinnou instalaci bezpečnostních
  programů vláda zrušila teprve **6. 10. 2014**, a weby u ActiveX zůstaly
  i po tom.

Druhý bod je odpověď na *„ActiveX v enterprise"* ze zadání: nejlepší
dostupný doklad není hypotetická firma, ale **stát, který si závislost
předepsal zákonem**.

---

## 🟡 8. S64 — „country by country" volá po čísle, které tam není

12 % celosvětově při spuštění countdownu (4. 3. 2011) je ověřeno
v `028/factcheck.md`. Ale scéna slibuje rozpad po zemích, a ten je
mnohem výmluvnější:

| | IE6 |
|---|---|
| **Čína, březen 2011** | **34,5 %** |
| Čína, konec 2011 | přes 25 % |
| Čína, 2012 | ~15 % |
| **USA, leden 2012** | **pod 1 %** |
| svět, srpen 2015 | pod 1 % všude kromě Číny (3,1 %) |

Ve stejném měsíci tedy jedna zem měla dvaatřicetkrát vyšší podíl než
druhá. To je ta „závislost" viditelná na mapě.

---

## ✅ Ověřeno v pořádku

> Čísla scén v celé první části jsou z **0.1** (`script 0.1.md`, 126 scén).
> Mapování na hotovou 0.2 je v tabulce níž, v části „Verze 0.2".

| scéna | tvrzení | doklad |
|---|---|---|
| S02 | IE6 vydán 2001, Windows XP přišel s ním | IE6 **24. 8. 2001**, XP **25. 10. 2001**, IE6 součástí XP RTM. IE6 byl **dřív** — „arrived with it" projde, simultánnost netvrdit |
| S02 | za pár let ovládl většinu webu | IE celkem 95,4 % (7/2003) |
| S06, S13 | po IE6 dlouho žádná nová verze; IE7 v roce 2006 | 24. 8. 2001 → 18. 10. 2006, **pět let a dva měsíce** |
| S14 | IE7 měl panely, lepší bezpečnost, nové rozhraní | doloženo; „engine that had finally moved forward" je hraniční, viz níž |
| S09 | Firefox 2004 | Firefox 1.0 **9. 11. 2004** |
| S40 | Chrome 2008 | beta pro Windows **2. 9. 2008**; scénář uvádí jen rok |
| S41 | Chrome se aktualizoval sám | automatický updater od první verze |
| S55–S58 | pohřeb: Denver, rakev, eulogie, 30 → 80–100 | Aten Design Group, **4. 3. 2010** (ověřeno v 028) |
| S63–S65 | countdown rok po pohřbu, 12 %, cíl pod 1 % | `ie6countdown.com` **4. 3. 2011**, tedy **přesně rok po pohřbu** (ověřeno v 028) |
| S80 | hasLayout, podmíněné komentáře, filtry, ActiveX, detekce prohlížeče | vše ověřeno v `028/factcheck.md` |
| S86 | Windows XP měl datum konce | **8. 4. 2014** |
| S115 | prohlížeč z roku 2001 strašil web přes dekádu | podpora IE6 skončila úplně **12. 1. 2016**, tedy po **čtrnácti letech** |

> **S14 „finally moved forward":** IE7 přinesl méně, než se čekalo, a byl
> za to kritizován. Tvrzení „konečně se pohnul" je obhajitelné, ale
> silnější, než co IE7 doopravdy udělal. Zmírnit na „had moved forward
> at all" nebo doplnit čím.

---

## Co v návrhu chybí a je doložené

Teze *„IE6 přežil, protože na něm bylo příliš mnoho věcí závislých"*ٍ je
správná. Návrh ji ale **dokládá fikcí**: *„Imagine an internal application
built in two thousand and two"* (S21), *„Maybe nobody remembers who wrote
it"* (S22), *„somewhere, there was still a warehouse. A hospital"* (S72).
Ani jeden skutečný případ ve 126 scénách.

To je proti tomu, co si díl 2 vydobyl: **každá položka je doklad, ne
položka seznamu.** A doklady tady existují, jsou lepší než ta fikce
a jeden je dokonce absurdnější:

| doklad | proč zesiluje právě tuhle tezi |
|---|---|
| **MED-V** (Microsoft Enterprise Desktop Virtualization, MDOP) | Microsoft **prodával produkt**, který spouští IE6 ve virtuálním XP uvnitř Windows 7, a MED-V 2.0 umí **přesměrovat konkrétní adresy do IE6**. Táž firma tedy zároveň běží veřejný odpočet ke smrti svého prohlížeče a dodává mu dýchací přístroj |
| **Enterprise Mode v IE11** (2014) | nový prohlížeč **emuluje IE7 a IE8**, aby staré weby a ActiveX „just work". Závislost zabudovaná do produktu, ne obejitá |
| **Blocker Toolkit** (IE7, 8, 9, 11) | oficiální nástroj Microsoftu, jak novou verzi **nedostat** |
| **Jižní Korea** | závislost předepsaná zákonem, rušená až 2014 |
| **NHS / britská vláda** | £5,584 mil. za jeden rok odkladu; 85 % z 800 000 počítačů |
| **Čína 34,5 % vs. USA pod 1 %** | tatáž doba, tentýž web, třicetidvojnásobný rozdíl |
| **Aurora + BSI a CERTA** (leden 2010) | jediná tvrdá příčina v celém příběhu; dává roku 2010 smysl |

První tři jsou navíc **novinky proti dílům 1 a 2** a nesou přesně tu
gradaci ze zadání: *dependency → infrastructure*. MED-V je její doslovná
podoba — infrastruktura, kterou se někdo bojí vypnout, dodávaná
v předplatném.

---

## Stopáž — měřeno, ne odhadnuto

Podle metodiky z `CLAUDE.md` (250 slabik za minutu **řeči**, pauzy zvlášť):

| | |
|---|---|
| scén | **126** |
| slov / slabik | 2 005 / 3 220 |
| řeč | **12:53** |
| + `scene_pause` 0,8 u všech scén | **14:35** |
| + blokové pauzy jako u 028 (+28 s) | **15:03** |
| bez šestnácti scén z bodu 0 | **13:12** |

Odhad 14–16 minut ze zadání tedy sedí. Dvě věci k tomu:

**Rytmus je sekanější než u dílu 2.** Medián scény je **6,1 s** (5,3 s
řeči + pauza), tedy na spodní hranici pravidla „scéna 6–12 s".
**43 scén ze 126 (34 %) má pod čtyři sekundy.** Díl 2 má na 13:10 jen
83 scén, tedy medián kolem 9,5 s. Verze 0.1 dílu 2 měla medián 4,1 s
a bylo to označeno za AI-slop rytmus; tenhle návrh je mezi tím.

Krátká scéna jako beat je v pořádku (*„Its reach."*, S101). Třiačtyřicet
z nich už není beat, ale rytmus — a scény se slepují snadněji než píše.

**Devět scén přesahuje 12 s** (S21, S25, S45, S72, S80, S99…) a ty naopak
volají po rozdělení, ne po zkrácení.

---

## Zdroje

- Wikipedie — Internet Explorer 6, 7, 8, 9; Web compatibility issues in South Korea
- Microsoft Learn — Blocker Toolkit (IE7/8/9/11), Overview of MED-V, Enterprise Mode for IE11
- Microsoft Blog, 15. 12. 2011 — automatický upgrade IE; TechCrunch k témuž
- McAfee / The Register / NBC News, leden 2010 — Operation Aurora, zero-day v IE
- IEEE Spectrum, Computerworld, Wikinews, blog.mozilla.org — BSI a CERTA, leden 2010
- CNN, Computerworld, Flickr (Aten Design Group), 4. 3. 2010 — pohřeb a květiny
- TechSpot, FlowingData, LiveSide, QuirksBlog — `ie6countdown.com`, Čína, USA
- Computer Weekly, The Register, Graham Cluley, 2014 — £5,584 mil. za podporu XP
- The Hacker News, Threatpost, The Register, květen 2014 — CVE-2014-1776 i pro XP
- Seattle Times, Techdirt, palant.info — ActiveX a zákon v Jižní Koreji
- `videos/017/factcheck.md`, `videos/028/factcheck.md` — podíly na trhu, datum IE6,
  Google 2010, pohřeb, countdown

---

# Verze 0.2 — přepsáno 2026-09-10

`script 0.2.md`, **97 scén**, měřeno **13:40**. Čísla scén níž jsou z 0.2.

Z 0.1 se vyhodil celý blok pohřbu a odpočtu (bod 0), narativ „XP = IE6"
se přepsal na „operační systém nebyl důvod, aplikace byla" (bod 1),
a hypotetická firma se nahradila doklady (MED-V, Blocker Toolkit, Korea,
NHS, Čína). Nová tvrzení, která tím vznikla, jsou ověřená takto:

| scéna | tvrzení | doklad |
|---|---|---|
| S03 | veřejný odpočet na webu Microsoftu, po zemích | `ie6countdown.com` od 4. 3. 2011 (ověřeno v `028/factcheck.md`) — v 0.2 už jen **premisa hooku, jednou větou**, ne blok |
| S10 | v lednu 2010 je víc než jeden prohlížeč z deseti pořád IE6 | únor 2010: **10–20 %** celosvětově. „více než jeden z deseti" je konzervativní konec pásma |
| S11–S13 | Google našel útočníka ve vlastní síti; zdrojový kód, účty, Gmaily čínských aktivistů; **nejméně dvacet** dalších firem | Google (12. 1. 2010), McAfee, The Register |
| S14 | vstupní branou byla neopravená chyba v IE, útok jí šel na **IE6** | McAfee, 14. 1. 2010; **CVE-2010-0249** |
| S15 | jméno Aurora dali výzkumníci, kteří útok rozebrali | McAfee (název podle cesty v malwaru) |
| S15 | Microsoft **porušil vlastní měsíční cyklus** a vydal opravu **tři týdny předem** | **MS10-002**, mimo cyklus **21. 1. 2010**; řádný termín byl druhé únorové úterý. Opravila osm zranitelností v IE6, 7 i 8 |
| S17 | německý spolkový úřad i Francie doporučily jiný prohlížeč | **BSI** a **CERTA**, leden 2010 |
| S18 | v Německu tři sta tisíc stažení Firefoxu za jeden víkend | blog.mozilla.org, 19. 1. 2010 (pátek až pondělí) |
| S19 | pár týdnů po Auroře: od **1. března** nefungují Google Docs a Google Sites v IE6 | Google to oznámil **29. 1. 2010** (Rajen Sheth; TechCrunch téhož dne), účinnost **1. 3. 2010**. Od Aurory (14. 1.) je to k oznámení dva týdny a k účinnosti sedm — proto **„A few weeks later"**, ne „six weeks" |
| S23 | IE7 vyšel 2006 a běžel na Windows XP | **18. 10. 2006**, požadavek XP SP2 |
| S24 | IE8 vyšel 2009 a běžel na XP taky | **19. 3. 2009**, poslední verze pro XP |
| S24 | IE9 (2011) na XP už neběžel vůbec | **14. 3. 2011**, vyžaduje Vista SP2; XP tím zůstal zaseknutý na osmičce |
| S25 | Microsoft rozeslal IE7 přes Windows Update jako **kritickou** aktualizaci | od **1. 11. 2006** přes Automatic Updates |
| S37–S39 | Microsoft vydal nástroj, který zabrání instalaci jeho vlastního nového prohlížeče, a **bez data expirace** | **IE7 Blocker Toolkit**; klíč `HKLM\…\Internet Explorer\Setup\7.0`, hodnota `DoNotAllowIE70`. Blokuje jen automatické doručení, ruční instalace zůstala možná |
| S40–S41 | totéž pro osmičku, devítku a jedenáctku, tedy čtyřikrát | Blocker Toolkit pro IE8, IE9, IE11 (Microsoft Download Center) |
| S44–S45 | po roce 2009 znamenal nový stroj Windows 7, na kterém IE6 neběžel | Windows 7 **22. 10. 2009**; IE6 podporoval nejvýš XP a Server 2003 |
| S48 | jmenuje se Microsoft Enterprise Desktop Virtualization a velké firmy si ho kupovaly v předplatném | MED-V, součást **MDOP** (Microsoft Desktop Optimization Pack) |
| S49–S50 | spustí celou kopii Windows XP uvnitř Windows 7 a v ní IE6 | MED-V nad Windows Virtual PC; „XP Mode s manageovatelností" |
| S51–S52 | druhá verze umí seznam adres, které se otevřou ve starém prohlížeči, a uživatel to nepozná | **MED-V 2.0**: přesměrování legacy webových aplikací podle domény a portu; aplikace se uživateli jeví jako běžné aplikace Windows 7 |
| S56 | o několik let později přinesl IE11 **režimy kompatibility** pro starší weby, z nichž jeden se choval jako IE8 | **Enterprise Mode**, IE11 (2013), režim dodán 2014; emulace IE7 a IE8 včetně user-agent stringu. Formulace „a mode that pretended to be Internet Explorer eight" byla ve 0.2 **zpřesněna** — IE11 v sobě neměl celý IE8, měl režim kompatibility |
| S56b | byl tam kvůli starým interním aplikacím a jejich ActiveX prvkům; Microsoftova dokumentace psala, že mnohé z nich budou dál fungovat | přesné znění je *„customers report that **many** of these ActiveX controls **just work** in Enterprise Mode"* — tedy **many**, a jako zpráva od zákazníků. Scénář to má zmírněné na „many of those" |
| S60–S61 | korejské předpisy z konce devadesátých let vyžadovaly u online plateb šifrování, které neumožňoval žádný prohlížeč, takže se přidalo přes ActiveX | vlastní šifra **SEED** (1999), důsledek amerických exportních omezení na silnou kryptografii; ActiveX byl jediná cesta, jak ji do prohlížeče dostat |
| S62–S63 | bankovnictví, státní weby i nakupování stály na ActiveX, tedy na jednom prohlížeči, a to z předpisu | Wikipedie „Web compatibility issues in South Korea", Seattle Times, Techdirt, palant.info |
| S64 | povinnost padla v roce 2014, pluginy na webech zůstaly | **6. 10. 2014** vláda zrušila povinnou instalaci bezpečnostních programů; weby ActiveX používaly dál |
| S66 | v lednu 2012 spadl IE6 v USA pod jedno procento | StatCounter / siliconfilter, leden 2012 |
| S67 | téže zimy byla v Číně čtvrtina prohlížečů pořád IE6, a na jaře před tím třetina | konec 2011 **přes 25 %**; **34,5 %** v březnu 2011 podle `ie6countdown.com` |
| S69 | v září 2013 běželo 85 % počítačů britské NHS na Windows XP | Computer Weekly, The Register |
| S70 | z přibližně osmi set tisíc strojů | ~**800 000** PC v NHS |
| S72 | britská vláda podepsala s Microsoftem smlouvu na pět a půl milionu liber za dalších dvanáct měsíců záplat pro celý veřejný sektor | **£5,584 mil.**, Crown Commercial Service, 2014 |
| S79–S80 | v prosinci 2011 Microsoft oznámil, že se přestane ptát, a bude IE upgradovat sám na nejvyšší verzi, kterou stroj unese; na XP tedy na osmičku | **15. 12. 2011**, spuštěno v lednu 2012 |
| S81 | odmítnout to pořád šlo | kdo dřív odmítl IE8 nebo IE9, ten automatický upgrade nedostal; aktualizaci šlo odinstalovat |
| S83 | podpora XP skončila v dubnu 2014, jak bylo slíbeno, dva roky po tom, co prohlížeč prohrál | **8. 4. 2014** |
| S84 | tři týdny po tom se našla vážná chyba a Microsoft ji na XP přesto zazáplatoval | **CVE-2014-1776**, mimořádná záplata **1. 5. 2014** i pro XP včetně Embedded, „based on the proximity to the end of support" |
| S85 | IE6 dostával bezpečnostní záplaty někde na světě až do ledna 2016, čtrnáct let po vydání | podpora IE6 skončila **12. 1. 2016** (XP Embedded); 24. 8. 2001 → 1/2016 je **14 let** |
| S86 | Internet Explorer sám byl vypnutý v červnu 2022 | IE11 desktop **15. 6. 2022** (ověřeno i v `017/factcheck.md`) |
| S87 | Edge pořád nese režim, který kreslí stránky jako Internet Explorer, a Microsoft slíbil, že bude fungovat **aspoň do roku 2029** | Microsoft Learn, Lifecycle FAQ: IE mode „supported through **at least 2029**", s ročním předstihem oznámení o ukončení. **Nuance:** IE mode používá engine **Trident/MSHTML z IE11**, ne z IE6. Věta *„a mode that draws pages the way Internet Explorer did"* je vypravěčská zkratka a je **záměrně obecná** — a pointu to spíš posiluje: IE6 nemusí doslova běžet, aby jeho odkaz přežíval |
| S88 | dvacet osm let po vydání prohlížeče, devatenáct let po tom, co byl vyhlášen za mrtvý | 2029 − 2001 = **28**; 2029 − 2010 = **19** |

## Co ve 0.2 zůstává k rozhodnutí

- **S19 „six weeks later"** — od Aurory (14. 1.) k účinnosti (1. 3.) je sedm
  týdnů, od Googlova oznámení (leden) k účinnosti šest. Věta je pravdivá
  k oznámení, ale divák si ji spojí s datem útoku. Buď „a few weeks later",
  nebo přesné datum.
- **`pronounce` v `project.json`** — fonémy ověřeny přes `kokoro_onnx`:
  `ActiveX` → `ˈaktɪv ˈɛks`, `Windows XP` → `wˈɪndəʊz ˌɛkspˈiː`,
  `Virtualization` → `vˌɜːtʃuːəlaɪzˈeɪʃən`, `Gmail` → `dʒˈiːmˈeɪl`,
  `Aurora` → `ɐɹˈɔːɹə`. **Žádné z nich `pronounce` nepotřebuje.**
- **Homografy** projeté: `used` (S14, sloveso), `use` (S17, S60, infinitiv
  a rozkaz) jsou v pořádku. `contract` a `refuse` byly preventivně
  přeformulovány na `deal` a `say no`.
- **Slabikovač počítá `XP` jako jednu slabiku**, Kokoro jako dvě; jedenáct
  výskytů, tedy asi +2 s proti odhadu. Do stopáže se to nepřepisovalo.

## LOCK 0.2 (2026-09-10)

Recenzent scénář prošel celý a řekl **LOCK** se dvěma změnami, obě
zapracované:

| | |
|---|---|
| **S19** | *„Six weeks later"* → **„A few weeks later"**. Google oznámil konec podpory 29. 1. 2010, účinnost 1. 3. 2010; „six weeks" se vázalo na oznámení, ale divák si to spojí s datem útoku |
| **S56** | *„a mode that pretended to be Internet Explorer eight"* → **„compatibility modes for older sites, one of them behaving like Internet Explorer eight"**. Obsahově to bylo správně, ale IE11 neobsahoval celý IE8 |

Scéna S56 tím narostla na 22 s, proto je rozdělená na **S56 a S56b**
(12,0 a 10,3 s). Písmenné číslování znamená, že se **nepřečísloval zbytek
videa** ani jediný odkaz v tomhle fact checku.

**Stav po zapracování:** 97 scén, měřeno **13:40**, medián scény **8,2 s**,
žádná scéna nad 14 s, žádný řádek nad 42 znaků.
