# Fact check — 042 „AI Didn't Start With ChatGPT"

Ověřeno 2026-09-12 proti `script 0.1.md` po dramaturgickém zamčení; opravy jsou v `script 0.2.md`.
Prošlo **každé** ověřitelné tvrzení scénáře, ne jen ta riziková — včetně
vět, které **vznikly až draftem** a v dodaném textu nebyly.

**Výsledek: 9 oprav zapsáno do scénáře, 3 věci zůstávají jako vědomé
zjednodušení** (níž v kapitole „Co jsme nechali").

---

## S01, S03, S47 — ChatGPT, konec listopadu 2022

> *„At the end of November 2022, a web page appeared with a small box
> on it."* / *„On the 30th of November 2022, OpenAI put a text box
> on a web page."*

ChatGPT byl zveřejněný **30. listopadu 2022**, tedy poslední den měsíce.
Přepočítáno: **byla to středa**, což sedí s Altmanovým *„ChatGPT launched
on wednesday"* z 5. 12. 2022.

✅ **Sedí.** *„At the end of November"* je záměrné — dodaný text měl
*„In November 2022, millions of people…"*, jenže milionty přišly
až v prosinci (viz S49b). Zkratka opravena už při převodu.

## S04b, S48b, S58 — „Fifty-six years earlier"

1966 → 2022 = **56 let**. Přepočítáno, ne odhadnuto.
Táž kontrola u zbylých dvou rozdílů ve scénáři:

| scéna | tvrzení | výpočet |
|---|---|---|
| S11 | *„Sixteen years earlier"* (od 1966 k Turingovi) | 1966 − 1950 = **16** ✅ |
| S16 | *„Six years after Turing's paper"* | 1956 − 1950 = **6** ✅ |
| S10 | *„the next half century"* | 1966 → 2022 je 56 let, tedy „půlstoletí" s rezervou ✅ |

## S05 — ELIZA, 1966, Joseph Weizenbaum, MIT

> *„In 1966, a researcher at MIT called Joseph Weizenbaum published
> a program called ELIZA."*

Weizenbaum byl na MIT ✅. Článek *„ELIZA — A Computer Program For the
Study of Natural Language Communication Between Man and Machine"* vyšel
v **Communications of the ACM, leden 1966** ✅.

> ⚠️ **Opraveno.** Draft původně říkal *„finished a program"*. ELIZA se
> vyvíjela zhruba **1964–1967**, takže „dokončil v roce 1966" není
> pravda — 1966 je rok **publikace**. Změněno na *„published"*.

> 🎨 **Pro storyboard, doplněno 2026-09-13 po stažení archivu:** snímek
> v `images/S05.png` je **z roku 1982**, ne z roku 1966 (`File:Weizenbaum
> 1982.jpg`, Rochester Institute of Technology, public domain, datováno
> 28. 10. 1982). Scéna mluví o roce 1966, takže **k té fotce se nesmí
> napsat 1966** — ani popiskem, ani nadpisem. Portrét osoby datum věty
> nedokládá a nemá ho tvrdit.

## S06 — ukázková výměna

> *„He says I'm depressed much of the time."* →
> *„I am sorry to hear you are depressed."*

✅ Z přepisu otištěného ve Weizenbaumově článku z roku 1966 (čtvrtá
výměna ukázkového rozhovoru) — **s jednou vynucenou úpravou, viz níž**.

> ⚠️ **„He says" → „My boyfriend says" (2026-09-13).** V článku zní ta
> replika doslova *„He says I'm depressed much of the time."*, jenže
> „he" tam ukazuje na **předchozí** repliku rozhovoru:
>
> | uživatel | ELIZA |
> |---|---|
> | *Well, my boyfriend made me come here.* | YOUR BOYFRIEND MADE YOU COME HERE |
> | *He says I'm depressed much of the time.* | I AM SORRY TO HEAR YOU ARE DEPRESSED |
>
> Video ukazuje jen druhou dvojici, takže divák nemá jak vědět, kdo je
> „he" — nahlásil to uživatel po přečtení titulku 12. Zájmeno je proto
> **rozvinuté o svůj antecedent**; věta nic nového netvrdí a zůstává
> v duchu originálu, ale **už to není citace slovo od slova** a tenhle
> odstavec je tu proto, aby se to dalo zpětně poznat.
>
> Plný kontext (obě dvojice) by byl autentičtější, ale nevešel by se:
> čtyři repliky potřebují čtyři bloky textu a **okno je páteř videa,
> takže se nesmí zvětšit**.

> ⚠️ **Opraveno, a je to nejdůležitější oprava tohohle typu.**
> Dodaný text i draft 0.1 měly *„I feel depressed."* → *„Why do you say
> you feel depressed?"*. Je to **věrohodně znějící rekonstrukce, ne
> citace** — kdo si otevře původní článek, tuhle výměnu tam nenajde.
> Nahrazeno doloženou. Vyšlo to i líp: *„I am sorry to hear"* je přesně
> ta věta, kvůli které lidé ELIZE přisuzovali porozumění.

> 🎨 **Pro storyboard:** v článku jsou **odpovědi stroje vysázené
> VERZÁLKAMI** (*„The capitalized lines are the machine responses"*).
> Diagram S06 to má dodržet — je to dobový detail zdarma.

## S07, S08 — jak ELIZA fungovala

> *„It was not a neural network. It understood nothing at all."*
> *„It matched keywords in what you typed and handed the rest back
> as a question."*

✅ **Sedí.** ELIZA pracovala s klíčovými slovy, jimž skript přiřazoval
prioritu, s **dekompozičními** pravidly (rozložení věty na části)
a **reassembly** pravidly (sestavení odpovědi). Žádná neuronová síť,
žádná reprezentace významu.

> ⚠️ **Opraveno: „A few hundred rules." vypadlo.** Hledal jsem doklad
> počtu pravidel skriptu DOCTOR ve Weizenbaumově článku, na
> `findingeliza.org` i v přepisech implementací — **nikde není**.
> Číslo, které nejde doložit, do scénáře nepatří (a do fact checku už
> vůbec ne). Nahrazeno doložitelným: *„The whole script fitted in the
> appendix of a journal paper."* — skript DOCTOR je otištěný jako
> **příloha článku z roku 1966**. Táž změna musela projít i do S58,
> kde je callback (*„a few pages of pattern matching"*).

## S09, S09b, S58 — sekretářka

> *„Weizenbaum's own secretary had watched him build it. She knew
> exactly what it was. After a few exchanges with it, she asked him
> to leave the room."*

✅ **Sedí, a je to doslova Weizenbaumova vlastní historka** z knihy
*Computer Power and Human Reason* (1976):

> *„Once my secretary, who had watched me work on the program for many
> months and therefore surely knew it to be merely a computer program,
> started conversing with it. After only a few interchanges with it,
> she asked me to leave the room."*

Weizenbaum k tomu dodává: *„What I had not realized is that extremely
short exposures to a relatively simple computer program could induce
powerful delusional thinking in quite normal people."* — to je přesně
otázka, kterou video klade v S10b.

> ⚠️ **Opraveno.** Draft měl *„After a few minutes at the keyboard"*.
> Weizenbaum píše *„after only a few interchanges"*, tedy o **počtu
> replik**, ne o čase. Změněno na *„After a few exchanges with it"*.
> Je to zároveň kratší.

> 💬 **Do komentářů:** zdroj je kniha z roku 1976, ne článek z roku
> 1966. Kdo bude hledat v článku, nenajde to.

## S11, S11b, S12, S13 — Turing 1950

> *„In 1950, the British mathematician Alan Turing opened a paper with
> a question."* / *„Can machines think?"*

✅ Článek **Computing Machinery and Intelligence**, časopis *Mind*,
**říjen 1950**. První věta zní *„I propose to consider the question,
'Can machines think?'"* — citovaná otázka je tedy pravá a je opravdu
v první větě.

> ⚠️ **Opraveno.** Draft říkal *„opened a paper with a single sentence"*
> a pak citoval jen otázku, což tvrdí, že první věta je *„Can machines
> think?"*. Není — je delší. Změněno na *„opened a paper with
> a question"*, čímž citace platí přesně.

> *„He decided the question was too vague to answer, and swapped it
> for a different one."* ✅ Turing tu otázku odmítá jako nevhodně
> položenou a nahrazuje ji imitační hrou.

> ⚠️ **Vědomé zjednodušení, viz níž:** S13 popisuje test jako
> **člověk versus stroj**. Turingova *původní* imitační hra je muž
> versus žena a teprve pak se ptá, co se stane, když roli A převezme
> stroj.

## S16, S17 — Dartmouth

> *„Six years after Turing's paper, a group of scientists spent the
> summer at Dartmouth College. Their proposal used a phrase that nobody
> had written down before. Artificial intelligence."*

✅ **Dartmouth Summer Research Project on Artificial Intelligence**,
léto **1956**. Návrh je datovaný **31. srpna 1955**, autoři McCarthy,
Minsky, Rochester a Shannon; **termín razí McCarthy právě v něm**
a je to doložitelně jeho první písemné užití.

> ⚠️ **Pozor na pořadí ve scénáři.** Věta jde „spent the summer…
> Their proposal", takže divák může návrh datovat do roku 1956, ačkoli
> je z roku 1955. Scénář žádný rok návrhu netvrdí, takže to není chyba
> — ale **diagram nesmí návrh označit rokem 1956**.

> *„If we could describe human intelligence precisely enough, we could
> program a machine to reproduce it."* ✅ Parafráze ústřední domněnky
> návrhu (*„every aspect of learning or any other feature of
> intelligence can in principle be so precisely described that
> a machine can be made to simulate it"*).

## S18b, S19, S20 — model neuronu. **Nejvíc přepsané místo scénáře.**

Tohle byl nález z rozboru dodaného textu, tys ho označil červeně
a ověření ukázalo, že obavy byly na místě.

| | doloženo |
|---|---|
| **1943**, McCulloch a Pitts | model neuronu: binární vstupy, **pevné** váhy a práh, žádné učení |
| **1957–58**, Rosenblatt | perceptron: váhy, které se **stroj naučí sám**, plus bias |

Dodaný text měl obojí slité do jedné věty **zasazené do roku 1956**.
Vážený neuron, který se učí, ale v roce 1956 neexistoval.

**Scénář to teď říká přesně:**

| scéna | co říká | doklad |
|---|---|---|
| S18b | *„In 1943, a neurophysiologist and a logician wrote down a simple model of a biological neuron."* | McCulloch byl neurofyziolog, Pitts logik ✅ |
| S19 | *„It took a few numbers in. Gave each one a weight. Added them up. And decided whether to fire."* | vážený součet proti prahu — model z roku 1943 ✅ |
| S20 | *„Its weights were fixed by hand. Two years after Dartmouth, a psychologist built one that could work them out for itself."* | Rosenblatt byl psycholog; 1956 + 2 = **1958** ✅ |

> ⚠️ **Zbylá nepřesnost, vědomá:** Rosenblattova první zpráva
> o perceptronu je z ledna **1957**, slavný článek v *Psychological
> Review* z **1958** a stroj Mark I Perceptron z **1958–60**.
> *„Two years after Dartmouth"* tedy ukazuje na 1958, což je obhajitelné
> („built one" = ten stroj), ale není to jediné možné datum.

> 🎨 **A tady je ta past, kterou jsi pojmenoval: diagram to tvrzení
> zesílí, i kdyby to popisek neřekl.** Kresba S19 musí ukázat neuron
> s **pevnými** vahami (číslo u každého vstupu, žádná šipka zpětné
> vazby) a teprve S20 přidat učení. Kdyby S19 nakreslila učící se síť,
> vrátí video chybu, kterou jsme z textu právě vyškrtli.

## S21–S27 — proč to nefungovalo, AI winters

> *„Computers were slow. Memory was tiny. And there was almost nothing
> to learn from."* ✅ Nekvantifikované a v souladu s dobou.

> *„A computer could do arithmetic faster than every human who had
> ever lived."* — rétorická hyperbola, ne měřitelné tvrzení. Ponecháno
> vědomě, viz níž.

> *„The field went through long stretches that later earned a name.
> AI winters."* ✅ Dvě hlavní zimy se datují zhruba **1974–1980**
> a **1987–1993**; spouštěči byly zpráva **ALPAC (1966)**, **Lighthillova
> zpráva (1973)** a škrty DARPA v polovině 70. let, druhá pak rozpad trhu
> s lispovými stroji kolem 1987.

> **Scénář schválně neuvádí žádný rok** a mluví v množném čísle.
> To je záměr: dodaný text stavěl zimy hned za 60. léta, což by
> s Lighthillem 1973 nesedělo. **Do diagramu se tedy roky taky
> nepíšou**, leda ty správné.

## S28–S31 — 90. léta, obrat od pravidel k datům

> *„From the 1990s onwards, computers got dramatically faster and
> storage got cheap. And the world began producing enormous amounts
> of digital data."* ✅ Nekvantifikované, nesporné.

> *„What if we hand it the data and let it work out the rules?"*
> ✅ Přechod od symbolické AI ke strojovému učení; scénář nikde netvrdí
> konkrétní rok ani konkrétní osobu.

## S32–S35 — Deep Blue, 1997

> *„In 1997, a machine called Deep Blue beat Garry Kasparov, the world
> chess champion."*

✅ **11. května 1997**, odveta, **3½–2½**. První porážka úřadujícího
mistra světa strojem v zápase za turnajových podmínek.

> ⚠️ **Nuance pro komentáře, vědomě nezapracovaná:** v květnu 1997
> držel Kasparov titul **PCA / klasický**; **mistr světa FIDE byl
> Anatolij Karpov** (rozkol od roku 1993). Označení *„the world chess
> champion"* používá prakticky každý zdroj včetně IBM a bylo by divné
> se mu vyhýbat, ale kdo to v komentářích zvedne, **má kus pravdy**.

> *„It could not learn anything."* — Deep Blue neměl strojové učení
> v dnešním smyslu (prohledávání plus ručně navržená hodnoticí funkce),
> ale **koeficienty té funkce se ladily z velmistrovských partií**.
> Obhajitelné ve smyslu „při hře se nic nenaučil", ne absolutně.
> Ponecháno, viz níž.

## S36–S39 — AlexNet, 2012

> *„In 2012, a neural network called AlexNet was pointed at more than
> a million photographs."*

✅ ILSVRC 2012, tréninková sada **1,2 milionu** snímků.

> ⚠️ **Opraveno.** Draft říkal *„a million photographs"*, což číslo
> podstřeluje. Změněno na *„more than a million"*.

> *„It won by a margin that made the older approaches look finished."*
> ✅ Chyba top-5 **15,3 %** proti **26,2 %** druhého v pořadí, tedy
> o 10,9 procentního bodu — **relativní pokles chyby o 42 %**.
> Číslo ve scénáři schválně není (nese ho obraz), ale doklad je tady.

> *„Neural networks were older than most of the people working on
> them."* — rétorické. Perceptron je z roku 1958, takže o většině
> výzkumníků z roku 2012 to skoro jistě platí, **doložit se to ale nedá**.
> Ponecháno, viz níž.

## S41, S42 — transformer, 2017

> *„In 2017, a paper came out of Google with an odd title. Attention
> Is All You Need."*

✅ Vaswani a spol., **12. června 2017**, osm autorů. Sedm z nich
z Google Brain a Google Research, **osmý (Aidan Gomez) z Univerzity
v Torontu** — práce vznikla při jeho stáži v Google Brain.
*„Came out of Google"* tedy sedí.

> *„Almost everything you have heard of since then is built on it.
> GPT. BERT. Claude. Gemini."* ✅ Všechny čtyři jsou transformerové
> architektury.

## S43–S46 — GPT

> *„OpenAI began building a family of models called GPT. GPT-1.
> GPT-2. GPT-3."*

✅ GPT-1 **červen 2018** (*Improving Language Understanding by
Generative Pre-Training*), GPT-2 **únor 2019**, GPT-3 **květen 2020**.

> *„Each one was larger than the last and better at the same trick.
> Given some text, guess what comes next."* ✅ Popis autoregresivního
> jazykového modelu.

> *„And almost nobody used it."* / *„You needed an account, some
> documentation, and a reason."* ✅ GPT-3 byl do listopadu 2022
> dostupný přes API s čekací listinou, ne jako spotřebitelská aplikace.

## S48, S48b — „nebyl to první chatbot"

> *„And it certainly was not the first chatbot."* / *„ELIZA was doing
> that job fifty-six years earlier."*

✅ ELIZA je uváděná jako **jeden z prvních** chatbotů a jeden z prvních
programů, které se pokusily o Turingův test.

> ⚠️ **Opraveno.** Draft měl *„ELIZA had that job fifty-six years
> earlier"*, což ELIZU korunuje na **první** chatbot. Zdroje jsou
> opatrnější (*„one of the first"*). Změněno na *„was doing that job"*
> — tvrzení o ChatGPT tím zůstalo v platnosti a ELIZE se nic
> nepřiznává navíc.

## S49b — milion lidí za pět dní. **Tvoje červená položka.**

> *„Five days later, a million people had signed up."*

Doklad jsou dva veřejné příspěvky z **5. prosince 2022**:

| kdo | co napsal |
|---|---|
| Sam Altman | *„ChatGPT launched on wednesday. today it crossed 1 million users!"* |
| Greg Brockman | *„ChatGPT just crossed 1 million users; it's been 5 days since launch."* |

Přepočítáno: 30. 11. + 5 dní = **5. 12. 2022** ✅.

> ⚠️ **Opraveno, a měls pravdu, že na tom záleží.** Draft říkal
> *„a million people had tried it"*. OpenAI ale oznámilo **uživatele**,
> tedy **založené účty** — což není totéž co „lidé, kteří to zkusili"
> (jeden člověk může mít víc účtů; návštěvník bez účtu se nepočítá).
> Změněno na *„a million people had signed up"*, což je přesně to,
> co ta čísla znamenají.

> 💬 **Do komentářů:** je to **údaj od OpenAI, nikdy nezávisle
> auditovaný**. Video ho podává jako jejich oznámení a nic víc.

## S50 — přirovnání ke Googlu

> *„It is a little like saying the internet started with Google.
> It did not. Google just made it enormously easier to use."*

Přirovnání, ne tvrzení o datech. Web je z roku 1991, Google z roku
1998 — scénář ani jedno neuvádí, takže není co ověřovat.

## S54, S55 — „ani v roce 1956 se nezačínalo od nuly"

> *„The models of neurons were already written down."* ✅ 1943, viz S18b.
> *„Turing had already asked whether the question made sense."* ✅ 1950.
> *„And people had been telling stories about artificial minds for
> a very long time before that."* ✅ Nekvantifikované; golem, Frankenstein,
> R.U.R. a starší. Scénář nejmenuje nic konkrétního, takže se nedá minout.

## S56, S57 — přiznání syntetického hlasu: SCÉNY ODSTRANĚNY

**Uživatel je 2026-09-13 vyškrtl.** Tvrdily *„For the last ten minutes,
a synthetic voice has been reading you the history of artificial
intelligence. A human wrote the words. A model said them out loud."*
a byla to pravda o tomhle videu; ověřovat teď není co.

Zůstává to tu zapsané proto, že **s nimi padl i invariant**, který se
u tohohle videa hlídal: *„For the last ten minutes"* muselo začínat
v 9:00 nebo později. Kdyby se meta-moment někdy vracel, ta podmínka se
vrací s ním.

---

## Co jsme nechali jako vědomé zjednodušení

Tři věci, které **nejsou chyby**, ale kdyby je někdo v komentářích
zvedl, má se odpovědět, ne mazat:

| | kde | proč to tak zůstalo |
|---|---|---|
| **Turingův test jako „člověk versus stroj"** | S13 | původní imitační hra je muž versus žena a stroj do ní vstupuje až v Turingově druhém kroku. Video popisuje test tak, jak ho míní každý, kdo o něm mluví — a Turing tu variantu skutečně formuluje |
| **Kasparov jako „the world chess champion"** | S32 | v roce 1997 byl mistrem světa FIDE Karpov. Označení používá i IBM a vysvětlovat rozkol PCA by stálo scénu, kterou video nemá |
| **rétorické hyperboly** | S23 (*„faster than every human who had ever lived"*), S37 (*„older than most of the people working on them"*) | nedoložitelné přesně, ale ani jedno není číslo, které by si divák odnesl jako fakt |

## Co z toho plyne pro storyboard

Tři věci, které **kresba může pokazit, i když text je správně**:

1. **S19 — neuron s PEVNÝMI vahami.** Žádná zpětná vazba, žádné učení.
   Učení přichází až v S20. Tohle je celá ta oprava; diagram ji umí
   zrušit.
2. **S16 — dartmouthský návrh se nesmí označit rokem 1956.** Je z roku
   **1955**, konference je 1956.
3. **S26 — u AI winters se nepíšou roky**, leda 1974–1980 a 1987–1993.
   Scénář je schválně nedatuje.

A jedna věc zdarma: **S06 má mít ELIZINY odpovědi VERZÁLKAMI**, protože
tak jsou vysázené ve Weizenbaumově článku.

## Zdroje

| tvrzení | zdroj |
|---|---|
| Turing 1950, první věta, *Mind* | Wikipedia: *Computing Machinery and Intelligence* |
| ELIZA: datace, mechanismus, přepis rozhovoru, příloha se skriptem | Weizenbaum, *CACM* 9(1), leden 1966 — plný text na `courses.cs.umbc.edu/331/papers/eliza.html`; Wikipedia: *ELIZA*; `findingeliza.org` |
| sekretářka | Weizenbaum, *Computer Power and Human Reason* (1976), citováno na `sites.google.com/view/elizaarchaeology` a v New Republic, Smithsonian a History.com |
| Dartmouth: návrh 31. 8. 1955, McCarthy razí termín | `home.dartmouth.edu/about/artificial-intelligence-ai-coined-dartmouth`; *AI Magazine*, reprint návrhu |
| McCulloch–Pitts versus Rosenblatt | srovnávací přehledy modelů; Raschka, *Single-Layer Neural Networks and Gradient Descent* |
| Deep Blue 1997, 3½–2½, 11. 5. | Wikipedia: *Deep Blue versus Garry Kasparov*; `ibm.com/history/deep-blue` |
| AlexNet: 15,3 % / 26,2 %, 1,2 mil. snímků | Krizhevsky, Sutskever, Hinton, ILSVRC 2012 |
| *Attention Is All You Need*, 12. 6. 2017, autoři | `arxiv.org/abs/1706.03762` |
| GPT-1/2/3 data | Wikipedia: *GPT-2*, *GPT-3* |
| milion uživatelů za pět dní | Sam Altman a Greg Brockman na X, 5. 12. 2022 |
| AI winters, ALPAC 1966, Lighthill 1973 | Wikipedia: *AI winter* |
