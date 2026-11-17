<!-- S01 -->
En septembre 2026, un seul lot
de mises à jour Windows a cassé
quatre choses d'un coup.

<!-- S02 -->
Le son ne marchait plus.
Remote Desktop ne marchait plus.
Les dossiers partagés des machines
virtuelles ne marchaient plus.

<!-- S03 -->
Et certains postes ne faisaient plus
confiance au réseau de l'entreprise
auquel ils appartenaient,
plus personne ne pouvait se connecter.

<!-- S04 -->
Un seul lot.
Un seul mardi.

<!-- S05 -->
Et si tu te dis
que ce n'est qu'une énième
mauvaise mise à jour...

<!-- S06 -->
ce n'en est pas une.

<!-- S07 -->
Parce que ça arrive
encore, et encore, et encore.

<!-- S08 -->
Mais que fait leur QA, au juste ?

<!-- S09 -->
Comment une entreprise pareille
publie-t-elle une mise à jour système
sans voir une chose aussi évidente ?

<!-- S10 -->
Commençons par la plus petite.

<!-- S11 -->
Microsoft a publié une mise à jour
qui changeait deux ou trois choses
dans la barre des tâches.
Et peu après, l'entreprise a reconnu
un problème dans les réglages
du curseur de la souris.

<!-- S12 -->
Chez certains, un curseur personnalisé
revenait à une grosse flèche blanche.
Le genre de flèche qui te fait vérifier
si tu n'as pas démarré par erreur
un ordinateur de 1998.

<!-- S13 -->
Ton curseur soigneusement choisi ?
Disparu.
Et le remettre
ne marchait pas non plus.

<!-- S14 -->
Là, tu te dis peut-être :
tout logiciel a des bugs.
Exactement.

<!-- S15 -->
Mais il y a une différence entre :
« Nous avons trouvé un défaut rare
dans une configuration matérielle
inhabituelle. »

<!-- S16 -->
Et :
« Après notre mise à jour,
ta souris ne ressemble plus à
la souris que tu as choisie. »

<!-- S17 -->
Parce que quelqu'un doit l'installer.
Quelqu'un doit se connecter.
Quelqu'un doit bouger la souris.
Et visiblement, ça n'a pas suffi.

<!-- S18 -->
Ensuite, il y a le son.
Tu installes une mise à jour.
Tu redémarres.
Plus de son.

<!-- S19 -->
Certains appareils audio USB
s'arrêtent, et Windows annonce
que l'appareil ne peut pas démarrer.

<!-- S20 -->
Et le son n'est pas vraiment
une fonction exotique.
On se dirait qu'un des tests de base
d'un système d'exploitation serait :

<!-- S21 -->
l'ordinateur émet-il encore un son ?

<!-- S22 -->
Visiblement, c'est plus compliqué
qu'il n'y paraît.
Littéralement.

<!-- S23 -->
À la maison, tout ça est agaçant.
Le curseur a l'air ridicule.
Les enceintes se taisent.
Mais tu survivras.

<!-- S24 -->
Mais un serveur qui cesse de faire
confiance au réseau dont il fait partie,
c'est plus personne qui se connecte,
et quelqu'un du service informatique
passe une très mauvaise matinée.

<!-- S25 -->
Et c'est là que ça cesse d'être
une collection d'anecdotes.

<!-- S26 -->
Parce qu'on peut regarder l'historique
des mises à jour de Microsoft.
Microsoft le publie.
Chaque mois, ils répertorient
ce que leurs mises à jour ont cassé.

<!-- S27 -->
Et si tu alignes
une seule année de cette liste,
le même schéma
se répète encore et encore.

<!-- S28 -->
Janvier a cassé des appareils audio
et des webcams.
Février a fait tourner le curseur,
la machine semblait figée.

<!-- S29 -->
Mars a donné des écrans bleus
et des installations
bloquées à mi-chemin.
Avril a cassé la connexion
par reconnaissance faciale.

<!-- S30 -->
En mai, l'Explorateur ne répondait
plus à la souris.
Et octobre a cassé les connexions
vers ton propre ordinateur.

<!-- S31 -->
Pas internet.
L'adresse qui veut dire « cette machine ».

<!-- S32 -->
Et deux d'entre elles
sont vraiment remarquables.

<!-- S33 -->
Une mise à jour a cassé le bouton
qui réinitialise le PC.
Une autre, l'écran de récupération,
où les souris et claviers USB
ne répondaient plus.

<!-- S34 -->
Relis ça.

<!-- S35 -->
Deux fois en trois mois,
une mise à jour a cassé l'outil
qui répare un ordinateur cassé.

<!-- S36 -->
Et un détail de plus,
peut-être le plus important.
Ce bug audio, celui où Windows
dit que l'appareil ne démarre pas ?

<!-- S37 -->
Il est apparu en janvier.
Puis il est réapparu
vingt mois plus tard.

<!-- S38 -->
Le même symptôme.
Le même type d'appareil.
Le même message.

<!-- S39 -->
Ce n'est pas une histoire
de code mal écrit.
C'est une histoire de tests.

<!-- S40 -->
Et rien de tout ça n'est nouveau.

<!-- S41 -->
En 2024, une mise à jour
a empêché Linux de démarrer
sur les machines en dual boot.
Le message d'erreur disait, mot pour mot :

<!-- S42 -->
« Quelque chose s'est
très mal passé. »

<!-- S43 -->
Ce qui est, franchement, le message
le plus juste que Windows ait affiché.

<!-- S44 -->
Et en 2018, une version
a dû être retirée complètement,
après que des gens ont signalé
que leurs fichiers avaient disparu.

<!-- S45 -->
Donc, à ce stade,
tu peux raisonnablement conclure :
Microsoft ne sait tout simplement pas
écrire de logiciels.

<!-- S46 -->
Et ça expliquerait tout.
Les bugs.
Les régressions.
Les mises à jour qui réparent une chose
et en cassent une autre.

<!-- S47 -->
Mais cette explication
pose un problème.
Microsoft ne fait pas que Windows.

<!-- S48 -->
Ils font Office.
Visual Studio.
Exchange.
Teams.
Et un très grand cloud.

<!-- S49 -->
Et tout ça a eu
ses propres bugs, ses régressions
et ses pannes spectaculaires.

<!-- S50 -->
Et c'est important.
Parce que l'explication habituelle pour
Windows, c'est qu'il traîne
trente ans de vieux code.

<!-- S51 -->
Un service cloud moderne
ne traîne trente ans
de rien du tout.
Il a été construit récemment,
par des gens qui savaient
exactement ce qu'ils construisaient.

<!-- S52 -->
Et il tombe en panne quand même.

<!-- S53 -->
Donc le problème n'a jamais été
seulement le vieux code.
Le problème, c'est la complexité
à l'échelle de Microsoft.

<!-- S54 -->
Et Windows est l'endroit
où cette complexité
se voit le mieux.

<!-- S55 -->
Parce que Windows n'est pas vraiment
un système d'exploitation.
Tout en bas, il y a une architecture
qui remonte au début des années 1990.

<!-- S56 -->
Puis des décennies d'interfaces.
Puis des couches de compatibilité.
Puis des pilotes.
Puis des services.

<!-- S57 -->
Puis des frameworks plus récents,
bâtis sur des frameworks plus anciens.
Puis une nouvelle apparence.
Puis encore une nouvelle apparence.

<!-- S58 -->
C'est moins un système d'exploitation
qu'une fouille archéologique
qui, va savoir comment, tourne encore.

<!-- S59 -->
Et Microsoft n'a pas le droit
de raser le site,
parce que des entreprises dépendent
de ce qu'il y a dessous.
Il y a une vidéo entière là-dessus.

<!-- S60 -->
Ce qui compte ici,
c'est l'effet sur les bugs.
Chaque couche doit continuer à marcher
avec chaque couche en dessous.

<!-- S61 -->
Donc un changement ici en haut
peut casser quelque chose
que personne n'a ouvert depuis des années.

<!-- S62 -->
Et il y a encore un indice
sur la façon dont ça se passe,
et il ne parle pas du tout de bugs.

<!-- S63 -->
C'est un schéma.
Microsoft retire quelque chose.
Les utilisateurs se plaignent.
Microsoft met des années
à y revenir.

<!-- S64 -->
Et entre-temps,
quelqu'un d'autre fabrique un outil
qui le remet en place.

<!-- S65 -->
Et le plus drôle,
c'est que ce ne sont pas
des projets d'amateurs obscurs.

<!-- S66 -->
Il existe des applications entières
dont le seul rôle est de faire que Windows
se comporte davantage comme...

<!-- S67 -->
eh bien...
Windows.

<!-- S68 -->
Elles ramènent un ancien menu Démarrer.
Elles restaurent la barre des tâches.
Elles modifient l'Explorateur de fichiers.

<!-- S69 -->
Et certaines te donnent plus de contrôle
sur Windows que Windows lui-même.

<!-- S70 -->
Microsoft a un nombre énorme
d'ingénieurs sur ce système.
Et là, quelqu'un de l'extérieur dit :
très bien.
Je remets la vieille barre moi-même.

<!-- S71 -->
Et maintenant, autre chose a changé.
Microsoft utilise de plus en plus l'IA
dans la façon dont son logiciel s'écrit.

<!-- S72 -->
Son propre PDG a déclaré
que vingt à trente pour cent
du code de leurs dépôts
est désormais écrit par du logiciel.

<!-- S73 -->
Et ça devrait vouloir dire
plus de productivité.
Plus de corrections.
Un développement plus rapide.

<!-- S74 -->
Mais il y a un goulot d'étranglement.
Écrire du code peut aller plus vite.

<!-- S75 -->
Tester un énorme système hérité
ne va pas forcément plus vite.

<!-- S76 -->
Et si tu produis des changements
plus vite que tu ne peux tester
comment ils interagissent avec
des décennies de code existant...

<!-- S77 -->
tu risques simplement de finir
par produire des régressions plus vite.

<!-- S78 -->
Et là, il faut être prudent.
Ce chiffre concerne tout Microsoft,
pas Windows en particulier.
Et personne n'a démontré
que l'IA a causé l'un de ces bugs.

<!-- S79 -->
Peut-être que l'IA n'a pas rendu
Microsoft plus mauvais aux tests.

<!-- S80 -->
Peut-être qu'elle a seulement accéléré
le problème qui était déjà là.

<!-- S80b -->
Au passage, si tu veux voir
où mène la suite de tout ça,
tu peux t'abonner.

Ça aide vraiment la chaîne.

<!-- S81 -->
L'essentiel de cette vidéo a soutenu
que Microsoft a
un vrai problème de qualité.
Et cet argument tient.

<!-- S82 -->
Mais voici la partie
qui surprend les gens.
Pourquoi le noyau
serait-il différent ?

<!-- S83 -->
Parce que presque tout
ce qui a été décrit jusqu'ici
n'est pas le noyau.

<!-- S84 -->
Le curseur.
La barre des tâches.
Le menu Démarrer.
Les paramètres.
L'écran de récupération.

<!-- S85 -->
Tout ça est posé par-dessus.

<!-- S86 -->
Le noyau, c'est la partie en dessous.
Il décide quel programme tourne
sur quel cœur du processeur.
Il distribue la mémoire.
Il parle au matériel.

<!-- S87 -->
Et si cette partie déraillait vraiment,
le symptôme ne serait pas
une souris qui a l'air ridicule.

<!-- S88 -->
Le symptôme, c'est une machine
qui s'arrête, corrompt tes données
ou laisse entrer quelqu'un en silence.

<!-- S88b -->
Et le noyau a quelque chose
que le reste de Windows n'a pas.
Des contraintes strictes.

<!-- S88c -->
Un ordonnanceur ne peut pas décider
de se comporter autrement
parce que quelqu'un a redessiné
le menu Démarrer.

<!-- S88d -->
La gestion mémoire ne se modernise pas
en déplaçant un bouton.
Et un pilote n'a pas le droit de supposer
que le matériel sera bien élevé.

<!-- S88e -->
Et surtout : le noyau n'a nulle part
où cacher une erreur, derrière
une page de paramètres un peu confuse.

<!-- S88f -->
Ce qui est une raison de soupçonner
que c'est une tout autre
affaire technique
que le reste de Windows.

<!-- S89 -->
Mais soupçonner n'est pas prouver.
Alors regarde ce que ce truc
a réellement dû encaisser.

<!-- S90 -->
L'architecture tout en bas est vieille.
Très vieille.
Et elle a survécu.

<!-- S91 -->
Elle est devenue Windows 2000.
Puis XP.
Puis Vista.
Puis 7, 8, 10 et 11.

<!-- S92 -->
Les processeurs ont changé.
Le nombre de cœurs a explosé.
La taille des mémoires a explosé.
Les machines virtuelles sont passées
d'exotiques à tout à fait banales.

<!-- S93 -->
Et la même famille de code
a fini par tourner sur des serveurs
dans le monde entier.

<!-- S94 -->
Serveurs de fichiers.
Authentification en entreprise.
Machines virtuelles.
Des charges que personne n'imaginait
quand ça a été conçu.

<!-- S95 -->
Si la partie qui décide
ce qui tourne et quand,
et qui distribue la mémoire,
était désespérément cassée...
la facture serait impossible à cacher.

<!-- S96 -->
Maintenant, un aveu honnête.
Personne hors de Microsoft ne peut lire
le code du noyau actuel,
donc personne ne peut le dire beau.

<!-- S96b -->
Même si quelqu'un a bel et bien
regardé une version plus ancienne.

<!-- S96c -->
Une partie du code de Windows 2000
a fuité en 2004,
et l'an dernier un chercheur
l'a passée au peigne fin.

<!-- S96d -->
Les conclusions n'étaient pas flatteuses.
Des bugs restés dans ce code
pendant seize ans
avant que quelqu'un ne les corrige.

<!-- S96e -->
Mais c'est le grand-père
du noyau d'aujourd'hui,
et seule une fraction a fuité.
Ça parle de l'an 2000,
pas de maintenant.

<!-- S97 -->
Et survivre n'est pas la même chose
qu'être excellent.

<!-- S98 -->
Donc ce n'est pas une affirmation
selon laquelle le noyau est génial.
Personne n'en sait rien.

<!-- S99 -->
Mais on a des décennies de preuves
qu'il fait son travail.

<!-- S100 -->
Et c'est une conclusion bien plus étrange
que « Windows, c'est nul ».

<!-- S101 -->
Parce que ça veut dire que la réponse
à « que fait leur QA »
n'est probablement pas
« Microsoft ne sait pas coder ».

<!-- S102 -->
C'est qu'ils ont passé des décennies
à bâtir du neuf sur du vieux,
sans jamais avoir le droit
de jeter le vieux.

<!-- S103 -->
Le résultat est énorme.
Puissant.
Compatible.
Et parfois ridicule.

<!-- S104 -->
Tu installes une mise à jour.
Ton son disparaît.
Ton curseur ressemble à Windows 98.

<!-- S105 -->
Et sous tout ça,
quelque chose décide en silence
quel programme tourne ensuite.
Distribue la mémoire.
Parle au matériel.

<!-- S106 -->
En faisant exactement
ce qu'il doit faire.

<!-- S107 -->
Du moins...
on le croit.

<!-- S108 -->
Parce que, contrairement à la barre...
on ne le voit pas.
