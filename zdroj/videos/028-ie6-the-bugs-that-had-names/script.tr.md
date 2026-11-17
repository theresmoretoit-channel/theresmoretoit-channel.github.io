# Internet Explorer 6 — Adı Olan Hatalar

<!-- S01 -->
Bu ikinci bölüm.

Birinci bölümü görmediysen
aşağıda bağlantısı var.

Yine de kısa hâlini anlatayım.

<!-- S02 -->
2001'de
Microsoft Internet Explorer altıyı
piyasaya sürdü
ve Windows XP ile birlikte geldi.

Birkaç yıl içinde
tarayıcı pazarının yüzde doksanından
fazlasını almıştı.

<!-- S03 -->
Microsoft bunu
tarayıcıyı bir uygulama platformuna
dönüştürmek için kullandı.

Gerçek bir fikirdi.

Bedelini ödeyenler
web geliştiricileri oldu, o kadar.

<!-- S04 -->
Birinci bölüm buydu.

Ama bir şeyi atlamıştım.

Hataların adı olduğu kısmı
atlamıştım.

<!-- S05 -->
Normalde bir tarayıcı hatası
bir takip sisteminde numaradır.

Issue dört bir yedi iki.

Kimse hatırlamaz.

Kimse öğle yemeğinde bundan söz etmez.

<!-- S06 -->
Internet Explorer altıda
hataların özel isimleri vardı.

Ve bu, o çağın tamamı hakkındaki
en açıklayıcı şey
olarak çıkıyor karşımıza.

<!-- S07 -->
Hafif bir hatayla başlayalım.

Bir görseli sola yaslıyorsun
ve yanına bir paragraf koyuyorsun.

Metnin tam görselin
yanında durması gerekir.

Onun yerine
üç piksel ötede duruyor.

<!-- S08 -->
Dört değil.

<!-- S08b -->
İki değil.

<!-- S08c -->
Üç.

<!-- S08d -->
Her seferinde.

Bir adı vardı.

The Three Pixel Jog.

<!-- S09 -->
Şimdi o görseli sola yasla
ve ona on piksellik
bir sol kenar boşluğu ver.

Internet Explorer altı
ona yirmi veriyor.

Kenar boşluğunu ikiye katlıyor,
ama sadece yasladığın
taraftan.

<!-- S10 -->
The Double Margin Bug.

Ve kabul görmüş çözüm,
yaslanmış bir öğeyi
satır içi ilan etmekti.

<!-- S11 -->
Ki bu saçmalık.

Float bir bloktur.

Ona satır içi demek
hiçbir anlama gelmez.

İşe yaradı, o yüzden insanlar yazdı.

<!-- S12 -->
Bir sonraki daha iyi.

Bir sayfa yüklüyorsun
ve içeriğin bir kısmı
öylece orada değil.

Aşağı kaydırıyorsun.

Geri yukarı kaydırıyorsun.

Ve beliriyor.

<!-- S13 -->
Hiçbir şey yüklenmedi.

Hiçbir şey değişmedi.

Sadece utangaçtı.

Ve adı da tam yerindeydi.

The Peekaboo Bug.

<!-- S14 -->
Çaresi, kaybolan öğeye
konumunun göreli olduğunu
söylemekti.

Bunun onu neden geri getirdiğini
kimse tam açıklayamıyordu.

<!-- S15 -->
Bir de şu var:
bir bağlantının üzerine geliyorsun
ve onun altındaki kutunun
arka planı
düz bir çizgi hâlinde kesiliyor.

The Guillotine Bug.

<!-- S16 -->
Metnin, koyduğun yerden
sürünerek kaçtığı bir hata vardı.

Magic Creeping Text.

Kenarlıkların yanlış yerde,
yanlış renkte
ya da hiç çıkmadığı
bir tanesi vardı.

Border Chaos.

<!-- S17 -->
Benim favorim daha sessiz.

Bir sıra kutu diziyorsun
ve sonuncusundaki harfler
altında yeniden beliriyor.

Her zaman değil.

Öngörülebilir biçimde de değil.

The Duplicate Character Bug.

<!-- S18 -->
Ve bunun senin başına gelip
gelmeyeceğini, kaç harfin
çift çıkacağını belirleyen şey,
işaretlemede bıraktığın
HTML yorumlarının
sayısıydı.

Yorumlar.

Dosyadaki, tarayıcının
atması gereken
tek şey.

<!-- S19 -->
Bir tane daha var
ve o farklı,
çünkü insanlar onu
bilerek kullandı.

Bir yükseklik verirsen
ve içerik daha uzunsa
kutunun taşması gerekir.

Internet Explorer altı
onun yerine kutuyu büyüttü.

<!-- S20 -->
Ki bu yanlış.

Ayrıca tam olarak
minimum yüksekliğin yaptığı şey.

Ve Internet Explorer altıda
minimum yükseklik yoktu.

Böylece geliştiriciler bunu
bildirmeyi bıraktı
ve buna bel bağlamaya başladı.

<!-- S21 -->
Dur ve şu listeye bak.

The Three Pixel Jog.

The Double Margin Bug.

Peekaboo.

The Guillotine.

Bir kez karşılaştığın bir hataya
isim vermezsin.

<!-- S22 -->
Bunların adı vardı,
çünkü herkes bunlarla karşılaşıyordu.

Ve işte işi daha da
kötüleştiren kısım.

Çoğunun altında
aynı sebep yatıyordu.

<!-- S23 -->
Internet Explorer altının içinde
her öğenin ya vardı
ya da yoktu:
layout denen bir şey.

<!-- S24 -->
Bu, öğenin kendi boyutunu ve
konumunu kendisinin mi belirlediğini,
yoksa bunu üst öğeye mi bıraktığını belirliyordu.

Ve onu ayarlayamazdın.

<!-- S25 -->
layout adında
bir özellik yoktu
ve onu istemenin bir yolu da yoktu.

Hiçbir şartnamede geçmiyordu.

Render motorunun içindeki
dahilî bir bayraktı.

<!-- S26 -->
Ama onu kazara
çevirebiliyordun.

Genişlik vermek onu çeviriyordu.

Yükseklik vermek onu çeviriyordu.

Bir öğeyi yaslamak onu çeviriyordu.

Yani bu videodaki çözümlerin yarısı,
göremedikleri bir anahtarı
çeviren insanlardı.

<!-- S27 -->
Bu yüzden onu bilerek çevirmenin
en ucuz yolunu
aramaya koyuldular.

Biri, yüksekliği
yüzde bir yapmaktı.

<!-- S28 -->
Diğer bütün tarayıcıları
bundan uzak tutmak gerekiyordu,
o yüzden birazdan geleceğimiz
bir hack'in içine girdi.

<!-- S29 -->
Ve Internet Explorer altıda
zararı yoktu,
çünkü sığamadığı bir yüksekliği
zaten aşıp büyütüyordu.

İki dakika önceki hata,
çözümü güvenli kılan şeydi.

<!-- S30 -->
Bir adı vardı.

The Holly Hack.

<!-- S31 -->
Diğer yol,
zoom adında bir Microsoft
özelliğini bire ayarlamaktı.

Zoom bir demek
yakınlaştırma demek değil.

<!-- S32 -->
Görebileceğin hiçbir şeyi değiştirmedi.

Zaten mesele buydu.

Stil dosyalarında,
sırf hataları yok eden
görünmez bir bayrağı
açmak için oturuyordu.

<!-- S33 -->
Bu da bizi hack'lere getiriyor
ve işin tuhaflaştığı yer
hack'ler.

Bir tarayıcıyı düzeltmek için
önce sadece o tarayıcıyla
konuşman gerekiyor.

<!-- S34 -->
Ve Internet Explorer altı,
html öğesinin üzerinde
başka bir öğe varmış gibi
davranıyordu.

Başka hiçbir tarayıcı öyle yapmıyordu.

Belgelenmiş de değildi.

Sadece öyle davranıyordu.

<!-- S35 -->
Böylece o hayaleti yakalayan
bir kural yazıyordun
ve onu yalnızca o tarayıcı
görebiliyordu.

Yıldız, boşluk, html.

<!-- S36 -->
Diğer bütün tarayıcılar ona baktı,
eşleşen bir şey bulamadı
ve yoluna devam etti.

İşte bu star hack
ve yıllarca web'deki
neredeyse her stil dosyasında
durdu.

<!-- S37 -->
Bir de
underscore hack vardı.

Bir özellik adının önüne
alt çizgi koyuyorsun.

<!-- S38 -->
Standartlara uyan bir tarayıcı
o satırı geçersiz sayıp
atıyor.

Internet Explorer altı
alt çizgiyi yok sayıp
onu uyguluyor.

<!-- S39 -->
Yani kendi stil dosyanı
bilerek bozuyordun
ve bozukluğun kendisi
talimattı.

<!-- S40 -->
Bir de Microsoft'un
bilerek yaptığı var.

Yalnızca Internet Explorer'ın uyduğu
bir yorum yazabiliyordun.

<!-- S41 -->
Diğer bütün tarayıcılar için
o sıradan bir yorumdu,
yorumlar nasıl yok sayılırsa öyle.

Internet Explorer altı içinse
sayfanın ikinci bir sürümüne
açılan bir
kapıydı.

<!-- S42 -->
Yani üretici duruma baktı,
bu tarayıcının kendine ait
bir stil dosyasına
ihtiyacı olduğunu kabul etti
ve bunu kolaylaştıran
bir özellik çıkardı.

<!-- S43 -->
Hasarın bir kısmı
hiç hata gerektirmiyordu bile.

Internet Explorer altının
iki modu vardı.

Modern olanda
standarda uyuyordu.

<!-- S44 -->
Eski olanda
bir kutunun genişliğine
iç boşluğu
ve kenarlığı da dahildi,
ki bu tamamen
başka bir sayı.

<!-- S45 -->
Hangi modu alacağın
belgenin ilk satırına
bağlıydı.

Ve herkesin geçmekte olduğu
HTML sürümü
oraya bir XML bildirimi
koymanı söylüyordu.

<!-- S46 -->
O satır, Internet Explorer altıyı
eski moda
itiyordu.

Daha yeni standarda uymak,
onu bozan şeydi.

<!-- S47 -->
Bir de saydamlık var.

Internet Explorer altı, yumuşak kenarlı
bir PNG'yi gösteremiyordu.

Görselin solması gereken yere
gri koyuyordu.

<!-- S48 -->
Microsoft'un cevabı, adı seri numarasına
benzeyen bir filtreydi.

İşe yarıyordu.

<!-- S49 -->
Ama tarayıcının normal
render sürecinin dışında
boyuyordu,
bu yüzden üstüne koyduğun bağlantılar
çoğu zaman çalışmaz oluyordu.

Resmi düzeltip
bağlantıyı bozuyordun.

<!-- S50 -->
Başka şeyleri soldurmak içinse
ikinci bir filtre gerekiyordu.
Kendi söz dizimi vardı
ve stil dosyasında, diğer bütün
tarayıcıların anladığı sıradan
özelliğin hemen yanında duruyordu.

<!-- S51 -->
Bunun bir kısmı
o hatalardan bile eski.

Bütün bunlardan önce
düzenler iç içe tablolardan
kuruluyordu.

<!-- S52 -->
Ve bir boşluğu açık tutmak için
bir piksel enindeki
saydam bir görseli
boşluğun olması gereken boyuta
gerdiriyordun.

Onun da bir adı vardı.

The spacer gif.

<!-- S53 -->
Üzerine gelmek bir diğeriydi.

Internet Explorer altıda
hover bağlantılarda çalışıyordu.

Yalnızca bağlantılarda.

<!-- S54 -->
Yani fareyi başka bir şeyin
üzerine getirdiğinde
açılan bir menü,
stil dosyasına iliştirilmiş
küçük bir programa ihtiyaç duyuyordu.

<!-- S55 -->
Sayfadaki bir betik değil.

CSS'ten atıfta bulunulan,
tarayıcıya tek bir seçiciyi
öğretmek dışında işi olmayan
kod taşıyan
ayrı bir dosya.

İnsanlar o dosyayı yıllarca
birbirine pasladı.

<!-- S56 -->
Birinci bölüm, JavaScript'i
bir stil dosyasının içine
koyabildiğinden söz etmişti.

Söz etmediği şey,
o JavaScript'in ne sıklıkla çalıştığıydı.

<!-- S57 -->
Her fare hareketinde.

Her tuş vuruşunda.

Her kaydırmada.

Tek bir genişliği hesaplamak için
tekrar tekrar.

<!-- S58 -->
Ve tarayıcının, başka kimsede
olmayan tavanları vardı.

Bir stil dosyası dört bin kuralı
biraz geçince
uygulanmayı bırakıyordu.

Bir sayfadaki otuz birinci
stil dosyasından sonrası
yok sayılıyordu.

<!-- S59 -->
Kulağa asla ulaşamayacağın
bir sayı gibi geliyor,
ta ki siten, birilerinin
tarayıcı görmeden önce stil dosyalarını
birleştirmekten başka işi olmayan
bir derleme adımı yazmak zorunda kalacağı
büyüklüğe erişene kadar.

<!-- S60 -->
Ve bir kısmı
hiç de kozmetik değildi.

Internet Explorer altı,
sayfa nesnelerini
ve betik nesnelerini
iki farklı şekilde sayıyordu
ve hiçbir taraf
döngünün tamamını göremiyordu.

<!-- S61 -->
Yani bir betik sayfanın
bir parçasını gösteriyorsa
ve sayfanın o parçası da
betiği geri gösteriyorsa
hiçbiri asla serbest bırakılmıyordu.

O pencereyi yeterince uzun açık bırak,
tarayıcı makineyi yiyordu.

<!-- S62 -->
Ama en iyisi
hiç düzen hatası değil.

Bir input etiketi yazıyorsun.

Ona bir tür veriyorsun.

Ve eşittir işaretini unutuyorsun.
<!-- S63 -->
Bu bozuk bir nitelik.

Şimdiye kadar yazılmış her ayrıştırıcının
buna bir cevabı vardır.

Yok say.

Tahmin et.

Devam et.
<!-- S64 -->
Internet Explorer çöktü.

İçeride, alanın gizli olup
olmadığını bilmek istedi,
bu yüzden yazdığın şeyi
hidden kelimesiyle karşılaştırdı.

Sen hiçbir şey yazmamıştın.
<!-- S65 -->
Böylece yazmadığın şeyi
sıfır adresinden
almaya gitti.

Bu, sıradan bir tarayıcı çökmesi
olurdu,
ama bunu yapan kod
tarayıcıda değildi.
<!-- S66 -->
Paylaşılan bir sistem kitaplığındaydı.

Yani o üç kelime
posta istemcisini
ve dosya yöneticisindeki
önizleme bölmesini de çökertti.
<!-- S67 -->
Kendi makinendeki dosyaları
listeleyen bir pencere,
bir web sayfası tarafından kapatıldı.

Bu, birinci bölümün savının
bir çökme raporu olarak gelişi.

Tarayıcı, sistemde çalışan
bir program değildi.

Sistemin bir parçasıydı.
<!-- S68 -->
Ve düzeltmeyi başka bir yerde
öylece test edemezdin.

Internet Explorer işletim sistemine
kaynak yapılmıştı,
yani bir bilgisayar
tam olarak tek bir sürüm çalıştırıyordu.

<!-- S69 -->
Bu yüzden 2006'da
bir ön yüz işi
bir raf dolusu yedek
makineyle geliyordu.

<!-- S70 -->
Ve sonraları da bir klasör dolusu
sanal makineyle.
Her biri, içinde tek bir sayfa
açılabilsin diye
koca bir işletim sistemi
taşıyordu.

<!-- S71 -->
Ve sonra biri
bariz olanı yaptı.

Tarayıcıya eksik bir özelliği
öğretebiliyorsan
hepsini öğretebilirsin.

<!-- S72 -->
Dean Edwards adında bir geliştirici,
tek amacı Internet Explorer altıyı
kendisinin daha sonraki bir sürümü
gibi davrandırmak olan
bir kütüphane
yazdı.

İnsanlar onu yayına aldı.

Üretimde.

<!-- S73 -->
İşte burada komik olmaktan
çıkıyor.

On yılın büyük kısmında
dünyadaki ön yüz işinin
ciddi bir bölümü
tek bir tarayıcının hatalarına gitti.

Özelliklere değil.

Ürünlere değil.

Telafiye.

<!-- S74 -->
Ve bu, birinci bölümün konusu
olan şey yüzünden sürdü.

Şirketler onun üstüne
gerçek uygulamalar kurmuştu,
yalnızca orada çalışan cinsten,
ve o uygulamaların
pazartesi hâlâ çalışması gerekiyordu.

<!-- S75 -->
Yani herkesin gitmesini
istediği tarayıcı,
kimsenin kaldırmasına
izin verilmeyen tarayıcıydı.

<!-- S76 -->
2010'da
Google, kendi uygulamalarının
onda çalışmayı bırakacağını duyurdu.

Ve Denver'daki bir tasarım stüdyosu
bunun bir cenazeyi hak ettiğine karar verdi.

<!-- S77 -->
Gerçek bir cenazeyi.

Bir tabut.

Bir cenaze konuşması.

Seksenle yüz arasında insan
bir tarayıcının gömülmesini
izlemeye geldi.

Otuz kişiye göre plan yapmışlardı.

<!-- S78 -->
Ve Microsoft çiçek gönderdi.

Kartta şöyle yazıyordu:
iyi zamanlar için teşekkürler,
Internet Explorer altı.

<!-- S79 -->
Bir yıl sonra, günü gününe,
Microsoft bir web sitesi açtı.

Dünyanın ne kadarının hâlâ
Internet Explorer altı
çalıştırdığını
ülke ülke takip ediyordu.

<!-- S80 -->
O noktada
hâlâ yüzde on ikiydi.

Hedef bunu
yüzde birin altına itmekti.

Tarayıcıyı yapan şirket,
kendi ürününün ölümüne
halka açık bir geri sayım yürütüyordu.

<!-- S81 -->
Peki hataların adı neden vardı?

Çünkü etrafından dolaşamadığın
şeylere isim verirsin.

<!-- S82 -->
Kimse içinden geçip gittiği
bir ülkenin havasına
isim vermez.

İsmi yaşadığın yerde verirsin.

Ve yaklaşık on yıl boyunca
web orada yaşadı.

<!-- S83 -->
Ama Internet Explorer altıyı
web'den çıkarmak başka bir hikâye.

Ve sırada oraya gidiyoruz.

Onu da istiyorsan
bir abone ol düğmesi var,
ve birinci bölümün bağlantısı aşağıda.
