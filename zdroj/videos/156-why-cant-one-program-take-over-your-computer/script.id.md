<!-- S01 -->
Pada 19 Juli 2024,
sebuah perusahaan keamanan bernama CrowdStrike
mengirim pembaruan rutin.

<!-- S02 -->
Bukan program baru.
Hanya file konfigurasi kecil.

<!-- S03 -->
Dalam hitungan jam, 8,5 juta
komputer Windows berhenti
di layar biru.

<!-- S04 -->
Maskapai menghentikan penerbangan.
Rumah sakit membatalkan operasi.
Sebuah saluran berita berhenti mengudara.

<!-- S05 -->
Dan kesalahan di baliknya
sangat biasa.
Programnya mengharapkan 20 data.
Pembaruannya memberinya 21.

<!-- S06 -->
Game dan aplikasimu membuat
kesalahan seperti itu terus-menerus.
Kalau itu terjadi, game-nya tertutup,
lalu kamu membukanya lagi.

<!-- S07 -->
Jenis bug yang sama.
Yang satu menutup sebuah jendela.
Yang lain menghentikan
8,5 juta mesin.

<!-- S08 -->
Bedanya bukan pada kesalahannya.
Tapi pada tempat kode itu berjalan.

<!-- S09 -->
Jadi kenapa satu program tidak bisa
mengambil alih komputermu...
dan kenapa yang satu ini bisa?

<!-- S10 -->
Dulu tidak selalu begini.

<!-- S11 -->
Di PC dengan DOS pada tahun 1980-an,
tidak ada apa pun di prosesor yang menghentikan program.
Program bisa menulis ke bagian memori mana saja
dan berbicara langsung dengan hardware.

<!-- S12 -->
Cukup satu program menulis
ke tempat yang salah,
dan sistem operasinya bisa tertimpa,
lalu seluruh mesin membeku.

<!-- S13 -->
Solusinya: berhenti memercayai program
dan menyerahkan urusan curiga
kepada prosesor.

<!-- S14 -->
Pada tahun 1982, prosesor Intel 80286
memperkenalkan protected mode,
dengan empat tingkat hak akses.

<!-- S15 -->
Biasanya digambar
sebagai empat cincin, satu di dalam yang lain.

<!-- S16 -->
Ring 0 ada di tengah.
Ring 3 ada di luar.

<!-- S17 -->
Dan penomorannya terbalik.
Makin kecil angkanya,
makin banyak yang boleh dilakukan kode.

<!-- S18 -->
Ring 0 milik kernel,
inti dari sistem operasi.
Kernel membagi memori,
memutuskan program mana yang berjalan berikutnya,
dan berbicara dengan hardware.

<!-- S19 -->
Di ring 3 berjalan browser-mu,
game-mu, dan editor teksmu.
Ini disebut user mode.

<!-- S19b -->
Windows, macOS, dan Linux
semuanya membagi tugas dengan cara ini.
Kernel di ring 0,
aplikasimu di ring 3.

<!-- S19c -->
Ponsel dan Mac baru buatan Apple
memakai chip ARM sebagai gantinya.
Di sana, tingkatnya disebut exception level.
Namanya beda, pembagiannya sama:
satu untuk kernel, satu untuk aplikasimu.

<!-- S20 -->
Prosesor selalu tahu
di ring mana ia sedang berjalan.
Dan ia memeriksanya.

<!-- S21 -->
Beberapa instruksi hanya bekerja di ring 0.
Misalnya mematikan interrupt
atau mengubah cara memori dipetakan.

<!-- S22 -->
Kalau program di ring 3 mencoba salah satunya,
prosesor menolak.
Ia memicu exception
dan menyerahkan kendali ke kernel,
yang biasanya menutup program itu.

<!-- S23 -->
Memori diperlakukan dengan cara yang sama.
Setiap halaman memori ditandai
sebagai user atau supervisor.

<!-- S24 -->
Program di ring 3
yang menyentuh halaman supervisor
tidak mendapat datanya.
Ia dihentikan.

<!-- S25 -->
Browser dan game-mu
sama-sama berjalan di ring 3.
Keduanya terpisah
karena masing-masing punya peta memorinya sendiri.
Memori program yang lain
sama sekali tidak ada di peta itu.

<!-- S26 -->
Jadi kalau sebuah game crash,
kerusakannya tetap di dalam game itu.
Kernel membereskannya.
Semua yang lain tetap berjalan.

<!-- S27 -->
Sekarang lihat lagi CrowdStrike.
Driver-nya berjalan di ring 0,
tepat di sebelah kernel.

<!-- S28 -->
Tidak ada apa pun di atas ring 0
yang bisa menangkap kesalahan seperti itu.

<!-- S29 -->
Jadi Windows melakukan satu-satunya hal aman yang tersisa.
Ia menghentikan seluruh mesin, dengan sengaja,
daripada terus berjalan dengan memori
yang tidak bisa lagi dipercaya.

<!-- S30 -->
Itulah layar biru.

<!-- S31 -->
Dan karena driver itu ikut menyala
setiap kali Windows menyala,
setiap restart membawa crash itu kembali.

<!-- S32 -->
Tapi ini memunculkan pertanyaan.
Kalau browser-mu tidak boleh menyentuh hardware,
bagaimana ia bisa menyimpan file
atau mengirim apa pun lewat jaringan?

<!-- S33 -->
Ia meminta.

<!-- S34 -->
Program menaruh permintaannya
di register prosesor.
File yang mana. Ke mana datanya harus pergi.
Berapa banyak.

<!-- S35 -->
Lalu ia menjalankan satu instruksi khusus.
Di PC modern, namanya SYSCALL.

<!-- S36 -->
Pada saat itu, prosesor berpindah
dari ring 3 ke ring 0...

<!-- S37 -->
tapi ia tidak melompat
ke mana pun program mau.
Ia melompat ke satu titik masuk
yang sudah dipilih kernel sebelumnya.

<!-- S38 -->
Kernel memeriksa permintaan itu,
mengerjakan tugasnya,
lalu kembali ke ring 3.
Program itu sendiri tidak pernah menyentuh disk.

<!-- S39 -->
Inilah system call,
dan ini terjadi terus-menerus.

<!-- S40 -->
Kami menghitungnya di sebuah laptop.
Program yang sama sekali tidak melakukan apa-apa
tetap membuat 30 system call.

<!-- S41 -->
Firefox, saat dibuka
dan memuat satu halaman Wikipedia,
membuat sekitar 670.000
dalam 20 detik...
padahal penghitungan kami ikut memperlambatnya.

<!-- S42 -->
Setiap system call
adalah perjalanan menembus tembok dan kembali.

<!-- S43 -->
Lalu ada yang aneh.
Empat ring,
dan kita hanya butuh dua.

<!-- S44 -->
Apa yang terjadi dengan ring 1 dan 2?

<!-- S45 -->
Gagasan ring lebih tua dari PC.
Multics, sistem operasi
dari akhir tahun 1960-an,
punya delapan.

<!-- S46 -->
Gagasannya adalah lapisan kepercayaan.
Inti sistem di tengah,
layanan yang kurang dipercaya di sekitarnya,
dan program di luar.

<!-- S46b -->
Intel menggambar hal yang sama.
Ring 1 dan 2 dimaksudkan
untuk lapisan di antaranya,
seperti driver dan layanan sistem.
Lebih dipercaya daripada aplikasimu,
tapi tidak sepercaya kernel.

<!-- S47 -->
Ada dua hal yang menghalangi.

<!-- S48 -->
Pertama, sistem seperti Unix dan Windows NT
dirancang untuk berjalan
di banyak jenis prosesor.

<!-- S49 -->
Dan satu-satunya pembagian
yang ditawarkan semua prosesor
adalah dua tingkat.
Satu untuk kernel,
satu untuk semua yang lain.

<!-- S50 -->
Kedua, prosesor x86 itu sendiri.
Saat memetakan memori,
setiap halaman hanya mengenal dua status.
User atau supervisor.

<!-- S51 -->
Ring 1 dan 2 dihitung sebagai supervisor.
Jadi driver di ring 1
tetap bisa menyentuh memori kernel.
Ring tambahan itu tidak banyak melindungi.

<!-- S51b -->
Beberapa sistem tetap memakainya.
OS/2 membiarkan sebagian program masuk ke ring 2,
hanya supaya bisa berbicara langsung dengan hardware.

<!-- S51c -->
Dan sebelum prosesor punya dukungan
untuk menjalankan mesin virtual,
Xen dan VirtualBox memindahkan kernel sistem tamu
ke ring 1,
supaya sistem di bawahnya
bisa memakai ring 0 sendirian.

<!-- S52 -->
Pada tahun 2023, Intel mengusulkan
penghapusan ring 1 dan 2 sepenuhnya.

<!-- S53 -->
Pada Desember 2024, Intel membatalkan rencana itu.
Ring itu masih ada di prosesormu.
Hampir tidak ada yang memakainya.

<!-- S54 -->
Sejauh ini, kedengarannya menenangkan.
Aturannya ada di hardware,
dan hardware memeriksa setiap akses.

<!-- S55 -->
Pada tahun 2017, tiga tim peneliti,
yang bekerja terpisah,
menemukan cara menembus tembok itu.

<!-- S56 -->
Mereka menamainya Meltdown.
Dan untuk memahaminya,
kamu perlu tahu satu trik
yang dimainkan prosesor modern.

<!-- S57 -->
Prosesor tidak menunggu
satu instruksi selesai
sebelum memulai yang berikutnya.
Ia berjalan lebih dulu,
mengerjakan instruksi yang mungkin akan dibutuhkan.

<!-- S58 -->
Kalau tebakannya salah,
ia membuang hasilnya,
seolah tidak terjadi apa-apa.

<!-- S59 -->
Inilah celahnya.
Pada chip Intel yang terdampak,
program di ring 3 bisa meminta
satu byte dari memori kernel...

<!-- S60 -->
dan prosesor mengambilnya
lalu meneruskannya ke instruksi berikutnya
sebelum selesai memeriksa
apakah itu diizinkan.

<!-- S61 -->
Pemeriksaannya memang gagal.
Hasilnya dibuang.

<!-- S62 -->
Tapi instruksi-instruksi berikutnya itu
sudah memakai byte rahasia tadi
untuk menarik satu bagian
dari memori program itu sendiri
ke dalam cache prosesor.

<!-- S63 -->
Dan cache tidak lupa
hanya karena hasilnya dibatalkan.

<!-- S64 -->
Jadi program itu mengukur
seberapa cepat setiap bagian memorinya merespons.
Bagian yang merespons cepat
membocorkan byte rahasia itu.

<!-- S65 -->
Byte demi byte,
program biasa bisa membaca
memori kernel,
dan rahasia apa pun yang tersimpan di sana.
Termasuk kata sandi dan kunci enkripsi.

<!-- S66 -->
Meltdown memengaruhi prosesor Intel
yang dibuat sejak tahun 1995.

<!-- S67 -->
Celah ini diumumkan
pada 3 Januari 2018.

<!-- S68 -->
Perbaikannya tidak bisa mengubah silikon.
Jadi sistem operasi mengubah petanya.

<!-- S69 -->
Selama programmu berjalan,
memori kernel sekarang dihapus
hampir seluruhnya dari petanya.
Tidak ada lagi yang bisa diambil.

<!-- S70 -->
Tapi ingat system call tadi.
Setiap perjalanan menembus tembok
sekarang juga harus mengganti peta.

<!-- S71 -->
Red Hat mengukur patch untuk Meltdown
dan celah terkait, Spectre.
Di bawah 1% untuk sebagian pekerjaan...
hingga 19% untuk database yang sibuk.

<!-- S72 -->
Aturannya benar dari awal.
Prosesornya saja yang memeriksa terlambat.

<!-- S73 -->
Ini membawa kita kembali ke CrowdStrike,
dan ke pertanyaan yang lebih sulit.

<!-- S74 -->
Kenapa program keamanan
berada di ring 0 sejak awal?

<!-- S75 -->
Karena dari sana ia melihat segalanya.
Ia menyala sebelum software lain.
Dan malware dengan hak administrator
lebih sulit mematikannya.

<!-- S76 -->
Daftar dari Microsoft sendiri
diakhiri dengan peringatan.
Driver di kernel memberi semua itu dengan mengorbankan ketahanan sistem.

<!-- S77 -->
Setelah gangguan itu,
Microsoft mulai membangun cara
agar antivirus
bisa berjalan di luar kernel.

<!-- S78 -->
Pada musim gugur 2026,
fitur itu masih ada di versi uji Windows saja.
Dan kernel belum ditutup
bagi perusahaan keamanan.

<!-- S79 -->
Game-mu menghadapi dilema yang sama.

<!-- S80 -->
Cheat yang berjalan di kernel
tidak terlihat oleh anti-cheat
yang berjalan di ring 3.

<!-- S81 -->
Jadi anti-cheat ikut pindah ke sana.
Vanguard buatan Riot, yang dipakai Valorant,
memasang driver di ring 0.
Di kebanyakan PC, driver itu dimuat saat Windows menyala...
bahkan kalau kamu tidak pernah membuka game-nya.

<!-- S82 -->
Itu tidak membuatnya cacat.
Tapi ia berada di tempat yang sama
dengan driver CrowdStrike dulu,
tempat satu kesalahan menghentikan seluruh mesin.

<!-- S83 -->
Jadi kenapa satu program tidak bisa
mengambil alih komputermu?

<!-- S84 -->
Karena prosesor menjauhkan
hampir semua program dari pusat
dan memeriksa mereka setiap kali mereka mengetuk.

<!-- S85 -->
Tapi prosesor tidak bisa memutuskan
siapa yang boleh masuk.
Yang memutuskan itu manusia...
setiap kali mereka memasang driver.

<!-- S86 -->
Jadi ini pertanyaan untuk kolom komentar.
Siapa yang seharusnya memutuskan program mana
yang boleh masuk ke ring 0:
kamu, Microsoft,
atau perusahaan yang membuatnya?
