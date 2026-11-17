<!-- S01 -->
Stell dir vor, du schaltest einen Windows-PC ein
und findest keine Taskleiste, keinen Startknopf
und kein einziges Symbol auf dem Desktop.

<!-- S02 -->
Stattdessen gibt es oben eine schmale Leiste,
ein Menü, das überall aufgeht, wo du klickst,
und vier virtuelle Desktops nebeneinander.

<!-- S03 -->
Es sieht aus wie Linux.
Aber deine Programme, Treiber und Dateien
sind genau da, wo du sie gelassen hast.
Es ist immer noch Windows.

<!-- S04 -->
Nur der Desktop hat sich geändert.
Und der Schalter, der ihn ändert,
ist eine einzige Einstellung.

<!-- S05 -->
Windows speichert sie in der Registry,
in einem Wert namens Shell.
Auf fast jedem Windows-PC
steht dort explorer.exe.

<!-- S06 -->
Trag dort den Namen eines anderen Programms ein,
melde dich ab und wieder an,
und Windows startet stattdessen dieses Programm.
Was immer es zeichnet, wird dein Desktop.

<!-- S07 -->
Und das ist kein Trick, den jemand letztes Jahr entdeckt hat.
Schon 1990 hatte Windows 3.0 denselben Schalter
in einer einfachen Textdatei namens system.ini.
Eine Zeile: shell=progman.exe.

<!-- S08 -->
Änderte man diesen Namen,
erschien der Programm-Manager, das Fenster voller Symbolgruppen,
gar nicht erst.

<!-- S09 -->
Die Frage ist also nicht, ob Windows
einen anderen Desktop haben kann.
Das konnte es schon immer.
Die Frage ist, warum fast niemand je einen gesehen hat.

<!-- S10 -->
Fangen wir damit an, worauf diese Zeile eigentlich zeigt.
Die Taskleiste, die Desktopsymbole,
der kleine Infobereich neben der Uhr:
das alles ist ein einziges Programm, der Explorer.

<!-- S11 -->
Ja, derselbe Explorer,
mit dem du deine Dateien durchsuchst.
Er erledigt zwei Aufgaben,
und die meisten bemerken immer nur eine.

<!-- S12 -->
Diese zweite Aufgabe hat einen Namen: die Shell.
Sie ist die Oberfläche, die du bedienst.
Darunter liegen der Kernel, die Treiber
und die Dienste, die Windows am Laufen halten.

<!-- S13 -->
Keiner davon braucht eine Taskleiste.
Beende den Explorer im Task-Manager,
und Taskleiste und Symbole verschwinden...
aber der Editor, dein Browser,
jedes andere Fenster läuft weiter.

<!-- S14 -->
Starte ihn neu, und der Desktop ist wieder da.
Einen deutlicheren Beweis gibt es kaum,
dass der Desktop nur ein weiteres Programm ist.

<!-- S14b -->
Wenn du schon mal den Launcher
auf einem Android-Handy gewechselt hast,
kennst du eine ähnliche Idee.
Bei Android geht das ganz normal in den Einstellungen.
Windows hat den Mechanismus auch,
hat normalen Nutzern aber nie
einen einfachen Knopf dafür gegeben.

<!-- S15 -->
Drei Begriffe werden hier gern verwechselt.
Die Shell ist das, von wo aus du Dinge startest:
die Taskleiste, die Menüs, der Desktop.
Ein Fenstermanager steuert, wie Fenster
platziert, gestapelt und fokussiert werden.
Eine Desktopumgebung
verbindet das alles zu einer einheitlichen Oberfläche.

<!-- S16 -->
Unter Linux lassen sich diese Teile
auf viele verschiedene Arten kombinieren.
Unter Windows ersetzt ein Austausch der Shell
weder die Fensterverwaltung des Systems
noch die Art, wie Anwendungen ihre Fensterrahmen zeichnen.

<!-- S17 -->
Das hielt die Leute nicht davon ab, es zu versuchen.
Anfang der Neunziger konntest du in einen Laden gehen
und einen Ersatz für den Programm-Manager kaufen.

<!-- S18 -->
Norton Desktop for Windows
gab dir einen eigenen Desktop,
eigene Dateiwerkzeuge und einen eigenen Launcher,
und darunter lief dasselbe Windows.

<!-- S19 -->
Manche Computerhersteller tauschten ihn aus,
bevor der Kunde den Rechner überhaupt einschaltete.
Packard Bells Navigator empfing Käufer
mit einem Haus, durch das man Raum für Raum gehen konnte.

<!-- S20 -->
Dann übergab Windows 95 die Aufgabe an den Explorer,
und die Zeile in der system.ini
wurde einfach zu explorer.exe.
Der Schalter blieb genau da, wo er war.

<!-- S21 -->
Ende der Neunziger
wuchs um diesen Schalter eine ganze Community.
Das bekannteste Projekt war LiteStep.

<!-- S22 -->
Sein Aussehen lieh es sich von AfterStep,
einem Unix-Fenstermanager nach dem Vorbild von NeXTSTEP,
von der Firma, die Steve Jobs nach seinem Weggang von Apple gründete.

<!-- S23 -->
LiteStep hatte kein Startmenü, außer du hast dir eins gebaut.
Alles war ein Modul:
hier ein Dock, da eine Uhr,
ein Menü, das überall aufging, wo du rechts geklickt hast.

<!-- S24 -->
Seine Themes wurden geteilt wie Hintergrundbilder.
Manche sahen futuristisch aus.
Manche wie eine Unix-Workstation.
Manche ließen fast gar nichts auf dem Bildschirm übrig.

<!-- S25 -->
Blackbox for Windows ging den umgekehrten Weg.
Es kopierte Blackbox, einen minimalistischen Unix-Fenstermanager,
bis hin zu einem einzigen schlichten Menü
und einer schmalen Werkzeugleiste.

<!-- S26 -->
Sein Nachfolger bbLean
hielt diese Idee unter Windows 2000 und XP am Leben.

<!-- S27 -->
Emerge Desktop zerlegte die Shell in einzelne Teile:
einen Launcher, einen Infobereich, eine Taskliste,
jeweils ein kleines Programm, das du behalten oder weglassen konntest.

<!-- S28 -->
Warum dieser ganze Aufwand?
Zum Teil, weil der Look von XP
leicht zu erkennen und schwer zu ändern war.
Designs änderten Farben und Schaltflächen.
Das Layout blieb.

<!-- S29 -->
Zum Teil wegen des Arbeitsspeichers.
Auf einem Rechner mit 128 Megabyte
versprach eine schlankere Shell mehr Platz
für alles andere.

<!-- S30 -->
Und zum Teil wegen Linux.
Dort war es normal, sich seinen Desktop auszusuchen,
und manche Windows-Nutzer wollten
dieselbe Wahl.

<!-- S31 -->
Die meisten dieser Projekte gibt es nicht mehr.
Die letzte Version von LiteStep war eine Vorabversion
von 2014, immer noch als Alpha markiert.
Auch Emerge Desktop und SharpEnviro wurden eingestellt.

<!-- S32 -->
Das lag zum Teil an den kleinen Freiwilligenteams.
Aber auch Windows hat sich verändert.
Im Lauf der Jahre wurde sein Desktop viel mehr
als eine einzelne ausführbare Datei.

<!-- S33 -->
Die Desktop-Oberfläche verteilt sich heute
auf mehrere Prozesse,
Systemkomponenten und paketierte Anwendungen.
Sogar das Startmenü läuft als eigenes Programm.

<!-- S34 -->
Den Explorer zu ersetzen heißt nicht,
alles zu ersetzen, woraus die moderne Windows-Oberfläche besteht.
Und das ist ein Grund, warum
ein vollständiger alternativer Desktop
heute schwerer zu bauen ist als früher.

<!-- S35 -->
Und trotzdem funktioniert es noch.
Cairo Desktop, ein Open-Source-Projekt,
läuft heute unter Windows 11.

<!-- S36 -->
Es bringt eine eigene Menüleiste oben mit,
eine eigene Taskleiste
und Ordner, die du als Stapel an die Leiste heften kannst.

<!-- S37 -->
Es kann neben dem Explorer laufen
oder die Rolle der Shell übernehmen.
In diesem zweiten Modus
können Teile von Windows 11 Probleme machen,
darunter die Einstellungen und die Windows-Sicherheit.

<!-- S38 -->
Seelen UI geht anders vor.
Es ersetzt den Explorer nicht.
Es blendet die Taskleiste aus und bringt eigene Teile mit:
ein Dock, eine Leiste, Widgets
und einen Fenstermanager, der deine Fenster kachelt.

<!-- S39 -->
Das Ergebnis muss überhaupt nicht nach Windows aussehen.
Aber darunter läuft der Explorer weiter.
Es ist ein neues Gesicht, keine neue Shell.

<!-- S40 -->
Und Microsoft?
Microsoft hat dafür tatsächlich eine offizielle Funktion.
Sie heißt Shell Launcher
und ist für Geräte wie Kioske gedacht.

<!-- S41 -->
Du hast so etwas wahrscheinlich schon benutzt,
ohne es zu wissen.
Den Fahrkartenautomaten am Bahnhof.
Eine Selbstbedienungskasse. Einen Geldautomaten.

<!-- S42 -->
Viele davon sind Windows-PCs,
deren ganze Shell eine einzige Anwendung ist.
Ein Administrator legt das Programm fest,
und nach der Anmeldung ist dieses Programm der ganze Desktop.

<!-- S43 -->
Aber es gibt ihn nur
in den Editionen Enterprise, Education
und IoT Enterprise.

<!-- S44 -->
Und der ältere Mechanismus in der Registry
ist immer noch Teil von Windows.
Microsoft hat daraus nur nie
eine normale Desktop-Einstellung
für gewöhnliche Nutzer gemacht.

<!-- S45 -->
Warum also scheint Windows nur einen Desktop zu haben?
Nicht, weil es keinen anderen haben könnte.
Sondern weil der Desktop das Produkt ist.

<!-- S46 -->
Unter Linux hast du beim Desktop die Wahl.
Manche Distributionen lassen dich einen aussuchen,
während du noch installierst.
KDE Plasma, GNOME, Xfce, Cinnamon...

<!-- S47 -->
Unter Windows ist der Desktop das, was Microsoft zeigt,
in jeder Werbung, auf jedem Screenshot
und auf jeder Supportseite.
Ein Desktop bedeutet eine Anleitung
für mehr als eine Milliarde Rechner.

<!-- S48 -->
Das ist ein echter Vorteil.
Wenn etwas kaputtgeht,
sieht der Bildschirm in der Anleitung aus wie deiner.
Der Preis ist, dass die meisten nie erfahren,
dass sie eine Wahl hatten.

<!-- S49 -->
Die Leute haben den Windows-Desktop ausgetauscht,
bevor es Windows 95 überhaupt gab.
Sie bauten Docks, karge Menüs
und Desktops, die völlig anders aussahen als alles andere.

<!-- S50 -->
Die meisten dieser Projekte sind verschwunden.
Die Idee nicht.
Unter jeder Taskleiste, die du je angeklickt hast,
steht immer noch diese eine Einstellung und wartet auf einen anderen Namen.

<!-- S51 -->
Der Desktop ist nur ein weiteres Stück Software.
Und Software lässt sich ersetzen.

<!-- S52 -->
Also, eine Frage an dich:
Wenn Windows dich deinen Desktop
bei der Installation wählen ließe, wie manche Linux-Distributionen,
würdest du wechseln oder bei dem bleiben, den du kennst?
Schreib's mir in die Kommentare.
