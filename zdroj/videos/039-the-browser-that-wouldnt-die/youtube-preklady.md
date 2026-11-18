# Lokalizované názvy a popisy — Internet Explorer 6: The Browser That Wouldn't Die

Podklad pro **YouTube Studio → video → Podrobnosti → Přidat jazyk**.
Pro každý jazyk jsou tu **dva bloky ke zkopírování**: název a popis.
Kopíruje se **celý blok mezi trojicí zpětných apostrofů**, co je mimo něj,
je poznámka. Anglický originál zůstává v `youtube.md` a nesahá se na něj.

Nahrává je `tools/lokalizace.py`, který čte právě tenhle formát.

## Co se NEPŘEKLÁDÁ

| | |
|---|---|
| **vlastní jména** | Internet Explorer, Windows XP, Windows 7, Windows Update, Microsoft, Google, Firefox, Chrome, ActiveX, Microsoft Edge |
| **Operation Aurora** | krycí jméno útoku, ne popis — překladem se ztratí, že to je jméno |
| **Blocker Toolkit, Microsoft Enterprise Desktop Virtualization** | názvy produktů |
| **časy kapitol** | musí sedět na vteřinu, jinak je YouTube neuzná |
| **tagy** | YouTube je per-jazyk nemá |
| **odkazy na předchozí díly** | `https://youtu.be/R7Un3IOMvbg` a `https://youtu.be/1dIM5UZUEZg` |

Názvy kapitol se naopak **překládají** — divák je čte v seznamu pod videem.

## Kontrola čísel

V popisu jsou čtyři: **6** v názvu prohlížeče, **7 a 8** u verzí, které
běžely na XP, **2010** jako rok a **pět a půl milionu liber**. Musí být
v každém překladu a nesmí se změnit. Kapitol je **dvacet**.

> **Obrazové zdroje tu nejsou a chybět nemají.** Tohle video nemá ani jeden
> archivní snímek (95 diagramů kreslených kódem a 2 malované SDXL scény),
> takže `sources.json` neexistuje a atribuovat není co.

---

## suomi (`fi`)

```
Internet Explorer 6 — selain, joka ei suostunut kuolemaan
```

```
Microsoft kehotti vuosikausia lopettamaan Internet Explorer 6:n käytön. Sen omalla sivustolla oli laskuri, prosentti prosentilta, maa maalta. Ja vuonna 2010 se oli yhä käynnissä miljoonilla koneilla.

Ei siksi, että kukaan olisi pitänyt siitä. Vaan siksi, että jokin ihmisten tarvitsema riippui siitä.

Tämä on osa kolme, ja se esittää vaikeamman kysymyksen: mitä tapahtuu, kun vanhentuneesta ohjelmistosta tulee infrastruktuuria? Vastaus ei ole Windows XP — Internet Explorer 7 ja 8 toimivat molemmat XP:llä, joten käyttöjärjestelmä ei koskaan ollut se, mikä noita koneita piti paikallaan. Se oli yksi sisäinen sovellus, jota kukaan ei enää täysin ymmärtänyt.

Matkan varrella: hyökkäys, joka murtautui Googleen Internet Explorerin tietoturva-aukon kautta; kaksi hallitusta, jotka kehottivat kansalaisiaan vaihtamaan selainta; työkalu, jonka Microsoft julkaisi estääkseen oman uuden selaimensa (neljä kertaa); tuote, jota se myi ja joka ajoi Windows 7:n sisällä piilotettua kopiota Windows XP:stä vain pitääkseen vanhan selaimen hengissä; maa, jonka pankkisäädökset sitoivat sen yhteen toimittajaan; ja viisi ja puoli miljoonaa puntaa, jotka maksettiin yhdestä lisävuodesta ilman päivitystä.

Osa yksi — kuinka Internet Explorer 6:sta tuli alusta:
https://youtu.be/R7Un3IOMvbg

Osa kaksi — virheet, joilla oli nimet:
https://youtu.be/1dIM5UZUEZg

Koko teksti, lähteet ja käännökset: https://theresmoretoit-channel.github.io/fi/videos/the-browser-that-wouldnt-die/

Luvut
00:00 Osa kolme
01:19 Tammikuu 2010
01:33 Joku Googlen sisällä
02:02 Operaatio Aurora
02:36 Google lakkaa odottamasta
03:04 Tavallinen selitys on väärä
04:06 Käyttöjärjestelmä ei ollut syy
04:20 Mikä se sovellus oli
05:13 Työkalu oman selaimen estämiseen
06:01 Kun itse kone kuolee
06:44 Windows XP Windows 7:n sisällä
07:26 Tapetaan ja myydään
07:59 Pelkkä asetus uudessa
08:39 Etelä-Korea
09:40 Kiina ja Amerikka
10:11 Kahdeksansataatuhatta konetta
11:22 Miten se todella päättyi
12:24 Sammutettiin 2022
12:53 Selain, alusta, riippuvuus
13:39 Kun maailma ei enää riippunut siitä

Tekstitykset on kirjoitettu tätä videota varten, ei luotu automaattisesti. Toisena ääniraitana on amerikanenglanti.
```

## français (`fr`)

Název:

```
Internet Explorer 6 — Le navigateur qui refusait de mourir
```

Popis:

```
Pendant des années, Microsoft a dit aux gens d'arrêter d'utiliser
Internet Explorer 6. Sur son propre site tournait un compte à rebours,
point de pourcentage après point, pays après pays. Et en 2010 il tournait
encore sur des millions de machines.

Pas parce que quelqu'un l'aimait. Mais parce que quelque chose dont les
gens avaient besoin en dépendait.

Voici la troisième partie, et elle pose la question difficile : que se
passe-t-il quand un logiciel obsolète devient une infrastructure ? La
réponse n'est pas Windows XP — Internet Explorer 7 et 8 tournaient tous
les deux sur XP, le système d'exploitation n'a donc jamais retenu ces
machines. C'était une application interne que plus personne ne comprenait
entièrement.

En chemin : l'attaque qui est entrée chez Google par une faille
d'Internet Explorer, deux gouvernements disant à leurs citoyens de
changer de navigateur, l'outil que Microsoft a publié pour bloquer son
propre nouveau navigateur (quatre fois), le produit qu'il vendait et qui
faisait tourner une copie cachée de Windows XP dans Windows 7 juste pour
garder l'ancien navigateur en vie, un pays que sa réglementation bancaire
a lié à un seul fournisseur, et cinq millions et demi de livres payés
pour une année de plus sans mise à jour.

Première partie — comment Internet Explorer 6 est devenu une plateforme :
https://youtu.be/R7Un3IOMvbg

Deuxième partie — les bugs qui avaient des noms :
https://youtu.be/1dIM5UZUEZg

Transcription complète, sources et traductions : https://theresmoretoit-channel.github.io/fr/videos/the-browser-that-wouldnt-die/

Chapitres
00:00 Troisième partie
01:19 Janvier 2010
01:33 Quelqu'un chez Google
02:02 Operation Aurora
02:36 Google cesse d'attendre
03:04 L'explication habituelle est fausse
04:06 Ce n'était pas le système d'exploitation
04:20 Quelle était cette application
05:13 Un outil contre son propre navigateur
06:01 Quand la machine elle-même meurt
06:44 Windows XP dans Windows 7
07:26 Le tuer et le vendre à la fois
07:59 Juste un réglage dans le nouveau
08:39 Corée du Sud
09:40 La Chine et l'Amérique
10:11 Huit cent mille machines
11:22 Comment cela s'est vraiment terminé
12:24 Éteint en 2022
12:53 Navigateur, plateforme, dépendance
13:39 Quand le monde a cessé d'en dépendre

Les sous-titres sont écrits pour cette vidéo, pas générés automatiquement. Une piste audio en anglais américain est disponible en seconde piste.
```

## Bahasa Indonesia (`id`)

```
Internet Explorer 6 — Browser yang Tak Mau Mati
```

```
Microsoft bertahun-tahun menyuruh orang berhenti memakai Internet Explorer 6. Di situsnya sendiri ada hitung mundur, persen demi persen, negara demi negara. Dan pada 2010 jutaan mesin masih menjalankannya.

Bukan karena ada yang menyukainya. Tapi karena sesuatu yang mereka butuhkan bergantung padanya.

Bagian ketiga ini mengangkat pertanyaan yang lebih sulit: apa yang terjadi ketika perangkat lunak usang menjadi infrastruktur? Jawabannya bukan Windows XP — Internet Explorer 7 dan 8 sama-sama berjalan di XP, jadi sistem operasi tidak pernah menjadi hal yang menahan mesin-mesin itu. Yang menahan adalah satu aplikasi internal yang tidak ada lagi orang yang benar-benar memahaminya.

Video ini juga membahas: serangan yang menembus Google melalui celah keamanan di Internet Explorer; dua pemerintah yang menyuruh warganya berganti browser; alat yang diterbitkan Microsoft untuk memblokir browser barunya sendiri (empat kali); produk yang dijualnya dan menjalankan salinan tersembunyi Windows XP di dalam Windows 7 hanya demi menjaga browser lama tetap hidup; sebuah negara yang regulasi perbankannya mengunci dirinya pada satu vendor; dan lima setengah juta pound yang dibayarkan demi satu tahun lagi tanpa pembaruan.

Bagian satu — bagaimana Internet Explorer 6 menjadi sebuah platform:
https://youtu.be/R7Un3IOMvbg

Bagian dua — bug-bug yang punya nama:
https://youtu.be/1dIM5UZUEZg

Transkrip lengkap, sumber, dan terjemahan: https://theresmoretoit-channel.github.io/id/videos/the-browser-that-wouldnt-die/

Bab
00:00 Bagian tiga
01:19 Januari 2010
01:33 Seseorang di dalam Google
02:02 Operasi Aurora
02:36 Google berhenti menunggu
03:04 Penjelasan yang biasa itu keliru
04:06 Sistem operasinya bukan alasannya
04:20 Aplikasi apa itu?
05:13 Alat untuk memblokir browser sendiri
06:01 Ketika mesinnya sendiri mati
06:44 Windows XP di dalam Windows 7
07:26 Membunuhnya sekaligus menjualnya
07:59 Pengaturan di browser baru
08:39 Korea Selatan
09:40 Tiongkok dan Amerika
10:11 Delapan ratus ribu mesin
11:22 Bagaimana sebenarnya itu berakhir
12:24 Dimatikan pada 2022
12:53 Browser, platform, ketergantungan
13:39 Ketika dunia berhenti bergantung

Subtitel ditulis khusus untuk video ini, bukan dibuat secara otomatis. Tersedia juga trek audio kedua dalam bahasa Inggris Amerika.
```

## italiano (`it`)

Název:

```
Internet Explorer 6 — Il browser che non voleva morire
```

Popis:

```
Per anni Microsoft ha detto alla gente di smettere di usare Internet
Explorer 6. Sul suo stesso sito scorreva un conto alla rovescia, punto
percentuale dopo punto, paese dopo paese. E nel 2010 girava ancora su
milioni di macchine.

Non perché piacesse a qualcuno. Ma perché qualcosa che serviva alle
persone ne dipendeva.

Questa è la terza parte e pone la domanda più difficile: cosa succede
quando un software obsoleto diventa infrastruttura? La risposta non è
Windows XP — Internet Explorer 7 e 8 giravano entrambi su XP, quindi il
sistema operativo non ha mai trattenuto quelle macchine. Le tratteneva
un'applicazione interna che nessuno capiva più fino in fondo.

Lungo la strada: l'attacco che è entrato in Google da un buco di Internet
Explorer, due governi che hanno detto ai cittadini di cambiare browser,
lo strumento che Microsoft ha pubblicato per bloccare il proprio nuovo
browser (quattro volte), il prodotto che vendeva e che eseguiva una copia
nascosta di Windows XP dentro Windows 7 solo per tenere in vita il
vecchio browser, un paese legato a un unico fornitore dalle proprie norme
bancarie, e cinque milioni e mezzo di sterline pagate per un altro anno
senza aggiornare.

Prima parte — come Internet Explorer 6 è diventato una piattaforma:
https://youtu.be/R7Un3IOMvbg

Seconda parte — i bug che avevano un nome:
https://youtu.be/1dIM5UZUEZg

Trascrizione completa, fonti e traduzioni: https://theresmoretoit-channel.github.io/it/videos/the-browser-that-wouldnt-die/

Capitoli
00:00 Terza parte
01:19 Gennaio 2010
01:33 Qualcuno dentro Google
02:02 Operation Aurora
02:36 Google smette di aspettare
03:04 La spiegazione solita è sbagliata
04:06 Non era il sistema operativo
04:20 Che applicazione era
05:13 Uno strumento contro il proprio browser
06:01 Quando muore la macchina stessa
06:44 Windows XP dentro Windows 7
07:26 Ucciderlo e venderlo insieme
07:59 Solo un'impostazione in quello nuovo
08:39 Corea del Sud
09:40 Cina e America
10:11 Ottocentomila macchine
11:22 Come è finita davvero
12:24 Spento nel 2022
12:53 Browser, piattaforma, dipendenza
13:39 Quando il mondo ha smesso di dipenderne

I sottotitoli sono scritti per questo video, non generati automaticamente. Come seconda traccia audio è disponibile l’inglese americano.
```

## Deutsch (`de`)

Název:

```
Internet Explorer 6 — Der Browser, der nicht sterben wollte
```

Popis:

```
Microsoft hat jahrelang dazu aufgerufen, Internet Explorer 6 nicht mehr
zu benutzen. Auf der eigenen Website lief ein Countdown, Prozent für
Prozent, Land für Land. Und 2010 lief er immer noch auf Millionen
Rechnern.

Nicht weil ihn jemand mochte. Sondern weil etwas, das die Leute
brauchten, von ihm abhing.

Das ist Teil drei, und er stellt die schwerere Frage: Was passiert, wenn
veraltete Software zu Infrastruktur wird? Die Antwort heißt nicht Windows
XP — Internet Explorer 7 und 8 liefen beide auf XP, das Betriebssystem
hat diese Rechner also nie festgehalten. Es war eine interne Anwendung,
die niemand mehr ganz verstand.

Unterwegs: der Angriff, der über ein Loch im Internet Explorer bei Google
eindrang, zwei Regierungen, die ihren Bürgern zum Wechsel rieten, das
Werkzeug, das Microsoft veröffentlichte, um den eigenen neuen Browser zu
blockieren (viermal), das Produkt, das es verkaufte und das in Windows 7
eine versteckte Kopie von Windows XP laufen ließ, nur um den alten
Browser am Leben zu halten, ein Land, das seine Bankvorschriften an einen
einzigen Anbieter banden, und fünfeinhalb Millionen Pfund für ein
weiteres Jahr Nichtaktualisieren.

Teil eins — wie Internet Explorer 6 zur Plattform wurde:
https://youtu.be/R7Un3IOMvbg

Teil zwei — die Bugs, die Namen hatten:
https://youtu.be/1dIM5UZUEZg

Vollständiger Text, Quellen und Übersetzungen: https://theresmoretoit-channel.github.io/de/videos/the-browser-that-wouldnt-die/

Kapitel
00:00 Teil drei
01:19 Januar 2010
01:33 Jemand bei Google
02:02 Operation Aurora
02:36 Google wartet nicht mehr
03:04 Die übliche Erklärung ist falsch
04:06 Es war nicht das Betriebssystem
04:20 Was das für eine Anwendung war
05:13 Ein Werkzeug gegen den eigenen Browser
06:01 Wenn der Rechner selbst stirbt
06:44 Windows XP in Windows 7
07:26 Töten und gleichzeitig verkaufen
07:59 Nur eine Einstellung im neuen
08:39 Südkorea
09:40 China und Amerika
10:11 Achthunderttausend Rechner
11:22 Wie es wirklich endete
12:24 2022 abgeschaltet
12:53 Browser, Plattform, Abhängigkeit
13:39 Als die Welt aufhörte, abzuhängen

Die Untertitel wurden für dieses Video geschrieben, nicht automatisch erzeugt. Als zweite Tonspur steht amerikanisches Englisch bereit.
```

## polski (`pl`)

Název:

```
Internet Explorer 6 — Przeglądarka, która nie chciała umrzeć
```

Popis:

```
Microsoft latami powtarzał ludziom, żeby przestali używać Internet
Explorera 6. Na jego własnej stronie szło odliczanie, procent po
procencie, kraj po kraju. A w 2010 roku wciąż działał na milionach
komputerów.

Nie dlatego, że ktoś go lubił. Tylko dlatego, że zależało od niego coś,
czego ludzie potrzebowali.

To jest część trzecia i zadaje trudniejsze pytanie: co się dzieje, gdy
przestarzałe oprogramowanie staje się infrastrukturą? Odpowiedź nie brzmi
Windows XP — Internet Explorer 7 i 8 działały na XP, więc system
operacyjny nigdy tych komputerów nie trzymał. Trzymała je jedna
wewnętrzna aplikacja, której nikt już w pełni nie rozumiał.

Po drodze: atak, który wszedł do Google dziurą w Internet Explorerze, dwa
rządy mówiące obywatelom, żeby zmienili przeglądarkę, narzędzie, które
Microsoft wydał, żeby zablokować własną nową przeglądarkę (cztery razy),
produkt, który sprzedawał i który uruchamiał ukrytą kopię Windows XP
wewnątrz Windows 7 tylko po to, żeby stara przeglądarka żyła dalej, kraj
przywiązany do jednego dostawcy przez własne przepisy bankowe, oraz pięć
i pół miliona funtów zapłacone za kolejny rok nieaktualizowania.

Część pierwsza — jak Internet Explorer 6 stał się platformą:
https://youtu.be/R7Un3IOMvbg

Część druga — błędy, które miały imiona:
https://youtu.be/1dIM5UZUEZg

Pełna transkrypcja, źródła i tłumaczenia: https://theresmoretoit-channel.github.io/pl/videos/the-browser-that-wouldnt-die/

Rozdziały
00:00 Część trzecia
01:19 Styczeń 2010
01:33 Ktoś wewnątrz Google
02:02 Operation Aurora
02:36 Google przestaje czekać
03:04 Zwykłe wyjaśnienie jest błędne
04:06 To nie był system operacyjny
04:20 Co to była za aplikacja
05:13 Narzędzie przeciw własnej przeglądarce
06:01 Gdy umiera sam komputer
06:44 Windows XP wewnątrz Windows 7
07:26 Zabijać i sprzedawać naraz
07:59 Tylko ustawienie w nowej
08:39 Korea Południowa
09:40 Chiny i Ameryka
10:11 Osiemset tysięcy komputerów
11:22 Jak to się naprawdę skończyło
12:24 Wyłączony w 2022
12:53 Przeglądarka, platforma, zależność
13:39 Gdy świat przestał od niej zależeć

Napisy są pisane do tego filmu, nie generowane automatycznie. Jako druga ścieżka dźwiękowa dostępny jest angielski amerykański.
```

## português (Brasil) (`pt-BR`)

Název:

```
Internet Explorer 6 — O navegador que não queria morrer
```

Popis:

```
A Microsoft passou anos dizendo às pessoas para pararem de usar o
Internet Explorer 6. No próprio site dela rodava uma contagem regressiva,
ponto percentual a ponto, país por país. E em 2010 ele ainda rodava em
milhões de máquinas.

Não porque alguém gostasse dele. Mas porque algo de que as pessoas
precisavam dependia dele.

Esta é a terceira parte e faz a pergunta mais difícil: o que acontece
quando um software obsoleto vira infraestrutura? A resposta não é o
Windows XP — o Internet Explorer 7 e o 8 rodavam no XP, então o sistema
operacional nunca prendeu aquelas máquinas. Quem prendia era uma
aplicação interna que ninguém mais entendia por completo.

Pelo caminho: o ataque que entrou no Google por um buraco do Internet
Explorer, dois governos dizendo aos cidadãos para trocar de navegador, a
ferramenta que a Microsoft publicou para bloquear o próprio navegador
novo (quatro vezes), o produto que ela vendia e que rodava uma cópia
escondida do Windows XP dentro do Windows 7 só para manter o navegador
velho vivo, um país amarrado a um único fornecedor pelas próprias regras
bancárias, e cinco milhões e meio de libras pagos por mais um ano sem
atualizar.

Primeira parte — como o Internet Explorer 6 virou plataforma:
https://youtu.be/R7Un3IOMvbg

Segunda parte — os bugs que tinham nome:
https://youtu.be/1dIM5UZUEZg

Transcrição completa, fontes e traduções: https://theresmoretoit-channel.github.io/pt-br/videos/the-browser-that-wouldnt-die/

Capítulos
00:00 Terceira parte
01:19 Janeiro de 2010
01:33 Alguém dentro do Google
02:02 Operation Aurora
02:36 O Google para de esperar
03:04 A explicação de sempre está errada
04:06 Não era o sistema operacional
04:20 Que aplicação era aquela
05:13 Uma ferramenta contra o próprio navegador
06:01 Quando a própria máquina morre
06:44 Windows XP dentro do Windows 7
07:26 Matar e vender ao mesmo tempo
07:59 Só uma configuração no novo
08:39 Coreia do Sul
09:40 China e Estados Unidos
10:11 Oitocentas mil máquinas
11:22 Como acabou de verdade
12:24 Desligado em 2022
12:53 Navegador, plataforma, dependência
13:39 Quando o mundo parou de depender

As legendas foram escritas para este vídeo, não geradas automaticamente. Como segunda faixa de áudio está disponível o inglês americano.
```

## Türkçe (`tr`)

```
Internet Explorer 6 — Bir Türlü Ölmeyen Tarayıcı
```

```
Microsoft yıllarca insanlara Internet Explorer 6’yı bırakmalarını söyledi. Kendi sitesinde bir geri sayım vardı; yüzde birer birer azalarak, ülke ülke. Ve 2010’da hâlâ milyonlarca makinede çalışıyordu.

Kimse onu sevdiği için değil. İhtiyaç duydukları bir şey ona bağlı olduğu için.

Bu üçüncü bölüm ve daha zor soruyu soruyor: eskimiş yazılım altyapıya dönüştüğünde ne olur? Cevap Windows XP değil — Internet Explorer 7 de 8 de XP’de çalışıyordu, yani o makineleri geride tutan hiçbir zaman işletim sistemi olmadı. Kimsenin artık tam olarak anlamadığı tek bir kurum içi uygulamaydı.

Bu bölümde ayrıca: Internet Explorer’daki bir güvenlik açığından Google’a sızan saldırı; vatandaşlarına tarayıcı değiştirmelerini söyleyen iki hükümet; Microsoft’un kendi yeni tarayıcısını engellemek için yayımladığı araç (dört kez); eski tarayıcıyı hayatta tutmak uğruna Windows 7 içinde gizli bir Windows XP kopyası çalıştıran ve satılan ürün; bankacılık düzenlemelerinin tek bir sağlayıcıya bağımlı kıldığı bir ülke; ve yükseltmemek için bir yıl daha ödenen beş buçuk milyon sterlin.

Birinci bölüm — Internet Explorer 6 nasıl bir platforma dönüştü:
https://youtu.be/R7Un3IOMvbg

İkinci bölüm — adı olan hatalar:
https://youtu.be/1dIM5UZUEZg

Metnin tamamı, kaynaklar ve çeviriler: https://theresmoretoit-channel.github.io/tr/videos/the-browser-that-wouldnt-die/

Bölümler
00:00 Üçüncü bölüm
01:19 Ocak 2010
01:33 Google’ın içinden biri
02:02 Aurora Operasyonu
02:36 Google beklemeyi bırakıyor
03:04 Alışıldık açıklama yanlış
04:06 Sebep işletim sistemi değildi
04:20 O uygulama neydi
05:13 Kendi tarayıcısını engelleyen araç
06:01 Makinenin kendisi öldüğünde
06:44 Windows 7 içinde Windows XP
07:26 Hem öldürüp hem satmak
07:59 Yenisinin içinde bir ayar
08:39 Güney Kore
09:40 Çin ve Amerika
10:11 Sekiz yüz bin makine
11:22 Aslında nasıl bitti
12:24 2022’de kapatıldı
12:53 Tarayıcı, platform, bağımlılık
13:39 Dünya bağımlı olmaktan çıkınca

Altyazılar bu video için yazıldı, otomatik olarak oluşturulmadı. İkinci ses parçası olarak Amerikan İngilizcesi de mevcut.
```

## українська (`uk`)

```
Internet Explorer 6 — браузер, який не хотів помирати
```

```
Microsoft роками закликала перестати користуватися Internet Explorer 6. На її власному сайті йшов зворотний відлік — відсоток за відсотком, країна за країною. А у 2010 році він досі працював на мільйонах машин.

Не тому, що він комусь подобався. А тому, що від нього залежало щось, чого люди потребували.

Це третя частина, і вона ставить складніше запитання: що стається, коли застаріле програмне забезпечення перетворюється на інфраструктуру? Відповідь — не Windows XP. Internet Explorer 7 і 8 обидва працювали на XP, тож операційна система ніколи не була тим, що заважало оновити ці комп’ютери. Це був один внутрішній застосунок, якого вже ніхто до кінця не розумів.

Також у відео: атака, що пробралася до Google через дірку в Internet Explorer; два уряди, які радили своїм громадянам змінити браузер; інструмент, який Microsoft опублікувала, щоб заблокувати власний новий браузер (чотири рази); продукт, який вона продавала і який запускав приховану копію Windows XP усередині Windows 7, аби лиш утримати старий браузер при житті; країна, чиї банківські правила прив’язали її до єдиного постачальника; і п’ять з половиною мільйонів фунтів, заплачених за ще один рік без оновлення.

Частина перша — як Internet Explorer 6 став платформою:
https://youtu.be/R7Un3IOMvbg

Частина друга — помилки, які мали імена:
https://youtu.be/1dIM5UZUEZg

Повний текст, джерела та переклади: https://theresmoretoit-channel.github.io/uk/videos/the-browser-that-wouldnt-die/

Розділи
00:00 Частина третя
01:19 Січень 2010
01:33 Хтось усередині Google
02:02 Операція «Аврора»
02:36 Google перестає чекати
03:04 Звичне пояснення хибне
04:06 Річ була не в операційній системі
04:20 Що це був за застосунок
05:13 Інструмент проти власного браузера
06:01 Коли вмирає сама машина
06:44 Windows XP усередині Windows 7
07:26 Убивати й продавати водночас
07:59 Просто налаштування в новому
08:39 Південна Корея
09:40 Китай і Америка
10:11 Вісімсот тисяч машин
11:22 Як це скінчилося насправді
12:24 Вимкнено у 2022-му
12:53 Браузер, платформа, залежність
13:39 Коли світ перестав від нього залежати

Субтитри написані для цього відео, а не згенеровані автоматично. Також доступна друга звукова доріжка — американською англійською.
```

## Tiếng Việt (`vi`)

```
Internet Explorer 6 — Trình duyệt không chịu chết
```

```
Trong nhiều năm, Microsoft đã kêu gọi mọi người ngừng dùng Internet Explorer 6. Trên chính website của họ có một bộ đếm ngược, từng phần trăm một, từng nước một. Vậy mà năm 2010 hàng triệu máy vẫn đang chạy nó.

Không phải vì có ai thích nó. Mà vì thứ họ cần lại phụ thuộc vào nó.

Đây là phần ba, và nó đặt ra câu hỏi khó hơn: chuyện gì xảy ra khi phần mềm lỗi thời trở thành hạ tầng? Câu trả lời không phải Windows XP — Internet Explorer 7 và 8 đều chạy được trên XP, nên hệ điều hành chưa bao giờ là thứ giữ chân những cỗ máy ấy. Đó là một ứng dụng nội bộ mà không còn ai hiểu trọn vẹn nữa.

Video cũng đề cập đến: vụ tấn công đột nhập vào Google qua một lỗ hổng trong Internet Explorer; hai chính phủ khuyên công dân đổi trình duyệt; công cụ Microsoft phát hành để chặn chính trình duyệt mới của mình (bốn lần); sản phẩm họ bán ra, chạy một bản Windows XP ẩn bên trong Windows 7 chỉ để giữ trình duyệt cũ sống sót; một quốc gia có quy định ngân hàng khóa chặt mình vào một nhà cung cấp duy nhất; và năm triệu rưỡi bảng Anh trả cho thêm một năm không nâng cấp.

Phần một — Internet Explorer 6 đã trở thành một nền tảng như thế nào:
https://youtu.be/R7Un3IOMvbg

Phần hai — những lỗi có tên riêng:
https://youtu.be/1dIM5UZUEZg

Toàn văn, nguồn và bản dịch: https://theresmoretoit-channel.github.io/vi/videos/the-browser-that-wouldnt-die/

Các chương
00:00 Phần ba
01:19 Tháng 1 năm 2010
01:33 Ai đó bên trong Google
02:02 Chiến dịch Aurora
02:36 Google thôi chờ đợi
03:04 Lời giải thích quen thuộc là sai
04:06 Hệ điều hành không phải lý do
04:20 Ứng dụng đó là gì
05:13 Công cụ chặn chính trình duyệt của mình
06:01 Khi chính cỗ máy chết đi
06:44 Windows XP bên trong Windows 7
07:26 Vừa khai tử vừa bán
07:59 Chỉ là một thiết lập trong bản mới
08:39 Hàn Quốc
09:40 Trung Quốc và Mỹ
10:11 Tám trăm nghìn máy
11:22 Nó thực sự kết thúc thế nào
12:24 Tắt hẳn năm 2022
12:53 Trình duyệt, nền tảng, sự phụ thuộc
13:39 Khi thế giới thôi phụ thuộc

Phụ đề được viết riêng cho video này, không phải tạo tự động. Có thể chọn tiếng Anh Mỹ ở bản âm thanh thứ hai.
```

## čeština (`cs`)

Název:

```
Internet Explorer 6 — Prohlížeč, který nechtěl umřít
```

Popis:

```
Microsoft roky opakoval lidem, ať přestanou používat Internet Explorer 6.
Na jeho vlastním webu běžel odpočet, procento po procentu, zemi po zemi.
A v roce 2010 na milionech strojů pořád běžel.

Ne že by ho měl někdo rád. Ale záviselo na něm něco, co lidé potřebovali.

Tohle je třetí díl a ptá se na těžší otázku: co se stane, když se
zastaralý software stane infrastrukturou? Odpověď nezní Windows XP —
Internet Explorer 7 i 8 na XP běžely, takže operační systém ty stroje
nikdy nedržel. Držela je jedna interní aplikace, které už nikdo úplně
nerozuměl.

Cestou: útok, který se do Googlu dostal dírou v Internet Exploreru, dvě
vlády, které svým občanům řekly, ať přejdou jinam, nástroj, který
Microsoft vydal, aby zablokoval vlastní nový prohlížeč (čtyřikrát),
produkt, který prodával a který uvnitř Windows 7 spouštěl skrytou kopii
Windows XP jen proto, aby starý prohlížeč zůstal naživu, země, kterou
k jedinému dodavateli přikovaly bankovní předpisy, a pět a půl milionu
liber zaplacených za další rok neupgradování.

První díl — jak se z Internet Exploreru 6 stala platforma:
https://youtu.be/R7Un3IOMvbg

Druhý díl — chyby, které měly jména:
https://youtu.be/1dIM5UZUEZg

Celý text, zdroje a překlady: https://theresmoretoit-channel.github.io/cs/videos/the-browser-that-wouldnt-die/

Kapitoly
00:00 Třetí díl
01:19 Leden 2010
01:33 Někdo uvnitř Googlu
02:02 Operation Aurora
02:36 Google přestal čekat
03:04 Obvyklé vysvětlení je špatně
04:06 Nebyl to operační systém
04:20 Co to bylo za aplikaci
05:13 Nástroj proti vlastnímu prohlížeči
06:01 Když umře sám ten stroj
06:44 Windows XP uvnitř Windows 7
07:26 Zabíjet ho a prodávat zároveň
07:59 Jen nastavení v tom novém
08:39 Jižní Korea
09:40 Čína a Amerika
10:11 Osm set tisíc strojů
11:22 Jak to doopravdy skončilo
12:24 Vypnutý v roce 2022
12:53 Prohlížeč, platforma, závislost
13:39 Když na něm svět přestal záviset

Titulky jsou psané pro tohle video, ne strojový přepis. Jako druhá zvuková stopa je k dispozici americká angličtina.
```

## español (`es`)

Název:

```
Internet Explorer 6 — El navegador que no quería morir
```

Popis:

```
Microsoft pasó años diciéndole a la gente que dejara de usar Internet
Explorer 6. En su propia web corría una cuenta atrás, punto porcentual a
punto, país por país. Y en 2010 seguía funcionando en millones de
máquinas.

No porque le gustara a nadie. Sino porque algo que la gente necesitaba
dependía de él.

Esta es la tercera parte y hace la pregunta difícil: ¿qué pasa cuando un
software obsoleto se convierte en infraestructura? La respuesta no es
Windows XP: Internet Explorer 7 y 8 funcionaban en XP, así que el sistema
operativo nunca retuvo esas máquinas. Las retenía una aplicación interna
que ya nadie entendía del todo.

Por el camino: el ataque que entró en Google por un agujero de Internet
Explorer, dos gobiernos diciéndoles a sus ciudadanos que cambiaran de
navegador, la herramienta que Microsoft publicó para bloquear su propio
navegador nuevo (cuatro veces), el producto que vendía y que ejecutaba
una copia oculta de Windows XP dentro de Windows 7 solo para mantener
vivo el navegador viejo, un país al que sus normas bancarias ataron a un
único proveedor, y cinco millones y medio de libras pagados por un año
más sin actualizar.

Primera parte — cómo Internet Explorer 6 se convirtió en plataforma:
https://youtu.be/R7Un3IOMvbg

Segunda parte — los fallos que tenían nombre:
https://youtu.be/1dIM5UZUEZg

Transcripción completa, fuentes y traducciones: https://theresmoretoit-channel.github.io/es/videos/the-browser-that-wouldnt-die/

Capítulos
00:00 Tercera parte
01:19 Enero de 2010
01:33 Alguien dentro de Google
02:02 Operation Aurora
02:36 Google deja de esperar
03:04 La explicación habitual es falsa
04:06 No era el sistema operativo
04:20 Qué aplicación era aquella
05:13 Una herramienta contra su propio navegador
06:01 Cuando muere la propia máquina
06:44 Windows XP dentro de Windows 7
07:26 Matarlo y venderlo a la vez
07:59 Solo un ajuste dentro del nuevo
08:39 Corea del Sur
09:40 China y Estados Unidos
10:11 Ochocientas mil máquinas
11:22 Cómo acabó de verdad
12:24 Apagado en 2022
12:53 Navegador, plataforma, dependencia
13:39 Cuando el mundo dejó de depender

Los subtítulos están escritos para este vídeo, no generados automáticamente. Como segunda pista de audio está disponible el inglés americano.
```

## svenska (`sv`)

Název:

```
Internet Explorer 6 — Webbläsaren som inte ville dö
```

Popis:

```
Microsoft ägnade år åt att säga till folk att sluta använda Internet
Explorer 6. På deras egen webbplats gick en nedräkning, procent för
procent, land för land. Och 2010 kördes den fortfarande på miljontals
datorer.

Inte för att någon gillade den. Utan för att något som folk behövde
berodde på den.

Det här är del tre, och den ställer den svårare frågan: vad händer när
föråldrad programvara blir infrastruktur? Svaret är inte Windows XP —
Internet Explorer 7 och 8 körde båda på XP, så operativsystemet höll
aldrig kvar de där datorerna. Det gjorde en intern applikation som ingen
längre förstod helt.

På vägen: attacken som tog sig in hos Google genom ett hål i Internet
Explorer, två regeringar som sa åt sina medborgare att byta webbläsare,
verktyget som Microsoft släppte för att blockera sin egen nya webbläsare
(fyra gånger), produkten de sålde som körde en dold kopia av Windows XP
inuti Windows 7 bara för att hålla den gamla webbläsaren vid liv, ett
land som bands till en enda leverantör av sina egna bankregler, och fem
och en halv miljoner pund som betalades för ett år till utan uppgradering.

Del ett — hur Internet Explorer 6 blev en plattform:
https://youtu.be/R7Un3IOMvbg

Del två — buggarna som hade namn:
https://youtu.be/1dIM5UZUEZg

Hela texten, källor och översättningar: https://theresmoretoit-channel.github.io/sv/videos/the-browser-that-wouldnt-die/

Kapitel
00:00 Del tre
01:19 Januari 2010
01:33 Någon inne hos Google
02:02 Operation Aurora
02:36 Google slutar vänta
03:04 Den vanliga förklaringen är fel
04:06 Det var inte operativsystemet
04:20 Vilken applikation det var
05:13 Ett verktyg mot den egna webbläsaren
06:01 När datorn själv dör
06:44 Windows XP inuti Windows 7
07:26 Döda den och sälja den samtidigt
07:59 Bara en inställning i den nya
08:39 Sydkorea
09:40 Kina och USA
10:11 Åttahundratusen datorer
11:22 Hur det egentligen tog slut
12:24 Avstängd 2022
12:53 Webbläsare, plattform, beroende
13:39 När världen slutade bero på den

Undertexterna är skrivna för den här videon, inte automatgenererade. Som andra ljudspår finns amerikansk engelska.
```
