# 149 — fact check scénáře (v0.3, 2026-11-07)

✅ = doloženo primárním nebo autoritativním zdrojem, ⚠ = sekundární zdroj, zjednodušení nebo úsudek (zdůvodněno).

## Zdroje

- [MS-Shell] Microsoft, *Shell Entry: Core Services* (Server 2003, archiv):
  `HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Winlogon`, `Shell`, výchozí `Explorer.exe`,
  *„Specifies the programs that provide the user interface to the operating system"*; Userinit.exe ho spouští.
  https://learn.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2003/cc738733(v=ws.10)
- [MS-CUI] Microsoft, *Custom user interface* (politika, User Configuration > Administrative Templates > System):
  *„the system starts the interface you specify instead of Explorer.exe"*. https://learn.microsoft.com/en-us/previous-versions/windows/it-pro/windows-2000-server/cc975911(v=technet.10)
- [MS-SL] Microsoft Learn, *Shell Launcher Overview* (2025-03): edice, kiosky, ATM, digital signage, v2 od 1809. https://learn.microsoft.com/en-us/windows/configuration/shell-launcher/
- [KB58341] *Windows 3.0 SYSTEM.INI [boot] Section*: `shell=`, výchozí progman.exe. https://ftp.zx.net.nz/pub/archive/ftp.microsoft.com/MISC/KB/en-us/58/341.HTM
- [KB172378] chyba při chybějícím odkazu na Explorer.exe v řádku `shell=` system.ini (Windows 95). https://jeffpar.github.io/kbarchive/kb/172/Q172378
- [WinBlog] *Announcing Windows 10 Insider Preview Build 18317*, 16. 1. 2019: Start z ShellExperienceHost.exe do vlastního StartMenuExperienceHost.exe. https://blogs.windows.com/windows-insider/2019/01/16/announcing-windows-10-insider-preview-build-18317/
- [WP-LS] Wikipedia, *LiteStep*; [WP-Alt] Wikipedia, *List of alternative shells for Windows*; [WP-PBN] Wikipedia, *Packard Bell Navigator*.
- [ManagedShell] knihovna Cairo, `EnvironmentHelper.cs`: čte `Shell` napřed z HKCU `…\WinLogon`, pak z HKLM. https://github.com/cairoshell/ManagedShell
- [KB314865] *System requirements for Windows XP*: 64 MB minimum, 128 MB doporučeno.

## Opravy proti zdroji od uživatele a proti v0.2

| co se tvrdilo | jak to je | důsledek |
|---|---|---|
| zdroj: *LiteStep was inspired by the Blackbox window manager* | [WP-LS]: inspirace AfterStep, ten NeXTSTEP. Z Blackboxu vychází Blackbox for Windows a bbLean | opraveno už ve v0.1 (S22, S25) |
| zdroj: Explorer obstarává i Start menu | ve Windows 10 hostil Start ShellExperienceHost.exe, od 2019 StartMenuExperienceHost.exe [WinBlog] | S10 Start nejmenuje, S33 |
| v0.2 S19: *cartoon house* | [WP-PBN]: dům přišel ve verzi 2 (1994) jako **předrenderované 3D místnosti**; verze 1.1 (1993) měla jen velké ikony | *a house you could walk through, room by room* |
| v0.2 S22: *the system Steve Jobs built* | NeXTSTEP vyvinula firma NeXT, kterou Jobs založil po odchodu z Apple (1985) | *from the company Steve Jobs founded* |
| v0.2 S24: témata jako Mac a *spaceship's console* | konkrétní téma LiteStepu v tomto stylu jsem nedoložil (LCARS existuje pro jiné nástroje) | znění zdroje: *futuristic*, *Unix workstation* |

## Po scénách

| scéna | tvrzení | ověření | |
|---|---|---|---|
| S01–S03 | plocha bez taskbaru, horní lišta, menu kdekoli, virtuální plochy; programy a soubory beze změny | ilustrativní popis prostředí typu LiteStep/bbLean; shell nesahá na programy ani ovladače [MS-Shell] | ⚠ |
| S04–S05 | přepíná to jedno nastavení, hodnota `Shell` v registru, skoro všude `explorer.exe` | [MS-Shell] | ✅ |
| S06 | jiný program, odhlásit a přihlásit, spustí se ten | Userinit spouští shell při přihlášení [MS-Shell]; Cairo na Windows 11 tím mechanismem běží [ManagedShell] | ✅ |
| S07 | 1990, Windows 3.0, system.ini, `shell=progman.exe` | [KB58341]; Windows 3.0 vyšel 22. 5. 1990 | ✅ |
| S08 | jiné jméno, Program Manager se nespustí | [KB58341], utilita WinShell (1990) přepisovala právě tenhle řádek | ✅ |
| S10–S11 | taskbar, ikony plochy, oznamovací oblast = explorer.exe, tentýž program jako správce souborů | proces „Průzkumník Windows" ve Správci úloh; Start a Nastavení jsou zvlášť | ✅ |
| S12 | pod shellem jádro, ovladače, služby | obecná architektura | ✅ |
| S13–S14 | ukončit Explorer: taskbar a ikony zmizí, okna běží; nové spuštění plochu vrátí | běžně známé chování, Cairo doporučuje stejný návrat (spustit explorer.exe ve Správci úloh). **Natočit ve VM, tím se to ověří i na Win 11** | ⚠ |
| S14b | Android: launcher se mění v Nastavení (*Home app*) | Nastavení > Aplikace > Výchozí aplikace > Domovská aplikace; launcher není celý shell, proto *similar idea* | ✅ |
| S15–S16 | shell / window manager / desktop environment; ve Windows výměna shellu nemění správu oken ani rámy | znění od uživatele; DWM je samostatný proces, správa oken je v systému (win32k), rámy kreslí aplikace přes systém | ✅ |
| S17–S18 | začátek 90. let, krabicová náhrada Program Manageru, Norton Desktop for Windows | NDW 1.0 18. 6. 1991 (WinWorld), nahrazoval Program Manager i File Manager, skupiny převáděl na Quick Access (COMPUTE!, Toasty Tech) | ✅ |
| S19 | výrobci to nahradili předem, Packard Bell Navigator, dům s místnostmi | [WP-PBN]: dodáván s PC Packard Bell, 1.1 v 1993, dům od verze 2 (1994), 3.5 kolem 1995 | ✅ |
| S20 | Windows 95: Explorer, řádek v system.ini `explorer.exe` | [KB172378], KB 142255 (návrat k Progman) | ✅ |
| S21 | koncem 90. let komunita, LiteStep | [WP-LS]: Francis Gastellu, closed source do dubna 1998 | ✅ |
| S22 | AfterStep (Unix), podle NeXTSTEPu, firma Jobse po odchodu z Apple | [WP-LS]; AfterStep je window manager pro X11 | ✅ |
| S23 | Start menu jen když si ho postavíš, moduly, menu na pravé tlačítko | [WP-LS]: moduly načítá téma, podle tématu Start a taskbar nahradí nebo odstraní; popup menu přes bangs. Pravé tlačítko na ploše je typická konfigurace, ne pevná vlastnost | ⚠ |
| S24 | témata sdílená, futuristická, jako unixová stanice, téměř prázdná | balíčky `.lsz`; vzhled ilustrativně, slova zdroje | ⚠ |
| S25 | Blackbox for Windows podle Blackboxu, minimalistický, jedno menu a lišta | Blackbox pro X11 (Brad Hughes); bb4win stylově, ne kódem; menu a toolbar jsou základ Blackboxu | ✅ |
| S26 | nástupce bbLean, Windows 2000 a XP | bbLean (grischka, od 2003, poslední 1.17.1 v 12/2009), větev bb4win, který skončil 2005 | ✅ |
| S27 | Emerge: launcher, tray, task list jako samostatné programy | wiki projektu: emergeLauncher, emergeTray, emergeTasks, emergeWorkspace, emergeCore; většina umí běžet samostatně | ✅ |
| S28 | vzhled XP: témata měnila barvy, rozložení zůstalo | XP visual styles (Luna a barevná schémata); úsudek | ⚠ |
| S29 | 128 MB, lehčí shell *slibuje* víc místa | [KB314865] 128 MB doporučeno; úspora nezměřena, proto *promised* (zpětná vazba k v0.1) | ⚠ |
| S30 | v Linuxu volba plochy normální | viz S46 | ✅ |
| S31 | LiteStep poslední preview 2014, alpha; Emerge a SharpEnviro skončily | [WP-LS] 0.25.0 Alpha 2. 9. 2014; [WP-Alt] Emerge a SharpEnviro *Discontinued*, Emerge 6.1.3 (2012) | ✅ |
| S32–S34 | Windows už není jeden program, Start vlastní proces, proto je náhrada těžší (*one reason*) | [WinBlog]; Nastavení je balíčková aplikace. Bez příčinné souvislosti se zánikem projektů (zpětná vazba k v0.1) | ✅ |
| S35 | Cairo, open source, Windows 11 | GitHub: Apache-2.0, *Windows 7 SP1, 8.1, 10, or 11*; [WP-Alt] *Active* | ✅ |
| S36 | horní lišta menu, vlastní taskbar, složky jako stacks | Cairo: menu bar (volitelně dole), taskbar; stacks (PR #836 přidal volbu zobrazovat disky jako stacks) | ✅ |
| S37 | vedle Exploreru i jako shell; v tom druhém režimu Win 11 zlobí | [ManagedShell] rozlišuje *configured as shell*; 0.4.317 opravila Poznámkový blok, Malování a PWA v režimu shellu, recenze hlásí Nastavení a Zabezpečení; na Win 11 neumí skrýt taskbar sám (ComputerBase, deskmodder) | ✅ |
| S38–S39 | Seelen UI: Explorer nenahrazuje, skryje taskbar, kreslí dock, lištu, widgety, dlaždicový správce oken | GitHub eythaann/Seelen-UI: dock/taskbar SeelenWeg, horní lišta, tiling z forku komorebi; že Explorer běží dál, shodně Windows Central, Neowin a dokumentace (podle uživatele) | ✅ |
| S40–S42 | Microsoft má oficiální Shell Launcher pro kiosky; automaty, pokladny, bankomaty; administrátor určí program | [MS-SL]: *kiosks, ATMs, and digital signage*, shell po přihlášení. *You've probably used something like it* a *many of them* jsou úsudek, počet Windows automatů nemám | ⚠ |
| S43 | jen Enterprise, Education, IoT Enterprise | [MS-SL]: *Enterprise / Enterprise LTSC, Education, IoT Enterprise / IoT Enterprise LTSC* | ✅ |
| S44 | starší mechanismus v registru je pořád součástí Windows, běžné nastavení z něj nikdy nebylo | [MS-Shell], [MS-CUI]; Cairo ho na Windows 11 používá [ManagedShell]. Věta záměrně netvrdí, že funguje na každé edici stejně (per-user hodnota v HKCU je zdokumentovaná jen nepřímo) | ✅ |
| S45 | *the desktop is the product* | pointa, úsudek | ⚠ |
| S46 | některé distribuce dají vybrat plochu při instalaci: KDE Plasma, GNOME, Xfce, Cinnamon | instalátor Debianu (tasksel): gnome, kde, xfce, lxde, cinnamon, mate, lxqt… | ✅ |
| S47 | víc než miliarda strojů | Microsoft: 1,4 mld. měsíčně aktivních zařízení (blog 24. 6. 2025), 1,6 mld. (Nadella, FY26 Q3, duben 2026) | ✅ |
| S48 | Start všude na stejném místě; lidé nevědí o volbě | úsudek | ⚠ |
| S49 | plochu měnili už před Windows 95 | S18–S19 (1991, 1993) | ✅ |
| S50–S51 | pod každým taskbarem je nastavení, které jmenuje program | [MS-Shell] | ✅ |
| S52 | otázka do komentářů | — | — |

## Otevřené do natáčení

- S13–S14 a S35–S39 se ověří znovu v praxi ve VM (záběry).
- Licence záběrů: Seelen UI ověřit při storyboardu.

## v0.4 — nálezy Codexu v angličtině (2026-11-07)

Codex na pracovní `script.cs.md` a `script.de.md` (`codex 0.3 cs.txt`, `codex 0.3 de.txt`), část D.
Schválil uživatel. Řádky tabulky výš platí pro v0.3; tyhle opravy je zpřesňují:

| scéna | v0.3 | v0.4 | důvod |
|---|---|---|---|
| S05 | *almost every PC in the world* | *almost every Windows PC* | PC bez Windows |
| S08 | *Change that name, … never appeared* | *If you changed that name* | rozkaz + minulý čas (oba jazyky) |
| S13 | *every open window keeps working* | *every other window* | okna složek patří procesu Explorer a zavřou se s ním (oba) |
| S22, S25 | *a Unix desktop* | *a Unix window manager* | AfterStep i Blackbox jsou správci oken; S15 pojmy rozlišuje (oba) |
| S28 | *Themes changed the colours.* | *… the colours and buttons.* | visual styles měnily i ovládací prvky |
| S32 | *it became much more than one executable* | *its desktop became …* | *it* ukazovalo na Windows (oba) |
| S37 | *that's exactly where it still breaks* | *Settings and Windows Security among them.* | konkrétně podle recenzí v řádku S37 výš; ⚠ ověřit ve VM |
| S38 | *draws its own:* | *brings its own pieces:* | dok + lišta + správce oken nejsou „taskbar“ |
| S42 | *that's all you get* | *that program is the whole desktop* | Shell Launcher sám přístup k jiným aplikacím neblokuje [MS-SL] (oba) |
| S48 | *everyone's Start menu is in the same place* | *the screen in the help article looks like yours* | Windows 11 umí Start zarovnat doleva i na střed (oba) |
| S50 | *one setting naming the program that draws it* | *still that one setting, waiting for a different name* | u Seelenu kreslí panel jiný program, než jaký nastavení jmenuje (S38–39) (oba) |
| S52 | *the way Linux does* | *the way some Linux distributions do* | soulad se S46 |

Většinové nálezy (oba jazyky) nebyly elipsy (`docs/preklady.md`), ale skutečné vady originálu.

## Obraz: S16 (2026-11-08)

| tvrzení v kresbě | ověření | závěr |
|---|---|---|
| LXQt panel jde se správcem oken Openbox, KWin i xfwm4 | LXQt volí správce oken v nastavení relace (výchozí Openbox, nabízí KWin, xfwm4 aj.) | ✅ |
| Xfce panel jde s Openboxem, KWinem i xfwm4 | xfwm4 je výchozí, nahrazuje se `openbox --replace` / `kwin --replace` a uložením relace, běžný postup | ✅ |
| GNOME Shell a Plasma v kresbě záměrně NEJSOU | GNOME Shell je plugin Mutteru, Plasma na Waylandu vyžaduje KWin: spojnice „každý s každým“ by lhala | — |

## Obraz: S18 (Norton Desktop, snímek Toasty Tech)

| co tvrdí obraz | ověření | závěr |
|---|---|---|
| DESKTOP = lišta nabídek a ikony disků | Toasty Tech: *„menu bar with many file management options, disk drive icons on the left and utility icons on the right“* | ✅ |
| LAUNCHER = Quick Access | Toasty Tech: při instalaci převezme skupiny Program Manageru do Quick Access | ✅ |
| FILE TOOLS = okno se stromem a soubory | Toasty Tech: dvojklik na disk otevře *desktop file manager* (strom vlevo, obsah vpravo) | ✅ |
| *on top of the same Windows* | Toasty Tech: tapeta Windows v tomhle snímku prosvítá, Norton Desktop plochu nezakrývá | ✅ |
| 1991 | snímek je verze 1.0 (*Copyright 1991 Symantec* v okně About na téže stránce) | ✅ |

## Obraz: S38–S39 (Seelen UI, skutečné snímky)

| co tvrdí obraz | ověření | závěr |
|---|---|---|
| Seelen skryje taskbar, přinese lištu, dok, widget | `seelen-bar.png`: taskbar Windows není, lišta nahoře, dok s přehrávačem dole | ✅ snímek |
| správce oken skládá okna do dlaždic | `seelen-tiling.png`: tři okna bez mezer a překryvu; uživatel ověřil, že změna velikosti jednoho okna přepočítá ostatní | ✅ snímek |
| pod Seelen pořád běží Explorer (S39) | lišta Seelen při zaostřené ploše: *Windows Explorer - Program Manager* — okno plochy patří procesu Exploreru a jmenuje se Program Manager (jméno shellu z Windows 3.x, S08) | ✅ snímek; výklad třídy `Progman` jen v `notes.md`, do obrazu nejde |
