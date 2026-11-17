<!-- S01 -->
Bayangkan kamu menyalakan PC Windows
dan tidak menemukan taskbar, tombol Mulai,
atau satu ikon pun di desktop.

<!-- S02 -->
Sebagai gantinya ada bilah tipis di bagian atas,
menu yang muncul di mana pun kamu mengklik,
dan empat desktop virtual berdampingan.

<!-- S03 -->
Kelihatannya seperti Linux.
Tapi program, driver, dan file kamu
masih persis di tempat kamu meninggalkannya.
Ini tetap Windows.

<!-- S04 -->
Hanya desktopnya yang berubah.
Dan sakelar yang mengubahnya
hanyalah satu pengaturan.

<!-- S05 -->
Windows menyimpannya di registry,
dalam nilai bernama Shell.
Di hampir setiap PC Windows,
isinya explorer.exe.

<!-- S06 -->
Tulis nama program lain di sana,
keluar lalu masuk lagi,
dan Windows akan menjalankan program itu sebagai gantinya.
Apa pun yang digambarnya menjadi desktop kamu.

<!-- S07 -->
Dan ini bukan trik yang baru ditemukan orang tahun lalu.
Pada 1990, Windows 3.0 sudah punya sakelar yang sama
di file teks biasa bernama system.ini.
Satu baris: shell=progman.exe.

<!-- S08 -->
Kalau nama itu diganti,
Program Manager, jendela penuh grup ikon,
sama sekali tidak muncul.

<!-- S09 -->
Jadi pertanyaannya bukan apakah Windows
bisa punya desktop lain.
Dari dulu bisa.
Pertanyaannya, kenapa hampir tidak ada yang pernah melihatnya.

<!-- S10 -->
Mulai dari apa yang sebenarnya ditunjuk baris itu.
Taskbar, ikon desktop,
area notifikasi kecil di dekat jam:
semuanya satu program, explorer.exe.

<!-- S11 -->
Ya, explorer.exe yang sama
yang kamu buka sebagai File Explorer untuk melihat file.
Ia mengerjakan dua tugas,
dan kebanyakan orang hanya menyadari satu.

<!-- S12 -->
Tugas kedua itu punya nama: shell.
Itulah lapisan yang kamu sentuh.
Di bawahnya ada kernel, driver,
dan layanan yang membuat Windows tetap berjalan.

<!-- S13 -->
Tidak satu pun dari mereka butuh taskbar.
Hentikan explorer.exe di Manajer Tugas,
maka taskbar dan ikon menghilang...
tapi Notepad, browser kamu,
dan semua jendela lain tetap berjalan.

<!-- S14 -->
Jalankan lagi, dan desktopnya kembali.
Itu kira-kira bukti paling jelas yang ada
bahwa desktop hanyalah program biasa.

<!-- S14b -->
Kalau kamu pernah mengganti launcher
di ponsel Android,
kamu sudah melihat ide yang mirip.
Di Android, itu pengaturan biasa.
Windows juga punya mekanismenya,
tapi tidak pernah memberi pengguna biasa
tombol yang sederhana untuk itu.

<!-- S15 -->
Tiga istilah sering tertukar di sini.
Shell adalah tempat kamu membuka berbagai hal:
taskbar, menu, desktop.
Window manager mengatur bagaimana jendela
diletakkan, ditumpuk, dan diberi fokus.
Lingkungan desktop
menyatukan seluruh pengalaman itu.

<!-- S16 -->
Di Linux, bagian-bagian ini bisa digabungkan
dengan banyak cara.
Di Windows, mengganti shell
tidak mengganti pengelolaan jendela sistem,
atau cara aplikasi menggambar bingkai jendelanya.

<!-- S17 -->
Itu tidak menghentikan orang untuk mencoba.
Di awal tahun 90-an, kamu bisa masuk ke toko
dan membeli pengganti Program Manager.

<!-- S18 -->
Norton Desktop for Windows
memberimu desktop sendiri,
alat pengelola file sendiri, dan peluncur sendiri,
di atas Windows yang sama.

<!-- S19 -->
Beberapa produsen komputer menggantinya
sebelum pembeli sempat menyalakan komputernya.
Navigator dari Packard Bell menyambut pembeli
dengan rumah yang bisa dijelajahi ruang demi ruang.

<!-- S20 -->
Lalu Windows 95 menyerahkan tugas itu ke explorer.exe,
dan baris di system.ini
berubah begitu saja menjadi explorer.exe.
Sakelarnya tetap di tempat yang sama.

<!-- S21 -->
Di akhir tahun 90-an,
satu komunitas utuh tumbuh di sekitar sakelar itu.
Proyek yang paling terkenal adalah LiteStep.

<!-- S22 -->
Tampilannya terinspirasi dari AfterStep,
window manager Unix yang meniru NeXTSTEP,
dari perusahaan yang didirikan Steve Jobs setelah keluar dari Apple.

<!-- S23 -->
LiteStep tidak punya menu Mulai kecuali kamu membuatnya sendiri.
Semuanya modul:
dock di sini, jam di sana,
menu yang terbuka di mana pun kamu klik kanan.

<!-- S24 -->
Temanya dibagikan seperti wallpaper.
Ada yang tampak futuristis.
Ada yang mirip workstation Unix.
Ada yang hampir tidak menyisakan apa pun di layar.

<!-- S25 -->
Blackbox for Windows mengambil arah sebaliknya.
Ia meniru Blackbox, window manager Unix yang minimalis,
sampai tinggal satu menu sederhana
dan satu toolbar tipis.

<!-- S26 -->
Penerusnya, bbLean,
membuat ide itu tetap hidup di Windows 2000 dan XP.

<!-- S27 -->
Emerge Desktop memecah shell menjadi bagian-bagian terpisah:
peluncur, area notifikasi, daftar tugas,
masing-masing program kecil yang bisa kamu pakai atau buang.

<!-- S28 -->
Kenapa repot-repot begitu?
Sebagian karena tampilan XP
gampang dikenali dan sulit diubah.
Tema mengubah warna dan tombol.
Tata letaknya tetap.

<!-- S29 -->
Sebagian karena memori.
Di mesin dengan 128 megabyte,
shell yang lebih ringan menjanjikan lebih banyak ruang
untuk yang lainnya.

<!-- S30 -->
Dan sebagian karena Linux.
Di sana, memilih desktop itu hal biasa,
dan sebagian pengguna Windows menginginkan
pilihan yang sama.

<!-- S31 -->
Sebagian besar proyek itu sekarang sudah tidak ada.
Rilis terakhir LiteStep adalah versi pratinjau
dari 2014, masih berlabel alfa.
Emerge Desktop dan SharpEnviro juga berhenti.

<!-- S32 -->
Tim relawan yang kecil jadi salah satu alasannya.
Tapi Windows juga berubah.
Seiring waktu, desktopnya menjadi jauh lebih
dari sekadar satu file executable.

<!-- S33 -->
Pengalaman desktop sekarang tersebar
di banyak proses,
komponen sistem, dan aplikasi terpaket.
Bahkan menu Mulai berjalan sebagai program tersendiri.

<!-- S34 -->
Mengganti explorer.exe tidak berarti mengganti
semua yang membentuk antarmuka Windows modern.
Dan itulah salah satu alasan kenapa membangun
desktop alternatif yang lengkap
lebih sulit daripada dulu.

<!-- S35 -->
Meski begitu, ini masih bisa.
Cairo Desktop, proyek open source,
berjalan di Windows 11 saat ini.

<!-- S36 -->
Ia membawa bilah menunya sendiri di bagian atas,
taskbar-nya sendiri,
dan folder yang bisa kamu sematkan ke bilah sebagai tumpukan.

<!-- S37 -->
Ia bisa berjalan berdampingan dengan explorer.exe,
atau mengambil alih sebagai shell.
Dalam mode kedua itu,
sebagian Windows 11 bisa bermasalah,
termasuk Pengaturan dan Keamanan Windows.

<!-- S38 -->
Seelen UI melakukannya dengan cara berbeda.
Ia tidak mengganti explorer.exe.
Ia menyembunyikan taskbar dan membawa bagiannya sendiri:
dock, bilah, widget,
dan window manager yang menyusun jendelamu berdampingan.

<!-- S39 -->
Hasilnya bisa sama sekali tidak mirip Windows.
Tapi di bawahnya, explorer.exe masih berjalan.
Ini wajah baru, bukan shell baru.

<!-- S40 -->
Lalu Microsoft?
Sebenarnya Microsoft punya fitur resmi untuk ini.
Namanya Shell Launcher,
dan dirancang untuk perangkat seperti kios.

<!-- S41 -->
Kamu mungkin pernah memakai yang seperti itu
tanpa sadar.
Mesin tiket di stasiun.
Mesin kasir mandiri. Mesin ATM.

<!-- S42 -->
Banyak di antaranya adalah PC Windows
yang seluruh shell-nya hanya satu aplikasi.
Administrator menentukan programnya,
dan setelah login, program itulah seluruh desktopnya.

<!-- S43 -->
Tapi fitur ini hanya tersedia
di edisi Enterprise, Education,
dan IoT Enterprise.

<!-- S44 -->
Dan mekanisme registry yang lama
masih menjadi bagian dari Windows.
Hanya saja Microsoft tidak pernah menjadikannya
pengaturan desktop biasa
untuk pengguna biasa.

<!-- S45 -->
Jadi kenapa Windows seolah hanya punya satu desktop?
Bukan karena tidak bisa punya yang lain.
Tapi karena desktop itulah produknya.

<!-- S46 -->
Di Linux, desktop adalah pilihan.
Beberapa distribusi memintamu memilih satu
saat kamu masih menginstal.
KDE Plasma, GNOME, Xfce, Cinnamon...

<!-- S47 -->
Di Windows, desktop adalah apa yang Microsoft tampilkan
di setiap iklan, setiap tangkapan layar,
dan setiap halaman dukungan.
Satu desktop berarti satu set petunjuk
untuk lebih dari satu miliar mesin.

<!-- S48 -->
Itu keuntungan yang nyata.
Kalau ada yang rusak,
layar di artikel bantuan terlihat sama dengan punyamu.
Tapi akibatnya, kebanyakan orang tidak pernah tahu
bahwa sebenarnya ada pilihan.

<!-- S49 -->
Orang sudah mengganti desktop Windows
bahkan sebelum Windows 95 ada.
Mereka membuat dock, menu polos,
dan desktop yang tidak mirip desktop lain mana pun.

<!-- S50 -->
Sebagian besar proyek itu sudah hilang.
Idenya tidak.
Di bawah setiap taskbar yang pernah kamu klik,
masih ada satu pengaturan itu, menunggu nama yang lain.

<!-- S51 -->
Desktop hanyalah satu lagi perangkat lunak.
Dan perangkat lunak bisa diganti.

<!-- S52 -->
Jadi, ini pertanyaan untukmu.
Kalau Windows membiarkanmu memilih desktop
saat instalasi, seperti beberapa distribusi Linux,
apakah kamu akan beralih, atau tetap memakai yang sudah kamu kenal?
Tulis di kolom komentar.
