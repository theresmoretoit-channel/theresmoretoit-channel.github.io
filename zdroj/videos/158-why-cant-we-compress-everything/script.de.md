<!-- S01 -->
Das hier sind alle Skripte,
die je für diesen Kanal entstanden sind.
158 Videos,
fast anderthalb Millionen Bytes Text.

<!-- S02 -->
Jagen Sie sie durch ein ganz normales Packprogramm
namens gzip.
Heraus kommt etwas mehr als ein halbes Megabyte.
Fast zwei Drittel weg.

<!-- S03 -->
Und dabei geht nichts verloren.
Entpacken Sie die Datei,
und jedes Skript ist wieder da,
Buchstabe für Buchstabe.

<!-- S04 -->
Jetzt komprimieren Sie sie noch einmal.

<!-- S05 -->
Sie wird größer.
98 Bytes größer.

<!-- S06 -->
Ein drittes Mal.
98 Bytes größer.
Ein viertes.
Wieder 98.

<!-- S07 -->
Die erste Runde wirft zwei Drittel weg.
Die zweite findet überhaupt nichts.
Warum können wir also nicht einfach weiter komprimieren?

<!-- S08 -->
Schauen wir in diese zweite Datei.
gzip hat nichts komprimiert.
Es hat die Daten unverändert übernommen,
in sechzehn Blöcken.

<!-- S09 -->
Jeder Block bekam ein Etikett von fünf Bytes.
Dazu ein kleiner Header und ein Footer,
und es sind genau 98.

<!-- S10 -->
Wenn ein Packprogramm nichts zum Entfernen findet,
speichert es die Daten so, wie sie sind,
und ergänzt nur, was es zum Entpacken braucht.

<!-- S11 -->
Warum hat die zweite Runde also nichts gefunden?
Und würde ein klügeres Programm etwas finden?

<!-- S12 -->
Ein Text wie dieser steckt voller Wiederholungen.
Dieselben Wörter, dieselben Wendungen,
dieselben kleinen Szenenmarken
am Anfang jeder Szene.

<!-- S13 -->
1977 veröffentlichten Jacob Ziv und Abraham Lempel
einen einfachen Trick.
Eine Wiederholung nicht noch einmal schreiben,
sondern dorthin zurückverweisen, wo sie stand.

<!-- S14 -->
Gehen Sie 300 Zeichen zurück
und kopieren Sie die nächsten zwölf.
Ein paar Bytes statt zwölf.

<!-- S15 -->
Der zweite Trick:
häufigen Buchstaben kurze Codes geben
und seltenen lange.

<!-- S16 -->
1951 konnte David Huffman,
Doktorand am MIT,
entweder die Abschlussprüfung schreiben
oder stattdessen eine Hausarbeit.

<!-- S17 -->
Robert Fano hatte die Aufgabe gestellt,
den effizientesten Code
genau dieser Art zu finden.

<!-- S18 -->
Monatelang kam Huffman nicht weiter.
Er gab auf
und fing an, für die Prüfung zu lernen.
Dann kam ihm die Idee.

<!-- S19 -->
Nehmen Sie die zwei seltensten Symbole,
fassen Sie sie zu einem zusammen
und wiederholen Sie das, bis nur noch ein Baum übrig ist.

<!-- S20 -->
Später nannte er es
„den einzigartigsten Moment meines Lebens“.

<!-- S21 -->
Fano hatte den Studenten nicht verraten,
dass er sich selbst daran abgemüht hatte,
und Claude Shannon ebenso.

<!-- S22 -->
Huffmans Code schlug die Methoden der beiden.
Und man kann beweisen,
dass kein Code dieser Art besser ist.

<!-- S23 -->
Anfang der 1990er-Jahre
kombinierte Phil Katz beide Tricks
für ZIP-Dateien.
gzip nutzt dieselbe Methode.

<!-- S24 -->
Die erste Runde hat schon aufgebraucht,
was gzip an Mustern finden kann.

<!-- S25 -->
Mit dem Rest kann es nichts mehr anfangen.
Für gzip sieht er aus wie Rauschen.

<!-- S26 -->
Aber ein klügeres Programm
könnte Muster sehen, die gzip übersehen hat.
Könnte irgendein Programm eines Tages
alles verkleinern, was Sie ihm geben?

<!-- S27 -->
Nein.
Und Sie müssen nicht wissen, wie es funktioniert,
um sich da sicher zu sein.

<!-- S28 -->
Nehmen Sie alle Dateien,
die genau drei Bit lang sind.
Davon gibt es acht.

<!-- S29 -->
Zählen Sie jetzt alle kürzeren.
Vier Dateien mit zwei Bit,
zwei mit einem Bit
und eine leere Datei.

<!-- S30 -->
Sieben.

<!-- S30b -->
Acht Dateien und sieben kürzere Plätze,
um sie unterzubringen.

<!-- S31 -->
Würde jede davon kürzer,
müssten sich zwei einen Platz teilen.
Und wenn Sie sie dann entpacken:
Welche war gemeint?

<!-- S32 -->
Das nennt man das Schubfachprinzip,
und es gilt für jede Länge.
Kürzere Dateien gibt es immer eine weniger,
als man bräuchte.

<!-- S33 -->
Jedes Packprogramm, das jede Datei annimmt
und manche davon verkleinert,
muss also andere vergrößern.
Nicht, weil es schlecht geschrieben ist.
Sie können einfach nirgendwo anders hin.

<!-- S34 -->
Diese 98 Bytes
sind der Preis, den gzip dafür zahlt.

<!-- S35 -->
Nehmen Sie ein beliebiges Packprogramm.
Von allen Dateien einer bestimmten Größe
kann es weniger als eine
von 250 auch nur um ein einziges Byte verkleinern.

<!-- S36 -->
Kompression funktioniert trotzdem,
weil die Dateien, die wir erzeugen, nicht zufällig sind.
Es sind Texte, Bilder und Programme,
voller Muster.

<!-- S37 -->
Das hat Leute nicht davon abgehalten,
mehr zu versprechen.

<!-- S38 -->
1992 kündigte WEB Technologies
eine Software an, die angeblich
fast beliebige Daten unter ein Kilobyte presst.
Sogar ihre eigene Ausgabe,
immer und immer wieder.

<!-- S39 -->
Der Vizepräsident sagte, die Methode
sei „nicht den Gesetzen
der Informationstheorie unterworfen“.
Das Produkt kam nie auf den Markt.

<!-- S40 -->
Wie werden Fotos und Musik dann
so viel kleiner?
Sie halten sich gar nicht an diese Regel.

<!-- S41 -->
Ein JPEG kommt nicht identisch zurück.
Es kommt ähnlich genug zurück.
Details, die Ihr Auge nicht vermisst,
werden endgültig weggeworfen.

<!-- S42 -->
Zoomen Sie hinein,
und Sie sehen, wo sie geblieben sind.

<!-- S43 -->
Das ist verlustbehaftete Kompression,
und das ist ein ganz anderes Spiel.
In diesem Video geht es um die andere Art.
Jedes Bit zurück, exakt.

<!-- S44 -->
Und Dateien, die tatsächlich Muster haben:
Wie klein können die werden?
Gibt es eine Untergrenze?

<!-- S45 -->
Die gibt es.
Sie wurde 1948 gefunden,
im selben Artikel, auf dem unser Video
über fehlerkorrigierende Codes beruht.

<!-- S46 -->
Dort zeigte Claude Shannon,
wie zusätzliche Redundanz eine Nachricht schützt.
Hier rechnete er aus,
wie viel davon man wegnehmen kann.

<!-- S47 -->
Seine Antwort war eine Zahl,
die er Entropie nannte:
wie schwer es ist zu erraten,
was als Nächstes kommt.

<!-- S48 -->
Kein verlustfreier Code kann diese Zahl unterbieten,
im Durchschnitt.
Aber man kann ihr
beliebig nahe kommen.

<!-- S49 -->
Wie unvorhersehbar ist Englisch also?
1951 maß Shannon es
mit einem Spiel.

<!-- S50 -->
Er gab jemandem einen Textabschnitt,
den die Person nie gesehen hatte,
und ließ sie ihn erraten,
Buchstabe für Buchstabe.

<!-- S51 -->
War ein Tipp falsch,
riet sie noch einmal,
bis sie richtig lag.

<!-- S52 -->
Menschen erwiesen sich als sehr gut darin.
Mit hundert Buchstaben Kontext
kam Englisch auf etwa ein Bit
pro Buchstabe.

<!-- S53 -->
Ein Computer speichert jeden Buchstaben
in acht Bit.
Ein menschlicher Leser braucht etwa eins.

<!-- S54 -->
Diesen Spielraum nutzt die Kompression.
gzip brachte die Skripte des Kanals
auf unter drei Bit pro Zeichen.

<!-- S55 -->
Wie nah an ein Bit
kommt also eine Maschine?

<!-- S56 -->
Genau dafür gibt es einen Preis.
Er heißt Hutter Prize,
und seit 2020 ist die Aufgabe eine einzige Datei:
ein Gigabyte der englischen Wikipedia.

<!-- S57 -->
gzip verkleinert sie auf ein Drittel.
Die besten gängigen Packprogramme
auf etwa ein Fünftel.

<!-- S58 -->
Der Rekord vom Juli 2026
liegt bei etwas über hundert Millionen Bytes.
Ein Zehntel.

<!-- S59 -->
Und der Dekompressor zählt mit.
Seine Größe geht in die Summe ein,
man kann Wikipedia also nicht
im Programm verstecken.

<!-- S60 -->
Der Fonds umfasst 500.000 Euro.
Jedes Prozent Verbesserung
bringt 5.000.

<!-- S61 -->
Marcus Hutter, der ihn finanziert, erklärt, warum:
„Gut komprimieren zu können,
hängt eng damit zusammen,
intelligent zu handeln.“

<!-- S62 -->
Denn die Programme an der Spitze
suchen nicht nach Wiederholungen.
Sie treffen Vorhersagen.

<!-- S63 -->
Vor jedem Zeichen
schätzen sie, wie wahrscheinlich
jedes mögliche nächste Zeichen ist.
Ein guter Tipp kostet nur einen Bruchteil eines Bits.

<!-- S64 -->
Es ist Shannons Ratespiel,
gespielt von einer Maschine.
Die besten Spieler nutzen heute neuronale Netze,
trainiert darauf, vorherzusagen, was als Nächstes kommt.

<!-- S65 -->
Das funktioniert sogar bei schon komprimierten Dateien.
2016 begann Dropbox, die JPEGs seiner Nutzer
mit einem besseren Prädiktor neu zu packen.
Im Schnitt über ein Fünftel kleiner.

<!-- S66 -->
Jede Datei kam Bit für Bit zurück,
und bis 2017
hatte das über 46 Petabyte gespart.
Das sind über 46.000 Terabyte.

<!-- S67 -->
Und dann sind da noch die Riesen.
2023 nutzten Forscher von DeepMind
ein großes Sprachmodell
als Packprogramm.

<!-- S68 -->
Bei kleinen Graustufen-Ausschnitten von Fotos
schlug es PNG:
48 Prozent der Originalgröße
gegen 58.

<!-- S69 -->
Bei Aufnahmen vorgelesener Sprache
schlug es FLAC:
21 Prozent gegen 30.

<!-- S70 -->
Aber da ist das Modell nicht mitgerechnet.
Zählt man seine Größe dazu,
fällt das Ergebnis
140-mal
größer aus als die Daten.

<!-- S71 -->
Ein Packprogramm, das größer ist als seine Daten,
hat nichts gespart.
Das Programm ist Teil der Beschreibung.

<!-- S72 -->
Und das bringt uns zum seltsamsten Teil.
Hier ist die erste Million Ziffern von π.

<!-- S73 -->
Geben Sie sie vier Packprogrammen.
Das beste bringt sie auf etwa
426.000 Bytes.

<!-- S74 -->
Jetzt geben Sie denselben Packprogrammen
eine Million zufällige Ziffern.
Dasselbe Ergebnis,
bis auf ein Zehntelprozent.

<!-- S75 -->
Aber π entsteht nicht zufällig.
Es folgt einer mathematischen Regel.
Hier ist ein Programm, das
jede einzelne dieser Million Ziffern ausgibt.

<!-- S76 -->
362 Bytes.
Über 2.000-mal kürzer als die Datei.

<!-- S77 -->
Die Packprogramme konnten
die mathematische Regel hinter π nicht sehen.
Sie sahen nur die Ziffern.

<!-- S78 -->
Eine Art, die Information
in Daten zu messen, ist die Frage:
Wie kurz kann ein Programm sein,
das sie trotzdem ausgibt?

<!-- S79 -->
Diese Länge nennt man
Kolmogorow-Komplexität,
nach einem der Männer, die sie beschrieben haben.

<!-- S80 -->
Die meisten Daten haben kein kurzes Programm.
Das ist wieder das Schubfachprinzip:
Es gibt nicht genug kurze Programme
für alle.

<!-- S81 -->
Für eine Million zufälliger Ziffern
gibt es sehr wahrscheinlich nichts Kürzeres.
π schon.

<!-- S82 -->
Warum also nicht einfach
das kürzeste Programm für jede Datei finden?
Weil bewiesen ist,
dass kein Algorithmus das
für jede Datei kann.

<!-- S83 -->
Jedes Programm liefert Ihnen eine Obergrenze.
Aber nichts kann Ihnen immer sagen,
ob es ein kürzeres gibt.
Sie wissen nie, ob Sie die Untergrenze erreicht haben.

<!-- S84 -->
gzip fand die Wiederholungen in den Skripten
und nichts weiter.
Es sieht Bytes,
nicht, was die Wörter bedeuten.

<!-- S85 -->
Um weiterzukommen, muss ein Programm
sie besser vorhersagen.
Und Text gut vorherzusagen
sieht allmählich sehr nach Verstehen aus.

<!-- S86 -->
Deshalb eine Frage an Sie.
Wenn ein Programm Wikipedia
kleiner pressen könnte als jedes andere,
würden Sie sagen, es versteht sie?
Schreiben Sie Ihre Antwort in die Kommentare.
