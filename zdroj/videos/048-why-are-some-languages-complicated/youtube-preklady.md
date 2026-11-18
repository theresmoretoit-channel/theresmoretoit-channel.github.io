# Lokalizované názvy a popisy — 048

Nahrává `tools/lokalizace.py` přes `videos.update(part="localizations")`.
Anglický titul a popis zůstávají v `youtube.md` a posílají se zpátky
beze změny.

```bash
python tools/lokalizace.py videos/048-why-are-some-languages-complicated --zkouska
python tools/lokalizace.py videos/048-why-are-some-languages-complicated
```

**Formát si vynucuje parser** (`bloky_z_podkladu()`): sekce jazyka je
nadpis `## <endonymum> (`<kód>`)`, uvnitř **přesně dva bloky** v trojici
zpětných apostrofů — první titul, druhý popis. Jiný počet nástroj
přeskočí s hláškou a jinak to nekřičí.

**Pořadí je podle YouTube Studia**, tedy bajtově podle UTF-8 a podle
ČESKÉHO názvu jazyka, ne abecedně podle kódu.

## Co se NEPŘEKLÁDÁ

- **anglická slova, o kterých video mluví** — `go`, `went`, `goed`,
  `wend`, `wended`. Jsou to předmět výkladu, ne text k překladu;
  přeložené by celá pasáž ztratila smysl
- **vlastní jména** — Beowulf, Cotton MS Vitellius A XV
- **časy kapitol** na vteřinu — jsou to tytéž okamžiky ve všech jazycích
- **tagy** — YouTube je per-jazyk nemá

Názvy kapitol a popisek kreditů se naopak **překládají**.

## Kontrola čísel

Video velká čísla skoro nemá, takže past s *billion* × *trillion* tu
nehrozí. Přesto se každé přepsalo vědomě:

| anglicky | co to je | pozor |
|---|---|---|
| five thousand years | 5 000 let | |
| three thousand years | 3 000 let | |
| several hundred million | ~10⁸ | de `mehrere hundert Millionen`, fr `plusieurs centaines de millions` |
| seventy-three per cent | 73 % | vymyšlené číslo, je to vtip o měření |
| six, five, seven (pády) | 6 / 5 / 7 | musí zůstat v tomhle pořadí — je to tvrzení o tom, že se počítají různě |

## Věta o americké stopě

Druhý odstavec od konce (`An American English audio track…`) platí,
**jen když se stopa doopravdy nahraje do Studia**. Když ne, vypusť ho
ze všech třinácti sekcí i z anglického popisu.

## suomi (`fi`)

```
Miksi jotkin kielet ovat niin mutkikkaita?
```

```
Viisituhatta vuotta sitten ei ollut sähköä, kirjoja eikä kouluja. Meidän mitoillamme tavattoman yksinkertainen elämä — voisi siis odottaa tavattoman yksinkertaista kieltä. Latina, muinaisenglanti ja muinaisnorja kertovat toista. Kaikilla oli kieliopillinen koneisto, jonka nykyenglanti on enimmäkseen menettänyt.

Vanhaa kieltä ei tarvita nähdäkseen, miten kummalliseksi tämä käy. Englanti sanoo "go" ja "went", eikä "went" ole koskaan kuulunut "go"-verbiin. Se oli toisen verbin, "wend", mennyt aika. Jossain vaiheessa englanti otti hiljaa toisen verbin menneen ajan ja antoi sen toiselle. Kukaan ei äänestänyt siitä. Kukaan ei kirjannut sitä säännöksi. Se tapahtui, ja sitten se jäi.

Tämä video kertoo, miksi se on tavallista eikä outoa. Miten yhdestä kielestä tulee monta ilman että kukaan päättää perustaa uuden. Miksi sijapäätteiden menettäminen ei tehnyt englannista yksinkertaisempaa, vaan siirsi työn sanajärjestykseen ja pieneen apuverbien armeijaan. Miksi kysymyksen "kuinka monimutkainen tämä kieli on" takana ei ole yhtä lukua. Ja miksi kantaindoeurooppa — kieli, josta kukaan ei ole löytänyt tekstiä — näyttää silti hienosyiseltä, kun kielentutkijat rekonstruoivat sen vertaamalla siitä syntyneitä kieliä.

Sitten se kohta, jonka ihmiset hyväksyvät vaikeimmin. Suuntaa ei ole. Slaavilaiset kielet näyttävät sen selvästi: useimmat säilyttivät rikkaan sijajärjestelmän, kun taas bulgaria menetti sen substantiiveista lähes kokonaan ja kasvatti tilalle jotain muuta, määräisen artikkelin sanan loppuun. Sama esi-isä, vastakkaiset suunnat, eikä kumpikaan ole päivitys.

Tekstitykset on kirjoitettu tätä videota varten, niitä ei ole luotu automaattisesti. Amerikanenglantilainen ääniraita on saatavilla toisena ääniraitana.

Koko teksti, lähteet ja käännökset: https://theresmoretoit-channel.github.io/fi/videos/why-are-some-languages-complicated/

Luvut
00:00 Yksinkertainen elämä, mutkikas kieli
00:36 Miksei "goed"?
01:31 Kieli ei ole tekniikkaa
02:25 Miten yhdestä kielestä tulee monta
03:18 Miksi ne eivät siis kulu helpoiksi?
03:52 Koira ja mies
04:22 Pieni apuverbien armeija
04:49 Monimutkaisuus muuttaa
05:03 Mittaria ei ole
05:49 Takaisin muinaiseen ihmiseen
06:09 Rekonstruktio, ei todiste
06:27 Yhteiskunta ilman tekniikkaa
06:45 Näitkö sen itse vai kerrottiinko sinulle?
07:19 Vähemmän insinöörityötä
08:04 Suuntaa ei ole
08:15 Slaavilainen esimerkki
08:47 Ei koskaan tikapuut
09:08 Miksi odotimme yksinkertaista?

KUVALÄHTEET
Beowulf, Cotton MS Vitellius A XV, f. 132r — public domain
Wikimedia Commonsin kautta
```

## français (`fr`)

```
Pourquoi certaines langues sont-elles si compliquées ?
```

```
Il y a cinq mille ans, il n'y avait ni électricité, ni livres, ni écoles. Selon nos critères, une vie extraordinairement simple — on s'attendrait donc à une langue tout aussi simple. Le latin, le vieil anglais et le vieux norrois disent le contraire. Toutes avaient une machinerie grammaticale que l'anglais d'aujourd'hui a largement perdue.

Nul besoin d'une langue ancienne pour voir à quel point cela devient étrange. L'anglais dit « go » et « went », et « went » n'a jamais appartenu à « go ». C'était le passé d'un autre verbe, « wend ». À un moment, l'anglais a pris en silence le passé de l'un et l'a donné à l'autre. Personne n'a voté. Personne ne l'a écrit comme règle. C'est arrivé, et c'est resté.

Cette vidéo explique pourquoi c'est ordinaire et non bizarre. Comment une langue en devient plusieurs sans que personne décide d'en fonder une nouvelle. Pourquoi la perte des désinences casuelles n'a pas rendu l'anglais plus simple, mais a déplacé le travail vers l'ordre des mots et vers une petite armée d'auxiliaires. Pourquoi « quelle est la complexité de cette langue » n'a aucun chiffre unique derrière. Et pourquoi l'indo-européen commun — une langue dont personne n'a jamais trouvé de texte — paraît malgré tout élaboré quand les linguistes le reconstruisent en comparant les langues qui en sont issues.

Puis la partie que les gens acceptent le plus mal. Il n'y a aucune direction. Les langues slaves le montrent clairement : la plupart ont gardé des cas riches, tandis que le bulgare les a presque entièrement perdus sur les noms et s'est fait pousser autre chose, un article défini collé à la fin du mot. Le même ancêtre, des directions opposées, et aucune des deux n'est la mise à jour.

Les sous-titres sont écrits pour cette vidéo, ils ne sont pas générés automatiquement. Une piste audio en anglais américain est disponible comme deuxième piste audio.

Transcription complète, sources et traductions : https://theresmoretoit-channel.github.io/fr/videos/why-are-some-languages-complicated/

Chapitres
00:00 Une vie simple, une langue compliquée
00:36 Pourquoi pas « goed » ?
01:31 La langue n'est pas une technique
02:25 Comment une langue en devient plusieurs
03:18 Pourquoi ne s'usent-elles pas ?
03:52 Le chien et l'homme
04:22 Une petite armée d'auxiliaires
04:49 La complexité déménage
05:03 Il n'y a pas de cadran
05:49 Retour à notre humain d'alors
06:09 Une reconstruction, pas un témoignage
06:27 Une société sans technique
06:45 L'avez-vous vu, ou vous l'a-t-on dit ?
07:19 Moins de l'ingénierie
08:04 Il n'y a aucune direction
08:15 L'exemple slave
08:47 Jamais une échelle
09:08 Pourquoi en attendions-nous une simple ?

CRÉDITS IMAGES
Beowulf, Cotton MS Vitellius A XV, f. 132r — domaine public
via Wikimedia Commons
```

## Bahasa Indonesia (`id`)

```
Mengapa Sebagian Bahasa Begitu Rumit?
```

```
Lima ribu tahun lalu tidak ada listrik, buku, atau sekolah. Menurut ukuran kita, hidup yang luar biasa sederhana — jadi Anda mungkin mengharapkan bahasa yang sama sederhananya. Latin, Inggris Kuno, dan Norse Kuno berkata lain. Semuanya punya mesin tata bahasa yang sebagian besar sudah hilang dari bahasa Inggris masa kini.

Anda tak butuh bahasa kuno untuk melihat betapa anehnya ini. Bahasa Inggris berkata "go" dan "went", padahal "went" tak pernah milik "go". Itu bentuk lampau kata kerja lain, "wend". Pada suatu titik bahasa Inggris diam-diam mengambil bentuk lampau yang satu dan menyerahkannya kepada yang lain. Tak ada yang memungutnya. Tak ada yang menuliskannya sebagai aturan. Itu terjadi, lalu bertahan.

Video ini tentang mengapa hal itu biasa, bukan ganjil. Bagaimana satu bahasa menjadi banyak tanpa ada yang memutuskan mendirikan bahasa baru. Mengapa hilangnya akhiran kasus tidak membuat bahasa Inggris lebih sederhana, melainkan memindahkan pekerjaannya ke urutan kata dan ke pasukan kecil kata kerja bantu. Mengapa pertanyaan "seberapa rumit bahasa ini" tak punya satu angka pun di baliknya. Dan mengapa Proto-Indo-Eropa — bahasa yang teksnya tak pernah ditemukan siapa pun — tetap tampak rumit ketika ahli bahasa merekonstruksinya dengan membandingkan bahasa-bahasa yang lahir darinya.

Lalu bagian yang paling sulit diterima orang. Tidak ada arah. Bahasa-bahasa Slavia menunjukkannya dengan jelas: sebagian besar menjaga kasus yang kaya, sementara bahasa Bulgaria kehilangannya pada kata benda hampir sepenuhnya dan menumbuhkan sesuatu yang lain, kata sandang tentu yang menempel di ujung kata. Leluhur yang sama, arah yang berlawanan, dan tak satu pun dari keduanya merupakan peningkatan.

Takarir ditulis khusus untuk video ini, bukan dibuat otomatis. Trek audio bahasa Inggris Amerika tersedia sebagai trek audio kedua.

Transkrip lengkap, sumber, dan terjemahan: https://theresmoretoit-channel.github.io/id/videos/why-are-some-languages-complicated/

Bab
00:00 Hidup sederhana, bahasa yang rumit
00:36 Mengapa bukan "goed"?
01:31 Bahasa bukan teknologi
02:25 Bagaimana satu bahasa menjadi banyak
03:18 Lalu mengapa tidak terkikis jadi mudah?
03:52 Anjing dan lelaki itu
04:22 Pasukan kecil kata kerja bantu
04:49 Kerumitan pindah rumah
05:03 Tidak ada panel ukur
05:49 Kembali ke manusia purba tadi
06:09 Rekonstruksi, bukan catatan
06:27 Masyarakat tanpa teknologi
06:45 Anda melihatnya sendiri atau diberi tahu?
07:19 Lebih sedikit rekayasa
08:04 Tidak ada arah
08:15 Contoh Slavia
08:47 Tak pernah berupa tangga
09:08 Mengapa kita mengharapkan yang sederhana?

KREDIT GAMBAR
Beowulf, Cotton MS Vitellius A XV, f. 132r — domain publik
via Wikimedia Commons
```

## italiano (`it`)

```
Perché alcune lingue sono così complicate?
```

```
Cinquemila anni fa non c'era elettricità, non c'erano libri né scuole. Per i nostri criteri, una vita straordinariamente semplice — ci si aspetterebbe quindi una lingua altrettanto semplice. Il latino, l'inglese antico e il norreno dicono il contrario. Tutte avevano un macchinario grammaticale che l'inglese di oggi ha in gran parte perso.

Non serve una lingua antica per vedere quanto diventa strano. L'inglese dice «go» e «went», e «went» non è mai appartenuto a «go». Era il passato di un altro verbo, «wend». A un certo punto l'inglese ha preso in silenzio il passato di uno e l'ha consegnato all'altro. Nessuno ha votato. Nessuno l'ha scritto come regola. È successo, e poi è rimasto.

Questo video spiega perché è normale e non bizzarro. Come una lingua ne diventa molte senza che nessuno decida di fondarne una nuova. Perché la perdita delle desinenze di caso non ha reso l'inglese più semplice, ma ha spostato il lavoro sull'ordine delle parole e su un piccolo esercito di verbi ausiliari. Perché dietro alla domanda «quanto è complessa questa lingua» non c'è un numero unico. E perché il protoindoeuropeo — una lingua di cui nessuno ha mai trovato un testo — appare comunque elaborato quando i linguisti lo ricostruiscono confrontando le lingue che ne sono uscite.

Poi la parte che si accetta più a fatica. Non c'è nessuna direzione. Le lingue slave lo mostrano con chiarezza: la maggior parte ha tenuto casi ricchi, mentre il bulgaro li ha persi sui nomi quasi del tutto e gli è cresciuta un'altra cosa, un articolo determinativo attaccato alla fine della parola. Lo stesso antenato, direzioni opposte, e nessuna delle due è l'aggiornamento.

I sottotitoli sono scritti per questo video, non generati automaticamente. È disponibile una traccia audio in inglese americano come seconda traccia.

Trascrizione completa, fonti e traduzioni: https://theresmoretoit-channel.github.io/it/videos/why-are-some-languages-complicated/

Capitoli
00:00 Una vita semplice, una lingua complicata
00:36 Perché non «goed»?
01:31 La lingua non è tecnologia
02:25 Come una lingua ne diventa molte
03:18 Perché allora non si consumano?
03:52 Il cane e l'uomo
04:22 Un piccolo esercito di ausiliari
04:49 La complessità trasloca
05:03 Non esiste un quadrante
05:49 Di nuovo al nostro uomo di allora
06:09 Una ricostruzione, non una testimonianza
06:27 Una società senza tecnologia
06:45 L'avete visto o ve l'hanno raccontato?
07:19 Meno ingegneria
08:04 Non c'è nessuna direzione
08:15 L'esempio slavo
08:47 Non è mai stata una scala
09:08 Perché ne aspettavamo una semplice?

CREDITI IMMAGINI
Beowulf, Cotton MS Vitellius A XV, f. 132r — pubblico dominio
via Wikimedia Commons
```

## Deutsch (`de`)

```
Warum sind manche Sprachen so kompliziert?
```

```
Vor fünftausend Jahren gab es keinen Strom, keine Bücher und keine Schulen. Nach unseren Maßstäben ein außerordentlich einfaches Leben — man würde also eine außerordentlich einfache Sprache erwarten. Latein, Altenglisch und Altnordisch sagen etwas anderes. Alle hatten grammatische Maschinerie, die das heutige Englisch größtenteils verloren hat.

Man braucht keine alte Sprache, um zu sehen, wie seltsam das wird. Das Englische sagt „go" und „went", und „went" hat nie zu „go" gehört. Es war die Vergangenheit eines anderen Verbs, „wend". Irgendwann nahm das Englische still die Vergangenheit des einen und gab sie dem anderen. Niemand hat darüber abgestimmt. Niemand hat es als Regel aufgeschrieben. Es geschah, und dann blieb es.

In diesem Video geht es darum, warum das gewöhnlich ist und nicht sonderbar. Wie aus einer Sprache viele werden, ohne dass jemand beschließt, eine neue zu gründen. Warum der Verlust der Kasusendungen das Englische nicht einfacher gemacht hat, sondern die Arbeit in die Wortstellung und in eine kleine Armee von Hilfsverben verschoben hat. Warum hinter der Frage „wie komplex ist diese Sprache" keine einzelne Zahl steht. Und warum das Urindogermanische — eine Sprache, in der niemand je einen Text gefunden hat — trotzdem aufwendig aussieht, wenn Sprachwissenschaftler es aus dem Vergleich seiner Nachfahren rekonstruieren.

Und dann der Teil, den Menschen am schwersten annehmen. Es gibt keine Richtung. Die slawischen Sprachen zeigen es deutlich: Die meisten behielten reiche Kasus, während das Bulgarische sie bei den Substantiven fast ganz verlor und stattdessen etwas anderes bekam, einen bestimmten Artikel, der hinten am Wort klebt. Derselbe Vorfahr, entgegengesetzte Richtungen, und keine von beiden ist das Upgrade.

Die Untertitel wurden für dieses Video geschrieben, nicht automatisch erzeugt. Eine amerikanisch-englische Tonspur ist als zweite Tonspur verfügbar.

Vollständiger Text, Quellen und Übersetzungen: https://theresmoretoit-channel.github.io/de/videos/why-are-some-languages-complicated/

Kapitel
00:00 Ein einfaches Leben, eine komplizierte Sprache
00:36 Warum nicht „goed"?
01:31 Sprache ist keine Technik
02:25 Wie aus einer Sprache viele werden
03:18 Warum schleifen sie sich nicht ab?
03:52 Der Hund und der Mann
04:22 Eine kleine Armee von Hilfsverben
04:49 Komplexität zieht um
05:03 Es gibt keine Anzeige
05:49 Zurück zu unserem Menschen von damals
06:09 Eine Rekonstruktion, kein Zeugnis
06:27 Eine Gesellschaft ohne Technik
06:45 Selbst gesehen oder erzählt bekommen?
07:19 Weniger Ingenieurskunst
08:04 Es gibt keine Richtung
08:15 Das slawische Beispiel
08:47 Nie eine Leiter
09:08 Warum erwarteten wir eine einfache?

BILDNACHWEIS
Beowulf, Cotton MS Vitellius A XV, f. 132r — gemeinfrei
über Wikimedia Commons
```

## polski (`pl`)

```
Dlaczego niektóre języki są tak skomplikowane?
```

```
Pięć tysięcy lat temu nie było prądu, książek ani szkół. Według naszych miar życie nadzwyczaj proste — można by więc oczekiwać równie prostego języka. Łacina, staroangielski i staronordycki mówią co innego. Wszystkie miały maszynerię gramatyczną, którą dzisiejszy angielski w dużej mierze utracił.

Nie trzeba dawnego języka, żeby zobaczyć, jak dziwnie to wygląda. Angielski mówi „go" i „went", a „went" nigdy nie należało do „go". To był czas przeszły innego czasownika, „wend". W pewnym momencie angielski po cichu wziął czas przeszły jednego i oddał go drugiemu. Nikt nad tym nie głosował. Nikt nie zapisał tego jako reguły. Stało się, a potem zostało.

Ten film jest o tym, dlaczego to zwyczajne, a nie dziwaczne. Jak z jednego języka robi się wiele, choć nikt nie postanawia zakładać nowego. Dlaczego utrata końcówek przypadków nie uprościła angielskiego, tylko przeniosła pracę na szyk i na małą armię czasowników posiłkowych. Dlaczego za pytaniem „jak złożony jest ten język" nie stoi żadna jedna liczba. I dlaczego praindoeuropejski — język, w którym nikt nigdy nie znalazł tekstu — i tak wygląda na wyszukany, kiedy językoznawcy odtwarzają go, porównując języki, które z niego wyszły.

A potem część, którą najtrudniej przyjąć. Nie ma żadnego kierunku. Języki słowiańskie pokazują to wyraźnie: większość zachowała bogatą odmianę, podczas gdy bułgarski stracił ją w rzeczownikach niemal całkowicie i wyrosło mu coś innego, rodzajnik określony doklejony na końcu wyrazu. Ten sam przodek, przeciwne kierunki, i żaden z nich nie jest ulepszeniem.

Napisy zostały napisane do tego filmu, nie wygenerowane automatycznie. Dostępna jest ścieżka dźwiękowa w amerykańskim angielskim jako druga ścieżka.

Pełna transkrypcja, źródła i tłumaczenia: https://theresmoretoit-channel.github.io/pl/videos/why-are-some-languages-complicated/

Rozdziały
00:00 Proste życie, skomplikowany język
00:36 Dlaczego nie „goed"?
01:31 Język to nie technika
02:25 Jak z jednego języka robi się wiele
03:18 Dlaczego więc się nie ścierają?
03:52 Pies i człowiek
04:22 Mała armia czasowników posiłkowych
04:49 Złożoność się przeprowadza
05:03 Nie ma żadnego wskaźnika
05:49 Z powrotem do naszego dawnego człowieka
06:09 Rekonstrukcja, nie świadectwo
06:27 Społeczeństwo bez techniki
06:45 Widziałeś to sam czy ktoś ci powiedział?
07:19 Mniej inżynierii
08:04 Nie ma żadnego kierunku
08:15 Przykład słowiański
08:47 To nigdy nie była drabina
09:08 Dlaczego spodziewaliśmy się prostego?

ŹRÓDŁA OBRAZÓW
Beowulf, Cotton MS Vitellius A XV, f. 132r — domena publiczna
przez Wikimedia Commons
```

## português (Brasil) (`pt-BR`)

```
Por que algumas línguas são tão complicadas?
```

```
Há cinco mil anos não havia eletricidade, livros nem escolas. Pelos nossos padrões, uma vida extraordinariamente simples — seria de esperar, então, uma língua igualmente simples. O latim, o inglês antigo e o nórdico antigo dizem o contrário. Todos tinham um maquinário gramatical que o inglês de hoje em grande parte perdeu.

Não é preciso uma língua antiga para ver como isso fica estranho. O inglês diz “go” e “went”, e “went” nunca pertenceu a “go”. Era o passado de um outro verbo, “wend”. Em algum momento o inglês pegou em silêncio o passado de um e entregou ao outro. Ninguém votou nisso. Ninguém escreveu como regra. Aconteceu, e depois ficou.

Este vídeo é sobre por que isso é comum, e não esquisito. Como uma língua vira muitas sem que ninguém decida fundar uma nova. Por que a perda das desinências de caso não deixou o inglês mais simples, e sim mudou o trabalho para a ordem das palavras e para um pequeno exército de verbos auxiliares. Por que a pergunta “quão complexa é esta língua” não tem um único número por trás. E por que o protoindo-europeu — uma língua da qual ninguém jamais achou um texto — mesmo assim parece elaborado quando os linguistas o reconstroem comparando as línguas que saíram dele.

E então a parte que as pessoas mais custam a aceitar. Não existe direção. As línguas eslavas mostram isso com clareza: a maioria manteve casos ricos, enquanto o búlgaro os perdeu nos substantivos quase por completo e lhe nasceu outra coisa, um artigo definido grudado no fim da palavra. O mesmo ancestral, direções opostas, e nenhuma das duas é a melhoria.

As legendas foram escritas para este vídeo, não geradas automaticamente. Há uma trilha de áudio em inglês americano disponível como segunda trilha.

Transcrição completa, fontes e traduções: https://theresmoretoit-channel.github.io/pt-br/videos/why-are-some-languages-complicated/

Capítulos
00:00 Vida simples, língua complicada
00:36 Por que não “goed”?
01:31 Língua não é tecnologia
02:25 Como uma língua vira muitas
03:18 Então por que não se desgastam?
03:52 O cachorro e o homem
04:22 Um pequeno exército de auxiliares
04:49 A complexidade muda de casa
05:03 Não existe mostrador
05:49 De volta ao nosso humano de então
06:09 Uma reconstrução, não um registro
06:27 Uma sociedade sem tecnologia
06:45 Você viu ou alguém lhe contou?
07:19 Menos engenharia
08:04 Não existe direção
08:15 O exemplo eslavo
08:47 Nunca foi uma escada
09:08 Por que esperávamos uma simples?

CRÉDITOS DAS IMAGENS
Beowulf, Cotton MS Vitellius A XV, f. 132r — domínio público
via Wikimedia Commons
```

## Türkçe (`tr`)

```
Bazı diller neden bu kadar karmaşık?
```

```
Beş bin yıl önce elektrik, kitap ve okul yoktu. Bizim ölçülerimizle son derece yalın bir hayat — o halde son derece yalın bir dil beklersiniz. Latince, Eski İngilizce ve Eski İskandinavca başka şey söylüyor. Hepsinde, bugünkü İngilizcenin büyük ölçüde yitirdiği bir dilbilgisi makinesi vardı.

Bunun ne kadar tuhaflaştığını görmek için eski bir dile gerek yok. İngilizce "go" ve "went" diyor, oysa "went" hiçbir zaman "go"nun olmadı. Başka bir fiilin, "wend"in geçmiş zamanıydı. Bir noktada İngilizce sessizce birinin geçmiş zamanını alıp öbürüne verdi. Kimse bunu oylamadı. Kimse bunu kural diye yazmadı. Oldu, sonra da kaldı.

Bu video bunun neden tuhaf değil olağan olduğunu anlatıyor. Kimse yeni bir dil kurmaya karar vermeden bir dilin nasıl pek çok dile dönüştüğünü. Ad çekim eklerinin yitmesinin İngilizceyi neden sadeleştirmediğini, işi sözcük sırasına ve küçük bir yardımcı fiil ordusuna kaydırdığını. "Bu dil ne kadar karmaşık" sorusunun ardında neden tek bir sayının bulunmadığını. Ve hiç kimsenin metnini bulamadığı Ana Hint-Avrupa dilinin, dilbilimciler onu soyundan gelen dilleri karşılaştırarak yeniden kurduğunda neden yine de ayrıntılı göründüğünü.

Sonra da insanların kabul etmekte en çok zorlandığı kısım. Hiçbir yön yok. Slav dilleri bunu açıkça gösteriyor: çoğu zengin ad çekimini korudu, Bulgarca ise onu adlarda neredeyse tümüyle yitirdi ve yerine başka bir şey büyüttü, sözcüğün sonuna yapışan bir belirtme tanımlığı. Aynı ata, karşıt yönler ve ikisinden hiçbiri yükseltme değil.

Altyazılar bu video için yazıldı, otomatik olarak üretilmedi. İkinci ses parçası olarak Amerikan İngilizcesi ses parçası mevcuttur.

Metnin tamamı, kaynaklar ve çeviriler: https://theresmoretoit-channel.github.io/tr/videos/why-are-some-languages-complicated/

Bölümler
00:00 Yalın bir hayat, karmaşık bir dil
00:36 Neden "goed" değil?
01:31 Dil teknoloji değildir
02:25 Bir dil nasıl pek çok dile dönüşür
03:18 Peki neden aşınıp kolaylaşmıyorlar?
03:52 Köpek ve adam
04:22 Küçük bir yardımcı fiil ordusu
04:49 Karmaşıklık ev değiştirir
05:03 Bir gösterge yok
05:49 O çok eski insana geri dönüş
06:09 Bir yeniden kurma, bir belge değil
06:27 Teknolojisi olmayan bir toplum
06:45 Kendiniz mi gördünüz, size mi anlattılar?
07:19 Daha az mühendislik
08:04 Hiçbir yön yok
08:15 Slav örneği
08:47 Hiçbir zaman merdiven değildi
09:08 Neden yalın bir dil bekledik?

GÖRSEL KAYNAKLARI
Beowulf, Cotton MS Vitellius A XV, f. 132r — kamu malı
Wikimedia Commons aracılığıyla
```

## українська (`uk`)

```
Чому деякі мови такі складні?
```

```
П'ять тисяч років тому не було ні електрики, ні книжок, ні шкіл. За нашими мірками надзвичайно просте життя — отже, можна було б чекати так само простої мови. Латина, давньоанглійська та давньоскандинавська кажуть інше. Усі вони мали граматичний механізм, який сучасна англійська здебільшого втратила.

Щоб побачити, як це дивно, давньої мови не потрібно. Англійська каже «go» і «went», а «went» ніколи не належало до «go». Це був минулий час іншого дієслова, «wend». Колись англійська тихо взяла минулий час одного й віддала його другому. Ніхто за це не голосував. Ніхто не записав цього як правило. Сталося, а потім лишилося.

Це відео про те, чому це звичайне, а не дивне. Як з однієї мови постає багато, хоч ніхто не вирішує засновувати нову. Чому втрата відмінкових закінчень не зробила англійську простішою, а перенесла роботу на порядок слів і на маленьку армію допоміжних дієслів. Чому за питанням «наскільки складна ця мова» не стоїть жодного одного числа. І чому праіндоєвропейська — мова, тексту якої ніхто ніколи не знайшов, — усе одно виглядає складною, коли мовознавці відтворюють її, порівнюючи мови, що з неї вийшли.

А потім частина, яку люди приймають найважче. Жодного напрямку немає. Слов'янські мови показують це виразно: більшість зберегла багату відміну, тоді як болгарська втратила її в іменниках майже цілком і виросло в неї щось інше — означений артикль, приліплений у кінці слова. Той самий предок, протилежні напрямки, і жоден із них не є вдосконаленням.

Субтитри написані для цього відео, а не згенеровані автоматично. Доступна доріжка американською англійською як друга звукова доріжка.

Повний текст, джерела та переклади: https://theresmoretoit-channel.github.io/uk/videos/why-are-some-languages-complicated/

Розділи
00:00 Просте життя, складна мова
00:36 Чому не «goed»?
01:31 Мова — не техніка
02:25 Як з однієї мови постає багато
03:18 То чому ж вони не стираються?
03:52 Пес і чоловік
04:22 Маленька армія допоміжних дієслів
04:49 Складність переїжджає
05:03 Жодної шкали немає
05:49 Назад до нашої давньої людини
06:09 Реконструкція, а не свідчення
06:27 Суспільство без техніки
06:45 Ви бачили самі чи вам розповіли?
07:19 Менше інженерії
08:04 Жодного напрямку немає
08:15 Слов'янський приклад
08:47 Це ніколи не було драбиною
09:08 Чому ми чекали простої?

ДЖЕРЕЛА ЗОБРАЖЕНЬ
Beowulf, Cotton MS Vitellius A XV, f. 132r — суспільне надбання
через Wikimedia Commons
```

## Tiếng Việt (`vi`)

```
Vì sao một số ngôn ngữ lại phức tạp đến thế?
```

```
Năm nghìn năm trước không có điện, không có sách, không có trường học. Theo tiêu chuẩn của chúng ta, một cuộc sống vô cùng đơn giản — vậy hẳn bạn sẽ chờ đợi một ngôn ngữ cũng đơn giản như thế. Tiếng Latinh, tiếng Anh cổ và tiếng Bắc Âu cổ nói điều ngược lại. Tất cả đều có bộ máy ngữ pháp mà tiếng Anh hôm nay phần lớn đã mất.

Bạn không cần một ngôn ngữ cổ để thấy chuyện này lạ đến đâu. Tiếng Anh nói "go" và "went", mà "went" chưa từng thuộc về "go". Đó là quá khứ của một động từ khác, "wend". Đến một lúc nào đó tiếng Anh lặng lẽ lấy quá khứ của từ này rồi trao cho từ kia. Không ai bỏ phiếu. Không ai viết nó thành quy tắc. Nó xảy ra, rồi nó ở lại.

Video này nói về việc vì sao điều đó là bình thường chứ không kỳ quặc. Vì sao một ngôn ngữ trở thành nhiều ngôn ngữ mà không ai quyết định lập ra cái mới. Vì sao việc mất đuôi cách không làm tiếng Anh đơn giản hơn, mà chuyển việc ấy sang trật tự từ và sang một đạo quân nhỏ các trợ động từ. Vì sao câu hỏi "ngôn ngữ này phức tạp đến mức nào" không có một con số duy nhất đứng sau. Và vì sao tiếng Ấn-Âu nguyên thủy — ngôn ngữ mà chưa ai từng tìm thấy văn bản — vẫn trông rất tinh vi khi các nhà ngôn ngữ học phục dựng nó bằng cách so sánh những ngôn ngữ sinh ra từ nó.

Rồi đến phần người ta khó chấp nhận nhất. Không có hướng nào cả. Các ngôn ngữ Slav cho thấy rõ điều đó: phần lớn giữ được hệ cách phong phú, trong khi tiếng Bulgaria mất nó ở danh từ gần như hoàn toàn và mọc lên thứ khác, một mạo từ xác định dính ở cuối từ. Cùng một tổ tiên, hai hướng ngược nhau, và không hướng nào là bản nâng cấp.

Phụ đề được viết riêng cho video này, không phải tạo tự động. Có bản âm thanh tiếng Anh Mỹ dưới dạng bản âm thanh thứ hai.

Toàn văn, nguồn và bản dịch: https://theresmoretoit-channel.github.io/vi/videos/why-are-some-languages-complicated/

Các chương
00:00 Đời sống giản dị, ngôn ngữ phức tạp
00:36 Sao không phải "goed"?
01:31 Ngôn ngữ không phải công nghệ
02:25 Một ngôn ngữ thành nhiều ngôn ngữ ra sao
03:18 Vậy sao chúng không mòn thành đơn giản?
03:52 Con chó và người đàn ông
04:22 Một đạo quân nhỏ các trợ động từ
04:49 Sự phức tạp chuyển nhà
05:03 Không có mặt đồng hồ nào
05:49 Trở lại với con người thuở xưa
06:09 Một phục dựng, không phải chứng tích
06:27 Một xã hội không công nghệ
06:45 Bạn tận mắt thấy hay nghe kể lại?
07:19 Bớt giống kỹ thuật
08:04 Không có hướng nào cả
08:15 Ví dụ Slav
08:47 Chưa bao giờ là một cái thang
09:08 Vì sao ta chờ đợi một thứ giản dị?

NGUỒN HÌNH ẢNH
Beowulf, Cotton MS Vitellius A XV, f. 132r — phạm vi công cộng
qua Wikimedia Commons
```

## čeština (`cs`)

```
Proč jsou některé jazyky tak složité?
```

```
Před pěti tisíci lety nebyla elektřina, knihy ani školy. Na naše poměry mimořádně prostý život — čekali byste tedy mimořádně prostý jazyk. Latina, stará angličtina a stará norština říkají něco jiného. Všechny měly gramatické ústrojí, které dnešní angličtina většinou ztratila.

K tomu, abyste viděli, jak je to zvláštní, není potřeba starý jazyk. Angličtina říká „go" a „went", a „went" k „go" nikdy nepatřilo. Byl to minulý čas jiného slovesa, „wend". V jednu chvíli angličtina tiše vzala minulý čas jednoho z nich a přidělila ho tomu druhému. Nikdo o tom nehlasoval. Nikdo to nesepsal jako pravidlo. Stalo se to a pak to zůstalo.

Tohle video je o tom, proč je to běžné, a ne podivné. Jak se z jednoho jazyka stane mnoho, aniž by někdo rozhodl založit nový. Proč ztráta pádových koncovek angličtinu nezjednodušila, nýbrž přesunula tu práci do slovosledu a do malé armády pomocných sloves. Proč za otázkou „jak složitý je tenhle jazyk" nestojí žádné jediné číslo. A proč praindoevropština — jazyk, v němž nikdo nikdy nenašel text — přesto vypadá propracovaně, když ji lingvisté rekonstruují porovnáním jazyků, které z ní vzešly.

A pak ta část, kterou lidé přijímají nejhůř. Žádný směr neexistuje. Slovanské jazyky to ukazují jasně: většina si udržela bohaté skloňování, kdežto bulharština ho u jmen skoro úplně ztratila a vyrostlo jí místo toho něco jiného, určitý člen přilepený na konec slova. Týž předek, opačné směry, a ani jeden z nich není vylepšení.

Titulky jsou k tomuhle videu napsané, ne vygenerované automaticky. Jako druhá zvuková stopa je k dispozici americká angličtina.

Celý text, zdroje a překlady: https://theresmoretoit-channel.github.io/cs/videos/why-are-some-languages-complicated/

Kapitoly
00:00 Prostý život, složitý jazyk
00:36 Proč ne „goed"?
01:31 Jazyk není technologie
02:25 Jak se z jednoho jazyka stane mnoho
03:18 Proč se tedy neobrousí?
03:52 Pes a člověk
04:22 Malá armáda pomocných sloves
04:49 Složitost se stěhuje
05:03 Žádný ciferník neexistuje
05:49 Zpátky k našemu dávnému člověku
06:09 Rekonstrukce, ne záznam
06:27 Společnost bez techniky
06:45 Viděli jste to, nebo vám to řekli?
07:19 Míň inženýrství
08:04 Žádný směr neexistuje
08:15 Slovanský příklad
08:47 Nikdy to nebyl žebřík
09:08 Proč jsme čekali jednoduchý?

ZDROJE OBRÁZKŮ
Beowulf, Cotton MS Vitellius A XV, f. 132r — volné dílo
přes Wikimedia Commons
```

## español (`es`)

```
¿Por qué algunas lenguas son tan complicadas?
```

```
Hace cinco mil años no había electricidad, ni libros, ni escuelas. Según nuestros criterios, una vida extraordinariamente simple — cabría esperar entonces una lengua igual de simple. El latín, el inglés antiguo y el nórdico antiguo dicen lo contrario. Todas tenían una maquinaria gramatical que el inglés de hoy casi ha perdido.

No hace falta una lengua antigua para ver lo raro que se pone esto. El inglés dice «go» y «went», y «went» nunca fue de «go». Era el pasado de otro verbo, «wend». En algún momento el inglés tomó en silencio el pasado de uno y se lo entregó al otro. Nadie lo votó. Nadie lo escribió como regla. Ocurrió, y luego se quedó.

Este vídeo trata de por qué eso es corriente y no extraño. Cómo una lengua se convierte en muchas sin que nadie decida fundar una nueva. Por qué perder las desinencias de caso no simplificó el inglés, sino que trasladó el trabajo al orden de palabras y a un pequeño ejército de verbos auxiliares. Por qué detrás de la pregunta «cuán compleja es esta lengua» no hay un número único. Y por qué el protoindoeuropeo — una lengua de la que nadie ha hallado jamás un texto — parece aun así elaborado cuando los lingüistas lo reconstruyen comparando las lenguas que salieron de él.

Y luego la parte que más cuesta aceptar. No hay ninguna dirección. Las lenguas eslavas lo enseñan con claridad: la mayoría conservó casos ricos, mientras que el búlgaro los perdió en los sustantivos casi del todo y le creció otra cosa, un artículo determinado pegado al final de la palabra. El mismo antepasado, direcciones opuestas, y ninguna de las dos es la mejora.

Los subtítulos están escritos para este vídeo, no generados automáticamente. Hay una pista de audio en inglés americano disponible como segunda pista.

Transcripción completa, fuentes y traducciones: https://theresmoretoit-channel.github.io/es/videos/why-are-some-languages-complicated/

Capítulos
00:00 Vida simple, lengua complicada
00:36 ¿Por qué no «goed»?
01:31 La lengua no es tecnología
02:25 Cómo una lengua se convierte en muchas
03:18 ¿Por qué no se desgastan, entonces?
03:52 El perro y el hombre
04:22 Un pequeño ejército de auxiliares
04:49 La complejidad se muda
05:03 No existe ningún dial
05:49 De vuelta a nuestro humano de entonces
06:09 Una reconstrucción, no un testimonio
06:27 Una sociedad sin tecnología
06:45 ¿Lo vio usted o se lo contaron?
07:19 Menos ingeniería
08:04 No hay ninguna dirección
08:15 El ejemplo eslavo
08:47 Nunca fue una escalera
09:08 ¿Por qué esperábamos una simple?

CRÉDITOS DE IMÁGENES
Beowulf, Cotton MS Vitellius A XV, f. 132r — dominio público
vía Wikimedia Commons
```

## svenska (`sv`)

```
Varför är vissa språk så komplicerade?
```

```
För femtusen år sedan fanns ingen elektricitet, inga böcker och inga skolor. Med våra mått mätt ett utomordentligt enkelt liv — man skulle alltså vänta sig ett lika enkelt språk. Latin, fornengelska och fornnordiska säger något annat. Alla hade ett grammatiskt maskineri som dagens engelska till stor del har tappat.

Man behöver inget gammalt språk för att se hur underligt det blir. Engelskan säger ”go” och ”went”, och ”went” hörde aldrig till ”go”. Det var preteritum av ett annat verb, ”wend”. Någon gång tog engelskan tyst preteritum från det ena och gav det till det andra. Ingen röstade om det. Ingen skrev ner det som en regel. Det hände, och sedan blev det kvar.

Den här videon handlar om varför det är vanligt och inte konstigt. Hur ett språk blir till många utan att någon bestämmer sig för att starta ett nytt. Varför förlusten av kasusändelser inte gjorde engelskan enklare, utan flyttade arbetet till ordföljden och till en liten armé av hjälpverb. Varför det inte finns någon enda siffra bakom frågan ”hur komplext är det här språket”. Och varför urindoeuropeiskan — ett språk som ingen någonsin hittat en text i — ändå ser utstuderad ut när språkforskare rekonstruerar den genom att jämföra de språk som kom ur den.

Och så den del som folk har svårast att acceptera. Det finns ingen riktning. De slaviska språken visar det tydligt: de flesta behöll rika kasus, medan bulgariskan tappade dem på substantiven nästan helt och fick något annat i stället, en bestämd artikel som sitter fast i slutet av ordet. Samma förfader, motsatta riktningar, och ingen av dem är uppgraderingen.

Undertexterna är skrivna för den här videon, inte automatgenererade. Ett ljudspår på amerikansk engelska finns som andra ljudspår.

Hela texten, källor och översättningar: https://theresmoretoit-channel.github.io/sv/videos/why-are-some-languages-complicated/

Kapitel
00:00 Ett enkelt liv, ett komplicerat språk
00:36 Varför inte ”goed”?
01:31 Språk är inte teknik
02:25 Hur ett språk blir till många
03:18 Varför nöts de då inte ner?
03:52 Hunden och mannen
04:22 En liten armé av hjälpverb
04:49 Komplexiteten flyttar
05:03 Det finns ingen mätare
05:49 Tillbaka till vår människa från förr
06:09 En rekonstruktion, inte ett vittnesmål
06:27 Ett samhälle utan teknik
06:45 Såg du det själv eller fick du höra det?
07:19 Mindre ingenjörskonst
08:04 Det finns ingen riktning
08:15 Det slaviska exemplet
08:47 Aldrig en stege
09:08 Varför väntade vi oss ett enkelt?

BILDKÄLLOR
Beowulf, Cotton MS Vitellius A XV, f. 132r — public domain
via Wikimedia Commons
```
