<!-- S01 -->
948.
Sebanyak itulah cara berbeda yang ditemukan sebuah AI
untuk mengambil alih komputer Linux dari dalam.

<!-- S02 -->
Tanpa kata sandi curian. Tanpa pembobolan jarak jauh.
Setiap cara dimulai dari pengguna biasa
yang tidak punya hak khusus apa pun,
dan berakhir dengan root,
akun yang bisa melakukan apa saja.

<!-- S03 -->
OpenAI menerbitkan hasilnya pada November 2026.
Seluruh prosesnya menghabiskan
1,2 juta dolar AS dalam kredit API.

<!-- S05 -->
Ini angka dari OpenAI sendiri,
diterbitkan sehari sebelum
mereka meluncurkan model yang menghasilkannya,
dan belum ada pihak luar yang mengonfirmasi jumlah lengkapnya.
Tapi ratusan laporan dan patch
sudah dikirimkan.

<!-- S06 -->
Inilah kenapa ini penting di luar Linux.
Kode sumber Linux itu publik.
Siapa pun bisa membacanya.
Selama puluhan tahun, itulah argumen
kenapa Linux aman.

<!-- S07 -->
Jadi, kalau mesin bisa membaca kode publik
dan mengubahnya menjadi eksploit yang berfungsi dalam skala ini,
haruskah perangkat lunak merahasiakan kodenya saja?

<!-- S08 -->
Mari lihat perangkat lunak yang sudah melakukannya.
Pada April 2026, Microsoft memperbaiki
164 celah keamanan
pada hari patch bulanannya.
Pada Oktober, Microsoft memperbaiki
1.413.

<!-- S09 -->
Dalam satu bulan itu saja, Microsoft memperbaiki lebih banyak
daripada dalam satu tahun penuh mana pun sebelumnya.
Lebih dari 1.000 perbaikan itu ada di Windows,
dan Microsoft sudah memperingatkan
bahwa alat AI miliknya sendiri akan mendorong lonjakan itu.

<!-- S10 -->
Kamu tidak bisa membandingkan kedua angka itu secara langsung.
Setiap perusahaan menghitung dengan cara berbeda,
dan Microsoft menelusuri kode privatnya sendiri.

<!-- S11 -->
Tapi ini menunjukkan satu hal.
Merahasiakan kode
tidak mencegah munculnya bug.

<!-- S12 -->
Jadi, apa yang sebenarnya melindungimu?
Untuk menjawabnya,
kita perlu melihat cara kerja mesin ini,
karena setiap tahapnya menyaring sesuatu.

<!-- S13 -->
Kernel Linux punya
lebih dari 40 juta baris kode.
Pertama, agen pengintai menjelajahinya
dan memilih bagian-bagian
yang benar-benar bisa dijangkau pengguna biasa.

<!-- S14 -->
Tersisa sekitar 7%.
Itulah bagian yang mereka nilai layak diserang,
bukan sampel acak,
jadi kamu tidak bisa mengalikan hasilnya dengan 14.

<!-- S15 -->
Berikutnya, agen analis memeriksa kode itu
dan mencatat semua yang mencurigakan.
2.308 kandidat,
dalam 12 jam.

<!-- S16 -->
Tapi kecurigaan tidak membuktikan apa-apa.
Jadi agen lain menulis program uji
dan menjalankannya di mesin virtual yang terisolasi.
1.724 bug
ternyata nyata.

<!-- S17 -->
Lalu tibalah bagian yang mahal:
membangun eksploit yang berfungsi,
dengan perlindungan standar
sistem desktop biasa dalam keadaan aktif.
1.169
berhasil mencapai root.

<!-- S18 -->
Kelompokkan berdasarkan celah dasarnya,
dan kamu mendapat angka 948.

<!-- S19 -->
Ada satu detail dalam laporan itu
yang sulit dilupakan.
Dalam salah satu proses awal,
para agen melaporkan 200 keberhasilan.
Lalu manusia memeriksa bagaimana mereka sampai ke sana.

<!-- S20 -->
Dua puluh di antaranya mencapai root
lewat bug lain yang belum diketahui,
bukan bug yang diperintahkan untuk dipakai.
Disuruh membuka satu pintu,
mereka menemukan pintu lain yang tak diketahui siapa pun.

<!-- S21 -->
Dalam sampel eksploitnya,
OpenAI mengidentifikasi sepuluh teknik eksploitasi
yang belum pernah dilihat para ahli luar.

<!-- S22 -->
Pada Juli, model sebelumnya
menemukan 166 celah semacam ini.
Setelah tiga bulan perbaikan,
model yang lebih baru menemukan 948.
Bug-nya belum habis.
Proses yang belakangan menemukan jauh lebih banyak.

<!-- S23 -->
Nah, ada satu batasan penting.
Semua ini tidak bisa membobol komputermu
lewat internet.
Penyerang harus sudah berada di mesin itu,
sebagai pengguna biasa.

<!-- S24 -->
Itu tidak semenenangkan kedengarannya,
karena serangan nyata sering terjadi dalam dua langkah.
Pertama, penyerang masuk,
lewat celah di browser atau unduhan berbahaya.
Lalu dia butuh root.
Inilah langkah kedua itu.

<!-- S25 -->
Saran OpenAI terus terang.
Di sistem tanpa patch terbaru,
anggap setiap akun biasa sebagai root,
setidaknya terhadap penyerang yang punya banyak dana.

<!-- S26 -->
Jadi, bagaimana nasib
argumen lama untuk kode terbuka?
Pada akhir tahun sembilan puluhan,
Eric Raymond memberinya slogan:
"Dengan cukup banyak mata, semua bug mudah ditemukan."

<!-- S27 -->
Dia menyebutnya Hukum Linus.
Itu ide yang indah, dengan satu asumsi di dalamnya:
bahwa ada orang yang benar-benar melihat.

<!-- S28 -->
Pada 2014, sebuah bug bernama Heartbleed
muncul di OpenSSL,
kode yang melindungi sebagian besar web.
Sekitar setengah juta server aman
diperkirakan terpapar.

<!-- S29 -->
Bug itu sudah dua tahun berada di kode publik.
Proyek itu menerima
sekitar 2.000 dolar AS per tahun dari donasi
dan hanya punya satu pengembang penuh waktu.

<!-- S30 -->
Siapa pun bisa membacanya.
Hampir tak ada yang melakukannya.

<!-- S31 -->
Itulah kelemahan sejati open source sejak dulu.
Bukan terlalu banyak mata yang melihat kode. Terlalu sedikit.

<!-- S32 -->
Dan bagian itulah yang diubah AI.
Mesin bisa terus memindai,
dan menyelidiki jauh lebih banyak kandidat
daripada yang sanggup ditangani seorang peneliti sendirian.
Janji lama akhirnya ditepati,
untuk semua orang, termasuk penyerang.

<!-- S33 -->
Jadi kode publik sekarang benar-benar diperiksa.
Apakah menyembunyikannya membantu?

<!-- S34 -->
Program tertutup tetap harus dijalankan,
jadi kode mesinnya ada
di setiap komputer yang memakainya.
Alat seperti Ghidra mengubahnya kembali
menjadi sesuatu yang mirip kode sumber.

<!-- S35 -->
Dan ada satu trik klasik.
Bandingkan sebuah program
sebelum dan sesudah pembaruan keamanan.
Apa pun yang berubah menunjukkan di mana celahnya.

<!-- S35b -->
Itu memberi tahu penyerang ke mana harus membidik,
jauh sebelum setiap sistem
selesai memasang pembaruan itu.

<!-- S36 -->
Anthropic mencoba ini pada kernel Windows,
dengan 21 celah
yang baru saja ditambal Microsoft,
dan tanpa kode sumber.
AI memicu crash pertama dalam 31 menit.
Dalam enam jam, ada 18.

<!-- S37 -->
Delapan menjadi eksploit yang berfungsi
yang mampu mengambil alih mesin sepenuhnya,
dengan biaya sekitar 2.000 dolar AS masing-masing.

<!-- S38 -->
Tapi ini bukan bug yang belum diketahui.
Patch-nya sudah menunjuk
ke tempat masalahnya.
Menemukan celah baru dari nol lebih sulit.

<!-- S39 -->
Jadi kerahasiaan masih membebani penyerang.
Ini polisi tidur, bukan tembok.
Seberapa tinggi polisi tidurnya?
Tidak ada angka publiknya.

<!-- S40 -->
Bagaimana dengan sisi lainnya?
Apa yang sebenarnya kamu dapat dari keterbukaan?
Jawabannya ada di satu detail kecil
dalam laporan OpenAI.

<!-- S41 -->
Selama sepuluh hari pemindaian dan analisis itu,
lebih dari 100 celah Linux ini
sudah diperbaiki, atau hampir,
oleh orang lain.
Sekitar 300 lainnya
sudah dibahas secara publik.

<!-- S42 -->
Orang lain menemukan bug yang sama
pada waktu yang sama.

<!-- S43 -->
Linus Torvalds sudah menggambarkan ini sejak Mei.
Dia bilang laporan dari AI
membuat milis keamanan kernel
"hampir sepenuhnya tak terkendali",
karena orang-orang yang berbeda terus menemukan
hal yang sama dengan alat yang sama.

<!-- S44 -->
Dan sarannya begini:
"Kalau kamu menemukan bug dengan alat AI,
kemungkinan besar orang lain juga menemukannya."

<!-- S45 -->
Aturan kernel kini mengatakannya terang-terangan.
Bug yang ditemukan dengan AI harus dianggap publik,
karena bug semacam ini ditemukan
oleh beberapa peneliti sekaligus,
sering kali pada hari yang sama.

<!-- S46 -->
Pikirkan apa artinya itu
bagi gagasan tentang bug rahasia.
Kalau murah bagimu untuk menemukannya,
berarti murah juga bagi semua orang.

<!-- S47 -->
Dengan open source,
siapa pun bisa memeriksa laporannya,
memverifikasi perbaikannya, dan menggugat hasilnya.
Dengan perangkat lunak tertutup,
kamu kebanyakan harus percaya pada vendornya.

<!-- S49 -->
Tapi keterbukaan juga ada harganya,
dan bukan seperti yang kamu kira.
Mudah untuk berkata
bahwa proyek kecil tidak sanggup membayar pemindaian.
Perusahaan AI sudah
menawarkan akses gratis kepada para pengelola.

<!-- S50 -->
Yang kurang adalah orangnya.
Kernel dulu mencatat
sekitar 500 masalah keamanan per rilis.
Tahun ini, jumlahnya melewati 1.500.
Banyak yang kecil,
tapi tetap harus ada yang memeriksanya.

<!-- S51 -->
Pada Januari, proyek curl
menghentikan program bug bounty berbayarnya,
agar tidak lagi memberi hadiah pada banjir laporan sampah.

<!-- S52 -->
Laporan yang bagus pun hanya memindahkan pekerjaan.
Patch buatan AI tetap butuh tinjauan manusia.
Beberapa perbaikan awal menambahkan kode yang tidak perlu
atau melewatkan versi lain dari bug yang sama.

<!-- S53 -->
Kamu bisa membeli lebih banyak pemindaian.
Tapi uang tidak bisa mendatangkan lebih banyak orang
yang memahami sepotong kode sebaik itu.
Di sini, perusahaan dengan tim keamanan berbayar
memang punya keunggulan.

<!-- S54 -->
Lalu datanglah masalah terakhir.
Diperbaiki tidak sama dengan terpasang.

<!-- S55 -->
Pada Maret 2017,
Microsoft menambal celah di Windows.
Kode tertutup, satu vendor, satu sistem pembaruan.
Dua bulan kemudian,
WannaCry masuk lewat lubang yang sama,
ke sekitar 200.000 komputer
di sekitar 150 negara.

<!-- S56 -->
Patch itu punya dua bulan untuk menyebar,
dan itu tidak cukup.
Penyerang mungkin tak lagi memberimu dua bulan.
Dalam studi Anthropic yang sama,
AI mengambil perbaikan publik
untuk mesin JavaScript Firefox
dan punya eksploit yang berfungsi dalam kurang dari satu jam.

<!-- S57 -->
Versi Firefox yang sudah diperbaiki
baru akan keluar 18 hari lagi.

<!-- S58 -->
Inilah bahayanya menerbitkan perbaikan.
Informasinya bisa sampai ke penyerang
sebelum pembaruannya sampai kepadamu.

<!-- S59 -->
Perbaikan Linux harus menempuh perjalanan panjang,
dari kernel ke rilis stabil,
ke distribusimu, ke perangkatmu.
Ponsel bisa menunggu berbulan-bulan, atau selamanya.

<!-- S60 -->
Dan perangkat lunak tertutup tidak lolos dari ini.
Kita baru saja melihatnya: patch Windows sudah cukup.
Setiap pembaruan kini juga sebuah peta.

<!-- S60b -->
Jadi, selalu perbarui semuanya,
komputermu, ponselmu, bahkan routermu,
dan pasang pembaruan begitu tersedia.
Seiring AI makin pandai mengubah perbaikan menjadi serangan,
setiap hari kamu menunda akan makin berarti.

<!-- S61 -->
Jadi, apakah open source masih lebih aman?
Jujur saja, tidak ada yang tahu.
Sejauh yang diketahui publik,
belum ada yang menjalankan uji yang sama di kedua sisi,
dengan aturan yang sama.

<!-- S62 -->
Yang bisa kita katakan lebih sederhana.
Manfaat menyembunyikan kode kini lebih kecil daripada dulu.
Membukanya memungkinkan siapa pun memeriksa pekerjaan itu,
dan menyerahkan tumpukan pekerjaan yang lebih besar
kepada orang-orang yang mengelolanya.

<!-- S64 -->
Bahkan kalau AI tidak pernah menemukan semua bug,
AI sudah mengubah biaya untuk menemukannya.

<!-- S65 -->
Yang penting sekarang adalah berapa lama sebuah celah tetap terbuka
antara saat seseorang menemukannya
dan saat celah itu ditutup di mesinmu.

<!-- S66 -->
Jadi, ini pertanyaan untukmu.
Kalau bug apa pun bisa ditemukan oleh siapa pun,
kamu lebih memilih memercayai kode yang bisa kamu baca,
atau perusahaan yang dibayar untuk memperbaikinya?
Tulis di kolom komentar.
