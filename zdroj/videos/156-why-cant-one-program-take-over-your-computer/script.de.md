<!-- S01 -->
Am 19. Juli 2024
verschickte die Sicherheitsfirma CrowdStrike
ein routinemäßiges Update.

<!-- S02 -->
Kein neues Programm.
Nur eine kleine Konfigurationsdatei.

<!-- S03 -->
Innerhalb weniger Stunden hingen 8,5 Millionen
Windows-Rechner fest,
auf einem Bluescreen.

<!-- S04 -->
Fluglinien strichen Flüge.
Krankenhäuser sagten Operationen ab.
Ein Nachrichtensender war nicht mehr auf Sendung.

<!-- S05 -->
Und der Fehler dahinter
war ein ganz gewöhnlicher.
Das Programm erwartete 20 Werte.
Das Update lieferte ihm 21.

<!-- S06 -->
Deine Spiele und Apps machen
ständig solche Fehler.
Dann schließt sich das Spiel,
und du startest es neu.

<!-- S07 -->
Dieselbe Art von Fehler.
Der eine schließt ein Fenster.
Der andere legt
8,5 Millionen Rechner lahm.

<!-- S08 -->
Der Unterschied liegt nicht im Fehler.
Sondern darin, wo der Code lief.

<!-- S09 -->
Warum kann also nicht ein Programm
deinen Computer übernehmen...
und warum konnte es dieses hier?

<!-- S10 -->
Das war nicht immer so.

<!-- S11 -->
Auf einem PC mit DOS in den 1980ern
hielt im Prozessor nichts ein Programm auf.
Es konnte überallhin in den Speicher schreiben
und direkt mit der Hardware reden.

<!-- S12 -->
Ein einziges Programm, das
irgendwohin schrieb, wo es nicht sollte,
konnte das Betriebssystem überschreiben,
und der ganze Rechner fror ein.

<!-- S13 -->
Die Lösung: Programmen nicht mehr vertrauen
und das Misstrauen
dem Prozessor überlassen.

<!-- S14 -->
1982 führte Intels Prozessor 80286
den Protected Mode ein,
mit vier Berechtigungsstufen.

<!-- S15 -->
Meist zeichnet man sie
als vier Ringe, einen im anderen.

<!-- S16 -->
Ring 0 ist in der Mitte.
Ring 3 ist ganz außen.

<!-- S17 -->
Und die Zählung läuft rückwärts.
Je niedriger die Zahl,
desto mehr darf der Code.

<!-- S18 -->
Ring 0 gehört dem Kernel,
dem Kern des Betriebssystems.
Er teilt den Speicher zu,
entscheidet, welches Programm als Nächstes läuft,
und redet mit der Hardware.

<!-- S19 -->
In Ring 3 laufen dein Browser,
deine Spiele und dein Texteditor.
Das nennt man User Mode.

<!-- S19b -->
Windows, macOS und Linux
teilen die Arbeit alle so auf.
Der Kernel in Ring 0,
deine Apps in Ring 3.

<!-- S19c -->
Handys und Apples neuere Macs
nutzen stattdessen ARM-Chips.
Dort heißen die Stufen Exception Levels.
Anderer Name, gleiche Aufteilung:
eine für den Kernel, eine für deine Apps.

<!-- S20 -->
Der Prozessor weiß immer,
in welchem Ring er gerade läuft.
Und er prüft es.

<!-- S21 -->
Manche Befehle funktionieren nur in Ring 0.
Zum Beispiel Interrupts abschalten
oder ändern, wie der Speicher abgebildet wird.

<!-- S22 -->
Versucht ein Programm in Ring 3 so einen,
verweigert der Prozessor.
Er löst eine Exception aus
und übergibt die Kontrolle an den Kernel,
der das Programm meist beendet.

<!-- S23 -->
Mit dem Speicher ist es genauso.
Jede Speicherseite ist markiert,
entweder als User oder als Supervisor.

<!-- S24 -->
Ein Programm in Ring 3,
das eine Supervisor-Seite anfasst,
bekommt die Daten nicht.
Es wird gestoppt.

<!-- S25 -->
Dein Browser und dein Spiel
laufen beide in Ring 3.
Was sie trennt, ist,
dass jedes seine eigene Karte des Speichers bekommt.
Der Speicher des anderen Programms
steht darauf einfach nicht.

<!-- S26 -->
Wenn also ein Spiel abstürzt,
bleibt der Schaden im Spiel.
Der Kernel räumt auf.
Alles andere läuft weiter.

<!-- S27 -->
Und jetzt noch mal zu CrowdStrike.
Sein Treiber lief in Ring 0,
direkt neben dem Kernel.

<!-- S28 -->
Über Ring 0 gibt es nichts mehr,
das so einen Fehler abfangen kann.

<!-- S29 -->
Also tat Windows das einzig Sichere, was blieb.
Es hielt den ganzen Rechner an, absichtlich,
statt mit Speicher weiterzuarbeiten,
dem es nicht mehr trauen konnte.

<!-- S30 -->
Genau das ist der Bluescreen.

<!-- S31 -->
Und weil der Treiber jedes Mal startete,
wenn Windows startete,
brachte jeder Neustart den Absturz zurück.

<!-- S32 -->
Aber da stellt sich eine Frage.
Wenn dein Browser die Hardware nicht anfassen darf,
wie speichert er dann überhaupt eine Datei
oder schickt etwas übers Netzwerk?

<!-- S33 -->
Er bittet darum.

<!-- S34 -->
Das Programm legt seine Anfrage
in die Register des Prozessors.
Welche Datei. Wohin die Daten sollen.
Wie viele.

<!-- S35 -->
Dann führt es einen besonderen Befehl aus.
Auf einem modernen PC heißt er SYSCALL.

<!-- S36 -->
In diesem Moment wechselt der Prozessor
von Ring 3 in Ring 0...

<!-- S37 -->
aber er springt nicht dorthin,
wohin das Programm will.
Er springt an einen einzigen Einstiegspunkt,
den der Kernel vorher festgelegt hat.

<!-- S38 -->
Der Kernel prüft die Anfrage,
erledigt die Arbeit
und kehrt in Ring 3 zurück.
Das Programm hat die Festplatte nie selbst berührt.

<!-- S39 -->
Das ist ein Systemaufruf,
und er passiert ständig.

<!-- S40 -->
Wir haben sie auf einem Laptop gezählt.
Ein Programm, das gar nichts tut,
macht trotzdem 30.

<!-- S41 -->
Firefox machte beim Start
und beim Laden einer Wikipedia-Seite
etwa 670.000
in 20 Sekunden...
obwohl unser Zählen ihn noch bremste.

<!-- S42 -->
Jeder davon
ist ein Gang durch die Wand und zurück.

<!-- S43 -->
Bleibt etwas Seltsames.
Vier Ringe,
und wir haben nur zwei gebraucht.

<!-- S44 -->
Was ist aus Ring 1 und 2 geworden?

<!-- S45 -->
Die Idee der Ringe ist älter als der PC.
Multics, ein Betriebssystem
aus den späten 1960ern,
hatte acht davon.

<!-- S46 -->
Die Idee: Schichten des Vertrauens.
Der Kern des Systems in der Mitte,
weniger vertrauenswürdige Dienste darum herum
und die Programme ganz außen.

<!-- S46b -->
Intel zeichnete dasselbe Bild.
Ring 1 und 2 waren gedacht
für die Schichten dazwischen,
etwa Treiber und Systemdienste.
Mehr Vertrauen als deine Apps,
weniger als der Kernel.

<!-- S47 -->
Zwei Dinge kamen dazwischen.

<!-- S48 -->
Erstens: Systeme wie Unix und Windows NT
waren dafür gebaut,
auf vielen Prozessortypen zu laufen.

<!-- S49 -->
Und die eine Aufteilung,
die jeder Prozessor bot,
waren zwei Stufen.
Eine für den Kernel,
eine für alles andere.

<!-- S50 -->
Zweitens: der x86-Prozessor selbst.
Wenn er Speicher abbildet,
kennt jede Seite nur zwei Zustände.
User oder Supervisor.

<!-- S51 -->
Ring 1 und 2 zählen als Supervisor.
Ein Treiber in Ring 1
könnte also trotzdem den Speicher des Kernels anfassen.
Der zusätzliche Ring würde wenig schützen.

<!-- S51b -->
Ein paar Systeme nutzten sie trotzdem.
OS/2 ließ manche Programme in Ring 2,
nur damit sie direkt mit der Hardware reden konnten.

<!-- S51c -->
Und bevor Prozessoren Unterstützung
für virtuelle Maschinen hatten,
verschoben Xen und VirtualBox den Kernel des Gastsystems
in Ring 1,
damit das System darunter
Ring 0 für sich behalten konnte.

<!-- S52 -->
2023 schlug Intel vor,
Ring 1 und 2 ganz abzuschaffen.

<!-- S53 -->
Im Dezember 2024 ließ Intel den Plan fallen.
Sie sind immer noch in deinem Prozessor.
Fast nichts nutzt sie.

<!-- S54 -->
Bis hierhin klingt das beruhigend.
Die Regeln stecken in der Hardware,
und die Hardware prüft jeden Zugriff.

<!-- S55 -->
2017 fanden drei Forscherteams,
unabhängig voneinander,
einen Weg durch diese Wand.

<!-- S56 -->
Sie nannten ihn Meltdown.
Und um ihn zu verstehen,
brauchst du einen Trick,
den moderne Prozessoren anwenden.

<!-- S57 -->
Ein Prozessor wartet nicht,
bis ein Befehl fertig ist,
bevor er mit dem nächsten beginnt.
Er arbeitet schon vor,
an Befehlen, die er wahrscheinlich gleich braucht.

<!-- S58 -->
Wenn er falsch geraten hat,
wirft er die Ergebnisse weg,
als wäre nichts gewesen.

<!-- S59 -->
Hier ist der Fehler.
Auf betroffenen Intel-Chips
konnte ein Programm in Ring 3
ein Byte aus dem Kernel-Speicher anfordern...

<!-- S60 -->
und der Prozessor holte es
und gab es an die nächsten Befehle weiter,
bevor er fertig geprüft hatte,
ob das erlaubt war.

<!-- S61 -->
Die Prüfung schlug zwar fehl.
Das Ergebnis wurde verworfen.

<!-- S62 -->
Aber diese nächsten Befehle
hatten das geheime Byte schon benutzt,
um ein Stück
vom eigenen Speicher des Programms
in den Cache des Prozessors zu holen.

<!-- S63 -->
Und der Cache vergisst nicht,
nur weil das Ergebnis verworfen wurde.

<!-- S64 -->
Also misst das Programm,
wie schnell es an jedes Stück seines Speichers kommt.
Das eine Stück, das schnell da ist,
verrät das geheime Byte.

<!-- S65 -->
Byte für Byte
konnte ein gewöhnliches Programm
den Speicher des Kernels lesen,
samt allen Geheimnissen, die darin lagen.
Passwörter und kryptografische Schlüssel inklusive.

<!-- S66 -->
Meltdown betraf Intel-Prozessoren
bis zurück ins Jahr 1995.

<!-- S67 -->
Öffentlich wurde es
am 3. Januar 2018.

<!-- S68 -->
Die Lösung konnte das Silizium nicht ändern.
Also änderten die Betriebssysteme die Karte.

<!-- S69 -->
Während dein Programm läuft,
ist der Speicher des Kernels jetzt
fast vollständig von seiner Karte entfernt.
Da gibt es nichts mehr zu holen.

<!-- S70 -->
Aber denk an die Systemaufrufe.
Jeder Gang durch die Wand
muss jetzt auch die Karte tauschen.

<!-- S71 -->
Red Hat hat die Patches gegen Meltdown
und eine verwandte Lücke, Spectre, gemessen.
Unter 1 % bei mancher Arbeit...
bis zu 19 % bei stark ausgelasteten Datenbanken.

<!-- S72 -->
Die Regel war die ganze Zeit richtig.
Der Prozessor hat sie nur zu spät geprüft.

<!-- S73 -->
Und damit sind wir zurück bei CrowdStrike
und bei einer schwierigeren Frage.

<!-- S74 -->
Warum lief ein Sicherheitsprogramm
überhaupt in Ring 0?

<!-- S75 -->
Weil es von dort alles sieht.
Es startet vor anderer Software.
Und Malware mit Administratorrechten
kann es schwerer abschalten.

<!-- S76 -->
Microsofts eigene Liste
endet mit einer Warnung.
Kernel-Treiber bieten das auf Kosten der Ausfallsicherheit.

<!-- S77 -->
Nach dem Ausfall
begann Microsoft, einen Weg zu bauen,
damit Antivirensoftware
außerhalb des Kernels laufen kann.

<!-- S78 -->
Im Herbst 2026
gibt es das immer noch nur in Testversionen von Windows.
Und für Sicherheitsfirmen
ist der Kernel nicht geschlossen worden.

<!-- S79 -->
Deine Spiele stehen vor demselben Dilemma.

<!-- S80 -->
Cheats, die im Kernel laufen,
sind unsichtbar für ein Anti-Cheat,
das in Ring 3 läuft.

<!-- S81 -->
Also zog das Anti-Cheat auch dort ein.
Riots Vanguard, genutzt von Valorant,
setzt einen Treiber in Ring 0.
Auf den meisten PCs lädt er schon beim Windows-Start...
auch wenn du das Spiel nie öffnest.

<!-- S82 -->
Das macht ihn nicht fehlerhaft.
Aber er sitzt an derselben Stelle
wie damals der CrowdStrike-Treiber,
wo ein Fehler den ganzen Rechner anhält.

<!-- S83 -->
Warum kann also nicht ein Programm
deinen Computer übernehmen?

<!-- S84 -->
Weil der Prozessor
fast jedes Programm aus der Mitte fernhält
und es jedes Mal prüft, wenn es anklopft.

<!-- S85 -->
Aber der Prozessor kann nicht entscheiden,
wer hereingelassen wird.
Das entscheiden Menschen...
jedes Mal, wenn sie einen Treiber installieren.

<!-- S86 -->
Also, eine Frage für die Kommentare.
Wer sollte entscheiden, welche Programme
in Ring 0 dürfen:
du, Microsoft
oder die Firmen, die sie herstellen?
