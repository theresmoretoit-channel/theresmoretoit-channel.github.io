# Fact check — 059 Why Can't Windows Delete a File That's in Use?

Proti `script.md` **0.2** (85 scén, 1 836 slabik). Ověřeno 2026-09-20.

**33 tvrzení ve čtyřech třídách:** 24× tvrdý fakt, 4× vlastní měření,
3× záměrné zjednodušení, 2× vyřazeno ze scénáře.

Zdroje jsou **primární**: dokumentace Microsoftu, manuálové stránky
tohoto stroje, a čtyři pokusy puštěné na tomhle notebooku. Sekundární
zdroj je použitý na jediném místě (rok vydání Unlockeru) a je tak
označený.

---

## A. Windows: sdílecí režim

### S12–S16 · „opening a file means filling in two things"

**Ověřeno.** `CreateFileW` má vedle `dwDesiredAccess` (co chci dělat já)
samostatný parametr `dwShareMode` (co smějí ostatní).

> „The requested sharing mode of the file or device, which can be read,
> write, both, delete, all of these, or none."

### S15/S16 · tři povolení, ne čtyřpolohový přepínač

**Ověřeno — a v draftu 0.1 to bylo ŠPATNĚ** (*„it has four positions"*).
Microsoft:

> „use a compatible combination of **one or more** of the following
> values"

| hodnota | |
|---|---|
| `FILE_SHARE_READ` | `0x00000001` |
| `FILE_SHARE_WRITE` | `0x00000002` |
| `FILE_SHARE_DELETE` | `0x00000004` |
| `0` | *„Prevents subsequent open operations on a file or device if they request delete, read, or write access."* |

Tři **nezávislé bity**, tedy osm kombinací. Scénář to teď říká jako
„můžeš určit, co smějí ostatní" + výčet tří možností + „nebo nic".

### S17/S18 · `FILE_SHARE_DELETE` a citace

**Ověřeno doslova.** Dokumentace `CreateFileW`, řádek pod
`FILE_SHARE_DELETE`:

> **„Note  Delete access allows both delete and rename operations."**

Scénář to cituje **beze změny**. S19 z toho vyvozuje jen důsledek
(*„a program that refuses delete sharing has blocked renaming as well"*),
což je táž věta obrácená — **ne zobecnění**.

### S21 · „It is called a sharing violation"

**Ověřeno.** `CreateFileW`:

> „**CreateFile** would fail and the GetLastError function would return
> **ERROR_SHARING_VIOLATION**."

---

## B. Windows: kdo drží soubor

### S06 · „Windows knows… It could name it."

**Doloženo nepřímo, ale pevně:** existují nástroje, které to hlásí
(Resource Monitor, Sysinternals Handle), takže ta informace v systému
je. Scénář **netvrdí, že to Explorer ví a schválně mlčí** — říká
„could name it".

### S01 · „It does not say which one" — ZPŘESNĚNO, ale scénář obstojí

Platí pro **chybu Exploreru při mazání**, o které scéna mluví.
Nálezené omezení, které do scénáře **nepatří, ale patří do odpovědí
v komentářích**:

| dialog | jmenuje program? |
|---|---|
| Explorer, mazání/přejmenování | ne (obecná hláška) |
| **`MsiRMFilesInUse`** (instalátor přes Restart Manager, Windows Installer 4.0+) | **ano, vypíše aplikace** |
| `FilesInUse` (starší dialog instalátoru) | ne |

> **Tohle scénář neoslabuje, nýbrž potvrzuje.** S06 říká, že Windows tu
> informaci má — a existence `MsiRMFilesInUse` je doklad, že ji Microsoft
> sám umí uživateli ukázat. Jen ne v tom dialogu, o kterém je řeč.

### S09/S10 · Resource Monitor, „Windows 7", „since 2009"

**Ověřeno, a datace je záměrně konzervativní.**

| | |
|---|---|
| Resource Monitor jako **samostatný `resmon.exe`** | **Windows 7**, vydání **22. 10. 2009** |
| ve Windows Vista | jen Resource Overview **uvnitř** Reliability and Performance Monitoru |
| záložka CPU | obsahuje výpisy Processes, Services, **Associated Handles**, Associated Modules |
| vyhledávání v Associated Handles | dokládané pro sedmičkovou verzi |

> **Vista se ve scénáři nejmenuje záměrně.** Předchůdce tam byl, ale
> prohledávatelný seznam handlů, jak ho lidé znají, je až sedmičkový.
> „Since 2009" je obhajitelné, „since Vista" by bylo na hraně.

### S08 · „Unlocker came out in 2005"

**Jediné tvrzení videa ze sekundárního zdroje.** Unlocker (Cedrick
Collomb), první vydání uváděno k **24. 4. 2005**. Autorská stránka
`emptyloop.com/unlocker` existuje, ale datum první verze na ní není.

> **Riziko je malé**, protože věta ve scénáři nestojí na roku, nýbrž na
> éře (*„on Windows XP that was the answer"*), a XP je v té době
> nesporné. Kdyby se rok ukázal jako nepřesný, věta se opraví na
> *„in the Windows XP years"* bez dopadu na smysl.

---

## C. Linux: jméno a objekt

### S30 · citace `unlink`

**Ověřeno doslova**, `man 2 unlink` na tomhle stroji:

> „If the name was the last link to a file but any processes still have
> the file open, the file will remain in existence until the last file
> descriptor referring to it is closed."

Scénář cituje druhou polovinu věty beze změny.

### S37 · citace `rename`

**Ověřeno doslova**, `man 2 rename`:

> „Any other hard links to the file (as created using link(2)) are
> unaffected. **Open file descriptors for oldpath are also unaffected.**"

### S31–S35 · POKUS s pětisetmegabajtovým logem

**Vlastní měření, zopakováno dvakrát se shodným výsledkem.**

```
zapsáno 500 MB, proces drží fd=3:   du=500 MB   df_used=1865 MB
PO unlink:                          du=  0 MB   df_used=1865 MB
ls                                  -> (prázdno)
PO close(fd):                       du=  0 MB   df_used=1365 MB
```

Uvolnilo se **přesně 500 MB** (1865 − 1365) a až po zavření deskriptoru.
`du` a `df` si mezitím odporovaly o celou velikost souboru.

### S34 · „there is a command just for finding files like this"

**Ověřeno doslova z manuálu** — `lsof` revize 4.99.7, popis `+|-L`:

> „A specification of the form ``**+L1**'' will select open files that
> have been unlinked."

A pokus to zachytil:

```
lsof +L1 .
python3  1741234  vrana  3r  REG  0,60  524288000  0  83809  .../app.log (deleted)
```

> **Zpětná vazba 0.2 si vyžádala, aby tu `lsof +L1` bylo jmenovitě.**
> Ve scénáři se nevyslovuje (bylo by to páté cizí slovo), ale **patří
> do obrazu S34** a do odpovědí v komentářích.

### S38/S38b · ETXTBSY

**Vlastní měření.** `man 2 open`:

> „ETXTBSY: path refers to an executable image which is currently being
> executed and write access was requested."

Naměřeno:

```
přepis běžícího programu NA MÍSTĚ  -> errno 26 (Text file busy)
unlink + nový soubor na totéž jméno -> prošel
starý proces po výměně              -> PID 1741255, 1743005 stále běží
```

Obě půlky scénáře tedy sedí: přepsat nejde, odpojit jméno ano, a starý
proces pak **běží z objektu bez jména** (S40).

> **Napoprvé mi kontrola běžícího procesu vyšla záporně**, protože byla
> napsaná špatně (hledala přesný řetězec argumentů). Zopakováno přes
> `ps -eo pid,comm,args` a potvrzeno. Zapisuju to, protože „pokus
> nevyšel" a „pokus je špatně napsaný" se pletou snadno.

### S61 · živá záplata jádra

**Ověřeno na tomhle stroji.** `/sys/kernel/livepatch` existuje,
jádro `7.1.8-1-default`, `CONFIG_LIVEPATCH=y`. Scénář je opatrný:
*„although live patching **can sometimes** avoid a reboot"*.

---

## D. Hlavní twist: Windows umí totéž

### S43b–S46 · POSIX delete semantics na NTFS

**Nejdůležitější ověření celého videa** — je to hlavní zvrat a je to
věta, kterou si divák v komentářích snadno ověří.

**Dva nezávislé primární zdroje Microsoftu, shodné znění:**

**1.** `FILE_DISPOSITION_INFORMATION_EX` (ntddk.h), `Flags`:

| | |
|---|---|
| `FILE_DISPOSITION_POSIX_SEMANTICS` | `0x00000002` |

> „When **FILE_DISPOSITION_POSIX_SEMANTICS** is set, the link is removed
> from the visible namespace as soon as the POSIX delete handle has been
> closed, but the file's data streams remain accessible by other existing
> handles until the last handle has been closed. That is, **applications
> that already had the file open can still use their handle to
> read/write even though the name they used to open it is gone** and the
> file's link count may have reached zero."

**2.** `[MS-FSCC]` 2.4.11.2 `FileDispositionInformationEx` (protokolová
specifikace):

> „If set and FILE_DISPOSITION_DELETE is set, indicates the file SHOULD
> be deleted using POSIX-style semantics. This means the link is removed
> from the visible namespace as soon as the POSIX delete handle is
> closed, but the file's data streams remain accessible by other existing
> handles."

Scénář (S44/S45) cituje z první varianty a **nic nezobecňuje**.

### Co se do scénáře VĚDOMĚ nedostalo

| tvrzení | proč ne |
|---|---|
| „Windows 10 verze 1607 / RS1" | Microsoft **minimální verzi u téhle struktury neuvádí**; číslo koluje jen v implementacích (Zig, Go, OpenJDK, CPython). Do obrazu smí jako `Windows 10`, do hlasu ne |
| „`DeleteFileW` dnes zkouší POSIX delete jako první" | **nedokumentované.** Kolovalo by to jako fakt a neobhájilo se |
| „funguje jen na NTFS" | doloženo jen nepřímo (hlášení, že na FAT selhává). Scénář říká **„On NTFS, Windows can…"**, což je tvrzení o NTFS, ne o ostatních |

> Scénář proto neříká verzi ani „jen NTFS", nýbrž **„On NTFS, Windows
> can ask for a POSIX style delete."** To je přesně to, co oba zdroje
> podpírají.

---

## E. Restarty

### S57/S58 · citace Microsoftu

**Ověřeno doslova**, *About Restart Manager*, první věta stránky:

> „**The primary reason software installation and updates require a
> system restart is that some of the files that are being updated are
> currently being used by a running application or service.**"

Scénář ji říká **slovo od slova**, jen rozdělenou do dvou scén kvůli
délce řádku.

### S53–S55 · Restart Manager a pořadí vypínání

**Ověřeno doslova**, tatáž stránka:

> „The Restart Manager stops applications in the following order, and
> after the applications have been updated, restarts applications that
> have been registered for restart in the reverse order.
> 1. GUI applications 2. Console applications 3. Windows services
> 4. Windows explorer"

Scénář: *„Windows applications, then console programs, then services,
and Windows Explorer last. Then it starts them up again."* — pořadí
i zpětné spuštění sedí.

> **Zjednodušení:** MS píše „GUI applications", scénář „Windows
> applications". Drobné, ale kdyby na to někdo ukázal, má pravdu.

### S60 · „You cannot swap the kernel underneath itself"

**Obecně platné a scénář to hned brzdí** (S61 live patching, S62 „the
honest version is smaller than the satisfying version").

### S63 · „made some components harder to replace… and that contributed"

**Záměrně slabá formulace.** Silná verze („Windows potřeboval restarty,
protože neuměl mazat soubory") je **nepravdivá** a scénář ji sám
odmítá v S59–S62. Tohle je přesně ta věta, kterou zpětná vazba
0.2 označila za nutnou brzdu.

---

## F. Záměrná zjednodušení

Tři místa, kde je scénář kratší než skutečnost. **Ani jedno není
nepravda**, ale kdyby na ně někdo ukázal, má kus pravdy.

### S48 · „On Windows, you get a contract. On Unix, you get a reference."

**Označeno zpětnou vazbou 0.2 a ponecháno v hlase.**

Ve skutečnosti: Linux **také má** zamykání (`flock`, `fcntl` — obojí
**advisory**, doloženo v `man 2 flock`: *„apply or remove an advisory
lock"*), a Windows **také dává** handle, tedy odkaz na objekt.

Skutečný rozdíl je v tom, **co je součástí běžného otevření a jak se
chování vůči ostatním procesům vynucuje**. To video říká v S47 hned
před tím (*„What differs is the default"*), takže S48 je zkratka,
kterou má divák z předchozích třiceti sekund pokrytou.

### S26/S27 · „The name is not the file"

Zjednodušení kvůli srozumitelnosti: scénář neříká slovo **inode** ani
nerozlišuje pevné odkazy. *„A line in a directory"* je přesné a
`man 2 rename` mluví o „hard links" v témž smyslu.

### S41 · „You can replace many things without touching the object in place"

Po zásahu ze zpětné vazby **už není absolutní** (0.1 mělo *„almost
anything… never edit in place"*). Další omezení, která scénář nejmenuje:
oprávnění, `mmap`, chování konkrétního souborového systému.

---

## G. Co se z tématu do scénáře nedostalo

| | proč |
|---|---|
| `openfiles` (vestavěné od XP/2003) | **neověřeno**, že bez `openfiles /local on` a restartu funguje na lokální soubory. Do scénáře bez doložení nesmí |
| mandatory versus advisory zamykání | čtvrtý technický pojem; `man 2 fcntl` na tomhle stroji už o mandatory locking nepíše nic (podpora se z jádra odstraňovala). Patří do komentářů |
| Sysinternals Handle | duplicitní k Resource Monitoru, a scénář má být o vestavěné cestě |

---

## Zdroje

**Primární — Microsoft**

- `CreateFileW`, parametr `dwShareMode` (`FILE_SHARE_DELETE`,
  `ERROR_SHARING_VIOLATION`) — learn.microsoft.com,
  `windows/win32/api/fileapi/nf-fileapi-createfilew`
- `_FILE_DISPOSITION_INFORMATION_EX` (ntddk.h) —
  `windows-hardware/drivers/ddi/ntddk/ns-ntddk-_file_disposition_information_ex`
- `[MS-FSCC]` FileDispositionInformationEx —
  `openspecs/windows_protocols/ms-fscc/2e860264-018a-47b3-8555-565a13b35a45`
- *About Restart Manager* — `windows/win32/rstmgr/about-restart-manager`
- *MsiRMFilesInUse Dialog* — `windows/win32/msi/msirmfilesinuse-dialog`

**Primární — tento stroj** (openSUSE, jádro 7.1.8-1-default)

- `man 2 unlink`, `man 2 rename`, `man 2 open` (ETXTBSY),
  `man 2 flock`, `man lsof` (revize 4.99.7)
- čtyři vlastní pokusy, viz oddíly C a D

**Sekundární** — rok vydání Unlockeru (2005). Jediné místo.
