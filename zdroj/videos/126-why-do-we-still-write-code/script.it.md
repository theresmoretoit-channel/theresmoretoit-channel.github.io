<!-- S01 -->
Ecco un requisito completo
per un software gestionale.
Un utente può annullare un ordine.

<!-- S02 -->
Sei parole.
Qualsiasi sviluppatore annuirebbe.
Qualsiasi cliente lo firmerebbe.

<!-- S03 -->
Quindi, un utente può annullare un ordine
dopo che la fattura è già partita?
E dopo che è già stato spedito?

<!-- S04 -->
Annullarlo annulla anche
la prenotazione presso il fornitore?
E se una persona lo annulla
e un'altra approva lo stesso ordine
nello stesso secondo?

<!-- S05 -->
La frase non risponde a niente di tutto questo.
Il codice deve rispondere a tutto.
E quella lacuna, tra la frase
e il codice, è ciò per cui i programmatori
vengono pagati davvero.
O almeno, così era una volta.

<!-- S06 -->
Oggi c'è un'idea allettante.
Scrivere solo le frasi.
Tenerle in documenti,
revisionarle, versionarle.
E lasciare che un'IA scriva il codice.

<!-- S07 -->
La specifica diventa
il codice sorgente.
E il codice diventa ciò che è oggi
l'assembly: qualcosa che gira
e che nessuno legge.

<!-- S08 -->
È una buona idea.
Ma non è nemmeno nuova.

<!-- S09 -->
Da quasi settant'anni si cerca
di alzare il livello
a cui diciamo ai computer cosa fare.
Gli strumenti erano diversi,
e così i loro obiettivi.
Ma ognuno ha spostato un po' più di lavoro
dalle persone alle macchine.

<!-- S10 -->
Nel 1957, un gruppo di IBM
ha pubblicato un articolo su FORTRAN.
Il titolo lo definiva
un sistema di codifica automatica.

<!-- S11 -->
All'epoca era la definizione esatta.
Tu scrivevi formule,
e le istruzioni macchina,
la parte che le persone scrivevano a mano,
ora le produceva la macchina stessa.

<!-- S12 -->
Oggi FORTRAN lo chiamiamo codice.

<!-- S13 -->
Negli anni Ottanta, gli strumenti CASE
e i linguaggi di quarta generazione
sono saliti di un altro livello.
Disegni i diagrammi, compili i moduli,
e gran parte dell'applicazione
viene generata per te.

<!-- S14 -->
Nel 2001, l'Object Management Group,
l'ente dietro UML,
ha annunciato la Model Driven Architecture.

<!-- S15 -->
La promessa ti suonerà familiare.
Descrivi il sistema una volta sola,
come modello, indipendente da qualsiasi tecnologia.
Poi gli strumenti generano l'implementazione
per qualunque piattaforma ti serva.

<!-- S16 -->
Le stesse regole di business.
Tecnologia sostituibile.

<!-- S17 -->
E nel 2014, gli analisti di Forrester
hanno dato un nome alle piattaforme
per creare applicazioni aziendali
con la minor quantità possibile
di codice scritto a mano.
Lo hanno chiamato low-code.

<!-- S18 -->
Quindi, ha funzionato qualcosa?

<!-- S19 -->
In parte.
Nel 2014, alcuni ricercatori della Lancaster University
hanno pubblicato un sondaggio
su 450 persone
che usavano davvero
lo sviluppo guidato dai modelli.

<!-- S20 -->
Funzionava,
e più diffusamente di quanto molti pensassero.
Ma di rado per un intero sistema.
Lo usavano per le parti chiave
e costruivano il resto in altri modi.

<!-- S21 -->
Gli ostacoli maggiori che hanno trovato
erano le persone e le organizzazioni,
non gli strumenti.
Ma c'è anche un limite tecnico,
e i programmatori ci scherzano sopra.

<!-- S22 -->
Una specifica abbastanza precisa
da poterne generare l'intero programma...
ha già un nome.
Si chiama codice.

<!-- S23 -->
Per generare tutto,
il modello doveva dire tutto.
Ogni stato, ogni eccezione,
ogni «e se lo fanno due persone insieme?».

<!-- S24 -->
A quel punto
la programmazione non l'hai evitata.
L'hai solo spostata in un diagramma,
che spesso è più difficile da leggere,
da confrontare e da revisionare.

<!-- S25 -->
Già alla fine degli anni Settanta,
Edsger Dijkstra ha riassunto l'altra metà
in una breve nota dal titolo brusco.
Sulla stoltezza
della programmazione in linguaggio naturale.

<!-- S26 -->
Secondo lui, la notazione formale
non è un peso da sopportare.
L'ha definita uno strumento straordinariamente efficace
per escludere ogni sorta di assurdità.

<!-- S27 -->
La lingua di tutti i giorni non le esclude.
Le nasconde.
Un utente può annullare un ordine.

<!-- S28 -->
Quindi, se niente di tutto questo ha sostituito il codice,
perché riprovarci?

<!-- S29 -->
Perché una cosa è davvero diversa.

<!-- S30 -->
I vecchi generatori non sapevano colmare una lacuna
da soli.
Se il modello non diceva cosa succede
a un ordine già spedito,
qualcuno doveva aggiungere quella regola esplicitamente.
Finché non lo faceva, la lacuna restava lì,
e si poteva trovare.

<!-- S31 -->
Un'IA non si ferma.
Dalle il requisito di sei parole
e risponderà a ogni domanda
che ci siamo fatti all'inizio.

<!-- S32 -->
Deciderà che un ordine spedito
si può annullare. O che non si può.
Deciderà sulla fattura
e sul fornitore.
Produrrà codice che gira,
sembra ragionevole
e passa i test che si è scritta da sola.

<!-- S33 -->
È proprio questo che la rende utile.
Ed è proprio questo che la rende pericolosa.
Perché un'ipotesi plausibile
non è una decisione di business.

<!-- S34 -->
Prima, le lacune erano errori.

<!-- S35 -->
Ora sono decisioni
prese senza che nessuno se ne accorgesse.

<!-- S36 -->
Quindi, se la specifica deve davvero
diventare il codice sorgente,
non può essere qualche paragrafo alla buona.

<!-- S37 -->
Immagina il repository.
Un documento descrive gli ordini
e tutti gli stati in cui possono trovarsi.
Un altro dice chi può approvarli
e chi può annullarli.

<!-- S38 -->
Un terzo dice quando si emette una fattura
e quando va stornata.
Un altro descrive il sistema contabile,
compreso cosa succede quando non funziona.

<!-- S39 -->
Una parte è prosa normale.
Ma dove la prosa sarebbe ambigua,
c'è qualcosa di più rigoroso:
un elenco di stati e dei passaggi tra l'uno e l'altro,
uno schema, una regola che una macchina può verificare.

<!-- S40 -->
E accanto, test di accettazione
che dicono esattamente cosa deve succedere.

<!-- S41 -->
Tutto questo vive in Git.
Le modifiche vengono revisionate.
Ogni requisito si può ricondurre
al test che lo verifica.

<!-- S42 -->
Allora, come funziona una modifica?
Mettiamo che il cliente decida
che un ordine spedito si può ancora annullare,
purché non sia stato consegnato.
E che in quel caso la fattura vada stornata.

<!-- S43 -->
Nessuno apre il backend.
Uno sviluppatore cambia una regola
nel documento sugli ordini.

<!-- S44 -->
Poi il sistema va a cercare
tutto ciò che quella regola tocca.
Gli stati dell'ordine.
Le regole sulle fatture.
I test sull'annullamento.
La prenotazione presso il fornitore.

<!-- S45 -->
E lì dovrebbe fermarsi e chiedere.
La specifica non ha mai detto
cosa succede alla prenotazione presso il fornitore
quando la merce è già in viaggio.
Quella è una decisione,
quindi spetta a una persona.

<!-- S46 -->
Solo allora viene generata
la nuova implementazione.
E viene verificata in entrambe le direzioni.
I test della nuova regola devono passare.
E tutti gli altri test devono continuare a passare,
senza modifiche.

<!-- S47 -->
Perché una modifica all'annullamento
non deve cambiare di nascosto nient'altro.
Anche se i test superati dimostrano solo
ciò che quei test controllano.

<!-- S48 -->
E poiché le regole
non sono legate alla tecnologia,
la stessa specifica potrebbe produrre
oggi un'applicazione in PHP
e domani qualcosa di completamente diverso.

<!-- S49 -->
Che è esattamente ciò che
la Model Driven Architecture prometteva
venticinque anni fa.
La differenza è che, stavolta,
il generatore potrebbe essere all'altezza.

<!-- S50 -->
Resta la domanda più difficile.
Come fai a sapere che l'IA
ha davvero seguito la specifica?

<!-- S51 -->
Un codice che funziona nelle situazioni normali
può comunque fallire in quelle insolite.
E quelle insolite sono proprio
i casi che a nessuno viene in mente di testare.

<!-- S52 -->
Amazon ci si è scontrata
sui propri sistemi cloud.
Nel 2014, i suoi ingegneri hanno raccontato
come avevano iniziato a scrivere
descrizioni precise e matematiche
dei loro progetti,
in un linguaggio chiamato TLA+.

<!-- S53 -->
Non del codice. Del progetto in sé.
Uno strumento prendeva poi un modello del sistema,
limitato a una dimensione fissa,
e provava ogni possibile ordine
di guasti e ripristini.

<!-- S54 -->
In DynamoDB, il servizio di database di Amazon,
ha trovato un bug che poteva far perdere dati.

<!-- S55 -->
Il modo più breve per innescarlo
richiedeva 35 passaggi,
esattamente nell'ordine giusto.
Era sfuggito alle revisioni del progetto,
alle revisioni del codice e ai test.

<!-- S56 -->
Quindi la versione onesta dell'idea
non è che l'IA scrive il codice
e noi ci fidiamo.
È che l'IA scrive il codice,
e qualcosa di indipendente lo verifica.

<!-- S57 -->
Ora guarda cosa abbiamo costruito.

<!-- S58 -->
Stati precisi.
Regole formali.
Test verificabili.
Versionato, revisionato, conservato in un repository.

<!-- S59 -->
Non sembra
la fine della programmazione.
Sembra programmazione,
in un linguaggio nuovo.

<!-- S60 -->
Ed è quello che è successo ogni volta.
FORTRAN era codifica automatica,
finché non è diventato il codice.
Ogni volta che la macchina si è presa
il «come», le persone sono salite al «cosa».

<!-- S61 -->
E il «cosa» è sempre stato la parte difficile.
Non digitare, ma decidere.
Cosa succede a un ordine spedito.
Chi può toccare quali dati.
Cosa il sistema non deve fare mai.

<!-- S62 -->
Forse il programmatore del futuro
non scriverà migliaia di righe di codice.

<!-- S63 -->
Ma qualcuno dovrà comunque capire
un problema abbastanza bene da dire
esattamente cosa deve fare un computer,
e verificare che l'abbia fatto.

<!-- S64 -->
E se la specifica
diventa il codice sorgente,
la competenza più importante
forse non sarà più sapere
come si scrive un programma.

<!-- S65 -->
Forse sarà sapere
come descriverne uno.

<!-- S66 -->
Allora, ecco la domanda
a cui mi piacerebbe leggere la tua risposta.
Se scrivi una specifica
abbastanza precisa
da permettere a una macchina di costruire il programma...
stai ancora programmando?
