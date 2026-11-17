<!-- S01 -->
Kamu menekan play di tape kaset.
Lalu ini yang keluar dari speakernya.

<!-- S02 -->
Ini bukan musik.
Dan ini juga bukan soundtrack sebuah game.

<!-- S03 -->
Inilah game-nya.
Setiap decitan adalah bagian dari program,
dan komputer sedang mendengarkannya.

<!-- S04 -->
Tape kasetnya sama sekali tidak tahu.
Baginya, ia sedang memutar lagu.

<!-- S05 -->
Jadi, bagaimana lagu bisa jadi game?
Dan kenapa satu nada yang salah
bisa menyia-nyiakan lima menit menunggu?

<!-- S06 -->
Begini triknya,
pada satu mesin tertentu:
ZX Spectrum,
komputer rumahan Inggris dari tahun 1982.

<!-- S07 -->
Ia memakai dua jenis pulsa.
Sepasang pulsa pendek berarti nol.

<!-- S08 -->
Angka satu adalah pasangan yang sama,
dengan tiap pulsa dua kali lebih panjang,
jadi nadanya satu oktaf lebih rendah.

<!-- S09 -->
Kirim sekitar seribu empat ratus bit
setiap detik,
dan jadilah bunyi yang barusan kamu dengar.

<!-- S09b -->
Ini juga berarti program penuh angka nol
dimuat lebih cepat dari yang penuh angka satu.
Setiap angka satu dikirim dua kali lebih lama.

<!-- S10 -->
Nah, kalau kamu besar di Amerika,
mungkin kamu tak pernah mendengarnya sama sekali.

<!-- S11 -->
Aneh juga,
karena idenya sendiri berasal dari Amerika.

<!-- S12 -->
Tahun 1975, dalam pertemuan di Kansas City,
para penghobi komputer menyepakati cara
menyimpan data sebagai suara
di kaset audio biasa.

<!-- S12b -->
Angka satu adalah delapan siklus cepat
nada tinggi,
angka nol berupa empat siklus lambat dari nada rendah.
Tiga ratus bit per detik.

<!-- S13 -->
Mesin-mesin awal seperti Apple II
dan TRS-80
menyimpan program mereka
di tape recorder biasa.

<!-- S14 -->
Tapi komputer rumahan di Amerika
dengan cepat beralih ke cara lain.

<!-- S15 -->
Tahun 1983, sebuah majalah melaporkan survei:
sembilan dari sepuluh pemilik baru Commodore 64
membeli disk drive
sekalian bersama komputernya.

<!-- S16 -->
Di Inggris, ceritanya justru sebaliknya.

<!-- S17 -->
Harga Spectrum seratus
dua puluh lima pound,
dan tidak dilengkapi penyimpanan sama sekali.
Kamu pakai tape kaset apa saja
yang sudah kamu punya.

<!-- S18 -->
Jadi bagi jutaan anak di seluruh Eropa,
bunyi ini adalah suara
game yang akan segera dimulai.

<!-- S18b -->
Setelah cukup sering memuat game,
kamu bahkan bisa menebak game apa itu
hanya dari decitannya.

<!-- S19 -->
Jadi, mari kita ikuti satu game
dari pita sampai masuk ke komputer.

<!-- S20 -->
Kamu ketik LOAD, tekan enter,
lalu tekan play.

<!-- S21 -->
Pertama datang dengung yang stabil,
delapan ratus siklus per detik,
selama sekitar lima detik.

<!-- S22 -->
Dengung ini sama sekali tidak membawa data.
Gunanya supaya komputer
bisa menemukan sinyalnya
dan mengunci iramanya.

<!-- S23 -->
Lalu dua pulsa cepat, sinyal sinkronisasi.
Artinya: mulai dari sini, ini data.

<!-- S24 -->
Yang pertama tiba
adalah header pendek.
Sembilan belas byte:
nama sampai sepuluh huruf,
jenis file-nya,
dan berapa panjangnya nanti.

<!-- S25 -->
Lalu dengung kedua yang lebih pendek,
kali ini dua detik,
lalu game-nya sendiri.

<!-- S26 -->
Setiap byte terdiri dari delapan nada itu,
satu demi satu,
tanpa jeda sama sekali antar-byte.

<!-- S27 -->
Dan komputer tidak mendengar nada.
Ia mengukur jeda waktu antara satu tepi
sinyal dan tepi berikutnya.

<!-- S28 -->
Pasangan pendek adalah nol.
Pasangan panjang adalah satu.

<!-- S28a -->
Itulah seluruh dekodernya.

<!-- S28b -->
Dan bunyi di awal video ini
bukan efek suara.
Kami membuatnya persis dengan aturan ini,
dan di dalamnya ada program Spectrum asli.

<!-- S28c -->
Kami akan memutar semuanya di akhir video.
Rekam, dan Spectrum akan memuatnya.

<!-- S29 -->
Kebanyakan game menampilkan gambar dulu,
dan gambar itu dimuat dengan urutan aneh.

<!-- S30 -->
Garis tipis muncul, berjarak delapan baris,
lalu terisi, baris demi baris,
sepertiga layar setiap kalinya.
Dan warnanya datang paling akhir,
menutupi seluruh gambar dari atas ke bawah.

<!-- S31 -->
Gambar itu saja
butuh sekitar empat puluh detik.
Seluruh game, sekitar lima menit.

<!-- S32 -->
Dan di akhir setiap blok
datang satu byte lagi.

<!-- S33 -->
Saat menyimpan, Spectrum memproses
setiap byte di blok itu
dengan aturan sederhana bernama XOR,
dan merekam hasilnya sebagai satu byte lagi.

<!-- S34 -->
Saat memuat, ia mengulang perhitungannya.
Kalau hasilnya cocok,
blok itu tiba dengan utuh.

<!-- S35 -->
Kalau tidak, Spectrum bilang begini.

<!-- S36 -->
Lima menit menunggu,
dan satu byte memutuskan
semuanya sia-sia.
Putar balik pitanya, dan mulai lagi.

<!-- S37 -->
Anehnya, header yang rusak
tidak memunculkan error sama sekali.
Spectrum cukup mengabaikannya,
dan terus mendengarkan header berikutnya.

<!-- S38 -->
Komputer lain memakai pendekatan berbeda.

<!-- S39 -->
Commodore 64 merekam
setiap blok dua kali,
jadi bagian yang rusak di satu salinan
bisa diselamatkan dari salinan lainnya.

<!-- S40 -->
Lebih aman, tapi lambat.
Dengan rutin bawaan Commodore,
program berukuran empat puluh kilobyte
butuh sekitar dua belas setengah menit.

<!-- S41 -->
Jadi penerbit game menulis
loader mereka sendiri yang lebih cepat,
sebagian sampai sekitar sepuluh kali lipat.

<!-- S42 -->
Lalu ada tape kasetnya sendiri.

<!-- S43 -->
Terlalu pelan,
dan tepinya tenggelam dalam desis.
Terlalu keras,
dan tepinya saling melebur.

<!-- S44 -->
Pita yang berputar sedikit terlalu cepat
atau lambat meregangkan setiap pulsa,
padahal komputer sedang mengukur waktu.

<!-- S45 -->
Yang paling parah adalah azimut,
yaitu sudut head pita.
Pita yang direkam di satu mesin
belum tentu pas di mesin lain.

<!-- S46 -->
Jadi orang menusukkan obeng kecil
ke lubang di samping head,
lalu memutarnya sedikit demi sedikit,
sambil mendengarkan.

<!-- S47 -->
Kelihatannya seperti takhayul.
Padahal itu penyetelan sinyal.

<!-- S48 -->
Tapi perhatikan apa yang tak pernah
perlu dilakukan tape kaset.

<!-- S49 -->
Ia tak pernah memahami satu bit pun.
Ia merekam suara,
lalu memutarnya kembali.

<!-- S50 -->
Artinya, sebuah program
sebenarnya tidak butuh kaset.
Apa pun yang bisa membawa suara
bisa membawa software.

<!-- S50b -->
Itu juga berarti menyalin game
semudah menyalin album.
Dua tape deck dan sebuah kabel.

<!-- S51 -->
Atari memakai kedua trek stereo.
Program di satu trek,
dan suara orang di trek lainnya,
yang berbicara padamu lewat TV
selama game dimuat.

<!-- S52 -->
Di Yugoslavia, sebuah acara di Radio Beograd
menyiarkan program komputer lewat udara.

<!-- S53 -->
Pendengar merekamnya di pita,
sekitar seratus lima puluh program
antara 1983 dan 1986.

<!-- S54 -->
Di Cekoslowakia, lewat televisi.
Sebuah program diputar sebagai suara
saat kredit penutup ditampilkan.

<!-- S55 -->
Dan pada 1983, penyanyi Pete Shelley
menyembunyikan program Spectrum
di akhir sebuah album piringan hitam.

<!-- S56 -->
Salin ke pita, muat,
dan liriknya muncul di layar
seiring dengan lagunya.

<!-- S57 -->
Tapi ada kendalanya.

<!-- S58 -->
Radio bisa membawa suara itu
ke setiap komputer di negeri itu.
Hanya komputer yang tepat yang memahaminya.

<!-- S59 -->
Putar game Spectrum ke Commodore,
dan yang didengar Commodore hanya derau.
Bit-bit itu hanya berarti
bagi mesin yang mengenal formatnya.

<!-- S60 -->
Jadi radio Belanda mencoba mengatasinya.
Tahun 1982, mereka menciptakan BASICODE:
satu format suara,
dengan program penerjemah kecil
untuk setiap jenis komputer.

<!-- S61 -->
Dan masalah itu tak pernah hilang.
Sebuah file hanya berguna
kalau masih ada yang bisa membacanya.

<!-- S62 -->
Kaset tentu saja kalah.
Disket lebih cepat,
lalu hard disk, lalu flash.

<!-- S63 -->
Hanya saja, pita sebenarnya tak pernah pergi.
Pusat data masih menyimpan
arsip mereka di pita magnetik.

<!-- S64 -->
Satu kartrid LTO-9 modern
menampung delapan belas terabyte.

<!-- S65 -->
Kalau dihitung dengan kecepatan Spectrum,
kapasitas itu akan memenuhi kira-kira
dua puluh sembilan juta kaset,
dan butuh lebih dari tiga ribu
tahun untuk dimuat.

<!-- S66 -->
Tapi idenya tetap sama.
Pola di atas pita yang bergerak,
yang diubah kembali menjadi angka
saat kamu membutuhkannya.

<!-- S67 -->
Jadi lain kali kamu mendengar decitan itu,
ingat apa itu sebenarnya.
Bukan derau.
Sebuah program, yang berkelana sebagai suara.

<!-- S68 -->
Dan di suatu tempat pada tahun 1985,
seorang anak duduk di depan televisi,
menunggu bunyinya berhenti.
Karena begitu bunyinya berhenti,
game-nya dimulai.

<!-- S69 -->
Jadi, ini pertanyaan untukmu.
Kalau kamu pernah memuat game dari kaset,
apa yang paling kamu ingat darinya?
Tulis di kolom komentar.

<!-- S70 -->
Dan seperti yang dijanjikan, ini programnya.
Sama seperti televisi Cekoslowakia,
kami memutarnya saat kredit penutup ditampilkan.
