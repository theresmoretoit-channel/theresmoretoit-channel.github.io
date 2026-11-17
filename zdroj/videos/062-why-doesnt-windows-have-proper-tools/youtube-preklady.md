# Lokalizované názvy a popisy — 062

Čte `tools/lokalizace.py`, nahraje jedním voláním `videos.update(part="localizations")`
za 50 jednotek kvóty. Formát si vynucuje parser, viz `docs/zverejneni.md`.

## Co se NEPŘEKLÁDÁ

- **Časy kapitol** — zůstávají na vteřinu stejné, překládá se jen jejich text.
- **Tagy** — YouTube je per-jazyk nemá.
- **Letopočty** — `1988`, `1993`, `2006` zůstávají číslicemi.
- **Jména a názvy** — Windows, Microsoft, Redmond, Total Commander,
  Windows Commander, DOS Shell, Sysinternals, Process Explorer, NTFS,
  a program **Everything** (je to jméno, ne slovo).
- **IMAGE CREDITS** — nadpis, názvy snímků, jména autorů i kódy licencí
  zůstávají. Překládá se **jen slovo `Licences:`**.

## Registr češtiny: TYKÁNÍ

Zvoleno podle rodiny videí, ne podle metriky. Čtyři poslední videa
o Windows a Applu tykají (**046, 053, 055, 056**), vyká jen starší 033.
Hustota „you" v anglickém scénáři je **22,2 na tisíc slov**, tedy přesně
mezi mediány tykajících (30,4) a vykajících (13,6) videí — sama tedy
nerozhoduje a rozhodla konzistence uvnitř tématu.

## Věta o americké stopě

Znění se nepřekládá znovu — **zkopírováno z videa 059**, jak žádá
`docs/zverejneni.md`. Turecky je to `ses parçası`, ne `ses kanalı`.

## Pořadí sekcí

Bajtově podle **českého** názvu jazyka, protože Studio má české UI:
`fi, fr, id, it, de, pl, pt-BR, tr, uk, vi, cs, es, sv`.
Neodvozuj ho z jiného videa.

---

## suomi (`fi`)

```
Miksi Windowsissa ei ole kunnon työkaluja?
```

```
Microsoftilla on Windowsin lähdekoodi. He kirjoittivat rajapinnat. Heillä on ollut käytössään kolmekymmentä vuotta aikaa ja ohjelmistohistorian suurimpiin kuuluvia kehitystiimejä.

Ja ensimmäinen asia, jonka vaativa Windows-käyttäjä tekee uudella koneella, on asentaa jonkun toisen tiedostonhallinta, jonkun toisen haku, jonkun toisen pakkausohjelma. Ennen mitään oikeaa työtä hän rakentaa työkalupakin uudelleen.

Tiedostonhallinta on räikein esimerkki. Kaksipaneelinen on ollut olemassa vuodesta 1993 — eikä sitä yhdeksänä ensimmäisenä vuotenaan kutsuttu nimellä Total Commander. Sen nimi oli Windows Commander, kunnes saapui kirje asianajajilta, jotka edustivat tuon tavaramerkin omistajaa. Microsoft ei siis rakentanut tuota työkalua. Microsoft pakotti sen vaihtamaan nimeä.

Ja ennen kuin oletat, ettei kukaan Redmondissa keksinyt ideaa: DOS Shell, 1988. Vasen paneeli, oikea paneeli. Paketissa mukana. Microsoft poisti sen.

Yksi näistä työkaluista ansaitsee reilun käsittelyn ja saa sen. Everything löytää tiedostot hetkessä, koska se lukee päätiedostotaulun ja seuraa sitten muutoslokia, jota NTFS jo pitää. Windowsin haku on hitaampi, koska se tekee vaikeampaa työtä — se lukee dokumenttiesi sisällön ja se ottaa huomioon, kenellä on oikeus nähdä mikäkin tiedosto. Se ei ole epäonnistuminen. Se on vastaus eri kysymykseen.

Sitten tapaus, joka ratkaisee asian. Process Explorer tuli yhtiöstä nimeltä Sysinternals. Microsoft osti sen vuonna 2006 ja sai mukaan miehen, joka sen kirjoitti; hän on nykyään Microsoftin pilviliiketoiminnan teknologiajohtaja. Microsoft tarjoaa ohjelman ladattavaksi omilla sivuillaan. Eikä se vieläkään kuulu Windowsiin.

Vastaus ei siis voi olla, ettei Microsoft osannut. Mikä tarkoittaa, ettei todellinen kysymys ollut koskaan se, miksi he epäonnistuivat. Se on se, miksi he päättivät olla tekemättä niitä.

Selityksiä on kolme, ja vain yhdestä löytyy oikeudenkäyntiasiakirjoja.

Luvut
0:00 Heillä oli kaikki syyt rakentaa ne
0:52 Aloitetaan tiedostonhallinnasta
1:14 Ohjelma joka on tehnyt kaiken sen vuodesta 1993
2:08 Microsoft toimitti yhden, sitten poisti sen
2:34 Tiedoston löytäminen, ja missä Windows on oikeassa
3:31 Levytila, kopiointi, pakatut tiedostot, kuvakaappaukset
4:28 Ohjelma joka valvoi toisten ohjelmien asennusta
5:09 Ei vastaa
5:30 Microsoft osti yhtiön sen takaa
6:00 Ei siis voi olla etteivät osanneet
6:12 Yksi: Windows myytiin alustana
6:52 Kaksi: tähän liittyy oikeudenkäyntejä
7:48 Ei muinaishistoriaa
8:54 Kolme: mitä paketti maksaa
9:33 Kaksikymmentä ohjelmaa, kaksikymmentä päivittäjää
9:58 Miksi Windowsissa ei ollut sellaista komentoa
10:30 Se on siis vastaus
10:41 Paitsi että jokin on muuttunut
10:59 Miksi juuri nyt?
11:53 Outo lopputulos

Tekstitykset on kirjoitettu tätä videota varten, ei koneellisesti. Amerikanenglanninkielinen ääniraita on saatavilla toisena ääniraitana.

Musiikki tuotetaan tälle kanavalle proseduraalisesti.

IMAGE CREDITS
Mark Russinovich — MicrosoftPDC, CC BY 2.0
E. Barrett Prettyman Courthouse from NGA East Building — Toohool, CC BY-SA 4.0
European Commission headquarters, The Berlaymont Building, Brussels — Ank Kumar, CC BY-SA 4.0
via Wikimedia Commons
Lisenssit: creativecommons.org/licenses/by/2.0, /by-sa/4.0
```

## français (`fr`)

```
Pourquoi Windows n'a-t-il pas de vrais outils ?
```

```
Microsoft possède le code source de Windows. Ils ont écrit les API. Ils ont eu trente ans et certaines des plus grandes équipes d'ingénierie de l'histoire du logiciel.

Et la première chose qu'un utilisateur sérieux de Windows fait sur une machine neuve, c'est installer le gestionnaire de fichiers de quelqu'un d'autre, l'outil de recherche de quelqu'un d'autre, l'outil d'archivage de quelqu'un d'autre. Avant le moindre vrai travail, il reconstruit la boîte à outils.

Le gestionnaire de fichiers est le cas le plus net. Il en existe un à deux panneaux depuis 1993 — et pendant ses neuf premières années il ne s'appelait pas Total Commander. Il s'appelait Windows Commander, jusqu'à l'arrivée d'une lettre d'avocats représentant le propriétaire de cette marque. Microsoft n'a donc pas construit cet outil. Microsoft l'a obligé à changer de nom.

Et avant de supposer que personne à Redmond n'a jamais eu l'idée : DOS Shell, 1988. Panneau gauche, panneau droit. Dans la boîte. Microsoft l'a retiré.

Un de ces outils mérite qu'on l'examine sans préjugés, et c'est ce qu'on fait. Everything paraît instantané parce qu'il lit la table de fichiers principale, puis suit le journal des modifications que NTFS tient déjà. La recherche Windows est plus lente parce qu'elle fait un travail plus difficile — elle lit à l'intérieur de vos documents et elle tient compte des droits d'accès aux fichiers. Ce n'est pas un échec. C'est la réponse à une autre question.

Puis le cas qui tranche. Process Explorer venait d'une société appelée Sysinternals. Microsoft l'a rachetée en 2006 et a ainsi fait entrer dans ses équipes le développeur qui l'avait écrit ; il est aujourd'hui directeur technique de l'activité cloud de Microsoft. Microsoft héberge lui-même le téléchargement. Et il n'est toujours pas dans Windows.

La réponse ne peut donc pas être que Microsoft n'en était pas capable. Ce qui veut dire que la vraie question n'a jamais été pourquoi ils ont échoué. C'est pourquoi ils ont choisi de ne pas le faire.

Il y a trois explications, et une seule s'appuie sur des documents judiciaires.

Chapitres
0:00 Ils avaient toutes les raisons de les construire
0:52 Commençons par le gestionnaire de fichiers
1:14 Un programme qui fait tout cela depuis 1993
2:08 Microsoft en a livré un, puis l'a retiré
2:34 Trouver un fichier, et là où Windows a raison
3:31 Espace disque, copie, archives, captures d'écran
4:28 Un programme qui surveillait l'installation des autres
5:09 Ne répond pas
5:30 Microsoft a racheté l'entreprise derrière l'outil
6:00 Ce n'était donc pas un manque de capacité
6:12 Un : Windows a été vendu comme une plateforme
6:52 Deux : celle-ci a des dates d'audience
7:48 Pas de l'histoire ancienne
8:54 Trois : ce que coûte la boîte
9:33 Vingt programmes, vingt outils de mise à jour
9:58 Pourquoi Windows n'avait pas une telle commande
10:30 Voilà donc la réponse
10:41 Sauf que quelque chose a changé
10:59 Pourquoi maintenant ?
11:53 L'étrange résultat

Les sous-titres sont rédigés pour cette vidéo, ils ne sont pas générés automatiquement. Une piste audio en anglais américain est disponible comme deuxième piste audio.

La musique est générée de façon procédurale pour cette chaîne.

IMAGE CREDITS
Mark Russinovich — MicrosoftPDC, CC BY 2.0
E. Barrett Prettyman Courthouse from NGA East Building — Toohool, CC BY-SA 4.0
European Commission headquarters, The Berlaymont Building, Brussels — Ank Kumar, CC BY-SA 4.0
via Wikimedia Commons
Licences : creativecommons.org/licenses/by/2.0, /by-sa/4.0
```

## Bahasa Indonesia (`id`)

```
Kenapa Windows Tidak Punya Alat yang Layak?
```

```
Microsoft punya kode sumber Windows. Merekalah yang menulis API-nya. Mereka sudah punya waktu tiga puluh tahun dan beberapa tim pengembang terbesar dalam sejarah perangkat lunak.

Dan hal pertama yang dilakukan pengguna Windows yang serius di mesin baru adalah memasang pengelola berkas, aplikasi pencarian, dan alat arsip buatan pihak lain. Sebelum mengerjakan apa pun, dia membangun ulang kotak perkakasnya.

Contoh paling jelas adalah pengelola berkas. Yang berpanel dua sudah ada sejak 1993 — dan selama sembilan tahun pertamanya namanya bukan Total Commander. Namanya Windows Commander, sampai datang surat dari pengacara yang mewakili pemilik merek dagang itu. Jadi Microsoft tidak membangun alat itu. Microsoft memaksanya mengganti nama.

Dan sebelum kamu menyimpulkan tidak ada orang di Redmond yang pernah punya ide itu: DOS Shell, 1988. Panel kiri, panel kanan. Sudah disertakan dalam paketnya. Microsoft menghapusnya.

Salah satu alat ini layak dinilai secara adil, dan di sini kita melakukannya. Everything terasa sangat cepat karena membaca master file table lalu mengikuti jurnal perubahan yang sudah dipelihara NTFS. Pencarian Windows lebih lambat karena pekerjaannya lebih berat — ia membaca isi dokumenmu dan mematuhi aturan tentang siapa yang boleh mengakses berkas mana. Itu bukan kegagalan. Itu jawaban atas pertanyaan yang berbeda.

Lalu kasus yang menentukan. Process Explorer datang dari perusahaan bernama Sysinternals. Microsoft membelinya pada 2006 dan mendapatkan orang yang menulisnya; hari ini dia adalah chief technology officer bisnis cloud Microsoft. Microsoft sendiri yang menyediakan unduhannya. Dan alat itu tetap tidak ada di dalam Windows.

Jadi jawabannya tidak mungkin bahwa Microsoft tidak mampu. Artinya pertanyaan sebenarnya tidak pernah kenapa mereka gagal. Tapi kenapa mereka memilih untuk tidak melakukannya.

Ada tiga penjelasan, dan hanya satu yang punya catatan pengadilan.

Bab
0:00 Mereka punya segala alasan untuk membangunnya
0:52 Mulai dari pengelola berkas
1:14 Program yang sudah melakukan semuanya sejak 1993
2:08 Microsoft pernah menyertakannya, lalu menghapusnya
2:34 Mencari berkas, dan apa yang sudah dilakukan Windows dengan benar
3:31 Ruang diska, menyalin, arsip, tangkapan layar
4:28 Program yang mengawasi program lain memasang diri
5:09 Tidak merespons
5:30 Microsoft mengakuisisi perusahaan pembuatnya
6:00 Jadi tidak mungkin mereka tidak mampu
6:12 Satu: Windows dijual sebagai platform
6:52 Dua: yang ini punya tanggal sidang
7:48 Bukan sejarah kuno
8:54 Tiga: berapa harga kotak itu
9:33 Dua puluh program, dua puluh pembaru
9:58 Kenapa Windows tidak punya perintah seperti itu
10:30 Jadi itulah jawabannya
10:41 Hanya saja ada yang berubah
10:59 Kenapa sekarang?
11:53 Hasil yang aneh

Subtitel ditulis khusus untuk video ini, bukan dibuat otomatis. Trek audio bahasa Inggris Amerika tersedia sebagai trek audio kedua.

Musik dibuat secara prosedural untuk kanal ini.

IMAGE CREDITS
Mark Russinovich — MicrosoftPDC, CC BY 2.0
E. Barrett Prettyman Courthouse from NGA East Building — Toohool, CC BY-SA 4.0
European Commission headquarters, The Berlaymont Building, Brussels — Ank Kumar, CC BY-SA 4.0
via Wikimedia Commons
Lisensi: creativecommons.org/licenses/by/2.0, /by-sa/4.0
```

## italiano (`it`)

```
Perché Windows non ha strumenti decenti?
```

```
Microsoft ha il codice sorgente di Windows. Ha scritto le API. Ha avuto trent'anni e alcuni dei più grandi team di ingegneria della storia del software.

E la prima cosa che un utente Windows serio fa su una macchina nuova è installare il gestore di file di qualcun altro, uno strumento di ricerca di qualcun altro, l'archiviatore di qualcun altro. Prima di qualsiasi lavoro vero, ricostruisce la cassetta degli attrezzi.

Il gestore di file è il caso più netto. Ne esiste uno a due pannelli dal 1993 — e per i suoi primi nove anni non si chiamava Total Commander. Si chiamava Windows Commander, finché non arrivò una lettera di avvocati che rappresentavano il proprietario di quel marchio. Microsoft quindi non ha costruito quello strumento. Microsoft lo ha costretto a cambiare nome.

E prima di dare per scontato che a Redmond non ci avesse mai pensato nessuno: DOS Shell, 1988. Pannello sinistro, pannello destro. Incluso nel sistema. Microsoft lo ha rimosso.

Uno di questi strumenti merita una valutazione equa, e qui la riceve. Everything sembra istantaneo perché legge la master file table e poi segue il journal delle modifiche che NTFS tiene già. La ricerca di Windows è più lenta perché fa un lavoro più difficile — legge dentro i tuoi documenti e rispetta i permessi di accesso ai file. Quello non è un fallimento. È la risposta a una domanda diversa.

Poi il caso che chiude la questione. Process Explorer veniva da un'azienda chiamata Sysinternals. Microsoft l'ha comprata nel 2006 e si è presa l'uomo che lo aveva scritto; oggi è chief technology officer del settore cloud di Microsoft. Il programma si scarica direttamente dal sito di Microsoft. E quello strumento non è ancora dentro Windows.

Quindi la risposta non può essere che Microsoft non ne fosse capace. Il che significa che la vera domanda non è mai stata perché hanno fallito. È perché hanno scelto di non farlo.

Ci sono tre spiegazioni, e solo una ha atti giudiziari.

Capitoli
0:00 Avevano ogni motivo per costruirli
0:52 Partiamo dal gestore di file
1:14 Un programma che fa tutto questo dal 1993
2:08 Microsoft ne aveva incluso uno, poi lo ha rimosso
2:34 Trovare un file, e dove Windows ha ragione
3:31 Spazio su disco, copie, archivi, screenshot
4:28 Un programma che sorvegliava l'installazione di altri
5:09 Non risponde
5:30 Microsoft ha comprato l'azienda che c'era dietro
6:00 Non può quindi essere che non fossero capaci
6:12 Uno: Windows è stato venduto come piattaforma
6:52 Due: per questa ci sono state udienze in tribunale
7:48 Non è storia antica
8:54 Tre: quanto costa la scatola
9:33 Venti programmi, venti aggiornatori
9:58 Perché Windows non aveva un comando del genere
10:30 Ecco quindi la risposta
10:41 Solo che qualcosa è cambiato
10:59 Perché proprio adesso?
11:53 Lo strano risultato

I sottotitoli sono scritti per questo video, non generati automaticamente. È disponibile una traccia audio in inglese americano come seconda traccia audio.

La musica è generata in modo procedurale per questo canale.

IMAGE CREDITS
Mark Russinovich — MicrosoftPDC, CC BY 2.0
E. Barrett Prettyman Courthouse from NGA East Building — Toohool, CC BY-SA 4.0
European Commission headquarters, The Berlaymont Building, Brussels — Ank Kumar, CC BY-SA 4.0
via Wikimedia Commons
Licenze: creativecommons.org/licenses/by/2.0, /by-sa/4.0
```

## Deutsch (`de`)

```
Warum hat Windows keine ordentlichen Werkzeuge?
```

```
Microsoft hat den Quellcode von Windows. Sie haben die APIs geschrieben. Sie hatten dreißig Jahre und einige der größten Entwicklungsteams der Softwaregeschichte.

Und das Erste, was ein ernsthafter Windows-Nutzer auf einem neuen Rechner tut, ist den Dateimanager von jemand anderem zu installieren, die Suche von jemand anderem, das Archivprogramm von jemand anderem. Vor jeder echten Arbeit baut er den Werkzeugkasten neu auf.

Am deutlichsten zeigt sich das beim Dateimanager. Einen mit zwei Fenstern gibt es seit 1993 — und in seinen ersten neun Jahren hieß er nicht Total Commander. Er hieß Windows Commander, bis ein Brief von Anwälten kam, die den Inhaber dieser Marke vertraten. Microsoft hat dieses Werkzeug also nicht gebaut. Microsoft hat die Umbenennung erzwungen.

Und bevor du annimmst, in Redmond wäre nie jemand auf die Idee gekommen: DOS Shell, 1988. Linkes Fenster, rechtes Fenster. Mit dabei. Microsoft hat es entfernt.

Eines dieser Werkzeuge verdient es, fair beurteilt zu werden – und genau das tun wir. Everything reagiert praktisch verzögerungsfrei, weil es die Master File Table liest und dann dem Änderungsjournal folgt, das NTFS ohnehin führt. Die Windows-Suche ist langsamer, weil sie eine schwerere Aufgabe erledigt — sie durchsucht auch den Inhalt deiner Dokumente und sie beachtet, wer welche Datei sehen darf. Das ist kein Versagen. Das ist die Antwort auf eine andere Frage.

Dann das entscheidende Beispiel. Process Explorer kam von einer Firma namens Sysinternals. Microsoft hat sie 2006 gekauft und den Mann bekommen, der ihn geschrieben hat; er ist heute Chief Technology Officer des Cloud-Geschäfts von Microsoft. Microsoft hostet den Download selbst. Und er ist immer noch nicht in Windows.

Die Antwort kann also nicht sein, dass Microsoft es nicht konnte. Das heißt, die eigentliche Frage war nie, warum sie gescheitert sind. Sie lautet, warum sie sich dagegen entschieden haben.

Es gibt drei Erklärungen, und nur eine hat Gerichtsakten.

Kapitel
0:00 Sie hatten jeden Grund, sie zu bauen
0:52 Fangen wir beim Dateimanager an
1:14 Ein Programm, das all das seit 1993 kann
2:08 Microsoft lieferte einen und entfernte ihn wieder
2:34 Eine Datei finden, und wo Windows recht hat
3:31 Speicherplatz, Kopieren, Archive, Bildschirmfotos
4:28 Ein Programm, das andere beim Installieren beobachtete
5:09 Keine Rückmeldung
5:30 Microsoft kaufte die Firma dahinter
6:00 Es kann also nicht sein, dass sie es nicht konnten
6:12 Eins: Windows wurde als Plattform verkauft
6:52 Zwei: Hier kam es zu Gerichtsverfahren
7:48 Keine ferne Vergangenheit
8:54 Drei: was die Schachtel kostet
9:33 Zwanzig Programme, zwanzig Updater
9:58 Warum Windows keinen solchen Befehl hatte
10:30 Das ist also die Antwort
10:41 Nur hat sich etwas geändert
10:59 Warum ausgerechnet jetzt?
11:53 Das seltsame Ergebnis

Die Untertitel wurden für dieses Video geschrieben, nicht automatisch erzeugt. Eine amerikanisch-englische Tonspur ist als zweite Tonspur verfügbar.

Die Musik wird für diesen Kanal prozedural erzeugt.

IMAGE CREDITS
Mark Russinovich — MicrosoftPDC, CC BY 2.0
E. Barrett Prettyman Courthouse from NGA East Building — Toohool, CC BY-SA 4.0
European Commission headquarters, The Berlaymont Building, Brussels — Ank Kumar, CC BY-SA 4.0
via Wikimedia Commons
Lizenzen: creativecommons.org/licenses/by/2.0, /by-sa/4.0
```

## polski (`pl`)

```
Dlaczego Windows nie ma porządnych narzędzi?
```

```
Microsoft ma kod źródłowy Windowsa. To oni napisali API. Mieli trzydzieści lat i jedne z największych zespołów inżynierskich w historii oprogramowania.

A pierwsze, co poważny użytkownik Windowsa robi na nowej maszynie, to instaluje cudzy menedżer plików, cudzą wyszukiwarkę, cudzy program do archiwów. Zanim weźmie się za jakąkolwiek prawdziwą pracę, odbudowuje skrzynkę z narzędziami.

Najdobitniejszym przykładem jest menedżer plików. Dwupanelowy istnieje od 1993 roku — i przez pierwsze dziewięć lat nie nazywał się Total Commander. Nazywał się Windows Commander, dopóki nie przyszedł list od prawników reprezentujących właściciela tego znaku towarowego. Microsoft więc tego narzędzia nie zbudował. Microsoft zmusił je do zmiany nazwy.

I zanim założysz, że w Redmond nikt nigdy nie wpadł na ten pomysł: DOS Shell, 1988. Lewy panel, prawy panel. W pudełku. Microsoft go usunął.

Jedno z tych narzędzi zasługuje na sprawiedliwą ocenę — i taką tu otrzymuje. Everything działa natychmiast, bo czyta główną tablicę plików, a potem śledzi dziennik zmian, który NTFS i tak prowadzi. Wyszukiwanie Windowsa jest wolniejsze, bo wykonuje trudniejszą pracę — przeszukuje treść twoich dokumentów i uwzględnia uprawnienia dostępu do poszczególnych plików. To nie jest porażka. To odpowiedź na inne pytanie.

Potem przypadek, który rozstrzyga. Process Explorer pochodził z firmy Sysinternals. Microsoft kupił ją w 2006 roku i dostał człowieka, który go napisał; dziś jest dyrektorem technicznym chmurowego biznesu Microsoftu. Microsoft sam udostępnia ten program do pobrania. A narzędzia wciąż nie ma w Windowsie.

Odpowiedź nie może więc brzmieć, że Microsoft nie potrafił. Czyli prawdziwe pytanie nigdy nie brzmiało, dlaczego im się nie udało. Brzmi: dlaczego postanowili tego nie robić.

Są trzy wyjaśnienia, a tylko jedno ma akta sądowe.

Rozdziały
0:00 Mieli wszelkie powody, żeby je zbudować
0:52 Zacznijmy od menedżera plików
1:14 Program, który robi to wszystko od 1993 roku
2:08 Microsoft dołączył taki menedżer, a potem go usunął
2:34 Znaleźć plik, i w czym Windows ma rację
3:31 Miejsce na dysku, kopiowanie, archiwa, zrzuty ekranu
4:28 Program, który monitorował instalację innych programów
5:09 Nie odpowiada
5:30 Microsoft kupił firmę, która za nim stała
6:00 Nie może więc być tak, że nie potrafili
6:12 Raz: Windows sprzedawano jako platformę
6:52 Dwa: za tym stoją konkretne rozprawy sądowe
7:48 To nie zamierzchła historia
8:54 Trzy: ile kosztuje pudełko
9:33 Dwadzieścia programów, dwadzieścia aktualizatorów
9:58 Dlaczego Windows nie miał takiej komendy
10:30 To jest więc odpowiedź
10:41 Tyle że coś się zmieniło
10:59 Dlaczego akurat teraz?
11:53 Dziwny rezultat

Napisy zostały napisane do tego filmu, nie wygenerowane automatycznie. Dostępna jest amerykańska angielska ścieżka dźwiękowa jako druga ścieżka.

Muzyka jest generowana proceduralnie dla tego kanału.

IMAGE CREDITS
Mark Russinovich — MicrosoftPDC, CC BY 2.0
E. Barrett Prettyman Courthouse from NGA East Building — Toohool, CC BY-SA 4.0
European Commission headquarters, The Berlaymont Building, Brussels — Ank Kumar, CC BY-SA 4.0
via Wikimedia Commons
Licencje: creativecommons.org/licenses/by/2.0, /by-sa/4.0
```

## português (Brasil) (`pt-BR`)

```
Por que o Windows não tem ferramentas de verdade?
```

```
A Microsoft tem o código-fonte do Windows. Foram eles que escreveram as APIs. Tiveram trinta anos e algumas das maiores equipes de engenharia da história do software.

E a primeira coisa que um usuário sério de Windows faz numa máquina nova é instalar o gerenciador de arquivos de outra pessoa, a busca de outra pessoa, o compactador de outra pessoa. Antes de qualquer trabalho de verdade, ele reconstrói a caixa de ferramentas.

O gerenciador de arquivos é o caso mais nítido. Existe um de dois painéis desde 1993 — e nos seus primeiros nove anos ele não se chamava Total Commander. Chamava-se Windows Commander, até chegar uma carta de advogados representando o dono daquela marca. Ou seja, a Microsoft não construiu essa ferramenta. A Microsoft obrigou a ferramenta a mudar de nome.

E antes de você supor que ninguém em Redmond teve a ideia: DOS Shell, 1988. Painel esquerdo, painel direito. Já vinha incluído no sistema. A Microsoft removeu.

Uma dessas ferramentas merece uma avaliação justa — e é isso que vamos fazer. O Everything parece instantâneo porque lê a tabela mestra de arquivos e depois acompanha o diário de mudanças que o NTFS já mantém. A busca do Windows é mais lenta porque faz um trabalho mais difícil — ela lê o conteúdo dos seus documentos e respeita quem pode ver qual arquivo. Isso não é um fracasso. É a resposta a uma pergunta diferente.

Agora vem o caso que encerra a discussão. O Process Explorer veio de uma empresa chamada Sysinternals. A Microsoft comprou a empresa em 2006 e levou junto o homem que o escreveu; hoje ele é diretor de tecnologia do negócio de nuvem da Microsoft. A própria Microsoft hospeda o download. E ele continua fora do Windows.

Então a resposta não pode ser que a Microsoft não conseguia. O que significa que a pergunta de verdade nunca foi por que eles falharam. É por que eles escolheram não fazer.

Há três explicações, e só uma tem registros judiciais.

Capítulos
0:00 Tinham todos os motivos para construí-las
0:52 Comecemos pelo gerenciador de arquivos
1:14 Um programa que faz tudo isso desde 1993
2:08 A Microsoft entregou um e depois removeu
2:34 Achar um arquivo, e onde o Windows tem razão
3:31 Espaço em disco, cópia, compactação, capturas de tela
4:28 Um programa que vigiava a instalação dos outros
5:09 Não está respondendo
5:30 A Microsoft comprou a empresa por trás dele
6:00 Não pode ser que não conseguissem
6:12 Um: o Windows foi vendido como plataforma
6:52 Dois: esta tem datas de audiência
7:48 Não é história antiga
8:54 Três: quanto custa a caixa
9:33 Vinte programas, vinte atualizadores
9:58 Por que o Windows não tinha um comando desses
10:30 Essa é, portanto, a resposta
10:41 Só que alguma coisa mudou
10:59 Por que agora?
11:53 O resultado estranho

As legendas foram escritas para este vídeo, não geradas automaticamente. Há uma faixa de áudio em inglês americano disponível como segunda faixa de áudio.

A música é gerada proceduralmente para este canal.

IMAGE CREDITS
Mark Russinovich — MicrosoftPDC, CC BY 2.0
E. Barrett Prettyman Courthouse from NGA East Building — Toohool, CC BY-SA 4.0
European Commission headquarters, The Berlaymont Building, Brussels — Ank Kumar, CC BY-SA 4.0
via Wikimedia Commons
Licenças: creativecommons.org/licenses/by/2.0, /by-sa/4.0
```

## Türkçe (`tr`)

```
Windows'ta neden düzgün araçlar yok?
```

```
Microsoft'un elinde Windows'un kaynak kodu var. API'leri onlar yazdı. Bunun için otuz yıl boyunca zamanları ve yazılım tarihinin en büyük mühendislik ekiplerinden bazıları vardı.

Ve ciddi bir Windows kullanıcısının yeni bir makinede yaptığı ilk şey, başkasının dosya yöneticisini, başkasının arama aracını, başkasının arşiv aracını kurmaktır. Asıl işe başlamadan önce alet çantasını yeniden kurar.

Dosya yöneticisi en çarpıcı örnek. Çift panelli olanı 1993'ten beri var — ve ilk dokuz yılında adı Total Commander değildi. Adı Windows Commander'dı, ta ki o markanın sahibini temsil eden avukatlardan bir mektup gelene kadar. Yani Microsoft o aracı yapmadı. Microsoft ona adını değiştirtti.

Ve Redmond'da kimsenin bu fikri bulmadığını varsaymadan önce: DOS Shell, 1988. Sol panel, sağ panel. Kutunun içinde. Microsoft onu kaldırdı.

Bu araçlardan birine hakkını vermek gerekiyor; burada da bunu yapıyoruz. Everything'de sonuçlar anında geliyor gibi, çünkü ana dosya tablosunu okuyor ve sonra NTFS'in zaten tuttuğu değişiklik günlüğünü takip ediyor. Windows Arama daha yavaş, çünkü daha zor bir iş yapıyor — belgelerinin içini okuyor ve dosyalara erişim izinlerini dikkate alıyor. Bu bir başarısızlık değil. Bu, başka bir sorunun cevabı.

Sonra meseleyi bitiren örnek. Process Explorer, Sysinternals adlı bir şirketten geldi. Microsoft şirketi 2006'da satın aldı ve onu yazan adamı da aldı; bugün Microsoft'un bulut biriminin teknolojiden sorumlu başkanı. İndirmeyi Microsoft'un kendisi barındırıyor. Ve o araç hâlâ Windows'un içinde değil.

Yani cevap, Microsoft'un yapamadığı olamaz. Bu da demek oluyor ki asıl soru hiçbir zaman neden başarısız oldukları değildi. Asıl soru, neden yapmamayı seçtikleri.

Üç açıklama var ve yalnızca birinin mahkeme kayıtları var.

Bölümler
0:00 Bu araçları geliştirmek için pek çok nedenleri vardı
0:52 Dosya yöneticisiyle başlayalım
1:14 1993'ten beri bunların hepsini yapan bir program
2:08 Microsoft böyle bir aracı sisteme dahil etti, sonra kaldırdı
2:34 Dosya bulmak ve Windows'un haklı olduğu yer
3:31 Disk alanı, kopyalama, arşivler, ekran görüntüleri
4:28 Başka programların kurulumunu izleyen bir program
5:09 Yanıt vermiyor
5:30 Microsoft arkasındaki şirketi satın aldı
6:00 Yani sebep, bunu yapamamaları değil
6:12 Bir: Windows bir platform olarak satıldı
6:52 İki: bunun duruşma tarihleri var
7:48 O kadar da eski değil
8:54 Üç: kutunun bedeli
9:33 Yirmi program, yirmi güncelleyici
9:58 Windows'ta neden öyle bir komut yoktu
10:30 Cevap işte bu
10:41 Ama bir şey değişti
10:59 Peki neden şimdi?
11:53 Tuhaf sonuç

Altyazılar bu video için yazıldı, otomatik olarak oluşturulmadı. İkinci ses parçası olarak Amerikan İngilizcesi ses parçası mevcuttur.

Müzik bu kanal için yordamsal olarak üretilmektedir.

IMAGE CREDITS
Mark Russinovich — MicrosoftPDC, CC BY 2.0
E. Barrett Prettyman Courthouse from NGA East Building — Toohool, CC BY-SA 4.0
European Commission headquarters, The Berlaymont Building, Brussels — Ank Kumar, CC BY-SA 4.0
via Wikimedia Commons
Lisanslar: creativecommons.org/licenses/by/2.0, /by-sa/4.0
```

## українська (`uk`)

```
Чому у Windows немає нормальних інструментів?
```

```
Microsoft має вихідний код Windows. Вони написали API. У них було тридцять років і одні з найбільших інженерних команд в історії програмного забезпечення.

А перше, що серйозний користувач Windows робить на новій машині, — встановлює чужий файловий менеджер, чужий пошук, чужий архіватор. Перш ніж узятися за будь-яку справжню роботу, він заново збирає собі набір інструментів.

Файловий менеджер — найяскравіший приклад. Двопанельний існує з 1993 року — і перші дев'ять років він називався не Total Commander. Він називався Windows Commander, доки не прийшов лист від юристів, які представляли власника цієї торгової марки. Тобто Microsoft той інструмент не створила. Microsoft змусила його змінити назву.

І перш ніж припустити, що в Редмонді ніхто не додумався: DOS Shell, 1988. Ліва панель, права панель. У комплекті з системою. Microsoft його прибрала.

Один із цих інструментів варто оцінити справедливо. Саме це й зробимо. Everything, здається, знаходить усе миттєво, бо читає головну таблицю файлів, а потім стежить за журналом змін, який NTFS і так веде. Пошук Windows повільніший, бо робить складнішу роботу — він читає вміст твоїх документів і зважає на те, кому який файл дозволено бачити. Це не провал. Це відповідь на інше питання.

Далі випадок, який усе вирішує. Process Explorer походив із компанії Sysinternals. Microsoft купила її у 2006 році й дістала людину, яка його написала; сьогодні він технічний директор хмарного бізнесу Microsoft. Програму можна завантажити із сайту самої Microsoft. І в Windows його досі немає.

Тож відповідь не може бути в тому, що Microsoft не могла цього зробити. А отже, справжнє питання ніколи не було в тому, чому вони не впоралися. Питання в тому, чому вони вирішили цього не робити.

Пояснень три, і лише одне з них підтверджують матеріали судових справ.

Розділи
0:00 Вони мали всі підстави їх зробити
0:52 Почнімо з файлового менеджера
1:14 Програма, яка все це робить із 1993 року
2:08 Microsoft випустила один, потім прибрала
2:34 Знайти файл, і в чому Windows має рацію
3:31 Місце на диску, копіювання, архіви, знімки екрана
4:28 Програма, що стежила за встановленням інших
5:09 Не відповідає
5:30 Microsoft купила компанію, що стояла за ним
6:00 Отже, річ не в тому, що вони не могли
6:12 Перше: Windows продавали як платформу
6:52 Друге: тут є конкретні дати судових засідань
7:48 Це не давня історія
8:54 Третє: скільки коштує коробка
9:33 Двадцять програм, двадцять оновлювачів
9:58 Чому у Windows не було такої команди
10:30 Ось і відповідь
10:41 Тільки дещо змінилося
10:59 Чому саме зараз?
11:53 Дивний результат

Субтитри написані для цього відео, а не згенеровані автоматично. Доступна аудіодоріжка американською англійською як друга звукова доріжка.

Музика генерується для цього каналу процедурно.

IMAGE CREDITS
Mark Russinovich — MicrosoftPDC, CC BY 2.0
E. Barrett Prettyman Courthouse from NGA East Building — Toohool, CC BY-SA 4.0
European Commission headquarters, The Berlaymont Building, Brussels — Ank Kumar, CC BY-SA 4.0
via Wikimedia Commons
Ліцензії: creativecommons.org/licenses/by/2.0, /by-sa/4.0
```

## Tiếng Việt (`vi`)

```
Vì sao Windows không có công cụ tử tế?
```

```
Microsoft có mã nguồn của Windows. Chính họ viết các API. Họ đã có ba mươi năm và một số đội kỹ sư lớn nhất trong lịch sử phần mềm.

Và điều đầu tiên một người dùng Windows thành thạo làm trên máy mới là cài trình quản lý tệp của người khác, công cụ tìm kiếm của người khác, phần mềm nén của người khác. Trước khi bắt tay vào công việc, họ tự trang bị lại cả bộ công cụ.

Trình quản lý tệp là trường hợp rõ nhất. Loại hai khung đã có từ năm 1993 — và trong chín năm đầu nó không tên là Total Commander. Nó tên là Windows Commander, cho đến khi một lá thư đến từ các luật sư đại diện cho chủ sở hữu nhãn hiệu đó. Vậy là Microsoft không phát triển công cụ ấy. Microsoft bắt nó đổi tên.

Và trước khi bạn cho rằng chẳng ai ở Redmond từng nghĩ ra: DOS Shell, 1988. Khung trái, khung phải. Được tích hợp sẵn. Microsoft đã gỡ nó đi.

Một trong các công cụ này cần được đánh giá công bằng, và video này sẽ làm điều đó. Everything cho cảm giác tức thì vì nó đọc bảng tệp chính rồi theo dõi nhật ký thay đổi mà NTFS vốn đã ghi. Tìm kiếm của Windows chậm hơn vì nó làm việc khó hơn — nó đọc bên trong tài liệu của bạn và nó tuân thủ quyền truy cập của từng người dùng. Đó không phải thất bại. Đó là câu trả lời cho một câu hỏi khác.

Rồi đến trường hợp quyết định tất cả. Process Explorer đến từ một công ty tên là Sysinternals. Microsoft mua lại vào năm 2006 và có luôn người đã viết nó; hôm nay ông là giám đốc công nghệ mảng đám mây của Microsoft. Chính Microsoft lưu trữ bản tải về. Và nó vẫn không nằm trong Windows.

Vậy câu trả lời không thể là Microsoft không làm được. Nghĩa là câu hỏi thật sự chưa bao giờ là vì sao họ thất bại. Mà là vì sao họ chọn không làm.

Có ba lời giải thích, và chỉ một trong số đó có hồ sơ tòa án.

Các chương
0:00 Họ có mọi lý do để phát triển những công cụ này
0:52 Bắt đầu từ trình quản lý tệp
1:14 Một chương trình làm tất cả từ năm 1993
2:08 Microsoft từng cung cấp một công cụ như vậy, rồi loại bỏ
2:34 Tìm tệp: Windows làm đúng ở điểm nào
3:31 Dung lượng đĩa, sao chép, nén, chụp màn hình
4:28 Chương trình theo dõi chương trình khác cài đặt
5:09 Không phản hồi
5:30 Microsoft mua lại công ty đứng sau nó
6:00 Vậy không thể là họ không làm được
6:12 Một: Windows được bán như một nền tảng
6:52 Hai: cái này có ngày ra tòa
7:48 Không phải chuyện xa xưa
8:54 Ba: cái hộp tốn bao nhiêu
9:33 Hai mươi chương trình, hai mươi bộ cập nhật
9:58 Vì sao Windows không có câu lệnh như vậy
10:30 Vậy đó là câu trả lời
10:41 Chỉ có điều đã có thứ thay đổi
10:59 Vì sao lại là bây giờ?
11:53 Kết quả kỳ lạ

Phụ đề được viết riêng cho video này, không phải tạo tự động. Có bản âm thanh tiếng Anh Mỹ dưới dạng bản âm thanh thứ hai.

Nhạc được tạo theo thuật toán riêng cho kênh này.

IMAGE CREDITS
Mark Russinovich — MicrosoftPDC, CC BY 2.0
E. Barrett Prettyman Courthouse from NGA East Building — Toohool, CC BY-SA 4.0
European Commission headquarters, The Berlaymont Building, Brussels — Ank Kumar, CC BY-SA 4.0
via Wikimedia Commons
Giấy phép: creativecommons.org/licenses/by/2.0, /by-sa/4.0
```

## čeština (`cs`)

```
Proč Windows nemá pořádné nástroje?
```

```
Microsoft má zdrojový kód Windows. Napsal jeho API. Měl třicet let a jedny z největších inženýrských týmů v dějinách softwaru.

A první, co náročný uživatel Windows na novém stroji udělá, je nainstalovat cizí správce souborů, cizí vyhledávání, cizí archivační program. Dřív než se pustí do jakékoli skutečné práce, znovu si sestaví vlastní sadu nástrojů.

Nejvýraznějším příkladem je správce souborů. Dvoupanelový existuje od roku 1993 — a prvních devět let se nejmenoval Total Commander. Jmenoval se Windows Commander, dokud nepřišel dopis od právníků zastupujících majitele té ochranné známky. Microsoft tedy ten nástroj nevytvořil. Microsoft ho donutil změnit jméno.

A než usoudíš, že v Redmondu na to nikdo nepřišel: DOS Shell, 1988. Levý panel, pravý panel. Součást systému. Microsoft ho odstranil.

U jednoho z těch nástrojů je ale fér uznat, co dělá dobře. Everything reaguje okamžitě, protože čte hlavní tabulku souborů a pak sleduje žurnál změn, který NTFS stejně vede. Vyhledávání Windows je pomalejší, protože dělá těžší práci — prohledává obsah tvých dokumentů a respektuje, kdo který soubor smí vidět. To není selhání. To je odpověď na jinou otázku.

Pak případ, který to rozhodne. Process Explorer pocházel z firmy Sysinternals. Microsoft ji v roce 2006 koupil a získal s ní muže, který ho napsal; dnes je technickým ředitelem cloudového byznysu Microsoftu. Microsoft ho sám nabízí ke stažení. A pořád to není ve Windows.

Odpověď tedy nemůže znít, že Microsoft nemohl. Což znamená, že skutečná otázka nikdy nezněla, proč selhali. Zní: proč se rozhodli to neudělat.

Vysvětlení jsou tři a jen jedno z nich je doložené soudními spisy.

Kapitoly
0:00 Měli všechny důvody je vytvořit
0:52 Začněme správcem souborů
1:14 Program, který tohle všechno umí od roku 1993
2:08 Microsoft jeden dodal a pak ho odstranil
2:34 Hledání souborů a v čem má Windows pravdu
3:31 Místo na disku, kopírování, archivy, snímky obrazovky
4:28 Program, který hlídal instalaci jiných programů
5:09 Neodpovídá
5:30 Microsoft koupil firmu, která za ním stála
6:00 Nemůže tedy jít o to, že to neuměli
6:12 Za prvé: Windows se prodával jako platforma
6:52 Za druhé: tohle se řešilo u soudu
7:48 Není to dávná historie
8:54 Za třetí: co stojí krabice
9:33 Dvacet programů, dvacet aktualizátorů
9:58 Proč Windows takový příkaz neměl
10:30 To je tedy ta odpověď
10:41 Jenže něco se změnilo
10:59 Tak proč zrovna teď?
11:53 Podivný výsledek

Titulky jsou k tomuhle videu napsané, ne strojově vygenerované. K dispozici je americká anglická zvuková stopa jako druhá zvuková stopa.

Hudba se pro tenhle kanál generuje procedurálně.

IMAGE CREDITS
Mark Russinovich — MicrosoftPDC, CC BY 2.0
E. Barrett Prettyman Courthouse from NGA East Building — Toohool, CC BY-SA 4.0
European Commission headquarters, The Berlaymont Building, Brussels — Ank Kumar, CC BY-SA 4.0
via Wikimedia Commons
Licence: creativecommons.org/licenses/by/2.0, /by-sa/4.0
```

## español (`es`)

```
¿Por qué Windows no tiene herramientas decentes?
```

```
Microsoft tiene el código fuente de Windows. Ellos escribieron las API. Han tenido treinta años y algunos de los equipos de ingeniería más grandes de la historia del software.

Y lo primero que hace un usuario serio de Windows en una máquina nueva es instalar el gestor de archivos de otro, la búsqueda de otro, el compresor de otro. Antes de cualquier trabajo real, reconstruye la caja de herramientas.

El gestor de archivos es el caso más claro. Existe uno de dos paneles desde 1993 — y durante sus primeros nueve años no se llamaba Total Commander. Se llamaba Windows Commander, hasta que llegó una carta de abogados que representaban al dueño de esa marca. Así que Microsoft no construyó esa herramienta. Microsoft la obligó a cambiar de nombre.

Y antes de que supongas que en Redmond nunca se les ocurrió: DOS Shell, 1988. Panel izquierdo, panel derecho. Venía incluido. Microsoft lo quitó.

Una de estas herramientas merece una evaluación justa, y aquí se la damos. Everything parece instantáneo porque lee la tabla maestra de archivos y luego sigue el diario de cambios que NTFS ya mantiene. La búsqueda de Windows es más lenta porque hace un trabajo más difícil — lee dentro de tus documentos y respeta quién puede ver qué archivo. Eso no es un fracaso. Es la respuesta a otra pregunta.

Después, el caso que lo zanja. Process Explorer venía de una empresa llamada Sysinternals. Microsoft la compró en 2006 y se llevó al hombre que lo había escrito; hoy es director de tecnología del negocio de nube de Microsoft. La propia Microsoft aloja la descarga. Y sigue sin estar dentro de Windows.

Así que la respuesta no puede ser que Microsoft no pudiera. Lo que significa que la pregunta de verdad nunca fue por qué fracasaron. Es por qué eligieron no hacerlo.

Hay tres explicaciones, y solo una tiene registros judiciales.

Capítulos
0:00 Tenían todas las razones para construirlas
0:52 Empecemos por el gestor de archivos
1:14 Un programa que hace todo eso desde 1993
2:08 Microsoft lo incluía y luego lo quitó
2:34 Encontrar un archivo, y en qué acierta Windows
3:31 Espacio en disco, copiar, archivos comprimidos, capturas
4:28 Un programa que vigilaba la instalación de otros
5:09 No responde
5:30 Microsoft compró la empresa que había detrás
6:00 No puede ser que no pudieran
6:12 Uno: Windows se vendió como plataforma
6:52 Dos: esta sí llegó a los tribunales
7:48 No es historia antigua
8:54 Tres: lo que cuesta la caja
9:33 Veinte programas, veinte actualizadores
9:58 Por qué Windows no tenía un comando así
10:30 Esa es, pues, la respuesta
10:41 Salvo que algo ha cambiado
10:59 ¿Y por qué ahora?
11:53 El resultado extraño

Los subtítulos están escritos para este vídeo, no generados automáticamente. Hay una pista de audio en inglés americano disponible como segunda pista de audio.

La música se genera de forma procedural para este canal.

IMAGE CREDITS
Mark Russinovich — MicrosoftPDC, CC BY 2.0
E. Barrett Prettyman Courthouse from NGA East Building — Toohool, CC BY-SA 4.0
European Commission headquarters, The Berlaymont Building, Brussels — Ank Kumar, CC BY-SA 4.0
via Wikimedia Commons
Licencias: creativecommons.org/licenses/by/2.0, /by-sa/4.0
```

## svenska (`sv`)

```
Varför har Windows inga riktiga verktyg?
```

```
Microsoft har källkoden till Windows. De skrev API:erna. De har haft trettio år och några av de största utvecklingsteamen i mjukvaruhistorien.

Och det första en seriös Windows-användare gör på en ny maskin är att installera någon annans filhanterare, någon annans sökning, någon annans arkivprogram. Innan de kan börja jobba på riktigt bygger de om verktygslådan.

Filhanteraren är det tydligaste exemplet. En med två paneler har funnits sedan 1993 — och under sina första nio år hette den inte Total Commander. Den hette Windows Commander, tills det kom ett brev från advokater som företrädde ägaren till det varumärket. Microsoft byggde alltså inte det verktyget. Microsoft tvingade det att byta namn.

Och innan du antar att ingen i Redmond någonsin kom på idén: DOS Shell, 1988. Vänster panel, höger panel. Ingick från början. Microsoft tog bort den.

Ett av verktygen förtjänar att få komma till tals, och får det. Everything känns blixtsnabbt för att det läser huvudfiltabellen och sedan följer ändringsjournalen som NTFS redan för. Windows sökning är långsammare för att den gör ett svårare jobb — den läser inuti dina dokument och den tar hänsyn till vem som får se vilken fil. Det är inte ett misslyckande. Det är svaret på en annan fråga.

Sedan fallet som avgör saken. Process Explorer kom från ett företag som hette Sysinternals. Microsoft köpte det 2006 och fick med mannen som skrev det; i dag är han teknikchef för Microsofts molnaffär. Microsoft står själv för nedladdningen. Och det finns fortfarande inte i Windows.

Svaret kan alltså inte vara att Microsoft inte kunde. Vilket betyder att den riktiga frågan aldrig var varför de misslyckades. Den är varför de valde att låta bli.

Det finns tre förklaringar, och bara en av dem har domstolshandlingar.

Kapitel
0:00 De hade alla skäl att bygga dem
0:52 Vi börjar med filhanteraren
1:14 Ett program som gjort allt detta sedan 1993
2:08 Microsoft levererade en och tog sedan bort den
2:34 Att hitta en fil – och när Windows har rätt
3:31 Diskutrymme, kopiering, arkiv, skärmbilder
4:28 Ett program som bevakade andra programs installation
5:09 Svarar inte
5:30 Microsoft köpte företaget bakom det
6:00 Brist på förmåga kan alltså inte vara förklaringen
6:12 Ett: Windows såldes som en plattform
6:52 Två: den här har rättegångsdatum
7:48 Det här är inte bara historia
8:54 Tre: vad det kostar att inkludera dem
9:33 Tjugo program, tjugo uppdaterare
9:58 Varför Windows inte hade ett sådant kommando
10:30 Det är alltså svaret
10:41 Fast något har förändrats
10:59 Varför just nu?
11:53 Det märkliga resultatet

Undertexterna är skrivna för den här videon, inte automatgenererade. Ett amerikansk-engelskt ljudspår finns tillgängligt som andra ljudspår.

Musiken genereras proceduralt för den här kanalen.

IMAGE CREDITS
Mark Russinovich — MicrosoftPDC, CC BY 2.0
E. Barrett Prettyman Courthouse from NGA East Building — Toohool, CC BY-SA 4.0
European Commission headquarters, The Berlaymont Building, Brussels — Ank Kumar, CC BY-SA 4.0
via Wikimedia Commons
Licenser: creativecommons.org/licenses/by/2.0, /by-sa/4.0
```
