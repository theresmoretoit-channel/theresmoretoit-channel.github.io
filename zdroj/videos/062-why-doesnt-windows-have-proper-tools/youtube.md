# Podklady pro YouTube — 062

Formát a pravidla: `docs/zverejneni.md`. **Uživatel kopíruje jen text
mezi trojicí zpětných apostrofů pod každým nadpisem**, takže všechno
povinné musí být uvnitř bloků.

Video zatím nahrané není. **Master ještě nevznikl** a **pět SDXL scén
jsou zatím placeholdery** — časy kapitol se tím ale nezmění, protože
obraz na stopáž nemá vliv.

## 1. Titul

```
Why Doesn't Windows Have Proper Tools?
```

## 2. Popis

```
Microsoft has the source code to Windows. They wrote the APIs. They have had thirty years and some of the largest engineering teams in the history of software.

And the first thing a serious Windows user does on a new machine is install somebody else's file manager, somebody else's search, somebody else's archive tool. Before any actual work, they rebuild the toolbox.

The file manager is the sharpest case. A two-panel one has existed since 1993 — and for its first nine years it was not called Total Commander. It was called Windows Commander, until a letter arrived from lawyers representing the owner of that trademark. So Microsoft did not build that tool. Microsoft made it change its name.

And before you assume nobody in Redmond ever had the idea: DOS Shell, 1988. Left panel, right panel. In the box. Microsoft removed it.

One of these tools deserves a fair hearing and gets one. Everything feels instant because it reads the master file table and then follows the change journal that NTFS is already keeping. Windows Search is slower because it is doing a harder job — it reads inside your documents and it respects who is allowed to see which file. That one is not a failure. It is a different question being answered.

Then the case that settles it. Process Explorer came from a company called Sysinternals. Microsoft bought them in 2006 and got the man who wrote it; he is the chief technology officer of Microsoft's cloud business today. Microsoft hosts the download itself. And it is still not in Windows.

So the answer cannot be that Microsoft couldn't. Which means the real question was never why they failed. It is why they chose not to.

There are three explanations, and only one of them has court records.

Full transcript, sources and translations: https://theresmoretoit-channel.github.io/videos/why-doesnt-windows-have-proper-tools/

Chapters
0:00 They had every reason to build them
0:52 Start with the file manager
1:14 A program that has done all of it since 1993
2:08 Microsoft shipped one, then removed it
2:34 Finding a file, and where Windows is right
3:31 Disk space, copying, archives, screenshots
4:28 A program that watched other programs install
5:09 Not responding
5:30 Microsoft bought the company behind it
6:00 So it cannot be that they couldn't
6:12 One: Windows was sold as a platform
6:52 Two: this one has court dates
7:48 Not ancient history
8:54 Three: what the box costs
9:33 Twenty programs, twenty updaters
9:58 Why Windows had no such command
10:30 So that is the answer
10:41 Except something has changed
10:59 So why now?
11:53 The strange result

Subtitles are written for this video, not auto-generated. An American English audio track is available as a second audio track.

Music is generated procedurally for this channel.

IMAGE CREDITS
Mark Russinovich — MicrosoftPDC, CC BY 2.0
E. Barrett Prettyman Courthouse from NGA East Building — Toohool, CC BY-SA 4.0
European Commission headquarters, The Berlaymont Building, Brussels — Ank Kumar, CC BY-SA 4.0
via Wikimedia Commons
Licences: creativecommons.org/licenses/by/2.0, /by-sa/4.0
```

## 3. Náhled

`render/thumbnail.jpg` — **hotový**, dodal uživatel (ChatGPT) podle
konceptu A. Zdroj, otisk a rozbor: `thumbnail/PUVOD.md`.
Prázdný kovový kufřík na nářadí; říká **premisu** videa a neprozrazuje
**pointu**. Jas 59,4, kontrast 84,3 — obojí uvnitř pásma 60 vydaných.

## 4. Titulky

`subtitles/*.srt` — zatím jen **`en`** (194 titulků). Chybí `en-US`
a třináct překladů (`cs sv es pt-BR de fr it pl id tr uk vi fi`).
Jazyk videa je **`en-gb`** a nastavuje se **první**, jinak zůstane
dlaždice Titulky ve Studiu zašedlá.

## 5. Lokalizované názvy a popisy

`youtube-preklady.md`, nahraje `tools/lokalizace.py`.

## 6. Tagy

```
windows, microsoft, total commander, windows commander, sysinternals, process explorer, powertoys, winget, package manager, dos shell, everything search, windows search, microsoft antitrust, software history, file manager, windows tools, why windows, operating systems, how computers work
```

## 7. Nastavení

| | |
|---|---|
| kategorie | Věda a technika |
| jazyk videa | **en-gb** (nastavit jako první) |
| pro děti | ne |
| **byla použita AI** | **ne** — SDXL scény jsou díky kotvě stylu malované ilustrace, ne fotorealismus; tři archivní snímky jsou upravené jen barevně (výslovná výjimka pravidel); hudba je procedurální; hlas není klonovaný |
| licence | standardní |
| vkládání | povolené |
| playlist | **`legacy`** (k 046, 053, 033, 059); doplnit do `playlisty.json`, pak `analytics.py --videa` a `playlisty.py` |

> **Odpověď „ne" platí, DOKUD se SDXL scény vygenerují se stávající
> kotvou stylu.** Těch pět scén zatím neexistuje (herní PC bylo mimo
> dosah). Kdyby se kotva změnila na fotorealistickou, odpověď se
> překlopí — viz `CLAUDE.md`, „Označení AI obsahu na YouTube".

## 8. Co musí uživatel naklikat sám

| | ručně ve Studiu + `--k-videu` | `videos.insert` |
|---|---|---|
| prohlášení o AI | vyřídí průvodce | **ručně** |
| osvědčení o zproštění | vyřídí průvodce | **ručně** |
| **závěrečná obrazovka** | **ručně** | **ručně** |

Místo na závěrečnou obrazovku je připravené v posledních 20 s, tedy ve
scénách **S134, S135, S136, S137 a S138**: `zaver_check.py` hlásí
u všech pěti **nulový překryv v horních rozích**. **Prvky patří nahoru**,
dole je ambrový titulek diagramu — celý ocas videa je proto navržený
s volným pruhem nad páteří.

## 9. Pořadí nahrávání se řídí CENOU

```bash
python tools/nahraj.py videos/062-why-doesnt-windows-have-proper-tools --k-videu <ID> --bez-titulku   # 100
python tools/lokalizace.py videos/062-why-doesnt-windows-have-proper-tools                            #  50
python tools/titulky.py videos/062-why-doesnt-windows-have-proper-tools                               # 400×N
```

Za 150 jednotek je hotové všechno kromě titulků. Kdyby kvóta došla
uprostřed nich, chybí jen ocas a druhý den se dobere přes `--jen`.

Po zveřejnění ještě `titulky.py --smaz-asr` na **tohle jedno video**
(150 jednotek) — `--vse` je generální úklid, ne rutina.

## 10. Atribuce je POVINNÁ a je uvnitř bloku

Tři archivní snímky, **všechny tři vyžadují uvedení autora**:

| scéna | co | autor | licence |
|---|---|---|---|
| S69 | Mark Russinovich | MicrosoftPDC | CC BY 2.0 |
| S83 | E. Barrett Prettyman Courthouse | Toohool | CC BY-SA 4.0 |
| S87 | Berlaymont, sídlo Evropské komise | Ank Kumar | CC BY-SA 4.0 |

Žádný veřejně volný snímek tu není, takže věta *„All other archive
images are in the public domain."* se nepíše.

Název snímku z Berlaymontu je v `sources.json` dlouhý a končí
`( Ank Kumar, Infosys Limited )`. V popisu je **zkrácený** na
*European Commission headquarters, The Berlaymont Building, Brussels* —
`docs/zverejneni.md` to u dlouhých názvů výslovně připouští a autor
zůstává uvedený zvlášť.

**Strojová kontrola:** každý autor z `sources.json` s licencí `CC BY*`
musí být v bloku pod „## 2. Popis". Ověřeno.
