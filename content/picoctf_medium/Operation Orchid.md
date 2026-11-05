---
title: Operation Orchid
tags: ["PicoCTF_Medium"]
---

Tải bài tập tại [đây](https://learn.cylabacademy.org/library/285?page=3&category=4&difficulty=2&workspace=true)
Tìm kiếm file đáng ngờ

![image](https://hackmd.io/_uploads/HJTIQr_qMe.png)

Đọc vào history

![image](https://hackmd.io/_uploads/S19OmBu5Mg.png)

Ta thấy có lệnh mã hóa
`openssl aes256 -salt -in flag.txt -out flag.txt.enc -k unbreakablepassword1234567`
Thì ta extract file đã được mã hóa và
`openssl aes256 -d -salt -in flag.txt.enc -out flag.txt -k unbreakablepassword1234567`

![image](https://hackmd.io/_uploads/B1Uh7SOcGl.png)

Flag là : academy{h4un71ng_p457_718ebd29}