---
title: Exiftool
tags: ["Tools"]
---

# I. Bản chất

-Trong mỗi bức ảnh, ngoài ảnh mình nhìn thấy đằng sau đó còn tồn tại các dữ liệu không thể đọc bằng mắt thường 
-Để đọc được những dữ liệu ấy, chúng ta cần dùng đến công cụ exiftool  	
-Exiftool cho phép ta đọc, ghi và chỉnh sửa Metadata <các thông tin liên quan như ngày tạo, ngày sửa, tên tác giả, tốc độ màn chập >  	
-Exiftool được hỗ trợ trên nhiều dạng file, nhưng thường đầy đủ nhất vẫn là file ảnh  	
	
# II. Tiến hành cài đặt exiftool trên Ubuntu
 
- `sudo apt install libimage-exiftool-perl`

# III. Các lệnh cơ bản của exiftool 

- `exiftool` + <file ảnh > : đọc metadata của <file ảnh 

![image (1)](https://hackmd.io/_uploads/Skeb-RWOzx.png)

- `exiftool -a -u` + <file ảnh > : đọc metadata bao gồm thẻ ẩn và thẻ không chuẩn 
- `exiftool -Artist=` + "Ten Tac Gia " + <file ảnh > : Chỉnh sửa tên tác giả
- `exiftool -all=` + <file ảnh > : Xóa toàn bộ metadata

