# Internet Explorer 6 — Les bugs qui avaient des noms

<!-- S01 -->
Ceci est la deuxième partie.

Si tu n'as pas vu la première,
le lien est en dessous.

Tu auras quand même le résumé.

<!-- S02 -->
En 2001,
Microsoft a sorti
Internet Explorer 6,
et il est arrivé avec Windows XP.

En quelques années
il avait plus de quatre-vingt-dix pour cent
du marché des navigateurs.

<!-- S03 -->
Microsoft s'en est servi
pour transformer le navigateur
en plateforme applicative.

C'était une vraie idée.

Ce sont juste les développeurs web
qui l'ont payée.

<!-- S04 -->
C'était la première partie.

Mais j'ai laissé quelque chose de côté.

J'ai laissé de côté le passage
où les bugs avaient des noms.

<!-- S05 -->
Un bug de navigateur, normalement,
c'est un numéro dans un outil de suivi.

Issue 4172.

Personne ne s'en souvient.

Personne n'en parle au déjeuner.

<!-- S06 -->
Dans Internet Explorer 6
les bugs avaient des noms propres.

Et c'est, il se trouve,
ce qu'il y a de plus révélateur
sur toute cette époque.

<!-- S07 -->
Commençons par un doux.

Tu fais flotter une image à gauche
et tu mets un paragraphe à côté.

Le texte devrait se poser
juste contre l'image.

Au lieu de ça il se pose
trois pixels plus loin.

<!-- S08 -->
Pas quatre.

<!-- S08b -->
Pas deux.

<!-- S08c -->
Trois.

<!-- S08d -->
À chaque fois.

Ça avait un nom.

The Three Pixel Jog.

<!-- S09 -->
Maintenant fais flotter cette image à gauche
et donne-lui une marge gauche
de dix pixels.

Internet Explorer 6
lui en donne vingt.

Il double la marge,
mais seulement du côté
vers lequel tu as fait flotter.

<!-- S10 -->
The Double Margin Bug.

Et la correction admise
était de déclarer
un élément flottant en inline.

<!-- S11 -->
Ce qui n'a aucun sens.

Un flottant est un bloc.

L'appeler inline
ne veut strictement rien dire.

Ça marchait, alors on l'écrivait.

<!-- S12 -->
Le suivant est meilleur.

Tu charges une page,
et une partie du contenu
n'est tout simplement pas là.

Tu descends.

Tu remontes.

Et elle apparaît.

<!-- S13 -->
Rien n'a été chargé.

Rien n'a changé.

Elle était juste timide.

Et elle avait le bon nom.

The Peekaboo Bug.

<!-- S14 -->
Le remède était de dire
à l'élément manquant
que sa position était relative.

Personne n'a jamais pu expliquer
pourquoi ça le ramenait.

<!-- S15 -->
Puis il y a celui
où tu survoles un lien,
et le fond
du bloc en dessous
se fait couper au cordeau.

The Guillotine Bug.

<!-- S16 -->
Il y avait un bug où le texte
s'éloignait de là où tu l'avais mis.

Magic Creeping Text.

Il y en avait un où les bordures
sortaient au mauvais endroit,
de la mauvaise couleur,
ou pas du tout.

Border Chaos.

<!-- S17 -->
Mon préféré est plus discret.

Tu poses une rangée de blocs,
et des lettres du dernier
réapparaissent en dessous.

Pas toujours.

Pas de façon prévisible.

The Duplicate Character Bug.

<!-- S18 -->
Et ce qui décidait
si ça t'arrivait,
et combien de lettres
sortaient en double,
c'était le nombre de commentaires HTML
que tu avais laissés dans le code.

Des commentaires.

La seule chose du fichier
que le navigateur
est censé jeter.

<!-- S19 -->
Il y en a encore un,
et il est différent,
parce que celui-là,
on s'en servait exprès.

Si tu fixes une hauteur
et que le contenu est plus haut,
le bloc devrait déborder.

Internet Explorer 6
agrandissait le bloc à la place.

<!-- S20 -->
Ce qui est faux.

C'est aussi exactement
ce que fait une hauteur minimale.

Et Internet Explorer 6
n'avait pas de hauteur minimale.

Alors les développeurs ont cessé
de signaler ce bug
et se sont mis à compter dessus.

<!-- S21 -->
Arrête-toi et regarde cette liste.

The Three Pixel Jog.

The Double Margin Bug.

Peekaboo.

The Guillotine.

On ne donne pas de nom à un bug
qu'on ne rencontre qu'une fois.

<!-- S22 -->
Ceux-là avaient des noms
parce que tout le monde les rencontrait.

Et voici ce qui
rend la chose pire.

La plupart avaient
la même cause en dessous.

<!-- S23 -->
À l'intérieur d'Internet Explorer 6,
chaque élément avait
ou n'avait pas
quelque chose appelé layout.

<!-- S24 -->
Ça décidait si l'élément
fixait lui-même sa taille et sa position,
ou laissait ça à son parent.

Et tu ne pouvais pas le régler.

<!-- S25 -->
Il n'existait aucune propriété
qui s'appelle layout,
et aucun moyen de la demander.

Elle n'était dans aucune spécification.

C'était un drapeau interne
du moteur de rendu.

<!-- S26 -->
Mais tu pouvais le basculer
par accident.

Fixer une largeur le faisait.

Fixer une hauteur le faisait.

Faire flotter un élément le faisait.

Donc la moitié des corrections de cette vidéo,
c'étaient des gens qui basculaient un interrupteur
qu'ils ne voyaient pas.

<!-- S27 -->
D'où la recherche
du moyen le moins cher
de le basculer exprès.

L'un était de fixer une hauteur
à un pour cent.

<!-- S28 -->
Il fallait tenir tous les autres
navigateurs à l'écart de ça,
donc c'est parti dans un hack
qu'on verra dans une minute.

<!-- S29 -->
Et dans Internet Explorer 6
ça ne faisait aucun mal,
parce qu'une hauteur où ça ne rentre pas
est une hauteur qu'il dépasse de toute façon.

Le bug d'il y a deux minutes,
c'est ce qui rend la correction sûre.

<!-- S30 -->
Ça avait un nom.

The Holly Hack.

<!-- S31 -->
L'autre moyen
était une propriété Microsoft
appelée zoom, mise à un.

Zoom à un veut dire
ne pas zoomer.

<!-- S32 -->
Ça ne changeait rien de visible.

C'était bien le but.

C'était dans les feuilles de style
uniquement pour poser
un drapeau invisible
qui faisait disparaître les bugs.

<!-- S33 -->
Ce qui nous amène aux hacks,
et c'est avec les hacks
que ça devient étrange.

Pour réparer un navigateur,
il faut d'abord pouvoir parler
à celui-là seulement.

<!-- S34 -->
Et Internet Explorer 6
se comportait comme s'il y avait
un autre élément
au-dessus de l'élément html.

Aucun autre navigateur ne faisait ça.

Ce n'était pas documenté.

C'est simplement ainsi qu'il agissait.

<!-- S35 -->
Alors tu écrivais une règle
qui correspondait au fantôme,
et seul ce navigateur-là
pouvait la voir.

Étoile, espace, html.

<!-- S36 -->
Tous les autres navigateurs la regardaient,
ne trouvaient rien qui corresponde,
et passaient à la suite.

C'est le star hack,
et pendant des années il est resté
dans presque toutes les feuilles de style
du web.

<!-- S37 -->
Il y avait aussi
le underscore hack.

Tu mets un tiret bas
devant un nom de propriété.

<!-- S38 -->
Un navigateur conforme aux standards
jette la ligne
parce qu'elle est invalide.

Internet Explorer 6
ignore le tiret bas
et l'applique.

<!-- S39 -->
Tu cassais donc délibérément
ta propre feuille de style,
et la cassure
était l'instruction.

<!-- S40 -->
Et puis il y a celui
que Microsoft a construit exprès.

Tu pouvais écrire un commentaire
que seul Internet Explorer obéissait.

<!-- S41 -->
Pour tous les autres navigateurs
c'était un commentaire ordinaire,
ignoré comme on ignore un commentaire.

Pour Internet Explorer 6
c'était une porte
vers une deuxième version
de la page.

<!-- S42 -->
Ce qui veut dire que l'éditeur
a regardé la situation,
a convenu que ce navigateur
avait besoin de sa propre feuille de style,
et a livré une fonctionnalité
pour rendre ça plus facile.

<!-- S43 -->
Une partie des dégâts
n'avait besoin d'aucun bug.

Internet Explorer 6
avait deux modes.

Dans le moderne,
il suivait le standard.

<!-- S44 -->
Dans l'ancien,
la largeur d'un bloc
comprenait sa marge intérieure
et sa bordure,
ce qui est un nombre
complètement différent.

<!-- S45 -->
Le mode que tu obtenais
dépendait de la première ligne
du document.

Et la version de HTML
vers laquelle tout le monde allait
te disait de mettre
une déclaration XML tout en haut.

<!-- S46 -->
Cette ligne poussait
Internet Explorer 6
dans l'ancien mode.

Ce qui le cassait,
c'était de suivre le standard plus récent.

<!-- S47 -->
Ensuite il y a la transparence.

Internet Explorer 6 ne savait pas
afficher un PNG aux bords doux.

Là où l'image devait s'estomper,
il mettait du gris.

<!-- S48 -->
La réponse de Microsoft était un filtre
au nom de numéro de série.

Il marchait.

<!-- S49 -->
Mais il peignait en dehors
du processus de rendu
normal du navigateur,
donc les liens que tu posais dessus
cessaient souvent de fonctionner.

Tu réparais l'image
et tu cassais le lien.

<!-- S50 -->
Et estomper autre chose,
c'était un deuxième filtre,
avec sa propre syntaxe,
posé dans la feuille de style
juste à côté de la propriété ordinaire
que tous les autres navigateurs comprenaient.

<!-- S51 -->
Une partie de tout ça est plus ancienne
que les bugs eux-mêmes.

Avant tout cela,
les mises en page se construisaient
avec des tableaux imbriqués.

<!-- S52 -->
Et pour tenir un espace ouvert
tu utilisais une image transparente
d'un pixel de côté,
étirée à la taille
dont l'espace avait besoin.

Ça aussi avait un nom.

The spacer gif.

<!-- S53 -->
Le survol, c'en était un autre.

Dans Internet Explorer 6,
le survol marchait sur les liens.

Sur les liens seulement.

<!-- S54 -->
Donc un menu qui s'ouvrait
quand tu passais la souris
sur autre chose
avait besoin d'un petit programme
accroché à la feuille de style.

<!-- S55 -->
Pas un script dans la page.

Un fichier séparé,
référencé depuis le CSS,
contenant du code dont le travail
était d'apprendre au navigateur
un seul sélecteur.

Ce fichier, les gens se le sont passé
pendant des années.

<!-- S56 -->
La première partie mentionnait
qu'on pouvait mettre du JavaScript
dans une feuille de style.

Ce qu'elle ne mentionnait pas,
c'est la fréquence à laquelle ce JavaScript tournait.

<!-- S57 -->
À chaque mouvement de souris.

À chaque touche.

À chaque défilement.

Encore et encore,
pour calculer une largeur.

<!-- S58 -->
Et le navigateur avait des plafonds
que personne d'autre n'avait.

Une feuille de style cessait de s'appliquer
quelque part au-delà de
quatre mille règles.

Tout ce qui venait après
la trente et unième feuille de style
d'une page était ignoré.

<!-- S59 -->
Ce qui ressemble à un nombre
qu'on n'atteint jamais,
jusqu'à ce que ton site soit assez gros
pour que quelqu'un doive écrire
une étape de build dont le seul travail
est de fusionner les feuilles de style
avant que le navigateur les voie.

<!-- S60 -->
Et une partie de tout ça n'était
pas du tout cosmétique.

Internet Explorer 6
comptait ses objets de page
et ses objets de script
de deux façons différentes,
et aucun des deux côtés
ne voyait la boucle entière.

<!-- S61 -->
Donc si un script pointait
vers une partie de la page,
et que cette partie de la page
pointait vers le script,
aucun des deux n'était jamais libéré.

Laisse cette fenêtre ouverte assez longtemps
et le navigateur mangeait la machine.

<!-- S62 -->
Mais le meilleur
n'est pas du tout un bug de mise en page.

Tu écris une balise input.

Tu lui donnes un type.

Et tu oublies le signe égal.

<!-- S63 -->
C'est un attribut mal formé.

Tous les analyseurs jamais écrits
ont une réponse à ça.

Ignore-le.

Devine ce qui était voulu.

Continue.

<!-- S64 -->
Internet Explorer plantait.

À l'intérieur, il voulait savoir
si le champ était caché,
alors il comparait ce que tu avais tapé
avec le mot hidden.

Tu n'avais rien tapé.

<!-- S65 -->
Alors il est allé chercher
ce que tu n'avais pas tapé
à l'adresse zéro.

Ce qui serait
un plantage de navigateur ordinaire,
sauf que le code qui faisait ça
n'était pas dans le navigateur.

<!-- S66 -->
Il était dans une bibliothèque système partagée.

Donc ces trois mots
faisaient aussi tomber le client mail,
et le volet d'aperçu
du gestionnaire de fichiers.

<!-- S67 -->
Une fenêtre listant des fichiers
sur ta propre machine,
fermée par une page web.

C'est l'argument de la première partie
qui arrive sous forme de rapport de plantage.

Le navigateur n'était pas un programme
qui tournait sur le système.

Il faisait partie du système.

<!-- S68 -->
Et tu ne pouvais pas simplement
tester la correction ailleurs.

Internet Explorer était soudé
au système d'exploitation,
donc un ordinateur
faisait tourner exactement une version.

<!-- S69 -->
C'est pourquoi un poste de front-end
en 2006
venait avec une étagère
de machines de rechange.

<!-- S70 -->
Et plus tard avec un dossier
de machines virtuelles,
chacune portant un système
d'exploitation entier
pour qu'une seule page
puisse être ouverte dedans.

<!-- S71 -->
Et puis quelqu'un a fait
la chose évidente.

Si tu peux apprendre au navigateur
une fonctionnalité manquante,
tu peux les lui apprendre toutes.

<!-- S72 -->
Un développeur nommé Dean Edwards
a écrit une bibliothèque
dont le seul but
était de faire qu'Internet Explorer 6
se comporte comme une version
plus tardive de lui-même.

Les gens ont déployé ça.

En production.

<!-- S73 -->
Et c'est là que ça cesse
d'être drôle.

Pendant presque une décennie,
une part sérieuse
du travail front-end mondial
est partie dans les erreurs d'un navigateur.

Pas des fonctionnalités.

Pas des produits.

De la compensation.

<!-- S74 -->
Et ça a duré à cause de
ce dont parlait la première partie.

Des entreprises avaient bâti dessus
de vraies applications,
du genre qui ne tournait que là,
et ces applications
devaient encore marcher le lundi.

<!-- S75 -->
Donc le navigateur dont tout le monde
voulait se débarrasser
était celui que personne
n'avait le droit d'enlever.

<!-- S76 -->
En 2010,
Google a annoncé que ses propres
applications cesseraient d'y fonctionner.

Et un studio de design à Denver
a décidé que ça méritait des funérailles.

<!-- S77 -->
De vraies funérailles.

Un cercueil.

Un éloge funèbre.

Entre quatre-vingts et cent personnes
sont venues voir enterrer
un navigateur.

Ils en avaient prévu trente.

<!-- S78 -->
Et Microsoft a envoyé des fleurs.

La carte disait :
merci pour les bons moments,
Internet Explorer 6.

<!-- S79 -->
Un an plus tard, jour pour jour,
Microsoft a lancé un site.

Il suivait quelle part du monde
utilisait encore
Internet Explorer 6,
pays par pays.

<!-- S80 -->
À ce moment-là
c'était encore douze pour cent.

Le but était de descendre
sous un.

L'entreprise qui avait construit le navigateur
tenait un compte à rebours public
jusqu'à la mort de son propre produit.

<!-- S81 -->
Alors pourquoi les bugs avaient-ils des noms ?

Parce qu'on nomme les choses
qu'on ne peut pas contourner.

<!-- S82 -->
Personne ne nomme le temps qu'il fait
dans un pays
qu'il ne fait que traverser.

On le nomme là où on habite.

Et pendant une dizaine d'années,
c'est là que le web habitait.

<!-- S83 -->
Mais sortir Internet Explorer 6
du web, c'est une autre histoire.

Et c'est là qu'on va ensuite.

Si tu la veux,
il y a un bouton d'abonnement,
et la première partie est en lien dessous.
