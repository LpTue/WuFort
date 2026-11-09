---
title: UnforgottenBits
tags: ["PicoCTF_Hard"]
---

Tải bài tập tại [đây](https://learn.cylabacademy.org/library/383?page=1&category=4&difficulty=3&workspace=true)

Đầu tiên lần theo thư mục `home\yone\irclogs\01\04\#avidreader13.log`

![image](https://lptue.github.io/WuFort/images/8f4c89dfae88ab21bc0a02507040c536.png)

Ta thấy đầu tiên dùng steghide sau đó liên quan tới mã hóa AES
Hướng tới thư mục `home\yone\gallery`
Ta sử steghide được 3 ảnh `1.bmp`, `2.bmp`, `3.bmp`

![image](https://lptue.github.io/WuFort/images/5a1bdb9190b4fd4789efa852d3ae186c.png)

Ta thu được 3 file với chuỗi ký tự rất lạ, dựa vào đoạn hội thoại, ta sử dụng decryt AES online

![image](https://lptue.github.io/WuFort/images/e69a85465fb2f9133b1d218d4ff6a3a2.png)

Khi dịch cả 3 file, ta thấy đây đều là cốt truyện game LOL --> rác
Truy cập theo đường dẫn `home\yone\notes\3.txt`

![image](https://lptue.github.io/WuFort/images/469a5783d7cf0b6a7091cc07f258bbce.png)

Ta thấy đoạn pass bị khuyết mất phía sau
Dựa vào gợi ý 

![image](https://lptue.github.io/WuFort/images/8a3f65bbe2f7d145a33ddc61600ef620.png)

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

![image](https://lptue.github.io/WuFort/images/381b5213ed276e7b05b86154dfd49804.png)

Ta dùng stegseek để tấn công wordlist

![image](https://lptue.github.io/WuFort/images/25ce4bfe9fd8b3fa401b1dc9b242e16a.png)

Ta thu được một file bị mã hóa AES

![image](https://lptue.github.io/WuFort/images/9c3ce3eef1534b8b61f2e055a871cd98.png)

Nhưng khóa ko khớp --> tìm khóa thay thế

![image](https://lptue.github.io/WuFort/images/10ac50aed3da07d57d0ffd1c8f287106.png)

Dựa vào gợi ý ta tìm được 
Mở file slack tại đường dẫn `home\yone\notes\1.txt-slack`

![image](https://lptue.github.io/WuFort/images/718ac9d522a270482b89555f862f1feb.png)

Tiếp tục tra tiếp `home\yone\.lynx\browsing-history.log`

![image](https://lptue.github.io/WuFort/images/391dce1e602f5bc9839f2c021820a164.png)

Ta thấy có tìm hiểu về `Golden_ratio_base`

![image](https://lptue.github.io/WuFort/images/9d91f6cdf00784b037f74a0bd9c6b60f.png)

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

![image](https://lptue.github.io/WuFort/images/59401a870f60b9c88419d82e887692c6.png)

Ta dùng key và iv mới để decrypt

![image](https://lptue.github.io/WuFort/images/28f5789a2b6cf5943d4ea6b1e7e80a6d.png)

Flag là: `academy{f473_53413d_e0c91991}`
