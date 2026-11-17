# Internet Explorer 6 — I bug che avevano un nome

<!-- S01 -->
Questa è la seconda parte.

Se non hai visto la prima,
il link è qui sotto.

Il riassunto te lo do lo stesso.

<!-- S02 -->
Nel 2001
Microsoft rilasciò
Internet Explorer 6,
e arrivò con Windows XP.

Nel giro di un paio d'anni
aveva più del novanta per cento
del mercato dei browser.

<!-- S03 -->
Microsoft usò quella posizione
per trasformare il browser
in una piattaforma applicativa.

Era un'idea vera.

Solo che a pagarla
furono gli sviluppatori web.

<!-- S04 -->
Quella era la prima parte.

Ma ho lasciato fuori qualcosa.

Ho lasciato fuori la parte
in cui i bug avevano un nome.

<!-- S05 -->
Un bug di un browser normalmente
è un numero in un tracker.

Issue 4172.

Nessuno se lo ricorda.

Nessuno ne parla a pranzo.

<!-- S06 -->
In Internet Explorer 6
i bug avevano nomi propri.

E si scopre che è
la cosa più rivelatrice
di tutta quell'epoca.

<!-- S07 -->
Partiamo da uno leggero.

Fai fluttuare un'immagine a sinistra
e le metti un paragrafo accanto.

Il testo dovrebbe stare
appiccicato all'immagine.

Invece sta
a tre pixel di distanza.

<!-- S08 -->
Non quattro.

<!-- S08b -->
Non due.

<!-- S08c -->
Tre.

<!-- S08d -->
Ogni volta.

Aveva un nome.

The Three Pixel Jog.

<!-- S09 -->
Ora fai fluttuare quell'immagine a sinistra
e dalle un margine sinistro
di dieci pixel.

Internet Explorer 6
gliene dà venti.

Raddoppia il margine,
ma solo dal lato
verso cui l'hai fatta fluttuare.

<!-- S10 -->
The Double Margin Bug.

E la correzione accettata
era dichiarare
un elemento flottante come inline.

<!-- S11 -->
Il che non ha senso.

Un flottante è un blocco.

Chiamarlo inline
non significa proprio niente.

Funzionava, quindi lo si scriveva.

<!-- S12 -->
Il prossimo è migliore.

Carichi una pagina,
e una parte del contenuto
semplicemente non c'è.

Scorri in basso.

Torni su.

Ed eccola.

<!-- S13 -->
Non si è caricato niente.

Non è cambiato niente.

Era solo timida.

E aveva il nome giusto.

The Peekaboo Bug.

<!-- S14 -->
Il rimedio era dire
all'elemento mancante
che la sua posizione era relativa.

Nessuno riuscì a spiegare del tutto
perché così tornava.

<!-- S15 -->
Poi c'è quello
in cui passi sopra un link,
e lo sfondo
del riquadro sotto
viene tagliato in linea retta.

The Guillotine Bug.

<!-- S16 -->
C'era un bug in cui il testo
strisciava via da dove l'avevi messo.

Magic Creeping Text.

Ce n'era uno in cui i bordi
uscivano nel posto sbagliato,
del colore sbagliato,
o non uscivano affatto.

Border Chaos.

<!-- S17 -->
Il mio preferito è più discreto.

Disponi una fila di riquadri,
e le lettere dell'ultimo
ricompaiono lì sotto.

Non sempre.

Non in modo prevedibile.

The Duplicate Character Bug.

<!-- S18 -->
E ciò che decideva
se capitava a te,
e quante lettere
uscivano doppie,
era il numero di commenti HTML
che avevi lasciato nel codice.

Commenti.

L'unica cosa nel file
che il browser
dovrebbe buttare via.

<!-- S19 -->
Ce n'è ancora uno,
ed è diverso,
perché questo la gente
lo usava di proposito.

Se imposti un'altezza
e il contenuto è più alto,
il riquadro dovrebbe traboccare.

Internet Explorer 6
ingrandiva il riquadro.

<!-- S20 -->
Il che è sbagliato.

Ed è anche esattamente
quello che fa un'altezza minima.

E Internet Explorer 6
non aveva l'altezza minima.

Così gli sviluppatori smisero
di segnalare quel bug
e cominciarono a contarci sopra.

<!-- S21 -->
Fermati e guarda quella lista.

The Three Pixel Jog.

The Double Margin Bug.

Peekaboo.

The Guillotine.

A un bug che incontri una volta
non dai un nome.

<!-- S22 -->
Questi avevano un nome
perché li incontravano tutti.

Ed ecco la parte
che peggiora le cose.

Quasi tutti avevano
la stessa causa sotto.

<!-- S23 -->
Dentro Internet Explorer 6,
ogni elemento aveva
oppure non aveva
qualcosa chiamato layout.

<!-- S24 -->
Decideva se l'elemento
si dava da sé dimensione e posizione,
o lasciava fare al genitore.

E non potevi impostarlo.

<!-- S25 -->
Non esisteva nessuna proprietà
di nome layout,
né un modo per chiederla.

Non era in nessuna specifica.

Era un flag interno
del motore di rendering.

<!-- S26 -->
Ma potevi farlo scattare
per sbaglio.

Impostare una larghezza lo faceva.

Impostare un'altezza lo faceva.

Far fluttuare un elemento lo faceva.

Quindi metà delle correzioni di questo video
erano persone che giravano un interruttore
che non potevano vedere.

<!-- S27 -->
Per questo si mise a cercare
il modo più economico
di farlo scattare apposta.

Uno era impostare un'altezza
dell'uno per cento.

<!-- S28 -->
Tutti gli altri browser
andavano tenuti lontani da quello,
quindi finì dentro un trucco
a cui arriviamo tra un minuto.

<!-- S29 -->
E in Internet Explorer 6
non faceva danni,
perché un'altezza in cui non ci sta
è comunque un'altezza che supera.

Il bug di due minuti fa
è ciò che rende sicura la correzione.

<!-- S30 -->
Aveva un nome.

The Holly Hack.

<!-- S31 -->
L'altro modo
era una proprietà Microsoft
chiamata zoom, messa a uno.

Zoom uno significa
non ingrandire.

<!-- S32 -->
Non cambiava niente di visibile.

Era proprio quello il punto.

Stava nei fogli di stile
solo per impostare
un flag invisibile
che faceva sparire i bug.

<!-- S33 -->
Il che ci porta ai trucchi,
ed è con i trucchi
che la cosa si fa strana.

Per sistemare un browser
devi prima poter parlare
soltanto a quello.

<!-- S34 -->
E Internet Explorer 6
si comportava come se ci fosse
un altro elemento
sopra l'elemento html.

Nessun altro browser lo faceva.

Non era documentato.

Semplicemente si comportava così.

<!-- S35 -->
Così scrivevi una regola
che corrispondeva al fantasma,
e solo quel browser
riusciva a vederla.

Asterisco, spazio, html.

<!-- S36 -->
Tutti gli altri browser la guardavano,
non trovavano niente che corrispondesse,
e andavano avanti.

Questo è lo star hack,
e per anni è rimasto
in quasi ogni foglio di stile
del web.

<!-- S37 -->
C'era anche
l'underscore hack.

Metti un trattino basso
davanti al nome di una proprietà.

<!-- S38 -->
Un browser conforme agli standard
butta via la riga
perché non è valida.

Internet Explorer 6
ignora il trattino basso
e la applica.

<!-- S39 -->
Quindi rompevi di proposito
il tuo stesso foglio di stile,
e la rottura
era l'istruzione.

<!-- S40 -->
E poi c'è quello
che Microsoft ha costruito apposta.

Potevi scrivere un commento
a cui obbediva solo Internet Explorer.

<!-- S41 -->
Per ogni altro browser
era un commento qualunque,
ignorato come si ignorano i commenti.

Per Internet Explorer 6
era una porta
verso una seconda versione
della pagina.

<!-- S42 -->
Il che significa che il produttore
ha guardato la situazione,
ha convenuto che questo browser
aveva bisogno di un foglio di stile suo,
e ha rilasciato una funzione
per rendere la cosa più facile.

<!-- S43 -->
Una parte del danno
non aveva bisogno di nessun bug.

Internet Explorer 6
aveva due modalità.

In quella moderna
seguiva lo standard.

<!-- S44 -->
In quella vecchia,
la larghezza di un riquadro
comprendeva il suo riempimento
e il suo bordo,
che è un numero
completamente diverso.

<!-- S45 -->
Quale modalità ti toccava
dipendeva dalla prima riga
del documento.

E la versione di HTML
verso cui si stavano spostando tutti
ti diceva di mettere
una dichiarazione XML lassù.

<!-- S46 -->
Quella riga spingeva
Internet Explorer 6
nella modalità vecchia.

A romperlo
era seguire lo standard più recente.

<!-- S47 -->
Poi c'è la trasparenza.

Internet Explorer 6 non sapeva
mostrare un PNG con bordi morbidi.

Dove l'immagine doveva sfumare,
metteva del grigio.

<!-- S48 -->
La risposta di Microsoft fu un filtro
con un nome da numero di serie.

Funzionava.

<!-- S49 -->
Ma disegnava fuori
dal normale processo
di rendering del browser,
quindi i link che ci mettevi sopra
spesso smettevano di funzionare.

Sistemavi l'immagine
e rompevi il link.

<!-- S50 -->
E sfumare qualsiasi altra cosa
era un secondo filtro,
con una sintassi propria,
messo nel foglio di stile
proprio accanto alla proprietà normale
che ogni altro browser capiva.

<!-- S51 -->
Una parte di tutto questo è più vecchia
dei bug stessi.

Prima di tutto ciò,
le impaginazioni si costruivano
con tabelle annidate.

<!-- S52 -->
E per tenere aperto uno spazio
usavi un'immagine trasparente
di un pixel,
stirata alla dimensione
che serviva a quello spazio.

Anche quello aveva un nome.

The spacer gif.

<!-- S53 -->
Il passaggio del mouse era un altro.

In Internet Explorer 6
funzionava sui link.

Solo sui link.

<!-- S54 -->
Così un menu che si apriva
quando muovevi il mouse
sopra qualsiasi altra cosa
richiedeva un piccolo programma
agganciato al foglio di stile.

<!-- S55 -->
Non uno script nella pagina.

Un file separato,
richiamato dal CSS,
con dentro codice il cui compito
era insegnare al browser
un solo selettore.

Quel file la gente se lo passò
per anni.

<!-- S56 -->
La prima parte diceva
che si poteva mettere JavaScript
dentro un foglio di stile.

Quello che non diceva
è quanto spesso quel JavaScript girava.

<!-- S57 -->
A ogni movimento del mouse.

A ogni tasto.

A ogni scorrimento.

Ancora e ancora,
per calcolare una larghezza.

<!-- S58 -->
E il browser aveva tetti
che non aveva nessun altro.

Un foglio di stile smetteva di valere
da qualche parte oltre
le quattromila regole.

Tutto quello che veniva dopo
il trentunesimo foglio di stile
di una pagina veniva ignorato.

<!-- S59 -->
Il che sembra un numero
che non raggiungerai mai,
finché il tuo sito non è così grande
che qualcuno deve scrivere
un passo di build il cui unico compito
è unire i fogli di stile
prima che il browser li veda.

<!-- S60 -->
E una parte di questo non era
affatto estetica.

Internet Explorer 6
contava i suoi oggetti di pagina
e i suoi oggetti di script
in due modi diversi,
e nessuno dei due lati
vedeva l'anello intero.

<!-- S61 -->
Quindi se uno script puntava
a una parte della pagina,
e quella parte della pagina
puntava di nuovo allo script,
nessuno dei due veniva mai liberato.

Lascia quella finestra aperta abbastanza
e il browser si mangiava la macchina.

<!-- S62 -->
Ma il migliore
non è affatto un bug di impaginazione.

Scrivi un tag input.

Gli dai un tipo.

E dimentichi il segno di uguale.

<!-- S63 -->
Quello è un attributo malformato.

Ogni parser mai scritto
ha una risposta per questo.

Ignoralo.

Indovina cosa si intendeva.

Vai avanti.

<!-- S64 -->
Internet Explorer andava in crash.

Dentro voleva sapere
se il campo era nascosto,
quindi confrontava quello che avevi scritto
con la parola hidden.

Tu non avevi scritto niente.

<!-- S65 -->
Così andò a prendere
quello che non avevi scritto
all'indirizzo zero.

Il che sarebbe
un normale crash del browser,
solo che il codice che lo faceva
non stava nel browser.

<!-- S66 -->
Stava in una libreria di sistema condivisa.

Quindi quelle tre parole
buttavano giù anche il client di posta,
e il riquadro di anteprima
del gestore dei file.

<!-- S67 -->
Una finestra con l'elenco dei file
sulla tua stessa macchina,
chiusa da una pagina web.

È la tesi della prima parte
che arriva come rapporto di crash.

Il browser non era un programma
che girava sul sistema.

Era parte del sistema.

<!-- S68 -->
E non potevi semplicemente
provare la correzione altrove.

Internet Explorer era saldato
al sistema operativo,
quindi un computer
faceva girare esattamente una versione.

<!-- S69 -->
Ecco perché un lavoro di front-end
nel 2006
veniva con uno scaffale
di macchine di scorta.

<!-- S70 -->
E più tardi con una cartella
di macchine virtuali,
ognuna con dentro un intero
sistema operativo
perché una sola pagina
potesse essere aperta lì.

<!-- S71 -->
E poi qualcuno fece
la cosa ovvia.

Se puoi insegnare al browser
una funzione che gli manca,
puoi insegnargliele tutte.

<!-- S72 -->
Uno sviluppatore di nome Dean Edwards
scrisse una libreria
il cui unico scopo
era far sì che Internet Explorer 6
si comportasse come una versione
successiva di sé stesso.

La gente la mise in campo.

In produzione.

<!-- S73 -->
Ed è qui che smette
di essere divertente.

Per quasi un decennio,
una fetta seria
del lavoro front-end del mondo
è finita negli errori di un browser.

Non funzioni.

Non prodotti.

Compensazione.

<!-- S74 -->
Ed è durato per
quello di cui parlava la prima parte.

Delle aziende ci avevano costruito
applicazioni vere,
di quelle che giravano solo lì,
e quelle applicazioni
dovevano funzionare anche il lunedì.

<!-- S75 -->
Così il browser di cui tutti
volevano liberarsi
era quello che nessuno
poteva togliere.

<!-- S76 -->
Nel 2010,
Google annunciò che le sue stesse
app avrebbero smesso di funzionarci.

E uno studio di design di Denver
decise che meritava un funerale.

<!-- S77 -->
Uno vero.

Una bara.

Un elogio funebre.

Tra ottanta e cento persone
vennero a vedere seppellire
un browser.

Ne avevano previste trenta.

<!-- S78 -->
E Microsoft mandò dei fiori.

Sul biglietto c'era scritto:
grazie per i bei momenti,
Internet Explorer 6.

<!-- S79 -->
Un anno dopo, giorno per giorno,
Microsoft lanciò un sito.

Seguiva quanta parte del mondo
usava ancora
Internet Explorer 6,
paese per paese.

<!-- S80 -->
A quel punto
era ancora il dodici per cento.

L'obiettivo era spingerlo
sotto l'uno.

L'azienda che aveva costruito il browser
teneva un conto alla rovescia pubblico
verso la morte del proprio prodotto.

<!-- S81 -->
Allora perché i bug avevano un nome?

Perché dai un nome alle cose
che non puoi aggirare.

<!-- S82 -->
Nessuno dà un nome al tempo
di un paese
che sta solo attraversando.

Glielo dai dove abiti.

E per una decina d'anni,
il web abitava lì.

<!-- S83 -->
Ma togliere Internet Explorer 6
dal web è un'altra storia.

Ed è lì che andremo la prossima volta.

Se la vuoi,
c'è un pulsante di iscrizione,
e la prima parte è linkata qui sotto.
