# YouTube — 089 „Why Can You Still Buy a Phone With a Keyboard?"

Stav: **hotovo — nahráno 2026-10-20 (JHO2onZxZG4), naplánováno na zveřejnění** — bez odpovědi Unihertzu i Clicks, **zveřejňuje se** (rozhodnuto 2026-10-20). Master `render/final-en-089.mp4` hotový 2026-10-20 (.207, hudba −36 dB jen v úsecích S01–S05, S16–S20, S32–S36, S57–S65 = 36 % stopáže, 7:28, −14,0 LUFS), US stopa přemíchána.

| | |
|---|---|
| ID videa | `JHO2onZxZG4` |
| nastavení, popis, tagy | ✅ 2026-10-20 |
| náhled | ✅ C4 (`thumbnail/c4-keys.svg`) → `render/thumbnail.jpg` |
| lokalizace | ✅ 2026-10-20, 13 jazyků (`youtube-preklady.md`), Codex proběhl a nálezy zapracované |
| automatický přepis | ✅ čisto (2026-10-20) |
| titulky | ✅ 2026-10-20 (API spadlo na kvótě, zbytek uživatel naklikal ručně ve Studiu) — 14 jazyků + `en-US`, překlady prošly Codexem (commit `f9866e62`) |
| playlist | ✅ `legacy`, uživatel přidal ručně 2026-10-20 (`playlisty.json` souhlasí) |
| závěrečná obrazovka, americká stopa | ✅ 2026-10-20 ručně, video naplánované na zveřejnění |

**Co musí uživatel naklikat sám:** nahrát MP4 ve Studiu (průvodce vyřídí
prohlášení o AI a osvědčení o zproštění), závěrečnou obrazovku a americkou
audiostopu (`render/audio-en-US.m4a`).

Soubor k nahrání: `render/final-en-089.mp4` (stopáž 7:28, `work/timing.json`
total 448,6 s).

Pořadí podle CENY (`docs/zverejneni.md`):

```bash
V=videos/089-why-can-you-still-buy-a-phone-with-a-keyboard
python tools/nahraj.py $V --k-videu=<ID> --bez-titulku    # 100
python tools/analytics.py --videa                         #   1  ← nutné
python tools/lokalizace.py $V                             #  50  ← až po Codexu
python tools/titulky.py $V --smaz-asr                     # 150  ← před titulky
python tools/titulky.py $V                                # 400×15
python tools/playlisty.py                                 #  50
```

---

## 1. Titul

```
Why Can You Still Buy a Phone With a Keyboard?
```

> Wh-otázka, 46 znaků, totožná s nadpisem `script.md`. Neprozrazuje
> odpověď (hmat, zkratky, a že scénáře kanálu vznikají na takovém telefonu).

---

## 2. Popis

```
5G. A recent version of Android. Twelve gigabytes of memory. And a physical QWERTY keyboard. Not a ten-year-old BlackBerry from eBay, but a phone you can buy today.

Touchscreens won this fight more than fifteen years ago. So why does a phone like this still exist? And who would actually want one?

From BlackBerry to the Unihertz Titan, the Astro Slide, the F(x)tec Pro1 X and the Clicks Communicator: what can physical keys do that glass can't, why don't Samsung, Apple or Google make phones like this — and is the keyboard on a phone really dead?

Subtitles are written for this video, not auto-generated. An American English audio track is available as a second audio track.

Full transcript, sources and translations: https://theresmoretoit-channel.github.io/videos/why-can-you-still-buy-a-phone-with-a-keyboard/

CHAPTERS
00:00 A new phone with a keyboard
00:35 BlackBerry
01:06 Then came the iPhone
01:43 The end of the story?
02:00 Unihertz Titan
02:49 Not the only one
03:48 Why physical keys?
04:38 Keys as shortcuts
05:07 Problem one: space
05:31 Problem two: language
05:54 It's economics
06:33 Is the keyboard dead?
07:02 The unexpected answer

IMAGE CREDITS
iPhone First Generation — Carl Berkeley from Riverside California, CC BY-SA 2.0, via Wikimedia Commons
Titan 2 and Titan 2 Elite product images: Unihertz
Clicks Communicator image: Clicks Technology
All other archive images are in the public domain.
Licences: creativecommons.org/licenses/by-sa/2.0
```

> **Blok se kopíruje CELÝ** (`docs/zverejneni.md`) — atribuce je UVNITŘ.
> Povinná je u S11 (Carl Berkeley, CC BY-SA 2.0). Produktové fotky Unihertz
> (S01–S03, S21, S22) a Clicks (S30) jsou použité bez svolení a jejich
> uvedení je znění z `art/PUVOD.md`. S07 (BlackBerry, Evan-Amos) je public
> domain. Vlastní fotky uživatele (S19, S62, S63) a SDXL S17 se neuvádějí.
>
> Kapitoly jsou ze scén S01, S06, S11, S16, S19, S25, S32, S40, S44, S48,
> S52, S57, S61 (`work/timing.json`, časy zaokrouhlené dolů). S32 začíná
> v 3:48, tedy za CTA (S31b 3:40–3:48). Nejkratší kapitola je 17 s
> (S16 → S19), všechny ≥ 10 s. **Po každém dalším běhu `tts.py` časy
> přepočítej** — a stejně tak v `youtube-preklady.md`.
>
> Popis neprozradí pointu S62 (scénář napsaný na tomhle telefonu) — kapitola
> „The unexpected answer" ji jen slibuje, stejně jako S05. Specifikace
> v prvním odstavci jsou ze S01 (ověřené ve `factcheck.md`).

---

## 3. Náhled

✅ **C4** (`thumbnail/c4-keys.svg`, kresleno kódem `thumbnail/gen.py`)
→ `render/thumbnail.jpg`, `KEYBOARD / WHO BUYS THIS?` nad oříznutou
produktovou fotkou Titanu 2. Původ, otisk a riziko v `thumbnail/PUVOD.md`.

---

## 4. Titulky

`subtitles/*.srt`, 14 jazyků + `en-US`. Jazyk videa **`en-gb`** (hlas
`bf_emma`) se musí nastavit dřív, než se nahrají titulkové stopy. Codex
proběhl na všech 13 překladech a nálezy jsou zapracované (cs a de dřív,
zbylých 11 v commitu `f9866e62`).

---

## 5. Nastavení

| | |
|---|---|
| kategorie | Science & Technology |
| jazyk videa | `en-gb` |
| licence | standardní |
| pro děti | **ne** |
| komentáře | zapnuté |
| **byla použita AI** | **ne** (návrh, rozhoduje uživatel). 63 scén kreslených kódem, 2 archivní snímky jen barevně upravené, produktové fotky výrobců a vlastní fotky uživatele jsou skutečné fotografie bez generování, jediná SDXL scéna (S17) malířským stylem, hudba procedurální, hlas není klon |

### Závěrečná obrazovka

`zaver_check.py`: S62–S65 mají kresbu do 10 %, dlaždice i kolečko odběru
se vejdou kamkoli kromě spodních rohů (titulek); u S62 navíc **ne vlevo
nahoře** (telefon). Dej je do **horní poloviny vpravo**. Dlaždice: návrh
**079** (*Why Is This 90-Year-Old Airplane Still Flying?*) — totéž téma,
stará technika, která přežila, protože je pro někoho pořád nejlepší.

---

## 6. Tagy

```
phone with keyboard, physical keyboard phone, qwerty phone, blackberry,
unihertz titan 2, titan 2 elite, astro slide, fxtec pro1 x,
clicks communicator, keyboard smartphone, android phone with keyboard,
touchscreen vs physical keyboard, smartphone history, tech explainer,
explainer, there's more to it
```

---

## 7. Playlist

Navrženo **`legacy`** — sousedí s 079 (letadlo staré 90 let, které pořád
létá) a 033 (Linux); téma „stará technika, která nezmizela". Dopiš slug do
`playlisty.json`, spusť `analytics.py --videa` a pak `tools/playlisty.py`.
