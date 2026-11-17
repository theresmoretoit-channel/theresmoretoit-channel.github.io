# Lokalizované názvy a popisy — AI Didn't Start With ChatGPT

Podklad pro **YouTube Studio → video → Podrobnosti → Přidat jazyk**.
Pro každý jazyk jsou tu **dva bloky ke zkopírování**: název a popis.
Kopíruje se **celý blok mezi trojicí zpětných apostrofů**, co je mimo něj,
je poznámka. Anglický originál zůstává v `youtube.md` a nesahá se na něj.

Nahrává je `tools/lokalizace.py`, který čte právě tenhle formát.

## Co se NEPŘEKLÁDÁ

| | |
|---|---|
| **vlastní jména** | ELIZA, Joseph Weizenbaum, Alan Turing, MIT, Dartmouth, Deep Blue, Garry Kasparov, AlexNet, ChatGPT, OpenAI, GPT, BERT, Claude, Gemini |
| **„Can machines think?"** | citace z Turingova článku; u ní zůstává anglický originál |
| **transformer** | název architektury; francouzsky ani polsky se nepřekládá |
| **Erik Pitti, CC BY 2.0** | atribuce musí zůstat dohledatelná |
| **AI Magazine 27(4), 2006** | bibliografický údaj |
| **časy kapitol** | musí sedět na vteřinu, jinak je YouTube neuzná |
| **tagy** | YouTube je per-jazyk nemá |

Názvy kapitol se naopak překládají — divák je čte v přehrávači.

## Kontrola čísel

Ve videu není žádné *trillion* ani *billion*, tedy ani past s řády
(anglická *trillion* je německy `Billionen`). Letopočty a „fifty-six
years" se přepisují beze změny hodnoty.

## suomi (`fi`)

```
Kuinka vanha tekoäly oikeastaan on?
```

```
Marraskuun lopussa 2022 ilmestyi verkkosivu, jolla oli pieni kenttä. Kirjoitit kysymyksen, ja tietokone vastasi. Miljoonille ihmisille se oli hetki, jolloin tekoäly syntyi.

Paitsi että tietokone oli tehnyt jotain tällaista jo viisikymmentäkuusi vuotta aiemmin.

Vuonna 1966 MIT:n tutkija julkaisi ohjelman nimeltä ELIZA. Se ei ollut älykäs, se ei ollut neuroverkko eikä se ymmärtänyt yhtään mitään — se etsi avainsanoja ja palautti loput kysymyksen muodossa. Ihmiset juttelivat sille silti. Weizenbaumin oma sihteeri oli katsonut, kun tämä rakensi sen, tiesi täsmälleen mistä oli kyse, ja pyysi muutaman vuorosanan jälkeen häntä poistumaan huoneesta.

Jäljelle jää kysymys, johon seuraava puoli vuosisataa törmäsi yhä uudelleen: kuinka vähän koneelta oikeastaan vaaditaan, jotta se vaikuttaisi älykkäältä?

Matkan varrella: artikkeli, jonka Alan Turing avasi sanoilla ”Can machines think?”, ja se kikka, jolla hän korvasi koko kysymyksen; vuoden 1943 neuronimalli, jonka painot asetettiin käsin; talvet, joina rahoitus loppui; koiran valokuva, jota tietokoneet eivät osanneet tunnistaa viiteenkymmeneen vuoteen; ja syy siihen, miksi tekstikenttä verkkosivulla merkitsi enemmän kuin mikään sen takana ollut tekniikka.

Luvut
00:00 Kenttä verkkosivulla
00:39 ELIZA
01:43 Voivatko koneet ajatella?
02:28 Ilmaus, jota kukaan ei ollut kirjoittanut
02:56 Neuroni paperilla
03:35 Mikään siitä ei toiminut
04:35 Sitten kolme asiaa muuttui
05:11 Deep Blue
05:49 Se koira
06:32 Transformer
07:02 GPT
07:42 30. marraskuuta 2022
08:17 Tekoäly ei alkanut ChatGPT:stä
08:47 Milloin se siis alkoi?
09:23 Paluu MIT:n sihteerin luo

KUVALÄHTEET
Say hello to Deep Blue — Erik Pitti, CC BY 2.0
via Wikimedia Commons
Lisenssit: creativecommons.org/licenses/by/2.0

A Proposal for the Dartmouth Summer Research Project on Artificial Intelligence (1955) — John McCarthy ym., public domain, jäljennetty AI Magazinen 27(4), 2006, faksimilestä.

Kaikki muut arkistokuvat ovat public domainia.

Tekstitykset on kirjoitettu tätä videota varten, ei luotu automaattisesti. Toisena ääniraitana on amerikanenglanti.
```

## français (`fr`)

```
Quel âge a vraiment l'IA ?
```

```
Fin novembre 2022, une page web est apparue avec un petit champ de saisie.
On y tapait une question, et un ordinateur répondait. Pour des millions de
gens, c'est le moment où l'intelligence artificielle a commencé.

Sauf qu'un ordinateur avait déjà fait ça cinquante-six ans plus tôt.

En 1966, un chercheur du MIT a publié un programme appelé ELIZA. Il n'était
pas intelligent, ce n'était pas un réseau de neurones et il ne comprenait
absolument rien : il cherchait des mots-clés et renvoyait le reste sous
forme de question. Les gens lui parlaient quand même. La secrétaire de Weizenbaum
elle-même l'avait vu écrire ce programme, savait exactement ce que
c'était, et après quelques échanges lui a demandé de sortir.

Reste une question qui est revenue sans cesse au cours du demi-siècle suivant : quel est le strict minimum dont une machine a
besoin pour paraître intelligente ?

En chemin : l'article qu'Alan Turing a ouvert par « Can machines think ? »
et l'astuce par laquelle il a remplacé cette question ; le modèle de
neurone de 1943 dont les poids étaient réglés à la main ; les hivers où les
financements se sont arrêtés ; la photo d'un chien que les ordinateurs
n'ont pas su reconnaître pendant cinquante ans ; et la raison pour laquelle
un champ de texte sur une page web a compté plus que toute la technologie
qui la faisait fonctionner.

Chapitres
00:00 Un champ de saisie sur une page web
00:39 ELIZA
01:43 Les machines peuvent-elles penser ?
02:28 Une expression que personne n'avait écrite
02:56 Un neurone sur le papier
03:35 Rien de tout ça n'a marché
04:35 Puis trois choses ont changé
05:11 Deep Blue
05:49 Le chien
06:32 Le Transformer
07:02 GPT
07:42 30 novembre 2022
08:17 L'IA n'a pas commencé avec ChatGPT
08:47 Alors quand a-t-elle commencé ?
09:23 Retour à une secrétaire du MIT

CRÉDITS PHOTO
Say hello to Deep Blue — Erik Pitti, CC BY 2.0
via Wikimedia Commons
Licences : creativecommons.org/licenses/by/2.0

A Proposal for the Dartmouth Summer Research Project on Artificial
Intelligence (1955) — John McCarthy et al., domaine public, reproduit
d'après le fac-similé paru dans AI Magazine 27(4), 2006.

Toutes les autres images d'archive sont dans le domaine public.

Les sous-titres sont écrits pour cette vidéo, pas générés automatiquement. Une piste audio en anglais américain est disponible en seconde piste.
```

## Bahasa Indonesia (`id`)

```
Sebenarnya Berapa Umur AI?
```

```
Pada akhir November 2022 muncul sebuah halaman web dengan kotak kecil di atasnya. Kamu mengetik pertanyaan, dan komputer menjawab. Bagi jutaan orang, itulah saat kecerdasan buatan dimulai.

Hanya saja sebuah komputer sudah melakukan hal semacam itu lima puluh enam tahun sebelumnya.

Pada 1966 seorang peneliti di MIT menerbitkan program bernama ELIZA. Program itu tidak cerdas, bukan jaringan saraf, dan sama sekali tidak mengerti apa pun — ia mencocokkan kata kunci lalu mengembalikan sisanya sebagai pertanyaan. Orang-orang tetap mengajaknya bicara. Sekretaris Weizenbaum sendiri sudah menyaksikan ia membuatnya, tahu persis apa itu, dan setelah beberapa kali bertukar kalimat memintanya keluar dari ruangan.

Maka tersisa satu pertanyaan yang terus ditemui setengah abad berikutnya: sebenarnya, apa saja kebutuhan minimal sebuah mesin agar tampak cerdas?

Video ini juga membahas: makalah yang dibuka Alan Turing dengan "Can machines think?" dan siasat yang ia pakai untuk mengganti pertanyaan itu; model neuron tahun 1943 yang bobotnya diatur secara manual; musim-musim dingin ketika pendanaan berhenti; foto seekor anjing yang tidak bisa dikenali komputer selama lima puluh tahun; dan alasan kenapa sebuah kotak teks di halaman web lebih berarti daripada seluruh teknologi di belakangnya.

Bab
00:00 Sebuah kotak di halaman web
00:39 ELIZA
01:43 Bisakah mesin berpikir?
02:28 Istilah yang belum pernah ditulis siapa pun
02:56 Neuron di atas kertas
03:35 Tidak ada satu pun yang berhasil
04:35 Lalu tiga hal berubah
05:11 Deep Blue
05:49 Anjing itu
06:32 Transformer
07:02 GPT
07:42 30 November 2022
08:17 AI tidak dimulai dari ChatGPT
08:47 Jadi kapan dimulainya?
09:23 Kembali ke sekretaris di MIT

KREDIT GAMBAR
Say hello to Deep Blue — Erik Pitti, CC BY 2.0
via Wikimedia Commons
Lisensi: creativecommons.org/licenses/by/2.0

A Proposal for the Dartmouth Summer Research Project on Artificial Intelligence (1955) — John McCarthy dkk., domain publik, direproduksi dari faksimile di AI Magazine 27(4), 2006.

Semua gambar arsip lainnya berada dalam domain publik.

Subtitel ditulis khusus untuk video ini, bukan dibuat secara otomatis. Tersedia juga trek audio kedua dalam bahasa Inggris Amerika.
```

## italiano (`it`)

```
Quanti anni ha davvero l'IA?
```

```
Alla fine di novembre 2022 è comparsa una pagina web con un piccolo campo di
testo. Ci scrivevi una domanda e un computer rispondeva. Per milioni di
persone quello è stato il momento in cui l'intelligenza artificiale è nata.

Solo che un computer aveva già fatto qualcosa di simile cinquantasei anni
prima.

Nel 1966 un ricercatore del MIT pubblicò un programma chiamato ELIZA. Non
era intelligente, non era una rete neurale e non capiva assolutamente
nulla: cercava parole chiave e restituiva il resto sotto forma di domanda.
La gente ci parlava lo stesso. La segretaria di Weizenbaum lo aveva visto
scrivere quel programma, sapeva benissimo che cosa fosse, e dopo poche
battute gli chiese di uscire dalla stanza.

Resta una domanda che si è ripresentata più volte nel mezzo secolo successivo: quanto poco serve davvero a una macchina per sembrare
intelligente?

Nel video: l'articolo che Alan Turing aprì con «Can machines think?»
e l'astuzia con cui sostituì quella domanda; il modello di neurone del 1943
i cui pesi si fissavano a mano; gli inverni in cui i finanziamenti si
fermarono; la foto di un cane che i computer non seppero riconoscere per
cinquant'anni; e il motivo per cui un campo di testo su una pagina web
contò più di tutta la tecnologia che c'era dietro.

Capitoli
00:00 Un campo di testo su una pagina web
00:39 ELIZA
01:43 Le macchine possono pensare?
02:28 Un'espressione che nessuno aveva scritto
02:56 Un neurone sulla carta
03:35 Niente di tutto ciò funzionò
04:35 Poi cambiarono tre cose
05:11 Deep Blue
05:49 Il cane
06:32 Il transformer
07:02 GPT
07:42 30 novembre 2022
08:17 L'IA non è cominciata con ChatGPT
08:47 Allora quando è cominciata?
09:23 Di nuovo quella segretaria del MIT

CREDITI FOTOGRAFICI
Say hello to Deep Blue — Erik Pitti, CC BY 2.0
via Wikimedia Commons
Licenze: creativecommons.org/licenses/by/2.0

A Proposal for the Dartmouth Summer Research Project on Artificial
Intelligence (1955) — John McCarthy e altri, pubblico dominio, riprodotto
dal facsimile in AI Magazine 27(4), 2006.

Tutte le altre immagini d'archivio sono di pubblico dominio.

I sottotitoli sono scritti per questo video, non generati automaticamente. Come seconda traccia audio è disponibile l’inglese americano.
```

## Deutsch (`de`)

```
Wie alt ist KI eigentlich?
```

```
Ende November 2022 erschien eine Webseite mit einem kleinen Feld darauf.
Man tippte eine Frage ein, und ein Computer antwortete. Für Millionen
Menschen war das der Moment, in dem künstliche Intelligenz begann.

Nur hatte ein Computer so etwas schon sechsundfünfzig Jahre früher
geschafft.

1966 veröffentlichte ein Forscher am MIT ein Programm namens ELIZA. Es war
nicht intelligent, es war kein neuronales Netz und es verstand überhaupt
nichts — es suchte Schlüsselwörter und gab den Rest als Frage zurück. Die
Leute redeten trotzdem mit ihm. Weizenbaums eigene Sekretärin hatte ihm
beim Programmieren zugesehen, wusste genau, was das war, und bat ihn nach
ein paar Sätzen, den Raum zu verlassen.

Damit bleibt eine Frage, die im folgenden halben Jahrhundert immer wieder
auftauchte: Wie wenig braucht eine Maschine eigentlich, um intelligent zu
wirken?

Außerdem im Video: der Aufsatz, den Alan Turing mit „Can machines think?" eröffnete,
und der Kniff, mit dem er diese Frage ersetzte; das Neuronenmodell von 1943,
dessen Gewichte von Hand gesetzt wurden; die Winter, in denen die Förderung
ausblieb; das Foto eines Hundes, das Computer fünfzig Jahre lang nicht
erkennen konnten; und der Grund, warum ein Textfeld auf einer Webseite mehr
bedeutete als die ganze Technik dahinter.

Kapitel
00:00 Ein Feld auf einer Webseite
00:39 ELIZA
01:43 Können Maschinen denken?
02:28 Ein Ausdruck, den niemand geschrieben hatte
02:56 Ein Neuron auf dem Papier
03:35 Nichts davon funktionierte
04:35 Dann änderten sich drei Dinge
05:11 Deep Blue
05:49 Der Hund
06:32 Der Transformer
07:02 GPT
07:42 30. November 2022
08:17 KI hat nicht mit ChatGPT angefangen
08:47 Wann hat sie also angefangen?
09:23 Zurück zu einer Sekretärin am MIT

BILDNACHWEISE
Say hello to Deep Blue — Erik Pitti, CC BY 2.0
via Wikimedia Commons
Lizenzen: creativecommons.org/licenses/by/2.0

A Proposal for the Dartmouth Summer Research Project on Artificial
Intelligence (1955) — John McCarthy u. a., gemeinfrei, reproduziert nach
dem Faksimile in AI Magazine 27(4), 2006.

Alle übrigen Archivbilder sind gemeinfrei.

Die Untertitel wurden für dieses Video geschrieben, nicht automatisch erzeugt. Als zweite Tonspur steht amerikanisches Englisch bereit.
```

## polski (`pl`)

```
Ile lat ma tak naprawdę SI?
```

```
Pod koniec listopada 2022 pojawiła się strona internetowa z małym polem.
Wpisywało się pytanie, a komputer odpowiadał. Dla milionów ludzi to był
moment, w którym zaczęła się sztuczna inteligencja.

Tyle że komputer zrobił coś takiego już pięćdziesiąt sześć lat wcześniej.

W 1966 badacz z MIT opublikował program o nazwie ELIZA. Nie był
inteligentny, nie był siecią neuronową i nie rozumiał zupełnie nic —
szukał w zdaniu słów kluczowych i oddawał resztę w postaci pytania. Ludzie
i tak z nim rozmawiali. Sama sekretarka Weizenbauma widziała, jak pisze
ten program, wiedziała dokładnie, co to jest, i po krótkiej wymianie zdań
poprosiła go, żeby wyszedł.

Pozostaje więc pytanie, które powracało przez następne pół wieku:
jak niewiele naprawdę potrzeba maszynie, żeby sprawiać wrażenie
inteligentnej?

Po drodze: artykuł, który Alan Turing rozpoczął pytaniem „Can machines
think?", i sztuczka, którą je zastąpił; model neuronu z 1943 roku, którego
wagi ustawiano ręcznie; zimy, kiedy wstrzymano finansowanie; zdjęcie psa,
którego komputery nie potrafiły rozpoznać przez pięćdziesiąt lat; i powód,
dla którego pole tekstowe na stronie internetowej znaczyło więcej niż cała
technologia, dzięki której działało.

Rozdziały
00:00 Pole na stronie internetowej
00:39 ELIZA
01:43 Czy maszyny mogą myśleć?
02:28 Wyrażenie, którego nikt nie zapisał
02:56 Neuron na papierze
03:35 Nic z tego nie działało
04:35 Potem zmieniły się trzy rzeczy
05:11 Deep Blue
05:49 Ten pies
06:32 Transformer
07:02 GPT
07:42 30 listopada 2022
08:17 SI nie zaczęła się od ChatGPT
08:47 Więc kiedy się zaczęła?
09:23 Z powrotem do sekretarki z MIT

ŹRÓDŁA ZDJĘĆ
Say hello to Deep Blue — Erik Pitti, CC BY 2.0
via Wikimedia Commons
Licencje: creativecommons.org/licenses/by/2.0

A Proposal for the Dartmouth Summer Research Project on Artificial
Intelligence (1955) — John McCarthy i inni, domena publiczna,
reprodukowane z faksymile w AI Magazine 27(4), 2006.

Pozostałe zdjęcia archiwalne są w domenie publicznej.

Napisy są pisane do tego filmu, nie generowane automatycznie. Jako druga ścieżka dźwiękowa dostępny jest angielski amerykański.
```

## português (Brasil) (`pt-BR`)

```
Afinal, quantos anos tem a IA?
```

```
No fim de novembro de 2022 apareceu uma página na internet com uma
caixinha. Você digitava uma pergunta e um computador respondia. Para
milhões de pessoas, esse foi o momento em que a inteligência artificial
começou.

Só que um computador já tinha feito algo assim cinquenta e seis anos antes.

Em 1966, um pesquisador do MIT publicou um programa chamado ELIZA. Não era
inteligente, não era uma rede neural e não entendia absolutamente nada:
procurava palavras-chave e devolvia o resto como uma pergunta. As pessoas
conversavam com ela mesmo assim. A própria secretária de Weizenbaum tinha
acompanhado a criação do programa, sabia exatamente o que era aquilo e, depois
de uma breve troca de mensagens, pediu que ele saísse da sala.

Fica uma pergunta que voltou a surgir repetidamente ao longo do meio século
seguinte: qual é o mínimo de que uma máquina realmente precisa para parecer
inteligente?

No caminho: o artigo que Alan Turing abriu com "Can machines think?" e o
truque com que substituiu essa pergunta; o modelo de neurônio de 1943 cujos
pesos eram ajustados à mão; os invernos em que os financiamentos foram
cortados; a foto de um cachorro que os computadores não souberam reconhecer
por cinquenta anos; e a razão pela qual uma caixa de texto numa página da
internet importou mais do que toda a tecnologia por trás dela.

Capítulos
00:00 Uma caixa numa página da internet
00:39 ELIZA
01:43 Máquinas podem pensar?
02:28 Uma expressão que ninguém tinha escrito
02:56 Um neurônio no papel
03:35 Nada disso funcionou
04:35 Então três coisas mudaram
05:11 Deep Blue
05:49 O cachorro
06:32 O transformer
07:02 GPT
07:42 30 de novembro de 2022
08:17 A IA não começou com o ChatGPT
08:47 Então quando começou?
09:23 De volta a uma secretária do MIT

CRÉDITOS DAS IMAGENS
Say hello to Deep Blue — Erik Pitti, CC BY 2.0
via Wikimedia Commons
Licenças: creativecommons.org/licenses/by/2.0

A Proposal for the Dartmouth Summer Research Project on Artificial
Intelligence (1955) — John McCarthy e outros, domínio público, reproduzido
do fac-símile em AI Magazine 27(4), 2006.

As demais imagens de arquivo são de domínio público.

As legendas foram escritas para este vídeo, não geradas automaticamente. Como segunda faixa de áudio está disponível o inglês americano.
```

## Türkçe (`tr`)

```
Yapay Zekâ Gerçekte Kaç Yaşında?
```

```
2022 Kasım’ının sonunda, üzerinde küçük bir kutu olan bir web sayfası belirdi. Bir soru yazıyordun ve bir bilgisayar cevap veriyordu. Milyonlarca insan için yapay zekânın başladığı an buydu.

Ama bir bilgisayar buna benzer bir şeyi elli altı yıl önce çoktan yapmıştı.

1966’da MIT’te bir araştırmacı ELIZA adlı bir program yayımladı. Zeki değildi, sinir ağı değildi ve hiçbir şey anlamıyordu — anahtar kelimeleri eşleştirip geri kalanını soru olarak geri veriyordu. İnsanlar yine de onunla konuştu. Weizenbaum’un kendi sekreteri, programı nasıl yazdığını görmüştü, ne olduğunu tam olarak biliyordu ve birkaç cümlenin ardından ondan odadan çıkmasını istedi.

Geriye, sonraki yarım yüzyılın defalarca çarptığı bir soru kalıyor: bir makinenin zeki görünmesi için aslında ne kadar az şey yeterli?

Bu bölümde ayrıca: Alan Turing’in "Can machines think?" diye açtığı makale ve o soruyu değiştirmek için kullandığı numara; ağırlıkları elle ayarlanan 1943 tarihli nöron modeli; fonun kesildiği kışlar; bilgisayarların elli yıl boyunca tanıyamadığı bir köpek fotoğrafı; ve bir web sayfasındaki metin kutusunun, arkasındaki bütün teknolojiden neden daha önemli olduğu.

Bölümler
00:00 Bir web sayfasındaki kutu
00:39 ELIZA
01:43 Makineler düşünebilir mi?
02:28 Kimsenin yazmadığı bir ifade
02:56 Kâğıt üstünde bir nöron
03:35 Hiçbiri işe yaramadı
04:35 Sonra üç şey değişti
05:11 Deep Blue
05:49 O köpek
06:32 Transformer
07:02 GPT
07:42 30 Kasım 2022
08:17 Yapay zekâ ChatGPT ile başlamadı
08:47 Peki ne zaman başladı?
09:23 MIT'teki sekretere dönelim

GÖRSEL KAYNAKLARI
Say hello to Deep Blue — Erik Pitti, CC BY 2.0
via Wikimedia Commons
Lisanslar: creativecommons.org/licenses/by/2.0

A Proposal for the Dartmouth Summer Research Project on Artificial Intelligence (1955) — John McCarthy ve diğerleri, kamu malı, AI Magazine 27(4), 2006 sayısındaki tıpkıbasımdan çoğaltıldı.

Diğer tüm arşiv görselleri kamu malıdır.

Altyazılar bu video için yazıldı, otomatik olarak oluşturulmadı. İkinci ses parçası olarak Amerikan İngilizcesi de mevcut.
```

## українська (`uk`)

```
Скільки насправді років штучному інтелекту?
```

```
Наприкінці листопада 2022 року з’явилася вебсторінка з невеликим полем. Ти вписував запитання — і комп’ютер відповідав. Для мільйонів людей це був момент, коли виник штучний інтелект.

От тільки комп’ютер зробив щось подібне на п’ятдесят шість років раніше.

1966 року дослідник з MIT опублікував програму під назвою ELIZA. Вона не була розумною, не була нейромережею і не розуміла геть нічого — вона шукала ключові слова й повертала решту у вигляді запитання. Люди однаково з нею розмовляли. Сама секретарка Вайценбаума бачила, як він її створював, чудово знала, що це таке, і після кількох реплік попросила його вийти з кімнати.

Лишається запитання, на яке наступні півстоліття наштовхувалися знову й знову: як мало насправді потрібно машині, щоб здаватися розумною?

Також у відео: стаття, яку Алан Тюрінг почав словами «Can machines think?», і той трюк, яким він замінив саме це запитання; модель нейрона 1943 року, ваги якої встановлювали вручну; зими, коли припинялося фінансування; фотографія пса, якого комп’ютери п’ятдесят років не могли впізнати; і причина, чому текстове поле на вебсторінці важило більше, ніж уся техніка за ним.

Розділи
00:00 Поле на вебсторінці
00:39 ELIZA
01:43 Чи можуть машини мислити?
02:28 Вислів, якого ніхто не записав
02:56 Нейрон на папері
03:35 Ніщо з цього не працювало
04:35 Тоді змінилися три речі
05:11 Deep Blue
05:49 Той пес
06:32 Трансформер
07:02 GPT
07:42 30 листопада 2022
08:17 Штучний інтелект почався не з ChatGPT
08:47 То коли ж він почався?
09:23 Повернення до секретарки з MIT

ДЖЕРЕЛА ЗОБРАЖЕНЬ
Say hello to Deep Blue — Erik Pitti, CC BY 2.0
via Wikimedia Commons
Ліцензії: creativecommons.org/licenses/by/2.0

A Proposal for the Dartmouth Summer Research Project on Artificial Intelligence (1955) — John McCarthy та ін., суспільне надбання, відтворено з факсиміле в AI Magazine 27(4), 2006.

Усі інші архівні зображення — суспільне надбання.

Субтитри написані для цього відео, а не згенеровані автоматично. Також доступна друга звукова доріжка — американською англійською.
```

## Tiếng Việt (`vi`)

```
Trí tuệ nhân tạo thực sự bao nhiêu tuổi?
```

```
Cuối tháng 11 năm 2022, một trang web xuất hiện với một ô nhỏ trên đó. Bạn gõ một câu hỏi, và máy tính trả lời. Với hàng triệu người, đó là thời điểm trí tuệ nhân tạo ra đời.

Chỉ có điều một chiếc máy tính đã làm điều tương tự từ năm mươi sáu năm trước.

Năm 1966, một nhà nghiên cứu ở MIT công bố chương trình tên ELIZA. Nó không thông minh, không phải mạng nơ-ron, và chẳng hiểu gì cả — nó dò từ khóa rồi trả phần còn lại về dưới dạng câu hỏi. Người ta vẫn cứ trò chuyện với nó. Chính người thư ký của Weizenbaum đã chứng kiến ông viết chương trình, hiểu rõ nó là gì, vậy mà sau vài lượt trao đổi vẫn đề nghị ông ra khỏi phòng.

Thế là còn lại một câu hỏi mà nửa thế kỷ tiếp theo cứ va vào mãi: thật ra một cỗ máy cần ít đến mức nào để trông có vẻ thông minh?

Video cũng đề cập đến: bài báo Alan Turing mở đầu bằng "Can machines think?" và mẹo ông dùng để thay thế chính câu hỏi đó; mô hình nơ-ron năm 1943 với các trọng số được thiết lập thủ công; những mùa đông khi nguồn tài trợ dừng lại; bức ảnh một con chó mà máy tính không nhận ra nổi suốt năm mươi năm; và lý do một ô văn bản trên trang web lại quan trọng hơn toàn bộ công nghệ đằng sau nó.

Các chương
00:00 Một ô trên trang web
00:39 ELIZA
01:43 Máy móc có thể nghĩ được không?
02:28 Cụm từ chưa ai từng viết ra
02:56 Một nơ-ron trên giấy
03:35 Tất cả đều không hiệu quả
04:35 Rồi ba điều thay đổi
05:11 Deep Blue
05:49 Con chó
06:32 Transformer
07:02 GPT
07:42 Ngày 30 tháng 11 năm 2022
08:17 AI không bắt đầu từ ChatGPT
08:47 Vậy nó bắt đầu khi nào?
09:23 Trở lại với người thư ký ở MIT

NGUỒN HÌNH ẢNH
Say hello to Deep Blue — Erik Pitti, CC BY 2.0
via Wikimedia Commons
Giấy phép: creativecommons.org/licenses/by/2.0

A Proposal for the Dartmouth Summer Research Project on Artificial Intelligence (1955) — John McCarthy và cộng sự, phạm vi công cộng, in lại từ bản fax-simile trong AI Magazine 27(4), 2006.

Mọi hình tư liệu khác đều thuộc phạm vi công cộng.

Phụ đề được viết riêng cho video này, không phải tạo tự động. Có thể chọn tiếng Anh Mỹ ở bản âm thanh thứ hai.
```

## čeština (`cs`)

```
Jak stará je vlastně umělá inteligence?
```

```
Na konci listopadu 2022 se objevila webová stránka s malým polem. Napsali
jste do něj otázku a počítač odpověděl. Pro miliony lidí to byl okamžik,
kdy umělá inteligence začala.

Jenže něco takového počítač dokázal už o šestapadesát let dřív.

V roce 1966 zveřejnil vědec z MIT program ELIZA. Nebyl inteligentní, nebyl
to neuronová síť a nerozuměl vůbec ničemu — hledal ve větě klíčová slova
a zbytek vracel jako otázku. Lidé si s ním stejně povídali. Weizenbaumova
sekretářka ho viděla ten program psát, věděla přesně, co to je, a po několika vyměněných zprávách požádala, ať odejde.

Zůstává tedy otázka, která se během následujícího půlstoletí opakovaně vracela:
jak málo toho stroj vlastně potřebuje, aby působil inteligentně?

Cestou: článek, který Alan Turing zahájil otázkou „Can machines think?",
a trik, kterým ji nahradil; model neuronu z roku 1943, jehož váhy se
nastavovaly ručně; zimy, kdy se zastavilo financování; fotka psa, kterou
počítače nedokázaly rozpoznat padesát let; a důvod, proč textové pole na
webové stránce znamenalo víc než veškerá technologie, díky níž fungovalo.

Kapitoly
00:00 Pole na webové stránce
00:39 ELIZA
01:43 Mohou stroje myslet?
02:28 Spojení, které nikdo nenapsal
02:56 Neuron na papíře
03:35 Nefungovalo z toho nic
04:35 Pak se změnily tři věci
05:11 Deep Blue
05:49 Ten pes
06:32 Transformer
07:02 GPT
07:42 30. listopadu 2022
08:17 Umělá inteligence nezačala až s ChatGPT
08:47 Tak kdy tedy začala?
09:23 Zpátky k sekretářce na MIT

OBRAZOVÉ ZDROJE
Say hello to Deep Blue — Erik Pitti, CC BY 2.0
via Wikimedia Commons
Licence: creativecommons.org/licenses/by/2.0

A Proposal for the Dartmouth Summer Research Project on Artificial
Intelligence (1955) — John McCarthy a kol., volné dílo, reprodukováno
z faksimile v AI Magazine 27(4), 2006.

Ostatní archivní snímky jsou volným dílem.

Titulky jsou psané pro tohle video, ne strojový přepis. Jako druhá zvuková stopa je k dispozici americká angličtina.
```

## español (`es`)

```
¿Cuántos años tiene realmente la IA?
```

```
A finales de noviembre de 2022 apareció una página web con un pequeño campo de
texto. Escribías una pregunta y un ordenador respondía. Para millones de
personas, ese fue el momento en que empezó la inteligencia artificial.

Solo que un ordenador ya había hecho algo así cincuenta y seis años antes.

En 1966, un investigador del MIT publicó un programa llamado ELIZA. No era
inteligente, no era una red neuronal y no entendía absolutamente nada:
buscaba palabras clave y devolvía el resto como una pregunta. La gente
hablaba con ella igualmente. La propia secretaria de Weizenbaum le había
visto escribir el programa, sabía exactamente qué era y, tras unas pocas
frases, le pidió que saliera de la sala.

Queda así una pregunta que se planteó una y otra vez durante el medio siglo
siguiente: ¿qué tan poco necesita realmente una máquina para parecer
inteligente?

Por el camino: el artículo que Alan Turing abrió con "Can machines think?"
y el truco con el que sustituyó esa pregunta; el modelo de neurona de 1943
cuyos pesos se fijaban a mano; los inviernos en que se cortaron las
subvenciones; la fotografía de un perro que los ordenadores no supieron
reconocer durante cincuenta años; y la razón por la que una casilla de
texto en una página web importó más que toda la tecnología que había
detrás.

Capítulos
00:00 Un campo de texto en una página web
00:39 ELIZA
01:43 ¿Pueden pensar las máquinas?
02:28 Una expresión que nadie había escrito
02:56 Una neurona sobre el papel
03:35 Nada de eso funcionó
04:35 Entonces cambiaron tres cosas
05:11 Deep Blue
05:49 El perro
06:32 El transformer
07:02 GPT
07:42 30 de noviembre de 2022
08:17 La IA no empezó con ChatGPT
08:47 Entonces, ¿cuándo empezó?
09:23 De vuelta a una secretaria del MIT

CRÉDITOS DE IMÁGENES
Say hello to Deep Blue — Erik Pitti, CC BY 2.0
vía Wikimedia Commons
Licencias: creativecommons.org/licenses/by/2.0

A Proposal for the Dartmouth Summer Research Project on Artificial
Intelligence (1955) — John McCarthy y otros, dominio público, reproducido
del facsímil en AI Magazine 27(4), 2006.

Las demás imágenes de archivo son de dominio público.

Los subtítulos están escritos para este vídeo, no generados automáticamente. Como segunda pista de audio está disponible el inglés americano.
```

## svenska (`sv`)

```
Hur gammal är AI egentligen?
```

```
I slutet av november 2022 dök det upp en webbsida med en liten ruta på. Man
skrev in en fråga, och en dator svarade. För miljoner människor var det
ögonblicket då artificiell intelligens började.

Fast en dator hade gjort något liknande femtiosex år tidigare.

1966 publicerade en forskare på MIT ett program som hette ELIZA. Det var
inte intelligent, det var inget neuralt nätverk och det förstod ingenting
alls — det letade efter nyckelord och lämnade tillbaka resten som en fråga. Folk
pratade med det ändå. Weizenbaums egen sekreterare hade sett honom skriva
programmet, visste precis vad det var, och bad honom efter några repliker
att lämna rummet.

Kvar står en fråga som återkom gång på gång under det följande halvseklet: hur lite behöver en maskin egentligen för att verka intelligent?

På vägen: artikeln som Alan Turing inledde med "Can machines think?" och
knepet han använde för att ersätta den frågan; neuronmodellen från 1943 vars vikter
sattes för hand; vintrarna när anslagen drogs in; fotot av en hund som
datorer inte kunde känna igen under femtio års tid; och skälet till att en textruta
på en webbsida betydde mer än all teknik bakom den.

Kapitel
00:00 En ruta på en webbsida
00:39 ELIZA
01:43 Kan maskiner tänka?
02:28 Ett uttryck ingen hade skrivit ned
02:56 En neuron på papper
03:35 Ingenting av det fungerade
04:35 Sedan ändrades tre saker
05:11 Deep Blue
05:49 Hunden
06:32 Transformern
07:02 GPT
07:42 30 november 2022
08:17 AI började inte med ChatGPT
08:47 Så när började den?
09:23 Tillbaka till en sekreterare på MIT

BILDKÄLLOR
Say hello to Deep Blue — Erik Pitti, CC BY 2.0
via Wikimedia Commons
Licenser: creativecommons.org/licenses/by/2.0

A Proposal for the Dartmouth Summer Research Project on Artificial
Intelligence (1955) — John McCarthy m.fl., public domain, återgiven efter
faksimilen i AI Magazine 27(4), 2006.

Alla övriga arkivbilder är public domain.

Undertexterna är skrivna för den här videon, inte automatgenererade. Som andra ljudspår finns amerikansk engelska.
```
