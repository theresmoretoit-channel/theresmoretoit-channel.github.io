# YouTube — 123 „Why Does Almost Every Culture Have Gods?“

Stav: **master hotový, nenahráno.** Stav zveřejnění je v `Témata.fods`.

| | |
|---|---|
| ID videa | ⬜ (po ručním nahrání MP4 ve Studiu) |
| master | ✅ `render/final-en-123.mp4` (7:43, 1920×1080, `ffprobe` 462,64 s) |
| náhled | ✅ `render/thumbnail.jpg` (koncept A, prázdná židle) |
| nastavení, popis, tagy | podklady níž |
| lokalizace | `youtube-preklady.md`, 13 jazyků |
| titulky | `subtitles/*.srt`, 14 jazyků + `en-US`, až po Codexu |
| americká stopa | `render/audio-en-US.m4a`, ručně ve Studiu |
| závěrečná obrazovka | od **7:22**, S49–S50, prvky **nahoru** (viz níž) |
| **karta** | **na 068 *Why Do People Still Believe in God?* v čase 1:29 (S10)** — ručně ve Studiu |
| playlist | `lide` (*Why We Do What We Do*), na konec |

**Co musí uživatel naklikat sám:** kartu na 068 v 1:29, závěrečnou
obrazovku, americkou audiostopu (`render/audio-en-US.m4a`) a osvědčení
o zproštění, pokud ho nevyřídil průvodce nahráním.

Stopáž 7:43 (`work/timing.json` total 462,6 s).

> Kdyby se znovu pouštěl `tts.py`, přepočítej kapitoly tady
> i v `youtube-preklady.md`, čas karty a přegeneruj `en-US` přes `us_stopa.py`.

Pořadí podle CENY (`docs/zverejneni.md`):

```bash
V=videos/123-why-does-almost-every-culture-have-gods
python tools/nahraj.py $V --k-videu=<ID> --bez-titulku   # 100
python tools/analytics.py --videa                        #   1  ← nutné
python tools/lokalizace.py $V                            #  50
python tools/titulky.py $V --smaz-asr                    # 150  ← před titulky
python tools/titulky.py $V                               # 400×15
python tools/playlisty.py                                #  50
# úklid, až je MP4 na YouTube:
rm $V/render/draft*.mp4
ssh vrana@192.168.0.207 'rm -rf /home/vrana/temp/render-123-why-does-almost-every-culture-have-gods'
```

---

## 1. Titul

```
Why Does Almost Every Culture Have Gods?
```

> Wh-otázka, 40 znaků, shodná s `project.json` a `Témata.fods`. Odpověď
> titul neprozrazuje.

---

## 2. Popis

```
A child is left alone in a room with a game that is almost impossible to win honestly. Before the game, the researcher points to an empty chair and says an invisible princess is sitting in it. Then he leaves, and reminds the child that she is watching.

Almost every culture we know of has spirits, ancestors or gods. But for most of human history, the greatest gods people believed in probably weren't moral judges. So this video asks two questions: why do humans imagine invisible minds so easily, and when did those minds start watching us?

Along the way: a puppet show with a baby mouse and an alligator, hunter-gatherer societies whose high gods mostly stayed out of human affairs, the psychologist Ara Norenzayan's idea of "big gods", a coin game played with 591 people in eight communities from Fiji to Tanzania, and a huge study that tried to settle which came first: big gods or big societies.

Why we believe something and whether it's true are separate questions. This video is about the first one.

Sources: Piazza, Bering & Ingram (2011), Journal of Experimental Child Psychology; Bering & Bjorklund (2004), Developmental Psychology; Peoples & Marlowe (2012), Human Nature; Swanson's High Gods coding, Standard Cross-Cultural Sample (D-PLACE); Watts et al. (2015), Proceedings of the Royal Society B; Norenzayan, Big Gods (2013); Purzycki et al. (2016), Nature; Whitehouse et al. (2019), Nature (retracted 2021); Beheim et al. (2021), Nature; Whitehouse et al. (2022), Religion, Brain & Behavior; World Values Survey / European Values Study 2017–2022 (via Our World in Data); Special Eurobarometer 225 (2005).

Subtitles are written for this video, not auto-generated. An American English audio track is available as a second audio track.

CHAPTERS
00:00 Princess Alice is watching
00:55 Two questions
01:27 A mind without a body
02:38 Hunter-gatherers and their gods
03:16 Trusting strangers
03:59 Can it be tested?
04:57 Which came first?
05:29 Two years later
06:10 The honest state of things
06:26 One more twist
06:49 So why gods?
```

> **Blok se kopíruje CELÝ** (`docs/zverejneni.md`). **Archivní snímky
> video nemá** (48 diagramů kreslených kódem + 2 SDXL scény, žádné
> `sources.json` ani `CREDITS.md`), takže `IMAGE CREDITS` tu není.
> Náhled je obrázek z ChatGPT bez cizí fotky, atribuci nepotřebuje.
>
> **Pointa se neprozrazuje.** Popis položí obě otázky a jmenuje studii
> z roku 2019 jen jako pokus *„which came first“*; neříká, jak spor
> dopadl (S36–S42), skandinávský obrat (S43–S44) ani závěr, že úplnou
> odpověď nemáme (S46–S48). Jediná stopa je `(retracted 2021)` v řádku
> zdrojů — citovat stažený článek bez označení by bylo horší.
>
> **Nic netvrdí víc než video** (`notes.md`, `factcheck.md`): bohové
> „probably weren't moral judges“ (S08), vysocí bohové „mostly stayed out
> of human affairs“ (S18–S19, kat. 1+2), „big gods“ jako *idea*
> Norenzayana, ne zjištění, žádná příčinná vazba bohové → společnosti.
> Alice představena **před** hrou, připomínka při odchodu (factcheck
> S02–S03); „a game almost impossible to win honestly“ odpovídá třem
> pravidlům (S01). Opravené formulace („one rule“, „still thinking“,
> „the cities came first“, „nobody knew“, Hadzové) se nevracejí.
>
> Kapitoly ze scén S01, S07, S10, S18, S22, S28, S34, S37, S42, S43, S45
> (`work/timing.json`, zaokrouhleno dolů). Nejkratší 16 s (S42 → S43),
> první na 00:00, všechny ≥ 10 s. Výzvy k odběru (za S10 a S33) leží
> uvnitř kapitol.
>
> Zdroje odpovídají `factcheck.md`; 591 a osm komunit je tatáž hodnota
> jako ve scénáři (S29).

---

## 3. Náhled

`render/thumbnail.jpg` — koncept A (prázdná židle, GODS / WHO SITS HERE?),
obrázek z ChatGPT, původ v `thumbnail/PUVOD.md`. Záloha pro Test & Compare:
koncept B (`thumbnail/ZADANI.md`).

---

## 4. Titulky

`subtitles/*.srt`, 14 jazyků + `en-US`. Jazyk videa **`en-gb`** (hlas
`bf_emma`) se musí nastavit dřív, než se nahrají titulkové stopy.
Nahrávají se až po Codexu.

---

## 5. Nastavení

| | |
|---|---|
| kategorie | **Science & Technology** (28) — posílá `nahraj.py` napevno |
| jazyk videa | `en-gb` |
| licence | standardní |
| pro děti | **ne** |
| komentáře | zapnuté (S50 končí otázkou do komentářů) |
| **byla použita AI** | **ne**. 48 scén je kreslených kódem; 2 SDXL scény (S07 police s hliněnými figurkami, S22 město ve svahu za zamračeného dne, drobné postavy bez tváří) jsou malované ilustrace podle kotvy stylu, ne fotorealismus ani konkrétní skutečné místo či událost. Archiv žádný, hudba procedurální, hlas není klon. |

### Karta

Na video **068 *Why Do People Still Believe in God?*** (`MeOQtxC7FY4`)
v čase **1:29** — S10 *„Part of the first answer came up in an earlier
video.“* začíná v 87,8 s, slovo *earlier* zazní v 89,6 s. Karty API
neumí, naklikává se ve Studiu (Karty → Video). Volitelný text upoutávky
např. *„Brains built to detect minds“*.

Výzva k odběru (bez hlasu) běží vlevo dole hned za S10 (~1:36–1:40);
karta je v pravém horním rohu, nekříží se.

### Závěrečná obrazovka

Od **7:22** (posledních 20 s z 462,6), tedy S49 (od 442,5 s) a S50.
`zaver_check` u obou hlásí volnou **horní polovinu** (místnost s židlí
a karta otázky leží dole), **dlaždici i kolečko odběru dej nahoru**.
Jako dlaždici doporučuju **073 *What Would It Take to Prove God?***
(`6IuuXCygHY0`) — navazuje na S45 *„Why we believe something and
whether it's true are separate questions“*; 068 už má kartu. Druhou
dlaždici nechat na „nejlepší pro diváka“.

---

## 6. Tagy

```
why does every culture have gods, origin of religion, cognitive science of religion,
big gods, ara norenzayan, princess alice experiment, moralizing gods,
supernatural punishment, hunter-gatherer religion, high gods, seshat,
religion and trust, evolution of religion, psychology of belief,
invisible minds, explainer, there's more to it
```

---

## 7. Playlist

**`lide`** (*Why We Do What We Do*), na konec, za 085. Je tam celá
„boží“ řada 068 → 073 → 085 i 057 (keř a predátor), na kterou video
navazuje; 123 je kognitivní a antropologické vysvětlení víry, tedy
přesně popis playlistu (*beliefs that look irrational from the outside*).
Alternativa `spolecnost` (velcí bohové a důvěra v cizí lidi, S22–S44).
**Do `playlisty.json` NEZAPSÁNO** — zapsat při nahrání; `playlisty.py`
ho stejně přeskočí, dokud video není v `analytics/videa.json`.
