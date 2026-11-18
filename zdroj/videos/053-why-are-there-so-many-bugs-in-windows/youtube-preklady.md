# Lokalizované názvy a popisy — Why Are There So Many Bugs in Windows?

Podklad pro **YouTube Studio → video → Podrobnosti → Přidat jazyk**.
Pro každý jazyk jsou tu **dva bloky ke zkopírování**: název a popis.
Kopíruje se **celý blok mezi trojicí zpětných apostrofů**, co je mimo něj,
je poznámka. Anglický originál zůstává v `youtube.md` a nesahá se na něj.

Nahrává je `tools/lokalizace.py`, který čte právě tenhle formát.
Pořadí jazyků je podle YouTube Studia, tedy bajtově podle UTF-8
**českého názvu jazyka** (ne podle kódu a ne podle endonyma):
fi, fr, id, it, de, pl, pt-BR, tr, uk, vi, cs, es, sv — **třináct**.

## Co se NEPŘEKLÁDÁ

| | |
|---|---|
| **vlastní jména** | Windows, Windows 98, Windows 2000, Windows XP, Windows NT, Microsoft, Remote Desktop, Linux |
| **časy kapitol** | musí sedět na vteřinu, jinak je YouTube neuzná |
| **tagy** | YouTube je per-jazyk nemá |

Názvy kapitol se naopak **překládají** — divák je čte v seznamu pod videem.

> **Atribuce tu žádná není**, protože video nemá jedinou archivní scénu:
> snímky rozhraní Windows nejsou pod volnou licencí (`notes.md`).

## Kontrola čísel

| v popisu | pozor |
|---|---|
| **září 2026** | měsíc i rok, ne jen „nedávno" |
| **dvacet měsíců** | odstup dvou výskytů téhož zvukového bugu |
| **dvakrát za tři měsíce** | rozbitý nástroj na opravu |

Žádné číslo v popisu není v řádu miliard, takže past `billion`/`Billion`
tady nehrozí — ale **„twenty months" se nesmí zaokrouhlit** na „skoro dva
roky", je to ověřený výpočet (`factcheck.md`).

---

## suomi (`fi`)

```
Miksi Windowsissa on niin paljon bugeja?
```

```
Syyskuussa 2026 yksi ainoa Windows-päivityserä rikkoi äänet, Remote
Desktopin, virtuaalikoneiden jaetut kansiot ja joidenkin koneiden kyvyn
kirjautua oman yrityksensä verkkoon. Yksi erä. Yksi tiistai.

Jos tämä kuulostaa vain yhdeltä huonolta Windows-päivitykseltä, se ei
sitä ole. Microsoft julkaisee itse listan siitä, mitä kukin päivitys
rikkoi, ja yhden vuoden lista toistaa samaa kaavaa kuukaudesta toiseen.
Kahdesti kolmessa kuukaudessa päivitys rikkoi juuri sen työkalun, jolla
rikkinäinen kone korjataan. Yksi äänibugi ilmestyi tammikuussa ja uudelleen
kaksikymmentä kuukautta myöhemmin, samoin oirein ja samalla ilmoituksella.

Ilmeinen johtopäätös on, ettei Microsoft yksinkertaisesti osaa tehdä
ohjelmistoja. Paitsi että Microsoft ei tee vain Windowsia — ja modernit
pilvipalvelut, jotka on rakennettu äskettäin ihmisten toimesta, jotka
tiesivät tarkalleen mitä rakensivat, hajoavat myös.

Tämä video kertoo siitä, mitä pinnan alla oikeasti tapahtuu: vuosikymmenten
kerroksista, joita kukaan ei saa poistaa, siitä mitä se tekee testaamiselle,
ja miksi Windowsin syvin osa saattaa olla sen vähiten noloa.

Koko teksti, lähteet ja käännökset: https://theresmoretoit-channel.github.io/fi/videos/why-are-there-so-many-bugs-in-windows/

Luvut:
0:00 Yksi erä, yksi tiistai
0:47 Kursori vuodelta 1998
1:45 Saako kone yhä äänen aikaan?
2:51 Yksi vuosi listaa
3:24 Päivitys, joka rikkoi korjaustyökalun
3:43 Sama bugi kaksikymmentä kuukautta myöhemmin
4:09 Mikään tästä ei ole uutta
4:53 Mutta Microsoft ei tee vain Windowsia
5:43 Arkeologinen kaivaus, joka yhä toimii
6:34 Windows käyttäytymään kuin Windows
7:30 Tekoäly kirjoittaa nopeammin. Testaus ei.
8:41 Miksi ydin voisi olla erilainen?
9:32 Kovat reunaehdot
10:05 Mitä sen on täytynyt kestää
11:06 Joku luki vanhemman version
11:50 Outo johtopäätös

Tekstitykset on kirjoitettu tätä videota varten, ei generoitu
automaattisesti. Toisena ääniraitana on amerikanenglanti.
```

## français (`fr`)

```
Pourquoi y a-t-il autant de bugs dans Windows ?
```

```
En septembre 2026, un seul lot de mises à jour Windows a cassé le son,
Remote Desktop, les dossiers partagés des machines virtuelles et, sur
certains postes, la possibilité de se connecter au réseau de leur propre
entreprise. Un seul lot. Un seul mardi.

Si cela ressemble à une énième mauvaise mise à jour, ce n'en est pas une.
Microsoft publie lui-même la liste de ce que chaque mise à jour a cassé,
et une seule année de cette liste répète le même schéma mois après mois.
Deux fois en trois mois, une mise à jour a cassé l'outil qui sert
justement à réparer un ordinateur en panne. Un bug audio est apparu en
janvier, puis de nouveau vingt mois plus tard, avec le même symptôme et
le même message.

La conclusion évidente serait que Microsoft ne sait tout simplement pas
écrire de logiciels. Sauf que Microsoft ne fait pas que Windows — et que
les services cloud modernes, construits récemment par des gens qui
savaient exactement ce qu'ils faisaient, tombent en panne eux aussi.

Cette vidéo parle de ce qui se passe réellement en dessous : des
décennies de couches que personne n'a le droit de retirer, de ce que cela
fait aux tests, et de la raison pour laquelle la partie la plus profonde
de Windows est peut-être la moins embarrassante.

Transcription complète, sources et traductions : https://theresmoretoit-channel.github.io/fr/videos/why-are-there-so-many-bugs-in-windows/

Chapitres :
0:00 Un lot, un mardi
0:47 Le curseur de 1998
1:45 L'ordinateur peut-il encore émettre un son ?
2:51 Une seule année de la liste
3:24 La mise à jour qui a cassé l'outil de réparation
3:43 Le même bug, vingt mois plus tard
4:09 Rien de tout cela n'est nouveau
4:53 Mais Microsoft ne fait pas que Windows
5:43 Une fouille archéologique qui fonctionne encore
6:34 Faire que Windows se comporte comme Windows
7:30 L'IA écrit plus vite. Pas les tests.
8:41 Pourquoi le noyau serait-il différent ?
9:32 Des contraintes dures
10:05 Ce qu'il a dû encaisser
11:06 Quelqu'un a lu une version plus ancienne
11:50 L'étrange conclusion

Les sous-titres sont rédigés pour cette vidéo, ils ne sont pas générés
automatiquement. Une piste audio en anglais américain est disponible
en seconde piste.
```

## Bahasa Indonesia (`id`)

```
Mengapa Ada Begitu Banyak Bug di Windows?
```

```
Pada September 2026, satu batch pembaruan Windows merusak audio, Remote
Desktop, folder bersama di mesin virtual, dan kemampuan sebagian komputer
untuk masuk ke jaringan perusahaannya sendiri. Satu batch. Satu Selasa.

Kalau itu terdengar seperti sekadar pembaruan Windows yang buruk lagi,
bukan. Microsoft sendiri menerbitkan daftar apa saja yang dirusak setiap
pembaruan, dan satu tahun dari daftar itu mengulang pola yang sama dari
bulan ke bulan. Dua kali dalam tiga bulan, sebuah pembaruan merusak justru
alat yang dipakai untuk memperbaiki komputer yang rusak. Satu bug audio
muncul pada bulan Januari, lalu muncul lagi dua puluh bulan kemudian,
dengan gejala dan pesan yang sama.

Kesimpulan yang jelas adalah Microsoft memang tidak bisa membuat
perangkat lunak. Hanya saja Microsoft tidak cuma membuat Windows — dan
layanan cloud modern, yang dibangun belum lama ini oleh orang-orang yang
tahu persis apa yang mereka bangun, juga rusak.

Video ini tentang apa yang sebenarnya terjadi di bawah permukaan:
lapisan-lapisan puluhan tahun yang tidak boleh dihapus siapa pun, apa
akibatnya bagi pengujian, dan mengapa bagian terdalam Windows mungkin
justru bagian yang paling tidak memalukan.

Transkrip lengkap, sumber, dan terjemahan: https://theresmoretoit-channel.github.io/id/videos/why-are-there-so-many-bugs-in-windows/

Bab:
0:00 Satu batch, satu Selasa
0:47 Kursor dari tahun 1998
1:45 Apakah komputernya masih bisa bersuara?
2:51 Satu tahun dari daftar itu
3:24 Pembaruan yang merusak alat perbaikan
3:43 Bug yang sama, dua puluh bulan kemudian
4:09 Tidak ada yang baru dari semua ini
4:53 Tapi Microsoft tidak cuma membuat Windows
5:43 Situs penggalian yang masih berjalan
6:34 Membuat Windows berperilaku seperti Windows
7:30 AI menulis lebih cepat. Pengujian tidak.
8:41 Mengapa kernel bisa berbeda?
9:32 Batasan yang keras
10:05 Apa yang harus dilaluinya
11:06 Ada yang membaca versi lama
11:50 Kesimpulan yang aneh

Subtitel ditulis khusus untuk video ini, bukan hasil pembuatan otomatis.
Tersedia juga trek audio kedua dalam bahasa Inggris Amerika.
```

## italiano (`it`)

```
Perché ci sono così tanti bug in Windows?
```

```
Nel settembre 2026 un solo gruppo di aggiornamenti Windows ha rotto
l'audio, Remote Desktop, le cartelle condivise nelle macchine virtuali e,
su alcuni computer, la possibilità di accedere alla rete della propria
azienda. Un solo gruppo. Un solo martedì.

Se sembra l'ennesimo aggiornamento sbagliato, non lo è. Microsoft
pubblica da sé l'elenco di ciò che ogni aggiornamento ha rotto, e un solo
anno di quell'elenco ripete lo stesso schema mese dopo mese. Due volte in
tre mesi un aggiornamento ha rotto proprio lo strumento che serve a
riparare un computer guasto. Un bug audio è comparso a gennaio, e poi di
nuovo venti mesi dopo, con lo stesso sintomo e lo stesso messaggio.

La conclusione ovvia è che Microsoft semplicemente non sa scrivere
software. Solo che Microsoft non fa soltanto Windows — e anche i servizi
cloud moderni, costruiti di recente da persone che sapevano esattamente
cosa stavano costruendo, si rompono.

Questo video parla di ciò che accade davvero sotto la superficie: decenni
di strati che nessuno può rimuovere, di che cosa questo comporta per i
test, e del perché la parte più profonda di Windows potrebbe essere la
meno imbarazzante.

Trascrizione completa, fonti e traduzioni: https://theresmoretoit-channel.github.io/it/videos/why-are-there-so-many-bugs-in-windows/

Capitoli:
0:00 Un gruppo, un martedì
0:47 Il cursore del 1998
1:45 Il computer riesce ancora a emettere un suono?
2:51 Un solo anno di quell'elenco
3:24 L'aggiornamento che ha rotto lo strumento di riparazione
3:43 Lo stesso bug, venti mesi dopo
4:09 Niente di tutto questo è nuovo
4:53 Ma Microsoft non fa soltanto Windows
5:43 Uno scavo archeologico che funziona ancora
6:34 Far comportare Windows come Windows
7:30 L'IA scrive più in fretta. I test no.
8:41 Perché il kernel potrebbe essere diverso?
9:32 Vincoli duri
10:05 Che cosa ha dovuto reggere
11:06 Qualcuno ha letto una versione più vecchia
11:50 La strana conclusione

I sottotitoli sono scritti per questo video, non generati automaticamente.
Come seconda traccia audio è disponibile l'inglese americano.
```

## Deutsch (`de`)

```
Warum gibt es in Windows so viele Bugs?
```

```
Im September 2026 hat ein einziger Schwung Windows-Updates den Ton kaputt
gemacht, Remote Desktop, freigegebene Ordner in virtuellen Maschinen —
und bei manchen Rechnern die Fähigkeit, sich am eigenen Firmennetz
anzumelden. Ein Schwung. Ein Dienstag.

Falls das nach nur einem weiteren schlechten Windows-Update klingt: ist
es nicht. Microsoft veröffentlicht selbst eine Liste dessen, was jedes
Update kaputt gemacht hat, und ein einziges Jahr dieser Liste wiederholt
Monat für Monat dasselbe Muster. Zweimal in drei Monaten hat ein Update
ausgerechnet das Werkzeug zerstört, mit dem man einen kaputten Rechner
repariert. Ein Audio-Bug tauchte im Januar auf und zwanzig Monate später
noch einmal, mit demselben Symptom und derselben Meldung.

Der naheliegende Schluss wäre, dass Microsoft einfach keine Software
schreiben kann. Nur macht Microsoft nicht bloß Windows — und moderne
Cloud-Dienste, kürzlich gebaut von Leuten, die genau wussten, was sie
bauen, gehen ebenfalls kaputt.

In diesem Video geht es darum, was darunter wirklich passiert:
jahrzehntelange Schichten, die niemand entfernen darf, was das mit dem
Testen macht, und warum der tiefste Teil von Windows womöglich der am
wenigsten peinliche ist.

Vollständiger Text, Quellen und Übersetzungen: https://theresmoretoit-channel.github.io/de/videos/why-are-there-so-many-bugs-in-windows/

Kapitel:
0:00 Ein Schwung, ein Dienstag
0:47 Der Mauszeiger von 1998
1:45 Bringt der Rechner noch einen Ton heraus?
2:51 Ein einziges Jahr dieser Liste
3:24 Das Update, das das Reparaturwerkzeug zerstörte
3:43 Derselbe Bug, zwanzig Monate später
4:09 Nichts davon ist neu
4:53 Aber Microsoft macht nicht nur Windows
5:43 Eine archäologische Grabung, die noch läuft
6:34 Windows dazu bringen, sich wie Windows zu verhalten
7:30 KI schreibt schneller. Testen nicht.
8:41 Warum könnte der Kernel anders sein?
9:32 Harte Randbedingungen
10:05 Was er aushalten musste
11:06 Jemand hat eine ältere Version gelesen
11:50 Der seltsame Schluss

Die Untertitel sind für dieses Video geschrieben, nicht automatisch
erzeugt. Als zweite Tonspur steht amerikanisches Englisch bereit.
```

## polski (`pl`)

```
Dlaczego w Windowsie jest tyle błędów?
```

```
We wrześniu 2026 roku jedna partia aktualizacji Windowsa zepsuła dźwięk,
Remote Desktop, foldery współdzielone w maszynach wirtualnych oraz — na
części komputerów — możliwość zalogowania się do własnej sieci firmowej.
Jedna partia. Jeden wtorek.

Jeśli brzmi to jak kolejna nieudana aktualizacja, to nie jest. Microsoft
sam publikuje listę tego, co każda aktualizacja zepsuła, a jeden rok tej
listy powtarza ten sam wzorzec miesiąc po miesiącu. Dwa razy w ciągu
trzech miesięcy aktualizacja zepsuła właśnie to narzędzie, którym naprawia
się zepsuty komputer. Jeden błąd dźwięku pojawił się w styczniu, a potem
znowu dwadzieścia miesięcy później — z tym samym objawem i tym samym
komunikatem.

Oczywisty wniosek jest taki, że Microsoft po prostu nie umie pisać
oprogramowania. Tyle że Microsoft nie robi wyłącznie Windowsa — a
nowoczesne usługi chmurowe, zbudowane niedawno przez ludzi, którzy
dokładnie wiedzieli, co budują, też się psują.

Ten film jest o tym, co naprawdę dzieje się pod spodem: o dziesięcioleciach
warstw, których nikomu nie wolno usunąć, o tym, co to robi z testowaniem,
i dlaczego najgłębsza część Windowsa może być tą najmniej wstydliwą.

Pełna transkrypcja, źródła i tłumaczenia: https://theresmoretoit-channel.github.io/pl/videos/why-are-there-so-many-bugs-in-windows/

Rozdziały:
0:00 Jedna partia, jeden wtorek
0:47 Kursor z 1998 roku
1:45 Czy komputer nadal wyda dźwięk?
2:51 Jeden rok z tej listy
3:24 Aktualizacja, która zepsuła narzędzie naprawcze
3:43 Ten sam błąd, dwadzieścia miesięcy później
4:09 Nic z tego nie jest nowe
4:53 Ale Microsoft nie robi tylko Windowsa
5:43 Wykopalisko, które wciąż działa
6:34 Żeby Windows zachowywał się jak Windows
7:30 AI pisze szybciej. Testowanie nie.
8:41 Dlaczego jądro miałoby być inne?
9:32 Twarde ograniczenia
10:05 Co musiało przetrwać
11:06 Ktoś przeczytał starszą wersję
11:50 Dziwny wniosek

Napisy są napisane do tego filmu, nie wygenerowane automatycznie.
Jako druga ścieżka dźwiękowa dostępny jest angielski amerykański.
```

## português (Brasil) (`pt-BR`)

```
Por que existem tantos bugs no Windows?
```

```
Em setembro de 2026, um único lote de atualizações do Windows quebrou o
áudio, o Remote Desktop, as pastas compartilhadas em máquinas virtuais e,
em alguns computadores, a capacidade de fazer login na rede da própria
empresa. Um lote. Uma terça-feira.

Se isso soa como apenas mais uma atualização ruim do Windows, não é. A
própria Microsoft publica a lista do que cada atualização quebrou, e um
único ano dessa lista repete o mesmo padrão mês após mês. Duas vezes em
três meses, uma atualização quebrou justamente a ferramenta que serve
para consertar um computador quebrado. Um bug de áudio apareceu em
janeiro e apareceu de novo vinte meses depois, com o mesmo sintoma e a
mesma mensagem.

A conclusão óbvia é que a Microsoft simplesmente não sabe escrever
software. Só que a Microsoft não faz apenas o Windows — e serviços de
nuvem modernos, construídos recentemente por gente que sabia exatamente
o que estava construindo, também quebram.

Este vídeo é sobre o que realmente acontece por baixo: décadas de camadas
que ninguém tem permissão de remover, o que isso faz com os testes, e por
que a parte mais profunda do Windows talvez seja a menos vergonhosa.

Transcrição completa, fontes e traduções: https://theresmoretoit-channel.github.io/pt-br/videos/why-are-there-so-many-bugs-in-windows/

Capítulos:
0:00 Um lote, uma terça-feira
0:47 O cursor de 1998
1:45 O computador ainda consegue emitir som?
2:51 Um único ano da lista
3:24 A atualização que quebrou a ferramenta de reparo
3:43 O mesmo bug, vinte meses depois
4:09 Nada disso é novo
4:53 Mas a Microsoft não faz só o Windows
5:43 Uma escavação arqueológica que ainda funciona
6:34 Fazer o Windows se comportar como Windows
7:30 A IA escreve mais rápido. Testar, não.
8:41 Por que o kernel poderia ser diferente?
9:32 Restrições duras
10:05 O que ele teve de aguentar
11:06 Alguém leu uma versão mais antiga
11:50 A conclusão estranha

As legendas foram escritas para este vídeo, não geradas automaticamente.
Como segunda faixa de áudio está disponível o inglês americano.
```

## Türkçe (`tr`)

```
Windows'ta Neden Bu Kadar Çok Hata Var?
```

```
Eylül 2026'da tek bir Windows güncelleme paketi sesi, Remote Desktop'ı,
sanal makinelerdeki paylaşılan klasörleri ve bazı bilgisayarların kendi
şirket ağına oturum açabilmesini bozdu. Tek bir paket. Tek bir salı.

Bu size sadece kötü bir Windows güncellemesi gibi geliyorsa, değil.
Microsoft her güncellemenin neyi bozduğunu kendisi yayımlıyor ve bu
listenin tek bir yılı ay ay aynı deseni tekrarlıyor. Üç ay içinde iki kez
bir güncelleme, tam da bozuk bilgisayarı onarmaya yarayan aracı bozdu. Bir
ses hatası ocak ayında ortaya çıktı ve yirmi ay sonra yeniden çıktı; aynı
belirtiyle ve aynı iletiyle.

Bariz sonuç, Microsoft'un yazılım yazmayı beceremediği olurdu. Ama
Microsoft sadece Windows yapmıyor — ve yakın zamanda, ne inşa ettiğini
tam olarak bilen insanlar tarafından kurulmuş modern bulut hizmetleri de
bozuluyor.

Bu video, altta gerçekte ne olduğunu anlatıyor: kimsenin kaldırmasına izin
verilmeyen onlarca yıllık katmanlar, bunun teste ne yaptığı ve Windows'un
en derin parçasının neden en az utanç verici parça olabileceği.

Metnin tamamı, kaynaklar ve çeviriler: https://theresmoretoit-channel.github.io/tr/videos/why-are-there-so-many-bugs-in-windows/

Bölümler:
0:00 Tek paket, tek salı
0:47 1998'den kalma imleç
1:45 Bilgisayar hâlâ ses çıkarabiliyor mu?
2:51 Listenin tek bir yılı
3:24 Onarım aracını bozan güncelleme
3:43 Aynı hata, yirmi ay sonra
4:09 Bunların hiçbiri yeni değil
4:53 Ama Microsoft sadece Windows yapmıyor
5:43 Hâlâ çalışan bir arkeolojik kazı
6:34 Windows'u Windows gibi davrandırmak
7:30 Yapay zekâ daha hızlı yazıyor. Test etmek değil.
8:41 Çekirdek neden farklı olabilir?
9:32 Sert kısıtlar
10:05 Nelere dayanmak zorunda kaldı
11:06 Biri daha eski bir sürümü okudu
11:50 Tuhaf sonuç

Altyazılar bu video için yazıldı, otomatik olarak oluşturulmadı.
İkinci ses parçası olarak Amerikan İngilizcesi de mevcut.
```

## українська (`uk`)

```
Чому у Windows так багато багів?
```

```
У вересні 2026 року одна-єдина партія оновлень Windows зламала звук,
Remote Desktop, спільні теки у віртуальних машинах і — на частині
комп'ютерів — можливість увійти до власної корпоративної мережі. Одна
партія. Один вівторок.

Якщо це звучить як просто чергове невдале оновлення, то ні. Microsoft сама
публікує перелік того, що зламало кожне оновлення, і один рік цього
переліку повторює ту саму схему місяць за місяцем. Двічі за три місяці
оновлення зламало саме той інструмент, яким лагодять зламаний комп'ютер.
Один баг зі звуком з'явився в січні, а потім знову через двадцять місяців
— з тим самим симптомом і тим самим повідомленням.

Очевидний висновок — що Microsoft просто не вміє писати програми. От
тільки Microsoft робить не лише Windows, а сучасні хмарні сервіси,
збудовані нещодавно людьми, які точно знали, що будують, теж ламаються.

Це відео про те, що насправді відбувається під поверхнею: десятиліття
шарів, які нікому не дозволено прибрати, що це робить із тестуванням, і
чому найглибша частина Windows, можливо, є найменш ганебною.

Повний текст, джерела та переклади: https://theresmoretoit-channel.github.io/uk/videos/why-are-there-so-many-bugs-in-windows/

Розділи:
0:00 Одна партія, один вівторок
0:47 Курсор із 1998 року
1:45 Чи комп'ютер іще видасть звук?
2:51 Один рік цього переліку
3:24 Оновлення, яке зламало інструмент відновлення
3:43 Той самий баг через двадцять місяців
4:09 Нічого з цього не нове
4:53 Але Microsoft робить не лише Windows
5:43 Археологічні розкопки, які досі працюють
6:34 Змусити Windows поводитися як Windows
7:30 ШІ пише швидше. Тестування — ні.
8:41 Чому ядро може бути іншим?
9:32 Жорсткі обмеження
10:05 Що йому довелося витримати
11:06 Хтось прочитав старішу версію
11:50 Дивний висновок

Субтитри написані для цього відео, а не згенеровані автоматично.
Також доступна друга звукова доріжка — американською англійською.
```

## Tiếng Việt (`vi`)

```
Vì sao Windows có nhiều lỗi đến vậy?
```

```
Vào tháng 9 năm 2026, chỉ một đợt cập nhật Windows đã làm hỏng âm thanh,
Remote Desktop, thư mục chia sẻ trong máy ảo, và khả năng đăng nhập vào
chính mạng công ty của một số máy. Một đợt. Một ngày thứ Ba.

Nếu bạn nghĩ đây chỉ là thêm một bản cập nhật Windows tồi nữa, thì không
phải. Chính Microsoft công bố danh sách những gì mỗi bản cập nhật đã làm
hỏng, và chỉ một năm của danh sách đó đã lặp lại cùng một khuôn mẫu hết
tháng này sang tháng khác. Hai lần trong ba tháng, một bản cập nhật đã
làm hỏng đúng công cụ dùng để sửa một máy tính bị hỏng. Một lỗi âm thanh
xuất hiện vào tháng Giêng, rồi lại xuất hiện hai mươi tháng sau, với cùng
triệu chứng và cùng thông báo.

Kết luận hiển nhiên là Microsoft đơn giản là không biết viết phần mềm.
Có điều Microsoft không chỉ làm Windows — và các dịch vụ đám mây hiện đại,
được xây dựng gần đây bởi những người biết chính xác mình đang xây gì,
cũng hỏng.

Video này nói về điều thực sự diễn ra bên dưới: hàng chục năm các lớp mà
không ai được phép gỡ bỏ, điều đó gây ra gì cho việc kiểm thử, và vì sao
phần sâu nhất của Windows có lẽ lại là phần ít đáng xấu hổ nhất.

Toàn văn, nguồn và bản dịch: https://theresmoretoit-channel.github.io/vi/videos/why-are-there-so-many-bugs-in-windows/

Các chương:
0:00 Một đợt, một ngày thứ Ba
0:47 Con trỏ từ năm 1998
1:45 Máy tính còn phát ra tiếng được không?
2:51 Một năm của danh sách đó
3:24 Bản cập nhật làm hỏng công cụ sửa chữa
3:43 Cùng một lỗi, hai mươi tháng sau
4:09 Chẳng có gì trong số này là mới
4:53 Nhưng Microsoft không chỉ làm Windows
5:43 Một cuộc khai quật vẫn đang chạy
6:34 Làm cho Windows hành xử giống Windows
7:30 AI viết nhanh hơn. Kiểm thử thì không.
8:41 Vì sao nhân có thể khác?
9:32 Những ràng buộc cứng
10:05 Những gì nó đã phải chịu đựng
11:06 Có người đã đọc một phiên bản cũ hơn
11:50 Kết luận kỳ lạ

Phụ đề được viết riêng cho video này, không phải tạo tự động.
Có thể chọn tiếng Anh Mỹ ở bản âm thanh thứ hai.
```

## čeština (`cs`)

```
Proč je ve Windows tolik chyb?
```

```
V září 2026 rozbila jediná dávka aktualizací Windows zvuk, Vzdálenou
plochu, sdílené složky ve virtuálních strojích a některým počítačům
i schopnost přihlásit se do vlastní firemní sítě. Jedna dávka. Jedno
úterý.

Jestli to zní jako další nepovedená aktualizace, není. Microsoft sám
zveřejňuje seznam toho, co která aktualizace rozbila, a jediný rok toho
seznamu opakuje tentýž vzorec měsíc po měsíci. Dvakrát za tři měsíce
rozbila aktualizace zrovna ten nástroj, kterým se opravuje rozbitý
počítač. Jedna chyba se zvukem se objevila v lednu a pak znovu o dvacet
měsíců později — s týmž příznakem a toutéž hláškou.

Zjevný závěr je, že Microsoft prostě neumí dělat software. Jenže Microsoft
nedělá jenom Windows — a moderní cloudové služby, které vznikly nedávno
a stavěli je lidé, co přesně věděli, co staví, se rozbíjejí taky.

Tohle video je o tom, co se doopravdy děje vespod: o desítkách let vrstev,
které nikdo nesmí odebrat, o tom, co to dělá s testováním, a proč je
nejhlubší část Windows možná ta nejmíň trapná.

Celý text, zdroje a překlady: https://theresmoretoit-channel.github.io/cs/videos/why-are-there-so-many-bugs-in-windows/

Kapitoly:
0:00 Jedna dávka, jedno úterý
0:47 Kurzor z roku 1998
1:45 Vydá ten počítač ještě zvuk?
2:51 Jediný rok toho seznamu
3:24 Aktualizace, která rozbila nástroj na opravu
3:43 Tatáž chyba o dvacet měsíců později
4:09 Nic z toho není nové
4:53 Jenže Microsoft nedělá jenom Windows
5:43 Archeologický výkop, který pořád běží
6:34 Aby se Windows chovaly jako Windows
7:30 AI píše rychleji. Testování ne.
8:41 Proč by na tom jádro mohlo být jinak?
9:32 Tvrdá omezení
10:05 Co všechno muselo vydržet
11:06 Někdo si starší verzi přečetl
11:50 Podivný závěr

Titulky jsou k tomuhle videu napsané, ne vygenerované automaticky.
Jako druhá zvuková stopa je k dispozici americká angličtina.
```

## español (`es`)

```
¿Por qué hay tantos errores en Windows?
```

```
En septiembre de 2026, un único lote de actualizaciones de Windows rompió
el audio, Remote Desktop, las carpetas compartidas en máquinas virtuales
y, en algunos equipos, la capacidad de iniciar sesión en la red de su
propia empresa. Un lote. Un martes.

Si suena a una mala actualización más de Windows, no lo es. Microsoft
publica su propia lista de lo que rompió cada actualización, y un solo año
de esa lista repite el mismo patrón mes tras mes. Dos veces en tres meses,
una actualización rompió justamente la herramienta que sirve para reparar
un ordenador averiado. Un error de audio apareció en enero y volvió a
aparecer veinte meses después, con el mismo síntoma y el mismo mensaje.

La conclusión evidente sería que Microsoft simplemente no sabe escribir
software. Solo que Microsoft no hace únicamente Windows — y los servicios
en la nube modernos, construidos hace poco por gente que sabía exactamente
lo que estaba construyendo, también se rompen.

Este vídeo trata de lo que ocurre de verdad por debajo: décadas de capas
que nadie tiene permiso para quitar, lo que eso le hace a las pruebas, y
por qué la parte más profunda de Windows quizá sea la menos vergonzosa.

Transcripción completa, fuentes y traducciones: https://theresmoretoit-channel.github.io/es/videos/why-are-there-so-many-bugs-in-windows/

Capítulos:
0:00 Un lote, un martes
0:47 El cursor de 1998
1:45 ¿El ordenador todavía puede emitir un sonido?
2:51 Un solo año de esa lista
3:24 La actualización que rompió la herramienta de reparación
3:43 El mismo error, veinte meses después
4:09 Nada de esto es nuevo
4:53 Pero Microsoft no hace solo Windows
5:43 Una excavación arqueológica que todavía funciona
6:34 Hacer que Windows se comporte como Windows
7:30 La IA escribe más rápido. Probar, no.
8:41 ¿Por qué el núcleo podría ser distinto?
9:32 Restricciones duras
10:05 Lo que ha tenido que aguantar
11:06 Alguien sí leyó una versión más antigua
11:50 La conclusión extraña

Los subtítulos están escritos para este vídeo, no generados
automáticamente. Como segunda pista de audio está disponible
el inglés americano.
```

## svenska (`sv`)

```
Varför finns det så många buggar i Windows?
```

```
I september 2026 slog en enda omgång Windows-uppdateringar sönder ljudet,
Remote Desktop, delade mappar i virtuella maskiner och, på vissa datorer,
möjligheten att logga in på det egna företagsnätverket. En omgång. En
tisdag.

Om det låter som ännu en dålig Windows-uppdatering är det inte det.
Microsoft publicerar själv en lista över vad varje uppdatering har slagit
sönder, och ett enda år av den listan upprepar samma mönster månad efter
månad. Två gånger på tre månader slog en uppdatering sönder just det
verktyg man använder för att laga en trasig dator. En ljudbugg dök upp i
januari och dök upp igen tjugo månader senare, med samma symtom och samma
meddelande.

Den uppenbara slutsatsen vore att Microsoft helt enkelt inte kan skriva
programvara. Fast Microsoft gör inte bara Windows — och moderna
molntjänster, byggda nyligen av folk som visste precis vad de byggde, går
också sönder.

Den här videon handlar om vad som egentligen pågår under ytan:
årtionden av lager som ingen får ta bort, vad det gör med testningen, och
varför den djupaste delen av Windows kanske är den minst pinsamma.

Hela texten, källor och översättningar: https://theresmoretoit-channel.github.io/sv/videos/why-are-there-so-many-bugs-in-windows/

Kapitel:
0:00 En omgång, en tisdag
0:47 Muspekaren från 1998
1:45 Får datorn fortfarande fram ett ljud?
2:51 Ett enda år av listan
3:24 Uppdateringen som slog sönder reparationsverktyget
3:43 Samma bugg, tjugo månader senare
4:09 Inget av det här är nytt
4:53 Men Microsoft gör inte bara Windows
5:43 En arkeologisk utgrävning som fortfarande fungerar
6:34 Få Windows att bete sig som Windows
7:30 AI skriver snabbare. Testningen gör det inte.
8:41 Varför skulle kärnan vara annorlunda?
9:32 Hårda begränsningar
10:05 Vad den har fått stå ut med
11:06 Någon läste faktiskt en äldre version
11:50 Den märkliga slutsatsen

Undertexterna är skrivna för den här videon, inte automatgenererade.
Som andra ljudspår finns amerikansk engelska.
```
