---
title: DDNNNNSS
tags: ["BKSec"]

---

Tải bài tập tại đây [đây](https://training.bksec.vn/challenges/34)

Mở bằng Hierarchy thấy nhiều packet DNS + tên đề bài nhấn mạnh vào dns 
Ta lọc dns

![image](https://hackmd.io/_uploads/H1MPWhBTGe.png)

Ta lướt thấy nhiều req từ ip 198.168.1.100 
Ta lọc `ip.src == 198.168.1.100 and dns`

![image](https://hackmd.io/_uploads/BybkG2HpGe.png)

Ta để ý nội dung tuân theo cú pháp `seq<số>.<chuỗi nhìn giống hex>.1337xBetbkseccom`
Ta lọc lấy nhanh nội dung bằng Tshark

![image](https://hackmd.io/_uploads/rk4OMnHaMe.png)

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

![image](https://hackmd.io/_uploads/HJOuShSaze.png)

Flag là: `BKSEC{dns_3xf1ll_is_n0t_a_b4d_choic3}`