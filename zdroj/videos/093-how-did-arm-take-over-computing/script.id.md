# Bagaimana ARM Menguasai Dunia Komputasi?

<!-- S01 -->
Pada tahun 1985, para insinyur di Inggris
menyalakan sebuah prosesor baru
untuk pertama kalinya.

<!-- S02 -->
Prosesor itu berfungsi.
Itu saja sudah semacam keajaiban kecil.

<!-- S03 -->
Tapi lalu mereka melihat sesuatu yang aneh.
Catu daya chip itu
ternyata tidak tersambung.

<!-- S04 -->
Tapi chip itu tetap berjalan.

<!-- S05 -->
Ia bertahan dengan arus yang sangat kecil
yang merembes masuk lewat pin input-nya,
dari sinyal chip-chip di sekitarnya.

<!-- S06 -->
Saat diukur dengan benar,
prosesor itu hanya butuh
sekitar sepersepuluh watt.

<!-- S07 -->
Tidak ada yang menargetkan itu.
Para insinyur cuma ingin chip
yang murah untuk dibuat.

<!-- S08 -->
Chip itu adalah prosesor ARM yang pertama.

<!-- S09 -->
Empat puluh tahun kemudian, keturunannya
ada di hampir setiap smartphone.
Di komputer-komputer Apple.
Di beberapa pusat data terbesar
di dunia.

<!-- S10 -->
Ratusan miliar chip.

<!-- S11 -->
Jadi, bagaimana prosesor
dari perusahaan komputer rumahan Inggris
bisa menguasai dunia komputasi?

<!-- S12 -->
Jawabannya bukan sekadar
karena dayanya sangat kecil.
Bagian itu nyaris kebetulan.

<!-- S12b -->
Ngomong-ngomong, kalau kamu suka
video seperti ini, kamu bisa subscribe.

Itu sangat membantu channel ini.

<!-- S13 -->
Untuk memahami apa yang sebenarnya terjadi,
kita harus kembali ke tahun 1983.

<!-- S14 -->
Perusahaannya bernama Acorn Computers.
Komputer BBC Micro buatannya ada di kelas-kelas
di seluruh Inggris.

<!-- S15 -->
BBC Micro memakai chip delapan bit
yang lebih tua, yaitu 6502.
Untuk mesin berikutnya,
Acorn butuh sesuatu yang jauh lebih cepat.

<!-- S16 -->
Jadi timnya menguji
prosesor-prosesor baru di pasaran.
Tidak ada yang sesuai keinginan Acorn.

<!-- S17 -->
Semuanya rumit,
dan tidak ada yang benar-benar cocok
dengan apa yang ingin dibangun Acorn.

<!-- S18 -->
Lalu dua insinyur Acorn,
Sophie Wilson dan Steve Furber,
pergi ke Arizona,
ke perusahaan yang didirikan salah satu
perancang asli chip 6502.

<!-- S19 -->
Mereka mengira akan menemukan perusahaan chip besar.
Ternyata yang mereka temukan hanya segelintir orang
yang bekerja dari sebuah rumah di pinggiran kota.

<!-- S20 -->
Dan mereka pulang
dengan kesimpulan sederhana.
Kalau mereka bisa merancang prosesor...
kita juga bisa.

<!-- S22 -->
Waktu itu, prosesor terus mendapat
instruksi yang makin lama makin rumit.

<!-- S23 -->
Satu instruksi bisa mengambil
sebuah angka dari memori,
melakukan perhitungan dengan angka itu,
lalu menulis hasilnya kembali.

<!-- S24 -->
Praktis bagi programmer.
Tapi setiap instruksi seperti itu
membuat chip makin sulit dibuat.

<!-- S25 -->
Chip butuh lebih banyak logika
hanya untuk memahami arti tiap instruksi.
Lebih banyak transistor.
Lebih lama waktu desain.

<!-- S26 -->
Para peneliti di Berkeley dan Stanford
sudah mengajukan pertanyaan radikal.

<!-- S27 -->
Bagaimana kalau sebuah prosesor
hanya punya instruksi sederhana,
dan sisanya dikerjakan oleh compiler?

<!-- S28 -->
Mereka menyebutnya RISC.
Komputer dengan set instruksi yang disederhanakan.

<!-- S29 -->
Sophie Wilson merancang
instruksi ARM dengan prinsip itu.

<!-- S30 -->
Operasi aritmetika hanya bekerja
pada register milik chip itu sendiri,
slot-slot kecil dan cepat di dalam prosesor.
Untuk memori, ada instruksi khusus.

<!-- S31 -->
Jadi menambahkan angka dari memori
menjadi tiga langkah.
Muat.
Tambahkan.
Simpan.

<!-- S32 -->
Ini disebut arsitektur load-store.

<!-- S33 -->
Langkah program jadi lebih banyak.
Tapi setiap langkahnya teratur,
mudah ditebak,
dan gampang didekode.

<!-- S34 -->
Dan ARM punya banyak register
untuk bekerja.
Enam belas, masing-masing 32 bit.
6502 hanya punya tiga register kecil.

<!-- S35 -->
Hasilnya adalah ARM1.

<!-- S36 -->
Chip ini punya sekitar
25.000 transistor.

<!-- S37 -->
Intel 286, yang diluncurkan beberapa tahun sebelumnya,
punya sekitar 134.000.

<!-- S38 -->
Lebih sedikit transistor berarti chip lebih kecil.
Chip lebih murah.

<!-- S39 -->
Dan, hampir sebagai efek samping,
chip yang nyaris tidak memakai daya.

<!-- S40 -->
Dari situlah asal
sepersepuluh watt tadi.
Acorn ingin kemasan plastik yang murah,
yang berarti dayanya harus di bawah satu watt.
Jadi mereka merancangnya dengan hati-hati...
dan hasilnya sepuluh kali lebih rendah.

<!-- S41 -->
Pada tahun 1987, versi ARM yang lebih cepat
dipasang di komputer baru Acorn,
yaitu Archimedes.

<!-- S42 -->
Komputer ini termasuk komputer pribadi
tercepat pada masanya.

<!-- S43 -->
Tapi itu nyaris tidak ada artinya.

<!-- S44 -->
Dunia membeli PC yang kompatibel dengan IBM
dengan prosesor Intel.
Software-nya tersedia untuk PC itu.
Itulah yang dibeli perusahaan-perusahaan.

<!-- S45 -->
Archimedes kebanyakan
hanya dipakai di sekolah-sekolah Inggris.

<!-- S46 -->
Dan Acorn sendiri sedang kesulitan.
Perusahaan ini bahkan sudah harus diselamatkan
oleh Olivetti pada tahun 1985.

<!-- S48 -->
Lalu bantuan datang dari Apple.
Apple sedang membuat komputer genggam
bernama Newton.

<!-- S49 -->
Apple butuh prosesor
yang cepat, murah,
dan bisa berjalan dengan baterai.

<!-- S50 -->
ARM sangat cocok.
Tapi Apple tidak mau bergantung
pada chip milik
produsen komputer saingannya.

<!-- S51 -->
Jadi pada tahun 1990, tim ARM
dipisahkan dari Acorn
menjadi perusahaan sendiri.

<!-- S52 -->
Acorn, Apple,
dan produsen chip VLSI
memilikinya bersama-sama.

<!-- S53 -->
Dua belas insinyur.
Sebuah lumbung tua di dekat Cambridge.

<!-- S54 -->
Dan sebuah model bisnis
yang ternyata menjadi rahasia sukses sebenarnya.

<!-- S55 -->
Intel merancang prosesornya,
membuatnya di pabrik sendiri,
lalu menjualnya.

<!-- S56 -->
ARM sama sekali tidak akan membuat apa pun.
ARM akan menjual desainnya.

<!-- S57 -->
Perusahaan mana pun bisa membeli lisensinya,
memasang inti ARM di chip buatannya sendiri,
lalu membayar biaya kecil
untuk setiap chip yang terjual.

<!-- S58 -->
Itu penting,
karena sebuah chip tidak harus
hanya berisi prosesor.
Di sekeliling inti ARM,
kamu bisa menaruh radio,
unit grafis,
prosesor kamera.

<!-- S59 -->
Satu chip,
dirancang oleh siapa pun yang membutuhkannya,
dengan ARM di tengahnya.

<!-- S60 -->
ARM tidak perlu mengalahkan Intel
di pasar komputer pribadi.
ARM bisa dipasang di dalam apa saja.

<!-- S61 -->
Dan pada tahun 1990-an,
"apa saja" makin sering berarti
ponsel.

<!-- S62 -->
Komputer desktop boleh memakai
seratus watt dan kipas besar.
Ponsel berjalan dengan baterai
di dalam sakumu.

<!-- S63 -->
Menjelang akhir dekade itu,
inti ARM sudah ada di dalam
beberapa ponsel paling laris,
dari Nokia dan merek lainnya.

<!-- S64 -->
Lalu datanglah iPod.
Lalu smartphone.

<!-- S65 -->
Miliaran orang tiba-tiba membawa
komputer yang harus bertahan
seharian dengan baterai.

<!-- S66 -->
Dan prosesor yang dibuat
karena murah
ternyata justru
yang dibutuhkan dunia seperti itu.

<!-- S67 -->
Jadi itu jawabannya, kan?
ARM itu sederhana,
sederhana berarti efisien,
dan yang efisien menang.

<!-- S68 -->
Tidak sepenuhnya.

<!-- S69 -->
Coba lihat isi inti ARM kelas atas yang modern.

<!-- S70 -->
Cache yang sangat besar.
Beberapa instruksi berjalan sekaligus.
Prediksi percabangan,
yaitu menebak ke mana program akan pergi
sebelum program sampai di sana.

<!-- S71 -->
Eksekusi di luar urutan,
yaitu menjalankan instruksi
dalam urutan mana pun yang paling cepat.

<!-- S72 -->
Miliaran transistor di dalam chip.
Tidak ada yang sederhana di sini.

<!-- S73 -->
Jadi, ke mana perginya kesederhanaan itu?

<!-- S74 -->
Kuncinya, sebuah prosesor
sebenarnya terdiri dari dua hal yang berbeda.

<!-- S75 -->
Set instruksi adalah bahasa
yang dipakai software.
Instruksi apa saja yang ada,
dan apa artinya.

<!-- S76 -->
Mikroarsitektur adalah mesin
yang benar-benar menjalankannya.

<!-- S77 -->
Bahasanya bisa tetap sederhana,
sementara mesin di baliknya
menjadi luar biasa rumit.

<!-- S78 -->
Dan hal yang sama terjadi
di pihak lain.

<!-- S79 -->
Instruksi x86 milik Intel
terkenal rumit.

<!-- S80 -->
Tapi sejak pertengahan 1990-an,
prosesor Intel dan AMD
memecahnya secara internal
menjadi operasi-operasi kecil yang sederhana.

<!-- S81 -->
Lalu operasi itu dijalankan di mesin
yang mirip sekali dengan mesin
di dalam inti ARM modern.

<!-- S82 -->
Di balik labelnya,
keduanya ternyata jadi sangat mirip.

<!-- S83 -->
Instruksi ARM yang lebih rapi tetap membantu.
Instruksinya lebih mudah didekode,
sehingga bisa sedikit menghemat daya.

<!-- S84 -->
Tapi itu bukan keunggulan ajaib
yang tidak akan pernah bisa dikejar x86.

<!-- S85 -->
Jadi ARM tidak menang
karena sederhana.
Dan ARM juga tidak dirancang untuk hemat daya.

<!-- S86 -->
ARM menang karena tiga hal bertemu.
Desain yang efisien.
Model bisnis
yang membuat siapa pun bisa membangun dengan ARM.
Dan dunia yang tiba-tiba membutuhkan
miliaran komputer bertenaga baterai.

<!-- S87 -->
Lalu, pada tahun 2020,
ceritanya kembali ke Apple.

<!-- S88 -->
Apple sudah menjual sahamnya di ARM
bertahun-tahun sebelumnya,
saat sangat butuh uang.

<!-- S89 -->
Kini Apple memasang chip berbasis ARM buatannya sendiri
di Mac.

<!-- S90 -->
Inti yang sejenis dengan di iPhone,
diperbesar untuk komputer.
Inti cepat, inti hemat daya,
grafis, dan banyak lagi,
dalam satu chip.

<!-- S91 -->
Chip itu lebih cepat
dari chip Intel yang digantikannya,
dan laptopnya bertahan jauh lebih lama
dengan sekali isi daya.

<!-- S92 -->
ARM bukan lagi
sekadar prosesor ponsel.

<!-- S93 -->
Dan ARM tidak berhenti di situ.
ARM juga masuk ke pusat data,
tempat setiap watt berarti biaya.
Amazon kini merancang
chip server ARM-nya sendiri.

<!-- S95 -->
Chip ARM pertama punya sekitar
25.000 transistor.
Chip masa kini punya miliaran.

<!-- S96 -->
Hampir semua hal tentang
cara kerjanya di dalam sudah berubah.

<!-- S98 -->
Sebuah tim kecil menginginkan
prosesor yang benar-benar bisa mereka buat.

<!-- S99 -->
Mereka tidak membuatnya untuk ponsel,
untuk Apple,
atau untuk mengalahkan Intel.

<!-- S100 -->
Dan pada akhirnya,
hal terpenting yang mereka ciptakan
bukanlah chip itu.

<!-- S101 -->
Melainkan fondasi sederhana
yang bisa dipakai semua orang untuk membangun.
