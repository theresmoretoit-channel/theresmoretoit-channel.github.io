# YouTube — 152 „Why Do Humans Keep Inventing Drugs?“

Stav: **nahráno 2026-11-10** (https://youtu.be/1t657P3T4-I), nastavení, popis, tagy a náhled přes `nahraj.py`. Titulky en, cs, sv, es, pt-BR, de, fr, it vloženy; u `pl` došla kvóta. **Zbývá (po 9:00):** `titulky.py --jen pl id tr uk vi fi en-US`, `lokalizace.py` (až po nálezech Codexu k `youtube-preklady.md`), ve Studiu americká stopa a závěrečná obrazovka, po zveřejnění `playlisty.py`.

| | |
|---|---|
| ID videa | `1t657P3T4-I` |
| master | `render/final-en-152.mp4` (.207, 3× supersampling, 692,1 s, 1920×1080, 52 MB, dekódováno bez chyby) |
| náhled | ✅ C1 `DRUGS / IS THIS ONE TOO?`, `render/thumbnail.jpg` (`thumbnail/PUVOD.md`) |
| nastavení, popis, tagy | podklady níž |
| lokalizace | `youtube-preklady.md`, 13 jazyků |
| titulky | `subtitles/<kód>.srt`, 14 jazyků + `en-US`, Codex v0.4 (cs, de) a v0.5 (11 jazyků) zapracován |
| americká stopa | `render/audio-en-US.m4a`, ručně ve Studiu |
| závěrečná obrazovka | S89–S91, **horní polovina** (viz níž) |
| karty | žádné |
| playlist | `lide` |

**Co musí uživatel naklikat sám:** závěrečnou obrazovku, americkou audiostopu
(`render/audio-en-US.m4a`), titulky, které nejdou přes API, a osvědčení o zproštění, pokud ho nevyřídil průvodce nahráním.

Stopáž 11:32 (`work/timing.json` total 692,098 s).

> Kdyby se znovu pouštěl `tts.py`, přepočítej kapitoly tady i v `youtube-preklady.md`
> a přegeneruj `en-US` přes `us_stopa.py`.

Pořadí podle CENY (`docs/zverejneni.md`):

```bash
V=videos/152-why-do-humans-keep-inventing-drugs
python tools/nahraj.py $V --k-videu=<ID> --bez-titulku   # 100
python tools/analytics.py --videa                        #   1  ← nutné
python tools/lokalizace.py $V                            #  50
python tools/titulky.py $V --smaz-asr                    # 150  ← před titulky
python tools/titulky.py $V                               # 400×N
python tools/playlisty.py                                #  50
# úklid, až je MP4 na YouTube:
rm $V/render/draft*.mp4
ssh vrana@192.168.0.207 'rm -rf /home/vrana/temp/render-152-why-do-humans-keep-inventing-drugs'
```

---

## 1. Titul

```
Why Do Humans Keep Inventing Drugs?
```

> Wh-otázka, 35 znaků, shodná s `project.json`. Odpověď (S85–S87: první vynalezly rostliny jako zbraně
> proti hmyzu, fungují na nás kvůli společným prastarým dílům a táhnou nás zpátky přes systém učení)
> titul neprozrazuje.

---

## 2. Popis

```
More than twelve thousand years ago, in what is now Utah, someone sat by a fire and left behind a few tobacco seeds. About eight thousand years ago, people in the Andes were chewing coca leaves. And about nine thousand years ago, in a village in China, people were brewing a drink from rice, honey and fruit. These people never met, and yet each of them found a plant that changes how a human brain works. Why does every human society find a way to change its own mind? And why does a plant contain a molecule that fits a human brain at all?

This video goes through caffeine-fed caterpillars and bees, how drugs led scientists to the brain's own opioids and cannabinoids, what dopamine really does, the mutation that let our ape ancestors break down alcohol, why most people who try a drug don't get hooked, coffee bans in Mecca and England, the pharmacist who isolated morphine, the Bayer chemist who made aspirin and heroin eleven days apart, the legal loophole of new psychoactive substances, and psilocybin on prescription in Australia.

Sources: Duke et al., Nature Human Behaviour (2021); Dillehay et al., Antiquity (2010); McGovern et al., PNAS (2004); Ren et al., Science Advances (2019); Nathanson, Science (1984); Nathanson et al., PNAS (1993); Wright et al., Science (2013); Carrigan et al., PNAS (2015); Anthony, Warner & Kessler, Experimental and Clinical Psychopharmacology (1994); Lasker Foundation, Opiate receptors and enkephalins; Devane et al., Science (1992); European Union Drugs Agency, European Drug Report (2025); Australian Therapeutic Goods Administration, psilocybin and MDMA rescheduling (2023).

Subtitles are written for this video, not auto-generated. An American English audio track is available as a second audio track.

CHAPTERS
00:00 Tobacco seeds by an ancient fire
01:04 Plants fight with chemistry
01:57 Why it works on us too
02:40 Caffeine for bees
03:08 Why would a brain want a poison?
03:31 A lock for a poppy
04:18 Hijacked systems
04:42 What dopamine really does
05:03 The alcohol mutation
05:41 Who gets hooked?
06:18 Not chasing a high
06:59 Coffee bans
07:48 From plant to pill
08:32 Aspirin and heroin
08:53 New molecules, new loopholes
09:52 What do we want our brains to do?
10:37 So why?

IMAGE CREDITS
All archive images are in the public domain, via Wikimedia Commons.
```

> **Blok se kopíruje CELÝ** (`docs/zverejneni.md`). Kredity: všechny tři archivní snímky ze `sources.json`
> (S62 londýnská kavárna, S66 Sertürner, S72b lahvička Heroin) jsou public domain, jmenovitá atribuce není povinná.
> SDXL scény video nemá, zbytek je kreslený kódem.
>
> **Pointa se neprozrazuje:** popis ani kapitoly neříkají S85–S87 ani S83 (*the line … isn't written in
> the molecule. We draw it.*). Kapitola 01:04 *Plants fight with chemistry* odpovídá S11, kde to video říká
> už v první minutě; závěrečné spojení všech tří důvodů je až v *So why?*.
>
> Kapitoly ze scén S01, S09, S16, S21, S25, S28, S35, S39, S42, S48, S53, S59, S65, S71, S73, S79, S84
> (`work/timing.json`, zaokrouhleno dolů). První na 00:00, všechny ≥ 10 s (nejkratší S71 → S73, 21 s;
> S25 → S28 23 s; poslední S84 → konec 54 s). Otázka do komentářů (S91) vlastní kapitolu nemá.
> Výzvy k odběru (za S15 a S47) leží uvnitř kapitol.
>
> **Zdroje:** primární studie a instituce z `factcheck.md`, kapitola Zdroje. Popularizační zprostředkovatelé
> (KSL, EurekAlert, PopSci, Wikipedia) v popisu nejsou, uvádí se původní práce. Anandamid je Devane et al. 1992,
> na kterou vede odkaz PMC47201.

---

## 3. Náhled

C1 z `thumbnail/ZADANI.md` (ChatGPT): bílý šálek espressa na tmavém kameni, `DRUGS / IS THIS ONE TOO?`.
`render/thumbnail.jpg`, původ v `thumbnail/PUVOD.md`.

---

## 4. Titulky

`subtitles/<kód>.srt` pro 14 jazyků a `en-US` (`codex 0.4 <kód>.txt`, `codex 0.5 <kód>.txt`).
Jazyk videa **`en-gb`** (hlas `bf_emma`) nastaví `nahraj.py` dřív, než se nahrají titulkové stopy.

---

## 5. Nastavení

| | |
|---|---|
| kategorie | **Science & Technology** (28), posílá `nahraj.py` napevno |
| jazyk videa | `en-gb` |
| licence | standardní |
| pro děti | **ne** |
| komentáře | zapnuté (S91 je otázka do komentářů) |
| **byla použita AI** | **ne**. 89 z 92 scén je kreslených kódem, žádná SDXL. Tři archivní snímky z Commons (S62, S66, S72b) jsou upravené jen barevně. Hudba je procedurální, hlas není klon skutečné osoby. |

> **Téma drogy a vhodnost pro inzerenty:** video je výkladové (historie, farmakologie, regulace), nikoho
> k užívání nenavádí a neukazuje užívání ani přípravu. V dotazníku vhodnosti pro inzerenty proto
> **„Recreational drugs and drug-related content“ = ne/nepropaguje**, vzdělávací kontext.

### Závěrečná obrazovka

Od **11:32 − 20 s = 11:12**, tedy S89–S91. `zaver_check` hlásí v obou dolních rozích titulek.
**Dlaždici i odběr dej do HORNÍ poloviny.** Jako dlaždici navrhuju **147 *Why Can't You Stop Scrolling?***
(dopamin jako učitel, S39–S41; tentýž playlist), druhou nechat na „nejlepší pro diváka“.
Alternativa: 105 *What Really Happens After 16 Hours Without Food?* (playlist `telo`).

---

## 6. Tagy

```
why do humans use drugs, history of drugs, psychoactive plants, caffeine, nicotine, cocaine, opium, morphine,
heroin, endorphins, anandamide, dopamine, addiction, why plants make caffeine, plant chemical defence,
drunken monkey hypothesis, coffee ban history, bayer heroin aspirin, new psychoactive substances, psilocybin,
there's more to it
```

---

## 7. Playlist

**`lide`**, za 147 *Why Can't You Stop Scrolling?* (lidské chování a mozek).
Dopsat slug do `playlisty.json` až po zveřejnění, pak `analytics.py --videa` a `playlisty.py`.
