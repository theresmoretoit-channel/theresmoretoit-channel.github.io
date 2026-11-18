# Lokalizované názvy a popisy — 108

Čte `tools/lokalizace.py` a nahrává přes `videos.update(part="localizations")`.
Anglický titul a popis jsou v `youtube.md` a posílají se zpátky beze změny.

**Pořadí sekcí je podle YouTube Studia** (bajtově podle ČESKÉHO názvu jazyka):
fi, fr, id, it, de, pl, pt-BR, tr, uk, vi, cs, es, sv.

## Co se NEPŘEKLÁDÁ

- citace zdrojů: autoři, roky, názvy článků a knih (Turing, Davis,
  Strachey, Havender, Coffman et al., Newcombe et al.) a názvy časopisů
  (Proceedings of the London Mathematical Society, The Computer Journal,
  IBM Systems Journal, ACM Computing Surveys, Communications of the ACM)
  zůstávají latinkou a anglicky ve všech jazycích včetně ukrajinštiny,
  aby se daly dohledat. Překládá se jen spojka mezi autory, popis zdroje
  u Microsoft Learn („průvodce deadlocky v SQL Serveru a chyba 1205“)
  a Vídeňská úmluva, která má v každém jazyce oficiální název (článek 18
  beze změny).
- jména Microsoft Learn, SQL Server, Amazon, Wikimedia Commons.
- časy kapitol na vteřinu (ze `youtube.md`, scény S01, S07, S13, S19,
  S26, S29, S33, S45, S51, S59).
- čísla: 35 kroků, 1936, milion — v popisu číslicí jako v anglickém.
- tagy — YouTube je per-jazyk nemá.

Odstavec o titulcích a americké stopě je **doslova** z tabulky
v `docs/zverejneni.md` („Popis NEJMENUJE počet jazyků titulků").

Terminologie podle titulků `script.<kód>.md` téhož jazyka: deadlock
(cs, de, it, id, pt-BR), interblocage (fr), interbloqueo (es),
zakleszczenie (pl), kilitlenme (tr), взаємне блокування (uk), bế tắc (vi),
lukkiutuminen (fi), baklås (sv); problém zastavení a jeho ekvivalenty
z S28; „oběť deadlocku“ z S16. Registr jako v titulcích: tykání
(cs, de, fr, it, es, pl, uk, tr, id, sv), pt-BR você, fi sinä, vi bạn.
Pointa se neprozrazuje víc než v angličtině: kapitola 04:37 je otázka z S33.

## suomi (`fi`)

```
Miksi tietokoneet eivät voi ennustaa jokaista lukkiutumista?
```

```
Neljä autoa saapuu risteykseen täsmälleen samalla hetkellä. Jokainen kuljettaja väistää oikealta tulevaa autoa, joten jokainen kuljettaja odottaa, eikä kukaan pääse koskaan liikkeelle. Ohjelmat jäävät jumiin samalla tavalla. Kumpikin kahdesta tehtävästä pitää lukkoa, jota toinen tarvitsee, ja koodi voi toimia miljoona kertaa ilman ongelmia, ennen kuin ajoitus jonain päivänä menee pieleen.

Tietokannat ovat hyviä havaitsemaan lukkiutumisen, kun se on jo tapahtunut. Microsoftin SQL Server jopa valitsee ”lukkiutumisen uhrin” ja käskee sen yrittää uudelleen. Mutta voisiko ohjelma lukea toisen ohjelman ja kertoa sinulle varmasti, jääkö se koskaan jumiin? Alan Turingin pysähtymisongelmasta kannettavaan tietokoneeseen, jonka muistilla on enemmän mahdollisia tiloja kuin kukaan voisi koskaan tarkistaa, ja vikaan, jonka Amazonin insinöörit löysivät ja joka ilmeni vasta 35 askeleen jälkeen: miksi mikään nopeampi tietokone ei korjaa tätä ja mitä ohjelmoijat tekevät sen sijaan.

Lähteet: A. M. Turing, "On Computable Numbers, with an Application to the Entscheidungsproblem", Proceedings of the London Mathematical Society (1936); M. Davis, Computability and Unsolvability (1958); C. Strachey, "An impossible program", The Computer Journal (1965); J. W. Havender, "Avoiding deadlock in multitasking systems", IBM Systems Journal (1968); E. G. Coffman, M. J. Elphick ja A. Shoshani, "System Deadlocks", ACM Computing Surveys (1971); C. Newcombe et al., "How Amazon Web Services Uses Formal Methods", Communications of the ACM 58(4) (2015); Microsoft Learn, SQL Serverin lukkiutumisopas ja virhe 1205; Wienin tieliikenneyleissopimus (1968), 18 artikla.

Tekstitykset on kirjoitettu tätä videota varten, ei luotu automaattisesti. Toisena ääniraitana on amerikanenglanti.

Koko teksti, lähteet ja käännökset: https://theresmoretoit-channel.github.io/fi/videos/why-computers-cant-always-detect-deadlocks/

LUVUT
00:00 Neljä autoa, eikä kukaan liiku
01:03 Miten ohjelma jää jumiin
02:02 Miten tietokannat huomaavat lukkiutumisen
02:49 Vaikea kysymys
03:41 Turing ja pysähtymisongelma
04:07 Ohjelma, joka tekee päinvastoin
04:37 Miten tämä liittyy lukkiutumisiin?
06:12 Mutta tietokoneet ovat äärellisiä
07:05 Mitä ohjelmoijat tekevät sen sijaan
08:24 Takaisin risteykseen

KUVALÄHTEET
Alan Turingin muotokuva 1930-luvulta on public domain -aineistoa, Wikimedia Commonsin kautta.
```

## français (`fr`)

```
Pourquoi les ordinateurs ne peuvent-ils pas prévoir tous les interblocages ?
```

```
Quatre voitures arrivent à un carrefour exactement au même moment. Chaque conducteur cède le passage à la voiture de droite, alors chaque conducteur attend, et personne ne bouge jamais. Les programmes se bloquent de la même façon. Deux tâches détiennent chacune un verrou dont l'autre a besoin, et le code peut tourner un million de fois sans problème, jusqu'au jour où les deux tâches se croisent au mauvais moment.

Les bases de données savent bien repérer un interblocage une fois qu'il s'est produit. SQL Server de Microsoft désigne même une « victime de l'interblocage » et lui demande de réessayer. Mais un programme pourrait-il lire un autre programme et te dire, avec certitude, s'il finira un jour par se bloquer ? Du problème de l'arrêt d'Alan Turing à un ordinateur portable dont la mémoire a tellement d'états possibles que personne ne pourrait jamais tous les vérifier, et jusqu'au bug que des ingénieurs d'Amazon ont trouvé et qui n'apparaissait qu'au bout de 35 étapes : pourquoi aucun ordinateur plus rapide n'y changera rien, et ce que font les programmeurs à la place.

Sources : A. M. Turing, "On Computable Numbers, with an Application to the Entscheidungsproblem", Proceedings of the London Mathematical Society (1936) ; M. Davis, Computability and Unsolvability (1958) ; C. Strachey, "An impossible program", The Computer Journal (1965) ; J. W. Havender, "Avoiding deadlock in multitasking systems", IBM Systems Journal (1968) ; E. G. Coffman, M. J. Elphick et A. Shoshani, "System Deadlocks", ACM Computing Surveys (1971) ; C. Newcombe et al., "How Amazon Web Services Uses Formal Methods", Communications of the ACM 58(4) (2015) ; Microsoft Learn, guide sur les interblocages dans SQL Server et erreur 1205 ; Convention de Vienne sur la circulation routière (1968), article 18.

Les sous-titres sont écrits pour cette vidéo, pas générés automatiquement. Une piste audio en anglais américain est disponible en seconde piste.

Transcription complète, sources et traductions : https://theresmoretoit-channel.github.io/fr/videos/why-computers-cant-always-detect-deadlocks/

CHAPITRES
00:00 Quatre voitures, et personne ne bouge
01:03 Comment un programme se bloque
02:02 Comment les bases de données repèrent un interblocage
02:49 La question difficile
03:41 Turing et le problème de l'arrêt
04:07 Un programme qui fait l'inverse
04:37 Quel rapport avec les interblocages ?
06:12 Mais un ordinateur n'est pas infini
07:05 Ce que font les programmeurs à la place
08:24 Retour au carrefour

CRÉDITS DES IMAGES
Le portrait d'Alan Turing dans les années 1930 est dans le domaine public, via Wikimedia Commons.
```

## Bahasa Indonesia (`id`)

```
Kenapa komputer tidak bisa memprediksi setiap deadlock?
```

```
Empat mobil tiba di sebuah persimpangan tepat pada saat yang sama. Setiap pengemudi memberi jalan kepada mobil di sebelah kanannya, jadi setiap pengemudi menunggu, dan tidak ada yang pernah bergerak. Program bisa macet dengan cara yang sama. Dua tugas masing-masing memegang kunci yang dibutuhkan tugas lainnya, dan kodenya bisa berjalan sejuta kali tanpa masalah, sampai suatu saat kedua tugas itu bertumpang tindih dalam urutan yang salah.

Basis data pandai mengenali deadlock setelah deadlock itu terjadi. SQL Server milik Microsoft bahkan memilih "korban deadlock" dan menyuruhnya mencoba lagi. Tapi bisakah sebuah program membaca program lain dan memberitahumu dengan pasti apakah program itu suatu saat akan macet? Dari masalah penghentian (halting problem) Alan Turing, ke laptop yang memorinya punya lebih banyak kemungkinan keadaan daripada yang bisa diperiksa siapa pun, hingga bug yang ditemukan para insinyur Amazon dan baru muncul setelah 35 langkah: kenapa komputer yang lebih cepat tidak akan bisa membereskan ini, dan apa yang dilakukan programmer sebagai gantinya.

Sumber: A. M. Turing, "On Computable Numbers, with an Application to the Entscheidungsproblem", Proceedings of the London Mathematical Society (1936); M. Davis, Computability and Unsolvability (1958); C. Strachey, "An impossible program", The Computer Journal (1965); J. W. Havender, "Avoiding deadlock in multitasking systems", IBM Systems Journal (1968); E. G. Coffman, M. J. Elphick dan A. Shoshani, "System Deadlocks", ACM Computing Surveys (1971); C. Newcombe et al., "How Amazon Web Services Uses Formal Methods", Communications of the ACM 58(4) (2015); Microsoft Learn, panduan deadlock SQL Server dan error 1205; Konvensi Wina tentang Lalu Lintas Jalan (1968), pasal 18.

Subtitel ditulis khusus untuk video ini, bukan dibuat secara otomatis. Tersedia juga trek audio kedua dalam bahasa Inggris Amerika.

Transkrip lengkap, sumber, dan terjemahan: https://theresmoretoit-channel.github.io/id/videos/why-computers-cant-always-detect-deadlocks/

BAB
00:00 Empat mobil, dan tidak ada yang bergerak
01:03 Bagaimana program bisa macet
02:02 Cara basis data mengenali deadlock
02:49 Pertanyaan yang sulit
03:41 Turing dan masalah penghentian
04:07 Program yang melakukan kebalikannya
04:37 Apa hubungannya dengan deadlock?
06:12 Tapi komputer itu terbatas
07:05 Apa yang dilakukan programmer sebagai gantinya
08:24 Kembali ke persimpangan

KREDIT GAMBAR
Potret Alan Turing dari tahun 1930-an berstatus domain publik, via Wikimedia Commons.
```

## italiano (`it`)

```
Perché i computer non possono prevedere ogni deadlock?
```

```
Quattro auto arrivano a un incrocio esattamente nello stesso momento. Ogni automobilista dà la precedenza all'auto alla sua destra, così ogni automobilista aspetta, e nessuno si muove mai. I programmi si bloccano allo stesso modo. Due operazioni tengono ciascuna un lock che serve all'altra, e il codice può girare un milione di volte senza problemi, finché un giorno le due operazioni non si sovrappongono nel momento sbagliato.

I database sono bravi a individuare un deadlock quando ormai è avvenuto. SQL Server di Microsoft sceglie persino una «vittima del deadlock» e le dice di riprovare. Ma un programma potrebbe leggere un altro programma e dirti con certezza se prima o poi si bloccherà? Dal problema della fermata di Alan Turing a un portatile con più stati di memoria possibili di quanti se ne potrebbero mai controllare, fino al bug che alcuni ingegneri di Amazon hanno trovato e che si manifestava solo dopo 35 passi: perché nessun computer più veloce risolverà la cosa, e che cosa fanno invece i programmatori.

Fonti: A. M. Turing, "On Computable Numbers, with an Application to the Entscheidungsproblem", Proceedings of the London Mathematical Society (1936); M. Davis, Computability and Unsolvability (1958); C. Strachey, "An impossible program", The Computer Journal (1965); J. W. Havender, "Avoiding deadlock in multitasking systems", IBM Systems Journal (1968); E. G. Coffman, M. J. Elphick e A. Shoshani, "System Deadlocks", ACM Computing Surveys (1971); C. Newcombe et al., "How Amazon Web Services Uses Formal Methods", Communications of the ACM 58(4) (2015); Microsoft Learn, guida ai deadlock di SQL Server ed errore 1205; Convenzione di Vienna sulla circolazione stradale (1968), articolo 18.

I sottotitoli sono scritti per questo video, non generati automaticamente. Come seconda traccia audio è disponibile l’inglese americano.

Trascrizione completa, fonti e traduzioni: https://theresmoretoit-channel.github.io/it/videos/why-computers-cant-always-detect-deadlocks/

CAPITOLI
00:00 Quattro auto, e nessuno si muove
01:03 Come si blocca un programma
02:02 Come i database scoprono un deadlock
02:49 La domanda difficile
03:41 Turing e il problema della fermata
04:07 Un programma che fa l'opposto
04:37 Cosa c'entra con i deadlock?
06:12 Ma un computer non è infinito
07:05 Cosa fanno invece i programmatori
08:24 Di nuovo all'incrocio

CREDITI DELLE IMMAGINI
Il ritratto di Alan Turing negli anni Trenta è di pubblico dominio, via Wikimedia Commons.
```

## Deutsch (`de`)

```
Warum können Computer nicht jeden Deadlock vorhersagen?
```

```
Vier Autos kommen genau im selben Moment an eine Kreuzung. Jeder Fahrer lässt dem Auto von rechts die Vorfahrt, also wartet jeder Fahrer, und niemand fährt je los. Programme bleiben genauso hängen. Zwei Aufgaben halten jeweils eine Sperre, die die andere braucht, und der Code kann eine Million Mal ohne Probleme laufen, bis das Timing irgendwann schiefgeht.

Datenbanken erkennen einen Deadlock gut, wenn er schon eingetreten ist. Microsofts SQL Server wählt sogar ein „Deadlockopfer“ aus und sagt ihm, es solle es noch einmal versuchen. Aber könnte ein Programm ein anderes lesen und dir mit Sicherheit sagen, ob es jemals hängen bleibt? Von Alan Turings Halteproblem über einen Laptop, dessen Speicher mehr mögliche Zustände hat, als je jemand prüfen könnte, bis zu dem Fehler, den Ingenieure bei Amazon fanden und der erst nach 35 Schritten auftrat: warum kein schnellerer Computer das lösen wird und was Programmierer stattdessen tun.

Quellen: A. M. Turing, "On Computable Numbers, with an Application to the Entscheidungsproblem", Proceedings of the London Mathematical Society (1936); M. Davis, Computability and Unsolvability (1958); C. Strachey, "An impossible program", The Computer Journal (1965); J. W. Havender, "Avoiding deadlock in multitasking systems", IBM Systems Journal (1968); E. G. Coffman, M. J. Elphick und A. Shoshani, "System Deadlocks", ACM Computing Surveys (1971); C. Newcombe et al., "How Amazon Web Services Uses Formal Methods", Communications of the ACM 58(4) (2015); Microsoft Learn, Leitfaden zu Deadlocks in SQL Server und Fehler 1205; Wiener Übereinkommen über den Straßenverkehr (1968), Artikel 18.

Die Untertitel wurden für dieses Video geschrieben, nicht automatisch erzeugt. Als zweite Tonspur steht amerikanisches Englisch bereit.

Vollständiger Text, Quellen und Übersetzungen: https://theresmoretoit-channel.github.io/de/videos/why-computers-cant-always-detect-deadlocks/

KAPITEL
00:00 Vier Autos, und keiner fährt
01:03 Wie ein Programm hängen bleibt
02:02 Wie Datenbanken einen Deadlock erkennen
02:49 Die schwierige Frage
03:41 Turing und das Halteproblem
04:07 Ein Programm, das das Gegenteil tut
04:37 Was hat das mit Deadlocks zu tun?
06:12 Aber Computer sind endlich
07:05 Was Programmierer stattdessen tun
08:24 Zurück an der Kreuzung

BILDNACHWEIS
Das Porträt von Alan Turing aus den 1930er-Jahren ist gemeinfrei, via Wikimedia Commons.
```

## polski (`pl`)

```
Dlaczego komputery nie potrafią przewidzieć każdego zakleszczenia?
```

```
Do skrzyżowania podjeżdżają cztery samochody dokładnie w tej samej chwili. Każdy kierowca ustępuje pierwszeństwa autu z prawej, więc każdy kierowca czeka i nikt nigdy nie ruszy. Programy utykają w ten sam sposób. Każde z dwóch zadań trzyma blokadę, której potrzebuje to drugie, a kod może zadziałać milion razy bez problemu, aż w końcu oba zadania nałożą się na siebie w złym momencie.

Bazy danych dobrze wykrywają zakleszczenie, gdy już do niego doszło. Microsoft SQL Server wybiera nawet „ofiarę zakleszczenia” i każe jej spróbować jeszcze raz. Ale czy program mógłby przeczytać inny program i powiedzieć ci z całą pewnością, czy ten kiedykolwiek utknie? Od problemu stopu Alana Turinga, przez laptop, którego pamięć ma więcej możliwych stanów, niż ktokolwiek zdołałby sprawdzić, po błąd ujawniający się dopiero po 35 krokach, który znaleźli inżynierowie z Amazona: dlaczego żaden szybszy komputer tego nie naprawi i co programiści robią zamiast tego.

Źródła: A. M. Turing, "On Computable Numbers, with an Application to the Entscheidungsproblem", Proceedings of the London Mathematical Society (1936); M. Davis, Computability and Unsolvability (1958); C. Strachey, "An impossible program", The Computer Journal (1965); J. W. Havender, "Avoiding deadlock in multitasking systems", IBM Systems Journal (1968); E. G. Coffman, M. J. Elphick i A. Shoshani, "System Deadlocks", ACM Computing Surveys (1971); C. Newcombe et al., "How Amazon Web Services Uses Formal Methods", Communications of the ACM 58(4) (2015); Microsoft Learn, przewodnik po zakleszczeniach w SQL Server i błąd 1205; Konwencja wiedeńska o ruchu drogowym (1968), artykuł 18.

Napisy są pisane do tego filmu, nie generowane automatycznie. Jako druga ścieżka dźwiękowa dostępny jest angielski amerykański.

Pełna transkrypcja, źródła i tłumaczenia: https://theresmoretoit-channel.github.io/pl/videos/why-computers-cant-always-detect-deadlocks/

ROZDZIAŁY
00:00 Cztery auta i nikt nie rusza
01:03 Jak program utyka
02:02 Jak bazy danych wykrywają zakleszczenie
02:49 Trudne pytanie
03:41 Turing i problem stopu
04:07 Program, który robi na odwrót
04:37 Co to ma wspólnego z zakleszczeniami?
06:12 Ale komputer nie jest nieskończony
07:05 Co programiści robią zamiast tego
08:24 Z powrotem na skrzyżowaniu

ŹRÓDŁA ZDJĘĆ
Portret Alana Turinga z lat 30. XX wieku należy do domeny publicznej, źródło: Wikimedia Commons.
```

## português (Brasil) (`pt-BR`)

```
Por que os computadores não conseguem prever todos os deadlocks?
```

```
Quatro carros chegam a um cruzamento exatamente no mesmo instante. Cada motorista dá a preferência ao carro à sua direita, então todos esperam, e ninguém nunca sai do lugar. Programas travam do mesmo jeito. Duas tarefas seguram, cada uma, um bloqueio de que a outra precisa, e o código pode rodar um milhão de vezes sem problema, até que um dia o timing dá errado.

Bancos de dados são bons em detectar um deadlock depois que ele acontece. O SQL Server, da Microsoft, chega a escolher uma “vítima do deadlock” e mandar que ela tente de novo. Mas será que um programa conseguiria ler outro programa e te dizer, com certeza, se ele vai travar algum dia? Do problema da parada de Alan Turing a um notebook com mais estados de memória possíveis do que alguém jamais conseguiria verificar, e ao bug que só aparecia depois de 35 passos, encontrado por engenheiros da Amazon: por que nenhum computador mais rápido vai resolver isso, e o que os programadores fazem em vez disso.

Fontes: A. M. Turing, "On Computable Numbers, with an Application to the Entscheidungsproblem", Proceedings of the London Mathematical Society (1936); M. Davis, Computability and Unsolvability (1958); C. Strachey, "An impossible program", The Computer Journal (1965); J. W. Havender, "Avoiding deadlock in multitasking systems", IBM Systems Journal (1968); E. G. Coffman, M. J. Elphick e A. Shoshani, "System Deadlocks", ACM Computing Surveys (1971); C. Newcombe et al., "How Amazon Web Services Uses Formal Methods", Communications of the ACM 58(4) (2015); Microsoft Learn, guia de deadlocks do SQL Server e erro 1205; Convenção de Viena sobre Trânsito Viário (1968), artigo 18.

As legendas foram escritas para este vídeo, não geradas automaticamente. Como segunda faixa de áudio está disponível o inglês americano.

Transcrição completa, fontes e traduções: https://theresmoretoit-channel.github.io/pt-br/videos/why-computers-cant-always-detect-deadlocks/

CAPÍTULOS
00:00 Quatro carros, e ninguém sai do lugar
01:03 Como um programa trava
02:02 Como os bancos de dados detectam um deadlock
02:49 A pergunta difícil
03:41 Turing e o problema da parada
04:07 Um programa que faz o contrário
04:37 O que isso tem a ver com deadlocks?
06:12 Mas computadores são finitos
07:05 O que os programadores fazem em vez disso
08:24 De volta ao cruzamento

CRÉDITOS DAS IMAGENS
O retrato de Alan Turing nos anos 1930 está em domínio público, via Wikimedia Commons.
```

## Türkçe (`tr`)

```
Bilgisayarlar neden her kilitlenmeyi önceden göremez?
```

```
Dört araba bir kavşağa tam aynı anda geliyor. Her sürücü sağındaki arabaya yol veriyor; bu yüzden her sürücü bekliyor ve kimse asla hareket etmiyor. Programlar da aynı şekilde kilitlenir. İki görevin her biri, diğerinin ihtiyaç duyduğu bir kilidi tutuyor ve kod, bir gün zamanlama ters gidene kadar bir milyon kez sorunsuz çalışabiliyor.

Veritabanları, gerçekleşmiş bir kilitlenmeyi yakalamakta iyidir. Microsoft'un SQL Server'ı bir "kilitlenme kurbanı" bile seçer ve ona yeniden denemesini söyler. Ama bir program başka bir programı okuyup onun bir gün kilitlenip kilitlenmeyeceğini sana kesin olarak söyleyebilir mi? Alan Turing'in durma probleminden, belleği kimsenin kontrol edemeyeceği kadar çok olası duruma sahip bir dizüstü bilgisayara ve Amazon mühendislerinin bulduğu, ortaya çıkması için 35 adım gereken hataya kadar: neden hiçbir bilgisayar, ne kadar hızlı olursa olsun, bunu çözemeyecek ve programcılar bunun yerine ne yapıyor.

Kaynaklar: A. M. Turing, "On Computable Numbers, with an Application to the Entscheidungsproblem", Proceedings of the London Mathematical Society (1936); M. Davis, Computability and Unsolvability (1958); C. Strachey, "An impossible program", The Computer Journal (1965); J. W. Havender, "Avoiding deadlock in multitasking systems", IBM Systems Journal (1968); E. G. Coffman, M. J. Elphick ve A. Shoshani, "System Deadlocks", ACM Computing Surveys (1971); C. Newcombe et al., "How Amazon Web Services Uses Formal Methods", Communications of the ACM 58(4) (2015); Microsoft Learn, SQL Server kilitlenme kılavuzu ve 1205 hatası; Karayolu Trafiği Hakkında Viyana Sözleşmesi (1968), madde 18.

Altyazılar bu video için yazıldı, otomatik olarak oluşturulmadı. İkinci ses parçası olarak Amerikan İngilizcesi de mevcut.

Metnin tamamı, kaynaklar ve çeviriler: https://theresmoretoit-channel.github.io/tr/videos/why-computers-cant-always-detect-deadlocks/

BÖLÜMLER
00:00 Dört araba ve kimse kıpırdamıyor
01:03 Bir program nasıl kilitlenir
02:02 Veritabanları kilitlenmeyi nasıl yakalar
02:49 Zor soru
03:41 Turing ve durma problemi
04:07 Tam tersini yapan bir program
04:37 Bunun kilitlenmelerle ne ilgisi var?
06:12 Ama bilgisayarlar sonlu
07:05 Programcılar bunun yerine ne yapıyor
08:24 Kavşağa geri dönüş

GÖRSEL KAYNAKLARI
Alan Turing'in 1930'lardaki portresi kamu malıdır, Wikimedia Commons üzerinden.
```

## українська (`uk`)

```
Чому комп'ютери не можуть передбачити кожне взаємне блокування?
```

```
Чотири машини під'їжджають до перехрестя рівно в один і той самий момент. Кожен водій пропускає машину, що праворуч, тож кожен водій чекає, і ніхто ніколи не рушить з місця. Програми застрягають так само. Кожне з двох завдань тримає блокування, потрібне іншому, і код може мільйон разів виконатися без проблем, аж поки одного разу два завдання не накладуться в невдалий момент.

Бази даних добре розпізнають взаємне блокування, коли воно вже сталося. Microsoft SQL Server навіть обирає «жертву взаємного блокування» і каже їй спробувати ще раз. Але чи може програма прочитати іншу програму і сказати тобі напевно, чи та колись застрягне? Від проблеми зупинки Алана Тюрінга до ноутбука, пам'ять якого має більше можливих станів, ніж будь-хто міг би перевірити, і до помилки, яка проявлялася лише після 35 кроків і яку знайшли інженери Amazon: чому жоден швидший комп'ютер цього не виправить і що програмісти роблять натомість.

Джерела: A. M. Turing, "On Computable Numbers, with an Application to the Entscheidungsproblem", Proceedings of the London Mathematical Society (1936); M. Davis, Computability and Unsolvability (1958); C. Strachey, "An impossible program", The Computer Journal (1965); J. W. Havender, "Avoiding deadlock in multitasking systems", IBM Systems Journal (1968); E. G. Coffman, M. J. Elphick і A. Shoshani, "System Deadlocks", ACM Computing Surveys (1971); C. Newcombe et al., "How Amazon Web Services Uses Formal Methods", Communications of the ACM 58(4) (2015); Microsoft Learn, посібник із взаємних блокувань у SQL Server і помилка 1205; Віденська конвенція про дорожній рух (1968), стаття 18.

Субтитри написані для цього відео, а не згенеровані автоматично. Також доступна друга звукова доріжка — американською англійською.

Повний текст, джерела та переклади: https://theresmoretoit-channel.github.io/uk/videos/why-computers-cant-always-detect-deadlocks/

РОЗДІЛИ
00:00 Чотири машини, і ніхто не рушає
01:03 Як програма застрягає
02:02 Як бази даних помічають взаємне блокування
02:49 Складне питання
03:41 Тюрінг і проблема зупинки
04:07 Програма, яка робить навпаки
04:37 Який це має стосунок до взаємних блокувань?
06:12 Але комп'ютери скінченні
07:05 Що програмісти роблять натомість
08:24 Знову на перехресті

ДЖЕРЕЛА ЗОБРАЖЕНЬ
Портрет Алана Тюрінга 1930-х років перебуває в суспільному надбанні, з Wikimedia Commons.
```

## Tiếng Việt (`vi`)

```
Vì sao máy tính không thể dự đoán trước mọi bế tắc?
```

```
Bốn chiếc xe đến một ngã tư vào đúng cùng một thời điểm. Tài xế nào cũng nhường đường cho xe bên phải, nên tài xế nào cũng chờ, và chẳng ai nhúc nhích được. Chương trình cũng bị kẹt y như vậy. Hai tác vụ, mỗi bên giữ một khóa mà bên kia cần, và đoạn mã có thể chạy cả triệu lần không trục trặc gì, cho đến một lần hai tác vụ chồng lên nhau đúng vào lúc không may.

Cơ sở dữ liệu khá giỏi phát hiện một bế tắc khi nó đã xảy ra. SQL Server của Microsoft thậm chí còn chọn ra một "nạn nhân của bế tắc" và bảo nó thử lại. Nhưng liệu một chương trình có thể đọc chương trình khác và nói chắc chắn với bạn rằng nó có bao giờ bị kẹt hay không? Từ bài toán dừng của Alan Turing, đến một chiếc laptop có nhiều trạng thái bộ nhớ khả dĩ hơn mức bất kỳ ai có thể kiểm tra hết, rồi đến lỗi mà các kỹ sư Amazon tìm ra, phải qua 35 bước mới xuất hiện: vì sao máy tính có nhanh hơn đến đâu cũng không giải quyết được chuyện này, và thay vào đó các lập trình viên làm gì.

Nguồn: A. M. Turing, "On Computable Numbers, with an Application to the Entscheidungsproblem", Proceedings of the London Mathematical Society (1936); M. Davis, Computability and Unsolvability (1958); C. Strachey, "An impossible program", The Computer Journal (1965); J. W. Havender, "Avoiding deadlock in multitasking systems", IBM Systems Journal (1968); E. G. Coffman, M. J. Elphick và A. Shoshani, "System Deadlocks", ACM Computing Surveys (1971); C. Newcombe et al., "How Amazon Web Services Uses Formal Methods", Communications of the ACM 58(4) (2015); Microsoft Learn, hướng dẫn về bế tắc trong SQL Server và lỗi 1205; Công ước Viên về giao thông đường bộ (1968), điều 18.

Phụ đề được viết riêng cho video này, không phải tạo tự động. Có thể chọn tiếng Anh Mỹ ở bản âm thanh thứ hai.

Toàn văn, nguồn và bản dịch: https://theresmoretoit-channel.github.io/vi/videos/why-computers-cant-always-detect-deadlocks/

CHƯƠNG
00:00 Bốn chiếc xe, không ai nhúc nhích
01:03 Một chương trình bị kẹt như thế nào
02:02 Cơ sở dữ liệu phát hiện bế tắc ra sao
02:49 Câu hỏi khó
03:41 Turing và bài toán dừng
04:07 Một chương trình làm điều ngược lại
04:37 Chuyện này liên quan gì đến bế tắc?
06:12 Nhưng máy tính không phải vô hạn
07:05 Các lập trình viên làm gì thay vào đó
08:24 Trở lại ngã tư

NGUỒN HÌNH ẢNH
Chân dung Alan Turing vào những năm 1930 thuộc phạm vi công cộng, qua Wikimedia Commons.
```

## Čeština (`cs`)

```
Proč počítače nedokážou předpovědět každý deadlock?
```

```
Ke křižovatce přijedou čtyři auta přesně ve stejnou chvíli. Každý řidič dává přednost autu zprava, takže každý řidič čeká a nikdo se nikdy nepohne. Programy uváznou úplně stejně. Každá ze dvou úloh drží zámek, který potřebuje ta druhá, a kód může proběhnout milionkrát bez problémů, než se ty dvě úlohy jednou sejdou v nevhodnou chvíli.

Databáze umějí deadlock dobře poznat, když už nastal. SQL Server od Microsoftu dokonce vybere „oběť deadlocku“ a řekne jí, ať to zkusí znovu. Dokáže ale program přečíst jiný program a říct ti s jistotou, jestli někdy uvázne? Od problému zastavení Alana Turinga přes notebook, jehož paměť má víc možných stavů, než by kdokoli kdy dokázal zkontrolovat, až k chybě, kterou našli inženýři v Amazonu a která se projevila až po 35 krocích: proč to nevyřeší žádný rychlejší počítač a co místo toho dělají programátoři.

Zdroje: A. M. Turing, "On Computable Numbers, with an Application to the Entscheidungsproblem", Proceedings of the London Mathematical Society (1936); M. Davis, Computability and Unsolvability (1958); C. Strachey, "An impossible program", The Computer Journal (1965); J. W. Havender, "Avoiding deadlock in multitasking systems", IBM Systems Journal (1968); E. G. Coffman, M. J. Elphick a A. Shoshani, "System Deadlocks", ACM Computing Surveys (1971); C. Newcombe et al., "How Amazon Web Services Uses Formal Methods", Communications of the ACM 58(4) (2015); Microsoft Learn, průvodce deadlocky v SQL Serveru a chyba 1205; Vídeňská úmluva o silničním provozu (1968), článek 18.

Titulky jsou psané pro tohle video, ne strojový přepis. Jako druhá zvuková stopa je k dispozici americká angličtina.

Celý text, zdroje a překlady: https://theresmoretoit-channel.github.io/cs/videos/why-computers-cant-always-detect-deadlocks/

KAPITOLY
00:00 Čtyři auta a nikdo se nehne
01:03 Jak program uvázne
02:02 Jak databáze poznají deadlock
02:49 Ta těžká otázka
03:41 Turing a problém zastavení
04:07 Program, který udělá pravý opak
04:37 Co to má společného s deadlocky?
06:12 Jenže skutečný počítač není nekonečný
07:05 Co místo toho dělají programátoři
08:24 Zpátky na křižovatce

ZDROJE OBRÁZKŮ
Portrét Alana Turinga z 30. let je volné dílo, zdroj: Wikimedia Commons.
```

## español (`es`)

```
¿Por qué los ordenadores no pueden predecir todos los interbloqueos?
```

```
Cuatro coches llegan a un cruce exactamente en el mismo momento. Cada conductor cede el paso al coche de su derecha, así que todos esperan, y nadie se mueve nunca. Los programas se atascan del mismo modo. Dos tareas tienen cada una un cerrojo que la otra necesita, y el código puede ejecutarse un millón de veces sin problemas, hasta que un día las dos tareas coinciden en el momento equivocado.

Las bases de datos son buenas detectando un interbloqueo una vez que ha ocurrido. SQL Server, de Microsoft, incluso elige una «víctima del interbloqueo» y le dice que vuelva a intentarlo. Pero ¿podría un programa leer otro programa y decirte, con total seguridad, si alguna vez se quedará atascado? Del problema de la parada de Alan Turing a un portátil con más estados de memoria posibles de los que nadie podría comprobar jamás, y al fallo que unos ingenieros de Amazon encontraron y que solo aparecía tras 35 pasos: por qué ningún ordenador más rápido arreglará esto, y qué hacen los programadores en su lugar.

Fuentes: A. M. Turing, "On Computable Numbers, with an Application to the Entscheidungsproblem", Proceedings of the London Mathematical Society (1936); M. Davis, Computability and Unsolvability (1958); C. Strachey, "An impossible program", The Computer Journal (1965); J. W. Havender, "Avoiding deadlock in multitasking systems", IBM Systems Journal (1968); E. G. Coffman, M. J. Elphick y A. Shoshani, "System Deadlocks", ACM Computing Surveys (1971); C. Newcombe et al., "How Amazon Web Services Uses Formal Methods", Communications of the ACM 58(4) (2015); Microsoft Learn, guía de interbloqueos de SQL Server y error 1205; Convención de Viena sobre la Circulación Vial (1968), artículo 18.

Los subtítulos están escritos para este vídeo, no generados automáticamente. Como segunda pista de audio está disponible el inglés americano.

Transcripción completa, fuentes y traducciones: https://theresmoretoit-channel.github.io/es/videos/why-computers-cant-always-detect-deadlocks/

CAPÍTULOS
00:00 Cuatro coches, y nadie se mueve
01:03 Cómo se atasca un programa
02:02 Cómo detectan las bases de datos un interbloqueo
02:49 La pregunta difícil
03:41 Turing y el problema de la parada
04:07 Un programa que hace lo contrario
04:37 ¿Qué tiene que ver esto con los interbloqueos?
06:12 Pero los ordenadores son finitos
07:05 Qué hacen los programadores en su lugar
08:24 De vuelta al cruce

CRÉDITOS DE LAS IMÁGENES
El retrato de Alan Turing en los años treinta es de dominio público, vía Wikimedia Commons.
```

## svenska (`sv`)

```
Varför kan datorer inte förutsäga varje baklås?
```

```
Fyra bilar kommer fram till en korsning i exakt samma ögonblick. Varje förare lämnar företräde åt bilen från höger, så varje förare väntar, och ingen kommer någonsin iväg. Program fastnar på samma sätt. Två processer håller var sitt lås som den andra behöver, och koden kan köras en miljon gånger utan problem innan tajmingen en dag slår fel.

Databaser är bra på att upptäcka ett baklås när det väl har uppstått. Microsofts SQL Server väljer till och med ut ett ”offer för baklåset” och säger åt det att försöka igen. Men skulle ett program kunna läsa ett annat program och tala om för dig, med säkerhet, om det någonsin kommer att fastna? Från Alan Turings stopproblem till en bärbar dator vars minne har fler möjliga tillstånd än någon någonsin skulle kunna kontrollera, och till buggen som ingenjörer på Amazon hittade och som krävde 35 steg för att visa sig: varför ingen snabbare dator kommer att lösa det här, och vad programmerare gör i stället.

Källor: A. M. Turing, "On Computable Numbers, with an Application to the Entscheidungsproblem", Proceedings of the London Mathematical Society (1936); M. Davis, Computability and Unsolvability (1958); C. Strachey, "An impossible program", The Computer Journal (1965); J. W. Havender, "Avoiding deadlock in multitasking systems", IBM Systems Journal (1968); E. G. Coffman, M. J. Elphick och A. Shoshani, "System Deadlocks", ACM Computing Surveys (1971); C. Newcombe et al., "How Amazon Web Services Uses Formal Methods", Communications of the ACM 58(4) (2015); Microsoft Learn, guide om baklås i SQL Server och fel 1205; Wienkonventionen om vägtrafik (1968), artikel 18.

Undertexterna är skrivna för den här videon, inte automatgenererade. Som andra ljudspår finns amerikansk engelska.

Hela texten, källor och översättningar: https://theresmoretoit-channel.github.io/sv/videos/why-computers-cant-always-detect-deadlocks/

KAPITEL
00:00 Fyra bilar, och ingen rör sig
01:03 Hur ett program fastnar
02:02 Hur databaser upptäcker ett baklås
02:49 Den svåra frågan
03:41 Turing och stopproblemet
04:07 Ett program som gör tvärtom
04:37 Vad har det här med baklås att göra?
06:12 Men datorer är ändliga
07:05 Vad programmerare gör i stället
08:24 Tillbaka i korsningen

BILDKÄLLOR
Porträttet av Alan Turing från 1930-talet är allmän egendom (public domain), via Wikimedia Commons.
```
