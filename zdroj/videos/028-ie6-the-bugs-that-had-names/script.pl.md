# Internet Explorer 6 — Błędy, które miały imiona

<!-- S01 -->
To jest część druga.

Jeśli nie widziałeś pierwszej,
link jest pod filmem.

Krótkie streszczenie i tak dostaniesz.

<!-- S02 -->
W 2001 roku
Microsoft wydał
Internet Explorer 6,
i przyszedł on razem z Windows XP.

W ciągu kilku lat
miał ponad dziewięćdziesiąt procent
rynku przeglądarek.

<!-- S03 -->
Microsoft to wykorzystał,
żeby zmienić przeglądarkę
w platformę aplikacyjną.

To był prawdziwy pomysł.

Zapłacili za niego tylko
akurat twórcy stron.

<!-- S04 -->
To była część pierwsza.

Ale coś pominąłem.

Pominąłem tę część,
w której błędy miały imiona.

<!-- S05 -->
Błąd przeglądarki to normalnie
numer w systemie zgłoszeń.

Issue 4172.

Nikt go nie pamięta.

Nikt o nim nie mówi przy obiedzie.

<!-- S06 -->
W Internet Explorerze 6
błędy miały nazwy własne.

I okazuje się, że to
najbardziej wymowna rzecz
w całej tamtej epoce.

<!-- S07 -->
Zacznijmy od łagodnego.

Puszczasz obrazek w lewo
i stawiasz obok akapit.

Tekst powinien stać
tuż przy obrazku.

Zamiast tego stoi
trzy piksele dalej.

<!-- S08 -->
Nie cztery.

<!-- S08b -->
Nie dwa.

<!-- S08c -->
Trzy.

<!-- S08d -->
Za każdym razem.

Miało to imię.

The Three Pixel Jog.

<!-- S09 -->
Teraz puść ten obrazek w lewo
i daj mu lewy margines
dziesięciu pikseli.

Internet Explorer 6
daje mu dwadzieścia.

Podwaja margines,
ale tylko po tej stronie,
w którą go puściłeś.

<!-- S10 -->
The Double Margin Bug.

A przyjętą poprawką
było zadeklarowanie
elementu pływającego jako liniowego.

<!-- S11 -->
Co jest bez sensu.

Element pływający to blok.

Nazwanie go liniowym
nie znaczy zupełnie nic.

Działało, więc ludzie to pisali.

<!-- S12 -->
Następny jest lepszy.

Wczytujesz stronę,
a części treści
po prostu nie ma.

Przewijasz w dół.

Przewijasz z powrotem w górę.

I się pojawia.

<!-- S13 -->
Nic się nie wczytało.

Nic się nie zmieniło.

Po prostu było nieśmiałe.

I miało właściwe imię.

The Peekaboo Bug.

<!-- S14 -->
Lekarstwem było powiedzieć
brakującemu elementowi,
że jego pozycja jest względna.

Nikt nie potrafił do końca wyjaśnić,
dlaczego to go przywracało.

<!-- S15 -->
Potem jest ten,
w którym najeżdżasz na odnośnik,
a tło
ramki pod nim
zostaje ucięte w prostej linii.

The Guillotine Bug.

<!-- S16 -->
Był błąd, w którym tekst
odpełzał z miejsca, gdzie go postawiłeś.

Magic Creeping Text.

Był taki, w którym obramowania
wychodziły w złym miejscu,
w złym kolorze,
albo wcale.

Border Chaos.

<!-- S17 -->
Mój ulubiony jest cichszy.

Układasz rząd bloków,
a litery z ostatniego
pojawiają się znowu pod nim.

Nie zawsze.

Nie w sposób przewidywalny.

The Duplicate Character Bug.

<!-- S18 -->
A o tym, czy trafiło
akurat na ciebie,
i ile liter
wyszło podwojonych,
decydowała liczba komentarzy HTML,
które zostawiłeś w kodzie.

Komentarzy.

Jedynej rzeczy w pliku,
którą przeglądarka
ma wyrzucić.

<!-- S19 -->
Jest jeszcze jeden
i jest inny,
bo tego ludzie używali
celowo.

Jeśli ustawisz wysokość,
a treść jest wyższa,
ramka powinna się przelać.

Internet Explorer 6
zamiast tego ją powiększał.

<!-- S20 -->
Co jest błędem.

I jest zarazem dokładnie tym,
co robi wysokość minimalna.

A Internet Explorer 6
wysokości minimalnej nie miał.

Więc programiści przestali
ten błąd zgłaszać
i zaczęli na nim polegać.

<!-- S21 -->
Zatrzymaj się i spójrz na tę listę.

The Three Pixel Jog.

The Double Margin Bug.

Peekaboo.

The Guillotine.

Błędowi, którego spotykasz raz,
nie nadaje się imienia.

<!-- S22 -->
Te miały imiona,
bo spotykał je każdy.

A teraz to,
co czyni sprawę gorszą.

Większość z nich miała
pod spodem tę samą przyczynę.

<!-- S23 -->
Wewnątrz Internet Explorera 6
każdy element albo miał,
albo nie miał
czegoś, co nazywało się layout.

<!-- S24 -->
Decydowało to, czy element
sam ustalał swój rozmiar i pozycję,
czy zostawiał to rodzicowi.

A ustawić tego się nie dało.

<!-- S25 -->
Nie istniała żadna właściwość
o nazwie layout
ani sposób, żeby o nią poprosić.

Nie było jej w żadnej specyfikacji.

To była wewnętrzna flaga
silnika renderującego.

<!-- S26 -->
Ale mogłeś ją przestawić
przez przypadek.

Ustawienie szerokości to robiło.

Ustawienie wysokości to robiło.

Puszczenie elementu to robiło.

Więc połowa poprawek w tym filmie
to ludzie przestawiający przełącznik,
którego nie widzieli.

<!-- S27 -->
Dlatego zaczęto szukać
najtańszego sposobu,
żeby przestawić go celowo.

Jednym było ustawienie wysokości
na jeden procent.

<!-- S28 -->
Wszystkie inne przeglądarki
trzeba było od tego trzymać z daleka,
więc trafiło to do sztuczki,
do której dojdziemy za chwilę.

<!-- S29 -->
A w Internet Explorerze 6
nie szkodziło to wcale,
bo wysokość, w której się nie mieści,
i tak jest wysokością, którą przerasta.

Błąd sprzed dwóch minut
jest tym, co czyni poprawkę bezpieczną.

<!-- S30 -->
Miało to imię.

The Holly Hack.

<!-- S31 -->
Drugim sposobem
była właściwość Microsoftu
o nazwie zoom, ustawiona na jeden.

Zoom jeden znaczy
nie powiększaj.

<!-- S32 -->
Nie zmieniało to nic widocznego.

O to właśnie chodziło.

Siedziało w arkuszach stylów
wyłącznie po to, by ustawić
niewidzialną flagę,
po której błędy znikały.

<!-- S33 -->
Co prowadzi nas do sztuczek,
a przy sztuczkach
robi się dziwnie.

Żeby naprawić jedną przeglądarkę,
musisz najpierw umieć mówić
tylko do niej.

<!-- S34 -->
A Internet Explorer 6
zachowywał się tak, jakby był
jeszcze jeden element
nad elementem html.

Żadna inna przeglądarka tak nie robiła.

Nie było to udokumentowane.

Po prostu tak się zachowywał.

<!-- S35 -->
Więc pisałeś regułę,
która pasowała do widma,
i tylko ta przeglądarka
mogła ją zobaczyć.

Gwiazdka, spacja, html.

<!-- S36 -->
Każda inna przeglądarka na nią patrzyła,
nie znajdowała nic pasującego
i szła dalej.

To jest star hack
i przez lata siedział
w niemal każdym arkuszu stylów
w sieci.

<!-- S37 -->
Był też
underscore hack.

Stawiasz podkreślnik
przed nazwą właściwości.

<!-- S38 -->
Przeglądarka zgodna ze standardami
wyrzuca tę linię
jako nieprawidłową.

Internet Explorer 6
ignoruje podkreślnik
i ją stosuje.

<!-- S39 -->
Więc celowo psułeś
własny arkusz stylów,
a to zepsucie
było instrukcją.

<!-- S40 -->
A potem jest ten,
który Microsoft zbudował celowo.

Mogłeś napisać komentarz,
którego słuchał tylko Internet Explorer.

<!-- S41 -->
Dla każdej innej przeglądarki
był to zwykły komentarz,
ignorowany tak, jak ignoruje się komentarze.

Dla Internet Explorera 6
były to drzwi
do drugiej wersji
strony.

<!-- S42 -->
Co znaczy, że producent
spojrzał na sytuację,
zgodził się, że ta przeglądarka
potrzebuje własnego arkusza stylów,
i dostarczył funkcję,
która ma to ułatwić.

<!-- S43 -->
Część tych szkód
nie potrzebowała żadnego błędu.

Internet Explorer 6
miał dwa tryby.

W nowoczesnym
trzymał się standardu.

<!-- S44 -->
W starym
szerokość ramki
obejmowała jej wypełnienie
i jej obramowanie,
co jest zupełnie
inną liczbą.

<!-- S45 -->
To, który tryb dostałeś,
zależało od pierwszej linii
dokumentu.

A ta wersja HTML,
do której wszyscy przechodzili,
kazała ci umieścić
tam na górze deklarację XML.

<!-- S46 -->
Ta linia spychała
Internet Explorera 6
do starego trybu.

Psuło go to,
że trzymałeś się nowszego standardu.

<!-- S47 -->
Potem jest przezroczystość.

Internet Explorer 6 nie umiał
pokazać PNG z miękkimi krawędziami.

Tam, gdzie obrazek miał się rozmyć,
kładł szarość.

<!-- S48 -->
Odpowiedzią Microsoftu był filtr
o nazwie jak numer seryjny.

Działał.

<!-- S49 -->
Ale malował poza
normalnym procesem
renderowania przeglądarki,
więc odnośniki, które kładłeś na nim,
często przestawały działać.

Naprawiałeś obrazek
i psułeś odnośnik.

<!-- S50 -->
A rozmycie czegokolwiek innego
to był drugi filtr,
z własną składnią,
siedzący w arkuszu stylów
tuż obok zwykłej właściwości,
którą rozumiała każda inna przeglądarka.

<!-- S51 -->
Część tego jest starsza
niż same błędy.

Zanim to wszystko nastało,
układy budowano
z zagnieżdżonych tabel.

<!-- S52 -->
A żeby utrzymać otwartą przerwę,
używałeś przezroczystego obrazka
o boku jednego piksela,
rozciągniętego do rozmiaru,
jakiego ta przerwa potrzebowała.

To też miało imię.

The spacer gif.

<!-- S53 -->
Najechanie myszą to kolejna rzecz.

W Internet Explorerze 6
najechanie działało na odnośnikach.

Tylko na odnośnikach.

<!-- S54 -->
Więc menu, które się otwierało,
gdy przesunąłeś mysz
nad cokolwiek innego,
potrzebowało małego programu
podpiętego do arkusza stylów.

<!-- S55 -->
Nie skryptu na stronie.

Osobnego pliku,
wskazanego z CSS,
niosącego kod, którego zadaniem
było nauczyć przeglądarkę
jednego selektora.

Ten plik ludzie podawali sobie
przez lata.

<!-- S56 -->
Część pierwsza wspominała,
że dało się wstawić JavaScript
do arkusza stylów.

Czego nie wspomniała,
to jak często ten JavaScript się wykonywał.

<!-- S57 -->
Przy każdym ruchu myszy.

Przy każdym klawiszu.

Przy każdym przewinięciu.

Raz za razem,
żeby wyliczyć jedną szerokość.

<!-- S58 -->
A przeglądarka miała sufity,
których nie miał nikt inny.

Arkusz stylów przestawał obowiązywać
gdzieś powyżej
czterech tysięcy reguł.

Wszystko po
trzydziestym pierwszym arkuszu stylów
na stronie było ignorowane.

<!-- S59 -->
Co brzmi jak liczba,
której nigdy nie osiągniesz,
dopóki twoja witryna nie jest tak duża,
że ktoś musi napisać
krok kompilacji, którego jedynym zadaniem
jest sklejenie arkuszy stylów,
zanim przeglądarka je zobaczy.

<!-- S60 -->
A część tego nie była
wcale kosmetyczna.

Internet Explorer 6
liczył swoje obiekty strony
i swoje obiekty skryptu
na dwa różne sposoby,
a żadna ze stron
nie widziała całej pętli.

<!-- S61 -->
Więc jeśli skrypt wskazywał
na część strony,
a ta część strony
wskazywała z powrotem na skrypt,
żadne z nich nigdy nie zostało zwolnione.

Zostaw to okno otwarte wystarczająco długo,
a przeglądarka zjadała maszynę.

<!-- S62 -->
Ale najlepszy
w ogóle nie jest błędem układu.

Piszesz znacznik input.

Dajesz mu typ.

I zapominasz znaku równości.

<!-- S63 -->
To jest wadliwy atrybut.

Każdy parser, jaki kiedykolwiek napisano,
ma na to odpowiedź.

Zignoruj go.

Zgadnij, o co chodziło.

Jedź dalej.

<!-- S64 -->
Internet Explorer się wysypywał.

W środku chciał wiedzieć,
czy pole jest ukryte,
więc porównywał to, co wpisałeś,
ze słowem hidden.

A ty nie wpisałeś nic.

<!-- S65 -->
Więc poszedł pobrać
to, czego nie wpisałeś,
spod adresu zero.

Co byłoby
zwykłą awarią przeglądarki,
tyle że kod, który to robił,
nie był w przeglądarce.

<!-- S66 -->
Był we współdzielonej bibliotece systemowej.

Więc te trzy słowa
kładły też klienta poczty
i podgląd
w menedżerze plików.

<!-- S67 -->
Okno z listą plików
na twojej własnej maszynie,
zamknięte przez stronę internetową.

To teza części pierwszej,
która przychodzi jako raport o awarii.

Przeglądarka nie była programem
działającym na systemie.

Była częścią systemu.

<!-- S68 -->
I nie mogłeś po prostu
przetestować poprawki gdzie indziej.

Internet Explorer był przyspawany
do systemu operacyjnego,
więc jeden komputer
uruchamiał dokładnie jedną wersję.

<!-- S69 -->
Dlatego do pracy przy front-endzie
w 2006 roku
należała półka
zapasowych maszyn.

<!-- S70 -->
A później folder
maszyn wirtualnych,
z których każda niosła cały
system operacyjny
po to, żeby dało się w niej
otworzyć jedną stronę.

<!-- S71 -->
A potem ktoś zrobił
rzecz oczywistą.

Skoro możesz nauczyć przeglądarkę
jednej brakującej rzeczy,
możesz nauczyć jej wszystkich.

<!-- S72 -->
Programista Dean Edwards
napisał bibliotekę,
której jedynym celem
było sprawić, żeby Internet Explorer 6
zachowywał się jak późniejsza
wersja samego siebie.

Ludzie to wdrażali.

Na produkcji.

<!-- S73 -->
I tu przestaje to być
zabawne.

Przez większość dekady
poważna część
światowej pracy przy front-endzie
szła w błędy jednej przeglądarki.

Nie w funkcje.

Nie w produkty.

W kompensację.

<!-- S74 -->
A trwało to z powodu tego,
o czym była część pierwsza.

Firmy zbudowały na niej
prawdziwe aplikacje,
takie, które działały tylko tam,
i te aplikacje
musiały w poniedziałek nadal działać.

<!-- S75 -->
Więc przeglądarka, której wszyscy
chcieli się pozbyć,
była tą, której nikt
nie miał prawa usunąć.

<!-- S76 -->
W 2010 roku
Google ogłosiło, że jego własne
aplikacje przestaną w niej działać.

A pewne studio projektowe w Denver
uznało, że to zasługuje na pogrzeb.

<!-- S77 -->
Prawdziwy.

Trumna.

Mowa pogrzebowa.

Od osiemdziesięciu do stu osób
przyszło zobaczyć, jak grzebie się
przeglądarkę.

Planowali trzydzieści.

<!-- S78 -->
A Microsoft przysłał kwiaty.

Na bileciku było:
dzięki za dobre czasy,
Internet Explorerze 6.

<!-- S79 -->
Dokładnie rok później
Microsoft uruchomił stronę.

Śledziła, jaka część świata
nadal używa
Internet Explorera 6,
kraj po kraju.

<!-- S80 -->
W tamtym momencie
było to wciąż dwanaście procent.

Celem było zepchnięcie tego
poniżej jednego.

Firma, która zbudowała przeglądarkę,
prowadziła publiczne odliczanie
do śmierci własnego produktu.

<!-- S81 -->
Więc dlaczego błędy miały imiona?

Bo nazywasz to,
czego nie da się obejść.

<!-- S82 -->
Nikt nie nazywa pogody
w kraju,
przez który tylko przejeżdża.

Nazywasz ją tam, gdzie mieszkasz.

A przez jakieś dziesięć lat
sieć mieszkała właśnie tam.

<!-- S83 -->
Ale usunięcie Internet Explorera 6
z sieci to inna historia.

I tam pójdziemy następnym razem.

Jeśli chcesz tę część,
jest przycisk subskrypcji,
a link do części pierwszej jest pod filmem.
