<!-- S01 -->
To jest ZX Spectrum, który wczytuje program.

<!-- S02 -->
A to jest ten sam program,
na tym samym komputerze,
z tego samego rodzaju kasety.

<!-- S03 -->
Wczytywanie trwa o połowę krócej.
Sprzęt w ogóle się nie zmienił.
Żadnej szybszej taśmy, żadnego szybszego magnetofonu.

<!-- S04 -->
Zmieniło się tylko jedno:
sposób, w jaki komputer słuchał.

<!-- S05 -->
Jak więc komputery 8-bitowe
nauczyły się szybciej wczytywać gry?
A skoro to było takie proste,
czemu nie robiły tego od początku?

<!-- S06 -->
W jednym z wcześniejszych filmów
widzieliśmy, jak Spectrum zapisuje bity
jako impulsy na taśmie.

<!-- S07 -->
Krótka para impulsów oznacza zero.
Para dwa razy dłuższa oznacza jedynkę.

<!-- S08 -->
To daje około tysiąca czterystu bitów
na sekundę.
Gra, która zapełnia 48K pamięci,
wczytuje się mniej więcej pięć minut.

<!-- S09 -->
A teraz skróć każdy impuls o połowę.

<!-- S10 -->
Komputer nadal odróżnia krótki od długiego.
Ale dwa razy więcej bitów
przechodzi co sekundę obok głowicy.

<!-- S11 -->
Na tym polega cały trik programu ładującego turbo.
I to nie jest tylko eksperyment myślowy.

<!-- S12 -->
W 1984 roku gra Skool Daze
wczytywała swoje dane dwa razy szybciej
niż Spectrum przy normalnej prędkości.

<!-- S13 -->
Czemu więc Spectrum
samo nie wczytywało tak szybko?

<!-- S14 -->
Wbudowany program ładujący siedzi w ROM-ie,
w układzie pamięci, od którego komputer startuje.
Nie mierzy impulsu w sekundach.

<!-- S15 -->
Liczy.
Po każdym zboczu sygnału
chwilę czeka,
a potem liczy, ile czasu minie do następnego.

<!-- S16 -->
Jedna jedyna liczba w ROM-ie
decyduje, gdzie kończy się zero,
a zaczyna jedynka.

<!-- S17 -->
I ta liczba zostawia spory zapas.
Zero może się wydłużyć
o ponad czterdzieści procent
i nadal zostanie odczytane jako zero.

<!-- S18 -->
To dzięki temu zapasowi zużyta taśma
na tanim magnetofonie
nadal się wczytuje.

<!-- S19 -->
I to nie komputer był ograniczeniem.
Spectrum sprawdza sygnał z taśmy
około sześćdziesięciu tysięcy razy na sekundę.

<!-- S20 -->
Ograniczeniem była kaseta.
Krótsze impulsy to wyższe tony.
Przy podwójnej prędkości zero
przesuwa się z dwóch kiloherców na cztery.

<!-- S21 -->
A wysokie tony to dokładnie to, co
tani magnetofon
albo lekko rozregulowana głowica
gubi w pierwszej kolejności.

<!-- S22 -->
Pewien magazyn o Spectrum oceniał w 1986 roku,
że większość ludzi da radę
co najmniej podwoić normalną prędkość.
O ile więcej,
zależało od magnetofonu.

<!-- S23 -->
Ale turbo miało dziwniejszy problem.

<!-- S24 -->
Skoro komputer zna tylko
wolny format,
jak ma wczytać program,
który nauczy go szybkiego?

<!-- S25 -->
Odpowiedź jest na początku taśmy.
Pierwsza część jest nagrana
w zwykłym, wolnym formacie.

<!-- S26 -->
Jest krótka
i ROM wczytuje ją jak każdy inny program.

<!-- S27 -->
Potem ten mały program przejmuje stery.
W najprostszym przypadku
to kopia procedury ładującej z samego ROM-u
z kilkoma zmienionymi liczbami.

<!-- S28 -->
W Skool Daze
zmiany są w trzech miejscach.
Krótsze czekanie, nowa wartość początkowa licznika,
nowy próg.

<!-- S29 -->
Czyli ROM wczytuje program,
który robi robotę ROM-u, tylko szybciej.

<!-- S30 -->
To trochę jak pobrać
szybszy program do pobierania.
Najpierw powoli pobierasz narzędzie.
Narzędzie robi resztę.

<!-- S31 -->
Gry komercyjne korzystały z tego samego pomysłu.
Jednym ze znanych przykładów był Speedlock,
po raz pierwszy użyty przez Ocean w 1984 roku.

<!-- S32 -->
Jeden z jego autorów powiedział, że go napisał,
bo miał już dość tego,
jak długo trwało ładowanie standardowym programem.

<!-- S33 -->
Ale tu jest niespodzianka.
Speedlock był szybszy tylko
mniej więcej półtora raza.

<!-- S34 -->
Pierwszy dzień
gry Daley Thompson's Decathlon
wczytywał się trzy minuty dwadzieścia sekund,
a te same dane przy normalnej prędkości
wczytywałyby się cztery minuty czterdzieści siedem.

<!-- S35 -->
Późniejsze wersje były tylko o jakąś
jedną piątą szybsze od ROM-u.
Bo nie chodziło tylko o szybkość.

<!-- S36 -->
Od 1983 roku programy kopiujące
potrafiły odczytać nagłówek gry
i skopiować całą grę na inną taśmę.

<!-- S37 -->
Własny format
nie dawał tym programom nic do odczytania.

<!-- S38 -->
Wczesny Speedlock dzielił nawet swój ton pilota
na krótkie serie,
żeby program ładujący z ROM-u
w ogóle go nie rozpoznał.

<!-- S39 -->
I było to słychać.
Taśma ze Speedlockiem wczytywała się z klikaniem,
a wokół ekranu skakały paski.

<!-- S40 -->
Nie przeszkadzało to nikomu w kopiowaniu
taśmy z jednego magnetofonu na drugi.
Ale dało wydawcom
powód, żeby pisać własne programy ładujące.

<!-- S41 -->
Na Commodore 64
powód do zmiany był dużo większy.

<!-- S42 -->
Jego wbudowana procedura
nagrywała wszystko dwa razy,
jako kopię zapasową.
Gra o rozmiarze czterdziestu kilobajtów wczytywała się
około dwunastu i pół minuty.

<!-- S43 -->
A tutaj magnetofon
nie robił prawie nic mądrego.
Po prostu zamieniał dźwięk
w czyste impulsy: włączone, wyłączone.

<!-- S44 -->
Komputer sam mierzył czas każdego impulsu,
programowo.

<!-- S45 -->
Więc szybszy program ładujący
był po prostu innym programem.

<!-- S46 -->
W 1985 roku magazyn Compute!
przetestował jeden z nich, o nazwie TurboTape.

<!-- S47 -->
Kiedy już znalazł program na taśmie,
wczytywał dwanaście kilobajtów
w dwadzieścia osiem sekund.

<!-- S48 -->
Stacja dyskietek samego Commodore
potrzebowała trzydziestu czterech sekund.

<!-- S49 -->
Kaseta,
która wygrywa z dyskietką.

<!-- S50 -->
A ponieważ komputer
sam słuchał taśmy,
mógł w międzyczasie robić inne rzeczy.

<!-- S51 -->
Programy ładujące takie jak Freeload
dawały pierwszeństwo czytaniu taśmy.
Czas procesora, który został,
szedł na muzykę, płynne przewijanie,
a nawet małe gry.

<!-- S52 -->
Z Invade-a-Load od Mastertronic
można było grać w klona Space Invaders,
podczas gdy wczytywała się prawdziwa gra.

<!-- S53 -->
Komputery 8-bitowe Atari
to była zupełnie inna historia.

<!-- S54 -->
Tutaj słuchał magnetofon.
W środku miał dwa filtry,
po jednym na każdy ton,
i układ, który podawał komputerowi
gotowe jedynki i zera.

<!-- S55 -->
Standard to było sześćset bitów na sekundę,
a filtry ograniczały,
na ile dało się przyspieszyć.

<!-- S56 -->
Sprytne oprogramowanie potrafiło to podkręcić
trochę, najwyżej do około tysiąca dwustu.
Ale żeby było dużo szybciej,
trzeba było otworzyć magnetofon.

<!-- S57 -->
I w Czechosłowacji ludzie to robili.

<!-- S58 -->
Stacja dyskietek kosztowała tam
dwa do trzech razy
więcej niż sam komputer.
Więc większość tamtejszych właścicieli Atari została przy kasetach.

<!-- S59 -->
W 1987 roku praski student
z miejscowego klubu Atari
zaprojektował Turbo 2000.

<!-- S60 -->
Dodał jedną nową drogę dla sygnału.
Przewód w magnetofonie brał dźwięk
prosto z jego wzmacniacza,
jeszcze przed filtrami,
prowadził go przez jeden mały układ scalony
i dalej na linię do komputera.

<!-- S61 -->
Przełącznik, sterowany przez komputer,
wybierał między starą a nową drogą.

<!-- S62 -->
Teraz komputer sam mierzył czas trwania impulsów.
Około dwóch tysięcy trzystu bitów
na sekundę.
Prawie cztery razy szybciej.

<!-- S63 -->
Turbo nie było jednym uniwersalnym formatem.

<!-- S64 -->
Czasem zmieniało się program.
Czasem trzeba było przerobić sam sprzęt.

<!-- S65 -->
A szybkość nie była za darmo.

<!-- S66 -->
Compute! ostrzegał, że nagranie TurboTape
czasem nie chciało się wczytać
na innym magnetofonie,
z głowicą ustawioną odrobinę inaczej.

<!-- S67 -->
Standardowy zapis, jak pisał magazyn,
był dużo wolniejszy,
ale niezwykle niezawodny.

<!-- S68 -->
Nagrywanie wszystkiego dwa razy
to nie było lenistwo Commodore.
To była cena niezawodnego wczytywania.

<!-- S69 -->
Ale inny program ładujący
potrafił też zrobić coś nieoczekiwanego.
Potrafił odczytać taśmę,
której wbudowany nie chciał przyjąć.

<!-- S70 -->
Na Sharpie MZ-800,
komputerze, który trafił
do Czechosłowacji pod koniec lat 80.,
właściciele znali program Turbo Copy.

<!-- S71 -->
Gra nie chciała się wczytać
i zgłaszała błąd sumy kontrolnej.
Właściciele odkryli, że Turbo Copy
często i tak potrafił ją wczytać.

<!-- S72 -->
Potem zapisywało się ją z normalną prędkością
na świeżą kasetę,
a komputer
znowu wczytywał ją normalnie.
To było jak naprawa zepsutej gry.

<!-- S73 -->
Jak więc jeden program ładujący mógł odczytać
to, czego drugi nie potrafił?

<!-- S74 -->
ROM Sharpa nagrywał każdy blok dwa razy,
z prędkością około tysiąca dwustu bitów na sekundę.

<!-- S75 -->
I nigdy nie mierzył impulsu.
Gdy zaczynał się każdy impuls,
odczekiwał z góry ustaloną chwilę
i patrzył jeden raz.

<!-- S76 -->
Nadal wysoko?

<!-- S76b -->
To jedynka.

<!-- S76c -->
Już nisko?

<!-- S76d -->
To zero.

<!-- S77 -->
Stoper, nastawiony z góry.

<!-- S78 -->
Na starej taśmie albo innym magnetofonie
impulsy wracały trochę bardziej zaokrąglone.
I wtedy to jedno spojrzenie
mogło trafić na zły poziom.

<!-- S79 -->
Jeden zły bit psuje sumę kontrolną.
Jeśli obie kopie zawiodą,
wczytywanie się nie udaje.

<!-- S80 -->
Turbo Copy słuchał inaczej.
Mierzył czas każdego impulsu
za pomocą układu czasowego komputera.

<!-- S81 -->
A przed każdym blokiem
słuchał tonu pilota
i ustawiał swój próg
według impulsów, które naprawdę słyszał.

<!-- S82 -->
Jego stoper był nastawiony
na taśmę, którą akurat miał przed sobą.

<!-- S83 -->
I ta naprawa nie była kopią dźwięku.
Turbo Copy zachowywał bajty
i zapisywał zupełnie nowy sygnał,
z czystym, równym taktowaniem.

<!-- S84 -->
Dane wcale nie przepadły.
Zwykły sposób ich odczytu
po prostu nie był dość dobry.

<!-- S84b -->
Turbo Copy umiał też zapisać grę w turbo,
dwa albo trzy razy szybciej niż normalnie,
z własnym małym programem ładującym na początku.

<!-- S85 -->
I właśnie to wszystkie te sztuczki
mają ze sobą wspólnego.

<!-- S86 -->
Kaseta została ta sama.
Zmienił się sposób, w jaki ją czytano.

<!-- S87 -->
Dziś oczekujemy, że gry wczytają się od razu.
W latach 80. wczytywanie było częścią gry.
Słuchało się taśmy.
Patrzyło się na paski.
Czekało się.

<!-- S88 -->
A czasem inny program ładujący
sprawiał, że ta sama kaseta zachowywała się
jak zupełnie inna maszyna.

<!-- S89 -->
Komputer nie potrzebował szybszej taśmy.
Potrzebował lepszego sposobu słuchania.

<!-- S90 -->
Mam więc do ciebie pytanie.
Zdarzało ci się wtedy używać programów ładujących turbo?
Jak je wspominasz?
Czy częściej zawodziły?
Napisz w komentarzach.

<!-- S91 -->
I na koniec cała taśma turbo,
od początku do końca.
Najpierw część z normalną prędkością,
potem turbo.
Przy tak małym programie
turbo się nie opłaca.
Program ładujący zajmuje więcej czasu,
niż oszczędza.
Przy całej grze mogło to oszczędzić minuty.
