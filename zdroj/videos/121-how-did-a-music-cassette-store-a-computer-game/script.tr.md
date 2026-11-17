<!-- S01 -->
Bir kasetçalarda play'e basıyorsun.
Ve hoparlörden bu çıkıyor.

<!-- S02 -->
Bu müzik değil.
Bir oyunun müziği de değil.

<!-- S03 -->
Bu, oyunun ta kendisi.
Her ciyaklama bir programın parçası
ve bilgisayar onu dinliyor.

<!-- S04 -->
Kasetçaların hiçbir şeyden haberi yok.
Ona kalırsa bir şarkı çalıyor.

<!-- S05 -->
Peki bir şarkı nasıl oyuna dönüşür?
Ve neden tek bir yanlış nota
beş dakikalık beklemeyi çöpe atabiliyordu?

<!-- S06 -->
İşin sırrı şu,
bir makine örneğiyle:
ZX Spectrum,
1982 yapımı bir İngiliz ev bilgisayarı.

<!-- S07 -->
İki tür darbe kullanıyor.
Kısa bir darbe çifti sıfır demek.

<!-- S08 -->
Bir ise aynı çift,
ama her darbe iki kat uzun,
bu yüzden tonu bir oktav daha pes.

<!-- S09 -->
Yaklaşık bin dört yüz biti
her saniye gönderirsen,
az önce duyduğun sesi elde edersin.

<!-- S09b -->
Bu ayrıca şu demek: sıfırlarla dolu bir program
birlerle dolu olandan daha hızlı yüklenir.
Her birin gönderilmesi iki kat uzun sürer.

<!-- S10 -->
Gerçi Amerika'da büyüdüysen,
bu sesi hiç duymamış olabilirsin.

<!-- S11 -->
Ki bu tuhaf,
çünkü fikir aslında Amerika'dan çıkmıştı.

<!-- S12 -->
1975'te Kansas City'deki bir toplantıda
bilgisayar meraklıları bir yöntemde uzlaştı:
verileri ses olarak
sıradan ses kasetlerine kaydetmek.

<!-- S12b -->
Bir biti, sekiz hızlı döngüden oluşuyordu,
yüksek bir tonda,
sıfır biti ise alçak tonda dört yavaş döngüden.
Saniyede üç yüz bit.

<!-- S13 -->
Apple II gibi ilk makineler
ve TRS-80,
programlarını
sıradan teyplere kaydediyordu.

<!-- S14 -->
Ama Amerika'da ev bilgisayarları
hızla bir sonraki aşamaya geçti.

<!-- S15 -->
1983'te bir dergi bir anket yayımladı:
yeni Commodore 64 sahiplerinin onda dokuzu
bir disket sürücüsünü de
bilgisayarla birlikte alıyordu.

<!-- S16 -->
İngiltere'de ise işler tam tersine gelişti.

<!-- S17 -->
Spectrum yüz
yirmi beş sterlindi
ve hiçbir depolama birimiyle gelmiyordu.
Evde zaten hangi kasetçalar varsa
onu kullanıyordun.

<!-- S18 -->
Yani Avrupa'daki milyonlarca çocuk için
bu ses,
başlamak üzere olan bir oyunun sesiydi.

<!-- S18b -->
Yeterince yükleme yaptıktan sonra
hangi oyun olduğunu bile anlayabiliyordun,
sadece o cızırtıdan.

<!-- S19 -->
Hadi bir oyunu
kasetten bilgisayara kadar takip edelim.

<!-- S20 -->
LOAD yazıyorsun, enter'a basıyorsun
ve play'e basıyorsun.

<!-- S21 -->
Önce sabit bir uğultu geliyor,
saniyede sekiz yüz döngü,
yaklaşık beş saniye boyunca.

<!-- S22 -->
Hiç veri taşımıyor.
Orada olmasının sebebi, bilgisayarın
sinyali bulabilmesi
ve ritmine kilitlenebilmesi.

<!-- S23 -->
Sonra iki hızlı darbe: senkron.
Anlamları şu: buradan sonrası veri.

<!-- S24 -->
İlk gelen şey
kısa bir başlık.
On dokuz bayt:
en fazla on harflik bir ad,
dosyanın türü
ve ne kadar uzun olacağı.

<!-- S25 -->
Sonra ikinci, daha kısa bir uğultu,
bu sefer iki saniye,
ve ardından oyunun kendisi.

<!-- S26 -->
Her bayt bu notalardan sekiz tanesi,
art arda,
baytlar arasında hiç boşluk olmadan.

<!-- S27 -->
Ve bilgisayar nota duymuyor.
Sinyalin bir kenarıyla bir sonraki kenarı
arasındaki süreyi ölçüyor.

<!-- S28 -->
Kısa bir çift sıfırdır.
Uzun bir çift birdir.

<!-- S28a -->
Kod çözücünün tamamı bu.

<!-- S28b -->
Ve bu videonun başındaki ses
bir ses efekti değil.
Onu tam olarak bu kurallarla ürettik
ve içinde gerçek bir Spectrum programı var.

<!-- S28c -->
Tamamını videonun en sonunda çalacağız.
Kaydet, bir Spectrum onu yükleyecektir.

<!-- S29 -->
Çoğu oyun önce bir resim gösterirdi
ve bu resim tuhaf bir sırayla yüklenirdi.

<!-- S30 -->
Sekiz satır arayla ince çizgiler belirir,
sonra satır satır dolardı,
her seferinde ekranın üçte biri.
Renkler ise en son gelirdi,
her şeyin üzerinden aşağı doğru süzülerek.

<!-- S31 -->
Sadece o resim
yaklaşık kırk saniye sürüyordu.
Oyunun tamamı ise beş dakika kadar.

<!-- S32 -->
Ve her bloğun sonunda
bir bayt daha gelir.

<!-- S33 -->
Kaydederken Spectrum
bloğun her baytını
XOR denen basit bir kuraldan geçirir
ve sonucu fazladan bir bayt olarak kaydeder.

<!-- S34 -->
Yüklerken hesabı tekrarlar.
Sonuçlar tutarsa,
blok sağlam gelmiş demektir.

<!-- S35 -->
Tutmazsa, Spectrum şunu söyler.

<!-- S36 -->
Beş dakikalık bekleyiş,
ve tek bir bayt
hepsinin boşa gittiğine karar verir.
Geri sar ve baştan başla.

<!-- S37 -->
İşin garibi, bozuk bir başlık
hiç hata vermez.
Spectrum onu görmezden gelir
ve sıradakini dinlemeye devam eder.

<!-- S38 -->
Diğer bilgisayarlar başka yollar denedi.

<!-- S39 -->
Commodore 64
her bloğu iki kez kaydederdi,
böylece bir kopyadaki hasarlı bir yer
diğerinden kurtarılabilirdi.

<!-- S40 -->
Daha güvenli ama yavaş.
Commodore'un yerleşik rutiniyle
kırk kilobaytlık bir program
yaklaşık on iki buçuk dakika sürerdi.

<!-- S41 -->
Bu yüzden oyun yayıncıları
kendi hızlı yükleyicilerini yazdı;
bazıları yaklaşık on kata kadar hızlıydı.

<!-- S42 -->
Bir de kasetçaların kendisi vardı.

<!-- S43 -->
Ses çok kısıksa
kenarlar hışırtıda kaybolur.
Çok yüksekse
birbirine karışır.

<!-- S44 -->
Biraz hızlı ya da yavaş dönen bir bant
her darbeyi esnetir,
oysa bilgisayar zamanı ölçüyor.

<!-- S45 -->
En kötüsü azimuttu,
yani kafanın açısı.
Bir makinede kaydedilen bant
başka bir makineyle hizalanmayabilirdi.

<!-- S46 -->
Bu yüzden insanlar minik bir tornavidayı
kafanın yanındaki bir deliğe sokar,
azar azar çevirir
ve dinlerdi.

<!-- S47 -->
Batıl inanç gibi görünüyordu.
Aslında sinyal ayarıydı.

<!-- S48 -->
Ama kasetçaların asla
yapmak zorunda olmadığı şeye dikkat et.

<!-- S49 -->
Tek bir biti bile anlamadı.
Sesi kaydetti
ve sonra çaldı.

<!-- S50 -->
Yani bir programın
aslında kasete ihtiyacı yoktu.
Sesi taşıyabilen her şey
yazılımı da taşıyabilirdi.

<!-- S50b -->
Bu, bir oyunu kopyalamanın da
bir albüm kopyalamak kadar kolay olduğu anlamına geliyordu.
İki kasetçalar ve bir kablo.

<!-- S51 -->
Atari iki stereo kanalı da kullandı.
Birinde program,
diğerinde ise bir anlatıcı sesi;
televizyondan seninle konuşurdu,
oyun yüklenirken.

<!-- S52 -->
Yugoslavya'da Radyo Belgrad'daki bir yayın
bilgisayar programlarını havadan yayınlardı.

<!-- S53 -->
Dinleyiciler bunları banda kaydederdi;
yaklaşık yüz elli program,
1983 ile 1986 arasında.

<!-- S54 -->
Çekoslovakya'da ise televizyondu.
Bir program ses olarak çalardı,
kapanış jeneriğinin altında.

<!-- S55 -->
Ve 1983'te şarkıcı Pete Shelley
bir Spectrum programını
bir plak albümünün sonuna gizledi.

<!-- S56 -->
Onu banda kopyala, yükle,
şarkı sözleri ekranda belirir,
şarkılarla eş zamanlı.

<!-- S57 -->
Ama bir sorun vardı.

<!-- S58 -->
Radyo, sesi
ülkedeki her bilgisayara ulaştırabilirdi.
Ama onu yalnızca doğru bilgisayar anlayabilirdi.

<!-- S59 -->
Bir Spectrum oyununu Commodore'a çal,
Commodore yalnızca gürültü duyar.
Bitler yalnızca
formatı bilen bir makine için anlam taşır.

<!-- S60 -->
Bu yüzden Hollanda radyosu bunu çözmeyi denedi.
1982'de BASICODE'u yarattı:
tek bir ses formatı
ve her bilgisayar türü için
küçük bir çevirici program.

<!-- S61 -->
Ve bu sorun hiç ortadan kalkmadı.
Bir dosya ancak, onu hâlâ
okuyabilen bir şey varsa işe yarar.

<!-- S62 -->
Kasetler tabii ki kaybetti.
Disketler daha hızlıydı,
sonra sabit diskler, sonra flash bellek.

<!-- S63 -->
Ne var ki bant aslında hiç gitmedi.
Veri merkezleri hâlâ
arşivlerini manyetik bantta saklıyor.

<!-- S64 -->
Modern bir LTO-9 kartuşu
on sekiz terabayt alıyor.

<!-- S65 -->
Spectrum hızına çevrildiğinde
bu kapasite kabaca
yirmi dokuz milyon kaseti doldurur
ve yüklenmesi üç bin
yıldan fazla sürer.

<!-- S66 -->
Yine de fikir aynı.
Hareket eden bir bant üzerindeki desenler,
ihtiyaç duyduğunda
yeniden sayılara dönüşüyor.

<!-- S67 -->
Bir dahaki sefere o cızırtıyı duyduğunda
ne olduğunu hatırla.
Gürültü değil.
Ses olarak yolculuk eden bir program.

<!-- S68 -->
Ve 1985'te bir yerde
bir çocuk televizyonun karşısında oturmuş,
sesin bitmesini bekliyor.
Çünkü ses bittiğinde
oyun başlıyor.

<!-- S69 -->
O zaman sana bir sorum var.
Hiç kasetten oyun yüklediysen,
en çok neyi hatırlıyorsun?
Yorumlarda yaz.

<!-- S70 -->
Ve söz verdiğimiz gibi, işte o program.
Tıpkı Çekoslovak televizyonu gibi
onu kapanış jeneriğinin altına koyduk.
