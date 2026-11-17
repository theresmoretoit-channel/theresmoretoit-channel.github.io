# YouTube — 135 „Where Did the Idea of Hell Come From?“

Stav: **nahráno jako soukromé 2026-11-06** (MP4 ručně; metadata, náhled, lokalizace, 15 titulků a playlist přes API týž den). Plán zveřejnění, americká stopa a závěrečná obrazovka ručně ve Studiu. Stav zveřejnění je v `Témata.fods`.

| | |
|---|---|
| ID videa | `V3_fJLasvv4` — https://www.youtube.com/watch?v=V3_fJLasvv4 |
| master | `render/final-en-135.mp4` (render na .207) |
| náhled | ✅ `render/thumbnail.jpg` — koncept C1 (`thumbnail/PUVOD.md`) |
| nastavení, popis, tagy | podklady níž |
| lokalizace | `youtube-preklady.md`, 13 jazyků |
| titulky | `subtitles/*.srt`, 14 jazyků + `en-US`, Codex zapracován, nahráno |
| americká stopa | `render/audio-en-US.m4a`, ručně ve Studiu |
| závěrečná obrazovka | S108–S110, **horní polovina** (viz níž) |
| karty | žádné |
| playlist | `lide` (*Why We Do What We Do*), hned za 085 |

**Co musí uživatel naklikat sám:** závěrečnou obrazovku, americkou audiostopu
(`render/audio-en-US.m4a`) a osvědčení o zproštění, pokud ho nevyřídil průvodce nahráním.

Stopáž 11:53 (`work/timing.json` total 713,3 s).

> Kdyby se znovu pouštěl `tts.py`, přepočítej kapitoly tady i v `youtube-preklady.md`
> a přegeneruj `en-US` přes `us_stopa.py`. S11 má hotový zvuk a pauzu 0,715 s, které drží časovou osu.

Pořadí podle CENY (`docs/zverejneni.md`):

```bash
V=videos/135-where-did-the-idea-of-hell-come-from
python tools/nahraj.py $V --k-videu=V3_fJLasvv4 --bez-titulku   # 100
python tools/analytics.py --videa                        #   1  ← nutné
python tools/lokalizace.py $V                            #  50
python tools/titulky.py $V --smaz-asr                    # 150  ← před titulky
python tools/titulky.py $V                               # 400×15
python tools/playlisty.py                                #  50
# úklid, až je MP4 na YouTube:
rm $V/render/draft*.mp4
ssh vrana@192.168.0.207 'rm -rf /home/vrana/temp/render-135-where-did-the-idea-of-hell-come-from'
```

---

## 1. Titul

```
Where Did the Idea of Hell Come From?
```

> Wh-otázka, 37 znaků, shodná s `project.json`. Odpověď (S106–S107) titul neprozrazuje.

---

## 2. Popis

```
Hell has an address. It's a valley just below the walls of old Jerusalem. You can walk through it today, and in 1987 Bob Dylan played a concert there. So how did that valley become a place of fire for the wicked?

The older books of the Bible don't have a hell at all. This video follows how the idea came together over thousands of years: a court in Egypt, a sentence in Plato, a motive in Judea, a valley outside Jerusalem, and pictures from a book that came very close to being in the Bible. It doesn't tell you whether hell is real. No historian can.

Sources: King James Bible (Deuteronomy, 1 Samuel, Ecclesiastes, Isaiah, Jeremiah, Daniel, 2 Maccabees, Mark, Revelation); 1 Enoch; Plato, Gorgias; Book of the Dead, spells 30 and 125; Gilgamesh, Enkidu and the Netherworld; Apocalypse of Peter; Muratorian Fragment; Apocalypse of Paul; Dante, Inferno XIX; John Paul II, General Audience, 28 July 1999; Pew Research Center, 2025.

Subtitles are written for this video, not auto-generated. An American English audio track is available as a second audio track.

CHAPTERS
00:00 Hell has an address
00:44 No hell at all
01:54 It had to be built
02:16 Part one: a court
03:21 Part two: a sentence
04:03 Part three: a motive
05:17 When the deal broke
06:16 Part four: the location
07:18 More than a valley
07:54 Where the word comes from
08:23 Part five: the pictures
09:38 Who were these hells built for?
10:16 A list that doesn't stop
10:42 Rather than a place
11:16 So where did it come from?
11:37 A question for you

IMAGE CREDITS
Jerusalem-Hinnom-Kidron-Old-City-323 — Bukvoed, CC BY 4.0
Sultan's Pool — RonAlmog, CC BY 2.0
The Newly Discovered Tablet V of the Epic of Gilgamesh — Osama Shukir Muhammed Amin FRCP(Glasg), CC BY-SA 4.0
Archelaos, Stater, 413-399 BC — CNG, CC BY-SA 2.5
Antiochos IV, silver tetradrachm — ArchaiOptix, CC BY-SA 4.0
Giotto, Boniface VIII proclaims the Jubilee of 1300, fragment — Sailko, CC BY 3.0
Heart Scarab — Museo Egizio, CC0
via Wikimedia Commons
Licences: creativecommons.org/licenses/by/4.0, /by/3.0, /by/2.0, /by-sa/4.0, /by-sa/2.5
All other archive images are in the public domain.
```

> **Blok se kopíruje CELÝ** (`docs/zverejneni.md`). CC BY* ze `sources.json`: S03 a S104 (Bukvoed), S04, S16, S38, S54, S88; S30 je CC0.
>
> **Pointa se neprozrazuje:** popis neříká *somebody got away with it* (S52, S92–S93, S107). Kapitola 09:38 je proto otázka.
>
> Kapitoly ze scén S01, S09, S20, S23, S34, S40, S53, S62, S69, S74, S77, S90, S96, S100, S105, S108 (`work/timing.json`, zaokrouhleno dolů).
> První na 00:00, všechny ≥ 10 s (nejkratší S105 → S108, 21 s). Výzvy k odběru (za S19 a S95) leží uvnitř kapitol.
>
> **Zdroje:** jen to, co jsem četl. Faulkner a Taylor u ceny svitku (S31) a Hornung u S33 v `factcheck.md` přes druhou ruku, proto tu nejsou.
> Wikipedia je ve `factcheck.md`, do popisu nepatří.

---

## 3. Náhled

`render/thumbnail.jpg` (1280×720): červený špendlík v tmavém kameni, *HELL* / *WHO PUT IT THERE?*. Koncept C1 z `thumbnail/ZADANI.md`, původ a otisky v `thumbnail/PUVOD.md`.

---

## 4. Titulky

`subtitles/*.srt`, 14 jazyků + `en-US`. Jazyk videa **`en-gb`** (hlas `bf_emma`) se musí nastavit dřív,
než se nahrají titulkové stopy.

---

## 5. Nastavení

| | |
|---|---|
| kategorie | **Science & Technology** (28) — posílá `nahraj.py` napevno |
| jazyk videa | `en-gb` |
| licence | standardní |
| pro děti | **ne** |
| komentáře | zapnuté (S108–S110 je otázka do komentářů) |
| **byla použita AI** | **ne**. Většina scén je kreslená kódem, archivní snímky jsou upravené jen barevně a ořezem, S45 a S98 ze SDXL jsou malované ilustrace, ne fotorealismus. Hudba je procedurální, hlas není klon skutečné osoby. |

### Závěrečná obrazovka

Od **11:33** (posledních 20 s), tedy S107–S110. `zaver_check` hlásí v dolních rozích titulek.
**Dlaždici i odběr dej do HORNÍ poloviny.** Jako dlaždici navrhuju **068 *Why Do People Still Believe in God?***,
druhou nechat na „nejlepší pro diváka".

---

## 6. Tagy

```
where did hell come from, history of hell, idea of hell, gehenna, valley of hinnom, sheol,
book of the dead, weighing of the heart, plato gorgias, book of enoch, book of daniel,
apocalypse of peter, dante inferno, king james bible, is hell real, religion history,
there's more to it
```

---

## 7. Playlist

**`lide`** (*Why We Do What We Do*), za 085 (*If God Exists, What Is God?*), kde leží 068, 073 a 085 k témuž okruhu.
Pinterest shortů: `Psychology & Human Behavior`. Zapsat do `playlisty.json` při nahrání;
`playlisty.py` ho přeskočí, dokud video není v `analytics/videa.json`.
