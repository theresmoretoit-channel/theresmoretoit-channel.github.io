# Internet Explorer 6 — Le navigateur devenu plateforme

Traduction de `script.md`. Mêmes marques de scène, même nombre de lignes.
Une ligne = une phrase = un sous-titre.

<!-- S01 -->
Imaginez que vous êtes développeur web
au début des années deux mille.

Vous avez écrit
une page web parfaitement raisonnable.

<!-- S02 -->
Elle marche dans Netscape.

Elle marche dans Opera.

Elle marche dans le nouveau Firefox.

Et puis vous l'ouvrez
dans Internet Explorer.

Tout est cassé.

<!-- S03 -->
La mise en page est fausse.

Les boutons ont bougé.

Les images PNG sont affreuses.

Et allez savoir pourquoi,
un seul retour à la ligne dans votre HTML
a créé un espace de trois pixels.

<!-- S04 -->
Bienvenue dans le développement web
à l'époque d'Internet Explorer 6.

Mais voilà ce qui est intéressant.

Internet Explorer 6
n'était pas juste un mauvais navigateur.

<!-- S05 -->
Microsoft essayait de résoudre des problèmes
que le web avait vraiment.

Il avait simplement un avantage énorme
sur tous les autres.

Windows.

<!-- S06 -->
Et cet avantage a fini par lui permettre
de transformer le navigateur
en quelque chose de bien plus grand
qu'un navigateur.

<!-- S07 -->
Au milieu des années quatre-vingt-dix,
le web était dominé
par Netscape Navigator.

Cela ne plaisait pas à Microsoft.

<!-- S08 -->
Internet Explorer a donc été
livré avec Windows
et mis à disposition gratuitement.

Vous achetiez un ordinateur sous Windows.

Internet Explorer était déjà là.

Rien à télécharger.

Rien à payer.

<!-- S09 -->
Et surtout,
Microsoft contrôlait
le système d'exploitation.

Peu après l'an 2000,
Internet Explorer détenait
plus de quatre-vingt-dix pour cent
du marché des navigateurs.

<!-- S10 -->
Internet Explorer 6 est arrivé
en 2001,
en même temps que Windows XP.

Et pendant un temps, on aurait dit
que Microsoft avait tout simplement gagné
la guerre des navigateurs.

<!-- S11 -->
Microsoft avait un problème.

Le web savait faire très peu de choses.

HTML pouvait afficher des documents.

CSS pouvait les mettre en forme.

JavaScript pouvait les rendre interactifs.

<!-- S12 -->
Et c'était à peu près tout.

Tout ce qui était plus compliqué
se heurtait directement
aux limites du navigateur.

<!-- S13 -->
Et si vous vouliez scanner un document ?

Ou dialoguer avec une carte à puce ?

Ou parler à un composant
matériel de Windows ?

<!-- S14 -->
Le navigateur ne savait
vraiment pas faire ça.

Microsoft a donc proposé une solution.

ActiveX.

<!-- S15 -->
L'idée de base était simple.

Pourquoi limiter une application web
à ce que sait faire le navigateur ?

Laissons-la utiliser
des composants natifs de Windows.

<!-- S16 -->
Et soudain une page web
pouvait faire des choses
dont le HTML ordinaire
ne pouvait même pas rêver.

<!-- S17 -->
Aujourd'hui, ActiveX fait peur.

Et à juste titre.

Un composant ActiveX pouvait atteindre
les fichiers, les applications,
le matériel
et le système d'exploitation.

<!-- S18 -->
Vu la sécurité d'aujourd'hui,
cela paraît totalement insensé.

Mais au début des années deux mille,
cela avait tout son sens
pour les applications d'entreprise.

<!-- S19 -->
Les entreprises ne voulaient pas
d'une jolie visionneuse de documents.

Elles voulaient des applications.

Elles voulaient des pages web
qui se comportent
presque comme un logiciel de bureau.

<!-- S20 -->
Et Microsoft leur a donné exactement ça.

Windows Update lui-même
reposait à l'origine sur ActiveX
pour inspecter le système
et déterminer quelles mises à jour
étaient nécessaires.

<!-- S21 -->
ActiveX n'était donc pas simplement
une erreur stupide.

C'était une tentative précoce
de transformer le navigateur
en plateforme applicative.

<!-- S22 -->
Et en ce sens, Microsoft
était vraiment en avance sur son temps.

Le problème, c'était le pouvoir
qu'il a donné à cette plateforme.

<!-- S23 -->
ActiveX n'était pas
la seule extension de Microsoft.

Il y avait VBScript.

Il y avait DHTML.

Et même CSS expression.

Oui.

<!-- S24 -->
Internet Explorer pouvait évaluer
du JavaScript directement dans le CSS.

On pouvait écrire quelque chose comme ça.

<!-- S25 -->
C'était ridicule.

Et parfois aussi
étonnamment utile.

Et rien de tout cela n'était garanti
de fonctionner ailleurs.

<!-- S26 -->
Microsoft ne se contentait pas
d'implémenter le web.

Microsoft étendait le web
dans sa propre direction.

Et avec quatre-vingt-dix pour cent
du marché,
il avait assez de pouvoir
pour que ça passe.

<!-- S27 -->
L'un des exemples les plus célèbres
était le modèle de boîte CSS.

Le modèle standard disait
que si un élément
faisait 200 pixels de large,
avec 20 pixels de remplissage
et 5 pixels de bordure,

<!-- S28 -->
la largeur totale
était de 250 pixels.

<!-- S29 -->
Les anciennes versions d'Internet Explorer
lisaient cela autrement.

En mode quirks, la largeur déclarée
pouvait inclure le remplissage
et la bordure.

<!-- S30 -->
Ce n'était pas forcément
une façon absurde de penser la largeur.

D'ailleurs, aujourd'hui nous demandons
souvent ce comportement exprès.

Cela s'appelle border-box.

<!-- S31 -->
Le vrai problème, c'était
que les différents navigateurs
se comportaient différemment.

Et cela voulait dire
que le développeur devait s'en soucier.

Beaucoup.

<!-- S32 -->
Il existait un truc appelé hasLayout.

Ce n'était pas une propriété CSS normale.

Cela ne faisait pas partie du standard.

Mais cela décidait
de la façon dont Internet Explorer
disposait les éléments.

<!-- S33 -->
Et parfois une mise en page cassée
se réparait mystérieusement
en ajoutant une seule ligne.

zoom: 1

Pourquoi ?

Parce que zoom: 1 pouvait déclencher
le mécanisme interne hasLayout.

<!-- S34 -->
Il y avait des problèmes
avec la transparence des PNG.

Il y avait des problèmes avec les éléments select,
qui s'affichaient par-dessus
des menus positionnés en absolu,
peu importe la valeur
que vous donniez au z-index.

<!-- S35 -->
Le développement web ne consistait pas seulement
à réaliser votre maquette.

Il consistait à apprendre les bugs
d'un moteur de rendu précis.

<!-- S36 -->
Encore un merveilleux exemple.

Les espaces blancs.

Et là, ce n'était même pas
la faute d'Internet Explorer.

On pouvait mettre deux images
juste l'une à côté de l'autre
dans le balisage,
sans rien entre les balises,
et obtenir un résultat.

<!-- S37 -->
Puis quelqu'un formatait proprement le HTML
et mettait chaque balise sur sa propre ligne.

Et soudain il y avait
un espace de quelques pixels entre les images.

Le retour à la ligne devenait significatif.

<!-- S38 -->
Votre formateur de code
pouvait littéralement casser votre page.

Et si vous utilisiez
une vieille version de Visual Studio,
il vous formatait le HTML
de bon cœur, tout seul.

Merci, Microsoft.

<!-- S39 -->
Les développeurs ont accumulé
toute une boîte à outils de contournements.

Les commentaires conditionnels.

<!-- S40 -->
Et parfois du HTML
à l'allure complètement bizarre
dont le seul but était
de faire tenir Internet Explorer tranquille.

<!-- S41 -->
Vous n'écriviez pas du code moche
parce que vous étiez un mauvais programmeur.

Vous écriviez du code moche
parce que le navigateur vous y forçait.

<!-- S42 -->
Internet Explorer plantait aussi
de façon spectaculaire, et emportait souvent
toutes les fenêtres ouvertes avec lui.

<!-- S43 -->
D'où une merveilleuse catégorie
de divertissement de bureau.

Hé, regarde ce lien.

Et vingt fenêtres d'Internet Explorer
disparaissent.

<!-- S44 -->
C'était le web avant que
les navigateurs soient isolés.

Le navigateur d'aujourd'hui dit ceci.

Ce site n'est pas fiable.

Je vais l'isoler.

<!-- S45 -->
Internet Explorer 6
ressemblait plutôt à ça.

Tu es une page web ?

Bien sûr.

Voici les clés de l'immeuble.

<!-- S46 -->
Pourquoi les développeurs
utilisaient-ils ces bidouilles ?

Parce qu'ils n'avaient pas le choix.

<!-- S47 -->
Imaginez une entreprise
de cinq cents salariés.

Chaque poste tourne sous Windows XP.

Chaque poste a Internet Explorer.

<!-- S48 -->
Le développeur a deux options.

Option une.

Développer pour Internet Explorer,
que tout le monde a déjà.

<!-- S49 -->
Option deux.

Développer pour tous les navigateurs,
tout tester partout,
et expliquer au service informatique
pourquoi il en faut un deuxième pour tous.

La réponse était en général évidente.

<!-- S50 -->
Ils ne choisissaient pas
la technologie de Microsoft
parce qu'ils aimaient Microsoft.

Ils choisissaient ce qui réglait
le problème du client.

Et parfois ActiveX
était le meilleur outil disponible.

<!-- S51 -->
Et un jour, quelqu'un en a eu assez.

Les bibliothèques JavaScript ont commencé
à masquer les différences entre navigateurs.

L'une des plus importantes
était jQuery.

<!-- S52 -->
Au lieu d'écrire
une gestion d'événements par navigateur,
on écrivait une seule ligne
qui marchait partout.

<!-- S53 -->
Au lieu de jongler à la main
avec différentes implémentations d'AJAX,
on utilisait une abstraction commune.

<!-- S54 -->
jQuery n'a pas fait
disparaître Internet Explorer.

Mais elle a rendu bien plus facile
le fait de faire comme s'il n'existait pas.

Et pour les développeurs web de l'époque,
c'était une merveille.

<!-- S55 -->
Firefox est apparu.

Opera a continué à se développer.

Safari est arrivé.

Et Google a fini par sortir Chrome.

<!-- S56 -->
La guerre des navigateurs était de retour,
et cette fois
la concurrence était différente.

Les moteurs JavaScript
sont devenus bien meilleurs.

HTML5 est arrivé.

<!-- S57 -->
Le navigateur lui-même a commencé à apprendre
tout ce pour quoi les développeurs
avaient eu besoin de greffons.

<!-- S58 -->
La vidéo.

L'audio.

Canvas.

SVG.

WebGL.

WebSockets.

Et finalement WebRTC.

Le web devenait
une plateforme applicative.

<!-- S59 -->
C'était exactement
ce que Microsoft avait essayé
d'obtenir avec ActiveX.

Sauf que cette fois cela passait
par des standards ouverts.

<!-- S60 -->
Microsoft a réessayé une fois.

Silverlight permettait de créer
des applications riches dans le navigateur
en C# et .NET.

Les débuts du streaming de Netflix
tournaient même dessus.

<!-- S61 -->
Mais le web ne voulait pas de greffons pour toujours.

Apple a refusé de prendre en charge Flash
sur l'iPhone.

Et soudain l'avenir n'était plus ceci.

Navigateur plus greffon.

C'était ceci.

Le navigateur lui-même.

<!-- S62 -->
Silverlight a disparu.

Flash a disparu.

ActiveX a disparu.

Et Internet Explorer
a fini par disparaître aussi.

<!-- S63 -->
Et c'est là que
l'histoire devient intéressante.

Parce que Microsoft
n'avait pas complètement tort.

Il avait correctement prédit
que le navigateur deviendrait
une plateforme applicative.

<!-- S64 -->
Il essayait juste d'y arriver
par des technologies propriétaires.

Le web a atteint la même destination
par les standards.

<!-- S65 -->
Le navigateur a gagné.

Mais il a gagné en devenant
quelque chose de bien plus puissant
que le navigateur
de 2001.

<!-- S66 -->
Microsoft était-il donc le méchant ?

Pas vraiment.

Et c'est ce qui rend
l'histoire plus intéressante.

<!-- S67 -->
Microsoft avait des ingénieurs brillants.

Il avait des moyens énormes.

Et il a construit beaucoup de technologies
vraiment en avance sur leur temps.

<!-- S68 -->
Mais Microsoft avait aussi
une position dominante écrasante.

Et cela a créé
une incitation dangereuse.

<!-- S69 -->
Si presque tout le monde
utilise votre navigateur,
pourquoi attendre les standards ?

Pourquoi ne pas simplement implémenter
votre propre solution ?

Pendant un temps, ça a marché.

Jusqu'à ce que le reste du web rattrape.

<!-- S70 -->
Aujourd'hui, Internet Explorer n'est plus là.

Les vieilles guerres de navigateurs
semblent de l'histoire ancienne.

Mais regardez
le marché actuel des navigateurs.

Chrome.

Edge.

Opera.

Brave.

Vivaldi.

<!-- S71 -->
Et beaucoup d'autres
reposent sur Chromium.

Des produits différents.

Souvent le même
moteur en dessous.

<!-- S72 -->
Alors peut-être avons-nous échangé ceci.

Un navigateur que tous devaient prendre en compte.

Contre ceci.

Un moteur sur lequel tous construisent.

Cela ne vous rappelle rien ?

<!-- S73 -->
Parce qu'un moteur dominant
ne décide pas seulement
comment les sites s'affichent.

<!-- S74 -->
Il influence ce que les développeurs construisent.

Quelles technologies deviennent populaires.

Et en fin de compte,
ce que le web lui-même devient.

<!-- S75 -->
Il y a toutefois
une différence très importante.

Le web d'aujourd'hui repose
sur des standards ouverts.

Firefox a toujours son propre moteur.

Safari a WebKit.

Chromium est libre.

<!-- S76 -->
Et les navigateurs modernes
se mettent à jour tout seuls.

Nous sommes très loin
de la situation
de 2003.

<!-- S77 -->
Mais la question de fond demeure.

Quelle influence
une seule entreprise devrait-elle avoir
sur une plateforme
utilisée par presque tout le monde ?

C'est la question
qui n'a jamais vraiment disparu.

<!-- S78 -->
Alors, Internet Explorer 6 était-il affreux ?

Oui.

Parfois spectaculairement affreux.

<!-- S79 -->
Mais ce n'est pas toute l'histoire.

C'était aussi un produit de son époque.

<!-- S80 -->
Le problème, c'est
que Microsoft avait gagné
les guerres de navigateurs si complètement
qu'il pouvait fixer les règles.

<!-- S81 -->
Et ce sont les développeurs web qui ont payé.

Ils ont appris les mystères
de hasLayout.

Ils ont découvert que zoom: 1
réparait les choses comme par magie.

Et ils ont prié.

<!-- S82 -->
Et Internet Explorer a fini
par devenir ce qu'il avait passé
vingt ans à construire.

Une plateforme héritée
que plus personne
ne voulait maintenir.

<!-- S83 -->
Le web n'a pas rejeté
la vision de Microsoft.

Il en a simplement construit
une meilleure version.

Et s'il y a une chose
que cette époque doit nous apprendre,
c'est celle-ci.

<!-- S84 -->
Une technologie ne devient pas un standard
parce qu'elle est bonne.

<!-- S85 -->
Parfois elle devient un standard
parce qu'une entreprise a assez de pouvoir
pour l'imposer à tout le monde.

<!-- S86 -->
Et parfois,
vingt ans plus tard,
on se rend compte qu'on a recommencé.
