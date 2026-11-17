<!-- S01 -->
Kamu mencoba menghapus sebuah berkas.
Komputer bilang berkas itu terbuka
di program lain.
Tapi tidak bilang program mana.

<!-- S02 -->
Pesan itu adalah ujung yang terlihat
dari pertanyaan yang jauh lebih aneh.
Apa sebenarnya artinya
membuka sebuah berkas?

<!-- S03 -->
Sebab di komputer lain
berkas yang sama, dibuka dengan cara sama,
terhapus tanpa keluhan sedikit pun.

<!-- S04 -->
Berkas yang sama.
Tindakan yang sama.
Dua jawaban yang sama sekali berbeda.

<!-- S05 -->
Mulai dari bagian
yang membuat semua orang jengkel.
Program yang mana?

<!-- S06 -->
Windows tahu.
Ia punya objek kernel
untuk berkas yang terbuka itu
dan tahu proses mana pemiliknya.
Ia bisa saja menyebut namanya.

<!-- S07 -->
Jadi kamu menutup program asal-asalan.
Kamu buka Pengelola Tugas.
Kamu menatap daftar proses
dan hampir tak mengenali satu pun.

<!-- S08 -->
Dan bertahun-tahun
jawabannya memang
mengunduh alat terpisah.
Unlocker keluar tahun 2005,
dan di Windows XP itulah jawabannya.

<!-- S09 -->
Lalu Windows 7 membawa
Monitor Sumber Daya.
Tab CPU.
Daftar bernama Associated Handles.

<!-- S10 -->
Ketik nama berkasnya.
Ia memberimu programnya
dan ID prosesnya.
Tidak ada yang perlu dipasang.
Sudah ada di sana sejak 2009.

<!-- S10b -->
Tapi alat terpisah itu melakukan
lebih dari sekadar memberitahu.
Mereka bisa menutup handle-nya
dan melepaskan berkas itu.

<!-- S11 -->
Yang membawa kita kembali
ke pertanyaan tadi.
Apa yang didapat program itu
ketika membuka berkasnya?

<!-- S12 -->
Katakanlah pemutar video membuka
berkas bernama movie.mp4.
Di Windows, membuka berkas
berarti mengisi dua hal.

<!-- S13 -->
Yang pertama sudah jelas.
Aku mau apa dengan berkas ini?
Membacanya. Menulis ke dalamnya.

<!-- S14 -->
Yang kedua itulah yang menarik.
Apa yang boleh dilakukan orang lain
selama aku membukanya?

<!-- S15 -->
Itu pengaturan sungguhan.
Kamu menentukan apa yang boleh
dilakukan program lain selama kamu memegangnya.

<!-- S16 -->
Mereka boleh membacanya.
Mereka juga boleh menulis ke dalamnya.
Mereka boleh menghapus atau mengganti namanya.

<!-- S16b -->
Atau tidak boleh apa pun.
Tidak ada yang menyentuhnya
selama aku memakainya.

<!-- S17 -->
Flag yang mengizinkan penghapusan
bernama FILE_SHARE_DELETE.
Dan dokumentasi Microsoft
menambahkan satu baris di bawahnya.

<!-- S18 -->
Hak akses hapus mencakup
menghapus dan mengganti nama sekaligus.

<!-- S19 -->
Jadi program yang menolak
berbagi untuk penghapusan
juga sudah mengunci penggantian nama.

<!-- S20 -->
Dan kalau program yang membuka berkas
tidak memberikannya,
tidak ada yang lain bisa mengambilnya.

<!-- S21 -->
Itu sebabnya kesalahannya
tidak disebut berkas sedang dipakai.
Namanya sharing violation.

<!-- S22 -->
Jawabannya sejak awal ada
di dalam nama
kesalahan itu sendiri.

<!-- S23 -->
Sekarang hal yang sama
di mesin Linux.
Pemutar membuka videonya.

<!-- S24 -->
Dan kamu mengetik
rm movie.mp4.

<!-- S24b -->
Berhasil.
Videonya terus berjalan.

<!-- S25 -->
Jadi apa yang didapat program itu,
kalau bukan kendali atas berkas itu?

<!-- S26 -->
Inilah seluruh gagasan
video ini.
Nama bukanlah berkas.

<!-- S27 -->
movie.mp4 adalah satu baris
di dalam sebuah direktori.
Baris itu menunjuk ke sebuah objek
yang menyimpan data sebenarnya.

<!-- S28 -->
Ketika program membuka berkasnya,
yang ia dapat adalah referensi
ke objek itu.
Bukan ke barisnya.

<!-- S29 -->
Jadi menghapus berkas
menghapus barisnya.
Objeknya tidak tersentuh.

<!-- S30 -->
Halaman manual mengatakannya
dalam satu kalimat.
Berkas akan tetap ada
sampai deskriptor berkas terakhir
yang menunjuk padanya ditutup.

<!-- S31 -->
Kedengarannya abstrak
sampai kamu melihatnya terjadi.
Jadi aku membuat berkas log
sebesar lima ratus megabita
dan membiarkan satu proses tetap membukanya.

<!-- S31b -->
Lalu aku menghapusnya.

<!-- S32 -->
Daftar isi direktorinya
tidak menampilkan apa pun.
Alat yang mengukur
ukuran folder bilang nol.

<!-- S33 -->
Dan alat yang mengukur
ruang kosong pada disk
bilang lima ratus megabita
masih hilang.

<!-- S33b -->
Folder kosong.
Setengah gigabita lenyap.

<!-- S34 -->
Ini cukup sering terjadi
sampai ada perintah khusus
hanya untuk mencari berkas seperti ini.
Terhapus, tak terlihat, masih di disk.

<!-- S35 -->
Dan ruangnya kembali
pada saat satu proses itu
melepaskan berkasnya.

<!-- S36 -->
Logika yang sama berlaku untuk penggantian nama.
Pindahkan berkasnya saat terbuka,
dan programnya tidak akan sadar.

<!-- S37 -->
Manualnya juga blak-blakan soal itu.
Deskriptor yang terbuka
untuk jalur lama tidak terpengaruh.

<!-- S37b -->
Ia tidak pernah memakai namanya.

<!-- S38 -->
Yang punya satu batas
yang layak diketahui.
Program yang sedang berjalan
tidak bisa ditimpa di tempatnya.

<!-- S38b -->
Linux menolak.
Text file busy.

<!-- S39 -->
Yang bisa kamu lakukan
adalah melepaskan namanya
dan menaruh berkas baru di sana.

<!-- S40 -->
Proses lama tetap berjalan
dari sebuah objek
yang tidak lagi punya nama.
Apa pun yang dimulai setelahnya dapat yang baru.

<!-- S41 -->
Itu lagi-lagi gagasan yang sama,
membuktikan dirinya sendiri.
Banyak hal bisa diganti
tanpa menyentuh objeknya di tempat.

<!-- S41b -->
Karena itulah Linux bisa memperbarui
program yang sedang berjalan.
Kamu hanya belum dapat versi barunya
sampai kamu memulai ulang program itu.

<!-- S42 -->
Jadi apakah Windows
memang rancangan yang lebih buruk?

<!-- S42b -->
Tidak.
Dan inilah bagian
yang hampir tak ada yang tahu.

<!-- S43 -->
Windows punya cara
untuk melakukan hal yang persis sama.

<!-- S43b -->
Di NTFS, Windows bisa meminta
penghapusan bergaya POSIX.

<!-- S44 -->
Microsoft menjelaskan
apa yang terjadi saat itu.
Namanya dihapus
dari ruang nama yang terlihat.

<!-- S45 -->
Dan aplikasi yang sudah terlanjur
membuka berkasnya tetap bisa memakainya,
meski nama
yang mereka pakai untuk membukanya sudah hilang.

<!-- S46 -->
Itu perilaku Unix.
Di NTFS.
Didokumentasikan oleh Microsoft.

<!-- S47 -->
Kedua sistem bisa melakukan keduanya.
Yang berbeda adalah setelan bawaannya.
Apa yang kamu dapat saat membuka berkas
tanpa memikirkannya sama sekali.

<!-- S48 -->
Di Windows kamu dapat sebuah kontrak.
Di Unix kamu dapat sebuah referensi
ke sebuah objek.

<!-- S49 -->
Yang terdengar seperti pertanyaan
untuk pemrogram,
sampai kamu pernah melihat
pesan yang satu ini.

<!-- S50 -->
Mulai ulang komputer
untuk menyelesaikan pemasangan pembaruan.

<!-- S51 -->
Misalkan Windows harus mengganti
pustaka yang tetap dibuka
oleh sebuah proses di bawah kontrak ketat.

<!-- S52 -->
Ia tidak bisa mengganti berkas itu
saat proses tersebut masih berjalan.
Jadi sesuatu harus melepaskannya.

<!-- S53 -->
Tutup aplikasinya.
Hentikan layanannya.
Atau serahkan seluruh pekerjaan
kepada Restart Manager.

<!-- S54 -->
Yang merupakan komponen sungguhan.
Ia mematikan semuanya satu per satu.
Aplikasi Windows,
lalu program konsol,

<!-- S55 -->
lalu layanan,
dan Windows Explorer terakhir.
Setelah itu ia menjalankannya lagi.

<!-- S56 -->
Dan ia ada karena satu alasan,
yang dikatakan Microsoft terang-terangan
di dalam dokumentasinya sendiri.

<!-- S57 -->
Alasan utama
pemasangan perangkat lunak
dan pembaruan memerlukan
mulai ulang sistem...

<!-- S58 -->
adalah karena sebagian berkas
yang diperbarui saat itu sedang dipakai
oleh aplikasi
atau layanan yang berjalan.

<!-- S59 -->
Terlalu rapi kalau berhenti di sini.
Aturan berbagi bukan satu-satunya alasan
komputer meminta untuk dimulai ulang.

<!-- S60 -->
Pembaruan kernel adalah soal lain.
Kernel tidak bisa diganti
saat dirinya sendiri sedang berjalan.

<!-- S61 -->
Linux punya masalah yang sama,
meski live patching
kadang bisa menghindari mulai ulang.

<!-- S62 -->
Jadi versi yang jujur
menjanjikan lebih sedikit
daripada versi yang memuaskan.

<!-- S63 -->
Cara Windows memperlakukan berkas
yang sedang dipakai membuat sebagian komponen
lebih sulit diganti saat sistem berjalan,
dan itu ikut berperan.

<!-- S64 -->
Sebab setiap pilihan rancangan
punya akibat di suatu tempat.

<!-- S65 -->
Windows membiarkan program
yang membuka berkas menentukan
apa yang boleh dilakukan orang lain.

<!-- S66 -->
Harganya adalah kadang
kamu tidak bisa menghapus berkasmu sendiri,
karena program lain
tidak mengizinkannya.

<!-- S67 -->
Unix memisahkan nama
dan objeknya,
sehingga banyak hal bisa diganti
saat sistem sedang berjalan.

<!-- S68 -->
Harganya adalah setengah gigabita
yang lenyap dari disk
dan tidak menjadi milik berkas mana pun.

<!-- S69 -->
Dan lihat bagaimana keduanya
masing-masing diselesaikan.
Di Windows, satu jalan keluarnya
adalah menutup program
yang memegang berkas itu.

<!-- S70 -->
Di Linux, satu cara
mendapatkan ruang itu kembali
adalah memulai ulang layanan
yang masih memegangnya.

<!-- S71 -->
Penyebabnya berbeda.
Kadang obatnya sama.

<!-- S71b -->
Omong-omong, kalau kamu ingin tahu
ke mana pertanyaan berikutnya membawa kita,
pertimbangkan untuk berlangganan.
Itu sangat membantu kanal ini.

<!-- S72 -->
Jadi. Pertanyaan dari awal tadi.
Apa artinya
membuka sebuah berkas?

<!-- S73 -->
Artinya kamu sedang memegang sesuatu.
Kedua sistem itu hanya menyerahkan
hal yang berbeda ke tanganmu.

<!-- S74 -->
Itu sebabnya pesan tadi
sebenarnya tidak pernah bilang
berkas ini tidak bisa dihapus.

<!-- S75 -->
Ia bilang program
yang membukanya
tidak mengizinkanmu.

<!-- S75b -->
Dan ia tahu program mana.
Hanya saja ia tidak menyebutnya.
