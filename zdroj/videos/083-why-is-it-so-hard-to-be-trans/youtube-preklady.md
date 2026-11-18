# YouTube — lokalizace 083 „Why Is It So Hard to Be Trans?"

Třináct překladů titulu a bloku „Popis" z `youtube.md` (anglický snippet se
posílá beze změny). Čte `tools/lokalizace.py`; formát a pořadí sekcí podle
`docs/zverejneni.md`.

## Co se NEPŘEKLÁDÁ

- **vlastní jména a termíny, které scénáře nechávají v originále** —
  *passing* (kromě pt-BR „passabilidade" a uk «пасинг», jako ve scénářích),
- **časy kapitol** (na vteřinu podle `work/timing.json` draftu 4, celkem
  781,2 s, kapitolové desky S11, S22, S34, S47, S59, S70, S80) — po každém
  dalším běhu `tts.py` je přepočítej tady i v `youtube.md`,
- **tagy** — YouTube je per jazyk nemá,
- **odstavec o titulcích a americké stopě** se nepřekládá znovu, je doslova
  z tabulky v `docs/zverejneni.md` („Popis NEJMENUJE počet jazyků titulků").

Video nemá archivní snímek, takže sekce ZDROJE OBRÁZKŮ odpadá (jako
v anglickém `youtube.md`).

Titul je první řádek `# …` přeloženého `script.<kód>.md`. Názvy kapitol
jsou mluvené kapitolové desky z přeložených scénářů (S11, S22, S34, S47,
S59, S70, S80), bez koncové tečky jako v anglickém `youtube.md`; kapitola
00:00 („The first thing people notice") desku nemá a je přeložená.
Sérijní odstavec jmenuje 080 a 081 jako v `082-*/youtube-preklady.md`
(080 se „zdá se" jako anglické „seem to be"), 082 nepřímou otázkou podle
jeho lokalizovaného titulu, poslední díl (084) podle S91 přeloženého
scénáře 083.

Terminologie podle `script.<kód>.md` téhož videa (cs „obtěžování",
„odmítnutí", „zdravotní péče", „průzkum"; de „Belästigung", „Ablehnung",
„Umfrage"; pl „nękanie", „odrzucenie"; uk «цькування», «неприйняття»;
tr „taciz", „reddedilme"; id „pelecehan", „penolakan"; fi „häirintä",
„torjunta"; vi „quấy rối", „chối bỏ"; fr „harcèlement", „rejet";
it „molestie", „rifiuto"; es „acoso", „rechazo"; pt-BR „assédio",
„rejeição"; sv „trakasserier", „bli avvisad").

Popis drží míru jistoty originálu: průzkum jen jmenuje, čísla neuvádí;
passing „není důkaz" identity, ne „nic neznamená".

Registr: tyká se tam, kde jazyk volí (cs, de du, pl, uk ти, tr sen,
id kamu, fr tu, es tú, it tu, pt-BR você, sv du), fi „sinä", vi „bạn" —
jako ve scénářích 083 a v 080–082. Rod se vůči divákovi nedoplňuje
(„kdo jsi", uk «хто ти є», pl „kim jesteś").

## suomi (`fi`)

```
Miksi on niin vaikeaa olla trans?
```

```
Ennen kuin sanot sanaakaan, ihmiset ovat jo päättäneet, oletko mies vai nainen. Useimmiten kukaan ei edes huomaa sen tapahtuvan. Mutta mitä tapahtuu, kun se, miten ihmiset sinut näkevät, ei vastaa sitä, kuka olet?

Tämä video käsittelee sitä, millaista on olla transihminen maailmassa, jossa ihmisiä arvioidaan ulkonäön perusteella. Mitä passing tarkoittaa ja miksi se ei todista kenenkään identiteettiä. Kuka päättää, miltä miehen tai naisen pitäisi näyttää. Miten häirintä ja jo pelkkä sen mahdollisuus vaikuttavat tavallisiin päätöksiin, ja mitä Yhdysvaltain laajin transihmisille tehty kysely sai selville. Miten torjunta perheessä, työssä tai terveydenhuollossa voi tehdä arjesta raskaampaa. Miksi niin monet julkiset kysymykset transihmisistä koskevat heidän kehoaan. Ja miksi tieto siitä, että olet trans, ei automaattisesti kuulu kaikille, jotka tapaavat sinut.

Tämä on neljäs video transihmisiä käsittelevässä sarjassa. Aiemmissa videoissa kysyttiin, miksi transihmisiä näyttää yhtäkkiä olevan niin paljon, mistä tiedät, että olet trans, ja miksi transihmiset muuttavat kehoaan. Viimeinen kysyy: milloin yhteiskunnasta tulee ongelma?

Tekstitykset on kirjoitettu tätä videota varten, ei luotu automaattisesti. Toisena ääniraitana on amerikanenglanti.

Koko teksti, lähteet ja käännökset: https://theresmoretoit-channel.github.io/fi/videos/why-is-it-so-hard-to-be-trans/

LUVUT
00:00 Ensimmäinen asia, jonka ihmiset huomaavat
01:21 Mitä passing oikeastaan tarkoittaa?
02:57 Kuka päättää, miltä miehen tai naisen pitäisi näyttää?
04:58 Kun erilaisuudella on hintansa
07:00 Perhe, työ ja arki
08:43 Miksi kaikki transihmisiin liittyvä seksualisoidaan?
10:17 Oikeus yksityisyyteen
11:41 Miltä hyväksyntä oikeastaan näyttäisi?
```

## français (`fr`)

```
Pourquoi est-ce si difficile d'être trans ?
```

```
Avant même que tu dises un mot, les gens ont déjà décidé si tu es un homme ou une femme. La plupart du temps, personne ne remarque que ça se produit. Mais que se passe-t-il quand la façon dont les gens te voient ne correspond pas à qui tu es ?

Cette vidéo raconte ce que signifie être transgenre dans un monde qui juge sur les apparences. Ce que veut dire le passing, et pourquoi il ne prouve rien sur l'identité de qui que ce soit. Qui décide à quoi un homme ou une femme doit ressembler. Comment le harcèlement, et la seule possibilité d'en subir, influence les décisions du quotidien, et ce qu'a constaté la plus grande enquête auprès des personnes trans aux États-Unis. Comment le rejet, dans la famille, au travail ou dans les soins médicaux, peut rendre la vie quotidienne plus difficile. Pourquoi tant de questions posées publiquement au sujet des personnes trans portent sur leur corps. Et pourquoi le fait que tu sois transgenre n'est pas une information que tous ceux qui te rencontrent ont automatiquement le droit de connaître.

C'est la quatrième vidéo d'une série sur les personnes transgenres. Les précédentes se demandaient pourquoi il semble soudain y avoir autant de personnes trans, comment savoir qu'on est trans, et pourquoi les personnes trans changent leur corps. La dernière pose la question : quand la société devient-elle le problème ?

Les sous-titres sont écrits pour cette vidéo, pas générés automatiquement. Une piste audio en anglais américain est disponible en seconde piste.

Transcription complète, sources et traductions : https://theresmoretoit-channel.github.io/fr/videos/why-is-it-so-hard-to-be-trans/

CHAPITRES
00:00 La première chose que les gens remarquent
01:21 Que veut vraiment dire le passing ?
02:57 Qui décide à quoi un homme ou une femme doit ressembler ?
04:58 Quand être différent a un prix
07:00 La famille, le travail et la vie quotidienne
08:43 Pourquoi tout ce qui touche aux personnes trans est-il si sexualisé ?
10:17 Le droit à la vie privée
11:41 À quoi ressemblerait vraiment l'acceptation ?
```

## Bahasa Indonesia (`id`)

```
Kenapa Begitu Sulit Menjadi Trans?
```

```
Sebelum kamu mengucapkan sepatah kata pun, orang-orang sudah memutuskan apakah kamu laki-laki atau perempuan. Biasanya, tidak ada yang menyadari hal itu terjadi. Tapi apa yang terjadi kalau cara orang melihatmu tidak sesuai dengan dirimu yang sebenarnya?

Video ini membahas seperti apa rasanya menjadi transgender di dunia yang menilai orang berdasarkan penampilan. Apa arti passing, dan kenapa passing bukan bukti identitas siapa pun. Siapa yang menentukan seperti apa seharusnya penampilan laki-laki atau perempuan. Bagaimana pelecehan, dan kemungkinan mengalaminya, memengaruhi keputusan sehari-hari, serta apa temuan survei terbesar terhadap orang trans di Amerika Serikat. Bagaimana penolakan dari keluarga, di tempat kerja, atau di layanan kesehatan bisa membuat kehidupan sehari-hari lebih berat. Kenapa begitu banyak pertanyaan yang diajukan di ruang publik tentang orang trans menyangkut tubuh mereka. Dan kenapa informasi bahwa kamu transgender bukanlah sesuatu yang otomatis berhak diketahui semua orang yang bertemu denganmu.

Ini adalah video keempat dalam seri tentang orang transgender. Video-video sebelumnya bertanya kenapa tiba-tiba sepertinya ada begitu banyak orang trans, bagaimana kamu tahu kalau kamu trans, dan kenapa orang trans mengubah tubuh mereka. Video terakhir bertanya: kapan masyarakat menjadi masalahnya?

Subtitel ditulis khusus untuk video ini, bukan dibuat secara otomatis. Tersedia juga trek audio kedua dalam bahasa Inggris Amerika.

Transkrip lengkap, sumber, dan terjemahan: https://theresmoretoit-channel.github.io/id/videos/why-is-it-so-hard-to-be-trans/

BAB
00:00 Hal pertama yang diperhatikan orang
01:21 Apa sebenarnya arti passing?
02:57 Siapa yang menentukan seperti apa seharusnya penampilan laki-laki atau perempuan?
04:58 Ketika ada harga yang harus dibayar karena berbeda
07:00 Keluarga, pekerjaan, dan kehidupan sehari-hari
08:43 Kenapa segala hal tentang orang trans begitu diseksualisasi?
10:17 Hak atas privasi
11:41 Seperti apa sebenarnya penerimaan itu?
```

## italiano (`it`)

```
Perché è così difficile essere trans?
```

```
Prima ancora che tu dica una parola, le persone hanno già deciso se sei un uomo o una donna. Il più delle volte nessuno si accorge che sta succedendo. Ma che cosa succede quando il modo in cui gli altri ti vedono non corrisponde a chi sei?

Questo video racconta che cosa vuol dire essere transgender in un mondo che giudica in base all'apparenza. Che cosa significa il passing, e perché non è la prova dell'identità di nessuno. Chi decide che aspetto dovrebbe avere un uomo o una donna. Come le molestie, e anche solo la possibilità di subirle, influenzano le decisioni di tutti i giorni, e che cosa ha rilevato la più grande indagine sulle persone trans negli Stati Uniti. Come il rifiuto in famiglia, sul lavoro o nell'assistenza sanitaria può rendere più difficile la vita quotidiana. Perché così tante domande poste pubblicamente sulle persone trans riguardano il loro corpo. E perché il fatto che tu sia transgender non è un'informazione che chiunque ti incontri abbia automaticamente il diritto di conoscere.

Questo è il quarto video di una serie sulle persone transgender. I precedenti si chiedevano perché all'improvviso sembrino esserci così tante persone trans, come fai a sapere di essere trans e perché le persone trans cambiano il proprio corpo. L'ultimo si chiede: quando è la società a diventare il problema?

I sottotitoli sono scritti per questo video, non generati automaticamente. Come seconda traccia audio è disponibile l’inglese americano.

Trascrizione completa, fonti e traduzioni: https://theresmoretoit-channel.github.io/it/videos/why-is-it-so-hard-to-be-trans/

CAPITOLI
00:00 La prima cosa che la gente nota
01:21 Che cosa significa davvero il passing?
02:57 Chi decide che aspetto dovrebbe avere un uomo o una donna?
04:58 Quando essere diversi ha un prezzo
07:00 Famiglia, lavoro e vita quotidiana
08:43 Perché tutto ciò che riguarda le persone trans è così sessualizzato?
10:17 Il diritto alla privacy
11:41 Come sarebbe, davvero, l'accettazione?
```

## Deutsch (`de`)

```
Warum ist es so schwer, trans zu sein?
```

```
Noch bevor du ein Wort sagst, haben die Leute schon entschieden, ob du ein Mann oder eine Frau bist. Meistens bemerkt das niemand. Aber was passiert, wenn das Bild, das andere von dir haben, nicht zu dem passt, wer du bist?

Dieses Video zeigt, wie es ist, trans zu sein in einer Welt, die Menschen nach ihrem Äußeren beurteilt. Was Passing bedeutet und warum es nichts über die Identität eines Menschen beweist. Wer entscheidet, wie ein Mann oder eine Frau aussehen sollte. Wie Belästigung und schon die Möglichkeit von Belästigung Alltagsentscheidungen prägen und was die größte Umfrage unter trans Menschen in den USA ergeben hat. Wie Ablehnung in der Familie, im Job oder im Gesundheitswesen den Alltag schwerer machen kann. Warum sich so viele Fragen, die öffentlich über trans Menschen gestellt werden, um deren Körper drehen. Und warum nicht jeder, der dir begegnet, automatisch ein Recht darauf hat, zu erfahren, dass du trans bist.

Das ist das vierte Video einer Reihe über trans Menschen. Die bisherigen fragten, warum es plötzlich so viele trans Menschen zu geben scheint, woher du weißt, dass du trans bist, und warum trans Menschen ihren Körper verändern. Das letzte fragt: Wann wird die Gesellschaft zum Problem?

Die Untertitel wurden für dieses Video geschrieben, nicht automatisch erzeugt. Als zweite Tonspur steht amerikanisches Englisch bereit.

Vollständiger Text, Quellen und Übersetzungen: https://theresmoretoit-channel.github.io/de/videos/why-is-it-so-hard-to-be-trans/

KAPITEL
00:00 Das Erste, was anderen auffällt
01:21 Was bedeutet Passing eigentlich?
02:57 Wer entscheidet, wie ein Mann oder eine Frau aussehen sollte?
04:58 Wenn Anderssein einen Preis hat
07:00 Familie, Arbeit und Alltag
08:43 Warum wird bei trans Menschen alles so sexualisiert?
10:17 Das Recht auf Privatsphäre
11:41 Wie würde Akzeptanz eigentlich aussehen?
```

## polski (`pl`)

```
Dlaczego tak trudno jest być trans?
```

```
Zanim powiesz choć słowo, ludzie już zdecydowali, czy jesteś mężczyzną, czy kobietą. Zwykle nikt nawet nie zauważa, że to się dzieje. Ale co wtedy, kiedy to, jak widzą cię inni, nie zgadza się z tym, kim jesteś?

Ten film pokazuje, jak to jest być osobą transpłciową w świecie, który ocenia ludzi po wyglądzie. Co oznacza passing i dlaczego nie jest dowodem niczyjej tożsamości. Kto decyduje, jak powinien wyglądać mężczyzna albo kobieta. Jak nękanie, a nawet sama jego możliwość, wpływa na codzienne decyzje i co wykazało największe badanie osób transpłciowych w Stanach Zjednoczonych. Jak odrzucenie w rodzinie, w pracy czy w placówkach opieki zdrowotnej może utrudniać codzienne życie. Dlaczego tak wiele pytań zadawanych publicznie o osoby trans dotyczy ich ciał. I dlaczego bycie osobą trans nie jest informacją, która automatycznie należy się każdemu, kto cię spotka.

To czwarty film z serii o osobach transpłciowych. Poprzednie pytały, dlaczego nagle wydaje się, że jest tyle osób trans, skąd wiesz, że jesteś trans, i dlaczego osoby trans zmieniają swoje ciała. Ostatni pyta: kiedy to społeczeństwo staje się problemem?

Napisy są pisane do tego filmu, nie generowane automatycznie. Jako druga ścieżka dźwiękowa dostępny jest angielski amerykański.

Pełna transkrypcja, źródła i tłumaczenia: https://theresmoretoit-channel.github.io/pl/videos/why-is-it-so-hard-to-be-trans/

ROZDZIAŁY
00:00 Pierwsze, co zauważają ludzie
01:21 Co właściwie oznacza passing?
02:57 Kto decyduje, jak powinien wyglądać mężczyzna albo kobieta?
04:58 Kiedy bycie innym ma swoją cenę
07:00 Rodzina, praca i codzienne życie
08:43 Dlaczego wszystko, co dotyczy osób trans, jest tak bardzo seksualizowane?
10:17 Prawo do prywatności
11:41 Jak właściwie wyglądałaby akceptacja?
```

## português (Brasil) (`pt-BR`)

```
Por que é tão difícil ser trans?
```

```
Antes de você dizer uma palavra, as pessoas já decidiram se você é homem ou mulher. Na maior parte das vezes, ninguém percebe que isso está acontecendo. Mas o que acontece quando o jeito como as pessoas veem você não corresponde a quem você é?

Este vídeo mostra como é ser transgênero num mundo que julga as pessoas pela aparência. O que é passabilidade, e por que ela não é prova da identidade de ninguém. Quem decide qual deve ser a aparência de um homem ou de uma mulher. Como o assédio, e a simples possibilidade dele, molda decisões do dia a dia, e o que descobriu a maior pesquisa com pessoas trans nos Estados Unidos. Como a rejeição na família, no trabalho ou no atendimento de saúde pode tornar o dia a dia mais difícil. Por que tantas perguntas feitas publicamente sobre pessoas trans dizem respeito ao corpo delas. E por que o fato de você ser transgênero não é uma informação que qualquer pessoa que você encontre tenha automaticamente o direito de saber.

Este é o quarto vídeo de uma série sobre pessoas transgênero. Os anteriores perguntavam por que de repente parece haver tantas pessoas trans, como você sabe que é trans e por que pessoas trans mudam o próprio corpo. O último pergunta: quando a sociedade passa a ser o problema?

As legendas foram escritas para este vídeo, não geradas automaticamente. Como segunda faixa de áudio está disponível o inglês americano.

Transcrição completa, fontes e traduções: https://theresmoretoit-channel.github.io/pt-br/videos/why-is-it-so-hard-to-be-trans/

CAPÍTULOS
00:00 A primeira coisa que as pessoas notam
01:21 O que a passabilidade significa de verdade?
02:57 Quem decide qual deve ser a aparência de um homem ou de uma mulher?
04:58 Quando ser diferente tem um custo
07:00 Família, trabalho e vida cotidiana
08:43 Por que tudo sobre pessoas trans é tão sexualizado?
10:17 O direito à privacidade
11:41 Como seria, de fato, a aceitação?
```

## Türkçe (`tr`)

```
Trans Olmak Neden Bu Kadar Zor?
```

```
Daha tek kelime etmeden, insanlar senin erkek mi kadın mı olduğuna çoktan karar vermiştir. Çoğu zaman kimse bunun olduğunu fark etmez bile. Peki insanların seni görme biçimi, senin kim olduğunla örtüşmediğinde ne olur?

Bu video, insanları dış görünüşlerine göre yargılayan bir dünyada transgender olmanın nasıl bir şey olduğunu ele alıyor. Passing ne demek ve neden kimsenin kimliğinin kanıtı değil? Bir erkeğin ya da kadının nasıl görünmesi gerektiğine kim karar veriyor? Taciz ve tacize uğrama ihtimali gündelik kararları nasıl şekillendiriyor ve Amerika Birleşik Devletleri'nde trans insanlarla yapılan en büyük anket neler ortaya koydu? Aileden, iş yerinden ya da sağlık hizmetlerinden gelen reddedilme gündelik hayatı nasıl zorlaştırabilir? Trans insanlar hakkında kamuoyunda sorulan bu kadar çok soru neden onların bedenleriyle ilgili? Ve neden seninle tanışan herkesin trans olduğunu bilmeye otomatik olarak hakkı yok?

Bu, transgender insanlar hakkındaki bir serinin dördüncü videosu. Öncekiler, neden birdenbire bu kadar çok trans insan varmış gibi göründüğünü, trans olduğunu nasıl anlayacağını ve trans insanların bedenlerini neden değiştirdiğini soruyordu. Sonuncusu şunu soruyor: Toplum ne zaman sorunun kendisi hâline gelir?

Altyazılar bu video için yazıldı, otomatik olarak oluşturulmadı. İkinci ses parçası olarak Amerikan İngilizcesi de mevcut.

Metnin tamamı, kaynaklar ve çeviriler: https://theresmoretoit-channel.github.io/tr/videos/why-is-it-so-hard-to-be-trans/

BÖLÜMLER
00:00 İnsanların ilk fark ettiği şey
01:21 Passing aslında ne demek?
02:57 Bir erkeğin ya da kadının nasıl görünmesi gerektiğine kim karar veriyor?
04:58 Farklı olmanın bir bedeli olduğunda
07:00 Aile, iş ve gündelik hayat
08:43 Trans insanlarla ilgili her şey neden bu kadar cinselleştiriliyor?
10:17 Mahremiyet hakkı
11:41 Kabul aslında nasıl bir şey olurdu?
```

## українська (`uk`)

```
Чому так важко бути транс?
```

```
Ще до того, як ти скажеш хоч слово, люди вже вирішили, чоловік ти чи жінка. Здебільшого ніхто навіть не помічає, що це відбувається. Але що буває, коли те, як тебе бачать інші, не збігається з тим, хто ти є?

Це відео про те, як це — бути трансгендерною людиною у світі, де людей оцінюють за зовнішністю. Що означає пасинг і чому він не доводить нічиєї ідентичності. Хто вирішує, як має виглядати чоловік чи жінка. Як цькування і навіть сама його ймовірність впливають на повсякденні рішення і що виявило найбільше опитування трансгендерних людей у Сполучених Штатах. Як неприйняття з боку родини, на роботі чи у сфері медичної допомоги може ускладнювати повсякденне життя. Чому так багато запитань, які публічно ставлять про трансгендерних людей, стосуються їхніх тіл. І чому інформація про те, що ти трансгендерна людина, не належить автоматично кожному, хто тебе зустрічає.

Це четверте відео із серії про трансгендерних людей. Попередні питали, чому здається, ніби раптом стало так багато трансгендерних людей, як зрозуміти, що ти транс, і чому трансгендерні люди змінюють свої тіла. Останнє питає: коли суспільство стає проблемою?

Субтитри написані для цього відео, а не згенеровані автоматично. Також доступна друга звукова доріжка — американською англійською.

Повний текст, джерела та переклади: https://theresmoretoit-channel.github.io/uk/videos/why-is-it-so-hard-to-be-trans/

РОЗДІЛИ
00:00 Перше, що помічають люди
01:21 Що насправді означає пасинг?
02:57 Хто вирішує, як має виглядати чоловік чи жінка?
04:58 Коли інакшість має ціну
07:00 Сім’я, робота й повсякденне життя
08:43 Чому все, що стосується трансгендерних людей, так сексуалізоване?
10:17 Право на приватність
11:41 Як насправді виглядало б прийняття?
```

## Tiếng Việt (`vi`)

```
Vì sao làm người chuyển giới lại khó khăn đến vậy?
```

```
Trước khi bạn kịp nói một lời, mọi người đã quyết định bạn là đàn ông hay phụ nữ. Thông thường, chẳng ai nhận ra điều đó đang diễn ra. Nhưng điều gì xảy ra khi cách người khác nhìn bạn không khớp với con người thật của bạn?

Video này tìm hiểu trải nghiệm của người chuyển giới trong một thế giới đánh giá con người qua vẻ bề ngoài. Passing nghĩa là gì, và vì sao nó không phải là bằng chứng cho bản dạng của bất kỳ ai. Ai quyết định đàn ông hay phụ nữ phải trông như thế nào. Sự quấy rối, và cả khả năng bị quấy rối, định hình những quyết định thường ngày ra sao, và cuộc khảo sát lớn nhất về người chuyển giới tại Hoa Kỳ đã phát hiện điều gì. Sự chối bỏ từ gia đình, nơi làm việc hay trong chăm sóc sức khỏe có thể khiến cuộc sống hằng ngày khó khăn hơn như thế nào. Vì sao rất nhiều câu hỏi được đặt ra công khai về người chuyển giới lại xoay quanh cơ thể của họ. Và vì sao không phải bất kỳ ai gặp bạn cũng mặc nhiên có quyền biết bạn là người chuyển giới.

Đây là video thứ tư trong loạt video về người chuyển giới. Các video trước đã hỏi vì sao có vẻ như đột nhiên có nhiều người chuyển giới đến vậy, làm sao bạn biết mình là người chuyển giới, và vì sao người chuyển giới thay đổi cơ thể mình. Video cuối cùng hỏi: khi nào xã hội trở thành vấn đề?

Phụ đề được viết riêng cho video này, không phải tạo tự động. Có thể chọn tiếng Anh Mỹ ở bản âm thanh thứ hai.

Toàn văn, nguồn và bản dịch: https://theresmoretoit-channel.github.io/vi/videos/why-is-it-so-hard-to-be-trans/

CHƯƠNG
00:00 Điều đầu tiên mọi người để ý
01:21 Passing thực ra có nghĩa là gì?
02:57 Ai quyết định đàn ông hay phụ nữ phải trông như thế nào?
04:58 Khi khác biệt phải trả giá
07:00 Gia đình, công việc và cuộc sống hằng ngày
08:43 Vì sao mọi thứ về người chuyển giới lại bị tình dục hóa đến thế?
10:17 Quyền riêng tư
11:41 Sự chấp nhận thực sự sẽ trông như thế nào?
```

## čeština (`cs`)

```
Proč je tak těžké být trans?
```

```
Ještě než promluvíš, lidé už mají rozhodnuto, jestli jsi muž, nebo žena. Většinou si nikdo ani nevšimne, že se to děje. Co se ale stane, když to, jak tě lidé vidí, neodpovídá tomu, kdo jsi?

Video ukazuje, jaké je být trans ve světě, který soudí podle vnějšku. Co znamená passing a proč není důkazem ničí identity. Kdo rozhoduje, jak má vypadat muž nebo žena. Jak obtěžování i pouhá možnost, že se s ním setkáš, ovlivňuje běžná rozhodnutí a co zjistil největší průzkum mezi trans lidmi ve Spojených státech. Jak odmítnutí v rodině, v práci nebo ve zdravotní péči může ztížit každodenní život. Proč se tolik otázek, které o trans lidech zaznívají veřejně, týká jejich těla. A proč každý, kdo tě potká, nemá automaticky právo vědět, že jsi trans.

Tohle je čtvrté video ze série o transgender lidech. Ta předchozí se ptala, proč se zdá, že je najednou tolik trans lidí, jak poznáš, že jsi trans, a proč trans lidé mění svá těla. To poslední se ptá: kdy se společnost stává problémem?

Titulky jsou psané pro tohle video, ne strojový přepis. Jako druhá zvuková stopa je k dispozici americká angličtina.

Celý text, zdroje a překlady: https://theresmoretoit-channel.github.io/cs/videos/why-is-it-so-hard-to-be-trans/

KAPITOLY
00:00 První, čeho si lidé všimnou
01:21 Co vlastně znamená passing?
02:57 Kdo rozhoduje, jak má vypadat muž nebo žena?
04:58 Když jinakost něco stojí
07:00 Rodina, práce a každodenní život
08:43 Proč je všechno kolem trans lidí tak sexualizované?
10:17 Právo na soukromí
11:41 Jak by vlastně vypadalo přijetí?
```

## español (`es`)

```
¿Por qué es tan difícil ser trans?
```

```
Antes de que digas una palabra, la gente ya ha decidido si eres un hombre o una mujer. Casi siempre, nadie se da cuenta de que esto ocurre. Pero ¿qué pasa cuando la forma en que te ve la gente no coincide con quién eres?

Este vídeo explora qué significa ser transgénero en un mundo que juzga por las apariencias. Qué es el passing y por qué no demuestra la identidad de nadie. Quién decide qué aspecto debe tener un hombre o una mujer. Cómo el acoso, y la mera posibilidad de sufrirlo, condiciona decisiones cotidianas, y qué encontró la mayor encuesta a personas trans en Estados Unidos. Cómo el rechazo de la familia, en el trabajo o en la atención sanitaria puede hacer más difícil el día a día. Por qué tantas preguntas que se hacen públicamente sobre las personas trans tienen que ver con su cuerpo. Y por qué cualquiera que se cruce contigo no tiene automáticamente derecho a saber que eres trans.

Este es el cuarto vídeo de una serie sobre las personas transgénero. Los anteriores se preguntaban por qué parece que de repente hay tantas personas trans, cómo sabes que eres trans y por qué las personas trans cambian su cuerpo. El último se pregunta: ¿cuándo pasa la sociedad a ser el problema?

Los subtítulos están escritos para este vídeo, no generados automáticamente. Como segunda pista de audio está disponible el inglés americano.

Transcripción completa, fuentes y traducciones: https://theresmoretoit-channel.github.io/es/videos/why-is-it-so-hard-to-be-trans/

CAPÍTULOS
00:00 Lo primero que nota la gente
01:21 ¿Qué significa realmente el passing?
02:57 ¿Quién decide qué aspecto debe tener un hombre o una mujer?
04:58 Cuando ser diferente tiene un precio
07:00 La familia, el trabajo y la vida cotidiana
08:43 ¿Por qué todo lo relacionado con las personas trans está tan sexualizado?
10:17 El derecho a la privacidad
11:41 ¿Cómo sería realmente la aceptación?
```

## svenska (`sv`)

```
Varför är det så svårt att vara trans?
```

```
Innan du har sagt ett ord har folk redan bestämt om du är man eller kvinna. För det mesta märker ingen ens att det händer. Men vad händer när det sätt som andra ser dig på inte stämmer med den du är?

Den här videon handlar om hur det är att vara trans i en värld där människor döms efter sitt utseende. Vad passing betyder och varför det inte bevisar någons identitet. Vem som bestämmer hur en man eller en kvinna ska se ut. Hur trakasserier, och bara risken för dem, påverkar vardagliga beslut, och vad den största undersökningen av transpersoner i USA kom fram till. Hur det kan göra vardagen svårare att bli avvisad av familjen, på jobbet eller inom vården. Varför så många frågor som ställs offentligt om transpersoner handlar om deras kroppar. Och varför inte alla som träffar dig automatiskt har rätt att veta att du är trans.

Det här är den fjärde videon i en serie om transpersoner. De tidigare frågade varför det plötsligt verkar finnas så många transpersoner, hur du vet att du är trans och varför transpersoner förändrar sina kroppar. Den sista frågar: när blir samhället problemet?

Undertexterna är skrivna för den här videon, inte automatgenererade. Som andra ljudspår finns amerikansk engelska.

Hela texten, källor och översättningar: https://theresmoretoit-channel.github.io/sv/videos/why-is-it-so-hard-to-be-trans/

KAPITEL
00:00 Det första folk lägger märke till
01:21 Vad betyder passing egentligen?
02:57 Vem bestämmer hur en man eller en kvinna ska se ut?
04:58 När det kostar att vara annorlunda
07:00 Familj, arbete och vardag
08:43 Varför sexualiseras allt som rör transpersoner?
10:17 Rätten till privatliv
11:41 Hur skulle acceptans egentligen se ut?
```
