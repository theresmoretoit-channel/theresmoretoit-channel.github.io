# Podklady pro nahrání na YouTube

Ručně psaný zdroj. Časy kapitol odpovídají masteru z `work/timing.json`
(celkem 12:05) — **po každém přegenerování hlasu je potřeba je znovu odvodit**,
protože se posunou.

---

## Titul

```
Why Is Modern Music So Simple?
```

29 znaků. Limit je 100, mobil ukáže zhruba 60 — vejde se bez oříznutí.
Otázka, ne tvrzení; formát kanálu.

Zvažované alternativy:

- `Modern Music Isn't Simpler. It's Optimised.` — přesnější, ale prozrazuje pointu
- `Four Chords, One Beat, Three Hundred Million Streams` — 51 znaků, popisnější,
  ale jako otázka se to hledá líp

Thumbnail nese údernou část, titul popisnou a vyhledatelnou — nemají opakovat totéž.

---

## Popis

První dva řádky jsou to jediné, co je vidět před „show more".

```
Four chords. A simple beat. A chorus that repeats. And somehow, hundreds of millions
of streams. So did music actually get simpler — or did we change what we compare it to?

Modern pop is simpler in some ways and far more complicated in others. This is about
where the complexity went, what streaming actually rewards, and the measurement problem
underneath the whole question: we compare today's average music with the best music
that survived sixty years of forgetting.

Full transcript, sources and translations: https://theresmoretoit-channel.github.io/videos/why-is-modern-music-so-simple/

Chapters
0:00 The question
1:03 What "simple" actually means
1:56 The production side
3:03 The four chords
3:49 Streaming changes the incentives
4:48 What the researchers measured
5:28 The charts became vocal
6:16 Fifteen seconds that matter
6:46 Survivorship bias
8:00 Diversity didn't decline
8:23 Where the complexity went
8:52 The studio in a laptop
10:01 A watch and a smartphone
10:48 So why is modern music so simple?
11:33 Simple compared to what?

Sources and image credits
All archive images are public domain, CC0, or Creative Commons. Full evidence
(SHA-256 of every original, licence text as retrieved): sources.json / LICENSES.md
in the project.

Bach, autograph score of BWV 39 (public domain)
  https://commons.wikimedia.org/wiki/File:BWV39-autograph-score-sinfonia.jpg
Western Electric 23C speech input mixing console, MIM Phoenix - bobistraveling, CC BY 2.0
  https://commons.wikimedia.org/wiki/File:Western_Electric_23C_Speech_input_mixing_console_(1940s)_purchased_by_Floyd_Ramsey_at_Audio_Recorders_(studio)_in_1954,_%26_unknown_recording_studio_rack_-_MIM_Phoenix_AZ_(2017-12-04_14.04.59_by_bobintraveling_140459).jpg
Groove and needle in close embrace from beginning to end - Franz van Duns, CC BY-SA 4.0
  https://commons.wikimedia.org/wiki/File:Groove_and_needle_in_close_embrace_from_beginning_to_end.jpg
Alarm clock mainspring - Chetvorno, CC0
  https://commons.wikimedia.org/wiki/File:Alarm_clock_mainspring.JPG

The chord progression heard in this video is I-V-vi-IV in C major (C - G - Am - F),
generated for this video, first bare and then produced.

Subtitles are written for this video, not auto-generated. An American English
audio track is available as a second audio track. Music, chord examples and
diagrams: made for this video.
```

> **Pozor na atribuci:** S17 je **CC BY 2.0** a S27 **CC BY-SA 4.0** — u obou
> je uvedení autora povinné, takže tyhle dva řádky z popisku vypadnout nesmí.
> Zbylé dva (Bach, Chetvorno) jsou public domain a CC0.

---

## Nastavení při nahrávání

| co | hodnota |
|---|---|
| jazyk videa | **`en-gb`** — nastavit **dřív** než titulky, jinak zůstane dlaždice zašedlá |
| kategorie | Education |
| titulky | `subtitles/*.srt` — devět jazyků |
| náhled | `render/thumbnail.jpg` (do 2 MB, 1280×720) |
| video | `render/final-en.mp4` — **master, ne draft** |

### Byla použita AI? — **ne**

Rozhoduje fotorealističnost, ne použití AI
([pravidla](https://support.google.com/youtube/answer/14328491)). U tohohle videa:

- SDXL scén je devět z dvaaosmdesáti a všechny jsou díky kotvě stylu
  **malované ilustrace**, ne fotorealismus
- archivní snímky jsou upravené jen barevně — *„color adjustment or lighting
  filters"* je výslovná výjimka
- hudba i akordové ukázky jsou **procedurální** (numpy), ne z generativního modelu
- hlas je syntetický, ale **není to klon skutečné osoby**

Odpověď se překlopí na **ano**, jakmile přibude hudba ze Suno/Udio, fotorealistický
checkpoint nebo scéna zobrazující konkrétní skutečné místo či událost.

---

## Thumbnail

**Zvolený: `c1-four-chords`** — kvintakordy C–G–Am–F na osnově, pod nimi
`FOUR CHORDS` a `hundreds of millions of streams`. Paradox je v tom rozporu:
nepatrný hudební materiál proti obrovskému výsledku.

```bash
python tools/thumbnail.py videos/003-why-is-modern-music-so-simple   # -> render/thumbnail.jpg
```

Volba je zapsaná v `project.json` → `thumbnail`, takže příkaz bez parametrů
vyrobí právě ji. Zbylé čtyři koncepty zůstávají v `thumbnail/` jako varianty
(`c2`–`c5`) a vyrobí se předáním `--svg`.

82 kB, tedy hluboko pod limitem YouTube 2 MB. Ověřeno zmenšením na 210 px
i 150 px — nadpis se čte v obou, podtitul jen ve 210 px.

> **Číslo na thumbnailu musí být doložené stejně jako ve scénáři.** První verze
> říkala „three hundred million streams", což je konkrétní hodnota, kterou
> nemám ověřenou — scénář mluví o „hundreds of millions". Opraveno.

> Pro srovnání na skutečném publiku umí YouTube „Test & Compare" až se třemi
> thumbnaily; nejsilnější protikandidát je `c4-not-simpler`, který je v malém
> nejčitelnější, ale rovnou prozradí pointu.

---

## Tagy

```
music theory, four chords, pop music, chord progression, music production,
streaming, survivorship bias, music analysis, why modern music sounds the same,
I-V-vi-IV, hook, music explained
```

---

## Titulky

**Všech devět hotových.**

| kód | jazyk | zdroj | titulků |
|---|---|---|---|
| `en` | English (United Kingdom) | `script.md` | 191 |
| `cs` | čeština | `script.cs.md` | 224 |
| `sv` | svenska | `script.sv.md` | 225 |
| `es` | español | `script.es.md` | 226 |
| `pt-BR` | português (Brasil) | `script.pt-BR.md` | 225 |
| `de` | Deutsch | `script.de.md` | 227 |
| `fr` | français | `script.fr.md` | 228 |
| `it` | italiano | `script.it.md` | 226 |
| `pl` | polski | `script.pl.md` | 225 |

Strukturální kontrola prošla u všech: **nula řádků přes 42 znaků, nula
třířádkových titulků**, útržků 1–6 na jazyk. `subtitles.py` navíc odmítne
soubor, kde nesedí počet řádků proti angličtině — takže shoda scén je
strojově zaručená.

```bash
for l in cs sv es pt-BR de fr it pl; do
  python tools/subtitles.py videos/003-why-is-modern-music-so-simple --lang $l
done
```

> **Co strojová kontrola nechytí, je kalk.** Struktura sedí, ale „není to česky"
> (a totéž v dalších osmi jazycích) pozná jen čtení. U druhého videa tím prošly
> dvě věcné chyby. Termíny jsem volila takto: *hook* zůstává hookem v `de`,
> `sv`, `it`, `pl`, kdežto `es`/`pt-BR` mají *gancho* a `fr` *l'accroche*;
> *survivorship bias* je `de` Survivorship Bias, `sv` överlevnadsbias,
> `es` sesgo de supervivencia, `pt-BR` viés de sobrevivência,
> `fr` biais du survivant, `it` bias di sopravvivenza, `pl` efekt przetrwania.

---

## Kontrola před nahráním

```bash
ffprobe -v error -show_entries format=duration -of default=nw=1:nk=1 \
        videos/003-why-is-modern-music-so-simple/render/final-en.mp4
ffmpeg -v error -i videos/003-why-is-modern-music-so-simple/render/final-en.mp4 -f null -
```

Druhý příkaz musí projít **beze slova** — `ffprobe` sám poškozený stream neodhalí,
délku přečte i z rozsypaného souboru.

**A nahraj jako neveřejné a podívej se na to v přehrávači.** YouTube video
překóduje a jak po jejich kompresi vyjdou tmavé scény, se na disku posoudit nedá.
