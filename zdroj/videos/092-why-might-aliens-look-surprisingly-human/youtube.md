# YouTube — 092 „Why Might Aliens Look Surprisingly Human?"

Stav: **nahráno a naplánované ke zveřejnění** (https://youtu.be/vGx-f9f39FI); titulky, US stopu, závěrečnou obrazovku a playlist dodělal uživatel ve Studiu (2026-10-07).

| | |
|---|---|
| ID videa | `vGx-f9f39FI` |
| nastavení, popis, tagy | ✅ `nahraj.py --k-videu --bez-titulku` |
| náhled | ✅ C1 (`thumbnail/c1-why-a-crab.svg`) → `render/thumbnail.jpg` |
| lokalizace | ✅ 13 jazyků (`lokalizace.py`) |
| automatický přepis | ⬜ |
| titulky | 🟡 `en` a `en-US` nahrané; zbylých 13 jazyků ručně (kvóta) |
| playlist | ⬜ návrh `vesmir` |
| závěrečná obrazovka, americká stopa | ⬜ uživatel ve Studiu |

**Co musí uživatel naklikat sám:** nahrát MP4 ve Studiu (průvodce vyřídí
prohlášení o AI a osvědčení o zproštění), závěrečnou obrazovku a americkou
audiostopu (`render/audio-en-US.m4a`).

Soubor k nahrání: `render/final-en-092.mp4` (stopáž 8:18, `work/timing.json`
total 498,2 s).

Pořadí podle CENY (`docs/zverejneni.md`):

```bash
V=videos/092-why-might-aliens-look-surprisingly-human
python tools/nahraj.py $V --k-videu=<ID> --bez-titulku    # 100
python tools/analytics.py --videa                         #   1  ← nutné
python tools/lokalizace.py $V                             #  50
python tools/titulky.py $V --smaz-asr                     # 150  ← před titulky
python tools/titulky.py $V                                # 400×15
python tools/playlisty.py                                 #  50
```

---

## 1. Titul

```
Why Might Aliens Look Surprisingly Human?
```

> Wh-otázka, 41 znaků, totožná s nadpisem `script.md`. Neprozrazuje
> pointu (výběrový efekt S42–S51 a „lidské v architektuře, ne ve vzhledu"
> S76).

---

## 2. Popis

```
Crabs have evolved at least five separate times. Eyes, more than forty. A shark, an ichthyosaur and a dolphin ended up with the same shape, although one is a fish, one a reptile and one a mammal. Evolution keeps finding the same answers to the same problems.

So if there is life on another planet, would it keep finding them too? And would an intelligent alien end up looking strangely familiar, or nothing like us at all?

Subtitles are written for this video, not auto-generated. An American English audio track is available as a second audio track.

CHAPTERS
00:00 Nature keeps making crabs
00:36 Eyes, wings and swimmers
01:16 Two skulls
01:46 What about aliens?
02:02 Why animals have a head
02:50 Brains are not enough
03:48 The octopus problem
04:18 Who we would actually meet
05:18 Eyes, and then a face
06:13 The dinosauroid
06:49 Rewinding the tape of life
07:08 Both might be right
07:41 A surprisingly small toolbox

IMAGE CREDITS
Octopus Eye — incidencematrix, CC BY 2.0
Canis lupus skull side — Eric Polk, CC BY-SA 4.0
Thylacinus cynocephalus skull, Royal Tyrrell Museum — Chris Woodrich, CC BY-SA 4.0
Atlantic bottlenose dolphin jumping at Pelican Point — Giles Laurent, CC BY-SA 4.0
Corvus moneduloides eating on branch — MD sajjad hossain photography, CC BY-SA 4.0
Troodon or Stenonychosaurus (update) — Conty, CC BY-SA 4.0
Dinosauroid drawing — HannahMoss, CC BY-SA 4.0
via Wikimedia Commons
All other archive images are in the public domain.
Licences: creativecommons.org/licenses/by-sa/4.0, creativecommons.org/licenses/by/2.0
```

> **Blok se kopíruje CELÝ** (`docs/zverejneni.md`) — atribuce je UVNITŘ.
> Povinná je u sedmi položek ze `sources.json` s licencí CC BY*: S07, S13,
> S13b, S29, S31, S64, S65. Bez povinné atribuce (PD): S14 (*Thylacinus
> at Hobart Zoo 1928*, Harry Burrell) a S38 (*Octopus vulgaris*,
> Merculiano), pokrývá je věta o public domain.
>
> Kapitoly jsou ze scén S01, S07, S13, S17, S20, S28, S37, S42, S52, S62,
> S68, S71, S77 (`work/timing.json`, časy zaokrouhlené dolů). Nejkratší
> kapitola je 16 s (S17 → S20), všechny ≥ 10 s,
> první na 00:00. **Po každém dalším běhu `tts.py` časy přepočítej** —
> a stejně tak v `youtube-preklady.md`.
>
> Scéna s výzvou k odběru je **S16b** (1:39) uvnitř kapitoly „Two skulls";
> žádnou kapitolu neposouvá.
>
> Popis neprozrazuje pointu: výběrový efekt (S42–S51) ani závěr S76 v něm
> nejsou, druhý odstavec jen klade otázku. Čísla v prvním odstavci (krab
> ≥ 5×, oči > 40×, tři plavci) jsou ověřená ve `factcheck.md`.

---

## 3. Náhled

✅ **C1** (`thumbnail/c1-why-a-crab.svg`, kresleno kódem `thumbnail/gen.py`)
→ `render/thumbnail.jpg`, `ALIENS / WHY A CRAB?` nad ambrovým krabem
z S01 (`_kit.krab()`). Bez archivní předlohy, takže bez atribuce.
Ostatní koncepty v `thumbnail/KONCEPTY.md`.

---

## 4. Titulky

`subtitles/*.srt`, 14 jazyků + `en-US`. Jazyk videa **`en-gb`** (hlas
`bf_emma`) se musí nastavit dřív, než se nahrají titulkové stopy.
Codex proběhl na všech 13 překladech včetně `cs` a nálezy jsou zapracované
(commit `9480f394`).

---

## 5. Nastavení

| | |
|---|---|
| kategorie | Science & Technology |
| jazyk videa | `en-gb` |
| licence | standardní |
| pro děti | **ne** |
| komentáře | zapnuté |
| **byla použita AI** | **ne** (návrh, rozhoduje uživatel). Většina scén kreslená kódem, 9 archivních snímků jen barevně upravených (*color adjustment* je výslovná výjimka), 2 SDXL scény (S44, S47) díky kotvě stylu jako malované ilustrace, ne fotorealismus, a nezobrazují skutečné místo ani událost. Hudba procedurální, hlas není klon |

### Závěrečná obrazovka

`zaver_check.py`: S80–S83 mají kresbu do 1,8 % plochy, dlaždice i kolečko
odběru se vejdou kamkoli kromě spodních rohů (titulek). Dej je do **horní
poloviny**. Dlaždice: **091** (*How Could Aliens Actually Look?*), sesterské
video s opačnou otázkou, na které S17 odkazuje („In another video…").

---

## 6. Tagy

```
aliens, what would aliens look like, convergent evolution, carcinisation,
alien life, extraterrestrial life, astrobiology, evolution, octopus eye,
thylacine, dinosauroid, dale russell, stephen jay gould,
simon conway morris, intelligent life, science explainer, there's more to it
```

---

## 7. Playlist

Navrženo **`vesmir`** (*Space — Getting There, and Who Else Is Out
There*), hned vedle sesterského **091**. Dopiš slug do `playlisty.json`,
spusť `analytics.py --videa` a pak `tools/playlisty.py`.
