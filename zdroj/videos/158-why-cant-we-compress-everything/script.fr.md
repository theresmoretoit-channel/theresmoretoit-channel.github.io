<!-- S01 -->
Voici tous les scripts
jamais écrits pour cette chaîne.
158 vidéos,
près d'un million et demi d'octets de texte.

<!-- S02 -->
Passez-les dans un compresseur ordinaire
appelé gzip.
Il en ressort un peu plus d'un demi-mégaoctet.
Près des deux tiers en moins.

<!-- S03 -->
Et rien n'est perdu.
Décompressez le fichier,
et chaque script revient,
lettre pour lettre.

<!-- S04 -->
Maintenant, compressez-le encore.

<!-- S05 -->
Il grossit.
98 octets de plus.

<!-- S06 -->
Une troisième fois.
98 octets de plus.
Une quatrième.
Encore 98.

<!-- S07 -->
Le premier passage élimine les deux tiers.
Le deuxième ne trouve rien du tout.
Alors pourquoi ne pas continuer à compresser ?

<!-- S08 -->
Regardons à l'intérieur de ce deuxième fichier.
gzip n'a rien compressé.
Il a recopié les données sans les modifier,
en seize blocs.

<!-- S09 -->
Chaque bloc a reçu une étiquette de cinq octets.
Ajoutez un petit en-tête et un pied de fichier,
et vous obtenez exactement 98.

<!-- S10 -->
Quand un compresseur ne trouve rien à retirer,
il stocke les données telles quelles
et n'ajoute que ce qu'il faut pour pouvoir décompresser.

<!-- S11 -->
Alors pourquoi le deuxième passage n'a-t-il rien trouvé ?
Et un programme plus malin trouverait-il quelque chose ?

<!-- S12 -->
Un texte comme celui-ci est plein de répétitions.
Les mêmes mots, les mêmes tournures,
les mêmes petits marqueurs de scène
en haut de chaque scène.

<!-- S13 -->
En 1977, Jacob Ziv et Abraham Lempel
ont publié une astuce toute simple.
Ne réécrivez pas une répétition.
Renvoyez à l'endroit où elle se trouvait.

<!-- S14 -->
Reculez de 300 caractères
et copiez les douze suivants.
Quelques octets au lieu de douze.

<!-- S15 -->
La deuxième astuce :
donner des codes courts aux lettres fréquentes,
et des codes longs aux lettres rares.

<!-- S16 -->
En 1951, David Huffman,
étudiant de troisième cycle au MIT,
pouvait passer l'examen final
ou rendre un devoir à la place.

<!-- S17 -->
Ce devoir, proposé par Robert Fano,
consistait à trouver le code le plus efficace
parmi les codes de ce type.

<!-- S18 -->
Pendant des mois, Huffman a piétiné.
Il a abandonné
et s'est mis à réviser pour l'examen.
Puis l'idée lui est venue.

<!-- S19 -->
Prenez les deux symboles les plus rares,
réunissez-les en un seul,
et recommencez jusqu'à ce qu'il ne reste qu'un arbre.

<!-- S20 -->
Il l'a appelé plus tard
« le moment le plus singulier de ma vie ».

<!-- S21 -->
Fano n'avait pas dit à ses étudiants
qu'il avait lui-même buté sur le problème,
tout comme Claude Shannon.

<!-- S22 -->
Le code de Huffman a battu leurs deux méthodes.
Et on peut démontrer
qu'aucun code de ce type ne fait mieux.

<!-- S23 -->
Au début des années 1990,
Phil Katz a combiné les deux astuces
pour les fichiers ZIP.
gzip utilise la même méthode.

<!-- S24 -->
Le premier passage a déjà épuisé
les motifs que gzip sait trouver.

<!-- S25 -->
Ce qui reste ne lui offre aucune prise.
Pour gzip, ça ressemble à du bruit.

<!-- S26 -->
Mais un programme plus malin
pourrait voir des motifs que gzip a ratés.
Un programme pourrait-il un jour
réduire tout ce que vous lui donnez ?

<!-- S27 -->
Non.
Et pas besoin de savoir comment il fonctionne
pour en être sûr.

<!-- S28 -->
Prenez tous les fichiers
d'exactement trois bits.
Il y en a huit.

<!-- S29 -->
Maintenant, comptez tous les plus courts.
Quatre fichiers de deux bits,
deux d'un bit,
et un fichier vide.

<!-- S30 -->
Sept.

<!-- S30b -->
Huit fichiers, et sept places plus courtes
où les ranger.

<!-- S31 -->
Si chacun devenait plus court,
deux devraient partager une place.
Et quand vous décompressez,
lequel vouliez-vous ?

<!-- S32 -->
C'est ce qu'on appelle le principe des tiroirs,
et il vaut pour n'importe quelle longueur.
Il y a toujours un fichier plus court de moins
qu'il n'en faudrait.

<!-- S33 -->
Donc tout compresseur qui accepte n'importe quel fichier
et en réduit certains
doit en agrandir d'autres.
Pas parce qu'il est mal écrit.
Ils n'ont simplement nulle part ailleurs où aller.

<!-- S34 -->
Ces 98 octets,
c'est le prix que gzip paie pour ça.

<!-- S35 -->
Prenez le compresseur de votre choix.
Parmi tous les fichiers d'une taille donnée,
il peut en raccourcir moins d'un sur 250
ne serait-ce que d'un octet.

<!-- S36 -->
La compression marche quand même,
parce que les fichiers que nous créons ne sont pas aléatoires.
Ce sont des textes, des images, des programmes,
pleins de motifs.

<!-- S37 -->
Ça n'a pas empêché certains
de promettre davantage.

<!-- S38 -->
En 1992, WEB Technologies
a annoncé un logiciel capable de comprimer
presque n'importe quelles données sous un kilooctet.
Même son propre résultat,
encore et encore.

<!-- S39 -->
Son vice-président a déclaré que la méthode
« n'était pas soumise aux lois
de la théorie de l'information ».
Le produit n'est jamais sorti.

<!-- S40 -->
Alors comment les photos et la musique
deviennent-elles aussi petites ?
Elles ne suivent pas du tout cette règle.

<!-- S41 -->
Un JPEG ne revient pas identique.
Il revient assez ressemblant.
Les détails dont votre œil ne remarquera pas l'absence
sont jetés pour de bon.

<!-- S42 -->
Zoomez,
et vous verrez où ils sont passés.

<!-- S43 -->
C'est la compression avec perte,
et c'est un autre jeu.
Cette vidéo parle de l'autre sorte.
Chaque bit restitué, à l'identique.

<!-- S44 -->
Alors, pour les fichiers qui ont des motifs,
jusqu'où peut-on descendre ?
Y a-t-il un plancher ?

<!-- S45 -->
Oui.
Il a été trouvé en 1948,
dans l'article même dont parle notre vidéo
sur les codes correcteurs d'erreurs.

<!-- S46 -->
Là, Claude Shannon montrait
comment ajouter de la redondance protège un message.
Ici, il a calculé
combien on peut en retirer.

<!-- S47 -->
Sa réponse était un nombre
qu'il a appelé entropie :
la difficulté à deviner
ce qui vient ensuite.

<!-- S48 -->
Aucun code sans perte ne peut descendre sous ce nombre
en moyenne.
Mais on peut s'en approcher
autant qu'on veut.

<!-- S49 -->
Alors, à quel point l'anglais est-il imprévisible ?
En 1951, Shannon l'a mesuré
avec un jeu.

<!-- S50 -->
Il donnait à quelqu'un un passage
qu'il n'avait jamais vu,
et lui demandait de le deviner,
lettre par lettre.

<!-- S51 -->
Si la réponse était fausse,
la personne réessayait,
jusqu'à trouver la bonne.

<!-- S52 -->
Les gens se sont révélés très doués.
Avec cent lettres de contexte,
l'anglais tombait à environ un bit
par lettre.

<!-- S53 -->
Un ordinateur stocke chaque lettre
sur huit bits.
Un lecteur humain en a besoin d'environ un.

<!-- S54 -->
C'est dans cet écart que travaille la compression.
gzip a ramené les scripts de la chaîne
sous les trois bits par caractère.

<!-- S55 -->
Alors, à quel point une machine
peut-elle s'approcher d'un bit ?

<!-- S56 -->
Il existe un prix justement pour ça.
Il s'appelle le Hutter Prize,
et depuis 2020, l'épreuve porte sur un seul fichier :
un gigaoctet de Wikipédia en anglais.

<!-- S57 -->
gzip le réduit au tiers.
Les meilleurs compresseurs courants,
à environ un cinquième.

<!-- S58 -->
Le record, établi en juillet 2026,
est d'un peu plus de 100 millions d'octets.
Un dixième.

<!-- S59 -->
Et le décompresseur compte aussi.
Sa taille s'ajoute au total,
donc impossible de cacher Wikipédia
dans le programme.

<!-- S60 -->
La dotation est de 500 000 euros.
Chaque pour cent d'amélioration
rapporte 5 000.

<!-- S61 -->
Marcus Hutter, qui le finance, explique pourquoi :
« savoir bien compresser
est étroitement lié
au fait d'agir intelligemment ».

<!-- S62 -->
Parce que les programmes en tête
ne cherchent pas les répétitions.
Ils prédisent.

<!-- S63 -->
Avant chaque caractère,
ils estiment la probabilité
de chaque caractère suivant possible.
Une bonne prédiction coûte une fraction de bit.

<!-- S64 -->
C'est le jeu de devinettes de Shannon,
joué par une machine.
Les meilleurs joueurs utilisent aujourd'hui des réseaux de neurones,
entraînés à prédire ce qui vient ensuite.

<!-- S65 -->
Ça marche même sur des fichiers déjà compressés.
En 2016, Dropbox a commencé à recompresser
les JPEG de ses utilisateurs avec un meilleur prédicteur.
En moyenne, réduits de plus d'un cinquième.

<!-- S66 -->
Chaque fichier revenait bit pour bit,
et en 2017,
ça avait économisé plus de 46 pétaoctets.
Soit plus de 46 000 téraoctets.

<!-- S67 -->
Et puis il y a les géants.
En 2023, des chercheurs de DeepMind
ont utilisé un grand modèle de langage
comme compresseur.

<!-- S68 -->
Sur de petits fragments de photos en niveaux de gris,
il a battu PNG :
48 % de la taille d'origine
contre 58.

<!-- S69 -->
Sur des enregistrements de lecture à voix haute,
il a battu FLAC :
21 % contre 30.

<!-- S70 -->
Mais c'est sans compter le modèle.
Ajoutez sa taille,
et le résultat est
140 fois
plus gros que les données.

<!-- S71 -->
Un compresseur plus gros que ses données
n'a rien économisé.
Le programme fait partie de la description.

<!-- S72 -->
Et ça nous amène à la partie la plus étrange.
Voici le premier million de chiffres de pi.

<!-- S73 -->
Donnez-les à quatre compresseurs.
Le meilleur les ramène à environ
426 000 octets.

<!-- S74 -->
Maintenant, donnez aux mêmes compresseurs
un million de chiffres aléatoires.
Même résultat,
à un dixième de pour cent près.

<!-- S75 -->
Mais pi n'est pas le fruit du hasard.
Il suit une règle mathématique.
Voici un programme qui affiche
ce million de chiffres, jusqu'au dernier.

<!-- S76 -->
362 octets.
Plus de 2 000 fois plus court que le fichier.

<!-- S77 -->
Les compresseurs ne voyaient pas
la règle mathématique derrière pi.
Ils ne voyaient que les chiffres.

<!-- S78 -->
Une façon de mesurer l'information
contenue dans des données, c'est de se demander :
à quel point un programme peut-il être court
tout en les affichant ?

<!-- S79 -->
Cette longueur s'appelle
la complexité de Kolmogorov,
du nom de l'un des hommes qui l'ont décrite.

<!-- S80 -->
La plupart des données n'ont pas de programme court.
C'est encore le principe des tiroirs :
il n'y a pas assez de programmes courts
pour tout le monde.

<!-- S81 -->
Pour un million de chiffres aléatoires,
il n'existe très probablement aucun programme plus court.
Pi, si.

<!-- S82 -->
Alors pourquoi ne pas simplement trouver
le programme le plus court pour n'importe quel fichier ?
Parce qu'il a été démontré
qu'aucun algorithme ne peut le faire
pour tous les fichiers.

<!-- S83 -->
Chaque programme vous donne une limite supérieure.
Mais rien ne peut toujours vous dire
s'il en existe un plus court.
Vous ne savez jamais si vous avez atteint le plancher.

<!-- S84 -->
gzip a trouvé les répétitions dans les scripts,
et rien de plus.
Il voit des octets,
pas ce que les mots veulent dire.

<!-- S85 -->
Pour aller plus loin, un programme
doit mieux les prédire.
Et bien prédire un texte,
on n'est plus très loin de le comprendre.

<!-- S86 -->
Alors voici une question pour vous.
Si un programme pouvait compresser Wikipédia
mieux que n'importe quel autre programme,
diriez-vous qu'il la comprend ?
Laissez votre réponse dans les commentaires.
