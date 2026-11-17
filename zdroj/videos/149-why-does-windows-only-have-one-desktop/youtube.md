# YouTube — 149 „Why Does Windows Only Have One Desktop?“

Stav: **MP4 nahrané ručně 2026-11-08** (`Na_Aarf8bbc`). Metadata, náhled, lokalizace (13 jazyků, po Codexu), titulky `en` a `en-US`
a playlist přes API týž den (~1 000 jednotek). Zbylých 13 jazyků titulků, americkou stopu a závěrečnou obrazovku naklikává
uživatel ve Studiu. Stav zveřejnění je v `Témata.fods`.

| | |
|---|---|
| ID videa | `Na_Aarf8bbc` — https://www.youtube.com/watch?v=Na_Aarf8bbc |
| master | `render/final-en-149.mp4` (herní PC přes wifi, 549,6 s, dekódováno bez chyby) |
| náhled | ✅ C1 `WINDOWS / IS THIS STILL WINDOWS?`, `render/thumbnail.jpg`, nahráno (`thumbnail/PUVOD.md`) |
| nastavení, popis, tagy | podklady níž |
| lokalizace | `youtube-preklady.md`, 13 jazyků, Codex zapracován (`codex lokalizace.txt`), nahráno |
| titulky | přes API 2026-11-08: `en`, `en-US`, `cs`, `sv`, `es`, `pt-BR` (podle logu, ověřit výpisem); **zbývá `de fr it pl id tr uk vi fi`**, kvóta došla |
| americká stopa | `render/audio-en-US.m4a`, ručně ve Studiu |
| závěrečná obrazovka | S51–S52, **horní polovina** (viz níž) |
| karty | žádné |
| playlist | `legacy` (*Legacy Tech*), za 129, zařazeno (pozice 26) |

**Co musí uživatel naklikat sám:** závěrečnou obrazovku, americkou audiostopu
(`render/audio-en-US.m4a`), titulky, které nejdou přes API, a osvědčení o zproštění, pokud ho nevyřídil průvodce nahráním.

Stopáž 9:10 (`work/timing.json` total 549,578 s).

> Kdyby se znovu pouštěl `tts.py`, přepočítej kapitoly tady i v `youtube-preklady.md`
> a přegeneruj `en-US` přes `us_stopa.py`.

Pořadí podle CENY (`docs/zverejneni.md`):

```bash
V=videos/149-why-does-windows-only-have-one-desktop
python tools/nahraj.py $V --k-videu=Na_Aarf8bbc --bez-titulku   # 100
python tools/analytics.py --videa                        #   1  ← nutné
python tools/lokalizace.py $V                            #  50
python tools/titulky.py $V --smaz-asr                    # 150  ← před titulky
python tools/titulky.py $V --jen en,en-US                # 800  (2026-11-08)
python tools/titulky.py $V --jen de,fr,it,pl,id,tr,uk,vi,fi   # 3 600, zbytek
python tools/playlisty.py                                #  50
# úklid, až je MP4 na YouTube:
rm $V/render/draft*.mp4
ssh vrana@192.168.0.207 'rm -rf /home/vrana/temp/render-149-why-does-windows-only-have-one-desktop'
```

---

## 1. Titul

```
Why Does Windows Only Have One Desktop?
```

> Wh-otázka, 39 znaků, shodná s `project.json`. Odpověď (*the desktop is the product*, S45) titul neprozrazuje.

---

## 2. Popis

```
Picture switching on a Windows PC and finding no taskbar, no Start button and not a single icon on the desktop. Your programs, drivers and files are exactly where you left them. Only the desktop has changed, and the switch that changes it is a single setting. So why does Windows only have one desktop?

This video goes through the setting that decides what your desktop is, the two jobs Explorer does, the replacement desktops people bought in the early nineties, LiteStep and the community that grew up around it, Blackbox, bbLean and Emerge Desktop, Cairo Desktop and Seelen UI on Windows 11 today, and an official Microsoft feature you may have used on a ticket machine without knowing.

This isn't a how-to: changing the Shell value without a working replacement can leave you with no desktop at all.

Sources: Microsoft Learn, Shell Launcher overview; Microsoft, Shell entry (Winlogon) and Custom user interface policy; Microsoft KB Q58341, Windows 3.0 SYSTEM.INI [boot] section; Windows Insider Blog, Build 18317 (2019); Cairo Desktop, ManagedShell source code; Wikipedia: LiteStep, Packard Bell Navigator, List of alternative shells for Windows.

Subtitles are written for this video, not auto-generated. An American English audio track is available as a second audio track.

CHAPTERS
00:00 A desktop with no taskbar
00:25 One setting
00:50 Windows 3.0, 1990
01:11 The real question
01:22 Explorer's two jobs
02:12 On Android, it's a setting
02:26 Shell, window manager, desktop
02:57 Norton Desktop and Packard Bell
03:40 LiteStep
04:18 Blackbox, bbLean and Emerge
04:44 Why go to all that trouble?
05:12 Where did they go?
06:02 Cairo Desktop
06:28 Seelen UI
06:52 What about Microsoft?
07:40 So why only one?
07:52 A choice on Linux
08:28 Before Windows 95

IMAGE CREDITS
Norton Desktop for Windows screenshot — Nathan Lineback, Toasty Tech GUI Gallery (toastytech.com/guis)
NonStep II desktop example — Meadowsd at English Wikipedia, GPL, via Wikimedia Commons
Licence: gnu.org/licenses/gpl.html
```

> **Blok se kopíruje CELÝ** (`docs/zverejneni.md`). Kredity: S18 Norton Desktop (Toasty Tech, povinný podle
> `art/PUVOD.md` a `notes.md`) a S23 ze `sources.json` (GPL, Commons). Ostatní snímky v `art/` (Cairo, Seelen,
> bbLean, Emerge) pořídil uživatel, kredit nepotřebují.
>
> **Pointa se neprozrazuje:** popis ani kapitoly neříkají *the desktop is the product* (S45) ani to, že Shell
> Launcher je pro kiosky jen v edicích Enterprise. Kapitola 07:40 je jen *So why only one?*
>
> **Věta „This isn't a how-to“** je navíc proti obvyklému popisu: video ukazuje, kde hodnota leží, a divák, který
> ji přepíše bez náhrady, zůstane bez plochy. Návrh, škrtni, když nechceš.
>
> Kapitoly ze scén S01, S04, S07, S09, S10, S14b, S15, S17, S21, S25, S28, S31, S35, S38, S40, S45, S46, S49
> (`work/timing.json`, zaokrouhleno dolů). První na 00:00, všechny ≥ 10 s (nejkratší S09 → S10, 10,9 s;
> poslední S49 → konec 41 s). Otázka do komentářů (S52) vlastní kapitolu nemá. Výzvy k odběru (za S14 a S45)
> leží uvnitř kapitol.
>
> **Zdroje:** primární a autoritativní z `factcheck.md` ([MS-SL], [MS-Shell], [MS-CUI], [KB58341], [WinBlog],
> [ManagedShell], [WP-*]). KB172378 a KB314865 jsou podrobnosti (Windows 95, paměť XP), v popisu nejsou.

---

## 3. Náhled

C1 z `thumbnail/ZADANI.md` (ChatGPT): notebook s cizí plochou, `WINDOWS / IS THIS STILL WINDOWS?`.
`render/thumbnail.jpg`, původ v `thumbnail/PUVOD.md`.

---

## 4. Titulky

`subtitles/<kód>.srt` pro 14 jazyků a `en-US` (Codex v0.5 zapracován, `codex 0.5 <kód>.txt`).
Jazyk videa **`en-gb`** (hlas `bf_emma`) nastaví `nahraj.py` dřív, než se nahrají titulkové stopy.

---

## 5. Nastavení

| | |
|---|---|
| kategorie | **Science & Technology** (28), posílá `nahraj.py` napevno |
| jazyk videa | `en-gb` |
| licence | standardní |
| pro děti | **ne** |
| komentáře | zapnuté (S52 je otázka do komentářů) |
| **byla použita AI** | **ne**. 52 ze 53 scén je kreslených kódem a SDXL video nemá vůbec. Snímky obrazovky (Norton Desktop, bbLean, Emerge, Cairo, Seelen) jsou skutečné záběry skutečného softwaru, upravené jen ořezem a retuší nápisu *Activate Windows* (`art/PUVOD.md`); S23 je archivní snímek z Commons. Hudba je procedurální, hlas není klon skutečné osoby. |

### Závěrečná obrazovka

Od **9:10 − 20 s = 8:50**, tedy S51–S52. `zaver_check` hlásí v obou dolních rozích titulek.
**Dlaždici i odběr dej do HORNÍ poloviny.** Jako dlaždici navrhuju **076 *How Did Windows Win Without
Inventing the GUI?*** (navazuje: Program Manager, Windows 3.x, Microsoft a jeho plocha), druhou nechat na
„nejlepší pro diváka“.

---

## 6. Tagy

```
windows shell, replace windows desktop, explorer.exe, alternative shell for windows, windows desktop replacement,
litestep, bblean, blackbox for windows, emerge desktop, cairo desktop, seelen ui, shell launcher,
windows kiosk mode, program manager, windows 3.0, norton desktop, packard bell navigator, windows history,
linux desktop environment, there's more to it
```

---

## 7. Playlist

**`legacy`** (*Legacy Tech — The Old Systems Still Running Everything*), s ostatními videi o Windows, za 129.
Zapsáno v `playlisty.json`, zařazeno `playlisty.py --jen legacy` 2026-11-08.
Pinterest shortů: `Legacy Tech`.
