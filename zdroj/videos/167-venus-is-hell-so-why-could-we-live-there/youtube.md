# YouTube — 167 „Venus Is Hell. So Why Could We Live There?“

Stav: **nahráno 2026-11-25 jako `_T7z5KvnUR8`, naplánováno na 29. 11. 2026.** Metadata, náhled a lokalizace 13 jazyků přes API; ruční kroky ve Studiu (US stopa, karta S82, závěrečná obrazovka, playlist `vesmir`) uživatel doklikal. **Titulky hotové:** ASR smazán, 14 stop přes API, `en-US` ručně (15 stop). Draft a kopie na .207 smazány.
Náhled C1 i master hotové, čeká se na ruční nahrání MP4 ve Studiu. Překlady 13 jazyků
prošly Codexem, lokalizace jsou v `youtube-preklady.md`.

| | |
|---|---|
| ID videa | `_T7z5KvnUR8` (MP4 nahrál uživatel ve Studiu, metadata `nahraj.py --k-videu`) |
| master | `render/final-en-167.mp4` — 11:06 (665,68 s), 1080p, .207, 2026-11-24 |
| náhled | `render/thumbnail.jpg` — C1 „VENUS / WOULD YOU LIVE HERE?“, původ v `thumbnail/PUVOD.md` |
| nastavení, popis, tagy | podklady níž |
| lokalizace | `youtube-preklady.md`, 13 jazyků |
| titulky | `subtitles/<kód>.srt`, 14 jazyků + `en-US` |
| americká stopa | `render/audio-en-US.m4a` (`af_heart`), ručně ve Studiu |
| závěrečná obrazovka | S87–S88, **horní polovina, vpravo** (viz níž) |
| karty | **S82 → 160** *Why Is It So Hard to Bring a Rock Back from Mars?* v **10:09** |
| playlist | návrh `vesmir` (viz níž) |
| komentář kanálu | otázka ze S88 v `pripnute-komentare.md`, viz oddíl 8 |

**Co musí uživatel naklikat sám:** závěrečnou obrazovku, kartu u S82, americkou audiostopu
(`render/audio-en-US.m4a`), osvědčení o zproštění (pokud ho nevyřídil průvodce nahráním)
a po zveřejnění připnout komentář kanálu.

Stopáž 11:06 (`work/timing.json` total 665,62 s, script 0.4, 93 scén).

> Kdyby se znovu pouštěl `tts.py`, přepočítej kapitoly tady i v `youtube-preklady.md`
> a přegeneruj `en-US` přes `us_stopa.py`.

Pořadí podle CENY (`docs/zverejneni.md`):

```bash
V=videos/167-venus-is-hell-so-why-could-we-live-there
python tools/odkaz_web.py --repo --jen 167                 # řádek s odkazem na web (po commitu)
python tools/nahraj.py $V --k-videu=<ID> --bez-titulku   # 100
python tools/analytics.py --videa                        #   1  ← nutné
python tools/lokalizace.py $V                            #  50
python tools/titulky.py $V --smaz-asr                    # 150  ← před titulky
python tools/titulky.py $V                               # 400×N
python tools/playlisty.py                                #  50
# po zveřejnění: komentář kanálu (vloží i systemd timer)
python tools/komentare.py --jen 167                      #  51
# úklid, až je MP4 na YouTube:
rm $V/render/draft*.mp4
ssh vrana@192.168.0.207 'rm -rf /home/vrana/temp/render-167-venus-is-hell-so-why-could-we-live-there'
```

---

## 1. Titul

```
Venus Is Hell. So Why Could We Live There?
```

> 42 znaků, shodný s `project.json`. Wh-otázka s paradoxem, převzatá ze zdroje
> (`notes.md`). Alternativa *Why Might Venus Beat Mars?* je kratší, ale vyzradí směr.

---

## 2. Popis

```
The surface of Venus is about 465 °C (869 °F), hot enough to melt lead, and the atmosphere presses down ninety times harder than on Earth. The Soviet lander Venera 13 lasted just over two hours there. And yet some NASA engineers argue that the most Earth-like conditions anywhere beyond our own planet are on Venus. Not on the surface, but fifty kilometres above it.

So let's keep score: Venus against Mars, point by point. Gravity, radiation, how a city could stay up in the sky, clouds of sulphuric acid, power, water, solid ground and the journey there. Along the way come the Soviet Vega balloons that floated through the clouds of Venus in 1985 and NASA's HAVOC study of a crewed airship. And at the end, the part the score doesn't show.

Sources: G. A. Landis, Colonization of Venus (STAIF 2003, NASA NTRS 20030022668); G. A. Landis, Settling Venus: A City in the Clouds? (AIAA 2020-4152, NASA NTRS 20205008515); C. A. Jones, D. C. Arney et al., HAVOC: Proofs of Concept (NASA Langley, NTRS 20160006580); D. C. Arney & C. A. Jones, HAVOC: An Exploration Strategy for Venus (AIAA Space 2015, NTRS 20160006329); Venus International Reference Atmosphere (VIRA); Vega balloon experiment, NASA NTRS 19860018820 and JPL VLBI tracking; NASA/JPL and MIT on MOXIE aboard the Perseverance rover; NASA Venus and Mars fact sheets.

Subtitles are written for this video, not auto-generated. An American English audio track is available as a second audio track.

Full transcript, sources and translations: https://theresmoretoit-channel.github.io/videos/venus-is-hell-so-why-could-we-live-there/

CHAPTERS
00:00 Hot enough to melt lead
00:44 Venus against Mars
00:56 Where exactly would we live?
01:51 Gravity
02:19 Radiation
02:53 How does a city stay up in the sky?
04:45 Balloons on Venus, 1985
05:26 A crewed airship
06:13 Clouds of sulphuric acid
07:11 Power
07:59 Water
08:51 Solid ground
09:25 Getting there
09:48 Getting home
10:21 The real answer

IMAGE CREDITS
All archive images are in the public domain or CC0 (USSR/NASA, NASA/JPL-Caltech, NASA/JPL-Caltech/MSSS, Daderot and Balon Greyjoy via Wikimedia Commons).
```

> **Blok se kopíruje CELÝ** (`docs/zverejneni.md`). Kredity ze `sources.json` / `CREDITS.md`
> (5 archivních snímků): **povinná atribuce žádná.** S04 Venera 13 (USSR/NASA, PD), S37 model
> Vegy (Daderot, PD), S38 balon Vega (Balon Greyjoy, CC0), S69 MOXIE (NASA/JPL-Caltech, PD),
> S73b Curiosity (NASA/JPL-Caltech/MSSS, PD). Autoři jsou v řádku jmenovaní ze slušnosti.
>
> **Pointa se neprozrazuje:** popis neříká konečné skóre ani to, že rozhoduje cesta domů
> (S78–S82). Kapitola 09:48 *Getting home* je jen téma, 10:21 *The real answer* nic neprozradí.
>
> Kapitoly ze scén S01, S08, S09, S16, S20, S25, S37, S43, S49, S57, S64, S71, S75, S78, S83
> (`work/timing.json`, začátky obsahují `lead_in` 0,15 s, zaokrouhleno dolů). První na 00:00,
> je jich 15, všechny ≥ 10 s (nejkratší S08 → S09 12 s; S47 *why is every plan about Mars?*
> by měla jen 12 s, proto je součástí *A crewed airship*). Poslední S83 → konec 44 s.
>
> **Zdroje:** z `factcheck.md` a `factcheck-zaklad.md`, primární čtyři (Landis 2003, 2020,
> HAVOC PoC, HAVOC 2015) jsou plné texty. Řádek s odkazem na web doplní
> `tools/odkaz_web.py --repo` (youtube.md přeskočí, dokud není commitnutý).
> °F v prvním odstavci je kvůli americkému publiku, stejně jako v diagramech.

---

## 3. Náhled

`render/thumbnail.jpg` (1280×720, 0,27 MB) je koncept **C1**: průhledný balon s obydlím nad žlutými
mraky, pod nimi rozžhavený povrch, text `VENUS` / `WOULD YOU LIVE HERE?`. Obrázek dodal uživatel
z externího nástroje podle `thumbnail/ZADANI.md`. Původ, otisky a `thumb_check` jsou v `thumbnail/PUVOD.md`.

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
| komentáře | zapnuté (S88 je otázka do komentářů) |
| **byla použita AI** | **ne**. 86 z 93 scén je kreslených kódem, 5 jsou archivní snímky upravené jen barevně a výřezem (výslovná výjimka *„color adjustment“*). S30 (balon nad mraky) a S86 (kajuta vzducholodi s oknem) jsou malované ilustrace z SDXL s kotvou stylu, smyšlené scény, ne skutečné místo, osoba ani událost. Hlas je syntetický Kokoro `bf_emma`, ne klon skutečné osoby; hudba je procedurální. |

### Karty

**S82 (10:09) → 160 *Why Is It So Hard to Bring a Rock Back from Mars?*** Scéna říká
*„It's one of the reasons bringing back a single rock is so hard.“* (`storyboard.json`, klíč `karta`).

### Závěrečná obrazovka

Od **11:06 − 20 s ≈ 10:45** (S87 začíná 10:45, S88 10:56). `zaver_check` hlásí S87–S88 OK,
volno je jen v **horní polovině**; v S87 je obsazený levý horní roh, takže **dlaždici i odběr
dej vpravo nahoru**. Jako dlaždici navrhuju **065 *Who Will Own Mars?*** (Mars jako místo
k životu, přímé pokračování otázky ze S88; 160 už dostane kartu), alternativa
165 *Why Hasn't Anyone Walked on the Moon Since 1972?*, druhou nechat na „nejlepší pro diváka“.

---

## 6. Tagy

```
venus, mars, venus colony, cloud city, floating city, havoc, nasa, venus atmosphere,
vega balloons, venera 13, space colonization, life on venus, planets, space,
science explained, there's more to it
```

---

## 7. Playlist

Návrh **`vesmir`** (je v něm 035, 070, 127 a 165 *Moon*). Rozhodne uživatel; pak dopsat
slug do `playlisty.json`, `analytics.py --videa`, `playlisty.py --jen vesmir`.

---

## 8. Komentář kanálu (otázka ze S88)

Podle `docs/cta.md`, „Táž otázka jako komentář kanálu“: psanou formou, bez *„So here's a question
for you“* a *„Let me know in the comments“*. **Zapsáno v `pripnute-komentare.md`** — musí
být pushnutá a stažená dřív, než video vyjde, jinak ji timer nevloží:

```
Would you rather live in a cave on Mars, or in a balloon 50 kilometres above Venus?
```

> Druhá půlka má „50 kilometres“ (číslicí podle `docs/cta.md`), protože komentář se čte bez videa. Vkládá se až po
> zveřejnění (`komentare.py --jen 167`, nebo systemd timer ve 21:15); připnout ručně ve Studiu.
