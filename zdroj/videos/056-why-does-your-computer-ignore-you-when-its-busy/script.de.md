<!-- S01 -->
Du klickst auf einen Knopf.
Nichts passiert.
Du klickst noch einmal.
Immer noch nichts.

<!-- S02 -->
Du bewegst die Maus.
Nichts.
Ein paar Sekunden lang
wirkt der Rechner völlig tot.

<!-- S03 -->
Und dann passiert alles auf einmal.
Das Fenster springt.
Das Menü klappt auf.
Alle deine Klicks kommen an,
alle zusammen.

<!-- S04 -->
Und jetzt das Seltsame.
Der Rechner wusste von dem Klick.
Er wusste es binnen Mikrosekunden.

<!-- S05 -->
Das ist keine Vermutung.
Gerade jetzt, während du
nichts Besonderes tust,
verarbeitet deine Maschine Tausende
Hardware-Ereignisse pro Sekunde.

<!-- S06 -->
Ein Tastendruck.
Ein ankommendes Paket.
Ein Timer, der ausläuft.
Eine Platte, die einen Auftrag beendet.

<!-- S07 -->
Jedes davon ist ein Interrupt,
und Rechner machen das
schon seit den Fünfzigern,
genau zu diesem Zweck:

<!-- S08 -->
damit ein Prozessor auf die Welt
außerhalb seiner selbst reagieren kann.

<!-- S09 -->
Die Hardware hat den Klick gemeldet.
Der Prozessor hat ihn bemerkt.
Und du saßt trotzdem fünf Sekunden
vor einem toten Bildschirm.

<!-- S10 -->
Sollte der Nutzer nicht Vorrang haben?

<!-- S11 -->
Es gibt eine Antwort,
und sie lautet nicht,
dein Rechner sei zu langsam.

<!-- S12 -->
Sie lautet: bemerkt werden
und bedient werden
sind zwei völlig verschiedene Dinge.

<!-- S13 -->
Fangen wir beim Bemerken an.
Denk dir einen Rechner ohne Interrupts.

<!-- S14 -->
Der Prozessor müsste
immer wieder fragen:
Kam etwas von der Tastatur?
Ist die Platte fertig?

<!-- S15 -->
Kam ein Paket an?
Hat sich die Maus bewegt?
Und dann wieder fragen.
Und wieder.

<!-- S16 -->
Fast jede Antwort wäre nein,
und das Fragen selbst
würde die Maschine auffressen.

<!-- S17 -->
Also bekamen Geräte eine Möglichkeit,
sich zu melden. Die Maus bewegt sich,
die Hardware löst einen Interrupt aus,

<!-- S18 -->
und der Prozessor lässt fallen,
was er gerade tat,
springt in ein kurzes Stück Code,
das man Handler nennt,

<!-- S19 -->
und das Betriebssystem erfährt,
dass etwas passiert ist.

<!-- S20 -->
Das ist eine großartige Idee.
Und sie führt zu einer sehr
naheliegenden Annahme.

<!-- S21 -->
Wenn man den Prozessor jederzeit
von allem wegreißen kann,
dann wird doch auch mein Klick
sofort erledigt.

<!-- S22 -->
Nur darf der Handler
fast nichts tun.

<!-- S23 -->
Solange der Prozessor darin steckt,
wartet alles andere.
Auch der nächste Interrupt.
Und der ist schon unterwegs.

<!-- S24 -->
Die Regel ist also genau umgekehrt,
als man erwarten würde.
Der Handler tut so wenig,
wie es nur irgend geht.

<!-- S25 -->
Er notiert, was passiert ist.
Er bestätigt dem Gerät,
dass die Meldung ankam.
Er legt das Ereignis in die Warteschlange.
Und verschwindet.

<!-- S26 -->
Kernel-Entwickler teilen die Arbeit
sogar in zwei benannte Hälften:
was jetzt sofort geschehen muss,
und was warten kann.

<!-- S27 -->
Alles Interessante,
alles, was du je zu sehen bekommst,
steckt in der zweiten Hälfte.

<!-- S28 -->
Und da ist die erste Antwort.
Ein Interrupt bekommt
die Aufmerksamkeit des Rechners.

<!-- S29 -->
Er bringt dein Programm
nicht auf einen Prozessor.

<!-- S30 -->
Gut, sagst du. Dann reparier das.
Mach die Eingabe zum Wichtigsten
im ganzen Haus.

<!-- S31 -->
Maus? Höchste Priorität.
Tastatur? Höchste Priorität.
Das Fenster vor dir?
Höchste Priorität.

<!-- S32 -->
Alles andere kann warten.
Klingt vollkommen vernünftig.

<!-- S33 -->
Und der beste Einwand dagegen
hat sich auf dem Mars abgespielt.

<!-- S34 -->
1997 setzte der Lander Pathfinder auf
und nahm seine Arbeit auf.
Dann, ein paar Tage später,
startete er sich selbst neu.

<!-- S35 -->
Keine kosmische Strahlung.
Kein defektes Bauteil.
Ein Problem der Ablaufplanung.

<!-- S36 -->
Da war eine Aufgabe mit hoher
Priorität, die Daten durch die
ganze Sonde verteilte,
und sie brauchte gemeinsamen Speicher.

<!-- S37 -->
Eine Aufgabe mit niedriger Priorität,
die Wetterdaten sammelte,
war zuerst dort
und hielt ihn fest.

<!-- S38 -->
Was einen Moment lang
gar nicht schlimm gewesen wäre.
Doch dann nahm sich eine Aufgabe
mit mittlerer Priorität den Prozessor,

<!-- S39 -->
und die mit der niedrigen
kam nie zum Ende.
Also gab sie den Speicher nie frei.

<!-- S40 -->
Die wichtigste Aufgabe
der ganzen Sonde
hing jetzt hinter
der allerunwichtigsten fest.

<!-- S41 -->
Das hat einen Namen.
Prioritätsinversion.

<!-- S42 -->
Ein Watchdog-Timer bemerkte,
dass die wichtige Aufgabe
viel zu lange nicht gelaufen war,
nahm eine Katastrophe an

<!-- S43 -->
und startete die ganze Sonde neu.
Dann passierte es wieder.
Und wieder.

<!-- S44 -->
Ingenieure auf der Erde fanden es
heraus und schickten einen Fix zum Mars.

<!-- S45 -->
Und die Lehre daraus
kostet uns gar nichts.
Hohe Priorität heißt nicht,
dass dich jemand bedient.

<!-- S46 -->
Sie heißt nur: du wirst zuerst gefragt.
Wenn das, was du brauchst,
jemand Langsamerem gehört,
kauft dir deine Wichtigkeit nichts.

<!-- S47 -->
Und Priorität hat eine zweite Grenze.
Sie entscheidet über die Reihenfolge.
Sie schafft keinen einzigen
Takt zusätzlich.

<!-- S48 -->
Nehmen wir an, alle deine Kerne
laufen auf hundert Prozent.
Du denkst, der Rechner ist eingefroren.
Meistens heißt es das nicht.

<!-- S49 -->
Der Scheduler verteilt Zeitscheiben
so schnell,
dass du die Übergänge nicht spürst.

<!-- S50 -->
Darum kannst du etwas Riesiges
kompilieren
und dabei eine Webseite
scrollen.

<!-- S51 -->
Unter Last ändert sich
gar nicht so sehr das Tempo.
Der Rechner ist nicht langsam.

<!-- S52 -->
Er kommt zu spät.

<!-- S53 -->
Du klickst, und die Antwort kommt
eine halbe Sekunde später.
Dann eine Sekunde.
Dann fünf.

<!-- S54 -->
Und Menschen bemerken so etwas
unglaublich gut.
Eine halbe Sekunde wirkt wie
eine Maschine, die nachdenkt.

<!-- S55 -->
Fünf Sekunden wirken wie
eine Maschine, die gestorben ist.

<!-- S56 -->
Und es gibt eine Spielart davon,
die am meisten überrascht.
Manchmal liegt es überhaupt
nicht am Prozessor.

<!-- S57 -->
Öffne zu viel auf einmal,
und der physische Speicher ist voll.
Das Betriebssystem beginnt, Seiten
auf die Platte auszulagern.

<!-- S58 -->
Wenn davon genug zusammenkommt,
verbringt die Maschine ihre Zeit
damit, Speicher umzuschichten,
statt deine Arbeit zu tun.

<!-- S59 -->
Auch das hat einen Namen.
Thrashing.

<!-- S60 -->
Und das ist das Verwirrende,
denn der Prozessor
muss gar nicht ausgelastet wirken.

<!-- S61 -->
Er arbeitet nicht.
Er wartet.

<!-- S62 -->
Du kannst einer wartenden Aufgabe
die höchste Priorität im System geben,
und sie wird genauso lange
warten wie vorher.

<!-- S63 -->
Und dann gibt es noch
die menschlichste Spielart davon.
Das Ereignis kam an.
Der Kernel hat es.

<!-- S64 -->
Es liegt in einer Warteschlange
und trägt den Namen deines Programms.
Und dein Programm
holt es nicht ab.

<!-- S65 -->
Vielleicht rechnet es gerade lange
auf demselben Thread,
der auf sein eigenes Fenster
achten soll.

<!-- S66 -->
Die Maus funktioniert also.
Die Tastatur funktioniert.
Andere Programme funktionieren.

<!-- S67 -->
Und dieses eine Fenster wird blass
und meldet: keine Rückmeldung.

<!-- S68 -->
Das ist keine Diagnose.
Windows setzt das Schild ans Fenster
nach etwa fünf Sekunden,
in denen niemand Nachrichten abholt.

<!-- S69 -->
Das System ist völlig am Leben.
Nur die Anwendung
ist nicht an die Tür gekommen.

<!-- S70 -->
Dass der Rechner den Klick annimmt
und dass die Anwendung darauf antwortet,
sind nicht dieselben Ereignisse.

<!-- S70b -->
Übrigens, wenn du sehen willst,
wohin uns die nächste Frage führt,
überleg dir, ob du abonnieren möchtest.

Das hilft dem Kanal wirklich.
<!-- S71 -->
Es fehlt noch ein Glied der Kette,
und es ist genau das,
an das wir nie denken.
Nichts davon hat bisher etwas
auf deinen Bildschirm gebracht.

<!-- S72 -->
Die Anwendung ändert ihren Zustand.
Jemand muss das nächste Bild bauen.
Die Grafikkarte muss es zeichnen.
Der Bildschirm muss es zeigen.

<!-- S73 -->
Auf einem gewöhnlichen Bildschirm
erscheint ein neues Bild
etwa alle sechzehn Millisekunden.

<!-- S73b -->
Es ist also ein Unterschied,
ob der Rechner deinen Klick erledigt
und ob du das auch siehst.

<!-- S74 -->
Und ganz darunter
liegt der Teil,
den keine Technik repariert.
Das Betriebssystem weiß,
dass sich die Maus bewegt hat.
Warum, hat es keine Ahnung.

<!-- S75 -->
Vielleicht zielst du gerade
in einem Spiel.
Oder bearbeitest ein Dokument.
Oder bist an den Tisch gestoßen.

<!-- S76 -->
Für die Hardware
sind das dieselben Ereignisse.
Ein System kann Arten von Arbeit
einstufen. Raten kann es nicht.

<!-- S77 -->
Also schließt es einen Kompromiss.
Schnell genug für dich,
meistens,
ohne den Rest ewig warten zu lassen.

<!-- S78 -->
Was uns zurückbringt
zu diesem toten Bildschirm.
Dein Klick war nie nur ein Ereignis.

<!-- S79 -->
Die Hardware muss ihn melden.
Der Kernel muss ihn ablegen.
Die Schlange muss dein Programm erreichen.

<!-- S80 -->
Dein Programm muss laufen.
Die Oberfläche muss sich ändern.
Jemand muss das neue Bild zeichnen,
und der Bildschirm muss es dir zeigen.

<!-- S81 -->
Jeder einzelne dieser Schritte
ist klein und schnell.

<!-- S82 -->
Verzögere einen davon,
und du erlebst kein
langsames Fenster.

<!-- S83 -->
Du erlebst einen toten Rechner.

<!-- S84 -->
Und das Seltsamste an der Sache ist,
wie selten
das überhaupt passiert.

<!-- S85 -->
Wir erwarten von einer Maschine,
die Milliarden Operationen
pro Sekunde macht,
eine Antwort auf ein Zucken der Hand.

<!-- S86 -->
Und fast immer antwortet sie.

<!-- S87 -->
Wenn du also das nächste Mal klickst
und nichts passiert,
gib ihr einen Moment.

<!-- S88 -->
Sie hat dich gehört.

<!-- S89 -->
Sie hatte nur eine Warteschlange,
und du standest darin.
