<!-- S01 -->
Đây là tất cả kịch bản
từng được viết cho kênh này.
158 video,
gần một triệu rưỡi byte văn bản.

<!-- S02 -->
Cho chúng chạy qua một trình nén bình thường
tên là gzip.
Kết quả chỉ hơn nửa megabyte một chút.
Gần hai phần ba biến mất.

<!-- S03 -->
Mà không mất gì cả.
Giải nén tệp ra,
mọi kịch bản đều trở lại,
từng chữ một.

<!-- S04 -->
Giờ hãy nén nó thêm lần nữa.

<!-- S05 -->
Nó lớn lên.
Lớn hơn 98 byte.

<!-- S06 -->
Lần thứ ba.
Lớn hơn 98 byte.
Lần thứ tư.
Lại 98.

<!-- S07 -->
Vòng đầu bỏ đi hai phần ba.
Vòng hai chẳng tìm thấy gì.
Vậy sao ta không thể cứ nén mãi?

<!-- S08 -->
Hãy xem bên trong tệp thứ hai đó.
gzip không nén gì cả.
Nó chép nguyên dữ liệu sang, không đổi gì,
thành mười sáu khối.

<!-- S09 -->
Mỗi khối có một nhãn năm byte.
Thêm một phần đầu và phần cuối nhỏ,
là ra đúng 98.

<!-- S10 -->
Khi trình nén không tìm thấy gì để bỏ,
nó lưu dữ liệu y nguyên,
và chỉ thêm những gì cần để giải nén lại.

<!-- S11 -->
Vậy tại sao vòng hai không tìm thấy gì?
Và một chương trình thông minh hơn thì có không?

<!-- S12 -->
Văn bản kiểu này đầy sự lặp lại.
Cùng những từ, cùng những cụm từ,
cùng những ký hiệu đánh dấu cảnh nhỏ
ở đầu mỗi cảnh.

<!-- S13 -->
Năm 1977, Jacob Ziv và Abraham Lempel
công bố một mẹo đơn giản.
Đừng viết lại phần lặp.
Hãy trỏ ngược về chỗ nó đã xuất hiện.

<!-- S14 -->
Lùi lại 300 ký tự,
rồi chép mười hai ký tự tiếp theo.
Vài byte thay cho mười hai.

<!-- S15 -->
Mẹo thứ hai:
cho chữ cái phổ biến mã ngắn,
và chữ cái hiếm mã dài.

<!-- S16 -->
Năm 1951, David Huffman,
nghiên cứu sinh tại MIT,
có thể dự kỳ thi cuối kỳ,
hoặc viết một bài tiểu luận thay thế.

<!-- S17 -->
Bài tiểu luận do Robert Fano ra đề
là tìm ra loại mã hiệu quả nhất
thuộc đúng dạng này.

<!-- S18 -->
Suốt nhiều tháng, Huffman chẳng đi đến đâu.
Ông bỏ cuộc,
và bắt đầu ôn thi.
Rồi lời giải bỗng đến với ông.

<!-- S19 -->
Lấy hai ký hiệu hiếm nhất,
gộp chúng thành một,
và lặp lại cho đến khi chỉ còn một cây.

<!-- S20 -->
Sau này ông gọi đó là
“khoảnh khắc phi thường nhất đời tôi.”

<!-- S21 -->
Fano đã không nói với cả lớp
rằng chính ông cũng từng vật lộn với bài toán này,
và Claude Shannon cũng vậy.

<!-- S22 -->
Mã Huffman đánh bại phương pháp của cả hai.
Và có thể chứng minh
rằng không mã nào thuộc loại này tốt hơn.

<!-- S23 -->
Đầu thập niên 1990,
Phil Katz kết hợp cả hai mẹo
cho tệp ZIP.
gzip dùng cùng phương pháp đó.

<!-- S24 -->
Vòng đầu đã dùng hết
những quy luật mà gzip biết cách tìm.

<!-- S25 -->
Phần còn lại chẳng có quy luật nào để nó tận dụng.
Với gzip, nó trông như nhiễu.

<!-- S26 -->
Nhưng một chương trình thông minh hơn
có thể thấy những quy luật gzip bỏ sót.
Liệu một ngày nào đó, có chương trình nào
thu nhỏ được bất cứ thứ gì bạn đưa cho nó?

<!-- S27 -->
Không.
Và bạn không cần biết nó hoạt động thế nào
mới chắc chắn được điều đó.

<!-- S28 -->
Lấy mọi tệp
dài đúng ba bit.
Có tám tệp như vậy.

<!-- S29 -->
Giờ đếm tất cả các tệp ngắn hơn.
Bốn tệp dài hai bit,
hai tệp dài một bit,
và một tệp rỗng.

<!-- S30 -->
Bảy.

<!-- S30b -->
Tám tệp, và bảy chỗ ngắn hơn
để đặt chúng vào.

<!-- S31 -->
Nếu tệp nào cũng ngắn đi,
hai tệp sẽ phải chung một chỗ.
Và khi bạn giải nén,
bạn muốn lấy tệp nào?

<!-- S32 -->
Nó được gọi là nguyên lý chuồng bồ câu,
và đúng với mọi độ dài.
Số tệp ngắn hơn luôn ít hơn
đúng một tệp so với số tệp ban đầu.

<!-- S33 -->
Vậy bất kỳ trình nén nào nhận mọi tệp
và làm nhỏ một số tệp
đều phải làm những tệp khác lớn hơn.
Không phải vì nó được viết tồi.
Mà vì chẳng còn chỗ nào khác cho chúng.

<!-- S34 -->
98 byte đó
là cái giá gzip phải trả.

<!-- S35 -->
Chọn trình nén nào bạn thích.
Trong mọi tệp có cùng một kích thước,
nó chỉ thu nhỏ được chưa tới một
trên 250 tệp, dù chỉ một byte.

<!-- S36 -->
Dù vậy nén vẫn hiệu quả,
vì những tệp ta tạo ra không ngẫu nhiên.
Đó là văn bản, hình ảnh và chương trình,
đầy quy luật.

<!-- S37 -->
Điều đó không ngăn được người ta
hứa hẹn nhiều hơn.

<!-- S38 -->
Năm 1992, WEB Technologies
công bố phần mềm có thể ép
hầu như mọi dữ liệu xuống dưới một kilobyte.
Kể cả chính đầu ra của nó,
hết lần này đến lần khác.

<!-- S39 -->
Phó chủ tịch công ty nói phương pháp này
“không chịu sự chi phối của các định luật
của lý thuyết thông tin.”
Sản phẩm không bao giờ được tung ra.

<!-- S40 -->
Vậy làm sao ảnh và nhạc
lại nhỏ đi nhiều đến thế?
Chúng hoàn toàn không theo quy tắc này.

<!-- S41 -->
Ảnh JPEG giải nén ra không y hệt.
Chỉ đủ giống ảnh gốc.
Những chi tiết mắt bạn không nhận ra là đã mất
bị bỏ đi vĩnh viễn.

<!-- S42 -->
Phóng to lên,
bạn sẽ thấy chúng đã đi đâu.

<!-- S43 -->
Đó là nén mất dữ liệu,
và đó là một cuộc chơi khác.
Video này nói về loại còn lại.
Mọi bit trở lại, chính xác.

<!-- S44 -->
Vậy với những tệp thật sự có quy luật,
chúng có thể nhỏ đến mức nào?
Có một cái đáy không?

<!-- S45 -->
Có.
Nó được tìm ra năm 1948,
trong cùng bài báo làm nền cho video của kênh
về mã sửa lỗi.

<!-- S46 -->
Ở đó, Claude Shannon cho thấy
thêm phần dư thừa giúp bảo vệ thông điệp ra sao.
Còn ở đây, ông tính ra
có thể bỏ bớt bao nhiêu phần dư thừa ấy.

<!-- S47 -->
Câu trả lời của ông là một con số
mà ông gọi là entropy:
khó đến mức nào để đoán
điều gì sẽ đến tiếp theo.

<!-- S48 -->
Không có mã không mất dữ liệu nào xuống dưới được con số đó
xét trung bình.
Nhưng bạn có thể tiến sát nó
gần bao nhiêu tùy ý.

<!-- S49 -->
Vậy tiếng Anh khó đoán đến mức nào?
Năm 1951, Shannon đo điều đó
bằng một trò chơi.

<!-- S50 -->
Ông đưa cho một người một đoạn văn
mà họ chưa từng thấy,
và bảo họ đoán,
từng chữ cái một.

<!-- S51 -->
Nếu đoán sai,
họ đoán lại,
cho đến khi đúng.

<!-- S52 -->
Hóa ra con người đoán rất giỏi.
Với ngữ cảnh một trăm chữ cái,
tiếng Anh ra khoảng một bit
mỗi chữ cái.

<!-- S53 -->
Máy tính lưu mỗi chữ cái
bằng tám bit.
Người đọc chỉ cần khoảng một.

<!-- S54 -->
Chính khoảng chênh lệch đó tạo chỗ cho việc nén.
gzip đưa kịch bản của kênh xuống
dưới ba bit mỗi ký tự.

<!-- S55 -->
Vậy máy móc có thể tiến
gần một bit đến mức nào?

<!-- S56 -->
Có hẳn một giải thưởng cho việc đó.
Nó tên là Hutter Prize,
và từ năm 2020, đề bài là một tệp duy nhất:
một gigabyte Wikipedia tiếng Anh.

<!-- S57 -->
gzip thu nó còn một phần ba.
Những trình nén thông dụng tốt nhất,
còn khoảng một phần năm.

<!-- S58 -->
Kỷ lục, lập vào tháng 7 năm 2026,
là hơn một trăm triệu byte một chút.
Một phần mười.

<!-- S59 -->
Và trình giải nén cũng được tính.
Kích thước của nó được cộng vào tổng,
nên bạn không thể giấu Wikipedia
bên trong chương trình.

<!-- S60 -->
Quỹ giải là 500.000 euro.
Mỗi một phần trăm cải thiện
được thưởng năm nghìn.

<!-- S61 -->
Marcus Hutter, người tài trợ giải, giải thích lý do:
“có khả năng nén tốt
có liên hệ mật thiết
với khả năng hành động thông minh.”

<!-- S62 -->
Bởi các chương trình dẫn đầu
không đi tìm phần lặp lại.
Chúng dự đoán.

<!-- S63 -->
Trước mỗi ký tự,
chúng ước tính khả năng xuất hiện
của từng ký tự có thể đến tiếp theo.
Một lần đoán tốt chỉ tốn một phần nhỏ của một bit.

<!-- S64 -->
Đó là trò chơi đoán chữ của Shannon,
do máy chơi.
Những người chơi giỏi nhất giờ dùng mạng nơ-ron,
được huấn luyện để đoán điều gì đến tiếp theo.

<!-- S65 -->
Cách này hiệu quả cả với tệp đã được nén.
Năm 2016, Dropbox bắt đầu đóng gói lại
ảnh JPEG của người dùng bằng bộ dự đoán tốt hơn.
Trung bình nhỏ đi hơn một phần năm.

<!-- S66 -->
Mọi tệp đều trở lại nguyên từng bit,
và đến năm 2017,
đã tiết kiệm được hơn 46 petabyte.
Tức là hơn 46.000 terabyte.

<!-- S67 -->
Rồi đến những gã khổng lồ.
Năm 2023, các nhà nghiên cứu ở DeepMind
dùng một mô hình ngôn ngữ lớn
làm trình nén.

<!-- S68 -->
Trên những mảnh ảnh xám nhỏ cắt từ ảnh chụp,
nó thắng PNG:
48% kích thước gốc
so với 58%.

<!-- S69 -->
Trên bản ghi âm giọng đọc,
nó thắng FLAC:
21% so với 30%.

<!-- S70 -->
Nhưng đó là chưa tính mô hình.
Cộng kích thước của nó vào,
và kết quả lớn
gấp 140 lần
so với chính dữ liệu.

<!-- S71 -->
Trình nén lớn hơn dữ liệu của nó
chẳng tiết kiệm được gì.
Chương trình là một phần của bản mô tả.

<!-- S72 -->
Và điều đó đưa ta đến phần kỳ lạ nhất.
Đây là một triệu chữ số đầu tiên của số π.

<!-- S73 -->
Đưa chúng cho bốn trình nén.
Trình tốt nhất đưa chúng xuống còn khoảng
426.000 byte.

<!-- S74 -->
Giờ đưa cho chính những trình nén đó
một triệu chữ số ngẫu nhiên.
Kết quả y như vậy,
chênh lệch chưa tới một phần mười phần trăm.

<!-- S75 -->
Nhưng π không được tạo ra ngẫu nhiên.
Nó tuân theo một quy tắc toán học.
Đây là một chương trình in ra
từng chữ số trong một triệu chữ số đó.

<!-- S76 -->
362 byte.
Ngắn hơn tệp kia hơn hai nghìn lần.

<!-- S77 -->
Các trình nén không thể thấy
quy tắc toán học đằng sau π.
Chúng chỉ thấy các chữ số.

<!-- S78 -->
Một cách để đo lượng thông tin
trong dữ liệu là hỏi:
một chương trình có thể ngắn đến mức nào
mà vẫn in ra được nó?

<!-- S79 -->
Độ dài đó được gọi là
độ phức tạp Kolmogorov,
theo tên một trong những người đã mô tả nó.

<!-- S80 -->
Phần lớn dữ liệu không có chương trình ngắn nào.
Lại là nguyên lý chuồng bồ câu:
không có đủ chương trình ngắn
để chia cho tất cả.

<!-- S81 -->
Một triệu chữ số ngẫu nhiên
rất có thể không có gì ngắn hơn.
Số π thì có.

<!-- S82 -->
Vậy sao không tìm luôn
chương trình ngắn nhất cho mọi tệp?
Vì người ta đã chứng minh
rằng không thuật toán nào làm được điều đó
cho mọi tệp.

<!-- S83 -->
Mỗi chương trình cho bạn một giới hạn trên.
Nhưng không gì có thể luôn cho bạn biết
liệu có chương trình ngắn hơn hay không.
Bạn không bao giờ biết mình đã chạm đáy.

<!-- S84 -->
gzip tìm ra phần lặp lại trong các kịch bản,
và không gì hơn.
Nó thấy byte,
chứ không thấy nghĩa của từ.

<!-- S85 -->
Để đi xa hơn, một chương trình
phải dự đoán chúng tốt hơn.
Và dự đoán văn bản thật tốt
bắt đầu trông rất giống việc hiểu nó.

<!-- S86 -->
Vậy đây là câu hỏi cho bạn.
Nếu một chương trình có thể nén Wikipedia
xuống nhỏ hơn mọi chương trình khác,
bạn có nói rằng nó hiểu Wikipedia không?
Hãy để lại câu trả lời trong phần bình luận.
