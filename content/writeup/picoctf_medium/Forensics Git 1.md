---
title: Forensics Git 1
tags: ["PicoCTF_Medium"]
---

Tải bài tại [đây](https://learn.cylabacademy.org/library/706?page=1&category=4&workspace=true&difficulty=2)

![image](/images/19dba5bc8a43e5eab2dbbab8af88392b.png)

Mở bằng autospy và trích xuất file ra
Di chuyển tới file .git
Dựa vào gợi ý dẫn ta tới cách khôi phục

![image](/images/059faeaee6c4fee7ef90456d41a43d68.png)

Vậy trước hết ta cần lấy được mã gì đó

![image](/images/ce9ad57ea09b43b407ef52fe36623daa.png)

Chạy lệnh git để coi toàn bộ lệnh
Ta đọc log

![image](/images/19744387d799e331f19ae4b0e137dd64.png)

Ta chạy checkout

![image](/images/b373f3d52eebc5ff08ffce4a96d42b09.png)

Flag là : `academy{g17_r3m3mb3r5_d4ddf904}`







