<!-- S01 -->
Neunhundertneunundneunzig Pfund
und neunundneunzig Pence.
Rechne einen Penny dazu.

<!-- S02 -->
Das Ergebnis ist null.

<!-- S03 -->
Keine Fehlermeldung. Kein Absturz.
Nur eine Null, still ins Konto geschrieben.

<!-- S04 -->
Wenn in COBOL das Feld für ein Ergebnis
zu klein ist, um es aufzunehmen,
kann die überzählige Ziffer einfach verschwinden.
Solange das Programm keine Warnung anfordert,
läuft die Rechnung weiter.

<!-- S05 -->
Und es rundet auch nicht.
Zwei Pfund und vierunddreißigeinhalb Pence,
auf den Penny genau gespeichert,
werden zu zwei Pfund vierunddreißig.

<!-- S06 -->
Schreib ein Wort mehr dazu, ROUNDED,
und es werden zwei Pfund fünfunddreißig.

<!-- S07 -->
Nichts davon ist ein Bug.
Das sind Regeln.
Und viele Banken auf der Welt
laufen immer noch mit solchen Regeln.

<!-- S08 -->
COBOL ist eine Programmiersprache
von 1959.
Nicht jedes Programm darin ist so alt.
Aber die Sprache schon,
und ihre Gewohnheiten auch.

<!-- S09 -->
Warum haben die Banken sie dann nicht ersetzt?
Geld haben sie.
Ingenieure auch.

<!-- S10 -->
Dazu schauen wir uns drei echte Fälle an.
Eine Bank, die ihr altes System verlassen wollte,
eine, der das gelungen ist,
und eine Krise, in der alle COBOL die Schuld gaben.

<!-- S11 -->
Aber zuerst zu dem fehlenden halben Penny.

<!-- S12 -->
Angenommen, du schreibst dieses Bankprogramm
in einer modernen Sprache neu.
Diese Regeln würdest du wohl korrigieren.
Ein Überlauf wird zum Fehler.
Ein halber Penny wird aufgerundet.

<!-- S13 -->
Sauberer. Sicherer.
Und überall, wo ein halber Penny auftaucht,
weicht dein Programm jetzt vom alten ab.

<!-- S14 -->
Moderne Sprachen können exakt dezimal rechnen.
Java hat dafür einen eigenen Typ.
Aber selbst dort
ist die Rundungsregel eine Entscheidung.

<!-- S15 -->
Eine gängige Einstellung rundet bei genau der Hälfte auf:
zwei Pfund fünfunddreißig.
Eine andere rundet zur nächsten geraden Ziffer:
zwei Pfund vierunddreißig.
Beides ist richtig. Nur eins stimmt überein.

<!-- S16 -->
Und mit gewöhnlichen Gleitkommazahlen,
wie sie der meiste Code standardmäßig nutzt,
wird es noch seltsamer.
Null Komma eins plus null Komma zwei
ist nicht null Komma drei.

<!-- S17 -->
COBOL zu ersetzen ist also keine Übersetzung.
Man muss jede solche Regel finden,
in Millionen von Zeilen,
und jede genau so erhalten, wie sie war.

<!-- S18 -->
Wie kam COBOL überhaupt dorthin?

<!-- S19 -->
Im Mai 1959
berief das US-Verteidigungsministerium
ein Treffen im Pentagon ein.
Computerhersteller, Behörden
und große Unternehmen kamen,
alle mit demselben Problem.

<!-- S20 -->
Jeder Computer hatte seine eigene Sprache.
Ein Lohnprogramm, geschrieben für eine Maschine,
war auf einer anderen nutzlos.

<!-- S21 -->
Ein Komitee entwarf eine gemeinsame Sprache
für die Wirtschaft.
Den größten Einfluss hatte FLOW-MATIC
von Grace Hoppers Team bei Remington Rand.

<!-- S22 -->
Und im Dezember 1960
lief im Wesentlichen dasselbe COBOL-Programm
auf zwei Computern
konkurrierender Hersteller.
Genau darum ging es.

<!-- S23 -->
Die Sprache sollte für Menschen lesbar sein.
ADD PAYMENT TO ACCOUNT-BALANCE.
Was das tut, kannst du dir wohl denken.

<!-- S24 -->
Und sie speicherte Geld so, wie Menschen es schreiben:
als Dezimalziffern.
Das Dezimalkomma
muss nicht einmal gespeichert werden.
Wo es hingehört, steht in der Beschreibung des Feldes:
Die letzten beiden Ziffern sind Pence.

<!-- S25 -->
1964 brachte IBM das System/360 heraus.
Sein Design enthielt Befehle
für Dezimalarithmetik.

<!-- S26 -->
Und seitdem baut IBM seine Großrechner
so, dass sie kompatibel bleiben.
Viele ältere Programme können noch
auf heutigen Maschinen laufen,
ohne neu geschrieben zu werden.

<!-- S27 -->
Es gab also selten einen Moment,
der jemanden zum Umstieg zwang.
Jedes Jahr lief der Code weiter,
und jedes Jahr sammelte er mehr Regeln an.
Neue Produkte, neue Steuern, neue Vorschriften,
neue Ausnahmen.

<!-- S28 -->
Niemand hat gezählt, wie viel COBOL
weltweit noch läuft.
Aber laut IBM nutzen fünfundvierzig
der fünfzig größten Banken der Welt
noch immer Großrechner von IBM.

<!-- S29 -->
Und manche Betreiber haben nachgezählt.
2017 erklärte die US-Sozialversicherung,
ihre Systeme enthielten
über sechzig Millionen Zeilen COBOL.

<!-- S30 -->
2025 listeten Prüfer der US-Regierung
die elf Bundessysteme auf,
die am dringendsten ersetzt werden müssen.

<!-- S31 -->
Sie waren zwischen dreiundzwanzig
und sechzig Jahre alt,
und ihr Betrieb kostete rund siebenhundertfünfzig
Millionen Dollar pro Jahr.

<!-- S32 -->
Der Code ist also alt, er ist überall,
und voller Regeln, die nie jemand aufgeschrieben hat.
Dann ist es doch gefährlich, ihn zu behalten.

<!-- S33 -->
Schauen wir, was passiert,
wenn eine Bank aussteigt.

<!-- S34 -->
2018 hatte eine britische Bank namens TSB
rund fünf Millionen Kunden
und ein Problem.

<!-- S35 -->
Ihre Systeme waren gemietet,
von der Lloyds Banking Group,
einem Konkurrenten,
und die Gebühren sollten kräftig steigen.

<!-- S36 -->
Also beschloss TSB, alles umzuziehen,
auf eine neue Plattform,
gebaut von ihrem neuen Eigentümer,
der spanischen Bank Sabadell.

<!-- S37 -->
Ein Wochenende im April.
Am Sonntagabend
wurde das neue System eingeschaltet.

<!-- S38 -->
Am Montag gab es rund
neunhunderttausend Anmeldeversuche.
Nur etwa jede zehnte Anmeldung
im Onlinebanking gelang.

<!-- S39 -->
Zahlungen schlugen fehl.
Manche Kunden meldeten sich an
und sahen fremde Konten.

<!-- S40 -->
Das Schlimmste dauerte etwa eine Woche.
Zum Normalbetrieb kehrte TSB erst
im Dezember zurück.

<!-- S41 -->
Die Folgen kosteten rund
dreihundertdreißig Millionen Pfund,
allein im Jahr 2018.
Später verhängten die Aufsichtsbehörden
noch Bußgelder von fast neunundvierzig Millionen.

<!-- S42 -->
Und jetzt kommt das Seltsame.
Die Kundendaten kamen unversehrt an.
Das sagen beide offiziellen Berichte.

<!-- S43 -->
Versagt hat die neue Plattform drumherum.
Zwei Rechenzentren, unterschiedlich eingerichtet.
Die Leistung nur in einem davon getestet,
und die Zielwerte gesenkt,
als die Tests nicht bestanden wurden.

<!-- S44 -->
Und es gab kein Zurück.
Sobald die Daten umgezogen waren,
war eine Rückkehr zum alten System,
in den Worten der Aufsicht,
„im Grunde unmöglich“.

<!-- S45 -->
TSB floh nicht vor einem kaputten System.
Sie verließ eines, das funktionierte,
wegen der Frage, wem es gehörte
und was es kostete.
Gefährlich war der Ausstieg.

<!-- S46 -->
Ist ein Ausstieg also immer eine Katastrophe?

<!-- S47 -->
2008 machte sich Australiens Commonwealth Bank
daran, ihre Kernsysteme zu ersetzen,
die ihr
über fünfundvierzig Jahre lang gedient hatten.

<!-- S48 -->
Der Plan: rund fünfhundertachtzig
Millionen australische Dollar
und vier Jahre.

<!-- S49 -->
Es dauerte fünf.
Presseberichte bezifferten die Summe später
auf etwa eins Komma eins Milliarden,
weil das Projekt immer größer wurde.

<!-- S50 -->
Aber sie zog nicht alles
an einem Wochenende um.
Zuerst kamen 2010 die Einlagenkonten.
Geschäftskonten folgten 2011
und Kredite 2012.

<!-- S51 -->
Jeder Schritt war etwas, das die Bank
beobachten, prüfen und auswerten konnte,
bevor sie auf den nächsten setzte.

<!-- S52 -->
Am Ende wurde sie, so die Bank,
die erste große australische Bank
mit Echtzeit-Banking,
rund um die Uhr.

<!-- S53 -->
Es geht also.
Aber sieh dir an, was es gekostet hat.
Fünf Jahre, eine viel höhere Rechnung
und Geduld.

<!-- S54 -->
Modernisierung ist kein Kauf.
Sie ist ein Projekt,
mit ganz eigenen Risiken.

<!-- S55 -->
Und nun zu der Krise,
an der alle COBOL die Schuld gaben.

<!-- S56 -->
März 2020.
Als die Pandemie New Jersey lahmlegte,
stiegen die Erstanträge auf Arbeitslosengeld
von unter zehntausend pro Woche
auf über hundertfünfundfünfzigtausend.

<!-- S57 -->
Sechzehnmal so viele,
in sieben Tagen.
Das Arbeitsamt kam nicht hinterher.

<!-- S58 -->
Anfang April bat der Gouverneur
um Freiwillige.
Nicht nur um Gesundheitspersonal,
sondern auch um Leute, die COBOL konnten.
Die Systeme des Bundesstaats, sagte er,
seien über vierzig Jahre alt.

<!-- S59 -->
Die Geschichte verbreitete sich schnell.
Uralter Code sei unter der Last
der Pandemie zusammengebrochen.

<!-- S60 -->
Doch als der staatliche Rechnungsprüfer
das später untersuchte,
fand er keinen Beleg dafür,
dass die Verzögerungen
an den Computersystemen lagen.

<!-- S61 -->
Unabhängig davon prüften Reporter
die Fehlermeldungen, die die Leute sahen,
und führten viele auf die vorgeschaltete Website zurück,
geschrieben in einer viel neueren Sprache, Java.
Der alte Code dahinter lief weiter.

<!-- S62 -->
Warum brauchte der Staat dann COBOL-Programmierer?
Weil der Kongress die Regeln änderte.
Neue Leistungen, neue Beträge,
neue Menschen mit Anspruch,
und jede Änderung musste
in den Code, und zwar schnell.

<!-- S63 -->
Das Problem war nicht, dass der Code alt war.
Sondern dass ihn nur wenige ändern konnten
und dass Telefone und Personal
ebenfalls überlastet waren.

<!-- S64 -->
Drei Fälle.
Eine Bank, die ein System verließ, das noch lief,
und deren Migration scheiterte.
Eine Bank, die vorsichtig ausstieg
und Erfolg hatte.
Und eine Krise, die man dem alten Code anlastete,
obwohl keiner zeigen konnte, dass er schuld war.

<!-- S65 -->
Das heißt nicht, dass alte Systeme nie versagen.
Das tun sie.
Sie werden teuer,
die Leute, die sie verstehen, gehen in Rente,
und auch das Warten hat seinen Preis.

<!-- S66 -->
Aber das Alter sieht man leicht,
die echten Risiken nicht.
Regeln, die nie jemand aufgeschrieben hat.
Wissen in den Köpfen weniger Leute.
Und der Moment der Umstellung.

<!-- S67 -->
Deshalb ersetzen viele Banken
den alten Kern nicht auf einen Schlag.
Sie bauen eine Hülle darum.
Die App auf deinem Handy ist neu,
aber vielleicht spricht sie mit etwas
viel Älterem.

<!-- S68 -->
Und sie ersetzen ihn Stück für Stück.
2004 benannte der IT-Autor Martin Fowler
dieses Vorgehen nach der Würgefeige,
einer Regenwaldpflanze, die einen Baum umwächst,
bis sie allein stehen kann.

<!-- S69 -->
Das alte System arbeitet weiter,
während das neue um es herum wächst,
eine Aufgabe nach der anderen,
bis nichts mehr vom alten abhängt.

<!-- S70 -->
Damit sind wir wieder beim halben Penny.
Irgendwo verwirft ihn vielleicht noch ein Programm,
weil jemand das so entschieden hat,
vor Jahrzehnten.
Wer dieses Programm ersetzt, muss das wissen,
und alles andere dieser Art.

<!-- S71 -->
Das alte System ist nicht unbedingt
das, was versagt.
Manchmal ist es das, was an seine Stelle tritt.

<!-- S72 -->
Denn die Technik zu ersetzen
ist nicht dasselbe, wie das Risiko zu beseitigen.
Manchmal verschiebt es das Risiko nur
auf ein einziges Wochenende im April.

<!-- S73 -->
Also, hier eine Frage an dich.
Wenn ein System seit vierzig Jahren funktioniert,
wann ist der richtige Zeitpunkt, es zu ersetzen?
Und musstest du selbst schon mal eins ersetzen?
Schreib es mir in die Kommentare.
