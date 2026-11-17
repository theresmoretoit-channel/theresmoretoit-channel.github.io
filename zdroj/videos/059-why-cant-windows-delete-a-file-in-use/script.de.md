<!-- S01 -->
Du willst eine Datei löschen.
Der Rechner sagt, sie sei offen
in einem anderen Programm.
Nur in welchem, sagt er nicht.

<!-- S02 -->
Diese Meldung ist das sichtbare Ende
einer viel merkwürdigeren Frage.
Was heißt es eigentlich,
eine Datei zu öffnen?

<!-- S03 -->
Denn auf einem anderen Rechner
lässt sich dieselbe Datei, auf dieselbe Weise geöffnet,
ohne jeden Einwand löschen.

<!-- S04 -->
Dieselbe Datei.
Dieselbe Aktion.
Zwei völlig verschiedene Antworten.

<!-- S05 -->
Fangen wir mit dem an,
was alle ärgert.
Welches Programm?

<!-- S06 -->
Windows weiß es.
Es hat ein Kernel-Objekt
für diese offene Datei
und kennt den Besitzerprozess.
Es könnte ihn benennen.

<!-- S07 -->
Also schließt du wahllos Programme.
Du öffnest den Task-Manager.
Du starrst auf eine Prozessliste
und erkennst fast keinen davon.

<!-- S08 -->
Und jahrelang
war die Antwort tatsächlich,
ein separates Tool herunterzuladen.
Unlocker erschien 2005,
und unter Windows XP war das die Antwort.

<!-- S09 -->
Dann brachte Windows 7
den Ressourcenmonitor.
Die Registerkarte CPU.
Eine Liste namens Zugeordnete Handles.

<!-- S10 -->
Tippe den Dateinamen ein.
Du bekommst das Programm
und die Prozess-ID.
Nichts zu installieren.
Das gibt es seit 2009.

<!-- S10b -->
Die separaten Tools taten aber
mehr, als es dir nur zu sagen.
Sie konnten das Handle schließen
und die Datei freigeben.

<!-- S11 -->
Womit wir zurück
bei der Frage wären.
Was hat das Programm bekommen,
als es die Datei öffnete?

<!-- S12 -->
Nehmen wir an, ein Player öffnet
eine Datei namens movie.mp4.
Unter Windows bedeutet das Öffnen
einer Datei, zwei Dinge festzulegen.

<!-- S13 -->
Das erste ist offensichtlich.
Was will ich damit machen?
Sie lesen. In sie schreiben.

<!-- S14 -->
Das zweite ist das interessante.
Was dürfen alle anderen tun,
solange ich sie offen habe?

<!-- S15 -->
Das ist eine echte Einstellung.
Du legst fest, was andere Programme
dürfen, solange du sie geöffnet hast.

<!-- S16 -->
Sie dürfen sie lesen.
Sie dürfen auch hineinschreiben.
Sie dürfen sie löschen oder umbenennen.

<!-- S16b -->
Oder gar nichts davon.
Solange ich sie benutze,
rührt sie niemand an.

<!-- S17 -->
Das Flag, das Löschen erlaubt,
heißt FILE_SHARE_DELETE.
Und Microsofts Dokumentation
fügt direkt darunter eine Zeile hinzu.

<!-- S18 -->
Der Löschzugriff umfasst
Löschen und Umbenennen zugleich.

<!-- S19 -->
Ein Programm, das die Freigabe
zum Löschen verweigert,
hat also auch das Umbenennen gesperrt.

<!-- S20 -->
Und wenn das Programm, das die Datei
geöffnet hat, sie nicht erteilt,
kann sie sich niemand nehmen.

<!-- S21 -->
Deshalb heißt der Fehler
nicht Datei in Benutzung.
Er heißt Freigabeverletzung.

<!-- S22 -->
Die Antwort steckte die ganze Zeit
im Namen
des Fehlers selbst.

<!-- S23 -->
Jetzt dasselbe
auf einem Linux-Rechner.
Ein Player öffnet das Video.

<!-- S24 -->
Und du tippst
rm movie.mp4.

<!-- S24b -->
Es klappt.
Das Video läuft weiter.

<!-- S25 -->
Was hat das Programm also bekommen,
wenn es die Datei nicht festhält?

<!-- S26 -->
Das ist die ganze Idee
dieses Videos.
Der Name ist nicht die Datei.

<!-- S27 -->
movie.mp4 ist eine Zeile
in einem Verzeichnis.
Diese Zeile zeigt auf ein Objekt,
in dem die eigentlichen Daten liegen.

<!-- S28 -->
Wenn ein Programm die Datei öffnet,
bekommt es einen Verweis
auf das Objekt.
Nicht auf die Zeile.

<!-- S29 -->
Die Datei zu löschen
entfernt also die Zeile.
Das Objekt bleibt unberührt.

<!-- S30 -->
Die Handbuchseite sagt es
in einem einzigen Satz.
Die Datei bleibt bestehen,
bis der letzte Dateideskriptor,
der auf sie verweist, geschlossen ist.

<!-- S31 -->
Das klingt abstrakt,
bis man es einmal sieht.
Ich habe also eine Protokolldatei
von fünfhundert Megabyte angelegt
und einen Prozess die Datei geöffnet halten lassen.

<!-- S31b -->
Dann habe ich sie gelöscht.

<!-- S32 -->
Die Verzeichnisliste
zeigt überhaupt nichts.
Das Werkzeug, das die Ordnergröße
misst, meldet null.

<!-- S33 -->
Und das Werkzeug, das den freien
Platz auf der Platte misst,
meldet, dass fünfhundert Megabyte
immer noch fehlen.

<!-- S33b -->
Ein leerer Ordner.
Ein halbes Gigabyte weg.

<!-- S34 -->
Das passiert oft genug,
dass es einen eigenen Befehl gibt,
nur um solche Dateien zu finden.
Gelöscht, unsichtbar, noch auf der Platte.

<!-- S35 -->
Und der Platz kommt zurück,
sobald dieser eine Prozess
die Datei loslässt.

<!-- S36 -->
Dasselbe gilt fürs Umbenennen.
Verschiebe sie, während sie geöffnet ist,
und das Programm merkt es nicht.

<!-- S37 -->
Das Handbuch ist auch da deutlich.
Offene Dateideskriptoren
für den alten Pfad bleiben unberührt.

<!-- S37b -->
Es hat den Namen nie benutzt.

<!-- S38 -->
Das hat eine Grenze,
die man kennen sollte.
Ein laufendes Programm
lässt sich nicht an Ort und Stelle überschreiben.

<!-- S38b -->
Linux weigert sich.
Text file busy.

<!-- S39 -->
Was geht,
ist den Namen zu entfernen
und eine neue Datei hinzulegen.

<!-- S40 -->
Der alte Prozess läuft weiter
mit einem Objekt,
das keinen Namen mehr hat.
Alles später Gestartete bekommt das neue.

<!-- S41 -->
Damit bestätigt sich dieselbe
Idee noch einmal.
Vieles lässt sich austauschen,
ohne das Objekt selbst anzufassen.

<!-- S41b -->
Deshalb kann Linux ein Programm
im laufenden Betrieb aktualisieren.
Die neue Version bekommst du nur,
wenn du es neu startest.

<!-- S42 -->
Ist Windows also
schlicht schlechter entworfen?

<!-- S42b -->
Nein.
Und das ist der Teil,
den kaum jemand kennt.

<!-- S43 -->
Windows hat einen Weg,
genau dasselbe zu tun.

<!-- S43b -->
Auf NTFS kann Windows
ein Löschen im POSIX-Stil anfordern.

<!-- S44 -->
Microsoft beschreibt,
was dann passiert.
Der Name verschwindet
aus dem sichtbaren Namensraum.

<!-- S45 -->
Und Anwendungen, die die Datei
schon offen hatten, nutzen sie weiter,
obwohl der Name,
mit dem sie sie öffneten, weg ist.

<!-- S46 -->
Das ist das Unix-Verhalten.
Auf NTFS.
Von Microsoft dokumentiert.

<!-- S47 -->
Beide Systeme können beides.
Was sich unterscheidet, ist die Vorgabe.
Das, was du bekommst, wenn du eine
Datei öffnest, ohne nachzudenken.

<!-- S48 -->
Unter Windows bekommst du einen Vertrag.
Unter Unix bekommst du einen Verweis
auf ein Objekt.

<!-- S49 -->
Was nach einer Frage
für Programmierer klingt,
bis man diese eine Meldung
gesehen hat.

<!-- S50 -->
Starten Sie den Computer neu,
um die Updates abzuschließen.

<!-- S51 -->
Angenommen, Windows muss
eine Bibliothek ersetzen, die ein Prozess
unter dem strengen Vertrag offen hält.

<!-- S52 -->
Es kann die Datei
unter dem Prozess nicht tauschen.
Also muss etwas loslassen.

<!-- S53 -->
Die Anwendung beenden.
Den Dienst stoppen.
Oder die ganze Sache
dem Neustart-Manager überlassen.

<!-- S54 -->
Der ist ein echter Bestandteil.
Er fährt alles der Reihe nach herunter.
Windows-Anwendungen,
dann Konsolenprogramme,

<!-- S55 -->
dann Dienste,
und den Explorer zuletzt.
Danach startet er sie wieder.

<!-- S56 -->
Und es gibt ihn aus einem Grund,
den Microsoft klar ausspricht,
in der eigenen Dokumentation.

<!-- S57 -->
Der Hauptgrund,
warum Softwareinstallationen
und Updates einen Neustart
des Systems verlangen...

<!-- S58 -->
ist, dass einige der Dateien,
die aktualisiert werden, gerade
von einer laufenden Anwendung
oder einem Dienst benutzt werden.

<!-- S59 -->
Es wäre zu ordentlich, hier zu enden.
Freigaberegeln sind nicht der einzige
Grund, warum ein Rechner zu einem Neustart auffordert.

<!-- S60 -->
Ein Kernel-Update ist etwas anderes.
Den Kernel unter sich selbst
zu tauschen geht nicht.

<!-- S61 -->
Linux hat dasselbe Problem,
auch wenn Live-Patching
einen Neustart manchmal erspart.

<!-- S62 -->
Die ehrliche Fassung
behauptet also weniger
als die befriedigende.

<!-- S63 -->
Wie Windows mit Dateien in Benutzung
umgeht, machte manche Bestandteile
im Betrieb schwerer austauschbar,
und das hat dazu beigetragen.

<!-- S64 -->
Denn jede Entwurfsentscheidung
hat irgendwo eine Folge.

<!-- S65 -->
Windows lässt das Programm,
das eine Datei öffnet, entscheiden,
was andere mit ihr tun dürfen.

<!-- S66 -->
Der Preis ist, dass du manchmal
deine eigene Datei nicht löschen kannst,
weil ein anderes Programm
es nicht erlaubt hat.

<!-- S67 -->
Unix trennt Name
und Objekt voneinander,
so lässt sich vieles austauschen,
während das System läuft.

<!-- S68 -->
Der Preis ist ein halbes Gigabyte,
das von der Platte verschwand
und zu gar keiner Datei gehört.

<!-- S69 -->
Und sieh dir an, wie sich
beides jeweils auflöst.
Unter Windows ist ein Ausweg,
das Programm zu beenden,
das die Datei hält.

<!-- S70 -->
Unter Linux ist ein Weg,
den Platz zurückzubekommen,
den Dienst neu zu starten,
der sie noch offen hat.

<!-- S71 -->
Verschiedene Ursachen.
Manchmal dasselbe Mittel.

<!-- S71b -->
Übrigens, wenn du sehen willst,
wohin uns die nächste Frage führt,
denk übers Abonnieren nach.
Das hilft dem Kanal sehr.

<!-- S72 -->
Also. Die Frage vom Anfang.
Was heißt es,
eine Datei zu öffnen?

<!-- S73 -->
Es heißt, dass du etwas hältst.
Die beiden Systeme geben dir
schlicht Verschiedenes in die Hand.

<!-- S74 -->
Deshalb hat diese Meldung
nie wirklich gesagt,
dass die Datei nicht löschbar ist.

<!-- S75 -->
Sie sagte, dass das Programm,
das sie geöffnet hat,
es dir nicht erlaubt hat.

<!-- S75b -->
Und es weiß, welches Programm.
Es hat es nur nicht erwähnt.
