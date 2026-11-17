# Lokalizované názvy a popisy — Why Do We Actually Need Exercise?

Podklad pro **YouTube Studio → video → Podrobnosti → Přidat jazyk**.
Pro každý jazyk jsou tu **dva bloky ke zkopírování**: název a popis.
Kopíruje se **celý blok mezi trojicí zpětných apostrofů**, co je mimo něj,
je poznámka. Anglický originál zůstává v `youtube.md` a nesahá se na něj.

Nahrává je `tools/lokalizace.py`, který čte právě tenhle formát.

Pořadí sekcí je **podle YouTube Studia**, tedy bajtově podle ČESKÉHO
názvu jazyka — proto jsou čeština, španělština a švédština nakonec.
Neodvozuj ho od abecedy kódů; devět videí to takhle mělo špatně právě
proto, že se formát opsal od souseda.

## Co se NEPŘEKLÁDÁ

| | |
|---|---|
| **Hadza** | jméno národa, v cílovém pravopisu, ale ne opisem |
| **Arnold Tibaijuka** | jméno autora snímku v atribuci |
| **název snímku**, **CC BY-SA 4.0**, odkaz na licenci | licenční údaje se nepřekládají |
| **časy kapitol** | musí sedět na vteřinu, jinak je YouTube neuzná |
| **tagy** | YouTube je per-jazyk nemá |

Názvy kapitol se naopak **překládají** — divák je čte v seznamu pod videem.

## Kontrola čísel

V popisu jsou: **1966**, **27 procent**, **pět** mužů, **dvacet** let,
**tři týdny**, **třicet let**, **deset** mužů, **deset tisíc** kroků,
**třináct set**, **dva týdny**. Musí být v každém překladu a nesmí se
změnit. Kapitol je **dvaadvacet** a časy se nepřekládají.

> **Atribuce je POVINNÁ a je uvnitř bloku.** Snímek S34 je z Wikimedia
> Commons pod **CC BY-SA 4.0**, která uvedení autora vyžaduje. Ve všech
> třinácti jazycích tedy musí zůstat jméno Arnold Tibaijuka i odkaz na
> podmínky. Druhý archivní snímek (S19, NASA) je public domain a
> vypisovat se nemusí.

> **Věta o americké audiostopě tu SCHVÁLNĚ NENÍ** — video druhou stopu
> zatím nemá. Až se vyrobí a nahraje, přidá se do každého popisu druhá
> věta odstavce o titulcích; hotové znění pro všech třináct jazyků je
> v `videos/045-why-did-internet-explorer-stop/youtube-preklady.md`.

> **Registr:** čeština **vyká** (viz `notes.md`), takže vykají i němčina,
> ukrajinština, turečtina a indonéština. Finština drží „sinä“
> a vietnamština „bạn“ — tam ta volba není.

## suomi (`fi`)

```
Miksi me oikeastaan tarvitsemme liikuntaa?
```

```
Sanotaan, että liikunta on sinulle hyväksi. Mutta oletko koskaan
pysähtynyt kysymään miksi?

Vuonna 1966 viisi tervettä kaksikymmentävuotiasta vietti kolme viikkoa
vuoteessa. Eivät sairaina, eivät loukkaantuneina — vain makuulla. Kun
tutkijat mittasivat, kuinka paljon happea heidän kehonsa pystyi
käyttämään täydessä rasituksessa, se oli laskenut 27 prosenttia.
Kolmekymmentä vuotta myöhemmin samat viisi miestä palasivat, ja kävi
ilmi, että kolme viikkoa vuoteessa kaksikymppisenä oli tehnyt enemmän
vahinkoa kuin kolme vuosikymmentä tavallista ikääntymistä.

Se luku on oikeastaan se, mistä tässä videossa on kyse, koska se kertoo,
millainen asia keho on. Ei materiakimpale, joka säilyttää muotonsa
kunnes jokin rikkoo sen, vaan järjestelmä, joka kysyy koko ajan yhtä
kysymystä: kuinka paljon minulta vaaditaan?

Siihen ei tarvita sairaalasänkyä. Kymmentä tervettä nuorta miestä
pyydettiin tekemään yksi asia — kävelemään vähemmän, noin
kymmenestätuhannesta askeleesta päivässä tuhanteenkolmeensataan. Kahden
viikon kuluttua heidän lihaksensa olivat mitattavasti huonompia ottamaan
sokeria verestä.

Ilmeinen seuraava askel on syyttää nykyaikaa, ja juuri siinä tämä tarina
yleensä menee pieleen. Siksi tämä video tekee kierroksen tuloksen
kautta, joka mutkistaa asiaa: kun tutkijat mittasivat, kuinka paljon
energiaa Tansanian hadzat oikeasti kuluttavat päivässä, se oli
suunnilleen sama kuin meillä. Sama kehon koko, sama päivän summa. Kaikki
se käveleminen ei näkynyt suurempana lukuna.

Jäljelle jää oudompi kysymys. Jos liikkumisella on näin paljon väliä,
miksi liikkumattomuus ei tunnu miltään?

Luvut
00:00 Liikunta on sinulle hyväksi
00:25 Mikä siis menee pieleen, kun emme liiku?
00:49 Kaksikymmentäseitsemän prosenttia poissa
01:01 Tutkimus odotti kolmekymmentä vuotta
01:16 Kolme viikkoa vastaan kolmekymmentä vuotta
01:42 Lihas on ilmeisin tapaus
01:56 Luu, ja mistä se lähtee ensin
02:19 Ei rapistu — mittaa
02:38 Kymmenestätuhannesta tuhanteenkolmeensataan
03:06 Miksi keho on rakennettu noin?
03:35 Hadzat
04:02 Ja sitten me muut
04:33 Missä tämä tarina yleensä menee pieleen
04:58 He kuluttavat saman verran kuin me
05:25 Miksi siltä ei tunnu?
05:44 Hälytystä ei ole
06:05 Kaksi kerrosta portaita
06:15 Toinen puoli
06:44 Ajatuskoe
07:29 Kolme sukupolvea
07:57 Väärän muotoinen lause
08:11 Ehkä kysymys ei ollutkaan se

Tekstitykset on kirjoitettu tätä videota varten, niitä ei ole luotu
automaattisesti.

KUVALÄHTEET
Back view of hunters walking single-file bush paths in Tanzania
— Arnold Tibaijuka, CC BY-SA 4.0
via Wikimedia Commons
Lisenssi: https://creativecommons.org/licenses/by-sa/4.0

Kaikki muu arkistokuva on public domain -aineistoa.

Kaikki muu kuvamateriaali tässä videossa on piirretty koodilla.
```

## français (`fr`)

```
Pourquoi avons-nous vraiment besoin d'exercice ?
```

```
On dit que l'exercice est bon pour vous. Mais vous êtes-vous déjà demandé
pourquoi ?

En 1966, cinq jeunes hommes de vingt ans en bonne santé ont passé trois
semaines au lit. Ni malades, ni blessés — simplement allongés. Quand les
chercheurs ont mesuré la quantité d'oxygène que leur corps pouvait
utiliser à l'effort maximal, elle avait chuté de 27 pour cent. Trente ans
plus tard, les mêmes cinq hommes sont revenus, et il s'est avéré que
trois semaines au lit à vingt ans avaient fait plus de dégâts que trois
décennies de vieillissement ordinaire.

Ce chiffre, c'est vraiment le sujet de cette vidéo, parce qu'il vous dit
quel genre de chose est un corps. Pas un bloc de matière qui garde sa
forme jusqu'à ce que quelque chose le casse, mais un système qui pose
sans cesse une question : combien d'effort me demande-t-on ?

Il n'y a pas besoin d'un lit d'hôpital pour le voir. On a demandé une
seule chose à dix jeunes hommes en bonne santé — marcher moins, en
passant d'environ dix mille pas par jour à mille trois cents. Deux
semaines plus tard, leurs muscles absorbaient le sucre du sang de façon
mesurablement moins efficace.

Le réflexe suivant est d'accuser la vie moderne, et c'est précisément là
que ce genre de récit déraille. Cette vidéo fait donc un détour par un
résultat qui complique les choses : quand des chercheurs ont mesuré
combien d'énergie les Hadza de Tanzanie dépensent réellement en une
journée, cela donnait à peu près la même chose que chez nous. Même taille
de corps, même total quotidien. Toute cette marche ne s'est pas traduite
par un chiffre plus élevé.

Reste une question plus étrange. Si le mouvement compte à ce point,
pourquoi ne pas bouger ne se sent-il pas du tout ?

Chapitres
00:00 L'exercice est bon pour vous
00:25 Qu'est-ce qui cloche quand on ne le fait pas ?
00:49 Vingt-sept pour cent en moins
01:01 L'étude a attendu trente ans
01:16 Trois semaines contre trente ans
01:42 Le muscle est le cas le plus évident
01:56 L'os, et par où ça commence
02:19 Pas une dégradation — une mesure
02:38 De dix mille pas à mille trois cents
03:06 Pourquoi un corps est-il construit ainsi ?
03:35 Les Hadza
04:02 Pendant ce temps, nous autres
04:33 Où ce récit déraille d'habitude
04:58 Ils dépensent autant que nous
05:25 Pourquoi ne le sent-on pas ?
05:44 Il n'y a aucune alarme
06:05 Deux étages d'escaliers
06:15 La seconde moitié
06:44 Une expérience de pensée
07:29 Trois générations
07:57 La mauvaise forme
08:11 La question n'était peut-être pas celle-là

Les sous-titres ont été écrits pour cette vidéo, ils ne sont pas générés
automatiquement.

CRÉDITS IMAGES
Back view of hunters walking single-file bush paths in Tanzania
— Arnold Tibaijuka, CC BY-SA 4.0
via Wikimedia Commons
Licence : https://creativecommons.org/licenses/by-sa/4.0

Toutes les autres images d'archives sont dans le domaine public.

Tout le reste des visuels de cette vidéo est dessiné par du code.
```

## Bahasa Indonesia (`id`)

```
Kenapa Kita Sebenarnya Butuh Olahraga?
```

```
Orang bilang olahraga itu baik untuk Anda. Tapi pernahkah Anda berhenti
dan bertanya kenapa?

Pada 1966, lima pria sehat berusia dua puluh tahun menghabiskan tiga
minggu di tempat tidur. Tidak sakit, tidak cedera — hanya berbaring.
Ketika para peneliti mengukur berapa banyak oksigen yang bisa dipakai
tubuh mereka saat mengerahkan tenaga penuh, angkanya sudah turun 27
persen. Tiga puluh tahun kemudian lima pria yang sama datang lagi, dan
ternyata tiga minggu berbaring di usia dua puluh merusak lebih banyak
daripada tiga dekade penuaan biasa.

Angka itulah yang sebenarnya menjadi inti video ini, karena angka itu
memberi tahu Anda tubuh itu benda macam apa. Bukan gumpalan materi yang
mempertahankan bentuknya sampai ada yang merusaknya, melainkan sistem
yang terus menanyakan satu hal: seberapa banyak yang diminta dari saya?

Anda tidak butuh ranjang rumah sakit untuk melihatnya. Sepuluh pria muda
yang sehat diminta melakukan satu hal — berjalan lebih sedikit, dari
sekitar sepuluh ribu langkah sehari menjadi seribu tiga ratus. Dua minggu
kemudian otot mereka terukur lebih buruk dalam menarik gula dari darah.

Langkah berikutnya yang paling gampang adalah menyalahkan kehidupan
modern, dan justru di situlah cerita semacam ini biasanya melenceng.
Karena itu video ini memutar lewat satu hasil yang membuatnya lebih
rumit: ketika para peneliti mengukur berapa banyak energi yang
benar-benar dibakar orang Hadza di Tanzania dalam sehari, hasilnya
kurang lebih sama dengan kita. Ukuran tubuh sama, total harian sama.
Semua jalan kaki itu tidak muncul sebagai angka yang lebih besar.

Yang tersisa adalah pertanyaan yang lebih aneh. Kalau gerak sepenting
itu, kenapa tidak bergerak sama sekali tidak terasa?

Bab
00:00 Olahraga itu baik untuk Anda
00:25 Jadi apa yang rusak kalau kita tidak bergerak?
00:49 Dua puluh tujuh persen hilang
01:01 Penelitian itu menunggu tiga puluh tahun
01:16 Tiga minggu melawan tiga puluh tahun
01:42 Otot adalah contoh paling jelas
01:56 Tulang, dan dari mana mulainya
02:19 Bukan membusuk — mengukur
02:38 Dari sepuluh ribu langkah ke seribu tiga ratus
03:06 Jadi kenapa tubuh dibangun seperti itu?
03:35 Orang Hadza
04:02 Sementara itu, kita semua
04:33 Di mana cerita ini biasanya melenceng
04:58 Mereka membakar sebanyak kita
05:25 Kenapa rasanya tidak begitu?
05:44 Tidak ada alarm
06:05 Dua lantai tangga
06:15 Separuh yang kedua
06:44 Sebuah eksperimen pikiran
07:29 Tiga generasi
07:57 Bentuk yang keliru
08:11 Mungkin pertanyaannya bukan itu

Terjemahan teks ditulis khusus untuk video ini, bukan dibuat otomatis.

KREDIT GAMBAR
Back view of hunters walking single-file bush paths in Tanzania
— Arnold Tibaijuka, CC BY-SA 4.0
via Wikimedia Commons
Lisensi: https://creativecommons.org/licenses/by-sa/4.0

Semua gambar arsip lainnya berada dalam domain publik.

Semua visual lain dalam video ini digambar dengan kode.
```

## italiano (`it`)

```
Perché abbiamo davvero bisogno di esercizio?
```

```
Si dice che l'esercizio faccia bene. Ma ti sei mai fermato a chiederti
perché?

Nel 1966 cinque ventenni sani passarono tre settimane a letto. Non
malati, non infortunati — solo sdraiati. Quando i ricercatori misurarono
quanto ossigeno il loro corpo riusciva a usare al massimo sforzo, era
calato del 27 per cento. Trent'anni dopo gli stessi cinque uomini
tornarono, e si scoprì che tre settimane a letto a vent'anni avevano
fatto più danni di trent'anni di normale invecchiamento.

Quel numero è in pratica il tema di questo video, perché ti dice che tipo
di cosa è un corpo. Non un pezzo di materia che mantiene la sua forma
finché qualcosa non lo rompe, ma un sistema che continua a farsi una
domanda: quanto mi si sta chiedendo?

Non serve un letto d'ospedale per vederlo. A dieci giovani uomini sani fu
chiesta una cosa sola — camminare di meno, da circa diecimila passi al
giorno a milletrecento. Due settimane dopo i loro muscoli assorbivano
meno zucchero dal sangue, e la differenza era misurabile.

La mossa successiva più ovvia è dare la colpa alla vita moderna, ed è
esattamente lì che questo tipo di racconto prende la strada sbagliata.
Perciò questo video fa una deviazione attraverso un risultato che
complica le cose: quando i ricercatori hanno misurato quanta energia gli
hadza della Tanzania consumano davvero in un giorno, è venuta fuori più
o meno la stessa nostra. Stessa taglia corporea, stesso totale
giornaliero. Tutto quel camminare non si traduceva in un consumo
maggiore.

Resta una domanda più strana. Se il movimento conta così tanto, perché
non muoversi non si sente per niente?

Capitoli
00:00 L'esercizio fa bene
00:25 Che cosa smette di funzionare se non ci muoviamo?
00:49 Ventisette per cento in meno
01:01 Lo studio ha aspettato trent'anni
01:16 Tre settimane contro trent'anni
01:42 Il muscolo è il caso più evidente
01:56 L'osso, e da dove comincia
02:19 Non si degrada — misura
02:38 Da diecimila passi a milletrecento
03:06 Perché un corpo è fatto così?
03:35 Gli hadza
04:02 Intanto, noi altri
04:33 Dove questo racconto sbaglia di solito
04:58 Consumano quanto noi
05:25 Perché non si sente?
05:44 Non c'è nessun allarme
06:05 Due rampe di scale
06:15 La seconda metà
06:44 Un esperimento mentale
07:29 Tre generazioni
07:57 Il modo sbagliato di dirlo
08:11 Forse la domanda non era quella

I sottotitoli sono scritti per questo video, non generati
automaticamente.

CREDITI IMMAGINI
Back view of hunters walking single-file bush paths in Tanzania
— Arnold Tibaijuka, CC BY-SA 4.0
via Wikimedia Commons
Licenza: https://creativecommons.org/licenses/by-sa/4.0

Tutte le altre immagini d'archivio sono di pubblico dominio.

Tutto il resto delle immagini di questo video è disegnato da codice.
```

## Deutsch (`de`)

```
Warum brauchen wir eigentlich Sport?
```

```
Man sagt, Sport sei gut für Sie. Aber haben Sie sich je gefragt, warum?

1966 verbrachten fünf gesunde Zwanzigjährige drei Wochen im Bett. Nicht
krank, nicht verletzt — einfach liegend. Als die Forscher maßen, wie viel
Sauerstoff ihre Körper bei voller Anstrengung verwerten konnten, war der
Wert um 27 Prozent gefallen. Dreißig Jahre später kamen dieselben fünf
Männer wieder, und es zeigte sich: drei Wochen im Bett mit zwanzig hatten
mehr Schaden angerichtet als drei Jahrzehnte gewöhnliches Älterwerden.

Um diese Zahl geht es in diesem Video eigentlich, denn sie sagt Ihnen,
was für ein Ding ein Körper ist. Kein Klumpen Materie, der seine Form
behält, bis etwas ihn zerbricht, sondern ein System, das ständig eine
Frage stellt: wie viel wird von mir verlangt?

Dafür braucht es kein Krankenhausbett. Zehn gesunde junge Männer bekamen
eine einzige Anweisung — weniger gehen, von etwa zehntausend Schritten am
Tag auf dreizehnhundert. Zwei Wochen später waren ihre Muskeln messbar
schlechter darin, Zucker aus dem Blut zu ziehen.

Der naheliegende nächste Schritt ist, das moderne Leben verantwortlich zu
machen, und genau da geht diese Art von Geschichte gewöhnlich schief.
Dieses Video macht deshalb einen Umweg über ein Ergebnis, das die Sache
verkompliziert: Als Forscher maßen, wie viel Energie die Hadza in
Tansania an einem Tag tatsächlich verbrauchen, kam ungefähr dasselbe
heraus wie bei uns. Gleiche Körpergröße, gleiche Tagessumme. All das
Gehen zeigte sich nicht als größere Zahl.

Bleibt eine seltsamere Frage. Wenn Bewegung so wichtig ist, warum fühlt
sich fehlende Bewegung nach gar nichts an?

Kapitel
00:00 Sport ist gut für Sie
00:25 Was geht schief, wenn wir es nicht tun?
00:49 Siebenundzwanzig Prozent weg
01:01 Die Studie wartete dreißig Jahre
01:16 Drei Wochen gegen dreißig Jahre
01:42 Der Muskel ist der offensichtliche Fall
01:56 Der Knochen, und wo es zuerst beginnt
02:19 Kein Verfall — eine Messung
02:38 Von zehntausend Schritten auf dreizehnhundert
03:06 Warum ist ein Körper so gebaut?
03:35 Die Hadza
04:02 Und wir anderen
04:33 Wo diese Geschichte gewöhnlich schiefgeht
04:58 Sie verbrauchen so viel wie wir
05:25 Warum fühlt es sich nicht so an?
05:44 Es gibt keinen Alarm
06:05 Zwei Stockwerke Treppen
06:15 Die zweite Hälfte
06:44 Ein Gedankenexperiment
07:29 Drei Generationen
07:57 Die falsche Form
08:11 Vielleicht war das nie die Frage

Die Untertitel wurden für dieses Video geschrieben, nicht automatisch
erzeugt.

BILDNACHWEISE
Back view of hunters walking single-file bush paths in Tanzania
— Arnold Tibaijuka, CC BY-SA 4.0
via Wikimedia Commons
Lizenz: https://creativecommons.org/licenses/by-sa/4.0

Alle anderen Archivbilder sind gemeinfrei.

Alles andere Bildmaterial in diesem Video ist aus Code gezeichnet.
```

## polski (`pl`)

```
Dlaczego właściwie potrzebujemy ćwiczeń?
```

```
Mówi się, że ćwiczenia są dla ciebie dobre. Ale czy kiedyś zastanawiałeś
się dlaczego?

W 1966 roku pięciu zdrowych dwudziestolatków spędziło trzy tygodnie w
łóżku. Nie byli chorzy, nie byli ranni — po prostu leżeli. Kiedy badacze
zmierzyli, ile tlenu ich ciała potrafią zużyć przy pełnym wysiłku, wynik
spadł o 27 procent. Trzydzieści lat później ci sami mężczyźni wrócili i
okazało się, że trzy tygodnie w łóżku w wieku dwudziestu lat zrobiły
więcej szkody niż trzy dekady zwykłego starzenia się.

Właśnie o tę liczbę w tym filmie chodzi, bo mówi ci, czym właściwie jest
ciało. Nie bryłą materii, która trzyma kształt, dopóki coś jej nie
złamie, ale układem, który wciąż zadaje jedno pytanie: ile się ode mnie
wymaga?

Nie trzeba do tego szpitalnego łóżka. Dziesięciu zdrowych młodych
mężczyzn dostało jedno polecenie — chodzić mniej, z około dziesięciu
tysięcy kroków dziennie do tysiąca trzystu. Dwa tygodnie później ich
mięśnie wyraźnie gorzej pobierały cukier z krwi.

Naturalny następny ruch to obwinić współczesne życie i właśnie tam ten
rodzaj opowieści zwykle idzie w złą stronę. Dlatego ten film robi objazd
przez wynik, który wszystko komplikuje: kiedy badacze zmierzyli, ile
energii Hadza z Tanzanii naprawdę wydają w ciągu dnia, wyszło mniej
więcej tyle co u nas. Ta sama wielkość ciała, ta sama dzienna suma. Całe
to chodzenie nie przełożyło się na wyższy wynik.

Zostaje dziwniejsze pytanie. Skoro ruch ma takie znaczenie, dlaczego brak
ruchu w ogóle nic nie daje odczuć?

Rozdziały
00:00 Ćwiczenia są dla ciebie dobre
00:25 Co się psuje, kiedy tego nie robimy?
00:49 Dwadzieścia siedem procent w dół
01:01 Badanie czekało trzydzieści lat
01:16 Trzy tygodnie kontra trzydzieści lat
01:42 Mięsień to najbardziej oczywisty przypadek
01:56 Kość i to, od czego się zaczyna
02:19 Nie rozpad — pomiar
02:38 Z dziesięciu tysięcy kroków do tysiąca trzystu
03:06 Dlaczego ciało jest tak zbudowane?
03:35 Hadza
04:02 A tymczasem my
04:33 Gdzie ta opowieść zwykle się psuje
04:58 Wydają tyle samo co my
05:25 Dlaczego tego nie czujemy?
05:44 Nie ma żadnego alarmu
06:05 Dwa piętra schodów
06:15 Druga połowa
06:44 Eksperyment myślowy
07:29 Trzy pokolenia
07:57 Zły kształt zdania
08:11 Może pytanie nigdy nie brzmiało tak

Napisy zostały napisane do tego filmu, nie są generowane automatycznie.

ŹRÓDŁA OBRAZÓW
Back view of hunters walking single-file bush paths in Tanzania
— Arnold Tibaijuka, CC BY-SA 4.0
via Wikimedia Commons
Licencja: https://creativecommons.org/licenses/by-sa/4.0

Wszystkie pozostałe zdjęcia archiwalne są w domenie publicznej.

Cała reszta grafiki w tym filmie jest rysowana kodem.
```

## português (Brasil) (`pt-BR`)

```
Por que a gente realmente precisa de exercício?
```

```
Dizem que exercício faz bem para você. Mas você já parou para perguntar
por quê?

Em 1966, cinco homens saudáveis de vinte anos passaram três semanas na
cama. Não estavam doentes, não estavam machucados — só deitados. Quando
os pesquisadores mediram quanto oxigênio o corpo deles conseguia usar em
esforço máximo, tinha caído 27 por cento. Trinta anos depois os mesmos
cinco homens voltaram, e ficou claro que três semanas na cama aos vinte
tinham causado mais dano do que três décadas de envelhecimento comum.

Esse número é, no fundo, o assunto deste vídeo, porque ele diz para você
que tipo de coisa é um corpo. Não um pedaço de matéria que mantém a forma
até algo quebrá-lo, mas um sistema que fica fazendo uma pergunta: quanto
está sendo pedido de mim?

Não é preciso uma cama de hospital para ver isso. Dez homens jovens e
saudáveis receberam uma única instrução — andar menos, de uns dez mil
passos por dia para mil e trezentos. Duas semanas depois os músculos
deles estavam mensuravelmente piores em puxar açúcar do sangue.

O passo seguinte mais óbvio é culpar a vida moderna, e é exatamente aí
que esse tipo de história costuma dar errado. Por isso este vídeo faz um
desvio por um resultado que complica tudo: quando pesquisadores mediram
quanta energia os hadza da Tanzânia realmente gastam num dia, deu mais ou
menos a mesma que a nossa. Mesmo tamanho de corpo, mesmo total diário.
Toda aquela caminhada não apareceu como um número maior.

Sobra uma pergunta mais estranha. Se o movimento importa tanto, por que
não se mexer não parece nada?

Capítulos
00:00 Exercício faz bem para você
00:25 Então o que dá errado quando não fazemos?
00:49 Vinte e sete por cento a menos
01:01 O estudo esperou trinta anos
01:16 Três semanas contra trinta anos
01:42 O músculo é o caso mais óbvio
01:56 O osso, e por onde começa
02:19 Não é deterioração — é medição
02:38 De dez mil passos para mil e trezentos
03:06 Então por que um corpo é feito assim?
03:35 Os hadza
04:02 Enquanto isso, o resto de nós
04:33 Onde essa história costuma dar errado
04:58 Eles gastam o mesmo que nós
05:25 Por que não parece que importa?
05:44 Não existe alarme
06:05 Dois lances de escada
06:15 A segunda metade
06:44 Um experimento mental
07:29 Três gerações
07:57 O formato errado
08:11 Talvez a pergunta nunca tenha sido essa

As legendas foram escritas para este vídeo, não são geradas
automaticamente.

CRÉDITOS DE IMAGEM
Back view of hunters walking single-file bush paths in Tanzania
— Arnold Tibaijuka, CC BY-SA 4.0
via Wikimedia Commons
Licença: https://creativecommons.org/licenses/by-sa/4.0

Todas as outras imagens de arquivo estão em domínio público.

Todo o resto do visual deste vídeo é desenhado por código.
```

## Türkçe (`tr`)

```
Egzersize Aslında Neden İhtiyacımız Var?
```

```
Egzersizin size iyi geldiği söylenir. Ama hiç durup neden diye sordunuz
mu?

1966'da beş sağlıklı yirmi yaşındaki adam üç haftayı yatakta geçirdi.
Hasta değillerdi, yaralı değillerdi — sadece yatıyorlardı.
Araştırmacılar vücutlarının tam eforda ne kadar oksijen kullanabildiğini
ölçtüklerinde, değer yüzde 27 düşmüştü. Otuz yıl sonra aynı beş adam geri
geldi ve ortaya çıktı ki yirmi yaşında üç hafta yatakta kalmak, otuz
yıllık sıradan yaşlanmadan daha fazla zarar vermişti.

Bu video aslında o sayıyla ilgili, çünkü o sayı size vücudun ne tür bir
şey olduğunu söylüyor. Bir şey onu kırana kadar biçimini koruyan bir
madde yığını değil, sürekli tek bir soru soran bir sistem: benden ne
kadar isteniyor?

Bunu görmek için hastane yatağı gerekmiyor. On sağlıklı genç adamdan tek
bir şey istendi — daha az yürümek, günde yaklaşık on bin adımdan bin üç
yüze. İki hafta sonra kasları kandaki şekeri çekme konusunda ölçülebilir
biçimde kötüleşmişti.

Sıradaki en kolay hamle modern hayatı suçlamak ve bu tür bir anlatı tam
orada yoldan çıkıyor. Bu yüzden video her şeyi karmaşıklaştıran bir
sonuca uğruyor: araştırmacılar Tanzanya'daki Hadza'nın bir günde gerçekte
ne kadar enerji harcadığını ölçtüklerinde, sonuç bizimkiyle aşağı yukarı
aynı çıktı. Aynı vücut ölçüsü, aynı günlük toplam. Bütün o yürüyüş daha
büyük bir sayı olarak görünmedi.

Geriye daha tuhaf bir soru kalıyor. Hareket bu kadar önemliyse, hareket
etmemek neden hiçbir şey hissettirmiyor?

Bölümler
00:00 Egzersiz size iyi gelir
00:25 Peki hareket etmediğimizde ne bozuluyor?
00:49 Yüzde yirmi yedi gitti
01:01 Çalışma otuz yıl bekledi
01:16 Üç haftaya karşı otuz yıl
01:42 Kas en bariz örnek
01:56 Kemik ve nereden başladığı
02:19 Çürüme değil — ölçüm
02:38 On bin adımdan bin üç yüze
03:06 Peki vücut neden böyle kurulmuş?
03:35 Hadza
04:02 Bu arada geri kalanımız
04:33 Bu anlatı genelde nerede yoldan çıkar
04:58 Bizimle aynı enerjiyi harcıyorlar
05:25 Neden öyle hissettirmiyor?
05:44 Hiçbir alarm yok
06:05 İki kat merdiven
06:15 İkinci yarı
06:44 Bir düşünce deneyi
07:29 Üç kuşak
07:57 Yanlış biçim
08:11 Belki asıl soru bu değildi

Altyazılar bu video için yazıldı, otomatik olarak oluşturulmadı.

GÖRSEL KAYNAKLARI
Back view of hunters walking single-file bush paths in Tanzania
— Arnold Tibaijuka, CC BY-SA 4.0
via Wikimedia Commons
Lisans: https://creativecommons.org/licenses/by-sa/4.0

Diğer tüm arşiv görselleri kamu malıdır.

Bu videodaki diğer tüm görseller kodla çizilmiştir.
```

## українська (`uk`)

```
Навіщо нам насправді потрібні вправи?
```

```
Кажуть, що вправи вам корисні. Але чи замислювалися ви колись, чому?

У 1966 році п'ятеро здорових двадцятирічних чоловіків провели три тижні
в ліжку. Не хворі, не травмовані — просто лежали. Коли дослідники
виміряли, скільки кисню їхні тіла здатні використати за повного зусилля,
показник упав на 27 відсотків. Через тридцять років ті самі п'ятеро
повернулися, і виявилося, що три тижні в ліжку у двадцять завдали більше
шкоди, ніж три десятиліття звичайного старіння.

Саме про це число це відео, бо воно каже вам, що таке тіло насправді. Не
шматок матерії, який тримає форму, доки щось його не зламає, а система,
яка постійно ставить одне запитання: скільки від мене вимагають?

Щоб це побачити, лікарняне ліжко не потрібне. Десятьом здоровим молодим
чоловікам дали одну вказівку — ходити менше, приблизно з десяти тисяч
кроків на день до тисячі трьохсот. Через два тижні їхні м'язи помітно
гірше засвоювали цукор із крові.

Найпростіший наступний крок — звинуватити сучасне життя, і саме тут така
розповідь зазвичай іде не туди. Тому це відео робить гак через
результат, який усе ускладнює: коли дослідники виміряли, скільки енергії
хадза в Танзанії насправді витрачають за день, вийшло приблизно стільки
ж, скільки в нас. Той самий розмір тіла, та сама денна сума. Уся та
ходьба не проявилася як більше число.

Лишається дивніше запитання. Якщо рух аж настільки важливий, чому
відсутність руху взагалі ніяк не відчувається?

Розділи
00:00 Вправи вам корисні
00:25 То що ламається, коли ми цього не робимо?
00:49 Двадцять сім відсотків зникло
01:01 Дослідження чекало тридцять років
01:16 Три тижні проти тридцяти років
01:42 М'яз — найочевидніший випадок
01:56 Кістка і з чого це починається
02:19 Не руйнування — вимірювання
02:38 Від десяти тисяч кроків до тисячі трьохсот
03:06 То чому тіло збудоване саме так?
03:35 Хадза
04:02 А тим часом ми
04:33 Де така розповідь зазвичай іде не туди
04:58 Вони витрачають стільки ж, скільки ми
05:25 Чому це так не відчувається?
05:44 Жодної тривоги немає
06:05 Два сходові прольоти
06:15 Друга половина
06:44 Уявний експеримент
07:29 Три покоління
07:57 Неправильна форма
08:11 Можливо, питання було не в тому

Субтитри написані для цього відео, а не створені автоматично.

ДЖЕРЕЛА ЗОБРАЖЕНЬ
Back view of hunters walking single-file bush paths in Tanzania
— Arnold Tibaijuka, CC BY-SA 4.0
via Wikimedia Commons
Ліцензія: https://creativecommons.org/licenses/by-sa/4.0

Усі інші архівні зображення є суспільним надбанням.

Усе інше зображення в цьому відео намальоване кодом.
```

## Tiếng Việt (`vi`)

```
Vì sao chúng ta thực sự cần vận động?
```

```
Người ta bảo tập thể dục thì tốt cho bạn. Nhưng bạn đã bao giờ dừng lại
và hỏi tại sao chưa?

Năm 1966, năm người đàn ông khỏe mạnh hai mươi tuổi nằm trên giường suốt
ba tuần. Không ốm, không chấn thương — chỉ nằm. Khi các nhà nghiên cứu đo
lượng ô-xy mà cơ thể họ có thể dùng khi gắng sức tối đa, con số đã giảm
27 phần trăm. Ba mươi năm sau đúng năm người đó quay lại, và hóa ra ba
tuần nằm giường ở tuổi hai mươi đã gây hại nhiều hơn ba thập kỷ lão hóa
bình thường.

Video này thật ra nói về con số đó, bởi nó cho bạn biết cơ thể là thứ
kiểu gì. Không phải một khối vật chất giữ nguyên hình dạng cho đến khi có
thứ gì làm nó vỡ, mà là một hệ thống liên tục hỏi một câu: người ta đang
đòi hỏi ở tôi bao nhiêu?

Không cần giường bệnh viện để thấy điều đó. Mười người đàn ông trẻ khỏe
mạnh được yêu cầu làm đúng một việc — đi bộ ít hơn, từ khoảng mười nghìn
bước mỗi ngày xuống còn một nghìn ba trăm. Hai tuần sau, khả năng hấp thu
đường từ máu của cơ bắp họ đã giảm đi rõ rệt.

Bước tiếp theo dễ nhất là đổ lỗi cho đời sống hiện đại, và đó chính là
chỗ loại câu chuyện này thường đi chệch hướng. Vì vậy video đi vòng qua
một kết quả làm mọi thứ rắc rối hơn: khi các nhà nghiên cứu đo người Hadza
ở Tanzania thực sự tiêu hao bao nhiêu năng lượng một ngày, kết quả xấp xỉ
bằng của chúng ta. Cùng kích thước cơ thể, cùng tổng mỗi ngày. Tất cả
việc đi bộ đó không hiện ra thành một con số lớn hơn.

Còn lại một câu hỏi lạ lùng hơn. Nếu vận động quan trọng đến thế, vì sao
việc không vận động lại chẳng khiến ta thấy gì cả?

Các phần
00:00 Tập thể dục thì tốt cho bạn
00:25 Vậy điều gì hỏng khi ta không vận động?
00:49 Mất hai mươi bảy phần trăm
01:01 Nghiên cứu đã chờ ba mươi năm
01:16 Ba tuần so với ba mươi năm
01:42 Cơ bắp là ví dụ rõ nhất
01:56 Xương, và bắt đầu từ đâu
02:19 Không mục ruỗng — mà là đo
02:38 Từ mười nghìn bước xuống một nghìn ba trăm
03:06 Vậy vì sao cơ thể được dựng như thế?
03:35 Người Hadza
04:02 Trong khi đó, phần còn lại của chúng ta
04:33 Chỗ câu chuyện này thường đi chệch
04:58 Họ tiêu hao ngang chúng ta
05:25 Vì sao ta không cảm thấy vậy?
05:44 Không có báo động nào cả
06:05 Hai tầng cầu thang
06:15 Nửa sau
06:44 Một thí nghiệm tưởng tượng
07:29 Ba thế hệ
07:57 Cách nói chưa đúng
08:11 Có lẽ câu hỏi chưa bao giờ là thế

Phụ đề được viết riêng cho video này, không phải do máy tạo tự động.

NGUỒN HÌNH ẢNH
Back view of hunters walking single-file bush paths in Tanzania
— Arnold Tibaijuka, CC BY-SA 4.0
via Wikimedia Commons
Giấy phép: https://creativecommons.org/licenses/by-sa/4.0

Tất cả hình ảnh tư liệu khác đều thuộc phạm vi công cộng.

Toàn bộ phần hình còn lại trong video này được vẽ bằng mã.
```

## čeština (`cs`)

```
Proč vlastně potřebujeme cvičit?
```

```
Říká se, že cvičení vám prospívá. Ale zamysleli jste se někdy nad tím
proč?

V roce 1966 strávilo pět zdravých dvacetiletých mužů tři týdny v posteli.
Nebyli nemocní, nebyli zranění — jen leželi. Když výzkumníci změřili,
kolik kyslíku jejich tělo dokáže spotřebovat při plné zátěži, kleslo to o
27 procent. O třicet let později se stejných pět mužů vrátilo a ukázalo
se, že tři týdny v posteli ve dvaceti napáchaly víc škody než tři
desetiletí obyčejného stárnutí.

O tom čísle vlastně celé tohle video je, protože vám říká, co je tělo
zač. Ne kus hmoty, který si drží tvar, dokud ho něco nerozbije, ale
soustava, která si pořád klade jednu otázku: kolik se toho po mně chce?

Nemocniční lůžko k tomu není potřeba. Deset zdravých mladých mužů dostalo
jediný pokyn — chodit míň, ze zhruba deseti tisíc kroků denně na nějakých
třináct set. Po dvou týdnech uměly jejich svaly vytahovat cukr z krve
měřitelně hůř.

Nejsnadnější další krok je svést to na moderní život, a přesně tam se
tenhle druh vyprávění obvykle pokazí. Video proto dělá zajížďku přes
výsledek, který to celé komplikuje: když výzkumníci změřili, kolik
energie Hadzové v Tanzanii za den doopravdy spálí, vyšlo to zhruba stejně
jako nám. Stejná velikost těla, stejný denní součet. Všechna ta chůze se
neprojevila jako vyšší číslo.

Zbývá podivnější otázka. Když na pohybu tolik záleží, proč nehybnost
vůbec nic necítíme?

Kapitoly
00:00 Cvičení vám prospívá
00:25 Tak co se pokazí, když necvičíme?
00:49 Dvacet sedm procent pryč
01:01 Studie počkala třicet let
01:16 Tři týdny proti třiceti letům
01:42 Sval je nejnázornější případ
01:56 Kost a čím to začíná
02:19 Nechátrá — měří
02:38 Z deseti tisíc kroků na třináct set
03:06 Tak proč je tělo postavené takhle?
03:35 Hadzové
04:02 A zatím my ostatní
04:33 Kde se tohle vyprávění obvykle pokazí
04:58 Spálí stejně co my
05:25 Proč to tak necítíme?
05:44 Žádný poplach neexistuje
06:05 Dvě patra schodů
06:15 Druhá půlka
06:44 Myšlenkový experiment
07:29 Tři generace
07:57 Špatný tvar věty
08:11 Možná otázka nikdy nezněla takhle

Titulky jsou k tomuhle videu napsané, ne vygenerované automaticky.

ZDROJE OBRÁZKŮ
Back view of hunters walking single-file bush paths in Tanzania
— Arnold Tibaijuka, CC BY-SA 4.0
via Wikimedia Commons
Licence: https://creativecommons.org/licenses/by-sa/4.0

Všechny ostatní archivní snímky jsou volné dílo.

Všechno ostatní v obraze je kreslené kódem.
```

## español (`es`)

```
¿Por qué necesitamos realmente hacer ejercicio?
```

```
Dicen que el ejercicio es bueno para ti. Pero ¿alguna vez te has parado a
preguntar por qué?

En 1966, cinco hombres sanos de veinte años pasaron tres semanas en cama.
No estaban enfermos, no estaban lesionados — solo tumbados. Cuando los
investigadores midieron cuánto oxígeno podían usar sus cuerpos al máximo
esfuerzo, había caído un 27 por ciento. Treinta años después volvieron
los mismos cinco hombres, y resultó que tres semanas en cama a los veinte
habían hecho más daño que tres décadas de envejecimiento normal.

De ese número va en realidad este vídeo, porque te dice qué clase de cosa
es un cuerpo. No un trozo de materia que mantiene su forma hasta que algo
lo rompe, sino un sistema que se hace una pregunta constantemente:
¿cuánto se me está pidiendo?

No hace falta una cama de hospital para verlo. A diez hombres jóvenes y
sanos les pidieron una sola cosa — caminar menos, de unos diez mil pasos
al día a mil trescientos. Dos semanas después, la capacidad de sus
músculos para extraer azúcar de la sangre había disminuido de forma
medible.

El siguiente paso obvio es culpar a la vida moderna, y ahí es justo donde
esta clase de relato suele torcerse. Por eso el vídeo da un rodeo por un
resultado que lo complica: cuando los investigadores midieron cuánta
energía gastan realmente los hadza de Tanzania en un día, salió más o
menos la misma que la nuestra. Mismo tamaño corporal, mismo total diario.
Todo aquel caminar no se tradujo en un gasto mayor.

Queda una pregunta más extraña. Si el movimiento importa tanto, ¿por qué
no moverse no se nota en absoluto?

Capítulos
00:00 El ejercicio es bueno para ti
00:25 ¿Qué falla cuando no lo hacemos?
00:49 Un veintisiete por ciento menos
01:01 El estudio esperó treinta años
01:16 Tres semanas frente a treinta años
01:42 El músculo es el caso más claro
01:56 El hueso, y por dónde empieza
02:19 No se deteriora — mide
02:38 De diez mil pasos a mil trescientos
03:06 ¿Por qué está hecho así un cuerpo?
03:35 Los hadza
04:02 Mientras tanto, los demás
04:33 Dónde suele torcerse este relato
04:58 Gastan lo mismo que nosotros
05:25 ¿Por qué no se nota?
05:44 No hay ninguna alarma
06:05 Dos pisos de escaleras
06:15 La segunda mitad
06:44 Un experimento mental
07:29 Tres generaciones
07:57 La forma equivocada
08:11 Quizá la pregunta nunca fue esa

Los subtítulos están escritos para este vídeo, no generados
automáticamente.

CRÉDITOS DE IMAGEN
Back view of hunters walking single-file bush paths in Tanzania
— Arnold Tibaijuka, CC BY-SA 4.0
via Wikimedia Commons
Licencia: https://creativecommons.org/licenses/by-sa/4.0

Todas las demás imágenes de archivo son de dominio público.

Todo el resto de lo que se ve en este vídeo está dibujado con código.
```

## svenska (`sv`)

```
Varför behöver vi egentligen träning?
```

```
Man säger att träning är bra för dig. Men har du någonsin stannat upp och
frågat varför?

1966 låg fem friska tjugoåringar i sängen i tre veckor. Inte sjuka, inte
skadade — bara liggande. När forskarna mätte hur mycket syre deras
kroppar kunde använda vid full ansträngning hade det sjunkit med 27
procent. Trettio år senare kom samma fem män tillbaka, och det visade sig
att tre veckor i sängen vid tjugo hade gjort mer skada än tre decennier
av vanligt åldrande.

Det är den siffran den här filmen egentligen handlar om, för den berättar
vad en kropp egentligen är. Inte en klump materia som behåller sin form
tills något förstör den, utan ett system som hela tiden ställer en fråga:
hur mycket krävs det av mig?

Det behövs ingen sjukhussäng för att se det. Tio friska unga män fick en
enda instruktion — gå mindre, från ungefär tiotusen steg om dagen till
trettonhundra. Två veckor senare var deras muskler mätbart sämre på att
ta upp socker ur blodet.

Nästa uppenbara drag är att skylla på det moderna livet, och det är
precis där den här sortens berättelse brukar gå fel. Därför tar filmen en
omväg förbi ett resultat som krånglar till det: när forskare mätte hur
mycket energi hadza i Tanzania faktiskt gör av med på en dag blev det
ungefär lika mycket som hos oss. Samma kroppsstorlek, samma dagssumma.
Allt det där gåendet syntes inte som en högre siffra.

Kvar blir en märkligare fråga. Om rörelse spelar så stor roll, varför
känns det inte alls att låta bli?

Kapitel
00:00 Träning är bra för dig
00:25 Så vad går fel när vi inte gör det?
00:49 Tjugosju procent borta
01:01 Studien väntade i trettio år
01:16 Tre veckor mot trettio år
01:42 Muskler är det tydligaste fallet
01:56 Skelettet, och var det börjar
02:19 Inget förfall — en mätning
02:38 Från tiotusen steg till trettonhundra
03:06 Varför är en kropp byggd så?
03:35 Hadza
04:02 Under tiden, vi andra
04:33 Där den här berättelsen brukar gå fel
04:58 De gör av med lika mycket som vi
05:25 Varför känns det inte så?
05:44 Det finns inget larm
06:05 Två trappor
06:15 Andra halvan
06:44 Ett tankeexperiment
07:29 Tre generationer
07:57 Fel form
08:11 Kanske var frågan aldrig den

Undertexterna är skrivna för den här filmen, inte automatiskt genererade.

BILDKÄLLOR
Back view of hunters walking single-file bush paths in Tanzania
— Arnold Tibaijuka, CC BY-SA 4.0
via Wikimedia Commons
Licens: https://creativecommons.org/licenses/by-sa/4.0

Allt annat arkivmaterial är public domain.

Allt annat bildmaterial i den här filmen är ritat med kod.
```
