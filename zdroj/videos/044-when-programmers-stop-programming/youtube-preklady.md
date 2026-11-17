# Lokalizované názvy a popisy — 044

Čte `tools/lokalizace.py` a nahrává přes `videos.update(part="localizations")`.
Anglický titul a popis jsou v `youtube.md` a posílají se zpátky beze změny.

**Pořadí jazyků je bajtově podle UTF-8**, tedy tak, jak je YouTube Studio
vypisuje shora dolů — podklad se pak kopíruje po řadě.

## Co se NEPŘEKLÁDÁ

- **Vlastní jména a názvy** — FORTRAN, COBOL, James Martin, IBM, NASA,
  a **anglické názvy profesí** `computer programmer` / `software developer`.
  Ta scéna je o tom, jak je pojmenoval americký statistický průzkum;
  přeložit je by zrušilo tvrzení.

  > **Čeština je vědomá výjimka** (rozhodl uživatel 2026-09-15):
  > „šest softwarových vývojářů na jednoho počítačového programátora"
  > mu zní líp než anglické termíny uprostřed české věty. Je to jediný
  > jazyk, u kterého přirozenost posoudí, takže jeho úsudek má přednost
  > před mechanickou shodou. Ostatní jazyky anglické tvary drží.
- **Název knihy z roku 1982** se uvádí v překladu, protože ve videu zazní
  přeložený — ale anglický originál *Application Development Without
  Programmers* zůstává v popisu v závorce.
- **Časy kapitol na vteřinu.**
- **Tagy** — YouTube je per-jazyk nemá.

Názvy jazyků v řádku o titulcích se naopak **překládají**: smíšený seznam
endonym uprostřed odstavce se čte jako nedodělaný překlad.

## Kontrola čísel

Ve všech jazycích musí sedět: **300 000** a **700 000** (éra před rokem
2003), **380 000** a **2 250 000** (rok 2025), poměr **6 : 1**, roky
**1954**, **1959**, **1980**, **1982**, **2003** a **dva a půl roku**
mezi zprávou a dodáním FORTRANu.

Pozor na anglické *billion*: ve videu není, ale kdyby přibylo, je to
10⁹, tedy německy `Milliarde`, polsky `miliard`.

## suomi (`fi`)

```
Mitä tapahtuu, kun ohjelmoijat lakkaavat ohjelmoimasta?
```

```
Kuvittele, että olet ohjelmoija. Eräänä päivänä avaat editorin, eikä siellä ole enää mitään kirjoitettavaa, koska kone osaa sen. Onneksi olkoon: sinusta tuli esihenkilö — mutta ilman esihenkilön palkkaa.

Kiinnostavinta ei kuitenkaan ole se, onko sinulla yhä työpaikka. Opetimme vuosikymmenten ajan ohjelmoijia kirjoittamaan koodia, jota toiset ohjelmoijat osaisivat lukea — ja nyt rakennamme koneita, jotka kirjoittavat koodia, jota ohjelmoija ei ehkä koskaan lue. Mitä varten se luettavuus siis oli?

Video seuraa lupausta, että ohjelmointi katoaa: vuoden 1954 IBM:n raportista, jonka mukaan FORTRAN ”poistaisi käytännössä koodauksen ja virheenkorjauksen”, COBOLin ja vuonna 1982 ilmestyneen kirjan Application Development Without Programmers kautta siihen, mitä ammatille todella tapahtui — ja se on oudompaa kuin miltä näyttää. Vuonna 2003 amerikkalainen työvoimatutkimus lisäsi vanhan ammattinimikkeen rinnalle toisen, ja nykyään yhtä computer programmeria kohden on noin kuusi software developeria. Työ ei kadonnut. Se nimettiin uudelleen.

Luvut:
0:00 Ei enää kirjoitettavaa
1:10 Mitä varten luettavuus oli?
1:19 Ohjelmointia on aina automatisoitu
1:41 1954: ”poistaa koodaus ja virheenkorjaus”
2:58 Kuinka monta siis jäi?
3:17 Sana joka muuttui
3:58 Miksi tällä kertaa on toisin
4:48 Se lakkaa olemasta filosofiaa
5:11 Painopiste siirtyy
6:00 Huomaamattomampi hinta
6:44 Koodityyli
7:23 Scifin avaruusalukset
8:06 Mitä ohjelmoijalle jää
8:35 Koneille kirjoitettu kieli
9:42 Väärä lause
10:02 Se oli meitä varten

Tekstitykset on kirjoitettu tätä videota varten, ei luotu automaattisesti. Toisena ääniraitana on amerikanenglanti.

Tämän videon väitteiden lähteet, muun muassa vuoden 1954 FORTRAN Preliminary Report ja Yhdysvaltain Bureau of Labor Statisticsin luvut, mainitaan videolla sitä mukaa kun ne tulevat esiin.

KUVALÄHTEET
IBM 704:n arkistokuva on NASAn ottama ja se on public domain.

There’s More To It — kysymyksiä, joiden vastaukset ovat pidempiä kuin luulisi.
```

## français (`fr`)

```
Que se passe-t-il quand les programmeurs arrêtent de programmer ?
```

```
Imagine que tu es programmeur. Un jour tu ouvres ton éditeur et tu comprends qu'il n'y reste plus rien à écrire pour toi, parce que la machine sait le faire. Félicitations : tu es devenu chef, mais sans le salaire d'un chef.

L'intéressant n'est pourtant pas de savoir si tu as encore un travail. Pendant des décennies on a appris aux programmeurs à écrire du code que d'autres programmeurs pourraient lire — et maintenant on construit des machines qui écrivent du code qu'aucun programmeur ne lira peut-être jamais. À quoi servait donc cette lisibilité ?

La vidéo suit la promesse que la programmation allait disparaître : d'un rapport d'IBM de 1954 selon lequel FORTRAN « devrait pratiquement éliminer le codage et le débogage », en passant par COBOL et un livre de 1982 intitulé Application Development Without Programmers, jusqu'à ce qui est réellement arrivé au métier — et c'est plus étrange qu'il n'y paraît. En 2003, l'enquête américaine sur l'emploi a ajouté un nouvel intitulé à côté de l'ancien, et il y a aujourd'hui environ six software developers pour un computer programmer. Le métier n'a pas disparu. Il a changé de nom.

Chapitres :
0:00 Plus rien à écrire
1:10 À quoi servait la lisibilité ?
1:19 Ça a toujours été automatisé
1:41 1954 : « éliminer le codage et le débogage »
2:58 Combien en restait-il alors ?
3:17 Le mot qui a changé
3:58 Pourquoi cette fois c'est différent
4:48 Ça cesse d'être de la philosophie
5:11 Le centre de gravité se déplace
6:00 Le coût plus discret
6:44 Le style de code
7:23 Les vaisseaux de la science-fiction
8:06 Ce qu'il reste au programmeur
8:35 Un langage écrit pour les machines
9:42 La mauvaise phrase
10:02 C'était pour nous

Les sous-titres sont écrits pour cette vidéo, pas générés automatiquement. Une piste audio en anglais américain est disponible en seconde piste.

Les sources des affirmations de cette vidéo, dont le FORTRAN Preliminary Report de 1954 et les chiffres du Bureau of Labor Statistics américain, sont citées dans la vidéo elle-même au fur et à mesure.

CRÉDITS PHOTO
La photographie d'archive de l'IBM 704 est de la NASA et relève du domaine public.

There's More To It — des questions dont les réponses sont plus longues qu'on ne le croit.
```

## Bahasa Indonesia (`id`)

```
Apa yang Terjadi Saat Programmer Berhenti Memprogram?
```

```
Bayangkan kamu seorang programmer. Suatu hari kamu membuka editor dan di dalamnya tidak ada lagi yang perlu kamu tulis, karena mesin bisa melakukannya. Selamat: kamu sekarang jadi manajer, hanya saja tanpa gaji manajer.

Tapi yang menarik bukan soal apakah kamu masih punya pekerjaan. Selama puluhan tahun kita mengajari programmer menulis kode yang bisa dibaca programmer lain — dan sekarang kita membangun mesin yang menulis kode yang mungkin tidak akan pernah dibaca programmer. Jadi, untuk apa kita selama ini berusaha membuat kode mudah dibaca?

Video ini mengikuti janji bahwa pemrograman akan hilang: dari laporan IBM tahun 1954 yang menyebut FORTRAN "diharapkan dapat menghilangkan hampir seluruh pekerjaan coding dan debugging", lewat COBOL dan sebuah buku tahun 1982 yang judulnya benar-benar Application Development Without Programmers, sampai apa yang sebenarnya terjadi pada pekerjaan itu — dan itu lebih aneh dari kelihatannya. Pada 2003 survei tenaga kerja Amerika menambahkan satu nama jabatan baru di samping yang lama, dan hari ini ada sekitar enam software developer untuk setiap satu computer programmer. Pekerjaannya tidak hilang. Namanya yang berganti.

Bab:
0:00 Tidak ada lagi yang perlu ditulis
1:10 Untuk apa keterbacaan itu?
1:19 Pemrograman selalu diotomatisasi
1:41 1954: "menghilangkan coding dan debugging"
2:58 Jadi berapa yang tersisa?
3:17 Kata yang berubah
3:58 Kenapa kali ini berbeda
4:48 Bukan lagi soal filsafat
5:11 Titik beratnya bergeser
6:00 Harga yang tak begitu terlihat
6:44 Gaya penulisan kode
7:23 Kapal-kapal dalam fiksi ilmiah
8:06 Apa yang tersisa bagi programmer
8:35 Bahasa yang ditulis untuk mesin
9:42 Kalimat yang keliru
10:02 Itu untuk kita

Subtitel ditulis khusus untuk video ini, bukan dibuat secara otomatis. Tersedia juga trek audio kedua dalam bahasa Inggris Amerika.

Sumber untuk klaim dalam video ini, termasuk FORTRAN Preliminary Report tahun 1954 dan angka-angka dari Bureau of Labor Statistics Amerika Serikat, disebutkan langsung di dalam video saat muncul.

KREDIT GAMBAR
Foto arsip IBM 704 dibuat oleh NASA dan berada dalam domain publik.

There’s More To It — pertanyaan yang jawabannya ternyata lebih panjang dari yang kamu kira.
```

## italiano (`it`)

```
Cosa succede quando i programmatori smettono di programmare?
```

```
Immagina di essere un programmatore. Un giorno apri l'editor e ti accorgi che lì dentro non è rimasto niente da scrivere, perché la macchina sa farlo. Complimenti: sei diventato un capo, solo senza lo stipendio da capo.

La cosa interessante però non è se hai ancora un lavoro. Per decenni abbiamo insegnato ai programmatori a scrivere codice che altri programmatori potessero leggere — e adesso costruiamo macchine che scrivono codice che forse nessun programmatore leggerà mai. A cosa serviva allora quella leggibilità?

Il video segue la promessa che programmare sarebbe scomparso: da una relazione IBM del 1954 secondo cui FORTRAN «dovrebbe praticamente eliminare la codifica e il debug», passando per COBOL e un libro del 1982 intitolato Application Development Without Programmers, fino a ciò che è davvero successo al mestiere — ed è più strano di quanto sembri. Nel 2003 l'indagine americana sul lavoro aggiunse una qualifica nuova accanto a quella vecchia, e oggi ci sono circa sei software developers per ogni computer programmer. Il lavoro non è sparito. Ha cambiato nome.

Capitoli:
0:00 Non resta niente da scrivere
1:10 A cosa serviva la leggibilità?
1:19 È sempre stato automatizzato
1:41 1954: "eliminare codifica e debug"
2:58 Quanti ne restavano, allora?
3:17 La parola che è cambiata
3:58 Perché stavolta è diverso
4:48 Smette di essere filosofia
5:11 Il baricentro si sposta
6:00 Il costo meno evidente
6:44 Lo stile del codice
7:23 Le navi nella fantascienza
8:06 Cosa resta al programmatore
8:35 Un linguaggio scritto per le macchine
9:42 La frase sbagliata
10:02 Era per noi

I sottotitoli sono scritti per questo video, non generati automaticamente. Come seconda traccia audio è disponibile l’inglese americano.

Le fonti delle affermazioni di questo video, compresi il FORTRAN Preliminary Report del 1954 e i dati del Bureau of Labor Statistics statunitense, sono citate nel video stesso man mano che compaiono.

CREDITI FOTOGRAFICI
La fotografia d'archivio dell'IBM 704 è della NASA ed è di pubblico dominio.

There's More To It — domande le cui risposte sono più lunghe di quanto ci si aspetti.
```

## Deutsch (`de`)

```
Was passiert, wenn Programmierer aufhören zu programmieren?
```

```
Stell dir vor, du bist Programmierer. Eines Tages öffnest du deinen Editor und merkst, dass darin nichts mehr übrig ist, was du schreiben müsstest, weil die Maschine das kann. Herzlichen Glückwunsch: du bist jetzt Manager, nur ohne das Gehalt eines Managers.

Interessant ist aber nicht, ob du noch einen Job hast. Jahrzehntelang brachten wir Programmierern bei, Code so zu schreiben, dass andere Programmierer ihn lesen können — und jetzt bauen wir Maschinen, die Code schreiben, den vielleicht nie ein Programmierer liest. Wofür war diese Lesbarkeit also da?

Das Video verfolgt das Versprechen, das Programmieren werde verschwinden: von einem IBM-Bericht aus dem Jahr 1954, nach dem FORTRAN „das Codieren und Debuggen praktisch überflüssig machen sollte", über COBOL und ein Buch von 1982 mit dem Titel Application Development Without Programmers bis zu dem, was mit dem Beruf tatsächlich geschah — und das ist seltsamer, als es aussieht. 2003 kam in der amerikanischen Arbeitsmarktbefragung neben dem alten Berufsnamen ein neuer dazu, und heute kommen rund sechs software developers auf einen computer programmer. Die Arbeit verschwand nicht. Sie wurde umbenannt.

Kapitel:
0:00 Nichts mehr zu schreiben
1:10 Wofür war die Lesbarkeit da?
1:19 Automatisiert wurde schon immer
1:41 1954: „Codieren und Debuggen überflüssig machen"
2:58 Wie viele blieben also übrig?
3:17 Das Wort, das sich änderte
3:58 Warum es diesmal anders ist
4:48 Keine reine Philosophie mehr
5:11 Der Schwerpunkt verschiebt sich
6:00 Die weniger sichtbaren Kosten
6:44 Programmierstil
7:23 Die Schiffe in der Science-Fiction
8:06 Was dem Programmierer bleibt
8:35 Eine Sprache für Maschinen
9:42 Der falsche Satz
10:02 Es war für uns

Die Untertitel wurden für dieses Video geschrieben, nicht automatisch erzeugt. Als zweite Tonspur steht amerikanisches Englisch bereit.

Die Quellen der Aussagen in diesem Video, darunter der FORTRAN Preliminary Report von 1954 und die Zahlen des US Bureau of Labor Statistics, werden im Video selbst genannt, sobald sie vorkommen.

BILDNACHWEIS
Die Archivaufnahme des IBM 704 stammt von der NASA und ist gemeinfrei.

There's More To It — Fragen, deren Antworten länger ausfallen als erwartet.
```

## polski (`pl`)

```
Co się stanie, gdy programiści przestaną programować?
```

```
Wyobraź sobie, że jesteś programistą. Pewnego dnia otwierasz edytor i orientujesz się, że nie zostało tam nic, co miałbyś napisać, bo maszyna to potrafi. Gratulacje: zostałeś szefem, tylko bez pensji szefa.

Ciekawe jednak nie jest to, czy nadal masz pracę. Przez dekady uczyliśmy programistów pisać kod tak, żeby mogli go czytać inni programiści — a teraz budujemy maszyny, które piszą kod, którego być może żaden programista nigdy nie przeczyta. Po co więc była ta czytelność?

Film śledzi obietnicę, że programowanie zniknie: od raportu IBM z 1954 roku, według którego FORTRAN „powinien praktycznie wyeliminować kodowanie i debugowanie", przez COBOL i książkę z 1982 roku zatytułowaną Application Development Without Programmers, aż po to, co naprawdę stało się z zawodem — a to jest dziwniejsze, niż wygląda. W 2003 roku w amerykańskim badaniu zatrudnienia obok starej nazwy pojawiła się nowa, a dziś na jednego computer programmer przypada około sześciu software developers. Praca nie zniknęła. Zmieniła nazwę.

Rozdziały:
0:00 Nie zostało nic do napisania
1:10 Po co była ta czytelność?
1:19 Automatyzowano od zawsze
1:41 1954: „wyeliminować kodowanie i debugowanie"
2:58 Ilu więc zostało?
3:17 Słowo, które się zmieniło
3:58 Dlaczego tym razem jest inaczej
4:48 Przestaje to być filozofia
5:11 Środek ciężkości się przesuwa
6:00 Mniej widoczny koszt
6:44 Styl pisania kodu
7:23 Statki w science fiction
8:06 Co zostaje programiście
8:35 Język pisany dla maszyn
9:42 Niewłaściwe zdanie
10:02 To było dla nas

Napisy są pisane do tego filmu, nie generowane automatycznie. Jako druga ścieżka dźwiękowa dostępny jest angielski amerykański.

Źródła twierdzeń z tego filmu, w tym FORTRAN Preliminary Report z 1954 roku i dane amerykańskiego Bureau of Labor Statistics, są podawane w samym filmie, kiedy się pojawiają.

ŹRÓDŁA ZDJĘĆ
Archiwalne zdjęcie komputera IBM 704 wykonała NASA i jest w domenie publicznej.

There's More To It — pytania, których odpowiedzi okazują się dłuższe, niż się wydaje.
```

## português (Brasil) (`pt-BR`)

```
O que acontece quando os programadores param de programar?
```

```
Imagine que você é programador. Um dia abre o editor e percebe que ali dentro não sobrou nada para você escrever, porque a máquina dá conta. Parabéns: você virou chefe, só que sem o salário de chefe.

O interessante, porém, não é se você ainda tem emprego. Por décadas ensinamos programadores a escrever código que outros programadores conseguissem ler — e agora construímos máquinas que escrevem código que talvez nenhum programador leia. Então para que servia toda aquela legibilidade?

O vídeo acompanha a promessa de que programar iria desaparecer: de um relatório da IBM de 1954 segundo o qual o FORTRAN "deveria praticamente eliminar a codificação e a depuração", passando pelo COBOL e por um livro de 1982 chamado Application Development Without Programmers, até o que de fato aconteceu com a profissão — e isso é mais estranho do que parece. Em 2003 a pesquisa de emprego americana acrescentou um novo cargo ao lado do antigo, e hoje há cerca de seis software developers para cada computer programmer. O trabalho não desapareceu. Ele foi renomeado.

Capítulos:
0:00 Não sobrou nada para escrever
1:10 Para que servia a legibilidade?
1:19 Sempre foi automatizado
1:41 1954: "eliminar a codificação e a depuração"
2:58 Quantos sobraram, então?
3:17 A palavra que mudou
3:58 Por que desta vez é diferente
4:48 Deixa de ser filosofia
5:11 O centro de gravidade se desloca
6:00 O custo menos visível
6:44 Estilo de código
7:23 As naves da ficção científica
8:06 O que resta ao programador
8:35 Uma linguagem escrita para máquinas
9:42 A frase errada
10:02 Era para nós

As legendas foram escritas para este vídeo, não geradas automaticamente. Como segunda faixa de áudio está disponível o inglês americano.

As fontes das afirmações deste vídeo, incluindo o FORTRAN Preliminary Report de 1954 e os números do Bureau of Labor Statistics dos EUA, são citadas no próprio vídeo à medida que as informações são apresentadas.

CRÉDITOS DE IMAGEM
A fotografia de arquivo do IBM 704 é da NASA e está em domínio público.

There's More To It — perguntas cujas respostas acabam sendo mais longas do que se espera.
```

## Türkçe (`tr`)

```
Programcılar Programlamayı Bıraktığında Ne Olur?
```

```
Bir programcı olduğunu düşün. Bir gün editörünü açıyorsun ve içinde yazacak hiçbir şey kalmamış, çünkü makine bunu yapabiliyor. Tebrikler: artık yöneticisin, ama yönetici maaşın yok.

Ama ilginç olan, hâlâ bir işinin olup olmadığı değil. Onlarca yıl boyunca programcılara, başka programcıların okuyabileceği kod yazmayı öğrettik — ve şimdi, belki hiçbir programcının okumayacağı kodu yazan makineler kuruyoruz. Peki bütün o okunabilirlik ne içindi?

Bu video, programlamanın ortadan kalkacağı vaadini izliyor: FORTRAN'ın "kodlamayı ve hata ayıklamayı neredeyse tamamen ortadan kaldırmasının beklendiğini" söyleyen 1954 tarihli IBM raporundan, COBOL'den ve adı birebir Application Development Without Programmers olan 1982 tarihli kitaptan, mesleğe gerçekte ne olduğuna kadar — ki bu göründüğünden daha tuhaf. 2003'te Amerikan işgücü anketi eski unvanın yanına ikinci bir unvan ekledi ve bugün her bir computer programmer'a karşılık yaklaşık altı software developer var. İş ortadan kalkmadı. Adı değişti.

Bölümler:
0:00 Yazacak bir şey kalmadı
1:10 Okunabilirlik ne içindi?
1:19 Hep otomatikleştirildi
1:41 1954: "kodlamayı ve hata ayıklamayı ortadan kaldırmak"
2:58 Peki geriye kaç kişi kaldı?
3:17 Değişen kelime
3:58 Bu sefer neden farklı
4:48 Felsefe olmaktan çıkıyor
5:11 Ağırlık merkezi kayıyor
6:00 Daha az fark edilen bedel
6:44 Kod yazma tarzı
7:23 Bilimkurgudaki gemiler
8:06 Programcıya ne kalıyor
8:35 Makineler için yazılmış bir dil
9:42 Yanlış cümle
10:02 Bizim içindi

Altyazılar bu video için yazıldı, otomatik olarak oluşturulmadı. İkinci ses parçası olarak Amerikan İngilizcesi de mevcut.

Bu videodaki iddiaların kaynakları — 1954 tarihli FORTRAN Preliminary Report ve ABD Bureau of Labor Statistics rakamları dahil — geçtikleri yerde videonun içinde belirtiliyor.

GÖRSEL KAYNAKLARI
IBM 704'ün arşiv fotoğrafı NASA'ya ait ve kamu malı.

There’s More To It — cevapları sandığından uzun çıkan sorular.
```

## українська (`uk`)

```
Що станеться, коли програмісти перестануть програмувати?
```

```
Уяви, що ти програміст. Одного дня ти відкриваєш редактор, а в ньому вже нема чого писати, бо це вміє машина. Вітаємо: ти став менеджером, тільки без менеджерської зарплати.

Але цікаве не те, чи є в тебе досі робота. Десятиліттями ми вчили програмістів писати код, який зможуть прочитати інші програмісти, — а тепер будуємо машини, які пишуть код, що його програміст, може, не прочитає ніколи. То для чого була вся ця читабельність?

Відео простежує обіцянку, що програмування зникне: від звіту IBM 1954 року, за яким FORTRAN «мав практично усунути кодування та зневадження», через COBOL і книжку 1982 року, яка так і називається — Application Development Without Programmers, до того, що з професією сталося насправді, — а це дивніше, ніж здається. У 2003 році американське обстеження робочої сили додало поруч зі старою назвою посади другу, і сьогодні на одного computer programmer припадає близько шести software developer. Робота не зникла. Її перейменували.

Розділи:
0:00 Не лишилося чого писати
1:10 Для чого була ця читабельність?
1:19 Автоматизували завжди
1:41 1954: «усунути кодування та зневадження»
2:58 То скільки їх лишилося?
3:17 Слово, яке змінилося
3:58 Чому цього разу інакше
4:48 Це перестає бути філософією
5:11 Центр ваги зміщується
6:00 Менш помітна ціна
6:44 Стиль написання коду
7:23 Кораблі у фантастиці
8:06 Що лишається програмісту
8:35 Мова, написана для машин
9:42 Хибне речення
10:02 Це було для нас

Субтитри написані для цього відео, а не згенеровані автоматично. Також доступна друга звукова доріжка — американською англійською.

Джерела тверджень у цьому відео, зокрема FORTRAN Preliminary Report 1954 року та дані американського Bureau of Labor Statistics, наведені прямо у відео, коли про них ідеться.

ДЖЕРЕЛА ЗОБРАЖЕНЬ
Архівний знімок IBM 704 зробило NASA, він у суспільному надбанні.

There’s More To It — питання, відповіді на які виявляються довшими, ніж очікуєш.
```

## Tiếng Việt (`vi`)

```
Điều gì xảy ra khi lập trình viên ngừng lập trình?
```

```
Hãy tưởng tượng bạn là một lập trình viên. Một ngày nọ bạn mở trình soạn thảo và trong đó không còn gì để bạn viết nữa, vì máy làm được rồi. Xin chúc mừng: bạn đã thành quản lý, chỉ là không có lương quản lý.

Nhưng điều thú vị không phải là bạn còn việc làm hay không. Suốt mấy chục năm chúng ta dạy lập trình viên viết mã sao cho lập trình viên khác đọc được — và giờ chúng ta đang dựng những cỗ máy viết ra mã mà có thể không lập trình viên nào đọc. Vậy bao công sức làm cho mã dễ đọc là để làm gì?

Video này lần theo lời hứa rằng lập trình sẽ biến mất: từ một báo cáo của IBM năm 1954 nói rằng FORTRAN "được kỳ vọng sẽ gần như loại bỏ việc viết mã và gỡ lỗi", qua COBOL và một cuốn sách năm 1982 mang chính cái tên Application Development Without Programmers, đến chuyện thực sự đã xảy ra với nghề này — và chuyện đó kỳ lạ hơn bạn tưởng. Năm 2003, khảo sát lao động của Mỹ thêm một chức danh thứ hai bên cạnh chức danh cũ, và ngày nay cứ một computer programmer thì có khoảng sáu software developer. Công việc không biến mất. Nó được đổi tên.

Các chương:
0:00 Không còn gì để viết
1:10 Tính dễ đọc là để làm gì?
1:19 Lập trình vẫn luôn được tự động hóa
1:41 1954: "loại bỏ việc viết mã và gỡ lỗi"
2:58 Vậy còn lại bao nhiêu?
3:17 Từ ngữ đã thay đổi
3:58 Vì sao lần này khác
4:48 Không còn là chuyện triết học
5:11 Trọng tâm dịch chuyển
6:00 Cái giá ít ai thấy
6:44 Phong cách viết mã
7:23 Những con tàu trong khoa học viễn tưởng
8:06 Còn lại gì cho lập trình viên
8:35 Một ngôn ngữ viết cho máy
9:42 Câu nói sai
10:02 Vì chúng ta

Phụ đề được viết riêng cho video này, không phải tạo tự động. Có thể chọn tiếng Anh Mỹ ở bản âm thanh thứ hai.

Nguồn cho các thông tin trong video này, gồm FORTRAN Preliminary Report năm 1954 và số liệu của Bureau of Labor Statistics Hoa Kỳ, được nêu ngay trong video khi chúng xuất hiện.

NGUỒN HÌNH ẢNH
Ảnh tư liệu về IBM 704 là của NASA và thuộc phạm vi công cộng.

There’s More To It — những câu hỏi mà câu trả lời hóa ra dài hơn bạn tưởng.
```

## čeština (`cs`)

```
Co se stane, až programátoři přestanou programovat?
```

```
Představ si, že jsi programátor. Jednou přijdeš do práce, otevřeš editor a zjistíš, že v něm pro tebe nezbylo nic na psaní, protože to zvládne stroj. Gratuluju: stal se z tebe manažer, jenom bez manažerského platu.

Zajímavé ale není to, jestli ještě máš práci. Desítky let jsme učili programátory psát kód tak, aby ho přečetli jiní programátoři — a teď stavíme stroje, které píšou kód, jejž už možná žádný programátor nepřečte. K čemu tedy ta čitelnost byla?

Video sleduje slib, že programování zmizí: od zprávy IBM z roku 1954, podle které měl FORTRAN „prakticky odstranit kódování a ladění", přes COBOL a knihu z roku 1982 s názvem Application Development Without Programmers až k tomu, co se s tou profesí opravdu stalo — a to je zvláštnější, než to vypadá. V roce 2003 přibyl v americkém průzkumu zaměstnanosti vedle starého názvu nový a dnes připadá zhruba šest softwarových vývojářů na jednoho počítačového programátora. Ta práce nezmizela. Přejmenovala se.

Kapitoly:
0:00 Nezbylo co psát
1:10 K čemu byla ta čitelnost?
1:19 Automatizovalo se odjakživa
1:41 1954: „odstranit kódování a ladění"
2:58 Kolik jich tedy zbylo?
3:17 Slovo, které se změnilo
3:58 Proč je to tentokrát jiné
4:48 Přestává to být filozofie
5:11 Těžiště se přesouvá
6:00 Méně nápadná cena
6:44 Styl psaní kódu
7:23 Lodě ve sci-fi
8:06 Co zbývá programátorovi
8:35 Jazyk psaný pro stroje
9:42 Špatná věta
10:02 Bylo to pro nás

Titulky jsou psané pro tohle video, ne strojový přepis. Jako druhá zvuková stopa je k dispozici americká angličtina.

Zdroje tvrzení z tohoto videa, včetně Předběžné zprávy o FORTRANu z roku 1954 a čísel amerického Bureau of Labor Statistics, jsou uvedené přímo ve videu, jak na ně přijde řada.

OBRAZOVÉ ZDROJE
Archivní snímek počítače IBM 704 pořídila NASA a je volným dílem.

There's More To It — otázky, jejichž odpovědi jsou delší, než člověk čeká.
```

## español (`es`)

```
¿Qué pasa cuando los programadores dejan de programar?
```

```
Imagina que eres programador. Un día abres tu editor y te das cuenta de que ahí dentro ya no queda nada que escribir, porque la máquina puede hacerlo. Enhorabuena: te has convertido en jefe, pero sin el sueldo de un jefe.

Lo interesante, sin embargo, no es si sigues teniendo trabajo. Durante décadas enseñamos a los programadores a escribir código que otros programadores pudieran leer — y ahora construimos máquinas que escriben código que quizá ningún programador lea nunca. ¿Para qué servía entonces esa legibilidad?

El vídeo sigue la promesa de que la programación desaparecería: desde un informe de IBM de 1954 según el cual FORTRAN "debería eliminar prácticamente la codificación y la depuración", pasando por COBOL y un libro de 1982 titulado Application Development Without Programmers, hasta lo que de verdad le ocurrió al oficio — que es más raro de lo que parece. En 2003 la encuesta laboral estadounidense añadió un título nuevo junto al antiguo, y hoy hay unos seis software developers por cada computer programmer. El trabajo no desapareció. Le cambiaron el nombre.

Capítulos:
0:00 No queda nada que escribir
1:10 ¿Para qué servía la legibilidad?
1:19 Siempre se ha automatizado
1:41 1954: "eliminar la codificación y la depuración"
2:58 ¿Cuántos quedaron entonces?
3:17 La palabra que cambió
3:58 Por qué esta vez es distinto
4:48 Deja de ser filosofía
5:11 El centro de gravedad se mueve
6:00 El coste menos visible
6:44 Estilo de código
7:23 Las naves de la ciencia ficción
8:06 Qué le queda al programador
8:35 Un lenguaje escrito para máquinas
9:42 La frase equivocada
10:02 Era para nosotros

Los subtítulos están escritos para este vídeo, no generados automáticamente. Como segunda pista de audio está disponible el inglés americano.

Las fuentes de las afirmaciones de este vídeo, entre ellas el FORTRAN Preliminary Report de 1954 y las cifras de la Oficina de Estadísticas Laborales de EE. UU., se citan en el propio vídeo a medida que se presentan las afirmaciones correspondientes.

CRÉDITOS DE IMAGEN
La fotografía de archivo del IBM 704 es de la NASA y es de dominio público.

There's More To It — preguntas cuyas respuestas resultan más largas de lo que uno espera.
```

## svenska (`sv`)

```
Vad händer när programmerare slutar programmera?
```

```
Tänk dig att du är programmerare. En dag öppnar du din editor och inser att det inte finns något kvar där inne för dig att skriva, för maskinen klarar det. Grattis: du har blivit chef, fast utan en chefs lön.

Det intressanta är dock inte om du fortfarande har ett jobb. I decennier lärde vi programmerare att skriva kod som andra programmerare kunde läsa — och nu bygger vi maskiner som skriver kod som kanske ingen programmerare läser. Vad var då all den där läsbarheten till för?

Videon följer löftet om att programmerandet skulle försvinna: från en IBM-rapport från 1954 enligt vilken FORTRAN "i praktiken borde undanröja kodning och felsökning", via COBOL och en bok från 1982 med titeln Application Development Without Programmers, fram till vad som faktiskt hände med yrket — och det är märkligare än det ser ut. År 2003 fick den amerikanska arbetskraftsundersökningen en ny yrkestitel bredvid den gamla, och i dag går det ungefär sex software developers på varje computer programmer. Jobbet försvann inte. Det bytte namn.

Kapitel:
0:00 Inget kvar att skriva
1:10 Vad var läsbarheten till för?
1:19 Det har alltid automatiserats
1:41 1954: ”eliminera kodning och felsökning”
2:58 Hur många fanns kvar då?
3:17 Ordet som ändrades
3:58 Varför det är annorlunda den här gången
4:48 Det slutar vara filosofi
5:11 Tyngdpunkten flyttas
6:00 Den mindre synliga kostnaden
6:44 Kodstil
7:23 Skeppen i science fiction
8:06 Vad återstår för programmeraren?
8:35 Ett språk skrivet för maskiner
9:42 Fel mening
10:02 Det var för oss

Undertexterna är skrivna för den här videon, inte automatgenererade. Som andra ljudspår finns amerikansk engelska.

Källorna till påståendena i den här videon, bland annat FORTRAN Preliminary Report från 1954 och siffrorna från amerikanska Bureau of Labor Statistics, anges i själva videon i samband med respektive påstående.

BILDKÄLLOR
Arkivbilden av IBM 704 är tagen av NASA och är public domain.

There's More To It — frågor vars svar visar sig vara längre än man tror.
```
