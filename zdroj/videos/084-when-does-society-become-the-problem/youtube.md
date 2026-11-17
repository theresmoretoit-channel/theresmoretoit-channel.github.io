# YouTube — 084 „When Does Society Become the Problem?"

Stav: **nahráno 2026-10-25** (`render/final-en-084.mp4`, 794,1 s, render .207, kopie na .207 i lokální draft smazány)

| | |
|---|---|
| ID videa | `S00-d39ze3g` — https://youtu.be/S00-d39ze3g |
| nastavení, popis, tagy | ✅ 2026-10-25 `nahraj.py --k-videu --bez-titulku` |
| náhled | ✅ C1 (ChatGPT), `thumbnail/PUVOD.md` |
| lokalizace | ✅ 13 jazyků |
| titulky | ✅ API: všech 15 stop (automatický přepis nebyl) |
| playlist | ✅ `spolecnost`, `bezne` (za 083), `trans` |
| ručně ve Studiu | ✅ MP4 (průvodce: AI, zproštění); ⏳ závěrečná obrazovka (playlist `trans`), americká audiostopa |

**Až vyjde 084:** u 083 vyměnit dlaždici závěrečné obrazovky z 082 na 084
(`083-*/youtube.md`). Po nahrání smazat kopii na .207 a `render/draft-en.mp4`.

Soubor k nahrání: `render/final-en-084.mp4` (stopáž 13:14, `work/timing.json`
total 794,08 s). Americká stopa: `render/audio-en-US.m4a`.

Pořadí podle CENY (`docs/zverejneni.md`):

```bash
V=videos/084-when-does-society-become-the-problem
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
When Does Society Become the Problem?
```

> wh-otázka („When…"), 37 znaků. Neprozrazuje odpověď — video ji skládá
> (dysforie vs. stres menšiny, čísla a jejich meze, přijetí, odpovědnost),
> titul se jen ptá. Je to otázka, kterou ohlásil konec 083 (S91).

---

## 2. Popis

```
Imagine waking up tomorrow and discovering that the way the world sees you has become a problem. Not because you have hurt anyone, but because you don't fit the expectations of the people around you.

This video looks at what research says about suicide among transgender people, and what it can and cannot tell us. A Danish study that followed an entire national population over four decades. The difference between gender dysphoria and transgender identity, and how ICD-11 and the American psychiatric manual treat each. Minority stress, and how hundreds of small experiences can add up. A large survey of LGBTQ+ young people in the United States, and what it found among those who felt accepted. And the question of what society is responsible for, when we cannot remove every source of someone's pain, but can choose not to add to it.

This is the fifth and final video in a series about transgender people. The earlier ones asked why there suddenly seem to be so many trans people, how you know you're trans, why trans people change their bodies, and why it is so hard to be trans.

IF YOU'RE STRUGGLING
You don't have to go through it alone. These services are free and confidential:
Find A Helpline, support in more than 175 countries: https://findahelpline.com
United States and Canada: call or text 988
The Trevor Project, for LGBTQ+ young people in the US: 1-866-488-7386, text START to 678-678, or chat at https://www.thetrevorproject.org/get-help/
Trans Lifeline, peer support run by trans people: US (877) 565-8860, Canada (877) 330-6366
UK and Ireland: Samaritans, 116 123
If you are in immediate danger, call your local emergency number.

Subtitles are written for this video, not auto-generated. An American English audio track is available as a second audio track.

CHAPTERS
00:00 What if the world saw you as a problem?
01:38 When your own body feels wrong
03:43 The world adds its own weight
05:39 The numbers behind the pain
08:10 What happens when people are accepted?
09:50 Who is responsible?
11:11 The mirror
```

> **Blok se kopíruje CELÝ** (`docs/zverejneni.md`). Video nemá archivní
> snímek (`sources.json` neexistuje), takže sekce IMAGE CREDITS odpadá.
>
> **Linky pomoci jsou povinné, ne ozdoba:** S60 slibuje *„links to free,
> confidential support services in the description, including options in
> many countries"*. Ověřeno 2026-10-25 na stránkách služeb: Find A Helpline
> (ThroughLine, 175+ zemí, zdarma, důvěrné); Trevor Project 1-866-488-7386,
> SMS START na 678-678, chat, 24/7, zdarma a důvěrně; Trans Lifeline
> US (877) 565-8860, Kanada (877) 330-6366, operátoři jsou trans lidé,
> **jen po–pá 13–21 ET**, proto není mezi „24/7"; 988 (USA a od 2023 i Kanada),
> Samaritans 116 123 (UK a Irsko). Nadpis je česky v lokalizacích přeložený,
> čísla a odkazy zůstávají.
>
> Kapitoly jsou kapitolové desky S14, S27, S43, S61, S74, S85
> (`work/timing.json` masteru, celkem 794,08 s, časy zaokrouhlené dolů).
> Kapitola 00:00 desku nemá a nese otázku S01. Nejkratší kapitola je 78 s
> (S74–S85). **Po každém dalším běhu `tts.py` časy přepočítej** — a stejně
> tak v `youtube-preklady.md`.
>
> Popis drží míru jistoty scénáře: čísla ze studií neuvádí (dánská studie
> má jen dvanáct úmrtí a interval 2–6×, Trevor je online průzkum, ne
> náhodný vzorek), přijetí „what it found among those who felt accepted", ne „what it prevents" —
> S68 *„correlations, not proof"*.

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
| komentáře | zapnuté — **téma je konfliktní a týká se sebevraždy, počítej s moderací** |
| **byla použita AI** | **ne** — 98 scén kreslených kódem, 3 SDXL scény (S32, S62, S87) v malované kotvě stylu (*painterly documentary illustration*, ne fotorealismus), žádná archivní fotka, hudba procedurální, hlas není klon skutečné osoby. Výzva k odběru je kresba (ikony Lucide), ne AI |

> YouTube u videí o sebevraždě může sám zobrazit panel s linkou pomoci;
> to je v pořádku a s popisem se to nebije. Video nic nepopisuje
> (metody, podrobnosti), takže věkové omezení se nečeká.

### Závěrečná obrazovka

`zaver_check.py`: S97–S100 (posledních 20 s) mají dole titulek — dlaždici
i kolečko odběru dej do **horní** poloviny (u S100 je horní pás nad rámem
zrcadla volný schválně). Série tímhle dílem končí, takže jako dlaždici dej
**playlist `trans`** (nebo 080 jako začátek série), ne „další díl".

---

## 6. Tagy

```
transgender, trans people, gender dysphoria, minority stress,
mental health, suicide prevention, acceptance, discrimination,
ICD-11, Trevor Project, explainer, there's more to it
```

---

## 7. Playlist

Tamtéž jako 080–083: `spolecnost` a `bezne` hned za 083, a `trans`
(zapsáno v `playlisty.json`). Po zveřejnění `analytics.py --videa`
a `playlisty.py`. Popis playlistu `trans` vyjmenovává jen 080–082 —
`playlisty.py` ho po založení nemění; teď, když je série celá, ho stojí
za to doplnit ve Studiu.
