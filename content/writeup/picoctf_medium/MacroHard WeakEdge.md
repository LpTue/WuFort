---
title: MacroHard WeakEdge
tags: ["PicoCTF_Medium"]
---

Tải bài tập tại [đây](https://learn.cylabacademy.org/library/130?page=4&category=4&difficulty=2&workspace=true)
Chuyển đổi thành file zip và giải nén

![image](/images/746ce5e30b0abae15075fb3ec981ec6f.png)

Ta tìm thấy file đáng ngờ

![image](/images/c10b38f7a5a535180df9c2d0d87f1cb0.png)

Ta viết lệnh đơn giản để xóa khoảng cách

```py=
fi = open("hidden","r")
chuoi = fi.readline().split()

a = ""
for i in chuoi:
    a += str(i)

print(a)
```
Ta đem giải mã

![image](/images/63f824738ebb1ee648b098ca649e686c.png)

Flag là : academy{D1d_u_kn0w_ppts_r_z1p5}
