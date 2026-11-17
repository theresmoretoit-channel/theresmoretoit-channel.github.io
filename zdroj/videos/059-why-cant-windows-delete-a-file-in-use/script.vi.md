<!-- S01 -->
Bạn thử xóa một tệp.
Máy tính nói rằng tệp đang mở
trong một chương trình khác.
Nhưng không nói là chương trình nào.

<!-- S02 -->
Thông báo đó chỉ là phần nổi
của một câu hỏi lạ hơn nhiều.
Mở một tệp
thật ra nghĩa là gì?

<!-- S03 -->
Bởi trên một máy khác
cùng tệp đó, mở y hệt,
lại xóa được mà không một lời phàn nàn.

<!-- S04 -->
Cùng một tệp.
Cùng một thao tác.
Hai câu trả lời hoàn toàn khác nhau.

<!-- S05 -->
Hãy bắt đầu từ phần
khiến ai cũng bực.
Chương trình nào?

<!-- S06 -->
Windows biết điều đó.
Nó có một đối tượng nhân
cho tệp đang mở ấy
và biết tiến trình nào sở hữu nó.
Nó hoàn toàn có thể nêu tên.

<!-- S07 -->
Thế là bạn đóng đại mọi thứ.
Bạn mở Trình quản lý Tác vụ.
Bạn nhìn chằm chằm danh sách tiến trình
và gần như chẳng nhận ra cái nào.

<!-- S08 -->
Và suốt nhiều năm
câu trả lời đúng là
tải về một công cụ riêng.
Unlocker ra mắt năm 2005,
và trên Windows XP đó là câu trả lời.

<!-- S09 -->
Rồi Windows 7 mang đến
Trình theo dõi Tài nguyên.
Thẻ CPU.
Một danh sách tên là Associated Handles.

<!-- S10 -->
Gõ tên tệp vào.
Nó cho bạn chương trình
và số hiệu tiến trình.
Không phải cài gì cả.
Nó đã ở đó từ năm 2009.

<!-- S10b -->
Nhưng những công cụ riêng ấy làm
nhiều hơn là chỉ cho bạn biết.
Chúng có thể đóng handle
và giải phóng tệp.

<!-- S11 -->
Điều đó đưa ta trở lại
với câu hỏi.
Chương trình ấy đã nhận được gì
khi nó mở tệp?

<!-- S12 -->
Giả sử một trình phát mở
một tệp tên là movie.mp4.
Trên Windows, mở một tệp
nghĩa là quyết định hai thứ.

<!-- S13 -->
Thứ nhất thì hiển nhiên.
Tôi muốn làm gì với nó?
Đọc nó. Ghi vào nó.

<!-- S14 -->
Thứ hai mới là thứ thú vị.
Những chương trình khác được làm gì
trong lúc tôi đang mở nó?

<!-- S15 -->
Đó là một thiết lập thật sự.
Bạn nói rõ các chương trình khác
được làm gì khi bạn đang mở nó.

<!-- S16 -->
Chúng được đọc nó.
Chúng cũng được ghi vào nó.
Chúng được xóa hoặc đổi tên nó.

<!-- S16b -->
Hoặc là không được gì cả.
Không ai đụng vào nó
trong lúc tôi đang dùng.

<!-- S17 -->
Cờ cho phép xóa
có tên là FILE_SHARE_DELETE.
Và tài liệu của Microsoft
thêm một dòng ngay bên dưới.

<!-- S18 -->
Quyền xóa bao gồm
cả xóa lẫn đổi tên.

<!-- S19 -->
Vậy nên chương trình nào từ chối
chia sẻ quyền xóa
thì cũng đã khóa luôn việc đổi tên.

<!-- S20 -->
Và nếu chương trình đã mở tệp
không cấp quyền ấy,
không ai khác giành được quyền ấy.

<!-- S21 -->
Đó là lý do lỗi này
không mang tên tệp đang bận.
Nó tên là vi phạm chia sẻ.

<!-- S22 -->
Câu trả lời đã nằm sẵn
trong chính tên
của lỗi đó suốt từ đầu.

<!-- S23 -->
Giờ làm điều tương tự
trên một máy Linux.
Một trình phát mở video.

<!-- S24 -->
Và bạn gõ
rm movie.mp4.

<!-- S24b -->
Nó chạy được.
Video vẫn phát tiếp.

<!-- S25 -->
Vậy chương trình ấy đã nhận gì,
nếu không phải là việc nắm giữ tệp?

<!-- S26 -->
Đây chính là toàn bộ ý tưởng
của video này.
Cái tên không phải là tệp.

<!-- S27 -->
movie.mp4 là một mục
trong một thư mục.
Mục đó trỏ tới một đối tượng
chứa dữ liệu thật sự.

<!-- S28 -->
Khi một chương trình mở tệp,
thứ nó nhận được là một tham chiếu
tới đối tượng.
Không phải tới mục ấy.

<!-- S29 -->
Vậy nên xóa tệp
là xóa cái mục đó.
Đối tượng vẫn nguyên vẹn.

<!-- S30 -->
Trang hướng dẫn nói điều đó
chỉ trong một câu.
Tệp sẽ còn tồn tại
cho tới khi bộ mô tả tệp cuối cùng
trỏ tới nó được đóng lại.

<!-- S31 -->
Nghe thì trừu tượng
cho tới khi bạn thấy nó xảy ra.
Nên tôi đã tạo một tệp nhật ký
nặng năm trăm megabyte
và để một tiến trình giữ nó mở.

<!-- S31b -->
Rồi tôi xóa nó.

<!-- S32 -->
Liệt kê thư mục
chẳng hiện gì cả.
Công cụ đo
kích thước thư mục báo là 0.

<!-- S33 -->
Còn công cụ đo
dung lượng trống trên đĩa
thì báo rằng năm trăm megabyte
vẫn còn thiếu.

<!-- S33b -->
Một thư mục rỗng.
Nửa gigabyte đã đi đâu mất.

<!-- S34 -->
Chuyện này xảy ra đủ thường xuyên
đến mức có hẳn một lệnh riêng
chỉ để tìm những tệp như vậy.
Đã xóa, vô hình, vẫn nằm trên đĩa.

<!-- S35 -->
Và dung lượng quay lại
đúng vào lúc tiến trình ấy
buông tệp ra.

<!-- S36 -->
Cùng logic đó áp dụng cho việc đổi tên.
Di chuyển tệp trong lúc nó đang mở,
và chương trình chẳng hề hay biết.

<!-- S37 -->
Tài liệu cũng nói thẳng chỗ đó.
Các bộ mô tả tệp đã mở
bằng đường dẫn cũ không bị ảnh hưởng.

<!-- S37b -->
Nó chưa bao giờ dùng cái tên.

<!-- S38 -->
Điều đó có một giới hạn
đáng để biết.
Một chương trình đang chạy
thì không ghi đè tại chỗ được.

<!-- S38b -->
Linux từ chối.
Text file busy.

<!-- S39 -->
Thứ bạn làm được
là tách cái tên ra
và đặt một tệp mới vào đó.

<!-- S40 -->
Tiến trình cũ vẫn chạy tiếp
từ một đối tượng
không còn cái tên nào nữa.
Thứ gì khởi động sau sẽ lấy bản mới.

<!-- S41 -->
Vẫn là ý tưởng ấy lần nữa,
và tự nó chứng minh điều đó.
Nhiều thứ có thể thay được
mà không đụng tới đối tượng tại chỗ.

<!-- S41b -->
Chính vì thế Linux có thể cập nhật
một chương trình đang chạy.
Chỉ là bạn chưa có bản mới
cho tới khi khởi động lại nó.

<!-- S42 -->
Vậy Windows
đơn giản là thiết kế tệ hơn sao?

<!-- S42b -->
Không.
Và đây mới là phần
mà hầu như không ai biết.

<!-- S43 -->
Windows có một cách
để làm đúng y như vậy.

<!-- S43b -->
Trên NTFS, Windows có thể yêu cầu
một lệnh xóa kiểu POSIX.

<!-- S44 -->
Microsoft mô tả
điều gì xảy ra khi đó.
Cái tên bị gỡ khỏi
không gian tên nhìn thấy được.

<!-- S45 -->
Và các ứng dụng đã mở tệp từ trước
vẫn dùng tiếp được,
dù cái tên
mà chúng dùng để mở đã biến mất.

<!-- S46 -->
Đó chính là hành vi của Unix.
Trên NTFS.
Do Microsoft ghi lại trong tài liệu.

<!-- S47 -->
Cả hai hệ điều hành đều làm được cả hai.
Khác nhau là ở mặc định.
Là thứ bạn nhận được khi mở một tệp
mà chẳng nghĩ gì về nó.

<!-- S48 -->
Trên Windows bạn nhận một hợp đồng.
Trên Unix bạn nhận một tham chiếu
tới một đối tượng.

<!-- S49 -->
Nghe như một câu hỏi
dành cho lập trình viên,
cho tới khi bạn từng thấy
đúng cái thông báo này.

<!-- S50 -->
Hãy khởi động lại máy tính
để hoàn tất cài đặt bản cập nhật.

<!-- S51 -->
Giả sử Windows phải thay
một thư viện mà một tiến trình
vẫn đang mở theo hợp đồng chặt chẽ.

<!-- S52 -->
Nó không thể tráo tệp
ngay dưới tiến trình ấy.
Vậy nên phải có thứ gì đó buông ra.

<!-- S53 -->
Đóng ứng dụng.
Dừng dịch vụ.
Hoặc giao trọn việc đó
cho Restart Manager.

<!-- S54 -->
Vốn là một thành phần có thật.
Nó tắt mọi thứ theo thứ tự.
Ứng dụng Windows,
rồi chương trình dòng lệnh,

<!-- S55 -->
rồi dịch vụ,
và Windows Explorer sau cùng.
Sau đó nó khởi động lại chúng.

<!-- S56 -->
Và nó tồn tại vì một lý do duy nhất,
mà Microsoft nói thẳng
trong chính tài liệu của mình.

<!-- S57 -->
Lý do chính
khiến việc cài đặt phần mềm
và cập nhật đòi hỏi
khởi động lại hệ thống...

<!-- S58 -->
là vì một số tệp
được cập nhật lúc đó vẫn đang được dùng
bởi một ứng dụng
hoặc dịch vụ đang chạy.

<!-- S59 -->
Dừng ở đây thì gọn quá.
Quy tắc chia sẻ không phải lý do duy nhất
khiến máy tính đòi khởi động lại.

<!-- S60 -->
Bản cập nhật nhân lại là chuyện khác.
Không thể tráo cái nhân
ngay dưới chính nó.

<!-- S61 -->
Linux cũng có vấn đề đó,
dù vá nóng
đôi khi tránh được việc khởi động lại.

<!-- S62 -->
Vậy nên bản trung thực
khẳng định ít hơn
bản nghe cho sướng tai.

<!-- S63 -->
Cách Windows xử lý những tệp
đang được dùng khiến một số thành phần
khó thay hơn khi hệ thống đang chạy,
và điều đó đã góp phần.

<!-- S64 -->
Bởi mọi lựa chọn thiết kế
đều có hệ quả ở đâu đó.

<!-- S65 -->
Windows để chương trình
mở tệp tự quyết định
người khác được làm gì với nó.

<!-- S66 -->
Cái giá là đôi khi
bạn không xóa nổi tệp của chính mình,
vì một chương trình khác
đã không cho phép.

<!-- S67 -->
Unix giữ cái tên
và đối tượng tách rời nhau,
nên nhiều thứ thay được
trong khi hệ thống vẫn chạy.

<!-- S68 -->
Cái giá là nửa gigabyte
đã biến mất khỏi đĩa
mà chẳng thuộc về tệp nào cả.

<!-- S69 -->
Và hãy xem mỗi bên
được giải quyết ra sao.
Trên Windows, một lối ra là
đóng chương trình
đang giữ tệp.

<!-- S70 -->
Trên Linux, một cách
lấy lại chỗ trống ấy
là khởi động lại dịch vụ
vẫn đang giữ nó mở.

<!-- S71 -->
Nguyên nhân khác nhau.
Đôi khi cùng một phương thuốc.

<!-- S71b -->
Nhân tiện, nếu bạn muốn xem
câu hỏi tiếp theo dẫn ta tới đâu,
hãy cân nhắc đăng ký kênh.
Điều đó giúp kênh rất nhiều.

<!-- S72 -->
Vậy đó. Câu hỏi từ đầu video.
Mở một tệp
nghĩa là gì?

<!-- S73 -->
Nghĩa là bạn đang cầm một thứ gì đó.
Hai hệ điều hành chỉ đơn giản đặt
những thứ khác nhau vào tay bạn.

<!-- S74 -->
Đó là lý do thông báo ấy
thật ra chưa bao giờ nói
rằng tệp này không xóa được.

<!-- S75 -->
Nó nói rằng chương trình
đã mở tệp
không cho phép bạn làm vậy.

<!-- S75b -->
Và nó biết đó là chương trình nào.
Chỉ là nó không nhắc tới.
