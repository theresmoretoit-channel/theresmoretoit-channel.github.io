<!-- S01 -->
Bốn chiếc xe đến một ngã tư
vào đúng cùng một thời điểm.
Không đèn. Không biển báo.
Chỉ có quy tắc mà nhiều nước áp dụng:
nhường đường cho xe bên phải.

<!-- S02 -->
Mỗi tài xế nhìn sang phải
và thấy một chiếc xe mà họ phải chờ.
Vậy là tài xế nào cũng chờ.

<!-- S03 -->
Không ai vi phạm quy tắc.
Ai cũng tuân thủ nó một cách hoàn hảo.
Và sẽ chẳng ai nhúc nhích được nữa.

<!-- S04 -->
Các nhà khoa học máy tính gọi đây là bế tắc (deadlock).
Và nó không chỉ xảy ra trên đường.
Nó xảy ra bên trong cơ sở dữ liệu,
hệ điều hành và phần mềm thông thường.

<!-- S05 -->
Máy tính thường khá giỏi phát hiện
một bế tắc khi nó đã xảy ra.
Nhưng liệu một chương trình có thể đọc chương trình khác
và nói chắc chắn với bạn
rằng nó có bao giờ bị kẹt hay không?

<!-- S06 -->
Với nhiều chương trình thì có.
Nhưng một phương pháp hoạt động
với mọi chương trình có thể có
thì không thể tồn tại.
Và không phải vì máy tính
chưa đủ nhanh.
Máy tính có nhanh hơn đến đâu cũng không thay đổi được điều đó.

<!-- S07 -->
Đây là cách một chương trình bị kẹt.
Hãy tưởng tượng một cửa hàng trực tuyến
với hai tác vụ chạy cùng lúc.

<!-- S08 -->
Trước khi một tác vụ thay đổi bất cứ thứ gì,
nó đặt khóa lên thứ đó,
để không ai khác chạm vào được.
Giống như cầm chiếc chìa khóa duy nhất của một căn phòng.

<!-- S09 -->
Tác vụ thứ nhất khóa tài khoản của khách hàng,
rồi tìm cách khóa đơn hàng của họ.
Tác vụ thứ hai khóa đơn hàng,
rồi tìm cách khóa tài khoản.

<!-- S10 -->
Một tác vụ giữ tài khoản
và chờ đơn hàng.
Tác vụ kia giữ đơn hàng
và chờ tài khoản.
Không bên nào chịu buông thứ mình đang giữ.

<!-- S11 -->
Và điều kỳ lạ là
đoạn mã này có thể chạy cả triệu lần
mà không gặp trục trặc gì.
Chỉ khi hai tác vụ chồng lên nhau
theo đúng cái thứ tự sai ấy
thì mọi thứ mới dừng lại.

<!-- S12 -->
Lỗi đã nằm ở đó từ đầu.
Chỉ là sự trùng hợp về thời điểm đã làm nó lộ ra.

<!-- S12b -->
Nhân tiện, nếu bạn thích những video
như thế này, bạn có thể đăng ký kênh.

Như vậy sẽ giúp kênh rất nhiều.

<!-- S13 -->
Cơ sở dữ liệu gặp chuyện này suốt,
nên chúng luôn canh chừng.
Chúng vẽ một bản đồ xem ai đang chờ ai.

<!-- S14 -->
Tác vụ thứ nhất chờ tác vụ thứ hai.
Tác vụ thứ hai chờ tác vụ thứ nhất.
Khi các mũi tên khép thành một vòng,
đó là bế tắc.
Không cần đoán. Vòng ấy nằm ngay đó.

<!-- S15 -->
Rồi cơ sở dữ liệu làm một việc tàn nhẫn.
Nó chọn một trong các tác vụ
và vứt bỏ công việc của tác vụ đó.

<!-- S16 -->
SQL Server của Microsoft thậm chí còn báo cho kẻ thua
rằng nó đã được chọn
làm nạn nhân của bế tắc
và nên thử lại.

<!-- S17 -->
Tác vụ kia tiếp tục chạy,
còn nạn nhân chỉ việc thử lại.

<!-- S18 -->
Hãy để ý xem cách này giải quyết được gì và không giải quyết được gì.
Bế tắc đã được gỡ.
Nhưng đoạn mã gây ra nó vẫn còn đó,
chờ khoảnh khắc xui xẻo tiếp theo.

<!-- S19 -->
Vậy phát hiện một bế tắc
đã xảy ra rồi
là phần dễ.
Câu hỏi khó là một câu hỏi khác.

<!-- S20 -->
Không phải: chương trình này có đang bị kẹt ngay lúc này không?
Mà là: cho nó dữ liệu đầu vào này.
Liệu nó có bao giờ bị kẹt không?

<!-- S21 -->
Câu thứ nhất là một bức ảnh của hiện tại.
Bạn chỉ cần nhìn vào nó.
Câu thứ hai là một dự đoán
về mọi tương lai có thể xảy ra.

<!-- S22 -->
Và các chương trình khiến việc đó rất khó.
Chúng đưa ra quyết định. Chúng lặp đi lặp lại.
Chúng có thể chạy những phép tính kéo dài
một giây, hoặc một nghìn năm.

<!-- S23 -->
Một chương trình có thể bị kẹt ngay lập tức,
sau một triệu bước,
với một đầu vào hiếm gặp,
hoặc không bao giờ.

<!-- S24 -->
Bạn có thể cứ chạy nó và quan sát.
Nhưng nếu sau một giờ nó vẫn chưa bị kẹt,
thì điều đó cho bạn biết gì?

<!-- S25 -->
Chẳng gì cả.
Nó có thể bị kẹt ngay giây tiếp theo,
hoặc không bao giờ.

<!-- S26 -->
Năm 1936, một nhà toán học trẻ
tên là Alan Turing đã chứng minh
rằng có những câu hỏi về chương trình
mà không chương trình nào trả lời được.
Câu hỏi nổi tiếng nhất nghe còn đơn giản hơn.

<!-- S27 -->
Lấy một chương trình bất kỳ, cùng đầu vào của nó.
Cuối cùng nó có dừng lại không?
Hay nó sẽ chạy mãi mãi?

<!-- S28 -->
Ngày nay nó được gọi là bài toán dừng.
Và không chương trình nào có thể trả lời nó
đúng trong mọi trường hợp.

<!-- S29 -->
Ý tưởng đằng sau chứng minh
ngắn đến bất ngờ.
Giả sử có ai đó đưa cho bạn
một bộ kiểm tra dừng hoàn hảo.

<!-- S30 -->
Giờ bạn viết một chương trình nhỏ ngang bướng.
Nó hỏi bộ kiểm tra về chính nó,
rồi làm điều ngược lại.

<!-- S31 -->
Nếu bộ kiểm tra nói nó sẽ dừng,
nó lặp vô tận.
Nếu bộ kiểm tra nói nó sẽ chạy mãi mãi,
nó dừng ngay lập tức.

<!-- S32 -->
Dù bộ kiểm tra nói gì về nó,
bộ kiểm tra cũng sai.
Vậy một bộ kiểm tra hoàn hảo không thể tồn tại.

<!-- S33 -->
Vậy chuyện này thì liên quan gì đến bế tắc?
Liên quan mật thiết đấy.

<!-- S34 -->
Hãy tưởng tượng có người tuyên bố đã chế tạo
một bộ dự đoán bế tắc hoàn hảo.
Đưa cho nó bất kỳ chương trình nào cùng đầu vào,
và nó luôn nói chính xác cho bạn
liệu chương trình đó có bao giờ bị kẹt không.

<!-- S35 -->
Hãy dùng nó
để giải bài toán dừng.

<!-- S36 -->
Lấy bất kỳ chương trình nào bạn muốn
và đặt nó vào bên trong một chương trình mới.

<!-- S37 -->
Đầu tiên, chương trình mới
chỉ đơn giản chạy chương trình cũ,
từng bước một, trên một luồng duy nhất.
Không khóa. Không gì dùng chung.
Không có gì có thể bị kẹt.

<!-- S38 -->
Sau đó, nếu chương trình cũ kết thúc,
chương trình mới khởi động hai tác vụ.
Mỗi tác vụ chiếm một khóa,
chờ đến khi tác vụ kia chiếm xong khóa của mình,
rồi tìm cách chiếm khóa của tác vụ kia.
Cố tình tạo ra bế tắc, lần nào cũng thế.

<!-- S39 -->
Nếu chương trình cũ không bao giờ kết thúc,
chương trình mới sẽ không bao giờ đi đến bước đó.
Không bế tắc. Không bao giờ.

<!-- S40 -->
Vậy chương trình mới bị kẹt
khi và chỉ khi chương trình cũ dừng.

<!-- S41 -->
Giờ hãy hỏi bộ dự đoán
về chương trình mới.
“Có, nó sẽ bế tắc”
nghĩa là chương trình cũ dừng.
“Không” nghĩa là nó chạy mãi mãi.

<!-- S42 -->
Chúng ta vừa giải được bài toán dừng.
Mà đó chính là điều không thể làm được.

<!-- S43 -->
Vậy bộ dự đoán bế tắc hoàn hảo
cũng không thể tồn tại.

<!-- S44 -->
Vấn đề không nằm ở các khóa,
ở cơ sở dữ liệu, hay ở những lập trình viên tồi.
Một chương trình có thể giấu bất kỳ phép tính nào
ngay trước một bế tắc.
Để dự đoán bế tắc,
bạn sẽ phải dự đoán xem phép tính đó có kết thúc không.

<!-- S45 -->
Nhưng khoan đã.
Một chiếc máy tính thật không phải vô hạn.
Bộ nhớ của nó chỉ có một số hữu hạn trạng thái.
Vậy chẳng lẽ không thể kiểm tra hết chúng sao?

<!-- S46 -->
Với một cỗ máy có lượng bộ nhớ
cố định, về nguyên tắc thì có.
Còn trên thực tế, hãy thử đếm chúng.

<!-- S47 -->
Bộ nhớ của một chiếc laptop
có tám gigabyte
có thể sắp xếp theo nhiều cách đến mức
chỉ riêng việc viết con số đó ra
đã cần khoảng hai mươi tỷ chữ số.

<!-- S48 -->
Còn số nguyên tử
trong vũ trụ quan sát được
có khoảng tám mươi chữ số.

<!-- S49 -->
Vậy trên một cỗ máy thật, kiểm tra tất cả
là khả thi về lý thuyết
và vô vọng trên thực tế.

<!-- S50 -->
Nhưng đó là một bức tường khác.
Giới hạn của Turing không phải chuyện có quá nhiều trạng thái.
Nó áp dụng cho những chương trình
luôn có thể xin thêm bộ nhớ.
Với những chương trình đó, không thể có bộ dự đoán hoàn hảo,
dù máy tính lớn đến đâu.

<!-- S51 -->
Vậy có phải bế tắc là vô phương cứu chữa?
Không.
Điều đó chỉ có nghĩa là không có bộ kiểm tra hoàn hảo.
Nên các lập trình viên viết những chương trình
dễ kiểm tra hơn.

<!-- S52 -->
Mẹo đơn giản nhất là quy định một thứ tự.
Mọi tác vụ phải khóa tài khoản
trước đơn hàng.
Không bao giờ ngược lại.

<!-- S53 -->
Nếu mọi tác vụ thật sự tuân theo thứ tự đó,
vòng khép kín không thể hình thành,
và kiểu bế tắc này không thể xảy ra.

<!-- S54 -->
Những hệ thống khác bỏ cuộc sau một khoảng thời gian chờ,
lấy tất cả các khóa cùng một lúc,
hoặc để cơ sở dữ liệu chọn một nạn nhân
rồi đơn giản là thử lại.

<!-- S55 -->
Và với những thiết kế nhỏ, được mô tả cẩn thận,
các công cụ có thể kiểm tra mọi trạng thái có thể.
Các kỹ sư ở Amazon đã dùng một công cụ như vậy
để tìm ra một lỗi cần đến ba mươi lăm bước,
theo đúng thứ tự, mới xuất hiện.

<!-- S56 -->
Những công cụ này hiệu quả
vì bài toán đã được thu nhỏ.
Chúng kiểm tra một mô hình của hệ thống,
chứ không phải mọi chương trình có thể có.

<!-- S57 -->
Tuy nhiên, với mã thực tế,
một bộ kiểm tra nhận bất kỳ chương trình nào
buộc phải hy sinh một điều gì đó.
Nó có thể cảnh báo về những bế tắc
không thể xảy ra,
bỏ sót vài bế tắc có thể xảy ra,
hoặc đôi khi chẳng đưa ra câu trả lời nào.

<!-- S58 -->
Một bộ kiểm tra không bao giờ báo động nhầm,
không bao giờ bỏ sót bế tắc nào,
và luôn đưa ra câu trả lời,
cho mọi chương trình,
chính là điều mà Turing đã loại trừ.

<!-- S59 -->
Trở lại ngã tư,
bốn tài xế sẽ không ngồi đó mãi mãi.

<!-- S60 -->
Có ai đó vẫy tay.
Một tài xế nhường lượt của mình,
và chỉ vài giây sau, bế tắc đã được gỡ.

<!-- S61 -->
Cơ sở dữ liệu cũng làm đúng như vậy.
Nó không dự đoán bế tắc.
Nó nhận ra bế tắc
và buộc ai đó phải nhường.

<!-- S62 -->
Có những vấn đề cần một máy tính nhanh hơn.
Có những vấn đề cần một ý tưởng hay hơn.

<!-- S63 -->
Và có những vấn đề, như vấn đề này,
hoàn toàn không có lời giải hoàn hảo.
Chỉ có những quy tắc tốt
và một ai đó sẵn sàng vẫy tay.
