# YouTube — 163 „Why Do the Amish Use Chainsaws but Avoid Cars?“

Stav: **MP4 nahráno ručně ve Studiu** (2026-11-21), náhled hotový. Master `render/final-en-163.mp4` (207, 1920×1080, 588,52 s, ověřen dekódováním).

| | |
|---|---|
| ID videa | `EI5XvLhaPas` (https://www.youtube.com/watch?v=EI5XvLhaPas) |
| master | `render/final-en-163.mp4` (207, plné rozlišení) |
| náhled | `render/thumbnail.jpg` z `thumbnail/c1-chatgpt.png` (C1, ChatGPT), viz `thumbnail/PUVOD.md` |
| nastavení, popis, tagy | podklady níž |
| lokalizace | `youtube-preklady.md`, 13 jazyků |
| titulky | `subtitles/<kód>.srt`, 14 jazyků + `en-US`; Codex na všech 13 překladech, nálezy zapracované |
| americká stopa | `render/audio-en-US.m4a` (`af_heart`, speed 0,9466), ručně ve Studiu |
| závěrečná obrazovka | S47–S48, **horní polovina** (viz níž) |
| karty | žádné |
| playlist | `lide` |

**Co musí uživatel naklikat sám:** závěrečnou obrazovku, americkou audiostopu
(`render/audio-en-US.m4a`) a osvědčení o zproštění, pokud ho nevyřídil průvodce nahráním.

Stopáž 9:48 (`work/timing.json` total 588,51 s).

> Kdyby se znovu pouštěl `tts.py`, přepočítej kapitoly tady i v `youtube-preklady.md`
> a přegeneruj `en-US` přes `us_stopa.py`.

Pořadí podle CENY (`docs/zverejneni.md`):

```bash
V=videos/163-why-do-the-amish-use-chainsaws-but-avoid-cars
python tools/nahraj.py $V --k-videu=EI5XvLhaPas --bez-titulku   # 100
python tools/analytics.py --videa                        #   1  ← nutné
python tools/lokalizace.py $V                            #  50
python tools/titulky.py $V --smaz-asr                    # 150  ← před titulky
python tools/titulky.py $V                               # 400×N
python tools/playlisty.py                                #  50
# úklid, až je MP4 na YouTube:
rm $V/render/draft*.mp4
```

---

## 1. Titul

```
Why Do the Amish Use Chainsaws but Avoid Cars?
```

> Wh-otázka, 46 znaků, shodná s `project.json`. Paradox je v titulu, odpověď (co technologie
> udělá s komunitou) ne.

---

## 2. Popis

```
Many Amish communities won't let their members own a car, and most refuse to connect to the public electricity grid. Yet you can find Amish workshops full of pneumatic tools, generators and chainsaws. Some families had telephones at home over a century ago, then banned them, then let them back in, but only into a wooden booth outside. So are the Amish really against technology?

This video looks at the question they keep asking instead: what will this technology do to our community? It covers cars, electricity, farm machinery, the telephone and today's mobile phones, then medicine, insurance, Social Security and the law. Then Rumspringa, the years when young Amish people get to try the outside world, and why most of them stay. And finally what holds the whole system together, and what the rest of us might borrow from it.

Sources: Young Center for Anabaptist and Pietist Studies, Elizabethtown College (Amish Studies: FAQ, Technology, Regulations, Language, Health, Government, Mutual Aid, Rumspringa, Population Growth, Amish Population 2026); Wisconsin v. Yoder, 406 U.S. 205 (1972); Diane Zimmerman Umble, Holding the Line: The Telephone in Old Order Mennonite and Amish Life (1996); Howard Rheingold, "Look Who's Talking", Wired (1999); Jameson Wetmore, "Amish Technology: Reinforcing Values and Building Community", IEEE Technology and Society Magazine (2007); Wenger et al., Pediatrics (2011); Scott et al., Vaccine (2021); Donald Kraybill interviews (NPR 2013, Michigan Public 2013).

Subtitles are written for this video, not auto-generated. An American English audio track is available as a second audio track.

Full transcript, sources and translations: https://theresmoretoit-channel.github.io/videos/why-do-the-amish-use-chainsaws-but-avoid-cars/

CHAPTERS
00:00 Life without a car
00:43 Who the Amish are
01:17 The Ordnung
01:39 Cars
02:37 Electricity
03:13 Machines and chainsaws
03:52 The telephone
04:35 Mobile phones
04:49 Medicine, insurance and the law
05:54 Rumspringa
06:55 Why so many stay
07:42 Not a utopia
08:17 Take away the religion
08:52 What we could borrow

IMAGE CREDITS
Amish Buggy 2018-11-06 962 — Chris Light, CC BY-SA 4.0
via Wikimedia Commons
Licence: creativecommons.org/licenses/by-sa/4.0/
All other archive images are in the public domain.
```

> **Blok se kopíruje CELÝ** (`docs/zverejneni.md`). Kredity ze `sources.json`: jediný snímek
> s povinnou atribucí je S11 (Chris Light, CC BY-SA 4.0). S05 (Luyken), S18 (Highsmith)
> a S45 (Rlevse) jsou public domain.
>
> **Pointa se neprozrazuje:** popis říká, na co se amišové ptají (to video říká už v S04),
> ale ne, že je drží pohromadě náboženství (S39–S42), ani kolik mladých zůstane (S30).
>
> Kapitoly ze scén S01, S05, S07, S09, S15, S18, S21, S24a, S24b, S25, S31, S36, S39, S43
> (`work/timing.json`, zaokrouhleno dolů). První na 00:00, všechny ≥ 10 s (nejkratší
> S24a → S24b 14 s; poslední S43 → konec 56 s). Otázka do komentářů (S48) vlastní kapitolu nemá.
>
> **Zdroje:** primární a hlavní sekundární z `factcheck.md`. Odkaz na web vznikne až po
> `tools/web_publikuj.sh` (viz `docs/web.md`).

---

## 3. Náhled

Koncept C1 (`AMISH` / `ANTI-TECH?`), `render/thumbnail.jpg`. Nahraje ho `nahraj.py`.

---

## 4. Titulky

`subtitles/<kód>.srt` pro 14 jazyků a `en-US`.
Jazyk videa **`en-gb`** (hlas `bf_emma`) nastaví `nahraj.py` dřív, než se nahrají titulkové stopy.

---

## 5. Nastavení

| | |
|---|---|
| kategorie | **Science & Technology** (28), posílá `nahraj.py` napevno |
| jazyk videa | `en-gb` |
| licence | standardní |
| pro děti | **ne** |
| komentáře | zapnuté (S48 je otázka do komentářů) |
| **byla použita AI** | **ne**. 48 z 54 scén je kreslených kódem, čtyři archivní snímky z Commons (S05 rytina, S11, S18, S45) jsou upravené jen barevně a ořezem. S27 (cesta z farmy k městu) a S36 (idylická pohlednice farmy) jsou malované ilustrace z SDXL, obecné scény, ne skutečné místo ani událost. Hudba je procedurální, hlas není klon skutečné osoby. |

### Závěrečná obrazovka

Od **9:48 − 20 s ≈ 9:28** (začátek S47 je 9:25). `zaver_check` hlásí S47–S48 OK, spodní
rohy jsou pod titulky. **Dlaždici i odběr dej do HORNÍ poloviny.**
Dlaždici nech na „nejlepší pro diváka“, kanál nemá video, na které by tohle přímo navazovalo.

---

## 6. Tagy

```
amish, amish technology, ordnung, rumspringa, pennsylvania dutch, anabaptist, amish cars,
amish electricity, amish telephone, social security exemption, wisconsin v yoder,
technology and community, simple living, there's more to it
```

---

## 7. Playlist

**`lide`** (*„Habits, hobbies and beliefs that look irrational from the outside and make
perfect sense from the inside“*). Dopsat slug do `playlisty.json`, `analytics.py --videa`,
`playlisty.py --jen lide`.
