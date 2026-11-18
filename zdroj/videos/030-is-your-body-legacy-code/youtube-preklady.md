# Lokalizované názvy a popisy — Is Your Body Legacy Code?

Podklad pro **YouTube Studio → video → Podrobnosti → Přidat jazyk**.
Pro každý jazyk **dva bloky ke zkopírování**: název a popis. Kopíruje se
**celý blok mezi trojicí zpětných apostrofů**. Anglický originál zůstává
v `youtube.md`.

**Jazyky jsou v pořadí YouTube Studia**, ne abecedně — Studio řadí
bajtově podle UTF-8.

## Co se NEPŘEKLÁDÁ

| | |
|---|---|
| **časy kapitol** | musí sedět na vteřinu, kopírují se beze změny |
| `finger` | název modulu z videa, je to identifikátor |
| **numpy** | název knihovny |
| **DNA** | zkratka; v každém jazyce se píše stejně (kromě `ADN` ve fr a es, kde je to zavedený tvar) |

Naopak **názvy kapitol se překládají** — jsou to popisky, ne
identifikátory. A **názvy jazyků v řádku o titulcích taky**: smíšený
seznam endonym uprostřed odstavce se čte jako nedotažený překlad.

> **Žádná atribuce.** Tohle video nemá jedinou archivní scénu, takže
> neexistuje `sources.json` ani `CREDITS.md` a v popisu není žádné
> jméno autora ani licence. Věta o původu vizuálů se překládá jako
> běžný text.

## Kontrola čísel

| v popisu | 10^ |
|---|---|
| **tři miliardy** znaků | 10⁹ — `drei Milliarden`, `tres mil millones`, `três bilhões`, `trois milliards`, `tre miliardi`, `trzy miliardy`, `tre miljarder` |
| **čtyři miliardy** let | 10⁹, tytéž tvary |
| **biliony** agentů | **10¹²** — `Billionen`, `billones`, `trilhões`, `des milliers de milliards`, `migliaia di miliardi`, `biliony`, `biljoner`. **Nikdy „trillionen"/„trillones"**, to je o šest řádů vedle |
| **devadesát devět procent** | vypisuje se slovy jako ve scénářích |
| **devět** jazyků titulků | |

---

## suomi (`fi`)

```
Onko kehosi legacy-koodia?
```

```
Kuvittele ohjelma, jossa on kolmen miljardin merkin verran käskyjä, kopioituna kokonaisena jokaiseen uuteen prosessiin — joka sitten jättää yhdeksänkymmentäyhdeksän prosenttia siitä huomiotta. Suunnilleen sitä solusi tekevät.

Lähes jokainen kehosi solu, jolla on tuma, kantaa samaa täydellistä kopiota genomistasi. Hermosolulla se on. Maksasolulla se on. Ne eivät käyttäydy lainkaan samoin. Niinpä geeni alkaa näyttää vähän funktiolta — paitsi ettei ole prosessoria, ei käskyosoitinta eikä mitään, joka suorittaisi DNA:ta rivi riviltä. Sen, mitkä osat otetaan käyttöön, ratkaisee molekyylien vuorovaikutusten verkosto, ja koodin omistaminen osoittautuu hyvin eri asiaksi kuin pääsy siihen.

Siitä eteenpäin ohjelmistovertaus muuttuu oudommaksi eikä heikommaksi. Repositorio, jonka commit-historia on neljä miljardia vuotta syvä ja jota ylläpidetään paikkauksilla ja kiertoteillä, koska mitään ei voi koskaan kirjoittaa uusiksi. Jatkuvan integraation putki, jonka testit ajetaan tuotantojärjestelmässä. Biljoonia pieniä toimijoita ilman keskuspalvelinta eikä ketään, jonka päässä arkkitehtuuri olisi. Ja kone, joka on ollut käynnissä vuosikymmeniä ilman ainuttakaan uudelleenkäynnistystä ja vaihtaa omia osiaan palvellessaan.

Sitten vertaus hajoaa, ja se on kaikkein kiinnostavinta. DNA ei ole rakennuspiirustus. Ei ole riviä, jossa lukisi luo käsivarsi. Osaamme sekvensoida genomin, tunnistaa geenejä ja mitata proteiineja — emmekä silti osaa panna yhden tavallisen solun DNA:ta tietokoneeseen, painaa suorita ja katsoa ihmisen kehittyvän. Meillä on genomi. Genomi ei ole koko kone.

Koko teksti, lähteet ja käännökset: https://theresmoretoit-channel.github.io/fi/videos/is-your-body-legacy-code/

Luvut
0:00 Ohjelma, jota kukaan ei kirjoittaisi
0:37 Jokaisessa solussa on koko juttu
0:57 Geenit näyttävät funktioilta
1:35 Mutta prosessoria ei ole
1:47 Mikä toimii osoittimen roolissa
2:49 Vaikka sinulla on koodi, et välttämättä pääse siihen käsiksi
3:10 Moduuli nimeltä finger
3:42 Kuka tämän suunnitteli?
3:56 Neljä miljardia vuotta commiteja
4:48 Se ei refaktoroi
5:26 Missä ovat yksikkötestit?
5:54 Kun solu voittaa ja sinä häviät
6:16 Keskuspalvelinta ei ole
6:57 Kehosi on hajautettu järjestelmä
7:36 Kukaan ei koskaan käynnistä sitä uudelleen
8:39 Ja jotenkin se toimii
9:00 Missä vertaus hajoaa
9:53 Meillä ei ole lähdekoodia
10:15 Lopullinen paradoksi

Jokainen tämän videon kuva on piirretty tai luotu sitä varten — arkistovalokuvia ei ole,
joten mitään ei ole tarpeen mainita lähteenä. Musiikki on proseduraalista, luotu numpyllä.

Tekstitykset on kirjoitettu tätä videota varten, ei luotu automaattisesti. Toisena ääniraitana on amerikanenglanti.
```

## français (`fr`)

Název:

```
Ton corps, c'est du code legacy ?
```

Popis:

```
Imagine un programme de trois milliards de caractères d'instructions, copié en entier dans
chaque nouveau processus — qui en ignore ensuite quatre-vingt-dix-neuf pour cent. C'est à peu
près ce que font tes cellules.

Presque chaque cellule de ton corps qui possède un noyau porte la même copie complète de ton
génome. Un neurone l'a. Une cellule du foie l'a. Elles ne se ressemblent en rien. Un gène finit
donc par ressembler un peu à une fonction — sauf qu'il n'y a pas de processeur, pas de pointeur
d'instruction et rien qui exécute l'ADN ligne par ligne. Ce qui décide des parties utilisées,
c'est un réseau d'interactions moléculaires, et avoir le code se révèle très différent d'y
avoir accès.

À partir de là, la comparaison logicielle devient plus étrange, pas plus faible. Un dépôt dont
l'historique de commits remonte à quatre milliards d'années, maintenu à coups de rustines parce
que rien ne peut jamais être réécrit. Une intégration continue dont les tests tournent sur le
système en production. Des milliers de milliards d'agents minuscules, sans serveur central et
sans personne qui garde l'architecture en tête. Et une machine qui tourne depuis des décennies
sans un seul redémarrage, en remplaçant ses propres pièces pendant qu'elle sert.

Puis la comparaison casse, et c'est le plus intéressant. L'ADN n'est pas un plan. Nulle part il
n'y a de ligne qui dise créer un bras. On sait séquencer un génome, identifier des gènes et
mesurer des protéines — et on ne sait toujours pas mettre l'ADN d'une cellule ordinaire dans un
ordinateur, appuyer sur exécuter et regarder un humain se développer. On a le génome. Le génome
n'est pas toute la machine.

Transcription complète, sources et traductions : https://theresmoretoit-channel.github.io/fr/videos/is-your-body-legacy-code/

Chapitres
0:00 Le programme que personne n'écrirait
0:37 Chaque cellule a le tout
0:57 Les gènes ressemblent à des fonctions
1:35 Mais il n'y a pas de processeur
1:47 Ce qui joue le rôle du pointeur
2:49 Avoir le code n'est pas y avoir accès
3:10 Le module appelé finger
3:42 Qui a conçu ça ?
3:56 Quatre milliards d'années de commits
4:48 Elle ne refactorise pas
5:26 Où sont les tests unitaires ?
5:54 Quand une cellule gagne et que tu perds
6:16 Il n'y a pas de serveur central
6:57 Ton corps est un système distribué
7:36 Personne ne le redémarre jamais
8:39 Et pourtant ça marche
9:00 Là où la comparaison casse
9:53 Nous n'avons pas le code source
10:15 Le paradoxe final

Tous les visuels de cette vidéo ont été dessinés ou générés pour elle — il n'y a aucune
photographie d'archive, donc rien à créditer. La musique est procédurale, générée avec numpy.

Les sous-titres sont écrits pour cette vidéo, pas générés automatiquement. Une piste audio en anglais américain est disponible en seconde piste.
```

---

## Bahasa Indonesia (`id`)

```
Apakah Tubuhmu Legacy Code?
```

```
Bayangkan sebuah program berisi tiga miliar karakter instruksi, disalin utuh ke setiap proses baru — yang lalu mengabaikan sembilan puluh sembilan persen darinya. Kurang lebih itulah yang dilakukan sel-selmu.

Hampir setiap sel bernukleus di tubuhmu membawa salinan lengkap genommu yang sama. Neuron punya. Sel hati punya. Perilakunya sama sekali berbeda. Jadi sebuah gen mulai terlihat sedikit seperti fungsi — hanya saja tidak ada CPU, tidak ada penunjuk instruksi dan tidak ada apa pun yang mengeksekusi DNA baris demi baris. Yang menentukan bagian mana yang dipakai adalah jaringan interaksi molekuler, dan punya kodenya ternyata sangat berbeda dari bisa mengaksesnya.

Dari situ analogi perangkat lunaknya justru makin aneh, bukan makin lemah. Sebuah repositori dengan riwayat commit sedalam empat miliar tahun, dirawat dengan tambalan dan solusi sementara karena tidak ada yang bisa ditulis ulang. Sebuah pipeline integrasi berkelanjutan yang tesnya berjalan di sistem produksi. Triliunan agen kecil tanpa server pusat dan tanpa siapa pun yang memegang arsitekturnya di kepala. Dan sebuah mesin yang sudah berjalan puluhan tahun tanpa sekali pun reboot, mengganti komponennya sendiri sambil terus melayani.

Lalu analoginya tidak berlaku lagi, dan justru itu bagian paling menariknya. DNA bukan cetak biru. Tidak ada baris yang berbunyi buat lengan. Kita bisa mengurutkan genom, mengidentifikasi gen dan mengukur protein — dan kita tetap tidak bisa memasukkan DNA satu sel biasa ke komputer, menekan run, lalu menonton seorang manusia berkembang. Genomnya kita punya. Genom bukanlah keseluruhan mesinnya.

Transkrip lengkap, sumber, dan terjemahan: https://theresmoretoit-channel.github.io/id/videos/is-your-body-legacy-code/

Bab
0:00 Program yang tidak akan ditulis siapa pun
0:37 Setiap sel punya seluruhnya
0:57 Gen terlihat seperti fungsi
1:35 Tapi tidak ada CPU
1:47 Apa yang berperan sebagai pointer
2:49 Punya kodenya bukan berarti bisa mengaksesnya
3:10 Modul bernama finger
3:42 Siapa yang merancang ini?
3:56 Empat miliar tahun commit
4:48 Ia tidak melakukan refactor
5:26 Mana unit test-nya?
5:54 Ketika sebuah sel menang dan kamu kalah
6:16 Tidak ada server pusat
6:57 Tubuhmu adalah sistem terdistribusi
7:36 Tidak ada yang pernah me-restart-nya
8:39 Dan entah bagaimana ia bekerja
9:00 Di mana analoginya tidak lagi berlaku
9:53 Kita tidak punya kode sumbernya
10:15 Paradoks terakhir

Setiap visual dalam video ini digambar atau dihasilkan khusus untuknya — tidak ada foto
arsip, jadi tidak ada yang perlu diatribusikan. Musiknya prosedural, dibuat dengan numpy.

Subtitel ditulis khusus untuk video ini, bukan dibuat secara otomatis. Tersedia juga trek audio kedua dalam bahasa Inggris Amerika.
```

## italiano (`it`)

Název:

```
Il tuo corpo è codice legacy?
```

Popis:

```
Immagina un programma con tre miliardi di caratteri di istruzioni, copiato per intero in ogni
nuovo processo — che poi ne ignora il novantanove per cento. È più o meno quello che fanno le
tue cellule.

Quasi ogni cellula del tuo corpo dotata di nucleo porta la stessa copia completa del tuo
genoma. Un neurone ce l'ha. Una cellula del fegato ce l'ha. Si comportano in modo del tutto
diverso. Un gene comincia così a somigliare a una funzione — solo che non c'è un processore,
non c'è un puntatore alle istruzioni e non c'è nulla che esegua il DNA riga per riga. A
decidere quali parti vengono usate è una rete di interazioni molecolari, e avere il codice si
rivela una cosa ben diversa dall'avervi accesso.

Da lì il paragone con il software diventa più strano, non più debole. Un repository la cui
cronologia di commit risale a quattro miliardi di anni fa, tenuto insieme da toppe perché nulla
può mai essere riscritto. Un'integrazione continua i cui test girano sul sistema in produzione.
Migliaia di miliardi di agenti minuscoli, senza server centrale e senza nessuno che tenga in
testa l'architettura. E una macchina che gira da decenni senza un solo riavvio, sostituendo i
propri pezzi mentre serve.

Poi il paragone si rompe, ed è la parte più interessante. Il DNA non è un progetto. Da nessuna
parte c'è una riga che dica crea un braccio. Sappiamo sequenziare un genoma, identificare i
geni e misurare le proteine — e ancora non sappiamo mettere il DNA di una cellula comune in un
computer, premere esegui e guardare una persona formarsi. Abbiamo il genoma. Il genoma non è
tutta la macchina.

Trascrizione completa, fonti e traduzioni: https://theresmoretoit-channel.github.io/it/videos/is-your-body-legacy-code/

Capitoli
0:00 Il programma che nessuno scriverebbe
0:37 Ogni cellula ha tutto quanto
0:57 I geni somigliano a funzioni
1:35 Ma non c'è nessun processore
1:47 Cosa fa le veci del puntatore
2:49 Avere il codice non è averne accesso
3:10 Il modulo chiamato finger
3:42 Chi ha progettato questa roba?
3:56 Quattro miliardi di anni di commit
4:48 Non rifattorizza
5:26 Dove sono i test unitari?
5:54 Quando una cellula vince e tu perdi
6:16 Non c'è nessun server centrale
6:57 Il tuo corpo è un sistema distribuito
7:36 Nessuno lo riavvia mai
8:39 Eppure funziona
9:00 Dove il paragone si rompe
9:53 Non abbiamo il codice sorgente
10:15 Il paradosso finale

Tutte le immagini di questo video sono state disegnate o generate per l'occasione — non c'è
nessuna fotografia d'archivio, quindi non c'è nulla da attribuire. La musica è procedurale,
generata con numpy.

I sottotitoli sono scritti per questo video, non generati automaticamente. Come seconda traccia audio è disponibile l’inglese americano.
```

---

## Deutsch (`de`)

Název:

```
Ist dein Körper Legacy-Code?
```

Popis:

```
Stell dir ein Programm mit drei Milliarden Zeichen an Anweisungen vor, das komplett in jeden
neuen Prozess kopiert wird — und der ignoriert davon dann neunundneunzig Prozent. Ungefähr das
tun deine Zellen.

Fast jede Zelle in deinem Körper, die einen Zellkern hat, trägt dieselbe vollständige Kopie
deines Genoms. Ein Neuron hat sie. Eine Leberzelle hat sie. Sie verhalten sich völlig
verschieden. Ein Gen sieht damit ein bisschen aus wie eine Funktion — nur gibt es keinen
Prozessor, keinen Befehlszeiger und nichts, was DNA Zeile für Zeile abarbeitet. Was entscheidet,
welche Teile genutzt werden, ist ein Netz molekularer Wechselwirkungen, und den Code zu haben
ist etwas ganz anderes, als Zugriff darauf zu haben.

Von da an wird der Softwarevergleich seltsamer statt schwächer. Ein Repository, dessen
Commit-Historie vier Milliarden Jahre zurückreicht, zusammengehalten von Flicken, weil nie
etwas neu geschrieben werden kann. Eine Continuous Integration, deren Tests auf dem
Produktivsystem laufen. Billionen winziger Agenten, ohne zentralen Server und ohne jemanden,
der die Architektur im Kopf hat. Und eine Maschine, die seit Jahrzehnten ohne einen einzigen
Neustart läuft und dabei ihre eigenen Teile austauscht.

Dann bricht der Vergleich, und das ist der interessanteste Teil. Die DNA ist kein Bauplan.
Nirgends steht eine Zeile, die sagt: erzeuge einen Arm. Wir können ein Genom sequenzieren, Gene
bestimmen und Proteine messen — und wir können die DNA einer gewöhnlichen Zelle immer noch
nicht in einen Computer laden, auf Start drücken und zusehen, wie ein Mensch entsteht. Wir
haben das Genom. Das Genom ist nicht die ganze Maschine.

Vollständiger Text, Quellen und Übersetzungen: https://theresmoretoit-channel.github.io/de/videos/is-your-body-legacy-code/

Kapitel
0:00 Das Programm, das niemand schreiben würde
0:37 Jede Zelle hat das Ganze
0:57 Gene sehen aus wie Funktionen
1:35 Aber es gibt keinen Prozessor
1:47 Was die Rolle des Zeigers spielt
2:49 Den Code haben heißt nicht drankommen
3:10 Das Modul namens finger
3:42 Wer hat das entworfen?
3:56 Vier Milliarden Jahre Commits
4:48 Sie refaktoriert nicht
5:26 Wo sind die Unit-Tests?
5:54 Wenn eine Zelle gewinnt und du verlierst
6:16 Es gibt keinen zentralen Server
6:57 Dein Körper ist ein verteiltes System
7:36 Niemand startet es je neu
8:39 Und irgendwie funktioniert es
9:00 Wo der Vergleich bricht
9:53 Wir haben den Quelltext nicht
10:15 Das letzte Paradox

Jedes Bild in diesem Video wurde dafür gezeichnet oder erzeugt — es gibt keine Archivfotos,
also gibt es auch nichts zu attribuieren. Die Musik ist prozedural, mit numpy erzeugt.

Die Untertitel wurden für dieses Video geschrieben, nicht automatisch erzeugt. Als zweite Tonspur steht amerikanisches Englisch bereit.
```

---

## polski (`pl`)

Název:

```
Czy twoje ciało to kod legacy?
```

Popis:

```
Wyobraź sobie program o trzech miliardach znaków instrukcji, kopiowany w całości do każdego
nowego procesu — który potem ignoruje dziewięćdziesiąt dziewięć procent. Mniej więcej to robią
twoje komórki.

Prawie każda komórka twojego ciała, która ma jądro, nosi tę samą pełną kopię twojego genomu.
Neuron ją ma. Komórka wątroby ją ma. Zachowują się zupełnie inaczej. Gen zaczyna więc
przypominać funkcję — tyle że nie ma procesora, nie ma wskaźnika instrukcji i nie ma niczego,
co wykonywałoby DNA linijka po linijce. O tym, które części zostaną użyte, decyduje sieć
oddziaływań molekularnych, a mieć kod okazuje się czymś zupełnie innym niż mieć do niego dostęp.

Od tego miejsca porównanie do oprogramowania robi się dziwniejsze, nie słabsze. Repozytorium,
którego historia commitów sięga cztery miliardy lat wstecz, trzymane na łatach, bo niczego nie
da się przepisać. Ciągła integracja, której testy działają na systemie produkcyjnym. Biliony
maleńkich agentów, bez centralnego serwera i bez nikogo, kto trzymałby architekturę w głowie.
I maszyna, która działa od dziesięcioleci bez jednego restartu, wymieniając własne części w
trakcie pracy.

Potem porównanie się załamuje i to jest najciekawsze. DNA nie jest planem. Nigdzie nie ma w nim
linijki, która mówi: stwórz rękę. Umiemy zsekwencjonować genom, zidentyfikować geny i zmierzyć
białka — i wciąż nie umiemy wgrać DNA zwykłej komórki do komputera, nacisnąć uruchom i patrzeć,
jak powstaje człowiek. Mamy genom. Genom to nie cała maszyna.

Pełna transkrypcja, źródła i tłumaczenia: https://theresmoretoit-channel.github.io/pl/videos/is-your-body-legacy-code/

Rozdziały
0:00 Program, którego nikt by nie napisał
0:37 Każda komórka ma całość
0:57 Geny wyglądają jak funkcje
1:35 Ale nie ma procesora
1:47 Co gra rolę wskaźnika
2:49 Mieć kod to nie mieć do niego dostęp
3:10 Moduł o nazwie finger
3:42 Kto to zaprojektował?
3:56 Cztery miliardy lat commitów
4:48 Nie refaktoryzuje
5:26 Gdzie są testy jednostkowe?
5:54 Gdy komórka wygrywa, a ty przegrywasz
6:16 Nie ma centralnego serwera
6:57 Twoje ciało to system rozproszony
7:36 Nikt tego nigdy nie restartuje
8:39 A jednak to działa
9:00 Tam, gdzie porównanie się załamuje
9:53 Nie mamy kodu źródłowego
10:15 Ostateczny paradoks

Każdy obraz w tym filmie został narysowany albo wygenerowany na jego potrzeby — nie ma tu
żadnych zdjęć archiwalnych, więc nie ma czego przypisywać. Muzyka jest proceduralna,
wygenerowana w numpy.

Napisy są pisane do tego filmu, nie generowane automatycznie. Jako druga ścieżka dźwiękowa dostępny jest angielski amerykański.
```

---

## português (Brasil) (`pt-BR`)

Název:

```
Seu corpo é código legado?
```

Popis:

```
Imagine um programa com três bilhões de caracteres de instruções, copiado inteiro para cada
processo novo — que depois ignora noventa e nove por cento dele. É mais ou menos isso que suas
células fazem.

Quase toda célula do seu corpo que tem núcleo carrega a mesma cópia completa do seu genoma. Um
neurônio tem. Uma célula do fígado tem. Elas se comportam de maneira completamente diferente.
Um gene passa então a parecer um pouco com uma função — só que não há processador, não há
ponteiro de instruções e não há nada executando o DNA linha por linha. Quem decide que partes
serão usadas é uma rede de interações moleculares, e ter o código acaba sendo bem diferente de
ter acesso a ele.

Daí em diante a comparação com software fica mais estranha, não mais fraca. Um repositório cujo
histórico de commits recua quatro bilhões de anos, sustentado por remendos porque nada pode ser
reescrito. Uma integração contínua cujos testes rodam no sistema em produção. Trilhões de
agentes minúsculos, sem servidor central e sem ninguém que guarde a arquitetura na cabeça. E
uma máquina que roda há décadas sem um único reinício, trocando as próprias peças enquanto
atende.

Depois a comparação quebra, e essa é a parte mais interessante. O DNA não é uma planta. Em
lugar nenhum existe uma linha dizendo: crie um braço. Sabemos sequenciar um genoma, identificar
genes e medir proteínas — e ainda não sabemos colocar o DNA de uma célula comum num computador,
apertar executar e ver uma pessoa se desenvolver. Temos o genoma. O genoma não é a máquina
inteira.

Transcrição completa, fontes e traduções: https://theresmoretoit-channel.github.io/pt-br/videos/is-your-body-legacy-code/

Capítulos
0:00 O programa que ninguém escreveria
0:37 Toda célula tem tudo
0:57 Genes parecem funções
1:35 Mas não existe processador
1:47 O que faz o papel do ponteiro
2:49 Ter o código não é ter acesso
3:10 O módulo chamado finger
3:42 Quem projetou isso?
3:56 Quatro bilhões de anos de commits
4:48 Ela não refatora
5:26 Cadê os testes unitários?
5:54 Quando uma célula ganha e você perde
6:16 Não existe servidor central
6:57 Seu corpo é um sistema distribuído
7:36 Ninguém nunca reinicia
8:39 E de algum jeito funciona
9:00 Onde a comparação quebra
9:53 Não temos o código-fonte
10:15 O paradoxo final

Todas as imagens deste vídeo foram desenhadas ou geradas para ele — não há nenhuma fotografia
de arquivo, então não há nada a creditar. A música é procedural, gerada com numpy.

As legendas foram escritas para este vídeo, não geradas automaticamente. Como segunda faixa de áudio está disponível o inglês americano.
```

---

## Türkçe (`tr`)

```
Bedenin Legacy Code mu?
```

```
Üç milyar karakterlik talimattan oluşan, her yeni sürece bütünüyle kopyalanan bir program düşün. Bu süreç sonra bunun yüzde doksan dokuzunu görmezden geliyor. Hücrelerinin yaptığı aşağı yukarı bu.

Bedenindeki çekirdeği olan hemen her hücre, genomunun aynı eksiksiz kopyasını taşıyor. Nöronda var. Karaciğer hücresinde var. Davranışları hiç benzemiyor. Böylece bir gen biraz fonksiyona benzemeye başlıyor — ne var ki ortada CPU yok, komut işaretçisi yok ve DNA’yı satır satır çalıştıran hiçbir şey yok. Hangi parçaların kullanılacağına moleküler etkileşimlerden oluşan bir ağ karar veriyor ve koda sahip olmanın, ona erişebilmekten epeyce farklı olduğu ortaya çıkıyor.

Oradan itibaren yazılım benzetmesi zayıflamak yerine tuhaflaşıyor. Commit geçmişi dört milyar yıl derinlikte olan, hiçbir şey baştan yazılamadığı için yamalar ve geçici çözümlerle idare edilen bir depo. Testleri üretim sisteminde koşan bir sürekli entegrasyon hattı. Merkezi sunucusu olmayan ve mimariyi kafasında tutan kimsenin bulunmadığı trilyonlarca küçük aktör. Ve onlarca yıldır tek bir kez bile yeniden başlatılmadan çalışan, hizmet verirken kendi parçalarını değiştiren bir makine.

Sonra benzetme kopuyor ve en ilginç kısım da bu. DNA bir yapı planı değil. İçinde kol oluştur yazan bir satır yok. Bir genomu dizileyebiliyor, genleri tanımlayabiliyor ve proteinleri ölçebiliyoruz — ama sıradan tek bir hücrenin DNA’sını bilgisayara koyup çalıştır tuşuna basarak bir insanın gelişmesini izleyemiyoruz. Genom elimizde. Genom, makinenin tamamı değil.

Metnin tamamı, kaynaklar ve çeviriler: https://theresmoretoit-channel.github.io/tr/videos/is-your-body-legacy-code/

Bölümler
0:00 Kimsenin yazmayacağı program
0:37 Her hücrede tamamı var
0:57 Genler fonksiyonlara benziyor
1:35 Ama ortada CPU yok
1:47 İşaretçi rolünü ne oynuyor
2:49 Koda sahip olmak, ona erişmek değil
3:10 finger adlı modül
3:42 Bunu kim tasarladı?
3:56 Dört milyar yıllık commit geçmişi
4:48 Refactor yapmıyor
5:26 Birim testler nerede?
5:54 Bir hücre kazanınca sen kaybediyorsun
6:16 Merkezi sunucu yok
6:57 Bedenin dağıtık bir sistem
7:36 Kimse onu hiç yeniden başlatmıyor
8:39 Ve bir şekilde çalışıyor
9:00 Benzetme nerede kopuyor
9:53 Kaynak kodu bizde yok
10:15 Son paradoks

Bu videodaki her görsel onun için çizildi ya da üretildi — arşiv fotoğrafı yok, dolayısıyla
atıf verilecek bir şey de yok. Müzik prosedürel, numpy ile üretildi.

Altyazılar bu video için yazıldı, otomatik olarak oluşturulmadı. İkinci ses parçası olarak Amerikan İngilizcesi de mevcut.
```

## українська (`uk`)

```
Чи є твоє тіло legacy-кодом?
```

```
Уяви програму на три мільярди символів інструкцій, яку цілком копіюють у кожен новий процес — а той потім ігнорує дев’яносто дев’ять відсотків із неї. Приблизно це роблять твої клітини.

Майже кожна клітина твого тіла, що має ядро, несе ту саму повну копію твого геному. Нейрон її має. Клітина печінки її має. Поводяться вони геть не однаково. Тож ген починає скидатися на функцію — от тільки немає процесора, немає лічильника команд і немає нічого, що виконувало б ДНК рядок за рядком. Те, які частини будуть використані, вирішує мережа молекулярних взаємодій, і мати код виявляється зовсім не тим самим, що мати до нього доступ.

Далі програмістська аналогія стає радше дивнішою, ніж слабшою. Репозиторій з історією комітів завглибшки чотири мільярди років, який підтримують латками й обхідними шляхами, бо нічого не можна переписати заново. Конвеєр безперервної інтеграції, чиї тести виконуються на продакшені. Трильйони крихітних агентів без центрального сервера й і ніхто не тримає всю архітектуру в голові. І машина, яка працює десятиліттями без жодного перезапуску й замінює власні деталі під час роботи.

А тоді аналогія ламається — і це найцікавіше. ДНК не є кресленням. Немає рядка, у якому було б написано створи руку. Ми вміємо секвенувати геном, розпізнавати гени й вимірювати білки — і все одно не вміємо взяти ДНК однієї звичайної клітини, вкласти її в комп’ютер, натиснути «запустити» й дивитися, як розвивається людина. Геном ми маємо. Геном — це не вся машина.

Повний текст, джерела та переклади: https://theresmoretoit-channel.github.io/uk/videos/is-your-body-legacy-code/

Розділи
0:00 Програма, якої ніхто не написав би
0:37 У кожній клітині є все
0:57 Гени схожі на функції
1:35 Але процесора немає
1:47 Що відіграє роль вказівника
2:49 Мати код — не те саме, що мати до нього доступ
3:10 Модуль на ім’я finger
3:42 Хто це спроєктував?
3:56 Чотири мільярди років комітів
4:48 Воно не рефакторить
5:26 Де юніт-тести?
5:54 Коли клітина виграє, а ти програєш
6:16 Центрального сервера немає
6:57 Твоє тіло — розподілена система
7:36 Ніхто його ніколи не перезапускає
8:39 І воно якось працює
9:00 Де аналогія ламається
9:53 Вихідного коду ми не маємо
10:15 Останній парадокс

Кожне зображення в цьому відео намальовано або згенеровано саме для нього — архівних
світлин немає, тож і атрибутувати нема що. Музика процедурна, згенерована за допомогою numpy.

Субтитри написані для цього відео, а не згенеровані автоматично. Також доступна друга звукова доріжка — американською англійською.
```

## Tiếng Việt (`vi`)

```
Cơ thể bạn có phải legacy code không?
```

```
Hãy hình dung một chương trình gồm ba tỉ ký tự lệnh, được sao chép nguyên vẹn vào mỗi tiến trình mới — rồi tiến trình ấy bỏ qua chín mươi chín phần trăm số đó. Đại khái đó là việc các tế bào của bạn đang làm.

Gần như mọi tế bào có nhân trong cơ thể bạn đều mang cùng một bản sao đầy đủ của bộ gene. Nơ-ron có. Tế bào gan có. Chúng hành xử chẳng giống nhau chút nào. Thế là một gene bắt đầu trông hơi giống một hàm — chỉ có điều không có CPU, không có con trỏ lệnh và không có gì thực thi DNA theo từng dòng. Thứ quyết định phần nào được dùng là một mạng lưới các tương tác phân tử, và hóa ra việc có mã rất khác với việc truy cập được vào mã.

Từ đó trở đi, phép so sánh với phần mềm càng lạ hơn chứ không yếu đi. Một kho mã có lịch sử commit sâu bốn tỉ năm, được duy trì bằng các bản vá và giải pháp tình thế, vì chẳng thứ gì có thể viết lại từ đầu. Một pipeline tích hợp liên tục mà các bài kiểm thử chạy thẳng trên hệ thống production. Hàng nghìn tỉ tác nhân tí hon, không máy chủ trung tâm và không ai giữ kiến trúc trong đầu. Và một cỗ máy đã chạy hàng chục năm mà chưa khởi động lại lần nào, thay chính các bộ phận của mình trong lúc vẫn phục vụ.

Rồi phép so sánh không còn đúng nữa, và đó mới là phần thú vị nhất. DNA không phải bản thiết kế. Không có dòng nào ghi hãy tạo một cánh tay. Chúng ta giải trình tự được bộ gene, nhận diện được gene và đo được protein — vậy mà vẫn không thể đưa DNA của một tế bào bình thường vào máy tính, bấm chạy và xem một con người phát triển. Bộ gene thì ta có. Bộ gene không phải toàn bộ cỗ máy.

Toàn văn, nguồn và bản dịch: https://theresmoretoit-channel.github.io/vi/videos/is-your-body-legacy-code/

Các chương
0:00 Chương trình chẳng ai viết như thế
0:37 Mỗi tế bào đều có trọn bộ
0:57 Gene trông như những hàm
1:35 Nhưng chẳng có CPU nào
1:47 Cái gì đóng vai con trỏ
2:49 Có mã không có nghĩa là truy cập được
3:10 Mô-đun tên là finger
3:42 Ai đã thiết kế thứ này?
3:56 Bốn tỉ năm commit
4:48 Nó không refactor
5:26 Unit test ở đâu?
5:54 Khi một tế bào thắng còn bạn thua
6:16 Không có máy chủ trung tâm
6:57 Cơ thể bạn là một hệ phân tán
7:36 Chẳng ai khởi động lại nó bao giờ
8:39 Vậy mà nó vẫn chạy
9:00 Chỗ phép so sánh gãy
9:53 Chúng ta không có mã nguồn
10:15 Nghịch lý cuối cùng

Mọi hình ảnh trong video này đều được vẽ hoặc tạo riêng cho nó — không có ảnh tư liệu nào,
nên cũng chẳng có gì phải ghi nguồn. Nhạc là nhạc thuật toán, tạo bằng numpy.

Phụ đề được viết riêng cho video này, không phải tạo tự động. Có thể chọn tiếng Anh Mỹ ở bản âm thanh thứ hai.
```

## čeština (`cs`)

Název:

```
Je tvoje tělo legacy kód?
```

Popis:

```
Představ si program o třech miliardách znaků instrukcí, který se celý zkopíruje do každého
nového procesu — a ten pak devadesát devět procent z něj ignoruje. Zhruba tohle dělají tvoje
buňky.

Skoro každá buňka v tvém těle, která má jádro, nese tutéž úplnou kopii tvého genomu. Neuron ji
má. Jaterní buňka ji má. Chovají se přitom úplně jinak. Gen tak začne připomínat funkci — jenže
tu není žádný procesor, žádný ukazatel instrukcí a nic, co by vykonávalo DNA řádek po řádku.
O tom, které části se použijí, rozhoduje síť molekulárních interakcí, a mít kód se ukazuje být
něco úplně jiného než mít k němu přístup.

Odtud dál je softwarové přirovnání čím dál zvláštnější, ne slabší. Repozitář, jehož historie
commitů sahá čtyři miliardy let zpátky, držený na záplatách, protože přepsat se nedá nic.
Průběžná integrace, jejíž testy běží na produkčním systému. Biliony drobných agentů bez
centrálního serveru a bez kohokoli, kdo by měl architekturu v hlavě. A stroj, který běží
desítky let bez jediného restartu a přitom si vyměňuje vlastní součástky za provozu.

Pak se přirovnání zlomí, a to je na tom nejzajímavější. DNA není plán. Nikde v ní nestojí
řádek, který by říkal: vytvoř ruku. Umíme sekvenovat genom, určit geny a změřit bílkoviny —
a pořád neumíme vzít DNA obyčejné buňky, nahrát ji do počítače, stisknout spustit a sledovat,
jak vzniká člověk. Máme genom. Genom ale není celý ten stroj.

Celý text, zdroje a překlady: https://theresmoretoit-channel.github.io/cs/videos/is-your-body-legacy-code/

Kapitoly
0:00 Program, který by nikdo nenapsal
0:37 Každá buňka má celek
0:57 Geny vypadají jako funkce
1:35 Jenže tu není procesor
1:47 Co hraje roli ukazatele
2:49 Mít kód není mít k němu přístup
3:10 Modul jménem finger
3:42 Kdo tohle navrhl?
3:56 Čtyři miliardy let commitů
4:48 Nerefaktoruje
5:26 Kde jsou unit testy?
5:54 Když buňka vyhraje a ty prohraješ
6:16 Není tu centrální server
6:57 Tvoje tělo je distribuovaný systém
7:36 Nikdo to nikdy nerestartuje
8:39 A ono to nějak funguje
9:00 Kde se přirovnání láme
9:53 Nemáme zdrojový kód
10:15 Poslední paradox

Každý obraz v tomhle videu vznikl přímo pro něj, ať kresbou nebo generováním — není tu jediná
archivní fotka, takže není co uvádět. Hudba je procedurální, vygenerovaná v numpy.

Titulky jsou psané pro tohle video, ne strojový přepis. Jako druhá zvuková stopa je k dispozici americká angličtina.
```

---

## español (`es`)

Název:

```
¿Tu cuerpo es código heredado?
```

Popis:

```
Imagina un programa con tres mil millones de caracteres de instrucciones, copiado entero en
cada proceso nuevo — que luego ignora el noventa y nueve por ciento. Eso es más o menos lo que
hacen tus células.

Casi todas las células de tu cuerpo que tienen núcleo llevan la misma copia completa de tu
genoma. Una neurona la tiene. Una célula del hígado la tiene. Se comportan de forma
completamente distinta. Así que un gen empieza a parecerse a una función — solo que no hay
procesador, no hay puntero de instrucciones y no hay nada que ejecute el ADN línea por línea.
Lo que decide qué partes se usan es una red de interacciones moleculares, y tener el código
resulta ser muy distinto de tener acceso a él.

A partir de ahí la comparación con el software se vuelve más rara, no más débil. Un repositorio
cuyo historial de commits se remonta cuatro mil millones de años, sostenido a base de parches
porque nada puede reescribirse. Una integración continua cuyas pruebas corren sobre el sistema
en producción. Billones de agentes diminutos, sin servidor central y sin nadie que tenga la
arquitectura en la cabeza. Y una máquina que lleva décadas funcionando sin un solo reinicio,
cambiando sus propias piezas mientras atiende.

Luego la comparación se rompe, y eso es lo más interesante. El ADN no es un plano. En ninguna
parte hay una línea que diga: crea un brazo. Sabemos secuenciar un genoma, identificar genes y
medir proteínas — y seguimos sin poder meter el ADN de una célula corriente en un ordenador,
pulsar ejecutar y ver cómo se desarrolla una persona. Tenemos el genoma. El genoma no es la
máquina entera.

Transcripción completa, fuentes y traducciones: https://theresmoretoit-channel.github.io/es/videos/is-your-body-legacy-code/

Capítulos
0:00 El programa que nadie escribiría
0:37 Cada célula lleva el conjunto entero
0:57 Los genes parecen funciones
1:35 Pero no hay procesador
1:47 Qué hace el papel del puntero
2:49 Tener el código no es tener acceso
3:10 El módulo llamado finger
3:42 ¿Quién diseñó esto?
3:56 Cuatro mil millones de años de commits
4:48 No refactoriza
5:26 ¿Dónde están las pruebas unitarias?
5:54 Cuando una célula gana y tú pierdes
6:16 No hay servidor central
6:57 Tu cuerpo es un sistema distribuido
7:36 Nadie lo reinicia nunca
8:39 Y de algún modo funciona
9:00 Donde la comparación se rompe
9:53 No tenemos el código fuente
10:15 La paradoja final

Todas las imágenes de este vídeo se dibujaron o generaron para él — no hay ninguna fotografía
de archivo, así que no hay nada que acreditar. La música es procedimental, generada con numpy.

Los subtítulos están escritos para este vídeo, no generados automáticamente. Como segunda pista de audio está disponible el inglés americano.
```

---

## svenska (`sv`)

Název:

```
Är din kropp legacy-kod?
```

Popis:

```
Tänk dig ett program med tre miljarder tecken instruktioner, kopierat i sin helhet in i varje
ny process — som sedan struntar i nittionio procent av det. Ungefär så gör dina celler.

Nästan varje cell i din kropp som har en cellkärna bär på samma fullständiga kopia av ditt
genom. En neuron har den. En levercell har den. De beter sig helt olika. En gen börjar därmed
likna en funktion — förutom att det inte finns någon processor, ingen instruktionspekare och
ingenting som betar av DNA rad för rad. Det som avgör vilka delar som används är ett nät av
molekylära samspel, och att ha koden visar sig vara något helt annat än att komma åt den.

Därifrån blir mjukvarujämförelsen märkligare, inte svagare. Ett repositorium vars
commit-historik sträcker sig fyra miljarder år bakåt, hopfogat av lappar eftersom ingenting
någonsin kan skrivas om. En continuous integration vars tester körs på produktionssystemet.
Biljoner små agenter, utan central server och utan någon som håller arkitekturen i huvudet. Och
en maskin som kört i årtionden utan en enda omstart och byter ut sina egna delar under tiden.

Sedan brister jämförelsen, och det är det mest intressanta. DNA är ingen ritning. Ingenstans
står det en rad som säger: skapa en arm. Vi kan sekvensera ett genom, identifiera gener och
mäta proteiner — och vi kan fortfarande inte lägga in DNA från en vanlig cell i en dator,
trycka på kör och se en människa växa fram. Vi har genomet. Genomet är inte hela maskinen.

Hela texten, källor och översättningar: https://theresmoretoit-channel.github.io/sv/videos/is-your-body-legacy-code/

Kapitel
0:00 Programmet ingen skulle skriva
0:37 Varje cell har alltihop
0:57 Gener liknar funktioner
1:35 Men det finns ingen processor
1:47 Vad som spelar pekarens roll
2:49 Att ha koden är inte att komma åt den
3:10 Modulen som heter finger
3:42 Vem har designat det här?
3:56 Fyra miljarder år av commits
4:48 Den refaktorerar inte
5:26 Var är enhetstesterna?
5:54 När en cell vinner och du förlorar
6:16 Det finns ingen central server
6:57 Din kropp är ett distribuerat system
7:36 Ingen startar någonsin om den
8:39 Och ändå fungerar det
9:00 Där jämförelsen brister
9:53 Vi har inte källkoden
10:15 Den sista paradoxen

Varje bild i den här videon är ritad eller genererad för den — det finns inga arkivfoton, så
det finns inget att kreditera. Musiken är procedurell, genererad med numpy.

Undertexterna är skrivna för den här videon, inte automatgenererade. Som andra ljudspår finns amerikansk engelska.
```
