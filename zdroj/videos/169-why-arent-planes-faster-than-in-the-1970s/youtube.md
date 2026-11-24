# YouTube — 169 „Why Aren't Planes Faster Than in the 1970s?“

Stav: **podklady hotové, master se renderuje** (2026-11-24). Draft schválený, náhled
`render/thumbnail.jpg` zatím není (koncepty `thumb-c1`–`c3` v `thumbnail/` čekají na výběr). Americká stopa
`render/audio-en-US.m4a` je hotová. Překlady prošly Codexem, titulky 15 stop jsou v `subtitles/`,
lokalizace 13 jazyků v `youtube-preklady.md`.

| | |
|---|---|
| ID videa | `35GIIKedEro` — https://www.youtube.com/watch?v=35GIIKedEro (MP4 nahrál uživatel 2026-11-24) |
| master | `render/final-en-169.mp4` (536,76 s, 207), stopáž 8:56 (536,70 s) |
| náhled | `render/thumbnail.jpg` — C1 machmetr přes obrázkový nástroj, viz `thumbnail/PUVOD.md` |
| nastavení, popis, tagy | podklady níž |
| lokalizace | `youtube-preklady.md`, 13 jazyků (odkaz na web doplněn) |
| titulky | `subtitles/<kód>.srt`, 14 jazyků + `en-US`; Codex na všech 13 překladech |
| americká stopa | `render/audio-en-US.m4a` (`af_heart`), ručně ve Studiu |
| závěrečná obrazovka | S65–S67, `zaver_check` OK, **horní polovina** (viz níž) |
| karty | **žádné** (storyboard nemá `"karta"`, scénář na jiné video neodkazuje) |
| playlist | návrh **`bezne`**, rozhodne uživatel (viz oddíl 7) |
| komentář kanálu | otázka ze S67, viz oddíl 8 — zapsaná v `pripnute-komentare.md` |
| shorty | `shorts/169-why-arent-planes-faster-than-in-the-1970s/` (vlastní podklady) |

**Co musí uživatel naklikat sám:** závěrečnou obrazovku, americkou audiostopu
(`render/audio-en-US.m4a`), osvědčení o zproštění (pokud ho nevyřídil průvodce nahráním)
a po zveřejnění připnout komentář kanálu.

Stopáž 8:56 (`work/timing.json` total 536,704 s, script 0.7).

> Kdyby se znovu pouštěl `tts.py`, přepočítej kapitoly tady i v `youtube-preklady.md`
> a přegeneruj `en-US` přes `us_stopa.py`.

Pořadí podle CENY (`docs/zverejneni.md`):

```bash
V=videos/169-why-arent-planes-faster-than-in-the-1970s
# odkaz na web je v youtube.md i youtube-preklady.md už doplněný (odkaz_web.radek/vloz)
python tools/nahraj.py $V --k-videu=35GIIKedEro --bez-titulku   # 100
python tools/analytics.py --videa                        #   1  ← nutné
python tools/lokalizace.py $V                            #  50
python tools/titulky.py $V --smaz-asr                    # 150  ← před titulky
python tools/titulky.py $V                               # 400×N
python tools/playlisty.py                                #  50
# po zveřejnění: komentář kanálu (vloží i systemd timer)
python tools/komentare.py --jen 169                      #  51
# úklid, až je MP4 na YouTube:
rm $V/render/draft*.mp4
ssh vrana@192.168.0.207 'rm -rf /home/vrana/temp/render-169-why-arent-planes-faster-than-in-the-1970s'
```

---

## 1. Titul

```
Why Aren't Planes Faster Than in the 1970s?
```

> Wh-otázka, 43 znaků, shodná s `project.json`. Neprozrazuje odpověď (zeď ze vzduchu ani to,
> že vyhrála cena).

---

## 2. Popis

```
In 1977, you could fly from London to New York in about three and a half hours. Today, the same trip takes around seven or eight. And it isn't just Concorde: the Boeing 747 entered service in 1970 cruising at about 85 percent of the speed of sound, and the newest airliners flying today cruise at about 85 percent of the speed of sound. In those fifty-odd years, computers went from filling rooms to fitting in pockets. The speed of a passenger jet barely moved. Did we forget how to build fast planes?

No. We hit a wall, and the wall is made of air. This video follows that wall and what it costs to get past it: shock waves on top of the wing, the price of fuel, Richard Whitcomb's supercritical wing at NASA, the Convair 990 that entered service as the fastest airliner in the world, Concorde and its sonic boom, the 1973 US ban on supersonic flight over land, and Boeing's Sonic Cruiser in 2001. Then it looks at what airliners got better at instead, and at NASA's X-59, built to make a much quieter boom.

Sources: British Airways, Celebrating Concorde, and Concorde retirement announcement (2003); IATA, Airline Profitability Outlook (2024); NASA, How a NASA Engineer Created the Modern Airplane Wing; IPCC, Aviation and the Global Atmosphere (1999); HistoryNet, Why Convair's Speedy 990 Lost Out to the Boeing 707; NOVA (PBS), Concorde fuel use per passenger; U.S. Air Force, sonic boom fact sheet; FAA, 14 CFR 91.817, civil supersonic flight over the United States (1973); Heritage Concorde, on the Pan Am and TWA options (1973); Britannica, Travel Weekly (20 August 1997) and The Washington Post (26 October 1997), on Concorde fares; Flight International, Sonic Cruiser: a different Boeing; Associated Press (November 2002) and NPR (21 December 2002), on the end of the Sonic Cruiser; ICCT, Efficiency Trends for New Commercial Jet Aircraft, 1960 to 2008 (2009); U.S. GAO, GAO-06-630 (2006); ICAO via World Bank, Air transport, passengers carried; NASA, X-59 first supersonic flight (June 2026); Federal Register 2026-13440, Enabling Supersonic Overland Flight, proposed rule (2 July 2026); Forecast International, Boom Supersonic Overture programme outlook (August 2025).

Subtitles are written for this video, not auto-generated. An American English audio track is available as a second audio track.

Full transcript, sources and translations: https://theresmoretoit-channel.github.io/videos/why-arent-planes-faster-than-in-the-1970s/

CHAPTERS
00:00 Fifty years at the same speed
00:50 A wall made of air
01:37 Paid for in fuel
02:32 Whitcomb's wing
02:55 The fastest airliner in the world
03:22 Straight through the wall
04:27 Bad timing
05:13 Faster or cheaper?
06:21 Better at something else
07:35 A quieter boom

IMAGE AND SOUND CREDITS
N736PA Clipper Victor Pan Am Boeing 747-121, London Heathrow — Paul Seymour, CC BY-SA 4.0
Concorde 1 94-9-5 kix (cropped) — Spaceaero2, CC BY-SA 3.0
Boeing 787-8 maiden flight overhead view — Dave Sizer, derivative work by Altair78, CC BY-SA 3.0
via Wikimedia Commons
Sonic boom sound: AirMan (SoundBible), CC BY 3.0, via Wikimedia Commons
https://commons.wikimedia.org/wiki/File:Sonic-boom-massive-sound.ogg
Shortened; the quieter X-59 "thump" is an illustration filtered from the same recording.
Licences: creativecommons.org/licenses/by-sa/4.0 · creativecommons.org/licenses/by-sa/3.0 · creativecommons.org/licenses/by/3.0
All other archive images are in the public domain (Wikimedia Commons).
```

> **Blok se kopíruje CELÝ** (`docs/zverejneni.md`). Kredity ze `sources.json` / `CREDITS.md`
> (6 archivních snímků) a `zvuk/ukazky.py`: **povinná atribuce je u čtyř** — S04 747 (Paul
> Seymour, CC BY-SA 4.0), S29 Concorde (Spaceaero2, CC BY-SA 3.0), S50 787 (Dave Sizer,
> odvozené dílo Altair78, CC BY-SA 3.0) a **zvuk třesku** v S32 (AirMan / SoundBible, CC BY 3.0,
> Commons; SHA-256 v `zvuk/ukazky.py`). S22 (NASA Armstrong), S25 (SAS) a S59 (NASA/Jim Ross)
> jsou public domain.
>
> **Úprava zvuku je uvedená záměrně** (CC BY žádá označit odvozené dílo): S32 je jen zkrácená
> nahrávka, ale „thump“ v S59 je z téže nahrávky filtrovaný a s ozvěnou — **skutečná nahrávka
> X-59 neexistuje** a bez té věty by si ji divák mohl splést s ní.
>
> **Pointa se neprozrazuje:** popis končí výčtem cest, nepíše „Cheaper won“ (S46), že se letadla
> zlepšila ve spotřebě a ceně (S51–S54), ani „We were watching the wrong number“ (S57). Prozrazená
> je jen zeď ze vzduchu, která ve videu zazní v 0:45 (S08). Kapitola 06:21 je proto *Better at
> something else* (S50 doslova), ne *The wrong number*.
>
> Kapitoly ze scén S01, S09, S15, S22, S25, S28, S36, S41, S49, S58 (`work/timing.json`, začátky
> obsahují `lead_in` 0,15 s, zaokrouhleno dolů). Hranice sedí na blokové pauzy storyboardu
> (2,2–2,4 s za S08, S14, S21, S40; 2,6 za S57) a na menší předěly (1,4 za S24 a S27→S28 je
> most „straight through it?“, 0,9 za S35). Pauza 4,0 s za S32 hranice není: je to místo pro
> zvuk třesku, S33 o třesku pokračuje. První kapitola na 00:00, je jich 10, všechny ≥ 10 s
> (nejkratší S22 → S25 23 s; poslední S58 → konec 81 s). Otázka do komentářů (S67) vlastní
> kapitolu nemá.
>
> **Zdroje:** z `factcheck.md`. Část má ve factchecku značku **U** (zdroj jmenovala kontrola
> uživatele, agent ho neotvíral): British Airways, IATA, NASA o Whitcombovi, IPCC, USAF, FAA,
> Heritage Concorde, AP. Název NOVA/PBS je popisný (stránka je učitelská aktivita bez titulku
> v evidenci), stejně USAF. Wikipedia a aerocorner se neuvádějí, stojí na nich jen pomocná
> tvrzení. Řádek s odkazem na web vložen funkcemi `tools/odkaz_web.py` (`radek()` / `vloz()`);
> samotné `--repo` youtube.md přeskočí, dokud není commitnutý.

---

## 3. Náhled

**Zatím není vybraný.** V `thumbnail/` jsou koncepty c1 machmetr, c2 concorde, c3 tabule (`render/thumb-c*.jpg`), `render/thumbnail.jpg` chybí. Podle
`docs/thumbnail-styl.md`: jeden koncept, otázka bez odpovědi (náhled nesmí ukázat, že vyhrála
cena / úspornost). `nahraj.py --k-videu` jde pustit i bez náhledu (`thumbnails.set` za 50 jednotek
kdykoli potom).

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
| komentáře | zapnuté (S67 je otázka do komentářů) |
| **byla použita AI** | **ne**. 59 ze 67 scén je kreslených kódem, 6 jsou archivní snímky upravené jen barevně (výslovná výjimka *„color adjustment“*). S41 a S58 jsou malované ilustrace z SDXL s kotvou stylu (stratosféra, kondenzační stopy), obecné scény, ne skutečné místo, osoba ani událost. Zvuk třesku je skutečná nahrávka (CC BY 3.0), „thump“ X-59 je z ní odvozený filtrem, ne z generativního modelu a v popisu je označený jako ilustrace. Hlas je syntetický Kokoro `bf_emma`, ne klon skutečné osoby; hudba je procedurální. |

### Karty

**Žádné.** Storyboard nemá klíč `"karta"` a scénář na jiné video kanálu neodkazuje.

### Závěrečná obrazovka

Od **8:56 − 20 s ≈ 8:36** (S65 začíná 8:33, S66 8:39, S67 8:48). `zaver_check` hlásí S65–S67 OK
(kresba 0,9–4,5 %), obě dolní rohy jsou pod titulky → **dlaždici i odběr do horní poloviny**.
Jako dlaždici navrhuju **002 *Where Does Jet Fuel Go?*** (palivo je osou celého videa;
alternativy 079 DC-3 — táž logika „rozhoduje cena provozu“, 165 Měsíc od 1972), druhou nechat
na „nejlepší pro diváka“.

---

## 6. Tagy

```
why aren't planes faster, concorde, supersonic flight, sonic boom, speed of sound, boeing 747,
boeing 707, transonic drag, shock wave, supercritical wing, richard whitcomb, convair 990,
boeing sonic cruiser, boeing 787, airline economics, jet fuel, nasa x-59, boom supersonic,
aviation history, there's more to it
```

---

## 7. Playlist

**Návrh `bezne`** (*Ordinary Things, Awkward Questions*; je v něm 002 *Where Does Jet Fuel Go?*).
Alternativy: `spolecnost` (*How Society Actually Runs* — ekonomika rozhodnutí aerolinek)
nebo `legacy` (je v něm 079 DC-3). Rozhodne uživatel; pak dopsat slug do `playlisty.json`,
`analytics.py --videa`, `playlisty.py --jen <klíč>`.

---

## 8. Komentář kanálu (otázka ze S67)

Podle `docs/cta.md`, „Táž otázka jako komentář kanálu“: psanou formou, bez *„So here's a question
for you“* a *„Let me know in the comments“*. **Zapsaná v `pripnute-komentare.md`** (2026-11-24) — musí být pushnutá
a stažená dřív, než video vyjde, jinak ji timer nevloží:

```
How much would you pay to land three hours earlier?
```

> Beze změny proti S67; „three hours“ se čte i bez kontextu videa (Concorde 3,5 h proti 7–8 h
> dnes je v první větě popisu).
