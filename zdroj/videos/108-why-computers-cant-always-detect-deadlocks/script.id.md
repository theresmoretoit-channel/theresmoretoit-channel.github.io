<!-- S01 -->
Empat mobil tiba di sebuah persimpangan
tepat pada saat yang sama.
Tidak ada lampu lalu lintas. Tidak ada rambu.
Hanya aturan yang dipakai di banyak negara:
beri jalan kepada mobil di sebelah kananmu.

<!-- S02 -->
Setiap pengemudi menoleh ke kanan,
dan melihat mobil yang harus ia tunggu.
Jadi setiap pengemudi menunggu.

<!-- S03 -->
Tidak ada yang melanggar aturan.
Semua orang mematuhinya dengan sempurna.
Dan tidak akan ada yang pernah bergerak.

<!-- S04 -->
Ilmuwan komputer menyebut ini deadlock, atau kebuntuan.
Dan ini tidak hanya terjadi di jalan.
Ini terjadi di dalam basis data,
sistem operasi, dan perangkat lunak biasa.

<!-- S05 -->
Komputer sering kali pandai mengenali
deadlock setelah deadlock itu terjadi.
Tapi bisakah sebuah program membaca program lain
dan memberitahumu dengan pasti
apakah program itu suatu saat akan macet?

<!-- S06 -->
Untuk banyak program, bisa.
Tapi metode yang berhasil
untuk semua program yang mungkin
mustahil ada.
Dan bukan karena komputer
belum cukup cepat.
Komputer yang lebih cepat pun tidak akan pernah mengubahnya.

<!-- S07 -->
Begini caranya sebuah program macet.
Bayangkan sebuah toko online,
dengan dua tugas yang berjalan bersamaan.

<!-- S08 -->
Sebelum sebuah tugas mengubah apa pun,
ia memasang kunci padanya,
supaya tidak ada pihak lain yang bisa menyentuhnya.
Seperti mengambil satu-satunya kunci sebuah ruangan.

<!-- S09 -->
Tugas pertama mengunci akun seorang pelanggan,
lalu mencoba mengunci pesanannya.
Tugas kedua mengunci pesanan itu,
lalu mencoba mengunci akunnya.

<!-- S10 -->
Yang satu memegang akun
dan menunggu pesanan.
Yang lain memegang pesanan
dan menunggu akun.
Tidak ada yang mau melepaskan apa yang dipegangnya.

<!-- S11 -->
Dan anehnya,
kode ini bisa berjalan sejuta kali
tanpa masalah apa pun.
Hanya ketika kedua tugas itu bertumpang tindih
tepat dalam urutan yang salah,
barulah semuanya berhenti.

<!-- S12 -->
Bug-nya sudah ada sejak awal.
Kebetulan waktunya saja yang membuatnya terungkap.

<!-- S12b -->
Ngomong-ngomong, kalau kamu suka
video seperti ini, kamu bisa subscribe.

Itu sangat membantu channel ini.

<!-- S13 -->
Basis data mengalami ini terus-menerus,
jadi mereka selalu berjaga.
Mereka menggambar peta siapa menunggu siapa.

<!-- S14 -->
Yang pertama menunggu yang kedua.
Yang kedua menunggu yang pertama.
Saat panah-panahnya membentuk lingkaran tertutup,
itulah deadlock.
Tanpa tebak-tebakan. Lingkarannya ada di situ.

<!-- S15 -->
Lalu basis data melakukan sesuatu yang brutal.
Ia memilih salah satu tugas
dan membuang pekerjaannya.

<!-- S16 -->
SQL Server milik Microsoft bahkan memberi tahu yang kalah
bahwa ia telah dipilih
sebagai korban deadlock,
dan harus mencoba lagi.

<!-- S17 -->
Tugas yang lain terus berjalan,
dan si korban tinggal mencoba lagi.

<!-- S18 -->
Perhatikan apa yang diperbaiki dan apa yang tidak.
Kebuntuannya sudah terurai.
Tapi kode yang menyebabkannya masih ada,
menunggu saat sial berikutnya.

<!-- S19 -->
Jadi mengenali deadlock
yang sudah terjadi
adalah bagian yang mudah.
Pertanyaan yang sulit lain lagi.

<!-- S20 -->
Bukan: apakah program ini macet sekarang?
Tapi: berikan input ini kepadanya.
Mungkinkah ia suatu saat macet?

<!-- S21 -->
Yang pertama adalah foto masa kini.
Kamu cukup melihatnya.
Yang kedua adalah ramalan
tentang setiap masa depan yang mungkin.

<!-- S22 -->
Dan program membuat hal itu sangat sulit.
Program mengambil keputusan. Program mengulang-ulang.
Program bisa menjalankan perhitungan yang makan waktu
sedetik, atau seribu tahun.

<!-- S23 -->
Sebuah program bisa macet seketika,
setelah sejuta langkah,
karena satu input langka,
atau tidak pernah sama sekali.

<!-- S24 -->
Kamu bisa saja menjalankannya dan mengamati.
Tapi kalau setelah satu jam ia belum macet,
apa yang bisa kamu simpulkan?

<!-- S25 -->
Tidak ada.
Bisa saja ia macet di detik berikutnya,
atau tidak pernah.

<!-- S26 -->
Pada tahun 1936, seorang matematikawan muda
bernama Alan Turing menunjukkan
bahwa ada pertanyaan tentang program
yang tidak bisa dijawab oleh program apa pun.
Yang paling terkenal terdengar lebih sederhana lagi.

<!-- S27 -->
Ambil program apa saja, beserta inputnya.
Apakah ia akhirnya akan berhenti?
Atau berjalan selamanya?

<!-- S28 -->
Kini namanya masalah penghentian (halting problem).
Dan tidak ada program yang bisa menjawabnya
dengan benar di setiap kasus.

<!-- S29 -->
Gagasan di balik buktinya
ternyata sangat singkat.
Misalkan seseorang memberimu
pemeriksa penghentian yang sempurna.

<!-- S30 -->
Lalu kamu menulis program kecil yang suka membangkang.
Ia bertanya kepada pemeriksa tentang dirinya sendiri,
lalu melakukan kebalikannya.

<!-- S31 -->
Kalau pemeriksa bilang ia akan berhenti,
ia berputar selamanya.
Kalau pemeriksa bilang ia akan berjalan selamanya,
ia langsung berhenti.

<!-- S32 -->
Apa pun yang dikatakan pemeriksa tentangnya,
pemeriksa itu salah.
Jadi pemeriksa yang sempurna tidak mungkin ada.

<!-- S33 -->
Lalu apa hubungannya dengan deadlock?
Sangat erat.

<!-- S34 -->
Bayangkan seseorang mengaku telah membuat
prediktor deadlock yang sempurna.
Berikan program apa saja beserta inputnya,
dan ia selalu memberitahumu dengan benar
apakah program itu suatu saat akan macet.

<!-- S35 -->
Mari kita pakai
untuk memecahkan masalah penghentian.

<!-- S36 -->
Ambil program apa saja yang kamu mau,
lalu masukkan ke dalam program baru.

<!-- S37 -->
Pertama, program baru itu
cukup menjalankan program lama,
langkah demi langkah, di satu thread.
Tanpa kunci. Tanpa apa pun yang dipakai bersama.
Tidak ada yang bisa macet.

<!-- S38 -->
Lalu, kalau program lama itu selesai,
program baru menjalankan dua tugas.
Masing-masing mengambil satu kunci,
menunggu sampai yang lain mengambil kuncinya sendiri,
lalu meraih kunci milik yang lain.
Deadlock, dengan sengaja, setiap kali.

<!-- S39 -->
Kalau program lama tidak pernah selesai,
program baru tidak pernah sampai ke situ.
Tidak ada deadlock. Tidak akan pernah.

<!-- S40 -->
Jadi program baru itu macet
jika, dan hanya jika, program lama berhenti.

<!-- S41 -->
Sekarang tanyakan kepada prediktor
tentang program baru itu.
"Ya, ia akan deadlock"
berarti program lama berhenti.
"Tidak" berarti program lama berjalan selamanya.

<!-- S42 -->
Kita baru saja memecahkan masalah penghentian.
Dan justru itulah yang mustahil.

<!-- S43 -->
Jadi prediktor deadlock yang sempurna
juga tidak mungkin ada.

<!-- S44 -->
Masalahnya bukan kunci,
atau basis data, atau programmer yang buruk.
Sebuah program bisa menyembunyikan perhitungan apa pun
tepat sebelum deadlock.
Untuk memprediksi deadlock itu,
kamu harus memprediksi apakah perhitungannya selesai.

<!-- S45 -->
Tapi tunggu dulu.
Komputer sungguhan punya batas.
Memorinya punya jumlah keadaan yang terbatas.
Jadi kenapa tidak diperiksa saja semuanya?

<!-- S46 -->
Untuk mesin dengan jumlah memori
yang tetap, secara prinsip, bisa.
Dalam praktiknya, coba saja hitung.

<!-- S47 -->
Memori sebuah laptop
dengan delapan gigabyte
bisa disusun dengan begitu banyak cara
sehingga menuliskan angkanya saja
butuh sekitar dua puluh miliar digit.

<!-- S48 -->
Jumlah atom
di alam semesta teramati
hanya punya sekitar delapan puluh digit.

<!-- S49 -->
Jadi di mesin sungguhan, memeriksa semuanya
mungkin secara teori,
dan sia-sia dalam praktik.

<!-- S50 -->
Tapi itu tembok yang berbeda.
Batas Turing bukan soal terlalu banyak keadaan.
Batas itu berlaku untuk program
yang selalu bisa meminta memori tambahan.
Bagi program seperti itu, prediktor sempurna mustahil ada,
sebesar apa pun komputernya.

<!-- S51 -->
Apakah itu berarti deadlock tak bisa diatasi?
Tidak.
Artinya, tidak ada pemeriksa yang sempurna.
Jadi programmer menulis program
yang lebih mudah diperiksa.

<!-- S52 -->
Trik paling sederhana: menetapkan urutan.
Setiap tugas harus mengunci akun
sebelum pesanan.
Tidak pernah sebaliknya.

<!-- S53 -->
Kalau setiap tugas benar-benar mematuhi urutan itu,
lingkaran tidak bisa terbentuk,
dan deadlock jenis ini tidak bisa terjadi.

<!-- S54 -->
Sistem lain menyerah setelah batas waktu habis,
mengambil semua kuncinya sekaligus,
atau membiarkan basis data memilih korban
lalu tinggal mencoba lagi.

<!-- S55 -->
Dan untuk desain kecil yang dijabarkan dengan cermat,
ada alat yang bisa memeriksa setiap keadaan yang mungkin.
Para insinyur Amazon memakai salah satunya
untuk menemukan bug yang butuh tiga puluh lima langkah,
dalam urutan yang persis tepat, untuk muncul.

<!-- S56 -->
Alat-alat ini berhasil
karena masalahnya sudah diperkecil.
Alat itu memeriksa model dari sistemnya,
bukan setiap program yang mungkin dibuat.

<!-- S57 -->
Tapi untuk kode sungguhan,
pemeriksa yang menerima program apa pun
harus mengorbankan sesuatu.
Ia mungkin memberi peringatan tentang deadlock
yang tidak mungkin terjadi,
melewatkan sebagian yang mungkin terjadi,
atau kadang tidak memberi jawaban sama sekali.

<!-- S58 -->
Pemeriksa yang tidak pernah memberi alarm palsu,
tidak pernah melewatkan satu deadlock pun,
dan selalu memberi jawaban,
untuk setiap program,
justru itulah yang dinyatakan mustahil oleh Turing.

<!-- S59 -->
Kembali ke persimpangan tadi,
keempat pengemudi itu tidak diam di sana selamanya.

<!-- S60 -->
Seseorang melambaikan tangan.
Satu pengemudi merelakan gilirannya,
dan dalam hitungan detik kebuntuan itu selesai.

<!-- S61 -->
Itu juga yang dilakukan basis data.
Ia tidak memprediksi kebuntuan itu.
Ia menyadarinya,
lalu menyuruh seseorang memberi jalan.

<!-- S62 -->
Ada masalah yang butuh komputer lebih cepat.
Ada yang butuh ide yang lebih baik.

<!-- S63 -->
Dan ada yang, seperti yang satu ini,
sama sekali tidak punya solusi sempurna.
Hanya aturan yang baik,
dan seseorang yang siap melambaikan tangan.
