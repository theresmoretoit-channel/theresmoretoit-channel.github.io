<!-- S01 -->
Do skrzyżowania podjeżdżają cztery samochody
dokładnie w tej samej chwili.
Żadnych świateł. Żadnych znaków.
Tylko zasada, która obowiązuje w wielu krajach:
ustąp pierwszeństwa autu z prawej.

<!-- S02 -->
Każdy kierowca patrzy w prawo
i widzi auto, na które musi poczekać.
Więc każdy kierowca czeka.

<!-- S03 -->
Nikt nie łamie zasady.
Wszyscy przestrzegają jej doskonale.
I nikt nigdy nie ruszy.

<!-- S04 -->
Informatycy nazywają to zakleszczeniem, po angielsku deadlock.
I zdarza się to nie tylko na drogach.
Zdarza się w bazach danych,
systemach operacyjnych i zwykłym oprogramowaniu.

<!-- S05 -->
Komputery często dobrze wykrywają
zakleszczenie, gdy już do niego doszło.
Ale czy program mógłby przeczytać inny program
i powiedzieć ci z całą pewnością,
czy ten kiedykolwiek utknie?

<!-- S06 -->
W przypadku wielu programów tak.
Ale metoda, która działa
dla każdego możliwego programu,
nie może istnieć.
I nie dlatego, że komputery
nie są jeszcze dość szybkie.
Żaden szybszy komputer nigdy tego nie zmieni.

<!-- S07 -->
Oto jak program może utknąć.
Wyobraź sobie sklep internetowy,
w którym jednocześnie działają dwa zadania.

<!-- S08 -->
Zanim zadanie cokolwiek zmieni,
zakłada na to blokadę,
żeby nikt inny nie mógł tego ruszyć.
Jak wtedy, gdy bierzesz jedyny klucz do pokoju.

<!-- S09 -->
Pierwsze zadanie blokuje konto klienta,
a potem próbuje zablokować jego zamówienie.
Drugie blokuje zamówienie,
a potem próbuje zablokować konto.

<!-- S10 -->
Jedno trzyma konto
i czeka na zamówienie.
Drugie trzyma zamówienie
i czeka na konto.
Żadne nie puści tego, co trzyma.

<!-- S11 -->
A najdziwniejsze jest to,
że ten kod może zadziałać milion razy
bez żadnego problemu.
Dopiero gdy oba zadania nałożą się na siebie
akurat w złej kolejności,
wszystko staje.

<!-- S12 -->
Błąd był tam przez cały czas.
Niefortunny zbieg w czasie tylko go ujawnił.

<!-- S12b -->
Przy okazji, jeśli lubisz takie
filmy, możesz zasubskrybować kanał.

To naprawdę pomaga kanałowi.

<!-- S13 -->
Bazy danych natrafiają na to cały czas,
więc są czujne.
Rysują mapę tego, kto na kogo czeka.

<!-- S14 -->
Pierwsze czeka na drugie.
Drugie czeka na pierwsze.
Kiedy strzałki zamkną się w pętlę,
to jest zakleszczenie.
Żadnego zgadywania. Pętlę po prostu widać.

<!-- S15 -->
Wtedy baza danych robi coś brutalnego.
Wybiera jedno z zadań
i odrzuca wyniki jego pracy.

<!-- S16 -->
Microsoft SQL Server nawet informuje przegranego,
że został wybrany
na ofiarę zakleszczenia
i powinien spróbować jeszcze raz.

<!-- S17 -->
Drugie zadanie działa dalej,
a ofiara może po prostu spróbować jeszcze raz.

<!-- S18 -->
Zauważ, co to naprawia, a czego nie.
Zakleszczenie zostało rozwiązane.
Ale kod, który je spowodował, wciąż tam jest
i czeka na kolejny pechowy moment.

<!-- S19 -->
Wykrycie zakleszczenia,
które już nastąpiło,
to więc ta łatwa część.
Trudne pytanie brzmi inaczej.

<!-- S20 -->
Nie: czy ten program właśnie utknął?
Tylko: daj mu te dane wejściowe.
Czy może kiedykolwiek utknąć?

<!-- S21 -->
Pierwsze to zdjęcie teraźniejszości.
Wystarczy na nie spojrzeć.
Drugie to przewidywanie
każdej możliwej przyszłości.

<!-- S22 -->
A programy bardzo to utrudniają.
Podejmują decyzje. Powtarzają różne rzeczy.
Mogą wykonywać obliczenia, które trwają
sekundę albo tysiąc lat.

<!-- S23 -->
Program może utknąć od razu,
po milionie kroków,
przy jednym rzadkim zestawie danych
albo wcale.

<!-- S24 -->
Możesz go po prostu uruchomić i patrzeć.
Ale jeśli po godzinie nie utknął,
co ci to mówi?

<!-- S25 -->
Nic.
Może utknąć w następnej sekundzie
albo nigdy.

<!-- S26 -->
W 1936 roku młody matematyk
Alan Turing wykazał,
że na niektóre pytania o programy
nie odpowie żaden program.
Najsłynniejsze z nich brzmi jeszcze prościej.

<!-- S27 -->
Weź dowolny program i jego dane wejściowe.
Czy w końcu się zatrzyma?
Czy może będzie działał bez końca?

<!-- S28 -->
Dziś nazywa się to problemem stopu.
I żaden program nie potrafi go rozstrzygnąć
poprawnie w każdym przypadku.

<!-- S29 -->
Idea dowodu
jest zaskakująco krótka.
Załóżmy, że ktoś daje ci
doskonały weryfikator stopu.

<!-- S30 -->
Teraz piszesz mały, przekorny program.
Pyta on weryfikator o samego siebie
i robi dokładnie odwrotnie.

<!-- S31 -->
Jeśli weryfikator powie, że program się zatrzyma,
ten zapętla się w nieskończoność.
Jeśli weryfikator powie, że będzie działał bez końca,
program od razu się zatrzymuje.

<!-- S32 -->
Cokolwiek weryfikator o nim powie,
myli się.
Więc doskonały weryfikator nie może istnieć.

<!-- S33 -->
Co to ma zatem wspólnego z zakleszczeniami?
Bardzo wiele.

<!-- S34 -->
Wyobraź sobie, że ktoś twierdzi, że zbudował
doskonały predyktor zakleszczeń.
Daj mu dowolny program i jego dane wejściowe,
a zawsze poprawnie ci powie,
czy ten program kiedykolwiek utknie.

<!-- S35 -->
Użyjmy go,
żeby rozwiązać problem stopu.

<!-- S36 -->
Weź dowolny program
i umieść go wewnątrz nowego programu.

<!-- S37 -->
Najpierw nowy program
po prostu uruchamia stary,
krok po kroku, w jednym wątku.
Żadnych blokad. Nic współdzielonego.
Nic, co mogłoby kiedykolwiek utknąć.

<!-- S38 -->
Potem, jeśli stary program kiedykolwiek się zakończy,
nowy uruchamia dwa zadania.
Każde chwyta jedną blokadę,
czeka, aż drugie złapie swoją,
a potem sięga po blokadę tego drugiego.
Zakleszczenie, celowo, za każdym razem.

<!-- S39 -->
Jeśli stary program nigdy się nie zakończy,
nowy nigdy nie dojdzie tak daleko.
Żadnego zakleszczenia. Nigdy.

<!-- S40 -->
Nowy program utknie więc
wtedy i tylko wtedy, gdy stary się zatrzyma.

<!-- S41 -->
Teraz zapytaj predyktor
o nowy program.
„Tak, dojdzie do zakleszczenia”
oznacza, że stary program się zatrzymuje.
„Nie” oznacza, że działa bez końca.

<!-- S42 -->
Właśnie rozwiązaliśmy problem stopu.
A dokładnie tego zrobić się nie da.

<!-- S43 -->
Więc doskonały predyktor zakleszczeń
też nie może istnieć.

<!-- S44 -->
Problem nie leży w blokadach,
w bazach danych ani w złych programistach.
Program może ukryć dowolne obliczenie
na drodze do zakleszczenia.
Żeby przewidzieć zakleszczenie,
musiałbyś przewidzieć, czy to obliczenie się skończy.

<!-- S45 -->
Ale chwileczkę.
Prawdziwy komputer nie jest nieskończony.
Jego pamięć ma ograniczoną liczbę stanów.
Czy nie dałoby się po prostu sprawdzić ich wszystkich?

<!-- S46 -->
Dla maszyny ze stałą ilością
pamięci w zasadzie tak.
W praktyce spróbuj je policzyć.

<!-- S47 -->
Zawartość pamięci laptopa
z ośmioma gigabajtami
może mieć tyle różnych układów,
że samo zapisanie tej liczby
wymaga około dwudziestu miliardów cyfr.

<!-- S48 -->
Liczba atomów
w obserwowalnym Wszechświecie
ma ich około osiemdziesięciu.

<!-- S49 -->
Na prawdziwej maszynie sprawdzenie wszystkiego
jest więc teoretycznie możliwe,
a w praktyce beznadziejne.

<!-- S50 -->
Ale to zupełnie inny mur.
Granica Turinga nie dotyczy zbyt wielu stanów.
Dotyczy programów,
które zawsze mogą poprosić o więcej pamięci.
Dla nich żaden doskonały predyktor nie może istnieć,
bez względu na to, jak duży jest komputer.

<!-- S51 -->
Czy to znaczy, że z zakleszczeniami nic nie da się zrobić?
Nie.
To znaczy tylko, że nie ma doskonałego weryfikatora.
Więc programiści piszą programy,
które łatwiej sprawdzić.

<!-- S52 -->
Najprostszy trik to ustalona kolejność.
Każde zadanie musi zablokować konto
przed zamówieniem.
Nigdy na odwrót.

<!-- S53 -->
Jeśli każde zadanie naprawdę trzyma się tej kolejności,
pętla nie może się zamknąć
i taki rodzaj zakleszczenia nie może wystąpić.

<!-- S54 -->
Inne systemy poddają się po przekroczeniu limitu czasu,
biorą wszystkie blokady naraz
albo pozwalają bazie danych wybrać ofiarę
i po prostu próbują ponownie.

<!-- S55 -->
A w przypadku małych, starannie opisanych projektów
narzędzia potrafią sprawdzić każdy możliwy stan.
Inżynierowie z Amazona użyli jednego z nich,
żeby znaleźć błąd, który wymagał trzydziestu pięciu kroków
w dokładnie właściwej kolejności, żeby się ujawnić.

<!-- S56 -->
Te narzędzia działają,
bo ograniczono zakres problemu.
Sprawdzają model systemu,
a nie każdy program, jaki mógłby kiedykolwiek istnieć.

<!-- S57 -->
Ale w przypadku prawdziwego kodu
weryfikator, który przyjmuje dowolny program,
musi z czegoś zrezygnować.
Może ostrzegać przed zakleszczeniami,
które nie mogą wystąpić,
przeoczyć niektóre, które mogą,
albo czasem w ogóle nie dać odpowiedzi.

<!-- S58 -->
Weryfikator, który nigdy nie podnosi fałszywego alarmu,
nigdy żadnego zakleszczenia nie przeocza
i zawsze daje odpowiedź,
i to dla każdego programu,
to dokładnie to, co wykluczył Turing.

<!-- S59 -->
Wróćmy na skrzyżowanie:
czterej kierowcy nie będą tam stali wiecznie.

<!-- S60 -->
Ktoś macha ręką.
Jeden kierowca przepuszcza pozostałych
i po kilku sekundach jest po wszystkim.

<!-- S61 -->
Dokładnie to samo robi baza danych.
Nie przewiduje zakleszczenia.
Zauważa je
i każe komuś ustąpić.

<!-- S62 -->
Niektóre problemy wymagają szybszego komputera.
Niektóre lepszego pomysłu.

<!-- S63 -->
A niektóre, tak jak ten,
w ogóle nie mają doskonałego rozwiązania.
Tylko dobre zasady
i kogoś, kto jest gotów pomachać.
