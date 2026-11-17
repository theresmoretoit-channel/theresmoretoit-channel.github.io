# YouTube — 112 „Why Can't We Travel Faster Than Light?“

Stav: **nahráno 2026-10-17** (https://www.youtube.com/watch?v=CBMf9aawV-o). Metadata, náhled, 13 lokalizací a všech 15 titulkových stop přes API, playlist `vesmir` přes `playlisty.py`; americkou stopu, závěrečnou obrazovku, kartu na 111 a zveřejnění dělá uživatel ve Studiu. Stav zveřejnění je v `Témata.ods`.

| | |
|---|---|
| ID videa | `CBMf9aawV-o` |
| master | ✅ `render/final-en-112.mp4` (10:00, 1920×1080, 48 MB, render 2026-10-17 na .207) |
| náhled | ✅ `render/thumbnail.jpg` (LIGHT SPEED / WHY NOT FASTER?, obálka) — `thumbnail/PUVOD.md` |
| nastavení, popis, tagy | podklady níž |
| lokalizace | `youtube-preklady.md`, 13 jazyků, prošlo Codexem (3 opravy), ✅ nahráno |
| titulky | `subtitles/*.srt`, 14 jazyků + `en-US`, všechny překlady prošly Codexem, ✅ všech 15 přes API |
| americká stopa | `render/audio-en-US.m4a` — nahrává uživatel ve Studiu |
| závěrečná obrazovka | ručně ve Studiu |
| **karta** | **na 111 *What Would It Take to Travel Faster Than Light?* v čase 0:22 (S05)** — ručně ve Studiu |
| playlist | ✅ `vesmir`, pozice 8 |

**Co musí uživatel naklikat sám:** nahrát MP4 ve Studiu (průvodce vyřídí
prohlášení o AI a osvědčení o zproštění), závěrečnou obrazovku, kartu
na 111, americkou audiostopu (`render/audio-en-US.m4a`) — a **u 111
závěrečnou obrazovku přepnout na 112** (pokračování).

Stopáž 10:00 (`work/timing.json` total 600,3 s).

> Kdyby se znovu pouštěl `tts.py`, přepočítej kapitoly tady
> i v `youtube-preklady.md`, čas karty a přegeneruj `en-US` přes `us_stopa.py`.

Pořadí podle CENY (`docs/zverejneni.md`):

```bash
V=videos/112-why-cant-we-travel-faster-than-light
python tools/nahraj.py $V --k-videu=<ID> --bez-titulku    # 100
python tools/analytics.py --videa                         #   1  ← nutné
python tools/lokalizace.py $V                             #  50
python tools/titulky.py $V --smaz-asr                     # 150  ← před titulky
python tools/titulky.py $V                                # 400×15
python tools/playlisty.py                                 #  50
# úklid, až je MP4 na YouTube:
rm $V/render/draft*.mp4
ssh vrana@192.168.0.207 'rm -rf /home/vrana/temp/render-112-why-cant-we-travel-faster-than-light'
```

---

## 1. Titul

```
Why Can't We Travel Faster Than Light?
```

> Wh-otázka, 38 znaků. Odpověď (nadsvětelný signál umí poslat zprávu do
> minulosti; Hawking vs. Novikov) titul neprozrazuje.

---

## 2. Popis

```
Imagine sending a message faster than light. A friend on a distant spaceship reads it and replies just as fast, and the reply reaches you before you've sent the message. That isn't science fiction. It's what the equations of relativity say could happen.

In 1964 William Bertozzi gave electrons thirty times more energy, and they still wouldn't pass the speed of light. In 2011 the OPERA experiment seemed to catch neutrinos doing exactly that. And in 1988 Kip Thorne and two colleagues showed how a wormhole could be turned into a time machine. So why do physicists think the universe might not allow any of it?

The previous video, on warp drives and wormholes: What Would It Take to Travel Faster Than Light? https://www.youtube.com/watch?v=zGxKaV9OROE

Sources: W. Bertozzi, Speed and Kinetic Energy of Relativistic Electrons, Am. J. Phys. 32, 551 (1964); A. Einstein, Relativity: The Special and General Theory (1917), §8–9; Benford, Book & Newcomb, The Tachyonic Antitelephone, Phys. Rev. D 2, 263 (1970); Nagel et al., Nat. Commun. 6, 8174 (2015); OPERA (arXiv 1109.4897) and ICARUS (arXiv 1203.3433); Morris, Thorne & Yurtsever, Phys. Rev. Lett. 61, 1446 (1988); S. Hawking, Chronology protection conjecture, Phys. Rev. D 46, 603 (1992); Friedman et al., Phys. Rev. D 42, 1915 (1990); Echeverria, Klinkhammer & Thorne, Phys. Rev. D 44, 1077 (1991).

Subtitles are written for this video, not auto-generated. An American English audio track is available as a second audio track.

CHAPTERS
00:00 A reply before the message
00:40 Measuring the speed limit
01:47 Why should there be a limit?
02:40 Can an effect come before its cause?
03:06 Alice, Bob and a faster message
04:03 The tachyonic antitelephone
04:58 Could relativity be wrong?
05:21 OPERA's faster-than-light neutrinos
06:23 Turning a wormhole into a time machine
07:56 Does the universe forbid it?
08:44 Novikov and the billiard ball
09:30 Neither answer is proven

IMAGE CREDITS
OPERA detector — Mhier, CC BY-SA 3.0
Kip Thorne at Caltech — Keenan Pepper, CC BY-SA 3.0
Kip Thorne and Igor Novikov — Konstantin Malanchev, CC BY 2.0
via Wikimedia Commons
Licences: creativecommons.org/licenses/by-sa/3.0, creativecommons.org/licenses/by/2.0
All other archive images: NASA, public domain.
```

> **Blok se kopíruje CELÝ** (`docs/zverejneni.md`). CC snímky jsou tři
> (S49 CC BY-SA 3.0, S55 CC BY-SA 3.0, S75 CC BY 2.0), všechny atribuce
> jsou uvnitř. S69 (Hawking, NASA/Paul E. Alers) je public domain.
>
> **Pointa se neprozrazuje.** První odstavec je háček z S01–S04 (zazní
> v prvních 20 s). OPERA jen „seemed to“, výsledek opravy ne; Hawkingova
> ani Novikovova odpověď v popisu není.
>
> Kapitoly ze scén S01, S07, S14, S22, S27, S37, S42, S46, S53, S68, S75,
> S82 (`work/timing.json`, zaokrouhleno dolů). Nejkratší 23 s (S42 → S46),
> všechny ≥ 10 s, první na 00:00. Výzva k odběru S13b (1:39) leží
> v kapitole „Measuring the speed limit“.
>
> Zdroje podle `factcheck.md`. Čísla v popisu (1964, třicetkrát, 2011,
> 1988) jsou tatáž jako ve scénáři.

---

## 3. Náhled

✅ `render/thumbnail.jpg` — LIGHT SPEED / WHY NOT FASTER? (obálka se
světelnými stopami). Hotový obrázek od uživatele (ChatGPT, zadání B),
jen zmenšený; původ a otisk v `thumbnail/PUVOD.md`.

---

## 4. Titulky

`subtitles/*.srt`, 14 jazyků + `en-US`. Jazyk videa **`en-gb`** (hlas
`bf_emma`) se musí nastavit dřív, než se nahrají titulkové stopy.
Nahrávají se až po zapracování nálezů Codexu.

---

## 5. Nastavení

| | |
|---|---|
| kategorie | **Science & Technology** (28) — posílá `nahraj.py` napevno |
| jazyk videa | `en-gb` |
| licence | standardní |
| pro děti | **ne** |
| komentáře | zapnuté |
| **byla použita AI** | **ne**. 86 scén je kreslených kódem, 4 archivní snímky (detektor OPERA, Thorne, Hawking, Thorne s Novikovem) jsou jen barevně upravené. S74 (prázdný sál) je SDXL malba bez lidí, ne fotorealismus. S06 je obrázek z ChatGPT, ale obecná noční obloha s paprskem, ne skutečné místo, osoba ani událost (`art/PUVOD.md`). Hudba je procedurální, hlas není klon. |

### Závěrečná obrazovka

Od **9:40** (posledních 20 s), tedy S83–S86. `zaver_check` u nich hlásí
volnou **horní polovinu**, prvky patří **nahoru** (dole je titulek).
Dlaždice: 111 (předchozí díl), případně nejnovější video.

### Karta

Na video **111 *What Would It Take to Travel Faster Than Light?***
(`zGxKaV9OROE`) v čase **0:22** — S05 *„In our last video, we asked
what it would take to travel faster than light.“* začíná v 22,6 s.
(Druhá možnost je S53 v 6:23, *„But in our last video, we met
a different idea.“*)

---

## 6. Tagy

```
faster than light, speed of light, causality, time travel, special relativity,
relativity of simultaneity, tachyon, tachyonic antitelephone, wormhole,
time machine, kip thorne, stephen hawking, chronology protection,
novikov self-consistency principle, opera neutrinos, physics explainer,
science explainer, there's more to it
```

---

## 7. Playlist

`vesmir` (*Space — Getting There, and Who Else Is Out There*), na konec,
hned za 111.
