# Lokalizované názvy a popisy — Does the Past Still Exist?

Podklad pro **YouTube Studio → video → Podrobnosti → Přidat jazyk**.
Pro každý jazyk jsou tu **dva bloky ke zkopírování**: název a popis.
Kopíruje se **celý blok mezi trojicí zpětných apostrofů**, co je mimo něj,
je poznámka. Anglický originál zůstává v `youtube.md` a nesahá se na něj.

Nahrává je `tools/lokalizace.py`, který čte právě tenhle formát.
Pořadí jazyků je **podle YouTube Studia**, tedy bajtově podle kódu.

## Co se NEPŘEKLÁDÁ

| | |
|---|---|
| **NASA, Solar Dynamics Observatory, Hubble Deep Field, GSFC, JPL, STScI** | vlastní jména a názvy přístrojů v kreditu |
| **časy kapitol** | musí sedět na vteřinu, jinak je YouTube neuzná |
| **tagy** | YouTube je per-jazyk nemá |

Názvy kapitol se naopak **překládají** — divák je čte v seznamu pod videem.
A **názvy jazyků v řádku o titulcích taky**: smíšený seznam endonym
uprostřed odstavce se čte jako nedotažený překlad.

## Kontrola čísel

Anglické *a billion* je 10⁹, tedy **miliarda** — ne *billion* ve smyslu
10¹². Španělsky proto **mil millones** (ne `billón`, to je 10¹²),
portugalsky **bilhão**, německy **Milliarde**, švédsky **miljard**,
polsky **miliard**, francouzsky **milliard**, italsky **miliardo**.
*Eight minutes* a *a thousand light years* jsou beze změny řádu.

---

## suomi (`fi`)

```
Onko menneisyys yhä olemassa?
```

```
Eilen heräsit, söit aamiaista, juttelit jonkun kanssa. Mikään siitä ei enää tapahdu. Mutta se tapahtui. Missä eilinen siis nyt on?

Tämä ei ole video siitä, mitä aika on. Se koskee paljon kapeampaa kysymystä: jos jokin ei enää tapahdu, mitä tarkoittaa sanoa, että se on olemassa?

Kaikki, mitä meillä menneisyydestä on, on jälki. Valokuva ei ole menneisyys — se on nykyhetkessä lojuva esine, joka sattuu kantamaan tietoa siitä. Fossiili ei ole dinosaurus. Tuhka ei ole puu. Ja suurin osa kaikesta tapahtuneesta ei jättänyt jälkeensä yhtään mitään.

Sitten se muuttuu oudommaksi. Et ole kertaakaan nähnyt mitään nykyhetkessä. Näkemäsi Aurinko lähetti tuon valon matkaan kahdeksan minuuttia sitten. Miljardin valovuoden päässä oleva galaksi on miljardi vuotta vanhentunut. Jopa edessäsi oleva näyttö on muutaman nanosekunnin vanha. Maailmankaikkeus on kyllästetty tiedolla omasta menneisyydestään — ja tieto menneisyydestä ei silti ole menneisyys.

Suhteellisuusteoria pahentaa asiaa: ei ole yhtä yleismaailmallista nyt-hetkeä, jonka koko maailmankaikkeus jakaisi. Yksi vastaus siihen on blokkiuniversumi, jossa lapsuutesi on yksinkertaisesti eri kohta aika-avaruutta. Mutta suhteellisuusteoria tekee tuosta ajatuksesta houkuttelevan; se ei todista sitä. Filosofeilla on vaihtoehdoille kolme nimeä — presentismi, eternalismi ja kasvava lohkouniversumi — eikä fysiikka ratkaissut kiistaa. Se teki siitä vaikeamman.

Ja sitten yksi kysymys repii erilleen kaksi ajatusta, jotka yleensä pidämme liimattuina yhteen. Kuvittele, että jokainen tallenne eilisestä on poissa: ei valokuvia, ei asiakirjoja, ei muistikuvaa yhdessäkään päässä, ei fyysistä jälkeä viimeistä atomia myöten. Olisiko eilinen lakannut olemasta? Vai olisiko se silti tapahtunut?

Luvut
00:00 Missä eilinen on?
00:36 Valokuva ei ole menneisyys
01:03 Fossiileja, tuhkaa, muistoja
01:17 Jäljet kertovat vähän
01:58 Aurinko, kahdeksan minuuttia sitten
02:13 Galaksi, miljardi vuotta sitten
02:39 Jopa tämä huone
03:15 Yleismaailmallista nyt-hetkeä ei ole
03:57 Blokkiuniversumi
04:40 Lapsuutesi aika-avaruudessa
04:56 Suhteellisuusteoria ei todista sitä
05:12 Presentismi
05:32 Eternalismi
05:52 Kasvava lohkouniversumi
06:13 Fysiikka teki siitä vaikeampaa
06:35 Mitä oikeastaan väitämme?
07:15 Kysymys, joka erottaa ne
07:35 Jos jokainen jälki olisi poissa
07:50 Keskustelu pronssikaudella
08:07 Olemassaolo ja todisteet
08:23 Onko siis?
08:49 Ne tapahtuivat

KUVALÄHTEET
Kuva Auringosta NASAn Solar Dynamics Observatorysta — NASA/GSFC/SDO
Hubble Deep Field — NASA/JPL/STScI Hubble Deep Field Team
Kuvat NASAn luvalla. NASA ei tue tätä videota.

Tekstitykset on kirjoitettu tätä videota varten, ei luotu automaattisesti. Toisena ääniraitana on amerikanenglanti.
```

## français (`fr`)

```
Le passé existe-t-il encore ?
```

```
Hier, vous vous êtes réveillé, vous avez pris le petit-déjeuner, vous
avez parlé à quelqu'un. Rien de tout cela n'est plus en train de se
passer. Mais cela s'est passé. Alors où est hier, maintenant ?

Ce n'est pas une vidéo sur ce qu'est le temps. Elle porte sur une
question bien plus étroite : si quelque chose n'est plus en train de se
passer, que veut dire qu'il existe ?

Tout ce que nous avons du passé est une trace. Une photo n'est pas le
passé : c'est un objet posé dans le présent qui se trouve porter une
information sur lui. Un fossile n'est pas le dinosaure. La cendre n'est
pas l'arbre. Et la plupart de ce qui est arrivé n'a rien laissé du tout.

Ensuite cela devient plus étrange. Vous n'avez jamais rien vu au présent.
Le Soleil que vous voyez a émis cette lumière il y a huit minutes. Une
galaxie à un milliard d'années-lumière a un milliard d'années de retard.
Même l'écran devant vous est à quelques nanosecondes dans le passé.
L'univers est saturé d'informations sur son propre passé — et une
information sur le passé n'est toujours pas le passé.

La relativité aggrave les choses : il n'y a pas de « maintenant »
universel partagé par tout l'univers. Une réponse à cela est
l'univers-bloc, où votre enfance est simplement une autre partie de
l'espace-temps. Mais la relativité rend cette idée séduisante ; elle ne
la prouve pas. Les philosophes ont trois noms pour les autres réponses :
présentisme, éternalisme et bloc en croissance. La physique n'a pas
tranché le débat. Elle l'a rendu plus difficile.

Et puis il y a une question qui sépare deux idées que nous gardons
d'habitude collées. Imaginez que toute trace d'hier ait disparu : aucune
photo, aucun document, aucun souvenir dans aucune tête, aucune trace
matérielle jusqu'au dernier atome. Hier aurait-il cessé d'exister ? Ou
cela aurait-il eu lieu quand même ?

Chapitres
00:00 Où est hier ?
00:36 La photo n'est pas le passé
01:03 Fossile, cendre, souvenir
01:17 Les traces en disent peu
01:58 Le Soleil d'il y a huit minutes
02:13 Une galaxie d'il y a un milliard d'années
02:39 Même cette pièce
03:15 Il n'y a pas de maintenant universel
03:57 L'univers-bloc
04:40 Votre enfance dans l'espace-temps
04:56 La relativité ne le prouve pas
05:12 Le présentisme
05:32 L'éternalisme
05:52 Le bloc en croissance
06:13 La physique l'a rendu plus difficile
06:35 Qu'affirmons-nous au juste ?
07:15 Une question qui les sépare
07:35 Si toute trace disparaissait
07:50 Une conversation à l'âge du bronze
08:07 Existence et preuve
08:23 Alors, existe-t-il ?
08:49 Cela a eu lieu

CRÉDITS PHOTO
Image du Soleil par le Solar Dynamics Observatory — NASA/GSFC/SDO
Hubble Deep Field — NASA/JPL/STScI Hubble Deep Field Team
Avec l'aimable autorisation de la NASA. La NASA ne cautionne pas cette
vidéo.

Les sous-titres sont écrits pour cette vidéo, pas générés automatiquement. Une piste audio en anglais américain est disponible en seconde piste.
```

---

## Bahasa Indonesia (`id`)

```
Apakah Masa Lalu Masih Ada?
```

```
Kemarin kamu bangun tidur, sarapan, berbicara dengan seseorang. Tidak satu pun dari itu masih berlangsung. Tapi itu pernah terjadi. Jadi kemarin sekarang ada di mana?

Ini bukan video tentang apa itu waktu. Ini tentang pertanyaan yang jauh lebih sempit: kalau sesuatu sudah tidak berlangsung lagi, apa artinya mengatakan bahwa ia ada?

Semua yang kita punya tentang masa lalu hanyalah jejak. Foto bukanlah masa lalu — ia benda yang berada di masa kini dan kebetulan membawa informasi tentangnya. Fosil bukan dinosaurus itu. Abu bukan pohon itu. Dan sebagian besar dari segala yang pernah terjadi sama sekali tidak meninggalkan apa-apa.

Lalu ini jadi makin aneh. Kamu belum pernah sekali pun melihat apa pun di masa kini. Matahari yang kamu lihat mengirimkan cahaya itu delapan menit lalu. Galaksi berjarak semiliar tahun cahaya sudah ketinggalan semiliar tahun. Bahkan layar di depanmu kamu lihat sebagaimana keadaannya beberapa nanodetik lalu. Alam semesta dipenuhi informasi tentang masa lalunya sendiri — dan informasi tentang masa lalu tetap bukan masa lalu.

Relativitas memperburuknya: tidak ada satu pun "sekarang" universal yang dimiliki bersama oleh seluruh alam semesta. Salah satu jawabannya adalah alam semesta blok, tempat masa kecilmu sekadar bagian lain dari ruang-waktu. Tapi relativitas hanya membuat gagasan itu menarik; ia tidak membuktikannya. Para filsuf punya tiga nama untuk pilihan-pilihan itu — presentisme, eternalisme dan blok yang terus tumbuh — dan fisika tidak menyelesaikan perdebatannya. Fisika justru mempersulitnya.

Lalu satu pertanyaan memisahkan dua gagasan yang biasanya kita rekatkan jadi satu. Bayangkan setiap rekaman tentang kemarin lenyap: tidak ada foto, tidak ada dokumen, tidak ada ingatan di kepala siapa pun, tidak ada jejak fisik sampai atom terakhir. Apakah kemarin jadi berhenti ada? Atau apakah ia tetap pernah terjadi?

Bab
00:00 Di mana kemarin berada?
00:36 Foto bukanlah masa lalu
01:03 Fosil, abu, ingatan
01:17 Jejak tak banyak bercerita
01:58 Matahari, delapan menit lalu
02:13 Sebuah galaksi, semiliar tahun lalu
02:39 Bahkan ruangan ini
03:15 Tidak ada "sekarang" yang universal
03:57 Alam semesta blok
04:40 Masa kecilmu di ruang-waktu
04:56 Relativitas tidak membuktikannya
05:12 Presentisme
05:32 Eternalisme
05:52 Blok yang terus tumbuh
06:13 Fisika justru mempersulitnya
06:35 Sebenarnya apa yang kita klaim?
07:15 Pertanyaan yang memisahkan keduanya
07:35 Kalau setiap jejak hilang
07:50 Sebuah percakapan di Zaman Perunggu
08:07 Keberadaan dan bukti
08:23 Jadi, masih ada?
08:49 Itu semua pernah terjadi

KREDIT GAMBAR
Gambar Matahari dari Solar Dynamics Observatory milik NASA — NASA/GSFC/SDO
Hubble Deep Field — NASA/JPL/STScI Hubble Deep Field Team
Atas izin NASA. NASA tidak mendukung video ini.

Subtitel ditulis khusus untuk video ini, bukan dibuat secara otomatis. Tersedia juga trek audio kedua dalam bahasa Inggris Amerika.
```

## italiano (`it`)

```
Il passato esiste ancora?
```

```
Ieri vi siete svegliati, avete fatto colazione, avete parlato con
qualcuno. Niente di tutto questo sta più accadendo. Ma è accaduto.
Allora dov'è adesso ieri?

Questo non è un video su che cosa sia il tempo. Riguarda una domanda
molto più stretta: se qualcosa non sta più accadendo, che cosa significa
dire che esiste?

Tutto quello che abbiamo del passato è una traccia. Una fotografia non è
il passato: è un oggetto che sta nel presente e che per caso porta
informazione su di esso. Un fossile non è il dinosauro. La cenere non è
l'albero. E la maggior parte di ciò che è accaduto non ha lasciato
proprio niente.

Poi diventa più strano. Non avete mai visto niente nel presente. Il Sole
che vedete ha emesso quella luce otto minuti fa. Una galassia a un
miliardo di anni luce è vecchia di un miliardo di anni. Perfino lo
schermo davanti a voi è qualche nanosecondo nel passato. L'universo è
saturo di informazioni sul proprio passato — e l'informazione sul passato
non è ancora il passato.

La relatività peggiora le cose: non esiste un unico « adesso » universale
condiviso da tutto l'universo. Una risposta è l'universo a blocco, dove
la vostra infanzia è semplicemente un'altra parte dello spaziotempo. Ma
la relatività rende quell'idea attraente; non la dimostra. I filosofi
hanno tre nomi per le alternative: presentismo, eternalismo e il blocco
che cresce. La fisica non ha chiuso la disputa. L'ha resa più difficile.

E poi c'è una domanda che separa due idee che di solito teniamo
incollate. Immaginate che ogni traccia di ieri sia sparita: nessuna
fotografia, nessun documento, nessun ricordo in nessuna testa, nessuna
traccia materiale fino all'ultimo atomo. Ieri avrebbe smesso di esistere?
Oppure sarebbe accaduto lo stesso?

Capitoli
00:00 Dov'è ieri?
00:36 La fotografia non è il passato
01:03 Fossile, cenere, ricordo
01:17 Le tracce dicono poco
01:58 Il Sole di otto minuti fa
02:13 Una galassia di un miliardo di anni fa
02:39 Perfino questa stanza
03:15 Non c'è un adesso universale
03:57 L'universo a blocco
04:40 La vostra infanzia nello spaziotempo
04:56 La relatività non lo dimostra
05:12 Presentismo
05:32 Eternalismo
05:52 Il blocco che cresce
06:13 La fisica l'ha resa più difficile
06:35 Che cosa stiamo affermando?
07:15 Una domanda che le separa
07:35 Se ogni traccia sparisse
07:50 Una conversazione nell'età del bronzo
08:07 Esistenza e prova
08:23 Allora, esiste?
08:49 È accaduto

CREDITI FOTOGRAFICI
Immagine del Sole dal Solar Dynamics Observatory — NASA/GSFC/SDO
Hubble Deep Field — NASA/JPL/STScI Hubble Deep Field Team
Per gentile concessione della NASA. La NASA non sostiene questo video.

I sottotitoli sono scritti per questo video, non generati automaticamente. Come seconda traccia audio è disponibile l’inglese americano.
```

---

## Deutsch (`de`)

```
Gibt es die Vergangenheit noch?
```

```
Gestern sind Sie aufgewacht, haben gefrühstückt, mit jemandem gesprochen.
Nichts davon passiert noch. Aber es ist passiert. Wo ist das Gestern also
jetzt?

Das hier ist kein Video darüber, was Zeit ist. Es geht um eine viel
engere Frage: Wenn etwas nicht mehr passiert, was heißt es dann, dass es
existiert?

Alles, was wir von der Vergangenheit haben, ist eine Spur. Ein Foto ist
nicht die Vergangenheit — es ist ein Ding in der Gegenwart, das zufällig
Information über sie trägt. Ein Fossil ist nicht der Dinosaurier. Asche
ist nicht der Baum. Und das meiste, was je passiert ist, hat überhaupt
nichts hinterlassen.

Dann wird es noch seltsamer. Sie haben noch nie irgendetwas in der
Gegenwart gesehen. Die Sonne, die Sie sehen, hat ihr Licht vor acht
Minuten losgeschickt. Eine Galaxie eine Milliarde Lichtjahre weit weg ist
eine Milliarde Jahre alt. Selbst der Bildschirm vor Ihnen ist ein paar
Nanosekunden in der Vergangenheit. Das Universum ist voller Information
über seine eigene Vergangenheit — und Information über die Vergangenheit
ist immer noch nicht die Vergangenheit.

Die Relativitätstheorie macht es schlimmer: Es gibt kein einziges
universelles „Jetzt", das im ganzen Universum gilt. Eine Antwort darauf
ist das Blockuniversum, in dem Ihre Kindheit einfach ein anderer Teil der
Raumzeit ist. Aber die Relativitätstheorie macht diese Idee reizvoll —
sie beweist sie nicht. Philosophen haben drei Namen für die Alternativen:
Präsentismus, Eternalismus und den wachsenden Block. Die Physik hat den
Streit nicht entschieden. Sie hat ihn schwerer gemacht.

Und dann gibt es eine Frage, die zwei Dinge auseinanderreißt, die wir
sonst zusammengeklebt halten. Stellen Sie sich vor, jede Aufzeichnung von
gestern ist fort: keine Fotos, keine Dokumente, keine Erinnerung in
keinem Kopf, keine physische Spur bis zum letzten Atom. Hätte das Gestern
dann aufgehört zu existieren? Oder wäre es trotzdem passiert?

Kapitel
00:00 Wo ist das Gestern?
00:36 Ein Foto ist nicht die Vergangenheit
01:03 Fossil, Asche, Erinnerung
01:17 Spuren sagen wenig
01:58 Die Sonne vor acht Minuten
02:13 Eine Galaxie vor einer Milliarde Jahren
02:39 Sogar dieser Raum
03:15 Es gibt kein universelles Jetzt
03:57 Das Blockuniversum
04:40 Ihre Kindheit in der Raumzeit
04:56 Die Relativitätstheorie beweist es nicht
05:12 Präsentismus
05:32 Eternalismus
05:52 Der wachsende Block
06:13 Die Physik hat es schwerer gemacht
06:35 Was behaupten wir eigentlich?
07:15 Eine Frage, die beides trennt
07:35 Wenn jede Spur fort wäre
07:50 Ein Gespräch in der Bronzezeit
08:07 Existenz und Beleg
08:23 Also, gibt es sie?
08:49 Es ist passiert

BILDNACHWEIS
Aufnahme der Sonne vom Solar Dynamics Observatory — NASA/GSFC/SDO
Hubble Deep Field — NASA/JPL/STScI Hubble Deep Field Team
Mit freundlicher Genehmigung der NASA. Die NASA unterstützt dieses Video
nicht.

Die Untertitel wurden für dieses Video geschrieben, nicht automatisch erzeugt. Als zweite Tonspur steht amerikanisches Englisch bereit.
```

---

## polski (`pl`)

```
Czy przeszłość nadal istnieje?
```

```
Wczoraj obudziliście się, zjedliście śniadanie, z kimś rozmawialiście.
Nic z tego już się nie dzieje. Ale się wydarzyło. Więc gdzie jest teraz
wczoraj?

To nie jest film o tym, czym jest czas. Jest o pytaniu dużo węższym:
jeśli coś już się nie dzieje, co właściwie znaczy powiedzieć, że to
istnieje?

Wszystko, co mamy z przeszłości, to ślad. Zdjęcie nie jest przeszłością —
to przedmiot leżący w teraźniejszości, który akurat niesie o niej
informację. Skamielina nie jest dinozaurem. Popiół nie jest drzewem.
A większość tego, co się kiedykolwiek wydarzyło, nie zostawiła zupełnie
nic.

Potem robi się jeszcze dziwniej. Nigdy nie widzieliście niczego
w teraźniejszości. Słońce, które widzicie, wysłało to światło osiem minut
temu. Galaktyka odległa o miliard lat świetlnych jest o miliard lat
spóźniona. Nawet ekran przed wami jest kilka nanosekund w przeszłości.
Wszechświat jest przesycony informacjami o własnej przeszłości —
a informacja o przeszłości wciąż nie jest przeszłością.

Teoria względności pogarsza sprawę: nie ma jednego uniwersalnego „teraz",
wspólnego całemu wszechświatowi. Jedną z odpowiedzi jest wszechświat
blokowy, w którym wasze dzieciństwo jest po prostu inną częścią
czasoprzestrzeni. Ale teoria względności czyni tę myśl kuszącą — nie
dowodzi jej. Filozofowie mają dla alternatyw trzy nazwy: prezentyzm,
eternalizm i rosnący blok. Fizyka nie rozstrzygnęła sporu. Uczyniła go
trudniejszym.

A potem jest pytanie, które rozrywa dwie rzeczy, które zwykle trzymamy
sklejone. Wyobraźcie sobie, że każdy zapis wczorajszego dnia zniknął:
żadnych zdjęć, żadnych dokumentów, żadnego wspomnienia w żadnej głowie,
żadnego materialnego śladu aż do ostatniego atomu. Czy wczoraj
przestałoby istnieć? Czy też wydarzyłoby się tak czy owak?

Rozdziały
00:00 Gdzie jest wczoraj?
00:36 Zdjęcie nie jest przeszłością
01:03 Skamielina, popiół, wspomnienie
01:17 Ślady mówią niewiele
01:58 Słońce sprzed ośmiu minut
02:13 Galaktyka sprzed miliarda lat
02:39 Nawet ten pokój
03:15 Nie ma uniwersalnego teraz
03:57 Wszechświat blokowy
04:40 Wasze dzieciństwo w czasoprzestrzeni
04:56 Teoria względności tego nie dowodzi
05:12 Prezentyzm
05:32 Eternalizm
05:52 Rosnący blok
06:13 Fizyka uczyniła to trudniejszym
06:35 Co właściwie twierdzimy?
07:15 Pytanie, które je rozdziela
07:35 Gdyby zniknął każdy ślad
07:50 Rozmowa w epoce brązu
08:07 Istnienie i dowód
08:23 Więc istnieje?
08:49 Wydarzyło się

ŹRÓDŁA ZDJĘĆ
Zdjęcie Słońca z Solar Dynamics Observatory — NASA/GSFC/SDO
Hubble Deep Field — NASA/JPL/STScI Hubble Deep Field Team
Dzięki uprzejmości NASA. NASA nie promuje tego filmu.

Napisy są pisane do tego filmu, nie generowane automatycznie. Jako druga ścieżka dźwiękowa dostępny jest angielski amerykański.
```

---

## português (Brasil) (`pt-BR`)

```
O passado ainda existe?
```

```
Ontem você acordou, tomou café da manhã, conversou com alguém. Nada disso
está mais acontecendo. Mas aconteceu. Então onde está o ontem agora?

Este não é um vídeo sobre o que é o tempo. É sobre uma pergunta bem mais
estreita: se algo não está mais acontecendo, o que significa dizer que
existe?

Tudo o que temos do passado é um rastro. Uma fotografia não é o passado:
é um objeto que está no presente e que por acaso carrega informação sobre
ele. Um fóssil não é o dinossauro. A cinza não é a árvore. E a maior
parte do que já aconteceu não deixou absolutamente nada.

Depois fica mais estranho. Você nunca viu nada no presente. O Sol que
você vê emitiu aquela luz há oito minutos. Uma galáxia a um bilhão de
anos-luz está um bilhão de anos atrasada. Até a tela na sua frente está
a alguns nanossegundos no passado. O universo está saturado de informação
sobre o próprio passado — e informação sobre o passado ainda não é o
passado.

A relatividade piora isso: não existe um único „agora" universal
compartilhado por todo o universo. Uma resposta é o universo bloco, em
que a sua infância é simplesmente outra parte do espaço-tempo. Mas a
relatividade torna essa ideia atraente; não a prova. Os filósofos têm três
nomes para as alternativas: presentismo, eternalismo e o bloco crescente.
A física não encerrou a discussão. Deixou-a mais difícil.

E então há uma pergunta que separa duas ideias que normalmente mantemos
coladas. Imagine que todo registro de ontem sumiu: nenhuma fotografia,
nenhum documento, nenhuma lembrança em cabeça nenhuma, nenhum rastro
físico até o último átomo. O ontem teria deixado de existir? Ou teria
acontecido do mesmo jeito?

Capítulos
00:00 Onde está o ontem?
00:36 A fotografia não é o passado
01:03 Fóssil, cinza, lembrança
01:17 Os rastros dizem pouco
01:58 O Sol de oito minutos atrás
02:13 Uma galáxia de um bilhão de anos atrás
02:39 Até esta sala
03:15 Não há um agora universal
03:57 O universo bloco
04:40 Sua infância no espaço-tempo
04:56 A relatividade não prova isso
05:12 Presentismo
05:32 Eternalismo
05:52 O bloco crescente
06:13 A física deixou mais difícil
06:35 O que estamos afirmando?
07:15 Uma pergunta que os separa
07:35 Se todo rastro sumisse
07:50 Uma conversa na Idade do Bronze
08:07 Existência e prova
08:23 Então, existe?
08:49 Aconteceu

CRÉDITOS DAS IMAGENS
Imagem do Sol do Solar Dynamics Observatory — NASA/GSFC/SDO
Hubble Deep Field — NASA/JPL/STScI Hubble Deep Field Team
Cortesia da NASA. A NASA não endossa este vídeo.

As legendas foram escritas para este vídeo, não geradas automaticamente. Como segunda faixa de áudio está disponível o inglês americano.
```

---

## Türkçe (`tr`)

```
Geçmiş Hâlâ Var mı?
```

```
Dün uyandın, kahvaltı ettin, biriyle konuştun. Bunların hiçbiri artık olmuyor. Ama oldu. Peki dün şimdi nerede?

Bu, zamanın ne olduğuna dair bir video değil. Çok daha dar bir soruyla ilgili: bir şey artık olmuyorsa, onun var olduğunu söylemek ne anlama gelir?

Geçmişe dair elimizdeki her şey bir izdir. Fotoğraf geçmiş değildir — şimdide duran ve tesadüfen geçmişe dair bilgi taşıyan bir nesnedir. Fosil, dinozorun kendisi değildir. Kül, ağaç değildir. Ve şimdiye dek yaşananların çoğu geriye hiçbir şey bırakmadı.

Sonra iş daha da tuhaflaşıyor. Şimdiye ait hiçbir şeyi bir kez bile görmedin. Gördüğün Güneş o ışığı sekiz dakika önce yolladı. Bir milyar ışık yılı uzaktaki bir galaksi bir milyar yıl geride. Önündeki ekran bile birkaç nanosaniye eski. Evren kendi geçmişine dair bilgiyle doymuş durumda — ve geçmişe dair bilgi yine de geçmiş değil.

Görelilik işi daha da kötüleştiriyor: bütün evrenin paylaştığı tek bir evrensel "şimdi" yok. Buna bir cevap, çocukluğunun yalnızca uzay-zamanın başka bir parçası olduğu blok evren. Ama görelilik bu fikri yalnızca cazip kılıyor; kanıtlamıyor. Filozofların seçenekler için üç adı var — şimdicilik, eternalizm ve büyüyen blok — ve fizik tartışmayı bitirmedi. Tartışmayı zorlaştırdı.

Ve sonra tek bir soru, normalde birbirine yapıştırdığımız iki fikri ayırıyor. Düne dair her kaydın yok olduğunu düşün: fotoğraf yok, belge yok, hiçbir kafada anı yok, son atomuna kadar fiziksel iz yok. Dün var olmaktan çıkmış mı olurdu? Yoksa yine de yaşanmış mı olurdu?

Bölümler
00:00 Dün nerede?
00:36 Fotoğraf geçmiş değildir
01:03 Fosiller, kül, hafıza
01:17 İzler pek az şey anlatır
01:58 Güneş, sekiz dakika önce
02:13 Bir galaksi, bir milyar yıl önce
02:39 Bu oda bile
03:15 Evrensel bir "şimdi" yok
03:57 Blok evren
04:40 Uzay-zamanda çocukluğun
04:56 Görelilik bunu kanıtlamıyor
05:12 Şimdicilik
05:32 Eternalizm
05:52 Büyüyen blok
06:13 Fizik işi zorlaştırdı
06:35 Aslında ne iddia ediyoruz?
07:15 İkisini birbirinden ayıran soru
07:35 Her iz yok olsaydı
07:50 Tunç Çağı’nda bir konuşma
08:07 Varlık ve kanıt
08:23 Peki, var mı?
08:49 Onlar yaşandı

GÖRSEL KAYNAKLARI
NASA’nın Solar Dynamics Observatory’sinden Güneş görüntüsü — NASA/GSFC/SDO
Hubble Deep Field — NASA/JPL/STScI Hubble Deep Field Team
NASA’nın izniyle. NASA bu videoyu desteklemiyor.

Altyazılar bu video için yazıldı, otomatik olarak oluşturulmadı. İkinci ses parçası olarak Amerikan İngilizcesi de mevcut.
```

## українська (`uk`)

```
Чи існує минуле досі?
```

```
Учора ти прокинувся, поснідав, з кимось поговорив. Нічого з цього вже не відбувається. Але воно сталося. То де тепер учора?

Це відео не про те, чим є час. Воно про значно вужче запитання: якщо щось уже не відбувається, що означає сказати, що воно існує?

Усе, що ми маємо від минулого, — це слід. Фотографія не є минулим: це предмет, який лежить у теперішньому й випадково несе інформацію про минуле. Скам’янілість не є динозавром. Попіл не є деревом. А більшість того, що будь-коли сталося, не лишила по собі геть нічого.

Далі стає дивніше. Ти жодного разу не бачив нічого в теперішньому. Сонце, яке ти бачиш, відправило це світло вісім хвилин тому. Галактику за мільярд світлових років ми бачимо такою, якою вона була мільярд років тому. Навіть екран перед тобою ти бачиш таким, яким він був кілька наносекунд тому. Всесвіт насичений інформацією про власне минуле — а інформація про минуле все одно не є минулим.

Відносність усе погіршує: не існує єдиного універсального «зараз», спільного для всього Всесвіту. Одна відповідь на це — блоковий всесвіт, у якому твоє дитинство є просто іншою частиною простору-часу. Але відносність робить цю ідею привабливою; вона її не доводить. Філософи мають для варіантів три назви — презентизм, етерналізм і зростаючий блок — і фізика суперечки не розв’язала. Вона зробила її складнішою.

А потім одне запитання розтягує в різні боки дві ідеї, які ми зазвичай тримаємо склеєними. Уяви, що зник кожен запис про вчора: жодних фотографій, жодних документів, жодного спогаду в жодній голові, жодного фізичного сліду аж до останнього атома. Чи перестало б учора існувати? Чи воно все одно сталося б?

Розділи
00:00 Де тепер учора?
00:36 Фотографія — це не минуле
01:03 Скам’янілості, попіл, пам’ять
01:17 Сліди мало розповідають
01:58 Сонце, вісім хвилин тому
02:13 Галактика, мільярд років тому
02:39 Навіть ця кімната
03:15 Універсального «зараз» не існує
03:57 Блоковий всесвіт
04:40 Твоє дитинство у просторі-часі
04:56 Відносність цього не доводить
05:12 Презентизм
05:32 Етерналізм
05:52 Зростаючий блок
06:13 Фізика все ускладнила
06:35 Що саме ми стверджуємо?
07:15 Запитання, яке їх розділяє
07:35 Якби зник кожен слід
07:50 Розмова в бронзовому віці
08:07 Існування і свідчення
08:23 То існує?
08:49 Вони сталися

ДЖЕРЕЛА ЗОБРАЖЕНЬ
Зображення Сонця з обсерваторії NASA Solar Dynamics Observatory — NASA/GSFC/SDO
Hubble Deep Field — NASA/JPL/STScI Hubble Deep Field Team
З люб’язної згоди NASA. NASA не підтримує це відео.

Субтитри написані для цього відео, а не згенеровані автоматично. Також доступна друга звукова доріжка — американською англійською.
```

## Tiếng Việt (`vi`)

```
Quá khứ có còn tồn tại không?
```

```
Hôm qua bạn thức dậy, ăn sáng, nói chuyện với ai đó. Chẳng điều nào trong số đó còn đang diễn ra. Nhưng nó đã diễn ra. Vậy hôm qua giờ đang ở đâu?

Đây không phải video về thời gian là gì. Video này bàn về một câu hỏi hẹp hơn nhiều: nếu một điều gì đó không còn đang diễn ra, thì nói rằng nó tồn tại nghĩa là sao?

Tất cả những gì ta có về quá khứ đều là dấu vết. Bức ảnh không phải là quá khứ — nó là một vật nằm trong hiện tại và tình cờ mang thông tin về quá khứ. Hóa thạch không phải con khủng long. Tro không phải cái cây. Và phần lớn những gì từng xảy ra chẳng để lại gì cả.

Rồi nó còn lạ hơn nữa. Bạn chưa một lần nào nhìn thấy bất cứ thứ gì ở hiện tại. Mặt Trời bạn đang thấy đã phát ra ánh sáng ấy từ tám phút trước. Một thiên hà cách đây một tỉ năm ánh sáng thì đã cũ mất một tỉ năm. Ngay cả màn hình trước mặt bạn cũng cũ vài nano giây. Vũ trụ bão hòa thông tin về chính quá khứ của nó — mà thông tin về quá khứ thì vẫn không phải là quá khứ.

Thuyết tương đối còn làm mọi thứ tệ hơn: không có một cái "bây giờ" phổ quát duy nhất mà cả vũ trụ cùng chia sẻ. Một câu trả lời cho điều đó là vũ trụ khối, nơi tuổi thơ của bạn chỉ đơn giản là một phần khác của không-thời gian. Nhưng thuyết tương đối chỉ khiến ý tưởng ấy hấp dẫn; nó không chứng minh được. Các triết gia có ba cái tên cho những lựa chọn này — thuyết hiện tại, thuyết vĩnh cửu và khối đang lớn dần — và vật lý đã không dàn xếp được cuộc tranh luận. Nó khiến cuộc tranh luận khó hơn.

Rồi một câu hỏi tách rời hai ý niệm mà ta vẫn thường dán chặt vào nhau. Hãy hình dung mọi ghi chép về hôm qua đều biến mất: không ảnh, không tài liệu, không ký ức trong bất kỳ cái đầu nào, không một dấu vết vật chất nào cho đến nguyên tử cuối cùng. Hôm qua có thôi tồn tại không? Hay những gì xảy ra hôm qua vẫn là điều đã xảy ra?

Các chương
00:00 Hôm qua đang ở đâu?
00:36 Bức ảnh không phải là quá khứ
01:03 Hóa thạch, tro tàn, ký ức
01:17 Dấu vết nói lên rất ít
01:58 Mặt Trời, tám phút trước
02:13 Một thiên hà, một tỉ năm trước
02:39 Ngay cả căn phòng này
03:15 Không có "bây giờ" chung cho cả vũ trụ
03:57 Vũ trụ khối
04:40 Tuổi thơ bạn trong không-thời gian
04:56 Thuyết tương đối không chứng minh điều đó
05:12 Thuyết hiện tại
05:32 Thuyết vĩnh cửu
05:52 Khối đang lớn dần
06:13 Vật lý làm mọi thứ khó hơn
06:35 Rốt cuộc ta đang khẳng định điều gì?
07:15 Câu hỏi phân biệt hai ý niệm
07:35 Nếu mọi dấu vết đều biến mất
07:50 Một cuộc trò chuyện thời đồ đồng
08:07 Sự tồn tại và bằng chứng
08:23 Vậy, quá khứ còn tồn tại không?
08:49 Chúng đã từng xảy ra

NGUỒN HÌNH ẢNH
Ảnh Mặt Trời từ Solar Dynamics Observatory của NASA — NASA/GSFC/SDO
Hubble Deep Field — NASA/JPL/STScI Hubble Deep Field Team
Được NASA cho phép sử dụng. NASA không bảo trợ video này.

Phụ đề được viết riêng cho video này, không phải tạo tự động. Có thể chọn tiếng Anh Mỹ ở bản âm thanh thứ hai.
```

## čeština (`cs`)

```
Existuje minulost ještě pořád?
```

```
Včera jste vstali, nasnídali se, s někým mluvili. Nic z toho se už
neděje. Ale stalo se to. Tak kde je teď včerejšek?

Tohle není video o tom, co je čas. Je o mnohem užší otázce: když se něco
už neděje, co vlastně znamená říct, že to existuje?

Všechno, co z minulosti máme, je stopa. Fotografie není minulost — je to
předmět ležící v přítomnosti, který o ní náhodou nese informaci. Fosilie
není dinosaurus. Popel není strom. A většina toho, co se kdy stalo,
nezanechala vůbec nic.

Pak je to ještě zvláštnější. Nikdy jste neviděli vůbec nic v přítomnosti.
Slunce, které vidíte, vyslalo to světlo před osmi minutami. Galaxie
miliardu světelných let daleko je miliardu let stará. I obrazovka před
vámi je pár nanosekund v minulosti. Vesmír je prosycený informacemi
o vlastní minulosti — a informace o minulosti pořád není ta minulost.

Relativita to zhoršuje: neexistuje jedno univerzální „teď", společné
celému vesmíru. Jedna odpověď na to je blokový vesmír, ve kterém je vaše
dětství prostě jiná část časoprostoru. Jenže relativita tu myšlenku dělá
lákavou — nedokazuje ji. Filozofové mají pro alternativy tři jména:
presentismus, eternalismus a rostoucí blok. Fyzika ten spor nerozhodla.
Udělala ho těžším.

A pak je tu otázka, která od sebe odtrhne dvě věci, jež normálně držíme
slepené. Představte si, že každý záznam o včerejšku je pryč: žádné
fotografie, žádné dokumenty, žádná vzpomínka v žádné hlavě, žádná hmotná
stopa až do posledního atomu. Přestal by tím včerejšek existovat? Nebo by
se stejně byl stal?

Kapitoly
00:00 Kde je včerejšek?
00:36 Fotografie není minulost
01:03 Fosilie, popel, vzpomínka
01:17 Stopy toho moc neřeknou
01:58 Slunce před osmi minutami
02:13 Galaxie před miliardou let
02:39 I tahle místnost
03:15 Univerzální teď neexistuje
03:57 Blokový vesmír
04:40 Vaše dětství v časoprostoru
04:56 Relativita to nedokazuje
05:12 Presentismus
05:32 Eternalismus
05:52 Rostoucí blok
06:13 Fyzika to udělala těžším
06:35 Co vlastně tvrdíme?
07:15 Otázka, která je odtrhne
07:35 Kdyby zmizely všechny stopy
07:50 Rozhovor v době bronzové
08:07 Existence a doklad
08:23 Tak existuje?
08:49 Stalo se to

OBRAZOVÉ ZDROJE
Snímek Slunce ze Solar Dynamics Observatory — NASA/GSFC/SDO
Hubble Deep Field — NASA/JPL/STScI Hubble Deep Field Team
S laskavým svolením NASA. NASA toto video nepodporuje.

Titulky jsou psané pro tohle video, ne strojový přepis. Jako druhá zvuková stopa je k dispozici americká angličtina.
```

---

## español (`es`)

```
¿Sigue existiendo el pasado?
```

```
Ayer se despertó, desayunó, habló con alguien. Nada de eso está pasando
ya. Pero pasó. Entonces, ¿dónde está el ayer ahora?

Este no es un vídeo sobre qué es el tiempo. Va de una pregunta mucho más
estrecha: si algo ya no está pasando, ¿qué significa decir que existe?

Todo lo que tenemos del pasado es un rastro. Una fotografía no es el
pasado: es un objeto que está en el presente y que da la casualidad de
que lleva información sobre él. Un fósil no es el dinosaurio. La ceniza
no es el árbol. Y la mayor parte de lo que ha pasado no dejó nada en
absoluto.

Y se vuelve más raro. Usted nunca ha visto nada en el presente. El Sol
que ve lanzó esa luz hace ocho minutos. Una galaxia a mil millones de
años luz tiene mil millones de años de retraso. Incluso la pantalla que
tiene delante está unos nanosegundos en el pasado. El universo está
saturado de información sobre su propio pasado, y la información sobre el
pasado sigue sin ser el pasado.

La relatividad lo empeora: no hay un único „ahora" universal compartido
por todo el universo. Una respuesta a eso es el universo bloque, donde su
infancia es sencillamente otra parte del espacio-tiempo. Pero la
relatividad hace esa idea atractiva; no la demuestra. Los filósofos
tienen tres nombres para las alternativas: presentismo, eternalismo y el
bloque creciente. La física no zanjó la discusión. La hizo más difícil.

Y luego hay una pregunta que separa dos ideas que normalmente mantenemos
pegadas. Imagine que todo registro de ayer ha desaparecido: ninguna
fotografía, ningún documento, ningún recuerdo en ninguna cabeza, ningún
rastro físico hasta el último átomo. ¿Habría dejado el ayer de existir?
¿O habría pasado igualmente?

Capítulos
00:00 ¿Dónde está el ayer?
00:36 La fotografía no es el pasado
01:03 Fósil, ceniza, recuerdo
01:17 Los rastros dicen poco
01:58 El Sol de hace ocho minutos
02:13 Una galaxia de hace mil millones de años
02:39 Incluso esta habitación
03:15 No hay un ahora universal
03:57 El universo bloque
04:40 Su infancia en el espacio-tiempo
04:56 La relatividad no lo demuestra
05:12 Presentismo
05:32 Eternalismo
05:52 El bloque creciente
06:13 La física lo hizo más difícil
06:35 ¿Qué estamos afirmando?
07:15 Una pregunta que los separa
07:35 Si no quedara ningún rastro
07:50 Una conversación en la Edad del Bronce
08:07 Existencia y prueba
08:23 Entonces, ¿existe?
08:49 Pasó

CRÉDITOS DE IMAGEN
Imagen del Sol del Solar Dynamics Observatory — NASA/GSFC/SDO
Hubble Deep Field — NASA/JPL/STScI Hubble Deep Field Team
Cortesía de la NASA. La NASA no respalda este vídeo.

Los subtítulos están escritos para este vídeo, no generados automáticamente. Como segunda pista de audio está disponible el inglés americano.
```

---

## svenska (`sv`)

```
Finns det förflutna fortfarande?
```

```
I går vaknade du, åt frukost, pratade med någon. Inget av det händer
längre. Men det hände. Så var är gårdagen nu?

Det här är ingen film om vad tid är. Den handlar om en mycket snävare
fråga: om något inte längre händer, vad betyder det då att det finns?

Allt vi har av det förflutna är spår. Ett fotografi är inte det
förflutna — det är ett föremål som ligger i nuet och som råkar bära
information om det. Ett fossil är inte dinosaurien. Aska är inte trädet.
Och det mesta som någonsin hänt lämnade ingenting alls.

Sedan blir det märkligare. Du har aldrig sett något i nuet. Solen du ser
sände ut det ljuset för åtta minuter sedan. En galax en miljard ljusår
bort är en miljard år gammal. Till och med skärmen framför dig är några
nanosekunder i det förflutna. Universum är mättat med information om sitt
eget förflutna — och information om det förflutna är ändå inte det
förflutna.

Relativitetsteorin gör det värre: det finns inget enda universellt
„nu" som hela universum delar. Ett svar på det är blockuniversum, där din
barndom helt enkelt är en annan del av rumtiden. Men relativitetsteorin
gör den tanken lockande; den bevisar den inte. Filosofer har tre namn på
alternativen: presentism, eternalism och det växande blocket. Fysiken
avgjorde inte tvisten. Den gjorde tvisten svårare.

Och så finns det en fråga som drar isär två saker som vi annars håller
ihoplimmade. Tänk dig att varje spår av gårdagen är borta: inga foton,
inga dokument, inget minne i något huvud, inget fysiskt spår ner till
sista atomen. Skulle gårdagen då ha slutat finnas? Eller skulle den ha
hänt ändå?

Kapitel
00:00 Var är gårdagen?
00:36 Fotografiet är inte det förflutna
01:03 Fossil, aska, minne
01:17 Spår säger lite
01:58 Solen för åtta minuter sedan
02:13 En galax för en miljard år sedan
02:39 Till och med det här rummet
03:15 Det finns inget universellt nu
03:57 Blockuniversum
04:40 Din barndom i rumtiden
04:56 Relativitetsteorin bevisar det inte
05:12 Presentism
05:32 Eternalism
05:52 Det växande blocket
06:13 Fysiken gjorde det svårare
06:35 Vad påstår vi egentligen?
07:15 En fråga som skiljer dem åt
07:35 Om varje spår var borta
07:50 Ett samtal under bronsåldern
08:07 Existens och belägg
08:23 Så, finns det?
08:49 Det hände

BILDKÄLLOR
Bild av solen från Solar Dynamics Observatory — NASA/GSFC/SDO
Hubble Deep Field — NASA/JPL/STScI Hubble Deep Field Team
Med tillstånd av NASA. NASA stöder inte den här filmen.

Undertexterna är skrivna för den här videon, inte automatgenererade. Som andra ljudspår finns amerikansk engelska.
```
