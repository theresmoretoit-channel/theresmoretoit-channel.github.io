# Podklady k nahrání — Teleportation: What Would It Actually Take?

| co | odkud |
|---|---|
| video | `render/final-en.mp4` (13:29, 1920×1080, −14,06 LUFS / −1,37 dBTP, 60,6 MB) |
| náhled | `render/thumbnail.jpg` (1280×720, 104 kB, koncept `c1-which-one`) |
| titulky | `subtitles/*.srt`, devět jazyků |
| jazyk videa | **`en-gb`** — nastavit PRVNÍ, jinak zůstane dlaždice „Titulky" zašedlá |
| byla použita AI? | **ne** — viz níž |

---

## 1. Titul

```
Teleportation: What Would It Actually Take?
```

## 2. Popis

**Zkopíruj CELÝ text mezi trojicí zpětných apostrofů.** Nic mimo tenhle
blok se na YouTube nedostane.

```
Teleportation is not one technology. It is at least five, and they fail
in completely different ways.

This video walks through each of them: the portal that removes the
distance instead of moving you, the transporter that scans and rebuilds
you, the machine that copies your mind, and the science-fiction trick of
walking through walls. Along the way we work out how much information a
human being actually is, why quantum mechanics makes the scan harder
rather than easier, and why the receiving machine turns out to be the
most advanced factory in the universe.

And then the part no engineering solves. If a perfect copy of you wakes
up on Mars while the original is still standing on Earth, which one is
you? Nobody can prove that the consciousness on the other side is the
same consciousness that entered.

Chapters:
00:00 Step in, step out
00:41 The portal
02:12 The transporter
03:18 You cannot photograph a brain
04:18 How much data is a person
05:19 The quantum problem
06:04 Now build the human
06:54 Where does the matter come from
08:04 One synapse wrong
08:38 Mars-you and Earth-you
09:22 Scan, kill, copy
10:12 And if there are two
10:46 Teleport the mind instead
11:26 Out of phase
12:00 Which one is hardest
12:34 Would you use it

Subtitles are written for this video, not auto-generated. An American
English audio track is available as a second audio track.

If you want the next one, there is a subscribe button.

All visuals in this video are drawn or painted. No archive photographs
were used, so there is nothing to attribute.
```

> **Proč tu není blok `IMAGE CREDITS`:** tohle video nemá **ani jeden**
> archivní snímek (96 diagramů + 4 malované SDXL scény), takže
> `sources.json` je prázdný a atribuovat není co. U videí s archivem
> patří kredity **dovnitř** tohohle bloku — naměřeno, že u čtyř
> ze šestnácti videí chyběly právě proto, že visely pod ním.

## 3. Kapitoly

Ověřeno proti `work/timing.json`: první je `00:00`, je jich **šestnáct**
a nejkratší trvá **33 s** (limit YouTube je 10 s). Hranice sedí na
začátky scén S01, S07, S19, S27, S35, S42, S46, S53, S59, S63, S69,
S76, S81, S86, S89, S93.

## 4. Titulky

Nahrát všech devět. Kód jazyka je zároveň přípona souboru.

| kód | jazyk | titulků |
|---|---|---|
| `en-gb` | English (United Kingdom) | 223 |
| `cs` | čeština | 295 |
| `sv` | svenska | 296 |
| `es` | español | 301 |
| `pt-BR` | português (Brasil) | 299 |
| `de` | Deutsch | 301 |
| `fr` | français | 301 |
| `it` | italiano | 301 |
| `pl` | polski | 297 |

U všech devíti: **nula řádků přes 42 znaků, nula třířádkových titulků.**

## 5. Nastavení

| pole | hodnota |
|---|---|
| jazyk videa | `en-gb` |
| **byla použita AI?** | **NE** |
| kategorie | Věda a technika |
| pro děti | ne |

**Proč „ne" u AI:** rozhoduje fotorealističnost, ne použití AI
([pravidla](https://support.google.com/youtube/answer/14328491)).
Devadesát šest scén ze sta jsou diagramy kreslené kódem. Zbylé čtyři
jsou SDXL, ale kotva stylu z nich dělá **malované ilustrace**, ne
fotografie. Hudba je **procedurální** (sinusovky a šum v numpy), ne
z generativního modelu. Hlas je Kokoro `bf_emma` — syntetický, ale
**neklonuje skutečnou osobu**.

## 6. Tagy

```
teleportation, physics, thought experiment, personal identity,
quantum teleportation, no-cloning theorem, wormhole, star trek
transporter, philosophy of mind, consciousness, science explained,
mars, duplicate problem, teleporter paradox
```

## 7. Než klikneš na Zveřejnit

1. **Napřed jazyk videa**, pak teprve titulky.
2. **Nahraj jako neveřejné a podívej se na to v přehrávači.** YouTube
   video překóduje a jak vyjde tmavá scéna po jejich kompresi se
   dopředu posoudit nedá. Tohle video je tmavé skoro celé (jas diagramů
   17 z 255), takže je to tady důležitější než obvykle.
3. Závěrečná obrazovka a karty jdou přidat i po zveřejnění.
   **Poslední scéna S100 je pro ně navržená** — kompozice je v horních
   dvou třetinách a vlevo, dolní třetina a pravá část rámu jsou prázdné.
