---
title: Wireshark2
tags: ["PicoCTF_Medium"]
---

Tải bài tập tại [đây](https://learn.cylabacademy.org/library/110?page=1&category=4&difficulty=2&workspace=true&solved=true)

Khi mở ta thấy nhiều cờ giả --> bỏ qua
Khi lọc theo dns

![image](/images/2118c3cd531548dd6227792b263ab097.png)

Ta thấy hầu như gửi tới 8.8.8.8
Có cái Ip 18.217.1.57 lạc loài

![image](/images/fc0b9d51e33adcb40d4306d283ea13bb.png)

Ta lọc ip đến và dns
Thấy được đoạn encode giống base64 ở phần info

![image](/images/7591591b736f8031be50e9ecf916650e.png)

Flag là : `academy{dns_3xf1l_ftw_deadbeef}`