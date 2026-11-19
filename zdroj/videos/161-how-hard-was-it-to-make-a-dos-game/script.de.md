<!-- S01 -->
1993 lief ein Spiel namens Doom
auf einem Computer
mit 4 Megabyte Arbeitsspeicher.

<!-- S02 -->
Das ist ungefähr die Größe
eines einzigen Fotos auf deinem Handy.

<!-- S03 -->
Einen 3D-Beschleuniger gab es nicht.
Der Hauptprozessor
übernahm das gesamte Rendering.

<!-- S04 -->
Heute beginnt ein Entwickler mit einer Engine,
etwa Unity oder Unreal,
die sich um Grafik, Sound,
Speicher und Hardware kümmert.

<!-- S05 -->
Unter DOS war all das
das Problem des Entwicklers.
Und ziemlich oft auch das des Spielers.

<!-- S06 -->
Wie schwer war es also,
ein Spiel für DOS zu machen?

<!-- S07 -->
Fangen wir mit dem Speicher an,
denn beim Speicher herrschte Chaos.

<!-- S08 -->
Der ursprüngliche IBM PC von 1981
konnte 1 Megabyte Speicher adressieren.

<!-- S09 -->
Aber nur die ersten
640 Kilobyte
waren für Programme gedacht.

<!-- S10 -->
Die übrigen 384 Kilobyte
waren für Videospeicher,
Erweiterungskarten und das BIOS reserviert.

<!-- S11 -->
Mehr als ein Jahrzehnt lang
startete DOS Programme normalerweise
innerhalb dieses Bereichs.
Alles darüber hinaus kostete Zusatzaufwand.

<!-- S12 -->
Daher stammt der berühmte Satz:
640 K sollten für jeden reichen.

<!-- S13 -->
Er wird meist Bill Gates zugeschrieben.
Es gibt keinen Beleg, dass er ihn je gesagt hat,
und er bestreitet es.

<!-- S14 -->
Anfang der Neunziger
hatte ein PC 4 Megabyte,
oder 8.

<!-- S15 -->
Und trotzdem konnte ein Spiel abbrechen
mit den Worten
„nicht genug Speicher“.

<!-- S16 -->
Speicher zu haben
und ihn nutzen zu können,
waren zwei verschiedene Dinge.

<!-- S17 -->
Ein Ausweg war Expanded Memory,
kurz EMS.

<!-- S18 -->
Ein 64-Kilobyte-Fenster
lag im oberen Teil
dieses ersten Megabytes.
Durch dieses Fenster sah ein Programm
4 Seiten zusätzlichen Speichers,
je 16 Kilobyte groß,

<!-- S19 -->
und konnte sie gegen andere tauschen,
als würdest du in einem Buch blättern,
durch ein Loch in einem Blatt Papier.

<!-- S20 -->
Ein anderer Weg war Extended Memory,
erreichbar über einen Treiber namens HIMEM.

<!-- S21 -->
Und genau hier
wurde das Problem des Entwicklers
zum Problem des Spielers.

<!-- S22 -->
Treiber für Maus, CD-Laufwerk
oder Soundkarte
knabberten am kostbaren Speicher,
außer du hast sie in den oberen Speicher geladen.

<!-- S23 -->
Also lernten Spieler, zwei Dateien zu bearbeiten:
CONFIG.SYS und AUTOEXEC.BAT.

<!-- S24 -->
Ein Spiel wollte EMS.
Ein anderes wollte es ausgeschaltet haben,
mit einer Einstellung namens NOEMS.
Und ein drittes brauchte jedes freie Kilobyte.

<!-- S25 -->
1993 brachte MS-DOS 6
ein Menü beim Start.

<!-- S26 -->
Du hast die Konfiguration gewählt
für das Spiel, das du spielen wolltest,
und der Computer startete für genau dieses Spiel.

<!-- S27 -->
Manche hatten am Ende
einen eigenen Eintrag
für fast jedes Spiel, das sie besaßen.

<!-- S28 -->
Doch zu dieser Zeit
hatten die größeren Spiele schon
einen Weg gefunden, die Grenzen von DOS zu umgehen.

<!-- S29 -->
Seit dem 386
konnte der Prozessor selbst
im 32-Bit-Protected-Mode laufen,
mit Platz für bis zu 4 Gigabyte.

<!-- S30 -->
Den Protected Mode haben wir
in einem früheren Video angeschaut.
DOS konnte ihn allerdings nicht nutzen.

<!-- S31 -->
Also brachten Spiele ihren eigenen Helfer mit,
einen DOS-Extender.
Der bekannteste war DOS/4GW.

<!-- S32 -->
Er lag einem beliebten Compiler bei,
Watcom C.

<!-- S33 -->
Wenn ein Spiel startete,
schaltete DOS/4GW den Prozessor
in den Protected Mode
und gab dem Spiel so Zugriff
auf Speicher jenseits der DOS-Grenze.

<!-- S34 -->
DOS war darunter immer noch da
und bot Dienste wie den Dateizugriff.
Aber das Spiel lief jetzt im Protected Mode,
nicht als klassisches DOS-Programm.

<!-- S35 -->
Wenn du in den Neunzigern DOS-Spiele gespielt hast,
hast du seinen Namen
über den Bildschirm huschen sehen.

<!-- S37 -->
Jetzt zum Bild.
In einem der meistgenutzten VGA-Modi,
dem Mode 13h,
hatte der Bildschirm 320
mal 200 Pixel,
in 256 Farben.

<!-- S38 -->
Jedes Pixel war ein Byte.
Um ein Pixel einzufärben,
hast du eine Zahl in den Speicher geschrieben.
Keine Grafikbibliothek. Nur Speicher.

<!-- S39 -->
Der ganze Bildschirm belegte
64.000 Byte.

<!-- S40 -->
Das ist knapp unter 64 Kilobyte,
klein genug für ein einziges Segment,
den Block, den ein 16-Bit-Programm
auf einmal adressieren konnte.
Ausnahmsweise spielte der Speicher mit.

<!-- S41 -->
Aber wenn du direkt
auf den sichtbaren Bildschirm zeichnest,
sieht der Spieler halbfertige Bilder,
und das Bild flackert.

<!-- S42 -->
Also zeichneten Spiele jedes Bild
zuerst in einen versteckten Puffer
und kopierten das fertige Bild dann
in den Videospeicher.

<!-- S43 -->
1991 veröffentlichte Michael Abrash,
Programmierer und Autor,
einen besseren Weg.
Er nannte ihn Mode X.

<!-- S44 -->
Er nutzte einen Teil der VGA,
den die meisten Programmierer
nie angefasst hatten.

<!-- S45 -->
Er bot quadratische Pixel
und Platz für mehrere Bildschirme
im Videospeicher.

<!-- S46 -->
Das Spiel zeichnete auf einen Bildschirm,
den niemand sehen konnte,
und schaltete dann einfach auf ihn um.
Aber das zu programmieren war viel schwieriger.

<!-- S47 -->
Dann gab es noch den Sound.
Und Sound war eine Lotterie.

<!-- S48 -->
Der eingebaute Lautsprecher des PCs
war zum Piepen gebaut.

<!-- S49 -->
Dann kamen Soundkarten
und andere Sound-Hardware.
Keine zwei davon
funktionierten gleich.

<!-- S50 -->
AdLib, mit einem Yamaha-Chip,
der Musik synthetisierte.
Sound Blaster, der auch
aufgenommenen Klang abspielen konnte.

<!-- S51 -->
Die Roland MT-32,
eine teure Box mit besser klingenden Instrumenten.
Die Gravis UltraSound.

<!-- S52 -->
Alle zu unterstützen
hieß, verschiedene Treiber zu schreiben.

<!-- S53 -->
Und das Spiel musste wissen,
wo die Karte war.
Ihren Port, ihren Interrupt
und ihren DMA-Kanal.

<!-- S54 -->
Die übliche Antwort bei einem Sound Blaster
war Port 220, IRQ 7, DMA 1.
Meistens.

<!-- S55 -->
Lag eins davon falsch,
blieb das Spiel stumm.
Oder es fror ein.

<!-- S56 -->
1991 veröffentlichte ein Programmierer namens John Miles
eine Bibliothek,
die mit vielen Soundkarten
über eine einzige Schnittstelle sprach.

<!-- S57 -->
Ein Spiel konnte seinen Soundcode einmal schreiben
und den Rest der Bibliothek überlassen.

<!-- S58 -->
Das war eine weitere Schicht
zwischen Spiel und Hardware.
Merk dir das.

<!-- S59 -->
Und dann war da die Geschwindigkeit.
Programmierer zählten
jeden Schritt des Prozessors.

<!-- S63 -->
Um ein Pixel auf dem Bildschirm zu finden,
multiplizierst du seine Zeile
mit 320.

<!-- S63b -->
Auf älteren Prozessoren
konnte Multiplizieren teuer sein.

<!-- S64 -->
Aber 320
ist 256
plus 64.
Beides sind Zweierpotenzen.

<!-- S65 -->
Also kannst du die Multiplikation ersetzen
durch zwei Bitverschiebungen und eine Addition.

<!-- S67 -->
Chris Sawyer ging bis direkt an die Hardware.
Er schrieb Transport Tycoon 1994
fast vollständig in Assembler,

<!-- S68 -->
also in den Befehlen,
die der Prozessor selbst versteht,
einen nach dem anderen.

<!-- S69 -->
Und manchmal
reichte selbst das alles nicht.

<!-- S70 -->
1990 hatte Wing Commander einen Fehler,
den das Team nicht finden konnte,
und die Deadline war nah.

<!-- S71 -->
Wenn du das Spiel verlassen hast,
stürzte der Speichermanager ab,
mit einer Fehlermeldung.

<!-- S72 -->
Also öffnete ein Programmierer, Ken Demarest,
den Speichermanager
in einem Hex-Editor
und änderte den Text dieser Meldung.

<!-- S73 -->
Jetzt stand da:
„Danke, dass du Wing Commander gespielt hast.“

<!-- S74 -->
Dann fand das Team den eigentlichen Fehler,
und der Witz wurde nie ausgeliefert.

<!-- S74b -->
Manche Spieler sind bis heute sicher, ihn gesehen zu haben.
Und spätere Origin-Spiele
verabschiedeten sich tatsächlich so.

<!-- S75 -->
Womit wir wieder bei Doom wären.

<!-- S76 -->
Doom nutzte DOS/4GW
und lief als 32-Bit-Programm.

<!-- S77 -->
Hardware für Gleitkommazahlen
war nicht in jedem PC garantiert.

<!-- S78 -->
Also nutzte Doom Festkommaarithmetik.
Ganze Zahlen,
bei denen die unteren 16 Bit
für den Nachkommaanteil standen.

<!-- S79 -->
Und seine Welt war nicht
wirklich dreidimensional.

<!-- S80 -->
Jedes Level ist ein flacher Grundriss,
mit einer Höhe für jeden Boden
und jede Decke.

<!-- S81 -->
Ein Raum kann nie über einem anderen liegen.
Und richtig nach oben oder unten schauen kannst du nicht.

<!-- S82 -->
Bevor ein Level spielbar war,
zerlegte ein Werkzeug die Karte
in einen Binärbaum, einen BSP.

<!-- S83 -->
Die Engine durchläuft diesen Baum
von vorne nach hinten,
beginnend auf der Seite des Spielers,
und überspringt Bereiche, die nicht sichtbar sind.

<!-- S84 -->
Und Doom wurde nicht einmal unter DOS geschrieben.

<!-- S85 -->
id Software entwickelte es
auf NeXT-Workstations
und kompilierte das Ergebnis für DOS.

<!-- S86 -->
Doom war keine allgemeine 3D-Engine.
Es war für genau
eine Art von Welt gebaut.
Diese Spezialisierung
half ihm, auf einem 386 zu laufen.

<!-- S87 -->
Und andere Studios wollten diese Welt.

<!-- S88 -->
Raven Software lizenzierte die Doom-Engine
für Heretic, 1994,
und Hexen, 1995.

<!-- S89 -->
Doom half, eine neue Art
der Spieleentwicklung zu etablieren.
Studios konnten eine bestehende Engine lizenzieren,
statt alles von Grund auf zu bauen.

<!-- S90 -->
Ein DOS-Extender.
Eine Soundbibliothek.
Eine lizenzierte Engine.

<!-- S91 -->
Jede davon nahm dem Entwickler
ein Problem ab.
Und die Schichten wuchsen weiter,
bis hin zu den Engines,
mit denen Entwickler heute anfangen.

<!-- S92 -->
War Spieleentwicklung damals also schwerer?
In vieler Hinsicht ja.

<!-- S93 -->
Aber die Schwierigkeit verschwand nicht.
Sie wanderte.

<!-- S94 -->
Heute kämpfen Entwickler
mit Gigabytes an Assets
und Millionen Polygonen
statt mit ein paar hundert Kilobyte.

<!-- S95 -->
Unter DOS musste sogar der Spieler
wissen, wohin sein Speicher verschwand.

<!-- S96 -->
Hier also eine Frage an dich.
Erinnerst du dich, wie du
ein Bootmenü eingerichtet hast, nur damit ein Spiel lief?
Und war das eine Qual
oder der halbe Spaß?
Schreib es mir in die Kommentare.
