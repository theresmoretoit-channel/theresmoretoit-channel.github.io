<!-- S01 -->
Oto kompletne wymaganie
dla oprogramowania biznesowego.
Użytkownik może anulować zamówienie.

<!-- S02 -->
Sześć słów.
Każdy programista by przytaknął.
Każdy klient by to podpisał.

<!-- S03 -->
Czy więc użytkownik może anulować zamówienie,
kiedy faktura już poszła?
Kiedy zostało już wysłane?

<!-- S04 -->
Czy anulowanie go anuluje też
rezerwację u dostawcy?
A co, jeśli jedna osoba je anuluje,
a druga zatwierdzi to samo zamówienie
w tej samej sekundzie?

<!-- S05 -->
To zdanie nie odpowiada na nic z tego.
Kod musi odpowiedzieć na wszystko.
I właśnie za tę lukę między zdaniem
a kodem programiści
tak naprawdę dostają pieniądze.
Przynajmniej kiedyś dostawali.

<!-- S06 -->
Dziś kusi pewien pomysł.
Pisz tylko zdania.
Trzymaj je w dokumentach,
przeglądaj je, wersjonuj je.
A kod niech napisze AI.

<!-- S07 -->
Specyfikacja staje się
kodem źródłowym.
A kod staje się tym, czym dziś
jest asembler: czymś, co działa
i czego nikt nie czyta.

<!-- S08 -->
To dobry pomysł.
Tyle że wcale nie nowy.

<!-- S09 -->
Od prawie siedemdziesięciu lat ludzie próbują
podnieść poziom,
na którym mówimy komputerom, co mają robić.
Narzędzia były różne,
i ich cele też.
Ale każde przenosiło kolejną część pracy
z ludzi na maszyny.

<!-- S10 -->
W 1957 roku zespół z IBM
opublikował artykuł o FORTRANIE.
Już w tytule nazwano go
automatycznym systemem kodowania.

<!-- S11 -->
Wtedy było to trafne określenie.
Pisało się wzory,
a instrukcje maszynowe,
tę część, którą ludzie pisali ręcznie,
generowała teraz sama maszyna.

<!-- S12 -->
Dziś FORTRAN nazywamy kodem.

<!-- S13 -->
W latach 80. narzędzia CASE
i języki czwartej generacji
weszły poziom wyżej.
Rysujesz diagramy, wypełniasz formularze,
a dużą część aplikacji
narzędzie wygeneruje za ciebie.

<!-- S14 -->
W 2001 roku Object Management Group,
organizacja stojąca za UML,
ogłosiła Model Driven Architecture.

<!-- S15 -->
Ta obietnica zabrzmi znajomo.
Opisujesz system raz,
jako model niezależny od jakiejkolwiek technologii.
Potem narzędzia generują implementację
na dowolną platformę, jakiej potrzebujesz.

<!-- S16 -->
Te same reguły biznesowe.
Wymienna technologia.

<!-- S17 -->
A w 2014 roku analitycy z Forrestera
nadali nazwę platformom
do budowania aplikacji biznesowych
przy jak najmniejszej ilości
ręcznie pisanego kodu.
Nazwali to low-code.

<!-- S18 -->
Czy więc cokolwiek z tego zadziałało?

<!-- S19 -->
Częściowo.
W 2014 roku badacze z Lancaster University
opublikowali wyniki ankiety
wśród 450 osób,
które naprawdę stosowały
programowanie sterowane modelem.

<!-- S20 -->
Zadziałało,
i to częściej, niż wielu sądziło.
Ale rzadko w całym systemie.
Ludzie używali go do kluczowych części,
a resztę budowali inaczej.

<!-- S21 -->
Największymi przeszkodami, jakie wskazali,
okazali się ludzie i organizacje,
a nie narzędzia.
Ale jest też ograniczenie techniczne,
a programiści mają o nim dowcip.

<!-- S22 -->
Specyfikacja na tyle precyzyjna,
żeby wygenerować z niej cały program...
ma już nazwę.
Nazywa się kod.

<!-- S23 -->
Żeby wygenerować wszystko,
model musiał mówić wszystko.
Każdy stan, każdy wyjątek,
każde „a co, jeśli dwie osoby zrobią to naraz”.

<!-- S24 -->
W tym momencie
od programowania wcale nie uciekasz.
Po prostu przenosisz je do diagramu,
który często trudniej czytać,
porównywać i przeglądać.

<!-- S25 -->
Już pod koniec lat 70.
Edsger Dijkstra ujął drugą stronę problemu
w krótkiej notatce o dosadnym tytule.
O głupocie
programowania w języku naturalnym.

<!-- S26 -->
Twierdził, że notacja formalna
nie jest ciężarem, który musimy znosić.
Nazwał ją zdumiewająco skutecznym narzędziem
do wykluczania wszelkiego rodzaju bzdur.

<!-- S27 -->
Zwykły język ich nie wyklucza.
Ukrywa je.
Użytkownik może anulować zamówienie.

<!-- S28 -->
Skoro więc nic z tego nie zastąpiło kodu,
po co próbować znowu?

<!-- S29 -->
Bo jedna rzecz naprawdę jest inna.

<!-- S30 -->
Starsze generatory nie umiały wypełnić luki
same z siebie.
Jeśli model nie mówił, co się dzieje
z wysłanym zamówieniem,
ktoś musiał wprost dopisać tę regułę.
Dopóki tego nie zrobił, luka wciąż istniała
i dało się ją znaleźć.

<!-- S31 -->
AI się nie zatrzymuje.
Daj jej to sześciowyrazowe wymaganie,
a odpowie na każde pytanie,
które zadaliśmy na początku.

<!-- S32 -->
Zdecyduje, że wysłane zamówienie
można anulować. Albo że nie można.
Zdecyduje o fakturze
i o dostawcy.
Wyprodukuje kod, który działa,
wygląda rozsądnie
i przechodzi testy, które sama napisała.

<!-- S33 -->
Właśnie to czyni ją użyteczną.
I właśnie to czyni ją niebezpieczną.
Bo wiarygodny domysł
to nie decyzja biznesowa.

<!-- S34 -->
Kiedyś luki były błędami.

<!-- S35 -->
Teraz są decyzjami,
o których podjęciu nikt nie wiedział.

<!-- S36 -->
Jeśli więc specyfikacja naprawdę
ma stać się kodem źródłowym,
nie może być paroma luźnymi akapitami.

<!-- S37 -->
Wyobraź sobie repozytorium.
Jeden dokument opisuje zamówienia
i wszystkie stany, w jakich mogą być.
Inny mówi, kto może je zatwierdzać
i kto może je anulować.

<!-- S38 -->
Trzeci mówi, kiedy wystawia się fakturę
i kiedy trzeba ją wystornować.
Kolejny opisuje system księgowy,
łącznie z tym, co się dzieje, gdy nie działa.

<!-- S39 -->
Część z tego to zwykły tekst.
Ale wszędzie tam, gdzie tekst byłby niejednoznaczny,
jest coś ściślejszego:
lista stanów i przejść między nimi,
schemat, reguła, którą maszyna może sprawdzić.

<!-- S40 -->
A obok testy akceptacyjne,
które mówią dokładnie, co musi się stać.

<!-- S41 -->
Wszystko to leży w Gicie.
Zmiany przechodzą przegląd.
Każde wymaganie da się powiązać
z testem, który je sprawdza.

<!-- S42 -->
Jak więc wygląda zmiana?
Powiedzmy, że klient decyduje,
że wysłane zamówienie wciąż można anulować,
dopóki nie zostało doręczone.
I wtedy trzeba wystornować fakturę.

<!-- S43 -->
Nikt nie otwiera backendu.
Programista zmienia jedną regułę
w dokumencie o zamówieniach.

<!-- S44 -->
Potem system wyszukuje
wszystko, czego ta reguła dotyczy.
Stany zamówienia.
Reguły dotyczące faktur.
Testy anulowania.
Rezerwację u dostawcy.

<!-- S45 -->
I tu powinien się zatrzymać i zapytać.
Specyfikacja nigdy nie mówiła,
co dzieje się z rezerwacją u dostawcy,
gdy towar jest już w drodze.
To jest decyzja,
więc wraca do człowieka.

<!-- S46 -->
Dopiero wtedy generowana jest
nowa implementacja.
I jest sprawdzana w obie strony.
Testy nowej reguły powinny przejść.
A wszystkie pozostałe testy powinny dalej przechodzić,
bez zmian.

<!-- S47 -->
Bo zmiana zasad anulowania
nie może po cichu zmienić niczego innego.
Choć zaliczone testy pokazują tylko
to, co testy sprawdzają.

<!-- S48 -->
A ponieważ reguły
nie są związane z technologią,
ta sama specyfikacja mogłaby dać
dziś aplikację w PHP,
a jutro coś zupełnie innego.

<!-- S49 -->
Czyli dokładnie to, co
Model Driven Architecture obiecywała
dwadzieścia pięć lat temu.
Różnica polega na tym, że tym razem
generator może być wystarczająco dobry.

<!-- S50 -->
Zostaje najtrudniejsze pytanie.
Skąd wiesz, że AI
naprawdę trzymała się specyfikacji?

<!-- S51 -->
Kod, który działa w zwykłych sytuacjach,
wciąż może zawieść w nietypowych.
A te nietypowe to właśnie
przypadki, których nikomu nie przyjdzie do głowy przetestować.

<!-- S52 -->
Amazon zetknął się z tym
we własnych systemach chmurowych.
W 2014 roku jego inżynierowie opisali,
jak zaczęli pisać
precyzyjne, matematyczne opisy
swoich projektów,
w języku o nazwie TLA+.

<!-- S53 -->
Nie kodu. Samego projektu.
Narzędzie brało potem model systemu,
ograniczony do stałego rozmiaru,
i sprawdzało każdą możliwą kolejność
awarii i powrotów do działania.

<!-- S54 -->
W DynamoDB, usłudze bazodanowej Amazona,
znalazło błąd, który mógł prowadzić do utraty danych.

<!-- S55 -->
Najkrótszy sposób, by go wywołać,
wymagał 35 kroków,
dokładnie we właściwej kolejności.
Błąd przeszedł przeglądy projektu,
przeglądy kodu i testy.

<!-- S56 -->
Uczciwa wersja tego pomysłu
nie brzmi więc: AI pisze kod,
a my jej ufamy.
Brzmi: AI pisze kod,
a coś niezależnego go sprawdza.

<!-- S57 -->
A teraz spójrz, co zbudowaliśmy.

<!-- S58 -->
Precyzyjne stany.
Formalne reguły.
Sprawdzalne testy.
Wersjonowane, przejrzane, trzymane w repozytorium.

<!-- S59 -->
To nie wygląda
na koniec programowania.
To wygląda na programowanie
w nowym języku.

<!-- S60 -->
I tak działo się za każdym razem.
FORTRAN był automatycznym kodowaniem,
dopóki nie stał się kodem.
Za każdym razem, gdy maszyna przejmowała
„jak”, ludzie przesuwali się wyżej, do „co”.

<!-- S61 -->
A to „co” zawsze było tą trudną częścią.
Nie pisanie, tylko decydowanie.
Co dzieje się z wysłanym zamówieniem.
Kto może ruszać które dane.
Czego system nie może zrobić nigdy.

<!-- S62 -->
Może programista przyszłości
nie będzie pisał tysięcy linii kodu.

<!-- S63 -->
Ale ktoś nadal będzie musiał zrozumieć
problem na tyle dobrze, by powiedzieć,
co dokładnie komputer ma zrobić,
i sprawdzić, czy to zrobił.

<!-- S64 -->
A jeśli specyfikacja
stanie się kodem źródłowym,
najważniejszą umiejętnością
może już nie być wiedza,
jak napisać program.

<!-- S65 -->
Może nią być wiedza,
jak go opisać.

<!-- S66 -->
Oto więc pytanie,
na które chętnie poznam twoją odpowiedź.
Jeśli napiszesz specyfikację
tak precyzyjną,
żeby maszyna mogła na jej podstawie zbudować program...
czy nadal programujesz?
