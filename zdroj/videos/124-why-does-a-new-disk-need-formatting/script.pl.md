<!-- S01 -->
Kupujesz nowiutki dysk.
Jeden terabajt, zupełnie pusty.
Zanim zapiszesz na nim choćby jeden plik,
najpierw trzeba go sformatować.

<!-- S02 -->
Więc formatujesz go na ext4,
standardowy system plików
w wielu komputerach z Linuksem.
Przy ustawieniach domyślnych,
zanim w ogóle cokolwiek zapiszesz,
znika około siedemnastu gigabajtów.

<!-- S03 -->
Nic jeszcze nie zostało zapisane.
Żadnych zdjęć, żadnych dokumentów.
Więc co zajmuje całe to miejsce?

<!-- S04 -->
I po co w ogóle dysk
trzeba formatować?
Przecież już potrafi przechowywać dane.
Potrafi czytać i zapisywać biliony bitów.

<!-- S05 -->
Dlaczego komputer nie może po prostu zapisywać
tam, gdzie akurat jest miejsce?

<!-- S06 -->
Bo zapisać dane
i potem znowu je znaleźć
to dwa zupełnie różne problemy.

<!-- S07 -->
Wyobraź sobie urząd, który zamiast formularzy
rozdaje czyste kartki.
Wszystko jest gdzieś zapisane...
i nikt niczego nie może znaleźć.

<!-- S08 -->
Dysk bez systemu plików
to właśnie ta sterta papieru.
Lepszym porównaniem
jest jednak zeszyt.

<!-- S09 -->
Wyobraź sobie zeszyt
z tysiącem stron
i kilkoma zasadami, jak go używać.

<!-- S10 -->
Po pierwsze: każda strona ma numer.
Teraz każde miejsce w zeszycie
ma adres.
Strona czterysta dwanaście
oznacza dokładnie jedno miejsce.

<!-- S11 -->
Po drugie: kilka pierwszych stron
to spis treści.
Każda pozycja ma nazwę
i stronę, na której się znajduje.
Naleśniki: strona dwanaście.

<!-- S12 -->
Po trzecie: na samym końcu
jest lista stron,
które są jeszcze puste.

<!-- S13 -->
Teraz dodaj przepis.
Szukasz z tyłu pustej strony.
Zapisujesz na niej przepis.
Dopisujesz linijkę do spisu treści.
I skreślasz tę stronę
z listy pustych.

<!-- S14 -->
Jeden przepis, trzy miejsca.
I wszystkie trzy muszą się zgadzać.

<!-- S15 -->
Potem przepis na naleśniki się rozrasta.
Strona dwanaście jest pełna,
a trzynasta jest już zajęta.
Więc ciąg dalszy: strona osiemdziesiąt siedem,
i spis treści musi to podawać.

<!-- S16 -->
I tu jest haczyk.
Jeśli chcesz mieć miejsce na tysiąc pozycji
w spisie treści,
musisz zarezerwować te strony,
zanim zapiszesz choćby jeden przepis.

<!-- S17 -->
Tyle analogii.
A teraz to, co naprawdę jest na dysku.

<!-- S18 -->
Dysk nie wie nic o plikach,
folderach ani nazwach.
Oferuje tylko długi rząd
ponumerowanych miejsc, zwanych sektorami.

<!-- S19 -->
Na dysku twardym
dane leżą na wirujących talerzach.
SSD trzyma je w pamięci flash.
Tak czy inaczej, komputer prosi tylko
o sektor o danym numerze,
a dysk sam ustala, gdzie on jest.

<!-- S20 -->
Sektor jest mały.
Zwykle 512 bajtów,
albo 4096
w nowszych dyskach.

<!-- S21 -->
Systemy plików zwykle pracują
na większych kawałkach, zwanych blokami.
W ext4 blok ma cztery kilobajty,
czyli tyle, co osiem sektorów starego typu.

<!-- S22 -->
Te ponumerowane bloki
to strony zeszytu.
Systemowi plików brakuje jeszcze
pozostałych dwóch części:
spisu treści
i listy tego, co wolne.

<!-- S23 -->
To właśnie tworzy formatowanie.
I właśnie tam
poszło tych siedemnaście gigabajtów.

<!-- S24 -->
Ext4 rezerwuje rekord
dla każdego pliku i folderu,
jakie dysk będzie mógł pomieścić naraz.
Każdy rekord ma
256 bajtów.
To tak zwany i-węzeł.

<!-- S25 -->
Kiedyś każdy i-węzeł będzie mówił,
jak duży jest plik,
kiedy został zmieniony,
kto może go otworzyć
i w których blokach jest jego zawartość.

<!-- S26 -->
Na terabajtowym dysku
ext4 przygotowuje około
sześćdziesięciu jeden milionów i-węzłów.
Wszystkie puste, wszystkie czekają.
To prawie szesnaście gigabajtów
pustych rekordów.

<!-- S27 -->
Dlaczego sześćdziesiąt jeden milionów?
Ext4 przyjmuje proste założenie:
jeden i-węzeł na każde szesnaście kilobajtów
miejsca na dysku.
Na typowym komputerze
większość tych rekordów
nigdy nie zostanie użyta.

<!-- S28 -->
Mniej więcej kolejny gigabajt
idzie na dziennik,
do którego jeszcze wrócimy.
Reszta to pozostała ewidencja,
w tym mapa z jednym bitem na blok,
który mówi, czy blok jest zajęty, czy wolny.

<!-- S29 -->
Ta liczba też jest stała.
Zużyj wszystkie rekordy
milionami malutkich plików,
a dysk powie ci, że jest pełny...
mimo że zostały na nim gigabajty miejsca.

<!-- S30 -->
Zobaczmy więc, jak to działa.
Utworzymy plik o nazwie hello.txt.
W środku tylko jedno słowo: hello.
Pięć liter. Pięć bajtów.

<!-- S31 -->
System plików wybiera pusty i-węzeł.
Powiedzmy, numer trzynaście.
Potem znajduje w mapie wolny blok
i oznacza go jako zajęty.

<!-- S32 -->
Zapisuje te pięć bajtów w tym bloku.
Potem wypełnia i-węzeł:
długość pięć bajtów, utworzony przed chwilą,
zapisany w tym jednym bloku.

<!-- S33 -->
I na koniec w folderze
dodaje jedną linijkę:
nazwę hello.txt
i numer trzynaście.

<!-- S34 -->
Zauważ, gdzie trafiła nazwa.
Nie do pliku.
Nie do i-węzła.
Nazwa mieszka w folderze,
który tak naprawdę jest tylko listą
nazw i numerów.

<!-- S35 -->
A folder to po prostu kolejny plik.
Akurat jego zawartością
jest ta lista.

<!-- S36 -->
Dlatego też przeniesienie pliku
do innego folderu w tym samym systemie plików
odbywa się natychmiast, bez względu na rozmiar.
Jeden folder traci linijkę,
drugi ją zyskuje,
a sama zawartość
zwykle wcale się nie rusza.

<!-- S37 -->
Pięć bajtów tekstu...
a na dysku zajmuje
4096.
Blok to najmniejszy kawałek,
jaki przydziela system plików,
więc nawet malutki plik zajmuje cały blok.

<!-- S38 -->
Kiedy plik przerośnie swój blok,
system plików znajduje kolejny wolny.
Może tuż obok.
Może zupełnie gdzie indziej.
A i-węzeł pamięta oba.

<!-- S39 -->
Z czasem duży plik może skończyć
w kawałkach rozrzuconych po całym dysku.
Dysk twardy musi między nimi skakać.
SSD radzi sobie z tym dużo lepiej.

<!-- S40 -->
Program, który zapisał plik,
nic o tym nie wie.
Powiedział „zapisz hello.txt”,
a cała reszta działa się w tle.

<!-- S41 -->
Teraz go usuń.
Nazwa znika z folderu.
I-węzeł zostaje oznaczony jako wolny.
Blok wraca na listę wolnych.

<!-- S42 -->
Na tradycyjnym dysku twardym
te pięć bajtów zostaje na swoim miejscu.
Nikt ich nie ruszał.
Zostają tam, dopóki coś nowego
nie zostanie na nich zapisane.

<!-- S43 -->
Dlatego usunięty plik
czasem da się odzyskać.
Usuwanie zwykle nie kasuje
samej zawartości.
Tylko oznacza miejsce jako dostępne.

<!-- S44 -->
Na SSD to mniej pewne.
System plików może powiedzieć dyskowi,
że te bloki nie są już potrzebne,
a dysk może wyrzucić to, co w nich jest.
Potem odzyskanie pliku
jest dużo mniej prawdopodobne.

<!-- S45 -->
Więc system plików to tak naprawdę księgowy.
Utworzenie tego jednego pliku
oznaczało aktualizację trzech rzeczy:
folderu, i-węzła
i mapy wolnych bloków.

<!-- S46 -->
Teraz odetnij prąd
w połowie zapisywania pliku.

<!-- S47 -->
Może blok został już oznaczony jako zajęty,
ale żaden i-węzeł jeszcze na niego nie wskazuje.
To miejsce po prostu przepada.
Irytujące, ale nieszkodliwe.

<!-- S48 -->
A może i-węzeł wskazuje na blok,
który mapa wciąż uznaje za wolny.
Następny plik może zostać zapisany
prosto na nim.
A pierwszy zostaje po cichu zniszczony.

<!-- S49 -->
Dlatego ext4 prowadzi dziennik.
Zanim zmieni swoją ewidencję,
zapisuje, co zamierza zrobić.
Po awarii odtwarza tylko te zmiany,
które zdążył w całości zapisać
i oznaczyć jako zakończone.
Wszystko niedokończone jest pomijane.

<!-- S50 -->
Jest też cichszy problem.
Czasem dysk zmienia bit
i nikomu o tym nie mówi.

<!-- S51 -->
Ext4 chroni swoje własne rekordy
sumami kontrolnymi,
więc tam potrafi wykryć uszkodzenia.
Ale zawartość twoich plików?
Tej po prostu ufa.

<!-- S52 -->
Niektóre systemy plików sprawdzają jedno i drugie.
A niektóre trzymają drugą kopię,
więc gdy jedna kopia jest uszkodzona,
mogą ją naprawić z tej drugiej.
Wykryć problem i go naprawić
to nie to samo.

<!-- S53 -->
Każdy system plików wykonuje więc tę samą pracę:
ponumerowane bloki, lista nazw
i mapa tego, co wolne.

<!-- S54 -->
Ale rozwiązania się różnią.
Ext4 przygotowuje sześćdziesiąt jeden milionów rekordów,
zanim cokolwiek zapiszesz.
NTFS w Windowsie trzyma swoje rekordy
w jednej dużej tabeli, która rośnie w miarę potrzeb.

<!-- S55 -->
A Btrfs nie przygotowuje
z góry stałej tabeli i-węzłów.
Tworzy je, w miarę jak przybywa plików.
I zwykle nie nadpisuje
danych w miejscu.
Zapisuje nową kopię
i dopiero wtedy zwalnia starą.

<!-- S56 -->
Domyślnie liczy też sumy kontrolne twoich plików,
więc potrafi wykryć, że zostały uszkodzone.

<!-- S57 -->
A ponieważ stara kopia
nie zostaje nadpisana,
snapshot może ją zachować przy życiu.
To zmienia odpowiedź
na prawie każde pytanie z tego filmu:
jakie skutki ma awaria,
co znaczy usunięcie
i nawet czym jest kopia.

<!-- S58 -->
Tu zaczyna się następny film.

<!-- S59 -->
Mam więc dla ciebie pytanie.
Czy system plików powinien tylko przechowywać twoje pliki,
czy też je chronić?
Daj znać w komentarzach.
