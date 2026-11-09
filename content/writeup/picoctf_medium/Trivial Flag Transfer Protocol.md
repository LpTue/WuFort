---
title: Trivial Flag Transfer Protocol
tags: ["PicoCTF_Medium"]
---

Tải bài tập tại [đây](https://learn.cylabacademy.org/library/103?page=4&category=4&difficulty=2&workspace=true)
Đầu tiên phân tích thấy nhiều protocol TFTP

![image](/images/46cc555c7b1c26afab641b382c3e5dee.png)

Ta trích xuất ra

![image](/images/b370a38e4641c8824ec671c0bf671155.png)

Ta đọc file plan

![image](/images/6fbe15939d87a99c7385b5d2c741b4d8.png)

![image](/images/97b8dea31ebb84716b412699096c1248.png)

Nội dung : I USED THE PROGRAMANDHIDIT WITH-DUEDILIGENCE .CHECKOUT THE PHOTOS
Ta steghide với từng file

![image](/images/6787aff039816b9d2345125a023ab192.png)

![image](/images/01b29a1a95f5f98b700704c67f954ba7.png)

Flag là : academy{h1dd3n_1n_pLa1n_51GHT_18375919}
