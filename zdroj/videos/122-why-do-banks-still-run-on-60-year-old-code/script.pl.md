<!-- S01 -->
Dziewięćset dziewięćdziesiąt dziewięć funtów
i dziewięćdziesiąt dziewięć pensów.
Dodaj jeden pens.

<!-- S02 -->
Wynik to zero.

<!-- S03 -->
Żadnego komunikatu o błędzie. Żadnej awarii.
Tylko zero, po cichu zapisane na koncie.

<!-- S04 -->
W COBOL-u, gdy pole na wynik
jest za małe, żeby go pomieścić,
nadmiarowa cyfra może po prostu zniknąć.
Jeśli program nie poprosi o ostrzeżenie,
obliczenia toczą się dalej.

<!-- S05 -->
Nie zaokrągla też wyniku.
Dwa funty i trzydzieści cztery i pół pensa,
zapisane z dokładnością do pensa,
zamieniają się w dwa trzydzieści cztery.

<!-- S06 -->
Dopisz jedno słowo, ROUNDED,
a wyjdzie dwa trzydzieści pięć.

<!-- S07 -->
Ani jedno, ani drugie nie jest błędem.
To reguły.
A wiele banków na świecie
wciąż działa na takich regułach.

<!-- S08 -->
COBOL to język programowania
z 1959 roku.
Nie każdy program w nim napisany jest tak stary.
Ale język tak,
i jego nawyki też.

<!-- S09 -->
Dlaczego więc banki go nie zastąpiły?
Pieniądze mają.
Inżynierów też.

<!-- S10 -->
Żeby to sprawdzić, przyjrzymy się trzem prawdziwym przypadkom.
Bankowi, który próbował odejść od starego systemu,
bankowi, któremu się to udało,
i kryzysowi, za który wszyscy winili COBOL.

<!-- S11 -->
Ale najpierw: to zgubione pół pensa.

<!-- S12 -->
Powiedzmy, że przepisujesz ten program bankowy
na nowoczesny język.
Pewnie przy okazji poprawisz te reguły.
Przepełnienie staje się błędem.
Pół pensa zaokrągla się w górę.

<!-- S13 -->
Czyściej. Bezpieczniej.
I teraz, gdziekolwiek pojawi się pół pensa,
twój program nie zgadza się ze starym.

<!-- S14 -->
Nowoczesne języki potrafią liczyć dokładnie na liczbach dziesiętnych.
Java ma do tego specjalny typ.
Ale nawet tam
reguła zaokrąglania to kwestia wyboru.

<!-- S15 -->
Jedno popularne ustawienie zaokrągla połówkę w górę:
dwa trzydzieści pięć.
Inne zaokrągla do najbliższej cyfry parzystej:
dwa trzydzieści cztery.
Oba są poprawne. Zgadza się tylko jedno.

<!-- S16 -->
A ze zwykłymi liczbami zmiennoprzecinkowymi,
których większość kodu używa domyślnie,
robi się jeszcze dziwniej.
Zero przecinek jeden plus zero przecinek dwa
to nie jest zero przecinek trzy.

<!-- S17 -->
Zastąpienie COBOL-a to więc nie tłumaczenie.
To znalezienie każdej takiej reguły
w milionach linii kodu
i zachowanie każdej dokładnie tak, jak była.

<!-- S18 -->
Jak on się tam w ogóle znalazł?

<!-- S19 -->
W maju 1959 roku
Departament Obrony USA
zwołał spotkanie w Pentagonie.
Przyszli producenci komputerów, agencje rządowe
i duże firmy,
wszyscy z tym samym problemem.

<!-- S20 -->
Każdy komputer miał własny język.
Program płacowy napisany na jedną maszynę
na innej był bezużyteczny.

<!-- S21 -->
Komitet zaprojektował wspólny język
dla biznesu.
Największy wpływ miał na niego FLOW-MATIC
zespołu Grace Hopper z Remington Rand.

<!-- S22 -->
A w grudniu 1960 roku
w zasadzie ten sam program w COBOL-u
zadziałał na dwóch komputerach
konkurencyjnych producentów.
O to właśnie chodziło.

<!-- S23 -->
Zaprojektowano go tak, żeby ludzie mogli go zrozumieć.
ADD PAYMENT TO ACCOUNT-BALANCE.
Pewnie zgadniesz, co to robi.

<!-- S24 -->
I przechowywał pieniądze tak, jak zapisują je ludzie:
jako cyfry dziesiętne.
Przecinka dziesiętnego
nie trzeba nawet przechowywać.
Gdzie ma stać, mówi opis pola:
ostatnie dwie cyfry to pensy.

<!-- S25 -->
W 1964 roku IBM wprowadził System/360.
Jego projekt obejmował instrukcje
do arytmetyki dziesiętnej.

<!-- S26 -->
I od tamtej pory IBM projektuje swoje komputery mainframe
tak, żeby zachowywały zgodność.
Wiele starszych programów wciąż może działać
na dzisiejszych maszynach
bez przepisywania.

<!-- S27 -->
Rzadko więc zdarzał się moment,
który zmusiłby kogokolwiek do zmiany.
Co roku kod dalej działał
i co roku zbierał kolejne reguły.
Nowe produkty, nowe podatki, nowe przepisy,
nowe wyjątki.

<!-- S28 -->
Nikt nie policzył, ile COBOL-a
wciąż działa na świecie.
Ale IBM twierdzi, że czterdzieści pięć
z pięćdziesięciu największych banków świata
wciąż używa jego komputerów mainframe.

<!-- S29 -->
A niektórzy właściciele policzyli.
W 2017 roku amerykańska Administracja
Ubezpieczeń Społecznych podała, że jej systemy mają
ponad sześćdziesiąt milionów linii COBOL-a.

<!-- S30 -->
W 2025 roku audytorzy rządu USA
wskazali jedenaście systemów federalnych,
które najbardziej wymagały wymiany.

<!-- S31 -->
Miały od dwudziestu trzech
do sześćdziesięciu lat,
a ich utrzymanie kosztowało około siedmiuset pięćdziesięciu
milionów dolarów rocznie.

<!-- S32 -->
Kod jest więc stary, jest wszędzie
i jest pełen reguł, których nikt nie spisał.
Na pewno więc groźne jest trzymanie się go.

<!-- S33 -->
Zobaczmy, co się dzieje,
kiedy bank odchodzi.

<!-- S34 -->
W 2018 roku brytyjski bank TSB
miał około pięciu milionów klientów
i problem.

<!-- S35 -->
Swoje systemy wynajmował
od Lloyds Banking Group,
konkurenta,
a opłaty miały mocno wzrosnąć.

<!-- S36 -->
TSB postanowił więc przenieść wszystko
na nową platformę,
zbudowaną przez swojego nowego właściciela,
hiszpański bank Sabadell.

<!-- S37 -->
Jeden weekend w kwietniu.
W niedzielę wieczorem
włączono nowy system.

<!-- S38 -->
W poniedziałek było około
dziewięciuset tysięcy prób logowania.
Udawało się tylko mniej więcej jedno logowanie
do bankowości internetowej na dziesięć.

<!-- S39 -->
Płatności nie przechodziły.
Niektórzy klienci się logowali
i widzieli cudze konta.

<!-- S40 -->
Najgorsze trwało około tygodnia.
Do normalnej pracy TSB wrócił
dopiero w grudniu.

<!-- S41 -->
Skutki kosztowały około
trzystu trzydziestu milionów funtów
w samym 2018 roku.
Regulatorzy dołożyli później
kary na prawie czterdzieści dziewięć milionów.

<!-- S42 -->
I tu robi się dziwnie.
Dane klientów dotarły nienaruszone.
Tak mówią oba oficjalne raporty.

<!-- S43 -->
Zawiodła nowa platforma wokół nich.
Dwa centra danych, każde skonfigurowane inaczej.
Wydajność przetestowana tylko na jednym z nich,
a wymagania obniżone,
kiedy testy nie wypadły pomyślnie.

<!-- S44 -->
I nie było odwrotu.
Gdy dane zostały przeniesione,
powrót do starego systemu był,
słowami regulatora,
„w zasadzie niemożliwy”.

<!-- S45 -->
TSB nie uciekał przed zepsutym systemem.
Porzucał taki, który działał,
ze względu na to, do kogo należał
i ile kosztował.
Niebezpieczne było właśnie odejście.

<!-- S46 -->
Czy więc odejście zawsze kończy się katastrofą?

<!-- S47 -->
W 2008 roku australijski Commonwealth Bank
postanowił wymienić systemy centralne,
które służyły mu
przez ponad czterdzieści pięć lat.

<!-- S48 -->
Plan: około pięciuset osiemdziesięciu
milionów dolarów australijskich
i cztery lata.

<!-- S49 -->
Zajęło to pięć.
Prasa szacowała później łączny koszt
na mniej więcej miliard sto milionów,
bo projekt się rozrastał.

<!-- S50 -->
Ale nie przeniósł wszystkiego
w jeden weekend.
Najpierw, w 2010 roku, poszły rachunki depozytowe.
Rachunki firmowe w 2011 roku,
a kredyty w 2012.

<!-- S51 -->
Każdy krok był czymś, co bank
mógł obserwować, sprawdzić i wyciągnąć z tego wnioski,
zanim przeszedł do następnego.

<!-- S52 -->
W końcu, jak twierdzi sam bank,
stał się pierwszym dużym bankiem w Australii
z bankowością w czasie rzeczywistym,
przez całą dobę.

<!-- S53 -->
Czyli da się.
Ale zobacz, czego to wymagało.
Pięciu lat, dużo wyższego rachunku
i cierpliwości.

<!-- S54 -->
Modernizacja to nie zakup.
To projekt
z własnym ryzykiem.

<!-- S55 -->
A teraz kryzys,
za który wszyscy winili COBOL.

<!-- S56 -->
Marzec 2020.
Gdy pandemia sparaliżowała New Jersey,
liczba nowych wniosków o zasiłek dla bezrobotnych skoczyła
z niecałych dziesięciu tysięcy tygodniowo
do ponad stu pięćdziesięciu pięciu tysięcy.

<!-- S57 -->
Szesnaście razy więcej,
w siedem dni.
Urząd pracy nie nadążał.

<!-- S58 -->
Na początku kwietnia gubernator
zaapelował o ochotników.
Nie tylko o medyków,
ale też o ludzi znających COBOL.
Stanowe systemy, jak mówił,
miały ponad czterdzieści lat.

<!-- S59 -->
Ta historia szybko się rozeszła.
Prastary kod załamał się
pod naporem pandemii.

<!-- S60 -->
Ale gdy stanowy audytor
zbadał to później,
nie znalazł żadnych dowodów
na to, że opóźnienia spowodowały
systemy komputerowe.

<!-- S61 -->
Niezależnie od tego dziennikarze, którzy przyjrzeli się
komunikatom o błędach, jakie widzieli ludzie,
wiele z nich powiązali ze stroną internetową,
napisanej w dużo nowszym języku, Javie.
Stary kod działający w tle pracował dalej.

<!-- S62 -->
Po co więc stan potrzebował programistów COBOL-a?
Bo Kongres zmieniał przepisy.
Nowe świadczenia, nowe kwoty,
nowe osoby uprawnione,
a każda zmiana musiała trafić
do kodu, i to szybko.

<!-- S63 -->
Problemem nie był wiek kodu.
Problemem było to, że mało kto umiał go zmieniać,
i że linie telefoniczne i personel
też były przeciążone.

<!-- S64 -->
Trzy przypadki.
Bank, który porzucił wciąż działający system,
a jego migracja się nie powiodła.
Bank, który odchodził ostrożnie
i odniósł sukces.
I kryzys, za który obwiniono stary kod,
a nikt nie potrafił wykazać, że to on był przyczyną.

<!-- S65 -->
To nie znaczy, że stare systemy nigdy nie zawodzą.
Zawodzą.
Robią się drogie,
ludzie, którzy je rozumieją, przechodzą na emeryturę,
a czekanie też ma swoją cenę.

<!-- S66 -->
Ale wiek łatwo zobaczyć,
a prawdziwe zagrożenia już nie.
Reguły, których nikt nie spisał.
Wiedza w głowach kilku osób.
I moment przełączenia.

<!-- S67 -->
Dlatego wiele banków nie wymienia
starego rdzenia za jednym zamachem.
Obudowują go.
Aplikacja w twoim telefonie jest nowa,
ale może rozmawiać z czymś
dużo starszym.

<!-- S68 -->
I wymieniają go kawałek po kawałku.
W 2004 roku Martin Fowler, autor piszący o oprogramowaniu,
nazwał to od figowca dusiciela,
rośliny lasów deszczowych, która obrasta drzewo,
aż sama potrafi się utrzymać.

<!-- S69 -->
Stary system dalej działa,
a nowy rośnie wokół niego,
zadanie po zadaniu,
aż nic już nie zależy od starego.

<!-- S70 -->
I tak wracamy do tego pół pensa.
Gdzieś jakiś program może go wciąż gubić,
bo ktoś tak postanowił
dziesiątki lat temu.
Żeby zastąpić ten program, trzeba o tym wiedzieć,
i o wszystkim podobnym.

<!-- S71 -->
To nie zawsze stary system
zawodzi.
Czasem zawodzi to, co go zastępuje.

<!-- S72 -->
Bo wymiana technologii
to nie to samo, co usunięcie ryzyka.
Czasem tylko przenosi ryzyko
na jeden kwietniowy weekend.

<!-- S73 -->
Mam więc dla ciebie pytanie.
Jeśli system działa od czterdziestu lat,
kiedy jest właściwy moment, żeby go wymienić?
A tobie zdarzyło się kiedyś samemu jakiś wymieniać?
Napisz w komentarzach.
