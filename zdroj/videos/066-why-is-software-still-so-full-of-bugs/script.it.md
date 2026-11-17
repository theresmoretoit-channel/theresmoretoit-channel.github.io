<!-- S01 -->
Ogni pochi giorni, un altro bug grave
finisce nelle notizie.
Un bug che permette a qualcuno di saltare il login.
Un bug che fa trapelare dati privati.
Un bug che consegna il tuo computer a un aggressore.

<!-- S02 -->
A volte è Windows. A volte Linux.
Un browser, un database, un servizio cloud...
o una piccola libreria
da cui dipendono milioni di sviluppatori.

<!-- S03 -->
E la reazione è quasi sempre la stessa.
Come hanno fatto i programmatori a non accorgersene?

<!-- S04 -->
Sono professionisti.
Hanno revisioni del codice, test automatici,
audit di sicurezza, fuzzing...
eppure i bug continuano ad arrivare.

<!-- S05 -->
Quindi è davvero possibile
scrivere software complesso senza bug?

<!-- S06 -->
Partiamo da un numero.
Immagina un programma con appena cento impostazioni,
ognuna accesa o spenta.

<!-- S07 -->
Cento semplici decisioni sì o no.
Quante combinazioni fanno?

<!-- S08 -->
Due elevato alla cento.
Cioè circa un milione di bilioni di bilioni.

<!-- S09 -->
Ora immagina di poter provare
un miliardo di combinazioni al secondo.
E di aver iniziato al Big Bang.

<!-- S10 -->
A oggi ne avresti provata
circa una combinazione su tremila.

<!-- S11 -->
E cento interruttori non sono niente.
Un programma vero ne ha milioni.
Quindi "basta provare tutto"
non è costoso. È impossibile.

<!-- S12 -->
E quegli interruttori non hanno niente di esotico.
Prendi una delle cose più semplici
che un programma faccia.
Un utente chiede il proprio account tramite il suo numero.
Noi lo troviamo nel database.
E glielo restituiamo.

<!-- S13 -->
Ma se l'utente non esiste?
E se qualcuno manda del testo invece di un numero?
O un numero negativo? O uno enorme?

<!-- S14 -->
E se questa persona non ha il permesso di vederlo?
E se qualcuno cancella l'account
proprio nel momento in cui lo stiamo caricando?
E se la stessa richiesta arriva due volte?

<!-- S15 -->
Ognuna di queste domande è semplice.
Il problema è come si combinano.
Ognuna è un altro interruttore.

<!-- S15b -->
A proposito, se ti piacciono video
come questo, puoi iscriverti al canale.

Aiuta davvero il canale.

<!-- S16 -->
E un computer non le risolve al posto nostro.
Fa esattamente quello che gli diciamo.
Non quello che intendevamo.

<!-- S17 -->
Ecco perché abbiamo inventato i linguaggi di programmazione.
Ci lasciano descrivere cose complesse
senza pensare a ogni dettaglio.

<!-- S18 -->
Ma alcuni si occupano di meno
di quanto vorresti.
Prendi il C. È veloce, è semplice,
e ti dà un enorme controllo sulla memoria.

<!-- S19 -->
Così puoi scrivere questo.
Riserviamo spazio per sedici caratteri.
Poi diciamo: copia qui l'input.

<!-- S20 -->
E se l'input è
lungo cinquecento caratteri?
Il C non chiede.
Continua semplicemente a scrivere oltre la fine.

<!-- S21 -->
E cosa c'è subito dopo quei sedici caratteri?
Spesso, qualcosa di molto importante.

<!-- S22 -->
Quando un programma chiama una funzione,
annota dove tornare
una volta finita la funzione.
Un indirizzo di ritorno.
In una disposizione classica si trova
non lontano dalla fine del nostro buffer.

<!-- S23 -->
Così un aggressore invia un input
della lunghezza esatta.
Prima, le sue istruzioni.
Poi, proprio alla fine, un nuovo indirizzo di ritorno...
che punta di nuovo a quelle istruzioni.

<!-- S24 -->
La funzione termina.
Il processore cerca dove tornare...
e salta dritto nel codice dell'aggressore.

<!-- S25 -->
Ora sta eseguendo il suo programma,
con tutti i permessi del tuo.
È questo che significa "eseguire codice arbitrario".

<!-- S26 -->
E il processore non ha fatto niente di sbagliato.
Ha seguito le istruzioni.

<!-- S27 -->
Nel 1988, un errore esattamente come questo
lasciò diffondere il worm Morris
nei primi tempi di internet.
E lo stesso trucco viene usato
negli attacchi da allora.

<!-- S28 -->
Così i linguaggi più recenti affidano parte del lavoro
al compilatore.
Rust, per esempio, si rifiuta di compilare
molti programmi che potrebbero gestire male la memoria.

<!-- S29 -->
Il programmatore dice:
ma so esattamente quello che faccio!
E il compilatore dice:
lo dicono tutti.

<!-- S30 -->
Ed è giusto essere sospettosi.
Microsoft e il team Chrome di Google
hanno riferito entrambi
che circa il settanta per cento
dei bug di sicurezza che hanno studiato
nasce da problemi di sicurezza della memoria.

<!-- S31 -->
Ma un programma può essere perfettamente sicuro in memoria
e comunque del tutto sbagliato.

<!-- S32 -->
Immagina che un utente acceda.
La sua password viene verificata correttamente.
Niente va in crash. Nessuna memoria si corrompe.

<!-- S33 -->
E poi il programma gli mostra
i dati di qualcun altro.
Perché il controllo dei permessi
è stato scritto un po' storto.

<!-- S34 -->
Nessun linguaggio può coglierlo da solo.
Il linguaggio non sa
cosa il programma doveva fare.
Solo noi lo sappiamo.

<!-- S35 -->
Allora torniamo ai test.
Un test può dirti:
per questo input ho ottenuto questo risultato.

<!-- S36 -->
Non può dirti:
il programma è corretto per ogni input.
E abbiamo già visto
perché non possiamo provarli tutti.

<!-- S37 -->
Nel 1970, l'informatico
Edsger Dijkstra lo riassunse in una frase.
I test possono mostrare la presenza di bug,
ma mai la loro assenza.

<!-- S38 -->
Va bene. Allora, invece di testare,
perché non scrivere un programma
che controlla altri programmi
e dimostra che sono corretti?
Dagli un codice qualsiasi, e ti dice
se quel codice fa quello che dovrebbe.

<!-- S39 -->
A quella domanda si rispose
prima ancora che il primo vero computer fosse costruito.
Nel 1936, Alan Turing dimostrò
che un programma del genere non può esistere.

<!-- S40 -->
Non che nessuno l'abbia ancora costruito.
Che non può esistere affatto.

<!-- S41 -->
Dimostrò che nessun programma può decidere,
per ogni altro programma,
se prima o poi si fermerà.

<!-- S42 -->
E nel 1953, Henry Rice andò oltre.
Lo stesso vale per ogni domanda non banale
su ciò che un programma fa davvero.

<!-- S43 -->
È sicuro? Fa trapelare dati?
Dà la risposta giusta?
Non esiste alcun metodo generale
che lo risolva per ogni programma.

<!-- S44 -->
Quindi il software senza bug è impossibile?
Non proprio.
Per un programma specifico
a volte puoi dimostrare che è corretto,
con uno sforzo enorme.

<!-- S45 -->
Nel 2009, un gruppo in Australia dimostrò
che un piccolo kernel di sistema operativo,
chiamato seL4,
fa esattamente quello che dice la sua specifica.

<!-- S46 -->
Aveva meno di diecimila righe di codice.
Costruire il kernel richiese
circa due anni-persona.
Dimostrarne la correttezza ne richiese circa venti.
Un browser web moderno
ha decine di milioni di righe.

<!-- S47 -->
Ma anche quella dimostrazione ha un limite.
Mostra che il programma corrisponde alla sua specifica.
Non può mostrare che la specifica
è ciò che volevamo davvero.

<!-- S48 -->
E la specifica è scritta da persone.
Così la domanda torna a noi.

<!-- S49 -->
E non è solo il nostro codice.
Un programmatore oggi si basa su framework,
librerie e centinaia di dipendenze.
Ogni livello ci risparmia enormi quantità di lavoro.
Ma ogni livello è qualcosa
che dobbiamo capire...
o almeno di cui fidarci.

<!-- S50 -->
Il che significa che non devi scrivere un bug
per averne uno nel tuo software.
Ti basta installarlo.

<!-- S51 -->
Poi aggiungi la pressione.
Nessuno vuole un prodotto perfetto tra dieci anni.
Ne vogliono uno che funzioni il mese prossimo.
E un'intrusione che non è mai avvenuta
è molto difficile da mostrare in una presentazione.

<!-- S52 -->
Ed ecco la parte più strana.
I nostri strumenti continuano a migliorare.
Linguaggi più sicuri, fuzzing, bug bounty...

<!-- S53 -->
Eppure il numero di vulnerabilità note
continua a crescere.
Solo nel 2024, circa quarantamila
hanno ricevuto un numero ufficiale.

<!-- S54 -->
In parte perché scriviamo anche
molto più software che mai.
È come rendere ogni strada più sicura...
mentre costruiamo milioni di volte più strade.

<!-- S55 -->
Quindi i programmatori sono incapaci nel loro lavoro?
No.
Gli chiediamo da sempre una cosa
che nessun metodo generale può garantire.

<!-- S56 -->
Quindi forse
"come scriviamo software senza bug?"
è la domanda sbagliata.

<!-- S57 -->
La domanda migliore è:
come costruiamo sistemi che restano sicuri
anche quando il software ha dei bug?

<!-- S58 -->
Ed è esattamente lì che va la sicurezza.
Non dice: non commettere mai un errore.
Dice: dai per scontato di averlo già commesso.

<!-- S59 -->
Ti ricordi quell'indirizzo di ritorno?
Oggi il sistema lo protegge.
Rimescola dove si trovano le cose in memoria.
E si rifiuta di eseguire istruzioni
nascoste nei dati.

<!-- S60 -->
Il bug nel nostro codice C è ancora lì.
Solo che è molto più difficile trasformarlo in un attacco.

<!-- S61 -->
E la stessa idea è ovunque.
Sandbox, permessi limitati,
processi isolati, cifratura,
backup, monitoraggio...
strato dopo strato,
perché un solo bug non diventi un disastro.

<!-- S62 -->
E ha una conseguenza molto pratica.
Se i bug sono inevitabili,
correggerli non è facoltativo.

<!-- S63 -->
Il software che stai usando oggi
potrebbe benissimo contenere una vulnerabilità
che nessuno ha ancora trovato.

<!-- S64 -->
E quando qualcuno la trova,
l'aggiornamento è la differenza tra
"è stata scoperta una vulnerabilità"
e "ci hanno hackerato".

<!-- S65 -->
Lo stesso vale per i sistemi che costruiamo.
Vecchie librerie e piattaforme non più supportate
non diventano più sicure se le ignori.
Si trasformano in debito tecnico.

<!-- S66 -->
E perché quel debito vada ripagato,
il mio video
"Funziona ancora. Allora perché aggiornarlo?"
parla esattamente di questo.

<!-- S67 -->
Perché, nel software,
"funziona ancora"
e "è ancora sicuro"
sono due cose molto diverse.
