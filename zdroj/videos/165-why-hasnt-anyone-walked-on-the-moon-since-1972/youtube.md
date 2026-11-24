# YouTube — 165 „Why Hasn't Anyone Walked on the Moon Since 1972?“

Stav: **připraveno k nahrání.** Master `render/final-en-165.mp4` (9:30, 1080p, 207, 2026-11-22)
a americká stopa `render/audio-en-US.m4a` (569,98 s, na mřížku) jsou hotové. Překlady prošly
Codexem, titulky 15 stop jsou v `subtitles/`, lokalizace 13 jazyků v `youtube-preklady.md`.
Náhled `render/thumbnail.jpg` je hotový (koncept C1, viz oddíl 3).

| | |
|---|---|
| ID videa | — (MP4 nahraje uživatel ručně ve Studiu, pak `--k-videu`) |
| master | `render/final-en-165.mp4` — 9:30 (570,0 s), 1080p, 207, 2026-11-22 |
| náhled | `render/thumbnail.jpg` — C1 „1972 / THE LAST STEP?“, původ v `thumbnail/PUVOD.md` |
| nastavení, popis, tagy | podklady níž |
| lokalizace | `youtube-preklady.md`, 13 jazyků (odkaz na web doplněn) |
| titulky | `subtitles/<kód>.srt`, 14 jazyků + `en-US`; Codex na všech 13 překladech |
| americká stopa | `render/audio-en-US.m4a` (`af_heart`), ručně ve Studiu |
| závěrečná obrazovka | S72–S73, **horní polovina** (viz níž) |
| karty | **žádné** (storyboard nemá klíč `karta`) |
| playlist | návrh `vesmir` (viz níž) |
| komentář kanálu | otázka ze S73 v `pripnute-komentare.md`, viz oddíl 8 |
| shorty | `shorts/165-why-hasnt-anyone-walked-on-the-moon-since-1972/` 01-n1, 02-not-interested, 03-lost-plans (vlastní podklady) |

**Co musí uživatel naklikat sám:** závěrečnou obrazovku, americkou audiostopu
(`render/audio-en-US.m4a`), osvědčení o zproštění (pokud ho nevyřídil průvodce nahráním)
a po zveřejnění připnout komentář kanálu.

Stopáž 9:30 (`work/timing.json` total 569,98 s, stav po přesyntéze S16, S23, S46 se „Saturn Five“,
script 0.7).

> Kdyby se znovu pouštěl `tts.py`, přepočítej kapitoly tady i v `youtube-preklady.md`
> a přegeneruj `en-US` přes `us_stopa.py`.

Pořadí podle CENY (`docs/zverejneni.md`):

```bash
V=videos/165-why-hasnt-anyone-walked-on-the-moon-since-1972
# odkaz na web je v youtube.md i youtube-preklady.md už doplněný (odkaz_web.repo)
python tools/nahraj.py $V --k-videu=<ID> --bez-titulku   # 100
python tools/analytics.py --videa                        #   1  ← nutné
python tools/lokalizace.py $V                            #  50
python tools/titulky.py $V --smaz-asr                    # 150  ← před titulky
python tools/titulky.py $V                               # 400×N
python tools/playlisty.py                                #  50
# po zveřejnění: komentář kanálu (vloží i systemd timer)
python tools/komentare.py --jen 165                      #  51
# úklid, až je MP4 na YouTube:
rm $V/render/draft*.mp4
ssh vrana@192.168.0.207 'rm -rf /home/vrana/temp/render-165-why-hasnt-anyone-walked-on-the-moon-since-1972'
```

---

## 1. Titul

```
Why Hasn't Anyone Walked on the Moon Since 1972?
```

> Wh-otázka, 48 znaků, shodná s `project.json`. Původní *Why Haven't We Gone Back to the Moon
> in 50 Years?* (`Témata.fods`) přestal platit: Artemis II s posádkou Měsíc v dubnu 2026 obletěla
> a od Apolla 17 je to 54 let, ne 50 (rozhodl uživatel, `notes.md`). Titul v `Témata.fods`
> přepisuje uživatel.

---

## 2. Popis

```
In April 2026, four astronauts flew around the far side of the Moon, further from Earth than anyone had ever been. Then they turned around and came home. Nobody has stood on the Moon since December 1972. Apollo landed there six times with computers weaker than a modern graphing calculator. So why can't we just do it again?

The usual answer is money, and it isn't wrong. But it only moves the question. This video looks at why anyone was willing to pay for Apollo in the first place, what happened to the Soviet N1 rocket, why the Artemis landing keeps slipping and what a single launch costs, and three less obvious reasons a return takes so long: risk, the knowledge that disappeared when Apollo's factories closed, and a much harder destination at the lunar south pole.

Sources: NASA, Artemis II flight day 6 updates (April 2026); U.S. OMB, Historical Tables (Table 4.1); The Planetary Society, cost of Apollo in 2025 dollars; NASA History Office, Kennedy–Webb meeting recording (November 1962); Space.com, on 1960s public opinion of Apollo (citing R. D. Launius, Space Policy 19, 2003); Gallup, Landing a Man on the Moon: The Public's View; RussianSpaceWeb, N1 launch vehicle; NASA Office of Inspector General, IG-22-003 (2021) and IG-24-011 (2024); A. Malley, interview with Neil Armstrong, CPA Australia (2012); W. Safire, In Event of Moon Disaster (1969), U.S. National Archives; NASA, Artemis I heat shield findings (December 2024); NASA Langley, Apollo fact sheet; Ars Technica, How NASA brought the monstrous F-1 moon rocket back to life (2013); NSSDC, Apollo landing sites; Spaceflight Now, NASA announces major overhaul of Artemis moon program (February 2026); Brookings, The Costs of the Manhattan Project; Popular Science, The Last Moonwalker (July 1999).

Subtitles are written for this video, not auto-generated. An American English audio track is available as a second audio track.

Full transcript, sources and translations: https://theresmoretoit-channel.github.io/videos/why-hasnt-anyone-walked-on-the-moon-since-1972/

CHAPTERS
00:00 Four astronauts, no landing
00:33 The usual answer: money
01:04 The race
01:48 The Soviet Moon rocket
02:23 Once the race was over
02:48 Not quite: Artemis
03:55 Two earlier attempts
04:21 Reason one: risk
05:33 Reason two: the ladder we took apart
06:26 Reason three: a harder goal
06:58 Refuelling in orbit
07:27 Putting it all together
07:49 Apollo's pace and price
08:34 A new race?
09:04 The last man on the Moon

IMAGE CREDITS
Launch Complex 34 — Zgyorko, CC BY-SA 3.0
Saturn V Rocket -- Johnson Space Center — Jim Evans, CC BY-SA 4.0
via Wikimedia Commons
Licences: creativecommons.org/licenses/by-sa/3.0, creativecommons.org/licenses/by-sa/4.0
All other archive images are in the public domain (NASA, NASA/JSC, NASA/MSFC, NASA/GSFC/Arizona State University, Wikimedia Commons).
```

> **Blok se kopíruje CELÝ** (`docs/zverejneni.md`). Kredity ze `sources.json` / `CREDITS.md`
> (16 archivních snímků): **povinná atribuce CC BY-SA jsou dvě** — S21 *Launch Complex 34*
> (Zgyorko, CC BY-SA 3.0) a S23 *Saturn V Rocket -- Johnson Space Center* (Jim Evans,
> CC BY-SA 4.0), obě Wikimedia Commons, formát TASL. Zbylých 14 je volné dílo: 10× NASA Image
> and Video Library (US Government; S29 fotograf Jude Guidry pro NASA) a 4× Commons s licencí
> Public domain (S11 Gagarin, S38 AS08-14-2383, S40 Safireův projev, S55 LRO WAC). Ty se podle
> dokumentu nevypisují.
>
> **Pointa se neprozrazuje:** popis ani kapitoly neříkají, že skutečná záhada je, jak se to
> podařilo napoprvé (S62), ani že Apollo bylo válečné úsilí studené války (S65). Kapitola 07:27 se
> proto jmenuje *Putting it all together*, ne *The real mystery*. Popis končí třemi důvody
> a Čínu (S68–S70) jen naznačuje kapitola *A new race?*.
>
> Kapitoly ze scén S01, S06, S11, S16, S20, S24, S32, S35, S45, S52, S58, S61, S63, S68, S72
> (`work/timing.json`, začátky už obsahují `lead_in` 0,15 s — S01 začíná na 0,15 —, zaokrouhleno
> dolů). První na 00:00, je jich 15, všechny ≥ 10 s (nejkratší S61 → S63 22 s; poslední
> S72 → konec 25 s). Riziko začíná S35 (*„three more reasons“*), protože S35 → S36 je jen 7 s.
> Otázka do komentářů (S73) vlastní kapitolu nemá.
>
> **Zdroje:** primární z `factcheck.md`. Launius je ve factchecku citován z druhé ruky (originál za
> paywallem), proto je v řádku zdrojů jako *Space.com … (citing Launius)* spolu s Gallupem, ne jako
> přečtený článek. U Planetary Society je popis stránky, ne doslovný titul. Řádek s odkazem na web vložen funkcemi
> `tools/odkaz_web.py` (`radek()` / `vloz()`); samotné `--repo` youtube.md přeskočí, dokud není
> commitnutý.

---

## 3. Náhled

`render/thumbnail.jpg` (1280×720, 0,36 MB) je koncept **C1**: poslední stopa v měsíčním prachu
s textem `1972` / `THE LAST STEP?`. Obrázek dodal uživatel z externího nástroje podle
`thumbnail/PROMPT.md`. Původ, otisky a `thumb_check` jsou v `thumbnail/PUVOD.md`. Odpověď videa
z náhledu nevyplývá. Kódem kreslené koncepty C1–C3 zůstávají v `thumbnail/gen.py`.

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
| komentáře | zapnuté (S73 je otázka do komentářů) |
| **byla použita AI** | **ne**. 56 ze 74 scén je kreslených kódem, 16 jsou archivní snímky upravené jen barevně (výslovná výjimka *„color adjustment“*). S57 (malá základna na Měsíci) a S71 (osamělá postava na měsíčním povrchu) jsou malované ilustrace z SDXL s kotvou *painterly editorial illustration*, obecné scény, ne skutečné místo, osoba ani událost. Hlas je syntetický Kokoro `bf_emma`, ne klon skutečné osoby; hudba je procedurální. |

### Karty

Žádné. `storyboard.json` nemá klíč `karta` a scénář na jiné video kanálu neodkazuje.

### Závěrečná obrazovka

Od **9:30 − 20 s ≈ 9:10** (S72 začíná 9:04, S73 9:18). `zaver_check` hlásí S72–S73 OK,
spodní rohy jsou pod titulky. **Dlaždici i odběr dej do HORNÍ poloviny.**
Jako dlaždici navrhuju **125 *Why Is Getting to Orbit So Hard?*** (související video podle
`notes.md`; alternativy 160 *Why Is It So Hard to Bring a Rock Back from Mars?*, 065 *Who Will
Own Mars?*), druhou nechat na „nejlepší pro diváka“.

---

## 6. Tagy

```
moon landing, apollo program, artemis program, artemis ii, nasa, space race, saturn v,
n1 rocket, apollo 11, apollo 17, gene cernan, space history, sls rocket, starship,
lunar south pole, china moon mission, cold war, space exploration, there's more to it
```

---

## 7. Playlist

Návrh **`vesmir`** (*Space — Getting There, and Who Else Is Out There*; je v něm 125 *Getting to
Orbit* i 065 *Who Will Own Mars?*). Rozhodne uživatel; pak dopsat slug do `playlisty.json`,
`analytics.py --videa`, `playlisty.py --jen vesmir`.

---

## 8. Komentář kanálu (otázka ze S73)

Podle `docs/cta.md`, „Táž otázka jako komentář kanálu“: psanou formou, bez *„So here's a question
for you“* a *„Let me know in the comments“*. **Zapsáno v `pripnute-komentare.md`** — musí
být pushnutá a stažená dřív, než video vyjde, jinak ji timer nevloží:

```
If there were no race to win, what reason would be good enough to go back to the Moon?
```

> Proti S73 přidáno *„to the Moon“*, protože komentář se čte bez kontextu videa. Vkládá se až po
> zveřejnění (`komentare.py --jen 165`, nebo systemd timer ve 21:15); připnout ručně ve Studiu.
