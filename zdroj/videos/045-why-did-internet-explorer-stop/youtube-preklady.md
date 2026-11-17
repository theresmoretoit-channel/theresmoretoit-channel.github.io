# Lokalizované názvy a popisy — Internet Explorer 6: Why Did It Stop For Five Years?

Podklad pro **YouTube Studio → video → Podrobnosti → Přidat jazyk**.
Pro každý jazyk jsou tu **dva bloky ke zkopírování**: název a popis.
Kopíruje se **celý blok mezi trojicí zpětných apostrofů**, co je mimo něj,
je poznámka. Anglický originál zůstává v `youtube.md` a nesahá se na něj.

Nahrává je `tools/lokalizace.py`, který čte právě tenhle formát.

## Co se NEPŘEKLÁDÁ

| | |
|---|---|
| **vlastní jména** | Internet Explorer, Windows, Windows XP, Microsoft, Macintosh, Netscape, Mozilla, Gecko, Firefox, Chrome, Safari, ActiveX, AJAX, Tasman |
| **Chris Wilson, Bill Gates** | jména osob |
| **časy kapitol** | musí sedět na vteřinu, jinak je YouTube neuzná |
| **tagy** | YouTube je per-jazyk nemá |
| **odkazy na předchozí díly** | tři adresy `https://youtu.be/…` |

Názvy kapitol se naopak **překládají** — divák je čte v seznamu pod videem.

> **`id` má navíc číslici 1990**, protože „devadesátá léta" se indonésky
> standardně píšou `era 1990-an` a slovní tvar `tahun sembilan puluhan`
> Codex označil za nestandardní. Strojová kontrola letopočtů to proto
> u indonéštiny hlásí jako odchylku — je to záměr, ne vada.

## Kontrola čísel

V popisu jsou: **6** v názvu prohlížeče, **2001** a **2006** jako roky
vydání, **pět let a dva měsíce**, **březen 2000** u druhého prohlížeče,
**šest týdnů**, **osm týdnů**, **1995** u vývojáře a **třetina obrazovky**
u lišt. Musí být v každém překladu a nesmí se změnit. Kapitol je
**dvacet tři**.

> **Obrazové zdroje tu nejsou a chybět nemají.** Tohle video nemá ani
> jeden archivní snímek — 88 diagramů kreslených kódem a 3 malované SDXL
> scény — takže `sources.json` je prázdný a povinná atribuce žádná.
> Poslední odstavec popisu to říká divákovi přímo.

## Pět nových jazyků (2026-09-15)

`fi`, `id`, `tr`, `uk`, `vi` přibyly při rozšíření kanálu na čtrnáct
jazyků. **Titulky v nich zatím NEJSOU** — doplňují se zvlášť a jsou
čtyřicetkrát dražší na kvótu. Do té doby závěrečný odstavec popisu
jmenuje **devět** jazyků titulků, i v těch nových pěti. Až SRT přibudou,
musí se ten odstavec přepsat **ve všech čtrnácti** a nahrát znovu.

> **Prošlo Codexem** (dvoudílný prompt A/B z `CLAUDE.md`): 23 nálezů
> přijato, dvě skupiny zamítnuty.
>
> **Zamítnuté tituly.** Codex u všech pěti chtěl upřesnit „zastavil se"
> na „jeho vývoj se zastavil" (*Miksi kehitys pysähtyi…*, *Geliştirilmesine
> Neden…*). Anglický originál je ale vágní schválně — je to wh-otázka,
> která nesmí vyzradit pointu — a všech devět hotových jazyků drží
> doslovný tvar (*Warum stand er fünf Jahre still?*). Stylová volba,
> ne chyba.
>
> **Zamítnutý obraz „cost the web a decade of workarounds"** u `uk`
> a `vi`. Codex ho chtěl rozepsat na „vývojáři museli deset let hledat
> obchozí řešení". Je to autorská metafora z originálu a němčina i ostatní
> ji drží doslova (*ein Jahrzehnt an Umwegen kostete*).
>
> **Vzorec napříč jazyky:** doslovné *„Along the way:"* označil Codex
> jako kalk **nezávisle u čtyř jazyků** (id, tr, uk, vi). To je podle
> `CLAUDE.md` znak překladatelského zlozvyku, ne překlepu — přijato
> všude.

## suomi (`fi`)

```
Internet Explorer 6 — miksi se pysähtyi viideksi vuodeksi?
```

```
Elokuussa 2001 Microsoft julkaisi Internet Explorer 6:n. Selaimen seuraava
versio ilmestyi lokakuussa 2006.

Viisi vuotta ja kaksi kuukautta, eikä siinä välissä yhtäkään uutta versiota
selaimesta, jota lähes kaikki maailmassa käyttivät. Eikä se johtunut siitä,
ettei kukaan olisi valittanut — jo tauon puolivälissä oli kokonaisia
verkkosivustoja, jotka käsittelivät selaimen ongelmia.

Tämä on neljäs osa, ja se kysyy kysymyksen, jota kolme ensimmäistä ei
kysynyt. Ei sitä, mitä selain teki verkolle. Vaan miksi se pysähtyi.

Vastaus ei ole se, ettei Microsoft olisi osannut rakentaa parempaa. Se osasi
ja teki niin: maaliskuussa 2000 se julkaisi selaimen, jossa oli eri moottori
eikä laatikkomallin virhettä, joka maksoi verkolle vuosikymmenen kiertoteitä
— ja lopetti sen kehityksen kuusi viikkoa sen jälkeen, kun se oli ilmoittanut
Internet Explorer 6:n olevan viimeinen erikseen asennettava versio.

Matkan varrella: kilpailuoikeudenkäynti, jonka uhka päättyi kahdeksan viikkoa
ennen Internet Explorer 6:n julkaisua; verkkokeskustelu, jossa Microsoft
sanoi selaimen olevan nyt Windowsin ominaisuus; kehittäjä, joka työskenteli
sen parissa vuodesta 1995 ja kirjoitti myöhemmin ylös, miksi se pysähtyi;
yrityssähköpostia varten yhdeksänkymmentäluvulla rakennettu komponentti,
jonka varaan koko moderni verkko myöhemmin rakennettiin; syy siihen, miksi
selaimesi kutsuu itseään yhä Mozillaksi; työkalupalkit, jotka söivät
kolmanneksen näytöstä; ja korjaus, joka saapui käyttöjärjestelmän service
packina uuden selaimen sijaan.

Osa yksi — kuinka Internet Explorer 6:sta tuli alusta:
https://youtu.be/R7Un3IOMvbg

Osa kaksi — virheet, joilla oli nimet:
https://youtu.be/1dIM5UZUEZg

Osa kolme — selain, joka ei suostunut kuolemaan:
https://youtu.be/dnF3SJoeTns

Luvut
00:00 Viisi vuotta ja kaksi kuukautta
00:40 Tämä on neljäs osa
01:01 Yhdeksänkymmentä prosenttia markkinoista
01:22 Oikeussalit
01:52 Kahdeksan viikkoa myöhemmin
02:26 Viimeinen erikseen asennettava versio
03:13 Seuraava Windows
03:48 Minne ihmiset menivät
04:42 Se lause, josta tässä on kyse
04:57 Se toinen selain
05:38 Kaksi tilaa, yhä tallella
06:06 Kaksi selainta, yksi kesä
06:47 Mitä sisällä jo oli
07:12 Sivu, joka osasi kysyä
07:58 AJAX
08:27 Mitä muuta täältä tuli
09:02 Kysy selaimeltasi, mikä se on
09:50 Toinen puolisko
10:20 Tapa laajentaa sitä
10:44 Neljä työkalupalkkia
11:28 Service pack, ei uusi selain
12:26 Firefox, sitten RSA
13:02 Miksi se siis pysähtyi?

Tekstitykset on kirjoitettu tätä videota varten, ei luotu
automaattisesti. Toisena ääniraitana on amerikanenglanti.

Kaikki kuvat on piirretty koodilla; videossa ei käytetä arkistovalokuvia.
```

## français (`fr`)

```
Internet Explorer 6 — Pourquoi s'est-il arrêté pendant cinq ans ?
```

```
En août 2001, Microsoft a publié Internet Explorer 6. La version suivante
du navigateur est sortie en octobre 2006.

Cinq ans et deux mois, et entre les deux pas une seule nouvelle version
du navigateur que presque tout le monde utilisait. Et ce n'était pas
faute de plaintes : au milieu de cet intervalle, des sites entiers
parlaient de ce qui clochait chez lui.

Voici la partie quatre, et elle pose la question que les trois premières
n'ont jamais posée. Pas ce que le navigateur a fait au web. Pourquoi il
s'est arrêté.

La réponse n'est pas que Microsoft ne savait pas faire mieux. Il savait,
et il l'a fait : en mars 2000 il a publié un navigateur avec un autre
moteur, sans le bug du modèle de boîte qui a coûté au web dix ans de
contournements — et il en a arrêté le développement six semaines après
avoir annoncé qu'Internet Explorer 6 serait la dernière version
installable séparément.

En chemin : l'affaire antitrust dont la menace a pris fin huit semaines
avant la sortie d'Internet Explorer 6 ; le chat en ligne où Microsoft a
dit que le navigateur était désormais une fonction de Windows ;
l'ingénieur qui y travaillait depuis 1995 et qui a écrit plus tard
pourquoi cela s'était arrêté ; le composant fabriqué dans les années
quatre-vingt-dix pour la messagerie d'entreprise sur lequel tout le web
moderne s'est ensuite construit ; la raison pour laquelle votre
navigateur se dit encore Mozilla ; les barres d'outils qui mangeaient un
tiers de l'écran ; et le correctif arrivé sous forme de service pack du
système d'exploitation plutôt que de nouveau navigateur.

Partie un — comment Internet Explorer 6 est devenu une plateforme :
https://youtu.be/R7Un3IOMvbg

Partie deux — les bugs qui avaient un nom :
https://youtu.be/1dIM5UZUEZg

Partie trois — le navigateur qui ne voulait pas mourir :
https://youtu.be/dnF3SJoeTns

Chapitres
00:00 Cinq ans et deux mois
00:40 Voici la partie quatre
01:01 Quatre-vingt-dix pour cent du marché
01:22 Les tribunaux
01:52 Huit semaines plus tard
02:26 La dernière version autonome
03:13 Le Windows suivant
03:48 Où sont passés les gens
04:42 La phrase dont il s'agit
04:57 L'autre navigateur
05:38 Deux modes, encore aujourd'hui
06:06 Deux navigateurs, un été
06:47 Ce qui était déjà dedans
07:12 Une page capable de demander
07:58 AJAX
08:27 Quoi d'autre vient d'ici
09:02 Demandez à votre navigateur ce qu'il est
09:50 L'autre moitié
10:20 Un moyen de l'étendre
10:44 Quatre barres d'outils
11:28 Un service pack au lieu d'un navigateur
12:26 Firefox, puis RSA
13:02 Alors pourquoi s'est-il arrêté ?

Les sous-titres sont écrits pour cette vidéo, pas générés
automatiquement. Une piste audio en anglais américain est disponible en
seconde piste.

Toutes les images sont dessinées par du code ; la vidéo n'utilise aucune
photographie d'archive.
```

## Bahasa Indonesia (`id`)

```
Internet Explorer 6 — Kenapa Berhenti Selama Lima Tahun?
```

```
Pada Agustus 2001, Microsoft merilis Internet Explorer 6. Versi berikutnya
dari browser itu baru keluar pada Oktober 2006.

Lima tahun dua bulan, dan di antaranya tidak ada satu pun versi baru dari
browser yang dipakai hampir semua orang di dunia. Bukan karena tidak ada
yang mengeluh — di tengah jeda itu ada situs-situs khusus yang membahas
apa saja yang salah dengannya.

Di bagian keempat ini kita membahas pertanyaan yang belum pernah diajukan
dalam tiga bagian sebelumnya. Bukan apa yang browser itu lakukan pada web.
Tapi kenapa ia berhenti.

Jawabannya bukan karena Microsoft tidak bisa membuat sesuatu yang lebih
baik. Mereka bisa, dan mereka melakukannya: pada Maret 2000 mereka merilis
browser dengan mesin yang berbeda, tanpa bug box model yang selama satu dekade
memaksa pengembang web mencari cara untuk mengakalinya — lalu menghentikan
pengembangannya enam minggu setelah mengumumkan bahwa Internet Explorer 6
akan menjadi versi terakhir yang bisa dipasang terpisah.

Dalam video ini juga: perkara antimonopoli yang ancamannya berakhir delapan
minggu sebelum Internet Explorer 6 dirilis; obrolan daring saat Microsoft
menyebut browser itu kini sebuah fitur Windows; insinyur yang
mengerjakannya sejak 1995 dan belakangan menuliskan kenapa semuanya
berhenti; komponen yang dibuat untuk email perusahaan pada era 1990-an dan kemudian menjadi fondasi seluruh web modern; alasan browser
Anda sampai sekarang masih menyebut dirinya Mozilla; bilah alat yang
memakan sepertiga layar; dan perbaikan yang datang sebagai service pack
untuk sistem operasi, bukan sebagai browser baru.

Bagian satu — bagaimana Internet Explorer 6 menjadi sebuah platform:
https://youtu.be/R7Un3IOMvbg

Bagian dua — bug-bug yang punya nama:
https://youtu.be/1dIM5UZUEZg

Bagian tiga — browser yang tidak mau mati:
https://youtu.be/dnF3SJoeTns

Bab
00:00 Lima tahun dua bulan
00:40 Ini bagian keempat
01:01 Sembilan puluh persen pasar
01:22 Pengadilan
01:52 Delapan minggu kemudian
02:26 Versi mandiri yang terakhir
03:13 Windows berikutnya
03:48 Ke mana orang-orang pergi
04:42 Kalimat yang jadi intinya
04:57 Browser yang satunya
05:38 Dua mode, masih ada
06:06 Dua browser, satu musim panas
06:47 Apa yang sudah ada di dalamnya
07:12 Halaman yang bisa bertanya
07:58 AJAX
08:27 Apa lagi yang lahir dari sini
09:02 Tanyakan kepada browser Anda apa identitasnya
09:50 Separuh yang lain
10:20 Cara untuk memperluasnya
10:44 Empat bilah alat
11:28 Service pack, bukan browser
12:26 Firefox, lalu RSA
13:02 Jadi kenapa ia berhenti?

Subtitel ditulis khusus untuk video ini, bukan hasil otomatis. Tersedia
juga trek audio kedua dalam bahasa Inggris Amerika.

Semua visual digambar dengan kode; video ini tidak memakai foto arsip.
```

## italiano (`it`)

```
Internet Explorer 6 — Perché si è fermato per cinque anni?
```

```
Nell'agosto del 2001 Microsoft ha rilasciato Internet Explorer 6. La
versione successiva del browser è uscita nell'ottobre del 2006.

Cinque anni e due mesi, e in mezzo nemmeno una nuova versione del browser
che usava quasi tutto il mondo. E non perché nessuno si lamentasse: a
metà di quel vuoto c'erano interi siti su ciò che non andava in lui.

Questa è la parte quattro, e pone la domanda che le prime tre non hanno
mai fatto. Non cosa il browser ha fatto al web. Perché si è fermato.

La risposta non è che Microsoft non sapesse fare di meglio. Sapeva, e
l'ha fatto: nel marzo del 2000 ha rilasciato un browser con un altro
motore, senza il bug del box model che è costato al web dieci anni di
aggiramenti — e ne ha chiuso lo sviluppo sei settimane dopo aver
annunciato che Internet Explorer 6 sarebbe stata l'ultima versione
installabile da sola.

Lungo la strada: la causa antitrust la cui minaccia è finita otto
settimane prima dell'uscita di Internet Explorer 6; la chat online in cui
Microsoft ha detto che il browser era ormai una funzione di Windows; lo
sviluppatore che ci lavorava dal 1995 e che poi ha scritto perché si è
fermato; il componente costruito negli anni novanta per la posta
aziendale su cui è poi stato costruito tutto il web moderno; il motivo
per cui il vostro browser si dichiara ancora Mozilla; le barre che si
mangiavano un terzo dello schermo; e la correzione arrivata come service
pack del sistema operativo invece che come browser nuovo.

Parte uno — come Internet Explorer 6 è diventato una piattaforma:
https://youtu.be/R7Un3IOMvbg

Parte due — i bug che avevano un nome:
https://youtu.be/1dIM5UZUEZg

Parte tre — il browser che non voleva morire:
https://youtu.be/dnF3SJoeTns

Capitoli
00:00 Cinque anni e due mesi
00:40 Questa è la parte quattro
01:01 Il novanta per cento del mercato
01:22 I tribunali
01:52 Otto settimane dopo
02:26 L'ultima versione a sé stante
03:13 Il Windows successivo
03:48 Dove sono finite le persone
04:42 La frase di cui si tratta
04:57 L'altro browser
05:38 Due modalità, ancora oggi
06:06 Due browser, un'estate
06:47 Cosa c'era già dentro
07:12 Una pagina che sapeva chiedere
07:58 AJAX
08:27 Cos'altro viene da qui
09:02 Chiedete al browser cos'è
09:50 L'altra metà
10:20 Un modo per estenderlo
10:44 Quattro barre
11:28 Un service pack invece di un browser
12:26 Firefox, poi RSA
13:02 Allora perché si è fermato?

I sottotitoli sono scritti per questo video, non generati
automaticamente. Come seconda traccia audio è disponibile l'inglese
americano.

Tutte le immagini sono disegnate da codice; il video non usa fotografie
d'archivio.
```

## Deutsch (`de`)

```
Internet Explorer 6 — Warum stand er fünf Jahre still?
```

```
Im August 2001 veröffentlichte Microsoft Internet Explorer 6. Die nächste
Version des Browsers kam im Oktober 2006.

Fünf Jahre und zwei Monate, und dazwischen keine einzige neue Version des
Browsers, den fast jeder auf der Welt benutzte. Und das lag nicht daran,
dass sich niemand beschwert hätte — mitten in dieser Lücke gab es ganze
Websites darüber, was an ihm falsch war.

Das ist Teil vier, und er stellt die Frage, die die ersten drei nie
gestellt haben. Nicht, was der Browser mit dem Web gemacht hat. Warum er
stehen blieb.

Die Antwort ist nicht, dass Microsoft nichts Besseres bauen konnte. Es
konnte, und es tat es: Im März 2000 erschien ein Browser mit einer anderen
Engine, ohne den Boxmodell-Fehler, der dem Web ein Jahrzehnt an Umwegen
kostete — und die Entwicklung wurde sechs Wochen nach der Ankündigung
eingestellt, dass Internet Explorer 6 die letzte einzeln installierbare
Version sein würde.

Unterwegs: das Kartellverfahren, dessen Drohung acht Wochen vor dem
Erscheinen von Internet Explorer 6 endete; der Online-Chat, in dem
Microsoft sagte, der Browser sei jetzt eine Funktion von Windows; der
Entwickler, der seit 1995 daran arbeitete und später aufschrieb, warum es
aufhörte; die in den Neunzigern für Firmen-E-Mail gebaute Komponente, auf
der später das ganze moderne Web stand; der Grund, warum sich Ihr Browser
bis heute Mozilla nennt; die Symbolleisten, die ein Drittel des
Bildschirms auffraßen; und die Lösung, die als Service Pack für das
Betriebssystem kam statt als neuer Browser.

Teil eins — wie Internet Explorer 6 zur Plattform wurde:
https://youtu.be/R7Un3IOMvbg

Teil zwei — die Fehler, die Namen hatten:
https://youtu.be/1dIM5UZUEZg

Teil drei — der Browser, der nicht sterben wollte:
https://youtu.be/dnF3SJoeTns

Kapitel
00:00 Fünf Jahre und zwei Monate
00:40 Das ist Teil vier
01:01 Neunzig Prozent des Marktes
01:22 Die Gerichte
01:52 Acht Wochen später
02:26 Die letzte eigenständige Version
03:13 Das nächste Windows
03:48 Wohin die Leute gingen
04:42 Der Satz, um den es geht
04:57 Der andere Browser
05:38 Zwei Modi, bis heute
06:06 Zwei Browser, ein Sommer
06:47 Was schon drin war
07:12 Eine Seite, die fragen konnte
07:58 AJAX
08:27 Was sonst noch von hier kommt
09:02 Fragen Sie Ihren Browser, was er ist
09:50 Die andere Hälfte
10:20 Ein Weg, ihn zu erweitern
10:44 Vier Symbolleisten
11:28 Ein Service Pack statt eines Browsers
12:26 Firefox, dann RSA
13:02 Warum blieb er also stehen?

Die Untertitel wurden für dieses Video geschrieben, nicht automatisch
erzeugt. Als zweite Tonspur steht amerikanisches Englisch bereit.

Alle Bilder sind aus Code gezeichnet; das Video verwendet keine
Archivfotos.
```

## polski (`pl`)

```
Internet Explorer 6 — Dlaczego zatrzymał się na pięć lat?
```

```
W sierpniu 2001 Microsoft wydał Internet Explorer 6. Następna wersja
przeglądarki ukazała się w październiku 2006.

Pięć lat i dwa miesiące, a w tym czasie ani jedna nowa wersja
przeglądarki, z której korzystali prawie wszyscy na świecie. I nie
dlatego, że nikt nie narzekał — w połowie tej luki istniały całe strony
o tym, co było z nią nie tak.

To jest część czwarta i zadaje pytanie, którego pierwsze trzy nigdy nie
zadały. Nie co ta przeglądarka zrobiła sieci. Dlaczego się zatrzymała.

Odpowiedź nie brzmi, że Microsoft nie umiał zrobić czegoś lepszego.
Umiał i zrobił: w marcu 2000 wydał przeglądarkę z innym silnikiem, bez
błędu modelu pudełkowego, który kosztował sieć dekadę obchodzenia — i
zakończył jej rozwój sześć tygodni po ogłoszeniu, że Internet Explorer 6
będzie ostatnią wersją instalowaną osobno.

Po drodze: sprawa antymonopolowa, której groźba skończyła się osiem
tygodni przed wydaniem Internet Explorera 6; czat internetowy, na którym
Microsoft powiedział, że przeglądarka jest teraz funkcją Windows;
programista, który pracował przy niej od 1995 roku i później zapisał,
dlaczego się zatrzymała; komponent zbudowany w latach dziewięćdziesiątych
dla firmowej poczty, na którym stanęła potem cała nowoczesna sieć; powód,
dla którego twoja przeglądarka do dziś podaje się za Mozillę; paski,
które zjadały jedną trzecią ekranu; i poprawka, która przyszła jako
dodatek Service Pack do systemu operacyjnego zamiast nowej przeglądarki.

Część pierwsza — jak Internet Explorer 6 stał się platformą:
https://youtu.be/R7Un3IOMvbg

Część druga — błędy, które miały imiona:
https://youtu.be/1dIM5UZUEZg

Część trzecia — przeglądarka, która nie chciała umrzeć:
https://youtu.be/dnF3SJoeTns

Rozdziały
00:00 Pięć lat i dwa miesiące
00:40 To jest część czwarta
01:01 Dziewięćdziesiąt procent rynku
01:22 Sądy
01:52 Osiem tygodni później
02:26 Ostatnia samodzielna wersja
03:13 Następny Windows
03:48 Gdzie podziali się ludzie
04:42 Zdanie, o które tu chodzi
04:57 Ta druga przeglądarka
05:38 Dwa tryby, do dziś
06:06 Dwie przeglądarki, jedno lato
06:47 Co już było w środku
07:12 Strona, która umiała zapytać
07:58 AJAX
08:27 Co jeszcze jest stąd
09:02 Zapytaj przeglądarkę, czym jest
09:50 Druga połowa
10:20 Sposób, żeby ją rozszerzyć
10:44 Cztery paski
11:28 Service Pack zamiast przeglądarki
12:26 Firefox, potem RSA
13:02 Więc dlaczego się zatrzymał?

Napisy są pisane do tego filmu, nie generowane automatycznie. Jako druga
ścieżka dźwiękowa dostępny jest angielski amerykański.

Wszystkie obrazy są rysowane kodem; film nie korzysta z żadnych zdjęć
archiwalnych.
```

## português (Brasil) (`pt-BR`)

```
Internet Explorer 6 — Por que ele parou por cinco anos?
```

```
Em agosto de 2001 a Microsoft lançou o Internet Explorer 6. A versão
seguinte do navegador saiu em outubro de 2006.

Cinco anos e dois meses, e nesse meio-tempo nenhuma versão nova do
navegador que quase todo mundo no mundo usava. E não foi porque ninguém
reclamou: no meio desse intervalo havia sites inteiros sobre o que havia
de errado nele.

Esta é a parte quatro, e faz a pergunta que as três primeiras nunca
fizeram. Não o que o navegador fez com a web. Por que ele parou.

A resposta não é que a Microsoft não soubesse fazer algo melhor. Sabia, e
fez: em março de 2000 lançou um navegador com outro motor, sem o bug do
modelo de caixa que custou à web uma década de contornos — e encerrou seu
desenvolvimento seis semanas depois de anunciar que o Internet Explorer 6
seria a última versão instalável sozinha.

Pelo caminho: o processo antitruste cuja ameaça terminou oito semanas
antes de o Internet Explorer 6 sair; o bate-papo on-line em que a
Microsoft disse que o navegador agora era um recurso do Windows; o
engenheiro que trabalhou nele desde 1995 e depois escreveu por que ele
parou; o componente feito nos anos noventa para e-mail corporativo sobre
o qual toda a web moderna foi construída; a razão pela qual o seu
navegador ainda se diz Mozilla; as barras que comiam um terço da tela; e
a correção que chegou como service pack do sistema operacional em vez de
um navegador novo.

Parte um — como o Internet Explorer 6 virou plataforma:
https://youtu.be/R7Un3IOMvbg

Parte dois — os bugs que tinham nome:
https://youtu.be/1dIM5UZUEZg

Parte três — o navegador que não queria morrer:
https://youtu.be/dnF3SJoeTns

Capítulos
00:00 Cinco anos e dois meses
00:40 Esta é a parte quatro
01:01 Noventa por cento do mercado
01:22 Os tribunais
01:52 Oito semanas depois
02:26 A última versão avulsa
03:13 O Windows seguinte
03:48 Para onde foram as pessoas
04:42 A frase de que se trata
04:57 O outro navegador
05:38 Dois modos, até hoje
06:06 Dois navegadores, um verão
06:47 O que já estava dentro
07:12 Uma página que sabia perguntar
07:58 AJAX
08:27 O que mais vem daqui
09:02 Pergunte ao navegador o que ele é
09:50 A outra metade
10:20 Um jeito de estendê-lo
10:44 Quatro barras
11:28 Um service pack em vez de um navegador
12:26 Firefox, depois RSA
13:02 Então por que ele parou?

As legendas foram escritas para este vídeo, não geradas
automaticamente. Como segunda faixa de áudio está disponível o inglês
americano.

Todas as imagens são desenhadas por código; o vídeo não usa fotografias
de arquivo.
```

## Türkçe (`tr`)

```
Internet Explorer 6 — Neden Beş Yıl Boyunca Durdu?
```

```
Ağustos 2001'de Microsoft, Internet Explorer 6'yı yayımladı. Tarayıcının
bir sonraki sürümü Ekim 2006'da çıktı.

Beş yıl iki ay ve arada, dünyada neredeyse herkesin kullandığı tarayıcının
tek bir yeni sürümü bile yok. Kimse şikâyet etmediğinden değil — bu aranın
ortalarına gelindiğinde sırf tarayıcının sorunlarını anlatan koca koca
siteler vardı.

Bu dördüncü bölüm ve ilk üçünün hiç sormadığı soruyu soruyor. Tarayıcının
web'e ne yaptığını değil. Neden durduğunu.

Cevap, Microsoft'un daha iyisini yapamaması değil. Yapabildi ve yaptı: Mart
2000'de farklı bir motoru olan, web geliştiricilerini on yıl boyunca geçici
çözümler üretmek zorunda bırakan kutu modeli hatasını taşımayan bir tarayıcı çıkardı — ve Internet
Explorer 6'nın ayrıca kurulabilen son sürüm olacağını duyurmasından altı
hafta sonra onun geliştirilmesini durdurdu.

Bu bölümde ayrıca: tehdidi Internet Explorer 6'nın çıkışından sekiz hafta önce
sona eren antitröst davası; Microsoft'un tarayıcının artık Windows'un bir
özelliği olduğunu söylediği çevrimiçi sohbet; 1995'ten beri üzerinde
çalışan ve sonradan neden durduğunu yazıya döken mühendis; doksanlarda
kurumsal e-posta için yapılan ve sonradan tüm modern web'in üzerine
kurulduğu bileşen; tarayıcınızın hâlâ kendine neden Mozilla dediği; ekranın
üçte birini yiyen araç çubukları; ve yeni bir tarayıcı yerine işletim
sistemine service pack olarak gelen düzeltme.

Birinci bölüm — Internet Explorer 6 nasıl bir platforma dönüştü:
https://youtu.be/R7Un3IOMvbg

İkinci bölüm — adı olan hatalar:
https://youtu.be/1dIM5UZUEZg

Üçüncü bölüm — bir türlü ölmeyen tarayıcı:
https://youtu.be/dnF3SJoeTns

Bölümler
00:00 Beş yıl iki ay
00:40 Bu dördüncü bölüm
01:01 Pazarın yüzde doksanı
01:22 Mahkemeler
01:52 Sekiz hafta sonra
02:26 Ayrıca kurulabilen son sürüm
03:13 Sıradaki Windows
03:48 İnsanlar nereye gitti
04:42 Asıl mesele olan cümle
04:57 Öteki tarayıcı
05:38 İki mod, hâlâ orada
06:06 İki tarayıcı, bir yaz
06:47 İçinde zaten ne vardı
07:12 Soru sorabilen bir sayfa
07:58 AJAX
08:27 Buradan başka ne çıktı
09:02 Tarayıcınıza ne olduğunu sorun
09:50 Öbür yarısı
10:20 Onu genişletmenin bir yolu
10:44 Dört araç çubuğu
11:28 Tarayıcı değil, bir service pack
12:26 Firefox, sonra RSA
13:02 Peki neden durdu?

Altyazılar bu video için yazıldı, otomatik olarak oluşturulmadı. İkinci
ses parçası olarak Amerikan İngilizcesi de mevcut.

Tüm görseller kodla çizildi; bu videoda arşiv fotoğrafı kullanılmıyor.
```

## українська (`uk`)

```
Internet Explorer 6 — чому він зупинився на п'ять років?
```

```
У серпні 2001 року Microsoft випустила Internet Explorer 6. Наступна версія
браузера вийшла в жовтні 2006-го.

П'ять років і два місяці — і за цей час жодної нової версії браузера, яким
користувалися майже всі у світі. І не тому, що ніхто не скаржився: у
середині тієї паузи існували цілі сайти про те, що з ним не так.

Це четверта частина, і вона ставить запитання, якого не поставили перші
три. Не що браузер зробив з вебом. А чому він зупинився.

Відповідь не в тому, що Microsoft не вміла зробити краще. Вміла й зробила:
у березні 2000 року вона випустила браузер з іншим рушієм і без помилки
блокової моделі, яка коштувала вебу десятиліття обхідних шляхів, — і
припинила його розробку через шість тижнів після оголошення, що Internet
Explorer 6 буде останньою версією, яку можна встановити окремо.

У цьому випуску також: антимонопольна справа, загроза якої скінчилася за вісім тижнів до
виходу Internet Explorer 6; онлайн-чат, у якому Microsoft сказала, що
браузер тепер є функцією Windows; інженер, який працював над ним з 1995
року і згодом записав, чому все зупинилося; компонент, зроблений у
дев'яностих для корпоративної пошти, на якому згодом збудували весь
сучасний веб; причина, чому ваш браузер досі називає себе Mozilla; панелі
інструментів, які з'їдали третину екрана; і виправлення, що прийшло як
service pack до операційної системи, а не як новий браузер.

Частина перша — як Internet Explorer 6 став платформою:
https://youtu.be/R7Un3IOMvbg

Частина друга — помилки, які мали імена:
https://youtu.be/1dIM5UZUEZg

Частина третя — браузер, який не хотів помирати:
https://youtu.be/dnF3SJoeTns

Розділи
00:00 П'ять років і два місяці
00:40 Це четверта частина
01:01 Дев'яносто відсотків ринку
01:22 Суди
01:52 Через вісім тижнів
02:26 Остання окрема версія
03:13 Наступна Windows
03:48 Куди пішли люди
04:42 Речення, про яке йдеться
04:57 Інший браузер
05:38 Два режими, що збереглися досі
06:06 Два браузери, одне літо
06:47 Що вже було всередині
07:12 Сторінка, яка могла запитати
07:58 AJAX
08:27 Що ще з цього виникло
09:02 Запитайте свій браузер, що він таке
09:50 Друга половина
10:20 Спосіб його розширити
10:44 Чотири панелі інструментів
11:28 Service pack, а не браузер
12:26 Firefox, потім RSA
13:02 То чому ж він зупинився?

Субтитри написані для цього відео, а не згенеровані автоматично. Також
доступна друга звукова доріжка — американською англійською.

Усі зображення намальовані кодом; у цьому відео немає архівних світлин.
```

## Tiếng Việt (`vi`)

```
Internet Explorer 6 — Vì sao nó dừng lại suốt năm năm?
```

```
Tháng 8 năm 2001, Microsoft phát hành Internet Explorer 6. Phiên bản tiếp
theo của trình duyệt này ra mắt vào tháng 10 năm 2006.

Năm năm hai tháng, và ở giữa không có lấy một phiên bản mới nào của trình
duyệt mà gần như cả thế giới đang dùng. Không phải vì không ai phàn nàn —
giữa quãng trống đó đã có hẳn những website nói về các vấn đề của trình duyệt này.

Phần bốn này đặt ra câu hỏi mà ba phần đầu chưa từng đề cập. Không phải
trình duyệt đã làm gì với web. Mà vì sao nó dừng lại.

Câu trả lời không phải là Microsoft không đủ sức làm thứ tốt hơn. Họ làm
được, và đã làm: tháng 3 năm 2000 họ ra mắt một trình duyệt với engine
khác, không có lỗi box model từng khiến web mất cả một thập kỷ đi đường
vòng — rồi dừng phát triển nó sáu tuần sau khi tuyên bố Internet Explorer 6
sẽ là phiên bản cuối cùng có thể cài riêng.

Video cũng đề cập đến: vụ kiện chống độc quyền mà mối đe dọa của nó kết thúc tám
tuần trước khi Internet Explorer 6 ra mắt; buổi trò chuyện trực tuyến nơi
Microsoft nói rằng trình duyệt giờ là một tính năng của Windows; người kỹ
sư làm việc với nó từ năm 1995 và sau này viết lại vì sao nó dừng; thành
phần được phát triển để phục vụ email doanh nghiệp hồi thập niên chín mươi mà về sau cả
web hiện đại được xây trên đó; lý do trình duyệt của bạn đến giờ vẫn tự gọi
mình là Mozilla; những thanh công cụ ngốn một phần ba màn hình; và bản sửa
lỗi đến dưới dạng service pack cho hệ điều hành thay vì một trình duyệt mới.

Phần một — Internet Explorer 6 đã trở thành một nền tảng như thế nào:
https://youtu.be/R7Un3IOMvbg

Phần hai — những lỗi có tên riêng:
https://youtu.be/1dIM5UZUEZg

Phần ba — trình duyệt không chịu chết:
https://youtu.be/dnF3SJoeTns

Các chương
00:00 Năm năm hai tháng
00:40 Đây là phần bốn
01:01 Chín mươi phần trăm thị trường
01:22 Tòa án
01:52 Tám tuần sau
02:26 Phiên bản cài riêng cuối cùng
03:13 Windows kế tiếp
03:48 Mọi người đã đi đâu
04:42 Câu nói mà tất cả xoay quanh
04:57 Trình duyệt còn lại
05:38 Hai chế độ, vẫn còn đó
06:06 Hai trình duyệt, một mùa hè
06:47 Những gì đã có sẵn bên trong
07:12 Một trang có thể hỏi
07:58 AJAX
08:27 Còn gì khác ra đời từ đây
09:02 Hãy hỏi trình duyệt xem nó là gì
09:50 Nửa còn lại
10:20 Một cách để mở rộng nó
10:44 Bốn thanh công cụ
11:28 Một service pack, không phải trình duyệt
12:26 Firefox, rồi RSA
13:02 Vậy vì sao nó dừng lại?

Phụ đề được viết riêng cho video này, không phải tạo tự động. Có thể
chọn tiếng Anh Mỹ ở bản âm thanh thứ hai.

Toàn bộ hình ảnh được vẽ bằng mã; video này không dùng ảnh tư liệu.
```

## čeština (`cs`)

```
Internet Explorer 6 — Proč se na pět let zastavil?
```

```
V srpnu 2001 vydal Microsoft Internet Explorer 6. Další verze prohlížeče
vyšla v říjnu 2006.

Pět let a dva měsíce, a mezitím ani jedna nová verze prohlížeče, který
používal skoro každý na světě. A nebylo to tím, že by si nikdo
nestěžoval — v půlce té mezery existovaly celé weby o tom, co je na něm
špatně.

Tohle je čtvrtý díl a ptá se na to, na co se první tři nezeptaly. Ne co
ten prohlížeč udělal s webem. Proč se zastavil.

Odpověď není, že Microsoft neuměl udělat něco lepšího. Uměl a udělal:
v březnu 2000 vydal prohlížeč s jiným enginem a bez chyby box modelu,
která web stála deset let obcházení — a jeho vývoj ukončil šest týdnů
po oznámení, že Internet Explorer 6 bude poslední verze, kterou půjde
nainstalovat zvlášť.

Cestou: antimonopolní spor, jehož hrozba skončila osm týdnů před
vydáním Internet Exploreru 6; online chat, ve kterém Microsoft řekl, že
prohlížeč je teď funkcí Windows; vývojář, který na něm dělal od roku
1995 a později napsal, proč se zastavil; komponenta postavená
v devadesátých letech pro firemní poštu, na které pak stál celý moderní
web; důvod, proč se váš prohlížeč dodnes hlásí jako Mozilla; lišty,
které vám sežraly třetinu obrazovky; a oprava, která přišla jako
service pack operačního systému místo nového prohlížeče.

První díl — jak se z Internet Exploreru 6 stala platforma:
https://youtu.be/R7Un3IOMvbg

Druhý díl — bugy, které měly jména:
https://youtu.be/1dIM5UZUEZg

Třetí díl — prohlížeč, který nechtěl umřít:
https://youtu.be/dnF3SJoeTns

Kapitoly
00:00 Pět let a dva měsíce
00:40 Tohle je čtvrtý díl
01:01 Devadesát procent trhu
01:22 Soud
01:52 O osm týdnů později
02:26 Poslední samostatná verze
03:13 Další Windows
03:48 Kam se poděli lidé
04:42 Věta, o kterou tu jde
04:57 Ten druhý prohlížeč
05:38 Dva režimy, dodnes
06:06 Dva prohlížeče, jedno léto
06:47 Co už bylo uvnitř
07:12 Stránka, která se uměla zeptat
07:58 AJAX
08:27 Co dalšího je odsud
09:02 Zeptejte se prohlížeče, co je zač
09:50 Druhá půlka
10:20 Způsob, jak ho rozšířit
10:44 Čtyři lišty
11:28 Service pack místo prohlížeče
12:26 Firefox, pak RSA
13:02 Tak proč se zastavil?

Titulky jsou psané pro tohle video, ne strojový přepis. Jako druhá
zvuková stopa je k dispozici americká angličtina.

Všechny obrazy jsou kreslené kódem; video nepoužívá žádné archivní
fotografie.
```

## español (`es`)

```
Internet Explorer 6 — ¿Por qué se detuvo durante cinco años?
```

```
En agosto de 2001 Microsoft lanzó Internet Explorer 6. La siguiente
versión del navegador salió en octubre de 2006.

Cinco años y dos meses, y entre medias ni una sola versión nueva del
navegador que usaba casi todo el mundo. Y no fue porque nadie se
quejara: a mitad de ese hueco había webs enteras sobre lo que fallaba
en él.

Esta es la parte cuatro, y hace la pregunta que las tres primeras nunca
hicieron. No qué le hizo el navegador a la web. Por qué se detuvo.

La respuesta no es que Microsoft no supiera hacer algo mejor. Sabía, y lo
hizo: en marzo de 2000 lanzó un navegador con otro motor, sin el fallo
del modelo de caja que costó a la web una década de rodeos, y terminó su
desarrollo seis semanas después de anunciar que Internet Explorer 6 sería
la última versión instalable por separado.

Por el camino: el caso antimonopolio cuya amenaza terminó ocho semanas
antes de que saliera Internet Explorer 6; el chat en línea en el que
Microsoft dijo que el navegador ya era una función de Windows; el
ingeniero que trabajó en él desde 1995 y después escribió por qué se
detuvo; el componente hecho en los noventa para el correo de empresa
sobre el que se construyó toda la web moderna; la razón por la que tu
navegador todavía dice llamarse Mozilla; las barras que se comían un
tercio de la pantalla; y el arreglo que llegó como un service pack del
sistema operativo en vez de como un navegador nuevo.

Parte uno — cómo Internet Explorer 6 se convirtió en plataforma:
https://youtu.be/R7Un3IOMvbg

Parte dos — los fallos que tenían nombre:
https://youtu.be/1dIM5UZUEZg

Parte tres — el navegador que no quería morir:
https://youtu.be/dnF3SJoeTns

Capítulos
00:00 Cinco años y dos meses
00:40 Esta es la parte cuatro
01:01 El noventa por ciento del mercado
01:22 Los tribunales
01:52 Ocho semanas después
02:26 La última versión independiente
03:13 El siguiente Windows
03:48 Adónde fue la gente
04:42 La frase de la que se trata
04:57 El otro navegador
05:38 Dos modos, todavía hoy
06:06 Dos navegadores, un verano
06:47 Lo que ya estaba dentro
07:12 Una página que podía preguntar
07:58 AJAX
08:27 Qué más viene de aquí
09:02 Pregunta a tu navegador qué es
09:50 La otra mitad
10:20 Una forma de extenderlo
10:44 Cuatro barras
11:28 Un service pack en vez de un navegador
12:26 Firefox, luego RSA
13:02 ¿Entonces por qué se detuvo?

Los subtítulos están escritos para este vídeo, no generados
automáticamente. Como segunda pista de audio está disponible el inglés
americano.

Todas las imágenes están dibujadas con código; el vídeo no usa
fotografías de archivo.
```

## svenska (`sv`)

```
Internet Explorer 6 — Varför stannade den i fem år?
```

```
I augusti 2001 släppte Microsoft Internet Explorer 6. Nästa version av
webbläsaren kom i oktober 2006.

Fem år och två månader, och däremellan inte en enda ny version av
webbläsaren som nästan alla i världen använde. Och det berodde inte på
att ingen klagade — mitt i den luckan fanns hela webbplatser om vad som
var fel med den.

Det här är del fyra, och den ställer frågan som de tre första aldrig
ställde. Inte vad webbläsaren gjorde med webben. Varför den stannade.

Svaret är inte att Microsoft inte kunde bygga något bättre. De kunde, och
de gjorde det: i mars 2000 släppte de en webbläsare med en annan motor,
utan boxmodellsbuggen som kostade webben ett decennium av kringgående —
och avslutade utvecklingen sex veckor efter beskedet att Internet
Explorer 6 skulle bli den sista versionen man kunde installera separat.

På vägen: kartellmålet vars hot tog slut åtta veckor innan Internet
Explorer 6 kom; onlinechatten där Microsoft sa att webbläsaren nu var en
funktion i Windows; utvecklaren som jobbat med den sedan 1995 och senare
skrev ner varför den stannade; komponenten som byggdes på nittiotalet för
företagspost och som hela den moderna webben sedan byggdes på; skälet
till att din webbläsare fortfarande säger sig vara Mozilla; verktygsfälten
som åt en tredjedel av skärmen; och lösningen som kom som ett servicepack
till operativsystemet i stället för som en ny webbläsare.

Del ett — hur Internet Explorer 6 blev en plattform:
https://youtu.be/R7Un3IOMvbg

Del två — buggarna som hade namn:
https://youtu.be/1dIM5UZUEZg

Del tre — webbläsaren som inte ville dö:
https://youtu.be/dnF3SJoeTns

Kapitel
00:00 Fem år och två månader
00:40 Det här är del fyra
01:01 Nittio procent av marknaden
01:22 Domstolarna
01:52 Åtta veckor senare
02:26 Den sista fristående versionen
03:13 Nästa Windows
03:48 Vart människorna tog vägen
04:42 Meningen det handlar om
04:57 Den andra webbläsaren
05:38 Två lägen, än i dag
06:06 Två webbläsare, en sommar
06:47 Vad som redan fanns inuti
07:12 En sida som kunde fråga
07:58 AJAX
08:27 Vad mer som kommer härifrån
09:02 Fråga din webbläsare vad den är
09:50 Den andra halvan
10:20 Ett sätt att bygga ut den
10:44 Fyra verktygsfält
11:28 Ett servicepack i stället för en webbläsare
12:26 Firefox, sedan RSA
13:02 Så varför stannade den?

Undertexterna är skrivna för den här videon, inte automatgenererade.
Som andra ljudspår finns amerikansk engelska.

Alla bilder är ritade med kod; videon använder inga arkivfoton.
```
