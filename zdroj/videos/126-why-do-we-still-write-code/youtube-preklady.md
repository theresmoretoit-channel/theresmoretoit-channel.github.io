# YouTube — 126 „Why Do We Still Write Code?“: lokalizace

Lokalizované názvy a popisy pro třináct jazyků (bez `en`, ten je
v `youtube.md`). Pořadí podle YouTube Studia. Nahrává
`python tools/lokalizace.py videos/126-why-do-we-still-write-code`
— **až po Codexu**.

**Co se NEPŘEKLÁDÁ:**

- vlastní jména a názvy (FORTRAN, CASE, Model Driven Architecture,
  low-code, DynamoDB, Edsger Dijkstra — v ukrajinštině v textu
  Дейкстра jako v titulcích),
- řádek zdrojů: autoři, roky, názvy článků, sborníků a časopisů zůstávají
  anglicky; přeložené je jen úvodní slovo „Sources:“,
- jména a licence v bloku atribucí (přeložený je nadpis, „via“ a „Licences“),
- časy kapitol, ty jsou na vteřinu shodné s angličtinou,
- tagy — YouTube je pro jednotlivé jazyky nemá.

**„Six words“ zůstává ŠEST**, protože se počítá anglická věta na obrazovce
(S01–S02). Kde má přeložená věta jiný počet slov (fi, id, pl, tr, uk, vi, cs),
stojí v popisu „anglicky šest slov“, aby čtenář nepočítal překlad; v de, fr,
es, it, pt-BR a sv má překlad sám šest slov, takže zůstává holé „Six words“.

Citace v textu (*automatic coding system*, *the foolishness of natural
language programming*) jsou přeložené stejně jako v `script.<kód>.md`
(S10, S25). Pointa videa (S29–S35, závěr S57–S65) se v popisu neprozrazuje,
stejně jako v angličtině. Odstavec o titulcích a americké stopě je doslova
z kanonické tabulky v `docs/zverejneni.md`. Registr jako v titulcích téhož
jazyka (cs ty, de du, fr tu, es tú, pt-BR você, it tu, pl ty, uk ти, tr sen,
id kamu, vi bạn, fi sinä, sv du); popis diváka přímo neoslovuje, takže se
to projeví jen v kapitolách.

## suomi (`fi`)

```
Miksi kirjoitamme yhä koodia?
```

```
Tässä on täydellinen vaatimus yrityksen ohjelmistolle: ”Käyttäjä voi perua tilauksen.” Englanniksi kuusi sanaa. Jokainen kehittäjä nyökkäisi. Silti se jättää auki lähes jokaisen todellisen kysymyksen. Entä kun lasku on jo lähtenyt? Entä kun tilaus on jo lähetetty? Entä toimittaja? Entä jos kaksi ihmistä toimii samalla sekunnilla?

Nyt on tarjolla houkutteleva ajatus: kirjoita vain määrittelyt, pidä ne dokumenteissa, tarkasta ne ja anna tekoälyn kirjoittaa koodi. Se on hyvä ajatus. Uusi se ei kuitenkaan ole. Tämä video seuraa lähes seitsemänkymmentä vuotta kestäneitä yrityksiä nostaa sitä tasoa, jolla kerromme tietokoneille, mitä niiden pitää tehdä, ja kysyy, mikä tällä kertaa on oikeasti toisin.

Matkan varrella: vuoden 1957 artikkeli, joka kutsui FORTRANia ”automaattiseksi koodausjärjestelmäksi”, CASE-työkalut ja neljännen sukupolven kielet, Model Driven Architecture, low-code, kysely 450 ihmiselle, jotka todella käyttivät mallipohjaista kehitystä, Edsger Dijkstran lyhyt kirjoitus ”luonnollisella kielellä ohjelmoinnin typeryydestä” sekä Amazonin DynamoDB:n bugi, jonka laukaiseminen vaati 35 askelta.

Lähteet: Backus et al. (1957), The FORTRAN Automatic Coding System, Proceedings of the Western Joint Computer Conference; Object Management Group, Model Driven Architecture (2001); Richardson & Rymer (2014), Forrester Research; Whittle, Hutchinson & Rouncefield (2014), The State of Practice in Model-Driven Engineering, IEEE Software; Dijkstra, EWD 667 (1978); Newcombe et al. (2014), Use of Formal Methods at Amazon Web Services; CommitStrip (2016), A very comprehensive and precise spec.

Tekstitykset on kirjoitettu tätä videota varten, ei luotu automaattisesti. Toisena ääniraitana on amerikanenglanti.

KUVALÄHTEET
Edsger Wybe Dijkstra — Hamilton Richards, CC BY-SA 3.0
Wikimedia Commonsin kautta
Lisenssi: creativecommons.org/licenses/by-sa/3.0/

LUVUT
00:00 Kuusi sanaa
00:42 Kirjoita vain lauseet
01:08 Vanha ajatus
01:45 Malleja koodin sijaan
02:32 Toimiko mikään näistä?
03:07 Ohjelmoijien vitsi
03:35 Dijkstran varoitus
04:04 Mikä on nyt toisin
05:07 Määrittely lähdekoodina
06:01 Miltä muutos näyttää
07:26 Mistä tiedät, että se toimi?
08:39 Katso, mitä olemme rakentaneet
09:21 Tulevaisuuden ohjelmoija
```

## français (`fr`)

```
Pourquoi écrit-on encore du code ?
```

```
Voici une exigence complète pour un logiciel de gestion : « Un utilisateur peut annuler une commande. » Six mots. N’importe quel développeur approuverait. Et pourtant, elle laisse ouvertes presque toutes les vraies questions. Une fois la facture envoyée ? Une fois la commande expédiée ? Et le fournisseur ? Et si deux personnes agissent dans la même seconde ?

Aujourd’hui, une idée séduisante circule : n’écrire que les spécifications, les ranger dans des documents, les relire, et laisser une IA écrire le code. C’est une bonne idée. Mais ce n’est pas une idée nouvelle. Cette vidéo suit près de soixante-dix ans de tentatives pour élever le niveau auquel on dit aux ordinateurs quoi faire, et se demande ce qui est vraiment différent cette fois.

En chemin : l’article de 1957 qui présentait FORTRAN comme un « système de codage automatique », les outils CASE et les langages de quatrième génération, Model Driven Architecture, le low-code, une enquête auprès de 450 personnes qui utilisaient réellement le développement dirigé par les modèles, la courte note d’Edsger Dijkstra « sur la sottise de la programmation en langage naturel », et un bug dans DynamoDB d’Amazon dont le déclenchement nécessitait 35 étapes.

Sources : Backus et al. (1957), The FORTRAN Automatic Coding System, Proceedings of the Western Joint Computer Conference ; Object Management Group, Model Driven Architecture (2001) ; Richardson & Rymer (2014), Forrester Research ; Whittle, Hutchinson & Rouncefield (2014), The State of Practice in Model-Driven Engineering, IEEE Software ; Dijkstra, EWD 667 (1978) ; Newcombe et al. (2014), Use of Formal Methods at Amazon Web Services ; CommitStrip (2016), A very comprehensive and precise spec.

Les sous-titres sont écrits pour cette vidéo, pas générés automatiquement. Une piste audio en anglais américain est disponible en seconde piste.

CRÉDITS DES IMAGES
Edsger Wybe Dijkstra — Hamilton Richards, CC BY-SA 3.0
via Wikimedia Commons
Licence : creativecommons.org/licenses/by-sa/3.0/

CHAPITRES
00:00 Six mots
00:42 N’écrire que les phrases
01:08 Une vieille idée
01:45 Des modèles au lieu du code
02:32 Est-ce que ça a marché ?
03:07 La blague des programmeurs
03:35 L’avertissement de Dijkstra
04:04 Ce qui change cette fois
05:07 La spécification comme code source
06:01 À quoi ressemble un changement
07:26 Comment tu sais que ça a marché ?
08:39 Regarde ce qu’on a construit
09:21 Le programmeur du futur
```

## Bahasa Indonesia (`id`)

```
Mengapa kita masih menulis kode?
```

```
Ini adalah persyaratan lengkap untuk sebuah perangkat lunak bisnis: "Pengguna dapat membatalkan pesanan." Dalam bahasa Inggris, enam kata. Setiap pengembang akan mengangguk. Namun, hampir semua pertanyaan yang muncul dalam praktik tetap belum terjawab. Setelah fakturnya dikirim? Setelah pesanannya dikirim? Bagaimana dengan pemasok? Bagaimana kalau dua orang bertindak pada detik yang sama?

Sekarang ada ide yang menggoda: tulis spesifikasinya saja, simpan di dalam dokumen, tinjau, lalu biarkan AI yang menulis kodenya. Itu ide yang bagus. Tapi bukan ide baru. Video ini menelusuri hampir tujuh puluh tahun upaya menaikkan tingkat abstraksi saat kita memberi tahu komputer apa yang harus dilakukan, dan bertanya apa yang benar-benar berbeda kali ini.

Di sepanjang perjalanan: makalah tahun 1957 yang menyebut FORTRAN "sistem pengodean otomatis", alat CASE dan bahasa generasi keempat, Model Driven Architecture, low-code, survei terhadap 450 orang yang benar-benar menggunakan pengembangan berbasis model, catatan pendek Edsger Dijkstra "tentang kebodohan pemrograman dengan bahasa alami", dan sebuah bug di DynamoDB milik Amazon yang butuh 35 langkah untuk dipicu.

Sumber: Backus et al. (1957), The FORTRAN Automatic Coding System, Proceedings of the Western Joint Computer Conference; Object Management Group, Model Driven Architecture (2001); Richardson & Rymer (2014), Forrester Research; Whittle, Hutchinson & Rouncefield (2014), The State of Practice in Model-Driven Engineering, IEEE Software; Dijkstra, EWD 667 (1978); Newcombe et al. (2014), Use of Formal Methods at Amazon Web Services; CommitStrip (2016), A very comprehensive and precise spec.

Subtitel ditulis khusus untuk video ini, bukan dibuat secara otomatis. Tersedia juga trek audio kedua dalam bahasa Inggris Amerika.

KREDIT GAMBAR
Edsger Wybe Dijkstra — Hamilton Richards, CC BY-SA 3.0
melalui Wikimedia Commons
Lisensi: creativecommons.org/licenses/by-sa/3.0/

BAB
00:00 Enam kata
00:42 Tulis kalimatnya saja
01:08 Ide lama
01:45 Model sebagai ganti kode
02:32 Apakah ada yang berhasil?
03:07 Lelucon para programmer
03:35 Peringatan Dijkstra
04:04 Apa yang berbeda kali ini
05:07 Spesifikasi sebagai kode sumber
06:01 Seperti apa sebuah perubahan
07:26 Bagaimana kamu tahu itu berhasil?
08:39 Lihat apa yang sudah kita bangun
09:21 Programmer masa depan
```

## italiano (`it`)

```
Perché scriviamo ancora codice?
```

```
Ecco un requisito completo per un software gestionale: «Un utente può annullare un ordine.» Sei parole. Qualsiasi sviluppatore annuirebbe. Eppure lascia senza risposta quasi tutte le questioni concrete. Dopo che la fattura è partita? Dopo che l’ordine è stato spedito? E il fornitore? E se due persone agiscono nello stesso secondo?

Oggi c’è un’idea allettante: scrivere solo le specifiche, tenerle in documenti, revisionarle e lasciare che un’IA scriva il codice. È una buona idea. Ma non è nuova. Questo video ripercorre quasi settant’anni di tentativi di alzare il livello a cui diciamo ai computer cosa fare, e si chiede che cosa sia davvero diverso questa volta.

Lungo la strada: l’articolo del 1957 che definiva FORTRAN un «sistema di codifica automatica», gli strumenti CASE e i linguaggi di quarta generazione, la Model Driven Architecture, il low-code, un sondaggio su 450 persone che usavano davvero lo sviluppo guidato dai modelli, la breve nota di Edsger Dijkstra «sulla stoltezza della programmazione in linguaggio naturale» e un bug in DynamoDB di Amazon che per manifestarsi richiedeva 35 passaggi.

Fonti: Backus et al. (1957), The FORTRAN Automatic Coding System, Proceedings of the Western Joint Computer Conference; Object Management Group, Model Driven Architecture (2001); Richardson & Rymer (2014), Forrester Research; Whittle, Hutchinson & Rouncefield (2014), The State of Practice in Model-Driven Engineering, IEEE Software; Dijkstra, EWD 667 (1978); Newcombe et al. (2014), Use of Formal Methods at Amazon Web Services; CommitStrip (2016), A very comprehensive and precise spec.

I sottotitoli sono scritti per questo video, non generati automaticamente. Come seconda traccia audio è disponibile l’inglese americano.

CREDITI DELLE IMMAGINI
Edsger Wybe Dijkstra — Hamilton Richards, CC BY-SA 3.0
tramite Wikimedia Commons
Licenza: creativecommons.org/licenses/by-sa/3.0/

CAPITOLI
00:00 Sei parole
00:42 Scrivere solo le frasi
01:08 Un’idea vecchia
01:45 Modelli al posto del codice
02:32 Ha funzionato qualcosa?
03:07 La battuta dei programmatori
03:35 L’avvertimento di Dijkstra
04:04 Cosa cambia questa volta
05:07 La specifica come codice sorgente
06:01 Com’è fatta una modifica
07:26 Come fai a sapere che ha funzionato?
08:39 Guarda cosa abbiamo costruito
09:21 Il programmatore del futuro
```

## Deutsch (`de`)

```
Warum schreiben wir immer noch Code?
```

```
Hier ist eine vollständige Anforderung an eine Unternehmenssoftware: „Ein Nutzer kann eine Bestellung stornieren.“ Sechs Wörter. Jeder Entwickler würde nicken. Und doch lässt sie fast jede echte Frage offen. Wenn die Rechnung schon raus ist? Wenn die Bestellung schon verschickt ist? Was ist mit dem Lieferanten? Und was, wenn zwei Leute in derselben Sekunde handeln?

Heute gibt es eine verlockende Idee: nur noch die Spezifikationen schreiben, sie in Dokumenten festhalten, prüfen und den Code von einer KI schreiben lassen. Das ist eine gute Idee. Neu ist sie allerdings nicht. Dieses Video zeichnet nach, wie man seit fast siebzig Jahren versucht, die Ebene anzuheben, auf der wir Computern sagen, was sie tun sollen, und fragt, was diesmal wirklich anders ist.

Unterwegs: der Aufsatz von 1957, der FORTRAN ein „automatisches Codiersystem“ nannte, CASE-Werkzeuge und Sprachen der vierten Generation, Model Driven Architecture, Low-Code, eine Umfrage unter 450 Leuten, die modellgetriebene Entwicklung tatsächlich einsetzten, Edsger Dijkstras kurze Notiz „über die Torheit des Programmierens in natürlicher Sprache“ und ein Fehler in Amazons DynamoDB, dessen Auslösung 35 Schritte erforderte.

Quellen: Backus et al. (1957), The FORTRAN Automatic Coding System, Proceedings of the Western Joint Computer Conference; Object Management Group, Model Driven Architecture (2001); Richardson & Rymer (2014), Forrester Research; Whittle, Hutchinson & Rouncefield (2014), The State of Practice in Model-Driven Engineering, IEEE Software; Dijkstra, EWD 667 (1978); Newcombe et al. (2014), Use of Formal Methods at Amazon Web Services; CommitStrip (2016), A very comprehensive and precise spec.

Die Untertitel wurden für dieses Video geschrieben, nicht automatisch erzeugt. Als zweite Tonspur steht amerikanisches Englisch bereit.

BILDNACHWEIS
Edsger Wybe Dijkstra — Hamilton Richards, CC BY-SA 3.0
über Wikimedia Commons
Lizenz: creativecommons.org/licenses/by-sa/3.0/

KAPITEL
00:00 Sechs Wörter
00:42 Schreib nur die Sätze
01:08 Eine alte Idee
01:45 Modelle statt Code
02:32 Hat irgendetwas davon funktioniert?
03:07 Der Witz der Programmierer
03:35 Dijkstras Warnung
04:04 Was diesmal anders ist
05:07 Die Spezifikation als Quellcode
06:01 Wie eine Änderung aussieht
07:26 Woher weißt du, dass es funktioniert hat?
08:39 Schau dir an, was wir gebaut haben
09:21 Der Programmierer der Zukunft
```

## polski (`pl`)

```
Dlaczego wciąż piszemy kod?
```

```
Oto kompletne wymaganie dla oprogramowania biznesowego: „Użytkownik może anulować zamówienie.” Po angielsku to sześć słów. Każdy programista by przytaknął. A jednak pozostawia bez odpowiedzi prawie wszystkie pytania, które pojawiają się w praktyce. Kiedy faktura już poszła? Kiedy zamówienie zostało już wysłane? A co z dostawcą? A co, jeśli dwie osoby zadziałają w tej samej sekundzie?

Dziś kusi pewien pomysł: pisać tylko specyfikacje, trzymać je w dokumentach, przeglądać je, a kod niech napisze AI. To dobry pomysł. Tyle że nienowy. Ten film śledzi blisko siedemdziesiąt lat prób podniesienia poziomu, na którym mówimy komputerom, co mają robić, i pyta, co tym razem jest naprawdę inne.

Po drodze: artykuł z 1957 roku, który nazwał FORTRAN „automatycznym systemem kodowania”, narzędzia CASE i języki czwartej generacji, Model Driven Architecture, low-code, ankieta wśród 450 osób, które naprawdę stosowały programowanie sterowane modelem, krótka notatka Edsgera Dijkstry „o głupocie programowania w języku naturalnym” i błąd w DynamoDB Amazona, którego wywołanie wymagało 35 kroków.

Źródła: Backus et al. (1957), The FORTRAN Automatic Coding System, Proceedings of the Western Joint Computer Conference; Object Management Group, Model Driven Architecture (2001); Richardson & Rymer (2014), Forrester Research; Whittle, Hutchinson & Rouncefield (2014), The State of Practice in Model-Driven Engineering, IEEE Software; Dijkstra, EWD 667 (1978); Newcombe et al. (2014), Use of Formal Methods at Amazon Web Services; CommitStrip (2016), A very comprehensive and precise spec.

Napisy są pisane do tego filmu, nie generowane automatycznie. Jako druga ścieżka dźwiękowa dostępny jest angielski amerykański.

ŹRÓDŁA ZDJĘĆ
Edsger Wybe Dijkstra — Hamilton Richards, CC BY-SA 3.0
przez Wikimedia Commons
Licencja: creativecommons.org/licenses/by-sa/3.0/

ROZDZIAŁY
00:00 Sześć słów
00:42 Pisz tylko zdania
01:08 Stary pomysł
01:45 Modele zamiast kodu
02:32 Czy coś z tego zadziałało?
03:07 Żart programistów
03:35 Ostrzeżenie Dijkstry
04:04 Co tym razem jest inne
05:07 Specyfikacja jako kod źródłowy
06:01 Jak wygląda zmiana
07:26 Skąd wiesz, że zadziałało?
08:39 Spójrz, co zbudowaliśmy
09:21 Programista przyszłości
```

## português (Brasil) (`pt-BR`)

```
Por que ainda escrevemos código?
```

```
Aqui está um requisito completo para um software empresarial: "Um usuário pode cancelar um pedido." Seis palavras. Qualquer desenvolvedor concordaria. E, mesmo assim, ele deixa em aberto quase todas as questões práticas. Depois que a fatura já foi enviada? Depois que o pedido já foi despachado? E o fornecedor? E se duas pessoas agirem no mesmo segundo?

Hoje existe uma ideia tentadora: escrever só as especificações, guardá-las em documentos, revisá-las e deixar uma IA escrever o código. É uma boa ideia. Mas também não é nova. Este vídeo acompanha quase setenta anos de tentativas de elevar o nível em que dizemos aos computadores o que fazer, e pergunta o que é realmente diferente desta vez.

Pelo caminho: o artigo de 1957 que chamou o FORTRAN de "sistema de codificação automática", as ferramentas CASE e as linguagens de quarta geração, a Model Driven Architecture, o low-code, uma pesquisa com 450 pessoas que realmente usavam desenvolvimento orientado a modelos, a nota curta de Edsger Dijkstra "sobre a tolice da programação em linguagem natural" e um bug no DynamoDB da Amazon que precisava de 35 passos para ser disparado.

Fontes: Backus et al. (1957), The FORTRAN Automatic Coding System, Proceedings of the Western Joint Computer Conference; Object Management Group, Model Driven Architecture (2001); Richardson & Rymer (2014), Forrester Research; Whittle, Hutchinson & Rouncefield (2014), The State of Practice in Model-Driven Engineering, IEEE Software; Dijkstra, EWD 667 (1978); Newcombe et al. (2014), Use of Formal Methods at Amazon Web Services; CommitStrip (2016), A very comprehensive and precise spec.

As legendas foram escritas para este vídeo, não geradas automaticamente. Como segunda faixa de áudio está disponível o inglês americano.

CRÉDITOS DAS IMAGENS
Edsger Wybe Dijkstra — Hamilton Richards, CC BY-SA 3.0
via Wikimedia Commons
Licença: creativecommons.org/licenses/by-sa/3.0/

CAPÍTULOS
00:00 Seis palavras
00:42 Escrever só as frases
01:08 Uma ideia antiga
01:45 Modelos em vez de código
02:32 Alguma coisa funcionou?
03:07 A piada dos programadores
03:35 O alerta de Dijkstra
04:04 O que muda desta vez
05:07 A especificação como código-fonte
06:01 Como é uma mudança
07:26 Como você sabe que funcionou?
08:39 Olhe o que construímos
09:21 O programador do futuro
```

## Türkçe (`tr`)

```
Neden hâlâ kod yazıyoruz?
```

```
İşte bir iş yazılımı için eksiksiz bir gereksinim: "Kullanıcı bir siparişi iptal edebilir." İngilizcesi altı kelime. Her geliştirici başını sallardı. Yine de uygulamada ortaya çıkan soruların neredeyse hepsini yanıtsız bırakıyor. Fatura gönderildikten sonra mı? Sipariş kargoya verildikten sonra mı? Peki ya tedarikçi? Peki ya iki kişi aynı saniyede işlem yaparsa?

Bugün cazip bir fikir var: sadece spesifikasyonları yaz, onları belgelerde tut, gözden geçir ve kodu yapay zekâ yazsın. İyi bir fikir. Ama yeni değil. Bu video, bilgisayarlara ne yapacaklarını söylediğimiz seviyeyi yükseltmeye yönelik yaklaşık yetmiş yıllık denemelerin izini sürüyor ve bu sefer gerçekten neyin farklı olduğunu soruyor.

Yol boyunca: FORTRAN'ı "otomatik kodlama sistemi" olarak tanımlayan 1957 tarihli makale, CASE araçları ve dördüncü nesil diller, Model Driven Architecture, low-code, model güdümlü geliştirmeyi gerçekten kullanan 450 kişiyle yapılan bir anket, Edsger Dijkstra'nın "doğal dille programlamanın budalalığı üzerine" kısa notu ve Amazon'un DynamoDB'sinde tetiklenmesi için 35 adım gereken bir hata.

Kaynaklar: Backus et al. (1957), The FORTRAN Automatic Coding System, Proceedings of the Western Joint Computer Conference; Object Management Group, Model Driven Architecture (2001); Richardson & Rymer (2014), Forrester Research; Whittle, Hutchinson & Rouncefield (2014), The State of Practice in Model-Driven Engineering, IEEE Software; Dijkstra, EWD 667 (1978); Newcombe et al. (2014), Use of Formal Methods at Amazon Web Services; CommitStrip (2016), A very comprehensive and precise spec.

Altyazılar bu video için yazıldı, otomatik olarak oluşturulmadı. İkinci ses parçası olarak Amerikan İngilizcesi de mevcut.

GÖRSEL KAYNAKLARI
Edsger Wybe Dijkstra — Hamilton Richards, CC BY-SA 3.0
Wikimedia Commons aracılığıyla
Lisans: creativecommons.org/licenses/by-sa/3.0/

BÖLÜMLER
00:00 Altı kelime
00:42 Sadece cümleleri yaz
01:08 Eski bir fikir
01:45 Kod yerine modeller
02:32 Bunlardan biri işe yaradı mı?
03:07 Programcıların şakası
03:35 Dijkstra'nın uyarısı
04:04 Bu sefer farklı olan ne
05:07 Kaynak kod olarak spesifikasyon
06:01 Bir değişiklik neye benzer
07:26 İşe yaradığını nereden bileceksin?
08:39 Ne inşa ettiğimize bak
09:21 Geleceğin programcısı
```

## українська (`uk`)

```
Чому ми досі пишемо код?
```

```
Ось повна вимога до програми для бізнесу: «Користувач може скасувати замовлення». Англійською це шість слів. Будь-який розробник кивнув би. І все ж вона залишає відкритими майже всі справжні питання. Коли рахунок уже надіслано? Коли замовлення вже відправили? А що з постачальником? А що, як двоє людей щось зроблять в одну й ту саму секунду?

Сьогодні є спокуслива ідея: писати тільки специфікації, зберігати їх у документах, рецензувати, а код нехай пише ШІ. Це добра ідея. Але не нова. Це відео простежує майже сімдесят років спроб підняти рівень, на якому ми кажемо комп’ютерам, що робити, і питає, що цього разу справді інакше.

А ще у відео: стаття 1957 року, яка назвала FORTRAN «системою автоматичного кодування», інструменти CASE і мови четвертого покоління, Model Driven Architecture, low-code, опитування 450 людей, які справді застосовували модельно-орієнтовану розробку, коротка нотатка Едсгера Дейкстри «про безглуздість програмування природною мовою» і помилка в DynamoDB від Amazon, для прояву якої знадобилося 35 кроків.

Джерела: Backus et al. (1957), The FORTRAN Automatic Coding System, Proceedings of the Western Joint Computer Conference; Object Management Group, Model Driven Architecture (2001); Richardson & Rymer (2014), Forrester Research; Whittle, Hutchinson & Rouncefield (2014), The State of Practice in Model-Driven Engineering, IEEE Software; Dijkstra, EWD 667 (1978); Newcombe et al. (2014), Use of Formal Methods at Amazon Web Services; CommitStrip (2016), A very comprehensive and precise spec.

Субтитри написані для цього відео, а не згенеровані автоматично. Також доступна друга звукова доріжка — американською англійською.

ДЖЕРЕЛА ЗОБРАЖЕНЬ
Edsger Wybe Dijkstra — Hamilton Richards, CC BY-SA 3.0
через Wikimedia Commons
Ліцензія: creativecommons.org/licenses/by-sa/3.0/

РОЗДІЛИ
00:00 Шість слів
00:42 Писати тільки речення
01:08 Стара ідея
01:45 Моделі замість коду
02:32 Чи спрацювало хоч щось?
03:07 Жарт програмістів
03:35 Застереження Дейкстри
04:04 Що інакше цього разу
05:07 Специфікація як вихідний код
06:01 Як виглядає зміна
07:26 Звідки ти знаєш, що це спрацювало?
08:39 Подивись, що ми збудували
09:21 Програміст майбутнього
```

## Tiếng Việt (`vi`)

```
Vì sao chúng ta vẫn còn viết mã?
```

```
Đây là một yêu cầu hoàn chỉnh cho một phần mềm doanh nghiệp: "Người dùng có thể hủy đơn hàng." Trong tiếng Anh, chỉ sáu từ. Lập trình viên nào cũng sẽ gật đầu. Vậy mà nó bỏ ngỏ gần như mọi câu hỏi thực tế. Sau khi hóa đơn đã được gửi đi? Sau khi hàng đã xuất kho? Còn nhà cung cấp thì sao? Nếu hai người cùng thao tác trong cùng một giây thì sao?

Ngày nay có một ý tưởng đầy hấp dẫn: chỉ viết các bản đặc tả, lưu chúng trong tài liệu, duyệt lại và để AI viết mã. Đó là một ý tưởng hay. Nhưng nó cũng không mới. Video này đi qua gần bảy mươi năm nỗ lực nâng cao mức độ trừu tượng khi chúng ta bảo máy tính phải làm gì, và đặt câu hỏi: lần này thực sự có gì khác?

Video cũng đề cập đến: bài báo năm 1957 gọi FORTRAN là "hệ thống viết mã tự động", các công cụ CASE và ngôn ngữ thế hệ thứ tư, Model Driven Architecture, low-code, một khảo sát với 450 người thực sự áp dụng phát triển hướng mô hình, ghi chú ngắn của Edsger Dijkstra "về sự ngu ngốc của lập trình bằng ngôn ngữ tự nhiên", và một lỗi trong DynamoDB của Amazon cần đến 35 bước mới kích hoạt được.

Nguồn: Backus et al. (1957), The FORTRAN Automatic Coding System, Proceedings of the Western Joint Computer Conference; Object Management Group, Model Driven Architecture (2001); Richardson & Rymer (2014), Forrester Research; Whittle, Hutchinson & Rouncefield (2014), The State of Practice in Model-Driven Engineering, IEEE Software; Dijkstra, EWD 667 (1978); Newcombe et al. (2014), Use of Formal Methods at Amazon Web Services; CommitStrip (2016), A very comprehensive and precise spec.

Phụ đề được viết riêng cho video này, không phải tạo tự động. Có thể chọn tiếng Anh Mỹ ở bản âm thanh thứ hai.

NGUỒN HÌNH ẢNH
Edsger Wybe Dijkstra — Hamilton Richards, CC BY-SA 3.0
qua Wikimedia Commons
Giấy phép: creativecommons.org/licenses/by-sa/3.0/

CHƯƠNG
00:00 Sáu từ
00:42 Chỉ viết các câu chữ
01:08 Một ý tưởng cũ
01:45 Mô hình thay cho mã
02:32 Có cái nào hiệu quả không?
03:07 Câu đùa của lập trình viên
03:35 Lời cảnh báo của Dijkstra
04:04 Lần này có gì khác
05:07 Đặc tả là mã nguồn
06:01 Một thay đổi trông như thế nào
07:26 Làm sao bạn biết nó hoạt động?
08:39 Hãy nhìn những gì ta đã xây
09:21 Lập trình viên của tương lai
```

## čeština (`cs`)

```
Proč pořád píšeme kód?
```

```
Tohle je úplný požadavek na kus podnikového softwaru: „Uživatel může zrušit objednávku.“ Anglicky šest slov. Každý vývojář by přikývl. A přesto nechává otevřené skoro všechny otázky, na kterých v praxi záleží. Když už odešla faktura? Když už je objednávka odeslaná? A co dodavatel? Co když dva lidé zasáhnou v téže vteřině?

Dnes se nabízí lákavý nápad: psát jen specifikace, držet je v dokumentech, revidovat je a kód nechat napsat AI. Je to dobrý nápad. Jenže není nový. Video sleduje skoro sedmdesát let pokusů zvednout úroveň, na které počítačům říkáme, co mají dělat, a ptá se, co je tentokrát doopravdy jinak.

Cestou: článek z roku 1957, který FORTRAN nazval „systémem automatického kódování“, nástroje CASE a jazyky čtvrté generace, Model Driven Architecture, low-code, průzkum mezi 450 lidmi, kteří modelem řízený vývoj skutečně používali, krátká poznámka Edsgera Dijkstry „o pošetilosti programování v přirozeném jazyce“ a chyba v DynamoDB od Amazonu, k jejímuž vyvolání bylo potřeba 35 kroků.

Zdroje: Backus et al. (1957), The FORTRAN Automatic Coding System, Proceedings of the Western Joint Computer Conference; Object Management Group, Model Driven Architecture (2001); Richardson & Rymer (2014), Forrester Research; Whittle, Hutchinson & Rouncefield (2014), The State of Practice in Model-Driven Engineering, IEEE Software; Dijkstra, EWD 667 (1978); Newcombe et al. (2014), Use of Formal Methods at Amazon Web Services; CommitStrip (2016), A very comprehensive and precise spec.

Titulky jsou psané pro tohle video, ne strojový přepis. Jako druhá zvuková stopa je k dispozici americká angličtina.

ZDROJE OBRÁZKŮ
Edsger Wybe Dijkstra — Hamilton Richards, CC BY-SA 3.0
prostřednictvím Wikimedia Commons
Licence: creativecommons.org/licenses/by-sa/3.0/

KAPITOLY
00:00 Šest slov
00:42 Psát jen ty věty
01:08 Starý nápad
01:45 Modely místo kódu
02:32 Fungovalo z toho něco?
03:07 Programátorský vtip
03:35 Dijkstrovo varování
04:04 Co je tentokrát jinak
05:07 Specifikace jako zdrojový kód
06:01 Jak vypadá změna
07:26 Jak poznáš, že to vyšlo?
08:39 Podívej se, co jsme postavili
09:21 Programátor budoucnosti
```

## español (`es`)

```
¿Por qué seguimos escribiendo código?
```

```
Aquí tienes un requisito completo para un programa de gestión empresarial: «Un usuario puede cancelar un pedido». Seis palabras. Cualquier desarrollador asentiría. Y, sin embargo, deja abiertas casi todas las preguntas reales. ¿Cuando ya se ha enviado la factura? ¿Cuando el pedido ya se ha despachado? ¿Y el proveedor? ¿Y si dos personas actúan en el mismo segundo?

Hoy circula una idea tentadora: escribir solo las especificaciones, guardarlas en documentos, revisarlas y dejar que una IA escriba el código. Es una buena idea. Pero tampoco es nueva. Este vídeo recorre casi setenta años de intentos de subir el nivel al que les decimos a los ordenadores qué hacer, y se pregunta qué es realmente distinto esta vez.

Por el camino: el artículo de 1957 que llamó a FORTRAN «sistema de codificación automática», las herramientas CASE y los lenguajes de cuarta generación, Model Driven Architecture, el low-code, una encuesta a 450 personas que de verdad usaban el desarrollo dirigido por modelos, la breve nota de Edsger Dijkstra «sobre la insensatez de programar en lenguaje natural» y un error en DynamoDB de Amazon que requería 35 pasos para manifestarse.

Fuentes: Backus et al. (1957), The FORTRAN Automatic Coding System, Proceedings of the Western Joint Computer Conference; Object Management Group, Model Driven Architecture (2001); Richardson & Rymer (2014), Forrester Research; Whittle, Hutchinson & Rouncefield (2014), The State of Practice in Model-Driven Engineering, IEEE Software; Dijkstra, EWD 667 (1978); Newcombe et al. (2014), Use of Formal Methods at Amazon Web Services; CommitStrip (2016), A very comprehensive and precise spec.

Los subtítulos están escritos para este vídeo, no generados automáticamente. Como segunda pista de audio está disponible el inglés americano.

CRÉDITOS DE LAS IMÁGENES
Edsger Wybe Dijkstra — Hamilton Richards, CC BY-SA 3.0
vía Wikimedia Commons
Licencia: creativecommons.org/licenses/by-sa/3.0/

CAPÍTULOS
00:00 Seis palabras
00:42 Escribir solo las frases
01:08 Una idea antigua
01:45 Modelos en lugar de código
02:32 ¿Funcionó algo de todo eso?
03:07 El chiste de los programadores
03:35 La advertencia de Dijkstra
04:04 Qué es distinto esta vez
05:07 La especificación como código fuente
06:01 Cómo es un cambio
07:26 ¿Cómo sabes que funcionó?
08:39 Mira lo que hemos construido
09:21 El programador del futuro
```

## svenska (`sv`)

```
Varför skriver vi fortfarande kod?
```

```
Här är ett komplett krav på ett affärssystem: ”En användare kan avbryta en beställning.” Sex ord. Varje utvecklare skulle nicka. Ändå lämnar det nästan alla praktiska frågor obesvarade. Efter att fakturan har gått iväg? Efter att beställningen har skickats? Och leverantören? Och om två personer agerar i samma sekund?

I dag finns det en lockande idé: skriv bara specifikationerna, spara dem i dokument, granska dem och låt en AI skriva koden. Det är en bra idé. Men den är inte ny. Den här videon följer nästan sjuttio år av försök att höja den nivå där vi talar om för datorer vad de ska göra, och frågar vad som verkligen är annorlunda den här gången.

Längs vägen: artikeln från 1957 som kallade FORTRAN ett ”automatiskt kodningssystem”, CASE-verktyg och fjärde generationens språk, Model Driven Architecture, low-code, en enkät bland 450 personer som faktiskt använde modelldriven utveckling, Edsger Dijkstras korta text ”om dårskapen i att programmera på naturligt språk” och en bugg i Amazons DynamoDB som krävde 35 steg för att utlösas.

Källor: Backus et al. (1957), The FORTRAN Automatic Coding System, Proceedings of the Western Joint Computer Conference; Object Management Group, Model Driven Architecture (2001); Richardson & Rymer (2014), Forrester Research; Whittle, Hutchinson & Rouncefield (2014), The State of Practice in Model-Driven Engineering, IEEE Software; Dijkstra, EWD 667 (1978); Newcombe et al. (2014), Use of Formal Methods at Amazon Web Services; CommitStrip (2016), A very comprehensive and precise spec.

Undertexterna är skrivna för den här videon, inte automatgenererade. Som andra ljudspår finns amerikansk engelska.

BILDKÄLLOR
Edsger Wybe Dijkstra — Hamilton Richards, CC BY-SA 3.0
via Wikimedia Commons
Licens: creativecommons.org/licenses/by-sa/3.0/

KAPITEL
00:00 Sex ord
00:42 Skriv bara meningarna
01:08 En gammal idé
01:45 Modeller i stället för kod
02:32 Fungerade något av det?
03:07 Programmerarnas skämt
03:35 Dijkstras varning
04:04 Vad som är annorlunda nu
05:07 Specifikationen som källkod
06:01 Hur en ändring ser ut
07:26 Hur vet du att det fungerade?
08:39 Titta på vad vi har byggt
09:21 Framtidens programmerare
```
