# Internet Explorer 6 — Peramban yang Menjadi Platform

<!-- S01 -->
Bayangkan Anda seorang pengembang web
di awal tahun 2000-an.

Anda sudah menulis
halaman web yang wajar-wajar saja.

<!-- S02 -->
Halaman itu berjalan dengan baik di Netscape.

Juga di Opera.

Juga di Firefox yang baru.

Lalu Anda membukanya
di Internet Explorer.

Semuanya rusak.

<!-- S03 -->
Tata letaknya salah.

Tombolnya bergeser.

Gambar PNG-nya terlihat buruk sekali.

Dan entah bagaimana,
menambahkan satu ganti baris di HTML Anda
menciptakan celah tiga piksel.

<!-- S04 -->
Selamat datang di pengembangan web
pada zaman Internet Explorer 6.

Tapi inilah bagian menariknya.

Internet Explorer 6
bukan sekadar peramban yang buruk.

<!-- S05 -->
Microsoft berusaha mengatasi masalah
yang memang ada di web.

Mereka cuma punya satu keunggulan besar
dibanding semua orang lain.

Windows.

<!-- S06 -->
Dan akhirnya, keunggulan itu
memungkinkan Microsoft mengubah peramban
menjadi sesuatu yang jauh lebih besar
daripada sebuah peramban.

<!-- S07 -->
Pada pertengahan 1990-an,
web dikuasai
oleh Netscape Navigator.

Microsoft tidak senang soal itu.

<!-- S08 -->
Jadi Internet Explorer
dipaketkan bersama Windows
dan disediakan secara gratis.

Anda membeli komputer Windows.

Internet Explorer sudah ada di sana.

Tidak ada yang perlu diunduh.

Tidak ada yang perlu dibayar.

<!-- S09 -->
Dan yang terpenting,
Microsoft menguasai
sistem operasinya.

Pada awal tahun 2000-an,
Internet Explorer punya
lebih dari sembilan puluh persen
pasar peramban.

<!-- S10 -->
Internet Explorer 6 datang
pada tahun 2001,
bersama Windows XP.

Dan untuk sesaat, kelihatannya
Microsoft memang sudah memenangkan
perang peramban.

<!-- S11 -->
Microsoft punya masalah.

Web sangat terbatas.

HTML bisa menampilkan dokumen.

CSS bisa menatanya.

JavaScript bisa membuatnya interaktif.

<!-- S12 -->
Tapi kurang lebih cuma itu.

Apa pun yang lebih rumit
langsung menabrak
batas peramban.

<!-- S13 -->
Bagaimana kalau Anda mau memindai dokumen?

Atau berkomunikasi dengan kartu pintar?

Atau berkomunikasi dengan perangkat keras
yang terhubung ke komputer Windows?

<!-- S14 -->
Peramban sebenarnya tidak bisa
melakukan hal-hal itu.

Jadi Microsoft mengajukan sebuah solusi.

ActiveX.

<!-- S15 -->
Gagasan dasarnya sederhana.

Kenapa membatasi aplikasi web
pada apa yang bisa dilakukan peramban?

Biarkan saja ia memakai
komponen native Windows.

<!-- S16 -->
Dan tiba-tiba sebuah halaman web
bisa melakukan hal-hal
yang bahkan tidak berani diimpikan
HTML biasa.

<!-- S17 -->
Hari ini, ActiveX kedengarannya menakutkan.

Dan memang beralasan.

Sebuah komponen ActiveX bisa menjangkau
berkas, aplikasi,
perangkat keras,
dan sistem operasi.

<!-- S18 -->
Dari sudut pandang keamanan hari ini,
itu kedengarannya benar-benar gila.

Tapi di awal tahun 2000-an,
itu sangat masuk akal
untuk aplikasi perusahaan.

<!-- S19 -->
Perusahaan tidak mau
penampil dokumen yang cantik.

Mereka mau aplikasi.

Mereka mau halaman web
yang bisa berperilaku
hampir seperti perangkat lunak desktop.

<!-- S20 -->
Dan Microsoft memberi mereka persis itu.

Bahkan Windows Update sendiri
awalnya mengandalkan ActiveX
untuk memeriksa sistem
dan mencari tahu pembaruan mana
yang diperlukan.

<!-- S21 -->
Jadi ActiveX bukan sekadar
kesalahan bodoh.

Ia adalah upaya awal
untuk mengubah peramban
menjadi platform aplikasi.

<!-- S22 -->
Dan dalam arti itu, Microsoft
sebenarnya mendahului zamannya.

Masalahnya adalah seberapa besar kuasa
yang mereka berikan pada platform itu.

<!-- S23 -->
ActiveX bukan satu-satunya
perluasan dari Microsoft.

Ada VBScript.

Ada DHTML.

Bahkan ada CSS expression.

Ya.

<!-- S24 -->
Internet Explorer bisa mengevaluasi
JavaScript langsung di dalam CSS.

Anda bisa melakukan sesuatu seperti ini.

<!-- S25 -->
Itu konyol.

Kadang ternyata
itu juga sangat berguna.

Dan tidak satu pun dijamin
bekerja di tempat lain.

<!-- S26 -->
Microsoft bukan sekadar
mengimplementasikan web.

Microsoft memperluas web
ke arahnya sendiri.

Dan dengan sembilan puluh persen
pasar,
ia punya cukup kuasa
untuk membuat itu berhasil.

<!-- S27 -->
Salah satu contoh paling terkenal
adalah model kotak CSS.

Model standarnya bilang
bahwa kalau sebuah elemen
lebarnya dua ratus piksel,
dengan padding dua puluh piksel
dan garis tepi lima piksel,

<!-- S28 -->
maka lebar totalnya
adalah dua ratus lima puluh piksel.

<!-- S29 -->
Versi Internet Explorer yang lebih tua
membacanya berbeda.

Dalam mode quirks, lebar yang dideklarasikan
bisa mencakup padding
dan garis tepinya.

<!-- S30 -->
Ini belum tentu
cara berpikir yang gila soal lebar.

Bahkan, hari ini kita sering dengan sengaja
memakai persis perilaku semacam itu.

Namanya border box sizing.

<!-- S31 -->
Masalah sebenarnya adalah
bahwa peramban yang berbeda
berperilaku berbeda.

Dan itu berarti
pengembang harus menangani semua perbedaan itu.

Banyak sekali yang harus ditangani.

<!-- S32 -->
Ada sesuatu bernama hasLayout.

Ia bukan properti CSS yang normal.

Ia bukan bagian dari standar.

Tapi ia yang menentukan
bagaimana Internet Explorer
menata elemen.

<!-- S33 -->
Dan kadang tata letak yang rusak
bisa secara misterius diperbaiki
dengan menambahkan satu baris.

zoom: 1

Kenapa?

Karena zoom: 1 bisa memicu
mekanisme hasLayout internalnya.

<!-- S34 -->
Ada masalah
dengan transparansi PNG.

Ada masalah dengan elemen select
yang muncul di atas
popup berposisi absolut,
tidak peduli seberapa tinggi
Anda menyetel z-index.

<!-- S35 -->
Pengembangan web bukan cuma soal
mewujudkan desain Anda.

Tapi juga soal memahami bug
pada mesin peramban tertentu.

<!-- S36 -->
Ini contoh indah yang lain.

Spasi kosong.

Dan yang ini bahkan bukan
salah Internet Explorer.

Anda bisa menaruh dua gambar
persis bersebelahan
di dalam markup,
tanpa apa pun di antara tagnya,
dan mendapat satu hasil.

<!-- S37 -->
Lalu seseorang merapikan HTML-nya
dan menaruh setiap tag di barisnya sendiri.

Dan tiba-tiba ada
celah beberapa piksel di antara gambarnya.

Ganti barisnya jadi bermakna.

<!-- S38 -->
Pemformat kode Anda
bisa benar-benar merusak halaman web Anda.

Dan kalau Anda memakai
versi lama Visual Studio,
ia dengan senang hati akan memformat
HTML Anda untuk Anda.

Terima kasih, Microsoft.

<!-- S39 -->
Para pengembang mengumpulkan
satu kotak perkakas penuh akal-akalan.

Komentar bersyarat.

<!-- S40 -->
Dan kadang HTML yang tampak
benar-benar aneh
yang satu-satunya tujuannya adalah membuat
Internet Explorer berkelakuan baik.

<!-- S41 -->
Anda menulis kode jelek bukan karena
Anda programmer yang buruk.

Anda menulis kode jelek
karena peramban memaksa Anda.

<!-- S42 -->
Internet Explorer juga crash
secara spektakuler, dan sering membuat
semua jendela yang terbuka ikut crash.

<!-- S43 -->
Yang melahirkan kategori hiburan kantor
yang indah.

Hei, coba lihat tautan ini.

Dan dua puluh jendela Internet Explorer
lenyap.

<!-- S44 -->
Inilah web
sebelum peramban dikurung dalam sandbox.

Peramban hari ini bilang begini.

Situs ini tidak tepercaya.

Akan saya isolasi.

<!-- S45 -->
Internet Explorer 6
kadang terasa lebih seperti ini.

Kamu halaman web?

Boleh.

Ini kunci gedungnya.

<!-- S46 -->
Kenapa para pengembang
benar-benar memakai akal-akalan ini?

Karena mereka terpaksa.

<!-- S47 -->
Bayangkan sebuah perusahaan
dengan lima ratus karyawan.

Setiap komputer memakai Windows XP.

Setiap komputer punya Internet Explorer.

<!-- S48 -->
Pengembangnya punya dua pilihan.

Pilihan satu.

Bangun untuk Internet Explorer,
yang sudah dipunyai semua orang.

<!-- S49 -->
Pilihan dua.

Bangun untuk setiap peramban,
uji semuanya di mana-mana,
lalu jelaskan ke departemen TI
kenapa semua orang butuh peramban kedua.

Jawabannya biasanya sudah jelas.

<!-- S50 -->
Mereka tidak memilih
teknologi Microsoft
karena mereka mencintai Microsoft.

Mereka memilih yang memecahkan
masalah pelanggannya.

Dan kadang ActiveX
adalah alat terbaik yang tersedia.

<!-- S51 -->
Dan akhirnya ada yang sudah muak.

Pustaka JavaScript mulai
menyembunyikan perbedaan antar-peramban.

Salah satu yang terpenting
adalah jQuery.

<!-- S52 -->
Alih-alih menulis
penanganan event khusus peramban,
Anda bisa menulis satu baris
yang bekerja di mana-mana.

<!-- S53 -->
Alih-alih berurusan manual
dengan berbagai implementasi AJAX,
Anda bisa memakai abstraksi bersama.

<!-- S54 -->
jQuery tidak membuat
Internet Explorer lenyap.

Tapi ia membuat jauh lebih mudah
untuk berpura-pura ia tidak ada.

Dan bagi pengembang web era itu,
itu hal yang indah.

<!-- S55 -->
Firefox muncul.

Opera terus berkembang.

Safari datang.

Dan akhirnya Google merilis Chrome.

<!-- S56 -->
Perang peramban kembali,
dan kali ini
persaingannya berbeda.

Mesin JavaScript
menjadi jauh lebih baik.

HTML5 datang.

<!-- S57 -->
Peramban itu sendiri mulai mempelajari
semua hal yang sebelumnya
membutuhkan plugin bagi pengembang.

<!-- S58 -->
Video.

Audio.

Canvas.

SVG.

WebGL.

WebSocket.

Dan akhirnya WebRTC.

Web sedang menjadi
sebuah platform aplikasi.

<!-- S59 -->
Yang justru persis
apa yang coba dicapai Microsoft
dengan ActiveX.

Tapi sekarang itu terjadi
lewat standar terbuka.

<!-- S60 -->
Microsoft mencoba sekali lagi.

Silverlight memungkinkan pengembang membangun
aplikasi web yang kaya fitur
memakai C# dan .NET.

Ia bahkan menggerakkan
streaming awal Netflix.

<!-- S61 -->
Tapi web tidak mau plugin selamanya.

Apple menolak mendukung Flash
di iPhone.

Dan tiba-tiba masa depannya bukan ini.

Peramban plus plugin.

Melainkan ini.

Peramban itu sendiri.

<!-- S62 -->
Silverlight lenyap.

Flash lenyap.

ActiveX lenyap.

Dan Internet Explorer
akhirnya lenyap juga.

<!-- S63 -->
Dan di sinilah
ceritanya jadi menarik.

Karena Microsoft
tidak sepenuhnya salah.

Mereka sudah meramalkan dengan benar
bahwa peramban akan menjadi
sebuah platform aplikasi.

<!-- S64 -->
Mereka cuma berusaha sampai ke sana
lewat teknologi berpemilik.

Web sampai ke tujuan yang sama
lewat standar.

<!-- S65 -->
Peramban menang.

Tapi ia menang dengan menjadi
sesuatu dengan kemampuan jauh lebih hebat
daripada peramban
tahun 2001.

<!-- S66 -->
Jadi apakah Microsoft penjahatnya?

Tidak juga.

Dan itulah yang membuat
ceritanya lebih menarik.

<!-- S67 -->
Microsoft punya insinyur-insinyur brilian.

Mereka punya sumber daya yang besar.

Dan mereka membangun banyak teknologi
yang memang benar-benar mendahului zamannya.

<!-- S68 -->
Tapi Microsoft juga punya
posisi pasar yang luar biasa besar.

Dan itu menciptakan
insentif yang berbahaya.

<!-- S69 -->
Kalau hampir semua orang
memakai peramban Anda,
buat apa menunggu standar?

Kenapa tidak langsung menerapkan
solusi Anda sendiri?

Untuk sementara, itu berhasil.

Sampai web yang lain menyusul.

<!-- S70 -->
Hari ini, Internet Explorer sudah tiada.

Perang peramban yang lama
terasa seperti sejarah kuno.

Tapi lihatlah
pasar peramban modern.

Chrome.

Edge.

Opera.

Brave.

Vivaldi.

<!-- S71 -->
Dan banyak yang lain
berbasis Chromium.

Produk yang berbeda.

Sering kali mesin peramban
yang sama di bawahnya.

<!-- S72 -->
Jadi mungkin kita sudah menukar ini.

Satu peramban yang harus didukung semua orang.

Dengan ini.

Satu mesin yang di atasnya semua orang membangun.

Terdengar familier?

<!-- S73 -->
Karena mesin peramban yang dominan
bukan cuma menentukan
bagaimana situs ditampilkan.

<!-- S74 -->
Ia memengaruhi apa yang dibangun pengembang.

Teknologi mana yang jadi populer.

Dan pada akhirnya,
web itu sendiri menjadi apa.

<!-- S75 -->
Namun, ada
satu perbedaan yang sangat penting.

Web hari ini dibangun
di atas standar terbuka.

Firefox masih punya mesinnya sendiri.

Safari punya WebKit.

Chromium sumber terbuka.

<!-- S76 -->
Dan peramban modern
memperbarui dirinya otomatis.

Situasi kita sudah jauh berbeda
dari keadaan
tahun 2003.

<!-- S77 -->
Tapi pertanyaan dasarnya tetap.

Seberapa besar pengaruh
yang boleh dimiliki satu perusahaan
atas sebuah platform
yang dipakai hampir semua orang?

Itulah pertanyaan
yang tidak pernah benar-benar pergi.

<!-- S78 -->
Jadi, apakah Internet Explorer 6 buruk?

Ya.

Kadang buruk secara spektakuler.

<!-- S79 -->
Tapi itu bukan keseluruhan ceritanya.

Ia juga produk zamannya.

<!-- S80 -->
Masalahnya adalah
bahwa Microsoft memenangkan
perang peramban begitu telak
sampai bisa menetapkan aturannya.

<!-- S81 -->
Dan para pengembang web yang membayar harganya.

Mereka mempelajari
misteri hasLayout.

Mereka menemukan bahwa zoom: 1
bisa secara ajaib membereskan banyak hal.

Dan mereka berdoa.

<!-- S82 -->
Dan akhirnya, Internet Explorer
menjadi apa yang selama dua puluh tahun
ia ciptakan sendiri.

Sebuah platform legacy
yang tidak ada lagi yang mau
mendukungnya.

<!-- S83 -->
Web tidak menolak
visi Microsoft.

Ia cuma membangun
versi yang lebih baik darinya.

Dan kalau ada satu hal
yang harus diajarkan era itu kepada kita,
inilah dia.

<!-- S84 -->
Teknologi tidak menjadi standar
cuma karena ia bagus.

<!-- S85 -->
Kadang ia menjadi standar
karena satu perusahaan punya cukup kuasa
untuk membuat semua orang memakainya.

<!-- S86 -->
Dan kadang,
dua puluh tahun kemudian...
kita sadar kita sudah melakukannya lagi.
