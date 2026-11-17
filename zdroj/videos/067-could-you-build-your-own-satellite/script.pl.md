<!-- S01 -->
Wyobraź sobie, że masz szalony pomysł.
Chcesz zbudować własnego satelitę.
Nie wartego miliard dolarów
satelitę komunikacyjnego.
Coś małego.

<!-- S02 -->
Pudełko wielkości mniej więcej
bochenka chleba.
W środku: komputer, panele słoneczne,
radio, kilka czujników.
Może nawet kamera.

<!-- S03 -->
Budujesz go w garażu.
A potem jakoś...
umieszczasz go na orbicie.
Brzmi niemożliwie.
Ale to możliwe.

<!-- S04 -->
Ludzie robią niemal dokładnie to
już od lat.
Takie satelity nazywamy CubeSatami.

<!-- S05 -->
A zaskakujące jest to,
że najtrudniejsze
nie jest zbudowanie satelity.
To cała reszta.

<!-- S06 -->
Podstawowa jednostka nazywa się 1U —
mniej więcej dziesięciocentymetrowy sześcian.
Składasz jednostki razem
i masz 2U, 3U, 6U
i większe.

<!-- S07 -->
Pomysł jest prosty.
Zamiast projektować nowy statek kosmiczny
od zera,
używasz standardowych rozmiarów
i standardowych interfejsów.
kosmos staje otworem
przed uczelniami, startupami,
a może nawet przed tobą.

<!-- S07b -->
A przy okazji, jeśli lubisz takie
filmy, rozważ subskrypcję.

To naprawdę pomaga kanałowi.

<!-- S08 -->
Co właściwie zawierałby
nasz mały satelita?
Najpierw potrzebuje komputera.
Coś musi uruchamiać oprogramowanie,
sterować sprzętem
i decydować, co robić.

<!-- S09 -->
Potem zasilanie.
Panele słoneczne wytwarzają prąd.
Akumulatory go magazynują
na czas, gdy satelita
wślizguje się w cień Ziemi.

<!-- S10 -->
Potem komunikacja.
Radio. Antena.
A na Ziemi
nasłuchująca stacja naziemna.

<!-- S11 -->
Potem czujniki.
Temperatura. Napięcie. Prąd.
Przyspieszenie. Pole magnetyczne.
I jakiś sposób, żeby stwierdzić,
w którą stronę satelita jest zwrócony.
Bo na orbicie
ustalenie, gdzie jest "góra", jest zaskakująco trudne.

<!-- S12 -->
Ale zanim go zbudujemy,
pojawia się niewygodne pytanie.
Ile kosztuje to małe pudełko?
Odpowiedź brzmi...
więcej, niż by się zdawało.

<!-- S13 -->
Prosty CubeSat 1U
może z łatwością kosztować
dziesiątki tysięcy dolarów —
tylko za sprzęt lotny.
System zasilania. Panele słoneczne.
Akumulatory. Komputer. Radio.
Układ sterowania orientacją. Konstrukcja.
I ładunek użyteczny.

<!-- S14 -->
Potem przychodzą rzeczy,
których nie ma na liście części.
Testowanie. Integracja.
Dokumentacja.
Obsługa stacji naziemnej.
Licencje.
I na koniec...
start.

<!-- S15 -->
Wspólny start z innymi satelitami
może kosztować dziesiątki tysięcy.
Większe misje i większe CubeSaty
sięgają setek tysięcy.
A to tylko za to,
żeby wynieść go w kosmos.

<!-- S16 -->
A teraz
jeszcze bardziej absurdalny problem.
Pamiętasz te wszystkie części?
Jak to wszystko, u licha,
mieści się w jednym małym pudełku?

<!-- S17 -->
W kosmosie nie ma miejsca
na przypadkowy stos elektroniki.
Liczy się każdy centymetr.
Liczy się każdy gram.
Liczy się każdy wat.
Satelita to trójwymiarowa układanka,
która musi przetrwać start rakiety.

<!-- S18 -->
Skąd więc weźmiesz
wszystkie te części?
Nie musisz projektować
wszystkiego sam.
Istnieje cały przemysł
sprzedający podzespoły do małych satelitów:
komputery, systemy zasilania,
radia, anteny i panele słoneczne.
Są nawet platformy sprzedażowe
specjalnie z częściami do CubeSatów.

<!-- S18b -->
A części są w dodatku znormalizowane.
Wiele z nich ma płytki tego samego formatu
i można je układać jedna na drugiej,
więc elementy od różnych producentów
pasują do jednej jednostki.
Firmy takie jak EnduroSat
i GomSpace je sprzedają,
a pojedynczy podsystem może kosztować
od kilku tysięcy
do dziesiątek tysięcy dolarów.

<!-- S19 -->
A to nie są
egzotyczne procesory.
Jeden współczesny komputer CubeSata
używa ARM Cortex-M7,
ze znanymi interfejsami —
SPI, I²C, UART i CAN.

<!-- S19b -->
I to nie jest specjalny kosmiczny chip.
To prawdziwa, dostępna w sprzedaży płytka,
którą mógłbyś wziąć do ręki.

<!-- S20 -->
Statek kosmiczny potrzebuje czegoś
ważniejszego niż moc obliczeniowa:
przewidywalnego działania,
niskiego poboru mocy i niezawodności.
Bardziej wymagające misje
mogą używać procesorów ARM Cortex-A —
a nawet Linuksa.

<!-- S20b -->
Ale nie jest szybki.
Typowy komputer CubeSata
działa na kilkuset megahercach.
Twój laptop działa na
czterech czy pięciu gigahercach,
z dużo większą liczbą rdzeni.
Poświęca szybkość obliczeń
na rzecz bardzo niskiego poboru mocy.

<!-- S21 -->
A jeśli jesteś programistą,
tu robi się ciekawie.
Nie piszesz
w jakimś tajemniczym "języku kosmicznym".
Piszesz oprogramowanie wbudowane.
Często w C lub C++.

<!-- S22 -->
Może działać bezpośrednio
na sprzęcie,
albo na systemie operacyjnym czasu rzeczywistego,
takim jak FreeRTOS, Zephyr czy RTEMS.
Istnieją nawet otwarte frameworki
stworzone dla statków kosmicznych.
Na przykład F Prime od NASA
to framework oprogramowania lotnego
dla systemów wbudowanych i kosmicznych.

<!-- S23 -->
Twój kod może wyglądać
mniej więcej tak.

<!-- S24 -->
Ale jest jedna ogromna różnica
w porównaniu ze zwykłym komputerem.
Nie zalogujesz się do niego przez SSH.
Nie podłączysz debuggera.
A jeśli oprogramowanie się zawiesi...
twój komputer jest
kilkaset kilometrów nad tobą.

<!-- S25 -->
Potrzebuje więc watchdogów,
trybów awaryjnych, wykrywania błędów
i automatycznego przywracania działania.
Niektóre problemy musi naprawić
bez twojej pomocy.

<!-- S25b -->
A jeden ważny powód, dla którego to wszystko potrzebne,
to promieniowanie.
W kosmosie promienie kosmiczne
mogą przełączyć bit w pamięci
albo nawet uszkodzić chip.
Nie ma ciężkiego ekranowania —
ważyłoby o wiele za dużo.
Zamiast tego komputer sam się pilnuje,
poprawia błędy
i resetuje się, gdy coś pójdzie nie tak.

<!-- S26 -->
Ale jeśli naprawdę
chcesz go wystrzelić...
robi się poważnie.
Część, która działa na twoim biurku,
nie jest automatycznie gotowa
na rakietę.
Musi przetrwać wibracje,
próżnię, skrajne temperatury
i promieniowanie.

<!-- S27 -->
Wróćmy teraz do problemu
z rozpoznaniem, w którą stronę
satelita jest zwrócony.
Wyobraź sobie, jak koziołkuje
w kosmosie.
Żadnej podłogi. Żadnego sufitu.
GPS może ci powiedzieć,
gdzie jesteś...
ale nie, w którą stronę
jesteś zwrócony.

<!-- S28 -->
Satelity łączą więc
żyroskopy, magnetometry
i czujniki słońca,
żeby ustalić swoją orientację.
A potem muszą ją zmienić.
Jedna popularna sztuczka
to magnetorquer.

<!-- S29 -->
Opiera się
o pole magnetyczne Ziemi
i wytwarza niewielki moment obrotowy.
To nie silnik rakietowy.
Nie przesuwa satelity.
Tylko go obraca.
I to wystarczy,
żeby skierować satelitę
dokładnie tam, gdzie chcesz.

<!-- S30 -->
Ale nic z tego
nie jest powodem,
dla którego zbudowaliśmy satelitę.
Potrzebujemy misji.
To jest ładunek użyteczny.
Zmierzyć promieniowanie.
Sfotografować Ziemię.
Badać atmosferę.
Przetestować nowy czujnik.
Albo po prostu udowodnić,
że nowa technologia działa.

<!-- S31 -->
Sam satelita
jest tam głównie po to,
żeby utrzymać ładunek przy życiu.
Zasilać go. Ustawiać go we właściwym kierunku.
Utrzymywać w cieple.
Przechowywać jego dane.
I odsyłać je do domu.

<!-- S32 -->
Gdy twój komputer się zawiesi,
restartujesz go.
Gdy zawiesi się twój satelita...
masz bardzo drogi obiekt,
który cicho okrąża Ziemię.

<!-- S33 -->
Powiedzmy więc, że go zbudowaliśmy.
Wszystko działa...
Komputer się uruchamia...
Radio nadaje.
Panele wytwarzają energię.
Ładunek działa...
Możemy go wystrzelić?
...Jeszcze nie.

<!-- S34 -->
Satelita musi udowodnić,
że przetrwa start.
To znaczy testy.
Mnóstwo testów.

<!-- S35 -->
Najpierw przykręć go
do wielkiej wstrząsarki.
Potem potrząśnij nim, mocno...
To test wibracyjny.
Start rakiety nie jest delikatny.
Musi przetrwać
hałas, wibracje i wstrząsy,
tak, żeby nic
się nie obluzowało ani nie pękło.
Liczy się każda śruba.
Liczy się każde złącze.
Liczy się każdy kawałek kabla.

<!-- S36 -->
Potem przychodzi próżnia.
Na Ziemi ciepło odprowadza powietrze.
W kosmosie nie ma powietrza.
Jedna strona może być skrajnie gorąca,
druga skrajnie zimna,
a elektronika
nadal musi pracować
w dopuszczalnym zakresie temperatur.
Satelita potrzebuje więc
taśm termicznych, powłok,
izolacji
i starannie dobranych materiałów.
Satelity nie mają
klimatyzacji.
Mają fizykę.

<!-- S37 -->
A z akumulatorem
robi się ciekawie.
Naładuj go światłem słonecznym.
Potem satelita
wślizguje się w cień Ziemi
i panele nie wytwarzają prawie nic.
Akumulator utrzymuje go przy życiu.
Potem z powrotem w światło słoneczne.
Ładowanie. Rozładowanie.
Ładowanie. Rozładowanie.
Wciąż od nowa.
Przez lata.
Jeden błąd w zasilaniu
mógłby cicho zakończyć misję.

<!-- S38 -->
A teraz — jak z nim rozmawiać?
Potrzebujesz radia.
Anteny.
I częstotliwości,
której wolno ci legalnie używać.
I stacji naziemnej.
Satelita
nie ma internetu.
Po prostu przelatuje nad głową
i nadaje.

<!-- S39 -->
Twoja stacja naziemna
łapie sygnał.
Komputer go dekoduje.
I nagle masz dane
z własnego statku kosmicznego.
Wyobraź sobie, że otwierasz terminal
i widzisz to.

Tyle że maszyna
wypisująca te liczby...
jest setki kilometrów
nad twoją głową.

<!-- S40 -->
Jak więc
właściwie wyniesiemy go tam?
Mógłbyś zbudować rakietę...
Proszę, nie rób tego...
Nie potrzebujesz jej.
CubeSaty latają
jako ładunki dodatkowe.

<!-- S41 -->
Jakaś rakieta i tak już leci w górę.
Ma jeszcze wolne miejsce.
Twój satelita jedzie razem
w standardowym deployerze.
Własna rakieta nie jest potrzebna.

<!-- S42 -->
A teraz siedzi
na szczycie rakiety.
Nie możesz go dotknąć.
Nie możesz otworzyć pudełka.
Nie możesz podłączyć kabla.
Rakieta startuje.
Jakieś dziewięć minut później
jesteś na orbicie.

<!-- S43 -->
Deployer
uwalnia twojego satelitę.
Wyskakuje swobodnie
i zaczyna koziołkować.

<!-- S43b -->
Ale skąd wie, że jest na zewnątrz?
...
Sprężynowe przełączniki, wciśnięte,
gdy siedział w deployerze,
wyskakują w chwili wyrzucenia,
i komputer się uruchamia.
Potem, zgodnie z przepisami,
milczy przez jakieś pół godziny.
Dopiero wtedy włącza radio,
rozkłada anteny
i wreszcie daje znać do domu.
A gdzieś na Ziemi...
twoja stacja naziemna go słyszy.

<!-- S44 -->
Zbudowałeś maszynę.
A teraz ta maszyna
okrąża planetę.

<!-- S44b -->
Tyle że to jeszcze nie koniec.
Martwy satelita nie może po prostu
zostać tam na zawsze.
Pozostawiony na orbicie przez stulecia,
staje się kosmicznym śmieciem.

<!-- S45 -->
To znaczy, że współczesne misje
coraz częściej muszą planować
koniec
życia statku kosmicznego.
W idealnym przypadku rzadka górna atmosfera
powoli ściąga go w dół.
Jego orbita się obniża.
Wraca w atmosferę.
I spala się.
Koniec misji...
jest częścią misji.

<!-- S46 -->
Więc... czy mógłbyś zbudować
własnego satelitę?
Technicznie tak.
Nie musisz być NASA.
Nie musisz
mieć własnej rakiety.
Nie musisz nawet koniecznie mieć
wielkiej firmy.

<!-- S47 -->
Satelita musi
przetrwać start.
Przetrwać kosmos.
Komunikować się legalnie.
Działać samodzielnie.
I na koniec
zejść z orbity.
To wszystko
musi zostać udowodnione,
zanim ktokolwiek
umieści go na rakiecie.

<!-- S48 -->
Dzięki CubeSatom kosmos nie stał się prosty.
Znormalizowały go.
Zamiast budować wszystko
od zera,
możesz zbudować coś,
co pasuje do istniejącego standardu.
A to zaskakująco duża zmiana.

<!-- S49 -->
Więc gdzieś, właśnie teraz,
są maleńkie maszyny
okrążające Ziemię.
Zbudowane przez uczelnie,
zespoły badawcze,
firmy i studentów.

<!-- S50 -->
Niektóre niosą kamery.
Niektóre mierzą promieniowanie.
Niektóre testują
zupełnie nową technologię.
A niektóre to tylko eksperymenty
z jednym pytaniem:
"czy uda nam się sprawić,
żeby to działało w kosmosie?"

<!-- S51 -->
I właśnie to sprawia,
że budowanie własnego satelity
jest tak fascynujące.
Bo odległość
między tobą a kosmosem
to już nie rakieta.
To może być...
dziesięciocentymetrowe pudełko.
I bardzo, bardzo
długa lista kontrolna.
