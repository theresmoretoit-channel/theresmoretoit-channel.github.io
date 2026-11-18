# YouTube — 124 „Why Does a New Disk Need Formatting?“

Stav: **MP4 nahráno ručně ve Studiu 2026-10-26.** Stav zveřejnění je v `Témata.fods`.

| | |
|---|---|
| ID videa | `z9sJkpM0NoI` |
| master | ✅ `render/final-en-124.mp4` (9:31, 1920×1080, 570,60 s) |
| náhled | ✅ `render/thumbnail.jpg` (koncept A, otevřený disk) |
| nastavení, popis, tagy | podklady níž |
| lokalizace | `youtube-preklady.md`, 13 jazyků |
| titulky | `subtitles/*.srt`, 14 jazyků + `en-US` (Codex hotový) |
| americká stopa | `render/audio-en-US.m4a`, ručně ve Studiu |
| závěrečná obrazovka | od **9:10**, S57–S59, prvky **nahoru** (viz níž) |
| karta | žádná (scénář na starší video neodkazuje) |
| playlist | `pocitace` (*Inside Your Computer*), na konec |

**Co musí uživatel naklikat sám:** závěrečnou obrazovku, americkou
audiostopu (`render/audio-en-US.m4a`) a osvědčení o zproštění, pokud ho
nevyřídil průvodce nahráním.

Stopáž 9:31 (`work/timing.json` total 570,55 s).

> Kdyby se znovu pouštěl `tts.py`, přepočítej kapitoly tady
> i v `youtube-preklady.md` a přegeneruj `en-US` přes `us_stopa.py`.

Pořadí podle CENY (`docs/zverejneni.md`):

```bash
V=videos/124-why-does-a-new-disk-need-formatting
python tools/nahraj.py $V --k-videu=z9sJkpM0NoI --bez-titulku   # 100
python tools/analytics.py --videa                               #   1  ← nutné
python tools/lokalizace.py $V                                   #  50
python tools/titulky.py $V --smaz-asr                           # 150  ← před titulky
python tools/titulky.py $V                                      # 400×15
python tools/playlisty.py                                       #  50
# úklid, až je MP4 na YouTube:
rm $V/render/draft*.mp4
ssh vrana@192.168.0.207 'rm -rf /home/vrana/temp/render-124-why-does-a-new-disk-need-formatting'
```

---

## 1. Titul

```
Why Does a New Disk Need Formatting?
```

> Wh-otázka, 36 znaků, shodná s `project.json` a `Témata.fods`. Odpověď
> titul neprozrazuje.

---

## 2. Popis

```
You buy a brand-new one terabyte drive and format it with ext4, the standard filesystem on many Linux computers. Before you've saved a single file, about seventeen gigabytes are gone. Nothing has been stored yet. So what's taking up all that space? And why does a drive need formatting in the first place?

This video builds the answer from the bottom up: what a drive actually offers a computer, what formatting adds on top of it, and what happens on the disk when you save one tiny file called hello.txt, when you delete it, and when the power cuts out halfway through saving.

Along the way: a notebook with a thousand pages, why a five-byte file takes up 4,096 bytes, why moving a huge file can be instant, why a deleted file can sometimes be recovered (and why that's less likely on an SSD), what a journal is for, and how ext4, NTFS and Btrfs make different choices about the same job.

The numbers come from formatting a 1 TB disk image with ext4 at its default settings (mke2fs 1.47.3). Other Linux distributions can use different defaults and get a slightly different figure.

Sources: Linux kernel documentation, ext4 Data Structures and Algorithms and the ext4 admin guide; e2fsprogs (mke2fs, dumpe2fs, debugfs); btrfs-progs documentation; Bairavasundaram et al. (2008), An Analysis of Data Corruption in the Storage Stack, USENIX FAST.

Subtitles are written for this video, not auto-generated. An American English audio track is available as a second audio track.

Full transcript, sources and translations: https://theresmoretoit-channel.github.io/videos/why-does-a-new-disk-need-formatting/

CHAPTERS
00:00 An empty disk that isn't
00:48 A pile of paper and a notebook
02:14 What's actually on the drive
03:10 Where did 17 GB go?
04:25 Saving hello.txt
05:01 Where the name lives
06:14 Deleting a file
07:09 Cut the power
07:51 Damage nobody reports
08:22 Same job, different choices
09:17 What's next
```

> **Blok se kopíruje CELÝ** (`docs/zverejneni.md`). **Archivní snímky
> video nemá** (58 diagramů kreslených kódem + 1 SDXL scéna, žádné
> `sources.json` ani `CREDITS.md`), takže `IMAGE CREDITS` tu není.
> Náhled je obrázek z ChatGPT bez cizí fotky a atribuci nepotřebuje.
>
> **Pointa se neprozrazuje.** Popis položí otázku ze S02–S05 a neříká,
> kam 17 GB zmizelo (inody, S24–S28). Kapitola *Where did 17 GB go?*
> je otázka, ne odpověď.
>
> **Nic netvrdí víc než video** (`factcheck.md`): „many Linux computers“
> (S02), „about seventeen gigabytes“ s výhradou výchozího nastavení
> (naměřeno 16,85 GB, `mereni-mkfs.txt`), 4,096 (S37), obnova „sometimes“
> a na SSD „less likely“ (S43–S44). Věta o jiných distribucích odpovídá
> výhradě ve fact checku k S02.
>
> Kapitoly ze scén S01, S07, S17, S23, S30, S34, S41, S46, S50, S53, S58
> (`work/timing.json`, zaokrouhleno dolů). Nejkratší má 13 s (S58 → konec),
> první začíná na 00:00 a všechny mají ≥ 10 s. Výzvy k odběru (za S16
> a S45) leží uvnitř kapitol.
>
> Zdroje odpovídají `factcheck.md`. NTFS (S54) tam konkrétní zdroj nemá,
> proto v řádku zdrojů není.

---

## 3. Náhled

`render/thumbnail.jpg` je koncept A (otevřený disk, EMPTY DISK / WHERE
DID 17 GB GO?), obrázek z ChatGPT, původ v `thumbnail/PUVOD.md`. Záloha
pro Test & Compare: koncept B (`thumbnail/ZADANI.md`).

---

## 4. Titulky

`subtitles/*.srt`, 14 jazyků + `en-US`. Jazyk videa **`en-gb`** (hlas
`bf_emma`) se musí nastavit dřív, než se nahrají titulkové stopy.
Codex proběhl (`notes.md`).

---

## 5. Nastavení

| | |
|---|---|
| kategorie | **Science & Technology** (28), posílá `nahraj.py` napevno |
| jazyk videa | `en-gb` |
| licence | standardní |
| pro děti | **ne** |
| komentáře | zapnuté (S59 končí otázkou do komentářů) |
| **byla použita AI** | **ne**. 58 scén je kreslených kódem; jediná SDXL scéna (S07, kancelář zavalená volnými listy papíru) je malovaná ilustrace podle kotvy stylu, ne fotorealismus ani konkrétní skutečné místo či událost. Archiv žádný, hudba procedurální, hlas není klon. |

### Závěrečná obrazovka

Od **9:10** (posledních 20 s z 570,6), tedy S57 (od 542,6 s), S58 a S59.
`zaver_check` u všech tří hlásí volnou **horní polovinu** (dole je
titulek), **dlaždici i kolečko odběru dej nahoru**. Jako dlaždici
doporučuju **121 *How Did a Music Cassette Store a Computer Game?***
(`YmUJgDi4vR0`): taky jde o to, jak se data fyzicky ukládají. Druhou
dlaždici nech na „nejlepší pro diváka“; díl o Btrfs (S58) zatím není.

---

## 6. Tagy

```
why does a new disk need formatting, what is formatting, filesystem explained,
ext4, inode, ntfs, btrfs, how file systems work, deleted file recovery,
journaling file system, ssd trim, hard drive, linux, data corruption,
explainer, there's more to it
```

---

## 7. Playlist

**`pocitace`** (*Inside Your Computer — Why It Behaves the Way It Does*),
na konec za 121. Alternativa `legacy` nesedí, filesystémy nejsou starý
systém, který přežívá.
