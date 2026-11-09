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

![image](/images/1833dfe4df0ba6a3b46839c8f1a60d51.png)

![image](/images/af439320a917604ae8e41e7898dcae23.png)

![image](/images/50dbc659849b7ee14521f78d553248f7.png)

## Với Autopsy
- Tạo case mới

![image](/images/13dc7c58031fb42c4bd44ee8f6c75149.png)

- Thêm disk vào

![image](/images/63a59462f431fcb8be79811ad656a5e4.png)

# IV. Một số tệp đáng lưu ý
- $MFT : Lưu trữ thông tin về tất cả các tệp và thư mục trên một ổ đĩa, bao gồm tên, quyền truy cập và thuộc tính của chúng
- $MFTMirr : Đóng vai trò sao lưu $MFT, rất quan trọng trong trường hợp $MFT gốc bị hỏng
- $LogFile : Tệp này ghi lại thông tin nhật ký giao dịch của siêu dữ liệu (khu vực MFT)
- Dùng `MFTECmd` để phân tích

