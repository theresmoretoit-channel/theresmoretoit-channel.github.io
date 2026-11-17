# Podklady pro YouTube — 059

Formát a pravidla: `docs/zverejneni.md`. **Uživatel kopíruje jen text
mezi trojicí zpětných apostrofů pod každým nadpisem**, takže všechno
povinné musí být uvnitř bloků.

**Nahráno 2026-09-21** jako `8LJ5eVEqxdI`
(https://www.youtube.com/watch?v=8LJ5eVEqxdI). MP4 nahrál uživatel ručně
ve Studiu, zbytek doplnily nástroje v pořadí podle ceny:

| krok | co se stalo | jednotek |
|---|---|---|
| `nahraj.py --k-videu --bez-titulku` | titul, popis, tagy, jazyk `en-GB`, náhled | 100 |
| `analytics.py --videa` | spárování slugu s ID | ~1 |
| `lokalizace.py --id` | **14 jazyků** jedním voláním | 50 |
| `titulky.py` | **15 stop** vloženo | 6 000 |
| `playlisty.py` | `legacy` (za 053) a `bezne` (za 056) | 100 |

`titulky.py --smaz-asr` hlásí **`bez asr`** — YouTube si strojový přepis
vyrobí až při dalším zpracování, takže se musí pustit **znovu po
zveřejnění**.

Zbývá ruční krok ve Studiu: **závěrečná obrazovka**. Data API na ni nemá
ani zdroj.

## 1. Titul

```
Why Can't Windows Delete a File That's in Use?
```

## 2. Popis

```
You try to delete a file. Windows says it is open in another program. It does not say which one.

That message is the visible end of a much stranger question: what does it actually mean to open a file? Because on another computer the same file, open in exactly the same way, deletes without complaining.

First, the useful part. Windows has known which program it is since 2009, and it will tell you — Resource Monitor, CPU tab, Associated Handles, type the filename. Nothing to install. People kept downloading a separate tool anyway, and they had a reason.

Then the mechanism. On Windows, opening a file means filling in two things, and the second one is a contract with everybody else: what may they do while I have this open? Microsoft's own documentation adds one line under the delete flag — delete access covers renaming too. Which is why the error is not called "file busy". It is called a sharing violation.

On Linux the same command just works, and the reason is stranger than it sounds. I made a five hundred megabyte log file, left one process holding it open, and deleted it. The directory listing shows nothing. The tool that measures the folder says zero. The tool that measures the disk says five hundred megabytes are still gone.

And then the turn I did not expect: Windows can do exactly the same thing. On NTFS it can ask for a POSIX-style delete, and Microsoft documents the result in the same words a Unix manual would use. Both systems can do both things. What differs is the default.

That difference is part of why Windows used to ask you to restart so often — Microsoft says so in the documentation for the tool built to avoid it. But it is not the whole reason, and Linux is not free of the problem either.

Chapters
0:00 The message everybody knows
0:29 Which program?
1:02 Windows already tells you
1:30 What you fill in when you open a file
2:16 FILE_SHARE_DELETE
2:41 A sharing violation
2:53 On Linux it just works
3:16 A name is not the file
3:48 Five hundred megabytes that vanish
4:34 Renaming, and one limit
5:36 Windows can do the same thing
6:31 Please restart your computer
7:03 The Restart Manager
7:38 But that is not the whole reason
8:16 What each choice costs
9:11 So what does it mean to open a file?

Subtitles are written for this video, not auto-generated. An American English audio track is available as a second audio track.

Music is generated procedurally for this channel.
```

## 3. Náhled

`render/thumbnail.jpg` — **hotový**, dodal uživatel (ChatGPT) podle
konceptu `c1-dialog`. Zdroj, otisk a rozbor: `thumbnail/PUVOD.md`.
Jas 113,5 a kontrast 104,5, tedy nad pásmem všech 59 vydaných náhledů.

## 4. Titulky

`subtitles/*.srt` — `en`, `en-US` a třináct překladů
(`cs sv es pt-BR de fr it pl id tr uk vi fi`).
Jazyk videa je **`en-gb`** a nastavuje se **první**, jinak zůstane
dlaždice Titulky ve Studiu zašedlá.

## 5. Lokalizované názvy a popisy

`youtube-preklady.md`, nahraje `tools/lokalizace.py`.

## 6. Tagy

```
windows, linux, file system, file locking, file in use, cannot delete file, sharing violation, file handle, file descriptor, inode, unlink, POSIX, NTFS, resource monitor, restart manager, why does windows need to restart, operating systems, how computers work
```

## 7. Nastavení

| | |
|---|---|
| kategorie | Věda a technika |
| jazyk videa | **en-gb** (nastavit jako první) |
| pro děti | ne |
| **byla použita AI** | **ne** — všech 86 obrazů jsou ploché kresby kódem, žádná SDXL ani archivní scéna, hudba je procedurální, hlas není klonovaný |
| licence | standardní |
| vkládání | povolené |
| playlist | **`legacy`** (k 046, 053, 033) a **`bezne`** (k 056); doplnit do `playlisty.json`, pak `analytics.py --videa` a `playlisty.py` |

## 8. Co musí uživatel naklikat sám

Podle toho, jak se video nahraje:

| | ručně ve Studiu + `--k-videu` | `videos.insert` |
|---|---|---|
| prohlášení o AI | vyřídí průvodce | **ručně** |
| osvědčení o zproštění | vyřídí průvodce | **ručně** |
| **závěrečná obrazovka** | **ručně** | **ručně** |

Místo na závěrečnou obrazovku je připravené ve scénách **S73, S74, S75
a S75b** (posledních 20 s): `zaver_check.py` hlásí u všech čtyř
**nulový překryv v horních rozích**. **Prvky patří nahoru**, dole je
ambrový titulek diagramu.

## 9. Pořadí nahrávání se řídí CENOU

```bash
python tools/nahraj.py videos/059-why-cant-windows-delete-a-file-in-use --k-videu <ID> --bez-titulku   # 100
python tools/lokalizace.py videos/059-why-cant-windows-delete-a-file-in-use                            #  50
python tools/titulky.py videos/059-why-cant-windows-delete-a-file-in-use                               # 400×N
```

Za 150 jednotek je hotové všechno kromě titulků. Kdyby kvóta došla
uprostřed nich, chybí jen ocas a druhý den se dobere přes `--jen`.

Po zveřejnění ještě `titulky.py --smaz-asr` na **tohle jedno video**
(150 jednotek) — `--vse` je generální úklid, ne rutina.

## 10. Bez atribucí, a je to v pořádku

Video nemá **jedinou archivní scénu** — 86 diagramů, nula SDXL, nula
archivu — takže `sources.json` ani `CREDITS.md` neexistují a v popisu
není co atribuovat. Hudba je procedurální (`tools/music.py`), tedy bez
licenčních vazeb.

> **Nula SDXL i nula archivu je rozhodnutí, ne opomenutí.** Dialogy se
> musely kreslit (snímek Windows je chráněný), mechanismus difuzní model
> nesvede a terminál s konkrétními čísly nikdo nevyfotí. Rozbor je
> v `notes.md`.
