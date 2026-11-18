# YouTube — lokalizace 084 „When Does Society Become the Problem?"

Třináct překladů titulu a bloku „Popis" z `youtube.md` (anglický snippet se
posílá beze změny). Čte `tools/lokalizace.py`; formát a pořadí sekcí podle
`docs/zverejneni.md`.

## Co se NEPŘEKLÁDÁ

- **vlastní jména** — Find A Helpline, The Trevor Project, Trans Lifeline,
  Samaritans, ICD-11 (kromě cs „MKN-11", fr „CIM-11", es „CIE-11",
  pt-BR „CID-11", uk «МКХ-11», jako ve scénářích),
- **linky pomoci: čísla, SMS kód START a odkazy** — beze změny, ověřeno
  2026-10-25 (viz poznámka v `youtube.md`). Překládá se jen nadpis,
  popisky a názvy zemí; nic se nepřidává ani neubírá (žádné místní linky
  navíc),
- **časy kapitol** (na vteřinu podle `work/timing.json` masteru, celkem
  794,08 s, kapitolové desky S14, S27, S43, S61, S74, S85) — po každém
  dalším běhu `tts.py` je přepočítej tady i v `youtube.md`,
- **tagy** — YouTube je per jazyk nemá,
- **odstavec o titulcích a americké stopě** se nepřekládá znovu, je doslova
  z tabulky v `docs/zverejneni.md` („Popis NEJMENUJE počet jazyků titulků").

Video nemá archivní snímek, takže sekce ZDROJE OBRÁZKŮ odpadá (jako
v anglickém `youtube.md`).

Titul je první řádek `# …` přeloženého `script.<kód>.md`. Názvy kapitol
jsou mluvené kapitolové desky z přeložených scénářů (S14, S27, S43, S61,
S74, S85), bez koncové tečky jako v anglickém `youtube.md`; kapitola
00:00 („What if the world saw you as a problem?") desku nemá a je
přeložená v duchu S01. Sérijní odstavec jmenuje 080–082 jako
`083-*/youtube-preklady.md` a 083 nepřímou otázkou podle jeho
lokalizovaného titulu.

Terminologie podle `script.<kód>.md` téhož videa (cs „genderová dysforie",
„minoritní stres", „průzkum", „americký psychiatrický manuál"; de
„Geschlechtsdysphorie", „Minderheitenstress", „Umfrage"; pl „dysforia
płciowa", „stres mniejszościowy", „ankieta"; uk «гендерна дисфорія»,
«стрес меншин», «опитування», «ЛГБТК+»; tr „cinsiyet disforisi", „azınlık
stresi", „anket"; id „disforia gender", „stres minoritas", „survei";
fi „sukupuolidysforia", „vähemmistöstressi", „kysely"; vi „phiền muộn
giới", „căng thẳng thiểu số", „khảo sát"; fr „dysphorie de genre", „stress
minoritaire", „enquête"; it „disforia di genere", „minority stress",
„sondaggio"; es „disforia de género", „estrés de minorías", „encuesta";
pt-BR „disforia de gênero", „estresse de minoria", „pesquisa"; sv
„könsdysfori", „minoritetsstress", „enkät", „hbtq+").

Popis drží míru jistoty originálu: čísla ze studií neuvádí, u průzkumu
„co zjistil, když se cítili přijímaní", ne „čemu přijetí zabrání";
výzkum „co nám říct může a co ne".

Registr: tyká se tam, kde jazyk volí (cs, de du, pl, uk ти, tr sen,
id kamu, fr tu, es tú, it tu, pt-BR você, sv du), fi „sinä", vi „bạn" —
jako ve scénářích 084 a v 080–083. Rod se vůči divákovi nedoplňuje:
cs „Ne proto, že by kvůli tobě někdo trpěl" (jako pl/uk S02), „nemusíš
tím procházet v osamění", pl „w pojedynkę", uk «наодинці», es „a solas",
it „in solitudine", fr „en solitaire", pt-BR „sem apoio".

## suomi (`fi`)

```
Milloin yhteiskunnasta tulee ongelma?
```

```
Kuvittele, että heräät huomenna ja huomaat, että siitä, miten maailma sinut näkee, on tullut ongelma. Ei siksi, että olisit satuttanut ketään, vaan siksi, ettet vastaa ympärilläsi olevien ihmisten odotuksia.

Tämä video käsittelee sitä, mitä tutkimus kertoo transihmisten itsemurhista ja mitä se pystyy kertomaan ja mitä ei. Tanskalainen tutkimus, joka seurasi koko maan väestöä neljän vuosikymmenen ajan. Sukupuolidysforian ja transidentiteetin ero sekä se, miten ICD-11 ja yhdysvaltalainen psykiatrinen käsikirja sitä kuvaavat. Vähemmistöstressi ja se, miten sadat pienet kokemukset voivat kasautua. Laaja kysely yhdysvaltalaisille LGBTQ+-nuorille ja se, mitä se havaitsi, kun nuoret kokivat tulevansa hyväksytyiksi. Ja kysymys siitä, mistä yhteiskunta on vastuussa, kun emme voi poistaa jokaista ihmisen kivun lähdettä mutta voimme päättää olla lisäämättä sitä.

Tämä on viides ja viimeinen video transihmisiä käsittelevässä sarjassa. Aiemmissa videoissa kysyttiin, miksi transihmisiä näyttää yhtäkkiä olevan niin paljon, mistä tiedät, että olet trans, miksi transihmiset muuttavat kehoaan ja miksi on niin vaikeaa olla trans.

JOS SINULLA ON NYT VAIKEAA
Sinun ei tarvitse selvitä siitä yksin. Nämä palvelut ovat maksuttomia ja luottamuksellisia:
Find A Helpline, tukea yli 175 maassa: https://findahelpline.com
Yhdysvallat ja Kanada: soita tai lähetä tekstiviesti numeroon 988
The Trevor Project, LGBTQ+-nuorille Yhdysvalloissa: 1-866-488-7386, tekstiviesti START numeroon 678-678 tai chat osoitteessa https://www.thetrevorproject.org/get-help/
Trans Lifeline, transihmisten ylläpitämää vertaistukea: Yhdysvallat (877) 565-8860, Kanada (877) 330-6366
Iso-Britannia ja Irlanti: Samaritans, 116 123
Jos olet välittömässä vaarassa, soita paikalliseen hätänumeroon.

Tekstitykset on kirjoitettu tätä videota varten, ei luotu automaattisesti. Toisena ääniraitana on amerikanenglanti.

Koko teksti, lähteet ja käännökset: https://theresmoretoit-channel.github.io/fi/videos/when-does-society-become-the-problem/

LUVUT
00:00 Entä jos maailma näkisi sinut ongelmana?
01:38 Kun oma keho tuntuu väärältä
03:43 Maailma tuo oman taakkansa
05:39 Luvut kivun takana
08:10 Mitä tapahtuu, kun ihmiset hyväksytään?
09:50 Kuka on vastuussa?
11:11 Peili
```

## français (`fr`)

```
Quand la société devient-elle le problème ?
```

```
Imagine que tu te réveilles demain et que tu découvres que la façon dont le monde te voit est devenue un problème. Pas parce que tu as fait du mal à quelqu'un, mais parce que tu ne corresponds pas aux attentes des gens qui t'entourent.

Cette vidéo examine ce que la recherche dit du suicide chez les personnes transgenres, et ce qu'elle peut et ne peut pas nous apprendre. Une étude danoise qui a suivi toute la population d'un pays sur quatre décennies. La différence entre la dysphorie de genre et l'identité transgenre, et la façon dont la CIM-11 et le manuel de psychiatrie américain en parlent. Le stress minoritaire, et comment des centaines de petites expériences peuvent s'additionner. Une grande enquête auprès de jeunes LGBTQ+ aux États-Unis, et ce qu'elle a constaté quand ces jeunes se sentaient acceptés. Et la question de ce dont la société est responsable, quand on ne peut pas supprimer chaque source de la douleur de quelqu'un, mais qu'on peut choisir de ne pas en rajouter.

C'est la cinquième et dernière vidéo d'une série sur les personnes transgenres. Les précédentes se demandaient pourquoi il semble soudain y avoir autant de personnes trans, comment savoir qu'on est trans, pourquoi les personnes trans changent leur corps, et pourquoi il est si difficile d'être trans.

SI TU TRAVERSES UNE PÉRIODE DIFFICILE
Tu n'as pas à affronter ça en solitaire. Ces services sont gratuits et confidentiels :
Find A Helpline, du soutien dans plus de 175 pays : https://findahelpline.com
États-Unis et Canada : appelle ou envoie un SMS au 988
The Trevor Project, pour les jeunes LGBTQ+ aux États-Unis : 1-866-488-7386, envoie START par SMS au 678-678, ou utilise le chat sur https://www.thetrevorproject.org/get-help/
Trans Lifeline, soutien entre pairs assuré par des personnes trans : États-Unis (877) 565-8860, Canada (877) 330-6366
Royaume-Uni et Irlande : Samaritans, 116 123
Si tu es en danger immédiat, appelle le numéro d'urgence local.

Les sous-titres sont écrits pour cette vidéo, pas générés automatiquement. Une piste audio en anglais américain est disponible en seconde piste.

Transcription complète, sources et traductions : https://theresmoretoit-channel.github.io/fr/videos/when-does-society-become-the-problem/

CHAPITRES
00:00 Et si le monde te voyait comme un problème ?
01:38 Quand ton propre corps ne te semble pas le bon
03:43 Le monde y ajoute son propre poids
05:39 Les chiffres derrière la douleur
08:10 Que se passe-t-il quand les gens sont acceptés ?
09:50 Qui est responsable ?
11:11 Le miroir
```

## Bahasa Indonesia (`id`)

```
Kapan Masyarakat Menjadi Masalahnya?
```

```
Bayangkan kamu bangun besok dan mendapati bahwa cara dunia melihatmu telah menjadi masalah. Bukan karena kamu menyakiti siapa pun, tetapi karena kamu tidak sesuai dengan harapan orang-orang di sekitarmu.

Video ini membahas apa kata penelitian tentang bunuh diri di kalangan orang transgender, serta apa yang bisa dan tidak bisa dikatakannya kepada kita. Sebuah studi Denmark yang mengikuti seluruh populasi negara itu selama empat dekade. Perbedaan antara disforia gender dan identitas transgender, serta bagaimana ICD-11 dan manual psikiatri Amerika menggambarkannya. Stres minoritas, dan bagaimana ratusan pengalaman kecil bisa menumpuk. Sebuah survei besar terhadap anak muda LGBTQ+ di Amerika Serikat, dan apa temuannya ketika mereka merasa diterima. Dan pertanyaan tentang apa yang menjadi tanggung jawab masyarakat, ketika kita tidak bisa menghapus setiap sumber rasa sakit seseorang, tetapi bisa memilih untuk tidak menambahnya.

Ini adalah video kelima sekaligus terakhir dalam seri tentang orang transgender. Video-video sebelumnya bertanya kenapa tiba-tiba sepertinya ada begitu banyak orang trans, bagaimana kamu tahu kalau kamu trans, kenapa orang trans mengubah tubuh mereka, dan kenapa begitu sulit menjadi trans.

JIKA KAMU SEDANG KESULITAN
Kamu tidak harus melewatinya sendirian. Layanan-layanan ini gratis dan menjaga kerahasiaanmu:
Find A Helpline, dukungan di lebih dari 175 negara: https://findahelpline.com
Amerika Serikat dan Kanada: telepon atau kirim SMS ke 988
The Trevor Project, untuk anak muda LGBTQ+ di AS: 1-866-488-7386, kirim SMS START ke 678-678, atau chat di https://www.thetrevorproject.org/get-help/
Trans Lifeline, dukungan sebaya yang dijalankan oleh orang trans: AS (877) 565-8860, Kanada (877) 330-6366
Inggris Raya dan Irlandia: Samaritans, 116 123
Jika kamu sedang dalam bahaya saat ini, segera hubungi nomor darurat setempat.

Subtitel ditulis khusus untuk video ini, bukan dibuat secara otomatis. Tersedia juga trek audio kedua dalam bahasa Inggris Amerika.

Transkrip lengkap, sumber, dan terjemahan: https://theresmoretoit-channel.github.io/id/videos/when-does-society-become-the-problem/

BAB
00:00 Bagaimana kalau dunia melihatmu sebagai masalah?
01:38 Ketika tubuhmu sendiri terasa salah
03:43 Dunia menambahkan bebannya sendiri
05:39 Angka-angka di balik rasa sakit
08:10 Apa yang terjadi ketika orang diterima?
09:50 Siapa yang bertanggung jawab?
11:11 Cermin
```

## italiano (`it`)

```
Quando è la società a diventare il problema?
```

```
Immagina di svegliarti domani e di scoprire che il modo in cui il mondo ti vede è diventato un problema. Non perché hai fatto del male a qualcuno, ma perché non corrispondi alle aspettative delle persone intorno a te.

Questo video esamina che cosa dice la ricerca sul suicidio tra le persone transgender, e che cosa può e non può dirci. Uno studio danese che ha seguito l'intera popolazione di un paese per quattro decenni. La differenza tra disforia di genere e identità transgender, e come ne parlano l'ICD-11 e il manuale psichiatrico americano. Il minority stress, e come centinaia di piccole esperienze possono sommarsi. Un grande sondaggio tra giovani LGBTQ+ negli Stati Uniti, e che cosa ha rilevato quando si sentivano accettati. E la domanda: di che cosa è responsabile la società, quando non possiamo eliminare ogni fonte del dolore di qualcuno, ma possiamo scegliere di non aggiungerne altro?

Questo è il quinto e ultimo video di una serie sulle persone transgender. I precedenti si chiedevano perché all'improvviso sembrino esserci così tante persone trans, come fai a sapere di essere trans, perché le persone trans cambiano il proprio corpo e perché è così difficile essere trans.

SE STAI ATTRAVERSANDO UN MOMENTO DIFFICILE
Non devi affrontarlo in solitudine. Questi servizi sono gratuiti e riservati:
Find A Helpline, supporto in oltre 175 paesi: https://findahelpline.com
Stati Uniti e Canada: chiama o manda un SMS al 988
The Trevor Project, per giovani LGBTQ+ negli Stati Uniti: 1-866-488-7386, manda START via SMS al 678-678 o usa la chat su https://www.thetrevorproject.org/get-help/
Trans Lifeline, supporto tra pari gestito da persone trans: Stati Uniti (877) 565-8860, Canada (877) 330-6366
Regno Unito e Irlanda: Samaritans, 116 123
Se sei in pericolo immediato, chiama il numero di emergenza locale.

I sottotitoli sono scritti per questo video, non generati automaticamente. Come seconda traccia audio è disponibile l’inglese americano.

Trascrizione completa, fonti e traduzioni: https://theresmoretoit-channel.github.io/it/videos/when-does-society-become-the-problem/

CAPITOLI
00:00 E se il mondo ti vedesse come un problema?
01:38 Quando il tuo stesso corpo ti sembra sbagliato
03:43 Il mondo aggiunge il suo peso
05:39 I numeri dietro il dolore
08:10 Che cosa succede quando le persone vengono accettate?
09:50 Chi è responsabile?
11:11 Lo specchio
```

## Deutsch (`de`)

```
Wann wird die Gesellschaft zum Problem?
```

```
Stell dir vor, du wachst morgen auf und merkst, dass die Art, wie die Welt dich sieht, zum Problem geworden ist. Nicht, weil du jemandem wehgetan hast, sondern weil du nicht den Erwartungen der Menschen um dich herum entsprichst.

Dieses Video zeigt, was die Forschung über Suizid bei trans Menschen sagt und was sie uns sagen kann und was nicht. Eine dänische Studie, die die gesamte Bevölkerung eines Landes über vier Jahrzehnte verfolgt hat. Der Unterschied zwischen Geschlechtsdysphorie und trans Identität und wie die ICD-11 und das amerikanische Psychiatrie-Handbuch das beschreiben. Minderheitenstress und wie sich Hunderte kleiner Erfahrungen summieren können. Eine große Umfrage unter jungen LGBTQ+-Menschen in den USA und was sie ergab, wenn sich die jungen Menschen akzeptiert fühlten. Und die Frage, wofür die Gesellschaft verantwortlich ist, wenn wir zwar nicht jede Quelle für den Schmerz eines Menschen beseitigen können, uns aber dafür entscheiden können, nicht noch etwas hinzuzufügen.

Das ist das fünfte und letzte Video einer Reihe über trans Menschen. Die bisherigen fragten, warum es plötzlich so viele trans Menschen zu geben scheint, woher du weißt, dass du trans bist, warum trans Menschen ihren Körper verändern und warum es so schwer ist, trans zu sein.

WENN ES DIR GERADE SCHLECHT GEHT
Du musst da nicht allein durch. Diese Angebote sind kostenlos und vertraulich:
Find A Helpline, Unterstützung in mehr als 175 Ländern: https://findahelpline.com
USA und Kanada: 988 anrufen oder eine SMS schicken
The Trevor Project, für junge LGBTQ+-Menschen in den USA: 1-866-488-7386, SMS mit START an 678-678 oder Chat unter https://www.thetrevorproject.org/get-help/
Trans Lifeline, Peer-Support von trans Menschen: USA (877) 565-8860, Kanada (877) 330-6366
Vereinigtes Königreich und Irland: Samaritans, 116 123
Wenn du in akuter Gefahr bist, ruf die örtliche Notrufnummer an.

Die Untertitel wurden für dieses Video geschrieben, nicht automatisch erzeugt. Als zweite Tonspur steht amerikanisches Englisch bereit.

Vollständiger Text, Quellen und Übersetzungen: https://theresmoretoit-channel.github.io/de/videos/when-does-society-become-the-problem/

KAPITEL
00:00 Was, wenn die Welt dich als Problem sähe?
01:38 Wenn sich der eigene Körper falsch anfühlt
03:43 Die Welt legt noch etwas obendrauf
05:39 Die Zahlen hinter dem Schmerz
08:10 Was passiert, wenn Menschen akzeptiert werden?
09:50 Wer trägt die Verantwortung?
11:11 Der Spiegel
```

## polski (`pl`)

```
Kiedy to społeczeństwo staje się problemem?
```

```
Wyobraź sobie, że budzisz się jutro i odkrywasz, że to, jak widzi cię świat, stało się problemem. Nie dlatego, że ktoś przez ciebie ucierpiał, ale dlatego, że nie spełniasz oczekiwań ludzi wokół ciebie.

Ten film przygląda się temu, co badania mówią o samobójstwach wśród osób transpłciowych i czego mogą, a czego nie mogą nam powiedzieć. Duńskie badanie, które przez cztery dekady śledziło całą populację kraju. Różnica między dysforią płciową a tożsamością transpłciową oraz to, jak opisują to ICD-11 i amerykański podręcznik psychiatryczny. Stres mniejszościowy i to, jak setki drobnych doświadczeń mogą się sumować. Duża ankieta wśród młodych osób LGBTQ+ w Stanach Zjednoczonych i to, co wykazała, kiedy czuły się one akceptowane. I pytanie, za co odpowiada społeczeństwo, skoro nie możemy usunąć każdego źródła czyjegoś bólu, ale możemy zdecydować, że nie będziemy do niego niczego dokładać.

To piąty i ostatni film z serii o osobach transpłciowych. Poprzednie pytały, dlaczego nagle wydaje się, że jest tyle osób trans, skąd wiesz, że jesteś trans, dlaczego osoby trans zmieniają swoje ciała i dlaczego tak trudno jest być trans.

JEŚLI JEST CI CIĘŻKO
Nie musisz przez to przechodzić w pojedynkę. Te usługi są bezpłatne i poufne:
Find A Helpline, wsparcie w ponad 175 krajach: https://findahelpline.com
Stany Zjednoczone i Kanada: zadzwoń lub wyślij SMS pod numer 988
The Trevor Project, dla młodych osób LGBTQ+ w USA: 1-866-488-7386, SMS o treści START pod numer 678-678 lub czat na https://www.thetrevorproject.org/get-help/
Trans Lifeline, wzajemne wsparcie prowadzone przez osoby trans: USA (877) 565-8860, Kanada (877) 330-6366
Wielka Brytania i Irlandia: Samaritans, 116 123
Jeśli grozi ci bezpośrednie niebezpieczeństwo, zadzwoń pod lokalny numer alarmowy.

Napisy są pisane do tego filmu, nie generowane automatycznie. Jako druga ścieżka dźwiękowa dostępny jest angielski amerykański.

Pełna transkrypcja, źródła i tłumaczenia: https://theresmoretoit-channel.github.io/pl/videos/when-does-society-become-the-problem/

ROZDZIAŁY
00:00 A gdyby świat widział w tobie problem?
01:38 Kiedy własne ciało wydaje się nie takie, jak powinno
03:43 Świat dokłada swój własny ciężar
05:39 Liczby stojące za bólem
08:10 Co się dzieje, kiedy ludzie są akceptowani?
09:50 Kto ponosi odpowiedzialność?
11:11 Lustro
```

## português (Brasil) (`pt-BR`)

```
Quando a sociedade passa a ser o problema?
```

```
Imagine acordar amanhã e descobrir que o jeito como o mundo vê você virou um problema. Não porque você machucou alguém, mas porque você não corresponde às expectativas das pessoas ao seu redor.

Este vídeo mostra o que os estudos dizem sobre suicídio entre pessoas transgênero, e o que eles podem e não podem nos dizer. Um estudo dinamarquês que acompanhou a população inteira de um país ao longo de quatro décadas. A diferença entre disforia de gênero e identidade transgênero, e como a CID-11 e o manual de psiquiatria americano descrevem isso. O estresse de minoria, e como centenas de pequenas experiências podem se acumular. Uma grande pesquisa com jovens LGBTQ+ nos Estados Unidos, e o que ela encontrou quando esses jovens se sentiam aceitos. E a pergunta: pelo que a sociedade é responsável, quando não podemos eliminar toda fonte de dor de alguém, mas podemos escolher não aumentá-la?

Este é o quinto e último vídeo de uma série sobre pessoas transgênero. Os anteriores perguntavam por que de repente parece haver tantas pessoas trans, como você sabe que é trans, por que pessoas trans mudam o próprio corpo e por que é tão difícil ser trans.

SE VOCÊ ESTÁ PASSANDO POR UM MOMENTO DIFÍCIL
Você não precisa passar por isso sem apoio. Estes serviços são gratuitos e confidenciais:
Find A Helpline, apoio em mais de 175 países: https://findahelpline.com
Estados Unidos e Canadá: ligue ou mande SMS para 988
The Trevor Project, para jovens LGBTQ+ nos EUA: 1-866-488-7386, mande START por SMS para 678-678 ou use o chat em https://www.thetrevorproject.org/get-help/
Trans Lifeline, apoio entre pares feito por pessoas trans: EUA (877) 565-8860, Canadá (877) 330-6366
Reino Unido e Irlanda: Samaritans, 116 123
Se você estiver em perigo imediato, ligue para o número de emergência local.

As legendas foram escritas para este vídeo, não geradas automaticamente. Como segunda faixa de áudio está disponível o inglês americano.

Transcrição completa, fontes e traduções: https://theresmoretoit-channel.github.io/pt-br/videos/when-does-society-become-the-problem/

CAPÍTULOS
00:00 E se o mundo visse você como um problema?
01:38 Quando o seu próprio corpo parece errado
03:43 O mundo acrescenta o seu próprio peso
05:39 Os números por trás da dor
08:10 O que acontece quando as pessoas são aceitas?
09:50 Quem é responsável?
11:11 O espelho
```

## Türkçe (`tr`)

```
Toplum Ne Zaman Sorunun Kendisi Hâline Gelir?
```

```
Hayal et: yarın uyanıyorsun ve dünyanın seni görme biçiminin bir sorun hâline geldiğini fark ediyorsun. Birine zarar verdiğin için değil, çevrendeki insanların beklentilerine uymadığın için.

Bu video, araştırmaların trans insanlar arasındaki intihar hakkında ne söylediğini, bize neyi söyleyebileceğini ve neyi söyleyemeyeceğini ele alıyor. Bir ülkenin tüm nüfusunu kırk yıl boyunca izleyen bir Danimarka çalışması. Cinsiyet disforisi ile transgender kimlik arasındaki fark ve ICD-11 ile Amerikan psikiyatri el kitabının bunu nasıl tanımladığı. Azınlık stresi ve yüzlerce küçük deneyimin nasıl birikebildiği. ABD'deki LGBTQ+ gençlerle yapılan büyük bir anket ve gençler kabul gördüklerini hissettiklerinde anketin ne bulduğu. Ve bir insanın acısının her kaynağını ortadan kaldıramasak da ona bir şey eklememeyi seçebildiğimiz durumda toplumun nelerden sorumlu olduğu sorusu.

Bu, transgender insanlar hakkındaki bir serinin beşinci ve son videosu. Öncekiler, neden birdenbire bu kadar çok trans insan varmış gibi göründüğünü, trans olduğunu nasıl anlayacağını, trans insanların bedenlerini neden değiştirdiğini ve trans olmanın neden bu kadar zor olduğunu soruyordu.

ZOR BİR DÖNEMDEN GEÇİYORSAN
Bununla tek başına başa çıkmak zorunda değilsin. Bu hizmetler ücretsizdir ve gizliliğini korur:
Find A Helpline, 175'ten fazla ülkede destek: https://findahelpline.com
ABD ve Kanada: 988'i ara ya da 988'e SMS gönder
The Trevor Project, ABD'deki LGBTQ+ gençler için: 1-866-488-7386, START yazıp 678-678'e SMS gönder ya da https://www.thetrevorproject.org/get-help/ adresinden sohbet et
Trans Lifeline, trans insanların yürüttüğü akran desteği: ABD (877) 565-8860, Kanada (877) 330-6366
Birleşik Krallık ve İrlanda: Samaritans, 116 123
Acil bir tehlike altındaysan yerel acil durum numarasını ara.

Altyazılar bu video için yazıldı, otomatik olarak oluşturulmadı. İkinci ses parçası olarak Amerikan İngilizcesi de mevcut.

Metnin tamamı, kaynaklar ve çeviriler: https://theresmoretoit-channel.github.io/tr/videos/when-does-society-become-the-problem/

BÖLÜMLER
00:00 Ya dünya seni bir sorun olarak görseydi?
01:38 Kendi bedenin sana yanlış geldiğinde
03:43 Dünya da kendi yükünü ekler
05:39 Acının ardındaki sayılar
08:10 İnsanlar kabul gördüğünde ne olur?
09:50 Sorumlu kim?
11:11 Ayna
```

## українська (`uk`)

```
Коли проблемою стає суспільство?
```

```
Уяви, що завтра ти прокидаєшся і виявляєш, що те, як тебе бачить світ, стало проблемою. Не тому, що через тебе хтось постраждав, а тому, що ти не відповідаєш очікуванням людей довкола.

Це відео про те, що кажуть дослідження про самогубства серед трансгендерних людей і що вони можуть, а чого не можуть нам сказати. Данське дослідження, яке чотири десятиліття відстежувало все населення країни. Різниця між гендерною дисфорією та трансгендерною ідентичністю і те, як це описують МКХ-11 та американський психіатричний посібник. Стрес меншин і те, як сотні дрібних переживань можуть накопичуватися. Велике опитування ЛГБТК+ молоді у Сполучених Штатах і те, що воно виявило, коли молоді люди відчували, що їх приймають. І питання, за що відповідає суспільство, коли ми не можемо усунути кожне джерело чужого болю, але можемо вирішити нічого до нього не додавати.

Це п’яте й останнє відео із серії про трансгендерних людей. У попередніх відео йшлося про те, чому здається, ніби раптом стало так багато трансгендерних людей, як зрозуміти, що ти транс, чому трансгендерні люди змінюють свої тіла і чому так важко бути транс.

ЯКЩО ТОБІ ЗАРАЗ ВАЖКО
Не обов’язково проходити через це наодинці. Ці служби безкоштовні й конфіденційні:
Find A Helpline, підтримка в понад 175 країнах: https://findahelpline.com
США і Канада: зателефонуй або надішли SMS на 988
The Trevor Project, для ЛГБТК+ молоді у США: 1-866-488-7386, SMS зі словом START на 678-678 або чат на https://www.thetrevorproject.org/get-help/
Trans Lifeline, взаємопідтримка, яку надають трансгендерні люди: США (877) 565-8860, Канада (877) 330-6366
Велика Британія та Ірландія: Samaritans, 116 123
Якщо тобі загрожує безпосередня небезпека, зателефонуй на місцевий номер екстреної допомоги.

Субтитри написані для цього відео, а не згенеровані автоматично. Також доступна друга звукова доріжка — американською англійською.

Повний текст, джерела та переклади: https://theresmoretoit-channel.github.io/uk/videos/when-does-society-become-the-problem/

РОЗДІЛИ
00:00 А якби світ бачив у тобі проблему?
01:38 Коли власне тіло здається неправильним
03:43 Світ додає свій тягар
05:39 Цифри, що стоять за болем
08:10 Що відбувається, коли людей приймають?
09:50 Хто відповідальний?
11:11 Дзеркало
```

## Tiếng Việt (`vi`)

```
Khi nào xã hội trở thành vấn đề?
```

```
Hãy tưởng tượng sáng mai bạn thức dậy và phát hiện ra rằng cách thế giới nhìn bạn đã trở thành một vấn đề. Không phải vì bạn đã làm tổn thương ai, mà vì bạn không phù hợp với kỳ vọng của những người xung quanh.

Video này xem xét các nghiên cứu nói gì về tự tử ở người chuyển giới, và những gì chúng có thể và không thể cho chúng ta biết. Một nghiên cứu ở Đan Mạch đã theo dõi toàn bộ dân số của cả nước trong suốt bốn thập kỷ. Sự khác biệt giữa phiền muộn giới và bản dạng chuyển giới, và cách ICD-11 cùng cẩm nang tâm thần học của Mỹ mô tả điều đó. Căng thẳng thiểu số, và cách hàng trăm trải nghiệm nhỏ có thể cộng dồn lại. Một khảo sát lớn với người trẻ LGBTQ+ ở Hoa Kỳ, và những gì khảo sát ghi nhận khi họ cảm thấy được chấp nhận. Và câu hỏi xã hội chịu trách nhiệm về điều gì, khi chúng ta không thể xóa bỏ mọi nguồn gốc nỗi đau của một người, nhưng có thể chọn không chồng thêm vào đó.

Đây là video thứ năm và cũng là video cuối cùng trong loạt video về người chuyển giới. Các video trước đã hỏi vì sao có vẻ như đột nhiên có nhiều người chuyển giới đến vậy, làm sao bạn biết mình là người chuyển giới, vì sao người chuyển giới thay đổi cơ thể mình, và vì sao làm người chuyển giới lại khó khăn đến vậy.

NẾU BẠN ĐANG GẶP KHÓ KHĂN
Bạn không phải một mình vượt qua điều này. Các dịch vụ sau đây miễn phí và bảo mật:
Find A Helpline, hỗ trợ tại hơn 175 quốc gia: https://findahelpline.com
Hoa Kỳ và Canada: gọi hoặc nhắn tin đến 988
The Trevor Project, dành cho người trẻ LGBTQ+ ở Hoa Kỳ: 1-866-488-7386, nhắn START đến 678-678, hoặc trò chuyện tại https://www.thetrevorproject.org/get-help/
Trans Lifeline, hỗ trợ đồng đẳng do người chuyển giới điều hành: Hoa Kỳ (877) 565-8860, Canada (877) 330-6366
Vương quốc Anh và Ireland: Samaritans, 116 123
Nếu bạn đang gặp nguy hiểm tức thời, hãy gọi số khẩn cấp tại nơi bạn ở.

Phụ đề được viết riêng cho video này, không phải tạo tự động. Có thể chọn tiếng Anh Mỹ ở bản âm thanh thứ hai.

Toàn văn, nguồn và bản dịch: https://theresmoretoit-channel.github.io/vi/videos/when-does-society-become-the-problem/

CHƯƠNG
00:00 Nếu thế giới coi bạn là một vấn đề thì sao?
01:38 Khi chính cơ thể bạn khiến bạn thấy không ổn
03:43 Thế giới chồng thêm sức nặng của riêng nó
05:39 Những con số đằng sau nỗi đau
08:10 Điều gì xảy ra khi con người được chấp nhận?
09:50 Ai chịu trách nhiệm?
11:11 Tấm gương
```

## čeština (`cs`)

```
Kdy se problémem stává společnost?
```

```
Představ si, že se zítra probudíš a zjistíš, že to, jak tě svět vidí, se stalo problémem. Ne proto, že by kvůli tobě někdo trpěl, ale proto, že neodpovídáš tomu, co od tebe čekají lidé kolem.

Video se zabývá tím, co výzkum říká o sebevraždách mezi trans lidmi a co nám říct může a co ne. Dánská studie, která čtyři desetiletí sledovala celou populaci země. Rozdíl mezi genderovou dysforií a trans identitou a jak to popisuje MKN-11 a americký psychiatrický manuál. Minoritní stres a to, jak se stovky drobných zkušeností můžou sčítat. Velký průzkum mezi LGBTQ+ mladými lidmi ve Spojených státech a co zjistil, když se cítili přijímaní. A otázka, za co společnost odpovídá, když nedokážeme odstranit každý zdroj něčí bolesti, ale můžeme se rozhodnout, že k ní nebudeme nic přidávat.

Tohle je páté a poslední video ze série o transgender lidech. Ta předchozí se ptala, proč se zdá, že je najednou tolik trans lidí, jak poznáš, že jsi trans, proč trans lidé mění svá těla a proč je tak těžké být trans.

POKUD TO MÁŠ TĚŽKÉ
Nemusíš tím procházet v osamění. Tyhle služby jsou zdarma a důvěrné:
Find A Helpline, pomoc ve více než 175 zemích: https://findahelpline.com
Spojené státy a Kanada: zavolej nebo pošli SMS na 988
The Trevor Project, pro LGBTQ+ mladé lidi v USA: 1-866-488-7386, SMS se slovem START na 678-678 nebo chat na https://www.thetrevorproject.org/get-help/
Trans Lifeline, vzájemná podpora, kterou poskytují trans lidé: USA (877) 565-8860, Kanada (877) 330-6366
Spojené království a Irsko: Samaritans, 116 123
Pokud ti hrozí bezprostřední nebezpečí, zavolej na místní tísňovou linku.

Titulky jsou psané pro tohle video, ne strojový přepis. Jako druhá zvuková stopa je k dispozici americká angličtina.

Celý text, zdroje a překlady: https://theresmoretoit-channel.github.io/cs/videos/when-does-society-become-the-problem/

KAPITOLY
00:00 Co kdyby tě svět viděl jako problém?
01:38 Když ti vlastní tělo nepřipadá správné
03:43 Svět k tomu přidává vlastní tíhu
05:39 Čísla za tou bolestí
08:10 Co se stane, když je okolí přijme?
09:50 Kdo za to nese odpovědnost?
11:11 Zrcadlo
```

## español (`es`)

```
¿Cuándo pasa la sociedad a ser el problema?
```

```
Imagina que te despiertas mañana y descubres que la forma en que el mundo te ve se ha convertido en un problema. No porque hayas hecho daño a nadie, sino porque no encajas en las expectativas de la gente que te rodea.

Este vídeo analiza lo que dice la investigación sobre el suicidio entre las personas transgénero, y lo que puede y no puede decirnos. Un estudio danés que siguió a toda la población de un país a lo largo de cuatro décadas. La diferencia entre la disforia de género y la identidad transgénero, y cómo lo describen la CIE-11 y el manual de psiquiatría estadounidense. El estrés de minorías, y cómo cientos de pequeñas experiencias pueden acumularse. Una gran encuesta a jóvenes LGBTQ+ de Estados Unidos, y lo que encontró cuando esos jóvenes se sentían aceptados. Y la pregunta de cuál es la responsabilidad de la sociedad, cuando no podemos eliminar cada fuente del dolor de alguien, pero sí podemos elegir no añadirle más.

Este es el quinto y último vídeo de una serie sobre las personas transgénero. Los anteriores se preguntaban por qué parece que de repente hay tantas personas trans, cómo sabes que eres trans, por qué las personas trans cambian su cuerpo y por qué es tan difícil ser trans.

SI LO ESTÁS PASANDO MAL
No tienes que pasar por esto a solas. Estos servicios son gratuitos y confidenciales:
Find A Helpline, apoyo en más de 175 países: https://findahelpline.com
Estados Unidos y Canadá: llama o envía un SMS al 988
The Trevor Project, para jóvenes LGBTQ+ en Estados Unidos: 1-866-488-7386, envía START por SMS al 678-678 o chatea en https://www.thetrevorproject.org/get-help/
Trans Lifeline, apoyo entre iguales a cargo de personas trans: Estados Unidos (877) 565-8860, Canadá (877) 330-6366
Reino Unido e Irlanda: Samaritans, 116 123
Si estás en peligro inmediato, llama al número de emergencias de tu zona.

Los subtítulos están escritos para este vídeo, no generados automáticamente. Como segunda pista de audio está disponible el inglés americano.

Transcripción completa, fuentes y traducciones: https://theresmoretoit-channel.github.io/es/videos/when-does-society-become-the-problem/

CAPÍTULOS
00:00 ¿Y si el mundo te viera como un problema?
01:38 Cuando sientes que tu propio cuerpo está mal
03:43 El mundo añade su propio peso
05:39 Las cifras detrás del dolor
08:10 ¿Qué pasa cuando las personas son aceptadas?
09:50 ¿Quién es responsable?
11:11 El espejo
```

## svenska (`sv`)

```
När blir samhället problemet?
```

```
Tänk dig att du vaknar i morgon och upptäcker att sättet som världen ser på dig har blivit ett problem. Inte för att du har skadat någon, utan för att du inte motsvarar förväntningarna hos människorna omkring dig.

Den här videon handlar om vad forskningen säger om självmord bland transpersoner, och vad den kan och inte kan berätta för oss. En dansk studie som följde ett helt lands befolkning under fyra decennier. Skillnaden mellan könsdysfori och transidentitet, och hur ICD-11 och den amerikanska psykiatriska manualen beskriver det. Minoritetsstress, och hur hundratals små upplevelser kan samlas på hög. En stor enkät bland unga hbtq+-personer i USA, och vad den kom fram till när de kände sig accepterade. Och frågan om vad samhället har ansvar för, när vi inte kan ta bort varje källa till en människas smärta men kan välja att inte lägga till mer.

Det här är den femte och sista videon i en serie om transpersoner. De tidigare frågade varför det plötsligt verkar finnas så många transpersoner, hur du vet att du är trans, varför transpersoner förändrar sina kroppar och varför det är så svårt att vara trans.

OM DU HAR DET TUNGT
Du behöver inte gå igenom det ensam. De här tjänsterna är gratis och konfidentiella:
Find A Helpline, stöd i fler än 175 länder: https://findahelpline.com
USA och Kanada: ring eller sms:a 988
The Trevor Project, för unga hbtq+-personer i USA: 1-866-488-7386, sms:a START till 678-678 eller chatta på https://www.thetrevorproject.org/get-help/
Trans Lifeline, kamratstöd som drivs av transpersoner: USA (877) 565-8860, Kanada (877) 330-6366
Storbritannien och Irland: Samaritans, 116 123
Om du är i akut fara, ring ditt lokala nödnummer.

Undertexterna är skrivna för den här videon, inte automatgenererade. Som andra ljudspår finns amerikansk engelska.

Hela texten, källor och översättningar: https://theresmoretoit-channel.github.io/sv/videos/when-does-society-become-the-problem/

KAPITEL
00:00 Tänk om världen såg dig som ett problem?
01:38 När din egen kropp känns fel
03:43 Världen lägger på sin egen tyngd
05:39 Siffrorna bakom smärtan
08:10 Vad händer när människor blir accepterade?
09:50 Vem bär ansvaret?
11:11 Spegeln
```
