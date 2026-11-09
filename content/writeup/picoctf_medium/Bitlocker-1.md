---
title: Bitlocker-1
tags: ["PicoCTF_Medium"]
---

Tải bài tập tại [đây](https://learn.cylabacademy.org/library/453?page=1&category=4&difficulty=2&workspace=true&bookmarked=true)

Đầu tiên ta cần lấy được mã băm của file bitlock
`bitlocker2john bitlocker-1.dd`

![image](/images/1041ab8058df0cc43bea4dba90a759b6.png)

Lúc này ta sẽ thấy được 4 mã băm bitlock khác nhau
4 mã băm này sẽ đều dẫn tới 1 pass 
Ta test với mã bitlock0 trước
Lưu mã lại 1 file tên `hash.txt`

![image](/images/0e3588a9e122459ff76405b7b81b68d3.png)

Ta sử dụng phương pháp tấn công từ điển 
`john --format=bitlocker --wordlist=rockyou.txt hash.txt`

![image](/images/76215b8badfb670cbf51a9f4f635587d.png)

Ta được pass là : `jacqueline`
Ta import file bitlock vào autospy 

![image](/images/80831a61c1167a06a60ac552b9d7e597.png)

![image](/images/2ee84156d76ef6ff5aebeeab692dc4db.png)

Flag là : `academy{us3_b3tt3r_p4ssw0rd5_pl5!_3242adb1}`
