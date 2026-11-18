# Lokalizované názvy a popisy — Why Does Your Computer Ignore You When It's Busy?

Podklad pro **YouTube Studio → video → Podrobnosti → Přidat jazyk**.
Pro každý jazyk jsou tu **dva bloky ke zkopírování**: název a popis.
Kopíruje se **celý blok mezi trojicí zpětných apostrofů**, co je mimo něj,
je poznámka. Anglický originál zůstává v `youtube.md` a nesahá se na něj.

Nahrává je `tools/lokalizace.py`, který čte právě tenhle formát.

## Co se NEPŘEKLÁDÁ

| | |
|---|---|
| **Windows** | název systému |
| **Mars Pathfinder**, **Pathfinder** | jméno sondy |
| **thrashing** | odborný termín; jazyky ho buď přebírají (de, it, pt-BR, pl, sv, tr, id, vi, fi), nebo mají vlastní slovo (es *hiperpaginación*, uk *трешинг*) — drží se tvar použitý ve `script.<kód>.md` |
| **NASA**, **NASA/JPL**, **NASA/JPL-Caltech** | jména institucí |
| **názvy archivních snímků** | *Mars Pathfinder Presidential Panorama*, *Pathfinder on Mars (PIA01120)*, *Mars Pathfinder Rover Team* — vlastní jména děl |
| **časy kapitol** | musí sedět na vteřinu, jinak je YouTube neuzná |
| **tagy** | YouTube je per-jazyk nemá |

Názvy kapitol se naopak **překládají** — divák je čte v seznamu pod videem.
Překládá se i *public domain* tam, kde jazyk má vžitý tvar (cs *volné dílo*,
es *dominio público*, it *pubblico dominio*); ve fi a sv se používá
*public domain*, protože tak se to v těch jazycích běžně píše.

## Kontrola čísel

Kapitol je **patnáct** a časy se nepřekládají. Archivní snímky jsou **tři**,
všechny NASA. Věta o titulcích **nejmenuje počet jazyků** (rozhodnuto
2026-09-15) a **věta o americké audiostopě tu není** — v `youtube.md` je
vysvětleno proč a co se dopíše, až ji uživatel do Studia nahraje.

> **Atribuce je uvnitř bloku.** Všechny tři snímky jsou public domain,
> kde uvedení autora povinné není, ale uvádí se — jinak by popis tvrdil
> míň, než `LICENSES.md` dokládá.

> **Registr:** čeština **tyká** (36,0 „you" na 1000 slov, viz `notes.md`),
> takže tykají i ukrajinština, turečtina a indonéština. Finština drží
> „sinä" a vietnamština „bạn" — tam ta volba není.

> **Tři pasti originálu:** *„being noticed"* vs *„being served"* je celá
> osa videa a musí zůstat jako dvě různá slovesa; *„not slow but late"*
> je pointa S51–S52, takže „pozdě" nesmí splynout s „pomalu"; a *„one
> event"* v poslední kapitole je **jedna** událost, ne „událost".

## suomi (`fi`)

```
Miksi tietokone ei kuuntele sinua, kun sillä on kiire?
```

```
Napsautat painiketta. Mitään ei tapahdu. Napsautat uudestaan. Yhä ei
mitään. Ja sitten, viisi sekuntia myöhemmin, kaikki tulee kerralla.

Outoa on tämä: kone tiesi. Se tiesi mikrosekunneissa. Juuri nyt, kun se
ei tee mitään erityistä, koneesi hoitaa tuhansia laitetapahtumia
sekunnissa, ja se mekanismi on ollut olemassa viisikymmenluvulta asti.

Miksi napsautus sitten jää makaamaan?

Tämä video kertoo kuilusta, joka on huomatuksi tulemisen ja palvelluksi
tulemisen välillä. Keskeytys saa koneen huomion, mutta se ei vie
ohjelmaasi suorittimelle — ja ilmeinen korjaus, syötteen nostaminen
korkeimpaan prioriteettiin, epäonnistuu tavalla, joka kerran käynnisti
avaruusaluksen uudelleen Marsissa.

Matkan varrella: miksi sadan prosentin suoritin ei tarkoita jumia, miksi
kone ei useinkaan ole hidas vaan myöhässä, miksi pullonkaula on joskus
muisti eikä suoritin, ja miksi sovellus voi kalveta ja lakata
vastaamasta, vaikka järjestelmä sen ympärillä on täysin elossa.

Koko teksti, lähteet ja käännökset: https://theresmoretoit-channel.github.io/fi/videos/why-does-your-computer-ignore-you-when-its-busy/

Luvut:
0:00 Napsautus. Mitään ei tapahdu.
1:18 Mikä keskeytys oikeastaan on
2:11 Käsittelijä tekee niin vähän kuin voi
2:52 Ensimmäinen vastaus: huomio ei ole suoritin
3:04 Annetaan syötteelle korkein prioriteetti
3:26 Mars, 1997
4:15 Prioriteetin inversio
4:37 Korkea prioriteetti ei tarkoita, että sinua palvellaan
4:53 Prioriteetti ei luo syklejä
5:28 Ei hidas. Myöhässä.
5:50 Kun suoritin ei ole ongelma
6:33 Sovellus, joka ei vastaa
7:31 Eikä mikään ole vielä päätynyt näytölle
8:03 Sillä ei ole aavistustakaan, miksi liikutit hiirtä
8:37 Napsautuksesi ei ollut koskaan yksi tapahtuma

Tekstitykset on kirjoitettu tätä videota varten, niitä ei ole tuotettu
automaattisesti. Amerikanenglanninkielinen ääniraita on saatavilla toisena ääniraitana.

KUVALÄHTEET
Mars Pathfinder Presidential Panorama — NASA, public domain
Pathfinder on Mars (PIA01120) — NASA/JPL, public domain
Mars Pathfinder Rover Team — NASA/JPL-Caltech, public domain

Kaikki muu kuvamateriaali on piirretty projektin omista lähdetiedostoista.
```

## français (`fr`)

```
Pourquoi ton ordinateur t'ignore-t-il quand il est occupé ?
```

```
Tu cliques sur un bouton. Rien ne se passe. Tu cliques encore. Toujours
rien. Et puis, cinq secondes plus tard, tout arrive d'un coup.

Voilà le plus étrange : l'ordinateur savait. Il le savait en quelques
microsecondes. En ce moment même, sans rien faire de particulier, ta
machine traite des milliers d'événements matériels par seconde, et le
mécanisme qui rend ça possible existe depuis les années cinquante.

Alors pourquoi le clic reste-t-il en plan ?

Cette vidéo parle de l'écart entre être remarqué et être servi. Une
interruption obtient l'attention de l'ordinateur, mais elle ne met pas
ton programme sur un processeur — et la solution évidente, donner à
l'entrée la priorité la plus haute, échoue d'une façon qui a un jour
redémarré une sonde sur Mars.

En chemin : pourquoi un processeur à cent pour cent ne veut pas dire
figé, pourquoi la machine n'est souvent pas lente mais en retard,
pourquoi le goulot d'étranglement est parfois la mémoire et non le
processeur, et pourquoi une application peut pâlir et cesser de répondre
alors que le système autour d'elle est parfaitement vivant.

Transcription complète, sources et traductions : https://theresmoretoit-channel.github.io/fr/videos/why-does-your-computer-ignore-you-when-its-busy/

Chapitres :
0:00 Clic. Rien ne se passe.
1:18 Ce qu'est vraiment une interruption
2:11 Le gestionnaire en fait le moins possible
2:52 Première réponse : l'attention n'est pas un processeur
3:04 Donnons donc à l'entrée la priorité la plus haute
3:26 Mars, 1997
4:15 L'inversion de priorité
4:37 Haute priorité ne veut pas dire être servi
4:53 La priorité ne crée aucun cycle
5:28 Pas lent. En retard.
5:50 Quand le problème n'est pas le processeur
6:33 L'application qui ne répond pas
7:31 Et rien n'est encore arrivé à l'écran
8:03 Elle n'a aucune idée de pourquoi tu as bougé la souris
8:37 Ton clic n'a jamais été un seul événement

Les sous-titres sont écrits pour cette vidéo, ils ne sont pas générés
automatiquement. Une piste audio en anglais américain est disponible comme deuxième piste.

CRÉDITS IMAGES
Mars Pathfinder Presidential Panorama — NASA, domaine public
Pathfinder on Mars (PIA01120) — NASA/JPL, domaine public
Mars Pathfinder Rover Team — NASA/JPL-Caltech, domaine public

Toutes les autres images proviennent des fichiers sources du projet.
```

## Bahasa Indonesia (`id`)

```
Kenapa Komputermu Mengabaikanmu Saat Sedang Sibuk?
```

```
Kamu mengeklik sebuah tombol. Tidak terjadi apa-apa. Kamu mengeklik
lagi. Tetap tidak ada. Lalu, lima detik kemudian, semuanya datang
sekaligus.

Inilah bagian anehnya: komputer itu tahu. Ia tahu dalam hitungan
mikrodetik. Saat ini juga, tanpa mengerjakan sesuatu yang khusus,
mesinmu menangani ribuan peristiwa perangkat keras setiap detik, dan
mekanisme yang memungkinkannya sudah ada sejak tahun lima puluhan.

Jadi kenapa klik itu diam saja di sana?

Video ini tentang jurang antara diperhatikan dan dilayani. Ternyata
interupsi mendapatkan perhatian komputer, tapi ia tidak menaruh
programmu di prosesor — dan perbaikan yang kelihatannya jelas, memberi
masukan prioritas tertinggi, gagal dengan cara yang pernah membuat
sebuah wahana di Mars berulang kali menyalakan ulang dirinya.

Di sepanjang jalan: kenapa prosesor pada seratus persen tidak berarti
membeku, kenapa mesin sering kali bukan lambat melainkan terlambat,
kenapa sumbatannya kadang memori dan bukan prosesor, dan kenapa sebuah
aplikasi bisa memudar dan berhenti menjawab sementara sistem di
sekelilingnya hidup sepenuhnya.

Transkrip lengkap, sumber, dan terjemahan: https://theresmoretoit-channel.github.io/id/videos/why-does-your-computer-ignore-you-when-its-busy/

Bab:
0:00 Klik. Tidak terjadi apa-apa.
1:18 Apa sebenarnya interupsi itu
2:11 Penangan mengerjakan sesedikit mungkin
2:52 Jawaban pertama: perhatian bukan prosesor
3:04 Kalau begitu beri masukan prioritas tertinggi
3:26 Mars, 1997
4:15 Inversi prioritas
4:37 Prioritas tinggi tidak berarti kamu dilayani
4:53 Prioritas tidak menciptakan siklus
5:28 Bukan lambat. Terlambat.
5:50 Ketika masalahnya bukan prosesor
6:33 Aplikasi yang tidak mau menjawab
7:31 Dan belum ada apa pun yang sampai ke layar
8:03 Ia tidak tahu kenapa kamu menggerakkan tetikus
8:37 Klikmu tak pernah satu peristiwa saja

Subtitle ditulis khusus untuk video ini, bukan dibuat otomatis. Trek audio bahasa Inggris Amerika tersedia sebagai trek audio kedua.

KREDIT GAMBAR
Mars Pathfinder Presidential Panorama — NASA, domain publik
Pathfinder on Mars (PIA01120) — NASA/JPL, domain publik
Mars Pathfinder Rover Team — NASA/JPL-Caltech, domain publik

Semua visual lainnya digambar dari berkas sumber proyek ini sendiri.
```

## italiano (`it`)

```
Perché il computer ti ignora quando è occupato?
```

```
Clicchi un pulsante. Non succede niente. Clicchi di nuovo. Ancora
niente. E poi, cinque secondi dopo, arriva tutto insieme.

Ed ecco la parte strana: il computer lo sapeva. Lo sapeva in pochi
microsecondi. Proprio adesso, senza fare niente di particolare, la tua
macchina sta gestendo migliaia di eventi hardware al secondo, e il
meccanismo che lo rende possibile c'è fin dagli anni cinquanta.

Allora perché il clic resta lì?

Questo video parla della distanza fra essere notati ed essere serviti.
Un'interruzione ottiene l'attenzione del computer, ma non porta il tuo
programma su un processore — e la soluzione ovvia, dare all'input la
priorità più alta, fallisce in un modo che una volta ha fatto riavviare
una sonda su Marte.

Lungo la strada: perché un processore al cento per cento non vuol dire
bloccato, perché la macchina spesso non è lenta ma in ritardo, perché il
collo di bottiglia a volte è la memoria e non il processore, e perché
un'applicazione può sbiadire e smettere di rispondere mentre il sistema
attorno a lei è perfettamente vivo.

Trascrizione completa, fonti e traduzioni: https://theresmoretoit-channel.github.io/it/videos/why-does-your-computer-ignore-you-when-its-busy/

Capitoli:
0:00 Clic. Non succede niente.
1:18 Cos'è davvero un'interruzione
2:11 Il gestore fa il meno possibile
2:52 Prima risposta: l'attenzione non è un processore
3:04 Diamo allora all'input la priorità più alta
3:26 Marte, 1997
4:15 Inversione di priorità
4:37 Priorità alta non vuol dire essere serviti
4:53 La priorità non crea cicli
5:28 Non lento. In ritardo.
5:50 Quando il problema non è il processore
6:33 L'applicazione che non risponde
7:31 E sullo schermo non è ancora arrivato niente
8:03 Non ha idea del perché hai mosso il mouse
8:37 Il tuo clic non è mai stato un solo evento

I sottotitoli sono scritti per questo video, non generati
automaticamente. È disponibile una traccia audio in inglese americano come seconda traccia.

CREDITI IMMAGINI
Mars Pathfinder Presidential Panorama — NASA, pubblico dominio
Pathfinder on Mars (PIA01120) — NASA/JPL, pubblico dominio
Mars Pathfinder Rover Team — NASA/JPL-Caltech, pubblico dominio

Tutte le altre immagini vengono dai file sorgente del progetto.
```

## Deutsch (`de`)

```
Warum ignoriert dich dein Rechner, wenn er beschäftigt ist?
```

```
Du klickst auf eine Schaltfläche. Nichts passiert. Du klickst noch mal.
Immer noch nichts. Und dann, fünf Sekunden später, kommt alles auf
einmal.

Und jetzt das Seltsame: Der Rechner wusste es. Er wusste es innerhalb
von Mikrosekunden. Gerade jetzt, ohne irgendetwas Besonderes zu tun,
verarbeitet deine Maschine Tausende Hardware-Ereignisse pro Sekunde, und
den Mechanismus dafür gibt es seit den Fünfzigern.

Warum bleibt der Klick dann liegen?

In diesem Video geht es um den Abstand zwischen bemerkt werden und
bedient werden. Ein Interrupt verschafft sich die Aufmerksamkeit des
Rechners, aber er bringt dein Programm nicht auf einen Prozessor — und
die naheliegende Lösung, der Eingabe die höchste Priorität zu geben,
scheitert auf eine Weise, die einmal eine Sonde auf dem Mars immer
wieder neu gestartet hat.

Unterwegs: warum ein Prozessor bei hundert Prozent nicht eingefroren
heißt, warum die Maschine oft nicht langsam ist, sondern zu spät kommt,
warum der Engpass manchmal der Speicher ist und nicht der Prozessor, und
warum eine Anwendung blass werden und aufhören kann zu antworten,
während das System um sie herum vollkommen lebendig ist.

Vollständiger Text, Quellen und Übersetzungen: https://theresmoretoit-channel.github.io/de/videos/why-does-your-computer-ignore-you-when-its-busy/

Kapitel:
0:00 Klick. Nichts passiert.
1:18 Was ein Interrupt wirklich ist
2:11 Der Handler tut so wenig wie möglich
2:52 Erste Antwort: Aufmerksamkeit ist kein Prozessor
3:04 Also geben wir der Eingabe die höchste Priorität
3:26 Mars, 1997
4:15 Prioritätsinversion
4:37 Hohe Priorität heißt nicht, dass du bedient wirst
4:53 Priorität erzeugt keine Taktzyklen
5:28 Nicht langsam. Zu spät.
5:50 Wenn der Prozessor nicht das Problem ist
6:33 Die Anwendung, die nicht antwortet
7:31 Und auf dem Bildschirm ist noch nichts angekommen
8:03 Er hat keine Ahnung, warum du die Maus bewegt hast
8:37 Dein Klick war nie ein einziges Ereignis

Die Untertitel sind für dieses Video geschrieben, nicht automatisch
generiert. Eine amerikanisch-englische Tonspur ist als zweite Tonspur verfügbar.

BILDNACHWEISE
Mars Pathfinder Presidential Panorama — NASA, gemeinfrei
Pathfinder on Mars (PIA01120) — NASA/JPL, gemeinfrei
Mars Pathfinder Rover Team — NASA/JPL-Caltech, gemeinfrei

Alle anderen Bilder stammen aus den eigenen Quelldateien des Projekts.
```

## polski (`pl`)

```
Dlaczego komputer cię ignoruje, kiedy jest zajęty?
```

```
Klikasz przycisk. Nic się nie dzieje. Klikasz jeszcze raz. Wciąż nic. A
potem, pięć sekund później, wszystko przychodzi naraz.

I tu rzecz dziwna: komputer wiedział. Wiedział w ciągu mikrosekund.
Właśnie teraz, nie robiąc nic szczególnego, twoja maszyna obsługuje
tysiące zdarzeń sprzętowych na sekundę, a mechanizm, który to
umożliwia, istnieje od lat pięćdziesiątych.

To dlaczego kliknięcie tam leży?

Ten film jest o przepaści między byciem zauważonym a byciem obsłużonym.
Przerwanie zdobywa uwagę komputera, ale nie stawia twojego programu na
procesorze — a oczywista poprawka, danie wejściu najwyższego priorytetu,
zawodzi w sposób, który kiedyś raz za razem restartował sondę na Marsie.

Po drodze: dlaczego procesor na stu procentach nie oznacza zawieszenia,
dlaczego maszyna często nie jest wolna, tylko się spóźnia, dlaczego
wąskim gardłem bywa pamięć, a nie procesor, i dlaczego aplikacja może
zblednąć i przestać odpowiadać, kiedy system wokół niej jest zupełnie
żywy.

Pełna transkrypcja, źródła i tłumaczenia: https://theresmoretoit-channel.github.io/pl/videos/why-does-your-computer-ignore-you-when-its-busy/

Rozdziały:
0:00 Klik. Nic się nie dzieje.
1:18 Czym właściwie jest przerwanie
2:11 Procedura obsługi robi jak najmniej
2:52 Pierwsza odpowiedź: uwaga to nie procesor
3:04 To dajmy wejściu najwyższy priorytet
3:26 Mars, 1997
4:15 Inwersja priorytetów
4:37 Wysoki priorytet nie znaczy, że zostaniesz obsłużony
4:53 Priorytet nie tworzy cykli
5:28 Nie wolny. Spóźniony.
5:50 Kiedy problemem nie jest procesor
6:33 Aplikacja, która nie odpowiada
7:31 A na ekran wciąż nic nie dotarło
8:03 Nie ma pojęcia, dlaczego ruszyłeś myszą
8:37 Twoje kliknięcie nigdy nie było jednym zdarzeniem

Napisy są napisane do tego filmu, nie wygenerowane automatycznie. Dostępna jest amerykańska angielska ścieżka dźwiękowa jako druga ścieżka.

ŹRÓDŁA ZDJĘĆ
Mars Pathfinder Presidential Panorama — NASA, domena publiczna
Pathfinder on Mars (PIA01120) — NASA/JPL, domena publiczna
Mars Pathfinder Rover Team — NASA/JPL-Caltech, domena publiczna

Cała reszta grafiki powstała z własnych plików źródłowych projektu.
```

## português (Brasil) (`pt-BR`)

```
Por que seu computador te ignora quando está ocupado?
```

```
Você clica num botão. Não acontece nada. Clica de novo. Ainda nada. E
então, cinco segundos depois, tudo chega de uma vez.

E aqui vem a parte estranha: o computador sabia. Sabia em
microssegundos. Agora mesmo, sem fazer nada de especial, sua máquina
está lidando com milhares de eventos de hardware por segundo, e o
mecanismo que torna isso possível existe desde os anos cinquenta.

Então por que o clique fica parado ali?

Este vídeo é sobre a distância entre ser percebido e ser atendido. Uma
interrupção conquista a atenção do computador, mas não coloca o seu
programa num processador — e a correção óbvia, dar à entrada a
prioridade mais alta, falha de um jeito que uma vez fez uma sonda em
Marte reiniciar sozinha.

No caminho: por que um processador a cem por cento não quer dizer
travado, por que a máquina muitas vezes não está lenta, mas atrasada,
por que o gargalo às vezes é a memória e não o processador, e por que um
aplicativo pode desbotar e parar de responder enquanto o sistema à volta
dele está perfeitamente vivo.

Transcrição completa, fontes e traduções: https://theresmoretoit-channel.github.io/pt-br/videos/why-does-your-computer-ignore-you-when-its-busy/

Capítulos:
0:00 Clique. Não acontece nada.
1:18 O que é de fato uma interrupção
2:11 O tratador faz o mínimo possível
2:52 Primeira resposta: atenção não é processador
3:04 Então dê à entrada a prioridade mais alta
3:26 Marte, 1997
4:15 Inversão de prioridade
4:37 Prioridade alta não quer dizer que você será atendido
4:53 Prioridade não cria ciclos
5:28 Não lento. Atrasado.
5:50 Quando o problema não é o processador
6:33 O aplicativo que não responde
7:31 E nada chegou à tela ainda
8:03 Ele não faz ideia de por que você moveu o mouse
8:37 Seu clique nunca foi um evento só

As legendas foram escritas para este vídeo, não geradas automaticamente. Há uma faixa de áudio em inglês americano disponível como segunda faixa.

CRÉDITOS DE IMAGEM
Mars Pathfinder Presidential Panorama — NASA, domínio público
Pathfinder on Mars (PIA01120) — NASA/JPL, domínio público
Mars Pathfinder Rover Team — NASA/JPL-Caltech, domínio público

Todo o resto das imagens vem dos arquivos de origem do próprio projeto.
```

## Türkçe (`tr`)

```
Bilgisayarın meşgulken seni neden görmezden gelir?
```

```
Bir düğmeye tıklıyorsun. Hiçbir şey olmuyor. Bir daha tıklıyorsun. Yine
hiçbir şey. Sonra, beş saniye sonra, her şey bir anda geliyor.

İşin tuhaf yanı şu: bilgisayar biliyordu. Mikrosaniyeler içinde
biliyordu. Tam şu anda, özel bir şey yapmıyorken, makinen saniyede
binlerce donanım olayıyla uğraşıyor ve bunu mümkün kılan düzenek ellili
yıllardan beri orada.

Peki tıklama neden öylece duruyor?

Bu video, fark edilmekle hizmet görmek arasındaki boşluğu anlatıyor.
Kesme, bilgisayarın dikkatini alıyor, ama programını bir işlemciye
bindirmiyor — ve akla ilk gelen çözüm, girdiye en yüksek önceliği
vermek, bir zamanlar Mars'taki bir aracı defalarca yeniden başlatan
biçimde başarısız oluyor.

Yol boyunca: işlemcinin yüzde yüzde olması neden donmuş demek değil,
makine neden çoğu zaman yavaş değil de geç kalmış oluyor, darboğaz neden
bazen işlemci değil bellek oluyor, ve çevresindeki sistem gayet
canlıyken bir uygulama neden solup yanıt vermeyi bırakabiliyor.

Metnin tamamı, kaynaklar ve çeviriler: https://theresmoretoit-channel.github.io/tr/videos/why-does-your-computer-ignore-you-when-its-busy/

Bölümler:
0:00 Tıklama. Hiçbir şey olmuyor.
1:18 Kesme aslında nedir
2:11 İşleyici yapabileceği en azı yapar
2:52 İlk cevap: dikkat bir işlemci değildir
3:04 O zaman girdiye en yüksek önceliği verelim
3:26 Mars, 1997
4:15 Öncelik tersinmesi
4:37 Yüksek öncelik, hizmet göreceğin anlamına gelmez
4:53 Öncelik çevrim yaratmaz
5:28 Yavaş değil. Geç.
5:50 Sorun işlemci olmadığında
6:33 Yanıt vermeyen uygulama
7:31 Ve ekrana daha hiçbir şey ulaşmadı
8:03 Fareyi neden oynattığına dair hiçbir fikri yok
8:37 Tıklaman hiçbir zaman tek bir olay değildi

Altyazılar bu video için yazıldı, otomatik üretilmedi. İkinci ses parçası olarak Amerikan İngilizcesi ses parçası mevcut.

GÖRSEL KAYNAKLARI
Mars Pathfinder Presidential Panorama — NASA, kamu malı
Pathfinder on Mars (PIA01120) — NASA/JPL, kamu malı
Mars Pathfinder Rover Team — NASA/JPL-Caltech, kamu malı

Diğer bütün görseller projenin kendi kaynak dosyalarından çizildi.
```

## українська (`uk`)

```
Чому комп'ютер ігнорує тебе, коли він зайнятий?
```

```
Ти клацаєш на кнопку. Нічого не відбувається. Клацаєш ще раз. Усе одно
нічого. А потім, за п'ять секунд, усе прилітає нараз.

І ось що дивно: комп'ютер знав. Знав протягом мікросекунд. Просто зараз,
не роблячи нічого особливого, твоя машина опрацьовує тисячі апаратних
подій щосекунди, і механізм, який це уможливлює, існує ще від
п'ятдесятих.

То чому ж те клацання просто лежить?

Це відео про прірву між тим, щоб тебе помітили, і тим, щоб тебе
обслужили. Переривання здобуває увагу комп'ютера, але не ставить твою
програму на процесор — а очевидне виправлення, дати вводу найвищий
пріоритет, провалюється у спосіб, який колись раз за разом
перезапускав апарат на Марсі.

Дорогою: чому процесор на ста відсотках не означає зависання, чому
машина часто не повільна, а запізнюється, чому вузьким місцем іноді є
пам'ять, а не процесор, і чому застосунок може зблідніти й перестати
відповідати, поки система довкола нього цілком жива.

Повний текст, джерела та переклади: https://theresmoretoit-channel.github.io/uk/videos/why-does-your-computer-ignore-you-when-its-busy/

Розділи:
0:00 Клац. Нічого не відбувається.
1:18 Що таке переривання насправді
2:11 Обробник робить якомога менше
2:52 Перша відповідь: увага — це не процесор
3:04 То дамо вводу найвищий пріоритет
3:26 Марс, 1997
4:15 Інверсія пріоритетів
4:37 Високий пріоритет не означає, що тебе обслужать
4:53 Пріоритет не створює тактів
5:28 Не повільний. Запізнюється.
5:50 Коли проблема не в процесорі
6:33 Застосунок, який не відповідає
7:31 А на екран ще нічого не потрапило
8:03 Він гадки не має, чому ти рухнув мишею
8:37 Твоє клацання ніколи не було однією подією

Субтитри написані саме до цього відео, а не згенеровані автоматично. Як друга звукова доріжка доступна доріжка американською англійською.

ДЖЕРЕЛА ЗОБРАЖЕНЬ
Mars Pathfinder Presidential Panorama — NASA, суспільне надбання
Pathfinder on Mars (PIA01120) — NASA/JPL, суспільне надбання
Mars Pathfinder Rover Team — NASA/JPL-Caltech, суспільне надбання

Уся решта графіки намальована з власних вихідних файлів проєкту.
```

## Tiếng Việt (`vi`)

```
Vì sao máy tính phớt lờ bạn khi nó đang bận?
```

```
Bạn bấm một nút. Không có gì xảy ra. Bạn bấm lại. Vẫn không gì. Rồi, năm
giây sau, mọi thứ ập đến cùng một lúc.

Và đây mới là chỗ lạ: máy tính đã biết. Nó biết trong vòng vài
micro giây. Ngay lúc này, khi không làm gì đặc biệt, máy của bạn đang xử
lý hàng nghìn sự kiện phần cứng mỗi giây, và cơ chế làm được điều đó đã
có từ những năm năm mươi.

Vậy vì sao cú bấm cứ nằm đó?

Video này nói về khoảng cách giữa được nhận thấy và được phục vụ. Một
ngắt giành được sự chú ý của máy tính, nhưng nó không đưa chương trình
của bạn lên bộ xử lý — và cách sửa tưởng như hiển nhiên, cho đầu vào ưu
tiên cao nhất, thất bại theo kiểu từng khiến một tàu thăm dò trên Sao
Hỏa tự khởi động lại hết lần này đến lần khác.

Trên đường đi: vì sao bộ xử lý ở một trăm phần trăm không có nghĩa là
treo máy, vì sao máy thường không chậm mà là đến muộn, vì sao nút thắt
đôi khi là bộ nhớ chứ không phải bộ xử lý, và vì sao một ứng dụng có thể
bạc đi và thôi trả lời trong khi hệ thống quanh nó vẫn sống nguyên vẹn.

Toàn văn, nguồn và bản dịch: https://theresmoretoit-channel.github.io/vi/videos/why-does-your-computer-ignore-you-when-its-busy/

Các phần:
0:00 Bấm. Không có gì xảy ra.
1:18 Ngắt thật ra là gì
2:11 Trình xử lý làm ít nhất có thể
2:52 Câu trả lời đầu tiên: chú ý không phải là bộ xử lý
3:04 Vậy cho đầu vào ưu tiên cao nhất
3:26 Sao Hỏa, 1997
4:15 Đảo ngược ưu tiên
4:37 Ưu tiên cao không có nghĩa là bạn được phục vụ
4:53 Ưu tiên không tạo ra chu kỳ nào
5:28 Không chậm. Muộn.
5:50 Khi vấn đề không nằm ở bộ xử lý
6:33 Ứng dụng không chịu trả lời
7:31 Và chưa có gì lên tới màn hình
8:03 Nó không hề biết vì sao bạn di chuột
8:37 Cú bấm của bạn chưa từng là một sự kiện

Phụ đề được viết riêng cho video này, không phải do máy tự tạo. Có một bản âm thanh tiếng Anh Mỹ dưới dạng bản âm thanh thứ hai.

NGUỒN HÌNH ẢNH
Mars Pathfinder Presidential Panorama — NASA, phạm vi công cộng
Pathfinder on Mars (PIA01120) — NASA/JPL, phạm vi công cộng
Mars Pathfinder Rover Team — NASA/JPL-Caltech, phạm vi công cộng

Toàn bộ hình ảnh còn lại được vẽ từ tệp nguồn của chính dự án.
```

## čeština (`cs`)

```
Proč tě počítač ignoruje, když má práci?
```

```
Klikneš na tlačítko. Nic se nestane. Klikneš znovu. Pořád nic. A pak,
o pět sekund později, dorazí všechno najednou.

A teď to divné: počítač o tom věděl. Věděl to během mikrosekund. Zrovna
teď, když zrovna nedělá nic zvláštního, zpracovává tvoje mašina tisíce
hardwarových událostí za sekundu — a mechanismus, který to umožňuje, tu
je už od padesátých let.

Tak proč to kliknutí leží?

Tohle video je o rozdílu mezi tím, že si tě někdo všimne, a tím, že tě
obslouží. Přerušení získá pozornost počítače, ale nedostane tvůj program
na procesor — a zjevná oprava, dát vstupu nejvyšší prioritu, selže
způsobem, který kdysi restartoval sondu na Marsu.

Cestou: proč procesor na sto procentech neznamená zaseknuto, proč
počítač často není pomalý, ale přichází pozdě, proč je úzkým hrdlem
někdy paměť místo procesoru, a proč může aplikace zešednout a přestat
odpovídat, zatímco systém kolem ní je úplně živý.

Celý text, zdroje a překlady: https://theresmoretoit-channel.github.io/cs/videos/why-does-your-computer-ignore-you-when-its-busy/

Kapitoly:
0:00 Klik. Nic se nestane.
1:18 Co je vlastně přerušení
2:11 Obsluha dělá co nejmíň
2:52 První odpověď: pozornost není procesor
3:04 Tak dej vstupu nejvyšší prioritu
3:26 Mars, 1997
4:15 Inverze priorit
4:37 Vysoká priorita neznamená, že tě obslouží
4:53 Priorita nevyrobí ani takt navíc
5:28 Ne pomalý. Pozdě.
5:50 Když problém není procesor
6:33 Aplikace, která neodpovídá
7:31 A na obrazovku se zatím nedostalo nic
8:03 Nemá tušení, proč jsi hnul myší
8:37 Tvoje kliknutí nikdy nebylo jednou událostí

Titulky jsou k tomuhle videu napsané, ne vygenerované automaticky. Jako druhá zvuková stopa je k dispozici stopa v americké angličtině.

ZDROJE OBRÁZKŮ
Mars Pathfinder Presidential Panorama — NASA, volné dílo
Pathfinder on Mars (PIA01120) — NASA/JPL, volné dílo
Mars Pathfinder Rover Team — NASA/JPL-Caltech, volné dílo

Všechno ostatní je nakreslené z vlastních zdrojů projektu.
```

## español (`es`)

```
¿Por qué tu ordenador te ignora cuando está ocupado?
```

```
Haces clic en un botón. No pasa nada. Vuelves a hacer clic. Sigue sin
pasar nada. Y entonces, cinco segundos después, todo llega de golpe.

Y aquí está lo raro: el ordenador lo sabía. Lo supo en microsegundos.
Ahora mismo, sin hacer nada en particular, tu máquina está atendiendo
miles de eventos de hardware por segundo, y el mecanismo que lo hace
posible está ahí desde los años cincuenta.

Entonces, ¿por qué el clic se queda ahí parado?

Este vídeo va de la distancia que hay entre ser visto y ser atendido.
Una interrupción consigue la atención del ordenador, pero no pone tu
programa en un procesador — y el arreglo evidente, dar a la entrada la
prioridad más alta, falla de una manera que una vez reinició una sonda
en Marte una y otra vez.

Por el camino: por qué un procesador al cien por cien no significa
colgado, por qué la máquina muchas veces no es lenta sino que llega
tarde, por qué el cuello de botella a veces es la memoria y no el
procesador, y por qué una aplicación puede atenuarse y dejar de
responder mientras el sistema a su alrededor está perfectamente vivo.

Transcripción completa, fuentes y traducciones: https://theresmoretoit-channel.github.io/es/videos/why-does-your-computer-ignore-you-when-its-busy/

Capítulos:
0:00 Clic. No pasa nada.
1:18 Qué es realmente una interrupción
2:11 El manejador hace lo menos posible
2:52 Primera respuesta: la atención no es un procesador
3:04 Pues demos a la entrada la prioridad más alta
3:26 Marte, 1997
4:15 Inversión de prioridad
4:37 Prioridad alta no significa que te atiendan
4:53 La prioridad no crea ciclos
5:28 No lento. Tarde.
5:50 Cuando el problema no es el procesador
6:33 La aplicación que no responde
7:31 Y a la pantalla todavía no ha llegado nada
8:03 No tiene ni idea de por qué moviste el ratón
8:37 Tu clic nunca fue un solo evento

Los subtítulos están escritos para este vídeo, no generados
automáticamente. Hay una pista de audio en inglés americano disponible como segunda pista.

CRÉDITOS DE IMAGEN
Mars Pathfinder Presidential Panorama — NASA, dominio público
Pathfinder on Mars (PIA01120) — NASA/JPL, dominio público
Mars Pathfinder Rover Team — NASA/JPL-Caltech, dominio público

Todas las demás imágenes salen de los archivos fuente del propio
proyecto.
```

## svenska (`sv`)

```
Varför ignorerar datorn dig när den har fullt upp?
```

```
Du klickar på en knapp. Ingenting händer. Du klickar igen. Fortfarande
ingenting. Och sedan, fem sekunder senare, kommer allt på en gång.

Och här är det märkliga: datorn visste. Den visste inom mikrosekunder.
Just nu, utan att göra något särskilt, hanterar din maskin tusentals
hårdvaruhändelser varje sekund, och mekanismen som gör det möjligt har
funnits sedan femtiotalet.

Så varför blir klicket liggande?

Den här filmen handlar om glappet mellan att bli uppmärksammad och att
bli betjänad. Ett avbrott får datorns uppmärksamhet, men det lägger inte
ditt program på en processor — och den självklara lösningen, att ge
inmatningen högsta prioritet, misslyckas på ett sätt som en gång
startade om en sond på Mars gång på gång.

På vägen: varför en processor på hundra procent inte betyder att det har
hängt sig, varför maskinen ofta inte är långsam utan sen, varför
flaskhalsen ibland är minnet och inte processorn, och varför ett program
kan blekna och sluta svara medan systemet runt omkring det är fullt
levande.

Hela texten, källor och översättningar: https://theresmoretoit-channel.github.io/sv/videos/why-does-your-computer-ignore-you-when-its-busy/

Kapitel:
0:00 Klick. Ingenting händer.
1:18 Vad ett avbrott faktiskt är
2:11 Hanteraren gör så lite som möjligt
2:52 Första svaret: uppmärksamhet är ingen processor
3:04 Ge då inmatningen högsta prioritet
3:26 Mars, 1997
4:15 Prioritetsinversion
4:37 Hög prioritet betyder inte att du blir betjänad
4:53 Prioritet skapar inga cykler
5:28 Inte långsam. Sen.
5:50 När processorn inte är problemet
6:33 Programmet som inte svarar
7:31 Och ännu har ingenting nått skärmen
8:03 Den har ingen aning om varför du rörde musen
8:37 Ditt klick var aldrig en enda händelse

Undertexterna är skrivna för den här filmen, inte automatgenererade. Ett amerikanskt engelskt ljudspår finns som andra ljudspår.

BILDKÄLLOR
Mars Pathfinder Presidential Panorama — NASA, public domain
Pathfinder on Mars (PIA01120) — NASA/JPL, public domain
Mars Pathfinder Rover Team — NASA/JPL-Caltech, public domain

Allt annat bildmaterial är ritat ur projektets egna källfiler.
```
