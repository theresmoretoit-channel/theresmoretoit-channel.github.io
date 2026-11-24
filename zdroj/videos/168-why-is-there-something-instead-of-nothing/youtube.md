# YouTube — 168 „Why Is There Something Instead of Nothing?“

Stav: **podklady hotové, video ještě NE.** Master `render/final-en-168.mp4` zatím není (jen
`render/draft-en.mp4`, schválený), náhled `render/thumbnail.jpg` taky ne (`thumbnail/` je prázdný).
Americká stopa `render/audio-en-US.m4a` (534,74 s, na mřížku) je hotová. Překlady prošly Codexem,
titulky 15 stop jsou v `subtitles/`, lokalizace 13 jazyků v `youtube-preklady.md`.

| | |
|---|---|
| ID videa | — (MP4 nahraje uživatel ručně ve Studiu, pak `--k-videu`) |
| master | **chybí** — `render/final-en-168.mp4` (207 nebo herní PC), stopáž 8:55 (534,74 s) |
| náhled | **chybí** — `render/thumbnail.jpg`, koncepty se teprve dělají |
| nastavení, popis, tagy | podklady níž |
| lokalizace | `youtube-preklady.md`, 13 jazyků (odkaz na web doplněn) |
| titulky | `subtitles/<kód>.srt`, 14 jazyků + `en-US`; Codex na všech 13 překladech |
| americká stopa | `render/audio-en-US.m4a` (`af_heart`), ručně ve Studiu |
| závěrečná obrazovka | S64–S66, **horní polovina, dlaždice vlevo** (viz níž) |
| karty | **jedna**: 1:04 (S09, neutrino) → 166 *Why Do Neutrinos Pass Through Everything?* |
| playlist | **`fyzika`** (rozhodl uživatel 2026-11-23) |
| komentář kanálu | otázka ze S66 v `pripnute-komentare.md`, viz oddíl 8 |
| shorty | `shorts/168-why-is-there-something-instead-of-nothing/` 01-leftover, 02-empty-box, 03-long-shot (vlastní podklady) |

**Co musí uživatel naklikat sám:** závěrečnou obrazovku, kartu na 166, americkou audiostopu
(`render/audio-en-US.m4a`), osvědčení o zproštění (pokud ho nevyřídil průvodce nahráním)
a po zveřejnění připnout komentář kanálu.

Stopáž 8:55 (`work/timing.json` total 534,742 s, script 0.7).

> Kdyby se znovu pouštěl `tts.py`, přepočítej kapitoly tady i v `youtube-preklady.md`
> a přegeneruj `en-US` přes `us_stopa.py`.

Pořadí podle CENY (`docs/zverejneni.md`):

```bash
V=videos/168-why-is-there-something-instead-of-nothing
# odkaz na web je v youtube.md i youtube-preklady.md už doplněný (odkaz_web.radek/vloz)
python tools/nahraj.py $V --k-videu=<ID> --bez-titulku   # 100
python tools/analytics.py --videa                        #   1  ← nutné
python tools/lokalizace.py $V                            #  50
python tools/titulky.py $V --smaz-asr                    # 150  ← před titulky
python tools/titulky.py $V                               # 400×N
python tools/playlisty.py                                #  50
# po zveřejnění: komentář kanálu (vloží i systemd timer)
python tools/komentare.py --jen 168                      #  51
# úklid, až je MP4 na YouTube:
rm $V/render/draft*.mp4
ssh vrana@192.168.0.207 'rm -rf /home/vrana/temp/render-168-why-is-there-something-instead-of-nothing'
```

---

## 1. Titul

```
Why Is There Something Instead of Nothing?
```

> Wh-otázka, 42 znaků, shodná s `project.json` a `Témata.fods`. Short 03 má proto jiný titul
> (*What are the odds of nothing?*), ať se ve výpisu nepletou.

---

## 2. Popis

```
When the universe was very young, it made matter and antimatter in almost exactly equal amounts, and when the two meet, both disappear. For every billion particles of antimatter, there were about a billion and one particles of matter, and everything you have ever seen is made of that leftover. Why the extra one? Nobody knows yet. And even the answer would only tell us why there is matter instead of just light. Not why there is anything at all.

So this video goes looking for real nothing, one step at a time: a box with everything taken out, the quantum vacuum and the Casimir effect, Edward Tryon's universe as a vacuum fluctuation, Lawrence Krauss's book A Universe from Nothing and David Albert's review of it, and Alexander Vilenkin's universe that appears with no space and no time before it. Then it turns to philosophy: Leibniz in 1714, the 1948 BBC radio debate between Bertrand Russell and Frederick Copleston, and Peter van Inwagen's attempt to count how many ways a world could be.

Sources: L. Canetti, M. Drewes & M. Shaposhnikov, Matter and Antimatter in the Universe, New J. Phys. 14 (2012) 095012; Planck Collaboration, Planck 2018 results VI: Cosmological parameters; M. Fukugita & T. Yanagida, Phys. Lett. B 174 (1986) 45; G. W. Leibniz, Principles of Nature and Grace (1714), §7–8; H. B. G. Casimir, Proc. KNAW 51 (1948) 793; S. K. Lamoreaux, Phys. Rev. Lett. 78 (1997) 5; G. Bressi et al., Phys. Rev. Lett. 88 (2002) 041804; R. L. Jaffe, Phys. Rev. D 72 (2005) 021301; E. P. Tryon, Is the Universe a Vacuum Fluctuation?, Nature 246 (1973) 396; L. M. Krauss, A Universe from Nothing (Free Press, 2012); D. Albert, On the Origin of Everything, The New York Times Book Review (March 2012); A. Vilenkin, Creation of Universes from Nothing, Phys. Lett. B 117 (1982) 25; B. Russell & F. C. Copleston, debate on the existence of God, BBC Third Programme (28 January 1948); F. C. Copleston, Aquinas (Pelican, 1955); P. van Inwagen, Why Is There Anything at All?, Proc. Aristotelian Society Supp. Vol. 70 (1996) 95–110.

Subtitles are written for this video, not auto-generated. An American English audio track is available as a second audio track.

Full transcript, sources and translations: https://theresmoretoit-channel.github.io/videos/why-is-there-something-instead-of-nothing/

CHAPTERS
00:00 One in a billion
01:29 Leibniz's question
02:10 Emptying a box
03:08 A universe from nothing?
04:05 No space, no time
05:05 Russell and Copleston
07:05 Counting possible worlds
08:05 Back to the question

IMAGE CREDITS
Hendrik Casimir (1958) — Anefo, CC BY-SA 3.0
via Wikimedia Commons
Licences: creativecommons.org/licenses/by-sa/3.0
All other archive images are in the public domain (Wikimedia Commons).
```

> **Blok se kopíruje CELÝ** (`docs/zverejneni.md`). Kredity ze `sources.json` / `CREDITS.md`
> (2 archivní snímky): **povinná atribuce CC BY-SA je jedna** — S23 *Hendrik Casimir (1958)*
> (Anefo, CC BY-SA 3.0, Wikimedia Commons), formát TASL. S12 Leibniz (Christoph Bernhard Francke)
> je volné dílo, podle dokumentu se nevypisuje.
>
> **Pointa se neprozrazuje:** popis končí výčtem cest, které video zkouší, a neříká, že žádná
> nedojde k nule (S37–S39) ani že tu vysvětlování končí (S63). Russell a Copleston bez vítěze,
> van Inwagen jen jako *„attempt to count“*, ne jeho závěr. Poslední kapitola je proto
> *Back to the question*, ne *Where explaining runs out*. Prozrazené je jen *„Nobody knows yet“*
> o přebytku hmoty, které ve videu zazní v 1:00 (S08).
>
> Kapitoly ze scén S01, S12, S17, S24, S32, S40, S53, S61 (`work/timing.json`, začátky
> obsahují `lead_in` 0,15 s — S01 začíná na 0,15 —, zaokrouhleno dolů). Hranice sedí na blokové
> pauzy storyboardu (2,2–2,8 s za S11, S16, S23, S31, S39, S52, S60). Pauza 2,4 s za S37 hranice
> není: S38–S39 dovozují z Vilenkina „tady fyzika končí“, patří ke stejnému bloku. První kapitola
> na 00:00, je jich 8, všechny ≥ 10 s (nejkratší S12 → S17 41 s; poslední S61 → konec 49 s).
> Otázka do komentářů (S66) vlastní kapitolu nemá.
>
> **Zdroje:** primární z `factcheck.md`. Albertova recenze je ve factchecku citovaná přes
> sekundární web (nytimes.com nedostupné), v řádku je proto jen titul, periodikum a měsíc.
> Van Inwagen ověřený přes SEP *Nothingness* (článek za zdí, 403). Řádek s odkazem na web vložen
> funkcemi `tools/odkaz_web.py` (`radek()` / `vloz()`); samotné `--repo` youtube.md přeskočí,
> dokud není commitnutý.

---

## 3. Náhled

**Zatím není.** `thumbnail/` je prázdný a `render/thumbnail.jpg` chybí. Podle
`docs/thumbnail-styl.md`: jeden koncept, otázka bez odpovědi (náhled nesmí říct „fyzika to nevysvětlí“
ani ukázat Boha / Russella jako vítěze). `nahraj.py --k-videu` jde pustit i bez náhledu
(`thumbnails.set` za 50 jednotek kdykoli potom).

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
| komentáře | zapnuté (S66 je otázka do komentářů) |
| **byla použita AI** | **ne**. 63 ze 66 scén je kreslených kódem, 2 jsou archivní snímky upravené jen barevně a vsazením do rámu (S12 Leibniz, S23 Casimir; výslovná výjimka *„color adjustment“*). S64 (drobná postava na kopci pod noční oblohou) je malovaná ilustrace z SDXL s kotvou *painterly editorial illustration*, obecná scéna, ne skutečné místo, osoba ani událost. Hlas je syntetický Kokoro `bf_emma`, ne klon skutečné osoby; hudba je procedurální. |

### Karty

**Jedna**, ze `storyboard.json` (`"karta"` u S09): **1:04** (S09, *„One suspect is the neutrino“*)
→ **166 *Why Do Neutrinos Pass Through Everything?*** `nahraj.py` ji vypíše mezi ručními kroky.

### Závěrečná obrazovka

Od **8:55 − 20 s ≈ 8:35** (S64 začíná 8:33, S65 8:38, S66 8:43). `zaver_check` hlásí S64–S66 OK.
**Dlaždici dej vlevo nahoru** (vpravo nahoře by v S64 zakryla 5,5 % kresby), odběr do horní
poloviny; spodní rohy jsou pod titulky. Jako dlaždici navrhuju **085 *If God Exists, What Is God?***
(navazuje na Coplestonovu nutnou bytost; alternativy 166 neutrina — ta už má kartu —, 040 *Does
the Past Still Exist?*, 164 svobodná vůle), druhou nechat na „nejlepší pro diváka“.

---

## 6. Tagy

```
why is there something rather than nothing, something from nothing, nothingness, leibniz,
a universe from nothing, lawrence krauss, matter antimatter asymmetry, antimatter, quantum vacuum,
casimir effect, alexander vilenkin, bertrand russell, frederick copleston, russell copleston debate,
peter van inwagen, contingency argument, philosophy of physics, cosmology, metaphysics, there's more to it
```

---

## 7. Playlist

**`fyzika`** — rozhodl uživatel 2026-11-23 (*Physics That Sounds Simple Until You Ask*; je v něm 040 *Does the Past Still
Exist?*, tatáž polička „velké otázky“). Alternativa / druhý playlist **`lide`** (*Why We Do What We
Do*; 073 a 085 o Bohu, 164 svobodná vůle). Rozhodne uživatel; pak dopsat slug do `playlisty.json`,
`analytics.py --videa`, `playlisty.py --jen <klíč>`. Nástěnka shortů na Pinterestu se řídí tímhle
rozhodnutím (u dvou playlistů ten menší).

---

## 8. Komentář kanálu (otázka ze S66)

Podle `docs/cta.md`, „Táž otázka jako komentář kanálu“: psanou formou, bez *„So here's a question
for you“* a *„Let me know in the comments“*. **Zapsáno v `pripnute-komentare.md`** — musí
být pushnutá a stažená dřív, než video vyjde, jinak ji timer nevloží:

```
Is "the universe is just there" an honest answer, or a way of not answering?
```

> Beze změny proti S66 — citát Russella se v komentáři čte i bez kontextu videa. Vkládá se až po
> zveřejnění (`komentare.py --jen 168`, nebo systemd timer ve 21:15); připnout ručně ve Studiu.
