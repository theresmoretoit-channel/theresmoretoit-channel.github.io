# Podklady k nahrání — How Does a War Economy Work?

| co | odkud |
|---|---|
| video | `render/final-en.mp4` — 8:45, 1920×1080, 37 MB, −14,0 LUFS |
| náhled | `render/thumbnail.jpg` — 1280×720, 136 kB, varianta `c4-destroyed-still-counted` |
| titulky | `subtitles/*.srt` — devět jazyků |

> **Postup, na kterém se to zdrží:** nejdřív nastav **jazyk videa na
> `en-GB`**, jinak zůstane dlaždice „Titulky" zašedlá. Hlas je `bf_emma`,
> tedy britská angličtina.

---

## 1. Titul

```
How Does a War Economy Work?
```

Alternativy, kdyby se testovalo:

- `A Country Can Win a War and Still Go Broke`
- `Why War Makes GDP Rise and People Poorer`

---

## 2. Popis

```
A war economy is not a machine for creating resources. It is a machine for consuming them.

When a war starts, a government suddenly needs millions of uniforms, trucks, shells, aircraft and tanks. But printing money does not create tanks — steel, workers and factories have to come from somewhere, and that somewhere is the civilian economy.

This video works through what that actually means. Why a country can win a war and still come out of it exhausted: Britain won in 1945, and rationing there did not end until 1954, almost nine years later. Why gross domestic product counts a destroyed tank twice and never subtracts the loss. Why more money chasing the same goods leads to rationing, and rationing to a black market. And why "the economy is booming" and "people are getting poorer" can both be true at the same time.

Full transcript, sources and translations: https://theresmoretoit-channel.github.io/videos/how-does-a-war-economy-work/

00:00 How a peacetime economy works
00:47 The government becomes the customer
01:28 Where the resources actually come from
02:19 The problem of workers
02:51 Britain: winning and paying for it
03:26 Rationing until 1954
03:49 The strange case of GDP
04:35 The illusion of a boom
05:07 Paying for the war
05:27 More money, same goods
05:45 Rationing and the black market
06:26 The American mobilisation
07:00 When the war ends
07:40 Every ton goes somewhere
08:00 The paradox

Subtitles are written for this video, not auto-generated. An American English audio track is available as a second audio track.

IMAGE CREDITS
All archive images in this video are in the public domain, via Wikimedia Commons — Imperial War Museums and the US Navy.

If you want the next one, there is a subscribe button.
```

> **Blok výše se kopíruje CELÝ.** Co je pod ním, se na YouTube nedostane —
> naměřeno 2026-09-03, že u čtyř videí ze šestnácti chyběla atribuce
> právě proto, že byla jako poznámka **pod** blokem.
>
> Atribuce je tu krátká záměrně: **všechny čtyři archivní snímky jsou
> public domain**, takže se podle pravidel projektu nemusí vypisovat po
> jednom. Kdyby přibyl snímek pod CC BY nebo CC BY-SA, musí se jméno
> autora dopsat dovnitř bloku.

---

## 3. Kapitoly

Patnáct kapitol, ověřené proti `work/timing.json`. První je `00:00`,
je jich víc než tři a každá trvá přes deset sekund — to jsou podmínky,
za kterých je YouTube uzná.

---

## 4. Tagy

```
war economy, economics, wartime production, GDP, gross domestic product, rationing, World War II, home front, opportunity cost, scarcity, inflation, black market, war bonds, mobilisation, Britain 1945, lend-lease, economic history, explainer
```

---

## 5. Nastavení

| položka | hodnota |
|---|---|
| jazyk videa | **`en-GB`** (nastavit PRVNÍ) |
| kategorie | Vzdělávání |
| **byla použita AI?** | **NE** — viz níž |
| pro děti | ne |
| viditelnost | nejdřív **neveřejné**, viz kontrola |

### Proč „byla použita AI" = ne

| složka | proč to nepřeklápí |
|---|---|
| **68 diagramů** | kreslené kódem (SVG), žádný model |
| **4 archivní snímky** | skutečné fotografie, upravené jen barevně — *„color adjustment or lighting filters"* je výslovná výjimka |
| **2 SDXL scény** (S02, S60) | malované ilustrace díky kotvě stylu, ne fotorealismus |
| **ikony v `art/`** | ploché čárové kresby; rozhoduje fotorealističnost, ne původ (viz `art/PUVOD.md`) |
| **hudba** | procedurální, sinusovky a šum v numpy — ne generativní model |
| **hlas** | Kokoro `bf_emma`, syntetický hlas bez předlohy ve skutečné osobě |

Překlopilo by to teprve: fotorealistický checkpoint, scéna zobrazující
konkrétní skutečné místo či událost, klonovaný hlas skutečné osoby, nebo
hudba ze Suno či Udio.

---

## 6. Kontrola před zveřejněním

```bash
ffprobe -v error -show_entries format=duration -of default=nw=1:nk=1 \
        videos/025-how-does-a-war-economy-work/render/final-en.mp4
ffmpeg -v error -i videos/025-how-does-a-war-economy-work/render/final-en.mp4 -f null -
```

- [ ] jazyk videa `en-GB` **před** nahráním titulků
- [ ] devět SRT souborů
- [ ] náhled do 2 MB, 1280×720
- [ ] **nahrát jako neveřejné a přehrát si to** — YouTube video překóduje
      a jak vyjde tmavá scéna po jejich kompresi, se na disku posoudit nedá
- [ ] doplnit číslo videa do `Témata.ods` (řádek „Válečná ekonomika")

Závěrečná obrazovka a karty jdou přidat i po zveřejnění. Poslední scéna
(S73) je na ně navržená: text drží v horní polovině, dolní třetina
a pravá strana zůstávají prázdné.
