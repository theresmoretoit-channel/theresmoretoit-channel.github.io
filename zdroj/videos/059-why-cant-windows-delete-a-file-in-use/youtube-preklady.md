# Lokalizované názvy a popisy — 059

Čte `tools/lokalizace.py`, nahraje jedním voláním `videos.update(part="localizations")`
za 50 jednotek kvóty. Formát si vynucuje parser, viz `docs/zverejneni.md`.

## Co se NEPŘEKLÁDÁ

- **Časy kapitol** — zůstávají na vteřinu stejné, překládá se jen jejich text.
- **Tagy** — YouTube je per-jazyk nemá.
- **`FILE_SHARE_DELETE`, `NTFS`, `POSIX`, `movie.mp4`** — názvy z dokumentace
  a příkaz zůstávají beze změny ve všech jazycích.
- **Roky 2005 a 2009** — číslice zůstávají číslicemi.
- **IMAGE CREDITS** tu nejsou vůbec: video nemá jedinou archivní scénu,
  takže není co atribuovat.

## Věta o americké stopě

Znění se nepřekládá znovu — **zkopírováno z videa 058**, jak žádá
`docs/zverejneni.md`. Turecky je to `ses parçası`, ne `ses kanalı`
(doloženo oficiální tureckou nápovědou YouTube; Codex si u toho mezi
dvěma běhy protiřečil).

## Pořadí sekcí

Bajtově podle **českého** názvu jazyka, protože Studio má české UI:
`fi, fr, id, it, de, pl, pt-BR, tr, uk, vi, cs, es, sv`.
Neodvozuj ho z jiného videa.

---

## suomi (`fi`)

```
Miksi Windows ei voi poistaa käytössä olevaa tiedostoa?
```

```
Yrität poistaa tiedoston. Windows sanoo, että se on auki toisessa ohjelmassa. Muttei kerro, missä.

Tuo viesti on näkyvä pää paljon oudommasta kysymyksestä: mitä tiedoston avaaminen oikeastaan tarkoittaa? Sillä toisella tietokoneella sama tiedosto, täsmälleen samalla tavalla auki, poistuu ilman yhtään valitusta.

Ensin hyödyllinen osa. Windows on tiennyt vuodesta 2009 asti, mikä ohjelma se on, ja se kertoo sen sinulle — Resurssienvalvonta, Suoritin-välilehti, Liittyvät kahvat, kirjoita tiedoston nimi. Mitään ei tarvitse asentaa. Ihmiset latasivat silti erillisen työkalun, ja siihen oli syy.

Sitten mekanismi. Windowsissa tiedoston avaaminen tarkoittaa kahden asian täyttämistä, ja toinen niistä on sopimus kaikkien muiden kanssa: mitä he saavat tehdä sillä aikaa kun tämä on minulla auki? Microsoftin oma dokumentaatio lisää poistolipun alle yhden rivin — poisto-oikeus kattaa myös uudelleennimeämisen. Siksi virheen nimi ei ole "tiedosto varattu". Sen nimi on jakamisen rikkomus.

Linuxissa sama komento vain toimii, ja syy on oudompi kuin miltä kuulostaa. Tein viidensadan megatavun lokitiedoston, jätin yhden prosessin pitämään sitä auki ja poistin sen. Hakemiston listaus ei näytä mitään. Kansion kokoa mittaava työkalu sanoo nolla. Levyä mittaava työkalu sanoo, että viisisataa megatavua on yhä poissa.

Ja sitten käänne, jota en odottanut: Windows osaa täsmälleen saman asian. NTFS:llä se voi pyytää POSIX-tyylistä poistoa, ja Microsoft kuvaa lopputuloksen samoilla sanoilla kuin Unixin manuaali. Kumpikin järjestelmä osaa molemmat. Ero on oletusasetuksessa.

Tuo ero on osa syytä, miksi Windows ennen pyysi niin usein käynnistämään uudelleen — Microsoft sanoo sen sen työkalun dokumentaatiossa, joka rakennettiin sitä välttämään. Mutta se ei ole koko syy, eikä Linuxkaan ole ongelmasta vapaa.

Koko teksti, lähteet ja käännökset: https://theresmoretoit-channel.github.io/fi/videos/why-cant-windows-delete-a-file-in-use/

Luvut
0:00 Viesti jonka kaikki tuntevat
0:29 Mikä ohjelma?
1:02 Windows kertoo sen jo nyt
1:30 Mitä täytät kun avaat tiedoston
2:16 FILE_SHARE_DELETE
2:41 Jakamisen rikkomus
2:53 Linuxissa se vain toimii
3:16 Nimi ei ole tiedosto
3:48 Viisisataa megatavua jotka katoavat
4:34 Uudelleennimeäminen ja yksi rajoitus
5:36 Windows osaa saman asian
6:31 Käynnistä tietokone uudelleen
7:03 Uudelleenkäynnistysten hallinta
7:38 Mutta se ei ole koko syy
8:16 Mitä kumpikin valinta maksaa
9:11 Eli mitä tiedoston avaaminen tarkoittaa?

Tekstitykset on kirjoitettu tätä videota varten, ei koneellisesti. Amerikanenglanninkielinen ääniraita on saatavilla toisena ääniraitana.

Musiikki tuotetaan tälle kanavalle proseduraalisesti.
```

## français (`fr`)

```
Pourquoi Windows ne peut-il pas supprimer un fichier en cours d'utilisation ?
```

```
Vous essayez de supprimer un fichier. Windows dit qu'il est ouvert dans un autre programme. Mais il ne dit pas lequel.

Ce message est la partie visible d'une question bien plus étrange : que veut dire au juste ouvrir un fichier ? Car sur un autre ordinateur, le même fichier, ouvert exactement pareil, se supprime sans broncher.

D'abord le côté utile. Windows sait depuis 2009 de quel programme il s'agit, et il vous le dira — Moniteur de ressources, onglet Processeur, Handles associés, tapez le nom du fichier. Rien à installer. Les gens ont quand même continué à télécharger un outil à part, et ils avaient une raison.

Ensuite le mécanisme. Sous Windows, ouvrir un fichier veut dire remplir deux choses, et la seconde est un contrat passé avec tous les autres : que peuvent-ils faire pendant que je le tiens ouvert ? La documentation de Microsoft ajoute une ligne sous l'indicateur de suppression — le droit de supprimer couvre aussi le renommage. Voilà pourquoi l'erreur ne s'appelle pas « fichier occupé ». Elle s'appelle violation de partage.

Sous Linux, la même commande fonctionne, et la raison est plus étrange qu'il n'y paraît. J'ai fait un fichier journal de cinq cents mégaoctets, laissé un processus le tenir ouvert, et je l'ai supprimé. Le listage du répertoire n'affiche rien. L'outil qui mesure le dossier dit zéro. L'outil qui mesure le disque dit que cinq cents mégaoctets manquent toujours.

Et puis le retournement que je n'attendais pas : Windows sait faire exactement la même chose. Sur NTFS, il peut demander une suppression à la POSIX, et Microsoft décrit le résultat avec les mots qu'emploierait un manuel Unix. Les deux systèmes savent faire les deux. Ce qui diffère, c'est le défaut.

Cette différence explique en partie pourquoi Windows demandait si souvent de redémarrer — Microsoft le dit dans la documentation de l'outil conçu pour l'éviter. Mais ce n'est pas toute l'explication, et Linux n'est pas exempt du problème non plus.

Transcription complète, sources et traductions : https://theresmoretoit-channel.github.io/fr/videos/why-cant-windows-delete-a-file-in-use/

Chapitres
0:00 Le message que tout le monde connaît
0:29 Quel programme ?
1:02 Windows vous le dit déjà
1:30 Ce que vous remplissez en ouvrant un fichier
2:16 FILE_SHARE_DELETE
2:41 Une violation de partage
2:53 Sous Linux, ça marche tout simplement
3:16 Un nom n'est pas le fichier
3:48 Cinq cents mégaoctets qui disparaissent
4:34 Le renommage, et une limite
5:36 Windows sait faire la même chose
6:31 Redémarrez votre ordinateur
7:03 Le Gestionnaire de redémarrage
7:38 Mais ce n'est pas toute la raison
8:16 Ce que chaque choix coûte
9:11 Alors, que veut dire ouvrir un fichier ?

Les sous-titres sont rédigés pour cette vidéo, ils ne sont pas générés automatiquement. Une piste audio en anglais américain est disponible comme deuxième piste audio.

La musique est générée de façon procédurale pour cette chaîne.
```

## Bahasa Indonesia (`id`)

```
Kenapa Windows Tidak Bisa Menghapus Berkas yang Sedang Dipakai?
```

```
Kamu mencoba menghapus sebuah berkas. Windows bilang berkas itu terbuka di program lain. Tapi tidak bilang program mana.

Pesan itu adalah ujung yang terlihat dari pertanyaan yang jauh lebih aneh: apa sebenarnya artinya membuka sebuah berkas? Sebab di komputer lain, berkas yang sama, dibuka dengan cara yang persis sama, terhapus tanpa keluhan sedikit pun.

Pertama bagian yang berguna. Windows sudah tahu program mana itu sejak 2009, dan ia mau memberitahumu — Monitor Sumber Daya, tab CPU, Associated Handles, ketik nama berkasnya. Tidak ada yang perlu dipasang. Orang tetap saja mengunduh alat terpisah, dan mereka punya alasan.

Lalu mekanismenya. Di Windows, membuka berkas berarti mengisi dua hal, dan yang kedua adalah kontrak dengan semua orang lain: apa yang boleh mereka lakukan selama berkas ini terbuka di tanganku? Dokumentasi Microsoft menambahkan satu baris di bawah tanda penghapusan — hak menghapus juga mencakup penggantian nama. Itu sebabnya kesalahannya tidak bernama "berkas sedang dipakai". Namanya pelanggaran berbagi.

Di Linux perintah yang sama langsung jalan, dan alasannya lebih aneh dari kedengarannya. Aku membuat berkas log lima ratus megabita, membiarkan satu proses membukanya, lalu menghapusnya. Daftar isi direktori tidak menampilkan apa pun. Alat pengukur folder bilang nol. Alat pengukur diska bilang lima ratus megabita masih hilang.

Lalu kejutan yang tidak kuduga: Windows bisa melakukan hal yang persis sama. Di NTFS ia bisa meminta penghapusan bergaya POSIX, dan Microsoft menjelaskan hasilnya dengan kata-kata yang sama seperti manual Unix. Kedua sistem bisa melakukan keduanya. Yang berbeda adalah setelan bawaannya.

Perbedaan itu sebagian menjelaskan kenapa dulu Windows begitu sering minta dimulai ulang — Microsoft mengatakannya sendiri di dokumentasi alat yang dibuat untuk menghindarinya. Tapi itu bukan seluruh alasannya, dan Linux pun tidak bebas dari masalah ini.

Transkrip lengkap, sumber, dan terjemahan: https://theresmoretoit-channel.github.io/id/videos/why-cant-windows-delete-a-file-in-use/

Bab
0:00 Pesan yang dikenal semua orang
0:29 Program yang mana?
1:02 Windows sudah memberitahumu
1:30 Apa yang kamu isi saat membuka berkas
2:16 FILE_SHARE_DELETE
2:41 Pelanggaran berbagi
2:53 Di Linux langsung jalan
3:16 Nama bukanlah berkas
3:48 Lima ratus megabita yang lenyap
4:34 Penggantian nama, dan satu batas
5:36 Windows bisa melakukan hal yang sama
6:31 Mulai ulang komputermu
7:03 Restart Manager
7:38 Tapi itu bukan seluruh alasannya
8:16 Berapa harga setiap pilihan
9:11 Jadi apa artinya membuka berkas?

Subtitel ditulis khusus untuk video ini, bukan dibuat otomatis. Trek audio bahasa Inggris Amerika tersedia sebagai trek audio kedua.

Musik dibuat secara prosedural untuk kanal ini.
```

## italiano (`it`)

```
Perché Windows non riesce a cancellare un file in uso?
```

```
Provi a cancellare un file. Windows dice che è aperto in un altro programma. Ma non dice quale.

Quel messaggio è il capo visibile di una domanda molto più strana: che cosa vuol dire davvero aprire un file? Perché su un altro computer lo stesso file, aperto esattamente allo stesso modo, si cancella senza una protesta.

Prima la parte utile. Windows sa dal 2009 di quale programma si tratta, e te lo dice — Monitoraggio risorse, scheda CPU, Handle associati, digita il nome del file. Niente da installare. La gente ha continuato lo stesso a scaricare uno strumento a parte, e aveva una ragione.

Poi il meccanismo. Su Windows, aprire un file vuol dire compilare due cose, e la seconda è un contratto con tutti gli altri: che cosa possono fare mentre io lo tengo aperto? La documentazione di Microsoft aggiunge una riga sotto il flag di cancellazione — il permesso di cancellare copre anche la rinomina. Ecco perché l'errore non si chiama "file occupato". Si chiama violazione di condivisione.

Su Linux lo stesso comando funziona e basta, e il motivo è più strano di quanto sembri. Ho creato un file di log da cinquecento megabyte, ho lasciato un processo a tenerlo aperto e l'ho cancellato. L'elenco della directory non mostra nulla. Lo strumento che misura la cartella dice zero. Quello che misura il disco dice che cinquecento megabyte mancano ancora.

E poi la svolta che non mi aspettavo: Windows sa fare esattamente la stessa cosa. Su NTFS può chiedere una cancellazione in stile POSIX, e Microsoft descrive il risultato con le parole che userebbe un manuale Unix. Entrambi i sistemi sanno fare entrambe le cose. A cambiare è l'impostazione predefinita.

Quella differenza spiega in parte perché Windows chiedeva così spesso di riavviare — lo dice Microsoft nella documentazione dello strumento costruito per evitarlo. Ma non è tutta la spiegazione, e nemmeno Linux è immune dal problema.

Trascrizione completa, fonti e traduzioni: https://theresmoretoit-channel.github.io/it/videos/why-cant-windows-delete-a-file-in-use/

Capitoli
0:00 Il messaggio che tutti conoscono
0:29 Quale programma?
1:02 Windows te lo dice già
1:30 Che cosa compili quando apri un file
2:16 FILE_SHARE_DELETE
2:41 Una violazione di condivisione
2:53 Su Linux funziona e basta
3:16 Un nome non è il file
3:48 Cinquecento megabyte che svaniscono
4:34 La rinomina, e un limite
5:36 Windows sa fare la stessa cosa
6:31 Riavvia il computer
7:03 Gestione riavvio
7:38 Ma non è tutta la ragione
8:16 Quanto costa ciascuna scelta
9:11 Allora che vuol dire aprire un file?

I sottotitoli sono scritti per questo video, non generati automaticamente. È disponibile una traccia audio in inglese americano come seconda traccia audio.

La musica è generata in modo procedurale per questo canale.
```

## Deutsch (`de`)

```
Warum kann Windows eine Datei in Benutzung nicht löschen?
```

```
Du willst eine Datei löschen. Windows sagt, sie sei in einem anderen Programm offen. Nur in welchem, sagt es nicht.

Diese Meldung ist das sichtbare Ende einer viel merkwürdigeren Frage: Was heißt es eigentlich, eine Datei zu öffnen? Denn auf einem anderen Rechner lässt sich dieselbe Datei, genau gleich geöffnet, ohne jeden Einwand löschen.

Zuerst das Nützliche. Windows weiß seit 2009, welches Programm es ist, und es sagt es dir auch — Ressourcenmonitor, Registerkarte CPU, Zugeordnete Handles, Dateinamen eintippen. Nichts zu installieren. Die Leute haben trotzdem weiter ein eigenes Werkzeug geladen, und sie hatten einen Grund.

Dann der Mechanismus. Unter Windows heißt eine Datei öffnen, zwei Dinge auszufüllen, und das zweite ist ein Vertrag mit allen anderen: Was dürfen die tun, solange ich sie offen habe? Microsofts eigene Dokumentation setzt unter das Löschflag eine Zeile — das Löschrecht umfasst auch das Umbenennen. Deshalb heißt der Fehler nicht „Datei in Benutzung". Er heißt Freigabeverletzung.

Unter Linux klappt derselbe Befehl einfach, und der Grund ist seltsamer, als er klingt. Ich habe eine Protokolldatei von fünfhundert Megabyte angelegt, einen Prozess sie offen halten lassen und sie gelöscht. Die Verzeichnisliste zeigt nichts. Das Werkzeug für die Ordnergröße meldet null. Das für die Platte meldet, dass fünfhundert Megabyte immer noch fehlen.

Und dann die Wendung, die ich nicht erwartet hatte: Windows kann genau dasselbe. Auf NTFS kann es ein Löschen im POSIX-Stil anfordern, und Microsoft beschreibt das Ergebnis mit denselben Worten wie ein Unix-Handbuch. Beide Systeme können beides. Was sich unterscheidet, ist die Vorgabe.

Dieser Unterschied ist ein Teil davon, warum Windows früher so oft um einen Neustart bat — Microsoft sagt das in der Dokumentation des Werkzeugs, das genau dafür gebaut wurde. Aber es ist nicht die ganze Erklärung, und Linux ist von dem Problem auch nicht frei.

Vollständiger Text, Quellen und Übersetzungen: https://theresmoretoit-channel.github.io/de/videos/why-cant-windows-delete-a-file-in-use/

Kapitel
0:00 Die Meldung, die jeder kennt
0:29 Welches Programm?
1:02 Windows sagt es dir längst
1:30 Was du beim Öffnen einer Datei ausfüllst
2:16 FILE_SHARE_DELETE
2:41 Eine Freigabeverletzung
2:53 Unter Linux klappt es einfach
3:16 Ein Name ist nicht die Datei
3:48 Fünfhundert Megabyte, die verschwinden
4:34 Umbenennen, und eine Grenze
5:36 Windows kann dasselbe
6:31 Starten Sie den Computer neu
7:03 Der Neustart-Manager
7:38 Aber das ist nicht der ganze Grund
8:16 Was jede Entscheidung kostet
9:11 Also, was heißt es, eine Datei zu öffnen?

Die Untertitel wurden für dieses Video geschrieben, nicht automatisch erzeugt. Eine amerikanisch-englische Tonspur ist als zweite Tonspur verfügbar.

Die Musik wird für diesen Kanal prozedural erzeugt.
```

## polski (`pl`)

```
Dlaczego Windows nie może usunąć pliku, który jest w użyciu?
```

```
Próbujesz usunąć plik. Windows mówi, że jest otwarty w innym programie. Ale nie mówi, w którym.

Ten komunikat to widoczny koniec o wiele dziwniejszego pytania: co właściwie znaczy otworzyć plik? Bo na innym komputerze ten sam plik, otwarty dokładnie tak samo, usuwa się bez słowa skargi.

Najpierw rzecz przydatna. Windows wie od 2009 roku, który to program, i powie ci to — Monitor zasobów, karta Procesor, Skojarzone dojścia, wpisz nazwę pliku. Nic do instalowania. Ludzie i tak dalej pobierali osobne narzędzie, i mieli powód.

Potem mechanizm. W Windows otworzyć plik znaczy wypełnić dwie rzeczy, a druga to umowa ze wszystkimi innymi: co im wolno, dopóki trzymam go otwartego? Dokumentacja Microsoftu dodaje pod flagą usuwania jedną linijkę — prawo do usuwania obejmuje też zmianę nazwy. Dlatego błąd nie nazywa się „plik zajęty". Nazywa się naruszenie współdzielenia.

W Linuksie to samo polecenie po prostu działa, a powód jest dziwniejszy, niż brzmi. Zrobiłem plik dziennika na pięćset megabajtów, zostawiłem jeden proces trzymający go otwartym i usunąłem go. Wypis katalogu nie pokazuje nic. Narzędzie mierzące folder mówi zero. Narzędzie mierzące dysk mówi, że pięciuset megabajtów wciąż brakuje.

A potem zwrot, którego się nie spodziewałem: Windows potrafi dokładnie to samo. Na NTFS może poprosić o usunięcie w stylu POSIX, a Microsoft opisuje wynik tymi samymi słowami, których użyłby podręcznik Uniksa. Oba systemy potrafią jedno i drugie. Różni je ustawienie domyślne.

Ta różnica jest częścią odpowiedzi, dlaczego Windows tak często prosił o restart — Microsoft mówi to w dokumentacji narzędzia zbudowanego po to, by go uniknąć. Ale to nie całe wyjaśnienie, a Linux też nie jest od tego problemu wolny.

Pełna transkrypcja, źródła i tłumaczenia: https://theresmoretoit-channel.github.io/pl/videos/why-cant-windows-delete-a-file-in-use/

Rozdziały
0:00 Komunikat, który zna każdy
0:29 Który program?
1:02 Windows już ci to mówi
1:30 Co wypełniasz, otwierając plik
2:16 FILE_SHARE_DELETE
2:41 Naruszenie współdzielenia
2:53 W Linuksie po prostu działa
3:16 Nazwa to nie plik
3:48 Pięćset megabajtów, które znikają
4:34 Zmiana nazwy i jedno ograniczenie
5:36 Windows potrafi to samo
6:31 Uruchom komputer ponownie
7:03 Menedżer ponownego uruchamiania
7:38 Ale to nie cały powód
8:16 Ile kosztuje każdy wybór
9:11 Więc co znaczy otworzyć plik?

Napisy zostały napisane do tego filmu, nie wygenerowane automatycznie. Dostępna jest amerykańska angielska ścieżka dźwiękowa jako druga ścieżka.

Muzyka jest generowana proceduralnie dla tego kanału.
```

## português (Brasil) (`pt-BR`)

```
Por que o Windows não consegue apagar um arquivo em uso?
```

```
Você tenta apagar um arquivo. O Windows diz que ele está aberto em outro programa. Mas não diz em qual.

Essa mensagem é a ponta visível de uma pergunta bem mais estranha: o que significa de fato abrir um arquivo? Porque em outro computador o mesmo arquivo, aberto exatamente do mesmo jeito, some sem uma única reclamação.

Primeiro a parte útil. O Windows sabe desde 2009 qual é o programa, e ele te conta — Monitor de Recursos, aba CPU, Identificadores Associados, digite o nome do arquivo. Nada para instalar. Mesmo assim as pessoas continuaram baixando uma ferramenta separada, e tinham um motivo.

Depois o mecanismo. No Windows, abrir um arquivo significa preencher duas coisas, e a segunda é um contrato com todo mundo: o que os outros podem fazer enquanto eu o mantenho aberto? A própria documentação da Microsoft acrescenta uma linha embaixo do sinalizador de exclusão — o direito de apagar abrange também a renomeação. É por isso que o erro não se chama "arquivo em uso". Chama-se violação de compartilhamento.

No Linux o mesmo comando simplesmente funciona, e o motivo é mais estranho do que parece. Fiz um arquivo de log de quinhentos megabytes, deixei um processo com ele aberto e apaguei. A listagem do diretório não mostra nada. A ferramenta que mede a pasta diz zero. A que mede o disco diz que quinhentos megabytes ainda estão faltando.

E então a virada que eu não esperava: o Windows faz exatamente a mesma coisa. No NTFS ele pode pedir uma exclusão no estilo POSIX, e a Microsoft descreve o resultado com as mesmas palavras que um manual Unix usaria. Os dois sistemas fazem as duas coisas. O que difere é o padrão.

Essa diferença é parte do motivo de o Windows pedir reinício com tanta frequência — a Microsoft diz isso na documentação da ferramenta feita para evitá-lo. Mas não é a explicação inteira, e o Linux também não está livre do problema.

Transcrição completa, fontes e traduções: https://theresmoretoit-channel.github.io/pt-br/videos/why-cant-windows-delete-a-file-in-use/

Capítulos
0:00 A mensagem que todo mundo conhece
0:29 Qual programa?
1:02 O Windows já te conta
1:30 O que você preenche ao abrir um arquivo
2:16 FILE_SHARE_DELETE
2:41 Uma violação de compartilhamento
2:53 No Linux simplesmente funciona
3:16 Um nome não é o arquivo
3:48 Quinhentos megabytes que somem
4:34 Renomear, e um limite
5:36 O Windows faz a mesma coisa
6:31 Reinicie o computador
7:03 O Gerenciador de Reinicialização
7:38 Mas esse não é o motivo todo
8:16 Quanto custa cada escolha
9:11 Então o que significa abrir um arquivo?

As legendas foram escritas para este vídeo, não geradas automaticamente. Há uma faixa de áudio em inglês americano disponível como segunda faixa de áudio.

A música é gerada proceduralmente para este canal.
```

## Türkçe (`tr`)

```
Windows kullanımdaki bir dosyayı neden silemiyor?
```

```
Bir dosyayı silmeye çalışıyorsun. Windows dosyanın başka bir programda açık olduğunu söylüyor. Ama hangisinde olduğunu söylemiyor.

Bu ileti, çok daha tuhaf bir sorunun görünen ucu: bir dosyayı açmak aslında ne demek? Çünkü başka bir bilgisayarda aynı dosya, tam olarak aynı biçimde açıkken, tek bir itiraz olmadan siliniyor.

Önce işe yarayan kısım. Windows 2009'dan beri hangi program olduğunu biliyor ve sana söylüyor da — Kaynak İzleyicisi, CPU sekmesi, Associated Handles, dosyanın adını yaz. Kurulacak bir şey yok. İnsanlar yine de ayrı bir araç indirmeye devam etti, ve bunun bir nedeni vardı.

Sonra düzeneğin kendisi. Windows'ta bir dosyayı açmak iki şeyi doldurmak demek, ve ikincisi herkesle yapılan bir sözleşme: ben bunu açık tutarken başkaları ne yapabilir? Microsoft'un kendi belgeleri silme bayrağının altına bir satır ekliyor — silme yetkisi ad değiştirmeyi de kapsıyor. İşte bu yüzden hatanın adı "dosya meşgul" değil. Adı paylaşım ihlali.

Linux'ta aynı komut öylece çalışıyor, ve nedeni kulağa geldiğinden daha tuhaf. Beş yüz megabaytlık bir günlük dosyası yaptım, bir sürecin onu açık tutmasını sağladım ve sildim. Dizin listesi hiçbir şey göstermiyor. Klasörü ölçen araç sıfır diyor. Diski ölçen araç beş yüz megabaytın hâlâ eksik olduğunu söylüyor.

Ve sonra beklemediğim dönüş: Windows tam olarak aynı şeyi yapabiliyor. NTFS üzerinde POSIX tarzı bir silme isteyebiliyor, ve Microsoft sonucu bir Unix kılavuzunun kullanacağı sözcüklerle anlatıyor. İki sistem de ikisini yapabiliyor. Farklı olan, varsayılan davranış.

Bu fark, Windows'un eskiden neden bu kadar sık yeniden başlatma istediğinin bir parçası — Microsoft bunu, tam da bundan kaçınmak için yapılmış aracın belgelerinde söylüyor. Ama açıklamanın tamamı değil, ve Linux da bu sorundan muaf değil.

Metnin tamamı, kaynaklar ve çeviriler: https://theresmoretoit-channel.github.io/tr/videos/why-cant-windows-delete-a-file-in-use/

Bölümler
0:00 Herkesin bildiği ileti
0:29 Hangi program?
1:02 Windows bunu zaten söylüyor
1:30 Bir dosyayı açarken neyi doldurursun
2:16 FILE_SHARE_DELETE
2:41 Paylaşım ihlali
2:53 Linux'ta öylece çalışıyor
3:16 Ad, dosyanın kendisi değil
3:48 Yok olan beş yüz megabayt
4:34 Ad değiştirme ve bir sınır
5:36 Windows da aynısını yapabiliyor
6:31 Bilgisayarı yeniden başlatın
7:03 Yeniden Başlatma Yöneticisi
7:38 Ama bütün neden bu değil
8:16 Her seçimin bedeli
9:11 Peki bir dosyayı açmak ne demek?

Altyazılar bu video için yazıldı, otomatik olarak oluşturulmadı. İkinci ses parçası olarak Amerikan İngilizcesi ses parçası mevcuttur.

Müzik bu kanal için yordamsal olarak üretilmektedir.
```

## українська (`uk`)

```
Чому Windows не може видалити файл, який зараз використовується?
```

```
Ти намагаєшся видалити файл. Windows каже, що він відкритий в іншій програмі. Але не каже, в якій.

Це повідомлення — видимий кінець набагато дивнішого питання: що насправді означає відкрити файл? Бо на іншому комп'ютері той самий файл, відкритий точно так само, видаляється без жодного заперечення.

Спершу корисне. Windows з 2009 року знає, яка це програма, і він тобі це скаже — Монітор ресурсів, вкладка ЦП, Пов'язані дескриптори, впиши ім'я файлу. Нічого не треба встановлювати. Люди все одно далі завантажували окремий інструмент, і мали на те причину.

Далі механізм. У Windows відкрити файл означає заповнити дві речі, і друга — це договір з усіма іншими: що їм дозволено, поки він у мене відкритий? Власна документація Microsoft додає під прапорцем видалення один рядок — право на видалення охоплює й перейменування. Ось чому помилка зветься не «файл зайнятий». Вона зветься порушення спільного доступу.

У Linux та сама команда просто спрацьовує, і причина дивніша, ніж здається. Я зробив файл журналу на п'ятсот мегабайтів, лишив один процес тримати його відкритим і видалив його. Перелік каталогу не показує нічого. Інструмент, що міряє теку, каже нуль. Інструмент, що міряє диск, каже, що п'ятсот мегабайтів досі бракує.

А потім поворот, якого я не чекав: Windows уміє робити точно те саме. На NTFS він може попросити видалення в стилі POSIX, і Microsoft описує результат тими самими словами, що й посібник Unix. Обидві системи вміють і те, і те. Різниться те, що є типовим.

Ця різниця — частина відповіді на те, чому Windows колись так часто просив перезавантажитися. Microsoft каже це в документації інструмента, збудованого саме для того, щоб цього уникнути. Але це не все пояснення, і Linux від цієї проблеми теж не вільний.

Повний текст, джерела та переклади: https://theresmoretoit-channel.github.io/uk/videos/why-cant-windows-delete-a-file-in-use/

Розділи
0:00 Повідомлення, яке знають усі
0:29 Яка програма?
1:02 Windows уже тобі це каже
1:30 Що ти заповнюєш, відкриваючи файл
2:16 FILE_SHARE_DELETE
2:41 Порушення спільного доступу
2:53 У Linux просто спрацьовує
3:16 Ім'я — це не файл
3:48 П'ятсот мегабайтів, що зникають
4:34 Перейменування й одне обмеження
5:36 Windows уміє те саме
6:31 Перезавантажте комп'ютер
7:03 Диспетчер перезапуску
7:38 Але це не вся причина
8:16 Чого коштує кожен вибір
9:11 То що означає відкрити файл?

Субтитри написані для цього відео, а не згенеровані автоматично. Доступна аудіодоріжка американською англійською як друга звукова доріжка.

Музика генерується для цього каналу процедурно.
```

## Tiếng Việt (`vi`)

```
Vì sao Windows không xóa được tệp đang mở?
```

```
Bạn thử xóa một tệp. Windows nói rằng tệp đang mở trong một chương trình khác. Nhưng không nói là chương trình nào.

Thông báo đó là phần thấy được của một câu hỏi lạ hơn nhiều: mở một tệp thật ra nghĩa là gì? Bởi trên một máy khác, cùng tệp đó, mở y hệt như vậy, lại xóa được mà không một lời phàn nàn.

Trước hết là phần hữu ích. Windows đã biết đó là chương trình nào từ năm 2009, và nó sẵn sàng cho bạn biết — Trình theo dõi Tài nguyên, thẻ CPU, Associated Handles, gõ tên tệp vào. Không phải cài gì cả. Người ta vẫn cứ tải công cụ riêng về, và họ có lý do.

Rồi đến cơ chế. Trên Windows, mở một tệp nghĩa là điền hai thứ, và thứ hai là một hợp đồng với tất cả những người khác: họ được làm gì trong lúc tôi đang mở nó? Chính tài liệu của Microsoft thêm một dòng ngay dưới cờ xóa — quyền xóa bao gồm cả đổi tên. Đó là lý do lỗi này không mang tên "tệp đang bận". Nó tên là vi phạm chia sẻ.

Trên Linux cùng câu lệnh đó chạy bình thường, và lý do lạ hơn ta tưởng. Tôi tạo một tệp nhật ký năm trăm megabyte, để một tiến trình giữ nó mở, rồi xóa đi. Liệt kê thư mục chẳng hiện gì. Công cụ đo thư mục báo số không. Công cụ đo đĩa báo rằng năm trăm megabyte vẫn đang biến mất.

Và rồi cú lật mà tôi không ngờ tới: Windows làm được đúng y như vậy. Trên NTFS nó có thể yêu cầu một lệnh xóa kiểu POSIX, và Microsoft mô tả kết quả bằng đúng những từ mà một trang hướng dẫn Unix sẽ dùng. Cả hai hệ điều hành đều làm được cả hai. Khác nhau là ở mặc định.

Sự khác biệt ấy là một phần lý do vì sao Windows từng hay bắt khởi động lại đến thế — Microsoft nói điều đó ngay trong tài liệu của công cụ được tạo ra để tránh việc này. Nhưng đó không phải toàn bộ lời giải, và Linux cũng không thoát khỏi vấn đề này.

Toàn văn, nguồn và bản dịch: https://theresmoretoit-channel.github.io/vi/videos/why-cant-windows-delete-a-file-in-use/

Các chương
0:00 Thông báo ai cũng biết
0:29 Chương trình nào?
1:02 Windows vốn đã cho bạn biết
1:30 Bạn điền gì khi mở một tệp
2:16 FILE_SHARE_DELETE
2:41 Vi phạm chia sẻ
2:53 Trên Linux thì chạy bình thường
3:16 Cái tên không phải là tệp
3:48 Năm trăm megabyte biến mất
4:34 Đổi tên, và một giới hạn
5:36 Windows làm được điều tương tự
6:31 Hãy khởi động lại máy tính
7:03 Restart Manager
7:38 Nhưng đó không phải toàn bộ lý do
8:16 Mỗi lựa chọn phải trả giá gì
9:11 Vậy mở một tệp nghĩa là gì?

Phụ đề được viết riêng cho video này, không phải tạo tự động. Có bản âm thanh tiếng Anh Mỹ dưới dạng bản âm thanh thứ hai.

Nhạc được tạo theo thuật toán riêng cho kênh này.
```

## čeština (`cs`)

```
Proč Windows nesmaže soubor, který se právě používá?
```

```
Zkusíš smazat soubor. Windows oznámí, že je otevřený v jiném programu. Ale neřekne, ve kterém.

Ta hláška je viditelný konec mnohem podivnější otázky: co vlastně znamená otevřít soubor? Protože na jiném počítači se týž soubor, otevřený úplně stejně, smaže bez jediné námitky.

Nejdřív to užitečné. Windows od roku 2009 ví, který program to je, a řekne ti to — Sledování prostředků, záložka Procesor, Přidružené popisovače, napiš jméno souboru. Nic se neinstaluje. Lidé si stejně dál stahovali zvláštní nástroj, a měli k tomu důvod.

Pak mechanismus. Ve Windows znamená otevřít soubor vyplnit dvě věci, a ta druhá je smlouva se všemi ostatními: co smějí dělat, dokud ho mám otevřený? Vlastní dokumentace Microsoftu přidává pod příznak mazání jednu větu — právo mazat zahrnuje i přejmenování. Proto se ta chyba nejmenuje „soubor se používá". Jmenuje se porušení sdílení.

V Linuxu týž příkaz prostě projde, a důvod je divnější, než zní. Udělal jsem protokol o velikosti pět set megabajtů, nechal ho jeden proces otevřený a smazal ho. Výpis adresáře neukáže nic. Nástroj, který měří složku, hlásí nulu. Nástroj, který měří disk, hlásí, že pět set megabajtů pořád chybí.

A pak obrat, který jsem nečekal: Windows umí přesně totéž. Na NTFS si umí říct o mazání ve stylu POSIX, a Microsoft popisuje výsledek slovy, kterými by to napsal unixový manuál. Oba systémy umějí obojí. Liší se to výchozí.

Ten rozdíl je část odpovědi na to, proč Windows kdysi tak často žádal o restart — Microsoft to říká v dokumentaci nástroje, který se postavil právě proto, aby se tomu vyhnul. Ale není to celé vysvětlení, a Linux od toho problému taky není osvobozený.

Celý text, zdroje a překlady: https://theresmoretoit-channel.github.io/cs/videos/why-cant-windows-delete-a-file-in-use/

Kapitoly
0:00 Hláška, kterou zná každý
0:29 Který program?
1:02 Windows ti to říká už teď
1:30 Co vyplňuješ, když otevíráš soubor
2:16 FILE_SHARE_DELETE
2:41 Porušení sdílení
2:53 V Linuxu to prostě projde
3:16 Jméno není soubor
3:48 Pět set megabajtů, které zmizí
4:34 Přejmenování a jedno omezení
5:36 Windows umí totéž
6:31 Restartujte počítač
7:03 Správce restartů
7:38 Ale to není celý důvod
8:16 Co která volba stojí
9:11 Tak co znamená otevřít soubor?

Titulky jsou k tomuhle videu napsané, ne strojově vygenerované. K dispozici je americká anglická zvuková stopa jako druhá zvuková stopa.

Hudba se pro tenhle kanál generuje procedurálně.
```

## español (`es`)

```
¿Por qué Windows no puede borrar un archivo que está en uso?
```

```
Intentas borrar un archivo. Windows dice que está abierto en otro programa. Pero no dice en cuál.

Ese mensaje es el extremo visible de una pregunta mucho más rara: ¿qué significa en realidad abrir un archivo? Porque en otro ordenador el mismo archivo, abierto exactamente igual, se borra sin una sola queja.

Primero lo útil. Windows sabe desde 2009 qué programa es, y te lo dice — Monitor de recursos, pestaña CPU, Identificadores asociados, escribe el nombre del archivo. Nada que instalar. Aun así la gente siguió descargando una herramienta aparte, y tenía un motivo.

Luego el mecanismo. En Windows, abrir un archivo significa rellenar dos cosas, y la segunda es un contrato con todos los demás: ¿qué pueden hacer mientras yo lo tengo abierto? La propia documentación de Microsoft añade una línea bajo el indicador de borrado: el permiso de borrar abarca también el renombrado. Por eso el error no se llama "archivo en uso". Se llama infracción de uso compartido.

En Linux la misma orden simplemente funciona, y el motivo es más raro de lo que suena. Hice un archivo de registro de quinientos megabytes, dejé un proceso teniéndolo abierto y lo borré. El listado del directorio no muestra nada. La herramienta que mide la carpeta dice cero. La que mide el disco dice que quinientos megabytes siguen faltando.

Y entonces el giro que no esperaba: Windows sabe hacer exactamente lo mismo. En NTFS puede pedir un borrado al estilo POSIX, y Microsoft describe el resultado con las mismas palabras que usaría un manual de Unix. Ambos sistemas saben hacer las dos cosas. Lo que cambia es lo predeterminado.

Esa diferencia es parte de por qué Windows pedía reiniciar tan a menudo: lo dice Microsoft en la documentación de la herramienta construida para evitarlo. Pero no es toda la explicación, y Linux tampoco está libre del problema.

Transcripción completa, fuentes y traducciones: https://theresmoretoit-channel.github.io/es/videos/why-cant-windows-delete-a-file-in-use/

Capítulos
0:00 El mensaje que todos conocen
0:29 ¿Qué programa?
1:02 Windows ya te lo dice
1:30 Qué rellenas al abrir un archivo
2:16 FILE_SHARE_DELETE
2:41 Una infracción de uso compartido
2:53 En Linux simplemente funciona
3:16 Un nombre no es el archivo
3:48 Quinientos megabytes que desaparecen
4:34 Renombrar, y un límite
5:36 Windows sabe hacer lo mismo
6:31 Reinicia el ordenador
7:03 El Administrador de reinicio
7:38 Pero esa no es toda la razón
8:16 Lo que cuesta cada elección
9:11 Entonces, ¿qué significa abrir un archivo?

Los subtítulos están escritos para este vídeo, no generados automáticamente. Hay una pista de audio en inglés americano disponible como segunda pista de audio.

La música se genera de forma procedural para este canal.
```

## svenska (`sv`)

```
Varför kan Windows inte radera en fil som används?
```

```
Du försöker radera en fil. Windows säger att den är öppen i ett annat program. Men inte vilket.

Det meddelandet är den synliga änden på en mycket märkligare fråga: vad betyder det egentligen att öppna en fil? För på en annan dator raderas samma fil, öppnad på exakt samma sätt, utan att någon klagar.

Först det användbara. Windows har vetat sedan 2009 vilket program det är, och det berättar det för dig — Resursövervakaren, fliken Processor, Tillhörande referenser, skriv filens namn. Inget att installera. Folk fortsatte ändå att ladda ner ett separat verktyg, och de hade ett skäl.

Sedan mekanismen. I Windows betyder det att öppna en fil att fylla i två saker, och den andra är ett kontrakt med alla andra: vad får de göra medan jag har den öppen? Microsofts egen dokumentation lägger en rad under raderingsflaggan — rätten att radera omfattar även namnbyte. Det är därför felet inte heter "filen används". Det heter delningsöverträdelse.

I Linux fungerar samma kommando bara, och skälet är märkligare än det låter. Jag gjorde en loggfil på femhundra megabyte, lät en process hålla den öppen och raderade den. Listningen av katalogen visar ingenting. Verktyget som mäter mappen säger noll. Verktyget som mäter disken säger att femhundra megabyte fortfarande saknas.

Och sedan vändningen jag inte väntade mig: Windows kan göra precis samma sak. På NTFS kan det be om en radering i POSIX-stil, och Microsoft beskriver resultatet med samma ord som en Unix-manual skulle använda. Båda systemen klarar båda sakerna. Det som skiljer är standardläget.

Den skillnaden är en del av varför Windows förr bad om omstart så ofta — Microsoft säger det i dokumentationen till verktyget som byggdes för att undvika det. Men det är inte hela förklaringen, och Linux är inte heller fritt från problemet.

Hela texten, källor och översättningar: https://theresmoretoit-channel.github.io/sv/videos/why-cant-windows-delete-a-file-in-use/

Kapitel
0:00 Meddelandet som alla känner igen
0:29 Vilket program?
1:02 Windows berättar det redan
1:30 Vad du fyller i när du öppnar en fil
2:16 FILE_SHARE_DELETE
2:41 En delningsöverträdelse
2:53 I Linux fungerar det bara
3:16 Ett namn är inte filen
3:48 Femhundra megabyte som försvinner
4:34 Namnbyte, och en gräns
5:36 Windows kan göra samma sak
6:31 Starta om datorn
7:03 Omstartshanteraren
7:38 Men det är inte hela skälet
8:16 Vad varje val kostar
9:11 Så vad betyder det att öppna en fil?

Undertexterna är skrivna för den här videon, inte automatgenererade. Ett amerikansk-engelskt ljudspår finns tillgängligt som andra ljudspår.

Musiken genereras proceduralt för den här kanalen.
```
