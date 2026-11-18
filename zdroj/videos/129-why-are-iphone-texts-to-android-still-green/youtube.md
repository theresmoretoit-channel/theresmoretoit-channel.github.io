# YouTube — 129 „Why Are iPhone Texts to Android Still Green?“

Stav: **MP4 nahráno ručně ve Studiu 2026-10-31; metadata, náhled, lokalizace (13 jazyků) 2026-10-31, titulky (15 stop) dokončeny 2026-11-01, playlist `legacy` hotový. Zbývá jen ruční část ve Studiu (níž).** Stav zveřejnění je v `Témata.fods`.

| | |
|---|---|
| ID videa | `GmsmPef4j9c` |
| master | ✅ `render/final-en-129.mp4` (7:48, 1920×1080, 468,1 s, herní PC) |
| náhled | ✅ `render/thumbnail.jpg` z konceptu C1 (`thumbnail/PUVOD.md`) |
| nastavení, popis, tagy | podklady níž |
| lokalizace | `youtube-preklady.md`, 13 jazyků |
| titulky | `subtitles/*.srt`, 14 jazyků + `en-US` (Codex hotový, nálezy zapracované) |
| americká stopa | `render/audio-en-US.m4a`, ručně ve Studiu |
| závěrečná obrazovka | od **7:28**, S93–S96, prvky **nahoru** (viz níž) |
| karta | žádná (scénář na starší video neodkazuje) |
| playlist | `legacy` (*Legacy Tech*), na konec za 128 |

**Co musí uživatel naklikat sám:** závěrečnou obrazovku, americkou
audiostopu (`render/audio-en-US.m4a`) a osvědčení o zproštění, pokud ho
nevyřídil průvodce nahráním.

Stopáž 7:48 (`work/timing.json` total 468,02 s).

> Kdyby se znovu pouštěl `tts.py`, přepočítej kapitoly tady
> i v `youtube-preklady.md` a přegeneruj `en-US` přes `us_stopa.py`.

Pořadí podle CENY (`docs/zverejneni.md`):

```bash
V=videos/129-why-are-iphone-texts-to-android-still-green
python tools/nahraj.py $V --k-videu=GmsmPef4j9c --bez-titulku          # 100
python tools/analytics.py --videa                               #   1  ← nutné
python tools/lokalizace.py $V                                   #  50
python tools/titulky.py $V --smaz-asr                           # 150  ← před titulky
python tools/titulky.py $V                                      # 400×15
python tools/playlisty.py                                       # 100
# úklid, až je MP4 na YouTube:
rm $V/render/draft*.mp4
ssh vrana@192.168.0.207 'rm -rf /home/vrana/temp/render-129-why-are-iphone-texts-to-android-still-green'
```

---

## 1. Titul

```
Why Are iPhone Texts to Android Still Green?
```

> Wh-otázka, 44 znaků, shodná s `project.json`. Odpověď (modrá je
> vyhrazená zprávám, které nese Apple; RCS není iMessage, S84–S90) titul
> neprozrazuje.

---

## 2. Popis

```
Send a message from one iPhone to another and it shows up blue. Send the same message to an Android phone and it turns green. In 2024 the iPhone finally got support for the same modern messaging standard Android phones use, so why are the bubbles still green?

This video follows the two roads a message can take: why green was there first and blue came later, what falling back to the old road did to group chats, videos and reactions, and why the colour became a social thing in America while most of the world barely noticed.

Along the way: emails from a court case showing Apple executives discussing iMessage on Android back in 2013, "Buy your mom an iPhone", Google's long line of messaging apps, RCS, Beeper Mini, and what changed in 2023 and 2024.

Sources: Apple Support, "If you see a green message bubble on your iPhone" (105087); United States et al. v. Apple Inc., complaint (2024); Epic Games v. Apple, Findings of Fact and Conclusions of Law (2021); T. Higgins, "Why Apple's iMessage Is Winning: Teens Dread the Green Text Bubble", The Wall Street Journal (2022); Piper Sandler, Taking Stock With Teens (fall 2022); J. Gruber, "Seeing Green", Daring Fireball (2022); Apple statement on RCS Universal Profile (November 2023); Apple Newsroom, end-to-end encrypted RCS messaging (May 2026); GSMA, RCS Universal Profile.

Subtitles are written for this video, not auto-generated. An American English audio track is available as a second audio track.

IMAGE CREDITS
iPhone First Generation 8GB — Carl Berkeley, CC BY-SA 2.0
Robert F. Kennedy Department of Justice Building — APK, CC BY 4.0
Tim Cook, March 2026 — Tessa Bury, CC BY 4.0
via Wikimedia Commons
Licences: creativecommons.org/licenses/by-sa/2.0, creativecommons.org/licenses/by/4.0
World map: BlankMap-World by Canuckguy, after the CIA World Factbook, public domain

Full transcript, sources and translations: https://theresmoretoit-channel.github.io/videos/why-are-iphone-texts-to-android-still-green/

CHAPTERS
00:00 Blue and green
00:34 Green came first
01:10 Two roads
02:29 What falling back cost
02:56 A social thing in America
03:33 The rest of the world shrugged
04:30 Why not iMessage on Android?
05:11 Google and RCS
05:51 The turn: 2023 to 2024
06:49 So why is it still green?
07:15 Who owns the road
```

> **Blok se kopíruje CELÝ** (`docs/zverejneni.md`). Archiv má tři snímky
> (`CREDITS.md`), všechny CC, všechny v TASL uvnitř bloku: S09 iPhone
> (Carl Berkeley, BY-SA 2.0), S42 budova DOJ (APK, BY 4.0), S63 Tim Cook
> (Tessa Bury, BY 4.0). Mapa (`art/PUVOD.md`) je public domain, uvedená
> jako zdvořilost.
>
> **Pointa se neprozrazuje.** Popis položí titulní otázku ze S05–S07
> a jmenuje témata, ne odpověď (S84–S95). „Green was there first and blue
> came later“ je první překvapení (S08–S13), ne pointa.
>
> **Nic netvrdí víc než video** (`factcheck.md`): 2024 podpora RCS (S05,
> iOS 18), e-maily ze soudního sporu z roku 2013 (S60, Epic FFCL ¶ 58),
> citát (S64, DOJ ¶ 92), „most of the world barely noticed“ = S46
> „barely registered“ (ZMÍRNIT, proto opatrně), 2023 ohlášení a 2024
> nasazení RCS (S73–S80).
>
> Kapitoly ze scén S01, S08, S16, S33, S38, S45, S58, S65, S73, S84, S91
> (`work/timing.json`, zaokrouhleno dolů). Nejkratší má 26 s (S84 → S91),
> poslední 32 s (S91 → konec), všechny ≥ 10 s. Výzvy k odběru (za S30
> a S64) leží uvnitř kapitol.
>
> Zdroje jsou z `factcheck.md` (primární, kde to šlo); sekundární zprávy
> (9to5Mac, TechCrunch, Computerworld) se neuvádějí.

---

## 3. Náhled

Koncept **C1** z `thumbnail/ZADANI.md` (jedna zelená bublina,
STILL GREEN / BUT WHY?), obrázek z ChatGPT. Původ, otisk a `thumb_check`
v `thumbnail/PUVOD.md`.

---

## 4. Titulky

`subtitles/*.srt`, 14 jazyků + `en-US`. Jazyk videa **`en-gb`** (hlas
`bf_emma`) se musí nastavit dřív, než se nahrají titulkové stopy.
Codex prošel všech 13 překladů a nálezy jsou zapracované.

---

## 5. Nastavení

| | |
|---|---|
| kategorie | **Science & Technology** (28), posílá `nahraj.py` napevno |
| jazyk videa | `en-gb` |
| licence | standardní |
| pro děti | **ne** |
| komentáře | zapnuté (S96 končí otázkou do komentářů) |
| **byla použita AI** | **ne**. Jediná SDXL scéna (S38, chodba školy, lidé zezadu bez obličejů) je malovaná ilustrace podle kotvy stylu, ne fotorealismus, a nezobrazuje konkrétní místo ani událost. Tři archivní snímky jsou upravené jen barevně, ostatní scény jsou kresba kódem (30 animovaných). Hudba procedurální, hlas není klon. |

### Závěrečná obrazovka

Od **7:28** (posledních 20 s z 468,0), tedy S93–S96 (od 444,1 s).
Horní polovina je ve všech čtyřech scénách volná (`zaver_check` OK),
**dlaždici i kolečko odběru dej nahoru**. Jako dlaždici doporučuju
**018 *Why Is 2G Still Everywhere?*** (`gMqVXGx4VXw`): táž „stará cesta“
mobilní sítě, po které jezdí SMS, a nejvyšší CTR kanálu. Až vyjde 128
(*How Did a 160-Character Message Become a Gold Mine?*), je to ještě
bližší pokračování (SMS, 160 znaků ze S20).

---

## 6. Tagy

```
why are iphone texts green, green bubble, blue bubble, imessage, iphone to android,
green text bubble, rcs, rcs messaging, sms, mms, imessage on android,
buy your mom an iphone, beeper mini, google messages, whatsapp,
apple antitrust, tech explainer, there's more to it
```

---

## 7. Playlist

**`legacy`** (*Legacy Tech — The Old Systems Still Running Everything*),
na konec za 128: SMS jako stará cesta, která funguje se všemi, je přesně
téma toho playlistu.
