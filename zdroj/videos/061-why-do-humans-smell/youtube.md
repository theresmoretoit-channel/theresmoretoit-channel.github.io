# Podklady pro YouTube — 061

Video je hotové: master 11:00, náhled i čtrnáct jazyků titulků.
Americká stopa zatím NENÍ.

> **Kapitoly byly z draftu 0.6 a zastaraly tiše**, přesně jak tu bylo
> předem napsáno: přibylo devatenáct scén a stopáž narostla z 9:32 na
> 11:00, takže se všech čtrnáct časů posunulo až o osmdesát sekund.
> Přepočítány z `work/timing.json`, ne od oka.

---

## 1. Titul

```
Why Do Humans Smell?
```

Wh-otázka; kanál má naměřeno 2,23 % CTR proti 1,63 % u tvrzení.
Anglické *smell* navíc znamená **zároveň „páchnout" i „čichat"**, takže
titul nese obě poloviny videa naráz a divák neví, která platí.

## 2. Popis

```
Your sweat does not smell. Fresh out of the gland, what comes out under your arms is close to odourless: a large molecule with a sulphur atom wrapped up so that it cannot evaporate.

Then a bacterium finds it. It lives all over your skin, and in the armpit it has something to work on. One enzyme trims the wrapping, a second cuts the sulphur free, and the thing that floats away is the smell. Your body makes a component. The bacteria on your skin finish the job.

Some odour molecules register at a few parts per billion. So why would a body run a process whose entire output is thrown into the surrounding air? Because smell is information, and it is older than soap, older than cities, older than words.

A Scottish nurse called Joy Milne noticed that her husband had begun to smell different — woody, musky. Twelve years later he was diagnosed with Parkinson's. Researchers gave her twelve shirts, six worn by patients and six by people without the disease. She picked out all six. Then she picked out a seventh and would not back down. That person was diagnosed nine months later.

Plants do it too. Cut the leaves of a sagebrush and a wild tobacco plant growing beside it takes measurably less damage from grasshoppers and caterpillars. No nerves, no brain, no nose — and a range of under fifteen centimetres.

So why does any of this disgust us? Partly for good reason: rot, waste, infection. And partly because in 1919 an advertising agency had an awkward client, a sweat-blocking liquid called Odorono. A copywriter called James Webb Young found that two women in three did not think it was about them, so he stopped selling the liquid and started selling the problem. The advertisement ran in Ladies' Home Journal. Two hundred readers cancelled their subscriptions, and sales rose by a hundred and twelve percent in a single year.

None of which invented the shame. People had minded the smell for centuries. What 1919 invented was the sale.

And somebody is reading that signature. People reach for the word pheromone; in humans not one has ever been found. A dog does not need one. Four dogs in Belfast picked the stressed breath and sweat of the same person out of seven hundred and twenty trials, and got it right ninety-four per cent of the time. To the dog none of that is a failing — it is simply what today smells like.

Full transcript, sources and translations: https://theresmoretoit-channel.github.io/videos/why-do-humans-smell/

Chapters
0:00 Your sweat does not smell
1:25 A few molecules in every billion
1:42 Why broadcast at all?
2:09 What a smell tells other animals
2:28 The nurse who smelled Parkinson's
3:29 Everybody carries a different mixture
3:51 What the dog reads
4:37 Sagebrush warns the plant beside it
5:11 Why any of it disgusts us
5:52 1919: the year somebody sold the problem
7:11 Washing, shaving, silver in the socks
7:33 The pump, and the people it skips
8:00 The test
8:47 What you were taught
9:02 Hygiene and odour are not the same thing
9:46 Back to the molecules

Subtitles are written for this video, not auto-generated.

Music is generated procedurally for this channel.

The archive image in this video is in the public domain.
```

**Kapitol je šestnáct**, první na `0:00`, nejkratší trvá **15 s** —
YouTube žádá aspoň tři a každou ≥ 10 s. Časy jsou z `work/timing.json`,
ne od oka. Dvě kapitoly přibyly s novými bloky: *What the dog reads*
(S44b) a *What you were taught* (S87b).

> **IMAGE CREDITS tu schválně NENÍ.** Video má jedinou archivní scénu
> (S46, pelyněk) a ta je **public domain**, takže povinná atribuce
> žádná není. `docs/zverejneni.md` říká, že public domain snímky se
> vypisovat nemusí — vypisovat jeden kvůli formě dělá jen šum. Věta
> o public domain v bloku zůstává, aby bylo poznat, že se na to
> nezapomnělo.
>
> **Kdyby se archivní scéna přidala nebo vyměnila, tohle se musí
> přepsat.** Kontrola: projít `sources.json` a ověřit, že žádná
> položka nemá licenci `CC BY*`.

## 3. Náhled

`render/thumbnail.jpg` — kuličkový deodorant s odklopeným víčkem,
nahoře `SWEAT`, dole `WHAT MAKES THE SMELL?`. Dodal uživatel, agent
přesadil uříznutý nadpis. Evidence v `thumbnail/PUVOD.md`.

## 4. Titulky

Hotových **čtrnáct jazyků** (en 184 titulků, ostatní 237 az 241).
Jazyk videa se nastavuje **`en-gb`**, protože hlas je `bf_emma` —
a musí se nastavit **dřív** než se nahrávají titulky, jinak zůstane
dlaždice Titulky ve Studiu zašedlá.

## 5. Lokalizované názvy a popisy

`youtube-preklady.md`, třináct jazyků bez `en`. Nahrává
`tools/lokalizace.py` jediným voláním za **50 jednotek** kvóty.

## 6. Tagy

```
smell, body odour, body odor, sweat, apocrine, skin bacteria, olfaction, Joy Milne, Parkinson's, plant communication, sagebrush, Odorono, advertising history, deodorant, hygiene, science communication, there's more to it
```

## 7. Nastavení

| | |
|---|---|
| jazyk videa | **`en-gb`** (nastavit PRVNÍ) |
| kategorie | Věda a technika |
| licence | standardní |
| vkládání | **povolit** |
| pro děti | ne |
| AI obsah | **ne** — viz níž |

**Prohlášení o AI: odpověď je ne**, a drží ji tytéž tři věci jako
u zbytku kanálu: SDXL scény jsou díky kotvě stylu malované ilustrace,
archivní snímek je upravený jen barevně (*„color adjustment or lighting
filters"* je výslovná výjimka) a hudba je procedurální, ne z
generativního modelu.

> **Ale u dvou scén to stojí za pohled tvým okem, ne mým.** S76
> (lékárenské lahvičky) a S104 (vypraná košile) jsou ze všech pěti
> SDXL scén nejblíž fotografii. Pravidla YouTube se ptají na
> **fotorealističnost**, ne na použití AI, a rozhodující je, že to
> nejsou konkrétní skutečná místa ani události — ale je to tvůj podpis
> pod prohlášením, tak ať víš, kterých dvou scén se to týká.

## 8. Co musí uživatel naklikat sám

Podle toho, jak se video založí:

| | ručně nahrané MP4 (`--k-videu`) | `videos.insert` |
|---|---|---|
| prohlášení o AI | ✅ vyřídí průvodce | ❌ **ručně** |
| osvědčení o zproštění | ✅ vyřídí průvodce | ❌ **ručně** |
| **závěrečná obrazovka** | ❌ **ručně** | ❌ **ručně** |

Závěrečnou obrazovku API neumí vůbec. **Místo na ni je připravené**:
`zaver_check.py` hlásí u všech pěti scén v okně (S106–S110) překryv
**0,0 %** v horní polovině.

## 9. Pořadí nahrávání se řídí CENOU

```bash
python tools/nahraj.py videos/061-why-do-humans-smell --k-videu <ID> --bez-titulku
python tools/lokalizace.py videos/061-why-do-humans-smell
python tools/titulky.py videos/061-why-do-humans-smell
python tools/titulky.py videos/061-why-do-humans-smell --smaz-asr
```

Za 150 jednotek je hotové všechno kromě titulků; ty stojí **400 za
jazyk**. Když kvóta dojde uprostřed nich, chybí jen ocas a dobere se
druhý den přes `--jen`.

## 10. Po zveřejnění

Dopsat slug do `playlisty.json`, spustit `analytics.py --videa`
a pak `tools/playlisty.py`.
