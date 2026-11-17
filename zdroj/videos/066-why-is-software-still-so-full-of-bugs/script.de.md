<!-- S01 -->
Alle paar Tage schafft es ein schwerer Bug
in die Nachrichten.
Ein Bug, mit dem man den Login überspringt.
Ein Bug, der private Daten preisgibt.
Ein Bug, der einem Angreifer Ihren Computer ausliefert.

<!-- S02 -->
Mal ist es Windows. Mal Linux.
Ein Browser, eine Datenbank, ein Clouddienst...
oder eine kleine Bibliothek,
auf die sich Millionen Entwickler verlassen.

<!-- S03 -->
Und die Reaktion ist fast immer dieselbe.
Wie konnten die Programmierer das übersehen?

<!-- S04 -->
Das sind Profis.
Sie haben Code-Reviews, automatische Tests,
Sicherheitsaudits, Fuzzing...
und trotzdem kommen immer neue Bugs.

<!-- S05 -->
Kann man also überhaupt
komplexe Software ohne Bugs schreiben?

<!-- S06 -->
Fangen wir mit einer Zahl an.
Stellen Sie sich ein Programm mit nur hundert Einstellungen vor,
jede davon entweder an oder aus.

<!-- S07 -->
Hundert einfache Ja-Nein-Entscheidungen.
Wie viele Kombinationen sind das?

<!-- S08 -->
Zwei hoch hundert.
Das ist ungefähr eine Million Billionen Billionen.

<!-- S09 -->
Stellen Sie sich jetzt vor, Sie könnten
eine Milliarde Kombinationen pro Sekunde testen.
Und Sie hätten beim Urknall angefangen.

<!-- S10 -->
Bis heute hätten Sie
etwa eine von dreitausend Kombinationen getestet.

<!-- S11 -->
Und hundert Schalter sind gar nichts.
Ein echtes Programm hat Millionen davon.
„Einfach alles testen“
ist also nicht teuer. Es ist unmöglich.

<!-- S12 -->
Und diese Schalter sind nichts Exotisches.
Nehmen wir eine der einfachsten Sachen,
die ein Programm überhaupt macht.
Ein Nutzer ruft sein Konto über dessen Nummer ab.
Wir suchen es in der Datenbank.
Wir schicken es zurück.

<!-- S13 -->
Aber was, wenn es den Nutzer nicht gibt?
Was, wenn jemand Text statt einer Zahl schickt?
Oder eine negative Zahl? Oder eine riesige?

<!-- S14 -->
Was, wenn diese Person es gar nicht sehen darf?
Was, wenn jemand das Konto löscht,
genau in dem Moment, in dem wir es laden?
Was, wenn dieselbe Anfrage zweimal ankommt?

<!-- S15 -->
Jede dieser Fragen ist einfach.
Das Problem ist, wie sie zusammenspielen.
Jede ist ein weiterer Schalter.

<!-- S15b -->
Übrigens, wenn Ihnen solche Videos
gefallen, können Sie den Kanal abonnieren.

Das hilft dem Kanal wirklich.

<!-- S16 -->
Und der Computer nimmt uns das nicht ab.
Er tut genau das, was wir ihm sagen.
Nicht das, was wir gemeint haben.

<!-- S17 -->
Deshalb haben wir Programmiersprachen erfunden.
Mit ihnen beschreiben wir komplexe Dinge,
ohne an jedes Detail denken zu müssen.

<!-- S18 -->
Aber manche nehmen uns weniger ab,
als man hoffen würde.
Nehmen wir C. Es ist schnell, es ist einfach,
und es gibt Ihnen enorme Kontrolle über den Speicher.

<!-- S19 -->
Sie können also das hier schreiben.
Wir reservieren Platz für sechzehn Zeichen.
Dann sagen wir: Kopiere die Eingabe hierher.

<!-- S20 -->
Was, wenn die Eingabe
fünfhundert Zeichen lang ist?
C fragt nicht nach.
Es schreibt einfach über das Ende hinaus weiter.

<!-- S21 -->
Und was liegt direkt hinter diesen sechzehn Zeichen?
Oft etwas sehr Wichtiges.

<!-- S22 -->
Wenn ein Programm eine Funktion aufruft,
notiert es sich, wohin es zurückkehren soll,
sobald die Funktion fertig ist.
Eine Rücksprungadresse.
In einem klassischen Speicherlayout liegt sie
nicht weit hinter dem Ende unseres Puffers.

<!-- S23 -->
Also schickt ein Angreifer eine Eingabe
von genau der richtigen Länge.
Zuerst seine eigenen Befehle.
Dann, ganz am Ende, eine neue Rücksprungadresse...
die zurück auf genau diese Befehle zeigt.

<!-- S24 -->
Die Funktion ist fertig.
Der Prozessor schaut nach, wohin er zurück soll...
und springt direkt in den Code des Angreifers.

<!-- S25 -->
Jetzt läuft dessen Programm,
mit denselben Rechten wie Ihr eigenes.
Genau das heißt „Ausführen von beliebigem Code“.

<!-- S26 -->
Und der Prozessor hat nichts falsch gemacht.
Er hat nur die Befehle befolgt.

<!-- S27 -->
1988 hat genau so ein Fehler
dem Morris-Wurm erlaubt, sich
im frühen Internet auszubreiten.
Und derselbe Trick wird seitdem
immer wieder für Angriffe genutzt.

<!-- S28 -->
Neuere Sprachen überlassen deshalb einen Teil der Arbeit
dem Compiler.
Rust zum Beispiel weigert sich, viele Programme
zu übersetzen, die Speicher falsch nutzen könnten.

<!-- S29 -->
Der Programmierer sagt:
Aber ich weiß genau, was ich tue!
Und der Compiler sagt:
Das sagen sie alle.

<!-- S30 -->
Und er hat allen Grund, misstrauisch zu sein.
Microsoft und das Chrome-Team von Google
haben beide berichtet,
dass rund siebzig Prozent
der von ihnen untersuchten Sicherheitslücken
auf Probleme mit der Speichersicherheit zurückgehen.

<!-- S31 -->
Aber ein Programm kann völlig speichersicher
und trotzdem komplett falsch sein.

<!-- S32 -->
Stellen Sie sich vor, ein Nutzer meldet sich an.
Sein Passwort wird korrekt geprüft.
Nichts stürzt ab. Kein Speicher wird beschädigt.

<!-- S33 -->
Und dann zeigt ihm das Programm
die Daten von jemand anderem.
Weil in der Berechtigungsprüfung
ein winziger Fehler steckte.

<!-- S34 -->
Das kann keine Sprache von allein erkennen.
Die Sprache weiß nicht,
was das Programm eigentlich tun sollte.
Das wissen nur wir.

<!-- S35 -->
Also zurück zum Testen.
Ein Test kann Ihnen sagen:
Für diese Eingabe kam dieses Ergebnis heraus.

<!-- S36 -->
Er kann Ihnen nicht sagen:
Das Programm funktioniert bei jeder Eingabe.
Und wir haben schon gesehen,
warum wir nicht alle ausprobieren können.

<!-- S37 -->
1970 hat der Informatiker
Edsger Dijkstra das in einem Satz gesagt.
Testen kann die Anwesenheit von Fehlern zeigen,
aber niemals ihre Abwesenheit.

<!-- S38 -->
Na gut. Warum dann nicht statt zu testen
ein Programm schreiben,
das andere Programme prüft
und beweist, dass sie korrekt sind?
Man gibt ihm beliebigen Code, und es sagt einem,
ob dieser Code tut, was er soll.

<!-- S39 -->
Diese Frage war schon beantwortet,
bevor überhaupt der erste echte Computer gebaut wurde.
1936 bewies Alan Turing,
dass es so ein Programm nicht geben kann.

<!-- S40 -->
Nicht, dass es noch niemand gebaut hat.
Sondern dass es überhaupt nicht existieren kann.

<!-- S41 -->
Er zeigte, dass kein Programm
für jedes andere Programm entscheiden kann,
ob es jemals aufhört zu laufen.

<!-- S42 -->
Und 1953 ging Henry Rice noch weiter.
Dasselbe gilt für jede nichttriviale Frage
danach, was ein Programm tatsächlich tut.

<!-- S43 -->
Ist es sicher? Gibt es Daten preis?
Liefert es die richtige Antwort?
Es gibt keine allgemeine Methode,
die das für jedes Programm klärt.

<!-- S44 -->
Ist fehlerfreie Software also unmöglich?
Nicht ganz.
Für ein bestimmtes Programm
kann man manchmal seine Korrektheit beweisen,
mit enormem Aufwand.

<!-- S45 -->
2009 bewies ein Team in Australien,
dass ein kleiner Betriebssystemkern
namens seL4
genau das tut, was seine Spezifikation sagt.

<!-- S46 -->
Er hatte unter zehntausend Zeilen Code.
Den Kern zu bauen dauerte
etwa zwei Personenjahre.
Seine Korrektheit zu beweisen etwa zwanzig.
Ein moderner Webbrowser
hat Dutzende Millionen Zeilen.

<!-- S47 -->
Und selbst dieser Beweis hat einen Haken.
Er zeigt, dass das Programm seiner Spezifikation entspricht.
Er kann nicht zeigen, dass die Spezifikation
das ist, was wir eigentlich wollten.

<!-- S48 -->
Und die Spezifikation schreiben Menschen.
Also landet die Frage wieder bei uns.

<!-- S49 -->
Und es geht nicht nur um unseren eigenen Code.
Wer heute programmiert, baut auf Frameworks,
Bibliotheken und Hunderten von Abhängigkeiten auf.
Jede Schicht spart uns enorm viel Arbeit.
Aber jede Schicht ist etwas,
das wir verstehen müssen...
oder dem wir zumindest vertrauen müssen.

<!-- S50 -->
Das heißt, Sie müssen keinen Bug schreiben,
um einen in Ihrer Software zu haben.
Sie können ihn einfach installieren.

<!-- S51 -->
Dazu kommt noch der Druck.
Niemand will ein perfektes Produkt in zehn Jahren.
Man will ein funktionierendes nächsten Monat.
Und einen Einbruch, der nie passiert ist,
kann man in einer Präsentation nur schwer vorzeigen.

<!-- S52 -->
Und jetzt kommt das Seltsamste.
Unsere Werkzeuge werden immer besser.
Sicherere Sprachen, Fuzzing, Bug-Bounties...

<!-- S53 -->
Und trotzdem wächst die Zahl
der bekannten Sicherheitslücken weiter.
Allein 2024 bekamen rund vierzigtausend
eine offizielle Nummer.

<!-- S54 -->
Auch deshalb, weil wir viel, viel mehr
Software schreiben als je zuvor.
Als würde man jede Straße sicherer machen...
und dabei millionenmal mehr Straßen bauen.

<!-- S55 -->
Sind Programmierer also schlecht in ihrem Job?
Nein.
Wir haben von ihnen etwas verlangt,
das keine allgemeine Methode garantieren kann.

<!-- S56 -->
Vielleicht ist also
„Wie schreiben wir Software ohne Bugs?“
die falsche Frage.

<!-- S57 -->
Die bessere Frage lautet:
Wie bauen wir Systeme, die sicher bleiben,
auch wenn die Software Bugs hat?

<!-- S58 -->
Und genau dahin entwickelt sich die IT-Sicherheit.
Sie sagt nicht: Mach nie einen Fehler.
Sie sagt: Geh davon aus, dass du schon einen gemacht hast.

<!-- S59 -->
Erinnern Sie sich an die Rücksprungadresse?
Heute bewacht das System sie.
Es legt die Dinge im Speicher zufällig ab.
Und es weigert sich, Befehle auszuführen,
die in Daten versteckt sind.

<!-- S60 -->
Der Bug in unserem C-Code ist immer noch da.
Nur lässt er sich viel schwerer für einen Angriff nutzen.

<!-- S61 -->
Und dieselbe Idee findet sich überall.
Sandboxes, eingeschränkte Rechte,
isolierte Prozesse, Verschlüsselung,
Backups, Monitoring...
Schicht für Schicht,
damit ein einzelner Bug nicht zur Katastrophe wird.

<!-- S62 -->
Und das hat eine sehr praktische Folge.
Wenn Bugs unvermeidlich sind,
dann ist das Beheben keine Option, sondern Pflicht.

<!-- S63 -->
Die Software, die Sie heute benutzen,
enthält womöglich eine Sicherheitslücke,
die noch niemand gefunden hat.

<!-- S64 -->
Und wenn sie jemand findet,
ist das Update der Unterschied zwischen
„Es wurde eine Sicherheitslücke entdeckt“
und „Wir wurden gehackt“.

<!-- S65 -->
Dasselbe gilt für die Systeme, die wir bauen.
Alte Bibliotheken und Plattformen ohne Support
werden nicht sicherer, wenn man sie ignoriert.
Sie werden zu technischen Schulden.

<!-- S66 -->
Und warum diese Schulden
irgendwann abbezahlt werden müssen,
darum geht es in meinem Video
„Es funktioniert doch. Warum also aktualisieren?“

<!-- S67 -->
Denn bei Software sind
„es funktioniert noch“
und „es ist noch sicher“
zwei sehr verschiedene Dinge.
