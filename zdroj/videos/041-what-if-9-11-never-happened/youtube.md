# Podklady k nahrání na YouTube

Časy kapitol **ověřené proti `work/timing.json`**, ne odhadnuté.

> **Master je hotový:** `render/final-en.mp4`, 1920×1080, 25 fps,
> 3× supersampling, CRF 18, 52,2 MB, 10:23. Dekódování prošlo beze
> slova (`ffmpeg -v error -f null -`). Vedle leží `draft-en.mp4`
> s vypálenými ID scén — ten se **nenahrává**.

> **Archivní snímek je jeden: S36.** Titulní strana zprávy Evropského
> parlamentu A5-0264/2001 o systému ECHELON. Licence je rozhodnutí
> Komise 2011/833/EU — **opakované použití je povolené, ale zdroj se
> uvést MUSÍ**, takže atribuce patří DOVNITŘ bloku „Popis". Je tam.

> **Citlivé téma.** Video je o skutečné tragédii se jmenovitými oběťmi.
> YouTube řadí terorismus mezi citlivé události, takže se dá čekat
> omezení reklam. Scénář je schválně maximálně střízlivý, náhled nemá
> hořící věže ani letadlo a v obraze není jediný záběr útoku.

---

## Titul

```
What If 9/11 Never Happened?
```

---

## Popis

**Kopíruje se CELÝ blok mezi apostrofy a nic jiného.**

```
Imagine waking up on the morning of September 11, 2001. You get
up. You go to work. You turn on the television. And nothing happened.

Now fast-forward 25 years. How much of the world you live in
today exists because of something that happened that morning?

This is not a video about the attack. It is a video about the world we
might have had instead — and about how quickly that question stops having
answers. No invasion of Afghanistan. Probably a very different decision
about Iraq. An airport that still annoys you, but not like this. A
surveillance apparatus that was already growing before anyone had heard
of the Patriot Act.

Along the way: the rule about taking your shoes off, which quietly ended
in 2025 because the scanners got better and not because the fear did; a
European Parliament report on global communications interception,
published on 11 July 2001, two months before the attacks;
the agency that did not exist until two months and eight days after them;
and the reason removing one disaster does not give you a peaceful history,
only a different one.

And then the part that is not geopolitics at all. Nearly 3,000
people would still be alive. There would be entire families in 2026 that
simply do not exist in our timeline.

Chapters
00:00 The morning nothing happened
00:36 A world where it never happened
00:51 Afghanistan
01:21 History has no undo button
01:54 Iraq
02:39 The arguments were already there
03:18 An educated guess
03:30 The airport
04:29 The rule that quietly ended
04:53 Surveillance
05:25 It was already growing
06:02 The Middle East
06:54 Would 2026 be better?
07:38 Through individual lives
08:15 Millions of private histories
08:53 September 10
09:18 Nothing happens
09:55 Not the only world

IMAGE CREDITS
Report on the existence of a global system for the interception of
private and commercial communications (ECHELON interception system),
A5-0264/2001 — European Parliament, reuse authorised under Commission
Decision 2011/833/EU, source acknowledged.
Source: europarl.europa.eu

Subtitles are written for this video, not auto-generated. An American
English audio track is available as a second audio track.
```

---

## Tagy

```
9/11, september 11, alternate history, counterfactual, what if, history, geopolitics, iraq war, afghanistan, patriot act, mass surveillance, echelon, airport security, tsa, 21st century
```

---

## Nastavení

| položka | hodnota |
|---|---|
| jazyk videa | **`en-gb`** — nastavit PRVNÍ, jinak zůstane dlaždice Titulky zašedlá |
| kategorie | Věda a technika |
| viditelnost | neveřejné, pak podívat se v přehrávači, teprve pak zveřejnit |
| licence | standardní licence YouTube |
| **prohlášení o AI** | **ne** — viz níž |
| pro děti | ne |
| titulky | devět jazyků z `subtitles/*.srt` |
| lokalizace | osm jazyků z `youtube-preklady.md` přes `tools/lokalizace.py` |
| playlist | doplnit do `playlisty.json` a spustit `tools/playlisty.py` |
| **závěrečná obrazovka** | **ruční krok ve Studiu** — API na to nemá zdroj. `zaver_check.py` hlásí u S63, S63b, S64 a S65 volné místo, ale **jen v HORNÍ polovině**: dole je ambrový nadpis |

### Prohlášení o AI: odpověď je NE

Rozhoduje fotorealističnost, ne použití AI:

- 64 scén jsou **diagramy kreslené kódem** (Inkscape z SVG)
- 7 scén je SDXL, ale kotva stylu z nich dělá **malované ilustrace**,
  ne fotorealismus, a v negativu je výslovný zákaz fotorealismu
- 1 scéna je **skutečný dokument** z archivu, upravený jen barevně
- hudba je **procedurální** (numpy), ne z generativního modelu
- hlas je Kokoro `bf_emma`, tedy syntéza, **ne klonovaný hlas skutečné
  osoby**

> Pozor: video **nezobrazuje žádné skutečné místo ani událost
> fotorealisticky**. Kdyby některá SDXL scéna ukazovala Manhattan roku
> 2001, odpověď by se překlopila na ano.

### Po nahrání

1. `python tools/titulky.py <ID> --smaz-asr` — automatický přepis od
   YouTube konkuruje devíti překladům a je z nich nejhorší
2. závěrečná obrazovka ručně
3. osvědčení o zproštění ručně (API na to pole nemá)
4. zapsat odkaz a stav do `Témata.ods`
