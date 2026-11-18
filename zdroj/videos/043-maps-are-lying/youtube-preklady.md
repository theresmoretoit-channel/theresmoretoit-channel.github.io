# Lokalizované názvy a popisy — 043

Nahrává `tools/lokalizace.py` přes `videos.update(part="localizations")`.
Anglický titul a popis zůstávají v `youtube.md` a posílají se zpátky
beze změny.

```bash
python tools/lokalizace.py videos/043-maps-are-lying --zkouska   # co by udělal
python tools/lokalizace.py videos/043-maps-are-lying             # nahraje
```

**Formát si vynucuje parser** (`bloky_z_podkladu()`): sekce jazyka je
nadpis `## <endonymum> (`<kód>`)`, uvnitř **přesně dva bloky** v trojici
zpětných apostrofů — první titul, druhý popis. Jiný počet nástroj
přeskočí s hláškou a jinak to nekřičí.

**Pořadí je podle YouTube Studia**, tedy bajtově podle UTF-8, ne
abecedně — Studio je tak vypisuje shora dolů a podklad se kopíruje po
řadě.

## Co se NEPŘEKLÁDÁ

- **vlastní jména** — Mercator, Gauss, Harry Beck, Leicester Square,
  Covent Garden, Boston
- **časy kapitol** na vteřinu — jsou to tytéž okamžiky ve všech jazycích
- **tagy** — YouTube je per-jazyk nemá

Názvy jazyků v řádku o titulcích se naopak **překládají**: smíšený
seznam endonym uprostřed odstavce se čte jako nedotažený překlad.

## Kontrola čísel

Všechna čísla videa jsou pod miliardou, takže past s *billion* /
*trillion* (10⁹ proti 10¹²) tady nehrozí. Přesto se každé přepočítalo,
ne přepsalo:

| anglicky | co to je |
|---|---|
| fourteen times | 14× |
| four / ten / eighty times | 4× / 10× / 80× |
| eight times | 8× |
| twenty-one kilometres | 21 km |
| two tenths of a millimetre | 0,2 mm |
| forty million times | 40 000 000× |
| two hundred and sixty metres | 260 m |
| twelve strips | 12 |

## suomi (`fi`)

```
Miksi kartat valehtelevat meille?
```

```
Katso maailmankarttaa. Grönlanti istuu siellä ylhäällä Kanadan vieressä, suunnilleen Afrikan kokoisena. Paitsi että Afrikka on neljätoista kertaa suurempi — eikä kartta tee virhettä. Se tekee täsmälleen sitä, mitä varten se rakennettiin.

Jokaisen Maan tasokartan on valehdeltava. Ei vahingossa, vaan välttämättä. Vuonna 1827 Carl Friedrich Gauss todisti sen: pinnan kaarevuus kuuluu pinnalle itselleen, joten palloa ei voi litistää venyttämättä tai repimättä sitä. Kartantekijät lakkasivat yrittämästä ja alkoivat sen sijaan valita, minkä valheen kertovat.

Mercator valitsi navigoinnin, ja hinta on laskuoppia. Oslo näkyy kartalla neljä kertaa todellista suurempana. Grönlannin keskiosa kymmenkertaisen. Pohjoiskärki yli kahdeksankymmenkertaisen. Grönlanti on pienempi kuin Kongo ja pienempi kuin Algeria, ja Etelä-Amerikka — joka näyttää tuolla kartalla pienemmältä — on yli kahdeksan kertaa suurempi.

Korjaa pinta-alat, niin muodot vääristyvät. Korjaa muodot, niin pinta-alat vääristyvät. Vuonna 2017 Bostonin julkiset koulut ottivat Mercatorin luokkiensa seiniltä — eikä kartta, jonka ne ripustivat tilalle, ole sekään se oikea.

Jäljelle jää karttapallo. Ei litistämistä, ei venyttämistä, navat yksinkertaisesti paikallaan. Paitsi että Maa ei ole pallo, Mount Everest olisi koulun karttapallolla kaksi kymmenesosaa millimetriä korkea, ja karttapallo painetaan tasona — kahdelletoista kapenevalle liuskalle, jotka sitten liimataan pallon päälle. Se on videon alun appelsiini, takaperin.

Karttapallo siis ratkaisee projektion ongelman. Se ei ratkaise esittämisen ongelmaa. Ja juuri siinä erossa on koko juttu — siksi paras koskaan piirretty kartta esittää maantieteen lähes kokonaan väärin, ja siksi Leicester Squaren ja Covent Gardenin välillä on kaksisataakuusikymmentä metriä, ja silti kaikki menevät junalla.

Koko teksti, lähteet ja käännökset: https://theresmoretoit-channel.github.io/fi/videos/maps-are-lying/

Luvut
00:00 Kartta, jonka olet nähnyt tuhat kertaa
00:35 Jokaisen tasokartan on valehdeltava
01:15 Gauss todistaa, että se on mahdotonta
02:07 Mercator, 1569
02:36 Hinta: nelin-, kymmenen- ja kahdeksankymmenkertaisesti
03:42 Korjataan se sitten
04:21 Boston ottaa Mercatorin seinältä
05:10 Kumpi kuva on oikea?
05:28 Karttapallo
05:56 Ei aivan
06:35 Miten karttapallo tehdään
06:58 Projektio ja esitys
07:17 Paras koskaan piirretty kartta
08:27 Kartta taskussasi
09:21 Mitä se pyrkii kuvaamaan tarkasti?

KUVALÄHTEET
Kaikki videon arkistokuvat ovat public domainia.

Rantaviiva-aineisto: Natural Earth (naturalearthdata.com), public domain.

Tekstitykset on kirjoitettu tätä videota varten, ei luotu automaattisesti. Toisena ääniraitana on amerikanenglanti.
```

## français (`fr`)

```
Pourquoi les cartes nous mentent-elles ?
```

```
Regardez une carte du monde. Le Groenland est là-haut, à côté du Canada,
à peu près de la taille de l'Afrique. Sauf que l'Afrique est quatorze
fois plus grande, et la carte ne se trompe pas : elle fait exactement ce
pour quoi elle a été conçue.

Toute carte plate de la Terre doit mentir. Pas par erreur, par
nécessité. En 1827, Carl Friedrich Gauss l'a démontré : la courbure
d'une surface appartient à la surface elle-même, on ne peut donc pas
aplatir une sphère sans l'étirer ni la déchirer. Les cartographes ont
renoncé et se sont mis à choisir quel mensonge raconter.

Mercator a choisi la navigation, et le prix est arithmétique. Oslo
occupe quatre fois la surface qu'elle a. Le centre du Groenland, dix
fois. La pointe nord, plus de quatre-vingts. Le Groenland est plus petit
que le Congo et que l'Algérie, et l'Amérique du Sud, qui paraît plus
petite sur cette carte, est plus de huit fois plus grande.

Corrigez les surfaces et les formes se cassent. Corrigez les formes et
les surfaces se cassent. En 2017, les écoles de Boston ont retiré
Mercator de leurs murs, et la carte qu'elles ont accrochée à la place
n'est pas non plus la vraie.

Reste le globe. Rien d'aplati, rien d'étiré, les pôles simplement là.
Sauf que la Terre n'est pas une sphère, l'Everest sur un globe scolaire
mesurerait deux dixièmes de millimètre, et un globe s'imprime à plat :
sur douze fuseaux effilés, collés ensuite sur une boule. C'est l'orange
du début de la vidéo, à l'envers.

Le globe résout donc le problème de la projection. Il ne résout pas le
problème de la représentation. Et toute l'affaire tient dans cette
différence : voilà pourquoi la meilleure carte jamais dessinée se trompe
sur presque toute la géographie, et pourquoi Leicester Square et Covent
Garden sont à deux cent soixante mètres alors que tout le monde prend
quand même le métro.

Transcription complète, sources et traductions : https://theresmoretoit-channel.github.io/fr/videos/maps-are-lying/

Chapitres
00:00 Une carte que vous avez vue mille fois
00:35 Toute carte plane doit mentir
01:15 Gauss prouve que c'est impossible
02:07 Mercator, 1569
02:36 Le prix : quatre fois, dix fois, quatre-vingts
03:42 Alors corrigeons-la
04:21 Boston décroche Mercator du mur
05:10 Quelle photographie est la bonne ?
05:28 Un globe
05:56 Pas tout à fait
06:35 Comment on fabrique un globe
06:58 Projection et représentation
07:17 La meilleure carte jamais dessinée
08:27 La carte dans votre poche
09:21 Que cherche-t-elle à représenter fidèlement ?

CRÉDITS ICONOGRAPHIQUES
Toutes les images d’archive de cette vidéo sont dans le domaine public.

Données de trait de côte : Natural Earth (naturalearthdata.com), domaine public.

Les sous-titres sont écrits pour cette vidéo, pas générés automatiquement. Une piste audio en anglais américain est disponible en seconde piste.
```

## Bahasa Indonesia (`id`)

```
Kenapa Peta Berbohong kepada Kita?
```

```
Lihat peta dunia. Greenland duduk di atas sana di sebelah Kanada, kira-kira sebesar Afrika. Hanya saja Afrika empat belas kali lebih besar — dan peta itu tidak sedang keliru. Ia melakukan persis apa yang memang dirancang untuk dilakukannya.

Setiap peta datar Bumi harus berbohong. Bukan karena kebetulan, tapi karena keharusan. Pada 1827 Carl Friedrich Gauss membuktikannya: kelengkungan sebuah permukaan adalah milik permukaan itu sendiri, jadi kamu tidak bisa mendatarkan bola tanpa meregangkan atau merobeknya. Para kartograf berhenti mencoba dan mulai memilih kebohongan mana yang akan mereka ceritakan.

Mercator memilih navigasi, dan harganya adalah aritmetika. Di peta, luas Oslo menjadi empat kali luas sebenarnya. Bagian tengah Greenland sepuluh kali. Ujung utaranya lebih dari delapan puluh kali. Greenland lebih kecil daripada Kongo dan lebih kecil daripada Aljazair, dan Amerika Selatan — yang di peta itu tampak lebih kecil — lebih dari delapan kali lebih besar.

Perbaiki luasnya, bentuknya yang rusak. Perbaiki bentuknya, luasnya yang rusak. Pada 2017 sekolah-sekolah negeri di Boston menurunkan Mercator dari dinding kelas — dan peta yang mereka pasang sebagai gantinya juga bukan peta yang benar.

Tinggal globe. Tidak ada yang didatarkan, tidak ada yang diregangkan, kutubnya memang ada di sana. Hanya saja Bumi bukan bola, Everest di globe sekolah akan setinggi dua persepuluh milimeter, dan globe dicetak dalam keadaan datar — pada dua belas bilah yang meruncing, lalu ditempelkan ke bola. Ini jeruk dari awal video, diputar mundur.

Jadi globe menyelesaikan masalah proyeksi. Ia tidak menyelesaikan masalah representasi. Dan justru pada perbedaan itulah seluruh persoalannya — itulah sebabnya peta terbaik yang pernah dibuat justru menggambarkan geografi dengan hampir sepenuhnya keliru, dan sebabnya Leicester Square dan Covent Garden hanya berjarak dua ratus enam puluh meter sementara semua orang naik kereta.

Transkrip lengkap, sumber, dan terjemahan: https://theresmoretoit-channel.github.io/id/videos/maps-are-lying/

Bab
00:00 Peta yang sudah kamu lihat ribuan kali
00:35 Setiap peta datar harus berbohong
01:15 Gauss membuktikan bahwa itu mustahil
02:07 Mercator, 1569
02:36 Harganya: empat kali, sepuluh kali, delapan puluh
03:42 Kalau begitu kita perbaiki
04:21 Boston menurunkan Mercator dari dinding
05:10 Foto yang mana yang benar?
05:28 Sebuah globe
05:56 Tidak sepenuhnya
06:35 Bagaimana globe dibuat
06:58 Proyeksi, dan representasi
07:17 Peta terbaik yang pernah dibuat
08:27 Peta di sakumu
09:21 Apa yang ingin digambarkannya secara akurat?

KREDIT GAMBAR
Semua gambar arsip dalam video ini berada dalam domain publik.

Data garis pantai: Natural Earth (naturalearthdata.com), domain publik.

Subtitel ditulis khusus untuk video ini, bukan dibuat secara otomatis. Tersedia juga trek audio kedua dalam bahasa Inggris Amerika.
```

## italiano (`it`)

```
Perché le carte ci mentono?
```

```
Guardi una carta del mondo. La Groenlandia sta lassù accanto al Canada,
grande più o meno quanto l'Africa. Solo che l'Africa è quattordici volte
più grande, e la carta non sta sbagliando: fa esattamente ciò per cui è
stata costruita.

Ogni carta piana della Terra deve mentire. Non per errore, per
necessità. Nel 1827 Carl Friedrich Gauss lo dimostrò: la curvatura di
una superficie appartiene alla superficie stessa, quindi una sfera non
si può appiattire senza tirarla o strapparla. I cartografi hanno smesso
di provarci e hanno cominciato a scegliere quale bugia raccontare.

Mercatore scelse la navigazione, e il prezzo è aritmetico. Oslo occupa
quattro volte l'area che ha. Il centro della Groenlandia dieci volte. La
punta settentrionale più di ottanta. La Groenlandia è più piccola del
Congo e dell'Algeria, e il Sudamerica, che su quella carta sembra più
piccolo, è più di otto volte più grande.

Aggiusti le aree e si rompono le forme. Aggiusti le forme e si rompono
le aree. Nel 2017 le scuole di Boston tolsero Mercatore dalle pareti, e
la carta che appesero al suo posto non è più vera.

Resta il mappamondo. Niente appiattito, niente allungato, i poli
semplicemente lì. Solo che la Terra non è una sfera, l'Everest su un
mappamondo scolastico sarebbe alto due decimi di millimetro, e un
mappamondo si stampa piatto: su dodici fusi rastremati, poi incollati su
una palla. È l'arancia dell'inizio del video, al contrario.

Il mappamondo risolve dunque il problema della proiezione. Non risolve
il problema della rappresentazione. E in quella differenza sta tutto:
per questo la migliore carta mai disegnata sbaglia quasi tutta la
geografia, e per questo Leicester Square e Covent Garden distano
duecentosessanta metri e tutti prendono lo stesso la metropolitana.

Trascrizione completa, fonti e traduzioni: https://theresmoretoit-channel.github.io/it/videos/maps-are-lying/

Capitoli
00:00 Una carta che hai visto mille volte
00:35 Ogni carta piana deve mentire
01:15 Gauss dimostra che è impossibile
02:07 Mercator, 1569
02:36 Il prezzo: quattro volte, dieci volte, ottanta
03:42 E allora sistemiamola
04:21 Boston toglie Mercator dal muro
05:10 Quale fotografia è quella giusta?
05:28 Un mappamondo
05:56 Non del tutto
06:35 Come si fa un mappamondo
06:58 Proiezione e rappresentazione
07:17 La migliore carta mai disegnata
08:27 La mappa che hai in tasca
09:21 Che cosa cerca di azzeccare?

CREDITI DELLE IMMAGINI
Tutte le immagini d’archivio di questo video sono di pubblico dominio.

Dati delle linee di costa: Natural Earth (naturalearthdata.com), pubblico dominio.

I sottotitoli sono scritti per questo video, non generati automaticamente. Come seconda traccia audio è disponibile l’inglese americano.
```

## Deutsch (`de`)

```
Warum lügen uns die Karten an?
```

```
Schauen Sie sich eine Weltkarte an. Grönland liegt oben neben Kanada,
ungefähr so groß wie Afrika. Nur ist Afrika vierzehnmal größer — und die
Karte macht keinen Fehler. Sie tut genau das, wofür sie gebaut wurde.

Jede flache Erdkarte muss lügen. Nicht aus Versehen, aus Notwendigkeit.
1827 bewies Carl Friedrich Gauß es: Die Krümmung einer Fläche gehört zur
Fläche selbst, also lässt sich eine Kugel nicht flach machen, ohne sie
zu dehnen oder zu zerreißen. Die Kartografen gaben es auf und begannen
stattdessen zu wählen, welche Lüge sie erzählen.

Mercator wählte die Navigation, und der Preis ist Arithmetik. Oslo nimmt
viermal so viel Fläche ein, wie es hat. Die Mitte Grönlands zehnmal. Die
Nordspitze mehr als achtzigmal. Grönland ist kleiner als der Kongo und
kleiner als Algerien, und Südamerika, das auf dieser Karte kleiner
wirkt, ist mehr als achtmal größer.

Reparieren Sie die Flächen, und die Formen brechen. Reparieren Sie die
Formen, und die Flächen brechen. 2017 nahmen die Schulen in Boston
Mercator von den Wänden — und die Karte, die sie stattdessen aufhängten,
ist auch nicht die wahre.

Bleibt der Globus. Nichts flachgedrückt, nichts gedehnt, die Pole
einfach da. Nur ist die Erde keine Kugel, der Everest wäre auf einem
Schulglobus zwei Zehntelmillimeter hoch, und ein Globus wird flach
gedruckt — auf zwölf zulaufenden Streifen, die dann auf eine Kugel
geklebt werden. Es ist die Orange vom Anfang des Videos, rückwärts.

Der Globus löst also das Problem der Projektion. Er löst nicht das
Problem der Darstellung. Und genau in diesem Unterschied steckt alles —
deshalb bekommt die beste je gezeichnete Karte die Geografie fast
vollständig falsch, und deshalb liegen Leicester Square und Covent
Garden zweihundertsechzig Meter auseinander, und alle nehmen trotzdem
die Bahn.

Vollständiger Text, Quellen und Übersetzungen: https://theresmoretoit-channel.github.io/de/videos/maps-are-lying/

Kapitel
00:00 Eine Karte, die Sie tausendmal gesehen haben
00:35 Jede flache Karte muss lügen
01:15 Gauß beweist, dass es unmöglich ist
02:07 Mercator, 1569
02:36 Der Preis: viermal, zehnmal, achtzigmal
03:42 Dann korrigieren wir es
04:21 Boston nimmt Mercator von der Wand
05:10 Welches Foto ist richtig?
05:28 Ein Globus
05:56 Nicht ganz
06:35 Wie ein Globus entsteht
06:58 Projektion und Darstellung
07:17 Die beste Karte, die je gezeichnet wurde
08:27 Die Karte in Ihrer Tasche
09:21 Was will sie richtig machen?

BILDNACHWEIS
Alle Archivbilder in diesem Video sind gemeinfrei.

Küstenliniendaten: Natural Earth (naturalearthdata.com), gemeinfrei.

Die Untertitel wurden für dieses Video geschrieben, nicht automatisch erzeugt. Als zweite Tonspur steht amerikanisches Englisch bereit.
```

## polski (`pl`)

```
Dlaczego mapy nas okłamują?
```

```
Proszę spojrzeć na mapę świata. Grenlandia leży na górze obok Kanady,
mniej więcej wielkości Afryki. Tyle że Afryka jest czternaście razy
większa, a mapa się nie myli: robi dokładnie to, do czego ją zbudowano.

Każda płaska mapa Ziemi musi kłamać. Nie przez pomyłkę, z konieczności.
W 1827 roku udowodnił to Carl Friedrich Gauss: krzywizna powierzchni
należy do samej powierzchni, więc kuli nie da się spłaszczyć bez
rozciągnięcia albo rozdarcia. Kartografowie przestali próbować i zaczęli
zamiast tego wybierać, które kłamstwo opowiedzieć.

Mercator wybrał nawigację, a ceną jest arytmetyka. Oslo zajmuje
czterokrotnie większą powierzchnię, niż ma. Środek Grenlandii
dziesięciokrotnie. Północny cypel ponad osiemdziesiąt razy. Grenlandia
jest mniejsza niż Kongo i niż Algieria, a Ameryka Południowa, która na
tej mapie wygląda na mniejszą, jest ponad osiem razy większa.

Naprawimy powierzchnie i rozsypią się kształty. Naprawimy kształty i
rozsypią się powierzchnie. W 2017 roku szkoły w Bostonie zdjęły
Mercatora ze ścian, a mapa, którą powiesiły zamiast niego, też nie jest
tą prawdziwą.

Zostaje globus. Nic nie spłaszczone, nic nie rozciągnięte, bieguny po
prostu są. Tyle że Ziemia nie jest kulą, Everest na szkolnym globusie
miałby dwie dziesiąte milimetra, a globus drukuje się na płasko: na
dwunastu zwężających się pasach, które potem nakleja się na kulę. To ta
pomarańcza z początku filmu, puszczona od tyłu.

Globus rozwiązuje więc problem odwzorowania. Nie rozwiązuje problemu
reprezentacji. I w tej właśnie różnicy mieści się wszystko — dlatego
najlepsza mapa, jaką kiedykolwiek narysowano, myli się niemal w całej
geografii, i dlatego Leicester Square i Covent Garden dzieli dwieście
sześćdziesiąt metrów, a ludzie i tak jadą metrem.

Pełna transkrypcja, źródła i tłumaczenia: https://theresmoretoit-channel.github.io/pl/videos/maps-are-lying/

Rozdziały
00:00 Mapa, którą widziałeś tysiąc razy
00:35 Każda płaska mapa musi kłamać
01:15 Gauss dowodzi, że to niemożliwe
02:07 Mercator, 1569
02:36 Cena: cztery razy, dziesięć razy, osiemdziesiąt
03:42 To ją naprawmy
04:21 Boston zdejmuje Mercatora ze ściany
05:10 Które zdjęcie jest poprawne?
05:28 Globus
05:56 Nie do końca
06:35 Jak powstaje globus
06:58 Odwzorowanie i reprezentacja
07:17 Najlepsza mapa, jaką narysowano
08:27 Mapa w twojej kieszeni
09:21 Co próbuje oddać wiernie?

ŹRÓDŁA ILUSTRACJI
Wszystkie archiwalne ilustracje w tym filmie są w domenie publicznej.

Dane linii brzegowej: Natural Earth (naturalearthdata.com), domena publiczna.

Napisy są pisane do tego filmu, nie generowane automatycznie. Jako druga ścieżka dźwiękowa dostępny jest angielski amerykański.
```

## português (Brasil) (`pt-BR`)

```
Por que os mapas mentem para nós?
```

```
Olhe um mapa-múndi. A Groenlândia fica lá em cima ao lado do Canadá,
mais ou menos do tamanho da África. Só que a África é catorze vezes
maior, e o mapa não está errando: ele faz exatamente aquilo para o que
foi construído.

Todo mapa plano da Terra precisa mentir. Não por engano, por
necessidade. Em 1827 Carl Friedrich Gauss provou: a curvatura de uma
superfície pertence à própria superfície, então não dá para achatar uma
esfera sem esticá-la ou rasgá-la. Os cartógrafos desistiram e passaram a
escolher qual mentira contar.

Mercator escolheu a navegação, e o preço é aritmético. Oslo ocupa quatro
vezes a área que tem. O meio da Groenlândia, dez vezes. A ponta norte,
mais de oitenta. A Groenlândia é menor que o Congo e menor que a
Argélia, e a América do Sul, que naquele mapa parece menor, é mais de
oito vezes maior.

Conserte as áreas e as formas quebram. Conserte as formas e as áreas
quebram. Em 2017 as escolas de Boston tiraram Mercator das paredes, e o
mapa que penduraram no lugar também não é o verdadeiro.

Resta o globo. Nada achatado, nada esticado, os polos simplesmente lá.
Só que a Terra não é uma esfera, o Everest num globo escolar teria dois
décimos de milímetro, e um globo é impresso plano: em doze faixas
afiladas, depois coladas numa bola. É a laranja do começo do vídeo, de
trás para frente.

O globo resolve então o problema da projeção. Não resolve o problema da
representação. E é nessa diferença que está tudo: por isso o melhor mapa
já desenhado erra quase toda a geografia, e por isso Leicester Square e
Covent Garden ficam a duzentos e sessenta metros e todo mundo pega o
trem mesmo assim.

Transcrição completa, fontes e traduções: https://theresmoretoit-channel.github.io/pt-br/videos/maps-are-lying/

Capítulos
00:00 Um mapa que você já viu mil vezes
00:35 Todo mapa plano precisa mentir
01:15 Gauss prova que é impossível
02:07 Mercator, 1569
02:36 O preço: quatro vezes, dez vezes, oitenta
03:42 Então vamos corrigir
04:21 Boston tira Mercator da parede
05:10 Qual fotografia está certa?
05:28 Um globo
05:56 Não totalmente
06:35 Como se faz um globo
06:58 Projeção e representação
07:17 O melhor mapa já desenhado
08:27 O mapa no seu bolso
09:21 O que ele tenta acertar?

CRÉDITOS DE IMAGEM
Todas as imagens de arquivo deste vídeo estão em domínio público.

Dados de linha de costa: Natural Earth (naturalearthdata.com), domínio público.

As legendas foram escritas para este vídeo, não geradas automaticamente. Como segunda faixa de áudio está disponível o inglês americano.
```

## Türkçe (`tr`)

```
Haritalar Bize Neden Yalan Söyler?
```

```
Bir dünya haritasına bak. Grönland yukarıda, Kanada’nın yanında, aşağı yukarı Afrika büyüklüğünde oturuyor. Ama Afrika on dört kat daha büyük — ve harita yanlış yapmıyor. Tam olarak ne için yapıldıysa onu yapıyor.

Dünya’nın her düz haritası yalan söylemek zorunda. Kazara değil, zorunluluktan. 1827’de Carl Friedrich Gauss bunu kanıtladı: bir yüzeyin eğriliği yüzeyin kendisine aittir, yani bir küreyi germeden ya da yırtmadan düzleştiremezsin. Haritacılar denemeyi bıraktı ve bunun yerine hangi yalanı söyleyeceklerini seçmeye başladı.

Mercator navigasyonu seçti ve bedeli aritmetik. Oslo sahip olduğu alanın dört katını kaplıyor. Grönland’ın ortası on katını. Kuzey ucu seksen kattan fazlasını. Grönland hem Kongo’dan hem Cezayir’den küçük, ve o haritada daha küçük görünen Güney Amerika sekiz kattan fazla büyük.

Alanları düzelt, biçimler bozulur. Biçimleri düzelt, alanlar bozulur. 2017’de Boston’daki devlet okulları Mercator’u sınıf duvarlarından indirdi — ve yerine astıkları harita da doğru olan değil.

Geriye yer küresi kalıyor. Düzleştirme yok, germe yok, kutuplar öylece yerinde. Ama Dünya bir küre değil, Everest, okullarda kullanılan bir yer küresinde iki onda bir milimetre yükseklikte olurdu. Yer küresinin haritası önce düz kâğıt şeritlere basılır — on iki tane incelen şerit — sonra bu şeritler bir topun üzerine yapıştırılır. Videonun başındaki portakalın ta kendisi, tersten.

Yani yer küresi izdüşüm sorununu çözüyor. Temsil sorununu çözmüyor. Ve bütün mesele tam da bu ayrımda — çizilmiş en iyi haritanın coğrafyayı neredeyse baştan sona yanlış vermesinin sebebi bu, ve Leicester Square ile Covent Garden arasında iki yüz altmış metre olmasına rağmen herkesin metroya binmesinin sebebi de bu.

Metnin tamamı, kaynaklar ve çeviriler: https://theresmoretoit-channel.github.io/tr/videos/maps-are-lying/

Bölümler
00:00 Bin kez gördüğün bir harita
00:35 Her düz harita yalan söylemek zorunda
01:15 Gauss bunun imkânsız olduğunu kanıtlıyor
02:07 Mercator, 1569
02:36 Bedeli: dört kat, on kat, seksen
03:42 O zaman düzeltelim
04:21 Boston Mercator'u duvardan indiriyor
05:10 Hangi fotoğraf doğru?
05:28 Bir yer küresi
05:56 Tam olarak değil
06:35 Bir yer küresi nasıl yapılır
06:58 İzdüşüm ve temsil
07:17 Çizilmiş en iyi harita
08:27 Cebindeki harita
09:21 Neyi doğru vermeye çalışıyor?

GÖRSEL KAYNAKLARI
Bu videodaki tüm arşiv görselleri kamu malıdır.

Kıyı çizgisi verileri: Natural Earth (naturalearthdata.com), kamu malı.

Altyazılar bu video için yazıldı, otomatik olarak oluşturulmadı. İkinci ses parçası olarak Amerikan İngilizcesi de mevcut.
```

## українська (`uk`)

```
Чому мапи нам брешуть?
```

```
Подивися на мапу світу. Ґренландія сидить там угорі поруч із Канадою, приблизно завбільшки з Африку. От тільки Африка вчотирнадцятеро більша — і мапа не помиляється. Вона робить рівно те, для чого її створили.

Кожна пласка мапа Землі мусить брехати. Не випадково, а з необхідності. 1827 року Карл Фрідріх Гаусс це довів: кривина поверхні належить самій поверхні, тож кулю не можна розпластати, не розтягнувши або не розірвавши її. Картографи облишили спроби й почали натомість обирати, яку брехню розповісти.

Меркатор обрав навігацію, і ціна — арифметична. Осло займає вчетверо більшу площу, ніж має. Середина Ґренландії — вдесятеро. Північний край — більш ніж у вісімдесят разів. Ґренландія менша за Конго і менша за Алжир, а Південна Америка, яка на тій мапі виглядає меншою, більша ніж увосьмеро.

Виправ площі — розсиплються форми. Виправ форми — розсиплються площі. У 2017 році державні школи Бостона зняли Меркатора зі стін класів — і мапа, яку вони повісили натомість, теж не є правдивою.

Лишається глобус. Нічого не сплющено, нічого не розтягнуто, полюси просто є. От тільки Земля не куля, Еверест на шкільному глобусі мав би дві десяті міліметра заввишки, а карту для глобуса друкують на пласкому папері — на дванадцяти смугах, що звужуються до кінців, які потім наклеюють на кулю. Це ніби процес із апельсином на початку відео, тільки у зворотному напрямку.

Отже, глобус розв’язує проблему проєкції. Він не розв’язує проблему репрезентації. І саме в цій різниці вся суть — тому найкраща мапа з усіх намальованих передає географію майже повністю хибно, і тому Лестер-сквер і Ковент-Ґарден розділяють двісті шістдесят метрів, а всі однаково їдуть метро.

Повний текст, джерела та переклади: https://theresmoretoit-channel.github.io/uk/videos/maps-are-lying/

Розділи
00:00 Мапа, яку ти бачив тисячу разів
00:35 Кожна пласка мапа мусить брехати
01:15 Гаусс доводить, що це неможливо
02:07 Меркатор, 1569
02:36 Ціна: вчетверо, вдесятеро, у вісімдесят разів
03:42 То виправмо це
04:21 Бостон знімає Меркатора зі стіни
05:10 Яка фотографія правильна?
05:28 Глобус
05:56 Не зовсім
06:35 Як роблять глобус
06:58 Проєкція і репрезентація
07:17 Найкраща мапа з усіх намальованих
08:27 Мапа у твоїй кишені
09:21 Що вона намагається передати правильно?

ДЖЕРЕЛА ЗОБРАЖЕНЬ
Усі архівні зображення в цьому відео — суспільне надбання.

Дані берегових ліній: Natural Earth (naturalearthdata.com), суспільне надбання.

Субтитри написані для цього відео, а не згенеровані автоматично. Також доступна друга звукова доріжка — американською англійською.
```

## Tiếng Việt (`vi`)

```
Vì sao bản đồ nói dối chúng ta?
```

```
Hãy nhìn một tấm bản đồ thế giới. Greenland nằm trên đó cạnh Canada, to xấp xỉ châu Phi. Chỉ có điều châu Phi lớn gấp mười bốn lần — và bản đồ không hề nhầm. Nó đang làm đúng cái việc mà nó được tạo ra để làm.

Mọi bản đồ phẳng của Trái Đất đều phải nói dối. Không phải do vô tình, mà do bắt buộc. Năm 1827 Carl Friedrich Gauss đã chứng minh điều đó: độ cong của một mặt thuộc về chính mặt ấy, nên bạn không thể trải phẳng một hình cầu mà không kéo giãn hay xé rách nó. Các nhà làm bản đồ không còn cố làm điều đó nữa, và bắt đầu chọn xem sẽ nói dối điều gì.

Mercator chọn hàng hải, và cái giá phải trả là số học. Oslo chiếm diện tích gấp bốn lần thực tế. Phần giữa Greenland gấp mười lần. Mỏm cực bắc hơn tám mươi lần. Greenland nhỏ hơn Congo và nhỏ hơn Algeria, còn Nam Mỹ — nơi trông nhỏ hơn trên tấm bản đồ đó — lớn hơn tám lần.

Giữ đúng diện tích thì hình dạng bị méo. Giữ đúng hình dạng thì diện tích bị sai lệch. Năm 2017 các trường công ở Boston gỡ Mercator khỏi tường lớp học — và tấm bản đồ họ treo lên thay thế cũng chẳng phải tấm đúng.

Vậy còn lại quả địa cầu. Không trải phẳng, không kéo giãn, hai cực cứ thế nằm đó. Chỉ có điều Trái Đất không phải hình cầu, đỉnh Everest trên quả địa cầu dùng trong trường học sẽ cao hai phần mười milimét, và quả địa cầu được in trên mặt phẳng — trên mười hai dải thuôn nhọn, rồi dán lên một quả bóng. Đó chính là quả cam ở đầu video, chạy ngược lại.

Vậy quả địa cầu giải quyết được vấn đề phép chiếu. Nó không giải quyết được vấn đề biểu diễn. Và chính sự khác biệt đó mới là mấu chốt — đó là lý do tấm bản đồ đẹp nhất từng được vẽ lại sai gần như toàn bộ về địa lý, và lý do Leicester Square với Covent Garden chỉ cách nhau hai trăm sáu mươi mét mà ai cũng đi tàu.

Toàn văn, nguồn và bản dịch: https://theresmoretoit-channel.github.io/vi/videos/maps-are-lying/

Các chương
00:00 Tấm bản đồ bạn đã thấy cả nghìn lần
00:35 Mọi bản đồ phẳng đều phải nói dối
01:15 Gauss chứng minh điều đó là không thể
02:07 Mercator, 1569
02:36 Cái giá: bốn lần, mười lần, tám mươi
03:42 Vậy thì sửa nó
04:21 Boston gỡ Mercator khỏi tường
05:10 Bức ảnh nào mới đúng?
05:28 Quả địa cầu
05:56 Không hẳn
06:35 Quả địa cầu được làm thế nào
06:58 Phép chiếu và biểu diễn
07:17 Tấm bản đồ đẹp nhất từng được vẽ
08:27 Tấm bản đồ trong túi bạn
09:21 Bản đồ muốn thể hiện đúng điều gì?

NGUỒN HÌNH ẢNH
Mọi hình tư liệu trong video này đều thuộc phạm vi công cộng.

Dữ liệu đường bờ biển: Natural Earth (naturalearthdata.com), phạm vi công cộng.

Phụ đề được viết riêng cho video này, không phải tạo tự động. Có thể chọn tiếng Anh Mỹ ở bản âm thanh thứ hai.
```

## čeština (`cs`)

```
Proč nám mapy lžou?
```

```
Podívejte se na mapu světa. Grónsko sedí nahoře vedle Kanady, zhruba tak
velké jako Afrika. Jenže Afrika je čtrnáctkrát větší — a mapa se nemýlí.
Dělá přesně to, k čemu byla postavená.

Každá plochá mapa Země musí lhát. Ne omylem, z nutnosti. Roku 1827 to
Carl Friedrich Gauss dokázal: zakřivení plochy patří té ploše samotné,
takže kouli nelze narovnat, aniž byste ji natáhli nebo roztrhli.
Kartografové to vzdali a začali místo toho vybírat, kterou lež řeknou.

Mercator si vybral navigaci a cena je aritmetická. Oslo zabírá čtyřikrát
větší plochu, než má. Střed Grónska desetkrát. Severní cíp víc než
osmdesátkrát. Grónsko je menší než Kongo i než Alžírsko a Jižní Amerika,
která na té mapě vypadá menší, je víc než osmkrát větší.

Spravte plochy a rozsypou se tvary. Spravte tvary a rozsypou se plochy.
Roku 2017 sundaly bostonské školy Mercatora ze stěn učeben — a mapa,
kterou pověsily místo něj, není o nic pravdivější.

Zbývá globus. Nic se nezploštilo, nic neroztáhlo, póly prostě jsou.
Jenže Země není koule, Everest by na školním globusu měřil dvě desetiny
milimetru a globus se tiskne na plocho — na dvanáct zužujících se pásů,
které se pak nalepí na kouli. Je to ten pomeranč ze začátku videa,
puštěný pozpátku.

Globus tedy řeší problém zobrazení. Neřeší problém reprezentace. A právě
v tom rozdílu je celá věc — proto je nejlepší mapa, jaká kdy vznikla,
geograficky skoro celá špatně, a proto dělí Leicester Square a Covent
Garden dvě stě šedesát metrů, a lidé stejně jedou metrem.

Celý text, zdroje a překlady: https://theresmoretoit-channel.github.io/cs/videos/maps-are-lying/

Kapitoly
00:00 Mapa, kterou jste viděli tisíckrát
00:35 Každá plochá mapa musí lhát
01:15 Gauss dokazuje, že to nejde
02:07 Mercator, 1569
02:36 Cena: čtyřikrát, desetkrát, osmdesátkrát
03:42 Tak to spravme
04:21 Boston sundává Mercatora ze zdi
05:10 Která fotka je správně?
05:28 Globus
05:56 Ne tak docela
06:35 Jak se vyrábí globus
06:58 Zobrazení a reprezentace
07:17 Nejlepší mapa, jaká kdy vznikla
08:27 Mapa ve vaší kapse
09:21 Co se snaží zachytit správně?

OBRAZOVÉ ZDROJE
Všechny archivní snímky v tomto videu jsou volným dílem.

Data pobřežních linií: Natural Earth (naturalearthdata.com), volné dílo.

Titulky jsou psané pro tohle video, ne strojový přepis. Jako druhá zvuková stopa je k dispozici americká angličtina.
```

## español (`es`)

```
¿Por qué nos mienten los mapas?
```

```
Mire un mapa del mundo. Groenlandia está arriba, junto a Canadá, más o
menos del tamaño de África. Solo que África es catorce veces mayor, y el
mapa no se equivoca: hace exactamente aquello para lo que fue hecho.

Todo mapa plano de la Tierra tiene que mentir. No por error, por
necesidad. En 1827 Carl Friedrich Gauss lo demostró: la curvatura de una
superficie pertenece a la superficie misma, así que no se puede aplanar
una esfera sin estirarla ni romperla. Los cartógrafos dejaron de
intentarlo y empezaron a elegir qué mentira contar.

Mercator eligió la navegación, y el precio es aritmético. Oslo ocupa
cuatro veces la superficie que tiene. El centro de Groenlandia, diez
veces. La punta norte, más de ochenta. Groenlandia es menor que el Congo
y menor que Argelia, y América del Sur, que en ese mapa parece más
pequeña, es más de ocho veces mayor.

Arregle las superficies y se rompen las formas. Arregle las formas y se
rompen las superficies. En 2017 las escuelas de Boston quitaron a
Mercator de las paredes, y el mapa que colgaron en su lugar tampoco es
el verdadero.

Queda el globo terráqueo. Nada aplanado, nada estirado, los polos
simplemente ahí. Solo que la Tierra no es una esfera, el Everest en un
globo escolar mediría dos décimas de milímetro, y un globo se imprime
plano: en doce tiras que se estrechan y luego se pegan sobre una bola.
Es la naranja del principio del vídeo, puesta del revés.

El globo resuelve entonces el problema de la proyección. No resuelve el
problema de la representación. Y en esa diferencia está todo: por eso el
mejor mapa jamás dibujado se equivoca en casi toda la geografía, y por
eso Leicester Square y Covent Garden están a doscientos sesenta metros y
todo el mundo coge el tren igual.

Transcripción completa, fuentes y traducciones: https://theresmoretoit-channel.github.io/es/videos/maps-are-lying/

Capítulos
00:00 Un mapa que has visto mil veces
00:35 Todo mapa plano tiene que mentir
01:15 Gauss demuestra que es imposible
02:07 Mercator, 1569
02:36 El precio: cuatro veces, diez veces, ochenta
03:42 Pues arreglémoslo
04:21 Boston quita a Mercator de la pared
05:10 ¿Qué fotografía es la correcta?
05:28 Un globo terráqueo
05:56 No del todo
06:35 Cómo se hace un globo terráqueo
06:58 Proyección y representación
07:17 El mejor mapa jamás dibujado
08:27 El mapa que llevas en el bolsillo
09:21 ¿Qué intenta acertar?

CRÉDITOS DE IMAGEN
Todas las imágenes de archivo de este vídeo son de dominio público.

Datos de líneas de costa: Natural Earth (naturalearthdata.com), dominio público.

Los subtítulos están escritos para este vídeo, no generados automáticamente. Como segunda pista de audio está disponible el inglés americano.
```

## svenska (`sv`)

```
Varför ljuger kartorna för oss?
```

```
Titta på en världskarta. Grönland ligger där uppe bredvid Kanada,
ungefär lika stort som Afrika. Fast Afrika är fjorton gånger större, och
kartan gör inget fel: den gör precis det den byggdes för.

Varje platt karta över jorden måste ljuga. Inte av misstag, av
nödvändighet. År 1827 bevisade Carl Friedrich Gauss det: en ytas
krökning hör till ytan själv, alltså går ett klot inte att platta till
utan att tänja eller riva sönder det. Kartograferna slutade försöka och
började i stället välja vilken lögn de skulle berätta.

Mercator valde navigationen, och priset är aritmetik. Oslo täcker fyra
gånger den yta staden har. Mitten av Grönland tio gånger. Nordspetsen
mer än åttio. Grönland är mindre än Kongo och mindre än Algeriet, och
Sydamerika, som ser mindre ut på den kartan, är mer än åtta gånger
större.

Laga ytorna så går formerna sönder. Laga formerna så går ytorna sönder.
År 2017 tog skolorna i Boston ner Mercator från väggarna, och kartan de
hängde upp i stället är inte heller den sanna.

Kvar finns jordgloben. Ingenting tillplattat, ingenting uttänjt, polerna
helt enkelt där. Fast jorden är inget klot, Mount Everest på en skolglob
skulle vara två tiondels millimeter hög, och en glob trycks platt: på
tolv avsmalnande remsor som sedan klistras på ett klot. Det är apelsinen
från filmens början, baklänges.

Jordgloben löser alltså projektionens problem. Den löser inte
representationens problem. Och i den skillnaden ligger alltihop — därför
har den bästa karta som någonsin ritats nästan hela geografin fel, och
därför ligger Leicester Square och Covent Garden tvåhundrasextio meter
isär medan alla ändå tar tåget.

Hela texten, källor och översättningar: https://theresmoretoit-channel.github.io/sv/videos/maps-are-lying/

Kapitel
00:00 En karta du har sett tusen gånger
00:35 Varje platt karta måste ljuga
01:15 Gauss bevisar att det är omöjligt
02:07 Mercator, 1569
02:36 Priset: fyra gånger, tio gånger, åttio
03:42 Då fixar vi det
04:21 Boston tar ner Mercator från väggen
05:10 Vilket fotografi är rätt?
05:28 En jordglob
05:56 Inte riktigt
06:35 Hur en jordglob görs
06:58 Projektion och representation
07:17 Den bästa karta som ritats
08:27 Kartan i din ficka
09:21 Vad försöker den återge korrekt?

BILDKÄLLOR
Alla arkivbilder i videon är public domain.

Kustlinjedata: Natural Earth (naturalearthdata.com), public domain.

Undertexterna är skrivna för den här videon, inte automatgenererade. Som andra ljudspår finns amerikansk engelska.
```
