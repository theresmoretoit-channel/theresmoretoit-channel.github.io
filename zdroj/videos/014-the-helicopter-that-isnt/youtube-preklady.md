# Lokalizované názvy a popisy — The Gyroplane

Podklad pro **YouTube Studio → video → Podrobnosti → Přidat jazyk**.
Pro každý jazyk jsou tu **dva bloky ke zkopírování**: název a popis.
Platí totéž pravidlo jako u `youtube.md` — **kopíruje se celý blok mezi
trojicí zpětných apostrofů**, co je mimo něj, je poznámka pro agenta.

Anglický originál se nesahá; ten zůstane v `youtube.md`.

> **Proč to má smysl zrovna u tohohle videa:** je to jediné video kanálu,
> které lidi skutečně **hledají** — `gyrocopter` (4 zhlédnutí) a `gyroplane`
> (2) jsou dva ze tří nejčastějších vyhledávaných výrazů celého kanálu.
> Německy se ten stroj jmenuje **Tragschrauber**, česky **vírník**,
> polsky **wiatrakowiec** — a na žádné z těch slov se dnes video najít nedá,
> protože v žádném poli není.

## Jazyky se řadí v pořadí YouTube Studia

**Francouzština, italština, němčina, polština, portugalština (Brazílie),
čeština, španělština, švédština.** Uživatel prochází Studio jazyk po jazyku
shora dolů, takže soubor v jiném pořadí ho nutí skákat.

Není to abeceda — Studio řadí **bajtově podle UTF-8**, takže nediakritické
názvy jdou první (F, I, N, P, P) a teprve za nimi Č a Š. Odvodit to jde
strojově: `sorted(nazvy, key=lambda x: x.encode("utf-8"))`.

> **Tenhle soubor to pořadí NEMÁ** — vznikl dřív, než se na to přišlo,
> a přerovnávat hotovou práci nemá cenu. Platí od dalšího videa.

## Co se NEPŘEKLÁDÁ

| | |
|---|---|
| **jména autorů a názvy děl** v obrazových zdrojích | atribuce je licenční povinnost, mění se jen nadpis sekce |
| **kódy licencí** (`CC BY-SA 2.0`) a odkazy na creativecommons.org | totéž |
| **časy kapitol** | musí sedět na vteřinu, jinak je YouTube neuzná |
| **tagy** | YouTube je per-jazyk nemá |

Slogan a názvy jazyků v řádku o titulcích se naopak **překládají**
(rozhodnuto 2026-09-05). Slogan je narážka na název kanálu, ne logo —
kdo ji nepřečte, přijde o pointu, a název kanálu zůstává anglicky všude,
takže značka se neztratí. A smíšený seznam endonym uprostřed českého
odstavce čte jako nedotažený překlad.

> **Atribuce musí být v každém jazyce.** Lokalizovaný popis ten anglický
> **nahrazuje**, ne doplňuje — takže bez obrazových zdrojů v českém bloku
> by český divák u snímků pod CC BY-SA neviděl žádnou atribuci. Je to
> táž chyba, která už jednou nastala u čtyř videí, jen o patro dál.

---

## suomi (`fi`)

```
Autogyro — helikopteri, joka ei ole helikopteri
```

```
Sen päällä on iso roottori. Se nousee ja laskeutuu yllättävän pienessä tilassa. Ja jos moottori sammuu ilmassa, se osaa silti laskeutua itse.

Kuulostaa helikopterilta. Ei ole — koska moottori ei pyöritä roottoria lainkaan. Ilma pyörittää.

Tässä videossa selvitetään: miksi roottori pyörii, vaikka mikään ei käytä sitä, miksi runko ei pyöri sen mukana, miksi kone ei osaa leijua paikallaan, ja miksi muutama niistä pystyy silti ponnahtamaan maasta ilman minkäänlaista kiitoa. Lisäksi se osa, jonka useimmat ymmärtävät väärin — autogyro on kolmetoista vuotta VANHEMPI kuin käyttökelpoinen helikopteri, ja se maksaa murto-osan siitä.

Luvut
00:00 Kone, joka näyttää helikopterilta
00:31 Miten helikopteri tekee sen
00:57 Täysin erillinen potkuri
01:20 Miksi ilma pyörittää roottoria?
02:26 Mitä vapaa roottori maksaa
02:45 Miksi runko ei pyöri
03:45 Se ei osaa leijua
04:28 Hyppylähtö
05:20 Kun moottori sammuu
06:07 Sekin voi joutua onnettomuuteen
06:37 Vanhempi kuin helikopteri
07:21 Yllättävän edullinen
08:18 Miksi kaikki eivät siis lennä sellaisella?
08:56 Ei halpa helikopteri — jotain muuta

Tekstitykset on kirjoitettu tätä videota varten, ei luotu automaattisesti. Toisena ääniraitana on amerikanenglanti.

Siinä on enemmänkin.

KUVALÄHTEET
Autogyro МТО-Sport and photographer in flight — Aleksandr Markin, CC BY-SA 2.0
Gyrocopter 2010 — Felix König, CC BY 3.0
Cierva C.30 — Hugh Llewelyn, CC BY-SA 2.0
Wikimedia Commonsin kautta
Lisenssit: creativecommons.org/licenses/by-sa/2.0 · creativecommons.org/licenses/by/3.0
Kaikki muut arkistokuvat ovat public domainia.
```

## français (`fr`)

Název:

```
L'autogire — l'hélicoptère qui n'en est pas un
```

Popis:

```
Il a un grand rotor sur le dessus. Il décolle et atterrit sur une surface
étonnamment réduite. Et si le moteur s'arrête en vol, il peut encore se
poser tout seul.

On dirait un hélicoptère. Ce n'en est pas un — parce que le moteur
n'entraîne pas du tout le rotor. C'est l'air qui le fait.

Cette vidéo démonte tout ça : pourquoi un rotor tourne alors que rien ne
l'entraîne, pourquoi le fuselage ne tourne pas avec lui, pourquoi
l'appareil ne peut pas faire du surplace, et pourquoi quelques-uns
quittent quand même le sol sans aucune course. Plus ce sur quoi presque
tout le monde se trompe — l'autogire a treize ans de PLUS que
l'hélicoptère utilisable, et coûte une fraction de son prix.

Chapitres
00:00 L'engin qui ressemble à un hélicoptère
00:31 Comment l'hélicoptère s'y prend
00:57 Une hélice complètement séparée
01:20 Pourquoi l'air fait-il tourner le rotor ?
02:26 Ce que coûte le rotor libre
02:45 Pourquoi le fuselage ne tourne pas
03:45 Il ne peut pas faire du surplace
04:28 Le décollage sauté
05:20 Quand le moteur s'arrête
06:07 Mais cela n'exclut pas l'accident
06:37 Plus ancien que l'hélicoptère
07:21 Étonnamment abordable
08:18 Pourquoi tout le monde n'en a-t-il pas ?
08:56 Pas un hélicoptère bon marché — autre chose

Les sous-titres sont écrits pour cette vidéo, pas générés automatiquement. Une piste audio en anglais américain est disponible en seconde piste.


Il y a plus qu'il n'y paraît.

CRÉDITS PHOTO
Autogyro МТО-Sport and photographer in flight — Aleksandr Markin, CC BY-SA 2.0
Gyrocopter 2010 — Felix König, CC BY 3.0
Cierva C.30 — Hugh Llewelyn, CC BY-SA 2.0
via Wikimedia Commons
Licences : creativecommons.org/licenses/by-sa/2.0 · creativecommons.org/licenses/by/3.0
Toutes les autres images d'archive sont dans le domaine public.
```

---

## Bahasa Indonesia (`id`)

```
Gyroplane — Helikopter yang Bukan Helikopter
```

```
Ia punya rotor besar di atasnya. Ia lepas landas dan mendarat di area yang ternyata sangat sempit. Dan kalau mesinnya mati di udara, ia tetap bisa mendaratkan dirinya sendiri.

Kedengarannya seperti helikopter. Bukan — karena mesinnya sama sekali tidak menggerakkan rotornya. Udaranyalah yang menggerakkan.

Video ini membongkarnya: kenapa sebuah rotor berputar padahal tidak ada yang menggerakkannya, kenapa badan pesawatnya tidak ikut berputar, kenapa mesin ini tidak bisa melayang di tempat, dan kenapa beberapa di antaranya tetap bisa melompat dari tanah tanpa ancang-ancang sama sekali. Ditambah bagian yang kebanyakan orang salah pahami — gyroplane itu tiga belas tahun LEBIH TUA daripada helikopter yang praktis, dan harganya hanya sebagian kecil dari harga helikopter.

Bab
00:00 Mesin yang kelihatan seperti helikopter
00:31 Bagaimana helikopter melakukannya
00:57 Baling-baling yang benar-benar terpisah
01:20 Kenapa udara memutar rotornya?
02:26 Berapa harga dari rotor yang bebas
02:45 Kenapa badan pesawatnya tidak ikut berputar
03:45 Ia tidak bisa melayang di tempat
04:28 Lepas landas melompat
05:20 Ketika mesinnya berhenti
06:07 Tapi ia tidak kebal kecelakaan
06:37 Lebih tua daripada helikopter
07:21 Ternyata terjangkau
08:18 Jadi kenapa tidak semua orang menerbangkannya?
08:56 Bukan helikopter murah — sesuatu yang lain

Subtitel ditulis khusus untuk video ini, bukan dibuat secara otomatis. Tersedia juga trek audio kedua dalam bahasa Inggris Amerika.

Ada lebih dari itu.

KREDIT GAMBAR
Autogyro МТО-Sport and photographer in flight — Aleksandr Markin, CC BY-SA 2.0
Gyrocopter 2010 — Felix König, CC BY 3.0
Cierva C.30 — Hugh Llewelyn, CC BY-SA 2.0
via Wikimedia Commons
Lisensi: creativecommons.org/licenses/by-sa/2.0 · creativecommons.org/licenses/by/3.0
Semua gambar arsip lainnya berada dalam domain publik.
```

## italiano (`it`)

Název:

```
L'autogiro — l'elicottero che non lo è
```

Popis:

```
Sopra ha un grande rotore. Decolla e atterra in uno spazio
sorprendentemente piccolo. E se il motore si ferma in volo, riesce ancora
a posarsi da solo.

Sembra un elicottero. Non lo è — perché il motore non muove affatto il
rotore. Lo muove l'aria.

Questo video lo smonta: perché un rotore gira quando niente lo trascina,
perché la fusoliera non gira con lui, perché il mezzo non sa restare
fermo in aria, e perché alcuni riescono comunque a staccarsi da terra
senza corsa alcuna. E poi la parte su cui quasi tutti sbagliano —
l'autogiro è tredici anni PIÙ VECCHIO dell'elicottero utilizzabile, e
costa una frazione del suo prezzo.

Capitoli
00:00 La macchina che sembra un elicottero
00:31 Come fa l'elicottero
00:57 Un'elica del tutto separata
01:20 Perché l'aria fa girare il rotore?
02:26 Quanto costa il rotore libero
02:45 Perché la fusoliera non gira
03:45 Non sa restare fermo in aria
04:28 Il decollo a salto
05:20 Quando si ferma il motore
06:07 Ma non è a prova di incidente
06:37 Più vecchio dell'elicottero
07:21 Sorprendentemente accessibile
08:18 E allora perché non lo usano tutti?
08:56 Non un elicottero economico — un'altra cosa

I sottotitoli sono scritti per questo video, non generati automaticamente. Come seconda traccia audio è disponibile l’inglese americano.


C'è dell'altro.

CREDITI IMMAGINI
Autogyro МТО-Sport and photographer in flight — Aleksandr Markin, CC BY-SA 2.0
Gyrocopter 2010 — Felix König, CC BY 3.0
Cierva C.30 — Hugh Llewelyn, CC BY-SA 2.0
via Wikimedia Commons
Licenze: creativecommons.org/licenses/by-sa/2.0 · creativecommons.org/licenses/by/3.0
Tutte le altre immagini d'archivio sono di pubblico dominio.
```

---

## Deutsch (`de`)

Název:

```
Der Tragschrauber — der Hubschrauber, der keiner ist
```

Popis:

```
Oben hat er einen großen Rotor. Er startet und landet auf erstaunlich
kleinem Raum. Und wenn der Motor in der Luft ausfällt, kann er trotzdem noch
selbst landen.

Klingt nach Hubschrauber. Ist keiner — denn der Motor treibt den Rotor
überhaupt nicht an. Dafür sorgt die Luft.

Dieses Video nimmt das auseinander: warum sich ein Rotor dreht, wenn ihn
nichts antreibt, warum sich der Rumpf nicht mitdreht, warum das Gerät
nicht schweben kann, und warum einige trotzdem ganz ohne Rollstrecke vom
Boden abheben. Dazu der Teil, bei dem sich die meisten irren — der
Tragschrauber ist dreizehn Jahre ÄLTER als der brauchbare Hubschrauber,
und kostet einen Bruchteil davon.

Kapitel
00:00 Das Gerät, das aussieht wie ein Hubschrauber
00:31 Wie der Hubschrauber es macht
00:57 Ein völlig getrennter Propeller
01:20 Warum dreht die Luft den Rotor?
02:26 Was der freie Rotor kostet
02:45 Warum sich der Rumpf nicht mitdreht
03:45 Er kann nicht schweben
04:28 Der Sprungstart
05:20 Wenn der Motor ausfällt
06:07 Aber unzerstörbar ist er nicht
06:37 Älter als der Hubschrauber
07:21 Erstaunlich erschwinglich
08:18 Warum fliegt dann nicht jeder einen?
08:56 Kein billiger Hubschrauber — etwas anderes

Die Untertitel wurden für dieses Video geschrieben, nicht automatisch erzeugt. Als zweite Tonspur steht amerikanisches Englisch bereit.


Da steckt mehr dahinter.

BILDNACHWEISE
Autogyro МТО-Sport and photographer in flight — Aleksandr Markin, CC BY-SA 2.0
Gyrocopter 2010 — Felix König, CC BY 3.0
Cierva C.30 — Hugh Llewelyn, CC BY-SA 2.0
via Wikimedia Commons
Lizenzen: creativecommons.org/licenses/by-sa/2.0 · creativecommons.org/licenses/by/3.0
Alle übrigen Archivbilder sind gemeinfrei.
```

---

## polski (`pl`)

Název:

```
Wiatrakowiec — śmigłowiec, który nim nie jest
```

Popis:

```
Na górze ma duży wirnik. Startuje i ląduje na zaskakująco małej
przestrzeni. A gdy silnik zgaśnie w powietrzu, wciąż potrafi sam
wylądować.

Brzmi jak śmigłowiec. Nie jest — bo silnik w ogóle nie napędza wirnika.
Napędza go powietrze.

Ten film to rozkłada: dlaczego wirnik się kręci, gdy nic go nie napędza,
dlaczego kadłub nie kręci się razem z nim, dlaczego maszyna nie potrafi
zawisnąć i dlaczego kilka z nich mimo to odrywa się od ziemi zupełnie bez
rozbiegu. Do tego rzecz, co do której większość się myli — wiatrakowiec
jest trzynaście lat STARSZY od użytecznego śmigłowca i kosztuje ułamek
jego ceny.

Rozdziały
00:00 Maszyna, która wygląda jak śmigłowiec
00:31 Jak robi to śmigłowiec
00:57 Całkiem osobne śmigło
01:20 Dlaczego powietrze obraca wirnik?
02:26 Ile kosztuje swobodny wirnik
02:45 Dlaczego kadłub się nie kręci
03:45 Nie potrafi zawisnąć
04:28 Start skokowy
05:20 Gdy zgaśnie silnik
06:07 Ale nie jest odporny na katastrofę
06:37 Starszy niż śmigłowiec
07:21 Zaskakująco przystępny
08:18 To czemu nie lata nim każdy?
08:56 To nie tani śmigłowiec — to coś innego

Napisy są pisane do tego filmu, nie generowane automatycznie. Jako druga ścieżka dźwiękowa dostępny jest angielski amerykański.


Jest w tym coś więcej.

ŹRÓDŁA ZDJĘĆ
Autogyro МТО-Sport and photographer in flight — Aleksandr Markin, CC BY-SA 2.0
Gyrocopter 2010 — Felix König, CC BY 3.0
Cierva C.30 — Hugh Llewelyn, CC BY-SA 2.0
via Wikimedia Commons
Licencje: creativecommons.org/licenses/by-sa/2.0 · creativecommons.org/licenses/by/3.0
Pozostałe zdjęcia archiwalne są w domenie publicznej.
```

## português (Brasil) (`pt-BR`)

Název:

```
O autogiro — o helicóptero que não é
```

Popis:

```
Tem um grande rotor em cima. Decola e pousa num espaço surpreendentemente
pequeno. E se o motor morrer em pleno voo, ele ainda consegue pousar
sozinho.

Parece um helicóptero. Não é — porque o motor não move o rotor de jeito
nenhum. Quem move é o ar.

Este vídeo desmonta isso: por que um rotor gira quando nada o aciona, por
que a fuselagem não gira junto, por que a aeronave não consegue pairar, e
por que alguns ainda assim saem do chão sem corrida nenhuma. Mais a parte
em que quase todo mundo erra — o autogiro é treze anos MAIS ANTIGO que o
helicóptero prático, e custa uma fração do preço dele.

Capítulos
00:00 A máquina que parece um helicóptero
00:31 Como o helicóptero faz isso
00:57 Uma hélice completamente separada
01:20 Por que o ar gira o rotor?
02:26 O que custa o rotor livre
02:45 Por que a fuselagem não gira
03:45 Ele não consegue pairar
04:28 A decolagem em salto
05:20 Quando o motor para
06:07 Mas não é à prova de acidente
06:37 Mais antigo que o helicóptero
07:21 Surpreendentemente acessível
08:18 E por que nem todo mundo voa um?
08:56 Não é um helicóptero barato — é outra coisa

As legendas foram escritas para este vídeo, não geradas automaticamente. Como segunda faixa de áudio está disponível o inglês americano.


Tem mais nessa história.

CRÉDITOS DAS IMAGENS
Autogyro МТО-Sport and photographer in flight — Aleksandr Markin, CC BY-SA 2.0
Gyrocopter 2010 — Felix König, CC BY 3.0
Cierva C.30 — Hugh Llewelyn, CC BY-SA 2.0
via Wikimedia Commons
Licenças: creativecommons.org/licenses/by-sa/2.0 · creativecommons.org/licenses/by/3.0
As demais imagens de arquivo são de domínio público.
```

---

## Türkçe (`tr`)

```
Cayrokopter — Helikopter Olmayan Helikopter
```

```
Üstünde kocaman bir rotor var. Şaşırtıcı derecede küçük bir alanda kalkıp iniyor. Ve havadayken motoru durursa, kendini yine de yere indirebiliyor.

Kulağa helikopter gibi geliyor. Değil — çünkü motor rotoru hiç döndürmüyor. Onu hava döndürüyor.

Bu video bunu parçalarına ayırıyor: hiçbir şey döndürmezken bir rotor neden döner, gövde neden onunla birlikte dönmez, bu makine neden havada asılı kalamaz ve birkaçı neden hiç kalkış koşusu olmadan yerden sıçrayabilir. Üstüne, çoğu kişinin yanlış bildiği kısım — cayrokopter, kullanışlı helikopterden on üç yıl DAHA ESKİ ve fiyatı bir helikopterin fiyatının çok küçük bir kısmı.

Bölümler
00:00 Helikoptere benzeyen makine
00:31 Helikopter bunu nasıl yapıyor
00:57 Tamamen ayrı bir pervane
01:20 Rotoru neden hava döndürüyor?
02:26 Serbest rotorun bedeli
02:45 Gövde neden dönmüyor
03:45 Havada asılı kalamıyor
04:28 Sıçrayarak kalkış
05:20 Motor durduğunda
06:07 Ama kaza geçirmez değil
06:37 Helikopterden daha eski
07:21 Şaşırtıcı biçimde uygun fiyatlı
08:18 Peki neden herkes bir tane uçurmuyor?
08:56 Ucuz helikopter değil — başka bir şey

Altyazılar bu video için yazıldı, otomatik olarak oluşturulmadı. İkinci ses parçası olarak Amerikan İngilizcesi de mevcut.

Bundan fazlası var.

GÖRSEL KAYNAKLARI
Autogyro МТО-Sport and photographer in flight — Aleksandr Markin, CC BY-SA 2.0
Gyrocopter 2010 — Felix König, CC BY 3.0
Cierva C.30 — Hugh Llewelyn, CC BY-SA 2.0
Wikimedia Commons üzerinden
Lisanslar: creativecommons.org/licenses/by-sa/2.0 · creativecommons.org/licenses/by/3.0
Diğer tüm arşiv görselleri kamu malıdır.
```

## українська (`uk`)

```
Автожир — гелікоптер, який ним не є
```

```
Згори має великий ротор. Злітає й сідає на напрочуд малому просторі. А якщо двигун у повітрі заглухне, він усе одно зможе приземлитися.

Звучить як гелікоптер. Ним не є — бо двигун ротор узагалі не крутить. Крутить його повітря.

У цьому відео пояснюємо: чому ротор обертається, хоча його ніщо не приводить у рух, чому фюзеляж не обертається разом з ним, чому машина не вміє висіти на місці, і чому деякі з них однаково здатні підстрибнути із землі взагалі без розбігу. А до того та частина, яку більшість розуміє хибно: автожир на тринадцять років СТАРШИЙ за придатний до використання гелікоптер і коштує дещицю його ціни.

Розділи
00:00 Машина, схожа на гелікоптер
00:31 Як це робить гелікоптер
00:57 Цілком окремий гвинт
01:20 Чому повітря змушує ротор обертатися?
02:26 Чого коштує вільний ротор
02:45 Чому фюзеляж не обертається
03:45 Він не вміє висіти
04:28 Стрибковий зліт
05:20 Коли двигун зупиняється
06:07 Але це не гарантує захисту від аварій
06:37 Старший за гелікоптер
07:21 Напрочуд доступний
08:18 То чому на ньому не літають усі?
08:56 Не дешевий гелікоптер — щось інше

Субтитри написані для цього відео, а не згенеровані автоматично. Також доступна друга звукова доріжка — американською англійською.

За цим криється більше.

ДЖЕРЕЛА ЗОБРАЖЕНЬ
Autogyro МТО-Sport and photographer in flight — Aleksandr Markin, CC BY-SA 2.0
Gyrocopter 2010 — Felix König, CC BY 3.0
Cierva C.30 — Hugh Llewelyn, CC BY-SA 2.0
через Wikimedia Commons
Ліцензії: creativecommons.org/licenses/by-sa/2.0 · creativecommons.org/licenses/by/3.0
Усі інші архівні зображення — суспільне надбання.
```

## Tiếng Việt (`vi`)

```
Máy bay cánh quạt tự quay — chiếc trực thăng không phải trực thăng
```

```
Nó có một rotor lớn ở trên đầu. Nó cất và hạ cánh trong khoảng không gian nhỏ đến bất ngờ. Và nếu động cơ tắt giữa không trung, nó vẫn tự hạ cánh được.

Nghe thì giống trực thăng. Nhưng không phải — bởi động cơ hoàn toàn không quay rotor. Chính không khí mới quay nó.

Video này mổ xẻ chuyện đó: vì sao một rotor lại quay dù chẳng có gì dẫn động nó, vì sao thân máy bay không quay theo, vì sao cỗ máy này không thể treo một chỗ, và vì sao vài chiếc trong số đó vẫn bật lên khỏi mặt đất mà không cần chạy đà chút nào. Cộng thêm phần mà phần lớn mọi người hiểu sai — loại máy bay này ra đời TRƯỚC chiếc trực thăng có thể sử dụng trong thực tế mười ba năm, và giá chỉ bằng một phần nhỏ.

Các chương
00:00 Cỗ máy trông giống trực thăng
00:31 Trực thăng làm điều đó thế nào
00:57 Một cánh quạt hoàn toàn riêng biệt
01:20 Vì sao không khí lại quay rotor?
02:26 Cái giá của một rotor tự do
02:45 Vì sao thân máy bay không quay theo
03:45 Nó không thể bay treo tại chỗ
04:28 Cất cánh kiểu nhảy
05:20 Khi động cơ tắt
06:07 Nhưng nó không miễn nhiễm tai nạn
06:37 Ra đời trước trực thăng
07:21 Rẻ đến bất ngờ
08:18 Vậy sao không phải ai cũng lái loại máy bay này?
08:56 Không phải trực thăng giá rẻ — mà là thứ khác

Phụ đề được viết riêng cho video này, không phải tạo tự động. Có thể chọn tiếng Anh Mỹ ở bản âm thanh thứ hai.

Còn nhiều điều hơn thế.

NGUỒN HÌNH ẢNH
Autogyro МТО-Sport and photographer in flight — Aleksandr Markin, CC BY-SA 2.0
Gyrocopter 2010 — Felix König, CC BY 3.0
Cierva C.30 — Hugh Llewelyn, CC BY-SA 2.0
qua Wikimedia Commons
Giấy phép: creativecommons.org/licenses/by-sa/2.0 · creativecommons.org/licenses/by/3.0
Mọi hình tư liệu khác đều thuộc phạm vi công cộng.
```

## čeština (`cs`)

Název:

```
Vírník — vrtulník, který jím není
```

Popis:

```
Nahoře má velký rotor. Vzlétne i přistane na překvapivě malém prostoru.
A když mu ve vzduchu zhasne motor, pořád se dokáže sám posadit na zem.

Zní to jako vrtulník. Není — protože motor ten rotor vůbec nepohání.
Pohání ho vzduch.

Tohle video to rozebírá: proč se rotor točí, když ho nic nepohání, proč
se s ním netočí i trup, proč stroj neumí viset, a proč se pár z nich
přesto dokáže odlepit od země úplně bez rozjezdu. A k tomu věc, ve které
se většina lidí mýlí — vírník je o třináct let STARŠÍ než použitelný
vrtulník a stojí zlomek jeho ceny.

Kapitoly
00:00 Stroj, který vypadá jako vrtulník
00:31 Jak to dělá vrtulník
00:57 Úplně samostatná vrtule
01:20 Proč vzduch roztáčí rotor?
02:26 Co stojí volný rotor
02:45 Proč se netočí trup
03:45 Neumí viset
04:28 Skokový vzlet
05:20 Když zhasne motor
06:07 Ale havárii to nevylučuje
06:37 Starší než vrtulník
07:21 Překvapivě dostupný
08:18 Tak proč na něm nelétá každý?
08:56 Není to levný vrtulník — je to něco jiného

Titulky jsou psané pro tohle video, ne strojový přepis. Jako druhá zvuková stopa je k dispozici americká angličtina.


Je za tím víc.

OBRAZOVÉ ZDROJE
Autogyro МТО-Sport and photographer in flight — Aleksandr Markin, CC BY-SA 2.0
Gyrocopter 2010 — Felix König, CC BY 3.0
Cierva C.30 — Hugh Llewelyn, CC BY-SA 2.0
via Wikimedia Commons
Licence: creativecommons.org/licenses/by-sa/2.0 · creativecommons.org/licenses/by/3.0
Ostatní archivní snímky jsou volné dílo.
```

---

## español (`es`)

Název:

```
El autogiro — el helicóptero que no lo es
```

Popis:

```
Lleva un gran rotor encima. Despega y aterriza en un espacio
sorprendentemente pequeño. Y si el motor se para en pleno vuelo, todavía
puede aterrizar por sí solo.

Suena a helicóptero. No lo es — porque el motor no mueve el rotor en
absoluto. Lo mueve el aire.

Este vídeo lo desmonta: por qué gira un rotor cuando nada lo impulsa, por
qué el fuselaje no gira con él, por qué el aparato no puede quedarse
suspendido, y por qué unos pocos consiguen aun así separarse del suelo
sin carrera ninguna. Y además lo que casi todo el mundo se equivoca — el
autogiro es trece años MÁS ANTIGUO que el helicóptero práctico, y cuesta
una fracción de uno.

Capítulos
00:00 La máquina que parece un helicóptero
00:31 Cómo lo hace un helicóptero
00:57 Una hélice completamente aparte
01:20 ¿Por qué el aire hace girar el rotor?
02:26 Lo que cuesta el rotor libre
02:45 Por qué no gira el fuselaje
03:45 No puede quedarse suspendido
04:28 El despegue de salto
05:20 Cuando se para el motor
06:07 Pero no está a salvo de estrellarse
06:37 Más antiguo que el helicóptero
07:21 Sorprendentemente asequible
08:18 ¿Y por qué no vuela uno todo el mundo?
08:56 No es un helicóptero barato — es otra cosa

Los subtítulos están escritos para este vídeo, no generados automáticamente. Como segunda pista de audio está disponible el inglés americano.


Hay más de lo que parece.

CRÉDITOS DE IMAGEN
Autogyro МТО-Sport and photographer in flight — Aleksandr Markin, CC BY-SA 2.0
Gyrocopter 2010 — Felix König, CC BY 3.0
Cierva C.30 — Hugh Llewelyn, CC BY-SA 2.0
via Wikimedia Commons
Licencias: creativecommons.org/licenses/by-sa/2.0 · creativecommons.org/licenses/by/3.0
Las demás imágenes de archivo son de dominio público.
```

---

## svenska (`sv`)

Název:

```
Autogiron — helikoptern som inte är en
```

Popis:

```
Den har en stor rotor upptill. Den lyfter och landar på förvånansvärt
liten yta. Och om motorn tystnar i luften kan den fortfarande landa på
egen hand.

Låter som en helikopter. Det är den inte — för motorn driver inte rotorn
alls. Det gör luften.

Den här videon tar isär det: varför en rotor snurrar när ingenting driver
den, varför flygkroppen inte snurrar med, varför farkosten inte kan hovra,
och varför några ändå lämnar marken helt utan startsträcka. Plus det som
de flesta har fel om — autogiron är tretton år ÄLDRE än den användbara
helikoptern, och kostar en bråkdel av en sådan.

Kapitel
00:00 Maskinen som ser ut som en helikopter
00:31 Så gör helikoptern det
00:57 En helt separat propeller
01:20 Varför snurrar luften rotorn?
02:26 Vad den fria rotorn kostar
02:45 Varför flygkroppen inte snurrar
03:45 Den kan inte hovra
04:28 Hoppstarten
05:20 När motorn stannar
06:07 Men kraschsäker är den inte
06:37 Äldre än helikoptern
07:21 Förvånansvärt prisvärd
08:18 Så varför flyger inte alla en?
08:56 Ingen billig helikopter — något annat

Undertexterna är skrivna för den här videon, inte automatgenererade. Som andra ljudspår finns amerikansk engelska.


Det ligger mer i det.

BILDKÄLLOR
Autogyro МТО-Sport and photographer in flight — Aleksandr Markin, CC BY-SA 2.0
Gyrocopter 2010 — Felix König, CC BY 3.0
Cierva C.30 — Hugh Llewelyn, CC BY-SA 2.0
via Wikimedia Commons
Licenser: creativecommons.org/licenses/by-sa/2.0 · creativecommons.org/licenses/by/3.0
Övriga arkivbilder är public domain.
```

---
