# Podklady pro YouTube — 057

Formát a pravidla: `docs/zverejneni.md`. **Uživatel kopíruje jen text
mezi trojicí zpětných apostrofů pod každým nadpisem**, takže všechno
povinné musí být uvnitř bloků.

Video nahrané ručně: **`l7ngTvlgKa8`**
(https://www.youtube.com/watch?v=l7ngTvlgKa8).

## 1. Titul

```
Why Do We Believe Before We Check?
```

## 2. Popis

```
You see a headline. You get angry. You share it. And only later do you ask yourself whether it was actually true.

That isn't a problem with the internet. It starts with something your brain does before the headline even lands — and the reason it's still there is that fear used to be cheap and being wrong about fear used to be fatal.

We go from a noise in the bushes to a street full of frightened people who never received a single piece of new information, to an election, to a 2005 study in which one second of looking at a face predicted the winner of roughly seven out of ten Senate races.

And then the turn. If our feelings push us around this easily, what are we supposed to do about it? Check everything ourselves? Try that exactly once — pick one claim about the economy and follow it to the bottom — and the real question turns out to be a different one: how do you decide who to trust when you can't check?

There is an answer, and it doesn't require you to be an expert. It also doesn't let any of us off the hook: the research on this is uncomfortable, because being good at reasoning turns out to make people better at defending what they already thought.

Chapters
0:00 A headline, and then a question
0:22 A brain that doesn't wait
1:00 Fear spreads without information
1:45 Now think about an election
2:17 One second and a face
3:10 Why a false story wins
4:00 But wait
4:16 Try checking one thing
4:58 Needing to trust isn't weakness
5:20 Science gets things wrong
6:25 Four questions anyone can ask
7:33 Being clever doesn't protect you
8:35 And this includes us
9:17 Ten seconds

Subtitles are written for this video, not auto-generated.

Music is generated procedurally for this channel.
```

## 3. Náhled

`render/thumbnail.jpg` — hotový, dodal uživatel (ChatGPT).
Zdroj, otisk a rozbor: `thumbnail/PUVOD.md`.

## 4. Titulky

`subtitles/*.srt` — `en`, `en-US` a třináct překladů
(`cs sv es pt-BR de fr it pl id tr uk vi fi`).
Jazyk videa je **`en-gb`** a nastavuje se **první**, jinak zůstane
dlaždice Titulky ve Studiu zašedlá.

## 5. Lokalizované názvy a popisy

`youtube-preklady.md`, nahraje `tools/lokalizace.py`.

## 6. Tagy

```
critical thinking, misinformation, disinformation, psychology, cognitive bias, motivated reasoning, media literacy, how to spot fake news, why people believe, emotion and reason, trust in science, fact checking, Kahan, Todorov, social psychology
```

## 7. Nastavení

| | |
|---|---|
| kategorie | Věda a technika |
| jazyk videa | **en-gb** (nastavit jako první) |
| pro děti | ne |
| **byla použita AI** | **ne** — kresby jsou ploché ilustrace, hudba je procedurální, žádná fotorealistická scéna ani klonovaný hlas |
| licence | standardní |
| vkládání | povolené |
| playlist | doplnit do `playlisty.json`, pak `analytics.py --videa` a `playlisty.py` |

## 8. Co musí uživatel naklikat sám

Video je nahrané ručně, takže prohlášení o AI i osvědčení o zproštění
vyřídil průvodce ve Studiu. **Zbývá jediné: závěrečná obrazovka** —
Data API na ni nemá ani zdroj (ověřeno 2026-09-08).

Místo na ni je připravené ve scénách **S70, S71 a S72** (posledních 20 s):
`zaver_check.py` hlásí u všech tří nulový překryv v horních rozích.
**Prvky patří nahoru**, dole je ambrový titulek diagramu.

## 9. Bez atribucí, a je to v pořádku

Video nemá **jedinou archivní scénu** — 73 diagramů, 3 SDXL, nula
archivu — takže `sources.json` ani `CREDITS.md` neexistují a v popisu
nic atribuovat netřeba. Hudba je procedurální (`tools/music.py`),
tedy bez licenčních vazeb.
