---
title: Verify
tags: ["PicoCTF_Easy"]
---

Đầu tiên ta hãy kết nối tới server 
![image](https://hackmd.io/_uploads/SyVuKoZOfg.png)

Ta hãy thử dịch các gợi ý của bài tập
![image](https://hackmd.io/_uploads/SkcqtobdMx.png)



Định hướng lúc này :			
	- Đầu tiên thử kiểm tra checksum và sha256 xem có trùng khớp ko			
	- Nếu tìm thấy file, ta sẽ tiếp tục kiểm tra file hoặc chạy lệnh giải mã			

![image](https://hackmd.io/_uploads/rk4jYoWOfl.png)


Khi chạy lệnh, có thể thấy có rất nhiều mã mà ta phải kiểm tra				
	--> Có thể dùng grep để lọc checksum mà ta cần				
![image](https://hackmd.io/_uploads/ryXnFoWdGe.png)


Lúc này khi đã tìm được file, ta tiến hành kiểm tra file có nội dung ko				
![image](https://hackmd.io/_uploads/HySpYiW_Ge.png)


Khi này dường như nội dung của file đang bị mã hóa ( vô nghĩa )			
	--> Ta hãy thử chạy lệnh như Pico đã cho			
![image](https://hackmd.io/_uploads/ByzRYibdfl.png)


Siuuuuu
