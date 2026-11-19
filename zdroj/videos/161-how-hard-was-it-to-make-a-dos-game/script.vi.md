<!-- S01 -->
Năm 1993, một trò chơi tên là Doom
chạy trên một chiếc máy tính
có 4 megabyte bộ nhớ.

<!-- S02 -->
Đó là khoảng dung lượng
của một bức ảnh trên điện thoại của bạn.

<!-- S03 -->
Khi đó chưa có card tăng tốc 3D.
Bộ xử lý chính
đảm nhận toàn bộ việc dựng hình.

<!-- S04 -->
Ngày nay, lập trình viên bắt đầu với một engine,
như Unity hay Unreal,
lo phần đồ họa, âm thanh,
bộ nhớ và phần cứng.

<!-- S05 -->
Trên DOS, tất cả những thứ đó
là việc của lập trình viên.
Và khá thường xuyên, của cả người chơi.

<!-- S06 -->
Vậy làm một trò chơi cho DOS
khó đến mức nào?

<!-- S07 -->
Hãy bắt đầu với bộ nhớ,
vì bộ nhớ là một mớ hỗn độn.

<!-- S08 -->
Chiếc IBM PC đầu tiên, ra đời năm 1981,
có thể đánh địa chỉ 1 megabyte bộ nhớ.

<!-- S09 -->
Nhưng chỉ
640 kilobyte đầu tiên
là dành cho chương trình.

<!-- S10 -->
384 kilobyte còn lại
được dành riêng cho bộ nhớ video,
card mở rộng và BIOS.

<!-- S11 -->
Trong hơn một thập kỷ,
DOS thường chạy chương trình
bên trong vùng đó.
Mọi thứ vượt ra ngoài đều tốn thêm công sức.

<!-- S12 -->
Câu nói nổi tiếng bắt nguồn từ đây:
640K là đủ cho bất kỳ ai.

<!-- S13 -->
Người ta thường gán nó cho Bill Gates.
Không có ghi chép nào cho thấy ông từng nói vậy,
và ông phủ nhận điều đó.

<!-- S14 -->
Đầu những năm chín mươi,
một chiếc PC có sẵn 4 megabyte,
hoặc 8.

<!-- S15 -->
Vậy mà một trò chơi vẫn có thể dừng lại
với dòng chữ
"không đủ bộ nhớ".

<!-- S16 -->
Có bộ nhớ
và dùng được nó
là hai chuyện khác nhau.

<!-- S17 -->
Một cách để lách là bộ nhớ expanded,
hay EMS.

<!-- S18 -->
Một cửa sổ 64 kilobyte
nằm ở phần trên
của megabyte đầu tiên đó.
Qua nó, chương trình có thể thấy
4 trang bộ nhớ bổ sung,
mỗi trang 16 kilobyte,

<!-- S19 -->
và đổi chúng lấy các trang khác,
giống như lật trang sách
qua một lỗ thủng trên tờ giấy.

<!-- S20 -->
Một cách khác là bộ nhớ extended,
truy cập qua một driver tên là HIMEM.

<!-- S21 -->
Và đây là lúc
vấn đề của lập trình viên
trở thành vấn đề của người chơi.

<!-- S22 -->
Driver cho chuột, ổ CD
hay card âm thanh
gặm mất một phần bộ nhớ quý giá đó,
trừ khi bạn nạp được chúng lên vùng nhớ cao.

<!-- S23 -->
Vì thế người chơi học cách sửa hai tệp,
CONFIG.SYS và AUTOEXEC.BAT.

<!-- S24 -->
Một trò cần EMS.
Một trò khác muốn tắt nó đi,
bằng một thiết lập tên là NOEMS.
Còn trò thứ ba cần từng kilobyte trống.

<!-- S25 -->
Năm 1993, MS-DOS 6 thêm vào
một menu khi khởi động.

<!-- S26 -->
Bạn chọn cấu hình
cho trò chơi bạn muốn chơi,
và máy tính khởi động riêng cho trò đó.

<!-- S27 -->
Có người cuối cùng có
một mục riêng
cho gần như mọi trò chơi họ sở hữu.

<!-- S28 -->
Nhưng đến lúc đó,
các trò chơi lớn đã tìm ra
cách vượt qua giới hạn của DOS.

<!-- S29 -->
Từ đời 386,
bản thân bộ xử lý có thể chạy
ở chế độ bảo vệ 32-bit,
với không gian lên đến 4 gigabyte.

<!-- S30 -->
Chúng ta đã nói về chế độ bảo vệ
trong một video trước.
Nhưng DOS thì không dùng được nó.

<!-- S31 -->
Vì thế các trò chơi mang theo trợ thủ riêng,
một DOS extender.
Nổi tiếng nhất là DOS/4GW.

<!-- S32 -->
Nó đi kèm với một trình biên dịch phổ biến,
Watcom C.

<!-- S33 -->
Khi một trò chơi khởi chạy,
DOS/4GW chuyển bộ xử lý
sang chế độ bảo vệ,
cho trò chơi quyền truy cập
vào bộ nhớ vượt quá giới hạn của DOS.

<!-- S34 -->
DOS vẫn ở bên dưới,
cung cấp các dịch vụ như truy cập tệp.
Nhưng giờ trò chơi chạy ở chế độ bảo vệ,
chứ không phải như một chương trình DOS truyền thống.

<!-- S35 -->
Nếu bạn từng chơi game DOS những năm chín mươi,
hẳn bạn đã thấy tên nó
lướt qua trên màn hình.

<!-- S37 -->
Giờ đến hình ảnh.
Ở một trong những chế độ VGA phổ biến nhất,
gọi là Mode 13h,
màn hình có 320
nhân 200 điểm ảnh,
với 256 màu.

<!-- S38 -->
Mỗi điểm ảnh là một byte.
Để tô màu một điểm ảnh,
bạn ghi một con số vào bộ nhớ.
Không có thư viện đồ họa. Chỉ có bộ nhớ.

<!-- S39 -->
Toàn bộ màn hình chiếm
64.000 byte.

<!-- S40 -->
Chỉ dưới 64 kilobyte một chút,
đủ nhỏ để nằm gọn trong một segment,
khối mà một chương trình 16-bit
có thể đánh địa chỉ trong một lần.
Hiếm hoi lắm, bộ nhớ mới đứng về phía bạn.

<!-- S41 -->
Nhưng nếu bạn vẽ thẳng
lên màn hình đang hiển thị,
người chơi sẽ thấy những hình vẽ dở dang,
và hình ảnh bị nhấp nháy.

<!-- S42 -->
Vì thế các trò chơi vẽ mỗi khung hình
trước tiên vào một bộ đệm ẩn,
rồi chép hình ảnh hoàn chỉnh
vào bộ nhớ video.

<!-- S43 -->
Năm 1991, Michael Abrash,
một lập trình viên kiêm tác giả,
công bố một cách tốt hơn.
Ông gọi nó là Mode X.

<!-- S44 -->
Nó dùng một phần của VGA
mà hầu hết lập trình viên
chưa từng động tới.

<!-- S45 -->
Nó cho điểm ảnh vuông,
và chỗ cho nhiều màn hình
trong bộ nhớ video.

<!-- S46 -->
Trò chơi vẽ lên một màn hình
không ai nhìn thấy,
rồi chỉ việc chuyển sang nó.
Nhưng lập trình thì khó hơn nhiều.

<!-- S47 -->
Rồi đến âm thanh.
Và âm thanh là một trò xổ số.

<!-- S48 -->
Chiếc loa sẵn có của PC
được làm ra để kêu bíp.

<!-- S49 -->
Rồi đến card âm thanh,
và các thiết bị âm thanh khác.
Không có hai cái nào
hoạt động giống nhau.

<!-- S50 -->
AdLib, với một con chip Yamaha
tổng hợp âm nhạc.
Sound Blaster, có thể phát cả
âm thanh thu sẵn.

<!-- S51 -->
Roland MT-32,
một chiếc hộp đắt tiền với nhạc cụ phong phú hơn.
Gravis UltraSound.

<!-- S52 -->
Hỗ trợ tất cả chúng
nghĩa là phải viết các driver khác nhau.

<!-- S53 -->
Và trò chơi phải biết
card nằm ở đâu.
Cổng của nó, ngắt của nó,
và kênh DMA của nó.

<!-- S54 -->
Câu trả lời quen thuộc, với Sound Blaster,
là cổng 220, IRQ 7, DMA 1.
Thường là vậy.

<!-- S55 -->
Sai một cái thôi,
là trò chơi không phát ra tiếng nào.
Hoặc bị treo.

<!-- S56 -->
Năm 1991, một lập trình viên tên John Miles
phát hành một thư viện
có thể giao tiếp với nhiều card âm thanh
qua một giao diện duy nhất.

<!-- S57 -->
Trò chơi có thể viết mã âm thanh một lần,
rồi để thư viện lo phần card.

<!-- S58 -->
Đó là thêm một lớp nữa
giữa trò chơi và phần cứng.
Hãy nhớ điều đó.

<!-- S59 -->
Rồi đến tốc độ.
Lập trình viên đếm
từng bước mà bộ xử lý thực hiện.

<!-- S63 -->
Để tìm một điểm ảnh trên màn hình,
bạn nhân số hàng của nó
với 320.

<!-- S63b -->
Trên các bộ xử lý cũ,
phép nhân có thể rất tốn kém.

<!-- S64 -->
Nhưng 320
bằng 256
cộng 64.
Cả hai đều là lũy thừa của hai.

<!-- S65 -->
Vậy bạn có thể thay phép nhân
bằng hai phép dịch bit và một phép cộng.

<!-- S67 -->
Chris Sawyer đi thẳng xuống tận phần cứng.
Ông viết Transport Tycoon năm 1994
gần như hoàn toàn bằng hợp ngữ,

<!-- S68 -->
tức là những lệnh
mà chính bộ xử lý hiểu được,
từng lệnh một.

<!-- S69 -->
Và đôi khi,
ngay cả tất cả những điều đó cũng chưa đủ.

<!-- S70 -->
Năm 1990, Wing Commander có một lỗi
mà cả nhóm không tìm ra,
trong khi hạn chót đã cận kề.

<!-- S71 -->
Khi bạn thoát trò chơi,
trình quản lý bộ nhớ bị sập
kèm một thông báo lỗi.

<!-- S72 -->
Thế là một lập trình viên, Ken Demarest,
mở trình quản lý bộ nhớ
bằng một trình sửa hex
và đổi nội dung của thông báo đó.

<!-- S73 -->
Giờ nó ghi:
"Cảm ơn bạn đã chơi Wing Commander."

<!-- S74 -->
Sau đó cả nhóm tìm ra lỗi thật,
và trò đùa ấy chưa bao giờ có mặt trong bản phát hành.

<!-- S74b -->
Một số người chơi đến giờ vẫn chắc chắn mình đã thấy nó.
Và các trò chơi sau này của Origin
thật sự chào tạm biệt như vậy.

<!-- S75 -->
Điều đó đưa chúng ta trở lại với Doom.

<!-- S76 -->
Doom dùng DOS/4GW
và chạy như một chương trình 32-bit.

<!-- S77 -->
Phần cứng tính toán dấu phẩy động
không phải máy PC nào cũng có.

<!-- S78 -->
Vì thế Doom dùng số học dấu phẩy cố định.
Những số nguyên,
với 16 bit thấp
đại diện cho phần thập phân.

<!-- S79 -->
Và thế giới của nó
không thật sự ba chiều.

<!-- S80 -->
Mỗi màn chơi là một sơ đồ mặt bằng phẳng,
với độ cao cho mỗi sàn
và mỗi trần.

<!-- S81 -->
Một căn phòng không bao giờ có thể nằm trên một phòng khác.
Và bạn không thể thật sự nhìn lên hay nhìn xuống.

<!-- S82 -->
Trước khi một màn có thể chơi được,
một công cụ chia bản đồ
thành một cây nhị phân, gọi là BSP.

<!-- S83 -->
Engine duyệt cây đó
từ trước ra sau,
bắt đầu từ phía người chơi,
và bỏ qua những vùng không thể nhìn thấy.

<!-- S84 -->
Và Doom thậm chí còn không được viết trên DOS.

<!-- S85 -->
id Software xây dựng nó
trên các máy trạm NeXT,
rồi biên dịch kết quả cho DOS.

<!-- S86 -->
Doom không phải engine 3D đa năng.
Nó được làm ra cho đúng
một kiểu thế giới.
Chính sự chuyên biệt ấy
đã giúp nó chạy được trên máy 386.

<!-- S87 -->
Và các studio khác muốn có thế giới đó.

<!-- S88 -->
Raven Software mua bản quyền engine của Doom
cho Heretic năm 1994
và Hexen năm 1995.

<!-- S89 -->
Doom góp phần định hình
một cách làm game mới.
Các studio có thể mua bản quyền một engine có sẵn,
thay vì tự xây mọi thứ từ đầu.

<!-- S90 -->
Một bộ mở rộng bộ nhớ.
Một thư viện âm thanh.
Một engine được cấp phép.

<!-- S91 -->
Mỗi thứ gỡ bớt một vấn đề
khỏi tay lập trình viên.
Và các lớp cứ thế tăng lên,
thành những engine
mà lập trình viên ngày nay dùng để bắt đầu.

<!-- S92 -->
Vậy hồi đó làm game có khó hơn không?
Theo nhiều cách, có.

<!-- S93 -->
Nhưng độ khó không biến mất.
Nó chỉ dời chỗ.

<!-- S94 -->
Ngày nay, lập trình viên vật lộn
với hàng gigabyte tài nguyên
và hàng triệu đa giác,
thay vì vài trăm kilobyte.

<!-- S95 -->
Trên DOS, ngay cả người chơi
cũng phải biết bộ nhớ của mình đi đâu.

<!-- S96 -->
Vậy đây là câu hỏi dành cho bạn.
Bạn có nhớ đã từng dựng
một menu khởi động chỉ để chạy được một trò chơi?
Đó là một cực hình,
hay là một nửa niềm vui?
Hãy cho mình biết trong phần bình luận.
