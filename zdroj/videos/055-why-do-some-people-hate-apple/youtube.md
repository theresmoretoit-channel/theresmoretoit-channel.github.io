# Podklady pro YouTube — 055

Formát a pravidla: `docs/zverejneni.md`. **Uživatel kopíruje jen text
mezi trojicí zpětných apostrofů pod každým nadpisem**, takže všechno
povinné (včetně atribucí) musí být uvnitř bloků.

## 1. Titul

```
Why Do Some People Hate Apple?
```

## 2. Popis

```
You paid for your phone. It's yours. And Apple decides what is allowed to run on it.

This isn't a complaint about quality — the hardware is superb. It's a question about who the thing belongs to. We walk through eight concrete cases: the headphone socket, the connector Apple kept for eleven years, parts pairing, the repair kit that arrived as two flight cases, memory you can't change, the App Store commission, and the year millions of phones were quietly slowed down.

And then the part that makes it genuinely hard: the same control that stops you fitting a screen you bought is the reason your headphones connect before you've asked them to. Take one away and you take the other.

Chapters
0:00 You own your phone
0:39 The socket that disappeared
1:56 The part that doesn't fit
3:13 The memory you can't change
3:58 The thirty per cent
4:17 The year the phones slowed down
5:29 Now here's the hard part
6:27 More than a device
7:31 A room, or a cage
8:13 Two people, one computer
8:55 Convenience against control

Subtitles are written for this video, not auto-generated.

IMAGE CREDITS
IPad2 queue, Miami Beach — David Boyle, CC BY 2.0
via Wikimedia Commons
Licences: creativecommons.org/licenses/by/2.0

All other archive images are in the public domain.

Music is generated procedurally for this channel.
```

## 3. Náhled

`render/thumbnail.jpg` — hotový, fotorealistický (dodal uživatel).
Zdroj a rozbor: `thumbnail/PUVOD.md`.

## 4. Titulky

`subtitles/*.srt` — `en`, `en-US` a třináct překladů
(`cs sv es pt-BR de fr it pl id tr uk vi fi`).
Jazyk videa je **`en-gb`** a nastavuje se **první**, jinak zůstane
dlaždice Titulky ve Studiu zašedlá.

## 5. Lokalizované názvy a popisy

`youtube-preklady.md` → `tools/lokalizace.py` (50 jednotek za všech
třináct jazyků naráz).

## 6. Tagy

```
apple, iphone, mac, right to repair, parts pairing, app store, batterygate, headphone jack, lightning connector, apple silicon, walled garden, consumer technology, technology explained, ownership, there's more to it
```

## 7. Nastavení

| co | hodnota | kdo |
|---|---|---|
| jazyk videa | **`en-gb`** — nastavit PRVNÍ | `nahraj.py` |
| byla použita AI | **ne** — SDXL scény jsou malované, archiv jen barevně upraven, hudba procedurální | `nahraj.py` posílá `containsSyntheticMedia: false` |
| osvědčení o zproštění | zaškrtnout | **ručně ve Studiu** |
| závěrečná obrazovka | dlaždice dalšího videa + kolečko odběru | **ručně ve Studiu** — API na to nemá ani zdroj |
| playlist | dopsat slug do `playlisty.json`, pak `analytics.py --videa` a `tools/playlisty.py` | |

## 8. Pořadí nahrávání

Řídí se **cenou**, ne tím, co je po ruce (`docs/zverejneni.md`):

```bash
python tools/nahraj.py videos/055-why-do-some-people-hate-apple --k-videu <ID> --bez-titulku   # 100
python tools/lokalizace.py videos/055-why-do-some-people-hate-apple                            #  50
python tools/titulky.py  videos/055-why-do-some-people-hate-apple                              # 400×15
python tools/titulky.py  videos/055-why-do-some-people-hate-apple --smaz-asr                   # 150
```

Za 150 jednotek je hotové všechno kromě titulků. Titulky stojí 6 000
za patnáct jazyků, takže se do denní kvóty vejdou jen s rezervou —
když dojde, zbytek se dobere druhý den přes `--jen`.
