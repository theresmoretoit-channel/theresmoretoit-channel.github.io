# 053 — fact check

Ověřeno 2026-09-17 proti `script 0.4.md`. Podklad a odkazy jsou
v `bugy-doklady.md`.

**Primární zdroj je `learn.microsoft.com/windows/release-health`** —
Microsoft tam vede vlastní seznam známých problémů s číslem KB, datem
otevření a stavem. Kde je uvedený, je tvrzení doložené tím, že chybu
přiznal sám výrobce.

| | |
|---|---|
| ověřitelných tvrzení | **31** |
| prošlo beze změny | 29 |
| **opraveno ve scénáři** | **1** (S33) |
| vedeno jako úvaha, ne fakt | 1 (S98–S99) |

> **Doplněno po zpětné vazbě (script 0.5):** ověřen znovu blok S36–S39
> (ptal ses, jestli to tvrzení opravdu drží — drží, a líp než jak bylo
> původně zapsané) a přibyly čtyři scény o uniklém zdrojáku.

---

## Zářijová vlna 2026 (S01–S04)

> *„In September 2026, a single batch of Windows updates broke four
> things at once."* … *„One batch. One Tuesday."*

| co scénář tvrdí | doklad | |
|---|---|---|
| zvuk přestal fungovat | USB Audio Class 1.0, „This device cannot start (Code 10)", KB5122871, 8. 9. 2026 | ✅ |
| Remote Desktop přestal fungovat | RDS nestabilní, RDP padá po několika minutách, KB5122871 | ✅ |
| sdílené složky ve virtuálech | Plan9 sdílení z hosta do linuxových VM, KB5124008 | ✅ |
| počítače přestaly věřit doménové síti a lidé se nepřihlásili | účty chráněné Credential Guardem ztratí secure channel k AD; *„unable to sign in interactively with valid domain credentials"*, KB5124008 | ✅ |
| **„One Tuesday"** | oba KB vyšly **8. 9. 2026**, a ten den **byl úterý** (ověřeno výpočtem) | ✅ |

> **Formulace je přesná právě proto, že říká „updates" v množném
> čísle.** Jsou to dva kumulativní balíky pro různé verze Windows,
> vydané týž patch Tuesday. „A single update" by pravda nebyla.

---

## Kurzor (S11–S13)

| tvrzení | doklad | |
|---|---|---|
| update měnil věci kolem lišty | KB5120998, 27. 8. 2026, vylepšení Start menu, lišty a vyhledávání | ✅ |
| Microsoft krátce nato problém přiznal | v release health jako známý problém | ✅ |
| vlastní kurzor se vrátí na velkou bílou šipku | *„high-DPI mouse cursors are replaced with larger, white cursors"* | ✅ |
| vrátit to zpátky nešlo | *„Attempts to restore the previous cursor customization are reported to be unsuccessful."* | ✅ |

---

## Rok opakovaných regresí (S28–S31)

Všechno jsou updaty roku **2025**, takže rámec *„a single year of that
list"* sedí.

| scénář | update | |
|---|---|---|
| leden: zvuková zařízení a webkamery | KB5050009 — USB DAC „Code 10", webkamery `0xA00F4244` | ✅ |
| únor: točící se kurzor, stroj vypadá zaseknutý | KB5050094 | ✅ |
| březen: modré obrazovky a uvízlé instalace | KB5053598 — BSOD, instalace stojí na 6 / 20 / 38 % | ✅ |
| duben: rozbité přihlašování obličejem | KB5055523 — Windows Hello selhává, IR kamery nefunkční | ⚠️ viz níž |
| květen: Průzkumník nereaguje na myš | KB5058411 | ✅ |
| říjen: rozbité spojení k vlastnímu počítači | KB5066835 — localhost (127.0.0.1) | ✅ |

> **⚠️ Duben je zjednodušený, ale ne nepravdivý.** Windows Hello
> selhávalo za určitých podmínek (zakrytá webkamera), ne vždy. Věta
> *„April broke the face recognition people use to log in"* je shrnutí,
> ne popis. Ponecháno — u výčtu o šesti položkách je to přiměřené.

> **Zdrojová opatrnost:** těchto šest položek pochází ze **souhrnného
> článku**, ne z primárního seznamu Microsoftu kus po kuse. Dvě
> nejnosnější (níž) jsem dohledal primárně. **Zobecnění z nich nedělej**
> — scénář to nedělá, mluví o konkrétních měsících, ne o „každém updatu".

---

## Dvě rozbité opravy (S33–S35) — punchline videa

| tvrzení | doklad | |
|---|---|---|
| jeden update rozbil tlačítko, co resetuje PC | **srpen 2025**, KB5063875 / KB5063709: „Reset this PC" se rozjede, restartuje a začne vracet změny, aniž dokončí. Mimořádná oprava KB5066189 (19. 8. 2025) | ✅ |
| druhý rozbil obrazovku obnovy | **říjen 2025**, KB5066835: v prostředí obnovy nefungují USB klávesnice a myši. Mimořádná oprava KB5070773 (20. 10. 2025) | ✅ |
| *„Twice in three months"* | 12. 8. → 14. 10. 2025 = **63 dní**, tři kalendářní měsíce | ✅ |

> ### ❌ OPRAVENO ve scénáři
>
> Stálo tam *„where the mouse and the keyboard stopped responding"*.
> Microsoft ale hlásí výslovně **USB** zařízení — Bluetooth a staré
> PS/2 fungovaly dál a byly uváděné jako náhradní řešení. Věta tedy
> tvrdila víc, než je pravda.
>
> Opraveno na **„where USB mice and keyboards stopped responding"**.
> Je to o slabiku delší a pointa se tím nemění.

---

## Týž bug dvakrát (S36–S39)

| tvrzení | doklad | |
|---|---|---|
| zvukový bug „device cannot start" byl v lednu | KB5050009, leden 2025 | ✅ |
| a znovu o **dvacet měsíců** později | KB5122871, září 2026 — **přesně 20 měsíců** (ověřeno výpočtem) | ✅ |
| stejný symptom, stejná hláška | obojí „This device cannot start (Code 10)" / zařízení se nerozběhne | ✅ |
| stejný typ zařízení | leden „USB DAC", září „USB Audio Class 1.0" — **obojí USB zvuk** | ✅ |

> Tohle je nejsilnější blok videa a **je doložený nejlíp ze všech**:
> obě strany má Microsoft ve vlastní evidenci.

### Přeověřeno 2026-09-18 — a vyšlo to SILNĚJI, než bylo zapsáno

Ptal ses, jestli to tvrzení opravdu drží. Drží, a shoda je těsnější:

| | leden 2025 | září 2026 |
|---|---|---|
| update | KB5050009 / KB5050021 / KB5049981 | KB5122871 |
| hláška | *„This device cannot start. (Code 10) Insufficient system resources exist to complete the API."* | *„This device cannot start (Code 10)"* |
| zařízení | externí DAC přes ovladač **USB Audio 1.0** | **USB Audio Class 1.0** |
| přiznal Microsoft | ✅ | ✅ (release health) |

**Je to tedy doslova táž třída zařízení** — původně jsem psal opatrně
„obojí USB zvuk", ale obě hlášení mluví konkrétně o USB Audio **1.0**.

> **Co scénář naopak NETVRDÍ a tvrdit nesmí: že je to týž bug.**
> U ledna Microsoft uvedl příčinu (nedostatek paměti pro DAC), u září
> příčinu nezveřejnil. Věta *„Same symptom. Same kind of device. Same
> message."* je proto přesná — a kdyby se při zkracování změnila na
> „the same bug came back", pravda by to nebyla.

---

## Historie (S41–S44)

| tvrzení | doklad | |
|---|---|---|
| update v 2024 zastavil zavádění Linuxu na dual-boot strojích | srpen 2024, SBAT proti CVE-2022-2601; Microsoft tvrdil, že se dual-bootu nedotkne, a dotklo | ✅ |
| hláška zněla *„Something has gone seriously wrong."* | plné znění: *„Verifying shim SBAT data failed: Security Policy Violation. **Something has gone seriously wrong:** SBAT self-check failed…"* — citovaná část je doslovná | ✅ |
| v 2018 se vydání muselo stáhnout celé poté, co lidé hlásili ztracené soubory | Windows 10 verze 1809, říjen 2018, staženo z Windows Update i Media Creation Tool; příčina Known Folder Redirection | ✅ |

> **Scénář záměrně NEŘÍKÁ, jak velký ten rozsah byl.** Microsoft uvádí
> zásah u **0,01 %** instalací. Věta *„after people reported that their
> files were gone"* je pravdivá a nic nezesiluje — **při dalším
> zkracování ji nepřepisuj na „mazal lidem soubory"**, to už by pravda
> nebylo.

---

## Microsoft mimo Windows (S48–S52)

| tvrzení | |
|---|---|
| Microsoft dělá Office, Visual Studio, Exchange, Teams a velký cloud | ✅ triviálně |
| všechno to mělo vlastní chyby, regrese a výpadky | ✅ výpadky Azure jsou veřejně dokumentované |
| moderní cloudová služba nenese třicet let kódu a **přesto padá** | ✅ argument, ne číslo; stojí na předchozím řádku |

---

## Architektura a jádro

| scéna | tvrzení | |
|---|---|---|
| S55 | *„At the bottom is an architecture that goes back to the early nineties."* | ✅ Windows NT 3.1 vyšlo v červenci 1993. **Opraveno v 0.3** z původního *„a core designed in the early nineties"*, které svádělo ke čtení, že jde o tentýž zdroják |
| S91 | NT → Windows 2000 → XP → Vista → 7, 8, 10, 11 | ✅ posloupnost NT sedí. Správně **nezahrnuje** 95/98/ME, což NT nebylo |
| S86, S105 | jádro rozhoduje, co běží na kterém jádru procesoru, přiděluje paměť, mluví s hardwarem | ✅ |
| S93 | *„ended up running servers all over the world"* | ✅ **zmírněno v 0.4** z *„an enormous amount of the world's server rooms"*, což by se muselo podložit číslem |
| S96 | zdrojový kód moderního Windows jádra si přečíst nemůžeme | ✅ veřejný není. Existují úniky a programy pro vybrané partnery a vlády, ale **ne běžná nezávislá kontrola** — což je přesně, co scénář říká |

### S98–S99 je ÚVAHA, ne fakt

> *„I'm not going to tell you that the Windows kernel is brilliant.
> We don't know that. But we do have decades of evidence that it is
> competent."*

Vedeno záměrně jako kalibrované tvrzení. **Nesmí se z něj při
zkracování stát „jádro je dobré"** — celý smysl té věty je, že
z dostupných dokladů plyne kompetence, ne genialita. Táž pojistka
je v S96 a S97.

---

## AI (S71–S80)

| tvrzení | doklad | |
|---|---|---|
| Microsoft čím dál víc používá AI při psaní softwaru | výrok generálního ředitele + veřejná strategie | ✅ |
| *„twenty to thirty per cent of the code in their repositories is now written by software"* | **Satya Nadella, LlamaCon, 29. 4. 2025**, rozhovor se Zuckerbergem: *„20 % to 30 % of code inside the company's repositories was written by software"* | ✅ doslova |
| *„That figure is Microsoft as a whole, not Windows in particular."* | ✅ Nadella mluvil o repozitářích celé firmy | ✅ |
| *„Nobody has shown that AI caused any of these bugs."* | ✅ žádný takový doklad neexistuje | ✅ |

> **Detail, který se do scénáře nevešel a stojí za zapamatování pro
> komentáře:** Nadella dodal, že to jde **líp u Pythonu než u C++**.
> Jádro Windows je v C a C++. Ten výrok tedy tlačí spíš **od** jádra
> než k němu — což videu argumentačně hraje do karet, ale je to
> odbočka a do scénáře jsem ji nedával.

> **Celá sekce je vedená jako otázka, ne obvinění**, a je to záměr.
> Tvrzení „AI způsobila tyhle regrese" doložit nejde a video ho
> nevyslovuje. Kdyby při dalším zkracování vypadla S78, vzniklo by —
> **neškrtat**.

---

## Co ve scénáři NENÍ a je to správně

- **Žádná čísla KB.** Nikdo je neposlouchá a v titulcích čtrnácti
  jazyků by byla šum. Evidence je v `bugy-doklady.md`.
- **Žádný počet inženýrů.** S70 říká jen *„an enormous number"* —
  Microsoft konkrétní číslo nezveřejňuje.
- **Žádné tvrzení o podílu Windows na serverech.** Viz S93.


---

## Uniklý zdrojový kód (S96b–S96e) — doplněno 2026-09-18

Vzniklo z tvé otázky, jestli někdo zkoumal uniklé zdrojáky starších
Windows a vydal hodnocení. **Ano, a je to čerstvé.**

| tvrzení ve scénáři | doklad | |
|---|---|---|
| část zdrojového kódu Windows 2000 unikla v roce 2004 | únik z února 2004; Microsoft ho potvrdil vlastním prohlášením. Uniklo **zhruba 15 %** stromu Windows 2000 (plus velká část NT 4.0), celkem kolem 13,5 milionu řádků | ✅ |
| „minulý rok se tím někdo probral" | audit publikoval **Matt Suiche, 19. 5. 2026** — systematický průchod uniklým stromem, křížově porovnaný s 25 lety zveřejněných zranitelností | ✅ |
| „nálezy nebyly lichotivé" | 45 kandidátů, **11 s vysokou jistotou** a konkrétní cestou útoku, **4 přímé shody s CVE**, 24 dotčených CVE z let 1999–2025 | ✅ |
| **„šestnáct let, než to někdo zaplátoval"** | autor uvádí střední dobu života **16,75 roku** | ✅ scénář zaokrouhluje DOLŮ na šestnáct, tedy nezveličuje |
| „je to prarodič dnešního jádra a uniklá jen část" | ✅ Windows 2000 je NT 5.0, dnešní jádro je o šest generací dál; uniklo ~15 % | ✅ |

> **S96e je POJISTKA a nesmí se škrtnout.** Bez ní by dvě předchozí
> scény tvrdily, že je dnešní jádro špatné — a to ten audit neříká
> ani nemůže. Proto je šipka mezi „Windows 2000" a „dnešní jádro"
> v obraze **čárkovaná**: usuzovat tím směrem nejde.

> **A druhá výhrada, kterou scénář nese sám:** audit je práce jednoho
> člověka (s pomocí AI agenta), ne recenzovaná studie. Scénář proto
> říká *„a researcher went through it"*, ne „bylo prokázáno".

**Proč to ve videu je, i když jde proti jeho tezi:** video tvrdí, že
na jádro nevidíme. Tohle je jediné místo, kde někdo dovnitř viděl —
vynechat to by znamenalo zamlčet nejbližší dostupný protiargument.
Zároveň to tezi nevyvrací: mluví o kódu z roku 2000.

### Odkazy

- audit: <https://www.msuiche.com/posts/from-y2k-to-patch-tuesday-2025-25-years-of-bugs-in-the-windows-2000-source-tree/>
- prohlášení Microsoftu k úniku: <https://news.microsoft.com/source/2004/02/12/statement-from-microsoft-regarding-illegal-posting-of-windows-2000-source-code/>
- leden 2025, DAC a Code 10: <https://www.theregister.com/2025/01/28/microsoft_admits_to_usb_digital/>
