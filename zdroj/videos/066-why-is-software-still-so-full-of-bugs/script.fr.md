<!-- S01 -->
Tous les quelques jours, un nouveau bug grave
fait la une.
Un bug qui laisse quelqu'un contourner la connexion.
Un bug qui laisse fuiter des données privées.
Un bug qui livre ton ordinateur à un attaquant.

<!-- S02 -->
Parfois c'est Windows. Parfois Linux.
Un navigateur, une base de données, un service cloud...
ou une petite bibliothèque
dont des millions de développeurs dépendent.

<!-- S03 -->
Et la réaction est presque toujours la même.
Comment les programmeurs ont-ils pu manquer ça ?

<!-- S04 -->
Ce sont des professionnels.
Ils ont des revues de code, des tests automatisés,
des audits de sécurité, du fuzzing...
et les bugs continuent quand même d'arriver.

<!-- S05 -->
Alors est-il seulement possible
d'écrire un logiciel complexe sans bugs ?

<!-- S06 -->
Commençons par un nombre.
Imagine un programme avec seulement cent réglages,
chacun soit activé, soit désactivé.

<!-- S07 -->
Cent simples décisions par oui ou par non.
Ça fait combien de combinaisons ?

<!-- S08 -->
Deux puissance cent.
C'est à peu près un million de billions de billions.

<!-- S09 -->
Imagine maintenant que tu puisses tester
un milliard de combinaisons par seconde.
Et que tu aies commencé au Big Bang.

<!-- S10 -->
À ce jour, tu aurais testé
environ une combinaison sur trois mille.

<!-- S11 -->
Et cent interrupteurs, ce n'est rien.
Un vrai programme en a des millions.
Alors « il suffit de tout tester »
n'est pas une question de coût. C'est impossible.

<!-- S12 -->
Et ces interrupteurs n'ont rien d'exotique.
Prends une des choses les plus simples
qu'un programme fasse.
Un utilisateur demande son compte par son numéro.
On le trouve dans la base de données.
On le renvoie.

<!-- S13 -->
Mais et si l'utilisateur n'existe pas ?
Et si quelqu'un envoie du texte au lieu d'un nombre ?
Ou un nombre négatif ? Ou un nombre énorme ?

<!-- S14 -->
Et si cette personne n'a pas le droit de le voir ?
Et si quelqu'un supprime le compte
au moment précis où on le charge ?
Et si la même requête arrive deux fois ?

<!-- S15 -->
Chacune de ces questions est simple.
Le problème, c'est leur combinaison.
Chacune est un interrupteur de plus.

<!-- S15b -->
Au fait, si tu aimes ce genre de
vidéos, pense à t'abonner.

Ça aide vraiment la chaîne.

<!-- S16 -->
Et un ordinateur ne va pas démêler ça pour nous.
Il fait exactement ce qu'on lui dit.
Pas ce qu'on voulait dire.

<!-- S17 -->
C'est pour ça qu'on a inventé les langages de programmation.
Ils nous laissent décrire des choses complexes
sans penser à chaque détail.

<!-- S18 -->
Mais certains s'occupent de moins
qu'on ne l'espérerait.
Prends le C. Il est rapide, il est simple,
et il te donne un énorme contrôle sur la mémoire.

<!-- S19 -->
Donc tu peux écrire ceci.
On réserve de la place pour seize caractères.
Puis on dit : copie l'entrée ici.

<!-- S20 -->
Et si l'entrée fait
cinq cents caractères de long ?
Le C ne demande pas.
Il continue simplement à écrire au-delà de la fin.

<!-- S21 -->
Et qu'y a-t-il juste après ces seize caractères ?
Souvent, quelque chose de très important.

<!-- S22 -->
Quand un programme appelle une fonction,
il note où revenir
une fois la fonction terminée.
Une adresse de retour.
Dans une disposition classique, elle se trouve
un peu après la fin de notre buffer.

<!-- S23 -->
Alors un attaquant envoie une entrée
d'exactement la bonne longueur.
D'abord, ses propres instructions.
Puis, tout à la fin, une nouvelle adresse de retour...
qui pointe vers ces instructions.

<!-- S24 -->
La fonction se termine.
Le processeur cherche où revenir...
et saute droit dans le code de l'attaquant.

<!-- S25 -->
Maintenant il exécute son programme à lui,
avec tous les droits de ton programme.
C'est ça que veut dire « exécuter du code arbitraire ».

<!-- S26 -->
Et le processeur n'a rien fait de mal.
Il a suivi les instructions.

<!-- S27 -->
En 1988, une erreur exactement comme celle-ci
a laissé le ver Morris se propager
sur l'internet de l'époque.
Et la même astuce est utilisée
dans des attaques depuis lors.

<!-- S28 -->
Alors les langages plus récents confient une partie du travail
au compilateur.
Rust, par exemple, refuse de compiler
beaucoup de programmes qui pourraient mal utiliser la mémoire.

<!-- S29 -->
Le programmeur dit :
mais je sais exactement ce que je fais !
Et le compilateur dit :
c'est ce que tout le monde dit.

<!-- S30 -->
Et il a raison de se méfier.
Microsoft et l'équipe Chrome de Google
ont toutes les deux rapporté
qu'environ soixante-dix pour cent
des failles de sécurité qu'elles ont étudiées
viennent de problèmes de sûreté de la mémoire.

<!-- S31 -->
Mais un programme peut être parfaitement sûr côté mémoire
et pourtant complètement faux.

<!-- S32 -->
Imagine qu'un utilisateur se connecte.
Son mot de passe est vérifié correctement.
Rien ne plante. Aucune mémoire n'est corrompue.

<!-- S33 -->
Et là, le programme lui montre
les données de quelqu'un d'autre.
Parce que la vérification des permissions
a été écrite un peu de travers.

<!-- S34 -->
Aucun langage ne peut détecter ça tout seul.
Le langage ne sait pas
ce que le programme était censé faire.
Nous seuls le savons.

<!-- S35 -->
Alors revenons aux tests.
Un test peut te dire :
pour cette entrée, j'ai obtenu ce résultat.

<!-- S36 -->
Il ne peut pas te dire :
le programme est correct pour toute entrée.
Et on a déjà vu
pourquoi on ne peut pas toutes les essayer.

<!-- S37 -->
En 1970, l'informaticien
Edsger Dijkstra l'a résumé en une phrase.
Les tests peuvent montrer la présence de bugs,
mais jamais leur absence.

<!-- S38 -->
Bon. Alors au lieu de tester,
pourquoi ne pas écrire un programme
qui vérifie d'autres programmes
et prouve qu'ils sont corrects ?
Donne-lui n'importe quel code, et il te dit
si ce code fait ce qu'il devrait.

<!-- S39 -->
Cette question a reçu sa réponse
avant même que le premier vrai ordinateur soit construit.
En 1936, Alan Turing a prouvé
qu'un tel programme ne peut pas exister.

<!-- S40 -->
Pas que personne ne l'ait encore construit.
Qu'il ne peut pas exister du tout.

<!-- S41 -->
Il a montré qu'aucun programme ne peut décider,
pour tout autre programme,
s'il finira un jour par s'arrêter.

<!-- S42 -->
Et en 1953, Henry Rice est allé plus loin.
La même chose vaut pour toute question non triviale
sur ce qu'un programme fait réellement.

<!-- S43 -->
Est-il sûr ? Laisse-t-il fuiter des données ?
Donne-t-il la bonne réponse ?
Il n'existe aucune méthode générale
qui tranche ça pour tout programme.

<!-- S44 -->
Alors un logiciel sans bugs, c'est impossible ?
Pas tout à fait.
Pour un programme bien précis,
on peut parfois prouver qu'il est correct,
au prix d'un effort énorme.

<!-- S45 -->
En 2009, une équipe en Australie a prouvé
qu'un petit noyau de système d'exploitation,
appelé seL4,
fait exactement ce que sa spécification dit.

<!-- S46 -->
Il faisait moins de dix mille lignes de code.
Construire le noyau a pris
environ deux années-personne.
Prouver qu'il était correct en a pris environ vingt.
Un navigateur web moderne
a des dizaines de millions de lignes.

<!-- S47 -->
Et même cette preuve a un hic.
Elle montre que le programme correspond à sa spécification.
Elle ne peut pas montrer que la spécification
est ce qu'on voulait vraiment.

<!-- S48 -->
Et la spécification est écrite par des gens.
Alors la question nous revient.

<!-- S49 -->
Et il n'y a pas que notre propre code.
Un programmeur aujourd'hui s'appuie sur des frameworks,
des bibliothèques et des centaines de dépendances.
Chaque couche nous épargne énormément de travail.
Mais chaque couche est quelque chose
qu'on doit comprendre...
ou au moins à qui faire confiance.

<!-- S50 -->
Ce qui veut dire que tu n'as pas besoin d'écrire un bug
pour en avoir un dans ton logiciel.
Il te suffit de l'installer.

<!-- S51 -->
Ajoute ensuite la pression.
Personne ne veut un produit parfait dans dix ans.
On en veut un qui marche le mois prochain.
Et une intrusion qui n'a jamais eu lieu
est très difficile à montrer dans une présentation.

<!-- S52 -->
Et voici le plus étrange.
Nos outils ne cessent de s'améliorer.
Des langages plus sûrs, du fuzzing, des primes pour trouver des failles...

<!-- S53 -->
Et pourtant le nombre de failles connues
ne cesse d'augmenter.
Rien qu'en 2024, environ quarante mille
ont reçu un numéro officiel.

<!-- S54 -->
En partie parce qu'on écrit aussi
bien plus de logiciels que jamais.
C'est comme rendre chaque route plus sûre...
tout en construisant des millions de fois plus de routes.

<!-- S55 -->
Alors les programmeurs sont-ils mauvais dans leur métier ?
Non.
On leur demande quelque chose
qu'aucune méthode générale ne peut garantir.

<!-- S56 -->
Alors peut-être que
« comment écrire un logiciel sans bugs ? »
est la mauvaise question.

<!-- S57 -->
La meilleure question, c'est :
comment construire des systèmes qui restent sûrs
même quand le logiciel a des bugs ?

<!-- S58 -->
Et c'est exactement là que va la sécurité.
Elle ne dit pas : ne fais jamais d'erreur.
Elle dit : suppose que tu en as déjà fait une.

<!-- S59 -->
Tu te souviens de cette adresse de retour ?
Aujourd'hui, le système la protège.
Il change au hasard l'emplacement des éléments en mémoire.
Et il refuse d'exécuter des instructions
cachées dans des données.

<!-- S60 -->
Le bug dans notre code C est toujours là.
Il est juste bien plus difficile à transformer en attaque.

<!-- S61 -->
Et la même idée est partout.
Bacs à sable, permissions limitées,
processus isolés, chiffrement,
sauvegardes, surveillance...
couche après couche,
pour qu'un seul bug ne devienne pas une catastrophe.

<!-- S62 -->
Et ça a une conséquence très concrète.
Si les bugs sont inévitables,
les corriger n'est pas optionnel.

<!-- S63 -->
Le logiciel que tu utilises aujourd'hui
pourrait bien contenir une faille
que personne n'a encore trouvée.

<!-- S64 -->
Et quand quelqu'un la trouve,
la mise à jour est la différence entre
« une faille a été découverte »
et « on s'est fait pirater ».

<!-- S65 -->
Il en va de même pour les systèmes qu'on construit.
Les vieilles bibliothèques et les plateformes non maintenues
ne deviennent pas plus sûres en étant ignorées.
Elles se transforment en dette technique.

<!-- S66 -->
Et pourquoi cette dette doit être remboursée,
c'est le sujet de ma vidéo
« Ça marche encore. Alors pourquoi le mettre à jour ? »
justement.

<!-- S67 -->
Parce que, en informatique,
« ça marche encore »
et « c'est encore sûr »
sont deux choses très différentes.
