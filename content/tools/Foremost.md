---
title: Foremost
tags: ["Tools"]
---

# I. Giới thiệu về foremost

- Foremost là chương trình phục hồi dữ liệu dựa trên tiêu đề, chân trang và cấu trúc dữ liệu
- Foremost làm trên các tệp hình ảnh, chẳng hạn như tệp tạo bởi dd, Safeback, Encase, v.v hoặc trực tiếp trên ổ đĩa
- Các tiêu đề, chân trang có thể được chỉnh vởi tệp cấu hình hoặc sử dụng dòng lệnh
- Nhìn vào cấu trúc dữ liệu của một định dạng tệp nhất định cho phép phục hồi đáng tin cậy và nhanh hơn

# II. Cài đặt

- `sudo apt install foremost`

# III. Các lệnh cơ bản

- `foremost -help`
    >V: Hiển thị thông tin bản quyền và thoát.
	-t: Chỉ định loại file cần khôi phục (Ví dụ: -t jpeg,pdf...).
	-d: Bật tính năng phát hiện khối gián tiếp (dành cho hệ thống tập tin UNIX).
	-i: Chỉ định file đầu vào (mặc định là nhận từ stdin).
	-a: Ghi lại tất cả các header tìm thấy, bỏ qua kiểm tra lỗi (dùng cho các file bị hỏng).
	-w: Chỉ ghi file nhật ký (audit file), không trích xuất các file tìm thấy ra đĩa cứng.
	-o: Thiết lập thư mục xuất kết quả (mặc định là thư mục output).
	-c: Chỉ định file cấu hình sẽ sử dụng (mặc định là foremost.conf).
	-q: Bật chế độ quét nhanh (Quick mode). Chỉ tìm kiếm tại các mốc ranh giới khối 512 byte.
	-Q: Bật chế độ yên lặng (Quiet mode). Ẩn bớt các thông báo hiển thị ra màn hình.
	-v: Chế độ chi tiết (Verbose mode). Hiển thị toàn bộ thông báo nhật ký lên màn hình.

# IV. Ví dụ 
	
Thử áp dụng foremost vào phục phồi ảnh ở 1 ổ đĩa
- `sudo fdisk -l` : quét phân vùng máy tính
- `sudo foremost -v -q -t  png -i  /dev/sbd` : Hiển thị thông báo trên màn hình, quét nhanh, chỉ phục hồi png, đầu vào là /dev/sbd 	
![image](https://hackmd.io/_uploads/Syy1E0bdGl.png)

	
