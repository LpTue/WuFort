---
title: American bee
tags: ["BKSec"]

---

Tải bài tập tại [đây](https://training.bksec.vn/api/files/3bfcffe4-ef84-48c6-8b6d-fd1f8d279152)

# I. Phổ cập kiến thức
Với một pcap usb, ta sẽ có 3 cách import ra flag

![image](https://hackmd.io/_uploads/S1plLlXhze.png)

Thêm nữa là host gửi dữ liệu để hỏi coi chuột hay bàn phím có dữ liệu không
Nên sẽ có lúc dữ liệu trống, lúc thì có dữ liệu
Có thể coi video để hiểu cách usb giao tiếp [tại đây](https://www.youtube.com/watch?v=_ysUxOKyGGU&t=302s)


# II. Phân tích
Đầu tiên ta thấy host đang giao tiếp tới 2 thiết bị

![image](https://hackmd.io/_uploads/rydFveX3Gg.png)

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

![image](https://hackmd.io/_uploads/ryawue7nze.png)

Ta được flag là : `BKSEC{n4ughty_bee_fr0m_AMERIKAAA}`
