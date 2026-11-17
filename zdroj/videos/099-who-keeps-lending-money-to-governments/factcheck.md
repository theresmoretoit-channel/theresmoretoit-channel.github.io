# Fact check — 099 Who Keeps Lending Money to Governments?

Ověřeno 2026-10-09 proti scénáři v0.2, opravy jsou ve v0.3. Čísla jsou
z primárních zdrojů (API Eurostatu a IMF, MoF/BoJ, PDMA, DMO, australský
Treasury), ne z paměti.

## Před finálním TTS / nahráním PŘEOVĚŘIT

| co | kdy | scény |
|---|---|---|
| IMF WEO říjen 2026 (USA 123,9 %, deficit 6,8 %; Japonsko 206,5 % — musí zůstat nad 200) | vychází **13. 10. 2026** | S31, S32, S48, S74 |
| Eurostat, říjnová notifikace EDP (může posunout 2025 o desetiny) | ~**21.–22. 10. 2026** | S11, S25, S28, S31, S34, S35 |
| výnosy 10letých dluhopisů Řecko vs. Francie | těsně před zveřejněním | S12, S55, popis videa |

## Úvod: Řecko (S07–S14)

- **S08 „nearly 130 % v roce 2009": OK, upraveno z „about".** Eurostat
  `gov_10dd_edpt1` (vintage 22. 4. 2026): **128,5 %**, IMF WEO taky 128,5.
- **S09 „within two years… interest no government could pay": OK.**
  Eurostat `irt_lt_mcby_m`, 10leté: 5,49 % (12/2009), 12,01 % (12/2010),
  21,14 % (12/2011). Přístup na trh Řecko ztratilo už při bailoutu 5/2010.
- **S10 „biggest government debt restructuring in history": OK.**
  Zettelmeyer, Trebesch & Gulati (2013), *The Greek Debt Restructuring: An
  Autopsy*: „the largest sovereign debt exchange operation in history",
  vyměněno 199,2 mld. €. Druhé největší je Rusko 1918, pod 100 mld. €
  v eurech roku 2011. https://repec.cepr.org/repec/cpr/ceprdp/DP9577.pdf
- **S11 „about 146 %": OK.** Eurostat 2025: 146,1 (IMF 145,7). Q1 2026 už
  143,5 a klesá.
- **S12 „levněji než Francie": OPRAVENO, doplněno období.** Měsíční průměry
  Eurostatu, Řecko proti Francii:
  - 12/2024 zhruba nastejno (3,05 / 3,01);
  - poprvé níž **8/2025** (3,37 / 3,42), pak níž až do 1/2026;
  - **3.–5. 2026 Řecko mírně VÝŠ** (3,71 / 3,64, 3,78 / 3,73, 3,75 / 3,74);
  - 6.–8. 2026 znovu níž (8/2026 3,87 / 4,00);
  - **2. 10. 2026: 4,523 % proti 4,910 %** (dnews.gr, 3. 10. 2026).

  **Celé období přeměřeno 2026-10-09** (Eurostat `irt_lt_mcby_m`, update
  11. 9. 2026), rozdíl Řecko − Francie v p. b.:

  | 10/25 | 11/25 | 12/25 | 1/26 | 2/26 | 3/26 | 4/26 | 5/26 | 6/26 | 7/26 | 8/26 | 9/26 |
  |---|---|---|---|---|---|---|---|---|---|---|---|
  | −0,14 | −0,14 | −0,12 | −0,10 | −0,01 | **+0,07** | **+0,05** | **+0,01** | −0,04 | −0,06 | −0,13 | ~−0,22 \* |

  \* září ještě není v měsíční řadě, je to denní kotace z 15. 9. (Euronews);
  2. 10. −0,39. Řecko je levnější **9 měsíců z 12**, dražší 3 měsíce
  (o 0,01–0,07 p. b.), únor prakticky nastejno.

  Nové znění *„for most of the past year… On ten-year bonds."* drží
  pro zveřejnění v říjnu 2026. **Do popisu videa patří snímek s datem.**
  Srovnání je výnos 10letého dluhopisu, ne průměrný úrok z celého dluhu.

## Deficit a dluh, Dánsko, USA, Evropa (S16–S36)

- **S24 „100 mld. USD by zničilo malou zemi a u velké se ztratí": OK.**
  IMF HDP 2025: Estonsko 47,0 mld. USD (≈ 213 %), USA 30 767 mld. (≈ 0,33 %).
- **S25–S28 Dánsko: OK.** Eurostat: dluh 2025 **27,9 %**, 2022 **33,3**,
  2023 33,0, 2024 30,5. Přebytek 2025 **+2,9**, předtím 2024 +4,5,
  2023 +3,4, 2022 +3,4, 2021 +4,1, takže „not for the first time" sedí.
  Pokles začal už dřív (2021: 39,6), „since 2022" je zvolený začátek.
- **S29 přebytek nemusí snížit hrubý dluh:** formulace uživatele,
  koncepčně v pořádku.
- **S31–S32 USA: OK, je to odhad IMF.** WEO duben 2026 (DataMapper
  `GGXWDG_NGDP`, `GGXCNL_NGDP`): dluh 2025 **123,9 %**, saldo **−6,8 %**.
  Jde o **general government**, ne o federální dluh. Neověřená výhrada (agent
  ji uvádí z paměti): IMF u USA započítává nekryté penzijní závazky
  zaměstnanců státu, Eurostat u maastrichtského dluhu ne. Proto USA
  **nejsou** ve sloupcovém grafu s Eurostatem.
- **S32b poměr klesá při rostoucí částce: OK.** D/Y klesá, když nominální
  HDP roste rychleji než nominální dluh.
- **S34–S35 Eurostat 2025: OK, všech sedm hodnot** (EE 24,1, DK 27,9,
  CZ 44,3, DE 63,5, FR 115,6, IT 137,1, EL 146,1). Zaokrouhlení v hlase
  sedí. Zdroj:
  https://ec.europa.eu/eurostat/api/dissemination/statistics/1.0/data/gov_10dd_edpt1?unit=PC_GDP&sector=S13&na_item=GD
- **S36 „six times as much": OK.** 146,1 / 24,1 = 6,06.

## Kdo půjčuje (S38–S46)

- **S38 vlády prodávají dluhopisy: OK** pro vyspělé ekonomiky („usually"
  pokrývá úvěry od MMF a Světové banky).
- **S39–S41 dluhopis: OPRAVENO** na *„interest payments every year"*.
  Treasuries, gilty a australské dluhopisy platí kupon pololetně, Bundy
  ročně.
- **S42 „foreign governments": OK.** TIC Table 5, červenec 2026: cizinci
  drží 9 248 mld. USD Treasuries, z toho **oficiální sektor 3 773 mld.
  (41 %)**.
- **S44–S46 penzijní fondy: OK, kvalitativně.** OECD *Pension Markets in
  Focus 2025*: dluhopisy a akcie tvoří přes polovinu aktiv ve 34 z 38 zemí,
  ale jedno číslo podílu státních dluhopisů napříč zeměmi není.
  „There's a good chance" je dost opatrné.

## Japonsko (S47–S51)

- **S48 „more than twice its economy": OK, ale těsně.** IMF WEO duben 2026:
  **206,5 %** (2025), 2026 projekce 204,4; 2022 to bylo 227,8. Starší
  vintage uváděly ~235, **necitovat**. Řecko 145,7.
- **S49 „about nine-tenths held at home": OPRAVENO** (dřív „much of it").
  MoF, *Breakdown by JGB and T-Bill Holders*, červen 2026 předběžně: cizinci
  drží **7,9 % JGB** a **13,1 % JGB a T-bills**, doma tedy 87–92 %.
  Banky 15,6 %, pojišťovny 15,1 %, veřejné penze 7,6 %, penzijní fondy 3,2 %.
  https://www.mof.go.jp/english/policy/jgbs/reference/Others/holdings01.pdf
- **S50 BoJ: OPRAVENO** na *„nearly half of its bonds"*. Tatáž tabulka:
  BoJ 470,0 bil. jenů = **46,7 % JGB** (vč. FILP, bez T-bills), 41,2 %
  s T-bills. Klesá kvůli QT, pod 50 % poprvé od 6/2022 (12/2025 49,0 %).
- „téměř nulový úrok": ve scénáři už není. BoJ 21. 9. 2016 cílila 10letý
  výnos „around zero percent", YCC skončila 3/2024.

## Řecko 2009 vs. dnes (S52–S55)

- **S52 „foreign banks": OPRAVENO** na *„foreign investors, many of them
  banks"*. Merler & Pisani-Ferry (Bruegel 2012/02): nerezidenti drželi
  **73,8 %** obchodovatelného dluhu na konci 2007, vrchol v 2008, od konce
  2009 pokles. Za vrcholem tedy „most" platí i pro 2009, přesné číslo za
  rok 2009 ale chybí.
- **S53 euro: OK.**
- **S54: OPRAVENO** na *„more than half"* (dřív „most"). PDMA Bulletin 122
  (6/2026): úvěry z mechanismů pomoci (GLF + EFSF + ESM) **203,1 mld. €**
  z 357,6 mld. € = **57 %**. Průměrná splatnost **18,3 roku**, náklad
  **1,43 %** (hotovostně). GLF jsou přímé bilaterální úvěry států, EFSF
  a ESM vlastní a ručí za ně státy eurozóny, takže „through rescue funds"
  je fér zjednodušení. https://www.pdma.gr/images/docs/Bulletin_n122EN.pdf

## Refinancování a Británie (S56–S64)

- **S56–S62: OK koncepčně.** „Exactly the same size" platí pro nominál
  v ilustračním příkladu.
- **S63 „last four undated government bonds" v roce 2015: OK.** HM Treasury
  27. 3. 2015: „redeem the last four undated bonds" (2¾% Annuities,
  2½% Annuities, 2½% Consolidated Stock, 2½% Treasury Stock), splaceny
  **5. 7. 2015**, dohromady 382 mil. £. Celý program osmi nedatovaných
  dluhopisů v roce 2015 dal **~2,6 mld. £** (3½% War Loan 1 938,6 mil. £,
  splacen 9. 3. 2015).
  https://www.gov.uk/government/news/repayment-of-26-billion-historical-debt-to-be-completed-by-government ,
  https://www.dmo.gov.uk/media/i2sfsfj4/pr270315.pdf
- **S64 „traced back to 1720": OK.** Gov.uk: poslední čtyři „can be traced
  back three centuries" a zahrnují gilty z roku 1853, kdy Gladstone
  konsolidoval akcie South Sea Company převzaté státem po krachu v roce 1720.
  Nástroj vrátil jen blízkou parafrázi, ne doslovný text, takže je to
  citace z druhé ruky. Půjčka na odškodnění podle zákona o zrušení otroctví
  (1835) skončila ve 4% Consols (splaceno 1. 2. 2015), v posledních čtyřech
  **není** — schválně to nezmiňujeme.

## Spirála a řecké selhání (S66–S75)

- **S72 „around thirty percent… at times, far more": OPRAVENO.** Měsíční
  průměr Eurostatu vrcholí na **29,24 % (2/2012)**. Denní kotace byly
  v únoru ~37 % a začátkem března (před výměnou) 41–47 % podle zdroje.
- **S73 „lost more than half": OK na všech měřítkách.** Nominál −53,5 %
  (100 − 15 EFSF − 31,5 nové dluhopisy), současná hodnota 59–65 % (ZTG:
  64,6 %), tržní konvence ~77 %.
- **S74 Japonsko vs. Řecko před krizí: OK.** Japonsko od ~2015 ≥ 200 %,
  Řecko 2009 128,5 %.

## Austrálie (S76–S81)

- **S77–S78: OPRAVENO, pořadí událostí.** Ve v0.2 stálo „téměř bez čistého
  dluhu → tak se zeptala". Ve skutečnosti se ptala **v roce 2002**, kdy byl
  čistý dluh 4–6 % HDP a očekávalo se, že zmizí. Costello, 30. 10. 2002:
  „the holding of CGS could be eliminated by 2005-06". Čistý dluh vládního
  sektoru (BP1 2017-18, Statement 11, Table 4): 2001-02 5,7 %, 2002-03 4,3,
  2004-05 1,8, **2005-06 0,2**, **2006-07 −2,1**, 2007-08 −3,3. Hrubé CGS
  63,0 mld. A$ (2001-02), pak 54–55 mld. až do 2007-08.
- **S79 rozhodnutí zachovat trh: OK.** Budget 2003-04, Statement 7: „the
  Government has decided to maintain the CGS market… ensuring sufficient
  CGS remains on issue to support the Treasury bond futures market."
  Zdůvodnění: zrušení by „lead to slightly higher interest rates…
  primarily from the higher costs associated with managing interest rate
  risk without a Treasury bond futures market".
- **S80: UPŘESNĚNO.** Futures SFE (3 a 10 let) se vypořádávají proti
  výnosům koše CGS, proto *„futures contracts were tied to them"*.
  Diskusní dokument, kap. 3: CGS a deriváty jsou „the primary vehicles in
  Australia for managing interest rate risk".
- **S80b „By 2007… owned outweighed owed. And it still kept selling":
  NOVÁ věta, doložená.** Čistý dluh 2006-07 −2,1 %, hrubé CGS zůstalo
  ~55 mld. A$. Je to rozlišení čistého a hrubého dluhu, které chtěl
  uživatel.
- **S81: OK.** Budget 2011-12, Statement 7: likvidní trh CGS kvůli futures
  „even without a budget financing need". **Pozor:** Treasury výslovně
  píše, že rozhodnutí „is not specifically targeted at meeting investor
  demand for risk-free financial assets", takže věta o „nejbezpečnějším
  místě pro úspory" se k Austrálii vracet nesmí (z v0.2 už vypadla).

## Závěr (S82–S88)

Hodnotící a shrnující věty bez nových faktů. S83 „other governments"
viz S42; S84 přepsané uživatelem tak, aby neplatilo „vše se vždy splatí".
