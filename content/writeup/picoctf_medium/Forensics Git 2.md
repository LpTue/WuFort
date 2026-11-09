---
title: Forensics Git 2
tags: ["PicoCTF_Medium"]
---

Tải bài tập tại [đây](https://learn.cylabacademy.org/library/707?page=1&category=4&workspace=true&difficulty=2)

Ta trích xuất file chứa git

![image](https://lptue.github.io/WuFort/images/1e46c81581fa7fac59b13c470d3db56d.png)

Khi đọc log thì nó báo chưa có cái commit nào trước đó

![image](https://lptue.github.io/WuFort/images/a6edb76a0af7aa1758e623626f2e63d5.png)

Nhưng khi đọc bằng autospy thì ta thấy có mấy cái git

![image](https://lptue.github.io/WuFort/images/d9b3968cdfef034bba55b12db2b11047.png)

Flag là : `academy{g17_r35cu3_16ac6bf3}`

