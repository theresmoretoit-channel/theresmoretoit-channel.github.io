# Fact check — 045 IE6: Why Did It Stop For Five Years?

**Předběžný fact check TŘÍ NOSNÝCH TVRZENÍ, ověřeno 2026-09-14 — před
scénářem, ne po něm.**

Důvod toho pořadí: u 039 fact check přepsal celý oblouk (*„XP = IE6"* bylo
věcně špatně) a scénář se psal dvakrát. Tady tři body drží tezi *„pět let
bez nové verze"*; kdyby neobstály, mění se stavba videa, ne formulace.

**Zbylých šest bodů ze `notes.md` (XMLHttpRequest, XP SP2, Firefox 1.0,
user-agent, data antimonopolního procesu, čísla o spyware) se ověří
standardně na hotovém scénáři** — mění věty, ne stavbu.

---

## 1. Pětiletá mezera ✅ POTVRZENO, a je delší, než zněl odhad

| | |
|---|---|
| IE6 | **24. 8. 2001** |
| IE7 | **18. 10. 2006** |
| mezera | **5 let a 2 měsíce** |

Mezitím vyšly dva service packy, takže **nesmí zaznít, že se pět let nic
neopravovalo** (viz „ZAMČENÁ FORMULACE" v `notes.md`):

| | | co přinesl |
|---|---|---|
| IE6 SP1 | 30. 8. 2002 | bezpečnostní záplaty, **beze změny vykreslování** |
| IE6 SP2 | 25. 8. 2004 | **blokování popupů, správce doplňků** |

> **🟡 NÁLEZ, který zpřesňuje tezi (a zlepšuje ji).** IE6 SP2 není
> samostatné vydání prohlížeče — **je to prohlížeč z Windows XP SP2**,
> a mění chování prohlížeče podstatně. Teze proto zní přesně takhle:
>
> **Pět let bez nové verze prohlížeče — a jediná podstatná změna za tu
> dobu přišla jako service pack OPERAČNÍHO SYSTÉMU, ne jako vydání
> prohlížeče.**
>
> Tím se blok 3 (XP SP2) mění z „třetího tématu" na **vyvrcholení téže
> teze**: prohlížeč se nemohl opravit jako prohlížeč, protože jím podle
> vlastní firmy přestal být. To je zároveň doslovné potvrzení dílu 017.

## 2. Útlum vývoje ✅ POTVRZENO, ale JINAK, než zadání předpokládalo

Formulace *„rozpuštění týmu"* je vyprávěná zkratka a přímý doklad pro ni
nemám. **Doložitelné jsou dvě věci, a jsou lepší:**

**a) Microsoft to oznámil veřejně — 7. 5. 2003.** Brian Countryman, program
manager IE, v online chatu Microsoftu: na Windows se **IE přestane
distribuovat samostatně**, IE6 je poslední samostatná verze a prohlížeč
bude pokračovat jen jako součást vývoje Windows, s aktualizacemi
v upgradech systému.

**b) Vedoucí vývojář IE to popsal sám, z první ruky.** Chris Wilson
(lead program manager IE, na IE od verze 2.0 v roce 1995) v textu
*„The 'IE plateau' — a history lesson"* (2010). Verbatim:

> „This led us to start working on the platform re-think that eventually
> became WPF/XAML/.NET3.0 – and that's what **most of us moved over to
> work on** in that timeframe."

> „we were **pretty far ahead of the competitor's released product** at
> that point, and sadly, **Microsoft does seem to work best with strong
> competition motivating it**."

Wilson uvádí jako „perfect storm" čtyři důvody najednou: přesun lidí na
platformu Windows (WPF/XAML), malé rozšíření bohatých webových aplikací
(prosazoval se Flash), splasknutí internetové bubliny a bezpečnostní
problémy, které si vyžádaly obrovské úsilí. K tomu „getting mired in
backwards compatibility".

> **Dopad na scénář:** blok 1 se **nemá** opírat o větu „Microsoft
> rozpustil tým". Má se opírat o tyhle dvě — oznámení z května 2003
> a Wilsonovo vlastní svědectví. Je to silnější, doložitelnější, a ta
> druhá citace **říká tezi videa za nás**: nepřestali, protože neuměli,
> ale protože je nikdo netlačil.

**A restart je taky doložený:** **15. 2. 2005** oznámil Bill Gates na
konferenci RSA nový Internet Explorer; jak Gates, tak Dean Hachamovitch
uvedli jako hlavní důvod **potřebné bezpečnostní zlepšení**. To potvrzuje
závěr videa („rozmrazil to bezpečnostní průšvih") z primárního směru —
z úst Microsoftu, ne z našeho výkladu.

## 3. Mac IE5 / Tasman ✅ POTVRZENO

| | |
|---|---|
| oznámeno | 5. 1. 2000, Macworld Expo San Francisco |
| vydáno | **27. 3. 2000** |
| engine | **Tasman**, cílil na HTML 4.0, CSS1, DOM1, ECMAScript |
| proti Tridentu | **lepší podpora CSS** a **netrpěl chybou box modelu** |
| konec vývoje | **13. 6. 2003** — Roz Ho (GM Macintosh Business Unit) potvrdila, že kromě bezpečnostních oprav už nové verze nebudou |
| poslední verze | **16. 6. 2003**, 5.2.3 pro Mac OS X |
| staženo z webu | 31. 1. 2006 |

**Protiobraz tedy platí a je ostrý:** v roce 2000 měl Microsoft prohlížeč
bez chyby box modelu, který je celým dílem 017 i 028, a v červnu 2003 ho
odložil — **šest týdnů po tom, co oznámil, že IE6 je poslední samostatná
verze.** Obě rozhodnutí padla v témž pololetí.

**Doctype switching** vznikl tam: vymyslel a napsal ho **Tantek Çelik**,
vývojový vedoucí Mac IE, po rozhovoru s Toddem Fahrnerem.

> **🟡 Rozpor ve zdrojích k hlídání:** jeden sekundární zdroj klade vydání
> Mac IE5 na březen **2002**. To je nejspíš záměna s verzí 5.2; držíme
> **27. 3. 2000** a před scénářem se to ověří ještě jednou, nejlépe
> dobovou tiskovou zprávou Microsoftu, ne encyklopedií.

---

## Co z toho plyne pro scénář

1. **Teze platí**, jen se zpřesňuje: pět let bez nové verze **prohlížeče**,
   a jediná podstatná změna přišla jako service pack systému.
2. **Blok 1 dostane jinou páteř**: ne „rozpustili tým", nýbrž
   **7. 5. 2003 (poslední samostatná verze)** + **Wilsonovo svědectví**
   + **13. 6. 2003 (konec Mac IE5)**. Tři data v jednom roce.
3. **Blok 3 přestává být třetí téma** a stává se vyvrcholením: oprava
   prohlížeče musela přijít jako záplata operačního systému.
4. **Závěr má doklad z první ruky** — Gates, RSA, únor 2005, důvodem
   bezpečnost; a Wilsonovo *„Microsoft does seem to work best with strong
   competition motivating it"*.

## Zdroje

- Wikipedia — [Internet Explorer 6](https://en.wikipedia.org/wiki/Internet_Explorer_6)
  (data vydání, SP1, SP2, oznámení z 7. 5. 2003)
- Wikipedia — [Internet Explorer 7](https://en.wikipedia.org/wiki/Internet_Explorer_7)
  (RSA 15. 2. 2005, bezpečnost jako důvod)
- Wikipedia — [Internet Explorer for Mac](https://en.wikipedia.org/wiki/Internet_Explorer_for_Mac)
  (Tasman, data, Roz Ho)
- Chris Wilson — [The „IE plateau" – a history lesson](https://cwilso.com/2010/04/30/the-ie-plateau-a-history-lesson/)
  (svědectví z první ruky, 2010)
- CSS-Tricks — [A Look Back at the History of CSS](https://css-tricks.com/look-back-history-css/)
  (doctype switching, Tantek Çelik, Todd Fahrner)

> **Encyklopedie je pro tyhle tři body dostatečná na ROZHODNUTÍ o stavbě,
> ne na citaci ve videu.** Každé datum, které ve scénáři skutečně zazní,
> se před TTS dohledá v dobovém nebo primárním zdroji — platí pravidlo
> z `CLAUDE.md`, že sekundární zdroj neunese zobecnění.

---

## Přibylo se storyboardem: DATA V OBRAZE (2026-09-14)

Páteř videa je časová osa a **hustota zářezů verzí je tvrzení**, ne
dekorace — divák z ní čte tezi dřív, než ji uslyší. Tyhle datumy jsou
tedy ve videu vidět a patří do fact checku stejně jako věty scénáře.
Leží v jedné tabulce `VERZE` v `diagrams/gen/_kit.py`:

| verze | datum v obraze |
|---|---|
| IE1 | 16. 8. 1995 |
| IE2 | 22. 11. 1995 |
| IE3 | 13. 8. 1996 |
| IE4 | 30. 9. 1997 |
| IE5 | 18. 3. 1999 |
| IE5.5 | 12. 7. 2000 |
| IE6 | **24. 8. 2001** (ověřeno výš, bod 1) |
| IE7 | **18. 10. 2006** (ověřeno výš, bod 1) |

🟡 **Ověřeno je zatím jen IE6 a IE7.** Zbylých šest je z encyklopedické
znalosti a před renderem se musí dohledat — u S01 na nich stojí obraz,
který nese tezi.

Totéž platí pro ostatní datumy na ose (`DATA` v témž souboru): žaloba
18. 5. 1998, rozdělení nařízeno 7. 6. 2000, odvolací soud 28. 6. 2001,
Mac IE5 27. 3. 2000, chat 7. 5. 2003, konec Mac IE5 13. 6. 2003,
XP SP2 25. 8. 2004, Firefox 1.0 9. 11. 2004, RSA 15. 2. 2005,
Vista 30. 1. 2007. **Osm z deseti je ověřeno výš**; neověřené zůstávají
přesná data XP SP2 a Visty.

> **Dva odstupy, které video vyslovuje, se nekreslí od oka.**
> `zkontroluj_pater()` v `_kit.py` počítá z týchž dat, že mezi
> rozsudkem a IE6 je osm týdnů a mezi oznámením a koncem Mac IE5 šest,
> a spadne, kdyby to přestalo platit. Kdyby se některé datum po ověření
> změnilo, ozve se to tam — ne u diváka.

---

## Druhé kolo: zbylých šest bodů (2026-09-14, po dokončení scénáře)

### ✅ XMLHttpRequest — potvrzeno včetně původu

Vznikl v týmu **Outlook Web Access** pro Exchange (koncept 1998, autorem
uváděn Shawn Bracewell, 1999) a dodal se jako **`XMLHTTP` v knihovně
MSXML, která přišla s Internet Explorerem 5 v březnu 1999** — tedy přesně
tak, jak to říká S46–S49: firemní pošta, komponenta ActiveX, jméno po
formátu, který ten rok letěl. Ostatní prohlížeče ho pak přepsaly jako
`XMLHttpRequest`; Microsoft převzal nativní podobu až v IE7. Scéna S51
(„ostatní si nakonec udělali vlastní") tím sedí.

### ✅ XP SP2 — potvrzeno všechny čtyři položky z S78

Vydáno **6. 8. 2004** (RTM), obsahuje **blokování popupů zapnuté ve
výchozím stavu**, **informační lištu** místo modálních dialogů, **správce
doplňků** (jmenovitě na „helper objects" a lišty) a **potvrzování
ActiveX** přes tu lištu. Scénář říká „August 2004" a jmenuje právě tyhle
čtyři věci — sedí.

### ✅ Firefox 1.0 — 9. 11. 2004

Tedy tři měsíce po SP2 a tři měsíce před RSA (15. 2. 2005). Obě „three
months" v S82 a S83 jsou správně.

### 🟠 Data verzí IE v obraze — DVĚ BYLA ŠPATNĚ, opraveno

| verze | bylo v `_kit.py` | správně |
|---|---|---|
| IE2 | 22. 11. 1995 | **27. 11. 1995** |
| IE4 | 30. 9. 1997 | **22. 9. 1997** |

Ostatní sedí (IE1 16. 8. 1995, IE3 13. 8. 1996, IE5 18. 3. 1999,
IE6 24. 8. 2001, IE7 18. 10. 2006). U **IE1 se zdroje liší** (16., 17.
i 24. srpna) a u **IE5.5 se přesné datum nepodařilo doložit** — držíme
12. 7. 2000 a je to jediný neověřený údaj v tabulce.

> **Dopad na obraz je měřitelně nulový.** Po opravě se S01 od předchozí
> verze liší **501 pixelem z 3 686 400, tedy 0,014 %** (PSNR 40,6 dB):
> zářezy se posunuly o pixel. V obraze totiž žádné datum není — jsou tam
> čísla verzí a stupnice let. **Master se proto nepřerenderovával** a je
> to vědomé rozhodnutí, ne přehlédnutí.

### 🟡 Zbývá k ověření před zveřejněním

- **user-agent řetězec v S61** — je opsaný z Chrome na Linuxu a ve videu
  se tvrdí, že si to divák může ověřit sám. Než se vydá, projít ho proti
  živému prohlížeči.
- **„čtyři lišty a třetina obrazovky" v S72** — je to charakteristika
  doby, ne doložené číslo. Ve scénáři zní jako obraz („machines with four
  of them"), takže se nechává; kdyby to mělo znít jako měření, chce to
  doklad.
- `innerHTML`, `contentEditable` a `text-overflow` jako dědictví IE
  (S57–S59): že pocházejí z IE, doložit jde. Věty **„every framework
  since is a descendant"** a **„every rich text editor… sits on top of
  it"** jsou ale výklad, ne fakt — zůstávají jako dramaturgické
  zobecnění a je to tu zapsané schválně.

