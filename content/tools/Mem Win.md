---
title: Mem Win
tags: ["Tools"]
---

# I. Giới thiệu
- Bài nào yêu cầu phân tích memory --> sử dụng vol
- Đầu tiên ta cần tạo môi trường ảo để tải

```=
cd ~
python3 -m venv mt
source ~/mt/bin/activate
pip install --upgrade pip
pip install volatility3
```

- File hướng dẫn `vol` : tại [đây](https://github.com/LpTue/Forensics/blob/main/L%C6%B0u%20tr%E1%BB%AF/vol.html)
- Cấu trúc cú pháp đơn giản
```=
vol -f <file mem> <option>
```

# II. Plugin mở rộng
### Plugin bitlocker

```=
# 1. Clone plugin
cd ~
git clone https://github.com/lorelyai/volatility3-bitlocker.git

# 2. Copy file plugin vào đúng thư mục
cp ~/volatility3-bitlocker/bitlocker.py <path>
```

![image](https://hackmd.io/_uploads/ryT68W16Ge.png)

`vol -f mem.raw windows.bitlocker.BitlockerFVEKScan --dislocker` : Trích xuất FVEK
