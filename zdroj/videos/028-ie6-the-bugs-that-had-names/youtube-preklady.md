# Lokalizované názvy a popisy — Internet Explorer 6: The Bugs That Had Names

Podklad pro **YouTube Studio → video → Podrobnosti → Přidat jazyk**.
Pro každý jazyk jsou tu **dva bloky ke zkopírování**: název a popis.
Kopíruje se **celý blok mezi trojicí zpětných apostrofů**, co je mimo něj,
je poznámka. Anglický originál zůstává v `youtube.md` a nesahá se na něj.

## Co se NEPŘEKLÁDÁ

| | |
|---|---|
| **jména chyb** | *Peekaboo*, *The Guillotine*, *The Three Pixel Jog*, *The Double Margin Bug*, *The Duplicate Character Bug*, *Magic Creeping Text*, *Border Chaos*, *The Holly Hack*, *star hack*, *underscore hack*, *spacer gif* — **celé video je o tom, že to jsou vlastní jména.** Přeložit je znamená zrušit tezi |
| **`hasLayout`, `zoom: 1`, `* html`** | zápisy v kódu |
| **Internet Explorer 6, Windows XP, Microsoft, Google, Dean Edwards, Denver** | vlastní jména |
| **časy kapitol** | musí sedět na vteřinu, jinak je YouTube neuzná |
| **tagy** | YouTube je per-jazyk nemá |
| **odkaz na první díl** | `https://youtu.be/R7Un3IOMvbg` |

## Kontrola čísel

V popisu jsou tři: **4172** (číslo tiketu, drží vtip o tom, že si ho nikdo
nepamatuje), **6** v názvu prohlížeče a **tři slova** HTML v posledním
odstavci. Musí být v každém překladu a nesmí se změnit.

Kapitol je **třicet** a časy se nepřekládají.

> **Obrazové zdroje tu nejsou a chybět nemají.** Tohle video nemá ani jeden
> archivní snímek (84 diagramů kreslených kódem a 2 malované SDXL scény),
> takže `sources.json` neexistuje a atribuovat není co. Místo sekce
> `OBRAZOVÉ ZDROJE` je v popisu jedna věta, že je všechno kreslené.

---

## suomi (`fi`)

```
Internet Explorer 6 — virheet, joilla oli nimet
```

```
Yleensä selainvirhe on numero seurantajärjestelmässä. Issue 4172. Kukaan ei muista sitä, kukaan ei puhu siitä lounaalla.

Internet Explorer 6:ssa virheillä oli erisnimet. Peekaboo. The Guillotine. The Three Pixel Jog. The Duplicate Character Bug. Ja se osoittautuu koko aikakauden paljastavimmaksi asiaksi: et anna nimeä virheelle, jonka kohtaat kerran.

Tämä on osa kaksi. Se kertoo siitä, mitä tuon alustan sisällä eläminen oikeasti tarkoitti — nimetyt virheet, useimpien virheiden taustalla oleva näkymätön lippu, CSS-kikat, jotka kirjoitettiin yhtä selainta varten, korjaus, joka oli tarkoituksellinen kirjoitusvirhe, ja ne kolme HTML-sanaa, jotka saattoivat sulkea ikkunan omalla koneellasi.

Osa yksi — kuinka Internet Explorer 6:sta ylipäätään tuli alusta:
https://youtu.be/R7Un3IOMvbg

Luvut
00:00 Osa kaksi
00:36 Virhe, jolla on numero
00:57 The Three Pixel Jog
01:17 The Double Margin Bug
01:44 Peekaboo
02:10 The Guillotine
02:32 The Duplicate Character Bug
03:00 The Expanding Box
03:27 Et anna nimeä virheelle, jonka kohtaat kerran
03:48 hasLayout
04:27 The Holly Hack
04:54 zoom: 1
05:14 Puhuminen yhdelle selaimelle
05:54 Alaviivakikka
06:15 Ehdolliset kommentit
06:45 Quirks mode
07:21 Läpinäkyvyys
07:59 Taulukot ja spacer gif
08:19 Hover ja tiedosto sivun vieressä
08:47 JavaScript tyylitiedostossa
09:04 Kattoja, joita kenelläkään muulla ei ollut
09:30 Muistivuoto
09:55 Puuttuva yhtäläisyysmerkki
10:34 Ulos selaimesta
11:12 Yksi kone, yksi versio
11:34 Kirjasto selaimen paikkaamiseen
11:48 Mitä se maksoi
12:31 Hautajaiset
12:48 Vuotta myöhemmin
13:12 Miksi virheillä oli nimet

Jokainen tämän videon kuva on piirretty koodilla tai maalattu; arkistovalokuvia ei ole,
joten mitään ei ole tarpeen mainita lähteenä.

Tekstitykset on kirjoitettu tätä videota varten, ei luotu automaattisesti. Toisena ääniraitana on amerikanenglanti.

There's More To It
```

## français (`fr`)

Název:

```
Internet Explorer 6 — Les bugs qui avaient des noms
```

Popis:

```
Un bug de navigateur, normalement, c'est un numéro dans un outil de suivi.
Issue 4172. Personne ne s'en souvient, personne n'en parle au déjeuner.

Dans Internet Explorer 6, les bugs avaient des noms propres. Peekaboo.
The Guillotine. The Three Pixel Jog. The Duplicate Character Bug. Et c'est,
il se trouve, ce qu'il y a de plus révélateur sur toute cette époque : on ne
donne pas de nom à un bug qu'on ne rencontre qu'une fois.

Ceci est la deuxième partie. Elle parle de ce que vivre dans cette
plateforme voulait vraiment dire : les bugs nommés, le drapeau invisible
sous la plupart d'entre eux, les hacks écrits pour s'adresser à un seul
navigateur, la correction qui était une faute de frappe volontaire, et les
trois mots de HTML capables de fermer une fenêtre sur ta propre machine.

La première partie, sur la façon dont Internet Explorer 6 est devenu une
plateforme : https://youtu.be/R7Un3IOMvbg

Chapitres
00:00 Deuxième partie
00:36 Un bug avec un numéro
00:57 The Three Pixel Jog
01:17 The Double Margin Bug
01:44 Peekaboo
02:10 The Guillotine
02:32 The Duplicate Character Bug
03:00 La boîte qui grandit
03:27 On ne nomme pas un bug rencontré une seule fois
03:48 hasLayout
04:27 The Holly Hack
04:54 zoom: 1
05:14 Parler à un seul navigateur
05:54 Le underscore hack
06:15 Les commentaires conditionnels
06:45 Le mode quirks
07:21 La transparence
07:59 Les tableaux et le spacer gif
08:19 Le survol et un fichier à côté de la page
08:47 Du JavaScript dans une feuille de style
09:04 Des plafonds que personne d'autre n'avait
09:30 La fuite de mémoire
09:55 Le signe égal manquant
10:34 Hors du navigateur
11:12 Une machine, une version
11:34 Une bibliothèque qui rapièce le navigateur
11:48 Ce que ça a coûté
12:31 Les funérailles
12:48 Un an plus tard
13:12 Pourquoi les bugs avaient des noms

Toutes les images de cette vidéo sont dessinées par code ou peintes ; il n'y
a aucune photographie d'archive, donc rien à attribuer.

Les sous-titres sont écrits pour cette vidéo, pas générés automatiquement. Une piste audio en anglais américain est disponible en seconde piste.

There's More To It
```

> **Zpětný překlad kapitol (nekopírovat):** Deuxième partie / Un bug avec un
> numéro / La boîte qui grandit = „Rostoucí rámeček" / Parler à un seul
> navigateur = „Mluvit na jediný prohlížeč" / Des plafonds que personne
> d'autre n'avait = „Stropy, které neměl nikdo jiný" / La fuite de mémoire =
> „Únik paměti" / Le signe égal manquant = „Chybějící rovnítko".

---

## Bahasa Indonesia (`id`)

```
Internet Explorer 6 — Bug-Bug yang Punya Nama
```

```
Biasanya bug browser hanyalah sebuah nomor dalam sistem pelacakan bug. Issue 4172. Tidak ada yang mengingatnya, tidak ada yang membicarakannya saat makan siang.

Di Internet Explorer 6, bug-bug itu punya nama diri. Peekaboo. The Guillotine. The Three Pixel Jog. The Duplicate Character Bug. Dan justru itulah hal yang paling menggambarkan seluruh era itu: kamu tidak menamai bug yang cuma kamu temui sekali.

Ini bagian dua. Isinya tentang apa artinya benar-benar hidup di dalam platform itu — bug-bug bernama, flag tak kasatmata di balik sebagian besarnya, hack yang ditulis demi menjangkau satu browser, perbaikan yang sengaja berupa salah ketik, dan tiga kata HTML yang bisa menutup sebuah jendela di mesinmu sendiri.

Bagian satu — bagaimana Internet Explorer 6 bisa menjadi sebuah platform:
https://youtu.be/R7Un3IOMvbg

Bab
00:00 Bagian dua
00:36 Bug dengan sebuah nomor
00:57 The Three Pixel Jog
01:17 The Double Margin Bug
01:44 Peekaboo
02:10 The Guillotine
02:32 The Duplicate Character Bug
03:00 The Expanding Box
03:27 Kamu tidak menamai bug yang cuma ditemui sekali
03:48 hasLayout
04:27 The Holly Hack
04:54 zoom: 1
05:14 Berbicara kepada satu browser
05:54 Hack garis bawah
06:15 Komentar bersyarat
06:45 Quirks mode
07:21 Transparansi
07:59 Tabel dan spacer gif
08:19 Hover, dan sebuah berkas di sebelah halaman
08:47 JavaScript di dalam stylesheet
09:04 Batas-batas yang tidak dimiliki orang lain
09:30 Kebocoran memori
09:55 Tanda sama dengan yang hilang
10:34 Keluar dari browser
11:12 Satu mesin, satu versi
11:34 Pustaka untuk menambal browser
11:48 Berapa harganya
12:31 Pemakaman
12:48 Setahun kemudian
13:12 Kenapa bug-bug itu punya nama

Setiap gambar dalam video ini digambar dengan kode atau dibuat sebagai lukisan; tidak ada foto arsip,
jadi tidak ada yang perlu diatribusikan.

Subtitel ditulis khusus untuk video ini, bukan dibuat secara otomatis. Tersedia juga trek audio kedua dalam bahasa Inggris Amerika.

There's More To It
```

## italiano (`it`)

Název:

```
Internet Explorer 6 — I bug che avevano un nome
```

Popis:

```
Un bug di un browser normalmente è un numero in un tracker. Issue 4172.
Nessuno se lo ricorda, nessuno ne parla a pranzo.

In Internet Explorer 6 i bug avevano nomi propri. Peekaboo. The Guillotine.
The Three Pixel Jog. The Duplicate Character Bug. E si scopre che è la cosa
più rivelatrice di tutta quell'epoca: a un bug che incontri una volta non
dai un nome.

Questa è la seconda parte. Parla di cosa volesse davvero dire vivere dentro
quella piattaforma: i bug con un nome, il flag invisibile sotto quasi tutti,
i trucchi scritti per parlare a un solo browser, la correzione che era un
refuso di proposito, e le tre parole di HTML capaci di chiudere una finestra
sulla tua stessa macchina.

La prima parte, su come Internet Explorer 6 sia diventato una piattaforma:
https://youtu.be/R7Un3IOMvbg

Capitoli
00:00 Parte due
00:36 Un bug con un numero
00:57 The Three Pixel Jog
01:17 The Double Margin Bug
01:44 Peekaboo
02:10 The Guillotine
02:32 The Duplicate Character Bug
03:00 Il riquadro che cresce
03:27 A un bug che incontri una volta non dai un nome
03:48 hasLayout
04:27 The Holly Hack
04:54 zoom: 1
05:14 Parlare a un solo browser
05:54 L'underscore hack
06:15 I commenti condizionali
06:45 La modalità quirks
07:21 La trasparenza
07:59 Le tabelle e lo spacer gif
08:19 Il passaggio del mouse e un file accanto alla pagina
08:47 JavaScript dentro un foglio di stile
09:04 Tetti che non aveva nessun altro
09:30 La perdita di memoria
09:55 Il segno di uguale mancante
10:34 Fuori dal browser
11:12 Una macchina, una versione
11:34 Una libreria che rattoppa il browser
11:48 Quanto è costato
12:31 Il funerale
12:48 Un anno dopo
13:12 Perché i bug avevano un nome

Ogni immagine di questo video è disegnata da codice o dipinta; non ci sono
fotografie d'archivio, quindi non c'è nulla da attribuire.

I sottotitoli sono scritti per questo video, non generati automaticamente. Come seconda traccia audio è disponibile l’inglese americano.

There's More To It
```

> **Zpětný překlad kapitol (nekopírovat):** Parte due / Un bug con un numero /
> Il riquadro che cresce = „Rostoucí rámeček" / Parlare a un solo browser =
> „Mluvit na jediný prohlížeč" / Tetti che non aveva nessun altro = „Stropy,
> které neměl nikdo jiný" / La perdita di memoria = „Únik paměti".

---

## Deutsch (`de`)

Název:

```
Internet Explorer 6 — Die Bugs, die Namen hatten
```

Popis:

```
Ein Browser-Bug ist normalerweise eine Nummer in einem Ticketsystem.
Issue 4172. Niemand erinnert sich daran, niemand redet beim Mittagessen
darüber.

Im Internet Explorer 6 hatten die Bugs Eigennamen. Peekaboo. The Guillotine.
The Three Pixel Jog. The Duplicate Character Bug. Und das ist, wie sich
zeigt, das Aufschlussreichste an dieser ganzen Zeit: einen Bug, dem man
einmal begegnet, benennt man nicht.

Das ist Teil zwei. Es geht darum, wie es wirklich war, in dieser Plattform
zu leben — um die benannten Bugs, um das unsichtbare Flag unter den meisten
von ihnen, um Hacks, die geschrieben wurden, um genau einen Browser
anzusprechen, um die Lösung, die ein absichtlicher Tippfehler war, und um
die drei Wörter HTML, die ein Fenster auf deinem eigenen Rechner schließen
konnten.

Teil eins, darüber, wie der Internet Explorer 6 überhaupt zur Plattform
wurde: https://youtu.be/R7Un3IOMvbg

Kapitel
00:00 Teil zwei
00:36 Ein Bug mit einer Nummer
00:57 The Three Pixel Jog
01:17 The Double Margin Bug
01:44 Peekaboo
02:10 The Guillotine
02:32 The Duplicate Character Bug
03:00 Der wachsende Kasten
03:27 Einen Bug, dem man einmal begegnet, benennt man nicht
03:48 hasLayout
04:27 The Holly Hack
04:54 zoom: 1
05:14 Mit einem einzigen Browser sprechen
05:54 Der underscore hack
06:15 Bedingte Kommentare
06:45 Quirks Mode
07:21 Transparenz
07:59 Tabellen und das spacer gif
08:19 Hover und eine Datei neben der Seite
08:47 JavaScript im Stylesheet
09:04 Obergrenzen, die sonst niemand hatte
09:30 Das Speicherleck
09:55 Das fehlende Gleichheitszeichen
10:34 Raus aus dem Browser
11:12 Ein Rechner, eine Version
11:34 Eine Bibliothek, die den Browser flickt
11:48 Was es gekostet hat
12:31 Die Beerdigung
12:48 Ein Jahr später
13:12 Warum die Bugs Namen hatten

Jedes Bild in diesem Video ist aus Code gezeichnet oder gemalt; es gibt
keine Archivfotos, also gibt es nichts zu attribuieren.

Die Untertitel wurden für dieses Video geschrieben, nicht automatisch erzeugt. Als zweite Tonspur steht amerikanisches Englisch bereit.

There's More To It
```

> **Zpětný překlad kapitol (nekopírovat):** Zweiter Teil / Ein Bug mit einer
> Nummer / … / Der wachsende Kasten = „Rostoucí rámeček" / Mit einem einzigen
> Browser sprechen = „Mluvit s jediným prohlížečem" / Obergrenzen, die sonst
> niemand hatte = „Stropy, které neměl nikdo jiný" / Das Speicherleck =
> „Únik paměti" / Warum die Bugs Namen hatten = „Proč měly ty chyby jména".

---

## polski (`pl`)

Název:

```
Internet Explorer 6 — Błędy, które miały imiona
```

Popis:

```
Błąd przeglądarki to normalnie numer w systemie zgłoszeń. Issue 4172. Nikt
go nie pamięta, nikt o nim nie mówi przy obiedzie.

W Internet Explorerze 6 błędy miały nazwy własne. Peekaboo. The Guillotine.
The Three Pixel Jog. The Duplicate Character Bug. I okazuje się, że to
najbardziej wymowna rzecz w całej tamtej epoce: błędowi, którego spotykasz
raz, nie nadaje się imienia.

To jest część druga. Jest o tym, jak naprawdę wyglądało życie wewnątrz tej
platformy: o nazwanych błędach, o niewidzialnej fladze pod większością z
nich, o sztuczkach pisanych po to, żeby odezwać się do jednej jedynej
przeglądarki, o poprawce, która była celową literówką, i o trzech słowach
HTML, które potrafiły zamknąć okno na twoim własnym komputerze.

Część pierwsza, o tym, jak Internet Explorer 6 w ogóle stał się platformą:
https://youtu.be/R7Un3IOMvbg

Rozdziały
00:00 Część druga
00:36 Błąd, który ma numer
00:57 The Three Pixel Jog
01:17 The Double Margin Bug
01:44 Peekaboo
02:10 The Guillotine
02:32 The Duplicate Character Bug
03:00 Rosnąca ramka
03:27 Błędowi, którego spotykasz raz, nie nadaje się imienia
03:48 hasLayout
04:27 The Holly Hack
04:54 zoom: 1
05:14 Jak mówić do jednej przeglądarki
05:54 Underscore hack
06:15 Komentarze warunkowe
06:45 Tryb quirks
07:21 Przezroczystość
07:59 Tabele i spacer gif
08:19 Najechanie myszą i plik obok strony
08:47 JavaScript w arkuszu stylów
09:04 Sufity, których nie miał nikt inny
09:30 Wyciek pamięci
09:55 Brakujący znak równości
10:34 Poza przeglądarką
11:12 Jedna maszyna, jedna wersja
11:34 Biblioteka, która łata przeglądarkę
11:48 Ile to kosztowało
12:31 Pogrzeb
12:48 Rok później
13:12 Dlaczego błędy miały imiona

Każdy obraz w tym filmie jest rysowany kodem albo malowany; nie ma tu
żadnych zdjęć archiwalnych, więc nie ma czego przypisywać.

Napisy są pisane do tego filmu, nie generowane automatycznie. Jako druga ścieżka dźwiękowa dostępny jest angielski amerykański.

There's More To It
```

> **Zpětný překlad kapitol (nekopírovat):** Część druga / Błąd, który ma
> numer / Rosnąca ramka = „Rostoucí rámeček" / Jak mówić do jednej
> przeglądarki = „Jak mluvit na jediný prohlížeč" / Sufity, których nie miał
> nikt inny = „Stropy, které neměl nikdo jiný" / Wyciek pamięci = „Únik
> paměti" / Brakujący znak równości = „Chybějící rovnítko".

---

## português (Brasil) (`pt-BR`)

Název:

```
Internet Explorer 6 — Os bugs que tinham nome
```

Popis:

```
Um bug de navegador normalmente é um número num sistema de chamados.
Issue 4172. Ninguém lembra dele, ninguém fala dele no almoço.

No Internet Explorer 6 os bugs tinham nomes próprios. Peekaboo.
The Guillotine. The Three Pixel Jog. The Duplicate Character Bug. E acontece
que isso é a coisa mais reveladora de toda aquela época: você não dá nome a
um bug que encontra uma vez.

Esta é a parte dois. É sobre o que significava de verdade viver dentro
daquela plataforma: os bugs com nome, a flag invisível embaixo de quase
todos, os truques escritos para falar com um único navegador, a correção que
era um erro de digitação de propósito, e as três palavras de HTML capazes de
fechar uma janela na sua própria máquina.

A parte um, sobre como o Internet Explorer 6 virou uma plataforma:
https://youtu.be/R7Un3IOMvbg

Capítulos
00:00 Parte dois
00:36 Um bug com número
00:57 The Three Pixel Jog
01:17 The Double Margin Bug
01:44 Peekaboo
02:10 The Guillotine
02:32 The Duplicate Character Bug
03:00 A caixa que cresce
03:27 Você não dá nome a um bug que encontra uma vez
03:48 hasLayout
04:27 The Holly Hack
04:54 zoom: 1
05:14 Falar com um único navegador
05:54 O underscore hack
06:15 Comentários condicionais
06:45 Modo quirks
07:21 Transparência
07:59 Tabelas e o spacer gif
08:19 O hover e um arquivo ao lado da página
08:47 JavaScript dentro da folha de estilo
09:04 Tetos que ninguém mais tinha
09:30 O vazamento de memória
09:55 O sinal de igual que faltou
10:34 Fora do navegador
11:12 Uma máquina, uma versão
11:34 Uma biblioteca que remenda o navegador
11:48 O que custou
12:31 O funeral
12:48 Um ano depois
13:12 Por que os bugs tinham nome

Todas as imagens deste vídeo são desenhadas por código ou pintadas; não há
fotografias de arquivo, então não há nada a atribuir.

As legendas foram escritas para este vídeo, não geradas automaticamente. Como segunda faixa de áudio está disponível o inglês americano.

There's More To It
```

> **Zpětný překlad kapitol (nekopírovat):** Parte dois / Um bug com número /
> A caixa que cresce = „Rostoucí rámeček" / Falar com um único navegador =
> „Mluvit s jediným prohlížečem" / Tetos que ninguém mais tinha = „Stropy,
> které neměl nikdo jiný" / O vazamento de memória = „Únik paměti".

---

## Türkçe (`tr`)

```
Internet Explorer 6 — Adı Olan Hatalar
```

```
Normalde bir tarayıcı hatası, takip sisteminde bir numaradır. Issue 4172. Kimse hatırlamaz, kimse öğle yemeğinde ondan söz etmez.

Internet Explorer 6’da hataların özel adları vardı. Peekaboo. The Guillotine. The Three Pixel Jog. The Duplicate Character Bug. Ve bütün o dönem hakkında en çok şeyi ele veren de bu: bir kez karşılaştığın hataya isim vermezsin.

Bu ikinci bölüm. O platformun içinde yaşamanın gerçekte ne demek olduğunu anlatıyor — adı olan hatalar, çoğunun altındaki görünmez bayrak, tek bir tarayıcıya ulaşmak için yazılan hileler, bilerek yapılmış bir yazım hatası olan düzeltme ve kendi makinende bir pencereyi kapatabilen üç kelimelik HTML.

Birinci bölüm — Internet Explorer 6 en başta nasıl bir platforma dönüştü:
https://youtu.be/R7Un3IOMvbg

Bölümler
00:00 İkinci bölüm
00:36 Numarası olan bir hata
00:57 The Three Pixel Jog
01:17 The Double Margin Bug
01:44 Peekaboo
02:10 The Guillotine
02:32 The Duplicate Character Bug
03:00 The Expanding Box
03:27 Bir kez karşılaştığın hataya isim vermezsin
03:48 hasLayout
04:27 The Holly Hack
04:54 zoom: 1
05:14 Tek bir tarayıcıyla konuşmak
05:54 Alt çizgi hilesi
06:15 Koşullu yorumlar
06:45 Quirks mode
07:21 Saydamlık
07:59 Tablolar ve spacer gif
08:19 Hover ve sayfanın yanındaki bir dosya
08:47 Stil dosyasının içinde JavaScript
09:04 Diğer tarayıcılarda olmayan sınırlar
09:30 Bellek sızıntısı
09:55 Eksik eşittir işareti
10:34 Tarayıcının dışına
11:12 Tek makine, tek sürüm
11:34 Tarayıcıyı yamamak için bir kütüphane
11:48 Neye mal oldu
12:31 Cenaze
12:48 Bir yıl sonra
13:12 Hataların neden adı vardı

Bu videodaki her görsel kodla çizildi ya da resmedildi; arşiv fotoğrafı yok, dolayısıyla
atıf verilecek bir şey de yok.

Altyazılar bu video için yazıldı, otomatik olarak oluşturulmadı. İkinci ses parçası olarak Amerikan İngilizcesi de mevcut.

There's More To It
```

## українська (`uk`)

```
Internet Explorer 6 — помилки, які мали імена
```

```
Зазвичай помилка браузера — це номер у трекері. Issue 4172. Ніхто її не пам’ятає, ніхто про неї не говорить за обідом.

В Internet Explorer 6 помилки мали власні імена. Peekaboo. The Guillotine. The Three Pixel Jog. The Duplicate Character Bug. І саме це найкраще характеризує всю ту епоху: помилці, яку зустрів один раз, імені не даєш.

Це друга частина. Вона про те, що насправді означало жити всередині тієї платформи — іменовані помилки, невидимий прапорець під більшістю з них, хаки, написані заради одного браузера, виправлення, яке було навмисною одруківкою, і ті три слова HTML, які могли закрити вікно на твоїй власній машині.

Частина перша — як Internet Explorer 6 узагалі став платформою:
https://youtu.be/R7Un3IOMvbg

Розділи
00:00 Частина друга
00:36 Помилка з номером
00:57 The Three Pixel Jog
01:17 The Double Margin Bug
01:44 Peekaboo
02:10 The Guillotine
02:32 The Duplicate Character Bug
03:00 The Expanding Box
03:27 Помилці, яку зустрів раз, імені не даєш
03:48 hasLayout
04:27 The Holly Hack
04:54 zoom: 1
05:14 Розмова з одним браузером
05:54 Хак із підкресленням
06:15 Умовні коментарі
06:45 Quirks mode
07:21 Прозорість
07:59 Таблиці й spacer gif
08:19 Hover і файл поряд зі сторінкою
08:47 JavaScript у таблиці стилів
09:04 Стелі, яких не мав більше ніхто
09:30 Витік пам’яті
09:55 Відсутній знак дорівнює
10:34 Поза браузером
11:12 Одна машина, одна версія
11:34 Бібліотека, щоб залатати браузер
11:48 Скільки це коштувало
12:31 Похорон
12:48 Через рік
13:12 Чому помилки мали імена

Кожне зображення в цьому відео створене за допомогою коду або виконане як живопис; архівних світлин немає,
тож і атрибутувати нема чого.

Субтитри написані для цього відео, а не згенеровані автоматично. Також доступна друга звукова доріжка — американською англійською.

There's More To It
```

## Tiếng Việt (`vi`)

```
Internet Explorer 6 — Những lỗi có tên riêng
```

```
Thông thường một lỗi trình duyệt chỉ là một con số trong hệ theo dõi. Issue 4172. Chẳng ai nhớ nó, chẳng ai nhắc tới nó trong bữa trưa.

Ở Internet Explorer 6, các lỗi có hẳn tên riêng. Peekaboo. The Guillotine. The Three Pixel Jog. The Duplicate Character Bug. Và hóa ra đó là điều nói lên nhiều nhất về cả thời kỳ ấy: bạn không đặt tên cho một lỗi chỉ gặp đúng một lần.

Đây là phần hai. Nó nói về việc sống bên trong nền tảng đó thực sự có nghĩa là gì — những lỗi có tên, cái cờ vô hình nằm dưới phần lớn trong số chúng, các thủ thuật được viết riêng cho một trình duyệt, bản sửa lỗi vốn là một lỗi đánh máy cố ý, và ba chữ HTML có thể đóng một cửa sổ ngay trên máy của bạn.

Phần một — Internet Explorer 6 đã trở thành một nền tảng như thế nào:
https://youtu.be/R7Un3IOMvbg

Các chương
00:00 Phần hai
00:36 Một lỗi mang số hiệu
00:57 The Three Pixel Jog
01:17 The Double Margin Bug
01:44 Peekaboo
02:10 The Guillotine
02:32 The Duplicate Character Bug
03:00 The Expanding Box
03:27 Bạn không đặt tên cho lỗi chỉ gặp một lần
03:48 hasLayout
04:27 The Holly Hack
04:54 zoom: 1
05:14 Nói chuyện với một trình duyệt
05:54 Thủ thuật dấu gạch dưới
06:15 Chú thích điều kiện
06:45 Quirks mode
07:21 Độ trong suốt
07:59 Bảng và ảnh spacer gif
08:19 Hover, và một tệp nằm cạnh trang
08:47 JavaScript trong tệp CSS
09:04 Những trần giới hạn không ai khác có
09:30 Rò rỉ bộ nhớ
09:55 Dấu bằng bị thiếu
10:34 Ra khỏi trình duyệt
11:12 Một máy, một phiên bản
11:34 Một thư viện để vá trình duyệt
11:48 Nó tốn những gì
12:31 Đám tang
12:48 Một năm sau
13:12 Vì sao những lỗi ấy có tên

Mọi hình ảnh trong video này đều được vẽ bằng mã hoặc dưới dạng tranh; không có ảnh tư liệu nào,
nên cũng chẳng có gì phải ghi nguồn.

Phụ đề được viết riêng cho video này, không phải tạo tự động. Có thể chọn tiếng Anh Mỹ ở bản âm thanh thứ hai.

There's More To It
```

## čeština (`cs`)

Název:

```
Internet Explorer 6 — Chyby, které měly jména
```

Popis:

```
Chyba v prohlížeči je normálně číslo v trackeru. Issue 4172. Nikdo si ji
nepamatuje, nikdo o ní nemluví u oběda.

V Internet Exploreru 6 měly chyby vlastní jména. Peekaboo. The Guillotine.
The Three Pixel Jog. The Duplicate Character Bug. A ukazuje se, že je to ta
nejvýmluvnější věc na celé té době: chybu, kterou potkáš jednou,
nepojmenováváš.

Tohle je druhý díl. Je o tom, jaké to doopravdy bylo uvnitř té platformy
žít — o pojmenovaných chybách, o neviditelném příznaku, který byl pod
většinou z nich, o hacích psaných proto, aby se dalo mluvit na jediný
prohlížeč, o opravě, která byla schválně napsaný překlep, a o třech slovech
HTML, která uměla zavřít okno na tvém vlastním počítači.

První díl, o tom, jak se z Internet Exploreru 6 vůbec stala platforma:
https://youtu.be/R7Un3IOMvbg

Kapitoly
00:00 Druhý díl
00:36 Chyba, která má číslo
00:57 The Three Pixel Jog
01:17 The Double Margin Bug
01:44 Peekaboo
02:10 The Guillotine
02:32 The Duplicate Character Bug
03:00 Rostoucí rámeček
03:27 Chybu, kterou potkáš jednou, nepojmenováváš
03:48 hasLayout
04:27 The Holly Hack
04:54 zoom: 1
05:14 Jak mluvit na jediný prohlížeč
05:54 Underscore hack
06:15 Podmíněné komentáře
06:45 Quirks mode
07:21 Průhlednost
07:59 Tabulky a spacer gif
08:19 Najetí myší a soubor vedle stránky
08:47 JavaScript uvnitř stylopisu
09:04 Stropy, které neměl nikdo jiný
09:30 Únik paměti
09:55 Chybějící rovnítko
10:34 Ven z prohlížeče
11:12 Jeden stroj, jedna verze
11:34 Knihovna, která záplatuje prohlížeč
11:48 Co to stálo
12:31 Pohřeb
12:48 O rok později
13:12 Proč měly ty chyby jména

Každý obrázek v tomhle videu je kreslený kódem nebo malovaný; nejsou tu
žádné archivní fotografie, takže není co atribuovat.

Titulky jsou psané pro tohle video, ne strojový přepis. Jako druhá zvuková stopa je k dispozici americká angličtina.

There's More To It
```

---

## español (`es`)

Název:

```
Internet Explorer 6 — Los errores que tenían nombre
```

Popis:

```
Un error de navegador normalmente es un número en un gestor de incidencias.
Issue 4172. Nadie lo recuerda, nadie habla de él en la comida.

En Internet Explorer 6 los errores tenían nombres propios. Peekaboo.
The Guillotine. The Three Pixel Jog. The Duplicate Character Bug. Y resulta
que eso es lo más revelador de toda aquella época: a un error que te
encuentras una vez no le pones nombre.

Esta es la segunda parte. Va sobre lo que significaba de verdad vivir dentro
de aquella plataforma: los errores con nombre, la bandera invisible que
estaba debajo de casi todos, los trucos escritos para hablarle a un solo
navegador, el arreglo que era una errata a propósito, y las tres palabras de
HTML que podían cerrar una ventana en tu propia máquina.

La primera parte, sobre cómo Internet Explorer 6 llegó a ser una plataforma:
https://youtu.be/R7Un3IOMvbg

Capítulos
00:00 Segunda parte
00:36 Un error con número
00:57 The Three Pixel Jog
01:17 The Double Margin Bug
01:44 Peekaboo
02:10 The Guillotine
02:32 The Duplicate Character Bug
03:00 La caja que crece
03:27 A un error que encuentras una vez no le pones nombre
03:48 hasLayout
04:27 The Holly Hack
04:54 zoom: 1
05:14 Hablarle a un solo navegador
05:54 El underscore hack
06:15 Comentarios condicionales
06:45 Quirks mode
07:21 Transparencia
07:59 Tablas y el spacer gif
08:19 El hover y un archivo al lado de la página
08:47 JavaScript dentro de la hoja de estilo
09:04 Techos que no tenía nadie más
09:30 La fuga de memoria
09:55 El signo igual que falta
10:34 Fuera del navegador
11:12 Una máquina, una versión
11:34 Una biblioteca que parchea el navegador
11:48 Lo que costó
12:31 El funeral
12:48 Un año después
13:12 Por qué los errores tenían nombre

Todas las imágenes de este vídeo están dibujadas con código o pintadas; no
hay fotografías de archivo, así que no hay nada que atribuir.

Los subtítulos están escritos para este vídeo, no generados automáticamente. Como segunda pista de audio está disponible el inglés americano.

There's More To It
```

> **Zpětný překlad kapitol (nekopírovat):** Segunda parte / Un error con
> número / La caja que crece = „Rostoucí rámeček" / Hablarle a un solo
> navegador = „Mluvit na jediný prohlížeč" / Techos que no tenía nadie más =
> „Stropy, které neměl nikdo jiný" / La fuga de memoria = „Únik paměti" /
> El signo igual que falta = „Chybějící rovnítko".

---

## svenska (`sv`)

Název:

```
Internet Explorer 6 — Buggarna som hade namn
```

Popis:

```
En webbläsarbugg är normalt ett nummer i ett ärendesystem. Issue 4172. Ingen
minns den, ingen pratar om den vid lunchen.

I Internet Explorer 6 hade buggarna egennamn. Peekaboo. The Guillotine.
The Three Pixel Jog. The Duplicate Character Bug. Och det visar sig vara det
mest talande av allt i hela den epoken: man namnger inte en bugg man möter
en gång.

Det här är del två. Den handlar om vad det faktiskt innebar att leva inuti
den plattformen — de namngivna buggarna, den osynliga flaggan under de
flesta av dem, hacken som skrevs för att kunna tala till en enda webbläsare,
lösningen som var ett avsiktligt stavfel, och de tre orden HTML som kunde
stänga ett fönster på din egen maskin.

Del ett, om hur Internet Explorer 6 blev en plattform från början:
https://youtu.be/R7Un3IOMvbg

Kapitel
00:00 Del två
00:36 En bugg med ett nummer
00:57 The Three Pixel Jog
01:17 The Double Margin Bug
01:44 Peekaboo
02:10 The Guillotine
02:32 The Duplicate Character Bug
03:00 Rutan som växer
03:27 Man namnger inte en bugg man möter en gång
03:48 hasLayout
04:27 The Holly Hack
04:54 zoom: 1
05:14 Att tala till en enda webbläsare
05:54 Underscore hack
06:15 Villkorliga kommentarer
06:45 Quirks-läget
07:21 Genomskinlighet
07:59 Tabeller och the spacer gif
08:19 Hovring och en fil bredvid sidan
08:47 JavaScript inuti en stilmall
09:04 Tak som ingen annan hade
09:30 Minnesläckan
09:55 Det saknade likhetstecknet
10:34 Ut ur webbläsaren
11:12 En maskin, en version
11:34 Ett bibliotek som lappar webbläsaren
11:48 Vad det kostade
12:31 Begravningen
12:48 Ett år senare
13:12 Varför buggarna hade namn

Varje bild i den här videon är ritad ur kod eller målad; det finns inga
arkivfotografier, så det finns inget att attribuera.

Undertexterna är skrivna för den här videon, inte automatgenererade. Som andra ljudspår finns amerikansk engelska.

There's More To It
```
