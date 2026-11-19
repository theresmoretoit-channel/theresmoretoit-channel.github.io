<!-- S01 -->
Nel 1993, un gioco chiamato Doom
girava su un computer
con 4 megabyte di memoria.

<!-- S02 -->
È più o meno la dimensione
di una singola foto sul tuo telefono.

<!-- S03 -->
Non c'era nessun acceleratore 3D.
Il processore principale
si occupava di tutto il rendering.

<!-- S04 -->
Oggi uno sviluppatore parte da un motore,
come Unity o Unreal,
che si occupa di grafica, audio,
memoria e hardware.

<!-- S05 -->
Sotto DOS, tutto questo
era un problema dello sviluppatore.
E abbastanza spesso, anche del giocatore.

<!-- S06 -->
Quindi, quanto era difficile
fare un gioco per DOS?

<!-- S07 -->
Cominciamo dalla memoria,
perché la memoria era un caos.

<!-- S08 -->
Il primo IBM PC, del 1981,
poteva indirizzare 1 megabyte di memoria.

<!-- S09 -->
Ma solo i primi
640 kilobyte
erano destinati ai programmi.

<!-- S10 -->
Gli altri 384
erano riservati alla memoria video,
alle schede di espansione e al BIOS.

<!-- S11 -->
Per più di dieci anni,
DOS avviava normalmente i programmi
dentro quello spazio.
Andare oltre richiedeva lavoro extra.

<!-- S12 -->
Da qui viene la frase famosa:
640K dovrebbero bastare a chiunque.

<!-- S13 -->
Di solito viene attribuita a Bill Gates.
Non c'è alcuna prova che l'abbia mai detta,
e lui lo nega.

<!-- S14 -->
All'inizio degli anni novanta,
un PC arrivava con 4 megabyte,
o 8.

<!-- S15 -->
E un gioco poteva comunque fermarsi
con le parole
"memoria insufficiente".

<!-- S16 -->
Avere la memoria
e riuscire a usarla
erano due cose diverse.

<!-- S17 -->
Un modo per aggirare il problema era la memoria espansa,
o EMS.

<!-- S18 -->
Una finestra da 64 kilobyte
stava nella parte alta
di quel primo megabyte.
Attraverso di essa, un programma vedeva
4 pagine di memoria aggiuntiva,
da 16 kilobyte ciascuna,

<!-- S19 -->
e poteva scambiarle con altre,
come sfogliare un libro
attraverso un buco in un foglio di carta.

<!-- S20 -->
Un altro modo era la memoria estesa,
raggiungibile tramite un driver chiamato HIMEM.

<!-- S21 -->
Ed è qui che
il problema dello sviluppatore
è diventato quello del giocatore.

<!-- S22 -->
I driver del mouse, del lettore CD
o della scheda audio
si mangiavano un pezzo di quella memoria preziosa,
a meno che tu non riuscissi a caricarli in memoria alta.

<!-- S23 -->
Così i giocatori hanno imparato a modificare due file,
CONFIG.SYS e AUTOEXEC.BAT.

<!-- S24 -->
Un gioco voleva la EMS.
Un altro la voleva disattivata,
con un'opzione chiamata NOEMS.
E un terzo aveva bisogno di ogni kilobyte libero.

<!-- S25 -->
Nel 1993, MS-DOS 6 ha aggiunto
un menu all'avvio.

<!-- S26 -->
Sceglievi la configurazione
per il gioco a cui volevi giocare,
e il computer si avviava proprio per quel gioco.

<!-- S27 -->
Alcuni finivano per avere
una voce separata
per quasi ogni gioco che possedevano.

<!-- S28 -->
Ma a quel punto,
i giochi più grandi avevano trovato
un modo per aggirare i limiti di DOS.

<!-- S29 -->
Dal 386 in poi,
il processore stesso poteva funzionare
in modalità protetta a 32 bit,
con spazio fino a 4 gigabyte.

<!-- S30 -->
Abbiamo parlato della modalità protetta
in un video precedente.
DOS, però, non riusciva a usarla.

<!-- S31 -->
Così i giochi si portavano un aiutante,
un DOS extender.
Il più noto era DOS/4GW.

<!-- S32 -->
Era incluso con un compilatore molto diffuso,
Watcom C.

<!-- S33 -->
Quando un gioco partiva,
DOS/4GW passava il processore
in modalità protetta,
dando al gioco accesso
alla memoria oltre il limite di DOS.

<!-- S34 -->
DOS era ancora lì sotto,
e forniva servizi come l'accesso ai file.
Ma ora il gioco girava in modalità protetta,
non come un programma DOS tradizionale.

<!-- S35 -->
Se negli anni novanta giocavi ai giochi DOS,
hai visto il suo nome
passare veloce sullo schermo.

<!-- S37 -->
Adesso, l'immagine.
In una delle modalità VGA più usate,
chiamata Mode 13h,
lo schermo era di 320
per 200 pixel,
a 256 colori.

<!-- S38 -->
Ogni pixel era un byte.
Per colorare un pixel,
scrivevi un numero in memoria.
Nessuna libreria grafica. Solo memoria.

<!-- S39 -->
L'intero schermo occupava
64.000 byte.

<!-- S40 -->
Appena sotto i 64 kilobyte,
abbastanza poco da stare in un solo segmento,
il blocco che un programma a 16 bit
poteva indirizzare in un colpo solo.
Per una volta, la memoria stava dalla tua parte.

<!-- S41 -->
Ma se disegni direttamente
sullo schermo visibile,
il giocatore vede immagini a metà,
e l'immagine sfarfalla.

<!-- S42 -->
Così i giochi disegnavano ogni fotogramma
prima in un buffer nascosto,
poi copiavano l'immagine finita
nella memoria video.

<!-- S43 -->
Nel 1991, Michael Abrash,
programmatore e scrittore,
ha pubblicato un metodo migliore.
L'ha chiamato Mode X.

<!-- S44 -->
Usava una parte della VGA
che la maggior parte dei programmatori
non aveva mai toccato.

<!-- S45 -->
Dava pixel quadrati
e spazio per più schermate
nella memoria video.

<!-- S46 -->
Il gioco disegnava su una schermata
che nessuno poteva vedere,
e poi passava semplicemente a quella.
Ma era molto più difficile da programmare.

<!-- S47 -->
Poi c'era l'audio.
E l'audio era una lotteria.

<!-- S48 -->
L'altoparlante interno del PC
era fatto per emettere bip.

<!-- S49 -->
Poi sono arrivate le schede audio,
e altro hardware audio.
Non ce n'erano due
che funzionassero allo stesso modo.

<!-- S50 -->
AdLib, con un chip Yamaha
che sintetizzava la musica.
Sound Blaster, che sapeva riprodurre anche
suoni registrati.

<!-- S51 -->
La Roland MT-32,
un modulo costoso con strumenti più ricchi.
La Gravis UltraSound.

<!-- S52 -->
Supportarle tutte
voleva dire scrivere driver diversi.

<!-- S53 -->
E il gioco doveva sapere
dove si trovava la scheda.
La sua porta, il suo interrupt
e il suo canale DMA.

<!-- S54 -->
La risposta tipica, per una Sound Blaster,
era porta 220, IRQ 7, DMA 1.
Di solito.

<!-- S55 -->
Bastava sbagliarne uno,
e il gioco restava muto.
O si bloccava.

<!-- S56 -->
Nel 1991, un programmatore di nome John Miles
ha pubblicato una libreria
che parlava con molte schede audio
attraverso un'unica interfaccia.

<!-- S57 -->
Un gioco poteva scrivere il codice audio una sola volta
e lasciare che la libreria si occupasse della scheda.

<!-- S58 -->
Era un altro strato
tra il gioco e l'hardware.
Tienilo a mente.

<!-- S59 -->
E poi c'era la velocità.
I programmatori contavano
ogni passo del processore.

<!-- S63 -->
Per trovare un pixel sullo schermo,
moltiplichi la sua riga
per 320.

<!-- S63b -->
Sui processori più vecchi,
moltiplicare poteva costare caro.

<!-- S64 -->
Ma 320
è 256
più 64.
Sono entrambi potenze di due.

<!-- S65 -->
Quindi puoi sostituire la moltiplicazione
con due spostamenti di bit e un'addizione.

<!-- S67 -->
Chris Sawyer è sceso al livello più basso.
Ha scritto Transport Tycoon, nel 1994,
quasi interamente in assembly,

<!-- S68 -->
le istruzioni
che il processore stesso capisce,
una per una.

<!-- S69 -->
E a volte
nemmeno tutto questo bastava.

<!-- S70 -->
Nel 1990, Wing Commander aveva un bug
che il team non riusciva a trovare,
con la scadenza vicina.

<!-- S71 -->
Quando uscivi dal gioco,
il gestore della memoria andava in crash
con un messaggio di errore.

<!-- S72 -->
Così un programmatore, Ken Demarest,
ha aperto il gestore della memoria
in un editor esadecimale
e ha cambiato il testo di quel messaggio.

<!-- S73 -->
Ora diceva:
"Grazie per aver giocato a Wing Commander."

<!-- S74 -->
Poi il team ha trovato il vero bug,
e lo scherzo non è mai arrivato nel gioco pubblicato.

<!-- S74b -->
Alcuni giocatori sono ancora sicuri di averlo visto.
E i giochi successivi di Origin
salutavano davvero così.

<!-- S75 -->
Il che ci riporta a Doom.

<!-- S76 -->
Doom usava DOS/4GW
e girava come programma a 32 bit.

<!-- S77 -->
L'hardware per la virgola mobile
non era garantito su ogni PC.

<!-- S78 -->
Così Doom usava l'aritmetica a virgola fissa.
Numeri interi,
in cui i 16 bit più bassi
rappresentavano la parte frazionaria.

<!-- S79 -->
E il suo mondo non era
davvero tridimensionale.

<!-- S80 -->
Ogni livello è una pianta piatta,
con un'altezza per ogni pavimento
e ogni soffitto.

<!-- S81 -->
Una stanza non può mai stare sopra un'altra.
E non puoi davvero guardare in alto o in basso.

<!-- S82 -->
Prima che un livello si potesse giocare,
uno strumento divideva la mappa
in un albero binario, un BSP.

<!-- S83 -->
Il motore percorre quell'albero
dal più vicino al più lontano,
partendo dal lato del giocatore,
e salta le zone che non si possono vedere.

<!-- S84 -->
E Doom non è stato nemmeno scritto su DOS.

<!-- S85 -->
id Software l'ha sviluppato
su workstation NeXT
e ha compilato il risultato per DOS.

<!-- S86 -->
Doom non era un motore 3D generico.
Era costruito esattamente
per un solo tipo di mondo.
Quella specializzazione
lo ha aiutato a girare su un 386.

<!-- S87 -->
E altri studi volevano quel mondo.

<!-- S88 -->
Raven Software ha preso in licenza il motore di Doom
per Heretic, nel 1994,
e Hexen, nel 1995.

<!-- S89 -->
Doom ha contribuito ad affermare
un nuovo modo di fare giochi.
Gli studi potevano prendere in licenza un motore esistente,
invece di costruire tutto da zero.

<!-- S90 -->
Un extender di memoria.
Una libreria audio.
Un motore in licenza.

<!-- S91 -->
Ognuno ha tolto un problema
dalle mani dello sviluppatore.
E gli strati hanno continuato a crescere,
fino ai motori
da cui gli sviluppatori partono oggi.

<!-- S92 -->
Quindi, fare giochi era più difficile allora?
Per molti versi, sì.

<!-- S93 -->
Ma la difficoltà non è scomparsa.
Si è spostata.

<!-- S94 -->
Oggi gli sviluppatori combattono
con gigabyte di asset
e milioni di poligoni,
invece di qualche centinaio di kilobyte.

<!-- S95 -->
Sotto DOS, perfino il giocatore
doveva sapere dove se ne andava la sua memoria.

<!-- S96 -->
Allora ecco una domanda per te.
Ti ricordi di quando costruivi
un menu di avvio solo per far partire un gioco?
Ed era una fatica,
o metà del divertimento?
Scrivimelo nei commenti.
