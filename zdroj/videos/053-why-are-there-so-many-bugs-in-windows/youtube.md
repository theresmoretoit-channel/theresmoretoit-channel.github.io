# Podklady k nahrání na YouTube

**Nahrává se** `render/final-en.mp4` (master, ne draft), `render/thumbnail.jpg`
a `subtitles/*.srt`.

> **Uživatel kopíruje jen text mezi trojicí zpětných apostrofů** pod nadpisem
> „Popis" a nic jiného — proto v tom bloku není žádná česká poznámka.
> Atribuce k obrázkům by musela být uvnitř toho bloku; tohle video ji
> nepotřebuje, protože **nemá jedinou archivní scénu** (snímky rozhraní
> Windows nejsou pod volnou licencí, viz `notes.md`).

---

## Titul

```
Why Are There So Many Bugs in Windows?
```

> Wh-otázka schválně. Naměřeno na kanálu (29 videí, vážené impresemi):
> wh-otázka **2,23 %**, tvrzení 1,63 %, ano/ne otázka 1,21 %.
>
> Vlastní titul zdrojového textu byl *„What the Hell Is Their QA Doing?"* —
> sprosté slovo a není to wh-otázka v tom užitečném smyslu, takže zůstal
> **uvnitř videa jako hláška**, ne na miniatuře.

## Popis

```
In September 2026, a single batch of Windows updates broke audio, Remote
Desktop, shared folders in virtual machines, and the ability of some
machines to log in to their own company network. One batch. One Tuesday.

If that sounds like just another bad Windows update, it isn't. Microsoft
publishes its own list of what each update broke, and a single year of
that list repeats the same pattern month after month. Twice in three
months an update broke the tool you use to repair a broken computer. One
audio bug turned up in January, and again twenty months later, with the
same symptom and the same message.

So the obvious conclusion is that Microsoft just isn't very good at
writing software. Except Microsoft doesn't only make Windows — and modern
cloud services, built recently by people who knew exactly what they were
building, break too.

This video is about what is actually going on underneath: decades of
layers that nobody is allowed to remove, what that does to testing, and
why the deepest part of Windows might be the least embarrassing part of
it.

Chapters:
0:00 One batch, one Tuesday
0:47 The cursor from 1998
1:45 Can the computer still make a sound?
2:51 A single year of the list
3:24 The update that broke the repair tool
3:43 The same bug, twenty months later
4:09 None of this is new
4:53 But Microsoft doesn't only make Windows
5:43 An archaeological dig that still runs
6:34 Making Windows behave like Windows
7:30 AI writes faster. Testing doesn't.
8:41 So why might the kernel be different?
9:32 Hard constraints
10:05 What it has had to survive
11:06 Somebody did read an older version
11:50 The strange conclusion

Subtitles are written for this video, not auto-generated. An American
English audio track is available as a second audio track.
```

> **Odstavec o titulcích je závazné znění** (`docs/zverejneni.md`) —
> nejmenuje počet jazyků schválně, aby se nemusel přepisovat na 530
> místech při každém rozšíření kanálu.
>
> **Věta o americké audiostopě tam JE**, protože tohle video stopu má:
> `render/audio-en-US.m4a` (17,3 MB) a `subtitles/en-US.srt` (204 titulků).
> Stopu umí nahrát **jedině Studio**, z API se její existence nepozná —
> proto je to zároveň položka v seznamu „co musí uživatel naklikat sám".

---

## Nastavení při nahrávání

| pole | hodnota |
|---|---|
| jazyk videa | **`en-GB`** — nastavit **NEJDŘÍV**, jinak zůstane dlaždice Titulky zašedlá |
| kategorie | Věda a technika |
| publikum | není určeno pro děti |
| prohlášení o AI | **ne** — SDXL scény jsou malované ilustrace (5 scén ze 118), žádný fotorealismus, hudba procedurální, hlas není klonovaný |
| viditelnost | nejdřív **neveřejně**, podívat se na to v přehrávači, teprve pak zveřejnit |

## Tagy

```
windows, microsoft, software quality, qa, testing, regression,
windows update, kernel, operating system, legacy code, technical debt,
software engineering, windows nt, ai coding, explainer
```

## STAV NAHRÁNÍ — video je na https://youtu.be/A5iiUF2u4WU (neveřejné)

Část doplnil `nahraj.py --k-videu`, pak **došla denní kvóta**. Ověřeno
výpisem z API, ne odhadem:

| | |
|---|---|
| titul, popis, 15 tagů | ✅ hotovo |
| jazyk videa `en-GB`, kategorie Věda a technika | ✅ hotovo |
| náhled | ✅ hotovo |
| titulky **en, cs, sv, es, pt-BR** | ✅ hotovo |

### Zbývá — vše ručně

**1. Titulky, deset jazyků.** Soubory jsou v `subtitles/`:

```
de  fr  it  pl  id  tr  uk  vi  fi  en-US
```

> Pozor: na videu je i stopa **`en-GB`, kterou jsme nenahrávali** — to je
> automatický přepis od YouTube. **Smaž ho**; konkuruje našim překladům
> a je z nich nejhorší. YouTube si ho po čase vyrobí znovu.

**2. Lokalizované názvy a popisy, třináct jazyků.**
Podrobnosti → Přidat jazyk. Zdroj je **`youtube-preklady.md`** — kopíruj
vždy celý blok mezi trojicí zpětných apostrofů, sekce jsou už seřazené
tak, jak je Studio zobrazuje (shora dolů).

**3. Americká audiostopa.** `render/audio-en-US.m4a` (17,3 MB).
**Nahrát ji umí jedině Studio**, přes API to nejde. Popis na ni už
odkazuje ve všech čtrnácti jazycích, takže bez ní by popis lhal.

**4. Závěrečná obrazovka.** Data API na ni nemá ani zdroj. Místo je
ověřené — `zaver_check.py` hlásí u všech čtyř posledních scén volné rohy
a kresbu kolem 1 %. **Prvky patří do HORNÍ poloviny**, dole je titulek.

**5. Playlist a evidence.** Dopsat slug do `playlisty.json`, spustit
`analytics.py --videa` a `tools/playlisty.py`. A zapsat číslo i odkaz
do **`Témata.ods`, řádek 53**.

## Co musí uživatel naklikat sám## Co musí uživatel naklikat sám

| | |
|---|---|
| **závěrečná obrazovka** | vždycky ručně — Data API na ni nemá ani zdroj. Místo je ověřené: `zaver_check.py` hlásí u všech čtyř posledních scén volné rohy a kresbu kolem 1 % |
| prohlášení o AI a osvědčení o zproštění | vyřídí průvodce, když se MP4 nahraje ručně ve Studiu |
| **americká audiostopa** | `render/audio-en-US.m4a` je hotová; nahrát ji umí **jedině Studio**, přes API to nejde |

## Po zveřejnění

1. `tools/nahraj.py --k-videu <ID>` — titul, popis, tagy, kategorie, jazyk.
   **Dokud se nepustí, video visí pod názvem souboru** a `analytics.py`
   ho nespáruje se slugem.
2. `tools/titulky.py` — titulkové stopy.
3. `tools/titulky.py --vse --smaz-asr` — smazat automatický přepis;
   YouTube si ho vyrobí znovu, takže se to pouští po každém nahrání.
4. `tools/lokalizace.py videos/053-… ` — lokalizované názvy a popisy
   z `youtube-preklady.md`.
5. Dopsat slug do `playlisty.json`, pak `analytics.py --videa`
   a `tools/playlisty.py`.
6. Zapsat odkaz a stav do **`Témata.ods`** (řádek 53).
