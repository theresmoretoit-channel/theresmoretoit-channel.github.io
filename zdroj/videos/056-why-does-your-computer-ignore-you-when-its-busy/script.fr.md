<!-- S01 -->
Tu cliques sur un bouton.
Rien ne se passe.
Tu cliques encore.
Toujours rien.

<!-- S02 -->
Tu bouges la souris.
Rien.
Pendant quelques secondes,
l'ordinateur a l'air mort.

<!-- S03 -->
Et puis tout arrive d'un coup.
La fenêtre bouge.
Le menu s'ouvre.
Tous tes clics arrivent,
tous ensemble.

<!-- S04 -->
Et voilà le plus étrange.
L'ordinateur savait que tu avais cliqué.
Il l'a su en quelques microsecondes.

<!-- S05 -->
Ce n'est pas une supposition.
En ce moment même, alors que
tu ne fais rien de particulier,
ta machine traite des milliers
d'événements matériels par seconde.

<!-- S06 -->
Une touche enfoncée.
Un paquet qui arrive.
Une minuterie qui sonne.
Un disque qui a fini.

<!-- S07 -->
Chacun d'eux est une interruption,
et les ordinateurs font ça
depuis les années cinquante,
exactement pour cette raison :

<!-- S08 -->
pour qu'un processeur puisse réagir
au monde en dehors de lui.

<!-- S09 -->
Le matériel a donc signalé ton clic.
Le processeur l'a remarqué.
Et tu es quand même resté cinq secondes
devant un écran mort.

<!-- S10 -->
L'utilisateur ne passe-t-il pas avant ?

<!-- S11 -->
Il y a une réponse,
et ce n'est pas
que ton ordinateur est trop lent.

<!-- S12 -->
C'est qu'être remarqué
et être servi
sont deux choses très différentes.

<!-- S13 -->
Commençons par le fait de remarquer.
Imagine un ordinateur sans interruptions.

<!-- S14 -->
Le processeur devrait
demander sans arrêt :
le clavier a-t-il reçu quelque chose ?
le disque a-t-il fini ?

<!-- S15 -->
Un paquet est-il arrivé ?
La souris a-t-elle bougé ?
Et puis redemander.
Et encore.

<!-- S16 -->
Presque toutes les réponses seraient non,
et le fait même de demander
dévorerait la machine.

<!-- S17 -->
Les appareils ont donc eu le moyen
de lever la main. La souris bouge,
le matériel déclenche une interruption,

<!-- S18 -->
et le processeur lâche
ce qu'il était en train de faire,
saute dans un court bout de code
qu'on appelle un gestionnaire,

<!-- S19 -->
et le système d'exploitation apprend
que quelque chose s'est passé.

<!-- S20 -->
C'est une idée brillante.
Et elle mène à une hypothèse
tout à fait raisonnable.

<!-- S21 -->
Si on peut arracher le processeur
à n'importe quoi, sur-le-champ,
alors mon clic sera sûrement
traité sur-le-champ aussi.

<!-- S22 -->
Sauf que le gestionnaire n'a pas
le droit de faire grand-chose.

<!-- S23 -->
Tant que le processeur est dedans,
tout le reste attend.
Y compris l'interruption suivante.
Et elle arrive déjà.

<!-- S24 -->
La règle est donc l'inverse exact
de ce qu'on attendrait.
Le gestionnaire en fait aussi peu
que possible.

<!-- S25 -->
Il note ce qui s'est passé.
Il confirme à l'appareil
que le message est arrivé.
Il dépose l'événement dans une file.
Et il s'en va.

<!-- S26 -->
Les développeurs de noyaux coupent
même le travail en deux moitiés :
ce qui doit arriver tout de suite,
et ce qui peut attendre.

<!-- S27 -->
Tout ce qui est intéressant,
tout ce que tu verras un jour,
est dans la seconde moitié.

<!-- S28 -->
Et voilà la première réponse.
Une interruption obtient
l'attention de l'ordinateur.

<!-- S29 -->
Elle ne met pas ton programme
sur un processeur.

<!-- S30 -->
Très bien, dis-tu. Alors répare ça.
Fais de l'entrée la chose
la plus importante de la maison.

<!-- S31 -->
La souris ? Priorité maximale.
Le clavier ? Priorité maximale.
La fenêtre devant toi ?
Priorité maximale.

<!-- S32 -->
Tout le reste peut attendre son tour.
Ça paraît évidemment juste.

<!-- S33 -->
Et la meilleure objection
s'est produite sur Mars.

<!-- S34 -->
En 1997, l'atterrisseur Pathfinder
s'est posé et s'est mis au travail.
Puis, quelques jours après,
il a commencé à redémarrer seul.

<!-- S35 -->
Pas un rayon cosmique.
Pas une pièce cassée.
Un problème d'ordonnancement.

<!-- S36 -->
Il y avait une tâche à priorité haute
qui distribuait des données
dans toute la sonde,
et il lui fallait une mémoire partagée.

<!-- S37 -->
Une tâche à priorité basse,
qui collectait des données météo,
y était arrivée la première
et la gardait.

<!-- S38 -->
Ce qui, un instant,
n'aurait posé aucun problème.
Mais une tâche à priorité moyenne
a ensuite pris le processeur,

<!-- S39 -->
et celle à priorité basse
n'a jamais pu finir.
Elle n'a donc jamais rien lâché.

<!-- S40 -->
La tâche la plus importante
de toute la sonde
était maintenant coincée derrière
la moins importante de toutes.

<!-- S41 -->
Ça porte un nom.
L'inversion de priorité.

<!-- S42 -->
Un minuteur de surveillance a vu
que la tâche importante
n'avait pas tourné depuis trop longtemps,
a conclu à la catastrophe,

<!-- S43 -->
et a redémarré toute la sonde.
Puis c'est arrivé encore.
Et encore.

<!-- S44 -->
Des ingénieurs sur Terre ont compris
et ont envoyé un correctif vers Mars.

<!-- S45 -->
Et la leçon ne nous coûte
absolument rien.
Priorité haute ne veut pas dire
qu'on te sert.

<!-- S46 -->
Ça veut dire qu'on te demande d'abord.
Si ce dont tu as besoin
est tenu par quelqu'un de plus lent,
ton importance ne t'achète rien.

<!-- S47 -->
Et la priorité a une seconde limite.
Elle décide de l'ordre.
Elle ne crée pas un seul
cycle de plus.

<!-- S48 -->
Admettons que tous tes cœurs
soient à cent pour cent.
Tu penses que ça veut dire figé.
En général, non.

<!-- S49 -->
L'ordonnanceur distribue des tranches
de temps si vite
que tu ne sens pas les transitions.

<!-- S50 -->
C'est pour ça que tu peux compiler
quelque chose d'énorme
et faire défiler une page web
en même temps.

<!-- S51 -->
Sous charge, ce qui change
n'est pas vraiment la vitesse.
L'ordinateur n'est pas lent.

<!-- S52 -->
Il est en retard.

<!-- S53 -->
Tu cliques, et la réponse arrive
une demi-seconde plus tard.
Puis une seconde.
Puis cinq.

<!-- S54 -->
Et les gens remarquent ça
extraordinairement bien.
Une demi-seconde, on dirait
une machine qui réfléchit.

<!-- S55 -->
Cinq secondes, on dirait
une machine qui est morte.

<!-- S56 -->
Et il existe une version de tout ça
qui surprend le plus.
Parfois le problème n'est
pas du tout le processeur.

<!-- S57 -->
Ouvre trop de choses d'un coup
et la mémoire physique se remplit.
Le système se met à déplacer
des pages vers le disque.

<!-- S58 -->
Qu'il y en ait assez,
et la machine passe son temps
à remuer de la mémoire
au lieu de faire ton travail.

<!-- S59 -->
Ça aussi porte un nom.
Le thrashing.

<!-- S60 -->
Et c'est là que ça devient déroutant,
parce que le processeur
peut n'avoir l'air de rien faire.

<!-- S61 -->
Il ne travaille pas.
Il attend.

<!-- S62 -->
Tu peux donner à une tâche qui attend
la priorité la plus haute du système,
elle attendra exactement
aussi longtemps.

<!-- S63 -->
Et puis il y a la version
la plus humaine de tout ça.
L'événement est arrivé.
Le noyau l'a.

<!-- S64 -->
Il est posé dans une file
au nom de ton programme.
Et ton programme
ne vient pas le chercher.

<!-- S65 -->
Peut-être qu'il fait un long calcul
sur le thread même
qui est censé surveiller
sa propre fenêtre.

<!-- S66 -->
Donc la souris marche.
Le clavier marche.
Les autres programmes marchent.

<!-- S67 -->
Et cette fenêtre-là pâlit
et annonce qu'elle ne répond pas.

<!-- S68 -->
Ce n'est pas un diagnostic.
Windows colle cette étiquette
au bout d'environ cinq secondes
sans que personne relève les messages.

<!-- S69 -->
Le système est parfaitement vivant.
C'est l'application
qui n'est pas venue à la porte.

<!-- S70 -->
Que l'ordinateur reçoive ton clic
et que l'application y réponde,
ce ne sont pas les mêmes événements.

<!-- S70b -->
Au fait, si vous voulez voir
où nous mène la prochaine question,
pensez à vous abonner.

Ça aide vraiment la chaîne.
<!-- S71 -->
Il reste un maillon,
et c'est justement celui
auquel on ne pense jamais.
Rien de tout ça n'a encore mis
quoi que ce soit à l'écran.

<!-- S72 -->
L'application change son état.
Quelqu'un doit monter l'image suivante.
La carte graphique doit la dessiner.
L'écran doit l'afficher.

<!-- S73 -->
Sur un écran ordinaire,
une nouvelle image apparaît
toutes les seize millisecondes environ.

<!-- S73b -->
Il y a donc une différence entre
l'ordinateur qui traite ton clic
et toi qui le vois.

<!-- S74 -->
Et tout en dessous
se trouve la partie
qu'aucune technique ne résout.
Le système d'exploitation sait
que la souris a bougé.
Pourquoi, il n'en a aucune idée.

<!-- S75 -->
Tu vises peut-être quelque chose
dans un jeu.
Ou tu modifies un document.
Ou tu as cogné le bureau.

<!-- S76 -->
Pour le matériel,
ce sont les mêmes événements.
Un système sait classer des travaux.
Deviner, il ne sait pas.

<!-- S77 -->
Alors il fait un compromis.
Assez rapide pour toi,
la plupart du temps,
sans faire attendre le reste sans fin.

<!-- S78 -->
Ce qui nous ramène
à cet écran mort.
Ton clic n'a jamais été un seul événement.

<!-- S79 -->
Le matériel doit le signaler.
Le noyau doit le ranger.
La file doit atteindre ton programme.

<!-- S80 -->
Ton programme doit tourner.
L'interface doit changer.
Quelqu'un doit dessiner la nouvelle image,
et l'écran doit te la montrer.

<!-- S81 -->
Chacune de ces étapes
est petite et rapide.

<!-- S82 -->
Retarde-en une seule
et tu ne vis pas
une fenêtre lente.

<!-- S83 -->
Tu vis un ordinateur mort.

<!-- S84 -->
Et le plus étrange dans tout ça,
c'est à quel point
ça arrive rarement.

<!-- S85 -->
Nous attendons d'une machine
qui fait des milliards d'opérations
par seconde
qu'elle réponde à un frémissement.

<!-- S86 -->
Et presque toujours, elle répond.

<!-- S87 -->
Alors la prochaine fois que tu cliques
et qu'il ne se passe rien,
laisse-lui un instant.

<!-- S88 -->
Il t'a entendu.

<!-- S89 -->
Il avait juste une file d'attente,
et tu étais dedans.
