---
title: Behind the mountain
tags: ["BKSec"]

---

Tải bài tập tại [đây](https://training.bksec.vn/challenges/171)
Các câu hỏi

```=
Cuộc tấn công bắt đầu từ khoảng thời gian nào? (Format: HourAM/PM;dd-mm-yy Timezone GMT+7. Ví dụ: 18pm;01-01-2024 GMT+7)

Kẻ tấn công (được cho là) có nguồn gốc từ quốc gia nào, và hắn đang thực hiện tấn công ở thành phố nào? Format: City/Country (all lowercase, bỏ tất cả dấu cách)
 
Kẻ tấn công đang sử dụng công cụ gì để che giấu hành vi trên Internet?
 
Server đang mở những cổng nào? (Format: viết các cổng từ nhỏ đến lớn, ngăn cách bằng dấu phẩy, chỉ tính các cổng từ 1-10000)
 
Webserver đang được serve tại cổng nào?
 
Sau khi thực hiện quét cổng, kẻ tấn công đã tiến hành quét tự động bằng một công cụ, User-Agent của công cụ này là gì?
 
Tên của dịch vụ đang chạy ở Webserver là gì? Dịch vụ này có 1 CVE được biết đến rộng rãi, bạn có thể nêu tên được không? (Format: ServiceName_CVE. Ví dụ: Atlassian Confluence_CVE-2023-22527)
 ```
 
# Câu 1

![image](https://lptue.github.io/WuFort/images/c9ae2e8f8dc15b2d7862dd35b80c3b0d.png)

Ta tìm thấy được tgian

![image](https://lptue.github.io/WuFort/images/007399595f44ea074d600d5991a812cf.png)

Đổi về giờ VN là `11am;30-03-2024 GMT+7`
 
# Câu 2

![image](https://lptue.github.io/WuFort/images/3a13b7598641d913eb51ea0d49e41b61.png)

![image](https://lptue.github.io/WuFort/images/0d1b6ecd839bba395b85c59a8efb4ab1.png)

Ta thấy lượng truy packet nhiều bất thường 
> Ip attacker : 45.134.190.42
> Ip Victim : 157.230.41.56

![image](https://lptue.github.io/WuFort/images/4d1e668670a64a956cd8becdc6735d72.png)

Ta dùng công cụ check vị trí theo ip 
Câu trả lời là `bandarseribegawan/brunei`

# Câu 3

![image](https://lptue.github.io/WuFort/images/d3aaecdb72330c46d470a5a7db2eaca1.png)

Ta thấy có ip attacker thì ta lần được bên cung cấp VPN

Câu trả lời là `NordVPN`

# Câu 4
Ta hiểu, khi đang mở cổng tức là có SYN và ACK
Ta lọc theo SYN và ACK với ip victim
`ip.src == 157.230.41.56 and tcp.flags.syn==1 and tcp.flags.ack==1`

![image](https://lptue.github.io/WuFort/images/13b6c2ec2b7f77937a5e71c2b051ef95.png)

Ta đọc thủ công từng cổng và sắp xếp lại
Câu trả lời là `22,135,139,445,5040,5357,7680,8001,8090`

# Câu 5
Vẫn tận dụng cái lọc cũ

![image](https://lptue.github.io/WuFort/images/71b4f6bf3144f79c919aaf382fdfac46.png)

Ta thấy tại cổng 8090 có đề cập tới server
Câu trả lời là `8090`

# Câu 6
Đề yêu cầu tìm User-Agent
`http.user_agent and ip.src == 45.134.190.42 and ip.dst == 157.230.41.56`

![image](https://lptue.github.io/WuFort/images/a2afbb0240b39fa084033cb962ecc1c3.png)

Ta để ý lúc khúc sau User-Agent là feroxbuster/2.10.1
Câu trả lời là `feroxbuster/2.10.1`

# Câu 7
Nhắc lại câu 5 ta trả lời webserver ở port 8090
Ta lọc theo port 8090 và http
`http or tcp.port == 8090`

![image](https://lptue.github.io/WuFort/images/48f9eb12c4aa56d89ebe8117483641fa.png)

![image](https://lptue.github.io/WuFort/images/9e81a949af5f87665ccdcf3e9d421729.png)

![image](https://lptue.github.io/WuFort/images/3434e0e296bcfb88d1a107075c4405d1.png)


Hầu như chỉ có DNN mới dùng cấu trúc thư mục `/DesktopModules/` như vậy

Ta tìm được tên đầu là `DotNetNuke`
Ta check CVE nổi tiếng của nó

Câu trả lời là `DotNetNuke_CVE-2017-9822`

![image](https://lptue.github.io/WuFort/images/b04d0c105a103c98dee9f4275e71d6b8.png)

