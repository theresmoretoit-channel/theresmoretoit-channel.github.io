<!-- S01 -->
Bạn mua một ổ đĩa mới tinh.
Một terabyte, hoàn toàn trống.
Trước khi chứa được dù chỉ một tập tin,
nó phải được định dạng trước đã.

<!-- S02 -->
Vậy là bạn định dạng nó bằng ext4,
hệ thống tập tin tiêu chuẩn
trên nhiều máy tính Linux.
Với thiết lập mặc định,
khi bạn còn chưa lưu gì cả,
khoảng mười bảy gigabyte đã biến mất.

<!-- S03 -->
Chưa có gì được lưu cả.
Không ảnh, không tài liệu.
Vậy thứ gì đang chiếm hết chỗ đó?

<!-- S04 -->
Mà sao ổ đĩa lại cần định dạng
ngay từ đầu?
Nó vốn đã lưu được dữ liệu.
Nó đọc và ghi được hàng nghìn tỷ bit.

<!-- S05 -->
Sao máy tính không cứ thế ghi
vào bất cứ chỗ nào còn trống?

<!-- S06 -->
Vì lưu dữ liệu
và tìm lại nó
là hai bài toán rất khác nhau.

<!-- S07 -->
Hãy tưởng tượng một văn phòng phát
giấy trắng thay vì biểu mẫu.
Mọi thứ đều được ghi ở đâu đó...
và chẳng ai tìm được gì.

<!-- S08 -->
Một ổ đĩa không có hệ thống tập tin
chính là đống giấy đó.
Nhưng một hình ảnh hay hơn
là một cuốn sổ.

<!-- S09 -->
Hãy hình dung một cuốn sổ
có một nghìn trang,
và vài quy tắc để dùng nó.

<!-- S10 -->
Thứ nhất, mỗi trang đều có số.
Giờ thì mọi chỗ trong cuốn sổ
đều có địa chỉ.
Trang bốn trăm mười hai
nghĩa là đúng một chỗ duy nhất.

<!-- S11 -->
Thứ hai, vài trang đầu
là mục lục.
Mỗi mục ghi một cái tên,
và trang nơi nó nằm.
Bánh kếp: trang mười hai.

<!-- S12 -->
Thứ ba, ở tận cuối sổ,
có một danh sách các trang
vẫn còn trống.

<!-- S13 -->
Giờ thêm một công thức.
Bạn xem danh sách ở cuối sổ để tìm trang trống.
Bạn viết công thức vào đó.
Bạn thêm một dòng vào mục lục.
Và bạn gạch trang đó
khỏi danh sách trang trống.

<!-- S14 -->
Một công thức, ba chỗ.
Và cả ba phải khớp nhau.

<!-- S15 -->
Rồi công thức bánh kếp dài ra.
Trang mười hai đã đầy,
còn trang mười ba thì đã có chủ.
Nên công thức được viết tiếp ở trang tám mươi bảy,
và mục lục phải ghi lại điều đó.

<!-- S16 -->
Và đây mới là chỗ khó.
Nếu bạn muốn có chỗ cho một nghìn mục
trong mục lục,
bạn phải dành sẵn những trang đó
trước khi viết dù chỉ một công thức.

<!-- S17 -->
Phép so sánh là vậy.
Còn đây là thứ thật sự nằm trên ổ đĩa.

<!-- S18 -->
Ổ đĩa không biết gì về tập tin,
thư mục hay tên gọi.
Nó chỉ cung cấp một dãy dài
các ô được đánh số, gọi là sector.

<!-- S19 -->
Trên ổ cứng HDD,
dữ liệu nằm trên các đĩa từ đang quay.
SSD thì giữ nó trong bộ nhớ flash.
Dù là loại nào, máy tính cũng chỉ yêu cầu
một sector theo số của nó,
và ổ đĩa tự tìm ra sector đó nằm ở đâu.

<!-- S20 -->
Một sector rất nhỏ.
Thường là 512 byte,
hoặc 4.096
trên các ổ đĩa mới hơn.

<!-- S21 -->
Hệ thống tập tin thường làm việc
với những mảnh lớn hơn, gọi là khối.
Trên ext4, một khối là bốn kilobyte,
bằng tám sector kiểu cũ.

<!-- S22 -->
Những khối được đánh số đó
chính là các trang của cuốn sổ.
Thứ hệ thống tập tin còn cần
là hai phần còn lại:
một mục lục,
và một danh sách những chỗ còn trống.

<!-- S23 -->
Đó là thứ mà việc định dạng tạo ra.
Và đó là nơi
mười bảy gigabyte kia đã đi mất.

<!-- S24 -->
Ext4 dành sẵn một bản ghi
cho mỗi tập tin và thư mục
mà ổ đĩa có thể chứa cùng lúc.
Mỗi bản ghi có
256 byte.
Nó được gọi là inode.

<!-- S25 -->
Một ngày nào đó, mỗi inode sẽ cho biết
một tập tin lớn cỡ nào,
nó được thay đổi khi nào,
ai được phép mở nó,
và những khối nào chứa nội dung của nó.

<!-- S26 -->
Trên một ổ đĩa một terabyte,
ext4 chuẩn bị khoảng
sáu mươi mốt triệu inode như vậy.
Tất cả đều trống, tất cả đều chờ.
Đó là gần mười sáu gigabyte
bản ghi trống.

<!-- S27 -->
Sao lại là sáu mươi mốt triệu?
Ext4 đoán một cách đơn giản:
cứ mỗi mười sáu kilobyte
dung lượng ổ đĩa thì có một inode.
Trên một máy tính thông thường,
phần lớn những bản ghi đó
sẽ không bao giờ được dùng đến.

<!-- S28 -->
Thêm khoảng một gigabyte nữa
dành cho nhật ký,
mà ta sẽ quay lại sau.
Phần còn lại là sổ sách khác,
gồm cả một bản đồ với một bit cho mỗi khối,
cho biết khối đó đang dùng hay còn trống.

<!-- S29 -->
Con số đó cũng cố định.
Hãy dùng hết mọi bản ghi
bằng hàng triệu tập tin nhỏ xíu,
và ổ đĩa sẽ báo với bạn là nó đã đầy...
dù vẫn còn trống hàng gigabyte.

<!-- S30 -->
Vậy hãy xem nó hoạt động.
Ta sẽ tạo một tập tin tên là hello.txt.
Bên trong chỉ có một từ: hello.
Năm chữ cái. Năm byte.

<!-- S31 -->
Hệ thống tập tin chọn một inode trống.
Giả sử là số mười ba.
Rồi nó tìm một khối trống trên bản đồ,
và đánh dấu khối đó là đã dùng.

<!-- S32 -->
Nó ghi năm byte đó vào khối ấy.
Rồi nó điền vào inode:
dài năm byte, vừa được tạo,
và nằm trong đúng một khối đó.

<!-- S33 -->
Và cuối cùng, trong thư mục,
nó thêm một dòng:
tên hello.txt,
và số mười ba.

<!-- S34 -->
Hãy để ý cái tên nằm ở đâu.
Không phải trong tập tin.
Không phải trong inode.
Cái tên nằm trong thư mục,
mà thư mục thật ra chỉ là một danh sách
gồm tên và số.

<!-- S35 -->
Và thư mục cũng chỉ là một tập tin khác.
Nội dung của nó
chẳng qua là danh sách đó.

<!-- S36 -->
Đó cũng là lý do việc chuyển một tập tin
sang thư mục khác trên cùng hệ thống tập tin
diễn ra tức thì, dù nó lớn đến đâu.
Một thư mục mất đi một dòng,
thư mục kia thêm một dòng,
và thường thì nội dung
chẳng di chuyển chút nào.

<!-- S37 -->
Năm byte văn bản...
mà trên ổ đĩa, nó chiếm
4.096.
Khối là mảnh nhỏ nhất
mà hệ thống tập tin cấp phát,
nên ngay cả tập tin nhỏ xíu cũng tốn nguyên một khối.

<!-- S38 -->
Khi tập tin lớn vượt quá khối của nó,
hệ thống tập tin tìm thêm một khối trống khác.
Có thể ngay sát bên.
Có thể ở một nơi hoàn toàn khác.
Và inode ghi nhớ cả hai.

<!-- S39 -->
Theo thời gian, một tập tin lớn có thể bị
chia thành nhiều mảnh rải khắp ổ đĩa.
Ổ cứng HDD phải nhảy qua lại giữa chúng.
SSD xử lý chuyện đó tốt hơn nhiều.

<!-- S40 -->
Chương trình đã lưu tập tin
không hề biết gì về những điều này.
Nó chỉ nói "lưu hello.txt",
và mọi thứ khác diễn ra bên dưới.

<!-- S41 -->
Giờ hãy xóa nó.
Cái tên bị gỡ khỏi thư mục.
Inode được đánh dấu là trống.
Khối quay về danh sách các khối trống.

<!-- S42 -->
Trên ổ cứng truyền thống,
bản thân năm byte đó vẫn nằm nguyên chỗ.
Không ai đụng đến chúng.
Chúng vẫn còn đó cho đến khi có thứ mới
được ghi đè lên.

<!-- S43 -->
Đó là lý do một tập tin đã xóa
đôi khi có thể được khôi phục.
Việc xóa thường không xóa sạch
nội dung.
Nó chỉ đánh dấu chỗ đó là còn trống.

<!-- S44 -->
Trên SSD thì kém chắc chắn hơn.
Hệ thống tập tin có thể báo cho ổ đĩa
rằng những khối đó không còn cần nữa,
và ổ đĩa có thể bỏ đi những gì trong đó.
Sau đó, khả năng lấy lại tập tin
thấp hơn nhiều.

<!-- S45 -->
Vậy hệ thống tập tin thực chất là người giữ sổ sách.
Chỉ riêng việc tạo tập tin này
nghĩa là cập nhật ba thứ:
thư mục, inode,
và bản đồ các khối trống.

<!-- S46 -->
Giờ hãy ngắt điện
giữa chừng lúc đang lưu tập tin.

<!-- S47 -->
Có thể khối đã được đánh dấu là đã dùng,
nhưng chưa có inode nào trỏ đến nó.
Chỗ đó coi như mất.
Phiền, nhưng vô hại.

<!-- S48 -->
Hoặc có thể inode trỏ đến một khối
mà bản đồ vẫn coi là trống.
Tập tin tiếp theo có thể được ghi
đè ngay lên đó.
Và tập tin đầu tiên âm thầm bị phá hủy.

<!-- S49 -->
Đó là lý do ext4 giữ một cuốn nhật ký.
Trước khi thay đổi sổ sách của mình,
nó ghi lại điều nó sắp làm.
Sau sự cố, nó chỉ thực hiện lại những thay đổi
mà nó đã ghi xong,
và đã đánh dấu là hoàn tất.
Những gì dang dở đều bị bỏ qua.

<!-- S50 -->
Và còn một vấn đề âm thầm hơn.
Đôi khi ổ đĩa làm thay đổi một bit
mà không báo cho ai cả.

<!-- S51 -->
Ext4 bảo vệ các bản ghi của chính nó
bằng tổng kiểm tra,
nên nó phát hiện được hư hỏng ở đó.
Nhưng còn nội dung tập tin của bạn?
Cái đó thì nó cứ thế tin.

<!-- S52 -->
Một số hệ thống tập tin kiểm tra cả hai.
Và một số giữ thêm một bản sao thứ hai,
nên khi một bản bị hỏng,
chúng có thể sửa nó từ bản kia.
Phát hiện vấn đề và sửa nó
không phải là một.

<!-- S53 -->
Vậy mọi hệ thống tập tin đều làm cùng một việc:
các khối được đánh số, một danh sách tên,
và một bản đồ những chỗ còn trống.

<!-- S54 -->
Nhưng cách làm thì khác nhau.
Ext4 chuẩn bị sáu mươi mốt triệu bản ghi
trước khi bạn lưu bất cứ thứ gì.
NTFS trên Windows giữ các bản ghi của nó
trong một bảng lớn duy nhất, lớn dần khi bạn dùng.

<!-- S55 -->
Còn Btrfs không chuẩn bị trước
một bảng inode cố định.
Nó tạo inode khi tập tin xuất hiện.
Và thông thường, nó không ghi đè
dữ liệu tại chỗ.
Nó ghi một bản sao mới,
rồi mới bỏ bản cũ.

<!-- S56 -->
Theo mặc định, nó còn tính tổng kiểm tra cho các tập tin của bạn,
nên biết được khi chúng bị hỏng.

<!-- S57 -->
Và vì bản cũ
không bị ghi đè,
một snapshot có thể giữ nó lại.
Điều đó thay đổi câu trả lời
cho gần như mọi câu hỏi trong video này:
sự cố gây ra điều gì,
xóa nghĩa là gì,
và thậm chí bản sao là gì.

<!-- S58 -->
Đó là nơi video tiếp theo bắt đầu.

<!-- S59 -->
Vậy đây là một câu hỏi cho bạn.
Hệ thống tập tin chỉ nên lưu trữ tập tin của bạn,
hay nên bảo vệ chúng nữa?
Hãy cho mình biết trong phần bình luận.
