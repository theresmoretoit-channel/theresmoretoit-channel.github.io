<!-- S01 -->
Neuf cent quatre-vingt-dix-neuf livres
et quatre-vingt-dix-neuf pence.
Ajoute un penny.

<!-- S02 -->
Le résultat est zéro.

<!-- S03 -->
Pas de message d'erreur. Pas de plantage.
Juste zéro, inscrit en silence sur le compte.

<!-- S04 -->
En COBOL, quand le champ du résultat
est trop petit pour le contenir,
le chiffre en trop peut tout simplement disparaître.
Sauf si le programme demande à être averti,
le calcul continue.

<!-- S05 -->
Et il n'arrondit pas non plus.
Deux livres et trente-quatre pence et demi,
stockés au penny près,
deviennent deux livres trente-quatre.

<!-- S06 -->
Écris un seul mot de plus, ROUNDED,
et on obtient deux livres trente-cinq.

<!-- S07 -->
Aucun des deux n'est un bug.
Ce sont des règles.
Et beaucoup de banques dans le monde
tournent encore avec des règles comme celles-là.

<!-- S08 -->
COBOL est un langage de programmation
de 1959.
Tous les programmes écrits en COBOL ne sont pas si vieux.
Mais le langage, si,
et ses habitudes aussi.

<!-- S09 -->
Alors pourquoi les banques ne l'ont-elles pas remplacé ?
Elles ont l'argent.
Elles ont les ingénieurs.

<!-- S10 -->
Pour le savoir, on va voir trois cas réels.
Une banque qui a tenté de quitter son vieux système,
une autre qui y est parvenue,
et une crise où tout le monde a accusé COBOL.

<!-- S11 -->
Mais d'abord, ce demi-penny qui manque.

<!-- S12 -->
Imagine que tu réécrives ce programme bancaire
dans un langage moderne.
Tu corrigerais sans doute ces règles.
Le dépassement devient une erreur.
Le demi-penny est arrondi au supérieur.

<!-- S13 -->
Plus propre. Plus sûr.
Et maintenant, partout où un demi-penny apparaît,
ton programme ne donne plus le même résultat que l'ancien.

<!-- S14 -->
Les langages modernes savent calculer exactement en décimal.
Java a un type prévu pour ça.
Mais même là,
la règle d'arrondi est un choix.

<!-- S15 -->
Un réglage courant arrondit au supérieur pile à la moitié :
deux livres trente-cinq.
Un autre arrondit au chiffre pair le plus proche :
deux livres trente-quatre.
Les deux sont corrects. Un seul concorde.

<!-- S16 -->
Et avec la virgule flottante ordinaire,
celle que la plupart des programmes utilisent par défaut,
c'est encore plus étrange.
Zéro virgule un plus zéro virgule deux
ne fait pas zéro virgule trois.

<!-- S17 -->
Remplacer COBOL, ce n'est donc pas traduire.
C'est retrouver chaque règle de ce genre,
dans des millions de lignes,
et garder chacune exactement comme elle était.

<!-- S18 -->
Mais comment COBOL en est-il arrivé là ?

<!-- S19 -->
En mai 1959,
le département de la Défense américain
a convoqué une réunion au Pentagone.
Constructeurs d'ordinateurs, administrations
et grandes entreprises sont venus,
tous avec le même problème.

<!-- S20 -->
Chaque ordinateur avait son propre langage.
Un programme de paie écrit pour une machine
ne servait à rien sur une autre.

<!-- S21 -->
Un comité a conçu un langage commun
pour les entreprises.
Sa principale influence était FLOW-MATIC,
de l'équipe de Grace Hopper chez Remington Rand.

<!-- S22 -->
Et en décembre 1960,
pratiquement le même programme COBOL
a tourné sur deux ordinateurs
de constructeurs concurrents.
C'était tout l'intérêt.

<!-- S23 -->
Il était conçu pour que les gens puissent le suivre.
ADD PAYMENT TO ACCOUNT-BALANCE.
Tu devines sans doute ce que ça fait.

<!-- S24 -->
Et il stockait l'argent comme on l'écrit :
en chiffres décimaux.
La virgule
n'a même pas besoin d'être stockée.
La description du champ indique où elle se place :
les deux derniers chiffres sont les pence.

<!-- S25 -->
En 1964, IBM a lancé le System/360.
Sa conception incluait des instructions
d'arithmétique décimale.

<!-- S26 -->
Et depuis, IBM conçoit ses mainframes
pour qu'ils restent compatibles.
Bien des programmes anciens peuvent encore tourner
sur les machines d'aujourd'hui
sans être réécrits.

<!-- S27 -->
Il y a donc rarement eu un moment
qui obligeait qui que ce soit à migrer.
Chaque année, le code continuait de marcher,
et chaque année, il accumulait de nouvelles règles.
Nouveaux produits, nouveaux impôts, nouvelles normes,
nouvelles exceptions.

<!-- S28 -->
Personne n'a mesuré combien de code COBOL
tourne encore dans le monde.
Mais selon IBM, quarante-cinq
des cinquante plus grandes banques du monde
utilisent encore ses mainframes.

<!-- S29 -->
Et certains propriétaires ont compté.
En 2017, la Sécurité sociale américaine
a déclaré que ses systèmes contenaient
plus de soixante millions de lignes de COBOL.

<!-- S30 -->
En 2025, les auditeurs du gouvernement américain
ont listé les onze systèmes fédéraux
qui avaient le plus besoin d'être remplacés.

<!-- S31 -->
Ils avaient entre vingt-trois
et soixante ans,
et leur fonctionnement coûtait environ sept cent cinquante
millions de dollars par an.

<!-- S32 -->
Bref, le code est vieux, il est partout,
et il est plein de règles que personne n'a documentées.
Le danger, c'est sûrement de le garder.

<!-- S33 -->
Voyons ce qui se passe
quand une banque s'en va.

<!-- S34 -->
En 2018, une banque britannique appelée TSB
avait environ cinq millions de clients,
et un problème.

<!-- S35 -->
Ses systèmes étaient loués
au Lloyds Banking Group,
un concurrent,
et les frais allaient fortement augmenter.

<!-- S36 -->
TSB a donc décidé de tout migrer
vers une nouvelle plateforme,
construite par son nouveau propriétaire,
la banque espagnole Sabadell.

<!-- S37 -->
Un week-end d'avril.
Le dimanche soir,
le nouveau système a été mis en service.

<!-- S38 -->
Le lundi, il y a eu environ
neuf cent mille tentatives de connexion.
Seule une connexion à la banque en ligne
sur dix environ a réussi.

<!-- S39 -->
Des paiements ont échoué.
Certains clients se sont connectés
et ont vu les comptes d'autres personnes.

<!-- S40 -->
Le pire a duré environ une semaine.
TSB n'est revenue à un fonctionnement normal
qu'en décembre.

<!-- S41 -->
Les retombées ont coûté environ
trois cent trente millions de livres
rien qu'en 2018.
Les régulateurs ont ensuite ajouté
près de quarante-neuf millions d'amendes.

<!-- S42 -->
Et voici le plus étrange.
Les données des clients sont arrivées intactes.
Les deux rapports officiels le disent.

<!-- S43 -->
Ce qui a lâché, c'est la nouvelle plateforme autour.
Deux centres de données, configurés différemment.
Des tests de performance sur un seul des deux,
et des objectifs revus à la baisse
quand les tests ont échoué.

<!-- S44 -->
Et il n'y avait pas de retour possible.
Une fois les données migrées,
revenir à l'ancien système était,
selon les mots du régulateur,
« pratiquement impossible ».

<!-- S45 -->
TSB ne fuyait pas un système en panne.
Elle quittait un système qui fonctionnait,
à cause de son propriétaire
et de son coût.
Le danger, c'était de partir.

<!-- S46 -->
Alors, partir, c'est toujours une catastrophe ?

<!-- S47 -->
En 2008, la Commonwealth Bank australienne
a entrepris de remplacer des systèmes centraux
qui la servaient
depuis plus de quarante-cinq ans.

<!-- S48 -->
Le plan : environ cinq cent quatre-vingts
millions de dollars australiens,
et quatre ans.

<!-- S49 -->
Il en a fallu cinq.
La presse a ensuite estimé le total
à environ un virgule un milliard,
à mesure que le projet s'élargissait.

<!-- S50 -->
Mais elle n'a pas tout migré
en un seul week-end.
Les comptes de dépôt d'abord, en 2010.
Les comptes professionnels ont suivi en 2011,
et les prêts en 2012.

<!-- S51 -->
Chaque étape, la banque pouvait
l'observer, la vérifier et en tirer des leçons
avant de miser sur la suivante.

<!-- S52 -->
Au bout du compte, selon la banque,
elle est devenue la première grande banque australienne
à proposer des services bancaires en temps réel,
jour et nuit.

<!-- S53 -->
Donc c'est possible.
Mais regarde ce que ça a demandé.
Cinq ans, une facture bien plus lourde,
et de la patience.

<!-- S54 -->
Moderniser, ce n'est pas un achat.
C'est un projet,
avec ses propres risques.

<!-- S55 -->
Passons maintenant à la crise
où tout le monde a accusé COBOL.

<!-- S56 -->
Mars 2020.
Alors que la pandémie paralysait le New Jersey,
les nouvelles demandes d'allocations chômage ont bondi
de moins de dix mille en une semaine
à plus de cent cinquante-cinq mille.

<!-- S57 -->
Seize fois plus,
en sept jours.
L'agence pour l'emploi était débordée.

<!-- S58 -->
Début avril, le gouverneur
a lancé un appel aux volontaires.
Pas seulement aux soignants,
mais aussi aux gens qui connaissaient COBOL.
Les systèmes de l'État, a-t-il dit,
avaient plus de quarante ans.

<!-- S59 -->
L'histoire s'est vite répandue.
Un code antique se serait effondré
sous le poids de la pandémie.

<!-- S60 -->
Mais quand l'auditeur de l'État
s'est penché sur la question plus tard,
il n'a trouvé aucune preuve
que les retards aient été causés
par les systèmes informatiques.

<!-- S61 -->
De leur côté, des journalistes qui ont examiné
les messages d'erreur que voyaient les gens
en ont attribué beaucoup au site web en façade,
écrit dans un langage bien plus récent, Java.
L'ancien code derrière continuait de tourner.

<!-- S62 -->
Alors pourquoi l'État avait-il besoin de programmeurs COBOL ?
Parce que le Congrès changeait les règles.
Nouvelles aides, nouveaux montants,
nouvelles personnes éligibles,
et chaque changement devait entrer
dans le code, et vite.

<!-- S63 -->
Le problème n'était pas que le code soit vieux.
C'est que peu de gens savaient le modifier,
et que les lignes téléphoniques étaient saturées
et le personnel débordé, lui aussi.

<!-- S64 -->
Trois cas.
Une banque qui a quitté un système qui marchait encore,
et dont la migration a échoué.
Une banque qui est partie prudemment,
et qui a réussi.
Et une crise où l'on a accusé le vieux code,
sans que personne puisse prouver qu'il était en cause.

<!-- S65 -->
Ça ne veut pas dire que les vieux systèmes ne lâchent jamais.
Ils lâchent.
Ils deviennent chers,
ceux qui les comprennent partent à la retraite,
et attendre a aussi un coût.

<!-- S66 -->
Mais l'âge se voit facilement,
les vrais risques, non.
Des règles que personne n'a documentées.
Un savoir dans la tête de quelques personnes.
Et le moment de la bascule.

<!-- S67 -->
Voilà pourquoi bien des banques ne remplacent pas
le vieux cœur du système d'un seul coup.
Elles l'enveloppent.
L'appli sur ton téléphone est récente,
mais elle parle peut-être à quelque chose
de bien plus ancien.

<!-- S68 -->
Et elles le remplacent morceau par morceau.
En 2004, Martin Fowler, qui écrit sur le logiciel,
a baptisé ça d'après le figuier étrangleur,
une plante de forêt tropicale qui entoure un arbre
jusqu'à pouvoir tenir debout toute seule.

<!-- S69 -->
L'ancien système continue de fonctionner
pendant que le nouveau pousse autour,
une tâche à la fois,
jusqu'à ce que plus rien ne dépende de l'ancien.

<!-- S70 -->
Ce qui nous ramène à ce demi-penny.
Quelque part, un programme le perd peut-être encore,
parce que quelqu'un en a décidé ainsi,
il y a des décennies.
Remplacer ce programme, c'est savoir ça,
et tout ce qui y ressemble.

<!-- S71 -->
Ce n'est pas forcément l'ancien système
qui lâche.
Parfois, c'est ce qui le remplace.

<!-- S72 -->
Parce que remplacer la technologie,
ce n'est pas supprimer le risque.
Parfois, ça ne fait que déplacer le risque
sur un seul week-end d'avril.

<!-- S73 -->
Alors, voici une question pour toi.
Si un système fonctionne depuis quarante ans,
quand faut-il le remplacer ?
Et toi, as-tu déjà dû en remplacer un ?
Dis-le-moi dans les commentaires.
