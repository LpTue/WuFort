---
title: Flag in Flame
tags: ["PicoCTF_Easy"]
---

Đầu tiên hãy thử phân tích file  
Thấy đây là file thuần ASCII
Thử ``` strings logs.txt | grep pico ```  
Thấy ko ra kết quả nên đổi cách  

Khúc này, nếu bạn khôn sẽ thấy "=" ở cuối --> có thể đây là dạng text của base64  
Do file quá lớn nên CyberChef ko thể hỗ trợ  
Dùng lệnh ``` base --decode logs.txt > da ```  
Lúc này bạn nhận được file base64  
![image](https://lptue.github.io/WuFort/images/c8a92e22be058b578fd05307efcfb336.png)

Khi mở file thấy đề PNG --> khả năng đây là file ảnh --> cho nên cyberchef để giải  
![download (1)](https://lptue.github.io/WuFort/images/59c3c0fffed527493c89f79d65cf7c76.png)

Nhận thấy file ảnh có dòng chữ nổi bật, hãy coppy chúng và đem lên cyberchef để giải   
![image](https://lptue.github.io/WuFort/images/bde018dc18ae9d72b06321ad0a038cc7.png)


