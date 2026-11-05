---
title: Behind the mountain
tags: ["BKSec"]

---

Tải bài tập tại [đây]
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

![image](https://hackmd.io/_uploads/rkwkqEZnfl.png)

Ta tìm thấy được tgian

![image](https://hackmd.io/_uploads/ry1McE-hGx.png)

Đổi về giờ VN là `11am;30-03-2024 GMT+7`
 
# Câu 2

![image](https://hackmd.io/_uploads/ByTUq4W2Gx.png)

![image](https://hackmd.io/_uploads/BkSaqEb3fx.png)

Ta thấy lượng truy packet nhiều bất thường 
> Ip attacker : 45.134.190.42
> Ip Victim : 157.230.41.56

![image](https://hackmd.io/_uploads/r18XoVWnGg.png)

Ta dùng công cụ check vị trí theo ip 
Câu trả lời là `bandarseribegawan/brunei`

# Câu 3

![image](https://hackmd.io/_uploads/Sk3Ko4-hze.png)

Ta thấy có ip attacker thì ta lần được bên cung cấp VPN

Câu trả lời là `NordVPN`

# Câu 4
Ta hiểu, khi đang mở cổng tức là có SYN và ACK
Ta lọc theo SYN và ACK với ip victim
`ip.src == 157.230.41.56 and tcp.flags.syn==1 and tcp.flags.ack==1`

![image](https://hackmd.io/_uploads/SkrHh4bnGg.png)

Ta đọc thủ công từng cổng và sắp xếp lại
Câu trả lời là `22,135,139,445,5040,5357,7680,8001,8090`

# Câu 5
Vẫn tận dụng cái lọc cũ

![image](https://hackmd.io/_uploads/ByYcnE-nfx.png)

Ta thấy tại cổng 8090 có đề cập tới server
Câu trả lời là `8090`

# Câu 6
Đề yêu cầu tìm User-Agent
`http.user_agent and ip.src == 45.134.190.42 and ip.dst == 157.230.41.56`

![image](https://hackmd.io/_uploads/HkWE6NZhMg.png)

Ta để ý lúc khúc sau User-Agent là feroxbuster/2.10.1
Câu trả lời là `feroxbuster/2.10.1`

# Câu 7
Nhắc lại câu 5 ta trả lời webserver ở port 8090
Ta lọc theo port 8090 và http
`http or tcp.port == 8090`

![image](https://hackmd.io/_uploads/S1JsaVZnGl.png)

![image](https://hackmd.io/_uploads/r1Q1RNZ2fx.png)

![image](https://hackmd.io/_uploads/HybXAVZnGx.png)


Hầu như chỉ có DNN mới dùng cấu trúc thư mục `/DesktopModules/` như vậy

Ta tìm được tên đầu là `DotNetNuke`
Ta check CVE nổi tiếng của nó

Câu trả lời là `DotNetNuke_CVE-2017-9822`

![image](https://hackmd.io/_uploads/SyPBWHZnMe.png)

