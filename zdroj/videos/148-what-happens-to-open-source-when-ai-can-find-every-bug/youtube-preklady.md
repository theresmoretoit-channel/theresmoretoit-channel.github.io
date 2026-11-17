# YouTube — 148 „What Happens to Open Source When AI Can Find Every Bug?“: lokalizace

Lokalizované názvy a popisy pro třináct jazyků (bez `en`, ten je
v `youtube.md`). Pořadí podle YouTube Studia. Nahrává
`python tools/lokalizace.py videos/148-what-happens-to-open-source-when-ai-can-find-every-bug`.

**Co se NEPŘEKLÁDÁ:**

- vlastní jména a časy kapitol, ty jsou na vteřinu shodné s angličtinou (v cyrilici *Лінус Торвальдс*, *Ерік Реймонд* podle scénáře),
- řádek zdrojů, přeložené je jen úvodní slovo „Sources:“. Názvy článků a knih zůstávají anglicky, jsou to doklady,
- řádky s atribucí snímků; přeložené jsou jen nadpis, „via Wikimedia Commons“, „Licences“ a slovo *logo*,
- tagy — YouTube je pro jednotlivé jazyky nemá.

Pointa videa (nikdo neví, co je bezpečnější, S61; utajení je práh, S39; rozhoduje doba do instalace, S65)
se v popisu neprozrazuje. Odstavec o titulcích a americké stopě je doslova z kanonické tabulky
v `docs/zverejneni.md`. Úvod popisu přebírá znění S01, S02, S06 a S07 daného jazyka (`script.<kód>.md`),
názvy kapitol termíny ze scénáře.

Codex (`codex lokalizace.txt`) zapracován: *OpenAI's run against the Linux kernel* znělo ve všech jazycích jako útok na jádro, přepsáno na testovací běh (i v angličtině), cs titul *dokáže najít*. Odmítnuto: kapitola 02:53 v množném čísle (podmětem jsou agenti, S20), fr/es *tous les bugs / todos los errores* (přirozenější než *chaque*), pl *w swój comiesięczny dzień* ve scénáři (akuzativ času je správně). Registr podle překladů scénáře: tyká všech třináct jazyků
(fi *sinä*, vi *bạn*, pt-BR *você*).

## suomi (`fi`)

```
Mitä avoimelle lähdekoodille tapahtuu, kun tekoäly löytää jokaisen bugin?
```

```
948. Niin monta eri tapaa tekoäly löysi Linux-tietokoneen kaappaamiseen sisältäpäin, ja jokainen alkaa tavallisesta käyttäjästä, jolla ei ole mitään erityisoikeuksia. Linuxin koodi on julkinen, ja vuosikymmeniä juuri se oli perustelu sille, miksi Linux on turvallinen. Jos siis kone pystyy lukemaan julkista koodia ja tekemään siitä toimivia hyökkäyskoodeja tässä mittakaavassa, pitäisikö ohjelmistojen sittenkin pitää koodinsa salassa?

Videossa käydään läpi OpenAI:n testiajo Linuxin ytimellä, Microsoftin ennätyskuukausi tietoturvakorjauksissa, Heartbleed-bugi, joka makasi julkisessa koodissa kaksi vuotta, se, mitä tekoäly saa irti Windowsin korjauksesta ilman lähdekoodia, miksi Linuxin ydin pitää nyt tekoälyllä löydettyjä bugeja julkisina, sekä kaksi kuukautta Windowsin korjauksen ja WannaCryn välillä.

Lähteet: OpenAI, "A thousand fewer paths to root" (2026); Anthropic, "N-days" (2026); Linux kernel documentation, security-bugs.rst; Linus Torvalds, Linux 7.1-rc4 announcement (2026); Eric S. Raymond, The Cathedral and the Bazaar (1999); Phoronix; TechSpot; The Register.

Tekstitykset on kirjoitettu tätä videota varten, ei luotu automaattisesti. Toisena ääniraitana on amerikanenglanti.

LUVUT
00:00 948 tietä sisään
00:42 Julkinen koodi
01:02 Microsoftin suljettu koodi
01:44 Miten kone toimii
02:53 Lähetettiin avaamaan yksi ovi
03:40 Tärkeä rajoitus
04:17 Kun silmäpareja on tarpeeksi
04:36 Heartbleed
05:27 Auttaako piilottaminen?
05:43 Ennen korjausta ja sen jälkeen
06:40 Mitä avoimuus antaa
07:06 Samat bugit, samana päivänä
07:59 Avoimuuden hinta
08:58 Korjattu ei ole asennettu
09:20 Alle tunnissa
10:08 Pidä kaikki ajan tasalla
10:24 Onko avoin lähdekoodi siis turvallisempi?

KUVALÄHTEET
Eric S Raymond portrait — jerone2, derivative work by Bilby, CC BY-SA 2.0
LinuxCon Europe Linus Torvalds 03 (cropped) — Krd (photo), Von Sprat (crop), CC BY-SA 4.0
Heartbleedin logo — Leena Kurjenniska / Codenomicon, CC0
Wikimedia Commonsin kautta
Lisenssit: creativecommons.org/licenses/by-sa/2.0, creativecommons.org/licenses/by-sa/4.0
```

## français (`fr`)

```
Que devient l'open source quand l'IA peut trouver tous les bugs ?
```

```
948. C'est le nombre de façons distinctes qu'une IA a trouvées pour prendre le contrôle d'un ordinateur Linux de l'intérieur, chacune en partant d'un utilisateur ordinaire qui n'a aucun droit particulier. Le code de Linux est public, et pendant des décennies, c'était l'argument qui expliquait pourquoi il est sûr. Alors, si une machine peut lire du code public et en tirer des exploits fonctionnels à cette échelle, les logiciels devraient-ils finalement garder leur code secret ?

Cette vidéo passe en revue le test d'OpenAI sur le noyau Linux, le mois record de correctifs de sécurité chez Microsoft, le bug Heartbleed resté deux ans dans du code public, ce qu'une IA peut faire d'un correctif Windows sans le code source, pourquoi le noyau Linux considère désormais comme publics les bugs trouvés avec l'IA, et les deux mois entre un correctif Windows et WannaCry.

Sources : OpenAI, "A thousand fewer paths to root" (2026); Anthropic, "N-days" (2026); Linux kernel documentation, security-bugs.rst; Linus Torvalds, Linux 7.1-rc4 announcement (2026); Eric S. Raymond, The Cathedral and the Bazaar (1999); Phoronix; TechSpot; The Register.

Les sous-titres sont écrits pour cette vidéo, pas générés automatiquement. Une piste audio en anglais américain est disponible en seconde piste.

CHAPITRES
00:00 948 façons d'entrer
00:42 Du code public
01:02 Le code privé de Microsoft
01:44 Comment fonctionne la machine
02:53 Envoyés pour ouvrir une porte
03:40 Une limite importante
04:17 Avec suffisamment d'yeux
04:36 Heartbleed
05:27 Le cacher, ça aide ?
05:43 Avant et après un correctif
06:40 Ce que l'ouverture t'apporte
07:06 Les mêmes bugs, le même jour
07:59 Le prix de l'ouverture
08:58 Corrigé ne veut pas dire installé
09:20 En moins d'une heure
10:08 Garde tout à jour
10:24 Alors, l'open source est-il plus sûr ?

CRÉDITS DES IMAGES
Eric S Raymond portrait — jerone2, derivative work by Bilby, CC BY-SA 2.0
LinuxCon Europe Linus Torvalds 03 (cropped) — Krd (photo), Von Sprat (crop), CC BY-SA 4.0
Logo de Heartbleed — Leena Kurjenniska / Codenomicon, CC0
via Wikimedia Commons
Licences : creativecommons.org/licenses/by-sa/2.0, creativecommons.org/licenses/by-sa/4.0
```

## Bahasa Indonesia (`id`)

```
Apa yang terjadi pada open source jika AI bisa menemukan semua bug?
```

```
948. Sebanyak itulah cara berbeda yang ditemukan sebuah AI untuk mengambil alih komputer Linux dari dalam, dan setiap cara dimulai dari pengguna biasa yang tidak punya hak khusus apa pun. Kode Linux itu publik, dan selama puluhan tahun, itulah argumen kenapa Linux aman. Jadi, kalau mesin bisa membaca kode publik dan mengubahnya menjadi eksploit yang berfungsi dalam skala ini, haruskah perangkat lunak merahasiakan kodenya saja?

Video ini membahas uji coba OpenAI pada kernel Linux, bulan rekor perbaikan keamanan Microsoft, bug Heartbleed yang dua tahun berada di kode publik, apa yang bisa dilakukan AI dengan patch Windows tanpa kode sumber, kenapa kernel Linux kini menganggap bug yang ditemukan dengan AI sebagai publik, dan dua bulan antara perbaikan Windows dan WannaCry.

Sumber: OpenAI, "A thousand fewer paths to root" (2026); Anthropic, "N-days" (2026); Linux kernel documentation, security-bugs.rst; Linus Torvalds, Linux 7.1-rc4 announcement (2026); Eric S. Raymond, The Cathedral and the Bazaar (1999); Phoronix; TechSpot; The Register.

Subtitel ditulis khusus untuk video ini, bukan dibuat secara otomatis. Tersedia juga trek audio kedua dalam bahasa Inggris Amerika.

BAB
00:00 948 cara masuk
00:42 Kode publik
01:02 Kode privat Microsoft
01:44 Cara kerja mesin ini
02:53 Disuruh membuka satu pintu
03:40 Satu batasan penting
04:17 Dengan cukup banyak mata
04:36 Heartbleed
05:27 Apakah menyembunyikannya membantu?
05:43 Sebelum dan sesudah patch
06:40 Apa yang kamu dapat dari keterbukaan
07:06 Bug yang sama, pada hari yang sama
07:59 Harga keterbukaan
08:58 Diperbaiki tidak sama dengan terpasang
09:20 Kurang dari satu jam
10:08 Selalu perbarui semuanya
10:24 Jadi, apakah open source lebih aman?

KREDIT GAMBAR
Eric S Raymond portrait — jerone2, derivative work by Bilby, CC BY-SA 2.0
LinuxCon Europe Linus Torvalds 03 (cropped) — Krd (photo), Von Sprat (crop), CC BY-SA 4.0
Logo Heartbleed — Leena Kurjenniska / Codenomicon, CC0
melalui Wikimedia Commons
Lisensi: creativecommons.org/licenses/by-sa/2.0, creativecommons.org/licenses/by-sa/4.0
```

## italiano (`it`)

```
Che fine fa l'open source se l'IA può trovare ogni bug?
```

```
948. Sono i modi diversi che un'IA ha trovato per prendere il controllo di un computer Linux dall'interno, e ognuno parte da un utente qualunque senza alcun privilegio particolare. Il codice di Linux è pubblico, e per decenni questo è stato l'argomento per sostenere che è sicuro. Quindi, se una macchina sa leggere codice pubblico e trasformarlo in exploit funzionanti su questa scala, il software dovrebbe tenere segreto il proprio codice, dopotutto?

Questo video racconta il test di OpenAI sul kernel Linux, il mese record di correzioni di sicurezza di Microsoft, il bug Heartbleed rimasto due anni nel codice pubblico, che cosa può fare un'IA con una patch di Windows e senza codice sorgente, perché il kernel Linux ora considera pubblici i bug trovati con l'IA, e i due mesi tra una correzione di Windows e WannaCry.

Fonti: OpenAI, "A thousand fewer paths to root" (2026); Anthropic, "N-days" (2026); Linux kernel documentation, security-bugs.rst; Linus Torvalds, Linux 7.1-rc4 announcement (2026); Eric S. Raymond, The Cathedral and the Bazaar (1999); Phoronix; TechSpot; The Register.

I sottotitoli sono scritti per questo video, non generati automaticamente. Come seconda traccia audio è disponibile l’inglese americano.

CAPITOLI
00:00 948 modi per entrare
00:42 Codice pubblico
01:02 Il codice privato di Microsoft
01:44 Come funziona la macchina
02:53 Mandati ad aprire una porta
03:40 Un limite importante
04:17 Con abbastanza occhi
04:36 Heartbleed
05:27 Nasconderlo serve?
05:43 Prima e dopo una patch
06:40 Che cosa ti dà il codice aperto
07:06 Gli stessi bug, lo stesso giorno
07:59 Il costo dell'apertura
08:58 Corretto non vuol dire installato
09:20 In meno di un'ora
10:08 Tieni tutto aggiornato
10:24 Allora, l'open source è più sicuro?

CREDITI DELLE IMMAGINI
Eric S Raymond portrait — jerone2, derivative work by Bilby, CC BY-SA 2.0
LinuxCon Europe Linus Torvalds 03 (cropped) — Krd (photo), Von Sprat (crop), CC BY-SA 4.0
Logo di Heartbleed — Leena Kurjenniska / Codenomicon, CC0
tramite Wikimedia Commons
Licenze: creativecommons.org/licenses/by-sa/2.0, creativecommons.org/licenses/by-sa/4.0
```

## Deutsch (`de`)

```
Was passiert mit Open Source, wenn KI jeden Fehler finden kann?
```

```
948. So viele verschiedene Wege hat eine KI gefunden, einen Linux-Rechner von innen zu übernehmen, und jeder beginnt bei einem gewöhnlichen Nutzer ohne besondere Rechte. Der Code von Linux ist öffentlich, und jahrzehntelang war genau das das Argument dafür, dass Linux sicher ist. Wenn also eine Maschine öffentlichen Code lesen und daraus in diesem Maßstab funktionierende Exploits machen kann, sollte Software ihren Code dann doch geheim halten?

Dieses Video geht durch OpenAIs Testlauf am Linux-Kernel, Microsofts Rekordmonat an Sicherheitskorrekturen, den Heartbleed-Fehler, der zwei Jahre in öffentlichem Code lag, was eine KI mit einem Windows-Patch und ohne Quellcode anfangen kann, warum der Linux-Kernel mit KI gefundene Fehler jetzt als öffentlich behandelt, und die zwei Monate zwischen einer Windows-Korrektur und WannaCry.

Quellen: OpenAI, "A thousand fewer paths to root" (2026); Anthropic, "N-days" (2026); Linux kernel documentation, security-bugs.rst; Linus Torvalds, Linux 7.1-rc4 announcement (2026); Eric S. Raymond, The Cathedral and the Bazaar (1999); Phoronix; TechSpot; The Register.

Die Untertitel wurden für dieses Video geschrieben, nicht automatisch erzeugt. Als zweite Tonspur steht amerikanisches Englisch bereit.

KAPITEL
00:00 948 Wege hinein
00:42 Öffentlicher Code
01:02 Microsofts privater Code
01:44 Wie die Maschine arbeitet
02:53 Geschickt, um eine Tür zu öffnen
03:40 Eine wichtige Grenze
04:17 Mit genug Augen
04:36 Heartbleed
05:27 Hilft Verstecken?
05:43 Vor und nach einem Patch
06:40 Was Offenheit dir bringt
07:06 Dieselben Fehler, am selben Tag
07:59 Der Preis der Offenheit
08:58 Behoben ist nicht installiert
09:20 In unter einer Stunde
10:08 Halte alles aktuell
10:24 Ist Open Source also sicherer?

BILDNACHWEISE
Eric S Raymond portrait — jerone2, derivative work by Bilby, CC BY-SA 2.0
LinuxCon Europe Linus Torvalds 03 (cropped) — Krd (photo), Von Sprat (crop), CC BY-SA 4.0
Heartbleed-Logo — Leena Kurjenniska / Codenomicon, CC0
über Wikimedia Commons
Lizenzen: creativecommons.org/licenses/by-sa/2.0, creativecommons.org/licenses/by-sa/4.0
```

## polski (`pl`)

```
Co się stanie z open source, gdy AI znajdzie każdy błąd?
```

```
948. Tyle różnych sposobów znalazła sztuczna inteligencja, żeby od środka przejąć komputer z Linuksem, a każdy zaczyna się od zwykłego użytkownika bez żadnych specjalnych uprawnień. Kod Linuksa jest publiczny i przez dziesięciolecia był to argument za tym, że jest bezpieczny. Skoro więc maszyna potrafi czytać publiczny kod i zamieniać go w działające exploity na taką skalę, to czy oprogramowanie nie powinno jednak trzymać kodu w tajemnicy?

Ten film opowiada o teście OpenAI na jądrze Linuksa, rekordowym miesiącu poprawek bezpieczeństwa w Microsofcie, błędzie Heartbleed, który przez dwa lata tkwił w publicznym kodzie, o tym, co AI potrafi zrobić z łatką Windowsa bez kodu źródłowego, dlaczego jądro Linuksa traktuje teraz błędy znalezione z pomocą AI jak publiczne, i o dwóch miesiącach między poprawką Windowsa a WannaCry.

Źródła: OpenAI, "A thousand fewer paths to root" (2026); Anthropic, "N-days" (2026); Linux kernel documentation, security-bugs.rst; Linus Torvalds, Linux 7.1-rc4 announcement (2026); Eric S. Raymond, The Cathedral and the Bazaar (1999); Phoronix; TechSpot; The Register.

Napisy są pisane do tego filmu, nie generowane automatycznie. Jako druga ścieżka dźwiękowa dostępny jest angielski amerykański.

ROZDZIAŁY
00:00 948 sposobów, żeby wejść
00:42 Publiczny kod
01:02 Prywatny kod Microsoftu
01:44 Jak działa ta maszyna
02:53 Wysłane, żeby otworzyć jedne drzwi
03:40 Ważne ograniczenie
04:17 Przy dostatecznie wielu oczach
04:36 Heartbleed
05:27 Czy ukrycie pomaga?
05:43 Przed łatką i po niej
06:40 Co daje ci otwartość
07:06 Te same błędy, tego samego dnia
07:59 Cena otwartości
08:58 Naprawione to nie zainstalowane
09:20 W niecałą godzinę
10:08 Aktualizuj wszystko
10:24 Czy open source jest więc bezpieczniejszy?

ŹRÓDŁA ZDJĘĆ
Eric S Raymond portrait — jerone2, derivative work by Bilby, CC BY-SA 2.0
LinuxCon Europe Linus Torvalds 03 (cropped) — Krd (photo), Von Sprat (crop), CC BY-SA 4.0
Logo Heartbleed — Leena Kurjenniska / Codenomicon, CC0
przez Wikimedia Commons
Licencje: creativecommons.org/licenses/by-sa/2.0, creativecommons.org/licenses/by-sa/4.0
```

## português (Brasil) (`pt-BR`)

```
O que acontece com o código aberto quando a IA pode encontrar todos os bugs?
```

```
948. Foi o número de formas diferentes que uma IA encontrou de assumir o controle de um computador Linux por dentro, e cada uma começa com um usuário comum sem nenhum privilégio especial. O código do Linux é público, e durante décadas esse foi o argumento para dizer que ele é seguro. Então, se uma máquina consegue ler código público e transformá-lo em exploits funcionais nessa escala, o software deveria manter seu código em segredo, afinal?

Este vídeo passa pelo teste da OpenAI no kernel do Linux, pelo mês recorde de correções de segurança da Microsoft, pelo bug Heartbleed, que ficou dois anos em código público, pelo que uma IA consegue fazer com um patch do Windows e sem código-fonte, por que o kernel do Linux agora trata como públicos os bugs encontrados com IA, e pelos dois meses entre uma correção do Windows e o WannaCry.

Fontes: OpenAI, "A thousand fewer paths to root" (2026); Anthropic, "N-days" (2026); Linux kernel documentation, security-bugs.rst; Linus Torvalds, Linux 7.1-rc4 announcement (2026); Eric S. Raymond, The Cathedral and the Bazaar (1999); Phoronix; TechSpot; The Register.

As legendas foram escritas para este vídeo, não geradas automaticamente. Como segunda faixa de áudio está disponível o inglês americano.

CAPÍTULOS
00:00 948 formas de entrar
00:42 Código público
01:02 O código privado da Microsoft
01:44 Como a máquina funciona
02:53 Enviados para abrir uma porta
03:40 Um limite importante
04:17 Com olhos suficientes
04:36 Heartbleed
05:27 Esconder ajuda?
05:43 Antes e depois de um patch
06:40 O que ser aberto traz para você
07:06 Os mesmos bugs, no mesmo dia
07:59 O custo da abertura
08:58 Corrigido não é instalado
09:20 Em menos de uma hora
10:08 Mantenha tudo atualizado
10:24 Então, o código aberto é mais seguro?

CRÉDITOS DAS IMAGENS
Eric S Raymond portrait — jerone2, derivative work by Bilby, CC BY-SA 2.0
LinuxCon Europe Linus Torvalds 03 (cropped) — Krd (photo), Von Sprat (crop), CC BY-SA 4.0
Logo do Heartbleed — Leena Kurjenniska / Codenomicon, CC0
via Wikimedia Commons
Licenças: creativecommons.org/licenses/by-sa/2.0, creativecommons.org/licenses/by-sa/4.0
```

## Türkçe (`tr`)

```
Yapay zekâ her hatayı bulabildiğinde açık kaynağa ne olur?
```

```
948. Bir yapay zekânın bir Linux bilgisayarı içeriden ele geçirmek için bulduğu farklı yolların sayısı bu, ve her biri hiçbir özel yetkisi olmayan sıradan bir kullanıcıyla başlıyor. Linux'un kodu herkese açık ve onlarca yıl boyunca bu, neden güvenli olduğunun gerekçesiydi. O hâlde bir makine açık kodu okuyup onu bu ölçekte çalışan istismar kodlarına çevirebiliyorsa, yazılımlar kodlarını gizli mi tutmalı?

Bu video, OpenAI'ın Linux çekirdeği üzerindeki test çalışmasını, Microsoft'un güvenlik düzeltmelerinde rekor kırdığı ayı, iki yıl boyunca açık kodda kalan Heartbleed hatasını, bir yapay zekânın kaynak kodu olmadan bir Windows yamasıyla neler yapabildiğini, Linux çekirdeğinin yapay zekâyla bulunan hataları neden artık kamuya açık saydığını ve bir Windows düzeltmesiyle WannaCry arasındaki iki ayı ele alıyor.

Kaynaklar: OpenAI, "A thousand fewer paths to root" (2026); Anthropic, "N-days" (2026); Linux kernel documentation, security-bugs.rst; Linus Torvalds, Linux 7.1-rc4 announcement (2026); Eric S. Raymond, The Cathedral and the Bazaar (1999); Phoronix; TechSpot; The Register.

Altyazılar bu video için yazıldı, otomatik olarak oluşturulmadı. İkinci ses parçası olarak Amerikan İngilizcesi de mevcut.

BÖLÜMLER
00:00 İçeri girmenin 948 yolu
00:42 Açık kod
01:02 Microsoft'un gizli kodu
01:44 Makine nasıl çalışıyor
02:53 Bir kapıyı açmaya gönderildiler
03:40 Önemli bir sınır
04:17 Yeterince göz varsa
04:36 Heartbleed
05:27 Gizlemek işe yarar mı?
05:43 Yamadan önce ve sonra
06:40 Açık olmak sana ne kazandırır
07:06 Aynı hatalar, aynı gün
07:59 Açıklığın bedeli
08:58 Düzeltilmiş, yüklenmiş demek değil
09:20 Bir saatten kısa sürede
10:08 Her şeyi güncel tut
10:24 Peki açık kaynak daha mı güvenli?

GÖRSEL KAYNAKLARI
Eric S Raymond portrait — jerone2, derivative work by Bilby, CC BY-SA 2.0
LinuxCon Europe Linus Torvalds 03 (cropped) — Krd (photo), Von Sprat (crop), CC BY-SA 4.0
Heartbleed logosu — Leena Kurjenniska / Codenomicon, CC0
Wikimedia Commons aracılığıyla
Lisanslar: creativecommons.org/licenses/by-sa/2.0, creativecommons.org/licenses/by-sa/4.0
```

## українська (`uk`)

```
Що буде з відкритим кодом, коли ШІ зможе знайти кожну помилку?
```

```
948. Стільки різних способів знайшов штучний інтелект, щоб зсередини захопити комп'ютер з Linux, і кожен починається зі звичайного користувача без жодних особливих прав. Код Linux відкритий, і десятиліттями це був аргумент на користь того, що він безпечний. Тож якщо машина може читати відкритий код і перетворювати його на робочі експлойти в такому масштабі, може, програмам усе ж варто тримати код у секреті?

У цьому відео — тестовий запуск OpenAI на ядрі Linux, рекордний місяць виправлень безпеки в Microsoft, помилка Heartbleed, яка два роки пролежала у відкритому коді, що ШІ може зробити з патчем Windows без вихідного коду, чому ядро Linux тепер вважає публічними помилки, знайдені за допомогою ШІ, і два місяці між виправленням Windows та WannaCry.

Джерела: OpenAI, "A thousand fewer paths to root" (2026); Anthropic, "N-days" (2026); Linux kernel documentation, security-bugs.rst; Linus Torvalds, Linux 7.1-rc4 announcement (2026); Eric S. Raymond, The Cathedral and the Bazaar (1999); Phoronix; TechSpot; The Register.

Субтитри написані для цього відео, а не згенеровані автоматично. Також доступна друга звукова доріжка — американською англійською.

РОЗДІЛИ
00:00 948 шляхів усередину
00:42 Відкритий код
01:02 Закритий код Microsoft
01:44 Як працює ця машина
02:53 Їх послали відчинити одні двері
03:40 Важливе обмеження
04:17 Якщо очей достатньо
04:36 Heartbleed
05:27 Чи допомагає приховування?
05:43 До і після патча
06:40 Що дає тобі відкритість
07:06 Ті самі помилки, того самого дня
07:59 Ціна відкритості
08:58 Виправлено — не означає встановлено
09:20 Менш ніж за годину
10:08 Оновлюй усе вчасно
10:24 Тож чи відкритий код безпечніший?

ДЖЕРЕЛА ЗОБРАЖЕНЬ
Eric S Raymond portrait — jerone2, derivative work by Bilby, CC BY-SA 2.0
LinuxCon Europe Linus Torvalds 03 (cropped) — Krd (photo), Von Sprat (crop), CC BY-SA 4.0
Логотип Heartbleed — Leena Kurjenniska / Codenomicon, CC0
через Wikimedia Commons
Ліцензії: creativecommons.org/licenses/by-sa/2.0, creativecommons.org/licenses/by-sa/4.0
```

## Tiếng Việt (`vi`)

```
Mã nguồn mở sẽ ra sao khi AI có thể tìm ra mọi lỗi?
```

```
948. Đó là số cách khác nhau mà một AI đã tìm ra để chiếm quyền một máy tính Linux từ bên trong, và mỗi cách đều bắt đầu từ một người dùng bình thường không có quyền đặc biệt nào. Mã nguồn Linux là công khai, và suốt nhiều thập kỷ, người ta dựa vào đó để nói rằng Linux an toàn. Vậy nếu một cỗ máy có thể đọc mã công khai và biến nó thành mã khai thác hoạt động được ở quy mô này, thì rốt cuộc phần mềm có nên giữ bí mật mã của mình không?

Video này đi qua đợt thử nghiệm của OpenAI trên nhân Linux, tháng sửa lỗi bảo mật kỷ lục của Microsoft, lỗi Heartbleed đã nằm trong mã công khai suốt hai năm, những gì AI làm được với một bản vá Windows mà không có mã nguồn, lý do nhân Linux giờ coi các lỗi tìm được bằng AI là công khai, và hai tháng giữa một bản sửa Windows và WannaCry.

Nguồn: OpenAI, "A thousand fewer paths to root" (2026); Anthropic, "N-days" (2026); Linux kernel documentation, security-bugs.rst; Linus Torvalds, Linux 7.1-rc4 announcement (2026); Eric S. Raymond, The Cathedral and the Bazaar (1999); Phoronix; TechSpot; The Register.

Phụ đề được viết riêng cho video này, không phải tạo tự động. Có thể chọn tiếng Anh Mỹ ở bản âm thanh thứ hai.

CHƯƠNG
00:00 948 cách để vào
00:42 Mã công khai
01:02 Mã nguồn đóng của Microsoft
01:44 Cỗ máy hoạt động thế nào
02:53 Được cử đi mở một cánh cửa
03:40 Một giới hạn quan trọng
04:17 Có đủ nhiều con mắt
04:36 Heartbleed
05:27 Giấu đi có giúp được gì không?
05:43 Trước và sau một bản vá
06:40 Sự cởi mở đem lại cho bạn điều gì
07:06 Cùng những lỗi ấy, trong cùng một ngày
07:59 Cái giá của sự cởi mở
08:58 Đã sửa không có nghĩa là đã cài
09:20 Chưa đầy một giờ
10:08 Hãy cập nhật mọi thứ
10:24 Vậy mã nguồn mở có an toàn hơn không?

NGUỒN HÌNH ẢNH
Eric S Raymond portrait — jerone2, derivative work by Bilby, CC BY-SA 2.0
LinuxCon Europe Linus Torvalds 03 (cropped) — Krd (photo), Von Sprat (crop), CC BY-SA 4.0
Logo Heartbleed — Leena Kurjenniska / Codenomicon, CC0
qua Wikimedia Commons
Giấy phép: creativecommons.org/licenses/by-sa/2.0, creativecommons.org/licenses/by-sa/4.0
```

## čeština (`cs`)

```
Co se stane s open source, když AI dokáže najít každou chybu?
```

```
948. Tolik různých způsobů našla AI, jak zevnitř ovládnout počítač s Linuxem, a každý začíná u obyčejného uživatele bez zvláštních práv. Kód Linuxu je veřejný a celá desetiletí to byl argument, proč je bezpečný. Když tedy stroj umí číst veřejný kód a dělat z něj v takovém měřítku funkční exploity, neměl by software svůj kód nakonec přece jen tajit?

Video projde test OpenAI na jádru Linuxu, rekordní měsíc bezpečnostních oprav u Microsoftu, chybu Heartbleed, která dva roky ležela ve veřejném kódu, co AI dokáže s opravou Windows bez zdrojového kódu, proč jádro Linuxu teď bere chyby nalezené pomocí AI jako veřejné, a dva měsíce mezi opravou Windows a WannaCry.

Zdroje: OpenAI, "A thousand fewer paths to root" (2026); Anthropic, "N-days" (2026); Linux kernel documentation, security-bugs.rst; Linus Torvalds, Linux 7.1-rc4 announcement (2026); Eric S. Raymond, The Cathedral and the Bazaar (1999); Phoronix; TechSpot; The Register.

Titulky jsou psané pro tohle video, ne strojový přepis. Jako druhá zvuková stopa je k dispozici americká angličtina.

KAPITOLY
00:00 948 cest dovnitř
00:42 Veřejný kód
01:02 Soukromý kód Microsoftu
01:44 Jak ten stroj funguje
02:53 Poslaní otevřít jedny dveře
03:40 Důležitá mez
04:17 Dost očí
04:36 Heartbleed
05:27 Pomáhá to schovat?
05:43 Před opravou a po ní
06:40 Co ti dává otevřenost
07:06 Stejné chyby, týž den
07:59 Účet za otevřenost
08:58 Opraveno neznamená nainstalováno
09:20 Za necelou hodinu
10:08 Aktualizuj všechno
10:24 Je tedy open source bezpečnější?

ZDROJE OBRÁZKŮ
Eric S Raymond portrait — jerone2, derivative work by Bilby, CC BY-SA 2.0
LinuxCon Europe Linus Torvalds 03 (cropped) — Krd (photo), Von Sprat (crop), CC BY-SA 4.0
Logo Heartbleed — Leena Kurjenniska / Codenomicon, CC0
přes Wikimedia Commons
Licence: creativecommons.org/licenses/by-sa/2.0, creativecommons.org/licenses/by-sa/4.0
```

## español (`es`)

```
¿Qué pasa con el código abierto cuando la IA puede encontrar todos los errores?
```

```
948. Tantas formas distintas encontró una IA de tomar el control de un ordenador Linux desde dentro, y cada una empieza con un usuario corriente sin ningún permiso especial. El código de Linux es público, y durante décadas ese fue el argumento para afirmar que era seguro. Así que, si una máquina puede leer código público y convertirlo en exploits funcionales a esta escala, ¿debería el software mantener su código en secreto?

Este vídeo repasa la prueba de OpenAI con el kernel de Linux, el mes récord de correcciones de seguridad de Microsoft, el fallo Heartbleed, que pasó dos años en código público, lo que una IA puede hacer con un parche de Windows y sin código fuente, por qué el kernel de Linux ahora trata como públicos los errores encontrados con IA, y los dos meses entre una corrección de Windows y WannaCry.

Fuentes: OpenAI, "A thousand fewer paths to root" (2026); Anthropic, "N-days" (2026); Linux kernel documentation, security-bugs.rst; Linus Torvalds, Linux 7.1-rc4 announcement (2026); Eric S. Raymond, The Cathedral and the Bazaar (1999); Phoronix; TechSpot; The Register.

Los subtítulos están escritos para este vídeo, no generados automáticamente. Como segunda pista de audio está disponible el inglés americano.

CAPÍTULOS
00:00 948 formas de entrar
00:42 Código público
01:02 El código privado de Microsoft
01:44 Cómo funciona la máquina
02:53 Enviados a abrir una puerta
03:40 Un límite importante
04:17 Con suficientes ojos
04:36 Heartbleed
05:27 ¿Sirve de algo esconderlo?
05:43 Antes y después de un parche
06:40 Lo que te aporta ser abierto
07:06 Los mismos errores, el mismo día
07:59 La factura de la apertura
08:58 Corregido no es instalado
09:20 En menos de una hora
10:08 Mantén todo actualizado
10:24 Entonces, ¿es más seguro el código abierto?

CRÉDITOS DE LAS IMÁGENES
Eric S Raymond portrait — jerone2, derivative work by Bilby, CC BY-SA 2.0
LinuxCon Europe Linus Torvalds 03 (cropped) — Krd (photo), Von Sprat (crop), CC BY-SA 4.0
Logo de Heartbleed — Leena Kurjenniska / Codenomicon, CC0
vía Wikimedia Commons
Licencias: creativecommons.org/licenses/by-sa/2.0, creativecommons.org/licenses/by-sa/4.0
```

## svenska (`sv`)

```
Vad händer med öppen källkod när AI kan hitta varenda bugg?
```

```
948. Så många olika sätt hittade en AI att ta över en Linuxdator inifrån, och vart och ett börjar med en vanlig användare utan några särskilda rättigheter. Linux kod är offentlig, och i årtionden var det argumentet för att den är säker. Så om en maskin kan läsa offentlig kod och göra om den till fungerande exploits i den här skalan, borde mjukvara ändå hålla sin kod hemlig?

Videon går igenom OpenAI:s testkörning på Linuxkärnan, Microsofts rekordmånad av säkerhetsrättelser, Heartbleed-buggen som låg två år i offentlig kod, vad en AI kan göra med en Windows-patch utan källkod, varför Linuxkärnan nu behandlar buggar som hittats med AI som offentliga, och de två månaderna mellan en Windows-rättelse och WannaCry.

Källor: OpenAI, "A thousand fewer paths to root" (2026); Anthropic, "N-days" (2026); Linux kernel documentation, security-bugs.rst; Linus Torvalds, Linux 7.1-rc4 announcement (2026); Eric S. Raymond, The Cathedral and the Bazaar (1999); Phoronix; TechSpot; The Register.

Undertexterna är skrivna för den här videon, inte automatgenererade. Som andra ljudspår finns amerikansk engelska.

KAPITEL
00:00 948 vägar in
00:42 Offentlig kod
01:02 Microsofts privata kod
01:44 Hur maskinen fungerar
02:53 Skickade för att öppna en dörr
03:40 En viktig begränsning
04:17 Med tillräckligt många ögon
04:36 Heartbleed
05:27 Hjälper det att gömma den?
05:43 Före och efter en patch
06:40 Vad öppenhet ger dig
07:06 Samma buggar, samma dag
07:59 Priset för öppenhet
08:58 Rättat är inte installerat
09:20 På under en timme
10:08 Håll allt uppdaterat
10:24 Är öppen källkod då säkrare?

BILDKÄLLOR
Eric S Raymond portrait — jerone2, derivative work by Bilby, CC BY-SA 2.0
LinuxCon Europe Linus Torvalds 03 (cropped) — Krd (photo), Von Sprat (crop), CC BY-SA 4.0
Heartbleeds logotyp — Leena Kurjenniska / Codenomicon, CC0
via Wikimedia Commons
Licenser: creativecommons.org/licenses/by-sa/2.0, creativecommons.org/licenses/by-sa/4.0
```
