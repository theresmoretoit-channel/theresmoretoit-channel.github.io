<!-- S01 -->
Quelque part chez toi,
il y a peut-être une horloge
que personne n'a jamais réglée.

<!-- S02 -->
Elle survit aux coupures de courant.
Elle passe à l'heure d'été et à l'heure d'hiver
toute seule, en pleine nuit.

<!-- S03 -->
Elle n'a aucune connexion internet.
Pas de wifi, pas de GPS,
pas d'appli sur ton téléphone.

<!-- S04 -->
Elle n'a qu'un minuscule récepteur radio.
Et une fois par seconde,
elle entend une seule impulsion.

<!-- S05 -->
Alors comment une horloge
transforme-t-elle une impulsion par seconde
en heure exacte, en date,
et même en jour de la semaine ?

<!-- S06 -->
En Europe, ces impulsions viennent
de DCF77, près de Francfort.
En Amérique, de WWVB, dans le Colorado.
Des émetteurs différents, la même idée.

<!-- S07 -->
Prenons l'allemand.
Il émet une onde radio continue,
jour et nuit.
Et au début de chaque seconde,
il baisse brièvement cette onde.

<!-- S08 -->
Toute l'astuce, c'est combien de temps
elle reste baissée.

<!-- S09 -->
Une baisse d'un dixième de seconde
signifie zéro.
Une baisse de deux dixièmes signifie un.

<!-- S10 -->
C'est tout le principe.
Pas de paquets, pas de réseau.
Juste une onde radio qui baisse
un court instant, ou un peu plus longtemps.

<!-- S11 -->
Un bit par seconde.
Ce qui veut dire qu'il faudrait une minute entière
pour envoyer seulement 60 bits.

<!-- S12 -->
Et en fait, il n'en envoie que 59.

<!-- S13 -->
Pendant la dernière seconde de chaque minute,
l'onde ne baisse pas du tout.
Et cette baisse manquante
est la partie la plus importante
de tout le signal.

<!-- S14 -->
Parce que quand la baisse suivante arrive,
l'horloge sait
qu'une nouvelle minute vient de commencer.

<!-- S15 -->
Le trou fonctionne comme un point.
Tout ce qui se trouve entre deux trous
forme une phrase complète.

<!-- S16 -->
Alors, que peut contenir une phrase
de 59 bits ?

<!-- S17 -->
La minute. L'heure.
Le jour du mois, le jour de la semaine,
le mois et l'année.

<!-- S18 -->
La plupart des nombres sont envoyés chiffre par chiffre.
47 minutes
ne sont pas envoyées comme 47.
Elles sont envoyées comme deux chiffres séparés,
un 4 et un 7.

<!-- S19 -->
4 bits suffisent pour n'importe quel chiffre
de 0 à 9.
Les dizaines de minutes ne dépassent jamais 5,
alors elles n'en ont que 3.

<!-- S20 -->
Et l'année n'a droit qu'à deux chiffres.
Pour l'émetteur,
2026, c'est simplement 26.
L'horloge ajoute le siècle elle-même.

<!-- S21 -->
Mais la radio n'est pas un canal propre.
Un moteur, un chargeur de téléphone,
une ampoule LED bon marché...
n'importe lequel peut brouiller une baisse.

<!-- S22 -->
Alors après chaque bloc de nombres
vient un bit de plus, appelé bit de parité.

<!-- S23 -->
On le choisit pour que le nombre de bits à 1
dans le bloc soit toujours pair.

<!-- S24 -->
Si une interférence inverse un seul bit,
le compte devient impair,
et l'horloge sait
que quelque chose a mal tourné.

<!-- S25 -->
Mais si deux bits s'inversent,
le compte redevient pair,
et l'erreur passe inaperçue.

<!-- S26 -->
C'est pour ça que beaucoup d'horloges
ne se fient pas à une seule minute.
Elles en attendent une autre valide.

<!-- S27 -->
Et c'est pour ça que se régler toute seule
peut prendre plusieurs minutes,
et, un mauvais jour, beaucoup plus.

<!-- S28 -->
Ce qui pose un drôle de problème.

<!-- S29 -->
L'horloge passe une minute entière
à recueillir l'heure de 10:48.
Mais pendant qu'elle recueille ce message,
il est encore 10:47.

<!-- S30 -->
Alors, quand change-t-elle vraiment ?

<!-- S31 -->
Parce que le message est une annonce.
Il dit quelle heure il sera
quand la minute suivante commencera.

<!-- S32 -->
L'horloge lit toute la phrase,
attend la fin de la baisse manquante,
et quand la baisse suivante arrive,
c'est elle, l'instant exact.

<!-- S33 -->
Les bits disent à l'horloge quelle heure il est.
La baisse lui dit quand.

<!-- S34 -->
Mais la phrase contient quelques mots de plus
que l'heure.

<!-- S35 -->
Deux bits indiquent si l'Allemagne
est à l'heure d'hiver ou à l'heure d'été.

<!-- S36 -->
Et un troisième est un avertissement.
Pendant toute l'heure qui précède le changement,
il est mis à 1.

<!-- S37 -->
Ton horloge n'a donc pas besoin de savoir
quel dimanche de mars
on avance l'heure,
ni quel dimanche d'octobre on la recule.
Personne ne lui a jamais appris la règle.
On la prévient, tout simplement, une heure à l'avance.

<!-- S38 -->
Si l'Europe arrête un jour de changer d'heure,
l'avertissement ne viendra tout simplement plus jamais.

<!-- S39 -->
Un autre bit servait à annoncer une seconde intercalaire,
une seconde ajoutée de temps en temps,
parce que la rotation de la Terre
n'est pas parfaitement régulière.
Cette minute-là pouvait compter 61 secondes.

<!-- S40 -->
La dernière a été ajoutée
fin 2016.
Mais en octobre 2026,
les instances mondiales de métrologie
ont décidé de supprimer les secondes intercalaires.
À partir du 20 mai 2027,
l'UTC s'écoulera sans interruption.

<!-- S41 -->
Et les 14 premiers bits
de chaque minute
ne parlent pas du tout de l'heure.

<!-- S42 -->
Depuis 2006, ils servent aussi
à transmettre des prévisions météo chiffrées
pour les stations météo compatibles.

<!-- S43 -->
Le signal qui règle ton réveil
pouvait donc aussi dire
à la station météo de quelqu'un d'autre
s'il allait pleuvoir jeudi.

<!-- S44 -->
Et pourtant, la plupart de ces horloges
n'écoutent pas en permanence.
Écouter, ça use la pile,
alors beaucoup essaient une fois par nuit,
au petit matin.

<!-- S45 -->
Les grandes ondes atteignent une horloge par deux chemins :
le long du sol,
et en rebondissant sur la haute atmosphère.
À la tombée de la nuit, ce chemin du haut change,
et le signal porte souvent plus loin.

<!-- S46 -->
Et à trois heures du matin,
il y a en général moins de machines, de chargeurs et de lampes
allumés à proximité pour le couvrir.

<!-- S47 -->
Entre ces vérifications,
l'horloge tourne sur un cristal de quartz,
qui peut dériver d'environ une seconde par jour.

<!-- S48 -->
À la vérification réussie suivante,
la radio corrige cette dérive.

<!-- S49 -->
Même l'endroit où elle écoute compte.
L'antenne est un petit barreau de ferrite
entouré de fil.

<!-- S50 -->
Elle capte le mieux quand le barreau est perpendiculaire
à la direction de l'émetteur,
et non pointé vers lui.
Tourne l'horloge,
et un signal faible peut disparaître complètement.

<!-- S51 -->
C'est pour ça qu'une horloge fonctionne sur une étagère,
alors que la même horloge, à deux mètres de là,
derrière un mur en béton armé, ne se règle jamais.

<!-- S52 -->
Mais d'où l'émetteur
tient-il son heure ?

<!-- S53 -->
De la PTB,
l'institut national de métrologie allemand,
qui fait fonctionner des horloges atomiques.

<!-- S54 -->
La seconde elle-même est définie
par des atomes de césium.
Une seconde, c'est exactement
9 192 631 770 oscillations
du rayonnement qu'ils émettent.

<!-- S55 -->
Un réveil bon marché sur une table de chevet
suit donc, littéralement,
un étalon de temps
défini par des atomes de césium.

<!-- S56 -->
Pas parfaitement, cependant.
Le signal voyage à la vitesse de la lumière,
et même elle met environ 3 millisecondes
pour chaque tranche de 1 000 kilomètres.

<!-- S57 -->
Le récepteur ajoute son propre retard,
et ton horloge ne corrige rien de tout ça.
Elle n'en a pas besoin.
Elle n'affiche que des secondes.

<!-- S58 -->
Depuis un seul site près de Francfort,
le signal atteint des horloges
jusqu'à environ 2 000 kilomètres.
C'est la plus grande partie de l'Europe.

<!-- S59 -->
La Suisse avait son propre émetteur,
appelé HBG, jusqu'à fin 2011.
Ses antennes devaient être remplacées,
trop peu de gens l'utilisaient,
et les horloges suisses pouvaient tout simplement
écouter l'Allemagne à la place.

<!-- S60 -->
D'autres ont gardé le leur.
Le Royaume-Uni, la France, le Japon et la Chine
ont tous leur propre émetteur.

<!-- S61 -->
Et en Amérique du Nord, WWVB
émet de Fort Collins depuis 1963,
avec un code horaire depuis 1965.

<!-- S62 -->
Même principe, autre dialecte.
Un zéro, c'est une baisse de deux dixièmes de seconde.
Un 1 dure une demi-seconde.

<!-- S63 -->
Et au lieu d'un trou par minute,
un repère plus long arrive toutes les 10 secondes,
comme des virgules dans la phrase.
Deux d'affilée signalent une nouvelle minute.

<!-- S64 -->
La plus grande différence,
c'est l'heure qu'il envoie.
L'Allemagne diffuse l'heure légale d'Europe centrale,
partagée par une grande partie du continent.

<!-- S65 -->
Mais les États-Unis
s'étendent sur plusieurs fuseaux horaires.
WWVB envoie donc le temps universel, l'UTC,
et c'est toi qui indiques à l'horloge où tu te trouves.

<!-- S66 -->
Il n'envoie même pas le mois.
Juste le jour de l'année,
de 1 à 366.

<!-- S67 -->
Aucune de ces stations
ne parle la même langue.
Une horloge faite pour l'Allemagne
ne comprend rien au Colorado.

<!-- S68 -->
Mais des deux côtés de l'Atlantique,
c'est la même routine silencieuse.
Nuit après nuit, un petit récepteur
se cale sur un étalon de temps atomique,
à des centaines ou des milliers de kilomètres.

<!-- S69 -->
Alors, une question pour toi.
Si tous les signaux horaires radio
disparaissaient cette nuit,
est-ce que tu t'en rendrais même compte ?
Dis-le-moi dans les commentaires.
