# Lokalizované názvy a popisy — 097

Čte `tools/lokalizace.py` a nahrává přes `videos.update(part="localizations")`.
Anglický titul a popis jsou v `youtube.md` a posílají se zpátky beze změny.

**Pořadí sekcí je podle YouTube Studia** (bajtově podle ČESKÉHO názvu jazyka):
fi, fr, id, it, de, pl, pt-BR, tr, uk, vi, cs, es, sv.

**Codex proběhl 2026-10-08** (`codex-youtube-preklady.txt`), 20 nálezů
(3 A, 17 B, C nic; rok, všech 12 časů, jména i atribuce sedí). Přijato 8:
fr a cs kapitola 05:08 bez slovesa dvojznačná („Plus une expérience…“, „Už
žádný…“ jako výzva) → „Ce n'est plus…“, „Už to není…“ podle S42 (Codexovo
„jen / simple“ by změnilo význam); cs „chatbot inzerovaný jako bez etických
zábran“ → „který měl podle reklamy fungovat bez…“; id těžkopádné „apa yang
memang jadi tujuan ia dibuat“ → „apa yang memang dirancang untuk
dilakukannya“; tr „basit bir kural“ (jednoduché pravidlo, anglické *just*
patří ke slovesu) → „sadece bir kural“; tr „düpedüz reddetmiyor“ →
„doğrudan reddetmiyor“; vi „không đơn giản là từ chối“ → „không từ chối
luôn“; vi kapitola 07:34 „Xây“ → „Xây dựng AI“ (jako S62). Zamítnuto 12:
kapitola 07:34 ve fi, fr, id, it, de, pl, pt-BR, tr, uk, es, sv — Codex
navrhoval „vyvíjet jako jiné technologie“, jenže kapitola má znít jako
scéna S62 daného jazyka („build … things“ = stavět, ne vyvíjet; kde scénář
má „technologie“, tam ji kapitola má taky); pl „dać jej zasady“ — genitiv
po záporu je správně a je to znění S16.

## Co se NEPŘEKLÁDÁ

- vlastní jména a názvy: WormGPT, FraudGPT, Skynet, SHODAN, Isaac Asimov
  (jen v pravopisu cílového jazyka — uk Азімов); „Three Laws of Robotics"
  se překládá všude tak, jak to má scénář daného jazyka (S17)
- atribuce: řádek s autorem a licencí zůstává beze změny anglicky, včetně
  `public domain` a `via Wikimedia Commons`; přeložený je jen nadpis bloku
- časy kapitol na vteřinu
- tagy (YouTube je per-jazyk nemá)

Odstavec o titulcích a americké stopě je doslova z tabulky kanonických znění
v `docs/zverejneni.md`. Titul = první řádek `script.<kód>.md`. Popis pointu
videa (úmysl dodává člověk, AI jen práci) neprozrazuje, jen klade otázku;
kapitoly ji naznačují stejně jako v angličtině. Terminologie kapitol je ze
scénáře daného jazyka (scény S01, S09, S16, S25, S29, S33, S37, S42, S49, S54,
S61, S65; „harm" jako v S25, pravidlo z S16, autobus z S39). Kapitola „Whose
morality?" je samostatně v 1. pádě (cs „Čí morálka?", pl, uk, tr), ve scénáři
je v pádě vazby z předchozí věty. Registr: cs ty, sv du, es tú, pt-BR você,
de du, fr tu, it tu, pl ty, id kamu, tr sen, uk ти, fi sinä, vi bạn — popis
diváka oslovuje jen v první větě.

## suomi (`fi`)

```
Miksi älykäs tekoäly auttaisi rikollista?
```

```
Pyydä chatbotia kirjoittamaan huijaussähköposti, niin se luultavasti sanoo ei. Mutta kesällä 2023 hakkerifoorumilla tuli myyntiin chatbot, jonka mainostettiin olevan vailla eettisiä rajoja, ja se teki juuri sitä, mihin se oli rakennettu.

Jos tekoäly on tarpeeksi älykäs tietääkseen, että jokin on rikos, miksei se yksinkertaisesti kieltäydy? Mitä tekemistä Asimovin robotiikan kolmella lailla on asian kanssa, ja miksi ”älä vahingoita ihmisiä” on niin vaikea muuttaa säännöksi, jota tietokone pystyy noudattamaan?

Tekstitykset on kirjoitettu tätä videota varten, ei luotu automaattisesti. Toisena ääniraitana on amerikanenglanti.

Koko teksti, lähteet ja käännökset: https://theresmoretoit-channel.github.io/fi/videos/why-would-a-smart-ai-help-a-criminal/

LUVUT
00:00 Tekoäly, joka auttaa silti
00:47 WormGPT ja FraudGPT
01:45 Miksei sille vain anneta sääntöä?
02:46 Mitä vahinko tarkoittaa?
03:13 Mitä tietokone oikeasti näkee
04:07 Samat sanat, eri aikomus
04:33 Kummallinen bussi
05:08 Ei enää ajatuskoe
06:08 Skynet ja SHODAN
06:42 Kenen moraali?
07:34 Rakenna se kuin muutkin voimakkaat teknologiat
08:04 Kuka sitä pitelee?

KUVALÄHTEET
Isaac Asimov — Phillip Leonian, New York World-Telegram & Sun, public domain, via Wikimedia Commons
```

## français (`fr`)

```
Pourquoi une IA intelligente aiderait-elle un criminel ?
```

```
Demande à un chatbot d'écrire un e-mail d'arnaque, et il dira sans doute non. Mais à l'été 2023, un chatbot présenté comme sans limites éthiques a été mis en vente sur un forum de hackers, et il a fait exactement ce pour quoi on l'avait conçu.

Si une IA est assez intelligente pour savoir que quelque chose est un crime, pourquoi ne refuse-t-elle pas tout simplement ? Quel rapport avec les Trois lois de la robotique d'Asimov, et pourquoi « Ne fais pas de mal aux gens » est-il si difficile à transformer en une règle qu'un ordinateur peut suivre ?

Les sous-titres sont écrits pour cette vidéo, pas générés automatiquement. Une piste audio en anglais américain est disponible en seconde piste.

Transcription complète, sources et traductions : https://theresmoretoit-channel.github.io/fr/videos/why-would-a-smart-ai-help-a-criminal/

CHAPITRES
00:00 Une IA qui aide quand même
00:47 WormGPT et FraudGPT
01:45 Pourquoi ne pas simplement lui donner une règle ?
02:46 « Faire du mal », ça veut dire quoi ?
03:13 Ce que l'ordinateur voit vraiment
04:07 Mêmes mots, intention différente
04:33 Un drôle de bus
05:08 Ce n'est plus une expérience de pensée
06:08 Skynet et SHODAN
06:42 La morale de qui ?
07:34 La construire comme d'autres choses puissantes
08:04 Qui le tient ?

CRÉDITS DES IMAGES
Isaac Asimov — Phillip Leonian, New York World-Telegram & Sun, public domain, via Wikimedia Commons
```

## Bahasa Indonesia (`id`)

```
Kenapa AI yang Pintar Mau Membantu Penjahat?
```

```
Minta chatbot menulis email penipuan, dan ia mungkin akan bilang tidak. Tapi pada musim panas 2023, sebuah chatbot yang diiklankan tanpa batasan etika mulai dijual di sebuah forum peretas, dan chatbot itu melakukan persis apa yang memang dirancang untuk dilakukannya.

Kalau sebuah AI cukup pintar untuk tahu bahwa sesuatu adalah kejahatan, kenapa ia tidak menolak saja? Apa hubungannya dengan Tiga Hukum Robotika Asimov, dan kenapa "jangan menyakiti manusia" begitu sulit diubah menjadi aturan yang bisa diikuti komputer?

Subtitel ditulis khusus untuk video ini, bukan dibuat secara otomatis. Tersedia juga trek audio kedua dalam bahasa Inggris Amerika.

Transkrip lengkap, sumber, dan terjemahan: https://theresmoretoit-channel.github.io/id/videos/why-would-a-smart-ai-help-a-criminal/

BAB
00:00 AI yang tetap membantu
00:47 WormGPT dan FraudGPT
01:45 Kenapa tidak beri saja aturan?
02:46 Apa arti "menyakiti"?
03:13 Apa yang sebenarnya dilihat komputer
04:07 Kata-kata sama, niat berbeda
04:33 Jenis bus yang aneh
05:08 Bukan lagi eksperimen pikiran
06:08 Skynet dan SHODAN
06:42 Moralitas siapa?
07:34 Membangunnya seperti teknologi berdaya besar lainnya
08:04 Siapa yang memegangnya?

KREDIT GAMBAR
Isaac Asimov — Phillip Leonian, New York World-Telegram & Sun, public domain, via Wikimedia Commons
```

## italiano (`it`)

```
Perché un'IA intelligente aiuterebbe un criminale?
```

```
Chiedi a un chatbot di scrivere un'email truffa e probabilmente ti dirà di no. Ma nell'estate del 2023 un chatbot pubblicizzato come privo di limiti etici è stato messo in vendita su un forum di hacker, e ha fatto esattamente ciò per cui era stato costruito.

Se un'IA è abbastanza intelligente da sapere che qualcosa è un reato, perché non si rifiuta e basta? Che c'entrano le Tre leggi della robotica di Asimov, e perché "Non fare del male alle persone" è così difficile da trasformare in una regola che un computer possa seguire?

I sottotitoli sono scritti per questo video, non generati automaticamente. Come seconda traccia audio è disponibile l’inglese americano.

Trascrizione completa, fonti e traduzioni: https://theresmoretoit-channel.github.io/it/videos/why-would-a-smart-ai-help-a-criminal/

CAPITOLI
00:00 Un'IA che aiuta lo stesso
00:47 WormGPT e FraudGPT
01:45 Perché non darle semplicemente una regola?
02:46 Cosa significa "danno"?
03:13 Cosa vede davvero il computer
04:07 Stesse parole, intenzioni diverse
04:33 Uno strano tipo di autobus
05:08 Non più un esperimento mentale
06:08 Skynet e SHODAN
06:42 La morale di chi?
07:34 Costruirla come altre cose potenti
08:04 Chi lo tiene in mano?

CREDITI DELLE IMMAGINI
Isaac Asimov — Phillip Leonian, New York World-Telegram & Sun, public domain, via Wikimedia Commons
```

## Deutsch (`de`)

```
Warum sollte eine kluge KI einem Kriminellen helfen?
```

```
Bitte einen Chatbot um eine Betrugs-E-Mail, und er sagt wahrscheinlich Nein. Doch im Sommer 2023 wurde in einem Hackerforum ein Chatbot zum Kauf angeboten, der als frei von ethischen Schranken beworben wurde – und er tat genau das, wofür er gebaut worden war.

Wenn eine KI klug genug ist, um zu wissen, dass etwas eine Straftat ist, warum lehnt sie dann nicht einfach ab? Was haben Asimovs drei Gesetze der Robotik damit zu tun, und warum ist es so schwer, aus „Füge Menschen keinen Schaden zu“ eine Regel zu machen, die ein Computer befolgen kann?

Die Untertitel wurden für dieses Video geschrieben, nicht automatisch erzeugt. Als zweite Tonspur steht amerikanisches Englisch bereit.

Vollständiger Text, Quellen und Übersetzungen: https://theresmoretoit-channel.github.io/de/videos/why-would-a-smart-ai-help-a-criminal/

KAPITEL
00:00 Eine KI, die trotzdem hilft
00:47 WormGPT und FraudGPT
01:45 Warum nicht einfach eine Regel?
02:46 Was bedeutet „Schaden“?
03:13 Was der Computer wirklich sieht
04:07 Gleiche Worte, andere Absicht
04:33 Eine seltsame Art von Bus
05:08 Kein Gedankenexperiment mehr
06:08 Skynet und SHODAN
06:42 Wessen Moral?
07:34 So bauen wie andere mächtige Dinge
08:04 Wer hält es in der Hand?

BILDNACHWEISE
Isaac Asimov — Phillip Leonian, New York World-Telegram & Sun, public domain, via Wikimedia Commons
```

## polski (`pl`)

```
Dlaczego inteligentna AI miałaby pomóc przestępcy?
```

```
Poproś chatbota o oszukańczego maila, a pewnie powie nie. Ale latem 2023 roku na forum hakerskim trafił do sprzedaży chatbot reklamowany jako pozbawiony etycznych ograniczeń – i robił dokładnie to, do czego go zbudowano.

Jeśli AI jest na tyle inteligentna, by wiedzieć, że coś jest przestępstwem, dlaczego po prostu nie odmówi? Co mają z tym wspólnego trzy prawa robotyki Asimova i dlaczego tak trudno zamienić „Nie krzywdź ludzi” w zasadę, której komputer potrafi przestrzegać?

Napisy są pisane do tego filmu, nie generowane automatycznie. Jako druga ścieżka dźwiękowa dostępny jest angielski amerykański.

Pełna transkrypcja, źródła i tłumaczenia: https://theresmoretoit-channel.github.io/pl/videos/why-would-a-smart-ai-help-a-criminal/

ROZDZIAŁY
00:00 AI, która i tak pomaga
00:47 WormGPT i FraudGPT
01:45 Czemu po prostu nie dać jej zasady?
02:46 Co znaczy „krzywda”?
03:13 Co naprawdę widzi komputer
04:07 Te same słowa, inna intencja
04:33 Dziwny rodzaj autobusu
05:08 To już nie eksperyment myślowy
06:08 Skynet i SHODAN
06:42 Czyja moralność?
07:34 Budować ją jak inne potężne rzeczy
08:04 Kto je trzyma?

ŹRÓDŁA ZDJĘĆ
Isaac Asimov — Phillip Leonian, New York World-Telegram & Sun, public domain, via Wikimedia Commons
```

## português (Brasil) (`pt-BR`)

```
Por que uma IA inteligente ajudaria um criminoso?
```

```
Peça para um chatbot escrever um e-mail de golpe e ele provavelmente vai dizer não. Mas no verão de 2023, um chatbot anunciado como sem limites éticos foi posto à venda num fórum de hackers, e fez exatamente aquilo para que foi criado.

Se uma IA é inteligente o bastante para saber que algo é crime, por que ela simplesmente não se recusa? O que as Três Leis da Robótica de Asimov têm a ver com isso, e por que "não machuque pessoas" é tão difícil de transformar numa regra que um computador consiga seguir?

As legendas foram escritas para este vídeo, não geradas automaticamente. Como segunda faixa de áudio está disponível o inglês americano.

Transcrição completa, fontes e traduções: https://theresmoretoit-channel.github.io/pt-br/videos/why-would-a-smart-ai-help-a-criminal/

CAPÍTULOS
00:00 Uma IA que ajuda mesmo assim
00:47 WormGPT e FraudGPT
01:45 Por que não dar uma regra para ela?
02:46 O que "fazer mal" significa?
03:13 O que o computador realmente vê
04:07 Mesmas palavras, intenções diferentes
04:33 Um tipo estranho de ônibus
05:08 Já não é um experimento mental
06:08 Skynet e SHODAN
06:42 A moral de quem?
07:34 Construir como outras coisas poderosas
08:04 Quem está segurando?

CRÉDITOS DAS IMAGENS
Isaac Asimov — Phillip Leonian, New York World-Telegram & Sun, public domain, via Wikimedia Commons
```

## Türkçe (`tr`)

```
Zeki Bir Yapay Zekâ Neden Bir Suçluya Yardım Etsin?
```

```
Bir sohbet botundan dolandırıcılık e-postası yazmasını iste, büyük ihtimalle hayır der. Ama 2023 yazında, etik sınırları olmadığı ilan edilen bir sohbet botu bir hacker forumunda satışa çıktı ve tam olarak yapılma amacı neyse onu yaptı.

Bir yapay zekâ bir şeyin suç olduğunu bilecek kadar zekiyse, neden doğrudan reddetmiyor? Asimov'un Üç Robot Yasası'nın bununla ne ilgisi var ve "İnsanlara zarar verme" ilkesini bir bilgisayarın uyabileceği bir kurala dönüştürmek neden bu kadar zor?

Altyazılar bu video için yazıldı, otomatik olarak oluşturulmadı. İkinci ses parçası olarak Amerikan İngilizcesi de mevcut.

Metnin tamamı, kaynaklar ve çeviriler: https://theresmoretoit-channel.github.io/tr/videos/why-would-a-smart-ai-help-a-criminal/

BÖLÜMLER
00:00 Yine de yardım eden bir yapay zekâ
00:47 WormGPT ve FraudGPT
01:45 Neden ona sadece bir kural vermiyoruz?
02:46 "Zarar" ne demek?
03:13 Bilgisayar aslında ne görür?
04:07 Aynı kelimeler, farklı niyet
04:33 Tuhaf bir otobüs türü
05:08 Artık bir düşünce deneyi değil
06:08 Skynet ve SHODAN
06:42 Kimin ahlakı?
07:34 Diğer güçlü şeyler gibi inşa etmek
08:04 Onu kim tutuyor?

GÖRSEL KAYNAKLARI
Isaac Asimov — Phillip Leonian, New York World-Telegram & Sun, public domain, via Wikimedia Commons
```

## українська (`uk`)

```
Чому розумний ШІ допоміг би злочинцеві?
```

```
Попроси чат-бот написати шахрайський лист, і він, найімовірніше, скаже «ні». Але влітку 2023 року на хакерському форумі з'явився в продажу чат-бот, який рекламували як вільний від етичних обмежень, — і він робив саме те, для чого його створили.

Якщо ШІ достатньо розумний, щоб знати, що щось є злочином, чому він просто не відмовляється? До чого тут Три закони робототехніки Азімова і чому «Не завдавай шкоди людям» так важко перетворити на правило, якого може дотримуватися комп'ютер?

Субтитри написані для цього відео, а не згенеровані автоматично. Також доступна друга звукова доріжка — американською англійською.

Повний текст, джерела та переклади: https://theresmoretoit-channel.github.io/uk/videos/why-would-a-smart-ai-help-a-criminal/

РОЗДІЛИ
00:00 ШІ, який усе одно допомагає
00:47 WormGPT і FraudGPT
01:45 Чому б просто не дати йому правило?
02:46 Що насправді означає «шкода»?
03:13 Що насправді бачить комп'ютер
04:07 Ті самі слова, різний намір
04:33 Дивний різновид автобуса
05:08 Уже не мисленнєвий експеримент
06:08 Skynet і SHODAN
06:42 Чия мораль?
07:34 Будувати його як інші потужні речі
08:04 Хто його тримає?

ДЖЕРЕЛА ЗОБРАЖЕНЬ
Isaac Asimov — Phillip Leonian, New York World-Telegram & Sun, public domain, via Wikimedia Commons
```

## Tiếng Việt (`vi`)

```
Vì sao một AI thông minh lại giúp tội phạm?
```

```
Nhờ một chatbot viết email lừa đảo, có lẽ nó sẽ nói không. Nhưng mùa hè năm 2023, một chatbot được quảng cáo là không có giới hạn đạo đức đã được rao bán trên một diễn đàn hacker, và nó làm đúng những gì nó được tạo ra để làm.

Nếu một AI đủ thông minh để biết một việc là phạm tội, sao nó không từ chối luôn? Ba định luật về robot của Asimov thì liên quan gì, và vì sao “không được làm hại con người” lại khó biến thành một quy tắc mà máy tính có thể tuân theo đến vậy?

Phụ đề được viết riêng cho video này, không phải tạo tự động. Có thể chọn tiếng Anh Mỹ ở bản âm thanh thứ hai.

Toàn văn, nguồn và bản dịch: https://theresmoretoit-channel.github.io/vi/videos/why-would-a-smart-ai-help-a-criminal/

CHƯƠNG
00:00 Một AI vẫn giúp bạn
00:47 WormGPT và FraudGPT
01:45 Sao không cho nó một quy tắc?
02:46 “Tổn hại” nghĩa là gì?
03:13 Máy tính thực sự thấy gì
04:07 Cùng câu chữ, khác ý định
04:33 Một loại xe buýt kỳ lạ
05:08 Không còn là thí nghiệm tưởng tượng
06:08 Skynet và SHODAN
06:42 Đạo đức của ai?
07:34 Xây dựng AI như những thứ mạnh mẽ khác
08:04 Ai đang cầm nó?

NGUỒN HÌNH ẢNH
Isaac Asimov — Phillip Leonian, New York World-Telegram & Sun, public domain, via Wikimedia Commons
```

## čeština (`cs`)

```
Proč by chytrá AI pomáhala zločinci?
```

```
Požádej chatbota o podvodný e-mail a nejspíš řekne ne. Jenže v létě 2023 se na hackerském fóru začal prodávat chatbot, který měl podle reklamy fungovat bez etických zábran – a dělal přesně to, k čemu byl postavený.

Když je AI dost chytrá na to, aby věděla, že něco je trestný čin, proč prostě neodmítne? Co s tím mají společného Asimovovy tři zákony robotiky a proč je tak těžké udělat z „Neubližuj lidem“ pravidlo, kterým se počítač dokáže řídit?

Titulky jsou psané pro tohle video, ne strojový přepis. Jako druhá zvuková stopa je k dispozici americká angličtina.

Celý text, zdroje a překlady: https://theresmoretoit-channel.github.io/cs/videos/why-would-a-smart-ai-help-a-criminal/

KAPITOLY
00:00 AI, která stejně pomůže
00:47 WormGPT a FraudGPT
01:45 Proč jí prostě nedat pravidlo?
02:46 Co vlastně znamená „ublížit“?
03:13 Co počítač doopravdy vidí
04:07 Stejná slova, jiný úmysl
04:33 Zvláštní druh autobusu
05:08 Už to není myšlenkový experiment
06:08 Skynet a SHODAN
06:42 Čí morálka?
07:34 Stavět ji jako jiné mocné technologie
08:04 Kdo ho drží v ruce?

ZDROJE OBRÁZKŮ
Isaac Asimov — Phillip Leonian, New York World-Telegram & Sun, public domain, via Wikimedia Commons
```

## español (`es`)

```
¿Por qué una IA inteligente ayudaría a un criminal?
```

```
Pídele a un chatbot que escriba un correo de estafa y probablemente te dirá que no. Pero en el verano de 2023, un chatbot anunciado como libre de límites éticos salió a la venta en un foro de hackers, e hizo exactamente aquello para lo que se creó.

Si una IA es lo bastante inteligente para saber que algo es un delito, ¿por qué no se niega sin más? ¿Qué tienen que ver las Tres Leyes de la Robótica de Asimov, y por qué es tan difícil convertir «no hagas daño a las personas» en una regla que un ordenador pueda seguir?

Los subtítulos están escritos para este vídeo, no generados automáticamente. Como segunda pista de audio está disponible el inglés americano.

Transcripción completa, fuentes y traducciones: https://theresmoretoit-channel.github.io/es/videos/why-would-a-smart-ai-help-a-criminal/

CAPÍTULOS
00:00 Una IA que ayuda igualmente
00:47 WormGPT y FraudGPT
01:45 ¿Por qué no darle una regla?
02:46 ¿Qué significa «daño»?
03:13 Lo que el ordenador ve de verdad
04:07 Mismas palabras, distinta intención
04:33 Un autobús muy raro
05:08 Ya no es un experimento mental
06:08 Skynet y SHODAN
06:42 ¿La moral de quién?
07:34 Construirla como otras cosas poderosas
08:04 ¿Quién la sostiene?

CRÉDITOS DE LAS IMÁGENES
Isaac Asimov — Phillip Leonian, New York World-Telegram & Sun, public domain, via Wikimedia Commons
```

## svenska (`sv`)

```
Varför skulle en smart AI hjälpa en brottsling?
```

```
Be en chattbot skriva ett bedrägerimejl, så säger den förmodligen nej. Men sommaren 2023 började en chattbot som marknadsfördes som fri från etiska spärrar säljas på ett hackerforum, och den gjorde precis det den var byggd för.

Om en AI är smart nog att veta att något är ett brott, varför vägrar den inte bara? Vad har Asimovs tre robotlagar med saken att göra, och varför är det så svårt att göra om ”skada inte människor” till en regel som en dator kan följa?

Undertexterna är skrivna för den här videon, inte automatgenererade. Som andra ljudspår finns amerikansk engelska.

Hela texten, källor och översättningar: https://theresmoretoit-channel.github.io/sv/videos/why-would-a-smart-ai-help-a-criminal/

KAPITEL
00:00 En AI som hjälper ändå
00:47 WormGPT och FraudGPT
01:45 Varför inte bara ge den en regel?
02:46 Vad betyder ”skada”?
03:13 Vad datorn faktiskt ser
04:07 Samma ord, olika avsikt
04:33 En märklig sorts buss
05:08 Inte längre ett tankeexperiment
06:08 Skynet och SHODAN
06:42 Vems moral?
07:34 Bygg den som andra kraftfulla saker
08:04 Vem håller i det?

BILDKÄLLOR
Isaac Asimov — Phillip Leonian, New York World-Telegram & Sun, public domain, via Wikimedia Commons
```
