# YouTube — 064 „Who Decides What's Men's and What's Women's?"

Stav: **ZVEŘEJNĚNO 2026-09-25** (MP4 nahráno ručně 24. 9., zbytek přes API).

| | |
|---|---|
| ID videa | **`8QnwOGEj2io`** |
| odkaz | https://youtu.be/8QnwOGEj2io |
| nastavení, popis, tagy, náhled | ✅ `nahraj.py --k-videu --bez-titulku` |
| lokalizace | ✅ 14 jazyků jedním voláním |
| titulky | ✅ **15 stop**: en-GB, en-US, cs, sv, es, pt-BR, de, fr, it, pl, id, tr, uk, vi, fi |
| automatický přepis | ✅ smazán (vrátí se — viz níž) |
| playlisty | ✅ `spolecnost`, `bezne` |
| závěrečná obrazovka, viditelnost | ✅ nastavil uživatel |
| spotřeba kvóty | ~6 400 z 10 000 |

Pořadí, které se OPRAVDU použilo — a liší se od toho, co tu stálo předtím:

```bash
python tools/nahraj.py $V --k-videu 8QnwOGEj2io --bez-titulku   # 100
python tools/analytics.py --videa                               #   1  ← nutné!
python tools/lokalizace.py $V                                   #  50
python tools/titulky.py $V --smaz-asr                           # 150  ← před titulky!
python tools/titulky.py $V                                      # 6 000
python tools/playlisty.py                                       # 100
```

> **Dvě věci, na kterých se to zastavilo:** `lokalizace.py` ani `titulky.py`
> nenajdou čerstvě nahrané video, dokud neproběhne `analytics.py --videa`;
> a automatický přepis musí zmizet DŘÍV, než se nahraje naše `en` stopa,
> jinak `captions.insert` spadne na existující jazyk. Zapsáno do
> `docs/zverejneni.md`.

> **Automatický přepis se vrátí.** Smazání ho odstraní, nezakáže — YouTube
> si ho po dalším zpracování vyrobí znovu. Za pár dní sebrat:
> `python tools/titulky.py videos/064-… --smaz-asr` (150 jednotek).
> `--vse` na to nepouštěj, u 65 videí stojí jen zjištění stavu 3 250.

**Co musí uživatel naklikat sám:** závěrečnou obrazovku (API na ni nemá
ani zdroj). Prohlášení o AI a osvědčení o zproštění vyřídil průvodce při
ručním nahrání MP4.

Pořadí podle CENY, ne podle toho, co je po ruce:

```bash
python tools/nahraj.py videos/064-who-decides-whats-mens-and-womens --k-videu <ID> --bez-titulku
python tools/lokalizace.py videos/064-who-decides-whats-mens-and-womens
python tools/titulky.py videos/064-who-decides-whats-mens-and-womens
python tools/titulky.py videos/064-who-decides-whats-mens-and-womens --smaz-asr
```

---

## 1. Titul

```
Who Decides What's Men's and What's Women's?
```

Wh-otázka podle měření z `docs/kanal-metriky.md` (2,23 % proti 1,63 %
u tvrzení a 1,21 % u ano/ne otázek).

---

## 2. Popis

```
There is no committee. No register. No standard. No inspector. And yet
almost everybody knows exactly which half of the shop they belong in.

So where do the rules come from? Not from anyone in particular — from a
loop that runs between manufacturers, retailers, advertisers and us, and
that keeps going because everyone keeps taking part in it.

Along the way: a trade magazine that told shops pink was the stronger,
more decided colour and therefore better for boys; a Roman law that
banned trousers inside the city; and a Paris ordinance that made a woman
ask the police for permission to wear them. Same garment, fourteen
centuries apart, two laws pointing opposite ways.

Because a convention is not a law, not physics, not biology and not a
moral rule. It only works as long as people believe that it matters.

Subtitles are written for this video, not auto-generated. An American
English audio track is available as a second audio track.

Full transcript, sources and translations: https://theresmoretoit-channel.github.io/videos/who-decides-whats-mens-and-womens/

CHAPTERS
00:00 An invisible line in every clothing shop
01:01 The honest part: some of the difference is practical
01:45 The loop: who keeps it alive
03:31 Why the companies are not the villain
04:19 The same object, two different promises
05:07 How we learned the map
06:08 Familiarity is not nature
07:19 When high heels were a man's shoe
07:43 Rome: a tunic to the knee, and no trousers
08:22 Paris, 1800: permission to wear trousers
09:25 The boundaries move
09:51 Invented does not mean harmless
10:42 The loop can also turn the other way
11:33 A better question than men's or women's
12:44 So who decides?
13:31 The one weakness every convention has
14:04 Who was holding the pencil

IMAGE CREDITS
Toga statue of a Roman dignitary — Osama Shukir Muhammed Amin FRCP(Glasg), CC BY-SA 4.0
via Wikimedia Commons
Licences: creativecommons.org/licenses/by-sa/4.0/

All other archive images are in the public domain.
```

> **Blok se kopíruje CELÝ.** Atribuce je uvnitř něj schválně — u čtyř
> videí ze šestnácti chyběla právě proto, že kredity visely jako poznámka
> pod blokem (`docs/zverejneni.md`). Public domain snímky se nevypisují.

---

## 3. Náhled

`render/thumbnail.jpg` — **zatím není.** Princip je v `CLAUDE.md`
(„Thumbnail není titulková karta"), prováděcí zadání v
`docs/thumbnail-styl.md`. Kontrola `python tools/thumb_check.py videos/064-…`.

---

## 4. Titulky

`subtitles/*.srt`. Hotové: **`en`, `cs`**. Zbývá dvanáct jazyků podle
seznamu v `CLAUDE.md`.

Jazyk videa je **`en-gb`** (hlas `bf_emma`) a musí se nastavit **dřív**,
než se nahrají titulkové stopy — jinak zůstane dlaždice Titulky ve Studiu
zašedlá.

---

## 5. Nastavení

| | |
|---|---|
| kategorie | Education |
| jazyk videa | `en-gb` |
| licence | standardní |
| pro děti | **ne** |
| komentáře | zapnuté |

### Prohlášení o AI: **ne**

Rozhoduje fotorealističnost, ne použití AI. Video **nemá jedinou SDXL
scénu** — 196 diagramů je kreslených kódem, čtyři kresby v `art/` jsou
ploché linkové piktogramy (rozbor v `art/PUVOD.md`), archivní snímky jsou
upravené jen barevně a hudba je procedurální.

### Co musí uživatel naklikat sám

- **závěrečná obrazovka** — Data API na ni nemá ani zdroj (ověřeno
  2026-09-08). Místo na ni je v posledních šesti scénách a `zaver_check.py`
  hlásí u všech OK; prvky patří do **horní** poloviny obrazu, dole sedí
  titulek diagramu.
- při `videos.insert` navíc prohlášení o AI a osvědčení o zproštění —
  při ručním nahrání MP4 to vyřídí průvodce.

---

## 6. Tagy

```
gender, clothing, fashion history, social norms, conventions, why do we
dress like this, men's and women's clothing, pink and blue, high heels
history, trousers history, ancient rome, cultural norms, sociology,
explainer, there's more to it
```

---

## 7. Playlist

`spolecnost` — „How Society Actually Runs". Sousedi 050, 057 a 063.
Dopiš slug do `playlisty.json`, spusť `analytics.py --videa`
a pak `tools/playlisty.py`.
