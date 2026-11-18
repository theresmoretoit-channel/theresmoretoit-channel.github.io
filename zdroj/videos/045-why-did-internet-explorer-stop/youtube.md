# Podklady k nahrání na YouTube

Časy kapitol **ověřené proti `work/timing.json`**, ne odhadnuté.
Každá kapitola je od předchozí aspoň 10 s, první je `00:00` a je jich
23 — YouTube uzná kapitoly, jen když platí všechny tři podmínky.

| co | odkud |
|---|---|
| video | `render/final-en.mp4` — 1920×1080, **13:45**, 48,3 MB |
| náhled | `render/thumbnail.jpg` — 1280×720, 0,22 MB |
| titulky | `subtitles/*.srt` — **deset stop**: devět jazyků + `en-US` |
| americká stopa | `render/audio-en-US.m4a` — 19,5 MB, sedí na obraz na tisícinu |
| lokalizované názvy a popisy | `youtube-preklady.md` přes `tools/lokalizace.py` |

**Archivní snímky video nemá ani jeden**, takže v popisu není žádná
povinná atribuce — `sources.json` je prázdný a `CREDITS.md` nevzniklo.
Je to první díl série bez archivu: všech 88 obrazů je kreslených kódem
a tři jsou z SDXL.

---

## Titul

```
Internet Explorer 6 — Why Did It Stop For Five Years?
```

> Wh-otázka schválně. Naměřeno na kanálu (29 videí, vážené impresemi):
> wh-otázka **2,23 %**, tvrzení 1,63 %. Všechny tři předchozí díly série
> jsou tvrzení.

## Popis

```
In August 2001, Microsoft released Internet Explorer 6. The next version
of the browser came out in October 2006.

Five years and two months, and in between no new version of the browser
almost everyone in the world was using. Not because nobody complained —
by the middle of that gap there were whole websites about what was wrong
with it.

This is part four, and it asks the question the first three never did.
Not what the browser did to the web. Why it stopped.

The answer isn't that Microsoft couldn't build something better. It could,
and it did: in March 2000 it shipped a browser with a different engine,
without the box model bug that cost the web a decade of workarounds — and
ended its development six weeks after announcing that Internet Explorer 6
would be the last version you could install on its own.

Along the way: the antitrust case that ended eight weeks before Internet
Explorer 6 shipped, the online chat where Microsoft said the browser was
now a feature of Windows, the engineer who worked on it from 1995 and
later wrote down why it stopped, the component built for company email in
the nineties that the whole modern web was later built on, the reason your
browser still calls itself Mozilla, the toolbars that ate a third of your
screen, and the fix that arrived as a service pack for the operating
system instead of a new browser.

Part one — how Internet Explorer 6 became a platform:
https://youtu.be/R7Un3IOMvbg

Part two — the bugs that had names:
https://youtu.be/1dIM5UZUEZg

Part three — the browser that wouldn't die:
https://youtu.be/dnF3SJoeTns

Full transcript, sources and translations: https://theresmoretoit-channel.github.io/videos/why-did-internet-explorer-stop/

Chapters
00:00 Five years and two months
00:40 This is part four
01:01 Ninety percent of the market
01:22 The courts
01:52 Eight weeks later
02:26 The last standalone version
03:13 The next Windows
03:48 Where the people went
04:42 The sentence this is about
04:57 The other browser
05:38 Two modes, still there
06:06 Two browsers, one summer
06:47 What was already inside
07:12 A page that could ask
07:58 AJAX
08:27 What else came from here
09:02 Ask your browser what it is
09:50 The other half
10:20 A way to extend it
10:44 Four toolbars
11:28 A service pack, not a browser
12:26 Firefox, then RSA
13:02 So why did it stop?

Subtitles are written for this video, not auto-generated. An American
English audio track is available as a second audio track.

All visuals are drawn from code; no archive photographs are used in this
video.
```

## Tagy

```
internet explorer, internet explorer 6, ie6, browser history, web history,
microsoft, web development, netscape, firefox, activex, xmlhttprequest,
ajax, browser wars, windows xp, service pack 2, tasman, web standards,
software history, tech history, monopoly
```

## Nastavení

| pole | hodnota |
|---|---|
| **jazyk videa** | **`en-gb`** — nastavit **PRVNÍ**, jinak zůstane dlaždice Titulky zašedlá |
| kategorie | Věda a technika |
| **byla použita AI** | **NE** — viz níž |
| licence | standardní licence YouTube |
| vkládání | **povolit** (`videos.update` smaže, co v těle není) |
| viditelnost | nahrát **neveřejně**, podívat se na to v přehrávači, teprve pak zveřejnit |
| playlist | dopsat slug do `playlisty.json`, pak `analytics.py --videa` a `tools/playlisty.py` |

### Proč „byla použita AI" = NE

Rozhoduje **fotorealističnost, ne použití AI**. U tohohle videa to drží:

- **88 z 91 obrazů je kreslených kódem** (SVG → Inkscape), tedy diagramy
- **tři SDXL scény** (S25, S44, S74) jsou díky kotvě stylu malované
  ilustrace, ne fotorealismus
- **archivní snímek žádný**
- hudba je **procedurální** (`tools/music.py`), ne z generativního modelu

Náhled je fotorealistický a dodaný zvenčí (viz `thumbnail/PUVOD.md`), ale
**ta otázka se ptá na obsah videa, ne na miniaturu**.

### Co musí uživatel naklikat sám

Při nahrání ručně ve Studiu + `nahraj.py --k-videu <ID>`:

| | kdo to dělá |
|---|---|
| prohlášení o AI | ✅ průvodce při nahrání |
| osvědčení o zproštění | ✅ průvodce při nahrání |
| **závěrečná obrazovka** | ❌ **ručně** — Data API na to nemá ani zdroj |
| **druhá audiostopa (`en-US`)** | ❌ **ručně** ve Studiu, API na to nemá volání |

`zaver_check.py` ověřil, že místo na závěrečnou obrazovku je: okno
posledních 20 s pokrývají **S88–S91** a u všech čtyř se dlaždice
i kolečko vejdou nahoru s nulovým překryvem. **Dole je titulek**, takže
prvky patří do horní poloviny.

### Po zveřejnění

```bash
python tools/titulky.py --vse --smaz-asr    # automatický přepis od YouTube
```

Smazání přepis jen odstraní, **nezakáže** — YouTube si ho vyrobí znovu,
takže se to pouští po každém novém videu.
