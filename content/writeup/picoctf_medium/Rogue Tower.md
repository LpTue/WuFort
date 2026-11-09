---
title: Rogue Tower
tags: ["PicoCTF_Medium"]
---

Tải bài tập tại [đây](https://learn.cylabacademy.org/library/714?page=1&category=4&difficulty=2&workspace=true)

Ta trích xuất file qua protocol html
Ta được đoạn code `U1ZXUlxbTEpABVFDCmlWAl5ZaUIJQQZDbVFSUl0DVwJQSA==`

![image](https://lptue.github.io/WuFort/images/383b77c243bca378ff48add8ab79a783.png)

Ta để ý `key` --> thuật toán mã hóa 
Từ IMSI của nạn nhân

![image](https://lptue.github.io/WuFort/images/4eb214d744fa51205953e13988107e8e.png)

Ta thấy IMSI cuối xuất hiện trước khi có post file là `310410725669651`

![image](https://lptue.github.io/WuFort/images/67b8155585ec9f2f746b17569ef16046.png)

Tạm giải thích ngta lấy 8 số cuối là vì đó là 5 số đầu là mã chung

![image](https://lptue.github.io/WuFort/images/736bb4c4fd34b5f283e9c31735d62ae6.png)

![image](https://lptue.github.io/WuFort/images/8e1759092cc61edd2f6a8758e9713e07.png)

Flag là : `academy{r0gu3_c3ll_t0w3r_dddd5b3b}`