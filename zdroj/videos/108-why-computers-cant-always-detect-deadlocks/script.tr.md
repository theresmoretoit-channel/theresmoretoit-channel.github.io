<!-- S01 -->
Dört araba bir kavşağa
tam aynı anda geliyor.
Işık yok. Tabela yok.
Sadece birçok ülkede geçerli olan kural:
sağındaki arabaya yol ver.

<!-- S02 -->
Her sürücü sağına bakıyor
ve beklemesi gereken bir araba görüyor.
Bu yüzden her sürücü bekliyor.

<!-- S03 -->
Kimse kuralı çiğnemiyor.
Herkes ona kusursuzca uyuyor.
Ve kimse asla kıpırdamayacak.

<!-- S04 -->
Bilgisayar bilimciler buna kilitlenme, yani deadlock diyor.
Ve bu sadece yollarda olmuyor.
Veritabanlarında,
işletim sistemlerinde ve sıradan yazılımlarda da oluyor.

<!-- S05 -->
Bilgisayarlar çoğu zaman bir kilitlenmeyi,
gerçekleştikten sonra kolayca tespit edebilir.
Ama bir program başka bir programı okuyup
sana kesin olarak söyleyebilir mi,
onun bir gün kilitlenip kilitlenmeyeceğini?

<!-- S06 -->
Birçok program için, evet.
Ama olası her program için
işe yarayan bir yöntem
var olamaz.
Ve bunun sebebi bilgisayarların
henüz yeterince hızlı olmaması değil.
Daha hızlı hiçbir bilgisayar bunu değiştiremeyecek.

<!-- S07 -->
Bir program işte böyle kilitlenir.
Bir online mağaza düşün;
içinde aynı anda iki görev çalışıyor.

<!-- S08 -->
Bir görev herhangi bir şeyi değiştirmeden önce
onun üzerine bir kilit koyar,
böylece başka kimse ona dokunamaz.
Bir odanın tek anahtarını almak gibi.

<!-- S09 -->
İlk görev bir müşterinin hesabını kilitler,
sonra siparişine uzanır.
İkincisi siparişi kilitler,
sonra hesaba uzanır.

<!-- S10 -->
Biri hesabı tutar
ve siparişi bekler.
Diğeri siparişi tutar
ve hesabı bekler.
İkisi de tuttuğunu bırakmaz.

<!-- S11 -->
İşin tuhaf yanı şu:
bu kod bir milyon kez
hiç sorun çıkarmadan çalışabilir.
Ancak iki görev
tam da yanlış sırayla çakıştığında
her şey durur.

<!-- S12 -->
Hata baştan beri oradaydı.
Zamanlama onu sadece ortaya çıkardı.

<!-- S12b -->
Bu arada, böyle videoları
beğeniyorsan abone olabilirsin.

Kanala gerçekten yardımcı oluyor.

<!-- S13 -->
Veritabanları bununla sürekli karşılaşır,
bu yüzden tetikte dururlar.
Kimin kimi beklediğinin haritasını çizerler.

<!-- S14 -->
Birincisi ikinciyi bekler.
İkincisi birinciyi bekler.
Oklar kapanıp bir döngü oluşturduğunda,
bu bir kilitlenmedir.
Tahmin yok. Döngü tam orada.

<!-- S15 -->
Sonra veritabanı acımasız bir şey yapar.
Görevlerden birini seçer
ve yaptığı işi çöpe atar.

<!-- S16 -->
Microsoft'un SQL Server'ı kaybedene
üstelik bir de haber verir:
kilitlenme kurbanı olarak seçildiğini
ve yeniden denemesi gerektiğini.

<!-- S17 -->
Diğer görev yoluna devam eder,
kurban da basitçe yeniden deneyebilir.

<!-- S18 -->
Bunun neyi düzeltip neyi düzeltmediğine dikkat et.
Kilitlenme çözüldü.
Ama ona yol açan kod hâlâ orada,
bir sonraki talihsiz anı bekliyor.

<!-- S19 -->
Yani zaten gerçekleşmiş
bir kilitlenmeyi fark etmek
işin kolay kısmı.
Zor soru ise başka.

<!-- S20 -->
Şu değil: bu program şu an kilitlendi mi?
Şu: ona bu girdiyi ver.
Bir gün kilitlenebilir mi?

<!-- S21 -->
Birincisi şimdinin bir fotoğrafı.
Sadece ona bakman yeterli.
İkincisi ise
olası her gelecek hakkında bir tahmin.

<!-- S22 -->
Programlar da bunu çok zorlaştırır.
Kararlar verirler. Bir şeyleri tekrarlarlar.
Çalıştırdıkları bir hesaplama
bir saniye de sürebilir, bin yıl da.

<!-- S23 -->
Bir program hemen kilitlenebilir,
bir milyon adım sonra,
nadir tek bir girdi yüzünden,
ya da hiçbir zaman.

<!-- S24 -->
Sadece çalıştırıp izleyebilirsin.
Ama bir saat sonra hâlâ kilitlenmediyse,
bu sana ne söyler?

<!-- S25 -->
Hiçbir şey.
Bir sonraki saniyede kilitlenebilir,
ya da hiçbir zaman.

<!-- S26 -->
1936'da genç bir matematikçi,
Alan Turing, şunu gösterdi:
programlarla ilgili bazı soruları
hiçbir program cevaplayamaz.
En ünlüsü kulağa daha da basit geliyor.

<!-- S27 -->
Herhangi bir programı ve girdisini al.
Sonunda duracak mı?
Yoksa sonsuza kadar mı çalışacak?

<!-- S28 -->
Buna bugün durma problemi deniyor.
Ve hiçbir program onu
her durumda doğru cevaplayamaz.

<!-- S29 -->
İspatın arkasındaki fikir
şaşırtıcı derecede kısa.
Diyelim ki biri sana
kusursuz bir durma denetleyicisi veriyor.

<!-- S30 -->
Şimdi aksi, küçük bir program yazıyorsun.
Denetleyiciye kendisini soruyor,
sonra da tam tersini yapıyor.

<!-- S31 -->
Denetleyici duracak derse,
sonsuza kadar döngüye girer.
Denetleyici sonsuza kadar çalışacak derse,
hemen durur.

<!-- S32 -->
Denetleyici onun hakkında ne derse desin,
denetleyici yanılır.
Yani kusursuz bir denetleyici var olamaz.

<!-- S33 -->
Peki bunun kilitlenmelerle ne ilgisi var?
Doğrudan ilgisi var.

<!-- S34 -->
Diyelim ki biri, kusursuz bir
kilitlenme tahmincisi yaptığını söylüyor.
Ona herhangi bir programı ve girdisini veriyorsun,
o da sana her seferinde doğru söylüyor:
bu program bir gün kilitlenecek mi, kilitlenmeyecek mi.

<!-- S35 -->
Hadi onu
durma problemini çözmek için kullanalım.

<!-- S36 -->
İstediğin bir programı al
ve onu yeni bir programın içine yerleştir.

<!-- S37 -->
Önce yeni program
eski programı basitçe çalıştırır,
adım adım, tek bir iş parçacığında.
Kilit yok. Paylaşılan hiçbir şey yok.
Kilitlenebilecek hiçbir şey yok.

<!-- S38 -->
Sonra, eski program bir gün biterse,
yeni program iki görev başlatır.
Her biri bir kilit alır,
diğerinin kendi kilidini almasını bekler,
sonra da diğerininkine uzanır.
Bilerek, her seferinde bir kilitlenme.

<!-- S39 -->
Eski program hiç bitmezse,
yeni program oraya hiç varamaz.
Kilitlenme yok. Asla.

<!-- S40 -->
Yani yeni program,
ancak ve ancak eski program durursa kilitlenir.

<!-- S41 -->
Şimdi tahminciye
yeni programı sor.
"Evet, kilitlenecek"
eski programın durduğu anlamına gelir.
"Hayır" ise sonsuza kadar çalıştığı anlamına.

<!-- S42 -->
Durma problemini az önce çözdük.
Ve bu, tam da yapılamayan şey.

<!-- S43 -->
Yani kusursuz bir kilitlenme tahmincisi
de var olamaz.

<!-- S44 -->
Sorun kilitler değil,
veritabanları ya da kötü programcılar da değil.
Bir program, kilitlenmeden önce
herhangi bir hesaplamayı gizleyebilir.
Kilitlenmeyi tahmin etmek için
o hesaplamanın bitip bitmeyeceğini tahmin etmen gerekir.

<!-- S45 -->
Ama dur bir dakika.
Gerçek bir bilgisayar sonsuz değil.
Belleğinin sınırlı sayıda durumu var.
O zaman hepsini tek tek kontrol edemez misin?

<!-- S46 -->
Sabit miktarda belleği olan
bir makine için, prensipte, evet.
Pratikte ise bir say bakalım.

<!-- S47 -->
Sekiz gigabaytlık
bir dizüstü bilgisayarın belleği
o kadar çok şekilde düzenlenebilir ki
sadece o sayıyı yazmak bile
yaklaşık yirmi milyar basamak tutar.

<!-- S48 -->
Gözlemlenebilir evrendeki
atomların sayısı
yaklaşık seksen basamaklı.

<!-- S49 -->
Yani gerçek bir makinede her şeyi kontrol etmek
teoride mümkün,
pratikte ise umutsuz.

<!-- S50 -->
Ama bu başka bir duvar.
Turing'in sınırı durumların fazlalığıyla ilgili değil.
Her zaman daha fazla bellek isteyebilen
programlar için geçerli.
Onlar için kusursuz bir tahminci var olamaz,
bilgisayar ne kadar büyük olursa olsun.

<!-- S51 -->
Peki bu, kilitlenmelere çare yok mu demek?
Hayır.
Bu sadece kusursuz bir denetleyici olmadığı anlamına geliyor.
Bu yüzden programcılar
kontrol etmesi daha kolay programlar yazar.

<!-- S52 -->
En basit hile, bir sıra belirlemek.
Her görev hesabı
siparişten önce kilitlemek zorunda.
Asla tersi değil.

<!-- S53 -->
Her görev bu sıraya gerçekten uyarsa,
döngü oluşamaz
ve bu tür bir kilitlenme yaşanamaz.

<!-- S54 -->
Başka sistemler bir zaman aşımından sonra pes eder,
tüm kilitlerini tek seferde alır,
ya da veritabanının bir kurban seçmesine izin verip
basitçe yeniden dener.

<!-- S55 -->
Küçük ve dikkatle tanımlanmış tasarımlarda ise
araçlar olası her durumu kontrol edebilir.
Amazon'daki mühendisler böyle bir araçla,
ortaya çıkması için tam doğru sırada
otuz beş adım gereken bir hata buldu.

<!-- S56 -->
Bu araçlar işe yarıyor,
çünkü problem küçültülmüş.
Sistemin bir modelini kontrol ediyorlar,
var olabilecek her programı değil.

<!-- S57 -->
Ama gerçek kod söz konusu olduğunda,
herhangi bir programı kabul eden bir denetleyici
bir şeylerden vazgeçmek zorunda.
Yaşanamayacak kilitlenmeler için
uyarı verebilir,
yaşanabilecek bazılarını kaçırabilir,
ya da bazen hiç cevap vermeyebilir.

<!-- S58 -->
Asla boş yere alarm vermeyen,
hiçbir kilitlenmeyi kaçırmayan
ve her zaman bir cevap veren,
hem de her program için,
bir denetleyici: Turing'in imkânsız olduğunu gösterdiği şey tam da bu.

<!-- S59 -->
Kavşağa geri dönelim:
dört sürücü orada sonsuza kadar beklemiyor.

<!-- S60 -->
Biri el sallıyor.
Bir sürücü sırasından vazgeçiyor
ve birkaç saniyede her şey çözülüyor.

<!-- S61 -->
Veritabanı da tam olarak bunu yapar.
Kilitlenmeyi önceden tahmin etmez.
Onu fark eder
ve birini yol vermeye zorlar.

<!-- S62 -->
Bazı problemler daha hızlı bir bilgisayar ister.
Bazıları daha iyi bir fikir.

<!-- S63 -->
Ve bazılarının, bunun gibi,
hiç kusursuz bir çözümü yok.
Sadece iyi kurallar var,
ve el sallamaya hazır biri.
