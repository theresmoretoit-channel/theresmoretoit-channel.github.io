# Lokalizované názvy a popisy — 047

Nahrává `tools/lokalizace.py` přes `videos.update(part="localizations")`.
Anglický titul a popis zůstávají v `youtube.md` a posílají se zpátky
beze změny.

```bash
python tools/lokalizace.py videos/047-how-did-5mb-become-terabytes --zkouska
python tools/lokalizace.py videos/047-how-did-5mb-become-terabytes
```

**Formát si vynucuje parser** (`bloky_z_podkladu()`): sekce jazyka je
nadpis `## <endonymum> (`<kód>`)`, uvnitř **přesně dva bloky** v trojici
zpětných apostrofů — první titul, druhý popis. Jiný počet nástroj
přeskočí s hláškou a jinak to nekřičí.

**Pořadí je podle YouTube Studia**, tedy bajtově podle UTF-8 a podle
ČESKÉHO názvu jazyka, ne abecedně podle kódu.

## Co se NEPŘEKLÁDÁ

- **vlastní jména** — IBM, RAMAC, Winchester, Samsung, Albert Fert,
  Peter Grünberg, Norsk Teknisk Museum
- **názvy archivních snímků** v kreditech — jsou to identifikátory
  souborů na Wikimedia Commons
- **časy kapitol** na vteřinu — jsou to tytéž okamžiky ve všech jazycích
- **tagy** — YouTube je per-jazyk nemá

Popisek kreditů (`IMAGE CREDITS`, `Licences:`) se naopak **překládá**,
stejně jako u videa 038.

## Kontrola čísel

Video má čísla přes miliardu, takže past s *billion* (10⁹) a *trillion*
(10¹²) tu hrozí naplno. Každé se přepočítalo, ne přepsalo:

| anglicky | co to je | pozor |
|---|---|---|
| five megabytes | 5 MB | |
| ten million times | 10 000 000× | |
| a thousand times lighter | 1 000× | |
| a billion times denser | 10⁹× | de `Milliarde`, es `mil millones`, pt-BR `bilhão`, fr `milliard`, it `miliardo`, fi `miljardi`, sv `miljard`, pl `miliard` |
| three hundred bits / cm² | 300 | |
| nearly three hundred billion | 3 × 10¹¹ | es `trescientos mil millones`, fr `trois cents milliards`, de `dreihundert Milliarden` |
| fifteen billion bits / cm² | 1,5 × 10¹⁰ | |
| twenty micrometres | 20 µm | |
| sixty centimetres | 60 cm | |
| two hundred kilograms | 200 kg | |
| four hundred and fifty degrees | 450 °C | |
| twenty-four layers | 24 | |
| more than nine tenths | > 9/10 | |

## suomi (`fi`)

```
Miten 5 megatavusta tuli teratavuja?
```

```
Vuonna 1956 IBM toimitti ensimmäisen kiintolevyn. Siihen mahtui noin viisi megatavua — yksi valokuva nykyisestä puhelimesta — ja kompressorin kanssa, joka piti sen käynnissä, se painoi yli tonnin.

Ilmeinen selitys on, että opimme rakentamaan pienempiä koneita. Selitys on totta ja se on se tylsä puolisko. Kone keveni noin tuhatkertaisesti. Tallennustiheys kasvoi noin miljardikertaiseksi. Kaikki kiinnostava tallennuksessa piilee tuossa erossa.

Vuoden 1956 levyllä yhdelle neliösentille mahtui kolmesataa bittiä. Nykylevy saa samalle neliösentille lähes kolmesataa miljardia. Tämä video kertoo, miten se tapahtui: pää, jonka piti lentää koskettamatta, kompressori joka katosi kun pää muotoiltiin siiveksi, vuonna 1988 kahdessa laboratoriossa toisistaan riippumatta löydetty ilmiö joka teki heikoista signaaleista luettavia, ja seinä joka tuli vastaan kun magneettinen rae oli tarpeeksi pieni kääntyäkseen huoneenlämmössä itsestään.

Ja sitten se osa, jossa alan molemmat puoliskot päätyvät samaan liikkeeseen. Kun bitti ei voinut enää pienentyä, bitti nostettiin pystyyn. Kun flash-solu ei voinut enää pienentyä, solut pinottiin. Eri aineet, eri fysiikka, eri yritykset — ja sama siirto.

Tekstitykset on kirjoitettu tätä videota varten, ei luotu automaattisesti. Toisena ääniraitana on amerikanenglanti.

Koko teksti, lähteet ja käännökset: https://theresmoretoit-channel.github.io/fi/videos/how-did-5mb-become-terabytes/

Luvut
00:00 Kone joka painoi tonnin
00:27 Tuhat vastaan miljardi
00:57 Nauha on jono
01:24 Viisikymmentä levyä, kaksikymmentä kierrosta sekunnissa
01:42 Pää ei saa koskettaa
02:14 Mitä viisi megatavua oikeasti oli
02:32 Kolmesataa bittiä
02:50 Kompressori katoaa
03:24 Mikä bitti oikeastaan on
03:59 Signaali käy liian heikoksi
04:14 Fert ja Grünberg
05:02 Miljardi kertaa
05:30 Seinä
06:04 Atomit loppuvat
06:30 Bitit nostetaan pystyyn
07:12 Laser lukupäässä
07:50 Poistetaan levy kokonaan
08:29 Flash törmää omaan seinäänsä
09:14 Sama vastaus
09:57 Vanha tekniikka muutti
10:15 Me rakensimme ylöspäin

KUVALÄHTEET
IBM 305 RAMAC system (2) — Norsk Teknisk Museum, CC BY-SA 4.0
via Wikimedia Commons
Lisenssit: creativecommons.org/licenses/by-sa/4.0
```

## français (`fr`)

```
Comment 5 Mo sont-ils devenus des téraoctets ?
```

```
En 1956, IBM livrait le premier disque dur. Il contenait environ cinq mégaoctets — une seule photo prise avec un téléphone d'aujourd'hui — et avec le compresseur qui le faisait fonctionner, il pesait plus d'une tonne.

L'explication évidente, c'est qu'on a appris à construire des machines plus petites. Elle est vraie, et c'est la moitié ennuyeuse. La machine est devenue environ mille fois plus légère. Le stockage est devenu environ un milliard de fois plus dense. Tout ce qui est intéressant dans le stockage se cache dans cet écart.

Sur le disque livré en 1956, un centimètre carré contenait trois cents bits. Un disque actuel en met près de trois cents milliards sur le même centimètre carré. Cette vidéo raconte comment : la tête qui devait voler sans jamais toucher, le compresseur disparu le jour où on a donné à la tête la forme d'une aile, l'effet physique trouvé indépendamment par deux laboratoires en 1988 qui a rendu lisibles les signaux faibles, et le mur atteint quand un grain magnétique devient assez petit pour que la température ambiante le retourne toute seule.

Et puis la partie où les deux moitiés de l'industrie riment. Quand le bit n'a plus pu rapetisser, on l'a mis debout. Quand la cellule flash n'a plus pu rapetisser, on a empilé les cellules. Des matériaux différents, une physique différente, des entreprises différentes — et le même geste.

Les sous-titres sont écrits pour cette vidéo, pas générés automatiquement. Une piste audio en anglais américain est disponible en deuxième piste.

Transcription complète, sources et traductions : https://theresmoretoit-channel.github.io/fr/videos/how-did-5mb-become-terabytes/

Chapitres
00:00 La machine qui pesait une tonne
00:27 Mille contre un milliard
00:57 La bande est une file d'attente
01:24 Cinquante disques, vingt tours par seconde
01:42 La tête ne doit pas toucher
02:14 Ce qu'étaient vraiment les cinq mégaoctets
02:32 Trois cents bits
02:50 Le compresseur disparaît
03:24 Ce qu'est un bit, physiquement
03:59 Le signal devient trop faible
04:14 Fert et Grünberg
05:02 Un milliard de fois
05:30 Le mur
06:04 On manque d'atomes
06:30 Mettre les bits debout
07:12 Un laser dans la tête
07:50 Enlever le disque complètement
08:29 La flash heurte son propre mur
09:14 La même réponse
09:57 L'ancienne technologie a déménagé
10:15 On a construit vers le haut

CRÉDITS IMAGES
IBM 305 RAMAC system (2) — Norsk Teknisk Museum, CC BY-SA 4.0
via Wikimedia Commons
Licences : creativecommons.org/licenses/by-sa/4.0
```

## Bahasa Indonesia (`id`)

```
Bagaimana 5 MB Menjadi Terabita?
```

```
Pada 1956, IBM mengirimkan hard disk pertama. Kapasitasnya sekitar lima megabita — satu foto dari ponsel zaman sekarang — dan dengan kompresor yang membuatnya tetap jalan, beratnya lebih dari satu ton.

Penjelasan yang gampang: kita jadi lebih pandai membuat mesin kecil. Penjelasan itu benar, dan itu bagian yang membosankan. Mesinnya menjadi sekitar seribu kali lebih ringan. Kerapatan penyimpanannya naik sekitar satu miliar kali. Semua yang menarik soal penyimpanan bersembunyi di jarak itu.

Di piringan yang dikirim IBM pada 1956, satu sentimeter persegi memuat tiga ratus bit. Drive modern menaruh hampir tiga ratus miliar di sentimeter persegi yang sama. Video ini tentang bagaimana itu bisa terjadi: kepala yang harus terbang tanpa menyentuh, kompresor yang hilang ketika kepala dibentuk seperti sayap, efek fisika yang ditemukan dua laboratorium secara terpisah pada 1988 sehingga sinyal lemah bisa dibaca, dan tembok yang muncul saat satu butiran magnetik cukup kecil untuk dibalik oleh suhu ruangan sendiri.

Lalu bagian yang membuat kedua sisi industri ini berima. Ketika bit tidak bisa lebih kecil lagi, bitnya didirikan. Ketika sel flash tidak bisa lebih kecil lagi, selnya ditumpuk. Bahan berbeda, fisika berbeda, perusahaan berbeda — dan langkah yang sama.

Subtitel ditulis khusus untuk video ini, bukan hasil otomatis. Tersedia juga trek audio bahasa Inggris Amerika sebagai trek kedua.

Transkrip lengkap, sumber, dan terjemahan: https://theresmoretoit-channel.github.io/id/videos/how-did-5mb-become-terabytes/

Bab
00:00 Mesin seberat satu ton
00:27 Seribu lawan satu miliar
00:57 Pita itu antrean
01:24 Lima puluh piringan, dua puluh putaran per detik
01:42 Kepala tidak boleh menyentuh
02:14 Sebenarnya berapa lima megabita itu
02:32 Tiga ratus bit
02:50 Kompresor pun hilang
03:24 Sebenarnya bit itu apa
03:59 Sinyalnya jadi terlalu lemah
04:14 Fert dan Grünberg
05:02 Satu miliar kali
05:30 Temboknya
06:04 Kehabisan atom
06:30 Mendirikan bit
07:12 Laser di dalam kepala
07:50 Buang saja piringannya
08:29 Flash menabrak temboknya sendiri
09:14 Jawaban yang sama
09:57 Teknologi lama pindah tempat
10:15 Kita membangun ke atas

KREDIT GAMBAR
IBM 305 RAMAC system (2) — Norsk Teknisk Museum, CC BY-SA 4.0
via Wikimedia Commons
Lisensi: creativecommons.org/licenses/by-sa/4.0
```

## italiano (`it`)

```
Come sono diventati terabyte 5 MB?
```

```
Nel 1956 IBM consegnò il primo disco rigido. Conteneva circa cinque megabyte — una sola foto di un telefono di oggi — e con il compressore che lo teneva in funzione pesava più di una tonnellata.

La spiegazione ovvia è che abbiamo imparato a costruire macchine più piccole. È vera, ed è la metà noiosa. La macchina è diventata circa mille volte più leggera. La memoria è diventata circa un miliardo di volte più densa. Tutto ciò che è interessante nello storage si nasconde in quello scarto.

Sul disco consegnato nel 1956, un centimetro quadrato conteneva trecento bit. Un disco moderno ne mette quasi trecento miliardi nello stesso centimetro quadrato. Questo video racconta come: la testina che doveva volare senza toccare, il compressore sparito quando le hanno dato la forma di un'ala, l'effetto fisico trovato da due laboratori indipendentemente nel 1988 che ha reso leggibili i segnali deboli, e il muro arrivato quando un grano magnetico diventa abbastanza piccolo da essere ribaltato dalla temperatura ambiente.

E poi la parte in cui le due metà dell'industria fanno rima. Quando il bit non poteva più rimpicciolirsi, il bit è stato messo in piedi. Quando la cella flash non poteva più rimpicciolirsi, le celle sono state impilate. Materiali diversi, fisica diversa, aziende diverse — e la stessa mossa.

I sottotitoli sono scritti per questo video, non generati automaticamente. È disponibile una traccia audio in inglese americano come seconda traccia.

Trascrizione completa, fonti e traduzioni: https://theresmoretoit-channel.github.io/it/videos/how-did-5mb-become-terabytes/

Capitoli
00:00 La macchina che pesava una tonnellata
00:27 Mille contro un miliardo
00:57 Il nastro è una coda
01:24 Cinquanta dischi, venti giri al secondo
01:42 La testina non deve toccare
02:14 Che cosa erano davvero cinque megabyte
02:32 Trecento bit
02:50 Il compressore sparisce
03:24 Che cos'è un bit, fisicamente
03:59 Il segnale diventa troppo debole
04:14 Fert e Grünberg
05:02 Un miliardo di volte
05:30 Il muro
06:04 Stanno finendo gli atomi
06:30 Mettere i bit in piedi
07:12 Un laser nella testina
07:50 Togliere del tutto il disco
08:29 La flash sbatte contro il suo muro
09:14 La stessa risposta
09:57 La vecchia tecnologia si è spostata
10:15 Abbiamo costruito verso l'alto

CREDITI IMMAGINI
IBM 305 RAMAC system (2) — Norsk Teknisk Museum, CC BY-SA 4.0
via Wikimedia Commons
Licenze: creativecommons.org/licenses/by-sa/4.0
```

## Deutsch (`de`)

```
Wie wurden aus 5 MB Terabyte?
```

```
1956 lieferte IBM die erste Festplatte aus. Sie fasste etwa fünf Megabyte — ein einziges Foto aus einem heutigen Handy — und mit dem Kompressor, der sie am Laufen hielt, wog sie über eine Tonne.

Die naheliegende Erklärung lautet: Wir bauen inzwischen kleinere Maschinen. Sie stimmt, und sie ist die langweilige Hälfte. Die Maschine wurde ungefähr tausendmal leichter. Der Speicher wurde ungefähr eine Milliarde Mal dichter. Alles Interessante am Speichern steckt in dieser Lücke.

Auf der Platte von 1956 fasste ein Quadratzentimeter dreihundert Bit. Eine heutige Platte bringt fast dreihundert Milliarden auf denselben Quadratzentimeter. Dieses Video erzählt, wie das ging: der Kopf, der fliegen musste, ohne zu berühren, der Kompressor, der verschwand, als man den Kopf wie einen Flügel formte, der physikalische Effekt, den 1988 zwei Labore unabhängig voneinander fanden und der schwache Signale lesbar machte, und die Wand, die kam, als ein magnetisches Korn klein genug wurde, dass Zimmertemperatur es von allein umklappt.

Und dann der Teil, in dem sich beide Hälften der Branche reimen. Als das Bit nicht kleiner werden konnte, wurde das Bit aufgerichtet. Als die Flash-Zelle nicht kleiner werden konnte, wurden die Zellen gestapelt. Andere Materialien, andere Physik, andere Firmen — und derselbe Zug.

Die Untertitel sind für dieses Video geschrieben, nicht automatisch erzeugt. Eine amerikanisch-englische Tonspur steht als zweite Tonspur zur Verfügung.

Vollständiger Text, Quellen und Übersetzungen: https://theresmoretoit-channel.github.io/de/videos/how-did-5mb-become-terabytes/

Kapitel
00:00 Die Maschine, die eine Tonne wog
00:27 Tausend gegen eine Milliarde
00:57 Band ist eine Warteschlange
01:24 Fünfzig Scheiben, zwanzig Umdrehungen pro Sekunde
01:42 Der Kopf darf nicht berühren
02:14 Was fünf Megabyte wirklich waren
02:32 Dreihundert Bit
02:50 Der Kompressor verschwindet
03:24 Was ein Bit physikalisch ist
03:59 Das Signal wird zu schwach
04:14 Fert und Grünberg
05:02 Eine Milliarde Mal
05:30 Die Wand
06:04 Die Atome gehen aus
06:30 Die Bits aufrichten
07:12 Ein Laser im Kopf
07:50 Die Platte ganz weglassen
08:29 Flash läuft gegen die eigene Wand
09:14 Dieselbe Antwort
09:57 Die alte Technik zog um
10:15 Wir bauten nach oben

BILDNACHWEIS
IBM 305 RAMAC system (2) — Norsk Teknisk Museum, CC BY-SA 4.0
via Wikimedia Commons
Lizenzen: creativecommons.org/licenses/by-sa/4.0
```

## polski (`pl`)

```
Jak 5 MB stało się terabajtami?
```

```
W 1956 roku IBM dostarczył pierwszy dysk twardy. Mieściło się na nim około pięciu megabajtów — jedno zdjęcie z dzisiejszego telefonu — a razem ze sprężarką, która utrzymywała go w ruchu, ważył ponad tonę.

Nasuwa się wyjaśnienie, że nauczyliśmy się budować mniejsze maszyny. Jest prawdziwe i jest tą nudniejszą połową. Maszyna zrobiła się jakieś tysiąc razy lżejsza. Gęstość zapisu wzrosła jakieś miliard razy. Wszystko, co ciekawe w pamięci masowej, kryje się w tej różnicy.

Na talerzu z 1956 roku jeden centymetr kwadratowy mieścił trzysta bitów. Dzisiejszy dysk mieści prawie trzysta miliardów na tym samym centymetrze kwadratowym. Ten film jest o tym, jak do tego doszło: głowica, która musiała latać, nie dotykając, sprężarka, która zniknęła, gdy głowicy nadano kształt skrzydła, efekt fizyczny znaleziony niezależnie przez dwa laboratoria w 1988 roku, dzięki któremu słabe sygnały dało się odczytać, i ściana, która pojawiła się, gdy magnetyczne ziarno stało się na tyle małe, że przewraca je sama temperatura pokojowa.

A potem część, w której obie połowy branży się rymują. Kiedy bit nie mógł być mniejszy, postawiono go na sztorc. Kiedy komórka flash nie mogła być mniejsza, ułożono komórki w stos. Inne materiały, inna fizyka, inne firmy — i ten sam ruch.

Napisy są napisane do tego filmu, nie wygenerowane automatycznie. Dostępna jest też ścieżka dźwiękowa w amerykańskiej angielszczyźnie jako druga ścieżka.

Pełna transkrypcja, źródła i tłumaczenia: https://theresmoretoit-channel.github.io/pl/videos/how-did-5mb-become-terabytes/

Rozdziały
00:00 Maszyna, która ważyła tonę
00:27 Tysiąc kontra miliard
00:57 Taśma to kolejka
01:24 Pięćdziesiąt talerzy, dwadzieścia obrotów na sekundę
01:42 Głowica nie może dotknąć
02:14 Czym naprawdę było pięć megabajtów
02:32 Trzysta bitów
02:50 Sprężarka znika
03:24 Czym właściwie jest bit
03:59 Sygnał robi się za słaby
04:14 Fert i Grünberg
05:02 Miliard razy
05:30 Ściana
06:04 Kończą się atomy
06:30 Bity na sztorc
07:12 Laser w głowicy
07:50 Wyjąć talerz w całości
08:29 Flash uderza we własną ścianę
09:14 Ta sama odpowiedź
09:57 Stara technologia się przeprowadziła
10:15 Zaczęliśmy budować w górę

ŹRÓDŁA ZDJĘĆ
IBM 305 RAMAC system (2) — Norsk Teknisk Museum, CC BY-SA 4.0
via Wikimedia Commons
Licencje: creativecommons.org/licenses/by-sa/4.0
```

## português (Brasil) (`pt-BR`)

```
Como 5 MB viraram terabytes?
```

```
Em 1956, a IBM entregou o primeiro disco rígido. Ele guardava cerca de cinco megabytes — uma única foto de um celular de hoje — e com o compressor que o mantinha funcionando, pesava mais de uma tonelada.

A explicação óbvia é que aprendemos a construir máquinas menores. Ela é verdadeira e é a metade chata. A máquina ficou cerca de mil vezes mais leve. O armazenamento ficou cerca de um bilhão de vezes mais denso. Tudo o que é interessante em armazenamento está escondido nessa diferença.

No disco entregue em 1956, um centímetro quadrado guardava trezentos bits. Um disco moderno põe quase trezentos bilhões no mesmo centímetro quadrado. Este vídeo é sobre como isso aconteceu: a cabeça que precisava voar sem encostar, o compressor que sumiu quando deram à cabeça o formato de uma asa, o efeito físico encontrado por dois laboratórios de forma independente em 1988 e que tornou legíveis os sinais fracos, e a parede que apareceu quando um grão magnético ficou pequeno o bastante para a temperatura ambiente virá-lo sozinha.

E depois a parte em que as duas metades da indústria rimam. Quando o bit não pôde ficar menor, o bit foi posto em pé. Quando a célula flash não pôde ficar menor, as células foram empilhadas. Materiais diferentes, física diferente, empresas diferentes — e o mesmo movimento.

As legendas foram escritas para este vídeo, não geradas automaticamente. Há também uma faixa de áudio em inglês americano como segunda faixa.

Transcrição completa, fontes e traduções: https://theresmoretoit-channel.github.io/pt-br/videos/how-did-5mb-become-terabytes/

Capítulos
00:00 A máquina que pesava uma tonelada
00:27 Mil contra um bilhão
00:57 Fita é uma fila
01:24 Cinquenta discos, vinte voltas por segundo
01:42 A cabeça não pode encostar
02:14 O que eram de verdade os cinco megabytes
02:32 Trezentos bits
02:50 O compressor some
03:24 O que é um bit, fisicamente
03:59 O sinal fica fraco demais
04:14 Fert e Grünberg
05:02 Um bilhão de vezes
05:30 A parede
06:04 Ficando sem átomos
06:30 Pondo os bits em pé
07:12 Um laser na cabeça
07:50 Tirar o disco por completo
08:29 A flash bate na própria parede
09:14 A mesma resposta
09:57 A tecnologia antiga mudou de lugar
10:15 A gente construiu para cima

CRÉDITOS DAS IMAGENS
IBM 305 RAMAC system (2) — Norsk Teknisk Museum, CC BY-SA 4.0
via Wikimedia Commons
Licenças: creativecommons.org/licenses/by-sa/4.0
```

## Türkçe (`tr`)

```
5 MB Nasıl Terabaytlara Dönüştü?
```

```
1956'da IBM ilk sabit diski teslim etti. İçine yaklaşık beş megabayt sığıyordu — bugünün telefonuyla çekilmiş tek bir fotoğraf kadar — ve onu çalışır tutan kompresörle birlikte bir tondan fazla geliyordu.

Akla ilk gelen açıklama, küçük makineler yapmayı öğrendiğimiz. Bu doğru ve işin sıkıcı yarısı. Makine yaklaşık bin kat hafifledi. Depolama ise yaklaşık bir milyar kat yoğunlaştı. Depolamayla ilgili ilginç olan her şey bu farkta saklı.

1956'da teslim edilen diskte bir santimetrekareye üç yüz bit sığıyordu. Modern bir disk aynı santimetrekareye neredeyse üç yüz milyar koyuyor. Bu video bunun nasıl olduğunu anlatıyor: değmeden uçmak zorunda olan kafa, kafaya kanat biçimi verildiğinde ortadan kalkan kompresör, 1988'de iki laboratuvarın birbirinden bağımsız bulduğu ve zayıf sinyalleri okunur kılan fiziksel etki, ve manyetik tanecik oda sıcaklığının onu kendiliğinden çevirebileceği kadar küçüldüğünde gelen duvar.

Sonra da sektörün iki yarısının aynı kafiyeye düştüğü kısım. Bit daha fazla küçülemeyince bit dik durduruldu. Flash hücresi daha fazla küçülemeyince hücreler üst üste yığıldı. Farklı malzemeler, farklı fizik, farklı şirketler — ve aynı hamle.

Altyazılar bu video için yazıldı, otomatik olarak oluşturulmadı. İkinci ses parçası olarak Amerikan İngilizcesi mevcut.

Metnin tamamı, kaynaklar ve çeviriler: https://theresmoretoit-channel.github.io/tr/videos/how-did-5mb-become-terabytes/

Bölümler
00:00 Bir ton ağırlığındaki makine
00:27 Bine karşı bir milyar
00:57 Bant bir kuyruktur
01:24 Elli disk, saniyede yirmi devir
01:42 Kafa değmemeli
02:14 Beş megabayt aslında neydi
02:32 Üç yüz bit
02:50 Kompresör gidiyor
03:24 Bit fiziksel olarak nedir
03:59 Sinyal fazla zayıflıyor
04:14 Fert ve Grünberg
05:02 Bir milyar kat
05:30 Duvar
06:04 Atomlar tükeniyor
06:30 Bitleri dik durdurmak
07:12 Kafanın içinde bir lazer
07:50 Diski tamamen çıkarmak
08:29 Flash kendi duvarına tosluyor
09:14 Aynı cevap
09:57 Eski teknoloji yer değiştirdi
10:15 Yukarı doğru inşa ettik

GÖRSEL KAYNAKLARI
IBM 305 RAMAC system (2) — Norsk Teknisk Museum, CC BY-SA 4.0
via Wikimedia Commons
Lisanslar: creativecommons.org/licenses/by-sa/4.0
```

## українська (`uk`)

```
Як 5 МБ стали терабайтами?
```

```
У 1956 році IBM випустила перший жорсткий диск. На нього вміщалося близько п'яти мегабайтів — одна фотографія із сучасного телефона — а разом із компресором, без якого він не працював, він важив понад тонну.

Очевидне пояснення: ми навчилися будувати менші машини. Воно правдиве і воно ж є нудною половиною. Машина стала приблизно в тисячу разів легшою. Щільність запису зросла приблизно в мільярд разів. Усе цікаве про зберігання даних ховається саме в цьому розриві.

На пластині 1956 року один квадратний сантиметр вміщав триста бітів. Сучасний диск кладе на той самий квадратний сантиметр майже триста мільярдів. Це відео про те, як так сталося: головка, яка мусила летіти, не торкаючись, компресор, що зник, коли головці надали форму крила, фізичний ефект, який 1988 року незалежно знайшли дві лабораторії і завдяки якому слабкі сигнали стало можливо читати, і стіна, що прийшла, коли магнітне зерно стало достатньо малим, щоб кімнатна температура перевертала його сама.

А далі частина, у якій обидві половини галузі римуються. Коли біт уже не міг стати меншим, біт поставили сторч. Коли комірка флеш-пам'яті вже не могла стати меншою, комірки склали у стос. Інші матеріали, інша фізика, інші компанії — і той самий хід.

Субтитри написані саме для цього відео, а не згенеровані автоматично. Другою звуковою доріжкою доступна американська англійська.

Повний текст, джерела та переклади: https://theresmoretoit-channel.github.io/uk/videos/how-did-5mb-become-terabytes/

Розділи
00:00 Машина, що важила тонну
00:27 Тисяча проти мільярда
00:57 Стрічка — це черга
01:24 П'ятдесят пластин, двадцять обертів за секунду
01:42 Головка не має торкатися
02:14 Чим насправді були п'ять мегабайтів
02:32 Триста бітів
02:50 Компресор зникає
03:24 Що таке біт фізично
03:59 Сигнал стає надто слабким
04:14 Фер і Ґрюнберг
05:02 У мільярд разів
05:30 Стіна
06:04 Закінчуються атоми
06:30 Ставимо біти сторч
07:12 Лазер у головці
07:50 Прибрати диск узагалі
08:29 Флеш упирається у власну стіну
09:14 Та сама відповідь
09:57 Стара технологія переїхала
10:15 Ми почали будувати вгору

ДЖЕРЕЛА ЗОБРАЖЕНЬ
IBM 305 RAMAC system (2) — Norsk Teknisk Museum, CC BY-SA 4.0
via Wikimedia Commons
Ліцензії: creativecommons.org/licenses/by-sa/4.0
```

## Tiếng Việt (`vi`)

```
5 MB đã trở thành terabyte như thế nào?
```

```
Năm 1956, IBM giao chiếc ổ cứng đầu tiên. Nó chứa được khoảng năm megabyte — đúng một tấm ảnh chụp bằng điện thoại ngày nay — và cùng với máy nén khí giữ cho nó chạy được, nó nặng hơn một tấn.

Lời giải thích hiển nhiên là chúng ta đã giỏi hơn trong việc làm máy nhỏ. Điều đó đúng, và đó là nửa phần nhàm chán. Cỗ máy nhẹ đi khoảng một nghìn lần. Mật độ lưu trữ tăng khoảng một tỷ lần. Mọi thứ thú vị của chuyện lưu trữ đều nằm trong khoảng cách đó.

Trên chiếc đĩa của năm 1956, một centimet vuông chứa được ba trăm bit. Ổ đĩa hiện đại nhét gần ba trăm tỷ bit vào đúng một centimet vuông ấy. Video này kể chuyện đó đã diễn ra thế nào: cái đầu từ phải bay mà không được chạm, cái máy nén khí biến mất khi người ta tạo hình đầu từ giống một cánh máy bay, hiệu ứng vật lý mà hai phòng thí nghiệm tìm ra độc lập với nhau năm 1988 khiến tín hiệu yếu đọc được, và bức tường xuất hiện khi một hạt từ đủ nhỏ để chính nhiệt độ phòng lật ngược nó.

Rồi tới phần mà cả hai nửa của ngành này gieo cùng một vần. Khi bit không thể nhỏ hơn nữa, người ta dựng đứng bit lên. Khi ô nhớ flash không thể nhỏ hơn nữa, người ta xếp chồng các ô. Vật liệu khác nhau, vật lý khác nhau, công ty khác nhau — và cùng một nước đi.

Phụ đề được viết riêng cho video này, không phải tạo tự động. Có thêm một bản âm thanh tiếng Anh Mỹ làm bản âm thanh thứ hai.

Toàn văn, nguồn và bản dịch: https://theresmoretoit-channel.github.io/vi/videos/how-did-5mb-become-terabytes/

Các phần
00:00 Cỗ máy nặng một tấn
00:27 Một nghìn so với một tỷ
00:57 Băng từ là một hàng chờ
01:24 Năm mươi đĩa, hai mươi vòng mỗi giây
01:42 Đầu từ không được chạm
02:14 Năm megabyte thật ra là bao nhiêu
02:32 Ba trăm bit
02:50 Máy nén khí biến mất
03:24 Xét về vật lý, bit là gì
03:59 Tín hiệu trở nên quá yếu
04:14 Fert và Grünberg
05:02 Gấp một tỷ lần
05:30 Bức tường
06:04 Sắp cạn nguyên tử
06:30 Dựng đứng các bit
07:12 Một tia laser trong đầu từ
07:50 Bỏ hẳn cái đĩa đi
08:29 Flash đâm vào bức tường của chính nó
09:14 Vẫn là câu trả lời ấy
09:57 Công nghệ cũ chuyển chỗ
10:15 Chúng ta xây lên cao

NGUỒN HÌNH ẢNH
IBM 305 RAMAC system (2) — Norsk Teknisk Museum, CC BY-SA 4.0
via Wikimedia Commons
Giấy phép: creativecommons.org/licenses/by-sa/4.0
```

## čeština (`cs`)

```
Jak se z 5 MB staly terabajty?
```

```
V roce 1956 dodalo IBM první pevný disk. Vešlo se do něj asi pět megabajtů — jedna fotka z dnešního mobilu — a s kompresorem, bez kterého nefungoval, vážil přes tunu.

Nabízí se vysvětlení, že jsme se naučili stavět menší stroje. Je pravdivé a je to ta nudnější půlka. Stroj byl asi tisíckrát lehčí. Hustota záznamu vzrostla asi miliardakrát. Všechno zajímavé na ukládání dat se skrývá v té mezeře.

Na plotně z roku 1956 se na čtvereční centimetr vešlo tři sta bitů. Dnešní disk jich na týž čtvereční centimetr dostane skoro tři sta miliard. Tohle video je o tom, jak se to stalo: hlava, která musela létat a nesměla se dotknout, kompresor, který zmizel, jakmile hlava dostala tvar křídla, fyzikální jev, který v roce 1988 nezávisle našly dvě laboratoře a díky němuž šly slabé signály přečíst, a zeď, která přišla ve chvíli, kdy je magnetické zrno tak malé, že ho převrátí sama pokojová teplota.

A pak část, ve které se obě poloviny oboru rýmují. Když nešlo bit dál zmenšovat, postavil se nastojato. Když nešla dál zmenšovat flashová buňka, začaly se buňky vrstvit. Jiné materiály, jiná fyzika, jiné firmy — a tentýž tah.

Titulky jsou k tomuhle videu napsané, ne strojově vygenerované. Jako druhá zvuková stopa je k dispozici americká angličtina.

Celý text, zdroje a překlady: https://theresmoretoit-channel.github.io/cs/videos/how-did-5mb-become-terabytes/

Kapitoly
00:00 Stroj, který vážil tunu
00:27 Tisíc proti miliardě
00:57 Páska je fronta
01:24 Padesát ploten, dvacet otáček za sekundu
01:42 Hlava se nesmí dotknout
02:14 Kolik bylo pět megabajtů doopravdy
02:32 Tři sta bitů
02:50 Kompresor mizí
03:24 Co je vlastně bit
03:59 Signál je příliš slabý
04:14 Fert a Grünberg
05:02 Miliardakrát
05:30 Zeď
06:04 Docházejí atomy
06:30 Bity nastojato
07:12 Laser v hlavě
07:50 Vyhodit plotnu úplně
08:29 Flash naráží do vlastní zdi
09:14 Tatáž odpověď
09:57 Stará technologie se přestěhovala
10:15 Začali jsme stavět nahoru

ZDROJE OBRÁZKŮ
IBM 305 RAMAC system (2) — Norsk Teknisk Museum, CC BY-SA 4.0
via Wikimedia Commons
Licence: creativecommons.org/licenses/by-sa/4.0
```

## español (`es`)

```
¿Cómo 5 MB se convirtieron en terabytes?
```

```
En 1956, IBM entregó el primer disco duro. Guardaba unos cinco megabytes — una sola foto de un móvil de hoy — y con el compresor que lo mantenía en marcha pesaba más de una tonelada.

La explicación obvia es que aprendimos a construir máquinas más pequeñas. Es cierta y es la mitad aburrida. La máquina se volvió unas mil veces más ligera. El almacenamiento se volvió unos mil millones de veces más denso. Todo lo interesante del almacenamiento se esconde en esa diferencia.

En el disco entregado en 1956, un centímetro cuadrado guardaba trescientos bits. Un disco moderno mete casi trescientos mil millones en ese mismo centímetro cuadrado. Este vídeo cuenta cómo pasó: el cabezal que tenía que volar sin tocar, el compresor que desapareció cuando le dieron al cabezal forma de ala, el efecto físico que dos laboratorios encontraron por separado en 1988 y que hizo legibles las señales débiles, y el muro que llegó cuando un grano magnético se hace tan pequeño que la temperatura ambiente lo voltea sola.

Y luego la parte en la que las dos mitades de la industria riman. Cuando el bit ya no pudo ser más pequeño, se puso de pie. Cuando la celda flash ya no pudo ser más pequeña, se apilaron las celdas. Materiales distintos, física distinta, empresas distintas — y el mismo movimiento.

Los subtítulos están escritos para este vídeo, no generados automáticamente. Hay una pista de audio en inglés americano como segunda pista.

Transcripción completa, fuentes y traducciones: https://theresmoretoit-channel.github.io/es/videos/how-did-5mb-become-terabytes/

Capítulos
00:00 La máquina que pesaba una tonelada
00:27 Mil contra mil millones
00:57 La cinta es una cola
01:24 Cincuenta discos, veinte vueltas por segundo
01:42 El cabezal no puede tocar
02:14 Qué eran de verdad los cinco megabytes
02:32 Trescientos bits
02:50 El compresor desaparece
03:24 Qué es un bit, físicamente
03:59 La señal se vuelve demasiado débil
04:14 Fert y Grünberg
05:02 Mil millones de veces
05:30 El muro
06:04 Se acaban los átomos
06:30 Poner los bits de pie
07:12 Un láser en el cabezal
07:50 Quitar el disco del todo
08:29 La flash choca contra su propio muro
09:14 La misma respuesta
09:57 La tecnología vieja se mudó
10:15 Construimos hacia arriba

CRÉDITOS DE IMAGEN
IBM 305 RAMAC system (2) — Norsk Teknisk Museum, CC BY-SA 4.0
via Wikimedia Commons
Licencias: creativecommons.org/licenses/by-sa/4.0
```

## svenska (`sv`)

```
Hur blev 5 MB till terabyte?
```

```
1956 levererade IBM den första hårddisken. Den rymde ungefär fem megabyte — ett enda foto från en dagens telefon — och med kompressorn som höll den igång vägde den över ett ton.

Den självklara förklaringen är att vi blev bättre på att bygga små maskiner. Den stämmer, och den är den tråkiga halvan. Maskinen blev ungefär tusen gånger lättare. Lagringen blev ungefär en miljard gånger tätare. Allt som är intressant med lagring gömmer sig i det gapet.

På skivan från 1956 rymde en kvadratcentimeter trehundra bitar. En modern disk får in nästan trehundra miljarder på samma kvadratcentimeter. Den här videon handlar om hur det gick till: huvudet som måste flyga utan att röra, kompressorn som försvann när huvudet formades som en vinge, den fysikaliska effekt som två laboratorier hittade oberoende av varandra 1988 och som gjorde svaga signaler läsbara, och väggen som kom när ett magnetiskt korn blir litet nog för att rumstemperatur ska vända på det av sig självt.

Och sedan delen där branschens båda halvor rimmar. När biten inte kunde bli mindre ställdes biten upprätt. När flashcellen inte kunde bli mindre staplades cellerna. Olika material, olika fysik, olika företag — och samma drag.

Undertexterna är skrivna för den här videon, inte automatgenererade. Ett amerikanskt engelskt ljudspår finns som andra ljudspår.

Hela texten, källor och översättningar: https://theresmoretoit-channel.github.io/sv/videos/how-did-5mb-become-terabytes/

Kapitel
00:00 Maskinen som vägde ett ton
00:27 Tusen mot en miljard
00:57 Band är en kö
01:24 Femtio skivor, tjugo varv i sekunden
01:42 Huvudet får inte röra
02:14 Vad fem megabyte egentligen var
02:32 Trehundra bitar
02:50 Kompressorn försvinner
03:24 Vad en bit egentligen är
03:59 Signalen blir för svag
04:14 Fert och Grünberg
05:02 En miljard gånger
05:30 Väggen
06:04 Atomerna tar slut
06:30 Att ställa bitarna upprätt
07:12 En laser i huvudet
07:50 Ta bort skivan helt
08:29 Flash går in i sin egen vägg
09:14 Samma svar
09:57 Den gamla tekniken flyttade
10:15 Vi byggde uppåt

BILDKÄLLOR
IBM 305 RAMAC system (2) — Norsk Teknisk Museum, CC BY-SA 4.0
via Wikimedia Commons
Licenser: creativecommons.org/licenses/by-sa/4.0
```
