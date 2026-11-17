<!-- S01 -->
Ecco tutti i copioni
mai scritti per questo canale.
158 video,
quasi un milione e mezzo di byte di testo.

<!-- S02 -->
Passateli in un normale compressore
chiamato gzip.
Ne esce poco più di mezzo megabyte.
Quasi due terzi spariti.

<!-- S03 -->
E non si perde nulla.
Decomprimete il file,
e ogni copione torna indietro,
lettera per lettera.

<!-- S04 -->
Ora comprimetelo di nuovo.

<!-- S05 -->
Diventa più grande.
Di 98 byte più grande.

<!-- S06 -->
Una terza volta.
Di 98 byte più grande.
Una quarta.
Di nuovo 98.

<!-- S07 -->
Il primo giro butta via due terzi.
Il secondo non trova proprio niente.
Perché allora non continuare a comprimere?

<!-- S08 -->
Guardiamo dentro quel secondo file.
gzip non ha compresso nulla.
Ha copiato i dati così com'erano,
in sedici blocchi.

<!-- S09 -->
Ogni blocco ha un'etichetta di cinque byte.
Aggiungete una piccola intestazione e una coda,
e si arriva esattamente a 98.

<!-- S10 -->
Quando un compressore non trova niente da togliere,
salva i dati così come sono,
e aggiunge solo ciò che serve per ripristinarli.

<!-- S11 -->
Allora perché il secondo giro non ha trovato niente?
E un programma più furbo ci riuscirebbe?

<!-- S12 -->
Un testo come questo è pieno di ripetizioni.
Le stesse parole, le stesse frasi,
gli stessi piccoli marcatori
in cima a ogni scena.

<!-- S13 -->
Nel 1977, Jacob Ziv e Abraham Lempel
pubblicarono un trucco semplice.
Non riscrivete una ripetizione.
Rimandate a dove compariva prima.

<!-- S14 -->
Tornate indietro di 300 caratteri
e copiate i dodici successivi.
Pochi byte invece di dodici.

<!-- S15 -->
Il secondo trucco:
dare codici brevi alle lettere frequenti
e codici lunghi a quelle rare.

<!-- S16 -->
Nel 1951, David Huffman,
studente di dottorato al MIT,
poteva scegliere: l'esame finale
oppure, al suo posto, una tesina.

<!-- S17 -->
La tesina, assegnata da Robert Fano,
chiedeva di trovare il codice più efficiente
proprio di questo tipo.

<!-- S18 -->
Per mesi, Huffman non approdò a nulla.
Si arrese
e cominciò a studiare per l'esame.
Poi gli venne l'idea.

<!-- S19 -->
Prendete i due simboli più rari,
uniteli in uno solo
e ripetete finché non resta un unico albero.

<!-- S20 -->
In seguito lo definì
«il momento più singolare della mia vita».

<!-- S21 -->
Fano non aveva detto alla classe
che ci si era scervellato anche lui,
e così pure Claude Shannon.

<!-- S22 -->
Il codice di Huffman batté i metodi di entrambi.
E si può dimostrare
che nessun codice del genere fa di meglio.

<!-- S23 -->
All'inizio degli anni '90,
Phil Katz mise insieme i due trucchi
per i file ZIP.
gzip usa lo stesso metodo.

<!-- S24 -->
Il primo giro ha già esaurito
le regolarità che gzip sa trovare.

<!-- S25 -->
Quel che resta non gli dà nulla su cui lavorare.
Per gzip, sembra rumore.

<!-- S26 -->
Ma un programma più furbo
potrebbe vedere regolarità sfuggite a gzip.
Potrebbe un programma, un giorno,
rimpicciolire qualunque cosa gli diate?

<!-- S27 -->
No.
E non serve sapere come funziona
per esserne sicuri.

<!-- S28 -->
Prendete tutti i file
lunghi esattamente tre bit.
Sono otto.

<!-- S29 -->
Ora contate tutti quelli più corti.
Quattro file da due bit,
due da un bit
e un file vuoto.

<!-- S30 -->
Sette.

<!-- S30b -->
Otto file e sette posti più corti
dove metterli.

<!-- S31 -->
Se ognuno si accorciasse,
due dovrebbero condividere un posto.
E quando lo decomprimete,
quale dei due intendevate?

<!-- S32 -->
Si chiama principio dei cassetti,
e vale per qualsiasi lunghezza.
C'è sempre un file più corto in meno
di quanti ne servirebbero.

<!-- S33 -->
Quindi ogni compressore che accetta qualsiasi file
e ne rimpicciolisce alcuni
deve ingrandirne altri.
Non perché sia scritto male.
Non c'è nessun altro posto dove metterli.

<!-- S34 -->
Quei 98 byte
sono il prezzo che paga gzip.

<!-- S35 -->
Scegliete un compressore qualsiasi.
Di tutti i file di una data dimensione,
ne può ridurre di un solo byte meno di uno
su 250.

<!-- S36 -->
La compressione funziona comunque,
perché i file che creiamo non sono casuali.
Sono testi, immagini e programmi,
pieni di regolarità.

<!-- S37 -->
Questo non ha impedito a qualcuno
di promettere di più.

<!-- S38 -->
Nel 1992, la WEB Technologies
annunciò un software capace di comprimere
quasi qualsiasi dato sotto un kilobyte.
Anche il proprio output,
ancora e ancora.

<!-- S39 -->
Il suo vicepresidente disse che il metodo
«non era soggetto alle leggi
della teoria dell'informazione».
Il prodotto non uscì mai.

<!-- S40 -->
Allora come fanno foto e musica
a diventare così piccole?
Non seguono affatto questa regola.

<!-- S41 -->
Un JPEG non torna identico.
Torna abbastanza simile.
I dettagli di cui l'occhio non sentirà la mancanza
vengono buttati via per sempre.

<!-- S42 -->
Ingrandite
e vedrete dove sono finiti.

<!-- S43 -->
Questa è la compressione con perdita,
ed è tutto un altro gioco.
Questo video parla dell'altro tipo.
Ogni bit torna identico.

<!-- S44 -->
E per i file che hanno regolarità,
quanto possono diventare piccoli?
C'è un minimo?

<!-- S45 -->
Sì.
Fu trovato nel 1948,
nello stesso articolo alla base del nostro video
sui codici a correzione d'errore.

<!-- S46 -->
Lì, Claude Shannon mostrò
come aggiungere ridondanza protegge un messaggio.
Qui, calcolò
quanta se ne può togliere.

<!-- S47 -->
La sua risposta fu un numero
che chiamò entropia:
quanto è difficile indovinare
cosa viene dopo.

<!-- S48 -->
Nessun codice senza perdita scende sotto quel numero
in media.
Ma ci si può avvicinare
quanto si vuole.

<!-- S49 -->
Allora, quanto è imprevedibile l'inglese?
Nel 1951, Shannon lo misurò
con un gioco.

<!-- S50 -->
Diede a una persona un brano
che non aveva mai visto,
e le chiese di indovinarlo,
lettera per lettera.

<!-- S51 -->
Se sbagliava,
ritentava,
finché non indovinava.

<!-- S52 -->
Si scoprì che le persone sono bravissime.
Con cento lettere di contesto,
l'inglese arrivava a circa un bit
per lettera.

<!-- S53 -->
Un computer memorizza ogni lettera
in otto bit.
A un lettore umano ne basta circa uno.

<!-- S54 -->
È questo divario che sfrutta la compressione.
gzip ha portato i copioni del canale
sotto i tre bit per carattere.

<!-- S55 -->
Allora quanto vicino a un bit
può arrivare una macchina?

<!-- S56 -->
C'è un premio proprio per questo.
Si chiama Hutter Prize,
e dal 2020 la sfida è comprimere un unico file:
un gigabyte della Wikipedia inglese.

<!-- S57 -->
gzip lo riduce a un terzo.
I migliori compressori di uso comune,
a circa un quinto.

<!-- S58 -->
Il record, stabilito a luglio 2026,
è di poco più di cento milioni di byte.
Un decimo.

<!-- S59 -->
E conta anche il decompressore.
La sua dimensione si somma al totale,
quindi non si può nascondere Wikipedia
dentro il programma.

<!-- S60 -->
Il fondo è di 500.000 euro.
Ogni miglioramento dell'uno per cento
ne frutta 5.000.

<!-- S61 -->
Marcus Hutter, che lo finanzia, spiega perché:
«saper comprimere bene
è strettamente legato
all'agire in modo intelligente».

<!-- S62 -->
Perché i programmi in vetta
non vanno a caccia di ripetizioni.
Prevedono.

<!-- S63 -->
Prima di ogni carattere,
stimano quanto è probabile
ogni possibile carattere successivo.
Una buona previsione costa una frazione di bit.

<!-- S64 -->
È il gioco delle previsioni di Shannon,
giocato da una macchina.
I migliori giocatori oggi usano reti neurali,
addestrate a prevedere cosa viene dopo.

<!-- S65 -->
Funziona anche su file già compressi.
Nel 2016, Dropbox iniziò a ricomprimere
i JPEG dei suoi utenti con un predittore migliore.
In media, oltre un quinto più piccoli.

<!-- S66 -->
Ogni file tornava identico bit per bit,
e entro il 2017
aveva fatto risparmiare oltre 46 petabyte.
Cioè oltre 46.000 terabyte.

<!-- S67 -->
Poi ci sono i giganti.
Nel 2023, i ricercatori di DeepMind
usarono un grande modello linguistico
come compressore.

<!-- S68 -->
Su piccoli ritagli di foto in scala di grigi,
batté il PNG:
il 48% della dimensione originale
contro il 58.

<!-- S69 -->
Su registrazioni di testi letti ad alta voce,
batté il FLAC:
21% contro 30.

<!-- S70 -->
Ma questo senza contare il modello.
Aggiungete la sua dimensione,
e il risultato viene
140 volte
più grande dei dati.

<!-- S71 -->
Un compressore più grande dei suoi dati
non ha risparmiato niente.
Il programma fa parte della descrizione.

<!-- S72 -->
E questo ci porta alla parte più strana.
Ecco il primo milione di cifre di pi greco.

<!-- S73 -->
Datele a quattro compressori.
Il migliore le riduce a circa
426.000 byte.

<!-- S74 -->
Ora date agli stessi compressori
un milione di cifre casuali.
Stesso risultato,
con uno scarto inferiore allo 0,1%.

<!-- S75 -->
Ma pi greco non nasce a caso.
Segue una regola matematica.
Ecco un programma che stampa
ognuna di quel milione di cifre.

<!-- S76 -->
362 byte.
Oltre duemila volte più corto del file.

<!-- S77 -->
I compressori non potevano vedere
la regola matematica dietro pi greco.
Vedevano solo le cifre.

<!-- S78 -->
Un modo per misurare l'informazione
contenuta nei dati è chiedersi:
quanto può essere corto un programma
che riesca ancora a stamparli?

<!-- S79 -->
Quella lunghezza si chiama
complessità di Kolmogorov,
dal nome di uno di coloro che la descrissero.

<!-- S80 -->
La maggior parte dei dati non ha un programma corto.
È di nuovo il principio dei cassetti:
non ci sono abbastanza programmi corti
per tutti.

<!-- S81 -->
Un milione di cifre casuali
molto probabilmente non ha niente di più corto.
Pi greco sì.

<!-- S82 -->
Allora perché non trovare semplicemente
il programma più corto per qualsiasi file?
Perché è stato dimostrato
che nessun algoritmo può farlo
per ogni file.

<!-- S83 -->
Ogni programma vi dà un limite superiore.
Ma niente può sempre dirvi
se ne esiste uno più corto.
Non sapete mai se avete raggiunto il minimo.

<!-- S84 -->
gzip ha trovato le ripetizioni nei copioni,
e nient'altro.
Vede byte,
non il significato delle parole.

<!-- S85 -->
Per andare oltre, un programma
deve saperle prevedere meglio.
E prevedere bene un testo
comincia ad assomigliare molto a capirlo.

<!-- S86 -->
Ecco allora una domanda per voi.
Se un programma riuscisse a comprimere Wikipedia
più di qualsiasi altro,
direste che la capisce?
Lasciate la vostra risposta nei commenti.
