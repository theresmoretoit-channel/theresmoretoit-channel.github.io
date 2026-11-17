<!-- S01 -->
Da qualche parte in casa tua
potrebbe esserci un orologio
che nessuno ha mai regolato.

<!-- S02 -->
Sopravvive ai blackout.
Passa all'ora legale e torna indietro
da solo, nel cuore della notte.

<!-- S03 -->
Non ha nessuna connessione a internet.
Niente Wi-Fi, niente GPS,
nessuna app sul telefono.

<!-- S04 -->
Ha solo un minuscolo ricevitore radio.
E una volta al secondo
sente un singolo impulso.

<!-- S05 -->
Quindi come fa un orologio
a trasformare un impulso al secondo
nell'ora esatta, nella data
e perfino nel giorno della settimana?

<!-- S06 -->
In Europa quegli impulsi arrivano
da DCF77, vicino a Francoforte.
In America da WWVB, in Colorado.
Trasmettitori diversi, stessa idea.

<!-- S07 -->
Prendiamo quello tedesco.
Trasmette un'onda radio costante,
giorno e notte.
E all'inizio di ogni secondo
abbassa per un attimo quell'onda.

<!-- S08 -->
Il trucco è quanto a lungo
resta abbassata.

<!-- S09 -->
Un calo di un decimo di secondo
significa zero.
Un calo di due decimi significa uno.

<!-- S10 -->
Tutto qui.
Niente pacchetti, niente rete.
Solo un'onda radio che cala
per poco tempo, o un po' più a lungo.

<!-- S11 -->
Un bit ogni secondo.
Il che significa che servirebbe un minuto intero
per mandare appena 60 bit.

<!-- S12 -->
E in realtà ne manda solo 59.

<!-- S13 -->
Nell'ultimo secondo di ogni minuto
l'onda non cala affatto.
E proprio quel calo mancante
è la parte più importante
di tutto il segnale.

<!-- S14 -->
Perché quando arriva il calo successivo,
l'orologio sa
che è appena iniziato un nuovo minuto.

<!-- S15 -->
Il vuoto funziona come un punto.
Tutto ciò che sta tra due vuoti
è una frase completa.

<!-- S16 -->
Allora, che cosa ci sta in una frase
di 59 bit?

<!-- S17 -->
Il minuto. L'ora.
Il giorno del mese, il giorno della settimana,
il mese e l'anno.

<!-- S18 -->
La maggior parte dei numeri viene inviata cifra per cifra.
47 minuti
non vengono inviati come 47.
Vengono inviati come due cifre separate,
un 4 e un 7.

<!-- S19 -->
4 bit bastano per qualsiasi cifra
da 0 a 9.
Le decine di minuti non superano mai il 5,
quindi ne ricevono solo 3.

<!-- S20 -->
E l'anno riceve solo due cifre.
Per il trasmettitore
il 2026 è semplicemente 26.
Il secolo lo aggiunge l'orologio da solo.

<!-- S21 -->
Ma la radio non è un canale pulito.
Un motore, un caricabatterie del telefono,
una lampadina LED economica...
ognuno di questi può alterare un calo.

<!-- S22 -->
Così, dopo ogni blocco di numeri,
arriva un bit in più, chiamato bit di parità.

<!-- S23 -->
Viene scelto in modo che il numero di 1
nel blocco risulti sempre pari.

<!-- S24 -->
Se un'interferenza inverte un singolo bit,
il conteggio diventa dispari
e l'orologio sa
che qualcosa è andato storto.

<!-- S25 -->
Ma se si invertono due bit,
il conteggio torna pari
e l'errore passa inosservato.

<!-- S26 -->
Ecco perché molti orologi
non si fidano di un solo minuto.
Ne aspettano un altro valido.

<!-- S27 -->
Ed ecco perché regolarsi da solo
può richiedere diversi minuti,
e in una giornata storta molto di più.

<!-- S28 -->
Il che crea uno strano problema.

<!-- S29 -->
L'orologio passa un minuto intero
a raccogliere l'ora delle 10:48.
Ma mentre raccoglie quel messaggio,
sono ancora le 10:47.

<!-- S30 -->
Quindi quando cambia davvero?

<!-- S31 -->
Perché il messaggio è un annuncio.
Dice che ore saranno
quando inizierà il minuto successivo.

<!-- S32 -->
L'orologio legge tutta la frase,
aspetta che passi il calo mancante,
e quando arriva il calo successivo,
quel calo è l'istante esatto.

<!-- S33 -->
I bit dicono all'orologio che ore sono.
Il calo gli dice quando.

<!-- S34 -->
Ma la frase contiene qualche parola in più
oltre all'ora.

<!-- S35 -->
Due bit dicono se in Germania
c'è l'ora solare o l'ora legale.

<!-- S36 -->
E un terzo è un avviso.
Per un'ora intera prima del cambio dell'ora,
è impostato a 1.

<!-- S37 -->
Quindi il tuo orologio non deve sapere
in quale domenica di marzo
si spostano avanti le lancette,
o in quale domenica di ottobre si spostano indietro.
Nessuno gli ha mai insegnato la regola.
Gli viene semplicemente detto, con un'ora di anticipo.

<!-- S38 -->
Se un giorno l'Europa smetterà di cambiare l'ora,
l'avviso semplicemente non arriverà mai più.

<!-- S39 -->
Un altro bit avvisava di un secondo intercalare,
un secondo in più aggiunto ogni tanto,
perché la rotazione della Terra
non scandisce il tempo alla perfezione.
Quel minuto poteva avere 61 secondi.

<!-- S40 -->
L'ultimo è stato aggiunto
alla fine del 2016.
Ma a ottobre 2026
le autorità mondiali della metrologia
hanno deciso di abolire i secondi intercalari.
Dal 20 maggio 2027
l'UTC scorrerà senza interruzioni.

<!-- S41 -->
E i primi 14 bit
di ogni minuto
non riguardano affatto l'ora.

<!-- S42 -->
Dal 2006 vengono usati anche
per trasmettere previsioni meteo cifrate
alle stazioni meteo compatibili.

<!-- S43 -->
Quindi il segnale che regola la tua sveglia
poteva anche dire
alla stazione meteo di qualcun altro
se giovedì avrebbe piovuto.

<!-- S44 -->
Eppure la maggior parte di questi orologi
non ascolta sempre.
Ascoltare consuma batteria,
quindi molti ci provano una volta per notte,
nelle prime ore del mattino.

<!-- S45 -->
Le onde lunghe raggiungono un orologio per due vie:
lungo il terreno
e rimbalzando sull'alta atmosfera.
Quando fa buio, quella via in alto cambia
e il segnale spesso arriva più lontano.

<!-- S46 -->
E alle tre del mattino,
di solito ci sono meno macchine, caricabatterie e luci
accesi nei dintorni a coprirlo.

<!-- S47 -->
Tra un controllo e l'altro,
l'orologio va con un cristallo di quarzo,
che può sgarrare di circa un secondo al giorno.

<!-- S48 -->
Al successivo controllo riuscito,
la radio corregge quello scarto.

<!-- S49 -->
Conta perfino dove ascolta.
L'antenna è una piccola barretta di ferrite
avvolta da un filo.

<!-- S50 -->
Sente meglio quando la barretta è di traverso
rispetto alla direzione del trasmettitore,
non quando punta verso di esso.
Gira l'orologio
e un segnale debole può sparire del tutto.

<!-- S51 -->
Ecco perché un orologio funziona su una mensola,
mentre lo stesso orologio, due metri più in là,
dietro un muro di cemento armato, non si regola mai.

<!-- S52 -->
Ma da dove prende l'ora
il trasmettitore?

<!-- S53 -->
Dal PTB,
l'istituto nazionale di metrologia tedesco,
che gestisce orologi atomici.

<!-- S54 -->
Il secondo stesso è definito
dagli atomi di cesio.
Un secondo corrisponde esattamente
a 9.192.631.770 oscillazioni
della radiazione che emettono.

<!-- S55 -->
Quindi una sveglia economica sul comodino
segue, letteralmente,
uno standard di tempo
definito dagli atomi di cesio.

<!-- S56 -->
Non alla perfezione, però.
Il segnale viaggia alla velocità della luce,
e ci mette comunque circa 3 millisecondi
ogni 1.000 chilometri.

<!-- S57 -->
Il ricevitore aggiunge un ritardo suo,
e il tuo orologio non corregge niente di tutto questo.
Non ne ha bisogno.
Mostra solo i secondi.

<!-- S58 -->
Da un unico sito vicino a Francoforte,
il segnale raggiunge orologi
fino a circa 2.000 chilometri di distanza.
È gran parte dell'Europa.

<!-- S59 -->
La Svizzera aveva un trasmettitore suo,
chiamato HBG, fino alla fine del 2011.
Le antenne andavano sostituite,
lo usava troppo poca gente,
e gli orologi svizzeri potevano semplicemente
ascoltare la Germania.

<!-- S60 -->
Altri hanno tenuto il loro.
Regno Unito, Francia, Giappone e Cina
ne hanno tutti uno proprio.

<!-- S61 -->
E in Nord America WWVB
trasmette da Fort Collins dal 1963,
con un codice orario dal 1965.

<!-- S62 -->
Stesso principio, dialetto diverso.
Uno zero è un calo di due decimi di secondo.
Un 1 dura mezzo secondo.

<!-- S63 -->
E invece di un vuoto al minuto,
ogni 10 secondi arriva un segnale più lungo,
come le virgole nella frase.
Due di fila indicano un nuovo minuto.

<!-- S64 -->
La differenza più grande
è quale ora trasmette.
La Germania trasmette l'ora civile dell'Europa centrale,
condivisa da gran parte del continente.

<!-- S65 -->
Ma gli Stati Uniti
si estendono su diversi fusi orari.
Così WWVB trasmette il tempo universale, l'UTC,
e sei tu a dire all'orologio dove ti trovi.

<!-- S66 -->
Non trasmette nemmeno il mese.
Solo il giorno dell'anno,
da 1 a 366.

<!-- S67 -->
Nessuna di queste stazioni
parla la stessa lingua.
Un orologio costruito per la Germania
non capisce niente del Colorado.

<!-- S68 -->
Ma su entrambe le sponde dell'Atlantico
è la stessa routine silenziosa.
Notte dopo notte, un piccolo ricevitore
si allinea a uno standard di tempo atomico
a centinaia o migliaia di chilometri di distanza.

<!-- S69 -->
Allora, una domanda per te.
Se tutti i segnali orari radio
sparissero stanotte,
te ne accorgeresti almeno?
Fammelo sapere nei commenti.
