---
title: Fake
tags: ["HuTechCTF"]

---

Tải bài tập tại [đây](https://brotherctf.com/practice/fake)

Sử dụng `zsteg` và `png check`

![image](https://hackmd.io/_uploads/H1Gfbgk0Ml.png)

Có thể thấy pngcheck báo sau `IEND` còn data, zsteg chỉ ra rõ data đằng sau là gì

![image](https://hackmd.io/_uploads/H1VAZxkAzg.png)

Ta mở bằng HxD, thấy đằng sau là cấu trúc một file png
Ta thay từ đoạn `Rar! --> IHDR` bằng `PNG --> IHDR như đoạn đầu`

![image](https://hackmd.io/_uploads/SJu7Mly0Me.png)

![image](https://hackmd.io/_uploads/rJvbNgkRfe.png)

Ta kiểm tra bằng lại bằng `binwalk` và lấy ra bằng `foremost`

![image](https://hackmd.io/_uploads/S1mvEeJAGl.png)

![image](https://hackmd.io/_uploads/Byi_NxJRzx.png)

Flag là : `HUTECH_CTF{D3n_R0i_A_T01_D01_H01_L4u}`