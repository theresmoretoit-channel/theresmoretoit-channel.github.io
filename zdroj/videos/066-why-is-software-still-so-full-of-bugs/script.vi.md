<!-- S01 -->
Cứ vài ngày, lại một lỗi nghiêm trọng nữa
lên tin tức.
Một lỗi cho phép ai đó bỏ qua bước đăng nhập.
Một lỗi làm rò rỉ dữ liệu riêng tư.
Một lỗi trao máy tính của bạn cho kẻ tấn công.

<!-- S02 -->
Đôi khi là Windows. Đôi khi là Linux.
Một trình duyệt, một cơ sở dữ liệu, một dịch vụ đám mây...
hoặc một thư viện nhỏ
mà hàng triệu lập trình viên phụ thuộc vào.

<!-- S03 -->
Và phản ứng hầu như luôn giống nhau.
Sao các lập trình viên lại bỏ sót điều này?

<!-- S04 -->
Họ là những người chuyên nghiệp.
Họ có rà soát mã, kiểm thử tự động,
kiểm toán an ninh, fuzzing...
mà lỗi vẫn cứ xuất hiện.

<!-- S05 -->
Vậy liệu có thể nào
viết phần mềm phức tạp mà không có lỗi?

<!-- S06 -->
Hãy bắt đầu bằng một con số.
Hình dung một chương trình chỉ với một trăm tùy chọn,
mỗi cái hoặc bật hoặc tắt.

<!-- S07 -->
Một trăm quyết định có-hoặc-không đơn giản.
Đó là bao nhiêu tổ hợp?

<!-- S08 -->
Hai lũy thừa một trăm.
Tức là khoảng một triệu nghìn tỷ nghìn tỷ.

<!-- S09 -->
Giờ hình dung bạn có thể thử
một tỷ tổ hợp mỗi giây.
Và bạn bắt đầu từ vụ Big Bang.

<!-- S10 -->
Đến hôm nay, bạn mới thử được
khoảng một tổ hợp trong ba nghìn.

<!-- S11 -->
Và một trăm công tắc chẳng là gì.
Một chương trình thật có hàng triệu cái.
Nên "cứ thử hết đi"
không phải là tốn kém. Mà là bất khả thi.

<!-- S12 -->
Và những công tắc đó chẳng có gì kỳ lạ.
Hãy lấy một trong những việc đơn giản nhất
mà một chương trình từng làm.
Người dùng hỏi tài khoản của mình theo số của nó.
Ta tìm nó trong cơ sở dữ liệu.
Ta gửi lại cho họ.

<!-- S13 -->
Nhưng nếu người dùng không tồn tại thì sao?
Nếu ai đó gửi chữ thay vì một con số thì sao?
Hay một số âm? Hay một số khổng lồ?

<!-- S14 -->
Nếu người này không được phép xem nó thì sao?
Nếu ai đó xóa tài khoản
ngay đúng lúc ta đang nạp nó thì sao?
Nếu cùng một yêu cầu đến hai lần thì sao?

<!-- S15 -->
Mỗi câu hỏi này đều đơn giản.
Vấn đề là chúng kết hợp với nhau ra sao.
Mỗi câu là thêm một công tắc.

<!-- S15b -->
Nhân tiện, nếu bạn thích những video
như thế này, bạn có thể đăng ký kênh.

Như vậy sẽ giúp kênh rất nhiều.

<!-- S16 -->
Và một máy tính sẽ không dàn xếp giúp ta.
Nó làm đúng chính xác điều ta bảo.
Không phải điều ta muốn nói.

<!-- S17 -->
Đó là lý do ta phát minh ra các ngôn ngữ lập trình.
Chúng cho ta mô tả những điều phức tạp
mà không cần nghĩ đến từng chi tiết.

<!-- S18 -->
Nhưng vài ngôn ngữ lo liệu ít hơn
bạn mong đợi.
Lấy C làm ví dụ. Nó nhanh, nó đơn giản,
và cho bạn quyền kiểm soát bộ nhớ cực lớn.

<!-- S19 -->
Nên bạn có thể viết thế này.
Ta dành chỗ cho mười sáu ký tự.
Rồi ta bảo: chép dữ liệu vào đây.

<!-- S20 -->
Nếu dữ liệu vào
dài năm trăm ký tự thì sao?
C sẽ không hỏi.
Nó cứ thế ghi tiếp, vượt qua điểm cuối.

<!-- S21 -->
Và ngay sau mười sáu ký tự đó là gì?
Thường là một thứ rất quan trọng.

<!-- S22 -->
Khi một chương trình gọi một hàm,
nó ghi lại nơi cần quay về
một khi hàm chạy xong.
Một địa chỉ trả về.
Với cách bố trí bộ nhớ truyền thống, nó nằm
cách cuối vùng đệm của ta không xa.

<!-- S23 -->
Thế là kẻ tấn công gửi một dữ liệu vào
có độ dài chính xác vừa vặn.
Trước hết, là các lệnh của chính hắn.
Rồi, ở tận cuối, một địa chỉ trả về mới...
trỏ ngược về chính những lệnh đó.

<!-- S24 -->
Hàm kết thúc.
Bộ xử lý tra xem cần quay về đâu...
và nhảy thẳng vào mã của kẻ tấn công.

<!-- S25 -->
Giờ nó đang chạy chương trình của hắn,
với toàn bộ quyền của chương trình của bạn.
"Thực thi mã tùy ý" nghĩa là như vậy.

<!-- S26 -->
Và bộ xử lý chẳng làm gì sai.
Nó đã làm theo các lệnh.

<!-- S27 -->
Năm 1988, một sai lầm y hệt thế này
đã để sâu Morris lan
khắp internet thời đầu.
Và cũng chiêu trò ấy vẫn được dùng
trong các cuộc tấn công kể từ đó.

<!-- S28 -->
Nên các ngôn ngữ mới hơn giao một phần việc
cho trình biên dịch.
Rust, chẳng hạn, từ chối biên dịch
nhiều chương trình có thể sử dụng bộ nhớ sai cách.

<!-- S29 -->
Lập trình viên nói:
nhưng tôi biết chính xác mình đang làm gì!
Và trình biên dịch nói:
ai cũng nói thế cả.

<!-- S30 -->
Và nó có lý khi nghi ngờ.
Microsoft và nhóm Chrome của Google
cả hai đều báo cáo
rằng khoảng bảy mươi phần trăm
số lỗi an ninh họ nghiên cứu
đến từ các vấn đề an toàn bộ nhớ.

<!-- S31 -->
Nhưng một chương trình có thể an toàn bộ nhớ hoàn hảo
mà vẫn hoàn toàn sai.

<!-- S32 -->
Hình dung một người dùng đăng nhập.
Mật khẩu của họ được kiểm tra đúng đắn.
Không gì sập cả. Không bộ nhớ nào hỏng.

<!-- S33 -->
Rồi chương trình lại cho họ xem
dữ liệu của người khác.
Bởi phần kiểm tra quyền
đã bị viết hơi sai.

<!-- S34 -->
Không ngôn ngữ nào tự bắt được điều đó.
Ngôn ngữ không biết
chương trình lẽ ra phải làm gì.
Chỉ chúng ta biết điều đó.

<!-- S35 -->
Vậy quay lại chuyện kiểm thử.
Một bài kiểm thử có thể cho bạn biết:
với dữ liệu vào này, tôi nhận được kết quả này.

<!-- S36 -->
Nó không thể cho bạn biết:
chương trình đúng với mọi dữ liệu vào.
Và ta đã thấy
vì sao ta không thể thử hết tất cả.

<!-- S37 -->
Năm 1970, nhà khoa học máy tính
Edsger Dijkstra gói gọn nó trong một câu.
Kiểm thử có thể cho thấy sự hiện diện của lỗi,
nhưng không bao giờ cho thấy sự vắng mặt của chúng.

<!-- S38 -->
Được. Vậy thay vì kiểm thử,
sao không viết một chương trình
kiểm tra các chương trình khác
và chứng minh chúng đúng?
Đưa cho nó bất kỳ đoạn mã nào, và nó cho biết
đoạn mã đó có làm đúng điều nó phải làm không.

<!-- S39 -->
Câu hỏi đó đã có lời đáp
trước cả khi chiếc máy tính thật đầu tiên được chế tạo.
Năm 1936, Alan Turing đã chứng minh
rằng một chương trình như thế không thể tồn tại.

<!-- S40 -->
Không phải chưa ai xây được nó.
Mà là nó không thể tồn tại chút nào.

<!-- S41 -->
Ông chỉ ra rằng không chương trình nào có thể quyết định,
với mọi chương trình khác,
liệu nó có bao giờ dừng chạy hay không.

<!-- S42 -->
Và năm 1953, Henry Rice còn đi xa hơn.
Điều tương tự đúng với mọi câu hỏi không tầm thường
về việc một chương trình thực sự làm gì.

<!-- S43 -->
Nó có an toàn không? Có rò rỉ dữ liệu không?
Có cho ra đáp án đúng không?
Không có phương pháp tổng quát nào
giải quyết điều đó cho mọi chương trình.

<!-- S44 -->
Vậy phần mềm không lỗi là bất khả thi?
Không hẳn.
Với một chương trình cụ thể,
đôi khi bạn có thể chứng minh nó đúng,
bằng một nỗ lực khổng lồ.

<!-- S45 -->
Năm 2009, một nhóm ở Úc đã chứng minh
rằng một nhân hệ điều hành nhỏ,
tên là seL4,
làm đúng chính xác điều đặc tả của nó nói.

<!-- S46 -->
Nó có dưới mười nghìn dòng mã.
Xây dựng cái nhân đó mất
khoảng hai người-năm.
Chứng minh nó đúng mất khoảng hai mươi.
Một trình duyệt web hiện đại
có hàng chục triệu dòng.

<!-- S47 -->
Và ngay cả chứng minh đó cũng có một điểm gợn.
Nó cho thấy chương trình khớp với đặc tả của nó.
Nó không thể cho thấy rằng đặc tả
đúng là điều ta thực sự muốn.

<!-- S48 -->
Và đặc tả là do con người viết.
Nên câu hỏi lại quay về với ta.

<!-- S49 -->
Và đâu chỉ là mã của riêng ta.
Một lập trình viên hôm nay dựng trên các framework,
thư viện và hàng trăm thành phần phụ thuộc.
Mỗi lớp giúp ta đỡ đi khối lượng công việc khổng lồ.
Nhưng mỗi lớp là một thứ
ta phải hiểu...
hoặc ít nhất phải tin.

<!-- S50 -->
Nghĩa là bạn không cần phải viết ra một lỗi
để có nó trong phần mềm của mình.
Bạn chỉ cần cài đặt nó.

<!-- S51 -->
Rồi thêm áp lực vào.
Không ai muốn một sản phẩm hoàn hảo sau mười năm.
Họ muốn một cái chạy được vào tháng sau.
Và một vụ đột nhập chưa từng xảy ra
thì rất khó trưng ra trong một buổi thuyết trình.

<!-- S52 -->
Và đây là phần lạ lùng nhất.
Công cụ của ta cứ ngày một tốt hơn.
Ngôn ngữ an toàn hơn, fuzzing, tiền thưởng cho việc phát hiện lỗ hổng...

<!-- S53 -->
Ấy vậy mà số lỗ hổng đã biết
vẫn cứ tăng.
Chỉ riêng năm 2024, khoảng bốn mươi nghìn
đã nhận được một số hiệu chính thức.

<!-- S54 -->
Một phần vì ta cũng đang viết
nhiều phần mềm hơn trước rất nhiều.
Giống như làm mọi con đường an toàn hơn...
trong khi xây thêm hàng triệu lần số đường.

<!-- S55 -->
Vậy lập trình viên kém cỏi trong nghề của họ sao?
Không.
Ta bấy lâu đòi hỏi ở họ một điều
mà không phương pháp tổng quát nào bảo đảm được.

<!-- S56 -->
Nên có lẽ
"làm sao viết phần mềm không lỗi?"
là câu hỏi sai.

<!-- S57 -->
Câu hỏi hay hơn là:
làm sao dựng những hệ thống vẫn an toàn
ngay cả khi phần mềm có lỗi?

<!-- S58 -->
Và đó chính là hướng an ninh đang đi.
Nó không nói: đừng bao giờ mắc lỗi.
Nó nói: hãy giả định rằng bạn đã mắc rồi.

<!-- S59 -->
Còn nhớ cái địa chỉ trả về đó chứ?
Ngày nay, hệ thống canh giữ nó.
Nó xáo trộn vị trí mọi thứ trong bộ nhớ.
Và nó từ chối chạy những lệnh
giấu trong dữ liệu.

<!-- S60 -->
Lỗi trong mã C của ta vẫn còn đó.
Chỉ là biến nó thành một cuộc tấn công khó hơn nhiều.

<!-- S61 -->
Và cũng ý tưởng ấy có mặt khắp nơi.
Hộp cát, quyền hạn giới hạn,
tiến trình cô lập, mã hóa,
sao lưu, giám sát...
lớp này chồng lớp kia,
để một lỗi không thành thảm họa.

<!-- S62 -->
Và điều đó có một hệ quả rất thực tế.
Nếu lỗi là không tránh khỏi,
thì sửa chúng không phải chuyện tùy chọn.

<!-- S63 -->
Phần mềm bạn đang dùng hôm nay
rất có thể chứa một lỗ hổng
mà chưa ai tìm ra.

<!-- S64 -->
Và khi có ai đó tìm ra,
bản cập nhật là khác biệt giữa
"một lỗ hổng đã được phát hiện"
và "hệ thống của chúng ta đã bị xâm nhập".

<!-- S65 -->
Điều tương tự đúng với các hệ thống ta dựng.
Thư viện cũ và nền tảng không còn được hỗ trợ
không an toàn hơn nhờ bị làm ngơ.
Chúng biến thành nợ kỹ thuật.

<!-- S66 -->
Còn vì sao món nợ đó phải được trả,
video của tôi
"Nó vẫn chạy mà. Vậy nâng cấp làm gì?"
nói đúng về điều đó.

<!-- S67 -->
Bởi trong phần mềm,
"nó vẫn chạy"
và "nó vẫn an toàn"
là hai điều rất khác nhau.
