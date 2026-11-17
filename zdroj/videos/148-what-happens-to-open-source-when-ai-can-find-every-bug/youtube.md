# YouTube — 148 „What Happens to Open Source When AI Can Find Every Bug?“

Stav: **MP4 nahrané ručně 2026-11-08** (`4Q_3G0MHb_U`). Metadata, náhled, lokalizace (13 jazyků, po Codexu), všech 15 titulkových stop
a playlist přes API týž den. Závěrečnou obrazovku a americkou stopu naklikává uživatel ve Studiu. Stav zveřejnění je v `Témata.fods`.

| | |
|---|---|
| ID videa | `4Q_3G0MHb_U` — https://www.youtube.com/watch?v=4Q_3G0MHb_U |
| master | `render/final-en-148.mp4` (.207, `--keep`, 677,8 s, dekóduje beze chyby) |
| náhled | ✅ C1 `OPEN SOURCE / WHO FINDS IT FIRST?`, `render/thumbnail.jpg` (`thumbnail/PUVOD.md`) |
| nastavení, popis, tagy | podklady níž |
| lokalizace | `youtube-preklady.md`, 13 jazyků, Codex zapracován, nahráno |
| titulky | `subtitles/<kód>.srt`, 14 jazyků + `en-US`, Codex v0.6 zapracován, nahráno přes API (ASR na videu nebyl) |
| americká stopa | `render/audio-en-US.m4a`, ručně ve Studiu |
| závěrečná obrazovka | S65–S66, **horní polovina** (viz níž) |
| karty | žádné |
| playlist | `ai` (*AI — Where It Came From and What It's Doing to Us*), za 126, zařazeno |

**Co musí uživatel naklikat sám:** závěrečnou obrazovku, americkou audiostopu
(`render/audio-en-US.m4a`) a osvědčení o zproštění, pokud ho nevyřídil průvodce nahráním.

Stopáž 11:17 (`work/timing.json` total 677,799 s).

> Kdyby se znovu pouštěl `tts.py`, přepočítej kapitoly tady i v `youtube-preklady.md`
> a přegeneruj `en-US` přes `us_stopa.py`.

Pořadí podle CENY (`docs/zverejneni.md`):

```bash
V=videos/148-what-happens-to-open-source-when-ai-can-find-every-bug
python tools/nahraj.py $V --k-videu=4Q_3G0MHb_U --bez-titulku   # 100
python tools/analytics.py --videa                        #   1  ← nutné
python tools/lokalizace.py $V                            #  50
python tools/titulky.py $V --smaz-asr                    # 150  ← před titulky
python tools/titulky.py $V                               # 400 × 15
python tools/playlisty.py                                #  50
# úklid, až je MP4 na YouTube:
rm $V/render/draft*.mp4
ssh vrana@192.168.0.207 'rm -rf /home/vrana/temp/render-148-what-happens-to-open-source-when-ai-can-find-every-bug'
```

---

## 1. Titul

```
What Happens to Open Source When AI Can Find Every Bug?
```

> Wh-otázka, 55 znaků, shodná s `project.json`. Odpověď (nikdo neví, utajení je práh, rozhoduje doba
> do instalace opravy, S39 a S61–S65) titul neprozrazuje.

---

## 2. Popis

```
948. That's how many separate ways an AI found to take over a Linux computer from the inside, each one starting as an ordinary user with no special rights. Linux code is public, and for decades that was the argument for why it's safe. So if a machine can read public code and turn it into working exploits at this scale, should software keep its code secret after all?

This video goes through OpenAI's test run on the Linux kernel, Microsoft's record month of security fixes, the Heartbleed bug that sat in public code for two years, what an AI can do with a Windows patch and no source code, why the Linux kernel now treats bugs found with AI as public, and the two months between a Windows fix and WannaCry.

Sources: OpenAI, "A thousand fewer paths to root" (2026); Anthropic, "N-days" (2026); Linux kernel documentation, security-bugs.rst; Linus Torvalds, Linux 7.1-rc4 announcement (2026); Eric S. Raymond, The Cathedral and the Bazaar (1999); Phoronix; TechSpot; The Register.

Subtitles are written for this video, not auto-generated. An American English audio track is available as a second audio track.

CHAPTERS
00:00 948 ways in
00:42 Public code
01:02 Microsoft's private code
01:44 How the machine works
02:53 Sent to open one door
03:40 An important limit
04:17 Given enough eyeballs
04:36 Heartbleed
05:27 Does hiding it help?
05:43 Before and after a patch
06:40 What openness buys you
07:06 The same bugs, the same day
07:59 The bill for openness
08:58 Fixed is not installed
09:20 Under an hour
10:08 Keep everything updated
10:24 So is open source safer?

IMAGE CREDITS
Eric S Raymond portrait — jerone2, derivative work by Bilby, CC BY-SA 2.0
LinuxCon Europe Linus Torvalds 03 (cropped) — Krd (photo), Von Sprat (crop), CC BY-SA 4.0
Heartbleed logo — Leena Kurjenniska / Codenomicon, CC0
via Wikimedia Commons
Licences: creativecommons.org/licenses/by-sa/2.0, creativecommons.org/licenses/by-sa/4.0
```

> **Blok se kopíruje CELÝ** (`docs/zverejneni.md`). CC BY-SA ze `sources.json`: S26 (Raymond) a S43
> (Torvalds); S28 (logo Heartbleed) je CC0, uvedené ze slušnosti, jiné archivní snímky video nemá.
>
> **Pointa se neprozrazuje:** popis ani kapitoly neříkají, že se neví, co je bezpečnější (S61), že utajení
> je jen práh (S39), ani že rozhoduje doba mezi nalezením a instalací (S65). Kapitola *Keep everything
> updated* (S60b) je rada, ne odpověď na titul.
>
> Kapitoly ze scén S01, S06, S08, S12, S19, S23, S26, S28, S33, S35, S40, S43, S49, S54, S56, S60b, S61
> (`work/timing.json`, zaokrouhleno dolů). První na 00:00, všechny ≥ 10 s (nejkratší S33 → S35, 16 s;
> poslední S61 → konec 53 s). Výzvy k odběru (za S11 a S47) leží uvnitř kapitol.
>
> **Zdroje:** jen to, co je ve `factcheck.md` přečtené. OpenAI *GPT-6 Cyber* (oznámení modelu) a Linux
> Foundation (Glasswing) tu nejsou, jsou to vedlejší doklady k S05 a S49. Wikipedia (Heartbleed,
> WannaCry, Linus's law) se jako zdroj neuvádí.

---

## 3. Náhled

C1 z `thumbnail/ZADANI.md` (ChatGPT): skleněný zámek a lupa, `OPEN SOURCE / WHO FINDS IT FIRST?`.
`render/thumbnail.jpg`, nahraje ho `nahraj.py --k-videu`. Původ v `thumbnail/PUVOD.md`.

---

## 4. Titulky

`subtitles/<kód>.srt` pro 14 jazyků + `en-US` (Codex v0.6 zapracován). Jazyk videa **`en-gb`**
(hlas `bf_emma`) nastaví `nahraj.py` dřív, než se nahrají titulkové stopy.

---

## 5. Nastavení

| | |
|---|---|
| kategorie | **Science & Technology** (28), posílá `nahraj.py` napevno |
| jazyk videa | `en-gb` |
| licence | standardní |
| pro děti | **ne** |
| komentáře | zapnuté (S66 je otázka do komentářů) |
| **byla použita AI** | **ne**. 60 ze 65 scén je kreslených kódem, tři archivní (S26 a S43 portréty upravené jen barevně, ořezem a jmenovkou, S28 logo), S30 (otevřená kniha v prázdném sále) a S33 (zavřené dveře) jsou malované ilustrace ze SDXL, ne fotorealismus ani skutečná osoba, místo či událost. Hudba je procedurální, hlas není klon skutečné osoby. |

### Závěrečná obrazovka

Od **10:57** (posledních 20 s), tedy S65–S66. `zaver_check` hlásí v obou dolních rozích titulek.
**Dlaždici i odběr dej do HORNÍ poloviny** (S64–S66 ji mají záměrně volnou). Jako dlaždici navrhuju
**126 *Why Do We Still Write Code?*** (týž playlist, AI a programování), druhou nechat na „nejlepší pro
diváka".

---

## 6. Tagy

```
open source security, linux kernel, ai finds bugs, ai vulnerability research, openai linux exploits,
privilege escalation, root access, linus's law, given enough eyeballs, heartbleed, wannacry,
patch diffing, n-day exploits, security updates, open source vs closed source, there's more to it
```

---

## 7. Playlist

**`ai`** (*AI — Where It Came From and What It's Doing to Us*), za 126. Pinterest shortů: nástěnka
playlistu `ai` z `playlisty.json`.
