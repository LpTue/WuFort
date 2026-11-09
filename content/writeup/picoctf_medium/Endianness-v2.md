---
title: Endianness-v2
tags: ["PicoCTF_Medium"]
---

Tải bài tại [đây](https://learn.cylabacademy.org/library/415?page=2&category=4&difficulty=2&workspace=true)

Mở bằng HxD

![image](/images/c38460047e509138af76a335746ce7fa.png)

Ta thấy file dường như đang bị đảo 
Ta chuyển về hex --> swap (đảo Big-Endian & Little-Endian) --> chuyển về dữ liệu thô --> render ra ảnh

![image](/images/60dbceaa7cbe8a9e66891bc214d30243.png)

Flag là : `academy{cert!f1Ed_iNd!4n_s0rrY_3nDian_5b37ea4e}`


