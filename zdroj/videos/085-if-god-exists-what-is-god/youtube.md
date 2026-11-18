# YouTube — 085 „If God Exists, What Is God?"

Stav: **nahráno 2026-10-03** — https://www.youtube.com/watch?v=aUf8iYNeebk

| | |
|---|---|
| ID videa | `aUf8iYNeebk` |
| nastavení, popis, tagy | ✅ |
| náhled | ✅ C1 (`thumbnail/c1-poklop.png`) |
| lokalizace | ✅ 13 jazyků |
| automatický přepis | ✅ čisté |
| titulky | ✅ `en`, `en-US` přes API; **zbylých 13 jazyků doplní uživatel ručně ve Studiu** (kvóta) |
| playlist | ✅ `lide`, pozice 11 |
| závěrečná obrazovka, americká stopa | ⬜ uživatel ve Studiu |

**Co musí uživatel naklikat sám:** nahrát MP4 ve Studiu (průvodce vyřídí
prohlášení o AI a osvědčení o zproštění), závěrečnou obrazovku (dlaždice
**073**, na které S68 odkazuje) a americkou audiostopu (`render/audio-en-US.m4a`).

Soubor k nahrání: `render/final-en-085.mp4` (stopáž 12:09, `work/timing.json`
total 729,1 s).

Pořadí podle CENY (`docs/zverejneni.md`):

```bash
V=videos/085-if-god-exists-what-is-god
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
If God Exists, What Is God?
```

> Wh-otázka, 27 znaků, totožná s názvem projektu. Neprozrazuje pointu
> (že důkaz první příčiny neříká nic o ostatních vlastnostech). Podmínka
> „If God exists" zároveň odstíní spor o existenci, který video záměrně
> nevede.

---

## 2. Popis

```
Suppose we could prove that God exists. Would that settle the question? Or would it only open a new one: what exactly have we proved exists?

This video grants the first step and then asks what follows from it. Where would a creator of space be? What does "before" mean if time began with the universe? Could something be non-physical, conscious without a brain, or think without one thought following another? Is there only one? What does "all-powerful" mean, and what happens to free will if the future is already known? Is a creator necessarily good, and why would a being that needs nothing create anything at all?

Along the way it looks at the difference between "something caused the universe" and the much richer picture most people mean by God, and at where all that extra information comes from.

An earlier video asked what it would take to prove God exists: https://youtu.be/6IuuXCygHY0

Subtitles are written for this video, not auto-generated. An American English audio track is available as a second audio track.

Full transcript, sources and translations: https://theresmoretoit-channel.github.io/videos/if-god-exists-what-is-god/

CHAPTERS
00:00 Suppose we prove God exists
00:58 Where is God?
01:41 When did God exist?
02:29 What is God made of?
03:19 Something, or someone?
04:09 Consciousness without a brain
04:44 Thinking outside time
05:28 One creator, or many?
06:00 The rock too heavy to lift
06:54 Knowing the future
07:36 Is God good?
08:09 Does God need anything?
09:04 Two very different claims
09:50 Smuggling in extra information
10:25 So what is God?
10:56 Would we even recognise it?
11:30 The deeper question

IMAGE CREDITS
NAMA Machine d'Anticythère 1 — Marsyas, CC BY 2.5, via Wikimedia Commons
All other archive images are in the public domain.
Licences: creativecommons.org/licenses/by/2.5
```

> **Blok se kopíruje CELÝ** (`docs/zverejneni.md`) — atribuce je UVNITŘ.
> Povinná je jen u S84 (Antikythérský mechanismus, CC BY 2.5, autor podle
> Commons „Marsyas assumed"). S10 (Hubble, NASA/GSFC) a S38 (Cajal) jsou
> public domain. Ilustrace z ChatGPT (S06, S16, S27, S73, S92, `art/`) se
> neuvádějí, stejně jako u 079.
>
> Kapitoly jsou ze scén S01, S10, S16, S22, S29, S37, S41, S47, S51, S59,
> S65, S69, S77, S83, S88, S92, S96 (`work/timing.json`, časy zaokrouhlené
> dolů). S22 začíná v 2:29, tedy hned za CTA (S21b 2:21–2:29). Nejkratší
> kapitola je 31 s (S88–S92), všechny ≥ 10 s.
> **Po každém dalším běhu `tts.py` časy přepočítej** — a stejně tak
> v `youtube-preklady.md`.
>
> Popis klade otázky ze scénáře a neodpovídá na ně; nepřidává žádné
> tvrzení, které by nebylo ve `factcheck.md`. Odkaz na 073 kvůli S68
> („As we saw in an earlier video").

---

## 3. Náhled

**Ještě není.** Koncepty podle `docs/thumbnail-styl.md`, pak
`render/thumbnail.jpg`, `thumbnail/PUVOD.md`, `thumb_check.py` a doplnit
`thumbnail` v `project.json`. `nahraj.py --k-videu` náhled nepotřebuje.

---

## 4. Titulky

`subtitles/*.srt`, 14 jazyků + `en-US`. Jazyk videa **`en-gb`** (hlas
`bf_emma`) se musí nastavit dřív, než se nahrají titulkové stopy. **Nahrávat
až po Codexu** na všech jazycích.

---

## 5. Nastavení

| | |
|---|---|
| kategorie | Education |
| jazyk videa | `en-gb` |
| licence | standardní |
| pro děti | **ne** |
| komentáře | zapnuté |
| **byla použita AI** | **ne** — scény kreslené kódem, 3 archivní snímky jen barevně upravené, žádná SDXL scéna, hudba procedurální, hlas není klon. Pět ilustrací z ChatGPT: S06, S73, S92 jsou zjevně malba; **S16 a S27 jsou blíž fotografii** (zátiší při svíčce), ale neukazují skutečnou osobu, místo ani událost. Uživatel 2026-10-03 rozhodl, že zůstávají (`art/PUVOD.md`); odpověď v průvodci Studia je na něm |

### Závěrečná obrazovka

`zaver_check.py`: S99–S102 (od 709 s) mají kresbu do 4,3 %, takže dlaždice i kolečko
odběru se vejdou kamkoli kromě spodku (titulek). Dej je do **horní**
poloviny. Dlaždice: **073** (*What Would It Take to Prove God?*).

---

## 6. Tagy

```
what is god, if god exists, nature of god, attributes of god,
philosophy of religion, cosmological argument, first cause, omnipotence
paradox, omnipotence, omniscience, free will, divine foreknowledge,
problem of evil, monotheism, theology, metaphysics, explainer,
there's more to it
```

---

## 7. Playlist

Navrženo **`lide`** — tam jsou 068 (*Why do people still believe in God*)
a 073, tedy obě předchozí videa téže řady. Dopiš slug do `playlisty.json`
za 073, spusť `analytics.py --videa` a pak `tools/playlisty.py`.
