---
title: Endianness-v2
tags: ["PicoCTF_Medium"]
---

Tải bài tại [đây](https://learn.cylabacademy.org/library/415?page=2&category=4&difficulty=2&workspace=true)

Mở bằng HxD

![image](https://hackmd.io/_uploads/Hk0UgF2hzg.png)

Ta thấy file dường như đang bị đảo 
Ta chuyển về hex --> swap (đảo Big-Endian & Little-Endian) --> chuyển về dữ liệu thô --> render ra ảnh

![image](https://hackmd.io/_uploads/Hyi_gtnhGx.png)

Flag là : `academy{cert!f1Ed_iNd!4n_s0rrY_3nDian_5b37ea4e}`


