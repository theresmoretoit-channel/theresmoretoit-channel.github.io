<!-- S01 -->
19 lipca 2024 roku
firma zajmująca się bezpieczeństwem, CrowdStrike,
rozesłała rutynową aktualizację.

<!-- S02 -->
Nie nowy program.
Tylko mały plik konfiguracyjny.

<!-- S03 -->
W ciągu kilku godzin 8,5 miliona
komputerów z Windowsem stanęło
na niebieskim ekranie.

<!-- S04 -->
Linie lotnicze odwołały loty.
Szpitale odwołały operacje.
Jedna stacja informacyjna zniknęła z anteny.

<!-- S05 -->
A błąd, który za tym stał,
był całkiem zwyczajny.
Program spodziewał się 20 wartości.
Aktualizacja dała mu 21.

<!-- S06 -->
Twoje gry i aplikacje robią
takie błędy cały czas.
Kiedy to się dzieje, gra się zamyka,
a ty uruchamiasz ją jeszcze raz.

<!-- S07 -->
Ten sam rodzaj błędu.
Jeden zamyka okno.
Drugi zatrzymuje
8,5 miliona maszyn.

<!-- S08 -->
Nie chodzi o sam błąd.
Tylko o to, gdzie działał kod.

<!-- S09 -->
Więc dlaczego jeden program nie może
przejąć twojego komputera...
i dlaczego ten mógł?

<!-- S10 -->
Nie zawsze tak było.

<!-- S11 -->
Na pecetach z DOS-em w latach 80.
nic w procesorze nie zatrzymywało programu.
Mógł pisać w dowolnym miejscu pamięci
i rozmawiać bezpośrednio ze sprzętem.

<!-- S12 -->
Wystarczyło, że jeden program zapisał coś
tam, gdzie nie powinien,
i mógł nadpisać system operacyjny,
a cała maszyna się zawieszała.

<!-- S13 -->
Rozwiązaniem było przestać ufać programom
i zostawić nieufność
procesorowi.

<!-- S14 -->
W 1982 roku procesor Intel 80286
wprowadził tryb chroniony
z czterema poziomami uprawnień.

<!-- S15 -->
Zwykle rysuje się je
jako cztery pierścienie, jeden w drugim.

<!-- S16 -->
Pierścień 0 jest w środku.
Pierścień 3 jest na zewnątrz.

<!-- S17 -->
A numeracja idzie od tyłu.
Im niższy numer,
tym więcej kodowi wolno.

<!-- S18 -->
Pierścień 0 należy do jądra,
centralnej części systemu operacyjnego.
Przydziela pamięć,
decyduje, który program działa następny,
i rozmawia ze sprzętem.

<!-- S19 -->
W pierścieniu 3 działają twoja przeglądarka,
twoje gry i twój edytor tekstu.
To się nazywa tryb użytkownika.

<!-- S19b -->
Windows, macOS i Linux
dzielą pracę właśnie tak.
Jądro w pierścieniu 0,
twoje aplikacje w pierścieniu 3.

<!-- S19c -->
Telefony i nowsze Maki od Apple
używają zamiast tego układów ARM.
Tam poziomy nazywają się exception levels.
Inna nazwa, ten sam podział:
jeden dla jądra, jeden dla twoich aplikacji.

<!-- S20 -->
Procesor zawsze wie,
w którym pierścieniu właśnie działa.
I to sprawdza.

<!-- S21 -->
Niektóre instrukcje działają tylko w pierścieniu 0.
Na przykład wyłączenie przerwań
albo zmiana tego, jak mapowana jest pamięć.

<!-- S22 -->
Kiedy program w pierścieniu 3 spróbuje takiej,
procesor odmawia.
Zgłasza wyjątek
i oddaje kontrolę jądru,
które zwykle kończy program.

<!-- S23 -->
Z pamięcią jest tak samo.
Każda strona pamięci jest oznaczona
jako user albo supervisor.

<!-- S24 -->
Program w pierścieniu 3,
który dotknie strony supervisor,
nie dostaje danych.
Zostaje zatrzymany.

<!-- S25 -->
Twoja przeglądarka i twoja gra
działają obie w pierścieniu 3.
Tym, co je od siebie oddziela,
jest to, że każda ma własną mapę pamięci.
Pamięci drugiego programu
po prostu na niej nie ma.

<!-- S26 -->
Więc kiedy gra się wysypie,
szkoda zostaje w grze.
Jądro po niej sprząta.
Wszystko inne działa dalej.

<!-- S27 -->
A teraz wróćmy do CrowdStrike.
Jego sterownik działał w pierścieniu 0,
tuż obok jądra.

<!-- S28 -->
Nic powyżej pierścienia 0
nie wyłapie takiego błędu.

<!-- S29 -->
Więc Windows zrobił jedyną bezpieczną rzecz, jaka została.
Zatrzymał całą maszynę, celowo,
zamiast dalej działać na pamięci,
której nie mógł już ufać.

<!-- S30 -->
Tym właśnie jest niebieski ekran.

<!-- S31 -->
A ponieważ sterownik uruchamiał się
za każdym razem, gdy startował Windows,
każdy restart przywracał awarię.

<!-- S32 -->
Ale tu pojawia się pytanie.
Skoro przeglądarka nie może dotykać sprzętu,
jak w ogóle zapisuje plik
albo wysyła cokolwiek przez sieć?

<!-- S33 -->
Prosi.

<!-- S34 -->
Program wkłada swoje żądanie
do rejestrów procesora.
Który plik. Dokąd mają trafić dane.
Ile ich.

<!-- S35 -->
Potem wykonuje jedną specjalną instrukcję.
Na współczesnym pececie nazywa się SYSCALL.

<!-- S36 -->
W tej chwili procesor przełącza się
z pierścienia 3 do pierścienia 0...

<!-- S37 -->
ale nie skacze tam,
gdzie chce program.
Skacze do jednego punktu wejścia,
który jądro wybrało wcześniej.

<!-- S38 -->
Jądro sprawdza żądanie,
wykonuje zadanie
i wraca do pierścienia 3.
Program nigdy sam nie dotknął dysku.

<!-- S39 -->
To jest wywołanie systemowe
i dzieje się bez przerwy.

<!-- S40 -->
Policzyliśmy je na laptopie.
Program, który nie robi zupełnie nic,
i tak wykonuje ich 30.

<!-- S41 -->
Firefox przy starcie
i wczytaniu jednej strony Wikipedii
wykonał ich około 670 tysięcy
w 20 sekund...
i to mimo że nasze liczenie go spowalniało.

<!-- S42 -->
Każde z nich
to podróż przez mur i z powrotem.

<!-- S43 -->
Zostaje coś dziwnego.
Cztery pierścienie,
a potrzebowaliśmy tylko dwóch.

<!-- S44 -->
Co się stało z pierścieniami 1 i 2?

<!-- S45 -->
Pomysł pierścieni jest starszy niż pecet.
Multics, system operacyjny
z końca lat 60.,
miał ich osiem.

<!-- S46 -->
Chodziło o warstwy zaufania.
Rdzeń systemu w środku,
mniej zaufane usługi wokół niego
i programy na zewnątrz.

<!-- S46b -->
Intel narysował ten sam obraz.
Pierścienie 1 i 2 miały służyć
warstwom pośrednim,
takim jak sterowniki i usługi systemowe.
Bardziej zaufane niż twoje aplikacje,
mniej niż jądro.

<!-- S47 -->
Na przeszkodzie stanęły dwie rzeczy.

<!-- S48 -->
Po pierwsze, systemy takie jak Unix i Windows NT
projektowano tak, żeby działały
na wielu rodzajach procesorów.

<!-- S49 -->
A jedyny podział,
jaki oferował każdy procesor,
to były dwa poziomy.
Jeden dla jądra,
jeden dla całej reszty.

<!-- S50 -->
Po drugie, sam procesor x86.
Kiedy mapuje pamięć,
każda strona zna tylko dwa stany.
User albo supervisor.

<!-- S51 -->
Pierścienie 1 i 2 liczą się jako supervisor.
Więc sterownik w pierścieniu 1
i tak mógłby dotykać pamięci jądra.
Dodatkowy pierścień niewiele by chronił.

<!-- S51b -->
Kilka systemów i tak z nich korzystało.
OS/2 wpuszczał niektóre programy do pierścienia 2,
tylko po to, żeby mogły rozmawiać bezpośrednio ze sprzętem.

<!-- S51c -->
A zanim procesory dostały wsparcie
dla maszyn wirtualnych,
Xen i VirtualBox przenosiły jądro systemu gościa
do pierścienia 1,
żeby system pod spodem
mógł zachować pierścień 0 dla siebie.

<!-- S52 -->
W 2023 roku Intel zaproponował
całkowite usunięcie pierścieni 1 i 2.

<!-- S53 -->
W grudniu 2024 roku porzucił ten plan.
Wciąż są w twoim procesorze.
Prawie nic z nich nie korzysta.

<!-- S54 -->
Na razie brzmi to uspokajająco.
Zasady są w sprzęcie,
a sprzęt sprawdza każdy dostęp.

<!-- S55 -->
W 2017 roku trzy zespoły badaczy,
niezależnie od siebie,
znalazły drogę przez ten mur.

<!-- S56 -->
Nazwali ją Meltdown.
A żeby to zrozumieć,
musisz znać jedną sztuczkę,
którą stosują współczesne procesory.

<!-- S57 -->
Procesor nie czeka,
aż jedna instrukcja się skończy,
zanim zacznie następną.
Wybiega naprzód
i wykonuje instrukcje, które pewnie będą mu potrzebne.

<!-- S58 -->
Jeśli źle zgadł,
wyrzuca wyniki,
jakby nic się nie stało.

<!-- S59 -->
I tu jest luka.
W podatnych układach Intela
program w pierścieniu 3 mógł poprosić
o bajt pamięci jądra...

<!-- S60 -->
a procesor go pobierał
i przekazywał kolejnym instrukcjom,
zanim skończył sprawdzać,
czy to w ogóle dozwolone.

<!-- S61 -->
Sprawdzenie faktycznie kończyło się porażką.
Wynik był wyrzucany.

<!-- S62 -->
Ale te kolejne instrukcje
zdążyły już użyć tajnego bajtu,
żeby wciągnąć jeden kawałek
własnej pamięci programu
do pamięci podręcznej procesora.

<!-- S63 -->
A pamięć podręczna nie zapomina
tylko dlatego, że wynik anulowano.

<!-- S64 -->
Więc program mierzy,
jak szybko odpowiada każdy kawałek jego pamięci.
Ten, który odpowie szybko,
zdradza tajny bajt.

<!-- S65 -->
Bajt po bajcie
zwykły program mógł czytać
pamięć jądra
i wszystkie tajemnice, które w niej leżały.
Łącznie z hasłami i kluczami szyfrowania.

<!-- S66 -->
Meltdown dotyczył procesorów Intela
aż od 1995 roku.

<!-- S67 -->
Ujawniono go
3 stycznia 2018 roku.

<!-- S68 -->
Poprawka nie mogła zmienić krzemu.
Więc systemy operacyjne zmieniły mapę.

<!-- S69 -->
Kiedy twój program działa,
pamięć jądra jest teraz prawie całkiem
usunięta z jego mapy.
Nie ma tam czego pobrać.

<!-- S70 -->
Ale pamiętasz wywołania systemowe?
Każda podróż przez mur
musi teraz też podmienić mapę.

<!-- S71 -->
Red Hat zmierzył łatki na Meltdown
i pokrewną lukę, Spectre.
Poniżej 1% przy niektórych zadaniach...
do 19% przy mocno obciążonych bazach danych.

<!-- S72 -->
Zasada była cały czas słuszna.
Procesor po prostu sprawdzał ją za późno.

<!-- S73 -->
I to sprowadza nas z powrotem do CrowdStrike
i do trudniejszego pytania.

<!-- S74 -->
Dlaczego program zabezpieczający
w ogóle siedział w pierścieniu 0?

<!-- S75 -->
Bo stamtąd widzi wszystko.
Uruchamia się przed innymi programami.
A złośliwemu oprogramowaniu z prawami administratora
trudniej go wyłączyć.

<!-- S76 -->
Lista samego Microsoftu
kończy się ostrzeżeniem.
Sterowniki w jądrze dają to kosztem odporności systemu.

<!-- S77 -->
Po awarii
Microsoft zaczął budować sposób,
żeby antywirusy
mogły działać poza jądrem.

<!-- S78 -->
Jesienią 2026 roku
to wciąż jest tylko w testowych wersjach Windowsa.
A jądro nie zostało zamknięte
dla firm od bezpieczeństwa.

<!-- S79 -->
Twoje gry stoją przed tym samym dylematem.

<!-- S80 -->
Cheaty, które działają w jądrze,
są niewidoczne dla anty-cheata,
który działa w pierścieniu 3.

<!-- S81 -->
Więc anty-cheat też się tam wprowadził.
Vanguard od Riotu, używany przez Valoranta,
umieszcza sterownik w pierścieniu 0.
Na większości pecetów ładuje się razem z Windowsem...
nawet jeśli nigdy nie otworzysz gry.

<!-- S82 -->
To nie znaczy, że jest wadliwy.
Ale siedzi w tym samym miejscu
co sterownik CrowdStrike,
gdzie jeden błąd zatrzymuje całą maszynę.

<!-- S83 -->
Więc dlaczego jeden program nie może
przejąć twojego komputera?

<!-- S84 -->
Bo procesor trzyma
prawie każdy program z dala od środka
i sprawdza go za każdym razem, gdy zapuka.

<!-- S85 -->
Ale procesor nie może zdecydować,
kogo wpuścić.
To decydują ludzie...
za każdym razem, gdy instalują sterownik.

<!-- S86 -->
Więc mam pytanie do komentarzy.
Kto powinien decydować, które programy
trafiają do pierścienia 0:
ty, Microsoft
czy firmy, które je tworzą?
