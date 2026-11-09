---
title: Trodua
tags: ["MiniCTF"]

---

Đọc mô tả, ta thấy nó chạy mỗi khi mở máy --> có thể được lưu trong start up
Tìm theo đường dẫn `Trodua\[root]\Users\Administrator\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup****`

![image](https://lptue.github.io/WuFort/images/247a16095b25d58b6493548e842e96ef.png)

![image](https://lptue.github.io/WuFort/images/602f507118960dc4cfcc1dff8e84a9df.png)

Ta giải mã xor ra

![image](https://lptue.github.io/WuFort/images/dae5b06fb5c201be3c4e77ec7b3e3713.png)

![image](https://lptue.github.io/WuFort/images/ba0abf333ecb110714199f94fbb89e24.png)

Ra được khúc sau là `N1ce_7rY`
Ta lần theo đường dẫn `Trodua\[root]\Users\Administrator\AppData\Roaming\Microsoft\Windows\Recent`

![image](https://lptue.github.io/WuFort/images/ae6393cef5c658c6ab981915b120e0ea.png)

Thấy nửa đầu là `MY_SUP3R_S3CR3T_D4T4`

Vậy flag là: KCSC{MY_SUP3R_S3CR3T_D4T4_N1ce_7rY}