<!-- S01 -->
Das ist ein QR-Code.
Er enthält eine kurze Textzeile.

<!-- S02 -->
Das Handy liest ihn sofort.

<!-- S03 -->
Jetzt reißen wir ein Stück heraus.

<!-- S04 -->
Und scannen ihn noch einmal.
Derselbe Text.
Jeder Buchstabe.

<!-- S05 -->
Ein Teil des Codes ist weg.
Nicht schwer lesbar.
Weg.

<!-- S06 -->
Wie kann ein Handy also etwas lesen,
das gar nicht mehr da ist?

<!-- S07 -->
Hier ist dasselbe Problem, nur kleiner.
Jemand schickt Ihnen acht Bits.
Unterwegs gehen drei davon verloren.

<!-- S08 -->
Jedes fehlende Bit ist eine Null oder Eins,
es gibt also acht Möglichkeiten, die Lücken zu füllen.
Und nichts von dem, was angekommen ist,
verrät Ihnen, welche die richtige ist.

<!-- S09 -->
Und doch hat das Handy genau das geschafft.
Es hat nicht geraten.
Die Antwort wurde gesendet,
bevor überhaupt etwas verloren ging.

<!-- S10 -->
Der Trick: Man sendet mehr
als nur die Nachricht selbst.

<!-- S11 -->
Am einfachsten ist es,
alles dreimal zu sagen.
Eine Null wird als drei Nullen gesendet,
eine Eins als drei Einsen.

<!-- S12 -->
Rauschen kippt eine davon,
und Sie empfangen eins, null, eins.
Zwei Stimmen gegen eine.
Es war fast sicher eine Eins.

<!-- S13 -->
Wenn Rauschen jedes zehnte Bit kippt,
zufällig und unabhängig voneinander,
liegt die Mehrheit von dreien falsch
in weniger als drei von hundert Fällen.

<!-- S14 -->
Aber Sie haben alles,
was Sie senden, verdreifacht.
Um näher an die Perfektion zu kommen,
müssten Sie fünfmal wiederholen, dann neunmal,
dann hundertmal...
und die Nachricht kriecht nur noch dahin.

<!-- S15 -->
Lange Zeit
schien das der Preis zu sein.
Weniger Fehler, langsamere Nachrichten.
Merken Sie sich das.

<!-- S16 -->
Ende der 1940er-Jahre
hatte Richard Hamming bei den Bell Labs
ein ganz eigenes Problem.

<!-- S17 -->
Zeit an einem Relaisrechner bekam er meist
am Wochenende,
wenn niemand da war, der ihn beaufsichtigte.

<!-- S18 -->
Die Maschine konnte erkennen,
wenn ihr ein Fehler unterlaufen war.
Dann wiederholte sie den Schritt,
dreimal...
und brach danach seinen Auftrag ab.
Zwei Wochenenden hintereinander
verlor er seine Arbeit.

<!-- S20 -->
Seine Frage, in seinen eigenen Worten:
„Wenn die Maschine feststellen kann,
dass ein Fehler da ist,
warum kann sie nicht feststellen, wo er ist?“
Die tatsächliche Wortwahl, gab er zu,
war wohl etwas derber.

<!-- S22 -->
Seine Lösung nimmt vier Datenbits
und fügt drei Prüfbits hinzu.
Sieben Bits insgesamt.

<!-- S23 -->
Jedes Prüfbit überwacht
eine andere Gruppe von Positionen
und sorgt dafür, dass diese Gruppe
eine gerade Anzahl von Einsen enthält.

<!-- S24 -->
Die Gruppen überlappen sich nach einem genauen Muster.
Jede Position gehört
zu ihrer eigenen Kombination von Gruppen.

<!-- S25 -->
Jetzt kippen wir ein Bit.
Sagen wir, das an Position sechs.

<!-- S26 -->
Der Empfänger führt die drei Prüfungen erneut durch.
Die erste ist bestanden.
Die zweite schlägt fehl.
Die dritte schlägt fehl.

<!-- S27 -->
Schreiben Sie eine fehlgeschlagene Prüfung als Eins,
eine bestandene als Null,
und lesen Sie sie von der letzten zur ersten.
Eins, eins, null.
Binär ist das sechs.

<!-- S28 -->
Die Prüfungen sagen nicht nur,
dass etwas schiefgelaufen ist.
Sie zeigen genau auf das betroffene Bit.

<!-- S29 -->
Kippen Sie es zurück,
und die Nachricht ist wieder vollständig.
Niemand musste etwas zweimal senden.

<!-- S30 -->
Das ist also die Antwort.
Der Empfänger baut verlorene
Information nicht aus dem Nichts wieder auf.
Der Sender hat sie mit eingepackt,
schon im Voraus.

<!-- S32 -->
Das kann nicht jede Prüfung.
Eine Prüfsumme, wie die in unserem Video
über Btrfs,
kann Ihnen sagen, dass ein Block beschädigt ist,
aber nicht, wie die Originaldaten aussahen.

<!-- S33 -->
Und es gibt eine zweite Art von Schaden.
Manchmal ist ein Bit nicht falsch.
Es fehlt einfach,
und Sie wissen genau, wo die Lücke ist.

<!-- S34 -->
Das nennt man eine Auslöschung,
und Auslöschungen sind einfacher.

<!-- S35 -->
Schicken Sie vier Zahlen,
4, 7, 2 und 9,
und eine fünfte:
ihre Summe, 22.

<!-- S36 -->
Wenn irgendeine davon verloren geht,
verraten die anderen, welche es war.
4, 7, irgendwas, 9,
22.
Es muss eine Zwei sein.

<!-- S37 -->
Server schützen ihre Festplatten
mit einer ähnlichen Prüfung,
verteilt über die Laufwerke.
Fällt ein Laufwerk aus,
wird sein Inhalt aus den übrigen berechnet.

<!-- S38 -->
Wie viel muss man also hinzufügen?
Die Wiederholung sagt:
Um die Fehler auf null zu bringen,
muss man auch das Tempo auf null bringen.

<!-- S39 -->
Zwei Jahre bevor Hammings Artikel
erschien,
hatte sein Kollege Claude Shannon
eine seltsamere Antwort veröffentlicht.

<!-- S40 -->
Jeder Kanal,
eine Funkverbindung, ein Kabel, eine Disc,
hat eine Grenze.
Eine Höchstgeschwindigkeit für Information.

<!-- S41 -->
Unterhalb dieser Grenze
lassen sich Fehler beliebig selten machen,
ohne langsamer zu werden.
Nicht durch mehr Wiederholung.
Durch klügere Codierung.

<!-- S42 -->
Oberhalb davon
hilft kein Code der Welt.

<!-- S43 -->
Aber es gab einen Haken.
Shannon bewies, dass solche Codes existieren.
Er zeigte nicht, wie man einen baut,
den man tatsächlich benutzen kann.

<!-- S44 -->
Nach seinem Beweis wäre ein Zufallscode
fast sicher gut.
Doch der naheliegende Weg, ihn zu dekodieren,
heißt, das Angekommene
mit jeder möglichen Nachricht zu vergleichen...
und bei einem Block von 1000 Bits
gibt es davon mehr
als Atome im Universum.

<!-- S46 -->
Shannons Artikel war also keine Lösung.
Er war ein Versprechen.
Und Ingenieure verbrachten die nächsten
45 Jahre damit, es einzulösen.

<!-- S47 -->
Hammings Code war ein erster Schritt.
Er korrigiert ein falsches Bit von sieben.

<!-- S48 -->
Echte Schäden treten aber gebündelt auf.
Ein Kratzer oder ein Knacksen in der Leitung
zerstört Hunderte Bits am Stück.

<!-- S49 -->
1960 haben Irving Reed und Gustave Solomon
am Lincoln Laboratory des MIT
einen fünf Seiten langen Artikel veröffentlicht.

<!-- S50 -->
Ihre Codes arbeiten mit ganzen Bytes,
nicht mit einzelnen Bits.
Zerstört ein Fehlerbündel alle acht Bits
eines Bytes,
ist das trotzdem nur ein falsches Byte.

<!-- S51 -->
Eine gängige Variante hängt
32 Prüfbytes
an 223
Datenbytes an.

<!-- S52 -->
Sie kann beliebige 16 Bytes korrigieren,
die falsch ankommen...
oder 32 wiederherstellen,
die gar nicht ankommen.

<!-- S53 -->
So spielt eine CD trotz eines Kratzers weiter.
Ihre zwei Reed-Solomon-Codes
können eine Lücke vollständig reparieren,
die etwa 4000 Bits umfasst,
also 2,5 Millimeter Spur.

<!-- S54 -->
Und deshalb hat der zerrissene QR-Code
trotzdem funktioniert.
In der stärksten Einstellung
kann ein QR-Code
bis zu etwa 30 % seiner Bytes wiederherstellen
und dennoch jeden Buchstaben liefern.

<!-- S56 -->
Voyager 2 startete 1977
schon mit einem Reed-Solomon-Encoder an Bord.

<!-- S57 -->
Doch bei Jupiter und Saturn
schützte die Sonde alles außer den Bildern
mit einem älteren Code von Marcel Golay,
der ein zusätzliches Bit sendete
für jedes Datenbit.

<!-- S58 -->
Für Uranus und Neptun,
als das Signal immer schwächer wurde,
schalteten die Ingenieure Reed-Solomon zu,
zusätzlich zu einem zweiten Code,
den ohnehin schon jedes Bit durchlief.

<!-- S59 -->
Mit diesem zweiten Code allein
waren etwa fünf von tausend Bits
immer noch falsch.
Mit Reed-Solomon obendrauf
etwa eines von einer Million.

<!-- S60 -->
Auch Rauschen kommt gebündelt,
deshalb mischte Voyager
die Bytes von vier Blöcken
vor dem Senden durcheinander.

<!-- S61 -->
Ein Fehlerbündel, das einen Block zerstört hätte,
nimmt jetzt jedem nur ein paar Bytes weg...
so wenige, dass jeder Block
sich selbst reparieren kann.

<!-- S62 -->
Den Rest der Geschichte, wie Neptuns Bilder
nach Hause kamen,
erzählt unser Video über Voyager.

<!-- S63 -->
Aber selbst das
blieb noch hinter Shannons Grenze zurück...
und ein Code, der viel näher herankommen konnte,
existierte bereits.

<!-- S65 -->
1960, in seiner Doktorarbeit am MIT,
beschrieb Robert Gallager Codes
aus vielen einfachen Prüfungen,
von denen jede nur wenige Bits ansieht.

<!-- S66 -->
Beim Dekodieren reichten die Prüfungen
Schätzungen hin und her,
Runde um Runde...
viel zu viel
für die Computer der 1960er-Jahre.
Also legte man die Idee beiseite,
und 30 Jahre lang war sie fast vergessen.

<!-- S68 -->
1993
stellte ein Team um zwei französische Ingenieure,
Claude Berrou und Alain Glavieux,
die Turbo-Codes
auf einer Konferenz in Genf vor.

<!-- S69 -->
Ihre Ergebnisse lagen so nah
an Shannons Grenze,
dass viele Experten annahmen,
sie hätten einen Fehler gemacht.
Wahrscheinlich ein Faktor zwei,
irgendwo in ihren Rechnungen.

<!-- S70 -->
Innerhalb eines Jahres
hatten andere Labore es bestätigt.

<!-- S71 -->
Auch Turbo-Codes arbeiteten damit,
Schätzungen hin und her zu reichen,
und das führte die Leute zurück zu Gallager.

<!-- S72 -->
1995 und 1996
entdeckten David MacKay und Radford Neal
seine Codes wieder
und zeigten, dass sie
genauso nah herankommen konnten.

<!-- S73 -->
Im Jahr 2001
kam eine verfeinerte Version von Gallagers Codes
bis auf 0,04 Dezibel
an Shannons Grenze heran.

<!-- S74 -->
Das ist weniger als ein Prozent
mehr Signalleistung
als das theoretische Minimum.
Das Versprechen von 1948 war eingelöst.

<!-- S75 -->
Heute transportieren Gallagers Codes
einen Großteil der Daten in 5G-Handys,
in modernem WLAN
und im Satellitenfernsehen.

<!-- S77 -->
Jetzt zurück zu unseren acht Bits.
Drei gingen verloren,
und es gibt acht Möglichkeiten,
die Lücken zu füllen.

<!-- S78 -->
Aber diese acht Bits
waren nie bloß eine Nachricht.
Sie trugen vier Datenbits,
Hammings drei Prüfbits
und eine weitere Prüfung über alle acht.

<!-- S79 -->
Von allen 256
möglichen Mustern aus acht Bits
erfüllen nur 16 diese Regeln.

<!-- S80 -->
Testen Sie die acht Kandidaten.
Einer nach dem anderen fällt durch.
Nur einer bleibt übrig.

<!-- S81 -->
Die fehlenden Bits waren nie wirklich weg.
Ihre Information war noch da,
in den Bits, die überlebt haben.

<!-- S82 -->
Hier also eine Frage an Sie:
Haben Sie schon einmal bemerkt, wie Fehlerkorrektur
in etwas wirkt, das Sie jeden Tag benutzen?
Schreiben Sie es in die Kommentare.
