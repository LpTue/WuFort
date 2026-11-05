---
title: Rogue Tower
tags: ["PicoCTF_Medium"]
---

Tải bài tập tại [đây](https://learn.cylabacademy.org/library/714?page=1&category=4&difficulty=2&workspace=true)

Ta trích xuất file qua protocol html
Ta được đoạn code `U1ZXUlxbTEpABVFDCmlWAl5ZaUIJQQZDbVFSUl0DVwJQSA==`

![image](https://hackmd.io/_uploads/S1bR9chhzg.png)

Ta để ý `key` --> thuật toán mã hóa 
Từ IMSI của nạn nhân

![image](https://hackmd.io/_uploads/BylSjc3hze.png)

Ta thấy IMSI cuối xuất hiện trước khi có post file là `310410725669651`

![image](https://hackmd.io/_uploads/S1vqs93hGl.png)

Tạm giải thích ngta lấy 8 số cuối là vì đó là 5 số đầu là mã chung

![image](https://hackmd.io/_uploads/SytJ25hhGl.png)

![image](https://hackmd.io/_uploads/HJXEhc33Mg.png)

Flag là : `academy{r0gu3_c3ll_t0w3r_dddd5b3b}`