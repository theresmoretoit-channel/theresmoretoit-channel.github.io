# Comment ARM a-t-il conquis l'informatique ?

<!-- S01 -->
En 1985, des ingénieurs britanniques
ont allumé un tout nouveau processeur
pour la toute première fois.

<!-- S02 -->
Il a fonctionné.
Ce qui était déjà un petit miracle.

<!-- S03 -->
Mais ils ont alors remarqué un truc bizarre.
L'alimentation de la puce
n'était pas branchée.

<!-- S04 -->
Et pourtant, elle tournait.

<!-- S05 -->
Elle se contentait de minuscules courants
qui s'infiltraient par ses broches d'entrée,
provenant des signaux des puces voisines.

<!-- S06 -->
Quand ils ont fait une vraie mesure,
le processeur consommait
environ un dixième de watt.

<!-- S07 -->
Personne n'avait visé ça.
Les ingénieurs voulaient juste une puce
bon marché à fabriquer.

<!-- S08 -->
Cette puce, c'était le premier processeur ARM.

<!-- S09 -->
Quarante ans plus tard, ses descendants
sont dans presque tous les smartphones.
Dans les ordinateurs d'Apple.
Dans certains des plus grands datacenters
du monde.

<!-- S10 -->
Des centaines de milliards de puces.

<!-- S11 -->
Alors comment un processeur
d'une entreprise britannique d'ordinateurs familiaux
a-t-il conquis l'informatique ?

<!-- S12 -->
La réponse, ce n'est pas simplement
qu'il consommait très peu.
Ça, c'était presque un accident.

<!-- S12b -->
Au fait, si tu aimes ce genre de
vidéos, pense à t'abonner.

Ça aide vraiment la chaîne.

<!-- S13 -->
Pour comprendre ce qui s'est vraiment passé,
il faut remonter à 1983.

<!-- S14 -->
L'entreprise s'appelait Acorn Computers.
Son BBC Micro équipait les salles de classe
de toute la Grande-Bretagne.

<!-- S15 -->
Le BBC Micro tournait sur une puce
plus ancienne, 8 bits : le 6502.
Pour sa machine suivante,
Acorn avait besoin de bien plus rapide.

<!-- S16 -->
L'équipe a donc testé
les nouveaux processeurs du marché.
Aucun ne faisait ce qu'Acorn voulait.

<!-- S17 -->
Ils étaient compliqués,
et aucun ne correspondait vraiment
à ce qu'Acorn voulait construire.

<!-- S18 -->
Puis deux ingénieurs d'Acorn,
Sophie Wilson et Steve Furber,
sont allés en Arizona,
dans une boîte fondée par l'un
des concepteurs d'origine du 6502.

<!-- S19 -->
Ils s'attendaient à un grand fabricant de puces.
À la place, ils ont trouvé une poignée de gens
qui travaillaient dans une maison de banlieue.

<!-- S20 -->
Et ils sont rentrés
avec une conclusion toute simple.
S'ils peuvent concevoir un processeur...
nous aussi.

<!-- S22 -->
À l'époque, les jeux d'instructions
devenaient de plus en plus élaborés.

<!-- S23 -->
Une seule instruction pouvait aller chercher
un nombre en mémoire,
faire un calcul avec,
et réécrire le résultat.

<!-- S24 -->
Pratique pour le programmeur.
Mais chaque instruction de ce genre
rend la puce plus difficile à construire.

<!-- S25 -->
Il faut plus de circuits logiques
rien que pour comprendre ce que chacune signifie.
Plus de transistors.
Plus de temps de conception.

<!-- S26 -->
Des chercheurs de Berkeley et de Stanford
s'étaient posé une question radicale.

<!-- S27 -->
Et si un processeur
n'avait que des instructions simples,
et que le compilateur faisait le reste ?

<!-- S28 -->
Ils ont appelé ça RISC.
Reduced Instruction Set Computer.

<!-- S29 -->
Sophie Wilson a conçu
les instructions d'ARM dans cet esprit.

<!-- S30 -->
Les calculs ne se font
que sur les registres de la puce,
de petites cases rapides dans le processeur.
La mémoire a ses propres instructions.

<!-- S31 -->
Additionner un nombre pris en mémoire,
ça devient donc trois étapes.
Le charger.
L'additionner.
Le ranger.

<!-- S32 -->
On appelle ça une architecture load-store.

<!-- S33 -->
Plus d'étapes pour le programme.
Mais chaque étape est régulière,
prévisible,
et facile à décoder.

<!-- S34 -->
Et ARM avait plein de registres
pour travailler.
Seize, chacun de 32 bits.
Le 6502 en avait trois petits.

<!-- S35 -->
Le résultat, c'était l'ARM1.

<!-- S36 -->
Il comptait environ
25 000 transistors.

<!-- S37 -->
Le 286 d'Intel, sorti quelques années plus tôt,
en avait environ 134 000.

<!-- S38 -->
Moins de transistors, ça voulait dire une puce plus petite.
Une puce moins chère.

<!-- S39 -->
Et, presque comme un effet secondaire,
une puce qui ne consommait quasiment rien.

<!-- S40 -->
Voilà d'où venait
ce dixième de watt.
Acorn voulait un boîtier plastique bon marché,
ce qui imposait de rester sous un watt.
Alors ils ont conçu la puce avec prudence...
et sont tombés dix fois en dessous.

<!-- S41 -->
En 1987, une version plus rapide de l'ARM
a équipé le nouvel ordinateur d'Acorn,
l'Archimedes.

<!-- S42 -->
C'était l'un des ordinateurs personnels
les plus rapides de son époque.

<!-- S43 -->
Et ça n'a presque rien changé.

<!-- S44 -->
Le monde achetait des PC compatibles IBM
avec des processeurs Intel.
C'est là qu'étaient les logiciels.
C'est ça qu'achetaient les entreprises.

<!-- S45 -->
L'Archimedes est resté
surtout dans les écoles britanniques.

<!-- S46 -->
Et Acorn elle-même était en difficulté.
Elle avait déjà dû être sauvée
par Olivetti, dès 1985.

<!-- S48 -->
Puis l'aide est venue d'Apple.
Apple construisait un ordinateur de poche
appelé le Newton.

<!-- S49 -->
Il lui fallait un processeur
rapide, bon marché,
et capable de tourner sur piles.

<!-- S50 -->
L'ARM convenait parfaitement.
Mais Apple ne voulait pas dépendre
d'une puce appartenant
à un fabricant d'ordinateurs concurrent.

<!-- S51 -->
Alors en 1990, l'équipe ARM
a été séparée d'Acorn
pour devenir une entreprise à part entière.

<!-- S52 -->
Acorn, Apple
et le fabricant de puces VLSI
la possédaient ensemble.

<!-- S53 -->
Douze ingénieurs.
Une vieille grange près de Cambridge.

<!-- S54 -->
Et un modèle économique
qui s'est révélé être le vrai secret de sa réussite.

<!-- S55 -->
Intel concevait ses processeurs,
les fabriquait dans ses propres usines
et les vendait.

<!-- S56 -->
ARM, elle, n'allait rien fabriquer du tout.
Elle allait vendre le design.

<!-- S57 -->
N'importe quelle entreprise pouvait en acheter la licence,
intégrer le cœur ARM dans sa propre puce,
et payer une petite redevance
sur chaque puce vendue.

<!-- S58 -->
C'était important,
parce qu'une puce n'a pas besoin d'être
seulement un processeur.
Autour du cœur ARM,
tu peux mettre une radio,
un circuit graphique,
un processeur pour l'appareil photo.

<!-- S59 -->
Une seule puce,
conçue par celui qui en a besoin,
avec ARM au centre.

<!-- S60 -->
ARM n'avait pas besoin de battre Intel
sur les ordinateurs personnels.
Il pouvait se retrouver dans n'importe quoi.

<!-- S61 -->
Et dans les années 1990,
« n'importe quoi », c'était de plus en plus
les téléphones portables.

<!-- S62 -->
Un ordinateur de bureau peut consommer
cent watts et avoir un gros ventilateur.
Un téléphone tourne sur une batterie,
dans ta poche.

<!-- S63 -->
À la fin de la décennie,
on trouvait des cœurs ARM
dans certains des téléphones les plus vendus,
chez Nokia et d'autres.

<!-- S64 -->
Puis est arrivé l'iPod.
Puis le smartphone.

<!-- S65 -->
Des milliards de gens se sont mis à porter
un ordinateur qui devait tenir
toute la journée sur une batterie.

<!-- S66 -->
Et le processeur conçu
parce qu'il était bon marché
s'est révélé être exactement
ce dont ce monde avait besoin.

<!-- S67 -->
Voilà donc notre réponse, non ?
ARM est simple,
simple veut dire efficace,
et l'efficacité l'emporte.

<!-- S68 -->
Pas tout à fait.

<!-- S69 -->
Regarde à l'intérieur d'un cœur ARM haut de gamme moderne.

<!-- S70 -->
D'énormes caches.
Plusieurs instructions exécutées à la fois.
La prédiction de branchement,
qui devine où le programme va aller
avant qu'il n'y arrive.

<!-- S71 -->
L'exécution dans le désordre,
qui exécute les instructions
dans l'ordre le plus rapide.

<!-- S72 -->
Des milliards de transistors sur la puce.
Rien là-dedans n'est simple.

<!-- S73 -->
Alors, où est passée la simplicité ?

<!-- S74 -->
L'astuce, c'est qu'un processeur,
ce sont en réalité deux choses différentes.

<!-- S75 -->
Le jeu d'instructions, c'est la langue
que parle le logiciel.
Quelles instructions existent,
et ce qu'elles veulent dire.

<!-- S76 -->
La microarchitecture, c'est la machine
qui les exécute réellement.

<!-- S77 -->
La langue peut rester simple,
pendant que la machine en dessous
devient extrêmement complexe.

<!-- S78 -->
Et la même chose s'est produite
de l'autre côté.

<!-- S79 -->
Les instructions x86 d'Intel
sont réputées pour leur complexité.

<!-- S80 -->
Mais depuis le milieu des années 1990,
les processeurs d'Intel et d'AMD
les décomposent en interne
en petites opérations simples.

<!-- S81 -->
Puis ils les exécutent sur un moteur
qui ressemble beaucoup à celui
d'un cœur ARM moderne.

<!-- S82 -->
Sous les étiquettes,
les deux ont fini par se ressembler étonnamment.

<!-- S83 -->
Les instructions plus épurées d'ARM restent un atout.
Elles sont plus faciles à décoder,
ce qui peut économiser un peu d'énergie.

<!-- S84 -->
Mais ce n'est pas un avantage magique
que le x86 ne pourrait jamais égaler.

<!-- S85 -->
Donc ARM ne s'est pas imposé
parce qu'il était simple.
Et il n'a pas été conçu pour consommer peu.

<!-- S86 -->
Il a gagné parce que trois choses se sont alignées.
Un design efficace.
Un modèle économique
qui permettait à n'importe qui de concevoir ses puces sur ARM.
Et un monde qui avait soudain besoin
de milliards d'ordinateurs sur batterie.

<!-- S87 -->
Et puis, en 2020,
l'histoire est revenue à Apple.

<!-- S88 -->
Apple avait vendu sa part dans ARM
des années plus tôt,
quand elle avait cruellement besoin d'argent.

<!-- S89 -->
Cette fois, elle a mis ses propres puces ARM
dans le Mac.

<!-- S90 -->
Le même genre de cœurs que dans l'iPhone,
en version musclée pour un ordinateur.
Des cœurs rapides, des cœurs économes,
le graphisme et bien plus,
dans une seule puce.

<!-- S91 -->
Elles étaient plus rapides
que les puces Intel qu'elles remplaçaient,
et les portables tenaient bien plus longtemps
sur une charge.

<!-- S92 -->
ARM n'était plus
seulement le processeur des téléphones.

<!-- S93 -->
Et ARM ne s'est pas arrêté là.
Il est aussi entré dans les datacenters,
où chaque watt coûte de l'argent.
Amazon conçoit aujourd'hui
ses propres puces ARM pour serveurs.

<!-- S95 -->
La première puce ARM comptait environ
25 000 transistors.
Celles d'aujourd'hui en ont des milliards.

<!-- S96 -->
Presque tout dans leur
fonctionnement interne a changé.

<!-- S98 -->
Une petite équipe voulait
un processeur qu'elle puisse vraiment construire.

<!-- S99 -->
Ils ne l'ont pas construit pour les téléphones,
ni pour Apple,
ni pour battre Intel.

<!-- S100 -->
Et au bout du compte,
la chose la plus importante qu'ils ont créée,
ce n'était pas la puce.

<!-- S101 -->
C'était une base simple
sur laquelle tous les autres pouvaient construire.
