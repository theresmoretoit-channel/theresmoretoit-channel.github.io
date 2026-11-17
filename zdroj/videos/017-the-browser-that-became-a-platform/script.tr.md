# Internet Explorer 6 — platforma dönüşen tarayıcı

<!-- S01 -->
İki binlerin başında
bir web geliştiricisi olduğunuzu düşünün.

Gayet makul bir web sayfası
yazmışsınız.

<!-- S02 -->
Netscape'te çalışıyor.

Opera'da çalışıyor.

Yeni Firefox'ta çalışıyor.

Ve sonra onu
Internet Explorer'da açıyorsunuz.

Her şey bozuk.

<!-- S03 -->
Yerleşim yanlış.

Düğmeler yerinden oynamış.

PNG görselleri berbat görünüyor.

Ve nedense
HTML'inize tek bir satır sonu eklemek
üç piksellik bir boşluk yaratmış.

<!-- S04 -->
Internet Explorer 6 çağında
web geliştirmeye hoş geldiniz.

Ama işin ilginç yanı şu.

Internet Explorer 6
sadece berbat bir tarayıcı değildi.

<!-- S05 -->
Microsoft, web'in gerçekten yaşadığı
sorunları çözmeye çalışıyordu.

Diğer herkese karşı
kocaman bir avantajı vardı.

Windows.

<!-- S06 -->
Ve sonunda o avantaj
Microsoft'un tarayıcıyı bir tarayıcıdan
çok daha büyük bir şeye
dönüştürmesini sağladı.

<!-- S07 -->
Doksanların ortasında
web'e Netscape Navigator
hâkimdi.

Microsoft bundan memnun değildi.

<!-- S08 -->
Böylece Internet Explorer
Windows'la birlikte paketlendi
ve ücretsiz sunuldu.

Bir Windows bilgisayar aldınız.

Internet Explorer zaten oradaydı.

İndirilecek bir şey yok.

Ödenecek bir şey yok.

<!-- S09 -->
Ve en önemlisi,
işletim sistemini
Microsoft denetliyordu.

İki binlerin başına gelindiğinde
Internet Explorer tarayıcı pazarının
yüzde doksanından fazlasına
sahipti.

<!-- S10 -->
Internet Explorer 6,
2001'de Windows XP ile
birlikte geldi.

Bir süre Microsoft tarayıcı
savaşlarını kazanmış
gibi görünüyordu.

<!-- S11 -->
Microsoft'un bir sorunu vardı.

Web son derece sınırlıydı.

HTML belge gösterebiliyordu.

CSS onları biçimlendirebiliyordu.

JavaScript onları etkileşimli yapabiliyordu.

<!-- S12 -->
Ama aşağı yukarı bu kadardı.

Bundan karmaşık her şey
doğrudan tarayıcının
sınırlarına tosluyordu.

<!-- S13 -->
Ya bir belge taramak isteseydiniz?

Ya da bir akıllı kartla haberleşmek?

Ya da bir Windows donanımıyla
konuşmak?

<!-- S14 -->
Tarayıcı bunları gerçekten
yapamıyordu.

Bu yüzden Microsoft bir çözüm buldu.

ActiveX.

<!-- S15 -->
Temel fikir basitti.

Bir web uygulamasını neden
tarayıcının yapabildikleriyle sınırlayalım?

Bırakalım yerel Windows
bileşenlerini kullansın.

<!-- S16 -->
Ve birden bir web sayfası
sıradan HTML'in
hayalini bile kuramayacağı
şeyleri yapabiliyordu.

<!-- S17 -->
Bugün ActiveX kulağa korkunç geliyor.

Haksız da sayılmaz.

Bir ActiveX bileşeni dosyalara,
uygulamalara, donanıma
ve işletim sistemine
erişebiliyordu.

<!-- S18 -->
Bugünün güvenlik bakışıyla
bu kesinlikle çılgınca geliyor.

Ama iki binlerin başında
kurumsal uygulamalar için
gayet mantıklıydı.

<!-- S19 -->
Şirketler güzel bir belge
görüntüleyici istemiyordu.

Uygulama istiyorlardı.

Neredeyse masaüstü yazılımı gibi
davranabilen web sayfaları
istiyorlardı.

<!-- S20 -->
Ve Microsoft onlara tam olarak bunu verdi.

Windows Update'in kendisi bile
başlangıçta sistemi incelemek
ve hangi güncellemelerin gerektiğini
bulmak için ActiveX'e
dayanıyordu.

<!-- S21 -->
Yani ActiveX sadece
aptalca bir hata değildi.

Tarayıcıyı bir uygulama platformuna
dönüştürmeye yönelik
erken bir girişimdi.

<!-- S22 -->
Ve bu anlamda Microsoft
aslında zamanının ilerisindeydi.

Sorun, o platforma ne kadar
güç verdikleriydi.

<!-- S23 -->
ActiveX, Microsoft'un tek
uzantısı değildi.

VBScript vardı.

DHTML vardı.

Hatta CSS expression vardı.

Evet.

<!-- S24 -->
Internet Explorer, JavaScript'i
doğrudan CSS'in içinde değerlendirebiliyordu.

Şöyle bir şey yapabiliyordunuz.

<!-- S25 -->
Saçmaydı.

Bazen aynı zamanda
şaşırtıcı ölçüde kullanışlıydı.

Ve hiçbirinin başka yerde
çalışacağının garantisi yoktu.

<!-- S26 -->
Microsoft sadece web
standartlarını uygulamıyordu.

Microsoft web'i kendi
istediği yönde genişletiyordu.

Ve pazarın yüzde doksanıyla
bunu işler kılacak
kadar gücü
vardı.

<!-- S27 -->
En ünlü örneklerden biri
CSS kutu modeliydi.

Standart model diyordu ki
bir öğenin genişliği iki yüz piksel,
iç boşluğu yirmi piksel
ve kenarlığı beş pikselse,
toplam genişliği

<!-- S28 -->
iki yüz elli
piksel oluyordu.

<!-- S29 -->
Internet Explorer'ın eski sürümleri
bunu farklı okuyordu.

Quirks modunda, bildirilen genişlik
iç boşluğu ve kenarlığı
içerebiliyordu.

<!-- S30 -->
Bu, genişliği düşünmenin
illa çılgın bir yolu değildi.

Hatta bugün çoğu zaman tam olarak
böyle bir davranışı bilerek kullanıyoruz.

Adı border box sizing.

<!-- S31 -->
Asıl sorun,
farklı tarayıcıların
farklı davranmasıydı.

Ve bu, geliştiricinin
bunu umursaması demekti.

Hem de çok.

<!-- S32 -->
hasLayout diye bir şey vardı.

Normal bir CSS özelliği değildi.

Standardın parçası değildi.

Ama Internet Explorer'ın öğeleri
nasıl yerleştireceğine
o karar veriyordu.

<!-- S33 -->
Ve bazen bozuk bir yerleşim
tek bir satır eklenerek
gizemli biçimde düzelebiliyordu.

zoom: 1

Neden?

Çünkü zoom: 1, dahilî hasLayout
mekanizmasını tetikleyebiliyordu.

<!-- S34 -->
PNG saydamlığıyla ilgili
sorunlar vardı.

z-index'i ne kadar yüksek
ayarlarsanız ayarlayın,
mutlak konumlanmış açılır kutuların
üstünde beliren select öğeleriyle
ilgili sorunlar vardı.

<!-- S35 -->
Web geliştirme sadece
tasarımınızı hayata geçirmek değildi.

Belirli bir tarayıcı motorunun
hatalarını öğrenmekti.

<!-- S36 -->
İşte harika bir örnek daha.

Boşluk.

Ve bu, Internet Explorer'ın
suçu bile değildi.

İki görseli işaretlemede
etiketler arasında hiçbir şey olmadan
yan yana koyup
belli bir görünüm
elde ediyordunuz.

<!-- S37 -->
Sonra biri HTML'i güzelce biçimlendirip
her etiketi kendi satırına koyuyordu.

Ve birden görsellerin arasında
birkaç piksellik bir boşluk oluyordu.

Satır sonu anlamlı hâle geliyordu.

<!-- S38 -->
Kod biçimlendiriciniz
web sayfanızı kelimenin tam anlamıyla bozabiliyordu.

Ve eski bir Visual Studio sürümü
kullanıyorsanız,
HTML'inizi sizin yerinize
seve seve biçimlendirebilirdi.

Teşekkürler Microsoft.

<!-- S39 -->
Geliştiriciler bir sürü
dolambaçlı çözüm biriktirdi.

Koşullu yorumlar.

<!-- S40 -->
Ve bazen tek amacı Internet Explorer'ı
uslu durmasını sağlamak olan
tamamen tuhaf görünüşlü
HTML.

<!-- S41 -->
Çirkin kod yazıyordunuz,
kötü bir programcı olduğunuz için değil.

Çirkin kod yazıyordunuz,
çünkü tarayıcı sizi buna zorluyordu.

<!-- S42 -->
Internet Explorer ayrıca görkemli biçimde
çöküyor ve çoğu zaman açık olan
her pencereyi de yanında götürüyordu.

<!-- S43 -->
Bu da harika bir ofis eğlencesi
kategorisi doğurdu.

Hey, şu bağlantıya bir bak.

Ve yirmi Internet Explorer penceresi
yok oluyor.

<!-- S44 -->
Bu, tarayıcılar yalıtılmadan
önceki web'di.

Bugünün tarayıcısı şöyle diyor.

Bu site güvenilmez.

Onu yalıtacağım.

<!-- S45 -->
Internet Explorer 6
bazen daha çok şöyle hissettiriyordu.

Web sayfası mısın?

Tabii.

Al sana binanın anahtarları.

<!-- S46 -->
Peki geliştiriciler bu numaraları
neden kullanıyordu?

Çünkü mecburdular.

<!-- S47 -->
Beş yüz çalışanı olan
bir şirket düşünün.

Her bilgisayarda Windows XP var.

Her bilgisayarda Internet Explorer var.

<!-- S48 -->
Geliştiricinin iki seçeneği var.

Birinci seçenek.

Zaten herkeste olan
Internet Explorer için yap.

<!-- S49 -->
İkinci seçenek.

Her tarayıcı için yap,
her şeyi her yerde test et
ve BT departmanına herkesin neden
ikinci bir tarayıcıya ihtiyacı olduğunu anlat.

Cevap genelde belliydi.

<!-- S50 -->
Microsoft teknolojisini
Microsoft'u sevdikleri için
seçmiyorlardı.

Müşterinin sorununu çözen şeyi
seçiyorlardı.

Ve bazen ActiveX
eldeki en iyi araçtı.

<!-- S51 -->
Ve sonunda birinin canına tak etti.

JavaScript kütüphaneleri tarayıcı
farklarını gizlemeye başladı.

En önemlilerinden biri
jQuery'ydi.

<!-- S52 -->
Tarayıcıya özgü olay işleme
yazmak yerine
her yerde çalışan tek bir satır
yazabiliyordunuz.

<!-- S53 -->
Farklı AJAX uygulamalarıyla
elle uğraşmak yerine
ortak bir soyutlama kullanabiliyordunuz.

<!-- S54 -->
jQuery, Internet Explorer'ı
yok etmedi.

Ama o yokmuş gibi davranmayı
çok daha kolaylaştırdı.

Ve o dönemin web geliştiricileri için
bu güzel bir şeydi.

<!-- S55 -->
Firefox çıktı.

Opera gelişmeyi sürdürdü.

Safari geldi.

Ve sonunda Google, Chrome'u yayımladı.

<!-- S56 -->
Tarayıcı savaşları geri dönmüştü
ve bu kez
rekabet farklıydı.

JavaScript motorları
çarpıcı biçimde iyileşti.

HTML5 geldi.

<!-- S57 -->
Tarayıcının kendisi, geliştiricilerin
daha önce eklentiye ihtiyaç duyduğu
her şeyi öğrenmeye başladı.

<!-- S58 -->
Video.

Ses.

Canvas.

SVG.

WebGL.

WebSocket.

Ve sonunda WebRTC.

Web bir uygulama platformuna
dönüşüyordu.

<!-- S59 -->
Ki bu tam olarak
Microsoft'un ActiveX ile
başarmaya çalıştığı şeydi.

Ama artık bu,
açık standartlar üzerinden oluyordu.

<!-- S60 -->
Microsoft bir kez daha denedi.

Silverlight, geliştiricilerin C# ve .NET ile
zengin tarayıcı uygulamaları
kurmasına izin veriyordu.

Hatta Netflix'in ilk dönem
yayınını o çalıştırıyordu.

<!-- S61 -->
Ama web sonsuza dek eklenti istemedi.

Apple, iPhone'da Flash'ı desteklemeyi
reddetti.

Ve birden gelecek şu değildi.

Tarayıcı artı eklenti.

Şuydu.

Tarayıcının kendisi.

<!-- S62 -->
Silverlight yok oldu.

Flash yok oldu.

ActiveX yok oldu.

Ve Internet Explorer da
sonunda yok oldu.

<!-- S63 -->
Ve işte hikâyenin
ilginçleştiği yer burası.

Çünkü Microsoft
tamamen yanılmıyordu.

Tarayıcının bir uygulama platformuna
dönüşeceğini doğru
tahmin etmişlerdi.

<!-- S64 -->
Sadece oraya tescilli teknolojiler
üzerinden varmaya çalışıyorlardı.

Web aynı hedefe
standartlar üzerinden ulaştı.

<!-- S65 -->
Tarayıcı kazandı.

Ama 2001'in tarayıcısından
çok daha güçlü bir şeye
dönüşerek
kazandı.

<!-- S66 -->
Peki Microsoft kötü adam mıydı?

Pek sayılmaz.

Ve hikâyeyi daha ilginç
kılan da bu.

<!-- S67 -->
Microsoft'un parlak mühendisleri vardı.

Devasa kaynakları vardı.

Ve gerçekten zamanının ilerisinde olan
birçok teknoloji kurdular.

<!-- S68 -->
Ama Microsoft'un ayrıca
ezici bir pazar konumu vardı.

Ve bu, tehlikeli bir
teşvik yarattı.

<!-- S69 -->
Neredeyse herkes
senin tarayıcını kullanıyorsa
neden standartları bekleyesin?

Neden kendi çözümünü
öylece uygulamayasın?

Bir süre bu işe yaradı.

Ta ki web'in geri kalanı yetişene kadar.

<!-- S70 -->
Bugün Internet Explorer yok.

Eski tarayıcı savaşları
kadim tarih gibi duruyor.

Ama bugünün tarayıcı
pazarına bir bakın.

Chrome.

Edge.

Opera.

Brave.

Vivaldi.

<!-- S71 -->
Ve daha birçoğu
Chromium tabanlı.

Farklı ürünler.

Çoğu zaman altta
aynı tarayıcı motoru.

<!-- S72 -->
Yani belki de şunu takas ettik.

Herkesin desteklemek zorunda olduğu tek tarayıcı.

Bununla.

Herkesin üstüne inşa ettiği tek motor.

Tanıdık geldi mi?

<!-- S73 -->
Çünkü baskın bir tarayıcı motoru
yalnızca sitelerin nasıl
görüntüleneceğine karar vermez.

<!-- S74 -->
Geliştiricilerin ne yapacağını etkiler.

Hangi teknolojilerin yaygınlaşacağını.

Ve nihayetinde
web'in kendisinin ne olacağını.

<!-- S75 -->
Ancak çok önemli
bir fark var.

Bugünün web'i açık standartlar
üzerine kurulu.

Firefox'un hâlâ kendi motoru var.

Safari'nin WebKit'i var.

Chromium açık kaynak.

<!-- S76 -->
Ve modern tarayıcılar
otomatik güncelleniyor.

2003'ün durumuna
yakın bile
değiliz.

<!-- S77 -->
Ama temel soru duruyor.

Neredeyse herkesin kullandığı
bir platform üzerinde
tek bir şirketin ne kadar
etkisi olmalı?

İşte hep gündemde
kalan soru bu.

<!-- S78 -->
Peki Internet Explorer 6 berbat mıydı?

Evet.

Bazen görkemli biçimde berbat.

<!-- S79 -->
Ama hikâyenin tamamı bu değil.

O aynı zamanda çağının bir ürünüydü.

<!-- S80 -->
Sorun, Microsoft'un tarayıcı
savaşlarını öyle eksiksiz kazanmasıydı ki
kuralları kendisi
belirleyebiliyordu.

<!-- S81 -->
Ve bedelini web geliştiricileri ödedi.

hasLayout'un gizemlerini
öğrendiler.

zoom: 1'in işleri sihirli biçimde
düzeltebildiğini keşfettiler.

Ve dua ettiler.

<!-- S82 -->
Ve sonunda Internet Explorer,
yirmi yıl boyunca yaratmakla
uğraştığı şeye dönüştü.

Kimsenin artık desteklemek
istemediği bir
legacy platform.

<!-- S83 -->
Web, Microsoft'un vizyonunu
reddetmedi.

Sadece onun daha iyi
bir sürümünü kurdu.

Ve o dönemin bize öğretmesi
gereken tek bir şey varsa
o da şu.

<!-- S84 -->
Bir teknoloji, iyi olduğu için
standart hâline gelmez.

<!-- S85 -->
Bazen standart hâline gelir,
çünkü tek bir şirketin herkese onu
kullandıracak kadar gücü vardır.

<!-- S86 -->
Ve bazen,
yirmi yıl sonra...
bunu yine yaptığımızı fark ederiz.
