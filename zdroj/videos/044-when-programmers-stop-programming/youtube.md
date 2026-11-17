# Podklady pro YouTube — 044

Nahrává se `render/final-en.mp4` (master, ne draft), `render/thumbnail.jpg`
a `subtitles/*.srt` v devíti jazycích. Lokalizované názvy a popisy jsou
v `youtube-preklady.md` a nahrává je `tools/lokalizace.py`.

## 1. Titul

```
What Happens When Programmers Stop Programming?
```

46 znaků. Limit je 100, mobil ukáže zhruba 60 — vejde se bez oříznutí.

**Wh-otázka, protože to kanál má naměřené**: na 29 videích s aspoň sto
zobrazeními, vážené impresemi, dává wh-otázka **2,23 %**, tvrzení 1,63 %
a ano/ne otázka **1,21 %** — ta nejhorší, protože si na ni divák odpoví
sám už ve výpisu.

Drží zároveň obě vyhledávaná slova, **programmers** i **programming**.
Toho si všímám schválně: u videa 042 se titul změnil na wh-otázku a cenou
bylo, že z něj vypadlo slovo *ChatGPT*.

Zvažované a zamítnuté:

| | proč ne |
|---|---|
| *Who Reads the Code Now?* | krátké a chytlavé, ale nemá ani jedno vyhledávané slovo a nedá se z něj poznat téma |
| *What Was All That Readable Code For?* | je to skutečná otázka videa, jenže z titulu není poznat, že jde o AI |
| *AI Is Taking Over Programming* | tvrzení, a navíc vyzradí pointu |

## 2. Popis

```
Imagine you are a programmer. One day you open your editor and there is nothing left in there for you to write, because the machine can do it. Congratulations: you have become a manager, just without the manager's salary.

But the interesting part is not whether you still have a job. We spent decades teaching programmers to write code that other programmers could read — and now we are building machines that write code programmers may never read. So what was all that readability for?

This video follows the promise that programming would be eliminated, from a 1954 IBM report that said FORTRAN "should virtually eliminate coding and debugging", through COBOL and a 1982 book literally called Application Development Without Programmers, to what actually happened to the job — which is stranger than it looks. In 2003 the American labour survey added a second job title next to the old one, and today there are roughly six software developers for every one computer programmer. The work did not disappear. It got renamed.

Chapters:
0:00 Nothing left to write
1:10 What was readability for?
1:19 It has always been automated
1:41 1954: "eliminate coding and debugging"
2:58 So how many were left?
3:17 The word that changed
3:58 Why this time is different
4:48 It stops being philosophy
5:11 The centre of gravity moves
6:00 The quieter cost
6:44 Coding style
7:23 The ships in science fiction
8:06 What is left for the programmer
8:35 A language written for machines
9:42 The wrong sentence
10:02 It was for us

Subtitles are written for this video, not auto-generated. An American English audio track is available as a second audio track.

Sources for the claims in this video, including the 1954 FORTRAN Preliminary Report and the US Bureau of Labor Statistics figures, are listed in the video itself as they come up.

IMAGE CREDITS
The archive photograph of the IBM 704 is by NASA and is in the public domain.

There's More To It — questions with answers that turn out to be longer than you expect.
```

> **Ten blok se kopíruje CELÝ a nesmí nic slibovat, co v něm není.**
> `docs/zverejneni.md` má naměřeno, že u čtyř videí ze šestnácti chyběla
> atribuce právě proto, že kredity visely jako poznámka **pod** blokem.
> Tady je jediný archivní snímek a je **public domain**, takže stačí
> jedna věta — vypisovat licenční pole by dělalo jen šum.

## 3. Tagy

```
programming, AI, software development, FORTRAN, COBOL, history of computing, automation, software engineering, career, code review, LLM, vibe coding, tech history, computer programmer, software developer
```

## 4. Nastavení

| | |
|---|---|
| kategorie | Science & Technology |
| jazyk videa | **English (United Kingdom)** — nastavit NAPŘED, jinak zůstane dlaždice Titulky zašedlá |
| titulky | devět souborů z `subtitles/` |
| licence | Standard YouTube |
| **prohlášení o AI** | **ne** — viz níž |
| publikum | není určeno dětem |

### Dotaz „byla použita AI": odpověď je NE

Rozhoduje **fotorealističnost, ne použití AI**
([pravidla](https://support.google.com/youtube/answer/14328491)). U tohohle
videa to drží čtyři věci:

- **74 z 82 scén je kreslených kódem** (SVG přes Inkscape), tedy diagramy.
- Jediná SDXL scéna (S34) je díky kotvě stylu **malovaná ilustrace**, ne
  fotorealismus.
- Jediný archivní snímek je upravený **jen barevně** — *„color adjustment
  or lighting filters"* je výslovná výjimka.
- Hudba je **procedurální** (sinusovky a šum v numpy), ne z generativního
  modelu.
- Kosmická loď v `art/lod.png` je **plochá linková kresba**; rozbor je
  v `art/PUVOD.md`.

> **Náhled je fotorealistický a na odpovědi to nic nemění** — dotaz se
> ptá na obsah videa, ne na miniaturu. Je to ale odchylka od dosavadní
> praxe kanálu, takže je zapsaná v `thumbnail/PUVOD.md`.

## 5. Co musí uživatel naklikat sám

Při výchozí cestě (**MP4 nahrát ručně ve Studiu**, pak
`nahraj.py --k-videu <ID>`):

| | |
|---|---|
| prohlášení o AI | ✅ vyřídí průvodce nahráním |
| osvědčení o zproštění | ✅ vyřídí průvodce |
| **závěrečná obrazovka** | ❌ **ručně** — API na ni nemá ani zdroj |

Závěrečná obrazovka má místo: do posledních 20 s spadá **šest scén**
(S71–S73) a u všech se dlaždice i kolečko odběru vejdou s překryvem
**0,0 %**. Prvky patří do **horní poloviny** — dole sedí ambrový titulek.

## 6. Po zveřejnění

1. `python tools/lokalizace.py videos/044-when-programmers-stop-programming`
2. Dopsat slug do `playlisty.json` — **`spolecnost`**, protože motorem
   videa je ekonomický tlak, ne stroj. Pak `analytics.py --videa`
   a `tools/playlisty.py`.
3. **`python tools/titulky.py videos/044-when-programmers-stop-programming --smaz-asr`**
   — adresářem, **ne `--vse`**. `--vse` čerstvě nahrané video vůbec nevidí
   (čte `analytics/videa.json`) a stojí 4 550 jednotek místo 100.
4. Doplnit číslo a odkaz do `Témata.ods`.
