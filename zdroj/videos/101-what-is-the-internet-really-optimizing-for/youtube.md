# YouTube — 101 „What Is the Internet Really Optimizing For?"

Stav: **podklady připravené, čeká na master a nahrání** (2026-10-11).

| | |
|---|---|
| ID videa | — (MP4 nahraje uživatel ve Studiu) |
| master | ⏳ renderuje se — `render/final-en-101.mp4` |
| náhled | ⏳ čeká na výběr (C1 / C2 / C3, `thumbnail/KONCEPTY.md`) |
| nastavení, popis, tagy | ⏳ `nahraj.py --k-videu --bez-titulku` |
| lokalizace | ⏳ 13 jazyků v `youtube-preklady.md`, Codex proběhl 2026-10-11 (13 nálezů přijato, 3 zamítnuty) |
| titulky | ⏳ až po Codexu na všech 14 jazycích scénáře + `en-US` |
| playlist | ⏳ návrh `spolecnost`, viz níž |
| závěrečná obrazovka, americká stopa | ⏳ uživatel ve Studiu |

**Co musí uživatel naklikat sám:** nahrát MP4 ve Studiu (průvodce vyřídí
prohlášení o AI a osvědčení o zproštění), závěrečnou obrazovku a americkou
audiostopu (`render/audio-en-US.m4a`).

Soubor k nahrání: `render/final-en-101.mp4` (stopáž 9:34, `work/timing.json`
total 574,2 s).

> Kdyby se znovu pouštěl `tts.py`, přepočítej kapitoly tady
> i v `youtube-preklady.md` a přegeneruj `en-US` přes `us_stopa.py`.

Pořadí podle CENY (`docs/zverejneni.md`):

```bash
V=videos/101-what-is-the-internet-really-optimizing-for
python tools/nahraj.py $V --k-videu=<ID> --bez-titulku    # 100
python tools/analytics.py --videa                         #   1  ← nutné
python tools/lokalizace.py $V                             #  50
python tools/titulky.py $V --smaz-asr                     # 150  ← před titulky
python tools/titulky.py $V                                # 400×15
python tools/playlisty.py                                 #  50
```

---

## 1. Titul

```
What Is the Internet Really Optimizing For?
```

> Wh-otázka, 43 znaků, schválená uživatelem. V titulu americké
> *Optimizing* (publikum ze 70 % US), ve scénáři britské *optimise*.
> Neprozrazuje odpověď (systém honí to, co umí změřit — S14 doba
> sledování, S32 Goodhart).

---

## 2. Popis

```
Imagine spending hours on a carefully researched video, then making a quick short that gets hundreds of views within a few hours, while the long one struggles to find anyone. One example proves very little. But the contrast raises a question: what exactly is the internet rewarding?

A recommendation system decides what millions of people get to see, yet it can't watch a video and tell what it's worth. So what does it go by instead, and what happens when everyone starts playing by its rules? From a change YouTube made in 2012 and a watermelon dropped off a roof to Facebook's 2018 feed change, a political party in Poland, a famous goldfish claim nobody can trace, and one unsettling answer to the Fermi paradox.

YouTube: Creator Blog (2012); Covington, Adams and Sargin, RecSys 2016; Goodrow, YouTube Official Blog (2021). Facebook and Poland: The Wall Street Journal, the Facebook Files (2021). Goldfish: Microsoft Canada, Attention Spans (2015); BBC More or Less (2017).

Subtitles are written for this video, not auto-generated. An American English audio track is available as a second audio track.

CHAPTERS
00:00 A long video and a short one
00:55 What can the system see?
01:35 What does a click prove?
02:13 Nuclear fusion or a watermelon?
02:44 One swipe away
03:42 Who pays the platforms?
04:16 Economists have a name for this
04:44 Facebook, 2018
05:26 Are people getting stupider?
06:01 What has actually changed?
06:38 Popular or valuable?
06:57 So what's the answer?
07:21 What the platforms are trying
08:10 Where is everybody?

IMAGE CREDITS
Pollice Verso, 1872 — Jean-Léon Gérôme, public domain
Family Watching TV, c. 1958 — Evert F. Baumgardner, public domain
via Wikimedia Commons
```

> **Blok se kopíruje CELÝ** (`docs/zverejneni.md`). Archivní snímky jsou
> jen dva a oba **public domain** (S42 Gérôme, S43 Baumgardner,
> `sources.json`), takže povinná atribuce není žádná a řádek `Licences:`
> odpadá; jsou vypsané ze slušnosti, protože jsou jen dva.
>
> **Pointa se neprozrazuje.** Popis ani kapitoly nejmenují dobu sledování,
> Goodhartův zákon ani „systém optimalizuje to, co umí změřit": změna
> YouTube 2012 je jen „a change", kapitola 04:16 říká, že název existuje,
> ne jaký, a 01:35 se ptá, co dokazuje klik. Goodhart je jen v tazích
> (divák je nevidí). TikTok v popisu není (S02 je hypotetické „Imagine…").
>
> Kapitoly jsou ze scén S01, S08, S12, S16, S20, S28, S32, S36, S41, S43,
> S48, S50, S53, S58 (`work/timing.json`, zaokrouhleno dolů). Nejkratší
> kapitola je 18,7 s (S48 → S50), poslední 84 s; všechny ≥ 10 s, první na
> 00:00. Výzva k odběru S11b (1:27) leží v kapitole „What can the system see?".
>
> Zdroje podle `factcheck.md`: Creator Blog 12. 3. a 9/2012 (S12–S14),
> Covington, Adams, Sargin RecSys '16 (S14b), Goodrow 15. 9. 2021
> (S08–S10, S53–S54), WSJ Facebook Files 15. 9. 2021 (S36–S39, polská
> strana je tam taky), Microsoft Canada 2015 + BBC More or Less 2017
> (S42b–S42c). Názvy článků schválně bez titulů — titul WSJ (*„…It Got
> Angrier Instead"*) by prozradil S37.

---

## 3. Náhled

⏳ **Čeká na výběr uživatele** — tři koncepty kreslené kódem
(`thumbnail/KONCEPTY.md`): C1 OPTIMIZED / FOR WHAT?, C2 THE FEED / WHY THIS
ONE?, C3 THE INTERNET / WHAT DOES IT WANT? Po výběru doplnit klíč
`thumbnail` v `project.json` a vyrobit `render/thumbnail.jpg`.

---

## 4. Titulky

`subtitles/*.srt`, 14 jazyků + `en-US`. Jazyk videa **`en-gb`** (hlas
`bf_emma`) se musí nastavit dřív, než se nahrají titulkové stopy. Titulky
a lokalizace se nahrávají **až po zapracování nálezů Codexu** na všech
překladech scénáře (cs a de hotové, zbylých jedenáct se dělá).

---

## 5. Nastavení

| | |
|---|---|
| kategorie | **Science & Technology** (28) — posílá `nahraj.py` napevno |
| jazyk videa | `en-gb` |
| licence | standardní |
| pro děti | **ne** |
| komentáře | zapnuté |
| **byla použita AI** | **ne** (návrh, rozhoduje uživatel). 67 scén kreslených kódem, 2 archivní snímky jen barevně upravené (*color adjustment* je výslovná výjimka), 3 SDXL scény (S20, S46, S62) jsou malované ilustrace podle kotvy stylu (*painterly editorial illustration*) — nefotorealistické, anonymní pokoj, město a hvězdárna, žádné konkrétní skutečné místo či událost. Hudba procedurální, hlas není klon |

### Závěrečná obrazovka

`zaver_check.py`: S65–S68 OK, prvky do horní poloviny. Závěrečná obrazovka
může být plných 20 s, **od 9:14**. Dlaždici i kolečko odběru do **horní
poloviny**, spodní rohy zabírá titulek.

---

## 6. Tagy

```
recommendation algorithm, YouTube algorithm, watch time, clickbait,
Goodhart's law, engagement, attention economy, social media, Facebook,
short videos, attention span, goldfish attention span, Fermi paradox,
internet culture, science explainer, there's more to it
```

---

## 7. Playlist

Navrženo **`spolecnost`** (*How Society Actually Runs*): video je o tom,
kdo rozhoduje, co uvidí miliony lidí, a jak pobídka platformy mění, co se
tvoří — tedy o fungování instituce, stejně jako 004 *Disinformation Then
and Now* a 057 *Why Do We Believe Before We Check?*, které tam leží.
Alternativa **`lide`** (*Why We Do What We Do*; 057 je i tam), kdyby
uživatel četl video spíš jako o tom, proč lidé koukají na to, na co
koukají. Dopiš slug do `playlisty.json`, spusť `analytics.py --videa`
a pak `tools/playlisty.py`.
