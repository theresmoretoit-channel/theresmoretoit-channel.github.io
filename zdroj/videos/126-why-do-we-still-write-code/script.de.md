<!-- S01 -->
Hier ist eine vollständige Anforderung
an eine Unternehmenssoftware.
Ein Nutzer kann eine Bestellung stornieren.

<!-- S02 -->
Sechs Wörter.
Jeder Entwickler würde nicken.
Jeder Kunde würde unterschreiben.

<!-- S03 -->
Kann ein Nutzer also eine Bestellung stornieren,
wenn die Rechnung schon raus ist?
Wenn die Ware schon verschickt ist?

<!-- S04 -->
Wird damit auch gleich
die Reservierung beim Lieferanten storniert?
Und was, wenn einer sie storniert
und ein anderer dieselbe Bestellung freigibt,
in derselben Sekunde?

<!-- S05 -->
Der Satz beantwortet nichts davon.
Der Code muss alles davon beantworten.
Und genau für diese Lücke zwischen dem Satz
und dem Code werden Programmierer
eigentlich bezahlt.
Zumindest war das früher so.

<!-- S06 -->
Heute gibt es eine verlockende Idee.
Schreib nur noch die Sätze.
Halte sie in Dokumenten fest,
prüfe sie, versioniere sie.
Und lass eine KI den Code schreiben.

<!-- S07 -->
Die Spezifikation wird
zum Quellcode.
Der Code wird zu dem, was Assembler
heute ist: etwas, das läuft
und das niemand liest.

<!-- S08 -->
Es ist eine gute Idee.
Nur ist sie nicht neu.

<!-- S09 -->
Seit fast siebzig Jahren versuchen Menschen,
die Ebene anzuheben,
auf der wir Computern sagen, was sie tun sollen.
Die Werkzeuge waren verschieden,
und ihre Ziele auch.
Aber jedes verlagerte mehr Arbeit
von Menschen auf Maschinen.

<!-- S10 -->
1957 veröffentlichte ein Team bei IBM
einen Aufsatz über FORTRAN.
Im Titel wurde es
ein automatisches Codiersystem genannt.

<!-- S11 -->
Damals war das eine treffende Bezeichnung.
Man schrieb Formeln,
und die Maschinenbefehle,
also den Teil, den Menschen von Hand geschrieben hatten,
erzeugte jetzt die Maschine.

<!-- S12 -->
Heute nennen wir FORTRAN Code.

<!-- S13 -->
In den 1980er-Jahren gingen CASE-Werkzeuge
und Sprachen der vierten Generation
eine Ebene höher.
Zeichne die Diagramme, füll die Formulare aus,
und ein großer Teil der Anwendung
wird für dich generiert.

<!-- S14 -->
2001 kündigte die Object Management Group,
das Gremium hinter UML,
die Model Driven Architecture an.

<!-- S15 -->
Das Versprechen wird dir bekannt vorkommen.
Du beschreibst das System einmal,
als Modell, unabhängig von jeder Technologie.
Dann erzeugen Werkzeuge die Implementierung
für jede Plattform, die du brauchst.

<!-- S16 -->
Dieselben Geschäftsregeln.
Austauschbare Technologie.

<!-- S17 -->
Und 2014 gaben die Analysten von Forrester
Plattformen einen Namen,
mit denen man Geschäftsanwendungen
mit so wenig handgeschriebenem Code
wie möglich baut.
Sie nannten es Low-Code.

<!-- S18 -->
Hat also irgendetwas davon funktioniert?

<!-- S19 -->
Teilweise.
2014 veröffentlichten Forscher der Lancaster University
eine Umfrage
unter 450 Leuten,
die modellgetriebene Entwicklung
tatsächlich einsetzten.

<!-- S20 -->
Es hat funktioniert,
und zwar häufiger, als viele dachten.
Aber selten für ein ganzes System.
Man nutzte es für zentrale Teile
und baute den Rest auf andere Weise.

<!-- S21 -->
Die größten Hindernisse, die sie fanden,
waren Menschen und Organisationen,
nicht Werkzeuge.
Aber es gibt auch eine technische Grenze,
und Programmierer haben einen Witz darüber.

<!-- S22 -->
Eine Spezifikation, die präzise genug ist,
um daraus das ganze Programm zu generieren...
hat schon einen Namen.
Sie heißt Code.

<!-- S23 -->
Um alles zu generieren,
musste das Modell alles sagen.
Jeden Zustand, jede Ausnahme,
jedes „Was, wenn zwei Leute es gleichzeitig tun?“.

<!-- S24 -->
An diesem Punkt
bist du dem Programmieren nicht entkommen.
Du hast es nur in ein Diagramm verschoben,
das oft schwerer zu lesen,
zu vergleichen und zu prüfen ist.

<!-- S25 -->
Schon Ende der 1970er-Jahre
fasste Edsger Dijkstra die andere Hälfte
in einer kurzen Notiz mit unverblümtem Titel zusammen.
Über die Torheit
des Programmierens in natürlicher Sprache.

<!-- S26 -->
Sein Punkt war, dass formale Notation
keine Last ist, die wir eben ertragen.
Er nannte sie ein erstaunlich wirksames Werkzeug,
um allen möglichen Unsinn auszuschließen.

<!-- S27 -->
Normale Sprache schließt ihn nicht aus.
Sie versteckt ihn.
Ein Nutzer kann eine Bestellung stornieren.

<!-- S28 -->
Wenn also nichts davon den Code ersetzt hat,
warum es noch einmal versuchen?

<!-- S29 -->
Weil eine Sache wirklich anders ist.

<!-- S30 -->
Ältere Generatoren konnten eine Lücke
nicht von sich aus füllen.
Wenn das Modell nicht sagte, was passiert
mit einer verschickten Bestellung,
musste jemand diese Regel ausdrücklich ergänzen.
Bis dahin war die Lücke noch da,
und man konnte sie finden.

<!-- S31 -->
Eine KI hält nicht an.
Gib ihr die Sechs-Wörter-Anforderung,
und sie beantwortet jede Frage,
die wir am Anfang gestellt haben.

<!-- S32 -->
Sie entscheidet, dass eine verschickte Bestellung
storniert werden kann. Oder eben nicht.
Sie entscheidet über die Rechnung
und über den Lieferanten.
Sie erzeugt Code, der läuft,
vernünftig aussieht
und die Tests besteht, die sie selbst geschrieben hat.

<!-- S33 -->
Genau das macht sie nützlich.
Und genau das macht sie gefährlich.
Denn eine plausible Vermutung
ist keine geschäftliche Entscheidung.

<!-- S34 -->
Früher waren die Lücken Fehler.

<!-- S35 -->
Jetzt sind sie Entscheidungen,
die gefallen sind, ohne dass es jemand gemerkt hat.

<!-- S36 -->
Wenn die Spezifikation also wirklich
zum Quellcode werden soll,
kann sie nicht aus ein paar locker formulierten Absätzen bestehen.

<!-- S37 -->
Stell dir das Repository vor.
Ein Dokument beschreibt Bestellungen
und alle Zustände, in denen sie sein können.
Ein anderes sagt, wer sie freigeben darf
und wer sie stornieren darf.

<!-- S38 -->
Ein drittes sagt, wann eine Rechnung ausgestellt wird
und wann sie storniert werden muss.
Ein weiteres beschreibt das Buchhaltungssystem,
auch, was passiert, wenn es ausfällt.

<!-- S39 -->
Einiges davon ist normaler Fließtext.
Aber überall, wo Text mehrdeutig wäre,
steht etwas Strengeres:
eine Liste von Zuständen und den Übergängen dazwischen,
ein Schema, eine Regel, die eine Maschine prüfen kann.

<!-- S40 -->
Und daneben Abnahmetests,
die genau sagen, was passieren muss.

<!-- S41 -->
All das liegt in Git.
Änderungen werden reviewt.
Jede Anforderung lässt sich
bis zu dem Test zurückverfolgen, der sie prüft.

<!-- S42 -->
Wie sieht also eine Änderung aus?
Sagen wir, der Kunde entscheidet,
dass eine verschickte Bestellung doch noch storniert werden kann,
solange sie noch nicht zugestellt ist.
Und dann muss die Rechnung storniert werden.

<!-- S43 -->
Niemand öffnet das Backend.
Ein Entwickler ändert eine einzige Regel
im Dokument über Bestellungen.

<!-- S44 -->
Dann sucht das System
alles heraus, was diese Regel berührt.
Die Zustände der Bestellung.
Die Rechnungsregeln.
Die Tests zum Stornieren.
Die Reservierung beim Lieferanten.

<!-- S45 -->
Und genau da sollte es anhalten und fragen.
Die Spezifikation hat nie gesagt,
was mit einer Reservierung beim Lieferanten passiert,
sobald die Ware unterwegs ist.
Das ist eine Entscheidung,
also geht sie zurück an einen Menschen.

<!-- S46 -->
Erst dann wird die neue Implementierung
generiert.
Und sie wird in beide Richtungen geprüft.
Die Tests für die neue Regel sollen durchlaufen.
Und alle anderen Tests sollen weiterhin durchlaufen,
unverändert.

<!-- S47 -->
Denn eine Änderung am Stornieren
darf nicht stillschweigend etwas anderes ändern.
Wobei bestandene Tests nur zeigen,
was die Tests prüfen.

<!-- S48 -->
Und weil die Regeln
nicht an die Technologie gebunden sind,
könnte dieselbe Spezifikation
heute eine PHP-Anwendung hervorbringen
und morgen etwas völlig anderes.

<!-- S49 -->
Und genau das hat
die Model Driven Architecture versprochen,
vor fünfundzwanzig Jahren.
Der Unterschied ist, dass diesmal
der Generator gut genug sein könnte.

<!-- S50 -->
Bleibt die schwierigste Frage.
Woher weißt du, dass sich die KI
wirklich an die Spezifikation gehalten hat?

<!-- S51 -->
Code, der in normalen Situationen funktioniert,
kann trotzdem in ungewöhnlichen versagen.
Und die ungewöhnlichen sind genau
die Fälle, die zu testen niemandem einfällt.

<!-- S52 -->
Amazon ist darauf gestoßen,
bei seinen eigenen Cloud-Systemen.
2014 beschrieben seine Ingenieure,
wie sie angefangen hatten,
präzise, mathematische Beschreibungen
ihrer Entwürfe zu schreiben,
in einer Sprache namens TLA+.

<!-- S53 -->
Nicht vom Code. Vom Entwurf selbst.
Ein Werkzeug nahm dann ein Modell des Systems,
begrenzt auf eine feste Größe,
und probierte jede mögliche Reihenfolge
von Ausfällen und Wiederherstellungen durch.

<!-- S54 -->
In DynamoDB, dem Datenbankdienst von Amazon,
fand es einen Fehler, der zu Datenverlust führen konnte.

<!-- S55 -->
Der kürzeste Weg, ihn auszulösen,
umfasste 35 Schritte,
in genau der richtigen Reihenfolge.
Der Fehler hatte Design-Reviews,
Code-Reviews und Tests überstanden.

<!-- S56 -->
Die ehrliche Version der Idee ist also
nicht, dass die KI den Code schreibt
und wir ihr vertrauen.
Sondern dass die KI den Code schreibt
und etwas Unabhängiges ihn prüft.

<!-- S57 -->
Schau dir jetzt an, was wir gebaut haben.

<!-- S58 -->
Präzise Zustände.
Formale Regeln.
Prüfbare Tests.
Versioniert, reviewt, in einem Repository abgelegt.

<!-- S59 -->
Das sieht nicht aus
wie das Ende des Programmierens.
Es sieht aus wie Programmieren,
in einer neuen Sprache.

<!-- S60 -->
Und genau das ist jedes Mal passiert.
FORTRAN war automatisches Codieren,
bis es zum Code wurde.
Jedes Mal, wenn die Maschine
das „Wie“ übernahm, rückten Menschen zum „Was“ auf.

<!-- S61 -->
Und das „Was“ war immer der schwierige Teil.
Nicht Tippen, sondern Entscheiden.
Was mit einer verschickten Bestellung passiert.
Wer welche Daten anfassen darf.
Was das System niemals tun darf.

<!-- S62 -->
Vielleicht schreibt der Programmierer der Zukunft
nicht mehr Tausende Zeilen Code.

<!-- S63 -->
Aber jemand wird immer noch ein Problem
gut genug verstehen müssen, um zu sagen,
was genau ein Computer tun muss,
und zu prüfen, ob er es getan hat.

<!-- S64 -->
Und wenn die Spezifikation
zum Quellcode wird,
ist die wichtigste Fähigkeit
vielleicht nicht mehr, zu wissen,
wie man ein Programm schreibt.

<!-- S65 -->
Sondern vielleicht, zu wissen,
wie man eines beschreibt.

<!-- S66 -->
Hier also die Frage,
auf die ich gern deine Antwort hören würde.
Wenn du eine Spezifikation schreibst,
die so präzise ist,
dass eine Maschine danach bauen kann...
programmierst du dann noch?
