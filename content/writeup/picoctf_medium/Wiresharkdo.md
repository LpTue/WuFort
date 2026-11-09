---
title: Wiresharkdo
tags: ["PicoCTF_Medium"]
---

Tải bài tập tại [đây](https://learn.cylabacademy.org/library/115?page=4&category=4&difficulty=2&workspace=true)
Đọc file thấy có nhiều protocol HTTP POST 
Ta nghĩ ngay tới lấy file thông qua HTTP

![image](https://lptue.github.io/WuFort/images/a9170b5061a0879e9343203633399e3e.png)

Ta được đoạn như này

![image](https://lptue.github.io/WuFort/images/48ca264da105dfa1e094a20ed2e85fdf.png)

Mở bằng VScode thấy có thể đây là mã hóa rot

![image](https://lptue.github.io/WuFort/images/94252cc078d5f8d8d6456031e435e5ab.png)

Flag là : academy{p33kab00_1_s33_u_deadbeef}