<!-- S01 -->
Il 19 luglio 2024,
un'azienda di sicurezza chiamata CrowdStrike
ha inviato un aggiornamento di routine.

<!-- S02 -->
Non un nuovo programma.
Solo un piccolo file di configurazione.

<!-- S03 -->
Nel giro di poche ore, 8,5 milioni
di computer Windows si erano fermati
su una schermata blu.

<!-- S04 -->
Le compagnie aeree hanno bloccato i voli.
Gli ospedali hanno annullato interventi.
Un canale di notizie è andato fuori onda.

<!-- S05 -->
E l'errore dietro a tutto questo
era del tutto banale.
Il programma si aspettava 20 dati.
L'aggiornamento gliene ha dati 21.

<!-- S06 -->
I tuoi giochi e le tue app fanno
errori così di continuo.
Quando succede, il gioco si chiude
e tu lo riavvii.

<!-- S07 -->
Lo stesso tipo di bug.
Uno chiude una finestra.
L'altro ferma
8,5 milioni di macchine.

<!-- S08 -->
La differenza non sta nell'errore.
Sta nel punto in cui girava il codice.

<!-- S09 -->
Allora perché un programma non può
prendere il controllo del tuo computer...
e perché questo invece ci è riuscito?

<!-- S10 -->
Non è sempre stato così.

<!-- S11 -->
Su un PC con DOS negli anni '80,
nel processore niente fermava un programma.
Poteva scrivere in qualsiasi punto della memoria
e parlare direttamente con l'hardware.

<!-- S12 -->
Bastava che un programma scrivesse
dove non doveva
per sovrascrivere il sistema operativo,
e l'intera macchina si bloccava.

<!-- S13 -->
La soluzione fu smettere di fidarsi dei programmi
e lasciare
che fosse il processore a diffidare.

<!-- S14 -->
Nel 1982, il processore 80286 di Intel
introdusse la modalità protetta,
con quattro livelli di privilegio.

<!-- S15 -->
Di solito si disegnano
come quattro anelli, uno dentro l'altro.

<!-- S16 -->
Il ring 0 è al centro.
Il ring 3 è all'esterno.

<!-- S17 -->
E la numerazione va al contrario.
Più basso è il numero,
più cose può fare il codice.

<!-- S18 -->
Il ring 0 appartiene al kernel,
il nucleo del sistema operativo.
Distribuisce la memoria,
decide quale programma gira dopo
e parla con l'hardware.

<!-- S19 -->
Nel ring 3 girano il tuo browser,
i tuoi giochi e il tuo editor di testo.
Si chiama modalità utente.

<!-- S19b -->
Windows, macOS e Linux
si dividono tutti il lavoro così.
Il kernel nel ring 0,
le tue app nel ring 3.

<!-- S19c -->
I telefoni e i Mac più recenti di Apple
usano invece chip ARM.
Lì i livelli si chiamano exception level.
Nome diverso, stessa divisione:
uno per il kernel, uno per le tue app.

<!-- S20 -->
Il processore sa sempre
in quale ring sta girando.
E controlla.

<!-- S21 -->
Alcune istruzioni funzionano solo nel ring 0.
Disattivare gli interrupt, per esempio,
o cambiare il modo in cui è mappata la memoria.

<!-- S22 -->
Quando un programma nel ring 3 ne prova una,
il processore si rifiuta.
Solleva un'eccezione
e passa il controllo al kernel,
che di solito chiude il programma.

<!-- S23 -->
La memoria riceve lo stesso trattamento.
Ogni pagina di memoria è contrassegnata
come user oppure supervisor.

<!-- S24 -->
Un programma nel ring 3
che tocca una pagina supervisor
non riceve i dati.
Viene fermato.

<!-- S25 -->
Il tuo browser e il tuo gioco
girano entrambi nel ring 3.
Quello che li tiene separati
è che ognuno ha la sua mappa della memoria.
La memoria dell'altro programma
semplicemente non c'è.

<!-- S26 -->
Così, quando un gioco va in crash,
il danno resta dentro il gioco.
Il kernel fa pulizia.
Tutto il resto va avanti.

<!-- S27 -->
Ora torniamo a CrowdStrike.
Il suo driver girava nel ring 0,
proprio accanto al kernel.

<!-- S28 -->
Sopra il ring 0 non c'è niente
che possa intercettare un errore del genere.

<!-- S29 -->
Così Windows ha fatto l'unica cosa sicura rimasta.
Ha fermato l'intera macchina, di proposito,
invece di andare avanti con una memoria
di cui non poteva più fidarsi.

<!-- S30 -->
Ecco cos'è la schermata blu.

<!-- S31 -->
E dato che il driver partiva
ogni volta che partiva Windows,
ogni riavvio riportava il crash.

<!-- S32 -->
Ma questo solleva una domanda.
Se il tuo browser non può toccare l'hardware,
come fa a salvare un file
o a mandare qualcosa in rete?

<!-- S33 -->
Lo chiede.

<!-- S34 -->
Il programma mette la sua richiesta
nei registri del processore.
Quale file. Dove devono andare i dati.
Quanti.

<!-- S35 -->
Poi esegue un'istruzione speciale.
Su un PC moderno si chiama SYSCALL.

<!-- S36 -->
In quell'istante il processore passa
dal ring 3 al ring 0...

<!-- S37 -->
ma non salta
dove vuole il programma.
Salta a un unico punto di ingresso
che il kernel ha scelto in anticipo.

<!-- S38 -->
Il kernel controlla la richiesta,
fa il lavoro
e torna al ring 3.
Il programma non ha mai toccato il disco da solo.

<!-- S39 -->
Questa è una chiamata di sistema,
e succede di continuo.

<!-- S40 -->
Le abbiamo contate su un portatile.
Un programma che non fa assolutamente niente
ne fa comunque 30.

<!-- S41 -->
Firefox, avviandosi
e caricando una sola pagina di Wikipedia,
ne ha fatte circa 670.000
in 20 secondi...
nonostante il nostro conteggio lo rallentasse.

<!-- S42 -->
Ognuna di esse
è un viaggio attraverso il muro, andata e ritorno.

<!-- S43 -->
E qui c'è qualcosa di strano.
Quattro ring,
e ce ne sono serviti solo due.

<!-- S44 -->
Che fine hanno fatto i ring 1 e 2?

<!-- S45 -->
L'idea dei ring è più vecchia del PC.
Multics, un sistema operativo
della fine degli anni '60,
ne aveva otto.

<!-- S46 -->
L'idea erano strati di fiducia.
Il nucleo del sistema al centro,
servizi meno affidabili intorno
e i programmi all'esterno.

<!-- S46b -->
Intel disegnò lo stesso schema.
I ring 1 e 2 erano pensati
per gli strati intermedi,
come i driver e i servizi di sistema.
Più fidati delle tue app,
meno del kernel.

<!-- S47 -->
Due cose si misero di mezzo.

<!-- S48 -->
Primo, sistemi come Unix e Windows NT
erano progettati per girare
su molti tipi di processore.

<!-- S49 -->
E l'unica divisione
che offrivano tutti i processori
erano due livelli.
Uno per il kernel,
uno per tutto il resto.

<!-- S50 -->
Secondo, il processore x86 stesso.
Quando mappa la memoria,
ogni pagina conosce solo due stati.
User o supervisor.

<!-- S51 -->
I ring 1 e 2 contano come supervisor.
Quindi un driver nel ring 1
potrebbe comunque toccare la memoria del kernel.
Il ring in più non proteggerebbe granché.

<!-- S51b -->
Alcuni sistemi li usarono lo stesso.
OS/2 faceva entrare alcuni programmi nel ring 2,
solo per parlare direttamente con l'hardware.

<!-- S51c -->
E prima che i processori avessero un supporto
per far girare macchine virtuali,
Xen e VirtualBox spostavano il kernel del sistema ospite
nel ring 1,
così che il sistema sottostante
potesse tenersi il ring 0 tutto per sé.

<!-- S52 -->
Nel 2023, Intel propose
di eliminare del tutto i ring 1 e 2.

<!-- S53 -->
A dicembre 2024 ha abbandonato il piano.
Sono ancora nel tuo processore.
Quasi niente li usa.

<!-- S54 -->
Fin qui sembra rassicurante.
Le regole stanno nell'hardware,
e l'hardware controlla ogni accesso.

<!-- S55 -->
Nel 2017, tre gruppi di ricercatori,
lavorando separatamente,
trovarono un modo per attraversare quel muro.

<!-- S56 -->
Lo chiamarono Meltdown.
E per seguirlo,
ti serve conoscere un trucco
che usano i processori moderni.

<!-- S57 -->
Un processore non aspetta
che un'istruzione finisca
prima di iniziare la successiva.
Va avanti
su istruzioni che probabilmente gli serviranno.

<!-- S58 -->
Se ha indovinato male,
butta via i risultati,
come se niente fosse.

<!-- S59 -->
Ecco il difetto.
Sui chip Intel colpiti,
un programma nel ring 3 poteva chiedere
un byte della memoria del kernel...

<!-- S60 -->
e il processore lo prendeva
e lo passava alle istruzioni successive
prima di aver finito di controllare
se era permesso.

<!-- S61 -->
Il controllo falliva, eccome.
Il risultato veniva scartato.

<!-- S62 -->
Ma quelle istruzioni successive
avevano già usato il byte segreto
per portare un pezzo
della memoria del programma stesso
nella cache del processore.

<!-- S63 -->
E la cache non dimentica
solo perché il risultato è stato annullato.

<!-- S64 -->
Così il programma misura
quanto tempo impiega ogni pezzo della sua memoria a rispondere.
Quello che risponde in fretta
rivela il byte segreto.

<!-- S65 -->
Un byte alla volta,
un normale programma poteva leggere
la memoria del kernel
e qualsiasi segreto ci fosse dentro.
Password e chiavi di cifratura comprese.

<!-- S66 -->
Meltdown colpiva processori Intel
risalenti fino al 1995.

<!-- S67 -->
È stato reso pubblico
il 3 gennaio 2018.

<!-- S68 -->
La correzione non poteva cambiare il silicio.
Così i sistemi operativi hanno cambiato la mappa.

<!-- S69 -->
Mentre il tuo programma gira,
la memoria del kernel ora viene tolta
quasi del tutto dalla sua mappa.
Non c'è più niente da prendere.

<!-- S70 -->
Ma ricordati delle chiamate di sistema.
Ogni viaggio attraverso il muro
ora deve cambiare anche la mappa.

<!-- S71 -->
Red Hat ha misurato le patch contro Meltdown
e un difetto simile, Spectre.
Meno dell'1% su alcuni carichi di lavoro...
fino al 19% su database molto carichi.

<!-- S72 -->
La regola era giusta fin dall'inizio.
Il processore la controllava solo troppo tardi.

<!-- S73 -->
Il che ci riporta a CrowdStrike,
e a una domanda più difficile.

<!-- S74 -->
Perché un programma di sicurezza
stava nel ring 0, tanto per cominciare?

<!-- S75 -->
Perché da lì vede tutto.
Si avvia prima degli altri software.
E un malware con diritti di amministratore
fa più fatica a disattivarlo.

<!-- S76 -->
L'elenco stesso di Microsoft
finisce con un avvertimento.
I driver nel kernel lo offrono a scapito della resilienza.

<!-- S77 -->
Dopo il blackout,
Microsoft ha iniziato a creare un sistema
che permetta agli antivirus
di funzionare fuori dal kernel.

<!-- S78 -->
Nell'autunno del 2026
è ancora disponibile solo nelle versioni di prova di Windows.
E il kernel non è stato chiuso
alle aziende di sicurezza.

<!-- S79 -->
I tuoi giochi affrontano lo stesso dilemma.

<!-- S80 -->
I cheat che girano nel kernel
sono invisibili per un anti-cheat
che gira nel ring 3.

<!-- S81 -->
Così anche l'anti-cheat si è trasferito lì.
Vanguard di Riot, usato da Valorant,
mette un driver nel ring 0.
Sulla maggior parte dei PC si carica all'avvio di Windows...
anche se non apri mai il gioco.

<!-- S82 -->
Questo non lo rende difettoso.
Ma sta nello stesso posto
in cui stava il driver di CrowdStrike,
dove un solo errore ferma l'intera macchina.

<!-- S83 -->
Allora perché un programma non può
prendere il controllo del tuo computer?

<!-- S84 -->
Perché il processore tiene
quasi tutti i programmi fuori dal centro
e li controlla ogni volta che bussano.

<!-- S85 -->
Ma il processore non può decidere
chi far entrare.
Lo decidono le persone...
ogni volta che installano un driver.

<!-- S86 -->
Allora, ecco una domanda per i commenti.
Chi dovrebbe decidere quali programmi
entrano nel ring 0:
tu, Microsoft
o le aziende che li producono?
