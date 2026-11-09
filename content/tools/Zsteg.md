---
title: Zsteg
tags: ["Tools"]
---

# I. Giới thiệu qua về Zsteg

- Zsteg là công cụ phát hiện dữ liệu ẩn của stegano trong PNG & BMP
- Ngoài ra còn có thể phát hiện : 
    > OpenStego
	Camouflage 1.2.1
	LSB with The Eratosthenes set
	LSB steganography trong PNG & BMP
	zlib-compressed data
- Tạm hiểu là người giấu và người giải mã tuân theo một quy luật nào đó để chỉnh sửa các bit trong bảng màu
	( Chưa hiểu rõ lắm, nếu được cần a giải thích chi tiết tại sao ạ )

# II. Các cài đặt Zsteg
	
- Bước 1 : Cài đặt thư viện RubyGems  : `sudo apt install rubygems`
- Bước 2 : Cài đặt zsteg : `gem install zsteg`

# III. Các câu lệnh cơ bản

- `zsteg -a` + <tên file > : Thử tất cả các phương pháp đã biết
- `zsteg -E` + <tên kênh > + <tên file > : Trích xuất kênh 

![image (6)](/images/e894f48aaa946577a39ff6a5bd28cfac.png)




