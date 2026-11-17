<!-- S01 -->
Bayangkan kamu punya ide gila.
Kamu ingin membuat satelitmu sendiri.
Bukan satelit komunikasi
senilai satu miliar dolar.
Sesuatu yang kecil.

<!-- S02 -->
Sebuah kotak kira-kira seukuran
sebongkah roti tawar.
Di dalamnya: komputer, panel surya,
radio, beberapa sensor.
Mungkin bahkan kamera.

<!-- S03 -->
Kamu merakitnya di garasi.
Lalu entah bagaimana...
kamu menempatkannya di orbit.
Kedengarannya mustahil.
Tapi tidak.

<!-- S04 -->
Orang-orang sudah melakukan
hal yang hampir persis ini selama bertahun-tahun.
Namanya CubeSat.

<!-- S05 -->
Dan yang mengejutkan
adalah bahwa hal tersulit
bukanlah membuat satelitnya.
Melainkan segala hal lainnya.

<!-- S06 -->
Unit dasarnya disebut 1U —
kira-kira kubus sepuluh sentimeter.
Susun beberapa unit
dan kamu dapat 2U, 3U, 6U
dan yang lebih besar.

<!-- S07 -->
Idenya sederhana.
Alih-alih merancang wahana antariksa baru
dari nol,
kamu memakai ulang ukuran standar
dan antarmuka standar.
Dan tiba-tiba, antariksa terbuka
bagi universitas, startup,
dan mungkin bahkan kamu.

<!-- S07b -->
Ngomong-ngomong, kalau kamu suka video
seperti ini, pertimbangkan untuk berlangganan.

Itu sangat membantu channel ini.

<!-- S08 -->
Jadi apa isi satelit kecil kita
sebenarnya?
Pertama, ia butuh komputer.
Sesuatu harus menjalankan perangkat lunak,
mengendalikan perangkat keras,
dan memutuskan apa yang harus dilakukan.

<!-- S09 -->
Lalu ada daya.
Panel surya menghasilkan listrik.
Baterai menyimpannya
untuk saat satelit
masuk ke bayangan Bumi.

<!-- S10 -->
Lalu komunikasi.
Radio. Antena.
Dan di Bumi,
stasiun bumi yang mendengarkan.

<!-- S11 -->
Lalu sensor.
Suhu. Tegangan. Arus.
Percepatan. Medan magnet.
Dan suatu cara untuk mengetahui
ke arah mana satelit menghadap.
Karena di orbit,
menyebut "atas" ternyata sulit sekali.

<!-- S12 -->
Tapi sebelum kita membuatnya,
ada pertanyaan yang tidak enak.
Berapa harga kotak kecil ini?
Jawabannya...
lebih mahal dari yang terlihat.

<!-- S13 -->
Sebuah CubeSat 1U sederhana
dengan mudah bisa berharga
puluhan ribu dolar —
hanya untuk perangkat keras penerbangan.
Sistem daya. Panel surya.
Baterai. Komputer. Radio.
Kendali sikap. Struktur.
Dan muatannya.

<!-- S14 -->
Lalu datang hal-hal
yang tidak ada di daftar komponen.
Pengujian. Integrasi.
Dokumentasi.
Operasi stasiun bumi.
Perizinan.
Dan akhirnya...
peluncuran.

<!-- S15 -->
Tumpangan untuk CubeSat mungil
bisa berharga puluhan ribu.
Misi lebih besar dan CubeSat lebih besar
mencapai ratusan ribu.
Dan itu hanya untuk
membawa benda itu ke antariksa.

<!-- S16 -->
Dan sekarang
masalah yang bahkan lebih konyol.
Ingat semua komponen tadi?
Bagaimana mungkin semua itu
muat dalam satu kotak mungil?

<!-- S17 -->
Di antariksa, tidak ada tempat
untuk tumpukan elektronik yang asal-asalan.
Setiap sentimeter berarti.
Setiap gram berarti.
Setiap watt berarti.
Satelit adalah teka-teki tiga dimensi
yang harus bertahan dari peluncuran roket.

<!-- S18 -->
Jadi dari mana kamu mendapatkan
semua komponen ini?
Kamu tidak harus merancang
semuanya sendiri.
Ada industri khusus
yang menjual komponen untuk satelit kecil:
komputer, sistem daya,
radio, antena, dan panel surya.
Bahkan ada pasar
yang dibuat khusus untuk komponen CubeSat.

<!-- S18b -->
Dan komponennya juga standar.
Banyak yang memakai satu format papan
dan tinggal disusun bertumpuk,
sehingga bagian dari produsen berbeda
cocok dalam satu unit.
Perusahaan seperti EnduroSat
dan GomSpace menjualnya,
dan satu subsistem bisa berharga
mulai dari beberapa ribu
hingga puluhan ribu dolar.

<!-- S19 -->
Dan ini bukan
prosesor eksotis.
Satu komputer CubeSat masa kini
memakai ARM Cortex-M7,
dengan antarmuka yang familier —
SPI, I²C, UART, dan CAN.

<!-- S19b -->
Dan itu bukan cip antariksa khusus.
Itu papan sungguhan yang dijual bebas,
yang bisa kamu genggam.

<!-- S20 -->
Wahana antariksa butuh sesuatu
yang lebih penting dari kecepatan mentah:
perilaku yang bisa diprediksi,
daya rendah, dan keandalan.
Misi yang lebih menuntut
bisa memakai prosesor ARM Cortex-A —
dan bahkan Linux.

<!-- S20b -->
Tapi ia tidak cepat.
Komputer CubeSat pada umumnya
berjalan pada beberapa ratus megahertz.
Laptopmu berjalan pada
empat atau lima gigahertz,
dengan jauh lebih banyak inti.
Ia menukar kecepatan mentah
demi nyaris tanpa konsumsi daya.

<!-- S21 -->
Dan kalau kamu seorang programmer,
di sinilah jadi menarik.
Kamu tidak menulis
semacam "bahasa antariksa" misterius.
Kamu menulis perangkat lunak tertanam.
Sering dalam C atau C++.

<!-- S22 -->
Ia bisa berjalan langsung
di perangkat keras,
atau di sistem operasi waktu-nyata
seperti FreeRTOS, Zephyr, atau RTEMS.
Bahkan ada framework terbuka
yang dibuat untuk wahana antariksa.
F Prime dari NASA, misalnya,
adalah framework perangkat lunak untuk komputer di wahana antariksa,
bagi sistem tertanam dan penerbangan antariksa.

<!-- S23 -->
Jadi kodemu mungkin terlihat
kurang lebih seperti ini.

<!-- S24 -->
Tapi ada satu perbedaan besar
dari komputer biasa.
Kamu tidak bisa SSH ke dalamnya.
Kamu tidak bisa memasang debugger.
Dan kalau perangkat lunakmu crash...
komputermu berada
beberapa ratus kilometer di atas.

<!-- S25 -->
Jadi ia butuh watchdog,
mode aman, deteksi kesalahan,
dan pemulihan otomatis.
Ia harus memperbaiki beberapa masalah
tanpa kamu di sana untuk membantu.

<!-- S25b -->
Dan salah satu alasan besar ia butuh itu semua
adalah radiasi.
Di antariksa, sinar kosmik
bisa membalik bit di memori,
atau bahkan melumpuhkan cip.
Tidak ada perisai berat —
itu akan terlalu berat.
Sebaliknya, komputer mengawasi dirinya sendiri,
mengoreksi kesalahan,
dan mereset saat ada yang tidak beres.

<!-- S26 -->
Tapi kalau kamu benar-benar
ingin meluncurkannya...
keadaan jadi serius.
Komponen yang berfungsi di mejamu
tidak otomatis siap
untuk roket.
Ia harus bertahan dari getaran,
vakum, suhu ekstrem,
dan radiasi.

<!-- S27 -->
Nah, kembali ke masalah
mengetahui ke arah mana
satelit menghadap.
Bayangkan ia berjungkir
melintasi antariksa.
Tidak ada lantai. Tidak ada langit-langit.
GPS bisa memberitahu
di mana kamu berada...
tapi bukan ke arah mana
kamu menghadap.

<!-- S28 -->
Jadi satelit menggabungkan
giroskop, magnetometer,
dan sensor matahari
untuk menentukan sikapnya.
Lalu ia harus mengubahnya.
Satu trik umum
adalah magnetorquer.

<!-- S29 -->
Ia berinteraksi dengan
medan magnet Bumi
dan menghasilkan torsi kecil.
Ia bukan mesin roket.
Ia tidak menggerakkan satelit.
Ia hanya memutarnya.
Dan itu cukup
untuk mengarahkan satelit
tepat ke tempat yang kamu mau.

<!-- S30 -->
Tapi tak satu pun dari ini
adalah alasan
kita membuat satelit.
Kita butuh sebuah misi.
Itulah muatannya.
Mengukur radiasi.
Memotret Bumi.
Mempelajari atmosfer.
Menguji sensor baru.
Atau sekadar membuktikan
sebuah teknologi baru berfungsi.

<!-- S31 -->
Fungsi utama satelit itu sendiri
adalah menjaga muatannya
tetap hidup.
Memberinya daya. Mengarahkannya.
Menjaganya tetap hangat.
Menyimpan datanya.
Dan mengirimkannya pulang.

<!-- S32 -->
Saat komputer mejamu macet,
kamu me-restart-nya.
Saat satelitmu macet...
kamu punya objek yang sangat mahal
yang diam-diam mengorbit Bumi.

<!-- S33 -->
Jadi katakanlah kita sudah membuatnya.
Semuanya berfungsi...
Komputer menyala...
Radio berbicara.
Panel menghasilkan daya.
Muatan berjalan...
Bisakah kita meluncurkannya?
...Belum.

<!-- S34 -->
Satelit harus membuktikan
ia bisa bertahan dari peluncuran.
Itu berarti pengujian.
Banyak pengujian.

<!-- S35 -->
Pertama, pasang satelitnya dengan baut
ke meja uji getaran raksasa.
Lalu guncangkan kuat-kuat...
Itu pengujian getaran.
Peluncuran roket tidaklah lembut.
Ia harus bertahan dari
kebisingan, getaran, dan guncangan
tanpa ada apa pun
yang terlepas atau patah.
Setiap baut berarti.
Setiap konektor berarti.
Setiap potong kabel berarti.

<!-- S36 -->
Lalu datang vakum.
Di Bumi, udara membantu membuang panas.
Di antariksa, tidak ada udara.
Satu sisi bisa jadi sangat panas,
sisi lain sangat dingin,
dan elektroniknya
tetap harus berada
di dalam batasnya.
Jadi satelit butuh
pita penghantar panas, pelapis,
insulasi,
dan material yang dipilih cermat.
Satelit tidak punya
pendingin ruangan.
Mereka punya fisika.

<!-- S37 -->
Dan baterainya
jadi menarik.
Isi dayanya dengan energi matahari.
Lalu satelit
masuk ke bayangan Bumi,
dan panel hampir tak menghasilkan apa-apa.
Baterai menjaganya tetap hidup.
Lalu kembali ke sinar matahari.
Isi daya. Pakai daya.
Isi daya. Pakai daya.
Lagi dan lagi.
Selama bertahun-tahun.
Satu kesalahan dalam pengelolaan daya
bisa diam-diam mengakhiri misi.

<!-- S38 -->
Dan sekarang, bagaimana kamu bicara dengannya?
Kamu butuh radio.
Antena.
Dan frekuensi
yang secara hukum boleh kamu pakai.
Dan stasiun bumi.
Satelit
tidak punya internet.
Ia hanya melintas di atas
dan memancarkan sinyal.

<!-- S39 -->
Stasiun bumimu
menangkap sinyalnya.
Komputer mendekodekannya.
Dan tiba-tiba kamu punya data
dari wahana antariksamu sendiri.
Bayangkan membuka terminal
dan melihat ini.

Hanya saja mesin
yang mencetak angka-angka itu...
berada ratusan kilometer
di atas kepalamu.

<!-- S40 -->
Jadi bagaimana kita
benar-benar membawanya ke atas sana?
Kamu bisa membuat roket...
Tolong jangan...
Kamu tidak membutuhkannya.
CubeSat terbang
sebagai muatan sekunder.

<!-- S41 -->
Sebuah roket toh sudah akan naik.
Ia punya ruang lebih.
Satelitmu ikut menumpang
dalam deployer standar.
Tidak perlu roket pribadi.

<!-- S42 -->
Dan sekarang ia duduk
di puncak sebuah roket.
Kamu tidak bisa menyentuhnya.
Kamu tidak bisa membuka kotaknya.
Kamu tidak bisa mencolokkan kabel.
Roket meluncur.
Sekitar sembilan menit kemudian,
kamu berada di orbit.

<!-- S43 -->
Deployer
melepaskan satelitmu.
Ia terlontar bebas
dan mulai berjungkir.

<!-- S43b -->
Tapi bagaimana ia tahu ia sudah keluar?
...
Sakelar berpegas yang tadinya tertekan
selama ia berada di dalam deployer
kembali ke posisi semula begitu satelit terlontar,
dan komputer menyala.
Lalu, sesuai aturan,
ia tetap diam sekitar setengah jam.
Baru setelah itu ia menyalakan radionya,
membentangkan antenanya,
dan akhirnya mengirim kabar ke Bumi.
Dan di suatu tempat di Bumi...
stasiun bumimu mendengarnya.

<!-- S44 -->
Kamu telah membuat sebuah mesin.
Dan sekarang mesin itu
mengorbit planet ini.

<!-- S44b -->
Hanya saja, kita belum selesai.
Satelit mati tidak bisa begitu saja
tinggal di atas sana selamanya.
Dibiarkan di orbit selama berabad-abad,
ia menjadi sampah antariksa.

<!-- S45 -->
Itu berarti misi modern
kian harus merencanakan
akhir
dari usia wahana antariksa.
Idealnya, atmosfer atas yang tipis
perlahan menariknya turun.
Orbitnya meluruh.
Ia masuk kembali ke atmosfer.
Dan ia terbakar habis.
Akhir misi...
adalah bagian dari misi.

<!-- S46 -->
Jadi... bisakah kamu membuat
satelitmu sendiri?
Secara teknis, bisa.
Kamu tidak harus menjadi NASA.
Kamu tidak perlu
memiliki roket.
Kamu bahkan tidak selalu butuh
perusahaan besar.

<!-- S47 -->
Satelit harus
bertahan dari peluncuran.
Bertahan di antariksa.
Berkomunikasi secara legal.
Berjalan sendiri.
Dan, pada akhirnya,
menyingkir dari orbit.
Semua itu
harus dibuktikan
sebelum siapa pun
menaruhnya di roket.

<!-- S48 -->
CubeSat tidak membuat antariksa jadi mudah.
Mereka membuatnya terstandar.
Alih-alih membangun semuanya
dari nol,
kamu bisa membangun sesuatu
yang sesuai dengan standar yang ada.
Dan itu perubahan yang mengejutkan besarnya.

<!-- S49 -->
Jadi di suatu tempat, saat ini juga,
ada mesin-mesin mungil
yang mengorbit Bumi.
Dibuat oleh universitas,
tim riset,
perusahaan, dan mahasiswa.

<!-- S50 -->
Beberapa membawa kamera.
Beberapa mengukur radiasi.
Beberapa menguji
teknologi yang benar-benar baru.
Dan beberapa hanya eksperimen
yang menanyakan satu hal:
"bisakah kita membuat benda ini
bekerja di antariksa?"

<!-- S51 -->
Dan itulah yang membuat
kegiatan merakit satelit sendiri
begitu menarik.
Karena jarak
antara kamu dan antariksa
bukan lagi sebuah roket.
Bisa jadi ia...
sebuah kotak sepuluh sentimeter.
Dan sebuah daftar periksa
yang sangat, sangat panjang.
