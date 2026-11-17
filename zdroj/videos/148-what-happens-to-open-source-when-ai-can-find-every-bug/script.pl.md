<!-- S01 -->
948.
Tyle różnych sposobów znalazła sztuczna inteligencja,
żeby od środka przejąć komputer z Linuksem.

<!-- S02 -->
Bez kradzieży hasła. Bez włamania z zewnątrz.
Każdy zaczyna się od zwykłego użytkownika,
który nie ma żadnych specjalnych uprawnień,
a kończy na roocie,
koncie, które może wszystko.

<!-- S03 -->
OpenAI opublikowało wynik w listopadzie 2026 roku.
Cały przebieg kosztował
1,2 miliona dolarów w kredytach API.

<!-- S05 -->
To dane podane przez samo OpenAI,
opublikowane dzień przed tym,
jak firma wypuściła model, który je uzyskał,
i nikt z zewnątrz nie potwierdził pełnej liczby.
Ale setki zgłoszeń i łatek
zostały już wysłane.

<!-- S06 -->
Oto dlaczego to ma znaczenie nie tylko dla Linuksa.
Kod źródłowy Linuksa jest publiczny.
Każdy może go przeczytać.
Przez dziesięciolecia był to argument
za tym, że jest bezpieczny.

<!-- S07 -->
Skoro więc maszyna potrafi czytać publiczny kod
i zamieniać go w działające exploity na taką skalę,
to czy oprogramowanie nie powinno jednak trzymać kodu w tajemnicy?

<!-- S08 -->
Spójrzmy na oprogramowanie, które już to robi.
W kwietniu 2026 roku Microsoft naprawił
164 luki bezpieczeństwa
w swój comiesięczny dzień poprawek.
W październiku naprawił ich
1413.

<!-- S09 -->
W tym jednym miesiącu naprawił więcej
niż w jakimkolwiek całym wcześniejszym roku.
Ponad 1000 z tych poprawek dotyczyło Windowsa,
a Microsoft uprzedzał,
że to jego własne narzędzia AI napędzą ten wzrost.

<!-- S10 -->
Nie możesz bezpośrednio porównać tych dwóch liczb.
Firmy liczą w różny sposób,
a Microsoft przeszukiwał własny, prywatny kod.

<!-- S11 -->
Ale jedno to pokazuje.
Trzymanie kodu w tajemnicy
nie uchroniło go przed błędami.

<!-- S12 -->
Co więc naprawdę cię chroni?
Żeby na to odpowiedzieć,
musimy zobaczyć, jak działa ta maszyna,
bo na każdym jej etapie coś odpada.

<!-- S13 -->
Jądro Linuksa ma
ponad 40 milionów linii kodu.
Najpierw przeszły przez nie agenty zwiadowcze
i wybrały te części,
do których zwykły użytkownik naprawdę może dotrzeć.

<!-- S14 -->
Zostało około 7%.
To część, którą uznały za wartą ataku,
a nie losowa próbka,
więc nie możesz pomnożyć wyniku przez 14.

<!-- S15 -->
Następnie agenty analityczne przejrzały ten kod
i wypisały wszystko, co podejrzane.
2308 kandydatów
w 12 godzin.

<!-- S16 -->
Ale podejrzenie niczego nie dowodzi.
Inne agenty napisały więc programy testowe
i uruchomiły je na odizolowanych maszynach wirtualnych.
1724 błędy
okazały się prawdziwe.

<!-- S17 -->
Potem przyszła kosztowna część:
budowanie działających exploitów
przy włączonych standardowych zabezpieczeniach
zwykłego systemu desktopowego.
1169
dotarło do roota.

<!-- S18 -->
Pogrupuj je według luk, które wykorzystują,
a wyjdzie ci 948.

<!-- S19 -->
W raporcie jest jeden szczegół,
który trudno zapomnieć.
W jednym z wczesnych przebiegów
agenty zgłosiły 200 sukcesów.
Potem ludzie sprawdzili, jak do nich doszły.

<!-- S20 -->
Dwadzieścia z nich dotarło do roota
przez inny, nieznany błąd,
a nie ten, którego kazano im użyć.
Wysłane, żeby otworzyć jedne drzwi,
znalazły inne, o których nikt nie wiedział.

<!-- S21 -->
W próbce swoich exploitów
OpenAI wskazało dziesięć technik eksploatacji,
których zewnętrzni eksperci wcześniej nie widzieli.

<!-- S22 -->
W lipcu wcześniejszy model
znalazł 166 takich luk.
Po trzech miesiącach poprawek
nowszy model znalazł 948.
Błędy się nie skończyły.
Późniejszy przebieg znalazł ich znacznie więcej.

<!-- S23 -->
Jest jednak ważne ograniczenie.
Nic z tego nie włamie się do twojego komputera
przez internet.
Atakujący musi już być na maszynie,
jako zwykły użytkownik.

<!-- S24 -->
To mniej pocieszające, niż brzmi,
bo prawdziwe ataki często mają dwa kroki.
Najpierw trzeba się dostać do środka,
przez lukę w przeglądarce albo złośliwy plik z sieci.
Potem potrzebny jest root.
To jest właśnie ten drugi krok.

<!-- S25 -->
Rada OpenAI jest bezceremonialna.
W systemie bez najnowszych łatek
traktuj każde zwykłe konto jak roota,
przynajmniej wobec dobrze finansowanego atakującego.

<!-- S26 -->
Co więc zostaje
ze starego argumentu za otwartym kodem?
Pod koniec lat dziewięćdziesiątych
Eric Raymond ujął go w hasło:
„Przy dostatecznie wielu oczach wszystkie błędy są płytkie”.

<!-- S27 -->
Nazwał to prawem Linusa.
To piękna idea, ale kryje się w niej założenie:
że ktoś naprawdę patrzy.

<!-- S28 -->
W 2014 roku błąd nazwany Heartbleed
wyszedł na jaw w OpenSSL,
kodzie, który chronił ogromną część sieci.
Uważano, że narażonych jest
około pół miliona bezpiecznych serwerów.

<!-- S29 -->
Błąd tkwił w publicznym kodzie od dwóch lat.
Projekt dostawał
około 2000 dolarów rocznie z darowizn
i miał jednego programistę na pełny etat.

<!-- S30 -->
Każdy mógł go przeczytać.
Prawie nikt tego nie zrobił.

<!-- S31 -->
To zawsze była prawdziwa słabość open source.
Nie za dużo oczu patrzących na kod. Za mało.

<!-- S32 -->
I właśnie to zmienia AI.
Maszyna może skanować bez przerwy
i zbadać o wiele więcej kandydatów,
niż ludzki badacz dałby radę sam.
Stara obietnica wreszcie jest dotrzymywana,
dla wszystkich, łącznie z atakującymi.

<!-- S33 -->
Publiczny kod jest więc teraz naprawdę badany.
Czy ukrycie go pomaga?

<!-- S34 -->
Zamknięty program i tak musi działać,
więc jego kod maszynowy leży
na każdym komputerze, który go używa.
Narzędzia takie jak Ghidra zamieniają go z powrotem
w coś podobnego do kodu źródłowego.

<!-- S35 -->
Jest też klasyczna sztuczka.
Porównaj program
przed aktualizacją bezpieczeństwa i po niej.
To, co się zmieniło, pokazuje ci, gdzie była dziura.

<!-- S35b -->
To mówi atakującym, gdzie celować,
na długo zanim każdy system
zainstaluje aktualizację.

<!-- S36 -->
Anthropic wypróbował to na jądrze Windowsa,
na 21 lukach,
które Microsoft niedawno załatał,
bez kodu źródłowego.
Pierwsza awaria wywołana przez AI pojawiła się po 31 minutach.
W ciągu sześciu godzin miała ich 18.

<!-- S37 -->
Osiem stało się działającymi exploitami
zdolnymi przejąć pełną kontrolę nad maszyną,
po około 2000 dolarów za sztukę.

<!-- S38 -->
Ale to nie były nieznane błędy.
Łatki już wskazywały,
gdzie leżą problemy.
Znalezienie nowej luki od zera jest trudniejsze.

<!-- S39 -->
Tajność nadal więc coś kosztuje atakującego.
To próg zwalniający, a nie mur.
Jak wysoki jest ten próg?
Nie ma publicznie dostępnych danych.

<!-- S40 -->
A co z drugą stroną?
Co tak naprawdę daje ci otwartość?
Odpowiedź kryje się w drobnym szczególe
raportu OpenAI.

<!-- S41 -->
W ciągu dziesięciu dni tego skanowania i analizy
ponad 100 z tych luk w Linuksie
zostało już naprawionych albo miało być wkrótce,
przez innych ludzi.
O około 300 kolejnych
już dyskutowano publicznie.

<!-- S42 -->
Inni znajdowali te same błędy
w tym samym czasie.

<!-- S43 -->
Linus Torvalds opisał to już w maju.
Powiedział, że zgłoszenia z AI
sprawiły, że lista dyskusyjna jądra o bezpieczeństwie
stała się „niemal zupełnie nie do ogarnięcia”,
bo różni ludzie wciąż znajdowali
te same rzeczy tymi samymi narzędziami.

<!-- S44 -->
A jego rada brzmiała tak:
„Jeśli znalazłeś błąd za pomocą narzędzi AI,
to najpewniej ktoś inny też go znalazł”.

<!-- S45 -->
Zasady jądra mówią to teraz wprost.
Błąd znaleziony z pomocą AI trzeba traktować jak publiczny,
bo takie błędy wypływają
u kilku badaczy,
często tego samego dnia.

<!-- S46 -->
Pomyśl, co to oznacza
dla idei tajnego błędu.
Jeśli znalezienie go niewiele cię kosztowało,
innych też kosztowało niewiele.

<!-- S47 -->
W open source
każdy może przejrzeć zgłoszenie,
sprawdzić poprawkę i podważyć wynik.
W zamkniętym oprogramowaniu
zwykle musisz zaufać dostawcy.

<!-- S49 -->
Ale otwartość ma swoją cenę,
i to nie taką, jakiej byś się spodziewał.
Kusi, żeby powiedzieć,
że małego projektu nie stać na skanowanie.
Firmy od AI już oferują
opiekunom kodu darmowy dostęp.

<!-- S50 -->
Brakuje ludzi.
Jądro odnotowywało kiedyś
około 500 problemów bezpieczeństwa na wydanie.
W tym roku przekroczyło 1500.
Wiele z nich jest drobnych,
ale ktoś i tak musi je przejrzeć.

<!-- S51 -->
W styczniu projekt curl
zakończył swój płatny program bug bounty,
żeby przestać nagradzać zalew śmieciowych zgłoszeń.

<!-- S52 -->
Nawet dobre zgłoszenia to dopiero początek pracy.
Łatki wygenerowane przez AI wciąż wymagają przeglądu przez człowieka.
Niektóre wczesne poprawki dodawały zbędny kod
albo pomijały inne odmiany tego samego błędu.

<!-- S53 -->
Możesz kupić więcej skanowania.
Nie kupisz więcej ludzi,
którzy rozumieją dany fragment kodu tak dobrze.
Tu firma z opłacanym zespołem bezpieczeństwa
naprawdę ma przewagę.

<!-- S54 -->
I wtedy pojawia się ostatni problem.
Naprawione to nie to samo co zainstalowane.

<!-- S55 -->
W marcu 2017 roku
Microsoft załatał lukę w Windowsie.
Zamknięty kod, jeden dostawca, jeden system aktualizacji.
Dwa miesiące później
WannaCry przeszedł przez tę samą dziurę
do około 200 000 komputerów
w mniej więcej 150 krajach.

<!-- S56 -->
Ta łatka miała dwa miesiące, żeby się rozejść,
i to nie wystarczyło.
Atakujący może już nie dać ci dwóch miesięcy.
W tym samym badaniu Anthropic
AI wzięła publiczną poprawkę
silnika JavaScript w Firefoksie
i w niecałą godzinę miała działający exploit.

<!-- S57 -->
Na poprawioną wersję Firefoksa
trzeba było czekać jeszcze 18 dni.

<!-- S58 -->
Na tym polega niebezpieczeństwo publikowania poprawki.
Informacja może dotrzeć do atakujących
wcześniej niż aktualizacja do ciebie.

<!-- S59 -->
Poprawka w Linuksie ma długą drogę do przebycia,
od jądra do stabilnego wydania,
do twojej dystrybucji, do twojego urządzenia.
Telefon może czekać miesiącami albo nigdy się nie doczekać.

<!-- S60 -->
I zamknięte oprogramowanie też tego nie uniknie.
Właśnie to widzieliśmy: łatka Windowsa wystarczyła.
Każda aktualizacja jest teraz także mapą.

<!-- S60b -->
Dlatego aktualizuj wszystko,
komputer, telefon, nawet router,
i instaluj aktualizacje, gdy tylko się pojawią.
W miarę jak AI coraz lepiej zamienia poprawki w ataki,
każdy dzień zwłoki będzie znaczył więcej.

<!-- S61 -->
Czy więc open source wciąż jest bezpieczniejszy?
Szczerze mówiąc, nikt tego nie wie.
O ile publicznie wiadomo,
nikt nie przeprowadził tego samego testu po obu stronach
na tych samych zasadach.

<!-- S62 -->
To, co możemy powiedzieć, jest skromniejsze.
Ukrywanie kodu daje mniej niż kiedyś.
Pokazanie go pozwala każdemu sprawdzić pracę
i zrzuca jeszcze więcej tej pracy
na ludzi, którzy ten kod utrzymują.

<!-- S64 -->
Nawet jeśli AI nigdy nie znajdzie wszystkich błędów,
już zmieniła to, ile kosztuje ich szukanie.

<!-- S65 -->
Liczy się teraz to, jak długo dziura pozostaje otwarta
między chwilą, gdy ktoś ją znajdzie,
a chwilą, gdy zostanie zamknięta na twojej maszynie.

<!-- S66 -->
Mam więc dla ciebie pytanie.
Jeśli każdy może znaleźć każdy błąd,
wolisz ufać kodowi, który możesz przeczytać,
czy firmie, której płacą za jego naprawienie?
Napisz w komentarzach.
