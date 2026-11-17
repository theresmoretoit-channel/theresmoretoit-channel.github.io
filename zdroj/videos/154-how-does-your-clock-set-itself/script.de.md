<!-- S01 -->
Irgendwo bei dir zu Hause
gibt es vielleicht eine Uhr,
die noch nie jemand gestellt hat.

<!-- S02 -->
Sie übersteht Stromausfälle.
Auf Sommer- und Winterzeit stellt sie sich
von selbst um, mitten in der Nacht.

<!-- S03 -->
Sie hat keinen Internetanschluss.
Kein WLAN, kein GPS,
keine App auf deinem Handy.

<!-- S04 -->
Sie hat nur einen winzigen Funkempfänger.
Und einmal pro Sekunde
hört sie einen einzigen Impuls.

<!-- S05 -->
Wie also macht eine Uhr
aus einem Impuls pro Sekunde
die genaue Uhrzeit, das Datum
und sogar den Wochentag?

<!-- S06 -->
In Europa kommen diese Impulse
von DCF77 bei Frankfurt.
In Amerika von WWVB in Colorado.
Andere Sender, dieselbe Idee.

<!-- S07 -->
Nehmen wir den deutschen.
Er sendet eine gleichmäßige Funkwelle,
Tag und Nacht.
Und zu Beginn jeder Sekunde
senkt er sie kurz ab.

<!-- S08 -->
Der Trick ist, wie lange
sie abgesenkt bleibt.

<!-- S09 -->
Eine Absenkung von einer Zehntelsekunde
bedeutet Null.
Zwei Zehntel bedeuten Eins.

<!-- S10 -->
Das ist schon die ganze Idee.
Keine Pakete, kein Netzwerk.
Nur eine Funkwelle, die abgesenkt wird,
kurz oder etwas länger.

<!-- S11 -->
Ein Bit pro Sekunde.
Das heißt, eine ganze Minute
reicht für gerade mal 60 Bits.

<!-- S12 -->
Und tatsächlich sendet er nur 59.

<!-- S13 -->
In der letzten Sekunde jeder Minute
wird die Welle gar nicht abgesenkt.
Und genau diese fehlende Absenkung
ist der wichtigste Teil
des ganzen Signals.

<!-- S14 -->
Denn wenn die nächste Absenkung kommt,
weiß die Uhr,
dass gerade eine neue Minute begonnen hat.

<!-- S15 -->
Die Lücke wirkt wie ein Punkt.
Alles zwischen zwei Lücken
ist ein vollständiger Satz.

<!-- S16 -->
Was passt also in einen Satz
aus 59 Bits?

<!-- S17 -->
Die Minute. Die Stunde.
Der Tag im Monat, der Wochentag,
der Monat und das Jahr.

<!-- S18 -->
Die meisten Zahlen werden Ziffer für Ziffer gesendet.
47 Minuten
werden nicht als 47 gesendet,
sondern als zwei einzelne Ziffern,
eine Vier und eine Sieben.

<!-- S19 -->
Vier Bits reichen für jede Ziffer
von null bis neun.
Die Zehner der Minuten gehen nie über fünf,
deshalb bekommen sie nur drei.

<!-- S20 -->
Und das Jahr bekommt nur zwei Ziffern.
Für den Sender
ist 2026 einfach 26.
Das Jahrhundert ergänzt die Uhr selbst.

<!-- S21 -->
Aber Funk ist kein sauberer Kanal.
Ein Motor, ein Handy-Ladegerät,
eine billige LED-Lampe...
jedes davon kann eine Absenkung verwischen.

<!-- S22 -->
Deshalb folgt nach jedem Zahlenblock
ein zusätzliches Bit, das Paritätsbit.

<!-- S23 -->
Es wird so gewählt, dass die Anzahl der Einsen
im Block immer gerade ist.

<!-- S24 -->
Wenn eine Störung ein einzelnes Bit umkippt,
wird die Anzahl ungerade,
und die Uhr weiß,
dass etwas schiefgegangen ist.

<!-- S25 -->
Kippen aber zwei Bits um,
ist die Anzahl wieder gerade,
und der Fehler rutscht durch.

<!-- S26 -->
Deshalb vertrauen viele Uhren
nicht einer einzigen Minute.
Sie warten auf eine weitere gültige.

<!-- S27 -->
Und deshalb kann das Stellen
mehrere Minuten dauern,
und an einem schlechten Tag viel länger.

<!-- S28 -->
Daraus ergibt sich ein seltsames Problem.

<!-- S29 -->
Die Uhr sammelt eine ganze Minute lang
die Uhrzeit 10:48.
Aber während sie diese Nachricht sammelt,
ist es noch 10:47.

<!-- S30 -->
Wann springt sie also tatsächlich um?

<!-- S31 -->
Die Nachricht ist nämlich eine Ankündigung.
Sie sagt, wie spät es sein wird,
wenn die nächste Minute beginnt.

<!-- S32 -->
Die Uhr liest den ganzen Satz,
wartet die fehlende Absenkung ab,
und wenn die nächste Absenkung kommt,
ist genau sie der exakte Moment.

<!-- S33 -->
Die Bits sagen der Uhr, wie spät es ist.
Die Absenkung sagt ihr, wann.

<!-- S34 -->
Aber der Satz enthält ein paar Wörter mehr
als nur die Uhrzeit.

<!-- S35 -->
Zwei Bits sagen, ob in Deutschland
Winterzeit oder Sommerzeit gilt.

<!-- S36 -->
Und ein drittes ist eine Warnung.
Eine ganze Stunde vor der Zeitumstellung
steht es auf Eins.

<!-- S37 -->
Deine Uhr muss also nicht wissen,
an welchem Sonntag im März
die Uhren vorgestellt werden
oder an welchem im Oktober zurück.
Niemand hat ihr die Regel je beigebracht.
Man sagt es ihr einfach eine Stunde vorher.

<!-- S38 -->
Falls Europa die Zeitumstellung je abschafft,
kommt die Warnung einfach nie wieder.

<!-- S39 -->
Ein weiteres Bit warnte früher vor einer Schaltsekunde,
einer zusätzlichen Sekunde, die ab und zu eingefügt wurde,
weil die Erdrotation
nicht perfekt im Takt ist.
Diese Minute konnte 61 Sekunden haben.

<!-- S40 -->
Die letzte wurde
Ende 2016 eingefügt.
Aber im Oktober 2026
haben die Metrologiebehörden der Welt
beschlossen, die Schaltsekunden abzuschaffen.
Ab dem 20. Mai 2027
läuft UTC durchgehend.

<!-- S41 -->
Und die ersten 14 Bits
jeder Minute
haben mit der Zeit gar nichts zu tun.

<!-- S42 -->
Seit 2006 werden sie außerdem genutzt,
um verschlüsselte Wettervorhersagen zu übertragen,
für kompatible Wetterstationen.

<!-- S43 -->
Das Signal, das deinen Wecker stellt,
konnte also auch
einer fremden Wetterstation sagen,
ob es am Donnerstag regnen würde.

<!-- S44 -->
Und doch hören die meisten dieser Uhren
nicht ständig zu.
Zuhören kostet Batterie,
deshalb versuchen es viele einmal pro Nacht,
in den frühen Morgenstunden.

<!-- S45 -->
Langwellen erreichen eine Uhr auf zwei Wegen:
am Boden entlang
und reflektiert an der oberen Atmosphäre.
Nach Einbruch der Dunkelheit verändert sich dieser obere Weg,
und das Signal reicht oft weiter.

<!-- S46 -->
Und um drei Uhr morgens
laufen in der Nähe meist weniger Maschinen,
Ladegeräte und Lampen, die es übertönen könnten.

<!-- S47 -->
Zwischen diesen Abgleichen
läuft die Uhr mit einem Quarzkristall,
der um etwa eine Sekunde pro Tag abweichen kann.

<!-- S48 -->
Beim nächsten erfolgreichen Abgleich
korrigiert das Funksignal diese Abweichung.

<!-- S49 -->
Sogar der Ort, an dem sie lauscht, spielt eine Rolle.
Die Antenne ist ein kleiner Ferritstab,
mit Draht umwickelt.

<!-- S50 -->
Sie empfängt am besten, wenn der Stab quer
zur Richtung des Senders liegt,
nicht wenn er auf ihn zeigt.
Dreh die Uhr um,
und ein schwaches Signal kann ganz verschwinden.

<!-- S51 -->
Deshalb funktioniert eine Uhr im Regal,
und dieselbe Uhr, zwei Meter weiter
hinter einer Stahlbetonwand, stellt sich nie.

<!-- S52 -->
Woher bekommt der Sender
also seine Zeit?

<!-- S53 -->
Von der PTB,
Deutschlands nationalem Metrologieinstitut,
das Atomuhren betreibt.

<!-- S54 -->
Die Sekunde selbst ist
über Cäsiumatome definiert.
Eine Sekunde sind genau
9.192.631.770 Schwingungen
der Strahlung, die sie abgeben.

<!-- S55 -->
Ein billiger Wecker auf dem Nachttisch
folgt also ganz buchstäblich
einem Zeitnormal,
das durch Cäsiumatome definiert ist.

<!-- S56 -->
Allerdings nicht perfekt.
Das Signal breitet sich mit Lichtgeschwindigkeit aus,
und braucht trotzdem etwa 3 Millisekunden
pro 1.000 Kilometer.

<!-- S57 -->
Der Empfänger fügt eine eigene Verzögerung hinzu,
und deine Uhr korrigiert nichts davon.
Muss sie auch nicht.
Sie zeigt nur Sekunden an.

<!-- S58 -->
Von einem einzigen Standort bei Frankfurt
erreicht das Signal Uhren
bis zu etwa 2.000 Kilometer entfernt.
Das ist der größte Teil Europas.

<!-- S59 -->
Die Schweiz hatte einen eigenen Sender
namens HBG, bis Ende 2011.
Seine Antennen hätten erneuert werden müssen,
zu wenige Leute nutzten ihn,
und Schweizer Uhren konnten einfach
stattdessen den deutschen Sender empfangen.

<!-- S60 -->
Andere behielten ihren.
Großbritannien, Frankreich, Japan und China
betreiben alle einen eigenen.

<!-- S61 -->
Und in Nordamerika sendet WWVB
seit 1963 aus Fort Collins,
mit Zeitcode seit 1965.

<!-- S62 -->
Gleiches Prinzip, anderer Dialekt.
Eine Null ist eine Absenkung von zwei Zehntelsekunden.
Eine Eins dauert eine halbe Sekunde.

<!-- S63 -->
Und statt einer Lücke pro Minute
kommt alle 10 Sekunden eine längere Marke,
wie Kommas im Satz.
Zwei hintereinander bedeuten eine neue Minute.

<!-- S64 -->
Der größte Unterschied ist,
welche Zeit gesendet wird.
Deutschland sendet die mitteleuropäische gesetzliche Zeit,
die in einem großen Teil des Kontinents gilt.

<!-- S65 -->
Aber die Vereinigten Staaten
erstrecken sich über mehrere Zeitzonen.
Deshalb sendet WWVB die Weltzeit UTC,
und du sagst der Uhr, wo du bist.

<!-- S66 -->
Den Monat sendet er nicht einmal.
Nur den Tag des Jahres,
von 1 bis 366.

<!-- S67 -->
Keine dieser Stationen
spricht dieselbe Sprache.
Eine Uhr für Deutschland
kann mit Colorado nichts anfangen.

<!-- S68 -->
Aber auf beiden Seiten des Atlantiks
ist es dieselbe stille Routine.
Nacht für Nacht gleicht sich ein kleiner Empfänger
mit einem atomaren Zeitnormal ab,
Hunderte oder Tausende Kilometer entfernt.

<!-- S69 -->
Also, eine Frage an dich.
Wenn alle Funkzeitsignale
heute Nacht verschwinden würden,
würdest du es überhaupt merken?
Schreib es mir in die Kommentare.
