# Podklady pro nahrání na YouTube

Ručně psaný zdroj. Časy kapitol odpovídají `work/timing.json` (celkem
**10:28**) — **po každém přegenerování hlasu je potřeba je znovu odvodit**,
protože se posunou.

---

## 1. Titul — A/B/C test

**Video běží od 7. 9. 2026 jako test tří dvojic náhled + titul.** YouTube
Studio umí zadat **tři různé názvy a k nim tři různé miniatury** (ověřeno
uživatelem; `docs/thumbnail-styl.md` to má zastarale jako trojici miniatur
k jednomu titulu).

| var. | náhled | text v obraze | titul |
|---|---|---|---|
| **A** | `thumbnail/dodany-a-osa.png` | `DEATH` / `IS ANYONE THERE?` | **What Does Death Feel Like?** |
| **B** | `thumbnail/dodany-b-zidle.png` | `DEATH` | **Is There Anything After Death?** |
| **C** | `thumbnail/dodany-c-nothing.png` | `NOTHING` | **Can You Imagine Nothing?** |

Základní náhled nahraný přes `nahraj.py` je **varianta B** (nejnižší ztráta
detailu z 31 vydaných náhledů kanálu, 19,0). Základní titul byl při nahrání
`Why You Can't Imagine Your Own Death`; po založení testu ho Studio přepsalo
na variantu A.

**Tři vady tohohle testu, ať se z něj nevyvozuje víc, než unese:**

1. **Mění se dvě věci naráz** — náhled i titul. Když nějaká varianta
   vyhraje, nepůjde říct, čím to bylo.
2. **A se navíc liší i třetí věcí:** jako jediná má v náhledu otázku
   (`IS ANYONE THERE?`), kdežto B a C mají jen jedno slovo.
3. **Objem.** Při zhruba 240 zobrazeních denně a třech variantách vychází
   ~80 zobrazení na variantu a den; při 1% CTR je to necelý proklik denně.
   Rozlišit 1 % od 2 % chce stovky prokliků na variantu.

> **Lokalizované názvy se testu neúčastní.** YouTube je má **per video**,
> ne per variantu, takže všech osm zůstává odvozených z původního
> `Why You Can't Imagine Your Own Death` — divák s českým rozhraním vidí
> pořád „Proč si nedokážeš představit vlastní smrt", ať anglický titul
> ukazuje kteroukoli variantu. Až bude vítěz, stojí za zvážení přepsat
> jich osm podle něj (`lokalizace.py --vse --prepis <kód>`).

Zvažované a zamítnuté tituly:

- `Death Is Not an Experience` — **prozrazuje pointu**, kterou video
  odkládá do 4:46
- `The One Thing Your Brain Cannot Imagine` — nejlepší háček, ale bez
  slova „death" se hůř vyhledá; podle metrik kanálu chodí **73 %
  zhlédnutí z procházení a vyhledávání**

---

## 2. Popis

První dva řádky jsou to jediné, co je vidět před „show more".

```
Try to imagine being dead. Most people picture darkness, or silence, or an endless wait.
Every one of those images quietly smuggles in the one thing that cannot be there: you.

This video goes through the answers one at a time — darkness, silence, an empty room, an
endless wait, eternal sleep, a black screen — and shows that each of them needs somebody
left over to notice it. Then it looks at what actually happens: under general anaesthesia
six hours can pass with almost no subjective time at all, and in the largest audit of its
kind, only about one patient in twenty thousand reported being aware.

Along the way: why your brain is a prediction machine and keeps adding time after the end,
why "I will be dead forever" quietly puts you back on the timeline, and why the eternity
before you were born never bothered you. That last argument is not modern — a Roman poet
wrote it down about two thousand years ago.

And one distinction that turns out to be the most useful of all: being afraid of death is
not the same as being afraid of dying.

Chapters
0:00 What we think it will feel like
1:16 Eternal sleep
1:53 Try to imagine nothing
2:25 Why your brain cannot
3:26 General anaesthesia
4:34 The simplest version of death
5:06 The computer analogy
5:56 So why does it frighten us?
6:40 The time before you were born
7:13 Lucretius
7:52 Dying is not being dead
8:40 The observer keeps coming back
9:05 The symmetry
9:29 A better question

Sources and image credits
De rerum natura, Leiden VLF 30 — the oldest surviving manuscript of Lucretius, 9th century.
Public domain, via Wikimedia Commons.

All other visuals are diagrams drawn for this video, or illustrations generated with
Stable Diffusion XL. The music is generated procedurally.

Subtitles are written for this video, not auto-generated. An American English
audio track is available as a second audio track.
```

> **Jediný archivní snímek je public domain**, takže povinná atribuce
> tu není žádná. `docs/zverejneni.md` říká, že PD snímky vypisovat
> nemusíš — jenže tenhle **nese tvrzení videa** („ten argument je dva
> tisíce let starý"), takže je uvedený schválně, ne z povinnosti.
>
> Kredity jsou **uvnitř bloku**, ne pod ním. U čtyř videí ze šestnácti
> atribuce chyběla přesně proto, že visela jako poznámka pod blokem,
> a uživatel kopíruje jen ten blok.

---

## 3. Kapitoly

Čtrnáct kapitol, první na `00:00`, nejkratší 24 s — YouTube je tím
pádem uzná (potřebuje aspoň tři a každou ≥ 10 s). Časy jsou odvozené
z `work/timing.json`, ne odhadnuté:

| čas | scéna | co začíná |
|---|---|---|
| 0:00 | S01 | otázka a první čtyři odpovědi |
| 1:16 | S12 | věčný spánek |
| 1:53 | S17 | zkus si představit nic |
| 2:25 | S22 | proč to mozek nesvede |
| 3:26 | S29 | celková anestezie |
| 4:34 | S39 | nejjednodušší verze smrti |
| 5:06 | S44 | počítačová analogie |
| 5:56 | S50 | proč nás to tedy děsí |
| 6:40 | S55 | doba před narozením |
| 7:13 | S60 | Lucretius |
| 7:52 | S65 | umírání versus být mrtvý |
| 8:40 | S71 | pozorovatel se vrací |
| 9:05 | S75 | symetrie |
| 9:29 | S77 | lepší otázka |

---

## 4. Nastavení při nahrávání

| | |
|---|---|
| video | `render/final-en.mp4` (master, **ne** draft) |
| náhled | `render/thumbnail.jpg` — 1280×720, 74 kB, koncept `c2-prazdna-zidle` |
| **jazyk videa** | **`en-gb` — nastavit NAPŘED**, jinak zůstane dlaždice Titulky zašedlá |
| titulky | `subtitles/*.srt`, devět jazyků |
| kategorie | Science & Technology |
| pro děti | ne |
| **byla použita AI** | **ne** — viz níž. `tools/nahraj.py` posílá `containsSyntheticMedia: false` |
| **Osvědčení o zproštění** | **zaškrtnout RUČNĚ ve Studiu** („obsah se nikdy nevysílal v televizi v USA"). Data API na to pole nemá |
| viditelnost | nahrát jako **neveřejné** a podívat se na to v přehrávači |

### Proč „ne" u otázky na AI

Rozhoduje **fotorealističnost, ne použití AI**
([pravidla](https://support.google.com/youtube/answer/14328491)):

- **79 scén z 83 jsou diagramy kreslené kódem**, tedy ne fotorealismus
- tři SDXL scény (S20, S29, S53) jsou díky kotvě stylu **malované
  ilustrace**; kotva výslovně vylučuje fotorealismus i konkrétní místa
- jediný archivní snímek je **fotografie rukopisu**, upravená jen barevně
  — *„color adjustment or lighting filters"* je výslovná výjimka
- hudba je **procedurální** (sinusovky a šum v numpy), ne z generativního
  modelu
- video nezobrazuje žádné konkrétní skutečné místo ani událost

> **Téma je citlivé, obrazy ne.** Ve videu není lebka, hrob, mrtvola ani
> nemocniční scéna s krví — negativní prompt to blokuje a archivní fotka
> operačního sálu byla z toho důvodu zamítnuta (viz `notes.md`).

---

## 5. Tagy

```
death, consciousness, philosophy of mind, what happens when you die, anaesthesia,
general anesthesia, awareness under anaesthesia, Lucretius, De rerum natura,
Epicurus, symmetry argument, fear of death, mortality, neuroscience, predictive brain,
subjective time, personal identity, science explained
```

---

## 6. Kontrola před nahráním

```bash
ffprobe -v error -show_entries format=duration -of default=nw=1:nk=1 \
        videos/031-what-does-death-feel-like/render/final-en.mp4
ffmpeg -v error -i videos/031-what-does-death-feel-like/render/final-en.mp4 -f null -
python tools/thumb_check.py videos/031-what-does-death-feel-like
python videos/031-what-does-death-feel-like/kontrola_factcheck.py
```

Naměřeno 7. 9. 2026 na hotovém masteru: **628,48 s** (10:28,5),
1920×1080, 25 fps, 15 712 snímků, **45,0 MB**. Dekóduje se celý
**beze slova** (`ffmpeg -v error -f null -`, návratový kód 0) — samotné
`ffprobe` by přečetlo délku z kontejneru i u rozsypaného streamu.
Hlasitost **−14,0 LUFS**, true peak **−1,3 dBFS**.

Titulky ve všech devíti jazycích končí na 627,26 s, tedy uvnitř videa.

Po zveřejnění zapiš odkaz do **`Témata.ods`**, řádek „Smrt a vědecký
pohled" — stav videí je tam a nikde jinde.
