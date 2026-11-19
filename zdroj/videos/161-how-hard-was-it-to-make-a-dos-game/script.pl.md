<!-- S01 -->
W 1993 roku gra o nazwie Doom
działała na komputerze
z 4 megabajtami pamięci.

<!-- S02 -->
To mniej więcej rozmiar
jednego zdjęcia w twoim telefonie.

<!-- S03 -->
Nie było akceleratora 3D.
Całe renderowanie
wykonywał główny procesor.

<!-- S04 -->
Dziś programista zaczyna od silnika,
takiego jak Unity czy Unreal,
który dba o grafikę, dźwięk,
pamięć i sprzęt.

<!-- S05 -->
W DOS-ie to wszystko
było problemem programisty.
A dość często także gracza.

<!-- S06 -->
Jak trudno było więc
zrobić grę na DOS-a?

<!-- S07 -->
Zacznijmy od pamięci,
bo z pamięcią był bałagan.

<!-- S08 -->
Pierwszy IBM PC z 1981 roku
mógł zaadresować 1 megabajt pamięci.

<!-- S09 -->
Ale tylko pierwsze
640 kilobajtów
było przeznaczone dla programów.

<!-- S10 -->
Pozostałe 384
zarezerwowano na pamięć wideo,
karty rozszerzeń i BIOS.

<!-- S11 -->
Przez ponad dekadę
DOS zwykle uruchamiał programy
w tej przestrzeni.
Wszystko ponad nią wymagało dodatkowej pracy.

<!-- S12 -->
Stąd pochodzi słynne zdanie:
640K powinno wystarczyć każdemu.

<!-- S13 -->
Zwykle przypisuje się je Billowi Gatesowi.
Nie ma żadnego zapisu, że kiedykolwiek to powiedział,
a on temu zaprzecza.

<!-- S14 -->
Na początku lat dziewięćdziesiątych
pecet miał 4 megabajty
albo 8.

<!-- S15 -->
A gra i tak mogła się zatrzymać
z komunikatem
„za mało pamięci”.

<!-- S16 -->
Mieć pamięć
i móc z niej skorzystać
to były dwie różne rzeczy.

<!-- S17 -->
Jednym obejściem była pamięć ekspandowana,
czyli EMS.

<!-- S18 -->
Okno o rozmiarze 64 kilobajtów
znajdowało się w górnej części
tego pierwszego megabajta.
Przez nie program widział
4 strony dodatkowej pamięci,
po 16 kilobajtów każda,

<!-- S19 -->
i mógł je zamieniać na inne,
jak przewracanie stron książki
przez dziurę w kartce papieru.

<!-- S20 -->
Innym sposobem była pamięć rozszerzona,
dostępna przez sterownik o nazwie HIMEM.

<!-- S21 -->
I właśnie tu
problem programisty
stał się problemem gracza.

<!-- S22 -->
Sterowniki myszy, napędu CD
czy karty dźwiękowej
odgryzały kawałek tej cennej pamięci,
chyba że udało ci się załadować je do pamięci górnej.

<!-- S23 -->
Gracze nauczyli się więc edytować dwa pliki,
CONFIG.SYS i AUTOEXEC.BAT.

<!-- S24 -->
Jedna gra chciała EMS.
Inna chciała ją wyłączoną,
za pomocą ustawienia NOEMS.
A trzecia potrzebowała każdego wolnego kilobajta.

<!-- S25 -->
W 1993 roku MS-DOS 6 dodał
menu przy starcie.

<!-- S26 -->
Wybierałeś konfigurację
dla gry, w którą chciałeś zagrać,
i komputer uruchamiał się w ustawieniach dla tej gry.

<!-- S27 -->
Niektórzy kończyli
z osobną pozycją
niemal dla każdej gry, jaką mieli.

<!-- S28 -->
Ale wtedy
większe gry znalazły już
sposób na obejście ograniczeń DOS-u.

<!-- S29 -->
Od 386
sam procesor potrafił działać
w 32-bitowym trybie chronionym,
z miejscem na maksymalnie 4 gigabajty.

<!-- S30 -->
Tryb chroniony omawialiśmy
we wcześniejszym filmie.
DOS jednak nie umiał z niego korzystać.

<!-- S31 -->
Gry przynosiły więc własnego pomocnika,
DOS extender.
Najbardziej znany był DOS/4GW.

<!-- S32 -->
Był dołączany do popularnego kompilatora,
Watcom C.

<!-- S33 -->
Kiedy gra się uruchamiała,
DOS/4GW przełączał procesor
w tryb chroniony,
dając grze dostęp
do pamięci powyżej limitu DOS-u.

<!-- S34 -->
DOS wciąż działał pod spodem,
zapewniając usługi takie jak dostęp do plików.
Ale gra działała teraz w trybie chronionym,
a nie jako tradycyjny program DOS-owy.

<!-- S35 -->
Jeśli grałeś w gry na DOS-a w latach dziewięćdziesiątych,
widziałeś, jak jego nazwa
mignęła na ekranie.

<!-- S37 -->
A teraz obraz.
W jednym z najczęściej używanych trybów VGA,
zwanym Mode 13h,
ekran miał 320
na 200 pikseli
i 256 kolorów.

<!-- S38 -->
Każdy piksel to był jeden bajt.
Żeby pokolorować piksel,
zapisywałeś liczbę w pamięci.
Żadnej biblioteki graficznej. Tylko pamięć.

<!-- S39 -->
Cały ekran zajmował
64 000 bajtów.

<!-- S40 -->
To tuż poniżej 64 kilobajtów,
na tyle mało, żeby zmieścić się w jednym segmencie,
bloku, który 16-bitowy program
mógł zaadresować za jednym razem.
Choć raz pamięć była po twojej stronie.

<!-- S41 -->
Ale jeśli rysujesz od razu
na widocznym ekranie,
gracz widzi niedokończone obrazy,
a obraz migocze.

<!-- S42 -->
Gry rysowały więc każdą klatkę
najpierw w ukrytym buforze,
a potem kopiowały gotowy obraz
do pamięci wideo.

<!-- S43 -->
W 1991 roku Michael Abrash,
programista i autor,
opublikował lepszy sposób.
Nazwał go Mode X.

<!-- S44 -->
Wykorzystywał część układu VGA,
której większość programistów
nigdy nie ruszała.

<!-- S45 -->
Dawał kwadratowe piksele
i miejsce na kilka ekranów
w pamięci wideo.

<!-- S46 -->
Gra rysowała na ekranie,
którego nikt nie widział,
a potem po prostu się na niego przełączała.
Ale programowało się to dużo trudniej.

<!-- S47 -->
Potem był dźwięk.
A dźwięk to była loteria.

<!-- S48 -->
Wbudowany głośniczek peceta
służył do pikania.

<!-- S49 -->
Potem przyszły karty dźwiękowe
i inny sprzęt audio.
Żadne dwa urządzenia
nie działały tak samo.

<!-- S50 -->
AdLib, z układem Yamahy,
który syntetyzował muzykę.
Sound Blaster, który potrafił też odtwarzać
nagrany dźwięk.

<!-- S51 -->
Roland MT-32,
drogie pudełko z bogatszymi instrumentami.
Gravis UltraSound.

<!-- S52 -->
Obsługa ich wszystkich
oznaczała pisanie różnych sterowników.

<!-- S53 -->
A gra musiała wiedzieć,
gdzie jest karta.
Jej port, jej przerwanie
i jej kanał DMA.

<!-- S54 -->
Zwykła odpowiedź dla Sound Blastera
brzmiała: port 220, IRQ 7, DMA 1.
Zazwyczaj.

<!-- S55 -->
Wystarczyło pomylić jedno
i gra milczała.
Albo się zawieszała.

<!-- S56 -->
W 1991 roku programista John Miles
wydał bibliotekę,
która rozmawiała z wieloma kartami dźwiękowymi
przez jeden interfejs.

<!-- S57 -->
Gra mogła napisać kod dźwięku raz
i zostawić obsługę karty bibliotece.

<!-- S58 -->
To była kolejna warstwa
między grą a sprzętem.
Zapamiętaj to.

<!-- S59 -->
A potem była szybkość.
Programiści liczyli
każdy krok procesora.

<!-- S63 -->
Żeby znaleźć piksel na ekranie,
mnożysz jego wiersz
przez 320.

<!-- S63b -->
Na starszych procesorach
mnożenie mogło być kosztowne.

<!-- S64 -->
Ale 320
to 256
plus 64.
Obie liczby to potęgi dwójki.

<!-- S65 -->
Mnożenie możesz więc zastąpić
dwoma przesunięciami bitowymi i dodawaniem.

<!-- S67 -->
Chris Sawyer zszedł na najniższy poziom.
Transport Tycoon napisał w 1994 roku
niemal w całości w asemblerze,

<!-- S68 -->
czyli w instrukcjach,
które rozumie sam procesor,
jedna po drugiej.

<!-- S69 -->
A czasem
nawet to wszystko nie wystarczało.

<!-- S70 -->
W 1990 roku Wing Commander miał błąd,
którego zespół nie umiał znaleźć,
a termin się zbliżał.

<!-- S71 -->
Kiedy wychodziłeś z gry,
menedżer pamięci się wywalał
z komunikatem o błędzie.

<!-- S72 -->
Programista Ken Demarest
otworzył więc menedżer pamięci
w edytorze szesnastkowym
i zmienił tekst tego komunikatu.

<!-- S73 -->
Teraz brzmiał:
„Dziękujemy za grę w Wing Commander”.

<!-- S74 -->
Potem zespół znalazł prawdziwy błąd,
a żart nigdy nie trafił do wydanej gry.

<!-- S74b -->
Niektórzy gracze do dziś są pewni, że go widzieli.
A późniejsze gry Origin
naprawdę tak się żegnały.

<!-- S75 -->
Co prowadzi nas z powrotem do Dooma.

<!-- S76 -->
Doom używał DOS/4GW
i działał jako program 32-bitowy.

<!-- S77 -->
Sprzęt do obliczeń zmiennoprzecinkowych
nie był gwarantowany w każdym pececie.

<!-- S78 -->
Doom używał więc arytmetyki stałoprzecinkowej.
Liczby całkowite,
w których dolne 16 bitów
oznaczało część ułamkową.

<!-- S79 -->
A jego świat nie był
naprawdę trójwymiarowy.

<!-- S80 -->
Każdy poziom to płaski rzut,
z wysokością każdej podłogi
i każdego sufitu.

<!-- S81 -->
Jedno pomieszczenie nigdy nie może leżeć nad drugim.
I nie da się porządnie spojrzeć w górę ani w dół.

<!-- S82 -->
Zanim dało się zagrać w poziom,
narzędzie dzieliło mapę
na drzewo binarne, BSP.

<!-- S83 -->
Silnik przechodzi to drzewo
od przodu do tyłu,
zaczynając od strony gracza,
i pomija obszary, których nie widać.

<!-- S84 -->
A Doom nie był nawet pisany w DOS-ie.

<!-- S85 -->
id Software tworzyło go
na stacjach roboczych NeXT
i kompilowało wynik pod DOS.

<!-- S86 -->
Doom nie był uniwersalnym silnikiem 3D.
Zbudowano go dokładnie
pod jeden rodzaj świata.
Ta specjalizacja
pomogła mu działać na 386.

<!-- S87 -->
A inne studia chciały ten świat.

<!-- S88 -->
Raven Software licencjonowało silnik Dooma
do Heretica w 1994 roku
i Hexena w 1995.

<!-- S89 -->
Doom pomógł ugruntować
nowy sposób robienia gier.
Studia mogły licencjonować istniejący silnik,
zamiast budować wszystko od zera.

<!-- S90 -->
Extender pamięci.
Biblioteka dźwiękowa.
Licencjonowany silnik.

<!-- S91 -->
Każdy z nich zdjął jeden problem
z barków programisty.
A warstw przybywało,
aż wyrosły z nich silniki,
od których programiści zaczynają dziś.

<!-- S92 -->
Czy więc robienie gier było kiedyś trudniejsze?
Pod wieloma względami tak.

<!-- S93 -->
Ale trudność nie zniknęła.
Przeniosła się.

<!-- S94 -->
Dziś programiści zmagają się
z gigabajtami zasobów
i milionami wielokątów,
zamiast z kilkuset kilobajtami.

<!-- S95 -->
W DOS-ie nawet gracz
musiał wiedzieć, gdzie podziewa się jego pamięć.

<!-- S96 -->
Mam więc do ciebie pytanie.
Pamiętasz, jak budowałeś
menu startowe tylko po to, żeby uruchomić jedną grę?
I była to męczarnia,
czy połowa zabawy?
Napisz mi w komentarzach.
