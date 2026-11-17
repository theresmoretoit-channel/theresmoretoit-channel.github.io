<!-- S01 -->
Tu achètes un disque tout neuf.
Un téraoctet, complètement vide.
Avant qu'il puisse accueillir le moindre fichier,
il faut d'abord le formater.

<!-- S02 -->
Alors tu le formates en ext4,
le système de fichiers standard
de nombreux ordinateurs sous Linux.
Avec les réglages par défaut,
avant même d'avoir enregistré quoi que ce soit,
environ dix-sept gigaoctets ont disparu.

<!-- S03 -->
Rien n'est encore stocké.
Ni photos, ni documents.
Alors qu'est-ce qui prend toute cette place ?

<!-- S04 -->
Et pourquoi faut-il formater un disque,
pour commencer ?
Il sait déjà stocker des données.
Il peut lire et écrire des milliers de milliards de bits.

<!-- S05 -->
Pourquoi l'ordinateur ne peut-il pas juste écrire
là où il y a de la place ?

<!-- S06 -->
Parce que stocker des données
et les retrouver ensuite,
ce sont deux problèmes très différents.

<!-- S07 -->
Imagine un bureau qui distribue
des feuilles blanches au lieu de formulaires.
Tout finit noté quelque part...
et personne ne retrouve rien.

<!-- S08 -->
Un disque sans système de fichiers,
c'est cette pile de papier.
Mais une meilleure image,
c'est un cahier.

<!-- S09 -->
Imagine un cahier
de mille pages,
avec quelques règles pour s'en servir.

<!-- S10 -->
D'abord, chaque page a un numéro.
Du coup, chaque endroit du cahier
a une adresse.
Page quatre cent douze,
ça désigne un seul endroit précis.

<!-- S11 -->
Ensuite, les premières pages
forment une table des matières.
Chaque entrée donne un nom,
et la page où il se trouve.
Crêpes : page douze.

<!-- S12 -->
Enfin, tout à la fin du cahier,
il y a une liste des pages
encore blanches.

<!-- S13 -->
Maintenant, ajoute une recette.
Tu cherches une page blanche à la fin.
Tu y écris la recette.
Tu ajoutes une ligne à la table des matières.
Et tu barres cette page
dans la liste des pages blanches.

<!-- S14 -->
Une recette, trois endroits.
Et les trois doivent concorder.

<!-- S15 -->
Puis la recette des crêpes s'allonge.
La page douze est pleine,
et la page treize est déjà prise.
Alors elle continue page quatre-vingt-sept,
et la table des matières doit l'indiquer.

<!-- S16 -->
Et voilà le hic.
Si tu veux de la place pour mille entrées
dans la table des matières,
tu dois réserver ces pages
avant d'écrire la moindre recette.

<!-- S17 -->
Voilà pour l'analogie.
Voici ce qu'il y a vraiment sur le disque.

<!-- S18 -->
Un disque ne connaît ni fichiers,
ni dossiers, ni noms.
Il offre juste une longue rangée
de cases numérotées, appelées secteurs.

<!-- S19 -->
Sur un disque dur,
les données sont sur des plateaux qui tournent.
Un SSD les garde en mémoire flash.
Dans les deux cas, l'ordinateur demande seulement
un secteur par son numéro,
et c'est le disque qui sait où il se trouve.

<!-- S20 -->
Un secteur, c'est petit.
En général 512 octets,
ou 4 096
sur les disques récents.

<!-- S21 -->
Les systèmes de fichiers travaillent souvent
avec de plus gros morceaux, appelés blocs.
En ext4, un bloc fait quatre kilo-octets,
soit la taille de huit secteurs à l'ancienne.

<!-- S22 -->
Ces blocs numérotés,
ce sont les pages du cahier.
Il manque encore au système de fichiers
les deux autres parties :
une table des matières,
et une liste de ce qui est libre.

<!-- S23 -->
C'est ça que construit le formatage.
Et c'est là
que sont passés ces dix-sept gigaoctets.

<!-- S24 -->
Ext4 réserve une fiche
pour chaque fichier et dossier
que le disque pourra contenir en même temps.
Chaque fiche fait
256 octets.
On l'appelle un inode.

<!-- S25 -->
Un jour, chaque inode indiquera
la taille d'un fichier,
quand il a été modifié,
qui a le droit de l'ouvrir,
et quels blocs contiennent ses données.

<!-- S26 -->
Sur un disque d'un téraoctet,
ext4 en prépare environ
soixante et un millions.
Tous vides, tous en attente.
Ça fait presque seize gigaoctets
de fiches vierges.

<!-- S27 -->
Pourquoi soixante et un millions ?
Ext4 fait une estimation simple :
un inode pour chaque tranche de seize kilo-octets
d'espace sur le disque.
Sur un ordinateur ordinaire,
la plupart de ces fiches
ne serviront jamais.

<!-- S28 -->
Environ un gigaoctet de plus
part dans un journal,
sur lequel on reviendra.
Le reste, c'est encore de la comptabilité,
dont une carte avec un bit par bloc,
qui indique s'il est utilisé ou libre.

<!-- S29 -->
Et ce nombre est fixe, lui aussi.
Épuise toutes les fiches
avec des millions de minuscules fichiers,
et le disque te dira qu'il est plein...
même s'il reste des gigaoctets d'espace.

<!-- S30 -->
Alors regardons-le fonctionner.
On va créer un fichier appelé hello.txt.
Dedans, un seul mot : hello.
Cinq lettres. Cinq octets.

<!-- S31 -->
Le système de fichiers choisit un inode vide.
Disons le numéro treize.
Puis il trouve un bloc libre dans la carte,
et le marque comme utilisé.

<!-- S32 -->
Il écrit les cinq octets dans ce bloc.
Puis il remplit l'inode :
cinq octets, créé à l'instant,
et stocké dans ce seul bloc.

<!-- S33 -->
Et enfin, dans le dossier,
il ajoute une ligne :
le nom hello.txt,
et le numéro treize.

<!-- S34 -->
Remarque où le nom a atterri.
Pas dans le fichier.
Pas dans l'inode.
Le nom se trouve dans le dossier,
qui n'est en fait qu'une liste
de noms et de numéros.

<!-- S35 -->
Et un dossier n'est qu'un fichier de plus.
Et ce qu'il contient, justement,
c'est cette liste.

<!-- S36 -->
C'est aussi pour ça que déplacer un fichier
vers un autre dossier du même système de fichiers
est instantané, quelle que soit sa taille.
Un dossier perd une ligne,
l'autre en gagne une,
et en général, le contenu
ne bouge pas du tout.

<!-- S37 -->
Cinq octets de texte...
et sur le disque, il en occupe
4 096.
Un bloc est la plus petite unité
que le système de fichiers attribue,
donc même un fichier minuscule coûte un bloc entier.

<!-- S38 -->
Quand le fichier déborde de son bloc,
le système de fichiers en trouve un autre de libre.
Peut-être juste à côté.
Peut-être complètement ailleurs.
Et l'inode garde la trace des deux.

<!-- S39 -->
Avec le temps, un gros fichier peut se retrouver
en morceaux un peu partout sur le disque.
Un disque dur doit sauter de l'un à l'autre.
Un SSD s'en sort beaucoup mieux.

<!-- S40 -->
Le programme qui a enregistré le fichier
ne sait rien de tout ça.
Il a dit « enregistre hello.txt »,
et tout le reste s'est fait en coulisses.

<!-- S41 -->
Maintenant, supprime-le.
Le nom est retiré du dossier.
L'inode est marqué comme libre.
Le bloc retourne dans la liste des blocs libres.

<!-- S42 -->
Sur un disque dur classique,
les cinq octets eux-mêmes restent en place.
Personne n'y a touché.
Ils restent là jusqu'à ce que quelque chose de nouveau
soit écrit par-dessus.

<!-- S43 -->
C'est pour ça qu'on peut parfois
récupérer un fichier supprimé.
En général, supprimer n'efface pas
le contenu.
Ça marque juste l'espace comme disponible.

<!-- S44 -->
Sur un SSD, c'est moins sûr.
Le système de fichiers peut dire au disque
que ces blocs ne servent plus,
et le disque peut jeter ce qu'ils contiennent.
Après ça, récupérer le fichier
devient beaucoup moins probable.

<!-- S45 -->
Un système de fichiers, c'est donc surtout un comptable.
Créer ce seul fichier
a demandé de mettre à jour trois choses :
le dossier, l'inode,
et la carte des blocs libres.

<!-- S46 -->
Maintenant, coupe le courant
en plein enregistrement d'un fichier.

<!-- S47 -->
Peut-être que le bloc a été marqué comme utilisé,
mais qu'aucun inode ne pointe encore dessus.
Cet espace est tout simplement perdu.
Agaçant, mais sans danger.

<!-- S48 -->
Ou alors l'inode pointe vers un bloc
que la carte considère toujours comme libre.
Le fichier suivant peut être écrit
juste par-dessus.
Et le premier est détruit sans bruit.

<!-- S49 -->
Voilà pourquoi ext4 tient un journal.
Avant de modifier sa comptabilité,
il note ce qu'il s'apprête à faire.
Après un plantage, il rejoue seulement les modifications
qu'il avait fini de noter
et qu'il avait marquées comme terminées.
Tout ce qui est inachevé est ignoré.

<!-- S50 -->
Et il y a un problème plus discret.
Parfois, un disque modifie un bit
sans prévenir personne.

<!-- S51 -->
Ext4 protège ses propres fiches
avec des sommes de contrôle,
il peut donc y repérer des dégâts.
Mais le contenu de tes fichiers ?
Ça, il lui fait simplement confiance.

<!-- S52 -->
Certains systèmes de fichiers vérifient les deux.
Et certains gardent une deuxième copie :
quand une copie est abîmée,
ils peuvent la réparer à partir de l'autre.
Repérer un problème et le réparer,
ce n'est pas la même chose.

<!-- S53 -->
Bref, tous les systèmes de fichiers font le même travail :
des blocs numérotés, une liste de noms,
et une carte de ce qui est libre.

<!-- S54 -->
Mais les choix diffèrent.
Ext4 prépare soixante et un millions de fiches
avant que tu enregistres quoi que ce soit.
NTFS, sous Windows, range ses fiches
dans une grande table qui grandit au fur et à mesure.

<!-- S55 -->
Et Btrfs ne prépare pas
de table fixe d'inodes à l'avance.
Il les crée à mesure que les fichiers arrivent.
Et normalement, il n'écrase pas
les données sur place.
Il écrit une nouvelle copie,
et seulement ensuite, il libère l'ancienne.

<!-- S56 -->
Par défaut, il calcule aussi les sommes de contrôle de tes fichiers,
pour savoir s'ils ont été abîmés.

<!-- S57 -->
Et comme l'ancienne copie
n'est pas écrasée,
un instantané peut la garder en vie.
Ça change la réponse
à presque toutes les questions de cette vidéo :
ce que provoque un plantage,
ce que veut dire supprimer,
et même ce qu'est une copie.

<!-- S58 -->
C'est là que commence la prochaine vidéo.

<!-- S59 -->
Alors j'ai une question pour toi.
Un système de fichiers doit-il juste stocker tes fichiers,
ou aussi les protéger ?
Dis-le-moi dans les commentaires.
