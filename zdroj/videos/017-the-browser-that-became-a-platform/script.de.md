# Internet Explorer 6 — Der Browser, der zur Plattform wurde

Übersetzung von `script.md`. Gleiche Szenenmarken, gleiche Zeilenzahl.
Eine Zeile = eine Phrase = ein Untertitel.

<!-- S01 -->
Stellen Sie sich vor, Sie sind Webentwickler
in den frühen Zweitausendern.

Sie haben
eine völlig vernünftige Webseite geschrieben.

<!-- S02 -->
Sie funktioniert in Netscape.

Sie funktioniert in Opera.

Sie funktioniert im neuen Firefox.

Und dann öffnen Sie sie
im Internet Explorer.

Alles ist kaputt.

<!-- S03 -->
Das Layout stimmt nicht.

Die Buttons sind verrutscht.

Die PNG-Bilder sehen furchtbar aus.

Und irgendwie hat
ein einziger Zeilenumbruch im HTML
eine Lücke von drei Pixeln erzeugt.

<!-- S04 -->
Willkommen in der Webentwicklung
im Zeitalter von Internet Explorer 6.

Aber jetzt kommt das Interessante.

Internet Explorer 6
war nicht einfach nur ein schlechter Browser.

<!-- S05 -->
Microsoft versuchte, Probleme zu lösen,
die das Web tatsächlich hatte.

Nur hatte Microsoft einen gewaltigen Vorteil
gegenüber allen anderen.

Windows.

<!-- S06 -->
Und dieser Vorteil erlaubte es
Microsoft schließlich, aus dem Browser
etwas sehr viel Größeres zu machen
als einen Browser.

<!-- S07 -->
Mitte der neunziger Jahre
wurde das Web beherrscht
von Netscape Navigator.

Microsoft gefiel das nicht.

<!-- S08 -->
Also wurde Internet Explorer
mit Windows ausgeliefert
und kostenlos angeboten.

Sie kauften einen Windows-Rechner.

Internet Explorer war schon da.

Nichts herunterzuladen.

Nichts zu bezahlen.

<!-- S09 -->
Und vor allem:
Microsoft kontrollierte
das Betriebssystem.

Kurz nach dem Jahr 2000
hatte Internet Explorer
mehr als neunzig Prozent
des Browsermarkts.

<!-- S10 -->
Internet Explorer 6 kam
im Jahr 2001,
zusammen mit Windows XP.

Und eine Weile sah es so aus,
als hätte Microsoft den Browserkrieg
schlicht gewonnen.

<!-- S11 -->
Microsoft hatte ein Problem.

Das Web konnte äußerst wenig.

HTML konnte Dokumente anzeigen.

CSS konnte sie gestalten.

JavaScript konnte sie interaktiv machen.

<!-- S12 -->
Und das war es dann auch.

Alles Kompliziertere
stieß direkt an
die Grenzen des Browsers.

<!-- S13 -->
Was, wenn Sie ein Dokument scannen wollten?

Oder mit einer Chipkarte sprechen?

Oder mit irgendeiner
Windows-Hardware reden?

<!-- S14 -->
Der Browser konnte das
alles nicht wirklich.

Also kam Microsoft mit einer Lösung.

ActiveX.

<!-- S15 -->
Die Grundidee war einfach.

Warum eine Webanwendung darauf beschränken,
was der Browser kann?

Lass sie doch einfach
native Windows-Komponenten benutzen.

<!-- S16 -->
Und plötzlich konnte eine Webseite
Dinge tun,
von denen gewöhnliches HTML
nicht einmal träumen konnte.

<!-- S17 -->
Heute klingt ActiveX beängstigend.

Und das zu Recht.

Eine ActiveX-Komponente kam heran
an die Dateien, die Anwendungen,
die Hardware
und das Betriebssystem.

<!-- S18 -->
Aus heutiger Sicht der Sicherheit
klingt das vollkommen wahnsinnig.

Kurz nach dem Jahr 2000
ergab es für Unternehmensanwendungen
aber vollkommen Sinn.

<!-- S19 -->
Firmen wollten keinen
hübschen Dokumentenbetrachter.

Sie wollten Anwendungen.

Sie wollten Webseiten,
die sich fast so verhalten
wie Desktop-Software.

<!-- S20 -->
Und genau das gab Microsoft ihnen.

Selbst Windows Update
setzte ursprünglich auf ActiveX,
um das System zu prüfen
und zu ermitteln, welche Updates
nötig waren.

<!-- S21 -->
ActiveX war also nicht einfach
ein dummer Fehler.

Es war ein früher Versuch,
aus dem Browser
eine Anwendungsplattform zu machen.

<!-- S22 -->
Und in dem Sinne war Microsoft
seiner Zeit tatsächlich voraus.

Das Problem war, wie viel Macht
es dieser Plattform gab.

<!-- S23 -->
ActiveX war nicht
die einzige Microsoft-Erweiterung.

Da war VBScript.

Da war DHTML.

Und sogar CSS expression.

Ja.

<!-- S24 -->
Internet Explorer konnte
JavaScript direkt in CSS auswerten.

So etwas ließ sich schreiben.

<!-- S25 -->
Es war absurd.

Und manchmal war es auch
überraschend nützlich.

Und nichts davon funktionierte
garantiert irgendwo sonst.

<!-- S26 -->
Microsoft setzte das Web
nicht einfach um.

Microsoft erweiterte das Web
in seine eigene Richtung.

Und mit neunzig Prozent
des Marktes
hatte es genug Macht,
damit durchzukommen.

<!-- S27 -->
Eines der berühmtesten Beispiele
war das CSS-Boxmodell.

Das Standardmodell besagte,
dass ein Element
mit 200 Pixeln Breite,
20 Pixeln Innenabstand
und 5 Pixeln Rahmen

<!-- S28 -->
insgesamt
250 Pixel breit ist.

<!-- S29 -->
Ältere Versionen des Internet Explorer
lasen das anders.

Im Quirks-Modus konnte die angegebene Breite
den Innenabstand
und den Rahmen enthalten.

<!-- S30 -->
Das war nicht zwangsläufig
eine verrückte Art, über Breite zu denken.

Heute fordern wir genau dieses
Verhalten sogar oft absichtlich an.

Es heißt border-box.

<!-- S31 -->
Das eigentliche Problem war,
dass sich verschiedene Browser
verschieden verhielten.

Und das bedeutete,
dass es die Entwickler kümmern musste.

Sehr.

<!-- S32 -->
Es gab etwas namens hasLayout.

Es war keine normale CSS-Eigenschaft.

Es war nicht Teil des Standards.

Aber es entschied darüber,
wie der Internet Explorer
Elemente anordnete.

<!-- S33 -->
Und manchmal ließ sich ein kaputtes Layout
auf mysteriöse Weise reparieren,
indem man eine einzige Zeile hinzufügte.

zoom: 1

Warum?

Weil zoom: 1 den internen
hasLayout-Mechanismus auslösen konnte.

<!-- S34 -->
Es gab Probleme
mit PNG-Transparenz.

Es gab Probleme mit select-Elementen,
die über absolut positionierten
Aufklappmenüs erschienen,
ganz gleich, wie hoch
man den z-index setzte.

<!-- S35 -->
Webentwicklung hieß nicht nur,
das eigene Design umzusetzen.

Sie hieß, die Fehler
einer bestimmten Browser-Engine zu lernen.

<!-- S36 -->
Noch ein wunderbares Beispiel.

Leerraum.

Und dafür konnte der Internet Explorer
nicht einmal etwas.

Man konnte zwei Bilder
direkt nebeneinander
ins Markup setzen,
ohne irgendetwas zwischen den Tags,
und bekam ein Ergebnis.

<!-- S37 -->
Dann formatierte jemand das HTML sauber
und setzte jeden Tag in eine eigene Zeile.

Und plötzlich war da
eine Lücke von ein paar Pixeln.

Der Zeilenumbruch wurde bedeutsam.

<!-- S38 -->
Ihr Code-Formatierer
konnte Ihre Webseite buchstäblich zerstören.

Und wenn Sie eine alte Version
von Visual Studio benutzten,
formatierte es Ihr HTML
bereitwillig von selbst.

Danke, Microsoft.

<!-- S39 -->
Entwickler sammelten
einen ganzen Werkzeugkasten voller Tricks.

Conditional Comments.

<!-- S40 -->
Und manchmal völlig
bizarr aussehendes HTML,
dessen einziger Zweck es war,
den Internet Explorer zu bändigen.

<!-- S41 -->
Sie schrieben hässlichen Code nicht,
weil Sie schlechte Programmierer waren.

Sie schrieben hässlichen Code,
weil der Browser Sie dazu zwang.

<!-- S42 -->
Der Internet Explorer stürzte auch
spektakulär ab und riss dabei oft
jedes offene Fenster mit sich.

<!-- S43 -->
Das führte zu einer wunderbaren Form
von Büro-Unterhaltung.

Hey, schau dir mal diesen Link an.

Und zwanzig Internet-Explorer-Fenster
verschwinden.

<!-- S44 -->
Das war das Web, bevor Browser
in einer Sandbox liefen.

Der heutige Browser sagt das hier.

Dieser Website traue ich nicht.

Ich sperre sie ab.

<!-- S45 -->
Internet Explorer 6
wirkte eher so.

Du bist eine Webseite?

Klar.

Hier sind die Schlüssel zum Gebäude.

<!-- S46 -->
Warum benutzten Entwickler
diese Tricks überhaupt?

Weil sie mussten.

<!-- S47 -->
Stellen Sie sich eine Firma
mit fünfhundert Angestellten vor.

Auf jedem Rechner läuft Windows XP.

Auf jedem ist Internet Explorer.

<!-- S48 -->
Der Entwickler hat zwei Möglichkeiten.

Möglichkeit eins.

Für den Internet Explorer bauen,
den ohnehin alle haben.

<!-- S49 -->
Möglichkeit zwei.

Für jeden Browser bauen,
alles überall testen
und der IT-Abteilung erklären,
warum alle noch einen zweiten brauchen.

Die Antwort war meist offensichtlich.

<!-- S50 -->
Sie wählten Microsoft-Technik
nicht deshalb,
weil sie Microsoft liebten.

Sie wählten das, was das Problem
des Kunden löste.

Und manchmal war ActiveX
das beste verfügbare Werkzeug.

<!-- S51 -->
Irgendwann hatte jemand genug.

JavaScript-Bibliotheken begannen,
die Browserunterschiede zu verstecken.

Eine der wichtigsten
war jQuery.

<!-- S52 -->
Statt browserspezifische
Ereignisbehandlung zu schreiben,
schrieb man eine einzige Zeile,
die überall funktionierte.

<!-- S53 -->
Statt sich von Hand
mit verschiedenen AJAX-Umsetzungen zu plagen,
benutzte man eine gemeinsame Abstraktion.

<!-- S54 -->
jQuery ließ den Internet Explorer
nicht verschwinden.

Aber sie machte es viel leichter
so zu tun, als gäbe es ihn nicht.

Und für Webentwickler jener Zeit
war das etwas Wunderbares.

<!-- S55 -->
Firefox erschien.

Opera entwickelte sich weiter.

Safari kam dazu.

Und schließlich veröffentlichte Google Chrome.

<!-- S56 -->
Die Browserkriege waren zurück,
und diesmal
sah der Wettbewerb anders aus.

JavaScript-Engines
wurden dramatisch besser.

HTML5 kam.

<!-- S57 -->
Der Browser selbst begann all das zu lernen,
wofür Entwickler zuvor
Plugins gebraucht hatten.

<!-- S58 -->
Video.

Audio.

Canvas.

SVG.

WebGL.

WebSockets.

Und schließlich WebRTC.

Das Web wurde
zu einer Anwendungsplattform.

<!-- S59 -->
Und das war genau das,
was Microsoft
mit ActiveX erreichen wollte.

Nur geschah es jetzt
über offene Standards.

<!-- S60 -->
Microsoft versuchte es noch einmal.

Silverlight ließ Entwickler
reichhaltige Browseranwendungen
in C# und .NET bauen.

Sogar Netflix' frühes Streaming
lief damit.

<!-- S61 -->
Aber das Web wollte Plugins nicht ewig.

Apple weigerte sich, Flash
auf dem iPhone zu unterstützen.

Und plötzlich war die Zukunft nicht das hier.

Browser plus Plugin.

Sie war das hier.

Der Browser selbst.

<!-- S62 -->
Silverlight verschwand.

Flash verschwand.

ActiveX verschwand.

Und schließlich verschwand
auch der Internet Explorer.

<!-- S63 -->
Und hier wird
die Geschichte interessant.

Denn Microsoft
lag nicht völlig falsch.

Es hatte richtig vorhergesagt,
dass der Browser
zur Anwendungsplattform wird.

<!-- S64 -->
Es versuchte nur, über
proprietäre Technik dorthin zu kommen.

Das Web erreichte dasselbe Ziel
über Standards.

<!-- S65 -->
Der Browser gewann.

Aber er gewann, indem er
etwas weit Mächtigeres wurde
als der Browser
von 2001.

<!-- S66 -->
War Microsoft also der Bösewicht?

Eigentlich nicht.

Und genau das macht
die Geschichte interessanter.

<!-- S67 -->
Microsoft hatte großartige Ingenieure.

Es hatte enorme Mittel.

Und es baute viele Technologien,
die ihrer Zeit wirklich voraus waren.

<!-- S68 -->
Aber Microsoft hatte auch
eine erdrückende Marktstellung.

Und das schuf
einen gefährlichen Anreiz.

<!-- S69 -->
Wenn fast jeder
Ihren Browser benutzt,
warum auf Standards warten?

Warum nicht einfach
die eigene Lösung umsetzen?

Eine Weile funktionierte das.

Bis der Rest des Webs aufholte.

<!-- S70 -->
Heute ist der Internet Explorer weg.

Die alten Browserkriege
wirken wie ferne Geschichte.

Aber sehen Sie sich
den heutigen Browsermarkt an.

Chrome.

Edge.

Opera.

Brave.

Vivaldi.

<!-- S71 -->
Und viele weitere
bauen auf Chromium.

Verschiedene Produkte.

Oft dieselbe
Browser-Engine darunter.

<!-- S72 -->
Vielleicht haben wir also das hier getauscht.

Einen Browser, den alle unterstützen mussten.

Gegen das hier.

Eine Engine, auf der alle bauen.

Kommt Ihnen das bekannt vor?

<!-- S73 -->
Denn eine beherrschende Engine
entscheidet nicht nur darüber,
wie Websites dargestellt werden.

<!-- S74 -->
Sie beeinflusst, was Entwickler bauen.

Welche Techniken populär werden.

Und letztlich das,
was aus dem Web selbst wird.

<!-- S75 -->
Es gibt allerdings
einen sehr wichtigen Unterschied.

Das heutige Web ruht
auf offenen Standards.

Firefox hat weiterhin seine eigene Engine.

Safari hat WebKit.

Chromium ist quelloffen.

<!-- S76 -->
Und moderne Browser
aktualisieren sich selbst.

Wir sind weit entfernt
von der Situation
des Jahres 2003.

<!-- S77 -->
Aber die Grundfrage bleibt.

Wie viel Einfluss
sollte ein einzelnes Unternehmen
auf eine Plattform haben,
die fast jeder benutzt?

Das ist die Frage,
die nie wirklich verschwunden ist.

<!-- S78 -->
War Internet Explorer 6 also furchtbar?

Ja.

Manchmal spektakulär furchtbar.

<!-- S79 -->
Aber das ist nicht die ganze Geschichte.

Er war auch ein Produkt seiner Zeit.

<!-- S80 -->
Das Problem war,
dass Microsoft die Browserkriege
so vollständig gewonnen hatte,
dass es die Regeln bestimmen konnte.

<!-- S81 -->
Und Webentwickler zahlten den Preis.

Sie lernten die Geheimnisse
von hasLayout.

Sie entdeckten, dass zoom: 1
Dinge auf magische Weise repariert.

Und sie beteten.

<!-- S82 -->
Und schließlich wurde der Internet Explorer
zu dem, woran er zwanzig Jahre lang
selbst gebaut hatte.

Eine Alt-Plattform,
die niemand mehr
unterstützen wollte.

<!-- S83 -->
Das Web hat Microsofts Vision
nicht abgelehnt.

Es hat einfach
eine bessere Fassung davon gebaut.

Und wenn uns diese Zeit
eines lehren sollte,
dann das hier.

<!-- S84 -->
Technik wird nicht zum Standard,
nur weil sie gut ist.

<!-- S85 -->
Manchmal wird sie zum Standard,
weil ein Unternehmen genug Macht hat,
sie allen aufzuzwingen.

<!-- S86 -->
Und manchmal merken wir
zwanzig Jahre später,
dass wir es wieder getan haben.
