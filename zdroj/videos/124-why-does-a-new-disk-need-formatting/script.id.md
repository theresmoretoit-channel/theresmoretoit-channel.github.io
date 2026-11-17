<!-- S01 -->
Kamu membeli disk yang benar-benar baru.
Satu terabyte, benar-benar kosong.
Sebelum bisa menyimpan satu file pun,
disk itu harus diformat dulu.

<!-- S02 -->
Jadi kamu memformatnya dengan ext4,
sistem berkas standar
di banyak komputer Linux.
Dengan pengaturan bawaan,
sebelum kamu menyimpan apa pun,
sekitar tujuh belas gigabyte sudah hilang.

<!-- S03 -->
Belum ada yang disimpan.
Tidak ada foto, tidak ada dokumen.
Jadi apa yang memakan semua ruang itu?

<!-- S04 -->
Lagi pula, kenapa disk perlu diformat
sejak awal?
Disk sudah bisa menyimpan data.
Disk bisa membaca dan menulis triliunan bit.

<!-- S05 -->
Kenapa komputer tidak langsung saja menulis
di mana pun ada tempat?

<!-- S06 -->
Karena menyimpan data
dan menemukannya lagi
adalah dua masalah yang sangat berbeda.

<!-- S07 -->
Bayangkan kantor yang membagikan
kertas kosong, bukan formulir.
Semuanya tercatat di suatu tempat...
dan tak ada yang bisa menemukan apa pun.

<!-- S08 -->
Disk tanpa sistem berkas
adalah tumpukan kertas itu.
Tapi gambaran yang lebih tepat
adalah sebuah buku catatan.

<!-- S09 -->
Bayangkan sebuah buku catatan
dengan seribu halaman,
dan beberapa aturan cara memakainya.

<!-- S10 -->
Pertama, setiap halaman punya nomor.
Sekarang setiap tempat di buku itu
punya alamat.
Halaman empat ratus dua belas
berarti tepat satu tempat.

<!-- S11 -->
Kedua, beberapa halaman pertama
adalah daftar isi.
Setiap entri berisi nama,
dan halaman tempatnya berada.
Panekuk: halaman dua belas.

<!-- S12 -->
Ketiga, di bagian paling belakang,
ada daftar halaman
yang masih kosong.

<!-- S13 -->
Sekarang tambahkan resep.
Kamu cek daftar di belakang untuk halaman kosong.
Kamu tulis resepnya di sana.
Kamu tambahkan satu baris di daftar isi.
Lalu kamu coret halaman itu
dari daftar halaman kosong.

<!-- S14 -->
Satu resep, tiga tempat.
Dan ketiganya harus cocok.

<!-- S15 -->
Lalu resep panekuknya bertambah panjang.
Halaman dua belas sudah penuh,
dan halaman tiga belas sudah terpakai.
Jadi resepnya berlanjut di halaman delapan puluh tujuh,
dan daftar isi harus mencatatnya.

<!-- S16 -->
Dan ini masalahnya.
Kalau kamu mau tempat untuk seribu entri
di daftar isi,
kamu harus menyisihkan halaman-halaman itu
sebelum menulis satu resep pun.

<!-- S17 -->
Itu analoginya.
Sekarang, ini yang sebenarnya ada di disk.

<!-- S18 -->
Disk tidak tahu soal file,
folder, atau nama.
Yang ditawarkannya hanya deretan panjang
slot bernomor, yang disebut sektor.

<!-- S19 -->
Di hard disk,
data tersimpan di piringan yang berputar.
SSD menyimpannya di memori flash.
Apa pun jenisnya, komputer hanya meminta
sebuah sektor berdasarkan nomornya,
dan disk sendiri yang mencari letaknya.

<!-- S20 -->
Sektor itu kecil.
Biasanya 512 byte,
atau 4.096
di disk yang lebih baru.

<!-- S21 -->
Sistem berkas biasanya bekerja
dengan potongan lebih besar, yang disebut blok.
Di ext4, satu blok berukuran empat kilobyte,
sebesar delapan sektor model lama.

<!-- S22 -->
Blok-blok bernomor itu
adalah halaman buku catatannya.
Yang masih dibutuhkan sistem berkas
adalah dua bagian lainnya:
daftar isi,
dan daftar tempat yang masih kosong.

<!-- S23 -->
Itulah yang dibuat saat memformat.
Dan ke situlah
tujuh belas gigabyte tadi pergi.

<!-- S24 -->
Ext4 menyisihkan satu catatan
untuk setiap file dan folder
yang bisa ditampung disk sekaligus.
Setiap catatan berukuran
256 byte.
Namanya inode.

<!-- S25 -->
Suatu hari, setiap inode akan mencatat
seberapa besar sebuah file,
kapan file itu diubah,
siapa yang boleh membukanya,
dan blok mana yang menyimpan isinya.

<!-- S26 -->
Di disk satu terabyte,
ext4 menyiapkan sekitar
enam puluh satu juta inode.
Semuanya kosong, semuanya menunggu.
Itu hampir enam belas gigabyte
catatan kosong.

<!-- S27 -->
Kenapa enam puluh satu juta?
Ext4 membuat tebakan sederhana:
satu inode untuk setiap enam belas kilobyte
ruang di disk.
Di komputer biasa,
sebagian besar catatan itu
tidak akan pernah terpakai.

<!-- S28 -->
Sekitar satu gigabyte lagi
dipakai untuk jurnal,
yang nanti akan kita bahas lagi.
Sisanya pembukuan lain,
termasuk peta dengan satu bit per blok,
yang menandai apakah blok itu terpakai atau kosong.

<!-- S29 -->
Jumlah itu juga tetap.
Habiskan semua catatan
dengan jutaan file kecil,
dan disk akan bilang sudah penuh...
padahal masih tersisa ruang beberapa gigabyte.

<!-- S30 -->
Jadi, mari kita lihat cara kerjanya.
Kita buat file bernama hello.txt.
Isinya cuma satu kata: hello.
Lima huruf. Lima byte.

<!-- S31 -->
Sistem berkas memilih inode yang kosong.
Misalnya nomor tiga belas.
Lalu ia mencari blok kosong di peta,
dan menandainya sebagai terpakai.

<!-- S32 -->
Ia menulis lima byte itu ke blok tersebut.
Lalu ia mengisi inode-nya:
panjang lima byte, dibuat barusan,
dan disimpan di satu blok itu.

<!-- S33 -->
Dan terakhir, di foldernya,
ia menambahkan satu baris:
nama hello.txt,
dan nomor tiga belas.

<!-- S34 -->
Perhatikan di mana namanya disimpan.
Bukan di file.
Bukan di inode.
Nama itu tinggal di folder,
yang sebenarnya cuma daftar
nama dan nomor.

<!-- S35 -->
Dan folder pun cuma sebuah file.
Kebetulan isinya
adalah daftar itu.

<!-- S36 -->
Itu juga sebabnya memindahkan file
ke folder lain di sistem berkas yang sama
terjadi seketika, sebesar apa pun filenya.
Satu folder kehilangan satu baris,
folder lainnya mendapat satu,
dan biasanya, isi filenya
sama sekali tidak berpindah.

<!-- S37 -->
Lima byte teks...
dan di disk, file itu memakan
4.096.
Blok adalah potongan terkecil
yang dibagikan sistem berkas,
jadi file sekecil apa pun memakan satu blok penuh.

<!-- S38 -->
Saat file sudah tak muat di bloknya,
sistem berkas mencari blok kosong lain.
Mungkin persis di sebelahnya.
Mungkin di tempat yang sama sekali lain.
Dan inode mencatat keduanya.

<!-- S39 -->
Lama-lama, file besar bisa berakhir
terpecah-pecah di seluruh disk.
Hard disk harus melompat di antara potongan itu.
SSD bisa menanganinya jauh lebih baik.

<!-- S40 -->
Program yang menyimpan file itu
tidak tahu apa-apa soal ini.
Ia hanya bilang "simpan hello.txt",
dan semua sisanya terjadi di balik layar.

<!-- S41 -->
Sekarang hapus file itu.
Namanya dihapus dari folder.
Inode-nya ditandai kosong.
Bloknya kembali ke daftar blok kosong.

<!-- S42 -->
Di hard disk tradisional,
lima byte itu sendiri tetap di tempatnya.
Tak ada yang menyentuhnya.
Kelimanya tetap ada sampai sesuatu yang baru
ditulis di atasnya.

<!-- S43 -->
Itu sebabnya file yang terhapus
kadang bisa dipulihkan.
Menghapus biasanya tidak melenyapkan
isinya.
Hanya menandai ruangnya sebagai tersedia.

<!-- S44 -->
Di SSD, hal ini kurang pasti.
Sistem berkas bisa memberi tahu disk
bahwa blok-blok itu tidak dibutuhkan lagi,
dan disk bisa membuang isinya.
Setelah itu, peluang mengembalikan file
jauh lebih kecil.

<!-- S45 -->
Jadi sistem berkas sebenarnya seorang juru buku.
Membuat satu file ini
berarti memperbarui tiga hal:
folder, inode,
dan peta blok kosong.

<!-- S46 -->
Sekarang putuskan listriknya
di tengah penyimpanan file.

<!-- S47 -->
Mungkin bloknya sudah ditandai terpakai,
tapi belum ada inode yang menunjuk ke sana.
Ruang itu hilang begitu saja.
Menyebalkan, tapi tidak berbahaya.

<!-- S48 -->
Atau mungkin inode menunjuk ke blok
yang menurut peta masih kosong.
File berikutnya bisa ditulis
tepat di atasnya.
Dan file pertama rusak diam-diam.

<!-- S49 -->
Karena itulah ext4 menyimpan jurnal.
Sebelum mengubah pembukuannya,
ia menulis dulu apa yang akan dilakukannya.
Setelah crash, ia hanya mengulang perubahan
yang sudah selesai ia tulis,
dan sudah ditandai lengkap.
Yang belum selesai diabaikan.

<!-- S50 -->
Lalu ada masalah yang lebih senyap.
Kadang disk mengubah satu bit
dan tidak memberi tahu siapa pun.

<!-- S51 -->
Ext4 melindungi catatannya sendiri
dengan checksum,
jadi ia bisa mendeteksi kerusakan di sana.
Tapi isi file-filemu?
Yang itu, ia percayai begitu saja.

<!-- S52 -->
Sebagian sistem berkas memeriksa keduanya.
Dan sebagian menyimpan salinan kedua,
jadi kalau satu salinan rusak,
mereka bisa memperbaikinya dari salinan lain.
Mendeteksi masalah dan memperbaikinya
bukan hal yang sama.

<!-- S53 -->
Jadi setiap sistem berkas melakukan tugas yang sama:
blok bernomor, daftar nama,
dan peta tempat yang masih kosong.

<!-- S54 -->
Tapi pilihannya berbeda.
Ext4 menyiapkan enam puluh satu juta catatan
sebelum kamu menyimpan apa pun.
NTFS, di Windows, menyimpan catatannya
dalam satu tabel besar yang terus bertambah seiring pemakaian.

<!-- S55 -->
Sementara Btrfs tidak menyiapkan
tabel inode yang tetap sejak awal.
Ia membuatnya saat file berdatangan.
Dan biasanya, ia tidak menimpa
data di tempatnya.
Ia menulis salinan baru,
dan baru setelah itu melepas yang lama.

<!-- S56 -->
Secara bawaan, ia juga membuat checksum untuk file-filemu,
jadi ia bisa tahu kalau file itu rusak.

<!-- S57 -->
Dan karena salinan lamanya
tidak ditimpa,
sebuah snapshot bisa mempertahankannya.
Itu mengubah jawaban
atas hampir setiap pertanyaan di video ini:
apa akibat crash,
apa arti menghapus,
dan bahkan apa itu salinan.

<!-- S58 -->
Dari situlah video berikutnya dimulai.

<!-- S59 -->
Jadi, ini pertanyaan untukmu.
Haruskah sistem berkas cuma menyimpan file-filemu,
atau juga melindunginya?
Beri tahu aku di kolom komentar.
