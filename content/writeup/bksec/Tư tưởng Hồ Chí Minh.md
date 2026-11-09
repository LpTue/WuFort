---
title: Tư tưởng Hồ Chí Minh
tags: ["BKSec"]

---

Tải bài tập tại [đây](https://training.bksec.vn/challenges/35)

Ta sử dụng binwalk để kiểm tra file ẩn tại ko thể lấy được nội dung bị bôi đen

![image](https://hackmd.io/_uploads/Byis2DAoMx.png)

Ta thấy có file ảnh nên ta lấy ra `dd if=TTHCM.pdf of=anh.jpg bs=266037 skip=1`

![image](https://hackmd.io/_uploads/BJva2wRiGx.png)

Flag là : BKSEC{hav3_s0me_commun1sm_my_c0mrade}