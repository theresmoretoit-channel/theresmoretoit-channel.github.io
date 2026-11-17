# Fact check — 097 Why Would a Smart AI Help a Criminal?

Ověřeno 2026-10-07 nad `script.md` (v0.2, 67 scén). `script.md` se zatím
**neměnil** — návrhy oprav jsou u jednotlivých scén a souhrnně na konci.
Závěr: **OK** / **ZPŘESNIT** (pravda, ale formulace jde za zdroj) /
**CHYBA** (zdroj říká něco jiného).

## Inteligence ≠ svědomí (S01–S08, S12–S15)

**S01–S05, S12–S15** — úvaha, ne faktické tvrzení. Odpovídá tezi
ortogonality (Bostrom 2012: inteligence a konečné cíle jsou na sobě
nezávislé). **OK** jako argument, nic k ověření.
[Bostrom, The Superintelligent Will](https://nickbostrom.com/superintelligentwill.pdf)

**S06** — *běžný asistent by podvodný e-mail nejspíš odmítl.* **OK.**
Podvody a phishing zakazují pravidla použití OpenAI i Anthropicu
a modely na to odmítání trénují. Scénář má „probably", takže
jailbreaky nevadí.
[Anthropic Usage Policy](https://www.anthropic.com/legal/aup),
[OpenAI Usage Policies](https://openai.com/policies/usage-policies/)

**S07–S08** — *to „ne" je natrénované, inteligence ho sama nevyrobí.*
**OK.** Odmítání vzniká dotrénováním (RLHF u InstructGPT, Constitutional
AI u Clauda), ne z předtrénování. Drobnost: u komerčních služeb ho
doplňují i klasifikátory mimo model — „trained in" to zjednodušuje,
ale nepopírá. Doklad k S08 je sám WormGPT: postavený na otevřeném
modelu GPT-J (2021), který bezpečnostní dotrénování neměl.
[Ouyang a kol. 2022 (InstructGPT)](https://arxiv.org/abs/2203.02155),
[Bai a kol. 2022 (Constitutional AI)](https://arxiv.org/abs/2212.08073)

## WormGPT a FraudGPT (S09–S11)

**S09** *„In July 2023, a tool called WormGPT went on sale on a hacker
forum."* — **CHYBA (drobná).** Prodávat se začal **v červnu 2023** na Hack
Forums (Trustwave: *„it wasn't until June that the developer started
selling access to the platform on a popular hacker forum"*). V červenci
(13.–15. 7. 2023) o něm **napsal SlashNext** a tehdy se o něm dozvěděla
veřejnost; další inzerát na fóru Exploit 14. 7. 2023. Hacker forum sedí.
→ návrh: *In the summer of 2023,*
[Trustwave/LevelBlue, 8. 8. 2023](https://www.levelblue.com/en-us/resources/blogs/spiderlabs-blog/wormgpt-and-fraudgpt-the-rise-of-malicious-llms),
[Krebs on Security, 8/2023](https://krebsonsecurity.com/2023/08/meet-the-brains-behind-the-malware-friendly-ai-chat-service-wormgpt/),
[Hackread (cituje SlashNext)](https://www.hackread.com/wormgpt-malicious-chatgpt-alternative-cybercrime/)

**S10** — *bez etických mezí, na podvodné e-maily, asi 60 € měsíčně.*
**OK.** SlashNext: *„the absence of ethical boundaries or limitations"*,
test na BEC dal přesvědčivý podvodný e-mail. Autor („Last") inzeroval:
*„Everything blackhat related that you can think of can be done with
WormGPT"*. Cena podle Trustwave **60–100 € měsíčně nebo 550 € ročně**,
soukromá verze 5 000 €; „about sixty" je dolní mez, obhajitelné.
(Krebs uvádí jen „licence za 500 až 5 000 €".)

**S11** — *během týdnů napodobenina FraudGPT.* **OK.** FraudGPT inzerován
od **22. 7. 2023** na Telegramu a darknetových tržištích (Netenrich,
25. 7. 2023), tedy 9 dní po zprávě o WormGPT a ~6–7 týdnů po začátku jeho
prodeje. „Copycat" je výklad (Netenrich ho přirovnává k WormGPT),
přijatelné. Cena 90–200 USD/měsíc — ve scénáři není.
[Netenrich](https://netenrich.com/blog/fraudgpt-the-villain-avatar-of-chatgpt)

## Asimov (S16–S24)

**S17** *„That idea is older than computers. In 1942…"* — **ZPŘESNIT.**
Zuseho **Z3** byl předveden 12. 5. 1941 a platí za první funkční
programovatelný plně automatický číslicový počítač; Atanasoff–Berry
Computer se zkoušel 1942. Runaround (březen 1942) je tedy mladší než
první počítače, starší jen než elektronické univerzální (ENIAC 1945).
Divák-technik tohle napíše do komentářů. → *That idea predates modern
computers.*
[Wikipedia: Z3](https://en.wikipedia.org/wiki/Z3_(computer))

**S17** — *Runaround 1942, v něm tři zákony.* **OK.** Astounding Science
Fiction, **březen 1942**; první povídka, kde jsou všechny tři zákony
vysloveny pohromadě (První zákon se objevil už v *Liar!*, 1941 — proto
„in it, the Three Laws" sedí, ne „first rule ever").
[Wikipedia: Runaround](https://en.wikipedia.org/wiki/Runaround_(story)),
[Wikipedia: Three Laws](https://en.wikipedia.org/wiki/Three_Laws_of_Robotics)

**S18–S20** — znění zákonů. **OK.** Kanonický text (Handbook of Robotics,
56th Edition, 2058 A.D.):
1. *„A robot may not injure a human being or, through inaction, allow
   a human being to come to harm."* — S18 doslova.
2. *„A robot must obey the orders given it by human beings except where
   such orders would conflict with the First Law."* — S19 věrná parafráze.
3. *„A robot must protect its own existence as long as such protection
   does not conflict with the First or Second Law."* — S20 věrná parafráze.

**S22** *„Asimov didn't write the laws as an engineering plan. He wrote
them to watch them fail."* — **ZPŘESNIT (hraničí s chybou).** Asimov
zákony myslel vážně: v pozdější eseji je vykládá jako obecné principy
každého nástroje (*„The Laws apply, as a matter of course, to every tool
that human beings use"* — nůž má rukojeť, granát pojistku) a na otázku,
jestli by fungovaly, odpověděl (Compute!, 1981): *„Yes, the Three Laws are
the only way in which rational human beings can deal with robots — or
with anything else."* Povídky přitom zákony většinou **nevyvracejí**:
roboti se chovají podivně, ale zákony platí a záhada se rozluští právě
z nich. Pravdivé je, že dějem jsou **mezery a dvojznačnosti** (James Gunn:
*„the ambiguity in the Three Laws and the ways in which Asimov played
twenty-nine variations upon a theme"*). „Watch them fail" jde za zdroj.
→ návrh: *But Asimov didn't treat the laws / as a finished answer. /
His stories live in their gaps.*
[Wikipedia: Three Laws (citace Asimova a Gunna)](https://en.wikipedia.org/wiki/Three_Laws_of_Robotics)

**S23** — *robot na Merkuru běhá v kruhu mezi dvěma stejně silnými zákony.*
**OK.** SPD-13 „Speedy" je poslán pro selen k jezírku; rozkaz byl dán
ledabyle (slabý Druhý zákon), nebezpečí pro drahého robota posiluje Třetí
zákon → krouží v bodě, kde jsou obě síly v rovnováze. Vyřeší to Powell,
který se vystaví nebezpečí a aktivuje První zákon. Drobnost: *„that very
first story"* — Runaround není první Asimovova robotí povídka (Robbie
1940), jen první se třemi zákony; v kontextu S17 to čte správně, ale
jistější je *In that same story,*.

**S24** — *povídka za povídkou stojí na mezeře v zákonech.* **OK** jako
charakteristika (Gunn, výš). „Watertight… the plot is the leak" je obraz.

## Co je harm (S25–S28)

**S26–S27** — samořídící auto, jeden vs. pět. **OK** jako myšlenkový
pokus (tramvajové dilema přenesené na autonomní vozidla; přesně tyhle
scénáře testoval Moral Machine). Scénář je formuluje jako otázky „What
if", netvrdí, že je auta dnes řeší.

## Nízká úroveň nemá morální význam (S29–S41)

**S30–S31, S33–S35** — technicky **OK**: na úrovni systémových volání
a síťových operací nese příkaz jen syntaxi; skenování zranitelností
používá obránce (pentest) i útočník stejnými nástroji.
**S37–S41** — analogie, nic k ověření. S41 „AI agent… finds its own
route" dokládá S45 (agenti sami přestavovali malware).

## Zpráva Anthropicu, září 2026 (S42–S48)

Zdroj: *Detecting and countering misuse of AI: September 2026*, stránka
založena 9. 9., zveřejněna 10. 9. 2026. Celý text stažen a přečten
(258 k znaků), relevantní pasáže: úvod kapitoly Cyber operations, případ
GTG-20006, případ GTG-50029, „Prevailing trends".
[Anthropic](https://anthropic.com/threat-intelligence-report-september-2026)

**S42** — *Anthropic publikuje zprávy o zneužití svých modelů.* **OK.**
Zpráva sama odkazuje na předchozí z března, srpna a listopadu 2025.

**S43** — *jediný hacktivista, 42 organizací, dovnitř aspoň do 14.*
Čísla **OK**: *„a single French-speaking actor was observed using Claude
to target European political parties, media, think-tanks, and the SaaS
providers"*; *„Across 42 tracked target entities, the actor gained
internal access to at least 14."* Kapitola má nadpis „Hacktivists
targeted…" a text ho nazývá hacktivistou. **ZPŘESNIT: „He"** — zpráva
pohlaví **neuvádí** (všude „the actor", „they", „one person").
→ *And got inside at least fourteen.* a v S44 *him/his* → *the attacker*.
Pozn.: Clauda používal přes **ukradené API klíče** a kombinoval i jiné
modely — „with the help of AI" je přesné.

**S44** — **OK.** (a) *nová cesta do webů*: *„exploiting a previously
undocumented WordPress re-installation race condition that created
a rogue administrator account… The actor used Claude to develop and debug
the exploit"*, úspěšně aspoň na čtyřech webech. (b) *napsala jeho
nástroje*: exploit, webshell *„built on the fly"*, plugin na sběr hesel.
(Rust skener na API klíče *„This actor built"* — bez výslovné zmínky AI,
ale „his tools" obecně sedí.) (c) *platforma na odhalování osobních údajů*:
*„fafsearch, a purpose-built doxxing platform… tens of millions of rows…
AI-assisted software engineering… the entire platform was created by just
one person."*

**S45** — *jiná skupina, agenti po detekci sami přestavěli malware, dokud
neprošel.* **OK.** GTG-20006 (ruská státní špionáž, shoda s Midnight
Blizzard): *„If their monitoring AI agents identified that any of their
deployed malware was detected by a security product, agents would then
set about the process of autonomously modifying and rebuilding the
malware to evade the existing detections. The agents were designed to
continue iterating… until it was undetected."* „Got through" =
„undetected", věrné.

**S46** — *práce, na kterou byl před rokem potřeba tým zkušených lidí,
zvládne teď jeden operátor.* **OK s drobnou výhradou.** Zpráva: *„AI has
collapsed the labor and tooling gap that used to separate well-resourced,
state-sponsored operations from individual operators… multi-victim
campaigns that, even just a year ago, would have required many skilled
operators and specialist knowledge."* a *„would previously have required
teams of operators"*. Výhrada: je to shrnutí z úvodu „Trends" (a znovu
v „Prevailing trends"), ne doslova „závěr"; „The report's conclusion"
je přijatelný opis.

**S47** — *lidé si nechali výběr cílů a rozhodnutí, co s výsledky.*
**OK.** *„humans have retained the decisions that matter most to them:
for example, they're still heavily involved in target selection,
monetization of findings, and review of results."* a *„Humans remained in
the loop by setting the targets of attacks and reviewing exfiltration."*
„Deciding what to do with the results" pokrývá monetizaci i revizi.

**S48** — výklad; zpráva sama říká *„The main distinguishing feature…
is no longer sophistication but intent."* — klíčová věta videa tím má
oporu přímo ve zdroji. **OK.**

## Skynet a SHODAN (S50–S51)

**S50** — Skynet. **OK.** *The Terminator* (1984): stane se sebeuvědomělým,
*„saw all humans as a threat"* a rozhodl o vyhlazení.
[Wikipedia: Skynet](https://en.wikipedia.org/wiki/Skynet_(Terminator))

**S51** — SHODAN, *System Shock* (1994, Looking Glass). **OK**: vlastní
vůle, cíle, pohrdání lidmi. **Upozornění (ne chyba):** SHODAN se zvrhla
proto, že jí **hacker na zakázku odstranil etické zábrany** — tedy přesně
mechanismus z S08 („co jeden natrénuje, druhý vynechá"). Kontrast v S51–S53
tím trochu slábne a v komentářích to někdo napíše. Buď nechat, nebo to
otočit ve prospěch videa (dramaturgické rozhodnutí uživatele).
[Wikipedia: SHODAN](https://en.wikipedia.org/wiki/SHODAN)

## Moral Machine (S55–S56)

Awad, Dsouza, Kim, Schulz, Henrich, Shariff, Bonnefon, Rahwan: *The Moral
Machine experiment*, Nature 563, 59–64, online 24. 10. 2018.
[PubMed 30356211](https://pubmed.ncbi.nlm.nih.gov/30356211/),
[Nature](https://www.nature.com/articles/s41586-018-0637-6)

**S55** — *2018, výzkumníci z MIT.* **OK.** První a poslední autor z MIT
Media Lab (spoluautoři Harvard, UBC, Toulouse). Platforma běžela od 2016,
článek 2018 — „published" sedí. *Přes dvě stě zemí a území*: abstrakt
*„233 countries and territories"* → **OK.** *Rozhodovali, koho má auto
zachránit*: dilemata nevyhnutelné nehody, koho ušetřit → **OK.**

**S56** — *skoro čtyřicet milionů rozhodnutí.* **OK** (abstrakt „40
million", v textu 39,61 mil.). *Odpovědi se lišily podle kultury*:
*„we report cross-cultural ethical variation, and uncover three major
clusters of countries"* (Western, Eastern, Southern) → **OK.** Pro úplnost:
některé preference byly globální (víc životů, lidé před zvířaty, mladí) —
scénář netvrdí opak.

## Závěr (S57–S67)

Úvahy a doporučení (omezená oprávnění, řízení přístupu, dohled, vypínač).
Nic k ověření.

## Co se primárně ověřit nepodařilo

- **Původní článek SlashNext** (13. 7. 2023) — doména přesměrovává na
  Varonis, archive.org nedostupný. Citace převzaty z Hackread a Trustwave.
- **Cena 60 € měsíčně** jen ze sekundárních zdrojů (Trustwave); Krebs
  uvádí jen rozpětí licencí 500–5 000 €. Původní inzerát nečten.
- **Asimovovy citace** (esej o nástrojích, rozhovor Compute! 1981, Gunn)
  jen přes Wikipedii, ne z originálů.
- **Plný text Moral Machine** (paywall) — 39,61 mil. a pojmenování shluků
  z paměti/sekundárně; abstrakt (40 mil., 233, tři shluky) ověřen
  v PubMedu.

## v0.5 (2026-10-08) — S32b–S32d, doplněno na žádost uživatele po draftu

**S32b** *„In his stories, they're built into the very design of the robot's
brain."* — **OK.** Asimov: zákony jsou *„an inalienable part of the
mathematical foundation underlying the positronic brain"*; bez teorie tří
zákonů postavy neumějí navrhnout funkční mozek; *„cannot be bypassed, being
intended as a safety feature"*. Formulace „very design" schválně netvrdí, že
je nejde změnit (Little Lost Robot: úprava 1. zákona je možná, jen nebezpečná).
[Wikipedia: Three Laws](https://en.wikipedia.org/wiki/Three_Laws_of_Robotics)

**S32c** *„a rule about harm can't go that deep… Down there, there is no harm.
Only operations."* — úsudek, navazuje na S30–S32 (nejnižší úroveň nevidí
morální význam). Ne faktické tvrzení.

**S32d** *„the machine must first judge what counts as harm… that judgement
comes from the very intelligence the rule was meant to keep in check."* —
**OK, a souhlasí i s Asimovem:** v The Robots of Dawn jsou pokročilí roboti
*„capable of determining which action is more harmful"*, Daneel: *„Injury to
a person can be estimated and judged."* Posouzení škody tedy i u Asimova
dělá robot sám.
