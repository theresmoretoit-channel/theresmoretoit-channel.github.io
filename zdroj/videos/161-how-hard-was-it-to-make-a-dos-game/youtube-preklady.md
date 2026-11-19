# YouTube — 161 „How Hard Was It to Make a DOS Game?“: lokalizace

Lokalizované názvy a popisy pro třináct jazyků (bez `en`, ten je
v `youtube.md`). Pořadí podle YouTube Studia. Nahrává
`python tools/lokalizace.py videos/161-how-hard-was-it-to-make-a-dos-game`.

**Co se NEPŘEKLÁDÁ:**

- vlastní jména a technické názvy (Doom, DOS/4GW, CONFIG.SYS, AUTOEXEC.BAT, MS-DOS 6, Mode 13h,
  Mode X, Wing Commander, Michael Abrash). Ukrajinština píše Abrashe cyrilicí jako titulky (Абраш),
- časy kapitol na vteřinu, jsou shodné s `youtube.md` (scény S01, S07, S17, S21, S28, S37, S43,
  S47, S59, S69, S75, S87, S92),
- řádek zdrojů, přeložené je jen úvodní slovo „Sources:“. Autoři, názvy prací a instituce zůstávají
  anglicky, jsou to doklady,
- kredity obrázků: názvy souborů z Commons, autoři, názvy licencí, „via Wikimedia Commons“.
  Přeložený je nadpis, „screenshot“, „licence“ a věta o volném díle,
- tagy — YouTube je pro jednotlivé jazyky nemá.

Odstavec o titulcích a americké stopě je doslova z kanonické tabulky v `docs/zverejneni.md`.
Pointa se neprozrazuje víc než v angličtině: popis neříká, že obtížnost nezmizela, ale přesunula se
(S93), ani jak dopadl vtip ve Wing Commanderu (S74).
Terminologie podle titulků `script.<kód>.md` (EMS/XMS: cs expandovaná/rozšířená, de Expanded/Extended
Memory, fr paginée/étendue, pl ekspandowana/rozszerzona, tr genişletilmiş/uzatılmış, uk відображувана/
розширена, fi expanded memory/laajennettu muisti; id a vi anglicky jako titulky). Kapitola 07:01 je
znění hlášky ze S73 každého jazyka. Kapitola 06:18 zrcadlí S59 („every step the processor took“).
Registr: popis diváka neoslovuje; kapitola 07:01 je znění hlášky ze S73 (uk po Codexu neosobní
„Дякуємо за гру“).

## suomi (`fi`)

```
Kuinka vaikeaa oli tehdä peli DOSille?
```

```
Vuonna 1993 Doom pyöri tietokoneella, jossa oli 4 megatavua muistia eikä 3D-kiihdytintä. Nykyään peli aloitetaan pelimoottorista, joka huolehtii grafiikasta, äänestä, muistista ja laitteistosta. DOSissa kaikki se oli kehittäjän ongelma, ja melko usein myös pelaajan. Kuinka vaikeaa siis oli tehdä peli DOSille?

Video käy läpi 640 kilotavun rajan ja lausahduksen, jota pidetään yleensä Bill Gatesin sanomana, expanded memoryn ja laajennetun muistin, miksi pelaajat päätyivät muokkaamaan CONFIG.SYS- ja AUTOEXEC.BAT-tiedostoja ja rakentamaan käynnistysvalikoita MS-DOS 6:ssa, mitä DOS/4GW teki, kun sen nimi vilahti ruudulla, miten Mode 13h ja Michael Abrashin Mode X saivat pikselit ruudulle, miksi äänikortit olivat porttien, IRQ:iden ja DMA-kanavien arpapeliä, miten ohjelmoijat korvasivat kertolaskun bittisiirroilla, Wing Commanderin pilailevan virheilmoituksen ja mitä tapahtui, kun muut studiot halusivat Doomin moottorin.

Lähteet: id Software, Doom README (1993) and Doom source code (GPL release, 1999); Microsoft, MS-DOS 6 online help and Knowledge Base Q91202 (MultiConfig); Quote Investigator, "640K of computer memory ought to be enough for anybody" (2011); M. Abrash, Dr. Dobb's Journal (July 1991); B. Sheffield, Dirty Coding Tricks II, Game Developer (March 2010); B. Lesnick, Mythbusters: Wing Commander I Edition, Wing Commander CIC (September 2023).

Tekstitykset on kirjoitettu tätä videota varten, ei luotu automaattisesti. Toisena ääniraitana on amerikanenglanti.

Koko teksti, lähteet ja käännökset: https://theresmoretoit-channel.github.io/fi/videos/how-hard-was-it-to-make-a-dos-game/

LUVUT
00:00 Doom neljällä megatavulla
00:35 640 kilotavun raja
01:33 Expanded memory ja laajennettu muisti
02:00 Kun siitä tuli pelaajan ongelma
02:47 DOS-laajentimet ja DOS/4GW
03:45 Yksi tavu pikseliä kohden
04:38 Mode X
05:04 Äänikorttien arpapeli
06:18 Jokainen askel laskettiin
07:01 Kiitos, että pelasit Wing Commanderia
07:40 Takaisin Doomiin
08:48 Moottorin lisensointi
09:25 Oliko se ennen vaikeampaa?

KUVALÄHTEET
Michael Abrash at Facebook's F8 2015 — Maurizio Pesce, CC BY 2.0
NeXTcube — Simon Claessen, CC BY-SA 2.0
Kuvakaappaus Freedoomista (Freedoom 2018) — Freedoom developers, BSD-lisenssi
Kuvakaappaus OpenTTD:stä (Farhill Transport, 14th Mar 1939) — OpenTTD authors, OpenGFX authors, Derpy Hooves; GPL
via Wikimedia Commons. Lisenssit: creativecommons.org/licenses/by/2.0, creativecommons.org/licenses/by-sa/2.0
IBM PC 5150:n ja Roland MT-32:n valokuvat ovat public domainia.
```

## français (`fr`)

```
À quel point était-ce difficile de faire un jeu pour DOS ?
```

```
En 1993, Doom tournait sur un ordinateur doté de 4 mégaoctets de mémoire et sans accélérateur 3D. Aujourd'hui, un jeu part d'un moteur qui s'occupe des graphismes, du son, de la mémoire et du matériel. Sous DOS, tout ça était le problème du développeur, et bien souvent celui du joueur aussi. Alors, à quel point était-ce difficile de faire un jeu pour DOS ?

Cette vidéo passe en revue la limite des 640 kilooctets et la phrase qu'on attribue généralement à Bill Gates, la mémoire paginée et la mémoire étendue, pourquoi les joueurs ont fini par modifier CONFIG.SYS et AUTOEXEC.BAT et par créer des menus de démarrage sous MS-DOS 6, ce que faisait DOS/4GW quand son nom défilait à l'écran, comment le Mode 13h et le Mode X de Michael Abrash affichaient les pixels, pourquoi les cartes son étaient une loterie de ports, d'IRQ et de canaux DMA, comment les programmeurs remplaçaient la multiplication par des décalages de bits, le faux message d'erreur de Wing Commander, et ce qui s'est passé quand d'autres studios ont voulu le moteur de Doom.

Sources : id Software, Doom README (1993) and Doom source code (GPL release, 1999); Microsoft, MS-DOS 6 online help and Knowledge Base Q91202 (MultiConfig); Quote Investigator, "640K of computer memory ought to be enough for anybody" (2011); M. Abrash, Dr. Dobb's Journal (July 1991); B. Sheffield, Dirty Coding Tricks II, Game Developer (March 2010); B. Lesnick, Mythbusters: Wing Commander I Edition, Wing Commander CIC (September 2023).

Les sous-titres sont écrits pour cette vidéo, pas générés automatiquement. Une piste audio en anglais américain est disponible en seconde piste.

Transcription complète, sources et traductions : https://theresmoretoit-channel.github.io/fr/videos/how-hard-was-it-to-make-a-dos-game/

CHAPITRES
00:00 Doom sur quatre mégaoctets
00:35 La limite des 640 kilooctets
01:33 Mémoire paginée et mémoire étendue
02:00 Quand le problème est passé au joueur
02:47 Les extendeurs DOS et DOS/4GW
03:45 Un octet par pixel
04:38 Le Mode X
05:04 La loterie des cartes son
06:18 Compter chaque étape
07:01 Merci d'avoir joué à Wing Commander
07:40 Retour à Doom
08:48 Le moteur sous licence
09:25 C'était plus dur à l'époque ?

CRÉDITS DES IMAGES
Michael Abrash at Facebook's F8 2015 — Maurizio Pesce, CC BY 2.0
NeXTcube — Simon Claessen, CC BY-SA 2.0
Capture d'écran de Freedoom (Freedoom 2018) — Freedoom developers, licence BSD
Capture d'écran d'OpenTTD (Farhill Transport, 14th Mar 1939) — OpenTTD authors, OpenGFX authors, Derpy Hooves ; GPL
via Wikimedia Commons. Licences : creativecommons.org/licenses/by/2.0, creativecommons.org/licenses/by-sa/2.0
Les photos de l'IBM PC 5150 et du Roland MT-32 sont dans le domaine public.
```

## Bahasa Indonesia (`id`)

```
Seberapa Sulit Membuat Game untuk DOS?
```

```
Pada tahun 1993, Doom berjalan di komputer dengan memori 4 megabyte dan tanpa akselerator 3D. Sekarang, sebuah game dimulai dengan engine yang mengurus grafis, suara, memori, dan perangkat keras. Di DOS, semua itu adalah masalah developer, dan cukup sering masalah pemain juga. Jadi, seberapa sulit membuat game untuk DOS?

Video ini membahas batas 640 kilobyte dan kalimat yang biasanya dikaitkan dengan Bill Gates, expanded memory dan extended memory, mengapa para pemain sampai mengedit CONFIG.SYS dan AUTOEXEC.BAT serta membuat menu boot di MS-DOS 6, apa yang dilakukan DOS/4GW saat namanya muncul sekilas di layar, bagaimana Mode 13h dan Mode X karya Michael Abrash menampilkan piksel di layar, mengapa kartu suara seperti lotre port, IRQ, dan kanal DMA, bagaimana programmer mengganti perkalian dengan pergeseran bit, pesan error lelucon di Wing Commander, dan apa yang terjadi ketika studio lain menginginkan engine Doom.

Sumber: id Software, Doom README (1993) and Doom source code (GPL release, 1999); Microsoft, MS-DOS 6 online help and Knowledge Base Q91202 (MultiConfig); Quote Investigator, "640K of computer memory ought to be enough for anybody" (2011); M. Abrash, Dr. Dobb's Journal (July 1991); B. Sheffield, Dirty Coding Tricks II, Game Developer (March 2010); B. Lesnick, Mythbusters: Wing Commander I Edition, Wing Commander CIC (September 2023).

Subtitel ditulis khusus untuk video ini, bukan dibuat secara otomatis. Tersedia juga trek audio kedua dalam bahasa Inggris Amerika.

Transkrip lengkap, sumber, dan terjemahan: https://theresmoretoit-channel.github.io/id/videos/how-hard-was-it-to-make-a-dos-game/

BAB
00:00 Doom dengan empat megabyte
00:35 Batas 640 kilobyte
01:33 Expanded memory dan extended memory
02:00 Saat masalahnya pindah ke pemain
02:47 DOS extender dan DOS/4GW
03:45 Satu byte per piksel
04:38 Mode X
05:04 Lotre kartu suara
06:18 Menghitung setiap langkah
07:01 Terima kasih sudah memainkan Wing Commander
07:40 Kembali ke Doom
08:48 Melisensikan engine
09:25 Apakah dulu lebih sulit?

KREDIT GAMBAR
Michael Abrash at Facebook's F8 2015 — Maurizio Pesce, CC BY 2.0
NeXTcube — Simon Claessen, CC BY-SA 2.0
Tangkapan layar Freedoom (Freedoom 2018) — Freedoom developers, lisensi BSD
Tangkapan layar OpenTTD (Farhill Transport, 14th Mar 1939) — OpenTTD authors, OpenGFX authors, Derpy Hooves; GPL
via Wikimedia Commons. Lisensi: creativecommons.org/licenses/by/2.0, creativecommons.org/licenses/by-sa/2.0
Foto IBM PC 5150 dan Roland MT-32 berada dalam domain publik.
```

## italiano (`it`)

```
Quanto era difficile fare un gioco per DOS?
```

```
Nel 1993 Doom girava su un computer con 4 megabyte di memoria e nessun acceleratore 3D. Oggi un gioco parte da un motore che si occupa di grafica, audio, memoria e hardware. Sotto DOS tutto questo era un problema dello sviluppatore, e abbastanza spesso anche del giocatore. Quindi, quanto era difficile fare un gioco per DOS?

Il video ripercorre il limite dei 640 kilobyte e la frase di solito attribuita a Bill Gates, la memoria espansa e la memoria estesa, perché i giocatori finivano per modificare CONFIG.SYS e AUTOEXEC.BAT e per creare menu di avvio in MS-DOS 6, che cosa faceva DOS/4GW quando il suo nome passava veloce sullo schermo, come il Mode 13h e il Mode X di Michael Abrash mettevano i pixel sullo schermo, perché le schede audio erano una lotteria di porte, IRQ e canali DMA, come i programmatori sostituivano la moltiplicazione con gli shift di bit, il finto messaggio di errore di Wing Commander e che cosa è successo quando altri studi hanno voluto il motore di Doom.

Fonti: id Software, Doom README (1993) and Doom source code (GPL release, 1999); Microsoft, MS-DOS 6 online help and Knowledge Base Q91202 (MultiConfig); Quote Investigator, "640K of computer memory ought to be enough for anybody" (2011); M. Abrash, Dr. Dobb's Journal (July 1991); B. Sheffield, Dirty Coding Tricks II, Game Developer (March 2010); B. Lesnick, Mythbusters: Wing Commander I Edition, Wing Commander CIC (September 2023).

I sottotitoli sono scritti per questo video, non generati automaticamente. Come seconda traccia audio è disponibile l’inglese americano.

Trascrizione completa, fonti e traduzioni: https://theresmoretoit-channel.github.io/it/videos/how-hard-was-it-to-make-a-dos-game/

CAPITOLI
00:00 Doom con quattro megabyte
00:35 Il limite dei 640 kilobyte
01:33 Memoria espansa e memoria estesa
02:00 Quando il problema è passato al giocatore
02:47 I DOS extender e DOS/4GW
03:45 Un byte per pixel
04:38 Il Mode X
05:04 La lotteria delle schede audio
06:18 Contare ogni passo
07:01 Grazie per aver giocato a Wing Commander
07:40 Ritorno a Doom
08:48 Il motore in licenza
09:25 Era più difficile allora?

CREDITI DELLE IMMAGINI
Michael Abrash at Facebook's F8 2015 — Maurizio Pesce, CC BY 2.0
NeXTcube — Simon Claessen, CC BY-SA 2.0
Screenshot di Freedoom (Freedoom 2018) — Freedoom developers, licenza BSD
Screenshot di OpenTTD (Farhill Transport, 14th Mar 1939) — OpenTTD authors, OpenGFX authors, Derpy Hooves; GPL
via Wikimedia Commons. Licenze: creativecommons.org/licenses/by/2.0, creativecommons.org/licenses/by-sa/2.0
Le foto dell'IBM PC 5150 e del Roland MT-32 sono di pubblico dominio.
```

## Deutsch (`de`)

```
Wie schwer war es, ein Spiel für DOS zu machen?
```

```
1993 lief Doom auf einem Computer mit 4 Megabyte Arbeitsspeicher und ohne 3D-Beschleuniger. Heute beginnt ein Spiel mit einer Engine, die sich um Grafik, Sound, Speicher und Hardware kümmert. Unter DOS war all das das Problem des Entwicklers, und ziemlich oft auch das des Spielers. Wie schwer war es also, ein Spiel für DOS zu machen?

Das Video geht durch die 640-Kilobyte-Grenze und den Satz, der meist Bill Gates zugeschrieben wird, Expanded und Extended Memory, warum Spieler am Ende CONFIG.SYS und AUTOEXEC.BAT bearbeiteten und unter MS-DOS 6 Startmenüs bauten, was DOS/4GW tat, wenn sein Name kurz auf dem Bildschirm aufblitzte, wie Mode 13h und Michael Abrashs Mode X Pixel auf den Bildschirm brachten, warum Soundkarten eine Lotterie aus Ports, IRQs und DMA-Kanälen waren, wie Programmierer Multiplikationen durch Bitverschiebungen ersetzten, die Scherz-Fehlermeldung in Wing Commander und was passierte, als andere Studios die Engine von Doom haben wollten.

Quellen: id Software, Doom README (1993) and Doom source code (GPL release, 1999); Microsoft, MS-DOS 6 online help and Knowledge Base Q91202 (MultiConfig); Quote Investigator, "640K of computer memory ought to be enough for anybody" (2011); M. Abrash, Dr. Dobb's Journal (July 1991); B. Sheffield, Dirty Coding Tricks II, Game Developer (March 2010); B. Lesnick, Mythbusters: Wing Commander I Edition, Wing Commander CIC (September 2023).

Die Untertitel wurden für dieses Video geschrieben, nicht automatisch erzeugt. Als zweite Tonspur steht amerikanisches Englisch bereit.

Vollständiger Text, Quellen und Übersetzungen: https://theresmoretoit-channel.github.io/de/videos/how-hard-was-it-to-make-a-dos-game/

KAPITEL
00:00 Doom mit vier Megabyte
00:35 Die 640-Kilobyte-Grenze
01:33 Expanded und Extended Memory
02:00 Als es zum Problem der Spieler wurde
02:47 DOS-Extender und DOS/4GW
03:45 Ein Byte pro Pixel
04:38 Mode X
05:04 Die Soundkarten-Lotterie
06:18 Jeder Schritt zählte
07:01 Danke, dass du Wing Commander gespielt hast
07:40 Zurück zu Doom
08:48 Die lizenzierte Engine
09:25 War es damals schwerer?

BILDNACHWEISE
Michael Abrash at Facebook's F8 2015 — Maurizio Pesce, CC BY 2.0
NeXTcube — Simon Claessen, CC BY-SA 2.0
Screenshot von Freedoom (Freedoom 2018) — Freedoom developers, BSD-Lizenz
Screenshot von OpenTTD (Farhill Transport, 14th Mar 1939) — OpenTTD authors, OpenGFX authors, Derpy Hooves; GPL
via Wikimedia Commons. Lizenzen: creativecommons.org/licenses/by/2.0, creativecommons.org/licenses/by-sa/2.0
Die Fotos des IBM PC 5150 und des Roland MT-32 sind gemeinfrei.
```

## polski (`pl`)

```
Jak trudno było zrobić grę na DOS-a?
```

```
W 1993 roku Doom działał na komputerze z 4 megabajtami pamięci i bez akceleratora 3D. Dziś gra zaczyna się od silnika, który dba o grafikę, dźwięk, pamięć i sprzęt. W DOS-ie to wszystko było problemem programisty, a dość często także gracza. Jak trudno było więc zrobić grę na DOS-a?

Film omawia limit 640 kilobajtów i zdanie zwykle przypisywane Billowi Gatesowi, pamięć ekspandowaną i rozszerzoną, dlaczego gracze w końcu edytowali CONFIG.SYS i AUTOEXEC.BAT i budowali menu startowe w MS-DOS 6, co robił DOS/4GW, gdy jego nazwa migała na ekranie, jak Mode 13h i Mode X Michaela Abrasha wyświetlały piksele, dlaczego karty dźwiękowe były loterią portów, IRQ i kanałów DMA, jak programiści zastępowali mnożenie przesunięciami bitowymi, żartobliwy komunikat o błędzie w Wing Commanderze i co się stało, gdy inne studia zapragnęły silnika Dooma.

Źródła: id Software, Doom README (1993) and Doom source code (GPL release, 1999); Microsoft, MS-DOS 6 online help and Knowledge Base Q91202 (MultiConfig); Quote Investigator, "640K of computer memory ought to be enough for anybody" (2011); M. Abrash, Dr. Dobb's Journal (July 1991); B. Sheffield, Dirty Coding Tricks II, Game Developer (March 2010); B. Lesnick, Mythbusters: Wing Commander I Edition, Wing Commander CIC (September 2023).

Napisy są pisane do tego filmu, nie generowane automatycznie. Jako druga ścieżka dźwiękowa dostępny jest angielski amerykański.

Pełna transkrypcja, źródła i tłumaczenia: https://theresmoretoit-channel.github.io/pl/videos/how-hard-was-it-to-make-a-dos-game/

ROZDZIAŁY
00:00 Doom na czterech megabajtach
00:35 Limit 640 kilobajtów
01:33 Pamięć ekspandowana i rozszerzona
02:00 Kiedy to stało się problemem gracza
02:47 DOS extendery i DOS/4GW
03:45 Jeden bajt na piksel
04:38 Mode X
05:04 Loteria kart dźwiękowych
06:18 Liczenie każdego kroku
07:01 Dziękujemy za grę w Wing Commander
07:40 Powrót do Dooma
08:48 Licencjonowany silnik
09:25 Czy kiedyś było trudniej?

ŹRÓDŁA ZDJĘĆ
Michael Abrash at Facebook's F8 2015 — Maurizio Pesce, CC BY 2.0
NeXTcube — Simon Claessen, CC BY-SA 2.0
Zrzut ekranu z Freedoom (Freedoom 2018) — Freedoom developers, licencja BSD
Zrzut ekranu z OpenTTD (Farhill Transport, 14th Mar 1939) — OpenTTD authors, OpenGFX authors, Derpy Hooves; GPL
via Wikimedia Commons. Licencje: creativecommons.org/licenses/by/2.0, creativecommons.org/licenses/by-sa/2.0
Zdjęcia IBM PC 5150 i Roland MT-32 są w domenie publicznej.
```

## português (Brasil) (`pt-BR`)

```
Quão difícil era fazer um jogo para DOS?
```

```
Em 1993, o Doom rodava num computador com 4 megabytes de memória e sem acelerador 3D. Hoje, um jogo começa com uma engine que cuida de gráficos, som, memória e hardware. No DOS, tudo isso era problema do desenvolvedor e, muitas vezes, do jogador também. Então, quão difícil era fazer um jogo para DOS?

Este vídeo passa pelo limite de 640 kilobytes e pela frase que costuma ser atribuída a Bill Gates, pela memória expandida e pela memória estendida, por que os jogadores acabaram editando o CONFIG.SYS e o AUTOEXEC.BAT e montando menus de inicialização no MS-DOS 6, o que o DOS/4GW fazia quando seu nome passava rapidinho na tela, como o Mode 13h e o Mode X de Michael Abrash colocavam pixels na tela, por que as placas de som eram uma loteria de portas, IRQs e canais de DMA, como os programadores trocavam a multiplicação por deslocamentos de bits, a mensagem de erro de brincadeira do Wing Commander e o que aconteceu quando outros estúdios quiseram a engine do Doom.

Fontes: id Software, Doom README (1993) and Doom source code (GPL release, 1999); Microsoft, MS-DOS 6 online help and Knowledge Base Q91202 (MultiConfig); Quote Investigator, "640K of computer memory ought to be enough for anybody" (2011); M. Abrash, Dr. Dobb's Journal (July 1991); B. Sheffield, Dirty Coding Tricks II, Game Developer (March 2010); B. Lesnick, Mythbusters: Wing Commander I Edition, Wing Commander CIC (September 2023).

As legendas foram escritas para este vídeo, não geradas automaticamente. Como segunda faixa de áudio está disponível o inglês americano.

Transcrição completa, fontes e traduções: https://theresmoretoit-channel.github.io/pt-br/videos/how-hard-was-it-to-make-a-dos-game/

CAPÍTULOS
00:00 Doom com quatro megabytes
00:35 O limite de 640 kilobytes
01:33 Memória expandida e estendida
02:00 Quando o problema virou do jogador
02:47 Extensores de DOS e o DOS/4GW
03:45 Um byte por pixel
04:38 Mode X
05:04 A loteria das placas de som
06:18 Contando cada passo
07:01 Obrigado por jogar Wing Commander
07:40 De volta ao Doom
08:48 Licenciando a engine
09:25 Era mais difícil naquela época?

CRÉDITOS DAS IMAGENS
Michael Abrash at Facebook's F8 2015 — Maurizio Pesce, CC BY 2.0
NeXTcube — Simon Claessen, CC BY-SA 2.0
Captura de tela do Freedoom (Freedoom 2018) — Freedoom developers, licença BSD
Captura de tela do OpenTTD (Farhill Transport, 14th Mar 1939) — OpenTTD authors, OpenGFX authors, Derpy Hooves; GPL
via Wikimedia Commons. Licenças: creativecommons.org/licenses/by/2.0, creativecommons.org/licenses/by-sa/2.0
As fotos do IBM PC 5150 e do Roland MT-32 estão em domínio público.
```

## Türkçe (`tr`)

```
DOS İçin Oyun Yapmak Ne Kadar Zordu?
```

```
1993'te Doom, 4 megabayt belleği olan ve 3D hızlandırıcısı bulunmayan bir bilgisayarda çalışıyordu. Bugün bir oyun; grafiği, sesi, belleği ve donanımı halleden bir motorla başlar. DOS'ta bunların hepsi geliştiricinin derdiydi, oldukça sık da oyuncunun. Peki DOS için oyun yapmak ne kadar zordu?

Bu video 640 kilobayt sınırını ve genellikle Bill Gates'e mal edilen sözü, genişletilmiş ve uzatılmış belleği, oyuncuların neden CONFIG.SYS ve AUTOEXEC.BAT dosyalarını düzenleyip MS-DOS 6'da açılış menüleri kurmak zorunda kaldığını, DOS/4GW'nin adı ekranda bir anlığına geçerken ne yaptığını, Mode 13h'in ve Michael Abrash'ın Mode X'inin pikselleri ekrana nasıl getirdiğini, ses kartlarının neden bir port, IRQ ve DMA kanalı piyangosu olduğunu, programcıların çarpmayı nasıl bit kaydırmayla değiştirdiğini, Wing Commander'daki şaka hata mesajını ve başka stüdyolar Doom'un motorunu istediğinde ne olduğunu anlatıyor.

Kaynaklar: id Software, Doom README (1993) and Doom source code (GPL release, 1999); Microsoft, MS-DOS 6 online help and Knowledge Base Q91202 (MultiConfig); Quote Investigator, "640K of computer memory ought to be enough for anybody" (2011); M. Abrash, Dr. Dobb's Journal (July 1991); B. Sheffield, Dirty Coding Tricks II, Game Developer (March 2010); B. Lesnick, Mythbusters: Wing Commander I Edition, Wing Commander CIC (September 2023).

Altyazılar bu video için yazıldı, otomatik olarak oluşturulmadı. İkinci ses parçası olarak Amerikan İngilizcesi de mevcut.

Metnin tamamı, kaynaklar ve çeviriler: https://theresmoretoit-channel.github.io/tr/videos/how-hard-was-it-to-make-a-dos-game/

BÖLÜMLER
00:00 Dört megabaytta Doom
00:35 640 kilobayt sınırı
01:33 Genişletilmiş ve uzatılmış bellek
02:00 Sorun oyuncunun sorunu olunca
02:47 DOS extender'lar ve DOS/4GW
03:45 Piksel başına bir bayt
04:38 Mode X
05:04 Ses kartı piyangosu
06:18 Her adımı saymak
07:01 Wing Commander oynadığın için teşekkürler
07:40 Doom'a dönüş
08:48 Motoru lisanslamak
09:25 O zamanlar daha mı zordu?

GÖRSEL KAYNAKLARI
Michael Abrash at Facebook's F8 2015 — Maurizio Pesce, CC BY 2.0
NeXTcube — Simon Claessen, CC BY-SA 2.0
Freedoom ekran görüntüsü (Freedoom 2018) — Freedoom developers, BSD lisansı
OpenTTD ekran görüntüsü (Farhill Transport, 14th Mar 1939) — OpenTTD authors, OpenGFX authors, Derpy Hooves; GPL
via Wikimedia Commons. Lisanslar: creativecommons.org/licenses/by/2.0, creativecommons.org/licenses/by-sa/2.0
IBM PC 5150 ve Roland MT-32 fotoğrafları kamu malıdır.
```

## українська (`uk`)

```
Наскільки складно було зробити гру для DOS?
```

```
У 1993 році Doom працював на комп'ютері з 4 мегабайтами пам'яті й без 3D-прискорювача. Сьогодні гра починається з рушія, який дбає про графіку, звук, пам'ять і залізо. У DOS усе це було проблемою розробника, а доволі часто — і гравця. То наскільки складно було зробити гру для DOS?

У відео йдеться про межу в 640 кілобайт і фразу, яку зазвичай приписують Біллу Гейтсу, про відображувану й розширену пам'ять, про те, чому гравці зрештою редагували CONFIG.SYS і AUTOEXEC.BAT та налаштовували меню завантаження в MS-DOS 6, що робив DOS/4GW, коли його назва промайнула на екрані, як Mode 13h і Mode X Майкла Абраша виводили пікселі на екран, чому звукові карти були лотереєю портів, IRQ і каналів DMA, як програмісти замінювали множення бітовими зсувами, про жартівливе повідомлення про помилку у Wing Commander і про те, що сталося, коли інші студії захотіли рушій Doom.

Джерела: id Software, Doom README (1993) and Doom source code (GPL release, 1999); Microsoft, MS-DOS 6 online help and Knowledge Base Q91202 (MultiConfig); Quote Investigator, "640K of computer memory ought to be enough for anybody" (2011); M. Abrash, Dr. Dobb's Journal (July 1991); B. Sheffield, Dirty Coding Tricks II, Game Developer (March 2010); B. Lesnick, Mythbusters: Wing Commander I Edition, Wing Commander CIC (September 2023).

Субтитри написані для цього відео, а не згенеровані автоматично. Також доступна друга звукова доріжка — американською англійською.

Повний текст, джерела та переклади: https://theresmoretoit-channel.github.io/uk/videos/how-hard-was-it-to-make-a-dos-game/

РОЗДІЛИ
00:00 Doom на чотирьох мегабайтах
00:35 Межа в 640 кілобайт
01:33 Відображувана й розширена пам'ять
02:00 Коли це стало проблемою гравця
02:47 DOS-розширювачі та DOS/4GW
03:45 Один байт на піксель
04:38 Mode X
05:04 Лотерея звукових карт
06:18 Кожен крок на рахунку
07:01 Дякуємо за гру у Wing Commander
07:40 Знову Doom
08:48 Ліцензований рушій
09:25 Чи було тоді складніше?

ДЖЕРЕЛА ЗОБРАЖЕНЬ
Michael Abrash at Facebook's F8 2015 — Maurizio Pesce, CC BY 2.0
NeXTcube — Simon Claessen, CC BY-SA 2.0
Знімок екрана Freedoom (Freedoom 2018) — Freedoom developers, ліцензія BSD
Знімок екрана OpenTTD (Farhill Transport, 14th Mar 1939) — OpenTTD authors, OpenGFX authors, Derpy Hooves; GPL
via Wikimedia Commons. Ліцензії: creativecommons.org/licenses/by/2.0, creativecommons.org/licenses/by-sa/2.0
Фотографії IBM PC 5150 і Roland MT-32 перебувають у суспільному надбанні.
```

## Tiếng Việt (`vi`)

```
Làm một trò chơi cho DOS khó đến mức nào?
```

```
Năm 1993, Doom chạy trên một chiếc máy tính có 4 megabyte bộ nhớ và không có card tăng tốc 3D. Ngày nay, một trò chơi bắt đầu từ một engine lo phần đồ họa, âm thanh, bộ nhớ và phần cứng. Trên DOS, tất cả những thứ đó là việc của lập trình viên, và khá thường xuyên, của cả người chơi. Vậy làm một trò chơi cho DOS khó đến mức nào?

Video này đi qua giới hạn 640 kilobyte và câu nói thường được gán cho Bill Gates, bộ nhớ expanded và extended, vì sao người chơi phải tự sửa CONFIG.SYS và AUTOEXEC.BAT và dựng menu khởi động trong MS-DOS 6, DOS/4GW làm gì khi tên nó lướt qua trên màn hình, Mode 13h và Mode X của Michael Abrash đưa điểm ảnh lên màn hình như thế nào, vì sao card âm thanh là một trò xổ số với cổng, IRQ và kênh DMA, các lập trình viên thay phép nhân bằng phép dịch bit ra sao, thông báo lỗi đùa trong Wing Commander, và chuyện gì xảy ra khi các studio khác muốn có engine của Doom.

Nguồn: id Software, Doom README (1993) and Doom source code (GPL release, 1999); Microsoft, MS-DOS 6 online help and Knowledge Base Q91202 (MultiConfig); Quote Investigator, "640K of computer memory ought to be enough for anybody" (2011); M. Abrash, Dr. Dobb's Journal (July 1991); B. Sheffield, Dirty Coding Tricks II, Game Developer (March 2010); B. Lesnick, Mythbusters: Wing Commander I Edition, Wing Commander CIC (September 2023).

Phụ đề được viết riêng cho video này, không phải tạo tự động. Có thể chọn tiếng Anh Mỹ ở bản âm thanh thứ hai.

Toàn văn, nguồn và bản dịch: https://theresmoretoit-channel.github.io/vi/videos/how-hard-was-it-to-make-a-dos-game/

CHƯƠNG
00:00 Doom trên bốn megabyte
00:35 Giới hạn 640 kilobyte
01:33 Bộ nhớ expanded và extended
02:00 Khi vấn đề chuyển sang người chơi
02:47 DOS extender và DOS/4GW
03:45 Một byte cho mỗi điểm ảnh
04:38 Mode X
05:04 Trò xổ số card âm thanh
06:18 Đếm từng bước
07:01 Cảm ơn bạn đã chơi Wing Commander
07:40 Trở lại với Doom
08:48 Cấp phép engine
09:25 Hồi đó có khó hơn không?

NGUỒN HÌNH ẢNH
Michael Abrash at Facebook's F8 2015 — Maurizio Pesce, CC BY 2.0
NeXTcube — Simon Claessen, CC BY-SA 2.0
Ảnh chụp màn hình Freedoom (Freedoom 2018) — Freedoom developers, giấy phép BSD
Ảnh chụp màn hình OpenTTD (Farhill Transport, 14th Mar 1939) — OpenTTD authors, OpenGFX authors, Derpy Hooves; GPL
via Wikimedia Commons. Giấy phép: creativecommons.org/licenses/by/2.0, creativecommons.org/licenses/by-sa/2.0
Ảnh IBM PC 5150 và Roland MT-32 thuộc phạm vi công cộng.
```

## čeština (`cs`)

```
Jak těžké bylo udělat hru pro DOS?
```

```
V roce 1993 běžel Doom na počítači se 4 megabajty paměti a bez 3D akcelerátoru. Dnes hra začíná enginem, který se postará o grafiku, zvuk, paměť a hardware. V DOSu bylo tohle všechno starostí vývojáře, a dost často i hráče. Jak těžké tedy bylo udělat hru pro DOS?

Video projde limit 640 kilobajtů a větu, která se obvykle připisuje Billu Gatesovi, expandovanou a rozšířenou paměť, proč hráči nakonec upravovali CONFIG.SYS a AUTOEXEC.BAT a stavěli si spouštěcí nabídky v MS-DOSu 6, co dělal DOS/4GW, když se jeho jméno mihlo na obrazovce, jak Mode 13h a Mode X Michaela Abrashe dostávaly pixely na obrazovku, proč byly zvukové karty loterií portů, IRQ a kanálů DMA, jak programátoři nahrazovali násobení bitovými posuny, žertovnou chybovou hlášku ve Wing Commanderu a co se stalo, když ostatní studia chtěla engine Doomu.

Zdroje: id Software, Doom README (1993) and Doom source code (GPL release, 1999); Microsoft, MS-DOS 6 online help and Knowledge Base Q91202 (MultiConfig); Quote Investigator, "640K of computer memory ought to be enough for anybody" (2011); M. Abrash, Dr. Dobb's Journal (July 1991); B. Sheffield, Dirty Coding Tricks II, Game Developer (March 2010); B. Lesnick, Mythbusters: Wing Commander I Edition, Wing Commander CIC (September 2023).

Titulky jsou psané pro tohle video, ne strojový přepis. Jako druhá zvuková stopa je k dispozici americká angličtina.

Celý text, zdroje a překlady: https://theresmoretoit-channel.github.io/cs/videos/how-hard-was-it-to-make-a-dos-game/

KAPITOLY
00:00 Doom na čtyřech megabajtech
00:35 Limit 640 kilobajtů
01:33 Expandovaná a rozšířená paměť
02:00 Když se z toho stal problém hráče
02:47 DOS extendery a DOS/4GW
03:45 Jeden bajt na pixel
04:38 Mode X
05:04 Loterie zvukových karet
06:18 Počítal se každý krok
07:01 Díky, že jsi hrál Wing Commander
07:40 Zpátky k Doomu
08:48 Licencovaný engine
09:25 Bylo to tehdy těžší?

ZDROJE OBRÁZKŮ
Michael Abrash at Facebook's F8 2015 — Maurizio Pesce, CC BY 2.0
NeXTcube — Simon Claessen, CC BY-SA 2.0
Snímek obrazovky Freedoomu (Freedoom 2018) — Freedoom developers, licence BSD
Snímek obrazovky OpenTTD (Farhill Transport, 14th Mar 1939) — OpenTTD authors, OpenGFX authors, Derpy Hooves; GPL
via Wikimedia Commons. Licence: creativecommons.org/licenses/by/2.0, creativecommons.org/licenses/by-sa/2.0
Fotografie IBM PC 5150 a Roland MT-32 jsou volné dílo.
```

## español (`es`)

```
¿Qué tan difícil era hacer un juego para DOS?
```

```
En 1993, Doom funcionaba en un ordenador con 4 megabytes de memoria y sin acelerador 3D. Hoy, un juego empieza con un motor que se encarga de los gráficos, el sonido, la memoria y el hardware. En DOS, todo eso era problema del desarrollador, y muchas veces también del jugador. Entonces, ¿qué tan difícil era hacer un juego para DOS?

Este vídeo recorre el límite de 640 kilobytes y la frase que se suele atribuir a Bill Gates, la memoria expandida y la memoria extendida, por qué los jugadores acabaron editando CONFIG.SYS y AUTOEXEC.BAT y creando menús de arranque en MS-DOS 6, qué hacía DOS/4GW cuando su nombre pasaba fugazmente por la pantalla, cómo el Mode 13h y el Mode X de Michael Abrash ponían los píxeles en pantalla, por qué las tarjetas de sonido eran una lotería de puertos, IRQ y canales DMA, cómo los programadores sustituían la multiplicación por desplazamientos de bits, el mensaje de error en broma de Wing Commander y qué pasó cuando otros estudios quisieron el motor de Doom.

Fuentes: id Software, Doom README (1993) and Doom source code (GPL release, 1999); Microsoft, MS-DOS 6 online help and Knowledge Base Q91202 (MultiConfig); Quote Investigator, "640K of computer memory ought to be enough for anybody" (2011); M. Abrash, Dr. Dobb's Journal (July 1991); B. Sheffield, Dirty Coding Tricks II, Game Developer (March 2010); B. Lesnick, Mythbusters: Wing Commander I Edition, Wing Commander CIC (September 2023).

Los subtítulos están escritos para este vídeo, no generados automáticamente. Como segunda pista de audio está disponible el inglés americano.

Transcripción completa, fuentes y traducciones: https://theresmoretoit-channel.github.io/es/videos/how-hard-was-it-to-make-a-dos-game/

CAPÍTULOS
00:00 Doom con cuatro megabytes
00:35 El límite de 640 kilobytes
01:33 Memoria expandida y extendida
02:00 Cuando el problema pasó al jugador
02:47 Los extensores de DOS y DOS/4GW
03:45 Un byte por píxel
04:38 Mode X
05:04 La lotería de las tarjetas de sonido
06:18 Contar cada paso
07:01 Gracias por jugar a Wing Commander
07:40 De vuelta a Doom
08:48 El motor con licencia
09:25 ¿Era más difícil entonces?

CRÉDITOS DE LAS IMÁGENES
Michael Abrash at Facebook's F8 2015 — Maurizio Pesce, CC BY 2.0
NeXTcube — Simon Claessen, CC BY-SA 2.0
Captura de pantalla de Freedoom (Freedoom 2018) — Freedoom developers, licencia BSD
Captura de pantalla de OpenTTD (Farhill Transport, 14th Mar 1939) — OpenTTD authors, OpenGFX authors, Derpy Hooves; GPL
via Wikimedia Commons. Licencias: creativecommons.org/licenses/by/2.0, creativecommons.org/licenses/by-sa/2.0
Las fotos del IBM PC 5150 y del Roland MT-32 son de dominio público.
```

## svenska (`sv`)

```
Hur svårt var det att göra ett spel för DOS?
```

```
1993 kördes Doom på en dator med 4 megabyte minne och utan 3D-accelerator. I dag börjar ett spel med en spelmotor som tar hand om grafik, ljud, minne och hårdvara. Under DOS var allt det där utvecklarens problem, och ganska ofta spelarens också. Så hur svårt var det att göra ett spel för DOS?

Videon går igenom gränsen på 640 kilobyte och citatet som brukar tillskrivas Bill Gates, expanderat och utökat minne, varför spelare till slut redigerade CONFIG.SYS och AUTOEXEC.BAT och byggde startmenyer i MS-DOS 6, vad DOS/4GW gjorde när dess namn blinkade förbi på skärmen, hur Mode 13h och Michael Abrashs Mode X fick ut pixlar på skärmen, varför ljudkort var ett lotteri av portar, IRQ:er och DMA-kanaler, hur programmerare ersatte multiplikation med bitskift, skämtfelmeddelandet i Wing Commander och vad som hände när andra studior ville ha Dooms motor.

Källor: id Software, Doom README (1993) and Doom source code (GPL release, 1999); Microsoft, MS-DOS 6 online help and Knowledge Base Q91202 (MultiConfig); Quote Investigator, "640K of computer memory ought to be enough for anybody" (2011); M. Abrash, Dr. Dobb's Journal (July 1991); B. Sheffield, Dirty Coding Tricks II, Game Developer (March 2010); B. Lesnick, Mythbusters: Wing Commander I Edition, Wing Commander CIC (September 2023).

Undertexterna är skrivna för den här videon, inte automatgenererade. Som andra ljudspår finns amerikansk engelska.

Hela texten, källor och översättningar: https://theresmoretoit-channel.github.io/sv/videos/how-hard-was-it-to-make-a-dos-game/

KAPITEL
00:00 Doom på fyra megabyte
00:35 Gränsen på 640 kilobyte
01:33 Expanderat och utökat minne
02:00 När det blev spelarens problem
02:47 DOS-extenders och DOS/4GW
03:45 En byte per pixel
04:38 Mode X
05:04 Ljudkortslotteriet
06:18 Varje steg räknades
07:01 Tack för att du spelade Wing Commander
07:40 Tillbaka till Doom
08:48 Den licensierade motorn
09:25 Var det svårare förr?

BILDKÄLLOR
Michael Abrash at Facebook's F8 2015 — Maurizio Pesce, CC BY 2.0
NeXTcube — Simon Claessen, CC BY-SA 2.0
Skärmbild från Freedoom (Freedoom 2018) — Freedoom developers, BSD-licens
Skärmbild från OpenTTD (Farhill Transport, 14th Mar 1939) — OpenTTD authors, OpenGFX authors, Derpy Hooves; GPL
via Wikimedia Commons. Licenser: creativecommons.org/licenses/by/2.0, creativecommons.org/licenses/by-sa/2.0
Fotona av IBM PC 5150 och Roland MT-32 är allmän egendom.
```
