<!-- S01 -->
En 1993, un jeu appelé Doom
tournait sur un ordinateur
doté de 4 mégaoctets de mémoire.

<!-- S02 -->
C'est à peu près la taille
d'une seule photo sur ton téléphone.

<!-- S03 -->
Il n'y avait pas d'accélérateur 3D.
Le processeur principal
s'occupait de tout le rendu.

<!-- S04 -->
Aujourd'hui, un développeur part d'un moteur,
comme Unity ou Unreal,
qui s'occupe des graphismes, du son,
de la mémoire et du matériel.

<!-- S05 -->
Sous DOS, tout ça
était le problème du développeur.
Et bien souvent, celui du joueur aussi.

<!-- S06 -->
Alors, à quel point était-ce difficile
de faire un jeu pour DOS ?

<!-- S07 -->
Commençons par la mémoire,
parce que la mémoire, c'était le chaos.

<!-- S08 -->
Le premier IBM PC, sorti en 1981,
pouvait adresser 1 mégaoctet de mémoire.

<!-- S09 -->
Mais seuls les
640 premiers kilooctets
étaient prévus pour les programmes.

<!-- S10 -->
Les 384 autres
étaient réservés à la mémoire vidéo,
aux cartes d'extension et au BIOS.

<!-- S11 -->
Pendant plus de dix ans,
DOS lançait normalement les programmes
dans cet espace.
Aller au-delà demandait du travail en plus.

<!-- S12 -->
C'est de là que vient la phrase célèbre :
640K devraient suffire à tout le monde.

<!-- S13 -->
On l'attribue généralement à Bill Gates.
Rien ne prouve qu'il l'ait jamais dite,
et il le dément.

<!-- S14 -->
Au début des années quatre-vingt-dix,
un PC était livré avec 4 mégaoctets,
ou 8.

<!-- S15 -->
Et un jeu pouvait quand même s'arrêter
avec ces mots :
« mémoire insuffisante ».

<!-- S16 -->
Avoir la mémoire
et pouvoir s'en servir,
c'étaient deux choses différentes.

<!-- S17 -->
Une façon de contourner ça, c'était la mémoire paginée,
ou EMS.

<!-- S18 -->
Une fenêtre de 64 kilooctets
se trouvait dans la partie haute
de ce premier mégaoctet.
À travers elle, un programme voyait
4 pages de mémoire en plus,
de 16 kilooctets chacune,

<!-- S19 -->
et pouvait les échanger contre d'autres,
comme si tu tournais les pages d'un livre
à travers un trou dans une feuille de papier.

<!-- S20 -->
Une autre façon, c'était la mémoire étendue,
accessible via un pilote appelé HIMEM.

<!-- S21 -->
Et c'est là que
le problème du développeur
est devenu celui du joueur.

<!-- S22 -->
Les pilotes de la souris, du lecteur CD
ou de la carte son
grignotaient cette précieuse mémoire,
à moins que tu réussisses à les charger en mémoire haute.

<!-- S23 -->
Alors les joueurs ont appris à modifier deux fichiers,
CONFIG.SYS et AUTOEXEC.BAT.

<!-- S24 -->
Un jeu voulait l'EMS.
Un autre la voulait désactivée,
avec un réglage appelé NOEMS.
Et un troisième avait besoin du moindre kilooctet libre.

<!-- S25 -->
En 1993, MS-DOS 6 a ajouté
un menu au démarrage.

<!-- S26 -->
Tu choisissais la configuration
du jeu auquel tu voulais jouer,
et l'ordinateur démarrait pour ce jeu-là.

<!-- S27 -->
Certains ont fini par avoir
une entrée à part
pour presque chacun de leurs jeux.

<!-- S28 -->
Mais à cette époque,
les plus gros jeux avaient trouvé
un moyen de contourner les limites de DOS.

<!-- S29 -->
Depuis le 386,
le processeur lui-même pouvait tourner
en mode protégé 32 bits,
avec de la place pour 4 gigaoctets au maximum.

<!-- S30 -->
On a parlé du mode protégé
dans une vidéo précédente.
DOS, lui, ne savait pas s'en servir.

<!-- S31 -->
Alors les jeux apportaient leur propre assistant,
un extendeur DOS.
Le plus connu était DOS/4GW.

<!-- S32 -->
Il était fourni avec un compilateur populaire,
Watcom C.

<!-- S33 -->
Au lancement d'un jeu,
DOS/4GW faisait passer le processeur
en mode protégé,
ce qui donnait au jeu accès
à la mémoire au-delà de la limite de DOS.

<!-- S34 -->
DOS était toujours là, en dessous,
et fournissait des services comme l'accès aux fichiers.
Mais le jeu tournait désormais en mode protégé,
et non comme un programme DOS classique.

<!-- S35 -->
Si tu jouais à des jeux DOS dans les années quatre-vingt-dix,
tu as vu son nom
défiler à l'écran.

<!-- S37 -->
Passons à l'image.
Dans l'un des modes VGA les plus utilisés,
appelé Mode 13h,
l'écran faisait 320
sur 200 pixels,
en 256 couleurs.

<!-- S38 -->
Chaque pixel tenait sur un octet.
Pour colorer un pixel,
tu écrivais un nombre en mémoire.
Pas de bibliothèque graphique. Juste de la mémoire.

<!-- S39 -->
L'écran entier occupait
64 000 octets.

<!-- S40 -->
C'est un peu moins de 64 kilooctets,
assez petit pour tenir dans un seul segment,
le bloc qu'un programme 16 bits
pouvait adresser d'un coup.
Pour une fois, la mémoire était de ton côté.

<!-- S41 -->
Mais si tu dessines directement
sur l'écran visible,
le joueur voit des images à moitié finies,
et l'image scintille.

<!-- S42 -->
Alors les jeux dessinaient chaque image
d'abord dans un tampon caché,
puis copiaient l'image terminée
dans la mémoire vidéo.

<!-- S43 -->
En 1991, Michael Abrash,
programmeur et auteur,
a publié une meilleure méthode.
Il l'a appelée Mode X.

<!-- S44 -->
Elle utilisait une partie de la VGA
que la plupart des programmeurs
n'avaient jamais touchée.

<!-- S45 -->
Elle donnait des pixels carrés,
et de la place pour plusieurs écrans
dans la mémoire vidéo.

<!-- S46 -->
Le jeu dessinait sur un écran
que personne ne voyait,
puis basculait simplement sur cet écran.
Mais c'était bien plus difficile à programmer.

<!-- S47 -->
Ensuite, il y avait le son.
Et le son, c'était une loterie.

<!-- S48 -->
Le haut-parleur du PC
était fait pour biper.

<!-- S49 -->
Puis sont arrivées les cartes son,
et d'autres matériels audio.
Il n'y en avait pas deux
qui fonctionnaient de la même façon.

<!-- S50 -->
L'AdLib, avec une puce Yamaha
qui synthétisait la musique.
La Sound Blaster, qui pouvait aussi jouer
du son enregistré.

<!-- S51 -->
Le Roland MT-32,
un boîtier coûteux aux instruments plus riches.
La Gravis UltraSound.

<!-- S52 -->
Les prendre toutes en charge
voulait dire écrire des pilotes différents.

<!-- S53 -->
Et le jeu devait savoir
où se trouvait la carte.
Son port, son IRQ
et son canal DMA.

<!-- S54 -->
La réponse habituelle, pour une Sound Blaster,
c'était port 220, IRQ 7, DMA 1.
En général.

<!-- S55 -->
Il suffisait de se tromper sur un seul réglage,
et le jeu restait muet.
Ou il se figeait.

<!-- S56 -->
En 1991, un programmeur nommé John Miles
a sorti une bibliothèque
qui parlait à de nombreuses cartes son
à travers une interface unique.

<!-- S57 -->
Un jeu pouvait écrire son code audio une seule fois,
et laisser la bibliothèque gérer la carte.

<!-- S58 -->
C'était une couche de plus
entre le jeu et le matériel.
Garde ça en tête.

<!-- S59 -->
Et puis il y avait la vitesse.
Les programmeurs comptaient
chaque étape du processeur.

<!-- S63 -->
Pour trouver un pixel à l'écran,
tu multiplies sa ligne
par 320.

<!-- S63b -->
Sur les processeurs plus anciens,
une multiplication pouvait coûter cher.

<!-- S64 -->
Mais 320,
c'est 256
plus 64.
Ce sont deux puissances de deux.

<!-- S65 -->
Tu peux donc remplacer la multiplication
par deux décalages de bits et une addition.

<!-- S67 -->
Chris Sawyer a programmé au plus près du matériel.
Il a écrit Transport Tycoon, en 1994,
presque entièrement en assembleur,

<!-- S68 -->
les instructions
que le processeur comprend directement,
une par une.

<!-- S69 -->
Et parfois,
même tout ça ne suffisait pas.

<!-- S70 -->
En 1990, Wing Commander avait un bug
que l'équipe n'arrivait pas à trouver,
et la date limite approchait.

<!-- S71 -->
Quand tu quittais le jeu,
le gestionnaire de mémoire plantait
avec un message d'erreur.

<!-- S72 -->
Alors un programmeur, Ken Demarest,
a ouvert le gestionnaire de mémoire
dans un éditeur hexadécimal
et a changé le texte de ce message.

<!-- S73 -->
Désormais, il disait :
« Merci d'avoir joué à Wing Commander. »

<!-- S74 -->
Puis l'équipe a trouvé le vrai bug,
et la blague n'est jamais sortie dans le jeu.

<!-- S74b -->
Certains joueurs sont encore sûrs de l'avoir vue.
Et des jeux Origin ultérieurs
disaient vraiment au revoir comme ça.

<!-- S75 -->
Ce qui nous ramène à Doom.

<!-- S76 -->
Doom utilisait DOS/4GW
et tournait comme un programme 32 bits.

<!-- S77 -->
Le matériel de calcul en virgule flottante
n'était pas garanti sur tous les PC.

<!-- S78 -->
Alors Doom utilisait l'arithmétique en virgule fixe.
Des nombres entiers,
dont les 16 bits de poids faible
représentaient la partie fractionnaire.

<!-- S79 -->
Et son monde n'était pas
vraiment en trois dimensions.

<!-- S80 -->
Chaque niveau est un plan à plat,
avec une hauteur pour chaque sol
et chaque plafond.

<!-- S81 -->
Une pièce ne peut jamais se trouver au-dessus d'une autre.
Et tu ne peux pas vraiment regarder en haut ou en bas.

<!-- S82 -->
Avant qu'un niveau puisse être joué,
un outil découpait la carte
en arbre binaire, un BSP.

<!-- S83 -->
Le moteur parcourt cet arbre
de l'avant vers l'arrière,
en partant du côté du joueur,
et saute les zones qu'on ne peut pas voir.

<!-- S84 -->
Et Doom n'a même pas été écrit sous DOS.

<!-- S85 -->
id Software l'a développé
sur des stations de travail NeXT,
puis a compilé le résultat pour DOS.

<!-- S86 -->
Doom n'était pas un moteur 3D généraliste.
Il était conçu pour exactement
un type de monde.
Cette spécialisation
l'a aidé à tourner sur un 386.

<!-- S87 -->
Et d'autres studios voulaient ce monde.

<!-- S88 -->
Raven Software a pris une licence du moteur de Doom
pour Heretic, en 1994,
et Hexen, en 1995.

<!-- S89 -->
Doom a contribué à imposer
une nouvelle façon de faire des jeux.
Les studios pouvaient prendre la licence d'un moteur existant,
au lieu de tout construire à partir de zéro.

<!-- S90 -->
Un extendeur de mémoire.
Une bibliothèque audio.
Un moteur sous licence.

<!-- S91 -->
Chacun a retiré un problème
des mains du développeur.
Et les couches n'ont cessé de s'accumuler,
jusqu'aux moteurs
avec lesquels les développeurs commencent aujourd'hui.

<!-- S92 -->
Alors, faire des jeux, c'était plus dur à l'époque ?
À bien des égards, oui.

<!-- S93 -->
Mais la difficulté n'a pas disparu.
Elle s'est déplacée.

<!-- S94 -->
Aujourd'hui, les développeurs se battent
avec des gigaoctets de ressources
et des millions de polygones,
au lieu de quelques centaines de kilooctets.

<!-- S95 -->
Sous DOS, même le joueur
devait savoir où passait sa mémoire.

<!-- S96 -->
Alors voici une question pour toi.
Tu te souviens d'avoir créé
un menu de démarrage juste pour lancer un jeu ?
Et c'était une galère,
ou la moitié du plaisir ?
Dis-le-moi dans les commentaires.
