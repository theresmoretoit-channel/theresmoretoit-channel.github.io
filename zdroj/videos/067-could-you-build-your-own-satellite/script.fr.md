<!-- S01 -->
Imagine que tu as une idée folle.
Tu veux construire ton propre satellite.
Pas un satellite de communication
à un milliard de dollars.
Quelque chose de petit.

<!-- S02 -->
Une boîte à peu près de la taille
d'un pain de mie.
Dedans : un ordinateur, des panneaux solaires,
une radio, quelques capteurs.
Peut-être même une caméra.

<!-- S03 -->
Tu le construis dans ton garage.
Et puis, d'une manière ou d'une autre...
tu le mets en orbite.
Ça semble impossible.
Mais ça ne l'est pas.

<!-- S04 -->
Des gens font
presque exactement ça depuis des années.
Ça s'appelle des CubeSats.

<!-- S05 -->
Et le plus surprenant,
c'est que le plus dur
n'est pas de construire le satellite.
C'est tout le reste.

<!-- S06 -->
L'unité de base s'appelle 1U —
un cube d'environ dix centimètres.
En empilant les unités,
tu obtiens des formats 2U, 3U, 6U
et même plus grands.

<!-- S07 -->
L'idée est simple.
Au lieu de concevoir un nouvel engin spatial
en partant de zéro,
tu réutilises des tailles standardisées
et des interfaces standardisées.
Et soudain, l'espace s'ouvre
aux universités, aux start-ups,
et peut-être même à toi.

<!-- S07b -->
Au fait, si tu aimes les vidéos
comme celle-ci, pense à t'abonner.

Ça aide vraiment la chaîne.

<!-- S08 -->
Alors que contiendrait vraiment
notre petit satellite ?
D'abord, il lui faut un ordinateur.
Quelque chose doit exécuter le logiciel,
contrôler le matériel,
et décider quoi faire.

<!-- S09 -->
Ensuite, l'alimentation.
Les panneaux solaires produisent de l'électricité.
Les batteries la stockent
pour quand le satellite
passe dans l'ombre de la Terre.

<!-- S10 -->
Ensuite, la communication.
Une radio. Une antenne.
Et, sur Terre,
une station au sol à l'écoute.

<!-- S11 -->
Ensuite, les capteurs.
Température. Tension. Courant.
Accélération. Champ magnétique.
Et un moyen de savoir
dans quelle direction pointe le satellite.
Parce qu'en orbite,
dire "en haut" est étonnamment difficile.

<!-- S12 -->
Mais avant d'en construire un,
il y a une question gênante.
Combien coûte cette petite boîte ?
La réponse est...
plus que ce qu'on croirait.

<!-- S13 -->
Un simple CubeSat 1U
peut facilement coûter
des dizaines de milliers de dollars —
rien qu'en matériel de vol.
L'alimentation. Les panneaux solaires.
Les batteries. L'ordinateur. La radio.
Le contrôle d'attitude. La structure.
Et la charge utile.

<!-- S14 -->
Puis viennent les choses
qui ne sont pas sur la liste des pièces.
Les tests. L'intégration.
La documentation.
L'exploitation de la station au sol.
Les licences.
Et enfin...
le lancement.

<!-- S15 -->
Un vol partagé pour un petit CubeSat
peut coûter des dizaines de milliers.
Les missions et CubeSats plus gros
atteignent des centaines de milliers.
Et ça, c'est juste
pour l'envoyer dans l'espace.

<!-- S16 -->
Et maintenant,
un problème encore plus absurde.
Tu te souviens de toutes ces pièces ?
Comment diable tout ça
tient-il dans une seule petite boîte ?

<!-- S17 -->
Dans l'espace, il n'y a pas de place
pour un tas d'électronique en vrac.
Chaque centimètre compte.
Chaque gramme compte.
Chaque watt compte.
Le satellite est un puzzle en trois dimensions
qui doit survivre au lancement d'une fusée.

<!-- S18 -->
Alors, où trouves-tu
toutes ces pièces ?
Tu n'as pas à concevoir
tout toi-même.
Il y a toute une industrie
qui vend des composants pour petits satellites :
ordinateurs, systèmes d'alimentation,
radios, antennes et panneaux solaires.
Il existe même des places de marché
dédiées spécialement aux pièces de CubeSats.

<!-- S18b -->
Et les pièces sont standardisées, elles aussi.
Beaucoup partagent un même format de carte
et s'empilent simplement,
si bien que des pièces de fabricants différents
s'assemblent en une seule unité.
Des entreprises comme EnduroSat
et GomSpace en vendent,
et un seul sous-système peut coûter
de quelques milliers
à des dizaines de milliers de dollars.

<!-- S19 -->
Et ce ne sont pas
des processeurs exotiques.
Un ordinateur de CubeSat actuel
utilise un ARM Cortex-M7,
avec des interfaces familières —
SPI, I²C, UART et CAN.

<!-- S19b -->
Et ce n'est pas une puce spatiale sur mesure.
C'est une vraie carte du commerce
que tu pourrais tenir dans ta main.

<!-- S20 -->
Un engin spatial a besoin de quelque chose
de plus important que la vitesse brute :
un comportement prévisible,
une faible consommation et la fiabilité.
Les missions plus exigeantes
peuvent utiliser des processeurs ARM Cortex-A —
et même Linux.

<!-- S20b -->
Mais il n'est pas rapide.
Un ordinateur de CubeSat typique
tourne à quelques centaines de mégahertz.
Ton ordinateur portable tourne à
quatre ou cinq gigahertz,
avec bien plus de cœurs.
Il échange la vitesse brute
contre une consommation quasi nulle.

<!-- S21 -->
Et si tu es programmeur,
c'est là que ça devient intéressant.
Tu n'écris pas
un mystérieux "langage spatial".
Tu écris du logiciel embarqué.
Souvent en C ou C++.

<!-- S22 -->
Il peut tourner directement
sur le matériel,
ou sur un système d'exploitation temps réel
comme FreeRTOS, Zephyr ou RTEMS.
Il existe même des frameworks ouverts
conçus pour les engins spatiaux.
F Prime de la NASA, par exemple,
est un framework de logiciel de vol
pour les systèmes embarqués et spatiaux.

<!-- S23 -->
Ton code pourrait donc ressembler
à quelque chose comme ça.

<!-- S24 -->
Mais il y a une énorme différence
avec un ordinateur normal.
Tu ne peux pas t'y connecter en SSH.
Tu ne peux pas brancher de débogueur.
Et si ton logiciel plante...
ton ordinateur est
à quelques centaines de kilomètres d'altitude.

<!-- S25 -->
Il lui faut donc des watchdogs,
des modes de survie, la détection de pannes
et un rétablissement automatique du fonctionnement.
Il doit résoudre certains problèmes
sans toi pour l'aider.

<!-- S25b -->
Et une des grandes raisons de tout ça,
ce sont les rayonnements.
Dans l'espace, les rayons cosmiques
peuvent inverser un bit en mémoire,
ou même griller une puce.
Il n'y a pas de blindage lourd —
ça pèserait bien trop.
À la place, l'ordinateur se surveille,
corrige les erreurs,
et redémarre quand quelque chose ne va pas.

<!-- S26 -->
Mais si tu veux vraiment
le lancer...
ça devient sérieux.
Une pièce qui marche sur ton bureau
n'est pas automatiquement prête
pour une fusée.
Elle doit survivre aux vibrations,
au vide, aux températures extrêmes
et aux rayonnements.

<!-- S27 -->
Revenons à ce problème :
savoir dans quelle direction
pointe le satellite.
Imagine-le en train de culbuter
à travers l'espace.
Pas de sol. Pas de plafond.
Le GPS peut te dire
où tu es...
mais pas dans quelle direction
tu es tourné.

<!-- S28 -->
Les satellites combinent donc
des gyroscopes, des magnétomètres
et des capteurs solaires
pour déterminer leur attitude.
Et ensuite, ils doivent la modifier.
Une astuce courante,
c'est un magnétocoupleur.

<!-- S29 -->
Il s'appuie
sur le champ magnétique terrestre
et crée un tout petit couple.
Ce n'est pas un moteur-fusée.
Il ne déplace pas le satellite.
Il ne fait que le tourner.
Et ça suffit
pour orienter le satellite
exactement où tu veux.

<!-- S30 -->
Mais rien de tout ça
n'est la raison
pour laquelle on a construit le satellite.
Il nous faut une mission.
C'est la charge utile.
Mesurer les rayonnements.
Photographier la Terre.
Étudier l'atmosphère.
Tester un nouveau capteur.
Ou simplement prouver
qu'une nouvelle technologie fonctionne.

<!-- S31 -->
Le satellite lui-même
est là surtout
pour maintenir la charge utile en vie.
L'alimenter. L'orienter.
La garder au chaud.
Stocker ses données.
Et les renvoyer sur Terre.

<!-- S32 -->
Quand ton ordinateur de bureau se fige,
tu le redémarres.
Quand ton satellite se fige...
tu as un objet très coûteux
qui orbite silencieusement autour de la Terre.

<!-- S33 -->
Disons donc qu'on l'a construit.
Tout marche...
L'ordinateur démarre...
La radio communique.
Les panneaux produisent de l'énergie.
La charge utile tourne...
On peut le lancer ?
...Pas encore.

<!-- S34 -->
Un satellite doit prouver
qu'il peut survivre au lancement.
Ça veut dire des tests.
Beaucoup de tests.

<!-- S35 -->
D'abord, boulonne-le
à un pot vibrant géant.
Puis secoue-le, fort...
C'est le test en vibrations.
Un lancement de fusée, ça secoue.
Il doit survivre
au bruit, aux vibrations et aux chocs
sans que rien
ne se desserre ou ne casse.
Chaque vis compte.
Chaque connecteur compte.
Chaque bout de câble compte.

<!-- S36 -->
Puis vient le vide.
Sur Terre, l'air évacue la chaleur.
Dans l'espace, il n'y a pas d'air.
Un côté peut devenir brûlant,
l'autre glacial,
et l'électronique
doit quand même rester
dans ses limites.
Le satellite a donc besoin
de tresses thermiques, de revêtements,
d'isolation
et de matériaux soigneusement choisis.
Les satellites n'ont pas
de climatisation.
Ils ont la physique.

<!-- S37 -->
Et avec la batterie,
ça devient intéressant.
Charge-la avec la lumière du soleil.
Puis le satellite
passe dans l'ombre de la Terre,
et les panneaux ne produisent presque rien.
La batterie le maintient en vie.
Puis retour au soleil.
Charge. Décharge.
Charge. Décharge.
Encore et encore.
Pendant des années.
Une seule erreur d'alimentation
pourrait discrètement mettre fin à la mission.

<!-- S38 -->
Et maintenant, comment lui parler ?
Il te faut une radio.
Une antenne.
Et une fréquence
que tu as le droit d'utiliser légalement.
Et une station au sol.
Le satellite
n'a pas d'internet.
Il passe simplement au-dessus de toi
et émet.

<!-- S39 -->
Ta station au sol
capte le signal.
L'ordinateur le décode.
Et soudain, tu as des données
de ton propre engin spatial.
Imagine ouvrir un terminal
et voir ça.

Sauf que la machine
qui affiche ces chiffres...
est à des centaines de kilomètres
au-dessus de ta tête.

<!-- S40 -->
Alors, comment
l'amener vraiment là-haut ?
Tu pourrais construire une fusée...
S'il te plaît, non...
Tu n'en as pas besoin.
Les CubeSats volent
comme charges utiles secondaires.

<!-- S41 -->
Une fusée part déjà là-haut.
Elle a de la place en rab.
Ton satellite fait le voyage
dans un déployeur standard.
Pas besoin de fusée personnelle.

<!-- S42 -->
Et maintenant, il est posé
au sommet d'une fusée.
Tu ne peux pas le toucher.
Tu ne peux pas ouvrir la boîte.
Tu ne peux pas brancher de câble.
La fusée décolle.
Environ neuf minutes plus tard,
tu es en orbite.

<!-- S43 -->
Le déployeur
libère ton satellite.
Il jaillit
et commence à culbuter.

<!-- S43b -->
Mais comment sait-il qu'il est sorti ?
...
Des interrupteurs à ressort, enfoncés
pendant qu'il était dans le déployeur,
se libèrent à l'instant de l'éjection,
et l'ordinateur démarre.
Ensuite, selon les règles,
il reste silencieux pendant environ une demi-heure.
Alors seulement, il allume sa radio,
déploie ses antennes,
et appelle enfin la maison.
Et quelque part sur Terre...
ta station au sol l'entend.

<!-- S44 -->
Tu as construit une machine.
Et maintenant cette machine
orbite autour de la planète.

<!-- S44b -->
Sauf qu'on n'a pas fini.
Un satellite mort ne peut pas
rester là-haut pour toujours.
Laissé en orbite pendant des siècles,
il devient un débris spatial.

<!-- S45 -->
Ça veut dire que les missions modernes
doivent de plus en plus prévoir
la fin
de la vie de l'engin spatial.
Idéalement, l'air raréfié de la haute atmosphère
le freine et le fait lentement redescendre.
Son orbite se dégrade.
Il rentre dans l'atmosphère.
Et il se consume.
La fin de la mission...
fait partie de la mission.

<!-- S46 -->
Alors... pourrais-tu construire
ton propre satellite ?
Techniquement, oui.
Tu n'as pas besoin d'être la NASA.
Tu n'as pas besoin
de posséder une fusée.
Tu n'as même pas forcément besoin
d'une énorme entreprise.

<!-- S47 -->
Le satellite doit
survivre au lancement.
Survivre à l'espace.
Communiquer légalement.
Fonctionner tout seul.
Et, à la fin,
dégager l'orbite.
Tout ça
doit être prouvé
avant que quiconque
ne le pose sur une fusée.

<!-- S48 -->
Les CubeSats n'ont pas rendu l'espace facile.
Ils l'ont rendu standardisé.
Au lieu de tout construire
en partant de zéro,
tu peux construire quelque chose
qui respecte un standard existant.
Et ça change bien plus de choses qu'on ne le croit.

<!-- S49 -->
Alors quelque part, en ce moment même,
il y a de minuscules machines
qui orbitent autour de la Terre.
Construites par des universités,
des équipes de recherche,
des entreprises et des étudiants.

<!-- S50 -->
Certaines emportent des caméras.
Certaines mesurent les rayonnements.
Certaines testent
une technologie toute neuve.
Et certaines ne sont que des expériences
qui posent une seule question :
"peut-on faire fonctionner ce truc
dans l'espace ?"

<!-- S51 -->
Et c'est ce qui rend
la construction de ton propre satellite
si fascinante.
Parce que la distance
entre toi et l'espace
n'est plus une fusée.
Ça pourrait être...
une boîte de dix centimètres.
Et une très, très
longue checklist.
