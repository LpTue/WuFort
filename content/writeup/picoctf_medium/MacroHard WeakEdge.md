---
title: MacroHard WeakEdge
tags: ["PicoCTF_Medium"]
---

Tải bài tập tại [đây](https://learn.cylabacademy.org/library/130?page=4&category=4&difficulty=2&workspace=true)
Chuyển đổi thành file zip và giải nén

![image](https://hackmd.io/_uploads/HyeljHuqGx.png)

Ta tìm thấy file đáng ngờ

![image](https://hackmd.io/_uploads/ryiZjS_9zl.png)

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

![image](https://hackmd.io/_uploads/ryd4jSO9Ml.png)

Flag là : academy{D1d_u_kn0w_ppts_r_z1p5}
