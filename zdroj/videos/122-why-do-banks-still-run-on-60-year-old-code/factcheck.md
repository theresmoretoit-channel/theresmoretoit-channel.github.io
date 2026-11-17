# 122 — fact check scénáře v0.2

v0.2: S64–S65 (SSA „století") škrtnuty, dřívější S66–S75 přečíslovány na S64–S73.

Zdroje, citace a výpočty jsou v `factcheck-zaklad.md` (A = technika
a historie, B = případy; odkazy `A2c` = část A, oddíl 2c). Tady je jen
přiřazení ke scénám a závěr. ✅ doloženo, ⚠️ doloženo jen sekundárně,
zjednodušení nebo rétorika (vysvětleno).

| scéna | tvrzení | ověření | závěr |
|---|---|---|---|
| S01–S03 | 999,99 + 0,01 dá nulu, bez chyby, program běží dál | A2c (IBM 6.4 LR: *„truncation rules apply"*); **spuštěno 2026-10-25** GnuCOBOL 3.2 `-std=ibm`, `PIC 9(3)V99`: `000.00` (`overeni/p.cob`) | ✅ |
| S04 | když je pole pro výsledek malé, číslice může zmizet; bez žádosti o varování (`ON SIZE ERROR`) výpočet pokračuje (v0.2: vázáno na velikost pole) | A2c | ✅ — **v obraze S02–S04 musí být vidět záměrně malé pole** |
| S05 | 2,345 uložené na pence → 2,34 (useknutí) | A2b; spuštěno (`p.cob`, `ar.cob`) | ✅ |
| S06 | s `ROUNDED` → 2,35 | A2b; spuštěno | ✅ |
| S07 | „many of the world's banks still run on rules like these" | nepřímo: A6 (IBM: 45 z 50 největších bank má mainframe), A4 (COBOL ve státní správě). Podíl bank na COBOLu doložený NENÍ (A3a slabé), proto „many", ne číslo | ⚠️ obecné, bez čísla |
| S08 | jazyk z 1959; ne každý program je tak starý | A1a | ✅ |
| S12–S13 | přepis „opraví" pravidla → rozchod se starým tam, kde vznikne půl pence | plyne z A2b, A2c (hypotetický přepis, tak i formulováno) | ✅ |
| S14 | moderní jazyky umějí přesnou desítkovou, Java má typ | A2e (`BigDecimal`) | ✅ |
| S15 | HALF_UP → 2,35, HALF_EVEN → 2,34, obojí správně | A2e, ukázka A; spuštěno ve třech jazycích | ✅ |
| S16 | `0.1 + 0.2` ≠ `0.3` v plovoucí čárce | A2e: `0.30000000000000004` | ✅ |
| S19 | květen 1959, ministerstvo obrany, Pentagon; výrobci, úřady, firmy | A1a | ✅ |
| S20 | každý počítač měl svůj jazyk, program pro jeden stroj nešel na jiném | motivace CODASYL (A1a, A1d: test přenositelnosti byl smyslem). **Zjednodušení:** jazyky existovaly i přes výrobce (FORTRAN), ale obchodní programy přenositelné nebyly | ⚠️ zjednodušení |
| S21 | navrhl to výbor; největší vliv FLOW-MATIC od týmu Grace Hopper v Remington Rand | A1b (ne „Hopper vynalezla COBOL") | ✅ |
| S22 | prosinec 1960, v podstatě týž program na dvou počítačích konkurentů | A1d: 6.–7. 12. 1960, RCA a Remington Rand UNIVAC, *„essentially the same"* | ✅ |
| S23 | `ADD PAYMENT TO ACCOUNT-BALANCE.` | platný příkaz COBOLu (`ADD … TO …`), ilustrace | ✅ |
| S24 | peníze jako desítkové číslice; tečka se ukládat nemusí, polohu určuje popis pole (v0.2) | A2a (IBM: *„does not exist as an actual character"*); spuštěno: 9 bajtů | ✅ |
| S25 | 1964 System/360, v návrhu desítkové instrukce | A2d (na části modelů volitelný „decimal feature", proto „its design included", ne „every machine") | ✅ |
| S26–S27 | IBM navrhuje mainframy kompatibilně, mnoho starších programů může běžet bez přepsání; „rarely a moment that forced anyone" (v0.2, ne absolutně) | A6 (*„high degree of compatibility"*, s podmínkami; ne absolutně) | ✅ |
| S28 | nikdo nespočítal COBOL celosvětově; IBM: 45 z 50 největších bank má jeho mainframy | A3 (odhady 200–800 mld. bez metodiky); A6: IBM 10-K FY2022 *„Forty-five of the world's top 50 banks"* — tvrzení IBM, uvedeno jako „IBM says". Mainframe ≠ COBOL, ve scénáři se nespojuje | ✅ s atribucí |
| S29 | 2017, SSA: přes 60 mil. řádků COBOLu | A4c (IT Modernization Plan 10/2017) | ✅ |
| S30–S31 | 2025, GAO: 11 systémů nejvíc potřebných náhrady, 23–60 let, ~750 mil. USD ročně | A4a: GAO-25-107795, 17. 7. 2025, $754 mil. | ✅ |
| S34 | 2018, TSB, ~5 mil. zákazníků | B1a: FCA 5,2 mil. | ✅ |
| S35 | systémy pronajaté od Lloyds, konkurenta; poplatky měly výrazně stoupnout | B1d: S&M §2.8 | ✅ |
| S36 | nová platforma od nového vlastníka Sabadell | B1c (Proteo4UK, SABIS). **Sabadell vlastní TSB od 2015 — dooveřit** | ⚠️ rok vlastnictví neověřen, ve scénáři jen „new owner" |
| S37 | jeden víkend v dubnu, zapnuto v neděli večer | B1b: go-live 22. 4. 2018 (neděle) 18:00 | ✅ |
| S38 | v pondělí ~900 000 pokusů o přihlášení, uspěl ~1 z 10 v internetovém bankovnictví | B1a: FCA §4.9 (pokusy, ne lidé — v0.1 opraveno) | ✅ |
| S39 | platby selhávaly; někteří viděli cizí účty | B1a: FCA §4.9 (48 % / 59 % plateb neúspěšných), §4.6–4.7 (440 zákazníků) | ✅ |
| S40 | nejhůř ~týden, běžný provoz až v prosinci | B1b: do 26. 4., BAU 10. 12. 2018 | ✅ |
| S41 | „fallout cost" ~£330 mil. v 2018 (v0.3: ne „clean-up", částka zahrnuje i ušlé příjmy), později pokuty skoro 49 mil. | B1e: £330,2 mil. (náklady + ušlé příjmy); B1f: £48,65 mil. | ✅ |
| S42 | data dorazila v pořádku, obě oficiální zprávy | B1c: S&M §2.2, FCA §4.4 | ✅ |
| S43 | dvě datová centra nastavená jinak, výkon testován jen na jednom, cíle sníženy po neúspěchu | B1c: S&M §2.43(A), (B) | ✅ (exekutivní shrnutí S&M; celá zpráva nedočtena) |
| S44 | návrat „essentially impossible" | B1c: FCA §4.51 *„technically speaking, essentially impossible"* | ✅ |
| S45 | TSB neutíkala z rozbitého systému, odcházela kvůli vlastníkovi a ceně | B1d: S&M §2.8 | ✅ |
| S47 | 2008, CBA, systémy přes 45 let | B2: oznámeno 28. 4. 2008 (P6); „over 45 years" CIO (S6) | ⚠️ stáří sekundárně (citace CIO v tisku) |
| S48 | plán ~580 mil. AUD na 4 roky | B2: P6 | ✅ |
| S49 | trvalo 5 let; tisk později uvedl ~1,1 mld. při rozšíření projektu (v0.2: připsáno tisku) | B2: dokončeno FY2013 (P7); 1,1 mld. a rozšíření rozsahu jen S4, S5 | ⚠️ částka sekundárně |
| S50 | po částech: vklady 2010, firemní 2011, úvěry 2012 | B2: S5 | ⚠️ sekundárně |
| S51 | každý krok šlo sledovat a poučit se | interpretace postupné migrace | ⚠️ rétorika |
| S52 | podle banky první velká australská banka s real-time bankovnictvím nonstop | B2: P7 (tvrzení banky, uvedeno „the bank says") | ✅ s atribucí |
| S53 | 5 let, „a much bigger bill" | S49 (v0.2: bez slabého poměru 1,9×) | ✅ |
| S56–S57 | březen 2020, NJ: z pod 10 000 na přes 155 000 za týden, 16× | B3: P9, 9 467 → 155 815 (týden do 21. 3.), 16,5× | ✅ |
| S58 | začátkem dubna guvernér žádal dobrovolníky i s COBOLem, systémy přes 40 let | B3: 4. 4. 2020 (S7, parafráze); „40-plus" je jeho výrok, tak i formulováno („he said") | ✅ |
| S59 | příběh se rozšířil: starý kód zkolaboval | dobové titulky; WIRED 22. 4. 2020 *„Don't Blame Cobol"* na ně reaguje | ⚠️ popis mediálního rámce |
| S60 | auditor nenašel doklad, že zdržení způsobily počítačové systémy | B3: P11 (citace ze shrnutí na Oversight.gov, PDF nestaženo) | ⚠️ primární zdroj čten jen ve shrnutí |
| S61 | ZVLÁŠŤ od auditu: novináři dohledali mnoho chybových hlášení k webu v Javě, starý kód běžel (v0.2: oddělené od závěru auditora, „many") | B3: S8 WIRED, S9 Hicks (žurnalistika, uvedeno „reporters") | ✅ s atribucí |
| S62 | COBOL byl potřeba kvůli rychlým změnám pravidel (Kongres) | B3: S8 (analytik Gartneru, CARES Act 27. 3. 2020) | ⚠️ sekundárně |
| S63 | málo lidí, kteří to umějí změnit; telefony a personál přetížené | B3: S7 (ministr práce), A7 | ✅ |
| S64 | TSB: „left a system that still ran, and whose migration failed" (v0.4: ne „and broke"); NJ: „nobody could show it was the cause" (v0.2) | B1c, B1d; B3: P11 | ✅ |
| S65 | staré systémy zdražují, lidé odcházejí | A4a, A4b, A7 (GAO, SSA najímala penzisty) | ✅ |
| S67 | mnoho bank starý základ obaluje, aplikace mluví se starším | obecná praxe; konkrétní banka nedoložena | ⚠️ obecné, „many", „may" |
| S68–S69 | 2004, Martin Fowler, strangler fig | A8 | ✅ |
| S70 | někde program pořád může půl pence zahazovat | rétorika, „may" | ⚠️ rétorika |

**Otevřené před finální verzí:** dočíst Slaughter and May (sken, 262
stran; potřeba OCR) — zvlášť pokud bude S43 tvrdit víc než exekutivní
shrnutí; primární doklad CBA k 1,1 mld. (pololetní výsledky 2/2011);
Sabadell a TSB od 2015; plné PDF auditu NJ.
