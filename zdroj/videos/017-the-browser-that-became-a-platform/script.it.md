# Internet Explorer 6 — Il browser che divenne una piattaforma

Traduzione di `script.md`. Stesse marche di scena, stesso numero di righe.
Una riga = una frase = un sottotitolo.

<!-- S01 -->
Immagina di essere uno sviluppatore web
all'inizio degli anni duemila.

Hai scritto
una pagina web perfettamente ragionevole.

<!-- S02 -->
Funziona in Netscape.

Funziona in Opera.

Funziona nel nuovo Firefox.

E poi la apri
in Internet Explorer.

È tutto rotto.

<!-- S03 -->
Il layout è sbagliato.

I pulsanti si sono spostati.

Le immagini PNG sono orribili.

E in qualche modo
un solo a capo nel tuo HTML
ha creato uno spazio di tre pixel.

<!-- S04 -->
Benvenuto nello sviluppo web
nell'era di Internet Explorer 6.

Ma ecco la parte interessante.

Internet Explorer 6
non era semplicemente un brutto browser.

<!-- S05 -->
Microsoft stava cercando di risolvere problemi
che il web aveva davvero.

Aveva solo un vantaggio enorme
su tutti gli altri.

Windows.

<!-- S06 -->
E alla fine quel vantaggio
le permise di trasformare il browser
in qualcosa di molto più grande
di un browser.

<!-- S07 -->
A metà degli anni novanta
il web era dominato
da Netscape Navigator.

A Microsoft la cosa non piaceva.

<!-- S08 -->
Così Internet Explorer
venne incluso in Windows
e reso disponibile gratuitamente.

Compravi un computer con Windows.

Internet Explorer era già lì.

Niente da scaricare.

Niente da pagare.

<!-- S09 -->
E soprattutto,
Microsoft controllava
il sistema operativo.

Poco dopo il 2000,
Internet Explorer aveva
più del novanta per cento
del mercato dei browser.

<!-- S10 -->
Internet Explorer 6 arrivò
nel 2001,
insieme a Windows XP.

E per un po' sembrò
che Microsoft avesse semplicemente vinto
la guerra dei browser.

<!-- S11 -->
Microsoft aveva un problema.

Il web era estremamente limitato.

HTML sapeva mostrare documenti.

CSS sapeva dar loro uno stile.

JavaScript sapeva renderli interattivi.

<!-- S12 -->
E poco altro.

Qualunque cosa più complicata
sbatteva dritta
contro i limiti del browser.

<!-- S13 -->
E se volevi scansionare un documento?

O comunicare con una smart card?

O parlare con un pezzo
di hardware di Windows?

<!-- S14 -->
Il browser non sapeva
davvero fare queste cose.

Così Microsoft propose una soluzione.

ActiveX.

<!-- S15 -->
L'idea di base era semplice.

Perché limitare un'applicazione web
a ciò che sa fare il browser?

Lasciamole usare
componenti nativi di Windows.

<!-- S16 -->
E all'improvviso una pagina web
poteva fare cose
che l'HTML normale
non poteva nemmeno sognare.

<!-- S17 -->
Oggi ActiveX suona terrificante.

E a ragione.

Un componente ActiveX poteva arrivare
ai file, alle applicazioni,
all'hardware
e al sistema operativo.

<!-- S18 -->
Dal punto di vista odierno della sicurezza
sembra assolutamente folle.

Ma all'inizio degli anni duemila
aveva perfettamente senso
per le applicazioni aziendali.

<!-- S19 -->
Le aziende non volevano
un bel visualizzatore di documenti.

Volevano applicazioni.

Volevano pagine web
che si comportassero
quasi come software da scrivania.

<!-- S20 -->
E Microsoft diede loro esattamente questo.

Perfino Windows Update
si basava all'inizio su ActiveX
per esaminare il sistema
e capire quali aggiornamenti
servivano.

<!-- S21 -->
Quindi ActiveX non fu semplicemente
uno stupido errore.

Fu un tentativo precoce
di trasformare il browser
in una piattaforma applicativa.

<!-- S22 -->
E in questo senso Microsoft
era davvero avanti sui tempi.

Il problema era quanto potere
diede a quella piattaforma.

<!-- S23 -->
ActiveX non era
l'unica estensione di Microsoft.

C'era VBScript.

C'era DHTML.

E persino CSS expression.

Sì.

<!-- S24 -->
Internet Explorer sapeva valutare
JavaScript direttamente dentro il CSS.

Si poteva scrivere qualcosa così.

<!-- S25 -->
Era ridicolo.

E a volte anche
sorprendentemente utile.

E niente di tutto ciò era garantito
funzionare altrove.

<!-- S26 -->
Microsoft non stava semplicemente
implementando il web.

Microsoft stava estendendo il web
in una direzione propria.

E con il novanta per cento
del mercato
aveva abbastanza potere
perché la cosa funzionasse.

<!-- S27 -->
Uno degli esempi più famosi
era il box model dei CSS.

Il modello standard diceva
che se un elemento
era largo 200 pixel,
con 20 pixel di padding
e 5 pixel di bordo,

<!-- S28 -->
la larghezza totale
era di 250 pixel.

<!-- S29 -->
Le vecchie versioni di Internet Explorer
lo leggevano diversamente.

In modalità quirks la larghezza dichiarata
poteva includere il padding
e il bordo.

<!-- S30 -->
Non era necessariamente
un modo folle di pensare la larghezza.

Anzi, oggi chiediamo spesso
proprio questo comportamento di proposito.

Si chiama border-box.

<!-- S31 -->
Il vero problema era
che browser diversi
si comportavano in modo diverso.

E questo voleva dire
che allo sviluppatore doveva importare.

Molto.

<!-- S32 -->
C'era una cosa chiamata hasLayout.

Non era una normale proprietà CSS.

Non faceva parte dello standard.

Ma decideva
come Internet Explorer
disponeva gli elementi.

<!-- S33 -->
E a volte un layout rotto
si aggiustava misteriosamente
aggiungendo una sola riga.

zoom: 1

Perché?

Perché zoom: 1 poteva attivare
il meccanismo interno hasLayout.

<!-- S34 -->
C'erano problemi
con la trasparenza dei PNG.

C'erano problemi con gli elementi select,
che comparivano sopra
menu posizionati in modo assoluto,
per quanto alto
impostassi lo z-index.

<!-- S35 -->
Sviluppare per il web non era solo
realizzare il proprio progetto.

Era imparare i bug
di un motore di rendering preciso.

<!-- S36 -->
Ecco un altro esempio meraviglioso.

Gli spazi bianchi.

E di questo Internet Explorer
non aveva nemmeno colpa.

Potevi mettere due immagini
una accanto all'altra
nel markup,
senza niente fra i tag,
e ottenere un risultato.

<!-- S37 -->
Poi qualcuno formattava bene l'HTML
e metteva ogni tag su una riga propria.

E all'improvviso c'era
uno spazio di qualche pixel fra le immagini.

L'a capo diventava significativo.

<!-- S38 -->
Il tuo formattatore di codice
poteva letteralmente rompere la pagina.

E se usavi
una vecchia versione di Visual Studio,
ti formattava l'HTML
volentieri, da solo.

Grazie, Microsoft.

<!-- S39 -->
Gli sviluppatori accumularono
un'intera cassetta di espedienti.

I commenti condizionali.

<!-- S40 -->
E a volte HTML
dall'aspetto completamente bizzarro,
il cui unico scopo era
far comportare bene Internet Explorer.

<!-- S41 -->
Non scrivevi codice brutto
perché eri un cattivo programmatore.

Scrivevi codice brutto
perché il browser ti costringeva.

<!-- S42 -->
Internet Explorer andava anche in crash
in modo spettacolare, e spesso si portava dietro
tutte le finestre aperte.

<!-- S43 -->
Il che diede vita a una splendida categoria
di intrattenimento da ufficio.

Ehi, guarda questo link.

E venti finestre di Internet Explorer
spariscono.

<!-- S44 -->
Questo era il web prima che
i browser fossero isolati.

Il browser di oggi dice così.

Di questo sito non mi fido.

Lo isolo.

<!-- S45 -->
Internet Explorer 6
suonava piuttosto così.

Sei una pagina web?

Certo.

Ecco le chiavi dell'edificio.

<!-- S46 -->
Perché gli sviluppatori
usavano davvero questi trucchi?

Perché dovevano.

<!-- S47 -->
Immagina un'azienda
con cinquecento dipendenti.

Su ogni computer gira Windows XP.

Su ognuno c'è Internet Explorer.

<!-- S48 -->
Lo sviluppatore ha due opzioni.

Opzione uno.

Farlo per Internet Explorer,
che tanto hanno già tutti.

<!-- S49 -->
Opzione due.

Farlo per ogni browser,
testare tutto ovunque
e spiegare al reparto informatico
perché a tutti serve un secondo.

La risposta era di solito ovvia.

<!-- S50 -->
Non sceglievano
la tecnologia Microsoft
perché amavano Microsoft.

Sceglievano ciò che risolveva
il problema del cliente.

E a volte ActiveX
era lo strumento migliore disponibile.

<!-- S51 -->
E alla fine qualcuno ne ebbe abbastanza.

Le librerie JavaScript cominciarono
a nascondere le differenze fra browser.

Una delle più importanti
era jQuery.

<!-- S52 -->
Invece di scrivere
la gestione degli eventi per ogni browser,
scrivevi una sola riga
che funzionava ovunque.

<!-- S53 -->
Invece di destreggiarti a mano
fra diverse implementazioni di AJAX,
usavi un'astrazione comune.

<!-- S54 -->
jQuery non fece
sparire Internet Explorer.

Ma rese molto più facile
fare finta che non esistesse.

E per gli sviluppatori web di allora
era una meraviglia.

<!-- S55 -->
Comparve Firefox.

Opera continuò a svilupparsi.

Arrivò Safari.

E alla fine Google rilasciò Chrome.

<!-- S56 -->
Le guerre dei browser erano tornate,
e questa volta
la concorrenza era diversa.

I motori JavaScript
migliorarono enormemente.

Arrivò HTML5.

<!-- S57 -->
Il browser stesso cominciò a imparare
tutto ciò per cui gli sviluppatori
avevano avuto bisogno di plugin.

<!-- S58 -->
Video.

Audio.

Canvas.

SVG.

WebGL.

WebSockets.

E infine WebRTC.

Il web stava diventando
una piattaforma applicativa.

<!-- S59 -->
Che era esattamente
ciò che Microsoft aveva cercato
di ottenere con ActiveX.

Solo che ora accadeva
attraverso standard aperti.

<!-- S60 -->
Microsoft ci provò ancora una volta.

Silverlight permetteva di creare
applicazioni ricche nel browser
con C# e .NET.

Ci girava perfino
il primo streaming di Netflix.

<!-- S61 -->
Ma il web non voleva plugin per sempre.

Apple si rifiutò di supportare Flash
sull'iPhone.

E all'improvviso il futuro non era questo.

Browser più plugin.

Era questo.

Il browser stesso.

<!-- S62 -->
Silverlight sparì.

Flash sparì.

ActiveX sparì.

E alla fine sparì
anche Internet Explorer.

<!-- S63 -->
Ed è qui che
la storia si fa interessante.

Perché Microsoft
non aveva del tutto torto.

Aveva previsto correttamente
che il browser sarebbe diventato
una piattaforma applicativa.

<!-- S64 -->
Cercava solo di arrivarci
con tecnologie proprietarie.

Il web raggiunse la stessa meta
attraverso gli standard.

<!-- S65 -->
Il browser vinse.

Ma vinse diventando
qualcosa di molto più potente
del browser
del 2001.

<!-- S66 -->
Microsoft era dunque il cattivo?

In realtà no.

Ed è proprio questo che rende
la storia più interessante.

<!-- S67 -->
Microsoft aveva ingegneri eccellenti.

Aveva risorse enormi.

E costruì molte tecnologie
davvero in anticipo sui tempi.

<!-- S68 -->
Ma Microsoft aveva anche
una posizione di mercato schiacciante.

E questo creò
un incentivo pericoloso.

<!-- S69 -->
Se quasi tutti
usano il tuo browser,
perché aspettare gli standard?

Perché non implementare
semplicemente la tua soluzione?

Per un po' ha funzionato.

Finché il resto del web non l'ha raggiunta.

<!-- S70 -->
Oggi Internet Explorer non c'è più.

Le vecchie guerre dei browser
sembrano storia antica.

Ma guarda
il mercato dei browser di oggi.

Chrome.

Edge.

Opera.

Brave.

Vivaldi.

<!-- S71 -->
E molti altri
sono basati su Chromium.

Prodotti diversi.

Spesso lo stesso
motore sotto.

<!-- S72 -->
Forse quindi abbiamo scambiato questo.

Un browser che tutti dovevano supportare.

Con questo.

Un motore su cui tutti costruiscono.

Non ti suona familiare?

<!-- S73 -->
Perché un motore dominante
non decide solo
come vengono mostrati i siti.

<!-- S74 -->
Influenza ciò che gli sviluppatori costruiscono.

Quali tecnologie diventano popolari.

E alla fine anche
ciò che il web stesso diventa.

<!-- S75 -->
C'è però
una differenza molto importante.

Il web di oggi poggia
su standard aperti.

Firefox ha ancora un motore proprio.

Safari ha WebKit.

Chromium è open source.

<!-- S76 -->
E i browser moderni
si aggiornano da soli.

Siamo lontanissimi
dalla situazione
del 2003.

<!-- S77 -->
Ma la domanda di fondo resta.

Quanta influenza
dovrebbe avere una sola azienda
su una piattaforma
usata da quasi tutti?

È la domanda
che non è mai davvero sparita.

<!-- S78 -->
Allora, Internet Explorer 6 era terribile?

Sì.

A volte spettacolarmente terribile.

<!-- S79 -->
Ma non è tutta la storia.

Era anche un prodotto del suo tempo.

<!-- S80 -->
Il problema era
che Microsoft aveva vinto
le guerre dei browser così del tutto
da poter dettare le regole.

<!-- S81 -->
E a pagarne il prezzo furono gli sviluppatori.

Impararono i misteri
di hasLayout.

Scoprirono che zoom: 1
sistemava le cose come per magia.

E pregavano.

<!-- S82 -->
E alla fine Internet Explorer
divenne ciò che aveva passato
vent'anni a costruire.

Una piattaforma obsoleta
che nessuno voleva più
mantenere.

<!-- S83 -->
Il web non ha rifiutato
la visione di Microsoft.

Ne ha semplicemente costruito
una versione migliore.

E se quell'epoca
deve insegnarci una cosa,
è questa.

<!-- S84 -->
Una tecnologia non diventa uno standard
solo perché è buona.

<!-- S85 -->
A volte diventa uno standard
perché un'azienda ha abbastanza potere
da farla usare a tutti.

<!-- S86 -->
E a volte,
vent'anni dopo,
ci accorgiamo di averlo rifatto.
