<!-- S01 -->
Premi play sul registratore a cassette.
E dall'altoparlante esce questo.

<!-- S02 -->
Non è musica.
E non è nemmeno la colonna sonora di un gioco.

<!-- S03 -->
È il gioco.
Ogni stridio è un pezzo di programma,
e il computer lo sta ascoltando.

<!-- S04 -->
Il registratore non ne ha la minima idea.
Per lui sta suonando una canzone.

<!-- S05 -->
Allora come si trasforma una canzone in un gioco?
E perché una sola nota sbagliata
poteva buttare via cinque minuti di attesa?

<!-- S06 -->
Ecco il trucco,
su una macchina in particolare:
lo ZX Spectrum,
un home computer britannico del 1982.

<!-- S07 -->
Usa due tipi di impulso.
Una coppia di impulsi brevi significa zero.

<!-- S08 -->
Un uno è la stessa coppia,
ma con ogni impulso lungo il doppio,
quindi il suo tono è un'ottava più basso.

<!-- S09 -->
Manda circa millequattrocento bit
al secondo,
e ottieni il rumore che hai appena sentito.

<!-- S09b -->
Vuol dire anche che un programma pieno di zeri
si carica più in fretta di uno pieno di uno.
Ogni uno richiede il doppio del tempo.

<!-- S10 -->
Ora, se sei cresciuto in America,
forse non l'hai mai sentito.

<!-- S11 -->
Il che è strano,
perché l'idea in sé era americana.

<!-- S12 -->
Nel 1975, a un incontro a Kansas City,
un gruppo di appassionati di computer
si accordò su come salvare dati come suono
su normali audiocassette.

<!-- S12b -->
Un uno corrispondeva a otto cicli rapidi
di un tono acuto,
uno zero quattro cicli più lenti di uno grave.
Trecento bit al secondo.

<!-- S13 -->
Le prime macchine come l'Apple II
e il TRS-80
salvavano i loro programmi
su comunissimi registratori a cassette.

<!-- S14 -->
Ma l'informatica domestica americana
andò avanti in fretta.

<!-- S15 -->
Nel 1983 una rivista riportò un sondaggio:
nove nuovi proprietari di Commodore 64 su dieci
compravano un'unità disco
insieme al computer.

<!-- S16 -->
In Gran Bretagna la storia andò al contrario.

<!-- S17 -->
Lo Spectrum costava
centoventicinque sterline,
e non aveva nessuna memoria di massa.
Usavi il registratore a cassette
che avevi già in casa.

<!-- S18 -->
Così per milioni di ragazzini in tutta Europa,
questo rumore era il suono
di un gioco che stava per partire.

<!-- S18b -->
Dopo un bel po' di caricamenti,
riuscivi perfino a capire di che gioco si trattava
solo dallo stridio.

<!-- S19 -->
Allora seguiamo un gioco
dal nastro fino al computer.

<!-- S20 -->
Scrivi LOAD, premi invio
e premi play.

<!-- S21 -->
Prima arriva un ronzio costante,
ottocento cicli al secondo,
per circa cinque secondi.

<!-- S22 -->
Non trasporta nessun dato.
Serve perché il computer
trovi il segnale
e si agganci al suo ritmo.

<!-- S23 -->
Poi due impulsi rapidi, la sincronizzazione.
Vogliono dire: da qui in poi, sono dati.

<!-- S24 -->
La prima cosa ad arrivare
è una breve intestazione.
Diciannove byte:
un nome di massimo dieci lettere,
che tipo di file è
e quanto sarà lungo.

<!-- S25 -->
Poi un secondo ronzio, più breve,
stavolta di due secondi,
e poi il gioco vero e proprio.

<!-- S26 -->
Ogni byte è fatto di otto di quelle note,
una dopo l'altra,
senza nessuna pausa tra un byte e l'altro.

<!-- S27 -->
E il computer non sente note.
Misura l'intervallo tra un fronte
del segnale e quello successivo.

<!-- S28 -->
Una coppia breve è uno zero.
Una coppia lunga è un uno.

<!-- S28a -->
Ecco tutto il decodificatore.

<!-- S28b -->
E il rumore all'inizio di questo video
non è un effetto sonoro.
L'abbiamo generato esattamente con queste regole,
e dentro c'è un vero programma per Spectrum.

<!-- S28c -->
Lo faremo sentire per intero alla fine.
Registralo, e uno Spectrum lo caricherà.

<!-- S29 -->
La maggior parte dei giochi mostrava prima un'immagine,
che si caricava in un ordine strano.

<!-- S30 -->
Comparivano righe sottili, a otto linee di distanza,
poi si riempivano, linea dopo linea,
un terzo dello schermo alla volta.
E i colori arrivavano per ultimi,
ricoprendo tutto dall'alto verso il basso.

<!-- S31 -->
Solo quell'immagine
richiedeva circa quaranta secondi.
Il gioco intero, circa cinque minuti.

<!-- S32 -->
E alla fine di ogni blocco
arriva un ultimo byte.

<!-- S33 -->
Durante il salvataggio, lo Spectrum fa passare
ogni byte del blocco
attraverso una semplice regola chiamata XOR,
e registra il risultato come un byte in più.

<!-- S34 -->
Durante il caricamento, ripete il calcolo.
Se i risultati coincidono,
il blocco è arrivato intatto.

<!-- S35 -->
Se no, lo Spectrum dice questo.

<!-- S36 -->
Cinque minuti di attesa,
e un solo byte decide
che è stato tutto inutile.
Riavvolgi, e ricomincia da capo.

<!-- S37 -->
Stranamente, un'intestazione rovinata
non dà nessun errore.
Lo Spectrum la ignora e basta,
e continua ad ascoltare in attesa della prossima.

<!-- S38 -->
Altri computer puntarono su altro.

<!-- S39 -->
Il Commodore 64 registrava
ogni blocco due volte,
così un punto danneggiato in una copia
si poteva recuperare dall'altra.

<!-- S40 -->
Più sicuro, ma lento.
Con la routine integrata del Commodore,
un programma da quaranta kilobyte
richiedeva circa dodici minuti e mezzo.

<!-- S41 -->
Così gli editori di videogiochi scrissero
dei caricatori propri, più veloci,
alcuni fino a circa dieci volte più rapidi.

<!-- S42 -->
E poi c'era il registratore.

<!-- S43 -->
Troppo basso,
e i fronti affondano nel fruscio.
Troppo alto,
e si impastano l'uno con l'altro.

<!-- S44 -->
Un nastro che gira un filo troppo veloce o lento
allunga ogni impulso,
e il computer sta misurando il tempo.

<!-- S45 -->
Il peggio di tutto era l'azimut,
l'angolo della testina.
Un nastro registrato su un apparecchio
poteva non allinearsi con un altro.

<!-- S46 -->
Così la gente infilava un cacciavite minuscolo
in un forellino accanto alla testina,
e lo girava un pochino alla volta,
ascoltando.

<!-- S47 -->
Sembrava superstizione.
Era taratura del segnale.

<!-- S48 -->
Ma nota cosa il registratore
non ha mai dovuto fare.

<!-- S49 -->
Non ha mai capito un solo bit.
Registrava il suono
e lo riproduceva.

<!-- S50 -->
Il che significa che un programma
non aveva davvero bisogno di una cassetta.
Qualsiasi cosa capace di trasportare suono
poteva trasportare software.

<!-- S50b -->
Significava anche che copiare un gioco
era facile come copiare un album.
Due piastre a cassette e un cavo.

<!-- S51 -->
Atari usava entrambe le tracce stereo.
Il programma su una,
e una voce sull'altra,
che ti parlava dalla TV
mentre il gioco si caricava.

<!-- S52 -->
In Jugoslavia, una trasmissione di Radio Belgrado
mandava in onda programmi per computer.

<!-- S53 -->
Gli ascoltatori li registravano su nastro,
circa centocinquanta programmi
tra il 1983 e il 1986.

<!-- S54 -->
In Cecoslovacchia, era la televisione.
Un programma andava in onda come suono
sotto i titoli di coda.

<!-- S55 -->
E nel 1983 il cantante Pete Shelley
nascose un programma per Spectrum
alla fine di un album in vinile.

<!-- S56 -->
Lo copiavi su nastro, lo caricavi,
e i testi comparivano sullo schermo
a tempo con le canzoni.

<!-- S57 -->
Ma c'era un problema.

<!-- S58 -->
La radio poteva portare il suono
a ogni computer del paese.
Ma solo quello giusto poteva capirlo.

<!-- S59 -->
Fai sentire un gioco per Spectrum a un Commodore,
e il Commodore sente solo rumore.
I bit significano qualcosa
solo per una macchina che conosce il formato.

<!-- S60 -->
Così la radio olandese provò a risolverlo.
Nel 1982 creò BASICODE:
un unico formato sonoro,
con un piccolo programma traduttore
per ogni tipo di computer.

<!-- S61 -->
E quel problema non è mai sparito.
Un file serve a qualcosa
solo se qualcosa riesce ancora a leggerlo.

<!-- S62 -->
Le cassette hanno perso, ovviamente.
I floppy erano più veloci,
poi gli hard disk, poi la memoria flash.

<!-- S63 -->
Solo che il nastro non se n'è mai andato davvero.
I data center tengono ancora
i loro archivi su nastro magnetico.

<!-- S64 -->
Una moderna cartuccia LTO-9
contiene diciotto terabyte.

<!-- S65 -->
Convertita alla velocità dello Spectrum,
quella capacità riempirebbe circa
ventinove milioni di cassette,
e ci vorrebbero più di tremila
anni per caricarla.

<!-- S66 -->
Ma l'idea è sempre la stessa.
Schemi su una striscia di nastro in movimento,
ritrasformati in numeri
quando ti servono.

<!-- S67 -->
Quindi la prossima volta che senti quello stridio,
ricordati che cos'è.
Non rumore.
Un programma che viaggia come suono.

<!-- S68 -->
E da qualche parte, nel 1985,
un ragazzino è seduto davanti a un televisore,
e aspetta che finisca.
Perché quando finisce,
comincia il gioco.

<!-- S69 -->
Allora ecco una domanda per te.
Se hai mai caricato un gioco da cassetta,
cosa ti ricordi di più?
Fammelo sapere nei commenti.

<!-- S70 -->
E come promesso, ecco quel programma.
Proprio come la televisione cecoslovacca,
l'abbiamo messo sotto i titoli di coda.
