# Ça marche. Alors pourquoi le mettre à jour ?

Traduction de `script.md`. Mêmes marques de scène, même nombre de lignes.

<!-- S01 -->
Imaginez une entreprise
qui développe du logiciel
depuis vingt ans.

Ses programmeurs savent
ce qu'est la dette technique.

<!-- S02 -->
Ils savent ce que veut dire
une technologie obsolète.

Ils savent que le support finit par s'arrêter.

Ils savent qu'un jour
le système devra être mis à jour.

Et pourtant...

<!-- S03 -->
...de temps en temps,
quelqu'un doit encore expliquer
pourquoi il faudrait mettre à jour.

Bienvenue dans l'informatique.

<!-- S04 -->
L'argument le plus populaire est :

« Mais ça marche. »

Et oui.

Ça marche.

<!-- S05 -->
Windows XP marchait.

Un téléphone de 2008 peut encore marcher.

Une voiture de vingt ans aussi.

<!-- S06 -->
Ça ne veut pas forcément dire
que vous devriez bâtir dessus
les dix prochaines années
de votre activité.

<!-- S07 -->
Parce que « ça marche »
n'est pas une propriété de votre logiciel.

C'est une propriété de votre logiciel
et de tout ce qui l'entoure.

Aujourd'hui.

<!-- S08 -->
Un logiciel n'existe pas tout seul.

Chaque application dépend de
langages, de frameworks, de bibliothèques,
de systèmes, de bases de données, de serveurs.

Et tout cela change en permanence.

<!-- S09 -->
Voici un exemple réel.

Imaginez un appareil
qui utilise un réseau 2G.

Il marche parfaitement.

Puis l'opérateur annonce :

« La 2G va disparaître. »

<!-- S10 -->
Et vous répondez :

« Mais mon appareil marche encore ! »

Oui.

Mais il a besoin du monde autour.

Et ce monde est passé à autre chose.

<!-- S11 -->
Poussons ça jusqu'à l'absurde.

Imaginez que votre distributeur d'eau annonce :

« À partir de l'an prochain,
nous passons à Water 2.0. »

<!-- S12 -->
Vos tuyaux marchent encore.

Votre lavabo marche encore.

Vos toilettes marchent encore.

Tout va bien.

<!-- S13 -->
Sauf que votre plomberie
ne gère que Water 1.0.

Vous avez donc deux choix.

Remplacer toute la plomberie...

ou payer un supplément
pour continuer à recevoir l'ancienne eau.

Pour toujours.

<!-- S14 -->
Ça paraît absurde.

Et pourtant c'est à peu près ce qui arrive
avec les technologies héritées.

<!-- S15 -->
Les vieilles versions perdent leur support.

Les nouveaux logiciels ne marchent plus avec.

Et vous finissez par payer un supplément
juste pour garder en vie quelque chose d'obsolète.

<!-- S16 -->
Poussons l'absurde encore plus loin.

Imaginez une entreprise
qui fabrique des chaises de bureau.

Elle sort Chair 8.

Votre entreprise a Chair 6.

<!-- S17 -->
Elle marche parfaitement.

Elle a quatre pieds.

Elle a un dossier.

Tout va bien.

<!-- S18 -->
Puis le fabricant annonce :

« Chair 6 n'est plus supportée. »

Fini les pièces de rechange.

Fini les correctifs de sécurité.

<!-- S19 -->
Vous dites :

« Pourquoi acheter de nouvelles chaises ?

Celles-ci marchent ! »

C'est vrai.

Vous pouvez garder Chair 6.

<!-- S20 -->
Sauf qu'un jour vous découvrez
qu'elle ne va pas sous les nouveaux bureaux.

Les pieds de rechange
ne se font plus.

Et la seule personne
qui savait réparer Chair 6
est partie en retraite il y a cinq ans.

<!-- S21 -->
Heureusement, il existe une solution.

Enterprise Extended Chair Support.

<!-- S22 -->
Pour quelques millions par an,
le fabricant continuera de produire
des pieds de rechange
pour vos chaises obsolètes.

<!-- S23 -->
Complètement absurde.

Mais remplacez « chaise » par « logiciel »...

et soudain plus personne
ne trouve ça bizarre.

<!-- S24 -->
Sauf que cette partie-là n'est pas une blague.

Quand le support de Windows XP
s'est arrêté en 2014,
Microsoft a vendu exactement ce contrat.

<!-- S25 -->
Custom Support.

Environ deux cents dollars
par machine pour la première année.

Le double pour la deuxième.

<!-- S26 -->
Le secteur public britannique a signé.

Cinq millions et demi de livres
pour une année de plus
de mises à jour de sécurité.

<!-- S27 -->
Un an plus tard
ils ont décidé de ne pas renouveler.

Et les vieilles machines
étaient toujours là.

<!-- S28 -->
Voilà Enterprise Extended Chair Support.

Ça cesse simplement d'être drôle
quand la facture est réelle.

<!-- S29 -->
C'est aussi pour ça que la question :

« Que va nous apporter cette mise à jour ? »

peut induire en erreur.

Une nouvelle fonction ?
Les utilisateurs la voient.

Un nouveau bouton ?

<!-- S29b -->
Les utilisateurs le voient.

Une mise à jour technique ?

<!-- S29c -->
Rien.

Et c'est exactement le sujet.

<!-- S30 -->
Une mise à jour réussie
a un résultat très ennuyeux :

Il ne se passe rien.

L'application continue de marcher,
mais sur une technologie supportée.

<!-- S31 -->
Même si ce n'est pas
tout à fait toute la vérité.

Une vieille technologie
tombe rarement en panne d'un coup.

<!-- S32 -->
Elle lâche quand l'audit de sécurité
remonte une non-conformité.

Quand la nouvelle interface d'un partenaire
demande quelque chose
que votre plateforme ne sait pas parler.

<!-- S33 -->
Quand l'hébergeur
retire l'image que vous utilisez.

Ou quand vous cherchez quelqu'un
et que personne ne veut le poste.

<!-- S34 -->
Rien de tout ça n'est un bug.

Il n'y a rien à réparer,
parce que rien n'est cassé.

Le monde a simplement
cessé de vous attendre.

<!-- S35 -->
C'est comme la vidange de votre voiture.

Personne ne s'enthousiasme pour de l'huile neuve.

Mais sautez l'entretien
assez longtemps...

et vous finirez par avoir
un problème bien plus palpitant.

<!-- S36 -->
La dette technique marche pareil.

Une petite mise à jour aujourd'hui, c'est :

Actualiser quelques dépendances.

Corriger quelques incompatibilités.

Lancer les tests.

Terminé.

<!-- S37 -->
Attendez cinq ans.

Maintenant c'est :

Actualiser la plateforme.

Remplacer la moitié des bibliothèques.

Monter le framework de version.

Réécrire ce composant préhistorique.

Et surtout, quoi que vous fassiez...

ne touchez pas à ce fichier.

<!-- S38 -->
À ce stade
nous ne faisons plus une mise à jour.

Nous faisons de l'archéologie.

<!-- S39 -->
« Regarde ! Une dépendance de 2014 ! »

« N'y touche pas. »

« Pourquoi ? »

« On ne sait pas ce qu'elle fait. »

<!-- S40 -->
Parce que la dette technique
n'est pas que du vieux logiciel.

C'est aussi de la peur.

La peur de changer quelque chose
que plus personne ne comprend vraiment.

<!-- S41 -->
Et c'est là qu'intervient
un vieux dicton.

Le cheval du forgeron va pieds nus.

<!-- S42 -->
Un forgeron passe sa vie
à ferrer
les chevaux de tout le monde...

et son propre cheval n'a rien aux pieds.

<!-- S43 -->
En anglais, on le dit
des enfants du cordonnier,
qui n'ont rien aux pieds.

Autre métier.

Même angle mort.

<!-- S44 -->
Les éditeurs de logiciels
sont remarquablement bons à ce jeu.

Nous expliquons depuis des décennies
pourquoi les vieux systèmes des clients
doivent être mis à jour...

pendant que les nôtres vieillissent.

<!-- S45 -->
Parce que :

« On n'a pas le temps là. »

L'année suivante :

« Toujours pas prioritaire. »

<!-- S46 -->
Quelques années plus tard :

« Ça va être
une sacrée mise à jour. »

Et finalement :

« C'est trop gros à mettre à jour. »

<!-- S47 -->
C'est ça, le piège.

Plus vous repoussez,
plus votre système s'éloigne
de la technologie qui l'entoure.

Et combler cet écart
coûte plus cher chaque année.

<!-- S48 -->
Et rien de tout ça
n'est un malentendu.

Ils savent que c'est vieux.

Ils savent que le support s'arrête.

Ils savent que la mise à jour
finira par être nécessaire.

C'est une décision de gestion.

<!-- S49 -->
Le coût de la mise à jour se voit aujourd'hui.

Le coût de ne rien faire
est quelque part dans l'avenir.

<!-- S50 -->
Et ces deux coûts
ne retombent pas sur la même personne.

La mise à jour sort
du budget de cette année,
validée par quelqu'un
qui n'en retire rien de visible.

<!-- S51 -->
La panne sort d'un budget
qui n'existe pas encore,
une année où c'est quelqu'un d'autre
qui sera assis sur cette chaise.

<!-- S52 -->
Les humains sont remarquablement bons
pour envoyer les problèmes dans l'avenir.

Malheureusement...

l'avenir finit par arriver.

<!-- S53 -->
La dette technique ne disparaît pas
quand on l'ignore.

Elle grossit.

<!-- S54 -->
Pour être juste,
tout n'a pas besoin d'être mis à jour.

Un système qu'on éteint l'an prochain
peut rester exactement tel quel.

<!-- S55 -->
Et « il existe une version plus récente »
n'est pas un argument en soi.

<!-- S56 -->
La question n'a jamais été
« est-ce la dernière version ? »

La question, c'est :

« quand ça cassera,
est-ce que quelqu'un saura encore réparer ? »

<!-- S57 -->
C'est pour ça que la version saine
a l'air décevante d'ennui.

Quelques dépendances à chaque livraison.

Une version de framework à la fois.

<!-- S58 -->
Pas un projet.

Pas une migration.

Pas un programme de deux ans
avec un comité de pilotage.

Juste de l'entretien.

Comme personne ne monte un projet
pour faire une vidange.

<!-- S59 -->
Alors la prochaine fois qu'on vous demande :

« Pourquoi mettre à jour ?
Ça marche encore. »

<!-- S60 -->
Souvenez-vous de la 2G.

Souvenez-vous de Water 2.0.

Et souvenez-vous de Chair 6.

<!-- S61 -->
Parce que « ça marche aujourd'hui »
n'est pas la même chose
que « ça marchera dans cinq ans ».

La technologie avance.

<!-- S62 -->
Et si nous n'avançons pas avec elle,
nous finirons par ne plus
entretenir notre logiciel.

Nous entretiendrons un musée.

<!-- S63 -->
Et c'est exactement ce que faisait
le cheval du forgeron.

Il marchait pieds nus...

pendant que le forgeron n'avait pas le temps,
occupé à ferrer tous les autres.
