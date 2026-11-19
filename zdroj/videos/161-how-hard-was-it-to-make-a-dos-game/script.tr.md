<!-- S01 -->
1993'te Doom adlı bir oyun
4 megabayt belleği olan
bir bilgisayarda çalışıyordu.

<!-- S02 -->
Bu, aşağı yukarı telefonundaki
tek bir fotoğrafın boyutu.

<!-- S03 -->
3D hızlandırıcı yoktu.
Tüm görüntü işlemeyi
ana işlemci yapıyordu.

<!-- S04 -->
Bugün bir geliştirici bir oyun motoruyla başlar,
Unity ya da Unreal gibi,
grafiği, sesi,
belleği ve donanımı o yönetir.

<!-- S05 -->
DOS'ta bunların hepsi
geliştiricinin derdiydi.
Ve oldukça sık, oyuncunun da.

<!-- S06 -->
Peki DOS için oyun yapmak
ne kadar zordu?

<!-- S07 -->
Bellekle başlayalım,
çünkü bellek tam bir karmaşaydı.

<!-- S08 -->
1981 tarihli ilk IBM PC
1 megabayt belleği adresleyebiliyordu.

<!-- S09 -->
Ama yalnızca ilk
640 kilobayt
programlar içindi.

<!-- S10 -->
Kalan 384 kilobayt
video belleğine, genişleme kartlarına
ve BIOS'a ayrılmıştı.

<!-- S11 -->
On yıldan uzun bir süre boyunca
DOS programları normalde
bu alanın içinde başlatıyordu.
Ötesine geçmek ekstra iş demekti.

<!-- S12 -->
O ünlü söz de buradan geliyor:
640K herkese yeter.

<!-- S13 -->
Genellikle Bill Gates'e mal edilir.
Bunu söylediğine dair hiçbir kayıt yok,
ve kendisi de inkâr ediyor.

<!-- S14 -->
Doksanların başında
bir PC 4 megabaytla geliyordu,
ya da 8.

<!-- S15 -->
Yine de bir oyun
şu sözlerle durabiliyordu:
"yetersiz bellek".

<!-- S16 -->
Belleğe sahip olmak
ve onu kullanabilmek
iki ayrı şeydi.

<!-- S17 -->
Bir çözüm genişletilmiş bellekti,
yani EMS.

<!-- S18 -->
64 kilobaytlık bir pencere
o ilk megabaytın
üst kısmında dururdu.
Program bu pencereden
4 sayfa ek bellek görebilirdi,
her biri 16 kilobaytlık,

<!-- S19 -->
ve onları başkalarıyla değiştirebilirdi,
tıpkı bir kitabın sayfalarını
kâğıttaki bir delikten çevirmek gibi.

<!-- S20 -->
Bir başka yol da uzatılmış bellekti,
HIMEM adlı bir sürücüyle erişilen.

<!-- S21 -->
İşte burada
geliştiricinin sorunu
oyuncunun sorunu oldu.

<!-- S22 -->
Fare, CD sürücüsü
ya da ses kartı sürücüleri
o değerli bellekten bir lokma alıyordu,
tabii onları üst belleğe yüklemeyi başaramadıysan.

<!-- S23 -->
Böylece oyuncular iki dosyayı düzenlemeyi öğrendi:
CONFIG.SYS ve AUTOEXEC.BAT.

<!-- S24 -->
Bir oyun EMS istiyordu.
Bir diğeri onun kapalı olmasını,
NOEMS adlı bir ayarla.
Üçüncüsü ise her boş kilobayta muhtaçtı.

<!-- S25 -->
1993'te MS-DOS 6,
açılışa bir menü ekledi.

<!-- S26 -->
Oynamak istediğin oyun için
yapılandırmayı seçiyordun,
ve bilgisayar o oyun için açılıyordu.

<!-- S27 -->
Bazı insanların sonunda
sahip oldukları neredeyse her oyun için
ayrı bir girdisi oluyordu.

<!-- S28 -->
Ama o zamana kadar
büyük oyunlar DOS'un sınırlarını
aşmanın bir yolunu bulmuştu.

<!-- S29 -->
386'dan beri
işlemcinin kendisi
32 bit korumalı modda çalışabiliyordu,
4 gigabayta kadar yer sunarak.

<!-- S30 -->
Korumalı moda
daha önceki bir videoda bakmıştık.
Ama DOS onu kullanamıyordu.

<!-- S31 -->
Bu yüzden oyunlar kendi yardımcılarını getirdi:
bir DOS extender.
En bilineni DOS/4GW'ydi.

<!-- S32 -->
Popüler bir derleyiciyle birlikte geliyordu:
Watcom C.

<!-- S33 -->
Bir oyun başladığında
DOS/4GW işlemciyi
korumalı moda geçirir,
oyuna DOS sınırının ötesindeki
belleğe erişim sağlardı.

<!-- S34 -->
DOS hâlâ alttaydı
ve dosya erişimi gibi hizmetler sunuyordu.
Ama oyun artık korumalı modda çalışıyordu,
geleneksel bir DOS programı olarak değil.

<!-- S35 -->
Doksanlarda DOS oyunları oynadıysan
onun adının ekranda
bir anlığına geçtiğini görmüşsündür.

<!-- S37 -->
Şimdi görüntüye gelelim.
En yaygın kullanılan VGA modlarından birinde,
Mode 13h denen modda,
ekran 320'ye
200 pikseldi,
256 renkle.

<!-- S38 -->
Her piksel bir bayttı.
Bir pikseli boyamak için
belleğe bir sayı yazardın.
Grafik kütüphanesi yok. Sadece bellek.

<!-- S39 -->
Tüm ekran
64.000 bayt tutuyordu.

<!-- S40 -->
Bu, 64 kilobaytın biraz altında,
tek bir segmente sığacak kadar küçük;
segment, 16 bitlik bir programın
tek seferde adresleyebildiği bloktu.
Bir kez olsun, bellek senin tarafındaydı.

<!-- S41 -->
Ama doğrudan
görünen ekrana çizersen
oyuncu yarım kalmış resimler görür
ve görüntü titrer.

<!-- S42 -->
Bu yüzden oyunlar her kareyi
önce gizli bir tampona çizer,
sonra bitmiş görüntüyü
video belleğine kopyalardı.

<!-- S43 -->
1991'de programcı ve yazar
Michael Abrash
daha iyi bir yöntem yayımladı.
Adını Mode X koydu.

<!-- S44 -->
VGA'nın, çoğu programcının
hiç dokunmadığı
bir bölümünü kullanıyordu.

<!-- S45 -->
Kare pikseller sağlıyordu,
video belleğinde de
birkaç ekranlık yer.

<!-- S46 -->
Oyun kimsenin göremediği
bir ekrana çizer,
sonra basitçe ona geçerdi.
Ama programlaması çok daha zordu.

<!-- S47 -->
Sonra ses vardı.
Ve ses bir piyangoydu.

<!-- S48 -->
PC'nin kendi hoparlörü
bip sesi için yapılmıştı.

<!-- S49 -->
Sonra ses kartları
ve başka ses donanımları geldi.
Hiçbiri
diğeriyle aynı şekilde çalışmıyordu.

<!-- S50 -->
AdLib, müzik sentezleyen
bir Yamaha çipiyle.
Sound Blaster ise kaydedilmiş sesi
de çalabiliyordu.

<!-- S51 -->
Roland MT-32,
daha zengin enstrümanlara sahip pahalı bir kutu.
Gravis UltraSound.

<!-- S52 -->
Hepsini desteklemek
farklı sürücüler yazmak demekti.

<!-- S53 -->
Ve oyunun kartın nerede olduğunu
bilmesi gerekiyordu.
Portunu, kesmesini
ve DMA kanalını.

<!-- S54 -->
Sound Blaster için olağan cevap
port 220, IRQ 7, DMA 1'di.
Genellikle.

<!-- S55 -->
Birini yanlış girersen
oyun sessiz kalırdı.
Ya da donardı.

<!-- S56 -->
1991'de John Miles adlı bir programcı
birçok ses kartıyla
tek bir arayüz üzerinden konuşan
bir kütüphane yayımladı.

<!-- S57 -->
Bir oyun ses kodunu bir kez yazar,
kartla uğraşmayı kütüphaneye bırakabilirdi.

<!-- S58 -->
Bu, oyunla donanım arasında
bir katman daha demekti.
Bunu aklında tut.

<!-- S59 -->
Sonra hız vardı.
Programcılar işlemcinin attığı
her adımı sayıyordu.

<!-- S63 -->
Ekranda bir pikseli bulmak için
satır numarasını
320 ile çarparsın.

<!-- S63b -->
Eski işlemcilerde
çarpma pahalı olabiliyordu.

<!-- S64 -->
Ama 320,
256
artı 64'tür.
İkisi de ikinin kuvveti.

<!-- S65 -->
Yani çarpmayı
iki bit kaydırma ve bir toplamayla değiştirebilirsin.

<!-- S67 -->
Chris Sawyer en alt seviyeye kadar indi.
1994'te Transport Tycoon'u
neredeyse tamamen assembly diliyle yazdı,

<!-- S68 -->
yani işlemcinin bizzat anladığı
komutlarla,
tek tek.

<!-- S69 -->
Ve bazen
bunların hepsi bile yetmiyordu.

<!-- S70 -->
1990'da Wing Commander'da
ekibin bulamadığı bir hata vardı
ve teslim tarihi yaklaşıyordu.

<!-- S71 -->
Oyundan çıktığında
bellek yöneticisi
bir hata mesajıyla çöküyordu.

<!-- S72 -->
Bunun üzerine programcı Ken Demarest
bellek yöneticisini
bir hex editörde açtı
ve o mesajın metnini değiştirdi.

<!-- S73 -->
Artık şöyle diyordu:
"Wing Commander oynadığın için teşekkürler."

<!-- S74 -->
Sonra ekip asıl hatayı buldu
ve şaka hiçbir zaman yayımlanan oyuna girmedi.

<!-- S74b -->
Bazı oyuncular hâlâ onu gördüklerinden emin.
Ve sonraki Origin oyunları
gerçekten de böyle veda ediyordu.

<!-- S75 -->
Bu da bizi Doom'a geri getiriyor.

<!-- S76 -->
Doom DOS/4GW kullanıyordu
ve 32 bitlik bir program olarak çalışıyordu.

<!-- S77 -->
Kayan nokta donanımı
her PC'de garanti değildi.

<!-- S78 -->
Bu yüzden Doom sabit nokta aritmetiği kullandı.
Tam sayılar,
alt 16 biti
kesirli kısmı temsil eden.

<!-- S79 -->
Ve dünyası
gerçekten üç boyutlu değildi.

<!-- S80 -->
Her bölüm düz bir kat planıdır,
her zemin ve her tavan için
bir yükseklikle.

<!-- S81 -->
Bir oda asla başka bir odanın üstünde olamaz.
Ve yukarı ya da aşağı düzgünce bakamazsın.

<!-- S82 -->
Bir bölüm oynanabilir hale gelmeden önce
bir araç haritayı
bir ikili ağaca, bir BSP'ye bölüyordu.

<!-- S83 -->
Motor bu ağacı
önden arkaya doğru dolaşır,
oyuncunun tarafından başlayarak,
ve görünmeyen alanları atlar.

<!-- S84 -->
Ve Doom DOS'ta yazılmadı bile.

<!-- S85 -->
id Software onu
NeXT iş istasyonlarında geliştirdi
ve sonucu DOS için derledi.

<!-- S86 -->
Doom genel amaçlı bir 3D motor değildi.
Tam olarak
tek bir dünya türü için yapılmıştı.
Bu uzmanlaşma
onun bir 386'da çalışmasına yardım etti.

<!-- S87 -->
Ve başka stüdyolar o dünyayı istedi.

<!-- S88 -->
Raven Software, Doom'un motorunu
1994'te Heretic
ve 1995'te Hexen için lisansladı.

<!-- S89 -->
Doom, oyun yapmanın
yeni bir yolunun yerleşmesine yardım etti.
Stüdyolar her şeyi sıfırdan kurmak yerine
var olan bir motoru lisanslayabiliyordu.

<!-- S90 -->
Bir bellek genişletici.
Bir ses kütüphanesi.
Lisanslı bir motor.

<!-- S91 -->
Her biri geliştiricinin üzerinden
bir sorunu kaldırdı.
Ve katmanlar büyümeye devam etti,
ta ki bugün geliştiricilerin
başlangıç noktası olan motorlara dönüşene kadar.

<!-- S92 -->
Peki o zamanlar oyun yapmak daha mı zordu?
Birçok açıdan, evet.

<!-- S93 -->
Ama zorluk ortadan kalkmadı.
Yer değiştirdi.

<!-- S94 -->
Bugün geliştiriciler
birkaç yüz kilobayt yerine
gigabaytlarca varlık
ve milyonlarca poligonla boğuşuyor.

<!-- S95 -->
DOS'ta oyuncu bile
belleğinin nereye gittiğini bilmek zorundaydı.

<!-- S96 -->
O zaman sana bir sorum var.
Sırf tek bir oyunu çalıştırmak için
bir açılış menüsü kurduğunu hatırlıyor musun?
Ve bu bir eziyet miydi,
yoksa eğlencenin yarısı mı?
Yorumlarda bana yaz.
