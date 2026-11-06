---
title: Trivial Flag Transfer Protocol
tags: ["PicoCTF_Medium"]
---

Tải bài tập tại [đây](https://learn.cylabacademy.org/library/103?page=4&category=4&difficulty=2&workspace=true)
Đầu tiên phân tích thấy nhiều protocol TFTP

![image](https://hackmd.io/_uploads/r1fJL2Uqfx.png)

Ta trích xuất ra

![image](https://hackmd.io/_uploads/r1pJ83L5Gx.png)

Ta đọc file plan

![image](https://hackmd.io/_uploads/Skip9nL5Ml.png)

![image](https://hackmd.io/_uploads/S1OR5nUcfe.png)

Nội dung : I USED THE PROGRAMANDHIDIT WITH-DUEDILIGENCE .CHECKOUT THE PHOTOS
Ta steghide với từng file

![image](https://hackmd.io/_uploads/SyaXih8cGl.png)

![image](https://hackmd.io/_uploads/r1YEohL9fg.png)

Flag là : academy{h1dd3n_1n_pLa1n_51GHT_18375919}
