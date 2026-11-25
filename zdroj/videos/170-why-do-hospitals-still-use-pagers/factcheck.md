# 170 — fact check scénáře (v0.3 → v0.4, 2026-11-22)

Ověřuje **každé** tvrzení `script.md`, scénu po scéně. Značky:
**P** primární zdroj přečtený, **S** sekundární, **M** spočítáno,
**Pam** z paměti (nedohledáno, riziko nízké).

Primární zdroje:
- **O'Leary 2017** — O'Leary K. a kol., *Hospital-Based Clinicians' Use of
  Technology for Patient Care-Related Communication: A National Survey*,
  J Hosp Med 2017;12:530–535, doi 10.12788/jhm.2767 (PDF přečteno, s. 530–532).
- **Ercole 2023** — *Moving from non-emergency bleeps and long-range pagers
  to a hospital-wide, EHR-integrated secure messaging system: an implementer
  report*, BMJ Health Care Inform 2023;30:e100706 (PubMed 37080612; preprint
  medRxiv 10.1101/2022.11.21.22282572). Plný text přečten 2026-11-22
  (přijatá verze z repozitáře Cambridge, `repository.cam.ac.uk`).
- **gov.uk 2019** — *Health and Social Care Secretary bans pagers from the NHS*.
- **Lemelson** — Lemelson-MIT, profil Al Gross.

> **Past nalezená při kontrole:** `notes.md` i zpětná vazba 0.1 uváděly
> pro Cambridge **PMC10990552**. To je jiný článek — Kwan a kol., JAMIA
> 2024, **UC San Diego**, žádné výjimky pro zástavu/úraz/požár. Správně je
> Ercole 2023 výš. Opraveno v `notes.md`.

Výsledek: **5 oprav** (✏️), v0.4 = v0.3 + tyto opravy. 68 scén.

## Háček (S01–S10)

| scéna | tvrzení | ověření | verdikt |
|---|---|---|---|
| S01–S02 | lékař 2026 se smartphonem a pagerem „z 80. let" | vzhled a koncepce jednosměrného alfanumerického pageru (POCSAG doporučen CCIR 1981) | ✅ Pam |
| S04 | 1949, Al Gross, „what he called a telephone pager", patent | Lemelson: *„In 1949, he invented the telephone pager"*, *„invented and patented the telephone pager"* | ✅ P |
| S05 | o rok později Jewish Hospital v New Yorku | Lemelson: *„New York's Jewish Hospital did implement Gross' pager system the next year (1950)"*. Pozn.: Wikipedie zmiňuje i službu pro lékaře v NY z 1950 bez jména nemocnice | ✅ P |
| S05 | víc než 20 let před prvním hovorem z mobilu | Martin Cooper, Motorola, 3. 4. 1973; 1973 − 1950 = 23 | ✅ Pam + M |
| S06 | „a 2017 survey" | sběr dat **duben–červenec 2016**, publikace 2017 | ✏️ → *„a survey published in 2017"* |
| S06 | američtí nemocniční klinici, ~8 z 10 respondentů dostalo pager | O'Leary: *„Pagers were provided to the majority of respondents by their hospitals (79.8%, 495/620)"*; databáze Society of Hospital Medicine, 87,8 % lékaři, 12,2 % NP/PA; adjusted response rate **11,0 %** — proto „of those who answered" | ✅ P |
| S07 | pro asi polovinu hlavní kanál zpráv o pacientech | O'Leary: *„49.0% (304/620) indicating this was the primary way they received PCR communication"* | ✅ P |
| S08 | 2019, vláda nařídila NHS skončit s pagery pro běžné zprávy do konce 2021 | gov.uk 2019: pagery pro **ne-nouzovou** komunikaci do konce 2021; tisk (ITPro, CSP): trusty si smí ponechat pagery pro nouzové situace | ✅ P/S |
| S08 | asi 130 000 pagerů | gov.uk 2019: ~130 000, £6,6 mil./rok. (Tvrzení „10 % pagerů světa" Full Fact nedoložil — ve scénáři **není**) | ✅ P |
| S09 | v létě 2026 se pořád používaly | dopis Layly Moran (Lib Dem) šéfovi NHS England 14. 8. 2026: pagery pořád v provozu, 5 let po termínu; spuštěno vyšetřováním BBC | ✅ S |

## Jak pager funguje (S11–S20)

| scéna | tvrzení | ověření | verdikt |
|---|---|---|---|
| S12 | „A pager has no transmitter" | platí pro **jednosměrný** pager; existují i obousměrné (Wikipedie: *„response pagers and two-way pagers can also acknowledge… using an internal transmitter"*) | ✏️ → *„A typical hospital pager has no transmitter"* |
| S13 | 1975, pošta svolala výrobce a inženýry z několika zemí | Wikipedie: skupina se začala scházet **1976**, *„attended by representatives of British, European, and Japanese pager manufacturers"*, předsedala British Post Office; Salford uvádí založení POCSAG **prosinec 1975**. Rok se mezi zdroji rozchází | ✏️ → *„In the mid-1970s… pager makers from Britain, Europe and Japan"* |
| S14 | kód dodnes ve vysílání, jméno po skupině POCSAG | CCIR přijal jako Radiopaging Code No. 1 (Rec. 584) 1981; dodnes používán (paging NHS v létě 2026, Vancouver 2018 — POCSAG) | ✅ S |
| S14 | každý pager má své číslo, síť vyšle číslo a za ním zprávu | POCSAG: adresní kódové slovo (RIC), za ním datová slova | ✅ S |
| S15–S16 | mobilní síť zná přibližně oblast; při hovoru volá v celé oblasti; inženýři tomu říkají paging | GSM/LTE: location/tracking area, paging channel (PCH) | ✅ Pam (standardy 3GPP) |
| S17 | telefon odpoví, pak obousměrné spojení | tamtéž (paging response) | ✅ Pam |
| S18–S19 | pagerová síť nedostává odpověď, vysílá do celé oblasti, reaguje jen pager s číslem | jednosměrný paging, simulcast; dokument FCC JAC o ReFLEX (nepřečten, 403) — princip je obecný | ✅ S |

## Výhody (S21–S37)

| scéna | tvrzení | ověření | verdikt |
|---|---|---|---|
| S21 | přijímač většinu času spí, probudí se jen ve svém úseku cyklu | Wikipedie POCSAG: dávky (sync + kódová slova), přijímač *„only needs to listen to the pair that applies to it"*, *„allows the receiver to turn off for a considerable percentage of the time"* | ✅ S |
| S22 | jedna malá baterie na týdny | manuály a provozovatelé: jednosměrný pager na AA alkalickou ~3–4 týdny, AAA 2–3 týdny až měsíce, podle provozu | ✅ S |
| S24 | stíněné místnosti kolem skenerů a rentgenů | MRI ve Faradayově kleci, rentgen stíněný | ✅ Pam |
| S25–S26 | telefon potřebuje obousměrný spoj, slabý je jeho vysílač | uplink z ručního zařízení je limitující směr; obecné | ✅ Pam |
| S27 | vysílač pagingu výkonný a vysoko, nejvýš pár tisíc bitů/s | POCSAG 512, 1 200, 2 400 b/s (Wikipedie); FLEX do 6 400 | ✅ S |
| S28 | pomalý signál se snáz vytáhne ze šumu; spolu s výkonem a frekvencí „často" dosáhne tam, kde telefony mají potíže | energie na bit roste s délkou bitu; tvrzení o pokrytí jsou hlavně od dodavatelů (Spok) → změkčeno „often… struggle" už ve v0.2 | ✅ S |
| S30 | při katastrofě každý hovor zatěžuje už přetíženou síť | obecné; Katrina výš | ✅ S |
| S31 | Katrina 2005: „five bars and can't get through" | Computerworld 2. 9. 2005 (S. Lawson): telefony ukazovaly signál, ale nespojily se — **příčina výpadek spojení vysílačů s ústřednou**, ne přetížení. K přetížení sedí jiná věta téhož článku: *„circuits often were jammed and callers turned to text messaging"* (Jim Gerace, Verizon Wireless). Doslovné „five bars" nedohledáno | ✏️ → *„Verizon said that where phones still worked at all, the circuits were often jammed"* |
| S32 | i pagerové sítě mají limity, stožáry selhávají; tisíc příjemců = jedno vysílání | princip vysílání; omezená kapacita kanálu | ✅ Pam |
| S34 | tým: lékař, anesteziolog, sestry, „někdy nosič" | nosič v týmu nedoložen | ✏️ → *„Doctors, an anaesthetist, several nurses"* |
| S35 | v mnoha britských nemocnicích 2222 | NPSA Patient Safety Alert, únor 2004: 2222 jako standardní číslo v Anglii a Walesu; National Cardiac Arrest Audit ho uvádí jako číslo na resuscitační tým v nemocnicích NHS | ✅ S |
| S35 | celý tým pípne ve stejnou sekundu | ústředna vyšle skupinovou výzvu (crash bleep); časová shoda „same second" je obrazná | ✅ Pam |
| S36–S37 | nic neodemykat, žádná aplikace; dosáhne na lidi po budově naráz bez odpovědi | vyplývá z výše uvedeného | ✅ |

## Cena (S38–S47)

| scéna | tvrzení | ověření | verdikt |
|---|---|---|---|
| S39–S40 | pager nepotvrdí doručení, lékař musí najít telefon a zavolat zpět | jednosměrný pager; gov.uk 2019 a tisk: *„one-way… staff cannot reply"* | ✅ S |
| S43 | některé systémy posílají holý text; šifrovaný paging existuje | Trend Micro *Leaking Beeps*; provozovatel sítě v kauze NHSBT: nabízí šifrovaný paging, za použití odpovídá zákazník | ✅ S |
| S44 | levný rádiový přijímač, kdokoli v dosahu | Trend Micro: SDR a levné vybavení, desítky km | ✅ S |
| S45 | 2018 výzkumníci ve Vancouveru: jména, diagnózy, čísla pokojů | Open Privacy Research Society, objeveno 11. 11. 2018, Vancouver Coastal Health; jména, diagnózy, ošetřující lékař, číslo pokoje (Trend Micro) | ✅ S |
| S46 | srpen 2026, BBC: služba NHS, která páruje darované orgány, posílala jména, data narození, údaje o orgánech | NHS Blood and Transplant přiznal (Computing, healthcare-management.uk, 14. 8. 2026): jména, data narození, údaje o orgánu, skóre shody tkání | ✅ S |
| S47 | omluvila se, přestala posílat osobní údaje vzduchem | NHSBT: *„deeply sorry"*, přestal posílat identifikovatelné údaje, nahlásil ICO | ✅ S |

## Aplikace a Cambridge (S48–S53)

| scéna | tvrzení | ověření | verdikt |
|---|---|---|---|
| S48 | zabezpečené aplikace, obousměrné, šifrované, s potvrzením přečtení | obecné (Epic Secure Chat, Vocera, …) | ✅ Pam |
| S50 | Cambridge University Hospitals začaly přecházet 2021 | Ercole 2023: *„Secure Chat was made available at our organisation in July 2021"*; trust na LinkedIn: plné nasazení **červen 2022** trust-wide | ✅ S |
| S51 | upgrade Wi-Fi na celý areál, týden souběhu, pak běžné pagery skončily | Ercole 2023: *„coincided with a major Wi-Fi infrastructure upgrade to give full coverage across the whole estate"*, *„Cutover was accompanied by a week of Secure Chat and bleeps running in parallel"* | ✅ S |
| S52 | na pageru zůstaly zástava, závažný úraz, požár | Ercole 2023: *„Our aim was to replace all bleeps/pagers apart from 'cardiac arrest', 'major trauma' and 'fire'"*; titul článku „Moving from **non-emergency** bleeps" → dosaženo. Formulace cíle je ze studie, výsledek z titulu | ✅ S |

## Pointa a závěr (S54–S68)

| scéna | tvrzení | ověření | verdikt |
|---|---|---|---|
| S54–S60 | dva druhy zpráv; pager = druhý kanál, který selhává jinak | interpretace, opřená o Cambridge a výjimku gov.uk pro nouzové situace | ✅ (argument) |
| S58 | moderní nemocnice má záložní napájení, Wi-Fi, vlastní nouzové systémy | obecné | ✅ Pam |
| S61 | víc než 70 let | 2026 − 1950 = 76 | ✅ M |
| S63 | Japonsko vypnulo poslední komerční pagerovou službu 2019 | Wikipedie: *„On 1 October 2019, Japan's last paging service provider shut down radio signals"* (Tokyo Telemessage, služba končila 30. 9.) | ✅ S |
| S64–S65 | méně zákazníků → méně sítí a výrobců; nemocnice „may become" posledními zákazníky | podmíněná hypotéza, ne předpověď (už ve v0.2) | ✅ (hypotéza) |

## Co zůstává otevřené

- **Ercole 2023 plný text** — 403 z medRxiv i BMJ; citace z výňatků.
  Kdyby šel stáhnout (repozitář Cambridge `repository.cam.ac.uk`),
  ověřit datum přechodu a že výjimky platí i po nasazení.
- **Gov.uk 2019** — přesné znění výjimky pro nouzové pagery mám jen z tisku.
- **Dokument FCC JAC o ReFLEX** (paging za 11. září a Katriny) — 403,
  ve scénáři se o něj nic neopírá.

## Dodatek k v0.5 (podle `zpetna vazba 0.4.txt`, 2026-11-22)

Ercole 2023 přečten celý. Čísla scén jsou **podle v0.5** (za S52 vložena
nová S53, zbytek o jednu dál).

| scéna v0.5 | tvrzení | ověření | verdikt |
|---|---|---|---|
| S50 | Cambridge přešla 2022 | *„Secure Chat was made available at our organisation in July 2021"*; *„The original 4th May 2022 go-live date was pushed back… to 8th June 2022"* | ✅ P |
| S51 | upgrade Wi-Fi na celý areál | *„coincided with a major Wi-Fi infrastructure upgrade to give full coverage across the estate"* | ✅ P |
| S51 | první týden šly zprávy do aplikace i na pagery | *„contact centre operatives would send messages both to Secure Chat and to existing bleeps for one week post go-live"* | ✅ P |
| S51 | pak běžné zprávy na pager klesly skoro na nulu | *„bleep counts dropped to negligible levels"*; *„We were able to effectively replace non-emergency bleeps/long-range pagers"* | ✅ P |
| S52 | tři druhy volání se přesouvat neměly | *„Our aim was to replace all bleeps/pagers apart from 'cardiac arrest', 'major trauma' and 'fire'"* — formulováno jako záměr, ne jako konečný stav | ✅ P |
| S53 | starý systém nevypnuli, zůstane, dokud posouzení odolnosti neukáže, že ho lze vyřadit (v0.6) | *„without physically retiring the legacy system"*; *„It is anticipated that the bleep system will be decommissioned in due course depending on a future resilience analysis"* | ✅ P |
| S18, S21 | jednosměrný pager / „this kind of pager" | sjednoceno s S12 | ✅ |
| S28 | pomalejší signál „can hold up better in noisy conditions" | změkčeno, viz S28 výš | ✅ |
| S43 | „They just don't use it" (o systémech s holým textem) | jen ty, které šifrování nemají; žádné tvrzení o rozšíření | ✅ |
| S60 | „another channel… can fail in different ways" | bez tvrzení o nezávislé infrastruktuře (S32: i pagerové vysílače selhávají) | ✅ |
| S69 | „designed to reach you when everything else fails" | „designed" = záměr, ne jistota | ✅ |

## Dodatek k v0.7 (po poslechu draftu, 2026-11-23)

| scéna | tvrzení | ověření | verdikt |
|---|---|---|---|
| S36 | „No code to enter.“ (dřív „Nothing to unlock.“) | táž myšlenka jako dřív (příjemce nemusí nic odemykat ani zadávat); netýká se vytočení 2222 odesílatelem, to je S35 | ✅ |
| S69 | „So here's a question for you… Let me know in the comments.“ | bez věcného tvrzení | ✅ |

## Dodatek k v0.8 (2026-11-25)

| scéna | tvrzení | ověření | verdikt |
|---|---|---|---|
| S07 | „For about half of **all who answered**“ (dřív „half of them“) | O'Leary: 304/620 = 49,0 % **všech** respondentů; „them“ se četlo jako polovina z těch, kdo pager dostali (495), a to zdroj netvrdí. Nález překladatele | ✏️ opraveno |
