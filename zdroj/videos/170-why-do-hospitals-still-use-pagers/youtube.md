# YouTube — 170 „Why Do Hospitals Still Use Pagers?“

Stav: **naplánováno na 2. 12. 2026 21:00** (2026-11-25), titulky 15 stop, ruční kroky hotové. Draft schválený, `script 0.8`.

| | |
|---|---|
| ID videa | `qVEjJeOPypo` — https://www.youtube.com/watch?v=qVEjJeOPypo (MP4 nahrál uživatel 2026-11-25) |
| master | `render/final-en-170.mp4`, 563,5 s, 207, dekódování čisté, −14,0 LUFS; stopáž 9:23 (563,467 s) |
| náhled | `render/thumbnail.jpg` — C3 (telefon a pager) přes obrázkový nástroj, viz `thumbnail/PUVOD.md` |
| lokalizace | `youtube-preklady.md`, 13 jazyků |
| titulky | `subtitles/<kód>.srt`, 14 jazyků + `en-US`; překlady 1× Codex |
| americká stopa | `render/audio-en-US.m4a` (`af_heart` 0,9522), ručně ve Studiu |
| závěrečná obrazovka | S68–S69 (od 9:03), **horní polovina** (níž) |
| karty | žádné |
| playlist | **`legacy`** (zařazeno 2026-11-25) |
| komentář kanálu | otázka ze S69, zapsaná v `pripnute-komentare.md` |
| shorty | `shorts/170-why-do-hospitals-still-use-pagers/` (vlastní podklady) |

**Ručně ve Studiu:** závěrečná obrazovka, americká audiostopa, osvědčení o zproštění (pokud ho
nevyřídil průvodce) a po zveřejnění připnout komentář.

> Kdyby se znovu pouštěl `tts.py`, přepočítej kapitoly tady i v `youtube-preklady.md` a přegeneruj
> `en-US` přes `us_stopa.py`.

```bash
V=videos/170-why-do-hospitals-still-use-pagers
python tools/nahraj.py $V --k-videu=qVEjJeOPypo --bez-titulku   # 100
python tools/analytics.py --videa                              #   1  ← nutné
python tools/lokalizace.py $V                                  #  50
python tools/titulky.py $V --smaz-asr                          # 150  ← před titulky
python tools/titulky.py $V                                     # 400×N
python tools/playlisty.py                                      #  50
python tools/komentare.py --jen 170                            #  51  po zveřejnění (vloží i timer)
rm $V/render/draft*.mp4
ssh vrana@192.168.0.207 'rm -rf /home/vrana/temp/render-170-why-do-hospitals-still-use-pagers'
```

---

## 1. Titul

```
Why Do Hospitals Still Use Pagers?
```

---

## 2. Popis

```
In 2026, a hospital doctor starts a shift with a smartphone in one pocket and, clipped to the belt, a pager: a small plastic box that can only beep and show a line of text. In a survey published in 2017, almost eight in ten of the American hospital clinicians who answered had been given one by their hospital. In 2019, the British government ordered the NHS to stop using pagers for everyday messages by the end of 2021. In the summer of 2026, they were still in use. So why won't it go away?

The answer starts with one strange fact about how a pager works: it never says anything. This video follows what comes out of that one decision: a battery that can last for weeks, radio inside thick concrete, what happens when everyone reaches for a phone at once, and a call that has to reach a whole team in the same second. Then it looks at the price, from messages nobody can confirm to patients' details picked up with a cheap radio receiver, and at what happened in 2022, when Cambridge University Hospitals moved its everyday messages to an app.

Sources: O'Leary et al., Hospital-Based Clinicians' Use of Technology for Patient Care-Related Communication: A National Survey, Journal of Hospital Medicine (2017); Ercole et al., Moving from non-emergency bleeps and long-range pagers to a hospital-wide, EHR-integrated secure messaging system, BMJ Health & Care Informatics (2023); GOV.UK, Health and Social Care Secretary bans pagers from the NHS (2019); Lemelson-MIT, Al Gross; Computerworld, on communications after Hurricane Katrina (2 September 2005); NPSA, Patient Safety Alert on the 2222 crash call number (2004); Trend Micro, Leaking Beeps, and Unsecure Pagers in Vancouver Expose Sensitive Patient Data; Open Privacy Research Society, on Vancouver pagers (2019); Computing, on NHS Blood and Transplant pager messages (14 August 2026).

Subtitles are written for this video, not auto-generated. An American English audio track is available as a second audio track.

Full transcript, sources and translations: https://theresmoretoit-channel.github.io/videos/why-do-hospitals-still-use-pagers/

CHAPTERS
00:00 A pager in 2026
01:15 It only listens
02:31 Weeks on one battery
03:00 Inside the building
03:51 On the worst day
04:27 A whole team at once
05:04 The price
06:15 Enter the app
07:23 Why it won't go away
08:24 An awkward question

IMAGE CREDITS
Motorola Pager 2 — Jakez, CC BY-SA 3.0, via Wikimedia Commons
Licence: creativecommons.org/licenses/by-sa/3.0
All other archive images are in the public domain (Wikimedia Commons).
```

> **Blok se kopíruje CELÝ.** Povinná atribuce jen u S03 (Jakez, CC BY-SA 3.0); S31 (U.S. Coast Guard)
> a S50 (Addenbrooke's) jsou public domain.
>
> **Pointa se neprozrazuje:** popis neříká, že nemocnice posílá dva druhy zpráv (S55), ani která
> tři volání se přesouvat neměla (S52). Že pager nevysílá, zazní ve videu v 1:20.
>
> Kapitoly ze scén S01, S11, S20, S23, S29, S33, S38, S48, S55, S63 (`work/timing.json`, zaokrouhleno
> dolů), je jich 10, první na 00:00, nejkratší 29 s. Zdroje z `factcheck.md`; NPSA 2004, Computerworld
> a Computing jsou ve factchecku značkou S (sekundární).

---

## 3. Náhled

**`render/thumbnail.jpg`**, koncept C3, dodal uživatel 2026-11-25. Náhled nesměl prozradit dva druhy zpráv, poplach ani běžící tým.

---

## 4. Titulky

`subtitles/<kód>.srt` pro 14 jazyků a `en-US`. Jazyk videa **`en-gb`** nastaví `nahraj.py`.

---

## 5. Nastavení

| | |
|---|---|
| kategorie | **Science & Technology** (28) |
| jazyk videa | `en-gb` |
| licence | standardní |
| pro děti | **ne** |
| komentáře | zapnuté |
| **byla použita AI** | **ne**. 64 ze 69 scén je kreslených kódem, 3 jsou archivní snímky upravené jen barevně. S24 a S29 jsou malované ilustrace ze SDXL (obecná chodba, nemocnice v bouři), ne skutečné místo ani událost. Hlas je syntetický Kokoro `bf_emma`, ne klon; hudba procedurální. |

### Závěrečná obrazovka

Od **9:03**. S68–S69 mají prázdnou horní polovinu, dolní rohy jsou pod titulky → **dlaždice i odběr
do horní poloviny**. Dlaždice: návrh **018 *Why Is 2G Still Everywhere?*** (stará technologie, která
drží dál; nejvyšší CTR kanálu), druhá „nejlepší pro diváka“.

---

## 6. Tagy

```
why do hospitals still use pagers, pager, pagers, hospital pager, beeper, pocsag, nhs pagers, paging network,
hospital communication, crash call, cardiac arrest team, secure messaging, cambridge university hospitals,
addenbrooke's, al gross, hospital technology, radio, legacy technology, medical technology, there's more to it
```

---

## 7. Playlist

**`legacy`** (*Legacy Tech — The Old Systems Still Running Everything*), potvrdil uživatel 2026-11-25.

---

## 8. Komentář kanálu (otázka ze S69)

```
In an emergency, would you rather get a message you can answer, or one designed to reach you when everything else fails?
```
