# YouTube — 151 „How Precise Can Time Actually Be?“

Stav: **nahráno 2026-11-10** (https://youtu.be/W9WcZdSe9hw): nastavení, popis, náhled, lokalizace 13 jazyků a 15 titulkových stop přes API;
zveřejnění naplánované, závěrečná obrazovka a americká stopa doklikány (2026-11-10); zbývá `playlisty.py` po zveřejnění. Úklid hotový (draft, kopie na .207).

| | |
|---|---|
| ID videa | `W9WcZdSe9hw` |
| master | `render/final-en-151.mp4` (.207, 514,2 s, 1920×1080, dekódováno bez chyby) |
| náhled | ✅ C1 `TIME / WHAT IF IT JITTERS?`, `render/thumbnail.jpg` (`thumbnail/PUVOD.md`) |
| nastavení, popis, tagy | podklady níž |
| lokalizace | `youtube-preklady.md`, 13 jazyků, Codex A/B/C zapracován (`codex youtube-preklady.txt`) |
| titulky | `subtitles/<kód>.srt`, 14 jazyků + `en-US`, Codex v0.5 zapracován (cs, de při scénáři; 11 jazyků 2026-11-10) |
| americká stopa | `render/audio-en-US.m4a`, ručně ve Studiu |
| závěrečná obrazovka | S65–S68, **horní polovina** (viz níž) |
| karty | žádné |
| playlist | `fyzika` (*Physics That Sounds Simple Until You Ask*) |

**Co musí uživatel naklikat sám:** závěrečnou obrazovku, americkou audiostopu
(`render/audio-en-US.m4a`), titulky, které nejdou přes API, a osvědčení o zproštění, pokud ho nevyřídil průvodce nahráním.

Stopáž 8:34 (`work/timing.json` total 514,137 s).

> Kdyby se znovu pouštěl `tts.py`, přepočítej kapitoly tady i v `youtube-preklady.md`
> a přegeneruj `en-US` přes `us_stopa.py`.

Pořadí podle CENY (`docs/zverejneni.md`):

```bash
V=videos/151-how-precise-can-time-actually-be
python tools/nahraj.py $V --k-videu=<ID> --bez-titulku   # 100
python tools/analytics.py --videa                        #   1  ← nutné
python tools/lokalizace.py $V                            #  50
python tools/titulky.py $V --smaz-asr                    # 150  ← před titulky
python tools/titulky.py $V                               # 400×N
python tools/playlisty.py                                #  50
# úklid, až je MP4 na YouTube:
rm $V/render/draft*.mp4
ssh vrana@192.168.0.207 'rm -rf /home/vrana/temp/render-151-how-precise-can-time-actually-be'
```

---

## 1. Titul

```
How Precise Can Time Actually Be?
```

> Wh-otázka, 33 znaků, shodná s `project.json`. Odpověď (*maybe not infinitely precise*, S66) ani twist
> (nejvíc trpí nejmenší hodiny, S10) titul neprozrazuje.

---

## 2. Popis

```
In a laboratory in Boulder, Colorado, there is a clock so precise that over the entire age of the universe, its uncertainty would add up to less than a second. And every generation of clocks has been better than the last. So how far can this go? Is there a point where the problem isn't the clock any more, but time itself?

In 2025, physicists in Rome and Budapest published a calculation that puts a crack in the idea of perfectly sharp time. This video goes through how a clock actually works, how gravity changes the rate of time (measured over thirty-three centimetres, and then across a single millimetre), the measurement problem at the heart of quantum mechanics, collapse models, the idea of Roger Penrose and Lajos Diósi that gravity forces nature to choose, and what all of that would mean for every clock in the universe, including a twist nobody would have guessed.

Sources: Bortolotti, Curceanu, Diósi, Manti, Piscicchia, Fundamental Limits on Clock Precision from Spacetime Uncertainty in Quantum Collapse Models, Physical Review Research 7, 043166 (2025); Aeppli et al., A clock with 8 × 10⁻¹⁹ systematic uncertainty, Physical Review Letters 133, 023401 (2024); Chou, Hume, Rosenband, Wineland, Optical Clocks and Relativity, Science 329, 1630 (2010); Bothwell et al., Resolving the gravitational redshift across a millimetre-scale atomic sample, Nature 602, 420 (2022); Ghirardi, Rimini, Weber, Physical Review D 34, 470 (1986); Donadi et al., Underground test of gravity-related wave function collapse, Nature Physics 17, 74 (2021).

Subtitles are written for this video, not auto-generated. An American English audio track is available as a second audio track.

Full transcript, sources and translations: https://theresmoretoit-channel.github.io/videos/how-precise-can-time-actually-be/

CHAPTERS
00:00 The most precise clock
00:35 A crack in the assumption
01:07 Three pieces
01:19 How a clock works
01:47 Gravity and time
02:38 A very old quantum problem
03:15 Collapse models
03:49 Where gravity comes in
04:32 Putting it together
04:50 Pixels of time?
05:23 The twist
06:14 How big is the drift?
06:42 Today's best clocks
07:18 Why it matters
07:47 Under a mountain in Italy
08:10 So how precise can time be?

IMAGE CREDITS
Corno Grande da Campo Imperatore — Fiat 500e, CC BY 4.0
via Wikimedia Commons
Licence: creativecommons.org/licenses/by/4.0
All other archive images are in the public domain.
```

> **Blok se kopíruje CELÝ** (`docs/zverejneni.md`). Kredity: dva archivní snímky ze `sources.json` —
> S63 CC BY 4.0 (povinná atribuce, uvnitř bloku), S14 NIST public domain (jen souhrnná věta). Zbytek kreslený kódem.
>
> **Úvod drží opatrnost scénáře:** *uncertainty would add up to less than a second* (nejistota frekvence, ne „hodiny se
> rozejdou“, factcheck S01); *puts a crack in the idea* (S06), ne „dokázali, že čas kolísá“.
>
> **Pointa se neprozrazuje:** popis ani kapitoly neříkají, které hodiny trpí nejvíc (kapitola je jen *The twist*),
> jak malý efekt je (S52–S58) ani závěr S66–S67. *Pixels of time?* je otázka, odpověď (ne) dá video v S39.
>
> Kapitoly ze scén S01, S06, S11, S12, S16, S22, S27, S31, S37, S39, S44, S51, S54, S59, S63, S65
> (`work/timing.json`, zaokrouhleno dolů). První na 00:00, všechny ≥ 10 s (nejkratší S11 → S12, 11 s;
> S37 → S39 18 s; poslední S65 → konec 24 s). Otázka do komentářů (S68) vlastní kapitolu nemá.
> Výzvy k odběru (za S15 a S50) leží uvnitř kapitol.
>
> **Zdroje:** primární z `factcheck.md` ([B25], [A24], [C10], [Bo22], [GRW], [D20]). [D20] vyšel online 7. 9. 2020,
> ve svazku 17 (2021) — v popisu rok svazku, ve scénáři (S63) rok výsledku. [BIPM] je z paměti, v popisu není.
> *metre/millimetre* britsky jako scénář (hlas `bf_emma`).

---

## 3. Náhled

C1 z `thumbnail/ZADANI.md` (ChatGPT): kapesní hodinky s chvějící se červenou vteřinovou ručkou, `TIME / WHAT IF IT JITTERS?`.
`render/thumbnail.jpg`, původ v `thumbnail/PUVOD.md`.

---

## 4. Titulky

`subtitles/<kód>.srt` pro 14 jazyků a `en-US` (`codex 0.5 <kód>.txt`).
Jazyk videa **`en-gb`** (hlas `bf_emma`) nastaví `nahraj.py` dřív, než se nahrají titulkové stopy.

---

## 5. Nastavení

| | |
|---|---|
| kategorie | **Science & Technology** (28), posílá `nahraj.py` napevno |
| jazyk videa | `en-gb` |
| licence | standardní |
| pro děti | **ne** |
| komentáře | zapnuté (S68 je otázka do komentářů) |
| **byla použita AI** | **ne**. 66 ze 68 scén je kreslených kódem, žádná SDXL. Dva archivní snímky z Commons (S14 stronciové hodiny NIST, S63 Gran Sasso) jsou upravené jen barevně. Hudba je procedurální, hlas není klon skutečné osoby. |

### Závěrečná obrazovka

Od **8:34 − 20 s = 8:14**, tedy S66–S68 (S65 začíná v 8:10). `zaver_check` hlásí v obou dolních rozích
titulek; storyboard drží v S65–S68 prázdnou **horní polovinu** (osa sjíždí dolů, `OSA_ZAVER_Y`).
**Dlaždici i odběr dej do HORNÍ poloviny.** Jako dlaždici navrhuju **127 *What Would a Spoonful of a Neutron
Star Do?*** (navazuje na pulsar v S48, tentýž playlist), druhou nechat na „nejlepší pro diváka“.

---

## 6. Tagy

```
how precise can time be, atomic clock, optical clock, most precise clock, time dilation, gravitational time dilation,
quantum mechanics, measurement problem, collapse models, schrödinger's cat, penrose, diosi, diósi-penrose model,
gravity and time, is time quantized, physics of time, jila boulder, strontium clock, gran sasso, there's more to it
```

---

## 7. Playlist

**`fyzika`** (*Physics That Sounds Simple Until You Ask*), za 127.
Dopsat slug do `playlisty.json` až po zveřejnění, pak `analytics.py --videa` a `playlisty.py`.
Pinterest shortů: nástěnka playlistu `fyzika` (*Science & Physics*).
