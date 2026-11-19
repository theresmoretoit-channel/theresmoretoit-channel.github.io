<!-- S01 -->
Pada tahun 1993, sebuah game bernama Doom
berjalan di komputer
dengan memori 4 megabyte.

<!-- S02 -->
Itu kira-kira seukuran
satu foto di ponselmu.

<!-- S03 -->
Belum ada akselerator 3D.
Prosesor utama
mengerjakan semua rendering.

<!-- S04 -->
Sekarang, developer mulai dengan sebuah engine,
seperti Unity atau Unreal,
yang mengurus grafis, suara,
memori, dan perangkat keras.

<!-- S05 -->
Di DOS, semua itu
adalah masalah developer.
Dan cukup sering, masalah pemain juga.

<!-- S06 -->
Jadi, seberapa sulit
membuat game untuk DOS?

<!-- S07 -->
Mari mulai dari memori,
karena memori itu kacau.

<!-- S08 -->
IBM PC asli, dari tahun 1981,
bisa mengalamati hingga 1 megabyte memori.

<!-- S09 -->
Tapi hanya
640 kilobyte pertama
yang ditujukan untuk program.

<!-- S10 -->
Sisanya, 384,
dicadangkan untuk memori video,
kartu ekspansi, dan BIOS.

<!-- S11 -->
Selama lebih dari satu dekade,
DOS biasanya menjalankan program
di dalam ruang itu.
Apa pun di luarnya butuh kerja ekstra.

<!-- S12 -->
Dari situlah kalimat terkenal ini berasal.
640K seharusnya cukup untuk siapa pun.

<!-- S13 -->
Kalimat itu biasanya dikaitkan dengan Bill Gates.
Tidak ada catatan bahwa dia pernah mengatakannya,
dan dia menyangkalnya.

<!-- S14 -->
Di awal tahun sembilan puluhan,
sebuah PC dijual dengan 4 megabyte,
atau 8.

<!-- S15 -->
Dan sebuah game masih bisa berhenti
dengan pesan
"memori tidak mencukupi".

<!-- S16 -->
Punya memori
dan bisa memakainya
adalah dua hal yang berbeda.

<!-- S17 -->
Salah satu jalan keluarnya adalah expanded memory,
atau EMS.

<!-- S18 -->
Sebuah jendela 64 kilobyte
berada di bagian atas
megabyte pertama itu.
Lewat jendela itu, program bisa melihat
4 halaman memori tambahan,
masing-masing 16 kilobyte,

<!-- S19 -->
dan menukarnya dengan halaman lain,
seperti membalik halaman buku
lewat lubang di selembar kertas.

<!-- S20 -->
Jalan lainnya adalah extended memory,
yang diakses lewat driver bernama HIMEM.

<!-- S21 -->
Dan di sinilah
masalah developer
menjadi masalah pemain.

<!-- S22 -->
Driver untuk mouse, drive CD,
atau kartu suara
menggerogoti memori yang berharga itu,
kecuali kamu berhasil memuatnya ke memori atas.

<!-- S23 -->
Jadi para pemain belajar mengedit dua file,
CONFIG.SYS dan AUTOEXEC.BAT.

<!-- S24 -->
Satu game butuh EMS.
Game lain ingin EMS dimatikan,
dengan pengaturan bernama NOEMS.
Dan game ketiga butuh setiap kilobyte yang tersisa.

<!-- S25 -->
Pada tahun 1993, MS-DOS 6 menambahkan
menu saat startup.

<!-- S26 -->
Kamu memilih konfigurasi
untuk game yang ingin kamu mainkan,
dan komputer menyala khusus untuk game itu.

<!-- S27 -->
Sebagian orang akhirnya punya
entri tersendiri
untuk hampir setiap game yang mereka miliki.

<!-- S28 -->
Tapi saat itu,
game-game yang lebih besar sudah menemukan
cara untuk menembus batas DOS.

<!-- S29 -->
Sejak 386,
prosesornya sendiri bisa berjalan
dalam protected mode 32-bit,
dengan ruang alamat hingga 4 gigabyte.

<!-- S30 -->
Kita sudah membahas protected mode
di video sebelumnya.
Tapi DOS tidak bisa memakainya.

<!-- S31 -->
Jadi game membawa pembantunya sendiri,
sebuah DOS extender.
Yang paling terkenal adalah DOS/4GW.

<!-- S32 -->
DOS/4GW disertakan bersama compiler populer,
Watcom C.

<!-- S33 -->
Saat sebuah game dimulai,
DOS/4GW mengalihkan prosesor
ke protected mode,
sehingga game mendapat akses
ke memori di atas batas DOS.

<!-- S34 -->
DOS masih ada di bawahnya,
menyediakan layanan seperti akses file.
Tapi game sekarang berjalan dalam protected mode,
bukan sebagai program DOS biasa.

<!-- S35 -->
Kalau kamu main game DOS di tahun sembilan puluhan,
kamu pernah melihat namanya
muncul sekilas di layar.

<!-- S37 -->
Sekarang, soal gambar.
Di salah satu mode VGA yang paling banyak dipakai,
yang disebut Mode 13h,
layarnya berukuran 320
kali 200 piksel,
dengan 256 warna.

<!-- S38 -->
Setiap piksel adalah satu byte.
Untuk mewarnai sebuah piksel,
kamu menulis sebuah angka ke memori.
Tanpa library grafis. Hanya memori.

<!-- S39 -->
Seluruh layar memakan
64.000 byte.

<!-- S40 -->
Itu sedikit di bawah 64 kilobyte,
cukup kecil untuk muat dalam satu segmen,
blok yang bisa dialamatkan
oleh program 16-bit sekaligus.
Kali ini, memori justru menguntungkanmu.

<!-- S41 -->
Tapi kalau kamu menggambar langsung
ke layar yang terlihat,
pemain akan melihat gambar setengah jadi,
dan gambarnya berkedip.

<!-- S42 -->
Jadi game menggambar setiap frame
lebih dulu di buffer tersembunyi,
lalu menyalin gambar yang sudah jadi
ke memori video.

<!-- S43 -->
Pada tahun 1991, Michael Abrash,
seorang programmer dan penulis,
menerbitkan cara yang lebih baik.
Dia menyebutnya Mode X.

<!-- S44 -->
Cara itu memakai bagian dari VGA
yang belum pernah disentuh
sebagian besar programmer.

<!-- S45 -->
Hasilnya piksel persegi,
dan ruang untuk beberapa layar
di memori video.

<!-- S46 -->
Game menggambar di layar
yang tidak bisa dilihat siapa pun,
lalu cukup beralih ke layar itu.
Tapi jauh lebih sulit diprogram.

<!-- S47 -->
Lalu ada soal suara.
Dan suara itu seperti lotre.

<!-- S48 -->
Speaker bawaan PC
dibuat untuk berbunyi bip.

<!-- S49 -->
Lalu datang kartu suara,
dan perangkat suara lainnya.
Tidak ada dua yang
bekerja dengan cara yang sama.

<!-- S50 -->
AdLib, dengan chip Yamaha
yang menyintesis musik.
Sound Blaster, yang juga bisa memutar
suara rekaman.

<!-- S51 -->
Roland MT-32,
sebuah kotak mahal dengan instrumen yang lebih kaya.
Gravis UltraSound.

<!-- S52 -->
Mendukung semuanya
berarti menulis driver yang berbeda-beda.

<!-- S53 -->
Dan game harus tahu
di mana kartu itu berada.
Port-nya, interupsinya,
dan kanal DMA-nya.

<!-- S54 -->
Jawaban yang lazim, untuk Sound Blaster,
adalah port 220, IRQ 7, DMA 1.
Biasanya.

<!-- S55 -->
Salah satu saja,
dan game-nya bisu.
Atau macet.

<!-- S56 -->
Pada tahun 1991, seorang programmer bernama John Miles
merilis sebuah library
yang bisa berbicara dengan banyak kartu suara
lewat satu antarmuka.

<!-- S57 -->
Game bisa menulis kode suaranya sekali saja,
dan membiarkan library mengurus kartunya.

<!-- S58 -->
Itu satu lapisan lagi
antara game dan perangkat keras.
Ingat itu.

<!-- S59 -->
Lalu ada soal kecepatan.
Programmer menghitung
setiap langkah yang diambil prosesor.

<!-- S63 -->
Untuk menemukan sebuah piksel di layar,
kamu mengalikan barisnya
dengan 320.

<!-- S63b -->
Di prosesor yang lebih tua,
perkalian bisa mahal.

<!-- S64 -->
Tapi 320
adalah 256
ditambah 64.
Keduanya pangkat dua.

<!-- S65 -->
Jadi kamu bisa mengganti perkalian itu
dengan dua pergeseran bit dan satu penjumlahan.

<!-- S67 -->
Chris Sawyer bekerja sedekat mungkin dengan perangkat keras.
Dia menulis Transport Tycoon pada tahun 1994
hampir seluruhnya dalam bahasa assembly,

<!-- S68 -->
instruksi
yang dipahami langsung oleh prosesor,
satu per satu.

<!-- S69 -->
Dan kadang,
semua itu pun belum cukup.

<!-- S70 -->
Pada tahun 1990, Wing Commander punya bug
yang tidak bisa ditemukan timnya,
padahal tenggat sudah dekat.

<!-- S71 -->
Saat kamu keluar dari game,
pengelola memorinya crash
dengan pesan error.

<!-- S72 -->
Jadi seorang programmer, Ken Demarest,
membuka pengelola memori itu
di hex editor
dan mengubah teks pesan tersebut.

<!-- S73 -->
Sekarang isinya:
"Terima kasih sudah memainkan Wing Commander."

<!-- S74 -->
Lalu tim menemukan bug yang sebenarnya,
dan lelucon itu tidak pernah masuk ke versi rilis.

<!-- S74b -->
Sebagian pemain masih yakin pernah melihatnya.
Dan game Origin berikutnya
memang berpamitan seperti itu.

<!-- S75 -->
Yang membawa kita kembali ke Doom.

<!-- S76 -->
Doom memakai DOS/4GW
dan berjalan sebagai program 32-bit.

<!-- S77 -->
Perangkat keras titik mengambang
tidak dijamin ada di setiap PC.

<!-- S78 -->
Jadi Doom memakai aritmetika titik tetap.
Bilangan bulat,
dengan 16 bit paling rendah
mewakili bagian pecahannya.

<!-- S79 -->
Dan dunianya tidak
benar-benar tiga dimensi.

<!-- S80 -->
Setiap level adalah denah datar,
dengan ketinggian untuk setiap lantai
dan setiap langit-langit.

<!-- S81 -->
Satu ruangan tidak pernah bisa berada di atas ruangan lain.
Dan kamu tidak bisa benar-benar melihat ke atas atau ke bawah.

<!-- S82 -->
Sebelum sebuah level bisa dimainkan,
sebuah alat memotong peta
menjadi pohon biner, sebuah BSP.

<!-- S83 -->
Engine menelusuri pohon itu
dari depan ke belakang,
mulai dari sisi pemain,
dan melewati area yang tidak terlihat.

<!-- S84 -->
Dan Doom bahkan tidak ditulis di DOS.

<!-- S85 -->
id Software membuatnya
di workstation NeXT,
lalu meng-compile hasilnya untuk DOS.

<!-- S86 -->
Doom bukan engine 3D serbaguna.
Ia dibuat untuk tepat
satu jenis dunia.
Spesialisasi itulah
yang membantunya berjalan di 386.

<!-- S87 -->
Dan studio lain menginginkan dunia itu.

<!-- S88 -->
Raven Software melisensikan engine Doom
untuk Heretic, pada tahun 1994,
dan Hexen, pada tahun 1995.

<!-- S89 -->
Doom ikut memantapkan
cara baru membuat game.
Studio bisa melisensikan engine yang sudah ada,
alih-alih membangun semuanya dari nol.

<!-- S90 -->
Sebuah extender memori.
Sebuah library suara.
Sebuah engine berlisensi.

<!-- S91 -->
Masing-masing mengambil alih satu masalah
dari developer.
Dan lapisannya terus bertambah,
hingga menjadi engine
yang dipakai developer sebagai titik awal hari ini.

<!-- S92 -->
Jadi, apakah membuat game dulu lebih sulit?
Dalam banyak hal, ya.

<!-- S93 -->
Tapi kesulitannya tidak hilang.
Ia berpindah.

<!-- S94 -->
Sekarang, developer bergulat
dengan gigabyte aset
dan jutaan poligon,
bukan dengan beberapa ratus kilobyte.

<!-- S95 -->
Di DOS, bahkan pemain
harus tahu ke mana memorinya pergi.

<!-- S96 -->
Jadi, ini pertanyaan untukmu.
Apakah kamu ingat pernah membuat
menu boot hanya supaya satu game bisa jalan?
Dan apakah itu merepotkan,
atau justru separuh keseruannya?
Ceritakan di kolom komentar.
