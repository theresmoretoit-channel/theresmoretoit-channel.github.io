# YouTube — 117 „What Would It Take for Russia to Change?“

Stav: **nahráno 2026-10-19 (`lhBhRSvGwvw`), zveřejnění naplánované**. Agent nahrál nastavení, popis, tagy, náhled, lokalizace (13 jazyků) a titulky `en` (en-GB) a `en-US`, automatický přepis smazal. Zbylé titulky, americkou stopu, karty a závěrečnou obrazovku dělá uživatel ručně ve Studiu. Stav zveřejnění je v `Témata.fods`.

| | |
|---|---|
| ID videa | `lhBhRSvGwvw` (MP4 nahrál uživatel 2026-10-19) |
| master | ✅ `render/final-en-117.mp4` (8:41, 1920×1080, 48 MB, hudba jen v šesti úsecích a o 1,6 dB tišší, render 2026-10-19 na .207 za 430 s, `ffmpeg -v error` čistý) |
| náhled | ✅ `render/thumbnail.jpg` (1280×720, 0,32 MB), RUSSIA / WHAT WOULD IT TAKE?, koncept A, původ v `thumbnail/PUVOD.md` |
| nastavení, popis, tagy | podklady níž |
| lokalizace | `youtube-preklady.md`, 13 jazyků |
| titulky | `subtitles/*.srt`, 14 jazyků + `en-US` |
| americká stopa | `render/audio-en-US.m4a`, ručně ve Studiu |
| závěrečná obrazovka | ručně ve Studiu |
| karty | 116 v 0:47, 050 v 3:19 (viz níž) |
| playlist | `spolecnost`, na konec, za 116 |

**Co musí uživatel naklikat sám:** nahrát MP4 ve Studiu (průvodce vyřídí
prohlášení o AI a osvědčení o zproštění), závěrečnou obrazovku, obě karty
a americkou audiostopu (`render/audio-en-US.m4a`).

Stopáž 8:41 (`work/timing.json` total 521,3 s).

> Kdyby se znovu pouštěl `tts.py`, přepočítej kapitoly tady
> i v `youtube-preklady.md` a přegeneruj `en-US` přes `us_stopa.py`.

> Odkaz na 116 v popisu (`BC9fxi97ARQ`) je doplněný 2026-10-19 a v lokalizacích jsou tituly 116 z `116/youtube-preklady.md`.

Pořadí podle CENY (`docs/zverejneni.md`):

```bash
V=videos/117-what-would-it-take-for-russia-to-change
python tools/nahraj.py $V --k-videu=<ID> --bez-titulku    # 100
python tools/analytics.py --videa                         #   1  ← nutné
python tools/lokalizace.py $V                             #  50
python tools/titulky.py $V --smaz-asr                     # 150  ← před titulky
python tools/titulky.py $V                                # 400×15
python tools/playlisty.py                                 #  50
# úklid, až je MP4 na YouTube:
rm $V/render/draft*.mp4
ssh vrana@192.168.0.207 'rm -rf /home/vrana/temp/render-117-what-would-it-take-for-russia-to-change'
```

---

## 1. Titul

```
What Would It Take for Russia to Change?
```

> Wh-otázka, 40 znaků, shodná s `project.json`. Odpověď (ne lepší muž
> nahoře, ale systém, který na žádném muži nezávisí) titul neprozrazuje.

---

## 2. Popis

```
In May 2008, Russia got a new president. He was forty-two, a lawyer, and he had just told an economic forum in Siberia that freedom is better than unfreedom. Three months after he took office, Russian troops were fighting in Georgia. In 2011, he announced he would step aside so that the man he had replaced could return.

Russia has tried changing the face at the top. So what would it actually take for the system itself to change, and how long would it take? This video looks at four conditions, from courts and elections to oil money, borders and the people who leave, and at the one thing nobody can predict: when change starts, and which way it goes.

Previous video: Why Does Russia Keep Choosing Confrontation? https://www.youtube.com/watch?v=BC9fxi97ARQ
Related: How Does a Dictatorship Become a Democracy? https://www.youtube.com/watch?v=Ax7VZG6Je-c

Sources: Constitution of the Russian Federation (1993, amended 2020); Judicial Department of the Supreme Court of Russia, court statistics (2023); OVD-Info (2025); Freedom House, Freedom in the World 2025: Russia; S. E. Hanson, PONARS Policy Memo 285 (2002); J. L. Weeks, Dictators at War and Peace (2014); Norges Bank Investment Management, half-year report (2026); Norwegian Petroleum (norskpetroleum.no), the fiscal rule; Budapest Memorandum on Security Assurances (1994); Treaty of Friendship, Cooperation and Partnership between Ukraine and the Russian Federation (1997); Treaty of Warsaw (1970); German–Polish Border Treaty (1990); Statistics Poland (GUS), foreign trade 2025; The Bell (2024); OutRush; Memorial, list of political prisoners (2026); Levada Center (December 2018); A. Amalrik, Will the Soviet Union Survive Until 1984? (1969).

Subtitles are written for this video, not auto-generated. An American English audio track is available as a second audio track.

Full transcript, sources and translations: https://theresmoretoit-channel.github.io/videos/what-would-it-take-for-russia-to-change/

CHAPTERS
00:00 A new president in 2008
00:47 Where we left off
01:18 Waiting for a new leader
01:59 Change from above
02:35 Condition one: power that can lose
03:40 Condition two: money
04:24 Condition three: borders
05:25 Condition four: people
05:46 How long would it take?
06:58 What nobody can predict
07:33 A question from 1969
07:54 A prisoner of its history?

IMAGE CREDITS
White House, Moscow, October 1993 (ベールイドーム) — Bergmann at Japanese Wikipedia, CC BY 3.0
Frankfurt (Oder) – Słubice — Sebastian Wallroth, CC BY 3.0
Monument to the Ghetto Heroes, Warsaw — Simon Burchell, CC BY-SA 4.0
via Wikimedia Commons
Licences: creativecommons.org/licenses/by/3.0, creativecommons.org/licenses/by-sa/4.0
```

> **Blok se kopíruje CELÝ** (`docs/zverejneni.md`). Archivní snímky jsou
> tři (S13, S39, S55) a všechny mají povinnou atribuci (`sources.json`).
> Public domain snímek tu není, takže věta „All other archive images…“
> chybí záměrně.
>
> **Pointa se neprozrazuje.** Popis končí tím, co předpovědět nejde.
> Že rozhoduje systém, a ne muž nahoře (S72), a že minulost nerozhodne
> (S74–S75), je výplata. Kapitola *„A prisoner of its history?“* je otázka
> z S68, ne odpověď.
>
> Kapitoly ze scén S01, S08, S11, S17, S21, S29, S35, S43, S46, S58, S64,
> S68 (`work/timing.json`, zaokrouhleno dolů). Nejkratší 21 s (S43 → S46
> a S64 → S68), všechny ≥ 10 s, první na 00:00. Výzva k odběru S10b (1:10)
> leží v kapitole „Where we left off“.
>
> Čísla a data v popisu (květen 2008, 42 let, tři měsíce, 2011) jsou tatáž
> jako ve scénáři a ve `factcheck.md` (S01–S05). Zdroje podle `factcheck.md`.
> Zprávy (Reuters, Meduza, Moscow Times) se necitují, citují se primární
> prameny. Laqueur se necituje, protože je ověřený jen z druhé ruky.

---

## 3. Náhled

`render/thumbnail.jpg`: pootevřené železné dveře se světlem ve škvíře,
RUSSIA / WHAT WOULD IT TAKE?. Koncept A ze `ZADANI.md`, obrázek z ChatGPT.
Původ, otisk a thumb_check jsou v `thumbnail/PUVOD.md`.

---

## 4. Titulky

`subtitles/*.srt`, 14 jazyků + `en-US`. Jazyk videa **`en-gb`** (hlas
`bf_emma`) se musí nastavit dřív, než se nahrají titulkové stopy.
Všechny překlady prošly Codexem (nálezy v `notes.md`).

---

## 5. Nastavení

| | |
|---|---|
| kategorie | **Science & Technology** (28) — posílá `nahraj.py` napevno |
| jazyk videa | `en-gb` |
| licence | standardní |
| pro děti | **ne** |
| komentáře | zapnuté |
| **byla použita AI** | **ne**. 71 scén je kreslených kódem, 3 archivní snímky jsou jen barevně upravené. SDXL je ve dvou scénách (S63 sovětská ulice v zimě, S68 silnice mezi břízami): obě jsou malované ilustrace a **generická místa**, ne skutečné místo ani událost. Hudba je procedurální, hlas není klon. Tváře politiků se nekreslí. |

### Závěrečná obrazovka

Od **8:21** (posledních 20 s), tedy S72–S75. `zaver_check` prošel a oba
horní rohy jsou volné. Jako dlaždici dalšího videa doporučuju **116 *Why
Does Russia Keep Choosing Confrontation?*** (první díl dvojice), druhou
dlaždici nechat na „nejlepší pro diváka“.

### Karty

- **116 v 0:47** (S08 *„In the last video, we looked at why Russia keeps
  choosing confrontation“*).
- **050 v 3:19** (S26b *„How they got there is the subject of an earlier
  video.“*). Scéna vznikla právě kvůli odkazu na 050.

---

## 6. Tagy

```
russia, russian politics, putin, medvedev, yeltsin, 1993 constitution,
rule of law, russian courts, elections, transfer of power, oil fund, norway,
budapest memorandum, ukraine borders, brandt, poland germany border,
brain drain, amalrik, soviet union, geopolitics explainer, there's more to it
```

---

## 7. Playlist

`spolecnost` (*How Society Actually Runs*), na konec, za 116. Zapsáno
v `playlisty.json`. `playlisty.py` ho přeskočí, dokud video není
v `analytics/videa.json`.
