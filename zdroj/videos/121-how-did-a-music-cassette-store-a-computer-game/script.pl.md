<!-- S01 -->
Wciskasz play na magnetofonie.
A z głośnika wydobywa się to.

<!-- S02 -->
To nie jest muzyka.
I nie jest to też ścieżka dźwiękowa gry.

<!-- S03 -->
To jest gra.
Każdy pisk to kawałek programu,
a komputer go słucha.

<!-- S04 -->
Magnetofon nie ma o tym pojęcia.
Według niego gra piosenkę.

<!-- S05 -->
Jak więc zamienić piosenkę w grę?
I czemu jedna zła nuta
mogła zmarnować pięć minut czekania?

<!-- S06 -->
Oto cała sztuczka,
na jednej konkretnej maszynie:
ZX Spectrum,
brytyjskim komputerze domowym z 1982 roku.

<!-- S07 -->
Używa dwóch rodzajów impulsów.
Krótka para impulsów oznacza zero.

<!-- S08 -->
Jedynka to ta sama para,
tylko każdy impuls jest dwa razy dłuższy,
więc jej ton brzmi o oktawę niżej.

<!-- S09 -->
Wysyłaj około tysiąca czterystu bitów
na sekundę,
a dostaniesz dźwięk, który właśnie słyszałeś.

<!-- S09b -->
To znaczy też, że program pełen zer
wczytuje się szybciej niż program pełen jedynek.
Wysłanie każdej jedynki trwa dwa razy dłużej.

<!-- S10 -->
Jeśli dorastałeś w Ameryce,
możliwe, że nigdy go nie słyszałeś.

<!-- S11 -->
Co jest dziwne,
bo sam pomysł był amerykański.

<!-- S12 -->
W 1975 roku, na spotkaniu w Kansas City,
komputerowi hobbyści uzgodnili sposób
zapisywania danych jako dźwięku
na zwykłych kasetach magnetofonowych.

<!-- S12b -->
Jedynka to było osiem szybkich drgań
wysokiego tonu,
zero – cztery wolniejsze drgania niskiego.
Trzysta bitów na sekundę.

<!-- S13 -->
Pierwsze maszyny, takie jak Apple II
i TRS-80,
zapisywały swoje programy
na zwykłych magnetofonach.

<!-- S14 -->
Ale w USA użytkownicy komputerów domowych
szybko przeszli na inne rozwiązania.

<!-- S15 -->
W 1983 roku pewien magazyn opisał ankietę:
dziewięciu na dziesięciu nowych właścicieli Commodore 64
kupowało stację dysków
razem z komputerem.

<!-- S16 -->
W Wielkiej Brytanii historia potoczyła się odwrotnie.

<!-- S17 -->
Spectrum kosztowało sto
dwadzieścia pięć funtów
i nie miało żadnej pamięci masowej.
Używałeś magnetofonu,
który już miałeś w domu.

<!-- S18 -->
Dla milionów dzieciaków w całej Europie
ten dźwięk był więc odgłosem
gry, która zaraz się zacznie.

<!-- S18b -->
Po odpowiednio wielu wczytaniach
dało się nawet rozpoznać, co to za gra,
po samym piszczeniu.

<!-- S19 -->
Prześledźmy więc jedną grę
od taśmy aż do komputera.

<!-- S20 -->
Wpisujesz LOAD, wciskasz enter
i wciskasz play.

<!-- S21 -->
Najpierw słychać równe buczenie,
osiemset drgań na sekundę,
przez jakieś pięć sekund.

<!-- S22 -->
Nie niesie żadnych danych.
Jest po to, żeby komputer
znalazł sygnał
i złapał jego rytm.

<!-- S23 -->
Potem dwa szybkie impulsy – synchronizacja.
Oznaczają: od tej chwili to są dane.

<!-- S24 -->
Najpierw przychodzi
krótki nagłówek.
Dziewiętnaście bajtów:
nazwa do dziesięciu liter,
rodzaj pliku
i to, jak będzie długi.

<!-- S25 -->
Potem drugie, krótsze buczenie,
tym razem przez dwie sekundy,
a potem sama gra.

<!-- S26 -->
Każdy bajt to osiem takich nut,
jedna po drugiej,
bez żadnych przerw między bajtami.

<!-- S27 -->
A komputer nie słyszy nut.
Mierzy czas między jednym zboczem
sygnału a następnym.

<!-- S28 -->
Krótka para to zero.
Długa para to jedynka.

<!-- S28a -->
I to jest cały dekoder.

<!-- S28b -->
A dźwięk z początku tego filmu
to nie efekt dźwiękowy.
Wygenerowaliśmy go dokładnie według tych zasad
i jest w nim prawdziwy program na Spectrum.

<!-- S28c -->
Puścimy go w całości na samym końcu.
Nagraj go, a Spectrum go wczyta.

<!-- S29 -->
Większość gier najpierw pokazywała obrazek,
który wczytywał się w dziwnej kolejności.

<!-- S30 -->
Pojawiały się cienkie paski, co osiem linii,
potem się wypełniały, linia po linii,
po jednej trzeciej ekranu naraz.
A kolory przychodziły na samym końcu,
spływając z góry na wszystko.

<!-- S31 -->
Sam obrazek
wczytywał się około czterdziestu sekund.
Cała gra – jakieś pięć minut.

<!-- S32 -->
A na końcu każdego bloku
przychodzi jeszcze jeden bajt.

<!-- S33 -->
Podczas zapisu Spectrum przepuszcza
każdy bajt bloku
przez prostą regułę o nazwie XOR
i zapisuje wynik jako dodatkowy bajt.

<!-- S34 -->
Podczas wczytywania powtarza obliczenie.
Jeśli wyniki się zgadzają,
blok dotarł bez uszkodzeń.

<!-- S35 -->
Jeśli nie, Spectrum mówi to.

<!-- S36 -->
Pięć minut czekania
i jeden bajt przesądza,
że wszystko poszło na marne.
Przewiń i zacznij od nowa.

<!-- S37 -->
Co dziwne, uszkodzony nagłówek
nie wywołuje żadnego błędu.
Spectrum po prostu go ignoruje
i dalej nasłuchuje następnego.

<!-- S38 -->
Inne komputery postawiły na co innego.

<!-- S39 -->
Commodore 64 zapisywał
każdy blok dwa razy,
więc uszkodzone miejsce w jednej kopii
dało się uratować z drugiej.

<!-- S40 -->
Bezpieczniej, ale wolno.
Z wbudowaną procedurą Commodore'a
program o rozmiarze czterdziestu kilobajtów
wczytywał się około dwunastu i pół minuty.

<!-- S41 -->
Wydawcy gier pisali więc
własne, szybsze programy ładujące,
niektóre nawet około dziesięciu razy szybsze.

<!-- S42 -->
A do tego był jeszcze magnetofon.

<!-- S43 -->
Za cicho –
i zbocza toną w szumie.
Za głośno –
i zlewają się ze sobą.

<!-- S44 -->
Taśma, która biegnie odrobinę za szybko albo za wolno,
rozciąga każdy impuls,
a komputer przecież mierzy czas.

<!-- S45 -->
Najgorszy ze wszystkiego był azymut,
czyli kąt ustawienia głowicy.
Taśma nagrana na jednym magnetofonie
mogła nie pasować do innego.

<!-- S46 -->
Ludzie wsuwali więc maleńki śrubokręt
do otworu obok głowicy
i obracali nim po troszeczku,
nasłuchując.

<!-- S47 -->
Wyglądało to na zabobon.
A było strojeniem sygnału.

<!-- S48 -->
Ale zwróć uwagę, czego magnetofon
nigdy nie musiał robić.

<!-- S49 -->
Nigdy nie zrozumiał ani jednego bitu.
Nagrywał dźwięk
i go odtwarzał.

<!-- S50 -->
A to znaczy, że program
właściwie nie potrzebował kasety.
Wszystko, co mogło przenieść dźwięk,
mogło przenieść oprogramowanie.

<!-- S50b -->
Znaczyło to też, że skopiowanie gry
było równie proste jak skopiowanie albumu.
Dwa magnetofony i kabel.

<!-- S51 -->
Atari wykorzystywało obie ścieżki stereo.
Na jednej program,
na drugiej głos,
który mówił do ciebie z telewizora,
kiedy gra się wczytywała.

<!-- S52 -->
W Jugosławii audycja Radia Belgrad
nadawała w eterze programy komputerowe.

<!-- S53 -->
Słuchacze nagrywali je na taśmę,
w sumie około stu pięćdziesięciu programów
między 1983 a 1986 rokiem.

<!-- S54 -->
W Czechosłowacji była to telewizja.
Program leciał jako dźwięk
pod napisami końcowymi.

<!-- S55 -->
A w 1983 roku piosenkarz Pete Shelley
ukrył program na Spectrum
na końcu płyty winylowej.

<!-- S56 -->
Skopiuj go na taśmę, wczytaj,
a na ekranie pojawią się teksty
w takt piosenek.

<!-- S57 -->
Był jednak haczyk.

<!-- S58 -->
Radio mogło dostarczyć dźwięk
do każdego komputera w kraju.
Zrozumieć go mógł tylko właściwy.

<!-- S59 -->
Puść grę na Spectrum Commodore'owi,
a Commodore usłyszy szum.
Bity coś znaczą tylko
dla maszyny, która zna format.

<!-- S60 -->
Holenderskie radio próbowało więc to naprawić.
W 1982 roku stworzyło BASICODE:
jeden format dźwiękowy
i mały program tłumaczący
dla każdego rodzaju komputera.

<!-- S61 -->
I ten problem nigdy nie zniknął.
Plik jest coś wart tylko wtedy,
gdy coś wciąż potrafi go odczytać.

<!-- S62 -->
Kasety oczywiście przegrały.
Dyskietki były szybsze,
potem dyski twarde, potem pamięć flash.

<!-- S63 -->
Tyle że taśma tak naprawdę nigdy nie odeszła.
Centra danych wciąż trzymają
swoje archiwa na taśmie magnetycznej.

<!-- S64 -->
Jedna nowoczesna kaseta LTO-9
mieści osiemnaście terabajtów.

<!-- S65 -->
W przeliczeniu na prędkość Spectrum
ta pojemność zapełniłaby mniej więcej
dwadzieścia dziewięć milionów kaset,
a wczytywanie trwałoby ponad trzy tysiące
lat.

<!-- S66 -->
Ale pomysł wciąż jest ten sam.
Wzory na przesuwającym się pasku taśmy,
zamieniane z powrotem w liczby,
kiedy ich potrzebujesz.

<!-- S67 -->
Więc kiedy następnym razem usłyszysz ten pisk,
pamiętaj, czym on jest.
Nie szum.
Program podróżujący jako dźwięk.

<!-- S68 -->
A gdzieś w 1985 roku
dzieciak siedzi przed telewizorem
i czeka, aż to się skończy.
Bo kiedy się skończy,
zacznie się gra.

<!-- S69 -->
Mam więc dla ciebie pytanie.
Jeśli kiedyś wczytywałeś grę z kasety,
co z tego pamiętasz najbardziej?
Napisz w komentarzach.

<!-- S70 -->
I tak jak obiecaliśmy, oto ten program.
Zupełnie jak czechosłowacka telewizja,
puściliśmy go pod napisami końcowymi.
