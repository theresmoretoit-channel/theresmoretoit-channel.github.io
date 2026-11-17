# Lokalizované názvy a popisy — 110

Čte `tools/lokalizace.py` a nahrává přes `videos.update(part="localizations")`.
Anglický titul a popis jsou v `youtube.md` a posílají se zpátky beze změny.

**Pořadí sekcí je podle YouTube Studia** (bajtově podle ČESKÉHO názvu jazyka):
fi, fr, id, it, de, pl, pt-BR, tr, uk, vi, cs, es, sv.

## Co se NEPŘEKLÁDÁ

- jména sond a institucí: Voyager 1/2, Mariner 4, JPL, NASA, Kodak,
  Deep Space Network, Very Large Array, Steven Sasson. Ukrajinština je
  píše tak jako titulky (Вояджер-2, Марінер-4, Стівен Сассон; Kodak, JPL,
  NASA latinkou).
- Pale Blue Dot se píše **tak, jak ho mají titulky** daného jazyka (S50):
  fi, de, sv *Pale Blue Dot*; fr *point bleu pâle*, id *Titik Biru Pucat*,
  it *Pallido puntino azzurro*, pl *Blada Niebieska Kropka*, pt-BR *Pálido
  Ponto Azul*, tr *Soluk Mavi Nokta*, uk *Блідо-блакитна цятка*, vi *Chấm
  xanh mờ (Pale Blue Dot)*, cs *Bledě modrá tečka*, es *Punto Azul Pálido*.
- časy kapitol na vteřinu (ze `youtube.md`, scény S01, S05, S11, S14,
  S20, S27, S33, S35, S41, S43, S51).
- IMAGE CREDITS: jméno autora (CGP Grey), licence a URL. Přeložené jsou
  popisek snímku (New Mexico jen tam, kde má jazyk vlastní tvar), nadpisy
  CHAPTERS / IMAGE CREDITS / Sources, „via Wikimedia Commons“, „Licence:“
  a věta o public domain.
- citace zdrojů: autoři, názvy prací (*Voyager Telecommunications*,
  *Computers in Spaceflight*, *Voyager Imaging Science Investigations*,
  *A Planet Painted by Hand*), JPL DESCANSO, NASA CR-182505, NSSDC,
  PIA00451–PIA00453. Přeložený je jen popis zdroje u PDS Rings Node
  a IEEE Spectrum.
- čísla: v popisu číslicí (4 a 6 miliard km, 12 let) — anglický popis
  je má slovy. *Billion* = 10⁹: miliarda, Milliarden, miljard(er),
  milliards, miliardi, miliar, milyar, мільярд, tỷ, bilhões (pt-BR),
  4000/6000 millones (es). Názvy kapitol slovy jako v originále.
- tagy — YouTube je per-jazyk nemá.

Odstavec o titulcích a americké stopě je **doslova** z tabulky
v `docs/zverejneni.md` („Popis NEJMENUJE počet jazyků titulků").

Terminologie podle titulků `script.<kód>.md` téhož jazyka: televizní
snímací elektronka (S02, S06: televisiokameraputki, tube de caméra de
télévision, tabung televisi, tubo da ripresa televisiva,
Fernsehaufnahmeröhre, lampa telewizyjna, tubo de televisão, televizyon
tüpü, телевізійна трубка, ống thu hình truyền hình, tubo de televisión,
tv-kamerarör), pastely (S11), antény DSN (S33), úzkoúhlá kamera (S20).
Rod sondy podle titulků (fr, it, es, pt-BR ženský; de *sie*).
Anglický popis má *„like the one in your phone"*; překlady diváka
neoslovují (*jaký mají dnešní telefony*), takže registr se v nich
neprojeví. Pointa se neprozrazuje víc než v angličtině: jak se obraz
dostal domů (řetěz, komprese přeprogramovaná za letu), popis neříká.

## suomi (`fi`)

```
Miten Voyager lähetti kuvia kotiin?
```

```
Elokuussa 1989 Voyager 2 lensi Neptunuksen ohi yli 4 miljardin kilometrin päässä Maasta ja kuvasi sen. Sen kamerat perustuivat 1970-luvulla suunniteltuihin televisiokameraputkiin: niissä ei ollut muistikorttia eikä sellaista kennoa kuin nykyisissä puhelimissa. Silti perille saapui tuhansia kuvia.

Tarina alkaa 12 vuotta ennen Voyagerin laukaisua, Mariner 4 -luotaimesta Marsin luona ja ensimmäisestä toisen planeetan lähikuvasta, jonka JPL:n insinöörit värittivät käsin pastelliliiduilla. Se kulkee Kodakin laboratorion kautta, jossa Steven Sasson rakensi vuonna 1975 aivan toisenlaisen kameran. Ja se päättyy Voyagerin kuuluisimpaan kuvaan: Pale Blue Dot -kuvaan, joka lähetettiin kotiin 6 miljardin kilometrin päästä.

Lähteet: Ludwig & Taylor, Voyager Telecommunications (JPL DESCANSO, 2002); PDS Rings Node, Voyagerin kapeakulmakameran kuvaus; J. Tomayko, Computers in Spaceflight (NASA CR-182505, 1988); B. A. Smith, Voyager Imaging Science Investigations (NASA, 1979); NSSDC, Mariner 4; Caltech Magazine, A Planet Painted by Hand; IEEE Spectrum, ensimmäisen digitaalikameran historia; NASA Photojournal PIA00451–PIA00453.

Tekstitykset on kirjoitettu tätä videota varten, ei luotu automaattisesti. Toisena ääniraitana on amerikanenglanti.

LUVUT
00:00 Kamera, jonka ytimenä oli televisioputki
00:35 Mariner 4 Marsin luona
01:32 Käsin väritetty kuva
02:06 Kamera Kodakin laboratoriossa
03:10 Voyagerin kamerat
04:17 Miten kuvat saatiin kotiin
05:04 Antennien uudistus Maassa
05:24 Uusi ohjelmisto kaukaiselle luotaimelle
06:27 Olivatko ne siis digitaalikameroita?
06:55 Pale Blue Dot
08:06 Yksitoista viikkoa kotimatkalla

KUVALÄHTEET
Very Large Array, New Mexico — CGP Grey, CC BY 2.0
Wikimedia Commonsin kautta
Lisenssi: creativecommons.org/licenses/by/2.0
Muut arkistokuvat: NASA, NASA/JPL, NASA/JPL-Caltech, NASA/GRC, public domain.
```

## français (`fr`)

```
Comment Voyager envoyait-elle ses photos sur Terre ?
```

```
En août 1989, Voyager 2 est passée près de Neptune, à plus de 4 milliards de kilomètres de la Terre, et en a pris des photos. Ses caméras reposaient sur des tubes de caméra de télévision conçus dans les années 1970, sans carte mémoire ni capteur comme celui des téléphones d’aujourd’hui. Et pourtant, des milliers d’images sont arrivées.

L’histoire commence 12 ans avant le lancement de Voyager, avec Mariner 4 près de Mars et la première image rapprochée d’une autre planète, que les ingénieurs du JPL ont coloriée à la main au pastel. Elle passe par un labo de Kodak, où Steven Sasson a construit en 1975 un appareil photo d’un tout autre genre. Et elle se termine par la photo la plus célèbre jamais prise par Voyager : le « point bleu pâle », envoyé sur Terre depuis 6 milliards de kilomètres.

Sources : Ludwig & Taylor, Voyager Telecommunications (JPL DESCANSO, 2002) ; PDS Rings Node, description de la caméra à champ étroit de Voyager ; J. Tomayko, Computers in Spaceflight (NASA CR-182505, 1988) ; B. A. Smith, Voyager Imaging Science Investigations (NASA, 1979) ; NSSDC, Mariner 4 ; Caltech Magazine, A Planet Painted by Hand ; IEEE Spectrum, histoire du premier appareil photo numérique ; NASA Photojournal PIA00451–PIA00453.

Les sous-titres sont écrits pour cette vidéo, pas générés automatiquement. Une piste audio en anglais américain est disponible en seconde piste.

CHAPITRES
00:00 Une caméra construite autour d’un tube de télévision
00:35 Mariner 4 près de Mars
01:32 Une image coloriée à la main
02:06 Un appareil photo dans un labo de Kodak
03:10 Les caméras de Voyager
04:17 Rapatrier les images
05:04 Reconstruire les antennes sur Terre
05:24 Un nouveau logiciel pour une sonde lointaine
06:27 Alors, étaient-ce des appareils photo numériques ?
06:55 Le point bleu pâle
08:06 Onze semaines pour rentrer à la maison

CRÉDITS DES IMAGES
Very Large Array, Nouveau-Mexique — CGP Grey, CC BY 2.0
via Wikimedia Commons
Licence : creativecommons.org/licenses/by/2.0
Toutes les autres images d’archives : NASA, NASA/JPL, NASA/JPL-Caltech, NASA/GRC, domaine public.
```

## Bahasa Indonesia (`id`)

```
Bagaimana Voyager mengirim foto pulang ke Bumi?
```

```
Pada Agustus 1989, Voyager 2 melintasi Neptunus, lebih dari 4 miliar kilometer dari Bumi, dan memotretnya. Kamera-kameranya menggunakan tabung kamera televisi yang dirancang pada tahun 1970-an, tanpa kartu memori dan tanpa sensor seperti di ponsel masa kini. Meski begitu, ribuan foto berhasil tiba.

Kisahnya dimulai 12 tahun sebelum peluncuran Voyager, dengan Mariner 4 yang melintasi Mars dan citra jarak dekat pertama dari planet lain, yang diwarnai dengan tangan memakai kapur pastel oleh para insinyur di JPL. Kisah ini melewati sebuah laboratorium Kodak, tempat Steven Sasson membuat jenis kamera yang sama sekali berbeda pada tahun 1975. Dan kisah ini berakhir dengan foto paling terkenal yang pernah diambil Voyager: Titik Biru Pucat, yang dikirim pulang dari jarak 6 miliar kilometer.

Sumber: Ludwig & Taylor, Voyager Telecommunications (JPL DESCANSO, 2002); PDS Rings Node, deskripsi kamera sudut sempit Voyager; J. Tomayko, Computers in Spaceflight (NASA CR-182505, 1988); B. A. Smith, Voyager Imaging Science Investigations (NASA, 1979); NSSDC, Mariner 4; Caltech Magazine, A Planet Painted by Hand; IEEE Spectrum, sejarah kamera digital pertama; NASA Photojournal PIA00451–PIA00453.

Subtitel ditulis khusus untuk video ini, bukan dibuat secara otomatis. Tersedia juga trek audio kedua dalam bahasa Inggris Amerika.

BAB
00:00 Kamera berbasis tabung televisi
00:35 Mariner 4 melintasi Mars
01:32 Gambar yang diwarnai dengan tangan
02:06 Kamera di laboratorium Kodak
03:10 Kamera-kamera Voyager
04:17 Membawa foto pulang
05:04 Membangun ulang antena di Bumi
05:24 Perangkat lunak baru untuk wahana yang jauh
06:27 Jadi, apakah itu kamera digital?
06:55 Titik Biru Pucat
08:06 Sebelas minggu perjalanan pulang

KREDIT GAMBAR
Very Large Array, New Mexico — CGP Grey, CC BY 2.0
melalui Wikimedia Commons
Lisensi: creativecommons.org/licenses/by/2.0
Semua gambar arsip lainnya: NASA, NASA/JPL, NASA/JPL-Caltech, NASA/GRC, domain publik.
```

## italiano (`it`)

```
Come faceva la Voyager a mandare le foto a casa?
```

```
Nell’agosto del 1989 la Voyager 2 è passata accanto a Nettuno, a più di 4 miliardi di chilometri dalla Terra, e l’ha fotografato. Le sue telecamere erano basate su tubi da ripresa televisiva progettati negli anni Settanta, senza scheda di memoria e senza un sensore come quello dei telefoni di oggi. Eppure sono arrivate migliaia di immagini.

La storia comincia 12 anni prima del lancio della Voyager, con la Mariner 4 vicino a Marte e la prima immagine ravvicinata di un altro pianeta, che gli ingegneri del JPL hanno colorato a mano con i gessetti pastello. Passa per un laboratorio della Kodak, dove nel 1975 Steven Sasson ha costruito una fotocamera di tutt’altro tipo. E finisce con la foto più famosa mai scattata dalla Voyager: il Pallido puntino azzurro, inviato a casa da 6 miliardi di chilometri di distanza.

Fonti: Ludwig & Taylor, Voyager Telecommunications (JPL DESCANSO, 2002); PDS Rings Node, descrizione della telecamera a campo stretto della Voyager; J. Tomayko, Computers in Spaceflight (NASA CR-182505, 1988); B. A. Smith, Voyager Imaging Science Investigations (NASA, 1979); NSSDC, Mariner 4; Caltech Magazine, A Planet Painted by Hand; IEEE Spectrum, storia della prima fotocamera digitale; NASA Photojournal PIA00451–PIA00453.

I sottotitoli sono scritti per questo video, non generati automaticamente. Come seconda traccia audio è disponibile l’inglese americano.

CAPITOLI
00:00 Una telecamera basata su un tubo televisivo
00:35 La Mariner 4 vicino a Marte
01:32 Un’immagine colorata a mano
02:06 Una fotocamera in un laboratorio della Kodak
03:10 Le telecamere della Voyager
04:17 Portare le immagini a casa
05:04 Ricostruire le antenne sulla Terra
05:24 Un nuovo software per una sonda lontana
06:27 Allora erano fotocamere digitali?
06:55 Il Pallido puntino azzurro
08:06 Undici settimane per tornare a casa

CREDITI DELLE IMMAGINI
Very Large Array, New Mexico — CGP Grey, CC BY 2.0
tramite Wikimedia Commons
Licenza: creativecommons.org/licenses/by/2.0
Tutte le altre immagini d’archivio: NASA, NASA/JPL, NASA/JPL-Caltech, NASA/GRC, pubblico dominio.
```

## Deutsch (`de`)

```
Wie schickte Voyager Bilder nach Hause?
```

```
Im August 1989 flog Voyager 2 an Neptun vorbei, mehr als 4 Milliarden Kilometer von der Erde entfernt, und fotografierte ihn. Ihre Kameras beruhten auf Fernsehaufnahmeröhren, die in den 1970er-Jahren entworfen worden waren, ohne Speicherkarte und ohne einen Sensor wie in heutigen Handys. Und doch kamen Tausende Bilder an.

Die Geschichte beginnt 12 Jahre vor dem Start von Voyager, mit Mariner 4 am Mars und der ersten Nahaufnahme eines anderen Planeten, die Ingenieure am JPL von Hand mit Pastellkreide ausmalten. Sie führt durch ein Labor bei Kodak, in dem Steven Sasson 1975 eine ganz andere Art von Kamera baute. Und sie endet mit dem berühmtesten Bild, das Voyager je aufgenommen hat: dem Pale Blue Dot, aus 6 Milliarden Kilometern Entfernung nach Hause geschickt.

Quellen: Ludwig & Taylor, Voyager Telecommunications (JPL DESCANSO, 2002); PDS Rings Node, Beschreibung der Telekamera von Voyager; J. Tomayko, Computers in Spaceflight (NASA CR-182505, 1988); B. A. Smith, Voyager Imaging Science Investigations (NASA, 1979); NSSDC, Mariner 4; Caltech Magazine, A Planet Painted by Hand; IEEE Spectrum, Geschichte der ersten Digitalkamera; NASA Photojournal PIA00451–PIA00453.

Die Untertitel wurden für dieses Video geschrieben, nicht automatisch erzeugt. Als zweite Tonspur steht amerikanisches Englisch bereit.

KAPITEL
00:00 Eine Kamera auf Basis einer Fernsehaufnahmeröhre
00:35 Mariner 4 am Mars
01:32 Ein von Hand ausgemaltes Bild
02:06 Eine Kamera in einem Labor bei Kodak
03:10 Die Kameras von Voyager
04:17 Wie die Bilder nach Hause kommen
05:04 Umbau der Antennen auf der Erde
05:24 Neue Software für eine ferne Sonde
06:27 Waren es also Digitalkameras?
06:55 Der Pale Blue Dot
08:06 Elf Wochen bis nach Hause

BILDNACHWEISE
Very Large Array, New Mexico — CGP Grey, CC BY 2.0
über Wikimedia Commons
Lizenz: creativecommons.org/licenses/by/2.0
Alle anderen Archivbilder: NASA, NASA/JPL, NASA/JPL-Caltech, NASA/GRC, gemeinfrei.
```

## polski (`pl`)

```
Jak Voyager wysyłał zdjęcia do domu?
```

```
W sierpniu 1989 roku Voyager 2 przeleciał obok Neptuna, ponad 4 miliardy kilometrów od Ziemi, i zrobił mu zdjęcia. Jego kamery opierały się na lampach telewizyjnych zaprojektowanych w latach 70., bez karty pamięci i bez matrycy takiej jak w dzisiejszych telefonach. A jednak dotarły tysiące zdjęć.

Historia zaczyna się 12 lat przed startem Voyagera, od przelotu sondy Mariner 4 obok Marsa i pierwszego obrazu innej planety z bliska, który inżynierowie z JPL ręcznie pokolorowali pastelami. Prowadzi przez laboratorium Kodaka, gdzie Steven Sasson zbudował w 1975 roku zupełnie inny rodzaj aparatu. I kończy się najsłynniejszym zdjęciem, jakie Voyager kiedykolwiek zrobił: Bladą Niebieską Kropką, wysłaną do domu z odległości 6 miliardów kilometrów.

Źródła: Ludwig & Taylor, Voyager Telecommunications (JPL DESCANSO, 2002); PDS Rings Node, opis wąskokątnej kamery Voyagera; J. Tomayko, Computers in Spaceflight (NASA CR-182505, 1988); B. A. Smith, Voyager Imaging Science Investigations (NASA, 1979); NSSDC, Mariner 4; Caltech Magazine, A Planet Painted by Hand; IEEE Spectrum, historia pierwszego aparatu cyfrowego; NASA Photojournal PIA00451–PIA00453.

Napisy są pisane do tego filmu, nie generowane automatycznie. Jako druga ścieżka dźwiękowa dostępny jest angielski amerykański.

ROZDZIAŁY
00:00 Kamera zbudowana wokół lampy telewizyjnej
00:35 Mariner 4 przy Marsie
01:32 Obraz pokolorowany ręcznie
02:06 Aparat w laboratorium Kodaka
03:10 Kamery Voyagera
04:17 Jak przesłać zdjęcia do domu
05:04 Przebudowa anten na Ziemi
05:24 Nowe oprogramowanie dla odległej sondy
06:27 Czy to były więc aparaty cyfrowe?
06:55 Blada Niebieska Kropka
08:06 Jedenaście tygodni drogi do domu

ŹRÓDŁA ZDJĘĆ
Very Large Array, Nowy Meksyk — CGP Grey, CC BY 2.0
przez Wikimedia Commons
Licencja: creativecommons.org/licenses/by/2.0
Pozostałe zdjęcia archiwalne: NASA, NASA/JPL, NASA/JPL-Caltech, NASA/GRC, domena publiczna.
```

## português (Brasil) (`pt-BR`)

```
Como a Voyager mandava fotos para casa?
```

```
Em agosto de 1989, a Voyager 2 passou por Netuno, a mais de 4 bilhões de quilômetros da Terra, e tirou fotos dele. As câmeras dela funcionavam com tubos de televisão projetados nos anos 1970, sem cartão de memória e sem um sensor como o dos celulares de hoje. E mesmo assim chegaram milhares de fotos.

A história começa 12 anos antes do lançamento da Voyager, com a Mariner 4 passando por Marte e a primeira imagem de perto de outro planeta, que os engenheiros do JPL coloriram à mão com giz pastel. Passa por um laboratório da Kodak, onde Steven Sasson construiu em 1975 um tipo de câmera bem diferente. E termina com a foto mais famosa que a Voyager já tirou: o Pálido Ponto Azul, enviado para casa de 6 bilhões de quilômetros de distância.

Fontes: Ludwig & Taylor, Voyager Telecommunications (JPL DESCANSO, 2002); PDS Rings Node, descrição da câmera de ângulo estreito da Voyager; J. Tomayko, Computers in Spaceflight (NASA CR-182505, 1988); B. A. Smith, Voyager Imaging Science Investigations (NASA, 1979); NSSDC, Mariner 4; Caltech Magazine, A Planet Painted by Hand; IEEE Spectrum, história da primeira câmera digital; NASA Photojournal PIA00451–PIA00453.

As legendas foram escritas para este vídeo, não geradas automaticamente. Como segunda faixa de áudio está disponível o inglês americano.

CAPÍTULOS
00:00 Uma câmera feita com um tubo de TV
00:35 A Mariner 4 em Marte
01:32 Uma imagem colorida à mão
02:06 Uma câmera num laboratório da Kodak
03:10 As câmeras da Voyager
04:17 Como trazer as fotos para casa
05:04 Reconstruindo as antenas na Terra
05:24 Um software novo para uma sonda distante
06:27 Então eram câmeras digitais?
06:55 O Pálido Ponto Azul
08:06 Onze semanas para chegar em casa

CRÉDITOS DAS IMAGENS
Very Large Array, Novo México — CGP Grey, CC BY 2.0
via Wikimedia Commons
Licença: creativecommons.org/licenses/by/2.0
Todas as outras imagens de arquivo: NASA, NASA/JPL, NASA/JPL-Caltech, NASA/GRC, domínio público.
```

## Türkçe (`tr`)

```
Voyager fotoğrafları eve nasıl gönderdi?
```

```
Ağustos 1989'da Voyager 2, Dünya'dan 4 milyar kilometreden daha uzaktayken Neptün'ün yanından geçti ve gezegenin fotoğraflarını çekti. Kameraları 1970'lerde tasarlanmış televizyon tüplerine dayanıyordu; hafıza kartı yoktu, bugünkü telefonlardakine benzer bir sensör de yoktu. Yine de binlerce fotoğraf Dünya'ya ulaştı.

Hikâye, Voyager'ın fırlatılmasından 12 yıl önce, Mars'ın yanından geçen Mariner 4 ve başka bir gezegenin yakından çekilmiş ilk görüntüsüyle başlıyor; JPL'deki mühendisler bu görüntüyü pastel boyalarla elle boyamıştı. Ardından Steven Sasson'ın 1975'te bambaşka türde bir kamera yaptığı Kodak laboratuvarından geçiyor. Ve Voyager'ın çektiği en ünlü fotoğrafla bitiyor: 6 milyar kilometre öteden eve gönderilen Soluk Mavi Nokta.

Kaynaklar: Ludwig & Taylor, Voyager Telecommunications (JPL DESCANSO, 2002); PDS Rings Node, Voyager dar açılı kamerasının tanımı; J. Tomayko, Computers in Spaceflight (NASA CR-182505, 1988); B. A. Smith, Voyager Imaging Science Investigations (NASA, 1979); NSSDC, Mariner 4; Caltech Magazine, A Planet Painted by Hand; IEEE Spectrum, ilk dijital kameranın tarihi; NASA Photojournal PIA00451–PIA00453.

Altyazılar bu video için yazıldı, otomatik olarak oluşturulmadı. İkinci ses parçası olarak Amerikan İngilizcesi de mevcut.

BÖLÜMLER
00:00 Televizyon tüpüne dayanan bir kamera
00:35 Mariner 4 Mars'ın yanında
01:32 Elle boyanmış bir görüntü
02:06 Kodak'ın laboratuvarında bir kamera
03:10 Voyager'ın kameraları
04:17 Fotoğrafları eve getirmek
05:04 Dünya'daki antenlerin yeniden yapılması
05:24 Uzaktaki bir uzay aracı için yeni yazılım
06:27 Peki bunlar dijital kamera mıydı?
06:55 Soluk Mavi Nokta
08:06 On bir haftalık eve dönüş

GÖRSEL KAYNAKLARI
Very Large Array, New Mexico — CGP Grey, CC BY 2.0
Wikimedia Commons aracılığıyla
Lisans: creativecommons.org/licenses/by/2.0
Diğer tüm arşiv görselleri: NASA, NASA/JPL, NASA/JPL-Caltech, NASA/GRC, kamu malı.
```

## українська (`uk`)

```
Як Вояджер надсилав знімки додому?
```

```
У серпні 1989 року Вояджер-2 пролетів повз Нептун на відстані понад 4 мільярди кілометрів від Землі і сфотографував його. Його камери були побудовані на основі телевізійних трубок, розроблених у 1970-х, — без карти пам'яті й без сенсора, як у сучасних телефонах. І все ж надійшли тисячі знімків.

Історія починається за 12 років до запуску Вояджера, з прольоту Марінера-4 повз Марс і першого зображення іншої планети зблизька, яке інженери JPL розфарбували вручну пастеллю. Далі історія переноситься до лабораторії Kodak, де Стівен Сассон у 1975 році зібрав зовсім інший фотоапарат. І закінчується найвідомішим знімком, який будь-коли зробив Вояджер: «Блідо-блакитною цяткою», надісланою додому з відстані 6 мільярдів кілометрів.

Джерела: Ludwig & Taylor, Voyager Telecommunications (JPL DESCANSO, 2002); PDS Rings Node, опис вузькокутної камери Вояджера; J. Tomayko, Computers in Spaceflight (NASA CR-182505, 1988); B. A. Smith, Voyager Imaging Science Investigations (NASA, 1979); NSSDC, Mariner 4; Caltech Magazine, A Planet Painted by Hand; IEEE Spectrum, історія першого цифрового фотоапарата; NASA Photojournal PIA00451–PIA00453.

Субтитри написані для цього відео, а не згенеровані автоматично. Також доступна друга звукова доріжка — американською англійською.

РОЗДІЛИ
00:00 Камера на основі телевізійної трубки
00:35 Марінер-4 біля Марса
01:32 Зображення, розфарбоване вручну
02:06 Фотоапарат у лабораторії Kodak
03:10 Камери Вояджера
04:17 Як доставити знімки додому
05:04 Перебудова антен на Землі
05:24 Нове програмне забезпечення для далекого зонда
06:27 То чи були це цифрові фотоапарати?
06:55 Блідо-блакитна цятка
08:06 Одинадцять тижнів дороги додому

ДЖЕРЕЛА ЗОБРАЖЕНЬ
Very Large Array, Нью-Мексико — CGP Grey, CC BY 2.0
через Wikimedia Commons
Ліцензія: creativecommons.org/licenses/by/2.0
Усі інші архівні зображення: NASA, NASA/JPL, NASA/JPL-Caltech, NASA/GRC, суспільне надбання.
```

## Tiếng Việt (`vi`)

```
Voyager đã gửi ảnh về Trái Đất bằng cách nào?
```

```
Vào tháng 8 năm 1989, Voyager 2 bay ngang qua Sao Hải Vương, ở cách Trái Đất hơn 4 tỷ kilômét, và chụp ảnh hành tinh này. Các máy ảnh của nó sử dụng những ống thu hình truyền hình được thiết kế vào thập niên 1970, không có thẻ nhớ và cũng không có cảm biến như trong điện thoại ngày nay. Vậy mà hàng nghìn bức ảnh vẫn về đến nơi.

Câu chuyện bắt đầu 12 năm trước khi Voyager được phóng, với tàu Mariner 4 bay ngang qua Sao Hỏa và hình ảnh cận cảnh đầu tiên của một hành tinh khác, được các kỹ sư ở JPL tô màu bằng tay với phấn màu. Tiếp đó, câu chuyện chuyển đến một phòng thí nghiệm của Kodak, nơi Steven Sasson chế tạo một loại máy ảnh hoàn toàn khác vào năm 1975. Và kết thúc với bức ảnh nổi tiếng nhất mà Voyager từng chụp: Chấm xanh mờ (Pale Blue Dot), được gửi về từ khoảng cách 6 tỷ kilômét.

Nguồn: Ludwig & Taylor, Voyager Telecommunications (JPL DESCANSO, 2002); PDS Rings Node, mô tả máy ảnh góc hẹp của Voyager; J. Tomayko, Computers in Spaceflight (NASA CR-182505, 1988); B. A. Smith, Voyager Imaging Science Investigations (NASA, 1979); NSSDC, Mariner 4; Caltech Magazine, A Planet Painted by Hand; IEEE Spectrum, lịch sử chiếc máy ảnh kỹ thuật số đầu tiên; NASA Photojournal PIA00451–PIA00453.

Phụ đề được viết riêng cho video này, không phải tạo tự động. Có thể chọn tiếng Anh Mỹ ở bản âm thanh thứ hai.

CHƯƠNG
00:00 Chiếc máy ảnh dựa trên ống truyền hình
00:35 Mariner 4 bay ngang Sao Hỏa
01:32 Bức ảnh được tô màu bằng tay
02:06 Chiếc máy ảnh trong phòng thí nghiệm Kodak
03:10 Các máy ảnh của Voyager
04:17 Đưa ảnh về Trái Đất
05:04 Xây lại các ăng-ten trên Trái Đất
05:24 Phần mềm mới cho một tàu vũ trụ ở xa
06:27 Vậy chúng có phải máy ảnh kỹ thuật số không?
06:55 Chấm xanh mờ
08:06 Mười một tuần để về nhà

NGUỒN HÌNH ẢNH
Very Large Array, New Mexico — CGP Grey, CC BY 2.0
qua Wikimedia Commons
Giấy phép: creativecommons.org/licenses/by/2.0
Tất cả các hình ảnh lưu trữ khác: NASA, NASA/JPL, NASA/JPL-Caltech, NASA/GRC, phạm vi công cộng.
```

## čeština (`cs`)

```
Jak Voyager posílal snímky domů?
```

```
V srpnu 1989 proletěl Voyager 2 kolem Neptunu, víc než 4 miliardy kilometrů od Země, a vyfotil ho. Jeho kamery byly postavené na televizních snímacích elektronkách navržených v sedmdesátých letech, bez paměťové karty a bez snímače, jaký mají dnešní telefony. A přesto dorazily tisíce snímků.

Příběh začíná 12 let před startem Voyageru, průletem sondy Mariner 4 kolem Marsu a prvním snímkem jiné planety zblízka, který inženýři v JPL ručně vybarvili pastely. Vede přes laboratoř Kodaku, kde Steven Sasson v roce 1975 sestavil úplně jiný druh fotoaparátu. A končí nejslavnějším snímkem, jaký kdy Voyager pořídil: Bledě modrou tečkou, kterou poslal domů ze vzdálenosti 6 miliard kilometrů.

Zdroje: Ludwig & Taylor, Voyager Telecommunications (JPL DESCANSO, 2002); PDS Rings Node, popis úzkoúhlé kamery Voyageru; J. Tomayko, Computers in Spaceflight (NASA CR-182505, 1988); B. A. Smith, Voyager Imaging Science Investigations (NASA, 1979); NSSDC, Mariner 4; Caltech Magazine, A Planet Painted by Hand; IEEE Spectrum, historie prvního digitálního fotoaparátu; NASA Photojournal PIA00451–PIA00453.

Titulky jsou psané pro tohle video, ne strojový přepis. Jako druhá zvuková stopa je k dispozici americká angličtina.

KAPITOLY
00:00 Kamera postavená na televizní elektronce
00:35 Mariner 4 u Marsu
01:32 Snímek vybarvený ručně
02:06 Fotoaparát v laboratoři Kodaku
03:10 Kamery Voyageru
04:17 Jak dostat snímky domů
05:04 Přestavba antén na Zemi
05:24 Nový software pro vzdálenou sondu
06:27 Byly to tedy digitální fotoaparáty?
06:55 Bledě modrá tečka
08:06 Jedenáct týdnů cesty domů

ZDROJE OBRÁZKŮ
Very Large Array, Nové Mexiko — CGP Grey, CC BY 2.0
přes Wikimedia Commons
Licence: creativecommons.org/licenses/by/2.0
Ostatní archivní snímky: NASA, NASA/JPL, NASA/JPL-Caltech, NASA/GRC, volná díla.
```

## español (`es`)

```
¿Cómo enviaba la Voyager sus fotos a casa?
```

```
En agosto de 1989, la Voyager 2 pasó junto a Neptuno, a más de 4000 millones de kilómetros de la Tierra, y le hizo fotos. Sus cámaras estaban construidas en torno a tubos de televisión diseñados en los años setenta, sin tarjeta de memoria ni un sensor como el de los móviles de hoy. Y aun así llegaron miles de fotos.

La historia empieza 12 años antes del lanzamiento de la Voyager, con el paso de la Mariner 4 junto a Marte y la primera imagen de cerca de otro planeta, que los ingenieros del JPL colorearon a mano con pasteles. Pasa por un laboratorio de Kodak, donde Steven Sasson construyó en 1975 una cámara muy distinta. Y termina con la foto más famosa que tomó nunca la Voyager: el Punto Azul Pálido, enviado a casa desde 6000 millones de kilómetros.

Fuentes: Ludwig & Taylor, Voyager Telecommunications (JPL DESCANSO, 2002); PDS Rings Node, descripción de la cámara de ángulo estrecho de la Voyager; J. Tomayko, Computers in Spaceflight (NASA CR-182505, 1988); B. A. Smith, Voyager Imaging Science Investigations (NASA, 1979); NSSDC, Mariner 4; Caltech Magazine, A Planet Painted by Hand; IEEE Spectrum, historia de la primera cámara digital; NASA Photojournal PIA00451–PIA00453.

Los subtítulos están escritos para este vídeo, no generados automáticamente. Como segunda pista de audio está disponible el inglés americano.

CAPÍTULOS
00:00 Una cámara construida en torno a un tubo de televisión
00:35 La Mariner 4 en Marte
01:32 Una imagen coloreada a mano
02:06 Una cámara en un laboratorio de Kodak
03:10 Las cámaras de la Voyager
04:17 Cómo traer las fotos a casa
05:04 Reconstruir las antenas en la Tierra
05:24 Software nuevo para una sonda lejana
06:27 Entonces, ¿eran cámaras digitales?
06:55 El Punto Azul Pálido
08:06 Once semanas para volver a casa

CRÉDITOS DE LAS IMÁGENES
Very Large Array, Nuevo México — CGP Grey, CC BY 2.0
vía Wikimedia Commons
Licencia: creativecommons.org/licenses/by/2.0
Todas las demás imágenes de archivo: NASA, NASA/JPL, NASA/JPL-Caltech, NASA/GRC, dominio público.
```

## svenska (`sv`)

```
Hur skickade Voyager hem bilder?
```

```
I augusti 1989 flög Voyager 2 förbi Neptunus, mer än 4 miljarder kilometer från jorden, och fotograferade den. Dess kameror var byggda kring tv-kamerarör som konstruerats på 1970-talet, utan minneskort och utan en sensor som den i dagens mobiler. Ändå kom det fram tusentals bilder.

Berättelsen börjar 12 år före Voyagers uppskjutning, med Mariner 4 vid Mars och den första närbilden av en annan planet, som ingenjörerna på JPL färglade för hand med pastellkritor. Den går via ett labb hos Kodak, där Steven Sasson 1975 byggde en helt annan sorts kamera. Och den slutar med den mest berömda bild som Voyager någonsin tog: Pale Blue Dot, skickad hem från 6 miljarder kilometers avstånd.

Källor: Ludwig & Taylor, Voyager Telecommunications (JPL DESCANSO, 2002); PDS Rings Node, beskrivning av Voyagers smalvinkelkamera; J. Tomayko, Computers in Spaceflight (NASA CR-182505, 1988); B. A. Smith, Voyager Imaging Science Investigations (NASA, 1979); NSSDC, Mariner 4; Caltech Magazine, A Planet Painted by Hand; IEEE Spectrum, historien om den första digitalkameran; NASA Photojournal PIA00451–PIA00453.

Undertexterna är skrivna för den här videon, inte automatgenererade. Som andra ljudspår finns amerikansk engelska.

KAPITEL
00:00 En kamera byggd kring ett tv-rör
00:35 Mariner 4 vid Mars
01:32 En bild färglagd för hand
02:06 En kamera i ett labb hos Kodak
03:10 Voyagers kameror
04:17 Att få hem bilderna
05:04 Antennerna på jorden byggs om
05:24 Ny mjukvara för en avlägsen rymdsond
06:27 Var de alltså digitalkameror?
06:55 Pale Blue Dot
08:06 Elva veckor på väg hem

BILDKÄLLOR
Very Large Array, New Mexico — CGP Grey, CC BY 2.0
via Wikimedia Commons
Licens: creativecommons.org/licenses/by/2.0
Alla andra arkivbilder: NASA, NASA/JPL, NASA/JPL-Caltech, NASA/GRC, fria från upphovsrätt (public domain).
```
