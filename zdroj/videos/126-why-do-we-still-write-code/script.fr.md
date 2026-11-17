<!-- S01 -->
Voici une exigence complète
pour un logiciel de gestion.
Un utilisateur peut annuler une commande.

<!-- S02 -->
Six mots.
N'importe quel développeur approuverait.
N'importe quel client signerait.

<!-- S03 -->
Alors, un utilisateur peut-il annuler une commande
une fois la facture envoyée ?
Une fois la commande expédiée ?

<!-- S04 -->
Est-ce que l'annuler annule aussi
la réservation chez le fournisseur ?
Et si quelqu'un l'annule
et qu'un autre valide la même commande
dans la même seconde ?

<!-- S05 -->
La phrase ne répond à rien de tout ça.
Le code, lui, doit répondre à tout.
Et cette lacune entre la phrase
et le code, c'est en réalité pour ça
qu'on paie les programmeurs.
Du moins, c'était le cas avant.

<!-- S06 -->
Aujourd'hui, une idée séduisante circule.
N'écrire que les phrases.
Les ranger dans des documents,
les relire, les versionner.
Et laisser une IA écrire le code.

<!-- S07 -->
La spécification devient
le code source.
Et le code devient ce qu'est
l'assembleur aujourd'hui : ça tourne,
et personne ne le lit.

<!-- S08 -->
C'est une bonne idée.
Mais elle n'a rien de nouveau.

<!-- S09 -->
Depuis près de soixante-dix ans, on essaie
d'élever le niveau
auquel on dit aux ordinateurs quoi faire.
Les outils étaient différents,
et leurs objectifs aussi.
Mais chacun a fait passer un peu plus de travail
des humains aux machines.

<!-- S10 -->
En 1957, une équipe d'IBM
a publié un article sur FORTRAN.
Son titre le présentait
comme un système de codage automatique.

<!-- S11 -->
À l'époque, le terme était juste.
Tu écrivais des formules,
et les instructions machine,
la partie que les gens écrivaient à la main,
étaient désormais produites par la machine.

<!-- S12 -->
Aujourd'hui, FORTRAN, on appelle ça du code.

<!-- S13 -->
Dans les années 1980, les outils CASE
et les langages de quatrième génération
sont montés d'un cran.
Tu dessines les diagrammes, tu remplis les formulaires,
et une bonne partie de l'application
est générée pour toi.

<!-- S14 -->
En 2001, l'Object Management Group,
l'organisme derrière UML,
a annoncé Model Driven Architecture.

<!-- S15 -->
Le discours va te sembler familier.
Tu décris le système une seule fois,
sous forme de modèle, indépendant de toute technologie.
Ensuite, des outils génèrent l'implémentation
pour la plateforme dont tu as besoin.

<!-- S16 -->
Les mêmes règles métier.
Une technologie remplaçable.

<!-- S17 -->
Et en 2014, les analystes de Forrester
ont donné un nom aux plateformes
qui permettent de créer des applications métier
avec le moins possible
de code écrit à la main.
Ils ont appelé ça le low-code.

<!-- S18 -->
Alors, est-ce que ça a marché ?

<!-- S19 -->
En partie.
En 2014, des chercheurs de l'université de Lancaster
ont publié une enquête
auprès de 450 personnes
qui utilisaient réellement
le développement dirigé par les modèles.

<!-- S20 -->
Ça marchait,
et plus largement que beaucoup ne le pensaient.
Mais rarement pour un système entier.
Les gens l'utilisaient pour des parties clés,
et construisaient le reste autrement.

<!-- S21 -->
Les plus gros obstacles qu'ils ont relevés
étaient les personnes et les organisations,
pas les outils.
Mais il y a aussi une limite technique,
et les programmeurs ont une blague là-dessus.

<!-- S22 -->
Une spécification assez précise
pour qu'on puisse en générer tout le programme...
a déjà un nom.
Ça s'appelle du code.

<!-- S23 -->
Pour tout générer,
le modèle devait tout dire.
Chaque état, chaque exception,
chaque « et si deux personnes le font en même temps ? ».

<!-- S24 -->
À ce stade,
tu n'as pas échappé à la programmation.
Tu l'as juste déplacée dans un diagramme,
souvent plus difficile à lire,
à comparer et à passer en revue.

<!-- S25 -->
Dès la fin des années 1970,
Edsger Dijkstra a résumé l'autre moitié du problème
dans une courte note au titre cinglant.
De la sottise
de la programmation en langage naturel.

<!-- S26 -->
Pour lui, la notation formelle
n'est pas un fardeau qu'on subit.
Il y voyait un outil étonnamment efficace
pour écarter toutes sortes d'absurdités.

<!-- S27 -->
Le langage courant ne les écarte pas.
Il les cache.
Un utilisateur peut annuler une commande.

<!-- S28 -->
Alors, si rien de tout ça n'a remplacé le code,
pourquoi réessayer ?

<!-- S29 -->
Parce qu'une chose est vraiment différente.

<!-- S30 -->
Les anciens générateurs ne pouvaient pas combler une lacune
tout seuls.
Si le modèle ne disait pas ce qui arrive
à une commande expédiée,
quelqu'un devait ajouter cette règle explicitement.
Tant que ce n'était pas fait, la lacune restait là,
et on pouvait la trouver.

<!-- S31 -->
Une IA, elle, ne s'arrête pas.
Donne-lui l'exigence de six mots
et elle répondra à toutes les questions
qu'on a posées au début.

<!-- S32 -->
Elle décidera qu'une commande expédiée
peut être annulée. Ou pas.
Elle tranchera pour la facture,
et pour le fournisseur.
Elle produira du code qui tourne,
qui a l'air raisonnable,
et qui passe les tests qu'elle a écrits elle-même.

<!-- S33 -->
C'est exactement ce qui la rend utile.
Et exactement ce qui la rend dangereuse.
Parce qu'une supposition plausible
n'est pas une décision métier.

<!-- S34 -->
Avant, les lacunes étaient des erreurs.

<!-- S35 -->
Maintenant, ce sont des décisions
prises sans que personne ne s'en rende compte.

<!-- S36 -->
Alors, si la spécification doit vraiment
devenir le code source,
ça ne peut pas être quelques paragraphes informels.

<!-- S37 -->
Imagine le dépôt.
Un document décrit les commandes
et tous les états par lesquels elles peuvent passer.
Un autre dit qui peut les approuver
et qui peut les annuler.

<!-- S38 -->
Un troisième dit quand une facture est émise,
et quand il faut l'annuler par un avoir.
Un autre décrit le système comptable,
y compris ce qui se passe quand il est en panne.

<!-- S39 -->
Une partie est en prose ordinaire.
Mais partout où la prose serait ambiguë,
il y a quelque chose de plus strict :
une liste d'états et des transitions entre eux,
un schéma, une règle qu'une machine peut vérifier.

<!-- S40 -->
Et à côté, des tests d'acceptation
qui disent exactement ce qui doit se passer.

<!-- S41 -->
Tout ça vit dans Git.
Les modifications sont relues.
Chaque exigence peut être reliée
au test qui la vérifie.

<!-- S42 -->
Alors, à quoi ressemble une modification ?
Disons que le client décide
qu'une commande expédiée peut encore être annulée,
tant qu'elle n'a pas été livrée.
Et qu'il faut alors annuler la facture par un avoir.

<!-- S43 -->
Personne n'ouvre le backend.
Un développeur modifie une règle
dans le document sur les commandes.

<!-- S44 -->
Ensuite, le système va chercher
tout ce que cette règle touche.
Les états de la commande.
Les règles de facturation.
Les tests d'annulation.
La réservation chez le fournisseur.

<!-- S45 -->
Et là, il devrait s'arrêter et poser la question.
La spécification n'a jamais dit
ce qui arrive à une réservation chez le fournisseur
une fois la marchandise en route.
C'est une décision,
donc elle revient à un humain.

<!-- S46 -->
Ce n'est qu'ensuite que la nouvelle implémentation
est générée.
Et elle est vérifiée dans les deux sens.
Les tests de la nouvelle règle doivent passer.
Et tous les autres tests doivent toujours passer,
sans modification.

<!-- S47 -->
Parce qu'une modification de l'annulation
ne doit rien changer d'autre en douce.
Cela dit, des tests qui passent ne montrent
que ce que les tests vérifient.

<!-- S48 -->
Et comme les règles
ne sont pas liées à la technologie,
la même spécification pourrait produire
une application PHP aujourd'hui,
et tout autre chose demain.

<!-- S49 -->
Ce qui est précisément ce que
Model Driven Architecture promettait
il y a vingt-cinq ans.
La différence, c'est que cette fois,
le générateur pourrait être assez bon.

<!-- S50 -->
Reste la question la plus difficile.
Comment savoir si l'IA
a vraiment suivi la spécification ?

<!-- S51 -->
Un code qui marche dans les situations ordinaires
peut quand même échouer dans les cas inhabituels.
Et les cas inhabituels sont justement
ceux que personne ne pense à tester.

<!-- S52 -->
Amazon s'est heurté à ce problème
sur ses propres systèmes cloud.
En 2014, ses ingénieurs ont raconté
comment ils s'étaient mis à écrire
des descriptions précises et mathématiques
de la conception de leurs systèmes,
dans un langage appelé TLA+.

<!-- S53 -->
Pas du code. De la conception elle-même.
Un outil prenait ensuite un modèle du système,
limité à une taille fixe,
et essayait tous les ordres possibles
de pannes et de reprises.

<!-- S54 -->
Dans DynamoDB, le service de base de données d'Amazon,
il a trouvé un bug qui pouvait faire perdre des données.

<!-- S55 -->
Le chemin le plus court pour le déclencher
faisait 35 étapes,
exactement dans le bon ordre.
Il avait passé les revues de conception,
les revues de code et les tests.

<!-- S56 -->
Donc, la version honnête de l'idée,
ce n'est pas que l'IA écrit le code
et qu'on lui fait confiance.
C'est que l'IA écrit le code,
et que quelque chose d'indépendant le vérifie.

<!-- S57 -->
Maintenant, regarde ce qu'on a construit.

<!-- S58 -->
Des états précis.
Des règles formelles.
Des tests vérifiables.
Versionné, relu, conservé dans un dépôt.

<!-- S59 -->
Ça ne ressemble pas
à la fin de la programmation.
Ça ressemble à de la programmation,
dans un nouveau langage.

<!-- S60 -->
Et c'est ce qui s'est passé à chaque fois.
FORTRAN, c'était du codage automatique,
jusqu'à ce que ça devienne du code.
À chaque fois que la machine a pris en charge
le « comment », les humains sont passés au « quoi ».

<!-- S61 -->
Et le « quoi » a toujours été le plus difficile.
Pas taper, mais décider.
Ce qui arrive à une commande expédiée.
Qui a le droit de toucher à quelles données.
Ce que le système ne doit jamais faire.

<!-- S62 -->
Peut-être que le programmeur du futur
n'écrira pas des milliers de lignes de code.

<!-- S63 -->
Mais quelqu'un devra toujours comprendre
un problème assez bien pour dire
exactement ce qu'un ordinateur doit faire,
et vérifier qu'il l'a fait.

<!-- S64 -->
Et si la spécification
devient le code source,
la compétence la plus importante
ne sera peut-être plus de savoir
écrire un programme.

<!-- S65 -->
Ce sera peut-être de savoir
en décrire un.

<!-- S66 -->
Alors, voici la question
à laquelle j'aimerais connaître ta réponse.
Si tu écris une spécification
assez précise
pour qu'une machine puisse en tirer le programme...
est-ce que tu programmes encore ?
