<!-- S01 -->
Novecentonovantanove sterline
e novantanove pence.
Aggiungi un penny.

<!-- S02 -->
Il risultato è zero.

<!-- S03 -->
Nessun messaggio di errore. Nessun crash.
Solo zero, scritto in silenzio sul conto.

<!-- S04 -->
In COBOL, quando il campo per un risultato
è troppo piccolo per contenerlo,
la cifra in più può semplicemente sparire.
A meno che il programma non chieda un avviso,
il calcolo va avanti.

<!-- S05 -->
E non arrotonda nemmeno.
Due sterline e trentaquattro pence e mezzo,
memorizzate con la precisione di un penny,
diventano due sterline e trentaquattro.

<!-- S06 -->
Scrivi una sola parola in più, ROUNDED,
e diventano due sterline e trentacinque.

<!-- S07 -->
Nessuna delle due cose è un bug.
Sono regole.
E molte banche nel mondo
funzionano ancora con regole come queste.

<!-- S08 -->
Il COBOL è un linguaggio di programmazione
del 1959.
Non tutti i programmi scritti in COBOL sono così vecchi.
Ma il linguaggio sì,
e anche le sue abitudini.

<!-- S09 -->
Allora perché le banche non l'hanno sostituito?
I soldi ce li hanno.
Gli ingegneri anche.

<!-- S10 -->
Per scoprirlo, vediamo tre casi reali.
Una banca che ha provato a lasciare il suo vecchio sistema,
una che ci è riuscita,
e una crisi in cui tutti hanno dato la colpa al COBOL.

<!-- S11 -->
Ma prima, quel mezzo penny mancante.

<!-- S12 -->
Mettiamo che tu riscriva quel programma bancario
in un linguaggio moderno.
Probabilmente correggeresti quelle regole.
L'overflow diventa un errore.
Il mezzo penny viene arrotondato per eccesso.

<!-- S13 -->
Più pulito. Più sicuro.
E ora, ovunque spunti mezzo penny,
il tuo programma non dà più lo stesso risultato di quello vecchio.

<!-- S14 -->
I linguaggi moderni sanno fare calcoli decimali esatti.
Java ha un tipo fatto apposta.
Ma anche lì,
la regola di arrotondamento è una scelta.

<!-- S15 -->
Un'impostazione comune, a metà esatta, arrotonda per eccesso:
due e trentacinque.
Un'altra arrotonda alla cifra pari più vicina:
due e trentaquattro.
Sono giuste entrambe. Solo una coincide.

<!-- S16 -->
E con la normale virgola mobile,
quella che la maggior parte del codice usa di default,
diventa ancora più strano.
Zero virgola uno più zero virgola due
non fa zero virgola tre.

<!-- S17 -->
Quindi sostituire il COBOL non è una traduzione.
È trovare ogni regola di questo tipo,
in milioni di righe,
e mantenerla esattamente com'era.

<!-- S18 -->
Ma come ci è finito, lì, il COBOL?

<!-- S19 -->
Nel maggio 1959
il Dipartimento della Difesa degli Stati Uniti
convocò una riunione al Pentagono.
Vennero produttori di computer, enti pubblici
e grandi aziende,
tutti con lo stesso problema.

<!-- S20 -->
Ogni computer aveva il suo linguaggio.
Un programma paghe scritto per una macchina
era inutile su un'altra.

<!-- S21 -->
Un comitato progettò un linguaggio comune
per le aziende.
L'influenza maggiore fu FLOW-MATIC,
del team di Grace Hopper alla Remington Rand.

<!-- S22 -->
E nel dicembre 1960
praticamente lo stesso programma COBOL
girò su due computer
di produttori rivali.
Era proprio questo lo scopo.

<!-- S23 -->
Era pensato perché le persone potessero seguirlo.
ADD PAYMENT TO ACCOUNT-BALANCE.
Probabilmente riesci a intuire cosa fa.

<!-- S24 -->
E memorizzava il denaro come lo scrive la gente:
in cifre decimali.
La virgola
non deve nemmeno essere memorizzata.
La descrizione del campo dice dove va:
le ultime due cifre sono i pence.

<!-- S25 -->
Nel 1964 IBM lanciò il System/360.
Il suo progetto includeva istruzioni
per l'aritmetica decimale.

<!-- S26 -->
E da allora IBM progetta i suoi mainframe
perché restino compatibili.
Molti programmi più vecchi possono ancora girare
sulle macchine di oggi
senza essere riscritti.

<!-- S27 -->
Così raramente c'è stato un momento
che costringesse qualcuno a cambiare.
Ogni anno il codice continuava a funzionare,
e ogni anno accumulava altre regole.
Nuovi prodotti, nuove tasse, nuove normative,
nuove eccezioni.

<!-- S28 -->
Nessuno ha contato quanto COBOL
giri ancora nel mondo.
Ma IBM dice che quarantacinque
delle cinquanta banche più grandi del mondo
usano ancora i suoi mainframe.

<!-- S29 -->
E alcuni proprietari hanno contato.
Nel 2017, l'ente previdenziale americano
ha dichiarato che i suoi sistemi contenevano
oltre sessanta milioni di righe di COBOL.

<!-- S30 -->
Nel 2025, i revisori del governo americano
hanno elencato gli undici sistemi federali
che avevano più bisogno di essere sostituiti.

<!-- S31 -->
Avevano tra i ventitré
e i sessant'anni,
e farli funzionare costava circa settecentocinquanta
milioni di dollari l'anno.

<!-- S32 -->
Quindi il codice è vecchio, è ovunque,
ed è pieno di regole che nessuno ha messo per iscritto.
Di sicuro il pericolo sta nel tenerlo.

<!-- S33 -->
Vediamo cosa succede
quando una banca se ne va.

<!-- S34 -->
Nel 2018 una banca britannica chiamata TSB
aveva circa cinque milioni di clienti,
e un problema.

<!-- S35 -->
I suoi sistemi erano in affitto
dal Lloyds Banking Group,
un concorrente,
e le tariffe stavano per salire di molto.

<!-- S36 -->
Così TSB decise di trasferire tutto
su una nuova piattaforma,
costruita dal suo nuovo proprietario,
la banca spagnola Sabadell.

<!-- S37 -->
Un fine settimana di aprile.
La domenica sera
il nuovo sistema fu acceso.

<!-- S38 -->
Il lunedì ci furono circa
novecentomila tentativi di accesso.
Solo un accesso all'internet banking
su dieci, circa, andò a buon fine.

<!-- S39 -->
I pagamenti fallivano.
Alcuni clienti entrarono
e videro i conti di altre persone.

<!-- S40 -->
Il peggio durò circa una settimana.
TSB tornò alla piena normalità
solo a dicembre.

<!-- S41 -->
Le conseguenze costarono circa
trecentotrenta milioni di sterline
solo nel 2018.
Più tardi le autorità di vigilanza aggiunsero
quasi quarantanove milioni di multe.

<!-- S42 -->
Ed ecco la parte strana.
I dati dei clienti arrivarono intatti.
Lo dicono entrambi i rapporti ufficiali.

<!-- S43 -->
A cedere fu la nuova piattaforma attorno ai dati.
Due data center, configurati in modo diverso.
Prestazioni testate solo su uno dei due,
e obiettivi abbassati
dopo che i test non erano stati superati.

<!-- S44 -->
E non si poteva tornare indietro.
Una volta spostati i dati,
tornare al vecchio sistema era,
con le parole dell'autorità di vigilanza,
«sostanzialmente impossibile».

<!-- S45 -->
TSB non stava fuggendo da un sistema guasto.
Stava lasciando un sistema che funzionava,
per via di chi lo possedeva
e di quanto costava.
Il pericolo era andarsene.

<!-- S46 -->
Quindi andarsene è sempre un disastro?

<!-- S47 -->
Nel 2008 la Commonwealth Bank australiana
si mise a sostituire i sistemi centrali
che l'avevano servita
per più di quarantacinque anni.

<!-- S48 -->
Il piano: circa cinquecentottanta
milioni di dollari australiani,
e quattro anni.

<!-- S49 -->
Ce ne vollero cinque.
In seguito la stampa stimò il totale
in circa un miliardo e cento milioni,
man mano che il progetto si allargava.

<!-- S50 -->
Ma non trasferì tutto
in un solo fine settimana.
Prima i conti di deposito, nel 2010.
Poi i conti aziendali, nel 2011,
e i prestiti nel 2012.

<!-- S51 -->
Ogni passo era qualcosa che la banca
poteva osservare, verificare e da cui imparare
prima di puntare sul successivo.

<!-- S52 -->
Alla fine, dice la banca,
è diventata la prima grande banca australiana
con servizi bancari in tempo reale,
giorno e notte.

<!-- S53 -->
Quindi si può fare.
Ma guarda cosa ha richiesto.
Cinque anni, un conto molto più salato,
e pazienza.

<!-- S54 -->
Modernizzare non è un acquisto.
È un progetto,
con i suoi rischi.

<!-- S55 -->
E ora la crisi
in cui tutti diedero la colpa al COBOL.

<!-- S56 -->
Marzo 2020.
Mentre la pandemia fermava il New Jersey,
le nuove domande di disoccupazione schizzarono
da meno di diecimila in una settimana
a oltre centocinquantacinquemila.

<!-- S57 -->
Sedici volte tante,
in sette giorni.
L'ufficio per la disoccupazione non teneva il passo.

<!-- S58 -->
A inizio aprile il governatore
chiese volontari.
Non solo operatori sanitari,
ma anche persone che conoscessero il COBOL.
I sistemi dello Stato, disse,
avevano più di quarant'anni.

<!-- S59 -->
La storia si diffuse in fretta.
Un codice antiquato era crollato
sotto il peso della pandemia.

<!-- S60 -->
Ma quando il revisore dello Stato
esaminò la questione in seguito,
non trovò alcuna prova
che i ritardi fossero stati causati
dai sistemi informatici.

<!-- S61 -->
Per conto loro, alcuni giornalisti che esaminarono
i messaggi di errore che la gente vedeva
ne ricondussero molti al sito web usato dagli utenti,
scritto in un linguaggio molto più recente, Java.
Il vecchio codice alle sue spalle continuava a girare.

<!-- S62 -->
Allora perché lo Stato aveva bisogno di programmatori COBOL?
Perché il Congresso stava cambiando le regole.
Nuovi sussidi, nuovi importi,
nuove persone aventi diritto,
e ogni modifica doveva entrare
nel codice, in fretta.

<!-- S63 -->
Il problema non era che il codice fosse vecchio.
Era che poche persone sapevano modificarlo,
e che anche le linee telefoniche erano intasate
e il personale sommerso.

<!-- S64 -->
Tre casi.
Una banca che ha lasciato un sistema che ancora funzionava,
e la cui migrazione è fallita.
Una banca che se n'è andata con cautela,
e ci è riuscita.
E una crisi in cui si è data la colpa al vecchio codice,
e nessuno ha potuto dimostrare che fosse la causa.

<!-- S65 -->
Questo non significa che i vecchi sistemi non cedano mai.
Cedono eccome.
Diventano costosi,
chi li capisce va in pensione,
e anche aspettare ha un costo.

<!-- S66 -->
Ma l'età si vede facilmente,
i rischi veri no.
Regole che nessuno ha messo per iscritto.
Conoscenze nella testa di poche persone.
E il momento del passaggio.

<!-- S67 -->
Per questo molte banche non sostituiscono
il vecchio nucleo in un colpo solo.
Lo avvolgono.
L'app sul tuo telefono è nuova,
ma forse sta parlando con qualcosa
di molto più vecchio.

<!-- S68 -->
E lo sostituiscono pezzo per pezzo.
Nel 2004 Martin Fowler, autore di libri sul software,
lo chiamò come il fico strangolatore,
una pianta della foresta pluviale che cresce attorno a un albero
finché non riesce a reggersi da sola.

<!-- S69 -->
Il vecchio sistema continua a funzionare
mentre il nuovo gli cresce intorno,
un compito alla volta,
finché niente dipende più da quello vecchio.

<!-- S70 -->
Il che ci riporta a quel mezzo penny.
Da qualche parte, un programma forse lo scarta ancora,
perché qualcuno ha deciso così,
decenni fa.
Sostituire quel programma significa saperlo,
e anche tutto il resto di questo tipo.

<!-- S71 -->
Il vecchio sistema non è per forza
ciò che si rompe.
A volte è ciò che lo sostituisce.

<!-- S72 -->
Perché sostituire la tecnologia
non equivale a eliminare il rischio.
A volte sposta solo il rischio
in un unico fine settimana di aprile.

<!-- S73 -->
Allora, ecco una domanda per te.
Se un sistema funziona da quarant'anni,
quando è il momento giusto per sostituirlo?
E a te è mai capitato di doverne sostituire uno?
Fammelo sapere nei commenti.
