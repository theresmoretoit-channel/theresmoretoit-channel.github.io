<!-- S01 -->
19 Temmuz 2024'te
CrowdStrike adlı bir güvenlik şirketi
sıradan bir güncelleme gönderdi.

<!-- S02 -->
Yeni bir program değil.
Sadece küçük bir yapılandırma dosyası.

<!-- S03 -->
Birkaç saat içinde 8,5 milyon
Windows bilgisayar
mavi ekranda durmuştu.

<!-- S04 -->
Havayolları uçuşları durdurdu.
Hastaneler ameliyatları iptal etti.
Bir haber kanalı yayından düştü.

<!-- S05 -->
Ve bunun arkasındaki hata
gayet sıradandı.
Program 20 veri bekliyordu.
Güncelleme ona 21 tane verdi.

<!-- S06 -->
Oyunların ve uygulamaların
böyle hataları sürekli yapar.
Yaptıklarında oyun kapanır,
sen de onu yeniden açarsın.

<!-- S07 -->
Aynı türden bir hata.
Biri bir pencereyi kapatıyor.
Öbürü
8,5 milyon makineyi durduruyor.

<!-- S08 -->
Fark hatanın kendisinde değil.
Kodun çalıştığı yerde.

<!-- S09 -->
Peki neden tek bir program
bilgisayarını ele geçiremez...
ve bu neden geçirebildi?

<!-- S10 -->
Her zaman böyle değildi.

<!-- S11 -->
1980'lerde DOS çalıştıran bir PC'de
işlemcide bir programı durduracak hiçbir şey yoktu.
Program belleğin istediği yerine yazabilir
ve donanımla doğrudan konuşabilirdi.

<!-- S12 -->
Tek bir programın
yazmaması gereken bir yere yazması
işletim sisteminin üzerine yazmasına yeterdi,
ve bütün makine donardı.

<!-- S13 -->
Çözüm, programlara güvenmeyi bırakmak
ve şüphelenme işini
işlemciye bırakmaktı.

<!-- S14 -->
1982'de Intel'in 80286 işlemcisi
korumalı modu getirdi,
dört yetki seviyesiyle birlikte.

<!-- S15 -->
Genellikle
iç içe dört halka olarak çizilirler.

<!-- S16 -->
Ring 0 merkezdedir.
Ring 3 en dıştadır.

<!-- S17 -->
Ve numaralar tersten gider.
Numara ne kadar küçükse,
kodun yapabildikleri o kadar fazladır.

<!-- S18 -->
Ring 0 çekirdeğe aittir,
yani işletim sisteminin kalbine.
Belleği dağıtır,
sırada hangi programın çalışacağına karar verir
ve donanımla konuşur.

<!-- S19 -->
Ring 3'te tarayıcın,
oyunların ve metin düzenleyicin çalışır.
Buna kullanıcı modu denir.

<!-- S19b -->
Windows, macOS ve Linux
işi hep bu şekilde bölüşür.
Çekirdek Ring 0'da,
uygulamaların Ring 3'te.

<!-- S19c -->
Telefonlar ve Apple'ın yeni Mac'leri
bunun yerine ARM çipler kullanır.
Orada seviyelere exception level denir.
Adı farklı, bölünme aynı:
biri çekirdek için, biri uygulamaların için.

<!-- S20 -->
İşlemci her zaman
hangi ringde çalıştığını bilir.
Ve bunu kontrol eder.

<!-- S21 -->
Bazı komutlar yalnızca Ring 0'da çalışır.
Örneğin kesmeleri kapatmak
ya da belleğin nasıl eşlendiğini değiştirmek.

<!-- S22 -->
Ring 3'teki bir program bunlardan birini denerse,
işlemci reddeder.
Bir istisna oluşturur
ve kontrolü çekirdeğe verir,
çekirdek de genellikle programı sonlandırır.

<!-- S23 -->
Bellek de aynı muameleyi görür.
Her bellek sayfası
ya user ya da supervisor olarak işaretlidir.

<!-- S24 -->
Ring 3'teki bir program
bir supervisor sayfasına dokunursa
veriyi alamaz.
Durdurulur.

<!-- S25 -->
Tarayıcın da oyunun da
Ring 3'te çalışır.
Onları birbirinden ayıran şey,
her birinin kendi bellek haritası olması.
Öbür programın belleği
bu haritada hiç yer almaz.

<!-- S26 -->
Yani bir oyun çöktüğünde
hasar oyunun içinde kalır.
Çekirdek ortalığı toplar.
Geri kalan her şey çalışmaya devam eder.

<!-- S27 -->
Şimdi CrowdStrike'a tekrar bak.
Onun sürücüsü Ring 0'da çalışıyordu,
çekirdeğin hemen yanında.

<!-- S28 -->
Ring 0'ın üstünde
böyle bir hatayı yakalayabilecek hiçbir şey yok.

<!-- S29 -->
Bu yüzden Windows geriye kalan tek güvenli şeyi yaptı.
Bütün makineyi bilerek durdurdu,
artık güvenemediği bir bellekle
devam etmek yerine.

<!-- S30 -->
Mavi ekran tam olarak budur.

<!-- S31 -->
Ve sürücü
Windows her açıldığında başladığı için,
her yeniden başlatma çökmeyi geri getirdi.

<!-- S32 -->
Ama bu bir soruyu akla getiriyor.
Tarayıcın donanıma dokunamıyorsa,
bir dosyayı nasıl kaydediyor
ya da ağ üzerinden bir şey nasıl gönderiyor?

<!-- S33 -->
Rica ediyor.

<!-- S34 -->
Program isteğini
işlemcinin yazmaçlarına koyar.
Hangi dosya. Veri nereye gidecek.
Ne kadar.

<!-- S35 -->
Sonra özel bir komut çalıştırır.
Modern bir PC'de bunun adı SYSCALL.

<!-- S36 -->
O anda işlemci
Ring 3'ten Ring 0'a geçer...

<!-- S37 -->
ama programın istediği
yere atlamaz.
Çekirdeğin önceden seçtiği
tek bir giriş noktasına atlar.

<!-- S38 -->
Çekirdek isteği kontrol eder,
işi yapar
ve Ring 3'e geri döner.
Program diske hiçbir zaman kendisi dokunmadı.

<!-- S39 -->
Buna sistem çağrısı denir,
ve sürekli olur.

<!-- S40 -->
Bunları bir dizüstü bilgisayarda saydık.
Hiçbir şey yapmayan bir program bile
30 tane yapıyor.

<!-- S41 -->
Firefox açılırken
ve tek bir Wikipedia sayfası yüklerken
yaklaşık 670 bin tane yaptı,
20 saniyede...
üstelik bizim saymamız onu yavaşlatırken.

<!-- S42 -->
Bunların her biri
duvardan geçip geri dönen bir yolculuk.

<!-- S43 -->
Geriye tuhaf bir şey kalıyor.
Dört ring var,
ama bize yalnızca ikisi lazım oldu.

<!-- S44 -->
Ring 1 ve 2'ye ne oldu?

<!-- S45 -->
Ring fikri PC'den daha eski.
1960'ların sonundan
bir işletim sistemi olan Multics'in
sekiz ringi vardı.

<!-- S46 -->
Fikir, güven katmanlarıydı.
Sistemin çekirdeği ortada,
daha az güvenilen hizmetler onun çevresinde,
programlar da en dışta.

<!-- S46b -->
Intel de aynı resmi çizdi.
Ring 1 ve 2,
aradaki katmanlar için düşünülmüştü,
mesela sürücüler ve sistem hizmetleri.
Uygulamalarından daha güvenilir,
çekirdekten daha az güvenilir.

<!-- S47 -->
İki şey buna engel oldu.

<!-- S48 -->
Birincisi, Unix ve Windows NT gibi sistemler
pek çok farklı işlemcide
çalışacak şekilde tasarlanmıştı.

<!-- S49 -->
Ve her işlemcinin sunduğu
tek bölünme
iki seviyeydi.
Biri çekirdek için,
biri geri kalan her şey için.

<!-- S50 -->
İkincisi, x86 işlemcinin kendisi.
Belleği eşlerken
her sayfa yalnızca iki durum bilir.
User ya da supervisor.

<!-- S51 -->
Ring 1 ve 2 supervisor sayılır.
Yani Ring 1'deki bir sürücü
yine de çekirdeğin belleğine dokunabilirdi.
Fazladan ring pek bir şey korumazdı.

<!-- S51b -->
Yine de birkaç sistem bunları kullandı.
OS/2 bazı programların Ring 2'ye geçmesine izin verdi,
sadece donanımla doğrudan konuşabilsinler diye.

<!-- S51c -->
Ve işlemcilerde sanal makine çalıştırmak için
bir destek olmadan önce,
Xen ve VirtualBox misafir sistemin çekirdeğini
Ring 1'e taşıyordu,
böylece alttaki sistem
Ring 0'ı kendine saklayabiliyordu.

<!-- S52 -->
2023'te Intel,
Ring 1 ve 2'yi tamamen kaldırmayı önerdi.

<!-- S53 -->
Aralık 2024'te bu plandan vazgeçti.
Hâlâ işlemcinde duruyorlar.
Neredeyse hiçbir şey onları kullanmıyor.

<!-- S54 -->
Buraya kadar kulağa güven verici geliyor.
Kurallar donanımda,
ve donanım her erişimi kontrol ediyor.

<!-- S55 -->
2017'de üç araştırmacı ekibi,
birbirinden bağımsız çalışarak,
o duvardan geçmenin bir yolunu buldu.

<!-- S56 -->
Buna Meltdown adını verdiler.
Ve bunu takip edebilmek için
modern işlemcilerin yaptığı
bir numarayı bilmen gerekiyor.

<!-- S57 -->
Bir işlemci,
bir komutun bitmesini beklemeden
sonrakine başlar.
Önden gider,
muhtemelen ihtiyaç duyacağı komutları yürütür.

<!-- S58 -->
Tahmini yanlış çıkarsa
sonuçları atar,
sanki hiçbir şey olmamış gibi.

<!-- S59 -->
İşte kusur burada.
Etkilenen Intel çiplerinde
Ring 3'teki bir program
çekirdek belleğinden bir bayt isteyebiliyordu...

<!-- S60 -->
ve işlemci onu getirip
sonraki komutlara aktarıyordu,
buna izin olup olmadığını
kontrol etmeyi bitirmeden önce.

<!-- S61 -->
Kontrol gerçekten başarısız oluyordu.
Sonuç atılıyordu.

<!-- S62 -->
Ama o sonraki komutlar
gizli baytı çoktan kullanmıştı,
programın kendi belleğinden
bir parçayı
işlemcinin önbelleğine çekmek için.

<!-- S63 -->
Ve önbellek, sonuç iptal edildi diye
unutmaz.

<!-- S64 -->
Böylece program,
belleğinin her parçasının ne kadar hızlı yanıt verdiğini ölçer.
Hızlı yanıt veren parça
gizli baytı ele verir.

<!-- S65 -->
Bayt bayt,
sıradan bir program
çekirdeğin belleğini
ve içindeki tüm sırları okuyabiliyordu.
Parolalar ve şifreleme anahtarları dahil.

<!-- S66 -->
Meltdown, 1995'e kadar uzanan
Intel işlemcileri etkiliyordu.

<!-- S67 -->
Kamuoyuna
3 Ocak 2018'de duyuruldu.

<!-- S68 -->
Düzeltme silisyumu değiştiremezdi.
Bu yüzden işletim sistemleri haritayı değiştirdi.

<!-- S69 -->
Programın çalışırken
çekirdeğin belleği artık
onun haritasından neredeyse tamamen çıkarılıyor.
Orada getirilecek bir şey yok.

<!-- S70 -->
Ama sistem çağrılarını hatırla.
Duvardan her geçiş
artık haritayı da değiştirmek zorunda.

<!-- S71 -->
Red Hat, Meltdown ve onunla bağlantılı bir açık olan
Spectre için yamaları ölçtü.
Bazı işlerde %1'in altında...
yoğun veritabanlarında %19'a kadar.

<!-- S72 -->
Kural başından beri doğruydu.
İşlemci sadece onu çok geç kontrol ediyordu.

<!-- S73 -->
Bu da bizi CrowdStrike'a,
ve daha zor bir soruya geri getiriyor.

<!-- S74 -->
Bir güvenlik programı
neden en başta Ring 0'daydı?

<!-- S75 -->
Çünkü oradan her şeyi görür.
Diğer yazılımlardan önce başlar.
Ve yönetici yetkisine sahip kötü amaçlı yazılım
onu kapatmakta daha çok zorlanır.

<!-- S76 -->
Microsoft'un kendi listesi
bir uyarıyla bitiyor.
Çekirdek sürücüleri bunu dayanıklılık pahasına sağlar.

<!-- S77 -->
Kesintiden sonra
Microsoft, antivirüs yazılımlarının
çekirdeğin dışında çalışabilmesi için
bir yol geliştirmeye başladı.

<!-- S78 -->
2026 sonbaharında
bu hâlâ yalnızca Windows'un test sürümlerinde.
Ve çekirdek
güvenlik şirketlerine kapatılmış değil.

<!-- S79 -->
Oyunların da aynı ikilemle karşı karşıya.

<!-- S80 -->
Çekirdekte çalışan hileler,
Ring 3'te çalışan
bir hile önleyiciye görünmez.

<!-- S81 -->
Bu yüzden hile önleyici de oraya taşındı.
Valorant'ın kullandığı Riot'un Vanguard'ı
Ring 0'a bir sürücü yerleştirir.
Çoğu PC'de Windows açılırken yüklenir...
oyunu hiç açmasan bile.

<!-- S82 -->
Bu onu hatalı yapmaz.
Ama CrowdStrike sürücüsünün durduğu
aynı yerde duruyor,
tek bir hatanın bütün makineyi durdurduğu yerde.

<!-- S83 -->
Peki neden tek bir program
bilgisayarını ele geçiremez?

<!-- S84 -->
Çünkü işlemci
neredeyse her programı merkezden uzak tutar
ve kapıyı her çaldıklarında onları kontrol eder.

<!-- S85 -->
Ama içeri kimin alınacağına
işlemci karar veremez.
Buna insanlar karar verir...
her sürücü kurduklarında.

<!-- S86 -->
O zaman yorumlara bir soru.
Hangi programların Ring 0'a
gireceğine kim karar vermeli:
sen mi, Microsoft mu,
yoksa onları yapan şirketler mi?
