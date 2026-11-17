<!-- S01 -->
Quatre voitures arrivent à un carrefour
exactement au même moment.
Pas de feux. Pas de panneaux.
Juste la règle de nombreux pays :
céder le passage à la voiture de droite.

<!-- S02 -->
Chaque conducteur regarde à droite
et voit une voiture qu'il doit laisser passer.
Alors chaque conducteur attend.

<!-- S03 -->
Personne n'enfreint la règle.
Tout le monde la respecte parfaitement.
Et personne ne bougera jamais.

<!-- S04 -->
Les informaticiens appellent ça un interblocage.
Et ça n'arrive pas que sur les routes.
Ça arrive dans les bases de données,
les systèmes d'exploitation et les logiciels courants.

<!-- S05 -->
Les ordinateurs savent souvent bien repérer
un interblocage une fois qu'il s'est produit.
Mais un programme pourrait-il lire un autre programme
et te dire, avec certitude,
s'il finira un jour par se bloquer ?

<!-- S06 -->
Pour beaucoup de programmes, oui.
Mais une méthode qui marche
pour tous les programmes possibles
ne peut pas exister.
Et pas parce que les ordinateurs
ne sont pas encore assez rapides.
Aucun ordinateur plus rapide n'y changera jamais rien.

<!-- S07 -->
Voici comment un programme se bloque.
Imagine une boutique en ligne,
avec deux tâches qui tournent en même temps.

<!-- S08 -->
Avant qu'une tâche modifie quoi que ce soit,
elle pose un verrou dessus,
pour que personne d'autre ne puisse y toucher.
Comme prendre la seule clé d'une pièce.

<!-- S09 -->
La première tâche verrouille le compte d'un client,
puis tente de verrouiller sa commande.
La deuxième verrouille la commande,
puis tente de verrouiller le compte.

<!-- S10 -->
L'une tient le compte
et attend la commande.
L'autre tient la commande
et attend le compte.
Aucune ne lâchera ce qu'elle tient.

<!-- S11 -->
Et le plus étrange,
c'est que ce code peut tourner un million de fois
sans le moindre problème.
C'est seulement quand les deux tâches se chevauchent
exactement dans le mauvais ordre
que tout s'arrête.

<!-- S12 -->
Le bug était là depuis le début.
Il a juste fallu le mauvais moment pour le révéler.

<!-- S12b -->
Au fait, si tu aimes ce genre de
vidéos, pense à t'abonner.

Ça aide vraiment la chaîne.

<!-- S13 -->
Les bases de données y sont confrontées sans arrêt,
alors elles surveillent.
Elles dessinent une carte de qui attend qui.

<!-- S14 -->
La première attend la deuxième.
La deuxième attend la première.
Quand les flèches se referment en boucle,
c'est un interblocage.
Rien à deviner. La boucle est juste là.

<!-- S15 -->
Alors la base de données fait quelque chose de brutal.
Elle choisit l'une des tâches
et jette son travail.

<!-- S16 -->
SQL Server de Microsoft annonce même au perdant
qu'il a été choisi
comme victime de l'interblocage,
et qu'il doit réessayer.

<!-- S17 -->
L'autre tâche continue,
et la victime peut tout simplement réessayer.

<!-- S18 -->
Remarque ce que ça règle, et ce que ça ne règle pas.
Le blocage est levé.
Mais le code qui l'a provoqué est toujours là,
à attendre le prochain mauvais moment.

<!-- S19 -->
Repérer un interblocage
qui s'est déjà produit,
c'est donc la partie facile.
La question difficile est tout autre.

<!-- S20 -->
Pas : ce programme est-il bloqué en ce moment ?
Mais : donne-lui cette entrée.
Pourrait-il un jour se bloquer ?

<!-- S21 -->
La première, c'est une photo du présent.
Il suffit de la regarder.
La seconde, c'est une prédiction
sur tous les futurs possibles.

<!-- S22 -->
Et les programmes rendent ça très difficile.
Ils prennent des décisions. Ils répètent des choses.
Ils peuvent lancer des calculs qui durent
une seconde, ou mille ans.

<!-- S23 -->
Un programme peut se bloquer tout de suite,
après un million d'étapes,
pour une seule entrée rare,
ou jamais.

<!-- S24 -->
Tu pourrais simplement le lancer et observer.
Mais s'il ne s'est pas bloqué au bout d'une heure,
qu'est-ce que ça t'apprend ?

<!-- S25 -->
Rien.
Il pourrait se bloquer à la seconde suivante,
ou jamais.

<!-- S26 -->
En 1936, un jeune mathématicien
nommé Alan Turing a montré
qu'à certaines questions sur les programmes,
aucun programme ne peut répondre.
La plus célèbre semble encore plus simple.

<!-- S27 -->
Prends n'importe quel programme, avec son entrée.
Finira-t-il par s'arrêter ?
Ou tournera-t-il indéfiniment ?

<!-- S28 -->
On l'appelle aujourd'hui le problème de l'arrêt.
Et aucun programme ne peut le résoudre
correctement dans tous les cas.

<!-- S29 -->
L'idée de la preuve
est étonnamment courte.
Suppose que quelqu'un te donne
un vérificateur d'arrêt parfait.

<!-- S30 -->
Maintenant, tu écris un petit programme contrariant.
Il interroge le vérificateur sur lui-même,
puis fait l'inverse.

<!-- S31 -->
Si le vérificateur dit qu'il va s'arrêter,
il boucle indéfiniment.
Si le vérificateur dit qu'il va tourner indéfiniment,
il s'arrête aussitôt.

<!-- S32 -->
Quoi que le vérificateur dise de lui,
le vérificateur se trompe.
Donc un vérificateur parfait ne peut pas exister.

<!-- S33 -->
Alors, quel rapport avec les interblocages ?
Un rapport direct.

<!-- S34 -->
Imagine que quelqu'un prétende avoir construit
un prédicteur d'interblocages parfait.
Tu lui donnes n'importe quel programme avec son entrée,
et il te dit toujours, sans se tromper,
si ce programme se bloquera un jour.

<!-- S35 -->
Utilisons-le
pour résoudre le problème de l'arrêt.

<!-- S36 -->
Prends le programme que tu veux,
et place-le à l'intérieur d'un nouveau programme.

<!-- S37 -->
D'abord, le nouveau programme
exécute simplement l'ancien,
pas à pas, sur un seul thread.
Pas de verrous. Rien de partagé.
Rien qui puisse jamais se bloquer.

<!-- S38 -->
Ensuite, si l'ancien programme finit un jour,
le nouveau lance deux tâches.
Chacune prend un verrou,
attend que l'autre ait pris le sien,
puis tente de prendre celui de l'autre.
Un interblocage, exprès, à chaque fois.

<!-- S39 -->
Si l'ancien programme ne finit jamais,
le nouveau n'arrive jamais jusque-là.
Pas d'interblocage. Jamais.

<!-- S40 -->
Donc le nouveau programme se bloque
si, et seulement si, l'ancien s'arrête.

<!-- S41 -->
Maintenant, interroge le prédicteur
sur le nouveau programme.
« Oui, il va se bloquer »
signifie que l'ancien programme s'arrête.
« Non » signifie qu'il tourne indéfiniment.

<!-- S42 -->
On vient de résoudre le problème de l'arrêt.
Et c'est exactement ce qui est impossible.

<!-- S43 -->
Donc le prédicteur d'interblocages parfait
ne peut pas exister non plus.

<!-- S44 -->
Le problème, ce ne sont pas les verrous,
ni les bases de données, ni les mauvais programmeurs.
Un programme peut cacher n'importe quel calcul
juste avant un interblocage.
Pour prédire l'interblocage,
il faudrait prédire si ce calcul se termine.

<!-- S45 -->
Mais attends.
Un vrai ordinateur n'est pas infini.
Sa mémoire a un nombre limité d'états.
Alors pourquoi ne pas tous les vérifier ?

<!-- S46 -->
Pour une machine avec une quantité fixe
de mémoire, en principe, oui.
En pratique, essaie de les compter.

<!-- S47 -->
La mémoire d'un ordinateur portable
de huit gigaoctets
peut être agencée de tant de façons
que rien que pour écrire ce nombre,
il faut environ vingt milliards de chiffres.

<!-- S48 -->
Le nombre d'atomes
dans l'univers observable
en a environ quatre-vingts.

<!-- S49 -->
Donc, sur une vraie machine, tout vérifier
est possible en théorie,
et sans espoir en pratique.

<!-- S50 -->
Mais c'est un autre mur.
La limite de Turing ne vient pas d'un excès d'états.
Elle s'applique aux programmes
qui peuvent toujours demander plus de mémoire.
Pour eux, aucun prédicteur parfait ne peut exister,
aussi gros que soit l'ordinateur.

<!-- S51 -->
Alors, les interblocages, c'est sans espoir ?
Non.
Ça veut juste dire qu'il n'y a pas de vérificateur parfait.
Donc les programmeurs écrivent des programmes
plus faciles à vérifier.

<!-- S52 -->
L'astuce la plus simple : imposer un ordre.
Chaque tâche doit verrouiller le compte
avant la commande.
Jamais l'inverse.

<!-- S53 -->
Si chaque tâche respecte vraiment cet ordre,
la boucle ne peut pas se former,
et ce type d'interblocage ne peut pas se produire.

<!-- S54 -->
D'autres systèmes abandonnent après un délai,
prennent tous leurs verrous d'un coup,
ou laissent la base de données choisir une victime
et réessaient, tout simplement.

<!-- S55 -->
Et pour de petits systèmes décrits avec soin,
des outils peuvent vérifier chaque état possible.
Des ingénieurs d'Amazon en ont utilisé un
pour trouver un bug qui demandait trente-cinq étapes,
exactement dans le bon ordre, pour apparaître.

<!-- S56 -->
Ces outils fonctionnent
parce qu'on a réduit la taille du problème.
Ils vérifient un modèle du système,
pas tous les programmes qui pourraient exister.

<!-- S57 -->
Pour du vrai code, en revanche,
un vérificateur qui accepte n'importe quel programme
doit renoncer à quelque chose.
Il peut signaler des interblocages
qui ne peuvent pas se produire,
en rater certains qui le peuvent,
ou parfois ne donner aucune réponse.

<!-- S58 -->
Un vérificateur qui ne crie jamais au loup,
ne rate jamais aucun interblocage,
et donne toujours une réponse,
pour tous les programmes,
c'est exactement ce que Turing a exclu.

<!-- S59 -->
Retour au carrefour :
les quatre conducteurs ne restent pas là éternellement.

<!-- S60 -->
Quelqu'un fait signe.
Un conducteur renonce à sa priorité,
et tout se débloque en quelques secondes.

<!-- S61 -->
C'est aussi ce que fait la base de données.
Elle ne prédit pas le blocage.
Elle le remarque,
et oblige quelqu'un à céder le passage.

<!-- S62 -->
Certains problèmes demandent un ordinateur plus rapide.
D'autres, une meilleure idée.

<!-- S63 -->
Et certains, comme celui-ci,
n'ont aucune solution parfaite.
Seulement de bonnes règles,
et quelqu'un prêt à faire signe.
