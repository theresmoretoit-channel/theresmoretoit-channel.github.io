<!-- S01 -->
948.
So viele verschiedene Wege hat eine KI gefunden,
einen Linux-Rechner von innen zu übernehmen.

<!-- S02 -->
Kein gestohlenes Passwort. Kein Einbruch übers Netz.
Jeder beginnt bei einem normalen Benutzer
ohne besondere Rechte
und endet bei root,
dem Konto, das alles darf.

<!-- S03 -->
OpenAI hat das Ergebnis im November 2026 veröffentlicht.
Der gesamte Lauf kostete
1,2 Millionen Dollar an API-Guthaben.

<!-- S05 -->
Das sind OpenAIs eigene Zahlen,
veröffentlicht am Tag,
bevor die Firma das Modell vorstellte, das sie erzeugt hat,
und von außen hat niemand die Gesamtzahl bestätigt.
Aber Hunderte Meldungen und Patches
sind schon verschickt.

<!-- S06 -->
Das betrifft nicht nur Linux.
Der Quellcode von Linux ist öffentlich.
Jeder kann ihn lesen.
Jahrzehntelang war das das Argument,
warum er sicher ist.

<!-- S07 -->
Wenn eine Maschine also öffentlichen Code lesen
und in diesem Maßstab funktionierende Exploits daraus bauen kann,
sollte Software ihren Code dann doch geheim halten?

<!-- S08 -->
Schauen wir uns Software an, die das schon tut.
Im April 2026 behob Microsoft
164 Sicherheitslücken
an seinem monatlichen Patchday.
Im Oktober waren es
1.413.

<!-- S09 -->
In diesem einen Monat waren es mehr
als je zuvor in einem ganzen Jahr.
Über tausend dieser Korrekturen betrafen Windows,
und Microsoft hatte gewarnt,
dass die eigenen KI-Werkzeuge den Anstieg antreiben würden.

<!-- S10 -->
Direkt vergleichen lassen sich die beiden Zahlen nicht.
Firmen zählen unterschiedlich,
und Microsoft durchsuchte seinen eigenen nichtöffentlichen Code.

<!-- S11 -->
Eines zeigt es aber.
Dass der Code privat blieb,
hat die Fehler nicht ferngehalten.

<!-- S12 -->
Was schützt dich also wirklich?
Um das zu beantworten,
müssen wir uns ansehen, wie diese Maschine arbeitet,
denn jeder ihrer Schritte wirft etwas weg.

<!-- S13 -->
Der Linux-Kernel hat
mehr als 40 Millionen Zeilen Code.
Zuerst gingen Späher-Agenten ihn durch
und suchten die Teile heraus,
an die ein normaler Benutzer wirklich herankommt.

<!-- S14 -->
Übrig blieben etwa sieben Prozent.
Das ist der Teil, bei dem sich ein Angriff ihrer Einschätzung nach lohnte,
keine Zufallsstichprobe,
also kannst du das Ergebnis nicht mal vierzehn nehmen.

<!-- S15 -->
Dann gingen Analyse-Agenten diesen Code durch
und listeten alles Verdächtige auf.
2.308 Kandidaten,
in zwölf Stunden.

<!-- S16 -->
Aber ein Verdacht beweist nichts.
Also schrieben andere Agenten Testprogramme
und ließen sie auf isolierten virtuellen Maschinen laufen.
1.724 Fehler
erwiesen sich als echt.

<!-- S17 -->
Dann kam der teure Teil:
funktionierende Exploits bauen,
mit eingeschalteten Standardschutzmechanismen
eines normalen Desktop-Systems.
1.169 davon
kamen bis root.

<!-- S18 -->
Gruppiere sie nach dem zugrunde liegenden Fehler,
und du erhältst die 948.

<!-- S19 -->
Ein Detail im Bericht
vergisst man nicht so leicht.
In einem frühen Lauf
meldeten die Agenten 200 Erfolge.
Dann prüften Menschen, wie sie dorthin gekommen waren.

<!-- S20 -->
Zwanzig von ihnen waren root geworden
über einen anderen, unbekannten Fehler,
nicht über den, den sie nutzen sollten.
Geschickt, um eine Tür zu öffnen,
fanden sie eine andere, von der niemand wusste.

<!-- S21 -->
In einer Stichprobe seiner Exploits
benannte OpenAI zehn Exploit-Techniken,
die externe Fachleute noch nicht gesehen hatten.

<!-- S22 -->
Im Juli fand ein älteres Modell
166 solcher Fehler.
Drei Monate voller Korrekturen später
fand das neuere Modell 948.
Die Fehler waren nicht ausgegangen.
Der spätere Lauf fand weit mehr.

<!-- S23 -->
Es gibt allerdings eine wichtige Grenze.
Mit diesen Exploits kommt niemand
übers Internet in deinen Rechner.
Der Angreifer muss schon auf der Maschine sein,
als normaler Benutzer.

<!-- S24 -->
Das beruhigt weniger, als es klingt,
denn echte Angriffe laufen oft in zwei Schritten ab.
Erst kommst du hinein,
über eine Browser-Lücke oder einen schädlichen Download.
Dann brauchst du root.
Das hier ist der zweite Schritt.

<!-- S25 -->
OpenAIs Rat ist unverblümt.
Auf einem System ohne die neuesten Patches
behandle jedes normale Konto wie root,
zumindest gegenüber einem finanzstarken Angreifer.

<!-- S26 -->
Wo bleibt also
das alte Argument für offenen Code?
In den späten Neunzigern
gab ihm Eric Raymond einen Slogan:
„Wenn genug Leute hinschauen, lässt sich jeder Fehler leicht aufspüren.“

<!-- S27 -->
Er nannte es Linus' Gesetz.
Eine schöne Idee, die aber voraussetzt,
dass tatsächlich jemand hinschaut.

<!-- S28 -->
2014 tauchte ein Fehler namens Heartbleed
in OpenSSL auf,
dem Code, der einen riesigen Teil des Webs schützte.
Etwa eine halbe Million sicherer Server
galten als gefährdet.

<!-- S29 -->
Der Fehler hatte zwei Jahre in öffentlichem Code gelegen.
Das Projekt bekam
etwa zweitausend Dollar Spenden im Jahr
und hatte einen einzigen Vollzeitentwickler.

<!-- S30 -->
Jeder hätte ihn lesen können.
Kaum jemand tat es.

<!-- S31 -->
Das war immer die wahre Schwäche von Open Source.
Nicht zu viele Augen auf dem Code. Zu wenige.

<!-- S32 -->
Und genau das ändert die KI.
Eine Maschine kann immer weiter scannen,
und weit mehr Kandidaten prüfen,
als ein menschlicher Forscher allein schaffen würde.
Das alte Versprechen wird endlich eingelöst,
für alle, Angreifer inklusive.

<!-- S33 -->
Öffentlicher Code wird jetzt also wirklich untersucht.
Hilft es, ihn zu verstecken?

<!-- S34 -->
Ein geschlossenes Programm muss trotzdem laufen,
also liegt sein Maschinencode
auf jedem Rechner, der es benutzt.
Werkzeuge wie Ghidra machen daraus wieder
etwas wie Quellcode.

<!-- S35 -->
Und es gibt einen klassischen Trick.
Vergleiche ein Programm
vor und nach einem Sicherheitsupdate.
Was sich geändert hat, zeigt dir, wo das Loch war.

<!-- S35b -->
Das verrät Angreifern, wohin sie zielen müssen,
lange bevor jedes System
das Update installiert hat.

<!-- S36 -->
Anthropic hat das am Windows-Kernel versucht,
mit 21 Lücken,
die Microsoft kürzlich geschlossen hatte,
und ohne Quellcode.
Den ersten Absturz schaffte die KI in 31 Minuten.
Innerhalb von sechs Stunden hatte sie 18.

<!-- S37 -->
Acht wurden zu funktionierenden Exploits,
mit denen sich der Rechner vollständig übernehmen ließ,
für jeweils rund zweitausend Dollar.

<!-- S38 -->
Aber das waren keine unbekannten Fehler.
Die Patches zeigten schon,
wo die Probleme lagen.
Eine neue Lücke ganz ohne Hinweis zu finden, ist schwerer.

<!-- S39 -->
Geheimhaltung kostet einen Angreifer also weiterhin etwas.
Sie ist eine Bremsschwelle, keine Mauer.
Wie hoch ist die Schwelle?
Eine öffentliche Zahl gibt es nicht.

<!-- S40 -->
Und die andere Seite?
Was bringt dir Offenheit eigentlich?
Die Antwort steckt in einem kleinen Detail
von OpenAIs Bericht.

<!-- S41 -->
In den zehn Tagen dieses Scans und der Analyse
wurden über hundert dieser Linux-Lücken
behoben oder standen kurz davor,
und zwar von anderen Leuten.
Über etwa dreihundert weitere
wurde schon öffentlich diskutiert.

<!-- S42 -->
Andere fanden dieselben Fehler
zur selben Zeit.

<!-- S43 -->
Linus Torvalds hatte das schon im Mai beschrieben.
Er sagte, KI-Meldungen
hätten die Sicherheits-Mailingliste des Kernels
„fast völlig unbeherrschbar“ gemacht,
weil verschiedene Leute immer wieder
dasselbe mit denselben Werkzeugen fanden.

<!-- S44 -->
Und sein Rat lautete:
„Wenn du einen Fehler mit KI-Werkzeugen gefunden hast,
stehen die Chancen gut, dass ihn auch jemand anders gefunden hat.“

<!-- S45 -->
Die Kernel-Regeln sagen es jetzt ganz offen.
Ein mit KI gefundener Fehler gilt als öffentlich,
weil solche Fehler
bei mehreren Forschenden auftauchen,
oft am selben Tag.

<!-- S46 -->
Überleg mal, was das
mit der Idee eines geheimen Fehlers macht.
Wenn er für dich billig zu finden war,
war er es für alle.

<!-- S47 -->
Bei Open Source
kann jeder die Meldung einsehen,
die Korrektur prüfen und das Ergebnis anfechten.
Bei geschlossener Software
musst du meist dem Hersteller vertrauen.

<!-- S49 -->
Aber Offenheit hat ihren Preis,
und es ist nicht der, den du erwartest.
Man möchte sagen,
ein kleines Projekt könne sich das Scannen nicht leisten.
KI-Firmen bieten den Maintainern
aber schon kostenlosen Zugang an.

<!-- S50 -->
Was fehlt, sind Menschen.
Der Kernel verzeichnete früher
etwa 500 Sicherheitsprobleme pro Release.
Dieses Jahr waren es über 1.500.
Viele sind weniger schwerwiegend,
aber jemand muss sie trotzdem durchgehen.

<!-- S51 -->
Im Januar stellte das curl-Projekt
sein bezahltes Bug-Bounty-Programm ein,
um eine Flut wertloser Meldungen nicht mehr zu belohnen.

<!-- S52 -->
Selbst gute Meldungen schieben die Arbeit nur weiter.
KI-Patches brauchen weiterhin menschliche Prüfung.
Manche frühen Korrekturen fügten unnötigen Code hinzu
oder übersahen andere Varianten desselben Fehlers.

<!-- S53 -->
Mehr Scannen kannst du kaufen.
Mehr Leute, die ein Stück Code
so gut verstehen, kannst du nicht kaufen.
Hier hat eine Firma mit bezahltem Sicherheitsteam
wirklich einen Vorteil.

<!-- S54 -->
Und dann kommt das letzte Problem.
Behoben heißt nicht installiert.

<!-- S55 -->
Im März 2017
schloss Microsoft eine Lücke in Windows.
Geschlossener Code, ein Hersteller, ein Update-System.
Zwei Monate später
ging WannaCry durch genau dieses Loch,
in rund zweihunderttausend Rechner
in etwa hundertfünfzig Ländern.

<!-- S56 -->
Dieser Patch hatte zwei Monate Zeit, sich zu verbreiten,
und das reichte nicht.
Zwei Monate lässt dir ein Angreifer heute vielleicht nicht mehr.
In derselben Anthropic-Studie
nahm die KI eine öffentliche Korrektur
für die JavaScript-Engine von Firefox
und hatte in unter einer Stunde einen funktionierenden Exploit.

<!-- S57 -->
Bis zur korrigierten Firefox-Version
dauerte es noch achtzehn Tage.

<!-- S58 -->
Das ist die Gefahr beim Veröffentlichen einer Korrektur.
Die Information kann Angreifer erreichen,
bevor das Update dich erreicht.

<!-- S59 -->
Eine Linux-Korrektur hat einen langen Weg vor sich,
vom Kernel in ein stabiles Release,
in deine Distribution, auf dein Gerät.
Ein Handy wartet vielleicht Monate, oder ewig.

<!-- S60 -->
Und geschlossene Software entkommt dem nicht.
Wir haben es gerade gesehen: Der Windows-Patch reichte.
Jedes Update ist jetzt auch eine Landkarte.

<!-- S60b -->
Halte also alles auf dem neuesten Stand,
deinen Computer, dein Handy, sogar deinen Router,
und installiere Updates, sobald sie erscheinen.
Je besser KI darin wird, aus Korrekturen Angriffe zu machen,
desto mehr zählt jeder Tag, den du wartest.

<!-- S61 -->
Ist Open Source also noch sicherer?
Ehrlich gesagt, das weiß niemand.
Soweit öffentlich bekannt,
hat niemand denselben Test auf beiden Seiten laufen lassen,
unter denselben Regeln.

<!-- S62 -->
Was wir sagen können, ist bescheidener.
Code zu verstecken bringt weniger als früher.
Ihn zu zeigen lässt jeden die Arbeit prüfen
und lädt einen größeren Berg dieser Arbeit
bei denen ab, die ihn pflegen.

<!-- S64 -->
Selbst wenn KI nie jeden Fehler findet,
hat sie die Ökonomie der Suche schon verändert.

<!-- S65 -->
Entscheidend ist jetzt, wie lange ein Loch offen bleibt,
zwischen dem Moment, in dem es jemand findet,
und dem Moment, in dem es auf deinem Rechner geschlossen ist.

<!-- S66 -->
Also eine Frage an dich.
Wenn jeder jeden Fehler finden kann,
würdest du lieber Code vertrauen, den du lesen kannst,
oder einer Firma, die dafür bezahlt wird, ihn zu beheben?
Schreib es in die Kommentare.
