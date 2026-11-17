<!-- S01 -->
Diyelim ki çılgın bir fikrin var.
Kendi uydunu yapmak istiyorsun.
Milyar dolarlık bir
iletişim uydusu değil.
Küçük bir şey.

<!-- S02 -->
Bir somun ekmek
büyüklüğünde bir kutu.
İçinde: bir bilgisayar, güneş panelleri,
bir telsiz, birkaç sensör.
Hatta belki bir kamera.

<!-- S03 -->
Onu garajında yapıyorsun.
Ve sonra bir şekilde...
onu yörüngeye oturtuyorsun.
İmkânsız gibi geliyor.
Ama değil.

<!-- S04 -->
İnsanlar yıllardır neredeyse
tam da bunu yapıyor.
Bunlara CubeSat deniyor.

<!-- S05 -->
Ve şaşırtıcı olan şu:
en zor şey
uyduyu yapmak değil.
Geri kalan her şey.

<!-- S06 -->
Temel birime 1U deniyor —
yaklaşık on santimetrelik bir küp.
Birimleri üst üste dizersin,
2U, 3U, 6U
ve daha büyüğünü elde edersin.

<!-- S07 -->
Fikir basit.
Sıfırdan yeni bir uzay aracı
tasarlamak yerine,
standart boyutları
ve standart arayüzleri kullanırsın.
Ve birden uzay,
üniversitelere, girişimlere
ve hatta belki sana açılıyor.

<!-- S07b -->
Bu arada, bunun gibi videoları
seviyorsan, abone olmayı düşün.

Kanala gerçekten yardımı oluyor.

<!-- S08 -->
Peki bizim küçük uydumuz
aslında neler içerir?
Önce, bir bilgisayara ihtiyacı var.
Bir şey yazılımı çalıştırmalı,
donanımı kontrol etmeli
ve ne yapılacağına karar vermeli.

<!-- S09 -->
Sonra güç var.
Güneş panelleri elektrik üretir.
Bataryalar onu depolar,
uydu Dünya'nın gölgesine
kaydığı anlar için.

<!-- S10 -->
Sonra iletişim.
Bir telsiz. Bir anten.
Ve aşağıda, Dünya'da,
dinleyen bir yer istasyonu.

<!-- S11 -->
Sonra sensörler.
Sıcaklık. Voltaj. Akım.
İvme. Manyetik alan.
Ve uydunun ne yöne baktığını
anlamanın bir yolu.
Çünkü yörüngede
"yukarı" demek şaşırtıcı derecede zor.

<!-- S12 -->
Ama birini yapmadan önce,
sıkıntılı bir soru var.
Bu küçük kutu ne kadara mal olur?
Cevap şu...
göründüğünden daha fazlasına.

<!-- S13 -->
Basit bir 1U CubeSat
kolayca on binlerce dolara
mal olabilir —
sadece uçuş donanımıyla.
Güç sistemi. Güneş panelleri.
Bataryalar. Bilgisayar. Telsiz.
Yönelim kontrolü. Yapı.
Ve faydalı yük.

<!-- S14 -->
Sonra parça listesinde
olmayan şeyler gelir.
Test. Entegrasyon.
Dokümantasyon.
Yer istasyonu operasyonları.
Lisanslama.
Ve son olarak...
fırlatma.

<!-- S15 -->
Küçük bir CubeSat için paylaşımlı fırlatma
on binlerce dolara mal olabilir.
Daha büyük görevler ve büyük CubeSat'ler
yüz binlere ulaşır.
Ve bu sadece
o şeyi uzaya çıkarmak.

<!-- S16 -->
Ve şimdi
daha da saçma bir sorun.
O parçaları hatırlıyor musun?
Bütün bunlar tek bir küçük kutuya
nasıl sığar ki?

<!-- S17 -->
Uzayda, rastgele bir elektronik yığınına
yer yok.
Her santimetre önemli.
Her gram önemli.
Her watt önemli.
Uydu, bir roket fırlatmasından sağ çıkması gereken
üç boyutlu bir bulmaca.

<!-- S18 -->
Peki bütün bu parçaları
nereden buluyorsun?
Her şeyi kendin tasarlamak
zorunda değilsin.
Küçük uydular için bileşen satan
koca bir sektör var:
bilgisayarlar, güç sistemleri,
telsizler, antenler ve güneş panelleri.
Hatta özellikle CubeSat parçaları için
kurulmuş pazar yerleri var.

<!-- S18b -->
Ve parçalar da standart.
Birçoğu aynı kart formatını kullanır
ve öylece üst üste dizilir,
böylece farklı üreticilerin parçaları
tek bir birime oturur.
EnduroSat ve GomSpace gibi
şirketler bunları satıyor
ve tek bir alt sistem
birkaç binden
on binlerce dolara kadar tutabilir.

<!-- S19 -->
Ve bunlar egzotik
işlemciler değil.
Güncel bir CubeSat bilgisayarı
bir ARM Cortex-M7 kullanıyor,
tanıdık arayüzlerle —
SPI, I²C, UART ve CAN.

<!-- S19b -->
Ve bu özel bir uzay çipi değil.
Gerçek, hazır satılan bir kart,
elinde tutabileceğin türden.

<!-- S20 -->
Bir uzay aracının ham hızdan
daha önemli bir şeye ihtiyacı var:
öngörülebilir davranış,
düşük güç tüketimi ve güvenilirlik.
Daha zorlu görevler
ARM Cortex-A işlemciler kullanabilir —
hatta Linux bile.

<!-- S20b -->
Ama hızlı değil.
Tipik bir CubeSat bilgisayarı
birkaç yüz megahertzde çalışır.
Senin dizüstün
dört beş gigahertzde çalışıyor,
çok daha fazla çekirdekle.
Çok az güç tüketmek için
ham hızdan ödün verir.

<!-- S21 -->
Ve eğer bir programcıysan,
işte burada ilginçleşiyor.
Gizemli bir 'uzay dili'
kod yazmıyorsun.
Gömülü yazılım yazıyorsun.
Çoğu zaman C ya da C++ ile.

<!-- S22 -->
Doğrudan donanım üzerinde
çalışabilir,
ya da FreeRTOS, Zephyr veya RTEMS gibi
bir gerçek zamanlı işletim sisteminde.
Uzay araçları için geliştirilmiş
açık kaynaklı yazılım çatıları bile var.
Örneğin NASA'nın F Prime'ı,
gömülü ve uzay uçuşu sistemleri için
bir uçuş yazılımı çatısı.

<!-- S23 -->
Yani kodun
şuna benzer görünebilir.

<!-- S24 -->
Ama normal bir bilgisayardan
kocaman bir farkı var.
Ona SSH ile bağlanamıyorsun.
Hata ayıklayıcı takamıyorsun.
Ve yazılımın çökerse...
bilgisayarın
birkaç yüz kilometre yukarıda.

<!-- S25 -->
Bu yüzden watchdog'lara,
güvenli modlara, hata tespitine
ve otomatik kurtarmaya ihtiyacı var.
Bazı sorunları sen orada olmadan
kendi kendine çözmesi gerekiyor.

<!-- S25b -->
Ve bütün bunlara ihtiyaç duymasının
büyük bir nedeni radyasyon.
Uzayda kozmik ışınlar
bellekteki bir biti çevirebilir,
hatta bir çipi çökertebilir.
Ağır bir kalkan yok —
o çok fazla ağırlık yapardı.
Bunun yerine bilgisayar kendini izler,
hataları düzeltir
ve bir şey ters gidince kendini sıfırlar.

<!-- S26 -->
Ama onu gerçekten
fırlatmak istiyorsan...
işler ciddileşir.
Masanda çalışan bir parça
bir roket için otomatik olarak
hazır değildir.
Titreşime, vakuma,
aşırı sıcak ve soğuğa ve radyasyona
dayanması gerekir.

<!-- S27 -->
Şimdi, uydunun ne yöne baktığını
bilme sorununa
geri dönelim.
Onu uzayda takla atarken
gözünde canlandır.
Ne zemin var. Ne tavan.
GPS sana nerede olduğunu
söyleyebilir...
ama ne yöne dönük olduğunu
söyleyemez.

<!-- S28 -->
Bu yüzden uydular
jiroskopları, manyetometreleri
ve güneş sensörlerini birleştirir,
yönelimlerini hesaplamak için.
Ve sonra onu değiştirmeleri gerekir.
Yaygın bir numara
manyetorktur.

<!-- S29 -->
Dünya'nın manyetik alanıyla
etkileşerek
küçük bir tork oluşturur.
Bir roket motoru değil.
Uyduyu hareket ettirmez.
Sadece onu döndürür.
Ve bu, uyduyu
tam istediğin yere yöneltmeye
yeter.

<!-- S30 -->
Ama bunların hiçbiri
uyduyu yapma
nedenimiz değil.
Bir göreve ihtiyacımız var.
İşte faydalı yük bu.
Radyasyon ölç.
Dünya'yı fotoğrafla.
Atmosferi incele.
Yeni bir sensör dene.
Ya da sadece yeni bir teknolojinin
işe yaradığını kanıtla.

<!-- S31 -->
Uydunun kendisi
çoğunlukla faydalı yükü
hayatta tutmak için orada.
Ona güç ver. Onu yönlendir.
Sıcak tut.
Verisini depola.
Ve eve gönder.

<!-- S32 -->
Masaüstün kilitlenince,
onu yeniden başlatırsın.
Uydun kilitlenince...
Dünya'nın çevresinde sessizce dönen
çok pahalı bir nesnen olur.

<!-- S33 -->
Diyelim ki onu yaptık.
Her şey çalışıyor...
Bilgisayar açılıyor...
Telsiz konuşuyor.
Paneller güç üretiyor.
Faydalı yük çalışıyor...
Onu fırlatabilir miyiz?
...Henüz değil.

<!-- S34 -->
Bir uydunun, fırlatmadan sağ
çıkabileceğini kanıtlaması gerekir.
Bu da test demek.
Çok fazla test.

<!-- S35 -->
Önce, onu dev bir
sarsıcıya cıvatala.
Sonra onu sert sert salla...
İşte bu titreşim testi.
Roket fırlatmaları nazik değildir.
Şuna dayanması gerekir:
gürültüye, titreşime ve şoka,
hiçbir şey gevşemeden
ya da kırılmadan.
Her vida önemli.
Her konnektör önemli.
Her kablo parçası önemli.

<!-- S36 -->
Sonra vakum gelir.
Dünya'da hava ısıyı uzaklaştırır.
Uzayda hava yoktur.
Bir taraf aşırı sıcak olabilir,
diğeri aşırı soğuk,
ve elektronik parçalar
yine de kendi sınırlarının
içinde kalmak zorunda.
Bu yüzden uydunun
ısı iletim şeritlerine, kaplamalara,
yalıtıma
ve özenle seçilmiş malzemelere ihtiyacı var.
Uyduların
kliması yok.
İşi fizik kuralları hallediyor.

<!-- S37 -->
Ve batarya
ilginçleşir.
Onu güneş ışığıyla şarj et.
Sonra uydu
Dünya'nın gölgesine kayar
ve paneller neredeyse hiçbir şey üretmez.
Bataryası onu hayatta tutar.
Sonra tekrar güneş ışığına.
Şarj. Deşarj.
Şarj. Deşarj.
Tekrar tekrar.
Yıllarca.
Güç yönetimindeki tek bir hata
görevi sessizce bitirebilir.

<!-- S38 -->
Peki şimdi, onunla nasıl konuşursun?
Bir telsize ihtiyacın var.
Bir antene.
Ve yasal olarak kullanmana
izin verilen bir frekansa.
Ve bir yer istasyonuna.
Uydunun
interneti yoktur.
Sadece tependen uçar
ve yayın yapar.

<!-- S39 -->
Senin yer istasyonun
sinyali yakalar.
Bilgisayar onu çözer.
Ve birden kendi uzay aracından
verilerin olur.
Bir terminal açtığını
ve bunu gördüğünü hayal et.

Ama o sayıları
yazan makine...
başının yüzlerce
kilometre üstünde.

<!-- S40 -->
Peki onu oraya
aslında nasıl çıkarırız?
Bir roket yapabilirsin...
Lütfen yapma...
Ona ihtiyacın yok.
CubeSat'ler
ikincil yük olarak uçar.

<!-- S41 -->
Zaten bir roket yukarı çıkıyor.
Fazladan yeri var.
Uydun standart bir deployer'da
birlikte yolculuk eder.
Kişisel roket gerekmez.

<!-- S42 -->
Ve şimdi bir roketin
tepesinde duruyor.
Ona dokunamazsın.
Kutuyu açamazsın.
Kablo takamazsın.
Roket fırlıyor.
Yaklaşık dokuz dakika sonra,
yörüngedesin.

<!-- S43 -->
Deployer
uydunu serbest bırakır.
Yayla dışarı fırlar
ve takla atmaya başlar.

<!-- S43b -->
Ama dışarıda olduğunu nasıl bilir?
...
Deployer'ın içinde dururken
basılı kalan yaylı anahtarlar,
fırlatıldığı an dışarı fırlar
ve bilgisayar açılır.
Sonra, kurallar gereği,
yaklaşık yarım saat sessiz kalır.
Ancak o zaman telsizini açar,
antenlerini açar,
ve nihayet eve seslenir.
Ve Dünya'da bir yerde...
yer istasyonun onu duyar.

<!-- S44 -->
Bir makine yaptın.
Ve şimdi o makine
gezegenin çevresinde dönüyor.

<!-- S44b -->
Ama işimiz bitmedi.
Ölü bir uydu sonsuza dek
orada kalamaz.
Yüzyıllarca yörüngede kalırsa,
uzay çöpüne dönüşür.

<!-- S45 -->
Bu, modern görevlerin
giderek uzay aracının
ömrünün sonunu
planlamak zorunda olduğu anlamına gelir.
İdeal olarak, üst atmosferdeki seyrek hava
onu yavaşça aşağı çeker.
Yörüngesi alçalır.
Atmosfere yeniden girer.
Ve yanar.
Görevin sonu...
görevin bir parçası.

<!-- S46 -->
Peki... kendi uydunu
yapabilir misin?
Teknik olarak, evet.
NASA olman gerekmez.
Bir rokete sahip olman
gerekmez.
Hatta illa büyük bir şirketin
olması bile gerekmez.

<!-- S47 -->
Uydunun fırlatmadan
sağ çıkması gerekir.
Uzayda sağ kalması.
Yasal olarak iletişim kurması.
Kendi başına çalışması.
Ve en sonunda,
yörüngeyi boşaltması.
Bütün bunlar,
biri onu bir rokete
koymadan önce
kanıtlanmış olmalı.

<!-- S48 -->
CubeSat'ler uzayı kolaylaştırmadı.
Onu standartlaştırdı.
Her şeyi sıfırdan
yapmak yerine,
var olan bir standarda uyan
bir şey yapabilirsin.
Ve bu şaşırtıcı derecede büyük bir değişim.

<!-- S49 -->
Yani şu anda bir yerde,
Dünya'nın çevresinde dönen
küçük makineler var.
Üniversiteler,
araştırma ekipleri,
şirketler ve öğrenciler tarafından yapılmış.

<!-- S50 -->
Bazıları kamera taşır.
Bazıları radyasyon ölçer.
Bazıları yepyeni
teknolojiyi test eder.
Ve bazıları sadece tek bir soru
soran deneyler:
"bu şeyi uzayda
çalıştırabilir miyiz?"

<!-- S51 -->
Ve işte bu yüzden
kendi uydunu yapmak
böylesine büyüleyici.
Çünkü seninle uzay
arasındaki mesafe
artık bir roket değil.
Belki de...
on santimetrelik bir kutu.
Ve çok, çok
uzun bir kontrol listesi.
