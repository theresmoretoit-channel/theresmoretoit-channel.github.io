<!-- S01 -->
Oto wszystkie scenariusze,
jakie kiedykolwiek powstały dla tego kanału.
158 filmów,
prawie półtora miliona bajtów tekstu.

<!-- S02 -->
Przepuśćcie je przez zwykły kompresor
o nazwie gzip.
Wychodzi z tego nieco ponad pół megabajta.
Prawie dwie trzecie znika.

<!-- S03 -->
I nic się nie gubi.
Rozpakujcie plik,
a każdy scenariusz wróci,
litera po literze.

<!-- S04 -->
Teraz skompresujcie go jeszcze raz.

<!-- S05 -->
Robi się większy.
O 98 bajtów większy.

<!-- S06 -->
Trzeci raz.
O 98 bajtów większy.
Czwarty.
Znowu 98.

<!-- S07 -->
Pierwsza runda wyrzuca dwie trzecie.
Druga nie znajduje zupełnie nic.
Czemu więc nie kompresować dalej i dalej?

<!-- S08 -->
Zajrzyjmy do tego drugiego pliku.
gzip niczego nie skompresował.
Przepisał dane bez zmian,
w szesnastu blokach.

<!-- S09 -->
Każdy blok dostał pięciobajtową etykietę.
Dodajcie mały nagłówek i stopkę,
a wyjdzie dokładnie 98.

<!-- S10 -->
Gdy kompresor nie znajduje nic do usunięcia,
zapisuje dane tak, jak są,
i dodaje tylko to, czego potrzeba, żeby to odwrócić.

<!-- S11 -->
Dlaczego więc druga runda nic nie znalazła?
I czy sprytniejszy program by coś znalazł?

<!-- S12 -->
Taki tekst jest pełen powtórzeń.
Te same słowa, te same zwroty,
te same małe znaczniki
na początku każdej sceny.

<!-- S13 -->
W 1977 roku Jacob Ziv i Abraham Lempel
opublikowali prostą sztuczkę.
Nie zapisujcie powtórzenia od nowa.
Wskażcie miejsce, gdzie już było.

<!-- S14 -->
Cofnijcie się o 300 znaków
i skopiujcie kolejnych dwanaście.
Kilka bajtów zamiast dwunastu.

<!-- S15 -->
Druga sztuczka:
częstym literom dać krótkie kody,
a rzadkim długie.

<!-- S16 -->
W 1951 roku David Huffman,
doktorant na MIT,
mógł przystąpić do egzaminu końcowego
albo zamiast niego napisać pracę semestralną.

<!-- S17 -->
Praca, zadana przez Roberta Fano,
polegała na znalezieniu najwydajniejszego kodu
dokładnie tego rodzaju.

<!-- S18 -->
Przez całe miesiące Huffman stał w miejscu.
Poddał się
i zaczął uczyć się do egzaminu.
I wtedy go olśniło.

<!-- S19 -->
Weźcie dwa najrzadsze symbole,
połączcie je w jeden
i powtarzajcie, aż zostanie jedno drzewo.

<!-- S20 -->
Później nazwał to
„najbardziej niezwykłą chwilą w moim życiu”.

<!-- S21 -->
Fano nie powiedział studentom,
że sam się z tym męczył,
podobnie jak Claude Shannon.

<!-- S22 -->
Kod Huffmana pobił metody ich obu.
I da się udowodnić,
że żaden kod tego rodzaju nie jest lepszy.

<!-- S23 -->
Na początku lat 90.
Phil Katz połączył obie sztuczki
w plikach ZIP.
gzip używa tej samej metody.

<!-- S24 -->
Pierwsza runda wykorzystała już
regularności, które gzip potrafi znaleźć.

<!-- S25 -->
W tym, co zostało, nie ma z czym pracować.
Dla gzipa wygląda to jak szum.

<!-- S26 -->
Ale sprytniejszy program
mógłby dostrzec regularności, które gzip przeoczył.
Czy jakiś program mógłby kiedyś
zmniejszyć wszystko, co mu dacie?

<!-- S27 -->
Nie.
I nie musicie wiedzieć, jak działa,
żeby mieć co do tego pewność.

<!-- S28 -->
Weźcie wszystkie pliki
o długości dokładnie trzech bitów.
Jest ich osiem.

<!-- S29 -->
Teraz policzcie wszystkie krótsze.
Cztery pliki dwubitowe,
dwa jednobitowe
i jeden pusty plik.

<!-- S30 -->
Siedem.

<!-- S30b -->
Osiem plików i siedem krótszych miejsc,
gdzie można je umieścić.

<!-- S31 -->
Gdyby każdy się skrócił,
dwa musiałyby dzielić jedno miejsce.
A kiedy je rozpakujecie,
o który wam chodziło?

<!-- S32 -->
To się nazywa zasada szufladkowa Dirichleta
i działa przy każdej długości.
Krótszych plików zawsze jest o jeden mniej,
niż potrzeba.

<!-- S33 -->
Więc każdy kompresor, który przyjmuje dowolny plik
i niektóre zmniejsza,
musi inne powiększać.
Nie dlatego, że jest źle napisany.
Po prostu nie ma ich gdzie podziać.

<!-- S34 -->
Te 98 bajtów
to cena, którą płaci za to gzip.

<!-- S35 -->
Weźcie dowolny kompresor.
Spośród wszystkich plików danej wielkości
o choćby jeden bajt zmniejszy mniej niż jeden
na 250.

<!-- S36 -->
Kompresja i tak działa,
bo pliki, które tworzymy, nie są losowe.
To teksty, obrazy i programy,
pełne regularności.

<!-- S37 -->
Nie powstrzymało to ludzi
przed obiecywaniem więcej.

<!-- S38 -->
W 1992 roku firma WEB Technologies
ogłosiła program, który miał ścisnąć
prawie dowolne dane poniżej kilobajta.
Nawet własny wynik,
raz za razem.

<!-- S39 -->
Jej wiceprezes stwierdził, że metoda
„nie podlega prawom
teorii informacji”.
Produkt nigdy nie trafił na rynek.

<!-- S40 -->
Jak to więc możliwe, że zdjęcia i muzyka
tak bardzo się zmniejszają?
W ogóle nie grają według tej zasady.

<!-- S41 -->
JPEG nie wraca identyczny.
Wraca wystarczająco podobny.
Szczegóły, których braku oko nie zauważy,
są wyrzucane na dobre.

<!-- S42 -->
Przybliżcie,
a zobaczycie, gdzie się podziały.

<!-- S43 -->
To kompresja stratna
i to zupełnie inna gra.
Ten film jest o tym drugim rodzaju.
Każdy bit wraca, co do joty.

<!-- S44 -->
A pliki, które regularności mają:
jak małe mogą się stać?
Czy istnieje dolna granica?

<!-- S45 -->
Jest.
Odkryto je w 1948 roku,
w tej samej pracy, o której mówi nasz film
o kodach korekcyjnych.

<!-- S46 -->
Tam Claude Shannon pokazał,
jak dodana nadmiarowość chroni wiadomość.
Tutaj obliczył,
ile da się jej usunąć.

<!-- S47 -->
Jego odpowiedzią była liczba,
którą nazwał entropią:
jak trudno zgadnąć,
co będzie dalej.

<!-- S48 -->
Żaden kod bezstratny nie zejdzie poniżej tej liczby
średnio.
Ale można się do niej zbliżyć
dowolnie blisko.

<!-- S49 -->
Jak bardzo nieprzewidywalny jest więc angielski?
W 1951 roku Shannon zmierzył to
za pomocą gry.

<!-- S50 -->
Dawał komuś fragment tekstu,
którego ta osoba nigdy nie widziała,
i prosił, żeby go zgadywała,
litera po literze.

<!-- S51 -->
Jeśli się pomyliła,
zgadywała dalej,
aż trafiła.

<!-- S52 -->
Okazało się, że ludzie są w tym bardzo dobrzy.
Przy stu literach kontekstu
angielski wychodził na mniej więcej jeden bit
na literę.

<!-- S53 -->
Komputer zapisuje każdą literę
na ośmiu bitach.
Czytelnikowi wystarcza mniej więcej jeden.

<!-- S54 -->
Tę różnicę wykorzystuje kompresja.
gzip zszedł ze scenariuszami kanału
poniżej trzech bitów na znak.

<!-- S55 -->
Jak blisko jednego bitu
może więc dojść maszyna?

<!-- S56 -->
Jest nagroda właśnie za to.
Nazywa się Hutter Prize,
a od 2020 roku chodzi o skompresowanie jednego pliku:
gigabajt angielskiej Wikipedii.

<!-- S57 -->
gzip zmniejsza go do jednej trzeciej.
Najlepsze zwykłe kompresory
do mniej więcej jednej piątej.

<!-- S58 -->
Rekord z lipca 2026 roku
to nieco ponad sto milionów bajtów.
Jedna dziesiąta.

<!-- S59 -->
Liczy się też dekompresor.
Jego rozmiar wlicza się do wyniku,
więc nie da się schować Wikipedii
w programie.

<!-- S60 -->
Pula nagród wynosi 500 000 euro.
Każdy procent poprawy
to 5000 euro.

<!-- S61 -->
Marcus Hutter, który ją funduje, wyjaśnia dlaczego:
„umiejętność dobrej kompresji
jest ściśle związana
z inteligentnym działaniem”.

<!-- S62 -->
Bo programy z czołówki
nie szukają powtórzeń.
One przewidują.

<!-- S63 -->
Przed każdym znakiem
szacują, jak prawdopodobny jest
każdy możliwy następny znak.
Dobre przewidywanie kosztuje ułamek bitu.

<!-- S64 -->
To gra w zgadywanie Shannona,
w którą gra maszyna.
Najlepsi gracze używają dziś sieci neuronowych,
wytrenowanych, by przewidywać, co będzie dalej.

<!-- S65 -->
To działa nawet na już skompresowanych plikach.
W 2016 roku Dropbox zaczął przepakowywać
JPEG-i swoich użytkowników lepszym predyktorem.
Średnio o ponad jedną piątą mniejsze.

<!-- S66 -->
Każdy plik wracał bit w bit,
a do 2017 roku
zaoszczędziło to ponad 46 petabajtów.
To ponad 46 000 terabajtów.

<!-- S67 -->
Są jeszcze giganci.
W 2023 roku badacze z DeepMind
użyli dużego modelu językowego
jako kompresora.

<!-- S68 -->
Na małych wycinkach zdjęć w skali szarości
pobił PNG:
48% pierwotnego rozmiaru
wobec 58.

<!-- S69 -->
Na nagraniach czytanej mowy
pobił FLAC:
21% wobec 30.

<!-- S70 -->
Ale to bez liczenia samego modelu.
Dodajcie jego rozmiar,
a wynik wychodzi
140 razy
większy niż dane.

<!-- S71 -->
Kompresor większy niż jego dane
niczego nie zaoszczędził.
Program jest częścią opisu.

<!-- S72 -->
I tu dochodzimy do najdziwniejszej części.
Oto pierwszy milion cyfr liczby π.

<!-- S73 -->
Dajcie je czterem kompresorom.
Najlepszy zmniejsza je do około
426 000 bajtów.

<!-- S74 -->
Teraz dajcie tym samym kompresorom
milion losowych cyfr.
Ten sam wynik,
z dokładnością do jednej dziesiątej procenta.

<!-- S75 -->
Ale π nie powstaje losowo.
Rządzi się regułą matematyczną.
Oto program, który wypisuje
każdą z tego miliona cyfr.

<!-- S76 -->
362 bajty.
Ponad dwa tysiące razy krótszy niż plik.

<!-- S77 -->
Kompresory nie widziały
matematycznej reguły stojącej za π.
Widziały tylko cyfry.

<!-- S78 -->
Jeden ze sposobów mierzenia informacji
w danych to zapytać:
jak krótki może być program,
który wciąż je wypisze?

<!-- S79 -->
Ta długość nazywa się
złożonością Kołmogorowa,
od nazwiska jednego z tych, którzy ją opisali.

<!-- S80 -->
Większość danych nie ma krótkiego programu.
To znowu zasada szufladkowa:
krótkich programów po prostu
nie starczy dla wszystkich.

<!-- S81 -->
Miliona losowych cyfr
najpewniej nie da się opisać krócej.
Liczbę π — tak.

<!-- S82 -->
Dlaczego więc po prostu nie znaleźć
najkrótszego programu dla dowolnego pliku?
Bo udowodniono,
że żaden algorytm nie potrafi tego zrobić
dla każdego pliku.

<!-- S83 -->
Każdy program daje wam górne ograniczenie.
Ale nie ma sposobu, by zawsze ustalić,
czy istnieje krótszy.
Nigdy nie wiecie, czy osiągnęliście dolną granicę.

<!-- S84 -->
gzip znalazł w scenariuszach powtórzenia
i nic więcej.
Widzi bajty,
a nie to, co znaczą słowa.

<!-- S85 -->
Żeby pójść dalej, program
musi lepiej je przewidywać.
A dobre przewidywanie tekstu
zaczyna bardzo przypominać jego rozumienie.

<!-- S86 -->
Oto więc pytanie do was.
Gdyby program potrafił ścisnąć Wikipedię
mocniej niż jakikolwiek inny program,
czy powiedzielibyście, że ją rozumie?
Zostawcie odpowiedź w komentarzach.
