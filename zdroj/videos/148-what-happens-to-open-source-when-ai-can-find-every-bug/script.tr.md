<!-- S01 -->
948.
Bir yapay zekânın bulduğu farklı yolların sayısı bu:
bir Linux bilgisayarı içeriden ele geçirmenin yolları.

<!-- S02 -->
Çalınmış şifre yok. Uzaktan sızma yok.
Her biri sıradan bir kullanıcıyla başlıyor,
hiçbir özel yetkisi olmayan biriyle,
ve root ile bitiyor,
yani her şeyi yapabilen hesapla.

<!-- S03 -->
OpenAI sonucu Kasım 2026'da yayımladı.
Tüm çalışma
1,2 milyon dolarlık API kredisine mal oldu.

<!-- S05 -->
Bunlar OpenAI'ın kendi rakamları,
onları üreten modeli piyasaya sürmesinden
bir gün önce yayımlandı,
ve dışarıdan kimse toplam sayıyı doğrulamadı.
Ama yüzlerce rapor ve yama
çoktan gönderildi.

<!-- S06 -->
Bunun Linux'un ötesinde neden önemli olduğu şu:
Linux'un kaynak kodu herkese açık.
Herkes okuyabilir.
Onlarca yıl boyunca bu,
neden güvenli olduğunun gerekçesiydi.

<!-- S07 -->
O hâlde bir makine açık kodu okuyup
onu bu ölçekte çalışan istismar kodlarına çevirebiliyorsa,
yazılımlar kodlarını gizli mi tutmalı?

<!-- S08 -->
Zaten bunu yapan yazılıma bakalım.
Nisan 2026'da Microsoft,
164 güvenlik açığını
aylık yama gününde düzeltti.
Ekim'de ise
1.413 açığı düzeltti.

<!-- S09 -->
Yalnızca o ay içinde, kendinden önceki
herhangi bir yılın tamamından fazlasını düzeltti.
Bu düzeltmelerin 1.000'den fazlası Windows'taydı,
ve Microsoft, bu artışı kendi yapay zekâ araçlarının
tetikleyeceği konusunda uyarmıştı.

<!-- S10 -->
Bu iki sayıyı doğrudan karşılaştıramazsın.
Şirketler farklı şekilde sayıyor,
ve Microsoft kendi özel kodunda arama yapıyordu.

<!-- S11 -->
Ama bu bir şeyi gösteriyor.
Kodu gizli tutmak
hataların oluşmasını engellememişti.

<!-- S12 -->
Peki seni gerçekten ne koruyor?
Bunu yanıtlamak için
bu makinenin nasıl çalıştığına bakmamız gerek,
çünkü her adımı bir şeyleri eliyor.

<!-- S13 -->
Linux çekirdeğinde
40 milyondan fazla satır kod var.
Önce keşif ajanları kodu taradı
ve sıradan bir kullanıcının
gerçekten erişebileceği kısımları seçti.

<!-- S14 -->
Geriye yaklaşık %7'si kaldı.
Bu, saldırmaya değer buldukları kısım,
rastgele bir örneklem değil,
yani sonucu 14 ile çarpamazsın.

<!-- S15 -->
Ardından analist ajanlar bu kodu inceledi
ve şüpheli olan her şeyi listeledi.
2.308 aday,
12 saatte.

<!-- S16 -->
Ama şüphe hiçbir şeyi kanıtlamaz.
Bu yüzden başka ajanlar test programları yazdı
ve bunları yalıtılmış sanal makinelerde çalıştırdı.
1.724 hatanın
gerçek olduğu ortaya çıktı.

<!-- S17 -->
Sonra pahalı kısım geldi:
çalışan istismar kodları yazmak,
hem de sıradan bir masaüstü sistemin
standart korumaları açıkken.
1.169 tanesi
root'a ulaştı.

<!-- S18 -->
Bunları altta yatan açığa göre gruplarsan,
948'e ulaşırsın.

<!-- S19 -->
Raporda bir ayrıntı var
ki unutması zor.
İlk çalışmalardan birinde
ajanlar 200 başarı bildirdi.
Sonra insanlar, oraya nasıl vardıklarını kontrol etti.

<!-- S20 -->
Bunların yirmisi root'a
bilinmeyen başka bir hata üzerinden ulaşmıştı,
kullanmaları söylenen hata üzerinden değil.
Bir kapıyı açmaya gönderilmişlerdi,
ama kimsenin bilmediği başka bir kapı buldular.

<!-- S21 -->
OpenAI, istismar kodlarından alınan bir örneklemde
dışarıdaki uzmanların daha önce görmediği
on istismar tekniği tespit etti.

<!-- S22 -->
Temmuz'da daha eski bir model
bu açıklardan 166 tane bulmuştu.
Üç aylık düzeltmelerden sonra
yeni model 948 tane buldu.
Hatalar tükenmemişti.
Sonraki çalışma çok daha fazlasını buldu.

<!-- S23 -->
Ama önemli bir sınır var.
Bunların hiçbiri bilgisayarına
internet üzerinden sızmıyor.
Saldırganın zaten makinede olması gerekiyor,
sıradan bir kullanıcı olarak.

<!-- S24 -->
Bu, göründüğü kadar rahatlatıcı değil,
çünkü gerçek saldırılar çoğu zaman iki adımda gelir.
Önce içeri girersin,
bir tarayıcı açığıyla ya da zararlı bir indirmeyle.
Sonra root gerekir.
Bu, ikinci adım.

<!-- S25 -->
OpenAI'ın tavsiyesi net.
En son yamaları yüklenmemiş bir sistemde
sıradan her hesabı root gibi düşün,
en azından bol kaynaklı bir saldırgana karşı.

<!-- S26 -->
Peki bu durumda
açık kod lehindeki eski argüman ne oluyor?
Doksanların sonunda
Eric Raymond ona bir slogan verdi:
"Yeterince göz varsa, bütün hatalar kolayca bulunur."

<!-- S27 -->
Buna Linus Yasası dedi.
Güzel bir fikir, ama içinde bir varsayım var:
birinin gerçekten bakıyor olması.

<!-- S28 -->
2014'te Heartbleed adlı bir hata
OpenSSL'de ortaya çıktı,
web'in çok büyük bir kısmını koruyan kodda.
Yaklaşık yarım milyon güvenli sunucunun
açıkta olduğu düşünülüyordu.

<!-- S29 -->
Hata iki yıldır açık kodun içinde duruyordu.
Proje yılda yaklaşık
2.000 dolar bağış alıyordu
ve tek bir tam zamanlı geliştiricisi vardı.

<!-- S30 -->
Herkes okuyabilirdi.
Neredeyse kimse okumadı.

<!-- S31 -->
Açık kaynağın asıl zayıflığı her zaman buydu.
Koda bakan çok fazla göz değil. Çok az göz.

<!-- S32 -->
Ve yapay zekânın değiştirdiği kısım da bu.
Bir makine taramayı sürdürebilir
ve bir insan araştırmacının tek başına
başa çıkabileceğinden çok daha fazla adayı inceleyebilir.
Eski vaat nihayet yerine geliyor,
herkes için, saldırganlar dahil.

<!-- S33 -->
Yani açık kod artık gerçekten inceleniyor.
Onu gizlemek işe yarar mı?

<!-- S34 -->
Kapalı bir program da çalışmak zorunda,
dolayısıyla makine kodu
onu kullanan her bilgisayarda duruyor.
Ghidra gibi araçlar bunu geri çevirip
kaynak koduna benzer bir şeye dönüştürüyor.

<!-- S35 -->
Bir de klasik bir numara var.
Bir programı
güvenlik güncellemesinden önce ve sonra karşılaştır.
Değişen yer, açığın nerede olduğunu gösterir.

<!-- S35b -->
Bu, saldırganlara nereyi hedefleyeceklerini söyler,
hem de her sistem
güncellemeyi yüklemeden çok önce.

<!-- S36 -->
Anthropic bunu Windows çekirdeğinde denedi,
Microsoft'un kısa süre önce yamaladığı
21 açıkla,
ve kaynak kodu olmadan.
Yapay zekâ ilk çökmeyi 31 dakikada tetikledi.
Altı saat içinde 18 tane vardı.

<!-- S37 -->
Sekizi, makinenin tam kontrolünü
ele geçirebilen çalışan istismar kodlarına dönüştü,
her biri yaklaşık 2.000 dolara.

<!-- S38 -->
Ama bunlar bilinmeyen hatalar değildi.
Yamalar zaten
sorunların nerede olduğunu gösteriyordu.
Sıfırdan yeni bir açık bulmak daha zor.

<!-- S39 -->
Yani gizlilik saldırgana hâlâ bir bedel ödetiyor.
Bu bir hız tümseği, duvar değil.
Tümsek ne kadar yüksek?
Bununla ilgili kamuya açık bir rakam yok.

<!-- S40 -->
Peki öbür taraf?
Açık olmak sana gerçekte ne kazandırıyor?
Cevap, OpenAI raporundaki
küçük bir ayrıntıda.

<!-- S41 -->
Tarama ve analizin sürdüğü on gün boyunca,
bu Linux açıklarının 100'den fazlası
başka insanlar tarafından
düzeltilmiş ya da düzeltilmek üzereydi.
Yaklaşık 300 tanesi daha
zaten herkesin önünde tartışılıyordu.

<!-- S42 -->
Başkaları da aynı hataları
aynı anda buluyordu.

<!-- S43 -->
Linus Torvalds bunu daha Mayıs'ta anlatmıştı.
Yapay zekâ raporlarının
çekirdeğin güvenlik e-posta listesini
"neredeyse tamamen yönetilemez" hâle getirdiğini söyledi,
çünkü farklı insanlar sürekli
aynı araçlarla aynı şeyleri buluyordu.

<!-- S44 -->
Ve tavsiyesi şuydu:
"Yapay zekâ araçlarıyla bir hata bulduysan,
büyük ihtimalle başka biri de bulmuştur."

<!-- S45 -->
Çekirdeğin kuralları artık bunu açıkça söylüyor.
Yapay zekâyla bulunan bir hata kamuya açık sayılmalı,
çünkü bu hatalar
birkaç araştırmacının önüne birden çıkıyor,
çoğu zaman aynı gün.

<!-- S46 -->
Bunun gizli hata fikrine
ne yaptığını bir düşün.
Senin için bulması ucuzsa,
herkes için de ucuzdu.

<!-- S47 -->
Açık kaynakta
herkes raporu inceleyebilir,
düzeltmeyi doğrulayabilir ve sonuca itiraz edebilir.
Kapalı yazılımda ise
çoğunlukla satıcıya güvenmek zorundasın.

<!-- S49 -->
Ama açıklığın bir faturası var,
ve beklediğin fatura değil.
Küçük bir projenin taramaya gücünün yetmediğini
söylemek cazip geliyor.
Yapay zekâ şirketleri şimdiden
projelerin bakımcılarına ücretsiz erişim sunuyor.

<!-- S50 -->
Eksik olan, insan.
Çekirdekte eskiden her sürümde
yaklaşık 500 güvenlik sorunu kaydedilirdi.
Bu yıl sayı 1.500'ü geçti.
Birçoğu küçük,
ama yine de birinin hepsini incelemesi gerekiyor.

<!-- S51 -->
Ocak'ta curl projesi
ücretli hata ödülü programını sonlandırdı,
gelen çöp rapor selini ödüllendirmeyi bırakmak için.

<!-- S52 -->
İyi raporlar bile işi yalnızca bir sonraki adıma taşıyor.
Yapay zekânın ürettiği yamalar hâlâ insan incelemesi gerektiriyor.
İlk düzeltmelerin bazıları gereksiz kod ekledi
ya da aynı hatanın başka sürümlerini gözden kaçırdı.

<!-- S53 -->
Daha fazla tarama satın alabilirsin.
Ama bir kod parçasını o kadar iyi anlayan
daha fazla insan satın alamazsın.
Burada, maaşlı bir güvenlik ekibi olan bir şirket
gerçekten avantajlı.

<!-- S54 -->
Ve sonra son sorun geliyor.
Düzeltilmiş olmak, yüklenmiş olmakla aynı şey değil.

<!-- S55 -->
Mart 2017'de
Microsoft, Windows'taki bir açığı yamaladı.
Kapalı kaynak, tek satıcı, tek güncelleme sistemi.
İki ay sonra
WannaCry aynı delikten geçerek
yaklaşık 200.000 bilgisayara girdi,
150 kadar ülkede.

<!-- S56 -->
O yamanın yayılmak için iki ayı vardı,
ve yetmedi.
Bir saldırgan artık sana iki ay bırakmayabilir.
Aynı Anthropic çalışmasında
yapay zekâ, Firefox'un JavaScript motoru için
yayımlanmış bir düzeltmeyi aldı
ve bir saatten kısa sürede çalışan bir istismar kodu elde etti.

<!-- S57 -->
Firefox'un düzeltilmiş sürümünün
çıkmasına daha 18 gün vardı.

<!-- S58 -->
Bir düzeltmeyi yayımlamanın tehlikesi bu.
Bilgi saldırganlara,
güncelleme sana ulaşmadan önce ulaşabilir.

<!-- S59 -->
Bir Linux düzeltmesinin katedeceği uzun bir yol var:
çekirdekten kararlı sürüme,
dağıtımına, oradan cihazına.
Bir telefon aylarca, hatta sonsuza dek bekleyebilir.

<!-- S60 -->
Kapalı yazılım da bundan kaçamıyor.
Az önce gördük: Windows yaması yetti.
Her güncelleme artık aynı zamanda bir harita.

<!-- S60b -->
O yüzden her şeyi güncel tut,
bilgisayarını, telefonunu, hatta yönlendiricini,
ve güncellemeleri gelir gelmez yükle.
Yapay zekâ düzeltmeleri saldırıya çevirmekte ustalaştıkça
beklediğin her gün daha çok önem taşıyacak.

<!-- S61 -->
Peki açık kaynak hâlâ daha mı güvenli?
Açıkçası, kimse bilmiyor.
Kamuoyunun bildiği kadarıyla
hiç kimse iki tarafta da aynı testi
aynı kurallarla yapmadı.

<!-- S62 -->
Söyleyebileceğimiz şey daha mütevazı.
Kodu gizlemek eskisi kadar kazandırmıyor.
Onu göstermek, herkesin işi kontrol etmesini sağlıyor
ve kodun bakımını yapanların
iş yükünü artırıyor.

<!-- S64 -->
Yapay zekâ hiçbir zaman bütün hataları bulamasa bile,
onları bulmanın maliyetini çoktan değiştirdi.

<!-- S65 -->
Artık önemli olan, bir deliğin ne kadar süre açık kaldığı:
birinin onu bulduğu an ile
senin makinende kapandığı an arasında.

<!-- S66 -->
O zaman sana bir soru.
Her hatayı herkes bulabiliyorsa,
okuyabildiğin koda mı güvenmeyi tercih edersin,
yoksa onu düzeltmesi için para alan bir şirkete mi?
Yorumlarda yaz.
