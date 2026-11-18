# YouTube — 036 What Is GDP — And Why Doesn't It Tell You Everything?

Nahrává se `render/final-en.mp4` (master, ne draft), `render/thumbnail.jpg`
a `subtitles/*.srt` v devíti jazycích.

| co | stav |
|---|---|
| náhled | ✅ `render/thumbnail.jpg` — varianta **`a-hurikan`**, 1280×720, 356 kB |
| titulky | ✅ devět jazyků |
| lokalizace | ✅ `youtube-preklady.md`, osm jazyků |
| **master** | ❌ čeká na SDXL scény a render na herním PC |

## 1. Titul

```
What GDP Really Measures — And What It Doesn't
```

**Vybráno uživatelem 2026-09-09** ze čtyř variant. 46 znaků, tedy nad
mediánem kanálu (33), ale hluboko pod hranicí, za kterou YouTube titul
v seznamu utne (~60). Pomlčka precedent má — *„Linux — You Probably Use
It Already"*.

**Rozhodla dvojice titul + náhled, ne titul sám.** Náhled už se ptá
(`GDP` nahoře, zkáza uprostřed, `WHY DOES THIS COUNT?` dole), takže
titul má **slibovat odpověď**, ne položit tutéž otázku podruhé.

| varianta | znaků | proč ne |
|---|---|---|
| `Why GDP Doesn't Tell You Everything` | 35 | je to **závěr videa**; náhled se ptá na hurikán a titul odpovídá na něco jiného |
| **`What GDP Really Measures — And What It Doesn't`** | **46** | ✅ vybráno — náhled se ptá, titul slibuje obě poloviny odpovědi |
| `How Can GDP Go Up When Things Get Destroyed?` | 44 | prakticky **totéž, co už stojí v náhledu**; dvojice by řekla jednu věc dvakrát |
| `How Can a Hurricane Make GDP Go Up?` | 35 | původní návrh agenta, táž vada jako výš |
| `What Is GDP — And Why Doesn't It Tell You Everything?` | 52 | dodaný; začíná učebnicově |

> **Forma titulu CTR nerozhoduje, aspoň ne v datech kanálu.** Otázky jsou
> na obou koncích: nejlepší náhled je *„What Is Time, Actually?"* (2,26 %)
> a nejhorší *„Where Do Microplastics Come From?"* (0,36 %), a
> `docs/kanal-metriky.md` přisuzuje ten pád nečitelné pneumatice
> v náhledu, ne titulu. Proto rozhodovala dvojice, ne statistika.

## 2. Popis

```
A hurricane destroys thousands of houses. People lose their homes, roads
are damaged, businesses are wrecked. And GDP can go up.

That isn't a glitch. It is what the number was built to do: GDP measures
the market value of what gets produced, and rebuilding a town is
production. The destruction itself is recorded somewhere else entirely,
in an account that never touches GDP. All of the production is counted.
None of the destruction is subtracted.

This video works through what GDP actually measures and what it quietly
leaves out. Why nominal and real growth are not the same thing. Why an
average per person can hide almost everything. Why cooking dinner for
your family is worth nothing to the statistics, while paying a
restaurant fifty dollars for the same meal is worth fifty dollars.

And this is not a modern complaint. In a 1934 report to the US Senate,
Simon Kuznets — one of the people who built national income accounting
in the first place — wrote that the welfare of a nation can scarcely be
inferred from a measurement like this. He listed unpaid housework among
the things left outside.

None of which makes GDP useless. Quite the opposite. A reasonably
consistent thermometer beats no thermometer at all. The problem is
asking a thermometer to tell you your blood pressure.

Full transcript, sources and translations: https://theresmoretoit-channel.github.io/videos/what-gdp-doesnt-tell-you/

CHAPTERS
0:00 How a hurricane can raise GDP
0:27 What GDP actually measures
1:08 Why anyone cares
1:39 Back to the hurricane
2:31 Nominal and real
3:22 Per capita, and PPP
3:58 A flow, not a stock
4:37 The dinner nobody counts
5:32 Kuznets warned in 1934
6:02 What GDP cannot see
6:33 War, pollution, crime
7:14 So is GDP useless?
7:55 GDP is a thermometer
8:24 What three percent means

Subtitles are written for this video, not auto-generated. An American
English audio track is available as a second audio track.

SOURCES
System of National Accounts 2008 (EC, IMF, OECD, UN, World Bank) -
production boundary 6.26-6.30, welfare 1.75-1.84, catastrophic losses
12.46, PPP 15.199
Kuznets, S. (1934). National Income, 1929-32. Senate Document No. 124,
73rd Congress, 2nd Session
US Bureau of Economic Analysis, FAQ: how the national accounts are
affected by a disaster

IMAGE CREDITS
Destroyed homes and debris on Bolivar Peninsula - Jocelyn Augustino,
FEMA, public domain
Simon Kuznets, 1971 - Associated Press, public domain
Both via Wikimedia Commons.

If you want the next one, there is a subscribe button.
```

> **Atribuce je UVNITŘ bloku**, ne pod ním. `docs/zverejneni.md`:
> u čtyř videí ze šestnácti chyběla v popisu právě proto, že kredity
> visely jako poznámka pod blokem. Uživatel kopíruje jen text mezi
> trojicí zpětných apostrofů.
>
> Oba snímky jsou **public domain**, takže povinná atribuce podle licence
> není žádná — jsou uvedené ze slušnosti a protože jsou jen dva.
> `CC BY*` položku `sources.json` neobsahuje.

## 3. Tagy

```
GDP, gross domestic product, economics, economy, macroeconomics,
economic growth, Simon Kuznets, national accounts, unpaid work,
purchasing power parity, real GDP, recession, explainer
```

## 4. Nastavení

| pole | hodnota |
|---|---|
| jazyk videa | **`en-gb`** — nastavit NAPŘED, jinak zůstane dlaždice Titulky zašedlá |
| kategorie | **Science & Technology** (28) — posílá `nahraj.py` |
| pro děti | ne |
| **byla použita AI** | **ne** — posílá `nahraj.py` jako `containsSyntheticMedia: false` |
| **osvědčení o zproštění** | ✅ **ručně ve Studiu**, API na to pole nemá |
| **závěrečná obrazovka** | ✅ **ručně ve Studiu**, API na to nemá ani zdroj |
| playlist | dopsat do `playlisty.json` před `tools/playlisty.py` |

## Proč je odpověď na „byla použita AI" NE

- **SDXL scény jsou 4 ze 101** a díky kotvě stylu jsou to malované
  ilustrace, ne fotorealismus.
- **Archivní snímky jsou 2** a upravené jen barevně — „color adjustment
  or lighting filters" je výslovná výjimka v pravidlech YouTube.
- **Hudba je procedurální** (sinusovky a šum v numpy), ne z generativního
  modelu.
- Zbylých **95 scén je kreslených kódem**.

## Závěrečná obrazovka

Prvky patří do **horní poloviny obrazu** — dole sedí ambrový titulek
diagramu. Ověřeno `tools/zaver_check.py`: posledních dvacet sekund tvoří
**S97–S101** a dlaždice i kolečko mají v levém horním rohu **0,0 %
překryvu**. Do spodních rohů je nedávat, tam vedou přes titulek.

Do dlaždice patří **025 — How Does a War Economy Work?**, na které video
odkazuje v S74.

## Karta na video 025

S74 (`6:33`, věta *„There's a whole video about that one."*) je kotva
karty. Deska v obraze je zástupné místo — karta má vyskočit na slovech
*„whole video"*.

## Postup nahrání

Výchozí cesta je **ruční nahrání MP4 ve Studiu + `--k-videu`**, ne
`videos.insert` — ušetří 1 600 jednotek kvóty a průvodce ve Studiu se
sám zeptá na prohlášení o AI i na osvědčení o zproštění.

```bash
# 1) MP4 přetáhnout do Studia, zjistit ID
python tools/nahraj.py videos/036-what-gdp-doesnt-tell-you --k-videu <ID>
python tools/lokalizace.py videos/036-what-gdp-doesnt-tell-you --id <ID>
python tools/titulky.py videos/036-what-gdp-doesnt-tell-you --smaz-asr
```

> **Pořadí není libovolné.** `lokalizace.py` potřebuje `defaultLanguage`,
> a to pole Studio pod „jazykem videa" NENASTAVUJE. Posílá ho až
> `nahraj.py`, takže musí běžet první.

> **`titulky.py` volej ADRESÁŘEM, ne `--vse`.** `--vse` čerstvě nahrané
> video vůbec nevidí (čte `analytics/videa.json`) a stojí 4 550 jednotek
> místo 100.
