---
title: Tư tưởng Hồ Chí Minh
tags: ["BKSec"]

---

Tải bài tập tại [đây](https://training.bksec.vn/challenges/35)

Ta sử dụng binwalk để kiểm tra file ẩn tại ko thể lấy được nội dung bị bôi đen

![image](/images/788999c186552731f6010d46445e0cde.png)

Ta thấy có file ảnh nên ta lấy ra `dd if=TTHCM.pdf of=anh.jpg bs=266037 skip=1`

![image](/images/c947d34b39d634022a12ca734cdd65d8.png)

Flag là : BKSEC{hav3_s0me_commun1sm_my_c0mrade}