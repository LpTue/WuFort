---
title: AUTH
tags: ["MiniCTF"]

---

![image](https://lptue.github.io/WuFort/images/44c81a133f36df073fe90167908ea5ad.png)

Ta tập trung vào tài khoản `student` 

![image](https://lptue.github.io/WuFort/images/4f6fafde687e3d96e0a7f83e4f4d633c.png)

Để ý thấy có format `host sudo: ` 
Nên ta dùng grep theo format đó

![image](https://lptue.github.io/WuFort/images/2f750235060315eccbe675c89f843813.png)

Ta thấy đoạn mã đáng ngờ bị mã hóa theo base64

![image](https://lptue.github.io/WuFort/images/7d741b8f7ca4fce9e28fc4941b75f96e.png)



