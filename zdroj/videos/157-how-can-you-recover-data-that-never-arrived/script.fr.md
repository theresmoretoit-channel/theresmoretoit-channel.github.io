<!-- S01 -->
Voici un QR code.
Il contient une courte ligne de texte.

<!-- S02 -->
Le téléphone le lit tout de suite.

<!-- S03 -->
Maintenant, arrachons-en un morceau.

<!-- S04 -->
Et scannons-le à nouveau.
Le même texte.
Chaque lettre.

<!-- S05 -->
Une partie de ce code a disparu.
Ce n'est pas qu'elle est difficile à lire.
Elle a disparu.

<!-- S06 -->
Alors comment un téléphone peut-il lire
ce qui n'est plus là ?

<!-- S07 -->
Voici le même problème, en plus petit.
Quelqu'un vous envoie huit bits.
En route, trois d'entre eux se perdent.

<!-- S08 -->
Chaque bit manquant vaut zéro ou un,
il y a donc huit façons de combler les trous.
Et rien dans ce qui est arrivé
ne vous dit laquelle est la bonne.

<!-- S09 -->
Et pourtant, le téléphone vient de faire exactement ça.
Il ne devinait pas.
La réponse avait été envoyée
avant que quoi que ce soit ne se perde.

<!-- S10 -->
L'astuce, c'est d'envoyer plus
que le message lui-même.

<!-- S11 -->
Le plus simple,
c'est de tout dire trois fois.
Un zéro est envoyé sous forme de trois zéros,
un un sous forme de trois uns.

<!-- S12 -->
Le bruit inverse l'un d'eux,
et vous recevez un, zéro, un.
Deux voix contre une.
C'était presque sûrement un un.

<!-- S13 -->
Si le bruit inverse un bit sur dix,
au hasard et de façon indépendante,
un vote à trois se trompe
moins de trois fois sur cent.

<!-- S14 -->
Mais vous avez triplé
tout ce que vous envoyez.
Pour vous approcher de la perfection,
il faudrait répéter cinq fois, puis neuf,
puis cent...
et le message avancerait à pas de tortue.

<!-- S15 -->
Pendant longtemps,
ça semblait être le prix à payer.
Moins d'erreurs, des messages plus lents.
Gardez ça en tête.

<!-- S16 -->
À la fin des années 1940,
Richard Hamming, aux Bell Labs,
avait son propre problème.

<!-- S17 -->
Il avait surtout accès à un ordinateur à relais
le week-end,
quand personne n'était là pour le surveiller.

<!-- S18 -->
La machine savait repérer
quand elle s'était trompée.
Elle refaisait l'étape,
trois fois...
puis abandonnait son calcul.
Deux week-ends de suite,
il a perdu son travail.

<!-- S20 -->
Sa question, avec ses propres mots :
« Si la machine peut détecter
qu'il y a une erreur,
pourquoi ne peut-elle pas localiser où elle est ? »
Les termes exacts, a-t-il admis,
étaient sans doute un peu plus forts.

<!-- S22 -->
Sa réponse prend quatre bits de message
et ajoute trois bits de contrôle.
Sept bits en tout.

<!-- S23 -->
Chaque bit de contrôle surveille
un groupe différent de positions,
et s'assure que ce groupe
contient un nombre pair de uns.

<!-- S24 -->
Les groupes se chevauchent selon un motif bien précis.
Chaque position appartient
à sa propre combinaison de groupes.

<!-- S25 -->
Maintenant, inversez un bit.
Disons celui en position six.

<!-- S26 -->
Le récepteur refait les trois contrôles.
Le premier passe.
Le deuxième échoue.
Le troisième échoue.

<!-- S27 -->
Notez un contrôle échoué par un,
un contrôle réussi par zéro,
et lisez-les du dernier au premier.
Un, un, zéro.
En binaire, ça fait six.

<!-- S28 -->
Les contrôles ne disent pas seulement
que quelque chose s'est mal passé.
Ils désignent le bit exact.

<!-- S29 -->
Inversez-le à nouveau,
et le message redevient intact.
Personne n'a eu à renvoyer quoi que ce soit.

<!-- S30 -->
Voilà donc la réponse.
Le récepteur ne reconstruit pas
l'information perdue à partir de rien.
L'expéditeur l'avait glissée dedans,
à l'avance.

<!-- S32 -->
Tous les contrôles n'en sont pas capables.
Une somme de contrôle, comme dans notre vidéo
sur Btrfs,
peut vous dire qu'un bloc est endommagé,
mais pas quelles étaient les données d'origine.

<!-- S33 -->
Et il existe un second type de dommage.
Parfois, un bit n'est pas faux.
Il manque, tout simplement,
et vous savez exactement où se trouve le trou.

<!-- S34 -->
C'est ce qu'on appelle un effacement,
et les effacements sont plus faciles à corriger.

<!-- S35 -->
Envoyez quatre nombres,
4, 7, 2 et 9,
et un cinquième :
leur somme, 22.

<!-- S36 -->
Si l'un d'eux disparaît,
les autres permettent de retrouver sa valeur.
4, 7, quelque chose, 9,
22.
Ce ne peut être que 2.

<!-- S37 -->
Les serveurs protègent leurs disques
avec un contrôle du même genre,
réparti sur l'ensemble des disques.
Quand un disque lâche,
son contenu est recalculé à partir des autres.

<!-- S38 -->
Alors, combien faut-il en ajouter ?
La répétition répond :
pour ramener les erreurs à zéro,
il faut ramener la vitesse à zéro.

<!-- S39 -->
Deux ans avant la parution
de l'article de Hamming,
son collègue Claude Shannon
avait publié une réponse plus étrange.

<!-- S40 -->
Chaque canal,
une liaison radio, un câble, un disque,
a une limite.
Une vitesse maximale pour l'information.

<!-- S41 -->
En dessous de cette limite,
on peut rendre les erreurs aussi rares qu'on veut,
sans ralentir.
Pas en répétant davantage.
En codant plus intelligemment.

<!-- S42 -->
Au-dessus,
aucun code au monde n'y pourra rien.

<!-- S43 -->
Mais il y avait un hic.
Shannon a prouvé que de tels codes existent.
Il n'a pas montré comment en construire un
qu'on puisse réellement utiliser.

<!-- S44 -->
Sa preuve disait qu'un code choisi au hasard
serait presque sûrement bon.
Mais la façon évidente de le décoder
consiste à comparer ce qui est arrivé
avec chaque message possible...
et pour un bloc de 1 000 bits,
il y en a plus
qu'il n'y a d'atomes dans l'univers.

<!-- S46 -->
L'article de Shannon n'était donc pas une solution.
C'était une promesse.
Et les ingénieurs ont passé les
45 années suivantes à essayer de la tenir.

<!-- S47 -->
Le code de Hamming était un premier pas.
Il corrige un bit erroné sur sept.

<!-- S48 -->
Mais les vrais dommages arrivent en rafales.
Une rayure ou un grésillement de parasites
emporte des centaines de bits d'affilée.

<!-- S49 -->
En 1960, Irving Reed et Gustave Solomon,
au Lincoln Laboratory du MIT,
ont publié un article de cinq pages.

<!-- S50 -->
Leurs codes travaillent sur des octets entiers,
pas sur des bits isolés.
Si une rafale détruit les huit bits
d'un octet,
ça ne fait toujours qu'un seul octet erroné.

<!-- S51 -->
Une version courante ajoute
32 octets de contrôle
à 223
octets de données.

<!-- S52 -->
Elle peut corriger 16 octets quelconques
qui arrivent erronés...
ou en reconstruire 32
qui n'arrivent jamais.

<!-- S53 -->
C'est comme ça qu'un CD rayé se lit quand même.
Ses deux codes de Reed-Solomon
peuvent réparer entièrement un trou
d'environ 4 000 bits,
soit 2,5 millimètres de piste.

<!-- S54 -->
Et c'est pour ça que le QR code déchiré
fonctionnait encore.
À son niveau le plus élevé,
un QR code peut reconstruire
jusqu'à environ 30 % de ses octets
et rendre quand même chaque lettre.

<!-- S56 -->
Voyager 2 a quitté la Terre en 1977
avec déjà un encodeur Reed-Solomon à bord.

<!-- S57 -->
Mais à Jupiter et Saturne,
elle protégeait tout sauf les images
avec un code plus ancien, de Marcel Golay,
qui envoyait un bit supplémentaire
pour chaque bit de données.

<!-- S58 -->
Pour Uranus et Neptune,
avec un signal de plus en plus faible,
les ingénieurs ont activé Reed-Solomon,
par-dessus un second code
par lequel passait déjà chaque bit.

<!-- S59 -->
Avec ce second code seul,
environ cinq bits sur mille
étaient encore faux.
Avec Reed-Solomon par-dessus,
environ un sur un million.

<!-- S60 -->
Le bruit arrive aussi en rafales,
alors Voyager mélangeait
les octets de quatre blocs
avant de les envoyer.

<!-- S61 -->
Une rafale qui aurait détruit un bloc
n'enlève plus que quelques octets à chacun...
assez peu pour que chaque bloc
puisse se réparer lui-même.

<!-- S62 -->
Le reste du voyage des images de Neptune
jusqu'à la Terre
est dans notre vidéo sur Voyager.

<!-- S63 -->
Mais même ça
n'atteignait pas encore la limite de Shannon...
et un code capable de s'en approcher bien plus
existait déjà.

<!-- S65 -->
En 1960, dans sa thèse de doctorat au MIT,
Robert Gallager a décrit des codes
faits de nombreux contrôles simples,
chacun ne regardant que quelques bits.

<!-- S66 -->
Pour les décoder, les contrôles devaient
s'échanger des hypothèses,
tour après tour...
bien trop
pour les ordinateurs des années 1960.
L'idée a donc été mise de côté,
et en grande partie oubliée pendant 30 ans.

<!-- S68 -->
En 1993,
une équipe menée par deux ingénieurs français,
Claude Berrou et Alain Glavieux,
a présenté les turbocodes
lors d'une conférence à Genève.

<!-- S69 -->
Leurs résultats étaient si proches
de la limite de Shannon
que beaucoup d'experts ont supposé
qu'ils s'étaient trompés.
Sans doute d'un facteur deux,
quelque part dans leurs calculs.

<!-- S70 -->
En moins d'un an,
d'autres laboratoires l'avaient confirmé.

<!-- S71 -->
Les turbocodes fonctionnaient eux aussi
en s'échangeant des hypothèses,
et ça a ramené les chercheurs vers Gallager.

<!-- S72 -->
En 1995 et 1996,
David MacKay et Radford Neal
ont redécouvert ses codes
et montré qu'ils pouvaient s'approcher
tout autant.

<!-- S73 -->
En 2001,
une version améliorée des codes de Gallager
est arrivée à 0,04 décibel
de la limite de Shannon.

<!-- S74 -->
C'est moins d'un pour cent
de puissance de signal en plus
que le minimum théorique.
La promesse de 1948 avait été tenue.

<!-- S75 -->
Aujourd'hui, les codes de Gallager transportent
une grande partie des données des téléphones 5G,
du Wi-Fi moderne
et de la télévision par satellite.

<!-- S77 -->
Revenons maintenant à nos huit bits.
Trois se sont perdus,
et il y a huit façons
de combler les trous.

<!-- S78 -->
Mais ces huit bits
n'ont jamais été un simple message.
Ils portaient quatre bits de données,
les trois contrôles de Hamming,
et un contrôle de plus sur les huit.

<!-- S79 -->
Sur les 256
combinaisons possibles de huit bits,
seules 16 respectent ces règles.

<!-- S80 -->
Testez les huit candidats.
Un par un, ils échouent.
Il n'en reste qu'un.

<!-- S81 -->
Les bits manquants n'avaient jamais vraiment disparu.
Leur information était toujours là,
dans les bits qui ont survécu.

<!-- S82 -->
Alors, voici une question pour vous.
Avez-vous déjà remarqué la correction d'erreurs
à l'œuvre dans quelque chose que vous utilisez tous les jours ?
Dites-le-moi dans les commentaires.
