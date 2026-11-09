---
title: Fake
tags: ["HuTechCTF"]

---

Tải bài tập tại [đây](https://brotherctf.com/practice/fake)

Sử dụng `zsteg` và `png check`

![image](/images/816fa6bd20300d748a79b03a.png)

Có thể thấy pngcheck báo sau `IEND` còn data, zsteg chỉ ra rõ data đằng sau là gì

![image](/images/70949f783d1bc3957162e0c3.png)

Ta mở bằng HxD, thấy đằng sau là cấu trúc một file png
Ta thay từ đoạn `Rar! --> IHDR` bằng `PNG --> IHDR như đoạn đầu`

![image](/images/71c5d309dd51dfe55e33c49a.png)

![image](/images/055d65bb650524b624083140.png)

Ta kiểm tra bằng lại bằng `binwalk` và lấy ra bằng `foremost`

![image](/images/78730f8d8fe4cb5c8ccba58e.png)

![image](/images/24a26a017cd0f187dfb0e5bb.png)

Flag là : `HUTECH_CTF{D3n_R0i_A_T01_D01_H01_L4u}`