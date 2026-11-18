# YouTube — 088 „Why Is Computer Stuff Called That?"

Stav: **nahráno 2026-10-05, dokončeno 2026-10-06** — https://www.youtube.com/watch?v=9c2d4Z1n1v4

| | |
|---|---|
| ID videa | `9c2d4Z1n1v4` |
| nastavení, popis, tagy | ✅ |
| náhled | ✅ C1 (`thumbnail/c1-poleno.png`) |
| lokalizace | ✅ 13 jazyků (2026-10-06, po Codexu) |
| automatický přepis | ✅ čisté (2026-10-05) |
| titulky | ✅ 15 stop (`en`, `en-US` + 13 jazyků) přes API, 2026-10-06; dvě kola Codexu |
| playlist | ✅ `jazyky` |
| závěrečná obrazovka, americká stopa | ⬜ uživatel ve Studiu |

**Co musí uživatel naklikat sám:** nahrát MP4 ve Studiu (průvodce vyřídí
prohlášení o AI a osvědčení o zproštění), závěrečnou obrazovku a americkou
audiostopu (`render/audio-en-US.m4a`).

Soubor k nahrání: `render/final-en-088.mp4` (stopáž 11:11, `work/timing.json`
total 670,6 s).

Pořadí podle CENY (`docs/zverejneni.md`):

```bash
V=videos/088-why-is-computer-stuff-called-that
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
Why Is Computer Stuff Called That?
```

> Wh-otázka, 34 znaků, totožná s nadpisem `script.md`. Neprozrazuje
> odpověď — že jména jsou vypůjčená od viditelného světa a u logu, bootu
> a bugu se obraz úplně vytratil.

---

## 2. Popis

```
This is a log. And so is the file your computer writes all day long. How did a piece of wood end up inside your computer?

Computers are full of words like this. Mouse. Desktop. Cloud. Bug. Some of them are obvious, some were chosen very carefully, and some have travelled so far that hardly anyone remembers where they started.

Why is the internet a "cloud"? What does a payload have to do with a truck? Why do computers "boot"? Was the first bug really a moth? And why does a background program have the name of a demon?

Subtitles are written for this video, not auto-generated. An American English audio track is available as a second audio track.

Full transcript, sources and translations: https://theresmoretoit-channel.github.io/videos/why-is-computer-stuff-called-that/

CHAPTERS
00:00 This is a log
00:36 The obvious ones: the mouse
01:00 The desktop
01:56 The cloud
02:34 The web
02:57 Packets
03:26 Payload
04:09 Stream and buffer
04:44 Pipeline
05:10 Padding
05:48 Back to the log
07:00 Booting
07:56 The bug
08:44 Daemon
09:41 Worm
10:28 The answer

IMAGE CREDITS
Replica of prototype Engelbart mouse, circa 1964, Computer History Museum — The wub, CC BY-SA 4.0, via Wikimedia Commons
Xerox Alto I, 1973, Computer History Museum — The wub, CC BY-SA 4.0, via Wikimedia Commons
Racks Amravati Data Center — PiDatacenters, CC BY-SA 4.0, via Wikimedia Commons
All other archive images are in the public domain.
Licences: creativecommons.org/licenses/by-sa/4.0
```

> **Blok se kopíruje CELÝ** (`docs/zverejneni.md`) — atribuce je UVNITŘ.
> Povinná je u S09, S12 (The wub) a S19 (PiDatacenters), všechny
> CC BY-SA 4.0. S36, S52, S65, S68 a S73 jsou public domain. SDXL scény
> a pavučina S22 upravená v ChatGPT (`art/`) se neuvádějí.
>
> Kapitoly jsou ze scén S01, S07, S11, S16, S21, S23, S27, S32, S38, S41,
> S46, S56, S63, S70, S77, S83 (`work/timing.json`, časy zaokrouhlené
> dolů). S16 začíná v 1:56, tedy za CTA (S14b 1:41–1:49). S46 a S47 jsou
> jen 7 s od sebe, proto jedna kapitola „Back to the log" od 5:48.
> Nejkratší kapitola je 23 s (S21 → S23), všechny ≥ 10 s.
> **Po každém dalším běhu `tts.py` časy přepočítej** — a stejně tak
> v `youtube-preklady.md`.
>
> Popis klade otázky ze scénáře a neodpovídá na ně; nepřidává žádné
> tvrzení, které by nebylo ve `factcheck.md`.

---

## 3. Náhled

✅ **C1** (`thumbnail/c1-poleno.png`, z ChatGPT) → `render/thumbnail.jpg`,
`LOG / WHY A LOG?`. Původ a měření v `thumbnail/PUVOD.md`, koncepty
v `thumbnail/KONCEPTY.md`.

---

## 4. Titulky

`subtitles/*.srt`, 14 jazyků + `en-US`. Jazyk videa **`en-gb`** (hlas
`bf_emma`) se musí nastavit dřív, než se nahrají titulkové stopy. Codex
proběhl na všech 13 překladech a nálezy jsou zapracované (commit `3127148b`).

---

## 5. Nastavení

| | |
|---|---|
| kategorie | Education |
| jazyk videa | `en-gb` |
| licence | standardní |
| pro děti | **ne** |
| komentáře | zapnuté |
| **byla použita AI** | **ne** (návrh, rozhoduje uživatel). Scény kreslené kódem, 8 archivních snímků jen barevně upravených, 4 SDXL scény malířským stylem (S22, S28, S33, S48 — S22 a S28 přegenerované právě kvůli fotorealismu), pavučina S22 upravená v ChatGPT je malba (`art/PUVOD.md`), hudba procedurální, hlas není klon |

### Závěrečná obrazovka

`zaver_check.py`: S86–S88 mají kresbu do 1 %, dlaždice i kolečko odběru
se vejdou kamkoli kromě spodních rohů (titulek). Dej je do **horní**
poloviny. Dlaždice: návrh **087** (*What Would English Sound Like Without
Articles?*) — sousední video o slovech.

---

## 6. Tagy

```
computer words, etymology, word origins, why is it called a log, bug,
first computer bug, bootstrapping, booting, daemon, maxwell's demon,
cloud computing, payload, buffer, computer worm, xerox parc,
computer history, explainer, there's more to it
```

---

## 7. Playlist

Navrženo **`jazyky`** (*Languages — Why We Speak the Way We Do*) — video je
o původu slov, sousedí s 087. Alternativa `legacy`. Dopiš slug do
`playlisty.json`, spusť `analytics.py --videa` a pak `tools/playlisty.py`.
