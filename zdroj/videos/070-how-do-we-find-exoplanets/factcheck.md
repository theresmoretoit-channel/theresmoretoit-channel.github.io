# Fact check — 070 — How Do We Find Exoplanets?

Ověřeno 2026-09-28. Výchozí text: `script 0.1.md`; výsledek:
`script 0.2.md` a shodný `script.md`. Podnět: `zpetna vazba 0.1.txt`.
Prošly všechny scény, nejen místa označená ve zpětné vazbě.

**Výsledek:** dvě lokální úpravy (S17 a S35), žádná změna oblouku,
žádné nové metody, žádné další CTA. Číslo 0,008 % je správně zaokrouhlené.
Formulace o minimální hmotnosti i o spektrálních stopách mohou zůstat.

Níže jsou oddělené ověřitelné výroky, autorská zjednodušení a pokyny
pro budoucí vizuál. **Toto je kontrola textu; dosud neexistující obrázky
ani zvuk nejsou tímto dokumentem schválené.** Odkazy byly otevřené a přečtené;
historické články dokládají metodu nebo konkrétní detekci, nikoli aktuální
počty planet či současný provoz misí. Do scénáře žádné takové počty nepřibyly.

## S01 — Exoplanety a jejich četnost
*Kotva: „outside our Solar System“*

- Exoplaneta je planeta mimo Sluneční soustavu. V tomto videu jde o planety
  u jiných hvězd, nikoli o úplnou definici zahrnující i volně plující planety.
- „They are everywhere“ je hovorové vyjádření četnosti, nikoli tvrzení,
  že každá hvězda má známou planetu. Keplerova populační měření ukazují,
  že planety jsou velmi běžné. [NASA, výsledky Keplera][kepler]
- Obtížnost přímého spatření rozebírají následující scény. **OK.**

## S02–S03 — Jasový kontrast a úhlová vzdálenost
*Kotva: „almost like a single point of light“*

- Nejvýkonnější dalekohled je myšlenkový experiment, nejmenuje se konkrétní
  přístroj ani neexistující absolutní žebříček výkonu.
- Planetu zpravidla překrývá záře hvězdy a malá úhlová separace; přímé
  snímkování je obtížnější zejména ve viditelném světle. [ESA, metody][esa]
- „Almost like a single point“ není tvrzení, že je separace vždy nulová:
  například jedna AU ve vzdálenosti deseti parseků odpovídá 0,1 úhlové sekundy
  (z definice parseku). Toto je vlastní geometrická ilustrace, ne nové číslo
  do narace. Desítky až stovky světelných let jsou realistické vzdálenosti:
  přímo pozorovaný HR 8799 leží přibližně 129 světelných let daleko. [ESO][gravity]
- **OK jako obecný popis.** V obraze neukazovat rozlišený kotouč exoplanety
  jako skutečnou fotografii.

## S04–S05 — Hlavní otázka a nepřímá detekce
*Kotva: „what the planet does“*

Otázka a hodnocení „clever“ nejsou fyzikální tvrzení. Hlavní princip
odpovídá změnám jasu, pohybu hvězdy a gravitačnímu čočkování.
Přímé snímkování je v další scéně výslovná výjimka. [Přehled NASA][methods]
**OK.**

## S06–S08 — Přímé snímky a mladé horké planety
*Kotva: „tend to be large, young“*

- Přímé snímky existují; nevyžadují tranzit. Potlačení hvězdného světla
  může zpřístupnit dostatečně jasného průvodce.
- Dosavadní přímé snímkování zvýhodňuje obří mladé planety, které dosud
  vyzařují teplo z formování. Infračervené záření je proto vhodné.
  „Tend to“ je správné omezení, nikoli absolutní podmínka. [NASA][methods]
- Zbytkové teplo doloženo i konkrétním objektem HR 8799 e. [ESO][gravity]
- **OK beze změny.** „Large“ neznamená, že známe poloměr každého přímo
  zobrazeného objektu; jde o obecné označení obřích planet.

## S09 — Koronograf
*Kotva: „blocks or suppresses“*

Koronograf potlačuje hvězdné světlo, aby šlo detekovat slabší okolní
zdroje. „May need“ a „blocks or suppresses“ správně ponechávají různé
optické konstrukce a jiné postupy. [NASA, část Coronagraph][methods]
**OK.** V diagramu neslibovat odstranění všech zbytků záře ani dostupnost
libovolně blízké planety; přístroj má omezenou vnitřní pracovní vzdálenost.

## S09b — CTA
*Kotva: „consider subscribing“*

Standardní text z `docs/cta.md`, jediný výskyt. Není astronomickým
tvrzením; věta o pomoci kanálu je autorská výzva. **Zachováno.**

## S10–S12 — Bodový zdroj a jeho spektrum
*Kotva: „chemical fingerprints“*

- Přímý snímek neposkytuje mapu povrchu; spektrum však může nést informace
  o atmosféře. [NASA, Rise of Direct Imaging][methods]
- Nejde jen o budoucí možnost: spektrum přímo pozorovaného HR 8799 e
  umožnilo určit atmosférické chemické charakteristiky. [ESO][gravity]
- „Can look“, „potentially“ a „may contain“ už vyjadřují podmíněnost.
  Samotný bod vedle hvězdy není automaticky potvrzená planeta; věta
  popisuje kombinaci identifikace objektu a následné charakterizace.
  **OK bez dalšího zeslabování.**

## S13–S15 — Tranzit
*Kotva: „The star gets slightly dimmer“*

Planeta před hvězdným diskem blokuje část toku k pozorovateli; při opuštění
disku se tato složka poklesu ztratí. To je tranzit. [NASA, potvrzování][confirm]
„Easier trick“ je srovnání metody u vhodné geometrie, ne záruka snadné
detekce každé planety; omezení je výslovně v S22. **OK.** Hvězda přitom
nemění vlastní svítivost kvůli tomu, že ji planeta zakrývá.

## S16 — Pokles jasu pro Zemi před Sluncem
*Kotva: „zero point zero zero eight per cent“*

Pro rovnoměrně svítící disk a planetu plně promítnutou na jeho plochu:

```text
delta = (R_planet / R_star)^2
R_Earth = 6 371 km; R_Sun = 695 700 km
delta = (6371 / 695700)^2 = 0.0000838631562673
100 * delta = 0.00838631562673 %
1e6 * delta = 83.8631562673 ppm
```

Vzorec: [NASA Exoplanet Archive, Transit Depth][poe]. Poloměry:
[NASA Sun Fact Sheet, volumetrické střední poloměry][sun].
Výpočet proveden Pythonem, nikoli převzatý odhad.

**OK:** „about 0.008 per cent“ je správné zaokrouhlení. Není to 0,008
jako zlomek ani 0,8 %. Skutečná křivka závisí na okrajovém ztemnění,
dráze přes disk a pásmu měření; scénář netvrdí přesnou hodnotu každého
tranzitu kolem libovolné hvězdy slunečního typu.

## S17 — Měřítko malého signálu
*Kotva: „in twelve thousand“*

**Upraveno v 0.2.** Přirovnání člověka před reflektorem ze vzdálenosti
tisíců kilometrů nemělo rozměry ani geometrii a nedokládalo uvedený
relativní pokles. Není nutně nemožné, ale jako fyzikální měřítko neurčité.
Nahrazeno podílem odvozeným ze stejného výpočtu:

```text
1 / delta = 11 924.1875
1 / 12000 = 0.0000833333 = 0.00833333 %
```

„About one part in twelve thousand“ je přesné na úrovni zaokrouhlení.
Detekovatelnost malých poklesů dokládá úspěch tranzitních průzkumů;
nejde o tvrzení o každém dalekohledu a každé hvězdě. [Kepler][kepler]

## S18 — Kandidát a falešné pozitivní signály
*Kotva: „A planet candidate“*

Pravidelné poklesy samy nedokazují planetu. Zákrytová dvojhvězda může
signál napodobit, stejně jako další astrofyzikální nebo přístrojové
vlivy. Scénář je správně rozlišuje. [NASA, kroky 3–4][confirm]
**OK.** Nevyžaduje se, aby každá planeta byla nutně potvrzena radiálními
rychlostmi; validace může využít i jiné důkazy.

## S19–S20 — Perioda, poloměr, tvar a trvání
*Kotva: „the planet's orbital period“*

- Rozestup po sobě následujících tranzitů téže planety udává periodu.
  Navazuje na vyloučení falešných příčin v S18. Zmeškané průchody mohou
  způsobit násobek periody; planetární interakce odchylky časů.
- Hloubka určuje především poměr poloměrů, ne samotný poloměr planety.
  Přesně to text říká; znalost velikosti hvězdy doplní S32. [NASA][confirm]
- Trvání a tvar omezují geometrii průchodu. Primární analýza WASP-80 b
  například fituje sklon a poměr velké poloosy k poloměru hvězdy
  společně s tranzitními parametry. [Bell et al., Methods][methane]
- **OK:** „can reveal additional information“ neslibuje jednoznačnou
  úplnou rekonstrukci dráhy z jedné křivky.

## S21 — Kepler a TESS
*Kotva: „such as Kepler and TESS“*

Obě mise využívají tranzitní fotometrii velkého počtu hvězd, nikoli
rozlišené fotografie planet. [NASA, metody][methods]
Keplerův historický výsledek zahrnuje tisíce potvrzených planet a sledování
statisíců hvězd. [NASA, Kepler's Legacy][kepler]
**OK:** neříkáme, že TESS sám potvrdil tisíce planet, a nezaměňujeme
kandidáty za potvrzené objevy. Kepler není popisován jako stále pracující.

## S22–S23 — Orientace dráhy
*Kotva: „never transit at all“*

K tranzitu je třeba dostatečně přesné promítnutí dráhy před disk hvězdy.
Nepřítomnost tranzitu neznamená nepřítomnost planety. [ESA][esa]
Radiální rychlosti mohou planetu najít i při sklonu, který tranzit
neumožňuje, ale mají vlastní závislost na sklonu. [Archive][poe]
**OK.** „Never“ zde označuje danou pozorovací geometrii, nikoli zákaz
dlouhodobé precese dráhy.

## S24–S26 — Společné těžiště
*Kotva: „their common centre of mass“*

V izolovaném dvoutělesovém systému obíhají obě složky kolem společného
těžiště. [NASA, Gravity & Mechanics][barycentre]
Z definice těžiště `M_star*r_star = M_planet*r_planet`, tedy při
`M_star >> M_planet` leží těžiště mnohem blíže hvězdě než planetě.
Nemusí být uvnitř hvězdy; scénář to netvrdí. U více planet se pohyby
skládají. **OK jako základní model.** „Tiny amounts“ je relativní popis,
ne jednotná číselná amplituda.

## S27–S28 — Spektrograf, absorpce a Dopplerův jev
*Kotva: „towards shorter wavelengths“*

- Spektrograf rozkládá světlo podle vlnové délky. Atomy a molekuly
  absorbují na charakteristických vlnových délkách či v pásmech, takže
  ve spektru mohou vznikat tmavé čáry. [NASA, Spectroscopy 101][spectra]
- Pohyb k pozorovateli posouvá čáry ke kratším vlnovým délkám,
  pohyb od něj k delším; měří se radiální složka rychlosti. [ESA][esa]
- **OK.** Hvězda v ilustraci nemá doslova modrat a červenat jako semafor;
  zobrazit posun čar vůči referenci a přiznat zvětšení měřítka.

## S29–S31 — Radiální rychlost a minimum hmotnosti
*Kotva: „unless the orbital inclination is known“*

Opakovaný posun může být planetární reflexní pohyb, ale není to jediná
možná příčina. „May“ a „one possible explanation“ jsou správně.
Perioda a amplituda rychlostní křivky spolu s parametry hvězdy umožní
odvodit hmotnostní omezení. [Archive, RV semi-amplitude][poe]

Pro Keplerovskou dvoutělesovou dráhu:

```text
K = (2*pi*G/P)^(1/3) * M_p*sin(i) / (M_star+M_p)^(2/3)
    / sqrt(1-e^2)
```

Při `M_p << M_star` měření určuje `M_p*sin(i)`; protože `sin(i) <= 1`,
jde bez znalosti sklonu o minimální hmotnost. Přesněji se řeší hmotnostní
funkce. [NASA HEASARC, Planet_Mass][mass]
**OK:** nemusíme přidávat rovnici do narace. Eccentricita se fituje
z celé křivky; „size of the star's motion“ v tomto kontextu znamená
amplitudu radiální rychlosti, nikoli úhlovou velikost dráhy na snímku.

## S32–S33 — Kombinace metod a hustota
*Kotva: „we can calculate density“*

Tranzit poskytuje relativní poloměr a omezení sklonu, známý poloměr
hvězdy dovolí určit poloměr planety. RV pak s tímto sklonem a hmotností
hvězdy poskytne hmotnost. [NASA][confirm], [HEASARC][mass]
Pro přibližně kulovou planetu je střední hustota
`rho = M / ((4/3)*pi*R^3)` — vlastní geometrické odvození z definice hustoty.
**OK.** U plynné planety je měřený tranzitní poloměr navázaný na vrstvu
atmosféry, ne na pevný povrch; graf nemá slibovat přesnou hranici jádra.

## S34–S35 — Složení z hustoty
*Kotva: „density alone cannot tell us“*

Vysoká hustota může odpovídat horninám a kovům, nižší podílu vody nebo
výraznému plynnému obalu. Různá složení a struktury mohou mít tutéž
hmotnost a poloměr. [Rogers & Seager 2010][interiors]
Voda v nitru nemusí být led; její stav závisí na tlaku a teplotě.
Modely Kepler-138 například zahrnují vysokotlakou a superkritickou vodu.
[NASA][water]

**Zpřesněno v 0.2:** „gas or ice“ → „water or gas“ a přidána jediná věta,
že samotná hustota přesné složení neurčí. Původní „could indicate“ není
samo chybné, ale nová formulace odstraňuje domněnku o skupenství
a výslovně odpovídá připomínce. Nejde o tvrzení, že všechny málo husté
planety mají vodu nebo pevné jádro.

## S36–S37 — Metody se doplňují
*Kotva: „different parts of the puzzle“*

Shrnutí předchozích odvození: různé observably omezují různé parametry.
Mikročočka nevyžaduje tranzit před vlastní hvězdou ani měření jejího
Dopplerova posunu; potřebuje jinou, náhodnou geometrii. [ESA][esa]
„Powerful“ a „stranger“ jsou autorská hodnocení. **OK.**

## S38–S40 — Čočkování a planetární anomálie
*Kotva: „an additional distortion“*

Hmotnost hvězdy v popředí ohýbá světlo vzdálenějšího zdroje; při vhodném
průchodu poblíž zorného paprsku se zdroj dočasně zesílí. Planeta může
vytvořit další odchylku světelné křivky. [NASA Roman][lensing]
**OK.** „Passes in front“ označuje projekci na oblohu, ne neprůhledné
zakrytí zdrojové hvězdy jako při tranzitu. Nejde ani o větší vyzařovaný
výkon zdrojové hvězdy. „Anomaly“ je vhodnější než povinný kladný druhý
vrchol. V obraze označit zdrojovou hvězdu a čočku odlišně.

## S41 — Co mikročočkování doplňuje
*Kotva: „difficult to detect by other methods“*

Metoda pokrývá oblast hmotností a orbitálních vzdáleností doplňující
Kepler a TESS; zahrnuje i volně plující planety. [NASA, technický popis
Galactic Bulge Time-Domain Survey][roman-survey]
**OK:** scénář netvrdí, že jiné metody tyto objekty nemohou najít vůbec,
ani neuvádí datum či počet budoucích objevů Romanu.

## S42–S43 — Neopakující se geometrie
*Kotva: „a rare cosmic coincidence“*

Mikročočkování stojí na náhodném průchodu dvou nezávisle se pohybujících
systémů; na rozdíl od orbitálních tranzitů se pozorovací událost zpravidla
nedá periodicky zopakovat. [ESA][esa]
**OK:** „may happen only once“ je přiměřené. Neznamená to, že pozdější
pozorování nemůže potvrdit vlastnosti čočky nebo oddělit hvězdy;
takový následný rozbor byl proveden Hubbleem a Keckem. [NASA][followup]

## S44–S46 — Transmisní spektroskopie
*Kotva: „during a transit“*

Malá část pozorovaného hvězdného světla prochází atmosférickým prstencem
planety. Absorpce závisí na vlnové délce; porovnání tranzitních a
mimotranzitních dat umožní vytvořit transmisní spektrum.
[NASA, pozorování WASP-39 b][co2]
Atomy a molekuly mají charakteristické spektrální znaky. [NASA][spectra]
**OK:** „sometimes“ a „may“ správně omezují možnost měření. Změny
se modelují i s aktivitou hvězdy, šumem a systematikou přístroje;
samotný rozdíl dvou snímků automaticky neurčuje chemické složení.

## S47 — Voda, oxid uhličitý, metan a sodík
*Kotva: „depending on the planet“*

| látka | konkrétní doklad |
|---|---|
| Vodní pára, H2O | Transmisní spektrum WASP-80 b, Bell et al.; detekce spolu s metanem. [Studie][methane] |
| Oxid uhličitý, CO2 | Spektrální znak WASP-39 b v infračervené oblasti. [NASA][co2] |
| Metan, CH4 | WASP-80 b; nezávislé redukce a různé modelové přístupy podporují detekci. [Bell et al. 2023][methane] |
| Sodík, Na | Absorpce na čarách Na D v transmisním spektru HD 209458 b. [Snellen et al. 2008][sodium] |

**OK beze změny:** „can reveal the fingerprints“ mluví o spektrálních
stopách, ne o vševědoucím rozboru všech atmosfér. Závěr výčtu správně
říká, že záleží na planetě a pozorování; netvrdí, že všechny čtyři látky
byly detekovány na jediném tělese. Sodík je atomární druh, ne molekula.

## S48 — Slabý signál bez rozlišeného snímku
*Kotva: „in an ordinary image“*

WASP-80 b není od své hvězdy přímo prostorově rozlišen ani Webbem,
přesto jeho tranzit a zákryt poskytují atmosférické spektrum.
[NASA, vysvětlení autory výzkumu][methane-nasa]
**OK:** „modern instruments can measure them“ je existenční tvrzení
o dosažených detekcích, nikoli záruka pro libovolnou planetu.

## S49–S51 — Rekapitulace detekčních účinků
*Kotva: „we detect their effects“*

Každá položka už je ověřena výše: S15 tranzitní pokles; S25 reflexní
pohyb hvězdy; S38–S40 gravitační čočka; S44–S47 atmosférická absorpce.
Převaha nepřímých objevů nad přímými snímky je doložená. [ESA][esa]
Atmosférická analýza je zde charakterizace známé planety, ne tvrzení
o samostatné hlavní metodě prvotního objevu. **OK.**

## S52–S53 — Skutečný důkaz není barevná fotografie
*Kotva: „A microscopic shift in a spectral line“*

Shrnutí týchž čtyř observablů. Doložené detekce jsou i ve vzdálenosti
stovek světelných let: například WASP-39 b přibližně 700 světelných let.
[NASA][co2]
„Microscopic“ znamená velmi malý, nikoli konkrétní mikrometrový posun.
„A few missing wavelengths“ je popularizační zkratka pro deficit světla
na určitých vlnových délkách, nikoli nulový počet fotonů. [NASA][spectra]
**OK se správným vizuálem:** kreslit mělké absorpční deficity, ne
celé vymazané barvy spektra a ne skutečně vyfotografovaný modrý povrch.

## S54–S55 — Rekonstrukce světa a závěrečná metafora
*Kotva: „the consequences of being there“*

- Dráha, velikost, hmotnost, hustota a někdy atmosféra jsou parametry,
  které různé kombinace dat opravdu omezují, viz S19–S20, S31–S35,
  S44–S47. Ne všechny známe u každé jednotlivé planety.
- „Reconstruct an entire world“ zůstává autorskou metaforou fyzikálního
  modelu, nikoli přesnou mapou povrchu či jednoznačným složením nitra.
- „Across the galaxy“ označuje mezihvězdnou cestu světla v Galaxii,
  nikoli měření přes celý galaktický průměr. Scénář má sám příklady
  desítek a stovek světelných let.
- „Cannot completely hide“ vyjadřuje existenci fyzikálních účinků,
  nikoli schopnost dnešních dalekohledů nalézt úplně každou planetu.
  Výběrová omezení byla uvedena v S07, S22 a S31.
- **Zachováno podle autorského záměru a zpětné vazby.** Vizuál posledních
  scén nesmí z metafory dělat tabulku úplných dat u každé exoplanety.

## Zdroje

Odkazy v jednotlivých sekcích ukazují přímo na podpůrný dokument.
Zdroje k původní verzi byly otevřené již při přípravě 0.1; ostatní při
tomto průchodu. Výpočty jsou vlastní a vstupní konstanty jsou doložené.

[methods]: https://science.nasa.gov/exoplanets/how-we-find-and-characterize/
[confirm]: https://science.nasa.gov/solar-system/10-steps-to-confirm-a-planet-around-another-star/
[esa]: https://www.esa.int/Science_Exploration/Space_Science/Exoplanets/How_to_find_an_exoplanet
[poe]: https://exoplanetarchive.ipac.caltech.edu/docs/poet_calculations.html
[sun]: https://nssdc.gsfc.nasa.gov/planetary/factsheet/sunfact.html
[kepler]: https://science.nasa.gov/exoplanets/keplerscience/
[gravity]: https://www.eso.org/public/news/eso1905/
[barycentre]: https://science.nasa.gov/learn/basics-of-space-flight/chapter3-3/
[spectra]: https://science.nasa.gov/mission/webb/science-overview/science-explainers/spectroscopy-101-how-absorption-and-emission-spectra-work/
[mass]: https://heasarc.gsfc.nasa.gov/W3Browse/all/exoplanets.html
[interiors]: https://arxiv.org/abs/0912.3288
[water]: https://science.nasa.gov/universe/exoplanets/two-super-earths-may-be-mostly-water/
[lensing]: https://science.nasa.gov/mission/roman-space-telescope/microlensing/
[roman-survey]: https://science.nasa.gov/mission/roman-space-telescope/galactic-bulge-time-domain-survey-technical/
[followup]: https://science.nasa.gov/missions/hubble/telescopes-team-up-to-find-distant-uranus-sized-planet-through-microlensing/
[co2]: https://science.nasa.gov/missions/webb/nasas-webb-detects-carbon-dioxide-in-exoplanet-atmosphere/
[methane]: https://arxiv.org/abs/2309.04042
[methane-nasa]: https://science.nasa.gov/blogs/webb/2023/11/22/nasas-webb-identifies-methane-in-an-exoplanets-atmosphere/
[sodium]: https://arxiv.org/abs/0805.0789
