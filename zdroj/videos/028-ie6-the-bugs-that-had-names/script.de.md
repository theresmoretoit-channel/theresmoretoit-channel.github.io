# Internet Explorer 6 — Die Bugs, die Namen hatten

<!-- S01 -->
Das ist Teil zwei.

Wenn du Teil eins nicht gesehen hast,
der Link steht unten.

Die Kurzfassung bekommst du trotzdem.

<!-- S02 -->
Im Jahr 2001
veröffentlichte Microsoft
den Internet Explorer 6,
und er kam mit Windows XP.

Innerhalb weniger Jahre
hatte er über neunzig Prozent
des Browsermarkts.

<!-- S03 -->
Microsoft nutzte das,
um aus dem Browser
eine Anwendungsplattform zu machen.

Das war eine echte Idee.

Bezahlt haben sie nur
zufällig die Webentwickler.

<!-- S04 -->
Das war Teil eins.

Aber ich habe etwas ausgelassen.

Ich habe den Teil ausgelassen,
in dem die Bugs Namen hatten.

<!-- S05 -->
Ein Browser-Bug ist normalerweise
eine Nummer in einem Ticketsystem.

Issue 4172.

Niemand erinnert sich daran.

Niemand redet beim Mittagessen darüber.

<!-- S06 -->
Im Internet Explorer 6
hatten die Bugs Eigennamen.

Und das ist, wie sich zeigt,
das Aufschlussreichste
an dieser ganzen Zeit.

<!-- S07 -->
Fangen wir sanft an.

Du lässt ein Bild nach links floaten
und setzt einen Absatz daneben.

Der Text soll
direkt neben dem Bild sitzen.

Stattdessen sitzt er
drei Pixel entfernt.

<!-- S08 -->
Nicht vier.

<!-- S08b -->
Nicht zwei.

<!-- S08c -->
Drei.

<!-- S08d -->
Jedes Mal.

Es hatte einen Namen.

The Three Pixel Jog.

<!-- S09 -->
Jetzt lass das Bild nach links floaten
und gib ihm einen linken Rand
von zehn Pixeln.

Der Internet Explorer 6
gibt ihm zwanzig.

Er verdoppelt den Rand,
aber nur auf der Seite,
zu der du gefloatet hast.

<!-- S10 -->
The Double Margin Bug.

Und die anerkannte Lösung
war, ein gefloatetes Element
zu inline zu erklären.

<!-- S11 -->
Was Unsinn ist.

Ein Float ist ein Block.

Ihn inline zu nennen
bedeutet überhaupt nichts.

Es funktionierte, also schrieb man es.

<!-- S12 -->
Der nächste ist besser.

Du lädst eine Seite,
und ein Teil des Inhalts
ist schlicht nicht da.

Du scrollst nach unten.

Du scrollst wieder nach oben.

Und da ist er.

<!-- S13 -->
Nichts wurde geladen.

Nichts hat sich geändert.

Er war nur schüchtern.

Und er hatte den richtigen Namen.

The Peekaboo Bug.

<!-- S14 -->
Das Heilmittel war, dem
fehlenden Element zu sagen,
seine Position sei relativ.

Niemand konnte ganz erklären,
warum es dadurch zurückkam.

<!-- S15 -->
Dann gibt es den,
bei dem du über einen Link fährst
und der Hintergrund
des Kastens darunter
in gerader Linie abgeschnitten wird.

The Guillotine Bug.

<!-- S16 -->
Es gab einen Bug, bei dem Text
von seinem Platz wegkroch.

Magic Creeping Text.

Es gab einen, bei dem Rahmen
an der falschen Stelle,
in der falschen Farbe
oder gar nicht erschienen.

Border Chaos.

<!-- S17 -->
Mein Liebling ist leiser.

Du setzt eine Reihe Kästen,
und Buchstaben aus dem letzten
tauchen darunter noch einmal auf.

Nicht immer.

Nicht vorhersehbar.

The Duplicate Character Bug.

<!-- S18 -->
Und was darüber entschied,
ob es dich traf,
und wie viele Buchstaben
doppelt herauskamen,
war die Zahl der HTML-Kommentare,
die du im Quelltext gelassen hattest.

Kommentare.

Das Einzige in der Datei,
das der Browser
wegwerfen soll.

<!-- S19 -->
Es gibt noch einen,
und der ist anders,
weil man diesen
mit Absicht benutzte.

Wenn du eine Höhe setzt
und der Inhalt höher ist,
soll der Kasten überlaufen.

Der Internet Explorer 6
vergrößerte stattdessen den Kasten.

<!-- S20 -->
Was falsch ist.

Es ist zugleich genau das,
was eine Mindesthöhe tut.

Und der Internet Explorer 6
hatte keine Mindesthöhe.

Also hörten Entwickler auf,
diesen Bug zu melden,
und verließen sich auf ihn.

<!-- S21 -->
Halt kurz inne und sieh dir die Liste an.

The Three Pixel Jog.

The Double Margin Bug.

Peekaboo.

The Guillotine.

Einen Bug, dem man einmal begegnet,
benennt man nicht.

<!-- S22 -->
Diese hatten Namen,
weil ihnen alle begegneten.

Und jetzt kommt der Teil,
der es schlimmer macht.

Die meisten von ihnen hatten
dieselbe Ursache darunter.

<!-- S23 -->
Im Internet Explorer 6
hatte jedes Element entweder
oder eben nicht
etwas, das layout hieß.

<!-- S24 -->
Es entschied, ob das Element
Größe und Position selbst bestimmte
oder das dem Elternelement überließ.

Und setzen konntest du es nicht.

<!-- S25 -->
Es gab keine Eigenschaft
namens layout,
und keine Möglichkeit, sie anzufordern.

Sie stand in keiner Spezifikation.

Sie war ein internes Flag
in der Rendering-Engine.

<!-- S26 -->
Umlegen konntest du es
aber aus Versehen.

Eine Breite zu setzen tat es.

Eine Höhe zu setzen tat es.

Ein Element zu floaten tat es.

Also war die Hälfte der Lösungen in diesem Video
das Umlegen eines Schalters,
den niemand sehen konnte.

<!-- S27 -->
Deshalb suchte man
nach dem billigsten Weg,
ihn mit Absicht umzulegen.

Einer war, eine Höhe
von einem Prozent zu setzen.

<!-- S28 -->
Alle anderen Browser
mussten davon ferngehalten werden,
also kam es in einen Hack,
zu dem wir gleich kommen.

<!-- S29 -->
Und im Internet Explorer 6
schadete es nicht,
denn eine Höhe, in die es nicht passt,
wächst es ohnehin über.

Der Bug von vor zwei Minuten
ist es, der die Lösung sicher macht.

<!-- S30 -->
Er hatte einen Namen.

The Holly Hack.

<!-- S31 -->
Der andere Weg
war eine Microsoft-Eigenschaft
namens zoom, auf eins gesetzt.

Zoom eins bedeutet
nicht zoomen.

<!-- S32 -->
Es änderte nichts Sichtbares.

Genau das war der Punkt.

Es stand in Stylesheets
einzig deshalb,
um ein unsichtbares Flag zu setzen,
das die Bugs verschwinden ließ.

<!-- S33 -->
Womit wir bei den Hacks wären,
und bei den Hacks
wird es seltsam.

Um einen Browser zu reparieren,
musst du erst mit genau diesem
sprechen können.

<!-- S34 -->
Und der Internet Explorer 6
verhielt sich, als gäbe es
noch ein Element
über dem html-Element.

Kein anderer Browser tat das.

Dokumentiert war es nicht.

So verhielt er sich einfach.

<!-- S35 -->
Also schriebst du eine Regel,
die auf das Phantom passte,
und nur dieser Browser
konnte sie sehen.

Stern, Leerzeichen, html.

<!-- S36 -->
Jeder andere Browser sah sie an,
fand nichts, was passte,
und machte weiter.

Das ist der star hack,
und jahrelang stand er
in fast jedem Stylesheet
im Web.

<!-- S37 -->
Es gab auch
den underscore hack.

Du setzt einen Unterstrich
vor einen Eigenschaftsnamen.

<!-- S38 -->
Ein standardkonformer Browser
wirft die Zeile
als ungültig weg.

Der Internet Explorer 6
ignoriert den Unterstrich
und wendet sie an.

<!-- S39 -->
Du hast also absichtlich
dein eigenes Stylesheet kaputt gemacht,
und das Kaputtsein
war die Anweisung.

<!-- S40 -->
Und dann gibt es den,
den Microsoft mit Absicht gebaut hat.

Du konntest einen Kommentar schreiben,
dem nur der Internet Explorer gehorchte.

<!-- S41 -->
Für jeden anderen Browser
war es ein gewöhnlicher Kommentar,
ignoriert, wie man Kommentare ignoriert.

Für den Internet Explorer 6
war es eine Tür
in eine zweite Version
der Seite.

<!-- S42 -->
Das heißt, der Hersteller
sah sich die Lage an,
stimmte zu, dass dieser Browser
ein eigenes Stylesheet braucht,
und lieferte eine Funktion,
die das erleichtert.

<!-- S43 -->
Ein Teil des Schadens
brauchte gar keinen Bug.

Der Internet Explorer 6
hatte zwei Modi.

Im modernen
folgte er dem Standard.

<!-- S44 -->
Im alten
umfasste die Breite eines Kastens
seinen Innenabstand
und seinen Rahmen,
was eine völlig
andere Zahl ist.

<!-- S45 -->
Welchen Modus du bekamst,
hing von der ersten Zeile
des Dokuments ab.

Und die HTML-Version,
zu der alle wechselten,
sagte dir, du sollst dort oben
eine XML-Deklaration hinschreiben.

<!-- S46 -->
Diese Zeile schob
den Internet Explorer 6
in den alten Modus.

Kaputt gemacht hat es,
dass du dem neueren Standard folgtest.

<!-- S47 -->
Dann ist da die Transparenz.

Der Internet Explorer 6 konnte
kein PNG mit weichen Kanten zeigen.

Wo das Bild ausblenden sollte,
setzte er Grau.

<!-- S48 -->
Microsofts Antwort war ein Filter
mit einem Namen wie eine Seriennummer.

Er funktionierte.

<!-- S49 -->
Aber er malte außerhalb
des normalen Rendering-Prozesses
des Browsers,
also hörten Links, die du darüberlegtest,
oft auf zu funktionieren.

Du hast das Bild repariert
und den Link kaputt gemacht.

<!-- S50 -->
Und alles andere auszublenden
war ein zweiter Filter,
mit eigener Syntax,
der im Stylesheet
direkt neben der gewöhnlichen Eigenschaft stand,
die jeder andere Browser verstand.

<!-- S51 -->
Manches davon ist älter
als die Bugs selbst.

Vor all dem
wurden Layouts
aus verschachtelten Tabellen gebaut.

<!-- S52 -->
Und um eine Lücke offen zu halten,
nahmst du ein transparentes Bild
von einem Pixel Breite,
gedehnt auf die Größe,
die die Lücke gerade brauchte.

Auch das hatte einen Namen.

The spacer gif.

<!-- S53 -->
Hovern war noch so etwas.

Im Internet Explorer 6
funktionierte Hover bei Links.

Nur bei Links.

<!-- S54 -->
Ein Menü, das aufging,
wenn du mit der Maus
über irgendetwas anderes fuhrst,
brauchte also ein kleines Programm,
das am Stylesheet hing.

<!-- S55 -->
Kein Skript in der Seite.

Eine eigene Datei,
aus CSS referenziert,
mit Code, dessen Aufgabe es war,
dem Browser
einen Selektor beizubringen.

Diese Datei reichten sich Leute
jahrelang weiter.

<!-- S56 -->
Teil eins erwähnte,
dass man JavaScript
in ein Stylesheet schreiben konnte.

Was er nicht erwähnte,
ist, wie oft dieses JavaScript lief.

<!-- S57 -->
Bei jeder Mausbewegung.

Bei jedem Tastendruck.

Bei jedem Scrollen.

Immer und immer wieder,
für eine einzige Breite.

<!-- S58 -->
Und der Browser hatte Obergrenzen,
die sonst niemand hatte.

Ein Stylesheet hörte auf zu gelten
irgendwo jenseits von
viertausend Regeln.

Alles nach
dem einunddreißigsten Stylesheet
einer Seite wurde ignoriert.

<!-- S59 -->
Was nach einer Zahl klingt,
die man nie erreicht,
bis deine Website so groß ist,
dass jemand einen Build-Schritt
schreiben muss, dessen einzige Aufgabe
es ist, Stylesheets zusammenzufügen,
bevor der Browser sie sieht.

<!-- S60 -->
Und manches davon war
überhaupt nicht kosmetisch.

Der Internet Explorer 6
zählte seine Seitenobjekte
und seine Skriptobjekte
auf zwei verschiedene Arten,
und keine der beiden Seiten
sah die ganze Schleife.

<!-- S61 -->
Wenn also ein Skript
auf einen Teil der Seite zeigte
und dieser Teil der Seite
zurück auf das Skript,
wurde keines je freigegeben.

Lass das Fenster lange genug offen,
und der Browser fraß die Maschine.

<!-- S62 -->
Der beste aber
ist gar kein Layout-Bug.

Du schreibst ein input-Tag.

Du gibst ihm einen Typ.

Und du vergisst das Gleichheitszeichen.

<!-- S63 -->
Das ist ein fehlerhaftes Attribut.

Jeder je geschriebene Parser
hat darauf eine Antwort.

Ignorier es.

Rate, was gemeint war.

Mach weiter.

<!-- S64 -->
Der Internet Explorer stürzte ab.

Innen wollte er wissen,
ob das Feld versteckt ist,
also verglich er, was du geschrieben hattest,
mit dem Wort hidden.

Du hattest nichts geschrieben.

<!-- S65 -->
Also holte er das,
was du nicht geschrieben hattest,
von Adresse null.

Was ein ganz
gewöhnlicher Browser-Absturz wäre,
nur dass der Code, der das tat,
nicht im Browser steckte.

<!-- S66 -->
Er steckte in einer gemeinsamen Systembibliothek.

Also legten diese drei Wörter
auch das Mailprogramm lahm
und die Vorschau
im Dateimanager.

<!-- S67 -->
Ein Fenster mit Dateien
auf deiner eigenen Maschine,
geschlossen von einer Webseite.

Das ist das Argument von Teil eins,
angekommen als Absturzbericht.

Der Browser war kein Programm,
das auf dem System lief.

Er war ein Teil des Systems.

<!-- S68 -->
Und du konntest die Lösung
nicht einfach woanders testen.

Der Internet Explorer war
mit dem Betriebssystem verschweißt,
also lief auf einem Rechner
genau eine Version.

<!-- S69 -->
Deshalb gehörte zu einem Frontend-Job
im Jahr 2006
ein Regal
mit Ersatzrechnern.

<!-- S70 -->
Und später ein Ordner
mit virtuellen,
von denen jeder ein ganzes
Betriebssystem trug,
damit sich darin eine
einzige Seite öffnen ließ.

<!-- S71 -->
Und dann tat jemand
das Naheliegende.

Wenn du dem Browser
eine fehlende Funktion beibringen kannst,
kannst du ihm alle beibringen.

<!-- S72 -->
Ein Entwickler namens Dean Edwards
schrieb eine Bibliothek,
deren einziger Zweck es war,
den Internet Explorer 6 dazu zu bringen,
sich wie eine spätere Version
seiner selbst zu verhalten.

Das setzten Leute ein.

Produktiv.

<!-- S73 -->
Und hier hört es auf,
lustig zu sein.

Fast ein Jahrzehnt lang
floss ein erheblicher Teil
der weltweiten Frontend-Arbeit
in die Fehler eines Browsers.

Keine Funktionen.

Keine Produkte.

Kompensation.

<!-- S74 -->
Und es hielt sich wegen dem,
worum es in Teil eins ging.

Firmen hatten darauf
echte Anwendungen gebaut,
solche, die nur dort liefen,
und diese Anwendungen
mussten montags weiter funktionieren.

<!-- S75 -->
Der Browser, den alle
loswerden wollten,
war also der, den niemand
entfernen durfte.

<!-- S76 -->
Im Jahr 2010
kündigte Google an, dass seine eigenen
Apps darin nicht mehr funktionieren würden.

Und ein Designstudio in Denver
fand, das verdiene eine Beerdigung.

<!-- S77 -->
Eine echte.

Einen Sarg.

Eine Grabrede.

Achtzig bis hundert Menschen
kamen, um einen Browser
begraben zu sehen.

Geplant hatten sie mit dreißig.

<!-- S78 -->
Und Microsoft schickte Blumen.

Auf der Karte stand:
danke für die schöne Zeit,
Internet Explorer 6.

<!-- S79 -->
Genau ein Jahr später
startete Microsoft eine Website.

Sie verfolgte, wie viel der Welt
noch immer
den Internet Explorer 6 nutzte,
Land für Land.

<!-- S80 -->
Zu dem Zeitpunkt
waren es noch zwölf Prozent.

Das Ziel war, es
unter eins zu drücken.

Die Firma, die den Browser gebaut hatte,
betrieb einen öffentlichen Countdown
zum Tod ihres eigenen Produkts.

<!-- S81 -->
Warum hatten die Bugs also Namen?

Weil man benennt, was man
nicht umgehen kann.

<!-- S82 -->
Niemand benennt das Wetter
in einem Land,
durch das er nur durchfährt.

Man benennt es dort, wo man wohnt.

Und etwa zehn Jahre lang
wohnte das Web genau dort.

<!-- S83 -->
Aber den Internet Explorer 6
aus dem Web zu bekommen, ist eine andere Geschichte.

Und dahin gehen wir als Nächstes.

Wenn du die willst,
es gibt einen Abonnieren-Knopf,
und Teil eins ist unten verlinkt.
