<!-- S01 -->
Gdzieś u ciebie w domu
może być zegar,
którego nikt nigdy nie ustawiał.

<!-- S02 -->
Przetrwa przerwę w dostawie prądu.
Sam zmienia czas na letni i zimowy,
w środku nocy.

<!-- S03 -->
Nie ma połączenia z internetem.
Żadnego Wi-Fi, żadnego GPS,
żadnej aplikacji w telefonie.

<!-- S04 -->
Ma tylko malutki odbiornik radiowy.
I raz na sekundę
słyszy pojedynczy impuls.

<!-- S05 -->
Jak więc zegar
zamienia jeden impuls na sekundę
w dokładną godzinę, datę,
a nawet dzień tygodnia?

<!-- S06 -->
W Europie te impulsy pochodzą
z DCF77 pod Frankfurtem.
W Ameryce z WWVB w Kolorado.
Różne nadajniki, ta sama idea.

<!-- S07 -->
Weźmy ten niemiecki.
Nadaje równą falę radiową,
dzień i noc.
A na początku każdej sekundy
na chwilę ją osłabia.

<!-- S08 -->
Cały sekret tkwi w tym, jak długo
pozostaje przyciszona.

<!-- S09 -->
Spadek na jedną dziesiątą sekundy
oznacza zero.
Spadek na dwie dziesiąte oznacza jedynkę.

<!-- S10 -->
I to cała idea.
Żadnych pakietów, żadnej sieci.
Tylko fala radiowa, która spada
na krótko albo na dłużej.

<!-- S11 -->
Jeden bit na sekundę.
Czyli wysłanie zaledwie 60 bitów
zajęłoby całą minutę.

<!-- S12 -->
A tak naprawdę wysyła ich tylko 59.

<!-- S13 -->
W ostatniej sekundzie każdej minuty
fala w ogóle nie spada.
I właśnie ten brakujący spadek
jest najważniejszą częścią
całego sygnału.

<!-- S14 -->
Bo kiedy przychodzi następny spadek,
zegar wie,
że właśnie zaczęła się nowa minuta.

<!-- S15 -->
Przerwa działa jak kropka.
Wszystko między dwiema przerwami
to jedno pełne zdanie.

<!-- S16 -->
Co więc mieści się w zdaniu
z 59 bitów?

<!-- S17 -->
Minuta. Godzina.
Dzień miesiąca, dzień tygodnia,
miesiąc i rok.

<!-- S18 -->
Większość liczb wysyła się cyfra po cyfrze.
47 minut
nie jest wysyłane jako 47.
Wysyła się je jako dwie osobne cyfry,
czwórkę i siódemkę.

<!-- S19 -->
4 bity wystarczą na dowolną cyfrę
od 0 do 9.
Dziesiątki minut nigdy nie przekraczają 5,
więc dostają tylko 3.

<!-- S20 -->
A rok dostaje tylko dwie cyfry.
Dla nadajnika
2026 to po prostu 26.
Stulecie zegar dopisuje sam.

<!-- S21 -->
Ale radio nie jest czystym kanałem.
Silnik, ładowarka do telefonu,
tania żarówka LED...
każda z nich może zniekształcić spadek.

<!-- S22 -->
Dlatego po każdym bloku liczb
przychodzi jeden dodatkowy bit, tak zwany bit parzystości.

<!-- S23 -->
Dobiera się go tak, by liczba jedynek
w bloku zawsze była parzysta.

<!-- S24 -->
Jeśli zakłócenie odwróci jeden bit,
liczba robi się nieparzysta
i zegar wie,
że coś poszło nie tak.

<!-- S25 -->
Ale jeśli odwrócą się dwa bity,
liczba znów jest parzysta
i błąd się prześlizguje.

<!-- S26 -->
Dlatego wiele zegarów
nie ufa pojedynczej minucie.
Czekają na kolejną poprawną.

<!-- S27 -->
I dlatego samo ustawienie się
może zająć kilka minut,
a w gorszy dzień dużo dłużej.

<!-- S28 -->
Co rodzi dziwny problem.

<!-- S29 -->
Zegar przez całą minutę
zbiera czas 10:48.
Ale gdy zbiera tę wiadomość,
wciąż jest 10:47.

<!-- S30 -->
Kiedy więc czas naprawdę się zmienia?

<!-- S31 -->
Bo ta wiadomość jest zapowiedzią.
Mówi, która będzie godzina,
kiedy zacznie się następna minuta.

<!-- S32 -->
Zegar czyta całe zdanie,
przeczekuje brakujący spadek,
a kiedy przychodzi następny spadek,
to właśnie on jest dokładnym momentem.

<!-- S33 -->
Bity mówią zegarowi, która jest godzina.
Spadek mówi kiedy.

<!-- S34 -->
Ale w zdaniu jest jeszcze kilka słów
poza samym czasem.

<!-- S35 -->
Dwa bity mówią, czy w Niemczech
obowiązuje czas zimowy, czy letni.

<!-- S36 -->
A trzeci to ostrzeżenie.
Przez całą godzinę przed zmianą czasu
ma wartość 1.

<!-- S37 -->
Twój zegar nie musi więc wiedzieć,
w którą niedzielę marca
przestawia się zegarki do przodu
ani w którą niedzielę października do tyłu.
Nikt go nigdy nie nauczył tej reguły.
Po prostu dowiaduje się o tym godzinę wcześniej.

<!-- S38 -->
Jeśli Europa kiedyś przestanie zmieniać czas,
to ostrzeżenie po prostu już nigdy nie przyjdzie.

<!-- S39 -->
Inny bit ostrzegał kiedyś przed sekundą przestępną,
dodatkową sekundą dodawaną od czasu do czasu,
bo obrót Ziemi
nie odmierza czasu idealnie.
Taka minuta mogła mieć 61 sekund.

<!-- S40 -->
Ostatnią dodano
pod koniec 2016 roku.
Ale w październiku 2026
światowe instytucje metrologiczne
zdecydowały o zniesieniu sekund przestępnych.
Od 20 maja 2027
UTC będzie płynąć bez przerw.

<!-- S41 -->
A pierwsze 14 bitów
każdej minuty
w ogóle nie dotyczy czasu.

<!-- S42 -->
Od 2006 roku służą też
do przesyłania zaszyfrowanych prognoz pogody
do zgodnych stacji pogodowych.

<!-- S43 -->
Czyli sygnał, który ustawia twój budzik,
mógł też powiedzieć
czyjejś stacji pogodowej,
czy w czwartek będzie padać.

<!-- S44 -->
A mimo to większość tych zegarów
nie nasłuchuje cały czas.
Nasłuchiwanie zużywa baterię,
więc wiele z nich próbuje raz na noc,
we wczesnych godzinach porannych.

<!-- S45 -->
Fale długie docierają do zegara dwiema drogami:
wzdłuż ziemi
i odbite od górnych warstw atmosfery.
Po zmroku ta górna droga się zmienia
i sygnał często sięga dalej.

<!-- S46 -->
A o trzeciej w nocy
w pobliżu zwykle działa mniej urządzeń, ładowarek i lamp,
które mogłyby go zagłuszyć.

<!-- S47 -->
Między tymi sprawdzeniami
zegar działa dzięki kryształowi kwarcu,
który może się rozjechać o mniej więcej sekundę na dobę.

<!-- S48 -->
Przy następnym udanym sprawdzeniu
radio koryguje tę odchyłkę.

<!-- S49 -->
Nawet to, gdzie nasłuchuje, ma znaczenie.
Antena to mały pręt ferrytowy
owinięty drutem.

<!-- S50 -->
Słyszy najlepiej, gdy pręt leży w poprzek
kierunku do nadajnika,
a nie wtedy, gdy w niego celuje.
Obróć zegar,
a słaby sygnał może całkiem zniknąć.

<!-- S51 -->
Dlatego jeden zegar działa na półce,
a ten sam zegar dwa metry dalej,
za ścianą z żelbetu, nigdy się nie ustawi.

<!-- S52 -->
Skąd więc nadajnik
bierze swój czas?

<!-- S53 -->
Z PTB,
niemieckiego krajowego instytutu metrologii,
który prowadzi zegary atomowe.

<!-- S54 -->
Sama sekunda jest zdefiniowana
za pomocą atomów cezu.
Jedna sekunda to dokładnie
9 192 631 770 drgań
promieniowania, które emitują.

<!-- S55 -->
Czyli tani budzik na szafce nocnej
dosłownie
podąża za wzorcem czasu
zdefiniowanym przez atomy cezu.

<!-- S56 -->
Choć nie idealnie.
Sygnał biegnie z prędkością światła,
a nawet ono potrzebuje około 3 milisekund
na każde 1000 kilometrów.

<!-- S57 -->
Odbiornik dodaje własne opóźnienie,
a twój zegar nie koryguje niczego z tego.
Nie musi.
Pokazuje tylko sekundy.

<!-- S58 -->
Z jednego miejsca pod Frankfurtem
sygnał dociera do zegarów
nawet o mniej więcej 2000 kilometrów od niego.
To większość Europy.

<!-- S59 -->
Szwajcaria miała własny nadajnik,
o nazwie HBG, do końca 2011 roku.
Jego anteny wymagały wymiany,
korzystało z niego zbyt mało ludzi,
a szwajcarskie zegary mogły po prostu
odbierać zamiast tego sygnał z Niemiec.

<!-- S60 -->
Inni zachowali swoje.
Wielka Brytania, Francja, Japonia i Chiny
mają własne.

<!-- S61 -->
A w Ameryce Północnej WWVB
nadaje z Fort Collins od 1963 roku,
z kodem czasu od 1965.

<!-- S62 -->
Ta sama zasada, inny dialekt.
Zero to spadek na dwie dziesiąte sekundy.
Jedynka trwa pół sekundy.

<!-- S63 -->
I zamiast jednej przerwy na minutę
co 10 sekund pojawia się dłuższy znacznik,
jak przecinki w zdaniu.
Dwa takie z rzędu oznaczają nową minutę.

<!-- S64 -->
Największa różnica
to to, jaki czas nadaje.
Niemcy nadają czas urzędowy środkowoeuropejski,
wspólny dla dużej części kontynentu.

<!-- S65 -->
Ale Stany Zjednoczone
rozciągają się na kilka stref czasowych.
Dlatego WWVB nadaje czas uniwersalny, UTC,
a ty mówisz zegarowi, gdzie jesteś.

<!-- S66 -->
Nie nadaje nawet miesiąca.
Tylko dzień roku,
od 1 do 366.

<!-- S67 -->
Żadna z tych stacji
nie mówi tym samym językiem.
Zegar zbudowany dla Niemiec
nic nie zrozumie z Kolorado.

<!-- S68 -->
Ale po obu stronach Atlantyku
to ta sama cicha rutyna.
Noc w noc mały odbiornik
synchronizuje się z atomowym wzorcem czasu
oddalonym o setki albo tysiące kilometrów.

<!-- S69 -->
Mam więc do ciebie pytanie.
Gdyby wszystkie radiowe sygnały czasu
zniknęły dziś w nocy,
czy w ogóle byś to zauważył?
Daj znać w komentarzach.
