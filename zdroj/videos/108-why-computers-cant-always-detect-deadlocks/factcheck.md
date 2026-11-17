# Fact check — 108 Why Can't Computers Predict Every Deadlock?

Ověřováno nad `script 0.3.md` (2026-10-14), opravy jsou ve `script 0.4.md`.
Čísla scén platí pro v0.3 i v0.4 (počet scén se nezměnil).

## Opraveno z v0.3

| scéna | v0.3 | v0.4 | proč |
|---|---|---|---|
| S05 | „Computers are good at spotting a deadlock" | „…**often** good at…" | zámkové deadlocky v databázi ano; ne každé uváznutí (čekání na zprávu, aktivní čekání) má graf, ve kterém jde smyčku najít |
| S06 | „For every possible program, the answer is no." | „For many programs, yes. But a method that works for every possible program can't exist." | **dvojznačný kvantifikátor**: šlo to slyšet jako „u žádného programu to nejde". Nemožnost se týká obecného prediktoru, ne nástrojů, které deadlocky úspěšně hledají (připomínka uživatele k S05–S06) |
| S17 | „the victim usually just runs again" | „the victim can simply try again" | SQL Server oběť **sám znovu nespouští**; aplikace má chybu 1205 zachytit a transakci poslat znovu (Microsoft: „can retry the transaction, which usually completes…") |
| S26 | „Alan Turing looked at a question that sounds even simpler" | „…showed that some questions about programs can't be answered by any program. The most famous one sounds even simpler." | Turing 1936 halting problem **v dnešní podobě nevyslovil** — dokázal nerozhodnutelnost příbuzných otázek (zda stroj je „circle-free", zda někdy vytiskne daný symbol). Název a dnešní znění: Davis 1958 (neformálně Kleene 1952) |
| S28 | „This became known as the halting problem. And Turing proved that no program…" | „It's now called the halting problem. And no program can answer it…" | totéž — připsat přímo Turingovi je běžné, ale programátor to může vytknout |
| S42 | „And Turing proved that's impossible." | „And that's exactly what can't be done." | totéž |

## Ověřeno

| scéna | tvrzení | ověření | závěr |
|---|---|---|---|
| S01 | „the rule many countries use: give way to the car on your right" | Vídeňská úmluva o silničním provozu 1968, čl. 18 odst. 4 písm. a): v zemích s pravostranným provozem dává řidič na křižovatce bez úpravy přednost vozidlům zprava ([Wikipedia: Priority to the right](https://en.wikipedia.org/wiki/Priority_to_the_right)). Britská Highway Code ho nemá, proto „many countries", ne obecně | ✅ |
| S02–S03 | čtyři auta naráz → každý čeká na toho vpravo → nikdo nepojede | logika pravidla: čtyři vztahy „čekám na pravého" tvoří kruh. **Ilustrace**, ne popis zákona — v praxi to řidiči řeší dohodou (S60) | ✅ jako ilustrace |
| S08–S11 | zámek, dvě transakce, účet/objednávka v opačném pořadí; prolnutí jen někdy | učebnicový příklad; Microsoft uvádí týž tvar (T1 drží r1 a čeká na r2, T2 obráceně) | ✅ |
| S13 | „Databases… keep watch" | SQL Server: lock monitor hledá deadlocky **každých 5 s**, při častých deadlockách až po 100 ms ([Microsoft Learn, Deadlocks guide](https://learn.microsoft.com/en-us/sql/relational-databases/sql-server-deadlocks-guide)) | ✅ |
| S13–S14 | „map of who is waiting for whom", smyčka = deadlock | tentýž zdroj: „Wait-for graph", „Because these dependencies form a cycle, there's a deadlock". U zámků s jedním držitelem smyčka deadlock skutečně znamená | ✅ |
| S15 | vybere jednu úlohu a zahodí její práci | „chooses one of the tasks as a victim and terminates its transaction with an error" — transakce se vrátí (rollback) | ✅ |
| S16 | SQL Server poraženému řekne, že byl vybrán jako oběť a má to zkusit znovu | chyba 1205: *„Transaction (Process ID 51) was deadlocked on lock resources with another process and has been chosen as the deadlock victim. Rerun the transaction."* Oběť: nižší `DEADLOCK_PRIORITY`, pak nejlevnější rollback, pak náhodně | ✅ |
| S26 | 1936, mladý matematik | „On Computable Numbers", Proc. London Math. Soc. (2) 42, 1936–37; Turing narozen 23. 6. 1912 → 23–24 let | ✅ |
| S27–S28 | halting problem: žádný program ho nerozhodne pro všechny případy | Davis 1958 (Computability and Unsolvability), důsledek Turinga 1936 ([arXiv 2407.00680](https://arxiv.org/html/2407.00680v3)) | ✅ po opravě atribuce |
| S29–S32 | „rozporný program" se zeptá kontroly sám na sebe a udělá opak | standardní podání (Strachey, *An impossible program*, Computer Journal 1965; učebnice). Uváděno jako „the idea behind the proof", ne jako Turingův důkaz | ✅ |
| S36–S44 | převod halting → deadlock | logika: nový program = simulace starého v **jednom vlákně bez zámků** (sama neuvázne) + na konci **zaručený** deadlock (každá úloha vezme svůj zámek, počká, až ho vezme i druhá, sáhne po cizím). Uvázne ⇔ starý program skončí. Když starý program při simulaci sám „uvázne", simulace prostě nekončí — tedy správně „nezastaví se" | ✅ |
| S46 | konečná paměť → v principu jde zkontrolovat | stroj s pevnou pamětí je konečný automat; dosažitelnost stavu (i deadlocku) je rozhodnutelná prohledáním | ✅ |
| S47 | 8 GB paměti → počet stavů má ~20 miliard číslic | 2^bitů má bitů × log₁₀2 číslic: **8 GiB → 20 686 623 784**, 8 GB (10⁹) → 19 265 919 722. Jen RAM, bez registrů a disku — proto „the memory of a laptop" | ✅ |
| S48 | atomů v pozorovatelném vesmíru → číslo s ~80 číslicemi | běžný odhad 10⁷⁸–10⁸² (nejčastěji 10⁸⁰, tedy 81 číslic) | ✅ „about eighty" |
| S50 | Turingova mez platí pro programy, které si mohou říct o další paměť | Turingův stroj má neomezenou pásku; nerozhodnutelnost platí pro tento model, ne pro pevně omezený stroj | ✅ |
| S52–S53 | pevné pořadí zámků → smyčka nevznikne | Havender 1968; Coffman et al. 1971 — porušení podmínky kruhového čekání. Omezeno na „if every task really sticks to that order" | ✅ |
| S54 | timeout, všechny zámky naráz, oběť a nový pokus | Coffmanovy podmínky: hold-and-wait (všechno naráz), no preemption (timeout, oběť). Timeouty: PostgreSQL `lock_timeout`, InnoDB `innodb_lock_wait_timeout` | ✅ |
| S55 | Amazon, nástroj prohledá všechny stavy malého návrhu, chyba až po 35 krocích ve správném pořadí | Newcombe, Rath, Zhang, Munteanu, Brooker, Deardeuff: *Use of Formal Methods at Amazon Web Services* (tech. zpráva 29. 9. 2014; CACM 58(4), 2015). DynamoDB, model checker TLC nad TLA+: *„a bug that could lead to losing data… the shortest error trace exhibiting the bug contained 35 high level steps"*; prošla předtím design review, code review i testy. **Nebyl to deadlock** — proto „a bug" | ✅ |
| S56–S58 | nástroj na libovolný program musí něco obětovat: falešné poplachy, přehlédnutí, nebo žádnou odpověď | přímý důsledek nerozhodnutelnosti (Riceova věta pro netriviální vlastnosti chování) | ✅ |
| S60–S62 | řidič zamává = databáze vybere oběť | analogie (preempce) | ✅ |

## Poznámky k výslovnosti (pro TTS)

- `1936` → `nineteen thirty-six` je v `project.json`.
- `SQL` — ověřit poslechem, jestli Kokoro hláskuje „S-Q-L"; obojí je
  správně, „sequel" je u SQL Serveru běžnější.
