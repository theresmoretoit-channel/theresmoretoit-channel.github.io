# Podklady k nahrání na YouTube

Časy kapitol **ověřené proti `work/timing.json`**, ne odhadnuté.
Každá kapitola je od předchozí aspoň 10 s, první je `00:00` a je jich
26 — YouTube uzná kapitoly, jen když platí všechny tři podmínky.

| co | odkud |
|---|---|
| video | `render/final-en.mp4` — 1920×1080, **11:48**, 52,9 MB |
| náhled | `render/thumbnail.jpg` — 1280×720, 0,08 MB (varianta A, viz níž) |
| titulky | `subtitles/*.srt` — **patnáct stop**: čtrnáct jazyků + `en-US` |
| americká stopa | `render/audio-en-US.m4a` — 16,5 MB, `af_heart` při `speed` 0,9547 |
| lokalizované názvy a popisy | `youtube-preklady.md` přes `tools/lokalizace.py` |

**Jeden archivní snímek (S27) a jeho atribuce je POVINNÁ** — KOGL Type 1
žádá uvedení zdroje. Je proto **uvnitř bloku „Popis"**, ne pod ním.

---

## Titul

```
How Does a Dictatorship Become a Democracy?
```

> Wh-otázka schválně (kanálem naměřeno na 29 videích, vážené impresemi:
> wh-otázka **2,23 %**, tvrzení 1,63 %, ano/ne otázka 1,21 %).
>
> **Tohle je varianta A z A/B/C testu.** Tři náhledy a tři tituly,
> soupis v `notes.md`. Studio vyhlásí vítěze, ale při objemu kanálu
> to **není měření** — rozlišit 2 % od 3 % chce 3 821 zobrazení na
> variantu a kanál má ~345 denně na všech 41 videí dohromady.

## Popis

```
Imagine you are a dictator. Somebody walks in and suggests holding a real
election, with a real chance of losing. Your first question is not about
democracy. It is: what happens to me if I lose?

For most of history the answer was prison, exile or a wall. And yet it has
happened — not once, but repeatedly, and usually without a revolution.

Taiwan spent 38 years under martial law, the longest in the world at the
time. Tens of thousands were imprisoned and thousands were executed. In
2000 the party that had run the island since 1949 lost a presidential
election, and handed over power. The tanks did not roll. Nobody announced
that the result had been misinterpreted.

South Korea did something similar in 1987, with the Olympic Games a year
away and the world about to watch. Chile's dictator wrote a referendum
into his own constitution, expecting to win it, and lost. Spain took its
transition apart from the inside after Franco died.

And then there is the case that did none of this: China got richer,
better educated and more connected to the world than any of them, and
the political system did not follow.

The pattern is not that dictators become democrats. It is that a regime
can reach a point where its own leaders start asking a different question
— not how do we hold on forever, but how do we change this without
destroying ourselves. That question has a name in this video: the exit
problem.

Chapters
00:00 Imagine you are a dictator
00:23 The whole problem in one line
00:43 Taiwan
01:09 What the authoritarian state looked like
01:42 And then it started to change
02:16 The party that was illegal
02:49 Martial law is lifted
03:06 The year 2000
03:22 The tanks did not roll
03:53 So why did Taiwan do it?
04:11 South Korea
04:29 The Olympics were coming
05:05 Chile votes on Pinochet
05:38 What he kept
05:58 Spain
06:38 The pattern
07:01 The exit problem
07:45 Every reason to hold on
08:11 China
08:59 Development is not destiny
09:13 What actually matters
09:44 Taking it apart from the inside
10:19 The paradox
10:37 The half nobody pictures
11:08 Losing is survivable

Subtitles are written for this video, not auto-generated. An American
English audio track is available as a second audio track.

IMAGE CREDITS
이한열 추모행진 집회 — 서울특별시, KOGL Type 1
via Wikimedia Commons
Licence: http://www.kogl.or.kr/info/licenseType1.do

Every other visual in this video is drawn from code.
```

## Tagy

```
democracy, dictatorship, taiwan, south korea, chile, spain, china,
political transition, authoritarianism, martial law, pinochet, kuomintang,
democratisation, elections, political science, history, comparative
politics, modernisation theory, tiananmen, deng xiaoping
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

Rozhoduje **fotorealističnost, ne použití AI**:

- **80 z 85 scén je kreslených kódem** (SVG → Inkscape), tedy diagramy
- **čtyři SDXL scény** (S10, S37, S53, S66) jsou díky kotvě stylu
  malované ilustrace, ne fotorealismus
- **jeden archivní snímek** (S27) je upravený jen barevně — *„color
  adjustment or lighting filters"* je výslovná výjimka pravidel
- hudba je **procedurální** (`tools/music.py`), ne z generativního modelu

Náhledy jsou kreslené kódem (`thumbnail/gen.py`), takže ani tady není co
řešit — a ta otázka se navíc ptá na obsah videa, ne na miniaturu.

### Co musí uživatel naklikat sám

Při nahrání ručně ve Studiu + `nahraj.py --k-videu <ID>`:

| | kdo to dělá |
|---|---|
| prohlášení o AI | ✅ průvodce při nahrání |
| osvědčení o zproštění | ✅ průvodce při nahrání |
| **závěrečná obrazovka** | ❌ **ručně** — Data API na to nemá ani zdroj |
| **druhá audiostopa (`en-US`)** | ❌ **ručně** ve Studiu, API na to nemá volání |
| **A/B/C test náhledu a titulu** | ❌ **ručně** — Test & Compare ve Studiu |

> **Popis slibuje americkou stopu, takže ji tam přidej**, jinak je ta
> věta nepravdivá ve čtrnácti jazycích naráz. Soubor je
> `render/audio-en-US.m4a` a sedí na obraz (707,629 s proti 707,64 s).

`zaver_check.py` ověřil, že místo na závěrečnou obrazovku je: okno
posledních 20 s pokrývají **S70, S71 a S72** a u všech tří se dlaždice
i kolečko vejdou **nahoru vlevo** s nulovým překryvem. **Dole je
titulek**, tam prvky nepatří.

### Po zveřejnění

```bash
python tools/titulky.py . --smaz-asr        # JEDNO video, 100 jednotek
```

`--vse` v den nahrávání ne — stojí 4 550 jednotek a čerstvé video stejně
nevidí, protože čte `analytics/videa.json`.
