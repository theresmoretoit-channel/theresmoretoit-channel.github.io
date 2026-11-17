<!-- S01 -->
Fai clic su un pulsante.
Non succede niente.
Fai clic di nuovo.
Ancora niente.

<!-- S02 -->
Muovi il mouse.
Niente.
Per qualche secondo
il computer sembra morto.

<!-- S03 -->
E poi succede tutto insieme.
La finestra si sposta.
Il menu si apre.
Tutti i tuoi clic arrivano,
tutti insieme.

<!-- S04 -->
Ed ecco la cosa strana.
Il computer sapeva del tuo clic.
L'ha saputo in microsecondi.

<!-- S05 -->
Non è un'ipotesi.
Proprio adesso, mentre
non stai facendo niente di che,
la tua macchina gestisce migliaia
di eventi hardware al secondo.

<!-- S06 -->
Un tasto premuto.
Un pacchetto in arrivo.
Un timer che scatta.
Un disco che ha finito.

<!-- S07 -->
Ognuno di questi è un'interruzione,
e i computer fanno così
fin dagli anni cinquanta,
esattamente per questo:

<!-- S08 -->
perché un processore possa reagire
al mondo fuori di sé.

<!-- S09 -->
L'hardware ha segnalato il tuo clic.
Il processore se n'è accorto.
E tu sei rimasto lì cinque secondi
davanti a uno schermo morto.

<!-- S10 -->
L'utente non dovrebbe venire prima?

<!-- S11 -->
Una risposta c'è,
e non è
che il computer sia lento.

<!-- S12 -->
È che essere notati
ed essere serviti
sono due cose del tutto diverse.

<!-- S13 -->
Partiamo dall'essere notati.
Immagina un computer senza interruzioni.

<!-- S14 -->
Il processore dovrebbe
chiedere in continuazione:
è arrivato qualcosa dalla tastiera?
il disco ha finito?

<!-- S15 -->
È arrivato un pacchetto?
Il mouse si è mosso?
E poi chiedere di nuovo.
E ancora.

<!-- S16 -->
Quasi tutte le risposte sarebbero no,
e il chiedere stesso
si mangerebbe viva la macchina.

<!-- S17 -->
Così i dispositivi hanno imparato
ad alzare la mano. Il mouse si muove,
l'hardware solleva un'interruzione,

<!-- S18 -->
e il processore molla
quello che stava facendo,
salta in un breve pezzo di codice
che si chiama gestore,

<!-- S19 -->
e il sistema operativo viene a sapere
che è successo qualcosa.

<!-- S20 -->
È un'idea geniale.
E porta a un'ipotesi
più che ragionevole.

<!-- S21 -->
Se il processore si può strappare
da qualunque cosa, all'istante,
allora anche il mio clic
verrà servito all'istante.

<!-- S22 -->
Solo che al gestore non è permesso
fare quasi niente.

<!-- S23 -->
Finché il processore è lì dentro,
tutto il resto aspetta.
Compresa l'interruzione successiva.
E quella sta già arrivando.

<!-- S24 -->
La regola è quindi l'opposto
di quello che ti aspetteresti.
Il gestore fa il meno
che può.

<!-- S25 -->
Annota cosa è successo.
Conferma al dispositivo
che il messaggio è arrivato.
Lascia l'evento in una coda.
E se ne va.

<!-- S26 -->
Chi scrive kernel arriva a dividere
il lavoro in due metà, ognuna con un nome:
quello che deve accadere ora,
e quello che può aspettare.

<!-- S27 -->
Tutto ciò che è interessante,
tutto quello che potrai mai vedere,
sta nella seconda metà.

<!-- S28 -->
Ed ecco la prima risposta.
Un'interruzione ottiene
l'attenzione del computer.

<!-- S29 -->
Non mette il tuo programma
su un processore.

<!-- S30 -->
Va bene, dirai. Allora sistemalo.
Fai dell'input la cosa più
importante di tutta la casa.

<!-- S31 -->
Il mouse? Priorità massima.
La tastiera? Priorità massima.
La finestra che hai davanti?
Priorità massima.

<!-- S32 -->
Tutto il resto aspetti il suo turno.
Sembra ovviamente giusto.

<!-- S33 -->
E la migliore obiezione a tutto ciò
è successa su Marte.

<!-- S34 -->
Nel 1997 il lander Pathfinder
è atterrato e si è messo al lavoro.
Poi, qualche giorno dopo,
ha cominciato a riavviarsi da solo.

<!-- S35 -->
Non un raggio cosmico.
Non un pezzo rotto.
Un problema di schedulazione.

<!-- S36 -->
C'era un compito ad alta priorità
che distribuiva dati
per tutta la sonda,
e gli serviva memoria condivisa.

<!-- S37 -->
Un compito a bassa priorità,
che raccoglieva dati meteo,
era arrivato lì per primo
e se la teneva.

<!-- S38 -->
Il che, per un momento,
non sarebbe stato un problema.
Ma poi un compito a media priorità
si è preso il processore,

<!-- S39 -->
e quello a bassa priorità
non è mai arrivato in fondo.
Quindi non l'ha mai mollata.

<!-- S40 -->
Il compito più importante
di tutta la sonda
era ora bloccato dietro
quello meno importante di tutti.

<!-- S41 -->
Ha un nome.
Inversione di priorità.

<!-- S42 -->
Un timer di controllo si è accorto
che il compito importante
non girava da troppo tempo,
ha dato per scontato il disastro

<!-- S43 -->
e ha riavviato l'intera sonda.
Poi è successo di nuovo.
E di nuovo.

<!-- S44 -->
Gli ingegneri sulla Terra hanno capito
e hanno mandato una correzione su Marte.

<!-- S45 -->
E la lezione da portarsi a casa
non ci costa proprio niente.
Alta priorità non vuol dire
che qualcuno ti serva.

<!-- S46 -->
Vuol dire solo che ti chiedono per primo.
Se quello che ti serve
è tenuto da qualcuno più lento,
la tua importanza non ti serve a niente.

<!-- S47 -->
E la priorità ha un secondo limite.
Decide chi va per primo.
Non crea nemmeno un ciclo
in più.

<!-- S48 -->
Mettiamo che tutti i tuoi core
siano al cento per cento.
Penserai che vuol dire bloccato.
Di solito non è così.

<!-- S49 -->
Lo scheduler distribuisce fette di tempo
così in fretta
che non senti i passaggi.

<!-- S50 -->
Per questo puoi compilare
qualcosa di enorme
e intanto far scorrere
una pagina web.

<!-- S51 -->
Sotto carico, quello che cambia
non è tanto la velocità.
Il computer non è lento.

<!-- S52 -->
È in ritardo.

<!-- S53 -->
Fai clic e la risposta arriva
mezzo secondo dopo.
Poi un secondo.
Poi cinque.

<!-- S54 -->
E le persone se ne accorgono
straordinariamente bene.
Mezzo secondo sembra una macchina
che sta pensando.

<!-- S55 -->
Cinque secondi sembrano una macchina
che è morta.

<!-- S56 -->
E c'è una versione di tutto questo
che sorprende ancora di più.
A volte il problema non è
affatto il processore.

<!-- S57 -->
Apri troppe cose insieme
e la memoria fisica si riempie.
Il sistema comincia a spostare
pagine di memoria sul disco.

<!-- S58 -->
Fallo abbastanza a lungo
e la macchina passa il tempo
a spostare pagine di memoria
invece di fare il tuo lavoro.

<!-- S59 -->
Anche questo ha un nome.
Thrashing.

<!-- S60 -->
Ed è qui che diventa confuso,
perché il processore
può non sembrare occupato affatto.

<!-- S61 -->
Non sta lavorando.
Sta aspettando.

<!-- S62 -->
Puoi dare a un compito che aspetta
la priorità più alta del sistema
e aspetterà esattamente
quanto prima.

<!-- S63 -->
E poi c'è la versione
più umana di tutto questo.
L'evento è arrivato.
Il kernel ce l'ha.

<!-- S64 -->
Sta in una coda
col nome del tuo programma.
E il tuo programma
non lo sta ritirando.

<!-- S65 -->
Magari sta facendo un calcolo lungo
sullo stesso thread
che dovrebbe gestire
la propria finestra.

<!-- S66 -->
Quindi il mouse funziona.
La tastiera funziona.
Gli altri programmi funzionano.

<!-- S67 -->
E quella finestra sbiadisce
e dice che non risponde.

<!-- S68 -->
E non è una diagnosi.
Windows ci mette quell'etichetta
dopo circa cinque secondi
in cui nessuno ritira i messaggi.

<!-- S69 -->
Il sistema è perfettamente vivo.
È l'applicazione
che non è venuta ad aprire.

<!-- S70 -->
Che il computer riceva il tuo clic
e che l'applicazione ti risponda
non sono lo stesso evento.

<!-- S70b -->
A proposito, se ti va di vedere
dove ci porta la prossima domanda,
puoi iscriverti al canale.

Aiuta davvero il canale.
<!-- S71 -->
Manca ancora un anello,
ed è proprio quello
a cui non pensiamo mai.
Niente di tutto questo ha ancora
messo qualcosa sul tuo schermo.

<!-- S72 -->
L'applicazione cambia il suo stato.
Qualcuno deve fare il prossimo fotogramma.
La scheda grafica deve disegnarlo.
Lo schermo deve mostrarlo.

<!-- S73 -->
Su uno schermo normale
compare un'immagine nuova
ogni sedici millisecondi circa.

<!-- S73b -->
C'è quindi differenza fra
il computer che gestisce il tuo clic
e tu che lo vedi.

<!-- S74 -->
E sotto tutto questo
c'è la parte
che nessuna ingegneria sistema.
Il sistema operativo sa
che il mouse si è mosso.
Perché, non ne ha idea.

<!-- S75 -->
Magari stai mirando a qualcosa
in un gioco.
O stai modificando un documento.
O hai urtato la scrivania.

<!-- S76 -->
Per l'hardware
sono lo stesso evento.
Un sistema sa dare priorità ai lavori.
Indovinare, no.

<!-- S77 -->
Così fa un compromesso.
Abbastanza veloce per te,
quasi sempre,
senza far aspettare il resto per sempre.

<!-- S78 -->
Il che ci riporta
a quello schermo morto.
Il clic non è mai stato un solo evento.

<!-- S79 -->
L'hardware deve segnalarlo.
Il kernel deve metterlo via.
La coda deve arrivare al tuo programma.

<!-- S80 -->
Il tuo programma deve girare.
L'interfaccia deve cambiare.
Qualcuno deve disegnare l'immagine nuova,
e lo schermo deve mostrartela.

<!-- S81 -->
Ognuno di quei passaggi
è piccolo e veloce.

<!-- S82 -->
Ritardane uno solo
e non ti sembrerà
una finestra lenta.

<!-- S83 -->
Ti sembrerà un computer morto.

<!-- S84 -->
E la cosa più strana di tutta
la faccenda è quanto di rado
succeda davvero.

<!-- S85 -->
Ci aspettiamo che una macchina
che fa miliardi di operazioni
al secondo
risponda a uno scatto della mano.

<!-- S86 -->
E quasi sempre risponde.

<!-- S87 -->
Quindi la prossima volta che fai clic
e non succede niente,
dagli un momento.

<!-- S88 -->
Ti ha sentito.

<!-- S89 -->
Aveva solo una coda,
e tu eri in coda.
