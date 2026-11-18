# YouTube — 103 „Why Would Anyone Build a Radio You Can't Tune?"

Stav: **hotovo, naplánováno na zveřejnění** (2026-10-12). Závěrečná obrazovka, americká stopa a playlist `spolecnost` naklikal uživatel ve Studiu.

| | |
|---|---|
| ID videa | **`ma6eJNXru-Q`** — https://www.youtube.com/watch?v=ma6eJNXru-Q |
| master | ✅ `render/final-en-103.mp4` (1920×1080, 8:59, dekódování bez chyby, 2026-10-12 na 207; S19/S30/S57 finální, bez ID scén) |
| náhled | ✅ od 2026-10-14 hotový obrázek od uživatele `RADIO / WHERE'S THE DIAL?`, fotka bakelitové krabičky (`thumbnail/PUVOD.md`); 12.–14. 10. běželo pod kresleným C1 se stejnými texty — **při srovnání CTR dělit k tomuto datu** |
| nastavení, popis, tagy | ✅ `nahraj.py --k-videu --bez-titulku` 2026-10-12 |
| lokalizace | ✅ nahráno 2026-10-12, 13 jazyků |
| titulky | ✅ 15 stop nahráno 2026-10-12 (ASR nebyl) |
| playlist | ✅ `spolecnost` (uživatel ve Studiu, zapsáno v `playlisty.json`) |
| závěrečná obrazovka, americká stopa | ✅ uživatel ve Studiu |

**Co musí uživatel naklikat sám:** nahrát MP4 ve Studiu (průvodce vyřídí
prohlášení o AI a osvědčení o zproštění), závěrečnou obrazovku a americkou
audiostopu (`render/audio-en-US.m4a`).

Stopáž 8:59 (`work/timing.json` total 539,0 s).

> Kdyby se znovu pouštěl `tts.py`, přepočítej kapitoly tady
> i v `youtube-preklady.md` a přegeneruj `en-US` přes `us_stopa.py`.

Pořadí podle CENY (`docs/zverejneni.md`):

```bash
V=videos/103-why-build-a-radio-you-cant-tune
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
Why Would Anyone Build a Radio You Can't Tune?
```

> Wh-otázka, 46 znaků, schválená uživatelem (notes.md, v0.2).

---

## 2. Popis

```
It's almost two in the morning on 21 August 1968. Warsaw Pact armies have crossed into Czechoslovakia, and as an announcer in Prague reads the news, the country's transmitters go silent. Yet in kitchens, offices and workshops, a small box on the wall keeps talking. It has no tuning dial, no antenna and only one programme. So why would anyone build a radio you can't tune?

From Soviet "radio points" and Cold War planning to Swiss mountain valleys, classical music down Italian telephone lines and loudspeakers rented out in British towns: the story of wired radio, and of the night it carried the news someone had tried to silence.

Sources: Czech Radio (1968.rozhlas.cz, the broadcasts of 21 August 1968; Czech Radio archive, document 01075583); Statement of the Presidium of the Central Committee of the Communist Party of Czechoslovakia (21 August 1968); Czechoslovak Decree 50/1985 Coll. on wired radio; Historical Dictionary of Switzerland (Telefonrundspruch); Rai (Filodiffusione, 1958); rediffusion.info (Rediffusion 1928–1978); Novinky.cz (2003–2004).

Subtitles are written for this video, not auto-generated. An American English audio track is available as a second audio track.

Full transcript, sources and translations: https://theresmoretoit-channel.github.io/videos/why-build-a-radio-you-cant-tune/

CHAPTERS
00:00 One night in 1968
00:55 Not really a radio
02:02 Why build a second network?
03:41 One cable, one voice
04:30 Democracies did it too
05:37 Back to that night
07:26 What happened to Hoffmann
08:01 The end of the wire
08:27 Who holds the other end?

IMAGE CREDITS
Orsk Local History Museum 50 (Soviet wired-radio loudspeaker) — Stolbovsky, CC BY-SA 3.0, via Wikimedia Commons (colour-graded)
Ricevitore per filodiffusione a transistor, Brionvega FD1101 — Museo Scienza e Tecnologia Milano; Brionvega, Achille and Pier Giacomo Castiglioni, CC BY-SA 4.0, via Wikimedia Commons (colour-graded)
Praga 11 — Engramma.it, CC BY-SA 3.0, via Wikimedia Commons (colour-graded)
Srpen 1968 4 — František Dostál, CC BY-SA 4.0, via Wikimedia Commons (colour-graded)
Licences: creativecommons.org/licenses/by-sa/3.0 · creativecommons.org/licenses/by-sa/4.0
All other archive images are in the public domain.
```

> **Blok se kopíruje CELÝ** (`docs/zverejneni.md`). Povinné kredity jsou
> čtyři CC BY-SA ze `sources.json`: S21, S37, S43, S49, u BY-SA i s uvedením
> úprav. S54 (Hoffmann, *Obrana lidu* 1971) je public domain.
> U S37 Commons uvádí jako credit výrobce a designéry, ne fotografa.
> Opsáno, jak to stojí, s muzeem jako zdrojem.
>
> **Pointa se neprozrazuje.** Popis neříká, kdo vysílače vypnul, ani co se
> s Hoffmannem stalo. Kapitola „What happened to Hoffmann" jen jmenuje.
> Úvod popisu jen převypráví studený začátek S01–S05 (0:00–0:37).
>
> Kapitoly jsou ze scén S01, S09, S18, S28, S34, S43, S54, S58, S61
> (`work/timing.json`, zaokrouhleno dolů). Nejkratší je 26 s (S58 → S61),
> poslední 32 s; všechny ≥ 10 s, první na 00:00. Výzva k odběru S17b
> (1:56) leží v kapitole „Not really a radio".
>
> Zdroje podle `factcheck.md`: [ČRo-A] PDF 01075583, [Prov] provolání,
> [1968] 1968.rozhlas.cz, vyhláška 50/1985 Sb., HLS (S36), it.wiki/Rai
> (S37), rediffusion.info (S38), [Nov] Novinky (S55–S56).

---

## 3. Náhled

✅ **C1 „RADIO / WHERE'S THE DIAL?"** (vybral uživatel 2026-10-12): krabička
z videa (S06) bez ladění, kabel dolů. Kresleno kódem (`thumbnail/gen.py`),
klíč `thumbnail` v `project.json`, soubor `render/thumbnail.jpg`.
Koncepty v `thumbnail/KONCEPTY.md`.

---

## 4. Titulky

`subtitles/*.srt`, 14 jazyků + `en-US`. Jazyk videa **`en-gb`** (hlas
`bf_emma`) se musí nastavit dřív, než se nahrají titulkové stopy. Codex
na všech 13 překladech proběhl a nálezy jsou zapracované (2026-10-12),
takže titulky a lokalizace můžou nahoru hned po `nahraj.py`.

---

## 5. Nastavení

| | |
|---|---|
| kategorie | **Science & Technology** (28) — posílá `nahraj.py` napevno |
| jazyk videa | `en-gb` |
| licence | standardní |
| pro děti | **ne** |
| komentáře | zapnuté |
| **byla použita AI** | **ne** (návrh, rozhoduje uživatel). Většina scén je kreslená kódem. Pět archivních snímků je jen barevně upravených (*color adjustment* je výslovná výjimka). S19 je SDXL. S30 a S57 jsou SDXL, které uživatel nechal upravit v ChatGPT (`art/PUVOD.md`). Všechny tři jsou malované ilustrace podle kotvy stylu, nefotorealistické, žádné konkrétní skutečné místo ani událost. Noc 1968 nese archiv a kresba, ne generovaný obraz. Hudba je procedurální, hlas není klon. |

### Závěrečná obrazovka

Může být plných 20 s, **od 8:39** (S63–S65). Závěr S62–S65 je kreslený
jen v dolní polovině (`DOLE`). Prvky patří do **horní poloviny**, protože
spodní rohy zabírá titulek (`zaver_check.py`: S65 OK).

---

## 6. Tagy

```
wired radio, radio by wire, Czechoslovakia 1968, Prague Spring, Warsaw Pact invasion,
Soviet invasion of Czechoslovakia, radio tochka, Telefonrundspruch, Filodiffusione,
Rediffusion, Karel Hoffmann, Cold War radio, propaganda, history of radio,
broadcasting history, science explainer, there's more to it
```

---

## 7. Playlist

Navrženo **`spolecnost`** (*How Society Actually Runs*). Video je o tom,
že technika sama neurčí, k čemu slouží, ale kdo drží síť a program
(S41, S64). Alternativa je **`legacy`**, kdyby uživatel četl video spíš
jako o staré technice. Ta ale v roce 1999 skončila, takže do „still
running" nesedí. Dopiš slug do `playlisty.json`, spusť `analytics.py --videa`
a pak `tools/playlisty.py`.
