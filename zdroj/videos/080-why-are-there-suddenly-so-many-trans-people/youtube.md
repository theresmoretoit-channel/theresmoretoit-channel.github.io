# YouTube — 080 „Why Are There Suddenly So Many Trans People?"

Stav: **nahráno 2026-10-21** — https://www.youtube.com/watch?v=B0EZzde1TZ8

| | |
|---|---|
| ID videa | `B0EZzde1TZ8` (MP4 nahrál uživatel ve Studiu) |
| nastavení, popis, tagy | ✅ `nahraj.py --k-videu --bez-titulku` |
| náhled | ✅ C1 (`TRANS` / `WHY NOW?`), `thumbnail/PUVOD.md` |
| lokalizace | ✅ 13 jazyků po Codexu |
| automatický přepis | ✅ nebyl (`--smaz-asr`: už čisto) |
| titulky | ✅ 15 stop (14 jazyků + `en-US`) |
| playlist | ✅ `spolecnost`, `bezne` (pozice 18) |
| závěrečná obrazovka, americká stopa, zveřejnění | ✅ naklikáno a naplánováno uživatelem (2026-10-21) |
| úklid | ✅ `render/draft-en.mp4` a kopie na .207 smazány |

**Co musí uživatel naklikat sám:** nahrát MP4 ve Studiu (průvodce vyřídí
prohlášení o AI a osvědčení o zproštění), závěrečnou obrazovku a americkou
audiostopu (`render/audio-en-US.m4a`).

Soubor k nahrání: `render/final-en-080.mp4` (stopáž 12:24, `work/timing.json`
total 744,3 s — po přidání S85).

Pořadí podle CENY (`docs/zverejneni.md`):

```bash
V=videos/080-why-are-there-suddenly-so-many-trans-people
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
Why Are There Suddenly So Many Trans People?
```

> wh-otázka („Why…"), 44 znaků. Rozhodl uživatel u v0.1 (`notes.md`).
> Odpověď neprozrazuje — video ji nechává otevřenou (S61: čísla samy
> neřeknou, kolik z rozdílu je viditelnost).

---

## 2. Popis

```
Have you ever met a transgender person? Maybe you have, and never knew. Over the last few years, it can seem as if trans people have suddenly appeared everywhere. So why does it look as though there are so many more of them?

This video starts with the basics: what transgender actually means, why gender identity and sexual orientation are different things, and what gender dysphoria can feel like. It looks at what transition is, why it isn't one particular operation, and whether being transgender is simply a fashion.

Then it turns to the numbers. Researchers estimate that in the United States, about one in a hundred people aged thirteen and over describe themselves as transgender. Among young adults aged eighteen to twenty-four, the share is roughly ten times higher than among people aged sixty-five and over. What can those numbers tell us, and what can't they?

Finally, it goes back almost a hundred years, to Magnus Hirschfeld's institute in Berlin, the Danish painter Lili Elbe, and what happened to the institute in May 1933.

This is the first video in a series about transgender people. The next one asks: how do you know you're trans?

Subtitles are written for this video, not auto-generated. An American English audio track is available as a second audio track.

CHAPTERS
00:00 Have you ever met a trans person?
00:43 What does transgender actually mean?
02:09 What does it feel like?
04:10 There isn't one kind of transgender person
04:52 What is transition?
06:18 Is being transgender a fashion?
07:21 Human biology isn't a standard system
08:04 Are there really more trans people now?
09:19 Were trans people around in the past?
10:51 Why do we notice them so much now?
11:18 Maybe the real change isn't in the people
11:45 Next: how do you know you're trans?

DATA
Herman, J. L. & Flores, A. R. (2025). How Many Adults and Youth Identify as Transgender in the United States? Williams Institute, UCLA.

IMAGE CREDITS
Lili Elbe, Copenhagen, 1930 — unknown photographer, Wellcome Collection, CC BY 4.0, via Wikimedia Commons
All other archive images are in the public domain.
Licence: creativecommons.org/licenses/by/4.0
```

> **Blok se kopíruje CELÝ** (`docs/zverejneni.md`) — atribuce je UVNITŘ.
> Povinná je jen u S66 (Lili Elbe, CC BY 4.0). `sources.json` má v poli
> `credit` jen „Unknown authorUnknown author" (zdvojené z Commons), takže
> strojová kontrola autora proti popisu **nesedne** — ověřeno ručně na
> stránce souboru (Commons API, `extmetadata`): autor neznámý, pole Credit
> odkazuje na Wellcome Images L0031868, popis *„from N. Hoyer, ed., Man
> into Woman… London: Jarrolds, 1933. Photograph: Lili Elbe, Copenhagen,
> 1930"*. Zbylé čtyři (S64, S65, S68, S69) jsou public domain.
>
> **DATA** je v popisu navíc proti běžnému vzoru kanálu: u tématu, kde se
> bude v komentářích přít o čísla, je zdroj čísel nejlepší první odpověď.
> Číslo a srovnání drží znění scénáře (S54–S56, souhrnná čísla WI 2025:
> 2,72 % vs 0,26 % → 10,5×), včetně „describe themselves" a „aged sixty-five
> and over". Nebinární lidi popis nezmiňuje; scénář ano (S54).
>
> Kapitoly jsou ze scén S01, S07, S15, S29, S34, S45, S51b, S53, S63, S73,
> S77, S80 (`work/timing.json`, celkem 744,3 s, časy zaokrouhlené dolů);
> mluvené nadpisy sekcí scénáře jsou zároveň kapitolami. Nejkratší
> kapitola je 26,8 s (S73–S77), všechny ≥ 10 s. **Po každém dalším běhu
> `tts.py` časy přepočítej** — a stejně tak v `youtube-preklady.md`.
>
> Popis drží míru jistoty scénáře: „it can seem as if", „researchers
> estimate", otázka „what can't they?" místo závěru. Že by šlo jen
> o viditelnost, popis netvrdí — netvrdí to ani video (S61).

---

## 3. Náhled

**Koncepty C1–C3 v `thumbnail/KONCEPTY.md`** (doporučen C1: dav stejných
bílých figurek, jedna svítí ambrově, `TRANS` / `WHY NOW?`). Po dodání
obrázku: `render/thumbnail.jpg`, `thumbnail/PUVOD.md`, `thumb_check.py`.
`nahraj.py --k-videu` náhled nepotřebuje, jde dodat i později.

> U tohohle tématu pozor na pravidlo „náhled se ptá, neodpovídá" i na
> kotvu stylu videa: **žádné tváře, žádná vlajka ani duha, žádný stereotyp**.
> Páteř videa je dav sta stejných postav (`dav()`) — jedna rozsvícená
> postava v davu je kandidát, který nic neprozradí.

---

## 4. Titulky

`subtitles/*.srt`, 14 jazyků + `en-US`. Jazyk videa **`en-gb`** (hlas
`bf_emma`) se musí nastavit dřív, než se nahrají titulkové stopy, jinak
zůstane dlaždice Titulky zašedlá. **Nahrávat až po Codexu** na všech
jazycích.

---

## 5. Nastavení

| | |
|---|---|
| kategorie | Education |
| jazyk videa | `en-gb` |
| licence | standardní |
| pro děti | **ne** |
| komentáře | zapnuté — **téma je konfliktní, počítej s moderací** |
| **byla použita AI** | **ne** — 79 scén kreslených kódem (z 93, včetně beatů dědících obraz), 9 SDXL scén v malované kotvě stylu (lidé malí, zezadu, bez tváří — ne fotorealismus), 5 archivních fotek jen barevně upravených a vsazených do rámu, hudba procedurální, hlas není klon skutečné osoby |

### Závěrečná obrazovka

`zaver_check.py`: S82–S85 (od 719,9 s, posledních 20 s) mají **horní
polovinu volnou** (kresba pod 1 %) — dlaždici i kolečko odběru dej do
**horní** poloviny, dole je titulek. Jako dlaždici dalšího videa dej
**081**, až bude venku (S85 ohlašuje jeho titul).

---

## 6. Tagy

```
transgender, trans people, gender identity, gender dysphoria,
transition, non-binary, cisgender, sexual orientation,
Magnus Hirschfeld, Lili Elbe, Institut für Sexualwissenschaft,
Williams Institute, LGBT history, explainer, there's more to it
```

---

## 7. Playlist

**Rozhodnuto 2026-10-21: tamtéž jako 064 a 072** — `spolecnost`
(„How Society Actually Runs") a `bezne` („Ordinary Things, Awkward
Questions"), v `playlisty.json` hned za 072. Po zveřejnění
`analytics.py --videa` a `playlisty.py`.

Odloženo:

- **playlist série 080–084** — série se dívá po dílech a S85
  na další díl přímo odkazuje; playlist by nesl pořadí. Stojí 50 jednotek
  navíc za založení. Dává smysl až s 081 venku.

---

## Kontrola atribucí (2026-10-21)

Jediná položka `sources.json` s licencí `CC BY*` je S66. Pole `credit`
je „Unknown authorUnknown author", takže strojové porovnání neprojde;
ručně: v bloku je „unknown photographer, Wellcome Collection, CC BY 4.0"
a adresa licence. 1/1.
