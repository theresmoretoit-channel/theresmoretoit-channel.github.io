<!-- S01 -->
Immagina di accendere un PC Windows
e di non trovare la barra delle applicazioni, né il pulsante Start,
né una sola icona sul desktop.

<!-- S02 -->
Al loro posto c'è una barra sottile in alto,
un menu che compare ovunque clicchi
e quattro desktop virtuali affiancati.

<!-- S03 -->
Sembra Linux.
Ma i tuoi programmi, i driver e i file
sono esattamente dove li avevi lasciati.
È sempre Windows.

<!-- S04 -->
È cambiato solo il desktop.
E l'interruttore che lo cambia
è una singola impostazione.

<!-- S05 -->
Windows la tiene nel registro,
in un valore chiamato Shell.
Su quasi tutti i PC Windows
c'è scritto explorer.exe.

<!-- S06 -->
Scrivici il nome di un altro programma,
esci e rientra,
e Windows avvierà quel programma al suo posto.
Tutto ciò che quel programma disegna diventa il tuo desktop.

<!-- S07 -->
E non è un trucco scoperto l'anno scorso.
Nel 1990 Windows 3.0 aveva già lo stesso interruttore
in un semplice file di testo chiamato system.ini.
Una riga: shell=progman.exe.

<!-- S08 -->
Se cambiavi quel nome,
il Program Manager, la finestra piena di gruppi di icone,
non compariva proprio.

<!-- S09 -->
Quindi la domanda non è se Windows
possa avere un altro desktop.
Ha sempre potuto farlo.
La domanda è perché quasi nessuno ne abbia mai visto uno.

<!-- S10 -->
Partiamo da ciò a cui punta davvero quella riga.
La barra delle applicazioni, le icone del desktop,
la piccola area di notifica vicino all'orologio:
tutto questo è un unico programma, explorer.exe.

<!-- S11 -->
Sì, lo stesso explorer.exe
che apri come Esplora file per sfogliare i tuoi file.
Fa due lavori,
e quasi tutti ne notano solo uno.

<!-- S12 -->
Quel secondo lavoro ha un nome: la shell.
È lo strato che tocchi con mano.
Sotto ci sono il kernel, i driver
e i servizi che tengono in piedi Windows.

<!-- S13 -->
Nessuno di loro ha bisogno della barra delle applicazioni.
Termina explorer.exe in Gestione attività,
e la barra delle applicazioni e le icone spariscono...
ma il Blocco note, il browser
e tutte le altre finestre continuano a funzionare.

<!-- S14 -->
Riavvialo, e il desktop torna.
È forse la dimostrazione più chiara
che il desktop è solo un programma come un altro.

<!-- S14b -->
Se hai mai cambiato il launcher
di un telefono Android,
hai già visto un'idea simile.
Android ne fa una normale impostazione.
Anche Windows ha il meccanismo,
ma non ha mai dato agli utenti comuni
un semplice pulsante per usarlo.

<!-- S15 -->
Qui si confondono tre termini.
La shell è ciò da cui avvii le cose:
la barra delle applicazioni, i menu, il desktop.
Un window manager decide dove stanno le finestre,
come si sovrappongono e quale è attiva.
Un ambiente desktop
tiene insieme tutta l'esperienza.

<!-- S16 -->
Su Linux questi pezzi si possono combinare
in molti modi diversi.
Su Windows, sostituire la shell
non sostituisce la gestione delle finestre del sistema,
né il modo in cui le applicazioni disegnano le cornici delle finestre.

<!-- S17 -->
Questo non ha impedito alla gente di provarci.
Nei primi anni '90 potevi entrare in un negozio
e comprare un sostituto del Program Manager.

<!-- S18 -->
Norton Desktop for Windows
ti dava un desktop tutto suo,
strumenti per i file e un launcher propri,
sopra lo stesso Windows di sempre.

<!-- S19 -->
Alcuni produttori di computer lo sostituivano
prima ancora che il cliente accendesse la macchina.
Il Navigator di Packard Bell accoglieva gli acquirenti
con una casa da esplorare stanza per stanza.

<!-- S20 -->
Poi Windows 95 passò il compito a explorer.exe,
e la riga in system.ini
diventò semplicemente explorer.exe.
L'interruttore rimase esattamente dov'era.

<!-- S21 -->
Alla fine degli anni '90,
attorno a quell'interruttore nacque un'intera comunità.
Il progetto più noto era LiteStep.

<!-- S22 -->
Prendeva il suo aspetto da AfterStep,
un window manager Unix ispirato a NeXTSTEP,
dell'azienda che Steve Jobs fondò dopo aver lasciato Apple.

<!-- S23 -->
LiteStep non aveva un menu Start, a meno che non te lo costruissi.
Tutto era un modulo:
un dock qui, un orologio là,
un menu che si apriva ovunque cliccassi col tasto destro.

<!-- S24 -->
I temi si scambiavano come sfondi.
Alcuni sembravano futuristici.
Altri sembravano una workstation Unix.
Altri non lasciavano quasi nulla sullo schermo.

<!-- S25 -->
Blackbox for Windows andò nella direzione opposta.
Copiava Blackbox, un window manager Unix minimalista,
fino a ridursi a un solo menu essenziale
e a una barra degli strumenti sottile.

<!-- S26 -->
Il suo successore, bbLean,
tenne viva quell'idea su Windows 2000 e XP.

<!-- S27 -->
Emerge Desktop divise la shell in parti separate:
un launcher, un'area di notifica, un elenco delle attività,
ognuna un piccolo programma che potevi tenere o togliere.

<!-- S28 -->
Perché darsi tanta pena?
In parte perché l'aspetto di XP
era facile da riconoscere e difficile da cambiare.
I temi cambiavano i colori e i pulsanti.
La disposizione restava.

<!-- S29 -->
In parte per la memoria.
Su una macchina con 128 megabyte,
una shell più leggera prometteva più spazio
per tutto il resto.

<!-- S30 -->
E in parte per Linux.
Lì scegliersi il desktop era normale,
e alcuni utenti Windows volevano
la stessa scelta.

<!-- S31 -->
La maggior parte di quei progetti ormai non esiste più.
L'ultima versione di LiteStep fu un'anteprima
del 2014, ancora contrassegnata come alfa.
Anche Emerge Desktop e SharpEnviro si fermarono.

<!-- S32 -->
In parte perché i team di volontari erano piccoli.
Ma anche Windows è cambiato.
Col tempo il suo desktop è diventato molto più
di un singolo eseguibile.

<!-- S33 -->
Oggi l'esperienza del desktop è distribuita
su più processi,
componenti di sistema e app pacchettizzate.
Persino il menu Start gira come programma a sé.

<!-- S34 -->
Sostituire explorer.exe non significa sostituire
tutto ciò che forma l'interfaccia moderna di Windows.
Ed è uno dei motivi per cui costruire
un desktop alternativo completo
è più difficile di un tempo.

<!-- S35 -->
Eppure funziona ancora.
Cairo Desktop, un progetto open source,
gira oggi su Windows 11.

<!-- S36 -->
Porta la sua barra dei menu in alto,
la sua barra delle applicazioni
e cartelle che puoi fissare alla barra come pile.

<!-- S37 -->
Può girare accanto a explorer.exe
oppure prenderne il posto come shell.
In questa seconda modalità,
alcune parti di Windows 11 possono dare problemi,
tra cui Impostazioni e Sicurezza di Windows.

<!-- S38 -->
Seelen UI ci arriva in un altro modo.
Non sostituisce explorer.exe.
Nasconde la barra delle applicazioni e porta pezzi suoi:
un dock, una barra, widget
e un window manager che affianca le tue finestre a mosaico.

<!-- S39 -->
Il risultato può non somigliare per niente a Windows.
Ma sotto, explorer.exe è ancora in esecuzione.
È una faccia nuova, non una nuova shell.

<!-- S40 -->
E Microsoft?
In realtà ha una funzione ufficiale per questo.
Si chiama Shell Launcher
ed è pensata per dispositivi come i chioschi.

<!-- S41 -->
Probabilmente hai già usato qualcosa del genere
senza saperlo.
La biglietteria automatica in stazione.
Una cassa self-service. Un bancomat.

<!-- S42 -->
Molti di questi sono PC Windows
la cui intera shell è una sola applicazione.
Un amministratore indica il programma,
e dopo l'accesso quel programma è tutto il desktop.

<!-- S43 -->
Ma è disponibile solo
nelle edizioni Enterprise, Education
e IoT Enterprise.

<!-- S44 -->
E il vecchio meccanismo nel registro
fa ancora parte di Windows.
Solo che Microsoft non l'ha mai trasformato
in una normale impostazione del desktop
per gli utenti comuni.

<!-- S45 -->
Allora perché Windows sembra avere un solo desktop?
Non perché non possa averne un altro.
Ma perché il desktop è il prodotto.

<!-- S46 -->
Su Linux il desktop è una scelta.
Alcune distribuzioni ti chiedono di sceglierne uno
mentre stai ancora installando.
KDE Plasma, GNOME, Xfce, Cinnamon...

<!-- S47 -->
Su Windows il desktop è quello che Microsoft mostra
in ogni pubblicità, in ogni screenshot
e in ogni pagina di supporto.
Un solo desktop significa un solo insieme di istruzioni
per più di un miliardo di macchine.

<!-- S48 -->
È un vantaggio reale.
Quando qualcosa si rompe,
la schermata nella guida è uguale alla tua.
Il prezzo è che quasi nessuno scopre mai
che c'era una scelta.

<!-- S49 -->
La gente sostituiva il desktop di Windows
prima ancora che esistesse Windows 95.
Costruivano dock, menu essenziali
e desktop che non somigliavano a nient'altro.

<!-- S50 -->
La maggior parte di quei progetti è sparita.
L'idea no.
Sotto ogni barra delle applicazioni su cui tu abbia mai cliccato
c'è ancora quell'unica impostazione, in attesa di un altro nome.

<!-- S51 -->
Il desktop è solo un altro pezzo di software.
E il software si può sostituire.

<!-- S52 -->
Allora ecco una domanda per te.
Se Windows ti lasciasse scegliere il desktop
durante l'installazione, come fanno alcune distribuzioni Linux,
cambieresti o terresti quello che conosci?
Scrivimelo nei commenti.
