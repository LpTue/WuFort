---
title: Milkslap
tags: ["PicoCTF_Medium"]
---

Tải bài tập tại [đây](https://learn.cylabacademy.org/library/139?page=3&category=4&difficulty=2&workspace=true)

Mở web cha vào check source

![image](https://hackmd.io/_uploads/S1Zrgya2ze.png)

Ta tải về bằng cách mở tab mới lưu ảnh hoặc dùng `wget`

![image](https://hackmd.io/_uploads/HyBKe1a3zg.png)

Check bằng exiftool ta thấy dòng RGB --> nghĩ tới zsteg
`export RUBY_THREAD_VM_STACK_SIZE=500000000` : tăng ruby's stack size limit

![image](https://hackmd.io/_uploads/SJpnxkahMx.png)

Flag là : `academy{imag3_m4n1pul4t10n_sl4p5}`