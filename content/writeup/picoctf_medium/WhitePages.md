---
title: WhitePages
tags: ["PicoCTF_Medium"]
---

Tải bài tập tại [đây](https://learn.cylabacademy.org/library/51?page=5&category=4&difficulty=2&workspace=true)

Đầu tiên mở bằng hex ta thấy 3 chuỗi `â€ƒ` luôn đi chung với nhau

![image](https://lptue.github.io/WuFort/images/68374d956739341ad70d56b019f3ca1d.png)

Sau tìm hiểu ta biết được đó là `em space`
Vậy file kia gồm 2 loại đó là `em space` và `normal space`
Ta viết code để chuyển thử về 0 và 1

```py=
fi = open("whitepages.txt","r")
chuoi = fi.readline()

bin = ""
binsau = ""
t = 0
for i in chuoi :
    if i == "â" or i == "€" or i == "ƒ":
        bin += "0"
    else:
        bin += "1"

for i in bin :
    if i == "0":
        t += 1
        if t == 3:
            binsau += "0"
            t = 0
    else:
        t = 0
        binsau += "1"

print(binsau)
```

![image](https://lptue.github.io/WuFort/images/9c86b7145f4862b2a0263b561d2b74e2.png)

Flag là : `academy{not_all_spaces_are_created_equal_743510e5f5459071ed7d4109b7832a8e}`


