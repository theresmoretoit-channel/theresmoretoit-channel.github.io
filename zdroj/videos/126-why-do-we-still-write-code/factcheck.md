# 126 — fact check (scénář 0.3, 2026-10-26)

Scény podle `script 0.3.md`. Závěr: ✅ doloženo, ✏️ opraveno ve scénáři,
💬 úvaha / argument (není faktické tvrzení, nemá zdroj, jen nesmí lhát).

## S01–S08 Háček a teze

| | tvrzení | ověření | |
|---|---|---|---|
| S01–S02 | *A user can cancel an order.* má šest slov | A·user·can·cancel·an·order = 6 | ✅ |
| S03–S05 | věta neodpovídá na fakturu, odeslání, dodavatele, souběh | příklad převzatý ze zdroje uživatele (blok 3 a 5) | 💬 |
| S07 | kód jako dnešní assembler, „nobody reads" | teze, se kterou končí 044; nadsázka, kterou S08 hned rámuje jako „idea" | 💬 |

## S09–S17 Historie

| | tvrzení | ověření | |
|---|---|---|---|
| S09 | „for **nearly** seventy years" | FORTRAN: projekt od léta 1954, článek 1957 → 69–72 let k 10/2026. Dřív „seventy", opraveno podle zpětné vazby 0.2 | ✏️ ✅ |
| S10 | 1957, tým z IBM, článek o FORTRANu, v titulu *automatic coding system* | Backus a kol., „The FORTRAN Automatic Coding System", Proc. Western Joint Computer Conference, únor 1957, s. 188–198 ([CHM 102663113](https://www.computerhistory.org/collections/catalog/102663113)); článek sám uvádí, že projekt začal v létě 1954 a cílil na IBM 704 | ✅ |
| S11 | píšeš vzorce, strojové instrukce vyrobí stroj | funkce překladače; „FORTRAN" = FORmula TRANslation. Dřívější výklad „to them FORTRAN wasn't programming" vypuštěn (nedoložená interpretace) | ✏️ ✅ |
| S13 | 80. léta: CASE nástroje a jazyky 4. generace, velká část aplikace se vygeneruje | CASE (computer-aided software engineering) a 4GL jsou typické pro 80. léta; termín 4GL zpopularizoval James Martin (1981/82 — v 044 je jeho kniha, tady se neopakuje). Formulace „much of the application", ne „builds itself" | ✏️ ✅ |
| S14 | 2001, Object Management Group, „the body behind UML", Model Driven Architecture | OMG odhlasovala MDA jako směr únor/březen 2001 ([tisková zpráva OMG 8. 3. 2001](https://oasis-open.org/cover/OMG-MDA2001-03-08a.htm)); UML 1.1 přijala OMG v listopadu 1997 a od té doby ho spravuje ([UML Partners](https://en.wikipedia.org/wiki/UML_Partners)) | ✅ |
| S15–S16 | popíšeš systém jednou jako model nezávislý na technologii, nástroje vygenerují implementaci pro libovolnou platformu | MDA: Platform-Independent Model → Platform-Specific Model → kód ([Wikipedia: MDA](https://en.wikipedia.org/wiki/Model-driven_architecture)) | ✅ |
| S17 | 2014, Forrester, platformy pro business aplikace s co nejmenším ručně psaným kódem, „low-code" | Richardson & Rymer, *New Development Platforms Emerge For Customer-Facing Applications*, Forrester 9. 6. 2014: „dramatically reducing the amount of hand-coding" ([Forrester RES113411](https://www.forrester.com/report/New-Development-Platforms-Emerge-For-CustomerFacing-Applications/RES113411)); pozdější definice Forresteru „a minimum of hand-coding". Rymer v rozhovoru 2016 potvrzuje, že termín razili oni ([SiliconANGLE](https://siliconangle.com/2016/05/21/analyst-gives-the-low-down-on-low-code-know16/)). Plné znění zprávy z 2014 je za paywallem — formulace scénáře se drží shrnutí | ✅ |

## S18–S27 Proč to nevyšlo

| | tvrzení | ověření | |
|---|---|---|---|
| S19 | 2014, výzkumníci z Lancaster University, průzkum mezi 450 lidmi, kteří MDE používají | Whittle, Hutchinson, Rouncefield (Lancaster University), *The State of Practice in Model-Driven Engineering*, IEEE Software 31(3), 2014: „surveyed 450 MDE practitioners and performed in-depth interviews with 22 more" — přečteno v plném textu | ✅ |
| S20 | funguje, rozšířenější, než se myslí; zřídka na celý systém; jen klíčové části | „although MDE might be more widespread than commonly believed, developers rarely use it to generate whole systems. Rather, they apply MDE to develop key parts of a system." Dřív „regular and repetitive parts … wrote the rest by hand" — to studie neříká | ✏️ ✅ |
| S21 | největší překážky jsou lidé a organizace, ne nástroje | abstrakt téže studie: adopce „largely depends on social and organizational factors". **Přidáno, protože 0.2 podávalo vtip jako DŮVOD neúspěchu**, kdežto studie ho vidí jinde | ✏️ ✅ |
| S22 | vtip: dost přesná specifikace už má jméno — kód | nepřipisuje se. Původ: CommitStrip, *A very comprehensive and precise spec*, 25. 8. 2016 ([odkaz](https://www.commitstrip.com/en/2016/08/25/a-very-comprehensive-and-precise-spec/)); rozvedeno v [Haskell for All, 17. 3. 2026](https://haskellforall.com/2026/03/a-sufficiently-detailed-spec-is-code). Myšlenka je starší (Bugtraq 2004). Punchline komiksu ověřena jen z druhé ruky | ✅ |
| S23–S24 | aby se vygenerovalo všechno, musí model říct všechno; diagram se hůř čte, porovnává a reviduje | argument, ne měření. „Often" drží míru jistoty | 💬 |
| S25 | konec 70. let, Dijkstra, krátký text *On the foolishness of „natural language programming"* | EWD 667, rok **1978**, „circulated privately" ([BibTeX index EWD archivu](https://www.cs.utexas.edu/~EWD/indexBibTeX.html)); tiskem 1979, LNCS 69 *Program Construction*. Tři strany | ✅ |
| S26 | formální notace není přítěž; „an amazingly effective tool for ruling out all sorts of nonsense" | přepis EWD 667: „formal symbolism … an amazingly effective tool for ruling out all sorts of nonsense"; „instead of regarding the obligation to use formal symbols as a burden, we should regard the convenience of using them as a privilege" ([EWD 667](https://www.cs.utexas.edu/~EWD/transcriptions/EWD06xx/EWD667.html)) | ✅ |

## S28–S36 Co je jinak

| | tvrzení | ověření | |
|---|---|---|---|
| S30 | starší generátory mezeru samy nevyplnily, pravidlo musel někdo doplnit výslovně | dřív „every older generator was literal", zmírněno podle zpětné vazby 0.2 (nástroje se lišily) | ✏️ 💬 |
| S31–S33 | AI dá odpověď na každou otázku, vyrobí běžící kód, projde testy, které sama napsala | popis chování dnešních modelů, ne konkrétní měření; „will" je tu podmíněné kontextem „give it the six-word requirement" | 💬 |
| S34–S36 | „a plausible guess is not a business decision"; mezery byly chyby, teď jsou rozhodnutí | věta ze zdroje uživatele; argument | 💬 |

## S37–S50 Repozitář specifikací a změna

| | tvrzení | ověření | |
|---|---|---|---|
| S37–S41 | Markdown, stavy, schémata, akceptační testy, Git, dohledatelnost | popis navrhovaného postupu (zdroj uživatele, blok 4) | 💬 |
| S42–S47 | změna pravidla rušení, dohledání dopadů, dotaz na člověka, kontrola oběma směry | **zamýšlený proces**, ne existující produkt; S46 „should", ne „must"; S47 dovětek „passing tests only shows what the tests check" (zpětná vazba 0.2) | ✏️ 💬 |
| S48 | tatáž specifikace → PHP dnes, něco jiného zítra | „could" — možnost | 💬 |
| S49 | slib MDA před 25 lety | 2001 → 2026 = 25 | ✅ |

## S51–S56 Ověřování: Amazon

Zdroj: Newcombe, Rath, Zhang, Munteanu, Brooker, Deardeuff, *Use of Formal
Methods at Amazon Web Services*, 29. 9. 2014 ([PDF](https://6826.csail.mit.edu/2019/papers/formal-methods-amazon.pdf));
rozšířená verze *How Amazon Web Services Uses Formal Methods*, CACM 58(4),
2015. **Přečteno v plném textu.**

| | tvrzení | ověření | |
|---|---|---|---|
| S52 | 2014 inženýři Amazonu popsali, jak začali psát přesné matematické popisy svých návrhů v jazyce TLA+ | ano; TLA+ (Lamport), u některých systémů PlusCal. Začali 2011 — scénář říká jen, kdy to **popsali** | ✅ |
| S53 | ne kód, návrh; nástroj vzal model omezené velikosti a zkusil každé pořadí selhání a obnov | model checker TLC nad specifikací, ne nad kódem; ověřuje „a sufficiently large instance of the system" — tedy konečnou instanci modelu. Dřív „a small version of the system", přeformulováno, aby nevznikl rozpor s „sufficiently large" a aby bylo jasné, že nejde o vyčerpávající analýzu produkčního systému | ✏️ ✅ |
| S54 | v DynamoDB, databázové službě Amazonu, našel chybu, která mohla ztratit data | tabulka 1: DynamoDB, „Replication & group-membership system", 939 řádků TLA+, „Found 3 bugs, some requiring traces of 35 steps"; text: „a bug that could lead to losing data if a particular sequence of failures and recovery steps was interleaved with other processing". DynamoDB = „‘No SQL’ data store", spuštěno 1/2012 | ✅ |
| S55 | nejkratší cesta: 35 kroků v přesném pořadí; prošla revizemi návrhu, kódu i testy | „the shortest error trace exhibiting the bug contained 35 high level steps"; „The bug had passed unnoticed through extensive design reviews, code reviews, and testing" | ✅ |
| S56 | poctivá verze: AI píše kód a něco nezávislého ho kontroluje | závěr argumentu | 💬 |

## S57–S66 Závěr

| | tvrzení | ověření | |
|---|---|---|---|
| S60 | „FORTRAN was automatic coding, until it became the code" | callback na S10, doloženo tam | ✅ |
| S61 | ten „co" byl vždycky ta těžká část | argument | 💬 |
| S62–S66 | budoucí programátor, otázka do komentářů | závěr zdroje uživatele, úvaha | 💬 |

## Obrázky

Storyboard zatím není. Až bude: portrét Dijkstry a titulní strana článku
FORTRAN (1957) z archivu ověřit proti `sources.json`; diagram MDA (PIM →
PSM) nesmí tvrdit víc než S15; ve scéně s Amazonem odlišit **model** od
**kódu** (S53) a ve scénách S46–S47 vizuálně odlišit „testy prošly" od
„testy stačí" (zpětná vazba 0.2, bod 3).
