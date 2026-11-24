# YouTube — 166 „Why Do Neutrinos Pass Through Everything?“

Stav: **nahráno 2026-11-23 jako `j7dXpL3cpmw`, naplánováno na 28. 11. 2026.** Ruční kroky ve Studiu
(9 titulků, US stopa, závěrečná obrazovka) uživatel naklikal. Metadata, náhled a lokalizace 13 jazyků jsou nahoře;
titulky **6 z 15** (en, cs, sv, es, pt-BR, de), pak došla kvóta. Zbylých 9 (fr, it, pl, id, tr, uk, vi, fi, en-US) nahrává **uživatel ručně
ve Studiu** (2026-11-23), `titulky.py` už nepouštět.
Playlist zatím ne (rozhodne uživatel). Master `render/final-en-166.mp4` (12:34, 1080p, .207, 2026-11-23)
a americká stopa `render/audio-en-US.m4a` (754,03 s) jsou hotové. Překlady prošly Codexem, titulky
15 stop jsou v `subtitles/`, lokalizace 13 jazyků v `youtube-preklady.md`.

| | |
|---|---|
| ID videa | `j7dXpL3cpmw` (MP4 nahrál uživatel ve Studiu, metadata `nahraj.py --k-videu`) |
| master | `render/final-en-166.mp4` — 12:34 (754,04 s), 1080p, .207, 2026-11-23 |
| náhled | `render/thumbnail.jpg` — C1 „NEUTRINOS / FEEL ANYTHING?“, původ v `thumbnail/PUVOD.md` |
| nastavení, popis, tagy | podklady níž |
| lokalizace | `youtube-preklady.md`, 13 jazyků |
| titulky | `subtitles/<kód>.srt`, 14 jazyků + `en-US`; Codex na všech 13 překladech |
| americká stopa | `render/audio-en-US.m4a` (`af_heart`), ručně ve Studiu |
| závěrečná obrazovka | S90–S91, **horní polovina** (viz níž) |
| karty | **žádné** (storyboard nemá klíč `karta`) |
| playlist | návrh `fyzika` (viz níž) |
| komentář kanálu | otázka ze S91 v `pripnute-komentare.md`, viz oddíl 8 |

**Co musí uživatel naklikat sám:** závěrečnou obrazovku, americkou audiostopu
(`render/audio-en-US.m4a`), osvědčení o zproštění (pokud ho nevyřídil průvodce nahráním)
a po zveřejnění připnout komentář kanálu.

Stopáž 12:34 (`work/timing.json` total 754,03 s, script 0.4, 101 scén).

> Kdyby se znovu pouštěl `tts.py`, přepočítej kapitoly tady i v `youtube-preklady.md`
> a přegeneruj `en-US` přes `us_stopa.py`.

Pořadí podle CENY (`docs/zverejneni.md`):

```bash
V=videos/166-why-do-neutrinos-pass-through-everything
python tools/odkaz_web.py --repo --jen 166                 # řádek s odkazem na web (po commitu)
python tools/nahraj.py $V --k-videu=<ID> --bez-titulku   # 100
python tools/analytics.py --videa                        #   1  ← nutné
python tools/lokalizace.py $V                            #  50
python tools/titulky.py $V --smaz-asr                    # 150  ← před titulky
python tools/titulky.py $V                               # 400×N
python tools/playlisty.py                                #  50
# po zveřejnění: komentář kanálu (vloží i systemd timer)
python tools/komentare.py --jen 166                      #  51
# úklid, až je MP4 na YouTube:
rm $V/render/draft*.mp4
ssh vrana@192.168.0.207 'rm -rf /home/vrana/temp/render-166-why-do-neutrinos-pass-through-everything'
```

---

## 1. Titul

```
Why Do Neutrinos Pass Through Everything?
```

> Wh-otázka, 41 znaků, shodná s `project.json` (schválil uživatel 2026-11-19).

---

## 2. Popis

```
Every second, tens of billions of neutrinos pass through your thumbnail. They go through your body and straight through the Earth beneath your feet, and at night they come up through the floor after crossing the whole planet. Almost none of them ever touch you. So how can a particle cross a planet without hitting anything? And if it never hits anything, how do we know it's there?

The story starts with energy that seemed to vanish from radioactive decay, and Wolfgang Pauli's "desperate remedy" in 1930. Then come a bet over a case of champagne, a reactor in South Carolina, a wall of lead a light-year thick, a Japanese tank holding fifty thousand tonnes of ultra-pure water, and a gold mine in South Dakota filled with dry-cleaning fluid, where two thirds of the Sun's neutrinos seemed to be missing for more than thirty years.

Sources: W. Pauli, letter to the Tübingen meeting (4 December 1930), via Symmetry Magazine; CERN Archive, Reines–Cowan telegram and Pauli's reply (1956); APS, Savannah River neutrino experiment; D. Haidt (DESY), on Pauli's champagne bet; on the history of beta decay, arXiv:1210.3065; Mitalas & Sills (1992), energy transport time in the Sun; Super-Kamiokande Collaboration, SK-I solar neutrino measurements (hep-ex/0508053); review of the Homestake chlorine experiment (hep-ex/0312045); SNO Collaboration, Phys. Rev. Lett. 89, 011301 (2002); Nobel Prize in Physics 2015, nobelprize.org; KATRIN Collaboration, Science 388, 180 (2025); SN 1987A observations by Kamiokande II, IMB and Baksan; H.-T. Janka, Explosion Mechanisms of Core-Collapse Supernovae (2012); KamLAND Collaboration, Nature Geoscience (2011); Particle Data Group, Big-Bang nucleosynthesis review; Planck Collaboration, cosmological parameters (2018); DESI Collaboration, neutrino mass constraints (2025).

Subtitles are written for this video, not auto-generated. An American English audio track is available as a second audio track.

Full transcript, sources and translations: https://theresmoretoit-channel.github.io/videos/why-do-neutrinos-pass-through-everything/

CHAPTERS
00:00 Through your thumbnail
00:47 Something went missing
01:32 Pauli's desperate remedy
02:21 A bet and a reactor
03:29 The telegram
03:58 Why they pass through everything
05:11 The Sun's neutrino factory
06:16 How to catch one
07:02 A tank of dry-cleaning fluid
08:01 Missing, again
09:02 How heavy is a neutrino?
09:31 A star explodes
10:27 The oldest neutrinos
11:22 Will space fill up with them?
11:57 Right now, all around you

IMAGE CREDITS
Wolfgang Pauli — unknown author, CC BY 4.0
Super Kamiokande, 1 to 135th — Motokoka, CC BY-SA 4.0
Cosmic Microwave Background (CMB) — ESA and the Planck Collaboration, CC BY 4.0
via Wikimedia Commons
Licences: creativecommons.org/licenses/by/4.0, creativecommons.org/licenses/by-sa/4.0
All other archive images are in the public domain (Savannah River Site, U.S. Department of Energy, NASA/ESA Hubble Heritage Team, Wikimedia Commons).
```

> **Blok se kopíruje CELÝ** (`docs/zverejneni.md`). Kredity ze `sources.json` / `CREDITS.md`
> (7 archivních snímků): **povinná atribuce jsou tři** — S14 *Wolfgang Pauli* (autor
> neznámý, CC BY 4.0), S52 *Super Kamiokande, 1 to 135th* (Motokoka, CC BY-SA 4.0) a S87
> *Cosmic Microwave Background (CMB)* (ESA and the Planck Collaboration, CC BY 4.0), formát
> TASL. Zbylé čtyři jsou volné dílo (S17 Chadwick, S22 Reines a Cowan / Savannah River Site,
> S58 výkres Homestake / ENERGY.GOV, S78 SN 1987A / Hubble Heritage Team). Kresba v `art/S82.png`
> je naše ilustrace (`art/PUVOD.md`), atribuci nepotřebuje.
>
> **Pointa se neprozrazuje:** popis končí u záhady chybějících slunečních neutrin a neříká,
> že se mění druh (S69) ani že z toho plyne hmotnost (S73). Kapitola 08:01 je proto
> *Missing, again*, ne *Neutrinos change flavour*, a 09:02 je otázka. SN 1987A, geoneutrina
> a reliktní neutrina popis vynechává, nesou je jen kapitoly.
>
> Kapitoly ze scén S01, S08, S14, S19, S28, S32, S43, S50, S57, S66, S73, S77, S82, S87b, S88
> (`work/timing.json`, začátky obsahují `lead_in` 0,15 s, zaokrouhleno dolů). První na 00:00,
> je jich 15, všechny ≥ 10 s (nejkratší S73 → S77 29 s a S28 → S32 29 s; poslední S88 → konec
> 37 s). Otázka do komentářů (S91) vlastní kapitolu nemá.
>
> **Zdroje:** z `factcheck.md` a `factcheck-zaklad.md`. Sekundární zdroje (Symmetry, CERN
> Archive, APS, Haidt) jsou jmenované jako takové; sázka i šampaňské jsou ve scénáři
> s výhradou *„the story goes“*. Řádek s odkazem na web doplní `tools/odkaz_web.py --repo`
> (youtube.md přeskočí, dokud není commitnutý).

---

## 3. Náhled

`render/thumbnail.jpg` (1280×720, 0,26 MB) je koncept **C1**: palec, kterým prolétají světelné stopy,
s textem `NEUTRINOS` / `FEEL ANYTHING?`. Obrázek dodal uživatel z externího nástroje podle
`thumbnail/ZADANI.md`. Původ, otisky a `thumb_check` jsou v `thumbnail/PUVOD.md`.

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
| komentáře | zapnuté (S91 je otázka do komentářů) |
| **byla použita AI** | **ne**. 92 ze 101 scén je kreslených kódem (S82 z toho s plochou ilustrací v `art/S82.png`, viz `art/PUVOD.md`), 7 jsou archivní snímky upravené jen barevně a výřezem (výslovná výjimka *„color adjustment“*). S43 (Slunce nad tmavou krajinou) a S57 (nádrž v podzemí) jsou malované ilustrace z SDXL s kotvou stylu, obecné scény, ne skutečné místo, osoba ani událost. Hlas je syntetický Kokoro `bf_emma`, ne klon skutečné osoby; hudba je procedurální. |

### Karty

Žádné. `storyboard.json` nemá klíč `karta` a scénář na jiné video kanálu neodkazuje.

### Závěrečná obrazovka

Od **12:34 − 20 s ≈ 12:14** (S90 začíná 12:11, S91 12:23). `zaver_check` hlásí S90–S91 OK.
**Dlaždici i odběr dej do HORNÍ poloviny.** Jako dlaždici navrhuju **127 *What Would a
Spoonful of a Neutron Star Do?*** (záplava neutrin ze supernovy, přímý callback k S79;
alternativa 112 *Why Can't We Travel Faster Than Light?*), druhou nechat na „nejlepší pro
diváka“.

---

## 6. Tagy

```
neutrinos, neutrino, particle physics, wolfgang pauli, super-kamiokande, solar neutrinos,
neutrino oscillation, ray davis, homestake experiment, reines cowan, supernova 1987a,
cosmic neutrino background, weak force, physics explained, science, there's more to it
```

---

## 7. Playlist

Návrh **`fyzika`** (*Physics That Sounds Simple Until You Ask*; je v něm 127 *Neutron Star*
i 159 *Entanglement*). Alternativa `vesmir` (Slunce, supernova). Rozhodne uživatel; pak dopsat
slug do `playlisty.json`, `analytics.py --videa`, `playlisty.py --jen fyzika`.

---

## 8. Komentář kanálu (otázka ze S91)

Podle `docs/cta.md`, „Táž otázka jako komentář kanálu“: psanou formou, bez *„So here's a question
for you“* a *„Let me know in the comments“*. **Zapsáno v `pripnute-komentare.md`** — musí
být pushnutá a stažená dřív, než video vyjde, jinak ji timer nevloží:

```
Did it surprise you just how many neutrinos are passing through you right now? Tens of billions through your thumbnail every second.
```

> Otázku zvolil uživatel (`notes.md`, 2026-11-22) místo původního kandidáta o detektoru,
> který v `pripnute-komentare.md` stál dřív. Druhá věta komentáři dává kontext, protože se
> čte bez videa. Vkládá se až po zveřejnění (`komentare.py --jen 166`, nebo systemd timer
> ve 21:15); připnout ručně ve Studiu.
