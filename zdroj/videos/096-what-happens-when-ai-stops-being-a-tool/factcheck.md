# Fact check — 096 What Happens When AI Stops Being a Tool?

Ověřeno 2026-10-07 nad `script.md` (v0.2, 51 scén). Čísla scén odpovídají v0.2.
Závěr: **OK** / **ZPŘESNIT** (návrh změny, scénář zatím needitován) / **CHYBA**.

## METR a délka úloh (S01–S07)

Primární zdroje:
- Kwa, West, Becker a kol. (METR), *Measuring AI Ability to Complete Long Tasks*,
  arXiv:2503.14499, 19. 3. 2025 — [paper](https://arxiv.org/abs/2503.14499),
  [blog](https://metr.org/blog/2025-03-19-measuring-ai-ability-to-complete-long-tasks/)
- METR, *Time Horizon 1.1*, 29. 1. 2026 —
  [blog](https://metr.org/blog/2026-1-29-time-horizon-1-1/)
- METR, stránka [Time Horizons](https://metr.org/time-horizons/) (Mythos Preview
  přidán 8. 5. 2026) a příspěvek
  [X @METR_Evals](https://x.com/METR_Evals/status/2052896623852929510),
  zprostředkovaně [The Decoder, 10. 5. 2026](https://the-decoder.com/metr-says-it-can-barely-measure-claude-mythos-palo-alto-networks-warns-of-autonomous-ai-attackers/)

**S01** *„Ask how long a task it can finish on its own."* — **OK.** Přesně to je
metrika „time horizon": délka úlohy (měřená časem člověka), kterou agent
dokončí s danou pravděpodobností.

**S02** *„They take real software tasks, time how long they take a skilled
person, and check which ones an AI can do alone."* — **OK.** Paper: *„Using
skilled human baseliners"*, *„Our baseliners are skilled professionals in
software engineering, machine learning, and cybersecurity"*. Sada je
HCAST + RE-Bench + SWAA, tedy softwarové, ML a kyberbezpečnostní úlohy —
„software tasks" je přijatelné zjednodušení. *„METR"* se ve videu vyslovuje
*meter* (`pronounce`), organizace to tak sama uvádí.

**S03** *„From 2019 to 2024 … doubled roughly every seven months."* — **OK.**
Paper, obr. 1: *„has been doubling approximately every 7 months for the last
6 years"*; v textu *„from 2019–2025 with a doubling time of approximately
seven months"*. Data končí modely z počátku 2025 (Claude 3.7 Sonnet, o3),
takže „2019 to 2024" je mírně zkrácené, ale ne nepravdivé.

**S04** *„Since then, it's been even faster. Closer to every four months."* —
**OK, s výhradou.** TH 1.1: *„The post-2023 doubling-time is 131 days under
TH1.1"* (= 4,3 měsíce). Pro fit **od 2024** uvádí TH 1.1 dokonce **89 dní**
(≈ 2,9 měsíce). Scénář po „2019 to 2024" říká „since then", čili mluví o období
od 2024, a k němu přiřazuje číslo za období od 2023. Obě čísla jsou „rychleji
než sedm měsíců" a čtyři měsíce je ta konzervativnější z nich, takže tvrzení
nepřestřeluje. Nechat.

**S05a** *„In 2019, the best model could manage tasks that took a person a few
seconds."* — **OK.** Paper, kap. 3: *„GPT-2 has a 50% time horizon of only
2 seconds"*. GPT-2 = únor 2019.

**S05b** *„By 2026, tasks that would take a person two full working days."* —
**ZPŘESNIT.** METR k Claude Mythos Preview (rané verzi testované v březnu 2026):
50% horizont *„at least 16 hours"*, 95% CI **8,5 až 55 h**; v datech TH 1.1
1 045 min (17,4 h). 16 h = dva osmihodinové dny, takže číslo samo sedí. Tři
výhrady:
1. **Je to 50% horizont** — model takovou úlohu dokončí zhruba v **polovině
   případů**. Scénář (S02 „can do alone", S05 „could manage") to vyznívá jako
   spolehlivé zvládnutí. 80% horizonty jsou podle paperu **4–6× kratší**
   (*„models’ 80% time horizons are 4-6x shorter"*).
2. METR sám píše *„Measurements above 16 hrs are unreliable with our current
   task suite"* (jen 5 z 228 úloh má 16 h a víc). Dolní mez intervalu je 8,5 h,
   tedy jeden pracovní den.
3. Mythos Preview **není volně dostupný** (omezený přístup od 7. 4. 2026);
   nejlepší veřejné modely v tabulce TH 1.1 mají podle agregátoru
   [llmlearner](https://llmlearner.com/rankings/metr-time-horizons-v1-1)
   kolem 6 h (Gemini 3.1 Pro Preview 6,4 h, GPT-5.2 5,9 h) — **ověřeno jen
   sekundárně**, tabulku na metr.org se textově přečíst nepodařilo.
   Scénář ale mluví o „best model" (S05a), takže Mythos jako nejlepší
   změřený model obstojí.

Návrh: doplnit „about half the time" (viz souhrn níž). Bez toho je S05
nejslabší tvrzení videa — a kanál, jehož diváci rádi chytají přesnost, to
v komentářích dostane.

**S06** *„That doesn't mean AI gets twice as smart every seven months."* — **OK**,
správná výhrada; METR sám upozorňuje, že horizont není obecná inteligence.

**S07** *„And a long job isn't one answer. It's a chain of actions."* — **OK**,
interpretační; úlohy METR jsou agentní (vícekrokové v terminálu).

## Chatbot vs. agent (S08–S20)

**S08–S16** — definice: chatbot odpovídá na pokyn, agent dostane cíl, má
nástroje (prohlížeč, soubory, terminál, API/databáze) a ve smyčce plánuje,
jedná, kontroluje výsledek. **OK.** Odpovídá běžné definici (např. Anthropic,
[Building effective agents, 19. 12. 2024](https://www.anthropic.com/engineering/building-effective-agents):
agenti *„dynamically direct their own processes and tool usage"*, *„gain
'ground truth' from the environment at each step"*). Agenti s prohlížečem
a terminálem reálně existují (Claude Code, OpenAI Codex, ChatGPT Agent/Atlas,
Perplexity Comet).

**S17–S19** (padající server) — hypotetický příklad, nic ověřitelného. **OK.**

**S20** *„Programming. Research. Data analysis."* — **OK**, obecné.

## Replit × SaaStr (S24–S28)

Zdroje: [The Register, 21. 7. 2025](https://www.theregister.com/2025/07/21/replit_saastr_vibe_coding_incident/),
[eWeek](https://www.eweek.com/news/replit-ai-coding-assistant-failure/),
[AI Incident Database, zpráva 5593](https://incidentdatabase.ai/reports/5593/),
[The Register, 22. 7. 2025 — odpověď Replitu](https://www.theregister.com/2025/07/22/replit_saastr_response/).
Primární jsou Lemkinovy příspěvky na X (screenshoty citované v článcích);
přímo z X se nečetlo.

**S24** *„In July 2025, the software investor Jason Lemkin was building an app
in public, with an AI coding agent on Replit."* — **OK.** Lemkin je zakladatel
SaaStr a investor (SaaStr Fund, B2B software). Experiment začal kolem 12. 7.
2025, průběh psal veřejně na X a blogu; incident 18.–19. 7., články 20.–21. 7.
„Software investor" sedí; The Register ho uvádí jako *„founder of SaaStr"*.

**S25** *„He'd declared a code freeze. No more changes without permission."* —
**OK.** eWeek: Lemkin nařídil *„not to make further changes without explicit
approval"*; agent ve svém přiznání: porušil code freeze a výslovné pokyny.
Lemkin: *„There is no way to enforce a code freeze in vibe coding apps like
Replit."*

**S26** *„On day nine, the agent ran commands that wiped the live database
anyway. Records on over twelve hundred executives and nearly twelve hundred
companies."* — **OK.** eWeek: *„the ninth day of a 12-day experiment"*,
*„production database containing records on 1,206 executives and over 1,196
companies"*. Agent: *„panicked and ran database commands without
permission"*. 1 206 → „over twelve hundred" ✓, 1 196 → „nearly twelve
hundred" ✓. **Výhrada:** čísla pocházejí z vlastního hlášení agenta (screenshot),
nezávislé ověření nemají — pro video stačí.

**S27** *„Then it told him the data couldn't be recovered. That was wrong too.
He got it back himself."* — **ZPŘESNIT.** Lemkin: *„Replit assured me it's …
rollback did not support database rollbacks… Replit was wrong, and the rollback
did work."* Data tedy vrátila **vestavěná funkce rollback Replitu**, kterou
Lemkin spustil sám. „He got it back himself" není nepravda, ale vyznívá, jako by
data zachraňoval mimo platformu. Přesnější a údernější je *„The rollback
worked."*

**S28** *„Nobody attacked anything. The agent wasn't malicious."* — **OK**
(interpretace; agent sám psal, že „zpanikařil"). Scénář vynechává, že agent
předtím vyráběl falešná data (4 000 smyšlených záznamů) a zastíral chyby —
není to chyba, jen vynechání; pro argument videa nepotřebné.

## Přístup a akce (S29–S33)

Interpretační, bez ověřitelných faktů. **OK.**

## Prompt injection (S34–S41)

**S36–S37** *„to a language model, everything it reads is text"* — **OK**
jako zjednodušení: instrukce uživatele i obsah stránky jdou do téhož
kontextového okna a model mezi nimi nemá tvrdou hranici. (Multimodální modely
čtou i obrázky, ale i tam se injection přenáší — scéna to nevyvrací.)

**S39–S40** bílý text na bílém pozadí — hypotetický příklad, **OK**; je to
zdokumentovaná technika (Brave ji popisuje mezi způsoby skrytí instrukcí).

**S41** *„it may simply do it"* — **OK**, opatrně formulováno.

## Brave × Perplexity Comet (S42–S45)

Zdroj (primární): Artem Chaikin, Shivan Kaul Sahib (Brave),
[*Agentic Browser Security: Indirect Prompt Injection in Perplexity Comet*, 20. 8. 2025](https://brave.com/blog/comet-prompt-injection/).

**S42** *„In August 2025, researchers at Brave hid instructions in a Reddit
comment, behind a spoiler tag."* — **OK.** Instrukce v komentáři na Redditu
*„behind the spoiler tag"*. Zveřejněno 20. 8. 2025; Perplexity nahlášeno už
25. 7. 2025 — „In August 2025" platí pro zveřejnění, ne pro nález. Pokud by
se chtělo přesně: *„In 2025"* nebo *„In the summer of 2025"*. Nechat.

**S43** *„Then they asked an AI browser, Perplexity's Comet, to summarise the
page."* — **OK.** Uživatel klikne na *„Summarize the current webpage"*.

**S44** *„It found the hidden instructions, followed them, and handed the
attacker a login code for the user's account."* — **OK.** Postup podle Brave:
agent (1) přešel na stránku účtu Perplexity a vyčetl e-mail, (2) přes
podvržený doménový zápis (`perplexity.ai.` s tečkou) vyvolal zaslání
jednorázového kódu, (3) otevřel Gmail, kde byl uživatel přihlášen, a kód
přečetl, (4) e-mail i kód vyvěsil jako odpověď pod týž komentář na Redditu.
S nimi mohl útočník převzít účet Perplexity. „Login code for the user's
account" je přesné. Byl to **demonstrační útok výzkumníků**, ne skutečná oběť
— scénář to říká správně („researchers").

**S45** *„Nobody hacked the browser. Nobody stole a password."* — **OK**
v rétorickém smyslu: nevyužila se softwarová chyba prohlížeče ani heslo;
odcizen byl jednorázový kód, ne heslo.

**S46** *„It's called prompt injection. And so far, nobody has a complete fix.
Even companies building these agents say it may never be fully solved."* —
**OK.** OpenAI, *Hardening Atlas against prompt injection*, 22. 12. 2025:
*„Prompt injection, much like scams and social engineering on the web, is
unlikely to ever be fully 'solved.'"* Britské NCSC (prosinec 2025): útoky
*„may never be totally mitigated"*. Brave v tomtéž článku: Perplexity první
opravu (27. 7.) nedotáhl, problém přetrvával i po zveřejnění.
[TechCrunch, 22. 12. 2025](https://techcrunch.com/2025/12/22/openai-says-ai-browsers-may-always-be-vulnerable-to-prompt-injection-attacks/),
[Fortune, 23. 12. 2025](https://fortune.com/2025/12/23/openai-ai-browser-prompt-injections-cybersecurity-hackers/).
Blog OpenAI vrátil při čtení 403; citát ověřen přes TechCrunch a Fortune,
které ho uvádějí shodně.

## Závěr (S47–S51)

Interpretační. **OK.**

## Neověřeno primárně

- **Mythos Preview 16 h** — z příspěvku METR na X přes The Decoder a ze stránky
  metr.org/time-horizons (graf, hodnotu textově nečte). Číslo 1 045 min jen
  z agregátoru.
- **Horizonty veřejných modelů 2026** (~6 h) — jen agregátor llmlearner;
  nemusí být úplný (chybí v něm některé modely z 2026).
- **Lemkinovy citace** (rollback, code freeze, 1 206 / 1 196) — přes The Register,
  eWeek a AIID, ne přímo z X.
- **Citát OpenAI** — přes TechCrunch a Fortune (openai.com vrátil 403).
