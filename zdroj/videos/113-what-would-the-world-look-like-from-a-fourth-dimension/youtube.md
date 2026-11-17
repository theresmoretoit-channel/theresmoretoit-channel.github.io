# YouTube — 113 „What If Space Had a Fourth Dimension?“

Stav: **hotovo, naplánováno ke zveřejnění** (https://www.youtube.com/watch?v=dXqHZlOilZY, nahráno 2026-10-17). Přes API metadata, náhled, 13 lokalizací a titulky en, cs, sv, es; po vyčerpání kvóty zbylých 11 stop, playlist, americkou stopu a závěrečnou obrazovku naklikal uživatel ve Studiu. Stav zveřejnění je v `Témata.ods`.

| | |
|---|---|
| ID videa | `dXqHZlOilZY` |
| master | ✅ `render/final-en-113.mp4` (9:32, 1920×1080, 35 MB, render 2026-10-17 na .207, `ffmpeg -v error` čistý; s hudbou, viz `notes.md`) |
| náhled | ✅ `render/thumbnail.jpg` (4D SPACE / HOW DID IT GET OUT?) — `thumbnail/PUVOD.md` |
| nastavení, popis, tagy | podklady níž |
| lokalizace | `youtube-preklady.md`, 13 jazyků, prošlo Codexem (12 oprav), ✅ nahráno |
| titulky | `subtitles/*.srt`, 14 jazyků + `en-US`, překlady prošly Codexem, ✅ en cs sv es přes API, zbylých 11 ručně ve Studiu |
| americká stopa | ✅ `render/audio-en-US.m4a`, ručně ve Studiu |
| závěrečná obrazovka | ✅ ručně ve Studiu |
| karta | žádná (viz níž) |
| playlist | ✅ `fyzika`, na konec (ručně) |

**Co musí uživatel naklikat sám:** nahrát MP4 ve Studiu (průvodce vyřídí
prohlášení o AI a osvědčení o zproštění), závěrečnou obrazovku
a americkou audiostopu (`render/audio-en-US.m4a`).

Stopáž 9:32 (`work/timing.json` total 572,4 s).

> Kdyby se znovu pouštěl `tts.py`, přepočítej kapitoly tady
> i v `youtube-preklady.md` a přegeneruj `en-US` přes `us_stopa.py`.

Pořadí podle CENY (`docs/zverejneni.md`):

```bash
V=videos/113-what-would-the-world-look-like-from-a-fourth-dimension
python tools/nahraj.py $V --k-videu=<ID> --bez-titulku    # 100
python tools/analytics.py --videa                         #   1  ← nutné
python tools/lokalizace.py $V                             #  50
python tools/titulky.py $V --smaz-asr                     # 150  ← před titulky
python tools/titulky.py $V                                # 400×15
# zbytek po kvótě (2026-10-17 prošly en cs sv es):
python tools/titulky.py $V --jen pt-BR,de,fr,it,pl,id,tr,uk,vi,fi,en-US
python tools/playlisty.py                                 #  50
# úklid, až je MP4 na YouTube:
rm $V/render/draft*.mp4
ssh vrana@192.168.0.207 'rm -rf /home/vrana/temp/render-113-what-would-the-world-look-like-from-a-fourth-dimension'
```

---

## 1. Titul

```
What If Space Had a Fourth Dimension?
```

> Wh-otázka, 37 znaků. `project.json` má pracovní titul *What Would the
> World Look Like From a Fourth Spatial Dimension?* (63 znaků), zvolen
> kratší (2026-10-17). Odpověď (velký čtvrtý rozměr by rozbil oběžné
> dráhy, malý nebo skrytý je otevřená otázka) titul neprozrazuje.

---

## 2. Popis

```
Imagine you're at home. The door is locked, the windows are shut, and suddenly someone is standing in your living room. They didn't pick the lock or break through a wall. They took a route you can't take: one more direction of space. Not time. A real direction, like left, forward or up.

In 1884 a London headmaster, Edwin Abbott, worked out how to think about it in Flatland, a book narrated by a square who has no idea that "up" exists. Using the same trick, we look at what a four-dimensional being could do with a locked safe, what a four-dimensional ball or cube would look like passing through your room, and why August Möbius noticed in 1827 that a fourth dimension could turn a left shoe into a right one. H. G. Wells and Liu Cixin turned it into fiction. But there's a catch, and it says a lot about whether such a direction could exist, and where it might be hiding.

Time as the fourth dimension is a different question: What Is Time, Actually? https://www.youtube.com/watch?v=LP_MJkgG4vA

Sources: E. A. Abbott, Flatland (1884); A. F. Möbius, Der barycentrische Calcul (1827); H. G. Wells, The Plattner Story (1896); Liu Cixin, Death's End (2010); P. Ehrenfest, Proc. Amsterdam Acad. 20 (1917); F. R. Tangherlini, Nuovo Cimento 27, 636 (1963); T. Kaluza, Sitzungsber. Preuss. Akad. Wiss. (1921); O. Klein, Z. Phys. 37 (1926); Arkani-Hamed, Dimopoulos & Dvali, Phys. Lett. B 429, 263 (1998; arXiv hep-ph/9803315); Lee et al., Phys. Rev. Lett. 124, 101101 (2020); ATLAS and CMS searches for missing energy at the LHC.

Subtitles are written for this video, not auto-generated. An American English audio track is available as a second audio track.

CHAPTERS
00:00 Someone inside a locked room
00:27 Flatland, 1884
02:03 What could a 4D being do?
02:20 Liu Cixin's Death's End
02:45 A 4D object passing through our world
03:29 Turning a left shoe into a right shoe
04:13 H. G. Wells and The Plattner Story
04:32 The catch
05:30 Ehrenfest and the planets
06:42 Why it's a clue
07:17 Curled up too small to see
07:45 Stuck to our three dimensions
08:08 Testing it
08:48 Where we are now

IMAGE CREDITS
Flatland, illustration from the first edition (1884); August Ferdinand Möbius — Adolf Neumann; H. G. Wells; Paul Ehrenfest
via Wikimedia Commons, all in the public domain.
```

> **Blok se kopíruje CELÝ** (`docs/zverejneni.md`). Archivní snímky jsou
> čtyři (S04, S24, S26, S36), všechny public domain (`CREDITS.md`),
> takže atribuce povinná není; jsou vypsané jen proto, že jich je málo.
>
> **Pointa se neprozrazuje.** Popis končí na *„there's a catch"*, nejmenuje
> gravitaci, oběžné dráhy ani Kaluzu–Kleina a ADD. Kapitoly jsou
> opatrnější než u 111: *„The catch"*, *„Ehrenfest and the planets"*,
> *„Testing it"*.
>
> Kapitoly ze scén S01, S04, S12, S14, S17, S21, S26, S28, S36, S43, S47,
> S50, S53, S56 (`work/timing.json`, zaokrouhleno dolů). Nejkratší 17 s
> (S12 → S14), všechny ≥ 10 s, první na 00:00. Výzva k odběru S11b (1:56)
> leží v kapitole „Flatland, 1884“.
>
> Zdroje podle `factcheck.md` (zvláštní sekce „Zdroje“ tam není, citace
> jsou u jednotlivých scén). *Death's End* vyšel čínsky 2010. Čísla
> v popisu (1884, 1827) jsou tatáž jako ve scénáři.
>
> Odkaz na **008** a ne na 040: úvod 113 říká *„Not time."* a 008 je
> o čase jako rozměru přímo.

---

## 3. Náhled

✅ `render/thumbnail.jpg` — 4D SPACE / HOW DID IT GET OUT? (zamčený sejf
a balík bankovek na něm). Hotový obrázek od uživatele (ChatGPT, zadání B),
jen zmenšený; původ a otisk v `thumbnail/PUVOD.md`, zadání
v `thumbnail/ZADANI.md`.

---

## 4. Titulky

`subtitles/*.srt`, 14 jazyků + `en-US`. Jazyk videa **`en-gb`** (hlas
`bf_emma`) se musí nastavit dřív, než se nahrají titulkové stopy.
Nahrávají se až po zapracování nálezů Codexu (hotovo 2026-10-16).

---

## 5. Nastavení

| | |
|---|---|
| kategorie | **Science & Technology** (28) — posílá `nahraj.py` napevno |
| jazyk videa | `en-gb` |
| licence | standardní |
| pro děti | **ne** |
| komentáře | zapnuté |
| **byla použita AI** | **ne**. 56 scén je kreslených kódem, 4 archivní snímky (titulní ilustrace *Flatland*, portréty Möbia, Wellse a Ehrenfesta) jsou jen barevně upravené. Jediná SDXL scéna (S44, Země z vesmíru) je malovaná ilustrace podle kotvy stylu, ne fotorealismus ani konkrétní událost. Hudba je procedurální, hlas není klon. |

### Závěrečná obrazovka

Od **9:12** (posledních 20 s), tedy S57–S59. `zaver_check` u nich hlásí
volnou **horní polovinu**, prvky patří **nahoru**. Jako dlaždici
dalšího videa doporučuju **008 *What Is Time, Actually?***, dokud
nevyjde 2. díl (*Why Haven't We Found a Fourth Spatial Dimension?*),
na který míří S59 *„That's where we're going next."* Pak dlaždici
vyměnit.

### Karta

Žádná. Jediné přirozené místo je S03 *„Not time."* (0:18), a karta
v první půlminutě by posílala diváky pryč v okně, kde se rozhoduje,
jestli zůstanou. Odkaz na 008 je v popisu.

---

## 6. Tagy

```
fourth dimension, 4th dimension, four dimensional space, tesseract,
hypercube, flatland, edwin abbott, liu cixin, death's end,
three body problem, h g wells, extra dimensions, kaluza klein,
gravity, physics explainer, science explainer, there's more to it
```

---

## 7. Playlist

`fyzika` (*Physics That Sounds Simple Until You Ask*), na konec. Leží
tam i 008 a 040 (čas jako čtvrtý rozměr).
