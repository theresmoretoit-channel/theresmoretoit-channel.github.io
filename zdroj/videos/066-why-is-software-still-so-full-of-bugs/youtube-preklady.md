# Lokalizované názvy a popisy — 066

Čte `tools/lokalizace.py` a nahrává přes `videos.update(part="localizations")`.
Anglický titul a popis jsou v `youtube.md` a posílají se zpátky beze změny.

## Co se NEPŘEKLÁDÁ

- **vlastní jména a termíny** — Windows, Linux, C, Rust, seL4, Big Bang,
  jména Edsger Dijkstra, Alan Turing, Henry Rice, Hamilton Richards,
  Elliott & Fry, název licence a adresa `creativecommons.org`
- **`2^100`** a **letopočty** (1936, 1953, 2009, 2024) — číslicí
- **časy kapitol** na vteřinu
- **tagy** — YouTube je per-jazyk nemá

## Kontrola čísel

Kapitolové časy jsou z `work/timing.json`. Po jakékoli změně stopáže je
přepočítat. Registr podle překladu scénáře: cs vyká, de `Sie`, es/it/pl/fr
tykají, sv `du`, uk/tr/id vykají, fi `sinä`, vi `bạn`.

## suomi (`fi`)

```
Miksi ohjelmistot ovat yhä täynnä bugeja?
```

```
Muutaman päivän välein taas yksi vakava bugi nousee uutisiin — sellainen,
joka vuotaa yksityisiä tietoja tai luovuttaa tietokoneen hyökkääjälle. Ja
reaktio on lähes aina sama: nämä ovat ammattilaisia, joilla on
koodikatselmoinnit, testit ja auditoinnit. Miten bugeja siis tulee koko
ajan lisää?

Tämä video kertoo miksi, eikä vastaus ole "huonot ohjelmoijat". Se on
matematiikkaan rakennettu seinä. Ohjelmassa, jossa on vain sata päällä-tai-
pois-asetusta, on jo enemmän yhdistelmiä kuin ehtisit koskaan testata —
enemmän kuin jos olisit alkanut tarkistaa miljardia niistä joka sekunti
alkuräjähdyksestä. Oikeissa ohjelmissa on miljoonia kytkimiä. "Testataan
vain kaikki" ei ole kallista. Se on mahdotonta.

Siitä se vain syvenee: muistibugit, joilla hyökkääjät ajavat omaa
koodiaan, se ettei mikään ohjelma voi tarkistaa jokaista toista ohjelmaa
(Alan Turing todisti sen 1936, Henry Rice meni pidemmälle 1953), ja koukku,
että täyskin matemaattinen todistus osoittaa vain, että koodi vastaa
määrittelyä — ja määrittelyn kirjoittavat ihmiset.

Joten ehkä "miten kirjoitamme ohjelmistoa ilman bugeja?" on väärä kysymys.
Parempi on: miten rakennamme järjestelmiä, jotka pysyvät turvassa silloinkin,
kun ohjelmistossa on bugeja?

Tekstitykset on kirjoitettu tätä videota varten, ei koneellisesti. Toisena
ääniraitana on amerikanenglanti.

Koko teksti, lähteet ja käännökset: https://theresmoretoit-channel.github.io/fi/videos/why-is-software-still-so-full-of-bugs/

LUVUT
00:00 Taas bugi uutisissa
00:44 Sata kytkintä, ja 2^100
01:27 Yksinkertaisin asia, jonka ohjelma tekee
02:34 C ja hallinta muistiin
04:04 Uudemmat kielet ja kääntäjä
04:33 Muistiturvallinen, ja silti väärä
05:04 Mitä testi voi ja ei voi todistaa
05:29 Ohjelma, joka todistaa ohjelmia?
06:33 seL4: todistettu oikeaksi, hintaan
07:15 Bugia ei tarvitse kirjoittaa
07:51 Paremmat työkalut, enemmän haavoittuvuuksia
08:33 Parempi kysymys
08:50 Miten järjestelmä vartioi muistia nykyään
09:23 Jos bugit ovat väistämättömiä
10:00 "Se toimii" vs. "se on turvallinen"

KUVALÄHTEET
Edsger W. Dijkstra — Hamilton Richards, CC BY-SA 3.0
via Wikimedia Commons
Lisenssi: creativecommons.org/licenses/by-sa/3.0/

Alan Turingin valokuva on public domain.
```

## français (`fr`)

```
Pourquoi les logiciels sont-ils encore pleins de bugs ?
```

```
Tous les quelques jours, un nouveau bug grave fait la une — un bug qui
laisse fuiter des données privées ou livre un ordinateur à un attaquant.
Et la réaction est presque toujours la même : ce sont des professionnels,
avec des revues de code, des tests et des audits. Alors comment les bugs
continuent-ils d'arriver ?

Cette vidéo explique pourquoi, et la réponse n'est pas « de mauvais
programmeurs ». C'est un mur inscrit dans les mathématiques. Un programme
avec seulement cent réglages activés ou désactivés a déjà plus de
combinaisons que tu ne pourrais jamais en tester — plus que si tu avais
commencé à en vérifier un milliard par seconde au Big Bang. Les vrais
programmes en ont des millions. « Il suffit de tout tester » n'est pas cher.
C'est impossible.

Ensuite, ça ne fait que s'approfondir : des bugs mémoire qui laissent les
attaquants exécuter leur propre code, le fait qu'aucun programme ne peut
vérifier tous les autres (Alan Turing l'a prouvé en 1936, Henry Rice est
allé plus loin en 1953), et le hic qu'une preuve mathématique complète
montre seulement que le code correspond à une spécification — et la
spécification est écrite par des gens.

Alors peut-être que « comment écrire un logiciel sans bugs ? » est la
mauvaise question. La meilleure : comment construire des systèmes qui
restent sûrs même quand le logiciel a des bugs ?

Les sous-titres sont écrits pour cette vidéo, pas générés automatiquement.
Une piste audio en anglais américain est disponible comme deuxième piste.

Transcription complète, sources et traductions : https://theresmoretoit-channel.github.io/fr/videos/why-is-software-still-so-full-of-bugs/

CHAPITRES
00:00 Encore un bug dans l'actualité
00:44 Cent interrupteurs, et 2^100
01:27 La chose la plus simple qu'un programme fasse
02:34 Le C et le contrôle de la mémoire
04:04 Les langages plus récents et le compilateur
04:33 Sûr côté mémoire, et pourtant faux
05:04 Ce qu'un test peut et ne peut pas prouver
05:29 Un programme qui prouve les programmes ?
06:33 seL4 : prouvé correct, à quel prix
07:15 Tu n'as pas besoin d'écrire un bug
07:51 De meilleurs outils, plus de failles
08:33 La meilleure question
08:50 Comment le système protège la mémoire aujourd'hui
09:23 Si les bugs sont inévitables
10:00 « Ça marche » contre « c'est sûr »

CRÉDITS IMAGES
Edsger W. Dijkstra — Hamilton Richards, CC BY-SA 3.0
via Wikimedia Commons
Licence : creativecommons.org/licenses/by-sa/3.0/

La photographie d'Alan Turing est dans le domaine public.
```

## Bahasa Indonesia (`id`)

```
Kenapa Perangkat Lunak Masih Penuh Bug?
```

```
Setiap beberapa hari, satu bug serius lagi muncul di berita — bug yang
membocorkan data pribadi, atau menyerahkan sebuah komputer ke penyerang.
Dan reaksinya hampir selalu sama: mereka ini profesional, punya tinjauan
kode, uji, dan audit. Jadi kenapa bug terus saja bermunculan?

Video ini soal kenapa, dan jawabannya bukan "pemrogram yang buruk". Ini
tembok yang tertanam di dalam matematika. Sebuah program dengan seratus
pengaturan nyala-atau-mati saja sudah punya lebih banyak kombinasi daripada
yang bisa Anda uji — lebih banyak daripada jika Anda mulai memeriksa satu
miliar kombinasi setiap detik sejak Big Bang. Program sungguhan punya jutaan
sakelar. "Tinggal uji semuanya" bukan mahal. Itu mustahil.

Dari sana justru makin dalam: bug memori yang membuat penyerang bisa
menjalankan kodenya sendiri, kenyataan bahwa tak ada program yang bisa
memeriksa setiap program lain (Alan Turing membuktikannya pada 1936, Henry
Rice melangkah lebih jauh pada 1953), dan jebakan bahwa bahkan bukti
matematis penuh hanya menunjukkan kode cocok dengan sebuah spesifikasi —
dan spesifikasi itu ditulis oleh manusia.

Jadi mungkin "bagaimana kita menulis perangkat lunak tanpa bug?" adalah
pertanyaan yang salah. Yang lebih baik: bagaimana kita membangun sistem yang
tetap aman bahkan ketika perangkat lunaknya punya bug?

Subtitel ditulis untuk video ini, bukan dibuat otomatis. Trek audio bahasa
Inggris Amerika tersedia sebagai trek audio kedua.

Transkrip lengkap, sumber, dan terjemahan: https://theresmoretoit-channel.github.io/id/videos/why-is-software-still-so-full-of-bugs/

BAB
00:00 Lagi-lagi bug di berita
00:44 Seratus sakelar, dan 2^100
01:27 Hal paling sederhana yang dilakukan program
02:34 C, dan kendali atas memori
04:04 Bahasa yang lebih baru dan kompiler
04:33 Aman memori, dan tetap salah
05:04 Apa yang bisa dan tak bisa dibuktikan sebuah uji
05:29 Program yang membuktikan program?
06:33 seL4: dibuktikan benar, dengan harga mahal
07:15 Anda tak perlu menulis bug
07:51 Alat makin baik, kerentanan makin banyak
08:33 Pertanyaan yang lebih baik
08:50 Bagaimana sistem menjaga memori sekarang
09:23 Kalau bug tak terhindarkan
10:00 "Masih berfungsi" vs "masih aman"

KREDIT GAMBAR
Edsger W. Dijkstra — Hamilton Richards, CC BY-SA 3.0
via Wikimedia Commons
Lisensi: creativecommons.org/licenses/by-sa/3.0/

Foto Alan Turing adalah domain publik.
```

## italiano (`it`)

```
Perché il software è ancora pieno di bug?
```

```
Ogni pochi giorni, un altro bug grave finisce nelle notizie — uno che fa
trapelare dati privati o consegna un computer a un aggressore. E la reazione
è quasi sempre la stessa: sono professionisti, con revisioni del codice,
test e audit. Allora come mai i bug continuano ad arrivare?

Questo video parla del perché, e la risposta non è "programmatori scarsi".
È un muro iscritto nella matematica. Un programma con appena cento
impostazioni accese o spente ha già più combinazioni di quante potresti mai
provarne — più che se avessi iniziato a controllarne un miliardo al secondo
dal Big Bang. I programmi veri ne hanno milioni. "Basta provare tutto" non è
costoso. È impossibile.

Da lì si va solo più a fondo: bug di memoria che lasciano eseguire agli
aggressori il proprio codice, il fatto che nessun programma può controllare
ogni altro programma (Alan Turing lo dimostrò nel 1936, Henry Rice andò
oltre nel 1953), e il tranello che perfino una dimostrazione matematica
completa mostra solo che il codice corrisponde a una specifica — e la
specifica è scritta da persone.

Quindi forse "come scriviamo software senza bug?" è la domanda sbagliata.
Quella migliore è: come costruiamo sistemi che restano sicuri anche quando
il software ha dei bug?

I sottotitoli sono scritti per questo video, non generati automaticamente.
Una traccia audio in inglese americano è disponibile come seconda traccia.

Trascrizione completa, fonti e traduzioni: https://theresmoretoit-channel.github.io/it/videos/why-is-software-still-so-full-of-bugs/

CAPITOLI
00:00 Ancora un bug nelle notizie
00:44 Cento interruttori, e 2^100
01:27 La cosa più semplice che un programma faccia
02:34 Il C e il controllo sulla memoria
04:04 I linguaggi più recenti e il compilatore
04:33 Sicuro in memoria, e comunque sbagliato
05:04 Cosa può e non può dimostrare un test
05:29 Un programma che dimostra i programmi?
06:33 seL4: dimostrato corretto, a caro prezzo
07:15 Non devi scrivere un bug
07:51 Strumenti migliori, più vulnerabilità
08:33 La domanda migliore
08:50 Come il sistema protegge la memoria oggi
09:23 Se i bug sono inevitabili
10:00 "Funziona" contro "è sicuro"

CREDITI IMMAGINI
Edsger W. Dijkstra — Hamilton Richards, CC BY-SA 3.0
via Wikimedia Commons
Licenza: creativecommons.org/licenses/by-sa/3.0/

La fotografia di Alan Turing è di pubblico dominio.
```

## Deutsch (`de`)

```
Warum steckt Software noch immer voller Bugs?
```

```
Alle paar Tage taucht ein weiterer schwerer Bug in den Nachrichten auf —
einer, der private Daten preisgibt oder einem Angreifer einen Computer
übergibt. Und die Reaktion ist fast immer dieselbe: Das sind Profis, mit
Code-Reviews, Tests und Audits. Wie kommen die Bugs also immer weiter?

In diesem Video geht es um das Warum, und die Antwort lautet nicht
„schlechte Programmierer". Es ist eine Mauer, die in der Mathematik steckt.
Ein Programm mit nur hundert Ein-oder-Aus-Einstellungen hat schon mehr
Kombinationen, als Sie je testen könnten — mehr, als wenn Sie beim Urknall
begonnen hätten, jede Sekunde eine Milliarde zu prüfen. Echte Programme
haben Millionen von Schaltern. „Einfach alles testen" ist nicht teuer. Es
ist unmöglich.

Von dort wird es nur tiefer: Speicherbugs, mit denen Angreifer eigenen Code
ausführen, die Tatsache, dass kein Programm jedes andere prüfen kann (Alan
Turing bewies es 1936, Henry Rice ging 1953 weiter), und der Haken, dass
selbst ein vollständiger mathematischer Beweis nur zeigt, dass der Code
einer Spezifikation entspricht — und die Spezifikation schreiben Menschen.

Vielleicht ist also „Wie schreiben wir Software ohne Bugs?" die falsche
Frage. Die bessere: Wie bauen wir Systeme, die sicher bleiben, selbst wenn
die Software Bugs hat?

Die Untertitel sind für dieses Video geschrieben, nicht automatisch erzeugt.
Eine amerikanisch-englische Tonspur ist als zweite Tonspur verfügbar.

Vollständiger Text, Quellen und Übersetzungen: https://theresmoretoit-channel.github.io/de/videos/why-is-software-still-so-full-of-bugs/

KAPITEL
00:00 Wieder ein Bug in den Nachrichten
00:44 Hundert Schalter, und 2^100
01:27 Das Einfachste, was ein Programm tut
02:34 C und die Kontrolle über den Speicher
04:04 Neuere Sprachen und der Compiler
04:33 Speichersicher, und trotzdem falsch
05:04 Was ein Test beweisen kann und was nicht
05:29 Ein Programm, das Programme beweist?
06:33 seL4: bewiesen korrekt, um welchen Preis
07:15 Man muss einen Bug nicht schreiben
07:51 Bessere Werkzeuge, mehr Schwachstellen
08:33 Die bessere Frage
08:50 Wie das System den Speicher heute schützt
09:23 Wenn Bugs unvermeidlich sind
10:00 „Es funktioniert" gegen „es ist sicher"

BILDNACHWEISE
Edsger W. Dijkstra — Hamilton Richards, CC BY-SA 3.0
via Wikimedia Commons
Lizenz: creativecommons.org/licenses/by-sa/3.0/

Das Foto von Alan Turing ist gemeinfrei.
```

## polski (`pl`)

```
Dlaczego oprogramowanie wciąż jest pełne błędów?
```

```
Co kilka dni w wiadomościach pojawia się kolejny poważny błąd — taki, który
wycieka prywatne dane albo oddaje komputer napastnikowi. A reakcja jest
niemal zawsze taka sama: to profesjonaliści, mają przeglądy kodu, testy i
audyty. Więc jak to możliwe, że błędy wciąż się pojawiają?

Ten film opowiada dlaczego, a odpowiedź nie brzmi „słabi programiści". To
ściana wbudowana w matematykę. Program z zaledwie stoma ustawieniami
włączony-albo-wyłączony ma już więcej kombinacji, niż zdołałbyś kiedykolwiek
przetestować — więcej, niż gdybyś zaczął sprawdzać miliard z nich na sekundę
w chwili Wielkiego Wybuchu. Prawdziwe programy mają miliony przełączników.
„Po prostu sprawdź wszystko" nie jest drogie. Jest niemożliwe.

Dalej robi się tylko głębiej: błędy pamięci, dzięki którym napastnicy
uruchamiają własny kod, fakt, że żaden program nie sprawdzi każdego innego
(Alan Turing udowodnił to w 1936, Henry Rice poszedł dalej w 1953), oraz
haczyk, że nawet pełny dowód matematyczny pokazuje tylko, że kod zgadza się
ze specyfikacją — a specyfikację piszą ludzie.

Więc może „jak pisać oprogramowanie bez błędów?" to złe pytanie. Lepsze
brzmi: jak budować systemy, które pozostają bezpieczne, nawet gdy
oprogramowanie ma błędy?

Napisy są napisane do tego filmu, nie wygenerowane automatycznie. Druga
ścieżka dźwiękowa to amerykański angielski.

Pełna transkrypcja, źródła i tłumaczenia: https://theresmoretoit-channel.github.io/pl/videos/why-is-software-still-so-full-of-bugs/

ROZDZIAŁY
00:00 Znów błąd w wiadomościach
00:44 Sto przełączników i 2^100
01:27 Najprostsza rzecz, jaką robi program
02:34 C i kontrola nad pamięcią
04:04 Nowsze języki i kompilator
04:33 Bezpieczny pamięciowo, a wciąż błędny
05:04 Co test może, a czego nie może udowodnić
05:29 Program, który dowodzi programów?
06:33 seL4: dowiedziony poprawnym, wielkim kosztem
07:15 Nie musisz pisać błędu
07:51 Lepsze narzędzia, więcej podatności
08:33 Lepsze pytanie
08:50 Jak system pilnuje dziś pamięci
09:23 Skoro błędy są nieuniknione
10:00 „Działa" kontra „jest bezpieczne"

ŹRÓDŁA OBRAZÓW
Edsger W. Dijkstra — Hamilton Richards, CC BY-SA 3.0
via Wikimedia Commons
Licencja: creativecommons.org/licenses/by-sa/3.0/

Zdjęcie Alana Turinga jest w domenie publicznej.
```

## português (Brasil) (`pt-BR`)

```
Por que o software ainda é tão cheio de bugs?
```

```
A cada poucos dias, mais um bug sério aparece nas notícias — um que vaza
dados privados ou entrega um computador a um invasor. E a reação é quase
sempre a mesma: são profissionais, com revisões de código, testes e
auditorias. Então como os bugs continuam aparecendo?

Este vídeo é sobre o porquê, e a resposta não é "programadores ruins". É uma
parede embutida na matemática. Um programa com apenas cem configurações
ligadas ou desligadas já tem mais combinações do que você conseguiria testar
— mais do que se tivesse começado a checar um bilhão delas por segundo no
Big Bang. Programas de verdade têm milhões de chaves. "É só testar tudo" não
é caro. É impossível.

A partir daí só fica mais fundo: bugs de memória que deixam invasores rodar
o próprio código, o fato de que nenhum programa consegue verificar todos os
outros (Alan Turing provou em 1936, Henry Rice foi além em 1953), e o porém
de que até uma prova matemática completa só mostra que o código bate com uma
especificação — e a especificação é escrita por pessoas.

Então talvez "como escrevemos software sem bugs?" seja a pergunta errada. A
melhor é: como construímos sistemas que continuam seguros mesmo quando o
software tem bugs?

As legendas foram escritas para este vídeo, não geradas automaticamente. Há
uma faixa de áudio em inglês americano como segunda faixa.

Transcrição completa, fontes e traduções: https://theresmoretoit-channel.github.io/pt-br/videos/why-is-software-still-so-full-of-bugs/

CAPÍTULOS
00:00 Mais um bug nas notícias
00:44 Cem chaves, e 2^100
01:27 A coisa mais simples que um programa faz
02:34 O C e o controle da memória
04:04 As linguagens mais novas e o compilador
04:33 Seguro na memória, e ainda assim errado
05:04 O que um teste pode e não pode provar
05:29 Um programa que prova programas?
06:33 seL4: provado correto, a um preço
07:15 Você não precisa escrever um bug
07:51 Ferramentas melhores, mais vulnerabilidades
08:33 A pergunta melhor
08:50 Como o sistema protege a memória hoje
09:23 Se os bugs são inevitáveis
10:00 "Ainda funciona" vs "ainda é seguro"

CRÉDITOS DE IMAGENS
Edsger W. Dijkstra — Hamilton Richards, CC BY-SA 3.0
via Wikimedia Commons
Licença: creativecommons.org/licenses/by-sa/3.0/

A fotografia de Alan Turing é de domínio público.
```

## Türkçe (`tr`)

```
Yazılım Neden Hâlâ Hatalarla Dolu?
```

```
Birkaç günde bir, ciddi bir hata daha haberlere düşüyor — özel verileri
sızdıran ya da bir bilgisayarı bir saldırgana teslim eden bir hata. Ve tepki
neredeyse hep aynı: bunlar profesyoneller; kod incelemeleri, testleri ve
denetimleri var. Peki hatalar nasıl gelmeye devam ediyor?

Bu video nedenini anlatıyor ve yanıt "kötü programcılar" değil.
Matematiğin içine örülü bir duvar bu. Yalnızca yüz aç-kapa ayarı olan bir
programın bile, ömrün boyunca test edebileceğinden daha fazla kombinasyonu
var — Büyük Patlama'da saniyede bir milyarını kontrol etmeye başlasaydın
elde edeceğinden bile fazla. Gerçek programlarda milyonlarca anahtar var.
"Hepsini test et yeter" pahalı değil. İmkânsız.

Oradan iş yalnızca derinleşiyor: saldırganların kendi kodunu çalıştırmasına
izin veren bellek hataları, hiçbir programın her başka programı
denetleyememesi (Alan Turing 1936'da kanıtladı, Henry Rice 1953'te daha da
ileri gitti) ve tam bir matematiksel kanıtın bile yalnızca kodun bir
belirtimle uyuştuğunu göstermesi — belirtimi ise insanlar yazıyor.

Yani belki de "yazılımı nasıl hatasız yazarız?" yanlış soru. Daha iyisi:
yazılımda hatalar olsa bile güvende kalan sistemleri nasıl kurarız?

Altyazılar bu video için yazıldı, otomatik üretilmedi. İkinci ses parçası
olarak Amerikan İngilizcesi mevcut.

Metnin tamamı, kaynaklar ve çeviriler: https://theresmoretoit-channel.github.io/tr/videos/why-is-software-still-so-full-of-bugs/

BÖLÜMLER
00:00 Haberlerde yine bir hata
00:44 Yüz anahtar, ve 2^100
01:27 Bir programın yaptığı en basit şey
02:34 C ve bellek üzerindeki denetim
04:04 Daha yeni diller ve derleyici
04:33 Bellekte güvenli, ama yine de yanlış
05:04 Bir testin kanıtlayabildiği ve kanıtlayamadığı
05:29 Programları kanıtlayan bir program?
06:33 seL4: doğruluğu kanıtlandı, bir bedelle
07:15 Bir hata yazmana gerek yok
07:51 Daha iyi araçlar, daha çok açık
08:33 Daha iyi soru
08:50 Sistem belleği bugün nasıl koruyor
09:23 Hatalar kaçınılmazsa
10:00 "Hâlâ çalışıyor" ile "hâlâ güvenli"

GÖRSEL KAYNAKLARI
Edsger W. Dijkstra — Hamilton Richards, CC BY-SA 3.0
via Wikimedia Commons
Lisans: creativecommons.org/licenses/by-sa/3.0/

Alan Turing'in fotoğrafı kamu malıdır.
```

## українська (`uk`)

```
Чому програми досі повні помилок?
```

```
Кожні кілька днів у новинах з'являється чергова серйозна вада — така, що
зливає приватні дані або віддає комп'ютер зловмиснику. І реакція майже
завжди однакова: це ж професіонали, у них є рев'ю коду, тести й аудити. То
як помилки все одно з'являються?

Це відео про те чому, і відповідь не «погані програмісти». Це стіна,
вбудована в математику. Програма лише зі ста налаштуваннями «увімкнено-або-
вимкнено» вже має більше комбінацій, ніж ви могли б колись перевірити —
більше, ніж якби ви почали перевіряти мільярд щосекунди від Великого вибуху.
У справжніх програмах їх мільйони. «Просто перевір усе» не дорого. Це
неможливо.

Далі стає лише глибше: вади пам'яті, що дають зловмисникам виконувати
власний код; те, що жодна програма не може перевірити кожну іншу (Алан
Тюрінг довів це 1936 року, Генрі Райс пішов далі 1953-го); і заковика, що
навіть повне математичне доведення показує лише, що код відповідає
специфікації — а специфікацію пишуть люди.

Тож, можливо, «як писати програми без помилок?» — хибне запитання. Краще:
як будувати системи, що лишаються безпечними, навіть коли в програмі є вади?

Субтитри написані для цього відео, а не згенеровані автоматично. Другою
аудіодоріжкою доступна американська англійська.

Повний текст, джерела та переклади: https://theresmoretoit-channel.github.io/uk/videos/why-is-software-still-so-full-of-bugs/

РОЗДІЛИ
00:00 Знову вада в новинах
00:44 Сто перемикачів, і 2^100
01:27 Найпростіше, що робить програма
02:34 C і контроль над пам'яттю
04:04 Новіші мови й компілятор
04:33 Безпечна щодо пам'яті, і все одно хибна
05:04 Що тест може довести, а що ні
05:29 Програма, що доводить програми?
06:33 seL4: доведено правильність, дорогою ціною
07:15 Не треба писати ваду
07:51 Кращі інструменти, більше вразливостей
08:33 Краще запитання
08:50 Як система оберігає пам'ять сьогодні
09:23 Якщо вади неминучі
10:00 «Воно працює» проти «воно безпечне»

ДЖЕРЕЛА ЗОБРАЖЕНЬ
Edsger W. Dijkstra — Hamilton Richards, CC BY-SA 3.0
via Wikimedia Commons
Ліцензія: creativecommons.org/licenses/by-sa/3.0/

Фотографія Алана Тюрінга є суспільним надбанням.
```

## Tiếng Việt (`vi`)

```
Vì sao phần mềm vẫn đầy lỗi?
```

```
Cứ vài ngày, lại một lỗi nghiêm trọng nữa lên tin tức — một lỗi làm rò rỉ dữ
liệu riêng tư, hoặc trao một chiếc máy tính cho kẻ tấn công. Và phản ứng hầu
như luôn giống nhau: họ là những người chuyên nghiệp, có rà soát mã, kiểm thử
và kiểm toán. Vậy sao lỗi vẫn cứ xuất hiện?

Video này nói về lý do, và câu trả lời không phải "lập trình viên kém". Đó là
một bức tường được xây ngay trong toán học. Một chương trình chỉ với một trăm
tùy chọn bật-hoặc-tắt đã có nhiều tổ hợp hơn số bạn có thể thử — nhiều hơn cả
khi bạn bắt đầu kiểm tra một tỷ tổ hợp mỗi giây từ vụ Big Bang. Chương trình
thật có hàng triệu công tắc. "Cứ thử hết đi" không phải là tốn kém. Mà là bất
khả thi.

Từ đó nó chỉ càng sâu hơn: những lỗi bộ nhớ cho phép kẻ tấn công chạy mã của
chính hắn, sự thật rằng không chương trình nào có thể kiểm tra mọi chương
trình khác (Alan Turing chứng minh năm 1936, Henry Rice đi xa hơn năm 1953),
và điểm gợn rằng ngay cả một chứng minh toán học đầy đủ cũng chỉ cho thấy mã
khớp với một đặc tả — và đặc tả là do con người viết.

Vậy nên có lẽ "làm sao viết phần mềm không lỗi?" là câu hỏi sai. Câu hay hơn
là: làm sao dựng những hệ thống vẫn an toàn ngay cả khi phần mềm có lỗi?

Phụ đề được viết cho video này, không phải tạo tự động. Có một bản âm thanh
tiếng Anh Mỹ ở dạng bản âm thanh thứ hai.

Toàn văn, nguồn và bản dịch: https://theresmoretoit-channel.github.io/vi/videos/why-is-software-still-so-full-of-bugs/

CHƯƠNG
00:00 Lại một lỗi lên tin tức
00:44 Một trăm công tắc, và 2^100
01:27 Việc đơn giản nhất một chương trình làm
02:34 C và quyền kiểm soát bộ nhớ
04:04 Các ngôn ngữ mới hơn và trình biên dịch
04:33 An toàn bộ nhớ, mà vẫn sai
05:04 Một bài kiểm thử chứng minh được gì và không
05:29 Một chương trình chứng minh các chương trình?
06:33 seL4: được chứng minh đúng, với cái giá đắt
07:15 Bạn không cần phải viết ra một lỗi
07:51 Công cụ tốt hơn, lỗ hổng nhiều hơn
08:33 Câu hỏi hay hơn
08:50 Hệ thống canh giữ bộ nhớ ngày nay ra sao
09:23 Nếu lỗi là không tránh khỏi
10:00 "Vẫn chạy" so với "vẫn an toàn"

NGUỒN HÌNH ẢNH
Edsger W. Dijkstra — Hamilton Richards, CC BY-SA 3.0
via Wikimedia Commons
Giấy phép: creativecommons.org/licenses/by-sa/3.0/

Ảnh của Alan Turing thuộc phạm vi công cộng.
```

## čeština (`cs`)

```
Proč je software pořád plný chyb?
```

```
Každých pár dní se v novinách objeví další vážná chyba — taková, co zlije
soukromá data nebo předá počítač útočníkovi. A reakce je skoro vždycky
stejná: vždyť to jsou profesionálové, mají revize kódu, testy a audity. Jak
to, že chyby pořád přicházejí?

Tohle video je o tom proč, a odpověď není „špatní programátoři". Je to zeď
zabudovaná do matematiky. Program s pouhými sto přepínači zapnuto-nebo-vypnuto
má už víc kombinací, než byste kdy stihli otestovat — víc, než kdybyste
začali kontrolovat miliardu za sekundu při Velkém třesku. Skutečné programy
jich mají miliony. „Prostě otestuj všechno" není drahé. Je to nemožné.

Odtud se to jen prohlubuje: chyby v paměti, díky nimž útočník spustí vlastní
kód; fakt, že žádný program neumí prověřit každý jiný (Alan Turing to dokázal
roku 1936, Henry Rice šel roku 1953 dál); a háček, že i úplný matematický
důkaz ukáže jen to, že se kód shoduje se specifikací — a specifikaci píšou
lidé.

Takže možná „jak psát software bez chyb?" je špatná otázka. Lepší zní: jak
stavět systémy, které zůstanou bezpečné, i když v softwaru chyby jsou?

Titulky jsou k tomuhle videu napsané, ne strojově vygenerované. Jako druhá
zvuková stopa je k dispozici americká angličtina.

Celý text, zdroje a překlady: https://theresmoretoit-channel.github.io/cs/videos/why-is-software-still-so-full-of-bugs/

KAPITOLY
00:00 Zase chyba ve zprávách
00:44 Sto přepínačů a 2^100
01:27 Nejjednodušší věc, kterou program dělá
02:34 Céčko a kontrola nad pamětí
04:04 Novější jazyky a překladač
04:33 Paměťově bezpečné, a přesto špatné
05:04 Co test dokáže a co ne
05:29 Program, který dokazuje programy?
06:33 seL4: dokázaná správnost, za jakou cenu
07:15 Chybu nemusíte napsat
07:51 Lepší nástroje, víc zranitelností
08:33 Lepší otázka
08:50 Jak systém dnes hlídá paměť
09:23 Když jsou chyby nevyhnutelné
10:00 „Funguje to" proti „je to bezpečné"

ZDROJE OBRÁZKŮ
Edsger W. Dijkstra — Hamilton Richards, CC BY-SA 3.0
via Wikimedia Commons
Licence: creativecommons.org/licenses/by-sa/3.0/

Fotografie Alana Turinga je volné dílo.
```

## español (`es`)

```
¿Por qué el software sigue lleno de errores?
```

```
Cada pocos días, otro error grave aparece en las noticias — uno que filtra
datos privados o entrega un ordenador a un atacante. Y la reacción es casi
siempre la misma: son profesionales, tienen revisiones de código, pruebas y
auditorías. Entonces, ¿cómo siguen apareciendo los errores?

Este vídeo trata del porqué, y la respuesta no es "malos programadores". Es
un muro inscrito en las matemáticas. Un programa con apenas cien ajustes de
encendido o apagado ya tiene más combinaciones de las que podrías probar
jamás — más que si hubieras empezado a comprobar mil millones por segundo en
el Big Bang. Los programas de verdad tienen millones de interruptores.
"Basta con probarlo todo" no es caro. Es imposible.

A partir de ahí solo se hace más profundo: errores de memoria que dejan a los
atacantes ejecutar su propio código, el hecho de que ningún programa puede
comprobar todos los demás (Alan Turing lo demostró en 1936, Henry Rice fue
más allá en 1953), y la trampa de que incluso una demostración matemática
completa solo muestra que el código coincide con una especificación — y la
especificación la escriben personas.

Así que quizá "¿cómo escribimos software sin errores?" sea la pregunta
equivocada. La mejor es: ¿cómo construimos sistemas que sigan seguros incluso
cuando el software tiene errores?

Los subtítulos están escritos para este vídeo, no generados automáticamente.
Hay una pista de audio en inglés americano como segunda pista.

Transcripción completa, fuentes y traducciones: https://theresmoretoit-channel.github.io/es/videos/why-is-software-still-so-full-of-bugs/

CAPÍTULOS
00:00 Otro error en las noticias
00:44 Cien interruptores, y 2^100
01:27 Lo más simple que hace un programa
02:34 El C y el control sobre la memoria
04:04 Los lenguajes más nuevos y el compilador
04:33 Seguro en memoria, y aun así equivocado
05:04 Lo que una prueba puede y no puede demostrar
05:29 ¿Un programa que demuestra programas?
06:33 seL4: demostrado correcto, a un precio
07:15 No hace falta escribir un error
07:51 Mejores herramientas, más vulnerabilidades
08:33 La pregunta mejor
08:50 Cómo protege la memoria el sistema hoy
09:23 Si los errores son inevitables
10:00 "Funciona" frente a "es seguro"

CRÉDITOS DE IMÁGENES
Edsger W. Dijkstra — Hamilton Richards, CC BY-SA 3.0
via Wikimedia Commons
Licencia: creativecommons.org/licenses/by-sa/3.0/

La fotografía de Alan Turing es de dominio público.
```

## svenska (`sv`)

```
Varför är mjukvara fortfarande full av buggar?
```

```
Med några dagars mellanrum dyker en ny allvarlig bugg upp i nyheterna — en
som läcker privata data eller ger en angripare en dator. Och reaktionen är
nästan alltid densamma: det här är proffs, med kodgranskningar, tester och
revisioner. Så hur kan buggarna fortsätta komma?

Den här videon handlar om varför, och svaret är inte "dåliga programmerare".
Det är en mur inbyggd i matematiken. Ett program med bara hundra av-eller-på-
inställningar har redan fler kombinationer än du någonsin skulle hinna testa
— fler än om du börjat kontrollera en miljard i sekunden vid Big Bang.
Riktiga program har miljoner brytare. "Testa bara allt" är inte dyrt. Det är
omöjligt.

Därifrån blir det bara djupare: minnesbuggar som låter angripare köra sin
egen kod, det faktum att inget program kan kontrollera varje annat program
(Alan Turing bevisade det 1936, Henry Rice gick längre 1953), och haken att
även ett fullständigt matematiskt bevis bara visar att koden matchar en
specifikation — och specifikationen skrivs av människor.

Så kanske "hur skriver vi mjukvara utan buggar?" är fel fråga. Den bättre är:
hur bygger vi system som förblir säkra även när mjukvaran har buggar?

Undertexterna är skrivna för den här videon, inte automatgenererade. Ett
amerikansk-engelskt ljudspår finns som andra ljudspår.

Hela texten, källor och översättningar: https://theresmoretoit-channel.github.io/sv/videos/why-is-software-still-so-full-of-bugs/

KAPITEL
00:00 Ännu en bugg i nyheterna
00:44 Hundra brytare, och 2^100
01:27 Det enklaste ett program gör
02:34 C och kontrollen över minnet
04:04 Nyare språk och kompilatorn
04:33 Minnessäkert, och ändå fel
05:04 Vad ett test kan och inte kan bevisa
05:29 Ett program som bevisar program?
06:33 seL4: bevisat korrekt, till ett pris
07:15 Du behöver inte skriva en bugg
07:51 Bättre verktyg, fler sårbarheter
08:33 Den bättre frågan
08:50 Hur systemet vaktar minnet idag
09:23 Om buggar är oundvikliga
10:00 "Det funkar" mot "det är säkert"

BILDKÄLLOR
Edsger W. Dijkstra — Hamilton Richards, CC BY-SA 3.0
via Wikimedia Commons
Licens: creativecommons.org/licenses/by-sa/3.0/

Fotografiet av Alan Turing är allmän egendom.
```
