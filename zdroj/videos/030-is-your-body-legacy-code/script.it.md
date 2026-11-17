<!-- S01 -->
Immagina un programma
con tre miliardi di caratteri
di istruzioni.

<!-- S02 -->
E che ogni volta
che avvii un nuovo processo
ci copi dentro l'intero programma.

<!-- S02b -->
Due volte.

<!-- S03 -->
Non solo le funzioni
che quel processo usa.
Assolutamente tutto.
Ogni modulo.
Ogni dipendenza.
Ogni pezzo di vecchio codice legacy.

<!-- S04 -->
E poi il processo semplicemente
ne ignora il novantanove per cento.
Sarebbe un pessimo lavoro
di ingegneria del software.

<!-- S05 -->
Eppure...

<!-- S06 -->
...è più o meno quello
che fanno le tue cellule.

<!-- S07 -->
Quasi ogni cellula del tuo corpo
dotata di nucleo
contiene in sostanza la stessa
copia completa del tuo genoma.

<!-- S08 -->
Un neurone ce l'ha.
Una cellula del fegato ce l'ha.
Una cellula della pelle ce l'ha.
Eppure si comportano
in modo completamente diverso.

<!-- S09 -->
Il codice c'è.
Solo che quasi tutto non viene usato.

<!-- S10 -->
Un gene si può vedere,
molto alla buona,
come una funzione o un modulo.

<!-- S11 -->
Porta un'informazione
da cui alla fine può
nascere un certo
prodotto funzionale,
spesso una proteina.
Possiamo immaginarlo così.

<!-- S12 -->
Ma avere la funzione nel codice
non vuol dire che sia in esecuzione.
Qualcosa deve attivarla.
Ed è qui che la biologia
diventa interessante.

<!-- S13 -->
Perché in un computer
scrivo semplicemente questo.
Oppure in codice macchina.

<!-- S14 -->
Il processore sa esattamente che fare.
C'è un'istruzione.
C'è un indirizzo.
C'è un puntatore alle istruzioni.

<!-- S15 -->
Ma una cellula non ha un processore
che esegua le istruzioni
del DNA una dopo l'altra.

<!-- S16 -->
Quindi...

<!-- S17 -->
...come fa a sapere cosa usare?

<!-- S18 -->
È qui che il paragone
con il computer si fa strano.
In un computer puoi saltare
a un preciso indirizzo di memoria.

<!-- S19 -->
Puoi avere permessi di accesso.
Puoi avere processi.
Puoi avere file di configurazione.
Puoi avere eventi
che attivano precisi pezzi di codice.

<!-- S20 -->
La biologia ha cose
con ruoli sorprendentemente simili.

<!-- S21 -->
I fattori di trascrizione si legano
a certe sequenze di DNA
e influenzano se un gene
venga trascritto o no.

<!-- S22 -->
Le sequenze regolatrici influenzano
quando e dove i geni sono espressi.
La struttura della cromatina decide
quanto sono accessibili
le singole regioni del DNA.

<!-- S23 -->
E le cellule ricevono di continuo
segnali dall'ambiente.

<!-- S24 -->
Così, invece di un processore,
di un puntatore alle istruzioni,
di un indirizzo e di un'esecuzione...

<!-- S25 -->
...hai piuttosto qualcosa del genere.

<!-- S26 -->
Non c'è un unico puntatore.
C'è un'enorme rete
di interazioni molecolari.

<!-- S27 -->
Il DNA c'è.
Ma le sue varie parti
sono più o meno accessibili
al macchinario molecolare
che le legge.

<!-- S28 -->
Quindi avere il codice
non è la stessa cosa
che avere accesso al codice.
Una cellula del fegato non cancella
i geni dei neuroni.
Le basta regolare
se vengano usati.

<!-- S29 -->
Torniamo
al nostro progetto software.
Diciamo che stai sviluppando
un'applicazione enorme.

<!-- S30 -->
Crei un modulo chiamato finger.
E invece di importare
le poche funzioni che gli servono...

<!-- S31 -->
...ci copi dentro l'intero
repository umano.

<!-- S32 -->
Il cervello.
Il fegato.
Il cuore.
Il sistema immunitario.
L'apparato riproduttivo.
Tutto.

<!-- S33 -->
E lo rifai...

<!-- S34 -->
...per ogni singola cellula.

<!-- S35 -->
Da programmatore
probabilmente chiederesti...
Chi ha progettato questa roba?

<!-- S36 -->
E la risposta è...

<!-- S37 -->
Nessuno.

<!-- S38 -->
Beh... Non proprio nessuno.
L'evoluzione.

<!-- S39 -->
E l'evoluzione ha una filosofia
di sviluppo molto diversa.

<!-- S40 -->
Immagina di aprire un repository
chiamato umano,
la cui cronologia di commit
risale a miliardi di anni fa.

<!-- S41 -->
Nessun architetto si è seduto
a progettare la versione 1.0.
Non c'è mai stata una riscrittura pulita.
Non c'è mai stato un umano versione due
con architettura rifatta.

<!-- S42 -->
Invece...
Aggiungi una funzione.
Rattoppa un bug.
Duplica un modulo.
Riusa un vecchio modulo.

<!-- S43 -->
Aggira un limite.
Aggiungi un'altra pezza.
Tieni la vecchia API,
perché qualcosa ci si appoggia.

<!-- S44 -->
Di nuovo.
E di nuovo.
E di nuovo.
Per miliardi di anni.

<!-- S45 -->
L'evoluzione non chiede
qual è l'architettura più pulita.
La sua domanda è molto più semplice.
Questo organismo
si riproduce con successo?

<!-- S46 -->
Se la risposta è sì,
il codice sopravvive.

<!-- S47 -->
Immagina di ereditare un progetto
mantenuto
da milioni di programmatori,
per miliardi di anni,
senza la minima possibilità
di riscriverlo da capo.

<!-- S48 -->
Trovi qualcosa e chiedi...
Perché esiste questa roba?
Perché qualcosa ci dipendeva.

<!-- S49 -->
Perché questa API è così strana?
Legacy.

<!-- S50 -->
Questa è l'evoluzione.
Il sistema legacy per eccellenza.
Non rifattorizza.
Modifica ciò che già esiste.

<!-- S51 -->
E dopo miliardi di anni...

<!-- S52 -->
...ne usciamo noi.

<!-- S53 -->
Lo sviluppo software moderno
parte da un'idea abbastanza sensata.
Fai una modifica.
Poi la collaudi.

<!-- S54 -->
Commit.
Build.
Test unitari.
Test di integrazione.
Rilascio.

<!-- S55 -->
La biologia ha qualcosa
che le somiglia vagamente.
Avviene una mutazione.

<!-- S56 -->
E poi...
O l'organismo sopravvive
e si riproduce.
Oppure no.

<!-- S57 -->
Non c'è nessun ambiente di staging.
Non c'è nessun rollback.

<!-- S58 -->
E ogni tanto
succede qualcosa di molto peggio.
Una mutazione può rendere una cellula
più brava a sopravvivere e moltiplicarsi
dentro l'organismo.
Questo può contribuire al cancro.

<!-- S59 -->
La biologia ha quindi una versione
terrificante dell'integrazione continua.
I test si fanno
sul sistema in produzione.

<!-- S60 -->
Ma è proprio qui
che il paragone
con il software si fa più interessante.
Quando guardi il corpo umano,
viene voglia di immaginare
qualcosa del genere.

<!-- S61 -->
Solo che non è così
che il sistema funziona.
Non c'è un server centrale
che manda ordini a ogni cellula.

<!-- S62 -->
Le tue cellule sorvegliano di continuo
l'ambiente più vicino.
Ricevono segnali chimici.
Sono in contatto con le vicine.
Reagiscono agli ormoni.

<!-- S63 -->
Una cellula non riceve mai
un messaggio che dice...

<!-- S64 -->
...cellula numero sette milioni
trecentonovantaduemila
centottantaquattro.
Esprimi ora il gene X, per favore.

<!-- S65 -->
Se programmi,
diventa improvvisamente utile
un altro concetto.
I sistemi distribuiti.

<!-- S66 -->
Le tue cellule sono in pratica
un numero immenso
di agenti individuali.
Ognuno ha il proprio stato.
I propri sensori.
I propri ingressi.
Le proprie risposte.

<!-- S67 -->
Non c'è un unico ciclo gigantesco
che dice a ogni cellula cosa fare.
È più vicino a un
sistema multiagente.
O a uno sciame.
O a un automa cellulare.

<!-- S68 -->
Regole locali semplici...

<!-- S69 -->
...da cui nasce un comportamento
d'insieme incredibilmente complicato.

<!-- S70 -->
E un'altra cosa che sarebbe
inaccettabile in un software normale.
Il tuo corpo gira
senza sosta da decenni.

<!-- S71 -->
Nessun riavvio.
Nessuna finestra di manutenzione.

<!-- S72 -->
Eppure il sistema
cambia in continuazione.
Le cellule muoiono.
Ne nascono di nuove.
Le proteine si formano e si disfano.

<!-- S73 -->
Il DNA viene copiato.
I danni vengono riparati.
I pezzi vengono sostituiti.

<!-- S74 -->
Il sistema non si spegne
per fare la manutenzione.
Fa la manutenzione
a pieno regime.

<!-- S75 -->
Quasi come se avessi un server
che si cambia i pezzi da solo
proprio nel momento
in cui serve le richieste...

<!-- S76 -->
...e non va mai offline.

<!-- S77 -->
Le cellule hanno il loro macchinario.
Comunicano.
Rispondono.
Si regolano a vicenda.
Formano tessuti.
I tessuti formano organi.
Gli organi formano apparati.
E gli apparati formano un organismo.

<!-- S78 -->
E non c'è un singolo pezzo
che tenga tutta l'architettura
in testa.

<!-- S79 -->
E in qualche modo...

<!-- S80 -->
...funziona.

<!-- S81 -->
Non alla perfezione.
Tutt'altro che alla perfezione.

<!-- S82 -->
Ma abbastanza da fare occhi.
Cuori.
Sistemi immunitari.
Cervelli.

<!-- S83 -->
E organismi capaci
di scrivere software per lamentarsi
di quanto sia mal progettato
il sistema.

<!-- S84 -->
Chiamiamo il DNA codice.
E il paragone è utile.
I geni ricordano un po' le funzioni.
Le mutazioni ricordano un po'
le modifiche al codice sorgente.

<!-- S85 -->
Ma c'è
una differenza importante.
Il DNA non è davvero
un progetto completo di un essere umano.

<!-- S86 -->
Da nessuna parte c'è una riga...
Crea un braccio.
Crea un occhio.
Crea un cuore.

<!-- S87 -->
Il DNA partecipa invece
a un'enorme trama di influenze
in cui entrano molecole, cellule,
forze fisiche, gradienti chimici,
tempi e ambiente.

<!-- S87b -->
L'organismo emerge da tutto questo.

<!-- S88 -->
Quindi il DNA si capisce meglio
come un insieme di istruzioni e regole
inserito in un sistema fisico...

<!-- S89 -->
...che come il listato completo
del codice sorgente di una persona.
E questo è in realtà molto più strano.

<!-- S90 -->
Sappiamo sequenziare un genoma,
identificare i geni
e misurare le proteine.

<!-- S91 -->
Ma ancora non sappiamo prendere il DNA
di una comune cellula umana,
metterlo in un computer,
premere esegui...

<!-- S92 -->
...e guardare quella persona formarsi.

<!-- S93 -->
Abbiamo il genoma.
Ma il genoma
non è tutta la macchina.

<!-- S94 -->
Ed è qui che arriviamo.
Siamo partiti da un'idea familiare.
Il DNA è come codice.

<!-- S95 -->
E il paragone si rivela
sorprendentemente utile.
Ma più a fondo guardiamo,
più il sistema diventa strano.

<!-- S96 -->
Non c'è un processore.
Non c'è un sistema operativo.
Non c'è un server centrale.

<!-- S97 -->
Non c'è un programmatore.
Non c'è GitHub.
Non c'è la revisione del codice.
Non c'è un ambiente di staging.
Non c'è il rollback.
Non c'è nemmeno per bene
un'architettura pulita.

<!-- S98 -->
Ci sono migliaia di miliardi di agenti,
ognuno che segue regole locali,
che si intende con i vicini,

<!-- S99 -->
che usa un repository enorme, antichissimo
e modificato di continuo...
E in qualche modo ne esce
un organismo che funziona.

<!-- S100 -->
Quindi se la biologia è software...

<!-- S101 -->
...è forse il sistema legacy
più vecchio, più caotico
e più sovraingegnerizzato che esista.

<!-- S102 -->
Un sistema con miliardi di anni
di commit.
Quasi nessun refactoring.
Nessun amministratore centrale.
E assolutamente nessun riavvio.

<!-- S103 -->
E in qualche modo...

<!-- S104 -->
...gira in produzione
da miliardi di anni.
