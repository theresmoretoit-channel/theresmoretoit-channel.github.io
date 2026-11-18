# YouTube — 079 „Why Is This 90-Year-Old Airplane Still Flying?"

Stav: **připraveno k nahrání** — master se renderuje, náhled ještě není vybraný.

| | |
|---|---|
| ID videa | — (doplní se po ručním nahrání MP4) |
| nastavení, popis, tagy | čeká |
| náhled | čeká na výběr konceptu (`thumbnail/KONCEPTY.md`, doporučen C1) |
| lokalizace | čeká — **až po Codexu** a zapracování nálezů |
| automatický přepis | čeká (`--smaz-asr` PŘED titulky) |
| titulky | čeká — 14 jazyků + `en-US`, **až po Codexu** |
| playlist | čeká — navrženo `legacy` |
| závěrečná obrazovka, americká stopa | čeká, ručně ve Studiu |

**Co musí uživatel naklikat sám:** nahrát MP4 ve Studiu (průvodce vyřídí
prohlášení o AI a osvědčení o zproštění), závěrečnou obrazovku a americkou
audiostopu (`render/audio-en-US.m4a`).

Soubor k nahrání: `render/final-en-079.mp4` (stopáž 9:19, `work/timing.json`
total 558,7 s).

Pořadí podle CENY (`docs/zverejneni.md`):

```bash
V=videos/079-why-is-this-90-year-old-airplane-still-flying
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
Why Is This 90-Year-Old Airplane Still Flying?
```

> wh-otázka („Why…"), 46 znaků. Neprozrazuje odpověď (žádné jediné
> tajemství: dobré ve všem naráz, shovívavé, opravitelné v terénu,
> válka z něj udělala ekosystém). „90-year-old" je věk **konstrukce**
> (první let 17. 12. 1935); konkrétní létající kusy jsou 80+ let — ve
> scénáři i popisu rozlišeno, rozhodl uživatel (`notes.md`, v0.2).
> `Airplane`, ne `aeroplane` — rozhodnutí uživatele, drží to i scénář.

---

## 2. Popis

```
The Douglas DC-3 first flew in 1935. More than ninety years later, some of them are still at work, hauling cargo and supplies to remote places. Most airliners are retired after about twenty-five years. So what did Douglas get so right?

This video goes back to the days when airlines struggled to make money carrying passengers alone, and looks at what the DC-3 changed. It follows what pilots say about the way it flies, what a mechanic can do with it on a gravel strip hundreds of kilometres from the nearest hangar, and what the Second World War did to its future.

It also asks why we aren't still flying them everywhere, and what the Basler BT-67, a DC-3 airframe with turboprop engines, says about the way technology really moves forward.

Subtitles are written for this video, not auto-generated. An American English audio track is available as a second audio track.

Full transcript, sources and translations: https://theresmoretoit-channel.github.io/videos/why-is-this-90-year-old-airplane-still-flying/

CHAPTERS
00:00 A 90-year-old airplane at work
01:01 Flying before the DC-3
01:19 From the DC-2 to the DC-3
02:07 So what was the secret?
02:33 Good enough at almost everything
03:10 The way it flies
03:55 Forgiving
04:42 Nobody planned for ninety years
05:14 Fixing it far from a hangar
06:15 The right moment, and a war
06:51 From an airplane to an ecosystem
07:18 Why aren't we still using them?
07:56 Old airframe, new engines
08:30 What the DC-3 says about progress

IMAGE CREDITS
Douglas DC-3 Lufthansa D-CADE Cockpit — Valder137, CC BY 2.0, via Wikimedia Commons
Douglas DC-3-194 Ibis airplane in Malmi, 1939 — Hugo Sundström, CC BY 4.0, via Wikimedia Commons
Buffalo Airways DC-3 — RAF-YYC from Calgary, Canada, CC BY-SA 2.0, via Wikimedia Commons
DC-3 in Colville Lake — Colin from Colville Lake, NWT, Canada, CC BY 2.0, via Wikimedia Commons
Basler BT-67 at Troll Airfield — Stein Nilsen, CC BY-SA 3.0, via Wikimedia Commons
All other archive images are in the public domain or have no known copyright restrictions.
Licences: creativecommons.org/licenses/by/2.0, creativecommons.org/licenses/by/4.0, creativecommons.org/licenses/by-sa/2.0, creativecommons.org/licenses/by-sa/3.0
```

> **Blok se kopíruje CELÝ** (`docs/zverejneni.md`) — atribuce je UVNITŘ.
> Povinná je u pěti snímků: CC BY-SA S08 (Buffalo Airways), S53 (BT-67),
> CC BY S04 (kokpit), S05 (Malmi), S50 (Colville Lake). Zbylých sedm je
> public domain, S45 (Piedmont) je Flickr Commons „No restrictions" —
> proto „or have no known copyright restrictions". Kontrola autorů proti
> `sources.json` prošla (viz konec souboru).
>
> **Ilustrace S38c (`art/S38c-panel.png`, ChatGPT)** se do popisu
> neuvádí: `docs/zverejneni.md` atribuci předepisuje jen archivním
> snímkům s licencí CC BY*, a na otázku „byla použita AI" nemá plochá
> ilustrace vliv (`art/PUVOD.md`).
>
> Kapitoly jsou ze scén S01, S11, S13, S17, S23, S27, S30, S32, S36, S41,
> S45, S48, S52, S56 (`work/timing.json`, celkem 558,7 s, časy zaokrouhlené
> dolů). Nejkratší kapitola je 17,6 s (S11–S13), všechny ≥ 10 s.
> **Po každém dalším běhu `tts.py` časy přepočítej** — a stejně tak
> v `youtube-preklady.md`.
>
> Popis drží míru jistoty scénáře: „some of them are still at work",
> žádný počet létajících kusů (`factcheck.md`: spolehlivý zdroj na počet
> v komerčním provozu neexistuje), „about twenty-five years". Odpověď
> na titulní otázku popis neprozrazuje.

---

## 3. Náhled

**Ještě není vybraný.** Koncepty C1–C3 v `thumbnail/KONCEPTY.md`
(doporučen C1: DC-3 na zasněžené štěrkové dráze, `1935` / `WHY WON'T IT
RETIRE?`). Po výběru: `render/thumbnail.jpg`, `thumbnail/PUVOD.md`,
`thumb_check.py`, a doplnit `thumbnail` v `project.json`.
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
| komentáře | zapnuté |
| **byla použita AI** | **ne** — 56 scén kreslených kódem (z toho S38c s plochou ilustrací z ChatGPT, `art/PUVOD.md`), 12 archivních fotek jen barevně upravených a ořezaných, žádná SDXL scéna, hudba procedurální, hlas není klon skutečné osoby |

### Závěrečná obrazovka

`zaver_check.py`: S59–S61 (od 539 s) mají **horní polovinu volnou**
(kresba 2 %) — dlaždici i kolečko odběru dej do **horní** poloviny,
dole je titulek.

---

## 6. Tagy

```
DC-3, Douglas DC-3, C-47, Dakota, Basler BT-67, aviation history,
vintage aircraft, radial engine, airliner history, bush flying,
aircraft maintenance, Buffalo Airways, legacy technology, explainer,
there's more to it
```

---

## 7. Playlist

Navrženo **`legacy`** („Legacy Tech — The Old Systems Still Running
Everything") — DC-3 je přesně ta teze: stará konstrukce, která pořád
pracuje a nová technika se k ní přidává. Dopiš slug do `playlisty.json`,
spusť `analytics.py --videa` a pak `tools/playlisty.py`.

---

## Kontrola atribucí (2026-10-03)

Strojově: každá položka `sources.json` s licencí `CC BY*` → jméno autora
(`credit`) v bloku pod „## 2. Popis". Výsledek: 5/5 nalezeno.
