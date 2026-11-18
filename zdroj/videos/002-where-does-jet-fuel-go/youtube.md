# Podklady pro nahrání na YouTube

Ručně psaný zdroj. Časy kapitol odpovídají `work/timing.json` (celkem 8:06) —
**po každém přegenerování hlasu je odvoď znovu**, protože se posunou.

Stav k 25. 8. 2026: **připraveno k nahrání**, kontroly níž prošly.

---

## 1. Titul

```
Where Does the Fuel Go When a Plane Dumps It?
```

44 znaků. Limit je 100, mobil ukáže zhruba 60 — vejde se bez oříznutí.

> ⚠️ **Titul a thumbnail říkají skoro totéž.** Thumbnail nese
> „WHERE DUMPED FUEL GOES". Pravidlo z prvního videa je, že thumbnail nese
> údernou část a titul popisnou a vyhledatelnou — nemají se opakovat.
> Alternativy, kdyby se to mělo rozdělit:
>
> - `The Hundred-Tonne Gap` — krátké, ale samo o sobě neříká, o čem to je
> - `Most Airliners Can't Dump Fuel At All` — nejsilnější, ale prozrazuje
>   twist, který ve videu přijde až v 6:30
>
> Titul jde změnit i po zveřejnění, takže to není blokátor.

---

## 2. Popis

První dva řádky jsou to jediné, co je vidět před „show more".
**Následující blok je k překopírování celý.**

```
A plane takes off, something goes wrong, and before it lands it dumps twenty tonnes of
fuel into the sky. Where does that actually go — and why not simply burn it instead?

The answer involves a hundred-tonne gap between what an aircraft may take off at and what
it may land at, a Cold War bomber that really did set its own dumped fuel on fire, and a
twist most articles never mention: most airliners cannot dump fuel at all.

Full transcript, sources and translations: https://theresmoretoit-channel.github.io/videos/where-does-jet-fuel-go/

CHAPTERS
0:00 The headline
0:26 Why it can't just land
1:24 Why not build it stronger
2:04 Where the fuel actually goes
3:20 Why not just burn it
3:51 The flying flamethrower
4:14 Somebody actually did it
5:09 What else could go overboard
5:30 The parachute solution
6:30 Most airliners can't dump at all
7:38 So why it happens

SOURCES
Weight figures: Boeing 747-400 Airplane Characteristics for Airport Planning (D6-58326-1).
Certification rule: FAR 25.1001 / CS-25. Evaporation figures: US ATSDR modelling of
jettisoned fuel. Full working, including what could not be verified, is in the project's
fact-check notes.

IMAGE CREDITS
All archive images are public domain, CC0 or Creative Commons. Colour graded, cropped, and
in one case retouched to remove airline markings; originals are unmodified at the links
below.

S04 · Airliner taking off from Heathrow — David Hawgood (CC BY-SA 2.0)
S11 · Twenty main wheels of Qatar Airways A380 — Adrian Pingstone (Public domain)
S14 · Aircraft approaching runway — Writpit (CC BY-SA 3.0)
S23 · Honeywell HTF7000 turbofan engine — Matti Blume (CC BY-SA 4.0)
S29 · General Dynamics F-111 Aardvark in flight — San Diego Air & Space Museum Archives (Public domain)
S30 · F-111 Fuel Dump, Avalon — Jjron (CC BY-SA 3.0)
S31 · F-111 Aardvark Australia — Scott Sandars (CC BY 2.0)
S35 · Mobility Guardian 2019 CRAF 757 — U.S. Air Force / Roland Balik (Public domain)
S37 · American Airlines A321neo economy cabin — EEJCC (CC0)
S41b · Military skydiver — U.S. Navy / Jason Isaacs (Public domain)
S49 · VC-25B Bridge aircraft at Waco, Texas — U.S. Air Force (Public domain)

All via Wikimedia Commons. Music is procedurally generated for this video.

Subtitles are written for this video, not auto-generated. An American English
audio track is available as a second audio track.
```

Plné znění licencí a otisky SHA-256 originálů jsou v `LICENSES.md`.
Ten do popisku nepatří, je to doklad původu.

---

## 3. Štítky

```
fuel dumping, fuel jettison, why planes dump fuel, jettison system, overweight landing,
maximum landing weight, MTOW, MLW, Boeing 747, F-111, dump and burn, narrowbody,
aviation explained, how planes work, aerospace engineering, aviation
```

16 štítků, 237 znaků z limitu 500. Žádný není delší než 30 znaků, takže
je YouTube nezkrátí.

Řazeno od konkrétního k obecnému, jako u prvního videa. První čtyři jsou
to, co člověk opravdu napíše do vyhledávání, když ho ta otázka napadne.
`MTOW` a `MLW` jsou tam kvůli lidem z oboru, kteří hledají zkratkou.

> **Nedávej štítky na věci, které ve videu nejsou.** `F-111` a `dump and
> burn` tam patří, protože tomu patří celá kapitola. `Airbus A380` ne,
> přestože se mihne na dvou záběrech — divák, který ho hledá, tady odpověď
> nenajde. Kanál stojí na tom, že slibuje jen to, co dodá.

---

## 4. Nastavení při nahrávání

| co | hodnota |
|---|---|
| soubor | `render/final-en.mp4` — **master, ne draft** |
| **jazyk videa** | **`en-gb`** — nastav **PRVNÍ**, jinak zůstane dlaždice Titulky zašedlá |
| titulky | `subtitles/en.srt` (English UK), `subtitles/cs.srt` (čeština) |
| náhled | `render/thumbnail.jpg` |
| kategorie | Věda a technika |
| viditelnost | **nejdřív neveřejné** |
| AI obsah | **ne** |
| pro děti | ne |

### Označení AI obsahu: ne

Drží to tři věci:

- SDXL dělá **6 scén z 52** a všechny jsou díky kotvě stylu malované
  ilustrace, ne fotorealismus
- archivní snímky jsou upravené barevně, výřezem a u S11 retuší, která
  odstranila polep dopravce — **žádná z těch úprav nevytváří scénu,
  která se nestala**
- hudba je procedurální (sinusovky a šum v numpy), ne z generativního modelu

> Zvažovalo se použít AI-retušované snímky letadel. **Zamítnuto** — měření
> ukázalo, že model obrázky překreslil (22 a 26 % změněné plochy), takže by
> šlo o fotorealistické vygenerované fotky a odpověď by se překlopila na
> **ano**. Viz „Retuš archivního snímku se ověřuje" v CLAUDE.md.

---

## 5. Kontrola před nahráním

```bash
V=videos/002-where-does-jet-fuel-go
ffmpeg -v error -i $V/render/final-en.mp4 -f null -    # musí projít BEZE SLOVA
ffprobe -v error -show_entries format=duration -of default=nw=1:nk=1 $V/render/final-en.mp4
ls -l $V/render/thumbnail.jpg                          # do 2 MB
grep -c " --> " $V/subtitles/*.srt
```

Stav 25. 8. 2026:

| kontrola | výsledek |
|---|---|
| dekódování masteru | ✅ čisté, ani jedna chyba |
| délka | 486,60 s = 8:06 |
| obraz / zvuk | 1920×1080, 25 fps, h264 + AAC |
| hlasitost | **−14,05 LUFS / −1,22 dBTP** |
| velikost | 72 MB |
| náhled | 1280×720, 61 kB |
| titulky | `en` 132, `cs` 171, bez překryvů a přetečení |

> `ffprobe` sám nestačí — délku přečte z kontejneru i u rozsypaného streamu.
> Poškozený render se pozná jen dekódováním a tím, že soubor mezi dvěma
> výpisy `ls` roste.

---

## 6. Po zveřejnění

- **Podívej se na to v přehrávači.** YouTube video překóduje a jak vyjdou
  tmavé diagramy po jejich kompresi se dopředu posoudit nedá. Je to jediný
  krok, který nejde udělat na disku.
- **Závěrečná obrazovka a karty** — tentokrát je na co odkazovat, první
  video existuje. U prvního videa to nešlo.
- **Další jazyky** — zatím jen `en` a `cs`. Další potřebují jen přeložený
  soubor se stejným počtem řádků, video se nesahá. CLAUDE.md k tomu má
  varování: jazyk, u kterého se neověří odborná terminologie, tam nepatří.
- **Test & Compare** — v `thumbnail/` leží čtyři další koncepty
  (`c1`–`c4`), kdyby se chtěl náhled testovat.
