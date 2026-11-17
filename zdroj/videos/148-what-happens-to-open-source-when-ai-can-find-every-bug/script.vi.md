<!-- S01 -->
948.
Đó là số cách khác nhau mà một AI đã tìm ra
để chiếm quyền một máy tính Linux từ bên trong.

<!-- S02 -->
Không có mật khẩu bị đánh cắp. Không có đột nhập từ xa.
Mỗi cách đều bắt đầu từ một người dùng bình thường
không có quyền đặc biệt nào,
và kết thúc với root,
tài khoản có thể làm mọi thứ.

<!-- S03 -->
OpenAI công bố kết quả vào tháng 11 năm 2026.
Toàn bộ đợt chạy tốn
1,2 triệu đô la tiền tín dụng API.

<!-- S05 -->
Đây là số liệu của chính OpenAI,
được công bố một ngày trước khi
họ ra mắt mô hình đã tạo ra chúng,
và chưa ai bên ngoài xác nhận toàn bộ con số.
Nhưng hàng trăm báo cáo và bản vá
đã được gửi đi.

<!-- S06 -->
Đây là lý do chuyện này quan trọng không chỉ với Linux.
Mã nguồn Linux là công khai.
Ai cũng có thể đọc.
Suốt nhiều thập kỷ, người ta dựa vào đó
để nói rằng Linux an toàn.

<!-- S07 -->
Vậy nếu một cỗ máy có thể đọc mã công khai
và biến nó thành mã khai thác hoạt động được ở quy mô này,
thì rốt cuộc phần mềm có nên giữ bí mật mã của mình không?

<!-- S08 -->
Hãy xem phần mềm vốn đã làm vậy.
Tháng 4 năm 2026, Microsoft đã sửa
164 lỗ hổng bảo mật
trong ngày vá lỗi hằng tháng.
Đến tháng 10, họ sửa
1.413.

<!-- S09 -->
Chỉ riêng tháng đó, họ đã sửa nhiều hơn
trong bất kỳ năm nào trước đó.
Hơn 1.000 bản sửa trong số đó là cho Windows,
và Microsoft từng cảnh báo
rằng chính các công cụ AI của họ sẽ đẩy con số này lên.

<!-- S10 -->
Bạn không thể so sánh trực tiếp hai con số này.
Mỗi công ty đếm theo cách khác nhau,
và Microsoft đang dò trong mã nguồn đóng của chính mình.

<!-- S11 -->
Nhưng nó cho thấy một điều.
Giữ kín mã nguồn
cũng không ngăn được lỗi tồn tại trong đó.

<!-- S12 -->
Vậy điều gì thực sự bảo vệ bạn?
Để trả lời,
ta cần xem cỗ máy này hoạt động thế nào,
vì mỗi bước của nó đều loại bỏ một thứ gì đó.

<!-- S13 -->
Nhân Linux có
hơn 40 triệu dòng mã.
Đầu tiên, các tác tử trinh sát đã rà qua nó
và chọn ra những phần
mà một người dùng bình thường thực sự chạm tới được.

<!-- S14 -->
Còn lại khoảng 7%.
Đó là phần họ cho là đáng tấn công,
không phải một mẫu ngẫu nhiên,
nên bạn không thể nhân kết quả lên 14 lần.

<!-- S15 -->
Tiếp theo, các tác tử phân tích đã xem xét phần mã đó
và liệt kê mọi thứ đáng ngờ.
2.308 trường hợp nghi có lỗi,
trong 12 giờ.

<!-- S16 -->
Nhưng nghi ngờ thì chẳng chứng minh được gì.
Vì vậy các tác tử khác viết chương trình thử nghiệm
và chạy chúng trên các máy ảo cô lập.
1.724 lỗi
hóa ra là có thật.

<!-- S17 -->
Rồi đến phần tốn kém:
xây dựng mã khai thác hoạt động được,
khi các lớp bảo vệ tiêu chuẩn
của một hệ thống máy tính để bàn bình thường đều đang bật.
1.169
đã chiếm được root.

<!-- S18 -->
Gộp chúng lại theo lỗ hổng gốc,
và bạn có con số 948.

<!-- S19 -->
Có một chi tiết trong báo cáo
thật khó quên.
Trong một đợt chạy ban đầu,
các tác tử báo cáo 200 lần thành công.
Rồi con người kiểm tra xem chúng đã làm được bằng cách nào.

<!-- S20 -->
Hai mươi trong số đó đã chiếm được root
qua một lỗi khác chưa ai biết,
chứ không phải lỗi chúng được giao sử dụng.
Được cử đi mở một cánh cửa,
chúng lại tìm ra một cánh cửa khác không ai hay biết.

<!-- S21 -->
Trong một mẫu các mã khai thác của mình,
OpenAI xác định được mười kỹ thuật khai thác
mà các chuyên gia bên ngoài chưa từng thấy.

<!-- S22 -->
Hồi tháng 7, một mô hình đời trước
đã tìm ra 166 lỗi loại này.
Sau ba tháng sửa lỗi,
mô hình mới hơn tìm ra 948.
Lỗi vẫn chưa cạn.
Đợt chạy sau tìm ra nhiều hơn hẳn.

<!-- S23 -->
Nhưng có một giới hạn quan trọng.
Không thứ gì trong số này xâm nhập máy tính của bạn
qua internet.
Kẻ tấn công phải có mặt sẵn trên máy,
với tư cách người dùng bình thường.

<!-- S24 -->
Nghe vậy nhưng chưa thể yên tâm,
vì các cuộc tấn công thật thường gồm hai bước.
Trước hết là lọt vào,
qua một lỗi trình duyệt hoặc một tệp tải về độc hại.
Sau đó cần có root.
Đây chính là bước thứ hai.

<!-- S25 -->
Lời khuyên của OpenAI rất thẳng thắn.
Trên một hệ thống chưa có các bản vá mới nhất,
hãy coi mọi tài khoản bình thường như root,
ít nhất là trước một kẻ tấn công có nhiều tiền bạc.

<!-- S26 -->
Vậy lập luận cũ ủng hộ mã nguồn mở
giờ còn đứng vững đến đâu?
Vào cuối thập niên chín mươi,
Eric Raymond đã đặt cho nó một khẩu hiệu:
"Có đủ nhiều con mắt, mọi lỗi đều lộ rõ."

<!-- S27 -->
Ông gọi đó là Định luật Linus.
Một ý tưởng đẹp, nhưng ẩn bên trong là một giả định:
rằng thực sự có ai đó đang nhìn.

<!-- S28 -->
Năm 2014, một lỗi tên là Heartbleed
xuất hiện trong OpenSSL,
đoạn mã bảo vệ một phần rất lớn của web.
Khoảng nửa triệu máy chủ bảo mật
được cho là đã bị phơi nhiễm.

<!-- S29 -->
Lỗi đó đã nằm trong mã công khai suốt hai năm.
Dự án nhận được
khoảng 2.000 đô la tiền quyên góp mỗi năm
và chỉ có một lập trình viên toàn thời gian.

<!-- S30 -->
Ai cũng có thể đọc nó.
Hầu như chẳng ai đọc.

<!-- S31 -->
Đó luôn là điểm yếu thật sự của mã nguồn mở.
Không phải quá nhiều con mắt nhìn vào mã. Mà là quá ít.

<!-- S32 -->
Và đó chính là phần mà AI thay đổi.
Một cỗ máy có thể quét không ngừng
và kiểm tra nhiều trường hợp nghi có lỗi hơn hẳn
so với sức một nhà nghiên cứu đơn độc.
Lời hứa cũ cuối cùng cũng được thực hiện,
cho tất cả mọi người, kể cả kẻ tấn công.

<!-- S33 -->
Vậy là giờ mã công khai thực sự được soi xét.
Giấu nó đi có giúp được gì không?

<!-- S34 -->
Một chương trình mã nguồn đóng vẫn phải chạy,
nên mã máy của nó nằm
trên mọi máy tính sử dụng nó.
Các công cụ như Ghidra biến nó trở lại
thành thứ gần giống mã nguồn.

<!-- S35 -->
Và có một mẹo kinh điển.
Hãy so sánh một chương trình
trước và sau một bản cập nhật bảo mật.
Những gì thay đổi sẽ cho bạn thấy lỗ hổng nằm ở đâu.

<!-- S35b -->
Điều đó chỉ cho kẻ tấn công biết nên nhắm vào đâu,
từ rất lâu trước khi tất cả các hệ thống
kịp cài bản cập nhật.

<!-- S36 -->
Anthropic đã thử điều này với nhân Windows,
với 21 lỗ hổng
mà Microsoft vừa mới vá,
và không có mã nguồn.
AI gây ra sự cố treo máy đầu tiên sau 31 phút.
Trong vòng sáu giờ, nó đã có 18.

<!-- S37 -->
Tám cái trở thành mã khai thác hoạt động được,
có thể chiếm toàn quyền điều khiển máy,
với chi phí khoảng 2.000 đô la mỗi cái.

<!-- S38 -->
Nhưng đây không phải là những lỗi chưa ai biết.
Các bản vá đã chỉ sẵn
chỗ có vấn đề.
Tìm một lỗi mới từ con số không thì khó hơn.

<!-- S39 -->
Vậy nên việc giữ bí mật vẫn khiến kẻ tấn công tốn công.
Nó là một gờ giảm tốc, không phải bức tường.
Gờ đó cao đến đâu?
Không có con số công khai nào.

<!-- S40 -->
Còn phía bên kia thì sao?
Sự cởi mở thực sự đem lại cho bạn điều gì?
Câu trả lời nằm trong một chi tiết nhỏ
của báo cáo OpenAI.

<!-- S41 -->
Trong mười ngày quét và phân tích đó,
hơn 100 lỗi Linux trong số này
đã được người khác sửa,
hoặc sắp được sửa.
Khoảng 300 lỗi nữa
đã được thảo luận công khai.

<!-- S42 -->
Người khác cũng đang tìm ra những lỗi y hệt
cùng một lúc.

<!-- S43 -->
Linus Torvalds đã mô tả điều này từ tháng 5.
Ông nói các báo cáo từ AI
đã khiến danh sách thư bảo mật của nhân Linux
"gần như hoàn toàn không thể quản lý nổi",
vì nhiều người khác nhau cứ liên tục tìm ra
cùng những thứ bằng cùng những công cụ.

<!-- S44 -->
Và lời khuyên của ông là:
"Nếu bạn tìm ra một lỗi bằng công cụ AI,
thì rất có thể người khác cũng đã tìm ra nó."

<!-- S45 -->
Quy định của nhân Linux giờ nói thẳng điều đó.
Lỗi tìm được bằng AI phải được coi là công khai,
vì những lỗi này được
nhiều nhà nghiên cứu phát hiện độc lập,
thường là trong cùng một ngày.

<!-- S46 -->
Hãy nghĩ xem điều đó tác động thế nào
đến ý niệm về một lỗi bí mật.
Nếu bạn tìm ra nó với giá rẻ,
thì ai cũng tìm ra nó với giá rẻ.

<!-- S47 -->
Với mã nguồn mở,
ai cũng có thể xem báo cáo,
kiểm chứng bản sửa và phản bác kết quả.
Với phần mềm đóng,
bạn chủ yếu phải tin vào nhà cung cấp.

<!-- S49 -->
Nhưng sự cởi mở có cái giá của nó,
và đó không phải cái giá bạn nghĩ.
Người ta dễ cho rằng
một dự án nhỏ không đủ tiền để quét.
Các công ty AI đã và đang
cho những người duy trì dự án dùng miễn phí.

<!-- S50 -->
Thứ thiếu là con người.
Nhân Linux từng ghi nhận
khoảng 500 vấn đề bảo mật mỗi phiên bản.
Năm nay, con số đã vượt 1.500.
Nhiều vấn đề nhỏ,
nhưng vẫn phải có người xem xét chúng.

<!-- S51 -->
Vào tháng 1, dự án curl
đã chấm dứt chương trình thưởng tìm lỗi có trả tiền,
để thôi thưởng cho một làn sóng báo cáo rác.

<!-- S52 -->
Ngay cả báo cáo tốt cũng chỉ đẩy công việc sang bước sau.
Bản vá do AI tạo ra vẫn cần con người xem xét.
Một số bản sửa ban đầu thêm mã không cần thiết
hoặc bỏ sót các biến thể khác của cùng một lỗi.

<!-- S53 -->
Có tiền thì có thể quét thêm.
Nhưng tiền không mua thêm được những người
hiểu một đoạn mã kỹ đến thế.
Ở điểm này, một công ty có đội bảo mật được trả lương
thực sự có lợi thế.

<!-- S54 -->
Và rồi đến vấn đề cuối cùng.
Đã sửa không có nghĩa là đã cài.

<!-- S55 -->
Vào tháng 3 năm 2017,
Microsoft đã vá một lỗ hổng trong Windows.
Mã nguồn đóng, một nhà cung cấp, một hệ thống cập nhật.
Hai tháng sau,
WannaCry đã lọt qua đúng lỗ hổng đó,
vào khoảng 200.000 máy tính
ở khoảng 150 quốc gia.

<!-- S56 -->
Bản vá đó có hai tháng để lan rộng,
và vẫn không đủ.
Kẻ tấn công có thể không còn cho bạn hai tháng nữa.
Trong cùng nghiên cứu của Anthropic,
AI đã lấy một bản sửa công khai
cho bộ máy JavaScript của Firefox
và có mã khai thác hoạt động được trong chưa đầy một giờ.

<!-- S57 -->
Phiên bản Firefox đã được sửa
khi đó vẫn còn 18 ngày nữa mới ra.

<!-- S58 -->
Đây là mối nguy của việc công bố bản sửa.
Thông tin có thể đến tay kẻ tấn công
trước khi bản cập nhật đến được với bạn.

<!-- S59 -->
Một bản sửa của Linux phải đi một chặng đường dài,
từ nhân lên một phiên bản ổn định,
đến bản phân phối của bạn, đến thiết bị của bạn.
Một chiếc điện thoại có thể phải chờ hàng tháng, hoặc mãi mãi.

<!-- S60 -->
Và phần mềm đóng cũng không thoát được điều này.
Ta vừa thấy rồi: bản vá Windows là đủ.
Giờ mỗi bản cập nhật cũng là một tấm bản đồ.

<!-- S60b -->
Vì vậy hãy cập nhật mọi thứ,
máy tính, điện thoại, cả bộ định tuyến của bạn,
và cài bản cập nhật ngay khi chúng có.
Khi AI ngày càng giỏi biến bản sửa thành đòn tấn công,
mỗi ngày bạn chờ sẽ càng quan trọng hơn.

<!-- S61 -->
Vậy mã nguồn mở có còn an toàn hơn không?
Thành thật mà nói, chẳng ai biết.
Theo những gì được biết công khai,
chưa ai chạy cùng một bài kiểm tra cho cả hai phía,
theo cùng một luật chơi.

<!-- S62 -->
Điều ta có thể nói khiêm tốn hơn.
Giấu mã giờ mang lại ít hơn trước.
Công khai mã cho phép bất kỳ ai kiểm tra công việc,
và đẩy một đống việc lớn hơn
sang những người duy trì nó.

<!-- S64 -->
Kể cả khi AI không bao giờ tìm ra mọi lỗi,
nó đã thay đổi bài toán kinh tế của việc tìm lỗi.

<!-- S65 -->
Điều quan trọng bây giờ là một lỗ hổng còn mở trong bao lâu
giữa khoảnh khắc ai đó tìm ra nó
và khoảnh khắc nó được vá trên máy của bạn.

<!-- S66 -->
Vậy đây là một câu hỏi cho bạn.
Nếu bất kỳ lỗi nào cũng có thể bị bất kỳ ai tìm ra,
bạn sẽ tin vào mã mà bạn đọc được,
hay vào một công ty được trả tiền để sửa nó?
Hãy cho mình biết trong phần bình luận.
