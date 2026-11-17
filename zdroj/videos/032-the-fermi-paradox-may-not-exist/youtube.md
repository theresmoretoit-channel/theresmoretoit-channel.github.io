# Podklady pro nahrání na YouTube

Video: `render/final-en.mp4` (1920×1080, 12:30, 60 MB)
Náhled: `render/thumbnail.jpg`
Titulky: `subtitles/*.srt` v devíti jazycích

---

## 1. Titul

```
The Fermi Paradox May Not Exist
```

Alternativy, kdyby se testovalo:

- `Where Is Everybody? Maybe That's the Wrong Question`
- `The Fermi Paradox Is Mostly Assumptions`

Vybraný titul je tvrzení proti očekávání — divák zná paradox jako fakt
a titul ho zpochybní. Náhled se ptá (`WHERE IS EVERYBODY?`), takže
dvojice titul + náhled dělá otázku i obrat.

---

## 2. Popis

První dva řádky jsou to jediné, co je vidět před „show more".

```
The Fermi paradox sounds like a conflict between two facts. It isn't. It's one observation —
we haven't detected anyone — combined with a long list of things we simply assumed.

This video takes that list apart, one assumption at a time. Aliens should be common. They
should become intelligent. They should survive. They should want to expand. And they should
leave traces we can recognise. Break any one of them and the paradox stops being paradoxical.

Along the way: why a sample size of one supports almost no conclusion at all, why an advanced
civilisation might have no reason to cross a hundred light-years, why the galaxy is not a
snapshot but a four-dimensional history, and why searching for loud civilisations might be
like searching for teenagers by looking only for abandoned toys.

Then the Dark Forest — the most famous answer of all — and the question that breaks it.
How exactly do you hide a planet? Earth's atmosphere has been reshaped by biology and,
increasingly, by technology. And in 2025 a group of researchers worked out how far away
our own technosignatures could be picked up. Planetary radar: about twelve thousand light-years.
Ordinary mobile phone towers: four.

We are already producing technosignatures. And we are not even trying to hide them.

Chapters
0:00 The question
1:19 Maybe intelligence is rare
2:11 Why would anyone expand?
3:40 The Great Filter
4:07 Maybe we're searching badly
4:40 A Roman with a radio telescope
5:15 The galaxy is not one moment
5:53 Civilisations may get quieter
6:25 The Dark Forest
7:17 But Earth is not quiet
8:43 The really loud part
9:45 So does that kill it?
10:30 The wrong question
11:17 We are difficult to hide
11:31 Perhaps there is no paradox

Sources
Sheikh, Huston, Fan, Wright, Beatty, Martini, Kopparapu & Frank (2025). "Earth detecting Earth:
at what distance could Earth's constellation of technosignatures be detected with present-day
technology?" The Astronomical Journal 169, 118. This is where the detection distances come from.

Wright, Kanodia & Lubar (2018). "How Much SETI Has Been Done? Finding Needles in the
n-dimensional Cosmic Haystack." The Astronomical Journal 156, 260.

Image credits
Early spark gap transmitter and coherer receiver — Victor Hugo Laughter, public domain,
via Wikimedia Commons.
Arecibo Observatory — National Science Foundation, public domain, via Wikimedia Commons.
Pale Blue Dot — NASA/JPL-Caltech, public domain. Earth photographed by Voyager 1 in 1990,
reprocessed 2020.

All other visuals are diagrams drawn for this video, or illustrations generated with
Stable Diffusion XL. The music is generated procedurally.

Subtitles are written for this video, not auto-generated. An American English
audio track is available as a second audio track.
```

> **Všechny tři archivní snímky jsou public domain**, takže povinná
> atribuce tu není žádná. Uvedené jsou schválně: Arecibo je zároveň
> náhled videa a Pale Blue Dot nese závěrečnou pointu.
>
> Kredity i zdroje jsou **uvnitř bloku**, ne pod ním. U čtyř videí ze
> šestnácti atribuce chyběla přesně proto, že visela jako poznámka pod
> blokem, a uživatel kopíruje jen ten blok.

---

## 3. Kapitoly

Patnáct kapitol, první na `00:00`, nejkratší 14 s. **Pozor: YouTube
uzná kapitoly jen tehdy, když je každá aspoň 10 s** — `11:17` a `11:31`
mají mezi sebou 14 s, takže projdou, ale je to nejtěsnější místo.
Časy jsou odvozené z `work/timing.json`, ne odhadnuté.

---

## 4. Nastavení při nahrávání

| pole | hodnota |
|---|---|
| viditelnost | **nejdřív neveřejné**, podívat se v přehrávači, teprve pak veřejné |
| jazyk videa | **English (United Kingdom)** — nastavit PRVNÍ, jinak zůstane dlaždice Titulky zašedlá |
| pro děti | ne |
| **byla použita AI** | **ne** — zdůvodnění níž |
| kategorie | Věda a technika |

### Proč „ne" u otázky na AI

Rozhoduje fotorealističnost, ne použití AI
(https://support.google.com/youtube/answer/14328491). U tohohle videa:

- pět SDXL scén je díky kotvě stylu **malovaná ilustrace**, ne fotorealismus
- tři archivní snímky jsou upravené jen barevně a výřezem —
  *„color adjustment or lighting filters"* je výslovná výjimka
- hudba je **procedurální** (numpy), ne z generativního modelu
- hlas je Kokoro, tedy syntéza, ne klon skutečné osoby

---

## 5. Tagy

```
fermi paradox, where is everybody, seti, technosignatures, dark forest,
great filter, extraterrestrial life, alien civilisation, arecibo,
pale blue dot, drake equation, astrobiology, exoplanets, sample size of one,
are we alone
```

---

## 6. Kontrola před nahráním

- [ ] `render/final-en.mp4` projde `ffmpeg -v error -i … -f null -` **beze slova** ✅ ověřeno
- [ ] náhled ≤ 2 MB, 1280×720, 16:9 ✅ 264 kB
- [ ] devět SRT, každý bez řádku nad 42 znaků ✅
- [ ] jazyk videa nastavený PŘED nahráním titulků
- [ ] `archive.py --evidence` naposledy proti `sources.json`
- [ ] po nahrání se na video podívat v přehrávači, ne jen v náhledu

**Ruční kroky ve Studiu — API na ně nemá pole ani zdroj:**

- [ ] **Osvědčení o zproštění** („nikdy se nevysílalo v televizi v USA")
- [ ] **Závěrečná obrazovka** — dlaždice dalšího videa a kolečko odběru.
      Místo na ně ověřeno: `zaver_check.py` hlásí u všech čtyř scén
      v posledních 20 s (S109–S112) volné umístění bez překryvu.
