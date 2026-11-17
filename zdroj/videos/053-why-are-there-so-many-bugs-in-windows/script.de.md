<!-- S01 -->
Im September 2026 hat ein einziger
Schwung Windows-Updates vier Dinge
auf einmal kaputt gemacht.

<!-- S02 -->
Der Ton ging nicht mehr.
Remote Desktop ging nicht mehr.
Freigegebene Ordner in virtuellen
Maschinen gingen nicht mehr.

<!-- S03 -->
Und manche Rechner vertrauten
dem Firmennetz nicht mehr,
zu dem sie gehörten,
niemand kam mehr rein.

<!-- S04 -->
Ein Schwung.
Ein Dienstag.

<!-- S05 -->
Und falls du denkst,
das sei nur wieder ein
schlechtes Windows-Update...

<!-- S06 -->
ist es das nicht.

<!-- S07 -->
Denn das passiert
immer und immer und immer wieder.

<!-- S08 -->
Was macht deren QA eigentlich?

<!-- S09 -->
Wie kann eine so riesige Firma
ein Systemupdate ausliefern
und etwas so Offensichtliches übersehen?

<!-- S10 -->
Fangen wir mit dem Kleinsten an.

<!-- S11 -->
Microsoft lieferte ein Update aus,
das ein paar Dinge
an der Taskleiste änderte.
Und kurz darauf räumte man ein,
dass es ein Problem
mit den Mauszeigereinstellungen gab.

<!-- S12 -->
Bei manchen sprang ein eigener Zeiger
auf einen großen weißen Pfeil zurück.
So einer, bei dem du nachsiehst,
ob du versehentlich einen Rechner
von 1998 gestartet hast.

<!-- S13 -->
Dein sorgfältig gewählter Zeiger?
Weg.
Und ihn zurückzusetzen
hat offenbar auch nicht geklappt.

<!-- S14 -->
Jetzt denkst du vielleicht:
jede Software hat Fehler.
Genau.

<!-- S15 -->
Aber es ist ein Unterschied zwischen:
„Wir haben einen seltenen Fehler
unter einer ungewöhnlichen
Hardwarekonfiguration gefunden.“

<!-- S16 -->
Und:
„Nach unserem Update
sieht deine Maus nicht mehr aus wie
die Maus, die du gewählt hast.“

<!-- S17 -->
Denn jemand muss es installieren.
Jemand muss sich anmelden.
Jemand muss die Maus bewegen.
Und das hat offenbar nicht gereicht.

<!-- S18 -->
Dann ist da der Ton.
Update installieren.
Neu starten.
Kein Ton.

<!-- S19 -->
Manche USB-Audiogeräte hören einfach auf,
und Windows meldet,
dass das Gerät nicht starten kann.

<!-- S20 -->
Und Ton ist nun wirklich
keine exotische Funktion.
Man sollte meinen, einer der Grundtests
für ein Betriebssystem wäre:

<!-- S21 -->
bringt der Rechner noch einen Ton heraus?

<!-- S22 -->
Offenbar ist das komplizierter,
als es klingt.
Buchstäblich.

<!-- S23 -->
Zu Hause ist das alles ärgerlich.
Der Zeiger sieht albern aus.
Die Lautsprecher schweigen.
Aber du überlebst es.

<!-- S24 -->
Doch ein Server, der dem Netz
nicht mehr vertraut,
bedeutet: niemand kommt rein,
und jemand in der IT-Abteilung
hat einen sehr schlechten Morgen.

<!-- S25 -->
Und hier hört es auf,
eine Sammlung lustiger Geschichten.

<!-- S26 -->
Denn wir können in Microsofts
eigene Update-Historie schauen.
Microsoft veröffentlicht sie.
Jeden Monat listen sie auf,
was ihre Updates kaputt gemacht haben.

<!-- S27 -->
Und wenn du ein einziges Jahr
dieser Liste nebeneinanderlegst,
wiederholt sich dasselbe Muster
immer wieder.

<!-- S28 -->
Januar zerlegte Audiogeräte
und Webcams.
Februar ließ den Zeiger kreiseln,
sodass der Rechner eingefroren wirkte.

<!-- S29 -->
März brachte Bluescreens
und Installationen,
die auf halbem Weg hängen blieben.
April zerlegte die Anmeldung
per Gesicht.

<!-- S30 -->
Im Mai reagierte der Explorer
nicht mehr auf die Maus.
Und Oktober zerlegte Verbindungen
zum eigenen Rechner.

<!-- S31 -->
Nicht das Internet.
Die Adresse, die „dieser Rechner“ heißt.

<!-- S32 -->
Und zwei davon
sind wirklich bemerkenswert.

<!-- S33 -->
Ein Update zerlegte die Schaltfläche,
die den PC zurücksetzt.
Ein anderes den Wiederherstellungs-
bildschirm, wo USB-Mäuse und
Tastaturen nicht mehr reagierten.

<!-- S34 -->
Lies das noch einmal.

<!-- S35 -->
Zweimal in drei Monaten zerlegte
ein Update genau das Werkzeug,
mit dem man einen Rechner repariert.

<!-- S36 -->
Und noch ein Detail,
vielleicht das wichtigste.
Dieser Audio-Fehler, bei dem Windows
sagt, das Gerät könne nicht starten?

<!-- S37 -->
Er tauchte im Januar auf.
Und dann tauchte er wieder auf,
zwanzig Monate später.

<!-- S38 -->
Dasselbe Symptom.
Dieselbe Art Gerät.
Dieselbe Meldung.

<!-- S39 -->
Das ist keine Geschichte
über schlechten Code.
Das ist eine Geschichte über Tests.

<!-- S40 -->
Und nichts davon ist neu.

<!-- S41 -->
2024 gab es ein Update,
nach dem Linux auf Rechnern
mit zwei Systemen nicht mehr startete.
Die Fehlermeldung lautete wörtlich:

<!-- S42 -->
„Etwas ist
ernsthaft schiefgelaufen.“

<!-- S43 -->
Was ehrlich gesagt die treffendste
Fehlermeldung ist, die Windows je zeigte.

<!-- S44 -->
Und 2018 gab es eine Version,
die komplett zurückgezogen wurde,
nachdem Leute berichteten,
dass ihre Dateien weg waren.

<!-- S45 -->
An dieser Stelle
kannst du vernünftig schließen:
Microsoft ist einfach nicht gut
darin, Software zu schreiben.

<!-- S46 -->
Und das würde alles erklären.
Die Fehler.
Die Regressionen.
Die Updates, die eines reparieren
und ein anderes zerlegen.

<!-- S47 -->
Aber diese Erklärung
hat ein Problem.
Microsoft macht nicht nur Windows.

<!-- S48 -->
Sie machen Office.
Visual Studio.
Exchange.
Teams.
Und eine sehr große Cloud.

<!-- S49 -->
Und all das hatte
eigene Fehler, eigene Regressionen
und eigene spektakuläre Ausfälle.

<!-- S50 -->
Und das ist wichtig.
Denn die übliche Erklärung für
Windows lautet, es schleppe
dreißig Jahre alten Code mit.

<!-- S51 -->
Ein moderner Cloud-Dienst
schleppt keine dreißig Jahre
von irgendetwas mit.
Er wurde kürzlich gebaut,
von Leuten, die wussten,
was sie bauen.

<!-- S52 -->
Und er geht trotzdem kaputt.

<!-- S53 -->
Das Problem war also nie
bloß alter Code.
Das Problem ist Komplexität
in Microsofts Größenordnung.

<!-- S54 -->
Und Windows ist die Stelle,
wo man diese Komplexität
am besten sieht.

<!-- S55 -->
Denn Windows ist eigentlich nicht
ein Betriebssystem.
Ganz unten liegt eine Architektur,
die bis in die frühen Neunziger reicht.

<!-- S56 -->
Dann Jahrzehnte von Schnittstellen.
Dann Kompatibilitätsschichten.
Dann Treiber.
Dann Dienste.

<!-- S57 -->
Dann neuere Frameworks,
gebaut auf älteren Frameworks.
Dann ein neues Aussehen.
Dann noch ein neues Aussehen.

<!-- S58 -->
Es ist weniger ein Betriebssystem
als eine archäologische Grabung,
die irgendwie noch läuft.

<!-- S59 -->
Und Microsoft darf
die Grabung nicht planieren,
weil Firmen von dem abhängen,
was darunter liegt.
Dazu gibt es ein ganzes Video.

<!-- S60 -->
Wichtig ist hier,
was das mit Fehlern macht.
Jede Schicht muss weiter
mit jeder Schicht darunter laufen.

<!-- S61 -->
Eine Änderung hier oben
kann also etwas zerlegen,
das seit Jahren niemand angesehen hat.

<!-- S62 -->
Und es gibt noch einen Hinweis
darauf, wie das läuft,
und der handelt gar nicht von Fehlern.

<!-- S63 -->
Es ist ein Muster.
Microsoft entfernt etwas.
Nutzer beschweren sich.
Microsoft überdenkt es
jahrelang.

<!-- S64 -->
Und in der Zwischenzeit
baut jemand anders ein Werkzeug,
das es zurückbringt.

<!-- S65 -->
Und das Komische daran ist,
dass das keine obskuren
Hobbyprojekte sind.

<!-- S66 -->
Es gibt ganze Anwendungen,
deren einzige Aufgabe ist,
Windows mehr wie... zu machen

<!-- S67 -->
nun ja...
wie Windows.

<!-- S68 -->
Sie holen ein älteres Startmenü zurück.
Sie stellen die Taskleiste wieder her.
Sie ändern das Verhalten des Explorers.

<!-- S69 -->
Und manche geben dir mehr Kontrolle
über Windows als Windows selbst.

<!-- S70 -->
Microsoft hat eine enorme Zahl
von Ingenieuren an diesem System.
Und dann sagt jemand außerhalb:
gut.
Ich baue die alte Leiste selbst ein.

<!-- S71 -->
Und jetzt hat sich noch etwas geändert.
Microsoft setzt zunehmend KI ein,
wenn Software geschrieben wird.

<!-- S72 -->
Der eigene Chef hat gesagt,
dass zwanzig bis dreißig Prozent
des Codes in ihren Repositorys
inzwischen von Software geschrieben wird.

<!-- S73 -->
Und das sollte bedeuten:
mehr Produktivität.
Mehr Fehlerbehebungen.
Schnellere Entwicklung.

<!-- S74 -->
Aber es gibt einen klaren Engpass.
Code schreiben kann schneller werden.

<!-- S75 -->
Ein riesiges Altsystem zu testen
wird nicht zwangsläufig schneller.

<!-- S76 -->
Und wenn du Änderungen schneller
produzierst, als du testen kannst,
wie sie mit jahrzehntealtem
Code zusammenspielen...

<!-- S77 -->
produzierst du am Ende vielleicht
einfach schneller Regressionen.

<!-- S78 -->
Und hier ist Vorsicht angebracht.
Diese Zahl gilt für ganz Microsoft,
nicht für Windows im Besonderen.
Und niemand hat gezeigt,
dass KI diese Fehler verursacht hat.

<!-- S79 -->
Vielleicht hat KI Microsoft nicht
schlechter im Testen gemacht.

<!-- S80 -->
Vielleicht hat sie nur das vorhandene
Problem beschleunigt.

<!-- S80b -->
Übrigens: wenn du sehen willst,
wohin der Rest davon führt,
kannst du den Kanal abonnieren.

Das hilft dem Kanal wirklich.

<!-- S81 -->
Der Großteil dieses Videos hat
argumentiert, dass Microsoft ein
echtes Qualitätsproblem hat.
Und dieses Argument hält.

<!-- S82 -->
Doch hier kommt der Teil,
der Leute überrascht.
Warum könnte der Kernel
trotzdem anders sein?

<!-- S83 -->
Denn fast alles,
was bisher beschrieben wurde,
ist nicht der Kernel.

<!-- S84 -->
Der Mauszeiger.
Die Taskleiste.
Das Startmenü.
Die Einstellungen.
Der Wiederherstellungsbildschirm.

<!-- S85 -->
Das alles liegt obendrauf.

<!-- S86 -->
Der Kernel ist der Teil darunter.
Er entscheidet, welches Programm
auf welchem Prozessorkern läuft.
Er teilt Speicher zu.
Er spricht mit der Hardware.

<!-- S87 -->
Und wenn dieser Teil ernsthaft
schiefginge, wäre das Symptom
keine albern aussehende Maus.

<!-- S88 -->
Das Symptom wäre eine Maschine,
die stehen bleibt, Daten beschädigt
oder still jemanden hereinlässt.

<!-- S88b -->
Und der Kernel hat etwas,
was der Rest von Windows nicht hat.
Harte Randbedingungen.

<!-- S88c -->
Ein Scheduler kann nicht beschließen,
sich anders zu verhalten,
weil jemand das Startmenü
neu gezeichnet hat.

<!-- S88d -->
Speicherverwaltung modernisiert man
nicht durch Verschieben einer Fläche.
Und ein Treiber darf nicht annehmen,
dass die Hardware sich brav verhält.

<!-- S88e -->
Und vor allem: der Kernel kann einen
Fehler nicht hinter einer leicht
verwirrenden Einstellungsseite verstecken.

<!-- S88f -->
Das ist ein Grund zu vermuten,
dass es eine ganz andere
technische Geschichte ist
als der Rest von Windows.

<!-- S89 -->
Aber Vermutung ist kein Beleg.
Also sehen wir, was dieses Ding
tatsächlich aushalten musste.

<!-- S90 -->
Die Architektur ganz unten ist alt.
Sehr alt.
Und sie hat überlebt.

<!-- S91 -->
Aus ihr wurde Windows 2000.
Dann XP.
Dann Vista.
Dann 7, 8, 10 und 11.

<!-- S92 -->
Prozessoren änderten sich.
Die Zahl der Kerne explodierte.
Die Speichergrößen explodierten.
Virtuelle Maschinen wurden vom Exoten
zur völligen Normalität.

<!-- S93 -->
Und dieselbe Code-Familie
landete auf Servern
auf der ganzen Welt.

<!-- S94 -->
Dateiserver.
Anmeldungen in Firmennetzen.
Virtuelle Maschinen.
Lasten, die sich niemand vorstellte,
als es entworfen wurde.

<!-- S95 -->
Wäre der Teil, der entscheidet,
was wann läuft,
und der den Speicher zuteilt,
hoffnungslos kaputt...
wären die Folgen nicht zu übersehen.

<!-- S96 -->
Nun ein ehrliches Eingeständnis.
Niemand außerhalb von Microsoft kann
den Quelltext des heutigen Kernels lesen,
also kann ihn niemand schön nennen.

<!-- S96b -->
Auf eine ältere Fassung
hat aber jemand geschaut.

<!-- S96c -->
Ein Teil des Quelltexts von
Windows 2000 gelangte 2004 nach außen,
und letztes Jahr hat ihn
ein Forscher durchgearbeitet.

<!-- S96d -->
Die Funde waren nicht schmeichelhaft.
Fehler, die sechzehn Jahre
in diesem Code saßen,
bevor sie jemand behoben hat.

<!-- S96e -->
Aber das ist der Großvater
des heutigen Kernels,
und nur ein Bruchteil kam heraus.
Es sagt etwas über 2000,
nicht über heute.

<!-- S97 -->
Und überlebt zu haben ist nicht
dasselbe wie ausgezeichnet zu sein.

<!-- S98 -->
Das ist also keine Behauptung,
der Windows-Kernel sei genial.
Das weiß niemand.

<!-- S99 -->
Aber wir haben Jahrzehnte an Belegen,
dass er seine Arbeit macht.

<!-- S100 -->
Und das ist ein viel seltsamerer Schluss
als „Windows ist schlecht“.

<!-- S101 -->
Denn es heißt, die Antwort
auf „was macht deren QA“
lautet vermutlich nicht
„Microsoft kann keine Software schreiben“.

<!-- S102 -->
Sondern: sie haben jahrzehntelang
Neues auf Altes gebaut,
ohne je das Alte
wegwerfen zu dürfen.

<!-- S103 -->
Das Ergebnis ist riesig.
Mächtig.
Kompatibel.
Und gelegentlich lächerlich.

<!-- S104 -->
Du installierst ein Update.
Der Ton verschwindet.
Der Zeiger sieht aus wie Windows 98.

<!-- S105 -->
Und unter alldem entscheidet
etwas ganz leise,
welches Programm als Nächstes läuft.
Teilt Speicher zu.
Spricht mit der Hardware.

<!-- S106 -->
Tut genau das,
was es tun soll.

<!-- S107 -->
Zumindest...
denken wir das.

<!-- S108 -->
Denn anders als die Taskleiste...
sehen wir es nicht.
