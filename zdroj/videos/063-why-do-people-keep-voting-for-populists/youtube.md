# Podklady pro YouTube — 063

Formát a pravidla: `docs/zverejneni.md`. **Uživatel kopíruje jen text
mezi trojicí zpětných apostrofů pod každým nadpisem**, takže všechno
povinné musí být uvnitř bloků.

Video zatím nahrané není.

> **U tohohle videa platí jedna věc navíc.** Popis nesmí říct divákovi,
> koho volit ani že některá z těch tří voleb byla chyba — stejně jako
> scénář. Rozbor je v `notes.md`, kapitola o neutralitě; prakticky to
> znamená, že se v popisu **žádné ze tří jmen nedostane přívlastek,
> který nedostanou i zbylá dvě**.

## 1. Titul

```
Why Do People Keep Voting for Populists?
```

Wh-otázka (2,23 % CTR proti 1,63 % u tvrzení a 1,21 % u ano/ne otázky),
pointu nevyzrazuje, slovo `Populists` pojmenuje téma ve výpisu.

## 2. Popis

```
Three politicians, three countries, and almost nothing else in common. Donald Trump won the American popular vote with 49.8 percent. The AfD came second in Germany with 20.8 percent, double its 2021 result. Robert Fico became prime minister of Slovakia for the fourth time — and his party is called Direction – Social Democracy, and it sat inside the family of European socialist parties until 2023.

They disagree with each other on almost everything. The machinery underneath them is nearly identical.

This video is about that machinery. Not about who is right.

Political scientists use the word more narrowly than we do. Populism in that sense is not a policy programme at all. It is one claim about who you are: that society splits into ordinary people and an elite that has taken the system and now runs it for itself. That is thin enough to sit inside almost any politics, which is why a left-wing and a right-wing version name a completely different elite and still build the same sentence.

And it works best when the problem is real. Housing nobody young can afford, healthcare that costs more every year, infrastructure quietly rotting. None of that has to be exaggerated. The populist does not have to invent the problem — only to explain it, and the explanation is always one word long.

Then there is a measurement, and it does not say what you would expect. In 2017 four economists took 220 European regions through the financial crisis. Where unemployment rose, votes for anti-establishment parties rose with it, and trust in national parliaments and European institutions fell. But attitudes towards immigrants hardly moved at all, and on culture they did not harden — if anything Europeans came out of the crisis slightly more open. The argument everybody was having and the thing actually moving the votes were two different objects.

In 1958, 73 percent of Americans said they trusted the government in Washington to do what is right. By September 2025 it was 17. And in sixteen months the party split in that number crossed straight over: Democrats from 35 to 9, Republicans from 11 to 26. The occupant changed. So that number was never measuring performance.

Which leads to the part almost nobody says out loud. A populist does not have to convince you that the simple solution will work — that would be hard, because solutions can be checked. Only that the current one has already failed. And that job is much easier, because quite often it is simply true.

Full transcript, sources and translations: https://theresmoretoit-channel.github.io/videos/why-do-people-keep-voting-for-populists/

Chapters
0:00 Simple answers to complicated problems
0:29 Trump. The AfD. Fico.
1:21 Not on the right. On the left.
1:51 What populism means in the research
2:49 Why a real problem works better
3:45 What actually moved the votes
5:03 You had your chance
5:30 Seventy-three percent, and seventeen
6:10 What do we have to lose?
6:30 The whole trick
6:51 Why a slogan wins
7:32 No single villain, no single fix
8:06 Why it keeps coming back
8:34 The occupant changed
9:20 Symptom, not disease
9:44 What happened before they did

Sources: Mudde, "The Populist Zeitgeist" (2004). Algan, Guriev, Papaioannou & Passari, "The European Trust Crisis and the Rise of Populism", Brookings Papers on Economic Activity (2017). Pew Research Center, "Public Trust in Government: 1958-2025".

Subtitles are written for this video, not auto-generated. An American English audio track is available as a second audio track.

Music is generated procedurally for this channel.
```

**Kredity k obrázkům se tu nevyskytují a je to v pořádku:** video nemá
ani jednu archivní scénu (`sources.json` neexistuje), takže není co
atribuovat. Všech 121 diagramů je kreslených kódem, tři atmosférické
scény jsou z SDXL.

## 3. Náhled

`render/thumbnail.jpg` — **hotový**, dodal uživatel podle konceptu
`c3-roztrzeny`. Zdroj, otisk a rozbor: `thumbnail/PUVOD.md`.
Roztržený hlasovací lístek s červeným křížkem, `POPULISTS` nahoře
a `IS IT THE VOTERS?` dole. Jas 76,4 a kontrast 90,3, tedy vysoko
v pásmu 61 vydaných náhledů; saturace 17,2 je třetí nejnižší na kanále
a je to záměr (obraz je skoro monochromatický).

**V náhledu není žádná tvář** — u politického tématu je podobizna
vyloučená.

## 4. Titulky

`subtitles/*.srt` — zatím jen `en`. Třináct překladů a `en-US` se
doplní.
Jazyk videa je **`en-gb`** a nastavuje se **první**, jinak zůstane
dlaždice Titulky ve Studiu zašedlá.

> **Výzva k odběru (S18b) má NOVÉ znění** a `docs/cta.md` k němu zatím
> nemá překlady — viz `notes.md`. Než se budou dělat titulky, musí se
> doplnit, jinak `cta_check.py` ohlásí neshodu právem.

## 5. Lokalizované názvy a popisy

`youtube-preklady.md`, nahraje `tools/lokalizace.py`.

## 6. Tagy

```
populism, why do people vote for populists, political science, Trump, AfD, Fico, Slovakia, Germany, elections, political trust, trust in government, Pew Research, anti-establishment, democracy, political systems, Cas Mudde, immigration and politics, European politics, how politics works, society
```

## 7. Nastavení

| | |
|---|---|
| kategorie | Věda a technika |
| jazyk videa | **en-gb** (nastavit jako první) |
| pro děti | ne |
| **byla použita AI** | **ne** — 121 ze 124 obrazů jsou ploché kresby kódem; tři SDXL scény jsou malované ilustrace bez lidí, ne fotorealismus; hudba je procedurální, hlas není klonovaný |
| licence | standardní |
| vkládání | povolené |
| playlist | **`spolecnost`** (k 050, 052); doplnit do `playlisty.json`, pak `analytics.py --videa` a `playlisty.py` |

## 8. Co musí uživatel naklikat sám

Při nahrání MP4 ručně ve Studiu a doplnění přes `nahraj.py --k-videu`:

| | |
|---|---|
| prohlášení o AI | ✅ vyřídí průvodce při nahrávání |
| osvědčení o zproštění | ✅ vyřídí průvodce |
| **závěrečná obrazovka** | ❌ **ručně** — API na ni nemá ani zdroj |

Scény S114–S118 mají **volnou horní polovinu obrazu** právě proto, aby
se tam dlaždice dalšího videa a kolečko odběru vešly. Dole je vždycky
ambrový titulek diagramu, takže spodní rohy volné nejsou.

## 9. Pořadí nahrávání

Podle CENY, ne podle toho, co je po ruce:

```
nahraj.py --k-videu <ID> --bez-titulku   # 50 + 50 jednotek
lokalizace.py                            # 50 jednotek za všech 13 jazyků
titulky.py                               # 400 za jazyk
```

Za 150 jednotek je hotové všechno kromě titulků; když pak kvóta dojde
uprostřed nich, chybí jen ocas, který se druhý den dobere přes `--jen`.
