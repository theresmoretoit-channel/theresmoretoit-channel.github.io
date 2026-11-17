# YouTube — 149 „Why Does Windows Only Have One Desktop?“: lokalizace

Lokalizované názvy a popisy pro třináct jazyků (bez `en`, ten je
v `youtube.md`). Pořadí podle YouTube Studia. Nahrává
`python tools/lokalizace.py videos/149-why-does-windows-only-have-one-desktop`.

**Co se NEPŘEKLÁDÁ:**

- vlastní jména a časy kapitol, ty jsou na vteřinu shodné s angličtinou (názvy programů, `explorer.exe`, hodnota *Shell*),
- řádek zdrojů, přeložené je jen úvodní slovo „Sources:“. Názvy dokumentů zůstávají anglicky, jsou to doklady,
- řádky s atribucí snímků; přeložené je jen slovo „screenshot“, nadpis, „via Wikimedia Commons“ a „Licence“,
- tagy — YouTube je pro jednotlivé jazyky nemá.

Pointa videa (*the desktop is the product*, S45) a omezení Shell Launcheru na edice Enterprise se v popisu neprozrazují.
Odstavec o titulcích a americké stopě je doslova z kanonické tabulky v `docs/zverejneni.md`.
Úvod popisu přebírá znění S01–S04 daného jazyka (`script.<kód>.md`) včetně názvů prvků Windows
po opravách Codexu (id *Mulai*, vi *Bắt đầu*). Explorer se jmenuje `explorer.exe` jako ve scénářích.
Registr podle překladů scénáře: tyká všech třináct jazyků (fi *sinä*, vi *bạn*, pt-BR *você*).

Codex (`codex lokalizace.txt`) zapracován: *two jobs* v popisu a kapitole 01:22 jako „funkce“, ne „práce“ (cs, fr, pt-BR, uk, es, sv; ve scénářích zůstává, tam navazuje S12), tr *alternatif* místo *yedek* (= záložní) a kapitola 04:44, uk a de „alternativní plochy“, it *attorno a LiteStep*, id a vi „jak bude plocha vypadat“, id kapitola 02:12 bez „biasa“, fi *vaihtoehtoiset*.

## suomi (`fi`)

```
Miksi Windowsissa on vain yksi työpöytä?
```

```
Kuvittele, että käynnistät Windows-koneen etkä löydä tehtäväpalkkia, Käynnistä-painiketta etkä ainuttakaan kuvaketta työpöydältä. Ohjelmasi, ajurisi ja tiedostosi ovat juuri siellä, mihin ne jätit. Vain työpöytä on vaihtunut, ja kytkin, joka sen vaihtaa, on yksi ainoa asetus. Miksi Windowsissa siis on vain yksi työpöytä?

Videossa käydään läpi asetus, joka ratkaisee, mikä työpöytäsi on, explorer.exen kaksi tehtävää, vaihtoehtoiset työpöydät, joita ihmiset ostivat 90-luvun alussa, LiteStep ja sen ympärille kasvanut yhteisö, Blackbox, bbLean ja Emerge Desktop, Cairo Desktop ja Seelen UI nykyisessä Windows 11:ssä sekä Microsoftin virallinen ominaisuus, jota olet ehkä käyttänyt lippuautomaatilla tietämättäsi.

Tämä ei ole ohje: jos muutat Shell-arvoa ilman toimivaa korvaajaa, voit jäädä kokonaan ilman työpöytää.

Lähteet: Microsoft Learn, Shell Launcher overview; Microsoft, Shell entry (Winlogon) and Custom user interface policy; Microsoft KB Q58341, Windows 3.0 SYSTEM.INI [boot] section; Windows Insider Blog, Build 18317 (2019); Cairo Desktop, ManagedShell source code; Wikipedia: LiteStep, Packard Bell Navigator, List of alternative shells for Windows.

Tekstitykset on kirjoitettu tätä videota varten, ei luotu automaattisesti. Toisena ääniraitana on amerikanenglanti.

LUVUT
00:00 Työpöytä ilman tehtäväpalkkia
00:25 Yksi asetus
00:50 Windows 3.0, 1990
01:11 Varsinainen kysymys
01:22 explorer.exen kaksi tehtävää
02:12 Androidissa se on asetus
02:26 Kuori, ikkunamanageri, työpöytä
02:57 Norton Desktop ja Packard Bell
03:40 LiteStep
04:18 Blackbox, bbLean ja Emerge
04:44 Miksi nähdä niin paljon vaivaa?
05:12 Mihin ne katosivat?
06:02 Cairo Desktop
06:28 Seelen UI
06:52 Entä Microsoft?
07:40 Miksi siis vain yksi?
07:52 Valinta Linuxissa
08:28 Ennen Windows 95:tä

KUVALÄHTEET
Norton Desktop for Windows -kuvakaappaus — Nathan Lineback, Toasty Tech GUI Gallery (toastytech.com/guis)
NonStep II desktop example — Meadowsd at English Wikipedia, GPL, Wikimedia Commonsin kautta
Lisenssi: gnu.org/licenses/gpl.html
```

## français (`fr`)

```
Pourquoi Windows n'a-t-il qu'un seul bureau ?
```

```
Imagine que tu allumes un PC sous Windows et que tu ne trouves ni barre des tâches, ni bouton Démarrer, ni une seule icône sur le bureau. Tes programmes, tes pilotes et tes fichiers sont exactement là où tu les as laissés. Seul le bureau a changé, et l'interrupteur qui le change est un simple réglage. Alors pourquoi Windows n'a-t-il qu'un seul bureau ?

Au programme : le réglage qui décide de ce qu'est ton bureau, les deux fonctions d'explorer.exe, les bureaux de remplacement qu'on achetait au début des années 90, LiteStep et la communauté qui s'est formée autour, Blackbox, bbLean et Emerge Desktop, Cairo Desktop et Seelen UI aujourd'hui sous Windows 11, et une fonctionnalité officielle de Microsoft que tu as peut-être déjà utilisée sur une borne de gare sans le savoir.

Ce n'est pas un tutoriel : modifier la valeur Shell sans remplaçant qui fonctionne peut te laisser sans aucun bureau.

Sources : Microsoft Learn, Shell Launcher overview; Microsoft, Shell entry (Winlogon) and Custom user interface policy; Microsoft KB Q58341, Windows 3.0 SYSTEM.INI [boot] section; Windows Insider Blog, Build 18317 (2019); Cairo Desktop, ManagedShell source code; Wikipedia: LiteStep, Packard Bell Navigator, List of alternative shells for Windows.

Les sous-titres sont écrits pour cette vidéo, pas générés automatiquement. Une piste audio en anglais américain est disponible en seconde piste.

CHAPITRES
00:00 Un bureau sans barre des tâches
00:25 Un seul réglage
00:50 Windows 3.0, 1990
01:11 La vraie question
01:22 Les deux fonctions d'explorer.exe
02:12 Sur Android, c'est un réglage
02:26 Shell, gestionnaire de fenêtres, bureau
02:57 Norton Desktop et Packard Bell
03:40 LiteStep
04:18 Blackbox, bbLean et Emerge
04:44 Pourquoi se donner tant de mal ?
05:12 Où sont-ils passés ?
06:02 Cairo Desktop
06:28 Seelen UI
06:52 Et Microsoft ?
07:40 Alors pourquoi un seul ?
07:52 Un choix sous Linux
08:28 Avant Windows 95

CRÉDITS DES IMAGES
Capture d'écran de Norton Desktop for Windows — Nathan Lineback, Toasty Tech GUI Gallery (toastytech.com/guis)
NonStep II desktop example — Meadowsd at English Wikipedia, GPL, via Wikimedia Commons
Licence : gnu.org/licenses/gpl.html
```

## Bahasa Indonesia (`id`)

```
Kenapa Windows Hanya Punya Satu Desktop?
```

```
Bayangkan kamu menyalakan PC Windows dan tidak menemukan taskbar, tombol Mulai, atau satu ikon pun di desktop. Program, driver, dan file kamu masih persis di tempat kamu meninggalkannya. Hanya desktopnya yang berubah, dan sakelar yang mengubahnya hanyalah satu pengaturan. Jadi, kenapa Windows hanya punya satu desktop?

Video ini membahas pengaturan yang menentukan seperti apa desktop kamu, dua tugas explorer.exe, desktop pengganti yang dibeli orang di awal tahun 90-an, LiteStep dan komunitas yang tumbuh di sekitarnya, Blackbox, bbLean, dan Emerge Desktop, Cairo Desktop dan Seelen UI di Windows 11 saat ini, serta fitur resmi Microsoft yang mungkin pernah kamu pakai di mesin tiket tanpa sadar.

Ini bukan tutorial: mengubah nilai Shell tanpa pengganti yang berfungsi bisa membuatmu sama sekali tanpa desktop.

Sumber: Microsoft Learn, Shell Launcher overview; Microsoft, Shell entry (Winlogon) and Custom user interface policy; Microsoft KB Q58341, Windows 3.0 SYSTEM.INI [boot] section; Windows Insider Blog, Build 18317 (2019); Cairo Desktop, ManagedShell source code; Wikipedia: LiteStep, Packard Bell Navigator, List of alternative shells for Windows.

Subtitel ditulis khusus untuk video ini, bukan dibuat secara otomatis. Tersedia juga trek audio kedua dalam bahasa Inggris Amerika.

BAB
00:00 Desktop tanpa taskbar
00:25 Satu pengaturan
00:50 Windows 3.0, 1990
01:11 Pertanyaan sebenarnya
01:22 Dua tugas explorer.exe
02:12 Di Android, itu sebuah pengaturan
02:26 Shell, window manager, desktop
02:57 Norton Desktop dan Packard Bell
03:40 LiteStep
04:18 Blackbox, bbLean, dan Emerge
04:44 Kenapa repot-repot begitu?
05:12 Ke mana semuanya?
06:02 Cairo Desktop
06:28 Seelen UI
06:52 Lalu Microsoft?
07:40 Jadi kenapa hanya satu?
07:52 Pilihan di Linux
08:28 Sebelum Windows 95

KREDIT GAMBAR
Tangkapan layar Norton Desktop for Windows — Nathan Lineback, Toasty Tech GUI Gallery (toastytech.com/guis)
NonStep II desktop example — Meadowsd at English Wikipedia, GPL, melalui Wikimedia Commons
Lisensi: gnu.org/licenses/gpl.html
```

## italiano (`it`)

```
Perché Windows ha un solo desktop?
```

```
Immagina di accendere un PC Windows e di non trovare la barra delle applicazioni, né il pulsante Start, né una sola icona sul desktop. I tuoi programmi, i driver e i file sono esattamente dove li avevi lasciati. È cambiato solo il desktop, e l'interruttore che lo cambia è una singola impostazione. Allora perché Windows ha un solo desktop?

In questo video: l'impostazione che decide che cos'è il tuo desktop, i due lavori di explorer.exe, i desktop sostitutivi che si compravano nei primi anni '90, LiteStep e la comunità nata attorno a LiteStep, Blackbox, bbLean ed Emerge Desktop, Cairo Desktop e Seelen UI oggi su Windows 11, e una funzione ufficiale di Microsoft che forse hai usato a una biglietteria automatica senza saperlo.

Non è un tutorial: cambiare il valore Shell senza un sostituto funzionante può lasciarti senza alcun desktop.

Fonti: Microsoft Learn, Shell Launcher overview; Microsoft, Shell entry (Winlogon) and Custom user interface policy; Microsoft KB Q58341, Windows 3.0 SYSTEM.INI [boot] section; Windows Insider Blog, Build 18317 (2019); Cairo Desktop, ManagedShell source code; Wikipedia: LiteStep, Packard Bell Navigator, List of alternative shells for Windows.

I sottotitoli sono scritti per questo video, non generati automaticamente. Come seconda traccia audio è disponibile l’inglese americano.

CAPITOLI
00:00 Un desktop senza barra delle applicazioni
00:25 Una sola impostazione
00:50 Windows 3.0, 1990
01:11 La vera domanda
01:22 I due lavori di explorer.exe
02:12 Su Android è un'impostazione
02:26 Shell, window manager, desktop
02:57 Norton Desktop e Packard Bell
03:40 LiteStep
04:18 Blackbox, bbLean ed Emerge
04:44 Perché darsi tanta pena?
05:12 Dove sono finiti?
06:02 Cairo Desktop
06:28 Seelen UI
06:52 E Microsoft?
07:40 Allora perché uno solo?
07:52 Una scelta su Linux
08:28 Prima di Windows 95

CREDITI DELLE IMMAGINI
Screenshot di Norton Desktop for Windows — Nathan Lineback, Toasty Tech GUI Gallery (toastytech.com/guis)
NonStep II desktop example — Meadowsd at English Wikipedia, GPL, tramite Wikimedia Commons
Licenza: gnu.org/licenses/gpl.html
```

## Deutsch (`de`)

```
Warum hat Windows nur einen Desktop?
```

```
Stell dir vor, du schaltest einen Windows-PC ein und findest keine Taskleiste, keinen Startknopf und kein einziges Symbol auf dem Desktop. Deine Programme, Treiber und Dateien sind genau da, wo du sie gelassen hast. Nur der Desktop hat sich geändert, und der Schalter, der ihn ändert, ist eine einzige Einstellung. Warum hat Windows also nur einen Desktop?

Im Video geht es um die Einstellung, die entscheidet, was dein Desktop ist, um die zwei Aufgaben des Explorers, um alternative Desktops, die man Anfang der 90er kaufen konnte, um LiteStep und die Community, die darum entstand, um Blackbox, bbLean und Emerge Desktop, um Cairo Desktop und Seelen UI unter Windows 11 heute und um eine offizielle Microsoft-Funktion, die du vielleicht schon an einem Fahrkartenautomaten benutzt hast, ohne es zu wissen.

Das ist keine Anleitung: Wer den Wert Shell ohne funktionierenden Ersatz ändert, steht am Ende womöglich ganz ohne Desktop da.

Quellen: Microsoft Learn, Shell Launcher overview; Microsoft, Shell entry (Winlogon) and Custom user interface policy; Microsoft KB Q58341, Windows 3.0 SYSTEM.INI [boot] section; Windows Insider Blog, Build 18317 (2019); Cairo Desktop, ManagedShell source code; Wikipedia: LiteStep, Packard Bell Navigator, List of alternative shells for Windows.

Die Untertitel wurden für dieses Video geschrieben, nicht automatisch erzeugt. Als zweite Tonspur steht amerikanisches Englisch bereit.

KAPITEL
00:00 Ein Desktop ohne Taskleiste
00:25 Eine einzige Einstellung
00:50 Windows 3.0, 1990
01:11 Die eigentliche Frage
01:22 Die zwei Aufgaben des Explorers
02:12 Bei Android ist es eine Einstellung
02:26 Shell, Fenstermanager, Desktop
02:57 Norton Desktop und Packard Bell
03:40 LiteStep
04:18 Blackbox, bbLean und Emerge
04:44 Warum der ganze Aufwand?
05:12 Wo sind sie geblieben?
06:02 Cairo Desktop
06:28 Seelen UI
06:52 Und Microsoft?
07:40 Warum also nur einer?
07:52 Eine Wahl unter Linux
08:28 Vor Windows 95

BILDNACHWEISE
Screenshot von Norton Desktop for Windows — Nathan Lineback, Toasty Tech GUI Gallery (toastytech.com/guis)
NonStep II desktop example — Meadowsd at English Wikipedia, GPL, über Wikimedia Commons
Lizenz: gnu.org/licenses/gpl.html
```

## polski (`pl`)

```
Dlaczego Windows ma tylko jeden pulpit?
```

```
Wyobraź sobie, że włączasz komputer z Windows i nie ma paska zadań, przycisku Start ani jednej ikony na pulpicie. Twoje programy, sterowniki i pliki są dokładnie tam, gdzie je zostawiłeś. Zmienił się tylko pulpit, a przełącznik, który go zmienia, to jedno ustawienie. Dlaczego więc Windows ma tylko jeden pulpit?

W filmie: ustawienie, które decyduje, czym jest twój pulpit, dwie funkcje explorer.exe, zastępcze pulpity, które kupowało się na początku lat 90., LiteStep i społeczność, która wokół niego wyrosła, Blackbox, bbLean i Emerge Desktop, Cairo Desktop i Seelen UI na dzisiejszym Windows 11, a także oficjalna funkcja Microsoftu, z której mogłeś już korzystać w biletomacie, nie wiedząc o tym.

To nie jest poradnik: zmiana wartości Shell bez działającego zamiennika może zostawić cię zupełnie bez pulpitu.

Źródła: Microsoft Learn, Shell Launcher overview; Microsoft, Shell entry (Winlogon) and Custom user interface policy; Microsoft KB Q58341, Windows 3.0 SYSTEM.INI [boot] section; Windows Insider Blog, Build 18317 (2019); Cairo Desktop, ManagedShell source code; Wikipedia: LiteStep, Packard Bell Navigator, List of alternative shells for Windows.

Napisy są pisane do tego filmu, nie generowane automatycznie. Jako druga ścieżka dźwiękowa dostępny jest angielski amerykański.

ROZDZIAŁY
00:00 Pulpit bez paska zadań
00:25 Jedno ustawienie
00:50 Windows 3.0, 1990
01:11 Prawdziwe pytanie
01:22 Dwie funkcje explorer.exe
02:12 W Androidzie to ustawienie
02:26 Powłoka, menedżer okien, pulpit
02:57 Norton Desktop i Packard Bell
03:40 LiteStep
04:18 Blackbox, bbLean i Emerge
04:44 Po co tyle zachodu?
05:12 Co się z nimi stało?
06:02 Cairo Desktop
06:28 Seelen UI
06:52 A Microsoft?
07:40 Dlaczego więc tylko jeden?
07:52 Wybór w Linuksie
08:28 Przed Windows 95

ŹRÓDŁA ILUSTRACJI
Zrzut ekranu Norton Desktop for Windows — Nathan Lineback, Toasty Tech GUI Gallery (toastytech.com/guis)
NonStep II desktop example — Meadowsd at English Wikipedia, GPL, via Wikimedia Commons
Licencja: gnu.org/licenses/gpl.html
```

## português (Brasil) (`pt-BR`)

```
Por que o Windows só tem uma área de trabalho?
```

```
Imagine ligar um PC com Windows e não encontrar barra de tarefas, nem botão Iniciar, nem um único ícone na área de trabalho. Seus programas, seus drivers e seus arquivos estão exatamente onde você os deixou. Só a área de trabalho mudou, e a chave que muda isso é uma única configuração. Então por que o Windows só tem uma área de trabalho?

Neste vídeo: a configuração que decide o que é a sua área de trabalho, as duas funções do explorer.exe, as áreas de trabalho substitutas que as pessoas compravam no começo dos anos 90, o LiteStep e a comunidade que cresceu em torno dele, o Blackbox, o bbLean e o Emerge Desktop, o Cairo Desktop e o Seelen UI no Windows 11 de hoje, e um recurso oficial da Microsoft que você talvez já tenha usado numa máquina de passagens sem saber.

Isto não é um tutorial: mudar o valor Shell sem um substituto que funcione pode deixar você sem área de trabalho nenhuma.

Fontes: Microsoft Learn, Shell Launcher overview; Microsoft, Shell entry (Winlogon) and Custom user interface policy; Microsoft KB Q58341, Windows 3.0 SYSTEM.INI [boot] section; Windows Insider Blog, Build 18317 (2019); Cairo Desktop, ManagedShell source code; Wikipedia: LiteStep, Packard Bell Navigator, List of alternative shells for Windows.

As legendas foram escritas para este vídeo, não geradas automaticamente. Como segunda faixa de áudio está disponível o inglês americano.

CAPÍTULOS
00:00 Uma área de trabalho sem barra de tarefas
00:25 Uma única configuração
00:50 Windows 3.0, 1990
01:11 A pergunta de verdade
01:22 As duas funções do explorer.exe
02:12 No Android, é uma configuração
02:26 Shell, gerenciador de janelas, desktop
02:57 Norton Desktop e Packard Bell
03:40 LiteStep
04:18 Blackbox, bbLean e Emerge
04:44 Por que ter tanto trabalho?
05:12 Onde eles foram parar?
06:02 Cairo Desktop
06:28 Seelen UI
06:52 E a Microsoft?
07:40 Então por que só uma?
07:52 Uma escolha no Linux
08:28 Antes do Windows 95

CRÉDITOS DAS IMAGENS
Captura de tela do Norton Desktop for Windows — Nathan Lineback, Toasty Tech GUI Gallery (toastytech.com/guis)
NonStep II desktop example — Meadowsd at English Wikipedia, GPL, via Wikimedia Commons
Licença: gnu.org/licenses/gpl.html
```

## Türkçe (`tr`)

```
Windows'ta Neden Tek Bir Masaüstü Var?
```

```
Bir Windows bilgisayarını açtığını düşün: ne görev çubuğu var, ne Başlat düğmesi, ne de masaüstünde tek bir simge. Programların, sürücülerin ve dosyaların tam bıraktığın yerde duruyor. Değişen yalnızca masaüstü ve onu değiştiren anahtar tek bir ayar. Peki Windows'ta neden tek bir masaüstü var?

Bu videoda şunlar var: masaüstünün ne olacağına karar veren ayar, explorer.exe'nin iki işi, 90'ların başında insanların satın aldığı alternatif masaüstleri, LiteStep ve etrafında oluşan topluluk, Blackbox, bbLean ve Emerge Desktop, bugün Windows 11'de çalışan Cairo Desktop ve Seelen UI, ve belki de farkında olmadan bir bilet makinesinde kullandığın resmî bir Microsoft özelliği.

Bu bir rehber değil: Shell değerini çalışan bir yedeği olmadan değiştirirsen masaüstün tamamen ortadan kalkabilir.

Kaynaklar: Microsoft Learn, Shell Launcher overview; Microsoft, Shell entry (Winlogon) and Custom user interface policy; Microsoft KB Q58341, Windows 3.0 SYSTEM.INI [boot] section; Windows Insider Blog, Build 18317 (2019); Cairo Desktop, ManagedShell source code; Wikipedia: LiteStep, Packard Bell Navigator, List of alternative shells for Windows.

Altyazılar bu video için yazıldı, otomatik olarak oluşturulmadı. İkinci ses parçası olarak Amerikan İngilizcesi de mevcut.

BÖLÜMLER
00:00 Görev çubuğu olmayan bir masaüstü
00:25 Tek bir ayar
00:50 Windows 3.0, 1990
01:11 Asıl soru
01:22 explorer.exe'nin iki işi
02:12 Android'de bu bir ayar
02:26 Kabuk, pencere yöneticisi, masaüstü
02:57 Norton Desktop ve Packard Bell
03:40 LiteStep
04:18 Blackbox, bbLean ve Emerge
04:44 Bunca zahmete neden katlanmalı?
05:12 Nereye gittiler?
06:02 Cairo Desktop
06:28 Seelen UI
06:52 Peki ya Microsoft?
07:40 Peki neden yalnızca bir tane?
07:52 Linux'ta bir seçim
08:28 Windows 95'ten önce

GÖRSEL KAYNAKLARI
Norton Desktop for Windows ekran görüntüsü — Nathan Lineback, Toasty Tech GUI Gallery (toastytech.com/guis)
NonStep II desktop example — Meadowsd at English Wikipedia, GPL, Wikimedia Commons aracılığıyla
Lisans: gnu.org/licenses/gpl.html
```

## українська (`uk`)

```
Чому у Windows лише один робочий стіл?
```

```
Уяви, що вмикаєш комп'ютер із Windows і не бачиш ні панелі завдань, ні кнопки «Пуск», ні жодного значка на робочому столі. Твої програми, драйвери й файли лежать саме там, де ти їх залишив. Змінився лише робочий стіл, а перемикач, що його змінює, — це одне-єдине налаштування. То чому у Windows лише один робочий стіл?

У відео: налаштування, яке визначає, що таке твій робочий стіл, дві функції explorer.exe, альтернативні робочі столи, які купували на початку 90-х, LiteStep і спільнота, що виросла навколо нього, Blackbox, bbLean та Emerge Desktop, Cairo Desktop і Seelen UI на сучасній Windows 11, а також офіційна функція Microsoft, якою ти, можливо, вже користувався біля квиткового автомата, навіть не знаючи про це.

Це не інструкція: якщо змінити значення Shell без робочої заміни, можна залишитися зовсім без робочого столу.

Джерела: Microsoft Learn, Shell Launcher overview; Microsoft, Shell entry (Winlogon) and Custom user interface policy; Microsoft KB Q58341, Windows 3.0 SYSTEM.INI [boot] section; Windows Insider Blog, Build 18317 (2019); Cairo Desktop, ManagedShell source code; Wikipedia: LiteStep, Packard Bell Navigator, List of alternative shells for Windows.

Субтитри написані для цього відео, а не згенеровані автоматично. Також доступна друга звукова доріжка — американською англійською.

РОЗДІЛИ
00:00 Робочий стіл без панелі завдань
00:25 Одне налаштування
00:50 Windows 3.0, 1990
01:11 Справжнє питання
01:22 Дві функції explorer.exe
02:12 В Android це налаштування
02:26 Оболонка, менеджер вікон, робочий стіл
02:57 Norton Desktop і Packard Bell
03:40 LiteStep
04:18 Blackbox, bbLean і Emerge
04:44 Навіщо стільки клопоту?
05:12 Куди вони поділися?
06:02 Cairo Desktop
06:28 Seelen UI
06:52 А Microsoft?
07:40 То чому лише один?
07:52 Вибір у Linux
08:28 До Windows 95

ДЖЕРЕЛА ЗОБРАЖЕНЬ
Знімок екрана Norton Desktop for Windows — Nathan Lineback, Toasty Tech GUI Gallery (toastytech.com/guis)
NonStep II desktop example — Meadowsd at English Wikipedia, GPL, через Wikimedia Commons
Ліцензія: gnu.org/licenses/gpl.html
```

## Tiếng Việt (`vi`)

```
Vì sao Windows chỉ có một desktop?
```

```
Hãy tưởng tượng bạn bật một máy tính Windows và không thấy thanh tác vụ, không có nút Bắt đầu, cũng chẳng có lấy một biểu tượng nào trên màn hình nền. Các chương trình, driver và tệp của bạn vẫn nằm đúng chỗ bạn để. Chỉ có desktop thay đổi, và công tắc thay đổi nó chỉ là một thiết lập duy nhất. Vậy vì sao Windows chỉ có một desktop?

Video này nói về thiết lập quyết định desktop của bạn sẽ như thế nào, hai việc mà explorer.exe làm, những desktop thay thế mà người ta mua vào đầu thập niên 90, LiteStep và cộng đồng hình thành quanh nó, Blackbox, bbLean và Emerge Desktop, Cairo Desktop và Seelen UI trên Windows 11 ngày nay, và một tính năng chính thức của Microsoft mà có thể bạn đã dùng ở máy bán vé mà không biết.

Đây không phải bài hướng dẫn: đổi giá trị Shell mà không có chương trình thay thế hoạt động được có thể khiến bạn không còn desktop nào cả.

Nguồn: Microsoft Learn, Shell Launcher overview; Microsoft, Shell entry (Winlogon) and Custom user interface policy; Microsoft KB Q58341, Windows 3.0 SYSTEM.INI [boot] section; Windows Insider Blog, Build 18317 (2019); Cairo Desktop, ManagedShell source code; Wikipedia: LiteStep, Packard Bell Navigator, List of alternative shells for Windows.

Phụ đề được viết riêng cho video này, không phải tạo tự động. Có thể chọn tiếng Anh Mỹ ở bản âm thanh thứ hai.

CHƯƠNG
00:00 Desktop không có thanh tác vụ
00:25 Một thiết lập duy nhất
00:50 Windows 3.0, 1990
01:11 Câu hỏi thực sự
01:22 Hai việc của explorer.exe
02:12 Trên Android, đó là một thiết lập
02:26 Shell, trình quản lý cửa sổ, desktop
02:57 Norton Desktop và Packard Bell
03:40 LiteStep
04:18 Blackbox, bbLean và Emerge
04:44 Sao phải mất công đến vậy?
05:12 Chúng đã đi đâu?
06:02 Cairo Desktop
06:28 Seelen UI
06:52 Còn Microsoft thì sao?
07:40 Vậy vì sao chỉ có một?
07:52 Một lựa chọn trên Linux
08:28 Trước Windows 95

NGUỒN HÌNH ẢNH
Ảnh chụp màn hình Norton Desktop for Windows — Nathan Lineback, Toasty Tech GUI Gallery (toastytech.com/guis)
NonStep II desktop example — Meadowsd at English Wikipedia, GPL, qua Wikimedia Commons
Giấy phép: gnu.org/licenses/gpl.html
```

## čeština (`cs`)

```
Proč má Windows jen jednu plochu?
```

```
Představ si, že zapneš počítač s Windows a nenajdeš žádný hlavní panel, žádné tlačítko Start a na ploše ani jednu ikonu. Tvoje programy, ovladače a soubory jsou přesně tam, kde jsi je nechal. Změnila se jen plocha a přepínač, který ji mění, je jediné nastavení. Proč má tedy Windows jen jednu plochu?

Ve videu se dozvíš o nastavení, které určuje, co je tvoje plocha, o dvou funkcích explorer.exe, o náhradních plochách, které si lidi kupovali na začátku devadesátých let, o LiteStepu a komunitě, která kolem něj vyrostla, o Blackboxu, bbLeanu a Emerge Desktopu, o Cairo Desktopu a Seelen UI na dnešním Windows 11 a o oficiální funkci Microsoftu, kterou jsi možná použil u automatu na jízdenky, aniž bys o tom věděl.

Tohle není návod: když hodnotu Shell přepíšeš bez funkční náhrady, můžeš zůstat úplně bez plochy.

Zdroje: Microsoft Learn, Shell Launcher overview; Microsoft, Shell entry (Winlogon) and Custom user interface policy; Microsoft KB Q58341, Windows 3.0 SYSTEM.INI [boot] section; Windows Insider Blog, Build 18317 (2019); Cairo Desktop, ManagedShell source code; Wikipedia: LiteStep, Packard Bell Navigator, List of alternative shells for Windows.

Titulky jsou psané pro tohle video, ne strojový přepis. Jako druhá zvuková stopa je k dispozici americká angličtina.

KAPITOLY
00:00 Plocha bez hlavního panelu
00:25 Jediné nastavení
00:50 Windows 3.0, 1990
01:11 Skutečná otázka
01:22 Dvě funkce explorer.exe
02:12 Na Androidu je to nastavení
02:26 Shell, správce oken, plocha
02:57 Norton Desktop a Packard Bell
03:40 LiteStep
04:18 Blackbox, bbLean a Emerge
04:44 Proč se s tím tolik dřít?
05:12 Kam se poděly?
06:02 Cairo Desktop
06:28 Seelen UI
06:52 A co Microsoft?
07:40 Tak proč jen jedna?
07:52 Volba na Linuxu
08:28 Před Windows 95

ZDROJE OBRÁZKŮ
Snímek obrazovky Norton Desktop for Windows — Nathan Lineback, Toasty Tech GUI Gallery (toastytech.com/guis)
NonStep II desktop example — Meadowsd at English Wikipedia, GPL, přes Wikimedia Commons
Licence: gnu.org/licenses/gpl.html
```

## español (`es`)

```
¿Por qué Windows solo tiene un escritorio?
```

```
Imagina que enciendes un PC con Windows y no encuentras barra de tareas, ni botón de Inicio, ni un solo icono en el escritorio. Tus programas, tus controladores y tus archivos están exactamente donde los dejaste. Solo ha cambiado el escritorio, y el interruptor que lo cambia es un único ajuste. Entonces, ¿por qué Windows solo tiene un escritorio?

En este vídeo: el ajuste que decide qué es tu escritorio, las dos funciones de explorer.exe, los escritorios de sustitución que la gente compraba a principios de los 90, LiteStep y la comunidad que creció a su alrededor, Blackbox, bbLean y Emerge Desktop, Cairo Desktop y Seelen UI hoy en Windows 11, y una función oficial de Microsoft que quizá hayas usado en una máquina de billetes sin saberlo.

Esto no es un tutorial: cambiar el valor Shell sin un sustituto que funcione puede dejarte sin ningún escritorio.

Fuentes: Microsoft Learn, Shell Launcher overview; Microsoft, Shell entry (Winlogon) and Custom user interface policy; Microsoft KB Q58341, Windows 3.0 SYSTEM.INI [boot] section; Windows Insider Blog, Build 18317 (2019); Cairo Desktop, ManagedShell source code; Wikipedia: LiteStep, Packard Bell Navigator, List of alternative shells for Windows.

Los subtítulos están escritos para este vídeo, no generados automáticamente. Como segunda pista de audio está disponible el inglés americano.

CAPÍTULOS
00:00 Un escritorio sin barra de tareas
00:25 Un único ajuste
00:50 Windows 3.0, 1990
01:11 La verdadera pregunta
01:22 Las dos funciones de explorer.exe
02:12 En Android es un ajuste
02:26 Shell, gestor de ventanas, escritorio
02:57 Norton Desktop y Packard Bell
03:40 LiteStep
04:18 Blackbox, bbLean y Emerge
04:44 ¿Por qué tomarse tantas molestias?
05:12 ¿Adónde fueron?
06:02 Cairo Desktop
06:28 Seelen UI
06:52 ¿Y Microsoft?
07:40 Entonces, ¿por qué solo uno?
07:52 Una elección en Linux
08:28 Antes de Windows 95

CRÉDITOS DE LAS IMÁGENES
Captura de pantalla de Norton Desktop for Windows — Nathan Lineback, Toasty Tech GUI Gallery (toastytech.com/guis)
NonStep II desktop example — Meadowsd at English Wikipedia, GPL, vía Wikimedia Commons
Licencia: gnu.org/licenses/gpl.html
```

## svenska (`sv`)

```
Varför har Windows bara ett skrivbord?
```

```
Tänk dig att du startar en Windows-dator och inte hittar något aktivitetsfält, ingen Start-knapp och inte en enda ikon på skrivbordet. Dina program, drivrutiner och filer ligger precis där du lämnade dem. Det är bara skrivbordet som har ändrats, och reglaget som ändrar det är en enda inställning. Så varför har Windows bara ett skrivbord?

I videon går vi igenom inställningen som avgör vad ditt skrivbord är, de två funktioner som explorer.exe har, ersättningsskrivborden som folk köpte i början av 90-talet, LiteStep och gemenskapen som växte fram kring det, Blackbox, bbLean och Emerge Desktop, Cairo Desktop och Seelen UI på dagens Windows 11, och en officiell Microsoft-funktion som du kanske har använt i en biljettautomat utan att veta om det.

Det här är ingen guide: ändrar du värdet Shell utan en fungerande ersättare kan du bli helt utan skrivbord.

Källor: Microsoft Learn, Shell Launcher overview; Microsoft, Shell entry (Winlogon) and Custom user interface policy; Microsoft KB Q58341, Windows 3.0 SYSTEM.INI [boot] section; Windows Insider Blog, Build 18317 (2019); Cairo Desktop, ManagedShell source code; Wikipedia: LiteStep, Packard Bell Navigator, List of alternative shells for Windows.

Undertexterna är skrivna för den här videon, inte automatgenererade. Som andra ljudspår finns amerikansk engelska.

KAPITEL
00:00 Ett skrivbord utan aktivitetsfält
00:25 En enda inställning
00:50 Windows 3.0, 1990
01:11 Den egentliga frågan
01:22 explorer.exe har två funktioner
02:12 På Android är det en inställning
02:26 Skal, fönsterhanterare, skrivbord
02:57 Norton Desktop och Packard Bell
03:40 LiteStep
04:18 Blackbox, bbLean och Emerge
04:44 Varför göra sig så mycket besvär?
05:12 Vart tog de vägen?
06:02 Cairo Desktop
06:28 Seelen UI
06:52 Och Microsoft?
07:40 Så varför bara ett?
07:52 Ett val på Linux
08:28 Före Windows 95

BILDKÄLLOR
Skärmbild av Norton Desktop for Windows — Nathan Lineback, Toasty Tech GUI Gallery (toastytech.com/guis)
NonStep II desktop example — Meadowsd at English Wikipedia, GPL, via Wikimedia Commons
Licens: gnu.org/licenses/gpl.html
```
