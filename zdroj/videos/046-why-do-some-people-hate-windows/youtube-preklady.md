# Lokalizované názvy a popisy — Why Do Some People Hate Windows?

Podklad pro **YouTube Studio → video → Podrobnosti → Přidat jazyk**.
Pro každý jazyk jsou tu **dva bloky ke zkopírování**: název a popis.
Kopíruje se **celý blok mezi trojicí zpětných apostrofů**, co je mimo něj,
je poznámka. Anglický originál zůstává v `youtube.md` a nesahá se na něj.

Nahrává je `tools/lokalizace.py`, který čte právě tenhle formát.
Pořadí jazyků je podle YouTube Studia, tedy bajtově podle UTF-8
**českého názvu jazyka** (ne podle kódu a ne podle endonyma):
fi, fr, id, it, de, pl, pt-BR, tr, uk, vi, cs, es, sv — **třináct**,
od rozšíření kanálu 2026-09-15.

## Co se NEPŘEKLÁDÁ

| | |
|---|---|
| **vlastní jména** | Windows, Windows 95, Windows 98, Windows ME, Windows NT, Windows XP, Microsoft, Linux, Apple, Mac, MS-DOS, Internet Explorer, Netscape, OneDrive, Edge |
| **Dmitry Nosachev** | jméno autora snímku, povinná atribuce |
| **Tekram DC-300B Fast SCSI ISA controller** | název díla v atribuci |
| **časy kapitol** | musí sedět na vteřinu, jinak je YouTube neuzná |
| **tagy** | YouTube je per-jazyk nemá |
| **CC BY-SA 4.0**, `creativecommons.org/licenses/by-sa/4.0` | licenční údaje |

Názvy kapitol se naopak **překládají** — divák je čte v seznamu pod videem.
Stejně tak se překládají **názvy jazyků** ve větě o titulcích: smíšený
seznam endonym uprostřed odstavce čte jako nedotažený překlad.

## Kontrola čísel

V popisu je **miliarda** počítačů a **sedmnáct** kapitol s časy
`0:00`–`10:43`. Miliarda je 10⁹, tedy `Milliarde` / `mil millones` /
`bilhão` / `milliard` / `miliardo` / `miliard` / `miljard` — **ne**
`billón`, `Billion` ani `trillion`, to je o tři až šest řádů vedle.

---

## suomi (`fi`)

```
Miksi jotkut vihaavat Windowsia?
```

```
Windows pyörii yli miljardilla tietokoneella. Useimmille sitä käyttäville
se on vain se, mikä käynnistyy, kun he painavat nappia.

Ja sitten on ihmisiä, jotka jaksavat puhua tunnin siitä, miksi se on
kamala.

Tämä video kertoo siitä, mitä nuo ihmiset oikeastaan vastustavat — ja
miksi se ei ehkä kuulosta sinusta lainkaan järkevältä.

Osa siitä on historiaa: nykyistä Windowsia ei koskaan suunniteltu yhdeksi
järjestelmäksi, ja taaksepäin yhteensopivuus on samaan aikaan sen suurin
vahvuus ja syy siihen, miksi se tuntuu teknologiselta tilkkutäkiltä. Osa
on mainetta, joka syntyi yhdeksänkymmentäluvulla eikä koskaan aivan
kadonnut. Ja osa koskee Microsoftia yhtiönä, ei Windowsia järjestelmänä.

Kaiken tämän alla on kuitenkin kysymys, jolla ei ole mitään tekemistä
bugien kanssa. Se koskee sitä, kuka päättää, mitä saat tehdä ostamallasi
asialla.

Koko teksti, lähteet ja käännökset: https://theresmoretoit-channel.github.io/fi/videos/why-do-some-people-hate-windows/

Luvut:
0:00 Useimmat eivät koskaan mieti sitä
0:42 Paradoksi: kolmekymmentä vuotta vanhat ohjelmat
1:12 Pesukone
1:39 Neljäkymmentä vuotta päälle rakentamista
2:07 Talo, jota ei voi purkaa
3:06 Windows 95, 98, ME — ja maine
3:32 Windows NT ja XP
4:04 Microsoft yhtiönä
4:42 ”Tietokonehan on minun”
5:33 Suljettu lähdekoodi
6:47 Kyse oli siitä, kuka päättää
7:04 Linux on toinen filosofia
7:56 Entä Apple?
8:59 Kolme lähestymistapaa
9:22 Nykyinen Windows
10:05 Kuka siis on oikeassa?
10:43 Mitä sinä oikeastaan haluat?

Tekstitykset ovat saatavilla englanniksi (UK), englanniksi (US),
tšekiksi, ruotsiksi, espanjaksi, portugaliksi (Brasilia), saksaksi,
ranskaksi, italiaksi, puolaksi, indonesiaksi, turkiksi, ukrainaksi,
vietnamiksi ja suomeksi. Ääniraitavalitsimessa on lisäksi
amerikanenglanninkielinen raita.

KUVALÄHTEET
Tekram DC-300B Fast SCSI ISA controller — Dmitry Nosachev, CC BY-SA 4.0
Wikimedia Commonsin kautta
Lisenssit: creativecommons.org/licenses/by-sa/4.0

Kaikki muut kuvat ovat projektin omista lähdetiedostoista.
```

## français (`fr`)

```
Pourquoi certains détestent-ils Windows ?
```

```
Windows tourne sur plus d'un milliard d'ordinateurs. Pour la plupart des
gens qui l'utilisent, c'est simplement ce qui démarre quand ils appuient
sur le bouton.

Et puis il y a ceux qui peuvent parler une heure de pourquoi c'est
atroce.

Cette vidéo parle de ce à quoi ces gens s'opposent vraiment — et de
pourquoi tout cela n'a peut-être aucun sens pour vous.

Une partie relève de l'histoire : le Windows d'aujourd'hui n'a jamais été
conçu comme un seul système, et la rétrocompatibilité est à la fois sa
plus grande force et la raison pour laquelle il donne l'impression d'un
patchwork technique. Une partie relève d'une réputation gagnée dans les
années quatre-vingt-dix et jamais tout à fait perdue. Et une partie
concerne Microsoft en tant qu'entreprise, pas Windows en tant que
système.

Mais sous tout cela il y a une question qui n'a rien à voir avec les
bugs. Elle porte sur qui décide de ce que vous avez le droit de faire
d'une chose que vous avez achetée.

Transcription complète, sources et traductions : https://theresmoretoit-channel.github.io/fr/videos/why-do-some-people-hate-windows/

Chapitres :
0:00 La plupart n'y pensent jamais
0:42 Le paradoxe : des programmes de trente ans
1:12 Le lave-linge
1:39 Quarante ans d'ajouts
2:07 L'immeuble qu'on ne peut pas démolir
3:06 Windows 95, 98, ME — et la réputation
3:32 Windows NT et XP
4:04 Microsoft en tant qu'entreprise
4:42 « Mais l'ordinateur est à moi »
5:33 Le code fermé
6:47 La question, c'était qui décide
7:04 Linux est une autre philosophie
7:56 Et Apple alors ?
8:59 Trois approches
9:22 Le Windows d'aujourd'hui
10:05 Alors, qui a raison ?
10:43 Que voulez-vous vraiment ?

Des sous-titres sont disponibles en anglais (Royaume-Uni), anglais
(États-Unis), tchèque, suédois, espagnol, portugais (Brésil), allemand,
français, italien et polonais. Le sélecteur de pistes audio propose en
plus une piste américaine.

CRÉDITS DES IMAGES
Tekram DC-300B Fast SCSI ISA controller — Dmitry Nosachev, CC BY-SA 4.0
via Wikimedia Commons
Licences : creativecommons.org/licenses/by-sa/4.0

Toutes les autres images proviennent des fichiers sources du projet.
```

## Bahasa Indonesia (`id`)

```
Kenapa sebagian orang benci Windows?
```

```
Windows berjalan di lebih dari satu miliar komputer. Bagi kebanyakan
orang yang memakainya, ia hanyalah yang menyala saat mereka menekan
tombol.

Lalu ada orang yang bisa bicara sejam soal kenapa Windows itu payah.

Video ini tentang apa yang sebenarnya ditolak orang-orang itu — dan
kenapa semua itu mungkin sama sekali tidak masuk akal buat kamu.

Sebagiannya sejarah: Windows hari ini tidak pernah dirancang sebagai satu
sistem, dan kompatibilitas ke belakang sekaligus merupakan kekuatan
terbesarnya dan alasan ia terasa seperti tambal sulam teknologi.
Sebagiannya reputasi yang didapat pada era 1990-an dan tidak pernah
benar-benar hilang. Dan sebagiannya soal Microsoft sebagai perusahaan,
bukan Windows sebagai sistem.

Tapi di bawah semua itu ada pertanyaan yang sama sekali tidak berkaitan
dengan bug. Pertanyaannya: siapa yang menentukan apa yang boleh kamu
lakukan dengan barang yang kamu beli.

Transkrip lengkap, sumber, dan terjemahan: https://theresmoretoit-channel.github.io/id/videos/why-do-some-people-hate-windows/

Bab:
0:00 Kebanyakan orang tidak pernah memikirkannya
0:42 Paradoks: program berumur tiga puluh tahun
1:12 Mesin cuci
1:39 Empat puluh tahun penambahan
2:07 Gedung yang tidak bisa dirobohkan
3:06 Windows 95, 98, ME — dan reputasinya
3:32 Windows NT dan XP
4:04 Microsoft sebagai perusahaan
4:42 "Tapi komputernya kan punyaku"
5:33 Kode tertutup
6:47 Ini soal siapa yang menentukan
7:04 Linux adalah filosofi lain
7:56 Bagaimana dengan Apple?
8:59 Tiga pendekatan
9:22 Windows masa kini
10:05 Jadi siapa yang benar?
10:43 Apa yang sebenarnya kamu mau?

Tersedia takarir dalam bahasa Inggris (Inggris), Inggris (AS), Ceko,
Swedia, Spanyol, Portugis (Brasil), Jerman, Prancis, Italia, Polandia,
Indonesia, Turki, Ukraina, Vietnam, dan Finlandia. Di pemilih trek audio
juga tersedia trek audio Amerika.

KREDIT GAMBAR
Tekram DC-300B Fast SCSI ISA controller — Dmitry Nosachev, CC BY-SA 4.0
melalui Wikimedia Commons
Lisensi: creativecommons.org/licenses/by-sa/4.0

Semua gambar lain berasal dari berkas sumber proyek ini.
```

## italiano (`it`)

```
Perché certe persone odiano Windows?
```

```
Windows gira su più di un miliardo di computer. Per la maggior parte di
chi lo usa è semplicemente la cosa che parte quando premono il pulsante.

E poi c'è chi riesce a parlare per un'ora di quanto sia orribile.

Questo video parla di ciò a cui quelle persone si oppongono davvero — e
del perché a te tutto questo potrebbe non dire assolutamente nulla.

Una parte è storia: il Windows di oggi non è mai stato progettato come un
sistema unico, e la compatibilità all'indietro è insieme il suo pregio
maggiore e il motivo per cui sembra un rattoppo tecnologico. Una parte è
una fama guadagnata negli anni novanta e mai del tutto persa. E una parte
riguarda Microsoft come azienda, non Windows come sistema.

Sotto tutto questo c'è però una domanda che con i bug non c'entra niente.
Riguarda chi decide cosa puoi fare con una cosa che hai comprato.

Trascrizione completa, fonti e traduzioni: https://theresmoretoit-channel.github.io/it/videos/why-do-some-people-hate-windows/

Capitoli:
0:00 La maggior parte non ci pensa mai
0:42 Il paradosso: programmi di trent'anni fa
1:12 La lavatrice
1:39 Quarant'anni di aggiunte
2:07 Il palazzo che non si può buttare giù
3:06 Windows 95, 98, ME — e la fama
3:32 Windows NT e XP
4:04 Microsoft come azienda
4:42 «Ma il computer è mio»
5:33 Codice chiuso
6:47 Il punto era chi decide
7:04 Linux è un'altra filosofia
7:56 E Apple?
8:59 Tre approcci
9:22 Il Windows di oggi
10:05 Allora chi ha ragione?
10:43 Cosa vuoi davvero tu?

I sottotitoli sono disponibili in inglese (Regno Unito), inglese (Stati
Uniti), ceco, svedese, spagnolo, portoghese (Brasile), tedesco, francese,
italiano e polacco. Nel selettore delle tracce audio c'è anche una
traccia americana.

CREDITI DELLE IMMAGINI
Tekram DC-300B Fast SCSI ISA controller — Dmitry Nosachev, CC BY-SA 4.0
tramite Wikimedia Commons
Licenze: creativecommons.org/licenses/by-sa/4.0

Tutte le altre immagini provengono dai file sorgente del progetto.
```

## Deutsch (`de`)

```
Warum hassen manche Leute Windows?
```

```
Windows läuft auf mehr als einer Milliarde Computer. Für die meisten
Menschen, die es benutzen, ist es einfach das, was startet, wenn sie den
Knopf drücken.

Und dann gibt es Leute, die eine Stunde lang erklären können, warum es
furchtbar ist.

Dieses Video handelt davon, wogegen sich diese Leute eigentlich wehren —
und warum das für dich vielleicht überhaupt keinen Sinn ergibt.

Ein Teil davon ist Geschichte: das heutige Windows wurde nie als ein
System entworfen, und die Abwärtskompatibilität ist zugleich seine
größte Stärke und der Grund, warum es sich wie ein technischer
Flickenteppich anfühlt. Ein Teil ist ein Ruf, der in den Neunzigern
entstand und nie ganz verschwand. Und ein Teil handelt von Microsoft als
Firma, nicht von Windows als System.

Darunter liegt aber eine Frage, die mit Fehlern nichts zu tun hat. Es
geht darum, wer entscheidet, was du mit etwas tun darfst, das du gekauft
hast.

Vollständiger Text, Quellen und Übersetzungen: https://theresmoretoit-channel.github.io/de/videos/why-do-some-people-hate-windows/

Kapitel:
0:00 Die meisten denken nie darüber nach
0:42 Das Paradox: dreißig Jahre alte Programme
1:12 Die Waschmaschine
1:39 Vierzig Jahre Anbauen
2:07 Das Haus, das niemand abreißen kann
3:06 Windows 95, 98, ME — und der Ruf
3:32 Windows NT und XP
4:04 Microsoft als Firma
4:42 „Der Computer gehört doch mir"
5:33 Geschlossener Quellcode
6:47 Es ging darum, wer entscheidet
7:04 Linux ist eine andere Philosophie
7:56 Und was ist mit Apple?
8:59 Drei Ansätze
9:22 Das heutige Windows
10:05 Wer hat also eigentlich recht?
10:43 Was willst du eigentlich?

Untertitel gibt es auf Englisch (UK), Englisch (US), Tschechisch,
Schwedisch, Spanisch, Portugiesisch (Brasilien), Deutsch, Französisch,
Italienisch und Polnisch. In der Tonspurauswahl gibt es zusätzlich eine
amerikanische Tonspur.

BILDNACHWEISE
Tekram DC-300B Fast SCSI ISA controller — Dmitry Nosachev, CC BY-SA 4.0
über Wikimedia Commons
Lizenzen: creativecommons.org/licenses/by-sa/4.0

Alle übrigen Bilder stammen aus den eigenen Quelldateien des Projekts.
```

## polski (`pl`)

```
Dlaczego niektórzy nienawidzą Windowsa?
```

```
Windows działa na ponad miliardzie komputerów. Dla większości ludzi,
którzy go używają, to po prostu to, co się uruchamia, kiedy naciskają
przycisk.

A są i tacy, którzy potrafią godzinę mówić o tym, dlaczego jest okropny.

Ten film jest o tym, czemu ci ludzie naprawdę się sprzeciwiają — i
dlaczego dla ciebie może to nie mieć żadnego sensu.

Część z tego to historia: dzisiejszy Windows nigdy nie był projektowany
jako jeden system, a zgodność wsteczna jest zarazem jego największą
zaletą i powodem, dla którego wydaje się technologicznym zlepkiem. Część
to opinia wyrobiona w latach dziewięćdziesiątych, której nigdy do końca
nie zrzucił. A część dotyczy Microsoftu jako firmy, nie Windowsa jako
systemu.

Pod tym wszystkim leży jednak pytanie, które z błędami nie ma nic
wspólnego. Chodzi o to, kto decyduje, co wolno ci zrobić z rzeczą, którą
kupiłeś.

Pełna transkrypcja, źródła i tłumaczenia: https://theresmoretoit-channel.github.io/pl/videos/why-do-some-people-hate-windows/

Rozdziały:
0:00 Większość nigdy o tym nie myśli
0:42 Paradoks: programy sprzed trzydziestu lat
1:12 Pralka
1:39 Czterdzieści lat dobudowywania
2:07 Budynek, którego nie da się zburzyć
3:06 Windows 95, 98, ME — i ta opinia
3:32 Windows NT i XP
4:04 Microsoft jako firma
4:42 „Przecież ten komputer jest mój"
5:33 Zamknięty kod
6:47 Chodziło o to, kto decyduje
7:04 Linux to inna filozofia
7:56 A co z Apple'em?
8:59 Trzy podejścia
9:22 Dzisiejszy Windows
10:05 Więc kto ma rację?
10:43 Czego ty właściwie chcesz?

Napisy są dostępne po angielsku (Wielka Brytania), angielsku (USA),
czesku, szwedzku, hiszpańsku, portugalsku (Brazylia), niemiecku,
francusku, włosku i polsku. W wyborze ścieżki dźwiękowej jest też
ścieżka amerykańska.

ŹRÓDŁA OBRAZÓW
Tekram DC-300B Fast SCSI ISA controller — Dmitry Nosachev, CC BY-SA 4.0
przez Wikimedia Commons
Licencje: creativecommons.org/licenses/by-sa/4.0

Wszystkie pozostałe obrazy powstały z plików źródłowych tego projektu.
```

## português (Brasil) (`pt-BR`)

```
Por que algumas pessoas odeiam o Windows?
```

```
O Windows roda em mais de um bilhão de computadores. Para a maioria das
pessoas que o usam, é simplesmente o que liga quando apertam o botão.

E existem pessoas capazes de falar uma hora sobre por que ele é horrível.

Este vídeo é sobre a que essas pessoas realmente se opõem — e por que
nada disso talvez faça o menor sentido para você.

Parte disso é história: o Windows de hoje nunca foi projetado como um
único sistema, e a compatibilidade com o passado é ao mesmo tempo a sua
maior força e o motivo de parecer uma colcha de retalhos tecnológica.
Parte é uma fama conquistada nos anos noventa e nunca totalmente perdida.
E parte tem a ver com a Microsoft como empresa, não com o Windows como
sistema.

Mas debaixo de tudo isso há uma pergunta que não tem nada a ver com bugs.
Ela é sobre quem decide o que você pode fazer com algo que comprou.

Transcrição completa, fontes e traduções: https://theresmoretoit-channel.github.io/pt-br/videos/why-do-some-people-hate-windows/

Capítulos:
0:00 A maioria nunca pensa nisso
0:42 O paradoxo: programas de trinta anos atrás
1:12 A máquina de lavar
1:39 Quarenta anos de acréscimos
2:07 O prédio que não dá para demolir
3:06 Windows 95, 98, ME — e a fama
3:32 Windows NT e XP
4:04 A Microsoft como empresa
4:42 "Mas o computador é meu"
5:33 Código fechado
6:47 Era sobre quem decide
7:04 O Linux é outra filosofia
7:56 E a Apple?
8:59 Três abordagens
9:22 O Windows de hoje
10:05 Então quem está certo?
10:43 O que você realmente quer?

Há legendas em inglês (Reino Unido), inglês (EUA), tcheco, sueco,
espanhol, português (Brasil), alemão, francês, italiano e polonês. No
seletor de faixas de áudio há também uma faixa americana.

CRÉDITOS DAS IMAGENS
Tekram DC-300B Fast SCSI ISA controller — Dmitry Nosachev, CC BY-SA 4.0
via Wikimedia Commons
Licenças: creativecommons.org/licenses/by-sa/4.0

Todas as outras imagens vêm dos arquivos-fonte do projeto.
```

## Türkçe (`tr`)

```
Bazı insanlar Windows'tan neden nefret eder?
```

```
Windows bir milyardan fazla bilgisayarda çalışıyor. Onu kullananların
çoğu için o sadece düğmeye bastıklarında açılan şey.

Bir de Windows'un neden berbat olduğunu bir saat anlatabilen insanlar
var.

Bu video, o insanların aslında neye karşı çıktığını anlatıyor — ve bunun
sana neden hiç anlamlı gelmeyebileceğini.

Bir kısmı tarih: bugünkü Windows hiçbir zaman tek bir sistem olarak
tasarlanmadı ve geriye dönük uyumluluk hem onun en büyük gücü hem de
teknolojik bir yamalı bohça gibi görünmesinin sebebi. Bir kısmı
doksanlarda kazanılmış ve hiç tam olarak kaybolmamış bir ün. Bir kısmı da
Windows'la değil, şirket olarak Microsoft'la ilgili.

Ama bütün bunların altında hatalarla hiç ilgisi olmayan bir soru yatıyor.
Satın aldığın bir şeyle ne yapabileceğine kimin karar verdiği sorusu.

Metnin tamamı, kaynaklar ve çeviriler: https://theresmoretoit-channel.github.io/tr/videos/why-do-some-people-hate-windows/

Bölümler:
0:00 Çoğu insan bunu hiç düşünmez
0:42 Paradoks: otuz yıllık programlar
1:12 Çamaşır makinesi
1:39 Kırk yıl üst üste ekleme
2:07 Yıkılamayan bina
3:06 Windows 95, 98, ME — ve o ün
3:32 Windows NT ve XP
4:04 Şirket olarak Microsoft
4:42 "Ama bilgisayar benim"
5:33 Kapalı kaynak
6:47 Mesele kimin karar verdiğiydi
7:04 Linux başka bir felsefe
7:56 Peki ya Apple?
8:59 Üç yaklaşım
9:22 Bugünün Windows'u
10:05 Peki aslında kim haklı?
10:43 Sen aslında ne istiyorsun?

Altyazılar İngilizce (BK), İngilizce (ABD), Çekçe, İsveççe, İspanyolca,
Portekizce (Brezilya), Almanca, Fransızca, İtalyanca, Lehçe, Endonezce,
Türkçe, Ukraynaca, Vietnamca ve Fince olarak mevcuttur. Ses parçası
seçicisinde ayrıca Amerikan İngilizcesi ses parçası bulunuyor.

GÖRSEL KAYNAKLAR
Tekram DC-300B Fast SCSI ISA controller — Dmitry Nosachev, CC BY-SA 4.0
Wikimedia Commons üzerinden
Lisanslar: creativecommons.org/licenses/by-sa/4.0

Diğer tüm görseller projenin kendi kaynak dosyalarından geliyor.
```

## українська (`uk`)

```
Чому дехто ненавидить Windows?
```

```
Windows працює більш ніж на мільярді комп'ютерів. Для більшості тих, хто
ним користується, це просто те, що вмикається, коли вони натискають
кнопку.

А ще є люди, які можуть годину розповідати, чому він жахливий.

Це відео про те, проти чого ті люди насправді заперечують — і чому тобі
все це може не мати жодного сенсу.

Частина з цього — історія: сьогоднішній Windows ніколи не проєктували як
одну систему, і зворотна сумісність є водночас його найбільшою перевагою
і причиною, чому він здається технологічним клаптиком. Частина — це
репутація, зароблена у дев'яностих і ніколи до кінця не втрачена.
А частина стосується Microsoft як компанії, а не Windows як системи.

Але під усім цим лежить питання, яке не має нічого спільного з помилками.
Воно про те, хто вирішує, що тобі можна робити з річчю, яку ти купив.

Повний текст, джерела та переклади: https://theresmoretoit-channel.github.io/uk/videos/why-do-some-people-hate-windows/

Розділи:
0:00 Більшість про це ніколи не думає
0:42 Парадокс: програми тридцятирічної давності
1:12 Пральна машина
1:39 Сорок років добудовування
2:07 Будинок, який не можна знести
3:06 Windows 95, 98, ME — і та репутація
3:32 Windows NT і XP
4:04 Microsoft як компанія
4:42 «Але ж комп'ютер мій»
5:33 Закритий код
6:47 Ішлося про те, хто вирішує
7:04 Linux — інша філософія
7:56 А що Apple?
8:59 Три підходи
9:22 Сьогоднішній Windows
10:05 То хто ж має рацію?
10:43 Чого насправді хочеш ти?

Субтитри доступні англійською (Велика Британія), англійською (США),
чеською, шведською, іспанською, португальською (Бразилія), німецькою,
французькою, італійською, польською, індонезійською, турецькою,
українською, в'єтнамською та фінською. У виборі звукової доріжки є також
американська доріжка.

ДЖЕРЕЛА ЗОБРАЖЕНЬ
Tekram DC-300B Fast SCSI ISA controller — Dmitry Nosachev, CC BY-SA 4.0
через Wikimedia Commons
Ліцензії: creativecommons.org/licenses/by-sa/4.0

Усі інші зображення створено з власних файлів проєкту.
```

## Tiếng Việt (`vi`)

```
Vì sao một số người ghét Windows?
```

```
Windows chạy trên hơn một tỷ máy tính. Với phần lớn những người dùng nó,
đó đơn giản là thứ khởi động khi họ bấm nút nguồn.

Và rồi có những người nói cả tiếng đồng hồ về chuyện nó tệ ra sao.

Video này nói về điều mà những người đó thực sự phản đối — và vì sao với
bạn tất cả những điều ấy có thể chẳng có nghĩa lý gì.

Một phần là lịch sử: Windows ngày nay chưa bao giờ được thiết kế như một
hệ thống duy nhất, và tính tương thích ngược vừa là điểm mạnh lớn nhất
của nó vừa là lý do nó giống một tấm chắp vá công nghệ. Một phần là tiếng
xấu có từ thập niên chín mươi và chưa bao giờ mất hẳn. Và một phần liên
quan tới Microsoft với tư cách công ty, chứ không phải Windows với tư
cách hệ thống.

Nhưng bên dưới tất cả những điều đó là một câu hỏi chẳng liên quan gì tới
lỗi. Nó là về chuyện ai quyết định bạn được làm gì với thứ bạn đã mua.

Toàn văn, nguồn và bản dịch: https://theresmoretoit-channel.github.io/vi/videos/why-do-some-people-hate-windows/

Các chương:
0:00 Phần lớn mọi người chưa bao giờ nghĩ tới
0:42 Nghịch lý: những chương trình ba mươi năm tuổi
1:12 Chiếc máy giặt
1:39 Bốn mươi năm chồng thêm
2:07 Tòa nhà không thể đập bỏ
3:06 Windows 95, 98, ME — và tiếng xấu
3:32 Windows NT và XP
4:04 Microsoft với tư cách công ty
4:42 "Nhưng máy tính là của tôi mà"
5:33 Mã nguồn đóng
6:47 Vấn đề là ai quyết định
7:04 Linux là một triết lý khác
7:56 Còn Apple thì sao?
8:59 Ba cách tiếp cận
9:22 Windows ngày nay
10:05 Vậy rốt cuộc ai đúng?
10:43 Bạn thật sự muốn gì?

Phụ đề có bằng tiếng Anh (Anh), tiếng Anh (Mỹ), tiếng Séc, tiếng Thụy
Điển, tiếng Tây Ban Nha, tiếng Bồ Đào Nha (Brazil), tiếng Đức, tiếng
Pháp, tiếng Ý, tiếng Ba Lan, tiếng Indonesia, tiếng Thổ Nhĩ Kỳ, tiếng
Ukraina, tiếng Việt và tiếng Phần Lan. Trong phần chọn bản âm thanh còn
có bản âm thanh giọng Mỹ.

NGUỒN HÌNH ẢNH
Tekram DC-300B Fast SCSI ISA controller — Dmitry Nosachev, CC BY-SA 4.0
qua Wikimedia Commons
Giấy phép: creativecommons.org/licenses/by-sa/4.0

Tất cả hình ảnh khác đều lấy từ các tệp nguồn của dự án.
```
## čeština (`cs`)

```
Proč někteří lidé nesnáší Windows?
```

```
Windows běží na víc než miliardě počítačů. Pro většinu lidí, kteří je
používají, je to prostě to, co naskočí, když zmáčknou tlačítko.

A pak jsou lidé, kteří dokážou hodinu vykládat, proč jsou hrozné.

Tohle video je o tom, čemu se ti lidé doopravdy brání — a proč ti to
možná nedává vůbec žádný smysl.

Něco z toho je historie: dnešní Windows nikdy nikdo nenavrhl jako jeden
systém a zpětná kompatibilita je zároveň jejich největší předností
i důvodem, proč působí jako technologická slepenina. Něco je pověst
vysloužená v devadesátkách, které se nikdy úplně nezbavily. A něco je
o Microsoftu jako firmě, ne o Windows jako systému.

Pod tím vším ale leží otázka, která s chybami nemá nic společného.
Je o tom, kdo rozhoduje, co smíš dělat s věcí, kterou sis koupil.

Celý text, zdroje a překlady: https://theresmoretoit-channel.github.io/cs/videos/why-do-some-people-hate-windows/

Kapitoly:
0:00 Většina lidí o tom nikdy nepřemýšlí
0:42 Paradox: třicet let staré programy
1:12 Pračka
1:39 Čtyřicet let přistavování
2:07 Dům, který nejde zbourat
3:06 Windows 95, 98, ME — a ta pověst
3:32 Windows NT a XP
4:04 Microsoft jako firma
4:42 „Vždyť ten počítač je můj"
5:33 Uzavřený kód
6:47 Šlo o to, kdo rozhoduje
7:04 Linux je jiná filozofie
7:56 A co Apple?
8:59 Tři přístupy
9:22 Dnešní Windows
10:05 Tak kdo má vlastně pravdu?
10:43 Co vlastně chceš ty?

Titulky jsou k dispozici v angličtině (UK), angličtině (US), češtině,
švédštině, španělštině, portugalštině (Brazílie), němčině, francouzštině,
italštině a polštině. Ve výběru zvukové stopy je i americká stopa.

OBRAZOVÉ ZDROJE
Tekram DC-300B Fast SCSI ISA controller — Dmitry Nosachev, CC BY-SA 4.0
přes Wikimedia Commons
Licence: creativecommons.org/licenses/by-sa/4.0

Všechny ostatní obrazy vznikly ze zdrojů tohoto projektu.
```

## español (`es`)

```
¿Por qué hay gente que odia Windows?
```

```
Windows funciona en más de mil millones de ordenadores. Para la mayoría
de quienes lo usan es simplemente lo que arranca cuando aprietan el
botón.

Y luego hay gente capaz de hablar una hora de por qué es horrible.

Este vídeo trata de a qué se oponen realmente esas personas, y de por qué
a ti puede que nada de eso te parezca razonable.

Parte de ello es historia: el Windows de hoy nunca se diseñó como un solo
sistema, y la compatibilidad hacia atrás es a la vez su mayor virtud y la
razón por la que parece un remiendo tecnológico. Parte es una fama que se
ganó en los noventa y de la que nunca se libró del todo. Y parte tiene
que ver con Microsoft como empresa, no con Windows como sistema.

Pero debajo de todo eso hay una pregunta que no tiene nada que ver con
los errores. Es sobre quién decide qué puedes hacer con algo que has
comprado.

Transcripción completa, fuentes y traducciones: https://theresmoretoit-channel.github.io/es/videos/why-do-some-people-hate-windows/

Capítulos:
0:00 La mayoría nunca piensa en ello
0:42 La paradoja: programas de hace treinta años
1:12 La lavadora
1:39 Cuarenta años de añadidos
2:07 El edificio que no se puede derribar
3:06 Windows 95, 98, ME — y la fama
3:32 Windows NT y XP
4:04 Microsoft como empresa
4:42 «Pero el ordenador es mío»
5:33 Código cerrado
6:47 Se trataba de quién decide
7:04 Linux es otra filosofía
7:56 ¿Y Apple?
8:59 Tres enfoques
9:22 El Windows de hoy
10:05 Entonces, ¿quién tiene razón?
10:43 ¿Qué quieres tú en realidad?

Hay subtítulos en inglés (RU), inglés (EE. UU.), checo, sueco, español,
portugués (Brasil), alemán, francés, italiano y polaco. En el selector de
pistas de audio hay además una pista estadounidense.

CRÉDITOS DE IMAGEN
Tekram DC-300B Fast SCSI ISA controller — Dmitry Nosachev, CC BY-SA 4.0
vía Wikimedia Commons
Licencias: creativecommons.org/licenses/by-sa/4.0

El resto de las imágenes procede de los archivos fuente del proyecto.
```

## svenska (`sv`)

```
Varför hatar vissa Windows?
```

```
Windows körs på mer än en miljard datorer. För de flesta som använder det
är det helt enkelt det som startar när de trycker på knappen.

Och så finns det de som kan prata i en timme om varför det är hemskt.

Den här videon handlar om vad de människorna faktiskt invänder mot — och
om varför det kanske är helt obegripligt för dig.

En del av det är historia: dagens Windows ritades aldrig som ett enda
system, och bakåtkompatibiliteten är på en gång dess största styrka och
skälet till att det känns som ett tekniskt lapptäcke. En del är ett rykte
som skapades på nittiotalet och aldrig riktigt försvann. Och en del
handlar om Microsoft som företag, inte om Windows som system.

Men under allt detta ligger en fråga som inte har med buggar att göra
alls. Den handlar om vem som bestämmer vad du får göra med något du har
köpt.

Hela texten, källor och översättningar: https://theresmoretoit-channel.github.io/sv/videos/why-do-some-people-hate-windows/

Kapitel:
0:00 De flesta tänker aldrig på det
0:42 Paradoxen: program från trettio år tillbaka
1:12 Tvättmaskinen
1:39 Fyrtio års tillbyggnad
2:07 Huset som inte går att riva
3:06 Windows 95, 98, ME — och ryktet
3:32 Windows NT och XP
4:04 Microsoft som företag
4:42 ”Men datorn är väl min”
5:33 Sluten källkod
6:47 Det handlade om vem som bestämmer
7:04 Linux är en annan filosofi
7:56 Och Apple då?
8:59 Tre hållningar
9:22 Dagens Windows
10:05 Så vem har egentligen rätt?
10:43 Vad vill du egentligen ha?

Undertexter finns på engelska (Storbritannien), engelska (USA),
tjeckiska, svenska, spanska, portugisiska (Brasilien), tyska, franska,
italienska och polska. I ljudspårsväljaren finns dessutom ett
amerikanskt ljudspår.

BILDKÄLLOR
Tekram DC-300B Fast SCSI ISA controller — Dmitry Nosachev, CC BY-SA 4.0
via Wikimedia Commons
Licenser: creativecommons.org/licenses/by-sa/4.0

Alla övriga bilder kommer från projektets egna källfiler.
```

