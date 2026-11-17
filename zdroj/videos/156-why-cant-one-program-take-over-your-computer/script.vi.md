<!-- S01 -->
Ngày 19 tháng 7 năm 2024,
một công ty bảo mật tên là CrowdStrike
đã gửi đi một bản cập nhật thường lệ.

<!-- S02 -->
Không phải một chương trình mới.
Chỉ là một tệp cấu hình nhỏ.

<!-- S03 -->
Chỉ trong vài giờ, 8,5 triệu
máy tính Windows đã dừng lại
ở màn hình xanh.

<!-- S04 -->
Các hãng hàng không phải dừng chuyến bay.
Bệnh viện hủy các ca phẫu thuật.
Một kênh tin tức bị mất sóng.

<!-- S05 -->
Và lỗi đằng sau chuyện đó
lại rất bình thường.
Chương trình chờ 20 mục dữ liệu.
Bản cập nhật đưa cho nó 21.

<!-- S06 -->
Game và ứng dụng của bạn
mắc những lỗi như thế suốt.
Khi đó, game tắt đi,
và bạn mở lại.

<!-- S07 -->
Cùng một kiểu lỗi.
Một cái đóng một cửa sổ.
Cái kia làm dừng
8,5 triệu cỗ máy.

<!-- S08 -->
Khác biệt không nằm ở lỗi.
Mà ở chỗ đoạn mã đó chạy ở đâu.

<!-- S09 -->
Vậy tại sao một chương trình không thể
chiếm quyền máy tính của bạn...
và tại sao chương trình này lại làm được?

<!-- S10 -->
Không phải lúc nào cũng như vậy.

<!-- S11 -->
Trên một chiếc PC chạy DOS những năm 1980,
không có gì trong bộ xử lý ngăn một chương trình lại.
Nó có thể ghi vào bất kỳ chỗ nào trong bộ nhớ
và nói chuyện thẳng với phần cứng.

<!-- S12 -->
Chỉ cần một chương trình ghi
vào chỗ không được ghi
là có thể ghi đè lên hệ điều hành,
và cả cỗ máy bị treo.

<!-- S13 -->
Cách khắc phục là thôi tin các chương trình,
và để bộ xử lý
đảm nhận việc nghi ngờ.

<!-- S14 -->
Năm 1982, bộ xử lý 80286 của Intel
giới thiệu chế độ bảo vệ,
với bốn cấp đặc quyền.

<!-- S15 -->
Chúng thường được vẽ
thành bốn vòng tròn, vòng này lồng trong vòng kia.

<!-- S16 -->
Ring 0 nằm ở giữa.
Ring 3 nằm ngoài cùng.

<!-- S17 -->
Và cách đánh số thì ngược.
Số càng nhỏ,
mã càng được phép làm nhiều việc.

<!-- S18 -->
Ring 0 thuộc về kernel,
phần lõi của hệ điều hành.
Nó phân phát bộ nhớ,
quyết định chương trình nào chạy tiếp theo,
và nói chuyện với phần cứng.

<!-- S19 -->
Ring 3 là nơi trình duyệt,
game và trình soạn thảo văn bản của bạn chạy.
Đây gọi là chế độ người dùng.

<!-- S19b -->
Windows, macOS và Linux
đều chia việc theo cách này.
Kernel ở ring 0,
ứng dụng của bạn ở ring 3.

<!-- S19c -->
Điện thoại và các máy Mac mới hơn của Apple
thì dùng chip ARM.
Ở đó, các cấp được gọi là exception level.
Tên khác, nhưng cách chia giống hệt:
một cho kernel, một cho ứng dụng của bạn.

<!-- S20 -->
Bộ xử lý luôn biết
nó đang chạy ở ring nào.
Và nó kiểm tra.

<!-- S21 -->
Một số lệnh chỉ hoạt động ở ring 0.
Ví dụ như tắt ngắt,
hoặc thay đổi cách ánh xạ bộ nhớ.

<!-- S22 -->
Khi một chương trình ở ring 3 thử một lệnh như thế,
bộ xử lý từ chối.
Nó phát sinh một ngoại lệ
và trao quyền điều khiển cho kernel,
nơi chương trình thường bị kết thúc.

<!-- S23 -->
Bộ nhớ cũng được đối xử như vậy.
Mỗi trang bộ nhớ được đánh dấu
là user hoặc supervisor.

<!-- S24 -->
Một chương trình ở ring 3
chạm vào trang supervisor
sẽ không nhận được dữ liệu.
Nó bị chặn lại.

<!-- S25 -->
Trình duyệt và game của bạn
đều chạy ở ring 3.
Thứ giữ chúng tách biệt
là mỗi chương trình có bản đồ bộ nhớ riêng.
Bộ nhớ của chương trình kia
đơn giản là không có trên đó.

<!-- S26 -->
Nên khi một game bị sập,
thiệt hại chỉ nằm trong game đó.
Kernel dọn dẹp.
Mọi thứ khác vẫn chạy tiếp.

<!-- S27 -->
Giờ hãy nhìn lại CrowdStrike.
Driver của nó chạy ở ring 0,
ngay cạnh kernel.

<!-- S28 -->
Không có gì ở trên ring 0
bắt được một lỗi như thế.

<!-- S29 -->
Nên Windows đã làm điều an toàn duy nhất còn lại.
Nó dừng cả cỗ máy, một cách cố ý,
thay vì tiếp tục với một bộ nhớ
mà nó không còn tin được nữa.

<!-- S30 -->
Màn hình xanh chính là như vậy.

<!-- S31 -->
Và vì driver khởi động
mỗi lần Windows khởi động,
mỗi lần khởi động lại, lỗi sập lại xảy ra.

<!-- S32 -->
Nhưng điều này đặt ra một câu hỏi.
Nếu trình duyệt không được chạm vào phần cứng,
thì làm sao nó lưu được một tệp
hay gửi bất cứ thứ gì qua mạng?

<!-- S33 -->
Nó xin.

<!-- S34 -->
Chương trình đặt yêu cầu của mình
vào các thanh ghi của bộ xử lý.
Tệp nào. Dữ liệu cần đi đâu.
Bao nhiêu.

<!-- S35 -->
Rồi nó chạy một lệnh đặc biệt.
Trên PC hiện đại, lệnh đó tên là SYSCALL.

<!-- S36 -->
Ngay lúc đó, bộ xử lý chuyển
từ ring 3 sang ring 0...

<!-- S37 -->
nhưng nó không nhảy
đến bất cứ đâu chương trình muốn.
Nó nhảy đến một điểm vào duy nhất
mà kernel đã chọn từ trước.

<!-- S38 -->
Kernel kiểm tra yêu cầu,
làm công việc,
rồi quay về ring 3.
Chương trình chưa bao giờ tự mình chạm vào ổ đĩa.

<!-- S39 -->
Đây là một lời gọi hệ thống,
và nó xảy ra liên tục.

<!-- S40 -->
Chúng tôi đã đếm chúng trên một chiếc laptop.
Một chương trình không làm gì cả
vẫn thực hiện 30 lần.

<!-- S41 -->
Firefox, khi khởi động
và tải một trang Wikipedia,
đã thực hiện khoảng 670.000 lần
trong 20 giây...
dù việc đếm của chúng tôi còn làm nó chậm đi.

<!-- S42 -->
Mỗi lần như thế
là một chuyến đi xuyên qua bức tường rồi quay lại.

<!-- S43 -->
Vậy là còn một điều lạ.
Bốn ring,
mà chúng ta mới chỉ cần đến hai.

<!-- S44 -->
Ring 1 và 2 đã đi đâu?

<!-- S45 -->
Ý tưởng về các ring còn có trước cả PC.
Multics, một hệ điều hành
từ cuối những năm 1960,
có tới tám ring.

<!-- S46 -->
Ý tưởng là các lớp tin cậy.
Phần lõi của hệ thống ở giữa,
các dịch vụ ít được tin hơn bao quanh,
và các chương trình ở ngoài cùng.

<!-- S46b -->
Intel cũng vẽ ra bức tranh đó.
Ring 1 và 2 được dành
cho các lớp ở giữa,
như driver và dịch vụ hệ thống.
Được tin hơn ứng dụng của bạn,
nhưng kém hơn kernel.

<!-- S47 -->
Có hai thứ cản đường.

<!-- S48 -->
Thứ nhất, các hệ thống như Unix và Windows NT
được thiết kế để chạy
trên nhiều loại bộ xử lý.

<!-- S49 -->
Và cách chia duy nhất
mà mọi bộ xử lý đều có
là hai cấp.
Một cho kernel,
một cho mọi thứ còn lại.

<!-- S50 -->
Thứ hai, chính bộ xử lý x86.
Khi nó ánh xạ bộ nhớ,
mỗi trang chỉ biết hai trạng thái.
User hoặc supervisor.

<!-- S51 -->
Ring 1 và 2 đều tính là supervisor.
Nên một driver ở ring 1
vẫn có thể chạm vào bộ nhớ của kernel.
Ring thêm vào cũng chẳng bảo vệ được bao nhiêu.

<!-- S51b -->
Dù vậy, vài hệ thống vẫn dùng chúng.
OS/2 cho một số chương trình bước vào ring 2,
chỉ để nói chuyện thẳng với phần cứng.

<!-- S51c -->
Và trước khi bộ xử lý có hỗ trợ
để chạy máy ảo,
Xen và VirtualBox chuyển kernel của hệ thống khách
xuống ring 1,
để hệ thống bên dưới
giữ ring 0 cho riêng mình.

<!-- S52 -->
Năm 2023, Intel đề xuất
bỏ hẳn ring 1 và 2.

<!-- S53 -->
Tháng 12 năm 2024, Intel từ bỏ kế hoạch đó.
Chúng vẫn còn trong bộ xử lý của bạn.
Hầu như chẳng có gì dùng đến chúng.

<!-- S54 -->
Đến đây, nghe có vẻ yên tâm.
Các quy tắc nằm trong phần cứng,
và phần cứng kiểm tra từng lần truy cập.

<!-- S55 -->
Năm 2017, ba nhóm nhà nghiên cứu,
làm việc riêng rẽ,
đã tìm ra một cách xuyên qua bức tường đó.

<!-- S56 -->
Họ gọi nó là Meltdown.
Và để hiểu được nó,
bạn cần biết một mẹo
mà các bộ xử lý hiện đại dùng.

<!-- S57 -->
Bộ xử lý không chờ
một lệnh chạy xong
rồi mới bắt đầu lệnh tiếp theo.
Nó chạy trước,
với những lệnh mà có lẽ nó sẽ cần.

<!-- S58 -->
Nếu đoán sai,
nó vứt bỏ kết quả,
như thể chưa có chuyện gì xảy ra.

<!-- S59 -->
Đây là lỗ hổng.
Trên các chip Intel bị ảnh hưởng,
một chương trình ở ring 3 có thể xin
một byte bộ nhớ của kernel...

<!-- S60 -->
và bộ xử lý lấy nó ra
rồi chuyển cho các lệnh tiếp theo
trước khi kiểm tra xong
xem việc đó có được phép không.

<!-- S61 -->
Lần kiểm tra quả thực thất bại.
Kết quả bị vứt bỏ.

<!-- S62 -->
Nhưng các lệnh tiếp theo đó
đã kịp dùng byte bí mật
để kéo một mẩu
trong chính bộ nhớ của chương trình
vào bộ nhớ đệm của bộ xử lý.

<!-- S63 -->
Và bộ nhớ đệm không quên
chỉ vì kết quả đã bị hủy.

<!-- S64 -->
Vậy là chương trình đo
thời gian truy cập từng mẩu bộ nhớ của nó.
Mẩu nào được truy cập nhanh
sẽ để lộ byte bí mật.

<!-- S65 -->
Từng byte một,
một chương trình bình thường có thể đọc
bộ nhớ của kernel,
và mọi bí mật đang nằm trong đó.
Kể cả mật khẩu và khóa mã hóa.

<!-- S66 -->
Meltdown ảnh hưởng đến các bộ xử lý Intel
từ tận năm 1995.

<!-- S67 -->
Nó được công bố
vào ngày 3 tháng 1 năm 2018.

<!-- S68 -->
Bản vá không thể thay đổi miếng silicon.
Nên các hệ điều hành đã thay đổi bản đồ.

<!-- S69 -->
Khi chương trình của bạn đang chạy,
bộ nhớ của kernel giờ bị gỡ
gần như hoàn toàn khỏi bản đồ của nó.
Chẳng còn gì ở đó để lấy.

<!-- S70 -->
Nhưng hãy nhớ những lời gọi hệ thống.
Mỗi chuyến đi xuyên tường
giờ còn phải đổi cả bản đồ.

<!-- S71 -->
Red Hat đã đo các bản vá cho Meltdown
và một lỗ hổng liên quan, Spectre.
Dưới 1% với một số công việc...
tới 19% với các cơ sở dữ liệu bận rộn.

<!-- S72 -->
Quy tắc vốn đúng từ đầu.
Chỉ là bộ xử lý kiểm tra nó quá muộn.

<!-- S73 -->
Điều đó đưa chúng ta trở lại CrowdStrike,
và một câu hỏi khó hơn.

<!-- S74 -->
Tại sao một chương trình bảo mật
lại nằm ở ring 0 ngay từ đầu?

<!-- S75 -->
Vì từ đó, nó thấy được mọi thứ.
Nó khởi động trước các phần mềm khác.
Và mã độc có quyền quản trị
sẽ khó tắt nó hơn.

<!-- S76 -->
Chính danh sách của Microsoft
kết thúc bằng một lời cảnh báo.
Driver trong kernel mang lại những điều đó, nhưng phải trả giá bằng độ ổn định của hệ thống.

<!-- S77 -->
Sau sự cố,
Microsoft bắt đầu xây dựng một cách
để phần mềm diệt virus
chạy bên ngoài kernel.

<!-- S78 -->
Đến mùa thu năm 2026,
nó vẫn chỉ có trong các bản thử nghiệm của Windows.
Và kernel vẫn chưa bị đóng
với các công ty bảo mật.

<!-- S79 -->
Game của bạn cũng đối mặt với thế khó tương tự.

<!-- S80 -->
Phần mềm gian lận chạy trong kernel
thì vô hình với một hệ thống chống gian lận
chạy ở ring 3.

<!-- S81 -->
Nên hệ thống chống gian lận cũng dọn vào đó.
Vanguard của Riot, được Valorant sử dụng,
đặt một driver vào ring 0.
Trên hầu hết các PC, nó được nạp ngay khi Windows khởi động...
kể cả khi bạn không bao giờ mở game.

<!-- S82 -->
Điều đó không có nghĩa là nó bị lỗi.
Nhưng nó nằm đúng chỗ
mà driver của CrowdStrike từng nằm,
nơi một lỗi duy nhất làm dừng cả cỗ máy.

<!-- S83 -->
Vậy tại sao một chương trình không thể
chiếm quyền máy tính của bạn?

<!-- S84 -->
Vì bộ xử lý giữ
gần như mọi chương trình tránh xa trung tâm,
và kiểm tra chúng mỗi lần chúng gõ cửa.

<!-- S85 -->
Nhưng bộ xử lý không thể quyết định
ai được cho vào.
Con người quyết định điều đó...
mỗi lần họ cài một driver.

<!-- S86 -->
Vậy đây là một câu hỏi cho phần bình luận.
Ai nên quyết định chương trình nào
được vào ring 0:
bạn, Microsoft,
hay chính các công ty làm ra chúng?
