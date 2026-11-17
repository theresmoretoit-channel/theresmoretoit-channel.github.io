<!-- S01 -->
Stell dir vor, du hast eine verrückte Idee.
Du willst deinen eigenen Satelliten bauen.
Keinen Kommunikationssatelliten
für eine Milliarde Dollar.
Etwas Kleines.

<!-- S02 -->
Eine Box, ungefähr so groß
wie ein Laib Brot.
Drinnen: ein Computer, Solarpanels,
ein Funkgerät, ein paar Sensoren.
Vielleicht sogar eine Kamera.

<!-- S03 -->
Du baust ihn in deiner Garage.
Und dann irgendwie...
bringst du ihn in die Umlaufbahn.
Klingt unmöglich.
Ist es aber nicht.

<!-- S04 -->
Fast genau das machen Menschen
schon seit Jahren.
Man nennt sie CubeSats.

<!-- S05 -->
Und das Überraschende ist,
dass das Schwierigste
nicht der Bau des Satelliten ist.
Es ist alles andere.

<!-- S06 -->
Die Grundeinheit heißt 1U —
ungefähr ein Zehn-Zentimeter-Würfel.
Stapelst du Einheiten,
bekommst du 2U, 3U, 6U
und größer.

<!-- S07 -->
Die Idee ist einfach.
Statt ein neues Raumfahrzeug
von Grund auf zu entwerfen,
nutzt du standardisierte Größen
und standardisierte Schnittstellen.
Und plötzlich ist der Weltraum offen
für Universitäten, Start-ups
und vielleicht sogar dich.

<!-- S07b -->
Übrigens, wenn dir solche Videos
gefallen, abonniere den Kanal.

Das hilft dem Kanal wirklich.

<!-- S08 -->
Was würde unser kleiner Satellit
eigentlich enthalten?
Zuerst braucht er einen Computer.
Irgendwas muss die Software ausführen,
die Hardware steuern
und entscheiden, was zu tun ist.

<!-- S09 -->
Dann die Stromversorgung.
Solarpanels erzeugen Strom.
Batterien speichern ihn
für den Moment, in dem der Satellit
in den Erdschatten gleitet.

<!-- S10 -->
Dann die Kommunikation.
Ein Funkgerät. Eine Antenne.
Und unten auf der Erde
eine lauschende Bodenstation.

<!-- S11 -->
Dann Sensoren.
Temperatur. Spannung. Strom.
Beschleunigung. Magnetfeld.
Und eine Möglichkeit festzustellen,
wohin der Satellit zeigt.
Denn im Orbit ist es überraschend schwer,
zu sagen, wo ‚oben' ist.

<!-- S12 -->
Aber bevor wir einen bauen,
kommt eine unangenehme Frage.
Wie viel kostet diese kleine Box?
Die Antwort lautet...
mehr, als man denken würde.

<!-- S13 -->
Ein einfacher 1U-CubeSat
kann leicht
Zehntausende Dollar kosten —
nur an Flughardware.
Die Stromversorgung. Solarpanels.
Batterien. Der Computer. Das Funkgerät.
Die Lageregelung. Die Struktur.
Und die Nutzlast.

<!-- S14 -->
Dann kommen die Dinge,
die nicht auf der Teileliste stehen.
Tests. Integration.
Dokumentation.
Betrieb der Bodenstation.
Lizenzen.
Und schließlich...
der Start.

<!-- S15 -->
Eine Mitfluggelegenheit für einen winzigen CubeSat
kann Zehntausende kosten.
Bei größeren Missionen und größeren CubeSats
geht es um Hunderttausende Dollar.
Und das ist nur,
um das Ding ins All zu bekommen.

<!-- S16 -->
Und jetzt
ein noch absurderes Problem.
Erinnerst du dich an all die Teile?
Wie um alles in der Welt passt das
alles in eine winzige Box?

<!-- S17 -->
Im All ist kein Platz
für einen wahllosen Haufen Elektronik.
Jeder Zentimeter zählt.
Jedes Gramm zählt.
Jedes Watt zählt.
Der Satellit ist ein dreidimensionales Puzzle,
das einen Raketenstart überstehen muss.

<!-- S18 -->
Wo bekommst du also
all diese Teile?
Du musst nicht alles
selbst entwerfen.
Es gibt eine ganze Industrie,
die Komponenten für kleine Satelliten verkauft:
Computer, Stromversorgungen,
Funkgeräte, Antennen und Solarpanels.
Es gibt sogar Marktplätze,
die eigens für CubeSat-Teile gemacht sind.

<!-- S18b -->
Und die Teile sind außerdem standardisiert.
Viele teilen sich ein Platinenformat
und lassen sich einfach stapeln,
sodass Teile verschiedener Hersteller
in eine Einheit passen.
Firmen wie EnduroSat
und GomSpace verkaufen sie,
und ein einzelnes Subsystem kann
zwischen ein paar Tausend
und Zehntausenden Dollar kosten.

<!-- S19 -->
Und das sind keine
exotischen Prozessoren.
Ein aktueller CubeSat-Computer
nutzt einen ARM Cortex-M7,
mit vertrauten Schnittstellen —
SPI, I²C, UART und CAN.

<!-- S19b -->
Und es ist kein spezieller Weltraumchip.
Es ist eine echte Standardplatine,
die du in der Hand halten könntest.

<!-- S20 -->
Ein Raumfahrzeug braucht etwas
Wichtigeres als reine Rechenleistung:
vorhersehbares Verhalten,
niedrigen Verbrauch und Zuverlässigkeit.
Anspruchsvollere Missionen
können ARM-Cortex-A-Prozessoren nutzen —
und sogar Linux.

<!-- S20b -->
Aber schnell ist er nicht.
Ein typischer CubeSat-Computer
läuft mit ein paar hundert Megahertz.
Dein Laptop läuft mit
vier oder fünf Gigahertz
und viel mehr Kernen.
Er verzichtet auf Rechenleistung
und verbraucht dafür kaum Strom.

<!-- S21 -->
Und wenn du Programmierer bist,
wird es hier interessant.
Du schreibst keine
mysteriöse "Weltraumsprache".
Du schreibst Embedded-Software.
Oft in C oder C++.

<!-- S22 -->
Sie läuft vielleicht direkt
auf der Hardware,
oder auf einem Echtzeitbetriebssystem
wie FreeRTOS, Zephyr oder RTEMS.
Es gibt sogar offene Frameworks,
die für Raumfahrzeuge gebaut sind.
NASAs F Prime zum Beispiel
ist ein Flugsoftware-Framework
für Embedded- und Raumfahrtsysteme.

<!-- S23 -->
Dein Code könnte also
ungefähr so aussehen.

<!-- S24 -->
Aber es gibt einen riesigen Unterschied
zu einem normalen Computer.
Du kannst dich nicht per SSH einloggen.
Du kannst keinen Debugger anschließen.
Und wenn deine Software abstürzt...
ist dein Computer
ein paar hundert Kilometer weit oben.

<!-- S25 -->
Also braucht er Watchdogs,
Sicherheitsmodi, Fehlererkennung
und automatische Wiederherstellung.
Manche Probleme muss er lösen,
ohne dass du dabei hilfst.

<!-- S25b -->
Und ein großer Grund dafür
ist Strahlung.
Im All können kosmische Strahlen
ein Bit im Speicher umkippen
oder sogar einen Chip lahmlegen.
Eine schwere Abschirmung gibt es nicht —
die würde viel zu viel wiegen.
Stattdessen überwacht sich der Computer selbst,
korrigiert Fehler
und startet neu, wenn etwas schiefgeht.

<!-- S26 -->
Aber wenn du ihn wirklich
starten willst...
wird es ernst.
Ein Bauteil, das auf deinem Schreibtisch funktioniert,
ist nicht automatisch bereit
für eine Rakete.
Es muss Vibration,
Vakuum, Temperaturextreme
und Strahlung überstehen.

<!-- S27 -->
Jetzt zurück zu dem Problem,
zu wissen, wohin
der Satellit zeigt.
Stell dir vor, wie er
durch den Weltraum taumelt.
Kein Boden. Keine Decke.
GPS kann dir sagen,
wo du bist...
aber nicht, in welche Richtung
du blickst.

<!-- S28 -->
Also kombinieren Satelliten
Gyroskope, Magnetometer
und Sonnensensoren,
um ihre Lage zu bestimmen.
Und dann müssen sie sie ändern.
Ein gängiger Trick
ist ein Magnetorquer.

<!-- S29 -->
Er drückt gegen
das Magnetfeld der Erde
und erzeugt ein winziges Drehmoment.
Es ist kein Raketentriebwerk.
Es bewegt den Satelliten nicht.
Es dreht ihn nur.
Und das genügt,
um den Satelliten
genau dorthin auszurichten, wohin du willst.

<!-- S30 -->
Aber nichts davon
ist der Grund,
warum wir den Satelliten gebaut haben.
Wir brauchen eine Mission.
Das ist die Nutzlast.
Strahlung messen.
Die Erde fotografieren.
Die Atmosphäre erforschen.
Einen neuen Sensor testen.
Oder einfach beweisen,
dass eine neue Technik funktioniert.

<!-- S31 -->
Der Satellit selbst
ist vor allem dazu da,
die Nutzlast am Leben zu halten.
Sie versorgen. Sie ausrichten.
Sie warm halten.
Ihre Daten speichern.
Und sie nach Hause schicken.

<!-- S32 -->
Wenn dein Rechner einfriert,
startest du ihn neu.
Wenn dein Satellit einfriert...
hast du ein sehr teures Objekt,
das stumm die Erde umkreist.

<!-- S33 -->
Sagen wir, wir haben ihn gebaut.
Alles funktioniert...
Der Computer startet...
Das Funkgerät sendet.
Die Panels erzeugen Strom.
Die Nutzlast läuft...
Können wir ihn starten?
...Noch nicht.

<!-- S34 -->
Ein Satellit muss beweisen,
dass er den Start übersteht.
Das bedeutet Tests.
Viele Tests.

<!-- S35 -->
Zuerst schraubst du ihn
auf einen riesigen Rütteltisch.
Dann rüttelst du ihn kräftig durch...
Das ist ein Vibrationstest.
Raketenstarts sind nicht sanft.
Er muss
Lärm, Vibration und Erschütterung überstehen,
ohne dass sich etwas
löst oder bricht.
Jede Schraube zählt.
Jeder Steckverbinder zählt.
Jedes Stück Kabel zählt.

<!-- S36 -->
Dann kommt das Vakuum.
Auf der Erde führt die Luft Wärme ab.
Im All gibt es keine Luft.
Eine Seite kann extrem heiß werden,
eine andere extrem kalt,
und die Elektronik
darf trotzdem weder zu heiß
noch zu kalt werden.
Also braucht der Satellit
Wärmeleitbänder, Beschichtungen,
Isolierung
und sorgfältig gewählte Materialien.
Satelliten haben keine
Klimaanlage.
Sie haben Physik.

<!-- S37 -->
Und bei der Batterie
wird es spannend.
Lade sie mit Sonnenlicht.
Dann gleitet der Satellit
in den Erdschatten,
und die Panels erzeugen fast nichts.
Die Batterie hält ihn am Leben.
Dann zurück ins Sonnenlicht.
Laden. Entladen.
Laden. Entladen.
Wieder und wieder.
Jahrelang.
Ein Fehler in der Stromversorgung
könnte die Mission still beenden.

<!-- S38 -->
Und wie sprichst du jetzt mit ihm?
Du brauchst ein Funkgerät.
Eine Antenne.
Und eine Frequenz,
die du legal nutzen darfst.
Und eine Bodenstation.
Der Satellit
hat kein Internet.
Er fliegt nur über dich hinweg
und sendet.

<!-- S39 -->
Deine Bodenstation
fängt das Signal ein.
Der Computer dekodiert es.
Und plötzlich hast du Daten
von deinem eigenen Raumfahrzeug.
Stell dir vor, du öffnest ein Terminal
und siehst das.

Nur dass die Maschine,
die diese Zahlen ausgibt...
Hunderte Kilometer
über deinem Kopf ist.

<!-- S40 -->
Wie bekommen wir ihn
also tatsächlich dort hinauf?
Du könntest eine Rakete bauen...
Bitte nicht...
Du brauchst keine.
CubeSats fliegen
als sekundäre Nutzlast.

<!-- S41 -->
Eine Rakete startet ohnehin.
Sie hat Platz übrig.
Dein Satellit fährt mit
in einem Standard-Deployer.
Keine eigene Rakete nötig.

<!-- S42 -->
Und jetzt sitzt er
auf der Spitze einer Rakete.
Du kannst ihn nicht anfassen.
Du kannst die Box nicht öffnen.
Du kannst kein Kabel anschließen.
Die Rakete startet.
Etwa neun Minuten später
bist du in der Umlaufbahn.

<!-- S43 -->
Der Deployer
gibt deinen Satelliten frei.
Er schnellt heraus
und beginnt zu taumeln.

<!-- S43b -->
Aber woher weiß er, dass er draußen ist?
...
Gefederte Schalter, die eingedrückt waren,
während er im Deployer saß,
springen im Moment des Auswurfs heraus,
und der Computer startet.
Dann bleibt er, laut Vorschrift,
etwa eine halbe Stunde lang still.
Erst dann schaltet er sein Funkgerät ein,
entfaltet seine Antennen
und meldet sich endlich zu Hause.
Und irgendwo auf der Erde...
hört ihn deine Bodenstation.

<!-- S44 -->
Du hast eine Maschine gebaut.
Und jetzt umkreist
diese Maschine den Planeten.

<!-- S44b -->
Nur sind wir noch nicht fertig.
Ein toter Satellit kann nicht einfach
für immer dort oben bleiben.
Bleibt er jahrhundertelang im Orbit,
wird er zu Weltraumschrott.

<!-- S45 -->
Das heißt, moderne Missionen
müssen immer öfter
das Ende
der Lebensdauer des Raumfahrzeugs einplanen.
Idealerweise zieht die dünne obere Atmosphäre
ihn langsam nach unten.
Seine Umlaufbahn sinkt.
Er tritt wieder in die Atmosphäre ein.
Und er verglüht.
Das Ende der Mission...
ist Teil der Mission.

<!-- S46 -->
Also... könntest du
deinen eigenen Satelliten bauen?
Technisch gesehen ja.
Du musst nicht die NASA sein.
Du musst keine
Rakete besitzen.
Du brauchst nicht einmal zwingend
eine riesige Firma.

<!-- S47 -->
Der Satellit muss
den Start überstehen.
Den Weltraum überstehen.
Legal kommunizieren.
Von allein laufen.
Und am Ende
die Umlaufbahn räumen.
Das alles
muss bewiesen werden,
bevor jemand
ihn auf eine Rakete setzt.

<!-- S48 -->
CubeSats haben den Weltraum nicht einfach gemacht.
Sie haben ihn standardisiert.
Statt alles
von Grund auf zu bauen,
kannst du etwas bauen,
das zu einem bestehenden Standard passt.
Und das ist eine überraschend große Veränderung.

<!-- S49 -->
Irgendwo, genau jetzt,
umkreisen winzige Maschinen
die Erde.
Gebaut von Universitäten,
Forschungsteams,
Firmen und Studenten.

<!-- S50 -->
Manche tragen Kameras.
Manche messen Strahlung.
Manche testen
brandneue Technik.
Und manche sind nur Experimente
mit einer einzigen Frage:
"Kriegen wir das Ding
im All zum Laufen?"

<!-- S51 -->
Und genau das macht
den Bau eines eigenen Satelliten
so faszinierend.
Denn die Distanz
zwischen dir und dem Weltraum
ist keine Rakete mehr.
Vielleicht ist es...
eine Zehn-Zentimeter-Box.
Und eine sehr, sehr
lange Checkliste.
