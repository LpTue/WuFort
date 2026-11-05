---
title: Step
tags: ["Knowledge"]
---

# I. Giới thiệu
- Đây là writeup tổng hợp lại các phương pháp phân tích từng dạng bài

# II. Phân tích ảnh
- `file` : kiểm tra xem file đúng định dạng không
- `strings` : kiểm tra đoạn cần tìm trong văn bản
- `exiftool` : kiểm tra metadata của ảnh
- `binwalk` : kiểm tra xem có file ẩn được giấu không
- `foremost` : trích xuất file bị giấu
- `zsteg` : kiểm tra các kênh màu của ảnh
- `hex` : sử dụng các công cụ như `Ghex` để kiểm tra và chỉnh sửa mã hex
- `steghide` : trích xuất file ẩn bằng `steghide` nhưng phải có pass
- [Stegall](https://picoctfsolutions.com/tools/stegall)
- `speic`

# III. Phân tích âm thanh :
- `sonic visualiser` : sử dụng để tách từng lớp layer kiểm tra
- Nếu âm thanh là mã morse thì công cụ tại [đây](https://morsecode.world/international/decoder/audio-decoder-adaptive.html)
- Từ âm thanh quét qua ảnh `SSTV` : tải tại [đây](https://bucknova.github.io/Open-SSTV/#install)

# IV. Phân tích văn bản Microsoft 
- `oletools` : Đọc source code 
- `dcodedmp` : Đọc P-Code

# V. Phân tích lưu lượng mạng
- `wireshark` : lọc và kiểm tra lưu lượng

# VI. Phân tích disk
- Sử dụng `autopsy` và `ftk-image`

# VII. Phân tích memory
- Sử dụng `Volality`

# VIII. Crack Pass
- `hash-identifier` : xác định kiểu mã băm
- `hash-cat` và `john` : tấn công

## Các web hỗ trợ giải mã
- CyberChef : truy cập tại [đây](https://gchq.github.io/CyberChef/)
- Dcode : liên quan tới ROT, truy cập tại [đây](https://www.dcode.fr/caesar-cipher)

## Tải các công cụ
- [Eric-Zic_tools](https://drive.google.com/file/d/18QKoXCKoDywiHlsbiaCJzGIVpRiH8rkl/view?usp=sharing)

## Tool thêm
`stegsnow` 
