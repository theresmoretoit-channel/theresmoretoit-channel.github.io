<!-- S01 -->
Du drückst am Kassettenrekorder auf Play.
Und das hier kommt aus dem Lautsprecher.

<!-- S02 -->
Das ist keine Musik.
Und auch nicht der Soundtrack eines Spiels.

<!-- S03 -->
Es ist das Spiel.
Jedes Fiepen ist Teil eines Programms,
und der Computer hört ihm zu.

<!-- S04 -->
Der Kassettenrekorder hat keine Ahnung.
Soweit er weiß, spielt er ein Lied.

<!-- S05 -->
Wie wird also aus einem Lied ein Spiel?
Und warum konnte ein einziger falscher Ton
fünf Minuten Warten zunichtemachen?

<!-- S06 -->
So funktioniert der Trick,
auf einem ganz bestimmten Gerät:
dem ZX Spectrum,
einem britischen Heimcomputer von 1982.

<!-- S07 -->
Er nutzt zwei Arten von Impulsen.
Ein kurzes Impulspaar bedeutet Null.

<!-- S08 -->
Eine Eins ist dasselbe Paar,
nur ist jeder Impuls doppelt so lang,
deshalb klingt ihr Ton eine Oktave tiefer.

<!-- S09 -->
Schick etwa vierzehnhundert Bit
pro Sekunde,
und du bekommst das Geräusch, das du eben gehört hast.

<!-- S09b -->
Das heißt auch: Ein Programm voller Nullen
lädt schneller als eins voller Einsen.
Jede Eins braucht doppelt so lange.

<!-- S10 -->
Wenn du in Amerika aufgewachsen bist,
hast du es vielleicht nie gehört.

<!-- S11 -->
Was seltsam ist,
denn die Idee selbst kam aus Amerika.

<!-- S12 -->
1975, bei einem Treffen in Kansas City,
einigten sich Computerbastler darauf,
wie man Daten als Klang
auf gewöhnlichen Audiokassetten speichert.

<!-- S12b -->
Eine Eins waren acht schnelle Schwingungen
eines hohen Tons,
eine Null vier langsamere eines tiefen.
Dreihundert Bit pro Sekunde.

<!-- S13 -->
Frühe Geräte wie der Apple II
und der TRS-80
speicherten ihre Programme
auf ganz normalen Kassettenrekordern.

<!-- S14 -->
Aber in Amerika stieg man bei Heimcomputern
schnell auf andere Speichermedien um.

<!-- S15 -->
1983 berichtete eine Zeitschrift von einer Umfrage:
Neun von zehn neuen Besitzern eines Commodore 64
kauften ein Diskettenlaufwerk
gleich zusammen mit dem Computer.

<!-- S16 -->
In Großbritannien lief die Geschichte andersherum.

<!-- S17 -->
Das Spectrum kostete
hundertfünfundzwanzig Pfund,
und es kam ganz ohne Speichergerät.
Du hast einfach den Kassettenrekorder genommen,
den du schon hattest.

<!-- S18 -->
Für Millionen Kinder in ganz Europa
war dieses Geräusch also der Klang
eines Spiels, das gleich losgeht.

<!-- S18b -->
Nach genug Ladevorgängen
konntest du sogar erkennen, welches Spiel es war,
allein am Kreischen.

<!-- S19 -->
Verfolgen wir also ein Spiel
vom Band bis in den Computer.

<!-- S20 -->
Du tippst LOAD, drückst Enter
und drückst Play.

<!-- S21 -->
Zuerst kommt ein gleichmäßiges Summen,
achthundert Schwingungen pro Sekunde,
etwa fünf Sekunden lang.

<!-- S22 -->
Es enthält überhaupt keine Daten.
Es ist dafür da, dass der Computer
das Signal findet
und sich auf seinen Rhythmus einstellt.

<!-- S23 -->
Dann zwei schnelle Impulse, die Synchronisation.
Sie bedeuten: Ab hier kommen Daten.

<!-- S24 -->
Als Erstes kommt
ein kurzer Header.
Neunzehn Bytes:
ein Name mit bis zu zehn Buchstaben,
welche Art von Datei es ist
und wie lang sie sein wird.

<!-- S25 -->
Dann ein zweites, kürzeres Summen,
diesmal zwei Sekunden,
und dann das Spiel selbst.

<!-- S26 -->
Jedes Byte besteht aus acht solchen Tönen,
einer nach dem anderen,
ganz ohne Lücken zwischen den Bytes.

<!-- S27 -->
Und der Computer hört keine Töne.
Er misst die Zeit zwischen einer Flanke
des Signals und der nächsten.

<!-- S28 -->
Ein kurzes Paar ist eine Null.
Ein langes Paar ist eine Eins.

<!-- S28a -->
Das ist schon der ganze Decoder.

<!-- S28b -->
Und das Geräusch am Anfang dieses Videos
ist kein Soundeffekt.
Wir haben es genau nach diesen Regeln erzeugt,
und darin steckt ein echtes Spectrum-Programm.

<!-- S28c -->
Wir spielen es ganz am Ende komplett ab.
Nimm es auf, und ein Spectrum lädt es.

<!-- S29 -->
Die meisten Spiele zeigten zuerst ein Bild,
und das lud in einer seltsamen Reihenfolge.

<!-- S30 -->
Dünne Streifen erschienen, acht Zeilen auseinander,
füllten sich dann Zeile für Zeile,
jeweils ein Drittel des Bildschirms.
Und die Farben kamen zuletzt
und zogen von oben über alles.

<!-- S31 -->
Allein das Laden dieses Bildes
dauerte etwa vierzig Sekunden.
Das ganze Spiel rund fünf Minuten.

<!-- S32 -->
Und am Ende jedes Blocks
kommt noch ein Byte.

<!-- S33 -->
Beim Speichern verknüpft das Spectrum
jedes Byte des Blocks
mit einer einfachen Regel namens XOR
und schreibt das Ergebnis als weiteres Byte auf.

<!-- S34 -->
Beim Laden wiederholt es die Rechnung.
Stimmen die Ergebnisse überein,
ist der Block unversehrt angekommen.

<!-- S35 -->
Wenn nicht, sagt das Spectrum das hier.

<!-- S36 -->
Fünf Minuten Warten,
und ein einziges Byte entscheidet,
dass alles umsonst war.
Zurückspulen und von vorn.

<!-- S37 -->
Seltsamerweise gibt es bei einem kaputten Header
überhaupt keine Fehlermeldung.
Das Spectrum ignoriert ihn einfach
und horcht weiter auf den nächsten.

<!-- S38 -->
Andere Computer setzten auf andere Karten.

<!-- S39 -->
Der Commodore 64 nahm
jeden Block zweimal auf,
damit eine beschädigte Stelle in der einen Kopie
aus der anderen gerettet werden konnte.

<!-- S40 -->
Sicherer, aber langsam.
Mit Commodores eingebauter Routine
brauchte ein Programm mit vierzig Kilobyte
etwa zwölfeinhalb Minuten.

<!-- S41 -->
Also schrieben die Spielefirmen
ihre eigenen, schnelleren Lader,
manche bis zu etwa zehnmal schneller.

<!-- S42 -->
Und dann war da noch der Kassettenrekorder.

<!-- S43 -->
Zu leise,
und die Flanken gehen im Rauschen unter.
Zu laut,
und sie verschmieren ineinander.

<!-- S44 -->
Ein Band, das etwas zu schnell oder zu langsam läuft,
dehnt jeden Impuls,
und der Computer misst ja die Zeit.

<!-- S45 -->
Am schlimmsten war der Azimut,
der Winkel des Tonkopfs.
Ein Band, das auf einem Gerät aufgenommen wurde,
passte womöglich nicht zu einem anderen.

<!-- S46 -->
Also steckten die Leute einen winzigen Schraubenzieher
in ein Loch neben dem Tonkopf,
drehten ihn immer nur ein kleines Stück
und horchten.

<!-- S47 -->
Es sah aus wie Aberglaube.
Es war Feinabstimmung des Signals.

<!-- S48 -->
Aber achte darauf, was der Kassettenrekorder
nie tun musste.

<!-- S49 -->
Er hat nie ein einziges Bit verstanden.
Er hat Klang aufgenommen
und wieder abgespielt.

<!-- S50 -->
Das heißt, ein Programm
brauchte eigentlich gar keine Kassette.
Alles, was Klang übertragen konnte,
konnte auch Software übertragen.

<!-- S50b -->
Es hieß auch, dass ein Spiel zu kopieren
so einfach war, wie ein Album zu kopieren.
Zwei Kassettendecks und ein Kabel.

<!-- S51 -->
Atari nutzte beide Stereospuren.
Auf der einen das Programm,
auf der anderen eine Stimme,
die über den Fernseher mit dir sprach,
während das Spiel lud.

<!-- S52 -->
In Jugoslawien strahlte eine Sendung von Radio Belgrad
Programme über den Äther aus.

<!-- S53 -->
Die Hörer nahmen sie auf Band auf,
etwa hundertfünfzig Programme
zwischen 1983 und 1986.

<!-- S54 -->
In der Tschechoslowakei war es das Fernsehen.
Ein Programm lief als Ton
unter dem Abspann.

<!-- S55 -->
Und 1983 versteckte der Sänger Pete Shelley
ein Spectrum-Programm
am Ende eines Vinylalbums.

<!-- S56 -->
Kopier es auf Band, lad es,
und die Songtexte erscheinen auf dem Bildschirm,
synchron zu den Liedern.

<!-- S57 -->
Aber es gab einen Haken.

<!-- S58 -->
Das Radio konnte den Klang
zu jedem Computer im Land bringen.
Verstehen konnte ihn nur der richtige.

<!-- S59 -->
Spiel einem Commodore ein Spectrum-Spiel vor,
und der Commodore hört Rauschen.
Die Bits bedeuten nur etwas
für ein Gerät, das das Format kennt.

<!-- S60 -->
Also versuchte der niederländische Rundfunk, das zu lösen.
1982 schuf er BASICODE:
ein einziges Klangformat,
mit einem kleinen Übersetzerprogramm
für jede Art von Computer.

<!-- S61 -->
Und dieses Problem ist nie verschwunden.
Eine Datei nützt nur etwas,
wenn sie noch von irgendetwas gelesen werden kann.

<!-- S62 -->
Kassetten haben natürlich verloren.
Disketten waren schneller,
dann Festplatten, dann Flash-Speicher.

<!-- S63 -->
Nur ist das Band eigentlich nie verschwunden.
Rechenzentren lagern
ihre Archive bis heute auf Magnetband.

<!-- S64 -->
Eine moderne LTO-9-Kassette
fasst achtzehn Terabyte.

<!-- S65 -->
Umgerechnet auf Spectrum-Tempo
würde diese Kapazität rund
neunundzwanzig Millionen Kassetten füllen
und mehr als dreitausend
Jahre zum Laden brauchen.

<!-- S66 -->
Und doch ist es dieselbe Idee.
Muster auf einem laufenden Bandstreifen,
die wieder zu Zahlen werden,
wenn du sie brauchst.

<!-- S67 -->
Wenn du also das nächste Mal dieses Kreischen hörst,
denk daran, was es ist.
Kein Rauschen.
Ein Programm, unterwegs als Klang.

<!-- S68 -->
Und irgendwo im Jahr 1985
sitzt ein Kind vor dem Fernseher
und wartet, dass es aufhört.
Denn wenn es aufhört,
beginnt das Spiel.

<!-- S69 -->
Also, hier ist eine Frage an dich.
Wenn du je ein Spiel von Kassette geladen hast,
woran erinnerst du dich dabei am meisten?
Schreib es in die Kommentare.

<!-- S70 -->
Und wie versprochen, hier ist das Programm.
Genau wie das tschechoslowakische Fernsehen
haben wir es unter den Abspann gelegt.
