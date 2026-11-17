<!-- S01 -->
Vous essayez de supprimer un fichier.
L'ordinateur dit qu'il est ouvert
dans un autre programme.
Mais il ne dit pas lequel.

<!-- S02 -->
Ce message est la partie visible
d'une question bien plus étrange.
Que veut dire au juste
ouvrir un fichier ?

<!-- S03 -->
Car sur un autre ordinateur,
le même fichier, ouvert pareil,
se supprime sans broncher.

<!-- S04 -->
Même fichier.
Même geste.
Deux réponses complètement différentes.

<!-- S05 -->
Commençons par ce
qui agace tout le monde.
Quel programme ?

<!-- S06 -->
Windows le sait.
Il a un objet noyau
pour ce fichier ouvert
et connaît le processus propriétaire.
Il pourrait le nommer.

<!-- S07 -->
Alors vous fermez des choses au hasard.
Vous ouvrez le Gestionnaire des tâches.
Vous fixez une liste de processus
et n'en reconnaissez presque aucun.

<!-- S08 -->
Et pendant des années,
la réponse était bel et bien
de télécharger un outil à part.
Unlocker est sorti en 2005,
et sous Windows XP c'était la réponse.

<!-- S09 -->
Puis Windows 7 a intégré
le Moniteur de ressources.
L'onglet Processeur.
Une liste nommée Handles associés.

<!-- S10 -->
Tapez le nom du fichier.
Il vous donne le programme
et l'identifiant du processus.
Rien à installer.
C'est là depuis 2009.

<!-- S10b -->
Mais les outils séparés faisaient
plus que vous le dire.
Ils savaient fermer le handle
et libérer le fichier.

<!-- S11 -->
Ce qui nous ramène
à la question.
Qu'a obtenu ce programme
en ouvrant le fichier ?

<!-- S12 -->
Disons qu'un lecteur ouvre
un fichier nommé movie.mp4.
Sous Windows, ouvrir un fichier
veut dire renseigner deux paramètres.

<!-- S13 -->
La première est évidente.
Qu'est-ce que je veux en faire ?
Le lire. Y écrire.

<!-- S14 -->
La seconde est la plus intéressante.
Que peuvent faire les autres
pendant que je le tiens ouvert ?

<!-- S15 -->
C'est un vrai réglage.
Vous dites ce que les autres programmes
peuvent faire pendant que vous le tenez.

<!-- S16 -->
Ils peuvent le lire.
Ils peuvent aussi y écrire.
Ils peuvent le supprimer ou le renommer.

<!-- S16b -->
Ou bien rien du tout.
Personne n'y touche
tant que je m'en sers.

<!-- S17 -->
L'indicateur qui autorise la suppression
s'appelle FILE_SHARE_DELETE.
Et la documentation de Microsoft
ajoute une ligne en dessous.

<!-- S18 -->
Le droit de supprimer couvre
la suppression et le renommage.

<!-- S19 -->
Donc un programme qui refuse
le partage de suppression
a bloqué le renommage aussi.

<!-- S20 -->
Et si le programme qui a ouvert
le fichier ne l'a pas accordé,
personne d'autre ne peut le prendre.

<!-- S21 -->
Voilà pourquoi l'erreur
ne s'appelle pas fichier occupé.
Elle s'appelle violation de partage.

<!-- S22 -->
La réponse était depuis le début
dans le nom
de l'erreur elle-même.

<!-- S23 -->
Maintenant la même chose
sur une machine Linux.
Un lecteur ouvre la vidéo.

<!-- S24 -->
Et vous tapez
rm movie.mp4.

<!-- S24b -->
Ça marche.
La vidéo continue de jouer.

<!-- S25 -->
Qu'a donc obtenu ce programme,
si ce n'est une prise sur le fichier ?

<!-- S26 -->
C'est toute l'idée
de cette vidéo.
Le nom n'est pas le fichier.

<!-- S27 -->
movie.mp4 est une ligne
dans un répertoire.
Cette ligne pointe vers un objet
qui contient les données réelles.

<!-- S28 -->
Quand un programme ouvre le fichier,
ce qu'il obtient est une référence
vers l'objet.
Pas vers la ligne.

<!-- S29 -->
Supprimer le fichier
efface donc la ligne.
L'objet reste intact.

<!-- S30 -->
La page de manuel le dit
en une seule phrase.
Le fichier continue d'exister
jusqu'à la fermeture du dernier
descripteur de fichier qui le référence.

<!-- S31 -->
Cela paraît abstrait
jusqu'à ce qu'on le voie.
J'ai donc fait un fichier journal
de cinq cents mégaoctets
et laissé un processus le tenir ouvert.

<!-- S31b -->
Puis je l'ai supprimé.

<!-- S32 -->
Le listage du répertoire
n'affiche plus rien du tout.
L'outil qui mesure
la taille du dossier dit zéro.

<!-- S33 -->
Et l'outil qui mesure
l'espace libre sur le disque
dit que cinq cents mégaoctets
manquent toujours.

<!-- S33b -->
Un dossier vide.
Un demi-gigaoctet envolé.

<!-- S34 -->
Cela arrive assez souvent
pour qu'il existe une commande
rien que pour trouver ces fichiers.
Supprimés, invisibles, encore sur le disque.

<!-- S35 -->
Et l'espace revient
à l'instant où ce processus
lâche le fichier.

<!-- S36 -->
La même logique vaut pour le renommage.
Déplacez le fichier ouvert,
et le programme ne remarque rien.

<!-- S37 -->
Le manuel est aussi net là-dessus.
Les descripteurs de fichier déjà
ouverts ne sont pas affectés.

<!-- S37b -->
Il n'a jamais utilisé le nom.

<!-- S38 -->
Ce qui a une limite
qu'il vaut mieux connaître.
On ne peut pas écraser sur place
un programme en cours d'exécution.

<!-- S38b -->
Linux refuse.
Text file busy.

<!-- S39 -->
Ce que vous pouvez faire,
c'est détacher le nom
et mettre un nouveau fichier là.

<!-- S40 -->
L'ancien processus continue
de s'exécuter à partir d'un objet
qui n'a plus aucun nom.
Tout ce qui démarre ensuite utilise le nouveau.

<!-- S41 -->
Ce qui est encore la même idée,
qui se confirme une fois de plus.
On peut remplacer beaucoup de choses
sans toucher à l'objet sur place.

<!-- S41b -->
C'est pourquoi Linux peut mettre à jour
un programme en cours d'exécution.
Vous n'obtenez la nouvelle version
qu'après l'avoir redémarré.

<!-- S42 -->
Windows est-il donc
simplement moins bien conçu ?

<!-- S42b -->
Non.
Et voici la partie
que presque personne ne connaît.

<!-- S43 -->
Windows a un moyen
de faire exactement la même chose.

<!-- S43b -->
Sur NTFS, Windows peut demander
une suppression à la POSIX.

<!-- S44 -->
Microsoft décrit
ce qui se passe alors.
Le nom est retiré
de l'espace de noms visible.

<!-- S45 -->
Et les applications qui avaient déjà
le fichier ouvert peuvent s'en servir,
même si le nom
par lequel elles l'ont ouvert a disparu.

<!-- S46 -->
C'est le comportement d'Unix.
Sur NTFS.
Documenté par Microsoft.

<!-- S47 -->
Les deux systèmes savent faire les deux.
Ce qui diffère, c'est le comportement par défaut.
Ce que vous obtenez en ouvrant
un fichier sans y penser.

<!-- S48 -->
Sous Windows, vous obtenez un contrat.
Sous Unix, vous obtenez une référence
à un objet.

<!-- S49 -->
Ce qui ressemble à une question
pour programmeurs,
jusqu'au jour où l'on a vu
ce message précis.

<!-- S50 -->
Redémarrez votre ordinateur
pour terminer l'installation des mises à jour.

<!-- S51 -->
Supposons que Windows doive remplacer
une bibliothèque qu'un processus
tient ouverte sous le contrat strict.

<!-- S52 -->
Il ne peut pas remplacer le fichier
alors que ce processus l'utilise.
Donc quelque chose doit lâcher.

<!-- S53 -->
Quittez l'application.
Arrêtez le service.
Ou confiez toute l'affaire
au Gestionnaire de redémarrage.

<!-- S54 -->
Qui est un vrai composant.
Il les arrête dans l'ordre.
Les applications Windows,
puis les programmes console,

<!-- S55 -->
puis les services,
et l'Explorateur en dernier.
Ensuite il les relance.

<!-- S56 -->
Et il existe pour une seule raison,
que Microsoft énonce clairement
dans sa propre documentation.

<!-- S57 -->
La raison principale
pour laquelle les installations
et les mises à jour exigent
un redémarrage du système...

<!-- S58 -->
c'est que certains des fichiers
mis à jour sont alors utilisés
par une application
ou un service en cours d'exécution.

<!-- S59 -->
Ce serait trop net de s'arrêter là.
Les règles de partage ne sont pas la seule
raison pour laquelle un ordinateur redémarre.

<!-- S60 -->
Une mise à jour du noyau, c'est autre chose.
On ne remplace pas le noyau
sous lui-même.

<!-- S61 -->
Linux a le même problème,
même si le correctif à chaud
évite parfois le redémarrage.

<!-- S62 -->
La version honnête
affirme donc moins
que la version satisfaisante.

<!-- S63 -->
La façon dont Windows traite les fichiers
en cours d'utilisation a rendu certains
composants plus difficiles à remplacer à chaud,
et cela y a contribué.

<!-- S64 -->
Car tout choix de conception
a une conséquence quelque part.

<!-- S65 -->
Windows laisse le programme
qui ouvre un fichier décider
de ce que les autres peuvent en faire.

<!-- S66 -->
Le prix, c'est que parfois
vous ne pouvez pas supprimer votre fichier,
parce qu'un autre programme
ne l'a pas permis.

<!-- S67 -->
Unix garde le nom
et l'objet séparés,
donc on peut remplacer beaucoup
pendant que le système tourne.

<!-- S68 -->
Le prix, c'est un demi-gigaoctet
disparu du disque
et qui n'appartient à aucun fichier.

<!-- S69 -->
Et regardez comment chacun
des deux se résout.
Sous Windows, une issue est
de fermer le programme
qui tient le fichier.

<!-- S70 -->
Sous Linux, une façon
de récupérer cet espace
est de redémarrer le service
qui le maintient encore ouvert.

<!-- S71 -->
Des causes différentes.
Parfois le même remède.

<!-- S71b -->
Au fait, si vous voulez voir
où nous mène la prochaine question,
pensez à vous abonner.
Cela aide beaucoup la chaîne.

<!-- S72 -->
Donc. La question du début.
Que veut dire
ouvrir un fichier ?

<!-- S73 -->
Cela veut dire que vous tenez quelque chose.
Les deux systèmes vous mettent
simplement autre chose dans la main.

<!-- S74 -->
Voilà pourquoi ce message
n'a jamais vraiment dit
que le fichier ne peut pas être supprimé.

<!-- S75 -->
Il disait que le programme
qui l'a ouvert
ne vous l'a pas permis.

<!-- S75b -->
Et il sait quel programme.
Il ne l'a simplement pas mentionné.
