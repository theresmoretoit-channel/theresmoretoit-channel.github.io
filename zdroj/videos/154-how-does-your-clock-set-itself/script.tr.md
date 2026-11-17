<!-- S01 -->
Evinde bir yerde,
hiç kimsenin ayarlamadığı
bir saat olabilir.

<!-- S02 -->
Elektrik kesintilerinden etkilenmez.
Yaz saatine geçişi
kendi kendine, gecenin ortasında yapar.

<!-- S03 -->
İnternet bağlantısı yoktur.
Wi-Fi yok, GPS yok,
telefonunda bir uygulama da yok.

<!-- S04 -->
Elinde minicik bir radyo alıcısından başka bir şey yok.
Ve saniyede bir kez
tek bir darbe duyar.

<!-- S05 -->
Peki bir saat,
saniyede tek bir darbeyi
nasıl tam saate, tarihe
ve hatta haftanın gününe çevirir?

<!-- S06 -->
Avrupa'da bu darbeler
Frankfurt yakınlarındaki DCF77'den gelir.
Amerika'da ise Colorado'daki WWVB'den.
Vericiler farklı, fikir aynı.

<!-- S07 -->
Alman olanı ele alalım.
Gece gündüz
sabit bir radyo dalgası yayınlar.
Ve her saniyenin başında
bu dalgayı kısa bir süre zayıflatır.

<!-- S08 -->
İşin sırrı, dalganın
ne kadar süre zayıf kaldığı.

<!-- S09 -->
Saniyenin onda biri kadar süren bir düşüş
sıfır demektir.
Onda iki süren bir düşüş bir demektir.

<!-- S10 -->
Bütün fikir bu.
Paket yok, ağ yok.
Sadece kısa bir süre ya da biraz daha uzun
düşüş yapan bir radyo dalgası.

<!-- S11 -->
Her saniyede bir bit.
Yani sadece 60 bit göndermek
koca bir dakika sürer.

<!-- S12 -->
Aslında yalnızca 59 tane gönderir.

<!-- S13 -->
Her dakikanın son saniyesinde
dalga hiç düşmez.
Ve işte bu eksik düşüş,
bütün sinyalin
en önemli kısmıdır.

<!-- S14 -->
Çünkü bir sonraki düşüş geldiğinde
saat,
yeni bir dakikanın başladığını anlar.

<!-- S15 -->
Boşluk bir nokta gibi işler.
İki boşluk arasındaki her şey
tam bir cümledir.

<!-- S16 -->
Peki 59 bitlik bir cümleye
neler sığar?

<!-- S17 -->
Dakika. Saat.
Ayın günü, haftanın günü,
ay ve yıl.

<!-- S18 -->
Çoğu sayı basamak basamak gönderilir.
47 dakika
47 olarak gönderilmez.
İki ayrı basamak olarak gönderilir:
bir 4 ve bir 7.

<!-- S19 -->
0'dan 9'a kadar herhangi bir basamak için
4 bit yeterlidir.
Dakikanın onlar basamağı hiçbir zaman 5'i geçmez,
o yüzden ona sadece 3 bit düşer.

<!-- S20 -->
Yıla da sadece iki basamak düşer.
Verici açısından
2026 düpedüz 26'dır.
Yüzyılı saat kendisi ekler.

<!-- S21 -->
Ama radyo temiz bir kanal değildir.
Bir motor, bir telefon şarj cihazı,
ucuz bir LED ampul...
bunlardan herhangi biri bir düşüşü bulandırabilir.

<!-- S22 -->
Bu yüzden her sayı bloğundan sonra
eşlik biti denen fazladan bir bit gelir.

<!-- S23 -->
Bu bit, bloktaki birlerin sayısı
her zaman çift çıkacak şekilde seçilir.

<!-- S24 -->
Parazit tek bir biti ters çevirirse
sayı tek olur
ve saat
bir şeylerin ters gittiğini anlar.

<!-- S25 -->
Ama iki bit ters dönerse
sayı yine çift olur
ve hata gözden kaçar.

<!-- S26 -->
Bu yüzden birçok saat
tek bir dakikaya güvenmez.
Geçerli bir dakika daha bekler.

<!-- S27 -->
Ve bu yüzden saatin kendini ayarlaması
birkaç dakika sürebilir,
kötü bir günde ise çok daha uzun.

<!-- S28 -->
Bu da tuhaf bir sorun doğurur.

<!-- S29 -->
Saat, 10:48'in bilgisini toplamak için
koca bir dakika harcar.
Ama bu mesajı toplarken
saat hâlâ 10:47'dir.

<!-- S30 -->
Peki saat aslında ne zaman değişir?

<!-- S31 -->
Çünkü mesaj bir duyurudur.
Bir sonraki dakika başladığında
saatin kaç olacağını söyler.

<!-- S32 -->
Saat bütün cümleyi okur,
düşüşün olmadığı saniyenin geçmesini bekler,
ve bir sonraki düşüş geldiğinde
o düşüş tam andır.

<!-- S33 -->
Bitler saate saatin kaç olduğunu söyler.
Düşüş ise ne zaman olduğunu.

<!-- S34 -->
Ama cümlede sadece saat yok,
birkaç kelime daha var.

<!-- S35 -->
İki bit, Almanya'nın
kış saatinde mi yaz saatinde mi olduğunu söyler.

<!-- S36 -->
Üçüncüsü ise bir uyarıdır.
Saatler değişmeden önceki bir saat boyunca
değeri bir olur.

<!-- S37 -->
Yani saatinin,
saatlerin Mart'ın hangi pazarı
ileri alındığını
ya da Ekim'in hangi pazarı geri alındığını bilmesi gerekmez.
Bu kuralı ona kimse öğretmedi.
Sadece bir saat önceden haber verilir.

<!-- S38 -->
Avrupa bir gün saatleri değiştirmeyi bırakırsa,
bu uyarı bir daha asla gelmez.

<!-- S39 -->
Bir başka bit eskiden artık saniye için uyarırdı:
ara sıra eklenen fazladan bir saniye,
çünkü Dünya'nın dönüşü
zamanı kusursuz tutmaz.
O dakika 61 saniye sürebilirdi.

<!-- S40 -->
Sonuncusu
2016'nın sonunda eklendi.
Ama Ekim 2026'da
dünyanın metroloji otoriteleri
artık saniyelere son verme kararı aldı.
20 Mayıs 2027'den itibaren
UTC kesintisiz işleyecek.

<!-- S41 -->
Ve her dakikanın
ilk 14 biti
zamanla hiç ilgili değildir.

<!-- S42 -->
2006'dan beri bu bitler,
uyumlu hava istasyonları için
şifreli hava tahminleri taşımakta da kullanılıyor.

<!-- S43 -->
Yani çalar saatini ayarlayan sinyal,
başka birinin hava istasyonuna
perşembe günü yağmur yağıp yağmayacağını
da söyleyebiliyordu.

<!-- S44 -->
Yine de bu saatlerin çoğu
sürekli dinlemez.
Dinlemek pil tüketir,
bu yüzden çoğu gecede bir kez,
sabaha karşı dener.

<!-- S45 -->
Uzun dalgalar bir saate iki yoldan ulaşır:
yer yüzeyi boyunca
ve üst atmosferden yansıyarak.
Hava karardıktan sonra yukarıdaki yol değişir
ve sinyal çoğu zaman daha uzağa gider.

<!-- S46 -->
Ve gece saat üçte,
çevrede onu bastıracak makine, şarj cihazı ve ışık
genellikle daha az çalışır.

<!-- S47 -->
Bu kontroller arasında
saat bir kuvars kristaliyle çalışır,
o da günde bir saniye kadar kayabilir.

<!-- S48 -->
Bir sonraki başarılı kontrolde
radyo bu kaymayı düzeltir.

<!-- S49 -->
Saatin nerede dinlediği bile önemlidir.
Anten, etrafına tel sarılmış
küçük bir ferrit çubuktur.

<!-- S50 -->
Çubuk, vericinin yönüne
dik durduğunda en iyi duyar,
vericiyi gösterdiğinde değil.
Saati çevirirsen
zayıf bir sinyal tamamen kaybolabilir.

<!-- S51 -->
Bu yüzden bir saat rafta çalışırken
aynı saat iki metre ötede,
betonarme bir duvarın arkasında kendini hiç ayarlayamaz.

<!-- S52 -->
Peki verici
zamanı nereden alır?

<!-- S53 -->
Atom saatleri işleten
Almanya'nın ulusal metroloji enstitüsü
PTB'den.

<!-- S54 -->
Saniyenin kendisi
sezyum atomlarıyla tanımlanır.
Bir saniye, yaydıkları ışınımın
tam olarak
9.192.631.770 titreşimine eşittir.

<!-- S55 -->
Yani komodindeki ucuz bir çalar saat,
kelimenin tam anlamıyla,
sezyum atomlarıyla tanımlanan
bir zaman standardını izler.

<!-- S56 -->
Ama kusursuz değil.
Sinyal ışık hızında yol alır
ve ışık bile her 1.000 kilometreyi
yaklaşık 3 milisaniyede alır.

<!-- S57 -->
Alıcı kendi gecikmesini ekler
ve senin saatin bunların hiçbirini düzeltmez.
Gerek de yoktur.
Sadece saniyeleri gösterir.

<!-- S58 -->
Frankfurt yakınlarındaki tek bir noktadan
sinyal, yaklaşık 2.000 kilometreye kadar
uzaktaki saatlere ulaşır.
Bu, Avrupa'nın büyük kısmı demek.

<!-- S59 -->
İsviçre'nin de 2011 sonuna kadar
HBG adında kendi vericisi vardı.
Antenlerinin değişmesi gerekiyordu,
çok az kişi kullanıyordu
ve İsviçre'deki saatler onun yerine
Almanya'yı dinleyebilirdi.

<!-- S60 -->
Diğerleri kendi vericilerini korudu.
Birleşik Krallık, Fransa, Japonya ve Çin
kendi vericilerini işletiyor.

<!-- S61 -->
Kuzey Amerika'da ise WWVB,
1963'ten beri Fort Collins'ten yayın yapıyor,
1965'ten beri de bir zaman koduyla.

<!-- S62 -->
Aynı ilke, farklı şive.
Sıfır, saniyenin onda ikisi süren bir düşüştür.
Bir içinse düşüş yarım saniye sürer.

<!-- S63 -->
Ve dakikada bir boşluk yerine,
her 10 saniyede daha uzun bir işaret gelir,
cümledeki virgüller gibi.
Art arda iki tane, yeni bir dakika demektir.

<!-- S64 -->
En büyük fark
hangi zamanı gönderdiğidir.
Almanya, kıtanın büyük bölümünün paylaştığı
Orta Avrupa resmî saatini yayınlar.

<!-- S65 -->
Ama Amerika Birleşik Devletleri
birkaç saat dilimine yayılır.
Bu yüzden WWVB evrensel saati, yani UTC'yi gönderir
ve nerede olduğunu saate sen söylersin.

<!-- S66 -->
Ayı bile göndermez.
Sadece yılın kaçıncı günü olduğunu,
1'den 366'ya kadar.

<!-- S67 -->
Bu istasyonların hiçbiri
aynı dili konuşmaz.
Almanya için yapılmış bir saat
Colorado'dan bir şey anlamaz.

<!-- S68 -->
Ama Atlantik'in iki yakasında da
aynı sessiz rutin sürer.
Her gece küçük bir alıcı,
yüzlerce ya da binlerce kilometre ötedeki
bir atomik zaman standardına kendini ayarlar.

<!-- S69 -->
O hâlde sana bir sorum var.
Bütün radyo zaman sinyalleri
bu gece ortadan kaybolsa,
fark eder miydin?
Yorumlarda bana yaz.
