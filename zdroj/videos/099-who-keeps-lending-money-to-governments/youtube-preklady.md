# Lokalizované názvy a popisy — 099

Čte `tools/lokalizace.py` a nahrává přes `videos.update(part="localizations")`.
Anglický titul a popis jsou v `youtube.md` a posílají se zpátky beze změny.

**Pořadí sekcí je podle YouTube Studia** (bajtově podle ČESKÉHO názvu jazyka):
fi, fr, id, it, de, pl, pt-BR, tr, uk, vi, cs, es, sv.

**Codex proběhl 2026-10-10** (`codex-youtube-preklady.txt`): čísla, data,
procenta, časy kapitol i terminologie sedí. Přijato všech 10 nálezů:
fr/id/pt-BR konec druhého odstavce („splácí se VŮBEC něco", ne „splatí se
všechno"); vi 06:11 a 09:01 (pokračování z *keeps*); id a vi 00:34 bez kalku;
it 06:11 s předmětem; cs a pl 07:11 jako věta podle S66 („Refinancování má
háček", „Refinansowanie ma haczyk" místo Codexova „gdzie tkwi haczyk?").

## Co se NEPŘEKLÁDÁ

- vlastní jména a názvy zdrojů: Eurostat, World Economic Outlook (zkratka
  IMF/MMF/FMI/IWF/MFW/МВФ podle cílového jazyka)
- atribuce: řádky s autorem a licencí zůstávají beze změny anglicky, včetně
  `via Wikimedia Commons`, `All other archive images are in the public
  domain.` a řádku `Licences: …`; přeložený je jen nadpis bloku IMAGE CREDITS
- časy kapitol na vteřinu
- tagy (YouTube je per-jazyk nemá)

Odstavec o titulcích a americké stopě je doslova z tabulky kanonických znění
v `docs/zverejneni.md`. Titul = první řádek `script.<kód>.md`. Čísla mají
desetinnou čárku a znak procenta podle zvyklosti jazyka (tr `%4,52`).
*Past year* = posledních dvanáct měsíců, stejně jako v S12 překladů (elipsa,
viz `notes.md`). Terminologie kapitol je ze scénáře daného jazyka (S07, S16,
S22, S33, S38, S47, S56, S66 háček/Haken/hic…, S76, S82). Registr podle
překladů: cs ty, sv du, es tú, pt-BR você, de du, fr tu, it tu, pl ty,
id kamu, tr sen, uk ти, fi sinä, vi bạn — popis ani kapitoly diváka
neoslovují (originál taky ne).

## suomi (`fi`)

```
Kuka lainaa valtioille jatkuvasti rahaa?
```

```
Kreikka on velkaa noin 146 % bruttokansantuotteestaan, enemmän kuin mikään muu Euroopan unionin maa. Silti se on suurimman osan kuluneesta vuodesta saanut lainaa halvemmalla kuin Ranska.

Valtiot kuluttavat vuodesta toiseen enemmän kuin keräävät, eivätkä vanhat lainat tunnu koskaan katoavan. Kuka niille siis jatkuvasti lainaa rahaa? Kuka oikeastaan ostaa valtion joukkovelkakirjoja, miten Japani voi olla velkaa yli kaksi kertaa koko taloutensa verran, ja maksetaanko siitä koskaan mitään takaisin?

Velka- ja alijäämäluvut: Eurostat (huhtikuun 2026 raportointi) ja IMF:n World Economic Outlook (huhtikuu 2026). Kymmenen vuoden valtionlainojen korot 2.10.2026: Kreikka 4,52 %, Ranska 4,91 %.

Tekstitykset on kirjoitettu tätä videota varten, ei luotu automaattisesti. Toisena ääniraitana on amerikanenglanti.

Koko teksti, lähteet ja käännökset: https://theresmoretoit-channel.github.io/fi/videos/who-keeps-lending-money-to-governments/

LUVUT
00:00 Lainaa joka vuosi
00:34 Missä se lakkasi toimimasta
01:30 Alijäämä ja velka
02:07 Kaksi todellista maata
03:38 Koko Eurooppa
04:07 Kuka ostaa valtionlainoja?
05:13 Japani
06:11 Milloin se maksetaan takaisin?
07:11 Jälleenrahoituksen koukku
08:13 Miksei kaikkea makseta pois?
09:01 Kuka siis lainaa jatkuvasti?

KUVALÄHTEET
2011 Greece Uprising — Kotsolis at English Wikipedia, CC BY-SA 3.0
United States Treasury Building — Rchuon24, CC BY-SA 3.0
Bank of Japan Head Office, Tokyo - Aug 29, 2011 — yt_siden, CC BY-SA 2.0
via Wikimedia Commons
All other archive images are in the public domain.
Licences: creativecommons.org/licenses/by-sa/3.0, creativecommons.org/licenses/by-sa/2.0
```

## français (`fr`)

```
Qui continue de prêter de l'argent aux États ?
```

```
La Grèce doit environ 146 % de son PIB, plus que tout autre pays de l'Union européenne. Et pourtant, pendant la majeure partie de l'année écoulée, elle a emprunté moins cher que la France.

Les États dépensent plus qu'ils n'encaissent, année après année, et les vieux emprunts ne semblent jamais disparaître. Alors qui continue de leur prêter de l'argent ? Qui achète vraiment les obligations d'État, comment le Japon peut-il devoir plus du double de toute son économie, et est-ce qu’une partie de cette dette finit un jour par être remboursée ?

Chiffres de dette et de déficit : Eurostat (notification d'avril 2026) et World Economic Outlook du FMI (avril 2026). Rendements des obligations d'État à dix ans au 2 octobre 2026 : Grèce 4,52 %, France 4,91 %.

Les sous-titres sont écrits pour cette vidéo, pas générés automatiquement. Une piste audio en anglais américain est disponible en seconde piste.

Transcription complète, sources et traductions : https://theresmoretoit-channel.github.io/fr/videos/who-keeps-lending-money-to-governments/

CHAPITRES
00:00 Emprunter chaque année
00:34 Là où ça a cessé de fonctionner
01:30 Déficit et dette
02:07 Deux pays bien réels
03:38 L'Europe entière
04:07 Qui achète les obligations d'État ?
05:13 Le Japon
06:11 Quand est-ce qu'on rembourse ?
07:11 Le hic du refinancement
08:13 Pourquoi ne pas tout rembourser ?
09:01 Alors, qui continue de prêter ?

CRÉDITS DES IMAGES
2011 Greece Uprising — Kotsolis at English Wikipedia, CC BY-SA 3.0
United States Treasury Building — Rchuon24, CC BY-SA 3.0
Bank of Japan Head Office, Tokyo - Aug 29, 2011 — yt_siden, CC BY-SA 2.0
via Wikimedia Commons
All other archive images are in the public domain.
Licences: creativecommons.org/licenses/by-sa/3.0, creativecommons.org/licenses/by-sa/2.0
```

## Bahasa Indonesia (`id`)

```
Siapa yang Terus Meminjamkan Uang kepada Pemerintah?
```

```
Utang Yunani sekitar 146% dari PDB-nya, lebih tinggi daripada negara lain mana pun di Uni Eropa. Namun selama sebagian besar dua belas bulan terakhir, Yunani bisa meminjam lebih murah daripada Prancis.

Tahun demi tahun, pemerintah membelanjakan lebih dari yang mereka kumpulkan, dan pinjaman lama seolah tak pernah hilang. Jadi siapa yang terus meminjamkan uang kepada mereka? Siapa sebenarnya yang membeli obligasi pemerintah, bagaimana utang Jepang bisa lebih dari dua kali lipat seluruh ekonominya, dan apakah sebagian dari utang itu pernah benar-benar dibayar kembali?

Angka utang dan defisit: Eurostat (notifikasi April 2026) dan World Economic Outlook IMF (April 2026). Imbal hasil obligasi pemerintah sepuluh tahun pada 2 Oktober 2026: Yunani 4,52%, Prancis 4,91%.

Subtitel ditulis khusus untuk video ini, bukan dibuat secara otomatis. Tersedia juga trek audio kedua dalam bahasa Inggris Amerika.

Transkrip lengkap, sumber, dan terjemahan: https://theresmoretoit-channel.github.io/id/videos/who-keeps-lending-money-to-governments/

BAB
00:00 Berutang setiap tahun
00:34 Ketika cara ini tak lagi berhasil
01:30 Defisit dan utang
02:07 Dua negara sungguhan
03:38 Seluruh Eropa
04:07 Siapa yang membeli obligasi pemerintah?
05:13 Jepang
06:11 Kapan semua itu dilunasi?
07:11 Jebakan refinancing
08:13 Kenapa tidak dilunasi saja semuanya?
09:01 Jadi, siapa yang terus meminjamkan?

KREDIT GAMBAR
2011 Greece Uprising — Kotsolis at English Wikipedia, CC BY-SA 3.0
United States Treasury Building — Rchuon24, CC BY-SA 3.0
Bank of Japan Head Office, Tokyo - Aug 29, 2011 — yt_siden, CC BY-SA 2.0
via Wikimedia Commons
All other archive images are in the public domain.
Licences: creativecommons.org/licenses/by-sa/3.0, creativecommons.org/licenses/by-sa/2.0
```

## italiano (`it`)

```
Chi continua a prestare soldi ai governi?
```

```
La Grecia deve circa il 146% del suo PIL, più di qualsiasi altro paese dell'Unione europea. Eppure, per gran parte dell'ultimo anno, si è finanziata a costi più bassi della Francia.

Gli Stati spendono più di quanto incassano, anno dopo anno, e i vecchi prestiti non sembrano mai sparire. Allora chi continua a prestare loro i soldi? Chi compra davvero i titoli di Stato, come fa il Giappone a dovere più del doppio della sua intera economia, e alla fine qualcosa viene mai restituito?

Dati su debito e deficit: Eurostat (notifica di aprile 2026) e World Economic Outlook del FMI (aprile 2026). Rendimenti dei titoli di Stato a dieci anni al 2 ottobre 2026: Grecia 4,52%, Francia 4,91%.

I sottotitoli sono scritti per questo video, non generati automaticamente. Come seconda traccia audio è disponibile l’inglese americano.

Trascrizione completa, fonti e traduzioni: https://theresmoretoit-channel.github.io/it/videos/who-keeps-lending-money-to-governments/

CAPITOLI
00:00 Indebitarsi ogni anno
00:34 Dove ha smesso di funzionare
01:30 Deficit e debito
02:07 Due paesi reali
03:38 Tutta l'Europa
04:07 Chi compra i titoli di Stato?
05:13 Il Giappone
06:11 Quando si rimborsano i debiti?
07:11 Il limite del rifinanziamento
08:13 Perché non ripagare tutto?
09:01 Allora, chi continua a prestare?

CREDITI DELLE IMMAGINI
2011 Greece Uprising — Kotsolis at English Wikipedia, CC BY-SA 3.0
United States Treasury Building — Rchuon24, CC BY-SA 3.0
Bank of Japan Head Office, Tokyo - Aug 29, 2011 — yt_siden, CC BY-SA 2.0
via Wikimedia Commons
All other archive images are in the public domain.
Licences: creativecommons.org/licenses/by-sa/3.0, creativecommons.org/licenses/by-sa/2.0
```

## Deutsch (`de`)

```
Wer leiht den Staaten immer wieder Geld?
```

```
Griechenland schuldet etwa 146 % seines BIP, mehr als jedes andere Land der Europäischen Union. Und trotzdem hat es sich die meiste Zeit der letzten zwölf Monate günstiger Geld geliehen als Frankreich.

Staaten geben Jahr für Jahr mehr aus, als sie einnehmen, und die alten Kredite scheinen nie zu verschwinden. Wer leiht ihnen also immer wieder das Geld? Wer kauft eigentlich Staatsanleihen, wie kann Japan mehr als das Doppelte seiner gesamten Wirtschaftsleistung schulden, und wird davon überhaupt jemals etwas zurückgezahlt?

Schulden- und Defizitzahlen: Eurostat (Meldung vom April 2026) und World Economic Outlook des IWF (April 2026). Renditen zehnjähriger Staatsanleihen am 2. Oktober 2026: Griechenland 4,52 %, Frankreich 4,91 %.

Die Untertitel wurden für dieses Video geschrieben, nicht automatisch erzeugt. Als zweite Tonspur steht amerikanisches Englisch bereit.

Vollständiger Text, Quellen und Übersetzungen: https://theresmoretoit-channel.github.io/de/videos/who-keeps-lending-money-to-governments/

KAPITEL
00:00 Jedes Jahr neue Schulden
00:34 Wo es nicht mehr funktioniert hat
01:30 Defizit und Schulden
02:07 Zwei echte Länder
03:38 Ganz Europa
04:07 Wer kauft Staatsanleihen?
05:13 Japan
06:11 Wann wird zurückgezahlt?
07:11 Der Haken an der Refinanzierung
08:13 Warum nicht einfach alles abzahlen?
09:01 Also, wer leiht immer wieder?

BILDNACHWEISE
2011 Greece Uprising — Kotsolis at English Wikipedia, CC BY-SA 3.0
United States Treasury Building — Rchuon24, CC BY-SA 3.0
Bank of Japan Head Office, Tokyo - Aug 29, 2011 — yt_siden, CC BY-SA 2.0
via Wikimedia Commons
All other archive images are in the public domain.
Licences: creativecommons.org/licenses/by-sa/3.0, creativecommons.org/licenses/by-sa/2.0
```

## polski (`pl`)

```
Kto ciągle pożycza pieniądze rządom?
```

```
Grecja jest winna około 146% swojego PKB, więcej niż jakikolwiek inny kraj Unii Europejskiej. A mimo to przez większą część ostatnich dwunastu miesięcy pożyczała taniej niż Francja.

Rządy rok w rok wydają więcej, niż wpływa do budżetu, a stare pożyczki jakby nigdy nie znikały. Kto więc ciągle pożycza im pieniądze? Kto właściwie kupuje obligacje skarbowe, jak Japonia może być winna ponad dwukrotność całej swojej gospodarki i czy cokolwiek z tego jest kiedyś spłacane?

Dane o długu i deficycie: Eurostat (notyfikacja z kwietnia 2026) i World Economic Outlook MFW (kwiecień 2026). Rentowności dziesięcioletnich obligacji skarbowych 2 października 2026: Grecja 4,52%, Francja 4,91%.

Napisy są pisane do tego filmu, nie generowane automatycznie. Jako druga ścieżka dźwiękowa dostępny jest angielski amerykański.

Pełna transkrypcja, źródła i tłumaczenia: https://theresmoretoit-channel.github.io/pl/videos/who-keeps-lending-money-to-governments/

ROZDZIAŁY
00:00 Pożyczki co roku
00:34 Tam, gdzie to przestało działać
01:30 Deficyt i dług
02:07 Dwa prawdziwe kraje
03:38 Cała Europa
04:07 Kto kupuje obligacje skarbowe?
05:13 Japonia
06:11 Kiedy to się spłaca?
07:11 Refinansowanie ma haczyk
08:13 Dlaczego nie spłacić wszystkiego?
09:01 Kto więc ciągle pożycza?

ŹRÓDŁA ZDJĘĆ
2011 Greece Uprising — Kotsolis at English Wikipedia, CC BY-SA 3.0
United States Treasury Building — Rchuon24, CC BY-SA 3.0
Bank of Japan Head Office, Tokyo - Aug 29, 2011 — yt_siden, CC BY-SA 2.0
via Wikimedia Commons
All other archive images are in the public domain.
Licences: creativecommons.org/licenses/by-sa/3.0, creativecommons.org/licenses/by-sa/2.0
```

## português (Brasil) (`pt-BR`)

```
Quem continua emprestando dinheiro aos governos?
```

```
A Grécia deve cerca de 146% do seu PIB, mais do que qualquer outro país da União Europeia. Mesmo assim, durante a maior parte do último ano, se financiou mais barato que a França.

Os governos gastam mais do que arrecadam, ano após ano, e os empréstimos antigos parecem nunca sumir. Então, quem continua emprestando dinheiro para eles? Quem de fato compra títulos públicos, como o Japão pode dever mais que o dobro de toda a sua economia, e alguma parte dessa dívida chega a ser paga?

Dados de dívida e déficit: Eurostat (notificação de abril de 2026) e World Economic Outlook do FMI (abril de 2026). Rendimento dos títulos públicos de dez anos em 2 de outubro de 2026: Grécia 4,52%, França 4,91%.

As legendas foram escritas para este vídeo, não geradas automaticamente. Como segunda faixa de áudio está disponível o inglês americano.

Transcrição completa, fontes e traduções: https://theresmoretoit-channel.github.io/pt-br/videos/who-keeps-lending-money-to-governments/

CAPÍTULOS
00:00 Pegando emprestado todo ano
00:34 Onde isso parou de funcionar
01:30 Déficit e dívida
02:07 Dois países de verdade
03:38 A Europa toda
04:07 Quem compra títulos públicos?
05:13 Japão
06:11 Quando a dívida é paga?
07:11 O porém do refinanciamento
08:13 Por que não quitar tudo?
09:01 Então, quem continua emprestando?

CRÉDITOS DAS IMAGENS
2011 Greece Uprising — Kotsolis at English Wikipedia, CC BY-SA 3.0
United States Treasury Building — Rchuon24, CC BY-SA 3.0
Bank of Japan Head Office, Tokyo - Aug 29, 2011 — yt_siden, CC BY-SA 2.0
via Wikimedia Commons
All other archive images are in the public domain.
Licences: creativecommons.org/licenses/by-sa/3.0, creativecommons.org/licenses/by-sa/2.0
```

## Türkçe (`tr`)

```
Hükümetlere Durmadan Kim Borç Veriyor?
```

```
Yunanistan'ın borcu GSYH'sinin yaklaşık %146'sı; bu, Avrupa Birliği'ndeki diğer tüm ülkelerden fazla. Yine de son bir yılın büyük bölümünde Fransa'dan daha ucuza borçlandı.

Hükümetler yıldan yıla topladığından fazlasını harcıyor ve eski borçlar hiç ortadan kalkmıyor gibi. Peki onlara durmadan kim borç veriyor? Devlet tahvillerini aslında kim satın alıyor, Japonya nasıl tüm ekonomisinin iki katından fazla borçlu olabiliyor ve bu borcun herhangi bir kısmı hiç geri ödeniyor mu?

Borç ve bütçe açığı rakamları: Eurostat (Nisan 2026 bildirimi) ve IMF World Economic Outlook (Nisan 2026). 2 Ekim 2026 itibarıyla on yıllık devlet tahvili getirileri: Yunanistan %4,52, Fransa %4,91.

Altyazılar bu video için yazıldı, otomatik olarak oluşturulmadı. İkinci ses parçası olarak Amerikan İngilizcesi de mevcut.

Metnin tamamı, kaynaklar ve çeviriler: https://theresmoretoit-channel.github.io/tr/videos/who-keeps-lending-money-to-governments/

BÖLÜMLER
00:00 Her yıl yeniden borç
00:34 Düzenin işlemez hâle geldiği yer
01:30 Bütçe açığı ve borç
02:07 İki gerçek ülke
03:38 Bütün Avrupa
04:07 Devlet tahvillerini kim alıyor?
05:13 Japonya
06:11 Borç ne zaman ödeniyor?
07:11 Borç çevirmenin sorunu
08:13 Neden hepsi ödenmiyor?
09:01 Peki, durmadan kim borç veriyor?

GÖRSEL KAYNAKLARI
2011 Greece Uprising — Kotsolis at English Wikipedia, CC BY-SA 3.0
United States Treasury Building — Rchuon24, CC BY-SA 3.0
Bank of Japan Head Office, Tokyo - Aug 29, 2011 — yt_siden, CC BY-SA 2.0
via Wikimedia Commons
All other archive images are in the public domain.
Licences: creativecommons.org/licenses/by-sa/3.0, creativecommons.org/licenses/by-sa/2.0
```

## українська (`uk`)

```
Хто постійно позичає гроші урядам?
```

```
Греція винна близько 146 % свого ВВП — більше, ніж будь-яка інша країна Європейського Союзу. І все ж більшу частину останніх дванадцяти місяців вона позичала дешевше, ніж Франція.

Уряди рік у рік витрачають більше, ніж збирають, а старі позики ніби ніколи не зникають. То хто ж постійно позичає їм гроші? Хто насправді купує державні облігації, як борг Японії може більш ніж удвічі перевищувати всю її економіку і чи повертається колись хоч щось із цього?

Дані про борг і дефіцит: Eurostat (повідомлення за квітень 2026 року) та World Economic Outlook МВФ (квітень 2026 року). Дохідність десятирічних державних облігацій на 2 жовтня 2026 року: Греція 4,52 %, Франція 4,91 %.

Субтитри написані для цього відео, а не згенеровані автоматично. Також доступна друга звукова доріжка — американською англійською.

Повний текст, джерела та переклади: https://theresmoretoit-channel.github.io/uk/videos/who-keeps-lending-money-to-governments/

РОЗДІЛИ
00:00 Позичати щороку
00:34 Де це перестало працювати
01:30 Дефіцит і борг
02:07 Дві реальні країни
03:38 Уся Європа
04:07 Хто купує державні облігації?
05:13 Японія
06:11 Коли це повертають?
07:11 Підводний камінь рефінансування
08:13 Чому б не сплатити все?
09:01 То хто ж постійно позичає?

ДЖЕРЕЛА ЗОБРАЖЕНЬ
2011 Greece Uprising — Kotsolis at English Wikipedia, CC BY-SA 3.0
United States Treasury Building — Rchuon24, CC BY-SA 3.0
Bank of Japan Head Office, Tokyo - Aug 29, 2011 — yt_siden, CC BY-SA 2.0
via Wikimedia Commons
All other archive images are in the public domain.
Licences: creativecommons.org/licenses/by-sa/3.0, creativecommons.org/licenses/by-sa/2.0
```

## Tiếng Việt (`vi`)

```
Ai cứ mãi cho các chính phủ vay tiền?
```

```
Hy Lạp nợ khoảng 146% GDP, nhiều hơn bất kỳ quốc gia nào khác trong Liên minh châu Âu. Vậy mà trong phần lớn năm qua, Hy Lạp vay được rẻ hơn cả Pháp.

Năm này qua năm khác, các chính phủ chi nhiều hơn số tiền thu về, và các khoản vay cũ dường như chẳng bao giờ biến mất. Vậy ai cứ mãi cho họ vay tiền? Ai thực sự mua trái phiếu chính phủ, vì sao Nhật Bản có thể nợ hơn gấp đôi toàn bộ nền kinh tế của mình, và rốt cuộc số nợ ấy có bao giờ được trả không?

Số liệu nợ và thâm hụt: Eurostat (báo cáo tháng 4/2026) và World Economic Outlook của IMF (tháng 4/2026). Lợi suất trái phiếu chính phủ kỳ hạn mười năm ngày 2/10/2026: Hy Lạp 4,52%, Pháp 4,91%.

Phụ đề được viết riêng cho video này, không phải tạo tự động. Có thể chọn tiếng Anh Mỹ ở bản âm thanh thứ hai.

Toàn văn, nguồn và bản dịch: https://theresmoretoit-channel.github.io/vi/videos/who-keeps-lending-money-to-governments/

CHƯƠNG
00:00 Năm nào cũng đi vay
00:34 Khi cách này không còn hiệu quả
01:30 Thâm hụt và nợ
02:07 Hai quốc gia có thật
03:38 Khắp châu Âu
04:07 Ai mua trái phiếu chính phủ?
05:13 Nhật Bản
06:11 Bao giờ khoản vay mới được trả?
07:11 Vấn đề của đảo nợ
08:13 Sao không trả hết cho xong?
09:01 Vậy ai vẫn tiếp tục cho vay?

NGUỒN HÌNH ẢNH
2011 Greece Uprising — Kotsolis at English Wikipedia, CC BY-SA 3.0
United States Treasury Building — Rchuon24, CC BY-SA 3.0
Bank of Japan Head Office, Tokyo - Aug 29, 2011 — yt_siden, CC BY-SA 2.0
via Wikimedia Commons
All other archive images are in the public domain.
Licences: creativecommons.org/licenses/by-sa/3.0, creativecommons.org/licenses/by-sa/2.0
```

## čeština (`cs`)

```
Kdo pořád půjčuje vládám peníze?
```

```
Řecko dluží zhruba 146 % svého HDP, víc než kterákoli jiná země Evropské unie. A přesto si po většinu posledních dvanácti měsíců půjčovalo levněji než Francie.

Vlády rok co rok utrácejí víc, než vyberou, a staré půjčky jako by nikdy nezmizely. Kdo jim tedy pořád půjčuje peníze? Kdo vlastně kupuje státní dluhopisy, jak může Japonsko dlužit víc než dvojnásobek celé své ekonomiky, a splácí se z toho vůbec někdy něco?

Údaje o dluhu a deficitu: Eurostat (notifikace z dubna 2026) a World Economic Outlook MMF (duben 2026). Výnosy desetiletých státních dluhopisů k 2. říjnu 2026: Řecko 4,52 %, Francie 4,91 %.

Titulky jsou psané pro tohle video, ne strojový přepis. Jako druhá zvuková stopa je k dispozici americká angličtina.

Celý text, zdroje a překlady: https://theresmoretoit-channel.github.io/cs/videos/who-keeps-lending-money-to-governments/

KAPITOLY
00:00 Každý rok nová půjčka
00:34 Kde to fungovat přestalo
01:30 Deficit a dluh
02:07 Dvě skutečné země
03:38 Celá Evropa
04:07 Kdo kupuje státní dluhopisy?
05:13 Japonsko
06:11 Kdy se to splatí?
07:11 Refinancování má háček
08:13 Proč to prostě všechno nesplatit?
09:01 Kdo tedy pořád půjčuje?

ZDROJE OBRÁZKŮ
2011 Greece Uprising — Kotsolis at English Wikipedia, CC BY-SA 3.0
United States Treasury Building — Rchuon24, CC BY-SA 3.0
Bank of Japan Head Office, Tokyo - Aug 29, 2011 — yt_siden, CC BY-SA 2.0
via Wikimedia Commons
All other archive images are in the public domain.
Licences: creativecommons.org/licenses/by-sa/3.0, creativecommons.org/licenses/by-sa/2.0
```

## español (`es`)

```
¿Quién sigue prestando dinero a los gobiernos?
```

```
Grecia debe alrededor del 146 % de su PIB, más que cualquier otro país de la Unión Europea. Y aun así, durante la mayor parte del último año, se ha financiado más barato que Francia.

Los gobiernos gastan más de lo que recaudan, año tras año, y los préstamos antiguos nunca parecen desaparecer. Entonces, ¿quién sigue prestándoles el dinero? ¿Quién compra de verdad los bonos del Estado, cómo puede Japón deber más del doble de toda su economía y se llega a devolver algo de todo eso alguna vez?

Cifras de deuda y déficit: Eurostat (notificación de abril de 2026) y World Economic Outlook del FMI (abril de 2026). Rentabilidad de los bonos del Estado a diez años el 2 de octubre de 2026: Grecia 4,52 %, Francia 4,91 %.

Los subtítulos están escritos para este vídeo, no generados automáticamente. Como segunda pista de audio está disponible el inglés americano.

Transcripción completa, fuentes y traducciones: https://theresmoretoit-channel.github.io/es/videos/who-keeps-lending-money-to-governments/

CAPÍTULOS
00:00 Pedir prestado cada año
00:34 Donde dejó de funcionar
01:30 Déficit y deuda
02:07 Dos países reales
03:38 Toda Europa
04:07 ¿Quién compra bonos del Estado?
05:13 Japón
06:11 ¿Cuándo se devuelve?
07:11 La pega de la refinanciación
08:13 ¿Por qué no pagarlo todo?
09:01 Entonces, ¿quién sigue prestando?

CRÉDITOS DE LAS IMÁGENES
2011 Greece Uprising — Kotsolis at English Wikipedia, CC BY-SA 3.0
United States Treasury Building — Rchuon24, CC BY-SA 3.0
Bank of Japan Head Office, Tokyo - Aug 29, 2011 — yt_siden, CC BY-SA 2.0
via Wikimedia Commons
All other archive images are in the public domain.
Licences: creativecommons.org/licenses/by-sa/3.0, creativecommons.org/licenses/by-sa/2.0
```

## svenska (`sv`)

```
Vem fortsätter att låna ut pengar till stater?
```

```
Grekland har en skuld på ungefär 146 % av sin BNP, mer än något annat land i Europeiska unionen. Och ändå har landet under större delen av de senaste tolv månaderna lånat billigare än Frankrike.

Stater gör av med mer än de får in, år efter år, och de gamla lånen verkar aldrig försvinna. Så vem fortsätter att låna ut pengarna till dem? Vem köper egentligen statsobligationer, hur kan Japan ha en skuld som är mer än dubbelt så stor som hela landets ekonomi, och betalas något av det någonsin tillbaka?

Siffror för skuld och underskott: Eurostat (rapporteringen i april 2026) och IMF:s World Economic Outlook (april 2026). Räntor på tioåriga statsobligationer den 2 oktober 2026: Grekland 4,52 %, Frankrike 4,91 %.

Undertexterna är skrivna för den här videon, inte automatgenererade. Som andra ljudspår finns amerikansk engelska.

Hela texten, källor och översättningar: https://theresmoretoit-channel.github.io/sv/videos/who-keeps-lending-money-to-governments/

KAPITEL
00:00 Lånar varje år
00:34 Där det slutade fungera
01:30 Underskott och skuld
02:07 Två verkliga länder
03:38 Hela Europa
04:07 Vem köper statsobligationer?
05:13 Japan
06:11 När betalas det tillbaka?
07:11 Haken med refinansiering
08:13 Varför inte betala av allt?
09:01 Så vem fortsätter att låna ut?

BILDKÄLLOR
2011 Greece Uprising — Kotsolis at English Wikipedia, CC BY-SA 3.0
United States Treasury Building — Rchuon24, CC BY-SA 3.0
Bank of Japan Head Office, Tokyo - Aug 29, 2011 — yt_siden, CC BY-SA 2.0
via Wikimedia Commons
All other archive images are in the public domain.
Licences: creativecommons.org/licenses/by-sa/3.0, creativecommons.org/licenses/by-sa/2.0
```
