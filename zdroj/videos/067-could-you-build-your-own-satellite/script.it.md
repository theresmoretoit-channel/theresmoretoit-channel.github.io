<!-- S01 -->
Immagina di avere un'idea folle.
Vuoi costruire il tuo satellite.
Non un satellite per comunicazioni
da un miliardo di dollari.
Qualcosa di piccolo.

<!-- S02 -->
Una scatola grande più o meno
come una pagnotta.
Dentro: un computer, pannelli solari,
una radio, qualche sensore.
Forse persino una fotocamera.

<!-- S03 -->
Lo costruisci nel tuo garage.
E poi, in qualche modo...
lo metti in orbita.
Sembra impossibile.
Ma non lo è.

<!-- S04 -->
C'è chi lo fa
quasi esattamente così da anni.
Si chiamano CubeSat.

<!-- S05 -->
E la cosa sorprendente
è che la parte più difficile
non è costruire il satellite.
È tutto il resto.

<!-- S06 -->
L'unità base si chiama 1U —
un cubo di circa dieci centimetri.
Impilando le unità
ottieni 2U, 3U, 6U
e oltre.

<!-- S07 -->
L'idea è semplice.
Invece di progettare un nuovo veicolo spaziale
da zero,
riutilizzi dimensioni standardizzate
e interfacce standardizzate.
E all'improvviso lo spazio si apre
alle università, alle start-up,
e forse persino a te.

<!-- S07b -->
A proposito, se ti piacciono i video
come questo, iscriviti.

Aiuta davvero il canale.

<!-- S08 -->
Allora, cosa conterrebbe davvero
il nostro piccolo satellite?
Prima di tutto, gli serve un computer.
Qualcosa deve eseguire il software,
controllare l'hardware,
e decidere cosa fare.

<!-- S09 -->
Poi c'è l'alimentazione.
I pannelli solari producono elettricità.
Le batterie la immagazzinano
per quando il satellite
scivola nell'ombra della Terra.

<!-- S10 -->
Poi la comunicazione.
Una radio. Un'antenna.
E, a terra,
una stazione di terra in ascolto.

<!-- S11 -->
Poi i sensori.
Temperatura. Tensione. Corrente.
Accelerazione. Campo magnetico.
E un modo per capire
in quale direzione punta il satellite.
Perché in orbita
dire "su" è sorprendentemente difficile.

<!-- S12 -->
Ma prima di costruirne uno,
c'è una domanda scomoda.
Quanto costa questa scatoletta?
La risposta è...
più di quanto sembrerebbe.

<!-- S13 -->
Un semplice CubeSat 1U
può facilmente costare
decine di migliaia di dollari —
solo di hardware di volo.
L'alimentazione. I pannelli solari.
Le batterie. Il computer. La radio.
Il controllo d'assetto. La struttura.
E il carico utile.

<!-- S14 -->
Poi arrivano le cose
che non sono nell'elenco dei componenti.
I test. L'integrazione.
La documentazione.
La gestione della stazione di terra.
Le licenze.
E infine...
il lancio.

<!-- S15 -->
Un volo condiviso per un piccolo CubeSat
può costare decine di migliaia.
Missioni e CubeSat più grandi
arrivano a centinaia di migliaia.
E questo è solo
per portarlo nello spazio.

<!-- S16 -->
E adesso
un problema ancora più assurdo.
Ti ricordi tutti quei componenti?
Come diavolo fa tutto quello
a stare in una sola scatoletta?

<!-- S17 -->
Nello spazio non c'è posto
per un mucchio disordinato di elettronica.
Ogni centimetro conta.
Ogni grammo conta.
Ogni watt conta.
Il satellite è un puzzle tridimensionale
che deve sopravvivere al lancio di un razzo.

<!-- S18 -->
Allora, dove trovi
tutti questi componenti?
Non devi progettare
tutto da solo.
C'è un'intera industria
che vende componenti per piccoli satelliti:
computer, sistemi di alimentazione,
radio, antenne e pannelli solari.
Esistono persino dei marketplace
pensati apposta per i componenti dei CubeSat.

<!-- S18b -->
E anche i componenti sono standardizzati.
Molti condividono un unico formato di scheda
e si impilano semplicemente,
così pezzi di produttori diversi
si combinano in un'unica unità.
Aziende come EnduroSat
e GomSpace li vendono,
e un singolo sottosistema può costare
da qualche migliaio
a decine di migliaia di dollari.

<!-- S19 -->
E non sono
processori esotici.
Un computer per CubeSat oggi in commercio
usa un ARM Cortex-M7,
con interfacce familiari —
SPI, I²C, UART e CAN.

<!-- S19b -->
E non è un chip spaziale su misura.
È una vera scheda commerciale
che potresti tenere in mano.

<!-- S20 -->
Un veicolo spaziale ha bisogno di qualcosa
di più importante della pura velocità:
un comportamento prevedibile,
bassi consumi e affidabilità.
Le missioni più esigenti
possono usare processori ARM Cortex-A —
e persino Linux.

<!-- S20b -->
Ma non è veloce.
Un tipico computer di CubeSat
gira a un paio di centinaia di megahertz.
Il tuo portatile gira a
quattro o cinque gigahertz,
con molti più core.
Baratta la pura velocità
per non consumare quasi nulla.

<!-- S21 -->
E se sei un programmatore,
è qui che diventa interessante.
Non scrivi
un misterioso "linguaggio spaziale".
Scrivi software embedded.
Spesso in C o C++.

<!-- S22 -->
Può girare direttamente
sull'hardware,
o su un sistema operativo in tempo reale
come FreeRTOS, Zephyr o RTEMS.
Esistono persino framework aperti
pensati per i veicoli spaziali.
F Prime della NASA, per esempio,
è un framework di software di volo
per sistemi embedded e spaziali.

<!-- S23 -->
Il tuo codice potrebbe quindi somigliare
a qualcosa del genere.

<!-- S24 -->
Ma c'è un'enorme differenza
rispetto a un computer normale.
Non puoi collegarti in SSH.
Non puoi attaccare un debugger.
E se il tuo software si blocca...
il tuo computer è
a qualche centinaio di chilometri di quota.

<!-- S25 -->
Gli servono quindi dei watchdog,
modalità sicure, rilevamento dei guasti
e ripristino automatico.
Deve risolvere alcuni problemi
senza che tu sia lì ad aiutarlo.

<!-- S25b -->
E uno dei motivi principali per tutto questo
è la radiazione.
Nello spazio i raggi cosmici
possono ribaltare un bit in memoria,
o persino mettere fuori uso un chip.
Non c'è una schermatura pesante —
peserebbe troppo.
Invece il computer si sorveglia,
corregge gli errori,
e si riavvia quando qualcosa va storto.

<!-- S26 -->
Ma se vuoi davvero
lanciarlo...
le cose si fanno serie.
Un componente che funziona sulla scrivania
non è automaticamente pronto
per un razzo.
Deve sopravvivere alle vibrazioni,
al vuoto, alle temperature estreme
e alla radiazione.

<!-- S27 -->
Torniamo a quel problema:
sapere in quale direzione
punta il satellite.
Immaginalo mentre ruota senza controllo
nello spazio.
Niente pavimento. Niente soffitto.
Il GPS può dirti
dove sei...
ma non in quale direzione
sei rivolto.

<!-- S28 -->
I satelliti combinano quindi
giroscopi, magnetometri
e sensori solari
per determinare il proprio assetto.
E poi devono cambiarlo.
Un trucco comune
è un magnetorquer.

<!-- S29 -->
Si appoggia
al campo magnetico terrestre
e genera una piccola coppia.
Non è un motore a razzo.
Non sposta il satellite.
Si limita a ruotarlo.
E questo basta
per orientare il satellite
esattamente dove vuoi.

<!-- S30 -->
Ma niente di tutto questo
è il motivo
per cui abbiamo costruito il satellite.
Ci serve una missione.
È il carico utile.
Misurare la radiazione.
Fotografare la Terra.
Studiare l'atmosfera.
Testare un nuovo sensore.
O semplicemente dimostrare
che una nuova tecnologia funziona.

<!-- S31 -->
Il satellite stesso
è lì soprattutto
per tenere in vita il carico utile.
Alimentarlo. Orientarlo.
Tenerlo al caldo.
Immagazzinare i suoi dati.
E inviarli a casa.

<!-- S32 -->
Quando il tuo computer si blocca,
lo riavvii.
Quando il tuo satellite si blocca...
hai un oggetto molto costoso
che orbita silenziosamente attorno alla Terra.

<!-- S33 -->
Diciamo quindi che l'abbiamo costruito.
Tutto funziona...
Il computer si avvia...
La radio comunica.
I pannelli producono energia.
Il carico utile funziona...
Possiamo lanciarlo?
...Non ancora.

<!-- S34 -->
Un satellite deve dimostrare
di poter sopravvivere al lancio.
Il che significa test.
Un sacco di test.

<!-- S35 -->
Prima, imbullonalo
a un enorme shaker.
Poi scuotilo, forte...
Questo è il test di vibrazione.
I lanci dei razzi non sono delicati.
Deve sopravvivere
a rumore, vibrazioni e urti
senza che nulla
si allenti o si rompa.
Ogni vite conta.
Ogni connettore conta.
Ogni pezzo di cavo conta.

<!-- S36 -->
Poi arriva il vuoto.
Sulla Terra l'aria porta via il calore.
Nello spazio non c'è aria.
Un lato può diventare bollente,
l'altro gelido,
e l'elettronica
deve comunque restare
entro i suoi limiti.
Il satellite ha quindi bisogno
di strap termici, rivestimenti,
isolamento
e materiali scelti con cura.
I satelliti non hanno
l'aria condizionata.
Hanno la fisica.

<!-- S37 -->
E con la batteria
le cose si fanno interessanti.
Caricala con la luce del sole.
Poi il satellite
scivola nell'ombra della Terra,
e i pannelli non producono quasi nulla.
La batteria lo tiene in vita.
Poi di nuovo al sole.
Carica. Scarica.
Carica. Scarica.
Ancora e ancora.
Per anni.
Un solo errore nell'alimentazione
potrebbe porre fine alla missione in silenzio.

<!-- S38 -->
E adesso, come ci parli?
Ti serve una radio.
Un'antenna.
E una frequenza
che puoi usare legalmente.
E una stazione di terra.
Il satellite
non ha internet.
Passa semplicemente sopra di te
e trasmette.

<!-- S39 -->
La tua stazione di terra
cattura il segnale.
Il computer lo decodifica.
E all'improvviso hai dei dati
dal tuo veicolo spaziale.
Immagina di aprire un terminale
e vedere questo.

Solo che la macchina
che stampa quei numeri...
è a centinaia di chilometri
sopra la tua testa.

<!-- S40 -->
Allora, come
lo portiamo davvero lassù?
Potresti costruire un razzo...
Ti prego, no...
Non ti serve.
I CubeSat volano
come carichi utili secondari.

<!-- S41 -->
Un razzo sta già partendo.
Ha spazio in più.
Il tuo satellite viaggia
in un deployer standard.
Non serve un razzo tutto tuo.

<!-- S42 -->
E adesso è posato
in cima a un razzo.
Non puoi toccarlo.
Non puoi aprire la scatola.
Non puoi collegare un cavo.
Il razzo parte.
Circa nove minuti dopo,
sei in orbita.

<!-- S43 -->
Il deployer
rilascia il tuo satellite.
Scatta fuori
e comincia a ruotare senza controllo.

<!-- S43b -->
Ma come fa a sapere che è fuori?
...
Interruttori a molla, premuti
mentre stava nel deployer,
scattano nell'istante in cui viene espulso,
e il computer si avvia.
Poi, secondo le regole,
resta in silenzio per circa mezz'ora.
Solo allora accende la radio,
dispiega le antenne,
e finalmente chiama casa.
E da qualche parte sulla Terra...
la tua stazione di terra lo sente.

<!-- S44 -->
Hai costruito una macchina.
E adesso quella macchina
orbita attorno al pianeta.

<!-- S44b -->
Solo che non abbiamo finito.
Un satellite morto non può
restare lassù per sempre.
Lasciato in orbita per secoli,
diventa un detrito spaziale.

<!-- S45 -->
Vuol dire che le missioni moderne
devono sempre più pianificare
la fine
della vita del veicolo spaziale.
Idealmente, l'atmosfera rarefatta in quota
lo trascina lentamente giù.
La sua orbita decade.
Rientra.
E brucia completamente.
La fine della missione...
fa parte della missione.

<!-- S46 -->
Allora... potresti costruire
il tuo satellite?
Tecnicamente, sì.
Non devi essere la NASA.
Non devi
possedere un razzo.
Non ti serve nemmeno per forza
un'azienda enorme.

<!-- S47 -->
Il satellite deve
sopravvivere al lancio.
Sopravvivere allo spazio.
Comunicare legalmente.
Funzionare da solo.
E, alla fine,
liberare l'orbita.
Tutto questo
deve essere dimostrato
prima che qualcuno
lo metta su un razzo.

<!-- S48 -->
I CubeSat non hanno reso lo spazio facile.
L'hanno reso standardizzato.
Invece di costruire tutto
da zero,
puoi costruire qualcosa
che rispetta uno standard esistente.
Ed è un cambiamento sorprendentemente grande.

<!-- S49 -->
Allora da qualche parte, proprio ora,
ci sono minuscole macchine
che orbitano attorno alla Terra.
Costruite da università,
gruppi di ricerca,
aziende e studenti.

<!-- S50 -->
Alcuni portano fotocamere.
Alcuni misurano la radiazione.
Alcuni testano
una tecnologia nuova di zecca.
E alcuni sono solo esperimenti
che pongono una sola domanda:
"riusciamo a far funzionare questo coso
nello spazio?"

<!-- S51 -->
Ed è questo che rende
costruire il tuo satellite
così affascinante.
Perché la distanza
tra te e lo spazio
non è più un razzo.
Potrebbe essere...
una scatola di dieci centimetri.
E una lista di controlli molto, molto
lunga.
