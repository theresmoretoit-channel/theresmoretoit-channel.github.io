<!-- S01 -->
Imagine que tu allumes un PC sous Windows
et que tu ne trouves ni barre des tâches, ni bouton Démarrer,
ni une seule icône sur le bureau.

<!-- S02 -->
À la place, il y a une fine barre en haut,
un menu qui s'ouvre partout où tu cliques
et quatre bureaux virtuels côte à côte.

<!-- S03 -->
On dirait Linux.
Pourtant, tes programmes, tes pilotes et tes fichiers
sont exactement là où tu les as laissés.
C'est toujours Windows.

<!-- S04 -->
Seul le bureau a changé.
Et l'interrupteur qui le change
est un simple réglage.

<!-- S05 -->
Windows le garde dans le registre,
dans une valeur appelée Shell.
Sur presque tous les PC sous Windows,
on y lit explorer.exe.

<!-- S06 -->
Écris là le nom d'un autre programme,
déconnecte-toi puis reconnecte-toi,
et Windows lance ce programme à la place.
Ce qu'il dessine devient ton bureau.

<!-- S07 -->
Et ce n'est pas une astuce découverte l'an dernier.
En 1990, Windows 3.0 avait déjà le même interrupteur
dans un simple fichier texte appelé system.ini.
Une ligne : shell=progman.exe.

<!-- S08 -->
Si on changeait ce nom,
le Gestionnaire de programmes, la fenêtre pleine de groupes d'icônes,
n'apparaissait jamais.

<!-- S09 -->
La question n'est donc pas de savoir si Windows
peut avoir un autre bureau.
Il l'a toujours pu.
La question, c'est pourquoi presque personne n'en a jamais vu.

<!-- S10 -->
Commençons par ce que cette ligne désigne vraiment.
La barre des tâches, les icônes du bureau,
la petite zone de notification près de l'horloge :
tout ça, c'est un seul programme, explorer.exe.

<!-- S11 -->
Oui, le même explorer.exe
que tu ouvres pour parcourir tes fichiers.
Il fait deux boulots,
et la plupart des gens n'en remarquent qu'un.

<!-- S12 -->
Ce deuxième boulot a un nom : le shell.
C'est la couche que tu touches.
En dessous, il y a le noyau, les pilotes
et les services qui font tourner Windows.

<!-- S13 -->
Aucun d'eux n'a besoin d'une barre des tâches.
Arrête explorer.exe dans le Gestionnaire des tâches,
et la barre des tâches et les icônes disparaissent...
mais le Bloc-notes, ton navigateur
et toutes les autres fenêtres continuent de fonctionner.

<!-- S14 -->
Relance-le, et le bureau revient.
C'est à peu près la preuve la plus claire qui soit
que le bureau n'est qu'un programme comme un autre.

<!-- S14b -->
Si tu as déjà changé de launcher
sur un téléphone Android,
tu connais déjà le principe.
Android en fait un réglage normal.
Windows a aussi le mécanisme,
mais n'a jamais donné aux utilisateurs ordinaires
un simple bouton pour ça.

<!-- S15 -->
Trois termes se mélangent ici.
Le shell, c'est ce d'où tu lances les choses :
la barre des tâches, les menus, le bureau.
Un gestionnaire de fenêtres contrôle comment les fenêtres
sont placées, empilées et reçoivent le focus.
Un environnement de bureau
rassemble le tout en un ensemble cohérent.

<!-- S16 -->
Sous Linux, ces pièces peuvent se combiner
de bien des manières.
Sous Windows, remplacer le shell
ne remplace pas la gestion des fenêtres du système,
ni la façon dont les applications dessinent les cadres de leurs fenêtres.

<!-- S17 -->
Ça n'a pas empêché les gens d'essayer.
Au début des années 90, on pouvait entrer dans un magasin
et acheter un remplaçant du Gestionnaire de programmes.

<!-- S18 -->
Norton Desktop for Windows
te donnait son propre bureau,
ses propres outils de gestion de fichiers et son propre lanceur,
par-dessus le même Windows.

<!-- S19 -->
Certains fabricants d'ordinateurs le remplaçaient
avant même que le client allume sa machine.
Le Navigator de Packard Bell accueillait les acheteurs
avec une maison qu'on pouvait visiter pièce par pièce.

<!-- S20 -->
Puis Windows 95 a confié ce travail à explorer.exe,
et la ligne de system.ini
est simplement devenue explorer.exe.
L'interrupteur est resté exactement à sa place.

<!-- S21 -->
À la fin des années 90,
toute une communauté s'est formée autour de cet interrupteur.
Le projet le plus connu était LiteStep.

<!-- S22 -->
Il empruntait son look à AfterStep,
un gestionnaire de fenêtres Unix inspiré de NeXTSTEP,
de l'entreprise fondée par Steve Jobs après son départ d'Apple.

<!-- S23 -->
LiteStep n'avait pas de menu Démarrer, sauf si tu en construisais un.
Tout était un module :
un dock ici, une horloge là,
un menu qui s'ouvrait partout où tu faisais un clic droit.

<!-- S24 -->
Les thèmes s'échangeaient comme des fonds d'écran.
Certains avaient l'air futuristes.
D'autres ressemblaient à une station de travail Unix.
D'autres ne laissaient presque rien à l'écran.

<!-- S25 -->
Blackbox for Windows a pris le chemin inverse.
Il reprenait Blackbox, un gestionnaire de fenêtres Unix minimaliste,
jusqu'à son unique menu tout simple
et sa fine barre d'outils.

<!-- S26 -->
Son successeur, bbLean,
a gardé cette idée en vie sous Windows 2000 et XP.

<!-- S27 -->
Emerge Desktop a découpé le shell en parties séparées :
un lanceur, une zone de notification, une liste des tâches,
chacune un petit programme que tu pouvais garder ou retirer.

<!-- S28 -->
Pourquoi se donner tant de mal ?
En partie parce que le look de XP
était facile à reconnaître et difficile à changer.
Les thèmes changeaient les couleurs et les boutons.
La disposition ne changeait pas.

<!-- S29 -->
En partie à cause de la mémoire.
Sur une machine à 128 mégaoctets,
un shell plus léger promettait plus de place
pour tout le reste.

<!-- S30 -->
Et en partie à cause de Linux.
Là-bas, choisir son bureau était normal,
et certains utilisateurs de Windows voulaient
le même choix.

<!-- S31 -->
La plupart de ces projets ont disparu.
La dernière version de LiteStep était une préversion
de 2014, toujours marquée alpha.
Emerge Desktop et SharpEnviro se sont arrêtés aussi.

<!-- S32 -->
Les petites équipes de bénévoles y sont pour quelque chose.
Mais Windows a changé, lui aussi.
Au fil des ans, son bureau est devenu bien plus
qu'un seul exécutable.

<!-- S33 -->
L'expérience du bureau est aujourd'hui répartie
entre plusieurs processus,
composants système et applications empaquetées.
Même le menu Démarrer tourne comme un programme à part.

<!-- S34 -->
Remplacer explorer.exe ne veut pas dire remplacer
tout ce qui compose l'interface moderne de Windows.
Et c'est l'une des raisons pour lesquelles construire
un bureau alternatif complet
est plus difficile qu'avant.

<!-- S35 -->
Et pourtant, ça marche encore.
Cairo Desktop, un projet open source,
tourne aujourd'hui sous Windows 11.

<!-- S36 -->
Il apporte sa propre barre de menus en haut,
sa propre barre des tâches
et des dossiers que tu peux épingler à la barre sous forme de piles.

<!-- S37 -->
Il peut tourner à côté d'explorer.exe
ou prendre la place du shell.
Dans ce deuxième mode,
certaines parties de Windows 11 peuvent dysfonctionner,
dont les Paramètres et la Sécurité Windows.

<!-- S38 -->
Seelen UI s'y prend autrement.
Il ne remplace pas explorer.exe.
Il masque la barre des tâches et apporte ses propres éléments :
un dock, une barre, des widgets
et un gestionnaire de fenêtres qui dispose tes fenêtres en mosaïque.

<!-- S39 -->
Le résultat peut ne ressembler en rien à Windows.
Mais en dessous, explorer.exe tourne toujours.
C'est un nouveau visage, pas un nouveau shell.

<!-- S40 -->
Et Microsoft ?
Il a en fait une fonctionnalité officielle pour ça.
Elle s'appelle Shell Launcher,
et elle est conçue pour des appareils comme les bornes interactives.

<!-- S41 -->
Tu as sûrement déjà utilisé un truc comme ça
sans le savoir.
La borne de vente de billets d'une gare.
Une caisse en libre-service. Un distributeur de billets.

<!-- S42 -->
Beaucoup sont des PC sous Windows
dont le shell entier est une seule application.
Un administrateur désigne le programme,
et après la connexion, ce programme est tout le bureau.

<!-- S43 -->
Mais elle n'est disponible
que dans les éditions Enterprise, Education
et IoT Enterprise.

<!-- S44 -->
Et l'ancien mécanisme du registre
fait toujours partie de Windows.
Microsoft ne l'a simplement jamais transformé
en un réglage de bureau normal
pour les utilisateurs ordinaires.

<!-- S45 -->
Alors pourquoi Windows semble-t-il n'avoir qu'un seul bureau ?
Pas parce qu'il ne pourrait pas en avoir un autre.
Parce que le bureau est le produit.

<!-- S46 -->
Sous Linux, le bureau est un choix.
Certaines distributions te demandent d'en choisir un
pendant l'installation.
KDE Plasma, GNOME, Xfce, Cinnamon...

<!-- S47 -->
Sous Windows, le bureau, c'est ce que Microsoft montre
dans chaque pub, sur chaque capture d'écran
et sur chaque page d'assistance.
Un seul bureau, c'est un seul mode d'emploi
pour plus d'un milliard de machines.

<!-- S48 -->
C'est un vrai avantage.
Quand quelque chose casse,
l'écran de l'article d'aide ressemble au tien.
Le prix, c'est que la plupart des gens n'apprennent jamais
qu'ils avaient le choix.

<!-- S49 -->
Les gens remplaçaient le bureau de Windows
avant même que Windows 95 existe.
Ils ont construit des docks, des menus dépouillés
et des bureaux qui ne ressemblaient à rien d'autre.

<!-- S50 -->
La plupart de ces projets ont disparu.
Pas l'idée.
Sous chaque barre des tâches sur laquelle tu as cliqué,
il y a toujours ce même réglage, qui attend un autre nom.

<!-- S51 -->
Le bureau n'est qu'un logiciel parmi d'autres.
Et un logiciel, ça se remplace.

<!-- S52 -->
Alors voici une question pour toi.
Si Windows te laissait choisir ton bureau
à l'installation, comme certaines distributions Linux,
tu changerais, ou tu garderais celui que tu connais ?
Dis-le-moi dans les commentaires.
