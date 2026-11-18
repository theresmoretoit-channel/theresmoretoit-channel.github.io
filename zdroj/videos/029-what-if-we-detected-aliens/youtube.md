# Podklady pro nahrání na YouTube

Ručně psaný zdroj. Časy kapitol odpovídají renderu z `work/timing.json`
(celkem 11:26) — **po každém přegenerování hlasu je potřeba je znovu
odvodit**, protože se posunou.

---

## 1. Titul

```
We Found Aliens. Now What?
```

26 znaků. Limit je 100, mobil ukáže zhruba 60 — vejde se bez oříznutí.

Zvažované alternativy:

- `What If We Detected Aliens?` — 26 znaků, doslova pracovní titul
  z `project.json`. Slabší proto, že se ptá na **detekci**, kdežto video
  je o tom, co přijde **potom**
- `How Would We Actually Talk to Aliens?` — 37 znaků, přesné, ale delší
  a míň úderné
- `The Conversation That Takes a Thousand Years` — nejhezčí, ale
  nevyhledatelné; „aliens" v titulu nést musí

Náhled říká `ALIENS` a ptá se, takže **titul to nemá opakovat jako
otázku znovu**. Nese oznámení („We Found Aliens.") a krátký háček
(„Now What?"), zatímco náhled nese obraz.

---

## 2. Popis

První dva řádky jsou to jediné, co je vidět před „show more". Zbytek
je pro ty, kdo rozkliknou.

```
Suppose we detect a signal that nothing in nature explains. That is the easy part.
The hard part is everything that comes after — and most of it has nothing to do with aliens.

We would be looking for technosignatures across the whole electromagnetic spectrum, not just
radio. We might read a planet's atmosphere without ever going there. And then distance takes
over: at five hundred light-years, one question and one answer cost a thousand years, so the
first reaction would not be "let's call them" but "record everything".

Even with the signal in hand, we would still have to work out what it means — which turns out
to be a bit like trying to hold a conversation with a dolphin. Dolphins are intelligent, they
communicate, we have recorded them for decades, and we share a planet, a biosphere and a
physical world with them. It is still extremely hard. Now remove all of that.

Full transcript, sources and translations: https://theresmoretoit-channel.github.io/videos/what-if-we-detected-aliens/

Chapters
0:00 A signal nothing in nature explains
0:38 First we have to find them
1:35 Five hundred light-years
2:53 We still have to work out what it means
3:17 The dolphin problem
4:31 Everything you understood without being told
5:17 They might not think like us
6:17 A different sense of time
6:38 Maybe there is no conversation
7:16 What an AI could actually do
8:07 Why we would never delete the data
9:02 They do not have to send us science
10:05 The distance is still there
10:38 What first contact might really look like

Sources and image credits
Tursiops truncatus Maldives — Julien Bidet, CC BY-SA 4.0
Parkes Radio Telescope 09 — Diceman Stephen West, CC BY-SA 3.0
via Wikimedia Commons
Licences: creativecommons.org/licenses/by-sa/4.0 and /by-sa/3.0

All other visuals are diagrams drawn for this video, or illustrations generated with
Stable Diffusion XL. The music is generated procedurally.

Subtitles are written for this video, not auto-generated. An American English
audio track is available as a second audio track.
```

> **Oba archivní snímky jsou CC BY-SA, takže uvedení autora je povinné
> a je uvnitř bloku.** `docs/zverejneni.md`: u čtyř videí ze šestnácti
> atribuce chyběla přesně proto, že kredity visely jako poznámka **pod**
> blokem, a uživatel kopíruje jen ten blok.
>
> Public domain snímek tu žádný není, takže se nic nevynechává.

---

## 3. Kapitoly

Čtrnáct kapitol, první na `00:00`, každá delší než 10 s — YouTube je
tím pádem uzná. Časy jsou odvozené z `work/timing.json`, ne odhadnuté:

| čas | scéna | co začíná |
|---|---|---|
| 0:00 | S01 | detekce |
| 0:38 | S08 | krok 1 — najít je |
| 1:35 | S14 | krok 2 — vzdálenost |
| 2:53 | S22 | krok 3 — co to znamená |
| 3:17 | S25 | delfíni |
| 4:31 | S34 | společná znalost |
| 5:17 | S40 | jiné myšlení |
| 6:17 | S47 | jiný čas |
| 6:38 | S49 | možná žádný rozhovor |
| 7:16 | S54 | AI |
| 8:07 | S59 | archiv |
| 9:02 | S65 | zábava jako data |
| 10:05 | S73 | vzdálenost se vrací |
| 10:38 | S78 | jak vypadá první kontakt |

---

## 4. Nastavení při nahrávání

| | |
|---|---|
| video | `render/final-en.mp4` (master, **ne** draft) |
| náhled | `render/thumbnail.jpg` — 1280×720, 352 kB (limit 2048). Hotový obrázek zvenčí, ne kreslený kódem — viz `thumbnail/PUVOD.md` |
| **jazyk videa** | **`en-gb` — nastavit NAPŘED**, jinak zůstane dlaždice Titulky zašedlá |
| titulky | `subtitles/*.srt`, devět jazyků |
| kategorie | Science & Technology |
| pro děti | ne |
| **byla použita AI** | **ne** — viz níž. `tools/nahraj.py` to posílá jako `containsSyntheticMedia: false` |
| **Osvědčení o zproštění** | **zaškrtnout RUČNĚ ve Studiu** („obsah se nikdy nevysílal v televizi v USA"). Data API na to pole nemá |
| viditelnost | nahrát jako **neveřejné** a podívat se na to v přehrávači |

> **Obojí u tohohle videa při prvním nahrání chybělo a nahlásil to
> uživatel.** Druhé se ve Studiu jmenuje **„Osvědčení o zproštění"**
> — pod tím názvem se hledá, ne pod textem otázky. Prohlášení o AI se od té doby posílá rovnou z
> `tools/nahraj.py`; to druhé pole ale `VideoStatus` nezná (má jen
> `containsSyntheticMedia`, `madeForKids`, `license`, `embeddable`,
> `privacyStatus`, `publicStatsViewable`, `publishAt`), takže se
> zaškrtává ve Studiu a nástroj na to na konci upozorní.

### Proč „ne" u otázky na AI

Rozhoduje **fotorealističnost, ne použití AI**
([pravidla](https://support.google.com/youtube/answer/14328491)):

- SDXL scény (S05, S49, S51) jsou díky kotvě stylu **malované
  ilustrace**, ne fotorealismus
- oba archivní snímky jsou upravené jen barevně — *„color adjustment or
  lighting filters"* je výslovná výjimka
- hudba je **procedurální** (sinusovky a šum v numpy), ne z generativního
  modelu
- video nezobrazuje žádné konkrétní skutečné místo ani událost

---

## 5. Tagy

```
aliens, extraterrestrial intelligence, SETI, technosignatures, first contact,
alien communication, exoplanets, radio astronomy, dolphins, animal communication,
interstellar distance, light years, artificial intelligence, decipherment,
astrobiology, science explained
```

---

## 6. Kontrola před nahráním

```bash
ffprobe -v error -show_entries format=duration -of default=nw=1:nk=1 \
        videos/029-what-if-we-detected-aliens/render/final-en.mp4
python tools/thumb_check.py videos/029-what-if-we-detected-aliens
```

Naměřeno 6. 9. 2026: master **686,16 s**, dekóduje se celý beze slova,
hlasitost **−14,0 LUFS**, true peak −1,1 dBFS.

Po zveřejnění zapiš odkaz do **`Témata.ods`**, řádek 29 — stav videí
je tam a nikde jinde.
