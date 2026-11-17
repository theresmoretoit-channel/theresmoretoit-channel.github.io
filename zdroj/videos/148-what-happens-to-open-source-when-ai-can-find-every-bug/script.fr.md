<!-- S01 -->
948.
C'est le nombre de façons distinctes qu'une IA a trouvées
pour prendre le contrôle d'un ordinateur Linux de l'intérieur.

<!-- S02 -->
Aucun mot de passe volé. Aucune intrusion à distance.
Chacune commence par un utilisateur ordinaire
qui n'a aucun droit particulier,
et se termine par root,
le compte qui peut tout faire.

<!-- S03 -->
OpenAI a publié le résultat en novembre 2026.
L'opération entière a coûté
1,2 million de dollars en crédits d'API.

<!-- S05 -->
Ce sont les propres chiffres d'OpenAI,
publiés la veille
du lancement du modèle qui les a produits,
et personne d'extérieur n'a confirmé le décompte complet.
Mais des centaines de signalements et de correctifs
ont déjà été envoyés.

<!-- S06 -->
Voici pourquoi cela dépasse Linux.
Le code source de Linux est public.
N'importe qui peut le lire.
Pendant des décennies, c'était l'argument
qui expliquait pourquoi il est sûr.

<!-- S07 -->
Alors, si une machine peut lire du code public
et en tirer des exploits fonctionnels à cette échelle,
les logiciels devraient-ils finalement garder leur code secret ?

<!-- S08 -->
Regardons un logiciel qui le fait déjà.
En avril 2026, Microsoft a corrigé
164 failles de sécurité
lors de sa journée mensuelle de correctifs.
En octobre, il en a corrigé
1 413.

<!-- S09 -->
Ce seul mois, il en a corrigé davantage
qu'au cours de n'importe quelle année entière auparavant.
Plus de 1 000 de ces correctifs concernaient Windows,
et Microsoft avait prévenu
que ses propres outils d'IA allaient provoquer cette hausse.

<!-- S10 -->
On ne peut pas comparer directement les deux chiffres.
Les entreprises ne comptent pas de la même façon,
et Microsoft fouillait son propre code privé.

<!-- S11 -->
Mais cela montre une chose.
Garder le code privé
n'avait pas tenu les bugs à l'écart.

<!-- S12 -->
Alors, qu'est-ce qui te protège vraiment ?
Pour y répondre,
il faut voir comment fonctionne cette machine,
car chacune de ses étapes laisse quelque chose de côté.

<!-- S13 -->
Le noyau Linux compte
plus de 40 millions de lignes de code.
D'abord, des agents éclaireurs l'ont parcouru
et ont sélectionné les parties
qu'un utilisateur ordinaire peut réellement atteindre.

<!-- S14 -->
Il en est resté environ 7 %.
C'est la partie qu'ils ont jugée digne d'être attaquée,
pas un échantillon aléatoire,
donc tu ne peux pas multiplier le résultat par 14.

<!-- S15 -->
Ensuite, des agents analystes ont passé ce code en revue
et ont relevé tout ce qui était suspect.
2 308 candidats,
en 12 heures.

<!-- S16 -->
Mais un soupçon ne prouve rien.
D'autres agents ont donc écrit des programmes de test
et les ont lancés sur des machines virtuelles isolées.
1 724 bugs
se sont révélés réels.

<!-- S17 -->
Puis est venue la partie coûteuse :
construire des exploits fonctionnels,
avec les protections standard
d'un système de bureau normal activées.
1 169
ont atteint root.

<!-- S18 -->
Regroupe-les selon la faille sous-jacente,
et tu obtiens les 948.

<!-- S19 -->
Il y a un détail dans le rapport
qu'on a du mal à oublier.
Lors d'une des premières exécutions,
les agents ont annoncé 200 succès.
Puis des humains ont vérifié comment ils y étaient arrivés.

<!-- S20 -->
Vingt d'entre eux avaient atteint root
par un autre bug inconnu,
et non celui qu'on leur avait demandé d'utiliser.
Envoyés pour ouvrir une porte,
ils en ont trouvé une autre que personne ne connaissait.

<!-- S21 -->
Dans un échantillon de ses exploits,
OpenAI a identifié dix techniques d'exploitation
que les experts extérieurs n'avaient jamais vues.

<!-- S22 -->
En juillet, un modèle plus ancien
avait trouvé 166 de ces failles.
Trois mois de correctifs plus tard,
le nouveau modèle en a trouvé 948.
Les bugs ne s'étaient pas épuisés.
L'exécution suivante en a trouvé bien plus.

<!-- S23 -->
Il y a cependant une limite importante.
Rien de tout cela ne pénètre dans ton ordinateur
par Internet.
L'attaquant doit déjà se trouver sur la machine,
en tant qu'utilisateur ordinaire.

<!-- S24 -->
C'est moins rassurant qu'il n'y paraît,
car les vraies attaques se font souvent en deux temps.
D'abord, on entre,
par une faille du navigateur ou un téléchargement malveillant.
Ensuite, il faut root.
Ceci, c'est la deuxième étape.

<!-- S25 -->
Le conseil d'OpenAI est sans détour.
Sur un système sans les derniers correctifs,
considère tout compte ordinaire comme root,
du moins face à un attaquant disposant de gros moyens.

<!-- S26 -->
Alors, que devient
le vieil argument en faveur du code ouvert ?
À la fin des années 1990,
Eric Raymond en a fait un slogan :
« Avec suffisamment d'yeux, tous les bugs sont superficiels. »

<!-- S27 -->
Il l'a appelé la loi de Linus.
C'est une belle idée, qui cache une hypothèse :
que quelqu'un regarde vraiment.

<!-- S28 -->
En 2014, un bug baptisé Heartbleed
a été découvert dans OpenSSL,
le code qui protégeait une énorme partie du web.
Environ un demi-million de serveurs sécurisés
étaient considérés comme exposés.

<!-- S29 -->
Le bug dormait dans du code public depuis deux ans.
Le projet recevait
environ 2 000 dollars de dons par an
et ne comptait qu'un seul développeur à plein temps.

<!-- S30 -->
Tout le monde pouvait le lire.
Presque personne ne l'a fait.

<!-- S31 -->
C'était depuis toujours la vraie faiblesse de l'open source.
Pas trop d'yeux sur le code. Trop peu.

<!-- S32 -->
Et c'est justement ce que l'IA change.
Une machine peut continuer à analyser
et examiner bien plus de candidats
qu'un chercheur humain ne pourrait en traiter seul.
La vieille promesse est enfin tenue,
pour tout le monde, attaquants compris.

<!-- S33 -->
Le code public est donc vraiment examiné, désormais.
Le cacher, est-ce que ça aide ?

<!-- S34 -->
Un programme fermé doit quand même s'exécuter,
donc son code machine se trouve
sur chaque ordinateur qui l'utilise.
Des outils comme Ghidra le retransforment
en quelque chose qui ressemble à du code source.

<!-- S35 -->
Et il existe une astuce classique.
Compare un programme
avant et après une mise à jour de sécurité.
Ce qui a changé te montre où se trouvait la faille.

<!-- S35b -->
Cela indique aux attaquants où viser,
bien avant que tous les systèmes
aient installé la mise à jour.

<!-- S36 -->
Anthropic a essayé sur le noyau de Windows,
avec 21 failles
que Microsoft venait de corriger,
et sans le code source.
L'IA a obtenu son premier plantage en 31 minutes.
En six heures, elle en avait 18.

<!-- S37 -->
Huit sont devenus des exploits fonctionnels
capables de prendre le contrôle total de la machine,
pour environ 2 000 dollars chacun.

<!-- S38 -->
Mais ce n'étaient pas des bugs inconnus.
Les correctifs indiquaient déjà
où se trouvaient les problèmes.
Trouver une faille nouvelle à partir de rien est plus difficile.

<!-- S39 -->
Le secret coûte donc encore quelque chose à l'attaquant.
C'est un ralentisseur, pas un mur.
Quelle est la hauteur du ralentisseur ?
Il n'existe aucun chiffre public.

<!-- S40 -->
Et de l'autre côté ?
Qu'est-ce que l'ouverture t'apporte vraiment ?
La réponse se trouve dans un petit détail
du rapport d'OpenAI.

<!-- S41 -->
Pendant les dix jours de cette analyse,
plus de 100 de ces failles de Linux
ont été corrigées, ou étaient sur le point de l'être,
par d'autres personnes.
Environ 300 autres
étaient déjà discutées publiquement.

<!-- S42 -->
D'autres trouvaient les mêmes bugs
au même moment.

<!-- S43 -->
Linus Torvalds l'avait déjà décrit en mai.
Il disait que les signalements produits par IA
avaient rendu la liste de diffusion sécurité du noyau
« presque entièrement ingérable »,
parce que différentes personnes trouvaient sans cesse
les mêmes choses avec les mêmes outils.

<!-- S44 -->
Et son conseil était le suivant :
« Si tu as trouvé un bug avec des outils d'IA,
il y a de fortes chances que quelqu'un d'autre l'ait trouvé aussi. »

<!-- S45 -->
Les règles du noyau le disent désormais clairement.
Un bug trouvé avec l'IA doit être considéré comme public,
car plusieurs chercheurs
tombent sur les mêmes bugs,
souvent le même jour.

<!-- S46 -->
Pense à ce que cela fait
à l'idée d'un bug secret.
Si le trouver t'a coûté peu,
ça a coûté peu à tout le monde.

<!-- S47 -->
Avec l'open source,
n'importe qui peut examiner le signalement,
vérifier le correctif et contester le résultat.
Avec un logiciel fermé,
tu dois surtout faire confiance à l'éditeur.

<!-- S49 -->
Mais l'ouverture a un prix,
et ce n'est pas celui que tu imagines.
On est tenté de dire
qu'un petit projet n'a pas les moyens de payer l'analyse.
Les entreprises d'IA proposent déjà
un accès gratuit aux mainteneurs.

<!-- S50 -->
Ce qui manque, ce sont des gens.
Le noyau enregistrait autrefois
environ 500 problèmes de sécurité par version.
Cette année, il a dépassé les 1 500.
Beaucoup sont mineurs,
mais quelqu'un doit quand même les examiner.

<!-- S51 -->
En janvier, le projet curl
a mis fin à son programme de primes aux bugs,
pour cesser de récompenser un flot de signalements bidon.

<!-- S52 -->
Même les bons signalements ne font que déplacer le travail.
Les correctifs générés par IA ont toujours besoin d'une relecture humaine.
Certains des premiers correctifs ajoutaient du code inutile
ou passaient à côté d'autres variantes du même bug.

<!-- S53 -->
Tu peux acheter plus d'analyse.
Tu ne peux pas acheter plus de gens
qui comprennent aussi bien un morceau de code.
Là, une entreprise avec une équipe de sécurité rémunérée
a vraiment un avantage.

<!-- S54 -->
Et puis vient le dernier problème.
Corrigé ne veut pas dire installé.

<!-- S55 -->
En mars 2017,
Microsoft a corrigé une faille dans Windows.
Code fermé, un seul éditeur, un seul système de mise à jour.
Deux mois plus tard,
WannaCry est passé par cette même faille,
dans quelque 200 000 ordinateurs
répartis dans environ 150 pays.

<!-- S56 -->
Ce correctif avait eu deux mois pour se diffuser,
et ça n'a pas suffi.
Un attaquant ne te laissera peut-être plus deux mois.
Dans la même étude d'Anthropic,
l'IA a pris un correctif public
du moteur JavaScript de Firefox
et a obtenu un exploit fonctionnel en moins d'une heure.

<!-- S57 -->
La version corrigée de Firefox
n'arriverait que 18 jours plus tard.

<!-- S58 -->
C'est le danger de la publication d'un correctif.
L'information peut atteindre les attaquants
avant que la mise à jour ne t'atteigne.

<!-- S59 -->
Un correctif Linux a un long chemin à parcourir,
du noyau à une version stable,
puis à ta distribution, puis à ton appareil.
Un téléphone peut attendre des mois, voire indéfiniment.

<!-- S60 -->
Et les logiciels fermés n'y échappent pas.
On vient de le voir : le correctif de Windows a suffi.
Chaque mise à jour est désormais aussi une carte.

<!-- S60b -->
Alors garde tout à jour,
ton ordinateur, ton téléphone, même ton routeur,
et installe les mises à jour dès qu'elles arrivent.
À mesure que l'IA transforme mieux les correctifs en attaques,
chaque jour d'attente comptera davantage.

<!-- S61 -->
Alors, l'open source est-il toujours plus sûr ?
Honnêtement, personne n'en sait rien.
À ce que l'on sait publiquement,
personne n'a mené le même test des deux côtés,
avec les mêmes règles.

<!-- S62 -->
Ce qu'on peut dire est plus modeste.
Cacher le code protège moins qu'avant.
Le montrer permet à chacun de vérifier le travail,
et fait peser encore plus de ce travail
sur ceux qui maintiennent le code.

<!-- S64 -->
Même si l'IA ne trouve jamais tous les bugs,
elle a déjà changé ce que coûte leur recherche.

<!-- S65 -->
Ce qui compte désormais, c'est combien de temps une faille reste ouverte
entre le moment où quelqu'un la trouve
et le moment où elle est refermée sur ta machine.

<!-- S66 -->
Alors voici une question pour toi.
Si n'importe quel bug peut être trouvé par n'importe qui,
tu préférerais faire confiance à du code que tu peux lire,
ou à une entreprise payée pour le corriger ?
Dis-le-moi dans les commentaires.
