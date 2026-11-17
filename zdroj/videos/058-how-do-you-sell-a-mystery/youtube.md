# Podklady pro YouTube — 058

Formát a pravidla: `docs/zverejneni.md`. **Uživatel kopíruje jen text
mezi trojicí zpětných apostrofů pod každým nadpisem**, takže všechno
povinné musí být uvnitř bloků.

Video nahrané ručně: **`F5A1ONGxNZE`**
(https://www.youtube.com/watch?v=F5A1ONGxNZE).

## 1. Titul

```
How Do You Sell A Mystery?
```

## 2. Popis

```
In March 1968 a Swiss hotel manager published a book about the pyramids. It sold seventy million copies. In November of the same year the police arrested him — not for anything he had written, but for forging hotel paperwork to take out loans worth a hundred and thirty thousand dollars, which he had spent on the travel the book describes.

Does that prove his theories about ancient aliens were a deliberate fraud? No. It proves he committed fraud. Those are two different claims, and the gap between them is what this video is about.

Because the interesting thing about Erich von Däniken isn't whether he was honest. It's that his method still works, and it has three steps: start with something real, point at something we don't fully understand, and ask whether the answer might be extraordinary. The first two steps can be completely true. That is exactly what makes the third one land.

We take that apart on the Nazca Lines and on the lid of Pakal's sarcophagus at Palenque — where the same carving carries two entirely different sets of names, and where archaeologists' objection isn't that it looks nothing like a rocket, but that the rocket reading comes from looking and nothing else.

Then the uncomfortable part: the method doesn't need a liar. It works perfectly well in the hands of a believer. And once television got hold of it, it didn't need the believer either.

Chapters
0:00 A way of telling a story
0:24 A hotel manager, arrested
0:58 Two different claims
1:27 How do you sell a mystery?
1:36 Step one: something real
1:59 Step two: something unexplained
2:21 Step three: something extraordinary
2:39 What archaeologists found
3:37 Take Palenque
4:08 What the reading skipped
4:32 So was he lying?
5:25 The method doesn't need a liar
6:07 Television arrives
6:39 Making the answer dull
7:32 Twenty seconds against three hours
7:56 One note about that film
8:30 What became of his idea
9:49 We already have people

The documentary mentioned in the video is Ancient Aliens Debunked (2012) by Chris White, a point-by-point look at the archaeology behind the claims: ancientaliensdebunked.com

Subtitles are written for this video, not auto-generated. An American English audio track is available as a second audio track.

Music is generated procedurally for this channel.

IMAGE CREDITS
Erich von Daniken (crop) — Michal Maňas, CC BY 3.0
Líneas de Nazca, Nazca, Perú — Diego Delso, CC BY-SA 4.0
Temple of Inscriptions, Palenque — Antony Stanley, CC BY-SA 2.0
Lápida del sarcófago de Pakal — Rjcastillo, CC BY-SA 4.0
via Wikimedia Commons
Licences: creativecommons.org/licenses/by/3.0, /by-sa/2.0, /by-sa/4.0
```

## 3. Náhled

`render/thumbnail.jpg` — hotový, dodal uživatel (ChatGPT) podle konceptu
c3. Zdroj, otisk, měření a rozbor: `thumbnail/PUVOD.md`.

## 4. Titulky

`subtitles/*.srt` — `en`, `en-US` a třináct překladů
(`cs sv es pt-BR de fr it pl id tr uk vi fi`).
Jazyk videa je **`en-gb`** a nastavuje se **první**, jinak zůstane
dlaždice Titulky ve Studiu zašedlá.

## 5. Lokalizované názvy a popisy

`youtube-preklady.md`, nahraje `tools/lokalizace.py`.

## 6. Tagy

```
ancient aliens, Erich von Daniken, Chariots of the Gods, pseudoscience, Nazca lines, Palenque, Pakal, ancient astronaut theory, critical thinking, archaeology, debunked, media literacy, how documentaries work, Ancient Aliens Debunked, Maya
```

## 7. Nastavení

| | |
|---|---|
| kategorie | Věda a technika |
| jazyk videa | **en-gb** (nastavit jako první) |
| pro děti | ne |
| **byla použita AI** | **ne** — SDXL scény jsou malované ilustrace, archivní snímky upravené jen barevně (výslovná výjimka pravidel), hudba procedurální, hlas není klonovaný |
| licence | standardní |
| vkládání | povolené |
| playlist | doplnit do `playlisty.json`, pak `analytics.py --videa` a `playlisty.py` |

## 8. Co musí uživatel naklikat sám

Podle toho, jak se video nahraje:

| | ručně ve Studiu (`--k-videu`) | `videos.insert` |
|---|---|---|
| prohlášení o AI | vyřídí průvodce | **ručně** |
| osvědčení o zproštění | vyřídí průvodce | **ručně** |
| **závěrečná obrazovka** | **ručně** | **ručně** |

Data API na závěrečnou obrazovku nemá ani zdroj (ověřeno 2026-09-08).
Místo na ni je ve scénách **S80–S84** (posledních 20 s): `zaver_check.py`
hlásí u všech pěti **nulový překryv** v horních rozích. **Prvky patří
nahoru** — dole sedí ambrový titulek diagramu.

## 9. Atribuce: čtyři povinné, a jedna z nich NENÍ v `CREDITS.md`

Video má tři archivní scény (S04, S14, S30) a **jeden snímek vložený
přímo do SVG** (víko Pakalova sarkofágu v S31–S35).

> **Ten čtvrtý `CREDITS.md` NEOBSAHUJE** a obsahovat nebude:
> generuje ho `archive.py` ze scén se `source: "archive"`, kdežto tenhle
> leží v `art/` a je uvnitř kresby. Evidence je v `art/PUVOD.md`
> a v `sources.json` pod klíčem `art:pakal-viko`.
>
> **Proto je v bloku „Popis" vypsaný ručně.** Kdyby se kredity jen
> zkopírovaly z `CREDITS.md`, chyběl by — a byla by to táž vada jako
> u čtyř videí ze šestnácti, kde atribuce visela mimo blok.

Všechny čtyři licence vyžadují uvedení autora; tři z nich jsou navíc
share-alike. Strojová kontrola: projít `sources.json`, vytáhnout položky
s `CC BY*` a ověřit, že jméno autora je v bloku pod `## 2. Popis`.

## 10. Odkaz na dokument je SLIB Z VIDEA, ne bonus

Scéna S68 říká doslova *„I will put a link to the documentary below."*
Kdyby odkaz v popisu nebyl, video by slibovalo něco, co nesplní —
a u videa o poctivém zacházení s doklady by to bylo obzvlášť nešikovné.

Odkazuje se na **vlastní stránku filmu**, ne na konkrétní kopii na
YouTube: kopie mizí, stránka je stabilnější a uvádí i zdroje.
