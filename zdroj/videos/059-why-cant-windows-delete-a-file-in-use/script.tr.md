<!-- S01 -->
Bir dosyayı silmeye çalışıyorsun.
Bilgisayar dosyanın başka bir programda
açık olduğunu söylüyor.
Ama hangisinde olduğunu söylemiyor.

<!-- S02 -->
Bu ileti, çok daha tuhaf bir sorunun
görünen ucu.
Bir dosyayı açmak
aslında ne demek?

<!-- S03 -->
Çünkü başka bir bilgisayarda
aynı dosya, aynı biçimde açıkken,
tek bir itiraz olmadan siliniyor.

<!-- S04 -->
Aynı dosya.
Aynı işlem.
Bambaşka iki yanıt.

<!-- S05 -->
Herkesi sinir eden
yerden başlayalım.
Hangi program?

<!-- S06 -->
Windows biliyor.
O açık dosya için
bir çekirdek nesnesi var
ve sahibi olan süreci biliyor.
Adını söyleyebilirdi.

<!-- S07 -->
Sen de rastgele program kapatıyorsun.
Görev Yöneticisi'ni açıyorsun.
Bir süreç listesine bakıyorsun
ve neredeyse hiçbirini tanımıyorsun.

<!-- S08 -->
Ve yıllarca
yanıt gerçekten de
ayrı bir araç indirmekti.
Unlocker 2005'te çıktı,
ve Windows XP'de yanıt buydu.

<!-- S09 -->
Sonra Windows 7
Kaynak İzleyicisi'ni getirdi.
CPU sekmesi.
Associated Handles adlı bir liste.

<!-- S10 -->
Dosyanın adını yaz.
Sana programı
ve süreç numarasını veriyor.
Kurulacak bir şey yok.
2009'dan beri orada duruyor.

<!-- S10b -->
Ama ayrı araçlar sana söylemekten
fazlasını yapıyordu.
Tanıtıcıyı kapatıp
dosyayı serbest bırakabiliyorlardı.

<!-- S11 -->
Bu da bizi
soruya geri getiriyor.
O program dosyayı açtığında
tam olarak ne aldı?

<!-- S12 -->
Diyelim ki bir oynatıcı
movie.mp4 adlı bir dosyayı açıyor.
Windows'ta bir dosyayı açmak
iki şeyi belirtmek demek.

<!-- S13 -->
Birincisi apaçık.
Onunla ne yapmak istiyorum?
Okumak. İçine yazmak.

<!-- S14 -->
İkincisi işin ilginç yanı.
Ben onu açık tutarken
başkaları ne yapabilir?

<!-- S15 -->
Bu gerçek bir ayar.
Sen tutarken diğer programların
ne yapabileceğini sen söylüyorsun.

<!-- S16 -->
Okuyabilirler.
İçine yazabilirler de.
Silebilir ya da adını değiştirebilirler.

<!-- S16b -->
Ya da hiçbirini.
Ben kullandığım sürece
kimse ona dokunmaz.

<!-- S17 -->
Silmeye izin veren bayrağın adı
FILE_SHARE_DELETE.
Ve Microsoft'un belgeleri
altına tek bir satır ekliyor.

<!-- S18 -->
Silme yetkisi hem silmeyi
hem ad değiştirmeyi kapsar.

<!-- S19 -->
Yani silme paylaşımını
reddeden bir program
ad değiştirmeyi de kilitlemiş olur.

<!-- S20 -->
Ve dosyayı açan program
bunu vermediyse,
başka hiç kimse alamaz.

<!-- S21 -->
İşte bu yüzden hatanın adı
dosya meşgul değil.
Adı paylaşım ihlali.

<!-- S22 -->
Yanıt en baştan beri
hatanın kendi adının
içinde duruyordu.

<!-- S23 -->
Şimdi aynı şey
bir Linux makinesinde.
Bir oynatıcı videoyu açıyor.

<!-- S24 -->
Ve sen yazıyorsun
rm movie.mp4.

<!-- S24b -->
İşe yarıyor.
Video oynatılmaya devam ediyor.

<!-- S25 -->
Peki o program ne aldı,
dosya üzerinde bir hakimiyet değilse?

<!-- S26 -->
Bu videonun bütün fikri
işte bu.
Ad, dosyanın kendisi değil.

<!-- S27 -->
movie.mp4 bir dizindeki
bir satır.
O satır, asıl verileri tutan
bir nesneyi gösteriyor.

<!-- S28 -->
Bir program dosyayı açtığında
aldığı şey nesneye
bir referans.
Satıra değil.

<!-- S29 -->
Yani dosyayı silmek
satırı siliyor.
Nesneye dokunulmuyor.

<!-- S30 -->
Kılavuz sayfası bunu
tek bir cümleyle söylüyor.
Dosya, kendisine işaret eden
son dosya tanımlayıcısı kapanana kadar
var olmayı sürdürür.

<!-- S31 -->
Bunu görene kadar
soyut geliyor.
Ben de beş yüz megabaytlık
bir günlük dosyası yaptım
ve bir sürecin onu açık tutmasını sağladım.

<!-- S31b -->
Sonra onu sildim.

<!-- S32 -->
Dizin listesi
hiçbir şey göstermiyor.
Klasör boyutunu ölçen araç
sıfır diyor.

<!-- S33 -->
Ve diskteki boş alanı
ölçen araç,
beş yüz megabaytın hâlâ
eksik olduğunu söylüyor.

<!-- S33b -->
Boş bir klasör.
Yarım gigabayt yok olmuş.

<!-- S34 -->
Bu o kadar sık oluyor ki
yalnızca böyle dosyaları bulmak için
ayrı bir komut var.
Silinmiş, görünmez, hâlâ diskte.

<!-- S35 -->
Ve alan, o tek süreç
dosyayı bıraktığı anda
geri geliyor.

<!-- S36 -->
Aynı mantık ad değiştirme için de geçerli.
Dosyayı açıkken taşı,
program bunu hiç fark etmez.

<!-- S37 -->
Kılavuz orada da dobra.
Eski yola ait açık dosya tanımlayıcıları
bundan etkilenmez.

<!-- S37b -->
Zaten adı hiç kullanmıyordu.

<!-- S38 -->
Bunun bilinmeye değer
bir sınırı var.
Çalışan bir programın üzerine
yerinde yazamazsın.

<!-- S38b -->
Linux reddediyor.
Text file busy.

<!-- S39 -->
Yapabileceğin şey
adı dosyadan ayırmak
ve oraya yeni bir dosya koymak.

<!-- S40 -->
Eski süreç, artık hiçbir adı
olmayan bir nesneyi kullanarak
çalışmayı sürdürüyor.
Sonra başlayan her şey yenisini alıyor.

<!-- S41 -->
Bu yine aynı fikrin
kendini kanıtlaması.
Pek çok şey, nesneye yerinde
dokunmadan değiştirilebilir.

<!-- S41b -->
Linux bu yüzden çalışan bir programı
güncelleyebiliyor.
Yeni sürümü yalnızca
yeniden başlattığında alırsın.

<!-- S42 -->
Peki Windows
sadece kötü mü tasarlanmış?

<!-- S42b -->
Hayır.
Ve işte neredeyse hiç kimsenin
bilmediği kısım bu.

<!-- S43 -->
Windows'un tam olarak aynı şeyi
yapmanın bir yolu var.

<!-- S43b -->
NTFS üzerinde Windows
POSIX tarzı bir silme isteyebilir.

<!-- S44 -->
Microsoft o zaman ne olduğunu
anlatıyor.
Ad, görünen ad alanından
kaldırılır.

<!-- S45 -->
Ve dosyayı zaten açmış olan
uygulamalar onu kullanmayı sürdürebilir,
açarken kullandıkları ad
artık yok olsa bile.

<!-- S46 -->
Bu, Unix davranışı.
NTFS üzerinde.
Microsoft tarafından belgelenmiş.

<!-- S47 -->
İki sistem de ikisini yapabiliyor.
Farklı olan, varsayılan davranış.
Bir dosyayı hiç düşünmeden açtığında
eline geçen şey.

<!-- S48 -->
Windows'ta bir sözleşme alıyorsun.
Unix'te bir nesneye
bir referans alıyorsun.

<!-- S49 -->
Bu, programcılara özgü
bir soru gibi geliyor,
ta ki tam olarak bu iletiyi
görene kadar.

<!-- S50 -->
Güncelleştirmelerin yüklenmesini
tamamlamak için bilgisayarı yeniden başlatın.

<!-- S51 -->
Diyelim ki Windows, çalışan bir sürecin
katı sözleşme altında açık tuttuğu
bir kitaplığı değiştirmek zorunda.

<!-- S52 -->
Dosyayı o sürecin altından
değiştiremez.
Yani bir şeyin bırakması gerekiyor.

<!-- S53 -->
Uygulamayı kapat.
Hizmeti durdur.
Ya da bütün işi
Yeniden Başlatma Yöneticisi'ne bırak.

<!-- S54 -->
Bu gerçekten bir bileşen.
İşleri sırayla kapatıyor.
Windows uygulamaları,
sonra konsol programları,

<!-- S55 -->
sonra hizmetler,
en sonda da Dosya Gezgini.
Sonra hepsini yeniden başlatıyor.

<!-- S56 -->
Ve tek bir nedenle var,
Microsoft bunu kendi belgelerinde
açıkça söylüyor.

<!-- S57 -->
Yazılım kurulumlarının
ve güncelleştirmelerin
sistemin yeniden başlatılmasını
gerektirmesinin başlıca nedeni...

<!-- S58 -->
güncellenen dosyalardan bazılarının
o sırada çalışan bir uygulama
ya da hizmet tarafından
kullanılıyor olması.

<!-- S59 -->
Burada bitirmek fazla derli toplu olurdu.
Paylaşım kuralları, bilgisayarın yeniden
başlatma istemesinin tek nedeni değil.

<!-- S60 -->
Çekirdek güncellemesi başka bir konu.
Çekirdek, kendi altından
değiştirilemez.

<!-- S61 -->
Linux'ta da aynı sorun var,
gerçi canlı yamalama
bazen yeniden başlatmayı önleyebiliyor.

<!-- S62 -->
Yani dürüst açıklama,
tatmin edici olandan
daha azını iddia ediyor.

<!-- S63 -->
Windows'un kullanımdaki dosyalara
davranışı, bazı bileşenlerin çalışırken
değiştirilmesini zorlaştırdı,
ve bu da buna katkıda bulundu.

<!-- S64 -->
Çünkü her tasarım kararının
bir yerde bir sonucu olur.

<!-- S65 -->
Windows, dosyayı açan programa
başkalarının onunla ne yapabileceğine
karar verme hakkını veriyor.

<!-- S66 -->
Bedeli, bazen kendi dosyanı
silememen,
çünkü başka bir program
buna izin vermemiş.

<!-- S67 -->
Unix adı ve nesneyi
ayrı tutuyor,
böylece sistem çalışırken
pek çok şey değiştirilebiliyor.

<!-- S68 -->
Bedeli, diskte kaybolan
ve hiçbir dosyaya ait olmayan
yarım gigabayt.

<!-- S69 -->
Ve bak, bu ikisinin her biri
nasıl çözülüyor.
Windows'ta bir çıkış yolu
dosyayı tutan programı
kapatmak.

<!-- S70 -->
Linux'ta o alanı geri almanın
bir yolu,
onu hâlâ açık tutan hizmeti
yeniden başlatmak.

<!-- S71 -->
Farklı nedenler.
Bazen aynı çare.

<!-- S71b -->
Bu arada, bir sonraki sorunun
bizi nereye götürdüğünü görmek istersen,
abone olmayı düşün.
Kanala çok yardımı oluyor.

<!-- S72 -->
Peki. Baştaki soru.
Bir dosyayı açmak
ne demek?

<!-- S73 -->
Bir şey tutuyorsun demek.
İki sistem sadece tutman için
farklı şeyler veriyor.

<!-- S74 -->
İşte bu yüzden o ileti
aslında hiçbir zaman
bu dosya silinemez demedi.

<!-- S75 -->
Onu açan programın
sana izin vermediğini
söyledi.

<!-- S75b -->
Ve hangi program olduğunu biliyor.
Sadece söylemedi.
