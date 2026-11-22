# YouTube — 162 „What Killed Windows Phone?“

Stav: **MP4 nahrané ručně** (`7q6Hw9RbYFw`) 2026-11-20. Přes API hotovo: nastavení, popis, tagy, náhled,
lokalizace 13 jazyků, playlist `legacy` (pozice 27) a titulky **en-GB, en-US, cs, de, pl, es, pt-BR, sv,
fi, id, vi, uk, tr, fr, it** — všech 15 stop. `--smaz-asr`: ASR zatím nevzniklo (9:1x), po zpracování pustit znovu.
**Ručně ve Studiu:** závěrečná obrazovka, karta 9:30 → 076, americká audiostopa.

| | |
|---|---|
| ID videa | `7q6Hw9RbYFw` (https://youtu.be/7q6Hw9RbYFw), MP4 nahrál uživatel ručně ve Studiu 2026-11-20 |
| master | `render/final-en-162.mp4` (207, plné rozlišení) |
| náhled | ✅ `render/thumbnail.jpg` (C1, ChatGPT, 1280×720, 0,32 MB), původ `thumbnail/PUVOD.md` |
| nastavení, popis, tagy | podklady níž |
| lokalizace | `youtube-preklady.md`, 13 jazyků |
| titulky | `subtitles/<kód>.srt`, 14 jazyků + `en-US`; Codex na všech 13 překladech |
| americká stopa | `render/audio-en-US.m4a` (`af_heart`, speed 0,9462), ručně ve Studiu |
| závěrečná obrazovka | S78–S80, **horní polovina** (viz níž) |
| karty | **jedna**, S70 → 076 (`nahraj.py` ji vypíše) |
| playlist | `legacy` |

**Co musí uživatel naklikat sám:** závěrečnou obrazovku, **kartu**, americkou audiostopu
(`render/audio-en-US.m4a`) a osvědčení o zproštění, pokud ho nevyřídil průvodce nahráním.

Stopáž 11:15 (`work/timing.json` total 674,89 s).

> Kdyby se znovu pouštěl `tts.py`, přepočítej kapitoly a čas karty tady i v `youtube-preklady.md`
> a přegeneruj `en-US` přes `us_stopa.py`.

Pořadí podle CENY (`docs/zverejneni.md`):

```bash
V=videos/162-what-killed-windows-phone
python tools/nahraj.py $V --k-videu=7q6Hw9RbYFw --bez-titulku   # 100
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
What Killed Windows Phone?
```

> Wh-otázka, 26 znaků, shodná s `project.json`. Odpověď (zeď aplikací a tři resety, kterými si
> Microsoft uškodil sám) titul neprozrazuje.

---

## 2. Popis

```
In 2013, Microsoft wrote its own YouTube app for Windows Phone, because Google wouldn't. Google wanted it gone, and blocked the rebuilt version too. Microsoft had the money, a design that reviewers loved, and Nokia, then the biggest phone maker on Earth. At its best, Windows Phone ran on about three smartphones in every hundred sold. In 2015, Microsoft wrote off 7.6 billion dollars on the phone business it had bought from Nokia, and two years later it quietly gave up. So what killed it?

This video treats it like a case with five suspects: Steve Ballmer laughing at the iPhone and a launch that came three years and nine months later, a first version without copy and paste, the missing apps from Instagram to Snapchat, Stephen Elop's "burning platform" memo and the MeeGo system Nokia dropped even though its only phone got excellent reviews, and Google, which said it would go where the users are, while Microsoft earned money from Android patents. And then it asks what a 1999 court ruling about Windows on the PC has to do with any of it.

Sources: Microsoft, Nokia impairment and restructuring announcement (July 2015); Gartner and IDC smartphone market share (2010–2014); Steve Ballmer, CNBC interview (January 2007); Stephen Elop, "Burning platform" memo to Nokia staff (February 2011); Nokia and Microsoft strategic partnership announcement (February 2011) and Nokia Devices and Services acquisition (September 2013); Microsoft, Windows Phone 8 announcement (June 2012) and Windows 10 Mobile end of support (December 2019); Joe Belfiore's statements on Windows Phone (October 2017); Microsoft v. Samsung court filing (2014); United States v. Microsoft, Findings of Fact (November 1999).

Subtitles are written for this video, not auto-generated. An American English audio track is available as a second audio track.

Full transcript, sources and translations: https://theresmoretoit-channel.github.io/videos/what-killed-windows-phone/

CHAPTERS
00:00 Microsoft's YouTube app
01:02 Five suspects
01:15 Suspect one: time
02:15 Suspect two: the phone
02:54 Suspect three: the apps
03:33 Case closed?
04:33 Suspect four: Nokia
05:45 A Trojan horse?
06:28 Suspect five: Google
06:55 Microsoft's money from Android
07:37 A suspect we missed
09:00 Back to 1999
10:10 The verdict
10:36 What happened next

IMAGE CREDITS
Steve Ballmer 2007 — Martin Olsson, CC BY-SA 3.0
Stephen Elop — luca.sartoni, CC BY-SA 2.0
Blue Nokia N9 — Bytearray render, CC BY-SA 3.0
Nokia Lumia 920 white — SoloveiYegor, CC BY-SA 3.0, retouched (operator branding removed)
Nokia Lumia 900 black — Shineyalight, CC BY-SA 3.0
via Wikimedia Commons
Licences: creativecommons.org/licenses/by-sa/3.0/ and creativecommons.org/licenses/by-sa/2.0/
```

> **Blok se kopíruje CELÝ** (`docs/zverejneni.md`). Kredity ze `sources.json`: všech pět
> archivních snímků je **CC BY-SA, atribuce povinná** a všech pět jmen je uvnitř bloku.
> U S44 je retuš uvedená, protože BY-SA žádá označit změny (`LICENSES.md`). Kontakt
> z pole autora S12 (e-mail Martina Olssona) se do popisu záměrně nepřenáší.
>
> **Pointa se neprozrazuje:** popis ani kapitoly neříkají, že šestým podezřelým je Microsoft
> (S56) ani že vrahem je bariéra vstupu (S67, S76). Kapitola 07:37 je S55 *„Which means we've
> missed one“*, ne S56. Rok 1999 v popisu jen láká, co s tím soud má společného.
>
> Kapitoly ze scén S01, S09, S11, S18, S23, S28, S36, S42, S47, S50, S55, S65, S74, S77
> (`work/timing.json`, zaokrouhleno dolů). První na 00:00, všechny ≥ 10 s (nejkratší
> S09 → S11 13 s; poslední S77 → konec 39 s). Otázka do komentářů (S80) vlastní kapitolu nemá.
>
> **Zdroje:** primární a hlavní sekundární z `factcheck.md`. Odkaz na web vznikne až po
> `tools/web_publikuj.sh` (viz `docs/web.md`).

---

## 3. Náhled

**C1** z `thumbnail/ZADANI.md`: telefon s barevnými dlaždicemi a přivázaným štítkem,
`WINDOWS PHONE` / `WHO DID IT?`. Nakreslil ChatGPT, dodávka `render/thumbnail.jpg` (1280×720,
0,32 MB), původ a otisk v `thumbnail/PUVOD.md`. `thumb_check`: jas 77,7, kontrast 90,5,
ve 150 px čitelné. Nahraje ho `nahraj.py`.

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
| komentáře | zapnuté (S80 je otázka do komentářů) |
| **byla použita AI** | **ne**. 76 z 82 scén je kreslených kódem, pět archivních snímků z Commons je upravených barevně a ořezem, S44 navíc retuší loga operátora (bez AI, klasickou výplní). S39 (hořící ropná plošina v noci, metafora z Elopova memoranda) je malovaná ilustrace z SDXL (kotva *painterly editorial illustration*), obecná scéna, ne skutečné místo ani událost. Hudba je procedurální, hlas není klon skutečné osoby. |

### Karty

| čas | scéna | cíl |
|---|---|---|
| **~9:32** | S70 *We've looked at how that wall made Windows on the PC* | 076 *How Did Windows Win Without Inventing the GUI?* (`crb68Ur-OTI`) |

> Čas je ze začátku scény + ~2 s; přesný vypíše `nahraj.py` z `work/timing.json`.

### Závěrečná obrazovka

Od **11:15 − 20 s ≈ 10:55** (začátek S78 je 10:49). `zaver_check` hlásí S78–S80 OK, spodní
rohy jsou pod titulky. **Dlaždici i odběr dej do HORNÍ poloviny.**
Jako dlaždici navrhuju **076 *How Did Windows Win Without Inventing the GUI?*** (táž zeď
z druhé strany, S70 na něj odkazuje), druhou nechat na „nejlepší pro diváka“.

---

## 6. Tagy

```
windows phone, microsoft, nokia, lumia, stephen elop, burning platform, steve ballmer,
iphone, android, symbian, meego, nokia n9, app gap, windows 10 mobile, smartphone history,
tech history, network effects, there's more to it
```

---

## 7. Playlist

**`legacy`** (je v něm 076 i 129). Dopsat slug do `playlisty.json`, `analytics.py --videa`,
`playlisty.py --jen legacy`.
