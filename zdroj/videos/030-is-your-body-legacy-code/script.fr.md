<!-- S01 -->
Imagine un programme informatique
de trois milliards de caractères
d'instructions.

<!-- S02 -->
Et qu'à chaque fois
que tu lances un nouveau processus,
tu y copies le programme entier.

<!-- S02b -->
Deux fois.

<!-- S03 -->
Pas seulement les fonctions
dont ce processus a besoin.
Absolument tout.
Chaque module.
Chaque dépendance.
Chaque bout de vieux code hérité.

<!-- S04 -->
Et ensuite le processus en ignore
tout simplement 99 %.
Ce serait un travail
d'ingénierie catastrophique.

<!-- S05 -->
Et pourtant...

<!-- S06 -->
...c'est à peu près ce que
font tes cellules.

<!-- S07 -->
Presque chaque cellule de ton corps
qui possède un noyau
contient au fond la même
copie complète de ton génome.

<!-- S08 -->
Un neurone l'a.
Une cellule du foie l'a.
Une cellule de peau l'a.
Et pourtant elles se comportent
de façon complètement différente.

<!-- S09 -->
Le code est là.
La plus grande partie ne sert pas.

<!-- S10 -->
Un gène peut se voir,
très grossièrement,
comme une fonction ou un module.

<!-- S11 -->
Il porte une information
qui peut finalement donner
un certain
produit fonctionnel,
souvent une protéine.
On peut se le représenter comme ça.

<!-- S12 -->
Mais avoir la fonction dans le code
ne veut pas dire qu'elle tourne.
Il faut que quelque chose l'active.
Et c'est là que la biologie
devient intéressante.

<!-- S13 -->
Parce que dans un ordinateur
j'écris simplement ceci.
Ou en code machine.

<!-- S14 -->
Le processeur sait exactement quoi faire.
Il y a une instruction.
Il y a une adresse.
Il y a un pointeur d'instruction.

<!-- S15 -->
Mais une cellule n'a pas de processeur
qui exécuterait les instructions
de l'ADN une par une.

<!-- S16 -->
Alors...

<!-- S17 -->
...comment sait-elle quoi utiliser ?

<!-- S18 -->
C'est ici que la comparaison
avec l'ordinateur devient étrange.
Dans un ordinateur, on peut sauter
à une adresse mémoire précise.

<!-- S19 -->
On peut avoir des droits d'accès.
On peut avoir des processus.
On peut avoir des fichiers de config.
On peut avoir des événements
qui déclenchent des bouts de code.

<!-- S20 -->
La biologie a des choses
qui jouent des rôles étonnamment proches.

<!-- S21 -->
Les facteurs de transcription se fixent
sur certaines séquences d'ADN
et influencent le fait qu'un gène
soit transcrit ou non.

<!-- S22 -->
Les séquences régulatrices influencent
quand et où les gènes s'expriment.
La structure de la chromatine décide
à quel point telle région
de l'ADN est accessible.

<!-- S23 -->
Et les cellules reçoivent sans cesse
des signaux de leur environnement.

<!-- S24 -->
Donc au lieu d'un processeur,
d'un pointeur d'instruction,
d'une adresse et d'une exécution...

<!-- S25 -->
...tu as plutôt quelque chose comme ça.

<!-- S26 -->
Il n'y a pas un pointeur unique.
Il y a un immense réseau
d'interactions moléculaires.

<!-- S27 -->
L'ADN est là.
Mais ses différentes parties
sont plus ou moins accessibles
à la machinerie moléculaire
qui les lit.

<!-- S28 -->
Donc avoir le code,
ce n'est pas la même chose
qu'avoir accès au code.
Une cellule du foie n'a pas à effacer
les gènes liés aux neurones.
Il lui suffit de régler
s'ils servent ou non.

<!-- S29 -->
Revenons
à notre projet logiciel.
Disons que tu développes
une énorme application.

<!-- S30 -->
Tu crées un module appelé finger.
Et au lieu d'importer
les quelques fonctions utiles...

<!-- S31 -->
...tu y copies le dépôt
humain tout entier.

<!-- S32 -->
Le cerveau.
Le foie.
Le cœur.
Le système immunitaire.
L'appareil reproducteur.
Tout.

<!-- S33 -->
Et tu recommences...

<!-- S34 -->
...pour chaque cellule.

<!-- S35 -->
En tant que programmeur,
tu demanderais sans doute...
Qui a conçu ça ?

<!-- S36 -->
Et la réponse est...

<!-- S37 -->
Personne.

<!-- S38 -->
Enfin... Pas tout à fait personne.
L'évolution.

<!-- S39 -->
Et l'évolution a une philosophie
de développement très différente.

<!-- S40 -->
Imagine ouvrir un dépôt
appelé humain,
dont l'historique de commits
remonte à des milliards d'années.

<!-- S41 -->
Aucun architecte ne s'est assis
pour concevoir la version 1.0.
Il n'y a jamais eu de réécriture propre.
Il n'y a jamais eu d'humain version deux
à l'architecture repensée.

<!-- S42 -->
À la place...
Ajouter une fonctionnalité.
Rustiner un bug.
Dupliquer un module.
Réutiliser un vieux module.

<!-- S43 -->
Contourner une limite.
Ajouter encore un bricolage.
Garder la vieille API
parce que quelque chose en dépend.

<!-- S44 -->
Encore.
Et encore.
Et encore.
Pendant des milliards d'années.

<!-- S45 -->
L'évolution ne demande pas
quelle est l'architecture la plus propre.
Sa question est bien plus simple.
Est-ce que cet organisme
se reproduit avec succès ?

<!-- S46 -->
Si la réponse est oui,
le code survit.

<!-- S47 -->
Imagine hériter d'un projet
maintenu
par des millions de programmeurs,
pendant des milliards d'années,
sans la moindre possibilité
de tout réécrire.

<!-- S48 -->
Tu tombes sur un truc et tu demandes...
Pourquoi ça existe ?
Parce que quelque chose en dépendait.

<!-- S49 -->
Pourquoi cette API est si bizarre ?
Legacy.

<!-- S50 -->
Voilà l'évolution.
Le système hérité par excellence.
Elle ne refactorise pas.
Elle modifie ce qui existe déjà.

<!-- S51 -->
Et au bout de milliards d'années...

<!-- S52 -->
...ça donne nous.

<!-- S53 -->
Le développement logiciel moderne
repose sur une idée assez sensée.
Tu fais une modification.
Puis tu la testes.

<!-- S54 -->
Commit.
Build.
Tests unitaires.
Tests d'intégration.
Déploiement.

<!-- S55 -->
La biologie a quelque chose
qui ressemble vaguement à ça.
Une mutation survient.

<!-- S56 -->
Et ensuite...
Soit l'organisme survit
et se reproduit.
Soit non.

<!-- S57 -->
Il n'y a pas d'environnement de staging.
Il n'y a pas de rollback.

<!-- S58 -->
Et de temps en temps
il se passe bien pire.
Une mutation peut rendre une cellule
meilleure pour survivre et se multiplier
à l'intérieur de l'organisme.
Cela peut contribuer au cancer.

<!-- S59 -->
La biologie a donc une version
terrifiante de l'intégration continue.
Les tests se font
sur le système en production.

<!-- S60 -->
Mais c'est justement ici
que la comparaison
avec le logiciel devient captivante.
Quand on regarde le corps humain,
on est tenté d'imaginer
quelque chose comme ça.

<!-- S61 -->
Sauf que ce n'est pas
comme ça que ça marche.
Il n'y a pas de serveur central
qui envoie des ordres à chaque cellule.

<!-- S62 -->
Tes cellules surveillent sans arrêt
leur environnement immédiat.
Elles reçoivent des signaux chimiques.
Elles sont en contact avec les voisines.
Elles réagissent aux hormones.

<!-- S63 -->
Une cellule ne reçoit jamais
de message disant...

<!-- S64 -->
...cellule numéro sept millions
trois cent quatre-vingt-douze mille
cent quatre-vingt-quatre.
Exprime le gène X maintenant, merci.

<!-- S65 -->
Si tu programmes,
un autre concept
devient soudain utile.
Les systèmes distribués.

<!-- S66 -->
Tes cellules sont en réalité
un nombre colossal
d'agents individuels.
Chacun a son propre état.
Ses propres capteurs.
Ses propres entrées.
Ses propres réponses.

<!-- S67 -->
Il n'y a pas une boucle géante
qui dit à chaque cellule quoi faire.
On est plus près d'un
système multi-agent.
Ou d'un essaim.
Ou d'un automate cellulaire.

<!-- S68 -->
Des règles locales simples...

<!-- S69 -->
...d'où sort un comportement
d'ensemble incroyablement complexe.

<!-- S70 -->
Et encore une chose qui serait
inacceptable dans un logiciel normal.
Ton corps tourne
sans interruption depuis des décennies.

<!-- S71 -->
Aucun redémarrage.
Aucune fenêtre de maintenance.

<!-- S72 -->
Et pourtant le système
change en permanence.
Des cellules meurent.
D'autres naissent.
Des protéines se font et se défont.

<!-- S73 -->
L'ADN est copié.
Les dégâts sont réparés.
Les pièces sont remplacées.

<!-- S74 -->
Le système ne s'éteint pas
pour faire la maintenance.
Il fait la maintenance
en pleine activité.

<!-- S75 -->
Presque comme si tu avais un serveur
qui remplace ses propres pièces
au moment précis
où il traite des requêtes...

<!-- S76 -->
...sans jamais tomber.

<!-- S77 -->
Les cellules ont leur machinerie.
Elles communiquent.
Elles répondent.
Elles se régulent entre elles.
Elles forment des tissus.
Les tissus forment des organes.
Les organes forment des systèmes.
Et les systèmes forment un organisme.

<!-- S78 -->
Et il n'y a pas une seule pièce
qui garde toute l'architecture
dans sa tête.

<!-- S79 -->
Et d'une manière ou d'une autre...

<!-- S80 -->
...ça marche.

<!-- S81 -->
Pas parfaitement.
Loin d'être parfaitement.

<!-- S82 -->
Mais assez bien pour faire des yeux.
Des cœurs.
Des systèmes immunitaires.
Des cerveaux.

<!-- S83 -->
Et des organismes capables
d'écrire des logiciels pour se plaindre
de la mauvaise conception
du système.

<!-- S84 -->
On appelle l'ADN du code.
Et la comparaison est utile.
Les gènes rappellent des fonctions.
Les mutations rappellent
des changements dans le code source.

<!-- S85 -->
Mais il y a
une différence importante.
L'ADN n'est pas vraiment
un plan complet d'un être humain.

<!-- S86 -->
Nulle part il n'y a une ligne...
Créer un bras.
Créer un œil.
Créer un cœur.

<!-- S87 -->
L'ADN participe plutôt
à un immense jeu d'influences
où entrent des molécules, des cellules,
des forces physiques, des gradients,
le tempo et l'environnement.

<!-- S87b -->
L'organisme émerge de tout cela.

<!-- S88 -->
On comprend donc mieux l'ADN
comme un jeu d'instructions et de règles
intégré à un système physique...

<!-- S89 -->
...que comme le listing complet
du code source d'un humain.
Et c'est en fait bien plus étrange.

<!-- S90 -->
On sait séquencer un génome,
identifier des gènes
et mesurer des protéines.

<!-- S91 -->
Mais on ne sait toujours pas prendre
l'ADN d'une cellule humaine ordinaire,
le mettre dans un ordinateur,
appuyer sur exécuter...

<!-- S92 -->
...et regarder cet humain se développer.

<!-- S93 -->
On a le génome.
Mais le génome
n'est pas toute la machine.

<!-- S94 -->
Et c'est là qu'on arrive.
On est parti d'une idée familière.
L'ADN est comme du code.

<!-- S95 -->
Et la comparaison se révèle
étonnamment utile.
Mais plus on regarde en profondeur,
plus le système devient étrange.

<!-- S96 -->
Il n'y a pas de processeur.
Il n'y a pas de système d'exploitation.
Il n'y a pas de serveur central.

<!-- S97 -->
Il n'y a pas de programmeur.
Il n'y a pas de GitHub.
Il n'y a pas de revue de code.
Il n'y a pas de staging.
Il n'y a pas de rollback.
Il n'y a même pas vraiment
d'architecture propre.

<!-- S98 -->
Il y a des milliers de milliards d'agents,
chacun suivant des règles locales,
communiquant avec ses voisins,

<!-- S99 -->
utilisant un dépôt immense, très ancien
et modifié sans arrêt...
Et il en sort quand même
un organisme qui fonctionne.

<!-- S100 -->
Donc si la biologie est un logiciel...

<!-- S101 -->
...c'est sans doute le système hérité
le plus vieux, le plus bordélique
et le plus inutilement complexe qui soit.

<!-- S102 -->
Un système avec des milliards
d'années de commits.
Presque aucune refactorisation.
Aucun administrateur central.
Et absolument aucun redémarrage.

<!-- S103 -->
Et d'une manière ou d'une autre...

<!-- S104 -->
...il tourne en production
depuis des milliards d'années.
