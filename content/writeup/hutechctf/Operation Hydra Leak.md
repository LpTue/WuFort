---
title: Operation Hydra Leak
tags: ["HuTechCTF"]

---

Tải bài tập tại [đây](https://brotherctf.com/practice/operation-hydra-leak)

Đầu tiên đọc vào `Protocol Hierarchy` thấy xuất hiện có giao thức `dns`,`http`,`icmp`
Ta phân tích từng giao thức một

![image](https://lptue.github.io/WuFort/images/c8a09abb37507a7ec02b62e7.png)

Với `dns` ta thấy có 2 đặc điểm lạ sau
> Có 5 gói tin ip.src == 8.8.8.8
> Và số lượng gói tin xuất hiện này ít bất thường so với những gói còn lại

![image](https://lptue.github.io/WuFort/images/302794c247c007045c946915.png)

Được đoạn `wir3sh4rk_`

![image](https://lptue.github.io/WuFort/images/415fbecb33b81cd2cb141a8b.png)


Với `icmp` ta cũng thấy những điểm bất thường sau
> Các gói khác có độ dài 60 nhưng có những gói độ dài 31

![image](https://lptue.github.io/WuFort/images/4ab0e4878743525fdcda111d.png)

![image](https://lptue.github.io/WuFort/images/0a4005a7642f4523eb5479f9.png)

Ta lọc với `tshark` để lấy seq và data
Ta sắp xếp lại theo seq được chuỗi `50434f45574b4a4e4a554132444647534c49414259345145`

![image](https://lptue.github.io/WuFort/images/369eeb78e35080dfb140d239.png)

Được nửa sau `duuduududu}`

![image](https://lptue.github.io/WuFort/images/37e644278c2abcc25037adad.png)

Với http ta thấy những điểm bất thường 
> Có [PSH,ACK] nhưng khi lần theo stream ko thấy, export http thì dường như file đang bị chia nhỏ và wireshark ko nhận diện được
> Điểm chung các file là đều chung ip.src và ip.dst nhưng khác port --> lí do lần theo tcp stream ko được

![image](https://lptue.github.io/WuFort/images/1ec3832885c0065236c7959f.png)

![image](https://lptue.github.io/WuFort/images/35d6f99576b1f1463fa752bd.png)
 
Ta thấy dữ liệu này dường như đang chứa mã hex, ta decode lại

![image](https://lptue.github.io/WuFort/images/130d1f2461ac5433503c5694.png)

Vậy flag là : `HUTECHCTF{b4by_wir3sh4rk_duuduududu}`