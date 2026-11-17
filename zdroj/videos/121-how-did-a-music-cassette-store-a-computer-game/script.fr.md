<!-- S01 -->
Tu lances la lecture sur un magnéto-cassette.
Et voilà ce qui sort du haut-parleur.

<!-- S02 -->
Ce n'est pas de la musique.
Et ce n'est pas non plus la bande-son d'un jeu.

<!-- S03 -->
C'est le jeu lui-même.
Chaque sifflement fait partie d'un programme,
et l'ordinateur l'écoute.

<!-- S04 -->
Le lecteur de cassettes n'en a aucune idée.
Pour lui, il est en train de jouer une chanson.

<!-- S05 -->
Alors comment transformer une chanson en jeu ?
Et pourquoi une seule fausse note
pouvait-elle réduire à néant cinq minutes d'attente ?

<!-- S06 -->
Voici l'astuce,
sur une machine bien précise :
le ZX Spectrum,
un ordinateur familial britannique de 1982.

<!-- S07 -->
Il utilise deux sortes d'impulsions.
Une paire d'impulsions courtes, c'est un zéro.

<!-- S08 -->
Un « un », c'est la même paire,
mais chaque impulsion dure deux fois plus longtemps,
donc sa note sonne une octave plus bas.

<!-- S09 -->
Envoie environ mille quatre cents bits
par seconde,
et tu obtiens le bruit que tu viens d'entendre.

<!-- S09b -->
Ça veut aussi dire qu'un programme plein de zéros
se charge plus vite qu'un programme plein de uns.
Chaque « un » met deux fois plus de temps à passer.

<!-- S10 -->
Cela dit, si tu as grandi aux États-Unis,
tu ne l'as peut-être jamais entendu.

<!-- S11 -->
Ce qui est curieux,
parce que l'idée elle-même était américaine.

<!-- S12 -->
En 1975, lors d'une réunion à Kansas City,
des passionnés d'informatique ont convenu d'une façon
de stocker des données sous forme de son
sur de simples cassettes audio.

<!-- S12b -->
Un « un », c'était huit cycles rapides
d'une note aiguë,
un zéro, quatre cycles plus lents d'une note grave.
Trois cents bits par seconde.

<!-- S13 -->
Les premières machines comme l'Apple II
et le TRS-80
enregistraient leurs programmes
sur des magnétophones tout ce qu'il y a de plus ordinaires.

<!-- S14 -->
Mais l'informatique familiale américaine
est vite passée à autre chose.

<!-- S15 -->
En 1983, un magazine a rapporté un sondage :
neuf nouveaux propriétaires de Commodore 64 sur dix
achetaient un lecteur de disquettes
en même temps que l'ordinateur.

<!-- S16 -->
En Grande-Bretagne, l'histoire a pris le chemin inverse.

<!-- S17 -->
Le Spectrum coûtait cent
vingt-cinq livres,
et il n'avait aucun support de stockage.
Tu utilisais le lecteur de cassettes
que tu avais déjà.

<!-- S18 -->
Alors pour des millions d'enfants à travers l'Europe,
ce bruit, c'était le son
d'un jeu sur le point de commencer.

<!-- S18b -->
À force de chargements,
tu pouvais même deviner de quel jeu il s'agissait
rien qu'au crissement.

<!-- S19 -->
Alors suivons un jeu
de la bande jusqu'à l'ordinateur.

<!-- S20 -->
Tu tapes LOAD, tu appuies sur Entrée,
et tu lances la lecture.

<!-- S21 -->
D'abord vient un bourdonnement continu,
huit cents cycles par seconde,
pendant environ cinq secondes.

<!-- S22 -->
Il ne transporte aucune donnée.
Il est là pour que l'ordinateur
trouve le signal
et se cale sur son rythme.

<!-- S23 -->
Puis deux impulsions rapides : la synchro.
Elles veulent dire : à partir d'ici, ce sont des données.

<!-- S24 -->
La première chose qui arrive,
c'est un court en-tête.
Dix-neuf octets :
un nom de dix lettres au maximum,
le type de fichier,
et la taille qu'il va faire.

<!-- S25 -->
Puis un deuxième bourdonnement, plus court,
deux secondes cette fois,
et ensuite le jeu lui-même.

<!-- S26 -->
Chaque octet, ce sont huit de ces notes,
l'une après l'autre,
sans le moindre blanc entre les octets.

<!-- S27 -->
Et l'ordinateur n'entend pas de notes.
Il chronomètre l'écart entre un front
du signal et le suivant.

<!-- S28 -->
Une paire courte, c'est un zéro.
Une paire longue, c'est un « un ».

<!-- S28a -->
Voilà tout le décodeur.

<!-- S28b -->
Et le bruit du début de cette vidéo
n'est pas un effet sonore.
On l'a généré en suivant exactement ces règles,
et il contient un vrai programme pour Spectrum.

<!-- S28c -->
On le passera en entier tout à la fin.
Enregistre-le, et un Spectrum le chargera.

<!-- S29 -->
La plupart des jeux affichaient d'abord une image,
et elle se chargeait dans un ordre bizarre.

<!-- S30 -->
De fines rayures apparaissaient, espacées de huit lignes,
puis se remplissaient, ligne par ligne,
un tiers de l'écran à la fois.
Et les couleurs arrivaient en dernier,
balayant tout de haut en bas.

<!-- S31 -->
Rien que cette image
prenait une quarantaine de secondes.
Le jeu entier, environ cinq minutes.

<!-- S32 -->
Et à la fin de chaque bloc
arrive un octet de plus.

<!-- S33 -->
À l'enregistrement, le Spectrum fait passer
chaque octet du bloc
par une règle simple appelée XOR,
et enregistre le résultat comme un octet de plus.

<!-- S34 -->
Au chargement, il refait le calcul.
Si les résultats concordent,
le bloc est arrivé intact.

<!-- S35 -->
Sinon, le Spectrum te dit ça.

<!-- S36 -->
Cinq minutes d'attente,
et un seul octet décide
que tout ça n'a servi à rien.
Rembobiner, et tout recommencer.

<!-- S37 -->
Bizarrement, un en-tête abîmé
ne déclenche aucune erreur.
Le Spectrum l'ignore tout simplement,
et continue d'écouter en attendant le suivant.

<!-- S38 -->
D'autres ordinateurs ont fait d'autres paris.

<!-- S39 -->
Le Commodore 64 enregistrait
chaque bloc deux fois,
pour pouvoir récupérer les données abîmées
à partir de l'autre copie.

<!-- S40 -->
Plus sûr, mais lent.
Avec la routine intégrée de Commodore,
un programme de quarante kilo-octets
prenait environ douze minutes et demie.

<!-- S41 -->
Alors les éditeurs de jeux ont écrit
leurs propres chargeurs, plus rapides,
certains jusqu'à environ dix fois plus rapides.

<!-- S42 -->
Et puis il y avait le lecteur de cassettes lui-même.

<!-- S43 -->
Trop faible,
et les fronts se noient dans le souffle.
Trop fort,
et ils bavent les uns sur les autres.

<!-- S44 -->
Une bande qui tourne un peu trop vite ou trop lentement
étire chaque impulsion,
or l'ordinateur, lui, mesure le temps.

<!-- S45 -->
Le pire de tout, c'était l'azimut,
l'angle de la tête de lecture.
Une cassette enregistrée sur un appareil
pouvait être mal alignée avec la tête d'un autre.

<!-- S46 -->
Alors les gens enfonçaient un minuscule tournevis
dans un trou à côté de la tête,
et le tournaient par petites touches,
en écoutant.

<!-- S47 -->
On aurait dit de la superstition.
En fait, on ajustait le signal.

<!-- S48 -->
Mais remarque ce que le lecteur de cassettes
n'a jamais eu à faire.

<!-- S49 -->
Il n'a jamais compris un seul bit.
Il enregistrait du son,
et le relisait.

<!-- S50 -->
Ce qui veut dire qu'un programme
n'avait pas vraiment besoin d'une cassette.
Tout ce qui pouvait transporter du son
pouvait transporter un logiciel.

<!-- S50b -->
Ça voulait aussi dire que copier un jeu
était aussi simple que copier un album.
Deux platines cassette et un câble.

<!-- S51 -->
Atari utilisait les deux pistes stéréo.
Le programme sur l'une,
et une voix sur l'autre,
qui te parlait à travers la télé
pendant que le jeu se chargeait.

<!-- S52 -->
En Yougoslavie, une émission de Radio Belgrade
diffusait des programmes sur les ondes.

<!-- S53 -->
Les auditeurs les enregistraient sur cassette,
environ cent cinquante programmes
entre 1983 et 1986.

<!-- S54 -->
En Tchécoslovaquie, c'était la télévision.
Un programme passait sous forme de son
pendant le générique de fin.

<!-- S55 -->
Et en 1983, le chanteur Pete Shelley
a caché un programme pour Spectrum
à la fin d'un album vinyle.

<!-- S56 -->
Tu le copiais sur cassette, tu le chargeais,
et les paroles s'affichaient à l'écran
en rythme avec les chansons.

<!-- S57 -->
Mais il y avait un hic.

<!-- S58 -->
La radio pouvait porter le son
jusqu'à chaque ordinateur du pays.
Seul le bon pouvait le comprendre.

<!-- S59 -->
Fais écouter un jeu Spectrum à un Commodore,
et le Commodore entend du bruit.
Les bits ne veulent dire quelque chose
que pour une machine qui connaît le format.

<!-- S60 -->
Alors la radio néerlandaise a essayé d'y remédier.
En 1982, elle a créé BASICODE :
un seul format sonore,
avec un petit programme traducteur
pour chaque type d'ordinateur.

<!-- S61 -->
Et ce problème n'a jamais disparu.
Un fichier n'est utile
que si quelque chose peut encore le lire.

<!-- S62 -->
Les cassettes ont perdu, bien sûr.
Les disquettes étaient plus rapides,
puis les disques durs, puis la mémoire flash.

<!-- S63 -->
Sauf que la bande n'est jamais vraiment partie.
Les centres de données gardent encore
leurs archives sur bande magnétique.

<!-- S64 -->
Une cartouche LTO-9 moderne
contient dix-huit téraoctets.

<!-- S65 -->
Ramenée à la vitesse du Spectrum,
cette capacité remplirait environ
vingt-neuf millions de cassettes,
et mettrait plus de trois mille
ans à se charger.

<!-- S66 -->
Mais c'est toujours la même idée.
Des motifs sur une bande qui défile,
retransformés en nombres
quand tu en as besoin.

<!-- S67 -->
Alors la prochaine fois que tu entends ce crissement,
souviens-toi de ce que c'est.
Pas du bruit.
Un programme qui voyage sous forme de son.

<!-- S68 -->
Et quelque part en 1985,
un enfant est assis devant une télévision,
à attendre que ça s'arrête.
Parce que quand ça s'arrête,
le jeu commence.

<!-- S69 -->
Alors voici une question pour toi.
Si tu as déjà chargé un jeu depuis une cassette,
qu'est-ce qui t'a le plus marqué ?
Dis-le-moi dans les commentaires.

<!-- S70 -->
Et comme promis, voici ce programme.
Comme la télévision tchécoslovaque,
on l'a mis sous le générique de fin.
