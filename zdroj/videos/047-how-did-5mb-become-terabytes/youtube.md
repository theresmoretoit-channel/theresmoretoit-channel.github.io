# Podklady k nahrání na YouTube

Časy kapitol **ověřené proti `work/timing.json`**, ne odhadnuté.
Každá kapitola je od předchozí aspoň 10 s, první je `00:00` a je jich
21 — YouTube uzná kapitoly, jen když platí všechny tři podmínky.

| co | odkud |
|---|---|
| video | `render/final-en.mp4` — 1920×1080, **10:51** (master se renderuje, draft sedí na sekundu) |
| náhled | `render/thumbnail.jpg` — 1280×720, 0,20 MB |
| titulky | `subtitles/*.srt` — **patnáct stop**: čtrnáct jazyků + `en-US` |
| americká stopa | `render/audio-en-US.m4a` — 15,0 MB, `speed` 0,949, přetečení 1,83 % |
| lokalizované názvy a popisy | `youtube-preklady.md` přes `tools/lokalizace.py` |

**Jeden archivní snímek, a je pod CC BY-SA 4.0**, takže atribuce je
POVINNÁ a je **uvnitř bloku „Popis"** — ne pod ním. Zbytek videa je
kreslený kódem (80 diagramů) a dvě scény z SDXL.

> **Věta o americké stopě platí, jen když ji uživatel do Studia
> doopravdy nahraje.** Z API ani z disku se to nepozná (`docs/zverejneni.md`),
> a popis, který slibuje stopu, jež tam není, je nepravdivý ve čtrnácti
> jazycích naráz. Když se stopa nenahraje, druhá věta se z popisu i ze
> všech překladů vypustí.

---

## Titul

```
How Did 5 MB Become Terabytes?
```

> Wh-otázka schválně (na kanálu 2,23 % proti 1,63 % u tvrzení) a číslice
> ve výpisu drží oko. Obě strany kontrastu jsou konkrétní a odpověď
> titul neprozrazuje.

## Popis

```
In 1956, IBM shipped the first hard drive. It stored about five megabytes
— one photograph from a modern phone — and with the compressor that kept
it running, it weighed more than a ton.

The obvious explanation is that we got better at building small machines.
That explanation is true and it is the boring half. The machine got about
a thousand times lighter. The storage got about a billion times denser.
Everything interesting about storage is hiding in that gap.

On the disk IBM shipped in 1956, one square centimetre held three hundred
bits. A modern drive puts nearly three hundred billion into the same
square centimetre. This video is about how that happened: the head that
had to fly without touching, the compressor that disappeared when someone
shaped the head like a wing, the physical effect two laboratories found
independently in 1988 that made weak signals readable, and the wall that
arrived when a magnetic grain became small enough for room temperature to
flip it on its own.

And then the part that makes both halves of the industry rhyme. When the
bit could not get any smaller, the bit was stood upright. When the flash
cell could not get any smaller, the cells were stacked. Different
materials, different physics, different companies — and the same move.

Subtitles are written for this video, not auto-generated. An American
English audio track is available as a second audio track.

Full transcript, sources and translations: https://theresmoretoit-channel.github.io/videos/how-did-5mb-become-terabytes/

Chapters
00:00 The machine that weighed a ton
00:27 A thousand against a billion
00:57 Tape is a queue
01:24 Fifty disks, twenty times a second
01:42 The head must not touch
02:14 What five megabytes really was
02:32 Three hundred bits
02:50 The compressor goes
03:24 What a bit actually is
03:59 The signal gets too weak
04:14 Fert and Grünberg
05:02 A billion times
05:30 The wall
06:04 Running out of atoms
06:30 Standing the bits upright
07:12 A laser in the head
07:50 Take the disk out entirely
08:29 Flash hits its own wall
09:14 The same answer
09:57 The old technology moved
10:15 We built upwards

IMAGE CREDITS
IBM 305 RAMAC system (2) — Norsk Teknisk Museum, CC BY-SA 4.0
via Wikimedia Commons
Licences: creativecommons.org/licenses/by-sa/4.0
```

## Tagy

```
hard drive, data storage, RAMAC, IBM, areal density, GMR, giant
magnetoresistance, perpendicular recording, HAMR, NAND flash, 3D NAND,
superparamagnetic limit, computer history, how it works, storage density
```

## Nastavení

| položka | hodnota |
|---|---|
| kategorie | Science & Technology (28) |
| jazyk videa | **en-GB** — nastavit PŘED titulky, jinak zůstane dlaždice Titulky zašedlá |
| licence | Creative Commons – Attribution (snímek je CC BY-SA, video je vlastní tvorba) |
| vytvořeno pro děti | ne |
| **prohlášení o AI** | **ne** — SDXL scény jsou malované ilustrace, archivní snímek je upravený jen barevně, hudba je procedurální |
| náhled | fotorealistický obrázek, ale ten se otázky na AI **netýká** (ptá se na obsah videa); rozbor v `thumbnail/PUVOD.md` |

## Co musí uživatel naklikat sám

1. **Závěrečná obrazovka** — API na ni nemá ani zdroj. Místo je ověřené
   `zaver_check.py`, poslední čtyři scény ho mají.
2. **Druhá audiostopa** (`render/audio-en-US.m4a`) — nahrát umí jedině
   Studio. Když se nenahraje, vypustit větu o ní z popisu i z překladů.
3. **Playlist** — dopsat slug do `playlisty.json`, pak `analytics.py --videa`
   a `tools/playlisty.py`.

## Pořadí kroků — RUČNĚ, protože kvóta API je vyčerpaná

**Rozhodl uživatel 2026-09-15: nic se nevolá přes API, všechno se
naklikává ve Studiu.** Denní strop je 10 000 jednotek na celý projekt
a tenhle postup by stál 7 753 (video 1 600, náhled 50, patnáct
titulkových stop 6 000, lokalizace 102, `videos.list` 1) — takže se
počká, nebo se to udělá rukou. Rukou to stojí nula jednotek.

| pořadí | co ve Studiu | odkud soubor |
|---|---|---|
| 1 | **nahrát video** jako neveřejné | `render/final-en.mp4` (1920×1080, 10:51, 41,8 MB) |
| 2 | **jazyk videa `en-GB`** | až potom jde nahrávat titulky — jinak zůstane dlaždice Titulky zašedlá |
| 3 | titul a popis | `youtube.md`, blok pod „Titul" a **celý** blok pod „Popis" včetně kreditů |
| 4 | kategorie, licence, děti, AI | tabulka „Nastavení" výš |
| 5 | **náhled** | `render/thumbnail.jpg` |
| 6 | **patnáct titulkových stop** | `subtitles/*.srt` — `en` jako hlavní, k tomu `en-US` a dvanáct dalších |
| 7 | **druhá audiostopa** | `render/audio-en-US.m4a` (Studio → Upravit → Zvukové stopy) |
| 8 | **třináct lokalizací** | `youtube-preklady.md` — sekce jsou **v pořadí Studia**, kopíruj shora dolů |
| 9 | **závěrečná obrazovka** | API na ni nemá ani zdroj, je ruční vždycky |
| 10 | zveřejnit, pak playlist | dopsat slug do `playlisty.json` |

> **Automatický přepis od YouTube se maže**, ale `titulky.py --smaz-asr`
> je taky API (50 + 50 jednotek na video). Buď se to udělá ve Studiu
> ručně (Titulky → automaticky vygenerované → smazat), nebo se to nechá
> na den, kdy bude kvóta volná. Smazání přepis jen odstraní, **nezakáže**
> — YouTube si ho vyrobí znovu, takže jeden průchod navíc nic nezkazí.

> **Až bude kvóta zase volná a bude se něco dodělávat přes API, pozor na
> `videos.update`:** přepisuje celou část, takže co v těle chybí, to
> smaže — včetně naplánovaného zveřejnění a „Povolit vkládání". Postup je
> vždycky `list` → upravit → `update` (viz `docs/zverejneni.md`).

## Kdyby se kvóta uvolnila dřív

```bash
python tools/nahraj.py videos/047-how-did-5mb-become-terabytes --k-videu <ID>
python tools/lokalizace.py videos/047-how-did-5mb-become-terabytes
python tools/titulky.py videos/047-how-did-5mb-become-terabytes --smaz-asr
```

> **`--vse` v den nahrávání ne** — `captions.list` stojí 50 jednotek za
> video a `--vse` projde celý kanál dvakrát, tedy 4 550 jednotek. Na nové
> video se navíc `--vse` vůbec nepodívá, protože čte `analytics/videa.json`.
