# Lokalizované názvy a popisy — 063

Čte to `tools/lokalizace.py`. Formát a pořadí sekcí popisuje
`docs/zverejneni.md`; **pořadí je podle Studia**, tedy bajtově podle
UTF-8 českého názvu jazyka — proto jsou čeština, španělština
a švédština nakonec.

## Co se NEPŘEKLÁDÁ

- **Vlastní jména**: Trump, AfD, Fico, Mudde, Algan, Guriev,
  Papaioannou, Passari, Pew Research Center, Brookings.
- **Názvy citovaných prací** — zůstávají anglicky, protože se podle nich
  hledá.
- **Časy kapitol** na vteřinu. Názvy kapitol se překládají.
- **Tagy** — YouTube je per-jazyk nemá.

## Kontrola čísel

Desetinná čárka místo tečky všude, kde to jazyk má: **49,8 / 20,8**
v cs, de, fr, it, pl, pt-BR, es, sv, fi, tr, uk, vi; tečka zůstává
v `id` (indonéština používá čárku — tedy **49,8** i tam) a v angličtině.
Celá čísla (73, 17, 35, 9, 11, 26, 220, 2017, 1958, 2025) se nemění.

## Jméno strany

Anglicky *Direction – Social Democracy*. V češtině se používá **slovenský
originál `Smer – sociálna demokracia`**, protože český divák ho zná;
jinde překlad do daného jazyka, protože originál nikomu nic neřekne.

## Registr

Čeština **vyká** (viz `notes.md`). Stejně tak němčina `Sie`,
ukrajinština `ви`, turečtina `siz`, indonéština `Anda`. Finština drží
`sinä`, vietnamština `bạn` — tam ta volba není.

---

## suomi (`fi`)

```
Miksi ihmiset äänestävät populisteja yhä uudelleen?
```

```
Kolme poliitikkoa, kolme maata, eikä juuri mitään muuta yhteistä. Donald Trump voitti Yhdysvaltain kansanäänestyksen 49,8 prosentilla. AfD nousi Saksassa toiseksi 20,8 prosentilla, kaksinkertaistaen vuoden 2021 tuloksensa. Robert Ficosta tuli Slovakian pääministeri neljättä kertaa – ja hänen puolueensa nimi on Suunta – sosiaalidemokratia, ja se kuului Euroopan sosialistipuolueiden perheeseen vuoteen 2023 asti.

He ovat eri mieltä keskenään lähes kaikesta. Heidän allaan oleva koneisto on lähes identtinen.

Tämä video kertoo siitä koneistosta. Ei siitä, kuka on oikeassa.

Politiikan tutkijat käyttävät sanaa kapeammin kuin me. Populismi siinä mielessä ei ole lainkaan poliittinen ohjelma. Se on yksi väite siitä, kuka sinä olet: että yhteiskunta jakautuu tavallisiin ihmisiin ja eliittiin, joka on ottanut järjestelmän haltuunsa ja pyörittää sitä nyt itselleen. Se on niin ohut ajatus, että se mahtuu lähes minkä tahansa politiikan sisään – siksi vasemmistolainen ja oikeistolainen versio nimeävät täysin eri eliitin ja rakentavat silti saman lauseen.

Ja se toimii parhaiten silloin, kun ongelma on aito. Asunnot, joihin kenelläkään nuorella ei ole varaa, terveydenhuolto, joka maksaa joka vuosi enemmän, hiljaa rapistuva infrastruktuuri. Mitään siitä ei tarvitse liioitella. Populistin ei tarvitse keksiä ongelmaa – vain selittää se, ja selitys on aina yhden sanan mittainen.

Sitten on mittaus, eikä se kerro sitä mitä odottaisi. Vuonna 2017 neljä taloustieteilijää seurasi 220:tä Euroopan aluetta finanssikriisin läpi. Siellä missä työttömyys nousi, nousivat myös äänet valtavirran ulkopuolisille puolueille, ja luottamus kansallisiin parlamentteihin ja EU:n instituutioihin laski. Mutta asenteet maahanmuuttajia kohtaan eivät juuri liikkuneet, eivätkä ne kulttuurin osalta koventuneet – pikemminkin eurooppalaiset tulivat kriisistä ulos hieman avoimempina. Se keskustelu jota kaikki kävivät, ja se mikä todella liikutti ääniä, olivat kaksi eri asiaa.

Vuonna 1958 73 prosenttia amerikkalaisista sanoi luottavansa siihen, että Washingtonin hallitus tekee oikein. Syyskuuhun 2025 mennessä luku oli 17. Ja kuudessatoista kuukaudessa puolueiden kannattajien luottamusluvut vaihtoivat järjestystä: demokraateilla 35:stä 9:ään, republikaaneilla 11:stä 26:een. Asukas vaihtui. Se luku ei siis koskaan mitannut suoriutumista.

Mikä johtaa siihen osaan, jota melkein kukaan ei sano ääneen. Populistin ei tarvitse vakuuttaa sinua siitä, että yksinkertainen ratkaisu toimii – se olisi vaikeaa, koska ratkaisut voi tarkistaa. Vain siitä, että nykyinen on jo epäonnistunut. Ja se on paljon helpompaa, koska varsin usein se on yksinkertaisesti totta.

Luvut
0:00 Yksinkertaisia vastauksia monimutkaisiin ongelmiin
0:29 Trump. AfD. Fico.
1:21 Ei oikealla. Vasemmalla.
1:51 Mitä populismi tutkimuksessa tarkoittaa
2:49 Miksi aito ongelma toimii paremmin
3:45 Mikä todella liikutti ääniä
5:03 Sinulla oli tilaisuutesi
5:30 Seitsemänkymmentäkolme prosenttia, ja seitsemäntoista
6:10 Mitä meillä on hävittävää?
6:30 Koko temppu
6:51 Miksi iskulause voittaa
7:32 Ei yhtä syyllistä, ei yhtä ratkaisua
8:06 Miksi se palaa aina
8:34 Asukas vaihtui
9:20 Oire, ei tauti
9:44 Mitä tapahtui ennen kuin he äänestivät

Lähteet: Mudde, "The Populist Zeitgeist" (2004). Algan, Guriev, Papaioannou & Passari, "The European Trust Crisis and the Rise of Populism", Brookings Papers on Economic Activity (2017). Pew Research Center, "Public Trust in Government: 1958-2025".

Tekstitykset on kirjoitettu tätä videota varten, ei koneellisesti. Amerikanenglanninkielinen ääniraita on saatavilla toisena ääniraitana.

Musiikki tuotetaan tälle kanavalle proseduraalisesti.
```

## français (`fr`)

```
Pourquoi les gens continuent-ils à voter pour des populistes ?
```

```
Trois responsables politiques, trois pays, et presque rien d'autre en commun. Donald Trump a remporté le vote populaire américain avec 49,8 pour cent. L'AfD est arrivée deuxième en Allemagne avec 20,8 pour cent, le double de son résultat de 2021. Robert Fico est devenu premier ministre slovaque pour la quatrième fois – et son parti s'appelle Direction – social-démocratie, et il a fait partie de la famille des partis socialistes européens jusqu'en 2023.

Ils sont en désaccord entre eux sur presque tout. La machinerie qui les porte est pratiquement identique.

Cette vidéo parle de cette machinerie. Pas de qui a raison.

Les politologues emploient le mot plus étroitement que nous. Le populisme, en ce sens, n'est pas du tout un programme politique. C'est une seule affirmation sur qui vous êtes : que la société se divise entre les gens ordinaires et une élite qui s'est emparée du système et le fait tourner pour elle-même. L'idée est assez étroite pour se greffer sur presque n'importe quelle politique, et c'est pourquoi une version de gauche et une version de droite désignent une élite complètement différente et construisent pourtant la même phrase.

Et cela marche le mieux quand le problème est réel. Un logement qu'aucun jeune ne peut se payer, des soins qui coûtent plus cher chaque année, des infrastructures qui se dégradent en silence. Rien de tout cela n'a besoin d'être exagéré. Le populiste n'a pas à inventer le problème – seulement à l'expliquer, et l'explication tient toujours en un mot.

Puis il y a une mesure, et elle ne dit pas ce qu'on attendrait. En 2017, quatre économistes ont suivi 220 régions européennes à travers la crise financière. Là où le chômage montait, les voix pour les partis anti-système montaient avec lui, et la confiance dans les parlements nationaux et les institutions européennes baissait. Mais les attitudes envers les immigrés n'ont presque pas bougé, et sur le plan culturel elles ne se sont pas durcies – si changement il y a eu, les Européens sont sortis de la crise légèrement plus ouverts. Le débat que tout le monde menait et ce qui déplaçait réellement les voix étaient deux choses différentes.

En 1958, 73 pour cent des Américains disaient faire confiance au gouvernement de Washington pour faire ce qui est juste. En septembre 2025, c'était 17. Et en seize mois, les niveaux de confiance des démocrates et des républicains se sont inversés : les démocrates de 35 à 9, les républicains de 11 à 26. L'occupant a changé. Ce chiffre ne mesurait donc jamais la performance.

Ce qui mène à la partie que presque personne ne dit à voix haute. Un populiste n'a pas à vous convaincre que la solution simple va marcher – ce serait difficile, parce que les solutions peuvent être vérifiées. Seulement que l'actuelle a déjà échoué. Et ce travail est bien plus facile, parce que très souvent c'est simplement vrai.

Chapitres
0:00 Des réponses simples à des problèmes compliqués
0:29 Trump. L'AfD. Fico.
1:21 Pas à droite. À gauche.
1:51 Ce que le populisme veut dire dans la recherche
2:49 Pourquoi un vrai problème marche mieux
3:45 Ce qui déplaçait réellement les voix
5:03 Vous avez eu votre chance
5:30 Soixante-treize pour cent, et dix-sept
6:10 Qu'avons-nous à perdre ?
6:30 Toute l'astuce
6:51 Pourquoi un slogan l'emporte
7:32 Pas de coupable unique, pas de solution unique
8:06 Pourquoi cela revient toujours
8:34 L'occupant a changé
9:20 Un symptôme, pas la maladie
9:44 Ce qui s'est passé avant leur vote

Sources : Mudde, "The Populist Zeitgeist" (2004). Algan, Guriev, Papaioannou & Passari, "The European Trust Crisis and the Rise of Populism", Brookings Papers on Economic Activity (2017). Pew Research Center, "Public Trust in Government: 1958-2025".

Les sous-titres sont rédigés pour cette vidéo, ils ne sont pas générés automatiquement. Une piste audio en anglais américain est disponible comme deuxième piste audio.

La musique est générée de façon procédurale pour cette chaîne.
```

## Bahasa Indonesia (`id`)

```
Mengapa Orang Terus Memilih Populis?
```

```
Tiga politikus, tiga negara, dan hampir tidak ada kesamaan lain. Donald Trump memenangkan suara populer Amerika dengan 49,8 persen. AfD menempati posisi kedua di Jerman dengan 20,8 persen, dua kali lipat hasilnya pada 2021. Robert Fico menjadi perdana menteri Slovakia untuk keempat kalinya – dan partainya bernama Arah – Demokrasi Sosial, dan partai itu berada di dalam keluarga partai-partai sosialis Eropa sampai 2023.

Mereka berselisih satu sama lain dalam hampir segala hal. Mesin yang bekerja di bawah mereka nyaris identik.

Video ini tentang mesin itu. Bukan tentang siapa yang benar.

Ilmuwan politik memakai kata itu lebih sempit daripada kita. Populisme dalam pengertian itu sama sekali bukan program kebijakan. Ia adalah satu klaim tentang siapa Anda: bahwa masyarakat terbelah menjadi orang biasa dan elite yang telah mengambil alih sistem dan kini menjalankannya untuk dirinya sendiri. Gagasan itu cukup sempit untuk menempel pada hampir semua aliran politik, dan karena itulah versi kiri dan versi kanan menyebut elite yang sama sekali berbeda namun tetap menyusun kalimat yang sama.

Dan itu paling ampuh justru ketika masalahnya nyata. Perumahan yang tak terjangkau anak muda, layanan kesehatan yang makin mahal tiap tahun, infrastruktur yang lapuk diam-diam. Tidak ada satu pun dari itu yang perlu dilebih-lebihkan. Sang populis tidak perlu mengarang masalahnya – hanya menjelaskannya, dan penjelasannya selalu sepanjang satu kata.

Lalu ada pengukurannya, dan hasilnya bukan yang Anda duga. Pada 2017 empat ekonom menelusuri 220 wilayah Eropa melewati krisis keuangan. Di tempat pengangguran naik, suara untuk partai anti-kemapanan ikut naik, dan kepercayaan pada parlemen nasional serta lembaga Eropa turun. Tetapi sikap terhadap imigran hampir tidak bergeser, dan soal budaya justru tidak mengeras – kalaupun ada, orang Eropa keluar dari krisis sedikit lebih terbuka. Perdebatan yang diikuti semua orang dan hal yang benar-benar menggerakkan suara adalah dua hal yang berbeda.

Pada 1958, 73 persen orang Amerika menyatakan percaya bahwa pemerintah di Washington melakukan hal yang benar. Pada September 2025 tinggal 17. Dan dalam enam belas bulan tingkat kepercayaan pendukung kedua partai bertukar tempat: Demokrat dari 35 ke 9, Republik dari 11 ke 26. Penghuninya berganti. Jadi angka itu tidak pernah mengukur kinerja.

Yang membawa kita ke bagian yang hampir tak pernah diucapkan. Seorang populis tidak perlu meyakinkan Anda bahwa solusi sederhana itu akan berhasil – itu sulit, karena solusi bisa diperiksa. Cukup meyakinkan bahwa yang sekarang sudah gagal. Dan pekerjaan itu jauh lebih mudah, karena cukup sering hal itu memang benar.

Bab
0:00 Jawaban sederhana untuk masalah rumit
0:29 Trump. AfD. Fico.
1:21 Bukan di kanan. Di kiri.
1:51 Apa arti populisme dalam penelitian
2:49 Mengapa masalah nyata bekerja lebih baik
3:45 Apa yang benar-benar menggerakkan suara
5:03 Anda sudah diberi kesempatan
5:30 Tujuh puluh tiga persen, dan tujuh belas
6:10 Apa yang bisa kita kehilangan?
6:30 Seluruh triknya
6:51 Mengapa slogan menang
7:32 Tak ada satu penjahat, tak ada satu solusi
8:06 Mengapa ini terus kembali
8:34 Penghuninya berganti
9:20 Gejala, bukan penyakit
9:44 Apa yang terjadi sebelum mereka memilih

Sumber: Mudde, "The Populist Zeitgeist" (2004). Algan, Guriev, Papaioannou & Passari, "The European Trust Crisis and the Rise of Populism", Brookings Papers on Economic Activity (2017). Pew Research Center, "Public Trust in Government: 1958-2025".

Subtitel ditulis khusus untuk video ini, bukan dibuat otomatis. Trek audio bahasa Inggris Amerika tersedia sebagai trek audio kedua.

Musik dibuat secara prosedural untuk kanal ini.
```

## italiano (`it`)

```
Perché la gente continua a votare i populisti?
```

```
Tre politici, tre paesi e quasi nient'altro in comune. Donald Trump ha vinto il voto popolare americano con il 49,8 per cento. L'AfD è arrivata seconda in Germania con il 20,8 per cento, il doppio del suo risultato del 2021. Robert Fico è diventato primo ministro slovacco per la quarta volta – e il suo partito si chiama Direzione – Socialdemocrazia, ed è rimasto dentro la famiglia dei partiti socialisti europei fino al 2023.

Fra loro sono in disaccordo su quasi tutto. Il meccanismo alla base del loro successo è quasi identico.

Questo video parla di quel meccanismo. Non di chi ha ragione.

I politologi usano la parola in modo più stretto di noi. Il populismo, in quel senso, non è affatto un programma di governo. È una sola affermazione su chi sei tu: che la società si divide fra la gente comune e un'élite che si è presa il sistema e ora lo fa girare per sé. È un'idea abbastanza ristretta da innestarsi su quasi qualunque politica, ed è per questo che una versione di sinistra e una di destra nominano un'élite completamente diversa e costruiscono comunque la stessa frase.

E funziona meglio quando il problema è vero. Case che nessun giovane può permettersi, sanità che costa di più ogni anno, infrastrutture che marciscono in silenzio. Niente di tutto questo ha bisogno di essere esagerato. Il populista non deve inventare il problema – solo spiegarlo, e la spiegazione è sempre lunga una parola.

Poi c'è una misura, e non dice quello che ti aspetteresti. Nel 2017 quattro economisti hanno seguito 220 regioni europee attraverso la crisi finanziaria. Dove la disoccupazione saliva, salivano con lei i voti per i partiti anti-establishment, e calava la fiducia nei parlamenti nazionali e nelle istituzioni europee. Ma gli atteggiamenti verso gli immigrati non si sono quasi mossi, e sul piano culturale non si sono induriti – semmai gli europei sono usciti dalla crisi leggermente più aperti. Il dibattito che tutti stavano facendo e la cosa che spostava davvero i voti erano due cose diverse.

Nel 1958 il 73 per cento degli americani diceva di fidarsi che il governo di Washington facesse la cosa giusta. A settembre 2025 era il 17. E in sedici mesi i livelli di fiducia fra democratici e repubblicani si sono invertiti: democratici da 35 a 9, repubblicani da 11 a 26. È cambiato l'inquilino. Quel numero, quindi, non stava misurando i risultati.

Il che porta alla parte che quasi nessuno dice ad alta voce. Un populista non deve convincerti che la soluzione semplice funzionerà – sarebbe difficile, perché le soluzioni si possono verificare. Solo che quella attuale ha già fallito. E questo è molto più facile, perché molto spesso è semplicemente vero.

Capitoli
0:00 Risposte semplici a problemi complicati
0:29 Trump. L'AfD. Fico.
1:21 Non a destra. A sinistra.
1:51 Che cosa significa populismo nella ricerca
2:49 Perché un problema vero funziona meglio
3:45 Che cosa spostava davvero i voti
5:03 Avete avuto la vostra occasione
5:30 Settantatré per cento, e diciassette
6:10 Che cosa abbiamo da perdere?
6:30 Tutto il trucco
6:51 Perché vince uno slogan
7:32 Nessun colpevole unico, nessuna soluzione unica
8:06 Perché continua a tornare
8:34 È cambiato l'inquilino
9:20 Sintomo, non malattia
9:44 Che cosa è successo prima che votassero

Fonti: Mudde, "The Populist Zeitgeist" (2004). Algan, Guriev, Papaioannou & Passari, "The European Trust Crisis and the Rise of Populism", Brookings Papers on Economic Activity (2017). Pew Research Center, "Public Trust in Government: 1958-2025".

I sottotitoli sono scritti per questo video, non generati automaticamente. È disponibile una traccia audio in inglese americano come seconda traccia audio.

La musica è generata in modo procedurale per questo canale.
```

## Deutsch (`de`)

```
Warum wählen Menschen immer wieder Populisten?
```

```
Drei Politiker, drei Länder und sonst fast nichts gemeinsam. Donald Trump gewann die amerikanische Volksabstimmung mit 49,8 Prozent. Die AfD wurde in Deutschland mit 20,8 Prozent zweitstärkste Kraft, doppelt so viel wie 2021. Robert Fico wurde zum vierten Mal slowakischer Ministerpräsident – und seine Partei heißt Richtung – Sozialdemokratie und gehörte bis 2023 zur Familie der europäischen sozialistischen Parteien.

Untereinander sind sie sich in fast allem uneinig. Die Maschinerie darunter ist nahezu identisch.

In diesem Video geht es um diese Maschinerie. Nicht darum, wer recht hat.

Politikwissenschaftler benutzen das Wort enger als wir. Populismus in diesem Sinn ist überhaupt kein Programm. Er ist eine einzige Behauptung darüber, wer Sie sind: dass die Gesellschaft in einfache Leute und eine Elite zerfällt, die sich das System genommen hat und es nun für sich betreibt. Das ist dünn genug, um in fast jede Politik zu passen – deshalb benennen eine linke und eine rechte Fassung eine völlig andere Elite und bauen trotzdem denselben Satz.

Und es funktioniert am besten, wenn das Problem echt ist. Wohnungen, die sich kein junger Mensch leisten kann, eine Gesundheitsversorgung, die jedes Jahr mehr kostet, Infrastruktur, die still verrottet. Nichts davon muss übertrieben werden. Der Populist muss das Problem nicht erfinden – nur erklären, und die Erklärung ist immer ein Wort lang.

Dann gibt es eine Messung, und sie sagt nicht das, was man erwarten würde. 2017 verfolgten vier Ökonomen 220 europäische Regionen durch die Finanzkrise. Wo die Arbeitslosigkeit stieg, stiegen die Stimmen für Anti-Establishment-Parteien mit, und das Vertrauen in nationale Parlamente und europäische Institutionen fiel. Die Einstellungen gegenüber Zuwanderern bewegten sich dagegen kaum, und kulturell verhärteten sie sich nicht – wenn überhaupt, kamen die Europäer etwas offener aus der Krise. Die Debatte, die alle führten, und das, was die Stimmen tatsächlich bewegte, waren zwei verschiedene Dinge.

1958 sagten 73 Prozent der Amerikaner, sie vertrauten darauf, dass die Regierung in Washington das Richtige tut. Im September 2025 waren es 17. Und in sechzehn Monaten kehrte sich das Verhältnis zwischen Demokraten und Republikanern um: Demokraten von 35 auf 9, Republikaner von 11 auf 26. Der Bewohner des Weißen Hauses wechselte. Diese Zahl hat also nie Leistung gemessen.

Was zu dem Teil führt, den fast niemand laut ausspricht. Ein Populist muss Sie nicht davon überzeugen, dass die einfache Lösung funktionieren wird – das wäre schwer, denn Lösungen lassen sich überprüfen. Nur davon, dass die jetzige bereits gescheitert ist. Und das ist viel leichter, weil es ziemlich oft schlicht stimmt.

Kapitel
0:00 Einfache Antworten auf komplizierte Probleme
0:29 Trump. Die AfD. Fico.
1:21 Nicht rechts. Links.
1:51 Was Populismus in der Forschung heißt
2:49 Warum ein echtes Problem besser funktioniert
3:45 Was die Stimmen tatsächlich bewegte
5:03 Sie hatten Ihre Chance
5:30 Dreiundsiebzig Prozent, und siebzehn
6:10 Was haben wir zu verlieren?
6:30 Der ganze Trick
6:51 Warum ein Slogan gewinnt
7:32 Kein einzelner Schuldiger, keine einzelne Lösung
8:06 Warum es immer wiederkommt
8:34 Der Bewohner des Weißen Hauses wechselte
9:20 Symptom, nicht Krankheit
9:44 Was geschah, bevor sie so wählten

Quellen: Mudde, "The Populist Zeitgeist" (2004). Algan, Guriev, Papaioannou & Passari, "The European Trust Crisis and the Rise of Populism", Brookings Papers on Economic Activity (2017). Pew Research Center, "Public Trust in Government: 1958-2025".

Die Untertitel wurden für dieses Video geschrieben, nicht automatisch erzeugt. Eine amerikanisch-englische Tonspur ist als zweite Tonspur verfügbar.

Die Musik wird für diesen Kanal prozedural erzeugt.
```

## polski (`pl`)

```
Dlaczego ludzie wciąż głosują na populistów?
```

```
Trzej politycy, trzy kraje i prawie nic więcej wspólnego. Donald Trump wygrał amerykańskie głosowanie powszechne z wynikiem 49,8 procent. AfD zajęła w Niemczech drugie miejsce z 20,8 procent, dwa razy więcej niż w 2021. Robert Fico został premierem Słowacji po raz czwarty – a jego partia nazywa się Kierunek – Socjaldemokracja i do 2023 roku należała do rodziny europejskich partii socjalistycznych.

Między sobą nie zgadzają się niemal we wszystkim. Maszyneria pod nimi jest prawie identyczna.

Ten film jest o tej maszynerii. Nie o tym, kto ma rację.

Politolodzy używają tego słowa węziej niż my. Populizm w tym sensie nie jest wcale programem politycznym. To jedno twierdzenie o tym, kim jesteś: że społeczeństwo dzieli się na zwykłych ludzi i elitę, która przejęła system i teraz prowadzi go dla siebie. To na tyle cienka idea, że mieści się w niemal każdej polityce – i dlatego wersja lewicowa i prawicowa wskazują zupełnie inną elitę, a i tak budują to samo zdanie.

A działa najlepiej wtedy, gdy problem jest prawdziwy. Mieszkania, na które nie stać żadnego młodego człowieka, ochrona zdrowia droższa z roku na rok, infrastruktura po cichu niszczejąca. Nic z tego nie musi być wyolbrzymione. Populista nie musi wymyślać problemu – wystarczy, że go wyjaśni, a wyjaśnienie zawsze ma długość jednego słowa.

Potem jest pomiar i mówi coś innego, niż można by się spodziewać. W 2017 czterech ekonomistów prześledziło 220 europejskich regionów w trakcie kryzysu finansowego. Tam, gdzie rosło bezrobocie, rosły też głosy na partie antysystemowe, a zaufanie do parlamentów krajowych i instytucji europejskich spadało. Ale postawy wobec imigrantów prawie się nie zmieniły, a w sprawach kultury wcale się nie zaostrzyły – jeśli już, Europejczycy wyszli z kryzysu odrobinę bardziej otwarci. Spór, który wszyscy toczyli, i to, co naprawdę przesuwało głosy, były dwiema różnymi rzeczami.

W 1958 roku 73 procent Amerykanów mówiło, że ufa, iż rząd w Waszyngtonie robi to, co słuszne. We wrześniu 2025 było to 17. A w szesnaście miesięcy poziomy zaufania wśród demokratów i republikanów zamieniły się miejscami: demokraci z 35 na 9, republikanie z 11 na 26. Zmienił się lokator. Ta liczba nigdy więc nie mierzyła skuteczności.

Co prowadzi do części, której prawie nikt nie mówi na głos. Populista nie musi przekonywać cię, że proste rozwiązanie zadziała – to byłoby trudne, bo rozwiązania da się sprawdzić. Wystarczy, że przekona cię, iż obecne już zawiodło. A to jest dużo łatwiejsze, bo całkiem często to po prostu prawda.

Rozdziały
0:00 Proste odpowiedzi na skomplikowane problemy
0:29 Trump. AfD. Fico.
1:21 Nie po prawej. Po lewej.
1:51 Co populizm znaczy w badaniach
2:49 Dlaczego prawdziwy problem działa lepiej
3:45 Co naprawdę przesuwało głosy
5:03 Mieliście swoją szansę
5:30 Siedemdziesiąt trzy procent, i siedemnaście
6:10 Co mamy do stracenia?
6:30 Cała sztuczka
6:51 Dlaczego wygrywa hasło
7:32 Nie ma jednego winnego ani jednego rozwiązania
8:06 Dlaczego to wciąż wraca
8:34 Zmienił się lokator
9:20 Objaw, nie choroba
9:44 Co wydarzyło się, zanim zagłosowali

Źródła: Mudde, "The Populist Zeitgeist" (2004). Algan, Guriev, Papaioannou & Passari, "The European Trust Crisis and the Rise of Populism", Brookings Papers on Economic Activity (2017). Pew Research Center, "Public Trust in Government: 1958-2025".

Napisy zostały napisane do tego filmu, nie wygenerowane automatycznie. Dostępna jest ścieżka dźwiękowa w amerykańskiej odmianie angielskiego jako druga ścieżka.

Muzyka jest generowana proceduralnie dla tego kanału.
```

## português (Brasil) (`pt-BR`)

```
Por que as pessoas continuam votando em populistas?
```

```
Três políticos, três países e quase nada mais em comum. Donald Trump venceu o voto popular americano com 49,8 por cento. A AfD ficou em segundo lugar na Alemanha com 20,8 por cento, o dobro do resultado de 2021. Robert Fico tornou-se primeiro-ministro da Eslováquia pela quarta vez – e o partido dele se chama Direção – Social-Democracia, e esteve dentro da família dos partidos socialistas europeus até 2023.

Entre si discordam em quase tudo. A maquinaria por baixo deles é quase idêntica.

Este vídeo é sobre essa maquinaria. Não sobre quem tem razão.

Os cientistas políticos usam a palavra de forma mais estreita do que nós. Populismo, nesse sentido, não é um programa de governo. É uma única afirmação sobre quem você é: que a sociedade se divide entre as pessoas comuns e uma elite que tomou o sistema e agora o faz funcionar para si mesma. A ideia é estreita o bastante para se encaixar em quase qualquer política, e é por isso que uma versão de esquerda e uma de direita apontam uma elite completamente diferente e ainda assim constroem a mesma frase.

E funciona melhor quando o problema é real. Moradia que nenhum jovem consegue pagar, saúde que custa mais a cada ano, infraestrutura apodrecendo em silêncio. Nada disso precisa ser exagerado. O populista não precisa inventar o problema – só explicá-lo, e a explicação se resume sempre a uma palavra.

Depois há uma medição, e ela não diz o que você esperaria. Em 2017, quatro economistas acompanharam 220 regiões europeias ao longo da crise financeira. Onde o desemprego subia, os votos em partidos antiestablishment subiam junto, e a confiança nos parlamentos nacionais e nas instituições europeias caía. Mas as atitudes em relação aos imigrantes quase não se moveram, e no plano cultural não endureceram – se tanto, os europeus saíram da crise um pouco mais abertos. O debate que todos travavam e aquilo que de fato movia os votos eram duas coisas diferentes.

Em 1958, 73 por cento dos americanos diziam confiar que o governo em Washington faria o que é certo. Em setembro de 2025 eram 17. E em dezesseis meses os níveis de confiança entre democratas e republicanos se inverteram: democratas de 35 para 9, republicanos de 11 para 26. O ocupante mudou. Ou seja, aquele número nunca mediu desempenho.

O que leva à parte que quase ninguém diz em voz alta. Um populista não precisa convencer você de que a solução simples vai funcionar – isso seria difícil, porque soluções podem ser verificadas. Só de que a atual já fracassou. E esse trabalho é bem mais fácil, porque muitas vezes é simplesmente verdade.

Capítulos
0:00 Respostas simples para problemas complicados
0:29 Trump. A AfD. Fico.
1:21 Não à direita. À esquerda.
1:51 O que populismo significa na pesquisa
2:49 Por que um problema real funciona melhor
3:45 O que de fato movia os votos
5:03 Vocês tiveram sua chance
5:30 Setenta e três por cento, e dezessete
6:10 O que temos a perder?
6:30 O truque inteiro
6:51 Por que um slogan vence
7:32 Nenhum vilão único, nenhuma solução única
8:06 Por que isso sempre volta
8:34 O ocupante mudou
9:20 Sintoma, não doença
9:44 O que aconteceu antes de eles votarem

Fontes: Mudde, "The Populist Zeitgeist" (2004). Algan, Guriev, Papaioannou & Passari, "The European Trust Crisis and the Rise of Populism", Brookings Papers on Economic Activity (2017). Pew Research Center, "Public Trust in Government: 1958-2025".

As legendas foram escritas para este vídeo, não geradas automaticamente. Há uma faixa de áudio em inglês americano disponível como segunda faixa de áudio.

A música é gerada proceduralmente para este canal.
```

## Türkçe (`tr`)

```
İnsanlar neden popülistlere oy vermeye devam ediyor?
```

```
Üç siyasetçi, üç ülke ve neredeyse başka hiçbir ortak nokta yok. Donald Trump Amerikan halk oylamasını yüzde 49,8 ile kazandı. AfD Almanya'da yüzde 20,8 ile ikinci oldu; bu, 2021 sonucunun iki katı. Robert Fico dördüncü kez Slovakya başbakanı oldu – ve partisinin adı Yön – Sosyal Demokrasi, ve 2023'e kadar Avrupa sosyalist partileri ailesinin içinde yer aldı.

Birbirleriyle neredeyse her konuda anlaşmazlar. Altlarındaki mekanizma ise neredeyse aynı.

Bu video o mekanizma hakkında. Kimin haklı olduğu hakkında değil.

Siyaset bilimciler bu kelimeyi bizden daha dar kullanıyor. O anlamda popülizm bir politika programı bile değil. Sizin kim olduğunuza dair tek bir iddia: toplumun sıradan insanlar ile sistemi ele geçirmiş ve şimdi onu kendisi için işleten bir seçkinler tabakasına bölündüğü iddiası. Bu fikir o kadar dardır ki neredeyse her siyasetin üzerine yapışabilir – bu yüzden sol bir sürüm ile sağ bir sürüm bambaşka bir seçkin tabaka adlandırır ve yine de aynı cümleyi kurar.

Ve en iyi, sorun gerçek olduğunda işler. Hiçbir gencin alamayacağı konutlar, her yıl daha pahalı hale gelen sağlık, sessizce çürüyen altyapı. Bunların hiçbirinin abartılması gerekmez. Popülistin sorunu icat etmesine gerek yoktur – yalnızca açıklaması yeter, ve açıklama her zaman tek kelimeliktir.

Sonra bir ölçüm var ve beklediğinizi söylemiyor. 2017'de dört iktisatçı 220 Avrupa bölgesini finansal kriz boyunca izledi. İşsizliğin arttığı yerde sistem karşıtı partilere giden oylar da arttı ve ulusal parlamentolara ve Avrupa kurumlarına duyulan güven düştü. Ama göçmenlere yönelik tutumlar neredeyse hiç kıpırdamadı, kültür konusunda ise sertleşmedi – hatta Avrupalılar krizden biraz daha açık çıktı. Herkesin yaptığı tartışma ile oyları gerçekten oynatan şey iki farklı şeydi.

1958'de Amerikalıların yüzde 73'ü Washington'daki hükümetin doğru olanı yapacağına güvendiğini söylüyordu. Eylül 2025'te bu oran 17'ydi. Ve on altı ayda bu sayıdaki parti ayrımı çaprazlama yer değiştirdi: Demokratlar 35'ten 9'a, Cumhuriyetçiler 11'den 26'ya. Oturan kişi değişti. Yani o sayı hiçbir zaman performansı ölçmüyordu.

Bu da neredeyse kimsenin yüksek sesle söylemediği kısma götürüyor. Bir popülistin sizi basit çözümün işe yarayacağına ikna etmesi gerekmez – bu zor olurdu, çünkü çözümler denetlenebilir. Yalnızca mevcut olanın çoktan başarısız olduğuna ikna etmesi yeter. Ve bu iş çok daha kolaydır, çünkü çoğu zaman gerçekten de öyledir.

Bölümler
0:00 Karmaşık sorunlara basit cevaplar
0:29 Trump. AfD. Fico.
1:21 Sağda değil. Solda.
1:51 Araştırmada popülizm ne demek
2:49 Gerçek bir sorun neden daha iyi işler
3:45 Oyları gerçekten oynatan neydi
5:03 Şansınızı kullandınız
5:30 Yüzde yetmiş üç, ve on yedi
6:10 Kaybedecek neyimiz var?
6:30 Bütün numara
6:51 Bir slogan neden kazanır
7:32 Tek bir suçlu yok, tek bir çözüm yok
8:06 Bu neden hep geri geliyor
8:34 Oturan kişi değişti
9:20 Belirti, hastalık değil
9:44 Onlar oy vermeden önce ne oldu

Kaynaklar: Mudde, "The Populist Zeitgeist" (2004). Algan, Guriev, Papaioannou & Passari, "The European Trust Crisis and the Rise of Populism", Brookings Papers on Economic Activity (2017). Pew Research Center, "Public Trust in Government: 1958-2025".

Altyazılar bu video için yazıldı, otomatik olarak oluşturulmadı. İkinci ses parçası olarak Amerikan İngilizcesi ses parçası mevcuttur.

Müzik bu kanal için yordamsal olarak üretilmektedir.
```

## українська (`uk`)

```
Чому люди й далі голосують за популістів?
```

```
Троє політиків, три країни — і майже нічого спільного більше. Дональд Трамп виграв американське народне голосування з 49,8 відсотка. AfD посіла в Німеччині друге місце з 20,8 відсотка, удвічі більше за свій результат 2021 року. Роберт Фіцо вчетверте став прем'єр-міністром Словаччини — а його партія називається Напрямок – соціальна демократія і до 2023 року належала до родини європейських соціалістичних партій.

Між собою вони не згодні майже в усьому. Механізм під ними майже однаковий.

Це відео — про той механізм. Не про те, хто має рацію.

Політологи вживають це слово вужче, ніж ми. Популізм у такому значенні взагалі не є політичною програмою. Це одне твердження про те, хто ви є: що суспільство ділиться на звичайних людей і еліту, яка захопила систему і тепер крутить її для себе. Це достатньо тонка ідея, щоб уміститися майже в будь-яку політику, — і саме тому ліва й права версії називають зовсім різну еліту, а речення будують те саме.

І найкраще це працює тоді, коли проблема справжня. Житло, якого не може собі дозволити жодна молода людина, медицина, що дорожчає щороку, інфраструктура, яка тихо розсипається. Нічого з цього не треба перебільшувати. Популістові не потрібно вигадувати проблему — лише пояснити її, і пояснення завжди завдовжки одне слово.

Далі є вимірювання, і воно каже не те, чого ви очікували б. У 2017 році четверо економістів простежили 220 європейських регіонів упродовж фінансової кризи. Там, де зростало безробіття, зростали й голоси за антисистемні партії, а довіра до національних парламентів і європейських інституцій падала. Але ставлення до іммігрантів майже не зрушило, а щодо культури воно навіть не затверділо — якщо вже, європейці вийшли з кризи трохи відкритішими. Суперечка, яку всі вели, і те, що насправді рухало голоси, були двома різними речами.

У 1958 році 73 відсотки американців казали, що довіряють уряду у Вашингтоні робити правильні речі. До вересня 2025 року лишилося 17. А за шістнадцять місяців показники довіри серед демократів і республіканців помінялися місцями: демократи з 35 до 9, республіканці з 11 до 26. Змінився господар Білого дому. Отже, це число ніколи не вимірювало результативності.

Що веде до частини, яку майже ніхто не каже вголос. Популістові не треба переконувати вас, що просте рішення спрацює, — це було б важко, бо рішення можна перевірити. Лише в тому, що нинішнє вже провалилося. І ця робота значно легша, бо доволі часто це просто правда.

Розділи
0:00 Прості відповіді на складні проблеми
0:29 Трамп. AfD. Фіцо.
1:21 Не праворуч. Ліворуч.
1:51 Що популізм означає в дослідженнях
2:49 Чому справжня проблема працює краще
3:45 Що насправді рухало голоси
5:03 Ви мали свій шанс
5:30 Сімдесят три відсотки — і сімнадцять
6:10 Що нам втрачати?
6:30 Увесь трюк
6:51 Чому виграє гасло
7:32 Немає одного винуватця й одного універсального рішення
8:06 Чому це щоразу повертається
8:34 Змінився господар Білого дому
9:20 Симптом, а не хвороба
9:44 Що сталося до того, як вони проголосували

Джерела: Mudde, "The Populist Zeitgeist" (2004). Algan, Guriev, Papaioannou & Passari, "The European Trust Crisis and the Rise of Populism", Brookings Papers on Economic Activity (2017). Pew Research Center, "Public Trust in Government: 1958-2025".

Субтитри написані для цього відео, а не згенеровані автоматично. Доступна аудіодоріжка американською англійською як друга звукова доріжка.

Музика генерується для цього каналу процедурно.
```

## Tiếng Việt (`vi`)

```
Vì sao người ta cứ bầu cho những người dân túy?
```

```
Ba chính trị gia, ba quốc gia, và gần như không còn gì chung nữa. Donald Trump thắng phiếu phổ thông ở Mỹ với 49,8 phần trăm. AfD về nhì ở Đức với 20,8 phần trăm, gấp đôi kết quả năm 2021. Robert Fico trở thành thủ tướng Slovakia lần thứ tư – và đảng của ông tên là Hướng đi – Dân chủ Xã hội, và nó từng nằm trong gia đình các đảng xã hội chủ nghĩa châu Âu cho đến năm 2023.

Họ bất đồng với nhau về hầu hết mọi chuyện. Cỗ máy bên dưới họ thì gần như giống hệt.

Video này nói về cỗ máy đó. Không nói ai đúng.

Các nhà khoa học chính trị dùng từ này hẹp hơn chúng ta. Dân túy theo nghĩa đó hoàn toàn không phải một chương trình chính sách. Nó là một tuyên bố duy nhất về việc bạn là ai: rằng xã hội chia thành người dân thường và một tầng lớp tinh hoa đã chiếm lấy hệ thống và giờ vận hành nó cho chính mình. Ý tưởng đó hẹp đến mức có thể gắn vào gần như mọi khuynh hướng chính trị – và vì thế phiên bản cánh tả và phiên bản cánh hữu gọi tên hai tầng lớp tinh hoa hoàn toàn khác nhau mà vẫn dựng nên cùng một câu.

Và nó hiệu quả nhất khi vấn đề là có thật. Nhà ở không người trẻ nào mua nổi, y tế mỗi năm một đắt hơn, hạ tầng mục ruỗng trong im lặng. Không điều nào trong đó cần phóng đại. Người dân túy không cần bịa ra vấn đề – chỉ cần giải thích nó, và lời giải thích luôn dài đúng một từ.

Rồi có một phép đo, và nó không nói điều bạn tưởng. Năm 2017, bốn nhà kinh tế theo dõi 220 vùng ở châu Âu suốt cuộc khủng hoảng tài chính. Nơi thất nghiệp tăng, phiếu cho các đảng chống thiết chế cũng tăng theo, và niềm tin vào quốc hội các nước cùng các định chế châu Âu thì giảm. Nhưng thái độ với người nhập cư gần như không nhúc nhích, và về mặt văn hóa còn không hề cứng lại – nếu có, người châu Âu bước ra khỏi khủng hoảng cởi mở hơn một chút. Cuộc tranh luận mà ai cũng tham gia và thứ thực sự làm dịch chuyển lá phiếu là hai chuyện khác nhau.

Năm 1958, 73 phần trăm người Mỹ nói họ tin chính quyền ở Washington làm điều đúng đắn. Đến tháng 9 năm 2025 chỉ còn 17. Và trong mười sáu tháng, mức tin tưởng của cử tri hai đảng đã đổi chỗ cho nhau: Dân chủ từ 35 xuống 9, Cộng hòa từ 11 lên 26. Người ngồi ghế đã đổi. Vậy là con số đó chưa bao giờ đo hiệu quả.

Điều đó dẫn tới phần mà gần như không ai nói thành lời. Người dân túy không cần thuyết phục bạn rằng giải pháp đơn giản sẽ hiệu quả – việc đó khó, vì giải pháp có thể kiểm chứng được. Chỉ cần thuyết phục rằng cái hiện tại đã thất bại rồi. Và việc đó dễ hơn nhiều, vì điều đó thường đúng.

Các chương
0:00 Câu trả lời đơn giản cho vấn đề phức tạp
0:29 Trump. AfD. Fico.
1:21 Không ở bên phải. Ở bên trái.
1:51 Dân túy nghĩa là gì trong nghiên cứu
2:49 Vì sao vấn đề có thật lại hiệu quả hơn
3:45 Thứ thực sự làm dịch chuyển lá phiếu
5:03 Các vị đã có cơ hội của mình
5:30 Bảy mươi ba phần trăm, và mười bảy
6:10 Chúng ta có gì để mất?
6:30 Toàn bộ mẹo là đây
6:51 Vì sao khẩu hiệu thắng
7:32 Không có một kẻ xấu duy nhất, không có một cách chữa duy nhất
8:06 Vì sao nó cứ quay lại
8:34 Người ngồi ghế đã đổi
9:20 Triệu chứng, không phải căn bệnh
9:44 Chuyện gì đã xảy ra trước khi họ bỏ phiếu

Nguồn: Mudde, "The Populist Zeitgeist" (2004). Algan, Guriev, Papaioannou & Passari, "The European Trust Crisis and the Rise of Populism", Brookings Papers on Economic Activity (2017). Pew Research Center, "Public Trust in Government: 1958-2025".

Phụ đề được viết riêng cho video này, không phải tạo tự động. Có bản âm thanh tiếng Anh Mỹ dưới dạng bản âm thanh thứ hai.

Nhạc được tạo theo thuật toán riêng cho kênh này.
```

## čeština (`cs`)

```
Proč lidé pořád volí populisty?
```

```
Tři politici, tři země a jinak skoro nic společného. Donald Trump vyhrál americké lidové hlasování s 49,8 procenty. AfD skončila v Německu druhá s 20,8 procenty, tedy dvojnásobkem svého výsledku z roku 2021. Robert Fico se počtvrté stal slovenským premiérem – a jeho strana se jmenuje Smer – sociálna demokracia a až do roku 2023 patřila do rodiny evropských socialistických stran.

Mezi sebou se neshodnou skoro na ničem. Mechanismus, na kterém stavějí, je přitom téměř totožný.

Tohle video je o tom mechanismu. Ne o tom, kdo má pravdu.

Politologové to slovo používají úžeji než my. Populismus v tomhle smyslu není vůbec žádný program. Je to jediné tvrzení o tom, kdo jste: že se společnost dělí na obyčejné lidi a na elitu, která si vzala systém a teď ho provozuje pro sebe. Je to natolik tenká myšlenka, že se vejde skoro do jakékoli politiky – a právě proto levicová a pravicová verze pojmenují úplně jinou elitu a přesto postaví tutéž větu.

A funguje to nejlíp tehdy, když je problém skutečný. Bydlení, na které nikdo mladý nedosáhne, zdravotnictví, které každý rok stojí víc, infrastruktura, která tiše chátrá. Nic z toho se nemusí přehánět. Populista nemusí problém vymyslet – stačí, když ho vysvětlí, a vysvětlení je vždycky dlouhé jedno slovo.

Pak je tu měření a neříká to, co byste čekali. V roce 2017 sledovali čtyři ekonomové 220 evropských regionů napříč finanční krizí. Kde rostla nezaměstnanost, rostly s ní i hlasy pro protisystémové strany a klesala důvěra v národní parlamenty i evropské instituce. Jenže postoje k přistěhovalcům se skoro nehnuly a v kulturní rovině dokonce nezatvrdly – jestli se něco změnilo, vyšli Evropané z krize o kousek otevřenější. Spor, který všichni vedli, a to, co hlasy doopravdy pohnulo, byly dvě různé věci.

V roce 1958 řeklo 73 procent Američanů, že věří, že vláda ve Washingtonu dělá správné věci. V září 2025 jich bylo 17. A za šestnáct měsíců se poměr důvěry mezi demokraty a republikány obrátil: demokraté z 35 na 9, republikáni z 11 na 26. Vyměnil se obyvatel Bílého domu. To číslo tedy nikdy neměřilo výkon.

Což vede k části, kterou skoro nikdo neřekne nahlas. Populista vás nemusí přesvědčit, že to jednoduché řešení bude fungovat – to by bylo těžké, protože řešení jde ověřit. Stačí, když vás přesvědčí, že to dosavadní už selhalo. A to je mnohem snazší, protože dost často je to prostě pravda.

Kapitoly
0:00 Jednoduché odpovědi na složité problémy
0:29 Trump. AfD. Fico.
1:21 Ne napravo. Nalevo.
1:51 Co populismus znamená ve výzkumu
2:49 Proč skutečný problém funguje líp
3:45 Co hlasy doopravdy pohnulo
5:03 Měli jste svou šanci
5:30 Sedmdesát tři procent, a sedmnáct
6:10 Co můžeme ztratit?
6:30 Celý ten trik
6:51 Proč vyhrává heslo
7:32 Není jeden viník ani jedno řešení
8:06 Proč se to pořád vrací
8:34 Vyměnil se obyvatel Bílého domu
9:20 Příznak, ne nemoc
9:44 Co se stalo předtím, než volili

Zdroje: Mudde, "The Populist Zeitgeist" (2004). Algan, Guriev, Papaioannou & Passari, "The European Trust Crisis and the Rise of Populism", Brookings Papers on Economic Activity (2017). Pew Research Center, "Public Trust in Government: 1958-2025".

Titulky jsou k tomuhle videu napsané, ne strojově vygenerované. Jako druhá zvuková stopa je k dispozici americká angličtina.

Hudba se pro tenhle kanál generuje procedurálně.
```

## español (`es`)

```
¿Por qué la gente sigue votando a los populistas?
```

```
Tres políticos, tres países y casi nada más en común. Donald Trump ganó el voto popular estadounidense con el 49,8 por ciento. AfD quedó segunda en Alemania con el 20,8 por ciento, el doble de su resultado de 2021. Robert Fico se convirtió en primer ministro de Eslovaquia por cuarta vez – y su partido se llama Dirección – Socialdemocracia, y estuvo dentro de la familia de los partidos socialistas europeos hasta 2023.

Entre ellos discrepan en casi todo. La maquinaria que tienen debajo es casi idéntica.

Este vídeo va de esa maquinaria. No de quién tiene razón.

Los politólogos usan la palabra en un sentido más restringido que nosotros. El populismo, en ese sentido, no es en absoluto un programa de gobierno. Es una única afirmación sobre quién es usted: que la sociedad se divide entre la gente corriente y una élite que se ha quedado con el sistema y ahora lo hace funcionar para sí misma. La idea es lo bastante estrecha como para acoplarse a casi cualquier política, y por eso una versión de izquierdas y otra de derechas nombran una élite completamente distinta y aun así construyen la misma frase.

Y funciona mejor cuando el problema es real. Vivienda que ningún joven puede pagar, sanidad que cuesta más cada año, infraestructuras que se pudren en silencio. Nada de eso necesita exagerarse. El populista no tiene que inventar el problema – solo explicarlo, y la explicación siempre se resume en una palabra.

Luego hay una medición, y no dice lo que usted esperaría. En 2017 cuatro economistas siguieron 220 regiones europeas a lo largo de la crisis financiera. Donde subía el paro, subían con él los votos a los partidos antisistema, y caía la confianza en los parlamentos nacionales y en las instituciones europeas. Pero las actitudes hacia los inmigrantes apenas se movieron, y en lo cultural ni siquiera se endurecieron – si acaso, los europeos salieron de la crisis algo más abiertos. El debate que todos mantenían y lo que de verdad movía los votos eran dos cosas distintas.

En 1958, el 73 por ciento de los estadounidenses decía confiar en que el gobierno de Washington hiciera lo correcto. En septiembre de 2025 era el 17. Y en dieciséis meses los niveles de confianza entre demócratas y republicanos se invirtieron: demócratas de 35 a 9, republicanos de 11 a 26. Cambió el inquilino. Así que esa cifra nunca estuvo midiendo resultados.

Lo que lleva a la parte que casi nadie dice en voz alta. Un populista no tiene que convencerle de que la solución simple va a funcionar – eso sería difícil, porque las soluciones se pueden comprobar. Solo de que la actual ya ha fracasado. Y ese trabajo es mucho más fácil, porque bastante a menudo es sencillamente cierto.

Capítulos
0:00 Respuestas simples a problemas complicados
0:29 Trump. AfD. Fico.
1:21 No a la derecha. A la izquierda.
1:51 Qué significa populismo en la investigación
2:49 Por qué un problema real funciona mejor
3:45 Qué movía de verdad los votos
5:03 Tuvieron su oportunidad
5:30 Setenta y tres por ciento, y diecisiete
6:10 ¿Qué tenemos que perder?
6:30 Todo el truco
6:51 Por qué gana un eslogan
7:32 Ningún culpable único, ninguna solución única
8:06 Por qué esto vuelve siempre
8:34 Cambió el inquilino
9:20 Síntoma, no enfermedad
9:44 Qué pasó antes de que votaran

Fuentes: Mudde, "The Populist Zeitgeist" (2004). Algan, Guriev, Papaioannou & Passari, "The European Trust Crisis and the Rise of Populism", Brookings Papers on Economic Activity (2017). Pew Research Center, "Public Trust in Government: 1958-2025".

Los subtítulos están escritos para este vídeo, no generados automáticamente. Hay una pista de audio en inglés americano disponible como segunda pista de audio.

La música se genera de forma procedural para este canal.
```

## svenska (`sv`)

```
Varför fortsätter folk rösta på populister?
```

```
Tre politiker, tre länder och nästan inget annat gemensamt. Donald Trump vann den amerikanska folkomröstningen med 49,8 procent. AfD kom tvåa i Tyskland med 20,8 procent, dubbelt så mycket som 2021. Robert Fico blev Slovakiens premiärminister för fjärde gången – och hans parti heter Riktning – socialdemokrati, och det tillhörde familjen av europeiska socialistiska partier fram till 2023.

Sinsemellan är de oense om nästan allt. Maskineriet under dem är nästan identiskt.

Den här videon handlar om det maskineriet. Inte om vem som har rätt.

Statsvetare använder ordet snävare än vi. Populism i den meningen är inget politiskt program alls. Det är ett enda påstående om vem du är: att samhället delas i vanligt folk och en elit som har tagit systemet och nu kör det för sig själv. Det är tunt nog för att rymmas inuti nästan vilken politik som helst – och därför pekar en vänsterversion och en högerversion ut helt olika eliter och bygger ändå samma mening.

Och det fungerar bäst när problemet är på riktigt. Bostäder som ingen ung har råd med, vård som kostar mer varje år, infrastruktur som tyst ruttnar. Inget av det behöver överdrivas. Populisten behöver inte hitta på problemet – bara förklara det, och förklaringen är alltid ett ord lång.

Sedan finns en mätning, och den säger inte det man skulle vänta sig. År 2017 följde fyra ekonomer 220 europeiska regioner genom finanskrisen. Där arbetslösheten steg, steg rösterna på antietablissemangspartier med den, och förtroendet för nationella parlament och europeiska institutioner föll. Men attityderna till invandrare rörde sig knappt, och kulturellt hårdnade de inte alls – om något kom européerna ur krisen något öppnare. Debatten som alla förde och det som faktiskt flyttade rösterna var två olika saker.

År 1958 sa 73 procent av amerikanerna att de litade på att regeringen i Washington gjorde det rätta. I september 2025 var det 17. Och på sexton månader bytte demokraternas och republikanernas förtroendesiffror plats: demokrater från 35 till 9, republikaner från 11 till 26. Hyresgästen byttes ut. Den siffran mätte alltså aldrig prestation.

Vilket leder till den del nästan ingen säger högt. En populist behöver inte övertyga dig om att den enkla lösningen kommer att fungera – det vore svårt, för lösningar går att kontrollera. Bara om att den nuvarande redan har misslyckats. Och det jobbet är mycket lättare, för ganska ofta är det helt enkelt sant.

Kapitel
0:00 Enkla svar på komplicerade problem
0:29 Trump. AfD. Fico.
1:21 Inte till höger. Till vänster.
1:51 Vad populism betyder i forskningen
2:49 Varför ett verkligt problem fungerar bättre
3:45 Vad som faktiskt flyttade rösterna
5:03 Ni fick er chans
5:30 Sjuttiotre procent, och sjutton
6:10 Vad har vi att förlora?
6:30 Hela tricket
6:51 Varför en slogan vinner
7:32 Ingen ensam bär skulden, ingen lösning löser allt
8:06 Varför det kommer tillbaka
8:34 Hyresgästen byttes ut
9:20 Symptom, inte sjukdom
9:44 Vad som hände innan de röstade

Källor: Mudde, "The Populist Zeitgeist" (2004). Algan, Guriev, Papaioannou & Passari, "The European Trust Crisis and the Rise of Populism", Brookings Papers on Economic Activity (2017). Pew Research Center, "Public Trust in Government: 1958-2025".

Undertexterna är skrivna för den här videon, inte automatgenererade. Ett amerikansk-engelskt ljudspår finns tillgängligt som andra ljudspår.

Musiken genereras proceduralt för den här kanalen.
```
