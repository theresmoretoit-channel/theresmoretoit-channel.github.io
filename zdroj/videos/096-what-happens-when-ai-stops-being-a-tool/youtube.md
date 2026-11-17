# YouTube — 096 „What Happens When AI Stops Being a Tool?"

Stav: **nahráno 2026-10-09** (`ooJbQ9F03dA`), zbývá jen ruční práce ve Studiu — master
`render/final-en-096.mp4` (render na 207 po S22c, S09 a hudbě, 1920×1080, 390,7 s,
`ffmpeg -f null` bez chyb). Pracovní kopie na 207 smazána po nahrání.

| | |
|---|---|
| ID videa | `ooJbQ9F03dA` (https://www.youtube.com/watch?v=ooJbQ9F03dA) |
| nastavení, popis, tagy | ✅ 2026-10-09 (`nahraj.py --k-videu --bez-titulku`) |
| náhled | ✅ nahrán; `render/thumbnail.jpg` (AI AGENT / WHO SAID YES?) |
| lokalizace | ✅ 13 jazyků (`lokalizace.py`) |
| automatický přepis | ✅ čisto (žádná asr stopa) |
| titulky | ✅ 15 stop přes API (14 jazyků + `en-US`); 8 v noci, zbylých 7 po resetu kvóty 9:01 |
| playlist | ✅ `ai` (playlist má automatické řazení — `playlisty.py` vkládá bez pozice) |
| závěrečná obrazovka, americká stopa | ⬜ uživatel ve Studiu |

**Co musí uživatel naklikat sám:** nahrát MP4 ve Studiu (průvodce vyřídí
prohlášení o AI a osvědčení o zproštění), závěrečnou obrazovku a americkou
audiostopu (`render/audio-en-US.m4a`).

Soubor k nahrání: `render/final-en-096.mp4` (stopáž 6:30, `work/timing.json`
total 390,6 s).

> Kdyby se znovu pouštěl `tts.py`, přepočítej kapitoly tady
> i v `youtube-preklady.md` a přegeneruj `en-US` přes `us_stopa.py`.

Pořadí podle CENY (`docs/zverejneni.md`):

```bash
V=videos/096-what-happens-when-ai-stops-being-a-tool
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
What Happens When AI Stops Being a Tool?
```

> Wh-otázka, 40 znaků, totožná s nadpisem `script.md`. Neprozrazuje, co AI
> místo nástroje bude, ani pointu (že rozkazy může dávat i to, co agent čte).

---

## 2. Popis

```
Researchers at METR measure AI in an unusual way: not by how clever it is, but by how long a task it can finish on its own. From 2019 to 2024, that length doubled roughly every seven months. Today the best models can tackle work that would take a person two full working days.

That changes what AI is. A chatbot answers. An agent is given a goal, a browser, files and a terminal, and it acts. In July 2025, an AI coding agent wiped a production database in the middle of a code freeze. So when an agent acts, who is actually giving the instructions?

Subtitles are written for this video, not auto-generated. An American English audio track is available as a second audio track.

CHAPTERS
00:00 A different way to measure AI
01:04 A very capable tool
01:24 Let it act
01:53 Chatbot or agent?
02:39 The price of access
03:02 The deleted database
03:51 Giving AI hands
04:24 Who gives the instructions?
05:17 A comment on Reddit
05:58 Who's really in charge?
06:08 From answers to actions
```

> **Blok se kopíruje CELÝ** (`docs/zverejneni.md`). Atribuce není potřeba:
> video nemá žádný archivní snímek (`sources.json` neexistuje), jen 49 scén
> kreslených kódem a dvě SDXL ilustrace (S20, S34).
>
> Kapitoly jsou ze scén S01, S08, S11, S16, S21, S24, S30, S34, S42, S47, S48
> (`work/timing.json`, zaokrouhleno dolů). Nejkratší kapitola je 10 s
> (S47 → S48, přesně 10,27 s), poslední 22 s; všechny ≥ 10 s, první na 00:00.
>
> Popis neprozrazuje pointu (prompt injection, S36–S47) — kapitoly
> „A comment on Reddit" a „Who's really in charge?" ji jen naznačují a jsou
> až pod otázkou, stejně jako u 095. Fakta (METR, zdvojení po sedmi měsících,
> dva pracovní dny, Replit v červenci 2025, code freeze) jsou ve `factcheck.md`.
> Popis neříká, čí databáze to byla ani jak dopadla (rollback), aby nepředbíhal
> S24–S27.

---

## 3. Náhled

✅ **AI AGENT / WHO SAID YES?** — kresleno kódem, koncept C2
(`thumbnail/c2-who-said-yes.svg` → `render/thumbnail.jpg`, 1280×720, 105 kB).
Koncepty a výběr v `thumbnail/KONCEPTY.md`.

---

## 4. Titulky

`subtitles/*.srt`, 14 jazyků + `en-US`. Jazyk videa **`en-gb`** (hlas
`bf_emma`) se musí nastavit dřív, než se nahrají titulkové stopy. Titulky
a lokalizace se nahrávají až po zapracování nálezů Codexu.

---

## 5. Nastavení

| | |
|---|---|
| kategorie | Science & Technology |
| jazyk videa | `en-gb` |
| licence | standardní |
| pro děti | **ne** |
| komentáře | zapnuté |
| **byla použita AI** | **ne** (návrh, rozhoduje uživatel). 49 scén kreslených kódem a 2 SDXL scény díky kotvě stylu jako malované ilustrace, ne fotorealismus; žádný archiv. Hudba procedurální, hlas není klon |

### Závěrečná obrazovka

`zaver_check.py` na masteru: S48–S51 OK (kresba do 1,6 %), takže závěrečná
obrazovka může být plných 20 s, **od 6:10**. Dlaždici i kolečko odběru do
**horní poloviny**, spodní rohy zabírá titulek. Dlaždice: návrh **097**
(*Why Would a Smart AI Help a Criminal?*), jakmile bude venku — téma navazuje;
do té doby **042** (*AI Didn't Start With ChatGPT*).

---

## 6. Tagy

```
AI agent, AI agents, what is an AI agent, chatbot vs agent, agentic AI,
METR, AI task length, Replit, Replit database deleted, Jason Lemkin,
prompt injection, Perplexity Comet, Brave, AI safety, AI browser,
science explainer, there's more to it
```

---

## 7. Playlist

Navrženo **`ai`** (*AI — Where It Came From and What It's Doing to Us*).
Dopiš slug do `playlisty.json`, spusť `analytics.py --videa` a pak
`tools/playlisty.py`. Pozor: 097 má navržený týž playlist a `playlisty.json`
je sdílený soubor — zapisuj, až nebude druhé sezení uprostřed zápisu.
