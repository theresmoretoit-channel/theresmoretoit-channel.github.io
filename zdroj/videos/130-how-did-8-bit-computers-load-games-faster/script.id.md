<!-- S01 -->
Ini ZX Spectrum yang sedang memuat program.

<!-- S02 -->
Dan ini program yang sama,
di komputer yang sama,
dari jenis kaset yang sama.

<!-- S03 -->
Selesainya dalam separuh waktu.
Tidak ada yang berubah di perangkat kerasnya.
Pitanya tidak lebih cepat, tape-nya juga tidak.

<!-- S04 -->
Satu-satunya yang berubah
adalah cara komputer mendengarkan.

<!-- S05 -->
Jadi, bagaimana komputer 8-bit
belajar memuat game lebih cepat?
Dan kalau memang semudah itu,
kenapa tidak dilakukan sejak awal?

<!-- S06 -->
Di video sebelumnya,
kita melihat bagaimana Spectrum menyimpan bit
sebagai pulsa di pita.

<!-- S07 -->
Sepasang pulsa pendek berarti nol.
Pasangan yang dua kali lebih panjang berarti satu.

<!-- S08 -->
Hasilnya sekitar seribu empat ratus bit
setiap detik.
Game yang memenuhi memori 48K
butuh sekitar lima menit.

<!-- S09 -->
Sekarang buat setiap pulsa jadi separuh panjangnya.

<!-- S10 -->
Komputer masih bisa membedakan pendek dan panjang.
Tapi dua kali lebih banyak bit
melewati head pita setiap detik.

<!-- S11 -->
Itulah seluruh trik di balik turbo loader.
Dan ini bukan sekadar eksperimen pikiran.

<!-- S12 -->
Tahun 1984, game Skool Daze
memuat datanya dengan dua kali
kecepatan normal Spectrum.

<!-- S13 -->
Lalu kenapa Spectrum
tidak memuat secepat itu dengan sendirinya?

<!-- S14 -->
Loader bawaannya tersimpan di ROM,
chip memori tempat komputer mulai bekerja.
Ia tidak mengukur pulsa dalam detik.

<!-- S15 -->
Ia menghitung.
Setelah setiap tepi sinyal,
ia menunggu sebentar,
lalu menghitung berapa lama sampai tepi berikutnya.

<!-- S16 -->
Satu angka saja di ROM
menentukan di mana nol berakhir
dan satu dimulai.

<!-- S17 -->
Dan angka itu memberi banyak kelonggaran.
Angka nol bisa memanjang
lebih dari empat puluh persen
dan tetap terbaca sebagai nol.

<!-- S18 -->
Kelonggaran itulah yang membuat pita usang
di tape murahan
tetap bisa dimuat.

<!-- S19 -->
Dan batasnya bukan komputer.
Spectrum memeriksa sinyal dari pita
sekitar enam puluh ribu kali per detik.

<!-- S20 -->
Batasnya adalah kaset.
Pulsa yang lebih pendek berarti nada lebih tinggi.
Pada kecepatan ganda, angka nol
naik dari dua kilohertz ke empat.

<!-- S21 -->
Dan nada tinggi justru yang
paling dulu hilang di tape murahan,
atau kalau head-nya
sedikit miring.

<!-- S22 -->
Sebuah majalah Spectrum tahun 1986 memperkirakan
kebanyakan orang bisa mencapai
setidaknya dua kali kecepatan normal.
Seberapa jauh lagi,
tergantung tape-nya.

<!-- S23 -->
Tapi turbo punya masalah yang lebih aneh.

<!-- S24 -->
Kalau komputer hanya mengenal
format yang lambat,
bagaimana ia memuat program
yang mengajarinya format yang cepat?

<!-- S25 -->
Jawabannya ada di awal pita.
Bagian pertama direkam
dalam format biasa yang lambat.

<!-- S26 -->
Bagian itu pendek,
dan ROM memuatnya seperti program lain.

<!-- S27 -->
Lalu program kecil itu mengambil alih.
Dalam kasus paling sederhana,
itu salinan rutin pemuatan milik ROM sendiri,
dengan beberapa angka yang diubah.

<!-- S28 -->
Di Skool Daze,
perubahannya ada di tiga tempat.
Waktu tunggu lebih pendek, hitungan awal baru,
garis pemisah baru.

<!-- S29 -->
Jadi ROM memuat program
yang mengerjakan tugas ROM, hanya lebih cepat.

<!-- S30 -->
Ini agak mirip mengunduh
pengunduh yang lebih cepat.
Langkah yang lambat memberimu alatnya.
Alat itu mengerjakan sisanya.

<!-- S31 -->
Game komersial memakai ide yang sama.
Salah satu contoh terkenal adalah Speedlock,
pertama kali dipakai Ocean pada 1984.

<!-- S32 -->
Salah satu pembuatnya bilang ia menulisnya
karena ia sudah muak
dengan lamanya loader standar.

<!-- S33 -->
Tapi ini kejutannya.
Speedlock hanya sekitar satu setengah
kali lebih cepat.

<!-- S34 -->
Hari pertama
Daley Thompson's Decathlon
butuh tiga menit dua puluh detik,
padahal data yang sama dengan kecepatan normal
akan butuh empat menit empat puluh tujuh detik.

<!-- S35 -->
Versi-versi berikutnya hanya sekitar
seperlima lebih cepat dari ROM.
Karena kecepatan bukan satu-satunya tugasnya.

<!-- S36 -->
Sejak 1983, program penyalin
bisa membaca header sebuah game
dan menyalin seluruh game ke pita lain.

<!-- S37 -->
Format buatan sendiri
tidak memberi program itu apa pun untuk dibaca.

<!-- S38 -->
Speedlock awal bahkan memotong nada pembukanya
menjadi semburan-semburan pendek,
supaya loader milik ROM sendiri
sama sekali tidak mengenalinya.

<!-- S39 -->
Dan itu bisa didengar.
Pita Speedlock dimuat dengan bunyi klik,
dan garis-garis yang bergerak patah-patah di tepi layar.

<!-- S40 -->
Ini tidak menghentikan siapa pun menyalin
pita dari satu tape ke tape lain.
Tapi ini memberi penerbit
alasan untuk menulis loader sendiri.

<!-- S41 -->
Di Commodore 64,
alasan untuk beralih jauh lebih besar.

<!-- S42 -->
Rutin bawaannya
merekam semuanya dua kali,
sebagai salinan cadangan.
Game empat puluh kilobyte butuh
sekitar dua belas setengah menit.

<!-- S43 -->
Dan di sini, tape-nya
hampir tidak melakukan apa pun yang canggih.
Ia hanya mengubah suara
menjadi pulsa nyala-mati yang bersih.

<!-- S44 -->
Komputer mengukur waktu setiap pulsa sendiri,
lewat software.

<!-- S45 -->
Jadi loader yang lebih cepat
hanyalah program yang berbeda.

<!-- S46 -->
Tahun 1985, majalah Compute!
menguji satu loader bernama TurboTape.

<!-- S47 -->
Begitu menemukan program di pita,
ia memuat dua belas kilobyte
dalam dua puluh delapan detik.

<!-- S48 -->
Drive disket buatan Commodore sendiri
butuh tiga puluh empat detik.

<!-- S49 -->
Sebuah kaset,
mengalahkan disket.

<!-- S50 -->
Dan karena komputer sendiri
yang mendengarkan semuanya,
ia bisa mengerjakan hal lain di sela-selanya.

<!-- S51 -->
Loader seperti Freeload
mendahulukan pembacaan pita.
Sisa waktu prosesor
dipakai untuk musik, scrolling yang mulus,
bahkan game kecil.

<!-- S52 -->
Dengan Invade-a-Load dari Mastertronic,
kamu memainkan klon Space Invaders
sementara game utamanya dimuat.

<!-- S53 -->
Komputer 8-bit Atari
lain lagi ceritanya.

<!-- S54 -->
Di sini, tape-nya yang mendengarkan.
Di dalamnya ada dua filter,
satu untuk tiap nada,
dan sirkuit yang menyerahkan ke komputer
angka satu dan nol yang sudah jadi.

<!-- S55 -->
Standarnya enam ratus bit per detik,
dan filter-filter itu membatasi
seberapa jauh kecepatannya bisa dinaikkan.

<!-- S56 -->
Software yang cerdik bisa menaikkannya
sedikit, paling tinggi sekitar seribu dua ratus.
Tapi untuk jauh lebih cepat,
kamu harus membongkar tape-nya.

<!-- S57 -->
Dan di Cekoslowakia, orang melakukannya.

<!-- S58 -->
Drive disket di sana
harganya dua sampai tiga kali
harga komputernya sendiri.
Jadi kebanyakan pemilik Atari di sana tetap memakai pita.

<!-- S59 -->
Tahun 1987, seorang mahasiswa Praha
dari klub Atari setempat
merancang Turbo 2000.

<!-- S60 -->
Ia menambahkan satu jalur baru untuk sinyal.
Sebuah kabel di dalam tape mengambil suara
langsung dari penguatnya,
sebelum filter,
melewati satu chip kecil,
lalu ke jalur menuju komputer.

<!-- S61 -->
Sebuah sakelar yang dikendalikan komputer
memilih antara jalur lama dan jalur baru.

<!-- S62 -->
Kini komputer mengukur waktu pulsa sendiri.
Sekitar dua ribu tiga ratus bit
per detik.
Hampir empat kali lebih cepat.

<!-- S63 -->
Turbo bukan satu format universal.

<!-- S64 -->
Kadang kamu cukup mengganti programnya.
Kadang, kamu harus mengubah mesinnya.

<!-- S65 -->
Dan lebih cepat itu ada harganya.

<!-- S66 -->
Compute! memperingatkan bahwa rekaman TurboTape
kadang menolak dimuat
di tape lain
yang head-nya disetel sedikit berbeda.

<!-- S67 -->
Penyimpanan standar, katanya,
jauh lebih lambat,
tapi sangat bisa diandalkan.

<!-- S68 -->
Merekam semuanya dua kali
bukan karena Commodore malas.
Itu harga untuk pemuatan yang andal.

<!-- S69 -->
Tapi loader yang berbeda
juga bisa melakukan hal tak terduga.
Ia bisa membaca pita
yang ditolak loader bawaan.

<!-- S70 -->
Di Sharp MZ-800,
komputer yang sampai
ke Cekoslowakia pada akhir 1980-an,
para pemiliknya mengenal program bernama Turbo Copy.

<!-- S71 -->
Sebuah game gagal dimuat,
dengan error checksum.
Para pemilik mendapati Turbo Copy
sering tetap bisa memuatnya.

<!-- S72 -->
Lalu kamu menyimpannya dengan kecepatan normal
ke kaset baru,
dan komputer
bisa memuatnya dengan normal lagi.
Rasanya seperti memperbaiki game yang rusak.

<!-- S73 -->
Jadi bagaimana satu loader bisa membaca
apa yang tidak bisa dibaca loader lain?

<!-- S74 -->
ROM Sharp merekam setiap blok dua kali,
sekitar seribu dua ratus bit per detik.

<!-- S75 -->
Dan ia tidak pernah mengukur pulsa.
Setelah setiap pulsa dimulai,
ia menunggu selama waktu yang tetap,
lalu melihat sekali.

<!-- S76 -->
Masih tinggi?

<!-- S76b -->
Berarti satu.

<!-- S76c -->
Sudah rendah?

<!-- S76d -->
Berarti nol.

<!-- S77 -->
Stopwatch yang disetel sebelumnya.

<!-- S78 -->
Di pita lama, atau di tape yang berbeda,
tepi pulsanya jadi sedikit lebih landai.
Akibatnya, sekali melihat saja
bisa salah membaca level sinyal.

<!-- S79 -->
Satu bit yang salah merusak checksum.
Kalau kedua salinan gagal,
pemuatannya gagal.

<!-- S80 -->
Turbo Copy mendengarkan dengan cara lain.
Ia mengukur waktu setiap pulsa
dengan chip timer komputer.

<!-- S81 -->
Dan sebelum setiap blok,
ia mendengarkan nada pembuka,
lalu menetapkan garis pemisahnya
dari pulsa yang benar-benar ia dengar.

<!-- S82 -->
Stopwatch-nya disetel
sesuai pita yang ada di depannya.

<!-- S83 -->
Dan perbaikannya bukan salinan suara.
Turbo Copy menyimpan byte-nya,
lalu menulis sinyal yang benar-benar baru,
dengan waktu pulsa yang tepat.

<!-- S84 -->
Datanya tidak hilang.
Cara biasa untuk membacanya
saja yang kurang bagus.

<!-- S84b -->
Turbo Copy juga bisa menyimpan game dengan turbo,
dua atau tiga kali kecepatan normal,
dengan loader kecilnya sendiri di depan.

<!-- S85 -->
Dan itulah kesamaan
dari semua cara ini.

<!-- S86 -->
Kasetnya tetap sama.
Yang berubah adalah cara membacanya.

<!-- S87 -->
Sekarang kita berharap game langsung termuat.
Di tahun 1980-an, memuat adalah bagian dari game.
Kamu mendengarkan pita.
Kamu menonton garis-garisnya.
Kamu menunggu.

<!-- S88 -->
Dan kadang, loader yang berbeda
membuat kaset yang sama berperilaku
seperti di mesin yang sama sekali lain.

<!-- S89 -->
Komputer tidak butuh pita yang lebih cepat.
Ia butuh cara mendengarkan yang lebih baik.

<!-- S90 -->
Jadi, ini pertanyaan untukmu.
Dulu kamu pernah pakai turbo loader?
Seperti apa kenanganmu tentang loader itu?
Apakah lebih sering gagal?
Tulis di kolom komentar.

<!-- S91 -->
Dan terakhir, seluruh pita turbo,
dari awal sampai akhir.
Pertama bagian dengan kecepatan normal,
lalu turbonya.
Untuk program sekecil ini,
turbo tidak sepadan.
Loader-nya makan waktu lebih lama
daripada waktu yang dihematnya.
Untuk satu game utuh, turbo bisa menghemat beberapa menit.
