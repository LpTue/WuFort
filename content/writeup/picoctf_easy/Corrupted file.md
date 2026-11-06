---
title: Corrupted file
tags: ["PicoCTF_Easy"]
---

Đầu tiên mở file bằng hex, thấy phần đầu là JFIF  
Khi ta thay đuôi bằng .jpg thì báo lỗi     
![image](https://hackmd.io/_uploads/BJBMl3-OGx.png)

Đây là một điều khá lạ bởi nếu đúng thì sửa đuôi phải ra  
Thêm nx phân tích đoạn văn bản thấy nó đúng kiểu ko thể đọc bằng ASCII  
	--> Nghĩ đến trường hợp có thể sai định dạng văn bản  
Truy cập https://gist.github.com/leommoore/f9e57ba2aa4bf197ebc5
![image](https://hackmd.io/_uploads/B1f4lhWdMe.png)


Ta phát hiện đoạn đầu đúng của ảnh JFIF có dạng : ffd8 ffe0 0010 4a46 4946 0001 0101 0047 theo như github nói  
Ta thay lại đoạn đầu bằng mã hex kia  
Sau đó ta đổi lại đuôi file   
![image](https://hackmd.io/_uploads/rkAEenWuze.png)

