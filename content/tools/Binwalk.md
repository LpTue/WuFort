---
title: Binwalk
tags: ["Tools"]
---

# I. Bản chất của Binwalk
	
- Binwalk được viết bằng ruby --> làm tăng đáng kể tốc độ so với Python
- Cả thuật toán nén và mã hóa đều tìm cách loại bỏ dữ liệu lặp, vì vậy dữ liệu bị nén rất ngẫu nhiên
- Phân tích entropy giúp xác định các phần của tệp có thể bị nén hoặc mã hóa!
- Binwalk chỉtốt khi tệp nén nằm trong danh sách "Các chữ ký đã biết "
Chi tiết tại [đây](https://github.com/ReFirmLabs/binwalk/wiki/Supported-Signatureshttps://)
- Có thể tạm hiểu Binwalk dựa vào phân tích entropy để tách riêng các tệp tin ra 
- Dựa bảng entropy
    > Trục X : Độ lệch của tệp
	Trục Y : Đo từ sự không ngẫu nhiên tới ngẫu nhiên (khá khó hiểu )

![image](https://hackmd.io/_uploads/Skn20abOGe.png)

# II. Cài đặt Binwalk 
	
`sudo apt install binwalk`
# III. Các lệnh cơ bản Binwalk
	
- `binwalk` + <file > : Scan một tệp tin
- `binwalk --dd=.*` + <file > : Trích xuất tấp cả tệp tin 
    
![image (2)](https://hackmd.io/_uploads/HJXKJAbdGl.png)
    
# IV. Mở rộng 
	
- Nếu extract bằng --dd=.* sẽ xuất hiện rất nhiều file
- Để lấy ra file cần chỉ: 	`dd if= <file_vao > of= <file_ra > bs=1 skip=decimal`
	> Ví dụ : dd if=PurpleThing.jpeg of=flag.png bs=1 skip=153493
- Hiểu 
    > dd : sao chép dữ liệu <sau tới sleulkit sẽ dùng >
	if = <file_vao > : Tệp tin đầu vào		
	of = <file_ra> : Tệp tin đầu ra
	bs = Mặc định là 512 block size
	skip = Số lượng byte bỏ qua với mỗi bs <block size >
		
    Vì vậy, nếu để bs = 512 thì skip = 153493 / 512 = 299.76 <khá lẻ >

![image (4)](https://hackmd.io/_uploads/S1LseRbuze.png)






