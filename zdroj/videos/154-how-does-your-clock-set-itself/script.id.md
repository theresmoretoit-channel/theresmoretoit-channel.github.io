<!-- S01 -->
Di suatu tempat di rumahmu,
mungkin ada jam
yang belum pernah diatur siapa pun.

<!-- S02 -->
Jam itu tetap jalan saat listrik padam.
Jam itu pindah ke waktu musim panas
sendiri, di tengah malam.

<!-- S03 -->
Jam itu tidak punya koneksi internet.
Tanpa Wi-Fi, tanpa GPS,
tanpa aplikasi di ponselmu.

<!-- S04 -->
Yang ia punya hanyalah penerima radio mungil.
Dan setiap satu detik sekali,
ia mendengar satu denyut.

<!-- S05 -->
Jadi bagaimana sebuah jam
mengubah satu denyut per detik
menjadi waktu yang tepat, tanggal,
bahkan nama hari?

<!-- S06 -->
Di Eropa, denyut itu berasal
dari DCF77, dekat Frankfurt.
Di Amerika, dari WWVB, di Colorado.
Pemancarnya berbeda, idenya sama.

<!-- S07 -->
Ambil yang dari Jerman.
Pemancar itu mengirim gelombang radio yang stabil,
siang dan malam.
Dan di awal setiap detik,
gelombang itu dilemahkan sebentar.

<!-- S08 -->
Triknya ada pada berapa lama
gelombang itu tetap lemah.

<!-- S09 -->
Penurunan selama sepersepuluh detik
berarti nol.
Penurunan selama dua persepuluh detik berarti satu.

<!-- S10 -->
Itulah seluruh idenya.
Tanpa paket data, tanpa jaringan.
Hanya gelombang radio yang turun
sebentar, atau sedikit lebih lama.

<!-- S11 -->
Satu bit setiap detik.
Artinya, butuh satu menit penuh
hanya untuk mengirim 60 bit.

<!-- S12 -->
Dan sebenarnya, yang dikirim hanya 59.

<!-- S13 -->
Di detik terakhir setiap menit,
gelombang itu sama sekali tidak turun.
Dan penurunan yang hilang itu
adalah bagian terpenting
dari seluruh sinyal.

<!-- S14 -->
Sebab saat penurunan berikutnya datang,
jam tahu
bahwa menit baru baru saja dimulai.

<!-- S15 -->
Celah itu berfungsi seperti titik.
Semua yang ada di antara dua celah
adalah satu kalimat utuh.

<!-- S16 -->
Lalu apa saja yang muat dalam kalimat
sepanjang 59 bit?

<!-- S17 -->
Menit. Jam.
Tanggal, hari dalam seminggu,
bulan, dan tahun.

<!-- S18 -->
Sebagian besar angka dikirim per digit.
47 menit
tidak dikirim sebagai 47.
Angka itu dikirim sebagai dua digit terpisah,
angka 4 dan angka 7.

<!-- S19 -->
4 bit cukup untuk digit apa pun
dari 0 sampai 9.
Puluhan menit tidak pernah lebih dari 5,
jadi cukup diberi 3 bit.

<!-- S20 -->
Dan tahun hanya mendapat dua digit.
Bagi pemancar,
2026 cukup ditulis 26.
Abadnya ditambahkan sendiri oleh jam.

<!-- S21 -->
Tapi radio bukan saluran yang bersih.
Motor, pengisi daya ponsel,
lampu LED murah...
semuanya bisa mengacaukan sebuah penurunan.

<!-- S22 -->
Jadi setelah setiap blok angka
datang satu bit tambahan, yang disebut bit paritas.

<!-- S23 -->
Nilainya dipilih supaya jumlah angka satu
dalam blok itu selalu genap.

<!-- S24 -->
Kalau gangguan membalik satu bit saja,
jumlahnya jadi ganjil,
dan jam tahu
ada yang salah.

<!-- S25 -->
Tapi kalau dua bit terbalik,
jumlahnya kembali genap,
dan kesalahannya lolos.

<!-- S26 -->
Itulah sebabnya banyak jam
tidak percaya pada satu menit saja.
Mereka menunggu satu menit lain yang valid.

<!-- S27 -->
Dan itulah sebabnya jam butuh
beberapa menit untuk mengatur dirinya sendiri,
dan saat kondisi buruk, jauh lebih lama.

<!-- S28 -->
Ini memunculkan masalah yang aneh.

<!-- S29 -->
Jam menghabiskan satu menit penuh
untuk mengumpulkan waktu 10.48.
Tapi selama ia mengumpulkan pesan itu,
waktunya masih 10.47.

<!-- S30 -->
Jadi kapan waktunya benar-benar berganti?

<!-- S31 -->
Sebab pesan itu adalah pengumuman.
Isinya: pukul berapa nanti
saat menit berikutnya dimulai.

<!-- S32 -->
Jam membaca seluruh kalimat,
menunggu penurunan yang hilang lewat,
dan saat penurunan berikutnya datang,
penurunan itulah momen yang tepat.

<!-- S33 -->
Bit memberi tahu jam pukul berapa sekarang.
Penurunan memberi tahu kapan.

<!-- S34 -->
Tapi kalimat itu punya beberapa kata lagi
selain waktu.

<!-- S35 -->
Dua bit menyatakan apakah Jerman
sedang memakai waktu musim dingin atau musim panas.

<!-- S36 -->
Dan bit ketiga adalah peringatan.
Selama satu jam penuh sebelum jam diganti,
nilainya dibuat satu.

<!-- S37 -->
Jadi jammu tidak perlu tahu
hari Minggu yang mana di bulan Maret
jam dimajukan,
atau hari Minggu yang mana di bulan Oktober jam dimundurkan.
Tak ada yang pernah mengajarinya aturan itu.
Ia hanya diberi tahu, satu jam sebelumnya.

<!-- S38 -->
Kalau suatu hari Eropa berhenti mengganti jam,
peringatan itu tidak akan pernah datang lagi.

<!-- S39 -->
Bit lain dulu dipakai untuk memperingatkan detik kabisat,
satu detik tambahan yang sesekali disisipkan,
karena rotasi Bumi
tidak menjaga waktu dengan sempurna.
Menit itu bisa berisi 61 detik.

<!-- S40 -->
Yang terakhir ditambahkan
pada akhir 2016.
Tapi pada Oktober 2026,
otoritas metrologi dunia
memutuskan untuk menghapus detik kabisat.
Mulai 20 Mei 2027,
UTC akan berjalan tanpa jeda.

<!-- S41 -->
Dan 14 bit pertama
setiap menit
sama sekali tidak berhubungan dengan waktu.

<!-- S42 -->
Sejak 2006, bit-bit itu juga dipakai
untuk membawa prakiraan cuaca terenkripsi
bagi stasiun cuaca yang kompatibel.

<!-- S43 -->
Jadi sinyal yang mengatur jam wekermu
juga bisa memberi tahu
stasiun cuaca milik orang lain
apakah hari Kamis akan hujan.

<!-- S44 -->
Meski begitu, kebanyakan jam ini
tidak mendengarkan sepanjang waktu.
Mendengarkan menguras baterai,
jadi banyak yang mencoba sekali setiap malam,
menjelang dini hari.

<!-- S45 -->
Gelombang panjang mencapai jam lewat dua jalur:
menyusuri permukaan tanah,
dan dipantulkan atmosfer atas.
Setelah gelap, jalur atas itu berubah,
dan sinyalnya sering menjangkau lebih jauh.

<!-- S46 -->
Dan pada pukul tiga dini hari,
biasanya lebih sedikit mesin, pengisi daya, dan lampu
yang menyala di sekitar untuk menenggelamkannya.

<!-- S47 -->
Di antara pengecekan itu,
jam berjalan dengan kristal kuarsa,
yang bisa meleset sekitar satu detik sehari.

<!-- S48 -->
Pada pengecekan berikutnya yang berhasil,
radio mengoreksi selisih itu.

<!-- S49 -->
Bahkan tempat jam mendengarkan pun berpengaruh.
Antenanya berupa batang ferit kecil
yang dililit kawat.

<!-- S50 -->
Antena paling peka saat batangnya melintang
terhadap arah pemancar,
bukan saat menunjuk ke arahnya.
Putar jamnya,
dan sinyal yang lemah bisa hilang sama sekali.

<!-- S51 -->
Itulah sebabnya satu jam berfungsi di rak,
sementara jam yang sama, dua meter dari situ,
di balik dinding beton bertulang, tak pernah bisa mengatur dirinya.

<!-- S52 -->
Lalu dari mana pemancar
mendapatkan waktunya?

<!-- S53 -->
Dari PTB,
lembaga metrologi nasional Jerman,
yang mengoperasikan jam atom.

<!-- S54 -->
Detik itu sendiri didefinisikan
oleh atom sesium.
Satu detik sama persis dengan
9.192.631.770 osilasi
radiasi yang dipancarkannya.

<!-- S55 -->
Jadi jam weker murah di meja samping tempat tidur
benar-benar
mengikuti standar waktu
yang didefinisikan oleh atom sesium.

<!-- S56 -->
Tapi tidak sempurna.
Sinyal merambat dengan kecepatan cahaya,
dan cahaya pun butuh sekitar 3 milidetik
untuk setiap 1.000 kilometer.

<!-- S57 -->
Penerima menambah jedanya sendiri,
dan jammu tidak mengoreksi semua itu.
Memang tidak perlu.
Jam itu hanya menampilkan detik.

<!-- S58 -->
Dari satu lokasi dekat Frankfurt,
sinyal itu menjangkau jam
hingga sekitar 2.000 kilometer jauhnya.
Itu sebagian besar Eropa.

<!-- S59 -->
Swiss dulu punya pemancar sendiri,
bernama HBG, sampai akhir 2011.
Antenanya perlu diganti,
terlalu sedikit orang yang memakainya,
dan jam di Swiss bisa saja
mendengarkan Jerman sebagai gantinya.

<!-- S60 -->
Negara lain mempertahankan miliknya.
Inggris, Prancis, Jepang, dan Tiongkok
semuanya punya pemancar sendiri.

<!-- S61 -->
Dan di Amerika Utara, WWVB
mengudara dari Fort Collins sejak 1963,
dengan kode waktu sejak 1965.

<!-- S62 -->
Prinsipnya sama, dialeknya beda.
Nol adalah penurunan selama dua persepuluh detik.
Satu berlangsung setengah detik.

<!-- S63 -->
Dan alih-alih satu celah per menit,
ada penanda yang lebih panjang setiap 10 detik,
seperti koma dalam kalimat.
Dua berturut-turut berarti menit baru.

<!-- S64 -->
Perbedaan terbesarnya
adalah waktu apa yang dikirim.
Jerman menyiarkan waktu sipil Eropa Tengah,
yang dipakai sebagian besar benua itu.

<!-- S65 -->
Tapi Amerika Serikat
membentang di beberapa zona waktu.
Jadi WWVB mengirim waktu universal, UTC,
dan kamu yang memberi tahu jam di mana kamu berada.

<!-- S66 -->
Pemancar itu bahkan tidak mengirim bulan.
Hanya hari ke berapa dalam setahun,
dari 1 sampai 366.

<!-- S67 -->
Tak satu pun stasiun ini
berbicara dalam bahasa yang sama.
Jam yang dibuat untuk Jerman
tidak bisa memahami Colorado.

<!-- S68 -->
Tapi di kedua sisi Samudra Atlantik,
rutinitasnya sama-sama sunyi.
Malam demi malam, sebuah penerima kecil
menyelaraskan diri dengan standar waktu atom
yang berjarak ratusan atau ribuan kilometer.

<!-- S69 -->
Jadi, ini pertanyaan untukmu.
Kalau semua sinyal waktu radio
hilang malam ini,
apa kamu bakal sadar?
Tulis jawabanmu di kolom komentar.
