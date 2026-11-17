<!-- S01 -->
Birkaç günde bir, ciddi bir hata daha
haberlere düşüyor.
Birinin girişi atlamasına izin veren bir hata.
Özel verileri sızdıran bir hata.
Bilgisayarınızı bir saldırgana teslim eden bir hata.

<!-- S02 -->
Kimi zaman Windows. Kimi zaman Linux.
Bir tarayıcı, bir veritabanı, bir bulut hizmeti...
ya da milyonlarca geliştiricinin bel bağladığı
küçük bir kütüphane.

<!-- S03 -->
Ve tepki neredeyse hep aynı.
Programcılar bunu nasıl gözden kaçırdı?

<!-- S04 -->
Bunlar profesyoneller.
Kod incelemeleri, otomatik testleri,
güvenlik denetimleri, fuzzing'leri var...
ama hatalar yine de gelmeye devam ediyor.

<!-- S05 -->
Peki karmaşık yazılımı hatasız yazmak
gerçekten mümkün mü?

<!-- S06 -->
Bir sayıyla başlayalım.
Sadece yüz ayarı olan bir program düşünün,
her biri ya açık ya kapalı.

<!-- S07 -->
Yüz tane basit evet-hayır kararı.
Bu kaç kombinasyon eder?

<!-- S08 -->
İkinin yüzüncü kuvveti.
Yani kabaca bir milyon trilyon trilyon.

<!-- S09 -->
Şimdi saniyede bir milyar kombinasyon
test edebildiğinizi düşünün.
Ve Büyük Patlama'da başladığınızı.

<!-- S10 -->
Bugüne dek ancak
üç binde bir kombinasyonu test etmiş olurdunuz.

<!-- S11 -->
Ve yüz anahtar hiçbir şey.
Gerçek bir programın milyonlarcası var.
Yani "hepsini test et yeter"
pahalı değil. İmkânsız.

<!-- S12 -->
Ve bu anahtarlar egzotik şeyler değil.
Bir programın yaptığı
en basit şeylerden birini alın.
Bir kullanıcı hesabını numarasıyla ister.
Onu veritabanında buluruz.
Ve geri göndeririz.

<!-- S13 -->
Peki ya kullanıcı yoksa?
Ya biri sayı yerine metin gönderirse?
Ya negatif bir sayı? Ya devasa bir sayı?

<!-- S14 -->
Ya bu kişinin onu görmeye izni yoksa?
Ya biri hesabı tam da onu yüklediğimiz anda
silerse?
Ya aynı istek iki kez gelirse?

<!-- S15 -->
Bu soruların her biri basit.
Asıl sorun nasıl birleştikleri.
Her biri bir anahtar daha.

<!-- S15b -->
Bu arada, böyle videoları
beğeniyorsanız abone olabilirsiniz.

Kanala gerçekten yardımcı oluyor.

<!-- S16 -->
Ve bir bilgisayar bunu bizim için çözmez.
Tam olarak söylediğimizi yapar.
Kastettiğimizi değil.

<!-- S17 -->
İşte bu yüzden programlama dillerini icat ettik.
Karmaşık şeyleri her ayrıntıyı düşünmeden
tanımlamamıza izin veriyorlar.

<!-- S18 -->
Ama bazıları umduğunuzdan
daha azını üstlenir.
C'yi alın. Hızlı, basit
ve bellek üzerinde size muazzam bir denetim verir.

<!-- S19 -->
Yani şunu yazabilirsiniz.
On altı karakterlik yer ayırırız.
Sonra deriz ki: girdiyi buraya kopyala.

<!-- S20 -->
Peki ya girdi
beş yüz karakter uzunluğundaysa?
C sormaz.
Sadece sonun ötesine yazmayı sürdürür.

<!-- S21 -->
Peki bu on altı karakterin hemen ardında ne var?
Çoğu zaman çok önemli bir şey.

<!-- S22 -->
Bir program bir işlevi çağırdığında,
işlev bittiğinde nereye döneceğini
not eder.
Bir dönüş adresi.
Klasik bir düzende, bu adres
arabelleğimizin sonundan biraz sonra durur.

<!-- S23 -->
Böylece saldırgan tam da doğru uzunlukta
bir girdi gönderir.
Önce kendi komutları.
Sonra, en sonda, yeni bir dönüş adresi...
o komutlara geri işaret eden.

<!-- S24 -->
İşlev biter.
İşlemci nereye döneceğine bakar...
ve doğrudan saldırganın koduna atlar.

<!-- S25 -->
Artık onun programını çalıştırıyor,
sizinkinin tüm izinleriyle.
"Rastgele kod çalıştırmak" işte bu demek.

<!-- S26 -->
Ve işlemci yanlış bir şey yapmadı.
Komutları izledi.

<!-- S27 -->
1988'de tam da bunun gibi bir hata,
Morris solucanının
erken internete yayılmasına yol açtı.
Ve aynı numara o zamandan beri
saldırılarda kullanılıyor.

<!-- S28 -->
Bu yüzden daha yeni diller işin bir kısmını
derleyiciye devreder.
Örneğin Rust, belleği kötüye kullanabilecek
birçok programı derlemeyi reddeder.

<!-- S29 -->
Programcı der ki:
ama ne yaptığımı tam olarak biliyorum!
Ve derleyici der ki:
herkes öyle der.

<!-- S30 -->
Ve şüphelenmekte haklı.
Microsoft ile Google'ın Chrome ekibi,
ikisi de bildirdi ki
inceledikleri güvenlik hatalarının
yaklaşık yüzde yetmişi
bellek güvenliği sorunlarından geliyor.

<!-- S31 -->
Ama bir program bellek açısından kusursuz güvenli
ve yine de tamamen yanlış olabilir.

<!-- S32 -->
Bir kullanıcının giriş yaptığını düşünün.
Parolası doğru şekilde denetlenir.
Hiçbir şey çökmez. Bellek bozulmaz.

<!-- S33 -->
Ve sonra program ona
başka birinin verilerini gösterir.
Çünkü izin denetimi
birazcık yanlış yazılmıştı.

<!-- S34 -->
Hiçbir dil bunu tek başına yakalayamaz.
Dil, programın ne yapması gerektiğini
bilmez.
Bunu yalnızca biz biliriz.

<!-- S35 -->
Öyleyse teste geri dönelim.
Bir test size şunu söyleyebilir:
bu girdi için şu sonucu aldım.

<!-- S36 -->
Size şunu söyleyemez:
program her girdi için doğru.
Ve hepsini neden deneyemeyeceğimizi
zaten gördük.

<!-- S37 -->
1970'te bilgisayar bilimci
Edsger Dijkstra bunu tek cümleye sığdırdı.
Test, hataların varlığını gösterebilir,
ama asla yokluğunu.

<!-- S38 -->
Peki. O halde test etmek yerine,
neden başka programları denetleyen
ve onların doğru olduğunu kanıtlayan
bir program yazmayalım?
Ona herhangi bir kod verin, size söylesin:
o kod yapması gerekeni yapıyor mu.

<!-- S39 -->
Bu sorunun yanıtı,
ilk gerçek bilgisayar daha yapılmadan verildi.
1936'da Alan Turing kanıtladı ki
böyle bir program var olamaz.

<!-- S40 -->
Kimse henüz yapmadığı için değil.
Hiçbir şekilde var olamayacağı için.

<!-- S41 -->
Gösterdi ki hiçbir program,
her başka program için,
onun hiç durup durmayacağına karar veremez.

<!-- S42 -->
Ve 1953'te Henry Rice daha da ileri gitti.
Aynısı, bir programın gerçekte ne yaptığına dair
her önemli soru için geçerli.

<!-- S43 -->
Güvenli mi? Veri sızdırıyor mu?
Doğru yanıtı veriyor mu?
Bunu her program için çözen
genel bir yöntem yok.

<!-- S44 -->
Peki hatasız yazılım imkânsız mı?
Tam olarak değil.
Belirli bir program için
bazen doğru olduğunu kanıtlayabilirsiniz,
muazzam bir çabayla.

<!-- S45 -->
2009'da Avustralya'daki bir ekip kanıtladı ki
seL4 adlı küçük bir işletim sistemi çekirdeği
tam olarak
belirtiminin söylediğini yapıyor.

<!-- S46 -->
On bin satır koddan azdı.
Çekirdeği yapmak
yaklaşık iki insan-yıl sürdü.
Doğruluğunu kanıtlamak yaklaşık yirmi.
Modern bir web tarayıcısının
onlarca milyon satırı var.

<!-- S47 -->
Ve o kanıtın bile bir sınırı var.
Programın belirtimiyle uyuştuğunu gösterir.
Belirtimin gerçekte istediğimiz şey olduğunu
gösteremez.

<!-- S48 -->
Ve belirtimi insanlar yazar.
Yani soru bize geri döner.

<!-- S49 -->
Ve bu yalnızca kendi kodumuz değil.
Bugün bir programcı çerçevelerin,
kütüphanelerin ve yüzlerce bağımlılığın üstüne inşa eder.
Her katman bizi çok büyük bir iş yükünden kurtarır.
Ama her katman
anlamamız...
ya da en azından güvenmemiz gereken bir şey.

<!-- S50 -->
Yani yazılımınızda bir hata olması için
onu yazmanız gerekmez.
Sadece kurmanız yeter.

<!-- S51 -->
Sonra baskıyı ekleyin.
Kimse on yıl sonra kusursuz bir ürün istemez.
Gelecek ay çalışan birini ister.
Ve hiç yaşanmamış bir sızma,
bir sunumda göstermesi çok zordur.

<!-- S52 -->
Ve işte en tuhaf kısmı.
Araçlarımız sürekli iyileşiyor.
Daha güvenli diller, fuzzing, hata ödülleri...

<!-- S53 -->
Yine de bilinen açıkların sayısı
büyümeye devam ediyor.
Yalnızca 2024'te yaklaşık kırk bini
resmi bir numara aldı.

<!-- S54 -->
Kısmen çünkü her zamankinden çok daha fazla
yazılım da yazıyoruz.
Bu, her yolu daha güvenli hale getirirken...
milyonlarca kat daha fazla yol yapmaya benziyor.

<!-- S55 -->
Peki programcılar işlerinde kötü mü?
Hayır.
Onlardan hep, hiçbir genel yöntemin
garanti edemeyeceği bir şey istedik.

<!-- S56 -->
Yani belki de
"yazılımı nasıl hatasız yazarız?"
yanlış soru.

<!-- S57 -->
Daha iyi soru şu:
yazılımda hatalar olsa bile güvende kalan
sistemleri nasıl kurarız?

<!-- S58 -->
Ve güvenlik tam da oraya gidiyor.
Şunu demiyor: asla hata yapma.
Şunu diyor: zaten yaptığını varsay.

<!-- S59 -->
O dönüş adresini hatırlıyor musunuz?
Bugün sistem onu koruyor.
Bellekteki yerleşimi rastgele değiştiriyor.
Ve verinin içine gizlenmiş komutları
çalıştırmayı reddediyor.

<!-- S60 -->
C kodumuzdaki hata hâlâ orada.
Sadece onu bir saldırıya dönüştürmek çok daha zor.

<!-- S61 -->
Ve aynı fikir her yerde.
Kum havuzları, sınırlı izinler,
yalıtılmış süreçler, şifreleme,
yedekler, izleme...
katman üstüne katman,
ki tek bir hata bir felakete dönüşmesin.

<!-- S62 -->
Ve bunun çok pratik bir sonucu var.
Hatalar kaçınılmazsa,
onları düzeltmek isteğe bağlı değil.

<!-- S63 -->
Bugün kullandığınız yazılım
büyük olasılıkla kimsenin henüz bulmadığı
bir açık barındırıyor.

<!-- S64 -->
Ve biri onu bulduğunda,
güncelleme, şu ikisi arasındaki farktır:
"bir açık keşfedildi"
ve "hacklendik".

<!-- S65 -->
Aynısı kurduğumuz sistemler için de geçerli.
Eski kütüphaneler ve desteklenmeyen platformlar
görmezden gelinerek güvenli hale gelmez.
Teknik borca dönüşürler.

<!-- S66 -->
Ve o borcun neden ödenmesi gerektiği,
"Hâlâ Çalışıyor. Peki Neden Güncelleyelim?"
adlı videomun
tam da konusu.

<!-- S67 -->
Çünkü yazılımda,
"hâlâ çalışıyor"
ile "hâlâ güvenli"
çok farklı iki şeydir.
