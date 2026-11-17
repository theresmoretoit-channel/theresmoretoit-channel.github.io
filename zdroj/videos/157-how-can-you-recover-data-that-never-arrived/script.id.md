<!-- S01 -->
Ini kode QR.
Isinya satu baris teks pendek.

<!-- S02 -->
Ponsel langsung bisa membacanya.

<!-- S03 -->
Sekarang mari kita sobek sebagian.

<!-- S04 -->
Lalu kita pindai lagi.
Teks yang sama.
Lengkap sampai huruf terakhir.

<!-- S05 -->
Sebagian kode itu hilang.
Bukan sulit dibaca.
Hilang.

<!-- S06 -->
Jadi bagaimana ponsel bisa membaca sesuatu
yang sudah tidak ada?

<!-- S07 -->
Ini masalah yang sama, dalam versi kecil.
Seseorang mengirimi Anda delapan bit.
Di tengah jalan, tiga di antaranya hilang.

<!-- S08 -->
Setiap bit yang hilang bernilai nol atau satu,
jadi ada delapan cara untuk mengisi celahnya.
Dan dari bit-bit yang diterima,
Anda tidak bisa tahu mana yang benar.

<!-- S09 -->
Namun ponsel tadi melakukan persis itu.
Ia tidak menebak.
Jawabannya sudah dikirim
sebelum ada yang hilang.

<!-- S10 -->
Triknya adalah mengirim lebih banyak
daripada pesannya sendiri.

<!-- S11 -->
Cara paling sederhana
adalah mengatakan semuanya tiga kali.
Nol dikirim sebagai tiga nol,
satu sebagai tiga satu.

<!-- S12 -->
Derau membalik salah satunya,
dan Anda menerima satu, nol, satu.
Dua suara lawan satu.
Hampir pasti itu tadinya satu.

<!-- S13 -->
Jika derau membalik satu dari sepuluh bit,
secara acak dan independen,
pemungutan suara tiga bit akan keliru
kurang dari tiga kali dalam seratus.

<!-- S14 -->
Tapi Anda jadi melipattigakan
semua yang Anda kirim.
Untuk makin mendekati sempurna,
Anda harus mengulang lima kali, lalu sembilan,
lalu seratus...
dan pesannya merayap pelan sekali.

<!-- S15 -->
Untuk waktu yang lama,
sepertinya memang itulah harganya.
Lebih sedikit kesalahan, pesan lebih lambat.
Ingat itu.

<!-- S16 -->
Pada akhir 1940-an,
Richard Hamming di Bell Labs
punya masalahnya sendiri.

<!-- S17 -->
Ia biasanya mendapat jatah waktu di komputer relai
pada akhir pekan,
saat tidak ada orang yang mengawasinya.

<!-- S18 -->
Mesin itu bisa tahu
kalau ia membuat kesalahan.
Ia akan mencoba langkah itu lagi,
tiga kali...
lalu membuang tugas Hamming begitu saja.
Dua akhir pekan berturut-turut,
hasil kerjanya lenyap.

<!-- S20 -->
Pertanyaannya, dengan kata-katanya sendiri:
"Kalau mesin bisa mengetahui
bahwa ada kesalahan,
kenapa ia tidak bisa mengetahui di mana letaknya?"
Kata-kata aslinya, ia mengakui,
mungkin sedikit lebih kasar.

<!-- S22 -->
Caranya: ambil empat bit pesan
lalu tambahkan tiga bit pemeriksa.
Total tujuh bit.

<!-- S23 -->
Setiap bit pemeriksa menjaga
kelompok posisi yang berbeda,
dan memastikan kelompok itu
memuat angka satu dalam jumlah genap.

<!-- S24 -->
Kelompoknya saling tumpang tindih dengan pola cermat.
Setiap posisi masuk
ke kombinasi kelompoknya sendiri.

<!-- S25 -->
Sekarang balik satu bit.
Misalnya, bit di posisi enam.

<!-- S26 -->
Penerima menjalankan tiga pemeriksaan itu lagi.
Yang pertama lolos.
Yang kedua gagal.
Yang ketiga gagal.

<!-- S27 -->
Tulis pemeriksaan yang gagal sebagai satu,
yang lolos sebagai nol,
lalu baca dari yang terakhir ke yang pertama.
Satu, satu, nol.
Dalam biner, itu enam.

<!-- S28 -->
Pemeriksaan itu tidak hanya mengatakan
bahwa ada yang salah.
Mereka menunjuk tepat ke bit itu.

<!-- S29 -->
Balik lagi bit itu,
dan pesannya utuh kembali.
Tidak ada yang perlu mengirim apa pun dua kali.

<!-- S30 -->
Jadi itulah jawabannya.
Penerima tidak membangun ulang
informasi yang hilang dari ketiadaan.
Pengirimlah yang sudah mengemasnya,
sejak awal.

<!-- S32 -->
Tidak semua pemeriksaan bisa begitu.
Checksum, seperti yang ada di video kami
tentang Btrfs,
bisa memberi tahu bahwa sebuah blok rusak,
tapi tidak bisa memberi tahu data aslinya.

<!-- S33 -->
Dan ada jenis kerusakan kedua.
Kadang sebuah bit tidak salah.
Ia hanya hilang,
dan Anda tahu persis di mana celahnya.

<!-- S34 -->
Itu disebut penghapusan,
dan penghapusan lebih mudah ditangani.

<!-- S35 -->
Kirim empat angka,
4, 7, 2, dan 9,
lalu angka kelima:
jumlahnya, 22.

<!-- S36 -->
Kalau salah satunya hilang,
sisanya memberi tahu Anda berapa nilainya.
4, 7, sesuatu, 9,
22.
Pasti dua.

<!-- S37 -->
Server melindungi disknya
dengan pemeriksaan sejenis,
yang tersebar di semua disk.
Saat satu disk mati,
isinya dihitung dari sisanya.

<!-- S38 -->
Jadi berapa banyak tambahan yang dibutuhkan?
Jawaban pengulangan:
untuk menekan kesalahan sampai nol,
kecepatan pengiriman harus turun sampai nol.

<!-- S39 -->
Dua tahun sebelum makalah Hamming
terbit,
rekannya, Claude Shannon,
sudah menerbitkan jawaban yang lebih aneh.

<!-- S40 -->
Setiap kanal,
tautan radio, kabel, cakram,
punya batas.
Kecepatan tertinggi untuk informasi.

<!-- S41 -->
Di bawah batas itu,
kesalahan bisa dibuat sejarang yang Anda mau,
tanpa melambat.
Bukan dengan mengulang lebih banyak.
Tapi dengan pengodean yang lebih cerdas.

<!-- S42 -->
Di atasnya,
tidak ada kode di dunia yang bisa membantu.

<!-- S43 -->
Tapi ada satu kendala.
Shannon membuktikan bahwa kode seperti itu ada.
Ia tidak menunjukkan cara membuat kode
yang bisa dipakai siapa pun.

<!-- S44 -->
Menurut buktinya, kode yang dipilih secara acak
hampir pasti bagus.
Tapi cara paling jelas untuk mendekodenya
berarti membandingkan apa yang tiba
dengan setiap pesan yang mungkin...
dan untuk blok berukuran 1.000 bit,
jumlah pesan itu lebih banyak
daripada atom di alam semesta.

<!-- S46 -->
Jadi makalah Shannon bukanlah solusi.
Itu sebuah janji.
Dan para insinyur menghabiskan
45 tahun berikutnya untuk menepatinya.

<!-- S47 -->
Kode Hamming adalah langkah pertama.
Kode ini memperbaiki satu bit salah dari tujuh.

<!-- S48 -->
Tapi kerusakan nyata datang beruntun.
Goresan atau derak gangguan statis
merusak ratusan bit berturut-turut.

<!-- S49 -->
Pada 1960, Irving Reed dan Gustave Solomon,
di MIT Lincoln Laboratory,
menerbitkan makalah sepanjang lima halaman.

<!-- S50 -->
Kode mereka bekerja pada byte utuh,
bukan bit satu per satu.
Jika rentetan kesalahan merusak kedelapan bit
dalam satu byte,
itu tetap hanya satu byte rusak.

<!-- S51 -->
Satu versi yang umum menambahkan
32 byte pemeriksa
ke 223
byte data.

<!-- S52 -->
Ia bisa memperbaiki 16 byte mana pun
yang tiba dalam keadaan salah...
atau membangun ulang 32 byte
yang sama sekali tidak tiba.

<!-- S53 -->
Itulah sebabnya CD tetap bisa diputar meski tergores.
Dua kode Reed-Solomon di dalamnya
bisa sepenuhnya memperbaiki celah
sekitar 4.000 bit,
atau 2,5 milimeter trek.

<!-- S54 -->
Dan itulah sebabnya kode QR yang sobek
tetap berfungsi.
Pada pengaturan terkuatnya,
kode QR bisa membangun ulang
hingga sekitar 30% byte-nya
dan tetap mengembalikan setiap huruf.

<!-- S56 -->
Voyager 2 meninggalkan Bumi pada 1977
sudah membawa pengode Reed-Solomon.

<!-- S57 -->
Tapi di Jupiter dan Saturnus,
ia melindungi semuanya kecuali gambar
dengan kode yang lebih tua, buatan Marcel Golay,
yang mengirim satu bit tambahan
untuk setiap bit data.

<!-- S58 -->
Untuk Uranus dan Neptunus,
karena sinyalnya makin lemah,
para insinyur menyalakan Reed-Solomon,
di atas kode kedua
yang memang sudah dilalui setiap bit.

<!-- S59 -->
Dengan kode kedua itu saja,
sekitar lima dari seribu bit
masih salah.
Dengan Reed-Solomon di atasnya,
sekitar satu dari sejuta.

<!-- S60 -->
Derau juga datang beruntun,
jadi Voyager mengacak
byte dari empat blok menjadi satu
sebelum mengirimkannya.

<!-- S61 -->
Rentetan yang tadinya merusak satu blok
kini hanya merusak beberapa byte dari tiap blok...
cukup sedikit sehingga setiap blok
bisa memperbaiki dirinya sendiri.

<!-- S62 -->
Sisa cerita tentang bagaimana gambar Neptunus
sampai ke Bumi
ada di video kami tentang Voyager.

<!-- S63 -->
Tapi ini pun
masih belum mencapai batas Shannon...
dan kode yang bisa jauh lebih mendekatinya
sudah ada.

<!-- S65 -->
Pada 1960, dalam disertasi doktoralnya di MIT,
Robert Gallager menjelaskan kode
yang tersusun dari banyak pemeriksaan sederhana,
yang masing-masing hanya melihat beberapa bit.

<!-- S66 -->
Mendekodenya berarti pemeriksaan-pemeriksaan itu
saling melempar tebakan bolak-balik,
putaran demi putaran...
terlalu berat
untuk komputer tahun 1960-an.
Jadi ide itu disimpan,
dan nyaris terlupakan selama 30 tahun.

<!-- S68 -->
Pada 1993,
sebuah tim yang dipimpin dua insinyur Prancis,
Claude Berrou dan Alain Glavieux,
memperkenalkan kode turbo
di sebuah konferensi di Jenewa.

<!-- S69 -->
Hasil mereka begitu dekat
dengan batas Shannon
sehingga banyak pakar mengira
mereka telah membuat kesalahan.
Mungkin meleset dua kali lipat,
di suatu tempat dalam perhitungan mereka.

<!-- S70 -->
Dalam setahun,
laboratorium lain sudah mengonfirmasinya.

<!-- S71 -->
Kode turbo juga bekerja
dengan melempar tebakan bolak-balik,
dan itu membuat orang kembali melirik Gallager.

<!-- S72 -->
Pada 1995 dan 1996,
David MacKay dan Radford Neal
menemukan kembali kodenya,
dan menunjukkan bahwa kode itu bisa
sama dekatnya dengan batas Shannon.

<!-- S73 -->
Pada 2001,
versi kode Gallager yang disempurnakan
berhasil mencapai jarak 0,04 desibel
dari batas Shannon.

<!-- S74 -->
Itu kurang dari 1%
daya sinyal tambahan
dibanding minimum teoretis.
Janji tahun 1948 telah ditepati.

<!-- S75 -->
Kini kode Gallager membawa
banyak data di ponsel 5G,
di Wi-Fi modern,
dan di televisi satelit.

<!-- S77 -->
Sekarang, kembali ke delapan bit kita.
Tiga bit hilang,
dan ada delapan cara
untuk mengisi celahnya.

<!-- S78 -->
Tapi delapan bit ini
tidak pernah sekadar pesan.
Isinya empat bit data,
tiga pemeriksaan Hamming,
dan satu pemeriksaan lagi atas kedelapan bit.

<!-- S79 -->
Dari semua 256
kemungkinan pola delapan bit,
hanya 16 yang mematuhi aturan itu.

<!-- S80 -->
Uji kedelapan kandidat.
Satu per satu, mereka gagal.
Hanya satu yang tersisa.

<!-- S81 -->
Bit yang hilang itu tidak pernah benar-benar lenyap.
Informasinya masih ada,
di dalam bit-bit yang selamat.

<!-- S82 -->
Jadi, ini pertanyaan untuk Anda.
Pernahkah Anda memperhatikan koreksi kesalahan
bekerja dalam sesuatu yang Anda pakai setiap hari?
Tulis di kolom komentar.
