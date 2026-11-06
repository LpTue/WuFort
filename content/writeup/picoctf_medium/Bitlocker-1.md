---
title: Bitlocker-1
tags: ["PicoCTF_Medium"]
---

Tải bài tập tại [đây](https://learn.cylabacademy.org/library/453?page=1&category=4&difficulty=2&workspace=true&bookmarked=true)

Đầu tiên ta cần lấy được mã băm của file bitlock
`bitlocker2john bitlocker-1.dd`

![image](https://hackmd.io/_uploads/BJFq0V03Ml.png)

Lúc này ta sẽ thấy được 4 mã băm bitlock khác nhau
4 mã băm này sẽ đều dẫn tới 1 pass 
Ta test với mã bitlock0 trước
Lưu mã lại 1 file tên `hash.txt`

![image](https://hackmd.io/_uploads/r1QL1B02Ge.png)

Ta sử dụng phương pháp tấn công từ điển 
`john --format=bitlocker --wordlist=rockyou.txt hash.txt`

![image](https://hackmd.io/_uploads/r11ukH02zl.png)

Ta được pass là : `jacqueline`
Ta import file bitlock vào autospy 

![image](https://hackmd.io/_uploads/H1unyHA3Me.png)

![image](https://hackmd.io/_uploads/H1RakH02Ge.png)

Flag là : `academy{us3_b3tt3r_p4ssw0rd5_pl5!_3242adb1}`
