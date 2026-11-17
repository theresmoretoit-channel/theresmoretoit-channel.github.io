# Fact check — Are You a Hacker Just Because You Opened a Terminal?

Proti `script.md` verze 0.3 (72 scén). Prošlo **každé** ověřitelné tvrzení,
ne jen ta, která vypadala riziková — riziko se pozná až po ověření.

Legenda: ✅ doloženo · 🎭 záměrná nadsázka (popis filmové konvence, ne tvrzení
o světě) · 💬 hodnotový soud, nedokládá se · ⚠️ pozor při vizuálu

---

## S06 — `sudo userdel -r john`

*Kotva: „A terminal says this instead."*

**Tvrzení:** grafické rozhraní řekne „delete user", terminál tohle.

✅ `userdel -r` je skutečný příkaz; `-r` odstraní i domovský adresář.
Vyžaduje práva roota, odtud `sudo`.

⚠️ **Do hlasu nepatří** — Kokoro to čte jako „pseudo-userdle are John"
(naměřeno, viz `notes.md`). Scéna říká „a terminal says this instead"
a příkaz je jen v obraze.

## S08, S09 — historie vzhledu terminálu

*Kotva: „green or amber phosphor text"*

**Tvrzení:** rané počítače neměly grafické rozhraní; mluvilo se s nimi přes
textové terminály; ty měly tmavé obrazovky se zeleným nebo ambrovým
fosforem; nebyl to pokus vypadat cool, ale vlastnost technologie.

✅ Fosfory jsou normalizované: **P1 zelený, P3 ambrový, P4 bílý**
(Wikipedia, *Monochrome monitor*). Volba byla technická, ne stylová —
ambrová se považovala za ergonomičtější kvůli menší únavě očí,
P4 se převzal z televizí.

⚠️ Scénář historii **zhušťuje**: před interaktivními terminály byly děrné
štítky a dávkové zpracování. Věta „lidé s nimi mluvili přes textové
terminály" platí pro éru interaktivních počítačů, ne pro úplný počátek.
Není to nepravda, jen zkratka — a scéna ji nepotřebuje přesnější.

## S13, S70 — „nine hundred words a minute"

*Kotva: „nine hundred words a minute"*

🎭 **Záměrná nadsázka**, a scéna to dává najevo (popisuje hollywoodskou
konvenci). Pro doložení, o kolik jde:

| | wpm |
|---|---|
| běžný uživatel, přepis (studie 1999) | 32,5 |
| profesionální písařka | 43–80 |
| rekord na běžné klávesnici, krátký úsek | přes 300 |
| rekord na stenotypu | 360 |
| **scénář** | **900** |

Tedy zhruba **2,5× nad nejrychlejším doloženým výkonem vůbec**. Jako vtip
to obstojí, jako tvrzení by neobstálo — a scénář ho jako tvrzení nepodává.

## S16–S18 — „turned off password logins six months ago"

*Kotva: „turned off password logins six months ago"*

✅ Odpovídá `PasswordAuthentication no` v konfiguraci SSH serveru. Běžná
a doporučovaná praxe (přihlašování klíčem místo hesla).

## S21–S24 — terminál je rozhraní, ne nástroj na hackování

*Kotva: „The screwdriver is not the criminal."*

💬 Teze videa. Není to empirické tvrzení, nýbrž definice — a šroubovák
je analogie, ne důkaz.

✅ Dílčí fakt, na kterém stojí: tytéž nástroje se skutečně objevují
na obou stranách. `nmap`, `ssh`, čtení logů a `tcpdump` používá správce
i útočník; rozdíl je v oprávnění, ne v programu.

## S25–S28 — etymologie slova *hacker*

*Kotva: „a much older history than modern cybercrime"*

**Tvrzení:** slovo má mnohem starší historii než dnešní kyberkriminalita;
původně to byl někdo, kdo rád zkoumal systémy a nacházel nečekaná řešení;
dnes může znamenat výzkumníka, penetračního testera, útočníka, nebo
prostě člověka, který ví znepokojivě moc o Linuxu.

✅ **RFC 1392, *Internet Users' Glossary*, leden 1993** — tedy dokument
starší než většina dnešního významu:

> **hacker:** „A person who delights in having an intimate understanding
> of the internal workings of a system, computers and computer networks
> in particular."
>
> **cracker:** „An individual who attempts to access computer systems
> without authorization. These individuals are often malicious, as opposed
> to hackers…"

Glosář výslovně upozorňuje, že se „hacker" často **mylně** používá tam,
kde by patřilo „cracker". To doslova doládá větu „the word has a much
older history than modern cybercrime".

⚠️ Tradiční původ (MIT, Tech Model Railroad Club, konec 50. let)
**v tomhle průchodu ověřený nebyl** a scénář ho netvrdí — žádné datum
ani místo nejmenuje. Kdyby se do storyboardu dostal letopočet, musí
se doložit napřed.

## S29b, S32, S33, S34 — co dělá nmap

*Kotva: „network discovery and security auditing"*

**Tvrzení:** „a tool for network discovery and security auditing";
namíříš ho na stroj a ptáš se, co vystavuje síti; řekne, které porty
jsou otevřené; porty odpovídají službám; není to automaticky útok.

✅ **Doslovná shoda s vlastním popisem projektu** (nmap.org):

> „Nmap ("Network Mapper") is a free and open source utility for
> **network discovery and security auditing**."

✅ Manuálová stránka (nmap.org/book/man.html) totéž jinými slovy
(„network exploration and security auditing") a popisuje stavy portů:
**open** (aplikace naslouchá), **closed**, **filtered** (blokuje firewall),
**unfiltered**, plus kombinace `open|filtered`.

✅ „Porty odpovídají síťovým službám" — přiřazení vede IANA
(*Service Name and Transport Protocol Port Number Registry*).

## S38–S41 — `/etc/passwd` versus `/etc/shadow`

*Kotva: „which is much more restricted"*

**Tvrzení:** soubor obsahuje informace o účtech, ale na moderním Linuxu
jsou vlastní otisky hesel jinde — v `/etc/shadow`, který je mnohem
přísněji omezený. Vidět `/etc/passwd` tedy není totéž co objevit hesla.

✅ **Změřeno přímo na stroji, kde video vzniká:**

```
/etc/passwd  -rw-r--r--  root:root      (644, čitelný pro všechny)
/etc/shadow  -rw-r-----  root:shadow    (640, pro ostatní nečitelný)
```

To je doklad slova „much more restricted" — ne odhad.

✅ Slovo **„modern"** je ve scénáři důležité a je tam správně: historicky
`/etc/passwd` otisky hesel **obsahoval** (odtud jeho jméno) a oddělení
do `/etc/shadow` je pozdější. Bez toho slova by věta nebyla přesná.

## S42, S43 — lámání hesla

*Kotva: „you let the computer try candidates"*

🎭 „cracks a password in approximately fourteen seconds" popisuje filmovou
scénu, ne skutečnost — scéna to říká výslovně („Another classic scene").

✅ Popis skutečného postupu sedí: útočník má **otisk** a **slovník**
a nechá počítač zkoušet kandidáty (offline slovníkový útok). Doba je
otevřená — od okamžiku po nikdy, podle síly hesla a rychlosti hardwaru.

## S46 — „someone solved it eleven years ago"

*Kotva: „someone solved it eleven years ago"*

✅ Aritmeticky v pořádku: Stack Overflow běží od září 2008, takže
v roce 2026 může být odpověď stará jedenáct let (2015). Je to vtip,
ale nesedělo by třeba „dvacet".

## S48–S53 — `sudo rm -rf /` a nebezpečné příkazy

*Kotva: „operating recursively on slash is dangerous"*

**Tvrzení scénáře (moje oprava proti zdroji):** moderní systém to odmítne;
odpoví, že rekurzivní operace na `/` je nebezpečná; a chce druhý přepínač.

✅ **Doloženo třemi nezávislými způsoby:**

1. **Manuál GNU coreutils** k `rm`: *„Fail upon any attempt to remove the
   root directory, `/`, when used with the `--recursive` option.
   **This is the default behavior.**"*
2. **Zdrojový kód** `src/rm.c`, řádek 236: `bool preserve_root = true;`
3. **Testovací sada** coreutils `tests/rm/r-root.sh`, řádky 194–195 —
   doslovné očekávané znění hlášky:

```
rm: it is dangerous to operate recursively on '/'
rm: use --no-preserve-root to override this failsafe
```

✅ **Kdy se to změnilo:** NEWS coreutils.

| verze | |
|---|---|
| **5.1.0** (2003-12-21) | zavedeny `--preserve-root` / `--no-preserve-root`, výchozí bylo **`--no-preserve-root`** — `rm -rf /` tedy tehdy opravdu mazal |
| **6.6** (2006-11-22) | *„rm now rejects attempts to remove the root directory, e.g., 'rm -fr /' now fails without removing anything."* |

Pojistka je tedy v systémech **od konce roku 2006**, což slovo „modern"
ve scénáři pokrývá s velkou rezervou.

⚠️ **Pro storyboard:** když se ta hláška dostane do obrazu, musí být
opsaná **přesně** podle rámečku výš. Scénář ji jen parafrázuje, obraz
by ji citoval — a citace se nesmí vymyslet.

⚠️ **Nedoloženo a scénář to netvrdí:** jestli tohle chování vyžaduje
POSIX. Nezkoumalo se; ve scénáři o tom není ani slovo.

💬 „The commands that really destroy things are duller" — hodnotový soud,
ale opřený o to, že pojistka existuje jen pro `/`, ne pro špatný adresář
nebo špatný disk. To je fakt, ne dojem.

## S54–S58 — jak vypadá skutečný útok

*Kotva: „might not look like hacking at all"*

**Tvrzení:** může jít o ukradené heslo, phishing, nezáplatovaný server,
uniklý API klíč, heslo použité znovu odjinud; útočník nemusí potřebovat
terminál, stačí se přihlásit do webového rozhraní.

✅ Všechno jsou to doložené a běžné vektory.

✅ Scénář **záměrně neříká „většinou"**, nýbrž „might involve" — je to
výčet možností, ne statistika, takže žádné číslo dokládat nemusí.
Kdyby se na to ptal divák v komentářích, referencí je *Verizon Data
Breach Investigations Report*, který dlouhodobě řadí zneužití přihlašovacích
údajů a phishing mezi nejčastější vstupní cesty. **Do videa se to netahá** —
tvrzení by pak bylo silnější než doklad, který jsem ověřoval.

## S59–S67 — stereotyp a závěr

*Kotva: „whether you have permission to do it"*

💬 Celé hodnotové, a je to pointa videa: rozdíl mezi správou a hackováním
není v barvě terminálu, počtu monitorů, rychlosti psaní ani v mikině,
nýbrž v tom, **co děláš a jestli k tomu máš oprávnění**.

✅ Jediné faktické tvrzení uvnitř: nic z toho vyjmenovaného (mikina, tmavá
místnost, svítící klávesnice) s hackováním technicky nesouvisí. Triviálně
pravdivé.

---

## Shrnutí

| | |
|---|---|
| ověřitelných tvrzení | 14 |
| ✅ doloženo | 11 |
| 🎭 záměrná nadsázka, označená ve scénáři | 2 (rychlost psaní, čtrnáct sekund) |
| ⚠️ zkratka, ne chyba | 1 (historie terminálů v S08) |
| **nalezených chyb ve verzi 0.3** | **0** |

Jediná věcná chyba tohohle scénáře byla ve **zdroji** a opravila se už
při převodu: naznačoval, že `sudo rm -rf /` systém prostě smaže.
Podrobnosti v `notes.md`.

### Co si hlídat ve storyboardu

1. Hláška `rm` se v obraze musí **citovat přesně**, ne parafrázovat.
2. `sudo userdel -r john` a IP adresa patří **jen do obrazu** — Kokoro je
   nečte správně.
3. Mem je **překreslený**, ne původní obrázek. Do `sources.json` nepatří,
   protože to není archivní snímek, ale vlastní kresba.
4. Kdyby se do obrazu dostal letopočet vzniku slova *hacker*, musí se
   napřed doložit — RFC 1392 dává rok 1993, ne původ.
