---
title: UnforgottenBits
tags: ["PicoCTF_Hard"]
---

Tải bài tập tại [đây](https://learn.cylabacademy.org/library/383?page=1&category=4&difficulty=3&workspace=true)

Đầu tiên lần theo thư mục `home\yone\irclogs\01\04\#avidreader13.log`

![image](https://hackmd.io/_uploads/Bym_zjcpGe.png)

Ta thấy đầu tiên dùng steghide sau đó liên quan tới mã hóa AES
Hướng tới thư mục `home\yone\gallery`
Ta sử steghide được 3 ảnh `1.bmp`, `2.bmp`, `3.bmp`

![image](https://hackmd.io/_uploads/rJAG7icpfg.png)

Ta thu được 3 file với chuỗi ký tự rất lạ, dựa vào đoạn hội thoại, ta sử dụng decryt AES online

![image](https://hackmd.io/_uploads/SJv1Ei5pfe.png)

Khi dịch cả 3 file, ta thấy đây đều là cốt truyện game LOL --> rác
Truy cập theo đường dẫn `home\yone\notes\3.txt`

![image](https://hackmd.io/_uploads/ryu4Ksqazl.png)

Ta thấy đoạn pass bị khuyết mất phía sau
Dựa vào gợi ý 

![image](https://hackmd.io/_uploads/SJ1uKj5afe.png)

Ta thấy pass nối thêm tên 2 vị tướng LOL
Tải danh sách tướng tại [đây](https://github.com/jetnew/league-tools/blob/master/champion_list.txt)

```py=
fi = open("champion_list.txt","r")
fo = open("pass.txt","w")
l =[]
mk = []

for i in range(1,149):
    a = fi.readline().strip().lower()
    l.append(a)

for i in range(0,148):
    for j in range(0,148):
        s = "yasuoaatrox" + str(l[i]) + str(l[j]) + "\n"
        fo.write(s)
```

![image](https://hackmd.io/_uploads/H1PH9iqTGe.png)

Ta dùng stegseek để tấn công wordlist

![image](https://hackmd.io/_uploads/BJrccocTMe.png)

Ta thu được một file bị mã hóa AES

![image](https://hackmd.io/_uploads/Bkyh5s5Tze.png)

Nhưng khóa ko khớp --> tìm khóa thay thế

![image](https://hackmd.io/_uploads/BJpaqic6ze.png)

Dựa vào gợi ý ta tìm được 
Mở file slack tại đường dẫn `home\yone\notes\1.txt-slack`

![image](https://hackmd.io/_uploads/B1S-oj5TGe.png)

Tiếp tục tra tiếp `home\yone\.lynx\browsing-history.log`

![image](https://hackmd.io/_uploads/Bklvooqpzx.png)

Ta thấy có tìm hiểu về `Golden_ratio_base`

![image](https://hackmd.io/_uploads/BkaYjo9aMe.png)

Lấy ví dụ `100` thì số sẽ là $\ (φ)^2$ tại số 1 ở vị trí số 2 từ dưới lên
Dựa vào tư duy này, ta code để dịch ngược về số

```py=
import math

fi = open("ma.txt","r")
fo = open("out.txt","w")
l = fi.read().split(".")
grb = 0.5 * (1 + math.sqrt(5))

def tt(n):
    n1 = n[::-1]
    t = 0
    for i in range(0,len(n)):
        if n1[i] == "1":
            t += pow(grb,i)
    return t

# các hằng số nhiễu: không có, φ^11, φ^12, phi^13
nhieu = [0, 199, 322, 521]

kq = ""
for i in l:
    a = math.ceil(tt(str(i)) - 0.000001) 
    for f in nhieu:
        if 1 <= a - f <= 126:            
            a = a - f
            break
    kq += chr(a)

print(kq)
fo.write(kq)
```

Thuật toán sẽ dịch từ mã 0 và 1 qua số nguyên
Với những số quá lớn, trừ dần cho tới khi về giá trị hợp lý (dưới 126 mà có thể hiển thị )
Sau đó sẽ chuyển lại về char

![image](https://hackmd.io/_uploads/H1vipi5pzg.png)

Ta dùng key và iv mới để decrypt

![image](https://hackmd.io/_uploads/Bk70TiqaGg.png)

Flag là: `academy{f473_53413d_e0c91991}`
