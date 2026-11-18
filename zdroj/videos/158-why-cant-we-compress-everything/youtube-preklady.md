# YouTube — 158, lokalizované názvy a popisy

Podklad pro `tools/lokalizace.py` (`videos.update(part="localizations")`). Anglický titul
a popis jsou v `youtube.md`; tady je třináct překladů v pořadí YouTube Studia.
Formát (nadpis s kódem, v sekci přesně dva bloky: titul, popis) je podle
`docs/zverejneni.md`, kapitola „Lokalizované názvy a popisy".

## Co se NEPŘEKLÁDÁ

- **vlastní jména** osob, firem a programů (Ziv, Lempel, Huffman, Shannon, Hutter, Dropbox,
  gzip, ZIP, JPEG); **Hutter Prize** zůstává anglicky jako vlastní název ceny, shodně
  se `script.cs.md`. V ukrajinštině jsou jména osob v souvislém textu přepsaná cyrilicí
  (Зів, Лемпель, Хаффман, Шеннон), v kreditech a zdrojích zůstává latinka.
- **názvy publikací, časopisů a konferencí v odstavci se zdroji** — přeložené je jen
  slovo „Sources" a závěrečná věta o měřeních;
- **časy kapitol** (beze změny proti `youtube.md`);
- **jména autorů a licence v kreditech obrázků** (i jména portrétovaných v řádcích
  Fano, Hutter, Kolmogorov); přeložené jsou nadpisy, popisky (fotka ledňáčka, portrét,
  oříznuto, překomprimováno, volné dílo) a „via Wikimedia Commons";
- **tagy** — YouTube je per jazyk nemá.

Registr: de Sie, fr vous, it voi, pl 1. osoba množného čísla / neosobně, uk ви, tr siz,
id Anda, cs vykání (jako `script.cs.md`); sv du, es tú, pt-BR você, fi sinä, vi bạn.

Pointa (proč nejde komprimovat všechno, kde je dno) se v popisu neprozrazuje, stejně
jako v originálu.

## suomi (`fi`)

```
Miksi kaikkea ei voi pakata?
```

```
Ota kaikki tälle kanavalle koskaan kirjoitetut käsikirjoitukset, lähes puolitoista miljoonaa tavua tekstiä, ja aja ne gzipin läpi. Lähes kaksi kolmasosaa katoaa, eikä mitään menetetä. Pakkaa tulos sitten uudelleen, ja se kasvaa. Yhdeksänkymmentäkahdeksan tavua suuremmaksi, joka ikinen kerta. Miksi emme siis voi vain jatkaa pakkaamista? Ja voisiko jokin nokkelampi ohjelma joskus kutistaa mitä tahansa, mitä sille annat?

Video käy läpi kaksi temppua, joihin ZIP ja gzip perustuvat: Jacob Zivin ja Abraham Lempelin viittaukset takaisin aiempaan tekstiin sekä David Huffmanin koodin, joka syntyi seminaarityöstä, jonka hän oli jo melkein jättänyt kesken. Sitten pieni laskupulma kolmen bitin tiedostoilla, vuoden 1992 tuote, joka väitti olevansa vapautettu informaatioteorian laeista, miksi JPEG pelaa eri peliä, Claude Shannonin arvauspeli ja raja, jonka alle mikään häviötön koodi ei pääse, Hutter Prize ja sen puoli miljoonaa euroa Wikipedian puristamisesta, miten Dropbox säästi 46 petatavua kuvissa, jotka se oli jo tallentanut, suuri kielimalli pakkaajana sekä piin miljoonan numeron kummallinen tapaus.

Lähteet: J. Ziv and A. Lempel, A Universal Algorithm for Sequential Data Compression, IEEE Transactions on Information Theory (1977); D. A. Huffman, A Method for the Construction of Minimum-Redundancy Codes, Proceedings of the IRE (1952); G. Stix, Profile: David A. Huffman, Scientific American (1991); P. Deutsch, RFC 1951 and RFC 1952 (1996); C. E. Shannon, A Mathematical Theory of Communication (1948); C. E. Shannon, Prediction and Entropy of Printed English, Bell System Technical Journal (1951); J.-l. Gailly, comp.compression FAQ (1999); D. R. Horn et al., The Design, Implementation, and Deployment of a System to Transparently Compress Hundreds of Petabytes of Image Files for a File-Storage Service, NSDI (2017); M. Hutter, Hutter Prize for Lossless Compression of Human Knowledge (prize.hutter1.net); M. Mahoney, Large Text Compression Benchmark; G. Delétang et al., Language Modeling Is Compression, ICLR (2024); A. N. Kolmogorov, Three Approaches to the Quantitative Definition of Information (1965); G. J. Chaitin, Information-Theoretic Limitations of Formal Systems (1974). Mittaukset gzipillä ja piillä tehtiin tätä videota varten.

Tekstitykset on kirjoitettu tätä videota varten, eivätkä ne ole automaattisesti luotuja. Toisena ääniraitana on saatavilla amerikanenglanti.

Koko teksti, lähteet ja käännökset: https://theresmoretoit-channel.github.io/fi/videos/why-cant-we-compress-everything/

LUVUT
00:00 Kaikki kanavan käsikirjoitukset pakattuina
00:24 Pakkaa se uudelleen
00:46 Toisen tiedoston sisällä
01:17 Viittauksia toistoihin
01:44 Huffmanin seminaarityö
02:38 ZIP ja gzip
02:58 Pystyisikö nokkelampi ohjelma siihen?
04:16 Ohjelmisto, joka lupasi liikoja
04:39 Miten valokuvista tulee niin pieniä?
05:08 Onko olemassa alaraja?
05:45 Shannonin arvauspeli
06:28 Hutter Prize
07:14 Ennustavat ohjelmat
07:59 Kielimalli pakkaajana
08:40 Miljoona piin numeroa
09:24 Lyhin ohjelma
10:11 Mitä gzip ei näe

KUVALÄHTEET
Robert Fano — 121a0012, CC BY 3.0
Marcus Hutter — Marcus Hutter, CC BY-SA 4.0
Andrey Kolmogorov — Konrad Jacobs, CC BY-SA 2.0 DE
Kuningaskalastajan kuva — Alexis LOURS, CC BY 2.0 (rajattu, pakattu uudelleen)
Wikimedia Commonsin kautta
Lisenssit: creativecommons.org/licenses/by/3.0, creativecommons.org/licenses/by-sa/4.0, creativecommons.org/licenses/by-sa/2.0/de, creativecommons.org/licenses/by/2.0
Claude Shannonin muotokuva — MIT Photo Service, public domain (vapaasti käytettävä)
```

## français (`fr`)

```
Pourquoi ne peut-on pas tout compresser ?
```

```
Prenez tous les scripts jamais écrits pour cette chaîne, près d’un million et demi d’octets de texte, et passez-les dans gzip. Près des deux tiers disparaissent, et rien n’est perdu. Compressez maintenant le résultat une deuxième fois : il grossit. De quatre-vingt-dix-huit octets, à chaque fois. Alors pourquoi ne pas continuer à compresser ? Et un programme plus astucieux pourrait-il un jour réduire tout ce que vous lui donnez ?

Cette vidéo explique les deux astuces au cœur de ZIP et de gzip : les renvois à des passages antérieurs, imaginés par Jacob Ziv et Abraham Lempel, et le code de David Huffman, né d’un devoir universitaire qu’il avait failli abandonner. Puis une petite énigme de dénombrement avec des fichiers de trois bits, un produit de 1992 qui se disait affranchi des lois de la théorie de l’information, pourquoi le JPEG joue à un autre jeu, le jeu de devinettes de Claude Shannon et la limite en dessous de laquelle aucun code sans perte ne peut descendre, le Hutter Prize et son demi-million d’euros pour comprimer Wikipédia, comment Dropbox a économisé 46 pétaoctets sur des photos qu’il stockait déjà, un grand modèle de langage utilisé comme compresseur, et l’étrange cas d’un million de chiffres de pi.

Sources : J. Ziv and A. Lempel, A Universal Algorithm for Sequential Data Compression, IEEE Transactions on Information Theory (1977); D. A. Huffman, A Method for the Construction of Minimum-Redundancy Codes, Proceedings of the IRE (1952); G. Stix, Profile: David A. Huffman, Scientific American (1991); P. Deutsch, RFC 1951 and RFC 1952 (1996); C. E. Shannon, A Mathematical Theory of Communication (1948); C. E. Shannon, Prediction and Entropy of Printed English, Bell System Technical Journal (1951); J.-l. Gailly, comp.compression FAQ (1999); D. R. Horn et al., The Design, Implementation, and Deployment of a System to Transparently Compress Hundreds of Petabytes of Image Files for a File-Storage Service, NSDI (2017); M. Hutter, Hutter Prize for Lossless Compression of Human Knowledge (prize.hutter1.net); M. Mahoney, Large Text Compression Benchmark; G. Delétang et al., Language Modeling Is Compression, ICLR (2024); A. N. Kolmogorov, Three Approaches to the Quantitative Definition of Information (1965); G. J. Chaitin, Information-Theoretic Limitations of Formal Systems (1974). Les mesures avec gzip et avec pi ont été réalisées pour cette vidéo.

Les sous-titres ont été écrits pour cette vidéo, ils ne sont pas générés automatiquement. Une version en anglais américain est disponible en deuxième piste audio.

Transcription complète, sources et traductions : https://theresmoretoit-channel.github.io/fr/videos/why-cant-we-compress-everything/

CHAPITRES
00:00 Tous les scripts de la chaîne, compressés
00:24 On recompresse
00:46 Dans le deuxième fichier
01:17 Renvoyer aux répétitions
01:44 Le devoir de Huffman
02:38 ZIP et gzip
02:58 Un programme plus astucieux y arriverait-il ?
04:16 Le logiciel qui promettait trop
04:39 Comment les photos deviennent-elles si petites ?
05:08 Y a-t-il un plancher ?
05:45 Le jeu de devinettes de Shannon
06:28 Le Hutter Prize
07:14 Des programmes qui prédisent
07:59 Un modèle de langage comme compresseur
08:40 Un million de chiffres de pi
09:24 Le programme le plus court
10:11 Ce que gzip ne voit pas

CRÉDITS DES IMAGES
Robert Fano — 121a0012, CC BY 3.0
Marcus Hutter — Marcus Hutter, CC BY-SA 4.0
Andrey Kolmogorov — Konrad Jacobs, CC BY-SA 2.0 DE
Photo de martin-pêcheur — Alexis LOURS, CC BY 2.0 (recadrée, recompressée)
via Wikimedia Commons
Licences : creativecommons.org/licenses/by/3.0, creativecommons.org/licenses/by-sa/4.0, creativecommons.org/licenses/by-sa/2.0/de, creativecommons.org/licenses/by/2.0
Portrait de Claude Shannon — MIT Photo Service, domaine public
```

## Bahasa Indonesia (`id`)

```
Mengapa Kita Tidak Bisa Mengompresi Segalanya?
```

```
Ambil semua naskah yang pernah ditulis untuk kanal ini, hampir satu setengah juta byte teks, lalu jalankan melalui gzip. Hampir dua pertiganya lenyap, dan tidak ada yang hilang. Sekarang kompres hasilnya sekali lagi, dan ukurannya malah bertambah. Sembilan puluh delapan byte lebih besar, setiap kali. Lalu mengapa kita tidak bisa terus mengompresi? Dan mungkinkah suatu hari program yang lebih cerdik bisa memperkecil apa pun yang Anda berikan kepadanya?

Video ini membahas dua trik di dalam ZIP dan gzip: penunjuk ke teks sebelumnya dari Jacob Ziv dan Abraham Lempel, serta kode David Huffman yang lahir dari makalah kuliah yang hampir ia tinggalkan. Lalu teka-teki hitungan kecil dengan berkas tiga bit, produk tahun 1992 yang mengaku kebal terhadap hukum teori informasi, mengapa JPEG bekerja dengan aturan yang berbeda, permainan tebak-tebakan Claude Shannon dan batas bawah yang tidak bisa dilewati ke bawah oleh kode lossless mana pun, Hutter Prize dan hadiah setengah juta euronya untuk memampatkan Wikipedia, bagaimana Dropbox menghemat 46 petabyte pada foto yang sudah disimpannya, model bahasa besar yang dipakai sebagai kompresor, dan kasus aneh sejuta digit pi.

Sumber: J. Ziv and A. Lempel, A Universal Algorithm for Sequential Data Compression, IEEE Transactions on Information Theory (1977); D. A. Huffman, A Method for the Construction of Minimum-Redundancy Codes, Proceedings of the IRE (1952); G. Stix, Profile: David A. Huffman, Scientific American (1991); P. Deutsch, RFC 1951 and RFC 1952 (1996); C. E. Shannon, A Mathematical Theory of Communication (1948); C. E. Shannon, Prediction and Entropy of Printed English, Bell System Technical Journal (1951); J.-l. Gailly, comp.compression FAQ (1999); D. R. Horn et al., The Design, Implementation, and Deployment of a System to Transparently Compress Hundreds of Petabytes of Image Files for a File-Storage Service, NSDI (2017); M. Hutter, Hutter Prize for Lossless Compression of Human Knowledge (prize.hutter1.net); M. Mahoney, Large Text Compression Benchmark; G. Delétang et al., Language Modeling Is Compression, ICLR (2024); A. N. Kolmogorov, Three Approaches to the Quantitative Definition of Information (1965); G. J. Chaitin, Information-Theoretic Limitations of Formal Systems (1974). Pengukuran dengan gzip dan pi dilakukan khusus untuk video ini.

Subtitel ditulis khusus untuk video ini, bukan dibuat otomatis. Trek audio bahasa Inggris Amerika tersedia sebagai trek audio kedua.

Transkrip lengkap, sumber, dan terjemahan: https://theresmoretoit-channel.github.io/id/videos/why-cant-we-compress-everything/

BAB
00:00 Semua naskah kanal ini, dikompresi
00:24 Kompres sekali lagi
00:46 Di dalam berkas kedua
01:17 Menunjuk ke pengulangan
01:44 Makalah kuliah Huffman
02:38 ZIP dan gzip
02:58 Bisakah program yang lebih cerdik melakukannya?
04:16 Perangkat lunak yang terlalu banyak berjanji
04:39 Bagaimana foto bisa sekecil itu?
05:08 Adakah batas bawahnya?
05:45 Permainan tebak-tebakan Shannon
06:28 Hutter Prize
07:14 Program yang memprediksi
07:59 Model bahasa sebagai kompresor
08:40 Sejuta digit pi
09:24 Program terpendek
10:11 Yang tidak terlihat oleh gzip

KREDIT GAMBAR
Robert Fano — 121a0012, CC BY 3.0
Marcus Hutter — Marcus Hutter, CC BY-SA 4.0
Andrey Kolmogorov — Konrad Jacobs, CC BY-SA 2.0 DE
Foto burung raja-udang — Alexis LOURS, CC BY 2.0 (dipotong, dikompresi ulang)
melalui Wikimedia Commons
Lisensi: creativecommons.org/licenses/by/3.0, creativecommons.org/licenses/by-sa/4.0, creativecommons.org/licenses/by-sa/2.0/de, creativecommons.org/licenses/by/2.0
Potret Claude Shannon — MIT Photo Service, domain publik
```

## italiano (`it`)

```
Perché non si può comprimere tutto?
```

```
Prendete tutti i copioni mai scritti per questo canale, quasi un milione e mezzo di byte di testo, e passateli a gzip. Quasi due terzi spariscono, e non si perde nulla. Ora comprimete di nuovo il risultato: diventa più grande. Di novantotto byte, ogni singola volta. Allora perché non possiamo continuare a comprimere? E un programma più astuto potrebbe, un giorno, rimpicciolire qualsiasi cosa gli diate?

Il video spiega i due trucchi dentro ZIP e gzip: i rimandi al testo precedente di Jacob Ziv e Abraham Lempel, e il codice di David Huffman, nato da una tesina a cui aveva quasi rinunciato. Poi un piccolo rompicapo di conteggio con file da tre bit, un prodotto del 1992 che si diceva esente dalle leggi della teoria dell’informazione, perché il JPEG gioca un’altra partita, il gioco delle previsioni di Claude Shannon e il limite al di sotto del quale nessun codice senza perdita può scendere, l’Hutter Prize e il suo mezzo milione di euro per comprimere Wikipedia, come Dropbox ha risparmiato 46 petabyte su foto che aveva già archiviato, un grande modello linguistico usato come compressore, e lo strano caso di un milione di cifre di pi greco.

Fonti: J. Ziv and A. Lempel, A Universal Algorithm for Sequential Data Compression, IEEE Transactions on Information Theory (1977); D. A. Huffman, A Method for the Construction of Minimum-Redundancy Codes, Proceedings of the IRE (1952); G. Stix, Profile: David A. Huffman, Scientific American (1991); P. Deutsch, RFC 1951 and RFC 1952 (1996); C. E. Shannon, A Mathematical Theory of Communication (1948); C. E. Shannon, Prediction and Entropy of Printed English, Bell System Technical Journal (1951); J.-l. Gailly, comp.compression FAQ (1999); D. R. Horn et al., The Design, Implementation, and Deployment of a System to Transparently Compress Hundreds of Petabytes of Image Files for a File-Storage Service, NSDI (2017); M. Hutter, Hutter Prize for Lossless Compression of Human Knowledge (prize.hutter1.net); M. Mahoney, Large Text Compression Benchmark; G. Delétang et al., Language Modeling Is Compression, ICLR (2024); A. N. Kolmogorov, Three Approaches to the Quantitative Definition of Information (1965); G. J. Chaitin, Information-Theoretic Limitations of Formal Systems (1974). Le misurazioni con gzip e con pi greco sono state fatte per questo video.

I sottotitoli sono scritti per questo video, non generati automaticamente. È disponibile una seconda traccia audio in inglese americano.

Trascrizione completa, fonti e traduzioni: https://theresmoretoit-channel.github.io/it/videos/why-cant-we-compress-everything/

CAPITOLI
00:00 Tutti i copioni del canale, compressi
00:24 Comprimerlo di nuovo
00:46 Dentro il secondo file
01:17 Rimandi alle ripetizioni
01:44 La tesina di Huffman
02:38 ZIP e gzip
02:58 Un programma più astuto ce la farebbe?
04:16 Il software che prometteva troppo
04:39 Come fanno le foto a diventare così piccole?
05:08 C’è un minimo?
05:45 Il gioco delle previsioni di Shannon
06:28 L’Hutter Prize
07:14 Programmi che prevedono
07:59 Un modello linguistico come compressore
08:40 Un milione di cifre di pi greco
09:24 Il programma più corto
10:11 Quello che gzip non vede

CREDITI DELLE IMMAGINI
Robert Fano — 121a0012, CC BY 3.0
Marcus Hutter — Marcus Hutter, CC BY-SA 4.0
Andrey Kolmogorov — Konrad Jacobs, CC BY-SA 2.0 DE
Foto del martin pescatore — Alexis LOURS, CC BY 2.0 (ritagliata, ricompressa)
tramite Wikimedia Commons
Licenze: creativecommons.org/licenses/by/3.0, creativecommons.org/licenses/by-sa/4.0, creativecommons.org/licenses/by-sa/2.0/de, creativecommons.org/licenses/by/2.0
Ritratto di Claude Shannon — MIT Photo Service, pubblico dominio
```

## Deutsch (`de`)

```
Warum kann man nicht alles komprimieren?
```

```
Nehmen Sie alle Skripte, die je für diesen Kanal geschrieben wurden, fast anderthalb Millionen Bytes Text, und jagen Sie sie durch gzip. Fast zwei Drittel verschwinden, und nichts geht verloren. Komprimieren Sie das Ergebnis jetzt noch einmal, und es wird größer. Achtundneunzig Bytes größer, jedes einzelne Mal. Warum können wir also nicht einfach weiter komprimieren? Und könnte ein klügeres Programm eines Tages alles verkleinern, was Sie ihm geben?

Das Video geht die zwei Tricks in ZIP und gzip durch: die Verweise auf früheren Text von Jacob Ziv und Abraham Lempel und den Code von David Huffman aus einer Hausarbeit, die er beinahe aufgegeben hätte. Dann ein kleines Zählrätsel mit Drei-Bit-Dateien, ein Produkt von 1992, das sich von den Gesetzen der Informationstheorie ausgenommen erklärte, warum JPEG ein anderes Spiel spielt, Claude Shannons Ratespiel und die Grenze, die kein verlustfreier Code unterbieten kann, der Hutter Prize und seine halbe Million Euro für das Zusammenpressen der Wikipedia, wie Dropbox 46 Petabyte bei Fotos einsparte, die längst gespeichert waren, ein großes Sprachmodell als Kompressor und der seltsame Fall von einer Million Ziffern von Pi.

Quellen: J. Ziv and A. Lempel, A Universal Algorithm for Sequential Data Compression, IEEE Transactions on Information Theory (1977); D. A. Huffman, A Method for the Construction of Minimum-Redundancy Codes, Proceedings of the IRE (1952); G. Stix, Profile: David A. Huffman, Scientific American (1991); P. Deutsch, RFC 1951 and RFC 1952 (1996); C. E. Shannon, A Mathematical Theory of Communication (1948); C. E. Shannon, Prediction and Entropy of Printed English, Bell System Technical Journal (1951); J.-l. Gailly, comp.compression FAQ (1999); D. R. Horn et al., The Design, Implementation, and Deployment of a System to Transparently Compress Hundreds of Petabytes of Image Files for a File-Storage Service, NSDI (2017); M. Hutter, Hutter Prize for Lossless Compression of Human Knowledge (prize.hutter1.net); M. Mahoney, Large Text Compression Benchmark; G. Delétang et al., Language Modeling Is Compression, ICLR (2024); A. N. Kolmogorov, Three Approaches to the Quantitative Definition of Information (1965); G. J. Chaitin, Information-Theoretic Limitations of Formal Systems (1974). Die Messungen mit gzip und mit Pi wurden für dieses Video durchgeführt.

Die Untertitel wurden für dieses Video geschrieben, nicht automatisch erzeugt. Eine Tonspur in amerikanischem Englisch ist als zweite Audiospur verfügbar.

Vollständiger Text, Quellen und Übersetzungen: https://theresmoretoit-channel.github.io/de/videos/why-cant-we-compress-everything/

KAPITEL
00:00 Alle Skripte dieses Kanals, komprimiert
00:24 Noch einmal komprimieren
00:46 In der zweiten Datei
01:17 Verweise auf Wiederholungen
01:44 Huffmans Hausarbeit
02:38 ZIP und gzip
02:58 Könnte ein klügeres Programm es schaffen?
04:16 Software, die zu viel versprach
04:39 Wie werden Fotos so klein?
05:08 Gibt es eine Untergrenze?
05:45 Shannons Ratespiel
06:28 Der Hutter Prize
07:14 Programme, die vorhersagen
07:59 Ein Sprachmodell als Kompressor
08:40 Eine Million Ziffern von Pi
09:24 Das kürzeste Programm
10:11 Was gzip nicht sieht

BILDNACHWEISE
Robert Fano — 121a0012, CC BY 3.0
Marcus Hutter — Marcus Hutter, CC BY-SA 4.0
Andrey Kolmogorov — Konrad Jacobs, CC BY-SA 2.0 DE
Eisvogel-Foto — Alexis LOURS, CC BY 2.0 (zugeschnitten, neu komprimiert)
über Wikimedia Commons
Lizenzen: creativecommons.org/licenses/by/3.0, creativecommons.org/licenses/by-sa/4.0, creativecommons.org/licenses/by-sa/2.0/de, creativecommons.org/licenses/by/2.0
Porträt von Claude Shannon — MIT Photo Service, gemeinfrei
```

## polski (`pl`)

```
Dlaczego nie da się skompresować wszystkiego?
```

```
Weźmy wszystkie scenariusze, jakie kiedykolwiek powstały dla tego kanału, prawie półtora miliona bajtów tekstu, i przepuśćmy je przez gzip. Prawie dwie trzecie znikają, a nic nie ginie. Teraz skompresujmy wynik jeszcze raz — i robi się większy. O dziewięćdziesiąt osiem bajtów, za każdym razem. Dlaczego więc nie można po prostu kompresować dalej? I czy sprytniejszy program mógłby kiedyś zmniejszyć wszystko, co mu się da?

Film omawia dwie sztuczki, na których opierają się ZIP i gzip: odwołania do wcześniejszego tekstu Jacoba Ziva i Abrahama Lempela oraz kod Davida Huffmana z pracy semestralnej, z której prawie zrezygnował. Potem mała łamigłówka z liczeniem plików trzybitowych, produkt z 1992 roku, którego twórcy twierdzili, że nie podlega prawom teorii informacji, dlaczego JPEG gra w inną grę, gra w zgadywanie Claude’a Shannona i granica, poniżej której nie zejdzie żaden kod bezstratny, nagroda Hutter Prize i jej pół miliona euro za ściśnięcie Wikipedii, jak Dropbox zaoszczędził 46 petabajtów na zdjęciach, które już przechowywał, duży model językowy w roli kompresora i dziwny przypadek miliona cyfr liczby pi.

Źródła: J. Ziv and A. Lempel, A Universal Algorithm for Sequential Data Compression, IEEE Transactions on Information Theory (1977); D. A. Huffman, A Method for the Construction of Minimum-Redundancy Codes, Proceedings of the IRE (1952); G. Stix, Profile: David A. Huffman, Scientific American (1991); P. Deutsch, RFC 1951 and RFC 1952 (1996); C. E. Shannon, A Mathematical Theory of Communication (1948); C. E. Shannon, Prediction and Entropy of Printed English, Bell System Technical Journal (1951); J.-l. Gailly, comp.compression FAQ (1999); D. R. Horn et al., The Design, Implementation, and Deployment of a System to Transparently Compress Hundreds of Petabytes of Image Files for a File-Storage Service, NSDI (2017); M. Hutter, Hutter Prize for Lossless Compression of Human Knowledge (prize.hutter1.net); M. Mahoney, Large Text Compression Benchmark; G. Delétang et al., Language Modeling Is Compression, ICLR (2024); A. N. Kolmogorov, Three Approaches to the Quantitative Definition of Information (1965); G. J. Chaitin, Information-Theoretic Limitations of Formal Systems (1974). Pomiary z gzipem i liczbą pi wykonano na potrzeby tego filmu.

Napisy przygotowano specjalnie do tego filmu, nie są generowane automatycznie. Jako druga ścieżka dźwiękowa dostępna jest wersja w amerykańskim angielskim.

Pełna transkrypcja, źródła i tłumaczenia: https://theresmoretoit-channel.github.io/pl/videos/why-cant-we-compress-everything/

ROZDZIAŁY
00:00 Wszystkie scenariusze kanału, skompresowane
00:24 Kompresja jeszcze raz
00:46 Wewnątrz drugiego pliku
01:17 Odwołania do powtórzeń
01:44 Praca semestralna Huffmana
02:38 ZIP i gzip
02:58 Czy sprytniejszy program dałby radę?
04:16 Oprogramowanie, które obiecywało za dużo
04:39 Jak zdjęcia stają się tak małe?
05:08 Czy istnieje dolna granica?
05:45 Gra w zgadywanie Shannona
06:28 Hutter Prize
07:14 Programy, które przewidują
07:59 Model językowy jako kompresor
08:40 Milion cyfr liczby pi
09:24 Najkrótszy program
10:11 Czego gzip nie widzi

ŹRÓDŁA ILUSTRACJI
Robert Fano — 121a0012, CC BY 3.0
Marcus Hutter — Marcus Hutter, CC BY-SA 4.0
Andrey Kolmogorov — Konrad Jacobs, CC BY-SA 2.0 DE
Zdjęcie zimorodka — Alexis LOURS, CC BY 2.0 (przycięte, ponownie skompresowane)
za pośrednictwem Wikimedia Commons
Licencje: creativecommons.org/licenses/by/3.0, creativecommons.org/licenses/by-sa/4.0, creativecommons.org/licenses/by-sa/2.0/de, creativecommons.org/licenses/by/2.0
Portret Claude’a Shannona — MIT Photo Service, domena publiczna
```

## português (Brasil) (`pt-BR`)

```
Por que não dá para comprimir tudo?
```

```
Pegue todos os roteiros já escritos para este canal, quase um milhão e meio de bytes de texto, e passe tudo pelo gzip. Quase dois terços desaparecem, e nada se perde. Agora comprima o resultado de novo, e ele fica maior. Noventa e oito bytes maior, toda vez. Então por que não dá para continuar comprimindo? E será que um programa mais esperto conseguiria, um dia, encolher qualquer coisa que você der a ele?

O vídeo mostra os dois truques dentro do ZIP e do gzip: as referências ao texto anterior de Jacob Ziv e Abraham Lempel, e o código de David Huffman, nascido de um trabalho de faculdade que ele quase abandonou. Depois, um pequeno quebra-cabeça de contagem com arquivos de três bits, um produto de 1992 que dizia estar isento das leis da teoria da informação, por que o JPEG joga outro jogo, o jogo de adivinhação de Claude Shannon e o limite abaixo do qual nenhum código sem perdas consegue chegar, o Hutter Prize e seu meio milhão de euros para espremer a Wikipédia, como o Dropbox economizou 46 petabytes em fotos que já tinha armazenadas, um grande modelo de linguagem usado como compressor, e o estranho caso de um milhão de dígitos de pi.

Fontes: J. Ziv and A. Lempel, A Universal Algorithm for Sequential Data Compression, IEEE Transactions on Information Theory (1977); D. A. Huffman, A Method for the Construction of Minimum-Redundancy Codes, Proceedings of the IRE (1952); G. Stix, Profile: David A. Huffman, Scientific American (1991); P. Deutsch, RFC 1951 and RFC 1952 (1996); C. E. Shannon, A Mathematical Theory of Communication (1948); C. E. Shannon, Prediction and Entropy of Printed English, Bell System Technical Journal (1951); J.-l. Gailly, comp.compression FAQ (1999); D. R. Horn et al., The Design, Implementation, and Deployment of a System to Transparently Compress Hundreds of Petabytes of Image Files for a File-Storage Service, NSDI (2017); M. Hutter, Hutter Prize for Lossless Compression of Human Knowledge (prize.hutter1.net); M. Mahoney, Large Text Compression Benchmark; G. Delétang et al., Language Modeling Is Compression, ICLR (2024); A. N. Kolmogorov, Three Approaches to the Quantitative Definition of Information (1965); G. J. Chaitin, Information-Theoretic Limitations of Formal Systems (1974). As medições com gzip e com pi foram feitas para este vídeo.

As legendas foram escritas para este vídeo, não geradas automaticamente. Uma faixa de áudio em inglês americano está disponível como segunda faixa de áudio.

Transcrição completa, fontes e traduções: https://theresmoretoit-channel.github.io/pt-br/videos/why-cant-we-compress-everything/

CAPÍTULOS
00:00 Todos os roteiros do canal, comprimidos
00:24 Comprimir de novo
00:46 Dentro do segundo arquivo
01:17 Apontando para as repetições
01:44 O trabalho de faculdade de Huffman
02:38 ZIP e gzip
02:58 Um programa mais esperto conseguiria?
04:16 O software que prometeu demais
04:39 Como as fotos ficam tão pequenas?
05:08 Existe um limite mínimo?
05:45 O jogo de adivinhação de Shannon
06:28 O Hutter Prize
07:14 Programas que preveem
07:59 Um modelo de linguagem como compressor
08:40 Um milhão de dígitos de pi
09:24 O programa mais curto
10:11 O que o gzip não vê

CRÉDITOS DAS IMAGENS
Robert Fano — 121a0012, CC BY 3.0
Marcus Hutter — Marcus Hutter, CC BY-SA 4.0
Andrey Kolmogorov — Konrad Jacobs, CC BY-SA 2.0 DE
Foto do martim-pescador — Alexis LOURS, CC BY 2.0 (recortada, recomprimida)
via Wikimedia Commons
Licenças: creativecommons.org/licenses/by/3.0, creativecommons.org/licenses/by-sa/4.0, creativecommons.org/licenses/by-sa/2.0/de, creativecommons.org/licenses/by/2.0
Retrato de Claude Shannon — MIT Photo Service, domínio público
```

## Türkçe (`tr`)

```
Neden Her Şeyi Sıkıştıramıyoruz?
```

```
Bu kanal için yazılmış bütün metinleri alın, neredeyse bir buçuk milyon baytlık metin, ve gzip’ten geçirin. Neredeyse üçte ikisi yok olur ve hiçbir şey kaybolmaz. Şimdi sonucu yeniden sıkıştırın: büyür. Her seferinde tam doksan sekiz bayt büyür. Peki neden sıkıştırmaya devam edemiyoruz? Ve daha akıllı bir program bir gün ona verdiğiniz her şeyi küçültebilir mi?

Bu video, ZIP ve gzip’in içindeki iki hileyi anlatıyor: Jacob Ziv ile Abraham Lempel’in önceki metne geri gösteren işaretçileri ve David Huffman’ın neredeyse vazgeçtiği bir dönem ödevinden doğan kodu. Ardından üç bitlik dosyalarla küçük bir sayma bulmacası, bilgi teorisinin yasalarından muaf olduğunu iddia eden 1992 tarihli bir ürün, JPEG’in neden başka bir oyun oynadığı, Claude Shannon’ın tahmin oyunu ve hiçbir kayıpsız kodun altına inemeyeceği sınır, Hutter Prize ve Wikipedia’yı sıkıştırmak için verilen yarım milyon avro, Dropbox’ın zaten depoladığı fotoğraflarda 46 petabaytlık alandan nasıl tasarruf ettiği, sıkıştırıcı olarak kullanılan büyük bir dil modeli ve pi sayısının bir milyon basamağının tuhaf hikâyesi.

Kaynaklar: J. Ziv and A. Lempel, A Universal Algorithm for Sequential Data Compression, IEEE Transactions on Information Theory (1977); D. A. Huffman, A Method for the Construction of Minimum-Redundancy Codes, Proceedings of the IRE (1952); G. Stix, Profile: David A. Huffman, Scientific American (1991); P. Deutsch, RFC 1951 and RFC 1952 (1996); C. E. Shannon, A Mathematical Theory of Communication (1948); C. E. Shannon, Prediction and Entropy of Printed English, Bell System Technical Journal (1951); J.-l. Gailly, comp.compression FAQ (1999); D. R. Horn et al., The Design, Implementation, and Deployment of a System to Transparently Compress Hundreds of Petabytes of Image Files for a File-Storage Service, NSDI (2017); M. Hutter, Hutter Prize for Lossless Compression of Human Knowledge (prize.hutter1.net); M. Mahoney, Large Text Compression Benchmark; G. Delétang et al., Language Modeling Is Compression, ICLR (2024); A. N. Kolmogorov, Three Approaches to the Quantitative Definition of Information (1965); G. J. Chaitin, Information-Theoretic Limitations of Formal Systems (1974). Bu video için gzip ve pi ile ölçümler yapıldı.

Altyazılar bu video için yazıldı, otomatik olarak oluşturulmadı. İkinci ses parçası olarak Amerikan İngilizcesi de mevcuttur.

Metnin tamamı, kaynaklar ve çeviriler: https://theresmoretoit-channel.github.io/tr/videos/why-cant-we-compress-everything/

BÖLÜMLER
00:00 Bu kanaldaki bütün metinler, sıkıştırılmış
00:24 Bir kez daha sıkıştırın
00:46 İkinci dosyanın içinde
01:17 Tekrarlara geri işaret etmek
01:44 Huffman’ın dönem ödevi
02:38 ZIP ve gzip
02:58 Daha akıllı bir program başarabilir mi?
04:16 Fazla vaat eden yazılım
04:39 Fotoğraflar nasıl bu kadar küçülüyor?
05:08 Bir alt sınır var mı?
05:45 Shannon’ın tahmin oyunu
06:28 Hutter Prize
07:14 Tahmin eden programlar
07:59 Sıkıştırıcı olarak dil modeli
08:40 Pi’nin bir milyon basamağı
09:24 En kısa program
10:11 gzip’in göremedikleri

GÖRSEL KAYNAKLARI
Robert Fano — 121a0012, CC BY 3.0
Marcus Hutter — Marcus Hutter, CC BY-SA 4.0
Andrey Kolmogorov — Konrad Jacobs, CC BY-SA 2.0 DE
Yalıçapkını fotoğrafı — Alexis LOURS, CC BY 2.0 (kırpıldı, yeniden sıkıştırıldı)
Wikimedia Commons aracılığıyla
Lisanslar: creativecommons.org/licenses/by/3.0, creativecommons.org/licenses/by-sa/4.0, creativecommons.org/licenses/by-sa/2.0/de, creativecommons.org/licenses/by/2.0
Claude Shannon portresi — MIT Photo Service, kamu malı
```

## українська (`uk`)

```
Чому не можна стиснути все?
```

```
Візьміть усі сценарії, які будь-коли написали для цього каналу, — майже півтора мільйона байтів тексту — і проженіть їх через gzip. Майже дві третини зникають, і нічого не втрачається. Тепер стисніть результат ще раз — і він стає більшим. На дев’яносто вісім байтів, щоразу. То чому ж не можна просто стискати далі? І чи зможе колись хитріша програма зменшити будь-що, що ви їй дасте?

У відео розібрано два трюки, на яких тримаються ZIP і gzip: посилання назад на попередній текст від Якоба Зіва та Абрахама Лемпеля і код Девіда Хаффмана з курсової роботи, яку він мало не покинув. Потім невелика задачка на підрахунок із трибітовими файлами, продукт 1992 року, який нібито не підлягав законам теорії інформації, чому JPEG грає в іншу гру, гра у вгадування Клода Шеннона і межа, нижче якої не опуститься жоден код без втрат, премія Hutter Prize і її пів мільйона євро за стиснення Вікіпедії, як Dropbox заощадив 46 петабайтів на фото, які вже зберігав, велика мовна модель у ролі компресора і дивна історія мільйона цифр числа пі.

Джерела: J. Ziv and A. Lempel, A Universal Algorithm for Sequential Data Compression, IEEE Transactions on Information Theory (1977); D. A. Huffman, A Method for the Construction of Minimum-Redundancy Codes, Proceedings of the IRE (1952); G. Stix, Profile: David A. Huffman, Scientific American (1991); P. Deutsch, RFC 1951 and RFC 1952 (1996); C. E. Shannon, A Mathematical Theory of Communication (1948); C. E. Shannon, Prediction and Entropy of Printed English, Bell System Technical Journal (1951); J.-l. Gailly, comp.compression FAQ (1999); D. R. Horn et al., The Design, Implementation, and Deployment of a System to Transparently Compress Hundreds of Petabytes of Image Files for a File-Storage Service, NSDI (2017); M. Hutter, Hutter Prize for Lossless Compression of Human Knowledge (prize.hutter1.net); M. Mahoney, Large Text Compression Benchmark; G. Delétang et al., Language Modeling Is Compression, ICLR (2024); A. N. Kolmogorov, Three Approaches to the Quantitative Definition of Information (1965); G. J. Chaitin, Information-Theoretic Limitations of Formal Systems (1974). Вимірювання з gzip і числом пі зроблено для цього відео.

Субтитри написані для цього відео, а не згенеровані автоматично. Як друга звукова доріжка доступна американська англійська.

Повний текст, джерела та переклади: https://theresmoretoit-channel.github.io/uk/videos/why-cant-we-compress-everything/

РОЗДІЛИ
00:00 Усі сценарії каналу, стиснуті
00:24 Стиснути ще раз
00:46 Усередині другого файлу
01:17 Посилання на повтори
01:44 Курсова робота Хаффмана
02:38 ZIP і gzip
02:58 Чи впоралася б хитріша програма?
04:16 Програма, яка обіцяла забагато
04:39 Як фото стають такими маленькими?
05:08 Чи є нижня межа?
05:45 Шеннонова гра у вгадування
06:28 Hutter Prize
07:14 Програми, що передбачають
07:59 Мовна модель як компресор
08:40 Мільйон цифр числа пі
09:24 Найкоротша програма
10:11 Чого не бачить gzip

ДЖЕРЕЛА ЗОБРАЖЕНЬ
Robert Fano — 121a0012, CC BY 3.0
Marcus Hutter — Marcus Hutter, CC BY-SA 4.0
Andrey Kolmogorov — Konrad Jacobs, CC BY-SA 2.0 DE
Фото рибалочки — Alexis LOURS, CC BY 2.0 (обрізано, повторно стиснуто)
через Wikimedia Commons
Ліцензії: creativecommons.org/licenses/by/3.0, creativecommons.org/licenses/by-sa/4.0, creativecommons.org/licenses/by-sa/2.0/de, creativecommons.org/licenses/by/2.0
Claude Shannon, портрет — MIT Photo Service, суспільне надбання
```

## Tiếng Việt (`vi`)

```
Tại sao không thể nén mọi thứ?
```

```
Hãy lấy tất cả kịch bản từng được viết cho kênh này, gần một triệu rưỡi byte văn bản, rồi cho chạy qua gzip. Gần hai phần ba dung lượng biến mất, vậy mà không một chữ nào bị mất. Giờ hãy nén kết quả thêm lần nữa, và nó lại to ra. To hơn chín mươi tám byte, lần nào cũng vậy. Vậy tại sao ta không thể cứ nén mãi? Và liệu một ngày nào đó, một chương trình khéo léo hơn có thể thu nhỏ bất cứ thứ gì bạn đưa cho nó?

Video này giải thích hai thủ thuật bên trong ZIP và gzip: những con trỏ trỏ ngược về đoạn văn bản trước đó của Jacob Ziv và Abraham Lempel, và mã của David Huffman ra đời từ một bài tiểu luận mà ông suýt bỏ dở. Sau đó là một câu đố đếm nhỏ với các tệp ba bit, một sản phẩm năm 1992 tự nhận là không chịu sự chi phối của các định luật lý thuyết thông tin, vì sao JPEG chơi một trò chơi khác, trò chơi đoán chữ của Claude Shannon và giới hạn mà không có mã không mất dữ liệu nào có thể xuống dưới, giải Hutter Prize với nửa triệu euro cho việc nén Wikipedia, cách Dropbox tiết kiệm được 46 petabyte trên những bức ảnh đã lưu sẵn, một mô hình ngôn ngữ lớn được dùng làm bộ nén, và trường hợp kỳ lạ của một triệu chữ số của số pi.

Nguồn: J. Ziv and A. Lempel, A Universal Algorithm for Sequential Data Compression, IEEE Transactions on Information Theory (1977); D. A. Huffman, A Method for the Construction of Minimum-Redundancy Codes, Proceedings of the IRE (1952); G. Stix, Profile: David A. Huffman, Scientific American (1991); P. Deutsch, RFC 1951 and RFC 1952 (1996); C. E. Shannon, A Mathematical Theory of Communication (1948); C. E. Shannon, Prediction and Entropy of Printed English, Bell System Technical Journal (1951); J.-l. Gailly, comp.compression FAQ (1999); D. R. Horn et al., The Design, Implementation, and Deployment of a System to Transparently Compress Hundreds of Petabytes of Image Files for a File-Storage Service, NSDI (2017); M. Hutter, Hutter Prize for Lossless Compression of Human Knowledge (prize.hutter1.net); M. Mahoney, Large Text Compression Benchmark; G. Delétang et al., Language Modeling Is Compression, ICLR (2024); A. N. Kolmogorov, Three Approaches to the Quantitative Definition of Information (1965); G. J. Chaitin, Information-Theoretic Limitations of Formal Systems (1974). Các phép đo với gzip và số pi được thực hiện riêng cho video này.

Phụ đề được viết riêng cho video này, không phải tạo tự động. Bản âm thanh tiếng Anh Mỹ có sẵn dưới dạng bản âm thanh thứ hai.

Toàn văn, nguồn và bản dịch: https://theresmoretoit-channel.github.io/vi/videos/why-cant-we-compress-everything/

CHƯƠNG
00:00 Mọi kịch bản của kênh, sau khi nén
00:24 Nén thêm lần nữa
00:46 Bên trong tệp thứ hai
01:17 Trỏ ngược về chỗ lặp lại
01:44 Bài tiểu luận của Huffman
02:38 ZIP và gzip
02:58 Một chương trình khéo hơn có làm được không?
04:16 Phần mềm hứa quá nhiều
04:39 Sao ảnh lại nhỏ được đến thế?
05:08 Có giới hạn dưới không?
05:45 Trò chơi đoán chữ của Shannon
06:28 Hutter Prize
07:14 Những chương trình biết dự đoán
07:59 Mô hình ngôn ngữ làm bộ nén
08:40 Một triệu chữ số của pi
09:24 Chương trình ngắn nhất
10:11 Điều gzip không thấy

NGUỒN HÌNH ẢNH
Robert Fano — 121a0012, CC BY 3.0
Marcus Hutter — Marcus Hutter, CC BY-SA 4.0
Andrey Kolmogorov — Konrad Jacobs, CC BY-SA 2.0 DE
Ảnh chim bói cá — Alexis LOURS, CC BY 2.0 (đã cắt, nén lại)
qua Wikimedia Commons
Giấy phép: creativecommons.org/licenses/by/3.0, creativecommons.org/licenses/by-sa/4.0, creativecommons.org/licenses/by-sa/2.0/de, creativecommons.org/licenses/by/2.0
Chân dung Claude Shannon — MIT Photo Service, phạm vi công cộng
```

## čeština (`cs`)

```
Proč nejde zkomprimovat všechno?
```

```
Vezměte všechny scénáře, které kdy pro tenhle kanál vznikly, skoro milion a půl bajtů textu, a prožeňte je gzipem. Skoro dvě třetiny zmizí a nic se neztratí. Teď výsledek zkomprimujte znovu – a zvětší se. O 98 bajtů, pokaždé znovu. Tak proč nemůžeme komprimovat pořád dál? A dokázal by jednou nějaký chytřejší program zmenšit cokoli, co mu dáte?

Video vysvětlí dva triky, na kterých stojí ZIP a gzip: odkazy zpět na dřívější text od Jacoba Ziva a Abrahama Lempela a kód Davida Huffmana ze seminární práce, kterou málem vzdal. Pak malá početní hádanka s tříbitovými soubory, produkt z roku 1992, o kterém výrobce tvrdil, že se na něj zákony teorie informace nevztahují, proč JPEG hraje jinou hru, hádací hra Clauda Shannona a mez, pod kterou se žádný bezeztrátový kód nedostane, Hutter Prize s odměnou půl milionu eur za zhuštění Wikipedie, jak Dropbox ušetřil 46 petabajtů na fotkách, které už měl uložené, velký jazykový model v roli kompresoru a podivný případ milionu číslic čísla π.

Zdroje: J. Ziv and A. Lempel, A Universal Algorithm for Sequential Data Compression, IEEE Transactions on Information Theory (1977); D. A. Huffman, A Method for the Construction of Minimum-Redundancy Codes, Proceedings of the IRE (1952); G. Stix, Profile: David A. Huffman, Scientific American (1991); P. Deutsch, RFC 1951 and RFC 1952 (1996); C. E. Shannon, A Mathematical Theory of Communication (1948); C. E. Shannon, Prediction and Entropy of Printed English, Bell System Technical Journal (1951); J.-l. Gailly, comp.compression FAQ (1999); D. R. Horn et al., The Design, Implementation, and Deployment of a System to Transparently Compress Hundreds of Petabytes of Image Files for a File-Storage Service, NSDI (2017); M. Hutter, Hutter Prize for Lossless Compression of Human Knowledge (prize.hutter1.net); M. Mahoney, Large Text Compression Benchmark; G. Delétang et al., Language Modeling Is Compression, ICLR (2024); A. N. Kolmogorov, Three Approaches to the Quantitative Definition of Information (1965); G. J. Chaitin, Information-Theoretic Limitations of Formal Systems (1974). Měření s gzipem a s číslem π vznikla pro toto video.

Titulky jsou k tomuto videu psané, ne automaticky generované. Jako druhá zvuková stopa je k dispozici americká angličtina.

Celý text, zdroje a překlady: https://theresmoretoit-channel.github.io/cs/videos/why-cant-we-compress-everything/

KAPITOLY
00:00 Všechny scénáře kanálu, zkomprimované
00:24 Zkomprimovat ještě jednou
00:46 Uvnitř druhého souboru
01:17 Odkazy zpět na opakování
01:44 Huffmanova seminární práce
02:38 ZIP a gzip
02:58 Zvládl by to chytřejší program?
04:16 Software, který sliboval příliš
04:39 Jak to, že jsou fotky tak malé?
05:08 Je někde dno?
05:45 Shannonova hádací hra
06:28 Hutter Prize
07:14 Programy, které předpovídají
07:59 Jazykový model jako kompresor
08:40 Milion číslic čísla π
09:24 Nejkratší program
10:11 Co gzip nevidí

ZDROJE OBRÁZKŮ
Robert Fano — 121a0012, CC BY 3.0
Marcus Hutter — Marcus Hutter, CC BY-SA 4.0
Andrey Kolmogorov — Konrad Jacobs, CC BY-SA 2.0 DE
Fotka ledňáčka — Alexis LOURS, CC BY 2.0 (oříznuto, znovu zkomprimováno)
z Wikimedia Commons
Licence: creativecommons.org/licenses/by/3.0, creativecommons.org/licenses/by-sa/4.0, creativecommons.org/licenses/by-sa/2.0/de, creativecommons.org/licenses/by/2.0
Portrét Clauda Shannona — MIT Photo Service, volné dílo
```

## español (`es`)

```
¿Por qué no se puede comprimir todo?
```

```
Toma todos los guiones escritos alguna vez para este canal, casi un millón y medio de bytes de texto, y pásalos por gzip. Casi dos tercios desaparecen, y no se pierde nada. Ahora comprime el resultado otra vez, y se hace más grande. Noventa y ocho bytes más grande, cada vez. Entonces, ¿por qué no podemos seguir comprimiendo? ¿Y podría algún día un programa más astuto encoger cualquier cosa que le des?

Este video recorre los dos trucos que hay dentro de ZIP y gzip: las referencias al texto anterior de Jacob Ziv y Abraham Lempel, y el código de David Huffman, salido de un trabajo de curso que casi abandonó. Después, un pequeño acertijo de conteo con archivos de tres bits, un producto de 1992 que decía estar exento de las leyes de la teoría de la información, por qué JPEG juega a otro juego, el juego de adivinar de Claude Shannon y el límite por debajo del cual ningún código sin pérdida puede bajar, el Hutter Prize y su medio millón de euros por exprimir Wikipedia, cómo Dropbox ahorró 46 petabytes en fotos que ya tenía guardadas, un gran modelo de lenguaje usado como compresor, y el extraño caso de un millón de dígitos de pi.

Fuentes: J. Ziv and A. Lempel, A Universal Algorithm for Sequential Data Compression, IEEE Transactions on Information Theory (1977); D. A. Huffman, A Method for the Construction of Minimum-Redundancy Codes, Proceedings of the IRE (1952); G. Stix, Profile: David A. Huffman, Scientific American (1991); P. Deutsch, RFC 1951 and RFC 1952 (1996); C. E. Shannon, A Mathematical Theory of Communication (1948); C. E. Shannon, Prediction and Entropy of Printed English, Bell System Technical Journal (1951); J.-l. Gailly, comp.compression FAQ (1999); D. R. Horn et al., The Design, Implementation, and Deployment of a System to Transparently Compress Hundreds of Petabytes of Image Files for a File-Storage Service, NSDI (2017); M. Hutter, Hutter Prize for Lossless Compression of Human Knowledge (prize.hutter1.net); M. Mahoney, Large Text Compression Benchmark; G. Delétang et al., Language Modeling Is Compression, ICLR (2024); A. N. Kolmogorov, Three Approaches to the Quantitative Definition of Information (1965); G. J. Chaitin, Information-Theoretic Limitations of Formal Systems (1974). Las mediciones con gzip y con pi se hicieron para este video.

Los subtítulos están escritos para este video, no generados automáticamente. Hay una pista de audio en inglés estadounidense disponible como segunda pista de audio.

Transcripción completa, fuentes y traducciones: https://theresmoretoit-channel.github.io/es/videos/why-cant-we-compress-everything/

CAPÍTULOS
00:00 Todos los guiones del canal, comprimidos
00:24 Comprimirlo otra vez
00:46 Dentro del segundo archivo
01:17 Referencias a repeticiones anteriores
01:44 El trabajo de curso de Huffman
02:38 ZIP y gzip
02:58 ¿Podría hacerlo un programa más astuto?
04:16 El software que prometía demasiado
04:39 ¿Cómo se vuelven tan pequeñas las fotos?
05:08 ¿Hay un mínimo?
05:45 El juego de adivinar de Shannon
06:28 El Hutter Prize
07:14 Programas que predicen
07:59 Un modelo de lenguaje como compresor
08:40 Un millón de dígitos de pi
09:24 El programa más corto
10:11 Lo que gzip no ve

CRÉDITOS DE LAS IMÁGENES
Robert Fano — 121a0012, CC BY 3.0
Marcus Hutter — Marcus Hutter, CC BY-SA 4.0
Andrey Kolmogorov — Konrad Jacobs, CC BY-SA 2.0 DE
Foto del martín pescador — Alexis LOURS, CC BY 2.0 (recortada, recomprimida)
vía Wikimedia Commons
Licencias: creativecommons.org/licenses/by/3.0, creativecommons.org/licenses/by-sa/4.0, creativecommons.org/licenses/by-sa/2.0/de, creativecommons.org/licenses/by/2.0
Retrato de Claude Shannon — MIT Photo Service, dominio público
```

## svenska (`sv`)

```
Varför kan man inte komprimera allt?
```

```
Ta alla manus som någonsin skrivits för den här kanalen, nästan en och en halv miljon byte text, och kör dem genom gzip. Nästan två tredjedelar försvinner, och ingenting går förlorat. Komprimera nu resultatet igen, och det blir större. Nittioåtta byte större, varenda gång. Så varför kan vi inte bara fortsätta komprimera? Och skulle ett smartare program en dag kunna krympa vad du än ger det?

Videon går igenom de två knepen i ZIP och gzip: Jacob Zivs och Abraham Lempels hänvisningar bakåt till tidigare text, och David Huffmans kod från en uppsats som han nästan hade gett upp. Sedan en liten räknegåta med filer på tre bitar, en produkt från 1992 som påstods vara undantagen från informationsteorins lagar, varför JPEG spelar ett annat spel, Claude Shannons gissningslek och gränsen som ingen förlustfri kod kan komma under, Hutter Prize och dess halva miljon euro för att krympa Wikipedia, hur Dropbox sparade 46 petabyte på foton som redan låg lagrade, en stor språkmodell som används som kompressor, och det märkliga fallet med en miljon siffror i pi.

Källor: J. Ziv and A. Lempel, A Universal Algorithm for Sequential Data Compression, IEEE Transactions on Information Theory (1977); D. A. Huffman, A Method for the Construction of Minimum-Redundancy Codes, Proceedings of the IRE (1952); G. Stix, Profile: David A. Huffman, Scientific American (1991); P. Deutsch, RFC 1951 and RFC 1952 (1996); C. E. Shannon, A Mathematical Theory of Communication (1948); C. E. Shannon, Prediction and Entropy of Printed English, Bell System Technical Journal (1951); J.-l. Gailly, comp.compression FAQ (1999); D. R. Horn et al., The Design, Implementation, and Deployment of a System to Transparently Compress Hundreds of Petabytes of Image Files for a File-Storage Service, NSDI (2017); M. Hutter, Hutter Prize for Lossless Compression of Human Knowledge (prize.hutter1.net); M. Mahoney, Large Text Compression Benchmark; G. Delétang et al., Language Modeling Is Compression, ICLR (2024); A. N. Kolmogorov, Three Approaches to the Quantitative Definition of Information (1965); G. J. Chaitin, Information-Theoretic Limitations of Formal Systems (1974). Mätningarna med gzip och pi gjordes för den här videon.

Undertexterna är skrivna för den här videon, inte automatiskt genererade. Amerikansk engelska finns som ett andra ljudspår.

Hela texten, källor och översättningar: https://theresmoretoit-channel.github.io/sv/videos/why-cant-we-compress-everything/

KAPITEL
00:00 Alla manus på kanalen, komprimerade
00:24 Komprimera igen
00:46 Inuti den andra filen
01:17 Hänvisningar bakåt till upprepningar
01:44 Huffmans uppsats
02:38 ZIP och gzip
02:58 Skulle ett smartare program klara det?
04:16 Programvaran som lovade för mycket
04:39 Hur blir foton så små?
05:08 Finns det en nedre gräns?
05:45 Shannons gissningslek
06:28 Hutter Prize
07:14 Program som förutsäger
07:59 En språkmodell som kompressor
08:40 En miljon siffror i pi
09:24 Det kortaste programmet
10:11 Det gzip inte ser

BILDKÄLLOR
Robert Fano — 121a0012, CC BY 3.0
Marcus Hutter — Marcus Hutter, CC BY-SA 4.0
Andrey Kolmogorov — Konrad Jacobs, CC BY-SA 2.0 DE
Foto av kungsfiskare — Alexis LOURS, CC BY 2.0 (beskuret, omkomprimerat)
via Wikimedia Commons
Licenser: creativecommons.org/licenses/by/3.0, creativecommons.org/licenses/by-sa/4.0, creativecommons.org/licenses/by-sa/2.0/de, creativecommons.org/licenses/by/2.0
Porträtt av Claude Shannon — MIT Photo Service, allmän egendom
```
