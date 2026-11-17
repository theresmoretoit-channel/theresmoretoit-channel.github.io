# Fact check — 031 What Does Death Feel Like?

Verze scénáře: **`script 0.4.md`**, 83 scén. Ověřeno 2026-09-07.

Tři číselné a jmenné kotvy prošel uživatel (`zpetna vazba 0.3.txt`)
a navrhl u dvou zpřesnění formulace. Tenhle soubor je **nezávislý
kontrolní průchod** přes všechna ověřitelná tvrzení, včetně těch, na které
se uživatel neptal, a včetně dvou nálezů navíc.

Fragment z každého nadpisu musí být doslova v uvedené scéně — kontrolu dělá
`kontrola_factcheck.py`, viz konec souboru.

---

## S06 — „A dim, shifting grey, delivered by a visual system that is still running"

**Tvrzení:** se zavřenýma očima nevidíš pravou černou, ale slabou šeď,
kterou vyrábí sám zrakový systém.

**Ověření:** jde o jev zvaný **eigengrau** (německy „vlastní šeď", též
*Eigenlicht*, „brain gray"). Vzniká tím, že rodopsin v tyčinkách
**spontánně izomerizuje tepelně**, tedy bez dopadu fotonu, a tyto události
jsou od skutečných fotonových zásahů nerozlišitelné. Šeď je vnímaná jako
světlejší než černý předmět za denního světla, protože zrakový systém
pracuje s kontrastem, ne s absolutním jasem.

**Závěr: ✅ platí, a je to silnější, než scénář říká.** Formulace
„delivered by a visual system that is still running" je doslova správná —
zdrojem je šum sítnice, ne zbytkové světlo.

Zdroj: [Eigengrau, Wikipedia](https://en.wikipedia.org/wiki/Eigengrau)

---

## S24 — „Neuroscientists have a phrase for it. Your brain is a prediction machine."

**Tvrzení:** mozek je popisován jako prediktivní stroj a to je zavedený
odborný rámec, ne autorská metafora.

**Ověření:** **prediktivní zpracování / prediktivní kódování** je mainstreamový
rámec kognitivní neurovědy (Fristonův princip volné energie; Andy Clark,
*Whatever Next? Predictive Brains, Situated Agents, and the Future of
Cognitive Science*, Behavioral and Brain Sciences 2013). Výraz „prediction
machine" se v té literatuře skutečně používá.

**Závěr: ✅ platí.** Scénář je záměrně opatrný („mají pro to výraz"),
netvrdí, že je věc uzavřená — a to je správně, protože prediktivní
zpracování je **rámec, ne měření**.

---

## S29 — „millions of people go through it every year. General anaesthesia."

**Tvrzení:** celkovou anestezií projdou každý rok miliony lidí.

**Ověření:** jen v NHS Spojeného království je to podle aktivitního
průzkumu NAP5 **2 766 600 celkových anestezií ročně** (viz S34).
Celosvětově je řádově víc.

**Závěr: ✅ platí s velkou rezervou.** „Millions" je podhodnocené, ne
nadhodnocené.

---

## S30 — „The brain isn't simply switched off. Parts of it stay active, still processing information"

**Tvrzení:** při celkové anestezii mozek nepřestane pracovat; části zůstanou
aktivní a zpracovávají informace, přestože vědomý zážitek zmizí.

**Ověření:** měřeno opakovaně a různými látkami. Pod propofolem
i ketaminem se ztrácí **dálková integrace** napříč více frekvenčními pásmy,
zatímco **lokální synchronie zůstává silně zachovaná**. Ferrarelli,
Massimini a spol. doložili rozpad efektivní kortikokortikální konektivity
při ztrátě vědomí navozené midazolamem.

**Závěr: ✅ platí.** Tatáž měření zároveň podpírají S41 („The integration
that produces conscious experience is gone") — to není řečnická figura,
nýbrž popis toho, co se naměřilo.

Zdroje: [Hudetz, General Anesthesia and Human Brain Connectivity, Brain
Connectivity 2012](https://journals.sagepub.com/doi/abs/10.1089/brain.2012.0107) ·
[Altered dynamical integration/segregation balance during anesthesia-induced
loss of consciousness, PMC10728865](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10728865/)

---

## S31 — „You can be unconscious for six hours."

**Tvrzení:** celková anestezie může trvat šest hodin.

**Ověření:** běžná délka velkých výkonů (kardiochirurgie, neurochirurgie,
rekonstrukční operace). Není to mezní ani rekordní hodnota.

**Závěr: ✅ platí.**

---

## S34–S35 — NAP5: tři miliony anestezií, jeden pacient z dvaceti tisíc

**Tvrzení ve scénáři** (po opravě níž):

> Britain gives around three million general anaesthetics a year.
> About one patient in twenty thousand reports being aware.

**Ověření, čtyři samostatná čísla:**

| co | zdroj | hodnota |
|---|---|---|
| incidence náhodného uvědomění | NAP5, souhrn hlavních zjištění | **~1 : 19 600** (95% CI 1 : 16 700 – 23 450) |
| počet celkových anestezií za rok | aktivitní průzkum NAP5 (Sury a spol., 2014) | **2 766 600** ročně, tedy 76,9 % všech výkonů |
| co se vlastně měřilo | NAP5 | *accidental awareness during general anaesthesia* — případy, které pacient **sám nahlásil** přes portál |
| pokrytí | NAP5 | **NHS celého Spojeného království**, 100% odezva nemocnic, 20 400 hlášení |

**Dva nálezy navíc, na které se uživatel neptal:**

**1. „Britain" versus „the UK".** Čísla jsou za NHS **celého Spojeného
království**, tedy včetně Severního Irska; „Britain" doslova znamená Velkou
Británii bez něj. Rozdíl je zhruba **tři procenta obyvatel**, což se
v zaokrouhlení „around three million" úplně ztratí (2,77 mil. → 2,85 mil.
by pořád byly „kolem tří milionů"). Navíc jde jen o NHS, soukromý sektor
v čísle není, takže skutečný počet je ještě o něco vyšší.
**Ponecháno; „around" tu odchylku pokrývá obousměrně.**

**2. „Remembers" je pořád o půl kroku vedle — správně je „reports".**
Tohle je podstatnější a uživatelovo zpřesnění to nechytilo celé. NAP5
počítal případy, které pacient **spontánně nahlásil**. Studie, které se
pacientů **cíleně ptají** (Briceův dotazník, opakovaně po dobu až 30 dnů),
nacházejí incidenci **1–2 na 1000 anestezií, tedy zhruba 1 : 500 až
1 : 1000** — o jeden a půl řádu víc. NAP5 ten rozdíl sám rozebírá
a vysvětluje ho právě metodou sběru.

> Věta „About one patient in twenty thousand **remembers** being aware"
> proto tvrdí víc, než z NAP5 plyne: dvacet tisíc je počet na jedno
> **nahlášení**, ne na jedno **vybavení**. Pedantický divák s Briceovým
> číslem v ruce má pravdu.
>
> **Opraveno na `reports being aware`.** Délka scény ani úder se nemění.

**Nemění to argument videa.** I ta vyšší, cíleným dotazováním zjištěná
incidence je 0,1–0,2 %, takže „subjektivní čas u drtivé většiny pacientů
prostě zmizí" platí u obou čísel. Kdyby se někdy chtělo použít to druhé
číslo, je stejně použitelné — jen se musí říct „when you ask them directly".

**Závěr: ✅ platí po opravě `remembers` → `reports`.**

Zdroje: [NAP5 summary of main findings and risk factors, BJA
2014](https://academic.oup.com/bja/article/113/4/549/2920161) ·
[NAP5 Baseline national survey of anaesthetists, BJA
2013](https://academic.oup.com/bja/article/110/4/501/359122) ·
[The state of UK anaesthesia: survey of NHS activity in 2013,
PubMed 25236896](https://pubmed.ncbi.nlm.nih.gov/25236896/) ·
[Accidental awareness under general anaesthesia, BJA
Education](https://www.bjaed.org/article/S2058-5349(20)30159-1/fulltext)

---

## S40 — „Cut the blood supply, and consciousness can be lost within about ten seconds."

**Tvrzení:** po zastavení přítoku krve do mozku se vědomí ztrácí zhruba
do deseti sekund.

**Ověření:** primárním podkladem jsou **Red Wing studies** — experimenty,
při kterých se dobrovolníkům nafukovací manžeta na krku (tlak 600 mmHg,
nafouknutí za osminu sekundy) zcela zastavila přítok krve do mozku.
Naměřeno: **přerušení už na 4 sekundy, nejpozději kolem 10 sekund, vedlo
ke ztrátě vědomí.** Celkem 129 subjektů.

**Závěr: ✅ platí, a formulace je po opravě bezpečná.** Původní znění
„and consciousness **is gone in** about ten seconds" znělo jako přesný
časovač; „**can be lost within** about ten seconds" pokrývá naměřený
rozptyl 4–10 s správným směrem.

> **Co se tvrdit NESMÍ:** deset sekund se týká **ztráty vědomí**, ne smrti
> mozku ani smrti. Formulaci typu „death occurs after ten seconds" scénář
> neobsahuje a obsahovat nesmí.

> **Etická poznámka k použití zdroje.** Red Wing studies probíhaly na
> vězních a chovancích nápravného zařízení; podle dnešních měřítek by
> neprošly. Číslo je doložené a nezávisle podpořené fyziologickou
> literaturou o globální zástavě mozkové perfuze, ale **studie se ve videu
> nejmenuje ani neukazuje** — a je to tak správně. Kdyby na ni někdo
> v komentářích narazil, tahle poznámka je odpověď.

Zdroj: [Experimental Arrest of Cerebral Blood Flow in Human Subjects:
the Red Wing studies revisited,
PMC3848716](https://pmc.ncbi.nlm.nih.gov/articles/PMC3848716/)

---

## S41 — „The integration that produces conscious experience is gone."

**Tvrzení:** vědomý zážitek závisí na integraci informací mezi částmi mozku
a s jejím rozpadem mizí.

**Ověření:** viz S30. Rozpad dálkové integrace při zachované lokální
aktivitě je opakovaně naměřený u anestezie i spánku a je jádrem hlavních
teorií vědomí (integrovaná informace, globální pracovní prostor).

**Závěr: ✅ platí.** Scénář netvrdí, kterou teorii má pravdu — jen to,
co se měří.

---

## S49 — „we have no reliable evidence for a consciousness that continues independently of the brain"

**Tvrzení:** negativní; neexistuje spolehlivý doklad pro vědomí přetrvávající
nezávisle na mozku.

**Ověření:** negativní tvrzení se nedokazuje, dokládá se **absencí opačného
dokladu**. Ta absence platí. Scénář zároveň nikde netvrdí, že je věc
vyřešená — má tam „Not yet, at least."

**Závěr: ✅ platí, a je správně formulované jako stav poznání, ne jako
metafyzický závěr.** Tohle je jediná věta, která ze čtyřscénové sekce
o duši ve verzi 0.2 zbyla, a nese celou její poctivost.

---

## S53 — „The universe can continue for billions or trillions of years."

**Tvrzení:** vesmír může pokračovat miliardy nebo biliony let.

**Ověření:** hvězdotvorná (stelární) éra se odhaduje řádově na 10¹⁴ let,
tedy stovky bilionů. „Billions or trillions" je tedy **podhodnocení
s rezervou**, ne nadsázka.

**Závěr: ✅ platí.**

> **Past pro překlad:** anglické *trillion* je 10¹², tedy česky **bilion**,
> německy `Billionen`, španělsky `billones`. Ne „trilion". Britská
> *billion* je 10⁹, tedy **miliarda**. Přepočítat, nepřepsat — viz
> „Past s číslovkami" v `CLAUDE.md`.

---

## S58 — „You didn't spend billions of years waiting to be born."

**Tvrzení:** před narozením uplynuly miliardy let.

**Ověření:** stáří vesmíru **13,8 miliardy let**.

**Závěr: ✅ platí.**

---

## S60–S61 — Lucretius

**Tvrzení ve scénáři:**

> And that argument is not new. A Roman poet wrote it down
> about two thousand years ago.
>
> Lucretius asked his readers to look back at the eternity before their
> birth, and to notice that it had cost them nothing.

**Ověření po částech:**

| část tvrzení | ověření |
|---|---|
| **římský básník** | Titus Lucretius Carus, římský básník a filozof, asi 99 – asi 55 př. n. l. ✅ |
| **„asi před dvěma tisíci lety"** | ~55 př. n. l. je od dneška **2 081 let**. „About two thousand years" ✅ |
| **kde to je** | *De rerum natura*, **kniha III**; jádro argumentu symetrie ve verších **832–842**, zrcadlová pasáž **972–975** ✅ |
| **obsah parafráze** | 3.972–975: *„Ohlédni se stejně tak, jak nekonečný čas před naším narozením pro nás nebyl ničím. Příroda nám tím nastavuje zrcadlo času, který přijde po naší smrti."* Scénářová parafráze („look back at the eternity before their birth… it had cost them nothing") tomu odpovídá ✅ |

**Závěr: ✅ platí ve všech čtyřech částech.**

> **Doplněk pro odpovědi v komentářích:** starším zdrojem téže myšlenky je
> **Epikúros, *List Menoikeovi*** („smrt pro nás není ničím"), asi o dvě
> století dřív. Scénář to netvrdí — říká jen „not new" a jmenuje Lucretia
> jako toho, kdo to **zapsal**, což sedí. Kdyby to někdo v komentářích
> namítl, má pravdu a video s ním není v rozporu.

Zdroje: [Warren, *Lucretius, Symmetry Arguments, and Fearing
Death*](https://www.faculty.umb.edu/adam_beresford/courses/phil_381_08/1_lucretius_death.pdf) ·
[De Rerum Natura Book III, překlad
Kline](https://www.poetryintranslation.com/PITBR/Latin/LucretiusDeRerumNaturaBkIII.php) ·
[Open Yale Courses PHIL 176, přednáška
18](https://oyc.yale.edu/philosophy/phil-176/lecture-18)

---

## S69 — „medicine can sometimes do a great deal to reduce them"

**Tvrzení:** medicína umí bolest, strach a zmatenost při umírání často
výrazně zmírnit.

**Ověření:** to je celý obor paliativní medicíny. Scénář je opatrný
dvakrát („sometimes", „a great deal to reduce", ne „odstranit"),
takže netvrdí, že to jde vždy — což by neplatilo.

**Závěr: ✅ platí, a opatrnost formulace je tu potřebná.**

---

## Tvrzení, která se ověřit nedají a ani nemají

Tohle je z podstaty filozofické video, takže velká část textu **není
faktické tvrzení**, nýbrž argument nebo myšlenkový pokus. Vypsáno, aby bylo
vidět, že se na ně nezapomnělo, a proč se u nich nic neověřovalo:

| scéna | co to je |
|---|---|
| S05–S11 | argument, že každý kandidát na „jaké to bude" propašuje pozorovatele — **logický, ne empirický** |
| S13–S16 | myšlenkový pokus se spánkem („Imagine falling asleep tonight") — uvozený jako představa |
| S17–S20 | pokus představit si nic — introspektivní výzva divákovi |
| S26 | `Me. Then death. Then time…` — popis toho, co dělá mysl, ne tvrzení o světě |
| S43 | *„Death is not a state you experience. It is the absence of experience."* — **hlavní teze videa**; plyne z S30, S40 a S41, ale sama je pojmovým závěrem |
| S44–S48 | počítačová analogie — přirovnání, výslovně uvozené „Here's a slightly morbid way of putting it" |
| S54, S75–S76 | symetrie a „no further point on your timeline" — argument |
| S79–S83 | závěr, hodnotový |

---

## Dvě vnitřní nesrovnalosti nalezené při téhle kontrole

Nejsou to faktické chyby o světě, ale chyby **uvnitř scénáře**, tedy přesně
to, co fact check chytit má:

| scéna | co bylo | proč to bylo špatně | opraveno na |
|---|---|---|---|
| **S42** | „And that is what **all four** of our answers missed." | kandidátů je **šest**: tma, ticho, prázdný pokoj, čekání, věčný spánek, černá obrazovka. Číslovka vznikla ve verzi 0.2 a přežila dva střihy | „And that is what **every one of those** answers missed." |
| **S71** | „A conscious brain **is even good** at imagining…" | „even" ztratilo protějšek, když se ve verzi 0.2 vyškrtla předchozí věta („very good at imagining 'I will be somewhere'"). Věta pak stupňuje proti ničemu | „A conscious brain **can even imagine**…" |

---

## Strojová kontrola

```bash
python videos/031-what-does-death-feel-like/kontrola_factcheck.py
```

Ověří, že fragment z každého nadpisu `## Sxx — …` je doslova ve scéně
`Sxx` ve `script.md`. Pouštět **po každém škrtu ve scénáři** — čísla scén
se posunou a evidence pak ukazuje na cizí tvrzení.
