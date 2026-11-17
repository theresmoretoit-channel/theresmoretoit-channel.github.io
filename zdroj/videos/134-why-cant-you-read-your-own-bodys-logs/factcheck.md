# 134 — fact check scénáře (v0.4, 2026-11-04)

Každé ověřitelné tvrzení `script.md`. Podklady, citace a odkazy jsou
v `factcheck-zaklad.md` (dál „základ"). ✅ = doloženo přečteným zdrojem,
⚠ = sekundární zdroj nebo zjednodušení (zdůvodněno), ⓘ = úsudek nebo metafora
scénáře, ne faktické tvrzení.

## Opravy během škrtání

| scéna | původně | nyní | proč |
|---|---|---|---|
| S05 | *your brain controls your heartbeat* (zdroj) | *adjusts* | srdce si rytmus dělá samo, mozek ho upravuje |
| S08 | *the dentist took an X-ray* (v0.1) | *an X-ray showed why* | zdroje neříkají, kdo snímek pořídil |
| S20 | *your conscious throughput* (v0.1) | *human thought and action* | studie měří propustnost chování, ne vědomí |
| S33 | *the crew took it for* (v0.2) | *seem to have taken it* | zpráva: závěr komise, hlasový záznam neexistuje |
| S34 | *until they passed out* (v0.2) | *stopped answering* | čas ztráty vědomí v přečtených pasážích zprávy není |
| S38 | *the leading explanation* (v0.3) | *the best-known explanation* | teorií je víc, konvergence je nejznámější, „vedoucí" neověřeno |
| S44 | *what has infected you* (v0.2) | *the viruses you've met* | protilátky dokládají setkání, ne vždy infekci |

## Tvrzení po scénách

| scéna | tvrzení | | ověření |
|---|---|---|---|
| S05 | mozek upravuje tep, řídí teplotu, komunikuje s imunitou | ✅ | srdce: základ „Srdce bez nervů"; zbytek obecná fyziologie |
| S05 | *Surely, you're the system administrator* | ⓘ | domněnka, ne tvrzení; přebitá v S51 |
| S07 | BMJ 1995, stavař, hřebík 15 cm, skrz botu | ⚠ | originál se nepodařilo stáhnout; tři podání, jedno cituje znění (základ). **Do popisu jen „BMJ, 1995"** |
| S08 | *the smallest movement hurt*, fentanyl a sedativum (midazolam) před vytažením | ⚠ | totéž; *„the smallest movement of the nail was painful"* |
| S09 | hřebík prošel mezi prsty, noha nezraněná | ⚠ | totéž; *„the foot was entirely uninjured"* |
| S10 | o deset let později (2005), Colorado, nastřelovačka zpětně vystřelila | ✅ | leden 2005, Breckenridge; TIME *„his nail gun backfired"* |
| S10 | prudký úder, potom bolest zubu | ✅ | AP: *„hit with a steel baseball bat"*, *„toothache"* |
| S11 | šest dní, prášky a led, potom zubař, rentgen | ✅ | AP/TIME; *„icing it and taking Advil"* |
| S12 | 10cm hřebík, patro, mozek; vyjmut; očekává se plné uzdravení | ✅ | 4 in = 10,2 cm; TIME *„expected to make a full recovery"* |
| S13 | první bez zranění, silný opioid | ⚠ | fentanyl je silný opioid; *entirely uninjured* jako výš. Bota poškozená, zranění žádné |
| S15 | bloudivý nerv spojuje mozek se srdcem, plícemi, střevy | ✅ | obecná anatomie |
| S15 | ~80 % vláken vede k mozku | ✅ | Biomolecules, Frontiers; rozptyl 70–90 %, proto *by the usual estimate* |
| S16 | interocepce; část vnímáme, většinu ne | ✅ | definice; *most of it never does* je obecně přijímané zjednodušení |
| S18 | v laboratoři většina lidí napočítá málo | ✅ | Zamariola 2018: přes 95 % skórů je podhodnocených. **Neříká**, že to měří vnímání těla (sporné) |
| S19 | ~330 miliard buněk denně, většinou krevní | ✅ | Sender & Milo 2021, 86 % krev |
| S20 | ~10 bitů/s, smysly ~miliarda | ✅ | Zheng & Meister 2024; *one recent estimate*, *by the same estimate* |
| S22 | Google, *Every page should be actionable*, pět slov | ✅ | přečteno v SRE Book, kap. 6, doslova |
| S23 | *page* = upozornění, které budí technika; *if nobody can do anything…* | ✅ | vlastní parafráze téže kapitoly |
| S25 | Wall 1979: bolest má víc společného s hladem a žízní než se zrakem a sluchem | ✅ | abstrakt, *Pain* 6:253, doslova. *A demand for action, not a measurement* je náš výklad jeho *sense of bodily need* (ⓘ) |
| S26 | vysoký tlak obvykle bez příznaků, třetina 30–79, skoro polovina neví | ✅ | WHO 2023: 33 %, *nearly half* |
| S27 | přes 45 % prvních infarktů odhaleno později na EKG | ✅ | ARIC, Zhang 2016: 317 tichých, 386 klinických, 317/703 = 45,1 %. *One large American study* |
| S27 | *nobody took it for a heart attack* | ✅ | definice: Q vlny na EKG bez klinicky zaznamenaného infarktu |
| S28 | po většinu dějin se s tlakem nedalo nic dělat; *no action, so perhaps, no alert* | ⚠ | úsudek, výslovně označený jako hypotéza. Opora Wall, Nesse; přímý důkaz neexistuje |
| S29 | Nesse, *smoke detector principle*, levný poplach, drahé opomenutí | ✅ | Nesse 2001; toast a dům jsou naše ilustrace (ⓘ) |
| S30 | bolest, horečka, zvracení *may be tuned* | ✅ | Nesse jmenuje všechny tři |
| S30 | stavař *wasn't malfunctioning* | ⓘ | výklad, *seen that way* |
| S31 | nutkání při zadržení dechu hlavně z CO₂ | ✅ | centrální chemoreceptory; *mainly*, protože hypoxie umí vzdušný hlad taky (Moosavi 2003) |
| S32 | když O₂ klesá a CO₂ odchází, alarm skoro nezazní | ✅ | CSB *„no warning"*; AAIASB 1.13.3 *„no subjective symptoms noticeable up to the time of unconsciousness"*, ale i *„air-hunger"*, proto *barely* |
| S32 | piloti to trénují, euforie, nepoznají, že jsou v nesnázích | ✅ | AAIASB 1.13.3; FAA přes citaci (⚠) |
| S33 | 2005, Helios 522, kabinový tlak klesal, houkačka, zřejmě záměna | ✅ | AAIASB, přečteno; 06:12:38, 12 040 ft |
| S34 | pozemní technik se ptal na panel, kapitán na jističe chlazení | ⚠ | přečteno v AAIASB, ale je to **výpověď technika** policii; první písemná výpověď dotaz na panel neobsahuje |
| S34 | posádka přestala odpovídat, 121 mrtvých | ✅ | 06:20:21; *„115 passengers and 6 crew"* |
| S35 | asi tisíc lidí, *once called Ondine's curse* | ✅ | NORD: odhad 1 000–1 200 případů |
| S36 | automatické dýchání skoro nereaguje na změny O₂ a CO₂; ventilátor při každém usnutí nebo stále | ✅ | NORD: *„cannot sense…"*, *„from sleep only to constant support"*; *barely* zvoleno jako opatrnější |
| S37 | infarkt jako bolest v ruce, zádech, čelisti | ✅ | NHLBI |
| S37 | chlad na patře bolí v čele | ⚠ | Wikipedia; tvrdí se jen kde chladí a kde bolí, ne mechanismus |
| S38 | útroby a kůže se sbíhají na tytéž neurony v míše | ✅ | konvergenčně-projekční teorie, *best-known explanation*; doklad u potkana: PMC4770360 |
| S39 | mozek svede signál na kůži | ✅ | táž teorie |
| S40 | nová nebo nevysvětlená bolest na hrudi = vyhledat pomoc hned | ✅ | NHLBI: nejčastější příznak infarktu |
| S41 | mozková tkáň nemá receptory bolesti; operace za bdělého stavu po znecitlivění kůže a plen | ✅ | Barnes-Jewish; výhrada k cévám a měkké pleně, proto *tissue itself* |
| S42 | bolest hlavy hlavně z tkání kolem mozku | ✅ | Live Science, rešerše k plenám a cévám; mechanismy nejsou úplně vyřešené, proto *mostly* |
| S44 | 2015, test z kapky krve, 206 druhů, průměr ~10 | ✅ | VirScan, Science 2015; *partial*, protilátky slábnou |
| S45 | vlas ~1 cm/měs., stopy kortizolu, pár cm = pár měsíců | ✅ | PMC4216259; spolehlivě do ~6 cm. Hormon, ne psychický stav: *hint at* |
| S46 | krabička denně rok = odhadem 150 mutací na plicní buňku | ✅ | Alexandrov 2016, KCL; odhad z nádorů, *estimated* |
| S47 | nemoc přeruší růst nehtu, rýha, dorůstá ~6 měs. | ✅ | Cleveland Clinic, přečteno |
| S48 | protilátky jsou pro imunitu, hormon pro cílové buňky | ⓘ | zjednodušení, biologicky správné |
| S49 | EKG, EEG, krevní testy, skenery, hodinky | ✅ | obecně známé |
| S50 | 100/min po schodech normální, v klidu může znamenat něco jiného | ✅ | horní mez klidového tepu je 100/min |
| S51–S54 | *never had root*, *unprivileged process*, *built to make you act* | ⓘ | metafora a výklad, navazuje na hypotézu z S28 |

## Neověřeno v originále

- **BMJ 1995** (S07–S09, S13): stránka odmítla stažení. Znění potvrzují tři podání.
  **Přesnou citaci BMJ 1995;310:70 a autory nepsat, dokud ji někdo neověří v archivu.**
- **FAA brožura** (S32): odmítla stažení, tvrzení kryje zpráva AAIASB.
- **IASP** (nepoužito ve scénáři).
