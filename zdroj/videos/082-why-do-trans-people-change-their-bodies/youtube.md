# YouTube — 082 „Why Do Trans People Change Their Bodies?"

Stav: **nahráno 2026-10-23** (`render/final-en-082.mp4`, 668,3 s, render .207, kopie na .207 i lokální draft smazány)

| | |
|---|---|
| ID videa | `aCWof8TGYyc` — https://youtu.be/aCWof8TGYyc |
| nastavení, popis, tagy | ✅ 2026-10-23 `nahraj.py --k-videu --bez-titulku` |
| náhled | ✅ C1 (ChatGPT), `thumbnail/PUVOD.md` |
| lokalizace | ✅ 13 jazyků |
| titulky | ✅ 15 stop (14 jazyků + en-US), automatický přepis nebyl |
| playlist | ✅ `spolecnost`, `bezne` (za 081), `trans` (nový, 080–082) |
| závěrečná obrazovka, americká stopa | ✅ naklikáno uživatelem, zveřejnění naplánované (2026-10-23) |

**Co musí uživatel naklikat sám:** nahrát MP4 ve Studiu (průvodce vyřídí
prohlášení o AI a osvědčení o zproštění), závěrečnou obrazovku a americkou
audiostopu (`render/audio-en-US.m4a`).

Soubor k nahrání: `render/final-en-082.mp4` (stopáž 11:08, `work/timing.json`
total 668,3 s).

Pořadí podle CENY (`docs/zverejneni.md`):

```bash
V=videos/082-why-do-trans-people-change-their-bodies
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
Why Do Trans People Change Their Bodies?
```

> wh-otázka („Why…"), 40 znaků. Odpověď neprozrazuje — video ji staví
> postupně (váhy S03–S07, výplata S60–S71) a titul ji jen klade.

---

## 2. Popis

```
Imagine choosing surgery not because of an injury, and not because of an illness that shows up on a scan, but because something about your own body feels profoundly wrong. Imagine taking medication for years, knowing it will change you in ways you cannot fully predict. Why would anyone choose that?

This video looks at what medical transition actually involves and why some trans people pursue it. What hormone therapy can and cannot change. What surgery costs, in recovery, risk and money. What gender dysphoria is, and why it is so hard to understand from the outside when you don't feel it yourself. Why the idea that it's just a whim or a trend struggles to explain why anyone would accept all of that. And why some trans people choose not to transition medically at all.

This is the third video in a series about transgender people. The first asked why there suddenly seem to be so many trans people, the second how you know you're trans. The next one asks: why is it so hard to be trans?

Subtitles are written for this video, not auto-generated. An American English audio track is available as a second audio track.

Full transcript, sources and translations: https://theresmoretoit-channel.github.io/videos/why-do-trans-people-change-their-bodies/

CHAPTERS
00:00 Why would anyone choose that?
01:33 Transition is not one thing
01:59 What hormones actually do
03:35 Surgery: the price of a physical change
05:37 What if you don't feel it yourself?
06:45 Back to the question we started with
08:33 Why some people choose not to transition medically
09:35 The question we should really be asking
```

> **Blok se kopíruje CELÝ** (`docs/zverejneni.md`). Video nemá archivní
> snímek (`sources.json` neexistuje), takže sekce IMAGE CREDITS odpadá.
>
> Kapitoly jsou ze scén S01, S14, S19, S31, S48, S59, S72, S81
> (`work/timing.json` po odstranění mluvené výzvy, celkem 668,3 s, časy
> zaokrouhlené dolů). Šest kapitolových desek se čte nahlas, S01 nese
> otázku z S05 a S59 návrat k ní (začátek jádra). Nejkratší kapitola je
> 26,6 s (S14–S19), všechny ≥ 10 s. **Po každém dalším běhu `tts.py` časy
> přepočítej** — a stejně tak v `youtube-preklady.md`.
>
> Popis drží míru jistoty scénáře: hormony „can and cannot", jádro jen jako
> otázka („struggles to explain"), žádná čísla komplikací (rozhodnutí
> uživatele, video je neříká).

---

## 3. Náhled

**Koncepty C1–C3 v `thumbnail/KONCEPTY.md`.** Po dodání obrázku:
`render/thumbnail.jpg`, `thumbnail/PUVOD.md`, `thumb_check.py`.
`nahraj.py --k-videu` náhled nepotřebuje, jde dodat i později.

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
| **byla použita AI** | **ne** — 92 scén kreslených kódem (dvě z nich, S09 a S28, jsou SDXL ilustrace dotažené v ChatGPT, `art/PUVOD.md`, plochá malba), 4 SDXL scény v malované kotvě stylu (ne fotorealismus), žádná archivní fotka, hudba procedurální, hlas není klon skutečné osoby. Výzva k odběru je kresba (ikony Lucide), ne AI |

### Závěrečná obrazovka

`zaver_check.py`: S92–S95 (posledních 20 s) mají dole titulek — dlaždici
i kolečko odběru dej do **horní** poloviny. Jako dlaždici dalšího videa dej
**083**, až bude venku (S95 ohlašuje jeho titul); do té doby 081.

---

## 6. Tagy

```
transgender, trans people, gender transition, medical transition,
gender dysphoria, hormone therapy, gender-affirming surgery,
gender identity, detransition, trans healthcare,
explainer, there's more to it
```

---

## 7. Playlist

Tamtéž jako 080 a 081: `spolecnost` a `bezne`, v `playlisty.json` hned za
081. Po zveřejnění `analytics.py --videa` a `playlisty.py`.
