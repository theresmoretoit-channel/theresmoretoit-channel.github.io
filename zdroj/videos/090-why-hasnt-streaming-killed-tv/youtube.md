# YouTube — 090 „Why Hasn't Streaming Killed TV?"

Stav: **nahráno a naplánované na zveřejnění 2026-10-06** (zbytek doklikal uživatel ve Studiu) — https://www.youtube.com/watch?v=-ASWm7SoLDk

| | |
|---|---|
| ID videa | `-ASWm7SoLDk` |
| nastavení, popis, tagy | ✅ |
| náhled | ✅ C1 (`thumbnail/c1-televize.png`, z ChatGPT) |
| lokalizace | ✅ 13 jazyků |
| automatický přepis | ✅ čisté |
| titulky | ✅ 8 přes API (`en cs sv es pt-BR de fr it`), zbylých 7 uživatel ručně ve Studiu |
| playlist | ✅ `legacy` (`playlisty.json`; `playlisty.py` je idempotentní, kdyby chybělo) |
| závěrečná obrazovka, americká stopa | ✅ uživatel ve Studiu |

**Zbývá po obnovení kvóty:**

```bash
V=videos/090-why-hasnt-streaming-killed-tv
python tools/titulky.py $V --jen pl,id,tr,uk,vi,fi,en-US     # 2 800
python tools/playlisty.py                                    #    50
```

**Co musí uživatel naklikat sám:** nahrát MP4 ve Studiu (průvodce vyřídí
prohlášení o AI — odpověď **ne** — a osvědčení o zproštění), závěrečnou
obrazovku a americkou audiostopu (`render/audio-en-US.m4a`).

Soubor k nahrání: `render/final-en-090.mp4` (stopáž 8:29, `work/timing.json`
total 508,7 s).

Pořadí podle CENY (`docs/zverejneni.md`):

```bash
V=videos/090-why-hasnt-streaming-killed-tv
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
Why Hasn't Streaming Killed TV?
```

> Wh-otázka, 31 znaků, totožná s nadpisem `script.md`. Zdroj měl ano/ne
> otázku „Is Classic TV Broadcasting Deprecated?" — nejhorší typ titulu
> podle CTR kanálu. Neprozrazuje odpověď (vysílání řeší jiný problém:
> totéž milionům najednou).

---

## 2. Popis

```
It's half past seven. You turn on the television: commercials, the news, more commercials, the weather. The film finally starts at eight, and with all the breaks it won't finish until quarter to eleven. You can't pause it. You didn't even choose it.

And yet in May 2025, after nearly twenty years of Netflix and YouTube, streaming only just overtook broadcast and cable in the United States: 44.8 percent of TV viewing against 44.2.

So why hasn't streaming killed it? What does a transmitter do that the Internet finds surprisingly hard? Are television and broadcasting even the same thing? And when would you actually want everyone to see the same thing at the same time?

Subtitles are written for this video, not auto-generated. An American English audio track is available as a second audio track.

Full transcript, sources and translations: https://theresmoretoit-channel.github.io/videos/why-hasnt-streaming-killed-tv/

CHAPTERS
00:00 An evening of linear TV
00:52 Of course, you could record it
01:21 Streaming overtook TV. Barely.
02:01 One transmitter, millions of receivers
02:53 Then the Internet happened
03:30 The World Cup final
03:56 Why the Internet works differently
04:41 Television isn't broadcasting
05:34 Sometimes people don't want to choose
06:15 When the Internet goes down
06:58 So, has streaming killed television?
```

> **Blok se kopíruje CELÝ** (`docs/zverejneni.md`). Video nemá žádný
> archivní snímek, takže povinná atribuce není. Ilustrace z ChatGPT (S42,
> `art/`) se neuvádí, stejně jako u 079, 085 a 086; S18 a S50 jsou SDXL.
>
> Kapitoly jsou ze scén S01, S07b, S09, S13, S19, S25, S28, S33, S41, S47,
> S51 (`work/timing.json`, časy zaokrouhlené dolů). S13 začíná ve 2:01,
> hned za CTA (S12b 1:52–2:01). Nejkratší kapitola je 29 s (S07b–S09),
> všechny ≥ 10 s. **Po každém dalším běhu `tts.py` časy přepočítej** —
> a stejně tak v `youtube-preklady.md`.
>
> Popis klade otázky ze scénáře a neodpovídá na ně; čísla (Nielsen 05/2025,
> 44,8 × 44,2, konec 22:45) jsou z `factcheck.md`.

---

## 3. Náhled

✅ **C1** zvolen (`TV / WHY IS IT STILL HERE?`), původ v `thumbnail/PUVOD.md`.

Původní koncepty pro ChatGPT podle šablony `docs/thumbnail-styl.md` (tmavé
texturované pozadí, jeden předmět, bílé slovo nahoře, žlutá otázka dole).
Náhled **nesmí prozradit odpověď** — že vysílání vyhrává tam, kde všichni
chtějí totéž najednou. Proto žádný stožár ani dav v obraze.

| | předmět | nahoře | dole |
|---|---|---|---|
| C1 | stará televize s anténkami („králičí uši"), obrazovka svítí | `TV` | `WHY ISN'T IT DEAD?` |
| C2 | televizní ovladač, jediné tlačítko svítí | `TV` | `WHO STILL WATCHES?` |
| C3 | moderní televize s pokojovou anténou na ní | `TV` | `WHY NOT STREAMING?` |

Po výběru: `thumbnail/` + `thumbnail/PUVOD.md`, `python tools/thumb_check.py`,
pohled na 150 px vedle sebe, pak `render/thumbnail.jpg`.

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
| **byla použita AI** | **ne** — scény kreslené kódem, žádný archivní snímek, dvě SDXL scény (S18, S50) jsou malované ilustrace podle kotvy stylu, S42 je malovaná ilustrace z ChatGPT bez skutečné osoby či místa (`art/PUVOD.md`), hudba procedurální, hlas není klon |

### Závěrečná obrazovka

`zaver_check.py`: S61–S63 mají kresbu do 2,1 %, obsah jen v dolní polovině.
Dlaždici i kolečko odběru dej do **horní** poloviny. Dlaždice: návrh **089**
(*Why Can You Still Buy a Phone With a Keyboard?*, totéž téma „stará
technologie přežívá") — nebo nejvýkonnější video podle volby ve Studiu.

---

## 6. Tagy

```
linear tv, broadcast television, streaming, why hasn't streaming killed tv,
cord cutting, terrestrial tv, broadcasting vs streaming, one to many,
nielsen the gauge, world cup final, emergency broadcasting, pvr, vcr,
television history, explainer, there's more to it
```

---

## 7. Playlist

Navrženo **`legacy`** (*Legacy Tech — The Old Systems Still Running
Everything*) — přesně téma videa: stará technologie, která pořád běží.
Dopiš slug do `playlisty.json`, spusť `analytics.py --videa` a pak
`tools/playlisty.py`.
