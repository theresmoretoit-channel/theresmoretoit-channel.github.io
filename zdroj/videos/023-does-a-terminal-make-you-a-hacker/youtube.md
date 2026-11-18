# Podklady k nahrání na YouTube

Dvacáté třetí video kanálu **There's More To It**.

| co | odkud |
|---|---|
| video | `render/final-en.mp4` — **9:56, 1920×1080, 53 MB, −14,0 LUFS / −1,2 dBTP** |
| náhled | `render/thumbnail.jpg` — hotový obrázek, 1280×720, 313 kB, viz `thumbnail/PUVOD.md` |
| titulky | `subtitles/*.srt`, devět jazyků |
| atribuce do popisu | `CREDITS.md` — dva archivní snímky |

> **Napřed nastav jazyk videa na `en-gb`**, jinak zůstane dlaždice
> „Titulky" zašedlá. Hlas je `bf_emma`, tedy britská angličtina.

> **Master je hotový a ověřený.** Dekódovací test projde beze slova,
> všech 72 scén má skutečný obrázek (žádné placeholdery). Renderováno
> na herním PC přes reverzní tunel za **9,4 minuty**.

---

## Titul

**Are You a Hacker Just Because You Opened a Terminal?**

Varianty, kdyby byl potřeba kratší:

- Are You a Hacker Just Because You Opened a Terminal?
- Is That Hacking, or Is He Just Fixing the Server?
- What Hacking Actually Looks Like

## Popis

```
You open a terminal. Someone walks past, sees a black screen covered in
mysterious text, and decides you are hacking.

Maybe. Or maybe you are just trying to find out why the server is down.

This video is about why terminals and hacking became almost the same
thing in popular culture — and what hacking actually looks like. The
green phosphor that Hollywood borrowed. The progress bar that reaches
one hundred per cent. The line "I'm in." And then the real version,
where the server says permission denied and you spend twenty minutes
discovering that you forgot one character in a configuration file.

Along the way: what nmap actually does, why seeing /etc/passwd is not
the same as discovering everyone's passwords, why sudo rm -rf / does not
do what the story says any more, and why a real attack usually looks
like a perfectly ordinary login screen.

The difference between administration and hacking is not the colour of
your terminal, how many monitors you have, or whether you are wearing a
hoodie. It is what you are doing, and whether you have permission to do it.

Chapters below. Subtitles are written for this video, not auto-generated.
An American English audio track is available as a second audio track.

---

Full transcript, sources and translations: https://theresmoretoit-channel.github.io/videos/does-a-terminal-make-you-a-hacker/

00:00 Someone walks past
00:29 The magical black screen
00:59 Why it looks like that
01:43 The Hollywood hacker
02:17 The real conversation
02:58 A terminal is an interface
03:41 What a hacker actually is
04:16 Back to the picture
04:51 What nmap really does
05:31 The password file myth
06:05 Cracking, slowly
06:29 Why they type so fast
06:57 The most dangerous command
07:43 What a real attack looks like
08:22 A hacker does not look like one
08:47 So was she hacking?
09:18 What the difference really is

---

IMAGE CREDITS
Vt100-adventure — Retro-Computing Society of Rhode Island, CC BY-SA 3.0
via Wikimedia Commons
Licences: creativecommons.org/licenses/by-sa/3.0
All other archive images are in the public domain.
```

## Kapitoly

Sedmnáct kapitol, ověřeno proti `work/timing.json`:

| | |
|---|---|
| první začíná na `00:00` | ✅ (S01 startuje v 0,4 s kvůli `lead_in`, kapitola se píše jako nula) |
| aspoň tři kapitoly | ✅ sedmnáct |
| každá aspoň 10 s | ✅ nejkratší **23,7 s** |

## Titulky

Devět jazyků, u všech **nula řádků přes 42 znaků a nula třířádkových**:

| | titulků | útržků |
|---|---|---|
| `en` | 165 | 2 % |
| `cs` | 217 | 6 % |
| `sv` | 218 | 5 % |
| `es` | 218 | 1 % |
| `pt-BR` | 219 | 1 % |
| `de` | 220 | 4 % |
| `fr` | 221 | 2 % |
| `it` | 217 | 2 % |
| `pl` | 218 | 4 % |

Kód jazyka je zároveň přípona souboru a odpovídá kódu, který zná YouTube.
Anglicky je **`en-gb`**.

## Náhled

**`thumbnail/c4-is-this-hacking-server-room.png`** — hotový obrázek
(ChatGPT, 2026-09-04), ne kreslený kódem. Postup podle
`docs/thumbnail-styl.md`; původ, otisk a rozbor jsou v `thumbnail/PUVOD.md`.

Serverovna, muž u terminálu s běžícím nmapem a druhý muž ve dveřích
s rukou na ústech. Text je jeden blok: bílé *IS THIS* a pod ním žluté
*HACKING?* na štětcovém pruhu.

| veličina | tento | pásmo vydaných náhledů |
|---|---|---|
| jas | **46,0** | 21,2 az 36,2 |
| saturace | **62,9** | 44,8 az 62,4 |
| kontrast | **71,6** | 35,5 az 64,9 |
| ztráta detailu | 37,8 | 23,9 az 48,8 |

**Terminál je věcně správný** a ověřený řádek po řádku při trojnásobném
zvětšení — to je u tohohle videa podstatné, protože deset minut opravuje
technické nesmysly. Trvalo to deset kol; co se v nich rozbilo a proč,
je v `PUVOD.md`.

Kreslené koncepty `c1` az `c3` zůstávají v `thumbnail/` pro případné
„Test & Compare".

## Označení AI obsahu

Odpověď na dotaz „byla použita AI" je **ne**:

- **86 %** scén jsou diagramy kreslené kódem (64 ze 72)
- SDXL dělá **6 scén** a všechny jsou malované ilustrace, ne fotorealismus
- dva archivní snímky jsou upravené jen barevně a výřezem — *„color
  adjustment or lighting filters"* je výslovná výjimka pravidel
- hudba je **procedurální** (`tools/music.py`), ne z generativního modelu

## Závěrečná obrazovka a karty

`S71` je na ně **navržená**: text je v horní třetině, dolní třetina
a pravá strana zůstávají prázdné, protože tam YouTube klade karty.

Trvá ale jen **3,4 s**, protože `timing.tail` je pořád 1,2 s. CLAUDE.md
tuhle úpravu **odkládá** za zvednutí CTR — závěrečnou obrazovku vidí podle
naměřených křivek asi patnáct lidí napříč kanálem, kdežto miniatura
rozhoduje o tisících. Až se CTR zvedne, stačí zvednout `tail` na 6 s
a přegenerovat; scéna už je připravená.

## Kontrola před nahráním

```bash
ffprobe -v error -show_entries format=duration -of default=nw=1:nk=1 \
        videos/023-does-a-terminal-make-you-a-hacker/render/final-en.mp4
ffmpeg -v error -i videos/023-does-a-terminal-make-you-a-hacker/render/final-en.mp4 -f null -
```

Druhý příkaz musí projít **beze slova**. A pak podle CLAUDE.md: **nahraj
jako neveřejné a podívej se na to v přehrávači** — jak vyjde tmavá scéna
po překódování YouTube se dopředu posoudit nedá, a tohle video je tmavé
skoro celé.
