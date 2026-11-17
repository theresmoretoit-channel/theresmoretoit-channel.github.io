<!-- S01 -->
Yepyeni bir disk alıyorsun.
Bir terabayt, tamamen boş.
Tek bir dosya bile tutabilmesi için
önce biçimlendirilmesi gerekiyor.

<!-- S02 -->
Sen de onu ext4 ile biçimlendiriyorsun,
yani birçok Linux bilgisayarındaki
standart dosya sistemiyle.
Varsayılan ayarlarla,
daha hiçbir şey kaydetmeden,
yaklaşık on yedi gigabayt gitmiş bile.

<!-- S03 -->
Henüz hiçbir şey kaydedilmedi.
Ne fotoğraf var, ne belge.
Peki bütün o yeri ne kaplıyor?

<!-- S04 -->
Hem bir disk neden
biçimlendirilmeye ihtiyaç duyar ki?
Zaten veri saklayabiliyor.
Trilyonlarca biti okuyup yazabiliyor.

<!-- S05 -->
Bilgisayar neden hemen yazmaya başlamasın,
nerede boş yer varsa oraya?

<!-- S06 -->
Çünkü veriyi saklamak
ve onu yeniden bulmak
birbirinden çok farklı iki sorun.

<!-- S07 -->
Bir ofis düşün; dağıttığı şey
form değil, boş kâğıt.
Her şey bir yerlere yazılıyor...
ama kimse hiçbir şeyi bulamıyor.

<!-- S08 -->
Dosya sistemi olmayan bir disk
işte o kâğıt yığını.
Ama daha iyi bir benzetme
bir defter.

<!-- S09 -->
Bir defter düşün,
bin sayfalık bir defter,
ve onu kullanmak için birkaç kural.

<!-- S10 -->
Birincisi, her sayfanın bir numarası var.
Böylece defterdeki her yerin
bir adresi oluyor.
Dört yüz on ikinci sayfa
tam olarak tek bir yer demek.

<!-- S11 -->
İkincisi, ilk birkaç sayfa
bir içindekiler tablosu.
Her maddede bir ad var
ve onun bulunduğu sayfa.
Krep: on ikinci sayfa.

<!-- S12 -->
Üçüncüsü, en arkada
hâlâ boş olan sayfaların
bir listesi var.

<!-- S13 -->
Şimdi bir tarif ekle.
Boş bir sayfa için arkadaki listeye bakıyorsun.
Tarifi oraya yazıyorsun.
İçindekilere bir satır ekliyorsun.
Ve o sayfanın üstünü
boş sayfalar listesinde çiziyorsun.

<!-- S14 -->
Tek tarif, üç yer.
Ve üçünün de birbirini tutması gerekiyor.

<!-- S15 -->
Sonra krep tarifi uzuyor.
On ikinci sayfa dolu,
on üçüncü sayfa da zaten kullanılıyor.
Bu yüzden tarif seksen yedinci sayfada devam ediyor,
ve içindekiler bunu belirtmek zorunda.

<!-- S16 -->
İşte işin can sıkıcı yanı.
Bin madde için yer istiyorsan
içindekiler tablosunda,
o sayfaları ayırman gerekiyor,
daha tek bir tarif yazmadan önce.

<!-- S17 -->
Benzetme bu kadar.
Şimdi diskte gerçekte ne olduğuna bakalım.

<!-- S18 -->
Disk dosyaları,
klasörleri ya da adları bilmez.
Sunduğu tek şey, uzun bir sıra halinde
numaralı yuvalar; bunlara sektör denir.

<!-- S19 -->
Sabit diskte
veri, dönen plakaların üzerinde durur.
SSD ise onu flaş bellekte tutar.
Her iki durumda da bilgisayar yalnızca
bir sektörü numarasıyla ister,
o sektörün nerede olduğunu disk kendisi bulur.

<!-- S20 -->
Sektör küçüktür.
Genellikle 512 bayt,
ya da 4.096,
daha yeni disklerde.

<!-- S21 -->
Dosya sistemleri genellikle
blok denen daha büyük parçalarla çalışır.
Ext4'te bir blok dört kilobayttır,
yani eski tip sekiz sektör büyüklüğünde.

<!-- S22 -->
Bu numaralı bloklar
defterin sayfaları.
Dosya sisteminin hâlâ ihtiyaç duyduğu şey
diğer iki parça:
bir içindekiler tablosu
ve neyin boş olduğunu gösteren bir liste.

<!-- S23 -->
Biçimlendirme işte bunları kurar.
Ve o on yedi gigabayt
işte buraya gitti.

<!-- S24 -->
Ext4, diskin aynı anda tutabileceği
her dosya ve klasör için
önceden bir kayıt ayırır.
Her kayıt
256 bayttır.
Buna inode denir.

<!-- S25 -->
Bir gün her inode şunları söyleyecek:
dosyanın ne kadar büyük olduğunu,
ne zaman değiştirildiğini,
kimin açabileceğini
ve içeriğini hangi blokların tuttuğunu.

<!-- S26 -->
Bir terabaytlık diskte
ext4 bunlardan yaklaşık
altmış bir milyon tane hazırlar.
Hepsi boş, hepsi bekliyor.
Bu, neredeyse on altı gigabayt
boş kayıt demek.

<!-- S27 -->
Neden altmış bir milyon?
Ext4 basit bir tahmin yapar:
diskteki her on altı kilobaytlık
alan için bir inode.
Sıradan bir bilgisayarda
bu kayıtların çoğu
hiç kullanılmayacak.

<!-- S28 -->
Yaklaşık bir gigabayt daha
günlüğe gider,
ona daha sonra döneceğiz.
Gerisi başka kayıt tutma işleri,
blok başına bir bit içeren bir harita da dahil;
bu bit, bloğun dolu mu boş mu olduğunu söyler.

<!-- S29 -->
Bu sayı da sabittir.
Bütün kayıtları tüket
milyonlarca minik dosyayla,
ve disk sana dolu olduğunu söyler...
gigabaytlarca boş yer kalmış olsa bile.

<!-- S30 -->
Hadi nasıl çalıştığını izleyelim.
hello.txt adında bir dosya oluşturacağız.
İçinde tek bir kelime var: hello.
Beş harf. Beş bayt.

<!-- S31 -->
Dosya sistemi boş bir inode seçer.
Diyelim ki on üç numara.
Sonra haritada boş bir blok bulur
ve onu kullanılıyor olarak işaretler.

<!-- S32 -->
Beş baytı o bloğa yazar.
Sonra inode'u doldurur:
beş bayt uzunluğunda, az önce oluşturuldu
ve o tek blokta saklanıyor.

<!-- S33 -->
Ve son olarak klasöre
tek bir satır ekler:
hello.txt adı
ve on üç numarası.

<!-- S34 -->
Adın nereye gittiğine dikkat et.
Dosyaya değil.
Inode'a da değil.
Ad, klasörde yaşar;
klasör de aslında sadece
adlardan ve numaralardan oluşan bir liste.

<!-- S35 -->
Ve klasör de sadece başka bir dosyadır.
Bir tek içinde
o liste vardır.

<!-- S36 -->
Bu yüzden bir dosyayı taşımak da,
aynı dosya sistemindeki başka bir klasöre,
ne kadar büyük olursa olsun anında olur.
Bir klasör bir satır kaybeder,
diğeri bir satır kazanır,
ve genellikle içerik
yerinden hiç kıpırdamaz.

<!-- S37 -->
Beş baytlık metin...
ama diskte kapladığı yer
4.096.
Blok, dosya sisteminin dağıttığı
en küçük parçadır,
bu yüzden minik bir dosya bile koca bir blok tüketir.

<!-- S38 -->
Dosya bloğuna sığmaz olunca,
dosya sistemi başka bir boş blok bulur.
Belki hemen yanında.
Belki bambaşka bir yerde.
Ve inode ikisini de takip eder.

<!-- S39 -->
Zamanla büyük bir dosya
diskin dört bir yanına parça parça dağılabilir.
Sabit disk bu parçalar arasında atlamak zorunda kalır.
SSD bununla çok daha iyi başa çıkar.

<!-- S40 -->
Dosyayı kaydeden program
bunların hiçbirini bilmez.
O sadece "hello.txt'yi kaydet" dedi,
gerisi hep perde arkasında oldu.

<!-- S41 -->
Şimdi onu sil.
Ad klasörden kaldırılır.
Inode boş olarak işaretlenir.
Blok, boş bloklar listesine geri döner.

<!-- S42 -->
Geleneksel bir sabit diskte
o beş baytın kendisi yerinde kalır.
Kimse onlara dokunmadı.
Orada kalırlar, ta ki yeni bir şey
üzerlerine yazılana kadar.

<!-- S43 -->
Bu yüzden silinmiş bir dosya
bazen kurtarılabilir.
Silme işlemi genellikle
içeriği ortadan kaldırmaz.
Sadece alanı kullanılabilir olarak işaretler.

<!-- S44 -->
SSD'de durum daha belirsiz.
Dosya sistemi diske
o blokların artık gerekmediğini söyleyebilir,
disk de içlerindekini atabilir.
Ondan sonra dosyayı geri getirme ihtimali
çok daha düşük.

<!-- S45 -->
Yani dosya sistemi aslında bir muhasebeci.
Bu tek dosyayı oluşturmak
üç şeyi güncellemek demekti:
klasörü, inode'u
ve boş blok haritasını.

<!-- S46 -->
Şimdi elektriği kes,
tam bir dosya kaydedilirken.

<!-- S47 -->
Belki blok kullanılıyor diye işaretlendi,
ama henüz hiçbir inode onu göstermiyor.
O alan düpedüz kaybolur.
Can sıkıcı ama zararsız.

<!-- S48 -->
Ya da belki inode, haritanın
hâlâ boş saydığı bir bloğu gösteriyor.
Sonraki dosya
tam onun üstüne yazılabilir.
Ve ilk dosya sessizce yok olur.

<!-- S49 -->
Ext4'ün bir günlük tutmasının sebebi bu.
Kayıtlarını değiştirmeden önce
ne yapmak üzere olduğunu not eder.
Bir çökmeden sonra yalnızca,
not almayı bitirip tamamlandı olarak işaretlediği
değişiklikleri yeniden uygular.
Yarım kalan her şey yok sayılır.

<!-- S50 -->
Bir de daha sessiz bir sorun var.
Bazen bir disk bir biti değiştirir
ve kimseye söylemez.

<!-- S51 -->
Ext4 kendi kayıtlarını
sağlama toplamlarıyla korur,
böylece oradaki hasarı fark edebilir.
Peki ya dosyalarının içeriği?
Ona düpedüz güvenir.

<!-- S52 -->
Bazı dosya sistemleri ikisini de denetler.
Bazıları da ikinci bir kopya tutar,
böylece bir kopya bozulduğunda
onu diğerinden onarabilirler.
Sorunu fark etmek ve onu düzeltmek
aynı şey değil.

<!-- S53 -->
Yani her dosya sistemi aynı işi yapar:
numaralı bloklar, bir ad listesi
ve neyin boş olduğunu gösteren bir harita.

<!-- S54 -->
Ama tercihler farklı.
Ext4 altmış bir milyon kayıt hazırlar,
sen daha hiçbir şey kaydetmeden.
Windows'taki NTFS ise kayıtlarını
kullandıkça büyüyen tek bir büyük tabloda tutar.

<!-- S55 -->
Btrfs ise önceden
sabit bir inode tablosu hazırlamaz.
Onları dosyalar geldikçe oluşturur.
Ve normalde mevcut verinin
olduğu yerde üzerine yazmaz.
Yeni bir kopya yazar
ve ancak ondan sonra eskisini bırakır.

<!-- S56 -->
Varsayılan olarak dosyalarının sağlama toplamını da tutar,
böylece hasar gördüklerinde bunu anlayabilir.

<!-- S57 -->
Ve eski kopyanın
üzerine yazılmadığı için
bir anlık görüntü onu hayatta tutabilir.
Bu da bu videodaki
neredeyse her sorunun cevabını değiştirir:
bir çökmenin ne yaptığını,
silmenin ne anlama geldiğini,
hatta kopyanın ne olduğunu bile.

<!-- S58 -->
Bir sonraki video tam da buradan başlıyor.

<!-- S59 -->
O zaman sana bir sorum var.
Bir dosya sistemi dosyalarını sadece saklamalı mı,
yoksa onları korumalı da mı?
Yorumlarda bana yaz.
