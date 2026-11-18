# YouTube — 147 „Why Can't You Stop Scrolling?“

Stav: **MP4 nahrané ručně 2026-11-07** (`KGVeMGkLpOg`). Metadata, lokalizace (13 jazyků, po Codexu) a playlist přes API týž den; z titulků přes API
**jen `en` a `en-US`** (rozhodl uživatel 2026-11-07), zbylých 13 jazyků nahrává uživatel ručně ve Studiu.
Závěrečná obrazovka, americká stopa, zbylých 13 titulků a plán zveřejnění naklikal uživatel ve Studiu 2026-11-07. Stav zveřejnění je v `Témata.fods`.

| | |
|---|---|
| ID videa | `KGVeMGkLpOg` — https://www.youtube.com/watch?v=KGVeMGkLpOg |
| master | `render/final-en-147.mp4` (herní PC přes wifi, 644,7 s) |
| náhled | ✅ C2 `SCROLLING / WHICH ONE SHOCKS?`, `render/thumbnail.jpg`, nahráno (`thumbnail/PUVOD.md`) |
| nastavení, popis, tagy | podklady níž |
| lokalizace | `youtube-preklady.md`, 13 jazyků, Codex zapracován, nahráno |
| titulky | `en` a `en-US` nahrané přes API (ASR na videu nebyl); `subtitles/<kód>.srt` pro 13 jazyků ručně ve Studiu (Codex v0.4 zapracován) |
| americká stopa | `render/audio-en-US.m4a`, ručně ve Studiu |
| závěrečná obrazovka | S73–S74, **horní polovina** (viz níž) |
| karty | žádné |
| playlist | `lide` (*Why We Do What We Do*), za 146, zařazeno |

**Co musí uživatel naklikat sám:** závěrečnou obrazovku, americkou audiostopu
(`render/audio-en-US.m4a`), titulky 13 jazyků a osvědčení o zproštění, pokud ho nevyřídil průvodce nahráním.

Stopáž 10:44 (`work/timing.json` total 644,636 s).

> Kdyby se znovu pouštěl `tts.py`, přepočítej kapitoly tady i v `youtube-preklady.md`
> a přegeneruj `en-US` přes `us_stopa.py`.

Pořadí podle CENY (`docs/zverejneni.md`):

```bash
V=videos/147-why-cant-you-stop-scrolling
python tools/nahraj.py $V --k-videu=KGVeMGkLpOg --bez-titulku   # 100
python tools/analytics.py --videa                        #   1  ← nutné
python tools/lokalizace.py $V                            #  50
python tools/titulky.py $V --smaz-asr                    # 150  ← před titulky
python tools/titulky.py $V --jen en,en-US                # 800
python tools/playlisty.py                                #  50
# úklid, až je MP4 na YouTube:
rm $V/render/draft*.mp4
ssh vrana@192.168.0.207 'rm -rf /home/vrana/temp/render-147-why-cant-you-stop-scrolling'
```

---

## 1. Titul

```
Why Can't You Stop Scrolling?
```

> Wh-otázka, 29 znaků, shodná s `project.json`. Odpověď (tři části, S13–S45) titul neprozrazuje.

---

## 2. Popis

```
Ten yellow pens on a table. Some of them will give you an electric shock. Nobody will tell you which. Students waiting for an experiment clicked them anyway, just to find out. So why can't you stop scrolling?

Doomscrolling means carrying on through bad news, even though you know it's making you feel worse. This video goes through more than twenty thousand headline tests, a game with two rocks and a hidden snake, the designer who came up with infinite scroll, 806 Twitter users and two versions of their feed, and the Boston Marathon bombing. And it ends with what you can actually do about it.

Sources: Holman, Garfin & Silver 2014, PNAS; Kushlev & Dunn 2015, Computers in Human Behavior; de Berker et al. 2016, Nature Communications; Hsee & Ruan 2016, Psychological Science; Thompson et al. 2019, Science Advances; Allcott et al. 2020, American Economic Review; Buchanan et al. 2021, PLoS ONE; Robertson et al. 2023, Nature Human Behaviour; Shabahang et al. 2024, Computers in Human Behavior Reports; Milli et al. 2025, PNAS Nexus; Türk Kurtça & Kocatürk 2025, Personality and Individual Differences.

Subtitles are written for this video, not auto-generated. An American English audio track is available as a second audio track.

Full transcript, sources and translations: https://theresmoretoit-channel.github.io/videos/why-cant-you-stop-scrolling/

CHAPTERS
00:00 Ten yellow pens
00:45 A phone in your hand
01:10 Doomscrolling
01:35 Something behind a bush
02:06 Twenty thousand headlines
02:49 A snake under a rock
03:21 Fifty-fifty
03:34 A war that's just begun
04:37 The last page
05:08 What the algorithm shows you
06:37 Does it do you any harm?
07:10 Boston, 2013
08:17 Staying informed
09:01 What can you do about it?
09:35 Back to the pens
09:55 So why can't you stop?

IMAGE CREDITS
Ne tf-2679 — NEXT Conference from Berlin, Deutschland, CC BY 2.0
BOSTON MARATHON FINISH LINE — Bill Morrow from Tucson, AZ, US, CC BY 2.0
via Wikimedia Commons
Licence: creativecommons.org/licenses/by/2.0
```

> **Blok se kopíruje CELÝ** (`docs/zverejneni.md`). CC BY* ze `sources.json`: S35 (NEXT Conference) a S49 (Bill Morrow),
> jiné archivní snímky video nemá, proto bez věty o public domain.
>
> **Pointa se neprozrazuje:** popis ani kapitoly nejmenují tři části odpovědi (nejistota, chybějící poslední stránka,
> algoritmus), ani *every headline is a yellow pen* (S32) a smyčku (S45, S56). Kapitola 03:21 je jen *Fifty-fifty*.
>
> Kapitoly ze scén S01, S07, S11, S14, S17, S21, S24, S26, S34, S37, S46, S49, S57, S65, S68, S70
> (`work/timing.json`, zaokrouhleno dolů). První na 00:00, všechny ≥ 10 s (nejkratší S24 → S26, 12,5 s;
> poslední S70 → konec 49 s). Otázka do komentářů (S74, 9 s) vlastní kapitolu nemá, byla by kratší než 10 s.
> Výzvy k odběru (za S16 a S44) leží uvnitř kapitol.
>
> **Zdroje:** jen to, co jsem četl v primárním znění nebo abstraktu (`factcheck.md`). Hsee & Ruan 2016 je
> ze tiskové zprávy APS o tomtéž článku, ale je to pokus, na kterém video stojí, takže je uvedený. Kaya & Griffiths 2025
> chybí, protože ve `factcheck.md` je jen zkratka časopisu (*BIT*) a plný název jsem neověřil; tvrzení S29 nese
> i Türk Kurtça & Kocatürk. BBC Panorama (Raskin) je přetisk, proto tu není.

---

## 3. Náhled

C2 z `thumbnail/ZADANI.md` (ChatGPT): deset žlutých per, `SCROLLING / WHICH ONE SHOCKS?`.
`render/thumbnail.jpg`, nahráno přes `thumbnails.set` 2026-11-07. Původ v `thumbnail/PUVOD.md`.

---

## 4. Titulky

Přes API jen `en` a `en-US` (`titulky.py --jen en,en-US`, po `--smaz-asr`). Zbylých 13 jazyků
(`subtitles/<kód>.srt`, Codex v0.4 zapracován) nahrává uživatel ručně. Jazyk videa **`en-gb`** (hlas `bf_emma`)
nastaví `nahraj.py` dřív, než se nahrají titulkové stopy.

---

## 5. Nastavení

| | |
|---|---|
| kategorie | **Science & Technology** (28), posílá `nahraj.py` napevno |
| jazyk videa | `en-gb` |
| licence | standardní |
| pro děti | **ne** |
| komentáře | zapnuté (S74 je otázka do komentářů) |
| **byla použita AI** | **ne**. 67 ze 71 scén je kreslených kódem, dva archivní snímky (S35, S49) jsou upravené jen barevně a ořezem, S14 (les) a S71 (noviny na stole) jsou ze SDXL. S71 je ze všech obrazů nejblíž fotce, ale je to zátiší obecného předmětu, ne skutečná osoba, místo ani událost, takže divák nemůže být uveden v omyl o něčem, co se stalo; pravidla YouTube označení žádají právě u toho. Hudba je procedurální, hlas není klon skutečné osoby. |

### Závěrečná obrazovka

Od **10:25** (posledních 20 s), tedy S73–S74. `zaver_check` hlásí v obou dolních rozích titulek.
**Dlaždici i odběr dej do HORNÍ poloviny.** Jako dlaždici navrhuju **011 *Why Is It So Hard to Quit Some Games?***
(totéž téma: proč se nedá přestat), druhou nechat na „nejlepší pro diváka".

---

## 6. Tagy

```
doomscrolling, why can't i stop scrolling, how to stop doomscrolling, doomscrolling psychology,
negativity bias, intolerance of uncertainty, infinite scroll, aza raskin, social media algorithm,
twitter algorithm, news anxiety, bad news, upworthy headlines, boston marathon bombing,
psychology experiments, there's more to it
```

---

## 7. Playlist

**`lide`** (*Why We Do What We Do*), za 146. Pinterest shortů: `Psychology & Human Behavior`.
