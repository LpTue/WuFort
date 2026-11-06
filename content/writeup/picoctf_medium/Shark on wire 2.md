---
title: Shark on wire 2
tags: ["PicoCTF_Medium"]
---

Tải bài tập tại [đây](https://learn.cylabacademy.org/library/84?page=4&category=4&difficulty=2&workspace=true)
Đầu tiên lọc bằng data

![image](https://hackmd.io/_uploads/B1MzoJ25Mg.png)

Thấy nhận tại cổng 22 khá bất thường
Bởi cổng 22 thường của ssh
Thêm nữa tại cổng số 22 ta tìm thấy đoạn 'start' và 'end'

![image](https://hackmd.io/_uploads/H1i_ik3cfg.png)

![image](https://hackmd.io/_uploads/S1mYiy2cfe.png)

Lọc theo `udp.dstport == 22`

Ta thấy được gửi từ cổng bắt đầu bằng số 5 theo sau 3 số
Nhìn khá giống số thập phân (byte )

![image](https://hackmd.io/_uploads/B1hEn1hqGx.png)

Flag là : academy{p1LLf3r3d_data_v1a_st3g0}

