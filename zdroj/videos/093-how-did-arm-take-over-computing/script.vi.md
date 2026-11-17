# ARM đã chiếm lĩnh ngành điện toán như thế nào?

<!-- S01 -->
Năm 1985, các kỹ sư ở Anh
bật một bộ xử lý hoàn toàn mới
lần đầu tiên.

<!-- S02 -->
Nó chạy.
Riêng điều đó đã là một phép màu nhỏ.

<!-- S03 -->
Nhưng rồi họ nhận ra một điều lạ.
Nguồn điện của con chip
chưa hề được nối.

<!-- S04 -->
Vậy mà nó vẫn chạy.

<!-- S05 -->
Nó sống nhờ những dòng điện cực nhỏ
rò vào qua các chân đầu vào,
từ tín hiệu của những con chip xung quanh.

<!-- S06 -->
Khi đo đạc cẩn thận,
họ thấy bộ xử lý chỉ cần
khoảng một phần mười watt.

<!-- S07 -->
Không ai nhắm tới điều đó.
Các kỹ sư chỉ muốn một con chip
có chi phí sản xuất thấp.

<!-- S08 -->
Con chip đó là bộ xử lý ARM đầu tiên.

<!-- S09 -->
Bốn mươi năm sau, hậu duệ của nó
có mặt trong gần như mọi điện thoại thông minh.
Trong máy tính của Apple.
Trong một số trung tâm dữ liệu lớn nhất
thế giới.

<!-- S10 -->
Hàng trăm tỷ con chip.

<!-- S11 -->
Vậy làm thế nào một bộ xử lý
của một công ty máy tính gia đình ở Anh
lại chiếm lĩnh ngành điện toán?

<!-- S12 -->
Câu trả lời không đơn giản là
nó tiêu thụ rất ít điện.
Phần đó gần như là tình cờ.

<!-- S12b -->
Nhân tiện, nếu bạn thích những video
như thế này, bạn có thể đăng ký kênh.

Như vậy sẽ giúp kênh rất nhiều.

<!-- S13 -->
Để hiểu điều gì thực sự đã xảy ra,
ta phải quay lại năm 1983.

<!-- S14 -->
Công ty đó là Acorn Computers.
Chiếc BBC Micro của họ có mặt trong lớp học
khắp nước Anh.

<!-- S15 -->
BBC Micro chạy trên một con chip
tám bit cũ hơn, chip 6502.
Cho cỗ máy tiếp theo,
Acorn cần thứ gì đó nhanh hơn nhiều.

<!-- S16 -->
Vì vậy nhóm đã thử
các bộ xử lý mới trên thị trường.
Không cái nào làm được điều Acorn muốn.

<!-- S17 -->
Chúng đều phức tạp,
và không cái nào thật sự hợp
với thứ Acorn muốn chế tạo.

<!-- S18 -->
Rồi hai kỹ sư của Acorn,
Sophie Wilson và Steve Furber,
bay sang Arizona,
tới một công ty do một trong những
người thiết kế ban đầu của 6502 lập ra.

<!-- S19 -->
Họ tưởng sẽ gặp một công ty chip lớn.
Thay vào đó, họ thấy một nhúm người
làm việc trong một căn nhà ở ngoại ô.

<!-- S20 -->
Và họ trở về
với một kết luận đơn giản.
Nếu họ thiết kế được bộ xử lý...
thì chúng ta cũng làm được.

<!-- S22 -->
Thời đó, bộ xử lý ngày càng có thêm
những lệnh phức tạp hơn.

<!-- S23 -->
Chỉ một lệnh có thể lấy
một số từ bộ nhớ,
tính toán với nó,
rồi ghi kết quả trở lại.

<!-- S24 -->
Tiện cho lập trình viên.
Nhưng mỗi lệnh như vậy
khiến con chip khó chế tạo hơn.

<!-- S25 -->
Chip cần thêm mạch logic
chỉ để hiểu mỗi lệnh có nghĩa là gì.
Thêm bóng bán dẫn.
Thêm thời gian thiết kế.

<!-- S26 -->
Các nhà nghiên cứu ở Berkeley và Stanford
đã đặt ra một câu hỏi táo bạo.

<!-- S27 -->
Sẽ ra sao nếu một bộ xử lý
chỉ có những lệnh đơn giản,
còn trình biên dịch lo phần còn lại?

<!-- S28 -->
Họ gọi nó là RISC.
Máy tính với tập lệnh rút gọn.

<!-- S29 -->
Sophie Wilson thiết kế
các lệnh của ARM theo hướng đó.

<!-- S30 -->
Các phép toán số học chỉ dùng
các thanh ghi của chính con chip,
những ô nhớ nhỏ, truy cập nhanh trong bộ xử lý.
Làm việc với bộ nhớ thì có lệnh riêng.

<!-- S31 -->
Vì vậy, cộng một số từ bộ nhớ
trở thành ba bước.
Nạp vào.
Cộng.
Lưu lại.

<!-- S32 -->
Đó gọi là kiến trúc load-store.

<!-- S33 -->
Chương trình phải làm nhiều bước hơn.
Nhưng bước nào cũng đồng nhất,
dễ đoán trước
và dễ giải mã.

<!-- S34 -->
Và ARM có rất nhiều thanh ghi
để dùng.
Mười sáu cái, mỗi cái rộng 32 bit.
6502 chỉ có ba thanh ghi nhỏ.

<!-- S35 -->
Kết quả là ARM1.

<!-- S36 -->
Nó có khoảng
25.000 bóng bán dẫn.

<!-- S37 -->
Chip 286 của Intel, ra mắt vài năm trước đó,
có khoảng 134.000.

<!-- S38 -->
Ít bóng bán dẫn hơn nghĩa là chip nhỏ hơn.
Chip rẻ hơn.

<!-- S39 -->
Và gần như là một tác dụng phụ,
một con chip hầu như không tốn điện.

<!-- S40 -->
Một phần mười watt kia
là từ đó mà ra.
Acorn muốn một vỏ nhựa rẻ tiền,
nghĩa là phải giữ dưới một watt.
Nên họ thiết kế thật cẩn thận...
và đạt mức thấp hơn tới mười lần.

<!-- S41 -->
Năm 1987, một phiên bản ARM nhanh hơn
được đưa vào máy tính mới của Acorn,
chiếc Archimedes.

<!-- S42 -->
Nó là một trong những máy tính cá nhân
nhanh nhất thời bấy giờ.

<!-- S43 -->
Và điều đó gần như chẳng có ý nghĩa gì.

<!-- S44 -->
Cả thế giới đang mua PC tương thích IBM
chạy bộ xử lý Intel.
Phần mềm được viết cho nền tảng đó.
Doanh nghiệp mua thứ đó.

<!-- S45 -->
Archimedes chủ yếu
chỉ quanh quẩn trong các trường học ở Anh.

<!-- S46 -->
Còn bản thân Acorn thì đang chật vật.
Ngay từ năm 1985, công ty đã phải
nhờ Olivetti giải cứu.

<!-- S48 -->
Rồi sự giúp đỡ đến từ Apple.
Apple đang làm một máy tính cầm tay
tên là Newton.

<!-- S49 -->
Họ cần một bộ xử lý
nhanh, rẻ,
và chạy được bằng pin.

<!-- S50 -->
ARM hoàn toàn phù hợp.
Nhưng Apple không muốn phụ thuộc
vào con chip thuộc về
một hãng máy tính đối thủ.

<!-- S51 -->
Vì thế năm 1990, nhóm ARM
được tách khỏi Acorn
thành một công ty riêng.

<!-- S52 -->
Acorn, Apple
và hãng sản xuất chip VLSI
cùng sở hữu công ty này.

<!-- S53 -->
Mười hai kỹ sư.
Một nhà kho nông trại cũ gần Cambridge.

<!-- S54 -->
Và một mô hình kinh doanh
hóa ra mới là bí quyết thành công thật sự.

<!-- S55 -->
Intel tự thiết kế bộ xử lý,
sản xuất trong nhà máy của chính mình
rồi đem bán.

<!-- S56 -->
ARM sẽ không sản xuất gì cả.
ARM sẽ bán bản thiết kế.

<!-- S57 -->
Bất kỳ công ty nào cũng có thể mua giấy phép,
đưa lõi ARM vào chip của riêng mình
và trả một khoản phí nhỏ
cho mỗi con chip bán ra.

<!-- S58 -->
Điều đó quan trọng,
vì một con chip không nhất thiết
chỉ là bộ xử lý.
Quanh lõi ARM,
bạn có thể đặt một mạch vô tuyến,
một khối đồ họa,
một bộ xử lý camera.

<!-- S59 -->
Một con chip,
do chính bên cần nó thiết kế,
với ARM ở trung tâm.

<!-- S60 -->
ARM không cần phải đánh bại Intel
trên thị trường máy tính cá nhân.
Nó có thể nằm bên trong bất cứ thứ gì.

<!-- S61 -->
Và trong thập niên 1990,
“bất cứ thứ gì” ngày càng có nghĩa là
điện thoại di động.

<!-- S62 -->
Máy tính để bàn có thể dùng
một trăm watt và một chiếc quạt lớn.
Điện thoại thì chạy bằng pin
trong túi bạn.

<!-- S63 -->
Đến cuối thập niên đó,
lõi ARM đã nằm trong
một số điện thoại bán chạy nhất,
của Nokia và các hãng khác.

<!-- S64 -->
Rồi iPod ra đời.
Rồi đến điện thoại thông minh.

<!-- S65 -->
Hàng tỷ người bỗng mang theo
một chiếc máy tính phải trụ được
cả ngày bằng pin.

<!-- S66 -->
Và bộ xử lý được tạo ra
vì nó rẻ
hóa ra lại chính là
thứ mà thế giới đó cần.

<!-- S67 -->
Vậy đó là câu trả lời, đúng không?
ARM đơn giản,
đơn giản nghĩa là hiệu quả,
và hiệu quả thì chiến thắng.

<!-- S68 -->
Không hẳn.

<!-- S69 -->
Hãy nhìn vào bên trong một lõi ARM cao cấp hiện đại.

<!-- S70 -->
Bộ nhớ đệm khổng lồ.
Nhiều lệnh chạy cùng lúc.
Dự đoán rẽ nhánh,
tức là đoán chương trình sẽ đi hướng nào
trước khi nó tới đó.

<!-- S71 -->
Thực thi không theo thứ tự,
tức là chạy các lệnh
theo bất kỳ thứ tự nào nhanh nhất.

<!-- S72 -->
Hàng tỷ bóng bán dẫn trên con chip.
Chẳng có gì ở đó là đơn giản.

<!-- S73 -->
Vậy sự đơn giản đã đi đâu?

<!-- S74 -->
Mấu chốt là một bộ xử lý
thực ra là hai thứ khác nhau.

<!-- S75 -->
Tập lệnh là ngôn ngữ
mà phần mềm sử dụng.
Có những lệnh nào,
và chúng có nghĩa là gì.

<!-- S76 -->
Vi kiến trúc là cỗ máy
thực sự thực thi các lệnh đó.

<!-- S77 -->
Ngôn ngữ có thể vẫn đơn giản,
trong khi cỗ máy bên dưới
trở nên phức tạp vô cùng.

<!-- S78 -->
Và điều tương tự cũng xảy ra
ở phía bên kia.

<!-- S79 -->
Các lệnh x86 của Intel
nổi tiếng là phức tạp.

<!-- S80 -->
Nhưng từ giữa thập niên 1990,
bộ xử lý của Intel và AMD
đã tách chúng ra bên trong
thành những thao tác nhỏ, đơn giản.

<!-- S81 -->
Rồi chạy chúng trên một cỗ máy
rất giống với cỗ máy
bên trong một lõi ARM hiện đại.

<!-- S82 -->
Bên dưới những cái tên,
hai bên đã trở nên giống nhau đến bất ngờ.

<!-- S83 -->
Các lệnh gọn gàng hơn của ARM vẫn có ích.
Chúng dễ giải mã hơn,
điều này có thể tiết kiệm chút điện.

<!-- S84 -->
Nhưng đó không phải lợi thế thần kỳ
mà x86 không bao giờ bắt kịp.

<!-- S85 -->
Vậy ARM không chiếm lĩnh
vì nó đơn giản.
Và nó cũng không được thiết kế để tiết kiệm điện.

<!-- S86 -->
Nó thắng vì ba điều cùng hội tụ.
Một thiết kế hiệu quả.
Một mô hình kinh doanh
cho phép bất kỳ ai xây dựng trên ARM.
Và một thế giới bỗng cần
hàng tỷ máy tính chạy bằng pin.

<!-- S87 -->
Rồi đến năm 2020,
câu chuyện quay lại với Apple.

<!-- S88 -->
Apple đã bán cổ phần của mình ở ARM
từ nhiều năm trước,
khi họ rất cần tiền.

<!-- S89 -->
Giờ họ đưa chip dựa trên ARM của riêng mình
vào máy Mac.

<!-- S90 -->
Cùng loại lõi như trong iPhone,
được mở rộng để dùng cho máy tính.
Lõi nhanh, lõi tiết kiệm điện,
đồ họa và nhiều thứ khác nữa,
trong một con chip duy nhất.

<!-- S91 -->
Chúng nhanh hơn
những con chip Intel mà chúng thay thế,
và máy tính xách tay chạy lâu hơn nhiều
sau mỗi lần sạc.

<!-- S92 -->
ARM không còn
chỉ là bộ xử lý cho điện thoại.

<!-- S93 -->
Và ARM không dừng ở đó.
Nó còn tiến vào các trung tâm dữ liệu,
nơi mỗi watt đều tốn tiền.
Amazon giờ tự thiết kế
chip máy chủ ARM của riêng mình.

<!-- S95 -->
Con chip ARM đầu tiên có khoảng
25.000 bóng bán dẫn.
Chip ngày nay có hàng tỷ.

<!-- S96 -->
Gần như mọi thứ về cách chúng
hoạt động bên trong đã thay đổi.

<!-- S98 -->
Một nhóm nhỏ muốn có
một bộ xử lý mà họ thực sự chế tạo được.

<!-- S99 -->
Họ không làm nó cho điện thoại,
cho Apple,
hay để đánh bại Intel.

<!-- S100 -->
Và rốt cuộc,
thứ quan trọng nhất họ tạo ra
không phải con chip.

<!-- S101 -->
Mà là một nền móng đơn giản
để mọi người khác xây dựng lên trên.
