<!-- S01 -->
Voici un ZX Spectrum en train de charger un programme.

<!-- S02 -->
Et voici le même programme,
sur le même ordinateur,
avec le même genre de cassette.

<!-- S03 -->
Il a fini en deux fois moins de temps.
Rien n'a changé dans le matériel.
Pas de bande plus rapide, pas de magnéto plus rapide.

<!-- S04 -->
La seule chose qui a changé,
c'est la façon dont l'ordinateur écoutait.

<!-- S05 -->
Alors comment les ordinateurs 8 bits
ont-ils appris à charger les jeux plus vite ?
Et si c'était si simple,
pourquoi ne pas l'avoir fait dès le début ?

<!-- S06 -->
Dans une vidéo précédente,
on a vu comment le Spectrum stocke les bits
sous forme d'impulsions sur la bande.

<!-- S07 -->
Une paire d'impulsions courtes, c'est un zéro.
Une paire deux fois plus longue, c'est un un.

<!-- S08 -->
Ça donne environ mille quatre cents bits
par seconde.
Un jeu qui remplit les 48K de mémoire
met environ cinq minutes à charger.

<!-- S09 -->
Maintenant, rends chaque impulsion deux fois plus courte.

<!-- S10 -->
L'ordinateur distingue toujours le court du long.
Mais deux fois plus de bits
passent devant la tête de lecture chaque seconde.

<!-- S11 -->
C'est tout le secret d'un chargeur turbo.
Et ce n'est pas qu'une expérience de pensée.

<!-- S12 -->
En 1984, le jeu Skool Daze
chargeait ses données au double
de la vitesse normale du Spectrum.

<!-- S13 -->
Alors pourquoi le Spectrum
ne chargeait-il pas aussi vite tout seul ?

<!-- S14 -->
Le chargeur intégré est stocké dans la ROM,
la puce mémoire sur laquelle l'ordinateur démarre.
Il ne mesure pas une impulsion en secondes.

<!-- S15 -->
Il compte.
Après chaque front du signal,
il attend un instant,
puis compte combien de temps passe jusqu'au suivant.

<!-- S16 -->
Un seul nombre dans la ROM
décide où s'arrête le zéro
et où commence le un.

<!-- S17 -->
Et ce nombre laisse beaucoup de marge.
Un zéro peut s'allonger
de plus de quarante pour cent
et être quand même lu comme un zéro.

<!-- S18 -->
C'est grâce à cette marge qu'une bande usée
sur un magnéto bon marché
se charge quand même.

<!-- S19 -->
Et la limite, ce n'était pas l'ordinateur.
Le Spectrum vérifie le signal de la bande
environ soixante mille fois par seconde.

<!-- S20 -->
La limite, c'était la cassette.
Des impulsions plus courtes, ce sont des sons plus aigus.
À double vitesse, un zéro
passe de deux kilohertz à quatre.

<!-- S21 -->
Et les aigus, c'est justement ce qu'
un magnéto bon marché,
ou une tête un peu mal alignée,
perd en premier.

<!-- S22 -->
En 1986, un magazine sur le Spectrum estimait
que la plupart des gens pouvaient atteindre
au moins le double de la vitesse normale.
Jusqu'où aller au-delà,
ça dépendait du magnéto.

<!-- S23 -->
Mais le turbo avait un problème plus étrange.

<!-- S24 -->
Si l'ordinateur ne connaît
que le format lent,
comment charge-t-il le programme
qui lui apprend le format rapide ?

<!-- S25 -->
La réponse est au début de la bande.
La première partie est enregistrée
dans le format ordinaire, le lent.

<!-- S26 -->
Elle est courte,
et la ROM la charge comme n'importe quel autre programme.

<!-- S27 -->
Puis ce petit programme prend le relais.
Dans le cas le plus simple,
c'est une copie de la routine de chargement de la ROM,
avec quelques nombres modifiés.

<!-- S28 -->
Dans Skool Daze,
les modifications sont à trois endroits.
Une attente plus courte, une nouvelle valeur de départ,
un nouveau seuil.

<!-- S29 -->
Donc la ROM charge le programme
qui fait le travail de la ROM, en plus rapide.

<!-- S30 -->
C'est un peu comme télécharger
un téléchargeur plus rapide.
L'étape lente te donne l'outil.
L'outil fait le reste.

<!-- S31 -->
Les jeux du commerce ont repris la même idée.
Un exemple célèbre, c'était Speedlock,
utilisé pour la première fois par Ocean en 1984.

<!-- S32 -->
L'un de ses auteurs a dit l'avoir écrit
parce qu'il en avait assez
de la lenteur du chargeur standard.

<!-- S33 -->
Mais voilà la surprise.
Speedlock n'était qu'environ une fois et demie
plus rapide.

<!-- S34 -->
Le premier jour
de Daley Thompson's Decathlon
prenait trois minutes vingt,
alors que les mêmes données à vitesse normale
auraient pris quatre minutes quarante-sept.

<!-- S35 -->
Les versions suivantes n'étaient plus rapides
que d'un cinquième environ par rapport à la ROM.
Parce qu'aller vite n'était pas leur seul rôle.

<!-- S36 -->
Dès 1983, des programmes de copie
savaient lire l'en-tête d'un jeu
et copier tout le jeu sur une autre bande.

<!-- S37 -->
Un format maison
ne laissait rien à lire à ces programmes.

<!-- S38 -->
Les premiers Speedlock découpaient même leur tonalité d'amorce
en courtes salves,
pour que le chargeur de la ROM
ne la reconnaisse pas du tout.

<!-- S39 -->
Et ça s'entendait.
Une cassette Speedlock se chargeait au son de clics,
avec des rayures saccadées autour de l'écran.

<!-- S40 -->
Ça n'empêchait personne de copier
une cassette d'une platine à l'autre.
Mais ça donnait aux éditeurs
une raison d'écrire leurs propres chargeurs.

<!-- S41 -->
Sur le Commodore 64,
la raison de changer était bien plus forte.

<!-- S42 -->
Sa routine intégrée
enregistrait tout deux fois,
comme copie de sécurité.
Un jeu de quarante kilo-octets mettait
environ douze minutes et demie.

<!-- S43 -->
Et là, le magnéto
ne faisait presque rien d'intelligent.
Il transformait juste le son
en impulsions nettes, tout ou rien.

<!-- S44 -->
L'ordinateur chronométrait lui-même chaque impulsion,
par logiciel.

<!-- S45 -->
Donc un chargeur plus rapide,
c'était juste un autre programme.

<!-- S46 -->
En 1985, le magazine Compute!
en a testé un qui s'appelait TurboTape.

<!-- S47 -->
Une fois le programme trouvé sur la bande,
il chargeait douze kilo-octets
en vingt-huit secondes.

<!-- S48 -->
Le lecteur de disquettes de Commodore
mettait trente-quatre secondes.

<!-- S49 -->
Une cassette
qui bat une disquette.

<!-- S50 -->
Et comme c'était l'ordinateur
qui écoutait tout lui-même,
il pouvait faire autre chose entre-temps.

<!-- S51 -->
Des chargeurs comme Freeload
donnaient la priorité à la lecture de la bande.
Le temps processeur qui restait
allait à la musique, à un défilement fluide,
et même à de petits jeux.

<!-- S52 -->
Avec Invade-a-Load de Mastertronic,
tu jouais à un clone de Space Invaders
pendant que le vrai jeu chargeait.

<!-- S53 -->
Les ordinateurs 8 bits d'Atari,
c'était une autre histoire.

<!-- S54 -->
Là, c'est le magnéto qui écoutait.
Il contenait deux filtres,
un pour chaque tonalité,
et un circuit qui fournissait à l'ordinateur
des uns et des zéros tout prêts.

<!-- S55 -->
La norme, c'était six cents bits par seconde,
et les filtres limitaient
jusqu'où on pouvait accélérer.

<!-- S56 -->
Un logiciel astucieux pouvait pousser ça
un peu, au mieux jusqu'à environ mille deux cents.
Mais pour aller beaucoup plus vite,
il fallait ouvrir le magnéto.

<!-- S57 -->
Et en Tchécoslovaquie, c'est ce que les gens ont fait.

<!-- S58 -->
Là-bas, un lecteur de disquettes
coûtait deux à trois fois
plus cher que l'ordinateur lui-même.
Alors la plupart des possesseurs d'Atari restaient à la cassette.

<!-- S59 -->
En 1987, un étudiant de Prague
du club Atari local
a conçu Turbo 2000.

<!-- S60 -->
Il ajoutait un nouveau chemin pour le signal.
Un fil dans le magnéto prenait le son
directement à la sortie de son amplificateur,
avant les filtres,
le faisait passer par une petite puce,
et l'envoyait sur la ligne vers l'ordinateur.

<!-- S61 -->
Un interrupteur, commandé par l'ordinateur,
choisissait entre l'ancien chemin et le nouveau.

<!-- S62 -->
Désormais, l'ordinateur chronométrait lui-même les impulsions.
Environ deux mille trois cents bits
par seconde.
Presque quatre fois plus vite.

<!-- S63 -->
Le turbo n'était pas un format universel unique.

<!-- S64 -->
Parfois, on changeait de programme.
Parfois, il fallait modifier la machine.

<!-- S65 -->
Et la vitesse avait un prix.

<!-- S66 -->
Compute! prévenait qu'un enregistrement TurboTape
refusait parfois de charger
sur un autre magnéto,
dont la tête était alignée un peu différemment.

<!-- S67 -->
La sauvegarde standard, d'après le magazine,
était bien plus lente,
mais extrêmement fiable.

<!-- S68 -->
Tout enregistrer deux fois,
ce n'était pas de la paresse de la part de Commodore.
C'était le prix d'un chargement fiable.

<!-- S69 -->
Mais un autre chargeur
pouvait aussi faire quelque chose d'inattendu.
Il pouvait lire une bande
que le chargeur intégré refusait.

<!-- S70 -->
Sur le Sharp MZ-800,
un ordinateur qui a fini par arriver
en Tchécoslovaquie à la fin des années 1980,
les utilisateurs connaissaient un programme : Turbo Copy.

<!-- S71 -->
Un jeu refusait de charger,
avec une erreur de somme de contrôle.
Les utilisateurs ont découvert que Turbo Copy
arrivait souvent à le charger quand même.

<!-- S72 -->
Ensuite, tu le sauvegardais à vitesse normale
sur une cassette neuve,
et l'ordinateur
le rechargeait normalement.
On aurait dit que tu réparais un jeu cassé.

<!-- S73 -->
Alors comment un chargeur pouvait-il lire
ce que l'autre n'arrivait pas à lire ?

<!-- S74 -->
La ROM du Sharp enregistrait chaque bloc deux fois,
à environ mille deux cents bits par seconde.

<!-- S75 -->
Et elle ne mesurait jamais une impulsion.
Après le début de chaque impulsion,
elle attendait un délai fixe,
et regardait une seule fois.

<!-- S76 -->
Toujours haut ?

<!-- S76b -->
C'est un un.

<!-- S76c -->
Déjà bas ?

<!-- S76d -->
C'est un zéro.

<!-- S77 -->
Un chronomètre, réglé à l'avance.

<!-- S78 -->
Sur une vieille bande, ou un autre magnéto,
les impulsions revenaient un peu plus arrondies.
Et ce coup d'œil unique
pouvait tomber sur le mauvais niveau.

<!-- S79 -->
Un seul mauvais bit gâche la somme de contrôle.
Si les deux copies échouent,
le chargement échoue.

<!-- S80 -->
Turbo Copy écoutait autrement.
Il chronométrait chaque impulsion
avec la puce timer de l'ordinateur.

<!-- S81 -->
Et avant chaque bloc,
il écoutait la tonalité d'amorce,
et réglait son seuil
d'après les impulsions qu'il entendait vraiment.

<!-- S82 -->
Son chronomètre était réglé
sur la bande qu'il avait devant lui.

<!-- S83 -->
Et la réparation n'était pas une copie du son.
Turbo Copy gardait les octets,
et écrivait un signal tout neuf,
au timing impeccable.

<!-- S84 -->
Les données n'avaient pas été perdues.
La façon habituelle de les lire
n'était tout simplement pas assez bonne.

<!-- S84b -->
Turbo Copy pouvait aussi sauvegarder le jeu en turbo,
à deux ou trois fois la vitesse normale,
précédé de son propre petit chargeur.

<!-- S85 -->
Et c'est ça que toutes ces astuces
ont en commun.

<!-- S86 -->
La cassette est restée la même.
Ce qui a changé, c'est la façon de la lire.

<!-- S87 -->
Aujourd'hui, on veut que les jeux chargent instantanément.
Dans les années 1980, le chargement faisait partie du jeu.
Tu écoutais la bande.
Tu regardais les rayures.
Tu attendais.

<!-- S88 -->
Et parfois, avec un autre chargeur,
la même cassette se comportait
comme une machine complètement différente.

<!-- S89 -->
L'ordinateur n'avait pas besoin d'une bande plus rapide.
Il lui fallait une meilleure façon d'écouter.

<!-- S90 -->
Alors, j'ai une question pour toi.
Tu utilisais des chargeurs turbo à l'époque ?
Quels souvenirs tu en gardes ?
Est-ce qu'ils échouaient plus souvent ?
Dis-le-moi dans les commentaires.

<!-- S91 -->
Et pour finir, toute la bande turbo,
du début à la fin.
D'abord la partie à vitesse normale,
puis le turbo.
Pour un programme aussi petit,
le turbo n'est pas rentable.
Le chargeur prend plus de temps
qu'il n'en fait gagner.
Pour un jeu entier, ça pouvait faire gagner des minutes.
