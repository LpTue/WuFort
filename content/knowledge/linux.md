---
title: Linux
tags: ["Knowledge"]
---

# I : Các lệnh cơ bản 

- `whoami` : Quyền hiện tại của người dùng trong session terminal đang dùng 
- `echo` : In nội dung ra
- `ls` : Liệt kê các thư mục và tệp tin 
- `cd` : Trỏ tới thư mục 
- `pwd` : Cho biết vị trí hiện tại
- `find` : Cho biết trong thư mục có những gì
- `grep` : Tìm kiếm nội dung trong file 
    > Ví du : `cat test1 | grep hello`
- `&` : Thực hiện lệnh song song
	> Ví dụ : `echo luongphutue & echo forensic`
- ``&&`` : Thực hiện lệnh lần lượt
	> Ví dụ : `echo luongphutue && echo forensic` 
- `>` : Ghi đè
	> Ví dụ : `echo hello > test1`
- ``>>`` : Thêm vào cuối 
	> echo `hi >> test1`
	Khi : `cat test1`
	Kết quả:
    ```
    hello 
    hi
    ```
- `ssh` : Kết nối máy chủ từ xa
	> Ví dụ : `ssh -p 2220 bandit0@bandit.labs.overthewire.org`
- `apt` : Cho phép truy cập kho phần mền cộng đồng
	> Ví dụ : `sudo apt install firefox` : Cho phép tải firefox từ kho phần mền
	
# II . Các lệnh quản lý folder và file 

- `ls -a` : Hiển thị những thư mục và tệp tin ẩn 
- `ls -l` : Hiển thị quyền hạn với thư mục và tệp tin
	>drwx------ 
	d : Thư mục 
    rwx : Người sở hữu được quyền **đọc, viết và thực thi**
	Nhóm người sở hữu không được quyền làm gì 
	Những người khác không được quyền làm gì 
	>rwxrwxrwx 
	r : Tệp tin 
    Người sở hữu được toàn quyền
	Người sở hữu được toàn quyền
	Những người khác được toàn quyền 
- `ls -help` : Hiển thị các đuôi mở rộng
- `man` : Giống help những hiển thị lần lượt
	> Ví dụ : man ls
- `touch` : Tạo một tệp tin trống
- `mkdir` : Tạo một thư mục trống
- `rm` : Xóa tệp tin
- `rm -r` : Xóa thư mục
- `cp` : Coppy tệp tin 
- `cp -r` : Coppy thư mục
- `mv` : Di chuyển tệp tin 
- `mv -r` : Di chuyển thư mục
- `file` : Cho biết kiểu tệp tin
- `nano` : Chỉnh sửa văn bản của tệp tin
- `wget` : Tải tệp xuống từ web thông qua http

# III : Mở rộng

- `sudo adduser` + <tên người dùng muốn tạo > : Tạo thêm người dùng mới
- `su` + <tên người dùng > : Chuyển sang người dùng 
	> Ví dụ : sudo adduser acc1
	Khi đó có thể : su acc1
	Kết quả hiển thị : acc1@LpTue:/home/lptue
- `scp` + <tên tệp tin > + < host + name@ip:đường dẫn > : Coppy tệp tin sang máy chủ ssh
	> Ví dụ : `scp imp.txt ubuntu@192.168.1.30:/home/ubuntu/transferred.txt`
- `scp` + < host + name@ip:đường dẫn > + <tên tệp tin > : Coppy tệp tin từ máy chủ ssh về máy mình
    > Ví dụ : `scp ubuntu@192.168.1.30:/home/ubuntu/document.txt notes.txt`
- `python3 -m http.server` : Mở host dưới dạng web
- `ps` : Cung cấp danh sách các chương trình ( Processess ) đang chạy
- `ps aux` : Cung cấp danh sách các chương trình do người dùng thực thi ( au : author , x : excte )
- `top` : Cung cấp danh sách các chương trình nhưng cập nhật mỗi 10s
- `kill` + <PID > : Đóng chương trình có PID tương ứng ( PID được lấy thông qua ps, ps aux , top )
- `systemctl` + <opt > + <service > : Chỉnh các dịch vụ ( opt : start, stop, enable, disable )
- `cron` : Lên lịch tự động (Chi tiết tại Google )

# IV : Mẹo cần biết
- Ctrl + C : Cho phép ta dừng lệnh đang chạy
    > Ví dụ 
    Đang chạy : `top`
	Khi ta : Ctrl + C
	Kết quả : Lệnh sẽ dừng lại
- Ctrl + Z : Cho phép ta ẩn lệnh đang chạy khỏi màn hình (Cho phép chạy ngầm )
	> Ví dụ
    Đang chạy : `top`
	Khi ta : Ctrl + Z
	Kết quả : Lệnh sẽ biến mất khỏi màn hình
	Khi ta muốn hiện lệnh trở lại : `fg`
- /etc : Lưu trữ tệp tin hệ thống
- /var : Lưu trữ tệp dữ liệu được truy cập hoặc ghi lại bởi các dịch vụ, ứng dụng chạy trên hệ thống
- /root : Thư mục chính của người dùng root
- /tmp : Thư mục tạm thời, lưu trữ dữ liệu chỉ truy cập 1 hoặc 2 lần, sẽ bị xóa khi khởi động lại máy

