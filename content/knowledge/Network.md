---
title: Network
tags: ["Knowledge"]
---

# . Giao thức TCP
- Các tệp tin gửi đi bởi TCP sẽ được đánh dấu và kiểm tra, nếu thiếu thì gửi lại
- Các tệp tin sẽ được đánh số thứ tự, lần lượt
    > Vì 2 lí do trên nên tuy tốc độ chậm nhưng có độ chính xác, tin cậy cao
- Phù hợp để gửi những tệp tin đòi hỏi sự chính xác như : Gmail, Ngân hàng v.v
- TCP có cơ chế bắt tay (3-way handshake )
    >Bước 1 : **Client gửi yêu cầu** tới Server : SYN ( SYN : The Synchronous Idle Character - Ký tự đồng bộ hóa )
Bước 2 : **Server gửi phản hồi** chấp nhận tới Client : SYN + ACK ( ACK : Acknowledgement - Chấp nhận )
Bước 3 : **Client gửi xác nhận** tới Server : ACK 
Khi này quy trình hoàn tất, đánh số thứ tự được đồng bộ, dữ liệu sẵn sàng gửi tới máy chủ

![image](https://hackmd.io/_uploads/rylax2bdGx.png)
 
# II. Giao thức UDP
- Các tệp tin gửi đi bởi UDP sẽ được gửi đi hàng loạt
- Các tệp tin sẽ ko được đánh số, ko được kiểm tra
    > Vì 2 lí do trên nên tốc độ tuy nhanh nhưng tộ tin cậy thấp
- Phù hợp trong môi trường đòi hỏi tốc độ : Game online, Video Youtube, v.v

![image](https://hackmd.io/_uploads/HJE0x3Zdzl.png)

# III. So sánh TCP và UDP
![image](https://hackmd.io/_uploads/rkZb-2bdfg.png)

- UDP được sử dụng cho DNS vì DNS sẽ không cần mất thời gian kết nối
- HTTP hay HTTPS là các đối tượng web cần tải về chính xác nên sử dụng TCP 

# IV. Giao thức HTTP
- HTTP (HyperText Transfer Protocol ) là giao thức truyền tải siêu văn bản
- Cách thức hoạt động của HTTP dựa trên mô hình Yêu cầu-phản hồi giữa Client và Server 
    >Bước 1 : Người dùng nhập URL, Client gửi yêu cầu tới Server chứa nội dung đó
Bước 2 : Máy chủ sẽ phản hồi với dữ liệu được yêu cầu

![image](https://hackmd.io/_uploads/r1cb-3WuMe.png)

- Khía cạnh cơ bản của HTTP
    > 1.HTTP đơn giản : Được thiết kế với tính đơn giản, rõ ràng giúp dễ dàng kiểm thử và sửa lỗi
2.HTTP là stateless, nhưng không thể mở rộng :
stateless (không trạng thái ) có nghĩa là mỗi yêu cầu gửi đi không liên kết nào với yêu cầu trước đó
				--> đòi hỏi sự bổ sung như cookie, session
		3. HTTP có thể mở rộng phục phụ nhu cầu cụ thể :
			HTTPS : tăng cường bảo mật
			HTTP/2 và HTTP/3 : tăng cường tốc độ

# V. Giao thức HTTPS

- HTTPS (Hypertext Transfer Protocol Secure ) giao thức truyền tải siêu văn bản an toàn
- Bản chất là HTTPS nhưng thêm SSL (Secure Sockets Layer - tầng ổ bảo mật ) hoặc TLS (Transport Layer Security - bảo mật tầng truyền tải )
- SSL và TLS đều sử dụng hệ thống PKI (Public Key Infrastructure - hạ tầng khóa công khai ) không đối xứng
- Hệ thống sử dụng 2 khóa để mã hóa thông tin liên lạc, gồm Public Key và Private Key
- Thứ gì được mã hóa bằng Public Key chỉ được giải mã bảo Private Key và ngược lại
	> Đảm bảo nội dung đc mã hóa khi truyền và giải mã khi nhận
            
![image](https://hackmd.io/_uploads/ryQfbhbdGx.png)

# VI. So sánh HTTP và HTTPS

![image](https://hackmd.io/_uploads/BJJQZh-_Gg.png)

# VII. Giao thức DNS

- DNS (Domain Name System ) phân giải tên miền dễ nhớ như facebook.com thành địa chỉ IP và ngược lại	
- Giống như danh bạ cho phép người dùng truy cập thông qua tên miền dễ nhớ 
- Quản lý tên miền và bản ghi DNS khác nhau
	>**A record (Address)**: Liên kết tên miền với địa chỉ IPv4 thật
**MX (Mail Exchange)**: Xác định máy chủ nhận email
**CNAME (Canonical Name)**: Tạo bí danh, giúp chuyển hướng từ subdomain sang domain chính
**TXT record**: Lưu thông tin xác thực như SPF, DKIM, bảo mật email và chống giả mạo
- Phân giải ngược (từ IP về tên miền tương ứng )
![image](https://hackmd.io/_uploads/rJzrb2WOGl.png)

# VII. Giao thức ARP

- ARP (Address Resolution Protocol ) xác định MAC tương ứng với một địa chỉ IP trong mạng LAN
![image](https://hackmd.io/_uploads/SJlL-nZ_zg.png)
- Hoạt động liên kết trong mô hình OSI, đóng vai trò thiết yếu trong quá trình truyền dữ liệu nội bộ mạng, nhất là trong mạng Ethernet
- Việc sử dụng ARP giúp tối ưu hóa việc truyền thông tin trong mạng, đảm bảo dữ liệu được gửi đến đúng thiết bị thông qua việc ánh xạ địa chỉ IP sang địa chỉ MAC phù hợp

# VIII. Mô hình OSI
	
- OSI là khung tham chiếu tiêu chuẩn, chia thành 7 tầng riêng biệt để chuẩn hóa và đơn giản hóa việc giao tiếp giữa các hệ thống mạng		
![image](https://hackmd.io/_uploads/S1zDZhZdMx.png)
- Tầng 7 : Tầng ứng dụng (Application Layer) : Tầng mà web, ứng dụng tương tác trực tiếp với người dùng		
- Tầng 6 : Tầng trình bày (Presentation Layer) : Đảm bảo giữ liệu được định dạng đúng, mã hóa, giải mã, nén và giải nén					
- Tầng 5 : Tầng phiên (Session Layer) : Thiết lập phiên, duy trì phiên, đồng bộ hóa và kết thúc phiên
- Tầng 4: Tầng vận chuyển (Transport Layer) : Phân đoạn và tái lắp ráp các segment, đánh địa chỉ cổng, kiểm soát kết nối, kiểm soát luồng, kiểm soát lỗi		 
- Tầng 3: Tầng mạng (Network Layer) : Định địa chỉ logic, định tuyến, phân mảnh và tái lắp ráp gói tin ( Nếu gói tin quá to thì mới cần phân mảnh  )		
- Tầng 2: Tầng liên kết dữ liệu (Data Link Layer) : Đóng khung, địa chỉ vật lý, kiểm soát luồng, kiểm soát lỗi, Kiểm soát truy cập đường truyền			
- Tầng 1 : Tầng vật lý (Physical Layer) : Đặc tính môi trường, biểu diễn bit, tốc độ dữ liệu, đồng bộ hóa bit, 
- Dữ liệu được truyền lần lượt từ tầng cao nhất xuống tầng thấp nhất

# IX. Mô hình TCP/IP

- TCP/IP là nền tảng giao thức giúp kết nối và truyền dữ liệu trên mạng Internet, gồm 4 tầng 		
![image](https://hackmd.io/_uploads/B1EubhWOfg.png)
- Tầng 4 – Tầng ứng dụng (Application) : Đây là tầng mà HTTP, HTTPS, FTP, SMP, v.v kết nối tới người dùng		
- Tầng 3 – Tầng giao vận (Transport) : Chịu trách nhiệm truyền tải dữ liệu, phổ biến là TCP và UDP		
- Tầng 2 – Tầng mạng (Internet)	: Định tuyến, gắn địa chỉ đồng thời tìm đường đi tối ưu		
- Tầng 1 – Tầng vật lý (Physical) : Chịu trách nhiệm truyền dữ liệu giữa các thiết bị trong cùng một mạng			
# X. So sánh mô hình OSI và TCP/IP

- OSI và TCP/IP khác nhau lớn về số tầng		
- TCP/IP gộp tầng 7, 6, 5 của OSI lại thành tầng 4		
- TCP/IP gộp tầng 2, 1 của OSI lại thành tầng 1		
- OSI giống như mô hình lý thuyết, còn TCP/IP là thực tế
- OSI giúp ta hiểu sâu hơn về mạng, đồng thời việc tách riêng từng tầng giúp dễ dàng kiểm tra nếu có lỗi


