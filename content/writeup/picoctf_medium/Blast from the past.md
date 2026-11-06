---
title: Blast from the past
tags: ["PicoCTF_Medium"]
---

Tải bài tập tại [đây](https://learn.cylabacademy.org/library/432?page=1&category=4&difficulty=2&workspace=true&solved=true)

Đọc miêu tả

![image](https://hackmd.io/_uploads/Sk8i5Cp2zl.png)

Ta thấy đề cập tới thời gian và exiftool

![image](https://hackmd.io/_uploads/Bye7j0phMg.png)

Ta đổi tên file cho phù hợp với bên host

![image](https://hackmd.io/_uploads/ryqKo0a3Ml.png)

Ta chỉnh lại từng tag cho tới khi nào đúng

![image](https://hackmd.io/_uploads/BkFdhR6hzl.png)

Với SamSung: TimeStamp nó dùng hệ riêng nên ta phải dùng HxD, tham khảo tại [đây](https://stackoverflow.com/questions/78185037/how-to-edit-the-samsung-trailer-tag-timestamp)

![image](https://hackmd.io/_uploads/ryH7TCThMx.png)

Với `1700513181420` là mili giây sau `1/1/1970`
Nên ta đổi về `0000000000001`, lúc này ta có thể chỉnh bằng exiftool được rồi

![image](https://hackmd.io/_uploads/Skhh6Canzx.png)

Thời gian tự động đổi về `1970:01:01 00:00:00.001`

![image](https://hackmd.io/_uploads/ByVg0CT2Ge.png)

Flag là : `academy{71m3_7r4v311ng_p1c7ur3_046dc81d}`