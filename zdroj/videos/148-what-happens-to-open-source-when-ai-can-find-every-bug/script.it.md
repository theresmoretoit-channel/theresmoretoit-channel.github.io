<!-- S01 -->
948.
Sono i modi diversi che un'IA ha trovato
per prendere il controllo di un computer Linux dall'interno.

<!-- S02 -->
Nessuna password rubata. Nessuna intrusione da remoto.
Ognuno parte da un utente qualunque
senza alcun privilegio particolare,
e finisce con root,
l'account che può fare qualsiasi cosa.

<!-- S03 -->
OpenAI ha pubblicato il risultato a novembre 2026.
L'intera esecuzione è costata
1,2 milioni di dollari in crediti API.

<!-- S05 -->
Sono numeri forniti dalla stessa OpenAI,
pubblicati il giorno prima
del lancio del modello che li ha prodotti,
e nessuno dall'esterno ha confermato il conteggio completo.
Ma centinaia di segnalazioni e patch
sono già state inviate.

<!-- S06 -->
Ecco perché la cosa va oltre Linux.
Il codice sorgente di Linux è pubblico.
Chiunque può leggerlo.
Per decenni, questo è stato l'argomento
per sostenere che è sicuro.

<!-- S07 -->
Quindi, se una macchina sa leggere codice pubblico
e trasformarlo in exploit funzionanti su questa scala,
il software dovrebbe tenere segreto il proprio codice, dopotutto?

<!-- S08 -->
Guardiamo un software che lo fa già.
Ad aprile 2026, Microsoft ha corretto
164 falle di sicurezza
nel suo appuntamento mensile con le patch.
A ottobre ne ha corrette
1.413.

<!-- S09 -->
In quel solo mese ne ha corrette di più
che in qualsiasi anno intero precedente.
Oltre 1.000 di quelle correzioni riguardavano Windows,
e Microsoft aveva avvertito
che proprio i suoi strumenti di IA avrebbero fatto crescere i numeri.

<!-- S10 -->
Non puoi confrontare direttamente i due numeri.
Le aziende contano in modo diverso,
e Microsoft stava cercando nel proprio codice privato.

<!-- S11 -->
Ma una cosa la dimostra.
Tenere privato il codice
non aveva tenuto fuori i bug.

<!-- S12 -->
Allora, che cosa ti protegge davvero?
Per rispondere,
dobbiamo vedere come funziona questa macchina,
perché ogni suo passaggio scarta qualcosa.

<!-- S13 -->
Il kernel Linux ha
più di 40 milioni di righe di codice.
Prima, degli agenti esploratori lo hanno passato al setaccio
e hanno scelto le parti
che un utente qualunque può effettivamente raggiungere.

<!-- S14 -->
Ne è rimasto circa il 7%.
È la parte che hanno giudicato degna di essere attaccata,
non un campione casuale,
quindi non puoi moltiplicare il risultato per 14.

<!-- S15 -->
Poi, degli agenti analisti hanno esaminato quel codice
e hanno elencato tutto ciò che era sospetto.
2.308 candidati,
in 12 ore.

<!-- S16 -->
Ma un sospetto non prova nulla.
Così altri agenti hanno scritto programmi di test
e li hanno eseguiti su macchine virtuali isolate.
1.724 bug
si sono rivelati reali.

<!-- S17 -->
Poi è arrivata la parte costosa:
costruire exploit funzionanti,
con le protezioni standard
di un normale sistema desktop attivate.
1.169
hanno raggiunto root.

<!-- S18 -->
Raggruppali in base alla falla di fondo,
e ottieni i 948.

<!-- S19 -->
C'è un dettaglio nel rapporto
difficile da dimenticare.
In una delle prime esecuzioni,
gli agenti hanno segnalato 200 successi.
Poi degli esseri umani hanno controllato come ci erano arrivati.

<!-- S20 -->
Venti di loro avevano raggiunto root
attraverso un altro bug sconosciuto,
non quello che era stato detto loro di usare.
Mandati ad aprire una porta,
ne avevano trovata un'altra che nessuno conosceva.

<!-- S21 -->
In un campione dei suoi exploit,
OpenAI ha individuato dieci tecniche di exploit
che gli esperti esterni non avevano mai visto.

<!-- S22 -->
A luglio, un modello precedente
aveva trovato 166 di queste falle.
Dopo tre mesi di correzioni,
il modello più recente ne ha trovate 948.
I bug non erano finiti.
L'esecuzione successiva ne ha trovati molti di più.

<!-- S23 -->
Ora, c'è un limite importante.
Niente di tutto questo entra nel tuo computer
via Internet.
L'attaccante deve già trovarsi sulla macchina,
come utente qualunque.

<!-- S24 -->
È meno rassicurante di quanto sembri,
perché gli attacchi reali spesso avvengono in due fasi.
Prima entri,
tramite una falla del browser o un download malevolo.
Poi ti serve root.
Questa è la seconda fase.

<!-- S25 -->
Il consiglio di OpenAI è schietto.
Su un sistema senza le patch più recenti,
considera qualunque account normale come root,
almeno contro un attaccante con molte risorse.

<!-- S26 -->
Allora, che fine fa
il vecchio argomento a favore del codice aperto?
Alla fine degli anni Novanta,
Eric Raymond gli ha dato uno slogan:
«Con abbastanza occhi, tutti i bug vengono a galla.»

<!-- S27 -->
La chiamò legge di Linus.
È un'idea bellissima, con un presupposto dentro:
che qualcuno stia davvero guardando.

<!-- S28 -->
Nel 2014, un bug chiamato Heartbleed
è emerso in OpenSSL,
il codice che proteggeva una parte enorme del web.
Si stimava che circa mezzo milione di server sicuri
fossero esposti.

<!-- S29 -->
Il bug era rimasto nel codice pubblico per due anni.
Il progetto riceveva
circa 2.000 dollari l'anno in donazioni
e aveva un solo sviluppatore a tempo pieno.

<!-- S30 -->
Chiunque poteva leggerlo.
Quasi nessuno l'ha fatto.

<!-- S31 -->
Questa è sempre stata la vera debolezza dell'open source.
Non troppi occhi sul codice. Troppo pochi.

<!-- S32 -->
Ed è questa la parte che l'IA cambia.
Una macchina può continuare a scansionare
ed esaminare molti più candidati
di quanti un ricercatore umano potrebbe gestirne da solo.
La vecchia promessa viene finalmente mantenuta,
per tutti, attaccanti compresi.

<!-- S33 -->
Quindi il codice pubblico ora viene davvero esaminato.
Nasconderlo serve a qualcosa?

<!-- S34 -->
Un programma chiuso deve comunque girare,
quindi il suo codice macchina si trova
su ogni computer che lo usa.
Strumenti come Ghidra lo ritrasformano
in qualcosa di simile al codice sorgente.

<!-- S35 -->
E c'è un trucco classico.
Confronta un programma
prima e dopo un aggiornamento di sicurezza.
Ciò che è cambiato ti mostra dov'era la falla.

<!-- S35b -->
Questo dice agli attaccanti dove mirare,
molto prima che ogni sistema
abbia installato l'aggiornamento.

<!-- S36 -->
Anthropic l'ha provato sul kernel di Windows,
con 21 falle
che Microsoft aveva corretto da poco,
e senza codice sorgente.
L'IA ha provocato il primo crash dopo 31 minuti.
In sei ore ne aveva 18.

<!-- S37 -->
Otto sono diventati exploit funzionanti
capaci di prendere il pieno controllo della macchina,
a circa 2.000 dollari l'uno.

<!-- S38 -->
Ma non erano bug sconosciuti.
Le patch indicavano già
dove si trovavano i problemi.
Trovare una falla nuova da zero è più difficile.

<!-- S39 -->
Quindi la segretezza costa ancora qualcosa a chi attacca.
È un dosso, non un muro.
Quanto è alto il dosso?
Non esiste un numero pubblico.

<!-- S40 -->
E dall'altra parte?
Che cosa ti dà davvero il codice aperto?
La risposta sta in un piccolo dettaglio
del rapporto di OpenAI.

<!-- S41 -->
Durante i dieci giorni di quella scansione e analisi,
più di 100 di queste falle di Linux
sono state corrette, o stavano per esserlo,
da altre persone.
Altre 300 circa
erano già discusse pubblicamente.

<!-- S42 -->
Altre persone trovavano gli stessi bug
nello stesso momento.

<!-- S43 -->
Linus Torvalds l'aveva descritto già a maggio.
Disse che le segnalazioni fatte con l'IA
avevano reso la mailing list di sicurezza del kernel
«quasi del tutto ingestibile»,
perché persone diverse continuavano a trovare
le stesse cose con gli stessi strumenti.

<!-- S44 -->
E il suo consiglio era questo:
«Se hai trovato un bug usando strumenti di IA,
è probabile che l'abbia trovato anche qualcun altro.»

<!-- S45 -->
Le regole del kernel ora lo dicono apertamente.
Un bug trovato con l'IA va trattato come pubblico,
perché questi bug vengono scoperti
da più ricercatori,
spesso nello stesso giorno.

<!-- S46 -->
Pensa a cosa significa
per l'idea di un bug segreto.
Se per te è stato economico trovarlo,
lo è stato per tutti.

<!-- S47 -->
Con l'open source,
chiunque può esaminare la segnalazione,
verificare la correzione e contestare il risultato.
Con il software chiuso,
per lo più devi fidarti del produttore.

<!-- S49 -->
Ma l'apertura ha un costo,
e non è quello che ti aspetteresti.
Viene da dire
che un piccolo progetto non può permettersi la scansione.
Le aziende di IA stanno già
offrendo accesso gratuito ai manutentori.

<!-- S50 -->
Quello che manca sono le persone.
Il kernel registrava
circa 500 problemi di sicurezza per versione.
Quest'anno ha superato i 1.500.
Molti sono minori,
ma qualcuno deve comunque esaminarli.

<!-- S51 -->
A gennaio, il progetto curl
ha chiuso il suo programma di bug bounty a pagamento,
per smettere di premiare un'ondata di segnalazioni spazzatura.

<!-- S52 -->
Anche le buone segnalazioni spostano solo il lavoro più avanti.
Le patch generate dall'IA hanno ancora bisogno di revisione umana.
Alcune delle prime correzioni aggiungevano codice inutile
o tralasciavano altre varianti dello stesso bug.

<!-- S53 -->
Puoi comprare più scansioni.
Non puoi comprare più persone
che capiscano così bene un pezzo di codice.
Qui un'azienda con un team di sicurezza retribuito
ha davvero un vantaggio.

<!-- S54 -->
E poi arriva l'ultimo problema.
Corretto non vuol dire installato.

<!-- S55 -->
A marzo 2017,
Microsoft ha corretto una falla in Windows.
Codice chiuso, un solo produttore, un solo sistema di aggiornamento.
Due mesi dopo,
WannaCry è passato da quella stessa falla,
entrando in circa 200.000 computer
in circa 150 Paesi.

<!-- S56 -->
Quella patch aveva avuto due mesi per diffondersi,
e non è bastato.
Un attaccante potrebbe non lasciarti più due mesi.
Nello stesso studio di Anthropic,
l'IA ha preso una correzione pubblica
del motore JavaScript di Firefox
e ha ottenuto un exploit funzionante in meno di un'ora.

<!-- S57 -->
La versione corretta di Firefox
sarebbe arrivata solo 18 giorni dopo.

<!-- S58 -->
Questo è il pericolo di pubblicare una correzione.
L'informazione può raggiungere gli attaccanti
prima che l'aggiornamento raggiunga te.

<!-- S59 -->
Una correzione di Linux ha molta strada da fare,
dal kernel a una versione stabile,
alla tua distribuzione, al tuo dispositivo.
Un telefono può aspettare mesi, o per sempre.

<!-- S60 -->
E il software chiuso non ne è immune.
L'abbiamo appena visto: la patch di Windows è bastata.
Ogni aggiornamento ora è anche una mappa.

<!-- S60b -->
Quindi tieni tutto aggiornato,
il computer, il telefono, perfino il router,
e installa gli aggiornamenti appena arrivano.
Man mano che l'IA diventa più brava a trasformare le correzioni in attacchi,
ogni giorno di attesa conterà di più.

<!-- S61 -->
Allora, l'open source è ancora più sicuro?
Sinceramente, nessuno lo sa.
Per quanto si sa pubblicamente,
nessuno ha fatto lo stesso test su entrambi i fronti,
con le stesse regole.

<!-- S62 -->
Quello che possiamo dire è più modesto.
Nascondere il codice rende meno di una volta.
Mostrarlo permette a chiunque di controllare il lavoro,
e scarica una mole maggiore di quel lavoro
su chi lo mantiene.

<!-- S64 -->
Anche se l'IA non troverà mai tutti i bug,
ha già cambiato quanto costa trovarli.

<!-- S65 -->
Ciò che conta ora è per quanto tempo una falla resta aperta
tra il momento in cui qualcuno la trova
e il momento in cui viene chiusa sulla tua macchina.

<!-- S66 -->
Quindi ecco una domanda per te.
Se chiunque può trovare qualsiasi bug,
preferiresti fidarti di codice che puoi leggere,
o di un'azienda pagata per correggerlo?
Fammelo sapere nei commenti.
