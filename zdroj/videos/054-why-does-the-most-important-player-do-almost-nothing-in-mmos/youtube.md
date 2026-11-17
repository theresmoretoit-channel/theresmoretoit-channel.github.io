# Podklady k nahrání na YouTube

Časy kapitol **ověřené proti `work/timing.json`**, ne odhadnuté.
První je `00:00`, nejmenší rozestup je 12 s a je jich 25 — YouTube uzná
kapitoly, jen když platí všechny tři podmínky.

| co | odkud |
|---|---|
| video | `render/final-en.mp4` — 1920×1080, **10:37**, 52,7 MB |
| náhled | `render/thumbnail.jpg` — 1280×720, 0,27 MB (dodaný obrázek, viz `thumbnail/PUVOD.md`) |
| titulky | `subtitles/*.srt` — **patnáct stop**: čtrnáct jazyků + `en-US` |
| americká stopa | `render/audio-en-US.m4a` — 15,4 MB, `af_heart` při `speed` 0,9696 |
| lokalizované názvy a popisy | `youtube-preklady.md` přes `tools/lokalizace.py` |

**Atribuce archivního snímku je POVINNÁ** a je proto **uvnitř bloku
„Popis"**, ne pod ním: uživatel kopíruje jen to, co je mezi trojicí
zpětných apostrofů, a u čtyř videí ze šestnácti kredity chyběly přesně
proto, že visely jako poznámka pod blokem.

Video má **dva** archivní snímky. `CREDITS.md` jmenuje oba, ale
povinná je atribuce jen u jednoho:

| scéna | zdroj | licence |
|---|---|---|
| S26 | *Flying across the keyboard* (cogdogblog) | **CC0** — atribuce nepovinná, uvádí se slušností |
| S85 | *2015 Malaysian GP opening lap* (Morio) | **CC BY-SA 4.0** — atribuce POVINNÁ |

---

## Titul

```
Why Can Tanking Be Surprisingly Easy?
```

> **Titul změnil uživatel 2026-09-18 přímo ve Studiu.** Živé znění je
> *Why Can Tanking Be Surprisingly Easy?*; tady i v `youtube-preklady.md`
> je podle něj srovnané, včetně **všech třinácti překladů názvu**, které
> do té doby překládaly původní *Why Does the Most Important Player Do
> Almost Nothing in MMOs?* — třináct jazyků tedy slíbilo jinou otázku než
> angličtina. **Popisy se neměnily**, protože popisují týž obsah.
>
> Němčina dostala navíc upřesnění *im MMO*: scénář používá pro tanking
> slovo `Tanken`, což samostatně v titulku znamená **tankovat palivo**.
>
> Nižší poznámky platí k původnímu názvu:
>
> Wh-otázka schválně (naměřeno na 29 videích, vážené impresemi:
> wh-otázka **2,23 %**, tvrzení 1,63 %, ano/ne otázka 1,21 %).
> Původní název námětu *„THE MOST IMPORTANT PLAYER DOES ALMOST NOTHING"*
> je tvrzení a navíc vyzrazuje pointu.
>
> **„in MMOs" tam není pro délku.** Samotné slovo *tank* čte divák ve
> výpisu i v miniatuře jako vojenské vozidlo, takže by video vypadalo
> na téma, kterým není.

## Popis

```
Join a group in World of Warcraft, Final Fantasy XIV or The Elder Scrolls
Online and you get three jobs to choose from: deal damage, heal, or tank.
And of the three, the tank is usually the one nobody puts their hand up
for — even though everyone agrees it is the important one.

Which is odd, because a lot of the time the job is to walk up to the boss,
press taunt, and stand there. The damage dealers are holding rotations and
tracking buffs. The healer is watching health bars. The tank is blocking,
waiting, and accepting that other people are going to make mistakes that
are not its problem.

Games have noticed how few people want it. World of Warcraft once added
Call to Arms, a bag of extra rewards for whichever role the queue was
short of. Final Fantasy XIV still has its own version, Adventurer in Need.
Whole reward systems, built to talk somebody into a role nobody
volunteered for.

So this is about why a role can be critical without being complicated —
and about what changes when the fight gets hard, when the same job turns
into positioning, interrupts, tank swaps and mechanics nobody else can do.

Subtitles are written for this video, not auto-generated. An American
English audio track is available as a second audio track.

Chapters
00:00 Three roles, and one nobody picks
00:27 The role nobody wants
01:04 What the damage dealers are doing
01:26 What the healer is doing
01:37 And then there is the tank
02:05 An astonishing amount of nothing
02:21 A small piano recital
02:48 Other people will make mistakes
03:15 Not keeping everyone alive
03:34 Whenever you are ready
03:58 Important without being complicated
04:34 Fewer things, bigger consequences
05:01 Games pay people to tank
05:29 So why is it intimidating?
06:01 Reliable, not perfect
06:15 Built to survive
06:36 Glass cannons
06:58 More room for error
07:15 But there is a catch
07:28 Everything a hard fight asks for
07:57 Reacting turns into planning
08:46 You do not start in Formula One
08:57 What tanking gives you
09:38 Important is not the same as busy
10:09 Doing almost nothing

Image credits
"2015 Malaysian GP opening lap" by Morio, CC BY-SA 4.0, via Wikimedia
Commons. "Flying across the keyboard" by cogdogblog, CC0, via Wikimedia
Commons.
```

> **Popis nejmenuje počet jazyků titulků** — rozhodnuto 2026-09-15.
> Dokud tam stálo „nine languages", musel se odstavec při každém
> rozšíření kanálu přepsat, a s překlady je to přes 530 míst.
>
> **Věta o americké stopě tam je, protože ji uživatel potvrdil.** Že
> video druhou stopu má, se z API ani z disku nepozná — `videos.list`
> vrací `audioStreams: 0` i u videí, která ji prokazatelně mají.

## Tagy

```
tanking, mmo, world of warcraft, final fantasy xiv, elder scrolls online,
tank role, mmo roles, damage dealer, healer, raid, dungeon, group content,
game design, why nobody tanks, tank shortage, glass cannon, boss mechanics,
teamwork, responsibility, video game essay
```

## Nastavení

| položka | hodnota |
|---|---|
| kategorie | **Věda a technika** (28) — `nahraj.py` ji má napevno (`KATEGORIE_VEDA`) a z tohohle souboru ji nečte, takže sem nemá smysl psát nic jiného. Gaming (20) by chtěl ruční změnu ve Studiu; celý kanál jede na 28. |
| jazyk videa | **`en-gb` — nastavit PRVNÍ**, jinak zůstane dlaždice Titulky zašedlá |
| titulky | 15 stop ze `subtitles/` |
| náhled | `render/thumbnail.jpg` |
| licence | standardní licence YouTube |
| pro děti | ne |
| **prohlášení o AI** | **ne** — viz níž |
| playlist | řeší uživatel, `playlisty.json` |

### Prohlášení o AI: odpověď je NE

Rozhoduje **fotorealističnost obsahu videa**, ne použití AI
([pravidla](https://support.google.com/youtube/answer/14328491)).
U tohohle videa ji drží tři věci:

- **101 ze 109 scén jsou diagramy kreslené kódem**, ne model
- **5 SDXL scén** jsou inkoustové lavírované kresby (kotva stylu
  `painterly documentary illustration`), ne fotorealismus
- **2 archivní snímky** jsou upravené jen barevně — *„color adjustment
  or lighting filters"* je výslovná výjimka
- hudba je **procedurální** (sinusovky a šum v numpy), ne z modelu

> **Náhled je fotorealistický a vyrobený generativním modelem**, jenže
> otázka YouTube se ptá na obsah videa, ne na miniaturu. Zapsáno
> v `thumbnail/PUVOD.md`, ať se to nemusí dohledávat.

## Co musí uživatel naklikat sám

Podle toho, jak se video založí:

| | ruční MP4 + `--k-videu` | `videos.insert` |
|---|---|---|
| prohlášení o AI | ✅ vyřídí průvodce | ❌ **ručně** |
| osvědčení o zproštění | ✅ vyřídí průvodce | ❌ **ručně** |
| **závěrečná obrazovka** | ❌ **ručně** | ❌ **ručně** |
| **americká audiostopa** | ❌ **ručně ve Studiu** | ❌ **ručně** |

Data API na závěrečnou obrazovku nemá ani zdroj, na audiostopu taky ne.

**Místo na závěrečnou obrazovku je ověřené** (`zaver_check.py`): scény
S100–S103, prvky se vejdou **vlevo nahoře** s překryvem 0,0 az 0,2 %.
Dole to nejde, tam sedí ambrový nadpis na 82,6 % výšky.

## Po nahrání

```bash
python tools/nahraj.py videos/054-... --k-videu <ID>
python tools/lokalizace.py videos/054-... --zkouska
python tools/lokalizace.py videos/054-...
python tools/titulky.py --vse --smaz-asr
python tools/analytics.py --videa
python tools/playlisty.py
```

> **Pořadí je závazné.** Dokud neproběhne `nahraj.py --k-videu`, visí
> video s titulem podle názvu souboru a `analytics.py --videa` ho
> nespáruje se slugem, protože páruje podle titulu.
>
> **Automatický přepis se maže** (`--smaz-asr`) — konkuruje čtrnácti
> překladům a je z nich nejhorší. Smazání ho jen odstraní, nezakáže,
> takže po nahrání se to pouští znovu.
