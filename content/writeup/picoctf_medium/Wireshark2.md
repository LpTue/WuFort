---
title: Wireshark2
tags: ["PicoCTF_Medium"]
---

Tải bài tập tại [đây](https://learn.cylabacademy.org/library/110?page=1&category=4&difficulty=2&workspace=true&solved=true)

Khi mở ta thấy nhiều cờ giả --> bỏ qua
Khi lọc theo dns

![image](https://hackmd.io/_uploads/SJfqh9a3fg.png)

Ta thấy hầu như gửi tới 8.8.8.8
Có cái Ip 18.217.1.57 lạc loài

![image](https://hackmd.io/_uploads/SJGancanMe.png)

Ta lọc ip đến và dns
Thấy được đoạn encode giống base64 ở phần info

![image](https://hackmd.io/_uploads/S1jkpcanzg.png)

Flag là : `academy{dns_3xf1l_ftw_deadbeef}`