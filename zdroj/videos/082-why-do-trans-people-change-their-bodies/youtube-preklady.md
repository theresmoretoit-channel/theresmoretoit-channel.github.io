# YouTube — lokalizace 082 „Why Do Trans People Change Their Bodies?"

Třináct překladů titulu a bloku „Popis" z `youtube.md` (anglický snippet se
posílá beze změny). Čte `tools/lokalizace.py`; formát a pořadí sekcí podle
`docs/zverejneni.md`.

## Co se NEPŘEKLÁDÁ

- **časy kapitol** (na vteřinu podle `work/timing.json` po odstranění
  mluvené výzvy, celkem 668,3 s, scény S01, S14, S19, S31, S48, S59, S72,
  S81) — po každém dalším běhu `tts.py` je přepočítej tady i v `youtube.md`,
- **tagy** — YouTube je per jazyk nemá,
- **odstavec o titulcích a americké stopě** se nepřekládá znovu, je doslova
  stejný jako v `081-*/youtube-preklady.md` (z tabulky v `docs/zverejneni.md`).

Video nemá archivní snímek, takže sekce ZDROJE OBRÁZKŮ odpadá (jako
v anglickém `youtube.md`).

Titul je první řádek `# …` přeloženého `script.<kód>.md`. Názvy kapitol
jsou mluvené nadpisy sekcí z přeložených scénářů (S14, S19, S31, S48, S72,
S81, bez koncové tečky, jako v anglickém `youtube.md`); kapitola 00:00 nese
otázku z S05, kapitola 06:45 je krátký „návrat k otázce" podle S59 téhož
jazyka. První díl (080) je nepřímá otázka **se „zdá se"** jako anglické
„seem to be" — převzato doslova ze sérijního odstavce
`081-*/youtube-preklady.md`. Druhý díl (081) je nepřímá otázka podle jeho
lokalizovaného titulu, další díl (083) je S95 přeloženého scénáře 082.

Terminologie podle `script.<kód>.md` téhož videa (cs „lékařská tranzice",
„hormonální léčba", „genderová dysforie", „rozmar nebo trend"; de
„medizinische Transition", „Hormontherapie", „Geschlechtsdysphorie";
pl „tranzycja medyczna", „dysforia płciowa"; uk «медичний перехід»,
«гендерна дисфорія»; tr „tıbbi geçiş", „cinsiyet disforisi"; id „transisi
medis", „disforia gender"; fi „lääketieteellinen transitio",
„sukupuolidysforia"; vi „chuyển đổi về mặt y tế", „phiền muộn giới" — při
prvním výskytu s anglickým „(gender dysphoria)" v závorce, stejně jako
081 u „detransition", protože vietnamský termín není ustálený). fr drží
scénářové „en décalage" pro „feels wrong".

Popis drží míru jistoty originálu: hormony „can and cannot" (dokáže
a nedokáže), jádro jen jako otázka („struggles to explain" = jen těžko
vysvětlí, ne „nevysvětlí"), žádná čísla komplikací.

Registr: tyká se tam, kde jazyk volí (cs, de du, pl, uk ти, tr sen,
id kamu, fr tu, es tú, it tu, pt-BR você, sv du), fi „sinä", vi „bạn" —
jako ve scénářích 082 a v 081. **Rod se nedoplňuje** vůči divákovi:
„when you don't feel it yourself" je cs „když ji v sobě necítíš" (ne
„sám"), pl a uk „z własnego doświadczenia" / «з власного досвіду» (jako
S48), ne mužské tvary.

## suomi (`fi`)

```
Miksi transihmiset muuttavat kehoaan?
```

```
Kuvittele, että päätät mennä leikkaukseen, ei vamman eikä tutkimuksissa näkyvän sairauden takia, vaan siksi, että jokin omassa kehossasi tuntuu syvästi väärältä. Kuvittele, että käytät lääkkeitä vuosia ja tiedät, että ne muuttavat sinua tavoilla, joita et pysty täysin ennustamaan. Miksi kukaan valitsisi sellaista?

Tämä video käsittelee sitä, mitä lääketieteellinen transitio todella pitää sisällään ja miksi jotkut transihmiset hakeutuvat siihen. Mitä hormonihoito voi muuttaa ja mitä ei. Mitä leikkaus vaatii toipumisen kannalta, millaisia riskejä siihen liittyy ja paljonko se maksaa. Mitä sukupuolidysforia on ja miksi sitä on niin vaikea ymmärtää ulkopuolelta, jos et itse tunne sitä. Miksi ajatus, että kyse on pelkästä päähänpistosta tai trendistä, selittää huonosti, miksi kukaan hyväksyisi kaiken tämän. Ja miksi jotkut transihmiset päättävät olla käymättä läpi lääketieteellistä transitiota lainkaan.

Tämä on kolmas video transihmisiä käsittelevässä sarjassa. Ensimmäinen kysyi, miksi transihmisiä näyttää yhtäkkiä olevan niin paljon, toinen, mistä tiedät, että olet trans. Seuraava kysyy: miksi on niin vaikeaa olla trans?

Tekstitykset on kirjoitettu tätä videota varten, ei luotu automaattisesti. Toisena ääniraitana on amerikanenglanti.

LUVUT
00:00 Miksi kukaan valitsisi sellaista?
01:33 Transitio ei ole yksi asia
01:59 Mitä hormonit oikeastaan tekevät
03:35 Leikkaus: fyysisen muutoksen hinta
05:37 Entä jos et itse tunne sitä?
06:45 Takaisin kysymykseen, josta aloitimme
08:33 Miksi jotkut päättävät olla käymättä läpi lääketieteellistä transitiota
09:35 Kysymys, jota meidän oikeasti pitäisi kysyä
```

## français (`fr`)

```
Pourquoi les personnes trans changent-elles leur corps ?
```

```
Imagine que tu décides de te faire opérer, pas à cause d'une blessure, ni à cause d'une maladie qu'on verrait sur un scanner, mais parce que quelque chose dans ton propre corps te semble profondément en décalage. Imagine prendre un traitement pendant des années, en sachant qu'il va te changer d'une façon que tu ne peux pas entièrement prévoir. Pourquoi est-ce que quelqu'un choisirait ça ?

Cette vidéo explique ce qu'implique vraiment une transition médicale et pourquoi certaines personnes trans s'y engagent. Ce que l'hormonothérapie peut changer, et ce qu'elle ne peut pas changer. Ce que coûte la chirurgie, en convalescence, en risques et en argent. Ce qu'est la dysphorie de genre, et pourquoi elle est si difficile à comprendre de l'extérieur quand tu ne la ressens pas toi-même. Pourquoi l'idée que ce ne serait qu'un caprice ou une mode peine à expliquer que quelqu'un accepte tout cela. Et pourquoi certaines personnes trans choisissent de ne pas faire de transition médicale du tout.

C'est la troisième vidéo d'une série sur les personnes transgenres. La première se demandait pourquoi il semble soudain y avoir autant de personnes trans, la deuxième comment savoir qu'on est trans. La suivante pose la question : pourquoi est-ce si difficile d'être trans ?

Les sous-titres sont écrits pour cette vidéo, pas générés automatiquement. Une piste audio en anglais américain est disponible en seconde piste.

CHAPITRES
00:00 Pourquoi est-ce que quelqu'un choisirait ça ?
01:33 La transition, ce n'est pas une seule chose
01:59 Ce que font vraiment les hormones
03:35 La chirurgie : le prix d'un changement physique
05:37 Et si tu ne le ressens pas toi-même ?
06:45 Retour à la question du début
08:33 Pourquoi certaines personnes choisissent de ne pas faire de transition médicale
09:35 La question qu'on devrait vraiment se poser
```

## Bahasa Indonesia (`id`)

```
Kenapa Orang Trans Mengubah Tubuh Mereka?
```

```
Bayangkan kamu memutuskan untuk menjalani operasi, bukan karena cedera, bukan karena penyakit yang terlihat di hasil pemeriksaan, tapi karena ada sesuatu pada tubuhmu sendiri yang terasa sangat salah. Bayangkan minum obat selama bertahun-tahun, sambil tahu bahwa obat itu akan mengubahmu dengan cara yang tidak bisa kamu prediksi sepenuhnya. Kenapa ada orang yang mau memilih itu?

Video ini membahas apa saja yang sebenarnya dijalani dalam transisi medis dan kenapa sebagian orang trans memilihnya. Apa yang bisa dan tidak bisa diubah oleh terapi hormon. Apa yang harus dijalani selama pemulihan setelah operasi, apa risikonya, dan berapa biayanya. Apa itu disforia gender, dan kenapa begitu sulit dipahami dari luar kalau kamu sendiri tidak merasakannya. Kenapa anggapan bahwa ini cuma keinginan sesaat atau tren sulit menjelaskan kenapa ada orang yang mau menerima semua itu. Dan kenapa sebagian orang trans memilih untuk tidak menjalani transisi medis sama sekali.

Ini adalah video ketiga dalam seri tentang orang transgender. Video pertama bertanya kenapa tiba-tiba sepertinya ada begitu banyak orang trans, video kedua bagaimana kamu tahu kalau kamu trans. Video berikutnya bertanya: kenapa begitu sulit menjadi trans?

Subtitel ditulis khusus untuk video ini, bukan dibuat secara otomatis. Tersedia juga trek audio kedua dalam bahasa Inggris Amerika.

BAB
00:00 Kenapa ada orang yang mau memilih itu?
01:33 Transisi bukan satu hal saja
01:59 Apa yang sebenarnya dilakukan hormon
03:35 Operasi: harga sebuah perubahan fisik
05:37 Bagaimana kalau kamu sendiri tidak merasakannya?
06:45 Kembali ke pertanyaan yang kita ajukan di awal
08:33 Kenapa sebagian orang memilih tidak menjalani transisi medis
09:35 Pertanyaan yang sebenarnya perlu kita ajukan
```

## italiano (`it`)

```
Perché le persone trans cambiano il proprio corpo?
```

```
Immagina di decidere di operarti, non per un infortunio, né per una malattia che si vede in un esame, ma perché qualcosa del tuo corpo ti sembra profondamente sbagliato. Immagina di prendere farmaci per anni, sapendo che ti cambieranno in modi che non puoi prevedere del tutto. Perché qualcuno dovrebbe scegliere una cosa del genere?

Questo video racconta che cosa comporta davvero la transizione medica e perché alcune persone trans la intraprendono. Che cosa la terapia ormonale può cambiare e che cosa no. Quanto costa la chirurgia, in convalescenza, rischi e denaro. Che cos'è la disforia di genere, e perché è così difficile da capire dall'esterno quando tu non la provi. Perché l'idea che sia solo un capriccio o una moda fatica a spiegare perché qualcuno dovrebbe accettare tutto questo. E perché alcune persone trans scelgono di non fare affatto la transizione medica.

Questo è il terzo video di una serie sulle persone transgender. Il primo si chiedeva perché all'improvviso sembrino esserci così tante persone trans, il secondo come fai a sapere di essere trans. Il prossimo si chiede: perché è così difficile essere trans?

I sottotitoli sono scritti per questo video, non generati automaticamente. Come seconda traccia audio è disponibile l’inglese americano.

CAPITOLI
00:00 Perché qualcuno dovrebbe scegliere una cosa del genere?
01:33 La transizione non è una cosa sola
01:59 Che cosa fanno davvero gli ormoni
03:35 La chirurgia: il prezzo di un cambiamento fisico
05:37 E se tu non lo provi?
06:45 Torniamo alla domanda da cui siamo partiti
08:33 Perché alcune persone scelgono di non fare la transizione medica
09:35 La domanda che dovremmo davvero farci
```

## Deutsch (`de`)

```
Warum verändern trans Menschen ihren Körper?
```

```
Stell dir vor, du entscheidest dich für eine Operation, nicht wegen einer Verletzung und nicht wegen einer Krankheit, die man bei einer Untersuchung sieht, sondern weil sich etwas an deinem eigenen Körper zutiefst falsch anfühlt. Stell dir vor, du nimmst jahrelang Medikamente und weißt, dass sie dich auf eine Weise verändern, die du nicht ganz vorhersehen kannst. Warum sollte sich jemand dafür entscheiden?

Dieses Video zeigt, was eine medizinische Transition tatsächlich bedeutet und warum manche trans Menschen diesen Weg gehen. Was eine Hormontherapie verändern kann und was nicht. Was eine Operation bedeutet: welche Erholungsphase nötig ist, welche Risiken sie birgt und wie viel sie kostet. Was Geschlechtsdysphorie ist und warum sie von außen so schwer zu verstehen ist, wenn du sie selbst nicht fühlst. Warum die Vorstellung, es sei nur eine Laune oder ein Trend, kaum erklären kann, warum jemand das alles auf sich nehmen würde. Und warum sich manche trans Menschen ganz gegen eine medizinische Transition entscheiden.

Das ist das dritte Video einer Reihe über trans Menschen. Das erste fragte, warum es plötzlich so viele trans Menschen zu geben scheint, das zweite, woher du weißt, dass du trans bist. Das nächste fragt: Warum ist es so schwer, trans zu sein?

Die Untertitel wurden für dieses Video geschrieben, nicht automatisch erzeugt. Als zweite Tonspur steht amerikanisches Englisch bereit.

KAPITEL
00:00 Warum sollte sich jemand dafür entscheiden?
01:33 Transition ist nicht nur eine Sache
01:59 Was Hormone wirklich bewirken
03:35 Chirurgie: der Preis einer körperlichen Veränderung
05:37 Und wenn du es selbst nicht fühlst?
06:45 Zurück zu der Frage, mit der wir angefangen haben
08:33 Warum sich manche gegen eine medizinische Transition entscheiden
09:35 Die Frage, die wir uns eigentlich stellen sollten
```

## polski (`pl`)

```
Dlaczego osoby trans zmieniają swoje ciała?
```

```
Wyobraź sobie, że decydujesz się na operację – nie z powodu urazu ani choroby, którą pokazałoby badanie, ale dlatego, że coś we własnym ciele odczuwasz jako głęboko niewłaściwe. Wyobraź sobie, że latami bierzesz leki i wiesz, że zmienią cię w sposób, którego nie możesz w pełni przewidzieć. Dlaczego ktoś miałby się na to zdecydować?

Ten film pokazuje, z czym naprawdę wiąże się tranzycja medyczna i dlaczego niektóre osoby trans się na nią decydują. Co terapia hormonalna może zmienić, a czego nie. Jaką cenę ma operacja: rekonwalescencja, ryzyko i pieniądze. Czym jest dysforia płciowa i dlaczego tak trudno zrozumieć ją z zewnątrz, kiedy nie znasz jej z własnego doświadczenia. Dlaczego przekonanie, że to tylko kaprys albo moda, z trudem wyjaśnia, czemu ktoś miałby się na to wszystko godzić. I dlaczego niektóre osoby trans postanawiają w ogóle nie przechodzić tranzycji medycznej.

To trzeci film z serii o osobach transpłciowych. Pierwszy pytał, dlaczego nagle wydaje się, że jest tyle osób trans, drugi – skąd wiesz, że jesteś trans. Następny pyta: dlaczego tak trudno jest być trans?

Napisy są pisane do tego filmu, nie generowane automatycznie. Jako druga ścieżka dźwiękowa dostępny jest angielski amerykański.

ROZDZIAŁY
00:00 Dlaczego ktoś miałby się na to zdecydować?
01:33 Tranzycja to nie jedna rzecz
01:59 Co właściwie robią hormony
03:35 Chirurgia: cena fizycznej zmiany
05:37 A jeśli nie znasz tego z własnego doświadczenia?
06:45 Powrót do pytania, od którego zaczęliśmy
08:33 Dlaczego niektórzy decydują się nie przechodzić tranzycji medycznej
09:35 Pytanie, które naprawdę powinniśmy sobie zadawać
```

## português (Brasil) (`pt-BR`)

```
Por que pessoas trans mudam o próprio corpo?
```

```
Imagine decidir fazer uma cirurgia, não por causa de uma lesão, nem por causa de uma doença que aparece num exame, mas porque algo no seu próprio corpo parece profundamente errado. Imagine tomar remédios por anos, sabendo que eles vão mudar você de formas que você não consegue prever totalmente. Por que alguém escolheria isso?

Este vídeo mostra o que a transição médica realmente envolve e por que algumas pessoas trans passam por ela. O que a terapia hormonal pode e não pode mudar. O que a cirurgia exige em termos de recuperação, quais riscos envolve e quanto custa. O que é disforia de gênero, e por que é tão difícil entendê-la de fora quando você não a sente. Por que a ideia de que é só um capricho ou uma moda mal consegue explicar por que alguém aceitaria tudo isso. E por que algumas pessoas trans escolhem não fazer nenhuma transição médica.

Este é o terceiro vídeo de uma série sobre pessoas transgênero. O primeiro perguntava por que de repente parece haver tantas pessoas trans; o segundo, como você sabe que é trans. O próximo pergunta: por que é tão difícil ser trans?

As legendas foram escritas para este vídeo, não geradas automaticamente. Como segunda faixa de áudio está disponível o inglês americano.

CAPÍTULOS
00:00 Por que alguém escolheria isso?
01:33 Transição não é uma coisa só
01:59 O que os hormônios realmente fazem
03:35 Cirurgia: o preço de uma mudança física
05:37 E se você não sente isso?
06:45 De volta à pergunta com que começamos
08:33 Por que algumas pessoas escolhem não fazer a transição médica
09:35 A pergunta que deveríamos estar fazendo de verdade
```

## Türkçe (`tr`)

```
Trans İnsanlar Bedenlerini Neden Değiştirir?
```

```
Bir yaralanma yüzünden değil, taramada görünecek bir hastalık yüzünden de değil, kendi bedenindeki bir şey sana derinden yanlış geldiği için ameliyat olmaya karar verdiğini düşün. Yıllarca ilaç kullandığını düşün; bunun seni tam olarak öngöremeyeceğin şekillerde değiştireceğini bilerek. Biri neden bunu seçsin?

Bu video, tıbbi geçişin aslında neleri kapsadığını ve bazı trans insanların neden bu yolu seçtiğini ele alıyor. Hormon tedavisi neyi değiştirebilir, neyi değiştiremez? Ameliyatın iyileşme, risk ve para açısından bedeli nedir? Cinsiyet disforisi nedir ve bunu kendin hissetmiyorsan dışarıdan anlamak neden bu kadar zordur? Bunun sadece bir heves ya da bir moda olduğu fikri, birinin bütün bunları neden kabul edeceğini açıklamakta neden zorlanır? Ve bazı trans insanlar neden hiç tıbbi geçiş yapmamayı seçer?

Bu, transgender insanlar hakkındaki bir serinin üçüncü videosu. İlki, neden birdenbire bu kadar çok trans insan varmış gibi göründüğünü, ikincisi trans olduğunu nasıl anlayacağını soruyordu. Bir sonraki video şunu soruyor: Trans olmak neden bu kadar zor?

Altyazılar bu video için yazıldı, otomatik olarak oluşturulmadı. İkinci ses parçası olarak Amerikan İngilizcesi de mevcut.

BÖLÜMLER
00:00 Biri neden bunu seçsin?
01:33 Geçiş tek bir şey değildir
01:59 Hormonlar aslında ne yapar
03:35 Ameliyat: fiziksel bir değişimin bedeli
05:37 Ya bunu kendin hissetmiyorsan?
06:45 Başladığımız soruya geri dönüş
08:33 Bazı insanlar neden tıbbi geçişi tercih etmez
09:35 Asıl sormamız gereken soru
```

## українська (`uk`)

```
Чому трансгендерні люди змінюють свої тіла?
```

```
Уяви, що ти вирішуєш піти на операцію не через травму і не через хворобу, яку показав би знімок, а тому, що щось у власному тілі здається тобі глибоко неправильним. Уяви, що роками приймаєш ліки й знаєш, що вони змінять тебе так, як ти не можеш до кінця передбачити. Навіщо комусь таке обирати?

Це відео про те, що насправді передбачає медичний перехід і чому деякі трансгендерні люди на нього йдуть. Що гормональна терапія може змінити, а чого — ні. Яку ціну має операція: відновлення, ризики й гроші. Що таке гендерна дисфорія і чому її так важко зрозуміти ззовні, коли не знаєш її з власного досвіду. Чому уявлення, що це лише примха чи тренд, погано пояснює, чому хтось погоджується на все це. І чому деякі трансгендерні люди взагалі вирішують не робити медичного переходу.

Це третє відео із серії про трансгендерних людей. Перше питало, чому здається, ніби раптом стало так багато трансгендерних людей, друге — як зрозуміти, що ти транс. Наступне питає: чому так важко бути транс?

Субтитри написані для цього відео, а не згенеровані автоматично. Також доступна друга звукова доріжка — американською англійською.

РОЗДІЛИ
00:00 Навіщо комусь таке обирати?
01:33 Перехід — це не щось одне
01:59 Що насправді роблять гормони
03:35 Хірургія: ціна фізичної зміни
05:37 А що, як ти не знаєш цього з власного досвіду?
06:45 Повернення до питання, з якого ми почали
08:33 Чому дехто вирішує не робити медичного переходу
09:35 Питання, яке нам насправді варто ставити
```

## Tiếng Việt (`vi`)

```
Vì sao người chuyển giới thay đổi cơ thể mình?
```

```
Hãy tưởng tượng bạn quyết định đi phẫu thuật, không phải vì một chấn thương, cũng không phải vì một căn bệnh có thể thấy được khi chụp chiếu, mà vì bạn cảm thấy có điều gì đó ở chính cơ thể mình hoàn toàn không ổn. Hãy tưởng tượng bạn dùng thuốc suốt nhiều năm, biết rằng nó sẽ thay đổi bạn theo những cách bạn không thể đoán trước hoàn toàn. Vì sao lại có người chọn điều đó?

Video này tìm hiểu chuyển đổi về mặt y tế thực sự bao gồm những gì và vì sao một số người chuyển giới theo đuổi nó. Liệu pháp hormone có thể và không thể thay đổi những gì. Người trải qua phẫu thuật phải đánh đổi những gì về thời gian hồi phục, rủi ro và tiền bạc. Phiền muộn giới (gender dysphoria) là gì, và vì sao nó rất khó hiểu khi nhìn từ bên ngoài nếu chính bạn không cảm thấy điều đó. Vì sao quan niệm cho rằng đó chỉ là một ý thích nhất thời hay một trào lưu khó lòng giải thích được vì sao lại có người chấp nhận tất cả những điều ấy. Và vì sao một số người chuyển giới chọn hoàn toàn không chuyển đổi về mặt y tế.

Đây là video thứ ba trong loạt video về người chuyển giới. Video đầu tiên đặt câu hỏi vì sao có vẻ như đột nhiên có nhiều người chuyển giới đến vậy, video thứ hai hỏi làm sao bạn biết mình là người chuyển giới. Video tiếp theo hỏi: vì sao làm người chuyển giới lại khó khăn đến vậy?

Phụ đề được viết riêng cho video này, không phải tạo tự động. Có thể chọn tiếng Anh Mỹ ở bản âm thanh thứ hai.

CHƯƠNG
00:00 Vì sao lại có người chọn điều đó?
01:33 Chuyển đổi không phải là một thứ duy nhất
01:59 Hormone thực sự làm gì
03:35 Phẫu thuật: cái giá của một thay đổi thể chất
05:37 Nếu chính bạn không cảm thấy điều đó thì sao?
06:45 Quay lại câu hỏi ta đã đặt ra lúc đầu
08:33 Vì sao có người chọn không chuyển đổi về mặt y tế
09:35 Câu hỏi mà ta thực sự nên đặt ra
```

## čeština (`cs`)

```
Proč trans lidé mění svá těla?
```

```
Představ si, že se rozhodneš jít na operaci, ne kvůli úrazu, ne kvůli nemoci, kterou by ukázalo vyšetření, ale protože ti něco na vlastním těle připadá hluboce špatně. Představ si, že roky bereš léky a víš, že tě změní způsobem, který nedokážeš úplně předvídat. Proč by si to někdo vybral?

Video ukazuje, co lékařská tranzice doopravdy obnáší a proč ji někteří trans lidé podstupují. Co hormonální léčba dokáže a nedokáže změnit. Jakou cenu má operace: zotavování, rizika a peníze. Co je genderová dysforie a proč se zvenku tak těžko chápe, když ji v sobě necítíš. Proč představa, že je to jen rozmar nebo trend, jen těžko vysvětlí, proč by tohle všechno někdo přijal. A proč se někteří trans lidé rozhodnou lékařskou tranzici vůbec nepodstoupit.

Tohle je třetí video ze série o transgender lidech. To první se ptalo, proč se zdá, že je najednou tolik trans lidí, to druhé, jak poznáš, že jsi trans. To další se ptá: proč je tak těžké být trans?

Titulky jsou psané pro tohle video, ne strojový přepis. Jako druhá zvuková stopa je k dispozici americká angličtina.

KAPITOLY
00:00 Proč by si to někdo vybral?
01:33 Tranzice není jedna věc
01:59 Co hormony doopravdy dělají
03:35 Chirurgie: cena fyzické změny
05:37 Co když to v sobě necítíš?
06:45 Zpátky k otázce, od které jsme začali
08:33 Proč někteří lidé lékařskou tranzici nepodstoupí
09:35 Otázka, kterou bychom si měli klást doopravdy
```

## español (`es`)

```
¿Por qué las personas trans cambian su cuerpo?
```

```
Imagina que decides operarte, no por una lesión, ni por una enfermedad que se vea en una prueba, sino porque sientes que algo de tu propio cuerpo está profundamente mal. Imagina tomar medicación durante años, sabiendo que va a cambiarte de formas que no puedes predecir del todo. ¿Por qué alguien elegiría algo así?

Este vídeo explora qué implica realmente la transición médica y por qué algunas personas trans la emprenden. Qué puede cambiar la terapia hormonal y qué no. Qué supone la cirugía en términos de recuperación, riesgos y coste económico. Qué es la disforia de género y por qué es tan difícil de entender desde fuera cuando tú no la sientes. Por qué la idea de que es solo un capricho o una moda difícilmente explica por qué alguien aceptaría todo eso. Y por qué algunas personas trans deciden no hacer ninguna transición médica.

Este es el tercer vídeo de una serie sobre las personas transgénero. El primero se preguntaba por qué parece que de repente hay tantas personas trans; el segundo, cómo sabes que eres trans. El siguiente se pregunta: ¿por qué es tan difícil ser trans?

Los subtítulos están escritos para este vídeo, no generados automáticamente. Como segunda pista de audio está disponible el inglés americano.

CAPÍTULOS
00:00 ¿Por qué alguien elegiría algo así?
01:33 La transición no es una sola cosa
01:59 Lo que hacen realmente las hormonas
03:35 Cirugía: el precio de un cambio físico
05:37 ¿Y si tú no lo sientes?
06:45 De vuelta a la pregunta con la que empezamos
08:33 Por qué algunas personas deciden no hacer la transición médica
09:35 La pregunta que de verdad deberíamos hacernos
```

## svenska (`sv`)

```
Varför förändrar transpersoner sina kroppar?
```

```
Tänk dig att du bestämmer dig för en operation, inte på grund av en skada och inte på grund av en sjukdom som syns vid en undersökning, utan för att något med din egen kropp känns djupt fel. Tänk dig att ta medicin i flera år och veta att den kommer att förändra dig på sätt som du inte helt kan förutse. Varför skulle någon välja det?

Den här videon handlar om vad medicinsk transition faktiskt innebär och varför vissa transpersoner genomgår den. Vad hormonbehandling kan och inte kan förändra. Vad kirurgi innebär i fråga om återhämtning, risker och ekonomiska kostnader. Vad könsdysfori är, och varför den är så svår att förstå utifrån när du inte känner den själv. Varför idén att det bara är ett infall eller en trend har svårt att förklara varför någon skulle acceptera allt det där. Och varför vissa transpersoner väljer att inte göra någon medicinsk transition alls.

Det här är den tredje videon i en serie om transpersoner. Den första frågade varför det plötsligt verkar finnas så många transpersoner, den andra hur du vet att du är trans. Nästa video frågar: varför är det så svårt att vara trans?

Undertexterna är skrivna för den här videon, inte automatgenererade. Som andra ljudspår finns amerikansk engelska.

KAPITEL
00:00 Varför skulle någon välja det?
01:33 Transition är inte en enda sak
01:59 Vad hormoner faktiskt gör
03:35 Kirurgi: priset för en fysisk förändring
05:37 Tänk om du inte känner det själv?
06:45 Tillbaka till frågan vi började med
08:33 Varför vissa väljer att inte göra en medicinsk transition
09:35 Frågan vi egentligen borde ställa
```
