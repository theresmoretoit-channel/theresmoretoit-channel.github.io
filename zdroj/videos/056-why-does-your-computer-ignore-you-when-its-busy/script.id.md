<!-- S01 -->
Kamu mengeklik sebuah tombol.
Tidak terjadi apa-apa.
Kamu mengeklik lagi.
Masih tidak ada.

<!-- S02 -->
Kamu menggerakkan tetikus.
Tidak ada.
Selama beberapa detik
komputer tampak mati total.

<!-- S03 -->
Lalu semuanya terjadi sekaligus.
Jendela bergeser.
Menu terbuka.
Semua klikmu sampai,
semuanya sekaligus.

<!-- S04 -->
Dan ini bagian anehnya.
Komputer tahu kamu mengeklik.
Ia tahu dalam hitungan mikrodetik.

<!-- S05 -->
Ini bukan tebakan.
Saat ini juga, ketika kamu
tidak melakukan apa-apa,
mesinmu menangani ribuan
peristiwa perangkat keras per detik.

<!-- S06 -->
Sebuah tombol ditekan.
Sebuah paket datang.
Sebuah timer terpicu.
Sebuah disk selesai bekerja.

<!-- S07 -->
Masing-masing itu adalah interupsi,
dan komputer bekerja begitu
sejak tahun lima puluhan,
justru untuk ini:

<!-- S08 -->
supaya prosesor bisa bereaksi
pada dunia di luar dirinya.

<!-- S09 -->
Jadi perangkat keras melaporkan klikmu.
Prosesor menyadarinya.
Dan kamu tetap duduk lima detik
di depan layar yang mati.

<!-- S10 -->
Bukankah pengguna harus didahulukan?

<!-- S11 -->
Ada jawabannya,
dan bukan
karena komputermu terlalu lambat.

<!-- S12 -->
Jawabannya: disadari
dan dilayani itu
dua hal yang sangat berbeda.

<!-- S13 -->
Mari mulai dari menyadari.
Bayangkan komputer tanpa interupsi.

<!-- S14 -->
Prosesor harus
bertanya berulang-ulang:
apakah ada sesuatu dari papan ketik?
apakah diska sudah selesai?

<!-- S15 -->
Apakah ada paket datang?
Apakah tetikus bergerak?
Lalu bertanya lagi.
Dan lagi.

<!-- S16 -->
Hampir semua jawabannya tidak,
dan bertanya itu sendiri
akan memakan mesin itu hidup-hidup.

<!-- S17 -->
Maka perangkat diberi cara
untuk mengangkat tangan. Tetikus bergerak,
perangkat keras memicu interupsi,

<!-- S18 -->
dan prosesor melepaskan
apa pun yang sedang dikerjakan,
melompat ke sepotong kode pendek
yang disebut penangan,

<!-- S19 -->
dan sistem operasi mengetahui
bahwa sesuatu telah terjadi.

<!-- S20 -->
Ini gagasan yang brilian.
Dan menuntun ke satu asumsi
yang sangat masuk akal.

<!-- S21 -->
Kalau prosesor bisa direnggut
dari apa pun, seketika,
maka klikku pun pasti
ditangani seketika juga.

<!-- S22 -->
Hanya saja penangan tidak boleh
melakukan banyak hal.

<!-- S23 -->
Selama prosesor menjalankannya,
semua yang lain menunggu.
Termasuk interupsi berikutnya.
Dan itu sudah dalam perjalanan.

<!-- S24 -->
Jadi aturannya justru kebalikan
dari yang kamu kira.
Penangan melakukan sesedikit
mungkin.

<!-- S25 -->
Ia mencatat apa yang terjadi.
Ia memberi tahu perangkat
bahwa pesannya sudah sampai.
Ia menaruh peristiwa itu di antrean.
Lalu pergi.

<!-- S26 -->
Pengembang kernel bahkan membagi
pekerjaan jadi dua bagian bernama:
yang harus terjadi sekarang,
dan yang bisa menunggu.

<!-- S27 -->
Semua yang menarik,
semua yang akan pernah kamu lihat,
ada di paruh yang kedua.

<!-- S28 -->
Dan inilah jawaban pertamanya.
Interupsi mendapat
perhatian komputer.

<!-- S29 -->
Ia tidak menaruh programmu
di prosesor.

<!-- S30 -->
Baik, katamu. Kalau begitu perbaiki.
Jadikan masukan hal paling
penting di seluruh gedung.

<!-- S31 -->
Tetikus? Prioritas tertinggi.
Papan ketik? Prioritas tertinggi.
Jendela di depanmu?
Prioritas tertinggi.

<!-- S32 -->
Sisanya menunggu gilirannya.
Kedengarannya jelas masuk akal.

<!-- S33 -->
Dan bantahan terbaiknya
terjadi di Mars.

<!-- S34 -->
Pada 1997 pendarat Pathfinder
mendarat dan mulai bekerja.
Lalu, beberapa hari kemudian,
ia mulai memulai ulang sendiri.

<!-- S35 -->
Bukan sinar kosmik.
Bukan komponen rusak.
Masalah penjadwalan.

<!-- S36 -->
Ada sebuah tugas berprioritas tinggi
yang mengantarkan data
ke seluruh wahana,
dan ia butuh memori bersama.

<!-- S37 -->
Sebuah tugas berprioritas rendah,
yang mengumpulkan data cuaca,
sampai di sana lebih dulu
dan memegangnya.

<!-- S38 -->
Yang sebentar saja
sebenarnya tidak masalah.
Tapi lalu tugas berprioritas menengah
mengambil alih prosesor,

<!-- S39 -->
dan yang berprioritas rendah
tak pernah sampai selesai.
Jadi ia tak pernah melepaskannya.

<!-- S40 -->
Tugas terpenting
di seluruh wahana
kini tersangkut di belakang
yang paling tidak penting.

<!-- S41 -->
Ini ada namanya.
Inversi prioritas.

<!-- S42 -->
Timer watchdog melihat
bahwa tugas penting itu
sudah terlalu lama tidak berjalan,
menyimpulkan ada bencana,

<!-- S43 -->
dan memulai ulang seluruh wahana.
Lalu terjadi lagi.
Dan lagi.

<!-- S44 -->
Para insinyur di Bumi menemukan
sebabnya dan mengirim perbaikan.

<!-- S45 -->
Dan pelajarannya gratis,
tinggal dibawa pulang.
Prioritas tinggi tidak berarti
kamu akan dilayani.

<!-- S46 -->
Artinya hanya kamu ditanya lebih dulu.
Kalau yang kamu butuhkan
dipegang seseorang yang lebih lambat,
kepentinganmu tidak membeli apa-apa.

<!-- S47 -->
Dan prioritas punya batas kedua.
Ia menentukan urutan.
Ia tidak menciptakan satu pun
siklus tambahan.

<!-- S48 -->
Misalkan semua intimu
berada di seratus persen.
Kamu kira itu berarti membeku.
Biasanya tidak.

<!-- S49 -->
Penjadwal membagikan potongan waktu
begitu cepat
sampai kamu tak merasakan peralihannya.

<!-- S50 -->
Karena itu kamu bisa mengompilasi
sesuatu yang besar sekali
dan sekaligus menggulir
sebuah halaman web.

<!-- S51 -->
Di bawah beban yang berubah
sebenarnya bukan kecepatan.
Komputer itu tidak lambat.

<!-- S52 -->
Ia datang terlambat.

<!-- S53 -->
Kamu mengeklik, dan jawabannya datang
setengah detik kemudian.
Lalu satu detik.
Lalu lima.

<!-- S54 -->
Dan manusia jago sekali
menyadari hal seperti itu.
Setengah detik terasa seperti mesin
yang sedang berpikir.

<!-- S55 -->
Lima detik terasa seperti mesin
yang sudah mati.

<!-- S56 -->
Dan ada versi dari ini
yang paling mengejutkan.
Kadang masalahnya sama sekali
bukan pada prosesor.

<!-- S57 -->
Buka terlalu banyak sekaligus
dan memori fisik pun penuh.
Sistem mulai memindahkan
halaman memori ke penyimpanan.

<!-- S58 -->
Kalau itu terkumpul cukup banyak,
mesin menghabiskan waktunya
mengaduk-aduk memori
alih-alih mengerjakan pekerjaanmu.

<!-- S59 -->
Ini pun ada namanya.
Thrashing.

<!-- S60 -->
Dan inilah yang membingungkan,
karena prosesornya
bisa tampak sama sekali tidak sibuk.

<!-- S61 -->
Ia tidak bekerja.
Ia menunggu.

<!-- S62 -->
Kamu bisa memberi tugas yang menunggu
prioritas tertinggi di sistem
dan ia akan menunggu
persis sama lamanya.

<!-- S63 -->
Lalu ada versi
yang paling manusiawi dari ini.
Peristiwanya sampai.
Kernel sudah memilikinya.

<!-- S64 -->
Ia tergeletak di antrean
yang bertuliskan nama programmu.
Dan programmu
tidak mengambilnya.

<!-- S65 -->
Mungkin ia sedang menghitung sesuatu
di utas yang sama
yang seharusnya menangani
jendelanya sendiri.

<!-- S66 -->
Jadi tetikus berfungsi.
Papan ketik berfungsi.
Program lain berfungsi.

<!-- S67 -->
Dan jendela yang satu itu memudar
dan berkata tidak merespons.

<!-- S68 -->
Dan itu bukan diagnosis.
Windows menempelkan label itu
setelah kira-kira lima detik
tanpa ada yang mengambil pesannya.

<!-- S69 -->
Sistemnya hidup sepenuhnya.
Hanya aplikasinya
yang tidak datang ke pintu.

<!-- S70 -->
Komputer menerima klikmu
dan aplikasi menjawabnya
bukanlah peristiwa yang sama.

<!-- S70b -->
Ngomong-ngomong, kalau kamu penasaran
ke mana pertanyaan berikutnya membawa kita,
kamu bisa subscribe.

Itu sangat membantu channel ini.
<!-- S71 -->
Masih ada satu mata rantai,
dan justru itulah yang
tak pernah kita pikirkan.
Sejauh ini belum ada yang menaruh
apa pun di layarmu.

<!-- S72 -->
Aplikasi mengubah keadaannya.
Sesuatu harus menyusun frame berikutnya.
Kartu grafis harus menggambarnya.
Layar harus menampilkannya.

<!-- S73 -->
Di layar biasa
gambar baru muncul
kira-kira setiap enam belas milidetik.

<!-- S73b -->
Jadi ada bedanya antara
komputer menangani klikmu
dan kamu melihatnya.

<!-- S74 -->
Dan di bawah semua itu
ada bagian
yang tak bisa diperbaiki rekayasa apa pun.
Sistem operasi tahu
bahwa tetikus bergerak.
Kenapa, ia sama sekali tidak tahu.

<!-- S75 -->
Mungkin kamu sedang membidik sesuatu
di sebuah permainan.
Atau menyunting dokumen.
Atau kamu menyenggol meja.

<!-- S76 -->
Bagi perangkat keras
itu peristiwa yang sama.
Sistem bisa memeringkat jenis kerja.
Menebak, ia tidak bisa.

<!-- S77 -->
Jadi ia berkompromi.
Cukup cepat untukmu,
hampir selalu,
tanpa membuat sisanya menunggu selamanya.

<!-- S78 -->
Yang membawa kita kembali
ke layar mati itu.
Klikmu tak pernah satu peristiwa saja.

<!-- S79 -->
Perangkat keras harus melaporkannya.
Kernel harus menyimpannya.
Antrean harus sampai ke programmu.

<!-- S80 -->
Programmu harus berjalan.
Antarmuka harus berubah.
Sesuatu harus menggambar gambar baru,
dan layar harus menunjukkannya padamu.

<!-- S81 -->
Setiap langkah itu
kecil dan cepat.

<!-- S82 -->
Perlambat salah satunya saja
dan kamu tidak akan merasakan
jendela yang lambat.

<!-- S83 -->
Rasanya komputermu mati.

<!-- S84 -->
Dan yang paling aneh dari semuanya
adalah betapa jarang
hal itu sungguh terjadi.

<!-- S85 -->
Kita berharap sebuah mesin
yang melakukan miliaran operasi
per detik
merespons sentakan tangan.

<!-- S86 -->
Dan hampir selalu ia menjawab.

<!-- S87 -->
Jadi lain kali kalau kamu mengeklik
dan tidak terjadi apa-apa,
beri dia sebentar.

<!-- S88 -->
Ia mendengarmu.

<!-- S89 -->
Ia cuma punya antrean,
dan kamu ada di dalamnya.
