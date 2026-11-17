# YouTube — 083 „Why Is It So Hard to Be Trans?"

Stav: **zveřejněno 2026-10-24** (`render/final-en-083.mp4`, 781,2 s, render .207, kopie na .207 i lokální draft smazány)

| | |
|---|---|
| ID videa | `mUjn7p8_GVo` — https://youtu.be/mUjn7p8_GVo |
| nastavení, popis, tagy | ✅ 2026-10-24 `nahraj.py --k-videu --bez-titulku` |
| náhled | ✅ C1 (ChatGPT), `thumbnail/PUVOD.md` |
| lokalizace | ✅ 13 jazyků |
| titulky | ✅ API: en, en-US, cs, sv (automatický přepis nebyl); zbylých 11 jazyků ✅ ručně uživatel (kvóta) |
| playlist | ✅ `spolecnost`, `bezne` (za 082), `trans` |
| ručně ve Studiu | ✅ MP4 (průvodce: AI, zproštění), závěrečná obrazovka (dlaždice 082), americká audiostopa |

**Až vyjde 084:** vyměnit dlaždici závěrečné obrazovky z 082 na 084.

Soubor k nahrání: `render/final-en-083.mp4` (stopáž 13:01, `work/timing.json`
total 781,2 s).

Pořadí podle CENY (`docs/zverejneni.md`):

```bash
V=videos/083-why-is-it-so-hard-to-be-trans
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
Why Is It So Hard to Be Trans?
```

> wh-otázka („Why…"), 30 znaků. Neprozrazuje odpověď — video ji skládá
> z pohledu zvenčí (passing, stereotypy, obtěžování, rodina a práce,
> sexualizace, soukromí), titul se jen ptá.

---

## 2. Popis

```
Before you say a word, people have already decided whether you are a man or a woman. Most of the time, nobody notices this happening. But what happens when the way people see you doesn't match who you are?

This video looks at what it is like to be transgender in a world that judges from the outside. What passing means, and why it is not proof of anyone's identity. Who decides what a man or a woman should look like. How harassment, and the possibility of it, shapes ordinary decisions, and what the largest survey of trans people in the United States found. How rejection by family, at work or in healthcare can make everyday life harder. Why so many questions asked publicly about trans people are about their bodies. And why being transgender is not information that automatically belongs to everyone who meets you.

This is the fourth video in a series about transgender people. The earlier ones asked why there suddenly seem to be so many trans people, how you know you're trans, and why trans people change their bodies. The final one asks: when does society become the problem?

Subtitles are written for this video, not auto-generated. An American English audio track is available as a second audio track.

CHAPTERS
00:00 The first thing people notice
01:21 What does passing actually mean?
02:57 Who decides what a man or woman should look like?
04:58 When being different has a cost
07:00 Family, work and everyday life
08:43 Why is everything about trans people so sexualised?
10:17 The right to privacy
11:41 What would acceptance actually look like?
```

> **Blok se kopíruje CELÝ** (`docs/zverejneni.md`). Video nemá archivní
> snímek (`sources.json` neexistuje), takže sekce IMAGE CREDITS odpadá.
>
> Kapitoly jsou kapitolové desky S11, S22, S34, S47, S59, S70, S80
> (`work/timing.json` draftu 4, celkem 781,2 s, časy zaokrouhlené dolů).
> První kapitola nese nečtený nadpis sekce 1 ze zdroje uživatele. Nejkratší
> kapitola je 81 s (S70–S80). Teaser na 084 (S87–S91, 12:32) samostatnou
> kapitolu nemá, stejně jako u 082. **Po každém dalším běhu `tts.py` časy
> přepočítej** — a stejně tak v `youtube-preklady.md`.
>
> Popis drží míru jistoty scénáře: průzkum USTS 2022 jen jmenuje, čísla
> neuvádí (ve videu je výhrada, že nejde o náhodný vzorek); *„not proof"*
> u passingu je věta S18.

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
| **byla použita AI** | **ne** — 91 scén kreslených kódem (dvě z nich, S56 a S67, jsou SDXL ilustrace dotažené v ChatGPT, `art/PUVOD.md`, plochá malba), 1 SDXL scéna (S38) v malované kotvě stylu (ne fotorealismus), žádná archivní fotka, hudba procedurální, hlas není klon skutečné osoby. Výzva k odběru je kresba (ikony Lucide), ne AI |

### Závěrečná obrazovka

`zaver_check.py`: S88–S91 (posledních 20 s) mají dole titulek — dlaždici
i kolečko odběru dej do **horní** poloviny. Jako dlaždici dalšího videa dej
**084**, až bude venku (S91 ohlašuje jeho otázku); do té doby 082.

---

## 6. Tagy

```
transgender, trans people, passing, gender identity,
gender stereotypes, harassment, discrimination, trans acceptance,
privacy, outing, explainer, there's more to it
```

---

## 7. Playlist

Tamtéž jako 080–082: `spolecnost` a `bezne` hned za 082, a `trans`
(už zapsáno v `playlisty.json`). Po zveřejnění `analytics.py --videa`
a `playlisty.py`. Popis playlistu `trans` vyjmenovává jen 080–082 —
`playlisty.py` ho po založení nemění, případně doplnit ve Studiu.
