# YouTube — 086 „Why Did a Blue Flash Kill a Scientist Nine Days Later?"

Stav: **nahráno 2026-10-03** — https://www.youtube.com/watch?v=IWQ3E7kSeJ8

| | |
|---|---|
| ID videa | `IWQ3E7kSeJ8` |
| nastavení, popis, tagy | ✅ |
| náhled | ✅ C1 (`thumbnail/c1-koule.png`) |
| lokalizace | ✅ 13 jazyků |
| automatický přepis | ✅ čisté |
| titulky | ✅ `en`, `en-US` přes API, zbylých 13 jazyků uživatel ručně ve Studiu |
| playlist | ✅ `fyzika`, na konci |
| závěrečná obrazovka, americká stopa | ✅ uživatel ve Studiu |

**Co musí uživatel naklikat sám:** nahrát MP4 ve Studiu (průvodce vyřídí
prohlášení o AI — odpověď **ne** — a osvědčení o zproštění), závěrečnou
obrazovku a americkou audiostopu (`render/audio-en-US.m4a`).

Soubor k nahrání: `render/final-en-086.mp4` (stopáž 9:07, `work/timing.json`
total 547,4 s).

Pořadí podle CENY (`docs/zverejneni.md`):

```bash
V=videos/086-why-did-a-blue-flash-kill-a-scientist
python tools/nahraj.py $V --k-videu=<ID> --bez-titulku    # 100
python tools/analytics.py --videa                         #   1  ← nutné
python tools/lokalizace.py $V                             #  50
python tools/titulky.py $V --smaz-asr                     # 150  ← před titulky
python tools/titulky.py $V                                # 400×15
python tools/playlisty.py                                 #  50
```

---

## 1. Titul

```
Why Did a Blue Flash Kill a Scientist Nine Days Later?
```

> Wh-otázka, 54 znaků, totožná s nadpisem `script.md`. Paradox (záblesk
> × smrt až po devíti dnech) bez prozrazení odpovědi — že záblesk nebyl
> to, co zabíjelo, ale jen viditelná stopa neviditelného ozáření.
> „Demon Core" v titulu záměrně není: kdo to jméno zná, zná i pointu.

---

## 2. Popis

```
A small metal sphere. No fire, no explosion, no siren. Just a flash of blue light, and the people in the room running for the door. Nine days later, the physicist who had been closest to it was dead.

In May 1946, Louis Slotin was demonstrating a criticality experiment at Los Alamos with a plutonium core made for the third atomic bomb. The only thing keeping two beryllium shells apart was a screwdriver in his hand.

Why could a core like that be handled at all? What turned it dangerous in a fraction of a second? Where did the blue light come from, if it wasn't an explosion? And why was this not even the first time the same core had killed someone?

Subtitles are written for this video, not auto-generated. An American English audio track is available as a second audio track.

Full transcript, sources and translations: https://theresmoretoit-channel.github.io/videos/why-did-a-blue-flash-kill-a-scientist/

CHAPTERS
00:00 A blue flash in a laboratory
00:48 He had been warned
01:50 What makes a core critical
02:20 Why the core alone wasn't so dangerous
02:45 Sending the neutrons back
03:16 May 21, 1946
03:55 The screwdriver slips
04:27 No explosion
04:49 "He knew he had had it"
05:26 Where did the blue light come from?
06:08 Nine days
06:29 Not the first time
07:14 The twenty-first of the month
07:51 What changed afterwards
08:33 What happened to the core
08:45 Remember the blue flash?

IMAGE CREDITS
Harry K. Daghlian — unknown author, CC BY-SA 3.0, via Wikimedia Commons
Partially reflected plutonium sphere — Los Alamos National Laboratory, via Wikimedia Commons
All other archive images are in the public domain.
Licences: creativecommons.org/licenses/by-sa/3.0
```

> **Blok se kopíruje CELÝ** (`docs/zverejneni.md`) — atribuce je UVNITŘ.
> Povinná je u S58 (Daghlian, CC BY-SA 3.0, autor na Commons „Unspecified")
> a u S59 (licence „Attribution" s kreditem LANL). S06, S09, S10, S24, S28,
> S42b a S44 jsou public domain. Ilustrace z ChatGPT (S19, S52, S54, S70,
> `art/`) se neuvádějí, stejně jako u 079 a 085.
>
> Kapitoly jsou ze scén S01, S08, S16, S19b, S20, S23, S29, S35, S39, S44,
> S52, S56, S63, S70, S77, S79 (`work/timing.json`, časy zaokrouhlené
> dolů). S16 začíná v 1:50, tedy hned za CTA (S15b 1:42–1:50). Nejkratší
> kapitola je 12 s (S77–S79), všechny ≥ 10 s.
> **Po každém dalším běhu `tts.py` časy přepočítej** — a stejně tak
> v `youtube-preklady.md`.
>
> Popis klade otázky ze scénáře a neodpovídá na ně; nepřidává žádné
> tvrzení, které by nebylo ve `factcheck.md`.

---

## 3. Náhled

✅ **C1** (`thumbnail/c1-koule.png`, z ChatGPT) → `render/thumbnail.jpg`,
`DEMON CORE / WHAT KILLED HIM?`. Původ a měření v `thumbnail/PUVOD.md`,
koncepty v `thumbnail/KONCEPTY.md`.

---

## 4. Titulky

`subtitles/*.srt`, 14 jazyků + `en-US`. Jazyk videa **`en-gb`** (hlas
`bf_emma`) se musí nastavit dřív, než se nahrají titulkové stopy. **Nahrávat
až po Codexu** na všech jazycích.

---

## 5. Nastavení

| | |
|---|---|
| kategorie | Education |
| jazyk videa | `en-gb` |
| licence | standardní |
| pro děti | **ne** |
| komentáře | zapnuté |
| **byla použita AI** | **ne** — rozhodl uživatel 2026-10-03. Scény kreslené kódem, 9 archivních snímků jen barevně upravených, žádná SDXL scéna, hudba procedurální, hlas není klon. Čtyři ilustrace z ChatGPT (S19, S52, S54, S70) jsou malby a neukazují skutečnou osobu ani místo (`art/PUVOD.md`) |

### Závěrečná obrazovka

`zaver_check.py`: S80–S83 mají kresbu do 2,5 %, takže dlaždice i kolečko
odběru se vejdou kamkoli kromě spodku (titulek). Dej je do **horní**
poloviny. Dlaždice: návrh **049** (*What Makes a Battery Catch Fire*) —
nebo nejlépe výkonné video kanálu, podle volby ve Studiu.

---

## 6. Tagy

```
demon core, louis slotin, harry daghlian, criticality accident,
blue flash, cherenkov radiation, plutonium, los alamos, manhattan
project, tickling the dragon's tail, radiation sickness, nuclear
history, beryllium reflector, chain reaction, explainer,
there's more to it
```

---

## 7. Playlist

Navrženo **`fyzika`** (*Physics That Sounds Simple Until You Ask*) — titul
je otázka typu „jak může záblesk zabít", odpověď vede přes kritičnost
a Čerenkovovo záření. Alternativa `energie` (palivo, baterie). Dopiš slug
do `playlisty.json`, spusť `analytics.py --videa` a pak `tools/playlisty.py`.
