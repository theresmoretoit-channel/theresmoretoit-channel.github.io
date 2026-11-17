# Jak ARM podbił świat komputerów?

<!-- S01 -->
W 1985 roku inżynierowie w Wielkiej Brytanii
włączyli zupełnie nowy procesor
po raz pierwszy.

<!-- S02 -->
Zadziałał.
Co samo w sobie było małym cudem.

<!-- S03 -->
Ale potem zauważyli coś dziwnego.
Zasilanie układu
nie było podłączone.

<!-- S04 -->
A mimo to działał.

<!-- S05 -->
Radził sobie dzięki maleńkim prądom,
które przeciekały przez jego piny wejściowe
z sygnałów sąsiednich układów.

<!-- S06 -->
Kiedy porządnie zmierzyli pobór prądu,
okazało się, że procesor potrzebuje
około jednej dziesiątej wata.

<!-- S07 -->
Nikt tego nie planował.
Inżynierowie chcieli po prostu układu,
który będzie tani w produkcji.

<!-- S08 -->
Ten układ był pierwszym procesorem ARM.

<!-- S09 -->
Czterdzieści lat później jego potomkowie
są w prawie każdym smartfonie.
W komputerach Apple.
W niektórych z największych centrów danych
na świecie.

<!-- S10 -->
Setki miliardów układów.

<!-- S11 -->
Jak więc procesor
z brytyjskiej firmy od komputerów domowych
podbił świat komputerów?

<!-- S12 -->
Odpowiedź nie brzmi po prostu,
że zużywał bardzo mało energii.
To akurat wyszło prawie przypadkiem.

<!-- S12b -->
Przy okazji, jeśli lubisz takie
filmy, możesz zasubskrybować kanał.

To naprawdę pomaga kanałowi.

<!-- S13 -->
Żeby zrozumieć, co naprawdę się stało,
musimy cofnąć się do 1983 roku.

<!-- S14 -->
Ta firma nazywała się Acorn Computers.
Jej BBC Micro stał w klasach
w całej Wielkiej Brytanii.

<!-- S15 -->
BBC Micro działał na starszym,
ośmiobitowym układzie 6502.
Do swojej następnej maszyny
Acorn potrzebował czegoś znacznie szybszego.

<!-- S16 -->
Zespół przetestował więc
nowe procesory dostępne na rynku.
Żaden nie robił tego, czego chciał Acorn.

<!-- S17 -->
Były skomplikowane
i żaden tak naprawdę nie pasował
do tego, co Acorn chciał zbudować.

<!-- S18 -->
Wtedy dwoje inżynierów Acorna,
Sophie Wilson i Steve Furber,
pojechało do Arizony,
do firmy założonej przez jednego
z pierwotnych projektantów 6502.

<!-- S19 -->
Spodziewali się dużej firmy od układów.
Zamiast tego zastali garstkę ludzi
pracujących w domu na przedmieściach.

<!-- S20 -->
I wrócili do domu
z prostym wnioskiem.
Skoro oni potrafią zaprojektować procesor...
to my też.

<!-- S22 -->
W tamtych czasach procesory dostawały
coraz bardziej rozbudowane instrukcje.

<!-- S23 -->
Jedna instrukcja potrafiła pobrać
liczbę z pamięci,
wykonać na niej obliczenie
i zapisać wynik z powrotem.

<!-- S24 -->
Wygodne dla programisty.
Ale każda taka instrukcja
utrudnia zbudowanie układu.

<!-- S25 -->
Potrzeba więcej logiki
tylko po to, żeby ustalić, co każda z nich znaczy.
Więcej tranzystorów.
Więcej czasu na projektowanie.

<!-- S26 -->
Badacze z Berkeley i Stanfordu
zadali sobie radykalne pytanie.

<!-- S27 -->
A gdyby procesor
miał tylko proste instrukcje,
a resztą zajmował się kompilator?

<!-- S28 -->
Nazwali to RISC.
Komputer o zredukowanej liście rozkazów.

<!-- S29 -->
Sophie Wilson zaprojektowała
instrukcje ARM właśnie w tym duchu.

<!-- S30 -->
Arytmetyka działa wyłącznie
na własnych rejestrach układu,
małych, szybkich schowkach w procesorze.
Do pracy z pamięcią są osobne instrukcje.

<!-- S31 -->
Dodanie liczby z pamięci
to więc trzy kroki.
Wczytaj.
Dodaj.
Zapisz.

<!-- S32 -->
Nazywa się to architekturą load-store.

<!-- S33 -->
Więcej kroków dla programu.
Ale każdy krok jest regularny,
przewidywalny
i łatwy do zdekodowania.

<!-- S34 -->
A ARM miał mnóstwo rejestrów
do dyspozycji.
Szesnaście, każdy 32-bitowy.
6502 miał trzy małe.

<!-- S35 -->
Efektem był ARM1.

<!-- S36 -->
Miał około
25 000 tranzystorów.

<!-- S37 -->
Intel 286, wprowadzony kilka lat wcześniej,
miał ich około 134 000.

<!-- S38 -->
Mniej tranzystorów oznaczało mniejszy układ.
Tańszy układ.

<!-- S39 -->
I, prawie jako efekt uboczny,
układ, który niemal nie pobierał prądu.

<!-- S40 -->
Stąd właśnie wzięła się
ta jedna dziesiąta wata.
Acorn chciał taniej plastikowej obudowy,
a to oznaczało zmieszczenie się poniżej jednego wata.
Projektowali więc ostrożnie...
i wylądowali dziesięć razy niżej.

<!-- S41 -->
W 1987 roku szybsza wersja ARM
trafiła do nowego komputera Acorna,
Archimedesa.

<!-- S42 -->
Był to jeden z najszybszych
komputerów osobistych swoich czasów.

<!-- S43 -->
I prawie nie miało to znaczenia.

<!-- S44 -->
Świat kupował pecety zgodne z IBM
z procesorami Intela.
Tam było oprogramowanie.
To kupowały firmy.

<!-- S45 -->
Archimedes został
głównie w brytyjskich szkołach.

<!-- S46 -->
A sam Acorn miał kłopoty.
Już w 1985 roku
musiała go ratować firma Olivetti.

<!-- S48 -->
Wtedy pomoc przyszła od Apple.
Firma budowała komputer kieszonkowy
o nazwie Newton.

<!-- S49 -->
Potrzebowała procesora,
który będzie szybki, tani
i da radę działać na bateriach.

<!-- S50 -->
ARM pasował idealnie.
Ale Apple nie chciało być zależne
od układu, który należy
do konkurencyjnego producenta komputerów.

<!-- S51 -->
Dlatego w 1990 roku zespół ARM
wydzielono z Acorna
jako osobną firmę.

<!-- S52 -->
Acorn, Apple
i producent układów VLSI
byli jej wspólnymi właścicielami.

<!-- S53 -->
Dwunastu inżynierów.
Stara stodoła pod Cambridge.

<!-- S54 -->
I model biznesowy,
który okazał się prawdziwym sekretem sukcesu.

<!-- S55 -->
Intel projektował swoje procesory,
produkował je we własnych fabrykach
i sprzedawał.

<!-- S56 -->
ARM nie miał produkować niczego.
Miał sprzedawać projekt.

<!-- S57 -->
Każda firma mogła kupić licencję,
wbudować rdzeń ARM we własny układ
i płacić niewielką opłatę
od każdego sprzedanego układu.

<!-- S58 -->
To było ważne,
bo układ nie musi być
tylko procesorem.
Wokół rdzenia ARM
możesz umieścić moduł radiowy,
układ graficzny,
procesor obrazu z aparatu.

<!-- S59 -->
Jeden układ,
zaprojektowany przez tego, kto go potrzebuje,
z ARM w samym środku.

<!-- S60 -->
ARM nie musiał pokonać Intela
w komputerach osobistych.
Mógł trafić do środka czegokolwiek.

<!-- S61 -->
A w latach 90.
„cokolwiek” coraz częściej oznaczało
telefony komórkowe.

<!-- S62 -->
Komputer stacjonarny może sobie pozwolić
na sto watów i duży wentylator.
Telefon działa na baterii
w twojej kieszeni.

<!-- S63 -->
Pod koniec dekady
rdzenie ARM siedziały
w niektórych z najlepiej sprzedających się telefonów,
od Nokii i innych.

<!-- S64 -->
Potem przyszedł iPod.
Potem smartfon.

<!-- S65 -->
Miliardy ludzi nagle nosiły przy sobie
komputer, który musiał wytrzymać
cały dzień na baterii.

<!-- S66 -->
I procesor, który powstał dlatego,
że był tani,
okazał się dokładnie tym,
czego ten świat potrzebował.

<!-- S67 -->
Więc to jest nasza odpowiedź, prawda?
ARM jest prosty,
prosty znaczy efektywny,
a efektywny wygrywa.

<!-- S68 -->
Niezupełnie.

<!-- S69 -->
Zajrzyj do nowoczesnego rdzenia ARM z najwyższej półki.

<!-- S70 -->
Ogromne pamięci podręczne.
Kilka instrukcji wykonywanych naraz.
Przewidywanie rozgałęzień,
czyli zgadywanie, dokąd pójdzie program,
zanim tam dotrze.

<!-- S71 -->
Wykonywanie poza kolejnością,
czyli wykonywanie instrukcji
w takiej kolejności, jaka jest najszybsza.

<!-- S72 -->
Miliardy tranzystorów w układzie.
Nie ma w tym nic prostego.

<!-- S73 -->
Gdzie więc podziała się prostota?

<!-- S74 -->
Sztuczka polega na tym, że procesor
to tak naprawdę dwie różne rzeczy.

<!-- S75 -->
Lista rozkazów to język,
którym mówi oprogramowanie.
Jakie instrukcje istnieją
i co znaczą.

<!-- S76 -->
Mikroarchitektura to maszyna,
która faktycznie je wykonuje.

<!-- S77 -->
Język może pozostać prosty,
podczas gdy maszyna pod spodem
staje się niesamowicie skomplikowana.

<!-- S78 -->
I to samo stało się
po drugiej stronie.

<!-- S79 -->
Instrukcje x86 Intela
słyną z tego, że są skomplikowane.

<!-- S80 -->
Ale od połowy lat 90.
procesory Intela i AMD
rozbijają je wewnętrznie
na małe, proste operacje.

<!-- S81 -->
A potem wykonują je w mechanizmie
bardzo podobnym do tego
w nowoczesnym rdzeniu ARM.

<!-- S82 -->
Pod różnymi etykietami
obie konstrukcje stały się zaskakująco podobne.

<!-- S83 -->
Bardziej uporządkowane instrukcje ARM nadal pomagają.
Łatwiej je zdekodować,
co może zaoszczędzić trochę energii.

<!-- S84 -->
Ale to nie jest magiczna przewaga,
której x86 nigdy nie zdołałby nadrobić.

<!-- S85 -->
ARM nie wygrał więc dlatego,
że był prosty.
I nie projektowano go z myślą o niskim poborze mocy.

<!-- S86 -->
Wygrał, bo zbiegły się trzy rzeczy.
Efektywny projekt.
Model biznesowy,
który pozwalał każdemu budować na ARM.
I świat, który nagle potrzebował
miliardów komputerów na baterie.

<!-- S87 -->
A potem, w 2020 roku,
historia wróciła do Apple.

<!-- S88 -->
Apple sprzedało swoje udziały w ARM
wiele lat wcześniej,
kiedy pilnie potrzebowało pieniędzy.

<!-- S89 -->
Teraz włożyło własne układy oparte na ARM
do Maca.

<!-- S90 -->
Ten sam rodzaj rdzeni co w iPhonie,
tylko powiększony na potrzeby komputera.
Szybkie rdzenie, energooszczędne rdzenie,
grafika i wiele więcej,
w jednym układzie.

<!-- S91 -->
Były szybsze
od układów Intela, które zastąpiły,
a laptopy działały dużo dłużej
na jednym ładowaniu.

<!-- S92 -->
ARM nie był już
tylko procesorem do telefonów.

<!-- S93 -->
I ARM się na tym nie zatrzymał.
Wszedł też do centrów danych,
gdzie każdy wat kosztuje.
Amazon projektuje dziś
własne serwerowe układy ARM.

<!-- S95 -->
Pierwszy układ ARM miał około
25 000 tranzystorów.
Dzisiejsze mają ich miliardy.

<!-- S96 -->
Prawie wszystko w tym,
jak działają w środku, się zmieniło.

<!-- S98 -->
Mały zespół chciał
procesora, który naprawdę da radę zbudować.

<!-- S99 -->
Nie budowali go z myślą o telefonach,
o Apple
ani o tym, żeby pokonać Intela.

<!-- S100 -->
I w końcu
najważniejszą rzeczą, jaką stworzyli,
nie był układ.

<!-- S101 -->
Była nią prosta podstawa,
na której mogli budować wszyscy inni.
