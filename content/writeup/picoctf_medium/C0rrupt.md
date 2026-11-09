---
title: C0rrupt
tags: ["PicoCTF_Medium"]
---

Tải bài tập tại [đây](https://learn.cylabacademy.org/library/53?page=5&category=4&difficulty=2&workspace=true)

Mở bằng hxd kéo xuống dưới

![image](https://lptue.github.io/WuFort/images/69dff9efe260f7e6b3f47cad23f9fe92.png)

Đây là dấu hiệu của file png
Ta sửa lại 8bit đầu về đúng signature number

![image](https://lptue.github.io/WuFort/images/a5a206143a116c3c0d48f667d105fc35.png)

![image](https://lptue.github.io/WuFort/images/5e9dc3868c8412a7b3e42335ef82691d.png)

Ta tìm hiểu thấy chỗ đúng của C"DR phải thay bằng IHDR

![image](https://lptue.github.io/WuFort/images/a68ca7120f0d7c30e8e5398dc879bed2.png)

Ta tiếp tục thấy sai lúc này ở chunk pHYs chứa hình ảnh --> liên tưởng tới IDAT

![image](https://lptue.github.io/WuFort/images/0fa1b062e5b2366e83f4026f660667a6.png)

Ta khoanh vùng vì đoạn này khá giống IDAT nhưng bị đổi

![image](https://lptue.github.io/WuFort/images/6f6ec0a8982005c5e0d9648473d096f6.png)

![image](https://lptue.github.io/WuFort/images/296b742275fba6bbadc7b2fe9dc7f75b.png)
 Flag là : `academy{c0rrupt10n_1847995}`