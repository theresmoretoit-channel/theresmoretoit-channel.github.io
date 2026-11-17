<!-- S01 -->
İşte bu kanal için
şimdiye kadar yazılmış bütün senaryolar.
158 video,
neredeyse bir buçuk milyon bayt metin.

<!-- S02 -->
Bunları sıradan bir sıkıştırıcıdan geçirin,
adı gzip.
Sonuç yarım megabaytın biraz üzerinde.
Neredeyse üçte ikisi gitti.

<!-- S03 -->
Üstelik hiçbir şey kaybolmuyor.
Dosyayı açın,
her senaryo geri geliyor,
harfi harfine.

<!-- S04 -->
Şimdi bir daha sıkıştırın.

<!-- S05 -->
Dosya büyüyor.
98 bayt daha büyük.

<!-- S06 -->
Üçüncü kez.
98 bayt daha büyük.
Dördüncü kez.
Yine 98.

<!-- S07 -->
İlk tur üçte ikisini atıyor.
İkinci tur hiçbir şey bulamıyor.
Peki neden sıkıştırmaya devam edemiyoruz?

<!-- S08 -->
O ikinci dosyanın içine bakalım.
gzip hiçbir şeyi sıkıştırmamış.
Veriyi olduğu gibi, değiştirmeden kopyalamış,
on altı blok halinde.

<!-- S09 -->
Her bloğa beş baytlık bir etiket eklenmiş.
Küçük bir başlık ve bir son kısım ekleyin,
tam 98 ediyor.

<!-- S10 -->
Sıkıştırıcı atacak bir şey bulamazsa,
veriyi olduğu gibi saklar
ve yalnızca geri açmak için gerekeni ekler.

<!-- S11 -->
Peki ikinci tur neden hiçbir şey bulamadı?
Daha akıllı bir program bulur muydu?

<!-- S12 -->
Böyle bir metin tekrarlarla dolu.
Aynı kelimeler, aynı ifadeler,
aynı küçük sahne işaretleri,
her sahnenin en başında.

<!-- S13 -->
1977'de Jacob Ziv ve Abraham Lempel
basit bir numara yayımladı.
Tekrarı yeniden yazmayın.
Daha önce geçtiği yeri gösterin.

<!-- S14 -->
300 karakter geri gidin
ve sonraki on iki karakteri kopyalayın.
On iki yerine birkaç bayt.

<!-- S15 -->
İkinci numara:
sık geçen harflere kısa kodlar,
nadir olanlara uzun kodlar verin.

<!-- S16 -->
1951'de David Huffman,
MIT'de bir lisansüstü öğrenci,
ya final sınavına girebilirdi
ya da onun yerine bir dönem ödevi yazabilirdi.

<!-- S17 -->
Ödevi Robert Fano vermişti;
amaç en verimli kodu bulmaktı,
hem de tam olarak bu türden.

<!-- S18 -->
Huffman aylarca bir yere varamadı.
Pes etti
ve sınava çalışmaya başladı.
Sonra çözüm birden aklına geldi.

<!-- S19 -->
En nadir iki sembolü alın,
onları tek bir sembolde birleştirin
ve tek bir ağaç kalana kadar tekrarlayın.

<!-- S20 -->
Sonradan bu anı şöyle anlattı:
“hayatımın en eşsiz anı.”

<!-- S21 -->
Fano sınıfa söylememişti:
kendisi de bununla boğuşmuştu,
Claude Shannon da.

<!-- S22 -->
Huffman'ın kodu ikisinin yöntemini de geçti.
Ve kanıtlanabilir ki
bu türden hiçbir kod daha iyisini yapamaz.

<!-- S23 -->
1990'ların başında
Phil Katz iki numarayı birleştirdi,
ZIP dosyaları için.
gzip de aynı yöntemi kullanıyor.

<!-- S24 -->
İlk tur çoktan tüketti
gzip'in bulabildiği örüntüleri.

<!-- S25 -->
Geriye kalanla yapabileceği bir şey yok.
gzip için bu, gürültü gibi görünüyor.

<!-- S26 -->
Ama daha akıllı bir program
gzip'in kaçırdığı örüntüleri görebilir.
Bir gün bir program
ona verdiğiniz her şeyi küçültebilir mi?

<!-- S27 -->
Hayır.
Ve nasıl çalıştığını bilmenize gerek yok
bundan emin olmak için.

<!-- S28 -->
Bütün dosyaları alın,
tam üç bit uzunluğunda olanları.
Sekiz tane var.

<!-- S29 -->
Şimdi daha kısa olanların hepsini sayın.
İki bitlik dört dosya,
bir bitlik iki dosya
ve bir boş dosya.

<!-- S30 -->
Yedi.

<!-- S30b -->
Sekiz dosya var, ama onları koymak için
yalnızca yedi daha kısa yer.

<!-- S31 -->
Hepsi kısalsaydı,
ikisi aynı yeri paylaşmak zorunda kalırdı.
Peki açtığınızda
hangisini kastetmiştiniz?

<!-- S32 -->
Buna güvercin yuvası ilkesi denir
ve her uzunlukta geçerlidir.
Daha kısa dosyalar hep bir tane eksik kalır,
herkese yetmez.

<!-- S33 -->
Yani her dosyayı alıp
bazılarını küçülten her sıkıştırıcı,
başkalarını büyütmek zorundadır.
Kötü yazıldığı için değil.
Gidecekleri başka bir yer yok.

<!-- S34 -->
O 98 bayt,
gzip'in bu bedeli ödeme şekli.

<!-- S35 -->
İstediğiniz sıkıştırıcıyı seçin.
Belli bir boyuttaki tüm dosyalardan
tek bir bayt bile küçültebildikleri
250'de birden azdır.

<!-- S36 -->
Sıkıştırma yine de işe yarıyor,
çünkü bizim ürettiğimiz dosyalar rastgele değil.
Metinler, resimler ve programlar,
örüntülerle dolu.

<!-- S37 -->
Bu, insanların
daha fazlasını vaat etmesini engellemedi.

<!-- S38 -->
1992'de WEB Technologies,
şunu yapabilen bir yazılım duyurdu:
neredeyse her veriyi bir kilobaytın altına indirmek.
Hatta kendi çıktısını bile,
tekrar tekrar.

<!-- S39 -->
Şirketin başkan yardımcısı, yöntemin
“bilgi teorisinin yasalarına
tabi olmadığını” söyledi.
Ürün hiçbir zaman piyasaya çıkmadı.

<!-- S40 -->
Peki fotoğraflar ve müzik
nasıl bu kadar küçülüyor?
Onlar bu kurala hiç uymuyor.

<!-- S41 -->
JPEG aynı haliyle geri gelmez.
Yeterince benzer geri gelir.
Gözünüzün eksikliğini fark etmeyeceği ayrıntılar
temelli atılır.

<!-- S42 -->
Yakınlaştırın,
nereye gittiklerini görebilirsiniz.

<!-- S43 -->
Bu, kayıplı sıkıştırma
ve bambaşka bir oyun.
Bu video öbür tür hakkında.
Her bit geri gelir, birebir.

<!-- S44 -->
Peki gerçekten örüntü içeren dosyalar
ne kadar küçülebilir?
Bunun bir dibi var mı?

<!-- S45 -->
Var.
1948'de bulundu,
hata düzelten kodlar videomuzun da
dayandığı aynı makalede.

<!-- S46 -->
Orada Claude Shannon,
artıklık eklemenin mesajı nasıl koruduğunu gösterdi.
Burada ise
artıklığın ne kadarının atılabileceğini hesapladı.

<!-- S47 -->
Cevabı bir sayıydı,
adını entropi koydu:
sırada ne geleceğini
tahmin etmenin ne kadar zor olduğu.

<!-- S48 -->
Hiçbir kayıpsız kod ortalamada
bu değerin altına inemez.
Ama ona istediğiniz kadar
yaklaşabilirsiniz.

<!-- S49 -->
Peki İngilizce ne kadar öngörülemez?
1951'de Shannon bunu
bir oyunla ölçtü.

<!-- S50 -->
Birine bir metin parçası verdi,
daha önce hiç görmediği bir parça,
ve tahmin etmesini istedi,
harf harf.

<!-- S51 -->
Tahmin yanlışsa,
yeniden tahmin ediyordu,
doğrusunu bulana kadar.

<!-- S52 -->
İnsanların bunda çok iyi olduğu ortaya çıktı.
Yüz harflik bağlamla,
İngilizce yaklaşık bir bit çıktı,
harf başına.

<!-- S53 -->
Bilgisayar her harfi
sekiz bitte saklar.
İnsan okura yaklaşık bir bit yeter.

<!-- S54 -->
Sıkıştırma işte bu farktan yararlanıyor.
gzip kanalın senaryolarını
karakter başına üç bitin altına indirdi.

<!-- S55 -->
Peki bir makine bir bite
ne kadar yaklaşabilir?

<!-- S56 -->
Tam da bunun için bir ödül var.
Adı Hutter Prize
ve 2020'den beri görev tek bir dosya:
İngilizce Vikipedi'nin bir gigabaytı.

<!-- S57 -->
gzip onu üçte birine indiriyor.
En iyi gündelik sıkıştırıcılar
yaklaşık beşte birine.

<!-- S58 -->
Temmuz 2026'da kırılan rekor
yüz milyon baytın biraz üzerinde.
Onda biri.

<!-- S59 -->
Açma programı da hesaba katılıyor.
Boyutu toplama ekleniyor,
yani Vikipedi'yi
programın içine saklayamazsınız.

<!-- S60 -->
Ödül fonu 500.000 avro.
Her yüzde birlik iyileşme
beş bin kazandırıyor.

<!-- S61 -->
Ödülü finanse eden Marcus Hutter nedenini açıklıyor:
“iyi sıkıştırabilmek,
akıllıca davranmakla
yakından ilişkilidir.”

<!-- S62 -->
Çünkü zirvedeki programlar
tekrar aramıyor.
Tahmin ediyor.

<!-- S63 -->
Her karakterden önce,
olası her bir sonraki karakterin
ne kadar muhtemel olduğunu tahmin ediyorlar.
İyi bir tahmin, bir bitin küçük bir kesrine mal olur.

<!-- S64 -->
Bu, Shannon'ın tahmin oyunu,
bu kez bir makine oynuyor.
En iyi oyuncular artık sinir ağları kullanıyor:
sıradakini tahmin etmek üzere eğitilmiş ağlar.

<!-- S65 -->
Bu, zaten sıkıştırılmış dosyalarda bile işe yarıyor.
2016'da Dropbox, kullanıcılarının JPEG'lerini
daha iyi bir tahminleyiciyle yeniden paketlemeye başladı.
Ortalamada beşte birden fazla küçüldüler.

<!-- S66 -->
Her dosya bit bit aynı geri geldi
ve 2017'ye kadar
46 petabayttan fazla yer kazanıldı.
Bu, 46.000 terabayttan fazla demek.

<!-- S67 -->
Bir de devler var.
2023'te DeepMind'daki araştırmacılar
büyük bir dil modelini
sıkıştırıcı olarak kullandı.

<!-- S68 -->
Fotoğraflardan alınmış küçük gri tonlamalı parçalarda
PNG'yi geçti:
orijinal boyutun %48'i,
%58'e karşı.

<!-- S69 -->
Sesli okuma kayıtlarında
FLAC'ı geçti:
%21'e karşı %30.

<!-- S70 -->
Ama bu, model hesaba katılmadan.
Modelin boyutunu ekleyin,
sonuç
140 kat
veriden daha büyük çıkıyor.

<!-- S71 -->
Verisinden büyük bir sıkıştırıcı
hiçbir şey kazandırmamıştır.
Program da tarifin bir parçasıdır.

<!-- S72 -->
Ve bu bizi en tuhaf kısma getiriyor.
İşte π'nin ilk bir milyon basamağı.

<!-- S73 -->
Bunları dört sıkıştırıcıya verin.
En iyisi onları yaklaşık
426.000 bayta indiriyor.

<!-- S74 -->
Şimdi aynı sıkıştırıcılara
bir milyon rastgele basamak verin.
Sonuç aynı,
aradaki fark binde birden az.

<!-- S75 -->
Ama π rastgele oluşmuyor.
Matematiksel bir kurala uyuyor.
İşte o bir milyon basamağın
her birini yazdıran bir program.

<!-- S76 -->
362 bayt.
Dosyadan iki bin kattan fazla daha kısa.

<!-- S77 -->
Sıkıştırıcılar π'nin ardındaki
matematiksel kuralı göremedi.
Yalnızca basamakları görebildiler.

<!-- S78 -->
Verideki bilgiyi ölçmenin
bir yolu şunu sormaktır:
bu veriyi yazdıran bir program
en fazla ne kadar kısa olabilir?

<!-- S79 -->
Bu uzunluğa
Kolmogorov karmaşıklığı denir,
onu tanımlayanlardan birinin adıyla.

<!-- S80 -->
Çoğu verinin kısa bir programı yoktur.
Yine güvercin yuvası ilkesi:
kısa programlar
herkese yetecek kadar çok değil.

<!-- S81 -->
Bir milyon rastgele basamağın
büyük olasılıkla daha kısası yoktur.
π'nin var.

<!-- S82 -->
Peki neden her dosya için
en kısa programı bulmuyoruz?
Çünkü kanıtlanmıştır ki
hiçbir algoritma bunu
her dosya için yapamaz.

<!-- S83 -->
Her program size bir üst sınır verir.
Ama hiçbir şey her zaman söyleyemez
daha kısasının olup olmadığını.
Dibe ulaştığınızı asla bilemezsiniz.

<!-- S84 -->
gzip senaryolardaki tekrarları buldu,
ama fazlasını değil.
Baytları görüyor,
kelimelerin ne anlama geldiğini değil.

<!-- S85 -->
Daha ileri gitmek için bir program
onları daha iyi tahmin etmek zorunda.
Ve metni iyi tahmin etmek
giderek onu anlamaya çok benzemeye başlıyor.

<!-- S86 -->
O halde size bir soru.
Bir program Vikipedi'yi
diğer tüm programlardan daha fazla sıkıştırabilseydi,
onu anladığını söyler miydiniz?
Cevabınızı yorumlara yazın.
