# Podklady k nahrání na YouTube

Časy kapitol **ověřené proti `work/timing.json`**, ne odhadnuté. Je jich
**22**, první je `00:00` a nejkratší rozestup je **10,1 s** — YouTube uzná
kapitoly, jen když platí všechny tři podmínky.

| co | odkud |
|---|---|
| video | `render/final-en.mp4` — **zatím NEEXISTUJE**, master čeká na herní PC |
| délka | **8:46** (526,7 s, z `work/timing.json`) |
| náhled | `render/thumbnail.jpg` — 1280×720, 0,15 MB |
| titulky | `subtitles/*.srt` — **čtrnáct jazyků** |
| americká stopa | **NENÍ** — viz níž |
| lokalizované názvy a popisy | `youtube-preklady.md` přes `tools/lokalizace.py` |

> **Tři SDXL scény (S32, S39, S71) jsou zatím placeholdery.** Master se
> nesmí renderovat, dokud se nevygenerují přes ComfyUI na herním PC.

> **Věta o americké audiostopě v popisu SCHVÁLNĚ NENÍ.** Video druhou
> stopu nemá — `subtitles/en-US.srt` ani `work-us/` neexistují. Až se
> stopa vyrobí (`tools/us_stopa.py`) a nahraje ve Studiu, přidá se do
> popisu i do všech třinácti překladů druhá věta odstavce:
> *„An American English audio track is available as a second audio
> track."* Znění pro třináct jazyků je hotové
> v `videos/045-why-did-internet-explorer-stop/youtube-preklady.md`.
>
> Doc to říká natvrdo: **z API ani ze souborů na disku se nepozná, jestli
> video stopu má** — `audioStreams` vrací 0 i u videí, která ji
> prokazatelně mají. Popis, který slibuje stopu, jež tam není, je
> nepravdivý ve čtrnácti jazycích naráz.

**Jeden archivní snímek (S34) má licenci CC BY-SA 4.0, takže je atribuce
POVINNÁ.** Je proto **uvnitř bloku „Popis"**, ne pod ním — u čtyř videí
z šestnácti chyběla právě proto, že kredity visely jako poznámka pod
blokem.

---

## 1. Titul

```
Why Do We Actually Need Exercise?
```

> Wh-otázka schválně (naměřeno na 29 videích kanálu, vážené impresemi:
> wh-otázka **2,23 %**, tvrzení 1,63 %, ano/ne otázka 1,21 %).
> Titul přišel s námětem od uživatele a neměnil se.

## 2. Popis

```
People say exercise is good for you. But have you ever stopped to ask why?

In 1966, five healthy twenty-year-olds spent three weeks in bed. Not ill,
not injured — just horizontal. When the researchers measured how much
oxygen their bodies could use at full effort, it had fallen by 27 per
cent. Thirty years later the same five men came back, and it turned out
that three weeks in bed at twenty had done more damage than three decades
of ordinary ageing.

That number is really what this video is about, because it tells you what
kind of thing a body is. Not a lump of matter that keeps its shape until
something breaks it, but a system that keeps asking one question: how much
am I being asked to do?

You do not need a hospital bed to see it. Ten healthy young men were asked
to do one thing — walk less, from about ten thousand steps a day to
thirteen hundred. Two weeks later their muscles were measurably worse at
pulling sugar out of the blood.

The obvious next move is to blame modern life, and that is where this kind
of story usually goes wrong. So this one takes a detour through a result
that complicates it: when researchers measured how much energy the Hadza
of Tanzania actually burn in a day, it came out about the same as ours.
Same body size, same daily total. All that walking did not show up as a
bigger number.

Which leaves a stranger question. If movement matters this much, why does
not moving not feel like anything at all?

Full transcript, sources and translations: https://theresmoretoit-channel.github.io/videos/why-do-we-actually-need-exercise/

Chapters
00:00 Exercise is good for you
00:25 So what goes wrong when we don't?
00:49 Twenty-seven per cent gone
01:01 The study waited thirty years
01:16 Three weeks versus thirty years
01:42 Muscle is the obvious case
01:56 Bone, and where it goes first
02:19 Not decaying — measuring
02:38 Ten thousand steps to thirteen hundred
03:06 So why is a body built like that?
03:35 The Hadza
04:02 Meanwhile, the rest of us
04:33 Where this story usually goes wrong
04:58 They burn the same as us
05:25 Why does it not feel like it?
05:44 There is no alarm
06:05 Two flights of stairs
06:15 The second half
06:44 A thought experiment
07:29 Three generations
07:57 The wrong shape
08:11 Perhaps the question was never that

Subtitles are written for this video, not auto-generated.

IMAGE CREDITS
Back view of hunters walking single-file bush paths in Tanzania
— Arnold Tibaijuka, CC BY-SA 4.0
via Wikimedia Commons
Licence: https://creativecommons.org/licenses/by-sa/4.0

All other archive images are in the public domain.

Every other visual in this video is drawn from code.
```

## 3. Tagy

```
exercise, physical activity, sedentary lifestyle, evolutionary medicine,
hadza, bed rest study, deconditioning, bone density, insulin sensitivity,
vo2max, human evolution, sitting all day, walking, steps per day,
physiology, exercise science, health, daniel lieberman, herman pontzer,
constrained energy expenditure
```

## 4. Nastavení

| pole | hodnota |
|---|---|
| **jazyk videa** | **`en-gb`** — nastavit **PRVNÍ**, jinak zůstane dlaždice Titulky zašedlá |
| kategorie | Věda a technika |
| **byla použita AI** | **NE** — viz níž |
| licence | standardní licence YouTube |
| vkládání | **povolit** |
| viditelnost | nejdřív **neveřejné** a podívat se na to v přehrávači |

### Proč „byla použita AI" = NE

Rozhoduje **fotorealističnost, ne použití AI**
([pravidla](https://support.google.com/youtube/answer/14328491)):

- tři SDXL scény jsou díky kotvě stylu **malované ilustrace**, ne fotorealismus
- oba archivní snímky jsou upravené **jen barevně** — „color adjustment or
  lighting filters" je výslovná výjimka
- hudba je **procedurální** (sinusovky a šum v numpy), ne z generativního modelu

> Prohlášení se ptá na **obsah videa**, ne na náhled. Náhled je
> fotorealistický obrázek od ChatGPT (viz `thumbnail/PUVOD.md`) a na
> odpověď to nemá vliv.

## 5. Co musí uživatel naklikat sám

Podle toho, jak se video založí:

| | nahrál MP4 ručně (`--k-videu`) | `videos.insert` |
|---|---|---|
| prohlášení o AI | ✅ vyřídí průvodce | ❌ **ručně** |
| osvědčení o zproštění | ✅ vyřídí průvodce | ❌ **ručně** |
| **závěrečná obrazovka** | ❌ **ručně** | ❌ **ručně** |

Data API na závěrečnou obrazovku nemá ani zdroj, takže je ruční vždycky.
`nahraj.py` správný seznam po běhu vypíše sám.

**Místo na ni v obraze je.** `zaver_check.py` na skutečném `timing.json`:
okno posledních 20 s zabírají tři scény (S75, S76, S76b) a u obou
kreslených se dlaždice i kolečko vejdou s **0,0 % překryvu** vlevo nahoře.

## 6. Po zveřejnění

1. Video do playlistu — dopsat slug do `playlisty.json`, pak
   `analytics.py --videa` a `tools/playlisty.py`.
2. `python tools/titulky.py <adresář> --smaz-asr` — automatický přepis
   od YouTube konkuruje čtrnácti překladům a je z nich nejhorší.
   **V den nahrávání používej variantu na jedno video, ne `--vse`**:
   `--vse` stojí přes 4 500 jednotek, tedy víc než nahrání celého videa.
3. Odkaz a stav do **`Témata.ods`** — číslo 051 tam zatím vůbec není.

### Rozpočet kvóty

Denní strop je **10 000 jednotek na celý projekt**, ne na video, a můžou
si ho sebrat i paralelní sezení.

| operace | jednotek |
|---|---|
| `videos.insert` (jen když se nahrává přes API) | 1 600 |
| `thumbnails.set` | 50 |
| čtrnáct titulkových stop po 400 | **5 600** |
| `lokalizace.py` | 102 |
| `titulky.py --smaz-asr` na jedno video | ~150 |

Při ručně nahraném MP4 a `--k-videu` to vychází na **~5 900 jednotek**,
takže se to za den stihne. Přes `videos.insert` **7 500** a druhé video
už se ten den nevejde.
