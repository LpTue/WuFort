---
title: DDNNNNSS
tags: ["BKSec"]

---

Tải bài tập tại đây [đây](https://training.bksec.vn/challenges/34)

Mở bằng Hierarchy thấy nhiều packet DNS + tên đề bài nhấn mạnh vào dns 
Ta lọc dns

![image](https://lptue.github.io/WuFort/images/c99345d1d629f868ae71f832a3fbf024.png)

Ta lướt thấy nhiều req từ ip 198.168.1.100 
Ta lọc `ip.src == 198.168.1.100 and dns`

![image](https://lptue.github.io/WuFort/images/eba9fb1ce4bc06eb65a0c64558e3df4e.png)

Ta để ý nội dung tuân theo cú pháp `seq<số>.<chuỗi nhìn giống hex>.1337xBetbkseccom`
Ta lọc lấy nhanh nội dung bằng Tshark

![image](https://lptue.github.io/WuFort/images/24167bc7ace249ae54fd2eb26c0b8ad6.png)

Ta viết code để lấy đoạn mã
```py=
fi = open("out.txt","r")
s = ""
for i in range(1,147):
    a = fi.readline()
    b = a[88:96]
    s += b

print(s)
```

Ta dùng cyberchef thấy ko nhận diện nên cần kiểm tra lại
Lấy ví dụ với `d3523319` thì trong đó có `5233` nằm trong dải ASCII đọc được (từ 20 đến 7E)
Ta sử lại code

```py=
fi = open("out.txt","r")
s = ""
for i in range(1,147):
    a = fi.readline()
    b = a[90:94]
    s += b

print(s)
```

![image](https://lptue.github.io/WuFort/images/17d61aca2ee751600c4dabc83f79bb80.png)

Flag là: `BKSEC{dns_3xf1ll_is_n0t_a_b4d_choic3}`