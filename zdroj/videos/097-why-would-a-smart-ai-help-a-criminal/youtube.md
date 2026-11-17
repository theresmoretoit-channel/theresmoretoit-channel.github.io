# YouTube — 097 „Why Would a Smart AI Help a Criminal?"

Stav: **nahráno 2026-10-09** (`c_5DqNv36BY`), zbývá jen ruční práce ve Studiu. Master `render/final-en-097.mp4` hotový
(2026-10-08, render na 207, 1920×1080, 505,1 s, `ffmpeg -f null` bez chyb).
Náhled C2 hotový (`render/thumbnail.jpg`).

| | |
|---|---|
| ID videa | `c_5DqNv36BY` (https://www.youtube.com/watch?v=c_5DqNv36BY), MP4 nahrál uživatel 2026-10-09 |
| nastavení, popis, tagy | ✅ 2026-10-09 (`nahraj.py --k-videu --bez-titulku`) |
| náhled | ✅ C2 IT KNOWS / SO WHY HELP? |
| lokalizace | ✅ 13 jazyků + en (`lokalizace.py`) |
| automatický přepis | ✅ smazán (asr=en) |
| titulky | ✅ 15 stop přes API (14 jazyků + `en-US`) |
| playlist | ✅ `ai`, pozice 4 |
| závěrečná obrazovka, americká stopa | ⬜ uživatel ve Studiu |

**Co musí uživatel naklikat sám:** nahrát MP4 ve Studiu (průvodce vyřídí
prohlášení o AI a osvědčení o zproštění), závěrečnou obrazovku a americkou
audiostopu (`render/audio-en-US.m4a`).

Soubor k nahrání: `render/final-en-097.mp4` (stopáž 8:25, `work/timing.json`
total 505,1 s).

> Kdyby se znovu pouštěl `tts.py`, přepočítej kapitoly tady
> i v `youtube-preklady.md` a přegeneruj `en-US` přes `us_stopa.py`.

Pořadí podle CENY (`docs/zverejneni.md`):

```bash
V=videos/097-why-would-a-smart-ai-help-a-criminal
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
Why Would a Smart AI Help a Criminal?
```

> Wh-otázka, 37 znaků, totožná s nadpisem `script.md`. Neprozrazuje
> pointu (úmysl dodává člověk, AI jen práci) — zdrojový titul uživatele
> *AI Doesn't Have to Be Evil* by ji vyzradil, proto změněn (notes.md).

---

## 2. Popis

```
Ask a chatbot to write a scam email and it will probably say no. But in the summer of 2023, a chatbot advertised as having no ethical limits went on sale on a hacker forum, and it did exactly what it was built to do.

If an AI is smart enough to know that something is a crime, why doesn't it simply refuse? What do Asimov's Three Laws of Robotics have to do with it, and why is "do not hurt people" so hard to turn into a rule a computer can follow?

Subtitles are written for this video, not auto-generated. An American English audio track is available as a second audio track.

CHAPTERS
00:00 An AI that helps anyway
00:47 WormGPT and FraudGPT
01:45 Why not just give it a rule?
02:46 What does harm mean?
03:13 What the computer actually sees
04:07 Same words, different intent
04:33 A strange kind of bus
05:08 Not a thought experiment
06:08 Skynet and SHODAN
06:42 Whose morality?
07:34 Build it like other powerful things
08:04 Who's holding it?

IMAGE CREDITS
Isaac Asimov — Phillip Leonian, New York World-Telegram & Sun, public domain, via Wikimedia Commons
```

> **Blok se kopíruje CELÝ** (`docs/zverejneni.md`). Jediný archivní snímek
> (S17, Asimov) je public domain, takže atribuce povinná není — uvedená je
> ze slušnosti.
>
> Kapitoly jsou ze scén S01, S09, S16, S25, S29, S33, S37, S42, S49, S54,
> S61, S65 (`work/timing.json`, zaokrouhleno dolů). Nejkratší kapitola je
> 26 s (S29 → S33 a S33 → S37), poslední 21 s; všechny ≥ 10 s, první na
> 00:00. Výzva k odběru S15b leží na konci kapitoly „WormGPT and FraudGPT".
>
> Popis neprozrazuje odpověď (AI dodá práci, úmysl člověk; omezená
> oprávnění) — kapitoly ji naznačují jen v posledních dvou, a ty jsou až
> pod otázkou. Fakta (WormGPT v létě 2023 na hackerském fóru, bez etických
> zábran, Asimovovy tři zákony) jsou ve `factcheck.md`.

---

## 3. Náhled

✅ **IT KNOWS / SO WHY HELP?** — C2 kreslený kódem (`thumbnail/c2-it-knows.svg` → `render/thumbnail.jpg`), koncepty v `thumbnail/KONCEPTY.md`.

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
| **byla použita AI** | **ne** (návrh, rozhoduje uživatel). 67 scén kreslených kódem, 1 archivní fotografie jen barevně upravená (*color adjustment* je výslovná výjimka), 3 SDXL scény: S50 a S62 malované, S29 (serverovna) vyšla realističtěji, ale nezobrazuje žádné konkrétní skutečné místo ani událost — uživatel ji 2026-10-08 přijal. Hudba procedurální, hlas není klon |

### Závěrečná obrazovka

`zaver_check.py` na masteru: S65–S67 OK (kresba do 2,5 %), takže závěrečná
obrazovka může být plných 20 s, **od 8:05**. Dlaždici i kolečko odběru do
**horní poloviny**, spodní rohy zabírá titulek. Dlaždice: návrh **096**
(*What Happens When AI Stops Being a Tool?*) — sesterské video, až bude
zveřejněné; jinak libovolné z playlistu `ai`.

---

## 6. Tagy

```
AI, artificial intelligence, AI safety, AI ethics, AI misuse,
WormGPT, FraudGPT, AI agents, cybercrime, Asimov, Three Laws of Robotics,
SHODAN, System Shock, Skynet, Moral Machine, AI alignment,
science explainer, there's more to it
```

---

## 7. Playlist

Navrženo **`ai`**. Dopiš slug do `playlisty.json`, spusť
`analytics.py --videa` a pak `tools/playlisty.py`.
