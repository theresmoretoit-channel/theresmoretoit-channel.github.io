<!-- S01 -->
Questo è uno ZX Spectrum che carica un programma.

<!-- S02 -->
E questo è lo stesso programma,
sullo stesso computer,
dallo stesso tipo di cassetta.

<!-- S03 -->
Finisce in metà tempo.
Nell'hardware non è cambiato niente.
Nessun nastro più veloce, nessun registratore più veloce.

<!-- S04 -->
L'unica cosa cambiata
era il modo in cui il computer ascoltava.

<!-- S05 -->
Allora, come hanno fatto i computer a 8 bit
a imparare a caricare i giochi più in fretta?
E se era così facile,
perché non l'hanno fatto fin dall'inizio?

<!-- S06 -->
In un video precedente
abbiamo visto come lo Spectrum memorizza i bit
sotto forma di impulsi sul nastro.

<!-- S07 -->
Una coppia di impulsi brevi significa zero.
Una coppia lunga il doppio significa uno.

<!-- S08 -->
Fanno circa millequattrocento bit
al secondo.
Un gioco che riempie i 48K di memoria
ci mette circa cinque minuti.

<!-- S09 -->
Ora rendi ogni impulso lungo la metà.

<!-- S10 -->
Il computer distingue ancora il breve dal lungo.
Ma il doppio dei bit
passa sotto la testina ogni secondo.

<!-- S11 -->
È tutto qui il trucco di un caricatore turbo.
E non è solo un esperimento mentale.

<!-- S12 -->
Nel 1984, il gioco Skool Daze
caricava i suoi dati al doppio
della velocità normale dello Spectrum.

<!-- S13 -->
Allora perché lo Spectrum
non caricava così veloce da solo?

<!-- S14 -->
Il caricatore integrato sta nella ROM,
il chip di memoria da cui il computer si avvia.
Non misura un impulso in secondi.

<!-- S15 -->
Conta.
Dopo ogni fronte del segnale,
aspetta un attimo,
poi conta quanto tempo passa fino al successivo.

<!-- S16 -->
Un solo numero nella ROM
decide dove finisce lo zero
e comincia l'uno.

<!-- S17 -->
E quel numero lascia parecchio margine.
Uno zero può allungarsi
di oltre il quaranta per cento
ed essere ancora letto come zero.

<!-- S18 -->
È quel margine che permette a un nastro consumato
su un registratore economico
di caricarsi comunque.

<!-- S19 -->
E il limite non era il computer.
Lo Spectrum controlla il segnale del nastro
circa sessantamila volte al secondo.

<!-- S20 -->
Il limite era la cassetta.
Impulsi più brevi vogliono dire toni più acuti.
A velocità doppia, uno zero
passa da due kilohertz a quattro.

<!-- S21 -->
E i toni acuti sono proprio ciò che
un registratore economico,
o una testina un po' disallineata,
perde per primo.

<!-- S22 -->
Una rivista sullo Spectrum nel 1986 stimava
che la maggior parte della gente potesse arrivare
almeno al doppio della velocità normale.
Quanto più in là si potesse andare
dipendeva dal registratore.

<!-- S23 -->
Ma il turbo aveva un problema più strano.

<!-- S24 -->
Se il computer conosce solo
il formato lento,
come fa a caricare il programma
che gli insegna quello veloce?

<!-- S25 -->
La risposta è all'inizio del nastro.
La prima parte è registrata
nel formato normale, quello lento.

<!-- S26 -->
È breve,
e la ROM la carica come qualsiasi altro programma.

<!-- S27 -->
Poi quel programmino prende il controllo.
Nel caso più semplice,
è una copia della routine di caricamento della ROM stessa,
con qualche numero cambiato.

<!-- S28 -->
In Skool Daze,
le modifiche stanno in tre punti.
Un'attesa più breve, un nuovo valore di partenza del conteggio,
una nuova linea di demarcazione.

<!-- S29 -->
Quindi la ROM carica il programma
che fa il lavoro della ROM, solo più veloce.

<!-- S30 -->
È un po' come scaricare
un programma per scaricare più veloce.
Il passaggio lento ti procura lo strumento.
Lo strumento fa il resto.

<!-- S31 -->
I giochi commerciali usarono la stessa idea.
Un esempio famoso fu Speedlock,
usato per la prima volta da Ocean nel 1984.

<!-- S32 -->
Uno dei suoi autori raccontò di averlo scritto
perché era stufo
di quanto ci metteva il caricatore standard.

<!-- S33 -->
Ma ecco la sorpresa.
Speedlock era solo circa una volta e mezzo
più veloce.

<!-- S34 -->
Il primo giorno
di Daley Thompson's Decathlon
ci metteva tre minuti e venti secondi,
mentre gli stessi dati a velocità normale
avrebbero richiesto quattro minuti e quarantasette.

<!-- S35 -->
Le versioni successive erano solo circa
un quinto più veloci della ROM.
Perché la velocità non era l'unico scopo.

<!-- S36 -->
Dal 1983, i programmi di copia
sapevano leggere l'intestazione di un gioco
e copiare il gioco intero su un altro nastro.

<!-- S37 -->
Un formato personalizzato
lasciava quei programmi senza niente da leggere.

<!-- S38 -->
Il primo Speedlock spezzettava perfino il tono pilota
in brevi raffiche,
così che il caricatore della ROM stessa
non lo riconoscesse proprio.

<!-- S39 -->
E si sentiva.
Un nastro Speedlock si caricava tra i clic,
con strisce che sussultavano attorno allo schermo.

<!-- S40 -->
Non impediva a nessuno di copiare
un nastro da un registratore all'altro.
Ma diede agli editori
un motivo per scriversi i propri caricatori.

<!-- S41 -->
Sul Commodore 64,
il motivo per cambiare era molto più forte.

<!-- S42 -->
La sua routine integrata
registrava tutto due volte,
come copia di sicurezza.
Un gioco da quaranta kilobyte richiedeva
circa dodici minuti e mezzo.

<!-- S43 -->
E qui il registratore
non faceva quasi niente di furbo.
Trasformava solo il suono
in impulsi puliti, acceso e spento.

<!-- S44 -->
Era il computer a cronometrare ogni impulso,
via software.

<!-- S45 -->
Quindi un caricatore più veloce
era solo un programma diverso.

<!-- S46 -->
Nel 1985, la rivista Compute!
ne provò uno chiamato TurboTape.

<!-- S47 -->
Una volta trovato il programma sul nastro,
caricò dodici kilobyte
in ventotto secondi.

<!-- S48 -->
Il lettore di floppy della Commodore stessa
ci mise trentaquattro secondi.

<!-- S49 -->
Una cassetta
che batte un floppy disk.

<!-- S50 -->
E siccome era il computer stesso
ad ascoltare il segnale,
poteva fare anche altre cose nel frattempo.

<!-- S51 -->
Caricatori come Freeload
davano la priorità alla lettura del nastro.
Il tempo di processore che avanzava
andava a musica, scorrimento fluido,
perfino piccoli giochi.

<!-- S52 -->
Con Invade-a-Load di Mastertronic,
giocavi a un clone di Space Invaders
mentre si caricava il gioco vero.

<!-- S53 -->
I computer Atari a 8 bit
erano un'altra storia.

<!-- S54 -->
Qui ad ascoltare era il registratore.
Dentro c'erano due filtri,
uno per ogni tono,
e un circuito che passava al computer
uni e zeri già pronti.

<!-- S55 -->
Lo standard era di seicento bit al secondo,
e i filtri limitavano
quanto si potesse andare più veloci.

<!-- S56 -->
Un software ingegnoso poteva salire
di poco, al massimo a circa milleduecento.
Ma per andare molto più veloci,
bisognava aprire il registratore.

<!-- S57 -->
E in Cecoslovacchia, la gente lo aprì.

<!-- S58 -->
Lì un lettore di floppy
costava due o tre volte
più del computer stesso.
Così lì la maggior parte dei possessori di Atari restò alle cassette.

<!-- S59 -->
Nel 1987, uno studente di Praga
del club Atari locale
progettò Turbo 2000.

<!-- S60 -->
Aggiungeva un nuovo percorso per il segnale.
Un filo dentro il registratore prendeva il suono
direttamente dal suo amplificatore,
prima dei filtri,
lo faceva passare per un piccolo chip
e poi sulla linea verso il computer.

<!-- S61 -->
Un commutatore, azionato dal computer,
sceglieva tra il vecchio percorso e il nuovo.

<!-- S62 -->
Ora era il computer a cronometrare gli impulsi.
Circa duemilatrecento bit
al secondo.
Quasi quattro volte più veloce.

<!-- S63 -->
Il turbo non era un unico formato universale.

<!-- S64 -->
A volte cambiavi il programma.
A volte dovevi cambiare la macchina.

<!-- S65 -->
E la velocità non era gratis.

<!-- S66 -->
Compute! avvertiva che una registrazione TurboTape
a volte non voleva saperne di caricarsi
su un registratore diverso,
con la testina allineata in modo leggermente diverso.

<!-- S67 -->
Il salvataggio standard, diceva,
era molto più lento,
ma estremamente affidabile.

<!-- S68 -->
Registrare tutto due volte
non era pigrizia da parte di Commodore.
Era il prezzo di un caricamento affidabile.

<!-- S69 -->
Ma un caricatore diverso
poteva anche fare qualcosa di inatteso.
Poteva leggere un nastro
che quello integrato rifiutava.

<!-- S70 -->
Sullo Sharp MZ-800,
un computer arrivato
in Cecoslovacchia alla fine degli anni '80,
i possessori conoscevano un programma chiamato Turbo Copy.

<!-- S71 -->
Un gioco non si caricava,
con un errore di checksum.
I possessori scoprirono che Turbo Copy
spesso riusciva a caricarlo lo stesso.

<!-- S72 -->
Poi lo salvavi a velocità normale
su una cassetta nuova,
e il computer
lo caricava di nuovo normalmente.
Sembrava di riparare un gioco rotto.

<!-- S73 -->
Allora come poteva un caricatore leggere
quello che l'altro non riusciva a leggere?

<!-- S74 -->
La ROM dello Sharp registrava ogni blocco due volte,
a circa milleduecento bit al secondo.

<!-- S75 -->
E non misurava mai un impulso.
Dopo l'inizio di ogni impulso,
aspettava un tempo fisso
e guardava una volta sola.

<!-- S76 -->
Ancora alto?

<!-- S76b -->
È un uno.

<!-- S76c -->
Già basso?

<!-- S76d -->
È uno zero.

<!-- S77 -->
Un cronometro, regolato in anticipo.

<!-- S78 -->
Su un nastro vecchio, o un registratore diverso,
gli impulsi tornavano un po' più arrotondati.
E allora con quell'unica occhiata
si poteva leggere il livello sbagliato.

<!-- S79 -->
Un solo bit sbagliato rovina il checksum.
Se falliscono entrambe le copie,
il caricamento fallisce.

<!-- S80 -->
Turbo Copy ascoltava in modo diverso.
Cronometrava ogni impulso
con il chip timer del computer.

<!-- S81 -->
E prima di ogni blocco,
ascoltava il tono pilota
e fissava la sua linea di demarcazione
in base agli impulsi che sentiva davvero.

<!-- S82 -->
Il suo cronometro era regolato
sul nastro che aveva davanti.

<!-- S83 -->
E la riparazione non era una copia del suono.
Turbo Copy teneva i byte
e scriveva un segnale tutto nuovo,
con impulsi dalla durata precisa.

<!-- S84 -->
I dati non erano andati persi.
Era il modo solito di leggerli
che non era abbastanza buono.

<!-- S84b -->
Turbo Copy poteva anche salvare il gioco in turbo,
a due o tre volte la velocità normale,
con un suo piccolo caricatore davanti.

<!-- S85 -->
Ed è questo che tutti questi trucchi
hanno in comune.

<!-- S86 -->
La cassetta restava la stessa.
Cambiava il modo in cui veniva letta.

<!-- S87 -->
Oggi ci aspettiamo che i giochi si carichino all'istante.
Negli anni '80, il caricamento faceva parte del gioco.
Ascoltavi il nastro.
Guardavi le strisce.
Aspettavi.

<!-- S88 -->
E a volte, un caricatore diverso
faceva sì che la stessa cassetta si comportasse
come una macchina completamente diversa.

<!-- S89 -->
Il computer non aveva bisogno di un nastro più veloce.
Aveva bisogno di un modo migliore di ascoltare.

<!-- S90 -->
Allora, ecco una domanda per te.
Usavi i caricatori turbo all'epoca?
Che ricordo ne hai?
Fallivano più spesso?
Fammelo sapere nei commenti.

<!-- S91 -->
E infine, l'intero nastro turbo,
dall'inizio alla fine.
Prima la parte a velocità normale,
poi il turbo.
Per un programma così piccolo,
il turbo non conviene.
Il caricatore ci mette più tempo
di quello che fa risparmiare.
Con un gioco intero, poteva far risparmiare minuti.
