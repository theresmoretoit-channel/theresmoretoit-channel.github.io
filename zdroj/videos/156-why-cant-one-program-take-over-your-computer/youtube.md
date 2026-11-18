# YouTube — 156 „Why Can't One Program Take Over Your Computer?“

Stav: **MP4 nahrál uživatel ručně 2026-11-15. Přes API 2026-11-15: nastavení + popis + tagy + náhled, lokalizace 13 jazyků (po Codexu), titulky 8 stop (en, cs, sv, es, pt-BR, de, fr, it).** Kvóta došla na `pl`; **zbývá 7 stop (pl, id, tr, uk, vi, fi, en-US) a playlist** — po 9:00 nejdřív ověřit výpisem, pak `titulky.py $V --jen pl,id,tr,uk,vi,fi,en-US`. Drafty smazané lokálně i na .207.

| | |
|---|---|
| ID videa | `qZdKjlQFpVY` — https://youtu.be/qZdKjlQFpVY |
| master | `render/final-en-156.mp4` (.207, 3× supersampling, 656,10 s, 46 MB, dekódováno bez chyby) |
| náhled | ✅ C1 čip s prstenci, `RING 0 / WHO GETS IN?`, `render/thumbnail.jpg` (`thumbnail/PUVOD.md`) |
| nastavení, popis, tagy | podklady níž |
| lokalizace | `youtube-preklady.md`, 13 jazyků |
| titulky | `subtitles/<kód>.srt`, 14 jazyků + `en-US`, Codex zapracován na 13 jazycích (cs čte uživatel) |
| americká stopa | `render/audio-en-US.m4a`, ručně ve Studiu |
| závěrečná obrazovka | S85–S86, **horní polovina** (viz níž) |
| playlist | `pocitace` |

**Co musí uživatel naklikat sám:** závěrečnou obrazovku, americkou audiostopu
(`render/audio-en-US.m4a`) a osvědčení o zproštění, pokud ho nevyřídil průvodce nahráním.

Stopáž 10:56 (`work/timing.json` total 656,061 s).

> Kdyby se znovu pouštěl `tts.py`, přepočítej kapitoly tady i v `youtube-preklady.md`,
> pusť `diagrams/gen/animace.py` a přegeneruj `en-US` přes `us_stopa.py`.

Pořadí podle CENY (`docs/zverejneni.md`):

```bash
V=videos/156-why-cant-one-program-take-over-your-computer
python tools/nahraj.py $V --k-videu=qZdKjlQFpVY --bez-titulku   # 100
python tools/analytics.py --videa                               #   1  ← nutné
python tools/lokalizace.py $V                                   #  50
python tools/titulky.py $V --smaz-asr                           # 150  ← před titulky
python tools/titulky.py $V                                      # 400×N
python tools/playlisty.py                                       #  50
# úklid, až je MP4 na YouTube:
rm $V/render/draft*.mp4
ssh vrana@192.168.0.207 'rm -rf /home/vrana/temp/render-156-why-cant-one-program-take-over-your-computer'
```

---

## 1. Titul

```
Why Can't One Program Take Over Your Computer?
```

> Wh-otázka, 46 znaků, shodná s `project.json`. *Rings* je v náhledu, ne v titulu (rozhodnuto 2026-11-14).
> Odpověď (procesor kontroluje každý přístup, system call) titul neprozrazuje.

---

## 2. Popis

```
On the 19th of July 2024, a security company called CrowdStrike sent out a routine update. Not a new program, just a small configuration file. Within hours, eight and a half million Windows computers had stopped on a blue screen. Airlines grounded flights and hospitals cancelled operations. And the mistake behind it was an ordinary one: the program expected twenty pieces of data, and the update gave it twenty-one. Your games make mistakes like that all the time, and they simply close. So why can't one program take over your computer, and why could this one?

This video goes through protection rings, the four privilege levels Intel introduced with the 80286 in 1982, why the numbering runs backwards, how the processor checks instructions and memory on every access, what a system call is and how many of them a browser makes, what happened to rings one and two, how Meltdown found a way through the wall, what the fix cost, why security software and game anti-cheat sit in ring zero anyway, and who gets to decide what goes in.

Sources: CrowdStrike, Channel File 291 Incident Root Cause Analysis (2024); Microsoft, Helping our customers through the CrowdStrike outage (2024); Microsoft Security, Windows security best practices for integrating and managing security tools (2024); Intel, 64 and IA-32 Architectures Software Developer's Manual, Volume 3; Schroeder and Saltzer, A Hardware Architecture for Implementing Protection Rings (Communications of the ACM, 1972); Google Project Zero, Reading privileged memory with a side-channel (2018); Red Hat, Speculative Execution Exploit Performance Impacts (2018); Riot Games, /dev/null: Anti-Cheat Kernel Driver (2020). System call counts are our own measurements with strace.

Subtitles are written for this video, not auto-generated. An American English audio track is available as a second audio track.

Full transcript, sources and translations: https://theresmoretoit-channel.github.io/videos/why-cant-one-program-take-over-your-computer/

CHAPTERS
00:00 Eight and a half million blue screens
01:01 When nothing stopped a program
01:36 Four rings, numbered backwards
02:29 The processor checks
03:28 Back to CrowdStrike
03:58 How does a browser save a file?
04:48 We counted the system calls
05:09 What happened to rings one and two?
06:58 Meltdown: a way through the wall
08:34 The fix and what it cost
09:12 Why was it in ring zero?
09:54 Anti-cheat in the kernel
10:26 So why can't one program take over?

IMAGE CREDITS
CrowdStrike BSOD at LGA — Smishra1, CC BY-SA 4.0
IBM PC 5150 — Ruben de Rijcke, CC BY-SA 3.0
80286 10MHz — Atsushi Nunome (Computer System Laboratory, Kyoto Institute of Technology), CC BY 4.0
Meltdown logo without text — Natascha Eibl, CC0
via Wikimedia Commons
Licences: creativecommons.org/licenses/by-sa/4.0, creativecommons.org/licenses/by-sa/3.0, creativecommons.org/licenses/by/4.0
```

> **Blok se kopíruje CELÝ** (`docs/zverejneni.md`). Kredity ze `sources.json`: S04, S10, S14 jsou CC BY
> (atribuce povinná), S56 CC0 — atribuci nevyžaduje, ale je jmenovitě. Kresba S79 (`art/`, ChatGPT)
> a zbytek jsou kreslené kódem. SDXL ve videu není.
>
> **Pointa se neprozrazuje:** popis říká, že se video ptá, kdo rozhoduje, ale ne, že rozhodují lidé
> při instalaci ovladače (S85). *Who gets to decide* je otázka, jako náhled.
>
> Kapitoly ze scén S01, S10, S15, S20, S27, S32, S40, S43, S54, S68, S73, S79, S83 (`work/timing.json`,
> zaokrouhleno dolů). První na 00:00, všechny ≥ 10 s (nejkratší S73 → S79, 42 s; S40 → S43, 21 s;
> poslední S83 → konec 30 s). Otázka do komentářů (S86) vlastní kapitolu nemá.
>
> **Zdroje:** z `factcheck-zaklad.md` a `factcheck.md` ty primární. Sekundární (TechPowerUp, Hackaday,
> Elastic, PC Gamer, GovInfoSecurity) v popisu nejsou.

---

## 3. Náhled

C1 z `thumbnail/ZADANI.md` (ChatGPT): čip s prstenci na tmavé břidlici, `RING 0` / `WHO GETS IN?`.
`render/thumbnail.jpg`, původ v `thumbnail/PUVOD.md`.

---

## 4. Titulky

`subtitles/<kód>.srt` pro 14 jazyků a `en-US`.
Jazyk videa **`en-gb`** (hlas `bf_emma`) nastaví `nahraj.py` dřív, než se nahrají titulkové stopy.

---

## 5. Nastavení

| | |
|---|---|
| kategorie | **Science & Technology** (28), posílá `nahraj.py` napevno |
| jazyk videa | `en-gb` |
| licence | standardní |
| pro děti | **ne** |
| komentáře | zapnuté (S86 je otázka do komentářů) |
| **byla použita AI** | **ne**. Video nemá jedinou SDXL scénu; 87 z 91 scén je kreslených kódem. S79 (hry) je plochá ilustrace z ChatGPT (`art/PUVOD.md`), ne fotorealismus. Čtyři archivní snímky z Commons (S04, S10, S14, S56) jsou upravené jen barevně. Hudba je procedurální, hlas není klon skutečné osoby. |

### Závěrečná obrazovka

Od **10:56 − 20 s = 10:36**, tedy S85–S86. `zaver_check` hlásí obě OK; dole je titulek,
**dlaždici i odběr dej do HORNÍ poloviny.** Jako dlaždici navrhuju **046 *Why Do Some People Hate Windows?***
(nejlepší CTR kanálu, Windows a CrowdStrike jsou téma obou), druhou nechat na „nejlepší pro diváka“.
Alternativa: 056 *Why Does Your Computer Ignore You When It's Busy?* (kernel a plánovač).

---

## 6. Tagy

```
protection rings, ring 0, kernel, user mode, kernel mode, crowdstrike, blue screen, bsod, system call, syscall,
meltdown, spectre, x86, intel 80286, multics, anti-cheat, vanguard, valorant, operating system, there's more to it
```

---

## 7. Playlist

**`pocitace`**, na konec. Vložit hned po `nahraj.py --k-videu` a `analytics.py --videa`.
