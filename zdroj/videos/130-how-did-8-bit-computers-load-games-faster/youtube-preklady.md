# YouTube — 130 „How Did 8-Bit Computers Load Games Faster?“: lokalizace

Lokalizované názvy a popisy pro třináct jazyků (bez `en`, ten je
v `youtube.md`). Pořadí podle YouTube Studia. Nahrává
`python tools/lokalizace.py videos/130-how-did-8-bit-computers-load-games-faster`.

**Co se NEPŘEKLÁDÁ:**

- vlastní jména (ZX Spectrum, Commodore 64, Atari, Sharp MZ-800,
  Speedlock, Skool Daze, SkoolKit, TurboTape, Turbo 2000, Turbo Copy,
  ROM…),
- časy kapitol, ty jsou na vteřinu shodné s angličtinou,
- citace v řádku zdrojů (názvy publikací, čísla a měsíce vydání, popisné
  části citací jako „on Speedlock“, „on Turbo 2000“) — přeložené je jen
  úvodní slovo „Sources:“ a spojka „and“ tam, kde spojuje dva různé
  zdroje (ROM disassembly + SkoolKit, World of Spectrum + CPCWiki,
  oldcomp.cz + atari-800.cz); „CRASH #24 and #44“ a „Compute! #56 and
  #57, January and February 1985“ jsou jedna citace a zůstávají,
- řádky s atribucí snímků (TASL) zůstávají jako v angličtině; přeložené
  jsou jen nadpis, „via“, „Licences“ a „(thumbnail)“,
- tagy — YouTube je pro jednotlivé jazyky nemá.

Pointa videa (S89 „It needed a better way to listen“, S80–S84 jak
Turbo Copy hru „opravil“) se v popisu neprozrazuje, stejně jako
v angličtině. Odstavec o titulcích a americké stopě je doslova
z kanonické tabulky v `docs/zverejneni.md`. Terminologie podle titulků
videa (`script.<kód>.md`: turbo zavaděč, magnetofon, disketa…). Registr
neformální tam, kde jazyk volbu má (český překlad scénáře tyká, rodově
neutrálně); finština „sinä“, vietnamština „bạn“, španělština evropská,
portugalština „você“.

## suomi (`fi`)

```
Miten 8-bittiset tietokoneet latasivat pelit nopeammin?
```

```
Sama tietokone. Samanlainen kasetti. Sama ohjelma. Yksi versio latautuu puolessa ajassa. Laitteistossa ei muuttunut mitään, joten mikä muuttui?

Tässä videossa tutustutaan 8-bittisten kotitietokoneiden turbolataajiin: miten ZX Spectrumin peli pystyi latautumaan kaksinkertaisella nopeudella, miksi Spectrum ei tehnyt sitä itse ja miten tietokone, joka ymmärtää vain hitaan formaatin, lataa ohjelman, joka opettaa sille nopean. Matkan varrella: Speedlock ja miksi se ei ollut tehty vain nopeuttamaan latausta, Commodore 64:n kasetti, joka voittaa levykkeen, Tšekkoslovakian Atari-omistajat, jotka avasivat nauhurinsa, sekä Sharp MZ-800:n ohjelma, jolla sai ladattua pelejä, joita tietokone itse ei suostunut lataamaan.

Videon latausäänet on tuotettu oikeista latausrutiineista (kopio Spectrumin ROM-lataajasta Skool Dazen käyttämillä vakioilla) ja tarkistettu emulaattorissa. Koko turbonauha soi lopussa.

Lähteet: ZX Spectrum ROM disassembly (LD-BYTES) ja SkoolKit's Skool Daze disassembly; Your Sinclair, May 1986 (Turboloader); CRASH #24 and #44 (David Aubrey-Jones on Speedlock); World of Spectrum ja CPCWiki on Speedlock; Compute! #56 and #57, January and February 1985 (TurboTape); Michael Steil, pagetable.com, C64 KERNAL disassembly; Commodore C2N Datassette service manual; ANTIC, February 1983, on the Atari cassette recorder; oldcomp.cz ja atari-800.cz on Turbo 2000; Sharp MZ-800 Technical Reference Manual; Sharp MZ-800 emulator archive (Turbo Copy).

Tekstitykset on kirjoitettu tätä videota varten, ei luotu automaattisesti. Toisena ääniraitana on amerikanenglanti.

LUVUT
00:00 Sama nauha, puolet ajasta
00:37 Lyhennä jokainen pulssi
01:22 Miksi Spectrum ei tehnyt sitä itse
02:34 Lataaja, joka lataa lataajan
03:26 Speedlock
04:42 Commodore 64: kasetti voittaa levykkeen
05:55 Atari: avaa nauhuri
07:09 Nopeuden hinta
07:45 Ohjelma, joka korjasi pelejä
08:19 Etukäteen asetettu sekuntikello
09:42 Mikä niille kaikille on yhteistä
10:17 Kysymys sinulle
10:27 Koko turbonauha

KUVALÄHTEET
Commodore 64 with the external power supply and Commodore 1530 (C2N) Datasette — Xavier Caballe, CC BY-SA 2.0
Atari 800 XL home computer with monitor and tape program recorder XC12 — winkelnkemper, CC BY-SA 2.0
Sharp MZ-821 — Superandi73, CC BY-SA 3.0
Compact Cassette C60, Tape, Labelled, Face (pikkukuva) — stuart.childs, CC BY 2.0
Wikimedia Commonsin kautta
Lisenssit: creativecommons.org/licenses/by-sa/2.0, creativecommons.org/licenses/by-sa/3.0, creativecommons.org/licenses/by/2.0
```

## français (`fr`)

```
Comment les ordinateurs 8 bits chargeaient-ils les jeux plus vite ?
```

```
Même ordinateur. Même type de cassette. Même programme. Une version se charge en deux fois moins de temps. Rien n’a changé dans le matériel, alors qu’est-ce qui a changé ?

Cette vidéo s’intéresse aux chargeurs turbo des ordinateurs familiaux 8 bits : comment un jeu ZX Spectrum pouvait se charger deux fois plus vite que la normale, pourquoi le Spectrum ne le faisait pas de lui-même, et comment un ordinateur qui ne comprend que le format lent charge le programme qui lui apprend le format rapide. On y croise aussi Speedlock et la raison pour laquelle il ne servait pas qu’à charger plus vite, une cassette de Commodore 64 qui bat une disquette, des possesseurs d’Atari en Tchécoslovaquie qui ouvraient leur magnétophone, et un programme pour Sharp MZ-800 capable de charger des jeux que l’ordinateur lui-même refusait.

Les sons de chargement de cette vidéo ont été générés à partir des vraies routines de chargement (une copie du chargeur de la ROM du Spectrum avec les constantes qu’utilisait Skool Daze) et vérifiés dans un émulateur. La bande turbo passe en entier à la fin.

Sources : ZX Spectrum ROM disassembly (LD-BYTES) et SkoolKit's Skool Daze disassembly ; Your Sinclair, May 1986 (Turboloader) ; CRASH #24 and #44 (David Aubrey-Jones on Speedlock) ; World of Spectrum et CPCWiki on Speedlock ; Compute! #56 and #57, January and February 1985 (TurboTape) ; Michael Steil, pagetable.com, C64 KERNAL disassembly ; Commodore C2N Datassette service manual ; ANTIC, February 1983, on the Atari cassette recorder ; oldcomp.cz et atari-800.cz on Turbo 2000 ; Sharp MZ-800 Technical Reference Manual ; Sharp MZ-800 emulator archive (Turbo Copy).

Les sous-titres sont écrits pour cette vidéo, pas générés automatiquement. Une piste audio en anglais américain est disponible en seconde piste.

CHAPITRES
00:00 Même bande, deux fois moins de temps
00:37 Raccourcir chaque impulsion
01:22 Pourquoi le Spectrum ne le faisait pas tout seul
02:34 Le chargeur qui charge le chargeur
03:26 Speedlock
04:42 Commodore 64 : une cassette bat une disquette
05:55 Atari : ouvrir le magnétophone
07:09 Le prix de la vitesse
07:45 Le programme qui réparait les jeux
08:19 Un chronomètre réglé à l’avance
09:42 Ce qu’ils ont tous en commun
10:17 Une question pour toi
10:27 Toute la bande turbo

CRÉDITS DES IMAGES
Commodore 64 with the external power supply and Commodore 1530 (C2N) Datasette — Xavier Caballe, CC BY-SA 2.0
Atari 800 XL home computer with monitor and tape program recorder XC12 — winkelnkemper, CC BY-SA 2.0
Sharp MZ-821 — Superandi73, CC BY-SA 3.0
Compact Cassette C60, Tape, Labelled, Face (miniature) — stuart.childs, CC BY 2.0
via Wikimedia Commons
Licences : creativecommons.org/licenses/by-sa/2.0, creativecommons.org/licenses/by-sa/3.0, creativecommons.org/licenses/by/2.0
```

## Bahasa Indonesia (`id`)

```
Bagaimana komputer 8-bit memuat game lebih cepat?
```

```
Komputer yang sama. Jenis kaset yang sama. Program yang sama. Satu versi selesai dimuat dalam separuh waktu. Tidak ada yang berubah di perangkat kerasnya, lalu apa yang berubah?

Video ini membahas turbo loader di komputer rumahan 8-bit: bagaimana game ZX Spectrum bisa dimuat dua kali lebih cepat dari biasanya, kenapa Spectrum tidak melakukannya sendiri, dan bagaimana komputer yang hanya mengerti format lambat memuat program yang mengajarinya format cepat. Video ini juga membahas Speedlock dan kenapa ia tidak hanya bertujuan mempercepat pemuatan, kaset Commodore 64 yang mengalahkan disket, pemilik Atari di Cekoslowakia yang membongkar tape recorder mereka, dan program Sharp MZ-800 yang bisa memuat game yang ditolak oleh komputernya sendiri.

Suara loading dalam video ini dibuat dari rutin loading yang asli (salinan loader ROM Spectrum dengan konstanta yang dipakai Skool Daze) dan diperiksa di emulator. Seluruh pita turbo diputar di bagian akhir.

Sumber: ZX Spectrum ROM disassembly (LD-BYTES) dan SkoolKit's Skool Daze disassembly; Your Sinclair, May 1986 (Turboloader); CRASH #24 and #44 (David Aubrey-Jones on Speedlock); World of Spectrum dan CPCWiki on Speedlock; Compute! #56 and #57, January and February 1985 (TurboTape); Michael Steil, pagetable.com, C64 KERNAL disassembly; Commodore C2N Datassette service manual; ANTIC, February 1983, on the Atari cassette recorder; oldcomp.cz dan atari-800.cz on Turbo 2000; Sharp MZ-800 Technical Reference Manual; Sharp MZ-800 emulator archive (Turbo Copy).

Subtitel ditulis khusus untuk video ini, bukan dibuat secara otomatis. Tersedia juga trek audio kedua dalam bahasa Inggris Amerika.

BAB
00:00 Pita yang sama, separuh waktu
00:37 Perpendek setiap pulsa
01:22 Kenapa Spectrum tidak melakukannya sendiri
02:34 Loader yang memuat loader
03:26 Speedlock
04:42 Commodore 64: kaset mengalahkan disket
05:55 Atari: bongkar tape recorder-nya
07:09 Harga dari kecepatan
07:45 Program yang memperbaiki game
08:19 Stopwatch yang disetel sebelumnya
09:42 Apa kesamaan semuanya
10:17 Pertanyaan untukmu
10:27 Seluruh pita turbo

KREDIT GAMBAR
Commodore 64 with the external power supply and Commodore 1530 (C2N) Datasette — Xavier Caballe, CC BY-SA 2.0
Atari 800 XL home computer with monitor and tape program recorder XC12 — winkelnkemper, CC BY-SA 2.0
Sharp MZ-821 — Superandi73, CC BY-SA 3.0
Compact Cassette C60, Tape, Labelled, Face (gambar mini) — stuart.childs, CC BY 2.0
melalui Wikimedia Commons
Lisensi: creativecommons.org/licenses/by-sa/2.0, creativecommons.org/licenses/by-sa/3.0, creativecommons.org/licenses/by/2.0
```

## italiano (`it`)

```
Come facevano i computer a 8 bit a caricare i giochi più in fretta?
```

```
Stesso computer. Stesso tipo di cassetta. Stesso programma. Una versione si carica in metà tempo. Nell’hardware non è cambiato niente, quindi cos’è cambiato?

Questo video parla dei caricatori turbo degli home computer a 8 bit: come un gioco per ZX Spectrum poteva caricarsi al doppio della velocità normale, perché lo Spectrum non lo faceva da solo e come un computer che capisce solo il formato lento carica il programma che gli insegna quello veloce. Si parla anche di Speedlock e del perché non serviva solo a caricare più in fretta, di una cassetta del Commodore 64 che batte un floppy disk, dei possessori di Atari in Cecoslovacchia che aprivano i loro registratori e di un programma per Sharp MZ-800 che riusciva a caricare giochi che il computer stesso rifiutava.

I suoni di caricamento di questo video sono stati generati dalle vere routine di caricamento (una copia del caricatore della ROM dello Spectrum con le costanti usate da Skool Daze) e verificati in un emulatore. L’intero nastro turbo viene riprodotto alla fine.

Fonti: ZX Spectrum ROM disassembly (LD-BYTES) e SkoolKit's Skool Daze disassembly; Your Sinclair, May 1986 (Turboloader); CRASH #24 and #44 (David Aubrey-Jones on Speedlock); World of Spectrum e CPCWiki on Speedlock; Compute! #56 and #57, January and February 1985 (TurboTape); Michael Steil, pagetable.com, C64 KERNAL disassembly; Commodore C2N Datassette service manual; ANTIC, February 1983, on the Atari cassette recorder; oldcomp.cz e atari-800.cz on Turbo 2000; Sharp MZ-800 Technical Reference Manual; Sharp MZ-800 emulator archive (Turbo Copy).

I sottotitoli sono scritti per questo video, non generati automaticamente. Come seconda traccia audio è disponibile l’inglese americano.

CAPITOLI
00:00 Stesso nastro, metà tempo
00:37 Accorcia ogni impulso
01:22 Perché lo Spectrum non lo faceva da solo
02:34 Il caricatore che carica il caricatore
03:26 Speedlock
04:42 Commodore 64: una cassetta batte un floppy
05:55 Atari: apri il registratore
07:09 Il prezzo della velocità
07:45 Il programma che riparava i giochi
08:19 Un cronometro regolato in anticipo
09:42 Cosa hanno tutti in comune
10:17 Una domanda per te
10:27 L’intero nastro turbo

CREDITI DELLE IMMAGINI
Commodore 64 with the external power supply and Commodore 1530 (C2N) Datasette — Xavier Caballe, CC BY-SA 2.0
Atari 800 XL home computer with monitor and tape program recorder XC12 — winkelnkemper, CC BY-SA 2.0
Sharp MZ-821 — Superandi73, CC BY-SA 3.0
Compact Cassette C60, Tape, Labelled, Face (miniatura) — stuart.childs, CC BY 2.0
tramite Wikimedia Commons
Licenze: creativecommons.org/licenses/by-sa/2.0, creativecommons.org/licenses/by-sa/3.0, creativecommons.org/licenses/by/2.0
```

## Deutsch (`de`)

```
Wie luden 8-Bit-Computer Spiele schneller?
```

```
Derselbe Computer. Dieselbe Art Kassette. Dasselbe Programm. Eine Version lädt in der halben Zeit. An der Hardware hat sich nichts geändert, also was dann?

In diesem Video geht es um Turbo-Loader auf 8-Bit-Heimcomputern: wie ein Spiel für das ZX Spectrum mit doppelter Geschwindigkeit laden konnte, warum das Spectrum das nicht von selbst tat und wie ein Computer, der nur das langsame Format versteht, das Programm lädt, das ihm das schnelle beibringt. Und nebenbei: Speedlock und warum es dabei nicht nur ums Tempo ging, eine Commodore-64-Kassette, die eine Diskette schlägt, Atari-Besitzer in der Tschechoslowakei, die ihre Kassettenrekorder aufschraubten, und ein Programm für den Sharp MZ-800, das Spiele laden konnte, die der Computer selbst nicht laden wollte.

Die Ladegeräusche in diesem Video wurden aus den echten Laderoutinen erzeugt (einer Kopie des ROM-Laders des Spectrum mit den Konstanten, die Skool Daze verwendete) und in einem Emulator überprüft. Das ganze Turbo-Band läuft am Ende.

Quellen: ZX Spectrum ROM disassembly (LD-BYTES) und SkoolKit's Skool Daze disassembly; Your Sinclair, May 1986 (Turboloader); CRASH #24 and #44 (David Aubrey-Jones on Speedlock); World of Spectrum und CPCWiki on Speedlock; Compute! #56 and #57, January and February 1985 (TurboTape); Michael Steil, pagetable.com, C64 KERNAL disassembly; Commodore C2N Datassette service manual; ANTIC, February 1983, on the Atari cassette recorder; oldcomp.cz und atari-800.cz on Turbo 2000; Sharp MZ-800 Technical Reference Manual; Sharp MZ-800 emulator archive (Turbo Copy).

Die Untertitel wurden für dieses Video geschrieben, nicht automatisch erzeugt. Als zweite Tonspur steht amerikanisches Englisch bereit.

KAPITEL
00:00 Dasselbe Band, die halbe Zeit
00:37 Jeden Impuls kürzer machen
01:22 Warum das Spectrum es nicht von selbst tat
02:34 Der Lader, der den Lader lädt
03:26 Speedlock
04:42 Commodore 64: Eine Kassette schlägt eine Diskette
05:55 Atari: Rekorder aufschrauben
07:09 Der Preis der Geschwindigkeit
07:45 Das Programm, das Spiele reparierte
08:19 Eine im Voraus eingestellte Stoppuhr
09:42 Was sie alle gemeinsam haben
10:17 Eine Frage an dich
10:27 Das ganze Turbo-Band

BILDNACHWEIS
Commodore 64 with the external power supply and Commodore 1530 (C2N) Datasette — Xavier Caballe, CC BY-SA 2.0
Atari 800 XL home computer with monitor and tape program recorder XC12 — winkelnkemper, CC BY-SA 2.0
Sharp MZ-821 — Superandi73, CC BY-SA 3.0
Compact Cassette C60, Tape, Labelled, Face (Vorschaubild) — stuart.childs, CC BY 2.0
über Wikimedia Commons
Lizenzen: creativecommons.org/licenses/by-sa/2.0, creativecommons.org/licenses/by-sa/3.0, creativecommons.org/licenses/by/2.0
```

## polski (`pl`)

```
Jak komputery 8-bitowe szybciej wczytywały gry?
```

```
Ten sam komputer. Ten sam rodzaj kasety. Ten sam program. Jedna wersja wczytuje się o połowę krócej. Sprzęt się nie zmienił, więc co się zmieniło?

Ten film opowiada o programach ładujących turbo w 8-bitowych komputerach domowych: jak gra na ZX Spectrum mogła się wczytywać dwa razy szybciej niż normalnie, dlaczego Spectrum nie robiło tego samo i jak komputer, który rozumie tylko wolny format, wczytuje program, który nauczy go szybkiego. Po drodze: Speedlock i to, dlaczego nie służył tylko do przyspieszania wczytywania, kaseta do Commodore 64, która wygrywa z dyskietką, właściciele Atari w Czechosłowacji, którzy otwierali swoje magnetofony, oraz program na Sharpa MZ-800, który potrafił wczytać gry odrzucane przez sam komputer.

Dźwięki ładowania w tym filmie wygenerowano na podstawie prawdziwych procedur ładujących (kopii programu ładującego z ROM-u Spectrum ze stałymi, których używało Skool Daze) i sprawdzono w emulatorze. Cała taśma turbo leci na końcu.

Źródła: ZX Spectrum ROM disassembly (LD-BYTES) i SkoolKit's Skool Daze disassembly; Your Sinclair, May 1986 (Turboloader); CRASH #24 and #44 (David Aubrey-Jones on Speedlock); World of Spectrum i CPCWiki on Speedlock; Compute! #56 and #57, January and February 1985 (TurboTape); Michael Steil, pagetable.com, C64 KERNAL disassembly; Commodore C2N Datassette service manual; ANTIC, February 1983, on the Atari cassette recorder; oldcomp.cz i atari-800.cz on Turbo 2000; Sharp MZ-800 Technical Reference Manual; Sharp MZ-800 emulator archive (Turbo Copy).

Napisy są pisane do tego filmu, nie generowane automatycznie. Jako druga ścieżka dźwiękowa dostępny jest angielski amerykański.

ROZDZIAŁY
00:00 Ta sama taśma, o połowę krócej
00:37 Skróć każdy impuls
01:22 Dlaczego Spectrum nie robiło tego samo
02:34 Program ładujący, który wczytuje program ładujący
03:26 Speedlock
04:42 Commodore 64: kaseta wygrywa z dyskietką
05:55 Atari: otwórz magnetofon
07:09 Cena szybkości
07:45 Program, który naprawiał gry
08:19 Stoper nastawiony z góry
09:42 Co je wszystkie łączy
10:17 Pytanie do ciebie
10:27 Cała taśma turbo

ŹRÓDŁA ZDJĘĆ
Commodore 64 with the external power supply and Commodore 1530 (C2N) Datasette — Xavier Caballe, CC BY-SA 2.0
Atari 800 XL home computer with monitor and tape program recorder XC12 — winkelnkemper, CC BY-SA 2.0
Sharp MZ-821 — Superandi73, CC BY-SA 3.0
Compact Cassette C60, Tape, Labelled, Face (miniatura) — stuart.childs, CC BY 2.0
przez Wikimedia Commons
Licencje: creativecommons.org/licenses/by-sa/2.0, creativecommons.org/licenses/by-sa/3.0, creativecommons.org/licenses/by/2.0
```

## português (Brasil) (`pt-BR`)

```
Como os computadores de 8 bits carregavam jogos mais rápido?
```

```
Mesmo computador. Mesmo tipo de fita. Mesmo programa. Uma versão carrega na metade do tempo. Nada mudou no hardware, então o que mudou?

Este vídeo fala dos carregadores turbo dos computadores domésticos de 8 bits: como um jogo de ZX Spectrum conseguia carregar no dobro da velocidade normal, por que o Spectrum não fazia isso sozinho e como um computador que só entende o formato lento carrega o programa que ensina o rápido para ele. O vídeo também aborda o Speedlock e por que ele não servia apenas para acelerar o carregamento, uma fita de Commodore 64 vencendo um disquete, donos de Atari na Tchecoslováquia abrindo seus gravadores e um programa para o Sharp MZ-800 que conseguia carregar jogos que o próprio computador recusava.

Os sons de carregamento deste vídeo foram gerados a partir das rotinas de carregamento reais (uma cópia do carregador da ROM do Spectrum com as constantes que o Skool Daze usava) e conferidos num emulador. A fita turbo inteira toca no final.

Fontes: ZX Spectrum ROM disassembly (LD-BYTES) e SkoolKit's Skool Daze disassembly; Your Sinclair, May 1986 (Turboloader); CRASH #24 and #44 (David Aubrey-Jones on Speedlock); World of Spectrum e CPCWiki on Speedlock; Compute! #56 and #57, January and February 1985 (TurboTape); Michael Steil, pagetable.com, C64 KERNAL disassembly; Commodore C2N Datassette service manual; ANTIC, February 1983, on the Atari cassette recorder; oldcomp.cz e atari-800.cz on Turbo 2000; Sharp MZ-800 Technical Reference Manual; Sharp MZ-800 emulator archive (Turbo Copy).

As legendas foram escritas para este vídeo, não geradas automaticamente. Como segunda faixa de áudio está disponível o inglês americano.

CAPÍTULOS
00:00 Mesma fita, metade do tempo
00:37 Encurte cada pulso
01:22 Por que o Spectrum não fazia isso sozinho
02:34 O carregador que carrega o carregador
03:26 Speedlock
04:42 Commodore 64: uma fita vence um disquete
05:55 Atari: abra o gravador
07:09 O preço da velocidade
07:45 O programa que consertava jogos
08:19 Um cronômetro ajustado de antemão
09:42 O que todos têm em comum
10:17 Uma pergunta para você
10:27 A fita turbo inteira

CRÉDITOS DAS IMAGENS
Commodore 64 with the external power supply and Commodore 1530 (C2N) Datasette — Xavier Caballe, CC BY-SA 2.0
Atari 800 XL home computer with monitor and tape program recorder XC12 — winkelnkemper, CC BY-SA 2.0
Sharp MZ-821 — Superandi73, CC BY-SA 3.0
Compact Cassette C60, Tape, Labelled, Face (miniatura) — stuart.childs, CC BY 2.0
via Wikimedia Commons
Licenças: creativecommons.org/licenses/by-sa/2.0, creativecommons.org/licenses/by-sa/3.0, creativecommons.org/licenses/by/2.0
```

## Türkçe (`tr`)

```
8 bitlik bilgisayarlar oyunları nasıl daha hızlı yüklüyordu?
```

```
Aynı bilgisayar. Aynı tür kaset. Aynı program. Bir sürüm yarı sürede yükleniyor. Donanımda hiçbir şey değişmedi, peki ne değişti?

Bu video 8 bitlik ev bilgisayarlarındaki turbo yükleyicileri ele alıyor: bir ZX Spectrum oyununun nasıl normal hızın iki katında yüklenebildiğini, Spectrum'un bunu neden kendiliğinden yapmadığını ve yalnızca yavaş formatı anlayan bir bilgisayarın, ona hızlı formatı öğretecek programı nasıl yüklediğini. Videoda ayrıca şunlar var: Speedlock ve neden yalnızca yüklemeyi hızlandırmak için kullanılmadığı, bir disketi geçen bir Commodore 64 kaseti, Çekoslovakya'da teyplerinin kasasını açan Atari sahipleri ve bilgisayarın kendisinin reddettiği oyunları yükleyebilen bir Sharp MZ-800 programı.

Bu videodaki yükleme sesleri gerçek yükleme rutinlerinden üretildi (Spectrum'un ROM yükleyicisinin, Skool Daze'in kullandığı sabitlerle yapılmış bir kopyası) ve bir emülatörde kontrol edildi. Turbo bandın tamamı sonda çalıyor.

Kaynaklar: ZX Spectrum ROM disassembly (LD-BYTES) ve SkoolKit's Skool Daze disassembly; Your Sinclair, May 1986 (Turboloader); CRASH #24 and #44 (David Aubrey-Jones on Speedlock); World of Spectrum ve CPCWiki on Speedlock; Compute! #56 and #57, January and February 1985 (TurboTape); Michael Steil, pagetable.com, C64 KERNAL disassembly; Commodore C2N Datassette service manual; ANTIC, February 1983, on the Atari cassette recorder; oldcomp.cz ve atari-800.cz on Turbo 2000; Sharp MZ-800 Technical Reference Manual; Sharp MZ-800 emulator archive (Turbo Copy).

Altyazılar bu video için yazıldı, otomatik olarak oluşturulmadı. İkinci ses parçası olarak Amerikan İngilizcesi de mevcut.

BÖLÜMLER
00:00 Aynı bant, yarı süre
00:37 Her darbeyi kısalt
01:22 Spectrum bunu neden kendisi yapmadı
02:34 Yükleyiciyi yükleyen yükleyici
03:26 Speedlock
04:42 Commodore 64: kaset disketi geçiyor
05:55 Atari: teybin kasasını aç
07:09 Hızın bedeli
07:45 Oyunları onaran program
08:19 Önceden ayarlanmış bir kronometre
09:42 Hepsinin ortak noktası
10:17 Sana bir soru
10:27 Turbo bandın tamamı

GÖRSEL KAYNAKLARI
Commodore 64 with the external power supply and Commodore 1530 (C2N) Datasette — Xavier Caballe, CC BY-SA 2.0
Atari 800 XL home computer with monitor and tape program recorder XC12 — winkelnkemper, CC BY-SA 2.0
Sharp MZ-821 — Superandi73, CC BY-SA 3.0
Compact Cassette C60, Tape, Labelled, Face (küçük resim) — stuart.childs, CC BY 2.0
Wikimedia Commons aracılığıyla
Lisanslar: creativecommons.org/licenses/by-sa/2.0, creativecommons.org/licenses/by-sa/3.0, creativecommons.org/licenses/by/2.0
```

## українська (`uk`)

```
Як 8-бітні комп’ютери швидше завантажували ігри?
```

```
Той самий комп’ютер. Той самий тип касети. Та сама програма. Одна версія завантажується вдвічі швидше. У залізі нічого не змінилося, то що ж змінилося?

Це відео розповідає про турбозавантажувачі на 8-бітних домашніх комп’ютерах: як гра для ZX Spectrum могла завантажуватися вдвічі швидше, ніж зазвичай, чому Spectrum не робив цього сам і як комп’ютер, що розуміє лише повільний формат, завантажує програму, яка навчить його швидкого. А ще у відео: Speedlock і чому він не лише прискорював завантаження, касета для Commodore 64, що обганяє дискету, власники Atari в Чехословаччині, які розкривали свої магнітофони, і програма для Sharp MZ-800, яка могла завантажити ігри, що їх відкидав сам комп’ютер.

Звуки завантаження в цьому відео згенеровано зі справжніх процедур завантаження (копії завантажувача з ROM Spectrum з константами, які використовувала Skool Daze) і перевірено в емуляторі. Уся турбострічка звучить наприкінці.

Джерела: ZX Spectrum ROM disassembly (LD-BYTES) та SkoolKit's Skool Daze disassembly; Your Sinclair, May 1986 (Turboloader); CRASH #24 and #44 (David Aubrey-Jones on Speedlock); World of Spectrum та CPCWiki on Speedlock; Compute! #56 and #57, January and February 1985 (TurboTape); Michael Steil, pagetable.com, C64 KERNAL disassembly; Commodore C2N Datassette service manual; ANTIC, February 1983, on the Atari cassette recorder; oldcomp.cz та atari-800.cz on Turbo 2000; Sharp MZ-800 Technical Reference Manual; Sharp MZ-800 emulator archive (Turbo Copy).

Субтитри написані для цього відео, а не згенеровані автоматично. Також доступна друга звукова доріжка — американською англійською.

РОЗДІЛИ
00:00 Та сама стрічка, удвічі швидше
00:37 Скороти кожен імпульс
01:22 Чому Spectrum не робив цього сам
02:34 Завантажувач, що завантажує завантажувач
03:26 Speedlock
04:42 Commodore 64: касета обганяє дискету
05:55 Atari: розкрий магнітофон
07:09 Ціна швидкості
07:45 Програма, що лагодила ігри
08:19 Секундомір, налаштований наперед
09:42 Що їх усіх об’єднує
10:17 Запитання до тебе
10:27 Уся турбострічка

ДЖЕРЕЛА ЗОБРАЖЕНЬ
Commodore 64 with the external power supply and Commodore 1530 (C2N) Datasette — Xavier Caballe, CC BY-SA 2.0
Atari 800 XL home computer with monitor and tape program recorder XC12 — winkelnkemper, CC BY-SA 2.0
Sharp MZ-821 — Superandi73, CC BY-SA 3.0
Compact Cassette C60, Tape, Labelled, Face (мініатюра) — stuart.childs, CC BY 2.0
через Wikimedia Commons
Ліцензії: creativecommons.org/licenses/by-sa/2.0, creativecommons.org/licenses/by-sa/3.0, creativecommons.org/licenses/by/2.0
```

## Tiếng Việt (`vi`)

```
Máy tính 8-bit đã tải game nhanh hơn bằng cách nào?
```

```
Cùng một máy tính. Cùng một loại băng cassette. Cùng một chương trình. Một phiên bản tải xong chỉ trong một nửa thời gian. Phần cứng không hề thay đổi, vậy thứ gì đã thay đổi?

Video này tìm hiểu các trình tải turbo trên máy tính gia đình 8-bit: một game ZX Spectrum có thể tải nhanh gấp đôi tốc độ bình thường như thế nào, vì sao Spectrum không tự làm điều đó, và một máy tính chỉ hiểu định dạng chậm tải chương trình dạy nó định dạng nhanh bằng cách nào. Video cũng đề cập đến Speedlock và vì sao nó không chỉ có nhiệm vụ tăng tốc độ tải, một cuộn băng Commodore 64 đánh bại đĩa mềm, những người dùng Atari ở Tiệp Khắc mở máy cassette của mình ra, và một chương trình trên Sharp MZ-800 có thể tải những game mà chính chiếc máy tính từ chối.

Âm thanh tải trong video này được tạo ra từ các thủ tục tải thật (một bản sao trình tải trong ROM của Spectrum với các hằng số mà Skool Daze đã dùng) và được kiểm tra trên trình giả lập. Toàn bộ cuộn băng turbo được phát ở cuối video.

Nguồn: ZX Spectrum ROM disassembly (LD-BYTES) và SkoolKit's Skool Daze disassembly; Your Sinclair, May 1986 (Turboloader); CRASH #24 and #44 (David Aubrey-Jones on Speedlock); World of Spectrum và CPCWiki on Speedlock; Compute! #56 and #57, January and February 1985 (TurboTape); Michael Steil, pagetable.com, C64 KERNAL disassembly; Commodore C2N Datassette service manual; ANTIC, February 1983, on the Atari cassette recorder; oldcomp.cz và atari-800.cz on Turbo 2000; Sharp MZ-800 Technical Reference Manual; Sharp MZ-800 emulator archive (Turbo Copy).

Phụ đề được viết riêng cho video này, không phải tạo tự động. Có thể chọn tiếng Anh Mỹ ở bản âm thanh thứ hai.

CHƯƠNG
00:00 Cùng cuộn băng, một nửa thời gian
00:37 Rút ngắn mọi xung
01:22 Vì sao Spectrum không tự làm
02:34 Trình tải dùng để tải trình tải
03:26 Speedlock
04:42 Commodore 64: băng cassette thắng đĩa mềm
05:55 Atari: mở máy cassette ra
07:09 Cái giá của tốc độ
07:45 Chương trình sửa game
08:19 Đồng hồ bấm giờ cài sẵn từ trước
09:42 Điểm chung của tất cả
10:17 Câu hỏi dành cho bạn
10:27 Toàn bộ cuộn băng turbo

NGUỒN HÌNH ẢNH
Commodore 64 with the external power supply and Commodore 1530 (C2N) Datasette — Xavier Caballe, CC BY-SA 2.0
Atari 800 XL home computer with monitor and tape program recorder XC12 — winkelnkemper, CC BY-SA 2.0
Sharp MZ-821 — Superandi73, CC BY-SA 3.0
Compact Cassette C60, Tape, Labelled, Face (ảnh thu nhỏ) — stuart.childs, CC BY 2.0
qua Wikimedia Commons
Giấy phép: creativecommons.org/licenses/by-sa/2.0, creativecommons.org/licenses/by-sa/3.0, creativecommons.org/licenses/by/2.0
```

## čeština (`cs`)

```
Jak osmibitové počítače nahrávaly hry rychleji?
```

```
Stejný počítač. Stejný druh kazety. Stejný program. Jedna verze se nahraje za poloviční dobu. Na hardwaru se nic nezměnilo, tak co se změnilo?

Tohle video je o turbo zavaděčích osmibitových domácích počítačů: jak se hra pro ZX Spectrum mohla nahrávat dvojnásobnou rychlostí, proč to Spectrum nedělalo samo a jak počítač, který rozumí jen pomalému formátu, nahraje program, který ho naučí ten rychlý. Dojde i na Speedlock a na to, proč nesloužil jen k rychlejšímu nahrávání, na kazetu pro Commodore 64, která porazila disketu, na majitele Atari v Československu, kteří otevírali své magnetofony, a na program pro Sharp MZ-800, který uměl nahrát hry, jež počítač sám odmítl.

Nahrávací zvuky v tomhle videu jsou vygenerované ze skutečných nahrávacích rutin (kopie zavaděče z ROM Spectra s konstantami, jaké používala hra Skool Daze) a ověřené v emulátoru. Celá turbo páska zazní na konci.

Zdroje: ZX Spectrum ROM disassembly (LD-BYTES) a SkoolKit's Skool Daze disassembly; Your Sinclair, May 1986 (Turboloader); CRASH #24 and #44 (David Aubrey-Jones on Speedlock); World of Spectrum a CPCWiki on Speedlock; Compute! #56 and #57, January and February 1985 (TurboTape); Michael Steil, pagetable.com, C64 KERNAL disassembly; Commodore C2N Datassette service manual; ANTIC, February 1983, on the Atari cassette recorder; oldcomp.cz a atari-800.cz on Turbo 2000; Sharp MZ-800 Technical Reference Manual; Sharp MZ-800 emulator archive (Turbo Copy).

Titulky jsou psané pro tohle video, ne strojový přepis. Jako druhá zvuková stopa je k dispozici americká angličtina.

KAPITOLY
00:00 Stejná páska, poloviční doba
00:37 Zkrať každý pulz
01:22 Proč to Spectrum nedělalo samo
02:34 Zavaděč, který nahraje zavaděč
03:26 Speedlock
04:42 Commodore 64: kazeta poráží disketu
05:55 Atari: otevři magnetofon
07:09 Cena za rychlost
07:45 Program, který opravoval hry
08:19 Stopky nastavené předem
09:42 Co mají všechny společné
10:17 Otázka pro tebe
10:27 Celá turbo páska

AUTOŘI SNÍMKŮ
Commodore 64 with the external power supply and Commodore 1530 (C2N) Datasette — Xavier Caballe, CC BY-SA 2.0
Atari 800 XL home computer with monitor and tape program recorder XC12 — winkelnkemper, CC BY-SA 2.0
Sharp MZ-821 — Superandi73, CC BY-SA 3.0
Compact Cassette C60, Tape, Labelled, Face (náhled) — stuart.childs, CC BY 2.0
prostřednictvím Wikimedia Commons
Licence: creativecommons.org/licenses/by-sa/2.0, creativecommons.org/licenses/by-sa/3.0, creativecommons.org/licenses/by/2.0
```

## español (`es`)

```
¿Cómo conseguían los ordenadores de 8 bits cargar los juegos más rápido?
```

```
El mismo ordenador. El mismo tipo de casete. El mismo programa. Una versión carga en la mitad de tiempo. En el hardware no cambió nada, así que ¿qué cambió?

Este vídeo trata de los cargadores turbo de los ordenadores domésticos de 8 bits: cómo un juego de ZX Spectrum podía cargar al doble de la velocidad normal, por qué el Spectrum no lo hacía por sí solo y cómo un ordenador que solo entiende el formato lento carga el programa que le enseña el rápido. Y por el camino: Speedlock y por qué no solo servía para acelerar la carga, un casete de Commodore 64 ganándole a un disquete, dueños de Atari en Checoslovaquia abriendo sus grabadoras y un programa para el Sharp MZ-800 capaz de cargar juegos que el propio ordenador rechazaba.

Los sonidos de carga de este vídeo se generaron a partir de las rutinas de carga reales (una copia del cargador de la ROM del Spectrum con las constantes que usaba Skool Daze) y se comprobaron en un emulador. La cinta turbo entera suena al final.

Fuentes: ZX Spectrum ROM disassembly (LD-BYTES) y SkoolKit's Skool Daze disassembly; Your Sinclair, May 1986 (Turboloader); CRASH #24 and #44 (David Aubrey-Jones on Speedlock); World of Spectrum y CPCWiki on Speedlock; Compute! #56 and #57, January and February 1985 (TurboTape); Michael Steil, pagetable.com, C64 KERNAL disassembly; Commodore C2N Datassette service manual; ANTIC, February 1983, on the Atari cassette recorder; oldcomp.cz y atari-800.cz on Turbo 2000; Sharp MZ-800 Technical Reference Manual; Sharp MZ-800 emulator archive (Turbo Copy).

Los subtítulos están escritos para este vídeo, no generados automáticamente. Como segunda pista de audio está disponible el inglés americano.

CAPÍTULOS
00:00 La misma cinta, la mitad de tiempo
00:37 Acorta cada pulso
01:22 Por qué el Spectrum no lo hacía solo
02:34 El cargador que carga el cargador
03:26 Speedlock
04:42 Commodore 64: un casete gana a un disquete
05:55 Atari: abre la grabadora
07:09 El precio de la velocidad
07:45 El programa que reparaba juegos
08:19 Un cronómetro ajustado de antemano
09:42 Lo que todos tienen en común
10:17 Una pregunta para ti
10:27 La cinta turbo entera

CRÉDITOS DE LAS IMÁGENES
Commodore 64 with the external power supply and Commodore 1530 (C2N) Datasette — Xavier Caballe, CC BY-SA 2.0
Atari 800 XL home computer with monitor and tape program recorder XC12 — winkelnkemper, CC BY-SA 2.0
Sharp MZ-821 — Superandi73, CC BY-SA 3.0
Compact Cassette C60, Tape, Labelled, Face (miniatura) — stuart.childs, CC BY 2.0
vía Wikimedia Commons
Licencias: creativecommons.org/licenses/by-sa/2.0, creativecommons.org/licenses/by-sa/3.0, creativecommons.org/licenses/by/2.0
```

## svenska (`sv`)

```
Hur kunde 8-bitarsdatorer ladda spel snabbare?
```

```
Samma dator. Samma sorts kassett. Samma program. En version laddar på halva tiden. Ingenting i hårdvaran ändrades, så vad var det som ändrades?

Den här videon handlar om turboladdare på 8-bitars hemdatorer: hur ett spel till ZX Spectrum kunde ladda dubbelt så snabbt som normalt, varför Spectrum inte gjorde det av sig självt och hur en dator som bara förstår det långsamma formatet laddar programmet som lär den det snabba. På vägen: Speedlock och varför det inte bara användes för att snabba upp laddningen, en Commodore 64-kassett som slår en diskett, Atariägare i Tjeckoslovakien som öppnade sina bandspelare, och ett program till Sharp MZ-800 som kunde ladda spel som datorn själv vägrade.

Laddningsljuden i den här videon är genererade från de riktiga laddningsrutinerna (en kopia av Spectrums ROM-laddare med de konstanter som Skool Daze använde) och kontrollerade i en emulator. Hela turbobandet spelas i slutet.

Källor: ZX Spectrum ROM disassembly (LD-BYTES) och SkoolKit's Skool Daze disassembly; Your Sinclair, May 1986 (Turboloader); CRASH #24 and #44 (David Aubrey-Jones on Speedlock); World of Spectrum och CPCWiki on Speedlock; Compute! #56 and #57, January and February 1985 (TurboTape); Michael Steil, pagetable.com, C64 KERNAL disassembly; Commodore C2N Datassette service manual; ANTIC, February 1983, on the Atari cassette recorder; oldcomp.cz och atari-800.cz on Turbo 2000; Sharp MZ-800 Technical Reference Manual; Sharp MZ-800 emulator archive (Turbo Copy).

Undertexterna är skrivna för den här videon, inte automatgenererade. Som andra ljudspår finns amerikansk engelska.

KAPITEL
00:00 Samma band, halva tiden
00:37 Gör varje puls kortare
01:22 Varför Spectrum inte gjorde det själv
02:34 Laddaren som laddar laddaren
03:26 Speedlock
04:42 Commodore 64: en kassett slår en diskett
05:55 Atari: öppna bandspelaren
07:09 Priset för hastigheten
07:45 Programmet som lagade spel
08:19 Ett stoppur inställt i förväg
09:42 Vad de alla har gemensamt
10:17 En fråga till dig
10:27 Hela turbobandet

BILDKÄLLOR
Commodore 64 with the external power supply and Commodore 1530 (C2N) Datasette — Xavier Caballe, CC BY-SA 2.0
Atari 800 XL home computer with monitor and tape program recorder XC12 — winkelnkemper, CC BY-SA 2.0
Sharp MZ-821 — Superandi73, CC BY-SA 3.0
Compact Cassette C60, Tape, Labelled, Face (miniatyrbild) — stuart.childs, CC BY 2.0
via Wikimedia Commons
Licenser: creativecommons.org/licenses/by-sa/2.0, creativecommons.org/licenses/by-sa/3.0, creativecommons.org/licenses/by/2.0
```
