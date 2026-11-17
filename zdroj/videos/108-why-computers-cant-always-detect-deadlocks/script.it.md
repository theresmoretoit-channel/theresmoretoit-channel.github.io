<!-- S01 -->
Quattro auto arrivano a un incrocio
esattamente nello stesso momento.
Niente semafori. Niente cartelli.
Solo la regola che vale in molti paesi:
dai la precedenza all'auto alla tua destra.

<!-- S02 -->
Ogni automobilista guarda a destra
e vede un'auto a cui deve dare la precedenza.
Così ogni automobilista aspetta.

<!-- S03 -->
Nessuno sta infrangendo la regola.
Tutti la rispettano alla perfezione.
E nessuno si muoverà mai.

<!-- S04 -->
Gli informatici lo chiamano deadlock, o stallo.
E non succede solo sulle strade.
Succede dentro i database,
nei sistemi operativi e nei normali software.

<!-- S05 -->
Spesso i computer sono bravi a individuare
un deadlock quando ormai è avvenuto.
Ma un programma potrebbe leggere un altro programma
e dirti con certezza
se prima o poi si bloccherà?

<!-- S06 -->
Per molti programmi, sì.
Ma un metodo che funzioni
per ogni programma possibile
non può esistere.
E non perché i computer
non siano ancora abbastanza veloci.
Nessun computer più veloce lo cambierà mai.

<!-- S07 -->
Ecco come si blocca un programma.
Immagina un negozio online
con due operazioni in corso contemporaneamente.

<!-- S08 -->
Prima che un'operazione modifichi qualcosa,
ci mette sopra un lock,
così che nessun altro possa toccarlo.
Come prendere l'unica chiave di una stanza.

<!-- S09 -->
La prima operazione blocca l'account di un cliente,
poi cerca di bloccare il suo ordine.
La seconda blocca l'ordine,
poi cerca di bloccare l'account.

<!-- S10 -->
Una tiene l'account
e aspetta l'ordine.
L'altra tiene l'ordine
e aspetta l'account.
Nessuna delle due molla quello che ha.

<!-- S11 -->
E la cosa strana è che
questo codice può girare un milione di volte
senza alcun problema.
Solo quando le due operazioni si sovrappongono
esattamente nell'ordine sbagliato
si ferma tutto.

<!-- S12 -->
Il bug c'era da sempre.
La coincidenza dei tempi l'ha solo fatto emergere.

<!-- S12b -->
A proposito, se ti piacciono video
come questo, puoi iscriverti al canale.

Aiuta davvero il canale.

<!-- S13 -->
I database ci sbattono contro di continuo,
perciò stanno all'erta.
Disegnano una mappa di chi aspetta chi.

<!-- S14 -->
La prima aspetta la seconda.
La seconda aspetta la prima.
Quando le frecce si chiudono in un ciclo,
quello è un deadlock.
Niente congetture. Il ciclo è proprio lì.

<!-- S15 -->
Allora il database fa una cosa brutale.
Sceglie una delle operazioni
e butta via il suo lavoro.

<!-- S16 -->
SQL Server di Microsoft dice persino alla perdente
che è stata scelta
come vittima del deadlock
e che deve riprovare.

<!-- S17 -->
L'altra operazione va avanti,
e la vittima può semplicemente riprovare.

<!-- S18 -->
Nota cosa risolve e cosa no.
Il deadlock è risolto.
Ma il codice che l'ha causato è ancora lì,
in attesa del prossimo momento sfortunato.

<!-- S19 -->
Quindi individuare un deadlock
che è già avvenuto
è la parte facile.
La domanda difficile è un'altra.

<!-- S20 -->
Non: questo programma è bloccato adesso?
Ma: dagli questo input.
Potrebbe mai bloccarsi?

<!-- S21 -->
La prima è una foto del presente.
Basta guardarla.
La seconda è una previsione
su ogni futuro possibile.

<!-- S22 -->
E i programmi la rendono molto difficile.
Prendono decisioni. Ripetono cose.
Possono eseguire calcoli che durano
un secondo, o mille anni.

<!-- S23 -->
Un programma potrebbe bloccarsi subito,
dopo un milione di passi,
per un solo input raro,
o mai.

<!-- S24 -->
Potresti semplicemente eseguirlo e guardare.
Ma se dopo un'ora non si è bloccato,
che cosa ti dice?

<!-- S25 -->
Niente.
Potrebbe bloccarsi nel secondo successivo,
o mai.

<!-- S26 -->
Nel 1936, un giovane matematico
di nome Alan Turing dimostrò
che ad alcune domande sui programmi
non può rispondere nessun programma.
La più famosa sembra ancora più semplice.

<!-- S27 -->
Prendi un programma qualsiasi e il suo input.
Prima o poi si fermerà?
O andrà avanti per sempre?

<!-- S28 -->
Oggi si chiama problema della fermata.
E nessun programma può risolverlo
correttamente in ogni caso.

<!-- S29 -->
L'idea alla base della dimostrazione
è sorprendentemente breve.
Supponi che qualcuno ti dia
un verificatore di fermata perfetto.

<!-- S30 -->
Ora scrivi un piccolo programma bastian contrario.
Interroga il verificatore su sé stesso
e poi fa l'opposto.

<!-- S31 -->
Se il verificatore dice che si fermerà,
gira in loop per sempre.
Se il verificatore dice che andrà avanti per sempre,
si ferma subito.

<!-- S32 -->
Qualunque cosa il verificatore dica su di lui,
il verificatore sbaglia.
Quindi un verificatore perfetto non può esistere.

<!-- S33 -->
E cosa c'entra tutto questo con i deadlock?
Tutto.

<!-- S34 -->
Immagina che qualcuno sostenga di aver costruito
un predittore di deadlock perfetto.
Gli dai un programma qualsiasi e il suo input,
e lui ti dice sempre, senza sbagliare,
se quel programma prima o poi si bloccherà.

<!-- S35 -->
Usiamolo
per risolvere il problema della fermata.

<!-- S36 -->
Prendi un programma qualsiasi
e inseriscilo in un nuovo programma.

<!-- S37 -->
Per prima cosa, il nuovo programma
esegue semplicemente quello vecchio,
passo dopo passo, su un solo thread.
Niente lock. Niente di condiviso.
Niente che possa mai bloccarsi.

<!-- S38 -->
Poi, se il vecchio programma termina,
il nuovo avvia due operazioni.
Ognuna prende un lock,
aspetta che l'altra abbia preso il suo,
e poi cerca di prendere quello dell'altra.
Un deadlock, apposta, ogni volta.

<!-- S39 -->
Se il vecchio programma non termina mai,
il nuovo non arriva mai fin lì.
Nessun deadlock. Mai.

<!-- S40 -->
Quindi il nuovo programma si blocca
se, e solo se, il vecchio si ferma.

<!-- S41 -->
Ora chiedi al predittore
del nuovo programma.
«Sì, andrà in deadlock»
significa che il vecchio programma si ferma.
«No» significa che va avanti per sempre.

<!-- S42 -->
Abbiamo appena risolto il problema della fermata.
Ed è esattamente ciò che non si può fare.

<!-- S43 -->
Quindi nemmeno il predittore di deadlock perfetto
può esistere.

<!-- S44 -->
Il problema non sono i lock,
né i database, né i programmatori scarsi.
Un programma può nascondere qualsiasi calcolo
prima di un deadlock.
Per prevedere il deadlock,
dovresti prevedere se quel calcolo finisce.

<!-- S45 -->
Ma un momento.
Un computer reale non è infinito.
La sua memoria ha un numero limitato di stati.
Quindi non potresti semplicemente controllarli tutti?

<!-- S46 -->
Per una macchina con una quantità fissa
di memoria, in linea di principio, sì.
In pratica, prova a contarli.

<!-- S47 -->
La memoria di un portatile
da otto gigabyte
si può disporre in così tanti modi
che solo scrivere quel numero
richiede circa venti miliardi di cifre.

<!-- S48 -->
Il numero di atomi
nell'universo osservabile
ne ha circa ottanta.

<!-- S49 -->
Quindi su una macchina reale, controllare tutto
è possibile in teoria
e irrealizzabile in pratica.

<!-- S50 -->
Ma questo è un altro muro.
Il limite di Turing non nasce dai troppi stati.
Vale per i programmi
che possono sempre chiedere più memoria.
Per quelli, nessun predittore perfetto può esistere,
per quanto grande sia il computer.

<!-- S51 -->
Vuol dire che con i deadlock non c'è niente da fare?
No.
Vuol dire che non esiste un verificatore perfetto.
Così i programmatori scrivono programmi
più facili da verificare.

<!-- S52 -->
Il trucco più semplice è stabilire un ordine.
Ogni operazione deve bloccare l'account
prima dell'ordine.
Mai il contrario.

<!-- S53 -->
Se ogni operazione rispetta davvero quell'ordine,
il ciclo non può formarsi,
e questo tipo di deadlock non può avvenire.

<!-- S54 -->
Altri sistemi rinunciano dopo un timeout,
prendono tutti i loro lock in una volta sola,
oppure lasciano che il database scelga una vittima
e semplicemente riprovano.

<!-- S55 -->
E per progetti piccoli e descritti con cura,
ci sono strumenti che controllano ogni stato possibile.
Alcuni ingegneri di Amazon ne hanno usato uno
per trovare un bug che richiedeva trentacinque passi,
esattamente nell'ordine giusto, per manifestarsi.

<!-- S56 -->
Questi strumenti funzionano
perché il problema è stato reso più piccolo.
Controllano un modello del sistema,
non ogni programma che potrebbe mai esistere.

<!-- S57 -->
Con il codice reale, però,
un verificatore che accetta qualsiasi programma
deve rinunciare a qualcosa.
Può segnalare deadlock
che non possono verificarsi,
lasciarsene sfuggire alcuni che invece possono verificarsi,
o a volte non dare alcuna risposta.

<!-- S58 -->
Un verificatore che non dia mai falsi allarmi,
non si lasci sfuggire nessun deadlock
e dia sempre una risposta,
per ogni programma,
è esattamente ciò che Turing ha escluso.

<!-- S59 -->
Torniamo all'incrocio:
i quattro automobilisti non restano lì per sempre.

<!-- S60 -->
Qualcuno fa un cenno con la mano.
Un automobilista rinuncia al suo turno,
e in pochi secondi tutto si sblocca.

<!-- S61 -->
È quello che fa anche il database.
Non prevede il deadlock.
Se ne accorge
e costringe qualcuno a cedere il passo.

<!-- S62 -->
Alcuni problemi hanno bisogno di un computer più veloce.
Altri di un'idea migliore.

<!-- S63 -->
E alcuni, come questo,
non hanno proprio una soluzione perfetta.
Solo buone regole
e qualcuno pronto a fare un cenno.
