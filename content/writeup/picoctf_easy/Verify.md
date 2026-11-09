---
title: Verify
tags: ["PicoCTF_Easy"]
---

Đầu tiên ta hãy kết nối tới server 
![image](https://lptue.github.io/WuFort/images/dce62540dd8982e015a35ff5bb5f1cec.png)

Ta hãy thử dịch các gợi ý của bài tập
![image](https://lptue.github.io/WuFort/images/bdde0f58d64915c09beedf935c2c565e.png)



Định hướng lúc này :			
	- Đầu tiên thử kiểm tra checksum và sha256 xem có trùng khớp ko			
	- Nếu tìm thấy file, ta sẽ tiếp tục kiểm tra file hoặc chạy lệnh giải mã			

![image](https://lptue.github.io/WuFort/images/daec7a4dd6f7bf481ac39c198c8c071d.png)


Khi chạy lệnh, có thể thấy có rất nhiều mã mà ta phải kiểm tra				
	--> Có thể dùng grep để lọc checksum mà ta cần				
![image](https://lptue.github.io/WuFort/images/d9a2c2333b01174d83701c87ac6531d5.png)


Lúc này khi đã tìm được file, ta tiến hành kiểm tra file có nội dung ko				
![image](https://lptue.github.io/WuFort/images/94ec70fe23646189dcf93388568a6355.png)


Khi này dường như nội dung của file đang bị mã hóa ( vô nghĩa )			
	--> Ta hãy thử chạy lệnh như Pico đã cho			
![image](https://lptue.github.io/WuFort/images/f176ef321a4574be39a7d942b965f7cf.png)


Siuuuuu
