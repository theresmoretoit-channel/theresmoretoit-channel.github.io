# YouTube — 133 „Why Hasn't Big Tech Replaced Linus Torvalds?“

Stav: **nahráno** (MP4 ručně 2026-11-02; metadata, náhled, lokalizace 13 jazyků a 15 titulkových stop přes API 2026-11-03). Stav zveřejnění je v `Témata.fods`. Stav zveřejnění je
v `Témata.fods`.

| | |
|---|---|
| ID videa | `yDxHtLOfVD8` — https://www.youtube.com/watch?v=yDxHtLOfVD8 |
| master | `render/final-en-133.mp4` (render na .207, 2026-11-02) |
| náhled | ✅ `render/thumbnail.jpg` — koncept C1 (`thumbnail/PUVOD.md`) |
| nastavení, popis, tagy | podklady níž |
| lokalizace | `youtube-preklady.md`, 13 jazyků |
| titulky | ✅ nahoře všech 15 (14 jazyků + `en-US`), automatický přepis smazán |
| americká stopa | `render/audio-en-US.m4a`, ručně ve Studiu |
| závěrečná obrazovka | S83–S85, **horní polovina** (viz níž) |
| karty | žádné |
| playlist | ✅ `legacy`, hned za 033 |

**Co musí uživatel naklikat sám:** závěrečnou obrazovku, americkou
audiostopu (`render/audio-en-US.m4a`) a osvědčení o zproštění, pokud ho
nevyřídil průvodce nahráním.

Stopáž 7:26 (`work/timing.json` total 446,2 s).

> **Před nahráním přeověřit S10** (`factcheck.md`): je-li venku 7.4
> (kolem začátku ledna 2027), čísla z LWN se mění — a s nimi hlas,
> titulky i diagram S10 (nese „LINUX 7.3“), ne jen popis.
>
> Kdyby se znovu pouštěl `tts.py`, přepočítej kapitoly tady
> i v `youtube-preklady.md` a přegeneruj `en-US` přes `us_stopa.py`.

Pořadí podle CENY (`docs/zverejneni.md`):

```bash
V=videos/133-why-hasnt-big-tech-replaced-linus-torvalds
python tools/nahraj.py $V --k-videu=yDxHtLOfVD8 --bez-titulku   # 100
python tools/analytics.py --videa                        #   1  ← nutné
python tools/lokalizace.py $V                            #  50
python tools/titulky.py $V --smaz-asr                    # 150  ← před titulky
python tools/titulky.py $V                               # 400×15
python tools/playlisty.py                                #  50
# úklid, až je MP4 na YouTube:
rm $V/render/draft*.mp4
ssh vrana@192.168.0.207 'rm -rf /home/vrana/temp/render-133-why-hasnt-big-tech-replaced-linus-torvalds'
```

---

## 1. Titul

```
Why Hasn't Big Tech Replaced Linus Torvalds?
```

> Wh-otázka, 44 znaků, shodná s `project.json`. Odpověď (důvěra, ne
> vlastnictví, S79–S83) titul neprozrazuje.

---

## 2. Popis

```
Google, Microsoft, Intel, Amazon and Meta all depend on Linux. When their engineers want to change it, they send their work to one man who doesn't work for any of them, and wait for his answer. They can't fire him. They can't overrule him. So why haven't they replaced him?

This video follows the code: how many of the latest nineteen thousand changes Linus wrote himself, what happened when Google kept its own branch of the kernel for Android, how a change travels through thousands of maintainers before it reaches him, who actually pays his salary, what happened when he took a whole file system back out of Linux, and what the project did the one time he stepped away.

Sources: LWN.net (kernel release statistics, Android and the mainline kernel, the 2018 break); the Linux kernel git history and documentation (development process, MAINTAINERS, project continuity); Greg Kroah-Hartman's blog (2010); Android Open Source Project documentation on the Generic Kernel Image; Android Developers Blog on Project Treble (2017); the Linux kernel mailing list and Phoronix on bcachefs (2024–2025); Linux Foundation Form 990 (FY2024), Annual Report 2025 and membership announcements; TOP500 (since November 2017).

Subtitles are written for this video, not auto-generated. An American English audio track is available as a second audio track.

Full transcript, sources and translations: https://theresmoretoit-channel.github.io/videos/why-hasnt-big-tech-replaced-linus-torvalds/

CHAPTERS
00:00 The man Big Tech can't fire
00:39 From a student's hobby to the world's servers
01:27 Make your own Linux
02:56 Easy to copy, expensive to keep
03:13 How code reaches Linus
03:56 Who pays Linus?
04:59 The final word
05:56 When Linus is gone
06:51 So why hasn't Big Tech replaced him?
07:14 A question for you

IMAGE CREDITS
LinuxCon Europe Linus Torvalds 03 (cropped) — Krd (photo), Von Sprat (crop), CC BY-SA 4.0
Greg-Kroah-Hartman — Sebastian Oliva, CC BY-SA 3.0
via Wikimedia Commons
Licences: creativecommons.org/licenses/by-sa/4.0, creativecommons.org/licenses/by-sa/3.0
```

> **Blok se kopíruje CELÝ** (`docs/zverejneni.md`). Archivní snímky jsou
> jen dva (S06, S73) a oba pod CC BY-SA, takže věta o public domain
> odpadá.
>
> **Pointa se neprozrazuje:** popis nejmenuje závěr S79–S83 (moc z důvěry,
> ne z vlastnictví; místo, které nevlastní žádná z firem), ani číslo
> „Nine“ (S12) — jen *how many … Linus wrote himself*. Kapitola 06:51 je
> proto otázka z titulu, ne odpověď.
>
> **Zdroje** jsou hlavní zdroje z `factcheck-zaklad.md`. Ballmer a The
> Register ve scénáři v0.4 nejsou, proto chybí i tady.
>
> Kapitoly ze scén S01, S09, S17, S33, S36, S44, S58, S69, S80, S84
> (`work/timing.json`, zaokrouhleno dolů). Nejkratší 11,4 s (S84 → konec),
> druhá 17,4 s (S33 → S36), první na 00:00, všechny ≥ 10 s. Výzvy
> k odběru (za S16 a S57) leží uvnitř kapitol.

---

## 3. Náhled

`render/thumbnail.jpg` (1280×720, 0,28 MB): keramický tučňák se zlatou
korunkou, *LINUX* / *WHO CROWNED HIM?* — koncept C1 z
`thumbnail/ZADANI.md`, původ a otisky v `thumbnail/PUVOD.md`.

---

## 4. Titulky

`subtitles/*.srt`, 14 jazyků + `en-US`. Jazyk videa **`en-gb`** (hlas
`bf_emma`) se musí nastavit dřív, než se nahrají titulkové stopy.
Codex hotový a zapracovaný (`notes.md`, „Překlady 14 jazyků“).

---

## 5. Nastavení

| | |
|---|---|
| kategorie | **Science & Technology** (28) — posílá `nahraj.py` napevno |
| jazyk videa | `en-gb` |
| licence | standardní |
| pro děti | **ne** |
| komentáře | zapnuté (S84–S85 je otázka do komentářů) |
| **byla použita AI** | **ne**. 81 scén z 85 je kreslených kódem (diagramy, 27 animací). Dvě SDXL scény (S44 věže firem, S71 prázdná židle) jsou podle kotvy stylu **malované ilustrace** (*painterly editorial illustration*), ne fotorealismus, a nezobrazují konkrétní skutečné místo ani událost. Dva archivní snímky (S06, S73) jsou jen barevně upravené. Hudba je procedurální, hlas není klon. |

### Závěrečná obrazovka

Od **7:06** (posledních 20 s), tedy S83–S85. `zaver_check` hlásí
v dolních rozích titulek, kresba je jen v dolní polovině. **Dlaždici
i odběr dej do HORNÍ poloviny.** Jako dlaždici doporučuju **033 *You
Probably Use Linux Already*** (1991, kde všude Linux běží — příběh, který
tohle video zkrátilo na dvě věty), druhou nechat na „nejlepší pro diváka“.

---

## 6. Tagy

```
linus torvalds, linux, linux kernel, open source, linux foundation,
greg kroah-hartman, android kernel, generic kernel image, fork,
kernel maintainers, bcachefs, big tech, google, microsoft,
open source governance, how linux is developed, there's more to it
```

---

## 7. Playlist

**Návrh: `legacy`** (*Legacy Tech — The Old Systems Still Running
Everything*), hned za 033 (*You Probably Use Linux Already*), se kterým
sdílí téma. Alternativa je `pocitace`, ten je ale o tom, co se děje
v počítači, ne o tom, kdo software řídí. Na playlistu závisí i nástěnka
Pinterestu u shortů (`zverejneni.md`). Zapsat do `playlisty.json` při
nahrání; `playlisty.py` ho přeskočí, dokud video není
v `analytics/videa.json`.
