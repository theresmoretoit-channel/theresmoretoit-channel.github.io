# 148 — fact check scénáře (v0.4, 2026-11-07)

✅ = doloženo přečteným primárním zněním, ⚠ = sekundární zdroj, zjednodušení nebo úsudek (zdůvodněno).

**Hlavní primární zdroj [OAI]:** OpenAI, *A thousand fewer paths to root*, 4. 11. 2026,
`https://openai.com/index/a-thousand-fewer-paths-to-root/`. Přímý přístup vrací 403, čteno ze snímku
`web.archive.org/web/20261106213507/…` celé.

## Opravy proti zdroji a tisku

| co se tvrdí | jak to je | důsledek |
|---|---|---|
| zdroj: QEMU dokazuje, že výzkum nepotřebuje zdrojový kód, rozdíl open/closed slábne | [OAI]: agent v běhu kernelCTF narazil na pád jádra a *„traced the issue to QEMU TCG, without access to QEMU's source code"*. Tedy **jeden** případ, náhodně, a QEMU je samo open source (model ho mohl znát z tréninku, to je můj úsudek); chyba *„had been fixed in upstream QEMU"* | vypuštěno, tvrzení nese S36–S39 |
| zdroj: 61 + 43 jako ukázka, jak funguje hlášení | [OAI, shrnutí]: *„patched or had staging patches **from other contributors**"* | S41–S46, jádro videa |
| zdroj: *thousands of distributions* | nepodložené, DistroWatch eviduje řádově stovky | vypuštěno |
| zdroj: malý projekt nemá na výpočetní výkon | Glasswing: *„maintainers get access to these tools for free"*, až 100 mil. USD v kreditech (Linux Foundation, 7. 4. 2026) | S49 |
| How-To Geek: běh trval ~30 hodin | 30 hodin je jen validace; objevování 12 hodin, sken a analýza celkem 10 dní | S15, S41 |
| Root.cz: 219 úniků informací, model GPT-5.6 Cyber; Phoronix: GPT-5.5 Cyber | [OAI]: **291** PoC, *„an upcoming cyber model"* bez jména | ve scénáři jen *newer model* |
| Tom's/tisk: srovnávání počtu CVE Linux vs. Microsoft | Kroah-Hartman: Apple, Microsoft a další hlásí jen vybrané, jádro všechno (Linuxiac) | S10: výslovně nesrovnáváme |

## Po scénách

| scéna | tvrzení | ověření | |
|---|---|---|---|
| S01–S02 | 948 různých LPE, z běžného uživatele root | [OAI]: *„948 local privilege escalation (LPE) exploits that could allow an unprivileged local user to gain root access"*. „Separate" = 948 různých záplat, kterými OpenAI počet určuje | ✅ |
| S03 | listopad 2026, 1,2 mil. USD | [OAI]: 4. 11., $1,213,430. Sám OpenAI píše, že náklady jsou spíš horní mez. Cena za exploit (*$1,279*) vypuštěna podle zpětné vazby | ✅ |
| S05 | vlastní čísla; den před uvedením modelu, který je vytvořil; nikdo nepotvrdil celý počet; stovky hlášení | post 4. 11.; OpenAI, *GPT‑6 Cyber*, 5. 11. 2026 (Wayback): *„Our researchers used GPT‑6 Cyber to develop 948 privilege escalation exploits in Linux"*. Nezávislé potvrzení 948 jsem nenašel, to je negativní tvrzení. *„sent out hundreds of reports and patches"* [OAI] | ✅ |
| S08 | 164 v dubnu, 1 413 v říjnu | Infosecurity (duben 164); říjen 1 413 TechSpot, CrowdStrike, většina tisku. Jiné součty 1 411, 1 415, 1 416, rozdíl v metodice | ✅ |
| S09 | víc než za kterýkoli celý rok; přes tisíc ve Windows; varování kvůli AI | TechSpot: *„more security flaws than … in any previous year"*, Windows 1 102; Dark Reading k září podobně; Infosecurity: varování v červenci kvůli agentním AI nástrojům. Microsoft netvrdí, že vše našla AI, proto *would drive the surge* | ⚠ |
| S10–S11 | nesrovnatelné; soukromí nezabránilo chybám | Linuxiac (Kroah-Hartman); úsudek | ⚠ |
| S13–S14 | 40 mil. řádků, ~7 %, dosažitelnost, nelze násobit | [OAI]: *„5,034 audit targets, about 2.8 million lines … roughly 7%"*, výběr podle dosažitelnosti a bezpečnostní relevance. 1/0,07 ≈ 14 | ✅ |
| S15 | 2 308 za 12 hodin | [OAI] | ✅ |
| S16 | 1 724 reprodukováno v izolovaných VM | [OAI]: ~74,7 %. „Real" = dynamicky reprodukované | ✅ |
| S17 | 1 169 exploitů, standardní ochrany | [OAI]: SMEP, SMAP, KASLR, HARDENED_USERCOPY, *„stock desktop operating system"* | ✅ |
| S18 | seskupení na 948 | [OAI]: *„variant analysis … 948 distinct patches … We use that number"* | ✅ |
| S19–S20 | 200 úspěchů, 20 jinou neznámou chybou | [OAI], *Using the wrong 0-day*: *„through a different 0-day vulnerability than the one assigned"*. „Nobody knew about" = 0-day | ✅ |
| S21 | vzorek, 10 technik, externí experti | [OAI]: vzorek 166 exploitů, *„the techniques were new to them as well"*, detaily nezveřejněné, nelze ověřit nezávisle | ⚠ |
| S22 | červenec 166, říjen 948, tři měsíce oprav; *the later run found far more* (v0.4 *the reader had improved*, po poslechu draftu změněno: přisuzovalo nárůst jednoznačně lepšímu modelu, ačkoli útrata byla 2,4× a stejný harness tvrdí jen OpenAI) | [OAI]: GPT-5.6 Sol 166 za $513,690, nový model 948 za $1,213,430, *„despite three months of hardening"*, oba na aktuálním master. OpenAI, GPT-6 Cyber: *„using the same research harness"*. **Výhrady:** útrata 2,4×, výsledek 5,7×, takže peníze samy rozdíl nevysvětlí, ale podíl na něm mít můžou. Stejný harness tvrdí jen OpenAI a červenec spadá do doby *„while we were developing the pipeline"*. Závěr je tedy úsudek, opřený o výrok autorů, a obraz S22 ukazuje útratu i harness | ⚠ |
| S23–S24 | jen lokálně, dvoukrokový útok | [OAI] LPE; How-To Geek; obecná praxe řetězení | ✅ |
| S25 | účet bez záplat = root | [OAI]: *„functionally equivalent to root access for a well-resourced threat actor"*, *near and medium term* | ✅ |
| S26–S27 | Raymond, Linus's Law | *The Cathedral and the Bazaar*, esej 1997, kniha 1999. Znění z Wikipedie (Linus's law), esej přímo stáhnout nešel | ✅ |
| S32 | stroj prověří víc kandidátů než člověk | [OAI]: *„too many for security researchers to manually review and triage"*, 2 308 kandidátů za 12 hodin. Tvrzení o klesající ceně vypuštěno podle zpětné vazby | ✅ |
| S28–S30 | Heartbleed: 2014, ~½ mil. serverů, 2 roky, ~2 000 USD ročně, jeden na plný úvazek | Wikipedia: vloženo 31. 12. 2011, vydáno 14. 3. 2012, odhaleno 7. 4. 2014; ~17 %; Wikipedia uvádí i verzi se dvěma lidmi. *Hardly anyone did* je nadsázka: nakonec chybu našli dva nezávislí | ⚠ |
| S34–S35 | Ghidra, porovnání záplat | všeobecně doloženo (NSA 2019, Ghidriff v [AN]) | ✅ |
| S35b | zveřejněná oprava ukazuje útočníkům, kam mířit, dřív než ji mají všichni nainstalovanou (v0.6, po druhém poslechu) | obecně doložený jev „n-day“: porovnání záplaty odhalí místo chyby, ohrožené jsou nezáplatované systémy; v videu doložené přímo S36–S37 [AN] a S55 (WannaCry dva měsíce po záplatě) | ✅ |
| S36–S37 | Windows, 21 chyb, bez zdrojáku; 31 min; 18 do 6 h; 8 funkčních exploitů ~2 000 USD | **[AN]** Anthropic, *N-days*: binárky, symboly, dekompilace Ghidra, diff, text oznámení; ~$15 700 za osm řetězců na SYSTEM. Cena je odhad autorů. Střet zájmů viz `notes.md` | ✅ |
| S38 | záplata ukazuje na chybu; od nuly je to těžší | [AN] + kritika Penligent: čistě binární výzkum je doložen slabě. Že je to těžší, je úsudek | ⚠ |
| S39 | práh, ne zeď; číslo neexistuje | úsudek | ⚠ |
| S41 | 10 dní; >100 oprav od jiných; ~300 v diskusi | [OAI]: 61 + 43, 299. Scénář nepřipisuje těch 300 výslovně jiným | ✅ |
| S42 | jiní našli totéž současně | úsudek z S41 a S45; překryv není vyčíslený | ⚠ |
| S43–S44 | citáty Torvalds, květen | Linux 7.1-rc4 oznámení, 17. 5. 2026, doslova přes Phoronix. Originál na LKML nečten | ✅ |
| S45 | musí se brát jako veřejná; týž den | `Documentation/process/security-bugs.rst`: *„you must treat it as public"*, *„simultaneously across multiple researchers, often on the same day"* | ✅ |
| S47 | otevřené lze kontrolovat, uzavřené ne | úsudek; Kroah-Hartman o selektivním hlášení | ⚠ |
| S49 | přístup zdarma | Linux Foundation o Glasswingu; OpenAI Patch the Planet. Rozsah pro malé projekty nejistý, proto *offering* | ⚠ |
| S50 | 500 → přes 1 500 na vydání, většinou drobné | Phoronix 28. 8. 2026 (Wayback), slajd Kroah-Hartmana: 6.9–6.19 ~500, od 7.0 přes 1 000, 7.2 přes 1 500; *„most often … lower priority"*. Počítá opravy, ne nové chyby | ✅ |
| S51 | curl, leden 2026, placené odměny | The Register: *„remove the incentive … AI generated or not"*. Stenberg 25. 2. 2026: *„there is no bug-bounty, no money for vulnerability reports"*; hlášení přes HackerOne se vrátilo od března bez peněz, proto *ended its paid bug bounty* a v obraze REPORTS STILL WELCOME | ✅ |
| S52 | záplaty jsou návrhy, dřívější přidávaly kód | [OAI], *Iteration improves patch generation* | ✅ |
| S53 | výhoda placeného týmu | úsudek | ⚠ |
| S55 | 14. 3. 2017, 12. 5. 2017, ~200 000, ~150 zemí | Wikipedia (Europol ~200 000; další odhady přes 300 000). Dva měsíce uplynuly od záplaty, ne od exploitu, proto S56 netvrdí, že vznik exploitu trval dva měsíce | ✅ |
| S56–S57 | Firefox, exploit do hodiny, 18 dní | [AN]: engine `jsshell`, ne celý prohlížeč; *„just under one hour"*; *18 days before*. Zadaný veřejný diff | ✅ |
| S59 | cesta opravy; telefon měsíce nebo nikdy | obecně, bez čísla | ⚠ |
| S60 | Windows patch stačil | [AN], s výhradou k S38 | ✅ |
| S60b | aktualizovat vše a hned; s lepší AI záleží na každém dni víc (v0.6) | rada, ne fakt; „bude záležet víc“ je úsudek z S56 (exploit z veřejné opravy do hodiny) a z trendu v S08–S09 a S22, netvrdí žádné číslo | ⚠ |
| S61 | stejný test na obou stranách nikdo | *as far as is publicly known* (v0.6, dřív *as far as I can tell*: bez první osoby) | ⚠ |

## Ostatní zdroje

- Phoronix, 7.1-rc4 a 948, přes Wayback; Help Net Security 5. 11. 2026; How-To Geek 5. 11. 2026; root.cz 2026-11-06.
- Infosecurity Magazine, Dark Reading, TechSpot (Patch Tuesday 2026); Linuxiac; Let's Data Science.
- Anthropic: `https://www.anthropic.com/research/n-days`. The Register 21. 1. 2026 (curl). Wikipedia: Heartbleed, WannaCry.

## Před TTS doověřit

Nic, čtyři otevřená tvrzení z v0.1 jsou uzavřená (S05, S26, S50, S51).
