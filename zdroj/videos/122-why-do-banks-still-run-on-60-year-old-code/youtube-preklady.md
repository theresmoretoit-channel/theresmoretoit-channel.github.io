# YouTube — 122 „Why Do Banks Still Run on 60-Year-Old Code?“: lokalizace

Lokalizované názvy a popisy pro třináct jazyků (bez `en`, ten je
v `youtube.md`). Pořadí podle YouTube Studia. Nahrává
`python tools/lokalizace.py videos/122-why-do-banks-still-run-on-60-year-old-code`.

**Co se NEPŘEKLÁDÁ:**

- vlastní jména (COBOL, GnuCOBOL, TSB, Commonwealth Bank, Pentagon
  v místním tvaru, IBM, Slaughter and May, Martin Fowler…),
- časy kapitol, ty jsou na vteřinu shodné s angličtinou,
- citace v řádku zdrojů (názvy publikací, institucí, dokumentů a data
  citací) — přeložené je jen úvodní slovo „Sources:“, spojky a vsuvka
  „with the examples run in GnuCOBOL 3.2“,
- řádky s atribucí snímků (TASL) zůstávají jako v angličtině; přeložené
  jsou jen nadpis, „via“, „Licences“ a věta o volných dílech,
- tagy — YouTube je pro jednotlivé jazyky nemá.

Částka je v místním zápisu desetinné čárky (999,99 £), „penny“ jako
v titulcích daného jazyka (cs penci, pl pens, es penique, vi xu, tr peni).
Kapitoly přebírají znění titulků (`script.<kód>.md`, S01, S12, S55, S70…).
Pointa videa (S71–S72) ani výsledek auditu v New Jersey (S60) se v popisu
neprozrazují, stejně jako v angličtině. Odstavec o titulcích a americké
stopě je doslova z kanonické tabulky v `docs/zverejneni.md`. Registr
neformální tam, kde jazyk volbu má, jako v překladech titulků (cs ty,
de du, fr tu, it tu, es tú evropská, pt-BR você, pl ty, uk ти, tr sen,
id kamu); finština „sinä“, vietnamština „bạn“.

## suomi (`fi`)

```
Miksi pankit käyttävät yhä 60 vuotta vanhaa koodia?
```

```
Lisää yksi penny summaan 999,99 £ väärässä COBOL-kentässä, ja tulos on nolla. Ei virheilmoitusta, ei kaatumista. Se ei ole bugi. Se on sääntö, ja monet maailman pankit toimivat yhä tällaisten sääntöjen varassa.

COBOL on ohjelmointikieli vuodelta 1959. Miksi pankit eivät siis ole korvanneet sitä, vaikka niillä on rahaa ja insinöörejä? Tässä videossa katsotaan, miksi uudelleenkirjoittaminen ei ole kääntämistä ja miten Pentagonissa pidetty kokous antoi liike-elämälle yhteisen kielen. Lisäksi käydään läpi kolme todellista tapausta: brittipankki, joka yritti jättää vanhan järjestelmänsä, australialainen pankki, joka onnistui siinä, ja pandemian aikainen kriisi New Jerseyssä, josta kaikki syyttivät COBOLia.

Lähteet: IBM Enterprise COBOL for z/OS 6.4 Language Reference (ROUNDED, SIZE ERROR, assumed decimal point), esimerkit ajettu GnuCOBOL 3.2:lla; Java BigDecimal documentation; COBOL initial specifications, US Department of Defense, April 1960; IBM System/360 Principles of Operation; IBM z/Architecture Principles of Operation; IBM 10-K, fiscal 2022; SSA IT Modernization Plan, 2017; GAO-25-107795 (2025); FCA Final Notice to TSB Bank plc (2022); Slaughter and May, TSB Review (2019); TSB 2018 full-year results; Commonwealth Bank of Australia, Recent Developments (2008) ja 2013 Shareholder Review; iTWire ja Delimiter, February 2011; New Jersey Department of Labor, March 2020; New Jersey Office of the State Auditor (2022); WIRED, "Can't File for Unemployment? Don't Blame Cobol" (2020); Mar Hicks, "Built to Last", Logic (2020); Martin Fowler, "StranglerApplication" (2004).

Tekstitykset on kirjoitettu tätä videota varten, ei luotu automaattisesti. Toisena ääniraitana on amerikanenglanti.

LUVUT
00:00 Lisää yksi penny
00:46 Kieli vuodelta 1959
01:17 Miksei sitä vain kirjoiteta uudelleen?
02:22 Miten COBOL päätyi sinne
03:56 Kuinka paljon on yhä käytössä
04:41 TSB: pankki lähtee
06:28 Commonwealth Bank: hidas lähtö
07:32 New Jersey: kaikki syyttivät COBOLia
08:57 Kolme tapausta
09:34 Rakenna ympärille, korvaa pala kerrallaan
10:07 Takaisin puoleen pennyyn

KUVALÄHTEET
Grace Hopper and UNIVAC — unknown author, CC BY 2.0
IBM System/360 Model 30 — ArnoldReinhold, CC BY-SA 3.0
TSB Newcastle — TubularWorld, CC BY-SA 3.0
Commonwealth Bank branch office — Maksym Kozlenko, CC BY-SA 4.0
Wikimedia Commonsin kautta
Lisenssit: creativecommons.org/licenses/by/2.0, creativecommons.org/licenses/by-sa/3.0, creativecommons.org/licenses/by-sa/4.0
Kaikki muut arkistokuvat ovat public domainia.
```

## français (`fr`)

```
Pourquoi les banques tournent-elles encore avec du code vieux de 60 ans ?
```

```
Ajoute un penny à 999,99 £ dans le mauvais champ COBOL, et le résultat est zéro. Pas de message d'erreur, pas de plantage. Ce n'est pas un bug. C'est une règle, et beaucoup de banques dans le monde tournent encore avec des règles comme celles-là.

COBOL est un langage de programmation de 1959. Pourquoi les banques ne l'ont-elles donc pas remplacé, alors qu'elles ont l'argent et les ingénieurs ? Cette vidéo montre pourquoi réécrire n'est pas traduire et comment une réunion au Pentagone a donné au monde des affaires sa langue commune, puis examine trois cas réels : une banque britannique qui a tenté de quitter son vieux système, une banque australienne qui y est parvenue, et une crise en pleine pandémie dans le New Jersey, où tout le monde a accusé COBOL.

Sources : IBM Enterprise COBOL for z/OS 6.4 Language Reference (ROUNDED, SIZE ERROR, assumed decimal point), avec les exemples exécutés dans GnuCOBOL 3.2 ; Java BigDecimal documentation ; COBOL initial specifications, US Department of Defense, April 1960 ; IBM System/360 Principles of Operation ; IBM z/Architecture Principles of Operation ; IBM 10-K, fiscal 2022 ; SSA IT Modernization Plan, 2017 ; GAO-25-107795 (2025) ; FCA Final Notice to TSB Bank plc (2022) ; Slaughter and May, TSB Review (2019) ; TSB 2018 full-year results ; Commonwealth Bank of Australia, Recent Developments (2008) et 2013 Shareholder Review ; iTWire et Delimiter, February 2011 ; New Jersey Department of Labor, March 2020 ; New Jersey Office of the State Auditor (2022) ; WIRED, "Can't File for Unemployment? Don't Blame Cobol" (2020) ; Mar Hicks, "Built to Last", Logic (2020) ; Martin Fowler, "StranglerApplication" (2004).

Les sous-titres sont écrits pour cette vidéo, pas générés automatiquement. Une piste audio en anglais américain est disponible en seconde piste.

CHAPITRES
00:00 Ajoute un penny
00:46 Un langage de 1959
01:17 Pourquoi ne pas tout réécrire ?
02:22 Comment COBOL en est arrivé là
03:56 Combien de code tourne encore
04:41 TSB : une banque s'en va
06:28 Commonwealth Bank : partir lentement
07:32 New Jersey : tout le monde a accusé COBOL
08:57 Trois cas
09:34 L'envelopper, le remplacer morceau par morceau
10:07 Retour au demi-penny

CRÉDITS DES IMAGES
Grace Hopper and UNIVAC — unknown author, CC BY 2.0
IBM System/360 Model 30 — ArnoldReinhold, CC BY-SA 3.0
TSB Newcastle — TubularWorld, CC BY-SA 3.0
Commonwealth Bank branch office — Maksym Kozlenko, CC BY-SA 4.0
via Wikimedia Commons
Licences : creativecommons.org/licenses/by/2.0, creativecommons.org/licenses/by-sa/3.0, creativecommons.org/licenses/by-sa/4.0
Toutes les autres images d'archives sont dans le domaine public.
```

## Bahasa Indonesia (`id`)

```
Mengapa bank masih berjalan dengan kode berusia 60 tahun?
```

```
Tambahkan satu penny ke £999,99 di field COBOL yang salah, dan hasilnya nol. Tanpa pesan error, tanpa crash. Itu bukan bug. Itu aturan, dan banyak bank di dunia masih berjalan di atas aturan seperti ini.

COBOL adalah bahasa pemrograman dari tahun 1959. Lalu mengapa bank belum menggantinya, padahal mereka punya uang dan insinyur? Video ini membahas mengapa menulis ulang bukan sekadar menerjemahkan, bagaimana sebuah rapat di Pentagon memberi dunia bisnis bahasa bersamanya, dan tiga kasus nyata: bank Inggris yang mencoba meninggalkan sistem lamanya, bank Australia yang berhasil melakukannya, dan krisis di masa pandemi di New Jersey yang membuat semua orang menyalahkan COBOL.

Sumber: IBM Enterprise COBOL for z/OS 6.4 Language Reference (ROUNDED, SIZE ERROR, assumed decimal point), dengan contoh-contoh yang dijalankan di GnuCOBOL 3.2; Java BigDecimal documentation; COBOL initial specifications, US Department of Defense, April 1960; IBM System/360 Principles of Operation; IBM z/Architecture Principles of Operation; IBM 10-K, fiscal 2022; SSA IT Modernization Plan, 2017; GAO-25-107795 (2025); FCA Final Notice to TSB Bank plc (2022); Slaughter and May, TSB Review (2019); TSB 2018 full-year results; Commonwealth Bank of Australia, Recent Developments (2008) dan 2013 Shareholder Review; iTWire dan Delimiter, February 2011; New Jersey Department of Labor, March 2020; New Jersey Office of the State Auditor (2022); WIRED, "Can't File for Unemployment? Don't Blame Cobol" (2020); Mar Hicks, "Built to Last", Logic (2020); Martin Fowler, "StranglerApplication" (2004).

Subtitel ditulis khusus untuk video ini, bukan dibuat secara otomatis. Tersedia juga trek audio kedua dalam bahasa Inggris Amerika.

BAB
00:00 Tambahkan satu penny
00:46 Bahasa dari tahun 1959
01:17 Kenapa tidak ditulis ulang saja?
02:22 Bagaimana COBOL bisa sampai di sana
03:56 Seberapa banyak yang masih berjalan
04:41 TSB: sebuah bank pindah
06:28 Commonwealth Bank: pindah pelan-pelan
07:32 New Jersey: semua orang menyalahkan COBOL
08:57 Tiga kasus
09:34 Bungkus, lalu ganti sedikit demi sedikit
10:07 Kembali ke setengah penny

KREDIT GAMBAR
Grace Hopper and UNIVAC — unknown author, CC BY 2.0
IBM System/360 Model 30 — ArnoldReinhold, CC BY-SA 3.0
TSB Newcastle — TubularWorld, CC BY-SA 3.0
Commonwealth Bank branch office — Maksym Kozlenko, CC BY-SA 4.0
melalui Wikimedia Commons
Lisensi: creativecommons.org/licenses/by/2.0, creativecommons.org/licenses/by-sa/3.0, creativecommons.org/licenses/by-sa/4.0
Semua gambar arsip lainnya berstatus domain publik.
```

## italiano (`it`)

```
Perché le banche funzionano ancora con codice di 60 anni fa?
```

```
Aggiungi un penny a 999,99 £ nel campo COBOL sbagliato e il risultato è zero. Nessun messaggio di errore, nessun crash. Non è un bug. È una regola, e molte banche nel mondo funzionano ancora con regole come queste.

Il COBOL è un linguaggio di programmazione del 1959. Allora perché le banche non l'hanno sostituito, visto che hanno i soldi e gli ingegneri? Questo video spiega perché riscrivere non è tradurre e come una riunione al Pentagono ha dato al mondo degli affari la sua lingua comune, poi racconta tre casi reali: una banca britannica che ha provato a lasciare il suo vecchio sistema, una banca australiana che ci è riuscita, e una crisi durante la pandemia nel New Jersey, in cui tutti hanno dato la colpa al COBOL.

Fonti: IBM Enterprise COBOL for z/OS 6.4 Language Reference (ROUNDED, SIZE ERROR, assumed decimal point), con gli esempi eseguiti in GnuCOBOL 3.2; Java BigDecimal documentation; COBOL initial specifications, US Department of Defense, April 1960; IBM System/360 Principles of Operation; IBM z/Architecture Principles of Operation; IBM 10-K, fiscal 2022; SSA IT Modernization Plan, 2017; GAO-25-107795 (2025); FCA Final Notice to TSB Bank plc (2022); Slaughter and May, TSB Review (2019); TSB 2018 full-year results; Commonwealth Bank of Australia, Recent Developments (2008) e 2013 Shareholder Review; iTWire e Delimiter, February 2011; New Jersey Department of Labor, March 2020; New Jersey Office of the State Auditor (2022); WIRED, "Can't File for Unemployment? Don't Blame Cobol" (2020); Mar Hicks, "Built to Last", Logic (2020); Martin Fowler, "StranglerApplication" (2004).

I sottotitoli sono scritti per questo video, non generati automaticamente. Come seconda traccia audio è disponibile l’inglese americano.

CAPITOLI
00:00 Aggiungi un penny
00:46 Un linguaggio del 1959
01:17 Perché non riscriverlo e basta?
02:22 Come ci è arrivato il COBOL
03:56 Quanto ne gira ancora
04:41 TSB: una banca se ne va
06:28 Commonwealth Bank: andarsene piano
07:32 New Jersey: tutti diedero la colpa al COBOL
08:57 Tre casi
09:34 Avvolgerlo, sostituirlo pezzo per pezzo
10:07 Ritorno al mezzo penny

CREDITI DELLE IMMAGINI
Grace Hopper and UNIVAC — unknown author, CC BY 2.0
IBM System/360 Model 30 — ArnoldReinhold, CC BY-SA 3.0
TSB Newcastle — TubularWorld, CC BY-SA 3.0
Commonwealth Bank branch office — Maksym Kozlenko, CC BY-SA 4.0
tramite Wikimedia Commons
Licenze: creativecommons.org/licenses/by/2.0, creativecommons.org/licenses/by-sa/3.0, creativecommons.org/licenses/by-sa/4.0
Tutte le altre immagini d'archivio sono di pubblico dominio.
```

## Deutsch (`de`)

```
Warum laufen Banken noch immer mit 60 Jahre altem Code?
```

```
Rechne im falschen COBOL-Feld einen Penny zu 999,99 £ dazu, und das Ergebnis ist null. Keine Fehlermeldung, kein Absturz. Das ist kein Bug. Das ist eine Regel, und viele Banken auf der Welt laufen immer noch mit solchen Regeln.

COBOL ist eine Programmiersprache von 1959. Warum haben die Banken sie also nicht ersetzt, obwohl sie das Geld und die Ingenieure haben? Dieses Video zeigt, warum Neuschreiben kein Übersetzen ist und wie ein Treffen im Pentagon der Geschäftswelt ihre gemeinsame Sprache gab. Dazu drei echte Fälle: eine britische Bank, die ihr altes System verlassen wollte, eine australische Bank, der das gelungen ist, und eine Krise während der Pandemie in New Jersey, an der alle COBOL die Schuld gaben.

Quellen: IBM Enterprise COBOL for z/OS 6.4 Language Reference (ROUNDED, SIZE ERROR, assumed decimal point), die Beispiele in GnuCOBOL 3.2 ausgeführt; Java BigDecimal documentation; COBOL initial specifications, US Department of Defense, April 1960; IBM System/360 Principles of Operation; IBM z/Architecture Principles of Operation; IBM 10-K, fiscal 2022; SSA IT Modernization Plan, 2017; GAO-25-107795 (2025); FCA Final Notice to TSB Bank plc (2022); Slaughter and May, TSB Review (2019); TSB 2018 full-year results; Commonwealth Bank of Australia, Recent Developments (2008) und 2013 Shareholder Review; iTWire und Delimiter, February 2011; New Jersey Department of Labor, March 2020; New Jersey Office of the State Auditor (2022); WIRED, "Can't File for Unemployment? Don't Blame Cobol" (2020); Mar Hicks, "Built to Last", Logic (2020); Martin Fowler, "StranglerApplication" (2004).

Die Untertitel wurden für dieses Video geschrieben, nicht automatisch erzeugt. Als zweite Tonspur steht amerikanisches Englisch bereit.

KAPITEL
00:00 Rechne einen Penny dazu
00:46 Eine Sprache von 1959
01:17 Warum nicht einfach neu schreiben?
02:22 Wie COBOL dorthin kam
03:56 Wie viel noch läuft
04:41 TSB: eine Bank steigt aus
06:28 Commonwealth Bank: langsam aussteigen
07:32 New Jersey: alle gaben COBOL die Schuld
08:57 Drei Fälle
09:34 Umhüllen und Stück für Stück ersetzen
10:07 Zurück zum halben Penny

BILDNACHWEIS
Grace Hopper and UNIVAC — unknown author, CC BY 2.0
IBM System/360 Model 30 — ArnoldReinhold, CC BY-SA 3.0
TSB Newcastle — TubularWorld, CC BY-SA 3.0
Commonwealth Bank branch office — Maksym Kozlenko, CC BY-SA 4.0
über Wikimedia Commons
Lizenzen: creativecommons.org/licenses/by/2.0, creativecommons.org/licenses/by-sa/3.0, creativecommons.org/licenses/by-sa/4.0
Alle übrigen Archivbilder sind gemeinfrei.
```

## polski (`pl`)

```
Dlaczego banki wciąż działają na 60-letnim kodzie?
```

```
Dodaj jeden pens do 999,99 £ w niewłaściwym polu COBOL-a, a wynik wyniesie zero. Żadnego komunikatu o błędzie, żadnej awarii. To nie jest usterka. To reguła, a wiele banków na świecie wciąż działa na takich regułach.

COBOL to język programowania z 1959 roku. Dlaczego więc banki go nie zastąpiły, skoro mają pieniądze i inżynierów? Ten film pokazuje, dlaczego przepisanie to nie tłumaczenie i jak spotkanie w Pentagonie dało biznesowi wspólny język, a potem przygląda się trzem prawdziwym przypadkom: brytyjskiemu bankowi, który próbował odejść od starego systemu, australijskiemu bankowi, któremu się to udało, i kryzysowi z czasów pandemii w New Jersey, za który wszyscy winili COBOL.

Źródła: IBM Enterprise COBOL for z/OS 6.4 Language Reference (ROUNDED, SIZE ERROR, assumed decimal point), przykłady uruchomione w GnuCOBOL 3.2; Java BigDecimal documentation; COBOL initial specifications, US Department of Defense, April 1960; IBM System/360 Principles of Operation; IBM z/Architecture Principles of Operation; IBM 10-K, fiscal 2022; SSA IT Modernization Plan, 2017; GAO-25-107795 (2025); FCA Final Notice to TSB Bank plc (2022); Slaughter and May, TSB Review (2019); TSB 2018 full-year results; Commonwealth Bank of Australia, Recent Developments (2008) i 2013 Shareholder Review; iTWire i Delimiter, February 2011; New Jersey Department of Labor, March 2020; New Jersey Office of the State Auditor (2022); WIRED, "Can't File for Unemployment? Don't Blame Cobol" (2020); Mar Hicks, "Built to Last", Logic (2020); Martin Fowler, "StranglerApplication" (2004).

Napisy są pisane do tego filmu, nie generowane automatycznie. Jako druga ścieżka dźwiękowa dostępny jest angielski amerykański.

ROZDZIAŁY
00:00 Dodaj jeden pens
00:46 Język z 1959 roku
01:17 Dlaczego po prostu go nie przepisać?
02:22 Jak COBOL się tam znalazł
03:56 Ile wciąż działa
04:41 TSB: bank odchodzi
06:28 Commonwealth Bank: powolne odejście
07:32 New Jersey: wszyscy winili COBOL
08:57 Trzy przypadki
09:34 Obudować i wymieniać kawałek po kawałku
10:07 Powrót do pół pensa

ŹRÓDŁA ZDJĘĆ
Grace Hopper and UNIVAC — unknown author, CC BY 2.0
IBM System/360 Model 30 — ArnoldReinhold, CC BY-SA 3.0
TSB Newcastle — TubularWorld, CC BY-SA 3.0
Commonwealth Bank branch office — Maksym Kozlenko, CC BY-SA 4.0
przez Wikimedia Commons
Licencje: creativecommons.org/licenses/by/2.0, creativecommons.org/licenses/by-sa/3.0, creativecommons.org/licenses/by-sa/4.0
Wszystkie pozostałe zdjęcia archiwalne należą do domeny publicznej.
```

## português (Brasil) (`pt-BR`)

```
Por que os bancos ainda rodam com código de 60 anos atrás?
```

```
Some um penny a £ 999,99 no campo COBOL errado, e o resultado é zero. Nenhuma mensagem de erro, nenhum travamento. Isso não é um bug. É uma regra, e muitos bancos do mundo ainda funcionam com regras assim.

COBOL é uma linguagem de programação de 1959. Então por que os bancos não a substituíram, se têm o dinheiro e os engenheiros? Este vídeo mostra por que reescrever não é traduzir e como uma reunião no Pentágono deu ao mundo dos negócios sua língua comum, e depois analisa três casos reais: um banco britânico que tentou deixar seu sistema antigo, um banco australiano que conseguiu, e uma crise durante a pandemia em Nova Jersey, em que todo mundo culpou o COBOL.

Fontes: IBM Enterprise COBOL for z/OS 6.4 Language Reference (ROUNDED, SIZE ERROR, assumed decimal point), com os exemplos executados no GnuCOBOL 3.2; Java BigDecimal documentation; COBOL initial specifications, US Department of Defense, April 1960; IBM System/360 Principles of Operation; IBM z/Architecture Principles of Operation; IBM 10-K, fiscal 2022; SSA IT Modernization Plan, 2017; GAO-25-107795 (2025); FCA Final Notice to TSB Bank plc (2022); Slaughter and May, TSB Review (2019); TSB 2018 full-year results; Commonwealth Bank of Australia, Recent Developments (2008) e 2013 Shareholder Review; iTWire e Delimiter, February 2011; New Jersey Department of Labor, March 2020; New Jersey Office of the State Auditor (2022); WIRED, "Can't File for Unemployment? Don't Blame Cobol" (2020); Mar Hicks, "Built to Last", Logic (2020); Martin Fowler, "StranglerApplication" (2004).

As legendas foram escritas para este vídeo, não geradas automaticamente. Como segunda faixa de áudio está disponível o inglês americano.

CAPÍTULOS
00:00 Some um penny
00:46 Uma linguagem de 1959
01:17 Por que não simplesmente reescrever?
02:22 Como o COBOL chegou lá
03:56 Quanto ainda está rodando
04:41 TSB: um banco sai
06:28 Commonwealth Bank: saindo devagar
07:32 Nova Jersey: todo mundo culpou o COBOL
08:57 Três casos
09:34 Envolver e substituir pedaço por pedaço
10:07 De volta ao meio penny

CRÉDITOS DAS IMAGENS
Grace Hopper and UNIVAC — unknown author, CC BY 2.0
IBM System/360 Model 30 — ArnoldReinhold, CC BY-SA 3.0
TSB Newcastle — TubularWorld, CC BY-SA 3.0
Commonwealth Bank branch office — Maksym Kozlenko, CC BY-SA 4.0
via Wikimedia Commons
Licenças: creativecommons.org/licenses/by/2.0, creativecommons.org/licenses/by-sa/3.0, creativecommons.org/licenses/by-sa/4.0
Todas as outras imagens de arquivo estão em domínio público.
```

## Türkçe (`tr`)

```
Bankalar neden hâlâ 60 yıllık kodla çalışıyor?
```

```
Yanlış bir COBOL alanında 999,99 sterline bir peni ekle, sonuç sıfır çıkar. Hata mesajı yok, çökme yok. Bu bir hata değil. Bu bir kural, ve dünyadaki pek çok banka hâlâ bu tür kurallarla çalışıyor.

COBOL, 1959'dan kalma bir programlama dili. Peki bankaların parası da mühendisi de varken neden onu değiştirmediler? Bu video, yeniden yazmanın neden çeviri olmadığını ve Pentagon'daki bir toplantının iş dünyasına ortak dilini nasıl verdiğini anlatıyor, ardından üç gerçek vakaya bakıyor: eski sisteminden ayrılmaya çalışan bir İngiliz bankası, bunu başaran bir Avustralya bankası ve pandemi sırasında New Jersey'de herkesin COBOL'u suçladığı bir kriz.

Kaynaklar: IBM Enterprise COBOL for z/OS 6.4 Language Reference (ROUNDED, SIZE ERROR, assumed decimal point), örnekler GnuCOBOL 3.2 ile çalıştırıldı; Java BigDecimal documentation; COBOL initial specifications, US Department of Defense, April 1960; IBM System/360 Principles of Operation; IBM z/Architecture Principles of Operation; IBM 10-K, fiscal 2022; SSA IT Modernization Plan, 2017; GAO-25-107795 (2025); FCA Final Notice to TSB Bank plc (2022); Slaughter and May, TSB Review (2019); TSB 2018 full-year results; Commonwealth Bank of Australia, Recent Developments (2008) ve 2013 Shareholder Review; iTWire ve Delimiter, February 2011; New Jersey Department of Labor, March 2020; New Jersey Office of the State Auditor (2022); WIRED, "Can't File for Unemployment? Don't Blame Cobol" (2020); Mar Hicks, "Built to Last", Logic (2020); Martin Fowler, "StranglerApplication" (2004).

Altyazılar bu video için yazıldı, otomatik olarak oluşturulmadı. İkinci ses parçası olarak Amerikan İngilizcesi de mevcut.

BÖLÜMLER
00:00 Bir peni ekle
00:46 1959'dan kalma bir dil
01:17 Neden baştan yazmıyoruz?
02:22 COBOL oraya nasıl geldi
03:56 Ne kadarı hâlâ çalışıyor
04:41 TSB: bir banka ayrılıyor
06:28 Commonwealth Bank: yavaş yavaş ayrılmak
07:32 New Jersey: herkes COBOL'u suçladı
08:57 Üç vaka
09:34 Sarmala, parça parça değiştir
10:07 Yarım peniye dönüş

GÖRSEL KAYNAKLARI
Grace Hopper and UNIVAC — unknown author, CC BY 2.0
IBM System/360 Model 30 — ArnoldReinhold, CC BY-SA 3.0
TSB Newcastle — TubularWorld, CC BY-SA 3.0
Commonwealth Bank branch office — Maksym Kozlenko, CC BY-SA 4.0
Wikimedia Commons aracılığıyla
Lisanslar: creativecommons.org/licenses/by/2.0, creativecommons.org/licenses/by-sa/3.0, creativecommons.org/licenses/by-sa/4.0
Diğer tüm arşiv görselleri kamu malıdır.
```

## українська (`uk`)

```
Чому банки досі працюють на коді 60-річної давнини?
```

```
Додай один пенні до 999,99 £ у невідповідному полі COBOL — і результат буде нуль. Жодного повідомлення про помилку, жодного збою. Це не баг. Це правило, і багато банків світу досі працюють за такими правилами.

COBOL — це мова програмування 1959 року. То чому ж банки її не замінили, якщо мають і гроші, і інженерів? У цьому відео — чому переписати не означає перекласти і як нарада в Пентагоні дала бізнесу спільну мову, а також три реальні випадки: британський банк, який намагався піти зі старої системи, австралійський банк, якому це вдалося, і криза під час пандемії в Нью-Джерсі, в якій усі звинуватили COBOL.

Джерела: IBM Enterprise COBOL for z/OS 6.4 Language Reference (ROUNDED, SIZE ERROR, assumed decimal point), приклади запущено в GnuCOBOL 3.2; Java BigDecimal documentation; COBOL initial specifications, US Department of Defense, April 1960; IBM System/360 Principles of Operation; IBM z/Architecture Principles of Operation; IBM 10-K, fiscal 2022; SSA IT Modernization Plan, 2017; GAO-25-107795 (2025); FCA Final Notice to TSB Bank plc (2022); Slaughter and May, TSB Review (2019); TSB 2018 full-year results; Commonwealth Bank of Australia, Recent Developments (2008) і 2013 Shareholder Review; iTWire і Delimiter, February 2011; New Jersey Department of Labor, March 2020; New Jersey Office of the State Auditor (2022); WIRED, "Can't File for Unemployment? Don't Blame Cobol" (2020); Mar Hicks, "Built to Last", Logic (2020); Martin Fowler, "StranglerApplication" (2004).

Субтитри написані для цього відео, а не згенеровані автоматично. Також доступна друга звукова доріжка — американською англійською.

РОЗДІЛИ
00:00 Додай один пенні
00:46 Мова 1959 року
01:17 Чому б просто не переписати?
02:22 Як COBOL туди потрапив
03:56 Скільки ще працює
04:41 TSB: банк іде
06:28 Commonwealth Bank: повільний відхід
07:32 Нью-Джерсі: усі звинуватили COBOL
08:57 Три випадки
09:34 Обгорнути й замінювати шматок за шматком
10:07 Повернення до пів пенні

ДЖЕРЕЛА ЗОБРАЖЕНЬ
Grace Hopper and UNIVAC — unknown author, CC BY 2.0
IBM System/360 Model 30 — ArnoldReinhold, CC BY-SA 3.0
TSB Newcastle — TubularWorld, CC BY-SA 3.0
Commonwealth Bank branch office — Maksym Kozlenko, CC BY-SA 4.0
через Wikimedia Commons
Ліцензії: creativecommons.org/licenses/by/2.0, creativecommons.org/licenses/by-sa/3.0, creativecommons.org/licenses/by-sa/4.0
Усі інші архівні зображення є суспільним надбанням.
```

## Tiếng Việt (`vi`)

```
Vì sao các ngân hàng vẫn chạy trên mã 60 năm tuổi?
```

```
Cộng thêm một xu vào 999,99 bảng Anh trong một trường COBOL không phù hợp, và kết quả là số không. Không có thông báo lỗi, không bị treo. Đó không phải là lỗi. Đó là một quy tắc, và nhiều ngân hàng trên thế giới vẫn đang hoạt động theo những quy tắc như vậy.

COBOL là một ngôn ngữ lập trình ra đời năm 1959. Vậy tại sao các ngân hàng chưa thay nó, khi họ có cả tiền lẫn kỹ sư? Video này tìm hiểu vì sao viết lại không phải là dịch, một cuộc họp ở Lầu Năm Góc đã mang đến cho giới kinh doanh ngôn ngữ chung của mình ra sao, và ba trường hợp có thật: một ngân hàng Anh đã cố rời bỏ hệ thống cũ, một ngân hàng Úc đã làm được, và một cuộc khủng hoảng thời đại dịch ở New Jersey mà ai cũng đổ lỗi cho COBOL.

Nguồn: IBM Enterprise COBOL for z/OS 6.4 Language Reference (ROUNDED, SIZE ERROR, assumed decimal point), các ví dụ được chạy trên GnuCOBOL 3.2; Java BigDecimal documentation; COBOL initial specifications, US Department of Defense, April 1960; IBM System/360 Principles of Operation; IBM z/Architecture Principles of Operation; IBM 10-K, fiscal 2022; SSA IT Modernization Plan, 2017; GAO-25-107795 (2025); FCA Final Notice to TSB Bank plc (2022); Slaughter and May, TSB Review (2019); TSB 2018 full-year results; Commonwealth Bank of Australia, Recent Developments (2008) và 2013 Shareholder Review; iTWire và Delimiter, February 2011; New Jersey Department of Labor, March 2020; New Jersey Office of the State Auditor (2022); WIRED, "Can't File for Unemployment? Don't Blame Cobol" (2020); Mar Hicks, "Built to Last", Logic (2020); Martin Fowler, "StranglerApplication" (2004).

Phụ đề được viết riêng cho video này, không phải tạo tự động. Có thể chọn tiếng Anh Mỹ ở bản âm thanh thứ hai.

CHƯƠNG
00:00 Cộng thêm một xu
00:46 Một ngôn ngữ từ năm 1959
01:17 Sao không viết lại luôn?
02:22 COBOL đã đến đó như thế nào
03:56 Còn bao nhiêu đang chạy
04:41 TSB: một ngân hàng rời đi
06:28 Commonwealth Bank: rời đi từ từ
07:32 New Jersey: ai cũng đổ lỗi cho COBOL
08:57 Ba trường hợp
09:34 Bọc lại, thay từng phần một
10:07 Trở lại nửa xu

NGUỒN HÌNH ẢNH
Grace Hopper and UNIVAC — unknown author, CC BY 2.0
IBM System/360 Model 30 — ArnoldReinhold, CC BY-SA 3.0
TSB Newcastle — TubularWorld, CC BY-SA 3.0
Commonwealth Bank branch office — Maksym Kozlenko, CC BY-SA 4.0
qua Wikimedia Commons
Giấy phép: creativecommons.org/licenses/by/2.0, creativecommons.org/licenses/by-sa/3.0, creativecommons.org/licenses/by-sa/4.0
Tất cả các hình ảnh lưu trữ khác thuộc phạm vi công cộng.
```

## čeština (`cs`)

```
Proč banky pořád jedou na 60 let starém kódu?
```

```
Přičti jednu penci k 999,99 £ v nevhodném poli COBOLu a výsledek je nula. Žádné chybové hlášení, žádný pád. To není chyba. Je to pravidlo a spousta bank na světě na takových pravidlech pořád jede.

COBOL je programovací jazyk z roku 1959. Proč ho tedy banky nenahradily, když mají peníze i inženýry? Video ukazuje, proč přepis není překlad a jak schůzka v Pentagonu dala byznysu společný jazyk, a pak prochází tři skutečné případy: britskou banku, která se pokusila opustit starý systém, australskou banku, které se to povedlo, a krizi za pandemie v New Jersey, za kterou všichni vinili COBOL.

Zdroje: IBM Enterprise COBOL for z/OS 6.4 Language Reference (ROUNDED, SIZE ERROR, assumed decimal point), příklady spuštěné v GnuCOBOL 3.2; Java BigDecimal documentation; COBOL initial specifications, US Department of Defense, April 1960; IBM System/360 Principles of Operation; IBM z/Architecture Principles of Operation; IBM 10-K, fiscal 2022; SSA IT Modernization Plan, 2017; GAO-25-107795 (2025); FCA Final Notice to TSB Bank plc (2022); Slaughter and May, TSB Review (2019); TSB 2018 full-year results; Commonwealth Bank of Australia, Recent Developments (2008) a 2013 Shareholder Review; iTWire a Delimiter, February 2011; New Jersey Department of Labor, March 2020; New Jersey Office of the State Auditor (2022); WIRED, "Can't File for Unemployment? Don't Blame Cobol" (2020); Mar Hicks, "Built to Last", Logic (2020); Martin Fowler, "StranglerApplication" (2004).

Titulky jsou psané pro tohle video, ne strojový přepis. Jako druhá zvuková stopa je k dispozici americká angličtina.

KAPITOLY
00:00 Přičti jednu penci
00:46 Jazyk z roku 1959
01:17 Proč to prostě nepřepsat?
02:22 Jak se tam COBOL dostal
03:56 Kolik toho pořád běží
04:41 TSB: banka odchází
06:28 Commonwealth Bank: pomalý odchod
07:32 New Jersey: všichni vinili COBOL
08:57 Tři případy
09:34 Obalit a nahrazovat kus po kusu
10:07 Zpátky k půl penci

ZDROJE OBRÁZKŮ
Grace Hopper and UNIVAC — unknown author, CC BY 2.0
IBM System/360 Model 30 — ArnoldReinhold, CC BY-SA 3.0
TSB Newcastle — TubularWorld, CC BY-SA 3.0
Commonwealth Bank branch office — Maksym Kozlenko, CC BY-SA 4.0
prostřednictvím Wikimedia Commons
Licence: creativecommons.org/licenses/by/2.0, creativecommons.org/licenses/by-sa/3.0, creativecommons.org/licenses/by-sa/4.0
Všechny ostatní archivní snímky jsou volná díla.
```

## español (`es`)

```
¿Por qué los bancos siguen funcionando con código de hace 60 años?
```

```
Súmale un penique a 999,99 £ en el campo de COBOL equivocado y el resultado es cero. Ni mensaje de error ni cuelgue. No es un fallo. Es una regla, y muchos bancos del mundo siguen funcionando con reglas así.

COBOL es un lenguaje de programación de 1959. Entonces, ¿por qué los bancos no lo han sustituido, si tienen el dinero y los ingenieros? Este vídeo explica por qué reescribir no es traducir y cómo una reunión en el Pentágono dio al mundo empresarial su lengua común, y después repasa tres casos reales: un banco británico que intentó dejar su sistema antiguo, un banco australiano que lo consiguió, y una crisis durante la pandemia en Nueva Jersey en la que todos culparon a COBOL.

Fuentes: IBM Enterprise COBOL for z/OS 6.4 Language Reference (ROUNDED, SIZE ERROR, assumed decimal point), con los ejemplos ejecutados en GnuCOBOL 3.2; Java BigDecimal documentation; COBOL initial specifications, US Department of Defense, April 1960; IBM System/360 Principles of Operation; IBM z/Architecture Principles of Operation; IBM 10-K, fiscal 2022; SSA IT Modernization Plan, 2017; GAO-25-107795 (2025); FCA Final Notice to TSB Bank plc (2022); Slaughter and May, TSB Review (2019); TSB 2018 full-year results; Commonwealth Bank of Australia, Recent Developments (2008) y 2013 Shareholder Review; iTWire y Delimiter, February 2011; New Jersey Department of Labor, March 2020; New Jersey Office of the State Auditor (2022); WIRED, "Can't File for Unemployment? Don't Blame Cobol" (2020); Mar Hicks, "Built to Last", Logic (2020); Martin Fowler, "StranglerApplication" (2004).

Los subtítulos están escritos para este vídeo, no generados automáticamente. Como segunda pista de audio está disponible el inglés americano.

CAPÍTULOS
00:00 Súmale un penique
00:46 Un lenguaje de 1959
01:17 ¿Por qué no reescribirlo sin más?
02:22 Cómo llegó COBOL hasta ahí
03:56 Cuánto sigue funcionando
04:41 TSB: un banco se va
06:28 Commonwealth Bank: irse despacio
07:32 Nueva Jersey: todos culparon a COBOL
08:57 Tres casos
09:34 Envolverlo y sustituirlo pieza a pieza
10:07 De vuelta al medio penique

CRÉDITOS DE LAS IMÁGENES
Grace Hopper and UNIVAC — unknown author, CC BY 2.0
IBM System/360 Model 30 — ArnoldReinhold, CC BY-SA 3.0
TSB Newcastle — TubularWorld, CC BY-SA 3.0
Commonwealth Bank branch office — Maksym Kozlenko, CC BY-SA 4.0
vía Wikimedia Commons
Licencias: creativecommons.org/licenses/by/2.0, creativecommons.org/licenses/by-sa/3.0, creativecommons.org/licenses/by-sa/4.0
Todas las demás imágenes de archivo son de dominio público.
```

## svenska (`sv`)

```
Varför kör bankerna fortfarande 60 år gammal kod?
```

```
Lägg till en penny till 999,99 £ i fel COBOL-fält, och svaret blir noll. Inget felmeddelande, ingen krasch. Det är ingen bugg. Det är en regel, och många av världens banker fungerar fortfarande enligt sådana regler.

COBOL är ett programspråk från 1959. Så varför har bankerna inte ersatt det, när de har både pengarna och ingenjörerna? Den här videon visar varför en omskrivning inte är en översättning och hur ett möte i Pentagon gav affärsvärlden ett gemensamt språk. Sedan tre verkliga fall: en brittisk bank som försökte lämna sitt gamla system, en australisk bank som lyckades, och en kris under pandemin i New Jersey där alla skyllde på COBOL.

Källor: IBM Enterprise COBOL for z/OS 6.4 Language Reference (ROUNDED, SIZE ERROR, assumed decimal point), med exemplen körda i GnuCOBOL 3.2; Java BigDecimal documentation; COBOL initial specifications, US Department of Defense, April 1960; IBM System/360 Principles of Operation; IBM z/Architecture Principles of Operation; IBM 10-K, fiscal 2022; SSA IT Modernization Plan, 2017; GAO-25-107795 (2025); FCA Final Notice to TSB Bank plc (2022); Slaughter and May, TSB Review (2019); TSB 2018 full-year results; Commonwealth Bank of Australia, Recent Developments (2008) och 2013 Shareholder Review; iTWire och Delimiter, February 2011; New Jersey Department of Labor, March 2020; New Jersey Office of the State Auditor (2022); WIRED, "Can't File for Unemployment? Don't Blame Cobol" (2020); Mar Hicks, "Built to Last", Logic (2020); Martin Fowler, "StranglerApplication" (2004).

Undertexterna är skrivna för den här videon, inte automatgenererade. Som andra ljudspår finns amerikansk engelska.

KAPITEL
00:00 Lägg till en penny
00:46 Ett språk från 1959
01:17 Varför inte bara skriva om det?
02:22 Hur COBOL hamnade där
03:56 Hur mycket som fortfarande körs
04:41 TSB: en bank lämnar
06:28 Commonwealth Bank: att lämna långsamt
07:32 New Jersey: alla skyllde på COBOL
08:57 Tre fall
09:34 Kapsla in, ersätt bit för bit
10:07 Tillbaka till den halva pennyn

BILDKÄLLOR
Grace Hopper and UNIVAC — unknown author, CC BY 2.0
IBM System/360 Model 30 — ArnoldReinhold, CC BY-SA 3.0
TSB Newcastle — TubularWorld, CC BY-SA 3.0
Commonwealth Bank branch office — Maksym Kozlenko, CC BY-SA 4.0
via Wikimedia Commons
Licenser: creativecommons.org/licenses/by/2.0, creativecommons.org/licenses/by-sa/3.0, creativecommons.org/licenses/by-sa/4.0
Alla övriga arkivbilder är fria från upphovsrätt (public domain).
```
