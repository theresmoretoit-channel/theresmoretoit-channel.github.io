<!-- S01 -->
Vier Autos kommen an eine Kreuzung,
genau im selben Moment.
Keine Ampeln. Keine Schilder.
Nur die Regel, die in vielen Ländern gilt:
Vorfahrt hat, wer von rechts kommt.

<!-- S02 -->
Jeder Fahrer schaut nach rechts
und sieht ein Auto, auf das er warten muss.
Also wartet jeder Fahrer.

<!-- S03 -->
Niemand bricht die Regel.
Alle halten sich perfekt daran.
Und niemand wird sich je bewegen.

<!-- S04 -->
Informatiker nennen das einen Deadlock.
Und das passiert nicht nur auf der Straße.
Es passiert in Datenbanken,
Betriebssystemen und ganz normaler Software.

<!-- S05 -->
Computer erkennen einen Deadlock oft gut,
wenn er schon eingetreten ist.
Aber könnte ein Programm ein anderes lesen
und dir mit Sicherheit sagen,
ob es jemals hängen bleibt?

<!-- S06 -->
Bei vielen Programmen schon.
Aber eine Methode, die
für jedes mögliche Programm funktioniert,
kann es nicht geben.
Und zwar nicht, weil Computer
noch nicht schnell genug sind.
Kein schnellerer Computer wird je etwas daran ändern.

<!-- S07 -->
So bleibt ein Programm hängen.
Stell dir einen Onlineshop vor,
in dem zwei Aufgaben gleichzeitig laufen.

<!-- S08 -->
Bevor eine Aufgabe etwas ändert,
setzt sie eine Sperre darauf,
damit niemand anderes es anfassen kann.
Als würdest du den einzigen Schlüssel zu einem Raum nehmen.

<!-- S09 -->
Die erste Aufgabe sperrt das Konto eines Kunden
und will dann seine Bestellung sperren.
Die zweite sperrt die Bestellung
und will dann das Konto sperren.

<!-- S10 -->
Die eine hält das Konto
und wartet auf die Bestellung.
Die andere hält die Bestellung
und wartet auf das Konto.
Keine lässt los, was sie hält.

<!-- S11 -->
Und das Seltsame ist:
Dieser Code kann millionenmal laufen,
ganz ohne Probleme.
Nur wenn sich die beiden Aufgaben
in genau der falschen Reihenfolge überschneiden,
bleibt alles stehen.

<!-- S12 -->
Der Fehler war die ganze Zeit da.
Das zeitliche Zusammentreffen hat ihn bloß sichtbar gemacht.

<!-- S12b -->
Übrigens, wenn dir solche Videos
gefallen, kannst du den Kanal abonnieren.

Das hilft dem Kanal wirklich.

<!-- S13 -->
Datenbanken stoßen ständig darauf,
deshalb passen sie auf.
Sie zeichnen eine Karte davon, wer auf wen wartet.

<!-- S14 -->
Die erste wartet auf die zweite.
Die zweite wartet auf die erste.
Wenn sich die Pfeile zu einer Schleife schließen,
ist das ein Deadlock.
Kein Raten. Die Schleife ist klar zu sehen.

<!-- S15 -->
Dann tut die Datenbank etwas Brutales.
Sie wählt eine der Aufgaben aus
und wirft ihre Arbeit weg.

<!-- S16 -->
Microsofts SQL Server teilt dem Verlierer sogar mit,
er sei ausgewählt worden,
und zwar als Deadlockopfer,
und solle es noch einmal versuchen.

<!-- S17 -->
Die andere Aufgabe läuft weiter,
und das Opfer kann es einfach noch einmal versuchen.

<!-- S18 -->
Achte darauf, was das behebt und was nicht.
Die Blockade ist aufgelöst.
Aber der Code, der sie verursacht hat, ist immer noch da
und wartet auf den nächsten unglücklichen Moment.

<!-- S19 -->
Einen Deadlock zu erkennen,
der schon eingetreten ist,
ist also der leichte Teil.
Die schwierige Frage ist eine andere.

<!-- S20 -->
Nicht: Hängt dieses Programm gerade fest?
Sondern: Gib ihm diese Eingabe.
Könnte es jemals hängen bleiben?

<!-- S21 -->
Das Erste ist ein Foto der Gegenwart.
Du kannst es dir einfach ansehen.
Das Zweite ist eine Vorhersage
über jede mögliche Zukunft.

<!-- S22 -->
Und Programme machen das sehr schwer.
Sie treffen Entscheidungen. Sie wiederholen Dinge.
Sie können Berechnungen ausführen, die
eine Sekunde dauern oder tausend Jahre.

<!-- S23 -->
Ein Programm kann sofort hängen bleiben,
nach einer Million Schritten,
bei einer einzigen seltenen Eingabe
oder überhaupt nie.

<!-- S24 -->
Du könntest es einfach laufen lassen und zusehen.
Aber wenn es nach einer Stunde noch nicht hängt,
was sagt dir das?

<!-- S25 -->
Nichts.
Es könnte in der nächsten Sekunde hängen bleiben
oder nie.

<!-- S26 -->
1936 zeigte ein junger Mathematiker
namens Alan Turing,
dass manche Fragen über Programme
von keinem Programm beantwortet werden können.
Die berühmteste klingt sogar noch einfacher.

<!-- S27 -->
Nimm ein beliebiges Programm und seine Eingabe.
Wird es irgendwann anhalten?
Oder läuft es ewig?

<!-- S28 -->
Heute nennt man das das Halteproblem.
Und kein Programm kann es
in jedem Fall richtig beantworten.

<!-- S29 -->
Die Idee hinter dem Beweis
ist überraschend kurz.
Angenommen, jemand gibt dir
einen perfekten Halteprüfer.

<!-- S30 -->
Jetzt schreibst du ein kleines, widerspenstiges Programm.
Es fragt den Prüfer nach sich selbst
und tut dann das Gegenteil.

<!-- S31 -->
Sagt der Prüfer, es hält an,
läuft es in einer Endlosschleife.
Sagt der Prüfer, es läuft ewig,
hält es sofort an.

<!-- S32 -->
Was der Prüfer auch darüber sagt,
der Prüfer liegt falsch.
Also kann es keinen perfekten Prüfer geben.

<!-- S33 -->
Was hat das also mit Deadlocks zu tun?
Sehr viel.

<!-- S34 -->
Stell dir vor, jemand behauptet, er habe
einen perfekten Deadlock-Vorhersager gebaut.
Gib ihm ein beliebiges Programm und seine Eingabe,
und er sagt dir immer korrekt,
ob dieses Programm jemals hängen bleibt.

<!-- S35 -->
Benutzen wir ihn,
um das Halteproblem zu lösen.

<!-- S36 -->
Nimm ein beliebiges Programm
und bette es in ein neues Programm ein.

<!-- S37 -->
Zuerst führt das neue Programm
einfach das alte aus,
Schritt für Schritt, in einem einzigen Thread.
Keine Sperren. Nichts Geteiltes.
Nichts, was jemals hängen bleiben könnte.

<!-- S38 -->
Dann, falls das alte Programm jemals fertig wird,
startet das neue zwei Aufgaben.
Jede schnappt sich eine Sperre,
wartet, bis die andere ihre eigene hat,
und greift dann nach deren Sperre.
Ein Deadlock, mit Absicht, jedes Mal.

<!-- S39 -->
Wird das alte Programm nie fertig,
kommt das neue nie so weit.
Kein Deadlock. Niemals.

<!-- S40 -->
Das neue Programm bleibt also hängen,
genau dann, wenn das alte anhält.

<!-- S41 -->
Jetzt frag den Vorhersager
nach dem neuen Programm.
„Ja, es gibt einen Deadlock“
heißt, dass das alte Programm anhält.
„Nein“ heißt, dass es ewig läuft.

<!-- S42 -->
Wir haben gerade das Halteproblem gelöst.
Und genau das ist unmöglich.

<!-- S43 -->
Also kann es den perfekten Deadlock-Vorhersager
auch nicht geben.

<!-- S44 -->
Das Problem sind nicht die Sperren,
nicht Datenbanken und nicht schlechte Programmierer.
Ein Programm kann jede beliebige Berechnung
auf dem Weg zu einem Deadlock verstecken.
Um den Deadlock vorherzusagen,
müsstest du vorhersagen, ob die Berechnung endet.

<!-- S45 -->
Aber Moment.
Ein echter Computer ist nicht unendlich.
Sein Speicher hat eine begrenzte Zahl von Zuständen.
Könntest du sie also nicht einfach alle prüfen?

<!-- S46 -->
Bei einer Maschine mit einer festen Menge
an Speicher im Prinzip schon.
In der Praxis: Zähl sie mal.

<!-- S47 -->
Der Speicher eines Laptops
mit acht Gigabyte
lässt sich auf so viele Arten belegen,
dass schon das Aufschreiben dieser Zahl
etwa 20 Milliarden Ziffern braucht.

<!-- S48 -->
Die Zahl der Atome
im beobachtbaren Universum
hat etwa 80.

<!-- S49 -->
Auf einer echten Maschine ist es also
theoretisch möglich, alles zu prüfen,
aber praktisch hoffnungslos.

<!-- S50 -->
Aber das ist eine andere Mauer.
Turings Grenze hat nichts mit zu vielen Zuständen zu tun.
Sie gilt für Programme,
die sich immer mehr Speicher holen können.
Für die kann es keinen perfekten Vorhersager geben,
egal wie groß der Computer ist.

<!-- S51 -->
Sind wir Deadlocks also hilflos ausgeliefert?
Nein.
Es heißt nur, dass es keinen perfekten Prüfer gibt.
Also schreiben Programmierer Programme,
die sich leichter prüfen lassen.

<!-- S52 -->
Der einfachste Trick ist eine feste Reihenfolge.
Jede Aufgabe muss das Konto sperren,
bevor sie die Bestellung sperrt.
Nie andersherum.

<!-- S53 -->
Wenn sich wirklich jede Aufgabe an diese Reihenfolge hält,
kann sich die Schleife nicht schließen,
und diese Art von Deadlock kann nicht auftreten.

<!-- S54 -->
Andere Systeme geben nach einem Timeout auf,
holen sich alle Sperren auf einmal
oder lassen die Datenbank ein Opfer wählen
und versuchen es einfach noch einmal.

<!-- S55 -->
Und bei kleinen, sorgfältig beschriebenen Entwürfen
können Werkzeuge jeden möglichen Zustand prüfen.
Ingenieure bei Amazon haben so eines benutzt,
um einen Fehler zu finden, der erst nach 35 Schritten
in genau der richtigen Reihenfolge auftrat.

<!-- S56 -->
Diese Werkzeuge funktionieren,
weil das Problem kleiner gemacht wurde.
Sie prüfen ein Modell des Systems,
nicht jedes Programm, das je existieren könnte.

<!-- S57 -->
Bei echtem Code aber
muss ein Prüfer, der jedes Programm annimmt,
auf etwas verzichten.
Er kann vor Deadlocks warnen,
die nicht eintreten können,
manche übersehen, die eintreten können,
oder manchmal gar keine Antwort geben.

<!-- S58 -->
Ein Prüfer, der nie falschen Alarm schlägt,
nie einen Deadlock übersieht
und immer eine Antwort gibt,
und zwar für jedes Programm,
ist genau das, was Turing ausgeschlossen hat.

<!-- S59 -->
Zurück an der Kreuzung:
Die vier Fahrer stehen dort nicht ewig.

<!-- S60 -->
Jemand winkt.
Ein Fahrer verzichtet auf seine Vorfahrt,
und nach Sekunden ist die Blockade gelöst.

<!-- S61 -->
Genau das macht auch die Datenbank.
Sie sagt die Blockade nicht voraus.
Sie bemerkt sie
und bringt jemanden dazu, nachzugeben.

<!-- S62 -->
Manche Probleme brauchen einen schnelleren Computer.
Manche eine bessere Idee.

<!-- S63 -->
Und manche, wie dieses,
haben überhaupt keine perfekte Lösung.
Nur gute Regeln
und jemanden, der bereit ist zu winken.
