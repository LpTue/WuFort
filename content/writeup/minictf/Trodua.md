---
title: Trodua
tags: ["MiniCTF"]

---

Đọc mô tả, ta thấy nó chạy mỗi khi mở máy --> có thể được lưu trong start up
Tìm theo đường dẫn `Trodua\[root]\Users\Administrator\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup****`

![image](https://hackmd.io/_uploads/rJjAJQe5fl.png)

![image](https://hackmd.io/_uploads/S1nlx7x5Mg.png)

Ta giải mã xor ra

![image](https://hackmd.io/_uploads/BJSNgQxqzg.png)

![image](https://hackmd.io/_uploads/BkxSeXxcMl.png)

Ra được khúc sau là `N1ce_7rY`
Ta lần theo đường dẫn `Trodua\[root]\Users\Administrator\AppData\Roaming\Microsoft\Windows\Recent`

![image](https://hackmd.io/_uploads/rJzwgQxqze.png)

Thấy nửa đầu là `MY_SUP3R_S3CR3T_D4T4`

Vậy flag là: KCSC{MY_SUP3R_S3CR3T_D4T4_N1ce_7rY}