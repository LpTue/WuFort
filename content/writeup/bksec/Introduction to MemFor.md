---
title: Introduction to MemFor
tags: ["BKSec"]

---

Tải bài tập tại [đây](https://training.bksec.vn/challenges/165)

Sử dụng vol 3 thay vì vol 2 để tăng tốc
```vol=
cd ~
python3 -m venv mt
source mt/bin/activate
pip install --upgrade pip
pip install volatility3
```

Di chuyển tới nơi lưu trữ file
Lấy thông tin của image
```=
vol -f memdump.mem windows.info.Info
```

![image](https://lptue.github.io/WuFort/images/b81d63c27ca3c51b4c2c376dda5b3401.png)

Ta có được thông tin phiên bản là **`10`** và múi giờ khi chuyển về VN là **`2025-02-20 22:05:26`**

Để kiểm tra phần mền đáng ngờ

```=
vol -f memdump.mem windows.pslist.PsList
```
Ta chú ý tới pid 8144

![image](https://lptue.github.io/WuFort/images/53c413a2dc935c819d644c42a395c03f.png)

Giải thích
> Bình thường sẽ là `svchost` thay vì là `svcost`

Để tìm pid cha thì ta chú ý tới ppid là 8268

![image](https://lptue.github.io/WuFort/images/222fb32b8745ec4b69a0c3cbd89333d8.png)

Ta kiểm tra các lệnh được chạy
```=
vol -f memdump.mem windows.cmdline.CmdLine
```

Ta chú ý tới dòng gần cuối thấy

![image](https://lptue.github.io/WuFort/images/55b323dcc66c2038028a0e271d2adcc4.png)

Để scan network ta chạy

```=
vol -f memdump.mem windows.netscan.NetScan
```

Ta chú ý tới tiến trình chạy bởi `svcost.exe`

![image](https://lptue.github.io/WuFort/images/a37ae5c271c472cacef5cdd73674ec2b.png)

Flag ẩn gồm 2 phần 
Ta kiểm tra các file có thể

```=
vol -f memdump.mem windows.filescan | grep -iE "flag|part|secret|\.txt|\.png|\.jpg|\.flag"
```

![image](https://lptue.github.io/WuFort/images/eed685792a9d0e1188e3a2b64df25583.png)

Ta thấy có 2 file đáng nghi là flag1 và flag2
Ta tạo 1 folder tạm thời lưu các file mới

```=
vol -f memdump.mem -o <TemFolder> windows.dumpfiles --virtaddr <Mã>
```

Ví dụ 
```=
vol -f memdump.mem -o tem windows.dumpfiles --virtaddr 0xd20dfd1244c0

vol -f memdump.mem -o tem windows.dumpfiles --virtaddr 0xd20dfd97a640

vol -f memdump.mem -o tem windows.dumpfiles --virtaddr 0xd20dfdc24e00
```

Sau khi vào ta chỉnh lại về đúng định dạng

![image](https://lptue.github.io/WuFort/images/7dfea3d4d6dab596c4d8f9ad344e4ad2.png)

Vì file flag1 ko extract được nên ta dùng cách kiểm tra mã hex

![image](https://lptue.github.io/WuFort/images/e5a36c47da6023c882ca1805d2d8f6c9.png)

Đoạn đầu là : `BKSEC{l00k_ljk3_w3_h4v3_a_n3w_`

Với file exe ta mở bằng cutter

![image](https://lptue.github.io/WuFort/images/32e5a608f75149b30f6fe9b6cb4dd1dc.png)

Đoạn sau là : `vol4tilitY_m4st3r_c0mjn9_in2_t0wn}`
Ta kiểm tra với file còn lại thì cũng thế
Vậy mã cuối là : `BKSEC{l00k_ljk3_w3_h4v3_a_n3w_vol4tilitY_m4st3r_c0mjn9_in2_t0wn}`

![image](https://lptue.github.io/WuFort/images/5455cd9a16ac4492bd5e4c22498d1139.png)

![image](https://lptue.github.io/WuFort/images/3328a0510901fd272552f53d883a9e8c.png)

Flag cuối cùng là : `BKSEC{1e70e595ccc9f7ac9ccae129561c5f862d0f7e43d38210ba46dc6076363f9daf}`