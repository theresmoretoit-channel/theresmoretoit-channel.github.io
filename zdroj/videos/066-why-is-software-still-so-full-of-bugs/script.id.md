<!-- S01 -->
Setiap beberapa hari, satu bug serius lagi
muncul di berita.
Bug yang membuat seseorang bisa melewati login.
Bug yang membocorkan data pribadi.
Bug yang menyerahkan komputer Anda ke penyerang.

<!-- S02 -->
Kadang itu Windows. Kadang Linux.
Peramban, basis data, layanan cloud...
atau sebuah pustaka kecil
yang diandalkan jutaan pengembang.

<!-- S03 -->
Dan reaksinya hampir selalu sama.
Bagaimana para pemrogram bisa melewatkan ini?

<!-- S04 -->
Mereka ini profesional.
Mereka punya tinjauan kode, uji otomatis,
audit keamanan, fuzzing...
dan bug tetap saja terus bermunculan.

<!-- S05 -->
Jadi apakah mungkin
menulis perangkat lunak rumit tanpa bug?

<!-- S06 -->
Mari mulai dengan sebuah angka.
Bayangkan sebuah program dengan seratus pengaturan saja,
masing-masing menyala atau mati.

<!-- S07 -->
Seratus keputusan ya-atau-tidak yang sederhana.
Berapa banyak kombinasinya?

<!-- S08 -->
Dua pangkat seratus.
Itu kira-kira sejuta triliun triliun.

<!-- S09 -->
Sekarang bayangkan Anda bisa menguji
satu miliar kombinasi setiap detik.
Dan Anda mulai sejak Big Bang.

<!-- S10 -->
Sampai hari ini, Anda baru menguji
kira-kira satu kombinasi dari tiga ribu.

<!-- S11 -->
Dan seratus sakelar itu bukan apa-apa.
Program sungguhan punya jutaan sakelar.
Jadi "tinggal uji semuanya"
bukan mahal. Itu mustahil.

<!-- S12 -->
Dan sakelar-sakelar itu tidak aneh.
Ambil salah satu hal paling sederhana
yang pernah dilakukan sebuah program.
Pengguna meminta akunnya lewat nomornya.
Kita menemukannya di basis data.
Kita mengirimkannya kembali.

<!-- S13 -->
Tapi bagaimana kalau penggunanya tidak ada?
Bagaimana kalau seseorang mengirim teks, bukan angka?
Atau angka negatif? Atau angka yang sangat besar?

<!-- S14 -->
Bagaimana kalau orang ini tidak boleh melihatnya?
Bagaimana kalau seseorang menghapus akun itu
tepat saat kita sedang memuatnya?
Bagaimana kalau permintaan yang sama datang dua kali?

<!-- S15 -->
Setiap pertanyaan ini sederhana.
Masalahnya adalah bagaimana semuanya bergabung.
Masing-masing adalah satu sakelar lagi.

<!-- S15b -->
Ngomong-ngomong, kalau Anda suka
video seperti ini, Anda bisa subscribe.

Itu sangat membantu channel ini.

<!-- S16 -->
Dan komputer tidak akan membereskannya untuk kita.
Ia melakukan persis seperti yang kita perintahkan.
Bukan yang kita maksudkan.

<!-- S17 -->
Itu sebabnya kita menciptakan bahasa pemrograman.
Bahasa itu membuat kita bisa menggambarkan hal rumit
tanpa memikirkan setiap detail.

<!-- S18 -->
Tapi sebagian dari bahasa itu mengurus lebih sedikit
daripada yang Anda harapkan.
Ambil C. Ia cepat, ia sederhana,
dan memberi Anda kendali sangat besar atas memori.

<!-- S19 -->
Jadi Anda bisa menulis ini.
Kita sisakan ruang untuk enam belas karakter.
Lalu kita bilang: salin masukan ke sini.

<!-- S20 -->
Bagaimana kalau masukannya
sepanjang lima ratus karakter?
C tidak akan bertanya.
Ia terus saja menulis melewati ujungnya.

<!-- S21 -->
Dan apa yang ada tepat setelah enam belas karakter itu?
Sering kali, sesuatu yang sangat penting.

<!-- S22 -->
Saat sebuah program memanggil fungsi,
ia mencatat ke mana harus kembali
begitu fungsinya selesai.
Sebuah alamat kembali.
Dalam tata letak klasik, ia terletak
tak jauh setelah ujung buffer kita.

<!-- S23 -->
Jadi penyerang mengirim masukan
yang panjangnya persis pas.
Pertama, instruksinya sendiri.
Lalu, di bagian paling akhir, alamat kembali baru...
yang menunjuk balik ke instruksi-instruksi itu.

<!-- S24 -->
Fungsinya selesai.
Prosesor mencari ke mana harus kembali...
dan melompat langsung ke kode penyerang.

<!-- S25 -->
Kini ia menjalankan program milik mereka,
dengan semua hak akses yang dimiliki program Anda.
Itulah arti "menjalankan kode sembarang".

<!-- S26 -->
Dan prosesor tidak melakukan kesalahan apa pun.
Ia mengikuti instruksi.

<!-- S27 -->
Pada 1988, kesalahan yang persis seperti ini
membuat worm Morris menyebar
ke seluruh internet masa awal.
Dan trik yang sama sudah dipakai
dalam serangan sejak saat itu.

<!-- S28 -->
Jadi bahasa yang lebih baru menyerahkan sebagian pekerjaan
kepada kompiler.
Rust, misalnya, menolak membangun
banyak program yang bisa menggunakan memori secara tidak aman.

<!-- S29 -->
Si pemrogram berkata:
tapi aku tahu persis apa yang kulakukan!
Dan kompiler menjawab:
begitu kata semua orang.

<!-- S30 -->
Dan wajar untuk curiga.
Microsoft dan tim Chrome dari Google
sama-sama melaporkan
bahwa sekitar tujuh puluh persen
bug keamanan yang mereka teliti
berasal dari masalah keamanan memori.

<!-- S31 -->
Tapi sebuah program bisa sepenuhnya aman memori
dan tetap sepenuhnya salah.

<!-- S32 -->
Bayangkan seorang pengguna masuk.
Kata sandinya diperiksa dengan benar.
Tak ada yang macet. Tak ada memori yang rusak.

<!-- S33 -->
Lalu program itu menampilkan kepadanya
data milik orang lain.
Karena pemeriksaan izin
ditulis sedikit keliru.

<!-- S34 -->
Tak ada bahasa yang bisa menangkap itu sendiri.
Bahasa tidak tahu
apa yang seharusnya dilakukan program.
Hanya kita yang tahu itu.

<!-- S35 -->
Jadi kembali ke pengujian.
Sebuah uji bisa memberi tahu Anda:
untuk masukan ini, aku dapat hasil ini.

<!-- S36 -->
Ia tak bisa memberi tahu Anda:
program ini benar untuk setiap masukan.
Dan kita sudah lihat
kenapa kita tak bisa mencoba semuanya.

<!-- S37 -->
Pada 1970, ilmuwan komputer
Edsger Dijkstra merangkumnya dalam satu kalimat.
Pengujian bisa menunjukkan adanya bug,
tapi tak pernah ketiadaannya.

<!-- S38 -->
Baik. Jadi alih-alih menguji,
kenapa tak menulis sebuah program
yang memeriksa program lain
dan membuktikan bahwa mereka benar?
Beri ia kode apa saja, dan ia akan memberi tahu
apakah kode itu melakukan yang seharusnya.

<!-- S39 -->
Pertanyaan itu sudah terjawab
bahkan sebelum komputer sungguhan pertama dibangun.
Pada 1936, Alan Turing membuktikan
bahwa program seperti itu tidak mungkin ada.

<!-- S40 -->
Bukan karena belum ada yang membangunnya.
Tapi karena ia sama sekali tidak bisa ada.

<!-- S41 -->
Ia menunjukkan bahwa tak ada program yang bisa memutuskan,
untuk setiap program lain,
apakah program itu akan pernah berhenti.

<!-- S42 -->
Dan pada 1953, Henry Rice melangkah lebih jauh.
Hal yang sama berlaku untuk setiap pertanyaan tak sepele
tentang apa yang sebenarnya dilakukan sebuah program.

<!-- S43 -->
Apakah ia aman? Apakah ia membocorkan data?
Apakah ia memberi jawaban yang benar?
Tak ada metode umum
yang menuntaskan itu untuk setiap program.

<!-- S44 -->
Jadi apakah perangkat lunak bebas bug itu mustahil?
Tidak sepenuhnya.
Untuk satu program tertentu,
kadang Anda bisa membuktikan bahwa ia benar,
dengan upaya yang sangat besar.

<!-- S45 -->
Pada 2009, sebuah tim di Australia membuktikan
bahwa sebuah kernel sistem operasi kecil,
bernama seL4,
melakukan persis seperti yang dikatakan spesifikasinya.

<!-- S46 -->
Ia berukuran kurang dari sepuluh ribu baris kode.
Membangun kernel itu memakan
sekitar dua tahun-orang.
Membuktikan kebenarannya memakan sekitar dua puluh.
Peramban web modern
punya puluhan juta baris.

<!-- S47 -->
Dan bahkan pembuktian itu pun ada batasnya.
Ia menunjukkan program cocok dengan spesifikasinya.
Ia tak bisa menunjukkan bahwa spesifikasinya
adalah yang sebenarnya kita inginkan.

<!-- S48 -->
Dan spesifikasi itu ditulis oleh manusia.
Jadi pertanyaannya kembali kepada kita.

<!-- S49 -->
Dan ini bukan cuma kode kita sendiri.
Seorang pemrogram hari ini bertumpu pada kerangka kerja,
pustaka, dan ratusan dependensi.
Setiap lapisan menghemat kerja kita dalam jumlah besar.
Tapi setiap lapisan adalah sesuatu
yang harus kita pahami...
atau setidaknya kita percayai.

<!-- S50 -->
Artinya, Anda tak perlu menulis bug
untuk punya satu di perangkat lunak Anda.
Anda cukup memasangnya.

<!-- S51 -->
Lalu tambahkan tekanannya.
Tak ada yang mau produk sempurna dalam sepuluh tahun.
Mereka mau yang berfungsi bulan depan.
Dan pembobolan yang tak pernah terjadi
sangat sulit ditampilkan dalam presentasi.

<!-- S52 -->
Dan inilah bagian yang paling aneh.
Alat kita terus membaik.
Bahasa yang lebih aman, fuzzing, bug bounty...

<!-- S53 -->
Namun jumlah kerentanan yang diketahui
terus bertambah.
Hanya pada 2024, sekitar empat puluh ribu
mendapat nomor resmi.

<!-- S54 -->
Sebagian karena kita juga menulis
jauh lebih banyak perangkat lunak dari sebelumnya.
Ini seperti membuat setiap jalan lebih aman...
sambil membangun jutaan kali lebih banyak jalan.

<!-- S55 -->
Jadi apakah para pemrogram buruk dalam pekerjaannya?
Tidak.
Kita selama ini meminta sesuatu dari mereka
yang tak bisa dijamin oleh metode umum mana pun.

<!-- S56 -->
Jadi mungkin
"bagaimana kita menulis perangkat lunak tanpa bug?"
adalah pertanyaan yang salah.

<!-- S57 -->
Pertanyaan yang lebih baik adalah:
bagaimana kita membangun sistem yang tetap aman
bahkan ketika perangkat lunaknya punya bug?

<!-- S58 -->
Dan justru ke sanalah arah keamanan.
Ia tak berkata: jangan pernah berbuat salah.
Ia berkata: anggaplah Anda sudah berbuat salah.

<!-- S59 -->
Ingat alamat kembali tadi?
Hari ini, sistem menjaganya.
Ia mengacak tempat segala sesuatu berada di memori.
Dan ia menolak menjalankan instruksi
yang tersembunyi di dalam data.

<!-- S60 -->
Bug di kode C kita masih ada di sana.
Hanya saja jauh lebih sulit diubah menjadi serangan.

<!-- S61 -->
Dan gagasan yang sama ada di mana-mana.
Sandbox, izin terbatas,
proses terisolasi, enkripsi,
cadangan, pemantauan...
lapis demi lapis,
supaya satu bug tak menjadi bencana.

<!-- S62 -->
Dan ini punya konsekuensi yang sangat praktis.
Kalau bug tak terhindarkan,
memperbaikinya adalah keharusan.

<!-- S63 -->
Perangkat lunak yang Anda pakai hari ini
sangat mungkin mengandung kerentanan
yang belum ditemukan siapa pun.

<!-- S64 -->
Dan ketika seseorang menemukannya,
pembaruan adalah pembeda antara
"sebuah kerentanan ditemukan"
dan "kami diretas".

<!-- S65 -->
Hal yang sama berlaku untuk sistem yang kita bangun.
Pustaka lama dan platform yang tak lagi didukung
tak menjadi lebih aman dengan diabaikan.
Semua itu berubah menjadi utang teknis.

<!-- S66 -->
Dan mengapa utang itu harus dilunasi —
video saya
"Masih Berfungsi. Lalu Kenapa Harus Diperbarui?"
membahas justru soal itu.

<!-- S67 -->
Sebab dalam perangkat lunak,
"masih berfungsi"
dan "masih aman"
adalah dua hal yang sangat berbeda.
