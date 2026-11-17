<!-- S01 -->
Ở đâu đó trong nhà bạn,
có thể có một chiếc đồng hồ
mà chưa ai từng chỉnh giờ.

<!-- S02 -->
Nó vẫn chạy đúng sau khi mất điện.
Nó tự chuyển sang giờ mùa hè và ngược lại,
giữa đêm khuya.

<!-- S03 -->
Nó không có kết nối internet.
Không Wi-Fi, không GPS,
không ứng dụng nào trên điện thoại.

<!-- S04 -->
Nó chỉ có một bộ thu radio bé xíu.
Và cứ mỗi giây một lần,
nó nghe thấy một xung duy nhất.

<!-- S05 -->
Vậy làm sao một chiếc đồng hồ
biến một xung mỗi giây
thành giờ chính xác, ngày tháng
và cả thứ trong tuần?

<!-- S06 -->
Ở châu Âu, những xung đó đến
từ DCF77, gần Frankfurt.
Ở Mỹ, từ WWVB, ở Colorado.
Máy phát khác nhau, cùng một ý tưởng.

<!-- S07 -->
Lấy máy phát của Đức làm ví dụ.
Nó phát một sóng radio đều đặn,
cả ngày lẫn đêm.
Và đầu mỗi giây,
nó hạ sóng đó xuống trong chốc lát.

<!-- S08 -->
Bí quyết nằm ở việc
sóng bị hạ xuống bao lâu.

<!-- S09 -->
Một lần hạ dài một phần mười giây
nghĩa là số 0.
Một lần hạ dài hai phần mười giây nghĩa là số 1.

<!-- S10 -->
Toàn bộ ý tưởng chỉ có vậy.
Không gói dữ liệu, không mạng.
Chỉ là một sóng radio hạ xuống
trong thời gian ngắn, hoặc lâu hơn một chút.

<!-- S11 -->
Mỗi giây một bit.
Nghĩa là phải mất trọn một phút
chỉ để gửi 60 bit.

<!-- S12 -->
Và thực ra, nó chỉ gửi 59 bit.

<!-- S13 -->
Ở giây cuối cùng của mỗi phút,
sóng hoàn toàn không hạ xuống.
Và chính lần hạ bị thiếu ấy
là phần quan trọng nhất
của toàn bộ tín hiệu.

<!-- S14 -->
Bởi khi lần hạ tiếp theo đến,
đồng hồ biết
một phút mới vừa bắt đầu.

<!-- S15 -->
Khoảng trống hoạt động như một dấu chấm.
Mọi thứ giữa hai khoảng trống
là một câu hoàn chỉnh.

<!-- S16 -->
Vậy một câu dài 59 bit
chứa được những gì?

<!-- S17 -->
Phút. Giờ.
Ngày trong tháng, thứ trong tuần,
tháng và năm.

<!-- S18 -->
Hầu hết các số được gửi từng chữ số một.
47 phút
không được gửi dưới dạng 47.
Nó được gửi thành hai chữ số riêng,
số 4 và số 7.

<!-- S19 -->
4 bit là đủ cho mọi chữ số
từ 0 đến 9.
Hàng chục của phút không bao giờ vượt quá 5,
nên chỉ cần 3 bit.

<!-- S20 -->
Còn năm chỉ được hai chữ số.
Với máy phát,
2026 đơn giản là 26.
Thế kỷ thì đồng hồ tự thêm vào.

<!-- S21 -->
Nhưng radio không phải là một kênh sạch.
Một động cơ, một bộ sạc điện thoại,
một bóng đèn LED rẻ tiền...
bất kỳ thứ nào cũng có thể làm nhòe một lần hạ.

<!-- S22 -->
Vì thế, sau mỗi khối số
có thêm một bit, gọi là bit chẵn lẻ.

<!-- S23 -->
Bit này được chọn sao cho số bit 1
trong khối luôn là số chẵn.

<!-- S24 -->
Nếu nhiễu làm đảo một bit,
tổng sẽ thành số lẻ,
và đồng hồ biết
đã có gì đó sai.

<!-- S25 -->
Nhưng nếu hai bit bị đảo,
tổng lại chẵn,
và lỗi lọt qua.

<!-- S26 -->
Vì vậy nhiều đồng hồ
không tin vào một phút duy nhất.
Chúng chờ thêm một phút hợp lệ nữa.

<!-- S27 -->
Và vì vậy việc tự chỉnh giờ
có thể mất vài phút,
còn hôm nào xui thì lâu hơn nhiều.

<!-- S28 -->
Điều này dẫn đến một vấn đề kỳ lạ.

<!-- S29 -->
Đồng hồ mất trọn một phút
để thu thập thời gian 10:48.
Nhưng trong lúc nó thu thông điệp đó,
thì vẫn đang là 10:47.

<!-- S30 -->
Vậy rốt cuộc khi nào giờ mới đổi?

<!-- S31 -->
Bởi vì thông điệp đó là một lời báo trước.
Nó cho biết lúc phút tiếp theo bắt đầu
thì sẽ là mấy giờ.

<!-- S32 -->
Đồng hồ đọc hết cả câu,
chờ qua lần hạ bị thiếu,
và khi lần hạ tiếp theo đến,
chính lần hạ đó là thời khắc chính xác.

<!-- S33 -->
Các bit cho đồng hồ biết bây giờ là mấy giờ.
Lần hạ cho nó biết khi nào.

<!-- S34 -->
Nhưng câu đó còn chứa vài từ khác
ngoài thời gian.

<!-- S35 -->
Hai bit cho biết nước Đức
đang dùng giờ mùa đông hay giờ mùa hè.

<!-- S36 -->
Còn bit thứ ba là một lời cảnh báo.
Trong trọn một giờ trước khi đổi giờ,
nó được đặt thành 1.

<!-- S37 -->
Vì thế đồng hồ của bạn không cần biết
Chủ nhật nào của tháng Ba
đồng hồ được vặn lên,
hay Chủ nhật nào của tháng Mười thì vặn lùi.
Chưa ai từng dạy nó quy tắc đó.
Nó chỉ đơn giản được báo trước một giờ.

<!-- S38 -->
Nếu một ngày châu Âu thôi đổi giờ,
lời cảnh báo ấy sẽ không bao giờ đến nữa.

<!-- S39 -->
Một bit khác từng dùng để báo trước giây nhuận,
một giây được thêm vào thỉnh thoảng,
vì sự tự quay của Trái Đất
không giữ giờ hoàn hảo.
Phút đó có thể dài 61 giây.

<!-- S40 -->
Giây nhuận cuối cùng được thêm
vào cuối năm 2016.
Nhưng vào tháng 10 năm 2026,
các cơ quan đo lường thế giới
đã quyết định bỏ giây nhuận.
Từ ngày 20 tháng 5 năm 2027,
UTC sẽ chạy liên tục.

<!-- S41 -->
Và 14 bit đầu tiên
của mỗi phút
hoàn toàn không liên quan đến thời gian.

<!-- S42 -->
Từ năm 2006, chúng còn được dùng
để truyền dự báo thời tiết đã mã hóa
cho các trạm thời tiết tương thích.

<!-- S43 -->
Vậy tín hiệu chỉnh chiếc đồng hồ báo thức của bạn
cũng có thể cho biết
trạm thời tiết của một người khác
thứ Năm có mưa hay không.

<!-- S44 -->
Dù vậy, phần lớn những chiếc đồng hồ này
không nghe liên tục.
Nghe thì tốn pin,
nên nhiều chiếc chỉ thử một lần mỗi đêm,
vào lúc rạng sáng.

<!-- S45 -->
Sóng dài đến đồng hồ theo hai đường:
dọc theo mặt đất,
và dội lại từ tầng khí quyển trên cao.
Khi trời tối, đường đi phía trên thay đổi,
và tín hiệu thường đi được xa hơn.

<!-- S46 -->
Và vào lúc ba giờ sáng,
xung quanh thường có ít máy móc, bộ sạc và đèn
đang bật để lấn át nó hơn.

<!-- S47 -->
Giữa các lần kiểm tra đó,
đồng hồ chạy theo một tinh thể thạch anh,
vốn có thể lệch khoảng một giây mỗi ngày.

<!-- S48 -->
Ở lần kiểm tra thành công kế tiếp,
tín hiệu radio sẽ sửa độ lệch đó.

<!-- S49 -->
Ngay cả chỗ nó nghe cũng quan trọng.
Ăng-ten là một thanh ferit nhỏ
quấn dây.

<!-- S50 -->
Nó nghe rõ nhất khi thanh nằm vuông góc
với hướng của máy phát,
chứ không phải chĩa thẳng vào đó.
Xoay đồng hồ đi,
và một tín hiệu yếu có thể biến mất hoàn toàn.

<!-- S51 -->
Đó là lý do một chiếc đồng hồ chạy tốt trên kệ,
còn chính chiếc đồng hồ ấy, cách đó hai mét,
sau một bức tường bê tông cốt thép, không bao giờ tự chỉnh được giờ.

<!-- S52 -->
Vậy máy phát
lấy giờ từ đâu?

<!-- S53 -->
Từ PTB,
viện đo lường quốc gia của Đức,
nơi vận hành các đồng hồ nguyên tử.

<!-- S54 -->
Bản thân giây được định nghĩa
bằng các nguyên tử xêsi.
Một giây đúng bằng
9.192.631.770 dao động
của bức xạ mà chúng phát ra.

<!-- S55 -->
Vậy một chiếc đồng hồ báo thức rẻ tiền trên tủ đầu giường
theo đúng nghĩa đen
đang đi theo một chuẩn thời gian
được định nghĩa bởi nguyên tử xêsi.

<!-- S56 -->
Có điều, không hoàn hảo.
Tín hiệu đi với tốc độ ánh sáng,
và ngay cả ánh sáng cũng mất khoảng 3 mili giây
cho mỗi 1.000 ki-lô-mét.

<!-- S57 -->
Bộ thu còn thêm độ trễ của riêng nó,
và đồng hồ của bạn không bù trừ chút nào cả.
Nó không cần.
Nó chỉ hiển thị đến giây.

<!-- S58 -->
Từ một địa điểm duy nhất gần Frankfurt,
tín hiệu đến được những chiếc đồng hồ
cách xa tới khoảng 2.000 ki-lô-mét.
Đó là phần lớn châu Âu.

<!-- S59 -->
Thụy Sĩ từng có máy phát riêng,
tên là HBG, cho đến cuối năm 2011.
Ăng-ten của nó cần thay mới,
quá ít người dùng nó,
và đồng hồ ở Thụy Sĩ có thể chỉ cần
nghe tín hiệu từ Đức thay thế.

<!-- S60 -->
Những nước khác giữ lại máy phát của mình.
Anh, Pháp, Nhật Bản và Trung Quốc
đều có máy phát riêng.

<!-- S61 -->
Còn ở Bắc Mỹ, WWVB
đã phát sóng từ Fort Collins từ năm 1963,
với mã thời gian từ năm 1965.

<!-- S62 -->
Cùng một nguyên lý, khác phương ngữ.
Số 0 là một lần hạ dài hai phần mười giây.
Số 1 kéo dài nửa giây.

<!-- S63 -->
Và thay vì mỗi phút một khoảng trống,
cứ 10 giây lại có một dấu mốc dài hơn,
như dấu phẩy trong câu.
Hai dấu liền nhau nghĩa là một phút mới.

<!-- S64 -->
Khác biệt lớn nhất
là nó phát giờ nào.
Đức phát giờ dân sự Trung Âu,
được dùng chung ở phần lớn lục địa.

<!-- S65 -->
Nhưng Hoa Kỳ
trải dài qua nhiều múi giờ.
Vì thế WWVB phát giờ quốc tế, tức UTC,
và bạn cho đồng hồ biết mình đang ở đâu.

<!-- S66 -->
Nó thậm chí không gửi tháng.
Chỉ gửi số thứ tự của ngày trong năm,
từ 1 đến 366.

<!-- S67 -->
Không trạm nào trong số đó
nói cùng một ngôn ngữ.
Một chiếc đồng hồ dành cho nước Đức
không hiểu nổi Colorado.

<!-- S68 -->
Nhưng ở cả hai bờ Đại Tây Dương,
đó là cùng một thói quen lặng lẽ.
Đêm này qua đêm khác, một bộ thu nhỏ
tự khớp với một chuẩn thời gian nguyên tử
cách xa hàng trăm hay hàng nghìn ki-lô-mét.

<!-- S69 -->
Vậy mình hỏi bạn một câu.
Nếu mọi tín hiệu thời gian qua radio
biến mất đêm nay,
liệu bạn có nhận ra không?
Hãy cho mình biết trong phần bình luận.
