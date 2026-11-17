<!-- S01 -->
To jest kod QR.
Zawiera jedną krótką linijkę tekstu.

<!-- S02 -->
Telefon odczytuje go od razu.

<!-- S03 -->
A teraz wyrwijmy z niego kawałek.

<!-- S04 -->
I zeskanujmy go jeszcze raz.
Ten sam tekst.
Co do litery.

<!-- S05 -->
Części tego kodu nie ma.
Nie chodzi o to, że jest nieczytelna.
Nie ma jej.

<!-- S06 -->
Jak więc telefon może odczytać coś,
czego już tam nie ma?

<!-- S07 -->
Oto ten sam problem w mniejszej skali.
Ktoś wysyła wam osiem bitów.
Po drodze trzy z nich giną.

<!-- S08 -->
Każdy brakujący bit to zero albo jedynka,
więc luki można wypełnić na osiem sposobów.
A nic w tym, co dotarło,
nie mówi wam, który jest właściwy.

<!-- S09 -->
A jednak telefon właśnie to zrobił.
Nie zgadywał.
Odpowiedź została wysłana,
zanim cokolwiek zginęło.

<!-- S10 -->
Sztuka polega na tym, żeby wysłać więcej
niż samą wiadomość.

<!-- S11 -->
Najprostszy sposób
to powiedzieć wszystko trzy razy.
Zero wysyła się jako trzy zera,
jedynkę jako trzy jedynki.

<!-- S12 -->
Szum odwraca jedną z nich
i dostajecie: jeden, zero, jeden.
Dwa głosy przeciw jednemu.
To niemal na pewno była jedynka.

<!-- S13 -->
Jeśli szum odwraca jeden bit na dziesięć,
losowo i niezależnie,
głosowanie trzech bitów daje zły wynik
rzadziej niż trzy razy na sto.

<!-- S14 -->
Ale potroiliście
wszystko, co wysyłacie.
Żeby zbliżyć się do ideału,
powtarzalibyście pięć razy, potem dziewięć,
potem sto...
a wiadomość wlokłaby się w żółwim tempie.

<!-- S15 -->
Przez długi czas
wydawało się, że taka jest cena.
Mniej błędów, wolniejsze wiadomości.
Zapamiętajcie to.

<!-- S16 -->
Pod koniec lat 40.
Richard Hamming z Bell Labs
miał własny problem.

<!-- S17 -->
Do komputera przekaźnikowego miał dostęp
głównie w weekendy,
kiedy nie było nikogo, kto by go pilnował.

<!-- S18 -->
Maszyna potrafiła wykryć,
że popełniła błąd.
Próbowała wykonać krok jeszcze raz,
trzy razy...
a potem porzucała jego zadanie.
Dwa weekendy z rzędu
jego praca szła na marne.

<!-- S20 -->
Jego pytanie, jego własnymi słowami:
„Skoro maszyna potrafi wykryć,
że jest błąd,
to czemu nie potrafi wykryć, gdzie on jest?”
Prawdziwe słowa, jak przyznał,
były pewnie nieco mocniejsze.

<!-- S22 -->
Jego metoda bierze cztery bity wiadomości
i dodaje trzy bity kontrolne.
Razem siedem bitów.

<!-- S23 -->
Każdy bit kontrolny pilnuje
innej grupy pozycji
i dba o to, żeby ta grupa
miała parzystą liczbę jedynek.

<!-- S24 -->
Grupy nakładają się według przemyślanego wzoru.
Każda pozycja należy
do własnej kombinacji grup.

<!-- S25 -->
Teraz odwróćmy jeden bit.
Powiedzmy ten na pozycji szóstej.

<!-- S26 -->
Odbiorca jeszcze raz wykonuje trzy sprawdzenia.
Pierwsze nie wykrywa błędu.
Drugie wykrywa błąd.
Trzecie też.

<!-- S27 -->
Wykryty błąd zapiszcie jako jedynkę,
brak błędu jako zero
i odczytajcie je od ostatniego do pierwszego.
Jeden, jeden, zero.
W systemie dwójkowym to sześć.

<!-- S28 -->
Sprawdzenia nie mówią tylko,
że coś poszło nie tak.
Wskazują dokładnie ten bit.

<!-- S29 -->
Odwróćcie go z powrotem
i wiadomość znów jest cała.
Nikt nie musiał niczego wysyłać dwa razy.

<!-- S30 -->
Więc to jest odpowiedź.
Odbiorca nie odtwarza
utraconej informacji z niczego.
Nadawca ją tam zapakował
z wyprzedzeniem.

<!-- S32 -->
Nie każde sprawdzenie to potrafi.
Suma kontrolna, taka jak w naszym filmie
o Btrfs,
powie wam, że blok jest uszkodzony,
ale nie, jakie były oryginalne dane.

<!-- S33 -->
Jest też drugi rodzaj uszkodzenia.
Czasem bit nie jest błędny.
Po prostu go brakuje
i dokładnie wiecie, gdzie jest luka.

<!-- S34 -->
To się nazywa wymazanie,
a z wymazaniami łatwiej sobie poradzić.

<!-- S35 -->
Wyślijcie cztery liczby,
4, 7, 2 i 9,
i do tego piątą:
ich sumę, 22.

<!-- S36 -->
Jeśli którejkolwiek z nich zabraknie,
pozostałe powiedzą wam, jaka była.
4, 7, coś, 9,
22.
To musi być dwójka.

<!-- S37 -->
Serwery chronią swoje dyski
podobnym rodzajem kontroli,
rozłożonym na wszystkie dyski.
Kiedy jeden dysk padnie,
jego zawartość wylicza się z pozostałych.

<!-- S38 -->
Ile więc trzeba dodać?
Powtarzanie mówi:
żeby zbić błędy do zera,
trzeba zwolnić do zera.

<!-- S39 -->
Dwa lata przed tym, jak artykuł Hamminga
się ukazał,
jego kolega Claude Shannon
opublikował dziwniejszą odpowiedź.

<!-- S40 -->
Każdy kanał,
łącze radiowe, kabel, płyta,
ma granicę.
Maksymalną prędkość przesyłu informacji.

<!-- S41 -->
Poniżej tej granicy
błędy mogą być tak rzadkie, jak chcecie,
bez zwalniania.
Nie dzięki większej liczbie powtórzeń.
Dzięki sprytniejszemu kodowaniu.

<!-- S42 -->
Powyżej niej
nie pomoże żaden kod na świecie.

<!-- S43 -->
Był jednak haczyk.
Shannon udowodnił, że takie kody istnieją.
Nie pokazał, jak zbudować taki,
którego ktokolwiek mógłby użyć.

<!-- S44 -->
Z jego dowodu wynikało, że losowo wybrany kod
byłby niemal na pewno dobry.
Ale oczywisty sposób dekodowania
oznacza porównanie tego, co dotarło,
z każdą możliwą wiadomością...
a dla bloku o długości 1 000 bitów
jest ich więcej
niż atomów we wszechświecie.

<!-- S46 -->
Artykuł Shannona nie był więc rozwiązaniem.
Był obietnicą.
A inżynierowie spędzili kolejne
45 lat, próbując jej dotrzymać.

<!-- S47 -->
Kod Hamminga był pierwszym krokiem.
Naprawia jeden błędny bit na siedem.

<!-- S48 -->
Ale prawdziwe uszkodzenia przychodzą seriami.
Rysa albo trzask zakłóceń
wybija setki bitów pod rząd.

<!-- S49 -->
W 1960 roku Irving Reed i Gustave Solomon
z MIT Lincoln Laboratory
opublikowali artykuł liczący pięć stron.

<!-- S50 -->
Ich kody działają na całych bajtach,
a nie na pojedynczych bitach.
Jeśli seria błędów zniszczy wszystkie osiem bitów
jednego bajtu,
to wciąż tylko jeden błędny bajt.

<!-- S51 -->
Jedna popularna wersja dodaje
32 bajty kontrolne
do 223
bajtów danych.

<!-- S52 -->
Potrafi naprawić dowolne 16 bajtów,
które dotrą z błędami...
albo odtworzyć 32,
które w ogóle nie dotrą.

<!-- S53 -->
Dlatego płyta CD gra mimo rysy.
Jej dwa kody Reeda-Solomona
potrafią w pełni naprawić lukę
długości około 4 000 bitów,
czyli 2,5 milimetra ścieżki.

<!-- S54 -->
I dlatego podarty kod QR
wciąż działał.
Przy najsilniejszym ustawieniu
kod QR potrafi odtworzyć
do około 30% swoich bajtów
i wciąż oddać każdą literę.

<!-- S56 -->
Voyager 2 opuścił Ziemię w 1977 roku
już z koderem Reeda-Solomona na pokładzie.

<!-- S57 -->
Ale przy Jowiszu i Saturnie
chronił wszystko oprócz zdjęć
starszym kodem Marcela Golaya,
który wysyłał jeden dodatkowy bit
na każdy bit danych.

<!-- S58 -->
Przy Uranie i Neptunie,
gdy sygnał słabł,
inżynierowie włączyli kod Reeda-Solomona,
nałożony na drugi kod,
przez który i tak przechodził każdy bit.

<!-- S59 -->
Z samym tym drugim kodem
około pięciu bitów na tysiąc
wciąż było błędnych.
Po dodaniu kodu Reeda-Solomona
około jednego na milion.

<!-- S60 -->
Szum też przychodzi seriami,
więc Voyager mieszał ze sobą
bajty czterech bloków,
zanim je wysłał.

<!-- S61 -->
Seria, która zniszczyłaby jeden blok,
teraz zabiera po kilka bajtów z każdego...
na tyle mało, że każdy blok
może naprawić się sam.

<!-- S62 -->
Resztę historii o tym, jak zdjęcia Neptuna
dotarły na Ziemię,
znajdziecie w naszym filmie o Voyagerze.

<!-- S63 -->
Ale nawet to
wciąż nie sięgało granicy Shannona...
a kod, który mógł podejść dużo bliżej,
już istniał.

<!-- S65 -->
W 1960 roku w swojej pracy doktorskiej na MIT
Robert Gallager opisał kody
złożone z wielu prostych sprawdzeń,
z których każde patrzy tylko na kilka bitów.

<!-- S66 -->
Dekodowanie polegało na tym, że sprawdzenia
przekazują sobie domysły tam i z powrotem,
runda za rundą...
a to było zdecydowanie za dużo
dla komputerów lat 60.
Pomysł odłożono więc na półkę
i na 30 lat w dużej mierze zapomniano.

<!-- S68 -->
W 1993 roku
zespół kierowany przez dwóch francuskich inżynierów,
Claude'a Berrou i Alaina Glavieux,
zaprezentował turbokody
na konferencji w Genewie.

<!-- S69 -->
Ich wyniki były tak bliskie
granicy Shannona,
że wielu ekspertów założyło,
że się pomylili.
Pewnie gdzieś w obliczeniach
pomnożyli lub podzielili przez dwa.

<!-- S70 -->
W ciągu roku
inne laboratoria to potwierdziły.

<!-- S71 -->
Turbokody też działały
dzięki przekazywaniu domysłów tam i z powrotem
i dzięki temu ludzie wrócili do Gallagera.

<!-- S72 -->
W latach 1995 i 1996
David MacKay i Radford Neal
odkryli jego kody na nowo
i pokazali, że mogą one podejść
równie blisko.

<!-- S73 -->
W 2001 roku
udoskonalona wersja kodów Gallagera
zbliżyła się na 0,04 decybela
do granicy Shannona.

<!-- S74 -->
To mniej niż 1%
więcej mocy sygnału
niż teoretyczne minimum.
Obietnica z 1948 roku została dotrzymana.

<!-- S75 -->
Dziś kody Gallagera przenoszą
dużą część danych w telefonach 5G,
w nowoczesnym Wi-Fi
i w telewizji satelitarnej.

<!-- S77 -->
A teraz wróćmy do naszych ośmiu bitów.
Trzy zginęły,
a luki można wypełnić
na osiem sposobów.

<!-- S78 -->
Ale tych osiem bitów
nigdy nie było samą wiadomością.
Niosły cztery bity danych,
trzy sprawdzenia Hamminga
i jeszcze jedno sprawdzenie obejmujące wszystkie osiem.

<!-- S79 -->
Ze wszystkich 256
możliwych układów ośmiu bitów
tylko 16 spełnia te warunki.

<!-- S80 -->
Sprawdźcie ośmiu kandydatów.
Jeden po drugim odpadają.
Zostaje tylko jeden.

<!-- S81 -->
Brakujące bity nigdy tak naprawdę nie zniknęły.
Ich informacja wciąż tam była,
w bitach, które przetrwały.

<!-- S82 -->
A teraz pytanie do was.
Zauważyliście kiedyś, jak korekcja błędów
działa w czymś, czego używacie na co dzień?
Napiszcie w komentarzach.
