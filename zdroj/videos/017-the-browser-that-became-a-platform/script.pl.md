# Internet Explorer 6 — Przeglądarka, która stała się platformą

Tłumaczenie `script.md`. Te same znaczniki scen, ta sama liczba wierszy.
Wiersz = jedna fraza = jeden napis.

<!-- S01 -->
Wyobraź sobie, że jesteś programistą webowym
na początku lat dwutysięcznych.

Napisałeś
całkowicie sensowną stronę internetową.

<!-- S02 -->
Działa w Netscape.

Działa w Operze.

Działa w nowym Firefoksie.

A potem otwierasz ją
w Internet Explorerze.

Wszystko jest zepsute.

<!-- S03 -->
Układ się rozjechał.

Przyciski się przesunęły.

Obrazki PNG wyglądają fatalnie.

I jakimś cudem
jedno złamanie wiersza w HTML-u
zrobiło trzypikselową szparę.

<!-- S04 -->
Witaj w tworzeniu stron
w epoce Internet Explorera 6.

Ale tu zaczyna się ciekawa część.

Internet Explorer 6
nie był po prostu kiepską przeglądarką.

<!-- S05 -->
Microsoft próbował rozwiązać problemy,
które sieć naprawdę miała.

Miał tylko jedną ogromną przewagę
nad wszystkimi innymi.

Windows.

<!-- S06 -->
I ta przewaga w końcu pozwoliła mu
zmienić przeglądarkę
w coś znacznie większego
niż przeglądarka.

<!-- S07 -->
W połowie lat dziewięćdziesiątych
w sieci dominował
Netscape Navigator.

Microsoftowi się to nie podobało.

<!-- S08 -->
Internet Explorer został więc
dołączony do Windowsa
i udostępniony za darmo.

Kupowałeś komputer z Windowsem.

Internet Explorer już tam był.

Nic do pobierania.

Nic do płacenia.

<!-- S09 -->
A co najważniejsze,
Microsoft kontrolował
system operacyjny.

Niedługo po roku 2000
Internet Explorer miał
ponad dziewięćdziesiąt procent
rynku przeglądarek.

<!-- S10 -->
Internet Explorer 6 pojawił się
w 2001 roku,
razem z Windowsem XP.

I przez chwilę wyglądało na to,
że Microsoft po prostu wygrał
wojnę przeglądarek.

<!-- S11 -->
Microsoft miał problem.

Sieć potrafiła bardzo niewiele.

HTML potrafił pokazać dokument.

CSS potrafił go ostylować.

JavaScript potrafił go ożywić.

<!-- S12 -->
I na tym koniec.

Cokolwiek bardziej skomplikowanego
uderzało prosto
w granice przeglądarki.

<!-- S13 -->
A gdybyś chciał zeskanować dokument?

Albo porozmawiać z kartą chipową?

Albo z jakimś
sprzętem w Windowsie?

<!-- S14 -->
Przeglądarka tak naprawdę
tego nie potrafiła.

Microsoft wymyślił więc rozwiązanie.

ActiveX.

<!-- S15 -->
Podstawowy pomysł był prosty.

Po co ograniczać aplikację webową
do tego, co potrafi przeglądarka?

Niech po prostu użyje
natywnych komponentów Windowsa.

<!-- S16 -->
I nagle strona internetowa
potrafiła rzeczy,
o których zwykłemu HTML-owi
nawet się nie śniło.

<!-- S17 -->
Dziś ActiveX brzmi przerażająco.

I słusznie.

Komponent ActiveX mógł sięgnąć
do plików, do aplikacji,
do sprzętu
i do systemu operacyjnego.

<!-- S18 -->
Z dzisiejszej perspektywy bezpieczeństwa
brzmi to kompletnie szaleńczo.

Ale na początku lat dwutysięcznych
miało to pełny sens
w zastosowaniach firmowych.

<!-- S19 -->
Firmy nie chciały
ładnej przeglądarki dokumentów.

Chciały aplikacji.

Chciały stron internetowych,
które zachowują się
niemal jak program na pulpicie.

<!-- S20 -->
I Microsoft dał im dokładnie to.

Nawet sam Windows Update
pierwotnie opierał się na ActiveX,
żeby sprawdzić system
i ustalić, które aktualizacje
są potrzebne.

<!-- S21 -->
ActiveX nie był więc po prostu
głupim błędem.

Był wczesną próbą
zmienienia przeglądarki
w platformę aplikacyjną.

<!-- S22 -->
I w tym sensie Microsoft
naprawdę wyprzedzał swoje czasy.

Problemem było to, ile władzy
dał tej platformie.

<!-- S23 -->
ActiveX nie był
jedynym rozszerzeniem Microsoftu.

Był VBScript.

Był DHTML.

A nawet CSS expression.

Tak.

<!-- S24 -->
Internet Explorer potrafił wykonać
JavaScript prosto wewnątrz CSS-a.

Dało się napisać coś takiego.

<!-- S25 -->
To było absurdalne.

A czasem także
zaskakująco użyteczne.

I nic z tego nie miało gwarancji,
że zadziała gdziekolwiek indziej.

<!-- S26 -->
Microsoft nie po prostu
wdrażał sieć.

Microsoft rozszerzał sieć
we własnym kierunku.

A mając dziewięćdziesiąt procent
rynku,
miał dość władzy,
żeby mu to uszło.

<!-- S27 -->
Jednym z najsłynniejszych przykładów
był model pudełkowy w CSS.

Model standardowy mówił,
że jeśli element
ma 200 pikseli szerokości,
20 pikseli dopełnienia
i 5 pikseli obramowania,

<!-- S28 -->
to całkowita szerokość
wynosi 250 pikseli.

<!-- S29 -->
Starsze wersje Internet Explorera
czytały to inaczej.

W trybie quirks zadeklarowana szerokość
mogła obejmować dopełnienie
i obramowanie.

<!-- S30 -->
Niekoniecznie był to
szalony sposób myślenia o szerokości.

Dziś zresztą często sami
prosimy dokładnie o takie zachowanie.

Nazywa się border-box.

<!-- S31 -->
Prawdziwym problemem było to,
że różne przeglądarki
zachowywały się różnie.

A to znaczyło,
że programistę musiało to obchodzić.

Bardzo.

<!-- S32 -->
Istniało coś o nazwie hasLayout.

Nie była to zwykła właściwość CSS.

Nie należała do standardu.

Ale decydowała o tym,
jak Internet Explorer
rozmieszcza elementy.

<!-- S33 -->
A zepsuty układ dawało się czasem
tajemniczo naprawić,
dodając jeden jedyny wiersz.

zoom: 1

Dlaczego?

Bo zoom: 1 potrafił uruchomić
wewnętrzny mechanizm hasLayout.

<!-- S34 -->
Były problemy
z przezroczystością PNG.

Były problemy z elementami select,
które wyświetlały się nad
absolutnie pozycjonowanymi menu,
bez względu na to, jak wysoko
ustawiłeś z-index.

<!-- S35 -->
Tworzenie stron nie polegało tylko
na wykonaniu własnego projektu.

Polegało na nauczeniu się błędów
konkretnego silnika przeglądarki.

<!-- S36 -->
Kolejny wspaniały przykład.

Białe znaki.

A za to Internet Explorer
nawet nie odpowiadał.

Dało się wstawić dwa obrazki
tuż obok siebie
w kodzie strony,
bez niczego pomiędzy znacznikami,
i dostać jeden wynik.

<!-- S37 -->
Potem ktoś ładnie formatował HTML
i dawał każdy znacznik do własnego wiersza.

I nagle między obrazkami
pojawiała się kilkupikselowa szpara.

Złamanie wiersza zaczynało coś znaczyć.

<!-- S38 -->
Twój formater kodu
potrafił dosłownie zepsuć stronę.

A jeśli używałeś
starej wersji Visual Studio,
chętnie formatował ci HTML
sam z siebie.

Dziękujemy, Microsofcie.

<!-- S39 -->
Programiści zgromadzili
całą skrzynkę obejść.

Komentarze warunkowe.

<!-- S40 -->
A czasem zupełnie
dziwacznie wyglądający HTML,
którego jedynym celem było
zmuszenie Internet Explorera do porządku.

<!-- S41 -->
Nie pisałeś brzydkiego kodu dlatego,
że byłeś kiepskim programistą.

Pisałeś brzydki kod dlatego,
że przeglądarka cię do tego zmuszała.

<!-- S42 -->
Internet Explorer potrafił też
spektakularnie się wywalić i często zabierał
ze sobą wszystkie otwarte okna.

<!-- S43 -->
Co dało początek wspaniałej kategorii
biurowej rozrywki.

Hej, zobacz ten link.

I dwadzieścia okien Internet Explorera
znika.

<!-- S44 -->
To była sieć, zanim przeglądarki
dostały piaskownicę.

Dzisiejsza przeglądarka mówi tak.

Nie ufam tej stronie.

Odizoluję ją.

<!-- S45 -->
Internet Explorer 6
brzmiał raczej tak.

Jesteś stroną internetową?

Jasne.

Masz tu klucze do budynku.

<!-- S46 -->
Dlaczego programiści
w ogóle używali tych obejść?

Bo musieli.

<!-- S47 -->
Wyobraź sobie firmę
z pięciuset pracownikami.

Na każdym komputerze działa Windows XP.

Na każdym jest Internet Explorer.

<!-- S48 -->
Programista ma dwie możliwości.

Możliwość pierwsza.

Zrobić to pod Internet Explorera,
którego i tak wszyscy mają.

<!-- S49 -->
Możliwość druga.

Zrobić to pod każdą przeglądarkę,
przetestować wszystko wszędzie
i wytłumaczyć działowi IT,
po co wszystkim druga przeglądarka.

Odpowiedź zwykle była oczywista.

<!-- S50 -->
Nie wybierali
technologii Microsoftu dlatego,
że kochali Microsoft.

Wybierali to, co rozwiązywało
problem klienta.

A czasem ActiveX
był najlepszym dostępnym narzędziem.

<!-- S51 -->
W końcu ktoś miał dość.

Biblioteki JavaScriptu zaczęły
ukrywać różnice między przeglądarkami.

Jedną z najważniejszych
było jQuery.

<!-- S52 -->
Zamiast pisać
obsługę zdarzeń pod każdą przeglądarkę,
pisałeś jeden wiersz,
który działał wszędzie.

<!-- S53 -->
Zamiast ręcznie mocować się
z różnymi implementacjami AJAX-a,
używałeś wspólnej abstrakcji.

<!-- S54 -->
jQuery nie sprawiło,
że Internet Explorer zniknął.

Ale dzięki niemu dużo łatwiej było
udawać, że go nie ma.

A dla ówczesnych programistów webowych
to była wspaniała rzecz.

<!-- S55 -->
Pojawił się Firefox.

Opera rozwijała się dalej.

Przyszło Safari.

A Google w końcu wydało Chrome.

<!-- S56 -->
Wojny przeglądarek wróciły,
a tym razem
konkurencja wyglądała inaczej.

Silniki JavaScriptu
zrobiły się dramatycznie lepsze.

Pojawił się HTML5.

<!-- S57 -->
Sama przeglądarka zaczęła się uczyć
wszystkiego tego, do czego programiści
wcześniej potrzebowali wtyczek.

<!-- S58 -->
Wideo.

Dźwięk.

Canvas.

SVG.

WebGL.

WebSockets.

I wreszcie WebRTC.

Sieć stawała się
platformą aplikacyjną.

<!-- S59 -->
Czyli dokładnie tym,
co Microsoft próbował
osiągnąć z ActiveX.

Tyle że teraz działo się to
przez otwarte standardy.

<!-- S60 -->
Microsoft spróbował jeszcze raz.

Silverlight pozwalał budować
bogate aplikacje w przeglądarce
w C# i .NET.

Działał na nim nawet
wczesny streaming Netflixa.

<!-- S61 -->
Ale sieć nie chciała wtyczek na zawsze.

Apple odmówiło obsługi Flasha
na iPhonie.

I nagle przyszłość nie wyglądała tak.

Przeglądarka plus wtyczka.

Wyglądała tak.

Sama przeglądarka.

<!-- S62 -->
Silverlight zniknął.

Flash zniknął.

ActiveX zniknął.

A w końcu zniknął
także Internet Explorer.

<!-- S63 -->
I tu ta historia
robi się interesująca.

Bo Microsoft
nie mylił się całkowicie.

Przewidział poprawnie,
że przeglądarka stanie się
platformą aplikacyjną.

<!-- S64 -->
Próbował tylko dojść tam
przez technologie zamknięte.

Sieć dotarła do tego samego celu
przez standardy.

<!-- S65 -->
Przeglądarka wygrała.

Ale wygrała, stając się
czymś znacznie potężniejszym
niż przeglądarka
z 2001 roku.

<!-- S66 -->
Czy Microsoft był więc czarnym charakterem?

Właściwie nie.

I to właśnie czyni
tę historię ciekawszą.

<!-- S67 -->
Microsoft miał świetnych inżynierów.

Miał ogromne zasoby.

I zbudował wiele technologii,
które naprawdę wyprzedzały swoje czasy.

<!-- S68 -->
Ale Microsoft miał też
przytłaczającą pozycję na rynku.

A to stworzyło
niebezpieczną pokusę.

<!-- S69 -->
Skoro prawie każdy
używa twojej przeglądarki,
po co czekać na standardy?

Czemu po prostu nie wdrożyć
własnego rozwiązania?

Przez pewien czas to działało.

Dopóki reszta sieci nie nadrobiła.

<!-- S70 -->
Dziś Internet Explorera już nie ma.

Dawne wojny przeglądarek
wyglądają na odległą historię.

Ale spójrz
na dzisiejszy rynek przeglądarek.

Chrome.

Edge.

Opera.

Brave.

Vivaldi.

<!-- S71 -->
A wiele innych
opiera się na Chromium.

Różne produkty.

Często ten sam
silnik pod spodem.

<!-- S72 -->
Może więc zamieniliśmy to.

Jedną przeglądarkę, o której wszyscy musieli pamiętać.

Na to.

Jeden silnik, na którym wszyscy budują.

Nie brzmi to znajomo?

<!-- S73 -->
Bo dominujący silnik
nie decyduje tylko o tym,
jak wyświetlają się strony.

<!-- S74 -->
Wpływa na to, co budują programiści.

Które technologie stają się popularne.

I ostatecznie na to,
czym staje się sama sieć.

<!-- S75 -->
Jest jednak
jedna bardzo ważna różnica.

Dzisiejsza sieć opiera się
na otwartych standardach.

Firefox wciąż ma własny silnik.

Safari ma WebKit.

Chromium jest otwartoźródłowy.

<!-- S76 -->
A nowoczesne przeglądarki
aktualizują się same.

Jesteśmy bardzo daleko
od sytuacji
z 2003 roku.

<!-- S77 -->
Ale podstawowe pytanie zostaje.

Jak wielki wpływ
powinna mieć jedna firma
na platformę,
z której korzysta prawie każdy?

To pytanie,
które nigdy naprawdę nie zniknęło.

<!-- S78 -->
Czy Internet Explorer 6 był więc okropny?

Tak.

Czasem spektakularnie okropny.

<!-- S79 -->
Ale to nie cała historia.

Był też produktem swoich czasów.

<!-- S80 -->
Problem polegał na tym,
że Microsoft wygrał
wojny przeglądarek tak całkowicie,
że mógł dyktować zasady.

<!-- S81 -->
A zapłacili za to programiści webowi.

Nauczyli się tajemnic
hasLayout.

Odkryli, że zoom: 1
magicznie naprawia różne rzeczy.

I modlili się.

<!-- S82 -->
I w końcu Internet Explorer
stał się tym, co przez dwadzieścia lat
sam budował.

Przestarzałą platformą,
której nikt już nie chciał
utrzymywać.

<!-- S83 -->
Sieć nie odrzuciła
wizji Microsoftu.

Po prostu zbudowała
jej lepszą wersję.

A jeśli tamta epoka
ma nas czegoś nauczyć,
to właśnie tego.

<!-- S84 -->
Technologia nie staje się standardem
dlatego, że jest dobra.

<!-- S85 -->
Czasem staje się standardem dlatego,
że jedna firma ma dość władzy,
by wszyscy jej używali.

<!-- S86 -->
A czasem
dwadzieścia lat później
orientujemy się, że zrobiliśmy to znowu.
