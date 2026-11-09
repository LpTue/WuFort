---
title: Blast from the past
tags: ["PicoCTF_Medium"]
---

Tải bài tập tại [đây](https://learn.cylabacademy.org/library/432?page=1&category=4&difficulty=2&workspace=true&solved=true)

Đọc miêu tả

![image](https://lptue.github.io/WuFort/images/bc8db68f60a3d7953ac4dfc971c788d1.png)

Ta thấy đề cập tới thời gian và exiftool

![image](https://lptue.github.io/WuFort/images/b46f7fc0cd0e55d9a32ddff142670075.png)

Ta đổi tên file cho phù hợp với bên host

![image](https://lptue.github.io/WuFort/images/30b9025534468faf773d81cf5807eb9a.png)

Ta chỉnh lại từng tag cho tới khi nào đúng

![image](https://lptue.github.io/WuFort/images/0dc32acc969e4837c6064e7e7b7c02f4.png)

Với SamSung: TimeStamp nó dùng hệ riêng nên ta phải dùng HxD, tham khảo tại [đây](https://stackoverflow.com/questions/78185037/how-to-edit-the-samsung-trailer-tag-timestamp)

![image](https://lptue.github.io/WuFort/images/c73b9efa199c8aaae23f92a7e3115deb.png)

Với `1700513181420` là mili giây sau `1/1/1970`
Nên ta đổi về `0000000000001`, lúc này ta có thể chỉnh bằng exiftool được rồi

![image](https://lptue.github.io/WuFort/images/d2045ba4dfaead8ea8c6ed3536b8e0a8.png)

Thời gian tự động đổi về `1970:01:01 00:00:00.001`

![image](https://lptue.github.io/WuFort/images/a06aeb0dc80b01029ae4fc260e6ca2ee.png)

Flag là : `academy{71m3_7r4v311ng_p1c7ur3_046dc81d}`