# Internet Explorer 6 — Bug yang Punya Nama

<!-- S01 -->
Ini bagian dua.

Kalau kamu belum menonton bagian satu,
tautannya ada di bawah.

Tapi ini versi singkatnya.

<!-- S02 -->
Pada 2001
Microsoft merilis
Internet Explorer enam,
dan ia datang bersama Windows XP.

Dalam beberapa tahun
ia menguasai lebih dari sembilan puluh persen
pasar peramban.

<!-- S03 -->
Microsoft memakai itu
untuk mengubah peramban
menjadi platform aplikasi.

Itu gagasan yang sungguhan.

Kebetulan saja yang membayarnya
adalah para pengembang web.

<!-- S04 -->
Itu bagian satu.

Tapi ada yang kulewatkan.

Aku melewatkan bagian
ketika bug-bug itu punya nama.

<!-- S05 -->
Biasanya bug peramban
adalah nomor di pelacak isu.

Issue empat satu tujuh dua.

Tidak ada yang mengingatnya.

Tidak ada yang membicarakannya saat makan siang.

<!-- S06 -->
Di Internet Explorer enam
bug-bug itu punya nama diri.

Dan ternyata itulah hal
yang paling banyak bercerita
tentang seluruh era itu.

<!-- S07 -->
Mulai dari yang ringan.

Kamu mengapungkan sebuah gambar ke kiri
dan menaruh paragraf di sebelahnya.

Teksnya seharusnya duduk
persis di sebelah gambar.

Alih-alih, ia duduk
tiga piksel jauhnya.

<!-- S08 -->
Bukan empat.

<!-- S08b -->
Bukan dua.

<!-- S08c -->
Tiga.

<!-- S08d -->
Setiap kali.

Itu punya nama.

The Three Pixel Jog.

<!-- S09 -->
Sekarang apungkan gambar itu ke kiri
dan beri ia margin kiri
sepuluh piksel.

Internet Explorer enam
memberinya dua puluh.

Ia menggandakan marginnya,
tapi hanya di sisi
tempat kamu mengapungkannya.

<!-- S10 -->
The Double Margin Bug.

Dan perbaikan yang diterima umum
adalah mendeklarasikan
elemen mengapung itu sebagai inline.

<!-- S11 -->
Yang mana omong kosong.

Float itu blok.

Menyebutnya inline
sama sekali tidak berarti apa-apa.

Itu berhasil, jadi orang menulisnya.

<!-- S12 -->
Yang berikutnya lebih bagus.

Kamu memuat sebuah halaman,
dan sebagian isinya
begitu saja tidak ada.

Kamu menggulir ke bawah.

Kamu menggulir kembali ke atas.

Dan ia muncul.

<!-- S13 -->
Tidak ada yang dimuat.

Tidak ada yang berubah.

Ia cuma malu-malu.

Dan namanya pas sekali.

The Peekaboo Bug.

<!-- S14 -->
Obatnya adalah memberi tahu
elemen yang hilang itu
bahwa posisinya relatif.

Tidak ada yang bisa menjelaskan sepenuhnya
kenapa itu mengembalikannya.

<!-- S15 -->
Lalu ada yang ini:
kamu mengarahkan kursor ke sebuah tautan,
dan latar belakang
kotak di bawahnya
terpotong dalam garis lurus.

The Guillotine Bug.

<!-- S16 -->
Ada bug ketika teks
merangkak menjauh dari tempatmu menaruhnya.

Magic Creeping Text.

Ada satu ketika garis tepi
muncul di tempat yang salah,
dengan warna yang salah,
atau tidak muncul sama sekali.

Border Chaos.

<!-- S17 -->
Favoritku lebih senyap.

Kamu menata sederet kotak,
dan huruf-huruf dari kotak terakhir
muncul lagi di bawahnya.

Tidak selalu.

Tidak bisa diduga.

The Duplicate Character Bug.

<!-- S18 -->
Dan yang menentukan apakah
itu terjadi padamu,
dan berapa banyak huruf
yang keluar dobel,
adalah jumlah komentar HTML
yang kamu tinggalkan di markup.

Komentar.

Satu-satunya hal di dalam berkas
yang seharusnya
dibuang oleh peramban.

<!-- S19 -->
Ada satu lagi,
dan yang ini berbeda,
karena orang memakainya
dengan sengaja.

Kalau kamu menetapkan tinggi
dan isinya lebih tinggi,
kotaknya seharusnya meluap.

Internet Explorer enam
malah membesarkan kotaknya.

<!-- S20 -->
Yang mana salah.

Itu juga persis
yang dilakukan tinggi minimum.

Dan Internet Explorer enam
tidak punya tinggi minimum.

Jadi para pengembang berhenti
melaporkan yang satu itu
dan mulai bergantung padanya.

<!-- S21 -->
Berhenti sejenak dan lihat daftar itu.

The Three Pixel Jog.

The Double Margin Bug.

Peekaboo.

The Guillotine.

Kamu tidak menamai bug
yang kamu temui sekali.

<!-- S22 -->
Yang ini punya nama
karena semua orang menemuinya.

Dan inilah bagian
yang membuatnya lebih parah.

Sebagian besar dari mereka punya
penyebab yang sama di bawahnya.

<!-- S23 -->
Di dalam Internet Explorer enam,
setiap elemen entah punya
atau tidak punya
sesuatu bernama layout.

<!-- S24 -->
Itu menentukan apakah elemen
menentukan ukuran dan posisinya sendiri,
atau menyerahkannya ke induknya.

Dan kamu tidak bisa menyetelnya.

<!-- S25 -->
Tidak ada properti
bernama layout,
dan tidak ada cara memintanya.

Ia tidak ada di spesifikasi mana pun.

Ia adalah bendera internal
di dalam mesin render.

<!-- S26 -->
Tapi kamu bisa membaliknya
tanpa sengaja.

Cukup menetapkan lebar.

Cukup menetapkan tinggi.

Cukup membuat elemen mengapung.

Jadi separuh perbaikan di video ini
adalah orang-orang yang membalik sakelar
yang tidak bisa mereka lihat.

<!-- S27 -->
Karena itulah mereka mencari
cara termurah
untuk membaliknya dengan sengaja.

Salah satunya adalah menetapkan tinggi
satu persen.

<!-- S28 -->
Semua peramban lain
harus dijauhkan dari itu,
jadi ia masuk ke dalam sebuah hack
yang akan kita bahas sebentar lagi.

<!-- S29 -->
Dan di Internet Explorer enam
itu tidak berbahaya,
karena kalau isinya tidak muat,
kotaknya memang akan membesar juga.

Bug dari dua menit lalu
itulah yang membuat perbaikannya aman.

<!-- S30 -->
Itu punya nama.

The Holly Hack.

<!-- S31 -->
Cara satunya
adalah properti Microsoft
bernama zoom, disetel ke satu.

Zoom satu berarti
jangan memperbesar.

<!-- S32 -->
Ia tidak mengubah apa pun yang bisa kamu lihat.

Justru itulah intinya.

Ia duduk di lembar gaya
semata-mata untuk menyalakan
sebuah bendera tak terlihat
yang membuat bug-bug itu lenyap.

<!-- S33 -->
Yang membawa kita ke hack,
dan hack adalah tempat
semuanya jadi aneh.

Untuk memperbaiki satu peramban
kamu harus lebih dulu berbicara
hanya kepada peramban itu.

<!-- S34 -->
Dan Internet Explorer enam
berperilaku seolah-olah ada
elemen lain
di atas elemen html.

Tidak ada peramban lain yang begitu.

Itu tidak terdokumentasi.

Memang begitu saja perilakunya.

<!-- S35 -->
Jadi kamu menulis aturan
yang cocok dengan hantu itu,
dan hanya peramban itu
yang bisa melihatnya.

Bintang, spasi, html.

<!-- S36 -->
Semua peramban lain melihatnya,
tidak menemukan yang cocok,
lalu jalan terus.

Itulah star hack,
dan selama bertahun-tahun ia duduk
di hampir setiap lembar gaya
di web.

<!-- S37 -->
Ada juga
underscore hack.

Kamu menaruh garis bawah
di depan nama properti.

<!-- S38 -->
Peramban yang patuh standar
membuang baris itu
sebagai tidak sah.

Internet Explorer enam
mengabaikan garis bawahnya
lalu menerapkannya.

<!-- S39 -->
Jadi kamu sengaja merusak
lembar gayamu sendiri,
dan kerusakan itulah
instruksinya.

<!-- S40 -->
Dan lalu ada yang satu ini,
yang dibuat Microsoft dengan sengaja.

Kamu bisa menulis komentar
yang hanya dipatuhi Internet Explorer.

<!-- S41 -->
Bagi semua peramban lain
itu komentar biasa,
diabaikan sebagaimana komentar diabaikan.

Bagi Internet Explorer enam
itu adalah pintu
menuju versi kedua
dari halaman itu.

<!-- S42 -->
Artinya sang vendor
melihat keadaan,
setuju bahwa peramban ini
butuh lembar gaya sendiri,
lalu merilis fitur
untuk mempermudahnya.

<!-- S43 -->
Sebagian kerusakannya
sama sekali tidak butuh bug.

Internet Explorer enam
punya dua mode.

Di mode modern
ia mengikuti standar.

<!-- S44 -->
Di mode lama,
lebar sebuah kotak
termasuk padding
dan garis tepinya,
yang merupakan angka
yang sama sekali berbeda.

<!-- S45 -->
Mode mana yang kamu dapat
bergantung pada baris pertama
dokumen.

Dan versi HTML
yang sedang dipakai semua orang
menyuruhmu menaruh
deklarasi XML di sana.

<!-- S46 -->
Baris itu mendorong
Internet Explorer enam
ke mode lama.

Mengikuti standar yang lebih baru
justru itulah yang merusaknya.

<!-- S47 -->
Lalu ada transparansi.

Internet Explorer enam tidak bisa
menampilkan PNG bertepi lembut.

Di tempat gambar seharusnya memudar,
ia menaruh warna abu-abu.

<!-- S48 -->
Jawaban Microsoft adalah sebuah filter
dengan nama mirip nomor seri.

Itu berhasil.

<!-- S49 -->
Tapi ia melukis di luar
proses render normal
peramban,
jadi tautan yang kamu taruh di atasnya
sering kali berhenti berfungsi.

Kamu memperbaiki gambarnya
dan merusak tautannya.

<!-- S50 -->
Dan memudarkan apa pun yang lain
adalah filter kedua,
dengan sintaksnya sendiri,
duduk di lembar gaya
tepat di sebelah properti biasa
yang dipahami semua peramban lain.

<!-- S51 -->
Sebagian dari ini bahkan
lebih tua dari bug-bug itu.

Sebelum semuanya,
tata letak dibangun
dari tabel bersarang.

<!-- S52 -->
Dan untuk menahan sebuah celah tetap terbuka
kamu memakai gambar transparan
selebar satu piksel,
diregangkan ke ukuran berapa pun
yang dibutuhkan celah itu.

Itu juga punya nama.

The spacer gif.

<!-- S53 -->
Hover adalah satu lagi.

Di Internet Explorer enam,
hover bekerja pada tautan.

Hanya pada tautan.

<!-- S54 -->
Jadi sebuah menu yang terbuka
saat kamu menggerakkan tetikus
ke atas apa pun selain tautan
membutuhkan program kecil
yang dilampirkan ke lembar gaya.

<!-- S55 -->
Bukan skrip di dalam halaman.

Sebuah berkas terpisah,
dirujuk dari CSS,
berisi kode yang tugasnya
mengajari peramban
satu selektor.

Orang saling mengoper berkas itu
selama bertahun-tahun.

<!-- S56 -->
Bagian satu menyebutkan
bahwa kamu bisa menaruh JavaScript
di dalam lembar gaya.

Yang tidak disebutkan
adalah seberapa sering JavaScript itu berjalan.

<!-- S57 -->
Setiap gerakan tetikus.

Setiap ketukan tombol.

Setiap gulir.

Berulang-ulang,
hanya untuk menghitung satu lebar.

<!-- S58 -->
Dan peramban itu punya batasan
yang tidak dimiliki peramban lain.

Sebuah lembar gaya berhenti berlaku
di suatu titik setelah
empat ribu aturan.

Apa pun setelah lembar gaya
ketiga puluh satu
di sebuah halaman diabaikan.

<!-- S59 -->
Yang terdengar seperti angka
yang tidak akan pernah kamu capai,
sampai situsmu cukup besar
sehingga seseorang harus menulis
langkah build yang tugasnya hanya
menggabungkan lembar-lembar gaya
sebelum dilihat peramban.

<!-- S60 -->
Dan sebagian darinya
sama sekali bukan kosmetik.

Internet Explorer enam
menghitung objek halamannya
dan objek skripnya
dengan dua cara berbeda,
dan tidak ada sisi
yang bisa melihat seluruh lingkarannya.

<!-- S61 -->
Jadi kalau sebuah skrip menunjuk
ke bagian halaman,
dan bagian halaman itu
menunjuk balik ke skripnya,
tidak satu pun pernah dilepaskan.

Biarkan jendela itu terbuka cukup lama
dan peramban memakan mesinmu.

<!-- S62 -->
Tapi yang terbaik
sama sekali bukan bug tata letak.

Kamu menulis tag input.

Kamu memberinya tipe.

Dan kamu lupa tanda sama dengan.
<!-- S63 -->
Itu atribut yang cacat.

Setiap parser yang pernah ditulis
punya jawaban untuk itu.

Abaikan.

Tebak.

Lanjutkan.
<!-- S64 -->
Internet Explorer crash.

Di dalam, ia ingin tahu
apakah bidangnya tersembunyi,
jadi ia membandingkan apa yang kamu ketik
dengan kata hidden.

Kamu tidak mengetik apa pun.
<!-- S65 -->
Jadi ia pergi mengambil
sesuatu yang tidak kamu ketik
dari alamat nol.

Yang seharusnya hanya
crash peramban biasa,
kecuali bahwa kode yang melakukannya
tidak ada di dalam peramban.
<!-- S66 -->
Ia ada di pustaka sistem bersama.

Jadi tiga kata itu
juga menjatuhkan klien surel,
dan panel pratinjau
di pengelola berkas.
<!-- S67 -->
Sebuah jendela yang mendaftar berkas
di mesinmu sendiri,
ditutup oleh sebuah halaman web.

Itu argumen bagian satu
yang datang sebagai laporan crash.

Peramban itu bukan program
yang berjalan di atas sistem.

Ia bagian dari sistem.
<!-- S68 -->
Dan kamu tidak bisa begitu saja
menguji perbaikannya di tempat lain.

Internet Explorer dilas
ke sistem operasi,
jadi satu komputer
menjalankan tepat satu versi.

<!-- S69 -->
Itulah sebabnya pekerjaan front end
pada 2006
datang bersama satu rak
mesin cadangan.

<!-- S70 -->
Dan kemudian bersama satu folder
mesin virtual,
masing-masing membawa
satu sistem operasi utuh
supaya satu halaman
bisa dibuka di dalamnya.

<!-- S71 -->
Dan lalu seseorang melakukan
hal yang sudah jelas.

Kalau kamu bisa mengajari peramban
satu fitur yang hilang,
kamu bisa mengajarinya semuanya.

<!-- S72 -->
Seorang pengembang bernama Dean Edwards
menulis sebuah pustaka
yang seluruh tujuannya
adalah membuat Internet Explorer enam
berperilaku seperti versi
dirinya yang lebih baru.

Orang benar-benar memakainya.

Di lingkungan produksi.

<!-- S73 -->
Dan di situlah hal ini berhenti
menjadi lucu.

Selama hampir satu dekade,
porsi yang cukup besar dari pekerjaan
front end dunia habis untuk
kesalahan satu peramban.

Bukan fitur.

Bukan produk.

Kompensasi.

<!-- S74 -->
Dan itu bertahan karena
hal yang jadi pokok bagian satu.

Perusahaan telah membangun
aplikasi sungguhan di atasnya,
jenis yang hanya jalan di sana,
dan aplikasi-aplikasi itu
tetap harus bekerja hari Senin.

<!-- S75 -->
Jadi peramban yang semua orang
ingin lenyap
adalah peramban yang tak seorang pun
boleh singkirkan.

<!-- S76 -->
Pada 2010,
Google mengumumkan bahwa aplikasinya
sendiri akan berhenti bekerja di sana.

Dan sebuah studio desain di Denver
memutuskan itu layak diberi pemakaman.

<!-- S77 -->
Yang sungguhan.

Sebuah peti mati.

Sebuah pidato perpisahan.

Antara delapan puluh sampai seratus orang
datang menyaksikan sebuah peramban
dikuburkan.

Mereka merencanakannya untuk tiga puluh orang.

<!-- S78 -->
Dan Microsoft mengirim bunga.

Kartunya bertuliskan,
terima kasih atas masa-masa indahnya,
Internet Explorer enam.

<!-- S79 -->
Setahun kemudian, tepat di hari yang sama,
Microsoft meluncurkan sebuah situs web.

Ia melacak berapa banyak bagian dunia
yang masih menjalankan
Internet Explorer enam,
negara demi negara.

<!-- S80 -->
Pada saat itu
angkanya masih dua belas persen.

Targetnya adalah mendorongnya
ke bawah satu persen.

Perusahaan yang membuat peramban itu
menjalankan hitung mundur publik
menuju kematian produknya sendiri.

<!-- S81 -->
Jadi kenapa bug-bug itu punya nama?

Karena kamu menamai hal-hal
yang tidak bisa kamu hindari.

<!-- S82 -->
Tidak ada yang menamai cuaca
di sebuah negara
yang cuma ia lewati.

Kamu menamainya di tempat kamu tinggal.

Dan selama kira-kira sepuluh tahun,
di situlah web tinggal.

<!-- S83 -->
Tapi menyingkirkan Internet Explorer enam
dari web adalah cerita lain.

Dan ke sanalah kita menuju berikutnya.

Kalau kamu mau yang itu,
ada tombol langganan,
dan bagian satu tautannya ada di bawah.
