---
title: Milkslap
tags: ["PicoCTF_Medium"]
---

Tải bài tập tại [đây](https://learn.cylabacademy.org/library/139?page=3&category=4&difficulty=2&workspace=true)

Mở web cha vào check source

![image](https://lptue.github.io/WuFort/images/23d15f69f58056427dd935928d8436ee.png)

Ta tải về bằng cách mở tab mới lưu ảnh hoặc dùng `wget`

![image](https://lptue.github.io/WuFort/images/0cba6c3af4507a16ea06ed0fe6e1f037.png)

Check bằng exiftool ta thấy dòng RGB --> nghĩ tới zsteg
`export RUBY_THREAD_VM_STACK_SIZE=500000000` : tăng ruby's stack size limit

![image](https://lptue.github.io/WuFort/images/f431601e1602b287a3dd08833ad41d12.png)

Flag là : `academy{imag3_m4n1pul4t10n_sl4p5}`