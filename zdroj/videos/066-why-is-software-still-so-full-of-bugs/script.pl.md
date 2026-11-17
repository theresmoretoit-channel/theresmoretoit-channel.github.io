<!-- S01 -->
Co kilka dni w wiadomościach pojawia się
kolejny poważny błąd.
Błąd, który pozwala komuś ominąć logowanie.
Błąd, przez który wyciekają prywatne dane.
Błąd, który oddaje twój komputer napastnikowi.

<!-- S02 -->
Czasem to Windows. Czasem Linux.
Przeglądarka, baza danych, usługa w chmurze...
albo mała biblioteka,
od której zależą miliony programistów.

<!-- S03 -->
A reakcja jest niemal zawsze taka sama.
Jak programiści mogli to przeoczyć?

<!-- S04 -->
To profesjonaliści.
Mają przeglądy kodu, testy automatyczne,
audyty bezpieczeństwa, fuzzing...
a błędy i tak wciąż się pojawiają.

<!-- S05 -->
Więc czy w ogóle da się
napisać złożone oprogramowanie bez błędów?

<!-- S06 -->
Zacznijmy od liczby.
Wyobraź sobie program ze stoma ustawieniami,
każde albo włączone, albo wyłączone.

<!-- S07 -->
Sto prostych decyzji tak albo nie.
Ile to kombinacji?

<!-- S08 -->
Dwa do setnej potęgi.
To mniej więcej milion bilionów bilionów.

<!-- S09 -->
Wyobraź sobie teraz, że możesz sprawdzać
miliard kombinacji na sekundę.
I że zacząłeś w chwili Wielkiego Wybuchu.

<!-- S10 -->
Do dziś sprawdziłbyś
mniej więcej jedną kombinację na trzy tysiące.

<!-- S11 -->
A sto przełączników to nic.
Prawdziwy program ma ich miliony.
Więc „po prostu sprawdź wszystko"
nie jest drogie. Jest niemożliwe.

<!-- S12 -->
A te przełączniki nie są niczym egzotycznym.
Weź jedną z najprostszych rzeczy,
jakie program w ogóle robi.
Użytkownik prosi o swoje konto po numerze.
Znajdujemy je w bazie danych.
I odsyłamy z powrotem.

<!-- S13 -->
Ale co, jeśli użytkownik nie istnieje?
Co, jeśli ktoś wyśle tekst zamiast liczby?
Albo liczbę ujemną? Albo ogromną?

<!-- S14 -->
Co, jeśli ta osoba nie ma prawa tego zobaczyć?
Co, jeśli ktoś usunie konto
dokładnie w chwili, gdy je wczytujemy?
Co, jeśli to samo żądanie przyjdzie dwa razy?

<!-- S15 -->
Każde z tych pytań jest proste.
Problemem jest to, jak się łączą.
Każde to kolejny przełącznik.

<!-- S15b -->
Przy okazji, jeśli lubisz takie
filmy, możesz zasubskrybować kanał.

To naprawdę pomaga kanałowi.

<!-- S16 -->
A komputer nie rozwiąże tego za nas.
Robi dokładnie to, co mu każemy.
Nie to, co mieliśmy na myśli.

<!-- S17 -->
Dlatego wymyśliliśmy języki programowania.
Pozwalają nam opisywać rzeczy złożone
bez myślenia o każdym szczególe.

<!-- S18 -->
Ale niektóre pilnują mniej,
niż byś chciał.
Weź C. Jest szybki, jest prosty
i daje ci ogromną kontrolę nad pamięcią.

<!-- S19 -->
Więc możesz napisać coś takiego.
Rezerwujemy miejsce na szesnaście znaków.
Potem mówimy: skopiuj tu dane wejściowe.

<!-- S20 -->
A co, jeśli dane wejściowe mają
pięćset znaków?
C nie zapyta.
Po prostu pisze dalej, za koniec.

<!-- S21 -->
A co jest tuż za tymi szesnastoma znakami?
Często coś bardzo ważnego.

<!-- S22 -->
Kiedy program wywołuje funkcję,
zapisuje, gdzie ma wrócić,
gdy funkcja się skończy.
Adres powrotu.
W klasycznym układzie leży
niedaleko za końcem naszego bufora.

<!-- S23 -->
Więc napastnik wysyła dane wejściowe
o dokładnie odpowiedniej długości.
Najpierw własne instrukcje.
Potem, na samym końcu, nowy adres powrotu...
wskazujący z powrotem na te instrukcje.

<!-- S24 -->
Funkcja się kończy.
Procesor sprawdza, gdzie wrócić...
i skacze prosto w kod napastnika.

<!-- S25 -->
Teraz uruchamia jego program,
ze wszystkimi uprawnieniami twojego programu.
To właśnie znaczy „wykonanie dowolnego kodu".

<!-- S26 -->
A procesor nie zrobił nic złego.
Wykonał instrukcje.

<!-- S27 -->
W 1988 roku błąd dokładnie taki jak ten
pozwolił robakowi Morrisa rozprzestrzenić się
po wczesnym internecie.
I ta sama sztuczka jest używana
w atakach do dziś.

<!-- S28 -->
Więc nowsze języki oddają część pracy
kompilatorowi.
Rust na przykład odmawia zbudowania
wielu programów, które mogłyby źle użyć pamięci.

<!-- S29 -->
Programista mówi:
przecież wiem dokładnie, co robię!
A kompilator mówi:
tak mówią wszyscy.

<!-- S30 -->
I słusznie jest podejrzliwy.
Microsoft i zespół Chrome od Google'a
zgłosili oba,
że około siedemdziesiąt procent
błędów bezpieczeństwa, które zbadali,
bierze się z problemów z bezpieczeństwem pamięci.

<!-- S31 -->
Ale program może być doskonale bezpieczny pamięciowo
i wciąż całkowicie błędny.

<!-- S32 -->
Wyobraź sobie, że użytkownik się loguje.
Jego hasło zostaje poprawnie sprawdzone.
Nic się nie zawiesza. Pamięć nie zostaje uszkodzona.

<!-- S33 -->
A potem program pokazuje mu
cudze dane.
Bo sprawdzenie uprawnień
napisano trochę źle.

<!-- S34 -->
Żaden język nie wychwyci tego sam.
Język nie wie,
co program miał robić.
Wiemy to tylko my.

<!-- S35 -->
Więc wróćmy do testów.
Test może ci powiedzieć:
dla tych danych dostałem taki wynik.

<!-- S36 -->
Nie może ci powiedzieć:
program jest poprawny dla każdych danych.
A już widzieliśmy,
dlaczego nie da się sprawdzić wszystkich.

<!-- S37 -->
W 1970 roku informatyk
Edsger Dijkstra ujął to w jednym zdaniu.
Testy mogą pokazać obecność błędów,
ale nigdy ich brak.

<!-- S38 -->
Dobrze. Więc zamiast testować,
czemu nie napisać programu,
który sprawdza inne programy
i dowodzi, że są poprawne?
Podaj mu dowolny kod, a powie ci,
czy ten kod robi to, co powinien.

<!-- S39 -->
Na to pytanie odpowiedziano,
zanim zbudowano pierwszy prawdziwy komputer.
W 1936 roku Alan Turing udowodnił,
że taki program nie może istnieć.

<!-- S40 -->
Nie że jeszcze nikt go nie zbudował.
Że nie może istnieć w ogóle.

<!-- S41 -->
Pokazał, że żaden program nie potrafi rozstrzygnąć,
dla każdego innego programu,
czy ten kiedykolwiek się zatrzyma.

<!-- S42 -->
A w 1953 roku Henry Rice poszedł dalej.
To samo dotyczy każdego nietrywialnego pytania
o to, co program naprawdę robi.

<!-- S43 -->
Czy jest bezpieczny? Czy ujawnia dane?
Czy daje właściwą odpowiedź?
Nie ma ogólnej metody,
która rozstrzyga to dla każdego programu.

<!-- S44 -->
Więc oprogramowanie bez błędów jest niemożliwe?
Niezupełnie.
Dla jednego konkretnego programu
czasem da się udowodnić, że jest poprawny,
ogromnym nakładem pracy.

<!-- S45 -->
W 2009 roku zespół w Australii udowodnił,
że małe jądro systemu operacyjnego,
zwane seL4,
robi dokładnie to, co mówi jego specyfikacja.

<!-- S46 -->
Miało poniżej dziesięciu tysięcy wierszy kodu.
Zbudowanie jądra zajęło
około dwóch osobolat.
Udowodnienie jego poprawności — około dwudziestu.
Nowoczesna przeglądarka
ma dziesiątki milionów wierszy.

<!-- S47 -->
I nawet ten dowód ma haczyk.
Pokazuje, że program zgadza się ze specyfikacją.
Nie potrafi pokazać, że specyfikacja
jest tym, czego naprawdę chcieliśmy.

<!-- S48 -->
A specyfikację piszą ludzie.
Więc pytanie wraca do nas.

<!-- S49 -->
I nie chodzi tylko o nasz własny kod.
Programista dziś opiera się na frameworkach,
bibliotekach i setkach zależności.
Każda warstwa oszczędza nam ogromu pracy.
Ale każda warstwa to coś,
co musimy zrozumieć...
albo przynajmniej czemu zaufać.

<!-- S50 -->
Co znaczy, że nie musisz napisać błędu,
żeby mieć go w swoim oprogramowaniu.
Wystarczy, że go zainstalujesz.

<!-- S51 -->
Do tego dorzuć presję.
Nikt nie chce doskonałego produktu za dziesięć lat.
Chcą działającego za miesiąc.
A włamanie, które nigdy się nie zdarzyło,
bardzo trudno pokazać na prezentacji.

<!-- S52 -->
I tu najdziwniejsza rzecz.
Nasze narzędzia wciąż się poprawiają.
Bezpieczniejsze języki, fuzzing, bug bounty...

<!-- S53 -->
A mimo to liczba znanych podatności
wciąż rośnie.
Tylko w 2024 roku około czterdziestu tysięcy
dostało oficjalny numer.

<!-- S54 -->
Po części dlatego, że piszemy też
o wiele więcej oprogramowania niż kiedykolwiek.
To jak uczynić każdą drogę bezpieczniejszą...
budując przy tym miliony razy więcej dróg.

<!-- S55 -->
Więc czy programiści są słabi w swojej pracy?
Nie.
Prosimy ich od dawna o coś,
czego żadna ogólna metoda nie może zagwarantować.

<!-- S56 -->
Więc może
„jak pisać oprogramowanie bez błędów?"
to złe pytanie.

<!-- S57 -->
Lepsze pytanie brzmi:
jak budować systemy, które pozostają bezpieczne,
nawet gdy oprogramowanie ma błędy?

<!-- S58 -->
I właśnie w tę stronę zmierza bezpieczeństwo.
Nie mówi: nigdy nie popełnij błędu.
Mówi: zakładaj, że już go popełniłeś.

<!-- S59 -->
Pamiętasz ten adres powrotu?
Dziś system go pilnuje.
Miesza to, gdzie rzeczy leżą w pamięci.
I odmawia wykonywania instrukcji
ukrytych w danych.

<!-- S60 -->
Błąd w naszym kodzie w C wciąż tam jest.
Tyle że o wiele trudniej zamienić go w atak.

<!-- S61 -->
I ta sama idea jest wszędzie.
Piaskownice, ograniczone uprawnienia,
izolowane procesy, szyfrowanie,
kopie zapasowe, monitorowanie...
warstwa po warstwie,
żeby jeden błąd nie stał się katastrofą.

<!-- S62 -->
I ma to bardzo praktyczny skutek.
Skoro błędy są nieuniknione,
ich naprawianie nie jest opcjonalne.

<!-- S63 -->
Oprogramowanie, którego dziś używasz,
może zawierać podatność,
której nikt jeszcze nie znalazł.

<!-- S64 -->
A gdy ktoś ją znajdzie,
aktualizacja jest różnicą między
„wykryto podatność"
a „zostaliśmy zhakowani".

<!-- S65 -->
To samo dotyczy systemów, które budujemy.
Stare biblioteki i niewspierane platformy
nie stają się bezpieczniejsze przez ignorowanie.
Zamieniają się w dług techniczny.

<!-- S66 -->
A dlaczego ten dług trzeba spłacić —
mój film
„Nadal działa. Więc po co aktualizować?"
opowiada właśnie o tym.

<!-- S67 -->
Bo w oprogramowaniu
„nadal działa"
i „nadal jest bezpieczne"
to dwie bardzo różne rzeczy.
