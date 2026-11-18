# Lokalizované názvy a popisy — 049

Nahrává `tools/lokalizace.py` přes `videos.update(part="localizations")`.
Anglický titul a popis zůstávají v `youtube.md` a posílají se zpátky
beze změny.

```bash
python tools/lokalizace.py videos/049-what-makes-a-battery-catch-fire --zkouska
python tools/lokalizace.py videos/049-what-makes-a-battery-catch-fire
```

**Formát si vynucuje parser** (`bloky_z_podkladu()`): sekce jazyka je
nadpis `## <endonymum> (`<kód>`)`, uvnitř **přesně dva bloky** v trojici
zpětných apostrofů — první titul, druhý popis. Jiný počet nástroj
přeskočí s hláškou a jinak to nekřičí.

**Pořadí je podle YouTube Studia**, tedy bajtově podle UTF-8 a podle
ČESKÉHO názvu jazyka, ne abecedně podle kódu.

## Co se NEPŘEKLÁDÁ

- **vlastní jména** — Samsung, Galaxy Note 7, Sony, New York, Wikimedia
  Commons, Lead holder, Pang Kakit
- **názvy archivních snímků** v kreditech — jsou to identifikátory
  souborů na Wikimedia Commons
- **časy kapitol** na vteřinu — jsou to tytéž okamžiky ve všech jazycích
- **tagy** — YouTube je per-jazyk nemá

Popisek kreditů (`IMAGE CREDITS`, `Licences:`) se naopak **překládá**.

## Kontrola čísel

| anglicky | co to je | pozor |
|---|---|---|
| two and a half million phones | 2,5 × 10⁶ | |
| ninety-two | 92 | |
| roughly a million | 10⁶ | |
| one in ten thousand | 1 : 10⁴ | |
| eighteen people | 18 | |
| twenty micrometres | 20 µm | fi `mikrometriä`, uk `мікрометрів` |
| 2016, 2023 | letopočty | v popisu číslicí ve všech jazycích |

## suomi (`fi`)

```
Mistä akku syttyy palamaan?
```

```
Muutaman päivän välein tulee taas uutinen akkupalosta. Varavirtalähde
lentokoneessa, potkulauta rappukäytävässä, joskus kokonainen talo.
Otsikko on aina sama: litiumioniakut ovat vaarallisia. Ja silti yksi on
taskussasi, yksi läppärissäsi ja luultavasti yksi parkissa ulkona,
eivätkä ne tee koko elinaikanaan yhtään mitään.

Tämä video kertoo siitä, minkä oikeasti täytyy mennä vikaan.
Litiumkenno kantaa oman polttoaineensa suljettuna sisällään.
Elektrodien välissä on muovikalvo, joka on alle kahdenkymmenen
mikrometrin paksuinen — ja muovi kestää kuumuutta huonosti. Kun oikosulku
kuumentaa yhden kohdan, reikä kalvossa kasvaa, isompi reikä johtaa
enemmän virtaa, enemmän virtaa tuottaa enemmän lämpöä, eikä mikään siinä
silmukassa hidasta sitä. Sitä kutsutaan lämpökarkaamiseksi.

Sitten vaikeampi puoli: kuinka usein niin käy. Kun Samsung veti takaisin
kaksi ja puoli miljoonaa puhelinta vuonna 2016, Amerikassa ilmoitettuja
tapauksia oli yhdeksänkymmentäkaksi, noin miljoonasta siellä myydystä.
Yksi kymmenestätuhannesta riitti lopettamaan lippulaivapuhelimen ja
kieltämään sen lentokoneissa. Näemme epäonnistumiset. Emme näe koskaan
nimittäjää — ja New Yorkissa, jossa nämä palot tappoivat kahdeksantoista
ihmistä vuonna 2023, se mikä muuttui, ei ollut kemia vaan se, mitkä akut
pääsivät markkinoille.

Tekstitykset on kirjoitettu tätä videota varten, ei koneellisesti luotu.
Toisena ääniraitana on saatavilla amerikanenglantilainen ääniraita.

Koko teksti, lähteet ja käännökset: https://theresmoretoit-channel.github.io/fi/videos/what-makes-a-battery-catch-fire/

Luvut
00:00 Taas paloi akku
00:40 Se kantaa oman polttoaineensa
01:05 Minkä täytyy mennä ensin vikaan
01:46 Puhelimen akun sisällä
02:25 Separaattori
02:51 Neljä tapaa
03:04 Sisäinen oikosulku
03:32 Silmukka
03:52 Lämpökarkaaminen
04:02 Mitä ulos tulee
04:31 Kennot eivät ole koskaan yksin
05:01 Ovatko ne siis vaarallisia?
05:21 Miltä harvinainen oikeasti näyttää
05:52 Laske ympärilläsi olevat akut
06:07 Nimittäjä
06:36 Akku on järjestelmä
07:20 Mitä New York teki
08:07 Miksi niitä ei vain tehdä turvallisiksi?
08:33 Mitä seuraavaksi
09:16 Takaisin paradoksiin

KUVALÄHTEET
Lithium-ion laptop battery internals — Lead holder, CC BY-SA 3.0
Samsung Galaxy Note 7 rear — Pang Kakit, CC BY-SA 4.0
molemmat Wikimedia Commonsin kautta
Lisenssit: creativecommons.org/licenses/by-sa/3.0
           creativecommons.org/licenses/by-sa/4.0
```

## français (`fr`)

```
Qu'est-ce qui fait brûler une batterie ?
```

```
Tous les quelques jours, une nouvelle histoire d'incendie de batterie.
Une batterie externe dans un avion, une trottinette dans une cage
d'escalier, parfois un immeuble entier. Le titre est toujours le même :
les batteries lithium-ion sont dangereuses. Et pourtant vous en avez une
dans la poche, une dans votre ordinateur et sans doute une garée dehors,
et presque toutes passent leur vie à ne rien faire du tout.

Cette vidéo parle de ce qui doit vraiment mal tourner. Une cellule au
lithium transporte son propre combustible, scellé à l'intérieur. Entre
les deux électrodes se trouve un film plastique de moins de vingt
micromètres — et le plastique supporte mal la chaleur. Dès qu'un
court-circuit chauffe un point, le trou dans ce film s'agrandit, un trou
plus grand laisse passer plus de courant, plus de courant produit plus
de chaleur, et rien dans cette boucle ne la ralentit. C'est
l'emballement thermique.

Puis la moitié la plus difficile : à quelle fréquence cela arrive. Quand
Samsung a rappelé deux millions et demi de téléphones en 2016, le nombre
d'incidents signalés aux États-Unis était de quatre-vingt-douze, sur
environ un million vendus là-bas. Un sur dix mille a suffi pour tuer un
téléphone haut de gamme et le faire interdire dans les avions. Nous
voyons les défaillances. Nous ne voyons jamais le dénominateur — et à
New York, où ces incendies ont tué dix-huit personnes en 2023, ce qui a
changé ensuite n'était pas la chimie mais les batteries autorisées sur
le marché.

Les sous-titres sont écrits pour cette vidéo, pas générés
automatiquement. Une piste audio en anglais américain est disponible
comme seconde piste audio.

Transcription complète, sources et traductions : https://theresmoretoit-channel.github.io/fr/videos/what-makes-a-battery-catch-fire/

Chapitres
00:00 Encore une batterie en feu
00:40 Elle transporte son propre combustible
01:05 Ce qui doit mal tourner d'abord
01:46 À l'intérieur d'une batterie de téléphone
02:25 Le séparateur
02:51 Quatre entrées possibles
03:04 Un court-circuit interne
03:32 La boucle
03:52 L'emballement thermique
04:02 Ce qui en sort
04:31 Les cellules ne sont jamais seules
05:01 Alors, sont-elles dangereuses ?
05:21 À quoi ressemble vraiment « rare »
05:52 Comptez les batteries autour de vous
06:07 Le dénominateur
06:36 Une batterie est un système
07:20 Ce qu'a fait New York
08:07 Pourquoi ne pas simplement les rendre sûres ?
08:33 Ce qui vient ensuite
09:16 Retour au paradoxe

CRÉDITS PHOTOS
Lithium-ion laptop battery internals — Lead holder, CC BY-SA 3.0
Samsung Galaxy Note 7 rear — Pang Kakit, CC BY-SA 4.0
les deux via Wikimedia Commons
Licences : creativecommons.org/licenses/by-sa/3.0
           creativecommons.org/licenses/by-sa/4.0
```

## Bahasa Indonesia (`id`)

```
Apa yang Membuat Baterai Terbakar?
```

```
Setiap beberapa hari ada lagi berita tentang baterai terbakar. Power
bank di pesawat, skuter di tangga, kadang satu gedung utuh. Judulnya
selalu sama: baterai lithium-ion itu berbahaya. Padahal satu ada di saku
Anda, satu di laptop Anda dan mungkin satu terparkir di luar, dan
hampir semuanya menghabiskan usianya tanpa melakukan apa pun.

Video ini tentang apa yang sebenarnya harus gagal lebih dulu. Sel
lithium membawa bahan bakarnya sendiri, tersegel di dalamnya. Di antara
kedua elektroda ada lapisan plastik setebal kurang dari dua puluh
mikrometer — dan plastik tidak tahan panas. Begitu korsleting membuat
satu titik panas, lubang pada lapisan itu membesar, lubang lebih besar
mengalirkan arus lebih besar, arus lebih besar menghasilkan panas lebih
banyak, dan tidak ada apa pun dalam lingkaran itu yang memperlambatnya.
Itulah pelarian termal.

Lalu bagian yang lebih sulit: seberapa sering itu terjadi. Ketika
Samsung menarik dua setengah juta ponsel pada tahun 2016, jumlah insiden
yang dilaporkan di Amerika adalah sembilan puluh dua, dari sekitar satu
juta yang terjual di sana. Satu dari sepuluh ribu sudah cukup untuk
menamatkan ponsel unggulan dan membuatnya dilarang di pesawat. Kita
melihat kegagalannya. Kita tidak pernah melihat penyebutnya — dan di New
York, tempat kebakaran semacam ini menewaskan delapan belas orang pada
tahun 2023, yang berubah setelahnya bukan kimianya, melainkan baterai
mana yang boleh masuk pasar.

Takarir ditulis khusus untuk video ini, bukan dibuat otomatis. Tersedia
juga trek audio kedua dalam bahasa Inggris Amerika.

Transkrip lengkap, sumber, dan terjemahan: https://theresmoretoit-channel.github.io/id/videos/what-makes-a-battery-catch-fire/

Bab
00:00 Ada baterai terbakar lagi
00:40 Ia membawa bahan bakarnya sendiri
01:05 Apa yang harus gagal lebih dulu
01:46 Di dalam baterai ponsel
02:25 Separator
02:51 Empat jalan masuk
03:04 Korsleting internal
03:32 Lingkarannya
03:52 Pelarian termal
04:02 Apa yang keluar
04:31 Sel tidak pernah sendirian
05:01 Jadi, apakah berbahaya?
05:21 Wujud sebenarnya dari langka
05:52 Hitung baterai di sekitar Anda
06:07 Penyebut
06:36 Baterai adalah sebuah sistem
07:20 Yang dilakukan New York
08:07 Kenapa tidak dibuat aman saja?
08:33 Apa yang datang berikutnya
09:16 Kembali ke paradoks

KREDIT GAMBAR
Lithium-ion laptop battery internals — Lead holder, CC BY-SA 3.0
Samsung Galaxy Note 7 rear — Pang Kakit, CC BY-SA 4.0
keduanya melalui Wikimedia Commons
Lisensi: creativecommons.org/licenses/by-sa/3.0
         creativecommons.org/licenses/by-sa/4.0
```

## italiano (`it`)

```
Che cosa fa prendere fuoco a una batteria?
```

```
Ogni pochi giorni arriva un'altra storia di batterie in fiamme. Un power
bank su un aereo, un monopattino in una tromba delle scale, a volte un
intero edificio. Il titolo è sempre lo stesso: le batterie agli ioni di
litio sono pericolose. Eppure ne hai una in tasca, una nel portatile e
probabilmente una parcheggiata fuori, e quasi tutte passano la vita
senza fare assolutamente nulla.

Questo video parla di che cosa deve davvero andare storto. Una cella al
litio si porta dietro il proprio combustibile, sigillato all'interno.
Tra i due elettrodi c'è una pellicola di plastica più sottile di venti
micrometri — e la plastica sopporta male il calore. Appena un
cortocircuito scalda un punto, il foro in quella pellicola si allarga,
un foro più grande porta più corrente, più corrente produce più calore,
e in quel circolo non c'è nulla che lo freni. Si chiama fuga termica.

Poi la metà più difficile: quanto spesso succede. Quando nel 2016
Samsung richiamò due milioni e mezzo di telefoni, i casi segnalati negli
Stati Uniti furono novantadue, su circa un milione venduti lì. Uno su
diecimila è bastato per far fuori un telefono di punta e per farlo
vietare sugli aerei. Vediamo i guasti. Non vediamo mai il denominatore —
e a New York, dove questi incendi hanno ucciso diciotto persone nel
2023, ciò che è cambiato dopo non è stata la chimica ma quali batterie
potevano arrivare sul mercato.

I sottotitoli sono scritti per questo video, non generati
automaticamente. È disponibile una seconda traccia audio in inglese
americano.

Trascrizione completa, fonti e traduzioni: https://theresmoretoit-channel.github.io/it/videos/what-makes-a-battery-catch-fire/

Capitoli
00:00 È bruciata un'altra batteria
00:40 Si porta dietro il proprio combustibile
01:05 Che cosa deve andare storto per primo
01:46 Dentro la batteria di un telefono
02:25 Il separatore
02:51 Quattro modi
03:04 Un cortocircuito interno
03:32 Il circolo
03:52 Fuga termica
04:02 Che cosa esce
04:31 Le celle non sono mai sole
05:01 Allora, sono pericolose?
05:21 Com'è fatto davvero il raro
05:52 Conta le batterie attorno a te
06:07 Il denominatore
06:36 Una batteria è un sistema
07:20 Che cosa ha fatto New York
08:07 Perché non renderle semplicemente sicure?
08:33 Che cosa arriva adesso
09:16 Di nuovo al paradosso

CREDITI IMMAGINI
Lithium-ion laptop battery internals — Lead holder, CC BY-SA 3.0
Samsung Galaxy Note 7 rear — Pang Kakit, CC BY-SA 4.0
entrambe via Wikimedia Commons
Licenze: creativecommons.org/licenses/by-sa/3.0
         creativecommons.org/licenses/by-sa/4.0
```

## Deutsch (`de`)

```
Was bringt einen Akku zum Brennen?
```

```
Alle paar Tage gibt es wieder eine Geschichte über einen brennenden
Akku. Eine Powerbank im Flugzeug, ein Roller im Treppenhaus, manchmal
ein ganzes Haus. Die Schlagzeile ist immer dieselbe: Lithium-Ionen-Akkus
sind gefährlich. Und doch steckt einer in Ihrer Tasche, einer in Ihrem
Laptop und wahrscheinlich einer vor dem Haus, und fast alle tun ihr
Leben lang überhaupt nichts.

In diesem Video geht es darum, was wirklich schiefgehen muss. Eine
Lithiumzelle trägt ihren Brennstoff mit sich, eingeschweißt in ihrem
Inneren. Zwischen den beiden Elektroden liegt eine Kunststofffolie,
dünner als zwanzig Mikrometer — und Kunststoff verträgt Hitze schlecht.
Sobald ein Kurzschluss eine Stelle heiß macht, wird das Loch in dieser
Folie größer, ein größeres Loch führt mehr Strom, mehr Strom macht mehr
Hitze, und nichts in dieser Schleife bremst sie. Das ist thermisches
Durchgehen.

Dann die schwierigere Hälfte: wie oft das passiert. Als Samsung 2016
zweieinhalb Millionen Handys zurückrief, lag die Zahl der gemeldeten
Vorfälle in Amerika bei zweiundneunzig, bei rund einer Million dort
verkaufter Geräte. Einer von zehntausend genügte, um ein Spitzenmodell
zu beenden und es in Flugzeugen verbieten zu lassen. Wir sehen die
Ausfälle. Den Nenner sehen wir nie — und in New York, wo diese Brände
2023 achtzehn Menschen töteten, änderte sich danach nicht die Chemie,
sondern welche Akkus auf den Markt durften.

Die Untertitel sind für dieses Video geschrieben, nicht automatisch
erzeugt. Eine amerikanisch-englische Tonspur steht als zweite Tonspur
zur Verfügung.

Vollständiger Text, Quellen und Übersetzungen: https://theresmoretoit-channel.github.io/de/videos/what-makes-a-battery-catch-fire/

Kapitel
00:00 Schon wieder ein brennender Akku
00:40 Er trägt seinen Brennstoff mit sich
01:05 Was zuerst schiefgehen muss
01:46 Im Inneren eines Handyakkus
02:25 Der Separator
02:51 Vier Wege hinein
03:04 Ein interner Kurzschluss
03:32 Die Schleife
03:52 Thermisches Durchgehen
04:02 Was herauskommt
04:31 Zellen sind nie allein
05:01 Also: Sind sie gefährlich?
05:21 Wie selten wirklich aussieht
05:52 Zählen Sie die Akkus um sich herum
06:07 Der Nenner
06:36 Ein Akku ist ein System
07:20 Was New York getan hat
08:07 Warum macht man sie nicht einfach sicher?
08:33 Was als Nächstes kommt
09:16 Zurück zum Paradox

BILDNACHWEISE
Lithium-ion laptop battery internals — Lead holder, CC BY-SA 3.0
Samsung Galaxy Note 7 rear — Pang Kakit, CC BY-SA 4.0
beide über Wikimedia Commons
Lizenzen: creativecommons.org/licenses/by-sa/3.0
          creativecommons.org/licenses/by-sa/4.0
```

## polski (`pl`)

```
Co sprawia, że bateria się zapala?
```

```
Co kilka dni pojawia się kolejna historia o płonącej baterii. Powerbank
w samolocie, hulajnoga na klatce schodowej, czasem cały budynek.
Nagłówek jest zawsze taki sam: baterie litowo-jonowe są niebezpieczne.
A jednak jedną masz w kieszeni, drugą w laptopie i pewnie jeszcze jedną
zaparkowaną przed domem, i prawie wszystkie spędzają całe życie nie
robiąc absolutnie nic.

Ten film jest o tym, co naprawdę musi pójść źle. Ogniwo litowe niesie
własne paliwo, zamknięte w środku. Między elektrodami leży plastikowa
folia cieńsza niż dwadzieścia mikrometrów — a plastik źle znosi gorąco.
Gdy zwarcie rozgrzeje jedno miejsce, dziura w tej folii rośnie, większa
dziura przepuszcza większy prąd, większy prąd daje więcej ciepła i nic w
tej pętli tego nie hamuje. To właśnie ucieczka termiczna.

Potem trudniejsza połowa: jak często to się zdarza. Kiedy w 2016 roku
Samsung wycofał dwa i pół miliona telefonów, liczba zgłoszonych
przypadków w Ameryce wyniosła dziewięćdziesiąt dwa, na mniej więcej
milion sprzedanych tam sztuk. Jeden na dziesięć tysięcy wystarczył, by
uśmiercić flagowy telefon i doprowadzić do zakazu w samolotach. Widzimy
awarie. Nigdy nie widzimy mianownika — a w Nowym Jorku, gdzie te pożary
zabiły osiemnaście osób w 2023 roku, zmieniła się potem nie chemia, lecz
to, które baterie mogły trafić na rynek.

Napisy są napisane do tego filmu, nie wygenerowane automatycznie. Jako
druga ścieżka dźwiękowa dostępna jest wersja w amerykańskiej angielszczyźnie.

Pełna transkrypcja, źródła i tłumaczenia: https://theresmoretoit-channel.github.io/pl/videos/what-makes-a-battery-catch-fire/

Rozdziały
00:00 Znowu zapaliła się bateria
00:40 Niesie własne paliwo
01:05 Co musi pójść źle jako pierwsze
01:46 W środku baterii telefonu
02:25 Separator
02:51 Cztery drogi
03:04 Zwarcie wewnętrzne
03:32 Pętla
03:52 Ucieczka termiczna
04:02 Co wychodzi na zewnątrz
04:31 Ogniwa nigdy nie są same
05:01 Więc czy są niebezpieczne?
05:21 Jak naprawdę wygląda rzadkie
05:52 Policz baterie wokół siebie
06:07 Mianownik
06:36 Bateria to system
07:20 Co zrobił Nowy Jork
08:07 Czemu po prostu nie zrobić ich bezpiecznymi?
08:33 Co będzie dalej
09:16 Z powrotem do paradoksu

ŹRÓDŁA ZDJĘĆ
Lithium-ion laptop battery internals — Lead holder, CC BY-SA 3.0
Samsung Galaxy Note 7 rear — Pang Kakit, CC BY-SA 4.0
oba przez Wikimedia Commons
Licencje: creativecommons.org/licenses/by-sa/3.0
          creativecommons.org/licenses/by-sa/4.0
```

## português (Brasil) (`pt-BR`)

```
O que faz uma bateria pegar fogo?
```

```
A cada poucos dias aparece mais uma história de bateria em chamas. Um
carregador portátil num avião, um patinete numa escada, às vezes um
prédio inteiro. A manchete é sempre a mesma: baterias de íon-lítio são
perigosas. E mesmo assim você tem uma no bolso, uma no notebook e
provavelmente uma estacionada lá fora, e quase todas passam a vida sem
fazer absolutamente nada.

Este vídeo é sobre o que de fato precisa dar errado. Uma célula de lítio
carrega o próprio combustível, selado dentro dela. Entre os dois
eletrodos há um filme plástico com menos de vinte micrômetros — e
plástico aguenta mal o calor. Assim que um curto-circuito esquenta um
ponto, o furo nesse filme aumenta, um furo maior conduz mais corrente,
mais corrente gera mais calor, e nada nesse ciclo o desacelera. Isso é
fuga térmica.

Depois vem a metade mais difícil: com que frequência acontece. Quando a
Samsung recolheu dois milhões e meio de celulares em 2016, o número de
incidentes relatados nos Estados Unidos foi noventa e dois, de cerca de
um milhão vendidos lá. Um em dez mil bastou para acabar com um celular
topo de linha e fazer com que fosse proibido em aviões. A gente vê as
falhas. Nunca vê o denominador — e em Nova York, onde esses incêndios
mataram dezoito pessoas em 2023, o que mudou depois não foi a química, e
sim quais baterias podiam chegar ao mercado.

As legendas foram escritas para este vídeo, não geradas automaticamente.
Há uma segunda faixa de áudio em inglês americano.

Transcrição completa, fontes e traduções: https://theresmoretoit-channel.github.io/pt-br/videos/what-makes-a-battery-catch-fire/

Capítulos
00:00 Outra bateria pegou fogo
00:40 Ela carrega o próprio combustível
01:05 O que precisa dar errado primeiro
01:46 Dentro da bateria de um celular
02:25 O separador
02:51 Quatro caminhos
03:04 Um curto interno
03:32 O ciclo
03:52 Fuga térmica
04:02 O que sai
04:31 As células nunca estão sozinhas
05:01 Então, elas são perigosas?
05:21 Como raro realmente se parece
05:52 Conte as baterias à sua volta
06:07 O denominador
06:36 Uma bateria é um sistema
07:20 O que Nova York fez
08:07 Por que não torná-las seguras?
08:33 O que vem por aí
09:16 De volta ao paradoxo

CRÉDITOS DAS IMAGENS
Lithium-ion laptop battery internals — Lead holder, CC BY-SA 3.0
Samsung Galaxy Note 7 rear — Pang Kakit, CC BY-SA 4.0
ambas via Wikimedia Commons
Licenças: creativecommons.org/licenses/by-sa/3.0
          creativecommons.org/licenses/by-sa/4.0
```

## Türkçe (`tr`)

```
Bir bataryayı ne tutuşturur?
```

```
Birkaç günde bir yine bir batarya yangını haberi çıkıyor. Uçakta bir
powerbank, merdiven boşluğunda bir scooter, bazen koca bir bina. Başlık
hep aynı: lityum iyon bataryalar tehlikelidir. Oysa bir tanesi
cebinizde, bir tanesi dizüstü bilgisayarınızda, muhtemelen bir tanesi de
dışarıda park halinde ve neredeyse hepsi ömrü boyunca hiçbir şey yapmaz.

Bu video, gerçekte neyin bozulması gerektiğini anlatıyor. Lityum hücre
kendi yakıtını içine kapatılmış olarak taşır. İki elektrot arasında
yirmi mikrometreden ince bir plastik film vardır — ve plastik ısıyla iyi
anlaşmaz. Bir kısa devre tek bir noktayı ısıttığı anda o filmdeki delik
büyür, daha büyük delik daha çok akım taşır, daha çok akım daha çok ısı
üretir ve bu döngüde onu yavaşlatan hiçbir şey yoktur. Buna termal kaçış
denir.

Sonra işin daha zor yarısı: bu ne sıklıkla oluyor. Samsung 2016'da iki
buçuk milyon telefonu geri çağırdığında, Amerika'da bildirilen olay
sayısı doksan ikiydi; orada satılan yaklaşık bir milyon cihaz içinde. On
binde bir, amiral gemisi bir telefonu bitirmeye ve uçaklarda
yasaklanmasına yetti. Arızaları görüyoruz. Paydayı hiç görmüyoruz — ve
bu yangınların 2023'te on sekiz kişiyi öldürdüğü New York'ta sonradan
değişen şey kimya değil, hangi bataryaların piyasaya çıkabildiğiydi.

Altyazılar bu video için yazıldı, otomatik üretilmedi. İkinci ses parçası
olarak Amerikan İngilizcesi mevcuttur.

Metnin tamamı, kaynaklar ve çeviriler: https://theresmoretoit-channel.github.io/tr/videos/what-makes-a-battery-catch-fire/

Bölümler
00:00 Yine bir batarya yandı
00:40 Kendi yakıtını taşıyor
01:05 Önce neyin bozulması gerekir
01:46 Telefon bataryasının içi
02:25 Separatör
02:51 Dört giriş yolu
03:04 İç kısa devre
03:32 Döngü
03:52 Termal kaçış
04:02 Dışarı ne çıkıyor
04:31 Hücreler asla yalnız değildir
05:01 Peki, tehlikeliler mi?
05:21 Nadir gerçekte nasıl görünür
05:52 Çevrenizdeki bataryaları sayın
06:07 Payda
06:36 Batarya bir sistemdir
07:20 New York ne yaptı
08:07 Neden basitçe güvenli yapılmıyor?
08:33 Sırada ne var
09:16 Yeniden paradoksa

GÖRSEL KAYNAKLARI
Lithium-ion laptop battery internals — Lead holder, CC BY-SA 3.0
Samsung Galaxy Note 7 rear — Pang Kakit, CC BY-SA 4.0
ikisi de Wikimedia Commons üzerinden
Lisanslar: creativecommons.org/licenses/by-sa/3.0
           creativecommons.org/licenses/by-sa/4.0
```

## українська (`uk`)

```
Через що батарея загоряється?
```

```
Кожні кілька днів з'являється чергова історія про пожежу через батарею.
Павербанк у літаку, самокат у під'їзді, іноді цілий будинок. Заголовок
завжди той самий: літій-іонні батареї небезпечні. І все ж одна лежить у
вас у кишені, друга в ноутбуці й, мабуть, ще одна припаркована надворі,
і майже всі вони проживають свій вік, не роблячи нічого.

Це відео про те, що насправді має зламатися. Літієвий елемент несе
власне паливо, запаяне всередині. Між двома електродами лежить
пластикова плівка, тонша за двадцять мікрометрів, — а пластик погано
переносить жар. Щойно коротке замикання розігріє одну точку, отвір у
цій плівці більшає, більший отвір пропускає більший струм, більший
струм дає більше тепла, і ніщо в цій петлі його не гальмує. Це і є
тепловий розгін.

Далі складніша половина: як часто це стається. Коли Samsung у 2016 році
відкликала два з половиною мільйони телефонів, кількість зафіксованих
випадків в Америці становила дев'яносто два — приблизно з мільйона
проданих там. Одного на десять тисяч вистачило, щоб покінчити з
флагманським телефоном і щоб його заборонили в літаках. Ми бачимо
відмови. Ми ніколи не бачимо знаменника — а в Нью-Йорку, де ці пожежі
забрали вісімнадцять життів у 2023 році, згодом змінилася не хімія, а
те, які батареї могли потрапити на ринок.

Субтитри написані для цього відео, а не згенеровані автоматично. Другою
звуковою доріжкою доступна американська англійська.

Повний текст, джерела та переклади: https://theresmoretoit-channel.github.io/uk/videos/what-makes-a-battery-catch-fire/

Розділи
00:00 Знову загорілася батарея
00:40 Вона несе власне паливо
01:05 Що має зламатися першим
01:46 Усередині батареї телефона
02:25 Сепаратор
02:51 Чотири шляхи
03:04 Внутрішнє коротке замикання
03:32 Петля
03:52 Тепловий розгін
04:02 Що виходить назовні
04:31 Елементи ніколи не бувають самі
05:01 То чи вони небезпечні?
05:21 Як насправді виглядає рідкісне
05:52 Порахуйте батареї навколо себе
06:07 Знаменник
06:36 Батарея — це система
07:20 Що зробив Нью-Йорк
08:07 Чому просто не зробити їх безпечними?
08:33 Що буде далі
09:16 Назад до парадоксу

ДЖЕРЕЛА ЗОБРАЖЕНЬ
Lithium-ion laptop battery internals — Lead holder, CC BY-SA 3.0
Samsung Galaxy Note 7 rear — Pang Kakit, CC BY-SA 4.0
обидва через Wikimedia Commons
Ліцензії: creativecommons.org/licenses/by-sa/3.0
          creativecommons.org/licenses/by-sa/4.0
```

## Tiếng Việt (`vi`)

```
Điều gì khiến một viên pin bốc cháy?
```

```
Cứ vài ngày lại có thêm một câu chuyện về pin cháy. Một pin dự phòng
trên máy bay, một chiếc xe điện ở cầu thang, đôi khi là cả một tòa nhà.
Tiêu đề lúc nào cũng giống nhau: pin lithium-ion rất nguy hiểm. Vậy mà
bạn đang có một viên trong túi, một viên trong laptop và có lẽ một viên
đang đỗ ngoài kia, và gần như tất cả đều sống hết đời mình mà chẳng làm
gì cả.

Video này nói về điều thực sự phải hỏng trước. Một cell lithium mang
theo nhiên liệu của chính nó, hàn kín bên trong. Giữa hai điện cực là
một lớp màng nhựa mỏng dưới hai mươi micromet — mà nhựa thì chịu nhiệt
rất kém. Khi một vụ chập mạch làm nóng một điểm, lỗ thủng trên lớp màng
ấy to thêm, lỗ to hơn dẫn dòng lớn hơn, dòng lớn hơn sinh nhiệt nhiều
hơn, và chẳng có gì trong vòng lặp đó làm nó chậm lại. Đó là hiện tượng
thoát nhiệt.

Rồi đến nửa khó hơn: chuyện đó xảy ra thường xuyên đến đâu. Khi Samsung
thu hồi hai triệu rưỡi điện thoại vào năm 2016, số vụ được ghi nhận ở
Mỹ là chín mươi hai, trên khoảng một triệu máy bán ra tại đó. Một trên
mười nghìn đã đủ để khai tử một chiếc điện thoại đầu bảng và khiến nó bị
cấm trên máy bay. Ta thấy những lần hỏng hóc. Ta không bao giờ thấy mẫu
số — và ở New York, nơi những đám cháy này lấy đi mười tám mạng người
năm 2023, thứ thay đổi sau đó không phải hóa học mà là những viên pin
nào được phép ra thị trường.

Phụ đề được viết riêng cho video này, không phải tạo tự động. Có thêm
một bản âm thanh tiếng Anh Mỹ làm rãnh âm thanh thứ hai.

Toàn văn, nguồn và bản dịch: https://theresmoretoit-channel.github.io/vi/videos/what-makes-a-battery-catch-fire/

Các chương
00:00 Lại một viên pin bốc cháy
00:40 Nó mang theo nhiên liệu của chính nó
01:05 Cái gì phải hỏng trước
01:46 Bên trong viên pin điện thoại
02:25 Màng ngăn
02:51 Bốn lối vào
03:04 Chập mạch bên trong
03:32 Vòng lặp
03:52 Thoát nhiệt
04:02 Thứ thoát ra ngoài
04:31 Các cell không bao giờ đứng một mình
05:01 Vậy chúng có nguy hiểm không?
05:21 Hiếm thật sự trông như thế nào
05:52 Hãy đếm số pin quanh bạn
06:07 Mẫu số
06:36 Pin là một hệ thống
07:20 New York đã làm gì
08:07 Sao không làm cho chúng an toàn luôn?
08:33 Điều gì đến tiếp theo
09:16 Trở lại nghịch lý

NGUỒN HÌNH ẢNH
Lithium-ion laptop battery internals — Lead holder, CC BY-SA 3.0
Samsung Galaxy Note 7 rear — Pang Kakit, CC BY-SA 4.0
cả hai qua Wikimedia Commons
Giấy phép: creativecommons.org/licenses/by-sa/3.0
           creativecommons.org/licenses/by-sa/4.0
```

## čeština (`cs`)

```
Proč začne baterie hořet?
```

```
Každých pár dní se objeví další příběh o hořící baterii. Powerbanka v
letadle, koloběžka na schodišti, někdy celý dům. Titulek je pokaždé
stejný: lithium-iontové baterie jsou nebezpečné. A přitom jednu máte v
kapse, jednu v notebooku a nejspíš jednu zaparkovanou před domem, a
skoro všechny prožijí celý svůj život tím, že nedělají vůbec nic.

Tohle video je o tom, co se doopravdy musí pokazit. Lithiový článek si
nese vlastní palivo, zatavené uvnitř. Mezi oběma elektrodami leží
plastová fólie tenčí než dvacet mikrometrů — a plast horko moc nesnáší.
Jakmile zkrat rozžhaví jedno místo, díra v té fólii se zvětší, větší
dírou projde větší proud, větší proud vyrobí víc tepla a v té smyčce
není nic, co by to brzdilo. Tomu se říká tepelný únik.

Pak přijde těžší půlka: jak často se to stane. Když Samsung v roce 2016
stáhl dva a půl milionu telefonů, nahlášených případů bylo v Americe
devadesát dva — zhruba z milionu tam prodaných kusů. Jeden z deseti
tisíc stačil na to, aby skončil vlajkový telefon a aby ho zakázali v
letadlech. Vidíme ta selhání. Nikdy nevidíme jmenovatele — a v New
Yorku, kde tyhle požáry v roce 2023 zabily osmnáct lidí, se potom
nezměnila chemie, ale to, které baterie se smějí dostat na trh.

Titulky jsou k tomuhle videu napsané, ne strojově vygenerované. Jako druhá
zvuková stopa je k dispozici americká angličtina.

Celý text, zdroje a překlady: https://theresmoretoit-channel.github.io/cs/videos/what-makes-a-battery-catch-fire/

Kapitoly
00:00 Zase hořela baterie
00:40 Nese si vlastní palivo
01:05 Co se musí pokazit jako první
01:46 Uvnitř baterie z telefonu
02:25 Separátor
02:51 Čtyři cesty dovnitř
03:04 Vnitřní zkrat
03:32 Smyčka
03:52 Tepelný únik
04:02 Co jde ven
04:31 Články nikdy nejsou samy
05:01 Tak jsou nebezpečné?
05:21 Jak vypadá vzácná událost
05:52 Spočítejte baterie kolem sebe
06:07 Jmenovatel
06:36 Baterie je systém
07:20 Co udělal New York
08:07 Proč je prostě neudělat bezpečné?
08:33 Co přijde dál
09:16 Zpátky u paradoxu

ZDROJE OBRÁZKŮ
Lithium-ion laptop battery internals — Lead holder, CC BY-SA 3.0
Samsung Galaxy Note 7 rear — Pang Kakit, CC BY-SA 4.0
obojí přes Wikimedia Commons
Licence: creativecommons.org/licenses/by-sa/3.0
         creativecommons.org/licenses/by-sa/4.0
```

## español (`es`)

```
¿Qué hace que una batería arda?
```

```
Cada pocos días aparece otra historia de una batería en llamas. Una
batería externa en un avión, un patinete en una escalera, a veces un
edificio entero. El titular es siempre el mismo: las baterías de ion de
litio son peligrosas. Y sin embargo tienes una en el bolsillo, otra en
el portátil y seguramente otra aparcada fuera, y casi todas se pasan la
vida sin hacer absolutamente nada.

Este vídeo trata de lo que de verdad tiene que fallar. Una celda de
litio lleva su propio combustible, sellado en su interior. Entre los dos
electrodos hay una lámina de plástico de menos de veinte micrómetros, y
el plástico aguanta mal el calor. En cuanto un cortocircuito calienta un
punto, el agujero de esa lámina se agranda, un agujero mayor lleva más
corriente, más corriente genera más calor, y nada en ese bucle lo frena.
Eso es la fuga térmica.

Luego viene la mitad más difícil: con qué frecuencia ocurre. Cuando
Samsung retiró dos millones y medio de móviles en 2016, el número de
incidentes notificados en Estados Unidos fue noventa y dos, de alrededor
de un millón vendidos allí. Uno de cada diez mil bastó para acabar con
un móvil insignia y para que lo prohibieran en los aviones. Vemos los
fallos. Nunca vemos el denominador — y en Nueva York, donde estos
incendios mataron a dieciocho personas en 2023, lo que cambió después no
fue la química, sino qué baterías podían llegar al mercado.

Los subtítulos están escritos para este vídeo, no generados
automáticamente. Hay una segunda pista de audio en inglés americano.

Transcripción completa, fuentes y traducciones: https://theresmoretoit-channel.github.io/es/videos/what-makes-a-battery-catch-fire/

Capítulos
00:00 Otra batería ardió
00:40 Lleva su propio combustible
01:05 Qué tiene que fallar primero
01:46 Dentro de la batería de un móvil
02:25 El separador
02:51 Cuatro maneras
03:04 Un cortocircuito interno
03:32 El bucle
03:52 Fuga térmica
04:02 Lo que sale
04:31 Las celdas nunca están solas
05:01 Entonces, ¿son peligrosas?
05:21 Cómo es de verdad lo raro
05:52 Cuenta las baterías que te rodean
06:07 El denominador
06:36 Una batería es un sistema
07:20 Lo que hizo Nueva York
08:07 ¿Por qué no hacerlas seguras sin más?
08:33 Lo que viene después
09:16 De vuelta a la paradoja

CRÉDITOS DE IMÁGENES
Lithium-ion laptop battery internals — Lead holder, CC BY-SA 3.0
Samsung Galaxy Note 7 rear — Pang Kakit, CC BY-SA 4.0
ambas vía Wikimedia Commons
Licencias: creativecommons.org/licenses/by-sa/3.0
           creativecommons.org/licenses/by-sa/4.0
```

## svenska (`sv`)

```
Vad får ett batteri att fatta eld?
```

```
Med några dagars mellanrum kommer ännu en historia om ett brinnande
batteri. En powerbank på ett flygplan, en elsparkcykel i ett trapphus,
ibland ett helt hus. Rubriken är alltid densamma: litiumjonbatterier är
farliga. Ändå har du ett i fickan, ett i laptopen och troligen ett
parkerat utanför, och nästan alla tillbringar hela sitt liv med att inte
göra någonting alls.

Den här videon handlar om vad som faktiskt måste gå fel. En litiumcell
bär med sig sitt eget bränsle, inneslutet inuti. Mellan de två
elektroderna ligger en plastfilm tunnare än tjugo mikrometer — och plast
tål hetta dåligt. Så snart en kortslutning gör en punkt het växer hålet
i den filmen, ett större hål leder mer ström, mer ström ger mer värme,
och inget i den slingan bromsar den. Det kallas termisk rusning.

Sedan den svårare halvan: hur ofta det händer. När Samsung återkallade
två och en halv miljon telefoner 2016 var antalet rapporterade
incidenter i USA nittiotvå, av ungefär en miljon sålda där. En på
tiotusen räckte för att ta död på en flaggskeppstelefon och få den
förbjuden på flygplan. Vi ser felen. Vi ser aldrig nämnaren — och i New
York, där dessa bränder dödade arton människor 2023, var det som
ändrades efteråt inte kemin utan vilka batterier som fick nå marknaden.

Undertexterna är skrivna för den här videon, inte automatgenererade. Som
andra ljudspår finns amerikansk engelska.

Hela texten, källor och översättningar: https://theresmoretoit-channel.github.io/sv/videos/what-makes-a-battery-catch-fire/

Kapitel
00:00 Ännu ett batteri brann
00:40 Det bär sitt eget bränsle
01:05 Vad som måste gå fel först
01:46 Inuti ett telefonbatteri
02:25 Separatorn
02:51 Fyra vägar in
03:04 En intern kortslutning
03:32 Slingan
03:52 Termisk rusning
04:02 Vad som kommer ut
04:31 Celler är aldrig ensamma
05:01 Så, är de farliga?
05:21 Hur sällsynt faktiskt ser ut
05:52 Räkna batterierna omkring dig
06:07 Nämnaren
06:36 Ett batteri är ett system
07:20 Vad New York gjorde
08:07 Varför inte bara göra dem säkra?
08:33 Vad som kommer härnäst
09:16 Tillbaka till paradoxen

BILDKÄLLOR
Lithium-ion laptop battery internals — Lead holder, CC BY-SA 3.0
Samsung Galaxy Note 7 rear — Pang Kakit, CC BY-SA 4.0
båda via Wikimedia Commons
Licenser: creativecommons.org/licenses/by-sa/3.0
          creativecommons.org/licenses/by-sa/4.0
```
