---
title: Shark on wire 2
tags: ["PicoCTF_Medium"]
---

Tải bài tập tại [đây](https://learn.cylabacademy.org/library/84?page=4&category=4&difficulty=2&workspace=true)
Đầu tiên lọc bằng data

![image](https://lptue.github.io/WuFort/images/84401dc36ce9a263ba0f0a2e8811fd0d.png)

Thấy nhận tại cổng 22 khá bất thường
Bởi cổng 22 thường của ssh
Thêm nữa tại cổng số 22 ta tìm thấy đoạn 'start' và 'end'

![image](https://lptue.github.io/WuFort/images/6ff2cddcabf581f20fa6d719ab456825.png)

![image](https://lptue.github.io/WuFort/images/ece2fa2146c51bd82983b265a4fd2c4c.png)

Lọc theo `udp.dstport == 22`

Ta thấy được gửi từ cổng bắt đầu bằng số 5 theo sau 3 số
Nhìn khá giống số thập phân (byte )

![image](https://lptue.github.io/WuFort/images/80c8060c72cd3348a0f292aaa19c689b.png)

Flag là : academy{p1LLf3r3d_data_v1a_st3g0}

