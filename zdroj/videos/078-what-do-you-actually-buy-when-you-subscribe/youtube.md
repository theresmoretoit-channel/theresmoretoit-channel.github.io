# YouTube — 078 „What Do You Actually Buy When You Subscribe?"

Stav: **HOTOVO** — závěrečnou obrazovku, americkou stopu a tagy (kontrola) naklikal uživatel ve Studiu a video naplánoval ke zveřejnění (2026-10-02).

| | |
|---|---|
| ID videa | `bdIsqdKqtTg` (https://www.youtube.com/watch?v=bdIsqdKqtTg) |
| nastavení, popis, tagy | ✅ 2026-10-02 `nahraj.py --k-videu=bdIsqdKqtTg --bez-titulku` |
| náhled | ✅ 2026-10-02 (týž běh), koncept C1, `thumbnail/PUVOD.md` |
| lokalizace | ✅ 2026-10-02 13 jazyků jedním voláním |
| automatický přepis | ✅ 2026-10-02 čisté (`--smaz-asr`, nic k smazání); za pár dní zopakovat |
| titulky | ✅ 2026-10-02 všech 15 stop (14 jazyků + `en-US`) |
| playlist | ✅ 2026-10-02 `bezne` |
| závěrečná obrazovka, americká stopa | ✅ 2026-10-02 ručně ve Studiu (uživatel) |

**Co musí uživatel naklikat sám:** nahrát MP4 ve Studiu (průvodce vyřídí
prohlášení o AI a osvědčení o zproštění), závěrečnou obrazovku a americkou
audiostopu (`render/audio-en-US.m4a`).

Soubor k nahrání: `render/final-en-078.mp4`.

Pořadí podle CENY (`docs/zverejneni.md`):

```bash
V=videos/078-what-do-you-actually-buy-when-you-subscribe
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
What Do You Actually Buy When You Subscribe?
```

> wh-otázka („What…") — podle `docs/kanal-metriky.md` nejlepší CTR. Titul
> neprozrazuje odpověď (vzdali jsme se vlastnictví, protože pohodlí za to stálo).

---

## 2. Popis

```
There was a time when buying an album, a film or a program meant you owned it. Today we pay every month for music, films, software, storage and games. So what do you actually get for that money?

This video starts with a cassette tape that nobody could switch off remotely, follows the move from files on your own disk to the cloud, and looks at the quiet shift from "I have the file" to "I have access to the file". It asks whether you could still live without subscriptions, what owning your own data really costs, and what happens when a service disappears, as it did in 2024 when Ubisoft shut down the servers for The Crew.

It isn't a video about subscriptions being a trick. They solve real problems, and convenience is worth paying for. But it is worth knowing what you are buying.

Subtitles are written for this video, not auto-generated. An American English audio track is available as a second audio track.

Full transcript, sources and translations: https://theresmoretoit-channel.github.io/videos/what-do-you-actually-buy-when-you-subscribe/

CHAPTERS
00:00 What did you actually buy?
01:04 A cassette tape
01:50 Computers and files
02:40 The cloud
03:02 From owning to access
03:43 Convenience is valuable
04:28 Software: the clearest trade-off
05:04 Could you live without subscriptions?
05:41 The price of owning things
06:53 Why subscriptions won
07:08 What if the service disappears?
08:01 When the internet goes down
08:23 What to teach children
08:53 The strangest part

IMAGE CREDITS
Fuji DR Type 1 Compact Cassette — Dillan Payne, CC BY-SA 4.0, via Wikimedia Commons
Licences: creativecommons.org/licenses/by-sa/4.0
```

> **Blok se kopíruje CELÝ** (`docs/zverejneni.md`) — atribuce je UVNITŘ.
> Jediný archivní snímek (S08) je CC BY-SA, tedy povinný. SDXL scény
> (S09, S13, S30) atribuci nepotřebují.
>
> Kapitoly jsou ze scén S01, S08, S13, S19, S21, S27b, S32, S36, S41, S47,
> S49, S52d, S54, S56 (`work/timing.json`, celkem 614,5 s). Všechny ≥ 10 s.
> **Po každém dalším běhu `tts.py` časy přepočítej** — a stejně tak
> v `youtube-preklady.md`.
>
> Popis drží míru jistoty scénáře: „isn't a video about subscriptions
> being a trick" (S28), The Crew jen to, co je ve `factcheck.md`.

---

## 3. Náhled

`render/thumbnail.jpg`: **hotový**, koncept C1 (kazeta s cenovkou „$9.99 / MONTH",
`SUBSCRIBED` / `WHAT DID YOU BUY?`, ChatGPT, dodal uživatel 2026-10-02). Původ
v `thumbnail/PUVOD.md`; `thumb_check.py`: jas 82,0, kontrast 96,7, uvnitř pásma kanálu.

---

## 4. Titulky

`subtitles/*.srt`, 14 jazyků + `en-US`. Jazyk videa **`en-gb`** (hlas
`bf_emma`) se musí nastavit dřív, než se nahrají titulkové stopy, jinak
zůstane dlaždice Titulky zašedlá.

---

## 5. Nastavení

| | |
|---|---|
| kategorie | Education |
| jazyk videa | `en-gb` |
| licence | standardní |
| pro děti | **ne** |
| komentáře | zapnuté |
| **byla použita AI** | **ne** — 69 scén kreslených kódem, 3 SDXL scény jako malované ilustrace, archivní snímek kazety jen barevně upravený, hudba procedurální, hlas není klon skutečné osoby |

### Závěrečná obrazovka

S60b–S61 mají **horní polovinu volnou** — dlaždici i kolečko odběru dej
do **horní** poloviny (dole je titulek).

---

## 6. Tagy

```
subscriptions, subscription economy, ownership, digital ownership,
streaming, cloud storage, software as a service, buy vs subscribe,
the crew ubisoft, owning your data, self hosting, linux, libreoffice,
explainer, there's more to it
```

---

## 7. Playlist

Playlist `bezne` („Ordinary Things, Awkward Questions"). Dopiš slug do
`playlisty.json`, spusť `analytics.py --videa` a pak `tools/playlisty.py`.
