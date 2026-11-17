<!-- S01 -->
Vous ouvrez un terminal.
Quelqu'un passe derrière vous.
Il voit un écran noir
couvert de texte mystérieux.
Et soudain...

<!-- S02 -->
« Oh mon Dieu ! Tu es en train de pirater ! »

<!-- S03 -->
Eh bien...
Peut-être.
Ou peut-être cherchez-vous simplement
pourquoi le serveur est tombé.

<!-- S04 -->
Aujourd'hui, nous allons voir pourquoi
les terminaux et le piratage sont devenus
presque la même chose dans la culture populaire.
Et, plus important encore...
à quoi ressemble vraiment le piratage.

<!-- S05 -->
Pour la plupart des gens, un ordinateur a des boutons.
Vous cliquez sur quelque chose.
Il se passe quelque chose.
Et puis il y a le terminal.
Pas de boutons.
Pas de messages aimables.
Juste ça.
Et c'est terrifiant.

<!-- S06 -->
Une interface graphique peut dire :
supprimer l'utilisateur.
Un terminal dit ceci à la place.

<!-- S07 -->
Pour un utilisateur de Linux expérimenté,
c'est parfaitement banal.
Pour tous les autres, on dirait
que vous allez lancer un missile.

<!-- S08 -->
Il y a en fait une raison historique
à cette apparence.
Les premiers ordinateurs n'avaient pas d'interface graphique.
On leur parlait par des terminaux de texte.

<!-- S09 -->
Et ces terminaux avaient des écrans sombres
avec du phosphore vert ou ambre.
Ce n'était pas une tentative de faire moderne.
C'est simplement ainsi que la technique fonctionnait.

<!-- S10 -->
Mais le cinéma et la télévision
ont alors remarqué quelque chose d'utile.
Un écran noir rempli de
texte qui défile vite paraît technique.
Et, plus important encore...
il paraît compliqué.

<!-- S11 -->
Vous n'avez pas besoin de comprendre
ce que signifient les caractères.
Vous voyez simplement ceci.
Et votre cerveau décide :
cette personne fait quelque chose d'illégal.

<!-- S12 -->
Hollywood a mis au point un langage
remarquablement uniforme pour le piratage.
Le hacker est assis dans une pièce sombre.
Il y a six écrans.

<!-- S13 -->
La pièce n'est éclairée que par les écrans.
Personne n'a allumé la lumière.
Le hacker se met à taper
à environ neuf cents mots par minute.

<!-- S14 -->
Le texte défile à toute allure.
Une barre de progression apparaît.
Quatre-vingt-dix-sept pour cent.
Quatre-vingt-dix-huit.
Quatre-vingt-dix-neuf.
Et enfin, cent.
Le hacker se recule dans son fauteuil.
Et dit...

<!-- S15 -->
« Je suis dedans. »

<!-- S16 -->
Ce n'est pas ainsi que se déroulent la plupart
des incidents de sécurité.
Imaginons la vraie conversation.
« Je vais pirater ce serveur. »
Et le serveur répond :
permission denied.

<!-- S17 -->
« Ah. »
Il réessaie.
Permission denied.
Il vérifie le mot de passe.

<!-- S18 -->
Il lit la documentation.
Il cherche le message d'erreur.
Il finit par découvrir que l'administrateur
a désactivé la connexion par mot de passe il y a six mois.

<!-- S19 -->
« D'accord. »

<!-- S20 -->
Les ordinateurs sont remarquablement doués pour vous
faire passer vingt minutes à découvrir que vous
avez oublié un seul caractère dans un fichier de configuration.

<!-- S21 -->
D'un côté de l'écran :
administrateur système.
De l'autre :
hacker.
Les mêmes outils peuvent apparaître des deux côtés.
C'est parce que le terminal
n'est pas un outil de piratage.
C'est une interface.

<!-- S22 -->
Vous pouvez vous en servir pour faire tourner un serveur,
lire des journaux, copier des fichiers, installer des logiciels,
ou comprendre ce qui a cassé à trois heures du matin.

<!-- S23 -->
Ou, selon ce que vous faites
et selon que vous en avez l'autorisation,
vous pouvez vous en servir pour tester la sécurité.
Ou pour une attaque.

<!-- S24 -->
L'outil lui-même ne vous dit pas
lequel des deux vous êtes en train de faire.
Un tournevis peut réparer un ordinateur.
Il peut aussi en détruire un.
Le tournevis n'est pas le coupable.

<!-- S25 -->
Alors, qu'est-ce qu'un hacker au juste ?
Le mot a une histoire bien plus ancienne
que la cybercriminalité moderne.

<!-- S26 -->
À l'origine, un hacker était quelqu'un
qui aimait explorer les systèmes
et savait trouver des solutions inattendues.

<!-- S27 -->
Avec le temps, le mot s'est attaché
à la sécurité informatique.
Et aujourd'hui, quand quelqu'un dit
« c'est un hacker », cela peut désigner

<!-- S28 -->
un chercheur en sécurité,
un testeur d'intrusion,
un véritable attaquant,
ou simplement quelqu'un qui en sait
une quantité inquiétante sur Linux.
En général, le contexte aide.

<!-- S29 -->
Revenons à notre image.
La légende dit :
tu l'as piraté.
Et regardez ses écrans.

<!-- S29b -->
Sur l'un, quelque chose comme nmap.
Sur l'autre, quelque chose qui a l'air
encore plus suspect.
Slash etc slash passwd.

<!-- S30 -->
Pour quelqu'un qui ne connaît pas Linux,
elle est manifestement en train d'entrer au Pentagone.
Pour un administrateur système, elle vérifie
le réseau et lit une liste de comptes.

<!-- S31 -->
Et c'est de là que vient la blague.
Cette femme ne pirate peut-être rien du tout.
Elle fait peut-être simplement son travail.

<!-- S32 -->
Alors que fait vraiment nmap ?
C'est un outil de découverte de réseau
et d'audit de sécurité.

<!-- S33 -->
En termes très simples,
vous le pointez vers une machine et vous demandez
ce que cet ordinateur
expose au réseau.

<!-- S34 -->
Il peut vous dire que certains ports sont ouverts.
Et les ports correspondent à des services réseau.
Ce n'est pas automatiquement une attaque.

<!-- S35 -->
Cela ressemble plutôt à regarder un bâtiment
et à demander quelles portes sont ouvertes.
Si c'est votre bâtiment,
c'est de l'administration normale.

<!-- S36 -->
Si c'est celui de quelqu'un d'autre
et que vous cherchez délibérément
un moyen d'entrer...

<!-- S37 -->
eh bien, c'est une autre histoire.

<!-- S38 -->
Et ce chemin de fichier, alors ?
Quelqu'un pourrait penser :
elle lit le fichier des mots de passe.
Il contient bien des informations sur les comptes.

<!-- S39 -->
Mais sur un système Linux moderne,
les empreintes des mots de passe sont stockées ailleurs.
Elles sont dans slash etc slash shadow,
qui est beaucoup plus protégé.

<!-- S40 -->
Voir ce fichier n'est donc pas la même chose
que découvrir les mots de passe de tout le monde.
Hollywood, bien sûr,
en ferait quelque chose de bien plus dramatique.

<!-- S41 -->
Un administrateur Linux dirait :
c'est littéralement une liste d'utilisateurs.

<!-- S42 -->
Une autre scène classique casse un mot de passe
en quatorze secondes environ.
Le vrai cassage est plus ennuyeux.
Vous avez une empreinte, vous avez un dictionnaire,
et vous laissez l'ordinateur essayer des candidats.

<!-- S43 -->
Peut-être en trouve-t-il un en une minute.
Peut-être en une semaine.
Peut-être jamais.
Et pendant qu'il travaille, l'attaquant
n'est pas assis là à taper.
Il mange peut-être un sandwich.

<!-- S44 -->
Ce qui m'amène à ma tradition
hollywoodienne préférée.
Les ordinateurs n'acceptent apparemment pas les commandes
si on ne les tape pas extrêmement vite.

<!-- S45 -->
Les vrais programmeurs et administrateurs
ne tapent pas en permanence.
Ils réfléchissent.
Ils lisent.
Ils fixent un message d'erreur.

<!-- S46 -->
Puis ils découvrent que quelqu'un
l'a résolu il y a onze ans.
Et ils copient la solution.

<!-- S47 -->
Voilà l'informatique.

<!-- S48 -->
Parfois, la chose la plus dangereuse
que vous puissiez taper n'est pas
une mystérieuse commande de piratage.
C'est quelque chose de parfaitement légitime.

<!-- S49 -->
L'exemple célèbre, c'est celui-ci.

<!-- S50 -->
Ce qui est une histoire magnifique,
sauf qu'un système moderne refuse.
Il répond qu'une opération récursive
sur le slash est dangereuse,
sauf si vous ajoutez une option disant que c'est voulu.

<!-- S51 -->
Les commandes qui détruisent vraiment
sont plus ennuyeuses.
Une suppression dans le mauvais répertoire.
Un disque écrit par-dessus le mauvais disque.

<!-- S52 -->
De celles-là, le terminal ne vous avertit pas,
car pour autant qu'il puisse en juger,
rien ne cloche.
Il peut seulement demander : êtes-vous absolument sûr ?

<!-- S53 -->
Et si vous répondez oui...
il vous croira peut-être.

<!-- S54 -->
Et voici le plus gros problème
du cliché hollywoodien.
Une vraie attaque peut ne pas
ressembler du tout à du piratage.

<!-- S55 -->
Cela peut être un mot de passe volé.
De l'hameçonnage.
Un serveur non mis à jour.
Une clé d'API divulguée.
Un mot de passe réutilisé d'ailleurs.

<!-- S56 -->
L'attaquant n'a peut-être même pas besoin
d'un terminal.
Il se connecte peut-être simplement
à une interface web.
Identifiant.
Mot de passe.
Et le voilà à l'intérieur.

<!-- S57 -->
Pas de texte vert.
Pas de graphismes façon Matrix.
Pas de musique dramatique.

<!-- S58 -->
Ce qui est sans doute bien plus effrayant.

<!-- S59 -->
On imagine un hacker comme un sweat à capuche,
une pièce sombre et un clavier lumineux.
Rien de tout cela n'a de rapport avec le piratage.

<!-- S60 -->
La personne assise à côté de vous dans le train,
avec un ordinateur portable tout à fait ordinaire,
en sait peut-être bien davantage
sur la sécurité informatique.

<!-- S61 -->
Et la personne assise
devant six serveurs
cherche peut-être simplement à comprendre
pourquoi la base de données ne démarre pas.

<!-- S62 -->
Revenons donc à notre image de départ.
L'homme pointe la femme du doigt.
Tu l'as piraté.
Était-elle en train de pirater ?

<!-- S63 -->
Peut-être.
Peut-être pas.

<!-- S64 -->
Elle a un terminal.
Elle a nmap.
Elle a une liste de comptes.
Mais rien de tout cela ne prouve
qu'elle a piraté quoi que ce soit.
Elle pourrait être l'administratrice
ou mener un audit de sécurité.

<!-- S65 -->
Ou elle pourrait vraiment être en train de pirater.
Nous n'en savons rien.
Et c'est ça, la blague.

<!-- S66 -->
La vraie différence entre
l'administration ordinaire et le piratage
n'est pas la couleur de votre terminal.
Ce n'est pas le nombre d'écrans que vous avez.

<!-- S67 -->
Ce n'est pas la vitesse à laquelle vous tapez.
Et ce n'est certainement pas
le fait de porter un sweat à capuche.
C'est ce que vous faites
et si vous avez l'autorisation de le faire.

<!-- S68 -->
Alors, la prochaine fois que vous verrez quelqu'un
fixer un écran noir
plein de texte mystérieux,
ne supposez pas qu'il pirate.

<!-- S69 -->
Il répare peut-être simplement le serveur.

<!-- S70 -->
Cela dit...
s'il tape neuf cents mots
par minute en criant
« je suis dedans »...

<!-- S71 -->
vous voudrez peut-être lui demander
ce qu'il est en train de faire.
