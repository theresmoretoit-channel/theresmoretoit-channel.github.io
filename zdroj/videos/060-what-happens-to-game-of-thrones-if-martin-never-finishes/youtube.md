# Podklady pro YouTube — 060

Formát a pravidla: `docs/zverejneni.md`. **Uživatel kopíruje jen text
mezi trojicí zpětných apostrofů pod každým nadpisem**, takže všechno
povinné — včetně atribucí — musí být uvnitř bloků.

**Nahráno 2026-09-21** jako `RxgRbWfy6cI`
(https://www.youtube.com/watch?v=RxgRbWfy6cI). MP4 nahrál uživatel ručně
ve Studiu, zbytek doplnily nástroje v pořadí podle ceny:

| krok | co se stalo | jednotek |
|---|---|---|
| `nahraj.py --k-videu --bez-titulku` | titul, popis, tagy, jazyk `en-GB`, náhled | 100 |
| `analytics.py --videa` | spárování slugu s ID | ~1 |
| `lokalizace.py --id` | **14 jazyků** jedním voláním | 50 |
| `titulky.py` | **7 stop z 15**, pak došla kvóta | 2 800 |

### Zbývá dobrat, až se kvóta resetuje (9:00 našeho času)

```bash
python tools/titulky.py videos/060-what-happens-to-game-of-thrones-if-martin-never-finishes \
       --jen it,pl,id,tr,uk,vi,fi,en-US            # 3 200 jednotek
python tools/titulky.py videos/060-what-happens-to-game-of-thrones-if-martin-never-finishes \
       --smaz-asr                                   # 150, až PO zveřejnění
python tools/playlisty.py                           # 50, do `spolecnost`
```

**Na videu je 7 stop, ověřeno `captions.list`, ne z logu:** `en-GB`,
`cs`, `sv`, `es`, `pt-BR`, `de`, `fr`. Spadlo `it` — log končí posledním
ÚSPĚŠNÝM jazykem, takže se z něj počet stop číst nedá.

Zbývá ruční krok ve Studiu: **závěrečná obrazovka** a **nahrání americké
audiostopy** (`render/audio-en-US.m4a`) — na obojí Data API nemá zdroj.

> **Párování slugu selhalo napoprvé, a nebyla to příčina z dokumentace.**
> `docs/zverejneni.md` říká „napřed `nahraj.py --k-videu`, teprve pak
> `analytics.py --videa`" — což jsem dodržel. Jenže `analytics.py` páruje
> podle **`title` v `project.json`**, a ten tu zněl „…Never Finishes
> **It**?", kdežto `youtube.md` a YouTube „…Never Finishes?". Záložní
> cesta přes odkaz v `Témata.ods` u čerstvého videa ještě neexistuje,
> takže selhaly obě. Opraveno srovnáním `project.json` s `youtube.md`.
>
> **Napříč kanálem se ty dva tituly rozcházejí u osmi videí** (004, 027,
> 029, 034, 036, 043, 044, 054). Těm to nevadí, protože jsou zveřejněná
> a párují se přes `Témata.ods` — ale u každého nového videa to znamená
> jedno selhání navíc. **Před `analytics.py --videa` srovnej
> `project.json.title` s blokem „1. Titul".**

## 1. Titul

```
What Happens to Game of Thrones If Martin Never Finishes?
```

Wh-otázka, jak žádá `CLAUDE.md`: napříč 29 videi s aspoň sto zobrazeními
mají wh-otázky vážené CTR **2,23 %** proti 1,63 % u tvrzení a 1,21 %
u ano/ne otázek.

## 2. Popis

```
In August 2017, at a steam fair in Dorset, a six-and-a-half tonne steamroller drove over a computer hard drive. Then they put what was left of it through a steam-powered stone crusher.

The drive belonged to Terry Pratchett. It held up to ten unfinished novels, and nobody will ever read them.

That wasn't vandalism — it was exactly what Pratchett wanted, and he had left instructions to do it. But look at who actually did it. Pratchett was already dead. Somebody else started the engine.

George R. R. Martin has been writing The Winds of Winter for fifteen years, on a DOS machine running WordStar 4.0. He has said that if he dies first, the book simply won't be finished. That sounds like an instruction. But an instruction needs somebody to carry it out, and that somebody won't be him.

So the first question isn't who finishes the book. It's who decides what happens to the files.

Franz Kafka left instructions with his friend Max Brod: burn everything, unread. Brod didn't, which is why we have The Trial and The Castle. Christopher Tolkien answered the same question a third way, spending decades editing his father's unfinished papers into twelve volumes of drafts rather than one finished novel. Nabokov's son published his father's last manuscript as photographs of the index cards.

And in 1873 a printer in Vermont finished The Mystery of Edwin Drood, saying Dickens had asked him to — at a seance. Decades later Arthur Conan Doyle went through it hunting for the fake, checking the spelling and the Americanisms. He found almost none.

Meanwhile, since 1992 Martin's papers have been going to an archive in Texas that now runs to over two hundred boxes. The closed part has a rule written down: to see it, you have to present a letter of permission. A letter from Martin.

There's one more detail that makes all of this worse. In 2013 Martin sat down with the television producers and told them how it ends — not the whole thing, just a handful of destinations the story has to arrive at. Which means a reconstruction could hit every single one of them and still be a completely different book.

Chapters
0:00 A steamroller and ten unfinished novels
0:39 Fifteen years of The Winds of Winter
0:58 The DOS machine, and what else is on it
1:43 Kafka told Brod to burn everything
2:23 Two hundred boxes in Texas
3:21 Publish the mess: Tolkien and Nabokov
4:31 Finish it: Dickens and the Vermont printer
5:51 A thousand endings, and pressure to pick one
6:46 The producers already know part of it
7:31 What only a living author can do
8:14 The quietest answer of all

Subtitles are written for this video, not auto-generated. An American English audio track is available as a second audio track.

Music is generated procedurally for this channel.

IMAGE CREDITS
View of a steam roller traction engine in the St Albans Steam and Country Show — Robert Lamb, CC BY-SA 2.0
Endlospapier fan-fold paper — Kungfuman, CC BY-SA 3.0
via Wikimedia Commons
Licences: creativecommons.org/licenses/by-sa/2.0, /by-sa/3.0

All other archive images are in the public domain.
```

**Kapitoly jsou z `work/timing.json`**, ne od oka. První začíná na
`0:00`, je jich jedenáct a nejkratší trvá **19 s** — YouTube žádá aspoň
tři a každou ≥ 10 s.

## 3. Náhled

`render/thumbnail.jpg`, 1280×720, **0,16 MB** (limit 2 MB).

Stoh strojopisu, kterému text dojde uprostřed věty, a za posledním
řádkem ambrový kurzor. Nahoře `THRONES`, dole `WHO ENDS IT?`.
Původ, otisky a rozbor v **`thumbnail/PUVOD.md`**; zamítnuté kreslené
koncepty vyrábí `thumbnail/gen.py`.

Kontrast **98,8** je druhý nejvyšší z 62 vydaných náhledů, ztráta detailu
při 150 px třetí nejnižší.

## 4. Titulky

**Patnáct stop**: `en` (en-GB) a `en-US`, k tomu třináct překladů —
`cs, sv, es, pt-BR, de, fr, it, pl, id, tr, uk, vi, fi`.

Všechny prošly strukturální kontrolou: **nula řádků přes 42 znaků**
a nula třířádkových titulků ve všech čtrnácti jazycích.

## 5. Lokalizované názvy a popisy

`youtube-preklady.md`, nahraje `tools/lokalizace.py` **jedním voláním
za 50 jednotek** (ne 50 za jazyk).

## 6. Tagy

```
game of thrones, george rr martin, the winds of winter, a song of ice and fire, terry pratchett, franz kafka, max brod, unfinished novels, literary estate, posthumous publication, the mystery of edwin drood, charles dickens, christopher tolkien, vladimir nabokov, wordstar, manuscripts, archives, copyright, who owns a book, writing
```

## 7. Nastavení

| | |
|---|---|
| kategorie | Věda a technika |
| jazyk videa | **en-gb** (nastavit jako první, jinak zůstane dlaždice Titulky zašedlá) |
| pro děti | ne |
| **byla použita AI** | **ne** — z 86 scén je **81 kreslených kódem**, 4 archivní upravené jen barevně („color adjustment or lighting filters" je výslovná výjimka) a **jediná** SDXL scéna (S12), a ta je malovaná ilustrace, ne fotorealismus. Hudba je procedurální (`tools/music.py`), hlas není klonovaný |
| licence | standardní |
| vkládání | povolené |
| playlist | **`spolecnost`** — „Who decides, who pays and who enforces it" sedí na tohle video doslova. (Alternativa `lide` je slabší: video není o fanoušcích, nýbrž o rozhodovacím právu.) Dopsat do `playlisty.json`, pak `analytics.py --videa` a `playlisty.py` |

> **Náhled sám fotorealistický JE** a vygenerovaný modelem — otázka
> YouTube ale míří na obsah videa, ne na miniaturu. Zapsáno
> v `thumbnail/PUVOD.md`.

## 8. Co musí uživatel naklikat sám

| | ručně ve Studiu + `--k-videu` | `videos.insert` |
|---|---|---|
| prohlášení o AI | vyřídí průvodce | **ručně** |
| osvědčení o zproštění | vyřídí průvodce | **ručně** |
| **závěrečná obrazovka** | **ručně** | **ručně** |

Místo na závěrečnou obrazovku je připravené ve scénách **S82, S83, S84
a S85** (posledních 20 s): `zaver_check.py` hlásí u všech čtyř
**nulový překryv** pro dlaždici i kolečko odběru. **Prvky patří nahoru**,
dole je ambrový titulek diagramu.

## 9. Pořadí nahrávání se řídí CENOU

```bash
python tools/nahraj.py videos/060-what-happens-to-game-of-thrones-if-martin-never-finishes --k-videu <ID> --bez-titulku   # 100
python tools/lokalizace.py videos/060-what-happens-to-game-of-thrones-if-martin-never-finishes                            #  50
python tools/titulky.py videos/060-what-happens-to-game-of-thrones-if-martin-never-finishes                               # 400×15
```

Za **150 jednotek** je hotové všechno kromě titulků. Kdyby kvóta došla
uprostřed nich, chybí jen ocas a druhý den se dobere přes `--jen`.

Po zveřejnění ještě `titulky.py <adresář> --smaz-asr` na **tohle jedno
video** (150 jednotek) — `--vse` stojí přes 4 500 a je to generální úklid,
ne rutina. A `--vse` čerstvě nahrané video stejně nevidí, protože čte
`analytics/videa.json`.

## 10. Atribuce — dvě povinné, dvě ne

| scéna | snímek | licence | v popisu |
|---|---|---|---|
| S03 | steam roller traction engine | **CC BY-SA 2.0** (Robert Lamb) | **ano, povinně** |
| S23 | Endlospapier fan-fold paper | **CC BY-SA 3.0** (Kungfuman) | **ano, povinně** |
| S16 | Franz Kafka, 1923 | public domain | ne, kryje souhrnná věta |
| S42 | Dickens Gurney head | public domain | ne, kryje souhrnná věta |

Obě povinné jsou **uvnitř bloku „Popis"**, ne pod ním. U čtyř videí
ze šestnácti atribuce chyběla právě proto, že kredity visely jako
poznámka pod blokem — uživatel kopíruje jen ten blok.

Vypisovat oba public-domain snímky po jménu nemá smysl; `All other
archive images are in the public domain.` je pokrývá a nedělá šum.
