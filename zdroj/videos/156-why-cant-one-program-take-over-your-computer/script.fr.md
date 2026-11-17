<!-- S01 -->
Le 19 juillet 2024,
une entreprise de sécurité nommée CrowdStrike
a envoyé une mise à jour de routine.

<!-- S02 -->
Pas un nouveau programme.
Juste un petit fichier de configuration.

<!-- S03 -->
En quelques heures, 8,5 millions
d'ordinateurs sous Windows s'étaient bloqués
sur un écran bleu.

<!-- S04 -->
Des compagnies aériennes ont cloué leurs avions au sol.
Des hôpitaux ont annulé des opérations.
Une chaîne d'info a cessé d'émettre.

<!-- S05 -->
Et l'erreur derrière tout ça
était tout à fait banale.
Le programme attendait 20 données.
La mise à jour lui en a donné 21.

<!-- S06 -->
Tes jeux et tes applis font
ce genre d'erreur tout le temps.
Quand ça arrive, le jeu se ferme,
et tu le relances.

<!-- S07 -->
Le même genre de bug.
L'un ferme une fenêtre.
L'autre arrête
8,5 millions de machines.

<!-- S08 -->
La différence n'est pas dans l'erreur.
Elle tient à l'endroit où le code tournait.

<!-- S09 -->
Alors pourquoi un programme ne peut-il pas
prendre le contrôle de ton ordinateur...
et pourquoi celui-ci l'a pu ?

<!-- S10 -->
Ça n'a pas toujours été comme ça.

<!-- S11 -->
Sur un PC sous DOS dans les années 1980,
rien dans le processeur n'arrêtait un programme.
Il pouvait écrire n'importe où en mémoire
et parler directement au matériel.

<!-- S12 -->
Il suffisait qu'un programme écrive
là où il ne fallait pas
pour écraser le système d'exploitation,
et toute la machine se figeait.

<!-- S13 -->
La solution a été d'arrêter de faire confiance aux programmes,
et de confier
la méfiance au processeur.

<!-- S14 -->
En 1982, le processeur 80286 d'Intel
a introduit le mode protégé,
avec quatre niveaux de privilège.

<!-- S15 -->
On les dessine généralement
comme quatre anneaux, l'un dans l'autre.

<!-- S16 -->
L'anneau 0 est au centre.
L'anneau 3 est à l'extérieur.

<!-- S17 -->
Et la numérotation va à l'envers.
Plus le numéro est bas,
plus le code a de droits.

<!-- S18 -->
L'anneau 0 appartient au noyau,
le cœur du système d'exploitation.
Il distribue la mémoire,
décide quel programme tourne ensuite
et parle au matériel.

<!-- S19 -->
L'anneau 3, c'est là que tournent ton navigateur,
tes jeux et ton éditeur de texte.
C'est ce qu'on appelle le mode utilisateur.

<!-- S19b -->
Windows, macOS et Linux
répartissent tous le travail de cette façon.
Le noyau dans l'anneau 0,
tes applis dans l'anneau 3.

<!-- S19c -->
Les téléphones et les Mac récents d'Apple
utilisent plutôt des puces ARM.
Là, les niveaux s'appellent des exception levels.
Autre nom, même partage :
un pour le noyau, un pour tes applis.

<!-- S20 -->
Le processeur sait toujours
dans quel anneau il tourne.
Et il vérifie.

<!-- S21 -->
Certaines instructions ne marchent que dans l'anneau 0.
Désactiver les interruptions, par exemple,
ou changer la façon dont la mémoire est mappée.

<!-- S22 -->
Quand un programme de l'anneau 3 en essaie une,
le processeur refuse.
Il déclenche une exception
et passe la main au noyau,
qui met généralement fin au programme.

<!-- S23 -->
La mémoire a droit au même traitement.
Chaque page de mémoire est marquée
soit user, soit supervisor.

<!-- S24 -->
Un programme de l'anneau 3
qui touche une page supervisor
n'obtient pas les données.
Il est arrêté.

<!-- S25 -->
Ton navigateur et ton jeu
tournent tous les deux dans l'anneau 3.
Ce qui les tient séparés,
c'est que chacun a sa propre carte de la mémoire.
La mémoire de l'autre programme
n'y figure tout simplement pas.

<!-- S26 -->
Alors quand un jeu plante,
les dégâts restent dans le jeu.
Le noyau fait le ménage.
Tout le reste continue.

<!-- S27 -->
Maintenant, reprenons CrowdStrike.
Son pilote tournait dans l'anneau 0,
juste à côté du noyau.

<!-- S28 -->
Rien au-dessus de l'anneau 0
ne peut rattraper une erreur pareille.

<!-- S29 -->
Alors Windows a fait la seule chose sûre qui restait.
Il a arrêté toute la machine, exprès,
plutôt que de continuer avec une mémoire
à laquelle il ne pouvait plus se fier.

<!-- S30 -->
C'est ça, l'écran bleu.

<!-- S31 -->
Et comme le pilote démarrait
à chaque démarrage de Windows,
chaque redémarrage ramenait le plantage.

<!-- S32 -->
Mais ça soulève une question.
Si ton navigateur ne peut pas toucher le matériel,
comment fait-il pour enregistrer un fichier
ou envoyer quoi que ce soit sur le réseau ?

<!-- S33 -->
Il demande.

<!-- S34 -->
Le programme place sa demande
dans les registres du processeur.
Quel fichier. Où doivent aller les données.
Combien.

<!-- S35 -->
Puis il exécute une instruction spéciale.
Sur un PC moderne, elle s'appelle SYSCALL.

<!-- S36 -->
À cet instant, le processeur passe
de l'anneau 3 à l'anneau 0...

<!-- S37 -->
mais il ne saute pas
là où le programme veut.
Il saute vers un unique point d'entrée
que le noyau a choisi à l'avance.

<!-- S38 -->
Le noyau vérifie la demande,
fait le travail
et redescend dans l'anneau 3.
Le programme n'a jamais touché le disque lui-même.

<!-- S39 -->
C'est un appel système,
et ça arrive en permanence.

<!-- S40 -->
On les a comptés sur un ordinateur portable.
Un programme qui ne fait rien du tout
en fait quand même 30.

<!-- S41 -->
Firefox, en démarrant
et en chargeant une seule page de Wikipédia,
en a fait environ 670 000
en 20 secondes...
alors même que notre comptage le ralentissait.

<!-- S42 -->
Chacun d'eux
est un aller-retour à travers le mur.

<!-- S43 -->
Reste un détail curieux.
Quatre anneaux,
et on n'en a eu besoin que de deux.

<!-- S44 -->
Qu'est-il arrivé aux anneaux 1 et 2 ?

<!-- S45 -->
L'idée des anneaux est plus ancienne que le PC.
Multics, un système d'exploitation
de la fin des années 1960,
en avait huit.

<!-- S46 -->
L'idée, c'était des couches de confiance.
Le cœur du système au milieu,
des services moins fiables autour
et les programmes à l'extérieur.

<!-- S46b -->
Intel a dessiné le même schéma.
Les anneaux 1 et 2 étaient prévus
pour les couches intermédiaires,
comme les pilotes et les services système.
Plus de confiance que tes applis,
moins que le noyau.

<!-- S47 -->
Deux obstacles se sont dressés.

<!-- S48 -->
D'abord, des systèmes comme Unix et Windows NT
étaient conçus pour tourner
sur de nombreux types de processeurs.

<!-- S49 -->
Et la seule séparation
que tous les processeurs offraient,
c'était deux niveaux.
Un pour le noyau,
un pour tout le reste.

<!-- S50 -->
Ensuite, le processeur x86 lui-même.
Quand il mappe la mémoire,
chaque page ne connaît que deux états.
User ou supervisor.

<!-- S51 -->
Les anneaux 1 et 2 comptent comme supervisor.
Un pilote dans l'anneau 1
pourrait donc quand même toucher la mémoire du noyau.
L'anneau en plus ne protégerait pas grand-chose.

<!-- S51b -->
Quelques systèmes s'en sont quand même servis.
OS/2 laissait certains programmes passer dans l'anneau 2,
juste pour parler directement au matériel.

<!-- S51c -->
Et avant que les processeurs aient de l'aide
pour faire tourner des machines virtuelles,
Xen et VirtualBox déplaçaient le noyau du système invité
dans l'anneau 1,
pour que le système en dessous
puisse garder l'anneau 0 pour lui seul.

<!-- S52 -->
En 2023, Intel a proposé
de supprimer complètement les anneaux 1 et 2.

<!-- S53 -->
En décembre 2024, Intel a abandonné le projet.
Ils sont toujours dans ton processeur.
Presque rien ne s'en sert.

<!-- S54 -->
Jusqu'ici, tout ça a l'air rassurant.
Les règles sont dans le matériel,
et le matériel vérifie chaque accès.

<!-- S55 -->
En 2017, trois équipes de chercheurs,
chacune de son côté,
ont trouvé un moyen de traverser ce mur.

<!-- S56 -->
Ils l'ont appelé Meltdown.
Et pour le comprendre,
il te faut connaître une astuce
qu'utilisent les processeurs modernes.

<!-- S57 -->
Un processeur n'attend pas
qu'une instruction soit terminée
pour commencer la suivante.
Il prend de l'avance
sur des instructions dont il aura probablement besoin.

<!-- S58 -->
S'il s'est trompé,
il jette les résultats,
comme si de rien n'était.

<!-- S59 -->
Voilà la faille.
Sur les puces Intel concernées,
un programme de l'anneau 3 pouvait demander
un octet de la mémoire du noyau...

<!-- S60 -->
et le processeur allait le chercher
et le transmettait aux instructions suivantes
avant d'avoir fini de vérifier
si c'était autorisé.

<!-- S61 -->
La vérification échouait bel et bien.
Le résultat était jeté.

<!-- S62 -->
Mais ces instructions suivantes
avaient déjà utilisé l'octet secret
pour charger un morceau
de la propre mémoire du programme
dans le cache du processeur.

<!-- S63 -->
Et le cache n'oublie pas
juste parce que le résultat a été annulé.

<!-- S64 -->
Alors le programme chronomètre
le temps que met chaque morceau de sa mémoire à répondre.
Celui qui répond vite
trahit l'octet secret.

<!-- S65 -->
Octet par octet,
un programme ordinaire pouvait lire
la mémoire du noyau,
et tous les secrets qui s'y trouvaient.
Mots de passe et clés de chiffrement compris.

<!-- S66 -->
Meltdown touchait des processeurs Intel
remontant jusqu'à 1995.

<!-- S67 -->
La faille a été rendue publique
le 3 janvier 2018.

<!-- S68 -->
Le correctif ne pouvait pas changer le silicium.
Alors les systèmes d'exploitation ont changé la carte.

<!-- S69 -->
Pendant que ton programme tourne,
la mémoire du noyau est désormais retirée
presque entièrement de sa carte.
Il n'y a plus rien à aller chercher.

<!-- S70 -->
Mais souviens-toi des appels système.
Chaque passage à travers le mur
doit maintenant changer aussi de carte.

<!-- S71 -->
Red Hat a mesuré les correctifs contre Meltdown
et une faille voisine, Spectre.
Moins de 1 % sur certaines tâches...
jusqu'à 19 % sur des bases de données très sollicitées.

<!-- S72 -->
La règle était juste depuis le début.
Le processeur la vérifiait simplement trop tard.

<!-- S73 -->
Ce qui nous ramène à CrowdStrike,
et à une question plus difficile.

<!-- S74 -->
Pourquoi un programme de sécurité
était-il dans l'anneau 0, au départ ?

<!-- S75 -->
Parce que de là, il voit tout.
Il démarre avant les autres logiciels.
Et un malware avec des droits d'administrateur
a plus de mal à le désactiver.

<!-- S76 -->
La liste de Microsoft lui-même
se termine par un avertissement.
Les pilotes du noyau offrent tout ça au détriment de la résilience.

<!-- S77 -->
Après la panne,
Microsoft a commencé à mettre au point un moyen
pour que les antivirus
tournent en dehors du noyau.

<!-- S78 -->
À l'automne 2026,
ça n'existe encore que dans des versions de test de Windows.
Et le noyau n'a pas été fermé
aux entreprises de sécurité.

<!-- S79 -->
Tes jeux font face au même dilemme.

<!-- S80 -->
Les triches qui tournent dans le noyau
sont invisibles pour un anti-triche
qui tourne dans l'anneau 3.

<!-- S81 -->
Alors l'anti-triche s'est installé là aussi.
Vanguard, de Riot, utilisé par Valorant,
place un pilote dans l'anneau 0.
Sur la plupart des PC, il se charge au démarrage de Windows...
même si tu n'ouvres jamais le jeu.

<!-- S82 -->
Ça ne le rend pas défectueux.
Mais il se trouve au même endroit
que le pilote de CrowdStrike,
là où une seule erreur arrête toute la machine.

<!-- S83 -->
Alors pourquoi un programme ne peut-il pas
prendre le contrôle de ton ordinateur ?

<!-- S84 -->
Parce que le processeur tient
presque tous les programmes à l'écart du centre,
et les vérifie à chaque fois qu'ils frappent à la porte.

<!-- S85 -->
Mais le processeur ne peut pas décider
qui on laisse entrer.
Ça, ce sont des gens qui le décident...
chaque fois qu'ils installent un pilote.

<!-- S86 -->
Alors voici une question pour les commentaires.
Qui devrait décider quels programmes
entrent dans l'anneau 0 :
toi, Microsoft,
ou les entreprises qui les fabriquent ?
