# Podklady k nahrání na YouTube

Časy kapitol **ověřené proti `work/timing.json`**, ne odhadnuté.
Každá kapitola je od předchozí aspoň 10 s, první je `00:00` a je jich
28 — YouTube uzná kapitoly, jen když platí všechny tři podmínky.

| co | odkud |
|---|---|
| video | `render/final-en.mp4` — 1920×1080, **9:54**, 54.8 MB |
| náhled | `render/thumbnail.jpg` — 1280×720, 0,08 MB (varianta c4, viz `notes.md`) |
| titulky | `subtitles/*.srt` — **patnáct stop**: čtrnáct jazyků + `en-US` |
| americká stopa | `render/audio-en-US.m4a` — 11,8 MB, `af_heart` při `speed` 0,9177 |
| lokalizované názvy a popisy | `youtube-preklady.md` přes `tools/lokalizace.py` |

**Šest archivních snímků a jejich atribuce je POVINNÁ** — pět z nich je
CC BY-SA, která uvedení autora vyžaduje. Je proto **uvnitř bloku
„Popis"**, ne pod ním: uživatel kopíruje jen to, co je mezi trojicí
zpětných apostrofů.

---

## Titul

```
Why Would Canada Join the European Union?
```

> Wh-otázka schválně (kanálem naměřeno na 29 videích, vážené impresemi:
> wh-otázka **2,23 %**, tvrzení 1,63 %, ano/ne otázka 1,21 %). Původní
> název námětu *„Canada wants to join the European Union"* je tvrzení
> a navíc vyzrazuje méně přesně, než se ve videu ukáže.

## Popis

```
In September 2026 the president of the European Commission stood up in the
European Parliament and invited Canada to become the first "associate
member" of the European Union. There is no such category in EU law. There
is also a treaty sentence saying that any European State may apply — and
Canada is not one.

But Canada is already halfway inside. It joined SAFE, the Union's joint
arms programme, in February 2026, as the first country from outside
Europe. It joined the EU research programme in 2024, two years after
Israel and New Zealand. Goods have crossed the Atlantic under a joint
trade agreement since 2017.

So geography guards the front door. It never guarded the side entrances.

This video is about what sits behind that: the Arctic, critical minerals,
a defence budget that is growing, and a trading relationship where three
quarters of everything Canada exports goes to one neighbour. And about the
problem Norway has lived with since 1994 — more than thirteen thousand
European rules adopted by a country that does not vote on any of them.

Nothing has been agreed. A summit in October is supposed to turn the idea
into something with edges, and Canada may end up with a slightly better
trade deal and nothing more. But Europe said out loud that membership
might not have to mean what it has always meant.

Chapters
00:00 Canada wants to join the European Union
00:22 Something that does not exist yet
00:37 Canada is already in SAFE
01:04 Research money and a trade deal
01:34 The rule about who may join
01:59 Israel and New Zealand are already in
02:19 Picture two doors
02:46 A third door
03:12 How wide does it open?
03:36 A carbon bill on imported steel
03:54 Norway said no. Twice.
04:14 Thirteen thousand rules
04:35 The staircase between in and out
05:00 Why would Europe want this?
05:12 The longest coastline on Earth
05:37 Nickel, cobalt, copper
06:00 The view from Ottawa
06:11 A dependency with a long border
06:25 Europe is doing the same arithmetic
06:57 The awkward questions
07:11 It follows the rule. It did not vote.
07:32 How many kinds of membership?
07:49 Back to the name
08:12 What the Union actually is
08:42 Six neighbours, 1951
08:55 Nothing has been agreed
09:27 Seventy-five years, one question
09:43 What the U could still mean

Subtitles are written for this video, not auto-generated. An American
English audio track is available as a second audio track.

IMAGE CREDITS
European Parliament Strasbourg Hemicycle — Diliff, CC BY-SA 3.0
Kiln 5, Pitstone cement plant — Dylan Moore, CC BY-SA 2.0
Norwegian EU membership referendum, 1994 result by counties — Paasikivi,
CC BY-SA 4.0
Sea Ice off Baffin Island — Jeff Schmaltz, public domain
Canada–United States border crossing at Vanceboro, Maine — DShaw20,
CC BY-SA 4.0
1951 CECA ECSC — Marc Baronnet, CC BY-SA 4.0
All via Wikimedia Commons.
CC BY-SA 2.0: https://creativecommons.org/licenses/by-sa/2.0
CC BY-SA 3.0: https://creativecommons.org/licenses/by-sa/3.0
CC BY-SA 4.0: https://creativecommons.org/licenses/by-sa/4.0

Every other visual in this video is drawn from code.
```

## Tagy

```
european union, canada, associate membership, eu enlargement, article 49,
norway, eea, single market, brussels, arctic, critical minerals, safe,
european defence, trade policy, cbam, carbon border, ottawa, geopolitics,
international organisations, sovereignty
```

## Nastavení

| pole | hodnota |
|---|---|
| **jazyk videa** | **`en-gb`** — nastavit **PRVNÍ**, jinak zůstane dlaždice Titulky zašedlá |
| kategorie | Věda a technika |
| **byla použita AI** | **NE** — viz níž |
| licence | standardní licence YouTube |
| vkládání | **povolit** (`videos.update` smaže, co v těle není) |
| viditelnost | nahrát **neveřejně**, podívat se na to v přehrávači, teprve pak zveřejnit |
| playlist | dopsat slug do `playlisty.json`, pak `analytics.py --videa` a `tools/playlisty.py` |

### Proč „byla použita AI" = NE

Rozhoduje **fotorealističnost, ne použití AI**:

- **93 ze 106 scén je kreslených kódem** (SVG → Inkscape), tedy diagramy
- **šest SDXL scén** (S12, S53, S59, S63, S94, S98) je díky kotvě stylu
  malovaných, ne fotorealistických
- **šest archivních snímků** je upravených jen barevně — *„color
  adjustment or lighting filters"* je výslovná výjimka pravidel
- hudba je **procedurální** (`tools/music.py`), ne z generativního modelu

Náhled je kreslený kódem (`thumbnail/gen.py`), takže ani tam není co
řešit — a ta otázka se navíc ptá na obsah videa, ne na miniaturu.

### Co musí uživatel naklikat sám

Při nahrání ručně ve Studiu + `nahraj.py --k-videu <ID>`:

| | |
|---|---|
| prohlášení o AI | ✅ vyřídí průvodce při nahrávání |
| osvědčení o zproštění | ✅ vyřídí průvodce |
| **závěrečná obrazovka** | ❌ **ručně** — Data API na ni nemá ani zdroj |

Poslední čtyři scény (S96–S102) mají volnou **horní** polovinu, takže se
tam dlaždice dalšího videa i kolečko odběru vejdou. Ověří
`python tools/zaver_check.py videos/052-why-would-canada-join-the-european-union`
po masteru.

### Stav: hotovo k nahrání

Master vyrenderovaný na herním PC (10,5 min, 1920×1080, supersample 3)
a ověřený `ffmpeg -v error -i … -f null -`, které **prošlo beze slova** —
samotná délka z kontejneru poškození neodhalí.

Šest SDXL scén (S12, S53, S59, S63, S94, S98) je vygenerovaných
ze skutečného modelu, ne placeholdery.

`zaver_check.py` hlásí u všech čtyř závěrečných scén (S99–S102) **nulový
překryv v horní polovině**. Prvky závěrečné obrazovky tedy patří NAHORU;
dole je ambrový nadpis, přes který detektor varuje u všech čtyř.
