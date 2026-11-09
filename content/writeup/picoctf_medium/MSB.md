---
title: ' MSB'
tags: ["PicoCTF_Medium"]
---

Tải bài tập tại [đây](https://learn.cylabacademy.org/library/359?page=2&category=4&difficulty=2&workspace=true)
Bài này cần sử dụng tới công cụ phân tích MSB Steganography
Tải tool tại [đây](https://github.com/Pulho/sigBits)
Chạy lệnh `python3 sigBits.py -i Ninja-and-Prince-Genji-Ukiyoe-Utagawa-Kunisada.flag.png -t MSB -out flag.txt`

![image](/images/fcdd545a184c167e78993ad0e9b66f40.png)

Ta có thể thấy chuỗi ký tự dài
Ta có thể dùng tìm kiếm của HxD để tìm flag

![image](/images/f43665899749b6372dfb0a3df0b97729.png)

Flag là : academy{15_y0ur_que57_qu1x071c_0r_h3r01c_80119e7f}
