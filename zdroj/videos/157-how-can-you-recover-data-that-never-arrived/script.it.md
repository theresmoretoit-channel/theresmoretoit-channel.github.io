<!-- S01 -->
Questo è un codice QR.
Contiene una breve riga di testo.

<!-- S02 -->
Il telefono lo legge subito.

<!-- S03 -->
Ora strappiamone un pezzo.

<!-- S04 -->
E scansioniamolo di nuovo.
Lo stesso testo.
Ogni singola lettera.

<!-- S05 -->
Una parte di quel codice non c'è più.
Non è che sia difficile da leggere.
Non c'è più.

<!-- S06 -->
Allora, come fa un telefono a leggere qualcosa
che lì non c'è più?

<!-- S07 -->
Ecco lo stesso problema, in piccolo.
Qualcuno vi manda otto bit.
Lungo la strada, tre vanno persi.

<!-- S08 -->
Ogni bit mancante è uno zero o un uno,
quindi ci sono otto modi per riempire i vuoti.
E niente di ciò che è arrivato
vi dice qual è quello giusto.

<!-- S09 -->
Eppure il telefono ha appena fatto proprio questo.
Non stava tirando a indovinare.
La risposta era stata inviata
prima che andasse perso qualcosa.

<!-- S10 -->
Il trucco è inviare qualcosa in più
oltre al messaggio stesso.

<!-- S11 -->
Il modo più semplice
è dire tutto tre volte.
Uno zero viene inviato come tre zeri,
un uno come tre uno.

<!-- S12 -->
Il rumore ne inverte uno,
e voi ricevete uno, zero, uno.
Due voti contro uno.
Quasi certamente era un uno.

<!-- S13 -->
Se il rumore inverte un bit su dieci,
a caso e in modo indipendente,
una votazione a tre sbaglia
meno di tre volte su cento.

<!-- S14 -->
Ma avete triplicato
tutto quello che inviate.
Per avvicinarvi alla perfezione,
dovreste ripetere cinque volte, poi nove,
poi cento...
e il messaggio andrebbe a passo di lumaca.

<!-- S15 -->
Per molto tempo,
sembrava che quello fosse il prezzo.
Meno errori, messaggi più lenti.
Tenetelo a mente.

<!-- S16 -->
Alla fine degli anni '40,
Richard Hamming, ai Bell Labs,
aveva un problema tutto suo.

<!-- S17 -->
Riusciva a usare un computer a relè soprattutto
nei fine settimana,
quando non c'era nessuno a sorvegliarlo.

<!-- S18 -->
La macchina sapeva accorgersi
di quando aveva commesso un errore.
Ritentava il passaggio,
tre volte...
e poi abbandonava il suo calcolo.
Per due fine settimana di fila,
ha perso tutto il lavoro.

<!-- S20 -->
La sua domanda, con le sue parole:
"Se la macchina riesce a capire
che c'è un errore,
perché non riesce a capire dov'è?"
Le parole vere, ha ammesso,
erano probabilmente un po' più colorite.

<!-- S22 -->
La sua risposta prende quattro bit di messaggio
e aggiunge tre bit di controllo.
Sette bit in tutto.

<!-- S23 -->
Ogni bit di controllo si occupa
di un gruppo diverso di posizioni,
e fa sì che quel gruppo
contenga un numero pari di uno.

<!-- S24 -->
I gruppi si sovrappongono secondo uno schema preciso.
Ogni posizione appartiene
alla propria combinazione di gruppi.

<!-- S25 -->
Ora invertite un bit.
Diciamo, quello in posizione sei.

<!-- S26 -->
Il ricevitore ripete i tre controlli.
Il primo passa.
Il secondo fallisce.
Il terzo fallisce.

<!-- S27 -->
Scrivete un controllo fallito come uno,
uno superato come zero,
e leggeteli dall'ultimo al primo.
Uno, uno, zero.
In binario, fa sei.

<!-- S28 -->
I controlli non dicono soltanto
che qualcosa è andato storto.
Indicano il bit esatto.

<!-- S29 -->
Rimettetelo com'era,
e il messaggio torna integro.
Nessuno ha dovuto inviare niente due volte.

<!-- S30 -->
Ecco quindi la risposta.
Il ricevitore non ricostruisce
dal nulla le informazioni perse.
Il mittente ce le aveva messe dentro
in anticipo.

<!-- S32 -->
Non tutti i controlli ci riescono.
Una somma di controllo, come quella del nostro video
su Btrfs,
può dirvi che un blocco è danneggiato,
ma non quali fossero i dati originali.

<!-- S33 -->
E c'è un secondo tipo di danno.
A volte un bit non è sbagliato.
Semplicemente manca,
e sapete esattamente dov'è il buco.

<!-- S34 -->
Questa si chiama cancellazione,
e le cancellazioni sono più facili.

<!-- S35 -->
Inviate quattro numeri,
4, 7, 2 e 9,
e un quinto:
la loro somma, 22.

<!-- S36 -->
Se uno qualsiasi va perso,
gli altri vi dicono qual era.
4, 7, qualcosa, 9,
22.
Deve per forza essere 2.

<!-- S37 -->
I server proteggono i loro dischi
con un controllo simile,
distribuito tra le unità.
Quando un'unità si guasta,
il suo contenuto si ricava dalle altre.

<!-- S38 -->
Allora, quanto serve in più?
La ripetizione dice:
per portare gli errori a zero,
dovete portare anche la velocità a zero.

<!-- S39 -->
Due anni prima che uscisse
l'articolo di Hamming,
il suo collega Claude Shannon
aveva pubblicato una risposta più strana.

<!-- S40 -->
Ogni canale,
un collegamento radio, un cavo, un disco,
ha un limite.
Una velocità massima per l'informazione.

<!-- S41 -->
Sotto quel limite,
gli errori si possono rendere rari quanto volete,
senza rallentare.
Non ripetendo di più.
Codificando in modo più intelligente.

<!-- S42 -->
Sopra,
nessun codice al mondo può aiutarvi.

<!-- S43 -->
Ma c'era un problema.
Shannon ha dimostrato che codici del genere esistono.
Non ha mostrato come costruirne uno
che qualcuno potesse davvero usare.

<!-- S44 -->
Secondo la sua dimostrazione, un codice scelto a caso
sarebbe stato quasi certamente buono.
Ma il modo più ovvio per decodificarlo
richiede di confrontare ciò che è arrivato
con ogni messaggio possibile...
e per un blocco di 1.000 bit,
i messaggi possibili sono più numerosi
degli atomi nell'universo.

<!-- S46 -->
Quindi l'articolo di Shannon non era una soluzione.
Era una promessa.
E gli ingegneri hanno passato i successivi
45 anni a cercare di mantenerla.

<!-- S47 -->
Il codice di Hamming è stato un primo passo.
Corregge un bit sbagliato su sette.

<!-- S48 -->
Ma i danni reali arrivano a raffiche.
Un graffio o una scarica di disturbi
si porta via centinaia di bit di fila.

<!-- S49 -->
Nel 1960, Irving Reed e Gustave Solomon,
al Lincoln Laboratory del MIT,
hanno pubblicato un articolo di cinque pagine.

<!-- S50 -->
I loro codici lavorano su byte interi,
non su singoli bit.
Se una raffica distrugge tutti gli otto bit
di un byte,
resta comunque un solo byte sbagliato.

<!-- S51 -->
Una versione comune aggiunge
32 byte di controllo
a 223
byte di dati.

<!-- S52 -->
Può correggere 16 byte qualsiasi
che arrivano sbagliati...
o ricostruirne 32
che non arrivano affatto.

<!-- S53 -->
È così che un CD graffiato suona lo stesso.
I suoi due codici di Reed-Solomon
possono riparare del tutto un buco
di circa 4.000 bit,
2,5 millimetri di traccia.

<!-- S54 -->
Ed è per questo che il codice QR strappato
funzionava ancora.
Al livello più alto,
un codice QR può ricostruire
fino a circa il 30% dei suoi byte
e restituire comunque ogni lettera.

<!-- S56 -->
La Voyager 2 ha lasciato la Terra nel 1977
con già a bordo un codificatore Reed-Solomon.

<!-- S57 -->
Ma a Giove e Saturno,
proteggeva tutto tranne le immagini
con un codice più vecchio, di Marcel Golay,
che inviava un bit in più
per ogni bit di dati.

<!-- S58 -->
Per Urano e Nettuno,
con un segnale sempre più debole,
gli ingegneri hanno attivato Reed-Solomon,
in aggiunta a un secondo codice
che veniva già applicato a ogni bit.

<!-- S59 -->
Con il solo secondo codice,
circa cinque bit su mille
erano ancora sbagliati.
Con Reed-Solomon in aggiunta,
circa uno su un milione.

<!-- S60 -->
Anche il rumore arriva a raffiche,
quindi la Voyager mescolava
i byte di quattro blocchi
prima di inviarli.

<!-- S61 -->
Una raffica che avrebbe distrutto un blocco
ora porta via pochi byte da ciascuno...
abbastanza pochi perché ogni blocco
possa ripararsi da solo.

<!-- S62 -->
Il resto del viaggio delle immagini di Nettuno
fino a casa
è nel nostro video sulla Voyager.

<!-- S63 -->
Ma anche questo
non arrivava ancora al limite di Shannon...
e un codice che poteva avvicinarsi molto di più
esisteva già.

<!-- S65 -->
Nel 1960, nella sua tesi di dottorato al MIT,
Robert Gallager ha descritto codici
fatti di tanti controlli semplici,
ognuno dei quali guarda solo pochi bit.

<!-- S66 -->
Per decodificarli, i controlli dovevano
passarsi ipotesi avanti e indietro,
un giro dopo l'altro...
decisamente troppo
per i computer degli anni '60.
Così l'idea è stata messa da parte,
e quasi dimenticata per 30 anni.

<!-- S68 -->
Nel 1993,
un gruppo guidato da due ingegneri francesi,
Claude Berrou e Alain Glavieux,
ha presentato i turbo codici
a una conferenza a Ginevra.

<!-- S69 -->
I loro risultati erano così vicini
al limite di Shannon
che molti esperti hanno pensato
che avessero fatto un errore.
Probabilmente un fattore due,
da qualche parte nei calcoli.

<!-- S70 -->
Nel giro di un anno,
altri laboratori avevano confermato i risultati.

<!-- S71 -->
Anche i turbo codici funzionavano
passandosi ipotesi avanti e indietro,
e questo ha riportato l'attenzione su Gallager.

<!-- S72 -->
Nel 1995 e nel 1996,
David MacKay e Radford Neal
hanno riscoperto i suoi codici,
e hanno dimostrato che potevano arrivare
altrettanto vicino.

<!-- S73 -->
Nel 2001,
una versione perfezionata dei codici di Gallager
è arrivata a 0,04 decibel
dal limite di Shannon.

<!-- S74 -->
È meno dell'uno per cento
di potenza del segnale in più
rispetto al minimo teorico.
La promessa del 1948 era stata mantenuta.

<!-- S75 -->
Oggi i codici di Gallager trasportano
gran parte dei dati nei telefoni 5G,
nel Wi-Fi moderno
e nella televisione satellitare.

<!-- S77 -->
Ora, torniamo ai nostri otto bit.
Tre sono andati persi,
e ci sono otto modi
per riempire i vuoti.

<!-- S78 -->
Ma questi otto bit
non sono mai stati solo un messaggio.
Contenevano quattro bit di dati,
i tre controlli di Hamming,
e un altro controllo su tutti e otto.

<!-- S79 -->
Tra tutte le 256
combinazioni possibili di otto bit,
solo 16 rispettano queste regole.

<!-- S80 -->
Provate gli otto candidati.
Uno dopo l'altro, falliscono.
Ne resta solo uno.

<!-- S81 -->
I bit mancanti non erano mai spariti davvero.
La loro informazione era ancora lì,
nei bit sopravvissuti.

<!-- S82 -->
Allora, ecco una domanda per voi.
Vi è mai capitato di notare la correzione degli errori
all'opera in qualcosa che usate ogni giorno?
Fatemelo sapere nei commenti.
