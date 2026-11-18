# Podklady pro YouTube — 042

Nahrává se `render/final-en.mp4` (master, ne draft), `render/thumbnail.jpg`
a `subtitles/*.srt` v devíti jazycích. Lokalizované názvy a popisy jsou
v `youtube-preklady.md` a nahrává je `tools/lokalizace.py`.

## 1. Titul

```
How Old Is AI, Really?
```

22 znaků. Limit je 100, mobil ukáže zhruba 60 — vejde se bez oříznutí.

> **Změněno 2026-09-13 na návrh uživatele.** Původní `AI Didn't Start
> With ChatGPT` je TVRZENÍ, které pointu videa řekne rovnou — táž vada,
> jakou měly první tři koncepty náhledu. Změřeno na 29 videích kanálu
> s aspoň sto zobrazeními: wh-otázka 2,23 % vážené CTR, tvrzení 1,63 %,
> ano/ne otázka 1,21 %. Proto wh-otázka, ne `Did AI Start With ChatGPT?`.
> Cena je, že v titulu zmizelo vyhledávané slovo ChatGPT — zůstává
> v tazích a hned v prvním odstavci popisu.

## 2. Popis

**Kopíruje se CELÝ blok mezi apostrofy a nic jiného.**

```
At the end of November 2022, a web page appeared with a small box on it.
You typed a question, and a computer answered. For millions of people,
that was the moment artificial intelligence began.

Except a computer had done something like this fifty-six years earlier.

In 1966, a researcher at MIT published a program called ELIZA. It was not
intelligent, it was not a neural network, and it understood nothing at
all — it matched keywords and handed the rest back as a question. People
talked to it anyway. Weizenbaum's own secretary had watched him build it,
knew exactly what it was, and after a few exchanges asked him to leave
the room.

Which leaves a question the next half century kept walking into: how
little does a machine actually need to seem intelligent?

Along the way: the paper Alan Turing opened with "Can machines think?"
and the trick he used to replace that question; the 1943 model of a
neuron whose weights were set by hand; the winters when the funding
stopped; the photograph of a dog that computers could not recognise for
fifty years; and the reason a text box on a web page mattered more than
any of the technology behind it.

Full transcript, sources and translations: https://theresmoretoit-channel.github.io/videos/ai-didnt-start-with-chatgpt/

Chapters
00:00 A box on a web page
00:39 ELIZA
01:43 Can machines think?
02:28 A phrase nobody had written down
02:56 A neuron on paper
03:35 None of it worked
04:35 Then three things changed
05:11 Deep Blue
05:49 The dog
06:32 The transformer
07:02 GPT
07:42 30 November 2022
08:17 AI did not start with ChatGPT
08:47 So when did it start?
09:23 Back to a secretary at MIT

IMAGE CREDITS
Say hello to Deep Blue — Erik Pitti, CC BY 2.0
via Wikimedia Commons
Licences: creativecommons.org/licenses/by/2.0

A Proposal for the Dartmouth Summer Research Project on Artificial
Intelligence (1955) — John McCarthy et al., public domain, reproduced
from the facsimile in AI Magazine 27(4), 2006.

All other archive images are in the public domain.

Subtitles are written for this video, not auto-generated. An American
English audio track is available as a second audio track.
```

## 3. Tagy

```
artificial intelligence, AI history, ELIZA, Weizenbaum, Alan Turing, Turing test, Dartmouth, chatbot, ChatGPT, neural networks, AlexNet, transformer, GPT, Deep Blue, AI winter, machine learning, history of computing, perceptron
```

## 4. Nastavení

| | |
|---|---|
| viditelnost | nejdřív **neveřejně**, podívat se na to v přehrávači |
| jazyk videa | **en-GB** — nastavit NAPŘED, jinak zůstane dlaždice Titulky zašedlá |
| kategorie | Věda a technika |
| prohlášení o AI | **ne** — viz níž |
| licence | standardní |
| playlist | doplnit do `playlisty.json` a spustit `tools/playlisty.py` |

### Prohlášení o AI: odpověď je NE

Rozhoduje fotorealističnost, ne použití AI. V tomhle videu:

- jediná SDXL scéna (S27) je **malovaná ilustrace**, ne fotorealismus
- archivní snímky jsou upravené jen barevně — *„color adjustment or
  lighting filters"* je výslovná výjimka
- hudba je **procedurální** (sinusovky a šum v numpy), ne z generativního
  modelu

### Co musí uživatel naklikat sám

| | nahrál MP4 ručně (`--k-videu`) | `videos.insert` |
|---|---|---|
| prohlášení o AI | ✅ vyřídil průvodce | ❌ **ručně** |
| osvědčení o zproštění | ✅ vyřídil průvodce | ❌ **ručně** |
| **závěrečná obrazovka** | ❌ **ručně** | ❌ **ručně** |

Závěrečnou obrazovku API neumí vůbec. `zaver_check.py` ověřil, že v
posledních dvaceti sekundách (S59, S60, S61) je místo pro dlaždici
i kolečko odběru — **v HORNÍ polovině**, dole je titulek.

## 5. Po zveřejnění

```bash
python tools/titulky.py --vse --smaz-asr    # automatický přepis konkuruje překladům
```

Zapsat odkaz do `Témata.ods`, doplnit slug do `playlisty.json`, spustit
`analytics.py --videa` a pak `tools/playlisty.py`.

---

## Poznámka k atribucím

**Dartmouthský sken NENÍ v `CREDITS.md`**, protože ho nestahoval
`archive.py` — je to obrázek vytažený z PDF, ne soubor z Commons.
Do bloku výš je proto dopsaný ručně; evidence a licence jsou
v `art/PUVOD.md`.

Strojová kontrola atribucí (projít `sources.json`, vytáhnout každou
položku s `CC BY*` a ověřit jméno autora v bloku) najde jen
**Erika Pittiho** — ten v bloku je. Zbylé dva archivní snímky
(Weizenbaum, Turing) jsou public domain a kryje je souhrnná věta.
