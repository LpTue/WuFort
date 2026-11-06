---
title: C0rrupt
tags: ["PicoCTF_Medium"]
---

Tải bài tập tại [đây](https://learn.cylabacademy.org/library/53?page=5&category=4&difficulty=2&workspace=true)

Mở bằng hxd kéo xuống dưới

![image](https://hackmd.io/_uploads/rkLzorhnMx.png)

Đây là dấu hiệu của file png
Ta sửa lại 8bit đầu về đúng signature number

![image](https://hackmd.io/_uploads/r1Yuir2nze.png)

![image](https://hackmd.io/_uploads/BkRjoS2hfg.png)

Ta tìm hiểu thấy chỗ đúng của C"DR phải thay bằng IHDR

![image](https://hackmd.io/_uploads/rJDWnH2hGg.png)

Ta tiếp tục thấy sai lúc này ở chunk pHYs chứa hình ảnh --> liên tưởng tới IDAT

![image](https://hackmd.io/_uploads/HyLShS33fg.png)

Ta khoanh vùng vì đoạn này khá giống IDAT nhưng bị đổi

![image](https://hackmd.io/_uploads/S1Nv2Bhhfe.png)

![image](https://hackmd.io/_uploads/S11u3H22Gl.png)
 Flag là : `academy{c0rrupt10n_1847995}`