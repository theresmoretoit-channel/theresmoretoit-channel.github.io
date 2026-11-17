# YouTube — 081 „How Do You Know You're Trans?"

Stav: **nahráno 2026-10-21** — https://www.youtube.com/watch?v=fvIgw3YEkoI

| | |
|---|---|
| ID videa | `fvIgw3YEkoI` (MP4 nahrál uživatel ve Studiu) |
| nastavení, popis, tagy | ✅ `nahraj.py --k-videu --bez-titulku` |
| náhled | ✅ C1 (`TRANS` / `HOW DO YOU KNOW?`), `thumbnail/PUVOD.md` |
| lokalizace | ✅ 13 jazyků po Codexu |
| titulky | ✅ `en`, `en-US` přes API, zbylých 13 jazyků ručně uživatel |
| automatický přepis | ⏳ `titulky.py --smaz-asr` neběžel (kvóta) — pustit jindy, 150 j. |
| playlist | ✅ `spolecnost`, `bezne` (za 080) |
| závěrečná obrazovka, americká stopa, zveřejnění | ✅ naklikáno a naplánováno uživatelem (2026-10-21) |
| úklid | ✅ `render/draft-en.mp4` a kopie na .207 smazány |

**Co musí uživatel naklikat sám:** nahrát MP4 ve Studiu (průvodce vyřídí
prohlášení o AI a osvědčení o zproštění), závěrečnou obrazovku a americkou
audiostopu (`render/audio-en-US.m4a`).

Soubor k nahrání: `render/final-en-081.mp4` (stopáž 10:57, `work/timing.json`
total 657,2 s).

Pořadí podle CENY (`docs/zverejneni.md`):

```bash
V=videos/081-how-do-you-know-youre-trans
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
How Do You Know You're Trans?
```

> wh-otázka („How…"), 29 znaků. Odpověď neprozrazuje — video ji nechává
> otevřenou (S90: pro někoho přijde brzy, pro jiného za roky, někdo
> jistou odpověď nenajde).

---

## 2. Popis

```
How do you know you're a man? Or a woman? Most people would simply say: I just know. They have never had to examine their gender identity, and nobody asks them to prove it. But what if that sense of certainty isn't there?

This video looks at how people come to understand that they're trans. Why it is often a slow process rather than a single dramatic moment. Why some people start asking these questions in childhood or puberty, and others at thirty, forty or sixty. Why it is hard to recognise something you don't have a word for. And why not fitting gender stereotypes, or being attracted to people of the same sex, is not the same thing as being trans.

It also looks at doubt, at people who suppress those feelings, at people who realise they're trans but decide not to transition, and at detransition: what it does and doesn't tell us.

This is the second video in a series about transgender people. The first one asked why there suddenly seem to be so many trans people. The next one asks: why do trans people change their bodies?

Subtitles are written for this video, not auto-generated. An American English audio track is available as a second audio track.

CHAPTERS
00:00 How do you know you're a man or a woman?
00:42 There isn't always a single moment
01:39 Childhood, puberty, adulthood
02:36 But why didn't you know earlier?
03:22 Maybe I'm not man enough
04:32 And what about sexuality?
05:07 What if I'm just imagining it?
05:42 Suppressing it
06:38 So do you have to transition?
07:16 Telling someone else
07:49 How do you know?
08:25 What if you're wrong?
09:27 So how do you know you're trans?

IMAGE CREDITS
Left-handed writing — Alejandro Escamilla, CC0, via Wikimedia Commons
```

> **Blok se kopíruje CELÝ** (`docs/zverejneni.md`). Jediný archivní snímek
> (S29) je **CC0**, takže atribuce povinná není; je tam ze slušnosti
> a nic nestojí.
>
> Kapitoly jsou ze scén S01, S07, S15, S24, S31, S41, S46, S52, S60, S66,
> S72, S77, S84 (`work/timing.json`, celkem 657,2 s, časy zaokrouhlené
> dolů). Mluvené nadpisy sekcí scénáře jsou zároveň kapitolami; S77
> a S84 mluvený nadpis nemají (notes.md), kapitola nese otázku, kterou
> scéna říká. Nejkratší kapitola je 32,9 s (S72–S77), všechny ≥ 10 s.
> **Po každém dalším běhu `tts.py` časy přepočítej** — a stejně tak
> v `youtube-preklady.md`.
>
> Popis drží míru jistoty scénáře: nic o tom, *jak* to člověk pozná
> (to je pointa, S76/S89), a u detranzice jen „what it does and doesn't
> tell us" (S81–S82). Žádná čísla — video žádná neříká.

---

## 3. Náhled

**Koncepty C1–C3 v `thumbnail/KONCEPTY.md`** (doporučen C1: tatáž ambrová
figurka jako v náhledu 080, sama, stín do otazníku, `TRANS` /
`HOW DO YOU KNOW?`). Po dodání obrázku: `render/thumbnail.jpg`,
`thumbnail/PUVOD.md`, `thumb_check.py`. `nahraj.py --k-videu` náhled
nepotřebuje, jde dodat i později.

---

## 4. Titulky

`subtitles/*.srt`, 14 jazyků + `en-US`. Jazyk videa **`en-gb`** (hlas
`bf_emma`) se musí nastavit dřív, než se nahrají titulkové stopy, jinak
zůstane dlaždice Titulky zašedlá. **Nahrávat až po Codexu** na všech
jazycích.

---

## 5. Nastavení

| | |
|---|---|
| kategorie | Education |
| jazyk videa | `en-gb` |
| licence | standardní |
| pro děti | **ne** |
| komentáře | zapnuté — **téma je konfliktní, počítej s moderací** |
| **byla použita AI** | **ne** — 88 scén kreslených kódem (z 96, včetně beatů dědících obraz; dvě z nich, S20 a S56, jsou SDXL ilustrace dotažené v ChatGPT, `art/PUVOD.md`, plochá malba), 7 SDXL scén v malované kotvě stylu (ne fotorealismus), 1 archivní fotka (ruka při psaní) jen barevně upravená, hudba procedurální, hlas není klon skutečné osoby |

### Závěrečná obrazovka

`zaver_check.py`: S92–S95 (od 637 s, posledních 20 s) mají **horní
polovinu volnou** (kresba pod 3 %) — dlaždici i kolečko odběru dej do
**horní** poloviny, dole je titulek. Jako dlaždici dalšího videa dej
**082**, až bude venku (S95 ohlašuje jeho titul); do té doby 080.

---

## 6. Tagy

```
transgender, trans people, gender identity, coming out,
questioning gender, gender dysphoria, transition, detransition,
gender stereotypes, sexual orientation, cisgender,
explainer, there's more to it
```

---

## 7. Playlist

Tamtéž jako 080: `spolecnost` („How Society Actually Runs") a `bezne`
(„Ordinary Things, Awkward Questions"), v `playlisty.json` hned za 080.
Po zveřejnění `analytics.py --videa` a `playlisty.py`.

Otevřené: **playlist série 080–084** — u 080 odloženo s tím, že „dává
smysl až s 081 venku". Rozhodne uživatel.

---

## Kontrola atribucí (2026-10-21)

`sources.json` má jedinou položku (S29), licence **CC0** — žádná
`CC BY*`, povinná atribuce 0/0. Autor (Alejandro Escamilla) v bloku je.
