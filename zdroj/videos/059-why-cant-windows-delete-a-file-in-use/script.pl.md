<!-- S01 -->
Próbujesz usunąć plik.
Komputer mówi, że jest otwarty
w innym programie.
Ale nie mówi, w którym.

<!-- S02 -->
Ten komunikat to widoczny koniec
o wiele dziwniejszego pytania.
Co właściwie znaczy
otworzyć plik?

<!-- S03 -->
Bo na innym komputerze
ten sam plik, otwarty tak samo,
usuwa się bez słowa skargi.

<!-- S04 -->
Ten sam plik.
To samo działanie.
Dwie zupełnie różne odpowiedzi.

<!-- S05 -->
Zacznijmy od tego,
co irytuje wszystkich.
Który program?

<!-- S06 -->
Windows to wie.
Ma obiekt jądra
dla tego otwartego pliku
i wie, który proces jest właścicielem.
Mógłby podać nazwę.

<!-- S07 -->
Więc zamykasz rzeczy na chybił trafił.
Otwierasz Menedżera zadań.
Wpatrujesz się w listę procesów
i prawie żadnego nie poznajesz.

<!-- S08 -->
I przez lata
odpowiedzią naprawdę było
pobranie osobnego narzędzia.
Unlocker wyszedł w 2005,
a na Windows XP to była odpowiedź.

<!-- S09 -->
Potem Windows 7 przyniósł
Monitor zasobów.
Kartę Procesor.
Listę o nazwie Skojarzone dojścia.

<!-- S10 -->
Wpisz nazwę pliku.
Dostajesz program
i identyfikator procesu.
Nic do instalowania.
Jest tam od 2009 roku.

<!-- S10b -->
Ale osobne narzędzia robiły
więcej niż samo wskazanie winowajcy.
Potrafiły zamknąć dojście
i uwolnić plik.

<!-- S11 -->
Co sprowadza nas z powrotem
do pytania.
Co ten program dostał,
kiedy otworzył plik?

<!-- S12 -->
Powiedzmy, że odtwarzacz otwiera
plik o nazwie movie.mp4.
W Windows otworzyć plik
znaczy wypełnić dwie rzeczy.

<!-- S13 -->
Pierwsza jest oczywista.
Co chcę z nim zrobić?
Czytać go. Pisać do niego.

<!-- S14 -->
Druga jest tą ciekawą.
Co wolno wszystkim innym,
dopóki trzymam go otwartego?

<!-- S15 -->
To prawdziwe ustawienie.
Mówisz w nim, co wolno innym
programom, dopóki go trzymasz.

<!-- S16 -->
Mogą go czytać.
Mogą też do niego pisać.
Mogą go usunąć albo zmienić nazwę.

<!-- S16b -->
Albo zupełnie nic.
Nikt go nie dotknie,
dopóki go używam.

<!-- S17 -->
Flaga, która pozwala usuwać,
nazywa się FILE_SHARE_DELETE.
A dokumentacja Microsoftu
dodaje pod nią jedną linijkę.

<!-- S18 -->
Prawo do usuwania obejmuje
usuwanie i zmianę nazwy razem.

<!-- S19 -->
Więc program, który odmawia
współdzielenia do usuwania,
zablokował też zmianę nazwy.

<!-- S20 -->
A jeśli program, który otworzył plik,
tego nie przyznał,
nikt inny tego nie weźmie.

<!-- S21 -->
Dlatego ten błąd
nie nazywa się plik zajęty.
Nazywa się naruszenie udostępniania.

<!-- S22 -->
Odpowiedź przez cały czas
siedziała w nazwie
samego błędu.

<!-- S23 -->
Teraz to samo
na maszynie z Linuksem.
Odtwarzacz otwiera wideo.

<!-- S24 -->
A ty wpisujesz
rm movie.mp4.

<!-- S24b -->
Działa.
Wideo nadal się odtwarza.

<!-- S25 -->
Co więc dostał ten program,
jeśli nie kontrolę nad plikiem?

<!-- S26 -->
To jest cała myśl
tego filmu.
Nazwa to nie plik.

<!-- S27 -->
movie.mp4 to wpis
w katalogu.
Ten wpis wskazuje na obiekt,
w którym są właściwe dane.

<!-- S28 -->
Kiedy program otwiera plik,
to, co dostaje, jest odwołaniem
do obiektu.
Nie do wpisu.

<!-- S29 -->
Usunięcie pliku
kasuje więc wpis.
Obiekt pozostaje nietknięty.

<!-- S30 -->
Podręcznik systemowy mówi to
w jednym zdaniu.
Plik będzie istniał dalej,
dopóki nie zamknie się ostatni
deskryptor, który się do niego odwołuje.

<!-- S31 -->
Brzmi to abstrakcyjnie,
dopóki się tego nie zobaczy.
Zrobiłem więc plik dziennika
o wielkości pięciuset megabajtów
i zostawiłem proces z nim otwartym.

<!-- S31b -->
Potem go usunąłem.

<!-- S32 -->
Wypis katalogu
nie pokazuje zupełnie nic.
Narzędzie, które mierzy
rozmiar folderu, mówi zero.

<!-- S33 -->
A narzędzie, które mierzy
wolne miejsce na dysku,
mówi, że pięćset megabajtów
wciąż brakuje.

<!-- S33b -->
Pusty folder.
Pół gigabajta zniknęło.

<!-- S34 -->
Zdarza się to na tyle często,
że istnieje osobne polecenie
tylko do znajdowania takich plików.
Usuniętych, niewidocznych, wciąż na dysku.

<!-- S35 -->
A miejsce wraca
w chwili, gdy ten jeden proces
puszcza plik.

<!-- S36 -->
Ta sama logika dotyczy zmiany nazwy.
Przenieś plik, gdy jest otwarty,
a program niczego nie zauważy.

<!-- S37 -->
Podręcznik jest tam równie jasny.
Otwarte deskryptory powiązane
ze starą ścieżką pozostają bez zmian.

<!-- S37b -->
Nigdy nie używał tej nazwy.

<!-- S38 -->
Co ma jedno ograniczenie,
które warto znać.
Działającego programu
nie da się nadpisać w miejscu.

<!-- S38b -->
Linux odmawia.
Text file busy.

<!-- S39 -->
To, co można zrobić,
to odłączyć nazwę
i położyć tam nowy plik.

<!-- S40 -->
Stary proces działa dalej
z obiektu,
który nie ma już żadnej nazwy.
Każdy proces uruchomiony później dostaje nowy.

<!-- S41 -->
To znów ta sama myśl —
i sama się potwierdza.
Wiele rzeczy da się wymienić,
nie dotykając obiektu w miejscu.

<!-- S41b -->
Dlatego Linux potrafi zaktualizować
program w trakcie działania.
Nowej wersji po prostu nie masz,
dopóki go nie uruchomisz ponownie.

<!-- S42 -->
Czy Windows jest więc
po prostu gorzej zaprojektowany?

<!-- S42b -->
Nie.
I to jest ta część,
którą prawie nikt nie zna.

<!-- S43 -->
Windows ma sposób,
żeby zrobić dokładnie to samo.

<!-- S43b -->
Na NTFS Windows może poprosić
o usunięcie w stylu POSIX.

<!-- S44 -->
Microsoft opisuje,
co się wtedy dzieje.
Nazwa znika
z widocznej przestrzeni nazw.

<!-- S45 -->
A aplikacje, które już miały
plik otwarty, mogą go dalej używać,
mimo że nazwa,
którą go otworzyły, zniknęła.

<!-- S46 -->
To jest zachowanie Uniksa.
Na NTFS.
Udokumentowane przez Microsoft.

<!-- S47 -->
Oba systemy potrafią jedno i drugie.
Różni je ustawienie domyślne.
To, co dostajesz, otwierając plik
i w ogóle o tym nie myśląc.

<!-- S48 -->
W Windows dostajesz umowę.
W Uniksie dostajesz odwołanie
do obiektu.

<!-- S49 -->
Co brzmi jak pytanie
dla programistów,
dopóki nie zobaczy się
właśnie tego komunikatu.

<!-- S50 -->
Uruchom komputer ponownie,
aby dokończyć instalowanie aktualizacji.

<!-- S51 -->
Załóżmy, że Windows ma wymienić
bibliotekę, którą działający proces
ma otwartą na ścisłej umowie.

<!-- S52 -->
Nie może podmienić pliku
pod tym procesem.
Więc coś musi puścić.

<!-- S53 -->
Zamknąć aplikację.
Zatrzymać usługę.
Albo oddać całą robotę
Menedżerowi ponownego uruchamiania.

<!-- S54 -->
Który jest prawdziwym składnikiem.
Zamyka je po kolei.
Aplikacje Windows,
potem programy konsolowe,

<!-- S55 -->
potem usługi,
a Eksploratora na końcu.
Potem uruchamia je z powrotem.

<!-- S56 -->
I istnieje z jednego powodu,
który Microsoft mówi wprost
we własnej dokumentacji.

<!-- S57 -->
Głównym powodem,
dla którego instalacje
i aktualizacje wymagają
ponownego uruchomienia systemu...

<!-- S58 -->
jest to, że część aktualizowanych
plików jest właśnie używana
przez działającą aplikację
albo usługę.

<!-- S59 -->
Byłoby zbyt zgrabnie skończyć tutaj.
Reguły współdzielenia to nie jedyny powód,
dla którego komputer prosi o restart.

<!-- S60 -->
Aktualizacja jądra to co innego.
Nie da się wymienić jądra,
kiedy samo działa.

<!-- S61 -->
Linux ma ten sam problem,
choć łatanie na żywo
czasem pozwala uniknąć restartu.

<!-- S62 -->
Uczciwa wersja obiecuje
więc mniej niż
ta satysfakcjonująca.

<!-- S63 -->
To, jak Windows traktuje pliki
w użyciu, utrudniło wymianę
niektórych składników podczas działania,
i to się do tego przyczyniło.

<!-- S64 -->
Bo każdy wybór projektowy
ma gdzieś swoje konsekwencje.

<!-- S65 -->
Windows pozwala programowi,
który otwiera plik, zdecydować,
co inni mogą z nim zrobić.

<!-- S66 -->
Ceną jest to, że czasem
nie usuniesz własnego pliku,
bo inny program
na to nie pozwolił.

<!-- S67 -->
Uniks trzyma nazwę
i obiekt osobno,
więc wiele da się wymienić
gdy system działa.

<!-- S68 -->
Ceną jest pół gigabajta,
które zniknęło z dysku
i nie należy do żadnego pliku.

<!-- S69 -->
I zobacz, jak rozwiązuje się
każdy z tych dwóch problemów.
W Windows jednym wyjściem jest
zamknąć program,
który trzyma plik.

<!-- S70 -->
W Linuksie jednym sposobem
na odzyskanie tego miejsca
jest zrestartować usługę,
która wciąż ma go otwarty.

<!-- S71 -->
Różne przyczyny.
Czasem to samo lekarstwo.

<!-- S71b -->
Swoją drogą, jeśli chcesz zobaczyć,
dokąd zaprowadzi nas kolejne pytanie,
rozważ subskrypcję.
Bardzo pomaga kanałowi.

<!-- S72 -->
No więc. Pytanie z początku.
Co znaczy
otworzyć plik?

<!-- S73 -->
Znaczy, że coś trzymasz.
Te dwa systemy po prostu wkładają
ci w rękę co innego.

<!-- S74 -->
Dlatego ten komunikat
nigdy naprawdę nie powiedział,
że pliku nie da się usunąć.

<!-- S75 -->
Powiedział, że program,
który go otworzył,
nie dał ci na to zgody.

<!-- S75b -->
I wie, który to program.
Po prostu o tym nie wspomniał.
