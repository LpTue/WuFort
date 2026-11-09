---
title: Operation Orchid
tags: ["PicoCTF_Medium"]
---

Tải bài tập tại [đây](https://learn.cylabacademy.org/library/285?page=3&category=4&difficulty=2&workspace=true)
Tìm kiếm file đáng ngờ

![image](/images/c12b6ec2e939bbab31c1622cacf4cd57.png)

Đọc vào history

![image](/images/20c7037ef7b4e1980c627d9e051cab0a.png)

Ta thấy có lệnh mã hóa
`openssl aes256 -salt -in flag.txt -out flag.txt.enc -k unbreakablepassword1234567`
Thì ta extract file đã được mã hóa và
`openssl aes256 -d -salt -in flag.txt.enc -out flag.txt -k unbreakablepassword1234567`

![image](/images/419c905ec5520dccc2fa9aa550003504.png)

Flag là : academy{h4un71ng_p457_718ebd29}