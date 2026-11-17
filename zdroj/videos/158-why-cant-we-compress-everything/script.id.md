<!-- S01 -->
Inilah semua naskah
yang pernah ditulis untuk kanal ini.
158 video,
hampir satu setengah juta byte teks.

<!-- S02 -->
Masukkan semuanya ke program kompresi biasa
bernama gzip.
Hasilnya sedikit di atas setengah megabyte.
Hampir dua pertiga lenyap.

<!-- S03 -->
Dan tak ada satu pun yang hilang.
Ekstrak file-nya,
dan setiap naskah kembali,
huruf demi huruf.

<!-- S04 -->
Sekarang kompres lagi.

<!-- S05 -->
Ukurannya malah membesar.
98 byte lebih besar.

<!-- S06 -->
Kali ketiga.
98 byte lebih besar.
Kali keempat.
98 lagi.

<!-- S07 -->
Putaran pertama membuang dua pertiga.
Putaran kedua tidak menemukan apa-apa.
Jadi kenapa kita tidak bisa terus mengompres?

<!-- S08 -->
Mari kita lihat isi file kedua itu.
gzip tidak mengompres apa pun.
Ia hanya menyalin datanya, tanpa diubah,
dalam enam belas blok.

<!-- S09 -->
Setiap blok diberi label lima byte.
Tambahkan header kecil dan footer,
dan hasilnya tepat 98.

<!-- S10 -->
Jika program kompresi tak menemukan yang bisa dibuang,
ia menyimpan data apa adanya,
dan hanya menambahkan yang perlu untuk memulihkannya.

<!-- S11 -->
Jadi kenapa putaran kedua tidak menemukan apa-apa?
Dan apakah program yang lebih cerdas bisa?

<!-- S12 -->
Teks seperti ini penuh pengulangan.
Kata yang sama, frasa yang sama,
penanda adegan kecil yang sama
di awal setiap adegan.

<!-- S13 -->
Pada 1977, Jacob Ziv dan Abraham Lempel
menerbitkan sebuah trik sederhana.
Jangan tulis ulang bagian yang berulang.
Tunjuk balik ke tempat ia sudah muncul.

<!-- S14 -->
Mundur 300 karakter,
lalu salin dua belas karakter berikutnya.
Beberapa byte, bukan dua belas.

<!-- S15 -->
Trik kedua:
beri huruf yang sering muncul kode pendek,
dan huruf yang jarang kode panjang.

<!-- S16 -->
Pada 1951, David Huffman,
mahasiswa pascasarjana di MIT,
bisa memilih: ikut ujian akhir,
atau menulis makalah sebagai gantinya.

<!-- S17 -->
Dalam makalah yang ditugaskan Robert Fano,
ia harus menemukan kode paling efisien
dari jenis seperti ini.

<!-- S18 -->
Selama berbulan-bulan, Huffman buntu.
Ia menyerah,
dan mulai belajar untuk ujian.
Lalu jawabannya tiba-tiba muncul.

<!-- S19 -->
Ambil dua simbol yang paling jarang,
gabungkan menjadi satu,
dan ulangi sampai tersisa satu pohon.

<!-- S20 -->
Belakangan ia menyebutnya
“momen paling luar biasa dalam hidup saya.”

<!-- S21 -->
Fano tidak memberi tahu kelasnya
bahwa ia sendiri pernah bergulat dengan soal itu,
begitu pula Claude Shannon.

<!-- S22 -->
Kode Huffman mengalahkan metode mereka berdua.
Dan bisa dibuktikan
bahwa tak ada kode sejenis yang lebih baik.

<!-- S23 -->
Di awal 1990-an,
Phil Katz menggabungkan kedua trik itu
untuk file ZIP.
gzip memakai metode yang sama.

<!-- S24 -->
Putaran pertama sudah menghabiskan
pola yang bisa ditemukan gzip.

<!-- S25 -->
Sisanya tidak memberinya bahan untuk diolah.
Bagi gzip, itu tampak seperti derau.

<!-- S26 -->
Tapi program yang lebih cerdas
mungkin melihat pola yang terlewat oleh gzip.
Mungkinkah suatu hari ada program
yang bisa memperkecil apa pun yang Anda berikan?

<!-- S27 -->
Tidak.
Dan Anda tidak perlu tahu cara kerjanya
untuk yakin akan hal itu.

<!-- S28 -->
Ambil semua file
yang panjangnya tepat tiga bit.
Jumlahnya delapan.

<!-- S29 -->
Sekarang hitung semua yang lebih pendek.
Empat file dua bit,
dua file satu bit,
dan satu file kosong.

<!-- S30 -->
Tujuh.

<!-- S30b -->
Delapan file, dan tujuh tempat yang lebih pendek
untuk menaruhnya.

<!-- S31 -->
Kalau semuanya jadi lebih pendek,
dua di antaranya harus berbagi tempat.
Dan saat Anda mengekstraknya,
yang mana yang Anda maksud?

<!-- S32 -->
Ini disebut prinsip sarang merpati,
dan berlaku untuk panjang berapa pun.
File yang lebih pendek selalu kurang satu
dari yang dibutuhkan.

<!-- S33 -->
Jadi program kompresi apa pun yang menerima semua file
dan memperkecil sebagian,
pasti memperbesar yang lain.
Bukan karena programnya ditulis dengan buruk.
Memang tidak ada tempat lain untuk mereka.

<!-- S34 -->
98 byte itu
adalah cara gzip membayar harganya.

<!-- S35 -->
Pilih program kompresi apa saja.
Dari semua file dengan ukuran tertentu,
ia bisa memperkecil kurang dari satu
dari 250 file, walau hanya satu byte.

<!-- S36 -->
Kompresi tetap berhasil,
karena file yang kita buat tidak acak.
Isinya teks, gambar, dan program,
penuh pola.

<!-- S37 -->
Itu tidak menghentikan orang
untuk menjanjikan lebih.

<!-- S38 -->
Pada 1992, WEB Technologies
mengumumkan perangkat lunak yang katanya bisa memampatkan
hampir semua data hingga di bawah satu kilobyte.
Bahkan keluarannya sendiri,
lagi dan lagi.

<!-- S39 -->
Wakil presidennya bilang metode itu
“tidak tunduk pada hukum
teori informasi.”
Produknya tak pernah dirilis.

<!-- S40 -->
Lalu bagaimana foto dan musik
bisa jadi jauh lebih kecil?
Keduanya sama sekali tidak ikut aturan ini.

<!-- S41 -->
JPEG tidak kembali persis sama.
Ia kembali cukup mirip.
Detail yang hilangnya tak akan Anda sadari
dibuang untuk selamanya.

<!-- S42 -->
Perbesar,
dan Anda bisa melihat ke mana perginya.

<!-- S43 -->
Itu kompresi lossy,
dan itu permainan yang berbeda.
Video ini membahas jenis yang satunya.
Setiap bit kembali, persis.

<!-- S44 -->
Jadi untuk file yang memang punya pola,
seberapa kecil bisa jadinya?
Adakah batas bawahnya?

<!-- S45 -->
Ada.
Batas itu ditemukan pada 1948,
dalam makalah yang sama yang mendasari video kami
tentang kode koreksi galat.

<!-- S46 -->
Di sana, Claude Shannon menunjukkan
bagaimana menambah redundansi melindungi pesan.
Di sini, ia menghitung
seberapa banyak redundansi yang bisa dibuang.

<!-- S47 -->
Jawabannya berupa angka
yang ia sebut entropi:
seberapa sulit menebak
apa yang muncul berikutnya.

<!-- S48 -->
Tak ada kode lossless yang bisa turun di bawah angka itu
secara rata-rata.
Tapi Anda bisa mendekatinya
sedekat yang Anda mau.

<!-- S49 -->
Jadi seberapa sulit bahasa Inggris ditebak?
Pada 1951, Shannon mengukurnya
dengan sebuah permainan.

<!-- S50 -->
Ia memberi seseorang sepotong teks
yang belum pernah dilihatnya,
lalu memintanya menebak,
huruf demi huruf.

<!-- S51 -->
Kalau tebakannya salah,
ia menebak lagi,
sampai benar.

<!-- S52 -->
Ternyata manusia sangat pandai melakukannya.
Dengan konteks seratus huruf,
hasilnya sekitar satu bit
per huruf untuk bahasa Inggris.

<!-- S53 -->
Komputer menyimpan setiap huruf
dalam delapan bit.
Pembaca manusia butuh sekitar satu.

<!-- S54 -->
Celah itulah ruang kerja kompresi.
gzip menekan naskah-naskah kanal ini
hingga di bawah tiga bit per karakter.

<!-- S55 -->
Jadi seberapa dekat mesin bisa
mendekati satu bit?

<!-- S56 -->
Ada hadiah khusus untuk itu.
Namanya Hutter Prize,
dan sejak 2020, tugasnya satu file:
satu gigabyte Wikipedia bahasa Inggris.

<!-- S57 -->
gzip memperkecilnya jadi sepertiga.
Program kompresi sehari-hari terbaik,
jadi sekitar seperlima.

<!-- S58 -->
Rekornya, yang dibuat Juli 2026,
sedikit di atas seratus juta byte.
Sepersepuluh.

<!-- S59 -->
Dan dekompresornya juga dihitung.
Ukurannya masuk ke total,
jadi Anda tidak bisa menyembunyikan Wikipedia
di dalam program.

<!-- S60 -->
Dananya 500.000 euro.
Setiap satu persen perbaikan
dihargai lima ribu.

<!-- S61 -->
Marcus Hutter, yang mendanainya, menjelaskan alasannya:
“mampu mengompres dengan baik
berkaitan erat
dengan bertindak secara cerdas.”

<!-- S62 -->
Sebab program-program teratas
tidak mencari pengulangan.
Mereka memprediksi.

<!-- S63 -->
Sebelum setiap karakter,
mereka memperkirakan seberapa mungkin
setiap karakter berikutnya muncul.
Tebakan yang bagus hanya butuh sebagian kecil dari satu bit.

<!-- S64 -->
Ini permainan tebak-tebakan Shannon,
yang dimainkan oleh mesin.
Pemain terbaik kini memakai jaringan saraf,
yang dilatih menebak apa yang muncul berikutnya.

<!-- S65 -->
Ini bahkan berhasil pada file yang sudah dikompresi.
Pada 2016, Dropbox mulai mengemas ulang
JPEG penggunanya dengan prediktor yang lebih baik.
Rata-rata, ukurannya berkurang lebih dari seperlima.

<!-- S66 -->
Setiap file kembali bit demi bit,
dan hingga 2017,
cara itu menghemat lebih dari 46 petabyte.
Itu lebih dari 46.000 terabyte.

<!-- S67 -->
Lalu ada para raksasa.
Pada 2023, peneliti di DeepMind
memakai model bahasa besar
sebagai program kompresi.

<!-- S68 -->
Pada potongan kecil foto skala abu-abu,
ia mengalahkan PNG:
48% dari ukuran asli
dibanding 58.

<!-- S69 -->
Pada rekaman ucapan yang dibacakan,
ia mengalahkan FLAC:
21% dibanding 30.

<!-- S70 -->
Tapi itu tanpa menghitung modelnya.
Tambahkan ukurannya,
dan hasilnya jadi
140 kali
lebih besar dari datanya.

<!-- S71 -->
Program kompresi yang lebih besar dari datanya
tidak menghemat apa pun.
Programnya adalah bagian dari deskripsi.

<!-- S72 -->
Dan itu membawa kita ke bagian paling aneh.
Inilah satu juta digit pertama π.

<!-- S73 -->
Berikan ke empat program kompresi.
Yang terbaik menekannya hingga sekitar
426.000 byte.

<!-- S74 -->
Sekarang beri program kompresi yang sama
satu juta digit acak.
Hasilnya sama,
selisihnya kurang dari sepersepuluh persen.

<!-- S75 -->
Tapi π tidak dibuat secara acak.
Ia mengikuti aturan matematika.
Inilah program yang mencetak
setiap digit dari satu juta digit itu.

<!-- S76 -->
362 byte.
Lebih dari dua ribu kali lebih pendek dari file-nya.

<!-- S77 -->
Program kompresi tidak bisa melihat
aturan matematika di balik π.
Mereka hanya melihat digitnya.

<!-- S78 -->
Salah satu cara mengukur informasi
dalam data adalah bertanya:
seberapa pendek sebuah program bisa dibuat
dan masih mencetaknya?

<!-- S79 -->
Panjang itu disebut
kompleksitas Kolmogorov,
dari nama salah satu orang yang merumuskannya.

<!-- S80 -->
Kebanyakan data tidak punya program pendek.
Lagi-lagi prinsip sarang merpati:
program pendek tidak cukup banyak
untuk semuanya.

<!-- S81 -->
Satu juta digit acak
sangat mungkin tidak punya yang lebih pendek.
π punya.

<!-- S82 -->
Lalu kenapa tidak cari saja
program terpendek untuk file apa pun?
Karena sudah dibuktikan
bahwa tak ada algoritme yang bisa melakukannya
untuk setiap file.

<!-- S83 -->
Setiap program memberi Anda batas atas.
Tapi tak ada yang selalu bisa memberi tahu
apakah ada yang lebih pendek.
Anda tak pernah tahu sudah mencapai dasar.

<!-- S84 -->
gzip menemukan pengulangan dalam naskah,
dan tidak lebih.
Ia melihat byte,
bukan makna kata-katanya.

<!-- S85 -->
Untuk melangkah lebih jauh, program
harus memprediksinya dengan lebih baik.
Dan memprediksi teks dengan baik
mulai tampak sangat mirip dengan memahaminya.

<!-- S86 -->
Jadi, ini pertanyaan untuk Anda.
Kalau sebuah program bisa memampatkan Wikipedia
lebih kecil daripada program lain mana pun,
apakah menurut Anda program itu memahaminya?
Tulis jawaban Anda di kolom komentar.
