# YouTube — 159 „Why Can't Entanglement Send Messages?“

Stav: **zveřejněno přes API celé** (`UG2taHmkj1k`): nastavení, náhled, lokalizace 13, titulky 15/15 vč. en-US, playlist `fyzika`. Zbývá ručně ve Studiu: karty, závěrečná obrazovka, US audiostopa.

| | |
|---|---|
| ID videa | `UG2taHmkj1k` (https://youtu.be/UG2taHmkj1k) |
| master | `render/final-en-159.mp4` (207, 3× supersampling, 623,3 s, 1920×1080, 39 MB, dekódováno bez chyby) |
| náhled | ✅ `render/thumbnail.jpg` (C1, ChatGPT, 1280×720, 0,28 MB), původ `thumbnail/PUVOD.md` |
| nastavení, popis, tagy | podklady níž |
| lokalizace | `youtube-preklady.md`, 13 jazyků |
| titulky | `subtitles/<kód>.srt`, 14 jazyků + `en-US`, Codex ve všech 13 překladech |
| americká stopa | ✅ `render/audio-en-US.m4a` (623,234 s = Emma, přetečení 2,1 %, drift en.srt medián 100 ms), ručně ve Studiu |
| závěrečná obrazovka | S74–S75, **horní polovina** (viz níž) |
| karty | **dvě**, S54 → 112, S56 → 027 (`nahraj.py` je vypíše) |
| playlist | `fyzika` (Physics That Sounds Simple Until You Ask) |

**Co musí uživatel naklikat sám:** závěrečnou obrazovku, **dvě karty**, americkou audiostopu
(`render/audio-en-US.m4a`) a osvědčení o zproštění, pokud ho nevyřídil průvodce nahráním.

Stopáž 10:23 (`work/timing.json` total 623,234 s).

> Kdyby se znovu pouštěl `tts.py`, přepočítej kapitoly a časy karet tady i v `youtube-preklady.md`
> a přegeneruj `en-US` přes `us_stopa.py`.

Pořadí podle CENY (`docs/zverejneni.md`):

```bash
V=videos/159-why-cant-entanglement-send-messages
python tools/nahraj.py $V --k-videu=<ID> --bez-titulku   # 100
python tools/analytics.py --videa                        #   1  ← nutné
python tools/lokalizace.py $V                            #  50
python tools/titulky.py $V --smaz-asr                    # 150  ← před titulky
python tools/titulky.py $V                               # 400×N
python tools/playlisty.py                                #  50
# úklid, až je MP4 na YouTube:
rm $V/render/draft*.mp4
```

---

## 1. Titul

```
Why Can't Entanglement Send Messages?
```

> Wh-otázka, 37 znaků, shodná s `project.json`. Odpověď (výsledek je náhodný, spojení je vidět
> až při porovnání záznamů) titul neprozrazuje.

---

## 2. Popis

```
In 2016, China's Micius satellite sent pairs of entangled photons to two observatories 1,200 kilometres apart, and the results were linked more tightly than anything ordinary allows. Physicists near Geneva showed that if anything does travel between such photons, then in the simplest picture it would have to go at least ten thousand times faster than light. So why can't you use it to send a message to a friend on Mars?

This video goes through what entanglement actually is, John Bell's argument with Reinhold Bertlmann's mismatched socks, David Mermin's two boxes with three-position switches, the experiments since 1972 and the 2022 Nobel Prize, what happens when Alice tries to send Bob a single bit, Steven Weinberg's tiny change to quantum mechanics and what Nicolas Gisin and Joseph Polchinski found in it, and a game where entangled particles win about 85 per cent of the time and never more. Then Popescu and Rohrlich's imaginary box that always wins, and the question nobody has answered yet.

Sources: J. Yin et al., Satellite-based entanglement distribution over 1200 kilometers, Science 356, 1140 (2017); D. Salart et al., Testing the speed of 'spooky action at a distance', Nature 454, 861 (2008); J. S. Bell, Bertlmann's socks and the nature of reality, J. Physique Colloques 42, C2-41 (1981); N. D. Mermin, Is the moon there when nobody looks?, Physics Today 38(4), 38 (1985); S. J. Freedman and J. F. Clauser, PRL 28, 938 (1972); B. Hensen et al., Nature 526, 682 (2015); G. C. Ghirardi, A. Rimini, T. Weber, Lett. Nuovo Cimento 27, 293 (1980); S. Weinberg, PRL 62, 485 (1989); J. J. Bollinger et al., PRL 63, 1031 (1989); N. Gisin, Phys. Lett. A 143, 1 (1990); J. Polchinski, PRL 66, 397 (1991); C. H. Bennett et al., PRL 70, 1895 (1993); J. F. Clauser, M. A. Horne, A. Shimony, R. A. Holt, PRL 23, 880 (1969); B. S. Cirel'son, Lett. Math. Phys. 4, 93 (1980); S. Popescu and D. Rohrlich, Found. Phys. 24, 379 (1994); G. Brassard et al., PRL 96, 250401 (2006); M. Pawłowski et al., Information causality as a physical principle, Nature 461, 1101 (2009); S. Popescu, Nonlocality beyond quantum mechanics, Nature Physics 10, 264 (2014).

Subtitles are written for this video, not auto-generated. An American English audio track is available as a second audio track.

CHAPTERS
00:00 Two photons, 1,200 km apart
00:57 A line to Mars?
01:26 What entanglement actually is
02:03 Are particles just like socks?
02:36 Mermin's two boxes
03:40 Delft, and a Nobel Prize
04:12 Trying to send one bit
05:03 The one thing Alice controls
06:01 What if the theory is slightly wrong?
06:33 Gisin, Polchinski and the Everett phone
07:18 A signal that arrives before it's sent
07:48 The second mystery: a game
08:40 A box that always wins
09:13 Why 85 per cent?
09:53 Back to Micius

IMAGE CREDITS
John Bell — CERN, CC BY 4.0, via Wikimedia Commons
Steven Weinberg, 1983 — Rob Croes for Anefo, CC0, via Wikimedia Commons
Albert Einstein — Oren Jack Turner, public domain
Licences: creativecommons.org/licenses/by/4.0
```

> **Blok se kopíruje CELÝ** (`docs/zverejneni.md`). Kredity ze `sources.json`: povinná atribuce je jen
> u S16 (John Bell, CERN, CC BY 4.0); Weinberg (S46) je CC0, Einstein (S14) public domain, jména jsou
> tam ze slušnosti. S10 a S48 jsou malované ilustrace z SDXL, zbytek kreslený kódem.
>
> **Pointa se neprozrazuje:** popis ani kapitoly neříkají, že výsledek je náhodný a spojení se ukáže
> až při porovnání záznamů (S31–S44). *Trying to send one bit* je pokus, ne odpověď; kapitola o vynucení
> výsledku (S42) proto vlastní kapitolu nemá. *Delft* = uzavření skulin (S28); slovo „loophole“ v popisu
> není, ať se nemusí vysvětlovat.
>
> Kapitoly ze scén S01, S07, S11, S15, S20, S28, S31, S38, S45, S49, S54, S58, S64, S69, S73
> (`work/timing.json`, zaokrouhleno dolů). První na 00:00, všechny ≥ 10 s (nejkratší S45 → S49, 31 s;
> poslední S73 → konec 30 s). Otázka do komentářů (S75) vlastní kapitolu nemá.
>
> **Zdroje:** z `factcheck-zaklad.md` ty primární. Weinbergova citace z *Dreams of a Final Theory*
> (jen z druhé ruky) a interpretace (Bohm, Valentini) v popisu nejsou, ve videu taky ne.

---

## 3. Náhled

**C1** z `thumbnail/ZADANI.md`: provázkový telefon se zářícím spojením, `ENTANGLED` / `SO WHY SILENT?`.
Nakreslil ChatGPT, dodávka `render/thumbnail.jpg` (1280×720, 0,28 MB), původ a otisk v `thumbnail/PUVOD.md`.
`thumb_check`: jas 77,2, kontrast 92,5, ve 150 px čitelné. Nahraje ho `nahraj.py`.

---

## 4. Titulky

`subtitles/<kód>.srt` pro 14 jazyků a `en-US`.
Jazyk videa **`en-gb`** (hlas `bf_emma`) nastaví `nahraj.py` dřív, než se nahrají titulkové stopy.

---

## 5. Nastavení

| | |
|---|---|
| kategorie | **Science & Technology** (28), posílá `nahraj.py` napevno |
| jazyk videa | `en-gb` |
| licence | standardní |
| pro děti | **ne** |
| komentáře | zapnuté (S75 je otázka do komentářů) |
| **byla použita AI** | **ne**. 70 ze 75 scén je kreslených kódem. S10 (observatoř v noci) a S48 (laboratoř) jsou malované ilustrace z SDXL, ne fotorealismus. Tři archivní portréty (Einstein, Bell, Weinberg) jsou upravené jen barevně. Hudba je procedurální, hlas není klon skutečné osoby. |

### Karty

Uživatel 2026-11-16: **na karty nezapomenout.** Obě cílová videa jsou zveřejněná.

| čas | scéna | cíl |
|---|---|---|
| **7:20** | S54 *As our video on faster-than-light travel showed* | 112 *Why Can't We Travel Faster Than Light?* (`CBMf9aawV-o`) |
| **7:36** | S56 *from our video on teleportation* | 027 *What Would Teleportation Take?* (`Sre7sQB1CIM`) |

> Časy jsou ze začátku scény + ~2 s; přesné vypíše `nahraj.py` z `work/timing.json`.

### Závěrečná obrazovka

Od **10:23 − 20 s ≈ 10:03**, prakticky od **10:05** (začátek S74). `zaver_check` hlásí S74–S75 OK,
**horní polovina je volná**. **Dlaždici i odběr dej do HORNÍ poloviny.**
Jako dlaždici navrhuju **112 *Why Can't We Travel Faster Than Light?*** (S54 na něj přímo odkazuje
a táž otázka „proč ne rychleji než světlo“ je jádro obou videí), druhou nechat na „nejlepší pro diváka“.

---

## 6. Tagy

```
quantum entanglement, entanglement, no-communication theorem, faster than light communication,
spooky action at a distance, bell's theorem, bell test, bertlmann's socks, mermin, micius satellite,
quantum mechanics, chsh game, tsirelson bound, popescu rohrlich box, information causality,
nobel prize physics 2022, quantum teleportation, there's more to it
```

---

## 7. Playlist

**`fyzika`** (Physics That Sounds Simple Until You Ask; je v něm i 027). Dopsat slug do
`playlisty.json`, `analytics.py --videa`, `playlisty.py --jen fyzika`.
