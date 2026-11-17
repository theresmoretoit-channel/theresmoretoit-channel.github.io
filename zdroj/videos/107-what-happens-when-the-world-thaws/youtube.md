# YouTube — 107 „What Happens When the World Thaws?“

Stav: **nahráno 2026-10-14** (https://www.youtube.com/watch?v=tb_PfBGezwY).
Metadata, náhled C2, lokalizace 13 jazyků, 15 titulkových stop a playlist
`zeme` hotové přes API. Ručně zbývá závěrečná obrazovka a americká stopa.
SDXL S41 nemá viditelné plameny (tři pokusy, vybrán seed 4101 se sloupem
oranžového kouře).

| | |
|---|---|
| ID videa | `tb_PfBGezwY` |
| master | ✅ `render/final-en-107.mp4` (207, 2026-10-14, 1920×1080, 481,8 s, `ffmpeg -f null` čistý) |
| náhled | ✅ hotový obrázek od uživatele podle C2 (`thumbnail/PUVOD.md`) — **nahrává uživatel ručně**; přes API je zatím nahraný kreslený C2 |
| nastavení, popis, tagy | podklady níž |
| lokalizace | ✅ `youtube-preklady.md`, 13 jazyků, nahráno (Codex všech 13: `work/codex-yt-*.txt`) |
| titulky | ✅ `subtitles/*.srt`, 14 jazyků + `en-US`, všechny prošly Codexem (`codex-zapracovano.md`) |
| americká stopa | ✅ `render/audio-en-US.m4a` — nahrává uživatel ve Studiu |
| závěrečná obrazovka | ručně ve Studiu |
| playlist | ✅ nový `zeme` (PLEEhg8Q73Im4), 107 na prvním místě |

**Co musí uživatel naklikat sám:** nahrát MP4 ve Studiu (průvodce vyřídí
prohlášení o AI a osvědčení o zproštění), závěrečnou obrazovku a americkou
audiostopu (`render/audio-en-US.m4a`).

Stopáž 8:02 (`work/timing.json` total 481,8 s).

> Kdyby se znovu pouštěl `tts.py`, přepočítej kapitoly tady
> i v `youtube-preklady.md` a přegeneruj `en-US` přes `us_stopa.py`.

Pořadí podle CENY (`docs/zverejneni.md`):

```bash
V=videos/107-what-happens-when-the-world-thaws
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
What Happens When the World Thaws?
```

> Wh-otázka, 34 znaků, pracovní název videa od založení. Neprozrazuje,
> že odpověď není epidemie.

---

## 2. Popis

```
In 2023, scientists thawed a lump of mud from 16 metres beneath a Siberian lake. A virus that had been frozen in it for more than 48,000 years could still infect a living cell. The ground it came from is thawing. So what else is in there? Diseases that disappeared long ago? Or something that could warm the planet even further?

From Batagaika, a crater in Yakutia whose walls are still retreating, to an anthrax outbreak among reindeer on the Yamal Peninsula, from a tundra fire on Alaska's North Slope, in a place with no trace of fire for 5,000 years, to fires that smoulder under the snow all winter: what is actually frozen in the permafrost, and which part of it is the real danger.

Sources: Alempic et al. (2023), Viruses; Legendre et al. (2014), PNAS; Obu et al. (2019), Earth-Science Reviews; Murton et al. (2023) and Kizyakov et al. (2024) on Batagaika; Liskova et al. (2021) and Hueffer et al. (2020) on the 2016 Yamal anthrax outbreak; Global Carbon Budget 2024 (Friedlingstein et al. 2025); Hugelius et al. (2014); Schuur et al. (2015), Nature; IPCC AR6 Working Group I; Mack et al. (2011), Nature, and Hu et al. (2010) on the Anaktuvuk River fire; Jones et al. (2015), Scientific Reports; Copernicus Atmosphere Monitoring Service (2020); Scholten et al. (2021), Nature; NOAA Arctic Report Card 2024 (Natali et al.); Hjort et al. (2018), Nature Communications.

Subtitles are written for this video, not auto-generated. An American English audio track is available as a second audio track.

CHAPTERS
00:00 A virus frozen for 48,000 years
00:39 What permafrost is
01:11 Batagaika, a crater that keeps growing
01:48 Could something down there infect us?
02:32 Anthrax on the Yamal Peninsula
03:37 The bigger danger
03:57 How much carbon is down there?
04:52 Microbes and methane
05:35 Fire on the tundra
06:34 Putting it all together
07:13 The ground under people's homes
07:31 What happens when the world thaws?

IMAGE CREDITS
Massive ice - retrogressive thaw slump - Herschel Island — Dave Fox, CC BY-SA 4.0, via Wikimedia Commons
Licences: creativecommons.org/licenses/by-sa/4.0
All other archive images are in the public domain: the Batagaika crater (NASA Earth Observatory, Landsat data from the U.S. Geological Survey) and the Yamal Peninsula (NASA Terra MODIS), via Wikimedia Commons.
```

> **Blok se kopíruje CELÝ** (`docs/zverejneni.md`). Povinná atribuce je
> jediná, S07 (CC BY-SA 4.0, Dave Fox), a je uvnitř bloku ve tvaru TASL.
> Oba public domain snímky jsou vypsané jen kvůli divákovi.
>
> **Pointa se neprozrazuje.** Popis neříká, že větší nebezpečí je uhlík
> a že tundra už víc vydává, než pohlcuje (S50) — jen „which part of it
> is the real danger“. Kapitola 06:34 je proto „Putting it all together“
> (věta z S47), ne „From store to source“.
>
> Kapitoly ze scén S01, S05, S09, S12, S17, S24, S27, S34, S40, S47, S53,
> S55 (`work/timing.json`, zaokrouhleno dolů). Nejkratší 18 s (S53 → S55),
> všechny ≥ 10 s, první na 00:00. Výzva k odběru S11b (1:40) leží
> v kapitole „Batagaika“.
>
> Zdroje podle `factcheck.md`. Čísla v popisu (16 m, 48 000 let, 5 000 let)
> jsou tatáž jako ve scénáři v0.5, tedy číslicí.

---

## 3. Náhled

✅ `48,000 YEARS / WHAT WAKES UP?` — blok tajícího ledu s virem. Napřed
kreslený C2 (`thumbnail/gen.py`), týž večer nahrazen hotovým obrázkem od
uživatele podle téhož konceptu (`thumbnail/PUVOD.md`: retuš vodoznaku,
1280×720). Pointu (uhlík) neprozrazuje.

---

## 4. Titulky

`subtitles/*.srt`, 14 jazyků + `en-US`. Jazyk videa **`en-gb`** (hlas
`bf_emma`) se musí nastavit dřív, než se nahrají titulkové stopy.
Codex na všech 13 překladech proběhl a nálezy jsou zapracované
(`codex-zapracovano.md`). **Po případných opravách scénáře z dalšího
poslechu je potřeba titulky přegenerovat** (naposledy 2026-10-14 po S47).

---

## 5. Nastavení

| | |
|---|---|
| kategorie | **Science & Technology** (28) — posílá `nahraj.py` napevno |
| jazyk videa | `en-gb` |
| licence | standardní |
| pro děti | **ne** |
| komentáře | zapnuté |
| **byla použita AI** | **ne** (návrh, rozhoduje uživatel). 50 scén je kreslených kódem, tři archivní snímky jsou jen barevně upravené (*color adjustment* je výslovná výjimka). **Čtyři scény ze SDXL** (S25, S38, S41, S53) — malované ilustrace kotvou stylu, ne fotorealismus. **Až budou vygenerované, zkontroluj to**, zvlášť S41 (požár u řeky Anaktuvuk) a S53 (domy na permafrostu): konkrétní skutečné místo či událost ve fotorealistickém podání by odpověď překlopilo na ano. Hudba je procedurální, hlas není klon. |

### Závěrečná obrazovka

Plných 20 s, **od 7:41** (S55–S57). `zaver_check.py`: S55–S57 OK, prvky
patří do **horní poloviny**, spodní rohy zabírá titulek.

---

## 6. Tagy

```
permafrost, thawing permafrost, arctic, climate change, permafrost carbon feedback,
zombie viruses, ancient viruses, batagaika crater, siberia, yamal anthrax,
methane, carbon cycle, tundra fires, zombie fires, arctic report card,
global warming, science explainer, there's more to it
```

---

## 7. Playlist

**Nový playlist `zeme`** — *Planet Earth — What We're Doing to It*
(PLEEhg8Q73Im4, založen 2026-10-14 na pokyn uživatele). Pořadí: 107,
012 a 075 (mikroplasty; ty zůstávají i v `bezne`). Poličku na stránce
kanálu je třeba naklikat ručně.
