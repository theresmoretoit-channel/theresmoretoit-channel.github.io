# Fact check — 098 Why Do Drones Fly on a Wire?

Ověřováno 2026-10-08 nad v0.1, opravy jsou ve `script 0.2.md`.
Verdikt: **OK** = beze změny, **UPRAVENO** = věta změněná ve v0.2.

## Vlákno a mechanika

| scéna | tvrzení | ověření | závěr |
|---|---|---|---|
| S03 | tlusté jako nejtenčí struna kytary | Ptashka 17-O-50: *„G.657.A2 fibre … cable diameter of 0.26 mm"* ([United24](https://united24media.com/war-in-ukraine/ukraine-sends-50-km-fiber-optic-fpvs-into-russian-rear-storage-sites-to-hit-hidden-armor-21500)); prodejci 0,25 mm. Struna E = 0,010″ = 0,254 mm. Raný 3DTech (2024) měl 250 g/km, tedy spíš ~0,5 mm. | OK |
| S04 | 20 km, některé 40 | Fedorov 7/2025: z 20 km na *„more than 40 km"* ([Pravda](https://www.pravda.com.ua/eng/news/2025/07/21/7522773)); Ptashka kodifikovaná na 50 km. Deklarace, ne nezávislé měření. | OK |
| S15 | světlo se „odráží" ve skle | G.657 je jednovidové, „odraz" je obraz totálního odrazu. Popularizační zjednodušení. | OK |
| S19 | dron váží pár kilogramů | Ukrajinský schválený model MTOW do 8,5 kg ([Liga](https://news.liga.net/en/amp/politics/news/defense-ministry-approves-new-ukrainian-fiber-optic-drone-photos-and-specifications)); 10–17″ drony. | OK |
| S21–S22 | cívka letí na dronu, vlákno se odmotává a leží | NPR: *„unspools as the drone flies away"* ([WUSF/NPR](https://www.wusf.org/2025-08-07/fiber-optic-drones-are-leaving-miles-of-plastic-trash-along-ukraines-front-lines)); „sky-end canister" s převodníkem. | OK |
| S43 | vlákno nese data, ne proud | sklo je nevodivé, převodník napájí baterie dronu | OK |
| S44 | ~~10 km ≈ 2 kg~~ → **10 km ≈ 1 kg** | GetFPV 10 km 0,95 kg vč. modulu; prodejce 950 g / 20 km 1,65 kg / 30 km 2,1 kg; 3DTech 1,1 kg/10 km. **Výpočet** 250µm vlákna: sklo Ø125 µm 1,227·10⁻⁴ cm² × 10⁵ cm × 2,2 = 27,0 g/km; akrylát 3,68·10⁻⁴ cm² × 10⁵ × 1,1–1,2 = 40,5–44,2 g/km; **68–71 g/km**, 10 km ≈ 0,7 kg + kanystr. Původní 2,3 kg byl ruský zdroj o jiném dronu. | **UPRAVENO** |
| S45 | ~~„pilots describe"~~ neohrabané, fouká je vítr | Fedorov (ministr, ne pilot): *„sluggish… prone to wind"*; CBC: *„slower to respond and more exposed to breezes"* ([CBC](https://www.cbc.ca/1.7441957), doslovné znění 403, z výtahu) | **UPRAVENO** na „They're described as" |
| S47–S48 | vlákno se položí jednou, nenavíjí se | NPR: *„once the drone crashes or explodes, the cable remains"*; sběr ani znovupoužití nedoloženo, brání miny ([Pravda 2026](https://www.pravda.com.ua/eng/news/2026/05/10/8034095/)) | OK |
| S51 | ~~ploty a střechy~~ → dráty a budovy | RFE/RL: *„lines can tangle or catch on objects"* ([GlobalSecurity/RFE](https://www.globalsecurity.org/wmd/library/news/ukraine/2025/03/ukraine-250312-rferl03.htm)); NPR *„left hanging in trees"*. Ploty/střechy výslovně ne. | **UPRAVENO** |
| S38–S39 | rádio slábne za kopcem/v budově; vlákno jde, kam dron | velitel: *„really great when you need to fly into some kind of building"*; DW pilot *„rooms, corridors"* (z výtahu vyhledávače) | OK, slabší doklad |
| S66 | ~~nehnije~~ → nehnije, nanejvýš se drolí na mikroplast | Pravda: *„decomposes slowly and can remain in the soil for a very long time"*; UV-tvrzený akrylát; drobení na mikroplasty ([Meduza](https://meduza.io/en/feature/2026/07/29/fiber-optic-cables-used-to-guide-drones-are-blanketing-ukraine-s-front-line-researchers-are-only-beginning-to-understand-their-environmental-impact)) | **UPRAVENO** |

## Historie a ekonomika

| scéna | tvrzení | ověření | závěr |
|---|---|---|---|
| S08 | RUSI 2023: ~10 000 dronů měsíčně | Watling & Reynolds, *Meatgrinder*, 19. 5. 2023, s. iii: *„Ukrainian UAV losses remain at approximately 10,000 per month."* ([PDF](https://static.rusi.org/403-SR-Russian-Tactics-web-final.pdf)); pozn. 55: zdrojem rozhovory s ukrajinskými důstojníky | OK |
| S09 | ~~„most weren't shot down, lost radio link"~~ → **velká část kvůli rušení** | s. 18: EW *„is contributing to"*, včetně *„navigational interference"*; „most" ani „neztratily spojení" tam není. RUSI 11/2022 s. 37: častější příčinou neúspěchu mise je *„disruption … through electronic warfare"* | **UPRAVENO** |
| S10–S12 | video dolů, povely nahoru; rušička přehluší; dron se unáší, přistane nebo spadne | Betaflight failsafe: výchozí *Drop* = *„immediate disarm and motor stop"*, alternativy Landing, GPS Rescue ([docs](https://betaflight.com/docs/wiki/guides/current/Failsafe)) | OK |
| S13 | přechod na jiné frekvence, rušičky za nimi | TWZ 28. 5. 2025, velitel: *„We change to other frequencies, but when they find out…, they also scale this solution up."* ([TWZ](https://www.twz.com/news-features/inside-ukraines-fiber-optic-drone-war)) | OK |
| S25 | ~~„since around 1970"~~ → **přes půl století**; TOW = …Wire-guided | TOW ve službě 1970 (Hughes); drátem naváděné střely starší: SS.10 od 1955, Maljutka 1963, X-7 1944–45 (data z paměti agenta, neověřeno primárně) | **UPRAVENO** — „since 1970" by naznačovalo vznik techniky |
| S26 | FOG-M v 80. letech, vlákno místo drátu, kamera v nose | GAO NSIAD-96-7: vývoj od 1978, zkoušky 1984 ([GAO](https://www.govinfo.gov/content/pkg/GAOREPORTS-NSIAD-96-7/html/GAOREPORTS-NSIAD-96-7.htm)); motor TOW, TV kamera v nose ([designation-systems](https://designation-systems.net/dusrm/m-157.html)) | OK |
| S27 | ~~„without ever seeing the target"~~ → zpoza kopce, cíl jen na obrazovce | GAO: *„The gunner views the flight path and the target via a seeker… linked … by fiber optic cable."* Cíl viděl, jen kamerou (NLOS). | **UPRAVENO** — původní věta byla nepravdivá |
| S28 | zrušeno, obnoveno, znovu zrušeno; ~~„simply"~~ → „mostly" moc drahé | GAO: NLOS *„terminated… January 1991… because of excessive cost growth"*; NLOS-CA *„disapproved for affordability reasons"*; EFOGM 1992, 6/2002 *„cancelled further funding"*; i *„other programs had higher priority"*; > 440 mil. $ | **UPRAVENO** |
| S30 | stovky milionů km vlákna ročně | CRU (přes [FBA](https://fiberbroadband.org/2024/03/07/world-optical-fiber-demand-poised-for-continued-growth/)): 2024 poptávka **557 mil. fibre-km**; 2023 ≈ 536 mil. Poptávka, ne výroba; prognóza. | OK |
| S31 | malý závodní dron stojí pár set dolarů | DroneXL 4/2025: vláknový ~800 $, *„double the price of standard FPV"* → ~400 $ ([DroneXL](https://dronexl.co/2025/04/23/fiber-optic-drones-warfare-ukraine)); jinde 200–1 000 $ | OK |
| S32 | levné natolik, aby se po jednom letu zahodilo | kamikadze, vlákno se nenavíjí. **Výhrada:** 2026 vlákno G.657.A2 zdražilo kvůli datacentrům AI, 50km cívka z 300 $ na *„easily $2,500"* (jeden operátor, [DroneXL 5/2026](https://dronexl.co/2026/05/11/ukraine-fiber-optic-spool-price-ai-data-center-demand/)); VYRIY: 1 km z ~4 $ na 29 $ | OK, nechané — pořád se zahazuje |
| S33 | do 2025 obě strany ve velkém | Rusko od jara 2024, Kursk 8/2024 (KVN, [Euronews](https://www.euronews.com/next/2024/09/01/ukraine-war-how-and-why-russia-is-using-almost-indetectable-drones)); Ukrajina 2025: **374 000** vláknových dronů od agentury zakázek ([Euromaidan](https://euromaidanpress.com/?p=402703)) | OK |

## Bojiště a životní prostředí

| scéna | tvrzení | ověření | závěr |
|---|---|---|---|
| S35–S37 | rádio jde zaměřit, pilot na vlákně je tichý | *„no thermal or radio signature"*, nevyzradí polohu *„by radio direction finding"* ([Wikipedia](https://en.wikipedia.org/wiki/Fiber_optic_drone), cituje Forbes, BI); [Forces News](https://www.forcesnews.com/technology/has-kyiv-found-way-stop-russias-unstoppable-fibre-optic-drones) | OK |
| S53–S55 | vlákno se leskne a dá se sledovat | DW, pilot Azovu: *„If the cable hangs or gets tangled in branches or grass… it is very noticeable in sunlight, especially at dawn or dusk"* ([Vreme/DW](https://vreme.com/en/svet/rat-u-ukrajini-da-li-ce-dronovi-s-optickim-vlaknima-promeniti-ishod-sukoba/)); Militarnyi 18. 2. 2025: brigáda Kara-Dag průzkumným dronem sledovala lesknoucí se vlákna až ke stanovišti operátorů ([Militarnyi](https://militarnyi.com/en/news/national-guardsmen-found-enemy-drone-operators-by-following-fiber-optic-wires/)). Sleduje se **ze vzduchu**, a v polích plných vláken je to dnes skoro nemožné. | **UPRAVENO** — doloženo, zpřesněno (tráva a větve, ze vzduchu) |
| S57 | když nejde rušit, musí se fyzicky | BI: brokovnice 12 ráže na každé misi ([BI](https://www.businessinsider.nl/the-ukrainian-soldiers-best-chance-against-russias-advanced-unjammable-drones-is-as-low-tech-as-it-gets)) | OK |
| S58–S59 | obě strany, sítě nad silnicí, na kilometry | Rusko: ~2 km tunel Bachmut–Časiv Jar ([TWZ](https://www.twz.com/news-features/russians-erect-mesh-net-tunnel-over-a-mile-long-to-counter-ukrainian-fpv-drones)); Ukrajina: Fedorov 822 km tras od začátku 2026, cíl 4 000 km ([Euromaidan](https://euromaidanpress.com/?p=410039), neověřeno nezávisle) | OK, „for kilometres" je skromné |
| S63–S65 | kilometry z jednoho letu, pole se třpytí jako pavučina | Sunday Times 11. 4. 2026: *„fields, roofs and treetops glistening with threads"*, *„a spider's web of cables"*; Reuters 30. 6. 2026: *„glistening in the sunlight like giant spider web"* ([bdnews24](https://bdnews24.com/world/a2e355134fad)) | OK |
| S67–S68 | červen 2026, fotka hnízda z východní Ukrajiny, shozené ze stromu bombou | Olena Tregub na X, foto Oleh Malchenko; strom zasažený ruskou klouzavou bombou v Doněcké oblasti ([NAKO 9. 6. 2026](https://nako.org.ua/?p=14034)). **Jiné hnízdo** našel Jurij Kochan (Azov) 2. 6. 2025 u Torecku — **ve videu ukazovat jen fotku z 2026**. | **UPRAVENO** („by a bomb", „spread around the world") |
| S69 | ~~„two of these nests are now kept"~~ → týž měsíc armáda poslala dvě hnízda do muzea | Reuters 30. 6. 2026: *„Kyiv's War Museum"* dostalo dvě hnízda od armády; plně **National Museum of the History of Ukraine in the Second World War**. Jedno zůstává v Kyjevě, druhé na výzkumu v Nizozemsku. Že je mezi nimi to z fotky, nedoloženo. | **UPRAVENO** — „like it", ne „these" |
| S70 | nikdo zatím neví, kolik škodí; vlákna se omotají; sovy | Novak (Ukr. společnost ochrany ptáků, Sunday Times): *„How exactly the fibre will affect birds, we will find out in a few years. There is a danger of chicks becoming entangled"*; Vasyliuk ([Meduza](https://meduza.io/en/feature/2026/07/29/fiber-optic-cables-used-to-guide-drones-are-blanketing-ukraine-s-front-line-researchers-are-only-beginning-to-understand-their-environmental-impact)): sovy *„become entangled and can't free themselves. They just hang there."* | **UPRAVENO** — přidány sovy, „nobody knows" zúženo na míru škody |

## Bez faktického obsahu

S01–S02, S05–S07, S14, S16–S18, S20, S23–S24, S29, S34, S40–S42, S46,
S49–S50, S52, S56, S60–S62, S71–S74 — rétorika a shrnutí výše ověřeného.
S72 *„the most crowded radio sky on Earth"* je nadsázka, ne měření;
S73 *„noise will stop that same day"* je obraz (rušičky se vypnou).

## Pro obrázky (až ve storyboardu)

- Hnízdo: **jen fotka z června 2026** (Tregub/Malchenko), ne azovské z 2025 —
  a licence fotky z X bude problém; spíš kresba.
- Vlákno: 0,25 mm, ne kabel s izolací; cívka na zádi/pod dronem.
