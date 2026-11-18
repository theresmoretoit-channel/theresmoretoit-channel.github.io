# YouTube — 127 „What Would a Spoonful of a Neutron Star Do?“

Stav: **MP4 nahráno ručně ve Studiu 2026-10-30 (master z 20:22, s opravami S22/S34); metadata, lokalizace, 15 titulkových stop, playlisty a náhled nahrané.** Stav zveřejnění je v `Témata.fods`.

| | |
|---|---|
| ID videa | `bMX7Mr6WsF0` |
| master | ✅ `render/final-en-127.mp4` (9:38, 1920×1080, 578,5 s) |
| náhled | ✅ `render/thumbnail.jpg` z konceptu A (`thumbnail/PUVOD.md`), nahráno |
| nastavení, popis, tagy | podklady níž |
| lokalizace | `youtube-preklady.md`, 13 jazyků |
| titulky | `subtitles/*.srt`, 14 jazyků + `en-US` (Codex hotový, nahráno) |
| americká stopa | `render/audio-en-US.m4a`, ručně ve Studiu |
| závěrečná obrazovka | od **9:18**, S73–S74, prvky **nahoru** (viz níž) |
| karta | žádná (scénář na starší video neodkazuje) |
| playlist | `fyzika` (*Physics That Sounds Simple Until You Ask*) a `vesmir`, na konec |

**Co musí uživatel naklikat sám:** závěrečnou obrazovku, americkou
audiostopu (`render/audio-en-US.m4a`) a osvědčení o zproštění, pokud ho
nevyřídil průvodce nahráním.

Stopáž 9:38 (`work/timing.json` total 578,50 s).

> Kdyby se znovu pouštěl `tts.py`, přepočítej kapitoly tady
> i v `youtube-preklady.md` a přegeneruj `en-US` přes `us_stopa.py`.

Pořadí podle CENY (`docs/zverejneni.md`):

```bash
V=videos/127-what-would-a-spoonful-of-a-neutron-star-do
python tools/nahraj.py $V --k-videu=bMX7Mr6WsF0 --bez-titulku          # 100
python tools/analytics.py --videa                               #   1  ← nutné
python tools/lokalizace.py $V                                   #  50
python tools/titulky.py $V --smaz-asr                           # 150  ← před titulky
python tools/titulky.py $V                                      # 400×15
python tools/playlisty.py                                       # 100
# úklid, až je MP4 na YouTube:
rm $V/render/draft*.mp4
ssh vrana@192.168.0.207 'rm -rf /home/vrana/temp/render-127-what-would-a-spoonful-of-a-neutron-star-do'
```

---

## 1. Titul

```
What Would a Spoonful of a Neutron Star Do?
```

> Wh-otázka, 43 znaků, shodná s `project.json`. Odpověď (lžička by se
> prudce rozepnula, S35–S37) titul neprozrazuje.

---

## 2. Popis

```
On Earth, a single teaspoon of neutron-star matter would weigh billions of tonnes, several times the mass of every person alive. How can that much mass fit into a teaspoon? And if you could somehow bring a spoonful here, what would it actually do?

This video works through it layer by layer: why ordinary matter is mostly empty space, what keeps an atomic nucleus from flying apart, how a dying star crushes a core the size of the Earth down to the size of a city in less than a second, and what the thing left behind is really made of.

Along the way: nuclear pasta, the collision of two neutron stars that telescopes all over the world turned to watch in 2017, where some of the gold on Earth may have come from, why the three quarks inside a proton add up to only about one percent of its mass, and a number with no units that nobody can explain.

Sources: J. M. Lattimer & M. Prakash (2004), The Physics of Neutron Stars, Science; N. Chamel & P. Haensel (2008), Physics of Neutron Star Crusts, Living Reviews in Relativity; LIGO Scientific Collaboration, Virgo Collaboration et al. (2017), Multi-messenger Observations of a Binary Neutron Star Merger, Astrophysical Journal Letters 848, L12; D. Watson et al. (2019), Identification of strontium in the merger of two neutron stars, Nature 574, 497; D. Kasen et al. (2017), Origin of the heavy elements in binary neutron-star mergers from a gravitational-wave event, Nature 551, 80; S. Dürr et al. (2008), Ab Initio Determination of Light Hadron Masses, Science 322, 1224; Y.-B. Yang et al. (2018), Proton Mass Decomposition from the QCD Energy Momentum Tensor, Physical Review Letters 121, 212001; CODATA recommended values (NIST), fine-structure constant; BIPM, 17th CGPM (1983), Resolution 1, definition of the metre.

Subtitles are written for this video, not auto-generated. An American English audio track is available as a second audio track.

IMAGE CREDITS
Blue Gene/P supercomputer rack — unknown author (uploaded by Raul654), CC BY-SA 3.0
Mètre-étalon, Paris — LPLT, CC BY-SA 3.0
via Wikimedia Commons
Licences: creativecommons.org/licenses/by-sa/3.0
NGC 4993 and the afterglow of GRB 170817A — NASA and ESA (Hubble Space Telescope)
All other archive images are in the public domain.

Full transcript, sources and translations: https://theresmoretoit-channel.github.io/videos/what-would-a-spoonful-of-a-neutron-star-do/

CHAPTERS
00:00 A teaspoon of a neutron star
00:24 Mostly empty space
01:13 What holds a nucleus together
02:04 How a star collapses
02:55 What's left behind
04:01 A spoonful on Earth
04:43 2017: two neutron stars collide
05:30 Why does it weigh anything?
06:45 Numbers the theory can't predict
07:51 A number with no units
08:47 Back to the teaspoon
```

> **Blok se kopíruje CELÝ** (`docs/zverejneni.md`). Archiv má čtyři
> snímky (`CREDITS.md`): **dva CC BY-SA 3.0** (S55 Blue Gene/P, autor
> neuveden, uploader Raul654 — rozhodl uživatel, že snímek zůstává;
> S60 mètre-étalon, LPLT), oba v TASL uvnitř bloku. S41 (Hubble, NASA
> a ESA) a S51 (Einstein, Schmutzer) jsou public domain; NASA/ESA je
> uvedená jako zdvořilost.
>
> **Pointa se neprozrazuje.** Popis položí obě otázky ze S04–S05 a jmenuje
> témata, ne odpověď (prudké rozepnutí a energie víc než asteroid, S35–S37;
> hmotnost z energie polí, S49–S53). Jediná konkrétní odpověď je
> „about one percent“ (S48), formulovaná jako otázka „proč“.
>
> **Nic netvrdí víc než video** (`factcheck.md`): miliardy tun a násobek
> hmotnosti lidstva (S02–S03), jádro velké jako Země → město za méně než
> sekundu (S21, S23), 2017 a dalekohledy po celém světě (S38–S40),
> „some of the gold … may have been made“ (S43), jedno procento (S48),
> bezrozměrná konstanta bez vysvětlení (S62–S66).
>
> Kapitoly ze scén S01, S06, S13, S20, S26, S34, S38, S44, S55, S62, S69
> (`work/timing.json`, zaokrouhleno dolů). Nejkratší má 48 s (S01 → S06),
> poslední 50 s (S69 → konec), všechny ≥ 10 s. Výzvy k odběru (za S19
> a S43) leží uvnitř kapitol.
>
> Zdroje jsou z `factcheck.md` (primární články); sekundární a zdroje
> k okrajovým číslům (populace, Chicxulub) se neuvádějí.

---

## 3. Náhled

Koncept **A** z `thumbnail/ZADANI.md` (lžička se svítící hmotou,
NEUTRON STAR / WHAT WOULD IT DO?), obrázek z ChatGPT. Původ, otisk
a `thumb_check` v `thumbnail/PUVOD.md`; nahráno 2026-10-30.

---

## 4. Titulky

`subtitles/*.srt`, 14 jazyků + `en-US`. Jazyk videa **`en-gb`** (hlas
`bf_emma`) se musí nastavit dřív, než se nahrají titulkové stopy.
Nahrávají se **až po zapracování nálezů Codexu**.

---

## 5. Nastavení

| | |
|---|---|
| kategorie | **Science & Technology** (28), posílá `nahraj.py` napevno |
| jazyk videa | `en-gb` |
| licence | standardní |
| pro děti | **ne** |
| komentáře | zapnuté (S74 končí otázkou do komentářů) |
| **byla použita AI** | **ne**. Tři SDXL scény (S20 hmotná hvězda, S25 supernova, S39 dvě neutronové hvězdy před srážkou) jsou malované ilustrace podle kotvy stylu, ne fotorealismus. S39 se sice týká skutečné události (GW170817), ale je to stylizovaná kresba dvou svítících koulí, ne realisticky vypadající záznam — srážku nikdo nevyfotil a obraz se za snímek nevydává. Archivní snímky jsou upravené jen barevně, 67 scén je kresba kódem (14 animovaných). Hudba procedurální, hlas není klon. |

### Závěrečná obrazovka

Od **9:18** (posledních 20 s z 578,5), tedy konec S73 (od 555,5 s)
a S74 (od 564,0 s). `zaver_check` u obou hlásí volný **horní levý roh**
(dole je titulek), **dlaždici i kolečko odběru dej nahoru**. Jako
dlaždici doporučuju **008 *What Is Time, Actually?*** (`LP_MJkgG4vA`):
další otázka, u které se pod jednoduchou odpovědí otevře „nikdo neví“.
Alternativa **111 *What Would It Take to Travel Faster Than Light?***
(`zGxKaV9OROE`): rychlost světla ze S59–S61 a táž vesmírná linka.

---

## 6. Tagy

```
what would a spoonful of a neutron star do, neutron star, teaspoon of neutron star,
neutron star matter, nuclear pasta, strong interaction, supernova, GW170817,
kilonova, gold from neutron stars, proton mass, quarks, higgs field,
fine-structure constant, 1/137, fundamental constants, physics explainer,
there's more to it
```

---

## 7. Playlist

**`fyzika`** (*Physics That Sounds Simple Until You Ask*), na konec za 114,
a duálně **`vesmir`** (*Space — Getting There, and Who Else Is Out There*),
na konec za 125. Duální členství má precedens (029/032 v `vesmir`
i `mysli`); `playlisty.py` jen přidává.
