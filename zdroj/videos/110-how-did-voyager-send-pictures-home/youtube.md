# YouTube — 110 „How Did Voyager Send Pictures Home?“

Stav: **nahráno 2026-10-15** (https://www.youtube.com/watch?v=QUQP72iXJgM). Metadata, náhled a 13 lokalizací přes API, titulky en/cs/sv/es přes API; zbylé titulky, playlist, americkou stopu, závěrečnou obrazovku a naplánované zveřejnění naklikal uživatel ve Studiu. Stav zveřejnění je v `Témata.ods`.

| | |
|---|---|
| ID videa | `QUQP72iXJgM` |
| master | ✅ `render/final-en-110.mp4` (8:38, 1920×1080, 58 MB, render 2026-10-15 na .207, `ffmpeg -v error` čistý) |
| náhled | ✅ `render/thumbnail.jpg` (1977 / HOW DID IT SEE NEPTUNE?) — `thumbnail/PUVOD.md` |
| nastavení, popis, tagy | podklady níž |
| lokalizace | ✅ `youtube-preklady.md`, 13 jazyků, prošlo Codexem (6 oprav), nahráno |
| titulky | ✅ en/cs/sv/es přes API, zbytek ručně ve Studiu (kvóta 2026-10-15 došla na pt-BR) |
| americká stopa | `render/audio-en-US.m4a` — nahrává uživatel ve Studiu |
| závěrečná obrazovka | ručně ve Studiu |
| playlist | ✅ `vesmir` (ručně ve Studiu; zapsáno i v `playlisty.json`) |

**Co musí uživatel naklikat sám:** nahrát MP4 ve Studiu (průvodce vyřídí
prohlášení o AI a osvědčení o zproštění), závěrečnou obrazovku a americkou
audiostopu (`render/audio-en-US.m4a`).

Stopáž 8:38 (`work/timing.json` total 518,2 s).

> Kdyby se znovu pouštěl `tts.py`, přepočítej kapitoly tady
> i v `youtube-preklady.md` a přegeneruj `en-US` přes `us_stopa.py`.

Pořadí podle CENY (`docs/zverejneni.md`):

```bash
V=videos/110-how-did-voyager-send-pictures-home
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
How Did Voyager Send Pictures Home?
```

> Wh-otázka, 35 znaků. Rozhodl uživatel (zadání k v0.2). Odpověď
> (vidicon → čísla → páska → rádio, a software přepsaný za letu) titul
> neprozrazuje.

---

## 2. Popis

```
In August 1989, Voyager 2 flew past Neptune, more than four billion kilometres from Earth, and took pictures of it. Its cameras were built around television tubes designed in the 1970s, with no memory card and no sensor like the one in your phone. And yet thousands of pictures arrived.

The story starts twelve years before Voyager's launch, with Mariner 4 at Mars and the first close-up image of another planet, which engineers at JPL coloured in by hand with pastels. It passes through a lab at Kodak, where Steven Sasson built a very different kind of camera in 1975. And it ends with the most famous picture Voyager ever took: the Pale Blue Dot, sent home from six billion kilometres away.

Sources: Ludwig & Taylor, Voyager Telecommunications (JPL DESCANSO, 2002); PDS Rings Node, Voyager Narrow Angle Camera description; J. Tomayko, Computers in Spaceflight (NASA CR-182505, 1988); B. A. Smith, Voyager Imaging Science Investigations (NASA, 1979); NSSDC, Mariner 4; Caltech Magazine, A Planet Painted by Hand; IEEE Spectrum, history of the first digital camera; NASA Photojournal PIA00451–PIA00453.

Subtitles are written for this video, not auto-generated. An American English audio track is available as a second audio track.

Full transcript, sources and translations: https://theresmoretoit-channel.github.io/videos/how-did-voyager-send-pictures-home/

CHAPTERS
00:00 A camera built around a TV tube
00:35 Mariner 4 at Mars
01:32 A picture coloured in by hand
02:06 A camera in a lab at Kodak
03:10 Voyager's cameras
04:17 Getting the pictures home
05:04 Rebuilding the dishes on Earth
05:24 New software for a distant spacecraft
06:27 So were they digital cameras?
06:55 The Pale Blue Dot
08:06 Eleven weeks to come home

IMAGE CREDITS
Very Large Array, New Mexico — CGP Grey, CC BY 2.0
via Wikimedia Commons
Licence: creativecommons.org/licenses/by/2.0
All other archive images: NASA, NASA/JPL, NASA/JPL-Caltech, NASA/GRC, public domain.
```

> **Blok se kopíruje CELÝ** (`docs/zverejneni.md`). Jediný CC BY snímek je
> S34 (VLA, CGP Grey), jeho atribuce je uvnitř. Ostatních dvanáct archivních
> snímků je NASA (S11 s creditem NASA/JPL-Caltech/Dan Goods, fotka rámu
> s ručně vybarveným Marsem).
>
> **Pointa se neprozrazuje.** Popis jmenuje Mariner, pastelky, Sassona
> a Pale Blue Dot (to je známé a láká), ale ne to, jak se obraz dostal
> domů — řetěz ani kompresi přeprogramovanou za letu.
>
> Kapitoly ze scén S01, S05, S11, S14, S20, S27, S33, S35, S41, S43, S51
> (`work/timing.json`, zaokrouhleno dolů). Nejkratší 20 s (S33 → S35),
> všechny ≥ 10 s, první na 00:00. Výzva k odběru S19b (3:01) leží
> v kapitole „A camera in a lab at Kodak“.
>
> Zdroje podle `factcheck.md`, „Zdroje“. Čísla v popisu (čtyři a šest
> miliard km, 1975) jsou tatáž jako ve scénáři.

---

## 3. Náhled

✅ `render/thumbnail.jpg` — 1977 / HOW DID IT SEE NEPTUNE? (televizor ze
70. let s Neptunem na obrazovce). Hotový obrázek od uživatele (ChatGPT,
zadání C), jen zmenšený; původ a otisk v `thumbnail/PUVOD.md`, zadání
v `thumbnail/ZADANI.md`.

---

## 4. Titulky

`subtitles/*.srt`, 14 jazyků + `en-US`. Jazyk videa **`en-gb`** (hlas
`bf_emma`) se musí nastavit dřív, než se nahrají titulkové stopy.
Nahrávají se až po zapracování nálezů Codexu.

---

## 5. Nastavení

| | |
|---|---|
| kategorie | **Science & Technology** (28) — posílá `nahraj.py` napevno |
| jazyk videa | `en-gb` |
| licence | standardní |
| pro děti | **ne** |
| komentáře | zapnuté |
| **byla použita AI** | **ne**. 42 scén je kreslených kódem, 13 archivních snímků (NASA, CGP Grey) je jen barevně upravených (*color adjustment* je výslovná výjimka); S49 má navíc decentní kroužek kolem Země, tedy popisek, ne změnu obsahu. Žádná SDXL scéna. Hudba je procedurální, hlas není klon. |

### Závěrečná obrazovka

Od **8:18** (posledních 20 s), tedy S52–S54. S51–S54 kreslí jen do
**dolní poloviny**, prvky patří **nahoru**.

---

## 6. Tagy

```
voyager, voyager 1, voyager 2, nasa, jpl, pale blue dot, carl sagan,
neptune, mariner 4, vidicon, digital camera, steven sasson, ccd,
deep space network, space probe, image compression, space history,
astronomy, science explainer, there's more to it
```

---

## 7. Playlist

`vesmir` (*Space — Getting There, and Who Else Is Out There*), na konec.
