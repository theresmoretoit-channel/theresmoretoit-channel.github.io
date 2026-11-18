# YouTube — 126 „Why Do We Still Write Code?“

Stav: **MP4 nahrané uživatelem ve Studiu (2026-10-28).** Stav zveřejnění je v `Témata.fods`.

| | |
|---|---|
| ID videa | `6SyWacfTu3A` |
| master | ✅ `render/final-en-126.mp4` (9:59, 1920×1080, `ffprobe` 599,00 s) |
| náhled | ✅ `render/thumbnail.jpg` (koncept C, bublina v závorkách; A záloha), nahrál uživatel ve Studiu |
| nastavení, popis, tagy | podklady níž |
| lokalizace | ✅ `youtube-preklady.md`, 13 jazyků, nahráno |
| titulky | ✅ 15 stop nahráno |
| americká stopa | `render/audio-en-US.m4a`, ručně ve Studiu |
| závěrečná obrazovka | od **9:39**, S65–S66, prvky **nahoru** (viz níž) |
| **karta** | **na 044 *What Happens When Programmers Stop Programming?* v čase 0:54 (S07)** — ručně ve Studiu |
| playlist | `ai` (*AI — Where It Came From and What It's Doing to Us*), na konec |

**Co musí uživatel naklikat sám:** kartu na 044 v 0:54, závěrečnou
obrazovku, americkou audiostopu (`render/audio-en-US.m4a`) a osvědčení
o zproštění, pokud ho nevyřídil průvodce nahráním.

Stopáž 9:59 (`work/timing.json` total 599,0 s).

> Kdyby se znovu pouštěl `tts.py`, přepočítej kapitoly tady
> i v `youtube-preklady.md`, čas karty a přegeneruj `en-US` přes `us_stopa.py`.

Pořadí podle CENY (`docs/zverejneni.md`):

```bash
V=videos/126-why-do-we-still-write-code
python tools/nahraj.py $V --k-videu=6SyWacfTu3A --bez-titulku   # 100
python tools/analytics.py --videa                               #   1  ← nutné
python tools/lokalizace.py $V                                   #  50
python tools/titulky.py $V --smaz-asr                           # 150  ← před titulky
python tools/titulky.py $V                                      # 400×15
python tools/playlisty.py                                       #  50
# úklid, až je MP4 na YouTube:
rm $V/render/draft*.mp4
ssh vrana@192.168.0.207 'rm -rf /home/vrana/temp/render-126-why-do-we-still-write-code'
```

---

## 1. Titul

```
Why Do We Still Write Code?
```

> Wh-otázka, 27 znaků, shodná s `project.json`. Odpověď titul
> neprozrazuje (video končí tím, že psaní specifikace JE programování
> v novém jazyce).

---

## 2. Popis

```
Here is a complete requirement for a piece of business software: "A user can cancel an order." Six words. Any developer would nod. And yet it leaves almost every real question open. After the invoice has gone out? After the order has shipped? What about the supplier? What if two people act in the same second?

Today there is a tempting idea: write only the specifications, keep them in documents, review them, and let an AI write the code. It's a good idea. It's also not a new one. This video follows nearly seventy years of attempts to raise the level at which we tell computers what to do, and asks what is really different this time.

Along the way: the 1957 paper that called FORTRAN an "automatic coding system", CASE tools and fourth-generation languages, Model Driven Architecture, low-code, a survey of 450 people who actually used model-driven development, Edsger Dijkstra's short note on "the foolishness of natural language programming", and a bug in Amazon's DynamoDB that took thirty-five steps to trigger.

Sources: Backus et al. (1957), The FORTRAN Automatic Coding System, Proceedings of the Western Joint Computer Conference; Object Management Group, Model Driven Architecture (2001); Richardson & Rymer (2014), Forrester Research; Whittle, Hutchinson & Rouncefield (2014), The State of Practice in Model-Driven Engineering, IEEE Software; Dijkstra, EWD 667 (1978); Newcombe et al. (2014), Use of Formal Methods at Amazon Web Services; CommitStrip (2016), A very comprehensive and precise spec.

Subtitles are written for this video, not auto-generated. An American English audio track is available as a second audio track.

IMAGE CREDITS
Edsger Wybe Dijkstra — Hamilton Richards, CC BY-SA 3.0
via Wikimedia Commons
Licences: creativecommons.org/licenses/by-sa/3.0/

Full transcript, sources and translations: https://theresmoretoit-channel.github.io/videos/why-do-we-still-write-code/

CHAPTERS
00:00 Six words
00:42 Write only the sentences
01:08 An old idea
01:45 Models instead of code
02:32 Did any of it work?
03:07 The programmers' joke
03:35 Dijkstra's warning
04:04 What's different this time
05:07 The specification as source code
06:01 What a change looks like
07:26 How do you know it worked?
08:39 Look at what we've built
09:21 The programmer of the future
```

> **Blok se kopíruje CELÝ** (`docs/zverejneni.md`). Jediný archivní snímek
> je S25 (Dijkstra, CC BY-SA 3.0, `sources.json` / `CREDITS.md`), atribuce
> je uvnitř bloku. S62 je SDXL, ostatní scény kreslené kódem.
>
> **Pointa se neprozrazuje.** Popis položí otázku a vyjmenuje historii;
> neříká, co je tentokrát jinak (S29–S35: mezery se z chyb stávají
> nepozorovaná rozhodnutí), ani závěr (S57–S65). „The programmers' joke“
> v kapitolách nezní jako odpověď.
>
> **Nic netvrdí víc než video** (`factcheck.md`): FORTRAN jako *automatic
> coding system* je titul článku (S10), „450 people who actually used“
> = S19, DynamoDB „took thirty-five steps“ = nejkratší cesta (S55).
>
> Kapitoly ze scén S01, S06, S09, S13, S18, S22, S25, S28, S36, S42, S50,
> S57, S62 (`work/timing.json`, zaokrouhleno dolů). Nejkratší 28 s
> (S22 → S25), první na 00:00, všechny ≥ 10 s. Výzvy k odběru (za S12
> a S49) leží uvnitř kapitol.

---

## 3. Náhled

`render/thumbnail.jpg` — koncept C (řečová bublina ve složených závorkách,
CODE / JUST SAY IT?), obrázek z ChatGPT, původ v `thumbnail/PUVOD.md`.
Záloha pro Test & Compare: koncept A (`thumbnail/a-karticka-chatgpt.png`).
**Nenahrán:** 2026-10-28 došla kvóta API. Buď ručně ve Studiu, nebo další
den `nahraj.py --k-videu=6SyWacfTu3A --bez-titulku` (100 jednotek).

---

## 4. Titulky

`subtitles/*.srt`, 14 jazyků + `en-US`. Jazyk videa **`en-gb`** (hlas
`bf_emma`) se musí nastavit dřív, než se nahrají titulkové stopy.
Codex prošel u všech 13 překladů, nálezy zapracované (`notes.md`).

---

## 5. Nastavení

| | |
|---|---|
| kategorie | **Science & Technology** (28) — posílá `nahraj.py` napevno |
| jazyk videa | `en-gb` |
| licence | standardní |
| pro děti | **ne** |
| komentáře | zapnuté (S66 končí otázkou do komentářů) |
| **byla použita AI** | **ne**. Scény jsou kreslené kódem; jediná SDXL scéna (S62) je malovaná ilustrace podle kotvy stylu, ne fotorealismus ani skutečné místo či událost. Archivní portrét Dijkstry (S25) je upravený jen barevně. Hudba procedurální, hlas není klon. |

### Karta

Na video **044 *What Happens When Programmers Stop Programming?***
(`tkxKY1eTurY`) v čase **0:54** — S07 (od 53,9 s) *„The code becomes what
assembly is today: something that runs, and that nobody reads.“* je teze,
se kterou 044 končí (`factcheck.md`, S07). Karty API neumí, naklikává se ve
Studiu (Karty → Video). Text upoutávky např. *„Code that nobody reads“*.

Výzva k odběru (bez hlasu) běží vlevo dole za S12 (1:44–1:48) a za S49
(7:25–7:29); karta je v pravém horním rohu, nekříží se.

### Závěrečná obrazovka

Od **9:39** (posledních 20 s z 599,0), tedy S65 a S66 (od 587,3 s).
`zaver_check` u obou hlásí, že spodní rohy leží **přes titulek** (páteř
VĚTA | MEZERA | KÓD je v dolním pásu), **dlaždici i kolečko odběru dej
nahoru**. Jako dlaždici doporučuju **122 *Why Do Banks Still Run on
60-Year-Old Code?*** (`BpEbqJGJitI`) — tatáž otázka z druhé strany (proč
starý kód nikdo nepřepíše); 044 už má kartu. Druhou dlaždici nechat na
„nejlepší pro diváka“.

---

## 6. Tagy

```
why do we still write code, ai writing code, specification as source code,
spec driven development, model driven architecture, low-code, fortran history,
automatic coding, dijkstra natural language programming, formal methods, tla+,
amazon dynamodb bug, future of programming, software requirements,
explainer, there's more to it
```

---

## 7. Playlist

**`ai`** (*AI — Where It Came From and What It's Doing to Us*), na konec,
za 097. Je tam 044 (programátoři, kteří přestanou programovat), na které
video přímo navazuje. Alternativa `pocitace` (*Inside Your Computer*).
Zapsáno do `playlisty.json` při nahrání.
