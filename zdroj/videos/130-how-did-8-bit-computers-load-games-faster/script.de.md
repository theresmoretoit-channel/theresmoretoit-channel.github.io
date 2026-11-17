<!-- S01 -->
Das ist ein ZX Spectrum, das ein Programm lädt.

<!-- S02 -->
Und das ist das gleiche Programm,
auf dem gleichen Computer,
von der gleichen Art Kassette.

<!-- S03 -->
Es ist in der halben Zeit fertig.
An der Hardware hat sich nichts geändert.
Kein schnelleres Band, kein schnellerer Rekorder.

<!-- S04 -->
Geändert hat sich nur eines:
die Art, wie der Computer zuhörte.

<!-- S05 -->
Wie haben 8-Bit-Computer also gelernt,
Spiele schneller zu laden?
Und wenn es so einfach war,
warum haben sie es nicht von Anfang an gemacht?

<!-- S06 -->
In einem früheren Video
haben wir gesehen, wie das Spectrum Bits
als Impulse auf dem Band speichert.

<!-- S07 -->
Ein kurzes Impulspaar bedeutet Null.
Ein doppelt so langes Paar bedeutet Eins.

<!-- S08 -->
Das ergibt etwa vierzehnhundert Bits
pro Sekunde.
Ein Spiel, das die 48K Speicher füllt,
braucht rund fünf Minuten.

<!-- S09 -->
Jetzt mach jeden Impuls halb so lang.

<!-- S10 -->
Der Computer unterscheidet immer noch kurz von lang.
Aber doppelt so viele Bits
laufen jede Sekunde am Tonkopf vorbei.

<!-- S11 -->
Das ist der ganze Trick hinter einem Turbo-Loader.
Und das ist nicht nur ein Gedankenexperiment.

<!-- S12 -->
1984 lud das Spiel Skool Daze
seine Daten doppelt so schnell
wie das Spectrum normalerweise.

<!-- S13 -->
Warum hat das Spectrum dann
nicht von selbst so schnell geladen?

<!-- S14 -->
Der eingebaute Lader steckt im ROM,
dem Speicherchip, mit dem der Computer startet.
Er misst einen Impuls nicht in Sekunden.

<!-- S15 -->
Er zählt.
Nach jeder Flanke des Signals
wartet er einen Moment
und zählt dann, wie lange es bis zur nächsten dauert.

<!-- S16 -->
Eine einzige Zahl im ROM
entscheidet, wo die Null aufhört
und die Eins anfängt.

<!-- S17 -->
Und diese Zahl lässt viel Spielraum.
Eine Null darf sich
um mehr als vierzig Prozent dehnen
und wird trotzdem als Null gelesen.

<!-- S18 -->
Dank dieses Spielraums lädt ein abgenutztes Band
auf einem billigen Rekorder
trotzdem noch.

<!-- S19 -->
Und der Computer war nicht die Grenze.
Das Spectrum prüft das Bandsignal
etwa sechzigtausendmal pro Sekunde.

<!-- S20 -->
Die Kassette war die Grenze.
Kürzere Impulse heißen höhere Töne.
Bei doppelter Geschwindigkeit wandert eine Null
von zwei Kilohertz auf vier.

<!-- S21 -->
Und hohe Töne sind genau das, was
ein billiger Rekorder
oder ein leicht verstellter Tonkopf
als Erstes verliert.

<!-- S22 -->
Eine Spectrum-Zeitschrift schätzte 1986,
die meisten Leute schafften
mindestens die doppelte Normalgeschwindigkeit.
Wie viel mehr ging,
hing vom Rekorder ab.

<!-- S23 -->
Aber Turbo hatte ein seltsameres Problem.

<!-- S24 -->
Wenn der Computer nur
das langsame Format kennt,
wie lädt er dann das Programm,
das ihm das schnelle beibringt?

<!-- S25 -->
Die Antwort steckt am Anfang des Bandes.
Der erste Teil ist
im ganz normalen, langsamen Format aufgenommen.

<!-- S26 -->
Er ist kurz,
und das ROM lädt ihn wie jedes andere Programm.

<!-- S27 -->
Dann übernimmt dieses kleine Programm.
Im einfachsten Fall
ist es eine Kopie der Laderoutine aus dem ROM selbst,
mit ein paar geänderten Zahlen.

<!-- S28 -->
Bei Skool Daze
sitzen die Änderungen an drei Stellen.
Eine kürzere Wartezeit, ein neuer Startwert fürs Zählen,
eine neue Trennlinie.

<!-- S29 -->
Das ROM lädt also das Programm,
das die Arbeit des ROMs macht, nur schneller.

<!-- S30 -->
Das ist ein bisschen, als würdest du
einen schnelleren Downloader herunterladen.
Der langsame Schritt bringt dir das Werkzeug.
Das Werkzeug macht den Rest.

<!-- S31 -->
Kommerzielle Spiele nutzten dieselbe Idee.
Ein bekanntes Beispiel war Speedlock,
das Ocean 1984 zum ersten Mal einsetzte.

<!-- S32 -->
Einer seiner Autoren sagte, er habe es geschrieben,
weil er es satthatte,
wie lange der Standardlader brauchte.

<!-- S33 -->
Aber jetzt kommt die Überraschung.
Speedlock war nur etwa anderthalbmal
so schnell.

<!-- S34 -->
Der erste Tag
von Daley Thompson's Decathlon
brauchte drei Minuten zwanzig Sekunden,
während dieselben Daten in normaler Geschwindigkeit
vier Minuten siebenundvierzig gebraucht hätten.

<!-- S35 -->
Spätere Versionen waren nur etwa
ein Fünftel schneller als das ROM.
Denn Tempo war nicht die einzige Aufgabe.

<!-- S36 -->
Ab 1983 konnten Kopierprogramme
den Header eines Spiels lesen
und das ganze Spiel auf ein anderes Band kopieren.

<!-- S37 -->
Ein eigenes Format
gab diesen Programmen nichts zu lesen.

<!-- S38 -->
Das frühe Speedlock zerhackte sogar seinen Pilotton
in kurze Stöße,
damit der Lader im ROM
ihn überhaupt nicht erkannte.

<!-- S39 -->
Und man konnte es hören.
Beim Laden mit Speedlock klickte es,
und am Bildschirmrand ruckelten Streifen.

<!-- S40 -->
Es hielt niemanden davon ab,
ein Band von einem Deck aufs andere zu kopieren.
Aber es gab den Verlagen
einen Grund, eigene Lader zu schreiben.

<!-- S41 -->
Beim Commodore 64
war der Grund zum Umstieg viel größer.

<!-- S42 -->
Seine eingebaute Routine
nahm alles zweimal auf,
als Sicherheitskopie.
Ein Spiel mit vierzig Kilobyte brauchte
etwa zwölfeinhalb Minuten.

<!-- S43 -->
Und hier machte der Rekorder
fast nichts Schlaues.
Er verwandelte den Ton nur
in saubere An-Aus-Impulse.

<!-- S44 -->
Der Computer maß die Dauer jedes Impulses selbst,
per Software.

<!-- S45 -->
Ein schnellerer Lader
war also einfach ein anderes Programm.

<!-- S46 -->
1985 testete die Zeitschrift Compute!
einen namens TurboTape.

<!-- S47 -->
Sobald er das Programm auf dem Band gefunden hatte,
lud er zwölf Kilobyte
in achtundzwanzig Sekunden.

<!-- S48 -->
Commodores eigenes Diskettenlaufwerk
brauchte vierunddreißig Sekunden.

<!-- S49 -->
Eine Kassette,
die eine Diskette schlägt.

<!-- S50 -->
Und weil der Computer
ganz allein zuhörte,
konnte er nebenbei andere Dinge tun.

<!-- S51 -->
Lader wie Freeload
gaben dem Lesen des Bandes Vorrang.
Die übrige Prozessorzeit
ging an Musik, weiches Scrolling,
sogar kleine Spiele.

<!-- S52 -->
Bei Mastertronics Invade-a-Load
hast du einen Space-Invaders-Klon gespielt,
während das eigentliche Spiel lud.

<!-- S53 -->
Die 8-Bit-Computer von Atari
waren eine andere Geschichte.

<!-- S54 -->
Hier hörte der Rekorder zu.
Darin steckten zwei Filter,
einer für jeden Ton,
und eine Schaltung, die dem Computer
fertige Einsen und Nullen lieferte.

<!-- S55 -->
Standard waren sechshundert Bits pro Sekunde,
und die Filter begrenzten,
wie viel schneller es gehen konnte.

<!-- S56 -->
Clevere Software konnte das etwas
hochschrauben, bestenfalls auf etwa zwölfhundert.
Aber um viel schneller zu werden,
musste man den Rekorder aufschrauben.

<!-- S57 -->
Und in der Tschechoslowakei taten die Leute das.

<!-- S58 -->
Ein Diskettenlaufwerk kostete dort
zwei- bis dreimal
so viel wie der Computer selbst.
Also blieben die meisten Atari-Besitzer dort bei Kassetten.

<!-- S59 -->
1987 entwarf ein Prager Student
aus dem örtlichen Atari-Club
Turbo 2000.

<!-- S60 -->
Es gab dem Signal einen neuen Weg.
Ein Draht im Rekorder nahm den Ton
direkt vom Verstärker ab,
noch vor den Filtern,
führte ihn durch einen kleinen Chip
und auf die Leitung zum Computer.

<!-- S61 -->
Ein Schalter, den der Computer umlegte,
wählte zwischen dem alten und dem neuen Weg.

<!-- S62 -->
Jetzt maß der Computer die Dauer der Impulse selbst.
Rund zweitausenddreihundert Bits
pro Sekunde.
Fast viermal so schnell.

<!-- S63 -->
Turbo war nicht ein einziges universelles Format.

<!-- S64 -->
Manchmal hat man das Programm gewechselt.
Manchmal musste man die Maschine umbauen.

<!-- S65 -->
Und schneller gab es nicht umsonst.

<!-- S66 -->
Compute! warnte, dass eine TurboTape-Aufnahme
manchmal nicht laden wollte,
auf einem anderen Rekorder,
dessen Tonkopf etwas anders justiert war.

<!-- S67 -->
Das Speichern im Standardformat, hieß es,
sei viel langsamer,
aber äußerst zuverlässig.

<!-- S68 -->
Dass alles zweimal aufgenommen wurde,
war keine Faulheit von Commodore.
Es war der Preis für zuverlässiges Laden.

<!-- S69 -->
Aber ein anderer Lader
konnte auch etwas Unerwartetes.
Er konnte ein Band lesen,
das der eingebaute nicht laden wollte.

<!-- S70 -->
Auf dem Sharp MZ-800,
einem Computer, der seinen Weg
Ende der 1980er in die Tschechoslowakei fand,
kannten die Besitzer ein Programm namens Turbo Copy.

<!-- S71 -->
Ein Spiel ließ sich nicht laden,
es meldete einen Prüfsummenfehler.
Die Besitzer merkten, dass Turbo Copy
es oft trotzdem laden konnte.

<!-- S72 -->
Dann hat man es mit normaler Geschwindigkeit
auf eine neue Kassette gespeichert,
und der Computer
hat es wieder ganz normal geladen.
Es fühlte sich an, als hätte man ein kaputtes Spiel repariert.

<!-- S73 -->
Wie konnte also ein Lader lesen,
was der andere nicht schaffte?

<!-- S74 -->
Das ROM des Sharp nahm jeden Block zweimal auf,
mit etwa zwölfhundert Bits pro Sekunde.

<!-- S75 -->
Und es hat nie einen Impuls gemessen.
Nachdem ein Impuls begonnen hatte,
wartete es eine festgelegte Zeit
und schaute ein einziges Mal hin.

<!-- S76 -->
Noch hoch?

<!-- S76b -->
Das ist eine Eins.

<!-- S76c -->
Schon niedrig?

<!-- S76d -->
Das ist eine Null.

<!-- S77 -->
Eine Stoppuhr, im Voraus eingestellt.

<!-- S78 -->
Auf einem alten Band oder einem anderen Rekorder
kamen die Impulse etwas runder zurück.
Dann konnte dieser eine Blick
den falschen Pegel erwischen.

<!-- S79 -->
Ein falsches Bit verdirbt die Prüfsumme.
Wenn beide Kopien scheitern,
scheitert das Laden.

<!-- S80 -->
Turbo Copy hörte anders zu.
Es maß die Dauer jedes Impulses
mit dem Timerchip des Computers.

<!-- S81 -->
Und vor jedem Block
hörte es sich den Pilotton an
und legte seine Trennlinie
nach den Impulsen fest, die es tatsächlich hörte.

<!-- S82 -->
Seine Stoppuhr war
auf genau das Band eingestellt, das gerade lief.

<!-- S83 -->
Und die Reparatur war keine Kopie des Tons.
Turbo Copy behielt die Bytes
und schrieb ein brandneues,
sauber getaktetes Signal.

<!-- S84 -->
Die Daten waren nicht verloren.
Die übliche Art, sie zu lesen,
war einfach nicht gut genug.

<!-- S84b -->
Turbo Copy konnte das Spiel auch mit Turbo speichern,
mit zwei- bis dreifacher Normalgeschwindigkeit,
mit einem eigenen kleinen Lader davor.

<!-- S85 -->
Und genau das haben all diese Tricks
gemeinsam.

<!-- S86 -->
Die Kassette blieb dieselbe.
Geändert hat sich, wie sie gelesen wurde.

<!-- S87 -->
Heute erwarten wir, dass Spiele sofort laden.
In den 1980ern war das Laden Teil des Spiels.
Du hast dem Band zugehört.
Du hast die Streifen beobachtet.
Du hast gewartet.

<!-- S88 -->
Und manchmal brachte ein anderer Lader
dieselbe Kassette dazu, sich zu verhalten,
als steckte sie in einer völlig anderen Maschine.

<!-- S89 -->
Der Computer brauchte kein schnelleres Band.
Er brauchte eine bessere Art zuzuhören.

<!-- S90 -->
Hier also eine Frage an dich.
Hast du damals Turbo-Loader benutzt?
Wie hast du sie in Erinnerung?
Sind sie öfter gescheitert?
Schreib es in die Kommentare.

<!-- S91 -->
Und zum Schluss das ganze Turbo-Band,
von Anfang bis Ende.
Zuerst der Teil in normaler Geschwindigkeit,
dann der Turbo-Teil.
Bei einem so kleinen Programm
lohnt sich Turbo nicht.
Der Lader braucht länger,
als er an Zeit spart.
Bei einem ganzen Spiel konnte es Minuten sparen.
