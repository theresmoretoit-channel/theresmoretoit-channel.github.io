<!-- S01 -->
Wyobraź sobie program komputerowy
o trzech miliardach znaków
instrukcji.

<!-- S02 -->
I że za każdym razem,
gdy uruchamiasz nowy proces,
kopiujesz do niego cały program.

<!-- S02b -->
Dwa razy.

<!-- S03 -->
Nie tylko te funkcje,
których ten proces potrzebuje.
Absolutnie wszystko.
Każdy moduł.
Każdą zależność.
Każdy kawałek starego kodu legacy.

<!-- S04 -->
A potem proces po prostu ignoruje
dziewięćdziesiąt dziewięć procent.
Byłaby to fatalna
inżynieria oprogramowania.

<!-- S05 -->
A jednak...

<!-- S06 -->
...mniej więcej to właśnie
robią twoje komórki.

<!-- S07 -->
Prawie każda komórka twojego ciała,
która ma jądro,
zawiera w gruncie rzeczy tę samą
pełną kopię twojego genomu.

<!-- S08 -->
Neuron ją ma.
Komórka wątroby ją ma.
Komórka skóry ją ma.
A mimo to zachowują się
zupełnie inaczej.

<!-- S09 -->
Kod tam jest.
Tyle że większość się nie używa.

<!-- S10 -->
Gen można sobie wyobrazić,
bardzo z grubsza,
jako funkcję albo moduł.

<!-- S11 -->
Niesie informację,
z której ostatecznie może
powstać określony
produkt funkcjonalny,
często białko.
Możemy to sobie wyobrazić tak.

<!-- S12 -->
Ale mieć funkcję w kodzie
to nie znaczy, że działa.
Coś musi ją uruchomić.
I tu właśnie biologia
robi się ciekawa.

<!-- S13 -->
Bo w komputerze
po prostu piszę to.
Albo w kodzie maszynowym.

<!-- S14 -->
Procesor dokładnie wie, co robić.
Jest instrukcja.
Jest adres.
Jest wskaźnik instrukcji.

<!-- S15 -->
Ale komórka nie ma procesora,
który wykonywałby instrukcje
DNA jedna po drugiej.

<!-- S16 -->
Więc...

<!-- S17 -->
...skąd wie, czego użyć?

<!-- S18 -->
Tu porównanie
z komputerem robi się dziwne.
W komputerze możesz skoczyć
pod konkretny adres w pamięci.

<!-- S19 -->
Możesz mieć uprawnienia dostępu.
Możesz mieć procesy.
Możesz mieć pliki konfiguracyjne.
Możesz mieć zdarzenia,
które wyzwalają konkretne fragmenty kodu.

<!-- S20 -->
Biologia ma rzeczy,
które grają zaskakująco podobne role.

<!-- S21 -->
Czynniki transkrypcyjne wiążą się
z określonymi sekwencjami DNA
i wpływają na to, czy gen
ulegnie transkrypcji, czy nie.

<!-- S22 -->
Sekwencje regulatorowe wpływają na to,
kiedy i gdzie geny ulegają ekspresji.
Struktura chromatyny decyduje,
jak dostępne są poszczególne
odcinki DNA.

<!-- S23 -->
A komórki bez przerwy odbierają
sygnały z otoczenia.

<!-- S24 -->
Więc zamiast procesora,
wskaźnika instrukcji,
adresu w pamięci i wykonania...

<!-- S25 -->
...masz raczej coś takiego.

<!-- S26 -->
Nie ma jednego wskaźnika instrukcji.
Jest ogromna sieć
oddziaływań molekularnych.

<!-- S27 -->
DNA tam jest.
Ale różne jego części
są mniej lub bardziej dostępne
dla maszynerii molekularnej,
która je czyta.

<!-- S28 -->
Więc mieć kod
to nie to samo,
co mieć do kodu dostęp.
Komórka wątroby nie musi kasować
genów neuronów.
Wystarczy, że reguluje,
czy zostaną użyte.

<!-- S29 -->
Wróćmy
do naszego projektu.
Powiedzmy, że rozwijasz
ogromną aplikację.

<!-- S30 -->
Tworzysz nowy moduł o nazwie finger.
I zamiast zaimportować
te kilka potrzebnych funkcji...

<!-- S31 -->
...kopiujesz do niego całe
repozytorium człowieka.

<!-- S32 -->
Mózg.
Wątrobę.
Serce.
Układ odpornościowy.
Układ rozrodczy.
Wszystko.

<!-- S33 -->
I robisz to znowu...

<!-- S34 -->
...dla każdej komórki.

<!-- S35 -->
Jako programista
pewnie byś zapytał...
Kto to zaprojektował?

<!-- S36 -->
A odpowiedź brzmi...

<!-- S37 -->
Nikt.

<!-- S38 -->
No... Nie do końca nikt.
Ewolucja.

<!-- S39 -->
A ewolucja ma zupełnie inną
filozofię rozwoju.

<!-- S40 -->
Wyobraź sobie, że otwierasz repozytorium
o nazwie człowiek,
którego historia commitów
sięga miliardy lat wstecz.

<!-- S41 -->
Żaden architekt nie usiadł
i nie zaprojektował wersji 1.0.
Nigdy nie było czystego przepisania.
Nigdy nie powstał człowiek wersja dwa
z przeprojektowaną architekturą.

<!-- S42 -->
Zamiast tego...
Dodaj funkcję.
Załataj błąd.
Zduplikuj moduł.
Użyj starego modułu ponownie.

<!-- S43 -->
Obejdź ograniczenie.
Dodaj kolejną prowizorkę.
Zostaw stare API,
bo coś od niego zależy.

<!-- S44 -->
Znowu.
I znowu.
I znowu.
Przez miliardy lat.

<!-- S45 -->
Ewolucja nie pyta,
jaka architektura jest najczystsza.
Jej pytanie jest znacznie prostsze.
Czy ten organizm
skutecznie się rozmnaża?

<!-- S46 -->
Jeśli tak,
kod przeżywa.

<!-- S47 -->
Wyobraź sobie, że dziedziczysz projekt
utrzymywany
przez miliony programistów,
przez miliardy lat,
i nie masz żadnej możliwości
przepisania go w całości.

<!-- S48 -->
Natrafiasz na coś i pytasz...
Po co to tu jest?
Bo coś od tego zależało.

<!-- S49 -->
Czemu to API jest takie dziwne?
Legacy.

<!-- S50 -->
To właśnie ewolucja.
Doskonały system legacy.
Nie refaktoryzuje.
Zmienia to, co już istnieje.

<!-- S51 -->
A po miliardach lat...

<!-- S52 -->
...wychodzimy z tego my.

<!-- S53 -->
Nowoczesne wytwarzanie oprogramowania
opiera się na rozsądnym pomyśle.
Wprowadzasz zmianę.
Potem ją testujesz.

<!-- S54 -->
Commit.
Build.
Testy jednostkowe.
Testy integracyjne.
Wdrożenie.

<!-- S55 -->
Biologia ma coś,
co wygląda mniej więcej podobnie.
Zachodzi mutacja.

<!-- S56 -->
A potem...
Organizm albo przeżywa
i się rozmnaża.
Albo nie.

<!-- S57 -->
Nie ma środowiska staging.
Nie ma rollbacku.

<!-- S58 -->
A czasem
zdarza się coś znacznie gorszego.
Mutacja może sprawić, że komórka
lepiej przeżywa i się mnoży
wewnątrz organizmu.
To może przyczynić się do raka.

<!-- S59 -->
Biologia ma więc dość przerażającą
wersję ciągłej integracji.
Testy odbywają się
na systemie produkcyjnym.

<!-- S60 -->
Ale właśnie tu
porównanie z oprogramowaniem
robi się jeszcze ciekawsze.
Kiedy patrzysz na ludzkie ciało,
kusi, żeby wyobrazić sobie
coś takiego.

<!-- S61 -->
Tyle że system
wcale tak nie działa.
Nie ma centralnego serwera,
który rozsyła polecenia komórkom.

<!-- S62 -->
Twoje komórki bez przerwy śledzą
swoje najbliższe otoczenie.
Odbierają sygnały chemiczne.
Mają kontakt z sąsiadkami.
Reagują na hormony.

<!-- S63 -->
Komórka nigdy nie dostaje
wiadomości o treści...

<!-- S64 -->
...komórko numer siedem milionów
trzysta dziewięćdziesiąt dwa tysiące
sto osiemdziesiąt cztery.
Uruchom ekspresję genu X, proszę.

<!-- S65 -->
Jeśli programujesz,
nagle przydaje się
jeszcze jedno pojęcie.
Systemy rozproszone.

<!-- S66 -->
Twoje komórki to w praktyce
ogromna liczba
pojedynczych agentów.
Każdy ma własny stan.
Własne czujniki.
Własne wejścia.
Własne reakcje.

<!-- S67 -->
Nie ma jednej wielkiej pętli,
która mówi każdej komórce, co robić.
Bliżej temu do
systemu wieloagentowego.
Albo do roju.
Albo do automatu komórkowego.

<!-- S68 -->
Proste lokalne reguły...

<!-- S69 -->
...z których powstaje zdumiewająco
złożone zachowanie całości.

<!-- S70 -->
I jeszcze coś, co w normalnym
oprogramowaniu byłoby nie do przyjęcia.
Twoje ciało działa
bez przerwy od dziesięcioleci.

<!-- S71 -->
Żadnego restartu.
Żadnego okna serwisowego.

<!-- S72 -->
A mimo to system
cały czas się zmienia.
Komórki umierają.
Powstają nowe.
Białka powstają i się rozpadają.

<!-- S73 -->
DNA jest kopiowane.
Uszkodzenia są naprawiane.
Części są wymieniane.

<!-- S74 -->
System się nie wyłącza po to,
żeby dało się zrobić serwis.
Robi serwis
na pełnym biegu.

<!-- S75 -->
Prawie jakbyś miał serwer,
który wymienia własne części
dokładnie w chwili,
gdy obsługuje żądania...

<!-- S76 -->
...i nigdy nie schodzi offline.

<!-- S77 -->
Komórki mają własną maszynerię.
Komunikują się.
Odpowiadają.
Regulują się nawzajem.
Tworzą tkanki.
Tkanki tworzą narządy.
Narządy tworzą układy.
A układy tworzą organizm.

<!-- S78 -->
I nie ma ani jednego elementu,
który trzymałby całą architekturę
w głowie.

<!-- S79 -->
I jakimś cudem...

<!-- S80 -->
...to działa.

<!-- S81 -->
Nie idealnie.
Ani trochę nie idealnie.

<!-- S82 -->
Ale dość dobrze, żeby powstały oczy.
Serca.
Układy odpornościowe.
Mózgi.

<!-- S83 -->
I organizmy zdolne
pisać oprogramowanie i narzekać,
jak fatalnie ten system
jest zaprojektowany.

<!-- S84 -->
Nazywamy DNA kodem.
I to porównanie jest przydatne.
Geny trochę przypominają funkcje.
Mutacje trochę przypominają
zmiany w kodzie źródłowym.

<!-- S85 -->
Ale jest
istotna różnica.
DNA wcale nie jest
pełnym planem człowieka.

<!-- S86 -->
Nigdzie nie ma w nim linijki...
Stwórz rękę.
Stwórz oko.
Stwórz serce.

<!-- S87 -->
DNA bierze za to udział
w ogromnej sieci oddziaływań,
do której należą cząsteczki, komórki,
siły fizyczne, gradienty chemiczne,
czas i środowisko.

<!-- S87b -->
Organizm wyłania się z tego wszystkiego.

<!-- S88 -->
DNA lepiej więc rozumieć
jako zbiór instrukcji i zasad
osadzony w układzie fizycznym...

<!-- S89 -->
...niż jako pełny wydruk
kodu źródłowego człowieka.
A to jest właściwie znacznie dziwniejsze.

<!-- S90 -->
Umiemy zsekwencjonować genom,
zidentyfikować geny
i zmierzyć białka.

<!-- S91 -->
Ale wciąż nie umiemy wziąć DNA
ze zwykłej ludzkiej komórki,
wgrać go do komputera,
nacisnąć uruchom...

<!-- S92 -->
...i patrzeć, jak ten człowiek rośnie.

<!-- S93 -->
Mamy genom.
Ale genom
to nie cała maszyna.

<!-- S94 -->
I tu kończymy.
Zaczęliśmy od znanej myśli.
DNA jest jak kod komputerowy.

<!-- S95 -->
I to porównanie okazuje się
zaskakująco przydatne.
Ale im głębiej patrzymy,
tym dziwniejszy staje się system.

<!-- S96 -->
Nie ma procesora.
Nie ma systemu operacyjnego.
Nie ma centralnego serwera.

<!-- S97 -->
Nie ma programisty.
Nie ma GitHuba.
Nie ma przeglądu kodu.
Nie ma środowiska staging.
Nie ma rollbacku.
Trudno tu w ogóle mówić
o czystej architekturze.

<!-- S98 -->
Są biliony maleńkich agentów,
z których każdy stosuje lokalne reguły,
dogaduje się z sąsiadami,

<!-- S99 -->
korzysta z ogromnego, prastarego,
bez przerwy zmienianego repozytorium...
I jakimś cudem powstaje z tego
działający organizm.

<!-- S100 -->
Więc jeśli biologia to oprogramowanie...

<!-- S101 -->
...jest chyba najstarszym,
najbardziej chaotycznym i przekombinowanym
systemem legacy, jaki można wymyślić.

<!-- S102 -->
System z miliardami lat
commitów.
Prawie bez refaktoryzacji.
Bez centralnego administratora.
I absolutnie bez restartu.

<!-- S103 -->
I jakimś cudem...

<!-- S104 -->
...działa na produkcji
od miliardów lat.
