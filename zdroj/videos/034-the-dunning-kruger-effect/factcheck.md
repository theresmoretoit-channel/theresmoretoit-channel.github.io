# Fact check — 034 The Dunning–Kruger Effect

Ověřováno proti `script 0.4.md` dne 2026-09-08. Metoda podle CLAUDE.md:
vypsat **každé** ověřitelné tvrzení, ne jen ta, která vypadají riziková,
a **zobecnění brát jen z primárního zdroje**.

## Primární zdroje, které se podařilo získat

| zkratka | co to je | jak získáno |
|---|---|---|
| **KD1999** | Kruger, J., & Dunning, D. (1999). *Unskilled and Unaware of It.* Journal of Personality and Social Psychology 77(6), 1121–1134 | plný text PDF, `pdftotext -layout` |
| **KD2002** | Kruger & Dunning (2002). *Unskilled and Unaware — But Why? A Reply to Krueger and Mueller.* JPSP 82(2), 189–192 | plný text PDF |
| **SDJK2013** | Schlösser, Dunning, Johnson & Kruger (2013). *How unaware are the unskilled?* Journal of Economic Psychology 39, 85–100 | plný text PDF |
| **NUH2016** | Nuhfer, Cogan, Fleisher, Gaze & Wirth (2016). *Random Number Simulations Reveal How Random Noise Affects…* Numeracy 9(1), art. 4 | **jen abstrakt** (plný text za Cloudflare) |
| **NUH2017** | Nuhfer, Fleisher, Cogan, Wirth & Gaze (2017). *How Random Noise and a Graphical Convention Subverted…* Numeracy 10(1), art. 4 | **jen abstrakt** |
| **GZ2020** | Gignac & Zajenkowski (2020). *The Dunning-Kruger effect is (mostly) a statistical artefact.* Intelligence 80, 101449 | **jen abstrakt** |
| **MP2022** | Magnus & Peresetsky (2022). *A Statistical Explanation of the Dunning–Kruger Effect.* Frontiers in Psychology | plný text (PMC8992690) |

> **Kde je doklad slabší, je to napsané.** NUH2016/2017 a GZ2020 jsou
> ověřené jen abstraktem, protože digitalcommons.usf.edu i ScienceDirect
> vracejí přes `curl` i `WebFetch` Cloudflare challenge, resp. 403.
> Abstrakty jsou ale u obojího dost konkrétní na tvrzení, která scénář
> dělá — viz jednotlivé body.

---

## S16 — „In nineteen ninety-nine, psychologists David Dunning and Justin Kruger published a study"

| | |
|---|---|
| rok | ✅ 1999, JPSP 77(6), 1121–1134 |
| jména | ✅ Justin Kruger, David Dunning, oba tehdy Cornell University |
| „psychologists" | ✅ obor i časopis sedí |

⚠️ **Poznámka, ne chyba: prvním autorem je KRUGER, ne Dunning.** Scénář
je uvádí v pořadí „David Dunning and Justin Kruger", což kopíruje název
efektu, ne pořadí autorů. Není to nepravda (studii publikovali oba)
a přehození by naopak vneslo rozpor s názvem „Dunning–Kruger effect",
který video používá od S06. **Ponecháno záměrně.** Kdyby se na to někdo
v komentářích ptal, tohle je odpověď.

## S18 — „They gave students tests of logical reasoning, grammar, and humour."

✅ **Ověřeno doslova.** KD1999, abstrakt: *„participants scoring in the
bottom quartile on tests of **humor, grammar, and logic**"*.

Rozpis čtyř studií z těla práce:

| studie | doména | účastníci |
|---|---|---|
| 1 | humor (vtipy hodnocené panelem profesionálních komiků) | Cornell undergraduates |
| 2 | logické uvažování | totéž |
| 3 | gramatika (American Standard Written English) | 84 Cornell undergraduates |
| 4 | logické uvažování (Wasonova selekční úloha) + trénink | totéž |

„students" ✅ — všechny čtyři studie jsou na vysokoškolácích Cornellu.

> Scénář říká *„tests"* v množném čísle, což je přesné: nešlo o jeden
> test se třemi částmi, nýbrž o čtyři studie ve třech doménách.

## S19 — „What they reported was that people who performed poorly … had difficulty recognising just how poorly they had performed."

✅ KD1999, abstrakt: *„their incompetence robs them of the metacognitive
ability to realize it"* a *„Several analyses linked this miscalibration
to deficits in metacognitive skill, or the capacity to distinguish
accuracy from error."*

Formulace *„What they reported was"* je záměrné přisouzení (viz
`notes.md`, bod 4 zpětné vazby) — scénář netvrdí, že to tak je, nýbrž
že to autoři naměřili. Po přidání sekce S55–S65 je to nutné.

## S21–S22 — čísla 62 a 12 ⭐ KLÍČOVÉ TVRZENÍ

> *„The people who performed in the bottom quarter estimated their
> performance as if they were around the sixty-second percentile.
> In reality, they were around the twelfth."*

✅ **Ověřeno proti abstraktu KD1999, doslovná shoda:**

> *„Across 4 studies, the authors found that participants scoring in the
> bottom quartile on tests of humor, grammar, and logic grossly
> overestimated their test performance and ability. **Although their test
> scores put them in the 12th percentile, they estimated themselves to be
> in the 62nd.**"*

Obě čísla jsou tedy **souhrn autorů přes všechny čtyři studie**, ne údaj
z jedné. Dílčí čísla z těla práce, pro úplnost a pro odpovědi
v komentářích:

| studie | doména | skutečný percentil | odhad schopnosti | odhad výsledku |
|---|---|---|---|---|
| 1 | humor | 12. | 58. | — |
| 2 | logika | 12. | 68. | 62. |
| 3 | gramatika | 10. | 67. | 61. |
| 4 | logika (Wason) | 13. | 55. | 53. |
| **abstrakt (souhrn)** | | **12.** | **62.** | |

„bottom quarter" = *bottom quartile* ✅ — v popularizačním textu správný
překlad, kvartil je čtvrtina.

## S26–S27 — „You need a certain amount of knowledge to perform a task. But you may also need some of that same knowledge to accurately judge your performance."

✅ To je „dual burden" hypotéza, jádro KD1999. Abstrakt: *„people who are
unskilled in these domains suffer a **dual burden**: Not only do these
people reach erroneous conclusions and make unfortunate choices, but
their incompetence robs them of the metacognitive ability to realize it."*

Scénář to má hedgované (*„may also need"*), což po sekci S55–S65 sedí.

## S53 — „does not mean: The less intelligent you are, the more confident you become."

✅ **Ověřeno z dat KD1999, a je to silnější, než scénář říká.** Studie
neměřila inteligenci, nýbrž výkon v konkrétní dovednosti — a hlavně:
**horní kvartil se hodnotil VÝŠ než dolní**, ne níž.

| studie 2 | skutečný percentil | odhad schopnosti |
|---|---|---|
| dolní kvartil | 12. | 68. |
| **horní kvartil** | **89.** | **72.** |

Populární verze („nejméně schopní jsou nejsebevědomější") je tedy
v přímém rozporu s primárními daty. Doklad do komentářů.

## S54 — „And it doesn't mean that experts are always insecure."

✅ Správně, ale s nuancí, kterou je dobré mít po ruce.

KD1999 **skutečně našla, že horní kvartil svůj relativní žebříček
PODhodnocuje** — ve studii 2 při skutečném 89. percentilu odhad
schopnosti 72. a výsledku 70. Autoři to ale nepřipisují nejistotě, nýbrž
**false-consensus efektu**: dobří odhadují ostatní jako lepší, než jsou.
KD2002 to potvrzuje: *„Krueger and Mueller also replicated our finding
that top performers underestimate their comparative ranking."*

Scénář říká *„always insecure"*, tedy popírá karikaturu, ne ten nález.
✅ Formulace obstojí. **Očekávaný komentář pod videem: „ale studie
ukázala, že experti se podceňují." Odpověď je tenhle odstavec.**

## S57–S58 — statistické námitky ⚠️ ZDE BYLA OPRAVA

**Původní znění 0.3 bylo věcně vedle:**

> ❌ *„And correlations introduced by the way performance and
> self-estimation are **measured**."*

Námitka se netýká **měření**, nýbrž **vynášení do grafu a porovnávání**.

| zdroj | co přesně říká |
|---|---|
| NUH2017 (abstrakt) | *„Much of the current consensus … comes from interpreting normative data presented in the Kruger-Dunning type **graphical format** or closely related **(y − x) vs. (x) graphical conventions**."* |
| NUH2016 (abstrakt) | *„**graphical conventions** common in the self-assessment literature **introduce artifacts that invite misinterpretation**. Troublesome conventions include: (y minus x) vs. (x) scatterplots; … line charts that display data aggregated as quantiles"* |
| GZ2020 (abstrakt) | *„The most common method … involves **plotting** the self-assessed and objectively assessed means across four categories (quartiles) … this method has been argued to be confounded by the **better-than-average effect** and **regression toward the mean**."* |
| KD2002 | *„a combination of the **better-than-average (BTA) effect** and a **regression artifact**"* (jak to shrnuli Krueger a Mueller 2002) |

**Opraveno na:**

> ✅ *„Things like regression to the mean. And the fact that almost
> everyone thinks they're above average. And a correlation created
> by the way the two measurements are **plotted against each other**."*

Přidán tím i **better-than-average effect**, který je v každém ze čtyř
zdrojů jmenován jako druhá polovina námitky a ve scénáři chyběl.

> Je to přesně ta past, před kterou uživatel varoval: natočit video
> o tom, že se Dunning-Kruger zjednodušuje, a přitom zjednodušit
> námitku proti němu. Rozdíl mezi „jak se to měří" a „jak se to kreslí
> do grafu" je v tomhle sporu ten podstatný.

## S60–S61 — simulovaná data ⚠️ ZDE BYLA DRUHÁ OPRAVA

**Původní znění 0.3 přestřelovalo:**

> ❌ *„If you generate **completely random** data, where the scores
> **mean nothing at all**, and plot it the same way… you get a graph
> that looks **remarkably similar**."*

Doložit se dá slabší tvrzení. MP2022 (plný text, primární):

> *„Ackerman et al. (2002) demonstrated that **pictures like Figure 1 can
> be obtained with simulated data using two random variables with small
> correlation r = 0.19**."*
> *„Nuhfer et al. (2016) used **simulated random variables with
> correlation less than 1** and various graphical representations of the
> data to illustrate the DK effect."*

Tedy **ne data bez jakéhokoli vztahu**, nýbrž data se slabým vztahem
a bez zabudovaného Dunning-Krugerova mechanismu. To je i podstata
námitky: obrázek vznikne, aniž by pod ním ten jev byl.

**Opraveno na:**

> ✅ *„If you take **simulated data with no such effect built into it**,
> and plot it the same way… **you can still get** a graph that looks
> **much like the original**."*

„can still get" odpovídá „can be obtained" v primárním zdroji.

## S63–S64 — „the debate isn't completely settled. There are responses to those criticisms, and responses to those responses."

✅ **Doloženo doslova, řetěz je delší než dvě kola:**

| rok | kdo | co |
|---|---|---|
| 1999 | Kruger & Dunning | původní práce |
| 2002 | Krueger & Mueller | námitka: better-than-average + regresní artefakt |
| 2002 | **Kruger & Dunning** | **odpověď na námitku** (KD2002) |
| 2016, 2017 | Nuhfer a spol. | námitka: grafická konvence a šum |
| 2020 | Gignac & Zajenkowski | námitka: *„(mostly) a statistical artefact"* |
| 2022 | Magnus & Peresetsky | statistické vysvětlení |
| 2023 | Hiller | **komentář ke Gignacovi a Zajenkowskému** |

GZ2020 sám závěr formuluje opatrně — *„although the phenomenon … **may
be to some degree plausible for some skills**, the magnitude of the
effect **may be much smaller** than reported previously"* — tedy ne
„neexistuje". Scénář to nikde netvrdí. ✅

## S66 — „Dunning and Kruger's own claim was more subtle."

✅ Odpovídá „dual burden" formulaci z abstraktu KD1999 (viz S26–S27).
Přisouzení autorům místo neosobního *„the real idea"* je záměrné.

---

## Neověřitelné a neproblematické

Zbytek scénáře jsou obecná tvrzení bez konkrétních čísel: příklad
s učením programovat (S08–S15), rozhodovací strom správce (S43–S51),
programátor pouští testy / vědec ověřuje / inženýr počítá rezervy
(S87–S90), a závěrečná pointa. **Neobsahují ověřitelný údaj** a nejsou
prezentovány jako výsledek výzkumu.

Jediné číslo v celém scénáři mimo studii je letopočet **nineteen
ninety-nine** ✅.

## Co zbývá dotáhnout

**NUH2016 a NUH2017 jsou ověřené jen abstraktem**, protože plné texty
jsou za Cloudflare (`curl` i `WebFetch` → 403, i přes přímé PDF URL
z OpenAlexu). Abstrakty pokrývají obě tvrzení, která na nich scénář
staví (grafická konvence `(y − x) vs. (x)`, artefakty z šumu), a tvrzení
o simulovaných datech navíc stojí na MP2022, kde plný text k dispozici
je. **Doklad tedy drží**, ale kdyby se scénář o Nuhfera opřel silněji,
je potřeba plný text sehnat jinudy.
