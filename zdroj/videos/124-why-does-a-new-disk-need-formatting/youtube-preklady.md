# YouTube — 124 „Why Does a New Disk Need Formatting?“: lokalizace

Lokalizované názvy a popisy pro třináct jazyků (bez `en`, ten je
v `youtube.md`). Pořadí podle YouTube Studia. Nahrává
`python tools/lokalizace.py videos/124-why-does-a-new-disk-need-formatting`
— **až po Codexu**.

**Co se NEPŘEKLÁDÁ:**

- vlastní jména a názvy produktů (Linux, Windows, SSD),
- názvy filesystémů ext4, NTFS, Btrfs a název souboru `hello.txt`,
- `mke2fs 1.47.3` a jednotky TB/GB (ukrajinsky ТБ/ГБ, francouzsky To/Go),
- citace v řádku zdrojů (názvy dokumentů, nástroje e2fsprogs a btrfs-progs,
  autoři, rok, název článku, USENIX FAST); přeložené je jen úvodní slovo
  „Sources:“ a popisné části („Linux kernel documentation“, „the ext4 admin
  guide“, „btrfs-progs documentation“),
- časy kapitol, ty jsou na vteřinu shodné s angličtinou,
- tagy — YouTube je pro jednotlivé jazyky nemá.

Pointa (kam 17 GB zmizelo, S24–S28) se v popisu neprozrazuje, stejně jako
v angličtině; kapitola „Where did 17 GB go?“ zůstává otázkou. Odstavec
o titulcích a americké stopě je doslova z kanonické tabulky
v `docs/zverejneni.md`. Archivní snímky video nemá, takže blok atribucí
chybí ve všech jazycích. Registr jako v titulcích téhož jazyka (cs ty,
de du, sv du, pl ty, es tú, pt-BR você, fr tu, it tu, id kamu, tr sen,
uk ти, vi bạn, fi sinä); popis diváka oslovuje hned v první větě.
Terminologie (souborový systém, sešit, žurnál, obraz disku…) je převzatá
z `script.<kód>.md`, číslo 4 096 ve formátu titulků daného jazyka.

## suomi (`fi`)

```
Miksi uusi levy pitää alustaa?
```

```
Ostat upouuden yhden teratavun levyn ja alustat sen ext4:ksi, joka on vakiotiedostojärjestelmä monissa Linux-tietokoneissa. Ennen kuin olet tallentanut yhtäkään tiedostoa, noin seitsemäntoista gigatavua on poissa. Mitään ei ole vielä tallennettu. Mikä siis vie kaiken sen tilan? Ja miksi levy ylipäätään pitää alustaa?

Tässä videossa vastaus selvitetään perusteista lähtien: mitä levy oikeastaan tarjoaa tietokoneelle, mitä alustus lisää sen päälle ja mitä levyllä tapahtuu, kun tallennat yhden pienen tiedoston nimeltä hello.txt, kun poistat sen ja kun virta katkeaa kesken tallennuksen.

Matkan varrella: muistivihko, jossa on tuhat sivua, miksi viiden tavun tiedosto vie 4 096 tavua, miksi valtavan tiedoston siirtäminen voi käydä hetkessä, miksi poistetun tiedoston voi joskus palauttaa (ja miksi se on SSD:llä epätodennäköisempää), mihin journaalia tarvitaan ja miten ext4, NTFS ja Btrfs ratkaisevat saman tehtävän eri tavoin.

Luvut ovat peräisin 1 TB:n levykuvasta, joka alustettiin ext4:ksi oletusasetuksilla (mke2fs 1.47.3). Muut Linux-jakelut voivat käyttää eri oletuksia ja saada hieman eri luvun.

Lähteet: Linux-ytimen dokumentaatio, ext4 Data Structures and Algorithms ja ext4:n ylläpito-opas; e2fsprogs (mke2fs, dumpe2fs, debugfs); btrfs-progsin dokumentaatio; Bairavasundaram et al. (2008), An Analysis of Data Corruption in the Storage Stack, USENIX FAST.

Tekstitykset on kirjoitettu tätä videota varten, ei luotu automaattisesti. Toisena ääniraitana on amerikanenglanti.

LUVUT
00:00 Tyhjä levy, joka ei ole tyhjä
00:48 Paperikasa ja muistivihko
02:14 Mitä levyllä oikeasti on
03:10 Minne katosi 17 GB?
04:25 Tallennetaan hello.txt
05:01 Missä nimi on
06:14 Tiedoston poistaminen
07:09 Katkaise virta
07:51 Vauriot, joista kukaan ei kerro
08:22 Sama työ, eri valinnat
09:17 Mitä seuraavaksi
```

## français (`fr`)

```
Pourquoi faut-il formater un disque neuf ?
```

```
Tu achètes un disque tout neuf d’un téraoctet et tu le formates en ext4, le système de fichiers standard de nombreux ordinateurs sous Linux. Avant même d’avoir enregistré le moindre fichier, environ dix-sept gigaoctets ont disparu. Rien n’est encore stocké. Alors qu’est-ce qui prend toute cette place ? Et pourquoi faut-il formater un disque, pour commencer ?

Cette vidéo répond à ces questions en partant des bases : ce qu’un disque offre vraiment à un ordinateur, ce que le formatage ajoute par-dessus, et ce qui se passe sur le disque quand tu enregistres un tout petit fichier appelé hello.txt, quand tu le supprimes, et quand le courant est coupé en plein enregistrement.

En chemin : un cahier de mille pages, pourquoi un fichier de cinq octets occupe 4 096 octets, pourquoi déplacer un énorme fichier peut être instantané, pourquoi on peut parfois récupérer un fichier supprimé (et pourquoi c’est moins probable sur un SSD), à quoi sert un journal, et comment ext4, NTFS et Btrfs font des choix différents pour le même travail.

Les chiffres viennent du formatage en ext4 d’une image disque de 1 To avec les réglages par défaut (mke2fs 1.47.3). D’autres distributions Linux peuvent avoir d’autres valeurs par défaut et obtenir un chiffre légèrement différent.

Sources : documentation du noyau Linux, ext4 Data Structures and Algorithms et le guide d’administration d’ext4 ; e2fsprogs (mke2fs, dumpe2fs, debugfs) ; documentation de btrfs-progs ; Bairavasundaram et al. (2008), An Analysis of Data Corruption in the Storage Stack, USENIX FAST.

Les sous-titres sont écrits pour cette vidéo, pas générés automatiquement. Une piste audio en anglais américain est disponible en seconde piste.

CHAPITRES
00:00 Un disque vide qui ne l’est pas
00:48 Une pile de papier et un cahier
02:14 Ce qu’il y a vraiment sur le disque
03:10 Où sont passés 17 Go ?
04:25 Enregistrer hello.txt
05:01 Où se trouve le nom
06:14 Supprimer un fichier
07:09 Coupe le courant
07:51 Des dégâts que personne ne signale
08:22 Même travail, choix différents
09:17 La suite
```

## Bahasa Indonesia (`id`)

```
Mengapa Disk Baru Harus Diformat?
```

```
Kamu membeli disk satu terabyte yang benar-benar baru dan memformatnya dengan ext4, sistem berkas standar di banyak komputer Linux. Sebelum kamu menyimpan satu file pun, sekitar tujuh belas gigabyte sudah hilang. Belum ada yang disimpan. Jadi apa yang memakan semua ruang itu? Lagi pula, kenapa disk perlu diformat sejak awal?

Video ini menyusun jawabannya dari dasar: apa yang sebenarnya disediakan disk bagi komputer, apa yang ditambahkan pemformatan di atasnya, dan apa yang terjadi di disk saat kamu menyimpan satu file kecil bernama hello.txt, saat kamu menghapusnya, dan saat listrik padam di tengah penyimpanan.

Video ini juga membahas: buku catatan dengan seribu halaman, mengapa file berukuran lima byte memakan 4.096 byte, mengapa memindahkan file raksasa bisa terjadi seketika, mengapa file yang terhapus kadang bisa dipulihkan (dan mengapa hal itu lebih kecil kemungkinannya di SSD), apa gunanya jurnal, dan bagaimana ext4, NTFS, dan Btrfs menggunakan pendekatan yang berbeda untuk tugas yang sama.

Angka-angka ini berasal dari pemformatan image disk 1 TB dengan ext4 menggunakan pengaturan bawaan (mke2fs 1.47.3). Distribusi Linux lain bisa memakai pengaturan bawaan yang berbeda dan mendapatkan angka yang sedikit berbeda.

Sumber: dokumentasi kernel Linux, ext4 Data Structures and Algorithms dan panduan administrasi ext4; e2fsprogs (mke2fs, dumpe2fs, debugfs); dokumentasi btrfs-progs; Bairavasundaram et al. (2008), An Analysis of Data Corruption in the Storage Stack, USENIX FAST.

Subtitel ditulis khusus untuk video ini, bukan dibuat secara otomatis. Tersedia juga trek audio kedua dalam bahasa Inggris Amerika.

BAB
00:00 Disk kosong yang ternyata tidak kosong
00:48 Tumpukan kertas dan buku catatan
02:14 Apa yang sebenarnya ada di disk
03:10 Ke mana perginya 17 GB?
04:25 Menyimpan hello.txt
05:01 Di mana nama file disimpan
06:14 Menghapus file
07:09 Putuskan listriknya
07:51 Kerusakan yang tak dilaporkan siapa pun
08:22 Tugas sama, pilihan berbeda
09:17 Selanjutnya
```

## italiano (`it`)

```
Perché un disco nuovo va formattato?
```

```
Compri un disco nuovo di zecca da un terabyte e lo formatti in ext4, il file system standard di molti computer con Linux. Prima ancora di aver salvato un solo file, sono già spariti circa diciassette gigabyte. Non è ancora stato salvato niente. E allora cosa occupa tutto quello spazio? E perché mai un disco va formattato, tanto per cominciare?

Questo video arriva alla risposta partendo dalle basi: che cosa offre davvero un disco a un computer, che cosa ci aggiunge sopra la formattazione e che cosa succede sul disco quando salvi un minuscolo file chiamato hello.txt, quando lo cancelli e quando va via la corrente a metà del salvataggio.

Nel corso del video: un quaderno di mille pagine, perché un file di cinque byte occupa 4096 byte, perché spostare un file enorme può essere istantaneo, perché a volte un file cancellato si può recuperare (e perché su un SSD è meno probabile), a che cosa serve un journal e come ext4, NTFS e Btrfs fanno scelte diverse per lo stesso lavoro.

I numeri vengono dalla formattazione in ext4 di un’immagine disco da 1 TB con le impostazioni predefinite (mke2fs 1.47.3). Altre distribuzioni Linux possono usare valori predefiniti diversi e arrivare a un numero leggermente diverso.

Fonti: documentazione del kernel Linux, ext4 Data Structures and Algorithms e la guida di amministrazione di ext4; e2fsprogs (mke2fs, dumpe2fs, debugfs); documentazione di btrfs-progs; Bairavasundaram et al. (2008), An Analysis of Data Corruption in the Storage Stack, USENIX FAST.

I sottotitoli sono scritti per questo video, non generati automaticamente. Come seconda traccia audio è disponibile l’inglese americano.

CAPITOLI
00:00 Un disco vuoto che non lo è
00:48 Una pila di fogli e un quaderno
02:14 Cosa c’è davvero sul disco
03:10 Dove sono finiti 17 GB?
04:25 Salviamo hello.txt
05:01 Dove sta il nome
06:14 Cancellare un file
07:09 Stacca la corrente
07:51 Danni che nessuno segnala
08:22 Stesso lavoro, scelte diverse
09:17 Cosa viene dopo
```

## Deutsch (`de`)

```
Warum muss ein neues Laufwerk formatiert werden?
```

```
Du kaufst dir ein brandneues Laufwerk mit einem Terabyte und formatierst es mit ext4, dem Standard-Dateisystem auf vielen Linux-Rechnern. Noch bevor du eine einzige Datei gespeichert hast, sind rund siebzehn Gigabyte weg. Gespeichert ist noch gar nichts. Was belegt also den ganzen Platz? Und warum muss ein Laufwerk überhaupt formatiert werden?

Dieses Video entwickelt die Antwort Schritt für Schritt aus den Grundlagen: was ein Laufwerk einem Computer eigentlich bietet, was die Formatierung noch hinzufügt und was auf dem Laufwerk passiert, wenn du eine winzige Datei namens hello.txt speicherst, wenn du sie löschst und wenn mitten beim Speichern der Strom ausfällt.

Unterwegs: ein Notizbuch mit tausend Seiten, warum eine Fünf-Byte-Datei 4.096 Byte belegt, warum das Verschieben einer riesigen Datei sofort erledigt sein kann, warum sich eine gelöschte Datei manchmal wiederherstellen lässt (und warum das bei einer SSD weniger wahrscheinlich ist), wofür ein Journal da ist und wie ext4, NTFS und Btrfs dieselbe Aufgabe unterschiedlich lösen.

Die Zahlen stammen aus der Formatierung eines 1-TB-Disk-Images mit ext4 in den Standardeinstellungen (mke2fs 1.47.3). Andere Linux-Distributionen können andere Standardwerte verwenden und kommen dann auf einen leicht anderen Wert.

Quellen: Dokumentation des Linux-Kernels, ext4 Data Structures and Algorithms und das ext4-Handbuch für Administratoren; e2fsprogs (mke2fs, dumpe2fs, debugfs); Dokumentation von btrfs-progs; Bairavasundaram et al. (2008), An Analysis of Data Corruption in the Storage Stack, USENIX FAST.

Die Untertitel wurden für dieses Video geschrieben, nicht automatisch erzeugt. Als zweite Tonspur steht amerikanisches Englisch bereit.

KAPITEL
00:00 Ein leeres Laufwerk, das nicht leer ist
00:48 Ein Papierstapel und ein Notizbuch
02:14 Was wirklich auf dem Laufwerk ist
03:10 Wo sind die 17 GB hin?
04:25 hello.txt speichern
05:01 Wo der Name steht
06:14 Eine Datei löschen
07:09 Stecker ziehen
07:51 Schäden, die niemand meldet
08:22 Gleiche Aufgabe, andere Entscheidungen
09:17 Wie es weitergeht
```

## polski (`pl`)

```
Dlaczego nowy dysk trzeba sformatować?
```

```
Kupujesz nowiutki dysk o pojemności jednego terabajta i formatujesz go na ext4, standardowy system plików w wielu komputerach z Linuksem. Zanim zapiszesz choćby jeden plik, około siedemnastu gigabajtów już nie ma. Nic jeszcze nie zostało zapisane. Więc co zajmuje całe to miejsce? I po co w ogóle dysk trzeba formatować?

Ten film buduje odpowiedź od podstaw: co dysk naprawdę oferuje komputerowi, co dokłada do tego formatowanie i co dzieje się na dysku, kiedy zapisujesz jeden malutki plik o nazwie hello.txt, kiedy go usuwasz i kiedy w połowie zapisywania zabraknie prądu.

Po drodze: zeszyt z tysiącem stron, dlaczego pięciobajtowy plik zajmuje 4096 bajtów, dlaczego przeniesienie ogromnego pliku może odbyć się natychmiast, dlaczego usunięty plik czasem da się odzyskać (i dlaczego na SSD jest to mniej prawdopodobne), do czego służy dziennik i jak ext4, NTFS i Btrfs na różne sposoby realizują to samo zadanie.

Liczby pochodzą ze sformatowania obrazu dysku o pojemności 1 TB na ext4 z ustawieniami domyślnymi (mke2fs 1.47.3). Inne dystrybucje Linuksa mogą mieć inne wartości domyślne i uzyskać nieco inną liczbę.

Źródła: dokumentacja jądra Linuksa, ext4 Data Structures and Algorithms i podręcznik administratora ext4; e2fsprogs (mke2fs, dumpe2fs, debugfs); dokumentacja btrfs-progs; Bairavasundaram et al. (2008), An Analysis of Data Corruption in the Storage Stack, USENIX FAST.

Napisy są pisane do tego filmu, nie generowane automatycznie. Jako druga ścieżka dźwiękowa dostępny jest angielski amerykański.

ROZDZIAŁY
00:00 Pusty dysk, który pusty nie jest
00:48 Sterta papieru i zeszyt
02:14 Co naprawdę jest na dysku
03:10 Gdzie się podziało 17 GB?
04:25 Zapisujemy hello.txt
05:01 Gdzie mieszka nazwa
06:14 Usuwanie pliku
07:09 Odetnij prąd
07:51 Uszkodzenia, których nikt nie zgłasza
08:22 Ta sama praca, różne wybory
09:17 Co dalej
```

## português (Brasil) (`pt-BR`)

```
Por que um disco novo precisa ser formatado?
```

```
Você compra um disco novinho de um terabyte e formata com ext4, o sistema de arquivos padrão em muitos computadores com Linux. Antes de salvar um único arquivo, uns dezessete gigabytes já sumiram. Ainda não tem nada guardado. Então o que está ocupando todo esse espaço? E por que um disco precisa de formatação, para começo de conversa?

Este vídeo chega à resposta começando pelo básico: o que um disco realmente oferece a um computador, o que a formatação acrescenta por cima disso e o que acontece no disco quando você salva um arquivinho chamado hello.txt, quando apaga esse arquivo e quando a energia cai no meio do salvamento.

No caminho: um caderno com mil páginas, por que um arquivo de cinco bytes ocupa 4.096 bytes, por que mover um arquivo enorme pode ser instantâneo, por que um arquivo apagado às vezes pode ser recuperado (e por que isso é menos provável num SSD), para que serve um journal e como o ext4, o NTFS e o Btrfs fazem escolhas diferentes para o mesmo trabalho.

Os números vêm da formatação de uma imagem de disco de 1 TB com ext4 nas configurações padrão (mke2fs 1.47.3). Outras distribuições Linux podem usar configurações padrão diferentes e chegar a um número um pouco diferente.

Fontes: documentação do kernel Linux, ext4 Data Structures and Algorithms e o guia de administração do ext4; e2fsprogs (mke2fs, dumpe2fs, debugfs); documentação do btrfs-progs; Bairavasundaram et al. (2008), An Analysis of Data Corruption in the Storage Stack, USENIX FAST.

As legendas foram escritas para este vídeo, não geradas automaticamente. Como segunda faixa de áudio está disponível o inglês americano.

CAPÍTULOS
00:00 Um disco vazio que não está vazio
00:48 Uma pilha de papel e um caderno
02:14 O que de fato existe no disco
03:10 Para onde foram 17 GB?
04:25 Salvando hello.txt
05:01 Onde o nome mora
06:14 Apagando um arquivo
07:09 Corte a energia
07:51 Danos que ninguém relata
08:22 Mesmo trabalho, escolhas diferentes
09:17 O que vem a seguir
```

## Türkçe (`tr`)

```
Yeni Bir Diskin Neden Biçimlendirilmesi Gerekir?
```

```
Bir terabaytlık yepyeni bir disk alıyorsun ve onu birçok Linux bilgisayarındaki standart dosya sistemi olan ext4 ile biçimlendiriyorsun. Daha tek bir dosya kaydetmeden yaklaşık on yedi gigabayt gitmiş bile. Henüz hiçbir şey kaydedilmedi. Peki bütün o yeri ne kaplıyor? Hem bir disk neden biçimlendirilmeye ihtiyaç duyar ki?

Bu video, en temel bilgilerden başlayarak cevaba adım adım ulaşıyor: bir diskin bilgisayara aslında ne sunduğu, biçimlendirmenin bunun üstüne ne eklediği ve hello.txt adında minicik bir dosyayı kaydettiğinde, sildiğinde ve kaydetmenin ortasında elektrik kesildiğinde diskte neler olduğu.

Yol boyunca: bin sayfalık bir defter, beş baytlık bir dosyanın neden 4.096 bayt yer kapladığı, devasa bir dosyanın neden bir anda taşınabildiği, silinmiş bir dosyanın neden bazen kurtarılabildiği (ve bunun SSD'de neden daha az olası olduğu), günlüğün ne işe yaradığı ve ext4, NTFS ile Btrfs'in aynı iş için nasıl farklı tercihler yaptığı.

Rakamlar, 1 TB'lık bir disk görüntüsünün varsayılan ayarlarla ext4 olarak biçimlendirilmesinden geliyor (mke2fs 1.47.3). Diğer Linux dağıtımları farklı varsayılanlar kullanıp biraz farklı bir sonuç alabilir.

Kaynaklar: Linux çekirdeği belgeleri, ext4 Data Structures and Algorithms ve ext4 yönetici kılavuzu; e2fsprogs (mke2fs, dumpe2fs, debugfs); btrfs-progs belgeleri; Bairavasundaram et al. (2008), An Analysis of Data Corruption in the Storage Stack, USENIX FAST.

Altyazılar bu video için yazıldı, otomatik olarak oluşturulmadı. İkinci ses parçası olarak Amerikan İngilizcesi de mevcut.

BÖLÜMLER
00:00 Boş olmayan boş disk
00:48 Bir kâğıt yığını ve bir defter
02:14 Diskte gerçekte ne var
03:10 17 GB nereye gitti?
04:25 hello.txt dosyasını kaydetmek
05:01 Dosya adı nerede saklanır
06:14 Bir dosyayı silmek
07:09 Elektriği kes
07:51 Kimsenin bildirmediği hasar
08:22 Aynı iş, farklı tercihler
09:17 Sırada ne var
```

## українська (`uk`)

```
Чому новий диск треба форматувати?
```

```
Ти купуєш новенький диск на один терабайт і форматуєш його в ext4, стандартну файлову систему на багатьох комп’ютерах з Linux. Ще до того, як ти збережеш хоч один файл, приблизно сімнадцяти гігабайтів уже немає. Нічого ще не збережено. То що ж займає все це місце? І навіщо диску взагалі потрібне форматування?

У цьому відео відповідь складається крок за кроком, починаючи з основ: що диск насправді пропонує комп’ютеру, що форматування додає поверх цього і що відбувається на диску, коли ти зберігаєш один крихітний файл hello.txt, коли видаляєш його і коли посеред збереження зникає живлення.

Також у відео: зошит на тисячу сторінок, чому п’ятибайтовий файл займає 4096 байтів, чому переміщення величезного файлу може бути миттєвим, чому видалений файл іноді можна відновити (і чому на SSD це менш імовірно), навіщо потрібен журнал і як ext4, NTFS і Btrfs по-різному вирішують одне й те саме завдання.

Цифри отримано форматуванням образу диска на 1 ТБ в ext4 з налаштуваннями за замовчуванням (mke2fs 1.47.3). Інші дистрибутиви Linux можуть мати інші налаштування за замовчуванням і отримати трохи інше число.

Джерела: документація ядра Linux, ext4 Data Structures and Algorithms і посібник адміністратора ext4; e2fsprogs (mke2fs, dumpe2fs, debugfs); документація btrfs-progs; Bairavasundaram et al. (2008), An Analysis of Data Corruption in the Storage Stack, USENIX FAST.

Субтитри написані для цього відео, а не згенеровані автоматично. Також доступна друга звукова доріжка — американською англійською.

РОЗДІЛИ
00:00 Порожній диск, який не порожній
00:48 Купа паперу і зошит
02:14 Що насправді є на диску
03:10 Куди поділися 17 ГБ?
04:25 Зберігаємо hello.txt
05:01 Де живе назва
06:14 Видалення файлу
07:09 Вимкни живлення
07:51 Пошкодження, про які ніхто не повідомляє
08:22 Та сама робота, різні рішення
09:17 Що далі
```

## Tiếng Việt (`vi`)

```
Tại sao ổ đĩa mới cần được định dạng?
```

```
Bạn mua một ổ đĩa một terabyte mới tinh và định dạng nó bằng ext4, hệ thống tập tin tiêu chuẩn trên nhiều máy tính Linux. Trước khi bạn lưu dù chỉ một tập tin, khoảng mười bảy gigabyte đã biến mất. Chưa có gì được lưu cả. Vậy thứ gì đang chiếm hết chỗ đó? Mà rốt cuộc vì sao ổ đĩa lại cần định dạng?

Video này đi tìm câu trả lời từ những kiến thức cơ bản nhất: ổ đĩa thực sự cung cấp gì cho máy tính, việc định dạng bổ sung gì lên trên đó, và điều gì xảy ra trên ổ đĩa khi bạn lưu một tập tin nhỏ xíu tên là hello.txt, khi bạn xóa nó và khi mất điện giữa chừng lúc đang lưu.

Video cũng đề cập đến: một cuốn sổ có một nghìn trang, vì sao một tập tin năm byte lại chiếm 4.096 byte, vì sao di chuyển một tập tin khổng lồ có thể diễn ra tức thì, vì sao tập tin đã xóa đôi khi vẫn khôi phục được (và vì sao trên SSD thì khả năng đó thấp hơn), nhật ký dùng để làm gì, và ext4, NTFS và Btrfs đưa ra những lựa chọn khác nhau ra sao cho cùng một công việc.

Các con số đến từ việc định dạng một ảnh đĩa 1 TB bằng ext4 với thiết lập mặc định (mke2fs 1.47.3). Các bản phân phối Linux khác có thể dùng thiết lập mặc định khác và cho ra con số hơi khác.

Nguồn: tài liệu nhân Linux, ext4 Data Structures and Algorithms và hướng dẫn quản trị ext4; e2fsprogs (mke2fs, dumpe2fs, debugfs); tài liệu btrfs-progs; Bairavasundaram et al. (2008), An Analysis of Data Corruption in the Storage Stack, USENIX FAST.

Phụ đề được viết riêng cho video này, không phải tạo tự động. Có thể chọn tiếng Anh Mỹ ở bản âm thanh thứ hai.

CHƯƠNG
00:00 Ổ đĩa trống mà không trống
00:48 Một đống giấy và một cuốn sổ
02:14 Thứ thật sự nằm trên ổ đĩa
03:10 17 GB đã đi đâu?
04:25 Lưu hello.txt
05:01 Cái tên nằm ở đâu
06:14 Xóa một tập tin
07:09 Ngắt điện
07:51 Hư hỏng không ai báo
08:22 Cùng một việc, lựa chọn khác nhau
09:17 Tiếp theo là gì
```

## čeština (`cs`)

```
Proč se nový disk musí formátovat?
```

```
Koupíš si úplně nový disk s kapacitou jednoho terabajtu a naformátuješ ho na ext4, standardní souborový systém mnoha linuxových počítačů. Ještě než uložíš jediný soubor, zmizí zhruba sedmnáct gigabajtů. Uložené na něm zatím není nic. Tak co zabírá všechno to místo? A proč vlastně disk vůbec potřebuje formátování?

Video skládá odpověď od úplných základů: co disk počítači doopravdy nabízí, co k tomu přidá formátování a co se na disku děje, když uložíš jeden drobný soubor hello.txt, když ho smažeš a když uprostřed ukládání vypadne proud.

Cestou: sešit s tisícem stran, proč pětibajtový soubor zabere 4 096 bajtů, proč může být přesun obřího souboru okamžitý, proč jde smazaný soubor někdy obnovit (a proč je to u SSD méně pravděpodobné), k čemu je žurnál a jak ext4, NTFS a Btrfs řeší stejný úkol různými způsoby.

Čísla pocházejí z naformátování obrazu disku o velikosti 1 TB na ext4 s výchozím nastavením (mke2fs 1.47.3). Jiné linuxové distribuce můžou mít jiné výchozí hodnoty a dojít k mírně jinému číslu.

Zdroje: dokumentace linuxového jádra, ext4 Data Structures and Algorithms a příručka správce k ext4; e2fsprogs (mke2fs, dumpe2fs, debugfs); dokumentace btrfs-progs; Bairavasundaram et al. (2008), An Analysis of Data Corruption in the Storage Stack, USENIX FAST.

Titulky jsou psané pro tohle video, ne strojový přepis. Jako druhá zvuková stopa je k dispozici americká angličtina.

KAPITOLY
00:00 Prázdný disk, který prázdný není
00:48 Hromada papíru a sešit
02:14 Co je doopravdy na disku
03:10 Kam zmizelo 17 GB?
04:25 Ukládáme hello.txt
05:01 Kde je uložený název
06:14 Mazání souboru
07:09 Vypni proud
07:51 Poškození, které nikdo nehlásí
08:22 Stejná práce, různé volby
09:17 Co bude dál
```

## español (`es`)

```
¿Por qué hay que formatear un disco nuevo?
```

```
Te compras un disco nuevo de un terabyte y lo formateas con ext4, el sistema de archivos estándar de muchos ordenadores con Linux. Antes de que hayas guardado un solo archivo, ya han desaparecido unos diecisiete gigabytes. Todavía no hay nada almacenado. Entonces, ¿qué ocupa todo ese espacio? ¿Y por qué hay que formatear un disco en primer lugar?

Este vídeo llega a la respuesta partiendo de lo más básico: qué le ofrece realmente un disco a un ordenador, qué añade el formateo por encima, y qué pasa en el disco cuando guardas un archivo diminuto llamado hello.txt, cuando lo borras y cuando se corta la corriente a mitad del guardado.

Por el camino: un cuaderno de mil páginas, por qué un archivo de cinco bytes ocupa 4096 bytes, por qué mover un archivo enorme puede ser instantáneo, por qué a veces se puede recuperar un archivo borrado (y por qué es menos probable en un SSD), para qué sirve un diario (journal), y cómo ext4, NTFS y Btrfs toman decisiones distintas para el mismo trabajo.

Las cifras salen de formatear con ext4 una imagen de disco de 1 TB con la configuración predeterminada (mke2fs 1.47.3). Otras distribuciones de Linux pueden usar valores predeterminados distintos y obtener una cifra algo diferente.

Fuentes: documentación del kernel de Linux, ext4 Data Structures and Algorithms y la guía de administración de ext4; e2fsprogs (mke2fs, dumpe2fs, debugfs); documentación de btrfs-progs; Bairavasundaram et al. (2008), An Analysis of Data Corruption in the Storage Stack, USENIX FAST.

Los subtítulos están escritos para este vídeo, no generados automáticamente. Como segunda pista de audio está disponible el inglés americano.

CAPÍTULOS
00:00 Un disco vacío que no lo está
00:48 Un montón de papeles y un cuaderno
02:14 Qué hay de verdad en el disco
03:10 ¿Adónde se han ido 17 GB?
04:25 Guardamos hello.txt
05:01 Dónde vive el nombre
06:14 Borrar un archivo
07:09 Corta la corriente
07:51 Daños de los que nadie avisa
08:22 Mismo trabajo, decisiones distintas
09:17 Lo que viene
```

## svenska (`sv`)

```
Varför måste en ny disk formateras?
```

```
Du köper en helt ny disk på en terabyte och formaterar den med ext4, standardfilsystemet på många Linuxdatorer. Innan du har sparat en enda fil är ungefär sjutton gigabyte borta. Ingenting har lagrats än. Så vad är det som tar upp all den platsen? Och varför behöver en disk formateras över huvud taget?

Videon förklarar svaret från grunden: vad en disk faktiskt erbjuder en dator, vad formateringen lägger till ovanpå det, och vad som händer på disken när du sparar en liten fil som heter hello.txt, när du raderar den och när strömmen bryts mitt under sparandet.

På vägen: en anteckningsbok med tusen sidor, varför en fil på fem byte tar upp 4 096 byte, varför det kan gå på ett ögonblick att flytta en jättestor fil, varför en raderad fil ibland kan återställas (och varför det är mindre troligt på en SSD), vad en journal är till för, och hur ext4, NTFS och Btrfs gör olika val för samma jobb.

Siffrorna kommer från en diskavbild på 1 TB som formaterats med ext4 med standardinställningarna (mke2fs 1.47.3). Andra Linuxdistributioner kan ha andra standardvärden och få en något annorlunda siffra.

Källor: Linuxkärnans dokumentation, ext4 Data Structures and Algorithms och administratörsguiden för ext4; e2fsprogs (mke2fs, dumpe2fs, debugfs); dokumentationen för btrfs-progs; Bairavasundaram et al. (2008), An Analysis of Data Corruption in the Storage Stack, USENIX FAST.

Undertexterna är skrivna för den här videon, inte automatgenererade. Som andra ljudspår finns amerikansk engelska.

KAPITEL
00:00 En tom disk som inte är tom
00:48 En pappershög och en anteckningsbok
02:14 Vad som faktiskt finns på disken
03:10 Vart tog 17 GB vägen?
04:25 Vi sparar hello.txt
05:01 Var namnet finns
06:14 Radera en fil
07:09 Bryt strömmen
07:51 Skador som ingen rapporterar
08:22 Samma jobb, olika val
09:17 Vad som kommer härnäst
```
