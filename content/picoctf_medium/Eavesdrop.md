---
title: Eavesdrop
tags: ["PicoCTF_Medium"]
---

Tải bài tập tại [đây](https://learn.cylabacademy.org/library/264?page=3&category=4&difficulty=2&workspace=true)
Mở bằng pcap ta đọc lén được đoạn văn bản

![image](https://hackmd.io/_uploads/HJWy8BU5Mg.png)

Ta thu thập được
- Lệnh : `openssl des3 -d -salt -md md5 -in file.des3 -out file.txt -k supersecretpassword123`
- Và có tệp tin nào đó được gửi qua cổng 9002

![image](https://hackmd.io/_uploads/ryd4ISL5zx.png)

Ta coppy mã hex để dựng lại file.des3
Và chạy lệnh

![image](https://hackmd.io/_uploads/rkn9IHI5zl.png)

Flag là : academy{nc_73115_411_02612719}
