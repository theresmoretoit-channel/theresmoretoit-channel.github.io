# Podklady pro nahrání na YouTube

Ručně psaný zdroj. Časy kapitol odpovídají `work/timing.json`
(celkem 9:35) — **po každém přegenerování hlasu je potřeba je znovu
odvodit**, protože se posunou.

---

## Titul

```
How Can You Sell Something You Don't Have?
```

41 znaků. Limit je 100, mobil ukáže zhruba 60 — vejde se bez oříznutí.
Otázka, ne tvrzení; odpovídá formátu kanálu a je to zároveň ústřední
otázka videa, na kterou se scénář v S57 vrací.

Zvažované alternativy:

- `The Day Oil Was Worth Less Than Nothing` — 38 znaků, nejsilnější háček,
  ale slibuje video o dubnu 2020, což je jen jedna třetina obsahu
- `You Can Sell Oil You Don't Own. Here's How.` — tvrzení místo otázky,
  a odpověď v titulku bere důvod dívat se
- `What Are We Actually Trading?` — přesné, ale bez konkrétní věci
  se nedá poznat téma, a náhled ho pak musí nést celý

> **Náhled má nést tu údernou část, titul popisnou a vyhledatelnou.**
> Až bude náhled hotový, zkontrolovat, že ta dvě neříkají totéž.

---

## Popis

První dva řádky jsou to jediné, co je vidět před „show more".

```
I offer to sell you a barrel of oil. There's one problem: I don't own it, and I don't
even want it. I just think the price is going down — and that turns out to be enough.

Short selling looks backwards because it is: you sell first and buy later. But follow
that idea far enough and it stops being about oil at all. Most futures contracts never
deliver a single barrel. Some refer to oil that hasn't been produced yet. And in April
2020 the price of a major oil contract briefly fell below zero, because holding it
meant being obliged to take delivery of something you had nowhere to put.

From barrels to contracts, from contracts to risk, and finally to markets that trade
nothing but the probability of an event. This is how a market can work without ever
needing the thing it is named after.

Chapters
0:00 The offer
0:25 Sell first, buy later
1:06 The loss with no ceiling
2:14 Why anyone would do this
3:10 We are not trading oil
3:58 Does the oil have to exist?
4:32 The anchor in the real world
5:16 April 2020: below zero
6:37 Trading obligations
7:10 A market in probabilities
8:12 The answer
8:55 So what are we trading?

Sources and image credits
The April 2020 settlement price of minus $37.63 per barrel is from the CFTC interim
report on NYMEX WTI crude contract trading around 20 April 2020. Fuel's share of
airline operating costs is from IATA. The share of futures contracts ending in
physical delivery is from CME Group.

IMAGE CREDITS
Boeing 757 at Miami airport with fuel truck, Dec 2016 — Sunnya343, CC BY-SA 4.0
Anacortes Refinery 31911 — Walter Siegmund, CC BY 2.5
Empty northwestern motorway during coronavirus lockdown — Megan Harvey, CC BY-SA 4.0
Oil storage tanks, Eastham (geograph.org.uk 209801) — Peter Craine, CC BY-SA 2.0
via Wikimedia Commons
Licences: creativecommons.org/licenses/by-sa/4.0, /by/2.5, /by-sa/2.0
All other archive images are in the public domain or CC0.

Music is generated procedurally for this channel. Illustrations are drawn in code or
generated as painterly illustration; no photorealistic synthetic imagery is used.

Subtitles are written for this video, not auto-generated. An American English
audio track is available as a second audio track.
```

> **Kredity jsou UVNITŘ bloku**, ne pod ním. U čtyř videí ze šestnácti
> chyběla atribuce právě proto, že visela jako poznámka pod blokem —
> uživatel kopíruje jen text mezi apostrofy.
>
> Vypsané jsou čtyři snímky s licencí `CC BY*`, u kterých je atribuce
> **povinná**. Pátý (Crude Oil Tanker in Port Arthur, Texas — Quintin
> Soloviev) je **CC0**, takže se vypisovat nemusí a je pokrytý poslední
> větou.

---

## Tagy

```
short selling, futures, derivatives, oil price, negative oil price, April 2020,
WTI, commodities, prediction markets, Polymarket, hedging, arbitrage, finance
explained, how markets work, economics explainer
```

---

## Nastavení

| položka | hodnota |
|---|---|
| jazyk videa | **`en-gb`** — nastavit NAPŘED, jinak zůstane dlaždice Titulky zašedlá |
| kategorie | Education |
| viditelnost | nejdřív **neveřejné**, podívat se v přehrávači, teprve pak veřejné |
| pro děti | ne |
| prohlášení o AI | **ne** — viz níž |
| titulky | devět jazyků z `subtitles/` |
| náhled | `render/thumbnail.jpg` |
| playlist | dopsat do `playlisty.json`, pak `analytics.py --videa` a `playlisty.py` |
| závěrečná obrazovka | **ručně ve Studiu** — API na ni nemá ani zdroj |

### Prohlášení o AI: odpověď je NE

Rozhoduje fotorealističnost, ne použití AI:

- SDXL scény (S32, S38, S47) jsou díky kotvě stylu **malované ilustrace**,
  ne fotorealismus
- archivní snímky jsou upravené jen barevně — *„color adjustment or
  lighting filters"* je výslovná výjimka
- hudba je **procedurální** (`tools/music.py`, sinusovky a šum v numpy),
  ne z generativního modelu
- 56 z 64 scén je kresba kódem

### Co zbývá na uživatele

Podle `docs/zverejneni.md` je výchozí cesta **ruční nahrání MP4 ve Studiu
plus `nahraj.py --k-videu <ID>`**. Průvodce ve Studiu se sám zeptá na
prohlášení o AI i na osvědčení o zproštění, takže zbývá:

1. **závěrečná obrazovka** — ručně vždy
2. playlist (po `analytics.py --videa`)
3. `python tools/titulky.py videos/038-can-you-sell-what-you-dont-own --smaz-asr`
   — **adresářem, ne `--vse`**: `--vse` čerstvě nahrané video vůbec nevidí
   a stojí 4 550 jednotek místo 100
