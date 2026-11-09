---
title: Wireshark
tags: ["Tools"]
---

# I. Wireshark: The Basics
## Misson 1 : Tổng quan về công cụ
### Giới thiệu
- Wireshark là công cụ phân tích lưu lượng truy cập mạng
- Mục đích 
    >Phát hiện và khắc phục sự cố mạng
    Phát hiện bất thường về bảo mật
    Điều tra và tìm hiểu về các giao thức
### Giao diện và dữ liệu
![image](/images/7d9af824cfcbd0a0ee2978a93dc09455.png)
- Toolbar : Chứa nhiều menu và phím tắt 
- Display filter : Phần truy vấn và lọc
- Recent files : Các tệp tin gần đây
- Capture filter and available sniffing interfaces : Giao diện mạng là điểm kết nối giữa máy tính và mạng, kết nối phần mền
- Status bar : Trạng thái công cụ, hồ sơ và thông tin gói số
### Tải file PCAP Files
![image](/images/5b06b2dd6d2df4fa250245ebd80d2330.png)
- Chi tiết gói được hiển thị trong 3 ngăn khác nhau 
    > Packet List Pane : Tóm tắt từng gói địa chỉ
    Packet Details Panel : Phân tích chi tiết gói đã chọn
    Packet Bytes Pane : Hex và ASCII của gói được chọn
### Gói màu ( Colouring Packets )
- Đánh màu các giao thức đồng thời giúp phát hiện các điểm bất thường
- Có 2 phương pháp tô màu gói tin
    > Quy tắc tạm thời : Trong phiên do mình đặt
    Quy tắc vĩnh viễn : Lưu dưới tệp hồ sơ

![image](/images/5114b4e91544caec8e1e5567c1f0fa34.png)

### Traffic Sniffing
- Dùng nút "shark" xanh dương để bắt đầu quét 
- Nút đỏ để dừng quét
- Nút xanh lá để khởi động lại quá trình quét

![image](/images/3708e749544133b4333a291998908ba2.png)

### Hợp nhất các tệp PCAP
![image](/images/0a4f983dc3309a9b2140268ae2a91226.png)

### Xem chi tiết tệp 
- Góc dưới bên trái
![image](/images/37af3be5f818380a2c630c7255f5a54d.png)

![image](/images/192d6f97194ea79ac7c035807a214ce8.png)

## Misson 2 : Phân tích gói tin
### Chi tiết gói dữ liệu
![img](/images/6eee83b86a68fbf61b15bb9319123804.svg)

- Mỗi lần trỏ vào 1 chi tiết, nó sẽ làm nổi bật phần tương ứng trong khung byte

![image](/images/b7a7882673effb70ed75546c7afc1bfb.png)

- Hãy cùng xem chi tiết

![image](/images/b46feed5e02d09ae55c71a531d5225c7.png)

- Tương ứng trong lớp OSI
    > Frame/packet : Layer 1
    ![image](/images/7ad47278bfac001a8cf9a0435e6e51cd.png)
    Source [MAC] : Layer 2 
    ![image](/images/aceac2d18e3aec81662399837483037c.png)
    Source [IP] : Layer 3 
    ![image](/images/a6fa60bf7e4de24be966198578d4ba5c.png)
    Giao thức : Layer 4 
    ![image](/images/e2fe8f378dd285bdcf8504478e8511dd.png)
    Lỗi giao thức
    ![image](/images/1269873be6f5f6481a4ab51957119e90.png)
    Giao thức ứng dụng : Layer 5
    ![image](/images/bc3095a4c18c3a5ef818ce43292919c7.png)
    Dữ liệu
    ![image](/images/f263d95b902fda0b206623538d9d3f77.png)

## Misson 3 : Điều hướng gói tin
### Số gói tin 
- Wireshark tính toán số lượng gói tin, giúp quá trình phân tích cho các bản ghi lớn và dễ dàng quay lại điểm cụ thể của sự kiện

![image](/images/adae64068406f28f0e91e3c43ef271e1.png)

### Đi đến gói tin
- Giúp dễ dàng tìm kiếm/điều tra các gói cụ thể

![image](/images/49f88c4f12ada8c94a26f881934e2e28.png)

### Tìm gói dữ liệu
- Tìm kiếm bên trong các gói tin cho một sự kiện cụ thể 

![image](/images/f39a1619e5e4843422a515f0b059ef64.png)

### Gói đánh dấu
- Giúp các nhà phân tích chỉ ra một sự kiện quan tâm hoặc xuất các gói cụ thể từ quá trình thu thập

![image](/images/de31de86d0403f9a20ef61156724f9a7.png)

### Bình luận gói tin
- Thêm chú thích cho các gói cụ thể để hỗ trợ điều tra thêm hoặc nhắc nhở và chỉ ra các điểm quan trọng/đáng ngờ

![image](/images/429b04e8c7930cb7d2d9bb31d4f6293d.png)

### Xuất gói dữ liệu
- Chức năng này giúp các nhà phân tích chia sẻ những gói đáng ngờ duy nhất (phạm vi đã được xác định)

![image](/images/64c5b405ad0f08c57339d86469968d75.png)

![image](/images/b2c41a1dd315aff6a98632d1491dfa13.png)

### Xuất đối tượng ( Tệp )
- Wireshark có thể trích xuất các tệp được truyền qua đường dây

![image](/images/4c5cec8d908948d6eb958b37bbd1a149.png)

### Định dạng hiển thị thời gian
- Wireshark liệt kê các gói tin khi chúng được ghi nhận, nên việc điều tra luồng mặc định không phải lúc nào cũng là lựa chọn tốt nhất

![image](/images/3a47a14b098969297e2108cdfa3bf937.png)

![image](/images/e51bb915e5252ef744e2c0f0bdac68a6.png)

### Expert Info ( Thông tin chuyên gia )
- Cung cấp một nhóm với 3 loại mức độ nghiêm trọng khác nhau

| Mức độ nghiêm trọng | Màu sắc | Thông tin |
| -------- | -------- | -------- |
| Chat  | Xanh dương     | Quy trình làm việc thông thường
|Note | Xanh lục | Những sự kiện đáng chú ý 
Warn | Vàng | Những cảnh báo 
Error | Đỏ | Các vấn đề như gói dữ liệu bị lỗi

- Các thông tin thường gặp được liệt kê

|  Nhóm | Thông tin | Nhóm | Thông tin |
| -------- | -------- | -------- | --- |
| Checksum   | Lỗi kiểm tra tổng     | Deprecated    |   Việc sử dụng giao thức bị loại bỏ  | 
Comment | Phát hiện bình luận gói tin | Malformed | Phát hiện gói dữ liệu bị lỗi 

![image](/images/667f211bcab805a4a16e0c92ce8e6d72.png)

## Misson 3 : Lọc gói tin
### Giới thiệu bộ lọc
- Giúp các nhà phân tích thu hẹp lưu lượng truy cập và tập trung vào sự kiện quan tâm
- Hai loại phương pháp lọc: bộ lọc thu thập và bộ lọc hiển thị

### Apply as Filter ( Áp dụng bộ lọc )
- Đây là cách cơ bản nhất để lọc lưu lượng

![image](/images/2c29ea93f27f5bf956f639f7a6ef6410.png)

### Conversation Filter ( Bộ lọc hội thoại )
- Điều tra một số gói cụ thể và tất cả các gói liên kết bằng cách tập trung vào địa chỉ IP và số cổng

![image](/images/3947662b707044edf3333c6335d62652.png)

### Colourise Conversation ( Tô màu cuộc hội thoại )
- Tương tự **Conversation Filter** nhưng nổi bật các gói tin liên kết mà không áp dụng bộ lọc hiển thị và giảm số lượng gói đã xem

![image](/images/8c7779ae40dd2584e2043c4f6206033e.png)

- Khi muốn phục hồi lại màu gốc

![image](/images/ad02aa9c9726b5609755817b9db79fda.png)

### Prepare as Filter ( Chuẩn bị làm bộ lọc )
- Tương tự như **Apply as Filter** nhưng ko làm thay đổi thứ tự như **Apply as Filter** mà chỉ trỏ tới

![image](/images/e449f0f09c1f876dcba6809d9212dce6.png)

### Apply as Column ( Áp dụng dưới dạng cột )
- Giúp các nhà phân tích kiểm tra sự xuất hiện của một giá trị/trường cụ thể trên các gói dữ liệu

![image](/images/6698e8dedb544e30679a567c26a311fd.png)

- Cột mới đã được thêm 

![image](/images/ce48d7bf146f395ff828e2f39a9536a4.png)

### Follow Stream ( Theo dõi luồng )
- Giúp các nhà phân tích tái tạo dữ liệu cấp ứng dụng và hiểu sự kiện quan tâm

![image](/images/557436ffbca5b08f5be3877edb713249.png)

- Khi này bộ lọc tương ứng sẽ được áp dụng vậy nên cần gỡ chúng bằng nút "X" trên thanh lọc 

![image](/images/daf1a63a817cb79a2d52008b0cf2daa6.png)

### Simple Display Filter Queries ( Truy vấn bộ lọc hiển thị đơn giản )
- Cách dễ nhất để lọc nhanh số lượng gói dữ liệu khổng lồ là áp dụng bộ lọc hiển thị qua thanh lọc

![image](/images/12fa8ad691da3b083642d49875c914a9.png)

- Lọc theo tên giao thức hoặc cổng ( Protocol hoặc port )

![image](/images/6b8a5f95b537ddb9442fa616cf9eda15.png)

![image](/images/e9f89a508ad2bfcd279d632f8204b321.png)

- Lọc theo địa chỉ IP 

![image](/images/49bc241b63764e61449576af29774a88.png)

# II. Wireshark: Packet Operations
## Misson 1 : Thống kê | Tóm tắt ( Summary )
### Giới thiệu
- Giúp người dùng nhìn tổng thể về thống kê chi tiết đặc thù của giao thức
### Resolved Addresses 
- Giúp các nhà phân tích xác định địa chỉ IP và tên DNS có trong tệp ghi

- ![image](/images/f46f18dae3abe5f9c9f9b983d7a0c325.png)

### Protocol Hierarchy
- Giúp các nhà phân tích xem giao thức dưới dạng cây dựa trên bộ đếm gói và tỷ lệ phần trăm

![image](/images/71e09da6a1e53ffa96c8bca2152ba0ac.png)

### Conversations
- Cung cấp danh sách các cuộc trò chuyện dưới năm định dạng cơ sở
- **Conservation** nó là hiển thị flow giao tiếp 2 chiều A <-> B

![image](/images/267ba939d2139173819d38a772e75d66.png)


### Endpoints 
- Tương tự **Conversations** nhưng tùy chọn này cung cấp thông tin duy nhất cho một trường thông tin duy nhất 
- **Endpoints** chỉ là 1 chiều thôi A->B hoặc B->A

![image](/images/4d0bd0eb2c21e86f03efa973c186b053.png)

- Wireshark cũng cung cấp các tùy chọn phân giải IP và tên cổng

![image](/images/f3472a3d979314d51fe1da696889d877.png)

- Chế độ xem **Endpoimts** với phân giải tên miền 

![image](/images/6b4a0d688ae6139bf1e745c6cf046878.png)

- Wireshark còn cung cấp bản đồ định vị địa lý IP giúp các nhà phân tích xác định địa chỉ nguồn và đích của bản đồ

![image](/images/c62ba691a0eb9aaa626505ffc0fd4a11.png)

![image](/images/188f1c88e84a3827d7d7ec5d26d898e1.png)

- Endpoint và góc nhìn GeoIP

![image](/images/92f1686e38470e4354b2405d898f84c5.png)

## Mission 2 : Thống kê | Chi tiết giao thức ( Protocol Details )
### IPv4 và IPv6
- Tùy chọn đều cung cấp thông tin chứa cả hai phiên bản địa chỉ IP
- Menu thống kê có hai tùy chọn để thu hẹp thống kê về các gói tin chứa phiên bản IP cụ thể

![image](/images/abac4bcb4cd5676988ce744556fef72e.png)

### DNS 
- Phân tích tất cả các gói DNS từ tệp thu thập và giúp các nhà phân tích xem kết quả dưới dạng cây dựa trên bộ đếm gói và tỷ lệ phần trăm của giao thức DNS

![image](/images/cf2205bc15581c453270531f607b5d3b.png)

### HTTP
- Phân tích tất cả các gói HTTP từ tệp thu thập và giúp các nhà phân tích xem kết quả dưới dạng cây dựa trên bộ đếm gói và tỷ lệ phần trăm của giao thức HTTP

![image](/images/8e3b293fa5490e489c87d9744d9d5985.png)

## Misson 3 : Lọc gói tin | Nguyên tắc
### Giới thiệu

| Capture Filters | Display Filters |
| -------- | -------- |
| Tạm hiểu lọc bằng lệnh     | Tạm hiểu lọc bằng các tùy chọn    |

### Cú pháp lọc Capture
- Bộ lọc này sử dụng các giá trị hex offset byte và mặt nạ với toán tử boolean
    > Phạm vi : host, net, port and portrange
    > Hướng : src, dst, src hoặc dst, src và dst
    > Giao thức : ether, wlan, ip, ip6, ARP. rarp, tcp và udp
    > Bộ lọc mẫu để thu thập lưu lượng cổng 80 : `tcp port 80` 
- Tài liệu tham khảo nhanh có sẵn

![image](/images/86db891ced54f8b1e298dffcf5647099.png)

### Cú pháp lọc Display
- **Display Filter Expression** lưu trữ tất cả các cấu trúc giao thức được hỗ trợ để giúp các nhà phân tích tạo bộ lọc hiển thị
- Tài liệu tham khảo nhanh có sẵn

![image](/images/fbb1982516f75eace0f1fcb92897217b.png)

### Các bài toán so sánh

| Eng | Cú phát | Nghĩa             | Ví dụ                  |
| --- | ------- | ----------------- | ---------------------- |
| eq  | ==      | Bằng              | `ip.src == 10.10.10.100` |
| ne  | !=      | Khác              | `ip.src != 10.10.10.100` |
| gt  | >       | Lớn hơn           | `ip.ttl > 250`           |
| lt  | <       | Bé hơn            | `ip.ttl < 10`           |
| ge  | >=      | Lớn hơn hoặc bằng | `ip.ttl >= 0xFA`         |
le|<=|Bé hơn hoặc bằng|`ip.ttl <= 0xA`|

### Các biểu thức logic 

| Eng | Cú pháp | Nghĩa |                                                       |
| --- | ------- | ----- | ----------------------------------------------------- |
| and | &&      | và    | `(ip.src == 10.10.10.100) and (ip.src == 10.10.10.111)` |
or| &#124;&#124; | hoặc | `(ip.src == 10.10.10.100) or (ip.src == 10.10.10.111)` |
not | ! | không | `!(ip.src == 10.10.10.222)`

### Thanh công cụ lọc gói
- Đây là một thanh công cụ thông minh giúp bạn dễ dàng tạo bộ lọc hiển thị hợp lệ
    > Bộ lọc được định nghĩa bằng chữ thường
    > Bộ lọc có tính năng tự động hoàn thành
    > Bộ lọc được biểu diễn bằng 3 màu

![image](/images/28c2286d54f0201c332690072feabf36.png)

![image](/images/2ec007e994183279fa72edf2af0342f9.png)

- Các tính năng của thanh lọc 

![image](/images/3db4370f5ecd715aa02405a1084362a4.png)

## Misson 4 : Lọc gói tin | Lọc giao thức
### Lọc giao thức
- Tác vụ này hiển thị việc tạo và sử dụng bộ lọc dựa trên các trường giao thức khác nhau

### Lọc IP
- Giúp các nhà phân tích lọc lưu lượng theo thông tin IP từ các gói tin ( lớp mạng của mô hình OSI )

| Bộ lọc | Mô tả |
| ------ | ----- |
|`ip`|Hiển thị tất cả gói IP|
|`ip.addr == 10.10.10.111`|Hiển thị tất cả các gói chứa địa chỉ IP 10.10.10.111|
|`ip.addr == 10.10.10.0/24`|Hiển thị tất cả các gói chứa địa chỉ IP từ mạng con 10.10.10.0/24|
|`ip.src == 10.10.10.111`|Hiển thị tất cả các gói tin xuất phát từ 10.10.10.111|
|`ip.dst == 10.10.10.111`|Hiển thị tất cả các gói tin đã gửi đến 10.10.10.111|

### Lọc TCP và UDP
- Giúp các nhà phân tích lọc lưu lượng theo thông tin giao thức từ các gói tin ( lớp Transport của mô hình OSI )

| Bộ lọc | Mô tả | Bộ lọc  | Mô tả |
| ------ | ----- | ---- | ------- |
| `tcp.port == 80`|Hiển thị tất cả TCP các gói tin có cổng 80|`udp.port == 53`|Hiển thị tất cả UDP gói tin có cổng 53|
|`tcp.srcport == 1234`|Hiển thị tất cả các gói TCP có nguồn gốc từ cổng 1234|`udp.srcport == 1234`|Hiển thị tất cả các gói UDP xuất phát từ cổng 1234|
|`tcp.dstport == 80`|Hiển thị tất cả các gói TCP gửi đến cổng 80|`udp.dstport == 5353`|Hiển thị tất cả các gói UDP gửi đến cổng 5353|

### Lọc HTTP và DNS
- Giúp các nhà phân tích lọc lưu lượng theo thông tin cấp giao thức ứng dụng từ các gói tin ( lớp ứng dụng của mô hình OSI )

| Bộ lọc | Miêu tả | Bộ lọc | Miêu tả    |
| -------- | -------- | -------- | --- |
|`http`|Hiển thị tất cả HTTP các gói|`dns`|Hiển thị tất cả DNS các gói|
|`http.response.code == 200`|Hiển thị tất cả các gói tin có mã phản hồi HTTP "200"|`dns.flags.response == 0`|Hiển thị tất cả yêu cầu DNS|
|`http.request.method == "GET"`|Hiển thị tất cả các yêu cầu HTTP GET|`dns.flags.response == 1`|Hiển thị tất cả phản hồi DNS|
|`http.request.method == "POST"`|Hiển thị tất cả các yêu cầu HTTP POST|`dns.qry.type == 1`|Hiển thị tất cả bản ghi DNS "A"|

### Lọc hiển thị ( Display Filter Expressions )
- Menu **Display Filter Expressions** cung cấp hướng dẫn xây dựng bộ lọc hiển thị dễ sử dụng

![image](/images/a78f83cf475ae9f4a541d68c2703b5a8.png)

## Misson 5 : Lọc nâng cao
### Giới thiệu
- Giúp nhà phân tích tiến hành phân tích sâu về một sự kiện quan tâm

### Lọc : "contains"

| | |
| :--- | :--- |
| **Bộ lọc** | contains |
| **Loại** | So sánh |
| **Mô tả** | Tìm kiếm một giá trị bên trong các gói |
| **Ví dụ** | Tìm tất cả "Apache" máy chủ|
|**Quy trình**|Liệt kê tất cả HTTP các gói tin mà trường "server" của gói tin chứa từ khóa "Apache"|
| **Lệnh** | `http.server contains "Apache"` |

![image](/images/24aa0ee039a2868264d804492ebdd847.png)

### Lọc : "matches"

| | |
| :--- | :--- |
| **Bộ lọc** | matches |
| **Loại** | So sánh |
| **Mô tả** | Tìm theo mẫu, không phiên biệt chữ hoa và thường |
| **Ví dụ** | Tìm trang .php và .html  |
| **Quy trình** | Liệt kê tất cả các gói HTTP mà trường "host" của gói trùng với từ khóa ".php" hoặc ".html" |
| **Lệnh** |`http.host matches "\.(php\|html)"`|

![image](/images/361663785c119c2502aad2e9f15b1628.png)

### Lọc : "in"

| | |
| :--- | :--- |
| **Bộ lọc** | in |
| **Loại** | Kiểm tra trong list |
| **Mô tả** | Tìm kiếm một giá trị hoặc trường trong phạm vi cụ thể |
| **Ví dụ** | Tìm tất cả các gói tin sử dụng cổng 80, 443 hoặc 8080 |
| **Quy trình** | Liệt kê tất cả các gói TCP mà các trường "port" của gói tin có giá trị 80, 443 hoặc 8080 |
| **Lệnh** | `tcp.port in {80 443 8080}` |

![image](/images/73c6224277eab40de096973223708fe8.png)

### Lọc : "upper"

| | |
| :--- | :--- |
| **Bộ lọc** | upper |
| **Loại** | Chức năng |
| **Mô tả** | Chuyển đổi chuỗi sang chữ hoa |
| **Ví dụ** | Tìm tất cả các máy chủ "APACHE" |
| **Quy trình** | Chuyển đổi tất cả các trường "server" của gói HTTP sang chữ hoa và liệt kê các gói chứa từ khóa "APACHE" |
| **Lệnh** | `upper(http.server) contains "APACHE"` |

![image](/images/c84c788ba0e8c9187d53dde7ac135b0c.png)

### Lọc : "lower"

| | |
| :--- | :--- |
| **Bộ lọc** |lower|
| **Loại** | Chức năng |
| **Mô tả** | Chuyển đổi giá trị chuỗi sang chữ thường |
| **Ví dụ** | Tìm tất cả các máy chủ "apache" |
| **Quy trình** | Chuyển đổi thông tin trường "máy chủ" của tất cả các gói HTTP sang chữ thường và liệt kê các gói chứa từ khóa "apache" |
| **Lệnh** | `lower(http.server) contains "apache"` |

![image](/images/0bf0f67b4beca410ca476177552dad50.png)

### Lọc : "string"

| | |
| :--- | :--- |
| **Bộ lọc** | string |
| **Loại** | Chức năng |
| **Mô tả** | Chuyển đổi giá trị không phải chuỗi thành chuỗi |
| **Ví dụ** | Tìm tất cả frame có số lẻ |
| **Quy trình** | Chuyển tất cả các trường "frame" thành giá trị chuỗi, và các khung danh sách kết thúc bằng giá trị lẻ |
| **Lệnh** | `string(frame.number) matches "[13579]$"` |

![image](/images/a26fd6f1862ab35e41523377df95a0f8.png)

### Dấu trang và nút lọc 
- Dấu trang giúp các nhà phân tích tái sử dụng các bộ lọc yêu thích/phức tạp chỉ với vài cú nhấp chuột
- Tương tự như dấu trang, bạn có thể tạo các nút lọc sẵn sàng áp dụng chỉ với một cú nhấp chuột

![image](/images/5acad1f3025ccae2facb98eada65def4.png)

![image](/images/f808c256f924b164c52e7b825ffa35c7.png)

### Hồ sơ ( Profiles )
- Giúp tạo nhiều hồ sơ cho các vụ án điều tra khác nhau và sử dụng chúng cho phù hợp

![image](/images/eeb6bbdbe375ab8fee68424ea5b7e826.png)

# III. Wireshark: Traffic Analysis
## Mission 1 : Nmap Scans
### Giới thiệu
- Công cụ tiêu chuẩn ngành để lập bản đồ mạng, xác định các máy chủ trực tiếp và khám phá các dịch vụ
- Các loại quét Nmap phổ biến nhất 
    > TCP connect scans
    > SYN scans
    > UDP scans
- Các bộ lọc Nmap đơn giản

| Ghi chú | Bộ lọc Wireshark |
| :--- | :--- |
| Tìm kiếm  | - `tcp`<br>- `udp` |
| - Chỉ có cờ SYN<br>- Cờ SYN đã được thiết lập. Những phần còn lại không quan trọng | - `tcp.flags == 2`<br>- `tcp.flags.syn == 1` |
| - Chỉ có cờ ACK<br>- Cờ ACK đã được đặt. Những phần còn lại không quan trọng | - `tcp.flags == 16`<br>- `tcp.flags.ack == 1` |
| - Chỉ có cờ SYN, ACK<br>- SYN và ACK đã sẵn sàng.Những phần còn lại không quan trọng. | - `tcp.flags == 18`<br>- `(tcp.flags.syn == 1) and (tcp.flags.ack == 1)` |
| - Chỉ có cờ RST<br>- Cờ RST đã được đặt. Những phần còn lại không quan trọng | - `tcp.flags == 4`<br>- `tcp.flags.reset == 1` |
| - Chỉ có cờ RST, ACK<br>- RST và ACK đã được thiết lập. Những phần còn lại không quan trọng | - `tcp.flags == 20`<br>- `(tcp.flags.reset == 1) and (tcp.flags.ack == 1)` |
| - Chỉ có cờ FIN<br>- Cờ FIN đã được đặt. Những phần còn lại không quan trọng | - `tcp.flags == 1`<br>- `tcp.flags.fin == 1` |

### Quét TCP Connect
- Tóm tắt về TCP Connect Scan
    > Dựa vào bắt tay 3 bước
    > Được sử dụng bởi người dùng ( ko root )
    > Thường có kích thước WIn lớn hơn 1024 byte

| Mở cổng TCP | Mở cổng TCP | Cổng TCP đã đóng |
| -------- | -------- | -------- |
|  SYN --> <br> <-- SYN, ACK <br> ACK -->     | SYN --> <br> <-- SYN, ACK <br> ACK --> <br> RST, ACK -->     | SYN --> <br> <-- RST, ACK |

- Mở cổng TCP ( kết nối )

![image](/images/2968b04af4f4ceeca3482a1f7dcba5b3.png)

- Cổng TCP đóng ( kết nối )

![image](/images/720956f186ef301f2fdd505362e7a733.png)

- Bộ lọc được cung cấp hiển thị các mẫu quét TCP Connect trong tệp ghi hình
`tcp.flags.syn==1 and tcp.flags.ack==0 and tcp.window_size > 1024`

![image](/images/2344ac208ae1fa1ba77859260b6fee4c.png)

### Quét UDP
- Tóm tắt
    > Không cần bắt tay
    > Không cần báo mở cổng
    > Thông báo lỗi ICMP khi đóng cổng


| Mở cổng UDP | Cổng UDP đã đóng |
| -------- | -------- |
| Gói UDP --> | Gói UDP --> <br> ICMP Type 3, Code 3 message ( Destination unreachable, port unreachable )  |

- Đóng ( cổng số 69 ) và mở ( cổng số 68 ) UDP ports

![image](/images/e3acfbf58fe80d2401f54686ecfd9c42.png)

- Khi bạn mở rộng phần ICMP trong khung chi tiết gói tin, bạn sẽ thấy dữ liệu đóng gói và yêu cầu gốc

![image](/images/a2fe6ec0d0ea681ebaa20f6df0621430.png)

- Bộ lọc cung cấp hiển thị UDP trong tệp
`icmp.type==3 and icmp.code==3`

![image](/images/d131071d70ea0e3e861d7055f8b567bc.png)

## Misson 2 : ARP Poisoning/ Spoofing ( Cuộc tấn công người ở giữa )
### Giới thiệu 
- Một loại tấn công liên quan đến việc gây nhiễu/thao túng mạng bằng cách gửi các gói ARP độc hại đến cổng mặc định
- Phân tích ARP tóm tắt 
    > Hoạt động trên mạng nội bộ
    > Cho phép giao tiếp giữa các địa chỉ MAC
    > Không phải gia thức an toàn
    > Không phải giao thức có thể định tuyến
    > Nó không có chức năng xác thực
    > Các mẫu phổ biến là yêu cầu và phẩn hồi, thông báo và các gói dữ liệu không cần thiết

| Ghi chú | Bộ lọc Wireshark |
| ------- | ---------------- |
| Tìm kiếm|`arp`|
| **Các lựa chọn "ARP" để nắm bắt những lợi ích dễ dàng:** <br> Mã số 1 : Yêu cầu ARP <br> Mã số 2 : Phản hồi ARP <br> Hunt : Quét ARP <br> Hunt : Khả năng phát hiện ARP Poisoning <br> Hunt : Khả năng phát hiện ARP flooding | `arp.opcode == 1` <br> `arp.opcode == 2` <br>  `arp.dst.hw_mac==00:00:00:00:00:00` <br> `arp.duplicate-address-detected or arp.duplicate-address-frame` <br> ``((arp) && (arp.opcode == 1)) && (arp.src.hw_mac == target-mac-address)``|

- Yêu cầu ARP

![image](/images/da6e277c1ac4b8f17ec774035293ee42.png)

- Phản hồi ARP 

![image](/images/02ea2e816371c8ba9837a82270a788b3.png)

- Một tình huống đáng ngờ có nghĩa là có hai phản hồi ARP khác nhau (xung đột) cho một địa chỉ IP cụ thể

![image](/images/39c183e291db00b8b58852e745026904.png)

## Mission 3 : Xác định máy chủ : DHCP, NetBIOS và Kerberos
### Nhận diện máy chủ
- Một trong những phương pháp tốt nhất là xác định các máy chủ và người dùng trên mạng để quyết định điểm bắt đầu điều tra và liệt kê các máy chủ cùng người dùng liên quan đến lưu lượng/hoạt động độc hại
- Các giao thức có thể sử dụng trong nhận dạng máy chủ và người dùng
    > Giao thức cấu hình Protocol ( DHCP ) traffic
    > NetBIOS ( NBNS ) traffic
    > Kerberos traffic
### Phân tích DHCP
- Công nghệ chịu trách nhiệm quản lý địa chỉ IP tự động và các thông số giao tiếp cần thiết

| Ghi chú | Bộ lọc Wireshark |
| :--- | :--- |
| Tìm kiếm toàn cầu. | - `dhcp` hoặc `bootp` |
| Lọc các tùy chọn gói DHCP phù hợp là rất quan trọng để tìm ra sự kiện quan trọng.<br><br>- Các gói "DHCP Request" chứa thông tin tên máy chủ<br>- Các gói "DHCP ACK" đại diện cho các yêu cầu được chấp nhận<br>- Các gói "DHCP NAK" đại diện cho các yêu cầu bị từ chối<br><br>Do tính chất của giao thức, chỉ có "Tùy chọn 53" (loại yêu cầu) có giá trị tĩnh được định nghĩa trước. Bạn nên lọc loại gói trước, sau đó có thể lọc các tùy chọn còn lại bằng cách "áp dụng dưới dạng cột" hoặc dùng các bộ lọc nâng cao như "chứa" và "khớp". | - Yêu cầu: `dhcp.option.dhcp == 3`<br>- ACK: `dhcp.option.dhcp == 5`<br>- NAK: `dhcp.option.dhcp == 6` |
| Các lựa chọn "Yêu cầu DHCP" để nắm bắt những lợi ích dễ dàng:<br><br>- **Lựa chọn 12:** Tên máy chủ.<br>- **Lựa chọn 50:** Địa chỉ IP được yêu cầu.<br>- **Lựa chọn 51:** Thời gian thuê IP đã yêu cầu.<br>- **Lựa chọn 61:** Địa chỉ MAC của khách hàng. | - `dhcp.option.hostname contains "keyword"` |
| Các lựa chọn "DHCP ACK" để nắm bắt những lợi ích dễ dàng:<br><br>- **Lựa chọn 15:** Tên miền.<br>- **Lựa chọn 51:** Thời gian thuê IP đã được phân công. | - `dhcp.option.domain_name contains "keyword"` |
| Các lựa chọn "DHCP NAK" để nắm bắt những lợi ích dễ dàng:<br><br>- **Lựa chọn 56:** Tin nhắn (chi tiết/lý do từ chối). | Vì thông điệp có thể duy nhất tùy theo trường hợp/tình huống, nên nên đọc thông điệp thay vì lọc nó. Do đó, nhà phân tích có thể tạo ra giả thuyết/kết quả đáng tin cậy hơn bằng cách hiểu các hoàn cảnh sự kiện. |

![image](/images/0fb5449fb533fa3b228607738467cc9e.png)

### Phân tích NetBIOS ( NBNS )
- Công nghệ chịu trách nhiệm cho phép các ứng dụng trên các máy chủ khác nhau giao tiếp với nhau

| Ghi chú | Bộ lọc Wireshark |
| -------- | -------- |
|Tìm kiếm|`nbns`|
| Các lựa chọn **"NBNS"** để nắm bắt những lợi ích dễ dàng: <br> **Truy vấn**:Chi tiết truy vấn <br> Chi tiết truy vấn có thể chứa **"tên, Thời gian sống (TTL) và chi tiết địa chỉ IP"** | `nbns.name contains "keyword"` |

![image](/images/96377b2ec9ad3f345cfc4884412e81d1.png)

### Phân tích Kerberos
- Nó chịu trách nhiệm xác thực các yêu cầu dịch vụ giữa hai hoặc nhiều máy tính qua mạng không đáng tin cậy

| Ghi chú | Bộ lọc Wireshark |
| :--- | :--- |
| Tìm kiếm toàn cầu. | - `kerberos` |
| Tìm kiếm tài khoản người dùng:<br><br>- **CNameString:** Tên người dùng.<br><br>Lưu ý: Một số gói tin có thể cung cấp thông tin tên máy chủ trong trường này. Để tránh sự nhầm lẫn này, hãy lọc giá trị ` "$" `. Các giá trị kết thúc bằng ` "$" ` là tên máy chủ, và những giá trị không có là tên người dùng. | - `kerberos.CNameString contains "keyword"`<br>- `kerberos.CNameString and ! (kerberos.CNameString contains "$" )` |
| Các lựa chọn "Kerberos" để nắm bắt những lợi ích dễ dàng:<br><br>- **PVNO:** Phiên bản giao thức.<br>- **Realm:** Tên miền cho vé được tạo.<br>- **SNAME:** Dịch vụ và tên miền cho phiếu hỗ trợ được tạo.<br>- **Địa chỉ:** Địa chỉ IP của máy khách và tên NetBIOS.<br><br>Lưu ý: thông tin "địa chỉ" chỉ có trong các gói yêu cầu. | - `kerberos.pvno == 5`<br>- `kerberos.realm contains ".org"`<br>- `kerberos.SNameString == "krbtg"` |

![image](/images/68e9c827d935c4265d2aafef2857f41d.png)

## Mission 4 : Lưu lượng xuyên hầm : DNS và ICMP
### Giao thông đào hầm ICMP và DNS 
- Là truyền dữ liệu/tài nguyên theo phương pháp an toàn đến các phân đoạn và vùng mạng
- Tunnelling mang lại sự ẩn danh và an ninh giao thông
### Phân tích ICMP
- Được thiết kế để chẩn đoán và báo cáo các sự cố giao tiếp mạng

| Ghi chú | Bộ lọc Wireshark |
| ------- | ---------------- |
| Tìm kiến|`icmp`|
| **Các lựa chọn "ICMP" để nắm bắt những lợi ích dễ dàng:** <br> Độ dài gói <br> Địa chỉ đích ICMP <br> Các ký hiệu giao thức được đóng gói trong tải trọng ICMP| `data.len > 64 and icmp`|

![image](/images/050a4d5cfed243855597038d21c61d51.png)

### Phân tích DNS
- Được thiết kế để chuyển đổi/chuyển đổi địa chỉ miền IP thành địa chỉ IP

| Ghi chú | Bộ lọc Wireshark |
| :--- | :--- |
| Tìm kiếm toàn cầu | - `dns` |
| Các lựa chọn "DNS" để nắm bắt những lợi ích dễ dàng:<br><br>- Độ dài truy vấn.<br>- Tên bất thường và không đều trong địa chỉ DNS.<br>- Địa chỉ DNS dài với địa chỉ tên miền phụ được mã hóa.<br>- Các mẫu đã biết như dnscat và dns2tcp.<br>- Phân tích thống kê như khối lượng yêu cầu DNS bất thường cho một mục tiêu cụ thể.<br><br>`!mdns`: Vô hiệu hóa truy vấn thiết bị liên kết cục bộ. | - `dns contains "dnscat"`<br>- `dns.qry.name.len > 15 and !mdns` |

![image](/images/0a075dae8dca789d432a33524cc4c6a9.png)

## Mission 5 : Phân tích giao thức Cleartext : FTP
### Phân tích giao thức Cleartext
### FTP phân tích
- Được thiết kế để truyền tệp một cách dễ dàng, vì vậy nó tập trung vào sự đơn giản hơn là bảo mật
    > MITM các cuộc tấn công
    > Đánh cắp thông tin đăng nhập và truy cập trái phép
    > Phishing
    > Gài phần mềm độc hại
    > Trích xuất dữ liệu

| Ghi chú | Bộ lọc Wireshark |
| :--- | :--- |
| Tìm kiếm toàn cầu | - `ftp` |
| Các lựa chọn "FTP" để nắm bắt những lợi ích dễ dàng:<br><br>- **Dòng x1x:** Phản hồi yêu cầu thông tin.<br>- **Dòng x2x:** Thông báo kết nối.<br>- **Dòng x3x:** Thông điệp xác thực.<br><br>Lưu ý: "200" nghĩa là lệnh thành công. | --- |
| Các lựa chọn trong dòng "x1x" để nắm bắt những lợi ích dễ dàng:<br><br>- **211:** Tình trạng hệ thống.<br>- **212:** Trạng thái thư mục.<br>- **213:** Tình trạng tệp | - `ftp.response.code == 211` |
| Các lựa chọn trong dòng "x2x" để nắm bắt những lợi ích dễ dàng:<br><br>- **220:** Dịch vụ sẵn sàng.<br>- **227:** Đang vào chế độ thụ động.<br>- **228:** Chế độ thụ động kéo dài.<br>- **229:** Chế độ thụ động mở rộng. | - `ftp.response.code == 227` |
| Các lựa chọn dòng "x3x" để nắm bắt những lợi ích dễ dàng:<br><br>- **230:** Đăng nhập người dùng.<br>- **231:** Đăng xuất người dùng.<br>- **331:** Tên người dùng hợp lệ.<br>- **430:** Tên đăng nhập hoặc mật khẩu không hợp lệ.<br>- **530:** Không đăng nhập, mật khẩu không hợp lệ. | - `ftp.response.code == 230` |
| Các lệnh "FTP" để nắm bắt những lợi ích dễ dàng:<br><br>- **NGƯỜI DÙNG:** Tên người dùng.<br>- **ĐẠT:** Mật khẩu.<br>- **CWD:** Thư mục công việc hiện tại.<br>- **DANH SÁCH:** Danh sách. | - `ftp.request.command == "USER"`<br>- `ftp.request.command == "PASS"`<br>- `ftp.request.arg == "password"` |
| Ví dụ về cách sử dụng nâng cao để nắm bắt những lợi ích dễ dàng:<br><br>- **Tín hiệu bruteforce:** Liệt kê các lần đăng nhập thất bại.<br>- **Tín hiệu bruteforce:** Danh sách tên người dùng mục tiêu.<br>- **Tín hiệu phun mật khẩu:** Liệt kê các mục tiêu cho mật khẩu tĩnh. | - `ftp.response.code == 530`<br>- `(ftp.response.code == 530) and (ftp.response.arg contains "username")`<br>- `(ftp.request.command == "PASS" ) and (ftp.request.arg == "password")` |

![image](/images/19d3395533944eb69273536ed4748c59.png)

## Mission 6 : Phân tích giao thức Cleartext : HTTP
### HTTP Phân tích
- Là một giao thức dựa trên văn bản rõ, kết hợp yêu cầu-phản hồi và giao thức client-server
    > Phishing các trang
    > Các cuộc tấn công web
    > Trích xuất dữ liệu
    > Giao thông chỉ hay và kiểm soát ( C2 )

| Ghi chú | Bộ lọc Wireshark |
| :--- | :--- |
| Tìm kiếm toàn cầu<br><br>Lưu ý: HTTP2 là phiên bản sửa đổi của giao thức HTTP nhằm nâng cao hiệu suất và bảo mật. Nó hỗ trợ truyền dữ liệu nhị phân và ghép kênh yêu cầu&phản hồi. | - `http`<br>- `http2` |
| "Phương thức yêu cầu HTTP" để nắm bắt những lợi ích dễ dàng:<br><br>- LẤY<br>- BƯU TIÊN<br>- Yêu cầu: Liệt kê tất cả các yêu cầu | - `http.request.method == "GET"`<br>- `http.request.method == "POST"`<br>- `http.request` |
| "Mã trạng thái phản hồi HTTP" để nắm bắt những lợi ích dễ dàng:<br><br>- **200 OK:** Yêu cầu thành công.<br>- **301 Di chuyển vĩnh viễn:** Tài nguyên được di chuyển đến URL/đường dẫn mới (vĩnh viễn).<br>- **302 Di chuyển tạm thời:** Tài nguyên được di chuyển đến URL/đường dẫn mới (tạm thời).<br>- **400 Yêu cầu xấu:** Nhân viên phục vụ không hiểu yêu cầu đó.<br>- **401 Không được phép:** URL cần xác thực (đăng nhập, v.v.).<br>- **403 Cấm:** Không có quyền truy cập URL được yêu cầu.<br>- **404 Không tìm thấy:** Máy chủ không tìm thấy URL được yêu cầu.<br>- **Phương pháp 405 không được phép:** Phương pháp sử dụng không phù hợp hoặc bị chặn.<br>- **Thời gian chờ yêu cầu 408:** Yêu cầu trông dài hơn thời gian chờ của máy chủ.<br>- **Lỗi máy chủ nội bộ 500:** Yêu cầu chưa hoàn thành, lỗi bất ngờ.<br>- **Dịch vụ 503 Không khả dụng:** Yêu cầu chưa hoàn thành máy chủ hoặc dịch vụ bị sập. | - `http.response.code == 200`<br>- `http.response.code == 401`<br>- `http.response.code == 403`<br>- `http.response.code == 404`<br>- `http.response.code == 405`<br>- `http.response.code == 503` |
| "Tham số HTTP" để nắm bắt những lợi ích dễ dàng:<br><br>- **User agent:** Nhận diện trình duyệt và hệ điều hành với ứng dụng máy chủ web.<br>- **Yêu cầu URI:** Trỏ tài nguyên được yêu cầu khỏi máy chủ.<br>- **\*URI đầy đủ:** Thông tin đầy đủ về URI.<br><br>\*URI: Định danh Tài nguyên Thống nhất. | - `http.user_agent contains "nmap"`<br>- `http.request.uri contains "admin"`<br>- `http.request.full_uri contains "admin"` |
| "Tham số HTTP" để nắm bắt những lợi ích dễ dàng:<br><br>- **Máy chủ:** Tên dịch vụ máy chủ.<br>- **Người dẫn chương trình:** Tên máy chủ của máy chủ<br>- **Kết nối:** Trạng thái kết nối.<br>- **Dữ liệu văn bản dựa trên dòng:** Dữ liệu văn bản rõ do máy chủ cung cấp.<br>- **URL biểu mẫu HTML đã mã hóa:** Thông tin biểu mẫu web. | - `http.server contains "apache"`<br>- `http.host contains "keyword"`<br>- `http.host == "keyword"`<br>- `http.connection == "Keep-Alive"`<br>- `data-text-lines contains "keyword"` |

### Phân tích User Agent

| Ghi chú | Bộ lọc Wireshark |
| :--- | :--- |
| Tìm kiếm toàn cầu. | - `http.user_agent` |
| Kết quả nghiên cứu để nắm bắt những thành quả dễ hái:<br><br>- Thông tin user agent khác nhau từ cùng một máy chủ trong thời gian ngắn.<br>- Thông tin user agent không chuẩn và tùy chỉnh.<br>- Sự khác biệt về chính tả tinh tế. ("Mozilla" không giống với "Mozlilla" hay "Mozlila")<br>- Kiểm tra thông tin các công cụ như Nmap, Nikto, Wfuzz và sqlmap trong trường user agent.<br>- Dữ liệu payload trong trường user agent. | - `(http.user_agent contains "sqlmap") or (http.user_agent contains "Nmap") or (http.user_agent contains "Wfuzz") or (http.user_agent contains "Nikto")` |

![image](/images/6b7dc3c5d48279b615ce5d7f6b89c00b.png)

### Phân tích Log4j

| Ghi chú | Bộ lọc Wireshark |
| :--- | :--- |
| Kết quả nghiên cứu để nắm bắt những thành quả dễ hái:<br><br>- Cuộc tấn công bắt đầu với yêu cầu "POST"<br>- Có các mẫu văn bản rõ ràng đã biết: "jndi:ldap" và "Exploit.class". | - `http.request.method == "POST"`<br>- `(ip contains "jndi") or ( ip contains "Exploit")`<br>- `(frame contains "jndi") or ( frame contains "Exploit")`<br>- `(http.user_agent contains "$") or (http.user_agent contains "==")` |

![image](/images/35bb5d8ddb49972956d4eb952224df6b.png)

## Phân tích giao thức mã hóa : Giải mã HTTPS
### Giải mã lưu lượng HTTPS
- Tăng cường bảo mật chống lại các cuộc tấn công giả mạo, đánh dấu và chặn

| Ghi chú | Bộ lọc Wireshark |
| :--- | :--- |
| "Tham số HTTPS" để nắm bắt những lợi ích dễ dàng:<br><br>- **Yêu cầu:** Liệt kê tất cả yêu cầu<br>- **TLS:** Tìm kiếm TLS toàn cục<br>- Yêu cầu Khách hàng TLS<br>- Phản hồi của máy chủ TLS<br>- Giao thức Khám phá Dịch vụ Đơn giản cục bộ (SSDP)<br><br>Lưu ý: SSDP là một giao thức mạng cung cấp quảng cáo và khám phá các dịch vụ mạng. | - `http.request`<br>- `tls`<br>- `tls.handshake.type == 1`<br>- `tls.handshake.type == 2`<br>- `ssdp` |

![image](/images/6c570950128284f337528f788e4e224d.png)

- Tương tự như quy trình bắt tay ba chiều TCP, giao thức TLS cũng có quy trình bắt tay riêng
- Hai bước đầu tiên chứa các thông điệp "Client Hello" và "Server Hello"
- Xin chào khách hàng: ``(http.request or tls.handshake.type == 1) and !(ssdp)``
- Xin chào máy chủ: ``(http.request or tls.handshake.type == 2) and !(ssdp)``

![image](/images/32f27be73e73e55e5e3af4fe41e603b6.png)

## Mission 7 : Thông tin đăng nhập Hunt Cleartext

![image](/images/deb07fe7be3e51c9c19960bf6cfc3db9.png)

## Mission 8 : Phần thưởng : Kết quả có thể hành động !
- Hiện tại, Wireshark có thể tạo các quy tắc cho
    > Netfilter (iptables)
    > Cisco IOS (tiêu chuẩn/mở rộng)
    > Bộ lọc IP (ipfilter)
    > IPFirewall (ipfw)
    > Bộ lọc gói tin (pf)
    > Windows Firewall (netsh định dạng mới/cũ)

![image](/images/f8b762b1d221480bcddeade03deb6bf6.png)
