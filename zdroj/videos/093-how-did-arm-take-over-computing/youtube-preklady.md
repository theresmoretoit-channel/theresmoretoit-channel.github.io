# Lokalizované názvy a popisy — 093

Čte `tools/lokalizace.py` a nahrává přes `videos.update(part="localizations")`.
Anglický titul a popis jsou v `youtube.md` a posílají se zpátky beze změny.

**Pořadí sekcí je podle YouTube Studia** (bajtově podle ČESKÉHO názvu jazyka).

**Codex proběhl 2026-10-07**, 21 nálezů, 11 zapracováno (fi, fr kapitola 05:17 „prodej návrhu“; de, pt-BR, uk kapitola 06:35; tr, vi kapitola 00:00; id, tr věta o Intelu; sv „likadana“ → „likartade“; pl „trafił“ → „znalazł się“). Zamítnuto: „efficient wins“ jako podstatné jméno v osmi jazycích (fi, de, pl, pt-BR, uk, vi, cs, sv) — popis cituje větu S67, kterou scénář každého jazyka má s přídavným jménem; cs „od britské firmy na domácí počítače“ (doslova S11 scénáře).

## Co se NEPŘEKLÁDÁ

- vlastní jména a názvy: Acorn, BBC Micro, Archimedes, ARM, ARM1, RISC,
  x86, Apple, Intel, Nokia, Amazon
- atribuce: řádky s autory a licencemi zůstávají beze změny anglicky,
  stejně jako `via Wikimedia Commons` a řádek `Licences: …`; přeložený je
  jen nadpis bloku a věta o public domain / CC0
- časy kapitol na vteřinu
- tagy (YouTube je per-jazyk nemá)

Odstavec o titulcích a americké stopě je doslova z tabulky kanonických znění
v `docs/zverejneni.md`. Titul = první řádek `script.<kód>.md`. Terminologie
podle scénáře daného jazyka (napájení / Stromversorgung / alimentation …
jako v S03; datová centra / Rechenzentren / datacenters / data center …
jako v S09 a S93; domácí počítače / Heimcomputer / ordinateurs familiaux …
jako v S11; ARM v pt-BR a it ženského rodu jako ve scénáři).
Registr podle scénáře: cs ty, de du, fr tu, it tu, es tú, pl ty, uk ти,
tr sen, id kamu, fi sinä, sv du, pt-BR você, vi bạn — popis ale diváka
přímo neoslovuje.

## suomi (`fi`)

```
Miten ARM valtasi tietotekniikan?
```

```
Vuonna 1985 ensimmäinen ARM-suoritin käynnistettiin ensimmäistä kertaa, ja se pysyi käynnissä, vaikka sen virransyöttöä ei ollut kytketty. Neljäkymmentä vuotta myöhemmin sen jälkeläisiä on lähes jokaisessa älypuhelimessa, Applen tietokoneissa ja joissakin maailman suurimmista datakeskuksista.

Tavallinen selitys on, että ARM on yksinkertainen ja energiatehokas, ja energiatehokas voittaa. Mutta nykyaikainen ARM-ydin on kaikkea muuta kuin yksinkertainen, ja 1990-luvun puolivälistä lähtien Intelin sirut ovat näyttäneet sisältä yllättävän samanlaisilta. Miten siis brittiläisen kotitietokoneyhtiön siru päätyi kaikkialle?

Tekstitykset on kirjoitettu tätä videota varten, ei luotu automaattisesti. Toisena ääniraitana on amerikanenglanti.

LUVUT
00:00 Siru, joka toimi ilman virtaa
01:10 Acorn, 1983
02:11 RISC-idea
03:34 ARM1
04:09 Archimedes
04:46 Apple ja uusi yhtiö
05:17 Suunnitelman myyminen
06:00 Puhelimet
06:35 Onko yksinkertaisuus vastaus?
07:13 Kaksi eri asiaa
07:36 Mitä x86:lle tapahtui
08:34 Takaisin Appleen
09:07 Datakeskukset
09:30 Mitä he oikeasti rakensivat

KUVALÄHTEET
Acorn Archimedes A310 with mouse and keyboard — mikkohoo, CC BY-SA 4.0
Apple Newton MessagePad 100 — Felix Winkelnkemper, CC BY-SA 4.0
Nokia 6110 blue-92111 — Raimond Spekking, CC BY-SA 4.0
via Wikimedia Commons
Kaikki muut arkistokuvat ovat public domainia tai CC0:aa.
Licences: creativecommons.org/licenses/by-sa/4.0
```

## français (`fr`)

```
Comment ARM a-t-il conquis l'informatique ?
```

```
En 1985, le premier processeur ARM a été allumé pour la toute première fois, et il a continué à fonctionner alors que son alimentation n'était pas branchée. Quarante ans plus tard, ses descendants sont dans presque tous les smartphones, dans les ordinateurs d'Apple et dans certains des plus grands datacenters du monde.

L'explication habituelle, c'est qu'ARM est simple et efficace, et que l'efficacité l'emporte. Mais un cœur ARM moderne est tout sauf simple, et depuis le milieu des années 1990, les puces d'Intel lui ressemblent étonnamment à l'intérieur. Alors comment une puce d'une entreprise britannique d'ordinateurs familiaux s'est-elle retrouvée partout ?

Les sous-titres sont écrits pour cette vidéo, pas générés automatiquement. Une piste audio en anglais américain est disponible en seconde piste.

CHAPITRES
00:00 La puce qui tournait sans courant
01:10 Acorn, 1983
02:11 L'idée RISC
03:34 L'ARM1
04:09 L'Archimedes
04:46 Apple et une nouvelle entreprise
05:17 Vendre les plans de la puce
06:00 Les téléphones
06:35 La simplicité, c'est la réponse ?
07:13 Deux choses différentes
07:36 Ce qu'est devenu le x86
08:34 Retour chez Apple
09:07 Les datacenters
09:30 Ce qu'ils ont vraiment construit

CRÉDITS DES IMAGES
Acorn Archimedes A310 with mouse and keyboard — mikkohoo, CC BY-SA 4.0
Apple Newton MessagePad 100 — Felix Winkelnkemper, CC BY-SA 4.0
Nokia 6110 blue-92111 — Raimond Spekking, CC BY-SA 4.0
via Wikimedia Commons
Toutes les autres images d'archives sont dans le domaine public ou sous CC0.
Licences: creativecommons.org/licenses/by-sa/4.0
```

## Bahasa Indonesia (`id`)

```
Bagaimana ARM Menguasai Dunia Komputasi?
```

```
Pada tahun 1985, prosesor ARM pertama dinyalakan untuk pertama kalinya, dan prosesor itu tetap berjalan meskipun catu dayanya tidak tersambung. Empat puluh tahun kemudian, keturunannya ada di hampir setiap smartphone, di komputer-komputer Apple, dan di beberapa pusat data terbesar di dunia.

Penjelasan yang biasa adalah bahwa ARM itu sederhana dan efisien, dan yang efisien menang. Tapi inti ARM modern sama sekali tidak sederhana, dan yang mengejutkan, sejak pertengahan 1990-an bagian dalam chip Intel pun ternyata mirip. Jadi, bagaimana chip dari perusahaan komputer rumahan Inggris bisa ada di mana-mana?

Subtitel ditulis khusus untuk video ini, bukan dibuat secara otomatis. Tersedia juga trek audio kedua dalam bahasa Inggris Amerika.

BAB
00:00 Chip yang berjalan tanpa daya
01:10 Acorn, 1983
02:11 Gagasan RISC
03:34 ARM1
04:09 Archimedes
04:46 Apple dan perusahaan baru
05:17 Menjual desainnya
06:00 Ponsel
06:35 Apakah kesederhanaan jawabannya?
07:13 Dua hal yang berbeda
07:36 Apa yang terjadi pada x86
08:34 Kembali ke Apple
09:07 Pusat data
09:30 Apa yang sebenarnya mereka bangun

KREDIT GAMBAR
Acorn Archimedes A310 with mouse and keyboard — mikkohoo, CC BY-SA 4.0
Apple Newton MessagePad 100 — Felix Winkelnkemper, CC BY-SA 4.0
Nokia 6110 blue-92111 — Raimond Spekking, CC BY-SA 4.0
via Wikimedia Commons
Semua gambar arsip lainnya berada dalam domain publik atau CC0.
Licences: creativecommons.org/licenses/by-sa/4.0
```

## italiano (`it`)

```
Come ha fatto ARM a conquistare l'informatica?
```

```
Nel 1985 il primo processore ARM fu acceso per la primissima volta, e continuò a funzionare anche se la sua alimentazione non era collegata. Quarant'anni dopo, i suoi discendenti sono in quasi tutti gli smartphone, nei computer di Apple e in alcuni dei più grandi data center del mondo.

La spiegazione abituale è che ARM è semplice ed efficiente, e chi è efficiente vince. Ma un core ARM moderno è tutt'altro che semplice, e dalla metà degli anni '90 i chip di Intel, al loro interno, gli somigliano in modo sorprendente. Allora come ha fatto un chip di un'azienda britannica di home computer a finire ovunque?

I sottotitoli sono scritti per questo video, non generati automaticamente. Come seconda traccia audio è disponibile l’inglese americano.

CAPITOLI
00:00 Il chip che funzionava senza corrente
01:10 Acorn, 1983
02:11 L'idea RISC
03:34 L'ARM1
04:09 L'Archimedes
04:46 Apple e una nuova azienda
05:17 Vendere il progetto
06:00 I telefoni
06:35 La semplicità è la risposta?
07:13 Due cose diverse
07:36 Che fine ha fatto l'x86
08:34 Ritorno ad Apple
09:07 I data center
09:30 Che cosa hanno costruito davvero

CREDITI DELLE IMMAGINI
Acorn Archimedes A310 with mouse and keyboard — mikkohoo, CC BY-SA 4.0
Apple Newton MessagePad 100 — Felix Winkelnkemper, CC BY-SA 4.0
Nokia 6110 blue-92111 — Raimond Spekking, CC BY-SA 4.0
via Wikimedia Commons
Tutte le altre immagini d'archivio sono di pubblico dominio o CC0.
Licences: creativecommons.org/licenses/by-sa/4.0
```

## Deutsch (`de`)

```
Wie hat ARM die Computerwelt erobert?
```

```
1985 wurde der erste ARM-Prozessor zum allerersten Mal eingeschaltet – und er lief weiter, obwohl seine Stromversorgung gar nicht angeschlossen war. Vierzig Jahre später stecken seine Nachfahren in fast jedem Smartphone, in Apples Computern und in einigen der größten Rechenzentren der Welt.

Die übliche Erklärung lautet: ARM ist einfach und effizient, und effizient gewinnt. Doch ein moderner ARM-Kern ist alles andere als einfach, und seit Mitte der 1990er-Jahre sehen Intels Chips innen überraschend ähnlich aus. Wie also ist ein Chip einer britischen Heimcomputerfirma überall gelandet?

Die Untertitel wurden für dieses Video geschrieben, nicht automatisch erzeugt. Als zweite Tonspur steht amerikanisches Englisch bereit.

KAPITEL
00:00 Der Chip, der ohne Strom lief
01:10 Acorn, 1983
02:11 Die RISC-Idee
03:34 Der ARM1
04:09 Der Archimedes
04:46 Apple und eine neue Firma
05:17 Das Design verkaufen
06:00 Handys
06:35 Ist Einfachheit die Antwort?
07:13 Zwei verschiedene Dinge
07:36 Was aus x86 wurde
08:34 Zurück zu Apple
09:07 Rechenzentren
09:30 Was sie wirklich gebaut haben

BILDNACHWEISE
Acorn Archimedes A310 with mouse and keyboard — mikkohoo, CC BY-SA 4.0
Apple Newton MessagePad 100 — Felix Winkelnkemper, CC BY-SA 4.0
Nokia 6110 blue-92111 — Raimond Spekking, CC BY-SA 4.0
via Wikimedia Commons
Alle anderen Archivbilder sind gemeinfrei oder CC0.
Licences: creativecommons.org/licenses/by-sa/4.0
```

## polski (`pl`)

```
Jak ARM podbił świat komputerów?
```

```
W 1985 roku pierwszy procesor ARM został włączony po raz pierwszy i działał dalej, choć jego zasilanie nie było podłączone. Czterdzieści lat później jego potomkowie są w prawie każdym smartfonie, w komputerach Apple i w niektórych z największych centrów danych na świecie.

Zwykłe wyjaśnienie brzmi: ARM jest prosty i efektywny, a efektywny wygrywa. Tyle że nowoczesny rdzeń ARM wcale nie jest prosty, a od połowy lat 90. układy Intela wyglądają w środku zaskakująco podobnie. Jak więc układ z brytyjskiej firmy od komputerów domowych znalazł się wszędzie?

Napisy są pisane do tego filmu, nie generowane automatycznie. Jako druga ścieżka dźwiękowa dostępny jest angielski amerykański.

ROZDZIAŁY
00:00 Układ, który działał bez zasilania
01:10 Acorn, 1983
02:11 Idea RISC
03:34 ARM1
04:09 Archimedes
04:46 Apple i nowa firma
05:17 Sprzedaż projektu
06:00 Telefony
06:35 Czy prostota to odpowiedź?
07:13 Dwie różne rzeczy
07:36 Co się stało z x86
08:34 Powrót do Apple
09:07 Centra danych
09:30 Co naprawdę zbudowali

ŹRÓDŁA ZDJĘĆ
Acorn Archimedes A310 with mouse and keyboard — mikkohoo, CC BY-SA 4.0
Apple Newton MessagePad 100 — Felix Winkelnkemper, CC BY-SA 4.0
Nokia 6110 blue-92111 — Raimond Spekking, CC BY-SA 4.0
via Wikimedia Commons
Wszystkie pozostałe zdjęcia archiwalne są w domenie publicznej lub na licencji CC0.
Licences: creativecommons.org/licenses/by-sa/4.0
```

## português (Brasil) (`pt-BR`)

```
Como a ARM dominou a computação?
```

```
Em 1985, o primeiro processador ARM foi ligado pela primeiríssima vez, e continuou funcionando mesmo com a alimentação desconectada. Quarenta anos depois, seus descendentes estão em quase todo smartphone, nos computadores da Apple e em alguns dos maiores data centers do mundo.

A explicação de sempre é que o ARM é simples e eficiente, e o eficiente vence. Mas um núcleo ARM moderno é tudo menos simples, e desde meados dos anos 90 os chips da Intel são surpreendentemente parecidos por dentro. Então, como um chip de uma empresa britânica de computadores domésticos foi parar em todo lugar?

As legendas foram escritas para este vídeo, não geradas automaticamente. Como segunda faixa de áudio está disponível o inglês americano.

CAPÍTULOS
00:00 O chip que funcionava sem energia
01:10 Acorn, 1983
02:11 A ideia RISC
03:34 O ARM1
04:09 O Archimedes
04:46 A Apple e uma nova empresa
05:17 Vendendo o projeto
06:00 Celulares
06:35 A simplicidade é a resposta?
07:13 Duas coisas diferentes
07:36 O que aconteceu com o x86
08:34 De volta à Apple
09:07 Data centers
09:30 O que eles realmente construíram

CRÉDITOS DAS IMAGENS
Acorn Archimedes A310 with mouse and keyboard — mikkohoo, CC BY-SA 4.0
Apple Newton MessagePad 100 — Felix Winkelnkemper, CC BY-SA 4.0
Nokia 6110 blue-92111 — Raimond Spekking, CC BY-SA 4.0
via Wikimedia Commons
Todas as outras imagens de arquivo estão em domínio público ou CC0.
Licences: creativecommons.org/licenses/by-sa/4.0
```

## Türkçe (`tr`)

```
ARM bilgisayar dünyasını nasıl ele geçirdi?
```

```
1985'te ilk ARM işlemcisi ilk kez çalıştırıldı ve güç kaynağı bağlı olmadığı hâlde çalışmaya devam etti. Kırk yıl sonra onun torunları neredeyse her akıllı telefonda, Apple'ın bilgisayarlarında ve dünyanın en büyük veri merkezlerinin bazılarında.

Yaygın açıklama şu: ARM basit ve verimli, verimli olan da kazanır. Ama modern bir ARM çekirdeği basit olmaktan çok uzak ve 1990'ların ortasından beri Intel'in çiplerinin iç yapısı da şaşırtıcı derecede benziyor. Peki İngiliz bir ev bilgisayarı şirketinin çipi nasıl her yere girdi?

Altyazılar bu video için yazıldı, otomatik olarak oluşturulmadı. İkinci ses parçası olarak Amerikan İngilizcesi de mevcut.

BÖLÜMLER
00:00 Elektrik olmadan çalışan çip
01:10 Acorn, 1983
02:11 RISC fikri
03:34 ARM1
04:09 Archimedes
04:46 Apple ve yeni bir şirket
05:17 Tasarımı satmak
06:00 Telefonlar
06:35 Cevap basitlik mi?
07:13 İki farklı şey
07:36 x86'ya ne oldu
08:34 Apple'a dönüş
09:07 Veri merkezleri
09:30 Gerçekte ne yaptılar

GÖRSEL KAYNAKLARI
Acorn Archimedes A310 with mouse and keyboard — mikkohoo, CC BY-SA 4.0
Apple Newton MessagePad 100 — Felix Winkelnkemper, CC BY-SA 4.0
Nokia 6110 blue-92111 — Raimond Spekking, CC BY-SA 4.0
via Wikimedia Commons
Diğer tüm arşiv görselleri kamu malı ya da CC0'dır.
Licences: creativecommons.org/licenses/by-sa/4.0
```

## українська (`uk`)

```
Як ARM підкорив комп’ютерний світ?
```

```
У 1985 році перший процесор ARM увімкнули вперше, і він працював далі, хоча його живлення не було під’єднане. Через сорок років його нащадки є майже в кожному смартфоні, у комп’ютерах Apple і в деяких із найбільших дата-центрів світу.

Звичне пояснення таке: ARM простий і ефективний, а ефективний перемагає. Але сучасне ядро ARM аж ніяк не просте, а з середини 1990-х чипи Intel усередині напрочуд схожі. То як чип від британського виробника домашніх комп’ютерів опинився всюди?

Субтитри написані для цього відео, а не згенеровані автоматично. Також доступна друга звукова доріжка — американською англійською.

РОЗДІЛИ
00:00 Чип, що працював без живлення
01:10 Acorn, 1983
02:11 Ідея RISC
03:34 ARM1
04:09 Archimedes
04:46 Apple і нова компанія
05:17 Продаж проєкту
06:00 Телефони
06:35 Чи є простота відповіддю?
07:13 Дві різні речі
07:36 Що сталося з x86
08:34 Повернення до Apple
09:07 Дата-центри
09:30 Що вони насправді збудували

ДЖЕРЕЛА ЗОБРАЖЕНЬ
Acorn Archimedes A310 with mouse and keyboard — mikkohoo, CC BY-SA 4.0
Apple Newton MessagePad 100 — Felix Winkelnkemper, CC BY-SA 4.0
Nokia 6110 blue-92111 — Raimond Spekking, CC BY-SA 4.0
via Wikimedia Commons
Усі інші архівні зображення є суспільним надбанням або мають ліцензію CC0.
Licences: creativecommons.org/licenses/by-sa/4.0
```

## Tiếng Việt (`vi`)

```
ARM đã chiếm lĩnh ngành điện toán như thế nào?
```

```
Năm 1985, bộ xử lý ARM đầu tiên được bật lên lần đầu tiên, và nó vẫn tiếp tục chạy dù nguồn điện chưa hề được nối. Bốn mươi năm sau, hậu duệ của nó có mặt trong gần như mọi điện thoại thông minh, trong máy tính của Apple và trong một số trung tâm dữ liệu lớn nhất thế giới.

Cách giải thích thường gặp là ARM đơn giản và hiệu quả, và hiệu quả thì chiến thắng. Nhưng một lõi ARM hiện đại chẳng hề đơn giản chút nào, và từ giữa thập niên 1990, bên trong các con chip của Intel cũng trông giống đến bất ngờ. Vậy làm thế nào một con chip của một công ty máy tính gia đình ở Anh lại có mặt ở khắp nơi?

Phụ đề được viết riêng cho video này, không phải tạo tự động. Có thể chọn tiếng Anh Mỹ ở bản âm thanh thứ hai.

CHƯƠNG
00:00 Con chip chạy khi chưa nối nguồn điện
01:10 Acorn, 1983
02:11 Ý tưởng RISC
03:34 ARM1
04:09 Archimedes
04:46 Apple và một công ty mới
05:17 Bán bản thiết kế
06:00 Điện thoại
06:35 Đơn giản có phải là câu trả lời?
07:13 Hai thứ khác nhau
07:36 Chuyện gì đã xảy ra với x86
08:34 Trở lại với Apple
09:07 Trung tâm dữ liệu
09:30 Những gì họ thực sự đã tạo ra

NGUỒN HÌNH ẢNH
Acorn Archimedes A310 with mouse and keyboard — mikkohoo, CC BY-SA 4.0
Apple Newton MessagePad 100 — Felix Winkelnkemper, CC BY-SA 4.0
Nokia 6110 blue-92111 — Raimond Spekking, CC BY-SA 4.0
via Wikimedia Commons
Tất cả các hình ảnh lưu trữ khác thuộc phạm vi công cộng hoặc CC0.
Licences: creativecommons.org/licenses/by-sa/4.0
```

## čeština (`cs`)

```
Jak ARM ovládl výpočetní techniku?
```

```
V roce 1985 poprvé zapnuli první procesor ARM – a ten běžel dál, přestože jeho napájení nebylo zapojené. O čtyřicet let později jsou jeho potomci skoro v každém chytrém telefonu, v počítačích Applu a v některých z největších datových center na světě.

Obvyklé vysvětlení zní, že ARM je jednoduchý a efektivní a efektivní vyhrává. Jenže moderní jádro ARM je všechno, jen ne jednoduché, a čipy Intelu vypadají od poloviny 90. let uvnitř překvapivě podobně. Jak tedy čip od britské firmy na domácí počítače skončil úplně všude?

Titulky jsou psané pro tohle video, ne strojový přepis. Jako druhá zvuková stopa je k dispozici americká angličtina.

KAPITOLY
00:00 Čip, který běžel bez napájení
01:10 Acorn, 1983
02:11 Myšlenka RISC
03:34 ARM1
04:09 Archimedes
04:46 Apple a nová firma
05:17 Prodej návrhu
06:00 Telefony
06:35 Je odpovědí jednoduchost?
07:13 Dvě různé věci
07:36 Co se stalo s x86
08:34 Zpátky k Applu
09:07 Datová centra
09:30 Co doopravdy postavili

ZDROJE OBRÁZKŮ
Acorn Archimedes A310 with mouse and keyboard — mikkohoo, CC BY-SA 4.0
Apple Newton MessagePad 100 — Felix Winkelnkemper, CC BY-SA 4.0
Nokia 6110 blue-92111 — Raimond Spekking, CC BY-SA 4.0
via Wikimedia Commons
Všechny ostatní archivní snímky jsou volné dílo nebo CC0.
Licences: creativecommons.org/licenses/by-sa/4.0
```

## español (`es`)

```
¿Cómo conquistó ARM la informática?
```

```
En 1985, el primer procesador ARM se encendió por primera vez, y siguió funcionando aunque su alimentación no estaba conectada. Cuarenta años después, sus descendientes están en casi todos los smartphones, en los ordenadores de Apple y en algunos de los mayores centros de datos del mundo.

La explicación habitual es que ARM es sencillo y eficiente, y lo eficiente gana. Pero un núcleo ARM moderno es cualquier cosa menos sencillo, y desde mediados de los noventa los chips de Intel se le parecen sorprendentemente por dentro. Entonces, ¿cómo acabó en todas partes un chip de una empresa británica de ordenadores domésticos?

Los subtítulos están escritos para este vídeo, no generados automáticamente. Como segunda pista de audio está disponible el inglés americano.

CAPÍTULOS
00:00 El chip que funcionaba sin corriente
01:10 Acorn, 1983
02:11 La idea RISC
03:34 El ARM1
04:09 El Archimedes
04:46 Apple y una nueva empresa
05:17 Vender el diseño
06:00 Los teléfonos
06:35 ¿Es lo sencillo la respuesta?
07:13 Dos cosas distintas
07:36 Qué pasó con x86
08:34 De vuelta a Apple
09:07 Centros de datos
09:30 Lo que construyeron de verdad

CRÉDITOS DE LAS IMÁGENES
Acorn Archimedes A310 with mouse and keyboard — mikkohoo, CC BY-SA 4.0
Apple Newton MessagePad 100 — Felix Winkelnkemper, CC BY-SA 4.0
Nokia 6110 blue-92111 — Raimond Spekking, CC BY-SA 4.0
via Wikimedia Commons
Todas las demás imágenes de archivo son de dominio público o CC0.
Licences: creativecommons.org/licenses/by-sa/4.0
```

## svenska (`sv`)

```
Hur tog ARM över datorvärlden?
```

```
År 1985 slogs den första ARM-processorn på för allra första gången, och den fortsatte att gå trots att strömförsörjningen inte var ansluten. Fyrtio år senare finns dess ättlingar i nästan varenda smartphone, i Apples datorer och i några av de största datacentren i världen.

Den vanliga förklaringen är att ARM är enkelt och effektivt, och effektivt vinner. Men en modern ARM-kärna är allt annat än enkel, och sedan mitten av 1990-talet ser Intels chip förvånansvärt likartade ut inuti. Så hur hamnade ett chip från ett brittiskt hemdatorföretag överallt?

Undertexterna är skrivna för den här videon, inte automatgenererade. Som andra ljudspår finns amerikansk engelska.

KAPITEL
00:00 Chippet som gick utan ström
01:10 Acorn, 1983
02:11 RISC-idén
03:34 ARM1
04:09 Archimedes
04:46 Apple och ett nytt företag
05:17 Att sälja konstruktionen
06:00 Telefoner
06:35 Är enkelhet svaret?
07:13 Två olika saker
07:36 Vad hände med x86
08:34 Tillbaka till Apple
09:07 Datacenter
09:30 Vad de egentligen byggde

BILDKÄLLOR
Acorn Archimedes A310 with mouse and keyboard — mikkohoo, CC BY-SA 4.0
Apple Newton MessagePad 100 — Felix Winkelnkemper, CC BY-SA 4.0
Nokia 6110 blue-92111 — Raimond Spekking, CC BY-SA 4.0
via Wikimedia Commons
Alla andra arkivbilder är fria från upphovsrätt eller CC0.
Licences: creativecommons.org/licenses/by-sa/4.0
```
