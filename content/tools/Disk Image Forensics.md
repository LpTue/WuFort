---
title: Disk Image Forensics
tags: ["Tools"]
---

# I. Giới thiệu về các thuật ngữ cơ bản
- Disk Image : bản sao từng bit toàn bộ ổ đĩa, phân vùng, giữ chính xác cấu trúc và nội dung
- Disk Imaging : quá trình tạo bản sao của ổ đĩa, các hàm băm được sử dụng để đối chiếu tính nguyên vẹn 
- Disk Image Forensics : là quá trình phân tích
# II. Giới thiệu các công cụ
- [Autopsy](https://www.autopsy.com/) : Công cụ phân tích nhiều tính năng
- [FTK Image](https://www.exterro.com/ftk-downloads/ftk-imager-8-3) : Công cụ phân tích có phần nhẹ hơn

# III. Các bước sử dụng
## Với FTK Image
- Nhập ảnh đĩa vào

![image](https://hackmd.io/_uploads/rkqjpM0tze.png)

![image](https://hackmd.io/_uploads/HJnTTGRKGg.png)

![image](https://hackmd.io/_uploads/SyzJ0MRYMl.png)

## Với Autopsy
- Tạo case mới

![image](https://hackmd.io/_uploads/H1u-AM0tMl.png)

- Thêm disk vào

![image](https://hackmd.io/_uploads/Bkv_CGAKfg.png)

# IV. Một số tệp đáng lưu ý
- $MFT : Lưu trữ thông tin về tất cả các tệp và thư mục trên một ổ đĩa, bao gồm tên, quyền truy cập và thuộc tính của chúng
- $MFTMirr : Đóng vai trò sao lưu $MFT, rất quan trọng trong trường hợp $MFT gốc bị hỏng
- $LogFile : Tệp này ghi lại thông tin nhật ký giao dịch của siêu dữ liệu (khu vực MFT)
- Dùng `MFTECmd` để phân tích

