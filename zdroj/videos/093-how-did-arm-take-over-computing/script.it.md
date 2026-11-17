# Come ha fatto ARM a conquistare l'informatica?

<!-- S01 -->
Nel 1985, alcuni ingegneri in Gran Bretagna
accesero un processore nuovo di zecca
per la primissima volta.

<!-- S02 -->
Funzionava.
E già questo era un piccolo miracolo.

<!-- S03 -->
Ma poi notarono una cosa strana.
L'alimentazione del chip
non era collegata.

<!-- S04 -->
Eppure funzionava lo stesso.

<!-- S05 -->
Si arrangiava con correnti minuscole
che filtravano dai suoi pin di ingresso,
dai segnali dei chip tutt'intorno.

<!-- S06 -->
Quando lo misurarono per bene,
il processore assorbiva
circa un decimo di watt.

<!-- S07 -->
Nessuno ci aveva puntato.
Gli ingegneri volevano solo un chip
economico da produrre.

<!-- S08 -->
Quel chip era il primo processore ARM.

<!-- S09 -->
Quarant'anni dopo, i suoi discendenti
sono in quasi tutti gli smartphone.
Nei computer di Apple.
In alcuni dei più grandi data center
del mondo.

<!-- S10 -->
Centinaia di miliardi di chip.

<!-- S11 -->
Allora come ha fatto un processore
di un'azienda britannica di home computer
a conquistare l'informatica?

<!-- S12 -->
La risposta non è semplicemente
che consumava pochissimo.
Quella parte fu quasi un caso.

<!-- S12b -->
A proposito, se ti piacciono video
come questo, puoi iscriverti al canale.

Aiuta davvero il canale.

<!-- S13 -->
Per capire cosa successe davvero,
dobbiamo tornare al 1983.

<!-- S14 -->
L'azienda era la Acorn Computers.
Il suo BBC Micro era nelle aule
di tutta la Gran Bretagna.

<!-- S15 -->
Il BBC Micro usava un chip
più vecchio, a 8 bit: il 6502.
Per la sua macchina successiva,
Acorn aveva bisogno di qualcosa di molto più veloce.

<!-- S16 -->
Così il team provò
i nuovi processori sul mercato.
Nessuno faceva quello che voleva Acorn.

<!-- S17 -->
Erano complicati,
e nessuno si adattava davvero
a quello che Acorn voleva costruire.

<!-- S18 -->
Poi due ingegneri di Acorn,
Sophie Wilson e Steve Furber,
andarono in Arizona,
in un'azienda fondata da uno
dei progettisti originali del 6502.

<!-- S19 -->
Si aspettavano una grande azienda di chip.
Invece trovarono un pugno di persone
che lavoravano in una casa di periferia.

<!-- S20 -->
E tornarono a casa
con una conclusione semplice.
Se loro riescono a progettare un processore...
possiamo farlo anche noi.

<!-- S22 -->
All'epoca, i processori supportavano
istruzioni sempre più elaborate.

<!-- S23 -->
Una sola istruzione poteva prendere
un numero dalla memoria,
farci un calcolo
e riscrivere il risultato.

<!-- S24 -->
Comodo per il programmatore.
Ma ogni istruzione del genere
rende il chip più difficile da costruire.

<!-- S25 -->
Serve più logica
solo per capire cosa significa ciascuna.
Più transistor.
Più tempo di progettazione.

<!-- S26 -->
Dei ricercatori di Berkeley e Stanford
si erano posti una domanda radicale.

<!-- S27 -->
E se un processore
avesse solo istruzioni semplici,
e al resto pensasse il compilatore?

<!-- S28 -->
La chiamarono RISC.
Reduced Instruction Set Computer.

<!-- S29 -->
Sophie Wilson progettò
le istruzioni di ARM seguendo questa idea.

<!-- S30 -->
I calcoli si fanno solo
sui registri del chip,
piccole caselle veloci dentro il processore.
Per la memoria ci sono istruzioni apposite.

<!-- S31 -->
Sommare un numero preso dalla memoria
richiede quindi tre passaggi.
Caricarlo.
Sommarlo.
Salvarlo.

<!-- S32 -->
Si chiama architettura load-store.

<!-- S33 -->
Più passaggi per il programma.
Ma ogni passaggio è regolare,
prevedibile
e facile da decodificare.

<!-- S34 -->
E ARM aveva un sacco di registri
con cui lavorare.
Sedici, ciascuno da 32 bit.
Il 6502 ne aveva tre piccoli.

<!-- S35 -->
Il risultato fu l'ARM1.

<!-- S36 -->
Aveva circa
25.000 transistor.

<!-- S37 -->
Il 286 di Intel, uscito qualche anno prima,
ne aveva circa 134.000.

<!-- S38 -->
Meno transistor volevano dire un chip più piccolo.
Un chip più economico.

<!-- S39 -->
E, quasi come effetto collaterale,
un chip che non consumava quasi niente.

<!-- S40 -->
Ecco da dove veniva
quel decimo di watt.
Acorn voleva un contenitore di plastica economico,
e questo significava restare sotto un watt.
Così progettarono con prudenza...
e finirono dieci volte più in basso.

<!-- S41 -->
Nel 1987, una versione più veloce dell'ARM
finì nel nuovo computer di Acorn,
l'Archimedes.

<!-- S42 -->
Era uno dei personal computer
più veloci del suo tempo.

<!-- S43 -->
E non contò quasi niente.

<!-- S44 -->
Il mondo comprava PC IBM compatibili
con processori Intel.
Lì c'erano i programmi.
Quello compravano le aziende.

<!-- S45 -->
L'Archimedes rimase
soprattutto nelle scuole britanniche.

<!-- S46 -->
E la stessa Acorn era in difficoltà.
Aveva già dovuto essere salvata
dalla Olivetti, nel 1985.

<!-- S48 -->
Poi arrivò un aiuto da Apple.
Stava costruendo un computer palmare
chiamato Newton.

<!-- S49 -->
Le serviva un processore
veloce, economico
e capace di andare a batterie.

<!-- S50 -->
L'ARM era perfetto.
Ma Apple non voleva dipendere
da un chip di proprietà
di un produttore di computer rivale.

<!-- S51 -->
Così nel 1990, il team ARM
fu separato da Acorn
e diventò un'azienda a sé.

<!-- S52 -->
Acorn, Apple
e il produttore di chip VLSI
ne erano proprietari insieme.

<!-- S53 -->
Dodici ingegneri.
Un vecchio fienile vicino a Cambridge.

<!-- S54 -->
E un modello di business
che si rivelò il vero segreto del suo successo.

<!-- S55 -->
Intel progettava i suoi processori,
li produceva nelle proprie fabbriche
e li vendeva.

<!-- S56 -->
ARM non avrebbe prodotto proprio niente.
Avrebbe venduto il progetto.

<!-- S57 -->
Qualsiasi azienda poteva prenderlo in licenza,
integrare il core ARM nel proprio chip
e pagare una piccola royalty
su ogni chip venduto.

<!-- S58 -->
Questo contava,
perché un chip non deve per forza essere
solo un processore.
Attorno al core ARM
puoi mettere una radio,
un'unità grafica,
un processore per la fotocamera.

<!-- S59 -->
Un solo chip,
progettato da chi ne ha bisogno,
con ARM al centro.

<!-- S60 -->
ARM non doveva battere Intel
nei personal computer.
Poteva finire dentro qualsiasi cosa.

<!-- S61 -->
E negli anni '90,
«qualsiasi cosa» voleva dire sempre più spesso
telefoni cellulari.

<!-- S62 -->
Un computer fisso può permettersi
cento watt e una grossa ventola.
Un telefono va a batteria
nella tua tasca.

<!-- S63 -->
Alla fine del decennio,
i core ARM erano dentro
alcuni dei telefoni più venduti,
di Nokia e di altri.

<!-- S64 -->
Poi arrivò l'iPod.
Poi lo smartphone.

<!-- S65 -->
Miliardi di persone all'improvviso si portavano dietro
un computer che doveva durare
tutto il giorno con una batteria.

<!-- S66 -->
E il processore nato
perché costava poco
si rivelò esattamente
quello di cui quel mondo aveva bisogno.

<!-- S67 -->
Quindi è questa la risposta, giusto?
ARM è semplice,
semplice vuol dire efficiente,
e chi è efficiente vince.

<!-- S68 -->
Non proprio.

<!-- S69 -->
Guarda dentro un moderno core ARM di fascia alta.

<!-- S70 -->
Cache enormi.
Più istruzioni eseguite insieme.
La predizione dei salti,
che indovina dove andrà il programma
prima che ci arrivi.

<!-- S71 -->
L'esecuzione fuori ordine,
che esegue le istruzioni
nell'ordine più veloce.

<!-- S72 -->
Miliardi di transistor sul chip.
Non c'è niente di semplice.

<!-- S73 -->
Allora dov'è finita la semplicità?

<!-- S74 -->
Il trucco è che un processore
in realtà è due cose diverse.

<!-- S75 -->
Il set di istruzioni è la lingua
che parla il software.
Quali istruzioni esistono,
e cosa significano.

<!-- S76 -->
La microarchitettura è la macchina
che le esegue davvero.

<!-- S77 -->
La lingua può restare semplice,
mentre la macchina sotto
diventa enormemente complicata.

<!-- S78 -->
E la stessa cosa è successa
dall'altra parte.

<!-- S79 -->
Le istruzioni x86 di Intel
sono notoriamente complicate.

<!-- S80 -->
Ma dalla metà degli anni '90,
i processori Intel e AMD
al loro interno le scompongono
in piccole operazioni semplici.

<!-- S81 -->
Poi le eseguono su un motore
molto simile a quello
di un moderno core ARM.

<!-- S82 -->
Al di là delle etichette,
i due sono diventati sorprendentemente simili.

<!-- S83 -->
Le istruzioni più pulite di ARM aiutano ancora.
Sono più facili da decodificare,
e questo può far risparmiare un po' di energia.

<!-- S84 -->
Ma non sono un vantaggio magico
che x86 non potrebbe mai eguagliare.

<!-- S85 -->
Quindi ARM non ha conquistato tutto
perché era semplice.
E non era stato progettato per consumare poco.

<!-- S86 -->
Ha vinto perché tre cose si sono allineate.
Un progetto efficiente.
Un modello di business
che permetteva a chiunque di costruire su ARM.
E un mondo che all'improvviso aveva bisogno
di miliardi di computer a batteria.

<!-- S87 -->
E poi, nel 2020,
la storia è tornata ad Apple.

<!-- S88 -->
Apple aveva venduto la sua quota di ARM
anni prima,
quando aveva un disperato bisogno di soldi.

<!-- S89 -->
Ora metteva i suoi chip basati su ARM
nel Mac.

<!-- S90 -->
Lo stesso tipo di core dell'iPhone,
potenziati per un computer.
Core veloci, core efficienti,
grafica e molto altro,
in un unico chip.

<!-- S91 -->
Erano più veloci
dei chip Intel che sostituivano,
e i portatili duravano molto di più
con una carica.

<!-- S92 -->
ARM non era più
solo il processore dei telefoni.

<!-- S93 -->
E ARM non si è fermata lì.
È entrata anche nei data center,
dove ogni watt costa soldi.
Oggi Amazon progetta
i propri chip ARM per server.

<!-- S95 -->
Il primo chip ARM aveva circa
25.000 transistor.
Quelli di oggi ne hanno miliardi.

<!-- S96 -->
Il loro funzionamento interno
è cambiato quasi del tutto.

<!-- S98 -->
Un piccolo team voleva
un processore che potesse davvero costruire.

<!-- S99 -->
Non l'hanno costruito per i telefoni,
né per Apple,
né per battere Intel.

<!-- S100 -->
E alla fine,
la cosa più importante che hanno creato
non era il chip.

<!-- S101 -->
Era una base semplice
su cui tutti gli altri potevano costruire.
