# Podklady k nahrání na YouTube

Časy kapitol **ověřené proti `work/timing.json`**, ne odhadnuté.
Je jich 18, první je `00:00` a každá je od předchozí aspoň 10 s —
YouTube uzná kapitoly, jen když platí všechny tři podmínky.

| co | odkud |
|---|---|
| video | `render/final-en.mp4` — 1920×1080, **9:42** (master se teprve renderuje; draft sedí na sekundu) |
| náhled | `render/thumbnail.jpg` — zatím **nevybraný** |
| titulky | `subtitles/*.srt` — **patnáct stop**: čtrnáct jazyků + `en-US` |
| americká stopa | `work-us/mix.wav` — `speed` 0,9441, přetečení 1,68 % |
| lokalizované názvy a popisy | `youtube-preklady.md` přes `tools/lokalizace.py` |

**Jediný archivní snímek je PUBLIC DOMAIN**, takže povinná atribuce
tentokrát není. Řádek s kreditem je v bloku stejně — stojí nic a je
poctivý. Zbytek videa je kreslený kódem (92 diagramů) a tři scény z SDXL.

> **Věta o americké stopě platí, jen když ji doopravdy nahraješ do
> Studia.** Z API ani z disku se to nepozná (`docs/zverejneni.md`),
> a popis, který slibuje stopu, jež tam není, je nepravdivý ve čtrnácti
> jazycích naráz. Když se stopa nenahraje, druhá věta se vypustí
> z popisu **i ze všech třinácti překladů**.

---

## Titul

```
Why Are Some Languages So Complicated?
```

> Wh-otázka schválně — na kanálu 2,23 % proti 1,63 % u tvrzení
> a 1,21 % u ano/ne otázky. Titul se ptá a odpověď neprozrazuje.

## Popis

```
Five thousand years ago there was no electricity, no books and no
schools. By our standards, an extraordinarily simple life — so you might
expect an extraordinarily simple language. Latin, Old English and Old
Norse say otherwise. All of them had grammatical machinery that modern
English has mostly lost.

You don't need an ancient language to see how strange this gets. English
says "go" and "went", and "went" never belonged to "go" at all. It was
the past tense of a different verb, "wend". At some point English quietly
took the past tense of one verb and handed it to the other. Nobody voted
on it. Nobody wrote it down as a rule. It happened, and then it stayed.

This video is about why that is ordinary rather than odd. How one
language becomes many without anyone deciding to start a new one. Why
Old English losing its case endings did not make English simpler, but
moved the work into word order and into a small army of auxiliary verbs.
Why "how complex is this language" has no single number behind it. And
why Proto-Indo-European — a language nobody has ever found a text in —
still looks elaborate when linguists reconstruct it by comparing the
languages that came out of it.

Then the part people find hardest to accept. There is no direction. The
Slavic languages make it plain: most of them kept a rich case system,
while Bulgarian lost it on its nouns almost entirely and grew something
else instead, a definite article stuck on the end of the word. Same
ancestor, opposite directions, and neither one is the upgrade.

Subtitles are written for this video, not auto-generated. An American
English audio track is available as a second audio track.

Full transcript, sources and translations: https://theresmoretoit-channel.github.io/videos/why-are-some-languages-complicated/

Chapters
00:00 A simple life, a complicated language
00:36 Why isn't it "goed"?
01:31 Language is not technology
02:25 How one language becomes many
03:18 So why don't they wear down?
03:52 The dog and the man
04:22 A small army of helper verbs
04:49 Complexity moves house
05:03 There is no dial
05:49 Back to our ancient human
06:09 A reconstruction, not a record
06:27 A society without technology
06:45 Did you see it, or were you told?
07:19 Less like engineering
08:04 There is no direction
08:15 The Slavic example
08:47 Never a ladder
09:08 Why did we expect a simple one?

IMAGE CREDITS
Beowulf, Cotton MS Vitellius A XV, f. 132r — public domain
via Wikimedia Commons
```

## Tagy

```
language, linguistics, historical linguistics, language change, grammar,
Old English, etymology, irregular verbs, went, Proto-Indo-European,
comparative method, case system, Slavic languages, Bulgarian,
evidentiality, why languages are complex
```

## Nastavení

| položka | hodnota |
|---|---|
| kategorie | Science & Technology (28) — norma kanálu; Education by tématu seděla taky |
| jazyk videa | **en-GB** — nastavit PŘED titulky, jinak zůstane dlaždice Titulky zašedlá |
| licence | Standardní licence YouTube (archivní snímek je public domain, zbytek vlastní tvorba) |
| vytvořeno pro děti | ne |
| **prohlášení o AI** | **ne** — SDXL scény jsou malované ilustrace, archivní snímek je upravený jen barevně, hudba je procedurální |

## Co musí uživatel naklikat sám

1. **Závěrečná obrazovka** — API na ni nemá ani zdroj. Místo je ověřené
   `zaver_check.py`: S83, S84 a S88 mají u dlaždice i kolečka **0,0 %
   překryvu**.
2. **Druhá audiostopa** — nahrát umí jedině Studio. Když se nenahraje,
   vypustit větu o ní z popisu i ze všech překladů.
3. **Náhled** — zatím nevybraný, viz níž.
4. **Playlist** — dopsat slug do `playlisty.json`, pak `analytics.py --videa`
   a `tools/playlisty.py`.

## Co ještě není hotové

| | |
|---|---|
| **tři SDXL scény** | S03, S35, S61 jsou zatím **placeholdery** — potřebují běžící ComfyUI na herním PC |
| **master** | `render/final-en.mp4` neexistuje; hotový je jen draft v 960×540 |
| **náhled** | nevybraný. Podle `docs/thumbnail-styl.md` rozhoduje princip, ne technika — jeden dominantní koncept, otázka místo tvrzení, čitelnost ve 150 px |

## Pořadí kroků ve Studiu

| pořadí | co | odkud |
|---|---|---|
| 1 | nahrát video jako **neveřejné** | `render/final-en.mp4` |
| 2 | **jazyk videa `en-GB`** | jinak zůstane dlaždice Titulky zašedlá |
| 3 | titul a popis | blok pod „Titul" a **celý** blok pod „Popis" |
| 4 | kategorie, licence, děti, AI | tabulka „Nastavení" |
| 5 | náhled | `render/thumbnail.jpg` |
| 6 | **patnáct titulkových stop** | `subtitles/*.srt` — `en` jako hlavní |
| 7 | druhá audiostopa | Studio → Upravit → Zvukové stopy |
| 8 | **třináct lokalizací** | `youtube-preklady.md`, sekce jsou **v pořadí Studia**, kopíruj shora dolů |
| 9 | závěrečná obrazovka | ruční vždycky |
| 10 | zveřejnit, pak playlist | |
