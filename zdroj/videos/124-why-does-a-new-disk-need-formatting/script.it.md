<!-- S01 -->
Compri un disco nuovo di zecca.
Un terabyte, completamente vuoto.
Prima di poterci salvare un solo file,
bisogna formattarlo.

<!-- S02 -->
Allora lo formatti in ext4,
il file system standard
di molti computer con Linux.
Con le impostazioni predefinite,
prima ancora di aver salvato qualcosa,
sono già spariti circa diciassette gigabyte.

<!-- S03 -->
Non è ancora stato salvato niente.
Niente foto, niente documenti.
E allora cosa occupa tutto quello spazio?

<!-- S04 -->
E perché mai un disco va formattato,
tanto per cominciare?
Sa già memorizzare dati.
Sa leggere e scrivere migliaia di miliardi di bit.

<!-- S05 -->
Perché il computer non può semplicemente scrivere
dove c'è posto?

<!-- S06 -->
Perché salvare i dati
e poi ritrovarli
sono due problemi molto diversi.

<!-- S07 -->
Immagina un ufficio che distribuisce
fogli bianchi invece di moduli.
Tutto finisce scritto da qualche parte...
e nessuno trova più niente.

<!-- S08 -->
Un disco senza file system
è quella pila di fogli.
Un'immagine migliore, però,
è un quaderno.

<!-- S09 -->
Immagina un quaderno
di mille pagine,
e qualche regola per usarlo.

<!-- S10 -->
Primo, ogni pagina ha un numero.
Così ogni punto del quaderno
ha un indirizzo.
Pagina quattrocentododici
indica un solo posto preciso.

<!-- S11 -->
Secondo, le prime pagine
sono un indice.
Ogni voce riporta un nome
e la pagina in cui si trova.
Pancake: pagina dodici.

<!-- S12 -->
Terzo, proprio in fondo,
c'è un elenco delle pagine
ancora bianche.

<!-- S13 -->
Ora aggiungi una ricetta.
Cerchi in fondo una pagina bianca.
Ci scrivi la ricetta.
Aggiungi una riga all'indice.
E depenni quella pagina
dall'elenco delle pagine bianche.

<!-- S14 -->
Una ricetta, tre posti.
E tutti e tre devono coincidere.

<!-- S15 -->
Poi la ricetta dei pancake si allunga.
Pagina dodici è piena,
e la tredici è già occupata.
Quindi continua a pagina ottantasette,
e l'indice deve dirlo.

<!-- S16 -->
Ed ecco il problema.
Se vuoi spazio per mille voci
nell'indice,
devi riservare quelle pagine
prima di scrivere una sola ricetta.

<!-- S17 -->
Questa era l'analogia.
Ecco cosa c'è davvero sul disco.

<!-- S18 -->
Un disco non sa niente di file,
cartelle o nomi.
Offre solo una lunga fila
di caselle numerate, chiamate settori.

<!-- S19 -->
In un disco rigido,
i dati stanno su piatti che girano.
Un SSD li tiene in una memoria flash.
In ogni caso, il computer chiede sempre e solo
un settore tramite il suo numero,
e il disco capisce da solo dove si trova.

<!-- S20 -->
Un settore è piccolo.
Di solito 512 byte,
oppure 4096
sui dischi più recenti.

<!-- S21 -->
I file system di solito lavorano
con pezzi più grandi, chiamati blocchi.
In ext4 un blocco è di quattro kilobyte,
la dimensione di otto settori vecchio stile.

<!-- S22 -->
Quei blocchi numerati
sono le pagine del quaderno.
Al file system mancano ancora
le altre due parti:
un indice
e un elenco di ciò che è libero.

<!-- S23 -->
È questo che costruisce la formattazione.
Ed è lì
che sono finiti quei diciassette gigabyte.

<!-- S24 -->
Ext4 riserva un record
per ogni file e cartella
che il disco potrà contenere contemporaneamente.
Ogni record occupa
256 byte.
Si chiama inode.

<!-- S25 -->
Un giorno, ogni inode dirà
quanto è grande un file,
quando è stato modificato,
chi può aprirlo
e quali blocchi ne contengono i dati.

<!-- S26 -->
Su un disco da un terabyte,
ext4 ne prepara circa
sessantun milioni.
Tutti vuoti, tutti in attesa.
Sono quasi sedici gigabyte
di record vuoti.

<!-- S27 -->
Perché sessantun milioni?
Ext4 fa una stima semplice:
un inode ogni sedici kilobyte
di spazio sul disco.
Su un computer normale,
la maggior parte di quei record
non verrà mai usata.

<!-- S28 -->
Circa un altro gigabyte
va a un journal,
su cui torneremo.
Il resto è altra contabilità,
tra cui una mappa con un bit per blocco,
che dice se è usato o libero.

<!-- S29 -->
E anche quel numero è fisso.
Esaurisci tutti i record
con milioni di file minuscoli,
e il disco ti dirà che è pieno...
anche con gigabyte di spazio libero.

<!-- S30 -->
Allora vediamolo all'opera.
Creiamo un file chiamato hello.txt.
Dentro, una sola parola: hello.
Cinque lettere. Cinque byte.

<!-- S31 -->
Il file system sceglie un inode vuoto.
Diciamo il numero tredici.
Poi trova un blocco libero nella mappa
e lo segna come usato.

<!-- S32 -->
Scrive i cinque byte in quel blocco.
Poi compila l'inode:
lungo cinque byte, creato proprio ora,
e salvato in quell'unico blocco.

<!-- S33 -->
E infine, nella cartella,
aggiunge una riga:
il nome hello.txt
e il numero tredici.

<!-- S34 -->
Nota dove è finito il nome.
Non nel file.
Non nell'inode.
Il nome sta nella cartella,
che in realtà è solo un elenco
di nomi e numeri.

<!-- S35 -->
E una cartella è solo un altro file.
E quello che contiene, guarda caso,
è proprio quell'elenco.

<!-- S36 -->
Per questo, spostare un file
in un'altra cartella dello stesso file system
è istantaneo, per quanto grande sia.
Una cartella perde una riga,
l'altra ne guadagna una,
e di solito il contenuto
non si sposta affatto.

<!-- S37 -->
Cinque byte di testo...
e sul disco ne occupa
4096.
Un blocco è il pezzo più piccolo
che il file system assegna,
quindi anche un file minuscolo costa un blocco intero.

<!-- S38 -->
Quando il file non sta più nel suo blocco,
il file system ne trova un altro libero.
Magari proprio accanto.
Magari da tutt'altra parte.
E l'inode tiene traccia di entrambi.

<!-- S39 -->
Col tempo, un file grande può finire
a pezzi sparsi per tutto il disco.
Un disco rigido deve saltare da un pezzo all'altro.
Un SSD se la cava molto meglio.

<!-- S40 -->
Il programma che ha salvato il file
non sa niente di tutto questo.
Ha detto «salva hello.txt»,
e tutto il resto è successo dietro le quinte.

<!-- S41 -->
Ora cancellalo.
Il nome viene tolto dalla cartella.
L'inode viene segnato come libero.
Il blocco torna nell'elenco di quelli liberi.

<!-- S42 -->
Su un disco rigido tradizionale,
i cinque byte restano lì dove sono.
Nessuno li ha toccati.
Rimangono finché qualcosa di nuovo
non ci viene scritto sopra.

<!-- S43 -->
Ecco perché un file cancellato
a volte si può recuperare.
Di solito cancellare non elimina
il contenuto.
Segna solo lo spazio come disponibile.

<!-- S44 -->
Su un SSD è meno sicuro.
Il file system può dire al disco
che quei blocchi non servono più,
e il disco può scartarne il contenuto.
A quel punto è molto meno probabile
riuscire a recuperare il file.

<!-- S45 -->
Quindi un file system è in fondo un contabile.
Creare questo singolo file
ha voluto dire aggiornare tre cose:
la cartella, l'inode
e la mappa dei blocchi liberi.

<!-- S46 -->
Ora stacca la corrente
a metà del salvataggio di un file.

<!-- S47 -->
Magari il blocco è stato segnato come usato,
ma nessun inode punta ancora lì.
Quello spazio è semplicemente perso.
Fastidioso, ma innocuo.

<!-- S48 -->
Oppure l'inode punta a un blocco
che per la mappa è ancora libero.
Il file successivo può essere scritto
proprio sopra.
E il primo viene distrutto in silenzio.

<!-- S49 -->
Ecco perché ext4 tiene un journal.
Prima di modificare la sua contabilità,
annota cosa sta per fare.
Dopo un crash, ripete solo le modifiche
che aveva finito di annotare
e segnato come completate.
Tutto ciò che è incompiuto viene ignorato.

<!-- S50 -->
E c'è un problema più silenzioso.
A volte un disco cambia un bit
e non lo dice a nessuno.

<!-- S51 -->
Ext4 protegge i propri record
con dei checksum,
così lì può accorgersi dei danni.
Ma il contenuto dei tuoi file?
Di quello si fida e basta.

<!-- S52 -->
Alcuni file system controllano entrambi.
E alcuni tengono una seconda copia,
così, quando una copia si danneggia,
possono ripararla usando l'altra.
Accorgersi di un problema e risolverlo
non sono la stessa cosa.

<!-- S53 -->
Quindi ogni file system fa lo stesso lavoro:
blocchi numerati, un elenco di nomi
e una mappa di ciò che è libero.

<!-- S54 -->
Ma le scelte cambiano.
Ext4 prepara sessantun milioni di record
prima che tu salvi qualsiasi cosa.
NTFS, su Windows, tiene i suoi record
in un'unica grande tabella che cresce man mano.

<!-- S55 -->
E Btrfs non prepara
in anticipo una tabella fissa di inode.
Li crea man mano che arrivano i file.
E di norma non sovrascrive
i dati nella stessa posizione.
Scrive una copia nuova,
e solo dopo libera quella vecchia.

<!-- S56 -->
Di default calcola anche il checksum dei tuoi file,
così può capire quando sono stati danneggiati.

<!-- S57 -->
E siccome la copia vecchia
non viene sovrascritta,
uno snapshot può tenerla in vita.
Questo cambia la risposta
a quasi tutte le domande di questo video:
che effetto ha un crash,
cosa vuol dire cancellare,
e perfino cosa sia una copia.

<!-- S58 -->
È lì che comincia il prossimo video.

<!-- S59 -->
Allora, ecco una domanda per te.
Un file system dovrebbe solo conservare i tuoi file,
o anche proteggerli?
Fammelo sapere nei commenti.
