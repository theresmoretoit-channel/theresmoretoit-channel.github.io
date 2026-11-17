# Internet Explorer 6 — Những lỗi có tên riêng

<!-- S01 -->
Đây là phần hai.

Nếu bạn chưa xem phần một,
link ở dưới.

Nhưng đây là bản tóm tắt.

<!-- S02 -->
Năm 2001
Microsoft phát hành
Internet Explorer 6,
và nó đi kèm Windows XP.

Chỉ trong vài năm
nó chiếm hơn chín mươi phần trăm
thị trường trình duyệt.

<!-- S03 -->
Microsoft dùng điều đó
để biến trình duyệt
thành một nền tảng ứng dụng.

Đó là một ý tưởng thật sự.

Chỉ là người trả giá
tình cờ lại là dân lập trình web.

<!-- S04 -->
Đó là phần một.

Nhưng tôi đã bỏ sót một thứ.

Tôi đã bỏ sót đoạn
mà những con lỗi có tên riêng.

<!-- S05 -->
Bình thường một lỗi trình duyệt
là một con số trong hệ theo dõi.

Issue bốn một bảy hai.

Chẳng ai nhớ nó.

Chẳng ai nhắc tới nó trong bữa trưa.

<!-- S06 -->
Trong Internet Explorer 6
những con lỗi có danh từ riêng.

Và hóa ra đó lại là điều
nói lên nhiều nhất
về cả thời kỳ ấy.

<!-- S07 -->
Bắt đầu bằng một cái nhẹ nhàng.

Bạn cho một tấm ảnh float sang trái
rồi đặt một đoạn văn bên cạnh.

Chữ lẽ ra phải nằm
ngay sát tấm ảnh.

Thay vào đó nó nằm
cách ra ba pixel.

<!-- S08 -->
Không phải bốn.

<!-- S08b -->
Không phải hai.

<!-- S08c -->
Ba.

<!-- S08d -->
Lần nào cũng thế.

Nó có một cái tên.

The Three Pixel Jog.

<!-- S09 -->
Giờ cho tấm ảnh ấy float sang trái
và cho nó lề trái
mười pixel.

Internet Explorer 6
cho nó hai mươi.

Nó nhân đôi cái lề,
nhưng chỉ ở phía
bạn đã float sang.

<!-- S10 -->
The Double Margin Bug.

Và cách sửa được chấp nhận
là khai báo một phần tử
đang float là inline.

<!-- S11 -->
Điều đó là vô nghĩa.

Float là một khối.

Gọi nó là inline
chẳng có nghĩa gì cả.

Nó chạy được, nên người ta cứ viết.

<!-- S12 -->
Cái tiếp theo còn hay hơn.

Bạn tải một trang,
và một phần nội dung
đơn giản là không có ở đó.

Bạn cuộn xuống.

Bạn cuộn ngược lên.

Và nó hiện ra.

<!-- S13 -->
Chẳng có gì được tải.

Chẳng có gì thay đổi.

Nó chỉ là nhút nhát thôi.

Và nó có cái tên rất đúng.

The Peekaboo Bug.

<!-- S14 -->
Cách chữa là bảo
phần tử bị mất
rằng vị trí của nó là relative.

Chẳng ai giải thích nổi trọn vẹn
vì sao điều đó gọi nó về.

<!-- S15 -->
Rồi còn cái này:
bạn rê chuột lên một liên kết,
và nền của cái hộp
ngay bên dưới
bị cắt cụt theo một đường thẳng.

The Guillotine Bug.

<!-- S16 -->
Có một lỗi làm chữ
bò dần khỏi chỗ bạn đặt nó.

Magic Creeping Text.

Có một lỗi làm đường viền
hiện ra sai chỗ,
sai màu,
hoặc không hiện gì cả.

Border Chaos.

<!-- S17 -->
Cái tôi thích nhất thì lặng lẽ hơn.

Bạn xếp một hàng hộp,
và các chữ cái từ hộp cuối
lại xuất hiện thêm lần nữa bên dưới nó.

Không phải lúc nào cũng vậy.

Không đoán trước được.

The Duplicate Character Bug.

<!-- S18 -->
Và thứ quyết định việc nó
có xảy ra với bạn hay không,
và bao nhiêu chữ cái
bị nhân đôi,
lại là số lượng chú thích HTML
bạn để lại trong mã.

Chú thích.

Thứ duy nhất trong tệp
mà trình duyệt lẽ ra
phải vứt đi.

<!-- S19 -->
Còn một cái nữa,
và nó khác,
vì người ta dùng nó
một cách cố ý.

Nếu bạn đặt chiều cao
mà nội dung cao hơn,
cái hộp lẽ ra phải tràn.

Internet Explorer 6
thì lại phình cái hộp ra.

<!-- S20 -->
Điều đó là sai.

Nó cũng đúng y hệt
cái mà chiều cao tối thiểu làm.

Và Internet Explorer 6
không có chiều cao tối thiểu.

Nên lập trình viên thôi
báo lỗi cái đó
và bắt đầu dựa vào nó.

<!-- S21 -->
Dừng lại và nhìn cái danh sách ấy.

The Three Pixel Jog.

The Double Margin Bug.

Peekaboo.

The Guillotine.

Bạn không đặt tên cho một con lỗi
mà bạn chỉ gặp một lần.

<!-- S22 -->
Những cái này có tên
vì ai cũng gặp chúng.

Và đây là phần
khiến chuyện còn tệ hơn.

Phần lớn chúng có
cùng một nguyên nhân bên dưới.

<!-- S23 -->
Bên trong Internet Explorer 6,
mỗi phần tử hoặc là có
hoặc là không có
một thứ gọi là layout.

<!-- S24 -->
Nó quyết định phần tử ấy
tự định kích thước và vị trí,
hay để việc đó cho phần tử cha.

Và bạn không đặt được nó.

<!-- S25 -->
Không có thuộc tính nào
tên là layout,
và không có cách nào yêu cầu nó.

Nó không nằm trong bất kỳ đặc tả nào.

Nó là một cờ nội bộ
trong bộ máy render.

<!-- S26 -->
Nhưng bạn có thể bật nó
một cách vô tình.

Đặt chiều rộng là bật.

Đặt chiều cao là bật.

Cho một phần tử float là bật.

Nên một nửa số cách sửa trong video này
là những người đang bật một cái công tắc
mà họ không nhìn thấy.

<!-- S27 -->
Đó là lý do họ đi tìm
cách rẻ nhất
để bật nó một cách cố ý.

Một cách là đặt chiều cao
bằng một phần trăm.

<!-- S28 -->
Mọi trình duyệt khác
phải được giữ tránh xa thứ đó,
nên nó chui vào trong một hack
mà lát nữa ta sẽ nói tới.

<!-- S29 -->
Và trong Internet Explorer 6
nó chẳng gây hại gì,
vì nếu nội dung không vừa
thì nó cũng tự phình cái hộp ra.

Chính con lỗi từ hai phút trước
đã khiến cách sửa ấy an toàn.

<!-- S30 -->
Nó có một cái tên.

The Holly Hack.

<!-- S31 -->
Cách còn lại
là một thuộc tính của Microsoft
tên là zoom, đặt bằng một.

Zoom bằng một nghĩa là
đừng phóng to.

<!-- S32 -->
Nó chẳng thay đổi gì mà bạn thấy được.

Đó chính là điểm mấu chốt.

Nó nằm trong bảng kiểu
thuần túy để bật
một cái cờ vô hình
làm các con lỗi biến mất.

<!-- S33 -->
Điều đó đưa ta tới các hack,
và các hack chính là chỗ
mọi thứ trở nên kỳ quặc.

Để sửa một trình duyệt
trước hết bạn phải nói chuyện
riêng với đúng trình duyệt đó.

<!-- S34 -->
Và Internet Explorer 6
hành xử như thể có
một phần tử khác
nằm trên cả phần tử html.

Không trình duyệt nào khác làm vậy.

Chuyện đó không được ghi trong tài liệu nào.

Nó chỉ đơn giản là hành xử thế.

<!-- S35 -->
Nên bạn viết một quy tắc
khớp với cái bóng ma ấy,
và chỉ trình duyệt đó
nhìn thấy nó.

Dấu sao, dấu cách, html.

<!-- S36 -->
Mọi trình duyệt khác nhìn vào đó,
không thấy gì khớp,
rồi đi tiếp.

Đó là star hack,
và suốt nhiều năm nó nằm
trong gần như mọi bảng kiểu
trên web.

<!-- S37 -->
Còn có
underscore hack.

Bạn đặt một dấu gạch dưới
trước tên thuộc tính.

<!-- S38 -->
Một trình duyệt tuân thủ chuẩn
vứt dòng ấy đi
vì không hợp lệ.

Internet Explorer 6
bỏ qua dấu gạch dưới
rồi áp dụng nó.

<!-- S39 -->
Nghĩa là bạn cố tình làm hỏng
bảng kiểu của chính mình,
và chỗ hỏng ấy
chính là câu lệnh.

<!-- S40 -->
Và rồi còn cái mà
Microsoft dựng nên một cách cố ý.

Bạn có thể viết một chú thích
mà chỉ Internet Explorer nghe theo.

<!-- S41 -->
Với mọi trình duyệt khác
nó là một chú thích bình thường,
bị bỏ qua như mọi chú thích.

Với Internet Explorer 6
nó là một cánh cửa
dẫn vào phiên bản thứ hai
của trang.

<!-- S42 -->
Nghĩa là nhà cung cấp
nhìn vào tình hình,
đồng ý rằng trình duyệt này
cần một bảng kiểu riêng,
rồi phát hành hẳn một tính năng
để việc đó dễ hơn.

<!-- S43 -->
Một phần thiệt hại
thậm chí chẳng cần con lỗi nào.

Internet Explorer 6
có hai chế độ.

Ở chế độ hiện đại
nó theo đúng chuẩn.

<!-- S44 -->
Ở chế độ cũ,
chiều rộng của một hộp
bao gồm cả padding
và đường viền của nó,
tức là một con số
hoàn toàn khác.

<!-- S45 -->
Bạn rơi vào chế độ nào
phụ thuộc vào dòng đầu tiên
của tài liệu.

Và phiên bản HTML
mà mọi người đang chuyển sang
lại bảo bạn đặt
một khai báo XML ở đó.

<!-- S46 -->
Dòng ấy đẩy
Internet Explorer 6
về chế độ cũ.

Chính việc tuân theo chuẩn mới hơn
là thứ làm nó hỏng.

<!-- S47 -->
Rồi tới chuyện trong suốt.

Internet Explorer 6 không thể
hiện một tấm PNG có viền mềm.

Chỗ lẽ ra ảnh phải mờ dần,
nó bôi màu xám.

<!-- S48 -->
Câu trả lời của Microsoft là một bộ lọc
có cái tên nghe như số sê-ri.

Nó chạy được.

<!-- S49 -->
Nhưng nó vẽ ở ngoài
quy trình render bình thường
của trình duyệt,
nên các liên kết bạn đặt lên trên
thường ngừng hoạt động.

Bạn sửa được tấm ảnh
và làm hỏng cái liên kết.

<!-- S50 -->
Còn làm mờ bất cứ thứ gì khác
lại là một bộ lọc thứ hai,
với cú pháp riêng của nó,
nằm trong bảng kiểu
ngay cạnh cái thuộc tính bình thường
mà mọi trình duyệt khác đều hiểu.

<!-- S51 -->
Một phần chuyện này
còn có trước cả đám lỗi kia.

Trước tất cả những thứ đó,
bố cục được dựng
bằng các bảng lồng nhau.

<!-- S52 -->
Và để giữ một khoảng trống,
bạn dùng một tấm ảnh trong suốt
rộng đúng một pixel,
kéo giãn ra đúng cỡ
mà khoảng trống ấy cần.

Nó cũng có một cái tên.

The spacer gif.

<!-- S53 -->
Rê chuột là một chuyện khác.

Trong Internet Explorer 6,
hover chạy trên các liên kết.

Chỉ trên liên kết.

<!-- S54 -->
Nên một menu bung ra
khi bạn rê chuột
lên bất cứ thứ gì khác
sẽ cần một chương trình nhỏ
gắn vào bảng kiểu.

<!-- S55 -->
Không phải một script trong trang.

Một tệp riêng,
được tham chiếu từ CSS,
chứa đoạn mã mà việc của nó
là dạy trình duyệt
đúng một bộ chọn.

Người ta chuyền tay nhau tệp ấy
suốt nhiều năm.

<!-- S56 -->
Phần một có nhắc rằng
bạn có thể nhét JavaScript
vào trong một bảng kiểu.

Cái nó không nhắc
là JavaScript ấy chạy thường xuyên đến mức nào.

<!-- S57 -->
Mỗi lần chuột di chuyển.

Mỗi lần gõ phím.

Mỗi lần cuộn.

Lặp đi lặp lại,
chỉ để tính ra một chiều rộng.

<!-- S58 -->
Và trình duyệt ấy có những giới hạn
mà các trình duyệt khác không có.

Một bảng kiểu ngừng có tác dụng
ở đâu đó sau
bốn nghìn quy tắc.

Bất cứ thứ gì sau
bảng kiểu thứ ba mươi mốt
trên một trang đều bị bỏ qua.

<!-- S59 -->
Nghe như một con số
bạn chẳng bao giờ chạm tới,
cho tới khi trang của bạn đủ lớn
để ai đó phải viết
một bước build mà việc duy nhất
là gộp các bảng kiểu lại
trước khi trình duyệt nhìn thấy chúng.

<!-- S60 -->
Và một phần trong đó
chẳng hề là chuyện thẩm mỹ.

Internet Explorer 6
đếm các đối tượng của trang
và các đối tượng của script
theo hai cách khác nhau,
và không bên nào
nhìn thấy trọn vòng tham chiếu.

<!-- S61 -->
Nên nếu một script trỏ
tới một phần của trang,
và phần trang ấy
trỏ ngược lại script,
thì chẳng cái nào được giải phóng.

Cứ để cửa sổ đó mở đủ lâu
là trình duyệt ăn sạch cái máy.

<!-- S62 -->
Nhưng cái hay nhất
lại chẳng phải lỗi bố cục.

Bạn viết một thẻ input.

Bạn cho nó một type.

Và bạn quên dấu bằng.
<!-- S63 -->
Đó là một thuộc tính dị dạng.

Mọi bộ phân tích cú pháp từng được viết
đều có cách xử lý chuyện đó.

Bỏ qua nó.

Đoán xem bạn định viết gì.

Đi tiếp.
<!-- S64 -->
Internet Explorer sập.

Bên trong, nó muốn biết
trường ấy có bị ẩn không,
nên nó đem thứ bạn gõ
so với chữ hidden.

Mà bạn có gõ gì đâu.
<!-- S65 -->
Thế là nó đi lấy
cái thứ bạn không gõ
từ địa chỉ số không.

Lẽ ra đó chỉ là
một cú sập trình duyệt bình thường,
trừ chuyện đoạn mã làm việc đó
không nằm trong trình duyệt.
<!-- S66 -->
Nó nằm trong một thư viện hệ thống dùng chung.

Nên ba chữ ấy
cũng hạ luôn trình đọc thư,
và khung xem trước
trong trình quản lý tệp.
<!-- S67 -->
Một cửa sổ đang liệt kê tệp
trên chính máy của bạn,
bị một trang web đóng sập.

Đó là luận điểm của phần một
gửi tới dưới dạng báo cáo sự cố.

Trình duyệt không phải một chương trình
chạy trên hệ thống.

Nó là một phần của hệ thống.
<!-- S68 -->
Và bạn không thể cứ thế
đem bản vá đi thử ở chỗ khác.

Internet Explorer bị hàn chết
vào hệ điều hành,
nên một cái máy
chạy đúng một phiên bản.

<!-- S69 -->
Đó là lý do một công việc front end
vào năm 2006
đi kèm cả một giá
đầy máy dự phòng.

<!-- S70 -->
Và về sau là cả một thư mục
đầy máy ảo,
mỗi cái cõng nguyên
một hệ điều hành
chỉ để mở được
một trang web bên trong.

<!-- S71 -->
Rồi có người làm
cái điều hiển nhiên.

Nếu bạn dạy được trình duyệt
một tính năng còn thiếu,
bạn dạy được nó tất cả.

<!-- S72 -->
Một lập trình viên tên Dean Edwards
viết một thư viện
mà toàn bộ mục đích
là khiến Internet Explorer 6
hành xử như một phiên bản
sau này của chính nó.

Và người ta đem nó đi dùng.

Trên production.

<!-- S73 -->
Đó là lúc chuyện này thôi
còn buồn cười.

Suốt gần một thập kỷ,
một phần đáng kể công việc
front end của cả thế giới đổ vào
những sai lầm của một trình duyệt.

Không phải tính năng.

Không phải sản phẩm.

Mà là bù trừ.

<!-- S74 -->
Và nó kéo dài được là nhờ
đúng cái điều mà phần một nói tới.

Các công ty đã dựng
những ứng dụng thật trên nó,
loại chỉ chạy được ở đó,
và thứ Hai tuần sau
chúng vẫn phải chạy.

<!-- S75 -->
Nên cái trình duyệt mà ai cũng
muốn nó biến mất
lại chính là cái không ai
được phép gỡ đi.

<!-- S76 -->
Năm 2010,
Google tuyên bố các ứng dụng
của chính họ sẽ ngừng chạy trên nó.

Và một studio thiết kế ở Denver
quyết định chuyện đó đáng có một đám tang.

<!-- S77 -->
Một đám tang thật.

Một cỗ quan tài.

Một bài điếu văn.

Từ tám mươi tới một trăm người
đã tới xem một trình duyệt
được chôn.

Họ chỉ dự tính ba mươi người.

<!-- S78 -->
Và Microsoft gửi hoa.

Tấm thiệp viết:
cảm ơn vì những ngày tháng đẹp,
Internet Explorer 6.

<!-- S79 -->
Đúng một năm sau, đúng ngày đó,
Microsoft mở một trang web.

Nó theo dõi tỷ lệ người dùng trên thế giới
vẫn còn đang chạy
Internet Explorer 6,
theo từng quốc gia.

<!-- S80 -->
Vào thời điểm ấy
con số vẫn là mười hai phần trăm.

Mục tiêu là đẩy nó
xuống dưới một.

Chính công ty làm ra trình duyệt ấy
đang chạy một đồng hồ đếm ngược công khai
tới cái chết của sản phẩm mình.

<!-- S81 -->
Vậy tại sao những con lỗi lại có tên?

Bởi bạn đặt tên cho những thứ
bạn không thể đi vòng tránh.

<!-- S82 -->
Chẳng ai đặt tên cho thời tiết
ở một đất nước
mà mình chỉ đi ngang qua.

Bạn đặt tên ở nơi mình sống.

Và suốt chừng mười năm,
đó là nơi web đã sống.

<!-- S83 -->
Nhưng đẩy được Internet Explorer 6
ra khỏi web lại là một câu chuyện khác.

Và đó là chỗ ta sẽ tới tiếp.

Nếu bạn muốn nghe phần đó,
có một nút đăng ký,
và phần một có link ở dưới.
