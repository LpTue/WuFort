---
title: Corrupted file
tags: ["PicoCTF_Easy"]
---

Đầu tiên mở file bằng hex, thấy phần đầu là JFIF  
Khi ta thay đuôi bằng .jpg thì báo lỗi     
![image](/images/283906ec238beebd5f34d635e954a7e7.png)

Đây là một điều khá lạ bởi nếu đúng thì sửa đuôi phải ra  
Thêm nx phân tích đoạn văn bản thấy nó đúng kiểu ko thể đọc bằng ASCII  
	--> Nghĩ đến trường hợp có thể sai định dạng văn bản  
Truy cập https://gist.github.com/leommoore/f9e57ba2aa4bf197ebc5
![image](/images/83d52da9ae051615835cb3c7917daf77.png)


Ta phát hiện đoạn đầu đúng của ảnh JFIF có dạng : ffd8 ffe0 0010 4a46 4946 0001 0101 0047 theo như github nói  
Ta thay lại đoạn đầu bằng mã hex kia  
Sau đó ta đổi lại đuôi file   
![image](/images/975b56271375d331e58e2c306b3c8499.png)

