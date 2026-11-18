# YouTube — 087 „What Would English Sound Like Without Articles?"

Stav: **nahráno 2026-10-05** — https://www.youtube.com/watch?v=Z0HYEjVHfpg

| | |
|---|---|
| ID videa | `Z0HYEjVHfpg` |
| nastavení, popis, tagy | ✅ |
| náhled | ✅ C2 (`thumbnail/c2-sazba.png`) → `render/thumbnail.jpg` |
| lokalizace | ✅ 13 jazyků |
| automatický přepis | ✅ čisté |
| titulky | ✅ 15 stop přes API (14 jazyků + `en-US`) |
| playlist | ✅ nový `jazyky` (`PLQjlRuTgr5nQ`), 087 první, 048 druhé |
| závěrečná obrazovka, americká stopa | ⏳ uživatel ve Studiu |

**Co musí uživatel naklikat sám:** nahrát MP4 ve Studiu (průvodce vyřídí
prohlášení o AI — odpověď **ne** — a osvědčení o zproštění), závěrečnou
obrazovku a americkou audiostopu (`render/audio-en-US.m4a`).

Soubor k nahrání: `render/final-en-087.mp4` (stopáž 8:13, `work/timing.json`
total 493,4 s).

Pořadí podle CENY (`docs/zverejneni.md`):

```bash
V=videos/087-what-would-english-sound-like-without-articles
python tools/nahraj.py $V --k-videu=<ID> --bez-titulku    # 100
python tools/analytics.py --videa                         #   1  ← nutné
python tools/lokalizace.py $V                             #  50
python tools/titulky.py $V --smaz-asr                     # 150  ← před titulky
python tools/titulky.py $V                                # 400×15
python tools/playlisty.py                                 # 100 (nový playlist + 2 položky)
```

---

## 1. Titul

```
What Would English Sound Like Without Articles?
```

> Wh-otázka, 47 znaků, totožná s nadpisem `script.md`. Neprozrazuje
> odpověď (že by angličtina fungovala, jen by dala víc práce) a „articles"
> pojmenuje téma hned.

---

## 2. Popis

```
I went to store and bought book. If English is your first language, that sounds wrong. And yet you understood every word of it. All that's missing are three tiny words: a, an and the.

Roughly a third of the world's languages have no articles at all, and their speakers get along perfectly well. So why does English bother? What do these little words actually do that nothing else can? Why are they among the last things learners of English get right? And where did they come from in the first place?

Subtitles are written for this video, not auto-generated. An American English audio track is available as a second audio track.

Full transcript, sources and translations: https://theresmoretoit-channel.github.io/videos/what-would-english-sound-like-without-articles/

CHAPTERS
00:00 I went to store and bought book
00:43 A dog or the dog?
01:20 Taking the articles away
02:14 English skips them too
02:48 One word, three meanings
03:21 How Czech does it
04:14 Pushing it harder
05:12 Where did articles come from?
05:52 When "one" stops counting
06:20 Latin's daughters did it too
06:45 The article at the end of the word
07:13 Bulgarian grew one, Czech didn't
07:38 How it sounds from the other side

IMAGE CREDITS
Base columna trajana — Aulldemolins, CC BY-SA 3.0, via Wikimedia Commons
All other archive images are in the public domain.
Licences: creativecommons.org/licenses/by-sa/3.0
```

> **Blok se kopíruje CELÝ** (`docs/zverejneni.md`) — atribuce je UVNITŘ.
> Povinná je jen u S55 (Trajánův sloup, CC BY-SA 3.0, Aulldemolins);
> S47 (rukopis Beowulfa) je public domain.
>
> Kapitoly jsou ze scén S01, S07, S12, S19, S24, S28, S35, S45, S52, S55,
> S59, S61, S64 (`work/timing.json`, časy zaokrouhlené dolů). Nejkratší
> kapitola je 24 s (S61–S64), všechny ≥ 10 s. Video nemá CTA (rozhodl
> uživatel, viz `notes.md`).
> **Po každém dalším běhu `tts.py` časy přepočítej** — a stejně tak
> v `youtube-preklady.md`.
>
> Popis klade otázky ze scénáře a neodpovídá na ně; nepřidává žádné
> tvrzení, které by nebylo ve `factcheck.md` („roughly a third" = WALS 37A/38A).

---

## 3. Náhled

✅ **C2** (`thumbnail/c2-sazba.png`, z ChatGPT) → `render/thumbnail.jpg`,
`THE / WHY BOTHER?`. Původ a měření v `thumbnail/PUVOD.md`, koncepty
v `thumbnail/KONCEPTY.md`.

---

## 4. Titulky

`subtitles/*.srt`, 14 jazyků + `en-US`. Jazyk videa **`en-gb`** (hlas
`bf_emma`) se musí nastavit dřív, než se nahrají titulkové stopy. Codex
proběhl na všech dvanácti přeložených jazycích (2026-10-05).

---

## 5. Nastavení

| | |
|---|---|
| kategorie | Education |
| jazyk videa | `en-gb` |
| licence | standardní |
| pro děti | **ne** |
| komentáře | zapnuté |
| **byla použita AI** | **ne** — 79 scén kreslených kódem, 2 archivní snímky jen barevně upravené, žádná SDXL scéna, žádná ilustrace z ChatGPT, hudba procedurální, hlas není klon |

### Závěrečná obrazovka

`zaver_check.py`: S67 a S68 mají kresbu do 3 %, dole je titulek. Dlaždici
i kolečko odběru dej do **horní** poloviny. Dlaždice: návrh **048**
(*Why Are Some Languages So Complicated?*) — týž nový playlist.

---

## 6. Tagy

```
articles, definite article, indefinite article, english grammar,
the word the, zero article, grammaticalisation, linguistics,
language learning, english as a second language, czech language,
swedish, norwegian, bulgarian, latin, history of english, explainer,
there's more to it
```

---

## 7. Playlist

**Nový playlist `jazyky`** (rozhodnuto 2026-10-05, návrh uživatele), 087
jako první, za ním 048. Je zapsaný v `playlisty.json`; `playlisty.py` ho
při prvním běhu založí i s popisem (popis se pak už jen naklikává).
Kandidát na doplnění po zveřejnění: 088 (*Why Is Computer Stuff Called
That?*, původ slov).
