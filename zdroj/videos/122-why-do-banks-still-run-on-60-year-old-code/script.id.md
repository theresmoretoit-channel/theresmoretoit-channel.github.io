<!-- S01 -->
999 pound
dan 99 pence.
Tambahkan satu penny.

<!-- S02 -->
Hasilnya nol.

<!-- S03 -->
Tanpa pesan error. Tanpa crash.
Hanya nol, diam-diam tercatat di rekening.

<!-- S04 -->
Di COBOL, kalau field untuk sebuah hasil
terlalu kecil untuk menampungnya,
digit yang berlebih bisa begitu saja hilang.
Kecuali programnya minta diperingatkan,
perhitungannya jalan terus.

<!-- S05 -->
Ia juga tidak membulatkan.
2 pound dan 34,5 pence,
disimpan dengan ketelitian satu penny,
menjadi 2,34.

<!-- S06 -->
Tulis satu kata tambahan, ROUNDED,
dan hasilnya jadi 2,35.

<!-- S07 -->
Keduanya bukan bug.
Itu aturan.
Dan banyak bank di dunia
masih berjalan di atas aturan seperti ini.

<!-- S08 -->
COBOL adalah bahasa pemrograman
dari tahun 1959.
Tak semua program dalam COBOL setua itu.
Tapi bahasanya iya,
begitu juga kebiasaannya.

<!-- S09 -->
Jadi kenapa bank belum menggantinya?
Uang mereka punya.
Insinyur mereka juga punya.

<!-- S10 -->
Untuk tahu, kita lihat tiga kasus nyata.
Bank yang mencoba meninggalkan sistem lamanya,
bank yang berhasil melakukannya,
dan krisis yang membuat semua orang menyalahkan COBOL.

<!-- S11 -->
Tapi pertama, setengah penny yang hilang tadi.

<!-- S12 -->
Misalkan kamu menulis ulang program bank itu
dalam bahasa modern.
Kamu mungkin akan memperbaiki aturan-aturan itu.
Overflow menjadi error.
Setengah penny dibulatkan ke atas.

<!-- S13 -->
Lebih rapi. Lebih aman.
Dan sekarang, di mana pun muncul setengah penny,
hasil programmu berbeda dengan program lama.

<!-- S14 -->
Bahasa modern bisa menghitung desimal dengan tepat.
Java punya tipe data khusus untuk itu.
Tapi bahkan di situ,
aturan pembulatannya tetap sebuah pilihan.

<!-- S15 -->
Satu pengaturan umum membulatkan setengah ke atas:
2,35.
Yang lain membulatkan ke digit genap terdekat:
2,34.
Keduanya benar. Hanya satu yang cocok.

<!-- S16 -->
Dan dengan floating point biasa,
jenis yang dipakai kebanyakan kode secara default,
hasilnya makin aneh.
Nol koma satu ditambah nol koma dua
bukan nol koma tiga.

<!-- S17 -->
Jadi mengganti COBOL bukan sekadar menerjemahkan.
Ini soal menemukan setiap aturan seperti ini,
di antara jutaan baris kode,
dan menjaga masing-masing persis seperti semula.

<!-- S18 -->
Bagaimana COBOL bisa sampai ke sana sejak awal?

<!-- S19 -->
Pada Mei 1959,
Departemen Pertahanan AS
mengadakan rapat di Pentagon.
Pembuat komputer, lembaga pemerintah,
dan perusahaan besar datang,
semuanya dengan masalah yang sama.

<!-- S20 -->
Setiap komputer punya bahasanya sendiri.
Program penggajian yang ditulis untuk satu mesin
tidak berguna di mesin lain.

<!-- S21 -->
Sebuah komite merancang bahasa bersama
untuk dunia bisnis.
Pengaruh terbesarnya adalah FLOW-MATIC,
dari tim Grace Hopper di Remington Rand.

<!-- S22 -->
Dan pada Desember 1960,
program COBOL yang pada dasarnya sama
berjalan di dua komputer
dari produsen yang saling bersaing.
Itulah intinya.

<!-- S23 -->
Ia dirancang agar mudah dipahami orang.
ADD PAYMENT TO ACCOUNT-BALANCE.
Kamu mungkin bisa menebak apa fungsinya.

<!-- S24 -->
Dan ia menyimpan uang seperti orang menulisnya:
sebagai digit desimal.
Tanda desimalnya
bahkan tidak perlu disimpan.
Deskripsi field-nya menentukan letaknya:
dua digit terakhir adalah pence.

<!-- S25 -->
Pada 1964, IBM meluncurkan System/360.
Desainnya mencakup instruksi
untuk aritmetika desimal.

<!-- S26 -->
Dan sejak itu IBM merancang mainframe-nya
agar tetap kompatibel.
Banyak program lama masih bisa berjalan
di mesin masa kini
tanpa perlu ditulis ulang.

<!-- S27 -->
Jadi jarang ada saat
yang memaksa siapa pun untuk pindah.
Setiap tahun kodenya tetap berjalan,
dan setiap tahun ia mengumpulkan aturan baru.
Produk baru, pajak baru, regulasi baru,
pengecualian baru.

<!-- S28 -->
Belum ada yang menghitung berapa banyak COBOL
yang masih berjalan di seluruh dunia.
Tapi menurut IBM, 45
dari 50 bank terbesar di dunia
masih memakai mainframe-nya.

<!-- S29 -->
Dan sebagian pemiliknya sudah menghitung.
Pada 2017, Badan Jaminan Sosial AS
menyatakan bahwa sistemnya berisi
lebih dari 60 juta baris COBOL.

<!-- S30 -->
Pada 2025, auditor pemerintah AS
mendaftar sebelas sistem federal
yang paling perlu diganti.

<!-- S31 -->
Usianya antara 23
hingga 60 tahun,
dan biaya operasinya sekitar
750 juta dolar per tahun.

<!-- S32 -->
Jadi kodenya tua, ada di mana-mana,
dan penuh aturan yang tak pernah dicatat siapa pun.
Tentu bahayanya justru kalau tetap dipakai.

<!-- S33 -->
Mari kita lihat apa yang terjadi
ketika sebuah bank meninggalkannya.

<!-- S34 -->
Pada 2018, bank Inggris bernama TSB
punya sekitar lima juta nasabah,
dan sebuah masalah.

<!-- S35 -->
Sistemnya disewa
dari Lloyds Banking Group,
pesaingnya sendiri,
dan biaya sewanya akan naik tajam.

<!-- S36 -->
Jadi TSB memutuskan memindahkan semuanya
ke platform baru,
yang dibangun oleh pemilik barunya,
bank Spanyol Sabadell.

<!-- S37 -->
Satu akhir pekan di bulan April.
Pada Minggu malam,
sistem baru dinyalakan.

<!-- S38 -->
Pada hari Senin, ada sekitar
sembilan ratus ribu upaya login.
Hanya sekitar satu dari sepuluh login
internet banking yang berhasil.

<!-- S39 -->
Pembayaran gagal.
Sebagian nasabah berhasil login
dan melihat rekening orang lain.

<!-- S40 -->
Masa terburuknya berlangsung sekitar seminggu.
TSB baru kembali beroperasi normal
pada bulan Desember.

<!-- S41 -->
Dampaknya menelan biaya sekitar
330 juta pound
pada 2018 saja.
Regulator kemudian menambahkan
denda hampir 49 juta pound.

<!-- S42 -->
Dan inilah bagian anehnya.
Data nasabah tiba dengan utuh.
Kedua laporan resmi menyatakan begitu.

<!-- S43 -->
Yang gagal adalah platform baru di sekitarnya.
Dua pusat data, dengan pengaturan berbeda.
Uji performa hanya di salah satunya,
dan targetnya diturunkan
setelah ujinya tidak lolos.

<!-- S44 -->
Dan tidak ada jalan kembali.
Begitu datanya dipindahkan,
kembali ke sistem lama,
menurut kata-kata regulator,
"pada dasarnya mustahil".

<!-- S45 -->
TSB tidak sedang kabur dari sistem yang rusak.
Ia meninggalkan sistem yang berjalan,
karena siapa pemiliknya
dan berapa biayanya.
Justru kepergian itulah yang berbahaya.

<!-- S46 -->
Jadi, apakah pindah selalu berakhir bencana?

<!-- S47 -->
Pada 2008, Commonwealth Bank di Australia
mulai mengganti sistem inti
yang telah melayaninya
selama lebih dari 45 tahun.

<!-- S48 -->
Rencananya: sekitar
580 juta dolar Australia,
dan empat tahun.

<!-- S49 -->
Ternyata lima tahun.
Laporan media kemudian menyebut totalnya
sekitar 1,1 miliar,
karena proyeknya terus membesar.

<!-- S50 -->
Tapi bank itu tidak memindahkan semuanya
dalam satu akhir pekan.
Rekening simpanan lebih dulu, pada 2010.
Rekening bisnis menyusul pada 2011,
dan pinjaman pada 2012.

<!-- S51 -->
Setiap langkah adalah sesuatu yang bisa
diamati, diperiksa, dan dipelajari bank itu
sebelum mengambil risiko di tahap berikutnya.

<!-- S52 -->
Pada akhirnya, menurut bank itu,
ia menjadi bank besar Australia pertama
dengan layanan perbankan real-time,
24 jam sehari.

<!-- S53 -->
Jadi, itu bisa dilakukan.
Tapi lihat apa yang dibutuhkan.
Lima tahun, tagihan yang jauh lebih besar,
dan kesabaran.

<!-- S54 -->
Modernisasi bukan sekadar membeli.
Ini sebuah proyek,
dengan risikonya sendiri.

<!-- S55 -->
Sekarang, krisis
yang membuat semua orang menyalahkan COBOL.

<!-- S56 -->
Maret 2020.
Saat pandemi melumpuhkan New Jersey,
klaim pengangguran baru melonjak
dari di bawah 10 ribu dalam seminggu
menjadi lebih dari 155 ribu.

<!-- S57 -->
Enam belas kali lipat,
dalam tujuh hari.
Kantor tunjangan pengangguran kewalahan.

<!-- S58 -->
Awal April, sang gubernur
meminta relawan.
Bukan hanya tenaga kesehatan,
tapi juga orang yang paham COBOL.
Sistem negara bagian itu, katanya,
sudah berusia lebih dari 40 tahun.

<!-- S59 -->
Ceritanya cepat menyebar.
Kode kuno telah runtuh
dihantam pandemi.

<!-- S60 -->
Tapi ketika auditor negara bagian
menyelidikinya kemudian,
ia tidak menemukan bukti
bahwa keterlambatan itu disebabkan
oleh sistem komputernya.

<!-- S61 -->
Secara terpisah, wartawan yang memeriksa
pesan error yang dilihat orang-orang
menemukan banyak di antaranya berasal dari situs web,
yang ditulis dalam bahasa jauh lebih baru, Java.
Kode lama di belakangnya tetap berjalan.

<!-- S62 -->
Lalu kenapa negara bagian butuh programmer COBOL?
Karena Kongres sedang mengubah aturan.
Tunjangan baru, jumlah baru,
orang baru yang memenuhi syarat,
dan setiap perubahan harus masuk
ke dalam kode, dengan cepat.

<!-- S63 -->
Masalahnya bukan karena kodenya tua.
Tapi karena sedikit orang bisa mengubahnya,
dan karena saluran telepon serta stafnya
juga kewalahan.

<!-- S64 -->
Tiga kasus.
Bank yang meninggalkan sistem yang masih berjalan,
dan migrasinya gagal.
Bank yang pindah dengan hati-hati,
dan berhasil.
Dan krisis yang disalahkan pada kode lama,
tanpa ada yang bisa membuktikan itu penyebabnya.

<!-- S65 -->
Bukan berarti sistem lama tidak pernah gagal.
Itu memang terjadi.
Biayanya makin mahal,
orang-orang yang memahaminya pensiun,
dan menunggu juga ada harganya.

<!-- S66 -->
Tapi usia mudah terlihat,
sedangkan risiko yang sebenarnya tidak.
Aturan yang tak pernah dicatat.
Pengetahuan di kepala segelintir orang.
Dan saat peralihan.

<!-- S67 -->
Itulah sebabnya banyak bank tidak mengganti
inti lamanya sekaligus.
Mereka membungkusnya.
Aplikasi di ponselmu memang baru,
tapi mungkin ia sedang berkomunikasi dengan sesuatu
yang jauh lebih tua.

<!-- S68 -->
Dan mereka menggantinya sedikit demi sedikit.
Pada 2004, penulis software Martin Fowler
memberi metode ini nama yang diambil dari ara pencekik,
tanaman hutan hujan yang tumbuh melilit pohon
sampai bisa berdiri sendiri.

<!-- S69 -->
Sistem lama tetap bekerja
sementara yang baru tumbuh di sekelilingnya,
satu tugas demi satu tugas,
sampai tak ada lagi yang bergantung pada yang lama.

<!-- S70 -->
Itu membawa kita kembali ke setengah penny tadi.
Di suatu tempat, sebuah program mungkin masih membuangnya,
karena seseorang memutuskan begitu,
puluhan tahun lalu.
Mengganti program itu berarti mengetahui hal itu,
dan semua hal yang serupa.

<!-- S71 -->
Sistem lama belum tentu
yang gagal.
Kadang, yang gagal justru penggantinya.

<!-- S72 -->
Karena mengganti teknologinya
tidak sama dengan menghilangkan risikonya.
Kadang itu hanya memindahkan risikonya
ke satu akhir pekan di bulan April.

<!-- S73 -->
Jadi, ini pertanyaan untukmu.
Kalau sebuah sistem sudah berjalan empat puluh tahun,
kapan waktu yang tepat untuk menggantinya?
Dan pernahkah kamu sendiri harus mengganti sistem seperti itu?
Ceritakan di kolom komentar.
