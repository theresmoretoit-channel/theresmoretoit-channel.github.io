<!-- S01 -->
Du kaufst dir ein brandneues Laufwerk.
Ein Terabyte, komplett leer.
Bevor es auch nur eine einzige Datei aufnimmt,
muss es erst formatiert werden.

<!-- S02 -->
Also formatierst du es mit ext4,
dem Standard-Dateisystem
auf vielen Linux-Rechnern.
Mit den Standardeinstellungen,
bevor du überhaupt etwas gespeichert hast,
sind schon rund siebzehn Gigabyte weg.

<!-- S03 -->
Gespeichert ist noch gar nichts.
Keine Fotos, keine Dokumente.
Was belegt also den ganzen Platz?

<!-- S04 -->
Und warum muss ein Laufwerk
überhaupt formatiert werden?
Daten speichern kann es doch schon.
Es kann Billionen von Bits lesen und schreiben.

<!-- S05 -->
Warum schreibt der Computer nicht einfach los,
wo immer gerade Platz ist?

<!-- S06 -->
Weil Daten zu speichern
und sie wiederzufinden
zwei ganz verschiedene Probleme sind.

<!-- S07 -->
Stell dir ein Amt vor, das statt Formularen
leere Blätter verteilt.
Alles wird irgendwo aufgeschrieben...
und niemand findet irgendwas.

<!-- S08 -->
Ein Laufwerk ohne Dateisystem
ist dieser Papierstapel.
Ein besseres Bild
ist aber ein Notizbuch.

<!-- S09 -->
Stell dir ein Notizbuch vor,
mit tausend Seiten
und ein paar Regeln, wie man es benutzt.

<!-- S10 -->
Erstens: Jede Seite hat eine Nummer.
Damit hat jede Stelle im Notizbuch
eine Adresse.
Seite vierhundertzwölf
bezeichnet genau eine Stelle.

<!-- S11 -->
Zweitens: Die ersten paar Seiten
sind ein Inhaltsverzeichnis.
Jeder Eintrag nennt einen Namen
und die Seite, auf der er steht.
Pfannkuchen: Seite zwölf.

<!-- S12 -->
Drittens: Ganz hinten
gibt es eine Liste der Seiten,
die noch leer sind.

<!-- S13 -->
Jetzt kommt ein Rezept dazu.
Du suchst hinten nach einer leeren Seite.
Du schreibst das Rezept dorthin.
Du ergänzt eine Zeile im Inhaltsverzeichnis.
Und du streichst diese Seite
von der Liste der leeren Seiten.

<!-- S14 -->
Ein Rezept, drei Stellen.
Und alle drei müssen übereinstimmen.

<!-- S15 -->
Dann wird das Pfannkuchenrezept länger.
Seite zwölf ist voll,
und Seite dreizehn ist schon belegt.
Also geht es auf Seite siebenundachtzig weiter,
und das Inhaltsverzeichnis muss das vermerken.

<!-- S16 -->
Und jetzt kommt der Haken.
Wenn du Platz für tausend Einträge
im Inhaltsverzeichnis willst,
musst du diese Seiten reservieren,
bevor du ein einziges Rezept schreibst.

<!-- S17 -->
So viel zum Vergleich.
Und so sieht es wirklich auf dem Laufwerk aus.

<!-- S18 -->
Ein Laufwerk weiß nichts von Dateien,
Ordnern oder Namen.
Es bietet nur eine lange Reihe
nummerierter Plätze, die Sektoren heißen.

<!-- S19 -->
Auf einer Festplatte
liegen die Daten auf rotierenden Scheiben.
Eine SSD speichert sie im Flash-Speicher.
So oder so fragt der Computer immer nur
nach einem Sektor mit seiner Nummer,
und das Laufwerk findet heraus, wo der liegt.

<!-- S20 -->
Ein Sektor ist klein.
Meist 512 Byte,
oder 4.096
bei neueren Laufwerken.

<!-- S21 -->
Dateisysteme arbeiten meist
mit größeren Stücken, den Blöcken.
Bei ext4 ist ein Block vier Kilobyte groß,
so groß wie acht Sektoren alter Bauart.

<!-- S22 -->
Diese nummerierten Blöcke
sind die Seiten des Notizbuchs.
Was dem Dateisystem noch fehlt,
sind die anderen beiden Teile:
ein Inhaltsverzeichnis
und eine Liste dessen, was frei ist.

<!-- S23 -->
Genau das legt das Formatieren an.
Und genau dorthin
sind die siebzehn Gigabyte verschwunden.

<!-- S24 -->
Ext4 reserviert einen Eintrag
für jede Datei und jeden Ordner,
die das Laufwerk gleichzeitig fassen kann.
Jeder Eintrag ist
256 Byte groß.
Er heißt Inode.

<!-- S25 -->
Eines Tages wird jeder Inode sagen,
wie groß eine Datei ist,
wann sie geändert wurde,
wer sie öffnen darf
und in welchen Blöcken ihr Inhalt liegt.

<!-- S26 -->
Auf einem Ein-Terabyte-Laufwerk
legt ext4 rund
einundsechzig Millionen davon an.
Alle sind leer, alle warten.
Das sind fast sechzehn Gigabyte
leerer Einträge.

<!-- S27 -->
Warum einundsechzig Millionen?
Ext4 schätzt ganz einfach:
ein Inode pro sechzehn Kilobyte
Platz auf dem Laufwerk.
Auf einem typischen Computer
wird der Großteil dieser Einträge
nie benutzt.

<!-- S28 -->
Etwa ein weiteres Gigabyte
geht an ein Journal,
auf das wir noch zurückkommen.
Der Rest ist weitere Buchhaltung,
darunter eine Karte mit einem Bit pro Block,
das sagt, ob er belegt oder frei ist.

<!-- S29 -->
Auch diese Zahl ist fest.
Verbrauch alle Einträge
mit Millionen winziger Dateien,
und das Laufwerk meldet dir, es sei voll...
obwohl noch Gigabytes frei sind.

<!-- S30 -->
Schauen wir also zu, wie das funktioniert.
Wir legen eine Datei namens hello.txt an.
Darin nur ein Wort: hello.
Fünf Buchstaben. Fünf Byte.

<!-- S31 -->
Das Dateisystem wählt einen leeren Inode.
Sagen wir, Nummer dreizehn.
Dann sucht es in der Karte einen freien Block
und markiert ihn als belegt.

<!-- S32 -->
Es schreibt die fünf Byte in diesen Block.
Dann füllt es den Inode aus:
fünf Byte lang, gerade eben erstellt
und in diesem einen Block gespeichert.

<!-- S33 -->
Und zuletzt fügt es im Ordner
eine Zeile hinzu:
den Namen hello.txt
und die Nummer dreizehn.

<!-- S34 -->
Achte darauf, wo der Name gelandet ist.
Nicht in der Datei.
Nicht im Inode.
Der Name steht im Ordner,
und der ist eigentlich nur eine Liste
aus Namen und Nummern.

<!-- S35 -->
Und ein Ordner ist einfach noch eine Datei.
Was sie eben enthält,
ist diese Liste.

<!-- S36 -->
Deshalb ist auch das Verschieben einer Datei
in einen anderen Ordner im selben Dateisystem
sofort erledigt, egal wie groß sie ist.
Ein Ordner verliert eine Zeile,
der andere bekommt eine dazu,
und meistens bewegt sich
der Inhalt überhaupt nicht.

<!-- S37 -->
Fünf Byte Text...
und auf dem Laufwerk belegen sie
4.096.
Ein Block ist das kleinste Stück,
das das Dateisystem vergibt,
also kostet selbst eine winzige Datei einen ganzen.

<!-- S38 -->
Wenn die Datei aus ihrem Block herauswächst,
sucht das Dateisystem einen weiteren freien.
Vielleicht direkt nebenan.
Vielleicht ganz woanders.
Und der Inode merkt sich beide.

<!-- S39 -->
Mit der Zeit kann eine große Datei
in Stücken über das ganze Laufwerk verstreut sein.
Eine Festplatte muss zwischen ihnen hin und her springen.
Eine SSD kommt damit viel besser zurecht.

<!-- S40 -->
Das Programm, das die Datei gespeichert hat,
weiß von alldem nichts.
Es hat „speichere hello.txt“ gesagt,
und alles andere lief im Hintergrund ab.

<!-- S41 -->
Jetzt lösch sie.
Der Name wird aus dem Ordner entfernt.
Der Inode wird als frei markiert.
Der Block kommt zurück auf die Liste der freien.

<!-- S42 -->
Auf einer klassischen Festplatte
bleiben die fünf Byte selbst, wo sie sind.
Niemand hat sie angefasst.
Sie bleiben, bis etwas Neues
darübergeschrieben wird.

<!-- S43 -->
Deshalb lässt sich eine gelöschte Datei
manchmal wiederherstellen.
Löschen entfernt meistens nicht
den Inhalt selbst.
Es markiert den Platz nur als verfügbar.

<!-- S44 -->
Bei einer SSD ist das weniger sicher.
Das Dateisystem kann dem Laufwerk sagen,
dass diese Blöcke nicht mehr gebraucht werden,
und das Laufwerk kann ihren Inhalt verwerfen.
Danach ist es viel unwahrscheinlicher,
die Datei zurückzubekommen.

<!-- S45 -->
Ein Dateisystem ist also eigentlich ein Buchhalter.
Diese eine Datei anzulegen
hieß, drei Dinge zu aktualisieren:
den Ordner, den Inode
und die Karte der freien Blöcke.

<!-- S46 -->
Jetzt zieh den Stecker,
mitten beim Speichern einer Datei.

<!-- S47 -->
Vielleicht wurde der Block schon als belegt markiert,
aber noch zeigt kein Inode auf ihn.
Dieser Platz ist dann einfach verloren.
Ärgerlich, aber harmlos.

<!-- S48 -->
Oder der Inode zeigt auf einen Block,
den die Karte noch als frei führt.
Die nächste Datei kann dann
direkt darüber geschrieben werden.
Und die erste wird still und leise zerstört.

<!-- S49 -->
Deshalb führt ext4 ein Journal.
Bevor es seine Buchhaltung ändert,
schreibt es auf, was es gleich tun wird.
Nach einem Absturz spielt es nur die Änderungen erneut ab,
die es fertig aufgeschrieben
und als abgeschlossen markiert hatte.
Alles Unfertige wird ignoriert.

<!-- S50 -->
Und dann gibt es ein unauffälligeres Problem.
Manchmal ändert ein Laufwerk ein Bit
und sagt niemandem Bescheid.

<!-- S51 -->
Ext4 schützt seine eigenen Einträge
mit Prüfsummen,
damit es dort Schäden erkennen kann.
Aber der Inhalt deiner Dateien?
Dem vertraut es einfach.

<!-- S52 -->
Manche Dateisysteme prüfen beides.
Und manche halten eine zweite Kopie bereit,
sodass sie eine beschädigte Kopie
mithilfe der anderen reparieren können.
Einen Fehler zu erkennen und ihn zu beheben,
ist nicht dasselbe.

<!-- S53 -->
Jedes Dateisystem macht also denselben Job:
nummerierte Blöcke, eine Liste von Namen
und eine Karte dessen, was frei ist.

<!-- S54 -->
Aber die Entscheidungen unterscheiden sich.
Ext4 legt einundsechzig Millionen Einträge an,
bevor du überhaupt etwas speicherst.
NTFS unter Windows führt seine Einträge
in einer großen Tabelle, die nach und nach wächst.

<!-- S55 -->
Und Btrfs legt keine
feste Inode-Tabelle im Voraus an.
Es erzeugt die Inodes, wenn Dateien dazukommen.
Und normalerweise überschreibt es
Daten nicht an Ort und Stelle.
Es schreibt eine neue Kopie
und gibt erst dann die alte frei.

<!-- S56 -->
Standardmäßig bildet es auch Prüfsummen über deine Dateien,
damit es merkt, wenn sie beschädigt wurden.

<!-- S57 -->
Und weil die alte Kopie
nicht überschrieben wird,
kann ein Snapshot sie am Leben halten.
Das ändert die Antwort
auf fast jede Frage in diesem Video:
was ein Absturz anrichtet,
was Löschen bedeutet
und sogar, was eine Kopie ist.

<!-- S58 -->
Genau da setzt das nächste Video an.

<!-- S59 -->
Also, hier eine Frage an dich.
Soll ein Dateisystem deine Dateien nur speichern,
oder soll es sie auch schützen?
Schreib's mir in die Kommentare.
