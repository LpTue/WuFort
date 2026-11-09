---
title: Win
tags: ["Knowledge"]
---

# I . Win_1

## Misson 1 
- Pro khác Home ở **mã hóa bitlock**    
Tham khảo tại [đây](https://www.microsoft.com/en-us/windows/compare-windows-11-home-vs-pro-versions#tabs1-2https://)

## Misson 2.1 : Để tắt hộp tìm kiếm         
- Click chuột phải vào thanh taskbar, chọn search, chọn hidden

## Misson 2.2 : Để ẩn/ tắt thanh tác vụ 
- Click chuột phải vào thanh taskbar, chọn Show Task View button

## Misson 2.3 : Ngoài đồng hồ và mạng nào, còn Action Center
- Nó là cái nút như nút tin nhắn cuối cùng

## Misson 3 : Khái niệm NTFS (New Technology File System )
- NTFS được biết đến như một **hệ thống tập tin nhật ký**
- Khi xảy ra sự cố, NTFS có thể **tự khắc phục** bằng thông tin lưu trong tệp nhật ký
- Giải quyết được hạn chế 
> Hỗ trợ tệp lớn hơn 4GB
Thiết lập quyền cụ thể cho thư mục và tệp
Nén thư mục và tệp
Mã hóa (Hệ thống tệp mã hóa hoặc EFS )        

- Tính năng khác là **Luồng thay thế** (ADS )
>Mỗi tệp đều có ít nhất một luồng giữ liệu, ADS cho lưu trữ nhiều hơn một luồng dữ liệu
Về mặt bảo mật, các nhà viết phần mền độc hại dùng ADS để ẩn dữ liệu

- Mở rộng về các File System :
> FAT : Là dạng tệp tin kiểu cũ, là dạng tệp tin 8-bit, do vậy số lượng cụm tăng khi ổ đĩa tăng dẫn tới sự ra đời của FAT12 - 12bit, FAT16 - 16bit, FAT32 - 32bit

- Cấu trúc FAT : 
![image](/images/ac73a48d0f8f2e7bd631f12e2c802404.png)

- Điểm khác biệt giữa FAT, FAT12, FAT16, FAT32 : 
![image](/images/d1229b2c9fb25d931b6df09ec1dccd5a.png)
	
- Điểm khac nhau so với NTFS :
![image](/images/715e96f28cc67fa15b2b05deccd17eec.png)

- Mở rộng về ExFAT 
>Giống FAT32 nhưng loại bỏ được hạn chế về giới hạn 4Gb
"Có thể " vì do tính bảo mật và dễ dàng khôi phục nên NTFS được thay thế thay cho FAT 

## Misson 4 : Biến môi trường ( %windir% )
- Biến môi trường **lưu trữ thông tin** về hệ điều hành, gồm :
>Đường dẫn hệ điều hành
Số lượng bộ xử lý được hệ điều hành sử dụng
Vị trí các thư mục tạm thời

- Mở rộng : 
>Thư mục Window () lưu trữ hệ điều hành, ko nhất thiết phải nằm ổ C
System32 lưu trữ các tệp quan trọng với hệ điều hành	

## Misson 5 : Người dùng tên tryhackmebilly
- Mở window + r (hoặc chuột phải vào biểu tượng window và chọn run )
- Gõ `lusrmgr.msc`
- Tất cả những đáp án cần đều ở trong đây
![image](/images/7ecb5bfda2d69f2d30737e0acd9088a2.png)

## Misson 6 : Khái niệm UAC (User Account Control )
- **Quyền cấp cao tăng nguy cơ xâm nhập** vì giúp phần mền đọc hại dễ lây hệ thống hơn
- Vì vậy UAC sẽ hiển thị để **xác nhận** xem họ có chạy thao tác đó không
- Khi chuột phải vào phần mền, chọn **Properties**, chọn mục **Security** sẽ xem được quyền của từng người dùng
![image](/images/7a7b96da6356943c4e8e6f2e419ea7f6.png)

## Misson 7 : Ngoài cài đặt còn Control Panel
- Để mở : gõ `Control Panel` vào thanh tìm kiếm
- Cung cấp nhiều lựa chọn tùy chỉnh
![image](/images/8153b6e329ac466b582842574d6fbb81.png)

## Misson 8 : Task manager
- Quản lý các tiến trình đang chạy
- Có thể bật bằng tổ hợp phím Ctrl + Shift + ESC
![image](/images/d7def95ae5a006c1a5d2b29ac39fdcd2.png)

# II . Win_2

## Misson 1.1 : Tìm hiểu về System Configuaration
- Cách mở : Gõ `MSConfig` vào thanh tìm kiếm
- Các tab phía trên gồm 
>Tổng quan <General > :Các lựa chọn khi khởi động Win
Boot : Các tùy chọn khi khởi động hệ điều hành
Dịch vụ <Services > : Cho biết trạng thái chạy hay dừng của các dịch vụ
Khởi động <Startup > : Gồm các cấu hình hệ thống KHÔNG phải quản lý chương trình như Task Manager
Công cụ <Tools > : Danh sách các tiện ích của hệ điều hành

![image](/images/125fef0cc93093d07f429fd2f8945299.png)

## Misson 1.2 : Tìm hiểu về Advanced System Settings
- Kiểm soát hành vi hiệu suất và phục hồi hệ thống
- Win sử dụng tệp làm RAM ảo khi RAM thật đầy, chỉnh chi tiết tại **Advanced** > mục **Performance** >**Settings**
- Có thể xem và chỉnh sửa cài đặt file crash dump tại tab **Advanced** > mục **Startup and Recovery** > **Settings**
![image](/images/01f5570a9cf82b2a64dc28145b0ded15.png)

## Misson 2 : Thay đổi cài đặt UAC
- Nhắc lại : UAC tạm hiểu là **thông báo** khi kích hoạt chức năng nâng cao
- Để mở, gõ `UAC` vào thanh tìm kiếm
![image](/images/c9dfce5c2ffac834ad5df6872e62af6d.png)

## Misson 3 : Tìm hiểu về Computer Management
- Để mở : Gõ `compmgmt` vào thanh tìm kiếm
- Trong mục **System Tools** gồm 
>Task Scheduler : Tạo và quản lý các tác vụ phổ biến
Event Viewer : Xem các sự kiện đã xảy ra trên máy tính
Shared Folders : Nơi xem đầy đủ các thư mục được chia sẻ
Performance : Xem dữ liệu hiệu suất theo thời gian thực từ tệp nhật ký
Device Manager : Xem và cấu hình phần cứng

- Mở rộng về Task Scheduler : 
![image](/images/40bba5d3f205ef64f1c9de2f25597e7c.png)

			
> Bức ảnh cho ta thấy tác vụ chạy một lệnh powershell vào mỗi 10h hàng ngày		
Kẻ tấn công có thể tạo tác vụ với phương thức xác thực Batch Logon (dùng mật khẩu), thay vì Interactive Token --Nhận được quyền cao nhất
Để khai thác, kẻ tấn công cần có mật khẩu của tài khoản mục tiêu, có thể thu được qua các phương pháp như bẻ khóa hash NTLMv2 hoặc khai thác lỗ hổng khác như CVE-2023-21726.​
Link bài viết tại [đây](https://www.facebook.com/groups/GroupWhiteHat/posts/4001955763465921/)

![image](/images/bfdef46dbe1f1efb0129d6e5b34eb427.png)


- Mở rộng về Event Viewer 
> Khung bên trái cung cấp danh sách phân cấp nhật ký sự kiện
hung ở giữa hiển thị tổng quan và tóm tắt về sự kiện cụ thể
Khung bên phải là khung hành động

- Các loại sự kiện ghi lại 
![image](/images/c84537e4ffa7dc324bb55f3261cfc6f1.png)

- Các nhật ký tiêu chuẩn 
![image](/images/212fef746fe7903be5f2c0d3af5b17c4.png)

- Trong mục Storage có Disk Management : Cho phép quản lý ổ đĩa
- Trong mục Services and Applications gồm 
> Services : Xem tất cả dịch vụ và trạng thái của chúng
WMI Control

## Misson 4 : Tìm hiểu về System Information
- Để mở : Gõ `msinfo32` vào phần tìm kiếm
- Gồm các mục 
> Hardware Resources : Tìm hiểu tại trang của Microsoft
Compone : Thông tin về các thiết bị phần cứng được cài đặt trên máy tính
Software Environment : Thông tin về phần mền được tích hợp trong hệ điều hành và phần mềm đã cài đặt

- Mở rộng : Nhớ lại về **Biến môi trường** <Environment Variables > 
> Lưu trữ thông tin về môi trường hệ điều hành
Biến môi trường lưu trữ giữ liệu được sử dụng bởi hệ điều hành và các chương trình khác

![MT](/images/463ad2b1a57e3b14f452e7d469bcd41c.png)
			
- Một phương pháp khác xem biến môi trường là OR
- Gõ Advanced system settings vào thanh tìm kiếm, sau đó chọn  Environment Variables <nút ở dưới >
    
![OR](/images/56bf7d7e5854a7ea24530555ef86b48d.png)
		
## Misson 5 : Tìm hiểu về Resource Monitor
- Để mở : Gõ `resmon` vào thanh tìm kiếm
- Hiển thị từng quy trình và tổng hợp GPU, bộ nhớ, thông tin sử dụng đĩa mạng
- Cung cấp chi tiết về các tiến trình từng sử dụng handle và module riêng lẻ
- Lọc cho phép tách riêng dữ liệu liên quan tới một hoặc nhiều tiến trình (ứng dụng và dịch vụ )
- Bao gồm tính năng phân tích quy trình, giúp xác định các tiến trình bị khóa, xung đột
- Trong tab gồm 
> CPU
Memory
Disk
Network
    
![RM](/images/182dfd16344ae7e99df102fabcb31350.png)

## Misson 6 : Tìm hiểu về CMD
- Để mở : Gõ `CMD` vào thanh tìm kiếm
- Các lệnh cmd đơn giản
>`hostname` : Tên máy tính
`whoami` : Tên người dùng đăng nhập
`ipconfig` : Hiển thị các thiết lập mạng cho máy tính
`ipconfig /?` : Hướng dẫn trợ giúp cho ipconfig <Phổ biến hay dùng /? >
`cls` : Xóa màn hình
`netstat` : Hiển thị thống kê giao thức và các kết nối mạng TCP/IP hiện tại
`net` : Quản lý tài nguyên mạng
`net help` : Hiển thị trợ giúp cho net <Đặc biệt với net >
					
## Mission 8 : Tìm hiểu về Registry Editor
- Để mở : Gõ `Registry Editor` vào thanh tìm kiếm
- Registry là cơ sở dữ liệu lưu trữ thông tin cần để cấu hình hệ thống cho người dùng, ứng dụng, thiết bị phần cứng
- Registry chứa thông tin mà Win liên tục tham chiếu như 
> Hồ sơ cho từng người dùng
Các ứng dụng được cài đặt trên máy tính
Các loại tài liệu mà mỗi ứng dụng có thể tạo
Cài đặt bảng thuộc tính cho thư mục và biểu tượng ứng dụng
Phần cứng tồn tại trên hệ thống
Các cổng đang được sử dụng

# III . Win_3

## Misson 1 : Windows Update 
- Cập nhật thường xuyên nhằm vá các lỗi nằm tăng tường bảo mật
- Gõ `Windows Update Setting` vào thanh tìm kiếm để xem chi tiết
    
![image](/images/d468ecea07f8a90fa7029d30e6a0824d.png)

## Misson 2 : Windows Security
- Là cài đặt quản lý các cài đặt về bảo mật
- Để mở : gõ Windows Security vào thanh tìm kiếm
- Gồm có 
> Virus & threat protection : Theo dõi nguy cơ về mã độc 
Firewall & network protection : Theo dõi nguy cơ về tường lửa và mạng
App & browser control 
Device security 

- Các màu tương ứng 
> Xanh : Tương đối an toàn
Vàng : Khuyến nghị cần xem xét
Đỏ : Cảnh báo về các mối nguy hại

![image](/images/b796f9f6b462064a21bed11523068a10.png)

## Misson 3 : Tìm hiểu sâu về Virus & threat protection 
- Các lựa chọn gồm : Scan, settings, update, ransomware protections (bảo vệ khỏi phần mền tống tiền )
- Các lựa chọn quét 
> Quét nhanh : Kiểm tra các thư mục nơi mà các mối nguy thường được tìm thấy
Quét toàn bộ : Kiểm tra toàn bộ thư mục và chương trình

- Nhìn mục Virus & threat protection settings > Manage settings
    
![image](/images/e2ae37f1c6a4ef3385eef83ac42b0058.png)

- Trong Manage Settings gồm
> Real-time protection : Phát hiện ngay lập tức 
Cloud-delivered protection : Bảo vệ tăng cường khi cho phép truy cập dữ liệu đám mây
Automatic sample submission : Gửi tệp mẫu đến Microsoft để giúp bạn và người khách tránh mối nguy
Controlled folder access : Bảo vệ thư mục, tệp tin khỏi các thay đổi trái phép
Exclusions : Không quét thư mục mà bạn loại trừ
Notifications : Thông báo cho bạn
		
## Misson 4 : Tìm hiểu sâu về Firewall & network protection 
- Các cài đặt lớn gồm 
> Domain network <miền mạng > : Mạng mà hệ thống máy chủ có thể xác thực với bộ điều khiển miền
Private network <mạng cá nhân > : Người dùng tự thiết lập, là mạng riêng tư hoặc gia đình
Public network <mạng công cộng > : Hồ sơ công khai, sử dụng mạng công cộng

- Định nghĩa : Lưu lượng truy cập vào và ra thiết bị thông qua cổng, và tường lửa quản lý những gì đi qua cổng đó
- Chỉnh sửa chi tiết tại nút Allow an app throught firewall

![image](/images/f8baebaaa298f5d775c73434d4246d24.png)

## Misson 5 : Tìm hiểu sâu về App & browser control
- Chức năng : Chống lại các web lừa đảo, chứa phần mền độc hại cũng như tải các phần mền độc hại
- Tìm hiểu chi tiết tại Google <quá lười để dịch từng chưng năng > 

## Misson 6 : Tìm hiểu sâu về Device Security
- Microsoft khuyến nghị không nên thay đổi 
- Giới thiệu về Trusted Platform Module (TMP ) <Tạm dịch là module đáng tin cậy >
- Được thiết kế để cung cấp chứng năng liên quan tới phần cứng
- Chip TMP được thiết kế để xử lý các hoạt động mã hóa 
- Chip gồm nhiều cơ chế chống can thiệp trái phép, phần mền độc hại không thể can thiệp chức năng bảo mật của TMP

## Misson 8 : Giới thiệu về Bitlock 
- Tính năng tích hợp với hệ điều hành ngăn chặn việc đánh cắp hoặc lộ dữ liệu
- Trên các máy cài đặt TMP, Bitlock hoạt động tốt nhất
		
## Misson 9 : Volume Shadow Copy Service (VSS )
- Tạm hiểu là hành động tạo 1 bản sao Shadow <ảnh chụp nhanh tại thời điểm cụ thể > của dữ liệu cần sao lưu
- Các bản sao VSS được lưu trên ổ đĩa được bật tính năng bảo vệ
- Nếu VSS được bật, ta có thể
> Tạo điểm khôi phục
Thực hiện khôi phục hệ thống
Cài đặt cấu hình khôi phục 
Xóa điểm khôi phục

