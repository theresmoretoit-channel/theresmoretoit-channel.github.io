# 159 — fact check (scénář v0.3 → v0.4 tímto průchodem, v0.5 podle zpětné vazby, 2026-11-15)

Zdroje s odkazy jsou v `factcheck-zaklad.md`, plné rešerše v `reserse/`,
výpočty v `mereni/bell.py` → `mereni/vysledky.txt`. Tady jsou tvrzení
po scénách. **P** primární, **S** sekundární, **M** spočítáno agentem.
Nadpis nese ID scény a doslovný fragment, `grep` ho musí najít v té scéně.

## Opravy ve scénáři (v0.3 → v0.4)

| scéna | bylo | je | proč |
|---|---|---|---|
| S01 | *Its job was to make pairs of photons* | *One of its jobs was to make pairs of photons* | Micius měl tři hlavní pokusy: distribuci provázání, kvantovou distribuci klíče (sestupný svazek) a teleportaci (vzestupný); „its job“ tvrdí, že jen ten první — P |
| S28 | *closed the last big loopholes* | *closed the two biggest loopholes at once* | Delft zavřel skulinu lokality a detekce **současně**; skulina svobodné volby zůstává (principiálně ji zavřít nejde), takže „the last“ je přestřelené — P |
| S73 | *And they're linked exactly as tightly / as quantum mechanics allows.* | *And no quantum link, however perfect, / gets past eighty-five per cent.* | fotony Miciusu dosáhly S = 2,37, tedy **79,6 %** ve hře, ne kvantové maximum 85,4 %; původní věta tvrdila o skutečném pokusu, že dosáhl Tsirelsonovy meze — P, M |

## Opravy podle zpětné vazby (v0.4 → v0.5, `zpetna vazba 0.4.txt`)

| scéna | bylo | je | proč |
|---|---|---|---|
| S05 | *Assuming the universe has / one preferred frame of reference* | *…a preferred frame, / in which Earth moves slowly / compared to light* | Salart 2008 předpokládá i rychlost Země vůči té soustavě pod 10⁻³ c; podmínka má zaznít celá. „Slowly compared to light“ místo navrženého „very slowly“: vůči reliktnímu záření se Země pohybuje ~370 km/s (~1,2 × 10⁻³ c), což „velmi pomalu“ v běžném smyslu není — P |
| S55 | *Entanglement doesn't cross that line.* | *Entanglement doesn't let information / cross that line.* | provázání necestuje, takže nemůže nic „překročit“; překročit by mohla jen informace |
| S72 | *And between eighty-five and ninety-one per cent, we still don't have an accepted principle that explains why nature stops where it does.* | *So far, no agreed principle explains / why nature allows exactly / these correlations, and nothing stronger.* | jinak to vypadá, že princip představený v S71 (information causality) hned prohlásíme za neexistující. „So far“ místo navrženého „But“, protože S71 už „But“ začíná |

Po opravách **75 scén**, slabiky v `notes.md`.

## Po scénách

### S01 — „In 2016, China launched a satellite"
Micius (QUESS) vypuštěn **16. 8. 2016** z Ťiou-čchüanu (Ren a kol. 2017) — P.
„One of its jobs… pairs of photons and split them up“: zdroj provázaných
fotonů na palubě (~5,9 milionu párů/s), dva sestupné svazky — P.

### S02 — „twelve hundred kilometres away"
Stanice **Delingha** (Čching-chaj, 3 153 m) a **Lijiang** (observatoř
Gaomeigu, Jün-nan, 3 233 m), **1 203 km** (Yin a kol., Science 356, 1140,
2017) — P. „An observatory in one city… in another“: obě stanice nesou
jméno města, u kterého leží; Gaomeigu je observatoř, Delingha pozemní
stanice Purpurové hory. Pro divácké „observatory“ to stačí. ✅

### S03 — „linked more tightly / than anything ordinary allows"
Bellův test přes Micius: **S = 2,37 ± 0,09** proti klasické mezi 2,
1 167 pokusů za 1 059 s — P. Zavřena skulina lokality, detekční jen
předpokladem fair sampling (`reserse/res-experimenty.md:28`); „ordinary“
= předem připravené lokální hodnoty. ✅

### S04 — „between two villages / eighteen kilometres apart"
Salart a kol., Nature 454, 861 (2008): Satigny a Jussy u Ženevy, **18,0 km** — P. ✅

### S05 — „ten thousand times faster than light"
Táž práce: za předpokladu **jedné preferované soustavy**, vůči které se Země
pohybuje pod 1/1000 c, by vliv musel být **> 10 000 c** (nejlépe 54 000 c) — P.
Obě podmínky jsou ve větě („a preferred frame, in which Earth moves slowly
compared to light“, v0.5). ✅

### S06 — „a limit on something hypothetical"
Mez na rychlost **hypotetického** vlivu, ne naměřená rychlost čehokoli — P. ✅

### S08 — „takes up to twenty-two minutes"
Země–Mars nejvýš ~401 mil. km → **22,3 min** jednosměrně, nejméně
~54,6 mil. km → 3,0 min — M. ✅

### S09 — „Not ever, as far as physics knows"
No-communication theorem v rámci standardní QM (viz S41) — P. „As far as
physics knows“ přiznává, že je to věta uvnitř teorie. ✅

### S13 — „the answers match. / In the ideal case, every time"
U stejně nastavených detektorů je výsledek dokonale korelovaný v ideálním
stavu. Singlet dává **opačné** výsledky; „match“ je konvence označení
(rozhodnuto, v obraze přeznačení). U fotonových párů typu Φ⁺ je shoda
doslovná. ✅

### S14 — „In a letter to Max Born in 1947"
*„spukhafte Fernwirkungen“*, dopis Bornovi, **březen 1947** (Born–Einstein
Letters, cit. Mermin 1985) — P/S. V článku EPR 1935 výraz **není**.
„Never accepted that quantum mechanics was the complete story“: EPR 1935
a celá pozdní korespondence — P. ✅

### S16 — „had a colleague, Reinhold Bertlmann"
Bertlmann spolupracoval s Bellem v CERNu a nosil ponožky různých barev;
Bell, *Bertlmann's socks and the nature of reality*, J. Physique Colloques
42, C2-41 (1981) — P. ✅

### S17 — „See that one sock is pink"
Bellův text: *„the first sock is pink… the second sock will not be pink“* — P. ✅

### S19 — „In 1981, Bell used those socks"
Publikováno 1981, přednáška 17. 6. 1980 — P. ✅

### S20 — „from the physicist David Mermin"
Mermin, Physics Today 38(4), 38 (1985): dva detektory, přepínač **na tři
polohy**, světlo **červené nebo zelené** — P. ✅

### S22 — „the colours always match"
Mermin 1985: při stejné poloze vždy stejná barva — P. ✅

### S24 — „In five of them, the colours match"
Sada RRG: shoda v (1,1), (2,2), (3,3), (1,2), (2,1) = **5 z 9** — M. ✅

### S25 — „at least five times out of nine"
Výčet všech osmi sad: minimum **5/9** (RRR a GGG dají 9/9), platí i pro
směsi — M (`vysledky.txt`, odd. 1). ✅

### S26 — „exactly half"
Osy po 120°: stejná poloha shoda 1, různá ¼ → (3 + 6 · ¼)/9 = **1/2** — M,
P (Mermin 1985). ✅

### S27 — „since 1972"
Freedman & Clauser, PRL 28, 938 (1972), první test Bellovy nerovnosti
(CHSH, ne Merminovo zařízení — proto „gaps like this“) — P. ✅

### S28 — „closed the two biggest loopholes at once"
Hensen a kol., Nature 526, 682 (2015), Delft, 1,3 km, NV centra: lokalita
i detekce zavřeny v jednom pokusu (S = 2,42 ± 0,20); téhož roku Vídeň
a NIST — P. **Opraveno** z „the last big loopholes“, viz tabulka.
Nobel 2022: Aspect, Clauser, Zeilinger, *„for experiments with entangled
photons, establishing the violation of Bell inequalities…“* — P.
„For their own work“, ne za Delft ✅.

### S29 — „at least not in any way / that stays local"
Bellův teorém: předem dané lokální hodnoty jsou vyloučené **za předpokladu
nezávislé volby nastavení** (rozhodnuto: v obraze nebo popisku) — P. ✅

### S30 — „doesn't mean one particle / sends a signal"
Porušení Bellovy nerovnosti signál neimplikuje; Bohmova mechanika nelokální
vliv má, ale v kvantové rovnováze nesignalizuje — P/S. ✅

### S32 — „Zero or one, the result is random"
Bornovo pravidlo; u maximálně provázaného stavu má Alice 50 : 50 v každé ose — M. ✅

### S33 — „whether Alice measured at all"
Bobova statistika je 0,5, ať Alice měří, nebo ne — M (`vysledky.txt`, odd. 7). ✅

### S34 — „About five hundred zeros"
Binomické rozdělení, n = 1 000, p = ½: směrodatná odchylka ~16 — M. ✅

### S37 — „they have to send them, / at the speed of light or slower"
Korelace je vlastnost dvojice záznamů; porovnání vyžaduje klasický
kanál — P (Bennett 1993, obecně). ✅

### S38 — „She chooses how to set her detector"
Volba osy mění sdruženou statistiku P(a, b), ne Bobovu marginální — M. ✅

### S40 — „measuring it, turning it, / or leaving it alone"
P(Bob ↑) = 0,500000 pro „nic“, měření ve čtyřech osách i unitární
natočení — M (`vysledky.txt`, odd. 7). ✅

### S41 — „physicists proved it / around 1980"
Eberhard 1978 (Nuovo Cim. B 46, 392), Ghirardi, Rimini, Weber 1980
(Lett. Nuovo Cim. 27, 293), Bussey 1982, Page 1982 — P (metadata). ✅

### S43 — „Then Bob would get her bit / every time he measured"
Kdyby Alice vynutila ↑ v ose 0°, P(Bob ↑ v ose 0°) = 0, tedy
deterministicky opak = bit — M (`vysledky.txt`, odd. 7). ✅

### S44 — „It's part of the reason"
Formulace podle rozhodnutí uživatele — náhoda je **součástí** důvodu,
ne úplné vysvětlení (no-signaling navíc sám plnou slučitelnost
s relativitou nedokazuje, Simon–Bužek–Gisin) — P/S. ✅

### S46 — „who had won a Nobel Prize / ten years earlier"
Weinberg, PRL 62, 485 (1989); Nobel **1979** s Glashowem a Salamem — P. ✅

### S47 — „He wanted experiments to test it"
Abstrakt PRL 1989: rámec nelineárních korekcí **jako vodítko pro
experimenty**, ne tvrzení, že QM je nelineární — P. ✅

### S48 — „and found nothing"
Bollinger 1989 (⁹Be⁺, < 4 × 10⁻²⁷ vazebné energie na nukleon), Majumder
1990, Walsworth 1990 — P. ✅

### S49 — „In 1990, Nicolas Gisin showed"
Gisin, Phys. Lett. A 143, 1 (1990): Weinbergova teorie **s obvyklým
pravidlem měření** umožní signál — S (abstrakt nedostupný, popis
v Polchinském článku a u Simon–Bužek–Gisin). ✅

### S50 — „Instantly. / At any distance."
Gisin: signál libovolně rychlý, nezávislý na vzdálenosti — S. „Instantly“
je tu správně, protože jde o hypotetickou teorii, ne o náš svět. ✅

### S52 — „He called it the Everett phone"
Polchinski, PRL 66, 397 (1991): po úpravě, která blokuje signál přes EPR,
zbude komunikace mezi větvemi vlnové funkce; „Everett phone“ jeho vlastní
název (paměti arXiv:1708.09093) — P. ✅

### S53 — „Not every nonlinear theory / has to fail this way"
Kent 2005 (nesignalizující nelineární modely); linearita vynucená, jen
když zůstane zbytek formalismu (Simon–Bužek–Gisin 2001) — P. ✅

### S54 — „could arrive before it was sent"
Video 112, S37–S41b: tachyonický antitelefon — vlastní video. ✅

### S55 — „doesn't let information / cross that line"
Opraveno ve v0.5. No-signaling: provázání vytváří korelace, informaci
nadsvětelně nepřenese (S41) — P. ✅

### S56 — „needs two ordinary bits"
Bennett a kol., PRL 70, 1895 (1993): dva klasické bity nutné, jinak by
šlo signalizovat nadsvětelně — P. Odkaz na video 027 (*What Would
Teleportation Take*, S43–S45). ✅

### S57 — „indistinguishable / from noise"
Bez korekčních bitů je Bobův stav maximálně smíšený — P (Bennett 1993). ✅

### S60 — „except when both get question one"
CHSH jako hra: výhra, když a ⊕ b = x · y — M. ✅

### S61 — „win three times out of four"
Výčet 16 deterministických strategií: max S = 2 → **75 %** — M. ✅

### S62 — „experiments keep beating three in four"
p = (S + 4)/8: Micius S = 2,37 → **79,6 %**, Delft S = 2,42 → **80,3 %** — M, P.
„About eighty-five per cent“ = cos²(π/8) = 85,36 % — M. ✅

### S63 — „In 1980, Boris Tsirelson proved"
Cirel'son, Lett. Math. Phys. 4, 93 (1980): kvantově nejvýš 2√2 → **85,4 %** — P, M. ✅

### S64 — „In 1994, Sandu Popescu / and Daniel Rohrlich"
Found. Phys. 24, 379 (1994); ptali se, *„why they do not violate it more“* — P. ✅

### S65 — „It isn't a real device, / just mathematics"
PR box je matematický model, ne pozorovaný systém — P. ✅

### S67 — „Bob sees fifty-fifty, whatever Alice asks"
a ⊕ b = x · y pokaždé, a přesto P(Bob = 1) = ½ pro každé x — M (odd. 6). ✅

### S70 — „above about / ninety-one per cent"
Brassard a kol., PRL 96, 250401 (2006): nad (3 + √6)/6 ≈ **90,8 %** je
komunikační složitost triviální (každá distribuovaná funkce jedním bitem) — P.
Je to práh výsledku o komunikační složitosti, ne fyzikální mez. ✅

### S71 — „gives the same eighty-five point four limit"
Pawłowski a kol., Nature 461, 1101 (2009): information causality dá
Tsirelsonovu mez pro CHSH, ne celou kvantovou množinu; „almost quantum“
korelace (2015) splní všechny dosavadní principy — P. ✅

### S72 — „no agreed principle explains"
Popescu, Nature Physics 10, 264 (2014): *„The jury is still out“*;
Gallego 2011 (žádný princip jen pro dvě strany kvantovou množinu
neodvodí); „almost quantum“ korelace 2015 — P. Přeformulováno ve v0.5:
neříká, že princip pro 85,4 % neexistuje, nýbrž že žádný uznávaný princip
nevymezí **přesně** kvantové korelace. ✅

### S73 — „gets past eighty-five per cent"
**Opraveno**, viz tabulka. Nová věta je Tsirelsonova mez (S63). ✅

### S75 — otázka do komentářů
Bez faktického tvrzení.
