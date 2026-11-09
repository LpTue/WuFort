---
title: Secret of the Polyglot
tags: ["PicoCTF_Easy"]
---

Đầu tiên mở file nên          
![image](https://lptue.github.io/WuFort/images/4386c27bde1f59281b694b31ed4245d5.png)


Có thể thấy file dường như đang thiếu đoạn đầu		
Hãy thử kiểm tra bằng strings ``` strings flag2of2-final.pdf  | grep pico ```    
Thấy ko có đoạn mã nào nên ta thử đọc với HxD      
![image](https://lptue.github.io/WuFort/images/f258ca41280275ede8df5c691c3135c2.png)


Thấy file có đoạn đầu là png nên ta đổi file thành đuôi .png      
![image](https://lptue.github.io/WuFort/images/08dcb2d749161896eebeb3da9af392b9.png)



