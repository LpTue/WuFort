---
title: American bee
tags: ["BKSec"]

---

Tải bài tập tại [đây](https://training.bksec.vn/challenges/15)

# I. Phổ cập kiến thức
Với một pcap usb, ta sẽ có 3 cách import ra flag

![image](https://lptue.github.io/WuFort/images/eba8fb3a7509e141a18b0e55e0152673.png)

Thêm nữa là host gửi dữ liệu để hỏi coi chuột hay bàn phím có dữ liệu không
Nên sẽ có lúc dữ liệu trống, lúc thì có dữ liệu
Có thể coi video để hiểu cách usb giao tiếp [tại đây](https://www.youtube.com/watch?v=_ysUxOKyGGU&t=302s)


# II. Phân tích
Đầu tiên ta thấy host đang giao tiếp tới 2 thiết bị

![image](https://lptue.github.io/WuFort/images/6c25120acad680a00cb7e66a55ade87c.png)

Ta sử dụng công cụ [này](https://github.com/Nissen96/USB-HID-decoders) để lấy dữ liệu 

Ta tạo một môi trường ảo
```=
cd ~
python3 -m venv usbinput
```
Ta chạy môi trường ảo để tải tool
Và chạy các lệnh
```=
git clone https://github.com/Nissen96/USB-HID-decoders.git
cd USB-HID-decoders
pip install -r requirements.txt
```

```=
./extract_hid_data.sh AA.pcapng
```
```=
python keyboard_decode.py usbdata-5.3.1.txt
```

![image](https://lptue.github.io/WuFort/images/75995531718c1e8fccf9b89eb88c1490.png)

Ta được flag là : `BKSEC{n4ughty_bee_fr0m_AMERIKAAA}`
