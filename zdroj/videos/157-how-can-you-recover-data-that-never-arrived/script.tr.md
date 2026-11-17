<!-- S01 -->
Bu bir QR kod.
İçinde kısa bir satır metin var.

<!-- S02 -->
Telefon onu hemen okuyor.

<!-- S03 -->
Şimdi ondan bir parça koparalım.

<!-- S04 -->
Ve tekrar tarayalım.
Aynı metin.
Harfi harfine.

<!-- S05 -->
Kodun bir kısmı yok.
Silik falan değil.
Yok.

<!-- S06 -->
Peki telefon, artık orada
olmayan bir şeyi nasıl okuyabilir?

<!-- S07 -->
İşte aynı problemin küçültülmüş hâli.
Biri size sekiz bit gönderiyor.
Yolda bunlardan üçü kayboluyor.

<!-- S08 -->
Her eksik bit ya sıfırdır ya bir,
yani boşlukları doldurmanın sekiz yolu var.
Ve gelen bitlerdeki hiçbir şey
hangisinin doğru olduğunu söylemiyor.

<!-- S09 -->
Yine de telefon tam olarak bunu yaptı.
Tahmin yürütmüyordu.
Cevap zaten gönderilmişti,
daha hiçbir şey kaybolmadan.

<!-- S10 -->
İşin sırrı, mesajın kendisinden
fazlasını göndermek.

<!-- S11 -->
En basit yol,
her şeyi üç kez söylemek.
Sıfır, üç sıfır olarak gönderilir;
bir ise üç bir olarak.

<!-- S12 -->
Gürültü bunlardan birini ters çevirir
ve siz bir, sıfır, bir alırsınız.
Bire karşı iki oy.
Gönderilen neredeyse kesinlikle birdi.

<!-- S13 -->
Gürültü her on bitten birini,
rastgele ve bağımsız olarak çevirirse,
üçlü oylamanın yanılma oranı
yüzde üçten az olur.

<!-- S14 -->
Ama gönderdiğiniz her şeyi
üçe katladınız.
Mükemmele daha çok yaklaşmak için
beş kez tekrarlardınız, sonra dokuz,
sonra yüz...
ve mesaj kaplumbağa hızına düşerdi.

<!-- S15 -->
Uzun süre
ödenmesi gereken bedel bu gibi göründü.
Daha az hata, daha yavaş mesaj.
Bunu aklınızda tutun.

<!-- S16 -->
1940'ların sonunda
Bell Labs'te Richard Hamming'in
kendine ait bir sorunu vardı.

<!-- S17 -->
Bir röle bilgisayarında çoğunlukla
hafta sonları zaman bulabiliyordu,
başında onu izleyecek kimse yokken.

<!-- S18 -->
Makine, hata yaptığını
anlayabiliyordu.
Adımı yeniden deniyordu,
üç kez...
sonra da işlemi iptal ediyordu.
Üst üste iki hafta sonu
emeği boşa gitti.

<!-- S20 -->
Kendi sözleriyle sorusu şuydu:
“Makine bir hata olduğunu
tespit edebiliyorsa,
neden nerede olduğunu tespit edemiyor?”
Gerçekte, diye itiraf etmişti,
sözleri muhtemelen biraz daha sertti.

<!-- S22 -->
Onun çözümü dört bitlik mesajı alıp
üç kontrol biti ekliyor.
Toplam yedi bit.

<!-- S23 -->
Her kontrol biti
farklı bir konum grubundan sorumludur
ve o grubun
çift sayıda 1 içermesini sağlar.

<!-- S24 -->
Gruplar özenle seçilmiş bir düzende örtüşür.
Her konum
kendine özgü bir grup bileşimine aittir.

<!-- S25 -->
Şimdi bir biti ters çevirelim.
Diyelim ki altıncı konumdakini.

<!-- S26 -->
Alıcı üç kontrolü yeniden yapar.
Birincisi geçer.
İkincisi başarısız olur.
Üçüncüsü başarısız olur.

<!-- S27 -->
Başarısız kontrolü bir,
başarılı kontrolü sıfır olarak yazın
ve sondan başa doğru okuyun.
Bir, bir, sıfır.
İkili sistemde bu altı eder.

<!-- S28 -->
Kontroller sadece bir şeylerin
ters gittiğini söylemez.
Doğrudan hatalı biti gösterir.

<!-- S29 -->
Onu geri çevirin
ve mesaj yeniden eksiksiz olur.
Kimsenin bir şeyi iki kez göndermesi gerekmedi.

<!-- S30 -->
Demek ki cevap bu.
Alıcı kayıp bilgiyi
yoktan yeniden oluşturmuyor.
Gönderen onu mesaja eklemişti,
önceden.

<!-- S32 -->
Her kontrol bunu yapamaz.
Bir sağlama toplamı, mesela
Btrfs videomuzdaki gibi,
bir bloğun bozuk olduğunu söyleyebilir,
ama orijinal verinin ne olduğunu söyleyemez.

<!-- S33 -->
Bir de ikinci tür hasar var.
Bazen bir bit yanlış değildir.
Sadece eksiktir
ve boşluğun tam olarak nerede olduğunu bilirsiniz.

<!-- S34 -->
Buna silinme denir
ve silinmeleri düzeltmek daha kolaydır.

<!-- S35 -->
Dört sayı gönderin,
4, 7, 2 ve 9,
bir de beşincisini:
toplamlarını, 22.

<!-- S36 -->
Herhangi biri kaybolursa,
diğerleri size onun ne olduğunu söyler.
4, 7, bir şey, 9,
22.
Bu ancak iki olabilir.

<!-- S37 -->
Sunucular disklerini
benzer bir kontrolle korur,
bu kontrol disklere yayılmış hâldedir.
Bir disk bozulduğunda,
içeriği geri kalanlardan hesaplanır.

<!-- S38 -->
Peki ne kadar ek bilgi gerekiyor?
Tekrarlamanın cevabı şu:
hataları sıfıra indirmek için
hızı da sıfıra indirmeniz gerekir.

<!-- S39 -->
Hamming'in makalesi yayımlanmadan
iki yıl önce,
meslektaşı Claude Shannon
daha tuhaf bir cevap yayımlamıştı.

<!-- S40 -->
Her kanalın,
bir radyo bağlantısının, bir kablonun, bir diskin,
bir sınırı vardır.
Bilgi için bir azami hız.

<!-- S41 -->
Bu sınırın altında,
hatalar istediğiniz kadar seyrekleştirilebilir,
hem de yavaşlamadan.
Daha çok tekrarlayarak değil.
Daha akıllıca kodlayarak.

<!-- S42 -->
Üstünde ise
dünyadaki hiçbir kod işe yaramaz.

<!-- S43 -->
Ama bir pürüz vardı.
Shannon böyle kodların var olduğunu kanıtladı.
Herkesin kullanabileceği
bir kodun nasıl yapılacağını ise göstermedi.

<!-- S44 -->
Kanıtına göre rastgele seçilmiş bir kod
neredeyse kesinlikle iyi olurdu.
Ama onu çözmenin bariz yolu,
gelen şeyi
olası her mesajla karşılaştırmak demektir...
ve 1.000 bitlik bir blok için
bu mesajların sayısı
evrendeki atomlardan fazladır.

<!-- S46 -->
Yani Shannon'ın makalesi bir çözüm değildi.
Bir sözdü.
Ve mühendisler sonraki
45 yılı bu sözü tutmaya çalışarak geçirdi.

<!-- S47 -->
Hamming'in kodu ilk adımdı.
Yedi bitteki tek bir yanlış biti düzeltir.

<!-- S48 -->
Ama gerçek hasar toplu hâlde gelir.
Bir çizik ya da bir parazit cızırtısı
art arda yüzlerce biti silip götürür.

<!-- S49 -->
1960'ta Irving Reed ve Gustave Solomon,
MIT Lincoln Laboratory'de,
beş sayfalık bir makale yayımladı.

<!-- S50 -->
Onların kodları bütün baytlarla çalışır,
tek tek bitlerle değil.
Toplu bir hata bir baytın
sekiz bitinin hepsini bozsa bile,
bu yine de yalnızca bir bozuk bayttır.

<!-- S51 -->
Yaygın bir sürüm
32 kontrol baytını
223
baytlık veriye ekler.

<!-- S52 -->
Hatalı gelen herhangi 16 baytı
düzeltebilir...
ya da hiç gelmeyen 32 baytı
yeniden oluşturabilir.

<!-- S53 -->
Bir CD'nin çiziğe rağmen çalmasının sebebi bu.
İçindeki iki Reed-Solomon kodu
yaklaşık 4.000 bitlik bir boşluğu
tamamen onarabilir;
bu da 2,5 milimetrelik bir iz demek.

<!-- S54 -->
Yırtık QR kodun
hâlâ çalışmasının sebebi de bu.
En güçlü ayarında
bir QR kod, baytlarının
yaklaşık %30'una kadarını yeniden oluşturup
yine de her harfi geri verebilir.

<!-- S56 -->
Voyager 2, 1977'de Dünya'dan ayrıldığında
zaten bir Reed-Solomon kodlayıcı taşıyordu.

<!-- S57 -->
Ama Jüpiter ve Satürn civarında
fotoğraflar dışındaki her şeyi
Marcel Golay'ın daha eski bir koduyla korudu;
bu kod her veri biti için
bir ek bit gönderiyordu.

<!-- S58 -->
Uranüs ve Neptün için,
sinyal zayıfladıkça,
mühendisler Reed-Solomon'u devreye soktu,
ikinci bir kodun üstüne;
her bit zaten o koddan geçiyordu.

<!-- S59 -->
Yalnızca o ikinci kodla
bin bitten yaklaşık beşi
hâlâ yanlış oluyordu.
Üstüne Reed-Solomon eklenince
milyonda yaklaşık bir.

<!-- S60 -->
Gürültü de toplu hâlde gelir,
bu yüzden Voyager
dört bloğun baytlarını birbirine karıştırıyordu,
onları göndermeden önce.

<!-- S61 -->
Bir bloğu mahvedecek toplu bir hata
artık her bloktan birkaç bayt alıyor...
o kadar az ki her blok
kendini onarabiliyor.

<!-- S62 -->
Neptün fotoğraflarının Dünya'ya
nasıl ulaştığının devamı
Voyager videomuzda.

<!-- S63 -->
Ama bu bile
hâlâ Shannon sınırının gerisindeydi...
ve ona çok daha fazla yaklaşabilen bir kod
zaten vardı.

<!-- S65 -->
1960'ta MIT'deki doktora tezinde
Robert Gallager, birçok basit
kontrolden oluşan kodlar tanımladı;
her kontrol yalnızca birkaç bite bakıyordu.

<!-- S66 -->
Bunları çözmek, kontrollerin
tahminleri karşılıklı alıp vermesi demekti,
tur üstüne tur...
bu, fazlasıyla ağırdı
1960'ların bilgisayarları için.
Böylece fikir rafa kaldırıldı
ve 30 yıl boyunca büyük ölçüde unutuldu.

<!-- S68 -->
1993'te
iki Fransız mühendis, Claude Berrou ve
Alain Glavieux'nün yönettiği bir ekip,
turbo kodları
Cenevre'deki bir konferansta tanıttı.

<!-- S69 -->
Sonuçları Shannon sınırına
o kadar yakındı ki
birçok uzman
bir hata yaptıklarını düşündü.
Muhtemelen iki katlık bir hata,
hesaplarının bir yerinde.

<!-- S70 -->
Bir yıl içinde
başka laboratuvarlar bunu doğruladı.

<!-- S71 -->
Turbo kodlar da
tahminleri karşılıklı alıp vererek çalışıyordu
ve bu, insanları yeniden Gallager'a yöneltti.

<!-- S72 -->
1995 ve 1996'da
David MacKay ve Radford Neal
onun kodlarını yeniden keşfetti
ve bu kodların da sınıra
aynı ölçüde yaklaşabildiğini gösterdi.

<!-- S73 -->
2001'e gelindiğinde
Gallager kodlarının geliştirilmiş bir sürümü
Shannon sınırına
0,04 desibel kadar yaklaşmıştı.

<!-- S74 -->
Yani gereken sinyal gücü,
teorik minimumdan
yüzde bir bile fazla değil.
1948'in sözü tutulmuştu.

<!-- S75 -->
Bugün Gallager'ın kodları
verinin önemli bir kısmını taşıyor: 5G telefonlarda,
modern Wi-Fi'da
ve uydu televizyonunda.

<!-- S77 -->
Şimdi sekiz bitimize dönelim.
Üçü kaybolmuştu
ve boşlukları doldurmanın
sekiz yolu var.

<!-- S78 -->
Ama bu sekiz bit
hiçbir zaman yalnızca bir mesaj değildi.
İçlerinde dört bit veri vardı,
Hamming'in üç kontrolü
ve sekizinin tamamını kapsayan bir kontrol daha.

<!-- S79 -->
Olası 256
sekiz bitlik dizilimin
yalnızca 16'sı bu kurallara uyar.

<!-- S80 -->
Sekiz adayı deneyin.
Teker teker elenirler.
Geriye yalnızca biri kalır.

<!-- S81 -->
Eksik bitler aslında hiç kaybolmamıştı.
Bilgileri hâlâ oradaydı,
hayatta kalan bitlerin içinde.

<!-- S82 -->
O hâlde size bir soru.
Hata düzeltmenin, her gün kullandığınız
bir şeyde iş başında olduğunu hiç fark ettiniz mi?
Yorumlarda bana yazın.
