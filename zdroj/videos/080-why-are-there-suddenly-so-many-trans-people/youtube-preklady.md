# YouTube — lokalizace 080 „Why Are There Suddenly So Many Trans People?"

Třináct překladů titulu a bloku „Popis" z `youtube.md` (anglický snippet se
posílá beze změny). Čte `tools/lokalizace.py`; formát a pořadí sekcí podle
`docs/zverejneni.md`.

## Co se NEPŘEKLÁDÁ

- **časy kapitol** (na vteřinu podle `work/timing.json`, celkem 744,3 s,
  scény S01, S07, S15, S29, S34, S45, S51b, S53, S63, S73, S77, S80) —
  po každém dalším běhu `tts.py` je přepočítej tady i v `youtube.md`,
- **vlastní jména** (Magnus Hirschfeld, Lili Elbe, Berlín v místním tvaru);
  v ukrajinštině jsou přepsaná do cyrilice jako v `script.uk.md`
  (Магнус Гіршфельд, Лілі Ельбе), letopočty 1933 číslicí,
- **název studie v DATA** (Herman & Flores… Williams Institute, UCLA) —
  přeložený je jen nadpis DATA,
- **atribuce snímku** celá beze změny, včetně „unknown photographer"
  (je to opsané pole zdroje, ne věta popisu; rozhodnuto konzistentně pro
  všech 13 jazyků), „Wellcome Collection, CC BY 4.0, via Wikimedia Commons"
  a adresa licence — překládají se jen nadpisy KAPITOLY / ZDROJE OBRÁZKŮ,
  věta o ostatních snímcích a slovo „Licence",
- **tagy** — YouTube je per jazyk nemá,
- **odstavec o titulcích a americké stopě** se nepřekládá znovu, je doslova
  z tabulky v `docs/zverejneni.md`.

Terminologie podle `script.<kód>.md` téhož videa (cs „genderová identita",
„genderová dysforie", „tranzice"; de „Geschlechtsidentität",
„Geschlechtsdysphorie", „trans Menschen"; pl „transpłciowy", „tranzycja";
fi „transihminen", „sukupuolidysforia"; uk «перехід»; vi „người chuyển
giới", „chứng phiền muộn giới"; tr „geçiş"). Titul je první řádek
`# …` scénáře, názvy kapitol jsou co nejblíž mluveným nadpisům sekcí
(S07, S15, S29, S34, S45, S53, S63, S73, S77), titul dalšího dílu je S85.

Registr: tyká se tam, kde jazyk volí (cs, de du, pl, uk ти, tr sen,
id kamu, fr tu, es tú, it tu, pt-BR você, sv du), fi „sinä", vi „bạn" —
jako ve scénářích téhož videa.

Čísla: „jeden ze sta" a „zhruba desetkrát" slovy jako v originálu, věky
(13+, 18–24, 65+) číslicí, ať jsou v popisu čitelné. Míra jistoty drží
originál: „it can seem as if", „researchers estimate", „roughly ten times",
otázka „what can't they?" místo závěru.

## suomi (`fi`)

```
Miksi transihmisiä on yhtäkkiä niin paljon?
```

```
Oletko koskaan tavannut transihmistä? Ehkä olet, etkä vain tiennyt sitä. Viime vuosina voi tuntua siltä, kuin transihmisiä olisi yhtäkkiä ilmestynyt kaikkialle. Miksi siis näyttää siltä, että heitä on nyt niin paljon enemmän?

Video aloittaa perusasioista: mitä trans oikeastaan tarkoittaa, miksi sukupuoli-identiteetti ja seksuaalinen suuntautuminen ovat eri asioita ja miltä sukupuolidysforia voi tuntua. Se kertoo, mitä transitio on, miksi se ei ole yksi tietty leikkaus ja onko transihmisyys pelkkä muoti-ilmiö.

Sitten vuorossa ovat luvut. Tutkijat arvioivat, että Yhdysvalloissa noin yksi sadasta 13 vuotta täyttäneestä kuvaa itseään transihmiseksi. 18–24-vuotiailla nuorilla aikuisilla osuus on suunnilleen kymmenkertainen 65 vuotta täyttäneisiin verrattuna. Mitä nuo luvut voivat kertoa ja mitä eivät?

Lopuksi video palaa lähes sadan vuoden taakse Berliiniin: Magnus Hirschfeldin instituuttiin, tanskalaiseen taidemaalariin Lili Elbeen ja siihen, mitä instituutille tapahtui toukokuussa 1933.

Tämä on ensimmäinen video transihmisiä käsittelevässä sarjassa. Seuraava kysyy: mistä tiedät, että olet trans?

Tekstitykset on kirjoitettu tätä videota varten, ei luotu automaattisesti. Toisena ääniraitana on amerikanenglanti.

LUVUT
00:00 Oletko koskaan tavannut transihmistä?
00:43 Mitä trans oikeastaan tarkoittaa?
02:09 Miltä se tuntuu?
04:10 Ei ole yhtä tietynlaista transihmistä
04:52 Mitä transitio on?
06:18 Onko transihmisyys muoti-ilmiö?
07:21 Ihmisen biologia ei ole standardijärjestelmä
08:04 Onko transihmisiä nyt todella enemmän?
09:19 Oliko transihmisiä olemassa ennenkin?
10:51 Miksi huomaamme heidät nyt niin selvästi?
11:18 Ehkä todellinen muutos ei ole ihmisissä
11:45 Seuraavaksi: mistä tiedät, että olet trans?

AINEISTO
Herman, J. L. & Flores, A. R. (2025). How Many Adults and Youth Identify as Transgender in the United States? Williams Institute, UCLA.

KUVALÄHTEET
Lili Elbe, Copenhagen, 1930 — unknown photographer, Wellcome Collection, CC BY 4.0, via Wikimedia Commons
Muut arkistokuvat ovat public domainia.
Lisenssi: creativecommons.org/licenses/by/4.0
```

## français (`fr`)

```
Pourquoi y a-t-il soudain autant de personnes trans ?
```

```
Tu as déjà rencontré une personne transgenre ? Peut-être que oui, sans jamais le savoir. Ces dernières années, on peut avoir l'impression que les personnes trans sont soudain apparues partout. Alors pourquoi semble-t-il qu'il y en ait tellement plus ?

Cette vidéo commence par les bases : ce que « transgenre » veut vraiment dire, pourquoi l'identité de genre et l'orientation sexuelle sont deux choses différentes, et ce que l'on peut ressentir avec la dysphorie de genre. Elle explique ce qu'est la transition, pourquoi elle ne se résume pas à une seule opération, et si être transgenre n'est qu'une mode.

Ensuite, place aux chiffres. Aux États-Unis, des chercheurs estiment qu'environ une personne sur cent âgée de 13 ans et plus se décrit comme transgenre. Chez les jeunes adultes de 18 à 24 ans, la proportion est environ dix fois plus élevée que chez les personnes de 65 ans et plus. Que peuvent nous dire ces chiffres, et que ne peuvent-ils pas nous dire ?

Enfin, elle remonte près de cent ans en arrière, jusqu'à l'institut de Magnus Hirschfeld à Berlin, à la peintre danoise Lili Elbe, et à ce qui est arrivé à l'institut en mai 1933.

C'est la première vidéo d'une série sur les personnes transgenres. La suivante pose la question : comment savoir qu'on est trans ?

Les sous-titres sont écrits pour cette vidéo, pas générés automatiquement. Une piste audio en anglais américain est disponible en seconde piste.

CHAPITRES
00:00 Tu as déjà rencontré une personne trans ?
00:43 Que veut vraiment dire « transgenre » ?
02:09 Qu'est-ce qu'on ressent ?
04:10 Il n'existe pas un seul type de personne transgenre
04:52 Qu'est-ce que la transition ?
06:18 Être transgenre, est-ce une mode ?
07:21 La biologie humaine n'est pas un système standard
08:04 Y a-t-il vraiment plus de personnes trans aujourd'hui ?
09:19 Les personnes trans existaient-elles autrefois ?
10:51 Pourquoi les remarque-t-on autant aujourd'hui ?
11:18 Peut-être que le vrai changement n'est pas chez les gens
11:45 À suivre : comment savoir qu'on est trans ?

DONNÉES
Herman, J. L. & Flores, A. R. (2025). How Many Adults and Youth Identify as Transgender in the United States? Williams Institute, UCLA.

CRÉDITS DES IMAGES
Lili Elbe, Copenhagen, 1930 — unknown photographer, Wellcome Collection, CC BY 4.0, via Wikimedia Commons
Toutes les autres images d'archives sont dans le domaine public.
Licence : creativecommons.org/licenses/by/4.0
```

## Bahasa Indonesia (`id`)

```
Kenapa Tiba-tiba Ada Begitu Banyak Orang Trans?
```

```
Pernahkah kamu bertemu orang transgender? Mungkin pernah, tapi kamu tidak pernah tahu. Dalam beberapa tahun terakhir, rasanya seolah-olah orang trans tiba-tiba muncul di mana-mana. Jadi, kenapa kelihatannya jumlah mereka jauh lebih banyak?

Video ini dimulai dari dasar: apa sebenarnya arti transgender, kenapa identitas gender dan orientasi seksual adalah dua hal yang berbeda, dan seperti apa rasanya mengalami disforia gender. Video ini juga membahas apa itu transisi, kenapa transisi bukan satu operasi tertentu, dan apakah menjadi transgender hanyalah tren.

Lalu video beralih ke angka. Para peneliti memperkirakan bahwa di Amerika Serikat, sekitar satu dari seratus orang berusia 13 tahun ke atas menyebut diri mereka transgender. Di kalangan orang dewasa muda berusia 18–24 tahun, proporsinya kira-kira sepuluh kali lebih tinggi daripada di kalangan orang berusia 65 tahun ke atas. Apa yang bisa kita ketahui dari angka-angka itu, dan apa yang tidak?

Terakhir, video ini kembali ke hampir seratus tahun lalu, ke institut Magnus Hirschfeld di Berlin, pelukis Denmark Lili Elbe, dan apa yang terjadi pada institut itu pada Mei 1933.

Ini adalah video pertama dalam seri tentang orang transgender. Video berikutnya bertanya: bagaimana kamu tahu kalau kamu trans?

Subtitel ditulis khusus untuk video ini, bukan dibuat secara otomatis. Tersedia juga trek audio kedua dalam bahasa Inggris Amerika.

BAB
00:00 Pernahkah kamu bertemu orang trans?
00:43 Apa sebenarnya arti transgender?
02:09 Bagaimana rasanya?
04:10 Tidak hanya ada satu jenis orang transgender
04:52 Apa itu transisi?
06:18 Apakah menjadi transgender itu sekadar tren?
07:21 Biologi manusia bukan sistem standar
08:04 Apakah sekarang benar-benar ada lebih banyak orang trans?
09:19 Apakah orang trans sudah ada di masa lalu?
10:51 Kenapa sekarang kita begitu memperhatikan mereka?
11:18 Mungkin perubahan yang sebenarnya bukan pada orang-orangnya
11:45 Berikutnya: bagaimana kamu tahu kalau kamu trans?

DATA
Herman, J. L. & Flores, A. R. (2025). How Many Adults and Youth Identify as Transgender in the United States? Williams Institute, UCLA.

SUMBER GAMBAR
Lili Elbe, Copenhagen, 1930 — unknown photographer, Wellcome Collection, CC BY 4.0, via Wikimedia Commons
Semua gambar arsip lainnya berada dalam domain publik.
Lisensi: creativecommons.org/licenses/by/4.0
```

## italiano (`it`)

```
Perché all'improvviso ci sono così tante persone trans?
```

```
Hai mai conosciuto una persona transgender? Forse sì, senza mai saperlo. Negli ultimi anni può sembrare che le persone trans siano improvvisamente comparse ovunque. Allora perché sembra che ce ne siano così tante di più?

Il video parte dalle basi: che cosa significa davvero transgender, perché identità di genere e orientamento sessuale sono cose diverse e che cosa si può provare con la disforia di genere. Spiega che cos'è la transizione, perché non è un'unica, specifica operazione e se essere transgender sia semplicemente una moda.

Poi passa ai numeri. Negli Stati Uniti, i ricercatori stimano che circa una persona su cento dai 13 anni in su si definisca transgender. Tra i giovani adulti dai 18 ai 24 anni la quota è circa dieci volte più alta che tra chi ha 65 anni o più. Che cosa possono dirci questi numeri, e che cosa no?

Infine torna indietro di quasi cent'anni, all'istituto di Magnus Hirschfeld a Berlino, alla pittrice danese Lili Elbe e a ciò che accadde all'istituto nel maggio del 1933.

Questo è il primo video di una serie sulle persone transgender. Il prossimo si chiede: come fai a sapere di essere trans?

I sottotitoli sono scritti per questo video, non generati automaticamente. Come seconda traccia audio è disponibile l’inglese americano.

CAPITOLI
00:00 Hai mai conosciuto una persona trans?
00:43 Che cosa significa davvero transgender?
02:09 Che cosa si prova?
04:10 Non esiste un solo tipo di persona transgender
04:52 Che cos'è la transizione?
06:18 Essere transgender è una moda?
07:21 La biologia umana non è un sistema standard
08:04 Ci sono davvero più persone trans oggi?
09:19 Esistevano persone trans anche in passato?
10:51 Perché le notiamo così tanto oggi?
11:18 Forse non sono le persone a essere davvero cambiate
11:45 Prossimo video: come fai a sapere di essere trans?

DATI
Herman, J. L. & Flores, A. R. (2025). How Many Adults and Youth Identify as Transgender in the United States? Williams Institute, UCLA.

CREDITI DELLE IMMAGINI
Lili Elbe, Copenhagen, 1930 — unknown photographer, Wellcome Collection, CC BY 4.0, via Wikimedia Commons
Tutte le altre immagini d'archivio sono di pubblico dominio.
Licenza: creativecommons.org/licenses/by/4.0
```

## Deutsch (`de`)

```
Warum gibt es plötzlich so viele trans Menschen?
```

```
Bist du schon mal einer trans Person begegnet? Vielleicht ja, ohne es je zu wissen. In den letzten Jahren kann es so wirken, als wären trans Menschen plötzlich überall aufgetaucht. Warum sieht es also so aus, als gäbe es so viel mehr von ihnen?

Das Video beginnt mit den Grundlagen: was transgender eigentlich bedeutet, warum Geschlechtsidentität und sexuelle Orientierung zwei verschiedene Dinge sind und wie sich Geschlechtsdysphorie anfühlen kann. Es zeigt, was eine Transition ist, warum sie nicht eine bestimmte Operation bedeutet und ob es einfach ein Modetrend ist, trans zu sein.

Dann geht es um die Zahlen. Forschende schätzen, dass sich in den USA etwa einer von hundert Menschen ab 13 Jahren als transgender bezeichnet. Bei jungen Erwachsenen zwischen 18 und 24 ist der Anteil ungefähr zehnmal so hoch wie bei Menschen ab 65. Was können uns diese Zahlen sagen und was nicht?

Zum Schluss geht es fast hundert Jahre zurück: zu Magnus Hirschfelds Institut in Berlin, zur dänischen Malerin Lili Elbe und zu dem, was im Mai 1933 mit dem Institut geschah.

Das ist das erste Video einer Reihe über trans Menschen. Das nächste fragt: Woher weißt du, dass du trans bist?

Die Untertitel wurden für dieses Video geschrieben, nicht automatisch erzeugt. Als zweite Tonspur steht amerikanisches Englisch bereit.

KAPITEL
00:00 Bist du schon mal einer trans Person begegnet?
00:43 Was bedeutet transgender eigentlich?
02:09 Wie fühlt sich das an?
04:10 Es gibt nicht die eine Art von trans Person
04:52 Was ist eine Transition?
06:18 Ist es ein Modetrend, trans zu sein?
07:21 Die menschliche Biologie ist kein Standardsystem
08:04 Gibt es heute wirklich mehr trans Menschen?
09:19 Gab es trans Menschen auch schon früher?
10:51 Warum fallen sie uns heute so sehr auf?
11:18 Vielleicht liegt die eigentliche Veränderung nicht bei den Menschen
11:45 Als Nächstes: Woher weißt du, dass du trans bist?

DATEN
Herman, J. L. & Flores, A. R. (2025). How Many Adults and Youth Identify as Transgender in the United States? Williams Institute, UCLA.

BILDNACHWEIS
Lili Elbe, Copenhagen, 1930 — unknown photographer, Wellcome Collection, CC BY 4.0, via Wikimedia Commons
Alle übrigen Archivbilder sind gemeinfrei.
Lizenz: creativecommons.org/licenses/by/4.0
```

## polski (`pl`)

```
Dlaczego nagle jest tyle osób trans?
```

```
Czy spotkałeś kiedyś osobę transpłciową? Może tak, tylko nigdy o tym nie wiedziałeś. W ostatnich latach może się wydawać, że osoby trans nagle pojawiły się wszędzie. Dlaczego więc wygląda na to, że jest ich teraz o tyle więcej?

Film zaczyna od podstaw: co właściwie znaczy „transpłciowy”, dlaczego tożsamość płciowa i orientacja seksualna to dwie różne rzeczy i jak można odczuwać dysforię płciową. Pokazuje, czym jest tranzycja, dlaczego nie jest jedną konkretną operacją i czy bycie trans to po prostu moda.

Potem przechodzi do liczb. Badacze szacują, że w Stanach Zjednoczonych mniej więcej jedna na sto osób w wieku od 13 lat określa się jako transpłciowa. Wśród młodych dorosłych w wieku 18–24 lat ten odsetek jest mniej więcej dziesięć razy wyższy niż wśród osób w wieku 65 lat i więcej. Co te liczby mogą nam powiedzieć, a czego nie?

Na koniec cofa się o prawie sto lat — do instytutu Magnusa Hirschfelda w Berlinie, do duńskiej malarki Lili Elbe i do tego, co stało się z instytutem w maju 1933 roku.

To pierwszy film z serii o osobach transpłciowych. Następny pyta: skąd wiesz, że jesteś trans?

Napisy są pisane do tego filmu, nie generowane automatycznie. Jako druga ścieżka dźwiękowa dostępny jest angielski amerykański.

ROZDZIAŁY
00:00 Czy spotkałeś kiedyś osobę trans?
00:43 Co właściwie znaczy „transpłciowy”?
02:09 Jak to jest?
04:10 Nie ma jednego typu osoby transpłciowej
04:52 Czym jest tranzycja?
06:18 Czy bycie trans to moda?
07:21 Ludzka biologia to nie standardowy system
08:04 Czy osób trans jest teraz naprawdę więcej?
09:19 Czy osoby trans istniały też w przeszłości?
10:51 Dlaczego teraz tak bardzo zwracają naszą uwagę?
11:18 Może prawdziwa zmiana nie zaszła w ludziach
11:45 W następnym filmie: skąd wiesz, że jesteś trans?

DANE
Herman, J. L. & Flores, A. R. (2025). How Many Adults and Youth Identify as Transgender in the United States? Williams Institute, UCLA.

ŹRÓDŁA ZDJĘĆ
Lili Elbe, Copenhagen, 1930 — unknown photographer, Wellcome Collection, CC BY 4.0, via Wikimedia Commons
Wszystkie pozostałe zdjęcia archiwalne są w domenie publicznej.
Licencja: creativecommons.org/licenses/by/4.0
```

## português (Brasil) (`pt-BR`)

```
Por que de repente existem tantas pessoas trans?
```

```
Você já conheceu uma pessoa transgênero? Talvez sim, sem nunca ter percebido. Nos últimos anos, pode parecer que as pessoas trans surgiram de repente por toda parte. Então por que parece que agora existem muito mais?

O vídeo começa pelo básico: o que transgênero quer dizer, afinal, por que identidade de gênero e orientação sexual são coisas diferentes e como alguém pode se sentir ao vivenciar a disforia de gênero. Ele mostra o que é a transição, por que ela não é uma operação específica e se ser transgênero é simplesmente moda.

Depois, passa para os números. Pesquisadores estimam que, nos Estados Unidos, cerca de uma em cada cem pessoas com 13 anos ou mais se descreve como transgênero. Entre jovens adultos de 18 a 24 anos, a proporção é cerca de dez vezes maior do que entre pessoas com 65 anos ou mais. O que esses números podem nos dizer, e o que não podem?

Por fim, ele volta quase cem anos no tempo, ao instituto de Magnus Hirschfeld em Berlim, à pintora dinamarquesa Lili Elbe e ao que aconteceu com o instituto em maio de 1933.

Este é o primeiro vídeo de uma série sobre pessoas transgênero. O próximo pergunta: como saber se você é trans?

As legendas foram escritas para este vídeo, não geradas automaticamente. Como segunda faixa de áudio está disponível o inglês americano.

CAPÍTULOS
00:00 Você já conheceu uma pessoa trans?
00:43 O que transgênero quer dizer, afinal?
02:09 Como é sentir isso?
04:10 Não existe um único tipo de pessoa transgênero
04:52 O que é a transição?
06:18 Ser transgênero é moda?
07:21 A biologia humana não é um sistema padrão
08:04 Existem mesmo mais pessoas trans hoje?
09:19 Pessoas trans existiam no passado?
10:51 Por que reparamos tanto nelas agora?
11:18 Talvez a verdadeira mudança não esteja nas pessoas
11:45 A seguir: como saber se você é trans?

DADOS
Herman, J. L. & Flores, A. R. (2025). How Many Adults and Youth Identify as Transgender in the United States? Williams Institute, UCLA.

CRÉDITOS DAS IMAGENS
Lili Elbe, Copenhagen, 1930 — unknown photographer, Wellcome Collection, CC BY 4.0, via Wikimedia Commons
Todas as outras imagens de arquivo estão em domínio público.
Licença: creativecommons.org/licenses/by/4.0
```

## Türkçe (`tr`)

```
Neden Birdenbire Bu Kadar Çok Trans İnsan Var?
```

```
Hiç transgender biriyle tanıştın mı? Belki tanıştın ama trans olduğunu hiç fark etmedin. Son birkaç yılda trans insanlar birdenbire her yerde ortaya çıkmış gibi görünebilir. Peki neden şimdi çok daha fazla trans insan varmış gibi geliyor?

Bu video temel konularla başlıyor: transgender aslında ne demek, cinsiyet kimliği ile cinsel yönelim neden farklı şeyler ve cinsiyet disforisi nasıl bir his olabilir. Geçişin ne olduğuna, neden tek bir belirli ameliyat anlamına gelmediğine ve transgender olmanın sadece bir moda olup olmadığına bakıyor.

Ardından sayılara geçiyor. Araştırmacıların tahminine göre ABD'de 13 yaş ve üzerindeki her yüz kişiden yaklaşık biri kendini transgender olarak tanımlıyor. 18–24 yaş arasındaki genç yetişkinlerde bu oran, 65 yaş ve üzerindekilere göre kabaca on kat daha yüksek. Bu sayılar bize neyi söyleyebilir, neyi söyleyemez?

Son olarak neredeyse yüz yıl geriye gidiyor: Magnus Hirschfeld'in Berlin'deki enstitüsüne, Danimarkalı ressam Lili Elbe'ye ve Mayıs 1933'te enstitünün başına gelenlere.

Bu, transgender insanlar hakkındaki bir serinin ilk videosu. Bir sonraki video şunu soruyor: Trans olduğunu nasıl anlarsın?

Altyazılar bu video için yazıldı, otomatik olarak oluşturulmadı. İkinci ses parçası olarak Amerikan İngilizcesi de mevcut.

BÖLÜMLER
00:00 Hiç trans biriyle tanıştın mı?
00:43 Transgender aslında ne demek?
02:09 Nasıl bir his?
04:10 Tek bir tür transgender insan yoktur
04:52 Geçiş nedir?
06:18 Transgender olmak bir moda mı?
07:21 İnsan biyolojisi standart bir sistem değildir
08:04 Gerçekten daha fazla trans insan mı var?
09:19 Geçmişte de trans insanlar var mıydı?
10:51 Neden şimdi bu kadar dikkatimizi çekiyorlar?
11:18 Belki asıl değişim insanlarda değildir
11:45 Sırada: Trans olduğunu nasıl anlarsın?

VERİ
Herman, J. L. & Flores, A. R. (2025). How Many Adults and Youth Identify as Transgender in the United States? Williams Institute, UCLA.

GÖRSEL KAYNAKLARI
Lili Elbe, Copenhagen, 1930 — unknown photographer, Wellcome Collection, CC BY 4.0, via Wikimedia Commons
Diğer tüm arşiv görselleri kamu malıdır.
Lisans: creativecommons.org/licenses/by/4.0
```

## українська (`uk`)

```
Чому раптом стало так багато трансгендерних людей?
```

```
Тобі колись траплялася трансгендерна людина? Може, так, і ти навіть не знав. Останніми роками може здаватися, ніби трансгендерні люди раптом з’явилися всюди. То чому складається враження, що їх стало набагато більше?

Відео починається з основ: що насправді означає «трансгендерний», чому гендерна ідентичність і сексуальна орієнтація — це різні речі і як може відчуватися гендерна дисфорія. Воно розповідає, що таке перехід, чому це не одна конкретна операція і чи трансгендерність — це просто мода.

Далі — цифри. За оцінками дослідників, у США приблизно одна людина зі ста віком від 13 років називає себе трансгендерною. Серед молодих дорослих віком 18–24 роки ця частка приблизно вдесятеро більша, ніж серед людей віком від 65 років. Що можуть сказати ці цифри, а чого не можуть?

Насамкінець відео повертається майже на сто років назад — до інституту Магнуса Гіршфельда в Берліні, до данської художниці Лілі Ельбе і до того, що сталося з інститутом у травні 1933 року.

Це перше відео із серії про трансгендерних людей. Наступне питає: як зрозуміти, що ти транс?

Субтитри написані для цього відео, а не згенеровані автоматично. Також доступна друга звукова доріжка — американською англійською.

РОЗДІЛИ
00:00 Тобі колись траплялася трансгендерна людина?
00:43 Що насправді означає «трансгендерний»?
02:09 Як це відчувається?
04:10 Немає одного типу трансгендерної людини
04:52 Що таке перехід?
06:18 Трансгендерність — це мода?
07:21 Людська біологія — не стандартна система
08:04 Чи справді зараз більше трансгендерних людей?
09:19 Чи були трансгендерні люди в минулому?
10:51 Чому зараз вони так привертають нашу увагу?
11:18 Можливо, справжня зміна не в людях
11:45 Далі: як зрозуміти, що ти транс?

ДАНІ
Herman, J. L. & Flores, A. R. (2025). How Many Adults and Youth Identify as Transgender in the United States? Williams Institute, UCLA.

ДЖЕРЕЛА ЗОБРАЖЕНЬ
Lili Elbe, Copenhagen, 1930 — unknown photographer, Wellcome Collection, CC BY 4.0, via Wikimedia Commons
Усі інші архівні зображення перебувають у суспільному надбанні.
Ліцензія: creativecommons.org/licenses/by/4.0
```

## Tiếng Việt (`vi`)

```
Vì sao đột nhiên có nhiều người chuyển giới đến vậy?
```

```
Bạn đã bao giờ gặp một người chuyển giới chưa? Có thể là có, chỉ là bạn không hề biết. Vài năm gần đây, có cảm giác như người chuyển giới bỗng dưng xuất hiện ở khắp nơi. Vậy vì sao có vẻ như số người chuyển giới đã tăng lên nhiều so với trước đây?

Video bắt đầu từ những điều cơ bản: chuyển giới thực ra nghĩa là gì, vì sao bản dạng giới và xu hướng tính dục là hai chuyện khác nhau, và chứng phiền muộn giới có thể mang lại cảm giác như thế nào. Video cũng tìm hiểu quá trình chuyển đổi là gì, vì sao đó không phải là một ca phẫu thuật cụ thể nào, và liệu chuyển giới có đơn giản chỉ là một trào lưu.

Sau đó video chuyển sang các con số. Các nhà nghiên cứu ước tính rằng ở Hoa Kỳ, cứ một trăm người từ 13 tuổi trở lên thì có khoảng một người tự nhận mình là người chuyển giới. Ở người trưởng thành trẻ tuổi từ 18 đến 24 tuổi, tỷ lệ này cao hơn khoảng mười lần so với những người từ 65 tuổi trở lên. Những con số ấy có thể cho ta biết điều gì, và không thể cho biết điều gì?

Cuối cùng, video quay ngược gần một trăm năm, về viện nghiên cứu của Magnus Hirschfeld ở Berlin, nữ họa sĩ người Đan Mạch Lili Elbe, và những gì đã xảy ra với viện vào tháng 5 năm 1933.

Đây là video đầu tiên trong loạt video về người chuyển giới. Video tiếp theo đặt câu hỏi: làm sao biết mình là người chuyển giới?

Phụ đề được viết riêng cho video này, không phải tạo tự động. Có thể chọn tiếng Anh Mỹ ở bản âm thanh thứ hai.

CHƯƠNG
00:00 Bạn đã bao giờ gặp một người chuyển giới chưa?
00:43 Chuyển giới thực ra nghĩa là gì?
02:09 Cảm giác đó như thế nào?
04:10 Không có một kiểu người chuyển giới duy nhất
04:52 Quá trình chuyển đổi là gì?
06:18 Chuyển giới có phải là một trào lưu?
07:21 Sinh học con người không phải một hệ thống chuẩn
08:04 Có thật là bây giờ có nhiều người chuyển giới hơn?
09:19 Trong quá khứ có người chuyển giới không?
10:51 Vì sao bây giờ ta lại để ý đến họ nhiều thế?
11:18 Có lẽ thay đổi thực sự không nằm ở con người
11:45 Tiếp theo: làm sao biết mình là người chuyển giới?

DỮ LIỆU
Herman, J. L. & Flores, A. R. (2025). How Many Adults and Youth Identify as Transgender in the United States? Williams Institute, UCLA.

NGUỒN HÌNH ẢNH
Lili Elbe, Copenhagen, 1930 — unknown photographer, Wellcome Collection, CC BY 4.0, via Wikimedia Commons
Tất cả các hình ảnh lưu trữ khác thuộc phạm vi công cộng.
Giấy phép: creativecommons.org/licenses/by/4.0
```

## čeština (`cs`)

```
Proč je najednou tolik trans lidí?
```

```
Potkal jsi někdy transgender člověka? Možná ano, a vůbec jsi o tom nevěděl. Posledních pár let to může vypadat, jako by se trans lidé najednou objevili všude. Tak proč se zdá, že jich je o tolik víc?

Video začíná od základů: co vlastně znamená transgender, proč jsou genderová identita a sexuální orientace dvě různé věci a jaké může být prožívat genderovou dysforii. Vysvětluje, co je tranzice, proč to není jedna konkrétní operace a jestli je to prostě móda, být transgender.

Pak přijdou na řadu čísla. Výzkumníci odhadují, že ve Spojených státech se zhruba jeden ze sta lidí ve věku od 13 let označuje za transgender. U mladých dospělých ve věku 18–24 let je ten podíl zhruba desetkrát vyšší než u lidí od 65 let. Co nám ta čísla můžou říct, a co ne?

Nakonec se vrací skoro sto let zpátky, k institutu Magnuse Hirschfelda v Berlíně, k dánské malířce Lili Elbe a k tomu, co se s institutem stalo v květnu 1933.

Tohle je první video ze série o transgender lidech. To další se ptá: jak poznáš, že jsi trans?

Titulky jsou psané pro tohle video, ne strojový přepis. Jako druhá zvuková stopa je k dispozici americká angličtina.

KAPITOLY
00:00 Potkal jsi někdy trans člověka?
00:43 Co vlastně znamená transgender?
02:09 Jaké to je?
04:10 Neexistuje jeden typ transgender člověka
04:52 Co je tranzice?
06:18 Je to móda, být transgender?
07:21 Lidská biologie není standardizovaný systém
08:04 Je dnes trans lidí opravdu víc?
09:19 Existovali trans lidé i v minulosti?
10:51 Proč si jich dnes tolik všímáme?
11:18 Možná se skutečná změna neodehrála v lidech
11:45 Příště: jak poznáš, že jsi trans?

DATA
Herman, J. L. & Flores, A. R. (2025). How Many Adults and Youth Identify as Transgender in the United States? Williams Institute, UCLA.

ZDROJE OBRÁZKŮ
Lili Elbe, Copenhagen, 1930 — unknown photographer, Wellcome Collection, CC BY 4.0, via Wikimedia Commons
Všechny ostatní archivní snímky jsou volné dílo.
Licence: creativecommons.org/licenses/by/4.0
```

## español (`es`)

```
¿Por qué de repente hay tantas personas trans?
```

```
¿Alguna vez has conocido a una persona transgénero? Quizá sí, y nunca lo supiste. En los últimos años, puede parecer que las personas trans han aparecido de repente por todas partes. Entonces, ¿por qué da la impresión de que hay tantas más?

Este vídeo empieza por lo básico: qué significa realmente transgénero, por qué la identidad de género y la orientación sexual son cosas distintas y qué se puede sentir con la disforia de género. Explica qué es la transición, por qué no es una operación concreta y si ser transgénero es simplemente una moda.

Después pasa a las cifras. Los investigadores estiman que en Estados Unidos alrededor de una de cada cien personas de 13 años o más se describe como transgénero. Entre los adultos jóvenes de 18 a 24 años, la proporción es aproximadamente diez veces mayor que entre las personas de 65 años o más. ¿Qué pueden decirnos esas cifras, y qué no?

Por último, retrocede casi cien años, hasta el instituto de Magnus Hirschfeld en Berlín, la pintora danesa Lili Elbe y lo que le ocurrió al instituto en mayo de 1933.

Este es el primer vídeo de una serie sobre las personas transgénero. El siguiente se pregunta: ¿cómo sabes que eres trans?

Los subtítulos están escritos para este vídeo, no generados automáticamente. Como segunda pista de audio está disponible el inglés americano.

CAPÍTULOS
00:00 ¿Alguna vez has conocido a una persona trans?
00:43 ¿Qué significa realmente transgénero?
02:09 ¿Qué se siente?
04:10 No hay un solo tipo de persona transgénero
04:52 ¿Qué es la transición?
06:18 ¿Ser transgénero es una moda?
07:21 La biología humana no es un sistema estándar
08:04 ¿De verdad hay ahora más personas trans?
09:19 ¿Existían personas trans en el pasado?
10:51 ¿Por qué nos fijamos tanto en ellas ahora?
11:18 Quizá el verdadero cambio no esté en las personas
11:45 Próximo vídeo: ¿cómo sabes que eres trans?

DATOS
Herman, J. L. & Flores, A. R. (2025). How Many Adults and Youth Identify as Transgender in the United States? Williams Institute, UCLA.

CRÉDITOS DE LAS IMÁGENES
Lili Elbe, Copenhagen, 1930 — unknown photographer, Wellcome Collection, CC BY 4.0, via Wikimedia Commons
Todas las demás imágenes de archivo son de dominio público.
Licencia: creativecommons.org/licenses/by/4.0
```

## svenska (`sv`)

```
Varför finns det plötsligt så många transpersoner?
```

```
Har du någonsin träffat en transperson? Kanske har du det, utan att någonsin veta om det. De senaste åren kan det verka som om transpersoner plötsligt har dykt upp överallt. Så varför ser det ut som att de har blivit så många fler?

Videon börjar med grunderna: vad trans egentligen betyder, varför könsidentitet och sexuell läggning är olika saker och hur könsdysfori kan kännas. Den tar upp vad transition är, varför det inte handlar om en viss operation och om det bara är en modefluga att vara trans.

Sedan kommer siffrorna. Forskare uppskattar att ungefär en av hundra personer i USA som är 13 år eller äldre beskriver sig som trans. Bland unga vuxna mellan 18 och 24 är andelen ungefär tio gånger högre än bland personer som är 65 eller äldre. Vad kan de siffrorna berätta för oss, och vad kan de inte?

Till sist går den nästan hundra år tillbaka i tiden, till Magnus Hirschfelds institut i Berlin, den danska målaren Lili Elbe och det som hände med institutet i maj 1933.

Det här är den första videon i en serie om transpersoner. Nästa video frågar: hur vet du att du är trans?

Undertexterna är skrivna för den här videon, inte automatgenererade. Som andra ljudspår finns amerikansk engelska.

KAPITEL
00:00 Har du någonsin träffat en transperson?
00:43 Vad betyder trans egentligen?
02:09 Hur känns det?
04:10 Det finns inte en enda sorts transperson
04:52 Vad är transition?
06:18 Är det en modefluga att vara trans?
07:21 Människans biologi är inget standardsystem
08:04 Finns det verkligen fler transpersoner nu?
09:19 Fanns det transpersoner förr i tiden?
10:51 Varför får de så mycket uppmärksamhet nu?
11:18 Kanske är den verkliga förändringen inte hos människorna
11:45 Nästa video: hur vet du att du är trans?

DATA
Herman, J. L. & Flores, A. R. (2025). How Many Adults and Youth Identify as Transgender in the United States? Williams Institute, UCLA.

BILDKÄLLOR
Lili Elbe, Copenhagen, 1930 — unknown photographer, Wellcome Collection, CC BY 4.0, via Wikimedia Commons
Alla övriga arkivbilder är allmän egendom.
Licens: creativecommons.org/licenses/by/4.0
```
