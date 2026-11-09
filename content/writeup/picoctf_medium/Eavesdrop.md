---
title: Eavesdrop
tags: ["PicoCTF_Medium"]
---

Tải bài tập tại [đây](https://learn.cylabacademy.org/library/264?page=3&category=4&difficulty=2&workspace=true)
Mở bằng pcap ta đọc lén được đoạn văn bản

![image](/images/7f8e64462ef2d882ad14f3e2bbca7b25.png)

Ta thu thập được
- Lệnh : `openssl des3 -d -salt -md md5 -in file.des3 -out file.txt -k supersecretpassword123`
- Và có tệp tin nào đó được gửi qua cổng 9002

![image](/images/8b972d6c3ea967f953915508a84f4991.png)

Ta coppy mã hex để dựng lại file.des3
Và chạy lệnh

![image](/images/6c2094eb8c01663566480015d0a62737.png)

Flag là : academy{nc_73115_411_02612719}
