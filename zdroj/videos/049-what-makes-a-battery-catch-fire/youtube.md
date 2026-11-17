# Podklady k nahrání na YouTube

Časy kapitol **ověřené proti `work/timing.json`**, ne odhadnuté.
Každá kapitola je od předchozí aspoň 10 s, první je `00:00` a je jich
20 — YouTube uzná kapitoly, jen když platí všechny tři podmínky.

| co | odkud |
|---|---|
| video | `render/final-en.mp4` — 1920×1080, **9:39**, 50,5 MB |
| náhled | `render/thumbnail.jpg` — 1280×720, 0,38 MB (hotový obrázek od uživatele, viz `thumbnail/PUVOD.md`) |
| titulky | `subtitles/*.srt` — **patnáct stop**: čtrnáct jazyků + `en-US` |
| americká stopa | `render/audio-en-US.m4a` — 14,2 MB, `speed` 0,9397, sedí na Emminu mřížku **na 0,000 s** |
| lokalizované názvy a popisy | `youtube-preklady.md` |

**Dva archivní snímky, oba pod CC BY-SA**, takže atribuce je POVINNÁ
a je **uvnitř bloku „Popis"** — ne pod ním. Zbytek videa je kreslený
kódem (77 diagramů) a čtyři scény z SDXL.

**Video je kompletní.** Čtyři SDXL scény (S38, S52, S67, S77) jsou
vygenerované a master z nich vyrenderovaný 2026-09-16.

---

## Titul

```
What Makes a Battery Catch Fire?
```

> Wh-otázka schválně (na kanálu 2,23 % proti 1,63 % u tvrzení).
> Titul pojmenuje téma prvním slovem a odpověď neprozrazuje — divák
> ví, o čem video je, ale ne že pointa stojí na jmenovateli.

## Popis

```
Every few days there is another story about a battery fire. A power
bank on a plane, a scooter in a stairwell, sometimes an entire
building. The headline is always the same: lithium-ion batteries are
dangerous. And yet there is one in your pocket, one in your laptop and
probably one parked outside, and almost all of them spend their lives
doing nothing at all.

This video is about what actually has to go wrong. A lithium cell
carries its own fuel, sealed inside it. Between the two electrodes sits
a plastic film thinner than twenty micrometres — and plastic does not
do well when heated. Once a short circuit makes one spot hot, the hole
in that film grows, a bigger hole carries more current, more current
makes more heat, and nothing in that loop slows it down. That is
thermal runaway.

Then the harder half: how often it happens. When Samsung recalled two
and a half million phones in 2016, the number of incidents reported in
America was ninety-two, out of roughly a million sold there. One in ten
thousand was enough to end a flagship phone and get it banned from
aeroplanes. We see the failures. We never see the denominator — and in
New York, where these fires killed eighteen people in 2023, what
changed afterwards was not the chemistry but which batteries were
allowed on the market.

Subtitles are written for this video, not auto-generated. An American
English audio track is available as a second audio track.

Chapters
00:00 Another battery caught fire
00:40 It carries its own fuel
01:05 What has to go wrong first
01:46 Inside a phone battery
02:25 The separator
02:51 Four ways in
03:04 An internal short
03:32 The loop
03:52 Thermal runaway
04:02 What comes out
04:31 Cells are never alone
05:01 So, are they dangerous?
05:21 What rare actually looks like
05:52 Count the batteries around you
06:07 The denominator
06:36 A battery is a system
07:20 What New York did
08:07 Why not just make them safe?
08:33 What comes next
09:16 Back to the paradox

IMAGE CREDITS
Lithium-ion laptop battery internals — Lead holder, CC BY-SA 3.0
Samsung Galaxy Note 7 rear — Pang Kakit, CC BY-SA 4.0
both via Wikimedia Commons
Licences: creativecommons.org/licenses/by-sa/3.0
          creativecommons.org/licenses/by-sa/4.0
```

## Tagy

```
lithium-ion battery, thermal runaway, battery fire, separator, LFP,
lithium iron phosphate, solid-state battery, battery safety, e-bike
battery, Galaxy Note 7, battery management system, how it works,
risk perception, electric vehicle battery
```

## Nastavení

| položka | hodnota |
|---|---|
| kategorie | Science & Technology (28) |
| jazyk videa | **en-GB** — nastavit PŘED titulky, jinak zůstane dlaždice Titulky zašedlá |
| licence | Creative Commons – Attribution (snímky jsou CC BY-SA, video je vlastní tvorba) |
| vytvořeno pro děti | ne |
| **prohlášení o AI** | **ne** — ověřeno na hotových scénách: všechny čtyři SDXL scény jsou malované ilustrace se skicovitým tahem, žádná nezobrazuje konkrétní skutečné místo ani událost; archivní snímky jsou upravené jen barevně; hudba je procedurální |
| náhled | **fotorealistický obrázek z generativního modelu**, ale prohlášení o AI se ptá na obsah VIDEA, ne na náhled — odpověď zůstává ne. Rozbor v `thumbnail/PUVOD.md` |

## Co musí uživatel naklikat sám

1. **Závěrečná obrazovka** — API na ni nemá ani zdroj. Místo je ověřené
   `zaver_check.py`: S80, S82 a S83 jsou volné, S81 je záměrně plná
   mřížka, kde překryv nic neubere.
2. **Druhá audiostopa** (`render/audio-en-US.m4a`) — nahrát ji umí jedině
   Studio. **Když se nenahraje, musí se věta o ní vypustit z popisu i ze
   všech třinácti překladů** — jinak popis slibuje stopu, která tam není.
3. **Playlist** — dopsat slug do `playlisty.json`, pak `analytics.py --videa`
   a `tools/playlisty.py`.
4. **Prohlášení o AI a osvědčení o zproštění**, pokud se video zakládá
   přes `videos.insert` místo ručního nahrání MP4.

## Stav dodávek

| | |
|---|---|
| master | ✅ `render/final-en.mp4`, 1920×1080, 579,8 s, stream ověřen `ffmpeg -v error` |
| náhled | ✅ `render/thumbnail.jpg` |
| titulky | ✅ patnáct stop |
| americká stopa | ✅ `render/audio-en-US.m4a` — délka 579,803 s sedí na master |
| SDXL scény | ✅ všechny čtyři (S38 na první pokus, S52 na druhý, S77 na třetí) |
