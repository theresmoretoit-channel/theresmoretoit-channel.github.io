<!-- S01 -->
Provi a cancellare un file.
Il computer dice che è aperto
in un altro programma.
Ma non dice quale.

<!-- S02 -->
Quel messaggio è la punta visibile
di una domanda molto più strana.
Che cosa vuol dire davvero
aprire un file?

<!-- S03 -->
Perché su un altro computer
lo stesso file, aperto nello stesso modo,
si cancella senza una protesta.

<!-- S04 -->
Stesso file.
Stessa azione.
Due risposte del tutto diverse.

<!-- S05 -->
Partiamo dalla parte
che dà fastidio a tutti.
Quale programma?

<!-- S06 -->
Windows lo sa.
Ha un oggetto del kernel
per quel file aperto
e sa quale processo lo possiede.
Potrebbe dirne il nome.

<!-- S07 -->
Così chiudi cose a caso.
Apri Gestione attività.
Fissi un elenco di processi
e non ne riconosci quasi nessuno.

<!-- S08 -->
E per anni
la risposta è stata davvero
scaricare uno strumento a parte.
Unlocker è uscito nel 2005,
e su Windows XP quella era la risposta.

<!-- S09 -->
Poi Windows 7 ha portato
il Monitoraggio risorse.
La scheda CPU.
Un elenco chiamato Handle associati.

<!-- S10 -->
Digita il nome del file.
Ti dà il programma
e l'identificativo del processo.
Niente da installare.
È lì dal 2009.

<!-- S10b -->
Ma gli strumenti a parte facevano
più che dirtelo soltanto.
Sapevano chiudere l'handle
e liberare il file.

<!-- S11 -->
Il che ci riporta
alla domanda.
Che cosa ha ottenuto quel programma
aprendo il file?

<!-- S12 -->
Mettiamo che un lettore apra
un file chiamato movie.mp4.
Su Windows, aprire un file
vuol dire specificare due cose.

<!-- S13 -->
La prima è ovvia.
Che cosa ci voglio fare?
Leggerlo. Scriverci.

<!-- S14 -->
La seconda è quella interessante.
Che cosa possono fare gli altri
mentre io lo tengo aperto?

<!-- S15 -->
È proprio un'impostazione.
Dici che cosa possono fare
gli altri programmi mentre lo tieni.

<!-- S16 -->
Possono leggerlo.
Possono anche scriverci.
Possono cancellarlo o rinominarlo.

<!-- S16b -->
Oppure niente.
Nessuno lo tocca
finché lo sto usando io.

<!-- S17 -->
Il flag che permette di cancellare
si chiama FILE_SHARE_DELETE.
E la documentazione di Microsoft
aggiunge una riga sotto.

<!-- S18 -->
Il permesso di cancellare copre
cancellazione e rinomina insieme.

<!-- S19 -->
Quindi un programma che rifiuta
la condivisione per la cancellazione
ha bloccato anche la rinomina.

<!-- S20 -->
E se il programma che ha aperto il file
non l'ha concessa,
nessun altro può ottenerla.

<!-- S21 -->
Ecco perché l'errore
non si chiama file in uso.
Si chiama violazione di condivisione.

<!-- S22 -->
La risposta era nel nome
dell'errore
per tutto il tempo.

<!-- S23 -->
Ora la stessa cosa
su una macchina Linux.
Un lettore apre il video.

<!-- S24 -->
E tu digiti
rm movie.mp4.

<!-- S24b -->
Funziona.
Il video continua a riprodursi.

<!-- S25 -->
Che cosa ha preso allora quel programma,
se non un controllo sul file?

<!-- S26 -->
Questo è il punto
centrale del video.
Il nome non è il file.

<!-- S27 -->
movie.mp4 è una riga
in una directory.
Quella riga punta a un oggetto
che contiene i dati veri.

<!-- S28 -->
Quando un programma apre il file,
quello che ottiene è un riferimento
all'oggetto.
Non alla riga.

<!-- S29 -->
Cancellare il file
elimina quindi la riga.
L'oggetto resta intatto.

<!-- S30 -->
La pagina del manuale lo dice
in una sola frase.
Il file continuerà a esistere
finché non si chiude l'ultimo
descrittore che vi fa riferimento.

<!-- S31 -->
Sembra astratto
finché non lo si vede accadere.
Così ho creato un file di log
da cinquecento megabyte
e lasciato un processo a tenerlo aperto.

<!-- S31b -->
Poi l'ho cancellato.

<!-- S32 -->
L'elenco della directory
non mostra proprio nulla.
Lo strumento che misura
la dimensione della cartella dice zero.

<!-- S33 -->
E lo strumento che misura
lo spazio libero sul disco
dice che cinquecento megabyte
mancano ancora.

<!-- S33b -->
Una cartella vuota.
Mezzo gigabyte sparito.

<!-- S34 -->
Succede abbastanza spesso
da esserci un comando
solo per trovare file così.
Cancellati, invisibili, ancora sul disco.

<!-- S35 -->
E lo spazio torna
nell'istante in cui quel processo
rilascia il file.

<!-- S36 -->
La stessa logica vale per la rinomina.
Sposta il file mentre è aperto,
e il programma non se ne accorge.

<!-- S37 -->
Anche lì il manuale è netto.
I descrittori già aperti
non ne risentono.

<!-- S37b -->
Non stava mai usando il nome.

<!-- S38 -->
Ma c'è un limite
che vale la pena conoscere.
Un programma in esecuzione
non si può sovrascrivere sul posto.

<!-- S38b -->
Linux non te lo permette.
Text file busy.

<!-- S39 -->
Quello che puoi fare
è staccare il nome
e metterci un file nuovo.

<!-- S40 -->
Il vecchio processo continua a usare
un oggetto
che non ha più nessun nome.
Tutto ciò che viene avviato dopo usa quello nuovo.

<!-- S41 -->
È di nuovo la stessa idea
che si dimostra da sola.
Molte cose si sostituiscono
senza toccare l'oggetto sul posto.

<!-- S41b -->
Per questo Linux può aggiornare
un programma mentre è in esecuzione.
Solo che la versione nuova arriva
quando lo riavvii.

<!-- S42 -->
Windows è dunque
semplicemente progettato peggio?

<!-- S42b -->
No.
Ed è questa la parte
che quasi nessuno conosce.

<!-- S43 -->
Windows ha un modo
di fare esattamente la stessa cosa.

<!-- S43b -->
Su NTFS, Windows può chiedere
una cancellazione in stile POSIX.

<!-- S44 -->
Microsoft descrive
che cosa succede allora.
Il nome viene rimosso
dallo spazio dei nomi visibile.

<!-- S45 -->
E le applicazioni che avevano già
il file aperto possono ancora usarlo,
anche se il nome
con cui l'hanno aperto non c'è più.

<!-- S46 -->
È il comportamento di Unix.
Su NTFS.
Documentato da Microsoft.

<!-- S47 -->
Entrambi i sistemi sanno fare entrambe.
A cambiare è l'impostazione predefinita.
Quello che ottieni aprendo un file
senza pensarci.

<!-- S48 -->
Su Windows ottieni un contratto.
Su Unix ottieni un riferimento
a un oggetto.

<!-- S49 -->
Il che suona come una domanda
da programmatori,
finché non hai visto
proprio questo messaggio.

<!-- S50 -->
Riavvia il computer
per completare l'installazione degli aggiornamenti.

<!-- S51 -->
Supponiamo che Windows debba sostituire
una libreria che un processo
tiene aperta sotto il contratto rigido.

<!-- S52 -->
Non può scambiare il file
sotto quel processo.
Quindi qualcosa deve mollare.

<!-- S53 -->
Chiudere l'applicazione.
Fermare il servizio.
O affidare tutto il lavoro
a Gestione riavvio.

<!-- S54 -->
Che è un componente vero.
Spegne le cose in ordine.
Le applicazioni Windows,
poi i programmi da console,

<!-- S55 -->
poi i servizi,
e Esplora file per ultimo.
Poi le riavvia.

<!-- S56 -->
Ed esiste per un solo motivo,
che Microsoft dice chiaramente
nella propria documentazione.

<!-- S57 -->
Il motivo principale
per cui le installazioni
e gli aggiornamenti richiedono
un riavvio del sistema...

<!-- S58 -->
è che alcuni dei file
in aggiornamento sono in quel momento
usati da un'applicazione
o da un servizio in esecuzione.

<!-- S59 -->
Sarebbe troppo pulito finire qui.
Le regole di condivisione non sono l'unico
motivo per cui un computer chiede il riavvio.

<!-- S60 -->
Un aggiornamento del kernel è altro.
Il kernel non si sostituisce
sotto se stesso.

<!-- S61 -->
Linux ha lo stesso problema,
anche se le patch a caldo
a volte evitano il riavvio.

<!-- S62 -->
Quindi la versione onesta
afferma meno di
quella soddisfacente.

<!-- S63 -->
Il modo in cui Windows tratta i file
in uso ha reso alcuni componenti
più difficili da sostituire a caldo,
e questo ha contribuito.

<!-- S64 -->
Perché ogni scelta di progetto
ha una conseguenza da qualche parte.

<!-- S65 -->
Windows lascia decidere al programma
che apre un file
che cosa possono farne gli altri.

<!-- S66 -->
Il prezzo è che a volte
non puoi cancellare un tuo file,
perché un altro programma
non l'ha permesso.

<!-- S67 -->
Unix tiene il nome
e l'oggetto separati,
così molte cose si sostituiscono
mentre il sistema è in funzione.

<!-- S68 -->
Il prezzo è mezzo gigabyte
sparito dal disco
che non appartiene a nessun file.

<!-- S69 -->
E guarda come si risolve
ciascuna delle due.
Su Windows, una via d'uscita è
chiudere il programma
che tiene il file.

<!-- S70 -->
Su Linux, un modo
per riavere quello spazio
è riavviare il servizio
che tiene ancora aperto il file.

<!-- S71 -->
Cause diverse.
A volte lo stesso rimedio.

<!-- S71b -->
A proposito, se vuoi vedere
dove ci porta la prossima domanda,
valuta di iscriverti.
Aiuta molto il canale.

<!-- S72 -->
Dunque. La domanda dell'inizio.
Che cosa vuol dire
aprire un file?

<!-- S73 -->
Vuol dire che stai tenendo qualcosa.
I due sistemi ti danno
semplicemente cose diverse da tenere.

<!-- S74 -->
Ecco perché quel messaggio
non ha mai detto davvero
che il file non si può cancellare.

<!-- S75 -->
Diceva che il programma
che l'ha aperto
non te l'ha permesso.

<!-- S75b -->
E sa quale programma è.
Solo che non l'ha detto.
